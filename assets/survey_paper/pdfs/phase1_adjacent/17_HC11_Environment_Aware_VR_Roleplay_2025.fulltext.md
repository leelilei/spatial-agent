Title: vr25a-sub1687-cam-i6

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/survey_paper/pdfs/phase1_adjacent/17_HC11_Environment_Aware_VR_Roleplay_2025.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T03:49:17+00:00
- page_count: 39
- status: ok
- text_char_count: 117089

Metadata:
- author: unknown
- doi: unknown
- keywords: unknown
- subject: VGTC Conference Paper

Outline:
- vr25a-sub1687-cam-i6 (page 1)
  - Introduction (page 1)
  - Related Work (page 2)
    - Simulating Human Behaviors with LLM Agents (page 2)
    - LLMs in Robotics and Interactive Games (page 2)
    - Summary (page 2)
  - System Implementation (page 2)
    - Schema (page 2)
      - System Context (page 3)
      - Objects (page 3)
      - Characters (page 3)
      - Spots (page 3)
      - Communication (page 3)
      - Overall Schema Architecture (page 3)
    - Prototype System as a Customizable Plugin (page 3)
    - Agent's Interactions and Conversations (page 3)
      - Action generation process (page 3)
      - Agent's Animations (page 4)
      - Agent's Dialogues (page 4)
    - User Inputs (page 4)
    - Scenario Example: ``Adding an Apple to the Shopping Basket from the Wood Box'' (page 4)
      - Agent Interaction Sequence (page 4)
      - User Interaction Sequence (page 5)
    - Scenarios (page 5)
      - Scenario 1: Fruit and Vegetable Store (page 5)
      - Scenario 2: Convenience Store (page 5)
      - Scenario 3: Art Gallery (page 5)
      - Scenario 4: Game Room (page 6)
      - Scenario 5: Fast-Food Store (page 6)
  - Methodology (page 6)
    - Apparatus and Study Procedure (page 6)
    - Participants (page 6)
  - Findings (page 6)
    - Token Usage and Responsiveness (page 6)
    - Virtual Environment Localization and Reasoning (page 7)
      - Spatial Localization via Object System (page 7)
      - Spatial Localization via Coordinate System (page 7)
      - Hallucination (page 7)
    - Conversations and Behaviors Based on Object Characteristics (page 7)
      - Conversations (page 7)
      - Interactions (page 7)
    - Awareness of User Interaction Cues (page 7)
      - Movement (page 7)
      - Pointing (page 7)
      - Touching (page 8)
      - Grabbing and Releasing (page 8)
    - Movements and Object Interactions (page 8)
      - Movement and Navigation (page 8)
      - Object Relocation (page 8)
    - Contextual Role-Play Conversations and Behaviors (page 8)
      - Conversations (page 8)
      - Interactions (page 8)
  - Discussion (page 8)
    - Summary (page 8)
    - Ethics of VR Role-Play Interactions with Agents (page 8)
    - Limitations and Future Work (page 9)
      - Scaling and Evaluating in Complex Scenarios (page 9)
      - Perceiving Virtual Environments via Text Prompts (page 9)
      - Enhancing Interaction Context (page 9)
      - Improving Responsiveness in Human-AI Interaction (page 9)
      - Addressing Limited Context Window (page 9)
    - Design Implications (page 9)
      - Objects and Containers (page 9)
      - Spots (page 9)
      - Interactions and Scenario Prompts (page 9)
  - Conclusion (page 9)
- vr25a-sub1687-cam-i8 (1) (page 12)
  - Abstract (page 12)
  - A Prompt (page 12)
    - A.1 System Prompt (page 12)
    - A.2 Scenario Prompt (page 14)
  - B Scenario Environment Setup (Scenario 2-5) (page 15)
  - C Schema Components (page 17)
    - C.1 Function List (page 17)
    - C.2 Object Element (page 17)
    - C.3 Character Element (page 18)
    - C.4 Character's Hand State Element (page 18)
    - C.5 Spot Element (page 18)
- vr25a-sub1687-cam-i30 (1) (page 19)

Markdown Content:

Exploring Large Language Model-Driven Agents for Environment-Aware
Spatial Interactions and Conversations in Virtual Reality Role-Play
Scenarios
ZimingLi* HuadongZhang† ChaoPeng‡ RoshanPeiris§
RochesterInstituteofTechnology
Figure1: (a)Theoverallschemaarchitectureofourproposedtextprompts, designedtoexploreenvironment-awarespatialin-
teractionsandconversationsofLargeLanguageModelagentsinvirtualrealityrole-playscenarios. Thearchitectureconsistsof
fivemaincomponents: SystemContext,Spots,Objects,Characters,andCommunications,eachwithitsownsubcomponents. (If
amaincomponenthasonlyonesubcomponentwiththesamename,itisnotseparatelylabeledinthediagram.) Fiverole-play
scenarioswereimplementedbasedonthisschema,whichare:(b)Scenario1:FruitandVegetableStore;(c)Scenario2:Conve-
nienceStore;(d)Scenario3:ArtGallery;(e)Scenario4:GameRoom;and(f)Scenario5:Fast-FoodStore.
ABSTRACT 1 INTRODUCTION
RecentresearchhasbegunadoptingLargeLanguageModel(LLM) ConversationalagentspoweredbyLargeLanguageModels(LLMs)
agents to enhance Virtual Reality (VR) interactions, creating im- areincreasinglybeingadoptedfortheirabilitytoreplicatehuman-
mersivechatbotexperiences. However,whilecurrentstudiesfocus likeconversationsacrossdiversecontexts[55,42,28,23]. Thein-
on generating dialogue from user speech inputs, their abilities to tegrationofLLMsenablestheseagentstonotonlyproducebeliev-
generatericherexperiencesbasedontheperceptionofLLMagents’ ableresponsesbutalsotomimicthenuancesofspecificdialogue
VRenvironmentsandinteractioncuesremainunexplored. Hence, interactions,includingservingasempatheticagentsforemotional
inthiswork,weproposeanapproachthatenablesLLMagentsto support, facilitating role-play for language learning, and tools for
perceivevirtualenvironmentsandgenerateenvironment-awarein- interviewandjobpreparation[62,17]. Unliketraditionalconver-
teractions and conversations for an embodied human-AI interac- sationalagents, whichrelyonpredefineddialoguepatterns, LLM
tion experience in VR environments. Here, we define a schema agents dynamically adjust their responses based on conversation
fordescribingVRenvironmentsandtheirinteractionsthroughtext context,leadingtomorenatural,engaging,andflexibleinteractions
prompts. Weevaluatetheperformanceofourmethodthroughfive thatcloselymimicreal-lifeconversations[9,45].
role-playscenarioscreatedusingourapproachinastudywith14 While previous research has integrated agents powered by ar-
participants. Thefindingsdiscusstheopportunitiesandchallenges tificial intelligence (AI) into virtual reality (VR) for applications
ofourproposedapproachfordevelopingenvironment-awareLLM likepersonalcompanions[34],education[33],jobtraining[49,48],
agents that facilitate spatial interactions and conversations within andconversationpractice[31,37],currentinteractiveagentsinVR,
VRrole-playscenarios. eventhoseincorporatingLLMs,aregenerallylimitedtoresponding
totextualorverbalinputs. Thislimitationunderminestherealism
IndexTerms: Virtualreality,role-playsimulations,generativeAI,
andimmersionoftheseagents,astheylackawarenessofthesur-
human-AIinteraction,largelanguagemodels,context-awareness
roundingenvironmentanduserinteractioncues,suchasobjecthan-
dling(e.g., pointing, orgrabbingobjects)andspatialmovements.
*e-mail:zl1398@rit.edu
†e-mail:hz2208@rit.edu Incorporating such environmental interactions in training scenar-
‡e-mail:cxpigm@rit.edu ios–especiallyfor individualswithintellectualand developmental
§e-mail:roshan.peiris@rit.edu disabilities[48,31,5,32]–couldenhancetrainingoutcomesbypro-
vidingmorerealisticandcontext-awareexperiences[7,19].
Recentadvancementsinhuman-AIinteractionresearchdemon-
stratethatLLM-poweredvirtualagentscanperceivetheirenviron-
mentthroughprovidedinformation,suchasthespatialrelationships

and characteristics of objects [35, 56, 15]. This indicates LLM human-like text, understand context-aware dialogues, and predict
agents, such as ChatGPT, can engage in meaningful interactions emotionalresponses[9,43,44,28]. ThesehaveenabledLLMsto
based on the context of their surrounding. Studies have also ex- simulatenuancedhumanconversationsandinteractions[6,21,47].
plored LLM-driven robots for executing tasks related to environ- LLMs have notably transformed the development of virtual
mentalobjects,guidedbyuserinstructions[51,52,45]. agents, shifting from scripted responses to dynamic, context-rich
Building on these insights and addressing the limitations men- interactions that mimic human behavioral patterns and emotional
tionedabove,ourstudyaimstodevelopandevaluateamethodthat nuances[46,60,24,31,53,37]. Forexample,Parketal.[42]pro-
enablesLLMagentstounderstandandrespondtospatialinterac- posedgenerativeagentsthatcansimulateawiderangeofbehav-
tionsandconversationsindynamicVRenvironments. Giventhat iorsthroughexperiencerecording,memorysynthesis,andadaptive
mostVRheadsetsprimarilysupporthandandheadtracking[4],we planning,enablingpersonalizedexperiencesandsocialinteraction
focusedonhand-basedinteractionsinthiswork.Ourmethodfacili- simulationsinvirtualenvironments.Hongetal.[23]introducedPI-
tatesenvironment-awarecommunicationsbasedonuseractionsand CAN,acontext-awareagentdesignedtoanswerusersqueriesand
dialogue. Forexample,inavirtualmuseum,ausermightpointto provideguidanceforsmootheronboardinginmetaversesettings.
anobjectanddiscussitwiththeguideagent,orinavirtualshop, Furthermore,otherhuman-behaviorsimulationssuchasinterac-
theycouldinquireaboutitemsfromashopkeeperagent. tive storytelling [11, 61], LLM agents enhance narrative interac-
Ourstudyfocusesonrole-playscenarios,exploringcommunica- tions,enablinguserstoengageindiverseanduniqueexperiences.
tionandinteractionwithLLMagentsinVRsettings.Whilevision-
based approaches (e.g., GPT-4 Vision [18, 39]) enable agents to 2.2 LLMsinRoboticsandInteractiveGames
“see”theenvironmentandperceiveuseractions, manyaspectsof TheintegrationofLLMsintoroboticsandinteractivegaminghas
virtualrole-playcannotbefullyconveyedthroughvisualinput.For enhancedthecognitiveandlinguisticcapabilitiesofrobotsandvir-
example,inastoresetting,anagentactingasashopkeeperrequires tualcharacters.Theseadvancementsenableagentstonavigatechal-
detailslikeitemlocationsandprices.Thisinformationisoftenob- lengesinbothphysicalandvirtualenvironments,asLLM-powered
scuredduetoocclusionsorthelimitedqualityofobjectmodelsand systemscaninterpretcomplexinstructions,adapttodynamicenvi-
texturesinvirtualenvironments. Additionally,vision-basedmeth- ronments,andaddresstasksrequiringcontextualawareness.
ods rely on capturing sequences of images over time to interpret Inrobotics,LLMsempowermachineslikeFigurerobots[18]to
userinteractions,whichcanintroducecomputationaloverheadthat handle complex commands and engage in meaningful dialogues.
compromisereal-timeresponsiveness[16].Toaddresstheselimita- Theirintegrationalsoenhancesroboticautonomy,enablingnaviga-
tions,thisstudyinvestigatesusingtextpromptsasamoreadaptable tionthroughcomplexenvironments,problem-solving,anddynamic
waytoconvey environmentalandinteractioncuesin virtual role- decision-makinginunpredictablescenarios[29,51,38,36].These
playcontexts,leadingtothefollowingresearchquestions(RQs): LLM-integratedsystemsgobeyondsimpletaskexecutionbyincor-
RQ1:Howcaninformationaboutvirtualenvironmentsanduser poratingstrategicplanningandreal-timeadaptability.
interactions be effectively communicated to an LLM agent using Similarly,ininteractivegaming,LLMstransformgamecharac-
textprompts? ters into responsive, narrative-driven entities that engage players
RQ2: WhatistheLLMagent’sviabilityandtaskperformance throughpersonalizedinteractions[58,27,12,13,10]. Bygenerat-
ingeneratingenvironment-awarespatialinteractionsandconversa- ing real-time language response, these characters adapt to player
tionsinrole-playscenarios,basedonperceivedenvironmentalin- choices, creating immersive, AI-driven storytelling experiences.
formationanduserinputs? Beyonddialoggeneration,LLMagentssuchasDEPS[54]enable
Toaddresstheseresearchquestions,wedevelopedaschemathat characterstolearnfromthegameenvironment,providingeffective
continuouslyinformsLLMagentsaboutdynamicVRenvironments planningandevolvingtheirbehaviorstocontinuallyengageusers.
andinteractionsviatextprompts(SeeFigure1(a)).Wethendevel-
opedasystemwithintheUnitygameengine[50]capableofgener- 2.3 Summary
atingmeta-informationaboutvirtualenvironmentsanduserinputs,
Building on prior works, we identified the AI-driven agents, es-
inaccordancewiththeproposedschema.Usingthissystem,wede-
pecially LLM agents, can simulate realistic human behaviors and
signedandimplementedaVRsimulationapplicationfeaturingfive
initiate interaction cues to complete tasks in both real-world and
role-playscenarioswithvirtualcharactersasLLMagents’avatars
virtualenvironments. However, limitedresearchhasexploredthe
(SeeFigure1(b-f)). Subsequently,weconducteduserstudieswith
applicationofcontext-awareLLMagentsinVR[53]. Toaddress
14 participants to evaluate the system, focusing on a behavioral
this gap, our study investigates spatial interactions and conversa-
evaluation of the agents’ environment-aware spatial communica-
tionsofLLMagentsinrole-playsimulationswithinVRsettings.
tioncapabilities,includinginteractionsandconversations,basedon
theirperformanceinthestudies.Ourcontributionsareasfollows: 3 SYSTEMIMPLEMENTATION
1)Developedaschemaarchitecture,implementedasacustomiz-
To answer RQ1, we developed a prototype system that uses a
able Unity plugin, that allows LLMs like GPT-4 Turbo to gener-
schemafortranslatingVRenvironmentdetailsandinteractionsinto
ateenvironment-awareinteractionandcommunicationcuesinVR
structuredtextpromptsforLLMagents. Thisschemaallowsgame
role-playsimulations.
engines, such as Unity, to interpret VR environments and their
2)AssessedLLMagentbehaviorsinaVRrole-playapplication
interactions into a series of prompts that guide the LLM agent’s
acrossfivescenariosdevelopedusingourproposedschema,gather-
environment-awareinteractionsandconversations.
ingdatafromuserstudieswith14participants.
3) Discussed opportunities, challenges, ethical considerations,
3.1 Schema
and design implications of using environment-aware LLM agents
Inspired by the prompting schemes for robotics proposed in pre-
inVRrole-playsimulations.
vious research [51], our schema defines five main components:
2 RELATEDWORK System Context, Objects, Characters, Spots, and Communica-
tion. These components, illustrated in Figure 1(a), were identi-
2.1 SimulatingHumanBehaviorswithLLMAgents
fied through trial and error and provide the necessary contextual
ThedevelopmentofAIcapableofsimulatinghumanbehaviorshas informationforrole-playscenariosintheVRenvironment. They
advancedsignificantly,withLLMstakingcenterstage. Initialde- systematicallydefinethestructureofthecontextprompt,whichin-
signedfortext-basedapplications,LLMshaveevolvedtogenerate formstheagent’scommunicationcuesandinteractionswithinthe

