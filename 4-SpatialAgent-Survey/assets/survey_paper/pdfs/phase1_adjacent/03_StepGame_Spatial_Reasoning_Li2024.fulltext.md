Title: 03_StepGame_Spatial_Reasoning_Li2024

Source PDF: /Users/mac/Documents/6-Research/4-SpatialAgent-Survey/assets/survey_paper/pdfs/phase1_adjacent/03_StepGame_Spatial_Reasoning_Li2024.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T02:55:06+00:00
- page_count: 12
- status: ok
- text_char_count: 52036

Metadata:
- author: unknown
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- none

Markdown Content:

Advancing Spatial Reasoning in Large Language Models: An In-Depth Evaluation
and Enhancement Using the StepGame Benchmark
FangjunLi1,DavidC.Hogg1,AnthonyG.Cohn1,2
1SchoolofComputing,UniversityofLeeds,Leeds,UK
2AlanTuringInstitute,UK
scfli@leeds.ac.uk,d.c.hogg@leeds.ac.uk,a.g.cohn@leeds.ac.uk
Abstract ities.However,despitetheirimpressiveabilities,LLMsen-
counter challenges in many logical reasoning aspects cru-
Artificial intelligence (AI) has made remarkable progress
cial for human communication, particularly spatial reason-
across various domains, with large language models like
ing(Bangetal.2023;CohnandHernandez-Orallo2023).
ChatGPT gaining substantial attention for their human-like
OneapproachtoevaluatingspatialreasoninginanAIsys-
text-generationcapabilities.Despitetheseachievements,spa-
temistousesyntheticbenchmarkssuchasStepGame(Shi,
tialreasoningremainsasignificantchallengeforthesemod-
els. Benchmarks like StepGame evaluate AI spatial reason- Zhang,andLipani2022)andSpartQA(MirzaeeandRajaby
ing,whereChatGPThasshownunsatisfactoryperformance. 2021).Unfortunately,modelslikeChatGPThaveshownun-
However, the presence of template errors in the benchmark satisfactory performance on these benchmarks. Improving
has an impact on the evaluation results. Thus there is po- thespatialreasoningcapabilitiesofLLMsremainsaprimary
tential for ChatGPT to perform better if these template er- focustoenhancetheiroverallperformanceandunderstand-
rorsareaddressed,leadingtomoreaccurateassessmentsof ingofcomplexenvironments.
itsspatialreasoningcapabilities.Inthisstudy,werefinethe
Whilst examining the StepGame benchmark we discov-
StepGamebenchmark,providingamoreaccuratedatasetfor
ered that it contains template errors that distort model per-
model evaluation. We analyze GPT’s spatial reasoning per-
formance evaluations. These errors were previously over-
formanceontherectifiedbenchmark,identifyingproficiency
looked,leadingtostudiesconductedonaflawedbenchmark,
inmappingnaturallanguagetexttospatialrelationsbutlimi-
tationsinmulti-hopreasoning.Weprovideaflawlesssolution inaccurately assessing the capabilities of the LLMs (Bang
tothebenchmarkbycombiningtemplate-to-relationmapping et al. 2023; Yang, Ishay, and Lee 2023). To rectify this is-
with logic-based reasoning. This combination demonstrates sue, we present a more accurate version of the StepGame
proficiencyinperformingqualitativereasoningonStepGame dataset for model evaluation, ensuring precise assessments
withoutencounteringanyerrors.Wethenaddressthelimita- ofthemodels’truecapabilitiesandlimitations1.
tionsofGPTmodelsinspatialreasoning.WedeployChain- Wethenconductedevaluationtestsontherectifiedbench-
of-thoughtandTree-of-thoughtspromptingstrategies,offer-
mark across various test subsets, few-shot sets, and mod-
ing insights into GPT’s “cognitive process”, and achieving
els.WeobservedthatlargerGPTmodelsdemonstrateprofi-
remarkableimprovementsinaccuracy.Ourinvestigationnot
ciencyinmappingnaturallanguagetexttospatialrelations.
onlyshedslightonmodeldeficienciesbutalsoproposesen-
However,theystrugglewithmulti-hopspatialreasoning.
hancements,contributingtotheadvancementofAIwithmore
robustspatialreasoningcapabilities. Ourgoalisnotmerelytocritique,butalsotoproposepo-
tentialimprovements.Tothisend,weprovideaflawlessso-
lutiontothebenchmark,andexploredifferentapproachesto
Introduction
enhancethespatialreasoningabilityofLLMs.
Spatialreasoning,theabilitytounderstandandnavigatere- Thesolutionweproposeforthebenchmarkentailscom-
lationshipsinphysicalspace,isafundamentalaspectofhu- bining template-based sentence-to-relation mapping with
mancognitionthatsignificantlyinfluencesinteractionswith logic-based spatial reasoning. The logical reasoner used in
the environment. Enhancing spatial reasoning in AI mod- this approach comes from (Yang, Ishay, and Lee 2023),
els has the potential to enrich their comprehension of their where they integrated GPT-3 for the task. GPT-3 was em-
surroundings and response to user interactions, leading to ployedtoparsespatialdescriptionsintosymbolicspatialre-
more advanced and immersive user experiences (Alomari lation representations, which were then passed to the log-
et al. 2022). In recent years, AI has revolutionized numer- ical program for spatial reasoning. This fusion resulted in
ous domains, from healthcare to finance to entertainment. significant improvement in StepGame, achieving state-of-
Notably,OpenAI’slargelanguagemodels(LLMs),suchas the-art (SOTA) but not perfect results: around 90% accu-
ChatGPT and GPT-4 (OpenAI 2023), have gained signifi-
cant attention for their human-like text generation capabil- 1The data associated with this paper are openly available
from the University of Leeds Data Repository. https://doi.org/10.
Copyright©2024,AssociationfortheAdvancementofArtificial 5518/1468. All code is available at https://github.com/Fangjun-
Intelligence(www.aaai.org).Allrightsreserved. Li/SpatialLM-StepGame.
4202
naJ
8
]IA.sc[
1v19930.1042:viXra

racyforlowerhopsand88.3%accuracyfor10-hopreason- in AI development, pushing the boundaries of what LLMs
ing.Theyattributed10.7%faultstodata-relatedissues.With canachieve.Ultimately,ourinvestigationcanpavetheway
our aforementioned work on rectifying the benchmark, We forthedevelopmentofadvanced,intuitive,anduser-friendly
take a step further to delve into the two components, an- AIsystemswithrobustspatialreasoningcapabilities.
alyzing the performance of each on our filtered version of
thedataset.Remarkably,weachieved100%accuracyforal- RelatedWork
most all hops, with only 2 errors among 1000 test exam- Thefieldofspatialreasoninginlanguagewithartificialin-
ples, which were due to GPT-3’s incorrect semantic pars- telligence has evolved through sustained efforts over time,
ing. Building on this, we replaced the GPT-3 parser with withsignificantadvancementsachievedthroughbothtradi-
our sentence-to-relation mapping method and combined it tionalmethodsandmodernLLMs.
withtheASPreasoner,showcasingproficiencyinperform- Earlystridesinspatialreasoninginlanguageweremarked
ing qualitative reasoning without encountering any errors, bythedevelopmentofformalstructurestorepresentspatial
thus demonstrating a method to achieve a perfect score on relationships.(Kordjamshidi,Moens,andvanOtterlo2010)
thecorrectedbenchmark. proposed a spatial ontology to formalize the representation
Neither our solution or the SOTA utilize LLMs for the of spatial relations. This work laid the groundwork for the
actual spatial reasoning functionality. Thus, we proceed to subsequent introduction of text-based spatial role labeling
enhance GPT’s capabilities as a native spatial reasoner. To (Kordjamshidi, Van Otterlo, and Moens 2011), which aims
achievethis,weemployChain-of-Thoughts(CoT)andTree- toconverttextintoformalspatialrepresentations.
of-Thoughts(ToT)promptingstrategies. Thencomessynthetictasksdesignedtoevaluatethetext
CoT (Wei et al. 2022) incorporates a sequence of inter- understandingandspatialreasoningcapabilitiesoflearning
mediatereasoningstepstofacilitateproblem-solving.How- algorithms. The positional reasoning task (Task 17) in the
ever, when applied to StepGame, previous studies (Yang, bAbIdataset(Westonetal.2015)isforspatialreasoningand
Ishay, and Lee 2023) have shown that CoT does not con- requiresmodelstoreasonusingoneortwosentences,which
sistently improve performance and may even reduce accu- makesthistaskcomparativelysimple.(Shi,Zhang,andLi-
racy in complex k-hop reasoning tasks. This observation is pani 2022) advanced this field by creating the StepGame
attributed to the higher probability of errors occurring in benchmark to evaluate multi-hop spatial reasoning in text,
lengthyCoTprocesses.Ontheotherhand,researchonother with richer variety in spatial relation descriptions. Both of
tasks (Zhou et al. 2022; Creswell, Shanahan, and Higgins thesedatasetsemphasizedirectionalspatialrelations(Cohn
2022)hasdemonstratedthatbreakingdowncomplexprob- and Hazarika 2001; Skiadopoulos and Koubarakis 2001;
lems into simpler subproblems and solving them sequen- Cohn and Renz 2008; Chen et al. 2015). Three spatial QA
tially can be beneficial. Given the ambiguity in the decom- datasets: SpartQA(Mirzaee and Rajaby 2021), SPARTUN,
positionof“thoughts”2withinCoT,weproposerefiningthe
andRESQ(MirzaeeandKordjamshidi2022)expandedthe
CoTprompttoempowerlanguagemodelstoperformbetter resource landscape by encompassing wider-ranging spatial
inspatialreasoningtasks. languageexpressions,posingchallengesfortraditionallog-
On the other hand, (Yao et al. 2023) introduced ToT, a icalprogramming,andareimportantbenchmarksforevalu-
framework enabling LLMs to explore multiple reasoning atingLLMs’spatialreasoningcapabilities.
paths,andtheydemonstrateditseffectivenessinimproving Concurrently, the advent of LLMs such as OpenAI’s
problem-solving capabilities across tasks like the game of ChatGPT has opened up fresh pathways for spatial rea-
24, creative writing, and mini crosswords. In our work, we soning.Thesemodels,leveragingtransformerarchitectures,
customizetheToTapproachforobject-linkingchainbuild- can generate human-like text and handle complex linguis-
ing, a crucial subproblem in addressing spatial reasoning tic structures. However, while these models are indeed im-
benchmarks. pressive,theircapabilitiesinspatialreasoningareyettobe
Our customized CoT method showcases its advantages fullyexploredandexploited.Onerecentapproachtoassess
more prominently in larger models such as GPT-4 and thesecapabilitieswastakenby(Bangetal.2023),whoput
Davinci, maintaining accuracy even as the tasks become ChatGPTtothetestusingSpartQAandStepGame.Despite
morecomplex.OurToTapproachdemonstratesitsstrengths the generally advanced capabilities of ChatGPT, the model
onthethreeGPTmodels:onthelargestmodel,GPT-4,we showedshortcomingsinthesetasks,signalinganeedforfur-
areabletomaintainanaccuracyofaround90%evenasthe therenhancementsintherealmofspatialreasoning.
tasks become more complex. On Davinci, the accuracy is A promising technique known as ‘prompt engineering’
maintained at around 50%, while Turbo achieves a lower (Bommasanietal.2021)hasbeenmakingitsmarkrecently.
levelofaccuracyataround30%. This approach involves crafting specific prompts to guide
By identifying current deficiencies and proposing en- the responses of the models, leading to outputs that are
hancements, we aim to contribute to the ongoing discourse more contextually apt and insightful. This method demon-
strates significant potential in enhancing the capabilities of
2Inthispaperweusetheword‘thoughts’inthesamewayas
LLMs like ChatGPT in various domains (Li, Hogg, and
isnowbeingusedintheliteratureonCoTandToT,whilstnoting
Cohn 2022), including the challenging area of logical rea-
thatthesearenotthoughtsinthehumansensebutrathergenerated
coherentunitsoftext,servingasintermediatestepsinaproblem soning (Wang et al. 2023). For instance, when faced with
solvingsetting,andwithoutwishingtoascribeananthropomorphic multi-stepreasoningtasks,amethodcalled‘few-shotchain-
meaningtotheword. of-thought’(CoT)prompting(Zhangetal.2022)comesinto

Figure2:Exampleof10-hopreasoning,featuringaquestion
Figure1:Anillustrativeexamplefordemonstratingrelation
regardingtwoentitiesthatarenotdirectlyconnectedinthe
extractionand1-hopspatialreasoning.
stories. The diagrams on the right do not form part of the
inputtotheAIsystembutareforillustrativepurposesonly.
play.ThesedemonstrationsenableLLMstoexplicitlygen-
erate reasoning steps, thereby improving their accuracy in
eitherdirectlyorindirectlyconnected.Multi-hopreason-
reasoningtasks.Thistechniqueinvolvesahandfulofmanu-
ingaddsmorecomplexitytotheproblem,asitinvolvesa
allycuratedstep-by-stepreasoningdemonstrations.
greater number of provided relations. To solve the prob-
As we review these developments, it is clear that while
lem, one needs to identify useful relations and then pro-
significant progress has been made, challenges remain in
ceedwithrelationinferencestepbystep.
both traditional and LLM approaches to spatial reasoning.
The limitations of models like ChatGPT indicate the need
forcontinuedresearchandenhancementstrategies.Thispa- ProblemswiththeDataset
peraimstocontributetothisbyexaminingtheselimitations
Eight spatial relations (top, down, left, right, top-left, top-
more closely and proposing potential avenues for improve-
right, down-left, and down-right) are utilized for the story
ment.WeaimtoexplorethelimitofGPTasageneralprob-
generation of StepGame. These relations are expressed
lemsolverthatexploresitsownthoughtsandguidesitsown
through sentences in natural language. All sentences/state-
explorationwithdeliberatereasoningasheuristics. ments are based on a crowd-sourced template base3. Each
“story” is accompanied by a question that seeks to identify
TheStepGameBenchmarkforEvaluating
therelationsbetweentwoobjects,anditislabeledaccording
SpatialReasoning totheintendedrelationsatthetimeofstorycreation,rather
than the actual sentences used. A template is considered to
Inthispaper,wefocusonStepGame,inlinewithotherstud-
contain an error if the meaning conveyed by the sentence
ies that evaluate ChatGPT’s spatial reasoning proficiency
doesnotalignwiththerelationshipthatwasintendedtobe
usingStepGameandSpartQA.StepGamecomprisesstory-
expressedduringthecreationofstoriesandlabels.
questionpairsinnaturallanguage,Theobjectiveistoanswer
Table 1 presents a detailed enumeration of errors in the
questionsregardingthespatialrelationsbetweentwospeci-
relation-to-sentence mappings identified in StepGame. Out
fiedentities.TheStepGamebenchmarkcontainstwosetsof
ofthe214templatesexamined,14werefoundtocontainer-
data:acleansetwheretherearepreciselyk factsgivenfor
rors.Oftheeightdifferentrelationshipmappingsavailable,
any given k-hop instance, and a noise set where there are
only o above o and o left o are devoid of mistakes.
morethankfactsgiven,andtheextrafactsaredistracting. 1 2 1 2
The question arises as to why there are so many errors in
SpatialReasoningTypes the crowd-sourced expressions; presumably this is down to
insufficientqualitycontroloverthecrowdworkerreponses.
• 1-Hop Spatial Reasoning. In 1-hop reasoning, we are
For each k value, the StepGame dataset includes 10,000
given a relation description between two entities and are
test samples. Table 2 displays the percentage of exam-
asked about the spatial relation from one entity to the
plescontainingsentencesderivedfromincorrecttemplates,
other.1-hoprelationreasoningandrelationextractioncan
which hints at a rising trend in inaccuracies as k increases,
be considered similar processes. As exemplified in Fig-
suggestingapotentialcumulativeimpact.
ure 1, consider the story where J is diagonally above B
Amongthese14incorrecttemplates,fourcannotbereme-
totherightata45-degreeangle.ThequestionisWhatis
diedinexistingStepGamebenchmarkexamples.
thespatialrelationofagentJtoagentB?.Thisissimilar
torelationextraction.However,ifwechangethequestion • o 1 upperright o 2 :ObjectAisaboveobjecto 1 .
to What is the spatial relation of agent B to agent J?, it • o upperleft o :o isdiagonallyleftandaboveo .
1 2 1 1
needsareversereasoningprocesstop right(“J”,“B”)→
• o lowerright o |o upperleft o |o upperright o :
down left(“B”,“J”). Both expressions are correct repre- 1 2 1 2 1 2
o is to the right and above o at an angle of about 45
sentationsforrelationextraction. 1 2
degrees.
• Multi-HopSpatialReasoning.Figure2providesoneex-
ampleof10-hopreasoning,whichisfromthe‘clean’set. 3https://github.com/ZhengxiangShi/StepGame/blob/main/
Thequestionsaskabouttherelationbetweentwoobjects, Code/template.py

Relation OriginalIncorrectTemplate
o ando areparallel,ando ontherightofo .
2 1 2 1
o ando areparallel,ando istotherightofo .
right 2 1 2 1
o ando arehorizontalando istotherightofo .
2 1 2 1
o ando areboththerewiththeobjecto istothe
2 1 2
rightofobjecto .
1
o isplacedatthebottomofo . Figure3:Sentence-to-RelationMappingExamples.
2 1
below o isatthebottomofo andisonthesamevertical
2 1
plane.
o 2 presentsbelowo 1 . we convert this template form into a structured represen-
lowerleft o 2 isthereando 1 isatthe10positionofaclockface. tation ν(o 0 ,o 1 ), where o 0 and o 1 correspond to the two
o ispositionedbelowo andtotheleft.
2 1 objectsmentionedinr,andν signifiesthespatialrelation
ObjectAisaboveobjecto andtotherightofit,too.
upperright o isdiagonallytotheupp 1 errightofo . between o 0 and o 1 . Specifically, for questions inquiring
2 1 about relations from the start object o to the target ob-
lowerright o istotherightandaboveo atanangleofabout45 0
1 2 ject o , the template is query o o , and the correspond-
degrees. t 0 t
ing ASP fact is represented as query(o ,o ). Illustrative
o istotherightandaboveo atanangleofabout45 0 t
upperleft d 1 egrees. 2 examplesofthisprocesscanbefoundinFigure3.
o 1 isdiagonallyleftandaboveo 1 . • LogicalReasoningwithASP.Thelogicalfactsν(o 0 ,o 1 ),
generatedthroughsemanticparsingforallrelationsinthe
Table1:IncorrectsentencetemplatesinStepGame.TheRe- story R, are used as input to the ASP module for spa-
lationcolumnsignifiesrelationforo relation o . tial reasoning. The ASP module was implemented us-
1 2
ing Clingo and includes rules specifically tailored for
k=1 k=2 k=3 k=4 k=5 k=6 k=7 k=8 k=9 k=10 StepGame. These rules transform StepGame into a qual-
Clean 7.64 15.0320.8726.3932.5437.6641.7147.2051.5054.29 itative spatial reasoning problem in a 2D grid space.
Noise20.4330.1934.5948.1857.1361.1463.6069.4572.8474.21 These rules incorporate offsets for 9 spatial relations,
such as offset(right) = (0,1) and offset(lower-left) =
Table2:Percentageofincorrectinstancesoutofallinstances (−1,−1).ThemainruleintheASPmodulecalculatesthe
overk=1–10testsets. locationofo too byaddingtheoffsetsν(o ,o ).
0 1 0 1
While this approach offers a solution to the StepGame
benchmark challenge, it does require prior familiarity with
• o lowerleft o |o upperleft o :o isthereando is
1 2 1 2 2 1
the templates and mandates updates to the template base
atthe10positionofaclockface.
when confronted with new stories employing novel tem-
The first and second templates are irreparable because plates. In contrast, an LLM approach holds the potential
it is impossible to identify what o 2 is when sentences to flexibly adjust to unfamiliar templates. Additionally, the
are formed using them. The third and fourth templates method’sdependenceoncustomizedruleswithinthelogical
cannot be corrected since they were applied to multiple programconstitutesanotheraspecttobemindfulof.
spatial relations, although each accurately represents just
one. For example, for the sentence ‘Q is to the right and Chain-of-Thought(CoT)Prompting
above P at an angle of about 45 degrees’, three map-
WedevisedacustomizedCoTforthespatialreasoningtask.
ping relations exist: Q upperright P, Q lowerright P,
The core idea of CoT is to introduce a chain of thoughts
and Q upperleft P. Although this sentence expresses the
c ,...,c ,...,c to bridge input x and output y, where i
meaning Q upperright P, it is uncertain which candidate 1 i n
representsi-thstep.InourcustomizedCoTforStepGame,x
wasusedforthelabel.Forsuchtemplates,auniquecorrec-
consistsofthetaskdescription,few-shotexamples,relation
tion could not be chosen, necessitating the removal of the
story,andquestion,whileyrepresentstheanswerregarding
sentencesthatusethesetemplatefromthedataset.
therelationsbetweenthequeriedobjects(fromthestartob-
jecto tothetargetobjecto ).Eachthoughtc istoidentify
Methods i t i
directspatialconnectionsbetweenobjects(o ando ).We
i i+1
SolutionfortheCorrectedBenchmark takeCoTastepfurtherbydecomposingeachstepofthought
Our error-free approach is entirely logic-based, without c i toexplorethepotentialadvantagesofincorporatingaco-
the use of LLMs. We begin by performing template-based herentanddetailedreasoningprocess.
sentence-to-relation mapping, akin to semantic parsing. ThoughtCategorisation.Wecategorisethethoughtinto
Then, we employ ASP for logical reasoning, utilizing the
threetypes:linkestablishmentthoughtsclink,relationmap-
ASP reasoner introduced by (Yang, Ishay, and Lee 2023). ping thoughts cmap, and coordinate calculation thoughts
Thesetwocomponentsoperateindependently:
ccalcu.Ateachreasoningstep,thesethreetypesofthought
aresequentiallysampledasacontinuouslanguagesequence
• Sentence-to-Relation Mapping. When presented with a c =[clink,cmap,ccalcu]usingtheLLM.
natural language relation description r, we first identify i i i i
thetemplateusedinrthroughacomparisonwiththetem- 1. clink:GuidetheLLMtoexamineallrelationsinthestory
i
platebase.Thistemplateissymbolizedaso ν o .Then, (R = [r1,...,rj,...,rk])andselectrj forthei-thstep
0 1

fork-hopreasoning,ensuringitdirectlydescribesthere- Algorithm1:OurToTApproach
lationwitho i andhasnotbeenusedinanypreviousstep. Require:LLM,inputx
Forthestartobject(i=0),weusetheprompt“Startwith
o .Accordingto”andforthemiddleobjects(i≥1),we 1: S 0 ←Init(x)
0 2: i←1
usetheprompt“Thensearchforo .Accordingto”.Full
detailsofthepromptscanbefound i intheAppendix4. 3: whilenos f ∈S i−1 hasarrivedato t do
2. cm i ap:Maprj toasimplerelationdescriptionsuchas“o i 4 5 : : S if i ′ S ← ′ = {s ∅ ·c th |c en ∈ r G et ( u s r , n j) f ∧ ai C lu h re ainExtn(c)∧s∈S i−1 }
i r s el t a o tio th n e fr ν om of o o i t + o 1 o ,” wh . e T r h e e ν pr r o e m pr p e t se “ n T t h s is th m e e k a e n y s” sp h a e t l i p a s l 6: S i ← i select(b,{⟨s,y⟩|s∈S i ′∧y =Σn 1 σ(V(s))})
i i+1 7: i=i+1
theLLMperformthismapping.
8: endwhile
3. cc i alcu:Userjtocalculatethecoordinatesofo i+1 .Weset 9: returnLink(s f )
o at (0,0), and each spatial relation is assigned an off-
o
settodeterminethepositionsoftheobjects.Theprompt
“o = o + offset(rj) = (x ,y ) + (x ,y ) =
i+1 i oi oi ν ν withinthechain.”Inourexperiment,wesetj =2,mean-
(x ,y )”instructstheLLMonthecalculationpro-
oi+1 oi+1 ingthatweinstructtheLLMtogeneratecontenttwicefor
cess. It computes the coordinates of o and generates
i+1 eachstates∈S .
theoutputlike“Therefore,Bisat(x ,y ).” i−1
oi+1 oi+1
• State Evaluation V(s). Our approach involves a classi-
Tree-of-Thoughts(ToT)Prompting fication methodology, using the designed value prompt
“Evaluate whether the chain can reach the target (sure/-
Algorithm 1 is designed to enhance the reasoning chain-
likely/impossible).Ifthechainhasalreadyreachedthetar-
buildingprocess,allowingLLMstoconsiderdifferentpath-
get,it’s‘sure’.Iftheunusedrelationsincludethecurrent
ways.Thisisusefulbecauseduringthesearchforrelations
object, it’s ‘likely’. If there are no unused relations that
withanobject,distractingconnectionsmayarise,asshown
includethecurrentobject,it’s‘impossible’.”Thisprompt
in Figure 2. However, it is essential to follow a correct se-
guides the LLM to sequentially examine all newly gen-
quence to successfully reach the target object. If an LLM erated states s ∈ S′ n times – using the stochasticity of
mistakenlytracksanincorrectsequence,itcouldgetstuckin i
theLLMwithanonzerotemperaturetoincreasethereli-
a dead end leading to incorrect reasoning conclusions such
abilityofthescoring. Thethreetypesofoutputs-‘sure’,
as“Thestorydoesnotprovidedirectspatialinformation.”
‘likely’, and ‘impossible’ - are converted into numerical
The algorithm initiates by prompting the LLM to set up
scoresusingafunctionσ()tofacilitatetheselectionpro-
theinitialtreestate,denotedasS ,usingtheinputx,which
0 cessamongallnewlygeneratedstates.
comprises a story and a question. S is in the form “chain:
0
o ->, target: o , unused: R”. R represents all connections • SearchAlgorithmThechoicebetweenutilizingbreadth-
0 t
betweenobjectsinthestory,intheformofobject1-object2. firstsearch(BFS)ordepth-firstsearch(DFS)dependson
Then it proceeds to construct a linking chain from o to o the tree structure. In the StepGame benchmark, the tree
0 t
in iterative steps, wherein for the i-th step (1 ≤ i ≤ 10), depthislimited(depth≤10),andthenumberofthought
the LLM considers the tree state S built up to that step. candidates k for each step is also limited (width ≤ 3 in
i−1
If no state s in S reaches o , the LLM is prompted to mostcases).However,adeepersearchdoesnotnecessar-
i−1 t
generate j candidate thoughts for each s in the current set ily guarantee better results. In certain scenarios, o 0 and
of states, S i (j = 2 in this paper). G prompts the LLM o t may be directly connected in one relation statement,
to search for a potential object o connected to the current allowing for shorter linking chains between them, which
i
object o from the unused relations Runused. A check is is preferable. Therefore, we opt for BFS to maintain all
i−1 i−1
made(CheckExtn(c)))toseeiftheproposalmadeisareal promising states. We set the breadth width b = 3, main-
candidateextension.Forallcandidatethoughts,V prompts taining the three most promising linking-chain states per
the LLM to evaluate the state to determine if the chain can step.Thecriterionforstoppingsearchingissetwhenthe
proceed with o and the updated Runused to reach o . The linkingchainarrivesatthetargetobject.
i i−1 t
top-ratedbtreestatesinS i ′ areselectedasS i .Whenthereis Our ToT approach is used to construct the reasoning
astates f whichreacheso t ,theLwillbepromptedwiththe chain from o 0 to o t . Subsequently, the spatial relation be-
linking chain construction prompt (Appendix D.4) to form tweentheseobjectsiscomputedfollowingthepreviousCoT
thefinallinksl. promptingmethod,withtheuseofcmapandccalcu.
• ThoughtGenerationG(s,j).Givenatreestates,welet
ExperimentalDesign
theLLMproposej thoughtsusingthethoughtgeneration
prompt “Use relations listed in unused relations to enu-
ModelSettings
merateallpotentialexpansionsofthechainbyconsidering
unusedrelationsthatexhibitadirectlinktothelastobject WeusetheAzureOpenAIServiceforChatGPT(3.5-Turbo)
andGPT-3(Davinci),andGPT-4APIaccess.Toyieldmore
4TheArXiv versionof thispaper includesthe Appendixcon- concentrated and deterministic results, we set the tempera-
tainingpromptingexamples. tureto0inCoTexperiments.InToTexperiments,wefollow

