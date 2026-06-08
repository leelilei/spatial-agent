Title: cshperspect-LNM-a021808 1..15

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/papers/pdfs/cshperspect-LNM-a021808.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T03:09:08+00:00
- page_count: 15
- status: ok
- text_char_count: 58106

Metadata:
- author: unknown
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- none

Markdown Content:

Place Cells, Grid Cells, and Memory
May-BrittMoser,DavidC.Rowland,andEdvardI.Moser
CentreforNeuralComputation,KavliInstituteforSystemsNeuroscience,NorwegianUniversityofScience
andTechnology,7489Trondheim,Norway
Correspondence:edvard.moser@ntnu.no
Thehippocampalsystemiscriticalforstorageandretrievalofdeclarativememories,includ-
ingmemoriesforlocationsandeventsthattakeplaceatthoselocations.Spatialmemories
placehighdemandsoncapacity.Memoriesmustbedistincttoberecalledwithoutinterfer-
enceandencodingmustbefast.Recentstudieshaveindicatedthathippocampalnetworks
allowforfaststorageoflargequantitiesofuncorrelatedspatialinformation.Theaimofthe
thisarticleistoreviewanddiscusssomeofthiswork,takingasastartingpointthediscovery
ofmultiplefunctionallyspecializedcelltypesofthehippocampal–entorhinalcircuit,such
asplace,grid,andbordercells.Wewillshowthatgridcellsprovidethehippocampuswitha
metric,aswellasaputativemechanismfordecorrelationofrepresentations,thattheforma-
tionofenvironment-specificplacemapsdependsonmechanismsforlong-termplasticityin
thehippocampus,andthatlong-termspatiotemporalmemorystoragemaydependonoffline
consolidationprocessesrelatedtosharp-waverippleactivityinthehippocampus.Themul-
titude of representations generated through interactions between avarietyof functionally
specialized cell types in the entorhinal–hippocampal circuit may be at the heart of the
mechanismfordeclarativememoryformation.
Thescientificstudyofhumanmemorystarted Tolman,arigorousprogramforidentifyingthe
withHermanEbbinghaus,whoinitiatedthe laws of animal learning was initiated. By the
quantitative investigation of associative mem- middleofthe20thcentury,alanguageforasso-
ory processes as they take place (Ebbinghaus ciative learning processes had been developed,
1885). Ebbinghaus described the conditions andmanyofthefundamentalrelationshipsbe-
thatinfluencememoryformationandhedeter- tweenenvironmentandbehaviorhadbeende-
minedseveralbasicprinciplesofencodingand scribed.Whatwascompletelymissing,though,
recall,suchasthelawoffrequencyandtheeffect was an understanding of the neural activity
oftimeonforgetting.WithEbbinghaus,higher underlying the formation of the memory. The
mentalfunctionswerebroughttothelaborato- behaviorists had deliberately shied away from
ry.Inparallelwiththehumanlearningtradition physiological explanations because of the in-
that Ebbinghaus started, a new generation of tangiblenatureofneuralactivityatthattime.
experimental psychologists described the laws Then the climate began to change. Karl
ofassociativelearninginanimals.Withbehav- Lashley had shown that lesions in the cerebral
iorists like Pavlov, Watson, Hull, Skinner, and cortex had predictable effects on behavior in
Editors:EricR.Kandel,YadinDudai,andMarkR.Mayford
AdditionalPerspectivesonLearningandMemoryavailableatwww.cshperspectives.org
Copyright#2015ColdSpringHarborLaboratoryPress;allrightsreserved;doi:10.1101/cshperspect.a021808
CitethisarticleasColdSpringHarbPerspectBiol2015;7:a021808
1

M.-B.Moseretal.
animals(Lashley1929,1950),andDonaldHebb grid,border,andheaddirectioncells,eachwith
introduced concepts and ideas to account for distinctrolesintherepresentationofspaceand
complex brain functions at the neural circuit spatialmemory.Inthisarticle,weshalldiscuss
level, many of which have retained a place in potentialmechanismsbywhichthesecelltypes,
modernneuroscience(Hebb1949).BothLash- particularlyplaceandgridcells,inconjunction
ley and Hebb searched for the engram, but withsynapticplasticity,mayformthebasisofa
theyfoundnospecificlocusforit.Asignificant mammalian system for fast high-capacity de-
turning point was reached when Scoville and clarativememory.
Milner (1957) reported severe loss of memory
inanepilepticpatient,patientH.M.,afterbilat-
PLACECELLS,SYNAPTICPLASTICITY,
eral surgical removal of the hippocampal for-
ANDMEMORY
mation and the surrounding medial temporal
lobe areas. “After operation this young man The growing interest in hippocampal function
could no longer recognize the hospital staff and memory led John O’Keefe and John Dos-
norfindhiswaytothebathroom,andheseemed trovsky(O’KeefeandDostrovsky1971)andJim
torecallnothingoftheday-to-dayeventsofhis Ranck(Ranck1973)tointroducemethodsfor
hospitallife.”Thistragicmisfortuneinspiredde- recording activity from hippocampal neurons
cadesofresearchonthefunctionofthehippo- inawakeandfreelymovinganimals.Usingmin-
campus in memory. H.M.’s memory impair- iaturized electrodes forextracellular single-cell
mentcouldbereproducedinmemorytasksin recording,theywereabletoshowreliablelinks
animalsandstudiesofH.M.,aswellaslabora- betweenneuralactivityandbehavior.Themost
tory animals, pointed to a critical role for the strikingrelationshipwasnotedbyO’Keefeand
hippocampusindeclarativememory—memo- Dostrovsky,whofoundthathippocampal cells
ry, which, in humans, can be consciously re- respondedspecificallytothecurrentlocationof
calledanddeclared,suchasmemoriesofexpe- theanimal.Theycalledthesecells“placecells”
riences and facts (Milner et al. 1968; Mishkin (Fig.1).Differentplacecellswerefoundtohave
1978;CohenandSquire1980;Squire1992;Cor- differentfiringlocations,orplacefields(O’Keefe
kin 2002). What was missing from these early 1976).Placewasmappednontopographicallyin
studies,however,wasawaytoaddresstheneu- the sense that place fields of neighboring cells
ronal mechanisms that led information to be were no more similar than those of cells that
storedasmemory. werefarapart (O’Keefe1976;WilsonandMc-
Theaimofthisarticleistoshowhowstudies Naughton 1993), although the size of the fir-
of hippocampal neuronal activity during the ingfieldsincreasedfromdorsaltoventralhip-
pastfewdecades havebroughtustoapointat pocampus (Jung et al. 1994; Kjelstrup et al.
which a mechanistic basis of memory forma- 2008).Thecombinationofcellsthatwereactive
tionisbeginningtosurface.Anearlylandmark ateachlocationintheenvironmentwasunique,
inthisseriesofinvestigationswasthediscovery despitethelackoflocationtopography,leading
ofplacecells,cellsthatfireselectivelyatoneor O’Keefe and Nadel (1978) to suggest that the
fewlocationsintheenvironment.Atfirst,these hippocampusisthelocusofthebrain’sinternal
cellsseemedtobepartoftheanimal’sinstanta- mapofthespatialenvironment,amanifestation
neous representation of location, independent ofthecognitivemapproposedfrompurelybe-
of memory, but gradually, over the course of havioralexperimentsbyEdwardTolmanseveral
several decades, it has become clear that place decadesearlier(Tolman1948).
cells express current as well as past and future Thediscoveryofplacecellschangedtheway
locations.Inmanyways,placecellscanbeused many experimental neuroscientists thought
as readouts of the memoriesthat are stored in about hippocampal functions. Clinical studies
the hippocampus. More recent work has also starting with patient H.M. pointed to a role
shown that place cells are part of awider net- for the hippocampus in declarative memory
workofspatiallymodulatedneurons,including (Squire 1992), but the fact that hippocampal
2 CitethisarticleasColdSpringHarbPerspectBiol2015;7:a021808

