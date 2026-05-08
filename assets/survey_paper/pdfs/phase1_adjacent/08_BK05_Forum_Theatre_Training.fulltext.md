Title: Mixed-Initiative Dialogue Management for Human-Virtual Agents Interaction in Forum Theatre Inspired Training

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/survey_paper/pdfs/phase1_adjacent/08_BK05_Forum_Theatre_Training.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T02:55:13+00:00
- page_count: 5
- status: ok
- text_char_count: 16726

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

Mixed-Initiative Dialogue Management for Human-Virtual Agents
Interaction in Forum Theatre Inspired Training
SamuelOtofa1,YacineZerenini2,FredericBechet1,BenoitFavre1,
Jean-MariePergandi2,MagalieOchs1
1LIS-AixMarseilleUniversity-CNRS-France,
2CRVM-AixMarseilleUniversity-CNRS-France
Correspondence:magalie.ochs@lis-lab.fr
Abstract ingtooldesignedtoraiseawarenessofethnicand
gender discrimination and to train users to react
Thisworkpresentsavirtualreality(VR)train-
appropriately as witnesses. Inspired by Augusto
ingtooldesignedtoraiseawarenessofsocial
discrimination(ethnicandgender-based)and Boal’sforumtheatre,thesystemstagesinteractive
totrainindividualstorespondeffectivelywhen discriminationscenarioswithautonomousvirtual
witnessing such situations. Inspired by Au- agents. Usersobserve,analyze,andreenactthese
gusto Boal’s forum theatre, the system recre- situationstoexplorealternativeresponses.
atesinteractivescenariosofdiscriminationus-
ing autonomous virtual agents. From a di- Technically,theprojectintroducesahybriddia-
alogue system perspective, the project intro- logue architecture combining state-based control
ducesahybriddialoguemanagementarchitec- with Large Language Model (LLM)-driven open
turecombiningstate-basedcontrolwithLarge
dialogue. Thisapproachsupportsbothstructured
LanguageModel(LLM)-drivenopendialogue.
trainingandflexible,context-sensitiveinteractions.
Thismixed-initiativeapproachallowsthesys-
Thedemonstratorwedescribeinthenextsections
tem to manage structured training sequences
showcasesthepotentialofVRdialoguesystemsfor
whilesupportingflexible,context-awareinter-
actionsonsensitivetopics. Thedemonstrator experientiallearningandsocialbehaviortraining
illustratesthisapproachthroughacaseofordi- inthecontextofworkplacesexism.
narysexisminaprofessionalsetting,highlight-
ingthepotentialofspokendialoguesystemsin
VRforexperientiallearningandsocialbehav-
iortraining. 2 TheForumTheatreapproach
1 Introduction
In the field of training, increasing attention has Weaimtodesignanddeployavirtualreality(VR)
beendirectedtowardsimulation-basedlearningus- trainingtoolintendedtoraiseawarenessofsocial
ingvirtualenvironments. Numerousstudieshave discrimination(bothethnicandgender-based)and
examinedsystemsthatsimulatesocialinteractions totrainindividualstorespondappropriatelywhen
withSociallyInteractiveAgents(SIAs)tofosterthe witnessing such situations. The tool draws inspi-
developmentofsocialskills(Bruijnesetal.,2019), rationfromtheforumtheatretechnique, aninter-
appliedtothemedicaldomain(Prangeetal.,2017; activetheatremethoddevelopedbyAugustoBoal
Campillos-Llanosetal.,2015)orinthecontextof inthe1960s(Boal,1972). Originallyconceivedas
teachertraining(Pautleretal.,2018). Thesestud- aformofpopulareducation,forumtheatreisnow
ieshaveshownthatSIAscaneffectivelyenhance widelyusedtopromoteawarenessofsocialissues
individuals’interpersonalabilities,forinstance,in suchasdiscriminationandviolence. Itinvolvesthe
jobinterviewpreparationorinterculturalcommu- dramatizationofaproblematicsituationperformed
nicationtraining(Andersonetal.,2013;Halletal., by actors, followed by active audience participa-
2011). However, several application domains re- tion: spectators are invited to take the place of a
main underexplored, notably the use of SIAs for characterandexplorealternativeactionstochange
trainingtopreventsocialdiscrimination,whichis thecourseofevents. Thismethodnotonlyraises
thefocusofthepresentstudy. awarenessbutalsoenablesparticipantstodevelop
In this context, the demonstration system we andpracticeconcretestrategiestheycanlaterap-
describeinthisstudyisavirtualreality(VR)train- plyinreal-lifecontexts.

