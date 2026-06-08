Title: Next-Gen orientation: supporting international students with generative AI NPCs in VR

Source PDF: /Users/mac/Documents/6-Research/4-SpatialAgent-Survey/assets/survey_paper/pdfs/phase1_adjacent/14_TW-13_TUMSphere_Next_Gen_Orientation_2026.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T03:19:56+00:00
- page_count: 21
- status: ok
- text_char_count: 95634

Metadata:
- author: Santiago Berrezueta-Guzman
- doi: unknown
- keywords: Convai; educational games; virtual reality; lip-sync; LLMS; NPCs; speech recognition; speech-to-text
- subject: Berrezueta-Guzman S and Wagner S (2026) Next-Gen orientation: supporting international students with generative AI NPCs in VR. Front. Comput. Sci. 8:1799323. doi: 10.3389/fcomp.2026.1799323

Outline:
- Next-Gen orientation: supporting international students with generative AI NPCs in VR (page 1)
  - 1 Introduction (page 1)
  - 2 Related work (page 2)
    - 2.1 LLM-powered NPCs in educational virtual reality (page 2)
    - 2.2 Virtual campus tours for university orientation (page 3)
  - 3 System architecture and design (page 4)
    - 3.1 TUMSphere platform overview (page 4)
      - 3.1.1 Game environment description (page 4)
      - 3.1.2 Educational objectives and game mechanics (page 5)
      - 3.1.3 Target user group (page 5)
      - 3.1.4 Inclusivity-driven design rationale (page 6)
    - 3.2 LLM integration architecture (page 6)
      - 3.2.1 Overall system design (page 6)
      - 3.2.2 Component interaction and data flow (page 6)
    - 3.3 Technical stack (page 7)
      - 3.3.1 Unreal engine (page 7)
      - 3.3.2 VaRest plugin (page 8)
      - 3.3.3 OpenAI GPT models (page 8)
      - 3.3.4 Convai plugin (page 8)
      - 3.3.5 ReadyPlayerMe (page 8)
    - 3.4 Alternative plugins and tools explored (page 8)
  - 4 Methodology and technical implementation details (page 8)
    - 4.1 Initial prototype development in UE as a chatbox with VaREST (page 8)
      - 4.1.1 User interface implementation (page 9)
      - 4.1.2 Input processing (page 9)
      - 4.1.3 API communication architecture (page 9)
    - 4.2 Research insights and system failure modes (page 10)
      - 4.2.1 Design trade-offs: cloud vs. local processing (page 10)
      - 4.2.2 Lessons for generalized VR+LLM systems (page 10)
    - 4.3 Transition to VR and voice integration (page 10)
    - 4.4 Convai platform integration (page 10)
      - 4.4.1 Platform architecture overview (page 10)
      - 4.4.2 Environmental awareness and object interaction (page 11)
    - 4.5 Character configuration through Convai web interface (page 12)
      - 4.5.1 Character creation and ID assignment (page 12)
      - 4.5.2 Character description and backstory (page 12)
      - 4.5.3 Knowledge bank integration (page 13)
      - 4.5.4 Language and speech configuration (page 14)
      - 4.5.5 Personality traits and core AI settings (page 14)
    - 4.6 Character integration with Convai ReadyPlayerMe plugin (page 14)
      - 4.6.1 Plugin installation and setup (page 14)
      - 4.6.2 Character blueprint eeconfiguration (page 14)
      - 4.6.3 Lip Sync and facial animation (page 14)
  - 5 Experimental setup and evaluation (page 14)
    - 5.1 User study design (page 15)
      - 5.1.1 Participants and demographics (page 15)
      - 5.1.2 Apparatus and environment (page 15)
      - 5.1.3 Experimental procedure (page 15)
      - 5.1.4 Metrics and questionnaires (page 15)
      - 5.1.5 Statistical reliability analysis (page 15)
    - 5.2 Performance evaluation (page 15)
      - 5.2.1 Latency measurement methodology (page 15)
      - 5.2.2 System resource profiling (page 16)
      - 5.2.3 Quantitative Lip-sync assessment (page 16)
  - 6 Results (page 16)
    - 6.1 System performance and latency analysis (page 16)
      - 6.1.1 Response latency (Time-to-Audio) (page 16)
      - 6.1.2 Frame rate stability (page 16)
      - 6.1.3 Lip-sync synchronization accuracy (page 16)
    - 6.2 User experience and usability (page 17)
      - 6.2.1 Task completion rates (page 17)
      - 6.2.2 Psychometric scores (page 17)
      - 6.2.3 Instrument reliability (page 17)
    - 6.3 Qualitative findings (page 18)
      - 6.3.1 Theme 1: reduced social anxiety in language learning (page 18)
      - 6.3.2 Theme 2: the ``Thinking'' silence (page 18)
      - 6.3.3 Theme 3: spatial guidance vs. verbal instructions (page 18)
      - 6.3.4 Negative case analysis (page 18)
  - 7 Discussion (page 18)
    - 7.1 Reducing social anxiety through artificial interlocutors (page 18)
    - 7.2 The latency-presence trade-off (page 18)
    - 7.3 Embodiment and spatial agency (page 18)
    - 7.4 Limitations (page 19)
  - 8 Conclusion (page 19)
  - 9 Future directions (page 19)
    - 9.1 Enhancing interaction fluidity and non-verbal realism (page 19)
    - 9.2 Structured pedagogy through hybrid narrative design (page 19)
    - 9.3 Environmental awareness, persistence, and scalability (page 19)
  - Data availability statement (page 20)
  - Ethics statement (page 20)
  - Author contributions (page 20)
  - Funding (page 20)
  - Conflict of interest (page 20)
  - Generative AI statement (page 20)
  - Publisher's note (page 20)
  - References (page 20)

Markdown Content:

TYPE OriginalResearch
PUBLISHED 12March2026
DOI 10.3389/fcomp.2026.1799323
Next-Gen orientation: supporting
international students with
OPENACCESS
generative AI NPCs in VR
EDITEDBY
SalvadorOtónTortosa,
UniversityofAlcalá,Spain
REVIEWEDBY SantiagoBerrezueta-Guzman* andStefanWagner
VladimirRobles-Bykbaev,
SalesianPolytechnicUniversity,Ecuador ChairofSoftwareEngineering,TechnicalUniversityofMunich,Heilbronn,Germany
MartínLópezNores,
UniversityofVigo,Spain
Educational Virtual Reality (VR) provides immersive learning environments, yet
*CORRESPONDENCE
SantiagoBerrezueta-Guzman most contemporary applications rely on pre-scripted Non-Player Characters
s.berrezueta@tum.de (NPCs) that offer limited personalization and rigid interaction paths. This study
RECEIVED29January2026 presents the technical implementation and evaluation of TUMSphere, a VR
REVISED19February2026
ACCEPTED20February2026 orientation platform designed to facilitate the academic and cultural transition
PUBLISHED12March2026 of international students. We propose a modular architecture that integrates
CITATION Large Language Models (LLMs) with Unreal Engine via the Conversational
Berrezueta-GuzmanSandWagnerS
AI (Convai) platform, enabling embodied NPCs to provide real-time speech
(2026)Next-Genorientation:supporting
internationalstudentswithgenerativeAI recognition, context-aware dialogue, and autonomous spatial navigation. To
NPCsinVR. validate this approach, a mixed-methods user study (N = 24) was conducted
Front.Comput.Sci.8:1799323.
with international students to assess system latency, usability, and pedagogical
doi:10.3389/fcomp.2026.1799323
efficacy. Results demonstrate a high System Usability Scale (SUS) score of
COPYRIGHT 76.4 (SD = 12.5) and robust task completion rates, reaching 100% for spatial
©2026 Berrezueta-Guzmanand
Wagner.Thisisanopen-accessarticle navigation and 96% for information retrieval. While technical benchmarking
distributedunderthetermsofthe revealed an average end-to-end latency of 2.90s for complex, retrieval-heavy
CreativeCommonsAttributionLicense
queries,qualitativefindingsindicatethatusersfindthis“latency-presencetrade-
(CCBY).Theuse,distributionor
reproductioninotherforumsis off”acceptableinexchangeforthepedagogicalbenefits.Crucially,participants
permitted,providedtheoriginalauthor(s) reportedasignificantreductioninsocialanxietywhenpracticinglanguageand
andthecopyrightowner(s)arecredited
administrative queries with AI agents compared to human interlocutors. These
andthattheoriginalpublicationinthis
journaliscited,inaccordancewith findingssuggestthatembodied,generativeAINPCscanserveasascalable,low-
acceptedacademicpractice.Nouse, pressure“socialsandbox”thateffectivelyredefinesstudentsupportsystemsand
distributionorreproductionispermitted
orientationstrategiesinhighereducation.
whichdoesnotcomplywiththeseterms.
KEYWORDS
Convai, educational games, virtual reality, lip-sync, LLMS, NPCs, speech recognition,
speech-to-text
1 Introduction
In recent years, educational Virtual Reality (VR) gaming has emerged as a powerful
formoflearningthatimmersesstudentsinsideinteractivevirtualworldswheretheycan
explore, experiment, test theories, and practice skills (Lin et al., 2024; Damianova and
Berrezueta-Guzman,2025).EducationalVRgamescanoftenbecategorizedintoseveral
types,includingvirtuallaboratorieswherestudentsconductscientificexperimentssafely
(Truchly et al., 2018; Konecki et al., 2023), historical simulations that allow learners
to walk through ancient civilizations, language learning environments where students
practice conversations in virtual cafes or shops (Hua and Wang, 2023; Peixoto et al.,
2021), and professional training simulations for fields such as medicine or engineering
FrontiersinComputerScience 01 frontiersin.org

Berrezueta-GuzmanandWagner 10.3389/fcomp.2026.1799323
(Du et al., 2025). VR has also gained relevance for remote and This paper presents the implementation and use-case study
distance education, particularly following the widespread shift to of AI-powered NPCs in TUMSphere, a novel educational
online learning (Levidze, 2024). The growth in educational VR virtualrealityplatformforfirst-semesterInformationEngineering
has been remarkable in recent years, with the market expected students. TUMSphere is a virtual campus environment that
to expand by USD 81.13 billion from 2025 to 2030 (Mordor combineseducationalmini-games,codingpuzzles,andrelaxation
Intelligence,2024). activitiesdesignedtohelpstudentsdevelopproblem-solvingskills
Most educational VR games that exist today rely on pre- while providing an engaging campus experience. This paper
designed scenarios with scripted interactions (Lin and Cheng, specifically focuses on the integration and implementation of
2024). Users might need to click on objects to read information, intelligent NPCs powered by large language models (LLMs)
follow predetermined quest paths, or interact with simple menu- within this platform. These conversational NPCs enable students
based systems. Some games include basic non-player characters to interact naturally via voice, providing personalized guidance
(NPCs) that guide, usually with pre-recorded voice lines or text on university services, answering questions, and supporting
bubbles,similartotraditionalvideogames.Forexample,astudent international students’ cultural adaptation. The implementation
exploring a virtual chemistry lab might click equipment to see leverages Unreal Engine and specialized conversational AI
explanations,followstep-by-stepinstructionsdisplayedon-screen, (convAI) plugins to create responsive, context-aware virtual
or receive feedback via pop-up messages when completing tasks charactersthataddressstudents’uniqueinformationneedsduring
(Viitaharju et al., 2023). While these approaches can also be theirinitialuniversityexperience.
engaging and educational, they create rigid experiences in which
students can access only information that developers specifically
programmed into the system, which is not personalized or offers
2 Related work
real-timeinteractions.
Meanwhile, large language models (LLMs) represent a
TobridgethegapbetweentheoreticalAImodelsandpractical
significant advancement in artificial intelligence’s (AI) ability to
immersiveeducation,thissectionsituatesourresearchwithinthe
understand and generate human language (Minaee et al., 2024;
broaderlandscapeofintelligentvirtualenvironments.
Wangetal.,2025).Thesemodels,suchasGPT(Leon,2025),are
trainedonextensivetextdatasetsandcanengageinconversations,
answerquestionsacrossvariousdomains,andprovidecontextual
2.1 LLM-powered NPCs in educational
explanations. In educational settings, LLMs have demonstrated
potential as adaptive tutoring systems, capable of responding to virtual reality
individual student queries and tailoring explanations to learner
needs (Chen et al., 2023; Wen et al., 2024; Dong et al., 2024). Recent research has explored various LLM implementations
Unlike traditional rule-based educational software that relies in VR settings, with a particular focus on conversational agents
on pre-programmed decision trees, LLMs can process natural that provide personalized guidance, support natural language
language input, maintain conversation context, and generate interactions,andadapttolearners’needsinrealtime.
relevant responses in real-time (Tracy and Spantidi, 2025). McKernetal.,presentaninnovativeapproachtocreatingAI-
Recent research has explored the applications of LLMs, such as powered digital assistants in VR environments by coupling two
ChatGPT, in classrooms, where they serve as teaching assistants, distinct AI systems: a Language Model (LM) for conversational
helpingstudentsunderstandcomplextopics,providingfeedbackon responses and a Movement Model (MM) for generating context-
assignments,andsupportingpersonalizedlearningacrossvarious relevant body movements. Their system employs a dual-channel
subjects(Husseinetal.,2024;Chenetal.,2024). LMarchitecture,withonechannelrespondingtouserqueries.At
Thus, this is where the intersection of LLMs and VR thesametime,theotherprovidestextinputtotheMM,enabling
environmentsoccurs,integratingintelligentNPCsintoeducational thegenerationofcoordinatedmovementsthatcomplementverbal
VR environments, which play a critical role in creating more communication. The authors implemented a proof-of-concept
dynamic and personalized learning experiences (Gonzales et al., prototype using GPT-3.5-turbo as the LM and a text-to-motion
2025; Wan et al., 2024). Intelligent NPCs powered by LLMs model based on the HumanML3D dataset, deployed in Unreal
that respond to user needs in real-time are highly valuable Engine5.5forvisualization.Inapreliminaryuserstudywithnine
for virtual training simulations, educational platforms, and even participants,theAI-generatedNPCswereratedsignificantlyhigher
therapy programs (Guevarra et al., 2025). These virtual tutors in understandability than human-recorded movements captured
canintroducestudentstocomplexproblemswhileadaptingtheir with their Avatar Replay System. The study demonstrated that
style to meet the students’ individual needs (Barmpari et al., AI-generated movements were more frequently and accurately
2026). In educational VR, intelligent NPCs simulate real-life identified by users, suggesting potential advantages over motion-
interactions with high realism, understanding and responding to captured animations in terms of clarity and creation efficiency
natural language, exhibiting human-like behavior, and adapting (McKernetal.,2024).
their actions based on student input (Özkaya et al., 2025). ExpandingonthisideaofsocialinteractioninVR,Liuetal.,
Furthermore,AI-enabledNPCscanaddressconcernsaboutlearner present ClassMeta, a GPT-4-powered virtual classmate designed
engagement, anxiety, and cognitive workload during remote topromoteclassroomparticipationinVRthroughpeerinfluence
education(Vallance,2023). behaviors, including note-taking, question-asking/answering,
FrontiersinComputerScience 02 frontiersin.org