(Yao et al. 2023), setting the temperature to 0.7 for gener- left/ above lower left/ lower right/
ating varied thought proposals. The remaining parameters right /below upper right upper left
wereleftatthestandardconfigurationsforthesemodels. total 44 53 50 53
text-curie-001 11 41 30 37
DifferentTestSubsets Itiscommonpracticeinthestud-
text-davinci-003 0 0 0 2
iescited(Bangetal.2023),(Yang,Ishay,andLee2023)to
gpt-3.5-turbo 2 2 3 1
useasubsetof30or100testexamplesfromthefullsetof
10,000 for each k value. While this method helps in con-
servingtokenusage,itcouldpotentiallyintroducebiasesor Table 3: The relation extraction performance of GPT. The
inaccurateestimationsofthemodelperformance. numbersinrows2-4areincorrectpredictionsnumbers.
We examine the effect of the number of test examples.
Specifically,wewantedtodeterminewhetherevaluatingon
alimitednumberoftestexamplescouldintroduceinaccura- consistently outperforms the others across all hop levels.
cies.Toachievethis,weconductedtestsonaclean,filtered Interestingly, clean 5shot (1,3,5,7,10) performs better than
test set for k-hop reasoning (k ∈ [1,10]), thereby covering clean 10shot (1∼10) at almost every hop level. This sug-
a range of task complexities. Tests were carried out on 30, geststhatselectingexamplesfromawiderrangeofhoplev-
100,and1000testexamplestoassesstheimpactofthenum- els(1,3,5,7,10)canbemorebeneficialthanhavinganexam-
beroftestexamplesontheevaluation. plefromeachhoplevelfrom1to10.
Different Few-Shot Sets We created three different few- Influence of Models As indicated in a recent study (Ye
shotpromptingsetstoevaluatetheinfluenceofinputexam- et al. 2023), Turbo demonstrates comparable performance
plesinprompts. toDavinciacrossmanytasks.However,itfallsshortinthe
• clean5shot(1,3,5,7,10):Createapromptconsistingoffive machine reading comprehension, part-of-speech, and rela-
examples,withoneexampleeachfromtasksrequiring1- tionextractiontasks,potentiallyowingtoitssmallermodel
hop,3-hop,5-hop,7-hop,and10-hopreasoning. size.TheStepGamespatialreasoningtaskrequiresthecom-
prehensionofsequentialspatialconnectionsandtheability
• clean 10shot: Formulate a prompt using ten examples,
to draw deductions from them. According to the right sub-
eachonederivedfromadistinctk-hoptaskincleanset.
plot of Figure 4, the Davinci model generally outperforms
• clean 5shot separate: Construct a prompt for each k-hop
the Turbo model across varying levels of task complexity
reasoning task, utilizing five examples from the corre-
(number ofhops). The differencesin performance between
spondingk-hoptrainingsetasfew-shotexamples.
thetwomodelsaremoresignificantatlowercomplexitylev-
els,buttheyappeartoconvergeasthecomplexityincreases.
ExperimentalResults
ResultsoftheImprovedMethods
EvaluationResults
Influence of Scale of Test Examples We employ the ResolutionfortheBenchmark Theresultsofourresolu-
clean 10shot prompting setting. The results are presented tion(sentence-to-relationmapping+ASP-basedreasoning)
in the left subplot of Figure 4. Upon evaluation of the ex- aredisplayed in the‘Map+ASP’rowof Table4.The num-
pandedtestsetcomprising1000examples,themodelshows bersinthetableindicateaccuracyscores,withhighervalues
a uniform decrement in performance as k increases from 1 indicating better performance. This demonstrates the profi-
to 10. This trend indicates the increased complexity as the ciency achieved in spatial relation mapping and multi-hop
number of hops increases. With smaller test sets of 100 or spatialreasoning,allwithoutencounteringanyerrors.
30 examples, the trend is less consistent, and there are oc-
GPTforRelationExtraction+ASPforReasoning We
casionalincreasesinperformanceatcertainhoplevels.The
analyze the performance of GPT in the relation extraction
varianceinperformance,particularlyforthe30-exampletest
subtask,asoutlinedinTable3.Curiehasthehighestnumber
set, may indeed be larger. This could be due to the smaller
ofwrongpredictionsacrossdifferentrelations,Davinciand
sample size providing less comprehensive coverage of the
Turboshowbetterperformance.
potentialrangeoftasks,leadingtomorefluctuationsinper-
Thestate-of-the-artresultsachievedby(Yang,Ishay,and
formance.Thisindicateslargertestsetscanprovideamore
Lee 2023) (using GPT-3 for semantic parsing and ASP for
stableandreliableindicatorofamodel’sperformanceacross
reasoning)arepresentedinthe“SOTA”rowofTable4.They
differentcomplexitylevels(i.e.,numberofhops).
achieve approximately 90% accuracy for lower hops and
InfluenceofPromptingExamples Themiddlesubplotin 88.3%accuracyfor10-hopreasoning.Theyattribute10.7%
figure4indicatesthatthechoiceofpromptingstrategycan oftheinaccuraciestodata-relatedconcerns.
impact the model’s ability to handle tasks of varying com- We provide an evaluation of their approach on-
plexity.Similartothepreviousdata,allpromptingstrategies the corrected dataset, with the results displayed in the
showatrendofdecreasingaccuracyasthenumberofhops “Curie+ASP” and “Davinci+ASP” rows. Among the 1000
increases.Thistrendisconsistentandsuggeststhatthecom- test examples (100 for each k), only 2 errors were encoun-
plexityofthetasksgrowswiththenumberofhops. teredwithDavinci.causedbysemanticparsing:thesentence
The performances of the three methods are close. While “If E is the center of a clock face, H is located between
differences exist at specific hop levels, no single method 2 and 3.” was parsed incorrectly as right(“H”,“E”), but

