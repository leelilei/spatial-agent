Title: A Voice-Controlled Dialogue System for NPC Interaction using Large Language Models

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/survey_paper/pdfs/phase1_adjacent/07_BK04_NPC_Interaction.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T02:55:12+00:00
- page_count: 10
- status: ok
- text_char_count: 34654

Metadata:
- author: Milan Wevelsiep ; Nicholas Thomas Walker ; Nicolas Wagner ; Stefan Ultes
- doi: unknown
- keywords: unknown
- subject: IWSDS2025 2025

Outline:
- Introduction (page 1)
- Related Work (page 1)
- Concept (page 2)
- Prototype Development (page 3)
- User Study (page 4)
- Results (page 6)
- Discussion (page 7)
- Conclusion (page 9)

Markdown Content:

A Voice-Controlled Dialogue System for NPC Interaction using Large
Language Models
MilanWevelsiep,NicholasThomasWalker,NicolasWagner and StefanUltes
NaturalLanguageGenerationandDialogueSystems
Otto-Friedrich-UniversityofBambergBamberg,Germany
nicholas.walker@uni-bamberg.de, stefan.ultes@uni-bamberg.de
Abstract Byevaluatingthishybridapproach,weaimtode-
termine its impact on the player experience, par-
This paper explores the integration of voice-
ticularlyinthecontextofnarrative-drivengames.
controlleddialoguesystemsinnarrative-driven
Specifically, we address the following research
videogames,addressingthelimitationsofexist-
ingapproaches. Weproposeahybridinterface questions:
thatallowsplayerstofreelyparaphraseprede-
fined dialogue options, combining player ex- 1. Howdoestheuseofavoice-controlledinter-
pressivenesswithnarrativecohesion. Thepro- face impact the immersion and user experi-
totypewasdevelopedinUnity,andalargelan- enceinagamewithanarrativefocus?
guagemodelwasusedtomapthetranscribed
voiceinputtoexistingdialogueoptions. The 2. DoestheplayerusingthisVCIhaveasense
approachwasevaluatedinauserstudy(n=14) offreedomgivenarestrictedsetofpredefined
thatcomparedthehybridinterfacetotraditional dialogueoptions?
point-and-clickmethods. Resultsindicatethat
theproposedinterfaceenhancestheplayer’sde- 3. Towhichdegreeofaccuracycantheplayer’s
greeofjoyandperceivedfreedomwhilemain- spoken responses be reliably mapped to a
tainingnarrativeconsistency. Thefindingspro-
givensetofdialogueoptions?
videinsightsintothedesignofscalableanden-
gagingvoice-controlledsystemsforinteractive
Thekeycontributionofthisworkliesinanap-
storytelling. Futureresearchshouldfocuson
proachtoenablespokeninteractioninanarrative-
reducinglatencyandrefininglanguagemodel
drivengamethatbalancesplayerfreedomwithnar-
accuracy to further improve user experience
rativeconsistency. Wepresentfindingsthathigh-
andimmersion.
light the potential of this approach in enhancing
1 Introduction
immersionandusersatisfactionwhilemaintaining
cohesivestorytelling.
Voiceinteractioninvideogamesremainsaniche
Theremainderofthepaperisstructuredasfol-
yet promising feature, especially as advances in
lows: Section 2 presents and discusses other ap-
technology offer new possibilities for immersion
proachesthatincludevoicecontrolintogamesand
and interaction of the player. Traditional ap-
discusseshowourapproachdiffers. Section3con-
proachestovoice-controlleddialogueswithNon-
tainsthecoreconceptofthevoice-controlleddia-
Playable Characters (NPCs) in games generally
logue system with a description of its realization
fall into two categories: reading out pre-written
inSection4. Sections5,6,and7presenttheuser
dialoguelinesorfreespeechinputinAI-generated
studydesign,theresultsandtheirdiscussion.
dialogues. Theformeroftenlimitsplayerexpres-
sion,whilethelattercanlacknarrativeconsistency
2 RelatedWork
and control. This paper aims to present a novel
approachthatservesasamiddlegroundbetween Voicecontrolasanarrativedeviceinvideogames
thesetwoapproaches,combiningtheflexibilityof has gained significant attention for its poten-
playerinputwithstructurednarrativecohesion. tial to enhance player immersion (Allison et al.,
Thegoalofthispaperistoexploretheimplemen- 2020). Natural voice interactions are generally
tationofavoice-controlledinterface(VCI)thatal- well-received,astheyenhanceplayerflowandre-
lowsplayerstofreelyphrasetheirresponseswhile duceidentitydissonance(Carteretal.,2015). Play-
still choosing from pre-defined dialogue options. ers often mimic character voices (Allison et al.,

2019;OskingandDoucette,2019),deepeningim- tended this concept by incorporating sentiment
mersion, though this can be challenging when analysistoadaptNPCresponsesbasedonplayer
there are differences in player and character at- emotions, thereby enhancing engagement. Simi-
tributes such as gender (Carter et al., 2015). Per- larly, Bot Colony (Joseph, 2019) and Vaudeville
sistentissueswithvoiceinterfacesincludeunnat- (Bumblebee-Studios,2023)utilizedAI-drivendia-
ural interactions, difficulty recalling commands, loguesystemstogenerateNPCresponses. While
slowerresponsetimescomparedtobuttoninputs theuseofLLMsindialogueswithNPCs,suchas
(Allison et al., 2019), and recognition failures thoseinVaudeville,cancreatehuman-likedialogue
(Zargham et al., 2022). This section reviews no- thatenhancesplayerengagement,theyalsopresent
tableapproachesspecificallyforvoice-controlled challenges including hallucinations, inconsisten-
dialogueswithnon-playablecharacters(NPCs). cies,anddifficultymaintainingnarrativecoherence.
Oneestablishedapproachistheuseofread-out- Fraseretal.’s(Fraseretal.,2018)sentiment-driven
loud interfaces, where players speak predefined approachdemonstratedimprovementsinemotional
dialoguelinestointeractwithNPCs(Oskingand immersion;however,concernsregardingscalability
Doucette,2019)(Cuebit,2018). Here,playerscan- in larger game environments and negative player
notfreelyphrasetheirvoiceinputbutarerestricted reactions to AI-generated dialogue remain (Cox
to the phrasing of the dialogue option they are andOoi,2024;Akouryetal.,2023).
choosing. Thismethodisreliableandcanenhance Building on these existing methods, this paper
immersionbyencouragingplayerstoembodytheir proposesamiddle-groundsolutionthatintegrates
characters. Forinstance,FlowersforDandan(Os- thestrengthsofbothapproaches. Byallowingplay-
kingandDoucette,2019)usedaread-out-loudin- ers to use free-form speech while mapping their
terfacewhereplayersverballyselecteddialogueop- inputtopredefineddialogueoptions,ourmethod
tionsbyreadingthetextofthedialogueoption,re- seekstomaintainimmersionanddeliveranatural
sultinginhigheremotionalengagementcompared interactiveexperiencewithoutcompromisingnar-
to traditional point-and-click controls. Similarly, rativecontrol. Thishybridapproachoffersamore
theDragonbornSpeaksNaturallymodificationfor scalable and robust solution for voice-controlled
Skyrim(Cuebit,2018)adoptedthisapproachtocre- dialoguesinnarrative-drivengamesbyaddressing
atemoreimmersiveplayer-NPCinteractionswith- thechallengesidentifiedinearlierresearch.
out the need for complex AI systems. The main
advantageofread-out-loudinterfacesistheirprac- 3 Concept
ticalintegrationintoexistinggames,astheyrelyon
predefined dialogue options and require minimal Thecoreoftheproposedapproachliesinamiddle-
changestothegame’sdialoguesystem. However, groundsolutionforintegratingvoiceinteractionin
therestrictivenatureofreadingoutpredefineddia- narrative-focused video games. It combines pre-
loguelinesmaylimittheplayer’ssenseofagency, defineddialogueoptionswiththeplayer’sability
reducingimmersionoverextendedplaysessions. to paraphrase freely. To achieve this, players are
Dynamicdialoguegenerationrepresentsanother givenpredefineddialoguechoicesthatcontainvery
approach,whereNPCresponsesaregeneratedin concisely worded versions of the core messages.
real-timeusingAItechniquessuchasnaturallan- However,insteadofaskingtheplayerstoreadthem
guage processing (NLP) or large language mod- outloud,theyareencouragedtoparaphrasethese
els(LLMs). Thisapproachprovidesplayerswith optionsintheirownwords. Forexample,anoption
greaterfreedomandmorenaturalinteractionsby like"Askformoreinformation"canbeexpressed
allowingthemtospeakfreelyratherthanselecting as "Could you give me more details?". While in
from predefined options. For example, the game some cases the participants nonetheless opted to
Façade(MateasandStern,2003),latermodifiedby readthetextasgivenornearlyso,othersweremore
Dow et al. (Dow et al., 2007), employed a "Wiz- creativeintheirformulations. Hence,apre-defined
ard of Oz" technique to simulate natural speech dialogueflowcontrolstheoveralldialoguewhile
input. Building on top of its underlying AI sys- userscanspeakfreelyandnaturally.
tems—natural language processing, autonomous The overall architecture of modelling the dia-
character behaviour, and a drama manager—this logue and processing new user input is shown in
approachfostereddynamicandimmersiveconver- Figure1. Newuserinputisfirstprocessedinthe
sations. Fraser et al. (Fraser et al., 2018) ex- Understandingcomponentthatutilizesalargelan-