Berrezueta-GuzmanandWagner 10.3389/fcomp.2026.1799323
discussion-driving,anddiscipline-reminding.Thesystememploys non-verbal cues, the system moves beyond traditional checklist-
a dual-context architecture, where agents digest lesson materials based simulations to offer authentic, unpredictable interactions.
as background context while capturing real-time classroom A core contribution is the user-friendly design interface, which
conversations.Thisenablesthemtogeneratecontextuallycoherent empowersclinicaleducators—regardlessoftechnicalexpertise—to
responses through both predefined action signals and dynamic customizepatientpersonasbasedonmedicalhistory,literacylevels,
dialogresponsesviaElevenLabstext-to-speech.Inabetween-group andspecificpersonalitytraits(e.g.,openness,agreeableness).While
studywith24participantscomparingClassMetatoabaselineVR the system effectively targets student challenges by personalizing
classroom, agents significantly improved student note quality communication for diverse patient backgrounds, it currently
(p < 0.001), reduced the need for instructor intervention, and requires developers to manually review AI-generated prompts
achievedsignificantlearninggainsinfourofsixkeycompetencies, before deployment to ensure their appropriateness (Zhu et al.,
includinglogicalthinkingskills(Liuetal.,2024). 2025).
Panetal.,introducedELLMA-T,aGPT-4-poweredembodied Hu et al., developed Nurse Town, a Unity-based simulation
agentinVRChatdesignedforsituatedEnglishlanguagelearning. designed to mitigate the clinical training shortage in nursing
Byintegrating levelassessment,dynamicrole-play scenarios,and education through GPT-4o-powered patient avatars. The system
personalized feedback, the system successfully reduced speaking distinguishes itself by featuring 10 randomized personality
anxiety among international graduate students who felt less types (e.g., anxious-emotional, dismissive-overconfident), forcing
judgedthaninhuman-to-humaninteractions.Despiteitscreative students to adapt their communication strategies dynamically.
content generation, the study highlighted significant technical Technically, the platform achieves low-latency (3 s) interactions
hurdlescommontoLLM-VRintegration,specificallyhighresponse usingWhisperSTTandOpenAITTS,complementedbycontext-
latency, rigid turn-taking, and a lack of non-verbal emotional aware synchronized gestures. A key feature is the automated
nuance.Ultimately,theauthorsarguethatwhileELLMA-Tproves assessment component, which uses educator-defined rubrics to
the potential for low-anxiety practice, future development must evaluate clinical accuracy, empathy, and professionalism. While
prioritizeadvancedmemoryarchitecturesandmoresophisticated earlydemonstrationsshowthesystemcaneffectivelydifferentiate
non-verbalcuestosupportlong-term,adaptivelearning(Panetal., betweenstudentperformancelevels,itscurrentlimitationsinclude
2025). a narrow clinical scope (hypertension only), a limited vocal
Luo et al., presented “Study with Confucius,” a ChatGPT- emotionalrange,andalackofformaluserevaluationdata(Huetal.,
powered educational game designed to teach classical Chinese 2025). Table1 presents a summary of related work, highlighting
literaturethroughthreeeducationalmodesthatcombinedifferent theirkeycontributionandtheirlimitations.
AI agent configurations and distinct pedagogical approaches.
The system uses the Unity engine with Prompt Graph to
create modular AI agents with capabilities such as teaching,
2.2 Virtual campus tours for university
verification,itemgeneration,andintelligentjudgment,resultingin
three gameplay levels where players act as Confucius’s disciples, orientation
learning ancient texts through task completion. In a mixed-
methods evaluation involving 32 eighth-graders and 7 high Virtual campus tours have emerged as essential tools
schoolers, the game demonstrated significantly higher knowledge for university marketing and student recruitment, providing
retentionandlearningabsorptioncomparedtotraditionaltextbook prospectivestudentswithimmersivepreviewsofcampusfacilities
methods.Studentsdemonstrateddeepimmersionandunexpected andacademicenvironmentsbeforetheyvisitinperson,orhelping
collaborative behavior during gameplay. However, the results thembecomeaccustomedtotheenvironmentandfeelcomfortable
revealed moderate Flow and Challenge scores, suggesting a high withit.
cognitiveload(Luoetal.,2024). Azizo et al., developed a voice-controlled VR 360 campus
Songetal.,developedLearningverseVR,animmersiveplatform tour for Universiti Teknologi Malaysia (UTM) using IBM
that leverages a hybrid generative AI architecture (combining Watson’s Speech-to-Text API and Unity 3D. The system allowed
GPT-3.5 and a local ChatGPT) to enable scriptless, high- users to navigate nine campus locations via spoken commands,
fidelity NPC interactions. To ensure pedagogical accuracy, the offering a hands-free alternative to controller-based movement.
system employs Retrieval Augmented Generation (RAG) and While participants generally valued the hands-free interaction,
vector databases to mitigate the risk of hallucinations. A key the reliance on cloud-based processing introduced significant
innovation is its dynamic affinity mechanism, which tracks limitations: the system struggled with accent recognition
interactionhistoryacrossfourdimensions—topicrelevance,tone, and background noise, suffered from latency due to internet
taskcompletion,andfrequency—topersonalizeNPCbehaviorover dependency,andcausedmotionsicknessinnearlyhalftheusers.
time. Furthermore, the platform introduces an “LLM ecosystem” These findings highlight the trade-offs between accessibility and
in which diverse agents (world, organic, and inorganic) interact, reliability when employing cloud-dependent speech APIs in
significantlyenhancingenvironmentalimmersionbeyondstandard educationalVR(Azizoetal.,2020).
conversationalagents(Songetal.,2024). Garcia et al., developed the MILES Virtual Tour, a playable
Zhuetal.,introducedVAPS(VirtualAIPatientSimulator),a 3D application for desktop and mobile devices designed to
GPT-4o-poweredVRplatformdesignedtobridgegapsinclinical maximize accessibility by removing the need for VR headsets.
communicationtrainingforHealthProfessions(HP)students.By Using an extended Technology Acceptance Model (TAM) with
utilizing high-fidelity MetaHuman characters with synchronized 104 participants, the study revealed that prospective students
FrontiersinComputerScience 03 frontiersin.org

Berrezueta-GuzmanandWagner 10.3389/fcomp.2026.1799323
TABLE1ComparativeanalysisofgenerativeAIarchitecturesineducationalVR.
Study CoreAIandarchitecture Keycontribution Identifiedlimitations
McKernetal. Dual-Channel(GPT-3.5+ Decouplesspeechandmovementgenerationto Smallsamplesize(N=9);prototypefocusedon
(2024) HumanML3D) createcoordinated,context-awarenon-verbal movementvalidationratherthanfull
behaviors. conversationalflow.
Liuetal.(2024) GPT-4+ElevenLabs(Dual-Context) “ClassMeta”agentsactasvirtualpeerstodrive Reliesonpredefinedactionsignalsforcertain
participationvianote-takinganddiscussion behaviors,specifictoclassroominteraction
prompts. contexts.
Panetal.(2025) GPT-4(VRChatIntegration) SocialVRagentforsituatedlanguagelearning Highresponselatency;rigidturn-takinglogic;lacks
thatsignificantlyreducesspeakinganxiety. emotionalnuanceinnon-verbalcues.
Luoetal.(2024) ChatGPT+PromptGraph(Unity) Modularagentroles(Teacher,Verifier,Judge)for Highcognitiveloadreportedbystudents(moderate
game-basedclassicalliteraturelearning. Flow/Challengescores).
Songetal.(2024) Hybrid(GPT-3.5+LocalChatGLM) “LLMEcosystem”whereOrganic/Inorganic Higharchitecturalcomplexityinvolving
+RAG agentsinteract;usesRAGtominimize synchronizationoflocal/cloudmodelsandmultiple
hallucinations. agenttypes.
Zhuetal.(2025) GPT-4o+MetaHuman User-friendlyconfigurationtoolallowing Scalabilitybottleneck:requiresmanualdeveloper
non-technicaleducatorstodefinepatient reviewofpromptstoensuresafety/appropriateness.
personas.
Huetal.(2025) GPT-4o+Whisper+OpenAITTS 10distinctpatientpersonalitieswithautomated Limitedscope(singlehypertensionscenario);
assessmentofclinicalempathyandaccuracy. emotionallyflatTTSvoices;lackofformaluser
evaluationdata.
perceivedsignificantlyhigherusefulnessandbehavioralintention administrative confusion for international students during their
than enrolled students, validating the system as an effective academictransition.
recruitment tool. Furthermore, beta testing highlighted a distinct
userpreferenceforinteractivegamemechanics—suchasrunning
and teleportation—over the passive navigation styles typical of 3 System architecture and design
static360-degreetours(Garciaetal.,2023).
SalimandKhalilovdevelopedahigh-fidelityVRcampustour 3.1 TUMSphere platform overview
for Tishk International University (TIU) using a pipeline that
combines Autodesk 3D Max for modeling and Unreal Engine TUMSphere is an educational VR game developed for the
4 for interactive deployment on the HTC Vive Pro. Achieving Technical University of Munich’s Heilbronn campus, specifically
over 90% user satisfaction during student competition testing, designed to support first-semester Information Engineering
the project validates the role of immersive tours in student students during their transition to university life. The platform
recruitment, citing parallel evidence of enrollment growth from combines immersive virtual reality technology with game-based
similar implementations. However, the current system relies learning principles to create an engaging introduction to both
on static visualization without conversational agents, limiting the physical campus environment and the core concepts of the
engagement compared to dynamic AI-driven approaches (Salim academicprogram.
andKhalilov,2024).
While prior work has advanced specific aspects of AI-
driven VR—ranging from motion generation (McKern et al., 3.1.1 Gameenvironmentdescription
2024) and peer modeling (Liu et al., 2024) to domain-specific
clinical training (Hu et al., 2025; Zhu et al., 2025)—TUMSphere The virtual environment recreates the Bildungscampus
distinguishes itself by integrating these elements into a holistic Heilbronn, with a particular focus on the TUM School of
student orientation platform. Unlike existing virtual campus Computation, Information and Technology (CIT) building, one
tours that rely on static visualization (Salim and Khalilov, of the main buildings at TUM. The game world was constructed
2024) or error-prone voice commands (Azizo et al., 2020), using a combination of on-site measurements, photogrammetry
our approach leverages a unified, modular architecture (Convai) (Berrezueta-Guzman et al., 2025), and official architectural floor
to create fully embodied agents capable of both retrieval- plans to achieve spatial authenticity while making necessary
augmentedconversationandautonomousspatialnavigation.This adjustments for VR comfort and navigability. The environment
implementation moves beyond the purely linguistic focus of includesboththeexteriorcampusgrounds,featuringsurrounding
ELLMA-T (Pan et al., 2025) or the complex hybrid architectures buildings and landscaping elements, and the interior spaces,
of LearningverseVR (Song et al., 2024), providing a streamlined, includingclassrooms,laboratories,corridors,andcommonareas.
scalablesolutionspecificallydesignedtomitigatesocialanxietyand Through iterative playtesting, the development team discovered
FrontiersinComputerScience 04 frontiersin.org