Figure4:Accuracycomparisonforvaryingnumbersofhops(1-10)onthecleantestset.Ontheleft,weshowtheperformance
variation of the Turbo model with 10shot prompting over different test set sizes (30, 100, and 1000 examples). The middle
sectionillustratestheperformanceoftheTurbomodelunderthreedistinctpromptingsettings:5shot(1,3,5,7,10),10shot,and
5shotseparate.Therightportionshowcasestheperformanceoftwomodels-DavinciandTurbo-using10shotprompting.
k=1k=2k=3k=4k=5k=6k=7k=8k=9k=10 largerhops.FortheTurbomodel,althoughourCoTmethod
Map+ASP 100 100 100 100 100 100 100 100 100 100 bringsimprovementsaskincreases,thegainsarenotaspro-
Curie+ASP 46 43 42 59 67 67 57 56 58 61 found as those observed with the Davinci and GPT-4. This
Davinci+ASP 100 100 99 100 100 99 100 100 100 100 couldbeattributedtothelonglengthofourprompts,requir-
SOTA 92.689.989.193.892.991.691.290.489.0 88.3 inganuancedunderstandingofcoordinatesandrelations.
base 62 43 30 35 29 25 29 31 16 20
Turbo CoT / 34 40 36 28 28 26 31 25 24 Conclusion
ToT CoT / / 35 35 25 45 15 40 40 35
base 77 42 21 26 25 30 23 23 22 22 ThispaperhasintroducedarevisedversionoftheStepGame
Davinci CoT / 48 53 46 46 48 40 45 41 32 benchmark, correcting template errors that distort model
ToT CoT / / 65 50 45 60 50 50 55 50
performance evaluations, leading to a more accurate eval-
base 100 70 55 45 40 25 40 35 35 25
uationofthespatialreasoningcapabilitiesofAIsystemsat-
GPT-4 CoT / 80 75 95 85 85 90 80 60 65
tempting the challenge. We highlight Davinci and Turbo’s
ToT CoT / / 85 85 90 90 85 90 100 95
abilities in mapping texts to spatial relations and their lim-
itations in multi-hop spatial reasoning. Our solution com-
Table 4: Accuracy comparison of GPT models on revised
binestemplate-to-relationmappingwithlogic-basedreason-
StepGameusingdifferentmethods.
ing, effectively addressing challenges in this task. We also
enhanceLLMs’spatialreasoningabilitythroughprompten-
gineering,usingCoTandToTstrategies.
supposedtobeup right(“H”,“E”).
ThispaperfocusesonStepGame;futurestudiescouldex-
CoTandToT TheexperimentalresultsinTable4involv- tendourfindingstootherbenchmarks.Ourmethodsaresuit-
ing GPT-4 and ToT are based on a test set comprising 20 ableforadaptationtovarious2Dgrid-baseddirectionalspa-
instances considering token usage, while for Davinci and tialtasks,suchasthebAbI(task17).Thisadaptationwould
Turbo, we used a larger test set of 100 samples. The re- involvecustomizingthetemplatefortheASP-basedsolution
sultsforthebaseandCoTmethodswereobtainedusingthe andmodifyingtaskdescriptionsandfew-shotexamplesfor
5shotseparatepromptingonthecleanset.AlltheToT CoT CoTandToTapproaches.Fortasksthatrequireacombina-
results presented in the table involve the use of GPT-4 for tionofdirectional,topological,anddistancereasoning,like
building the linking chain, followed by the application of SpartQA,itwouldbenecessarytointegrateadditionalrules
Turbo,Davinci,andGPT-4forCoTreasoningwiththecon- andontologyintoboththeASPprogramandthepromptsto
structed linking chain. The GPT-4 model exhibits superior LLMsforeffectivesolutiondevelopment.
performanceacrossnearlyallsettings.Withthebasicinput- The effective resolution of the StepGame benchmark
outputprompt,despitestartingat100%accuracyfork =1, prompts a need for more challenging versions. While hav-
itsaccuracydipsto25%fork =10,indicatingthateventhe ingawell-definedsetofspatialrelationsconvertedintonat-
most powerful GPT model struggles to maintain accuracy urallanguageusingasetoftemplatesisappealing,itleads
as task complexity rises. Humans would probably find this to controlled natural language which is more amenable to
challengingtoo. special purpose reasoning. Finding a way to generate more
With the implementation of our CoT and ToT approach, naturalistic problem statements automatically would there-
the GPT-4 model demonstrates significant performance en- fore be highly desirable. Additionally, the current indepen-
hancementsformorecomplextasks(rangingfromk =2to dent use of LLMs and logic programs suggests a potential
k = 10).OurToTandCoTmethodconsiderablyenhances research direction towards integrating these tools for more
the performance of the Davinci and GPT-4, particularly in comprehensiveandcohesiveproblem-solvingstrategies.