Variousinteractivescenarioscanbesimulated,
encompassing different forms of social discrimi-
nation. In the proposed demonstration, we focus
onordinarysexismoccurringindiversesocialcon-
texts(e.g.,hierarchicalrelationships,mixed-gender
interactions)andexpressedthroughvaryingsocio-
emotionalbehaviorsofvirtualagents(e.g.,concil-
iatoryvs. aggressiveattitudes). Ordinarysexismis
definedas“stereotypesandcollectiverepresenta-
tionsthattranslateintowords,gestures,behaviors
Figure1: ScreenshotofaVRscenedepictingadiscrim-
oractionsthatexclude,marginaliseorinferiorize
inatory situation enacted by two autonomous virtual
women”(Grésy,2009);forexample,sexistremarks
characters
andjokesordeviousseduction.
ThevirtualactorsareintegratedintoaVRplat-
formthatsimulatessocialinteractions. Asaninitial
step, we use a collected corpus of forum theatre
performancesondiscriminationdescribedin(Ochs
etal.,2023). Motioncapturewasusedinthiscor-
pustorecreaterealisticsceneswithvirtualcharac-
ters and to model the behavior of discriminatory
agents (Figure 4). This behavioral modeling en-
ablesthevirtualactorstoreproducediscriminatory
attitudes dynamically during interaction with the
user.
Figure2: ScreenshotofaVRsceneinwhichtheuser
hasthetasktoidentifythedifferentdiscriminatorybe-
4 DialogueManagementandInteraction
haviorsobservedinthepreviousscenethroughnatural
Strategy
langagedialogwithavirtualcharacter.
Oursystemadoptsamixed-initiativedialogueman-
3 Systemoverview agementstrategycombiningpredefinedsequences
withopen-endedinteractionviaaLargeLanguage
Withinthisframework,ourdemonstratorconsists Model(LLM)API.Predefinedsequencesinclude
of three main stages. In a first step, the user is replayed discrimination scenes, system explana-
immersed,viaaVRheadset,inasimulatedscene tions,andrecoverymechanismsforsensitiveuser
depictingadiscriminatorysituationenactedbytwo inputs. During open-ended dialogue, a dialogue
autonomousvirtualcharacters(Figure1). Thiscor- staterepresentationtracksdiscussiontopics,scene
respondstotheWitnessStage. Inasecondstep,the progression,andcriticalevents.
userinteractswithinnaturallangagewithavirtual
charactertoidentifyandanalyzethedifferentprob- 4.1 GeneralArchitecture
lematicbehaviorsobservedinthescene. Through
As shown in Figure 3, the system integrates an
dialogue,thecharacterhelpstheuseridentifysitu-
Automatic Speech Recognition (ASR) module, a
ationsofdiscriminationthathemayhaveobserved
dialoguecontroller,atext-to-speechsynthesizer,a
in the scene played out by the two virtual actors,
VRanimationmanager,andanLLM-basedchatbot.
remindinghimofdifferentmomentsinthescene
WeusetheGoogleSpeechAPI forASR,inworld-
and pointing out problematic behaviours (Figure
tts-1-max1 forspeechsynthesis,theUnityVRen-
2). This is the Discussion Stage. In a final step,
gine2foranimation,andtheGemini-2.5-flashLLM
theuserreplaysthesamesceneinVRsimulatedby
fordialogturngeneration.
thetwovirtualactors,butinthestep,theuserem-
The dialogue controller combines state-based
bodyingthediscriminatedcharacter,andattempts
managementwithopenconversationalcapabilities,
to respond to the discriminatory behavior of the
virtual actor in order to resolve or transform the 1https://inworld.ai/
situation. ThisistheConfrontationStage. 2https://unity.com/solutions/vr