Berrezueta-GuzmanandWagner 10.3389/fcomp.2026.1799323
thatreal-worldmeasurementsneededtobemodifiedforoptimal progressingtomoreadvancedsubjectssuchasOperatingSystems,
VR perception, leading to subtle geometric adjustments that Databases, and Linear Algebra. Each mini-game is designed
preservedthecampuslayoutwhileenhancinguserexperienceand to provide conceptual exposure rather than comprehensive
spatiallegibility. instruction,servingasanengagingpreviewofacademiccontent.
The virtual campus serves multiple functions beyond simple Game mechanics include standard VR interaction paradigms
visualization.StudentscanfreelyexploretheenvironmentusingVR such as locomotion via thumbstick controls with optional
locomotioncontrols,interactwithvariousobjectsandspaces,and teleportation,objectinteractionthroughgrabmechanicsusingVR
encountercontextuallyplacededucationalcontent.Thisapproach controllertriggers,spatialnavigationguidedbyvisualcuesandin-
transformspassiveobservationintoactivediscovery,allowingusers game NPCs, and progression systems that unlock new areas and
tobuildspatialfamiliaritywiththeiracademicenvironmentbefore challenges as students complete tasks. The control scheme was
oralongsidetheirphysicalcampusexperience. deliberatelysimplifiedandintroducedthroughatutorialsequence,
with persistent access to a settings menu for reference, ensuring
accessibilityforuserswithvaryinglevelsofVRexperience.
3.1.2 Educationalobjectivesandgame
mechanics
3.1.3 Targetusergroup
TUMSphere pursues several interconnected educational
objectives aligned with the needs of incoming Information The primary target audience for TUMSphere consists of
Engineering students. The primary goal is to familiarize students prospective and newly enrolled students in the Information
with the campus, enabling them to navigate and understand Engineering bachelor’s program at TUM Campus Heilbronn. Of
the physical layout of their study environment, locate essential particular significance is the international student population,
facilities such as lecture halls, laboratories, student services, and which represents a substantial proportion of the campus
recreationalspaces,andreduceanxietyassociatedwithnavigating community. According to internal enrollment statistics from
anunfamiliarcampus.Asecondaryobjectivefocusesoncurricular the 2024/25 academic year, the BIE program includes 603
introduction, where the game introduces core subjects from the students, of whom approximately 89% are international,
InformationEngineeringprogramthroughinteractivemini-games representing 77 different countries. This demographic diversity
thatcorrespondtofirstandsecond-semestercourses. underscorestheneedformultilingualsupport,accessibleguidance
The game employs a progression-based structure visualized systems, and culturally adaptive interaction design within the
in a comprehensive workflow diagram (as shown in Figure1) TUMSphereplatform.
that maps mini-games to specific academic subjects. Students International students face unique challenges during their
advance through increasingly complex challenges that mirror transition to German university life, including language barriers,
their educational journey, starting with foundational topics unfamiliarity with German academic culture and administrative
like Computer Architecture and Software Engineering, then systems, limited prior knowledge of campus geography and local
FIGURE1
Workflowdiagrammappingtheprogressionofmini-gamestotheircorrespondingacademicsubjects.Eachnumberednoderepresentsamini-game,
andthelayoutillustratesthesequentialstructuredesignedforfirst-semesterInformationEngineeringstudents.
FrontiersinComputerScience 05 frontiersin.org