Acknowledgments Li, F.; Hogg, D. C.; and Cohn, A. G. 2022. Ontol-
ogy Knowledge-enhanced In-Context Learning for Action-
This work has been partially supported by Microsoft Re-
EffectPrediction. InAdvancesinCognitiveSystems.ACS-
search - Accelerating Foundation Models Research pro-
2022.
gram,withtheprovisionofAzureresourcestoaccessGPT.
This work was also partially supported by the Turing’s Mirzaee,R.;andKordjamshidi,P.2022. TransferLearning
Defence and Security programme through a partnership withSyntheticCorporaforSpatialRoleLabelingandRea-
withtheUKgovernmentinaccordancewiththeframework soning. arXivpreprintarXiv:2210.16952.
agreementbetweenGCHQandTheAlanTuringInstitute. Mirzaee, R.; and Rajaby, H. 2021. SpartQA: A Tex-
tual Question Answering Benchmark for Spatial Reason-
AuthorContributions ing. In The 2021 Annual Conference of the North Ameri-
canChapteroftheAssociationforComputationalLinguis-
AGC and DCH proposed the initial line of work. FL de-
tics(NAACL-2021).
signed the actual implementation, performed all the eval-
OpenAI. 2023. GPT-4 Technical Report. ArXiv,
uations, and wrote the initial paper draft. DCH and AGC
abs/2303.08774.
supervisedFL.Allauthorscontributedtosubsequentpaper
revisions. Shi,Z.;Zhang,Q.;andLipani,A.2022. Stepgame:Anew
benchmark for robust multi-hop spatial reasoning in texts.
References InProceedingsoftheAAAIConferenceonArtificialIntelli-
gence,11321–11329.
Alomari, M.; Li, F.; Hogg, D. C.; and Cohn, A. G. 2022.
Skiadopoulos, S.; and Koubarakis, M. 2001. Composing
Onlineperceptuallearningandnaturallanguageacquisition
cardinaldirectionrelations. InInternationalSymposiumon
forautonomousrobots. ArtificialIntelligence,303:103637.
SpatialandTemporalDatabases,299–317.Springer.
Bang,Y.;Cahyawijaya,S.;Lee,N.;Dai,W.;Su,D.;Wilie,
Wang,L.;Xu,W.;Lan,Y.;Hu,Z.;Lan,Y.;Lee,R.K.-W.;
B.; Lovenia, H.; Ji, Z.; Yu, T.; Chung, W.; et al. 2023. A
andLim,E.-P.2023. Plan-and-SolvePrompting:Improving
multitask,multilingual,multimodalevaluationofChatGPT
Zero-ShotChain-of-ThoughtReasoningbyLargeLanguage
onreasoning,hallucination,andinteractivity. arXivpreprint
Models. arXivpreprintarXiv:2305.04091.
arXiv:2302.04023.
Wei, J.; Wang, X.; Schuurmans, D.; Bosma, M.; Chi, E.;
Bommasani, R.; Hudson, D. A.; Adeli, E.; Altman, R.;
Le, Q.; and Zhou, D. 2022. Chain of thought prompting
Arora,S.;vonArx,S.;Bernstein,M.S.;Bohg,J.;Bosselut,
elicits reasoning in large language models. arXiv preprint
A.;Brunskill,E.;etal.2021. Ontheopportunitiesandrisks
arXiv:2201.11903.
offoundationmodels. arXivpreprintarXiv:2108.07258.
Weston, J.; Bordes, A.; Chopra, S.; Rush, A. M.;
Chen, J.; Cohn, A. G.; Liu, D.; Wang, S.; Ouyang, J.; and
VanMerrie¨nboer,B.;Joulin,A.;andMikolov,T.2015. To-
Yu,Q.2015. Asurveyofqualitativespatialrepresentations.
wardsai-completequestionanswering:Asetofprerequisite
TheKnowledgeEngineeringReview,30(1):106–136.
toytasks. arXivpreprintarXiv:1502.05698.
Cohn,A.G.;andHazarika,S.M.2001. Qualitativespatial
Yang, Z.; Ishay, A.; and Lee, J. 2023. Coupling
representationandreasoning:Anoverview. Fundamentain-
Large Language Models with Logic Programming for Ro-
formaticae,46(1-2):1–29.
bust and General Reasoning from Text. arXiv preprint
Cohn,A.G.;andHernandez-Orallo,J.2023.Dialecticallan- arXiv:2307.07696.
guagemodelevaluation:Aninitialappraisalofthecommon- Yao, S.; Yu, D.; Zhao, J.; Shafran, I.; Griffiths, T. L.; Cao,
sense spatial reasoning abilities of LLMs. arXiv preprint Y.;andNarasimhan,K.2023. Treeofthoughts:Deliberate
arXiv:2304.11164. problemsolvingwithlargelanguagemodels. arXivpreprint
Cohn,A.G.;andRenz,J.2008.Qualitativespatialrepresen- arXiv:2305.10601.
tationandreasoning. FoundationsofArtificialIntelligence, Ye,J.;Chen,X.;Xu,N.;Zu,C.;Shao,Z.;Liu,S.;Cui,Y.;
3:551–596. Zhou,Z.;Gong,C.;Shen,Y.;etal.2023. Acomprehensive
Creswell, A.; Shanahan, M.; and Higgins, I. 2022. capabilityanalysisofgpt-3andgpt-3.5seriesmodels. arXiv
Selection-inference: Exploiting large language models preprintarXiv:2303.10420.
for interpretable logical reasoning. arXiv preprint Zhang, Z.; Zhang, A.; Li, M.; and Smola, A. 2022. Auto-
arXiv:2205.09712. maticchainofthoughtpromptinginlargelanguagemodels.
Kordjamshidi, P.; Moens, M.-F.; and van Otterlo, M. 2010. arXivpreprintarXiv:2210.03493.
Spatialrolelabeling:Taskdefinitionandannotationscheme. Zhou, D.; Scha¨rli, N.; Hou, L.; Wei, J.; Scales, N.; Wang,
In Proceedings of the Seventh conference on International X.; Schuurmans, D.; Cui, C.; Bousquet, O.; Le, Q.; et al.
Language Resources and Evaluation (LREC’10), 413–420. 2022. Least-to-mostpromptingenablescomplexreasoning
EuropeanLanguageResourcesAssociation(ELRA). inlargelanguagemodels.arXivpreprintarXiv:2205.10625.
Kordjamshidi,P.;VanOtterlo,M.;andMoens,M.-F.2011.
Spatialrolelabeling:Towardsextractionofspatialrelations
from natural language. ACM Transactions on Speech and
LanguageProcessing(TSLP),8(3):1–36.