LLM
User Input
Understanding Figure 2: A screenshot of the tutorial-section of the
game. Thetwodialogueoptions,displayedinGerman
language,translateto"Howdotheflowerslooklike?"
User Input and"Offersupport".
Options
Dialog Flow prototypewasbuiltusingUnity,chosenforitsflexi-
bilityandextensivelibraryofassets. Unityhandled
System Response Progression
allgamemechanics,visualelements,characterin-
teractions,anduserinterfacecomponents. Custom
Figure1:Overalldialoguearchitecture:anLLMisused
C#scriptsmanagedcoregameinteractions,suchas
tomapnewuserinputtooneoftheuserinputoptions
dialogueflow,NPCresponses,andplayercontrols.
definedbythedialogueflow.
Thegameenvironmentandcharacterswerecreated
usingfreeUnityAssetStoreresources,providing
guage model to map the user input to one of the afunctionalgameworldforvoiceinteractiontest-
possibledialogueoptions. Theseoptionsarepart ing. AscreenshotofthegameisshowninFigure
of the pre-defined dialogue flow and represented 2. Inthetutorialshowninthefigure,theplayeris
intextualform. Thelargelanguagemodelisthen instructedbyanNPCtohelpsearchforflowersin
prompted to either map the user input to one of theforestbyselectingoneoftwooptionsofhow
thedialogueoptionsgiventheprevioussystemre- torespond.
sponse,ortomapittomisunderstood.
Voice Interaction: Player speech input was cap-
Oncetheuserinputismappedtooneofthepre- turedinUnityandprocessedthroughtheWhisper
defineddialogueoptions,thedialogueprogresses AI service for transcription. Given that the lan-
to the next node of the pre-defined dialogue flow guagemodelperformedbetterwithEnglishinput,
whichdefinesthesystemoutputalongwithanew thetranscribedGermantextwastranslatedintoEn-
setofdialogueoptionsaspossibleuserinputs. The glishviatheGoogleCloudTranslationAPIbefore
new set of dialogue options is subsequently used furtherprocessing.
together with the following user input in the Un-
Dialogue Management: A structured dialogue
derstandingcomponent.
graph,implementedwithUnity’sinternaltoolsand
Thus,thisconceptdrawsfromread-out-loudin-
customC#scripts,servedasthebackbonefordia-
terfaces(OskingandDoucette,2019)anddynamic
logueflow. Eachnodeinthisgraphrepresenteda
input methods (Fraser et al., 2018; Bumblebee-
specificnarrativepointlinkedtopredefinedplayer
Studios, 2023) alike. It allows player freedom
options. Playerinputwasmappedtotheseoptions
and the capability to maintain narrative control.
using the Llama-2 13B language model, hosted
UnlikefullygenerativeNPCresponses,whichof-
on an Nvidia A100 GPU. The model received a
tenlackcoherence,thisapproachreliesonastruc-
promptthatincludedthetranscribedandtranslated
tureddialoguegraphtoensureconsistencywhile
response,thecurrentNPCdialogue,andavailable
enablingnaturalvoiceinteraction. Allowingplay-
dialogue options. The model then returned the
erstophrasetheirresponsesfreelyisexpectedto
option number that best matched the player’s in-
enhanceimmersionandengagementcomparedto
tent. Prompt engineering was applied by using
restrictiveread-aloudinterfaces.
langchain to improve mapping accuracy and re-
ducelatency. Anexcerptofthesystemmessageis
4 PrototypeDevelopment
showninFigure3.
The proposed concept is realized in a prototype UserInterface: DevelopedwithinUnity,theuser
implementation of a narrative-driven game. The interfacedisplayedavailabledialogueoptionsand