Contextual Spoken
Speech text
Language
speech Recognition Understanding
text+dialog state+
STOP warning+script labels
Dialog State dialog history
Update yes + dialog state
yes Warning
End detection
Speech dialog ? ?
Synthesis Answer no no Dialog State
+ Generation Script ID
VR animation
dialog history
yes Script + dialog state
detection
Script (text+VR) Script ID ?
no
text + metadata
dialog controller
Script Chatbot LLM Prompt
Sequences text prompt Generation
Figure3: Architectureofthedialoguecontroller.
ensuringbothrobustnessandflexibilityinhandling cific situations that must be addressed before the
sensitivesocialinteractions. dialogue can be concluded. For instance, during
theDiscussionstage,theuserisexpectedtocom-
4.2 DialogueController mentoneachdiscriminatorysituationidentifiedin
LLM-basedagentsfacetwomainchallenges: main- the Witness stage. Each situation is represented
taininglong-termcoherenceandpreventingharm- byauniquelabel,andthedialoguestatestructure
fulorinappropriatebehavior. Previousstudieshave tracks which labels have already been discussed
addressedtheseissuesthroughmemoryabstraction andwhichremainpending.
techniques(Leeetal.,2023;Seoetal.,2025)and
Contextual Spoken Language Understanding
outputconstraints(Rebedeaetal.,2023). Ourap-
(CSLU) - This module analyzes the automatic
proachintegratesboththroughadynamicprompt
transcriptionofuserspeechinrelationtothecur-
chainingmechanismandanexplicitdialoguestate
rentdialoguestate. Itprovidesfourprimaryfunc-
representationguidingconversationflowandgoal
tions: (1)detectingdiscriminatorysituationsbased
completion.
onthecurrentdialoguestageandupdatingthedi-
Our approach draws inspiration from these
aloguestatetoreflectnewlydiscussedsituations;
worksbyintegratingbothadynamicpromptchain-
(2)triggeringpredefinedscriptedsequencesinre-
ing mechanism, which continuously updates the
sponse to the dialogue state and user input; (3)
LLMprompthistorytoguidetheconversation,and
detecting the completion of a dialogue stage and
an explicit dialogue state representation that su-
returningcontroltothemainVRmenusystem;and
pervises dialogue flow and ensures all goals are
(4) identifying problematic situations originating
fulfilledbeforetheconversationends.
fromeithertheuserortheLLM,andinitiatingcor-
Inadditiontotheseenhancedmemorymethods, rectivescriptedsequencesorsafelyterminatingthe
weimplementedaproblematicsituationdetector
interaction.
and a contextual scripted dialogue router, which
ScriptedSequences- Thisdatabasecontainspre-
cantemporarilyoverrideLLMcontrolwhenneces-
definedVRsequencesassociatedwitheachstage.
sary. Thesemodulesaredescribedbelow.
For instance, during the Witness Stage, the se-
Dialogue State - This data structure maintains quence is fully scripted, as will be described in
both the dialogue history and the set of goals thenextsection. IntheDiscussionStage,scripted
achievedduringtheinteraction. Theactivegoalset sequencescorrespondtoexplanatoryinterventions
dependsonthecurrentstage(Witness,Discussion, aboutspecificdiscriminationsituations,including
Confrontation) and consists of references to spe- legalimplicationsorcontextualclarifications.