A.ExamplePromptsforBase If the sentence is describing cardinal
Given a story about spatial relations directions, then north denotes above, east
among objects, answer the relation between denotes right, south denotes below, and west
two queried objects. Possible relations denotes left.
are: overlap, above, below, left, right,
upper-left, upper-right, lower-left, and Story:
lower-right. If a sentence in the story is Q is to the right of O and is on the same
describing clock-wise information, then 12 horizontal plane.
denotes above, 1 and 2 denote upper-right, 3 Q is slightly off center to the top left
denotes right, 4 and 5 denote lower-right, 6 and M is slightly off center to the bottom
denotes below, 7 and 8 denote lower-left, 9 right.
denote left, 10 and 11 denote upper-left. X and E are next to each other with X on the
If the sentence is describing cardinal top and E at the bottom.
directions, then north denotes above, east O is sitting at the upper right position to
denotes right, south denotes below, and west E.
denotes left. W is on the right side and below M.
What is the relation of the agent W to the
Story: agent E?
Q is to the right of O and is on the same Answer: We first link W and E using the
horizontal plane. relations in the story. W is to the
Q is slightly off center to the top left lower-right of M. M is to the lower-right
and M is slightly off center to the bottom of Q. Q is to the right of O. O is to
right. the upper-right of E. So the answer is
X and E are next to each other with X on the lower-right.
top and E at the bottom. ···
O is sitting at the upper right position to
E. Story:
W is on the right side and below M. 1. The object E is positioned directly above
What is the relation of the agent W to the the object W.
agent E? 2. E is sitting at the upper right position
Answer: lower-right to I.
3. W is placed at the upper left of C.
··· 4. L is over there and Y is on the left.
5. C and Y are both there with the object Y
Story: below the object C.
1. The object E is positioned directly above 6. What is the relation of the agent E to
the object W. the agent Y?
2. E is sitting at the upper right position
to I. C.ExamplePromptsforOurCoT
3. W is placed at the upper left of C. Given a story about spatial relations
4. L is over there and Y is on the left. among objects, answer the relation between
5. C and Y are both there with the object Y two queried objects. Possible relations
below the object C. are: overlap, above, below, left, right,
6. What is the relation of the agent E to upper-left, upper-right, lower-left, and
the agent Y? lower-right. If a sentence in the story
is describing clock-wise information,
B.ExamplePromptsforCoTin(Yang,Ishay,andLee then 12 denotes above, 1 and 2 denote
2023) upper-right, 3 denotes right, 4 and 5
Given a story about spatial relations denote lower-right, 6 denotes below, 7 and
among objects, answer the relation between 8 denote lower-left, 9 denote left, 10 and
two queried objects. Possible relations 11 denote upper-left. If the sentence is
are: overlap, above, below, left, right, describing cardinal directions, then north
upper-left, upper-right, lower-left, and denotes above, east denotes right, south
lower-right. If a sentence in the story is denotes below, and west denotes left. In
describing clock-wise information, then 12 all the spatial relations, assume that all
denotes above, 1 and 2 denote upper-right, 3 agents occupy a position on a grid point
denotes right, 4 and 5 denote lower-right, 6 of equally spaced points in the vertical
denotes below, 7 and 8 denote lower-left, 9 and horizontal directions and that agents
denote left, 10 and 11 denote upper-left. occupy the nearest grid point consistent