Figure3: Anexcerptofthesystemmessageusedinthefew-shotprompting. Thesystemmessageincludesan
explanationofthetaskandexamplesonhowtomapplayer’sresponsestooptions.
providedimmediatevisualfeedback. Whenplay- thebasiccontrolsandmechanics.
ersusedvoiceinput,theUIindicatedongoingpro- Limitations: The game’s world and characters
cessing and highlighted the chosen option after areconstructedfromdifferentresourcesfromthe
recognition, helping players understand the sys- Unity Asset Store. Therefore, the game environ-
tem’sresponsetotheirspokeninput. mentappearsvisuallyinconsistentandtheNPC’s
facialexpressionsandanimationsarelimited. Both
KeyFeatures: Theprototypeincludesseveralkey
aspectsleadtoapresumablylessimmersiveandbe-
designelementstoenhanceplayerexperienceand
lievableexperience. Responselatencyinthevoice
immersion. Thegameadoptsafirst-personperspec-
interfacepresentsanotherissue,withdelayssome-
tive,allowingplayerstointeractdirectlywiththe
timesinterruptingthenaturalflowofconversation.
environmentandNPCstocreateamoreengaging
Finally, while the automatic German-to-English
experience. While in a dialogue, the player can
translationsystemgenerallyperformswell,itocca-
choose the dialogue options hands-free, i.e., the
sionallymisinterpretsnuancedphrases,whichcan
player does not need to press a button to start or
resultinfaultymappingofplayer’sspeechinputto
stopthevoiceinput. Afterabriefperiodofsilence
thedialogueoptions.
detection,Unityprocessestheplayer’sspeechand
matchesitwiththeavailabledialogueoptions. The
5 UserStudy
VCI also provides a mechanism for revising dia-
logue options. When the system misinterprets a The user study aimed to evaluate the proposed
player’sinput,phrasessuchas“Ididn’tmeanthat” voice-controlled interface (VCI) by comparing it
triggera"Misunderstood"option. Inordertoavoid with a traditional point-and-click interface (PCI).
mentaloverloadbyvisualizingthisadditionalop- Thestudycombinedusabilitytesting,A/Btesting,
tion,therevise-optiononlybecomesvisibleupon andsurveystoassessthesystem’simpactonuser
selection. Theparticipantsintheuserstudyhave experience, perceived freedom, and system accu-
beenmadeawareofthatoptioninaninitialintro- racy.
duction. Theprototypealsoincludesatutorialde- Thestudyinvolved14participants,consistingof
signedtohelpplayersfamiliarizethemselveswith an equal number of male and female individuals,