PlaceCells,GridCells,andMemory
Grid Place
Figure1.Gridcellsandplacecells.(Left)Agridcellfromtheentorhinalcortexoftheratbrain.Theblacktrace
showsthetrajectoryofaforagingratinpartofa1.5-m-diameter-widesquareenclosure.Spikelocationsofthe
gridcellare superimposedin redonthetrajectory. Eachreddotcorrespondsto onespike. Blueequilateral
triangleshavebeendrawnontopofthespikedistributiontoillustratetheregularhexagonalstructureofthegrid
pattern.(Right)Gridcellandplacecell.(Top)Trajectorywithspikelocations,asintheleftpart.(Bottom)Color-
codedratemapwithredshowinghighactivityandblueshowinglowactivity.Gridcellsarethoughttoprovide
much,butnotall,oftheentorhinalspatialinputtoplacecells.
neuronsweresostronglymodulatedbylocation manysemantic memories (Buzsa´ki and Moser
suggestedthatspacewasprimary.Moreover,for 2013).
the most part, place cells represented current Aroleforplacecellsinhippocampalmem-
space,notasexpectedifthefunctionofthehip- orywasapparentalreadyintheearlieststudies
pocampus was purely mnemonic. Reconciling ofplacecells.Itwasshowninthesestudiesthat
spaceandmemory functionsremainedachal- ensembles of place cells represent not only the
lenge for several decades after the discoveryof animal’scurrentlocationbutalsolocationsthat
placecells. the animal had visited earlier. In maze tasks,
Aframeworkthataccountsforbothlinesof place cells fired when the animal made errors,
observationhasnowemerged.Convergingevi- asiftheanimalwasinthelocationwherethecell
dencehassuggestedthathippocampalneurons fired normally (O’Keefe and Speakman 1987).
respondalsotononspatialfeaturesoftheenvi- In spatial alternation tasks, firing patterns re-
ronment, such as odors (Eichenbaum et al. flectedlocationsthattheanimalcamefrom,as
1987; Wood et al. 1999; Igarashi et al. 2014), well as upcoming locations (Franket al. 2000;
tactile inputs (Young et al. 1994), and timing Woods et al. 2000; Ferbinteanu and Shapiro
(Hampsonetal.1993).Thesamecellsthatre- 2003),andduringsequentialtestinginmultiple
spond to nonspatial stimuli firelikeplace cells environments, place-cell activity was found to
when animals move around in space, suggest- carry over from one environment to the next
ing that place cells express the location of the (Leutgebetal.2004,2005a).Moreover,sequenc-
animalincombinationwithinformationabout es of spatial firing during exploration were
eventsthattakeplaceortookplacethere(Leut- showntobereplayedduringrestorsleepsubse-
gebetal.2005b;Moseretal.2008).Therepre- quent to the behavioral experience, as if those
sentationofspacedoesnotexcludeacentralrole patterns were stored in the hippocampal net-
of the hippocampus in declarative memory,as work during exploration and retrieved later in
space is a central element of all episodic and offlinemode,whentheanimalwasnotacquir-
CitethisarticleasColdSpringHarbPerspectBiol2015;7:a021808 3

M.-B.Moseretal.
ing new information (Pavlides and Winson pendentofatleastonemajorformoflong-term
1989; Wilson and McNaughton 1994; Foster synaptic plasticity. However, cellular mecha-
andWilson2006;O’Neilletal.2006). nismsinvolvedinlong-termplasticityareclear-
Thefactthatplacecellsexpresspastexperi- lyrequiredforthelong-termstabilityofnewly
ence raises the question whether ensembles of formed maps (Rotenberg et al. 1996; Kentros
placecellsarecompletelyformedbyexperience et al. 1998). These studies suggest that the
or if there is an underlying component that is place-cell map of the environment is stored
hardwiredin thecircuit.Hill(1978)soughtto and stabilized through changes in synaptic
address this issue by recording place fields as weights,similartoothermemorysystems(Kan-
ratsenteredanovelenvironment.Ofthe12cells delandSchwartz1982).
that he recorded, 10 appeared to have spatial NMDA receptors also play a role in more
firing fields immediately, supporting the idea subtle forms of experience-dependent modifi-
that the place-cell map was largely predeter- cations of place fields. One example is the ex-
mined. Subsequently, studies with larger en- perience-dependent asymmetric expansion of
sembles of cells found that place fields often placefieldsobservedfollowingrepeatedtravers-
tookseveralminutesofexplorationbeforeset- alsofplacefieldsonalineartrack(Mehtaetal.
tlingintoastablefiringfield(McNaughtonand 1997, 2000). It was suggested in theoretical
Wilson1993;Franketal.2004)andtheforma- studiesinthe1990sthatasaratmovesthrough
tion of newand stable place fields was depen- locations A, B, and C along a linear track, the
dentontheanimal’sbehaviorandattentionto cellscoding for location Awill repeatedlyacti-
thespatialfeaturesoftheenvironment(Kentros vatethecellscodingforlocationBandthecells
et al. 2004; Monaco et al. 2014). These results codingforlocationBwill,inturn,activatecells
pointtoacriticalroleforexperienceinforming codingforlocationC.BythelogicofHebbian
the hippocampal map of space. However, the plasticity, the connections from A to B and B
plasticitycanoccurextremelyrapidly(Leutgeb toCshouldbecomestrengthened,withthere-
et al. 2006) and, just as Hill observed, some sult that place fields of cells A, B, and C are
placecellsshowstablefiringfieldsimmediately shiftedforwardonthetrack,againstthedirec-
(Frank et al. 2004). Thus, place maps are ex- tion of motion (Abbott andBlum 1996; Blum
pressed, in someform,fromtheverymoment and Abbott 1996). Experimental evidence for
whenanimalsareputintoanenvironmentfor suchexperience-dependentasymmetricexpan-
thefirsttime,althoughthemapmayevolvefur- sion was obtained by Mehta and colleagues
therwithexperience.Thefindingsraisethepos- (1997,2000).Subsequently,studies found that
sibility that a skeletal map of a novel environ- theasymmetricshiftdependsonNMDArecep-
ment is drawn from a set of preexisting maps, toractivation(Ekstrometal.2001),consistent
and then gets modified to fit the specifics of withthesuggestionthatplacemapsarerefined
the environment through experience-depen- by experience-dependent long-term synaptic
dentplasticity(SamsonovichandMcNaughton plasticity.
1997;DragoiandTonegawa2011,2013).
Theroleofsynapticplasticityintheforma-
MEMORYENCODING
tion of place maps has been tested experi-
mentally. In agreement with the proposed ex- What are the factors that determine whether
istence of prewired maps, neither systemic newplacemapsarestabilized?Oneofthehall-
pharmacological blockade of N-methyl-D-as- marks of episodic memories is that attended
partate(NMDA)receptors,norsubfield-specif- information is more likely to be encoded and
ic targeted knockouts of such receptors, have stored long term (Chun and Turk-Browne
a large effect on the basic firing patterns of 2007).Itissimplyimpossibletorememberev-
place cells in familiar or novel environments erything,andasEbbinghaus’scurveofmemory
(McHughetal.1996;Kentrosetal.1998),sug- shows, most memories will fade over time.
gestingthatplace-fieldexpressionisquiteinde- However, some particularly meaningful mem-
4 CitethisarticleasColdSpringHarbPerspectBiol2015;7:a021808