VRenvironment.Eachentityintheschemaisdescribedthroughan 3.1.5 Communication
element,withsubcomponentsdenotedas<[subcomponent]>.
The Communication component, described as <Communication
Messages>, manages action cues and dialogues between charac-
3.1.1 SystemContext
ters. It dynamically tracks previous actions and conversations to
The System Context component includes three subcomponents: helptheagentgenerateappropriatereactions. Additionally,itvali-
<SystemSettings>,<ScenarioSettings>,and<FunctionList>. datestheagent’sactionsbyconfirmingwhetherinvokedfunctions
<SystemSettings>definestheschema’sstructure,outliningthe aresuccessful, providingerrormessageswhennecessary. Anex-
rulesofthevirtualenvironment,includinginteractionprotocolsand ampleofcommunicationmessagesislistedinTable1.
the coordinate system. <Scenario Settings> specifies the roles,
rules,andobjectivesforthecurrentscenario(asdescribedinSec- <Player’srighthandpointsatCoffee(hot)>
tion3.6). <FunctionList>definestheavailableactionstheagent Customer(Player’srole):“Hello!Howmuchisthis?”
canperformwithintheenvironment,suchasmovingtoaspot,look- invalid <Avatar’slefthandgrabsCoffee(hot)>
ingatanobject,andinteractingwithobjectsusingeitherhand(e.g., <Error: The object is out of your interaction field.
grabbing,releasing,pointing,ortouching).Thesefunctionstrigger Pleasemovetoacloserspot.>
specificanimationsorinteractions,suchaswalkingorpickingup <AvatarmovestoCounterDeskSpot>
objects.Thefulldefinitionofthe<FunctionList>isshowninthe <Avatar’slefthandgrabsCoffee(hot)>
AppendixC.1. Server(Agent’srole):“Oh!Thishotcoffeeis$5.”
Additionally,functionscanbeintegratedoradjustbasedonthe
Table1:Anexampleofcommunicationmessages:Theplayer(‘cus-
scenario,providedtheyareanimatableandalignwiththeschema’s tomer’)interactswithacupofhotcoffeeandasksforitsprice. The
requirements. Insuchcases,theschemamaybeupdatedtoensure agent (‘server’) attempts to reach for the cup but is warned by the
thatobject-relatedcharacteristicremainconsistentwiththeoverall system.Itthenadjustsitsbehaviorandanswersthequestion.Anin-
scenedesign. validmessagewasexcludedfromthecontextduetoanerrorduring
theinteraction,andanerrormessagewasprovidedasfeedback.
3.1.2 Objects
The Object component comprises the <Object List> and <Con-
tainerList>,whichdetailobjectsandcontainersinthevirtualenvi- 3.1.6 OverallSchemaArchitecture
ronment. <ObjectList>includesmeta-informationsuchasobject
Allthecomponentsarecompiledintoatext-basedcontextprompt,
names,descriptions,positions,andgrabbability,while<Container
whichiscommunicatedtotheLLMagent.Thispromptinformsthe
List>describescontainersthatholdobjects(e.g.,abasketforhold-
agentofthemostrecentstateoftheVRenvironmentandguidesits
ingapples).AnObjectelementisshowninAppendixC.2.
interactionsandresponses. Thefullarchitectureoftheschemais
Objects are classified as fixed or movable and as containers or
outlinedinFigure1(a). SeeAppendixA.1fortheexamplesystem
non-containers,resultinginfourcombinations:fixednon-container
promptandAppendixDforacompletecontextpromptexample.
(e.g.,statues),movablenon-container(e.g.,apples),fixedcontainer
(e.g., shelves), and movable container (e.g., shopping baskets). 3.2 PrototypeSystemasaCustomizablePlugin
Containers can hold other objects, enabling hierarchical relation-
OurprototypesystemisimplementedasacustomizableUnityplu-
ships. Forexample, applesinsideashoppingbasketonacounter
gin that integrates with scenes during development. This plu-
establish a container-within-container relationship. These classi-
gindynamicallygeneratescontextpromptsbasedonourproposed
ficationshelpagentsunderstandspatialrelationshipsandperform
schema.
actions in the environment. See Figure 4 for an example of how
During environment creation process, VR designers configure
theobjectsarearranged. Anexampleofobjects’meta-information
thepluginbyspecifyingkeyelements,suchasthescenariodescrip-
organizedbasedontheschemaisprovidedinFigure3.
tion, game objects used in the scenario simulation, object names
anddescriptions,aswellaspropertieslikewhetherobjectsaremov-
3.1.3 Characters
ableorserveascontainers.Additionally,designerscandefinechar-
The Character component includes the <Character List> and acter names and assign spot prefabs within the scene to facilitate
<Character’s Hand State>. This component provides meta- expectedorrequiredinteractions. Otherconfigurationsettingsare
informationaboutcharacters,suchastheirname,positions,direc- automaticallyderivedbythepluginbasedonthescene’sstructure
tions, andhandstates(objecttheyareholding). Thisinformation andthepropertiesofthegameobjects.
helpstheagentgeneratehuman-likebehaviorandperceivethestate
ofothercharacters,particulartheuser,tofacilitateinteractions.An 3.3 Agent’sInteractionsandConversations
exampleofacharacter’shandstate’supdateprocessisprovidedin We incorporated OpenAI’s GPT-4 Turbo (‘gpt-4-0125-preview’)
Figure3. ACharacter elementisshowninAppendixC.3, anda intoourLLMagents,chosenforitsefficientcontextmanagement
Character’sHandStateelementisshowninAppendixC.4. andthoroughcomprehensionofextensivecontent. Onceprovided
with a context prompt, the agent’s response may involve actions
3.1.4 Spots (movements,objectinteractions)and/orverbaldialogues(SeeFig-
The Spot component, defined by the the <Spot List>, describes ure2). Fordialogues,thegameengineverbalizestheagent’stext
specificlocationsinthevirtualenvironmentthatofferaffordances asdetailedinSection3.3.3.
forinteractions. Forinstance,aspotmayindicateanidealposition We deliberately refrained from fine-tuning the agents’ interac-
foraccessingobjectsorpresentingexhibits,oranexitofthescene. tionsordialogues,aimingtoexploretheirbehaviorsacrossdiverse
Spotinformationincludesitsname(spot’saffordance),itsposition, scenarioswithoutpotentialbiasesthroughsuchadjustments[22].
and direction relative to the agent (enabling the agent to perceive
3.3.1 Actiongenerationprocess
thespot’sspatiallocation).Itcanbedynamicallyupdatedbasedon
changesintheenvironment. Thisensuresthatinteractionsremain TheactionsperformedbytheLLMagentfollowsafive-steppro-
consistentandoccurlogicallywithinthescene,suchaspreventing cess.
theagentfromreachinganobjectthroughwalls.ASpotelementis (1)Theagentselectsanintendedaction(e.g.,objectinteraction,
shownintheAppendixC.5. movement) from the function list provided in the context prompt

Figure2: ThecommunicationflowbetweenourVRsimulationapplicationandanLLM.Specifically,itdescribeshowtheresponsemessages
fromtheLLMarehandledbyoursystembeforepresentingthemwithintheVRenvironment.
(definedinSection3.1.1). Thisselectionrequiresidentifyingcor- suchasaMetaQuest,anduseVRcontrollerstointeractwiththe
rectparameterssuchasobject nameandspot name. scene.Thisinteractionincludespointingatitems(viaraycasting),
(2) To supply the parameters, the agent retrieves meta- grabbing items by pressing buttons, moving with the controller’s
informationfromtheprovidedlistsinthecontextpromptandinserts joystick,andinitiatingconversationsusingOpenAI’sdictationfea-
themintothefunctionparametersasperthepredefinedguideline. ture.UsercontrolismanagedinUnitythroughtheOculusIntegra-
(3)Thefunctioncallisvalidatedbythegameenginetoensure tionPackage.
itsexecutability. Ifvalid,thefunctionispassedtotheanimator;if Userinteractionsfollowsthesamerulesasagentbehaviors. For
invalid,anerrormessageisgeneratedandreturnedtotheagentas instance, users cannot grab or move fixed objects, nor can they
afeedback. Functionvaliditydependson: (a)matchingthecorrect collide with fixed objects and characters. The system tracks user
functionname,(b)ensuringparametersreferenceactualobjectsor behaviors using similar patterns applied to agents: recording the
spotsinthescene, and(c)adheringtopredefinedfunctionguide- player’s state (e.g., position, hand occupation). Each user action
lines(Section3.1.1). Forexample,theleft hand grabfunctionre- withinthesceneistranscribedintodescriptivetext,whichisthen
quirestheagent’slefthandtobefree,theobjecttobemovable,and senttotheagentsascontextwhentheuserinitiatesaconversation.
within the agent’s interaction range. The error message indicates Theinteractionprocessisturn-based: afteranagentcompletes
thereasonoftheaction’sinvalidityinthecurrentstate,whichalso its actions or dialogue, it waits for the user to provide an action
servesasahintfortheagentforitsreasoningandreferencetofixit cueorinitiateaconversation.Likewise,theusercanonlyconverse
afterward. orsendactioncuestotheagentoncetheagenthascompletedits
(4)Oncevalidated,theanimatorexecutesthecorrespondingin- actionsordialogue.
teraction,suchasananimationoftheagentgrabbinganobject. Toassistusersinperformingscenario’stasks,visualaidssuchas
(5) After execution, feedback is sent along with the context tooltips(indicatingobjectcharacteristics)andobjectoutlines(high-
prompttotheLLMagent, indicatingwhethertheactionwassuc- lightinginteractableelements)arealsoimplemented.
cessfulandupdatingtheagent’sstate.
3.5 Scenario Example: “Adding an Apple to the Shop-
3.3.2 Agent’sAnimations pingBasketfromtheWoodBox”
The agent’s avatar, created using Ready Player Me, is animated Thissectionprovidesanexampleofhowanagentorusercaninter-
through the Unity game engine. Facial expressions are managed actwithinafruitandvegetablestorescenebyaddinganapplefrom
withtheRealisticEyeMovementpackage,whilemouthanimations a wood box to a shopping basket. We outline how each system
are powered by Oculus Lipsync. We utilized Inverse Kinematics componentprocessestheseinteractionswithinthedefinedschema.
(IK)forskeletalanimations,ensuringprecisehandpositioningrel- To add an apple, the agent or user first needs to move to the
ativetotargetobjects. woodbox,grabanapplewithanemptyhand(e.g.,righthand),and
To enhance animation control, Unity’s Animator system man- releaseitintotheshoppingbasketheldintheotherhand.
agesbothmovementandhandanimations, withmasksandlayers In this context, the shopping basket is classified as a movable
enablingsimultaneousactions,suchascarryingobjectswhilemov- containerobject,theappleasamovablenon-containerobject,and
ing. Spatial movements were facilitated using Unity’s navigation thewoodboxasafixedcontainerobject. Thespotclosesttothe
mesh(NavMesh),whichhandlescollisionavoidanceandcharacter woodboxisnamed“AppleSpot.” Initially, twoapplesareinthe
turning.TheNavMeshsystemwasintegratedwiththeAnimatorto box,andtheagentoruserholdsanemptyshoppingbasketintheir
synchronizewalkinganimationsandoverallmovementincomplex lefthand. Theschema’scontextupdateprocessfortheseinterac-
environments. tionsisdepictedinFigure3.Eachobjectinthesceneisassigneda
uniqueidentifier,whichiscriticalforlocatingspecificobjectsdur-
3.3.3 Agent’sDialogues ingfunctioncalls.
Conversationsaregeneratedthroughwit.ai’sText-to-Speech(TTS)
featuretosimulatenaturallanguageinteractions. Optionally,cap- 3.5.1 AgentInteractionSequence
tionscanbedisplayedtoaiduser’scomprehension. TheLLMagentinitiatesitsactionsthroughfunctioncalls.
First, the agent identifies the closest spot to the apples by ei-
3.4 UserInputs
thercheckingthe‘closest spots’parameterintheObjectelementor
Users interact with the virtual environment similar to the agents, searchingthecontext’sspotlistfor“AppleSpot”orsimilardescrip-
performingactions,navigatingthescene,andengaginginconver- tions(Figure3(1)).Oncelocated,theagentmovestothespotusing
sations. To experience the application, users wear a VR headset, the‘move to(AppleSpot)’function,triggeringthegameengineto

Figure3:Theflowoftheexamplescenariowhichtheagentaddsanappletoitsshoppingbasket.Onlyupdatestoanelement‘field’areshown.
Characterandhandstateelementsaremergedforsimplicity,andelementsunrelatedtotheinteractions,suchas‘AppleSpot,’‘ExitSpot,’and
‘Apple(1)’,areomitted. (1)Theinitialelementsofkeyentitiesinthisscenario(excludingpropertiessuchasthecharacter’sandobject’sinitial
positionanddirection).Inthisstage,theagentholdsashoppingbasketwithitslefthandandstandsneartheExitspot.(2)Theagentheadsto
theapplespot.(3)Theagentgrabsanapplefromthebox.(4)Theagentputstheappleintotheshoppingbasketandinitiatesadialog.
animate thevirtual character’smovement andorientation towards schema, focusing on how the LLM agent can interact with envi-
thewoodbox(Figure3(2)). Amessage(“AvatarmovestoApple ronment to build meaningful conversations and interactions, and
Spot”)isthensenttotheLLMagentasfeedbackandappendedto achievescenarioobjectives.Onlyessentialobjectsrelevanttoeach
thecontext. role-play scenario were implemented in the schema. Figure 4 il-
Next, the agent locates an apple either by searching the object lustratesthearrangementofelementsinScenario1asanexample.
list for an apple associated with ‘Apple Spot’ or inspecting the (Scenario prompts and figures are provided in the Appendix A.2
contents of the wood box. To grab the apple, the agent calls the andB.)
function ‘right hand grab object(Apple(2)),’ which the game en-
gineprocesses, initiatingananimationforthevirtualcharacterto 3.6.1 Scenario1: FruitandVegetableStore
grasp the apple. A feedback message (“Avatar’s right hand grabs In this role-play scenario, the agent plays the role of a customer
Apple(2)”)issenttotheLLMagentandaddedtothecontext. The purchasingitems,whiletheuseractsasthecounterstaff. Theuser
systemupdatesthecharacter’shandstatetoreflecttheapplebeing providesverbalinstructionsbutcannotassistphysically(SeeFig-
held in the agent’s right hand and adjusts the object hierarchy to ure 1(b)). The scenario is completed when the “customer” gath-
indicatetheapple’sremovalfromthewoodbox(Figure3(3)). ers all the desired items, places them in a shopping basket, and
Finally,theagentreleasestheappleintotheshoppingbasketus- checks out. This scenario assesses the agent’s ability to interact
ing the function ‘right hand release object to container(Apple(2), withvariousobjects,suchasmovablecontainerobjects(shopping
Shoppingbasket),’promptinganotheranimation.Afeedbackmes- baskets),movablenon-containerobjects(fruitandvegetableitems),
sage(“Avatar’srighthandreleasesApple(2)toShoppingbasket”) andfixedcontainerobjects(likecashiercounters),whilenavigating
issenttotheagent,andthesystemupdatestheobjectandhandstate variousspotswithinthescene(SeeFigure4). Ituses5,747tokens
toreflecttheapple’sadditiontotheshoppingbasket(Figure3(4)). tosetuptheschema,containing34virtualobjectsand15spots.
3.5.2 UserInteractionSequence 3.6.2 Scenario2: ConvenienceStore
User interactions, performed through VR controllers, follow a Here, the agent is a counter staff member guiding the user (cus-
sequence similar to that of the agent. While the object struc- tomer)tolocateitemsinthestore(SeeFigure1(c)).Theagentuses
ture updates remain consistent, the communication messages dif- only verbal instructions and remains stationary, ensuring its item
ferslightlyfor‘releasingobjects’and‘moving’actionsduetothe identificationreliesonthescenesetupratherthanusercues. This
user’smoreflexibleinteractionstyle.Whenmoving,thedestination scenarioevaluatestheagent’sabilitytopinpointitemlocationson
isspecifiedusing‘X,Y,Z’coordinatesratherthanaspotname(e.g., shelvesandengageinconversationsregardingproductdetails,such
“Playermovesto(-0.46,0,1.48)”),andnocontainernameispro- aspricesanddiscounts. Thissceneuses7,650tokenstosetupthe
videdwhenreleasinganobject(e.g.,“Player’srighthandreleases schema,including76virtualobjectsand1spot.
Apple(2)”).Despitethesedifferences,LLMagentscanstillretrieve
relevantobjectinformationfromthesystemcontext,includingthe 3.6.3 Scenario3: ArtGallery
ObjectListandContainerObjectList.
Inthisscenario, theagentservesasatourguideinanartgallery,
whiletheuserisavisitor(seeFigure1(d)). Theagentleadstours
3.6 Scenarios
andprovidesexhibitinformation, dynamicallyrespondingtouser
Toevaluateourapproach, wedesignedfiverole-playscenariosin actions,suchaspointingatorstandingnearanexhibit. Thissce-
theUnitygameengine: afruitandvegetablestore,aconvenience nario focuses on the agent’s ability to facilitate communication,
store, an art gallery, a game room, and a fast-food store. These navigatetheenvironment,andprovidemeaningfuldescriptionsof
scenariosexaminedifferentaspectsofthecomponentswithinour fixednon-containerobjects(suchasstatuesandpaintings). Ituses