6 6
6
5
4
3 3
2
2
1 1 1
0
0
vlow low neutral high vhigh
tnuoma
AffinitytoVideoGames/VoiceInterfaces inquirefurtheraboutthisissueorignoreitand
focusonfindingthekey. Eachsessionended
uponreachingoneofthegame’sthreepossi-
bleoutcomes. Thethreeendingscorrespond
tolow,mediumandhighlevelsofempathyas
determinedbythelevelofempathyshownto
Felixintheplayer’sresponsesoverthecourse
ofthedialogue.
4. Post-PlayQuestionnaire: Participantscom-
pletedaquestionnaireassessingtheinterface
theyhadjustused.
5. SecondPlaythrough: Participantsreplayed
Aff.toVideoGames Aff.toVoiceInt.
themaingamewiththealternativeinterface,
followedbythesamequestionnaire.
Figure 4: Self-reported affinity towards video games
andvoiceinterfacesbytheparticipants.
6. FinalQuestionnaire: Acomprehensiveques-
tionnairecapturedadditionalmetricslikeac-
agedbetween23and36years(meanage: 29,stan- curacy,enjoyment,andoverallpreference.
darddeviation: 4). Mostparticipants(11)helduni-
Thestudywasconductedonalaptopequipped
versitydegrees,andallwerenativeGermanspeak-
with the Unity-based prototype. Voice input was
ers. Participantswerepersonallyrecruitedandin-
captured using a Logitech webcam microphone,
cluded a mix of friends, acquaintances, and indi-
chosen for its accuracy over the laptop’s built-in
vidualswithnocloseconnectiontotheresearchers.
microphone. Participantscompletedquestionnaires
Thisgrouprepresentedvariedlevelsoffamiliarity
onthesamelaptop. Audiorecordingsdocumented
with gaming and voice interfaces. While partici-
verbalinteractions,whilelogscapturedsystemre-
pantshadmoderatelyhighexperiencewithvideo
sponses,dialoguechoices,andobservationalnotes.
games,theirexposuretovoiceinterfaceswascom-
Two primary data sources, questionnaires and
paratively limited (see Fig. 4). Participants alter-
play-throughdocumentation,informedthestudy’s
natedbetweenthetwointerfacestocounterbalance
findings.
order effects, with one group using the VCI first
Questionnaires: Participantsrespondedtoaseries
andtheotherstartingwiththePCI.Theprocedure
of structured questions using seven-point Likert
includedthefollowingphases:
scales. Thequestionnaireswereadaptedfromex-
1. IntroductionandOrientation: Participants isting instruments, namely the SASSI (Hone and
were briefed on the study, signed consent Graham,2000)forassessingthespeechinterface
forms,andreceivedinstructionsongameplay withregardtotheusabilityaspects,andtheGUESS
mechanics. Apresentationhighlightedtheuse (Vieiraetal.,2019)formeasuringvideogamesat-
ofvoiceinput,includingthecorrectionfeature isfaction and user experience. The adapted ques-
formisunderstoodinputs. tionnairecoveredfivescales:
• SystemResponseAccuracy: Assessedhow
2. Tutorial Level: Participants completed a
reliablyplayerinputsweremappedtoprede-
short tutorial using the VCI to familiarize
finedoptions(ItemsI1–I2).
themselveswiththesystem. Assistancewas
providedduringthisphaseasneeded.
• Likeability: Measured user enjoyment and
perceivedfreedom(ItemsI3–I4).
3. Main Game Playthrough: Participants
playedthemaingamewithoneinterfacewhile
• CognitiveDemandandHabitability: Eval-
the researcher minimized observer effects.
uated ease of use and confidence in issuing
ThetaskofthegameistohelptheNPCFelix
voicecommands(ItemsI5–I6).
to find a missing key. During this task, the
dialoguehintsthatFelixisbotheredbysome- • AnnoyanceandSpeed: Capturedfrustration
thing else, and the player has the option to anddelaysduringgameplay(ItemI7).