PlaceCells,GridCells,andMemory
oriesbecomepermanent.Onthisbackground, MEMORYCONSOLIDATION
Kentrosetal.(2004)consideredwhetheratten- ANDRETRIEVAL
tiontospatialcuescouldimprovethelong-term
stability of place fields. They trained mice to Onceencoded,thememoriesmustbeconsoli-
find an unmarked goal location in a cylinder dated. In an early theoretical paper, Buzsa´ki
(similar to the Morris water maze) while re- (1989) proposed that hippocampal memory
cordinghippocampalplacecells.Themicethat formationoccursintwostages.First,thereisa
learned the task had more stable place fields stageinwhichmemoryisencodedviaweaksyn-
thanmicethatweresimplyrunninginthesame apticpotentiationintheCA3networkwhenthe
cylinder with no task requirements. To test networkisintheta-oscillationmodeduringex-
whetherthedrivingforcewastrueselectiveat- ploratory behavior. Then, there is a memory
tention,asopposedtogeneralarousal,Muzzio consolidationstage,whichcantakeplacehours
etal.(2009)trainedmicetoattendtoodorcues laterduringsharp-waveactivity,associatedwith
andignorespatialcuesorviceversa.Whenthe sleepandresting.Inthisstage,synapsesthatwere
odorsweretherelevantcues,thehippocampal weaklypotentiatedduringtheprecedingexplo-
neurons acquired stable odor representations, rationparticipateinsharp-waveactivitythat,in
but had less stable spatial representations. The turn,evokesrippleactivityintheCA1areaofthe
reversewastruewhenspacewasrelevant.Taken hippocampus.Ripplesoccuratafrequencythat
together with recent evidence suggesting that isoptimalforinductionoflong-termpotentia-
placefields can be induced byattentivescann- tion(LTP)inefferentsynapsesofCA1cells,pos-
ing(Monacoetal.2014),thefindingspointto siblyincludinglong-distancetargetsinthecor-
selective attention, and not merely general tex.Bythismechanism,memorywasthoughtto
arousal,asamajordeterminantofexperience- be slowly induced in the neocortex, consistent
dependent stabilization of hippocampal place withalargebodyofevidencepointingtogradual
maps. recruitment of neocortical memory circuits in
Whatcouldbethemechanismsforselective long-term storage of hippocampal memories
attentioninthehippocampus?Recently,Igara- (McClelland et al. 1995; Squire and Alvarez
shietal.(2014)recordedsimultaneously from 1995; Frankland et al. 2001). Over the years,
thelateralentorhinalcortexandCA1regionof considerableevidencehasaccumulatedtopoint
therathippocampusastheanimalslearnedan toaroleforsharpwavesandripplesinthefor-
odor–placeassociation.Astheanimalslearned mation of hippocampus-dependent long-term
the association, the two structures showed an memories. Selectively disrupting sharp-wave
increasingdegreeofsynchronousoscillatoryac- ripple activityduring posttraining rest periods
tivity in the 20- to 40-Hz range and a corre- impairs learning, providing a causal link be-
spondingincreaseinspikingactivitytothere- tween sharp-wave ripples and consolidation
warded odors. The development of temporal (Girardeauetal.2009;Ego-StengelandWilson
coherencebetweenactivityinthehippocampus 2010).Moreover,itisnowclearthatsequencesof
and entorhinal cortex may allow CA1 cells to firingamongplacecellsarereplayedduringsub-
respond to particular entorhinal inputs at the sequent sharp-wave ripples in the same or re-
sametimeasthecellsareclosesttofiringthresh- verseorderthatthecellswereactiveduringex-
old(Singer1993).The20-to40-Hzoscillation perience(WilsonandMcNaughton1994;Foster
issubstantiallylowerthanthefast (60-100Hz) and Wilson 2006; Diba and Buzsa´ki 2007).
gammaoscillationfoundinthemedialentorhi- Structuredreplayisseenacrossmanybrainre-
nalcortex(Colginetal.2009).Thetwosubdi- gions(HoffmanandMcNaughton2002),indi-
visionsoftheentorhinalcortexmay,therefore, cating that the sequence information from the
convey relevant information to the hippo- hippocampusmaybeconferredondownstream
campus via distinct frequency channels, each corticaltargets.
leading toadifferentfiring patterninthehip- Recentworkpointstoawiderroleforreplay
pocampus. inwhichreplaymaycontributenotonlytocon-
CitethisarticleasColdSpringHarbPerspectBiol2015;7:a021808 5

M.-B.Moseretal.
solidation and recall of memory, but also to thetimecourseofreactivationwassimilartoa
planningoffuturebehavior.Studiesinhuman typicalsharp-waverippleeventinrodents,and
subjects show that overlapping hippocampal maythereforereflectaqualitativelysimilarphe-
networks are activated during episodic recall nomenon.Theplacecellactivityduringrecallof
andimaginationoffictitiousexperiences(Has- eventsoritemslikelybringstomindthespatial
sabisetal.2007).Inanimals,sharp-waveripples contextinwhichtheeventsanditemswereex-
can activate cells along both past and future perienced,creatingafullyreconstructedmem-
trajectories (Karlsson and Frank 2009; Gupta oryforwhatwasexperienced,alongwithwhere
et al. 2010; Pfeiffer and Foster 2013). Pfeiffer itwasexperienced.
and Foster (2013), for example, trained rats to
findarewardedwellwithinalargeenvironment
UPSTREAMOFPLACECELLS:GRIDCELLS
whilesharp-waveripple-associatedreplayevents
ANDOTHERCELLTYPES
wererecordedinthehippocampus.Inmanyof
theevents,thesequenceofactivecellsbeganat To get a better insight into the mechanismsof
thecurrentlocationandendedatthegoalloca- memory formation in hippocampal place-cell
tion, followed by the animal taking the path circuits, it may pay off to consider how place
definedbytheplace-cellactivity.Althoughthe cellsinteractwithcellsinadjacentbrainsystems.
sequenceofactivatedcellsclearlyprecededbe- The origin of the place-cell signal was long
havior,thephenomenonalsodependedonpre- thought to be intrahippocampal, considering
viousexperiencewiththeenvironmentandthe thatearlyrecordingsupstreamintheentorhinal
rulesofthetask.Thus,thereplaycaneitherlead cortex showed only weak spatial modulation
orfollowthebehavioroncethemapofspaceis (Barnes et al. 1990; Quirk et al. 1992; Frank
established.Inthatsense,thereplayphenome- etal.2000).Attheturnofthemillennium,we
nonmaysupport“mentaltimetravel”(Sudden- startedaseriesofexperimentsaimedatlocaliz-
dorf and Corballis 2007) through the spatial ingthesourcesoftheplacesignal.First,weiso-
map, both forward and backward in time. latedtheCA1regionofthehippocampusfrom
Whetherthesharp-waveripple-mediatedreplay theearlierpartsofthehippocampalexcitatory
inratsrepresentsconsciousrecallisimpossible circuit, that is, the dentate gyrus and the CA3
to know, but observations in humans during (Brun et al. 2002). Activity was then recorded
free recall provide a clue (Gelbard-Sagiv et al. from the remaining CA1. Place cells were still
2008;Milleretal.2013).Milleretal.(2013),for present, suggesting that intrahippocampal cir-
example, recorded from the medial temporal cuitsarenotnecessaryforspatialsignalstode-
lobeofhumansubjectsastheynavigatedavir- velop. The findings pointed to direct inputs
tual town (the subjects were awaiting surgery from the entorhinal cortex as an alternative
forepilepsyand had electrodes placed in their source of incoming spatial information to the
medial temporal lobe to localize the origin of hippocampus.Thus,inasubsequentstudy,we
theseizures,affordingMilleretal.therareop- recorded directly from the entorhinal cortex,
portunitytorecordplacecellsinhumans).After not in the deep ventral areas where cells had
an initial familiarization period, subjects were been recorded in previous studies, but in the
askedtodeliveritemstooneofthestoresinthe dorsal partsthat projected directly to the hip-
townandwhenallthedeliverieswerecomplete, pocampal recording locationsusedbyO’Keefe
thesubjectswereaskedtorecallonlytheitems and others (Fyhn et al. 2004). Electrodes were
they delivered. Remarkably, the place cells re- placedinthemedialpartoftheentorhinalcor-
sponsive to the areawhere the itemwas deliv- tex. We found that many neurons in this area
ered became active during recall of the item, wereassharplymodulatedbypositionasplace
closely mirroringthereactivationofplacecells cells in the hippocampus. Entorhinal neurons
during replayevents in rodents. Although free had multiple firing fields with clear regions of
recallinhumans isnotlikely tocorrespondto silence between the fields. In a third study, we
sharp-waverippleevents(Watrousetal.2013), expandedthesizeoftherecordingenvironment
6 CitethisarticleasColdSpringHarbPerspectBiol2015;7:a021808