PromptGeneration- WhentheCSLUmodule
allowstheLLMtogeneratethenextsystemutter-
ance, this module constructs the prompt contain-
ing instructions for the LLM API. The LLM is
expectedtoreturnaJSONstructurewithtwofields:
(1) a text output corresponding to the avatar’s
speech;and(2)anarray,possiblyempty,contain-
ing dialogue state labels identified in the current
conversationalstep. Thepromptitselfconsistsof
fourparts: (1)adescriptionofthepersonaplayed
Figure 4: Extract from the recorded corpus showing
by the LLM; (2) a description of the current dia-
face-to-faceinteractionwithdiscriminatorybehaviors.
loguestage,includingthesetofpossibledialogue
states, their labels, and examples; (3) general be-
havioralguidelinesforthepersona;and(4)stage- niquefrequentlyusedforcorporatetrainingondis-
specificinstructionssummarizingthedialoguehis- criminationawareness.
tory and directing the next conversational goal Basedonmotioncapturedatafromtherecorded
basedonthedialoguestaterepresentation. corpus,bodyanimationswerecreatedusingiClone
andintegratedintoUnity. Facialexpressionswere
AnswerGeneration- Whethertheresponseorig-
extractedfromthevideosusingOpenFace(Amos
inatesfromascriptedsequenceoranLLMoutput,
et al., 2016). In Unity, we developed two main
this module generates the corresponding VR in-
animationlibraries, talkingandlistening, andde-
structions for speech synthesis and avatar move-
signedadditionalidlemovements. Thesebehaviors
ment.
werederivedfromthecorpus,enhancedwithMix-
DialogueStateUpdate- Ateachinteractionstep, amo assets, and informed by our previous work
thedialoguestaterepresentationisupdatedbased onvirtualcharacteranimation. Intotal,weimple-
ontheselectedscriptedsequenceortheprocessed mented8idle,10listening,9talking,19facial,and
LLMoutput. 16headmovementanimations.
Animationsarelayered(body,face,andhead)to
5 UseCase: OrdinarySexismin generate varied full-body behaviors. Their selec-
ProfessionalSituations tion(talking,listening,oridle)dependsonanima-
tionstatevariablesinUnity,automaticallyupdated
Thedevelopedtrainingtoolisillustratedthrough
bythedialoguecontroller. Alightweightalgorithm
ascenariodepictingordinarysexisminthework-
ensuresanimationvariability,whilelipmovements
place. Thesceneinvolvesaconversationbetweena
aresynchronizedwithspeechusingtheSALSAlip-
malesupervisorandhisfemaleemployeeregarding
synctool.
animportantassignment. Althoughthesupervisor
intends to entrust her with the task, he expresses 6 Conclusion
doubts about her ability to lead a team. The sce-
nariowasdesignedbasedondescriptionsofordi- WepresentaVRtrainingsystemthatcombinesa
narysexisminprofessionalsettings(Grésy,2009, LargeLanguageModel–drivendialoguecontroller
2015), incorporating common behaviors such as: withrealisticvirtualcharacterstoaddresseveryday
condescensionandpaternalism(e.g.,“mysweet- sexism in professional contexts. The system re-
heart”),denigration(e.g.,“youdon’thavetheca- liesonahybridarchitecturethatintegratesscripted
pacity for this job”), indirect seduction (encour- sequences with open-ended dialogue, balancing
agingstereotypicalfemininity),maternityoffence interactionflexibilitywithcontrolinsensitiveex-
(e.g., “it’s not the right time for another child”), changes.
part-time bias (e.g., “you’re lucky you’re not do- Theproposedusecasedepictsaworkplacesce-
ing anything tomorrow, Wednesday”), and sexist nario inspired by real instances of ordinary sex-
remarksorjokes. ism. Futureworkwillextendtheapproachtoother
Two professional actors from the company formsofsocialbiasandincludeinitialevaluations
NextLevel performed the scene (Figure 4). Both ofuserengagementandlearningoutcomesbased
haveextensiveexperienceinforumtheatre,atech- onpost-interactionsurveys.