• Immersion: Examined how natural and en- Table 1: Summary of the Results for the Voice-
ControlledInterface
gagingtheinteractionsfelt(ItemI8).
• Preference and Overall Assessment: As- Item Median Mean
sessedwhichinterfaceplayerspreferred(Item I1:AccuracyofMapping 5.0 4.89
I2:CorrectionofMisunderstoodInput – –
I9).
I3:DegreeofJoy 5.0 4.93
I4:ExpressingFreedom 4.0 3.93
PlaythroughDocumentation: Logsrecordeddia- I5:EaseofUse 4.0 4.07
loguechoices,LLMprompt-responses,andvoice I6:ConfidenceinUsingtheVCI 3.0 3.86
I7:Annoyance 4.5 4.38
inputaccuracy. Audiorecordingsandobservational
I8:Immersion 3.0 3.68
notesprovidedqualitativeinsightsintouserbehav-
OverallAssessmentandPreference:
ior,naturalnessofinteractions,andsystemrespon-
Useinrealgames 5.5 5.43
siveness. Preferenceifimproved 6.0 5.79
The study faced several limitations that must be
acknowledged. Thesmallandrelativelyhomoge-
neous sample, consisting of younger participants user experience. Items I3, I5, I6, I7, and I8 were
withhighereducation,isnotrepresentativeofthe analysed:
broader gaming population. The limited dura- DegreeofJoy(ItemI3): Participantsrateden-
tionofthestudyrestrictedparticipants’familiarity joyment of the VCI with a median of 5.0 and a
withtheinterfaces,potentiallylimitingthelearning meanof4.93,suggestingamoderatelypositiveex-
curve and long-term usability assessment. Some perience. When compared directly with the PCI,
prototypelimitations,suchaslatency,translation the VCI scored higher (median 5.5, mean 5.43),
inaccuracies,andlimitedNPCanimations,likely indicatingenhancedenjoymentthroughvoiceinter-
influenceduserperceptionsofthesystem. Factors action.
like mood, time of day, and external distractions Ease of Use (Item I5): Ease of use received
couldalsohaveimpactedparticipantperformance mixedratings,withamedianof4.0andameanof
andfeedback. 4.07. Participantsnotedhighercognitivedemand
for the VCI due to the need for paraphrasing. In
6 Results
comparingbothinterfacesdirectlywitheachother,
participantsreportedtheVCIasmoredemanding
The results of the user study are presented in
(median2.5, mean3.07). Inpart, thiscanbedue
this section, focusing on the impact of the voice-
to higher familiarity with a traditional interface.
controlledinterface(VCI)onimmersion,userexpe-
However,thementalloadforputtingaparaphrased
rience,perceivedfreedom,andaccuracyofspoken
dialogueoptionintoone’sownwordsmostlikely
inputs. A total of 14 participants completed the
furthercontributedtothis.
study,whichinvolvedgameplaywithboththeVCI
and a traditional point-and-click interface (PCI), ConfidenceinUsingtheVCI(ItemI6): Con-
followed by corresponding questionnaires. An fidence levels varied, with a median of 3.0 and a
overview of the results for the VCI is shown in meanof3.86. Participantsexpressedmoderatecon-
table1. fidencebutreporteduncertaintyregardingwhether
Thequestionnaireresponseswerecollectedon theirphrasingwouldbecorrectlyrecognized,sug-
a7-pointLikertscalerangingfrom“stronglydis- gestinganeedforimprovement.
agree” (1) to “strongly agree” (7). For positively Annoyance(ItemI7): Generalannoyancewas
phrasedstatements,highervaluesindicateamore low(median5.0,mean5.21),butparticipantsgave
favorable response, while for negatively phrased amoreneutralratingoftheirattitudetowardsthe
statements,thescalewasreversedtoensureconsis- VCI response time (median 3.5, mean 3.93). Re-
tencyininterpretation,wherehighervaluesalways ducinglatencycouldsignificantlyimprovetheover-
reflectapositiveattitudetowardstheVCI. allexperience.
Immersion (Item I8): The VCI provided
ImpactonImmersionandUserExperience
slightly better immersion compared to the PCI
(R1)
(median 3.0, mean 3.57), but neither fully repli-
Research Question R1 evaluated the overall im- cated natural dialogue. Improvements in natural
pactoftheVCIonimmersionandotheraspectsof languageprocessingareneededtoenhanceimmer-