Figure4: TheenvironmentsetupofafruitandvegetablestoreinScenario1. Yellowoutlinesindicateinteractiveobjects. Grayovalshapeson
thefloorvisualizethespots. Greencuboidsmarkthestructuresofvisuallyhiddencontainersondesksurfaces. Thisfigureonlyrepresentsa
partofthescene.Onlyrepresentativeentitiesfromeachcomponentappliedwithinthescenariowereselectedfordisplayandlabeling.
3,982tokenstosetuptheschema,including11virtualobjectsand scenarios. The application ran on the laptop, which mirrored the
12spots. headset’sview.TheGoProcamerarecordedthelaptop’sscreenand
theparticipants’commentsandconversations. Additionally, tran-
3.6.4 Scenario4: GameRoom scriptsofconversationsandinteractionsbetweenparticipantsand
Thisscenariotakesplaceinagameroomwheretheagentanduser, agentsweresavedonthelaptopforanalysis.
actingasplaymates,taketurnsmovingtoysbetweenbaskets(See TheuserstudycomprisedademographicsurveyandaVRex-
Figure1(e)). Theusercanalsoinstructtheagenttomovespecific perience session. Participants began with the demographic ques-
toysoranswerquestionsaboutthebasketcontents. Thisscenario tionnaire followed by a practice session where they practiced the
evaluatestheagent’sobjectmanipulation,reasoningskills,andits basiccontrols(e.g.,pointing,touching,andgrabbingobjectsusing
awarenessofuser’sinteractioncues. Thissceneuses3,600tokens VR controllers, conversing with the agent) in a learning scenario
tosetuptheschema,including11virtualobjectsand3spots. (similar setting to other scenarios). Next, the participants experi-
encedeachscenarioinacounterbalancedorderwhileamoderator
3.6.5 Scenario5: Fast-FoodStore observed. A 5-minute break was provided between scenarios. In
total,thestudylastedamaximumof120minutes.
Inthisscenario,theagentactsasafast-foodcounterstaffassisting
a user (first-time customer) with ordering food (See Figure 1(f)). 4.2 Participants
Theuserprimarilyreliesonimplicitcues,suchaspointingatmenu
Werecruited14participantsfromtheauthors’institutionthrough
items. The scenario tests the agent’s ability to retrieve informa-
advertisementsandword-of-mouth. Participantswererequired to
tionfromfixedobjects,plantasks,andtransferitemsbasedonuser
beolderthan18yearsoldandfluentinEnglishtobeeligiblefor
instructions. This scene uses 4,167 tokens to set up the schema,
the study. Each participant received a compensation of 30 USD
including16virtualobjectsand6spots.
uponcompletingthestudy.
Themedianagescoreofthe14participantswas4(3=“18-24
4 METHODOLOGY
years old”, 4 = “25-34 years old”, 5 = “35-44 years old”). Nine
We conducted a study with 14 participants to answer RQ2 that ofthemidentifiedasfemale,whilefiveidentifiedasmale. Twelve
aimedtoevaluatetheLLMagents’abilitiestounderstandandre- ofthemweregraduatestudents,onewasanundergraduatestudent,
spondtothedynamicVRenvironmentsandtheirbehaviorsacross andonewasafacultymember.
thefivescenariosthatlistedinSection3.6.
Our user studies were conducted using an exploration experi- 5 FINDINGS
mentaldesign.Inthisformat,participantswereprovidedwithguid- ToanswerRQ2,weanalyzedagentbehaviorsobservedinuserstud-
anceandobjectivesforeachscenario,yettheyhadthefreedomto iesacrossfiverole-playscenarios.Athematicanalysis[8]assessed
plantheirinteractionsandconversations. Thisapproachwascho- agents’ interactions with the virtual environment and players, as
sentobetterexploretheagents’behaviorswithinvariousscenario wellasagents’taskperformanceinrole-playscenarios. Thesuc-
settings. cess rate (SR) is calculated as the agent’s successful completions
dividedbytheparticipant-initiatedattemptsforthegivenpattern.
4.1 ApparatusandStudyProcedure
Whileweadoptedanexplorationexperimentaldesign,itresulted
ThestudywasapprovedbytheIRBofficeoftheauthors’institu- in a diversity of behaviors in the agents across participants. This
tion. Theparticipantswererecruitedafterscreeningforanypoten- analysis highlights key themes of commonly observed behaviors,
tialhealthrisks(e.g.,nausea,anxiety)toensuretheirsafety. aswellasnotablevariations,includingerraticactionstriggeredby
Thestudytookplaceinalabattheauthors’institution.Tomin- specificinteractionswithaminorityofparticipants.
imizetheriskofVR-relatedmotionsickness,participantsweread-
5.1 TokenUsageandResponsiveness
visedtoremainseatedduringtheexperience.Theequipmentsetup
included a Meta Rift S headset, a GoPro camera, and a 15-inch Weexaminedtokenusageandagentresponsivenessbasedonuser
Windows 11 laptop. The study utilized the previously described interactions during the five provided scenarios. While the ex-

S1 S2 S3 S4 S5
spatialreasoningabilityusingrelativepositionsinObjectelements,
Mean 7389.21 9317.71 6023.79 5777.57 6330.64 player’sCharacterelement,andplayer’smovementcues.
SD 289.30 787.64 535.82 668.40 728.79
Table2:AveragetokenusageforScenarios1to5.
5.2.3 Hallucination
InScenario2,weobservedthattheagenthallucinatedobjectsnot
S1 S2 S3 S4 S5
presentedinthescene(P3-P6,P14). Forexample,P5’sagentsug-
Mean(seconds) 3.53 3.91 4.77 3.69 3.90
gestedAisle5wasnearthebackwall,adetailthattheagenthallu-
SD(seconds) 1.07 0.32 1.23 0.81 1.24
cinatedsincethewallswerenotdefinedintheObjectelementsof
Table3:AverageagentresponselatencyforScenarios1to5.
theschema.
5.3 Conversations and Behaviors Based on Object
ploratorydesignlimitsstrictquantitativeanalysis,thereporteddata Characteristics
offeranempiricaloverviewofusagepatternsandresponsivenessas
5.3.1 Conversations
evaluatedbyparticipants.
Themeantokenusageacrossthefivescenariosissummarized Agents used Object element descriptions to develop meaningful
inTable2. Theminimumtokenusageforcompletingascenario’s conversationsinScenarios2,3,and5,wheretheyactedasservice
taskswas4,850(P14,Scenario4),whilethemaximumwas11,281 staffs. InScenario5,agentsaccuratelystateditempricesandused
(P12,Scenario2).Asnonewobjectswereintroducedafterscenario thisinformationduringthecheckoutprocess.
setup(detailedinSection3.6),theincreaseintokenusageduringan Someagentsalsoprovidedadditionalinformationtoenrichcon-
experience session primarily reflects interaction and conversation versations,likeketchupbrandnames(P4,Scenario2)orchipnu-
dynamicsbetweentheuserandtheagent. Thisvariationdepends tritional details (P12, Scenario 2), though these were technically
ontheparticipant’sdecisionandtheagent’sresponses. “hallucinations.”InScenario3,agentsconvincinglyintroducedex-
ThemeanresponselatencyoftheagentispresentedinTable3. hibitsbasedontheirownknowledgeasLLMagents(thoseexhibits
While the majority of response latency can be attributed to LLM hadreal-worldcounterparts).
processing,networktransmissiondelays,andoursystemprocess-
InScenarios2and5,agentscouldintegrateobjectcharacteristics
ing time, participants occasionally experienced noticeable “lag”
intotheirconversations,especiallywithfixednon-containerobjects
when the agent reattempted to generate a response following an
likepostersandmenuboards. Forexample,inScenario2,agents
“error”messagefromoursystem.
initiated conversations about store deals based on poster descrip-
tions(P5,P12).
5.2 VirtualEnvironmentLocalizationandReasoning
5.2.1 SpatialLocalizationviaObjectSystem
5.3.2 Interactions
AsoutlinedinSection3.1.2,theObjectcomponentinourschema
AgentsalsoplannedtheirinteractionswithobjectsbasedonObject
classifies virtual environment entities into four types. Agents
elementinformation. InScenario1,agentsavoidedplacingwater-
demonstratedtheabilitytoperceiveandreasonaboutkeyobjects
melonsintoshoppingbasketswheninstructedtodoso(P1,P6),as
inrole-playscenariosusingthissystem.
thewatermelons’Objectelementindicatedthattheycouldnot be
This was specifically observed in Scenario 2, which was de-
placedintoshoppingbaskets.
signedtoassesstheagent’sabilitytoidentifyandlocateitems.The
agent accurately described item locations (P1-P14; Success Rate Conversely,inScenario5,whenparticipantsorderedquantities
(SR):100%),suchas“Themayonnaisejarsyou’relookingforare offooditemsexceedingtheactualamountsavailableinthescene,
inAisle4, Tier2.” Notably, theitem’sexacttierorshelfnumber agentsneitherrefusedtheordersnorinformedtheplayers,leading
wasspecifiedonlyinthe“shelftier”fixedcontainerobject,notin toerrorsinfulfillingtherequests(P5,P10).
theitem’sschema. Moreover,P8relocateda“juice”fromAisle3,
Tier 3 to Aisle 5, Tier 2, and the agent successfully identified its 5.4 AwarenessofUserInteractionCues
newlocation.
Agentsdemonstratedawarenessofuserinteractionscues,including
Beyond locating objects, agents could list items within a con-
movement,pointing,touching,andgrabbing.
tainer. InScenario4, allparticipantsexceptP2andP6askedthe
agentstolisttoysinabasket,andagentsaccuratelynamedthecon-
tents(SR:100%). InScenario2,agentsprovidedaisle-specificin- 5.4.1 Movement
formationwhenqueriedaboutanaisle’scontents(P6andP7),like
Agent’s awareness of the players’ movement were particularly
“Aisle6isallthewayatthebackofthestore,toyourright.You’ll
notedinScenario3,wheretheplayersfrequentlymovedaroundan
findcoffee,ketchup,andafewotheritemsthere.”(P7’sagent)
artgallery,agentswereabletotrackandrespondtotheusers’up-
datedpositions,adjustingtheirresponsesbasedonplayers’move-
5.2.2 SpatialLocalizationviaCoordinateSystem
ments.ThisalignswithfindingsdescribedinSection5.2.2.
TheObject,Character,andSpotcomponentsalsoprovidedagents
withrelativepositionanddirectioninformationtoassistinperceiv-
5.4.2 Pointing
ingtheenvironmentsanduserinteractions.
InScenario2,agentscoulddescribethestorelayoutwhenpar- Pointing was a key interaction in Scenarios 2, 3, and 5, helping
ticipantsaskedforitemlocations(P2-P5, P7, P8, P12, P14). For agentsinterpretuserreferences(SR:100%). InScenario5,forex-
example, P3’s agent directed them to the ice cream with, “Just ample,whenP11pointedattheOverheadMenuBoardsthatlisted,
headstraighttotheback,thentakealeft. Theicecream’sinthose ‘GiantBurgers’,‘FrenchFries’,and‘SpecialBurgers’,saying“Can
freezersagainstthewall.”Additionally,P14’sagentaccuratelyex- Igetonethisandthreeofthisandtwothisone?”,theagentcould
plainedhowtheaislenumberedinthestore. successfully interpret the request–“Sure, let me confirm your or-
In Scenario 3, as participants moved within the environment, der. You’dlikeoneGiantBurger,threepacksofFrenchFries,and
agentsidentifiednearbyexhibitsrelativetotheplayer’scurrentlo- twoSpecialBurgers,correct?”–demonstratingtheagent’sabilityto
cation (P1-P3, P5, P6; SR: 80%). This indicates that the agent’s contextualizepointingactionswithinconversations.

5.4.3 Touching suggest that agents effectively generated contextual conversations
andbehaviorsbasedonthespecificscenarios.
Thetouching(poking)interactionwaslessfrequentlyused. How-
ever,inScenario3,itsscenariopromptnoted,“Ifaplayertouches
5.6.1 Conversations
orgrabsanexhibit,pleasewarnthem,”aimingtosimulateareal-
isticartgalleryexperience. Whenparticipantstouchedanexhibit InScenarios2,3,and5,agentsactedasservicestaffsandactively
(P4,P5,P8-P11,P14),agentsrespondedappropriatelybyremind- engaged in scenario-appropriate conversations. For example, in
ingthemofgalleryrules(SR:87.50%). Scenario2,agentsprovidedreciperecommendationsbasedonthe
selected objects (P4, P11, P12) and calculated total prices of the
5.4.4 GrabbingandReleasing itemsbroughttothecounter(P1-P14;SR:92.86%). InScenario3,
Grabbing interactions were common in Scenario 2, where partic- agentsansweredquestionsaboutexhibitsbasedontheirknowledge
ipants often picked up items and asked agents for their informa- ofreal-worldcounterparts(P1-P14;SR:100%).AndinScenario5,
tion. Agents successfully responded to these cues and integrated agentsofferedmenusuggestionsbasedonplayers’preferencesand
the grabbed item into conversations (P1-P4, P8, P11, P12; SR: allergies(P4,P12-P14). Furthermore,whenparticipantsattempted
100%). In Scenario 4, agents also recognized objects that partic- toaskagentstoperformtasksoutsidethescenario’sintendedpur-
ipants moved between baskets (P1-P14; SR: 85.71%). However, pose, such as when participants in Scenario 2 demanded to take
theyoccasionallyfailedtotrackobjectmovementswhichcouldbe items out of the store for free (P6, P12), agents could inform the
due to the lack of specific information about target containers in playersandmaintaintheirroleaccordingtothescenariosettings.
userinteractioncues(P3,P7,P10,P11).
5.6.2 Interactions
5.5 MovementsandObjectInteractions Inadditiontoconversations,agentsperformedrole-appropriateac-
5.5.1 MovementandNavigation tions. Beyondcompletingtasksasperthescenariosetuporusers’
implications,suchasfinishingshoppinginScenario1andcollect-
Using the Spot system, agents demonstrated effective navigation
ingplayers’orderitemsinScenario5,weobservedthatinScenario
withinthevirtualenvironment. InScenario1,forexample,agents
3, agents could assume the role of tour guides. Here, they phys-
couldmovetospecificspotstocollectfruits,simulatingashopping
ically guided players around the art gallery as per their requests,
experience(P1-P14;SR:85.71%,withfailuresinP3andP13’sini-
providing a lifelike museum tour experience (P2, P4, P5, P7, P9,
tial attempts). Similarly, in Scenario3, agents couldmove to the
P11,P12,P14;SR:80%).
spotofanexhibitwhenguidingtheplayersthroughanartgallery
(P2,P4,P5,P7,P9,P11,P12,P14;SR:80%),orfollowtheplay-
6 DISCUSSION
erstoexhibitstointroducethem(P1,P7,P11,P14). Additionally,
6.1 Summary
inScenario4,agentscouldmovetothe“turnaroundspot”asper
thegame’srules(P4-P11; SR:60%). InScenario5, agentscould To address RQ1, we formulated schema consisting of five main
navigatearoundthedispenserstocollecttheplayers’ordereditems components: System Context, Objects, Characters, Spots, and
(P1-P14;SR:85.71%,withfailuresinP3andP5). Communications. This schema, implemented as a customizable
However, in Scenario 5, we observed navigation errors, where Unityplugin, facilitatesthespecificationofdynamicvirtualenvi-
agents moved among dispensers without collecting items during ronmentsandinteractioncuesthroughtextprompts,guidingLLM
its first few moves (P2, P4, P7, P9-P14), which was occasionally agentstoinitiatespatialinteractionsanddialogueswithinthevir-
verballyclaimedbytheagentas“working”ontheirorders. This tualenvironmentbasedonscenariosetupsanduserinputs.
reflects the challenges agents face in managing complex tasks, a We developed a VR simulation application featuring five vir-
knownlimitationofcurrentLLMsystems[41]. tualrole-playscenariosbuiltuponourproposedschema,integrat-
Moreover,duringtheexperiencesofP2,P4,andP9inScenario ingvirtualcharactersasavatarsofLLMagentspoweredbyGPT-
1, items accidentally fell onto the floor during their interactions. 4Turbo. Auserstudyinvolving14participantswasconductedto
Wheninstructedbyparticipantstopickuptheitems,agentsfailed evaluateagents’behaviorsacrossthesescenarios.Participantswere
toperformthistaskduetothelackofspotsneartheitems. These encouragedtofreelyengagewiththescenarioswhileadheringto
incidentshighlightedtheneedfordynamicspotsthatupdatetheir objectives and instructions. The agent’s behaviors were assessed
positionastheirassociatedobjectsbecomeunoccupied,aimingto throughobservationofuserstudiesandanalysisofinteractiontran-
ensure their reachability. (Although such functionality is feasible scripts, aimed at addressing RQ2. Our findings indicate that the
accordingtothecurrent‘Spotsystem’design,itwasnotspecifically agentscaneffectivelylocateobjects,engageinconversations,and
implementedinourscenesinthisearly-stageexploration.) initiateinteractionsbasedonourprovidedenvironmentalandcom-
munication cues. However, challenges were identified, including
5.5.2 ObjectRelocation LLM agents’ inaccuracies in managing complex multi-step plan-
Inscenariosthatinvolvedobjectsrelocation, suchasScenarios1, ning[26,45,41]andtheirtendencyto‘hallucinate’environments
4, and 5, agents can move objects between containers according and interactions [25], leading to unnatural and inconsistent inter-
tothescenario’ssettingsandinstructions(SR:86.84%). However, actions. Here, enhancing the specificity of system, scenario, and
weobservedrareinstanceswhereagentsattemptedtograbanitem objectdescriptionscouldmitigatehallucinationsrelatedtoenviron-
with a hand already occupied before releasing it. In such cases, mentsetups,whileprovidingmorecontextualdetailsininteraction
agentscouldstillcompletethetaskswhenexplicitlyinstructedby cuesmayaddresshallucinationsrelatedtouserinteractions[59].
theplayer.Similarly,inScenario5,ifagentseithercollectedincor-
rectitemsormisseditemsintheirorders,theywereabletocorrect 6.2 EthicsofVRRole-PlayInteractionswithAgents
these errors through player guidance (P4, P7, P8, P11, P14; SR: DuetothegenerativenatureofLLMagents,theirreactionscanbe
60%).Theinaccuraciesinthetaskcompletionobservedinthesein- unpredictable,reactingtoawiderangeofuserinput.Whilemodels
stancescouldbeattributedtocompoundedactionsnotconsistently suchasGPT-4andClaudeincorporateAIsafetymeasures[40,20],
registeringinthesystem[41]. we recommend that applications employing these agents imple-
mentadditionalrestrictionsandprovideclearguidanceinlinewith
5.6 ContextualRole-PlayConversationsandBehaviors
human-AIinteractionguidelines[3,57]forethicaldeployment.
Inourstudy,agentsweretaskedwithassumingrolesinvarioussce- Moreover, usersmayengageinimproperorharmfulbehaviors
nariostosimulaterealisticrole-playexperiences.Ourobservations towardagentsorvirtualenvironment,oftendrivenbycuriosityora

