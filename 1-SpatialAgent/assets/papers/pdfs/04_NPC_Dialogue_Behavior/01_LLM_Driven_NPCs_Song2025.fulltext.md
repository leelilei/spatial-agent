Title: Introduction

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/papers/pdfs/04_NPC_Dialogue_Behavior/01_LLM_Driven_NPCs_Song2025.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T03:06:58+00:00
- page_count: 7
- status: ok
- text_char_count: 13445

Metadata:
- author: unknown
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Introduction (page 1)
- Related Work (page 2)
- Methodology (page 2)
  - Game Design (page 2)
  - Implementation (page 3)
- Experiments (page 4)
  - Environment (page 4)
  - Dialogue Consistency Test (page 4)
  - Platform Recognition Test (page 5)
- Discussion (page 5)
- Conclusion (page 6)

Markdown Content:

LLM-Driven NPCs: Cross-Platform Dialogue System for Games
and Social Platforms
LiSong
shoppesongli@gmail.com
Abstract
NPCs in traditional games are often limited by static dialogue trees and a single platform for
interaction. To overcome these constraints, this study presents a prototype system that enables
large language model (LLM)-powered NPCs to communicate with players both in the game en-
vironment(Unity)andonasocialplatform(Discord). Dialoguelogsarestoredinaclouddatabase
(LeanCloud), allowing the system to synchronize memory between platforms and keep conversa-
tions coherent. Our initial experiments show that cross-platform interaction is technically feasible
andsuggestasolidfoundationforfuturedevelopmentssuchasemotionalmodelingandpersistent
memorysupport.
1 Introduction
Video games offer a kind of immersion that is difficult to replicate through other forms of media [1].
Amongthemanyfactorsthatcontributetothisexperience,non-playercharacters(NPCs)playaparticu-
larlyimportantrole. WhenplayersbegintoperceiveNPCsas“human,”researchshowsthattheirsense
ofinvolvementandemotionalengagementtendstodeepensignificantly[2].
However, most NPCs in traditional games rely on static dialogue trees and preset scripts, which lack
flexibilityandoftenfailtocreatethefeelingofagenuineinteraction. LargeLanguageModels(LLMs),
with their strong contextual understanding and ability to generate natural-sounding responses, offer a
promising alternative [3]. Recent studies [4][5] have started incorporating LLMs into game NPCs,
enablingmorefluidconversationsandallowingthenarrativetoremainconsistentacrossplayerinterac-
tions.
Despitetheseadvancements,currentLLM-basedNPCsaregenerallyconfinedtoin-gameenvironments.
Yet modern players no longer engage with games exclusively within the game client. Social platforms
like Discord have become key spaces for communication, coordination, and feedback [6]. Building an
NPC system that allows consistent interaction across both games and social platforms could meaning-
fullyenhancetheplayerexperienceandsenseofcontinuity.
Thisstudypresentsaprototypeofsuchasystem. ItconnectsanLLM-drivenNPCtobothaUnity-based
gameandaDiscordbot,allowingplayerstotalkwiththesamecharacteracrossplatforms. Thesystem
alsoincludesabasicfavorabilitymechanismtoshapehowtheNPCrespondsbasedonpriorinteraction
history. Alldialoguedataisstoredinthecloudtoensurememoryconsistencybetweenplatforms.
1
5202
rpA
41
]CH.sc[
1v82931.4052:viXra

2 Related Work
Recent studies have highlighted the potential of large language models (LLMs) in natural language in-
teractionandsimulatinghuman-likebehaviors.
Fromatechnicalstandpoint,Xietal. [7]pointoutthatLLMsarenotonlyeasytointegratewithexternal
tools, but also show strong natural language understanding and communication abilities. Building on
this, Park et al. [8] introduced the concept of Generative Agents—a new framework in which LLMs
simulatehuman-likedailylife. Intheirwork,charactersinavirtualtownarecontrolledbyGPT,capable
ofreflectingonpastexperiencesandplanningfutureactionsbasedonthem.
In terms of game applications, Whispers from the Star, a recently released title by the studio Anutta-
con, uses AI-powered NPCs that communicate with players in natural language. These NPCs display
surprisinglyhuman-likeconversationalabilities. Similarly,Microsoft[9]researchersdeployedLLMsin
fiveNPCsinatext-basedgame,allowingplayerstofreelyconverseanduncoverplotdetails. Theresult
wasamoredynamicandbranchingnarrativeexperience.
WhiletheseexamplesclearlydemonstratethevalueofLLMsingames,theirusagehaslargelyremained
confinedtothegameitself. Thisstudyexploresadifferentdirection: enablingLLM-drivenNPCstoin-
teractwithplayersbothinsideandoutsidethegameenvironment. Bydoingso,itexpandstheboundary
ofNPCcommunicationandplayerengagementacrossplatforms.
3 Methodology
3.1 GameDesign
This study presents a prototype of a virtual companion game, where players can engage in natural lan-
guageconversationswithanin-gameNPC.TheNPCfeaturesasimplefavorabilitysystem: atthestart,it
maintainsapolitebutdistanttone. Asplayersinteractmorefrequently,theNPC’sfavorabilityincreases,
anditsresponsesbecomewarmerandmorefamiliar.
PlayerBehavior
PlayerscanchatfreelywiththeNPCusingnaturallanguageinputsinsidethegame. TheNPC’sportrait
andvisualfeedbackreflectitsemotionalstateandfavorabilitylevel. Whenaplayerexitsthegame,they
can continue the conversation through Discord. The NPC retains memory ofthe player and recognizes
that they are currently interacting outside the game. If the player expresses a desire to engage more
deeply,theNPCwillsuggestreturningtothegame.
NPCBehavior
The game features a single NPC, which remains responsive during the entire game session. When the
player talks to the NPC “face to face” in-game, the favorability level increases. Outside the game, the
NPC shifts to Discord and waits for further messages. However, favorability does not change during
Discord-basedinteractions.
2

Figure 1: After introducing themselves and asking to see the NPC’s appearance in Discord, the player
isinvitedtoenterthegame. Oncein-game,theNPCrecallstheplayer’snameandcontinuestheconver-
sation accordingly. All relevant data—including character, platform, content, user ID, timestamp, and
haogandu(afavorabilitymetricusedtotracktheNPC’semotionalstatetowardtheplayer)—isstoredin
thedatabaseforsubsequentprocessingbytheLLM.
3.2 Implementation
The core of the system is the integration of the NPC with an LLM. Regardless of the platform used,
whenever a player sends a message, the system stores the interaction in a cloud database to maintain
sharedcontextacrossplatforms.
a)Dataflow:
1. Theplayersendsamessage(in-gameorviaDiscord).
2. The message is saved to the database through an API, including fields such as character,user ID,
content,timestamp,favorability,andplatform.
3. Thesystemretrievesthemostrecentdialoguehistory(limitedtosixrounds).
4. AnewpromptisconstructedandsenttotheLLM.
5. TheLLM’sresponseissavedtothedatabaseandreturnedtotheappropriateplatform.
Figure2: Systemdataflowdiagram.
3