with the spatial relation. The offsets to I.
of 9 spacial relations: offset(overlap) = 3. W is placed at the upper left of C.
(0,0); offset(above) = (0,1); offset(below) 4. L is over there and Y is on the left.
= (0,-1); offset(left) = (-1,0); 5. C and Y are both there with the object Y
offset(right) = (1,0); offset(upper-left) below the object C.
= (-1,1); offset(upper-right) = 6. What is the relation of the agent E to
(1,1); offset(lower-left) = (-1,-1); the agent Y?
offset(lower-right) = (1,-1).
D.ExamplePromptsforOurToT
Story: D.1.Treestateinitializationprompt
1. Q is to the right of O and is on the same Provided with a sequence of statements
horizontal plane. that define the spatial relationships among
2. Q is slightly off center to the top left various objects, your task is to detail the
and M is slightly off center to the bottom subsequent actions. This includes initiating
right. the chain of connections, identifying the
3. X and E are next to each other with X on target object, and enumerating all links
the top and E at the bottom. between objects from the statements.
4. O is sitting at the upper right position
to E. Input: 1. Q is to the right of O and is on
5. W is on the right side and below M. the same horizontal plane. 2. Q is slightly
What is the relation of the agent W to the off center to the top left and M is slightly
agent E? off center to the bottom right. 3. X and
Reasoning: E are next to each other with X on the top
Let’s suppose W is at (0,0). We can connect and E at the bottom. 4. O is sitting at the
W and E using the relations given in the upper right position to E. 5. W is on the
story. right side and below M. What is the relation
Start with W. According to 5, "W is of the agent W to the agent E?
on the right side and below M." This Possible next steps:
means M is to the upper-left of W. M= W+ chain: W ->, target: E, unused: 1. Q-O, 2.
offset(upper-left) = (0,0)+(-1,1)=(-1,1). Q-M, 3. X-E, 4. O-E, 5. W-M.
Therefore, M is at (-1,1).
Then search for M. According to 2, "Q ···
is slightly off center to the top left
and M is slightly off center to the Input: {input}
bottom right." This means Q is to the Possible next steps:
upper-left of M. Q= M+ offset(upper-left)
= (-1,1)+(-1,1)=(-2,2). Therefore, Q is at D.2.Thoughtgenerationprompt
(-2,2). Use relations listed in unused relations
Then search for Q. According to 1, "Q is to to enumerate all potential expansions of the
the right of O and is on the same horizontal chain by considering unused relations that
plane." This means O is to the left of Q. exhibit a direct link to the last object
O= Q+ offset(left) = (-2,2)+(-1,0)=(-3,2). within the chain.
Therefore, O is at (-3,2).
Then search for O. According to 4, "O is Input: chain: G ->, target: Q, unused: 1.
sitting at the upper right position to C-R, 2. L-Q, 3. C-J, 4. J-E, 5. T-A, 6. G-N,
E." This means E is to the lower-left 7. G-A, 8. L-Y, 9. R-Q, 10. Y-T.
of O. E= O+ offset(lower-left) = Possible next steps:
(-3,2)+(-1,-1)=(-4,1). Therefore, E is at The last object within the chain is G, and
(-4,1). the unused relations 6. G-N and 7. G-A
We’ve reached E. So, considering W(0,0) and include G. relation chain: G -> N (use 6)
E(-4,1), W is to the lower-right of E. ->, target: Q, unused: 1. C-R, 2. L-Q, 3.
Answer: lower-right C-J, 4. J-E, 5. T-A, 7. G-A, 8. L-Y, 9. R-Q,
10. Y-T.
··· chain: G -> A (use 7) ->, target: Q,
unused: 1. C-R, 2. L-Q, 3. C-J, 4. J-E,
Story: 5. T-A, 6. G-N, 8. L-Y, 9. R-Q, 10. Y-T.
1. The object E is positioned directly above
the object W. ···
2. E is sitting at the upper right position