desiretotesttheagents’reactions.Inourpractice,interactionswere networklatency.Forthelatter,futureworkcouldfocusonenabling
limitedtobasicactionssuchasmovementandobjectmanipulation. agentstoautomaticallyretrieveinformationfromtheenvironment
Theagentsweredesignedtoignorecuesoutsidetheintendedsce- anduseractions,minimizingtheneedforuser-initiatedinteraction
nario. Userstudiesshowedthattheagentscouldmaintainconver- andcreatingamoreseamlessandimmersiveexperience.
sations and adhere to predefined roles, even when prompted with
actions beyond the scenario’s scope. Therefore, we recommend 6.3.5 AddressingLimitedContextWindow
thatdevelopersclearlydefinescenarioparametersthroughprompts In our user study, the maximum prompt tokens used to complete
toensureacontrolledandsafeinteractionenvironment,especially a scenario’s tasks was 11,281, while the GPT model used in our
foreducationalpurposes. prototypeoffersa128,000-tokencontextwindow. Thiscapacityis
Last but not least, there is a risk of users developing paraso- sufficientforsimulatingsmall-scalecommunicationandinteraction
cialbehaviorswiththeavatars,potentiallyleadingtoinappropriate scenariosinVR.Forlarger-scalescenariosimulations,futurework
emotionalattachments[1]. Aspreviousstudiessuggest[42], itis couldexploreoptimizationstrategiessuchasomittingdetailsand
crucialtoinformusersthattheseagentsareartificialentitiesandto propertiesofobjectslessrelevanttothespecificrole-playscenario
cautionagainstover-relianceordependenceonthem. fromtheschemawhentheyareoutsidethevirtualcharacter’sfield
ofviewanddividingthetasksamongmultiplesub-agentstobetter
6.3 LimitationsandFutureWork
manageandsummarizespecificcomponentsofthecontext[30].
6.3.1 ScalingandEvaluatinginComplexScenarios
6.4 DesignImplications
Our exploration focused on environment-aware VR agents in
fiverole-playscenarios,emphasizingbasicsocialinteractionsand Inthiswork,weidentifiedkeydesignelementsessentialforcreat-
object-basedcommunication. Theschemaincludedonlyessential ingimmersiveVRrole-playscenarioswithLLMagents.
objectsrelevanttoeachrole-playscenarios. However, theperfor-
6.4.1 ObjectsandContainers
mance of this approach in more complex settings, such as multi-
levelenvironments,dynamicinteractions,orscenarioswithnumer- Thecategoryofobject(e.g.,movablecontainer)shouldbedefined
ousobjectsandspots,remainuntested. Operatinginstaticsetups byitsrolewithinascenario,notitsreal-worldcharacteristics. For
alsolimitsagents’abilitytoadapttochangingenvironmentsorre- example, acoastermightbeamovablenon-containerinamarket
spondwhenusersinteractwhileawaitingLLMoutputs. whensoldasmerchandise,butafixedcontainerobjectinarestau-
Future works will focus on extending this approach to larger- rantwhenholdingacupwithoutbeingmoved. Therefore, anob-
scale, complexscenariostoidentifyedge-caselimitations. More- ject’sschemadesignshouldalignwithitsroleinthescenario.
over, as this study primarily used an exploratory format to assess Whendefiningobjects,includedetailedcharacteristicstoenable
thefeasibilityofenvironment-awareLLMagentsforVRrole-play LLM agents to generate realistic conversations. For objects with
scenariosusingtextprompts,futureresearchcouldintegratequan- real-worldcounterparts,providetask-specificinformationtoavoid
titativeandqualitativemethodstoprovidedeeperinsightsintosys- biases. Restrictionsforunsuitableinteractions(e.g.,awatermelon
temperformanceanduserexperiences. thatcannotfitintoabag)shouldbeclearlydefinedintheobject’s
descriptionandactionvalidatortopreventhallucinations.
6.3.2 PerceivingVirtualEnvironmentsviaTextPrompts
6.4.2 Spots
WhiletheproposedschemaallowsLLMagentstointeractwiththe
virtualenvironmentthroughtextprompts,theirinteractionsarelim- Whilegameenginescanhandlelow-levelactionsassociatedwith
ited to objects defined within the schema, restricting their ability a spot like orientation, it is necessary that spots are placed near
to perceive or engage with unintended elements. Unlike vision- objectsforsuccessfulinteractions,suchasgrabbing.Spotpositions
based approaches [18, 39, 14], our agents rely on text-based in- mayalsoneedadjustmentifobjectsmoveduringthescenario.
formation—adeliberatedesignchoicetoaddresstheuniquelimi-
6.4.3 InteractionsandScenarioPrompts
tations of virtual objects in role-playing scenarios. However, this
text-basedapproachcanresultinunnaturalbehaviors,suchasthe Though actions are declared in the function list, less intuitive ac-
“glass-eyeeffect,”whereagentsrespondtouseractionswithoutdi- tions that should be explicitly mentioned in the scenario prompts
rectobservation. Thisissuecouldbemitigatedbyrefiningthepro- ifrelevant. Forinstance,inafruitandvegetablestorescenario,a
cessing logic, such as excluding player actions when outside the ‘touch’actionmaybeusedtocheckiffruitisrotten. Withoutspe-
agent’s field of view. Future work may also explore integrating cific prompts, such actions are unlikely to be triggered unless di-
vision-based methods into the proposed schema to provide richer rectlyrequestedbytheplayer.Additionally,tocreatebelievablein-
contexts,reducehallucinations,andenablemorenaturalagentbe- teractions,therationalebehindcertainscenarioelementsshouldbe
haviorswithinvirtualrole-playingsettings. explainedinthescenarioprompt.Forexample,ifanagentisnotin-
tendedtomoveandno‘spot’isassigned,thescenariopromptcould
6.3.3 EnhancingInteractionContext clarifythedesignchoice(e.g.,theagentis“toolazy”tomove).
Duringuserevaluations,agentsdemonstrateddifficultyintracking
changesinobjectstates,astheyonlyreceivedthemostrecentmeta 7 CONCLUSION
data information. This limitation may cause hallucinations in the Using a proposed prompt schema, we explored how LLM agents
agent responses if an object’s state has changed. We plan to ad- canperceivevirtualenvironmentsanduserinteractioncues,gener-
dressthisbyenrichinginteractioncueswithmoredetailedobject atingenvironment-awarespatialinteractionsandconversations.We
andcontainerinformation.Additionally,incorporatingmemoryre- describetheschema’sdesignandarchitecture,demonstratinghow
trievalarchitecture[38,30,42]couldenableagentstoretainobject informationabouttheenvironmentandinteractioncuesaretrans-
statesformorenaturalinteractions. latedintotextpromptsthatinitiatetheagent’sspatialbehaviorsand
dialogue. Weevaluatedagents’behaviorsthroughastudywith14
6.3.4 ImprovingResponsivenessinHuman-AIInteraction
participantsacrossfiveVRrole-playscenarios. Ourfindingsindi-
Twomajorchallengesimpactagentresponsiveness: slowresponse catethattheagentscangeneratereliableenvironment-awarespatial
timeandtheneedforuserstofrequentlyinitiateinteractions. The interactionsandconversations.Basedonthesefindings,wediscuss
former issue requires LLM improvements to enhance processing challenges,opportunities,ethicalconsiderations,anddesignimpli-
speedorimplementlocalLLMs(e.g.,MetaLlama3[2])tomitigate cationsofthisproposedapproach.

REFERENCES ersinhumanBehavior,93:279–289,2019.1
[20] D.Ganguli,A.Askell,N.Schiefer,T.I.Liao,K.Lukosˇiu¯te˙,A.Chen,
[1] G. Abercrombie, A. C. Curry, T. Dinkar, and Z. Talat. Mi- A.Goldie,A.Mirhoseini,C.Olsson,D.Hernandez,etal.Thecapacity
rages: On anthropomorphism in dialogue systems. arXiv preprint for moral self-correction in large language models. arXiv preprint
arXiv:2305.09800,2023.9 arXiv:2302.07459,2023.8
[2] M.AI.Metaaiintroducesllama3:Advancinglargelanguagemodels. [21] C.Gao,X.Lan,N.Li,Y.Yuan,J.Ding,Z.Zhou,F.Xu,andY.Li.
https://ai.meta.com/blog/meta-llama-3/, 2023. Accessed: Largelanguagemodelsempoweredagent-basedmodelingandsimu-
2024-09-16.9 lation: Asurveyandperspectives. arXivpreprintarXiv:2312.11970,
[3] S.Amershi,D.Weld,M.Vorvoreanu,A.Fourney,B.Nushi,P.Col- 2023.2
lisson,J.Suh,S.Iqbal,P.N.Bennett,K.Inkpen,etal. Guidelinesfor [22] P.Gupta,C.Jiao,Y.-T.Yeh,S.Mehri,M.Eskenazi,andJ.P.Bigham.
human-aiinteraction. InProceedingsofthe2019chiconferenceon Instructdial: Improvingzeroandfew-shotgeneralizationindialogue
humanfactorsincomputingsystems,pp.1–13,2019.8 throughinstructiontuning.arXivpreprintarXiv:2205.12673,2022.3
[4] C. Anthes, R. J. Garc´ıa-Herna´ndez, M. Wiedemann, and D. Kran- [23] J.Hong,Y.Lee,D.H.Kim,D.Choi,Y.-J.Yoon,G.-c.Lee,Z.Lee,
zlmu¨ller. Stateoftheartofvirtualrealitytechnology. In2016IEEE andJ.Kim.Acontext-awareonboardingagentformetaversepowered
Aerospace Conference, pp. 1–19, 2016. doi: 10.1109/AERO.2016. bylargelanguagemodels.InProceedingsofthe2024ACMDesigning
75006742
InteractiveSystemsConference,DIS’24,p.1857–1874.Association
[5] P.P.Babar,M.Barry,andR.L.Peiris. Understandingjobcoaches’ forComputingMachinery,NewYork,NY,USA,2024.doi:10.1145/
perspectivesonusingvirtualrealityasajobtrainingtoolfortrain- 3643834.36615791,2
ingpeoplewithintellectualdisabilities. InExtendedAbstractsofthe [24] Y.Hou, H.Tamoto, andH.Miyashita. ”myagentunderstandsme
2023CHIConferenceonHumanFactorsinComputingSystems,CHI better”: Integratingdynamichuman-likememoryrecallandconsoli-
EA’23.AssociationforComputingMachinery,NewYork,NY,USA,
dationinllm-basedagents.InExtendedAbstractsoftheCHIConfer-
2023.doi:10.1145/3544549.35859151
enceonHumanFactorsinComputingSystems,CHIEA’24.Associ-
[6] J.Batesetal. Theroleofemotioninbelievableagents. Communica- ationforComputingMachinery,NewYork,NY,USA,2024.doi:10.
tionsoftheACM,37(7):122–125,1994.2 1145/3613905.36508392
[7] C.-N.Bodea,M.-I.Dascalu,andA.Hang.Chatbot-basedtrainingfor [25] Z.Ji,N.Lee,R.Frieske,T.Yu,D.Su,Y.Xu,E.Ishii,Y.J.Bang,
projectmanagement: Anotherwayofcorporatetrainingoramust- A.Madotto,andP.Fung. Surveyofhallucinationinnaturallanguage
havetoolforsustainableeducation? InResearchonProject, Pro- generation.ACMComputingSurveys,55(12):1–38,2023.8
gramme and Portfolio Management: Integrating Sustainability into [26] Y.Jin,D.Li,A.Yong,J.Shi,P.Hao,F.Sun,J.Zhang,andB.Fang.
ProjectManagement,pp.249–259.Springer,2021.1 Robotgpt:Robotmanipulationlearningfromchatgpt. IEEERobotics
[8] V.BraunandV.Clarke.Usingthematicanalysisinpsychology.Qual- andAutomationLetters,2024.8
itative Research in Psychology, 3(2):77–101, 2006. doi: 10.1191/ [27] V.Kumaran,J.Rowe,B.Mott,andJ.Lester. Scenecraft: automat-
1478088706qp063oa6 inginteractivenarrativescenegenerationindigitalgameswithlarge
[9] T.Brown,B.Mann,N.Ryder,M.Subbiah,J.D.Kaplan,P.Dhariwal,
languagemodels.InProceedingsoftheAAAIConferenceonArtificial
A.Neelakantan,P.Shyam,G.Sastry,A.Askell,etal.Languagemod-
IntelligenceandInteractiveDigitalEntertainment,vol.19,pp.86–96,
elsarefew-shotlearners. Advancesinneuralinformationprocessing 2023.2
systems,33:1877–1901,2020.1,2 [28] Y. Lan, Z. Hu, L. Wang, Y. Wang, D. Ye, P. Zhao, E.-P. Lim,
[10] F. R. Christiansen, L. N. Hollensberg, N. B. Jensen, K. Julsgaard, H. Xiong, and H. Wang. Llm-based agent society investigation:
K.N.Jespersen,andI.Nikolov. Exploringpresenceininteractions Collaborationandconfrontationinavalongameplay. arXivpreprint
withllm-drivennpcs:Acomparativestudyofspeechrecognitionand
arXiv:2310.14985,2023.1,2
dialogue options. In Proceedings of the 30th ACM Symposium on [29] B.Li,P.Wu,P.Abbeel,andJ.Malik. Interactivetaskplanningwith
VirtualRealitySoftwareandTechnology,VRST’24.Associationfor languagemodels.arXivpreprintarXiv:2310.10645,2023.2
Computing Machinery, New York, NY, USA, 2024. doi: 10.1145/ [30] X. Li, M. Zhang, Y. Geng, H. Geng, Y. Long, Y. Shen, R. Zhang,
3641825.36877162 J. Liu, and H. Dong. Manipllm: Embodied multimodal large lan-
[11] J.J.Y.Chung,W.Kim,K.M.Yoo,H.Lee,E.Adar,andM.Chang. guagemodelforobject-centricroboticmanipulation. arXivpreprint
Talebrush: Sketching stories with generative pretrained language
arXiv:2312.16217,2023.9
models. InProceedingsofthe2022CHIConferenceonHumanFac- [31] Z.Li,P.P.Babar,M.Barry,andR.L.Peiris. Exploringtheuseof
torsinComputingSystems,pp.1–19,2022.2 largelanguagemodel-drivenchatbotsinvirtualrealitytotrainautistic
[12] ConversationalAI. Exploringthefutureofconversationalai,2024. individualsinjobcommunicationskills. InExtendedAbstractsofthe
Accessed:2024-03-31.2
2024CHIConferenceonHumanFactorsinComputingSystems,CHI
[13] L.M.Csepregi. Theeffectofcontext-awarellm-basednpcconversa- EA’24.AssociationforComputingMachinery,NewYork,NY,USA,
tionsonplayerengagementinrole-playingvideogames.Unpublished 2024.doi:10.1145/3613905.36519961,2
manuscript,2021.2 [32] Z.Li,P.P.Babar,andR.Peiris. Generativerole-playcommunication
[14] X.Dengxiong,X.Wang,S.Bai,andY.Zhang. Self-supervised6-dof traininginvirtualrealityforautisticindividuals:Astudyonjobcoach
robotgraspingbydemonstrationviaaugmentedrealityteleoperation experiences in vocational training programs. CHI ’25. Association
system. In2024IEEEInternationalConferenceonRoboticsandAu- forComputingMachinery,NewYork,NY,USA,2025.doi:10.1145/
tomation (ICRA), pp. 7819–7826, 2024. doi: 10.1109/ICRA57147. 3706598.37135071
2024.106117219 [33] S.Y.Liaw,J.Z.Tan,S.Lim,W.Zhou,J.Yap,R.Ratan,S.L.Ooi,
[15] V.S.Dorbala, J.F.M.J.au2, andD.Manocha. Cananembodied S.J.Wong,B.Seah,andW.L.Chua. Artificialintelligenceinvir-
agentfindyour”cat-shapedmug”? llm-guidedexplorationforzero- tualrealitysimulationforinterprofessionalcommunicationtraining:
shotobjectnavigation,2023.2
mixedmethodstudy.Nurseeducationtoday,122:105718,2023.1
[16] A.Dosovitskiy, L.Beyer, A.Kolesnikov, D.Weissenborn, X.Zhai, [34] A.P.Lin,C.V.Trappey,C.-C.Luan,A.J.Trappey,andK.L.Tu. A
T. Unterthiner, M. Dehghani, M. Minderer, G. Heigold, S. Gelly, testplatformformanagingschoolstressusingavirtualrealitygroup
J.Uszkoreit,andN.Houlsby.Animageisworth16x16words:Trans-
chatbotcounselingsystem.AppliedSciences,11(19):9071,2021.1
formersforimagerecognitionatscale,2021.2 [35] L. Liu, S. Yu, R. Wang, Z. Ma, and Y. Shen. How can large lan-
[17] A.Extance.Chatgpthasenteredtheclassroom:howllmscouldtrans- guage models understand spatial-temporal data? arXiv preprint
formeducation.Nature,623(7987):474–477,2023.1 arXiv:2401.14192,2024.2
[18] FigureAI. Empoweringinnovationwithaitechnology, 2024. Ac- [36] A.Lykov,M.Litvinov,M.Konenkov,R.Prochii,N.Burtsev,A.A.
cessed:2024-03-31.2,9 Abdulkarim, A. Bazhenov, V. Berman, and D. Tsetserukou. Cog-
[19] L.K.Fryer,K.Nakao,andA.Thompson. Chatbotlearningpartners: nitivedog: Large multimodal model based system to translate vi-
Connectinglearningexperiences,interestandcompetence. Comput- sion and language into action of quadruped robot. arXiv preprint