sionfurther. Table 2: Summary of participant responses to direct
comparisonquestionsbetweenthevoice-controlledin-
terface (VCI) and the point-and-click interface (PCI).
SenseofFreedom(R2)
HighervaluesindicateagreaterpreferencefortheVCI.
ResearchQuestionR2examinedparticipants’per-
ceivedfreedomwhileusingtheVCI: Item Median Mean
Expressing Freedom (Item I4): Participants I3:Joy(VCIvs.PCI) 5.5 5.43
I4:ExpressingFreedom(VCIvs.PCI) 5.0 5.07
feltmoderatelyfreetoexpressthemselves(median
I5:EaseofUse(VCIvs.PCI) 2.5 3.07
5.0, mean 4.5). While compared to the PCI, the I3:Boredom(VCIvs.PCI) 6.0 5.50
VCI allowed more authentic expression (median I8:Immersion(VCIvs.PCI) 4.0 4.36
5.0, mean5.07), thelimitationsofpredefinedop-
tions occasionally hindered free expression (me-
InterpretationofResults
dian3.0,mean3.36).
The user study findings show that the VCI proto-
DegreeofAccuracy(R3) type was generally well-received by participants,
offering notable advantages in engagement and
ResearchQuestionR3focusedontheaccuracyof
user experience compared to the conventional
mappingspokenresponsestodialogueoptions:
point-and-click interface (PCI). Participants ex-
AccuracyofMapping(ItemI1): Mappingac-
pressed a preference for the VCI, indicating its
curacy was rated positively (median 5.0, mean
potential to enhance player involvement and en-
4.89), with a system accuracy of approximately
joyment, despite the presence of technical issues
90%. Participantsoftenadheredcloselytoprede-
likeresponselatencyandspeechrecognitionchal-
finedphrasing,positivelyinfluencingaccuracy.
lenges.
CorrectionofMisunderstoodInput(ItemI2):
Impact on Immersion and User Experience
Thecorrectionfeaturewasrarelyusedduetoinfre-
(R1): ParticipantsfoundtheVCIenjoyable,though
quentmappingerrors. However,itshiddennature
delaysinprocessingvoiceinputcausedfrustration
ledtoparticipantsoftenoverlookingthisfunction-
andmoderateannoyance. Confidenceinusingthe
ality, suggesting a need for better visibility and
systemwasmixed,likelyduetotheunfamiliarity
usability.
ofcombiningpredefinedoptionswiththefreedom
toparaphraseresponses. Improvementsinresponse
OverallAssessmentandPreference
timeandsystemreliabilityareessentialtoenhance
ParticipantsratedtheVCIpositivelyforpotential immersionandusercomfort. Despitetheseflaws,
useinrealgames(median5.5,mean5.43). While the VCI had a slight advantage over the PCI in
directpreferencesbetweentheVCIandPCIwere termsofimmersion,highlightingitspotentialfor
mixed(median4.0,mean4.36),mostparticipants narrative-drivengames.
indicated they would use the VCI if its accuracy Sense of Freedom (R2): Participants appreci-
andspeedwereimproved(median6.0,mean5.86). ated the ability to paraphrase predefined options,
Additionally, no significant correlation was which contributed to a sense of authenticity and
foundbetweenparticipants’familiaritywithvideo self-expression. However, the restricted nature
gamesorvoiceinterfacesandtheirperceptionof ofpredefinedchoicesoccasionallylimitedpartic-
theVCI.ThissuggeststhattheVCIisaccessible ipants’senseoffreedom. Futureiterationsofthe
and engaging for a broad audience, regardless of VCIcouldimproveflexibility,reducingperceived
priorexperience,supportingitspotentialappealin constraintsandenhancingplayerempowerment.
diversegamingcontexts. AccuracyofMapping(R3): Participantsgen-
erallyfoundtheVCIpredictable,thoughinconsis-
7 Discussion tenciesinspeechrecognitionaffectedhowreliably
spokeninputwasmappedtodialogueoptions. The
Thissectionoffersacomprehensivediscussionof correctionfeatureformisunderstoodinputswasun-
the user study results and final reflections on the derutilizedduetoitshiddenpresentation. Despite
voice-controlledinterface(VCI)prototype,synthe- theseissues,thetechnicalapproach—usingalan-
sizingthefindings, implications, limitations, and guagemodel(LLM)formapping—showspromise,
directionsforfutureresearch. particularlywithimprovedspeechrecognitionand