Input: {input} D.5.Spatialrelationreasoningprompt
Possible next steps: Given a story about spatial relations
among objects, answer the relation between
D.3.Stateevaluationprompt two queried objects. Possible relations
Evaluate whether the chain can reach the are: overlap, above, below, left, right,
target (sure/ likely/impossible). If the upper-left, upper-right, lower-left, and
chain has already reached the target, it’s lower-right. If a sentence in the story
’sure’. If the unused relations include the is describing clock-wise information,
current object, it’s ’likely’. If there are then 12 denotes above, 1 and 2 denote
no unused relations that include the current upper-right, 3 denotes right, 4 and 5
object, it’s ’impossible’. denote lower-right, 6 denotes below, 7 and
8 denote lower-left, 9 denote left, 10 and
chain: F ->, target: X, unused: 1. Y-F, 11 denote upper-left. If the sentence is
2. X-Y, 3. I-Q, 4. A-Q, 5. N-W, 6. N-A, 7. describing cardinal directions, then north
F-O, 8. O-W. The current object is F, there denotes above, east denotes right, south
are unused relations that include F (1. Y-F, denotes below, and west denotes left. In
7. F-O). all the spatial relations, assume that all
likely agents occupy a position on a grid point
of equally spaced points in the vertical
chain: L -> Q (use 2) ->, target: Q, unused: and horizontal directions and that agents
1. C-R, 3. C-J, 4. J-E, 7. G-A, 8. L-Y, 9. occupy the nearest grid point consistent
R-Q. with the spatial relation. The offsets
The chain already reaches the target object of 9 spacial relations: offset(overlap) =
Q. (0,0); offset(above) = (0,1); offset(below)
sure = (0,-1); offset(left) = (-1,0);
offset(right) = (1,0); offset(upper-left)
chain: G -> N (use 6) ->, target: Q, unused: = (-1,1); offset(upper-right) =
1. C-R, 2. L-Q, 3. C-J, 4. J-E, 5. T-A, 8. (1,1); offset(lower-left) = (-1,-1);
L-Y, 9. R-Q, 10. Y-T. offset(lower-right) = (1,-1).
The current object is N, and there are no Story:
unused relations that include N. 1. Q is to the right of O and is on the same
impossible horizontal plane.
2. Q is slightly off center to the top left
{input} and M is slightly off center to the bottom
right.
D.4.Linkingchainconstructionprompt 3. X and E are next to each other with X on
Given an input about spatial relations the top and E at the bottom.
among objects, build the linking chain 4. O is sitting at the upper right position
between the two queried objets. to E.
5. W is on the right side and below M.
Input: What is the relation of the agent W to the
1. H is above S with a small gap between agent E?
them. 2. S is positioned below I. 3. P is on Linking chain: W -> M (use 5) -> Q (use 2)
the top side to I. What is the relation of -> O (use 1) -> E (use 4)
the agent S to the agent P? Reasoning:
Steps: Let’s suppose W is at (0,0). We can analyze
chain: S ->, target: P, unused: 1. H-S, 2. the relation of W to E by following the
S-I, 3. P-I. linking chain and considering the relations
chain: S -> I (use 2) ->, target: P, provided in the story step by step.
unused: 1. H-S, 3. P-I. Start with W. According to 5, "W is
chain: I -> P (use 3) ->, target: P, on the right side and below M." This
unused: 1. H-S. means M is to the upper-left of W. M= W+
Answer: S -> I (use 2) -> P (use 3) offset(upper-left) = (0,0)+(-1,1)=(-1,1).
Therefore, M is at (-1,1).
··· Then come to M. According to 2, "Q is
slightly off center to the top left
Input: and M is slightly off center to the
{input} bottom right." This means Q is to the
upper-left of M. Q= M+ offset(upper-left)

= (-1,1)+(-1,1)=(-2,2). Therefore, Q is at
(-2,2).
Then come to Q. According to 1, "Q is to
the right of O and is on the same horizontal
plane." This means O is to the left of Q.
O= Q+ offset(left) = (-2,2)+(-1,0)=(-3,2).
Therefore, O is at (-3,2).
Then come to O. According to 4, "O is
sitting at the upper right position to
E." This means E is to the lower-left
of O. E= O+ offset(lower-left) =
(-3,2)+(-1,-1)=(-4,1). Therefore, E is at
(-4,1).
We’ve reached E. So, considering W(0,0) and
E(-4,1), W is to the lower-right of E.
Answer: lower-right
···
Story:
{input}
Linking chain: {chain}