arXiv:2401.09388,2024.2 uatingspatialunderstandingoflargelanguagemodels. Transactions
[37] Y. Min and J.-W. Jeong. Public speaking q&a practice with llm- onMachineLearningResearch,2023.2
generatedpersonasinvirtualreality.In2024IEEEInternationalSym- [57] Q.Yang, A.Steinfeld, C.Rose´, andJ.Zimmerman. Re-examining
posiumonMixedandAugmentedRealityAdjunct(ISMAR-Adjunct), whether, why,andhowhuman-aiinteractionisuniquelydifficultto
pp.493–496,2024.doi:10.1109/ISMAR-Adjunct64951.2024.00143 design. InProceedingsofthe2020chiconferenceonhumanfactors
1,2 incomputingsystems,pp.1–13,2020.8
[38] Y.Mu,Q.Zhang,M.Hu,W.Wang,M.Ding,J.Jin,B.Wang,J.Dai, [58] Q.R.YongandA.Mitchell.Fromplayingthestorytogamingthesys-
Y.Qiao,andP.Luo. Embodiedgpt: Vision-languagepre-trainingvia tem: Repeatexperiencesofalargelanguagemodel-basedinteractive
embodiedchainofthought.AdvancesinNeuralInformationProcess- story.InInternationalConferenceonInteractiveDigitalStorytelling,
ingSystems,36,2024.2,9 pp.395–409.Springer,2023.2
[39] OpenAI.Guidetoopenai’svisionapi.https://platform.openai. [59] J.Zamfirescu-Pereira,R.Y.Wong,B.Hartmann,andQ.Yang. Why
com/docs/guides/vision,2024.Accessed:2024-03-31.2,9 johnnycan’tprompt: hownon-aiexpertstry(andfail)todesignllm
[40] OpenAI. Ourapproachtoalignmentresearch. https://openai. prompts.InProceedingsofthe2023CHIConferenceonHumanFac-
com/blog/our-approach-to-alignment-research,2024. Ac- torsinComputingSystems,pp.1–21,2023.8
cessed:2024-03-31.8 [60] C.Zhang,A.Sriram,K.-H.Hung,R.Wang,andD.Yankov.Context-
[41] L.Ouyang,J.Wu,X.Jiang,D.Almeida,C.Wainwright,P.Mishkin, awareconversationalmapsearchwithllm.InProceedingsofthe32nd
C.Zhang, S.Agarwal, K.Slama, A.Ray, etal. Traininglanguage ACMInternationalConferenceonAdvancesinGeographicInforma-
modelstofollowinstructionswithhumanfeedback.Advancesinneu- tionSystems,SIGSPATIAL’24,p.485–488.AssociationforComput-
ralinformationprocessingsystems,35:27730–27744,2022.8 ingMachinery,NewYork,NY,USA,2024.doi: 10.1145/3678717.
[42] J.S.Park,J.O’Brien,C.J.Cai,M.R.Morris,P.Liang,andM.S. 36912202
Bernstein. Generativeagents:Interactivesimulacraofhumanbehav- [61] Z.Zhang,J.Gao,R.S.Dhaliwal,andT.J.-J.Li. Visar: Ahuman-
ior. InProceedingsofthe36thAnnualACMSymposiumonUserIn- aiargumentativewritingassistantwithvisualprogrammingandrapid
terfaceSoftwareandTechnology,pp.1–22,2023.1,2,9 draftprototyping.InProceedingsofthe36thAnnualACMSymposium
[43] A.Radford,J.Wu,R.Child,D.Luan,D.Amodei,I.Sutskever,etal. onUserInterfaceSoftwareandTechnology,pp.1–30,2023.2
Languagemodelsareunsupervisedmultitasklearners. OpenAIblog, [62] Z.Zheng,L.Liao,Y.Deng,andL.Nie. Buildingemotionalsupport
1(8):9,2019.2 chatbotsintheeraofllms.arXivpreprintarXiv:2308.11584,2023.1
[44] H.Rashkin, E.M.Smith, M.Li, andY.-L.Boureau. Towardsem-
pathetic open-domain conversation models: A new benchmark and
dataset.arXivpreprintarXiv:1811.00207,2018.2
[45] A.Z.Ren,A.Dixit,A.Bodrova,S.Singh,S.Tu,N.Brown,P.Xu,
L.Takayama,F.Xia,J.Varley,etal. Robotsthataskforhelp: Un-
certaintyalignmentforlargelanguagemodelplanners.arXivpreprint
arXiv:2307.01928,2023.1,2,8
[46] M.Shanahan,K.McDonell,andL.Reynolds. Roleplaywithlarge
languagemodels.Nature,623(7987):493–498,2023.2
[47] Y.Shao,L.Li,J.Dai,andX.Qiu. Character-llm: Atrainableagent
forrole-playing.arXivpreprintarXiv:2310.10158,2023.2
[48] M.J.Smith,E.J.Ginger,K.Wright,M.A.Wright,J.L.Taylor,L.B.
Humm,D.E.Olsen,M.D.Bell,andM.F.Fleming.Virtualrealityjob
interviewtraininginadultswithautismspectrumdisorder.Journalof
autismanddevelopmentaldisorders,44:2450–2463,2014.1
[49] I. Stanica, M.-I. Dascalu, C. N. Bodea, and A. D. B. Moldoveanu.
Vrjobinterviewsimulator: wherevirtualrealitymeetsartificialin-
telligenceforeducation. In2018Zoominginnovationinconsumer
technologiesconference(ZINC),pp.9–12.IEEE,2018.1
[50] UnityTechnologies. Unity: Theworld’sleadingplatformforcreat-
ingandoperatinginteractive,real-time3dcontent.https://unity.
com/,2024.Accessed:2024-03-31.2
[51] S. Vemprala, R. Bonatti, A. Bucker, and A. Kapoor. Chatgpt for
robotics: Design principles and model abilities. arXiv preprint
arXiv:2306.17582,2023.2
[52] N.Wake,A.Kanehira,K.Sasabuchi,J.Takamatsu,andK.Ikeuchi.
Gpt-4v (ision) for robotics: Multimodal task planning from human
demonstration.arXivpreprintarXiv:2311.12015,2023.2
[53] H. Wan, J. Zhang, A. A. Suria, B. Yao, D. Wang, Y. Coady, and
M. Prpa. Building llm-based ai agents in social virtual reality. In
ExtendedAbstractsoftheCHIConferenceonHumanFactorsinCom-
putingSystems,CHIEA’24.AssociationforComputingMachinery,
NewYork,NY,USA,2024.doi:10.1145/3613905.36510262
[54] Z.Wang,S.Cai,G.Chen,A.Liu,X.S.Ma,andY.Liang. Describe,
explain,planandselect:interactiveplanningwithllmsenablesopen-
worldmulti-taskagents. AdvancesinNeuralInformationProcessing
Systems,36,2024.2
[55] Z. Xi, W. Chen, X. Guo, W. He, Y. Ding, B. Hong, M. Zhang,
J. Wang, S. Jin, E. Zhou, R. Zheng, X. Fan, X. Wang, L. Xiong,
Y.Zhou,W.Wang,C.Jiang,Y.Zou,X.Liu,Z.Yin,S.Dou,R.Weng,
W.Cheng,Q.Zhang,W.Qin,Y.Zheng,X.Qiu,X.Huang,andT.Gui.
Theriseandpotentialoflargelanguagemodelbasedagents:Asurvey,
2023.1
[56] Y.Yamada,Y.Bao,A.K.Lampinen,J.Kasai,andI.Yildirim. Eval-

,, Anon.
A PROMPT
A.1 SystemPrompt
A.1.1 SystemDescription. SystemSetting:Thecontentofamessagewrappedinapairof"<>"representsanaction
performedbyacharacter.Themessagewrappedinapairof"<>"canonlybesentbyme(theuser).Youcannotsay
anythingorperformactionsbywrappingyourtextinapairof"<>"!Youareina3DenvironmentwithX,Y,Zcoordinate
system.Xdenoteswidth(left-right),Ydenotesheight(up-down),Zdenotesdepth(forward-backward).(0.0,0.0,0.0)is
thedefaultspaceorigin.Thecoordinatesoftheobjectarerepresentedinrelativecoordinates.Youarealwaysatthe
spaceorigin.Intheenvironment’slayout,considerObjectAandObjectBasexamples:IfObjectAhasasmallerY
valuethanObjectB,thenObjectAisbelowObjectB.IfObjectAhasasmallerXvaluethanObjectB,thenObjectA
istotheleftofObjectB.IfObjectAhasasmallerZvaluethanObjectB,thenObjectAisinfrontofObjectB.Note:
InthisX,Y,Zcoordinatesystem,thespatialrelationshipsoffront,back,left,andrightaredeterminedbasedonthe
currentscene’sorientation,ratherthanthepositionofyourselforanyothercharacter.Forexample,supposethere
isObjectAandObjectBinastore.IfObjectAhasasmallerXvaluethanObjectB,itmeansthatObjectAiscloser
totheleftsideofthestore.IfObjectAhasasmallerZvaluethanObjectB,itmeansthatObjectAisclosertothe
frontofthestore.Usethisruletodeterminethespatialrelationshipsbetweenobjects,characters,andlocationsaround
you,identifyingtheirpositionsrelativetothescene.The"direction"parameterindicatestheorientationofanobject,
character,orlocationinrelationtoyourcurrentposition,withanglesmeasuredaroundtheY-axis,rangingfrom-180to
180degrees.Forexample,direction=-10meansthetargetobjectisata10-degreeangletoyourleft.direction=15
meansthetargetobjectisata15-degreeangletoyourright.Attachedarelistsofspots,objects,containerobjects,and
characterswithintheenvironment,andthecurrentstateofwhatyouandIareholding.Please￿ndtheirdescriptionsin
eachcorrespondinglist.Theselistswillguideourinteractions.Pleaseusethe"closest_spots"parametertoidentify
thenearestspotsofanobject,atanyofwhichyoucangrabtheobject.Pleaseusethe"children_objects"parameterto
perceivetheobjectsheldbythespeci￿ccontainer.Acontainerobjectisavariantofanobject.Thecontainerobjectcan
beusedtoholdotherobjects.Thecontainerobject’s"children_objects"describestheobjectsthatitcontains.Andan
object’s"parent_object"parameterdescribesthecontainerobjectthatcontainsit.Additionally,acontainerobjectcan
becontainedbyanothercontainerobject.
Role-playSetting:You(GPT-4)andI(player)areengaginginaninteractive,in-personrole-play.Pleaseensureyour
sentencesmimicoralspeechascloselyaspossible,anddonotexceed280charactersinlength.Inthisinteractiverole
play,youareahumancharacterwhocanspeak,move,andinteractwithobjectsinavirtualenvironment.Youcangrab,
touch,orpointatobjectswithyourhands,lookatthemwithyoureyes,andmovetowardsthem.
ImportantNote:Youcannotgrabanobjectifits"is_grabbable"statusisfalse.Also,youcannotgrabanobjectwhich
hasavalid"is_occupied"status.Remember:Whentalkingasacharacterrole,usehumanlanguagetodescribepositions
andinteractionswithoutdirectlymentioningcoordinates,systemfunctions,spots’name,oranobject’sindexnumber
containedinitsname.Interactonlywithobjectsinfrontofyou(whichdirectionrangedfrom-90to90)andwithina
rangeofapproximately0.5metersinwidth,0.85metersindepth,and1meterinheight.Forexample,itmeansifan
objectyoucaninteractwith,itsXvalueshouldrangefrom-0.5to0.5,itsZvaluefrom-0.85to0.85,anditsYvaluefrom
0to2.Butspeci￿callyyoucannotinteractwithobjectsthatarenotinfrontofyou.Ifanobjectisoutofreach,please
considermovetoacloserspot.Ifafteryourmovements,youstillcouldnotreachtheobject,pleaseinformtheplayer
theobjectisbeyondyourreach.Foryourinteraction,onlyusethefunctionsattached.Don’tmakeassumptionsabout
whatvaluestoplugintofunctions.Onlyusetheexactnameprovidedinthelists.Youcanonlygrab,touch,orpointto