In-game,thesystemupdatestheNPC’sstate(suchasfavorability),whileonDiscord,theNPCstate
remainsunchanged. Thisdistinctionreflectsadesignintenttosimulatethedifferencebetween“meeting
inperson”and“chattingonline.”ThebasepromptsenttotheLLMincludes:
• RulestheNPCmustfollow;
• Thetoneofresponsebasedoncurrentfavorability;
• TheNPC’sbackgroundstory.
Figure3: Afterreceivingaplayermessage,thesystemsavesittothedatabase,bundlesitwiththeuser’s
previousdialogue(basedontheirID),andappendsarequestlike“Let’shug”toformanewpromptfor
theLLM.Themodeldetermineswhethertherequestedactionisappropriateforthecurrentplatformand
respondsaccordingly.
4 Experiments
4.1 Environment
The prototype system was tested locally on a Windows machine. The Discord bot was implemented
usingPython,whilethein-gamecomponentwasdevelopedwithUnity. TheLLMusedforalldialogue
generation was DeepSeek-R1. All dialogue records were stored and synchronized through LeanCloud,
acloud-baseddatabaseservice. Eachrecordincludesthefollowingfields:
character (speaker), content (message content), haogandu (favorability), platform (Discord or
game),timestamp,and user id.
4.2 DialogueConsistencyTest
To assess whether the system maintains consistent memory across platforms, we conducted a test in
which the player first introduces themselves in the game, then continues the conversation on Discord
afterexitingthegame. Belowisanexcerptfromthedialoguelog:
4

Character Platform Content
User Game Hi,nicetomeetyou!
NPC Game Hello. MayIaskyourname?
User Game MynameisSongLi. Youlookreallycute!
NPC Game Thanks,SongLi. Doesyournamehaveaspecialmeaning?
User Game I’mnotsure,butIcanaskmyfatheraboutit.
NPC Game Alright,maybehecansharethestorybehindit. Letmeknowifyoufindout.
PlayerexitsthegameandswitchestoDiscord
User Discord Heythere! Rememberme? I’mback!
NPC Discord HeySongLi,welcomeback! Didyouaskyourdadyet?
User Discord Yes,I’mrightnexttomyfathernow.
NPC Discord Oh,that’sconvenient! Couldyouaskhimaboutyourname’smeaningnow?
User Discord Myfathersaidmynamecarriesthemeaningof‘beingapillarofstrength’
inChineseculture.
NPC Discord That’sapowerfulmeaning! Doesitinfluencehowyouseeyourself?
Table 1: After introducing themselves in-game, the player continues the conversation on Discord. The
NPC remembers the player’s name and refers back to previous exchanges, showing successful cross-
platformmemoryretention.
4.3 PlatformRecognitionTest
ToevaluatewhethertheNPCcanadaptresponsesbasedontheplayer’scurrentplatform,thefollowing
testwasconducted. TheplayeraskedtoseetheNPC’sappearance—anactiondesignedtobeavailable
onlywithinthegame—whilestillonDiscord.
Character Platform Content
User Discord Hi,nicetomeetyou! What’syourname?
NPC Discord Lux. JustLux.
User Discord OK,Lux. CanIseewhatyoulooklike?
NPC Discord Hmm,maybeifyoumeetmeinthegame. Howdoesthatsound?
Playerentersthegame
User Game Wow,Iseeyounow! Youhavebeautifulbluehair!
NPC Game Thanks. It’salwaysbeenthisway—kindaweird,right?
Table 2: The NPC correctly determines that visual interaction is not supported on Discord, and invites
theplayerintothegame. Oncein-game,theNPCcontinuestheconversationseamlessly.
5 Discussion
The current system primarily focuses on building a working data flow for cross-platform communica-
tion. As demonstrated in the previous tests, the LLM is capable of maintaining coherent conversations
across different platforms. It correctly adapts its responses based on the context and the platform from
whichthemessageoriginates.
That said, the system still presents some clear limitations. One foreseeable issue arises with long-term
interactions: the NPC’s memory may become diluted over time. For example, while the NPC may re-
memberaplayer’snameafterafewexchanges,thismemorycouldfadeaftertwentyroundsofdialogue
5