Berrezueta-GuzmanandWagner 10.3389/fcomp.2026.1799323
services,andpotentialsocialisolationduringtheinitialadaptation recognition, proximity detection), the integration layer (API
period. TUMSphere addresses these challenges through multiple communication, data serialization, response handling), and the
design features, most notably the integration of AI-powered AI service layer (speech recognition, language model processing,
NPCs capable of engaging in natural language conversations. speechsynthesis).
These NPCs provide personalized guidance on university This layered architecture evolved through iterative
services, answer questions about academic requirements and development, beginning with a simpler desktop prototype
campus life, and offer a low-pressure environment for practicing that established core communication patterns before introducing
conversationalinteractions. VR-specificrequirements.Theinitialimplementationutilizedthe
The platform also serves secondary audiences, including VaRest plugin to handle HTTP REST API communication with
current students seeking academic support or campus navigation OpenAI’s GPT models, providing fundamental capabilities
assistance, university staff and faculty interested in innovative for JSON parsing, asynchronous request handling, and
pedagogicaltools,prospectivestudentsconductingvirtualcampus response processing. However, the transition to VR revealed
tours during the decision-making process, and researchers significant limitations in text-based interaction, necessitating the
investigating the use of serious games and VR applications integration of speech-to-text and text-to-speech capabilities to
in higher education. This broader accessibility enhances the maintainimmersion.
platform’sutilitywhilemaintainingitscorefocusonsupportingthe Rather than assembling these capabilities from multiple
international student experience during the critical first-semester disparate services, the final architecture adopted the Convai
transitionperiod. platform, which provides an integrated solution combining
automaticspeechrecognition,naturallanguageprocessingthrough
LLM integration, neural text-to-speech synthesis, and automated
3.1.4 Inclusivity-drivendesignrationale generation of lip-sync and facial animation parameters. This
unified approach significantly reduced architectural complexity
The platform’s design moves beyond general orientation by whileprovidingadditionalfeaturessuchaspersistentconversation
operationalizing specific inclusivity mechanisms for international memory, character-specific personality configuration, and voice
students(N =603,89%ofcohort). customizationoptions.
1. Linguistic Accessibility: To mitigate high cognitive
workload, NPC speech rates were reduced to 0.8x of
conversational standard, and accents were set to neutral 3.2.2 Componentinteractionanddataflow
English models to ensure comprehension across 77 different
linguisticbackgrounds. The interaction between system components follows a well-
2. Psychological Safety: The “judgment-free” nature of the definedsequence,asshowninFigure2,triggeredbyuserproximity
AIagentwasspecificallyimplementedasananxiety-reduction orexplicitinput,andcanbetracedthroughseveraldistinctphases
mechanism,allowingstudentstorehearseadministrativequeries inatypicalconversationalexchange.
(TaskA)orlinguisticroleplay(TaskC)inalow-stakessandbox InitiationPhase:Whenastudentnavigatesthevirtualcampus
beforephysicalcampusimmersion. and encounters an NPC within a defined interaction radius or
pressesadesignatedactivationbutton(mappedtothe“A”buttonon
VRcontrollers),thesysteminitiatestheconversationpipeline.The
VRclientcapturesthestudent’sspatialpositionandcontrollerinput
3.2 LLM integration architecture state,anddetermineswhethertheinteractionconditionsaremet.
Visualfeedback,suchasasubtlehighlightorattentionanimation,
ThedevelopmentofconversationalNPCswithinTUMSphere indicatesthattheNPCisreadytoreceiveinput,andaudiocapture
followed an iterative approach, evolving from initial desktop isactivated.
prototyping to fully immersive VR implementation. This Input Capture and Processing: The student speaks naturally
evolutionaryprocessenabledthesystematicexplorationofvarious while the system continuously streams audio data from the VR
integrationstrategiesandtechnicalsolutionsbeforecommittingto headset microphone through Unreal Engine’s audio subsystem,
thefinalarchitecture. here, to the Convai plugin’s input handler, which manages
buffering and network transmission. This streaming approach
reduces perceived latency compared to waiting for complete
3.2.1 Overallsystemdesign utterancedetectionbeforetransmission.Onremoteservers,speech
recognition services analyze the audio stream, applying acoustic
The LLM integration architecture follows a client-server models and language models to produce text transcripts with
model, with the Unreal Engine-based VR application serving as associatedconfidencescores.
the client and communicating with cloud-based AI services via Language Model Processing: The transcripts, packaged with
structured API calls. The system was designed with modularity contextual metadata including NPC personality definitions,
in mind, separating concerns between different functional layers: conversation history, and current game state, are forwarded to
the VR presentation layer (user interface, 3D environment, the large language model. The LLM evaluates the input against
characterrendering),theinteractionlayer(inputcapture,gesture its training data, the NPC’s specific instructions and personality
FrontiersinComputerScience 06 frontiersin.org

Berrezueta-GuzmanandWagner 10.3389/fcomp.2026.1799323
FIGURE2
Five-phasedataflowarchitectureoftheVRconversationalAIsystem,illustratingthebidirectionalinteractionbetweenlocalUnrealEngineclient
components(inputcapture,rendering)andcloud-basedprocessingontheConvaiplatform(STT,LLM,TTS,andanimationsynthesis).
parameters, conversation history stored in memory, and any Error-handling mechanisms ensure that connection failures,
relevant knowledge base entries configured for the character. timeouts,ormalformedresponsesdonotbreaktheuserexperience;
Responsegenerationconsidersmultiplefactors,includingsemantic instead, they trigger fallback behaviors such as predefined error
coherence,characterconsistency,educationalappropriateness,and messagesortemporaryNPCunavailabilityindicators.
conversationalgoals. The modular nature of this architecture provides flexibility
Response Synthesis: The generated response text undergoes for future enhancements, allowing individual components to
parallelprocessingforaudioandanimationgeneration.Thetext- be upgraded or replaced without requiring a complete system
to-speechsystemappliesprosodymodelstogeneratenaturalspeech redesign.Forinstance,alternativeLLMproviders,differentspeech
patterns, including pitch variations, speaking rate, emotional synthesis services, or enhanced animation systems could be
coloring, and punctuation pauses. Simultaneously, a phoneme integrated by modifying only the relevant interface layer while
analysis system generates timing data indicating when specific preservingtheoveralldataflowstructure.
mouth shapes should occur during speech playback. These
phonemesequencesaremappedtoanimationblendshapes,orbone
transformscompatiblewiththecharacter’sfacialrig.
3.3 Technical stack
Presentation and Playback: The VR client receives these
processed outputs and coordinates their presentation. Audio
The final TUMSphere NPC implementation leverages several
streamsarerenderedthroughspatialaudioprocessing,positioned
interconnected technologies to create a cohesive conversational
attheNPC’slocationin3Dspacewithappropriateattenuationand
experience,asillustratedinFigure3.
environmentaleffects.Animationdatadrivesreal-timeupdatesto
the character’s facial mesh, creating synchronized lip movements
andcomplementaryexpressionssuchasblinks,eyebrowraises,or
head tilts. The conversation state is updated with the exchange, 3.3.1 Unrealengine
enabling context retention for subsequent interactions in which
NPCscanreferencepreviousexchangesandadapttheirresponses Unreal Engine serves as the primary development platform,
basedoninteractionhistory. utilizing OpenXR for cross-platform VR support. The Blueprint
This data flow architecture balances responsiveness with visual scripting system facilitated rapid prototyping of NPC
quality, employing various optimization strategies including behaviors and interaction logic without compilation delays.
asynchronousprocessingtopreventblockingthemainrendering Furthermore, the engine’s native skeletal mesh system provides
thread, progressive response streaming where supported, the necessary infrastructure for character animation, specifically
and graceful degradation when network conditions degrade. supportingmorphtargetsrequiredforreal-timefacialexpression
FrontiersinComputerScience 07 frontiersin.org

Berrezueta-GuzmanandWagner 10.3389/fcomp.2026.1799323
FIGURE3
Evolutionofthetechnicalarchitecturefromtheinitialdesktopprototype(Phase1)tothefinalVRimplementationinTUMSphere(Phase2).
and lip-syncing (Berrezueta-Guzman and Wagner, 2026; Epic 3.3.5 ReadyPlayerMe
Games,2024).
Visual representation is handled by Ready Player Me, which
providescustomizable,high-fidelity3Davatars.Theseavatarsare
3.3.2 VaRestplugin importedwithpre-configuredskeletalrigsandfacialblendshapes
(compatiblewithARKitandOculusVisemes).Thisstandardization
Utilizedprimarilyduringtheinitialdesktopprototypingphase, is critical for the pipeline, as it allows the phoneme timing data
the VaRest plugin enabled direct REST API communication generated by Convai to drive the avatar’s mouth movements
within Blueprints. It handled HTTP request construction, JSON automatically,resultinginaccurate,real-timelip-synchronization
parsing,andasynchronousresponsemanagement.Thiscomponent withoutmanualanimationrigging(ReadyPlayerMe,2024;Convai,
validatedthecorelogicofconnectingUnrealEnginetoOpenAI’s 2024a).
endpoints before the transition to the more comprehensive
Convaisolution.
3.4 Alternative plugins and tools explored
3.3.3 OpenAIGPTmodels Duringtheprototypingphase,weevaluatedseveralalternative
toolsforconversationalAIinVR.Whileviableforothercontexts,
ConversationalintelligencereliesonOpenAI’sGPT-3.5Turbo. these were not selected for TUMSphere. Table2 compares these
Thismodelwasselectedforitsoptimalbalancebetweenreasoning solutions, illustrating why Convai was chosen: it offers the only
capabilityandinferencespeed.Forthespecificusecaseofcampus unified platform combining LLM integration, speech processing,
orientation—which requires factual information retrieval rather and VR-optimized lip-sync, thereby eliminating the architectural
thancomplexcreativewriting—GPT-3.5-turboofferedsufficiently complexityofintegratingmultiplespecializedplugins.
low latency to maintain the “illusion of presence” in VR while
minimizing the delay between user input and NPC response
(OpenAI,2024).
4 Methodology and technical
implementation details
3.3.4 Convaiplugin
4.1 Initial prototype development in UE as
The Convai plugin functions as the central integration a chatbox with VaREST
hub in the final VR architecture. It manages the runtime
conversationpipeline,includingcharacterinitializationviaunique The initial prototype was developed as a desktop application
IDs, audio capture, and event-driven response handling. By inUnrealEngine,implementingatext-basedchatboxinterfacethat
unifying Automatic Speech Recognition (ASR), LLM processing, communicatedwithOpenAI’sGPT-3.5TurbomodelviatheVaRest
and Text-to-Speech (TTS) into a single plugin, it eliminates the plugin,asillustratedinFigure4.Thisimplementationestablished
complexityofmanagingseparateAPIs.Additionally,itsweb-based thefoundationalconversationloopandvalidatedthecoreconcept
dashboard enables “no-code” configuration of NPC personalities ofLLMintegrationwithintheUnrealEngineenvironmentbefore
andKnowledgeBanks(Convai,2024b;Nnoli,2024). introducingVR-specificcomplexities.
FrontiersinComputerScience 08 frontiersin.org

Berrezueta-GuzmanandWagner 10.3389/fcomp.2026.1799323
TABLE2ComparisonofalternativeunrealenginepluginsforconversationalAI.
Feature Runtime-AIchatbot Runtime-speech RuntimeMetaHuman Convai
recognizer LipSync
Primaryfunction LLMintegration Speech-to-text Lip-syncanimation All-in-one
Internetrequired Yes(cloudAPIs) No(offline) No(offline) Yes(cloudplatform)
VR-ready Partial Partial Yes(questsupport) Yes(fullsupport)
Lip-syncsupport No No Yes(3models) Yes
Emotionalcontrol No No Yes(12moods) Limited
Platformsupport AllUEplatforms AllUEplatforms AllUEplatforms AllUEplatforms
GPUacceleration N/A Vulkan/Metal onnxruntime Server-sideprocessing
Modeloptions 15+LLMs Whisper(5sizes) 3qualitylevels 18LLMs
Bestusecase Multi-LLMprojects Privacy-firstSTT MetaHumancharacters VRconversationalNPCs
FIGURE4
EarlydesktopprototypeofourNPCinteractionsystem,builtinUnrealEngineusingtheVaRestplugin.Thefigureshowsthesimplescrollablechatbox
ontheright,wheretheusertypesmessagesandreceivesresponsesfromtheLLM.
4.1.1 Userinterfaceimplementation 4.1.2 Inputprocessing
The prototype featured a scrollable chat interface built using User input was captured through a standard text entry field
Unreal Motion Graphics (UMG), Unreal Engine’s visual UI where students typed their questions or messages. The system
authoring system. The interface employed a vertical scrolling monitoredfortheEnterkeypresstosubmitmessages,triggering
containerthatdynamicallydisplayedtheconversationhistory,with the API communication sequence. Before sending any request
eachmessageappearingasaseparatetextelement.Usermessages to the OpenAI API, the implementation validated that the input
andAIresponseswerevisuallydistinguishedbycolor—userinputs was not empty, preventing unnecessary API calls and associated
were white, while AI-generated responses were pink, creating a costs from blank submissions. This validation step represented a
clearvisualseparationbetweenparticipants. basic but essential form of error prevention, ensuring that only
The system automatically scrolled to display the most recent meaningfuluserinputreachedthelanguagemodel.
message as the conversation progressed, eliminating the need to
manually navigate the chat history. Each time a new message
was added to the interface, whether from the user or the AI, 4.1.3 APIcommunicationarchitecture
the scroll position updated to show the latest content. A brief
0.2-s delay was introduced between message display and scroll The communication with OpenAI’s API was implemented
adjustmenttoensuresmoothvisualtransitionsandpreventjarring using the VaRest plugin, which provides Blueprint-accessible
interfaceupdates. nodes for REST API interactions. The VaRest plugin handled
FrontiersinComputerScience 09 frontiersin.org

Berrezueta-GuzmanandWagner 10.3389/fcomp.2026.1799323
the HTTP protocol communication, JSON formatting, and UI overlay rather than emanating from a character within the
asynchronous request management that would otherwise require virtualenvironment.Therefore,wenoticedwerequirevoice-based
C++programming. interaction with speech recognition and synthesis capabilities,
Thetemperatureparameterdeservesparticularattention.This as well as embodied NPCs with synchronized facial animation
value,rangingfrom0to1,determineshowdeterministicorcreative and spatial audio. The research phase that followed evaluated
the model’s responses will be. The prototype experimented with available solutions for these requirements, examining standalone
valuesbetween0.1and0.5,ultimatelyfavoringlowervaluesaround speech-to-text(STT)andtext-to-speech(TTS)plugins,animation
0.1 for educational contexts. Lower temperatures produce more synchronizationsystems,andintegratedplatforms(asintroduced
focusedandconsistentresponses,whichprovedmoreappropriate inprevioussections).
for providing factual information about university services and However,implementingSTTandTTSasseparatecomponents
campusnavigationthanhighlycreativeorvariedanswers. would have required integrating multiple services and managing
theirindividualAPIs,authenticationprotocols,anddataflows.This
architectural complexity, combined with the need to synchronize
4.2 Research insights and system failure speechaudiowithcharacterlipmovementsandfacialexpressions,
modes presented substantial technical challenges. During the research
phase exploring VR voice integration solutions, the Convai
platformemergedasacomprehensivesolutionaddressingmultiple
While the initial desktop prototype validated basic LLM-
integrationchallengessimultaneously,asillustratedinFigure5.
UE5 communication via REST protocols, the transition to
VR revealed critical design trade-offs that extend beyond
standardimplementation.
4.4 Convai platform integration
4.2.1 Designtrade-offs:cloudvs.local
processing Building upon the validated LLM communication patterns
establishedinthedesktopprototype,thedevelopmenttransitioned
Akeyfailuremodeidentifiedwasthe“latency-presencegap.” toimplementingvoice-enabledNPCswithintheVRenvironment
Utilizingcloud-basedLLMs(GPT-3.5)providedsuperiorsemantic using the Convai platform. Convai distinguished itself through
understanding but introduced a variable end-to-end latency of its comprehensive feature set, including multiple LLM provider
1.42sto2.90s.InVR,thisdelaydisruptsthesocialrhythm,leading options (OpenAI, Anthropic, and others), extensive voice
to“doubling,”inwhichusersspeakovertheNPC. customization with various accents and speaking styles,
knowledge bank integration for domain-specific information,
character background and personality configuration, and unified
4.2.2 LessonsforgeneralizedVR+LLMsystems API handling STT, LLM processing, TTS, and animation
generation. This all-in-one architecture eliminated the
complexity of coordinating multiple services while providing
1. Input Modality Preference: Voice-driven interaction is
VR-optimizedfeaturesdesignedexplicitlyforinteractivecharacter
mandatory for presence; physical keyboard requirements in
implementationingameengines.
earlyprototypeswerefoundtobeimmersion-breaking.
2. Navigation as Intelligence: Embodiment (Task B)
significantly outperformed verbal instructions in utility,
suggesting that for orientation tasks, an LLM’s value is 4.4.1 Platformarchitectureoverview
maximizedwhencoupledwithspatialagency(NavMesh)rather
thanjustspeech. Convai operates as a conversational AI platform specifically
designed for games and virtual worlds, providing an integrated
solution that combines LLM capabilities with voice interaction
and character animation features. The platform operates on a
4.3 Transition to VR and voice integration client-server model, where the Unreal Engine plugin manages
local operations, such as audio capture, animation playback
The desktop prototype successfully demonstrated that LLM coordination, and user interface responses. Meanwhile, Convai’s
integrationwithUnrealEnginewastechnicallyfeasibleandcould cloud infrastructure handles computationally intensive tasks,
produce coherent, contextually appropriate responses to user includingautomaticspeechrecognition,LLMinference,andneural
queries. Students could ask questions about campus facilities, text-to-speechsynthesis.
university services, or general information and receive relevant TheConvaiintegrationwithinTUMSphererequiredadapting
answersgeneratedbythelanguagemodel.Theconversationhistory the plugin’s default interaction mechanisms to suit VR-specific
displayalloweduserstoreviewpreviousexchanges,andthesystem requirementsandtheeducationalcontext.Theprimaryintegration
maintainedreasonableresponsetimesfortypicalqueries. workinvolvedconfiguringinputmappings,establishinginteraction
However, the prototype lacked any integration with 3D triggers, and connecting Convai’s conversation system with
characters or spatial positioning—responses appeared in a flat TUMSphere’sexistingVRplayercontroller.
FrontiersinComputerScience 10 frontiersin.org

Berrezueta-GuzmanandWagner 10.3389/fcomp.2026.1799323
FIGURE5
ModularpipelineusingseparateAPIsforeachvoiceinteractioncomponent.SpeechinputfromtheVRheadsetisprocessedthroughdistinctSTT,
LLM,TTS,andlip-syncmodulesbeforereachingtheanimatedNPCcharacter.
To make interacting with NPCs feel natural, we set the “A” ensuringthe3Dmodelintheheadsetstaysperfectlysyncedwith
button on the VR controller as the primary trigger for speaking. theAIconfigurationstoredonline.
We created a custom command, IA_Talk, that works with both
VR controllers and keyboards, enabling a simple “push-to-talk”
systemsimilartoawalkie-talkie.Bylinkingthiscommanddirectly 4.4.2 Environmentalawarenessandobject
to the AI’s listening functions, the system starts recording when interaction
the button is pressed and stops when it is released, ensuring a
consistent,easy-to-test,andintuitiveinteractionforstudents. Beyond conversational capabilities, the Convai integration
Tomakethesystemeasiertomaintainandupdate,wemoved includedenvironmentalawarenessfeaturesthatenabledNPCsto
thepush-to-talkcodefromtheplugin’sdefaultfilesintoourown perceive and interact with objects in the virtual campus. This
customplayerfile,theVRPawnBlueprint.Initially,ourlogicwas functionality, implemented through Convai’s Actions API, allows
buried inside the plugin’s original code, which made it difficult characters to recognize named objects in their surroundings and
to customize and risked our changes being erased whenever the performactionsrelatedtothem,creatingmoredynamic,spatially
pluginwasupdated.Bymovingthecontrolstoourownsystem,we awareinteractionsthanpurelyconversationalsystems.
gainedfullcontrolovertheVRinteractionflowwhileensuringthe The implementation involved registering specific campus
gameremainsstableandfuture-proofagainstsoftwareupdates(see objects with NPC characters through the Convai web interface’s
Figure6). Objects configuration section. For TUMSphere, key campus
Beyond input remapping, the integration established facilities and landmarks were identified and added to character
proximity-based eligibility for interaction. The system tracked awareness,includingvendingmachines,lecturehalls,laboratories,
VR hand controller positions relative to NPC locations, enabling studentserviceoffices,recreationalareas,andbuildingentrances.
conversations only when students positioned their controllers Eachobjectwasassignedadescriptivenameandpositionreference
within a defined interaction radius around characters. This thatthecharactercoulduseduringnavigationandconversation.
spatial requirement created intuitive interaction mechanics When students asked location-related questions such as
that let students “approach” NPCs and reach toward them “Where is the nearest vending machine?”, NPCs could not only
to initiate dialogue, mirroring natural social interaction provide verbal directions but also physically navigate to the
patterns rather than relying on abstract button presses without requestedlocation.ThenavigationsystemutilizedUnrealEngine’s
spatialcontext. NavMesh(NavigationMesh)system,whichdefinedwalkableareas
TobringeachNPCtolife,welinkedthegame’s3Dcharacters throughout the virtual campus. A NavMesh Bounds Volume
to their “brains” in the cloud using unique Character IDs. We encompassing the campus environment enabled characters to
generatedtheseIDsintheConvaiwebdashboardandthenpasted pathfind around obstacles, through corridors, and across open
themintoeachcharacter’ssettingswithinUnrealEngine.Thislink spaces,guidingstudentstotheirrequesteddestinations.
tells the game exactly which personality, voice, and specialized Thefollowingbehaviorprovedparticularlyvaluableforcampus
knowledge to use for each person the student meets on campus, orientation. Students could request “Follow me around the
FrontiersinComputerScience 11 frontiersin.org

Berrezueta-GuzmanandWagner 10.3389/fcomp.2026.1799323
FIGURE6
Finalizedpush-to-talkimplementationmovedintothecustomVRPawnBlueprint,providingfullcontroloverVR-specificlogic.
building,” and the NPC would accompany them, maintaining an approachesanNPC,thecharacterrespondswiththespecificvoice
appropriatefollowingdistancewhilecontinuingtheconversation. andexpertiseassignedtoit.
This escort functionality combined spatial navigation with For the TUMSphere environment, we developed multiple
conversationalguidance,enablingcharacterstoprovidecontextual NPCstailoredtothespecificneedsofinternationalstudents.One
information about locations as students explored the campus primarycharacterservesasaCampusBuddy,afriendlyguidewho
togetherwiththeirvirtualguide. supportsnewcomerswithorientationandadministrativequestions,
These environmental interaction capabilities transformed and provides details about the university’s Buddy Program. This
NPCs from static information kiosks into active participants in NPC is programmed with specific knowledge about campus
campus exploration, providing a more engaging and practical facilities and course structures to help first-semester students
orientationexperiencethanpurelyverbaldirectionsorstaticmaps feel at home. Another character serves as a dedicated Language
couldoffer. Partner, helping users practice their German in a relaxed, low-
pressure setting. Together, these AI-driven agents transform the
virtual campus from a static 3D model into an interactive social
4.5 Character configuration through sandbox where students can prepare for their academic and
culturaltransition.
Convai web interface
The behavioral characteristics, knowledge bases, and
personalities of individual NPCs were configured through 4.5.2 Characterdescriptionandbackstory
Convai’s web-based dashboard interface. This cloud-based
configuration system provided a crucial separation between TheCharacterDescriptionsectionillustratedinFigure7served
technicalimplementationandcontentauthorship. as the foundation for NPC personality definition. This text field
accepted natural language descriptions of the character’s role,
background, personality traits, and conversational objectives. For
4.5.1 CharactercreationandIDassignment example,acampustourguidecharactermightbedescribedas“a
friendlyandenthusiasticstudentambassadorwhohasbeenatTUM
Setting up each NPC is a straightforward process of linking Heilbronn for three years, loves helping international students
a digital “brain” in the cloud to a physical “body” in the virtual feel welcome, and enjoys sharing interesting facts about campus
environment. This begins on the Convai web dashboard, where facilitiesandlocalculture.”Thesedescriptionsinformedhowthe
wedefinethecharacter’spersonality,voice,andspecificknowledge underlying LLM interpreted conversation context and generated
base.Onceconfigured,thedashboardgeneratesauniqueCharacter responsesalignedwiththecharacter’sestablishedidentity.
ID—a specific string of text that acts as a bridge between the The backstory functionality allowed the creation of rich
cloud-basedAIandtheUnrealEngineBlueprint.Bycopyingand character histories that influenced conversational behavior.
pasting this ID into the character’s properties in the engine, we Characters could reference their backgrounds naturally during
establishavitalconnectionthatenablesthesystemtoretrievethe conversations,creatingmorebelievableandengaginginteractions
correctconfigurationinrealtime.Thisensuresthatwhenastudent thanpurelyfunctionalinformation-deliverysystems.
FrontiersinComputerScience 12 frontiersin.org

Berrezueta-GuzmanandWagner 10.3389/fcomp.2026.1799323
FIGURE7
(1)Themaincharacterconfigurationpanel,includingname,ID,andhigh-levelprofilesettings.(2)ThecoreAIconfigurationcategories,suchas
KnowledgeBank,PersonalityTraits,andCoreAISettings.(3)Additionalbehaviorandnarrativemodules,includingStateofMind,EmbodiedActions,
andNarrativeDesign.
TABLE3SystempromptandpersonaconfigurationforNPC“Akira”. 4.5.3 Knowledgebankintegration
Category Technicalimplementationandprompt
The Knowledge Bank section provided one of the most
content
impactful features for building educational and informational
Core “Youareathird-semesterInformationEngineeringstudentat NPCs.Thiscomponentenabledtheuploadofcustomdocuments,
identity TUMCampusHeilbronnandamemberoftheTUMCampus structured datasets, and curated textual resources that characters
HeilbronnBuddyProgram.” could reference during conversations. Unlike generic LLM
behavior,whichreliessolelyonpre-training,theKnowledgeBank
Behavioral “Youshareyourownexperiencestohelpnewstudentsadapt
allowedprecisegroundingofresponsesininstitution-specificand
logic bothacademicallyandsocially.Youguidenewstudents,
context-sensitiveinformation.
especiallyintheD-Building.”
For TUMSphere, the Knowledge Bank was populated with a
Persona “YouvaluetheeasycommunicationwithprofessorsandPhDs
diverse collection of resources tailored to both campus guidance
constraints thankstotheopen-doorculture.Youenjoythemodern,friendly
andlanguage-learningusecases.Theseincludeddetaileduniversity
atmosphereofthecampus.” information, such as campus facilities, contact information,
Backstory “Whenyoufirstarrivedinyour1stsemester,youfeltabit academic program structures, and international student support
and overwhelmed,whichiswhynowyouenjoyhelpingnewcomers.” services. Additionally, local area information about Heilbronn
motivation was incorporated, including nearby transportation options, city
orientationtips,andpracticalguidance.TheErsti-Guide,prepared
Tonestyle Friendly,enthusiasticstudentambassador;Clear,neutralEnglish
bytheTUMStudentCouncilHeilbronn,wasprocessedintoaclean,
ataslightlyreducedspeakingratefornon-native
structured text format and uploaded to ensure optimal retrieval
comprehension.
qualityinsideConvai.
Knowledge Integrated“KnowledgeBank”containingtheTUMErsti-Guide,
To support the German-practice NPCs, the Knowledge Bank
access campusfacilitylocations,andacademicprogramstructures.
wasfurtherexpandedwithofficialGoethe-Institutvocabularylists
forA1,A2,B1,andB2proficiencylevels.Thesedocumentsenabled
thecharactertoprovidelevel-appropriateexplanations,vocabulary
To ensure scientific reproducibility of our NPC’s behavior, assistance, and guided speaking feedback grounded in authentic
Table3detailsthespecificsystempromptandpersonaconstraints exam-relevant language data. By combining campus-specific
implementedforthecharacter‘Akira’. content with standardized language-learning resources, the
FrontiersinComputerScience 13 frontiersin.org

Berrezueta-GuzmanandWagner 10.3389/fcomp.2026.1799323
Knowledge Bank enabled characters to accurately handle a wide provided customizable, high-quality 3D character models with
rangeofqueries. facialanimationsupport,eliminatingtheneedforcustomcharacter
When users interacted with the system, Convai performed modelingwhilemaintainingvisualconsistencyacrosstheplatform.
retrieval-augmented generation (RAG), scanning the Knowledge
Bank for relevant passages before producing an answer. In this
process,Convaiautomaticallyhandlesdocumentvectorizationand 4.6.1 Plugininstallationandsetup
embedding creation, as well as the underlying similarity search
overtheseembeddings,sonoseparatevectordatabaseorcustom
The character mesh integration required installing two
RAG pipeline (e.g., based on Pinecone or Weaviate) is required
additional plugins beyond the core Convai plugin: the Convai
onthedeveloperside.Thissignificantlyimprovedfactualaccuracy,
Ready Player Me Plugin and the Convai Lip Sync Plugin, both
consistency,andcontextualgrounding.Asaresult,NPCresponses
compatiblewithUnrealEngine5.Thesepluginsweredownloaded
aligned closely with real procedures, local campus details, and
from Convai’s documentation resources, extracted, and placed in
exam-alignedlinguisticknowledgeforGermanpractice,farbeyond
a Plugins folder within the TUMSphere project directory. After
whatageneralLLMcouldprovidewithoutexternalreferences.
restartingtheUnrealEditor,theprojectrecognizedthenewplugins
andmadetheirfunctionalityavailableforcharacterconfiguration.
The installation process required recompiling the project to
4.5.4 Languageandspeechconfiguration integrate the plugin code with TUMSphere’s existing Blueprint
systems.Uponrestart,theeditordisplayedconfirmationmessages
The Language and Speech section controlled voice synthesis indicatingsuccessfulpluginintegration,andnewBlueprintparent
parameters that determined how characters sounded during classesbecameavailableforcharacterimplementation.
conversations. Options included selecting from numerous voice
models with different accents, genders, and tonal qualities;
adjusting speaking rate to ensure clarity for non-native speakers; 4.6.2 Characterblueprinteeconfiguration
configuringpitchandemphasispatterns;andselectingprimaryand
secondarylanguagesformultilingualsupport.
To integrate Ready Player Me avatars, the NPC parent
For TUMSphere’s international student audience, characters
class was updated from ConvaiBaseCharacter to
were configured with clear, neutral English accents at slightly
ConvaiReadyPlayerMeCharacter, enabling automatic
slower speaking rates than conversational defaults. This
model downloading and rendering. While customized avatars
adjustment improved comprehension for students with
only appear at runtime, the cloud-based initialization typically
varying English proficiency levels while maintaining natural-
completes in under one second. Because this occurs before the
sounding speech. Some characters were configured to support
user encounters the NPC, immersion is maintained without
German, allowing students to practice German conversation in a
the need for loading indicators. Future versions may utilize
low-pressureenvironment.
locally stored models to eliminate this minor “cold-start”
delayentirely.
4.5.5 PersonalitytraitsandcoreAIsettings
4.6.3 LipSyncandfacialanimation
The Personality Traits section offered structured personality
configurationbeyondfree-formdescriptions.Characterscouldbe
TheConvai Lip Sync Pluginsynchronizessynthesized
assigned traits along various dimensions such as friendliness vs.
speech with facial animations by mapping real-time phoneme
formality, enthusiasm vs. reservedness, verbosity vs. conciseness,
datatotheReady Player Meavatars’pre-configuredARKit
and helpfulness vs. directness. These parameters influenced
and Oculus Viseme blend shapes. As the text-to-speech system
responsegenerationpatterns:friendlycharactersproducedwarmer,
generatesaudio,theplatformsimultaneouslyproducestimingdata
moreconversationalresponses,whileformalcharactersmaintained
thatautomaticallydrivesjawandlipmovements.Thisautomated
professionaldistance.
pipeline eliminates the need for manual rigging or animation
The Core AI Settings section provided access to advanced
authoringwhilemaintainingconversationalbelievability.
parameters, including LLM model selection, temperature and
response randomness controls, maximum response length limits,
andcontextwindowsizeforconversationmemory.
5 Experimental setup and evaluation
4.6 Character integration with Convai
To validate the efficacy of the TUMSphere platform and
ReadyPlayerMe plugin the integration of LLM-powered NPCs, we designed a two-fold
evaluation strategy. This approach assesses both the pedagogical
The visual representation of conversational NPCs in usabilityofthesystemfromastudent’sperspective(UserStudy)and
TUMSphere utilized Ready Player Me avatars integrated through thetechnicalviabilityofthearchitecturewithrespecttolatencyand
Convai’s dedicated Ready Player Me plugin. This integration resourceconsumption(PerformanceEvaluation).
FrontiersinComputerScience 14 frontiersin.org

Berrezueta-GuzmanandWagner 10.3389/fcomp.2026.1799323
5.1 User study design in German, utilizing the A1-level vocabulary set in the
KnowledgeBank.
The user study was designed to evaluate whether intelligent
NPCs can effectively serve as campus guides and cultural 3. Post-Experience Evaluation (10 min): Semi-structured
mediators for international students. The study follows a mixed- interviews were analyzed using a reflexive Thematic Analysis
methods approach, combining quantitative psychometric scales approach.Tworesearchersindependentlycodedthetranscripts,
withqualitativesemi-structuredinterviews. reachingathematicsaturationatN =24.Inter-rateragreement
(Cohen’s κ) was 0.82, ensuring that the reported themes were
systematicallyderivedratherthananecdotal.
5.1.1 Participantsanddemographics
WerecruitedatotalofN =24participantsfromthefreshman
cohortoftheInformationEngineeringprogramatTUMCampus 5.1.4 Metricsandquestionnaires
Heilbronn. To align with our target demographic, the inclusion
criteria required participants to be international students (non- To quantify the user experience, we employed standard
German citizens) who had arrived in Germany within the past 6 usabilityinstruments:
months.Thegroupconsistedof14malesand10females,aged18–
26(M=21.4,SD=2.3).Allparticipantshadnormalorcorrected- • System Usability Scale (SUS): To measure the perceived
to-normalvision.While65%ofparticipantsreportedhavingplayed usabilityoftheVRinterfaceandinteractionmechanics.
video games previously, only 25% had prior experience with • User Experience Questionnaire (UEQ): To assess the
VRheadsets. experience across 6 scales (Attractiveness, Perspicuity,
Efficiency,Dependability,Stimulation,andNovelty).
• IgroupPresenceQuestionnaire(IPQ):Specificallytomeasure
the sense of spatial presence and the realism of the
5.1.2 Apparatusandenvironment
NPCinteractions.
• Task Completion Rate (TCR): Binary measurement
Thestudywasconductedinacontrolledlabenvironmentatthe
(Success/Fail) of whether the participant successfully
university.ThehardwaresetupconsistedofaMetaQuest3headset
retrievedthecorrectinformationfromtheNPCs.
connected via Air Link to a high-performance workstation (Intel
Core i9-13900K, NVIDIA RTX 4090, 64GB RAM) running the
packagedUnrealEngine5buildofTUMSphere.Thissetupensured
5.1.5 Statisticalreliabilityanalysis
thatanyperformancebottleneckswereattributabletothesoftware
architectureornetworklatencyratherthanhardwarelimitations.
To ensure the internal consistency of the psychometric
instruments within our specific international student cohort
(N = 24), we calculated Cronbach’s alpha (α) for the SUS,
5.1.3 Experimentalprocedure
IPQ, and each UEQ subscale. Following standard psychometric
practice, a coefficient of α ≥ 0.70 was established as
The procedure was divided into three phases, lasting
the threshold for acceptable reliability, confirming that the
approximately45minperparticipant:
questionnaire items consistently measured the intended usability
andpresenceconstructs.
1. Onboarding (10 min): Participants were briefed on safety
protocols and completed a generic VR tutorial to familiarize
themselves with locomotion and the “grab” mechanics. They
5.2 Performance evaluation
were also introduced to the specific “push-to-talk” mechanic
mappedtothecontroller“A”button.
2. Task Execution (25 min): Participants were asked to While user satisfaction is paramount, the technical feasibility
complete a “Campus Scavenger Hunt” scenario requiring ofreal-timeconversationalAIinVRreliesheavilyonlowlatency.
interactionwiththreedistinctNPCarchetypes: High delays between a user’s question and the NPC’s answer can
break the “illusion of presence” and induce cognitive dissonance.
• TaskA(InformationRetrieval):Locatethe“StudentService Therefore, we conducted a technical performance benchmark
Center”NPCandinquireaboutthedeadlineforsemester focusingonresponselatencyandframeratestability.
feepaymentsandhowtovalidatethestudentcard.
• TaskB(Navigation):Findthe“BuddyProgram”NPCand
askforaguidedtourtothenearestlibrary.Theparticipant 5.2.1 Latencymeasurementmethodology
had to follow the NPC as it physically navigated the
NavMesh. We defined the key metric as Time-to-Audio (TTA)—the
• TaskC(LanguagePractice):Engagethe“GermanLanguage duration from the moment the user releases the “talk” button
Tutor” NPC in a role-play scenario to order a coffee (sending the audio buffer) to the moment the engine renders
FrontiersinComputerScience 15 frontiersin.org

Berrezueta-GuzmanandWagner 10.3389/fcomp.2026.1799323
thefirstaudioframe.This“end-to-end”latencyencompassesfour 6.1 System performance and latency
distinctstages: analysis
1. Upload&STT:TransmissionofaudiotoConvaiserversand A critical factor for immersion in conversational VR is end-
transcription(Whisper). to-endlatency—thetimeelapsedbetweentheuserfinishingtheir
2. LLMInference:Generationofthetextresponse(GPT-3.5/4). sentenceandtheNPCbeginningtospeak.
3. TTSSynthesis:Conversionoftexttoaudio.
4. Download & Buffering: Receiving the audio stream in
UnrealEngine.
6.1.1 Responselatency(Time-to-Audio)
We instrumented the Blueprint code to log timestamps at
each stage of the network request. We ran a series of 50
We analyzed 50 interaction cycles categorized into “Short
automated test queries ranging from short greetings (“Hello”) to
Queries”(greetings,simpleconfirmations)and“ComplexQueries”
complex,retrieval-heavyquestions(“Explainthemodulestructure
(retrieval-augmentedquestionsrequiringKnowledgeBankaccess).
forInformationEngineering”).
The breakdown of processing time across the pipeline stages is
summarizedinTable4.
The LLM inference stage is the most significant
5.2.2 Systemresourceprofiling
bottleneck, particularly for complex queries that require
parsing the Knowledge Bank context. However, the average
ToensuretheintegrationdoesnotdegradetheVRexperience,
latency for standard interactions remained under 1.5 s,
we profiled the application using Unreal Insights. We measured
which users generally found acceptable for a “walkie-
the Game Thread and Render Thread times during active
talkie” style interaction, though slightly delayed for a
conversation states. Since the Convai plugin handles network
face-to-faceconversation.
requestsasynchronously,wehypothesizedthattheimpactonframe
rate (FPS) would be negligible. We targeted a stable 90 FPS,
which is the native refresh rate of the Meta Quest 3, to prevent
motionsickness.
6.1.2 Frameratestability
To ensure comfort in VR, maintaining a stable frame rate is
5.2.3 QuantitativeLip-syncassessment
essential. Profiling data from Unreal Insights confirmed that the
asynchronous nature of the Convai plugin prevented the main
To objectively quantify the synchronization between
gamethreadfromlockingduringAPIcalls.
synthesized speech and facial animation, we introduce the
Viseme-AudioSynchronizationError(VASE).Thismetricmeasures
thetemporaloffset((cid:4)t)betweentheonsetofanaudiophoneme • IdleState:90FPS(Stable)
• ActiveConversation(Listening/Thinking):89.4FPS
and the peak activation of its corresponding viseme blendshape
• ActiveConversation(Speaking/Animating):88.2FPS
withintheUnrealEngineenvironment.
Theerroriscalculatedas:
The slight dip during the speaking phase is attributed to the
VASE=|t −t | (1) CPUcostofprocessingreal-timelip-syncblendshapesontheReady
viseme_peak audio_onset
Player Me avatars. Still, performance remained well above the 72
FPS minimum threshold for comfortable VR experiences on the
TimestampswereextractedbyloggingtheOnPhonemeReceived
MetaQuest3.
eventsfromtheConvaiLipSyncPluginandcorrelatingthemwith
the Unreal Engine high-resolution audio clock. This allows us to
assesswhethernetwork-inducedlatencyorCPU-boundanimation
processingcausesthemouthmovementstolagbehindthespatial
6.1.3 Lip-syncsynchronizationaccuracy
audioplayback.
Quantitative testing using the VASE metric revealed
a mean synchronization error of 32ms (SD = 8ms)
6 Results
across 50 interaction cycles. As shown in Table4, the
synchronization remains stable even during complex RAG-
This section presents the findings from our performance based queries, despite the higher end-to-end latency reported in
benchmarking and user evaluation. We first analyze the system’s Table3.
technicalviabilitywithrespecttoresponselatencyandrendering These results indicate that the Convai Lip Sync Plugin
stability, followed by analyses of user engagement, usability effectivelybuffersphonemetimingdatatomatchtheaudiostream,
scores, and qualitative feedback gathered during the campus thereby avoiding the “uncanny valley” effect despite the cloud-
simulationtasks. basedinference.
FrontiersinComputerScience 16 frontiersin.org

Berrezueta-GuzmanandWagner 10.3389/fcomp.2026.1799323
TABLE4Averageend-to-endlatencybreakdownbyquerytype(inseconds).
Querytype STTprocessing LLMinference TTSandnetwork TotalTime-to-Audio
Short(greetings) 0.45s 0.62s 0.35s 1.42s(±0.2)
Complex(RAG-based) 0.55s 1.85s 0.50s 2.90s(±0.6)
Thedatarepresentthemeanvalueacross50trials.Boldvalueindicates“Time-to-Audio”latency.
FIGURE8 FIGURE9
Taskscompletionratesresults. UserExperienceQuestionnaire(UEQ)results.
TABLE5QuantitativeLip-syncaccuracy(VASE).
6.2 User experience and usability
Querycontext MeanVASE(ms) Std.Dev.(ms)
Participant responses (N = 24) were analyzed using Standardinteraction 28 5
the System Usability Scale (SUS) and the User Experience ComplexRAGretrieval 36 11
Questionnaire(UEQ). PerceptionThreshold <45 –
TABLE6Internalconsistency(Cronbach’salpha)forpsychometricscales.
6.2.1 Taskcompletionrates
Instrument/scale Numberof Cronbach’s
items alpha(α)
Participants showed a high success rate in accomplishing the
definededucationalobjectives,asshowninFigure8. SystemUsabilityScale 10 0.84
(SUS)
• TaskA(InformationRetrieval):96%successrate.Participants
UEQ(attractiveness) 6 0.79
successfullyretrieveddeadlineinformation.
• Task B (Navigation): 100% success rate. All participants UEQ(pragmaticquality) 12 0.76
successfullyfollowedtheNPCtothelibrary. UEQ(hedonicquality) 8 0.81
• TaskC(GermanLanguagePractice):83%successrate.Failures IgroupPresence(IPQ) 14 0.82
were primarily due to speech recognition misinterpreting
heavyaccentsorhesitationduringGermanphrasing.
6.2.3 Instrumentreliability
6.2.2 Psychometricscores Theinternalconsistencyanalysisconfirmedthatallemployed
scales reached the required reliability threshold for the study’s
TheoverallSystemUsabilityScale(SUS)scorewas76.4(SD= demographics. The Cronbach’s alpha values for the primary
12.5), placing the TUMSphere NPC system in the “Good” to constructs are summarized in Table5. These results indicate
“Excellent”rangeofusability. that the “Good” to “Excellent” usability scores reported (SUS =
The User Experience Questionnaire (UEQ) results, visualized 76.4) are statistically reliable and not the result of inconsistent
in Figure9, indicate particularly high scores for Stimulation and participantresponding.
Novelty, suggesting students found the AI interaction engaging The particularly high reliability of the Hedonic Quality and
and innovative. However, Dependability scored lower, reflecting Presence scales (α > 0.80) reinforces the qualitative findings of
occasionalfrustrationswithspeechrecognitionaccuracyorvariable high engagement and an “illusion of presence” experienced by
responselatency. studentsduringNPCinteractionsasillustratedinTable6.
FrontiersinComputerScience 17 frontiersin.org

Berrezueta-GuzmanandWagner 10.3389/fcomp.2026.1799323
6.3 Qualitative findings 7.1 Reducing social anxiety through
artificial interlocutors
Semi-structured interviews revealed three dominant themes
regardingtheinteractionparadigm. One of the most significant pedagogical findings of this
study is AI agents’ capacity to lower the threshold for social
interaction. As indicated by our qualitative data, international
6.3.1 Theme1:reducedsocialanxietyin
students frequently cited the NPCs’ “judgment-free” nature as a
languagelearning
primary advantage. This aligns with findings by Pan et al. (2025)
regardingELLMA-T,confirmingthatvirtualagentscaneffectively
Asignificantmajority,75%ofparticipants,identifiedtheNPC
mitigate the “Foreign Language Anxiety” often experienced in
as a “social sandbox.” One participant (P12) noted: “With a real
real-worldimmersion.
officer,Iworryaboutmygrammarmorethanthedeadline.Therobot
Unlike traditional role-play partners, the TUMSphere NPCs
doesn’tmindifIrepeatmyselfthreetimes.”Thisconfirmstheagent’s
allow students to pause, repeat questions, or make grammatical
roleasaculturalmediator.
errors without fear of social embarrassment. This supports
the hypothesis that VR combined with GenAI serves as an
effective “sandbox” for social acclimatization. However, unlike
6.3.2 Theme2:the“Thinking”silence
pure language-learning applications, TUMSphere contextualizes
these interactions within the specific administrative and spatial
Whilethelatencywastechnicallymanaged,thesilenceduring
realities of the university campus. The high success rate in Task
the“Thinking”phase(approx.2–3sforcomplexanswers)caused
A (Information Retrieval) suggests that reduced anxiety directly
social awkwardness. Forty percent of participants reported being
correlates with effective information absorption, as students felt
unsure if the system had heard them. “I didn’t know if I should
comfortableaskingclarifyingquestionstheymightotherwisehave
speakagainorwait.Asimple’Letmecheckthatforyou’orathinking
hesitatedtoask.
animationwouldhelp,”suggestedoneparticipant.
6.3.3 Theme3:spatialguidancevs.verbal
7.2 The latency-presence trade-off
instructions
From a technical perspective, the “Time-to-Audio” latency—
Participants overwhelmingly preferred the embodied
averaging1.42sforsimpleand2.90sforcomplexqueries—presents
navigation(TaskB)oververbaldescriptions.TheNPC’sabilityto
anuancedchallengetothesenseofpresence.WhileourSUSscores
say “Follow me” and physically walk to the destination was cited
indicate the system is usable, the qualitative feedback regarding
asthemosthelpfulfeatureforcampusorientation,confirmingthe
“awkwardsilences”highlightsagapbetweenuserexpectationsset
valueofintegratingtheLLMwiththeUnrealEngineNavMesh.
by human conversation (turn-taking gaps of ≈200ms) and the
realityofcloud-basedinference.
Our results contrast slightly with the lower latency reported
6.3.4 Negativecaseanalysis
by purely text-based implementations or local deployments like
Nurse Town (Hu et al., 2025). The additional overhead in our
Despite 96% success in information retrieval, the 17% failure
architecture stems from the synchronization of the Knowledge
rateinGermanpractice(TaskC)highlightsacriticalfailuremode:
Bank retrieval (RAG) and the phoneme-generation pipeline
the system’s inability to parse heavy phonetic variation or the
requiredforlip-sync.Thisintroducesa“Latency-PresenceTrade-
hesitant “filler” words common among A1-level speakers. This
off”:toprovideaccurate,institution-specificanswers(highutility)
suggests that “inclusive” STT requires fine-tuning on non-native
and realistic visual articulation (high immersion), we currently
datasetsratherthanoff-the-shelfmodels.
sacrificeconversationalfluidity.
Future iterations must address this by implementing
“conversational fillers” (e.g., having the NPC nod or say “Let
7 Discussion
me check that...”) to mask the processing time, a technique
suggested in conversational agent literature but not yet natively
The integration of Large Language Models into virtual implementedinthestandardpluginconfigurationused.
reality environments represents a paradigm shift from static,
pre-scriptededucationalexperiencestodynamic,learner-centered
interactions.Thisstudyaimedtoevaluatethetechnicalfeasibility
and pedagogical potential of this integration within TUMSphere. 7.3 Embodiment and spatial agency
OurfindingssuggestthatwhileLLM-poweredNPCssignificantly
enhance engagement and provide a unique “safe space” for Our study reinforces the necessity of embodiment in
international students, technical challenges related to latency educational VR. The universal success of Task B (Navigation),
and non-verbal synchronization remain critical hurdles to wherestudentsfollowedtheNPC,demonstratesthatspatialagency
seamlessimmersion. isasimportantasverbalintelligence.AnLLMthatcanonlyspeak
FrontiersinComputerScience 18 frontiersin.org

Berrezueta-GuzmanandWagner 10.3389/fcomp.2026.1799323
is essentially a “radio”; an LLM that can navigate the NavMesh However, the transition from prototype to production-
becomesa“guide.” ready educational tool reveals distinct challenges. The “latency-
This extends the work of McKern et al. (2024), who focused presence trade-off” remains a critical technical hurdle, where the
ongesturegeneration.InTUMSphere,thecouplingoftheNPC’s cognitivedissonancecausedbyprocessingdelaysconflictswiththe
movementwithitsverbalinstructions(“Followmetothelibrary”) immersiverealismofthevisualenvironment.
reduced the cognitive load required to translate verbal directions
intospatialnavigation.Thissuggeststhatthefutureofeducational
NPCs lies not just in better language models, but in tighter
9 Future directions
integration between the LLM’s semantic understanding and the
gameengine’sphysicsandnavigationsystems—allowingtheAIto
“act”intheworldratherthanjustdescribeit. Building on the initial validation of TUMSphere, our future
researchanddevelopmentwillfocusonthreekeypillarstomove
the platform from a successful prototype to a persistent, high-
7.4 Limitations fidelityeducationalecosystem.
Severallimitationsofthisstudymustbeacknowledged.First,
thesamplesize(N = 24)andtherestrictiontoasingleuniversity 9.1 Enhancing interaction fluidity and
campus limit the generalizability of the quantitative findings. non-verbal realism
Second, the study was conducted on high-end hardware (RTX
4090) via Air Link. Deploying this architecture on standalone To mitigate the “thinking silence” identified in our user
headsets (e.g., Meta Quest 3 native) would likely introduce study, we plan to implement continuous listening modes
additionalperformanceconstraintsnotcapturedhere. and conversational fillers (e.g., hesitation markers or verbal
Furthermore,whiletheKnowledgeBanksignificantlyreduced acknowledgments) to mask processing latency. Beyond verbal
hallucinations, it did not eliminate them. On rare occasions, improvements, we will activate the State of Mind and Embodied
the NPCs provided plausible but incorrect information about Actions modules. By establishing a dynamic emotional layer,
specific university deadlines that were not explicitly covered in NPCscanexhibitcontext-awaremoods—suchasenthusiasmwhen
the uploaded documents. This underscores the need for robust welcomingastudentorconcernwhendiscussingsafetyprocedures.
“guardrails” in educational AI, where misinformation can have These states will be synchronized with physical gestures and
real-worldacademicconsequences. posturechanges,leveragingtheUnrealEngineanimationsystemto
Finally, we observed a “Novelty Effect” (reflected in the high reducethe“uncannyvalley”effectandensurethatnon-verbalcues
UEQNoveltyscores).Long-termstudiesarerequiredtodetermine authenticallycomplementthesynthesizedspeech.
whether student engagement persists once the initial wonder of
talkingtoavirtualcharacterfades,orwhetherthesystem’sutility
sustainsusagethroughoutthesemester. 9.2 Structured pedagogy through hybrid
narrative design
8 Conclusion Whilefree-formconversationprovidesarobustsocialsandbox,
academic orientation requires structured progression. We intend
to leverage Narrative Design features to create hybrid interaction
ThisstudypresentedTUMSphere,anovelimplementationofan
models.Thisframeworkwillallowustodefinespecificconversation
educationalVirtualRealityenvironmentthatleveragesGenerative
trees and branching paths that guide students toward critical
AI to transform static Non-Player Characters into dynamic,
educational objectives—such as mandatory safety briefings or
conversational campus guides. By integrating Unreal Engine 5
administrative onboarding—without sacrificing natural language
withtheConvaiplatform,wedemonstratedascalablearchitecture
flexibility.Unlikethecurrentinitiative-drivenmodel,theseagents
for creating embodied AI agents capable of natural language
willbeabletotrackwhichtopicshavebeendiscussed(e.g.,semester
interaction,spatialnavigation,andcontext-awareassistance.
deadlines or student card validation) and proactively prompt
Our results indicate that the convergence of VR and
the student to explore missing information, effectively blending
LLMs offers substantial pedagogical value, particularly for
scriptedpedagogywithgenerativefreedom.
international students navigating the complexities of a new
academic environment. The system successfully provided a
“safe,”low-anxietyspaceforpracticinglanguageskillsandasking
9.3 Environmental awareness, persistence,
administrative questions, addressing the psychological barriers
often associated with real-world help-seeking. Furthermore, and scalability
the strong user preference for NPCs that can physically guide
users through the virtual campus underscores the importance of To deepen the NPC’s connection to the user and the virtual
embodiment—demonstrating that in VR, an AI agent must be environment,wewillimplementMindviewandMemorymodules.
more than just a chatbot; it must be an active participant in the Mindview will grant agents observational awareness, allowing
3Dspace. them to comment on the student’s spatial actions or items they
FrontiersinComputerScience 19 frontiersin.org

Berrezueta-GuzmanandWagner 10.3389/fcomp.2026.1799323
interact with on campus. Furthermore, by utilizing persistent Methodology, Investigation. SW: Supervision, Writing – review
Memorysettings,NPCswillbeabletorecognizereturningstudents &editing.
and reference previous interactions across different VR sessions,
fosteringacontinuoussupportsystemthatevolveswiththestudent
throughouttheirfirstsemester.
Funding
Finally, we aim to optimize these pipelines for standalone
VR hardware (e.g., Meta Quest native) and explore multi-user
Theauthor(s)declaredthatfinancialsupportwasreceivedfor
synchronization.Thiswillenablegroupsofinternationalstudents
this work and/or its publication. This research was financially
to participate in collective orientation sessions, transforming
supported by the TUM Campus Heilbronn Incentive Fund 2024
TUMSphere from an individual practice tool into a collaborative,
oftheTechnicalUniversityofMunich,TUMCampusHeilbronn
social learning environment that grows alongside the students
(5420023). We gratefully acknowledge their support, which
itsupports.
provided the essential resources and opportunities to conduct
thisstudy.
Data availability statement
Conflict of interest
Theoriginalcontributionspresentedinthestudyareincluded
in the article/supplementary material, further inquiries can be
The author(s) declared that this work was conducted in the
directedtothecorrespondingauthor.
absenceofanycommercialorfinancialrelationshipsthatcouldbe
construedasapotentialconflictofinterest.
Ethics statement
Generative AI statement
Ethical review and approval were not required for the study
involvinghumanparticipants,inaccordancewithlocallegislation
and institutional requirements. The research involved standard Theauthor(s)declaredthatgenerativeAIwasnotusedinthe
usability and user experience testing of an educational software creationofthismanuscript.
application with healthy adult volunteers, posing no physical or Any alternative text (alt text) provided alongside figures
psychological risks beyond those encountered in daily life or in this article has been generated by Frontiers with the
standard Virtual Reality usage. All participants provided written support of artificial intelligence and reasonable efforts have
informed consent before their participation, acknowledging the been made to ensure accuracy, including review by the
voluntarynatureofthestudy,theirrighttowithdrawatanytime, authors wherever possible. If you identify any issues, please
and the anonymized processing of their data, in full compliance contactus.
withtheDeclarationofHelsinkiandtheGeneralDataProtection
Regulation(GDPR).Writteninformedconsentwasobtainedfrom
theindividual(s)forthepublicationofanypotentiallyidentifiable Publisher’s note
imagesordataincludedinthisarticle.
All claims expressed in this article are solely those of the
authors and do not necessarily represent those of their affiliated
Author contributions organizations, or those of the publisher, the editors and the
reviewers. Any product that may be evaluated in this article, or
SB-G: Writing – review & editing, Funding acquisition, claimthatmaybemadebyitsmanufacturer,isnotguaranteedor
Writing – original draft, Formal analysis, Conceptualization, endorsedbythepublisher.
References
Azizo, A. S. B., Mohamed, F. B., Siang, C. V., and Isham, M. I. M. (2020). Berrezueta-Guzman, S., Koshelev, A., and Wagner, S. (2025). “From reality to
“Virtual reality 360 utm campus tour with voice commands,” in 2020 6th virtual worlds: The role of photogrammetry in game development,” in 2025 IEEE
InternationalConferenceonInteractiveDigitalMedia(ICIDM)(Xianyang:IEEE),1–6. Gaming, Entertainment, and Media Conference (GEM) (Kaohsiung: IEEE), 1–6.
doi:10.1109/ICIDM51048.2020.9339665 doi:10.1109/GEM66882.2025.11155764
Barmpari,A.,Voyiatzaki,E.,andHatzilygeroudis,I.(2026).“Aneducationalvirtual Berrezueta-Guzman,S.,andWagner,S.(2026).Choosingtherightengineinthevirtual
worldsystemwithgamificationfeaturesandllmguidednpcs,”inGenerativeSystems realitylandscape.IEEEAccess14,13972–13985.doi:10.1109/ACCESS.2026.3657272
andIntelligentTutoringSystems,eds.S.GrafandA.Markos(Cham:SpringerNature Chen,S.,Xu,X.,Zhang,H.,andZhang,Y.(2023).“Rolesofchatgptinvirtualteaching
Switzerland),213–223.doi:10.1007/978-3-031-98281-1_17 assistantandintelligenttutoringsystem:opportunitiesandchallenges,”inProceedings
FrontiersinComputerScience 20 frontiersin.org

Berrezueta-GuzmanandWagner 10.3389/fcomp.2026.1799323
ofthe20235thWorldSymposiumonSoftwareEngineering,WSSE’23(NewYork,NY: Luo,H.,Gao,F.,Fang,K.,Liu,D.,Lin,Z.,andChan,W.K.V.(2024).“Studywith
AssociationforComputingMachinery),201–206.doi:10.1145/3631991.3632024 confucius:anAI-basedimmersiveeducationalgamewithmultipleeducationalmodes,”
inSIGGRAPHAsia2024Educator’sForum(NewYork,NY:AssociationforComputing
Chen, Y., Ding, N., Zheng, H.-T., Liu, Z., Sun, M., and Zhou, B. (2024).
Machinery),1–6.doi:10.1145/3680533.3697066
“Empoweringprivatetutoringbychaininglargelanguagemodels,”inProceedingsof
the33rdACMInternationalConferenceonInformationandKnowledgeManagement, McKern, A., Mayer, A., Greif, L., Chardonnet, J.-R., and Ovtcharova, J. (2024).
CIKM ’24 (New York, NY: Association for Computing Machinery), 354–364. “AI-based interactive digital assistants for virtual reality in educational contexts,”
doi:10.1145/3627673.3679665 in 2024 IEEE 3rd German Education Conference (GECon) (Munich: IEEE), 1–5.
doi:10.1109/GECon62014.2024.10734030
Convai(2024a).AddingLipsynctoMetaHuman—ConvaiUnrealEnginePluginGuide.
SanJose,CA:Convai(AccessedOctober14,2025). Minaee, S., Mikolov, T., Nikzad, N., Chenaghlu, M., Socher, R., Amatriain, X.,
et al. (2024). Large language models: a survey. arXiv preprint arXiv:2402.06196.
Convai(2024b).ConvaiAPIDocumentation.SanJose,CA:Convai(AccessedOctober
doi:10.48550/arXiv.2402.06196
14,2025).
Mordor Intelligence (2024). Virtual Reality (VR) Market in Education - Growth,
Damianova, N., and Berrezueta-Guzman, S. (2025). Serious games
Trends,COVID-19Impact,andForecasts(2025-2030).Hyderabad:MordorIntelligence
supported by virtual reality–literature review. IEEE Access 13, 38548–38561.
(AccessedOctober13,2025).
doi:10.1109/ACCESS.2025.3544022
Nnoli, I. (2024). Spotlight: Convai Reinvents Non-Playable Character Interactions.
Dong, B., Bai, J., Xu, T., and Zhou, Y. (2024). “Large language models
NVIDIADeveloperBlog(AccessedOctober14,2025).
in education: a systematic review,” in 2024 6th International Conference on
Computer Science and Technologies in Education (CSTE) (Xi’an: IEEE), 131–134. OpenAI(2024).CompareModels—OpenAIAPIDocumentation.SanFrancisco,CA:
doi:10.1109/CSTE62025.2024.00031 OpenAI(AccessedOctober14,2025).
Du, W., Xu, Z., and Dang, T. (2025). “Research on the application of virtual Özkaya, S., Berrezueta-Guzman, S., and Wagner, S. (2025). How llms
reality technology in the field of education,” in 2025 5th International Conference are shaping the future of virtual reality. IEEE Access 13, 193335–193355.
on Artificial Intelligence and Education (ICAIE) (Suzhou: IEEE), 541–545. doi:10.1109/ACCESS.2025.3631594
doi:10.1109/ICAIE64856.2025.11158564
Pan,M.,Kitson,A.,Wan,H.,andPrpa,M.(2025).“Ellma-t:anembodiedllm-agent
Epic Games (2024). Virtual Reality Development Documentation. Unreal Engine forsupportingenglishlanguagelearninginsocialvr,”inProceedingsofthe2025ACM
Documentation(AccessedOctober14,2025). Designing InteractiveSystems Conference, DIS ’25 (NewYork, NY: Association for
ComputingMachinery),576–594.doi:10.1145/3715336.3735786
Garcia,M.,Mansul,D.,Pempina,E.,Perez,M.,andAdao,R.(2023).“Aplayable3d
virtualtourforaninteractivecampusvisitexperience:showcasingschoolfacilities Peixoto,B.,Pinto,R.,Melo,M.,Cabral,L.,andBessa,M.(2021).Immersivevirtual
toattractpotentialenrollees,”in20239thInternationalConferenceonVirtualReality reality for foreign language education: a prisma systematic review. IEEE Access 9,
(ICVR)(Xianyang:IEEE),461–466.doi:10.1109/ICVR57957.2023.10169768 48952–48962.doi:10.1109/ACCESS.2021.3068858
Gonzales, W. D. W., Shen, D. J., Yan, A., Xie, N., Francisco, M. L., and ReadyPlayerMe(2024).ReadyPlayerMeDocumentation.ReadyPlayerMe(Accessed
Wong, P. P. Y. (2025). “AI NPCS in an educational metaverse: evaluating the October14,2025).
effectivenessofprompttemplatesforcontextualinteractions,”inInnovatingEducation
Salim, M., and Khalilov, S. (2024). “Developing a virtual tiu campus tour:
with AI, ed. E. C. K. Cheng (Singapore: Springer Nature Singapore), 53–74.
integrating3dvisualizationofuniversityfacilitiesinvr,”in202421stInternational
doi:10.1007/978-981-96-4952-5_4
Multi-Conference on Systems, Signals Devices (SSD) (Erbil: IEEE), 540–544.
Guevarra,M.,Bhattacharjee,I.,Das,S.,Wayllace,C.,Epp,C.D.,Taylor,M.E.,etal. doi:10.1109/SSD61670.2024.10548711
(2025). “An llm-guided tutoring system for social skills training,” in Proceedings
Song, Y., Wu, K., and Ding, J. (2024). Developing an immersive game-based
of the Thirty-Ninth AAAI Conference on Artificial Intelligence and Thirty-Seventh
learningplatformwithgenerativeartificialintelligenceandvirtualrealitytechnologies–
ConferenceonInnovativeApplicationsofArtificialIntelligenceandFifteenthSymposium
“learningversevr”. Comput. Educ.: X Reality 4:100069. doi: 10.1016/j.cexr.2024.10
on Educational Advances in Artificial Intelligence, AAAI’25/IAAI’25/EAAI’25
0069
(Washington,DC:AAAIPress),29643–29645.doi:10.1609/aaai.v39i28.35353
Tracy, K., and Spantidi, O. (2025). Impact of gpt-driven teaching assistants
Hu,Y.,Xiong,Q.,Yi,L.,andYoon,I.(2025).“Nursetown:anllm-poweredsimulation
in vr learning environments. IEEE Trans. Learn. Technol. 18, 192–205.
gamefornursingeducation,”in2025IEEEConferenceonArtificialIntelligence(CAI)
doi:10.1109/TLT.2025.3539179
(SantaClara,CA:IEEE),215–222.doi:10.1109/CAI64502.2025.00041
Truchly,P.,Medvecký,M.,Podhradský,P.,andVancˇo,M.(2018).“Virtualreality
Hua,C.,andWang,J.(2023).Virtualreality-assistedlanguagelearning:afollow-up
applicationsinstemeducation,”in201816thInternationalConferenceonEmerging
review(2018-2022).Front.Psychol.14:1153642.doi:10.3389/fpsyg.2023.1153642
eLearningTechnologiesandApplications(ICETA)(StarySmokovec:IEEE),597–602.
Hussein, R., Zhang, Z., Amarante, P., Hancock, N., Orduna, P., and Rodriguez- doi:10.1109/ICETA.2018.8572133
Gil, L. (2024). “Integrating personalized ai-assisted instruction into remote
Vallance, M. (2023). Independently supporting learners in vr with an ai-
laboratories: Enhancing engineering education with openai’s gpt models,” in 2024
enabled non-player character (npc). Immers. Learn. Res. - Pract. 1, 69–73.
IEEE Frontiers in Education Conference (FIE) (Washington, DC: IEEE), 1–7.
doi:10.56198/ITIG2WMWY
doi:10.1109/FIE61694.2024.10892918
Viitaharju,P.,Nieminen,M.,Linnera,J.,Yliniemi,K.,andKarttunen,A.J.(2023).
Konecki,M.,Konecki,M.,andVlahov,D.(2023).“Usingvirtualrealityineducation
Studentexperiencesfromvirtualreality-basedchemistrylaboratoryexercises.Educ.
ofprogramming,”in202311thInternationalConferenceonInformationandEducation
Chem.Eng.44,191–199.doi:10.1016/j.ece.2023.06.004
Technology(ICIET)(Fujisawa:IEEE),39–43.doi:10.1109/ICIET56899.2023.10111156
Wan,H.,Zhang,J.,Suria,A.A.,Yao,B.,Wang,D.,Coady,Y.,etal.(2024).“Building
Leon,M.(2025).Gpt-5andopen-weightlargelanguagemodels:advancesinreasoning,
llm-basedaiagentsinsocialvirtualreality,”inExtendedAbstractsoftheCHIConference
transparency,andcontrol.Inform.Syst.136:102620.doi:10.1016/j.is.2025.102620
onHumanFactorsinComputingSystems,CHIEA’24(NewYork,NY:Associationfor
Levidze, M. (2024). Mapping the research landscape: a bibliometric ComputingMachinery),1–8.doi:10.1145/3613905.3651026
analysis of e-learning during the COVID-19 pandemic. Heliyon 10:e33875.
Wang,Z.,Chu,Z.,Doan,T.V.,Ni,S.,Yang,M.,andZhang,W.(2025).History,
doi:10.1016/j.heliyon.2024.e33875
development,andprinciplesoflargelanguagemodels:anintroductorysurvey.AI
Lin,A.J.,andCheng,F.F.(2024).“Virtualrealitygameforscienceeducation,”in2024 Ethics5,1955–1971.doi:10.1007/s43681-024-00583-7
5thInternationalConferenceonComputerScience,Engineering,andEducation(CSEE)
Wen, Q., Liang, J., Sierra, C., Luckin, R., Tong, R., Liu, Z., et al. (2024). “AI for
(Shanghai:IEEE),8–12.doi:10.1109/CSEE63195.2024.00010
education(ai4edu):advancingpersonalizededucationwithllmandadaptivelearning,”
Lin,X.P.,Li,B.B.,Yao,Z.N.,Yang,Z.,andZhang,M.(2024).Theimpactofvirtual inProceedingsofthe30thACMSIGKDDConferenceonKnowledgeDiscoveryandData
realityonstudentengagementintheclassroom:acriticalreviewoftheliterature.Front. Mining,KDD’24(NewYork,NY:AssociationforComputingMachinery),6743–6744.
Psychol.15:1360574.doi:10.3389/fpsyg.2024.1360574 doi:10.1145/3637528.3671498
Liu,Z.,Zhu,Z.,Zhu,L.,Jiang,E.,Hu,X.,Peppler,K.A.,etal.(2024).“Classmeta: Zhu,X.T.,Cheerman,H.,Cheng,M.,Kiami,S.R.,Chukoskie,L.,andMcGivney,
designing interactive virtual classmate to promote vr classroom participation,” E.(2025).“Designingvrsimulationsystemforclinicalcommunicationtrainingwith
in Proceedings of the 2024 CHI Conference on Human Factors in Computing llms-basedembodiedconversationalagents,”inProceedingsoftheExtendedAbstracts
Systems, CHI ’24 (New York, NY: Association for Computing Machinery), 1–17. oftheCHIConferenceonHumanFactorsinComputingSystems(Yokohama:ACM),
doi:10.1145/3613904.3642947 1–9.doi:10.1145/3706599.3719693
FrontiersinComputerScience 21 frontiersin.org