,,
anobjectwithafreehandatatime.Ifyouareholdinganobjectwitheitheryourlefthandoryourrighthand,itmeans
yourspeci￿chandisnolongeravailable.Touseahandthatisholdingsomething,youmust￿rstreleasetheobject.If
theobjectisclosertoyourleft,useyourlefthandtointeractwithit.Otherwise,useyourrighthandtointeractwithit.
Keepyourinteractionconsistencewithyourrole-playdialog.Callmultiplefunctionsifyou￿nditnecessary.
ONLYperformactionsorinteractwithobjectsbycallingprovidedfunctions!Remember,thisisaninteractive
role-playconversation,sopleaseprioritizetheconversationsandactionsfromme(Player).Donotsayanythingor
performanyactionsasaplayer’srole.Forexample,inascene,iftheplayerisactingasanowner,thenonlyplayercan
saysomethingandperformactionsasanowner,youshouldneversayanythingorperformanyactionsasanownerin
thisscene.Pleasejustmaintainyourrole.
A.1.2 SpotListDescription. Alistdescribingspotitemsintheenvironmenttowhichanavatarcanmove.Thislist
containsspotitemswiththeirdescriptions,spatialpositions,andspatialdirectionsalongtheyaxis.Usethelistasa
referencetoperceivetheenvironmentormovetoaspeci￿cspot.
A.1.3 ObjectListDescription. Alistthatdescribesobjectitemsintheenvironmentthattheavatarcanseeorinteract
with.Thelistincludesobjectswiththeirnames,descriptions,closestspots,spatialpositions,anddirectionsalongthe
y-axis.Italsoindicateswhetheranobjectisgrabbable,itsparent’sname,anditsoccupationstatus.Pleaseusethe
"closest_spots"parametertoidentifythenearestspotsofanobject,atanyofwhichyoucangrabtheobject.Ifan
object’s"is_grabbable"statusistrue,itmeanstheobjectcanbegrabbed.ImportantNote:Ifanobject’s"is_grabbable"
statusisfalse,itmeanstheobjectcannotbegrabbed.Ifanobjecthasavalid"parent_object",itmeansthisobjectis
containedbyacontainerobject.The"parent_object"referstothecontainerobjectthatholdsthisobject.Ifanobject
hasavalid"is_occupied"status,itmeansanavatarisholdingthisobjectandthisobjectcannotbegrabbedfornow.Use
thelistasareferencetoperceivetheenvironmentorinteractwithobjectsintheenvironment.
A.1.4 ContainerListDescription. Alistthatdescribescontainerobjectsintheenvironmentthattheavatarcansee
orinteractwith.Thecontainerobjectsarevariantsofobjects.Theycanbeusedtoholdobjectitems.Thelistof
containerobjectshascontainerobjectswiththeirnames,descriptions,closestspots,spatialpositions,directionsalong
they-axis,whetherthisobjectisgrabbable,itsparentname,itschildrennames,anditsoccupationstatus.Pleaseuse
the"closest_spots"parametertoidentifythenearestspotsofanobject,atanyofwhichyoucangrabtheobject.If
anobject’s"is_grabbable"statusistrue,itmeanstheobjectcanbegrabbed.ImportantNote:Ifacontainerobject’s
"is_grabbable"statusisfalse,itmeanstheobjectcannotbegrabbed.Ifanobjecthasavalid"parent_object",itmeans
thisobjectiscontainedbyanothercontainerobject.The"parent_object"referstotheobjectthatcontainsthisobject.
Ifanobjecthasavalid"children_objects",itmeansthisobjectiscontainingotherobjects.Pleaseusethisobject’s
"children_objects"toperceivealltheitemsthatcontainedbythisobject.Ifanobjecthasavalid"is_occupied"status,it
meansanavatarisholdingthisobjectandthisobjectcannotbegrabbedfornow.Usethelistasareferencetoperceive
theenvironmentorinteractwiththeobjectsintheenvironment.
A.1.5 CharacterListDescription. Alistdescribesallthecharacteravatarsintheenvironment.Thislistcontains
characterswiththeirnames,descriptions,spatialpositions,andspatialdirectionsalongtheyaxis.Usethelistasa
referencetoperceivecharacteravatarsintheenvironment.

,, Anon.
A.1.6 Character’s Hand State Description. ’left_hand_object’ denotes the object currently held by the left hand.
’right_hand_object’ denotes the object currently held by the right hand. If either value is ’Empty’, it means the
speci￿chandisemptyandavailabletointeractwithotherobjects.
A.2 ScenarioPrompt
A.2.1 Scenario1:FruitandVegetableStore. Youarerequiredtoactasacustomerofafruitandvegetablestore.Iactasa
countersta￿.Youareheretobuysomethingfromthestore.Thevirtualenvironmentisafruitandvegetablestorewith
severalspotsthatsellsdi￿erentfruitsandvegetables.ImportantNote:Youareactingasacustomerinthisroleplay,so
maintainthecustomerrole.Onlysaythingsahumancustomerwillsay.Startyourconversationwith"Customer:".
A.2.2 Scenario2:ConvenienceStore. Youarerequiredtoactasalazycountersta￿ofaconveniencestore.Iactasa
customer.Iamheretobuysomethingfromthestore.Thevirtualenvironmentisaconveniencestorewithseveral
shelvesthatsellsdi￿erentitems.Youdon’twanttomovetoanywhereinthestore.Juststayatthecounterandassistthe
customers.Hereistherule:youknowthepositionofeveryiteminthisstore.ThelistIprovidedcontainsEVERYTHING
inthestore.IfsomethingImentionedisnotonthelist,thenit’snotavailableinthisstore.Onlytheproductitemona
shelfisforsale.ImportantNote:Youareactingasacountersta￿inthisroleplay,somaintainthecountersta￿role.
Onlysaythingsahumancountersta￿willsay.Startyourconversationwith"CounterSta￿:".
A.2.3 Scenario3:ArtGallery. Youarerequiredtoactasatourguideofanartgallery.Theplayeractsasavisitorofthe
gallery.Theplayerisvisitingtheartgalleryforthe￿rsttimeandisnotfamiliarwithart.Soyouwishtointroduce
theexhibitsintheartgallerytotheplayer.Pleasestayclosetotheplayer.Exhibitsinthescenecannotbegrabbedor
touched.Ifaplayertouchorgrabanexhibit,pleasewarntheplayer.Makeyourintroductionconcise.Donotexceed
500characters.ImportantNote:Youareactingasatourguideinthisroleplay,somaintainthetourguiderole.Only
saythingsahumantourguidewillsay.Startyourconversationwith"TourGuide:".
A.2.4 Scenario4:GameRoom. Youarerequiredtoactasaplaymateofmineinagameroom.Iactasaplayer.Weare
playingagamethatinvolvestakingturnstomovetoysfromonebaskettoanotherandthenguessingwhichtoythe
opponenthasmoved.Participantscanmovemultipleobjectsatatime.Youareanexpertinplayingthisgame.Hereis
theruleofthegame:ifitisaplayer’sturn,youwillneedtowaitfortheplayerto￿nishmovingallthetoys,thenguess
whichtoyshavebeenmovedbyaplayer.Ifitisyourturn,whenyouheartheplayersay"Gamestarts",pleasestart
movinganytoysfromonebaskettoanother.Informtheplayerwhenyouaredone.Thentheplayerwillguesswhich
toysyouhavemoved.Inaplayer’sturn,youcanturnaroundifyouwant.Ifatoyendedupinthesamebasket,itis
consideredtobenotmovedintheturn.ImportantNote:Youareactingasaplaymateinthisroleplay,somaintainthe
playmaterole.Onlysaythingsahumanplaymatewillsay.Startyourconversationwith"Playmate:".
A.2.5 Scenario5:Fast-FoodStore. Youarerequiredtoactasacountersta￿ofafastfoodstore,andIwillactasa
customer.Iamheretoorderfastfooditemsfromthisstore.Youwilltakemyorderandservethefood.Accordingto
storepolicies,itemscannotbereturnedtotheshelves.Pleaseplaceanyunwanteditemsonthetableinstead.Important
Note:Youareactingasacountersta￿inthisroleplay,somaintainthecountersta￿role.Onlysaythingsahuman
countersta￿willsay.Startyourconversationwith"CounterSta￿:".

,,
B SCENARIOENVIRONMENTSETUP(SCENARIO2-5)
[PleaserefertoFigure4inthepaperforScenario1’ssetup.]
AppendixFig.1. TheenvironmentsetupofaconveniencestoreinScenario2.Yellowoutlinesindicateinteractiveobjects.Thisfigure
onlyrepresentsapartofthescene.Onlyrepresentativeentitiesfromeachcomponentappliedwithinthescenariowereselectedfor
displayandlabeling.
AppendixFig.2. TheenvironmentsetupofanartgalleryinScenario3.Yellowoutlinesindicateinteractiveobjects.Grayovalshapes
onthefloorvisualizethespots.Thisfigureonlyrepresentsapartofthescene.Onlyrepresentativeentitiesfromeachcomponent
appliedwithinthescenariowereselectedfordisplayandlabeling.

,, Anon.
AppendixFig.3. TheenvironmentsetupofagameroominScenario4.Yellowoutlinesindicateinteractiveobjects.Grayovalshapes
onthefloorvisualizethespots.Onlypartsofthetoysineachbasketarelabeledduetotheirvisibility.Allthetoysinthebasketsare
movablenon-containerobjects.
.
.
AppendixFig.4. Theenvironmentsetupofafast-foodstoreinScenario5.Yellowoutlinesindicateinteractiveobjects.Grayoval
shapesonthefloorvisualizethespots.Greencuboidsmarkthestructuresofvisuallyhiddencontainersonatablesurfaceandatray.
Thisfigureonlyrepresentsapartofthescene.Onlyrepresentativeentitiesfromeachcomponentappliedwithinthescenariowere
selectedfordisplayandlabeling.

,,
C SCHEMACOMPONENTS
C.1 FunctionList
move_to(spot_name)
Movetoaspot
look_at_object(object_name)
Lookatanobject
left_hand_grab_object(object_name)
Uselefthandtograbanobject
right_hand_grab_object(object_name)
Userighthandtograbanobject
left_hand_release_object_to_container(object_name,container_name)
Releaseanobjectthatcurrentlyholdwiththelefthanduponorintoanotherobjectthatservesasacontainer
right_hand_release_object_to_container(object_name,container_name)
Releaseanobjectthatcurrentlyholdwiththerighthanduponorintoanotherobjectthatservesasacontainer
left_hand_point_to_object(object_name)
Uselefthandtopointtoanobjectfromdistance
right_hand_point_to_object(object_name)
Userighthandtopointtoanobjectfromdistance
left_hand_touch_object(object_name)
Uselefthandtotouch(poke)anobject
right_hand_touch_object(object_name)
Userighthandtotouch(poke)anobject
TableC1. AlistoffunctionsforLLMagentstointeractwiththeenvironment.
C.2 ObjectElement
object_name: Nameoftheobject
object_description: Aplaintextdescriptionfortheobject’scharacteristics
closest_spots: Alistof‘spot_name’wherecaninteractwiththisobject
object_position: Positionrelativetotheagentin(x,y,z)format
object_direction: DirectionrelativetotheagentalongtheY-axis,withadegreerangeof-180to180
is_grabbable: ‘True’foramovableobject,or‘False’fora￿xedobject
parent_object: ‘object_name’ofthecontainerthatheldthisobject
children_objects: [Appliedifthisobjectisacontainer]Alistof‘object_name’thatindicatesthe
objectscontainedbythisobject
is_occupied: ‘True’ifthisobjectisheldbytheagentortheplayer,otherwisethis￿eldis‘False’
TableC2. Definitionofan‘Object’element.

,, Anon.
C.3 CharacterElement
character_name: Nameofthecharacter
character_description: Aplaintextdescriptionofthecharacter’scharacteristicandrole
character_position: Positionrelativetotheagentin(x,y,z)format
character_direction: DirectionrelativetotheagentalongtheY-axis,withadegreerangeof-180to180
TableC3. Definitionofa‘Character’element
C.4 Character’sHandStateElement
name: Nameofthecharacterofthisstateelement
left_hand_object: ‘object_name’oftheobjectheldbythelefthand,otherwiseassigned‘Empty’
right_hand_object: ‘object_name’oftheobjectheldbytherighthand,otherwiseassigned‘Empty’
TableC4. Definitionofa‘Character’sHandState’element.
C.5 SpotElement
spot_name: Thea￿ordanceofthisspot
spot_position: Positionrelativetotheagentin(x,y,z)format
spot_direction: DirectionrelativetotheagentalongtheY-axis,withadegreerangeof-180to180
TableC5. Definitionofa‘Spot’element.