responsiveness. eral ways by participants. For instance, an "Ask
formoreinformation"dialogueoptionmaybein-
PracticalandTheoreticalImplications
terpretedaspertainingtospecificorgeneralinfor-
The positive reception of the VCI suggests that mation. The specificity or generality of dialogue
voiceinteraction,particularlyinnarrativecontexts, optionsmaythusconstituteanadditionalfactorfor
isanengagingfeatureforvideogames. Thehybrid participantexperiencesthatwouldbeofinterestto
approachofcombiningpredefineddialogueoptions subsequentresearch.
withparaphrasingoffersascalablesolutionforin- Technical limitations also played a significant
tegratingvoicecontrolintogameswithoutcompro- roleinshapinguserexperience. Latencyissuesand
mising narrative coherence. Allowing players to inconsistenciesinspeechrecognitiondisruptedcon-
"playasthemselves"enhancesplayerembodiment, versationflowandreducedimmersion. Thefixed
especiallyingameswhereplayeragencyisacore timerequiredforvoicerecognition,combinedwith
feature,suchasrole-playinggames(RPGs). delaysintranscriptionandlanguagemodelprocess-
Addressing technical limitations such as re- ing,significantlyaffectedusersatisfaction. Addi-
sponse time and speech recognition accuracy is tionally,thelackofexpressivecharacteranimations
essentialforthecommercialadoptionoftheVCI. andauthenticvoiceoutputfurtherhinderedimmer-
Improvements in these areas would significantly sionandthebelievabilityofNPCinteractions.
enhance player experience, making the interface A final limitation worth mentioning regarding
morereliableandenjoyable. Addingtheflexibility immersionisthatvariousaspectsoflanguagesuch
to toggle the VCI on and off would give players assarcasm,irony,orothernuancedaspectsofhow
greatercontrol,cateringtodiversepreferences. humansnaturallycommunicatewereoutofscope
Thestudyalsocontributestounderstandinghow forthisstudy. Therelativeadvantagesofavoice-
voiceinteractioncanbeeffectivelyintegratedinto controlledinterfaceoverapoint-and-clickinterface
videogames. Unliketraditionaltop-downcommu- willlikelybemoststronglyobservableinasystem
nication,theVCIallowsformorenaturalinterac- that incorporates further subtleties of human ex-
tionswithnon-playablecharacters(NPCs),foster- pression.
ingimmersionbyenablingplayerstoprojecttheir
FutureResearch
identityontothecharacter. Toachievedeeperim-
mersion,improvementsinsystemspeed,accuracy, Future research should prioritize addressing the
andNPCresponsivenessarestillrequired. technicalandmethodologicallimitationsidentified
inthisstudy. Enhancingthespeedandaccuracyof
Limitations
voice recognition through real-time transcription
Thestudyfacedseverallimitationsthataffectthe and more advanced language models could sig-
generalizabilityofthefindings. Methodologically, nificantlyimprovetheVCI’sperformance. Incor-
the short duration of the study restricted partic- poratingdynamicdialoguegenerationcouldalso
ipants’ ability to become familiar with the VCI, providemoreflexibleandadaptiveplayer-NPCin-
limitinginsightsintolong-termusability. Thecon- teractions,addressingtheconstraintsofpredefined
trolled environment may not fully replicate real- dialogueoptions.
worldgamingconditions,influencinginteractions Long-termstudiesareneededtounderstandthe
andfeedback. Additionally,thesmallsamplesize sustainedeffectsofvoiceinteractiononplayeren-
andparticipanthomogeneitylimittheapplicability gagementandimmersion. IntegratingtheVCIinto
ofthefindingstoabroadergamingaudience. commercialgamesforextendedperiodswouldpro-
An additional limitation of the study is the in- vide valuable insights into how players adapt to
fluence of the presented options on the players’ and perceive the system. Additionally, future re-
thinking. Thespecificwordingoftheoptionsmay searchshouldexploretheroleofvoiceinteraction
influencethewayinwhichparticipantsphrasetheir infosteringemotionalconnectionsbetweenplayers
statementsinthedialogue. Furtherworkwhichana- andNPCs,particularlythroughimprovedNPCani-
lyzesdifferencesinuserinputdependentuponhow mations,responsivedialogue,andenhancedplayer
optionsarepresentedorifoptionsaredisplayedat agency.
allwouldlikelyyieldadditionalinsights. Dynamic Dialogue Generation within Dia-
Similarly,specificswithinthedialogueoptions logue Graphs: Dynamic dialogue generation is
may also be interpreted in specific or more gen- a promising direction for enhancing flexibility in