References Traian Rebedea, Razvan Dinu, Makesh Narsimhan
Sreedhar,ChristopherParisien,andJonathanCohen.
Brandon Amos, BartoszLudwiczuk, Mahadev Satya-
2023. NeMoguardrails: Atoolkitforcontrollable
narayanan,etal.2016. Openface: Ageneral-purpose
andsafeLLMapplicationswithprogrammablerails.
face recognition library with mobile applications.
InProceedingsofthe2023ConferenceonEmpirical
CMUSchoolofComputerScience,6(2):20.
Methods in Natural Language Processing: System
Demonstrations,pages431–445,Singapore.Associa-
Keith Anderson, Elisabeth André, Tobias Baur, Sara
tionforComputationalLinguistics.
Bernardini,MathieuChollet,EviChryssafidou,Ionut
Damian,CathyEnnis,ArjanEgges,PatrickGebhard,
SeongbumSeo,SangbongYoo,andYunJang.2025. A
et al. 2013. The tardis framework: intelligent vir-
promptchainingframeworkforlong-termrecallin
tualagentsforsocialcoachinginjobinterviews. In
llm-poweredintelligentassistant. InProceedingsof
InternationalConferenceonAdvancesinComputer
the30thInternationalConferenceonIntelligentUser
EntertainmentTechnology,pages476–491.Springer.
Interfaces,pages89–105.
AugustoBoal.1972. Catégoriesduthéâtrepopulaire.
Travailthéâtral,6:3–26.
MerijnBruijnes,JeroenLinssen,andDirkHeylen.2019.
Specialissueeditorial: Virtualagentsforsocialskills
training.
LeonardoCampillos-Llanos, D.Bouamor, ÉricBilin-
ski,Anne-LaureLigozat,PierreZweigenbaum,and
S.Rosset.2015. Descriptionofthepatientgenesys
dialoguesystem. InSIGDIALConference.
BrigitteGrésy.2009. Petittraitécontrelesexismeordi-
naire. AlbinMichel.
Brigitte Grésy. 2015. Le sexisme dans le monde du
travail,entredénietréalité. Technicalreport,Rap-
portduConseilsupérieurdel’égalitéprofessionnelle
entrelesfemmesetleshommessolidaire.
LynneHall,SusanJJones,RuthAylett,ElisabethAn-
dre, Ana Paiva, Gert Jan Hofstede, Arvid Kappas,
YukikoNakano,andToyoakiNishida.2011. Foster-
ingempathicbehaviourinchildrenandyoungpeople:
interactionwithintelligentcharactersembodyingcul-
turallyspecificbehaviourinvirtualworldsimulations.
INTED2011Proceedings,pages2804–2814.
GibbeumLee,VolkerHartmann,JonghoPark,Dimitris
Papailiopoulos,andKangwookLee.2023. Prompted
LLMsaschatbotmodulesforlongopen-domaincon-
versation. InFindingsoftheAssociationforCompu-
tational Linguistics: ACL 2023, pages 4536–4554,
Toronto,Canada.AssociationforComputationalLin-
guistics.
MagalieOchs,Jean-MariePergandi,AlainGhio,Carine
André, Patrick Sainton, Emmanuel Ayad, Auriane
Boudin,andRoxaneBertrand.2023. Aforumtheater
corpus for discrimination awareness. Frontiers in
ComputerScience,5:1081586.
D. Pautler, Vikram Ramanarayanan, Kirby Cofino,
P.Lange,andD.Suendermann-Oeft.2018. Leverag-
ingmultimodaldialogtechnologyforthedesignof
automatedandinteractivestudentagentsforteacher
training. InSIGDIALConference.
Alexander Prange, Margarita Chikobava, P. Poller,
MichaelBarz,andDanielSonntag.2017. Amulti-
modaldialoguesystemformedicaldecisionsupport
insidevirtualreality. InSIGDIALConference.