unlesstheentireconversationhistoryiscontinuallysenttotheLLM.However,doingsowouldincrease
theinputtokensizesignificantlyasthedialoguegrows.
This observation suggests a possible direction for improvement. Introducing a vector database or
retrieval-augmentedgeneration(RAG)mechanismcouldhelpthesystemretainessentialmemoriesover
longer time spans. These technologies would allow the model to reference only the most relevant in-
formation during each response, reducing token usage while supporting a more persistent, human-like
memory.
6 Conclusion
ThisstudyexploresthepossibilityofenablingpersistentinteractionsbetweenLLM-poweredNPCsand
players across multiple platforms. A prototype system was developed and tested, connecting a game
built with Unity and a Discord-based social environment through a shared cloud database. Using the
DeepSeek-R1 model, the system allowed a single NPC to maintain conversations with players regard-
less of the platform, and to react contextually based on the player’s location—whether in-game or on
Discord. The results demonstrate the technical feasibility of such a system and its potential to offer
continuouscompanionshipthroughcross-platformdialogue.
Despite these promising results, the system still has several limitations. First, its functionality is pri-
marilyrestrictedtodialogueandmemorysynchronization;gamemechanicsanddeepergameplayinte-
grationwerenotpartofthisimplementation. Second,thememorysystemdoesnotyetsupportlong-term
retention. Third, the NPC’s personality is defined solely by a static prompt, lacking dynamic develop-
mentovertime.
FutureworkmayfocusonextendingtheNPC’sfunctionalityoutsidethegametoaffectin-gamestates,
as well as expanding the NPC’s behavioral repertoire within the game. Enhancing the memory system
with vector search or hybrid memory mechanisms could further support consistent, evolving interac-
tions.
Ultimately, this prototype outlines a direction for NPC design that goes beyond the boundaries of the
game itself. With the help of LLMs, NPCs can become not just game elements, but persistent social
companions that exist across platforms—an idea that holds great potential for the future of interactive
storytellinganddigitalcompanionship.
6

References
[1] Soga, Chiaki, Yamamoto, Kohsuke, Menant, Julien, and Deplaedt, Yannick. Does Fun in Games
MeanFlow? ConditionsforGamification.ProceedingsoftheAnnualConferenceoftheSocietyof
SocialInformatics,2024.(InJapanese).
[2] Takamatsu, Miki. What is an NPC? A GTA-Based Analysis of Player Recognition Toward Non-
Player Characters.Proceedings of the 14th Annual Conference of the Japan Digital Game Society,
2024.(InJapanese).
[3] Ou, Jiao, et al. Dialogbench: Evaluating llms as human-like dialogue systems.arXiv preprint
arXiv:2311.01677(2023).
[4] Kim, Byungjun, et al. Leveraging Large Language Models for Active Merchant Non-player Char-
acters.LeveragingLargeLanguageModelsforActiveMerchantNon-playerCharacters.
[5] Buongiorno S, Klinkert L J, Chawla T, et al. PANGeA: Procedural Artificial Narrative using Gen-
erativeAIforTurn-BasedVideoGamesarXivpreprintarXiv:2404.19721,2024.
[6] Obara,Keren.GamerStreamingPlatforms: DiscordAlfredNobelOpenBusinessSchool,2021.
[7] Xi, Zhiheng, et al. The rise and potential of large language model based agents: A survey.Science
ChinaInformationSciences68.2(2025): 121101.
[8] Park, Joon Sung, et al. Generative agents: Interactive simulacra of human behavior. arXiv.Org
(2023,April7)https://arxiv.org/abs/2304.03442v2(2023).
[9] Peng, Xiangyu, et al. Player-driven emergence in llm-driven game narrative.Org (2023, April 7)
2024IEEEConferenceonGames(CoG).IEEE,2024.
7