voiceinteractions. Thecurrentprototyperelieson Fraser Allison, Joshua Newn, Wally Smith, Marcus
predefineddialogueoptions,limitingadaptability. Carter,andMartinGibbs.2019. FrameAnalysisof
VoiceInteractionGameplay. InProceedingsofthe
By integrating dynamic dialogue generation into
2019 CHI Conference on Human Factors in Com-
dialoguegraphs,NPCresponsescanbegenerated
putingSystems,pages1–14,GlasgowScotlandUk.
based on the player’s phrasing and narrative con- ACM.
text,improvingnaturalinteractionflow.
Bumblebee-Studios. 2023. Vaudeville. https://
This hybrid approach, using language models
bumblebeestudios.itch.io/vaudeville.
to generate context-aware responses while main-
tainingthestructureprovidedbydialoguegraphs, MarcusCarter,FraserAllison,JohnDowns,andMartin
Gibbs.2015. PlayerIdentityDissonanceandVoice
couldofferamorepersonalizedexperience. NPC
Interaction in Games. In Proceedings of the 2015
responsescouldvarybasedonplayerphrasing,past AnnualSymposiumonComputer-HumanInteraction
interactions,andstorylinecontext,makingconver- in Play, pages 265–269, London United Kingdom.
sationsmoreengagingandlifelike. However,chal- ACM.
lengessuchasmaintainingemotionalauthenticity,
Samuel Rhys Cox and Wei Tsang Ooi. 2024. Con-
ensuring lip synchronization, and minimizing la- versationalInteractionswithNPCsinLLM-Driven
tencyneedtobeaddressed. Futureresearchshould Gaming: Guidelines from a Content Analysis of
PlayerFeedback. InAsbjørnFølstad,TheoAraujo,
explore lightweight language models capable of
SymeonPapadopoulos,EffieL.-C.Law,EwaLuger,
efficientoperationwithingameenvironments.
MortenGoodwin,SebastianHobert,andPetterBae
Brandtzaeg,editors,ChatbotResearchandDesign,
8 Conclusion volume 14524, pages 167–184. Springer Nature
Switzerland,Cham. SeriesTitle: LectureNotesin
Thisstudycontributestothegrowingfieldofvoice ComputerScience.
interaction in video games, particularly NPC in-
Cuebit. 2018. Dragonborn Speaks Naturally. https:
teractions. ThehybridVCIapproach—combining
//www.nexusmods.com/skyrimspecialedition/
predefineddialogueoptionswiththeabilitytopara- mods/16514?tab=description.
phrase—hasproventobeanengagingfeaturethat
StevenDow,ManishMehta,EllieHarmon,BlairMac-
enhancesaplayer’ssenseoffreedomandoverall
Intyre, and Michael Mateas. 2007. Presence and
userexperience. Allowingplayerstointeractnatu-
engagement in an interactive drama. In Proceed-
rally,intheirownwords,createsamorepersonal- ingsoftheSIGCHIConferenceonHumanFactors
izedexperiencethatcanalignwellwithnarrative- inComputingSystems,pages1475–1484,SanJose
CaliforniaUSA.ACM.
drivengames.
While the study’s findings show the potential JamieFraser,IoannisPapaioannou,andOliverLemon.
of voice-controlled interfaces, the technical and 2018. Spoken Conversational AI in Video Games:
EmotionalDialogueManagementIncreasesUserEn-
methodological challenges identified must be ad-
gagement. InProceedingsofthe18thInternational
dressed for long-term success. Improvements in
ConferenceonIntelligentVirtualAgents,pages179–
systemspeed,reliabilityandmoreadvancedchar- 184,SydneyNSWAustralia.ACM.
acterdesignarecriticalforimpactingthesenseof
Kate S. Hone and Robert Graham. 2000. Towards a
immersiontoagreaterextent. Withtheseenhance-
toolfortheSubjectiveAssessmentofSpeechSystem
ments,voiceinteractioncouldbecomeanintegral Interfaces(SASSI). NaturalLanguageEngineering,
partofvideogamedialoguesystems,providinga 6(3&4):287–303.
richerandmoreimmersiveplayerexperience.
EugeneJoseph.2019. FromVirtualtoReal: AFrame-
work for Verbal Interaction with Robots. In Pro-
ceedingsoftheCombinedWorkshoponSpatialLan-
References guage Understanding, pages 18–28, Minneapolis,
Minnesota.AssociationforComputationalLinguis-
NaderAkoury,QianYang,andMohitIyyer.2023. A
tics.
FrameworkforExploringPlayerPerceptionsofLLM-
GeneratedDialogueinCommercialVideoGames. In M.MateasandA.Stern.2003. Façade: AnExperiment
FindingsoftheAssociationforComputationalLin- inBuildingaFully-RealizedInteractiveDrama. In
guistics:EMNLP2023,pages2295–2311,Singapore. GameDeveloper’sConference: GameDesignTrack.
AssociationforComputationalLinguistics.
HunterOskingandJohnA.Doucette.2019. Enhancing
FraserAllison,MarcusCarter,andMartinGibbs.2020. Emotional Effectiveness of Virtual-Reality Experi-
WordPlay: AHistoryofVoiceInteractioninDigital enceswithVoiceControlInterfaces. InDennisBeck,
Games. GamesandCulture,15(2):91–113. AnasolPeña-Rios, ToddOgle, DaphneEconomou,

Markos Mentzelopoulos, Leonel Morgado, Chris-
tianEckhardt,JohannaPirker,RoxaneKoitz-Hristov,
JonathonRichter,ChristianGütl,andMichaelGard-
ner,editors,ImmersiveLearningResearchNetwork,
volume1044,pages199–209.SpringerInternational
Publishing,Cham. SeriesTitle: Communicationsin
ComputerandInformationScience.
Estela Aparecida Oliveira Vieira, Aleph Campos Da
Silveira,andRoneiXimenesMartins.2019. Heuris-
tic Evaluation on Usability of Educational Games:
A Systematic Review. Informatics in Education,
18(2):427–442.
NimaZargham,JohannesPfau,TobiasSchnackenberg,
andRainerMalaka.2022. “IDidn’tCatchThat,But
I’ll Try My Best”: Anticipatory Error Handling in
a Voice Controlled Game. In CHI Conference on
HumanFactorsinComputingSystems,pages1–13,
NewOrleansLAUSA.ACM.
