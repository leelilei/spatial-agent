Title: Fixed-Persona SLMs with Modular Memory: Scalable NPC Dialogue on Consumer Hardware

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/papers/pdfs/04_NPC_Dialogue_Behavior/04_Fixed_Persona_SLMs_Braas2025.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T03:07:00+00:00
- page_count: 8
- status: ok
- text_char_count: 37167

Metadata:
- author: Martin Braas; Lukas Esterle
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- none

Markdown Content:

Fixed-Persona SLMs with Modular Memory: Scalable NPC Dialogue on
Consumer Hardware
MartinBraasAndreasen1,LukasEsterle1,2
1DepartmentofElectricalandComputerEngineering,AarhusUniversity
2DIGIT
mba@ece.au.dk;lukas.esterle@ece.au.dk
Abstract text.Atruntime,eachmodelusestwodistincttypesofmem-
ory: conversational memory, preserving previous interac-
LargeLanguageModels(LLMs)havedemonstratedremark- tions between the NPC and player to maintain continuity,
ablecapabilitiesingeneratinghuman-liketext,yettheirap-
andworldknowledgememory,providingcontextuallyrele-
plicability to dialogue systems in computer games remains
vant facts and narrative background specific to the NPC’s
limited.Thislimitationarisesfromtheirsubstantialhardware
role. This architecture enables the deployment of multi-
requirements,latencyconstraints,andthenecessitytomain-
ple, expressive NPCs with long-term memory without re-
tainclearlydefinedknowledgeboundarieswithinagameset-
ting.Inthispaper,weproposeamodularNPCdialoguesys- training or reloading new models during gameplay. Each
tem that leverages Small Language Models (SLMs), fine- SLM is trained with a distinct, embedded persona using a
tuned to encode specific NPC personas and integrated with lightweight fine-tuning pipeline. At runtime, the model is
runtime-swappable memory modules. These memory mod- coupledwithadedicatedmemorystore,dynamicallyswap-
ules preserve character-specific conversational context and pabletoreflectindividualNPCinstancesinthegame
worldknowledge,enablingexpressiveinteractionsandlong-
Thisdesignpreservescharacteridentity(personaisfixed
term memory without retraining or model reloading dur-
in training), while supporting flexible, context-rich interac-
inggameplay.Wecomprehensivelyevaluateoursystemus-
tions through memory. It allows the same model to power
ingthreeopen-sourceSLMs:DistilGPT-2,TinyLlama-1.1B-
Chat,andMistral-7B-Instruct,trainedonsyntheticpersona- multipleNPCsofthesametype,suchasseveralinnkeepers
aligneddataandbenchmarkedonconsumer-gradehardware. or guards, pilots or mechanics, each with their own unique
Whileourapproachismotivatedbyapplicationsingaming, memory and interaction history. The result is a scalable,
its modular design and persona-driven memory architecture fully local NPC dialogue system, meaning that models can
holdsignificantpotentialforbroaderadoptionindomainsre- rundirectlyonconsumerhardwarewithoutrelyingonexter-
quiringexpressive,scalable,andmemory-richconversational nalcloudservicesorAPIs,deliveringhighqualityresponses
agents, such as virtual assistants, customer support bots, or
even under hardware constraints. Although presented pri-
interactiveeducationalsystems.
marilyinthecontextofNPCsandcomputergames,itsmod-
ulardesignandpersona-drivenapproachmakeitbroadlyap-
Introduction plicable to any domain requiring expressive, memory-rich
conversational agents, such as virtual assistants, customer
Non-playable characters (NPCs) are central to immersive
supportbots,orinteractiveeducationalsystems.
storytelling and dynamic player experiences in modern
Tosupportthisarchitecture,weimplementafullpipeline:
video games. Yet, most commercial NPC systems rely on
a multi-stage fine-tuning process for fast NPC creation,
handcrafted dialogue trees or rigid behavior scripts, which
a modular memory system using ChromaDB, and (cur-
scale poorly and fail to produce nuanced or long-term co-
rently,pre-gameintegration)aCLI-basedruntimethatcom-
herent interactions (Schlu¨nder and Klabunde 2013). More
poses prompts dynamically with retrieved memory and
recently,largelanguagemodels(LLMs)haveenabledopen-
player input. We evaluate our system using three open-
ended, expressive dialogue generation, but their substantial
sourceSLMs:DistilGPT-2(DistilBERT2023),TinyLlama-
hardware requirements and reliance on cloud APIs make
1.1B-Chat(Zhangetal.2024;TinyLlamaTeam2023),and
themimpracticalforlocal,real-timeuseingames,especially
Mistral-7B-Instruct(Jiangetal.2023;MistralAI2023),all
whenmultipledistinctcharactersareneeded(Parvini2024;
trainedonsyntheticpersona-aligneddata,andbenchmarked
GaoandEmami2023).
onconsumer-gradehardware.
Inthiswork,weexploreanalternativedesign:SmallLan-
Thispapermakesthefollowingcontributions:
guageModels(SLMs)fine-tunedforspecificNPCpersonas,
• AmodularNPCdialoguesystemwhereeachfine-tuned
paired with runtime-swappable memory modules that pre-
SLMencodesafixedpersona,andmemorymodulescan
servecharacter-specificknowledgeandconversationalcon-
be swapped at runtime to enable distinct character in-
Copyright©2026,AssociationfortheAdvancementofArtificial stances.
Intelligence(www.aaai.org).Allrightsreserved. • Alightweightseed-basedfine-tuningpipelinethaten-
5202
voN
31
]IA.sc[
1v77201.1152:viXra

ablesrapidpersonainstantiationwithoutrelyingonpro- agent.Themodelisresponsibleformaintainingin-character
prietarymodels. behavior, tone and knowledge boundaries. During deploy-
• A retrieval-augmented runtime framework for man- ment, the system combines this static behavioral core with
aging conversational history and world knowledge in dynamic memory components to generate contextually ap-
memory,supportinglong-termcoherentinteractions. propriateandtemporallycoherentdialogue.
• Acomprehensiveevaluationacrossfactuality,memory The full system includes: (i) the fine-tuned SLM back-
retention, fluency, latency, and memory usage - demon- end; (ii) two modular memory stores per NPC; (iii) a run-
stratingthefeasibilityofexpressiveNPCdialogueonlo- time prompt composer, and (iv) a command-line interface
calconsumerhardware. forinteractionandevaluation.
RelatedWork FixedPersonaviaFine-Tuning
Each NPC’s personality is fine-tuned using Low-Rank
Dialogue systems for non-playable characters (NPCs) have
Adaptation (LoRA), training on a small curated dataset.
historically relied on handcrafted dialogue trees or rule-
This dataset encodes the character’s voice, behavior con-
based methods, which limit scalability and expressive in-
straints,andpermissibleknowledge.Forexample,afriendly
teraction (Schlu¨nder and Klabunde 2013). Recent interest
innkeeperNPCistrainedtoavoidtopicsbeyondtheirworld
has shifted towards leveraging generative AI models, such
knowledgeorbehaveoutsidetheirtemperament.
astransformer-basedarchitectures,toenhanceNPCrealism
These personas are not injected at runtime. The result is
and interactivity in games (Gao and Emami 2023; Parvini
a stable, character-consistent response style that avoids the
2024). NVIDIA’s ACE platform exemplifies recent indus-
brittleness and token overhead of in-context prompt condi-
tryinterestinusinggenerativeAIforexpressive,interactive
tioning.Whilethepersonaremainsstatic,dynamicvariabil-
NPCdialogues(NVIDIACorporation2023).
ityisintroducedviathemodularmemorysystem.
Efficient deployment of dialogue models remains chal-
lengingduetocomputationalconstraints.Approachessuch
ModularMemoryStore(Runtime-Swappable)
asdistillation,exemplifiedbyDistilBERTandDistilGPT-2,
haveshownhowmodelscanretainsubstantialperformance Toenableunique,context-awareinteractionsforeachNPC
while significantly reducing computational demands (Sanh instance, the system employs two separate vector memory
et al. 2020; DistilBERT 2023). Similarly, the development storesusingChromaDB(ChromaTeam2023):
ofsmallbutperformantopen-sourcelanguagemodels,such • Conversationmemorystorespriorinteractionsbetween
as TinyLlama (Zhang et al. 2024; TinyLlama Team 2023), the player and the NPC. This supports long-term conti-
and Mistral (Jiang et al. 2023), illustrates ongoing efforts nuity,personalfamiliarity,andcontextualgrounding.
to balance efficiency and expressivity. Recent industry ap-
• World knowledge stores structured facts, background
plications also confirm the growing viability of small lan-
information,ornarrativehooksrelevanttotheNPC’sdo-
guage models (SLMs) for on-device game character dia-
mainorrole.
logues(Nnoli2024).
Parameter-efficient fine-tuning methods (Houlsby et al. At runtime, these memory stores are queried indepen-
2019) have enabled further reductions in computational dentlyusingcosinesimilaritybetweentheincomingplayer
overhead. Techniques such as LoRA (Low-Rank Adapta- inputandstoredembeddings(ReimersandGurevych2019).
tion (Hu et al. 2021)) significantly decrease the number The system retrieves the top-k relevant entries from each
of trainable parameters, making fine-tuning on limited re- storeandintegratesthemintotheprompt.Becausethemem-
sourcesfeasiblewithoutsacrificingsubstantialperformance. oryismodularanddecoupledfromthemodel,differentNPC
Our approach uniquely integrates and extends these instances can share the same SLM while maintaining dis-
strandsofresearch.Specifically,wedemonstratehowcom- tincthistoriesandknowledgebases.Thisallows,forexam-
bining small language models, efficient LoRA fine-tuning, ple,multipleinnkeepercharactersacrossthegameworldto
and runtime-swappable modular memory provides a scal- be powered by a single innkeeper model while exhibiting
able and resource-efficient architecture specifically tailored differentcontextualknowledgeandmemory.
forinteractiveNPCdialoguesystems,butpotentiallyappli-
RuntimeDialoguePipeline
cabletootherconversationalscenariosaswell.
The system’s dialogue generation process follows a struc-
SystemOverview:Fixed-Persona, turedpipelineasseeninFigure1:
Modular-MemoryNPCs 1. PlayerInput:Apromptisenteredbytheplayerviathe
command-line interface (or in the game, after integra-
The proposed system enables scalable deployment of non-
tion)
playable characters (NPCs) using small language models
(SLMs)thatarefine-tunedwithfixedpersonasandcoupled 2. Memory Retrieval: The system searches both the con-
withmodularmemorycomponentsatruntime.Thissepara- versationalandworldknowledgememorystoresforthe
tionbetweencharacteridentityanddialoguecontextallows top-kmostrelevantentries.
a single model to support multiple, memory-rich NPC in- 3. Prompt Construction: Retrieved entries are concate-
stances without retraining or modification. At a high level, nated with the player’s input and passed through a for-
each NPC model serves as a persona-anchored dialogue mattinglayer,producingthefinalmodelprompt.

qualitypersonaalignmentwhileminimizingmanualannota-
1. Player Input
tion effort, and avoids reliance on large proprietary models
duringdatageneration.
This pipeline was applied to generate a dataset for a
2. Conversational 2. World Knowledge merchant-personawhichwasusedonallthreebase-models
toenableeasycomparisonofperformance.First,wegener-
atedaninitialcurateddataset(∼115pairs,aftermanualre-
3. Prompt view)tofine-tuneanintermediateNPCmodel,whichsubse-
Construction quentlyproducedalargersyntheticdata(∼564pairs).This
5. Memory was done to explore the impact of different dataset sizes
Update
whenusingLoRAandthedifferentbase-models.Thisledto
4. Response
thecreationof7models,namedafterbase-modelandtrain-
Generation
ingdatasetsize.Thenamingconventioncanbeseenintable
1
Figure1:DiagramdepictingtheRuntimeDialoguePipeline
Name BaseModel DatasetSize
JackS DistilGPT-2 Small
4. Response Generation: The SLM, guided by its fixed JackL DistilGPT-2 Large
persona, and augmented by contextual memory, gener- CasperS TinyLlama-1.1B-Chat Small
atesacharacter-consistentresponse. CasperL TinyLlama-1.1B-Chat Large
5. MemoryUpdate:Thenewdialogueturnisappendedto OliverS Mistral-7B-Instruct Small
theconversationmemoryforfuturereference. OliverL Mistral-7B-Instruct Large
OliverQ Mistral-7B-Instruct Small
Thispipelinesupportsfastinteractionanddynamicmem-
ory use without requiring the model to be reloaded, mod-
Table1:NPC’snamingconventions
ified, or recompiled. The results is a scalable and expres-
sive NPC dialogue system capable of running entirely on
consumer-gradehardware. TheNPCsareassigneddevelopmentnames,withasuffix
annotatingwhethertheyhavebeentrainedonthelarge(”L”,
Fine-tuningpipeline e.g.,OliverL)orsmall(”S”,e.g.,OliverS)dataset.Theonly
exemption from this naming convention is OliverQ, which
To support character-consistent dialogue generation, each wascreatedtoexploretheimpactofquantizationusingAu-
NPC model in the system is fine-tuned to encode a fixed toGTPQ(Frantaretal.2023).
personaalignedwithitsnarrativerole.Thissectionoutlines Theresultofthispipelineisasetoffixed-personaNPCs
thelightweight,multi-stagefine-tuningpipelineusedtocre- that maintain consistent behavioral boundaries and tone,
ateexpressiveNPCsfromopen-sourcesmalllanguagemod- whilebeinglightweightenoughtodeploylocallyalongside
els(SLMs),whilemaintainingcompatibilitywithconsumer- modular memory systems (as described in Section ). The
gradehardware. next section details how these models are evaluated across
The process begins with the creation of a small seed qualityandsystemperformancedimensions.
dataset consisting of 10-20 handcrafted prompt-response
pairs. These examples are written to reflect the intended Results
persona’svoice,tone,anddomain-specificbehavior.Forin-
stance,aninnkeepercharactermayanswerquestionsabout This section presents the detailed results and discussions
local inns and travelers, while avoiding topics unrelated to groupedintothreemaincategories:DialogueQuality,Hard-
theirknowledgescope. ware Efficiency, and Runtime Modularity. Each subsection
includes a description of the evaluation methodology, vi-
ThisseeddatasetisusedtoperformapreliminaryLoRA
sual representation of results, and interpretation. All ex-
fine-tuning of an intermediate model, which serves as a
periments,includingtrainingandevaluation,hasbeencon-
synthetic data generator (Hu et al. 2021). The intermedi-
ducted locally on a Windows 11 Desktop PC with an In-
ate model is prompted with new player inputs to generate
tel Core i7-8700K CPU, 4x8GB 3200MHz RAM, and an
a larger set of synthetic prompt-response pairs, typically
NVIDIARTX2070SuperGPU(8GBVRAM).Thesystem
around 150 entries but can be extended depending on the
used Python 3.12.3 with Torch 2.6.0, Transformers 4.49.0,
desired training depth. These generations are manually re-
ChromaDB0.6.3,andSentenceTransformers3.4.1.
viewed to ensure alignment with the intended persona and
consistencywithin-universeknowledgeconstraints.
DialogueQuality
This dataset is then used to fine-tune the NPCs, but the
process can be repeated to generate even larger synthetic FactualConsistency WeassessedNPCadherencetopre-
dataset.WhenusingLoRA,greatresultshavebeenachieved definedpersonaknowledgeusingtheOpenchat-3.6modelas
using”smaller”datasets,buttheapproachcanberepeatedto anautomatedjudge(Wangetal.2024),prompt-engineered
create larger synthetic datasets, which may be used to per- via an instruction template to evaluate factual correctness
formfullfine-tuning.This”staged”approachenableshigh- andappropriaterefusalbehavior(questionsoutsidedefined

knowledge scope) across 100 responses per NPC variant.
Figure 2 show that OliverS significantly outperformed all
JackS JackL CasperS CasperL OliverS OliverL Oliver Q
Model
)%(
001
fo
tuo
tcerroC
Correct Factual Responses by NPC Model (%)
16.0%
9.0%
55.0%
39.0%
93.0%
70.0%
84.0% 80
60
40
20
0
Figure2:Factual accuracyofNPCresponsesacross differ-
entmodelvariants.
othervariants(93%),andmodelswithsmallerdatasetscon-
sistently performing better compared to the same models
with larger datasets (JackS 16% vs JackL 9% and CasperS
55%vsCasperL39%),suggestingpossibledatasetquality
issuesoroverfitting.
Context Retention (Conversational Memory) We eval-
uated the NPC’s ability to recall previously introduced in-
formation across multiple dialogue turns. In 30 multi-turn
interactions, NPCs were tested on their ability to reference
keywordsintroducedearlier,suchastheplayer’sname.
JackS JackL CasperS CasperL OliverS OliverL Oliver Q
Model
03
fo
tuo
tcerroC
Context Retention: Correct Responses by Model (%)
6.7%
10.0%
63.3%
13.3%
100%
60.0%
73.3%
WWoorrlldd KKnnoowwlleeddggee:: CCoorrrreecctt RReessppoonnsseess bbyy MMooddeell ((%%))
JackS JackL CasperS CasperL OliverS OliverL
Oliver
Q
30
25
20
15
10
5
0
Figure3:ContextretentionperformanceofeachNPCvari-
ant,measuredbythepercentageofcorrectkeywordrecalls
inmulti-turnconversations.
OliverS (100 %) demonstrated perfect retention (Fig. 3),
clearlyoutperformingothermodels,withCasperS(63.3%)
showing moderate but surprisingly good results. Jack vari-
antsarenotablylaggingbehind(JackS6.7%,JackL10%).
World Knowledge Retrieval We measured NPC accu-
racy in retrieving specific information from their world
knowledgedatabasebysystematicallyexecuting30queries
per variant, each designed to trigger retrieval of distinct
knowledge entries. Oliver variants (OliverS 100 %, Oliv-
erL96.7%,OliverQ100%)excelledwithperfectandnear-
perfectretrieval(Fig.4),whileCasperS(76.7%)performed
robustly, but CasperL and Jack variants showed significant
shortcomings.
)%(
03
fo
tuo
tcerroC
30
25
20
15
10
5
0
Model
20.0%
10.0%
76.7%
3.3%
100.0%
96.7%
100.0%
Figure 4: Accuracy of world knowledge retrieval by NPC
model, illustrating the percentage of correctly retrieved en-
triesfrommemorydatabases.
Fluency (Grammar and Style) We evaluated linguistic
fluencybyanalyzinggrammatical,spelling,andstylisticer-
rors in 30 NPC-generated responses per variant using the
LanguageToolgrammarchecker(LanguageTool2025).Re-
sults are reported as average errors per response. OliverS
JackS JackL CasperS CasperL OliverS OliverL
Oliver
Q
esnopseR
rep
srorrE
.gvA
Average Grammar/Style Errors per Response (Lower = Better)
2.23 2.0
1.5
0.97
1.0
0.5
0.03 0.03 0.00 0.03 0.03
0.0
Figure 5: Average grammatical and stylistic errors per re-
sponse produced by NPC models, as measured by Lan-
guageTool.Lowervaluesindicatebetterfluency.
generatedflawlessresponses(Fig.5).Jackvariantsshowed
significantgrammaticalissuesreflectinglowermodelcom-
plexity,whileothermodelsremainednearlyerror-free.
HardwareEfficiencyMetrics
GPUMemoryUsage(VRAM) WemeasuredmeanGPU
VRAMusageduringinference,assessingsuitabilityforlo-
cal deployment. Figure 6 shows Jack variants had mini-
mal GPU requirements (∼130MB), ideal for low-resource
setups. Casper (∼807MB) balanced efficiency and perfor-
mance, while Oliver variants (∼4.2GB) remained feasible
onhigher-endconsumerGPUs.
ModelDiskFootprint Wemeasureddiskstoragerequire-
mentstoevaluatedeploymentpracticality.Figure7demon-
strates that quantization significantly reduced OliverS foot-
print (OliverS 15.93GB, OliverQ 3,9GB). Jack (∼0.4GB)
and CasperS (2.73GB) variants also offered compact sizes,
suitableforconstrainedenvironments.

GPU Memory Usage (MB)
)BM(
egasU
yromeM
UPG
4000
3000
2000
1000
0 JackS JackL CasperS CasperL OliverS OliverL
Oliver
Q
129.8097 129.8097
807.1342 807.1333
4206.8790 4206.8790 4330.2282
Model
Figure 6: Average GPU memory consumption (VRAM in
MB)duringinferenceacrossdifferentNPCmodelvariants.
Model Disk Footprint by Component
)BG(
eziS
ksiD
23.73
20
15.93
15
10
7.01
5 3.90 2.73
0.46 0.35
0
JackS JackL CasperS CasperL OliverS OliverL Oliver Q
Model
Figure7:Diskstoragefootprint(GB)foreachNPCmodel.
Latency (Total Response Generation Time) Latency
was measured from input submission to full response de-
livery,crucialforreal-timeinteractions.
JackS JackL CasperS CasperL OliverS OliverL
Oliver
Q
Model
)s(
ycnetaL
suitabilityoftheNPCs.
JackS JackL CasperS CasperL OliverS OliverL
Oliver
Q
Mean Latency with Standard Deviation (s)
35
34.58
30
25
20
15
10 6.67
5.49
5 1.91 1.52
0.89 0.78
0
Figure 8: Mean latency (seconds) for response generation
acrossmodels.
Figure 8 indicates Jack (∼0.8s) and Casper (∼1.7-1.9s)
variants had low latency, suitable for interactive scenarios.
OliverS’smoderatelatency(5.49s)remainsacceptablewith
latency-masking methods (on-screen text rendering, Text-
To-Speech),whileOliverQ(34.58s)facedsignificantlatency
fromquantizationoverhead.
Time-To-First-Token (TTFT) Time-To-First-Token
measures initial responsiveness from query to output
generationstart.Animportantmetrictodeterminereal-time
)s(
nekoT
tsriF
ot
emiT
naeM
Time To First Token Mean with Standard Deviation
0.8 0.7022
0.6
0.4
0.1145 0.1088
0.2 0.0750 0.0751
0.0157 0.0164
0.0
Figure9:Meantime-to-first-token(TTFTinseconds)indi-
catinginitialmodelresponsivenessafterquerysubmission.
Figure 9 shows all models except OliverQ had excel-
lentinitialresponsiveness(<0.2s).OliverQ’snotablyhigher
TTFT(0.7022s)limitsitsimmediateresponsivenessinreal-
timesettings.
RuntimeModularityMetrics
Average Memory Swap Time We evaluated swap times
betweensmall(100entries),medium(500),andlarge(1000)
NPC memory databases, executing 50 swaps per combi-
nation. Test entries were standardized filler texts used ex-
clusively for performance benchmarks. Figure 10 shows
Average Swap Time per Memory Swap (with Standard Deviation)
Large Large Medium Medium Small Small
Medium Small Large Small Large Medium
)s(
emiT
pawS
0.040
0.030
0.020
0.010
0.000
Figure10:Averagememorydatabaseswaptime(seconds).
extremely fast memory swap times (<0.03s), enabling
seamlessandimperceptibleNPCinstanceswitchingduring
gameplay.
Memory Retrieval Time Memory retrieval latency was
evaluated by querying each database size (Small, Medium,
Large)50timesforbothConversationalandWorldKnowl-
edgeentries.Figure11highlightsverylowretrievallatency
(<0.042s),evenforlargedatabases,confirmingsystemscal-
abilityandsuitabilityforreal-timeplayerinteractions.
Memory Database Disk Footprint Disk footprints of
memory databases were assessed across different entry
counts to determine scalability. Figure 12 shows minimal
footprintincreasesfromsmall(3.92MB)tolarge(8.98MB),
underscoringthemodularmemorysystem’spracticalityand
scalability,enablingextensiveandmemory-richNPCpopu-
lationswithminimalresourceoverhead.

Large Medium Small
)s(
emiT
laveirteR
Retrieval Time by Memory Database (with Sandard deviation)
0.07
0.06
0.05
0.04
0.03
0.02
0.01
0.00
Figure11:Averageretrievaltime(seconds)forentriesfrom
conversationalhistoryandworldknowledgedatabases.
Disk Footprint of Memory Systems
)BM(
eziS
ksiD
ing the effectiveness of quantization methods such as Au-
toGTPQforstorageefficiency.However,OliverQexhibited
significantlyincreasedlatency(34.58secondsmeanslatency
comparedto5.49secondsforOliverS),alongsidemoderate
degradation in factual accuracy and context retention. This
indicatesthatwhilequantizationeffectivelyreducesstorage
demands, it introduces non-trivial computational overhead,
particularlynoticeableonlimitedGPUhardware.
Aconsistenttrendemergedregardingdatasetsize:smaller
datasets(denotedbythesuffix”S”)generallyoutperformed
their larger counterparts (”L”) across factuality, context re-
tention,worldknowledgeretrieval,andfluency.Thiscoun-
terintuitiveresultlikelyarisesfromdecreaseddatasetqual-
ity or coherence in the larger synthetic dataset, introduc-
ing potential noise or conflicting examples. Additionally,
larger datasets might lead to overfitting, negatively impact-
10 8.98 MB ing generalization performance (Brown et al. 2020). Con-
sequently,ourfindingsstronglysuggestprioritizingsmaller,
8
high-quality datasets for NPC model fine-tuning, when us-
6.12 MB
6 ingLow-RankAdaptation(LoRA).
3.92 MB
4
ModularityandRuntimeMemorySwapping
2
A key contribution of this work is the demonstrated practi-
0 calfeasibilityofamodulararchitectureemployingruntime-
Small Medium Large swappable memory stores, allowing multiple distinct NPC
(100 Entries) (500 Entries) (1000 Entries)
interactions from a single fine-tuned base model. Our em-
Figure12:Diskfootprint(MB)forsmall,medium,andlarge piricalvalidationofthisapproachprovidedcompellingevi-
memorydatabases. denceforitspracticalviability:
Firstly,memoryswaptimeswereexceptionallylow,rang-
ing from 0.012 to 0.027 seconds across different scenarios
Figure 12 illustrates minimal footprint growth (small (small, medium, and large databases). These negligible la-
3.92MB,large8.98MB),highlightingthepracticalityandef- tencies confirm that memory swapping occurs practically
ficiencyofscalablemodularmemorystorage. seamlesslyfromtheuser’sperspective,effectivelysupport-
ing multiple NPC instances without perceptible gameplay
Note on RAM Usage during Swapping Due to Chro-
disruptions. Secondly, memory retrieval times remained
maDB’s lazy loading and memory-mapped storage ap-
consistently fast, even with the largest database size (1000
proach,explicitRAMusagemeasurementsduringmemory
entries), yielding retrieval latencies below 0.042 seconds.
swapwereimpractical.DataloadingintoRAMoccursonly
This highlights the inherent scalability and responsiveness
upon query access, maintaining memory efficiency. Conse-
of the modular memory system, reinforcing its suitabil-
quently,thisdesignminimizesRAMusageoverheadduring
ity for real-time gameplay contexts. Importantly, memory
swaps,confirmingthepracticalityandefficiencyofourmod-
databases showed minimal increases in disk footprint from
ularruntimememoryarchitecture.
small (3.92MB) to large (8.98MB), suggesting trivial stor-
Discussion age overhead and strong scalability potential. This mini-
malincreasemakesourapproachparticularlywell-suitedfor
SummaryandInterpretationofKeyResults gamesrequiringextensiveNPCpopulations,eachwiththeir
Ourevaluationdemonstratesseveralclearinsightsregarding owndistinctmemorycontexts.ExplicitRAMusageduring
theeffectivenessofsmalllanguagemodels(SLMs)inpow- memoryswapswasnotmeasurableduetoChromaDB’sim-
eringmodularNPCdialoguesystems.Mostnotably,OliverS plementationoflazyloadingandmemory-mappedstorage.
consistently achieved superior performance across all dia- This means data from a memory store is only loaded into
loguequalitymetrics,includingfactuality(93%),contextre- RAMuponactualqueryaccess,providingsignificantpracti-
tention(100%),worldknowledgeretrieval(100%),andlin- caladvantages,maintainingRAMefficiencywithoutunnec-
guisticfluency(0errors).ThissuggeststhattheMistral-7B- essaryoverhead.
Instructmodel,whentrainedonacarefullycuratedsmaller Taken together, these results decisively confirm our hy-
dataset,providesarobustbalanceofexpressivityandaccu- pothesis: runtime memory modularity is not only feasi-
racy, making it highly suitable for dialogue-rich, narrative- ble but highly practical. A single fine-tuned NPC model
focusedinteractions. can effectively power multiple unique NPC instances, each
Thequantizedvariant,OliverQ,showedasubstantiallyre- enriched by distinct, memory-driven interactions, enabling
duceddiskfootprint(from15.93GBto3.9GB),highlight- context-richgameplayexperiences.

Trade-offsandConsiderationsforModelSelection The practicality of memory modularity further enhances
our system’s deployment appeal. Extremely low memory
Balancing dialogue quality and hardware performance is
swap times (below 0.03 seconds) facilitate seamless NPC
central to practical NPC deployment decisions. OliverS,
transitions, enabling game designers to efficiently populate
based on the Mistral-7B-Instruct model fine-tuned with a
extensivegameworldswithdiverse,memory-richcharacters
smaller dataset, delivers exceptional dialogue quality suit-
atminimalstorageandcomputationalcost.
able for high-importance NPCs demanding nuanced and
Finally,whileourapproachisprimarilymotivatedbyap-
contextually accurate interactions. However, its relatively
plications within computer games, the modular, persona-
higherlatency(5.49seconds)suggestpracticaldeployment
driven memory architecture has significant potential for
strategies involving latency masking through incremental
broaderdeploymentinotherdomains.Applicationssuchas
text rendering or real-time text-to-speech (TTS) methods
virtual assistants, customer support bots, interactive educa-
should be employed (as is the norm for LLMs) (Ren et al.
tionalsystems,oranyscenariorequiringmultipleexpressive
2022).ThelowTime-To-First-Token(0.1145seconds)sup-
conversationalagentswithdistinctlong-termmemorystores
ports such approaches effectively, enhancing perceived re-
couldreadilybenefitfromourproposedapproach.
sponsivenessforreal-timegameplayscenarios.
CasperS (TinyLlama) emerges as a balanced alternative
combining good dialogue quality metrics (e.g., factuality Conclusion
55%, context retention 63.3%, world knowledge retrieval
This paper introduced a novel modular dialogue architec-
76.7%) with reduced latency (1.91 seconds). Its moderate
ture for non-playable characters (NPCs) using LoRA fine-
GPUmemoryusage(∼807MB)makesithighlysuitablefor
tunedSmallLanguageModels(SLMs)pairedwithruntime-
broader NPC deployments with numerous responsive char-
swappablememorymodules.Ourprimarycontributionlies
acters without sacrificing substantial dialogue quality. Fur-
in demonstrating that a single fine-tuned base model can
therexperimentsmaysubstantiateCasperS’sresults.
efficiently power multiple distinct NPC instances, each en-
TheJackmodels(DistilGPT-2),despitenotablylowerdi-
richedbyuniqueconversationalandworld-knowledgemem-
alogue quality (factuality <20%, context retention <11%),
ories. This approach significantly reduces computational
offer extremely low latency (∼0.8 seconds) and minimal
andstorageoverhead,enablingexpressiveandscalablesys-
GPU usage (∼130 MB). Such traits position Jack models
tems suitable for real-time deployment in modern games.
as viable candidates for simple NPCs, but not for dialogue
WhileprimarilydesignedforNPCdialogueingames,thear-
relatedscenarios.
chitecture’s modularity and efficiency also suggest promis-
The quantized OliverQ model presents complex trade-
ing applicability to other domains requiring memory-rich
offs,significantlyreducingdiskfootprintbutsufferingsub-
conversationalagents.
stantiallatencypenaltiesandmoderatequalitydegradation.
Throughcomprehensive evaluations,we showedthat the
Its practical application thus hinges on scenarios prioritiz-
Mistral-7B-Instruct model fine-tuned with a carefully cu-
ing storage saving and deploying more capable hardware
rated smaller synthetic dataset (OliverS) consistently pro-
setups capable of managing increased latency. However, in
vided superior dialogue quality, including near-perfect fac-
anyrealisticscenario;Asystemcapableofrunninga4GB+
tual accuracy, context retention, and linguistic fluency. Al-
VRAMmodelwillnothaveanyissueswiththe<16GBdisk
thoughquantizationdramaticallyreducedthediskfootprint,
spacerequiredtorunOliverS,whichoutperformsOliverQin
it introduced substantial latency penalties, highlighting im-
everyothermetricexceptdiskfootprint.
portant trade-offs. Additionally, our results highlighted the
viability of memory modularity, demonstrating negligible
PracticalDeploymentImplications
memoryswaptimesandexcellentretrievalscalability.
Our evaluation confirms the practicality of local deploy- Inpracticalterms,ourarchitecturesupportsseamlessreal-
ment.GPUmemoryrequirements(∼4.2GBforOlivervari- time interactions through effective latency-masking tech-
ants) are compatible with standard consumer-grade GPUs, niquessuchasincrementaltextrenderingorreal-timetext-
makingourNPCmodelsaccessibleformostgamingsetups. to-speech.Themodularmemoryapproachensuresminimal
Latencyanalysishighlightsimportantusabilityconsider- overhead,makingithighlysuitableforgamesfeaturingex-
ations. OliverS’s latency of 5.49 seconds is initially high tensiveanddiverseNPCpopulations,allpoweredbyasingle
butoffsetbyanimpressivelylowTTFTof0.1145seconds. fine-tunedmodel.
By employing on-screen text rendering or TTS solutions, Ourworkalsoidentifiesseveralimportantlimitationsthat
thislatencycanbeeffectivelymasked,significantlyimprov- suggestcleardirectionsforfutureresearch:
ing perceived responsiveness and ensuring real-time via- • Since dataset quality emerged as a critical factor for
bility. CasperS provides an excellent compromise, with la- NPC performance, future work should explore improv-
tencyunder2secondssuitableforwide-rangingNPCinter- ingdatasetquality/refinementmethods.Perhapsthrough
actionswithoutrequiringadditionalmaskingstrategies.For iterativefeedbackloops(Ouyangetal.2022).
CasperS, further experimentation might improve dialogue • Latency penalties introduced by quantization require
relatedevaluationmetrics.Jackmodelsuselesshardwarere- more exploration of alternative methods or optimized
sources,butthiscomesatasteeppenaltyindialoguerelated quantization techniques (Dettmers et al. 2022; Stock
metrics, and is therefore not recommended without careful etal.2020).
considerationofitsuse-case. • Current system uses static personas, future work could

exploreruntimepersonaadjustments(Seeetal.2019;Di- MistralAI.2023. Mistral-7B-v0.1. https://huggingface.co/
nanetal.2019). mistralai/Mistral-7B-v0.1. Accessed:19-03-2025.
• Future work should explore real-world player feedback Nnoli,I.2024. DeploytheFirstOn-DeviceSmallLanguage
studies, to see if SLM powered NPCs could enhance Model for Improved Game Character Roleplay. Accessed:
playerexperience(Rolleretal.2020;Jietal.2023). 19-03-2025.
NVIDIA Corporation. 2023. NVIDIA ACE for Games:
References
Generative AI NPCs. https://www.nvidia.com/en-
Brown,T.B.;Mann,B.;Ryder,N.;Subbiah,M.;Kaplan,J.; us/geforce/news/nvidia-ace-for-games-generative-ai-npcs/.
Dhariwal,P.;Neelakantan,A.;Shyam,P.;Sastry,G.;Askell, Accessed:2025-03-18.
A.; Agarwal, S.; Herbert-Voss, A.; Krueger, G.; Henighan, Ouyang, L.; Wu, J.; Jiang, X.; Almeida, D.; Wainwright,
T.; Child, R.; Ramesh, A.; Ziegler, D. M.; Wu, J.; Winter, C.L.;Mishkin,P.;Zhang,C.;Agarwal,S.;Slama,K.;Ray,
C.; Hesse, C.; Chen, M.; Sigler, E.; Litwin, M.; Gray, S.; A.; Schulman, J.; Hilton, J.; Kelton, F.; Miller, L.; Simens,
Chess, B.; Clark, J.; Berner, C.; McCandlish, S.; Radford, M.; Askell, A.; Welinder, P.; Christiano, P.; Leike, J.; and
A.; Sutskever, I.; and Amodei, D. 2020. Language Models Lowe,R.2022. Traininglanguagemodelstofollowinstruc-
areFew-ShotLearners. arXiv:2005.14165. tionswithhumanfeedback. arXiv:2203.02155.
Chroma Team. 2023. Chroma: The Open-Source Embed- Parvini, S. 2024. Can AI make video games more immer-
ding Database. https://www.trychroma.com. Accessed: sive? Some studios turn to AI-fueled NPCs for more inter-
2024-03-25. action. Accessed:19-03-2025.
Dettmers, T.; Lewis, M.; Belkada, Y.; and Zettlemoyer, L. Reimers, N.; and Gurevych, I. 2019. Sentence-BERT:
2022. LLM.int8(): 8-bit Matrix Multiplication for Trans- Sentence Embeddings using Siamese BERT-Networks.
formersatScale. arXivpreprintarXiv:2208.07339. arXiv:1908.10084.
Dinan, E.; Roller, S.; Shuster, K.; Fan, A.; Auli, M.; and Ren, Y.; Hu, C.; Tan, X.; Qin, T.; Zhao, S.; Zhao, Z.; and
Weston,J.2019.WizardofWikipedia:Knowledge-Powered Liu,T.-Y.2022. FastSpeech2:FastandHigh-QualityEnd-
Conversationalagents. arXiv:1811.01241. to-EndTexttoSpeech. arXiv:2006.04558.
Roller,S.;Dinan,E.;Goyal,N.;Ju,D.;Williamson,M.;Liu,
DistilBERT. 2023. HuggingFace Page for DistilGPT2.
Y.;Xu,J.;Ott,M.;Shuster,K.;Smith,E.M.;Boureau,Y.-L.;
https://huggingface.co/distilbert/distilgpt2. Accessed: 19-
andWeston,J.2020. Recipesforbuildinganopen-domain
03-2025.
chatbot. arXiv:2004.13637.
Frantar,E.;Ashkboos,S.;Hoefler,T.;andAlistarh,D.2023.
Sanh,V.;Debut,L.;Chaumond,J.;andWolf,T.2020. Dis-
GPTQ:AccuratePost-TrainingQuantizationforGenerative
tilBERT,adistilledversionofBERT:smaller,faster,cheaper
Pre-trainedTransformers. arXiv:2210.17323.
andlighter. arXiv:1910.01108.
Gao, Q. C.; and Emami, A. 2023. The Turing Quest:
Schlu¨nder,B.;andKlabunde,R.2013.GreetingsGeneration
CanTransformersMakeGoodNPCs? InPadmakumar,V.;
in Video Role Playing Games. In Proceedings of the 14th
Vallejo,G.;andFu,Y.,eds.,Proceedingsofthe61stAnnual
EuropeanWorkshoponNaturalLanguageGeneration,167–
Meeting of the Association for Computational Linguistics
171.AssociationforComputationalLinguistics.
(Volume 4: Student Research Workshop), 93–103. Toronto,
See, A.; Roller, S.; Kiela, D.; and Weston, J. 2019. What
Canada:AssociationforComputationalLinguistics.
makesagoodconversation?Howcontrollableattributesaf-
Houlsby, N.; Giurgiu, A.; Jastrzebski, S.; Morrone, B.;
fecthumanjudgments. arXiv:1902.08654.
deLaroussilhe,Q.;Gesmundo,A.;Attariyan,M.;andGelly,
Stock,P.;Joulin,A.;Gribonval,R.;Graham,B.;andJe´gou,
S. 2019. Parameter-Efficient Transfer Learning for NLP.
H.2020. AndtheBitGoesDown:RevisitingtheQuantiza-
arXiv:1902.00751.
tionofNeuralNetworks. arXiv:1907.05686.
Hu,E.J.;Shen,Y.;Wallis,P.;Allen-Zhu,Z.;Li,Y.;Wang,
TinyLlamaTeam.2023. TinyLlama-1.1B-Chat-v1.0. https:
S.; and Chen, W. 2021. LoRA: Low-Rank Adaptation of
//huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0.
LargeLanguageModels. arXiv:2106.09685.
Accessed:19-03-2025.
Ji,Z.;Lee,N.;Frieske,R.;Yu,T.;Su,D.;Xu,Y.;Ishii,E.;
Wang,G.;Cheng,S.;Zhan,X.;Li,X.;Song,S.;andLiu,Y.
Bang,Y.J.;Madotto,A.;andFung,P.2023. SurveyofHal-
2024. OpenChat:AdvancingOpen-sourceLanguageMod-
lucinationinNaturalLanguageGeneration. ACMComput-
elswithMixed-QualityData. arXiv:2309.11235.
ingSurveys,55(12):1–38.
Zhang, P.; Zeng, G.; Wang, T.; and Lu, W. 2024.
Jiang, A. Q.; Sablayrolles, A.; Mensch, A.; Bamford, C.;
TinyLlama: An Open-Source Small Language Model.
Chaplot,D.S.;delasCasas,D.;Bressand,F.;Lengyel,G.;
arXiv:2401.02385.
Lample, G.; Saulnier, L.; Lavaud, L. R.; Lachaux, M.-A.;
Stock,P.;Scao,T.L.;Lavril,T.;Wang,T.;Lacroix,T.;and
Sayed,W.E.2023. Mistral7B. arXiv:2310.06825.
LanguageTool. 2025. LanguageTool: Open-source gram-
mar,style,andspellchecker. https://languagetool.org/. Ac-
cessed:2025-05-24.