PlaceCells,GridCells,andMemory
to determine the spatial structure of the many etal.2006;Solstadetal.2006).Thesuggestion
firingfields(Haftingetal.2005).Themultiple wasthat,becausethewavelengthoftheindivid-
firing fields of individual entorhinal neurons ualgridpatternsisdifferent,thepatternscancel
formeda regularlyspacedtriangularorhexag- eachotherexceptatthecentralpeak,whichbe-
onal grid pattern, which repeated itself across comestheplacefieldofthereceivingcell(Fig.2).
theentireavailablespace.Wenamedthesecells Experimental observations have suggested
“gridcells.”Gridcellswereorganizedinanon- thatthemechanismsaremorecomplex,howev-
topographicmanner,muchlikeplacecells.The er.Ifplacecellsweregeneratedexclusivelyfrom
firing fields of neighboring grid cells were no gridcells,gridandplacecellswouldbeexpected
more similar than those of grid cells recorded toappearsimultaneouslyindevelopinganimals
at different brain locations. However, the scale or with afaster time course for grid cellsthan
ofthegridincreasedfromdorsaltoventralme- place cells. Recordings from rat pups suggest
dialentorhinalcortex(Fyhnetal.2004;Hafting that this is not the case (Langston et al. 2010;
etal.2005),suggestingthattheearliestrecord- Willsetal.2010).Whenpupsleavethenestfor
ingsintheentorhinalcortexhadmissedthegrid thefirsttimeat2–2.5weeksofage,sharpand
patternbecausetheperiodofthefiringpattern confinedfiringfieldsarepresentinalargepro-
wastoolargeforrepeatedfieldstobeobservedin portion of the hippocampal pyramidal-cell
conventionally sized recording boxes. The dis- population. In contrast, grid cells show only
coveryofgridcellswasfollowedbystudiesshow- weakly periodic fields at that age. Strong peri-
ing that these cellswerepart of awider spatial odicityisnotexpresseduntil3–4weeksofage.
network comprising other cell types as well, Thedelayedmaturationofthegridcellsoffersat
suchasheaddirection–modulatedcells(Sargo- leasttwointerpretations.First,weakspatialin-
linietal.2006)andcellsthatfirespecificallyalong putsmaybesufficientforplace-cellformation.
oneorseveralbordersofthelocalenvironment Sharplyconfinedfiringfieldsmaybegenerated
(bordercells) (Savelli et al. 2008; Solstad et al. by local mechanisms in the hippocampal net-
2008).Headdirectioncellshadpreviouslybeen work,suchasrecurrentinhibition(deAlmeida
observedinanumberofbrainsystems,fromthe etal.2009;MonacoandAbbott2011),Hebbian
dorsal tegmental nucleus in the brain stem to plasticity(Rollsetal.2006;SavelliandKnierim
the pre-and parasubiculum in the parahippo- 2010), oractive dendritic properties (Smith et
campal cortex (Ranck 1985; Taube et al. 1990; al.2013).Alternatively,placecellsmaybegen-
Taube2007).Bordercellsweredescribedatthe eratedfromotherclassesofspatiallymodulated
sametimeinthesubiculum(Barryetal.2006; cells,suchasbordercells,whichhaveadult-like
Leveretal.2009).Thus,bytheendofthefirst propertiesfromtheveryfirstdayofexploration
decadeofthenewmillennium,itwasclearthat outside the nest (Bjerknes et al. 2014). Retro-
place and grid cells were part of a diverse and grade labeling studies suggest that bordercells
entangled network of cell types with distinct haveprojectionstothehippocampusthatmay
functionsinspatialrepresentation. be equally dense as those from grid cells, al-
Howplacecellsareformedfromthediver- though the latter are more abundant (Zhang
sityofcelltypesremainstobedetermined.An etal.2013).Apotentialroleforbordercellsin
obviouspossibilityisthatplacecellsaregener- place-cell formation would be consistent with
atedbytransformationofspatialinputfromgrid earlymodels,suggestingthatplacecellsariseby
cells.Thepresenceofgridcellsinthesuperficial linear combination of inputs from cells with
layersoftheentorhinalcortex,themaincortical firing fields defined by their proximity to geo-
inputtothe hippocampus,ledinvestigatorsto metricboundaries(O’KeefeandBurgess1996;
proposethatplacefieldsformbylinearcombi- Hartley et al. 2000). Recordings in the medial
nation of periodic firing fields from grid cells entorhinal cortex have, so far, identified such
withacommoncentralpeak,butdifferentgrid cells only near the boundaries of the environ-
spacing and orientation (O’Keefe and Burgess ment (Solstad et al. 2008; Zhang et al. 2013;
2005; Fuhs and Touretzky 2006; McNaughton Bjerknes et al. 2014), suggesting that a contri-
CitethisarticleasColdSpringHarbPerspectBiol2015;7:a021808 7

M.-B.Moseretal.
Map #1 Map #2
+ +
– –
+ +
– –
Figure2.Schematicillustrationofhowperiodicgridcellscouldbetransformedtononperiodicplacecellsby
linearsummationofoutputfromgridcellswithoverlappingfiringfields,butdifferentspacingandorientation,
andhowdifferentialresponsesamongmodulesofgridcellsmightgiverisetoremappinginthehippocampus.
(Left)Map1,gridcellswithdifferentspacingconvergetogenerateplacecellsinasubsetofthehippocampal
place-cellpopulation.Eachgridcellbelongstoadifferentgridmodule.(Right)Map2,differentialrealignment
ofeachofthegridmapsinducesrecruitmentofanewsubsetofplacecells.(FromimagesinSolstadetal.2006
andFyhnetal.2007;modified,withpermission,fromtheauthorsandNaturePublishingGroup#2006and
2007,respectively.)
bution by these cells may be limited to place REMAPPINGANDMEMORY
cellswithperipheralfiringfields.
The exact function of different entorhinal Oneoftheeventsthatpointedtoplacecellsasan
celltypesinplace-cellformationremainstobe expression of declarative memory wasthe dis-
determined,butitisnotunlikelythatindividual coveryofremapping,orthefactthatanyplace
place cells receive inputs from both grid and cell is part of not one, but many independent
bordercells, possibly with grid cells providing representations.In1987,BobMullerandJohn
self-motion-based distance information and Kubiefoundthatplacecellscanaltertheirfiring
border cells providing position in relation to patterns in response to minor changes in the
geometricboundaries(Bushetal.2014;Zhang experimental task, such as alterations in the
etal.2014).Thestrongestinput mayoriginate shapeoftherecordingenclosure(Fig.3)(Muller
from grid cells, which, in the superficial layers andKubie1987;Bostocketal.1991).Placecells
ofthemedialentorhinalcortex,areseveraltimes may begin firing, stop firing, or change their
more abundant than border cells (Sargolini firinglocation.Thechangesareexpressedwidely
et al. 2006; Solstad et al. 2008; Boccara et al. acrosstheplace-cellpopulation,suchthatanew
2010).Undermostcircumstances,thetwoclas- map is installed foreach occasion. Remapping
sesofinputarelikelytobecoherentandredun- couldalsobeinducedbychangesinmotivation-
dant. If one is absent, the other may often be al state or behavioral context (Markus et al.
sufficienttogeneratelocalizedfiringinthehip- 1995;Franketal.2000;Woodetal.2000;Moita
pocampus. etal.2004).
8 CitethisarticleasColdSpringHarbPerspectBiol2015;7:a021808

White Black Black White
Light Dark A
11064 21 Hz 18 Hz 27 Hz A A B Rat 11554
CA3
t5c2 t5c2
22 Hz
11 Hz 12 Hz 22 Hz CA3 MEC
1 MEC 10 Hz
t6c1 t6c1 0.8
0.6
14 Hz 12 Hz 14 Hz 1 0.4
t6c3 t6c3 0.2
–1
1 m 1 m
The remapping experiments showed that 2007).Thediscoveryofremappingandtheun-
placecellsparticipateinmultiplespatialmaps. correlatednatureofplacemapswasimportant
Different maps could be recruited not only in becauseitshowedthatplacecellsparticipatein
differentenvironments,butalsowhenanimals multipleorthogonalrepresentations,asexpect-
aretestedunderdifferentconditionsinthesame ed if the hippocampus plays a role in accurate
location (Markus et al. 1995; Leutgeb et al. storageandretrievalofhigh-capacitydeclarative
2005b).Mapsfordifferentconditionsorplaces memory.Thenumberofplacemapsstoredinthe
wereoftencompletelyuncorrelated (globalre- hippocampusisnotknown,butifplacemapsare
mapping)(Leutgebetal.2004;Fyhnetal.2007), expressionsofindividualmemories,thatnum-
as if a pattern-separation process takes place bershouldbeverylarge.Remappingis,thus,a
when information enters the hippocampus necessityifplacecellsexpressmemories.
from the surrounding cortex (Marr 1971; Mc- Do spatial inputs from medial entorhinal
NaughtonandMorris1987;Leutgebetal.2004, cortex contribute to remapping in the hippo-
noitalerroc
laitapS
PlaceCells,GridCells,andMemory
B A′
×A′ ×
1 Hz
2 Hz
0
–0.2
1 2 3 4 5 6 7 8 9 1012 3 4 5 6 7 8 91011
Time (min)
Figure3.Remappinginplacecellsandgridcells.(Topleft)JohnKubieandBobMullerin1983.(Topright)
Color-codedfiringratemapforahippocampalplacecellfromanearlyremappingexperiment(purple,high
rate;yellow,lowrate).Thecellfiredatdifferentlocationsindifferentversionsoftherecordingcylinder,one
withablackcuecardandonewithawhitecuecard.(Bottomleft)Realignmentofentorhinalgridcellsunder
conditionsthat generate global remapping in the hippocampus. The rat wastested in boxes with square or
circularsurfaces.Theleftpanelshowscolor-codedratemapsforthreegridcells(t5c2,t6c1,andt6c3)(color
codedasinFig.1).Therightpanelshowscross-correlationmapsforpairsofratemaps(samegridcellsasin
theleftpanel;repeatedtrialsinAoronetrialinAandonetrialinB).Thecross-correlationmapsarecolor-
coded, with red corresponding to high correlation and blue to low (negative) correlation. Note that the
centerofthecross-correlationmapisshiftedinthesamedirectionandatasimilardistancefromtheorigin
in all three grid cells, suggesting that all grid cells in an ensemble respond coherently to changes in the
environmentverymuchunliketheremappingthatisobservedinthehippocampus.(Bottomright)Response
toachangeintheenvironment(darkness)inasimultaneouslyrecordedpairofgridandplacecells.(Topleft
photo courteously provided by John Kubie; top right image is modified from data in Bostock et al. 1991;
bottom image from Fyhn et al. 2007; reprinted, with permission, from the authors and Nature Publishing
Group # 2007.)
CitethisarticleasColdSpringHarbPerspectBiol2015;7:a021808 9

M.-B.Moseretal.
campus?Thefirstcluetotheunderlyingmech- cellsgiverisetoremappinginthehippocampus.
anism is that remapping is unique to the hip- Two classes of explanations were put forward
pocampus.Theorthogonalnatureofplace-cell when we observed that remapping in the hip-
mapsisnotsharedbyanyoftheknownspatial pocampusisaccompaniedbycoherentrealign-
celltypesupstreamofthehippocampus.Inthe ment in the grid-cell population (Fyhn et al.
hippocampus,andparticularlyintheCA3sub- 2007). The first class assumed a continuous
field,differentsubsetsoftheplace-cellpopula- map of space in the medial entorhinal cortex.
tion are active in different environments. The Inthisscenario,differentportionsofauniversal
overlapbetweenactivesubsetsintwoenviron- entorhinalmapwouldbeactivatedindifferent
ments is not larger than expected by chance environments. Different subsets of hippocam-
(Leutgeb et al. 2004). The apparent indepen- pal cells would be activated from independent
denceoftheplace-cellmapscontrastswiththe portions of the entorhinal map and global re-
functional rigidity of the grid-cell population mapping would be seen in the hippocampus.
(Fig. 2). Changes in the environment, which The second class of explanation assumes that
leadtoglobalremappinginthehippocampus, gridcellshaveamodularorganizationandthat
inducechangesinthefiringlocationsofsimul- differentmodulesofgridcellsrespondindepen-
taneouslyrecordedgridcells,butthesechanges dently to changes in the environment. Place
arealwayscoherentamongnumbersofgridcells cellswerethoughttoreceiveinputfromseveral
(Fyhnetal.2007).Amonggridcellswithsimilar modules.Differentialrealignmentacrossmod-
gridspacing,thefiringlocationsofthegridcells uleswouldleadtodifferentoverlapofincoming
shift in thexy plane from one environment to gridsignalsinhippocampaltargetcells;thesub-
theother,butthedistanceanddirectionofgrid setofhippocampalcellsactivatedbyentorhinal
displacements aresimilaracrossthe cellpopu- grid-cellinputswouldbeentirelydependenton
lation.Similarly,internalcoherenceisobserved thedifferenceinrealignmentbetweendifferent
in head direction and bordercells. When ani- modules.
malsaremovedfromonetasktoanother,head Subsequently, experimental studies have
directioncellsinthepresubiculumandanterior provided evidence for a modular organization
nuclei of the thalamus rotate coherently such of grid cells, consistent with the second expla-
that the magnitude of the difference in direc- nation (Stensola et al. 2012). For many years,
tionalpreferenceamonganypairofheaddirec- the low number of simultaneously recorded
tioncellsisretainedfromoneconditiontothe gridcellspreventedaclearanswertotheques-
next(Taubeetal.1990;TaubeandBurton1995; tionofwhethergridcellsweremodularornot,
Yoganarasimha et al. 2006). A similar spatial althoughearlystudiespointedinthatdirection
coherence is seen among border cells (Solstad (Barry et al. 2007). With a more than 10-fold
etal.2008).Pairsofcellsthatfirealongthesame increase in the number of grid cells from the
wallinoneenvironmentalsofirealongthesame sameanimal, it was possible to show that grid
wallinanotherenvironment;cellsthatfirealong cellsclusterintomoduleswithdistinctgridscale
opposite walls in one box fire along opposite andgridorientation(Stensolaetal.2012).Four
walls in another box. Changes in orientation modulescouldbedetectedinmostanimals,but
are coherent also across entorhinal cell types; thenumbermaybelarger,consideringthatonly
if border fields switch to the opposite wall, apartofthemedialentorhinalcortexwassam-
thisisaccompaniedbya180-degreechangein pled.Itwasnotonly thepropertiesofthegrid
theorientationofheaddirectioncells,aswellas patternthatdifferedbetweenmodules,howev-
grid cells (Solstad et al. 2008). Taken together, er;theyalsorespondedindependentlytochang-
these observations suggest that remapping is es in the environment (Stensola et al. 2012).
generated not in the entorhinal cortex, but in When the recording environment was com-
thehippocampusitself. pressed,changingitfromasquaretoarectan-
Thefindingsdonotruleout,however,that gle, grid cells in the module with the smallest
inputsfromrealignedorreorientedentorhinal grid spacing maintained their firing locations,
10 CitethisarticleasColdSpringHarbPerspectBiol2015;7:a021808

PlaceCells,GridCells,andMemory
whereas cells in the larger modules rescaled eachotherdependsstronglyonthestateoftheta
completely and consistently, firing at shorter and gamma oscillations, which, during active
spatialwavelengthsinthecompresseddirection, awake behavior, predominates frequency spec-
butmaintainingwavelengthsintheorthogonal trainbothregions(Buzsa´kietal.1983;Bragin
unaltered direction. The apparent indepen- etal.1995;ChrobakandBuzsa´ki1998;Csicsvari
dencebetweengridmodulescontrastswiththe etal.2003;Colginetal.2009).Thetaoscillations
strongcoherenceobservedinearlierrecordings aregenerallycoherentacrossmostoftheento-
fromgridcells(Fyhnetal.2007).Thedifference rhinal–hippocampal network, but the coher-
islikelytoreflectthefactthattheearlierrecord- ence of beta and gamma oscillations is more
ingswereallmadefromthesamelocationand, local and fluctuates at subsecond timescales
probably,mostlyfromasinglemodule. (Colgin et al. 2009; Igarashi et al. 2014). Such
Thenewdatasuggestthatmodulesrespond fluctuations may enable place cells to interact
with different degrees of displacement and re- withdifferententorhinalsubpopulationsatdif-
orientationwhenanimalsmovefromoneenvi- ferenttimes.Coincidenceofpre-andpostsyn-
ronment to another. Computational simula- apticactivitymaybeaprerequisitenotonlyfor
tionshaveshownthatindependentrealignment synapticstrengtheningofconnectionsbetween
infourorfewermodulesissufficienttogenerate entorhinal and hippocampal cell pairs (Singer
complete or global remapping in the hippo- 1993; Bi and Poo 1998), but also for pattern-
campus (Monacoand Abbott2011). Indepen- completion processes during retrieval of al-
dent responses among only a handful of grid ready-storedinformation.Whetheraplacecell
modules may be sufficient to create an enor- respondstoinputsfromgridorbordercellsmay
mous diversityof firing patterns in the hippo- changewith time, as may the influence of dif-
campusbecausethenumberofdisplacementsor ferent modules of grid cells. Recordings from
phasesthateachmodulemaytakeislarge.The CA1 and lateral entorhinal cortex suggest that
mechanismwouldbesimilartothatofacom- placecellsalsoresponddynamicallytononspa-
bination lock in which 10,000 combinations tialinputs,suchasodors,withlearnedrelation-
may be generated with only four modules of shipstolocationsintheenvironment (Igarashi
10 possible values each (Rowland and Moser et al. 2014). Beta and gamma oscillations may
2014),orthatofanalphabetinwhichallwords enableplacecellstorespondtemporarilytoin-
of a language can be generated by combining formationaboutthecontentoflocationsinthe
only30lettersorless.Theproposedmechanism spatialenvironment.
isonlyahypothesis,however.Whetherhippo-
campal remapping actually requires indepen-
CONCLUSION
dentrealignmentamonggridmodulesremains
tobedetermined.Itshouldalsobenotedthata Wehaveknownforalmostsixdecadesthatcer-
possibleconnectionbetweengridmodulesand taintypesofmemorydependonthehippocam-
remappingdoesnotruleoutrolesforothercell pus and surrounding areas. The discovery of
types, such as bordercells,in inducing hippo- placecellsshowedthatspaceisacriticalelement
campal remapping, although modular organi- oftheinformationthatisstoredandexpressed
zation has not yet been observed in anyof the byneuronsinthehippocampus;however,itis,
other functional cell populations (Giocomo perhaps,withstudiesofplacecellsattheensem-
etal.2014). ble or population level and interventions that
Finally,wewouldliketoemphasizethat,up selectivelychangesynapticplasticityinspecific
tothispoint,wehavemostlydiscussedtheen- braincircuits,thatthemechanismsofmemory
torhinal–hippocampalspacecircuitasifinter- processing have become accessible. Today, we
actions between cell types were constant over know that hippocampal networks can rapidly
time.However,theconnectivityofthisnetwork store a multitude of uncorrelated representa-
isdynamic(Buzsa´kiandMoser2013).Whether tions,apropertythatanyhigh-capacityepisod-
entorhinalandhippocampalneuronsinfluence ic memory network must have. We know that
CitethisarticleasColdSpringHarbPerspectBiol2015;7:a021808 11

M.-B.Moseretal.
placecellsareonlyoneelementofawidernet- BushD,BarryC,BurgessN.2014.Whatdogridcellscon-
work for spatial mapping. Place cells coexist tributetoplacecellfiring?TrendsNeurosci37:136–145.
with grid, head direction, and border cells, all
Buzsa´kiG.1989.Two-stagemodelofmemorytraceforma-
tion: A role for “noisy” brain states. Neuroscience 31:
likelytointeractwitheachothertoyieldaglobal
551–570.
representation of the animal’s changing posi-
Buzsa´kiG,MoserEI.2013.Memory,navigationandtheta
tion, which may be used to guide the animal rhythminthehippocampal-entorhinalsystem.NatNeu-
to particular locations in the environment. rosci16:130–138.
With a modularorganization of grid cells, the Buzsa´kiG,LeungLW,VanderwolfCH.1983.Cellularbases
ofhippocampalEEGinthebehavingrat.BrainRes287:
network may be able to generate not onlyone
139–171.
map of the external environment, but thou-
Chrobak JJ, Buzsa´ki G. 1998. Gamma oscillations in the
sands or millions. Whether and how these entorhinalcortexofthefreelybehavingrat.JNeurosci
mapscontributetodeclarativememoryremains 18:388–398.
to be determined, but the investigation of the ChunMM,Turk-BrowneNB.2007.Interactionsbetween
attentionandmemory.CurrOpinNeurobiol17:177–184.
hippocampal–entorhinal circuit is now at a
CohenNJ,SquireLR.1980.Preservedlearningandreten-
stageinwhich the computational mechanisms
tionofpatternanalyzingskillinamnesia:Dissociationof
underlyingspecificmemoryprocessesarefully
knowinghowandknowingthat.Science210:207–209.
addressable. ColginLL,DenningerT,FyhnM,HaftingT,BonnevieT,
JensenO,MoserMB,MoserEI.2009.Frequencyofgam-
maoscillationsroutesflowofinformationinthehippo-
REFERENCES campus.Nature462:353–357.
CorkinS.2002.What’snewwiththeamnesicpatientH.M.?
AbbottLF,BlumKI.1996.Functionalsignificanceoflong- NatureRevNeurosci3:153–160.
termpotentiationforsequencelearningandprediction.
CsicsvariJ,JamiesonB,WiseKD,Buzsa´kiG.2003.Mecha-
CerebCortex6:406–416.
nismsofgammaoscillationsinthehippocampusofthe
BarnesCA,McNaughtonBL,MizumoriSJ,LeonardBW,
behavingrat.Neuron37:311–322.
LinLH.1990.Comparisonofspatialandtemporalchar-
deAlmeidaL,IdiartM,LismanJE.2009.Theinput–output
acteristicsofneuronalactivityinsequentialstagesofhip-
pocampalprocessing.ProgBrainRes83:287–300. transformationofthehippocampalgranulecells:From
gridcellstoplacefields.JNeurosci29:7504–7512.
BarryC,LeverC,HaymanR,HartleyT,BurtonS,O’KeefeJ,
JefferyK,BurgessN.2006.Theboundaryvectorcorpcell DibaK,BuzsakiG.2007.Forwardandreversehippocampal
modelofplacecellfiringandspatialmemory.RevNeuro- place-cell sequences during ripples. Nat Neurosci 10:
sci17:71–97. 1241–1242.
BarryC,HaymanR,BurgessN,JefferyKJ.2007.Experience- Dragoi G, Tonegawa S. 2011. Preplayof future place cell
dependentrescalingofentorhinalgrids.NatNeurosci10: sequences by hippocampal cellular assemblies. Nature
682–684. 469:397–401.
BiGQ,PooMM.1998.Synapticmodificationsincultured DragoiG,TonegawaS.2013.Distinctpreplayofmultiple
hippocampalneurons:Dependenceonspiketiming,syn- novelspatialexperiencesintherat.ProcNatlAcadSci
apticstrength,andpostsynapticcelltype.JNeurosci18: 110:9100–9105.
10464–10472. EbbinghausH.1885.U¨berdasGeda¨chtnisUntersuchungen
BjerknesTL,MoserEI,MoserMB.2014.Representationof
zurExperimentellenPsychologie[Memory:Acontribution
geometricbordersinthedevelopingrat.Neuron82:71–
toexperimentalpsychology].vonDunckerandHumber,
78.
Leipzig,Germany.
BlumKI,AbbottLF.1996.Amodelofspatialmapformation
Ego-Stengel V, Wilson MA. 2010. Disruption of ripple-
inthehippocampusoftherat.NeuralComput8:85–93.
associatedhippocampalactivityduringrestimpairsspa-
BoccaraCN,SargoliniF,ThoresenVH,SolstadT,WitterMP,
tiallearningintherat.Hippocampus20:1–10.
MoserEI,MoserM-B.2010.Gridcellsinpre-andpara-
EichenbaumH,KupersteinM, FaganA, NagodeJ. 1987.
subiculum.NatNeurosci13:987–994.
Cue-sampling and goal-approach correlates of hippo-
BostockE,MullerRU,KubieJL.1991.Experience-depen-
campalunitactivityinratsperforminganodor-discrim-
dentmodificationsofhippocampalplacecellfiring.Hip-
inationtask.JNeurosci7:716–732.
pocampus1:193–205.
BraginA,Jando´G,Na´dasdyZ,HetkeJ,WiseK,Buzsa´kiG. EkstromAD,MeltzerJ,McNaughtonBL,BarnesCA.2001.
1995.Gamma(40–100Hz)oscillationinthehippocam- NMDA receptorantagonism blocks experience-depen-
pusofthebehavingrat.JNeurosci15:47–60. dent expansion of hippocampal “place fields.” Neuron
31:631–638.
BrunVH,OtnassMK,MoldenS,SteffenachHA,WitterMP,
MoserMB,MoserEI.2002.Placecellsandplacerecog- FerbinteanuJ,ShapiroML.2003.Prospectiveandretrospec-
nition maintained by direct entorhinal–hippocampal tive memory coding in the hippocampus. Neuron 40:
circuitry.Science296:2243–2246. 1227–1239.
12 CitethisarticleasColdSpringHarbPerspectBiol2015;7:a021808

PlaceCells,GridCells,andMemory
FosterDJ,WilsonMA.2006.Reversereplayofbehavioural KandelER,SchwartzJH.1982.Molecularbiologyoflearn-
sequencesinhippocampalplacecellsduringtheawake ing:Modulationoftransmitterrelease.Science218:433–
state.Nature440:680–683. 443.
FrankLM,BrownEN,WilsonM.2000.Trajectoryencoding KarlssonMP,FrankLM.2009.Awakereplayofremoteex-
inthehippocampusandentorhinalcortex.Neuron27: periences in the hippocampus. Nat Neurosci 12: 913–
169–178. 918.
FrankLM,StanleyGB,BrownEN.2004.Hippocampalplas- KentrosC,HargreavesE,HawkinsRD,KandelER,Shapiro
ticityacrossmultipledaysofexposuretonovelenviron- M,MullerRV.1998.Abolitionoflong-termstabilityof
ments.JNeurosci24:7681–7689. new hippocampal place cell maps by NMDA receptor
blockade.Science280:2121–2126.
FranklandPW,O’BrienC,OhnoM,KirkwoodA,SilvaAJ.
2001. a-CaMKII-dependent plasticity in the cortex is KentrosCG,AgnihotriNT,StreaterS,HawkinsRD,Kandel
requiredforpermanentmemory.Nature411:309–313. ER.2004.Increasedattentiontospatialcontextincreases
bothplacefieldstabilityandspatialmemory.Neuron42:
FuhsMC,TouretzkyDS.2006.Aspinglassmodelofpath
283–295.
integrationinratmedialentorhinalcortex.JNeurosci26:
Kjelstrup KB, Solstad T, Brun VH, Hafting T, Leutgeb S,
4266–4276.
WitterMP,MoserEI,MoserM-B.2008.Finitescalesof
FyhnM,MoldenS,WitterMP,MoserEI,MoserM-B.2004.
spatialrepresentationinthehippocampus.Science321:
Spatial representation inthe entorhinalcortex. Science
140–143.
305:1258–1264.
LangstonRF,AingeJA,CoueyJJ,CantoCB,BjerknesTL,
FyhnM,HaftingT,TrevesA,MoserM-B,MoserEI.2007. WitterMP,MoserEI,MoserM-B.2010.Developmentof
Hippocampalremappingandgridrealignmentinento- thespatialrepresentationsystemintherat.Science328:
rhinalcortex.Nature446:190–194. 1576–1580.
Gelbard-SagivH,MukamelR,HarelM,MalachR,FriedI. LashleyKS.1929.Brainmechanismsandintelligence:Aqual-
2008.Internallygeneratedreactivationofsingleneurons itativestudyofinjuriestothebrain.UniversityofChicago
inhumanhippocampusduringfreerecall.Science322: Press,Chicago.
96–101.
LashleyKS.1950.Insearchoftheengram.InSymposiumof
GiocomoLM,StensolaT,BonnevieT,VanCauterT,Moser the society for experimental biology, Vol. 4. Cambridge
M-B,MoserEI.2014.Topographyofheaddirectioncells UniversityPress,NewYork.
inmedialentorhinalcortex.CurrBiol24:252–262. Leutgeb S, Leutgeb JK, Treves A, Moser M-B, Moser EI.
GirardeauG,BenchenaneK,WienerSI,BuzsakiG,Zugaro 2004. Distinct ensemble codes in hippocampal areas
MB.2009.Selectivesuppressionofhippocampalripples CA3andCA1.Science305:1295–1298.
impairsspatialmemory.NatNeurosci12:1222–1223. LeutgebJK,LeutgebS,TrevesA,MeyerR,BarnesCA,Mc-
Gupta AS, van der Meer MA, TouretzkyDS, Redish AD. NaughtonBL,MoserM-B,MoserEI.2005a.Progressive
2010.Hippocampalreplay is not a simplefunctionof transformationofhippocampalneuronalrepresentations
experience.Neuron65:695–705. in“morphed”environments.Neuron48:345–358.
HaftingT,FyhnM,MoldenS,MoserM-B,MoserEI.2005. LeutgebS,LeutgebJK,BarnesCA,MoserEI,McNaughton
Microstructureofaspatialmapintheentorhinalcortex. BL, Moser M-B. 2005b. Independent codes for spatial
Nature436:801–806. andepisodicmemoryinhippocampalneuronalensem-
bles.Science309:619–623.
HampsonRE,HeyserCJ,DeadwylerSA.1993.Hippocam-
palcellfiringcorrelatesofdelayed-match-to-sampleper- LeutgebS,LeutgebJK,MoserEI,MoserMB.2006.Fastrate
formanceintherat.BehavNeurosci107:715–739. codinginhippocampalCA3cellensembles.Hippocam-
pus16:765–774.
HartleyT,BurgessN,LeverC,CacucciF,O’KeefeJ.2000.
Modelingplacefieldsintermsofthecorticalinputstothe LeutgebJK,LeutgebS,MoserMB,MoserEI.2007.Pattern
separationinthedentategyrusandCA3ofthehippo-
hippocampus.Hippocampus10:369–379.
campus.Science315:961–966.
HassabisD,KumaranD,MaguireEA.2007.Usingimagina-
LeverC,BurtonS,JeewajeeA,O’KeefeJ,BurgessN.2009.
tiontounderstandtheneuralbasisofepisodicmemory.J
Boundaryvectorcellsinthesubiculumofthehippocam-
Neurosci27:14365–14374.
palformation.JNeurosci29:9771–9777.
HebbDO.1949.Theorganizationofbehavior.Wiley,New
MarkusEJ,QinYL,LeonardB,SkaggsWE,McNaughton
York.
BL,BarnesCA.1995.Interactionsbetweenlocationand
HillAJ.1978.Firstoccurrenceofhippocampalspatialfiring taskaffectthespatialanddirectionalfiringofhippocam-
inanewenvironment.ExpNeurol62:282–297. palneurons.JNeurosci15:7079–7094.
HoffmanKL,McNaughtonBL.2002.Coordinatedreacti- MarrD.1971.Simplememory:Atheoryforarchicortex.
vationofdistributedmemorytracesinprimateneocor- PhilosTransRSocLondBBiolSci262:23–81.
tex.Science297:2070–2073.
McClellandJL,McNaughtonBL,O’ReillyRC.1995.Why
IgarashiKM,LuL,ColginLL,MoserM-B,MoserEI.2014. therearecomplementarylearningsystemsinthehippo-
Coordinationofentorhinal–hippocampalensembleac- campusandneocortex:Insightsfromthesuccessesand
tivityduringassociativelearning.Nature510:143–147. failuresofconnectionistmodelsoflearningandmemory.
JungMW,WienerSI,McNaughtonBL.1994.Comparison PsycholRev102:419–457.
ofspatialfiringcharacteristicsofunitsindorsalandven- McHughTJ,BlumKI,TsienJZ,TonegawaS,WilsonMA.
tralhippocampusoftherat.JNeurosci14:7347–7356. 1996.Impairedhippocampalrepresentationofspacein
CitethisarticleasColdSpringHarbPerspectBiol2015;7:a021808 13

M.-B.Moseretal.
CA1-specificNMDAR1knockoutmice.Cell87:1339– O’NeillJ,SeniorT,CsicsvariJ.2006.Place-selectivefiringof
1349. CA1pyramidalcellsduringsharpwave/ripplenetwork
McNaughtonBL,BattagliaFP,JensenO,MoserEI,Moser patternsinexploratorybehavior.Neuron49:143–155.
M-B.2006.Pathintegrationandtheneuralbasisofthe PavlidesC,WinsonJ.1989.Influencesofhippocampalplace
“cognitivemap.”NatureRevNeurosci7:663–678. cellfiringintheawakestateontheactivityofthesecells
MehtaMR,BarnesCA,McNaughtonBL.1997.Experience- duringsubsequentsleepepisodes.JNeurosci 9:2907–
dependent,asymmetricexpansionofhippocampalplace 2918.
fields.ProcNatlAcadSci94:8918–8921. Pfeiffer BE, Foster DJ. 2013. Hippocampal place-cell se-
MehtaMR,QuirkMC,WilsonMA.2000.Experience-de- quencesdepictfuturepathstorememberedgoals.Nature
pendent asymmetric shape of hippocampal receptive 497:74–79.
fields.Neuron25:707–715. Quirk GJ, Muller RU, Kubie JL, Ranck JB Jr. 1992. The
MillerJF,NeufangM,SolwayA,BrandtA,TrippelM,Mader positional firing properties of medial entorhinal neu-
I,HefftS,MerkowM,PolynSM,JacobsJ,etal.2013. rons: Description and comparison with hippocampal
Neuralactivityinhumanhippocampalformationreveals placecells.JNeurosci12:1945–1963.
thespatialcontext ofretrievedmemories.Science342: RanckJBJr.1973.Studiesonsingleneuronsindorsalhip-
1111–1114. pocampal formation and septum in unrestrained rats:
MilnerB,CorkinS,TeuberHL.1968.Furtheranalysisofthe I.Behavioralcorrelatesandfiringrepertoires.ExpNeurol
hippocampal amnesic syndrome: 14-year follow-up 41:461–531.
studyofH.M.Neuropsychologia6:215–234.
RanckJB.1985.Headdirectioncellsinthedeepcelllayerof
MishkinM.1978.Memoryinmonkeysseverelyimpairedby dorsalpresubiculuminfreelymovingrats.InElectrical
combinedbutnotbyseparateremovalofamygdalaand activity of the archicortex (ed. Buzsa´ki G, Vanderwolf
hippocampus.Nature273:297–298. CH),pp.217–220.AkademiaiKiado,Budapest.
MoitaMA, Rosis S,Zhou Y, LeDouxJE, Blair HT. 2004. RollsET,StringerSM,ElliotT.2006.Entorhinalcortexgrid
Putting fear in its place: Remapping of hippocampal cellscanmaptohippocampalplacecellsbycompetitive
place cells during fear conditioning. J Neurosci 24: learning.Network17:447–465.
7015–7023.
RotenbergA,MayfordM,HawkinsRD,KandelER,Muller
MonacoJD,AbbottLF.2011.Modularrealignmentofen-
RU. 1996. Mice expressing activated CaMKII lack low
torhinalgridcellactivityasabasisforhippocampalre-
frequencyLTPanddonotformstableplacecellsinthe
mapping.JNeurosci31:9414–9425.
CA1regionofthehippocampus.Cell87:1351–1361.
MonacoJD,RaoG,RothED,KnierimJJ.2014.Attentive
RowlandDC,MoserM-B.2014.Fromcorticalmodulesto
scanningbehaviordrivesone-trialpotentiationofhip-
memories.CurrOpinNeurobiol24C:22–27.
pocampalplacefields.NatNeurosci17:725–731.
Samsonovich A, McNaughton BL. 1997.Path integration
MoserEI,KropffE,MoserM-B.2008.Placecells,gridcells,
andcognitivemappinginacontinuousattractorneural
andthebrain’sspatialrepresentationsystem.AnnuRev
networkmodel.JNeurosci17:5900–5920.
Neurosci31:69–89.
SargoliniF,FyhnM,HaftingT,McNaughtonBL,WitterMP,
MullerRU,KubieJL.1987.Theeffectsofchangesinthe
MoserM-B,MoserEI.2006.Conjunctiverepresentation
environmentonthespatialfiringofhippocampalcom-
ofposition,directionandvelocityinentorhinalcortex.
plex-spikecells.JNeurosci7:1951–1968.
Science312:754–758.
MuzzioIA,LevitaL,KulkarniJ,MonacoJ,KentrosC,Stead
SavelliF,KnierimJJ.2010.Hebbiananalysisofthetransfor-
M,AbbottLF,KandelER.2009.Attentionenhancesthe
mationofmedialentorhinalgrid-cellinputstohippo-
retrievalandstabilityofvisuospatialandolfactoryrep-
campalplacefields.JNeurophysiol103:3167–3183.
resentations in the dorsal hippocampus. PLoS Biol 7:
e1000140. SavelliF,YoganarasimhaD,KnierimJJ.2008.Influenceof
boundaryremovalonthespatialrepresentationsofthe
O’KeefeJ.1976.Placeunitsinthehippocampusofthefreely
movingrat.ExpNeurol51:78–109. medialentorhinalcortex.Hippocampus18:1270–1282.
O’KeefeJ,BurgessN.1996.Geometricdeterminantsofthe ScovilleWB,MilnerB.1957.Lossofrecentmemoryafter
placefieldsofhippocampalneurons.Nature381:425– bilateralhippocampallesions.JNeurolNeurosurgPsychi-
428. atry20:11–21.
O’KeefeJ,BurgessN.2005.Dualphaseandratecodingin SingerW.1993.Synchronizationofcorticalactivityandits
hippocampalplacecells:Theoreticalsignificanceandre- putative role in information processing and learning.
lationshiptoentorhinalgridcells.Hippocampus15:853– AnnuRevPhysiol55:349–374.
866. SmithSL,SmithIT,BrancoT,Ha¨usserM.2013.Dendritic
O’KeefeJ,DostrovskyJ.1971.Thehippocampusasaspatial spikesenhancestimulusselectivityincorticalneuronsin
map.Preliminaryevidencefromunitactivityinthefree- vivo.Nature503:115–120.
ly-movingrat.BrainRes34:171–175. SolstadT,MoserEI,EinevollGT.2006.Fromgridcellsto
O’KeefeJ,NadelL.1978.Thehippocampusasacognitive place cells: A mathematical model. Hippocampus 16:
map.Clarendon,Oxford. 1026–1031.
O’KeefeJ,SpeakmanA.1987.Singleunitactivityintherat Solstad T, Boccara CN, Kropff E, Moser M-B, Moser EI.
hippocampusduringaspatialmemorytask.ExpBrain 2008.Representationofgeometricbordersintheento-
Res68:1–27. rhinalcortex.Science322:1865–1868.
14 CitethisarticleasColdSpringHarbPerspectBiol2015;7:a021808

PlaceCells,GridCells,andMemory
SquireLR.1992.Memoryandthehippocampus:Asynthesis WilsonMA,McNaughtonBL.1993.Dynamicsofthehip-
fromfindingswithrats,monkeys,andhumans.Psychol pocampalensemblecodeforspace.Science261:1055–
Rev99:195–231. 1058.
SquireLR,AlvarezP.1995.Retrogradeamnesiaandmemory WilsonMA,McNaughtonBL.1994.Reactivationofhippo-
consolidation:Aneurobiologicalperspective.CurrOpin campal ensemble memories during sleep. Science 265:
Neurobiol5:169–177. 676–679.
StensolaH,StensolaT,SolstadT,FrølandK,MoserM-B, WoodER,DudchenkoPA,EichenbaumH.1999.Theglobal
MoserEI.2012.Theentorhinalmapisdiscretized.Na- recordofmemoryinhippocampalneuronalactivity.Na-
ture492:72–78. ture397:613–616.
SuddendorfT,CorballisMC.2007.Theevolutionoffore- Wood ER, Dudchenko PA, Robitsek RJ, Eichenbaum H.
sight: What is mental time travel, and is it unique to 2000.Hippocampalneuronsencodeinformationabout
humans?BehavBrainSci30:299–313. differenttypesofmemoryepisodesoccurringinthesame
location.Neuron27:623–633.
Taube JS. 2007. The head direction signal: Origins and
YoganarasimhaD,YuX,KnierimJJ.2006.Headdirection
sensory-motorintegration.AnnuRevNeurosci30:181–
cellrepresentationsmaintaininternalcoherenceduring
207.
conflictingproximalanddistalcuerotations:Compari-
Taube JS, Burton HL. 1995. Head direction cell activity
sonwithhippocampalplacecells.JNeurosci26:622–631.
monitoredinanovelenvironmentandduringacuecon-
YoungBJ,FoxGD,EichenbaumH.1994.Correlatesofhip-
flictsituation.JNeurophysiol74:1953–1971.
pocampalcomplex-spikecellactivityinratsperforminga
TaubeJS,MullerRU,RanckJBJr.1990.Head-directioncells nonspatialradialmazetask.JNeurosci14:6553–6563.
recordedfromthepostsubiculuminfreelymovingrats:
ZhangSJ,YeJ,MiaoCL,TsaoA,CerniauskasI,Ledergerber
I.Descriptionandquantitativeanalysis. JNeurosci 10:
D,MoserM-B,MoserEI.2013.Optogeneticdissectionof
420–435.
entorhinal-hippocampalfunctionalconnectivity.Science
TolmanEC.1948.Cognitivemapsinratsandmen.Psychol 340:1232627.
Rev55:189–208.
ZhangS-J,YeJ,CoueyJJ,WitterMP,MoserEI,MoserM-B.
WatrousAJ,TandonN,ConnerCR,PietersT,EkstromAD. 2014.Functionalconnectivityoftheentorhinal-hippo-
2013.Frequency-specificnetworkconnectivityincreases campalspacecircuit.PhilosTransRSocLondBBiolSci
underlieaccuratespatiotemporalmemoryretrieval.Nat 369:20120516.
Neurosci16:349–356. Zola-MorganS,SquireLR,AmaralDG.1986.Humanam-
WillsTJ,CacucciF,BurgessN,O’KeefeJ.2010.Develop- nesiaandthemedialtemporalregion:Enduringmemory
mentofthehippocampalcognitivemapinpreweanling impairmentfollowingabilaterallesionlimitedtofield
rats.Science328:1573–1576. CA1ofthehippocampus.JNeurosci6:2950–2967.
CitethisarticleasColdSpringHarbPerspectBiol2015;7:a021808 15