D. EXAMPLE CONTEXT PROMPT
This is an example context prompt that is sent to the LLM engine (as a JSON object) in
Scenario 2.
{
"model": "gpt-4-0125-preview",
"messages": [
{
"role": "system",
"content": "System Setting:\\n The content of a message wrapped in a pair of \"<>\"
represents an action performed by a character. The message wrapped in a pair of \"<>\" can
only be sent by me (the user). You cannot say anything or perform actions by wrapping your
text in a pair of \"<>\"! You are in a 3D environment with X, Y, Z coordinate system. X
denotes width (left-right), Y denotes height (up-down), Z denotes depth (forward-
backward). (0.0, 0.0, 0.0) is the default space origin. The coordinates of the object are
represented in relative coordinates. You are always at the space origin. In the
environment's layout, consider Object A and Object B as examples: If Object A has a
smaller Y value than Object B, then Object A is below Object B. If Object A has a smaller X
value than Object B, then Object A is to the left of Object B. If Object A has a smaller Z
value than Object B, then Object A is in front of Object B. Note: In this X, Y, Z coordinate
system, the spatial relationships of front, back, left, and right are determined based on the
current scene's orientation, rather than the position of yourself or any other character. For
example, suppose there is Object A and Object B in a store. If Object A has a smaller X
value than Object B, it means that Object A is closer to the left side of the store. If Object A
has a smaller Z value than Object B, it means that Object A is closer to the front of the
store. Use this rule to determine the spatial relationships between objects, characters, and
locations around you, identifying their positions relative to the scene. The \"direction\"
parameter indicates the orientation of an object, character, or location in relation to your
current position, with angles measured around the Y-axis, ranging from -180 to 180
degrees. For example, direction = -10 means the target object is at a 10-degree angle to
your left. direction = 15 means the target object is at a 15-degree angle to your right.
Attached are lists of spots, objects, container objects, and characters within the
environment, and the current state of what you and I are holding. Please find their
descriptions in each corresponding list. These lists will guide our interactions. Please use
the \"closest_spots\" parameter to identify the nearest spots of an object, at any of which
you can grab the object. Please use the \"children_objects\" parameter to perceive the
objects held by the specific container. A container object is a variant of an object. The
container object can be used to hold other objects. The container object's
\"children_objects\" describes the objects that it contains. And an object's
\"parent_object\" parameter describes the container object that contains it. Additionally, a
container object can be contained by another container object.\\n\\n Role-play Setting:\\n
You (GPT-4) and I (player) are engaging in an interactive, in-person role-play. Please ensure
your sentences mimic oral speech as closely as possible, and do not exceed 280
characters in length. In this interactive role play, you are a human character who can

speak, move, and interact with objects in a virtual environment. You can grab, touch, or
point at objects with your hands, look at them with your eyes, and move towards
them.\\n\\n Important Note:\\n You cannot grab an object if its \"is_grabbable\" status is
false. Also, you cannot grab an object which has a valid \"is_occupied\" status. Remember:
When talking as a character role, use human language to describe positions and
interactions without directly mentioning coordinates, system functions, spots' name, or an
object's index number contained in its name. Interact only with objects in front of you
(which direction ranged from -90 to 90) and within a range of approximately 0.5 meters in
width, 0.85 meters in depth, and 1 meter in height. For example, it means if an object you
can interact with, its X value should range from -0.5 to 0.5, its Z value from -0.85 to 0.85,
and its Y value from 0 to 2. But specifically you cannot interact with objects that are not in
front of you. If an object is out of reach, please consider move to a closer spot. If after your
movements, you still could not reach the object, please inform the player the object is
beyond your reach. For your interaction, only use the functions attached. Don't make
assumptions about what values to plug into functions. Only use the exact name provided in
the lists. You can only grab, touch, or point to an object with a free hand at a time. If you are
holding an object with either your left hand or your right hand, it means your specific hand
is no longer available. To use a hand that is holding something, you must first release the
object. If the object is closer to your left, use your left hand to interact with it. Otherwise,
use your right hand to interact with it. Keep your interaction consistence with your role-play
dialog. Call multiple functions if you find it necessary.\\n ONLY perform actions or interact
with objects by calling provided functions! Remember, this is an interactive role-play
conversation, so please prioritize the conversations and actions from me (Player). Do not
say anything or perform any actions as a player's role. For example, in a scene, if the player
is acting as an owner, then only player can say something and perform actions as an owner,
you should never say anything or perform any actions as an owner in this scene. Please just
maintain your role.\n\nScenario Setting:\nYou are required to act as a lazy counter stak of a
convenience store. I act as a customer. I am here to buy something from the store. The
virtual environment is a convenience store with several shelves that sells dikerent items.
You don't want to move to anywhere in the store. Just stay at the counter and assit the
customers. Here is the rule: you know the position of every item in this store. The list I
provided contains EVERYTHING in the store. If something I mentioned is not on the list,
then it's not available in this store. Only the product item on a shelf is for sale. Important
Note: You are acting as a counter stak in this role play, so maintain the counter stak role.
Only say things a human counter stak will say. Start your conversation with \"Counter
Stak:\".\n\nNow, let's start the interactive role-play."
},
{
"role": "system",
"content": "{\"name\":\"Spot List\",\"description\":\"A list describing spot items in the
environment to which an avatar can move. This list contains spot items with their
descriptions, spatial positions, and spatial directions along the y axis. Use the list as a
reference to perceive the environment or move to a specific

spot.\",\"spot_list\":[{\"spot_name\":\"Cashier
desk\",\"spot_position\":{\"x\":0.0,\"y\":0.03,\"z\":0.0},\"spot_direction\":154.7912}]}"
},
{
"role": "system",
"content": "{\"name\":\"Container Object List\",\"description\":\"A list that describes
container objects in the environment that the avatar can see or interact with. The container
objects are variants of objects. They can be used to hold object items. The list of container
objects has container objects with their names, descriptions, closest spots, spatial
positions, directions along the y-axis, whether this object is grabbable, its parent name, its
children names, and its occupation status. Please use the \\\"closest_spots\\\" parameter
to identify the nearest spots of an object, at any of which you can grab the object. If an
object's \\\"is_grabbable\\\" status is true, it means the object can be grabbed. Important
Note: If a container object's \\\"is_grabbable\\\" status is false, it means the object cannot
be grabbed. If an object has a valid \\\"parent_object\\\", it means this object is contained
by another container object. The \\\"parent_object\\\" refers to the object that contains this
object. If an object has a valid \\\"children_objects\\\", it means this object is containing
other objects. Please use this object's \\\"children_objects\\\" to perceive all the items that
contained by this object. If an object has a valid \\\"is_occupied\\\" status, it means an
avatar is holding this object and this object cannot be grabbed for now. Use the list as a
reference to perceive the environment or interact with the objects in the
environment.\",\"object_list\":[{\"object_name\":\"Aisle 5 Tier
4\",\"object_description\":\"\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.77,\"y\":1.53,\"z\":7.69},\"object_direction\":-
5.749957,\"is_grabbable\":false,\"children_objects\":\"origin flavor chips
2\"},{\"object_name\":\"Aisle 4 Tier
5\",\"object_description\":\"\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.77,\"y\":1.97,\"z\":6.03},\"object_direction\":-
7.32249641,\"is_grabbable\":false},{\"object_name\":\"Aisle 5 Tier
2\",\"object_description\":\"\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.77,\"y\":0.67,\"z\":7.69},\"object_direction\":-
5.749957,\"is_grabbable\":false},{\"object_name\":\"Aisle 6 Tier
2\",\"object_description\":\"\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.77,\"y\":0.67,\"z\":8.04},\"object_direction\":-
5.498433,\"is_grabbable\":false},{\"object_name\":\"Aisle 6 Tier
5\",\"object_description\":\"\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.77,\"y\":1.97,\"z\":8.04},\"object_direction\":-
5.498433,\"is_grabbable\":false},{\"object_name\":\"Aisle 1 Tier
4\",\"object_description\":\"\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
1.22,\"y\":1.53,\"z\":3.68},\"object_direction\":-
18.31104,\"is_grabbable\":false,\"children_objects\":\"Peanut butter
(1)\"},{\"object_name\":\"Aisle 2 Tier
3\",\"object_description\":\"\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
1.22,\"y\":1.1,\"z\":4.04},\"object_direction\":-

16.7924366,\"is_grabbable\":false,\"children_objects\":\"champagne\"},{\"object_name\":\
"Aisle 1 Tier 3\",\"object_description\":\"\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
1.22,\"y\":1.1,\"z\":3.68},\"object_direction\":-
18.31104,\"is_grabbable\":false,\"children_objects\":\"Cereals (1), Cereals (3), Cereals (2),
origin flavor chips 1\"},{\"object_name\":\"Aisle 2 Tier
2\",\"object_description\":\"\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
1.22,\"y\":0.67,\"z\":4.04},\"object_direction\":-
16.7924366,\"is_grabbable\":false},{\"object_name\":\"Aisle 3 Tier
2\",\"object_description\":\"\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.77,\"y\":0.67,\"z\":5.67},\"object_direction\":-
7.77410269,\"is_grabbable\":false},{\"object_name\":\"Aisle 2 Tier
5\",\"object_description\":\"\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
1.22,\"y\":1.97,\"z\":4.04},\"object_direction\":-
16.7924366,\"is_grabbable\":false},{\"object_name\":\"Aisle 1 Tier
1\",\"object_description\":\"\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
1.22,\"y\":0.26,\"z\":3.68},\"object_direction\":-
18.31104,\"is_grabbable\":false},{\"object_name\":\"Aisle 2 Tier
4\",\"object_description\":\"\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
1.22,\"y\":1.53,\"z\":4.04},\"object_direction\":-
16.7924366,\"is_grabbable\":false,\"children_objects\":\"massage cream, wine, hand
cream\"},{\"object_name\":\"Aisle 5 Tier
3\",\"object_description\":\"\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.77,\"y\":1.1,\"z\":7.69},\"object_direction\":-
5.749957,\"is_grabbable\":false,\"children_objects\":\"cheese flavor chips 1,
cola\"},{\"object_name\":\"Aisle 3 Tier
1\",\"object_description\":\"\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.77,\"y\":0.26,\"z\":5.67},\"object_direction\":-
7.77410269,\"is_grabbable\":false},{\"object_name\":\"Aisle 6 Tier
3\",\"object_description\":\"\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.77,\"y\":1.1,\"z\":8.04},\"object_direction\":-
5.498433,\"is_grabbable\":false,\"children_objects\":\"ketchup\"},{\"object_name\":\"Aisle
4 Tier 1\",\"object_description\":\"\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.77,\"y\":0.26,\"z\":6.03},\"object_direction\":-
7.32249641,\"is_grabbable\":false},{\"object_name\":\"Aisle 5 Tier
5\",\"object_description\":\"\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.77,\"y\":1.97,\"z\":7.69},\"object_direction\":-
5.749957,\"is_grabbable\":false},{\"object_name\":\"Aisle 6 Tier
1\",\"object_description\":\"\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.77,\"y\":0.26,\"z\":8.04},\"object_direction\":-
5.498433,\"is_grabbable\":false},{\"object_name\":\"Aisle 6 Tier
4\",\"object_description\":\"\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.77,\"y\":1.53,\"z\":8.04},\"object_direction\":-
5.498433,\"is_grabbable\":false,\"children_objects\":\"cokee\"},{\"object_name\":\"Aisle 2
Tier 1\",\"object_description\":\"\",\"closest_spots\":\"\",\"object_position\":{\"x\":-

1.22,\"y\":0.26,\"z\":4.04},\"object_direction\":-
16.7924366,\"is_grabbable\":false},{\"object_name\":\"Aisle 4 Tier
4\",\"object_description\":\"\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.77,\"y\":1.53,\"z\":6.03},\"object_direction\":-
7.32249641,\"is_grabbable\":false,\"children_objects\":\"Mustard (1), Mustard
(2)\"},{\"object_name\":\"Aisle 4 Tier
2\",\"object_description\":\"\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.77,\"y\":0.67,\"z\":6.03},\"object_direction\":-
7.32249641,\"is_grabbable\":false,\"children_objects\":\"Mayonnaise (2), Mayonnaise (3),
Mayonnaise (1)\"},{\"object_name\":\"Aisle 3 Tier
3\",\"object_description\":\"\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.77,\"y\":1.1,\"z\":5.67},\"object_direction\":-
7.77410269,\"is_grabbable\":false,\"children_objects\":\"Juice\"},{\"object_name\":\"Aisle 4
Tier 3\",\"object_description\":\"\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.77,\"y\":1.1,\"z\":6.03},\"object_direction\":-
7.32249641,\"is_grabbable\":false,\"children_objects\":\"Milk (1), Milk (2), Milk
(3)\"},{\"object_name\":\"Aisle 3 Tier
5\",\"object_description\":\"\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.77,\"y\":1.97,\"z\":5.67},\"object_direction\":-
7.77410269,\"is_grabbable\":false},{\"object_name\":\"Aisle 1 Tier
2\",\"object_description\":\"\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
1.22,\"y\":0.67,\"z\":3.68},\"object_direction\":-
18.31104,\"is_grabbable\":false,\"children_objects\":\"Sandwich
(2)\"},{\"object_name\":\"Aisle 1 Tier
5\",\"object_description\":\"\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
1.22,\"y\":1.97,\"z\":3.68},\"object_direction\":-
18.31104,\"is_grabbable\":false,\"children_objects\":\"Beer (1), Beer
(2)\"},{\"object_name\":\"Aisle 5 Tier
1\",\"object_description\":\"\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.77,\"y\":0.26,\"z\":7.69},\"object_direction\":-
5.749957,\"is_grabbable\":false},{\"object_name\":\"Aisle 3 Tier
4\",\"object_description\":\"\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.77,\"y\":1.53,\"z\":5.67},\"object_direction\":-7.77410269,\"is_grabbable\":false}]}"
},
{
"role": "system",
"content": "{\"name\":\"Object List\",\"description\":\"A list that describes object
items in the environment that the avatar can see or interact with. The list includes objects
with their names, descriptions, closest spots, spatial positions, and directions along the y-
axis. It also indicates whether an object is grabbable, its parent's name, and its occupation
status. Please use the \\\"closest_spots\\\" parameter to identify the nearest spots of an
object, at any of which you can grab the object. If an object's \\\"is_grabbable\\\" status is
true, it means the object can be grabbed. Important Note: If an object's \\\"is_grabbable\\\"
status is false, it means the object cannot be grabbed. If an object has a valid

\\\"parent_object\\\", it means this object is contained by a container object. The
\\\"parent_object\\\" refers to the container object that holds this object. If an object has a
valid \\\"is_occupied\\\" status, it means an avatar is holding this object and this object
cannot be grabbed for now. Use the list as a reference to perceive the environment or
interact with objects in the environment.\",\"object_list\":[{\"object_name\":\"Peanut butter
(1)\",\"object_description\":\"A jar of peanut butter. $6
each\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.84,\"y\":1.38,\"z\":3.61},\"object_direction\":-
13.0912466,\"is_grabbable\":true,\"parent_object\":\"Aisle 1 Tier
4\"},{\"object_name\":\"Beer (2)\",\"object_description\":\"Premium bear. $4.5
each.\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
1.78,\"y\":1.82,\"z\":3.61},\"object_direction\":-
26.2418747,\"is_grabbable\":true,\"parent_object\":\"Aisle 1 Tier
5\"},{\"object_name\":\"wine\",\"object_description\":\"very expensive wine. $500
each\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
1.47,\"y\":1.36,\"z\":4.05},\"object_direction\":-
20.0152531,\"is_grabbable\":true,\"parent_object\":\"Aisle 2 Tier
4\"},{\"object_name\":\"Beer (1)\",\"object_description\":\"Fresh bear. $2.5
each.\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
1.58,\"y\":1.82,\"z\":3.61},\"object_direction\":-
23.667099,\"is_grabbable\":true,\"parent_object\":\"Aisle 1 Tier
5\"},{\"object_name\":\"Product Shelf (4)\",\"object_description\":\"The leftmost shelf in the
second row\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
12.43,\"y\":0.03,\"z\":25.76},\"object_direction\":-
25.75503,\"is_grabbable\":false},{\"object_name\":\"origin flavor chips
2\",\"object_description\":\"origin flavor chips. on discount $1.5
each.\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.15,\"y\":1.36,\"z\":7.61},\"object_direction\":-
1.10446727,\"is_grabbable\":true,\"parent_object\":\"Aisle 5 Tier
4\"},{\"object_name\":\"Commercial Refrigerator (3)\",\"object_description\":\"A beverage
refrigerator\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
1.09,\"y\":0.03,\"z\":10.02},\"object_direction\":-
6.20513535,\"is_grabbable\":false},{\"object_name\":\"Mayonnaise
(3)\",\"object_description\":\"A jar of mayonnaise. $5.5
each.\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
1.14,\"y\":0.51,\"z\":6.11},\"object_direction\":-
10.6086044,\"is_grabbable\":true,\"parent_object\":\"Aisle 4 Tier
2\"},{\"object_name\":\"Juice\",\"object_description\":\"Juice on discount. $2
each\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.63,\"y\":0.92,\"z\":5.77},\"object_direction\":-
6.20143747,\"is_grabbable\":true,\"parent_object\":\"Aisle 3 Tier
3\"},{\"object_name\":\"origin flavor chips 1\",\"object_description\":\"a bag of origin flavor
chips. on discount $1.5 each.\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.37,\"y\":1.06,\"z\":3.55},\"object_direction\":-

6.024703,\"is_grabbable\":true,\"parent_object\":\"Aisle 1 Tier
3\"},{\"object_name\":\"Sandwich (2)\",\"object_description\":\"Tomato + avocado
sandwich. $2.5 each.\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.78,\"y\":0.48,\"z\":3.61},\"object_direction\":-
12.2474623,\"is_grabbable\":true,\"parent_object\":\"Aisle 1 Tier
2\"},{\"object_name\":\"Mustard (1)\",\"object_description\":\"A bottle of mustard. $3.5
each.\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.53,\"y\":1.38,\"z\":6.11},\"object_direction\":-
4.94205046,\"is_grabbable\":true,\"parent_object\":\"Aisle 4 Tier
4\"},{\"object_name\":\"cokee\",\"object_description\":\"$1.5
each.\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.23,\"y\":1.37,\"z\":8.11},\"object_direction\":-
1.63542235,\"is_grabbable\":true,\"parent_object\":\"Aisle 6 Tier
4\"},{\"object_name\":\"Peanut butter (2)\",\"object_description\":\"A jar of peanut butter.
$6 each\",\"closest_spots\":\"Cashier
desk\",\"object_position\":{\"x\":0.06,\"y\":0.97,\"z\":0.72},\"object_direction\":4.3647995,\
"is_grabbable\":true},{\"object_name\":\"Mayonnaise (2)\",\"object_description\":\"A jar of
mayonnaise. $5.5 each.\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.74,\"y\":0.51,\"z\":6.11},\"object_direction\":-
6.862671,\"is_grabbable\":true,\"parent_object\":\"Aisle 4 Tier
2\"},{\"object_name\":\"cola\",\"object_description\":\"$2
each.\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
1.6,\"y\":0.93,\"z\":7.58},\"object_direction\":-
11.9341459,\"is_grabbable\":true,\"parent_object\":\"Aisle 5 Tier
3\"},{\"object_name\":\"champagne\",\"object_description\":\"champagne from the year
2015. $55 each\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.06,\"y\":0.92,\"z\":4.09},\"object_direction\":-
0.8645667,\"is_grabbable\":true,\"parent_object\":\"Aisle 2 Tier
3\"},{\"object_name\":\"cheese flavor chips 1\",\"object_description\":\"a bag of cheese
flavor chips. on discount $1.5 each.\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.47,\"y\":0.94,\"z\":7.64},\"object_direction\":-
3.556333,\"is_grabbable\":true,\"parent_object\":\"Aisle 5 Tier
3\"},{\"object_name\":\"Product Shelf (3)\",\"object_description\":\"The rightmost shelf in
the first row\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
12.43,\"y\":0.03,\"z\":25.76},\"object_direction\":-
25.75503,\"is_grabbable\":false},{\"object_name\":\"Product Shelf
(1)\",\"object_description\":\"The leftmost shelf in the first
row\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
12.43,\"y\":0.03,\"z\":25.76},\"object_direction\":-
25.75503,\"is_grabbable\":false},{\"object_name\":\"Sandwich
(1)\",\"object_description\":\"Tomato + avocado sandwich. $2.5
each.\",\"closest_spots\":\"\",\"object_position\":{\"x\":1.7,\"y\":1.04,\"z\":0.73},\"object_dir
ection\":66.6969452,\"is_grabbable\":true},{\"object_name\":\"Product Shelf
(6)\",\"object_description\":\"The leftmost shelf in the third

row\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
12.43,\"y\":0.03,\"z\":25.76},\"object_direction\":-
25.75503,\"is_grabbable\":false},{\"object_name\":\"Product Shelf
(7)\",\"object_description\":\"The rightmost shelf in the third
row\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
12.43,\"y\":0.03,\"z\":25.76},\"object_direction\":-
25.75503,\"is_grabbable\":false},{\"object_name\":\"Cash register
(1)\",\"object_description\":\"\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.65,\"y\":0.97,\"z\":0.66},\"object_direction\":-
44.3587723,\"is_grabbable\":false},{\"object_name\":\"Milk (2)\",\"object_description\":\"A
box of milk. 3.5% calcium added. $2
each.\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
1.23,\"y\":0.95,\"z\":6.11},\"object_direction\":-
11.3859482,\"is_grabbable\":true,\"parent_object\":\"Aisle 4 Tier
3\"},{\"object_name\":\"Milk (3)\",\"object_description\":\"A box of milk. 3.5% calcium
added. $2 each.\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
1.0,\"y\":0.95,\"z\":6.11},\"object_direction\":-
9.314708,\"is_grabbable\":true,\"parent_object\":\"Aisle 4 Tier
3\"},{\"object_name\":\"Cereals (1)\",\"object_description\":\"Cereals for kids. $8 each
pack.\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
1.58,\"y\":0.92,\"z\":3.61},\"object_direction\":-
23.6671162,\"is_grabbable\":true,\"parent_object\":\"Aisle 1 Tier
3\"},{\"object_name\":\"Cereals (2)\",\"object_description\":\"Cereals for adults. $10 each
pack.\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
1.91,\"y\":0.92,\"z\":3.61},\"object_direction\":-
27.8144455,\"is_grabbable\":true,\"parent_object\":\"Aisle 1 Tier
3\"},{\"object_name\":\"Cereals (3)\",\"object_description\":\"Cereals for kids. $8 each
pack.\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
2.22,\"y\":0.92,\"z\":3.61},\"object_direction\":-
31.6152077,\"is_grabbable\":true,\"parent_object\":\"Aisle 1 Tier
3\"},{\"object_name\":\"Product Shelf (2)\",\"object_description\":\"The middle shelf in the
first row\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
12.43,\"y\":0.03,\"z\":25.76},\"object_direction\":-
25.75503,\"is_grabbable\":false},{\"object_name\":\"Mayonnaise
(1)\",\"object_description\":\"A jar of mayonnaise. $5.5
each.\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.94,\"y\":0.51,\"z\":6.11},\"object_direction\":-
8.74963,\"is_grabbable\":true,\"parent_object\":\"Aisle 4 Tier
2\"},{\"object_name\":\"Freezer (2)\",\"object_description\":\"An ice creem
freezer\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
3.6,\"y\":0.03,\"z\":8.54},\"object_direction\":-
22.8624649,\"is_grabbable\":false},{\"object_name\":\"Mustard
(2)\",\"object_description\":\"A bottle of mustard. $3.5
each.\",\"closest_spots\":\"\",\"object_position\":{\"x\":-

0.32,\"y\":1.38,\"z\":6.11},\"object_direction\":-
3.019539,\"is_grabbable\":true,\"parent_object\":\"Aisle 4 Tier 4\"},{\"object_name\":\"Milk
(1)\",\"object_description\":\"A box of milk. 3.5% calcium added. $2
each.\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
1.48,\"y\":0.95,\"z\":6.12},\"object_direction\":-
13.591423,\"is_grabbable\":true,\"parent_object\":\"Aisle 4 Tier
3\"},{\"object_name\":\"Product Shelf (5)\",\"object_description\":\"The rightmost shelf in
the second row\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
12.43,\"y\":0.03,\"z\":25.76},\"object_direction\":-
25.75503,\"is_grabbable\":false},{\"object_name\":\"Poster
1\",\"object_description\":\"Poster: Fresh orange juice on sale! $2 each. original price is
$3.5 each $\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
4.08,\"y\":1.1,\"z\":3.38},\"object_direction\":-
50.43155,\"is_grabbable\":false},{\"object_name\":\"ketchup\",\"object_description\":\"a
bottle of ketchup. $2 each\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.84,\"y\":0.93,\"z\":8.13},\"object_direction\":-
5.8791666,\"is_grabbable\":true,\"parent_object\":\"Aisle 6 Tier
3\"},{\"object_name\":\"Cashier
table\",\"object_description\":\"\",\"closest_spots\":\"Cashier
desk\",\"object_position\":{\"x\":0.5,\"y\":0.04,\"z\":0.77},\"object_direction\":32.81278,\"is
_grabbable\":false},{\"object_name\":\"massage cream\",\"object_description\":\"a 200ml
massage cream. $35 each\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
2.62,\"y\":1.36,\"z\":4.09},\"object_direction\":-
32.6143646,\"is_grabbable\":true,\"parent_object\":\"Aisle 2 Tier
4\"},{\"object_name\":\"Poster 3\",\"object_description\":\"Poster: original flavor and
cheese flavor chips. Buy 2 get one free. Each price is
$1.5\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
4.09,\"y\":1.09,\"z\":4.41},\"object_direction\":-
42.9067726,\"is_grabbable\":false},{\"object_name\":\"hand
cream\",\"object_description\":\"a 50 ml hand cream. $5
each\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
2.66,\"y\":1.36,\"z\":4.04},\"object_direction\":-
33.3525734,\"is_grabbable\":true,\"parent_object\":\"Aisle 2 Tier
4\"},{\"object_name\":\"Door (Left)\",\"object_description\":\"The left-hand door of the
store\",\"closest_spots\":\"\",\"object_position\":{\"x\":2.44,\"y\":1.06,\"z\":6.74},\"object_di
rection\":19.8868828,\"is_grabbable\":false},{\"object_name\":\"Door
(Right)\",\"object_description\":\"The right-hand door of the
store\",\"closest_spots\":\"\",\"object_position\":{\"x\":2.44,\"y\":1.06,\"z\":8.59},\"object_di
rection\":15.8488073,\"is_grabbable\":false},{\"object_name\":\"Freezer
(1)\",\"object_description\":\"An ice creem
freezer\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
3.61,\"y\":0.03,\"z\":7.08},\"object_direction\":-
27.0151081,\"is_grabbable\":false},{\"object_name\":\"Commercial Refrigerator
(2)\",\"object_description\":\"A beverage

refrigerator\",\"closest_spots\":\"\",\"object_position\":{\"x\":-
0.32,\"y\":0.03,\"z\":10.03},\"object_direction\":-
1.82069683,\"is_grabbable\":false},{\"object_name\":\"Commercial Refrigerator
(1)\",\"object_description\":\"A beverage
refrigerator\",\"closest_spots\":\"\",\"object_position\":{\"x\":0.46,\"y\":0.03,\"z\":10.03},\"o
bject_direction\":2.62547374,\"is_grabbable\":false}]}"
},
{
"role": "system",
"content": "{\"name\":\"Character List\",\"description\":\"A list describes all the
character avatars in the environment. This list contains characters with their names,
descriptions, spatial positions, and spatial directions along the y axis. Use the list as a
reference to perceive character avatars in the
environment.\",\"character_list\":[{\"character_name\":\"Player
(Me)\",\"character_description\":\"A customer of the store\",\"character_position\":{\"x\":-
0.11,\"y\":0.2,\"z\":1.22},\"character_direction\":-5.169073},{\"character_name\":\"Avatar
(You)\",\"character_description\":\"A counter stak of the convenience
store\",\"character_position\":{\"x\":0.0,\"y\":0.0,\"z\":0.0},\"character_direction\":0.0}]}"
},
{
"role": "system",
"content": "{\"name\":\"Character's Hands State\",\"description\":\"'left_hand_object'
denotes the object currently held by the left hand. 'right_hand_object' denotes the object
currently held by the right hand. If either value is 'Empty', it means the specific hand is
empty and available to interact with other objects.\",\"avatar_state\":{\"name\":\"Avatar
(you)\",\"left_hand_object\":\"Empty\",\"right_hand_object\":\"Empty\"},\"player_state\":{\"
name\":\"Player (me)\",\"left_hand_object\":\"Empty\",\"right_hand_object\":\"Empty\"}}"
},
{
"role": "user",
"content": "<Player moves to (1.076191, 0.1934951, 6.56734)>"
},
{
"role": "user",
"content": "<Player moves to (0.9144081, 0.2000498, 7.667905)>"
},
{
"role": "user",
"content": "<Player moves to (1.194124, 0.1934951, 8.969465)>"
},
{
"role": "user",
"content": "<Player moves to (-0.1004406, 0.1934951, 9.242599)>"
},

{
"role": "user",
"content": "<Player moves to (-2.622591, 0.1934952, 8.557277)>"
},
{
"role": "user",
"content": "<Player moves to (-2.33429, 0.1934952, 7.056303)>"
},
{
"role": "user",
"content": "<Player moves to (-1.516973, 0.1934952, 6.44771)>"
},
{
"role": "user",
"content": "<Player moves to (0.5621392, 0.1934951, 5.513387)>"
},
{
"role": "user",
"content": "<Player moves to (0.06363191, 0.2010497, 1.626612)>"
},
{
"role": "user",
"content": "Customer: Hey, how much is the milk for?"
},
{
"role": "assistant",
"content": "Counter Stak: The milk goes for $2 each. It's a box of milk with 3.5%
calcium added. Anything else I can help you find today?"
},
{
"role": "user",
"content": "<Player moves to (0.5331991, 0.1934951, 2.840597)>"
},
{
"role": "user",
"content": "<Player moves to (1.029485, 0.1934951, 5.30425)>"
},
{
"role": "user",
"content": "<Player moves to (-0.1791987, 0.1934951, 7.089159)>"
},
{
"role": "user",
"content": "<Player moves to (-1.003158, 0.1934951, 7.160236)>"

},
{
"role": "user",
"content": "<Player moves to (0.3264987, 0.1934951, 5.206827)>"
},
{
"role": "user",
"content": "<Player moves to (0.373145, 0.2004361, 2.117098)>"
},
{
"role": "user",
"content": "Customer: Can you tell me where the milk is?"
},
{
"role": "assistant",
"content": "Counter Stak: Sure, the milk is located in Aisle 4, Tier 3. If you need more,
just let me know!"
},
{
"role": "user",
"content": "<Player moves to (1.356798, 0.193495, 5.906858)>"
},
{
"role": "user",
"content": "<Player moves to (1.046156, 0.193495, 6.648202)>"
},
{
"role": "user",
"content": "<Player moves to (0.08381611, 0.1934951, 6.873918)>"
},
{
"role": "user",
"content": "<Player moves to (0.9012686, 0.1934951, 5.22525)>"
},
{
"role": "user",
"content": "<Player's right hand points to champagne>"
},
{
"role": "user",
"content": "Customer: Can you tell me what this is?"
},
{
"role": "assistant",

"content": "Counter Stak: Ah, you're pointing at our champagne from the year 2015.
It's quite exquisite and priced at $55 each. Anything else you'd like to know?"
},
{
"role": "user",
"content": "<Player moves to (1.009242, 0.1934951, 6.721435)>"
},
{
"role": "user",
"content": "<Player moves to (0.4729962, 0.1934951, 7.432083)>"
},
{
"role": "user",
"content": "<Player's right hand grabs origin flavor chips 1>"
},
{
"role": "user",
"content": "<Player moves to (1.421953, 0.193495, 5.939298)>"
},
{
"role": "user",
"content": "<Player moves to (0.4083078, 0.1934951, 3.363313)>"
},
{
"role": "user",
"content": "<Player's right hand releases origin flavor chips 1>"
},
{
"role": "user",
"content": "<Player moves to (-0.0514384, 0.2010497, 1.236349)>"
},
{
"role": "user",
"content": "<Player's right hand points to origin flavor chips 1>"
},
{
"role": "user",
"content": "Customer: What is this?"
},
{
"role": "assistant",
"content": "Counter Stak: That's a bag of origin flavor chips, currently on discount for
$1.5 each. Would you like to grab a bag?"
},

{
"role": "user",
"content": "Customer: Let me check it out."
},
{
"role": "assistant",
"content": "Counter Stak: Sure thing. Take your time to check it out. If you have any
questions or need further assistance, feel free to ask!"
},
{
"role": "user",
"content": "<Player's right hand touches origin flavor chips 1>"
},
{
"role": "user",
"content": "<Player's right hand grabs origin flavor chips 1>"
},
{
"role": "user",
"content": "<Player's right hand releases origin flavor chips 1>"
},
{
"role": "user",
"content": "<Player moves to (-0.3464338, 0.1934951, 3.063518)>"
},
{
"role": "user",
"content": "<Player's right hand grabs Peanut butter (2)>"
},
{
"role": "user",
"content": "<Player moves to (-0.4786616, 0.2010497, 1.988413)>"
},
{
"role": "user",
"content": "<Player's right hand releases Peanut butter (2)>"
},
{
"role": "user",
"content": "<Player moves to (-0.3463375, 0.1934951, 2.952121)>"
},
{
"role": "user",
"content": "<Player's right hand points to Sandwich (1)>"

},
{
"role": "user",
"content": "<Player's right hand grabs Sandwich (1)>"
},
{
"role": "user",
"content": "<Player's right hand releases Sandwich (1)>"
},
{
"role": "user",
"content": "<Player moves to (1.569798, 0.2010497, 1.223906)>"
},
{
"role": "user",
"content": "<Player moves to (-0.3729983, 0.2010497, 1.585102)>"
},
{
"role": "user",
"content": "<Player's right hand points to Peanut butter (2)>"
},
{
"role": "user",
"content": "Customer: Can you check this out for me?"
},
{
"role": "assistant",
"content": "Counter Stak: That's a jar of peanut butter, priced at $6 each. It's quite
popular for its creamy texture and rich flavor. Do you need anything else?"
},
{
"role": "user",
"content": "<Player moves to (0.370036, 0.1962744, 2.135883)>"
},
{
"role": "user",
"content": "<Player's right hand points to Peanut butter (2)>"
},
{
"role": "user",
"content": "<Player moves to (-0.3368512, 0.2010497, 1.728058)>"
},
{
"role": "user",

"content": "Customer: Thank you. Can you I want to get it"
},
{
"role": "assistant",
"content": "Counter Stak: Absolutely, you've made a great choice with the peanut
butter. You can grab it and bring it to the counter whenever you're ready to check out.
Anything else you need help with?"
},
{
"role": "user",
"content": "<Player's right hand grabs Peanut butter (2)>"
},
{
"role": "user",
"content": "<Player's right hand releases Peanut butter (2)>"
},
{
"role": "user",
"content": "Customer: I'm ready to check."
},
{
"role": "assistant",
"content": "Counter Stak: Perfect! Let me ring that up for you. Alright, your total
comes to $6 for the peanut butter. How would you like to pay today?"
},
{
"role": "user",
"content": "Customer: I'll use a credit card."
}
],
"temperature": 0.8,
"tools": [
{
"type": "function",
"function": {
"name": "left_hand_grab_object",
"description": "Use your left hand to grab an object in the environment",
"parameters": {
"type": "object",
"properties": {
"object_name": {
"type": "string",
"description": "Exact name of the object in the environment"
}

},
"required": [
"object_name"
]
}
}
},
{
"type": "function",
"function": {
"name": "right_hand_grab_object",
"description": "Use your right hand to grab an object in the environment",
"parameters": {
"type": "object",
"properties": {
"object_name": {
"type": "string",
"description": "Exact name of the object in the environment"
}
},
"required": [
"object_name"
]
}
}
},
{
"type": "function",
"function": {
"name": "look_at_object",
"description": "Look at an object in the environment",
"parameters": {
"type": "object",
"properties": {
"object_name": {
"type": "string",
"description": "Exact name of the object in the environment"
}
},
"required": [
"object_name"
]
}
}

},
{
"type": "function",
"function": {
"name": "left_hand_point_to_object",
"description": "Use your left hand to point to an object from distance in the
environment",
"parameters": {
"type": "object",
"properties": {
"object_name": {
"type": "string",
"description": "Exact name of the object in the environment"
}
},
"required": [
"object_name"
]
}
}
},
{
"type": "function",
"function": {
"name": "right_hand_point_to_object",
"description": "Use your right hand to point to an object from distance in the
environment",
"parameters": {
"type": "object",
"properties": {
"object_name": {
"type": "string",
"description": "Exact name of the object in the environment"
}
},
"required": [
"object_name"
]
}
}
},
{
"type": "function",
"function": {

"name": "left_hand_touch_object",
"description": "Use your left hand to touch an object in the environment",
"parameters": {
"type": "object",
"properties": {
"object_name": {
"type": "string",
"description": "Exact name of the object in the environment"
}
},
"required": [
"object_name"
]
}
}
},
{
"type": "function",
"function": {
"name": "right_hand_touch_object",
"description": "Use your right hand to touch an object in the environment",
"parameters": {
"type": "object",
"properties": {
"object_name": {
"type": "string",
"description": "Exact name of the object in the environment"
}
},
"required": [
"object_name"
]
}
}
},
{
"type": "function",
"function": {
"name": "left_hand_release_object_to_container",
"description": "Release an object that currently hold with the left hand upon or into
another object that serves as a container",
"parameters": {
"type": "object",
"properties": {

"object_name": {
"type": "string",
"description": "Exact name of the object in the environment"
},
"container_name": {
"type": "string",
"description": "Exact name of the object in the environment that serves as a
container"
}
},
"required": [
"object_name",
"container_name"
]
}
}
},
{
"type": "function",
"function": {
"name": "right_hand_release_object_to_container",
"description": "Release an object that currently hold with the right hand upon or
into another object that serves as a container",
"parameters": {
"type": "object",
"properties": {
"object_name": {
"type": "string",
"description": "Exact name of the object in the environment"
},
"container_name": {
"type": "string",
"description": "Exact name of the object in the environment that serves as a
container"
}
},
"required": [
"object_name",
"container_name"
]
}
}
},
{

"type": "function",
"function": {
"name": "move_to",
"description": "Move to a spot in the environment",
"parameters": {
"type": "object",
"properties": {
"spot_name": {
"type": "string",
"description": "Exact name of a spot in the environment"
}
},
"required": [
"spot_name"
]
}
}
}
],
"tool_choice": "auto"
}
