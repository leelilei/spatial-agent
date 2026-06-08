Title: A non-spatial account of place and grid cells based on clustering models of concept learning

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/papers/pdfs/06_Agent_Memory_Cognitive/07_Non_Spatial_Place_Grid_Cells_Love2019.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T03:07:56+00:00
- page_count: 9
- status: ok
- text_char_count: 52279

Metadata:
- author: Robert M. Mok
- doi: 10.1038/s41467-019-13760-8
- keywords: unknown
- subject: Nature Communications, doi:10.1038/s41467-019-13760-8

Outline:
- A non-spatial account of place and grid cells based on clustering models of concept learning (page 1)
  - Results (page 3)
    - A common learning mechanism for space and concepts (page 3)
    - Clustering solutions match grid patterns in mEC (page 3)
    - Cluster representations are shaped by environmental geometry (page 3)
  - Discussion (page 4)
  - Methods (page 6)
    - Simulations (page 6)
    - Simulation procedure and model specifications (page 6)
    - Assessing regularity of cluster positions (page 7)
    - Assessing change in gridness during and after learning (page 7)
    - Classification and percentage of grid cell-like maps (page 7)
    - Gridness in trapezoid environments (page 7)
    - Reporting summary (page 7)
  - Data availability (page 8)
  - References (page 8)
  - Acknowledgements (page 9)
  - Author contributions (page 9)
  - Competing interests (page 9)
  - Additional information (page 9)

Markdown Content:

ARTICLE
OPEN
https://doi.org/10.1038/s41467-019-13760-8
A non-spatial account of place and grid cells based
on clustering models of concept learning
Robert M. Mok 1* & Bradley C. Love 1,2*
Oneviewisthatconceptualknowledgeisorganizedusingthecircuitryinthemedialtemporal
lobe (MTL) that supports spatial processing and navigation. In contrast, we find that a
domain-general learning algorithm explains key findings in both spatial and conceptual
domains.Whentheclusteringmodelisappliedtospatialnavigationtasks,so-calledplaceand
gridcell-likerepresentationsemergebecauseoftherelativelyuniformdistributionofpossible
inputs in these tasks. The same mechanism applied to conceptual tasks, where the overall
space can be higher-dimensional and sampling sparser, leading to representations more
aligned with human conceptual knowledge. Although the types of memory supported by
the MTL are superficially dissimilar, the information processing steps appear shared. Our
account suggests that the MTL uses a general-purpose algorithm to learn and organize
context-relevant information in a useful format, rather than relying on navigation-specific
neural circuitry.
1DepartmentofExperimentalPsychology,UniversityCollegeLondon,26BedfordWay,LondonWC1H0AP,UK.2TheAlanTuringInstitute,London,UK.
*email:robert.mok@ucl.ac.uk;b.love@ucl.ac.uk
NATURECOMMUNICATIONS| (2019) 10:5685 |https://doi.org/10.1038/s41467-019-13760-8|www.nature.com/naturecommunications 1
;,:)(0987654321

C
onceptsorganizeexperiencestoenablegeneralizationand represent experience in terms of conceptual clusters, which are
inference. For example, a traveler encountering an unfa- not uniformly distributed17. For example, in a simple case with
miliar bird species would reasonably infer the bird was two clearly separable and internally coherent sets of objects, a
born from an egg. One longstanding question is the basis for clusteringmodelwoulduseoneclustertorepresenteachconcept,
people’sabstractconceptualknowledge.Oneintuitiveideaisthat each of which would be centered amidst its members in repre-
concepts ground in a more basic and concrete substrate, such as sentational space (e.g. Fig. 1a).
sensory-motor experience1. For example, abstract concepts such When the model is presented with a novel item, the closest
as time may be represented in terms of experience of space2. cluster in representational space is activated, which signals the
Relatedly,conceptualknowledgemaybeorganizedusingcircuitry category membership of the item. An error-monitoring signal
in the medial temporal lobe (MTL) that supports navigation3. gauges how well an item matches this closest cluster in repre-
This view is supported by recent studies that find the brain’s sentational space. In these models, only the closest cluster
responses to conceptual tasks parallel those previously found in maintains non-zero activation (winner-takes-all), so an error-
spatialtasks.Placecellsinthehippocampus4typicallyhavesingle monitoring signal (entropy term) ‘monitors’ activation of all
firing fields at circumscribed locations in a spatial environment, existingclusterswhichindicateshowcloseorfarawaythecurrent
and grid cells in the medial entorhinal cortex
(mEC)5–7
display locationwasfromanycluster,actingasaclustermatch(ornon-
multiple regularly-spaced firing fields arranged in a hexagonal match signal)17,18.
pattern covering the environment. These spatially-tuned cells in These clustering representations successfully capture patterns
the MTL are thought to implement a spatial cognitive map for ofactivityintheMTL19,20andareinaccordwiththenotionthat
navigation8–11,andrecentworksuggeststhesecellsalsorepresent
the human hippocampus contains concept cells in which indivi-
conceptual12 and task spaces13. One key question is whether the dual cells respond to a specific concept, much like how a cluster
same brain systems and computations support concept learning, in a possibly high-dimensional space can encode a concept21.
memory, and spatial navigation. Analogously,placecellsrespondtoalocationinaparticulartwo-
One neglected possibility is that the relation between spatial dimensional spatial context. It is important to note that clusters
and conceptual representations has been framed backwards. areabstractentitiesinthemodel,andthereneednotbeaone-to-
Perhaps, rather than concepts grounding in the machinery of onemappingtosingleconceptorplacecell(e.g.aclustercanbe
navigation, spatial concepts are a limiting case of a single, more represented by a group of place cells with similar tuning (c.f.
general,learningsystem.Suchalearningsystemwouldbetasked refs. 22)—a functional mapping of multiple place cells to one
with learning all relevant concepts, including those tied to phy- cluster, and the place cell population to the whole cluster repre-
sical space (also see refs. 14,15, and Discussion). This general sentation; Fig. 2c). Furthermore, clustering models explain how
learning system would support learning concepts, which are individual episodes give rise to conceptual knowledge over the
typically clumpy in that they consist of clusters of interrelated course of learning23, consistent with both the hippocampus’s
featuresinahigh-dimensionalspace16.Forexample,animalsthat importance in memory24,25. We evaluate whether the same
flytendtobesmallandhavewings(seeFig.1a).Notallpossible mechanisms alsoofferageneralunderstandingofplaceandgrid
combinations of features are relevant and represented. In con- cells, and their relationship to concepts.
trast,manyspatialtasks5andtheirconceptualanalogs12typically Tofacilitatethisevaluation,wesimplifiedtheclusteringmodels
involve a uniform and exhaustive sampling of all possible com- toonlyincludeaspectsnecessaryforthiscontribution.Clustering
binationswithinalow(two-)dimensionalspacecorrespondingto models that capture behavior on a trial-by-trial basis typically
locations in an environment (see Fig. 1c, d). recruit a new cluster in response to a surprising error. These
Weevaluatewhetheradomaingeneralaccountisplausibleby models also learn attention weights that accentuate task-relevant
applying successful models of human concept learning to spatial stimulus dimensions and associate clusters with behavioral
contexts. In concept learning studies, these models learn to responses (e.g., respond “bird”). Without loss of generality, we
A
Clustering concepts Clustering over navigated space
Size
B
Time Time
thgilF
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-13760-8
C
D
Fig.1Clusterlearningappliedtoconceptualandspatialexamples.aThemostsimilarclustermoves(i.e.,adjustsitstuning)towarditsnewestmember
andbecomesassociatedwitharesponse(blueforbird,redformammal).bOutofapoolofmanyrandomlytunedclusters,asubsetcomestorepresent
thetwoconceptsoverlearning.c,dThesamelearningsystemappliedtoanagentlocomotinginacircularorasquareenvironmentgivesrisetoa
hexagonalclusterorganization.Howthestimulusspaceissampledaffectshowclustersaredistributedintherepresentationalspace.
2 NATURECOMMUNICATIONS| (2019) 10:5685 |https://doi.org/10.1038/s41467-019-13760-8|www.nature.com/naturecommunications

ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-13760-8
A Results
Concept case after learning
A common learning mechanism for space and concepts. As
showninFig.1a,themodelwhenappliedtocategorizinganimals
as birds or mammals learns to segregate the items into two
groupings. These clusters can be seen as concept cells, akin to
Stimulus position
in representational space placecells(Fig.2a,b).Noticethattheitems(i.e.,experiences)and
theclustersonlycoveraselectportionofthestimulusspace.For
example, no animal exists that is as massive as an elephant and
can fly. Clustering solutions capture the structure of the envir-
Cluster activity ... onment, which enables generalization to novel cases.
In contrast, the same model applied to an agent exploring a
typical laboratory environment leads to clusters that uniformly
Cluster-match / covertheentirerepresentationalspaceinahexagonalpattern(see
error-monitoring Fig.1c,d).Inthespatialcase,thereisnosalientstructurepresent
in the input to the model, which results in clusters covering the
representational space, much like how a bunch of tennis balls
B
Spatial case after learning droppedintoasquareboxwillself-organizeintoagrid-likelattice
accordingtothemathematicsofpacking28–33.Inthespatialcase,
theclustersfunctioninasimilarwaytoapopulationofplacecells
Stimulus position
that code for (i.e., discriminate) locations.
in representational space
In our account, grid-like responses arise from monitoring the
match (inverse error) of the clustering solution (Fig. 2a, b). In
unsupervised learning, error or uncertainty is simply the inverse
Cluster activity
(akin to place cell responses) ... ofhowsimilaranitemistothebestmatchingcluster.Noticethat
matching clusters in the spatial case should display a hexagonal
patternbecauseofthehexagonalclusteringpatterninrepresenta-
Cluster-match / tional space, resulting in canonical grid-like receptive fields (see
error-monitoring Fig. 2b). In the conceptual case, we predict that typical grid cell
akin to grid/spatial cell firing patterns should not be observed because the clusters (i.e.,
place cells) do not form a hexagon pattern (Fig. 2a) in
C representational space. One might object that our account is
Abstract cluster representations are
inconsistent with conceptual learning brain imaging studies that
encoded by multiple neurons
find grid-like response patterns12. However, these studies are
Hippocampus Medial Entorhinal Cortex consistent with the model because they follow the design
principles of typical spatial studies—all feature combinations
withina2-dimensionalstimulusspacearesampled,whichwould
lead to a hexagonal clustering solution (Fig. 2b).
ClusteringsolutionsmatchgridpatternsinmEC.Torelateour
account to typical spatial studies, we simulated an agent moving
through itsenvironment as in a free-foraging rodentexperiment.
Asexpected,learningled toclustersforminga hexagonalpattern
(see examples in Fig. 3a, b, left). To assess this quantitatively, we
computed the spatial autocorrelograms of the cluster activation
maps(Fig.3a,b,right)toobtainthegridscore,whichreflectsthe
Fig.2Clusterrepresentationsafterlearningforconceptualandspatial
degree six-fold hexagonal symmetry in the cluster activation
tasks.aClustersclumpintotwogroups.Thus,novelbirdandmammal
patternacrosstrials5(seeMethods).Wecomputedgridscoresfor
stimuliwillstronglyactivateoneortheothergrouping,whichdoesnotlead
eachtimebinduringlearningandfoundthatgridscorestendedto
toagridresponseacrosspossiblestimuli.bIncontrast,forthespatialcase,
increaseoverlearninginboththesquare(seeFig.3cforexamples
clustersformahexagonalgridwhichleadstoagrid-likeresponseacross
and Fig. S1 for all conditions; mean slope: 0.0044, bootstrap CIs:
possiblestimuliwhenclusteractivityismonitored.cClustersdeterminethe
receptivefieldsforapopulationofplaceorconceptcells,andthecluster- [0.0040, 0.0048]) and circular environment (mean slope: 0.0042,
monitoring/error-monitoringmechanism(gridorspatialcells)reflectthe bootstrap CIs [0.0038, 0.0046]; see TablesS1 and S2).
Followinglearning,weevaluatedthegridnessoftheclustering
distributionoftheclusters.Abstractclusterrepresentationsareinstantiated
solution (see examples in Fig. 3a, b and Figs. S2 and S3). A
bymultiplecellsinthehippocampusandmedialentorhinalcortex(mEC)
withsimilarfiringfieldstorepresentthesamelocation(orconcept)inthe substantial proportion of simulations satisfied the criterion for
grid-likeorganization,with45.3%inthesquareand38.6%inthe
caseofhippocampalcellsorclustermatchinthecaseofmECcells.
circular environment, which closely match the proportions in
empirical results (45% and 38%, respectively; see Supplementary
simplified the models by pre-seeding with a fixed number of Note 1)34,35. The average grid score in both the square
environment (mean: 0.277, bootstrap CIs [0.273, 0.0.280]) and
clusters and limiting learning to updating cluster positions. In
circular environment (mean: 0.313, bootstrap CIs [0.309, 0.318])
particular, the cluster most similar to the current stimulus
were greater than zero; see Tables S3 and S4).
updated its position in representational space to be closer (more
similar)toitsnewestmember(seeMethodsforfulldetails),much
like cluster updating in Kohonen learning maps26 and k-means Clusterrepresentationsareshapedbyenvironmentalgeometry.
clustering27. According to the clustering account, grid-like responses should
NATURECOMMUNICATIONS| (2019) 10:5685 |https://doi.org/10.1038/s41467-019-13760-8|www.nature.com/naturecommunications 3

101112131415161718192021222324252627282930
Number of Clusters
only arise under very specific conditions in which the environ- task-relevant feature space captures conceptual structure in
mentisfairlyuniform.Theimpositionofanystructure,including concept learning tasks and spatial structure in two-dimensional
changestotheoverallgeometryoftheenvironment,shouldaffect navigation contexts, which lead to place and grid cell-like
the clustering in a manner that makes it less grid-like. representations. Rather than spatial mechanisms providing a
Related,Krupicetal.36identifiedgridcellsinrodentmECina scaffolding for more abstract conceptual knowledge3,10, the cur-
square box, then placedthe animals in a trapezoid environment. rent results suggest that key findings in the spatial literature
They found that activity maps of grid cells became less grid-like naturally arise as limiting cases of a more general concept
in the trapezoid and that the decline was greatest for responses learning mechanism. Whereas concepts can be clumpy, struc-
elicited on the narrow side of the trapezoid. To simulate this tured, and high dimensional, typical spatial tasks involve
experiment, the model was first trained in a square and then exhaustive and uniform sampling of simple two-dimensional
transferred to a trapezoid environment (see Fig. 4a–d for an environments,whichleadstodegenerateclusteringsolutionsthat
example and Fig. S4 for more examples). As in the empirical pack clusters into a hexagon lattice, giving rise to so-called grid
studies, the model’s overall grid scores declined in the trapezoid cells (Fig. 3). The clustering account correctly predicted how
environment(Fig.4e;trapezoidmeangridscore:0.058,bootstrap deviationsfromtheseunstructuredlearningenvironmentsshould
CIs [0.054, 0.061]; Fig. 4f; square minus trapezoid mean: 0.219, reduce grid-like cell responses (Fig. 4).
bootstrap CIs [0.214, 0.224]) and the grid scores were higher on Ourproposalstandsincontrasttootherideasthatadedicated,
the wide than on the narrow side of the trapezoid (Fig. 4g; wide phylogenetically older spatial navigation system in the MTL
minus narrow mean: 0.133, bootstrap CIs [0.127, 0.139]; see supports the newer, higher-level cognitive functions3,10. In par-
Tables S5–S7). ticular,wesuggesttherearenointrinsic‘place’or‘grid’cells,but
insteadaflexiblesystemthatwillrepresenttherelevantvariables
athand,including physicalspace. Emergingevidenceshows that
Discussion cellsintheMTLexhibitmixed-selectivityinthattheyrespondto
Previous work has explained a wide array of learning and multiple variables, such as place and grid cells that also code for
memory phenomena in terms of clustering computations sup- task-relevant sound frequency13, routes37,38, objects and con-
ported by the MTL23. Here, this same basic account was shown text39, and time40, suggesting a flexible code. Clustering is a
to account for basic spatial navigation phenomenon, including flexible mechanism and can learn representations in multi-
placeandgridcell-likeresponsepatterns.Specifically,weshowed dimensional space, and therefore is a strong candidate mechan-
that a learning mechanism that seeks to minimize error in the ism for organizing multi-modal, complex information for
erocS
dirG
1 1 1 1
0.5 0.5 0.5 0.5
0 0 0 0
-0.5 -0.5 -0.5 -0.5
101112131415161718192021222324252627282930
Circular Environment
erocS
dirG
A B C Learning over time
10 clusters 12 clusters 18 clusters 25 clusters
g = 0.48 g = 0.63
Square
10
g = 0.80 g = 1.04 Circle
12 Time (20 time bins)
D
Square Environment
g = 0.83 g = 0.81
18
g = 0.71 g = 0.84
20
g = 0.67 g = 0.61 E
23
g = 0.72 g = 0.66
25
erocS
dirG
erocS
dirG
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-13760-8
1
0.5
0
-0.5
1
0.5 0
-0.5
1.4
1.2
1
0.8
0.6
0.4
0.2
0
-0.2
-0.4
1.4
1.2
1
0.8
0.6
0.4
0.2
0
-0.2
-0.4
Fig.3Clusteringleadstoactivationmapssimilartospatialcellsinmedialentorhinalcortex.a,bExamplesofactivationmapswithgridpatternsina
squareenvironment(A-left)andtheircorrespondingspatialautocorrelograms(A-right),andactivationmapsinacircularenvironment(B-left),andspatial
autocorrelograms(B-right).cExamplesshowinggridscoresincreasingoverlearninginthesquare(top)andcircle(bottom).d,eUnivariatescatterplots
showinggridscoresforsimulationsinthesquare(d)andcircle(e).Dashedlinerepresentsthemostconservativethresholdfora‘gridcell’.
4 NATURECOMMUNICATIONS| (2019) 10:5685 |https://doi.org/10.1038/s41467-019-13760-8|www.nature.com/naturecommunications

A B g = -0.15 C D
g = 0.58 g = 0.35
Square-Trapezoid Wide-Narrow half of Trapezoid
101112131415161718192021222324252627282930 101112131415161718192021222324252627282930 101112131415161718192021222324252627282930
Number of Clusters
consolidation of knowledge for memories and concepts. A information in mEC can be used to generalize to different con-
growingbodyofworksupportstheideathattheMTLsystemisa textswithsharedstructure.Inouraccount,conceptualknowledge
key part of a general learning system for organizing knowledge and its structure is represented in the hippocampus, and any
into a useful representation, which can be used for effective generalization to new instances from existing structure is from
behavior and for memory consolidation. hippocampal representations (as generalization is performed in
Clustering models organize information and represent con- clustering models of concept learning). In contrast to the view
cepts in feature space to enable the identification, classification, thathippocampalrepresentationsarisefrominteractionsbetween
and generalization of novel objects17,18. These models can be mEC and lEC, we argue for a central role of prefrontal cortex
closelylinkedtoepisodicmemory23andaccountsofhippocampal (representation of the task or relevant features) for shaping
functionincludingrelationalmemory41,statisticallearning42,and hippocampal representations19, in combination with sensory
transitionstatistics(successorrepresentation14,43–45),withobjects
inputs arriving via entorhinal and perirhinal cortex, and from
or memories arranged in the form of a cognitive map. anterior inferior temporal cortex to prefrontal cortex47,48 to the
Several recent accounts have proposed different mechanisms hippocampus.
for the hippocampal-entorhinal cell circuit in organizing non- Whereas our account holds that place and grid cells emerge
spatial information10,14,15. One major feature that distinguishes fromagenerallearningsystem,Bellmundandcolleaguessuggest
ouraccountistheroleofplaceandgridcells.Inouraccount,the that the population code of place and grid cells play a role in
hippocampusplaysacentralroleinorganizinginformationabout mapping the dimensions of cognitive spaces in cognitive tasks,
the current environment or task, and the mEC monitors these and that spatial navigation could serve as a model system to
hippocampal representations. As such, mEC cells do not play a understandcognitivespaces10(alsoseeref.3).Althoughthereare
representational role, but play a role in learning—monitoring commonalities, their proposal suggests that place and grid cells
error from existing clusters in order to update the cluster repre- provideora‘metric’ordistancecodeforabstractspaces,andthat
sentation. Both grid and non-grid spatial cells contribute to this thereisastraightforwardmappingfromneuralrepresentationsof
function,andthehighgridnessofasubsetofthesecellsisaresult physical space to abstract space. In our view, when the context
of the environment or space. involves a significant degree of selective attention to stimulus
Other accounts hold that grid cells are key representational features or task variables, the representational space can be
units in the cognitive map. For example, Stachenfeld and col- warpedtoadifferent,moreeffectiverepresentationofthecontext
leagues14 suggested that place cells encode predictions of future at hand (e.g. reducing dimensionality by attending to the task-
states, and grid cells encode a low-dimensional decomposition relevantdimensions49),whichdoesnotsimplymapontothetwo-
of this hippocampal predictive map that may be useful for sta- dimensional spatial case.
bilizing the map and representing sub-goals. In contrast, we Our higher-level account provides a general theoretical fra-
suggest that place cells (clusters) are the key representational meworkapplicabletoalargerangeoftasks,incontrasttolower-
units which encode locations in representational space and its level models of place and grid cells which make specific predic-
structure, whereas grid cells monitor place cell activity. Behrens tions in spatial contexts but have less explanatory power to
and colleagues15,46 proposed that the hippocampal-entorhinal generalizeacrosscontexts.Ourmodel’scontributionisproviding
circuit learns and represents structural knowledge useful for ageneralmechanismthatcouldbeusedacrossdomains.Here,we
generalization. This account assumes objects are represented in provided an algorithmic-level model50 that links across two dif-
lateral EC (lEC), structure is represented in mEC, and the hip- ferent computational accounts of task descriptions (spatial and
pocampusencodesconjunctionsofthetwo.Thelearntstructural concept tasks), and connects learning mechanisms from concept
erocS
dirG
ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-13760-8
E F G
Trapezoid environment
1.4 2 2
1.2
1.5 1.5
1
0.8 1 1
0.6 0.5 0.5
0.4
0.2 0 0
0 -0.5 -0.5
-0.2 -1
-1
-0.4
-1.5
-0.6 -1.5
Fig.4Theclusteringmodelcapturesdeclinesingridresponsesintrapezoidenvironments.a–dExampleofdistortioninatrapezoidenvironment.
aExampleofanactivitymapinatrapezoidenvironmentwith18clusters.Thedottedlinedemarcatesthewideandnarrowhalvesofthetrapezoid.bSpatial
autocorrelogramofthetrapezoid.cSpatialautocorrelogramsofthewide(left)anddnarrow(right)portionofthetrapezoidina.eUnivariatescatterplot
showinggridscoresforsimulationsinthetrapezoidenclosureafterlearninginasquareenclosure.fThedifference(positive)betweengridscoresinthe
squareandtrapezoid.gThedifference(positive)betweengridscoresforthewideandnarrowhalvesofthetrapezoid.
NATURECOMMUNICATIONS| (2019) 10:5685 |https://doi.org/10.1038/s41467-019-13760-8|www.nature.com/naturecommunications 5

ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-13760-8
learning to spatial representations found at the single-cell level. When error is low, this signifies a good match between the
Specifically, we were able to link the model representations to environment and one’s current knowledge (cluster representa-
neural measures reported in the spatial literature, closely tion) and experience, and little or no update is necessary. Inac-
matching a number of empirical observations. tivating the mEC should disrupt the error signal, which should
Our model showed a similar proportion of grid-like cells in disrupt learning in new environments. Recent evidence suggests
foundinmEC.Othermodelseitherdonotcapturethehexagonal
placeandgridcellsbothmovetowardsgoalsorrewards57–59,and
code14 (90 degree grids) or need to build in additional con- there seems to be a greater number of place cells recruited near
straints32 (non-negativity constraint changes the 90 degree grid goal locations60,61 consistent withmore clustersmoving towards
patterns to 60 degree grid patterns). When they find a large the goal or more clusters recruited at locations near the goal.
proportionofgridcells,theyaretoogoodinthatallthesimulated Finally, our model predicts that both grid and non-grid spatial
cells are grid cells32,51. Other work have modeled or analyzed cells should perform the same function, in both concept and
mathematicalpropertiesofthegridcode(e.g.refs.31,33),butalso spatialtasks.Thereissomeevidenceinthespatialdomainwhich
donotaccountforvariabilityinthegridscoreinmECcells.Here, showedthatnon-gridspatialcellsinmECcontainasmuchspatial
we used a simple model from a high-level perspective based on information as grid cells and could serve similar functions62.
ideas from concept learning and memory and matched the pro- The primary strength of our account, namely that it offers an
portion of grid cells with empirical data, suggesting that the algorithmic account of spatial and concept learning tasks, serves
constraints of the clustering model matches the constraints the to highlight the need for complementary lower-level accounts.
brain uses to build these representations. There are various open questions such as how place cell remap-
Ourmodelalsocapturedthecausalrelationbetweenplaceand ping occurs across contexts and partial remapping effects with
gridcells.Inouraccount,gridcellsplayacluster-matchorerror- disruption to mEC63,64. Our hope is that our model can even-
monitoring function where they monitor (connected to and tually link to lower-level models that incorporate biological
receive input from) place cells, and self-organize over time to details suchas spiking neurons and incorporateknowledge from
produce a hexagonal firing pattern. This is consistent with memory research that can explain more empirical findings and
developmental work52,53, where place cells appear in baby rats provide new insights to these questions. Accounts are needed at
very early in life, and grid cells develop shortly after, as they multiplelevelsofanalysis.Weviewourmodelasintermediary(at
explore and learn about spatial environments during normal thealgorithmiclevel)andaimforittoserveasabridgebetween
development. Furthermore, inactivation of the hippocampus the goal of the computation and its implementation. Our model
(withplacecells)leadstogridcellsinmEClosingtheperiodicity can serve as a guide for howoperations suchas cluster updating
oftheirfiringfields54,whereasinactivationofthemEC(withgrid are physically realized.
cells) only mildly affect hippocampal place fields55. Our account Buildingthisintegrativebridgebetweentheconcept,memory,
provides a different way of thinking about hippocampal-mEC and spatial literatures allows for findings from one domain to
interactions, which makes predictions that can guide future inform the other. For example, task goals and attentional
experiments and analyses. mechanisms in the concept literature have been found to shape
Our account suggests that grid-like responses from the MTL hippocampalrepresentations19,20.Analogoustaskscanreadilybe
should be the exception, not the rule, when encoding abstract constructed to evaluate whether spatial cells support broader
spaces. Outside the typical laboratory study, representational information processing functions (cf. ref. 13) and how general
spacesmaybehighdimensionalandnotalldimensionsorvalues learning algorithms shape their response properties (cf. ref. 14).
along dimensions will be equally relevant, nor will all combina- Likewise, the concept literature emphasizes the hippocampus’s
tion of values across dimensions (see Fig. 1a). In support of this interactions with other brain areas, such as medial prefrontal
characterization, empirical work has shown that grid cells also cortex, to assist in encoding task relevant information19. When
lose their grid-like properties in more complex environments richer spatial tasks are considered, there is a ready set of candi-
such as mazes56. date mechanisms and neural systems that may offer domain
Our account made several predictions that matched empirical general explanations that link across brain, behavior, and
data, where changes in environmental geometry lead to specific computation.
changes in the cluster representation. The model also provides
further predictions. First, the mapping from place to grid cells
Methods
within a context should be predictable. An mEC grid or spatial
Simulations.Asimulationruncomprisedofalearningperiodwithamilliontrials
cell is assumed to receive input from multiple place cells in the (trainingphase)whereclustersupdatedtheirpositionsinrelationtotheagent’s
hippocampus, and that mEC cell should have fields in the same positionasitexploredtheenvironment.Afterlearning,wequantitativelyassessed
location as the place cells it receives input from (Fig. 2a, b). theregularityoftheclusterpositionarrangements(testphase).Weran
Therefore, if place cells that represent a certain location are 1000simulationrunsforeachcondition(numberofclusters).
inactivated, the corresponding fields of the mEC cells that
monitorthoseplacecellsshouldalsodisappear.SinceanmECcell Simulationprocedureandmodelspecifications.Atthebeginningofthelearning
may receive inputs from multiple place cells, a strict test would phaseofeachsimulationrun,wesetthenumberofclusters,numberoflearning
requireinactivationofall(oratleastalargeproportionof)place trials,theenvironment(square,circle),thelearningrate,andthelearningupdate
batchsize.Thenumberofclusterswereset(rangingfrom10to30)andwere
cells that represent one location (a cluster in the model), pre-
initiatedatrandomlocationsintheenvironment.Theshapeoftheenvironment
dicting all mEC cells should also lose those fields. Future work wasdefinedbyasetofpointsthatcouldbevisitedbytheagent.Thesquare
with large-scale concurrent recordings in multiple brain regions environmentwas50by50,whereeachpointwasalocationspecifiedbyavalueon
with specific (e.g. optogentic) manipulation may allow these thex-andy-axis.Thecircularenvironmentwasdefinedbydrawingacirclein
Matlabwitharadiusof50,andselectingthepointswithintheboundsofthecircle.
predictionstobetested.Onenovelpredictionofourmodelisthat
Thestartingpositionandmovementtrajectoryoftheagentwasthendeterminedas
whenerrorishighearlyinlearningforaparticularlocation,mEC
arandomwalkoveronemilliontrials.Theagentstartedatarandompositionand
cells should show a low firing rate and that best matching place stepsinthehorizontalandverticalaxeswerecomputedseparately.Oneachtrial,
cellsshouldupdatetheirtuningstomorestronglyrespondatthat theagentcouldgoup,down,orstayontheverticalaxis,andleft,right,orstayon
thehorizontalaxis.Thestepwassampledfrom[−4,−2,−1,−1,0,1,1,2,4],
location(i.e.,clusterupdating).Updatingacluster(orrecruitinga
wherenegativevaluesarestepstotheleft,positivestepsarestepstotheright,and
new cluster) should result in adjustment to the tuning of neigh-
zeromeansstay.Movementontheverticaldimensionwasdeterminedinthesame
boringclusters,leadingtoacascadeofchangesacrossplacecells. way,butnegativevalueswereupwardstepsandpositivevaluesweredownwards
6 NATURECOMMUNICATIONS| (2019) 10:5685 |https://doi.org/10.1038/s41467-019-13760-8|www.nature.com/naturecommunications

ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-13760-8
steps.Ifthegeneratedstepbroughttheagentoutoftheenvironment,thestepwas 200betavalues.Wecomputedthemeanandbootstrapped95%confidence
cancelledandanewstepwasgeneratedasabove. intervals(CIs)overallconditionsandsimulationrunstotestifthegridscore
Weconsideredasimplewinner-take-allnetworkinwhichonlytheclusterat increasedovertime.Wealsocomputedthemeanandbootstrapped95%CIsover
positionpos closesttostimulusx(agent’slocation)hadanon-zeroactivation. the200betavaluesforeachcondition.
i
Boldtypeisreservedforvectors.Thedistancebetweenpos andxisdefinedas: Toassessgridnessattheendoflearning,anewmovementtrajectorywas
i
generatedwith100,000trialsandclusterpositionswerefixed.Gridscoreafter
dist ¼kpos (cid:2)xk ð1Þ
i i learningwasassessedforall1000simulationruns.Theactivationsandnormalized
IntheKohonenlearningrule,clusteriupdatesitspositionpos tomovetoward activationmapwerecomputedoveralltesttrials,theactivationmapwassmoothed
stimulusxaccordingto:
i (Gaussiankernel,SD=1)andthespatialautocorrelogramoftheactivationmap
wascomputedfollowingHaftingetal.5,exceptfiringrateswerereplacedwith
Δpos
i
¼η
t
(cid:3)ðx(cid:2)pos
i
Þ; ð2Þ
normalizedclusteractivationvaluesateachlocation.Gridscoreswerethen
whereη isthelearningrateattimet.Inthepresentsimulations,weusedbatch computedbasedonthespatialautocorrelogramsusingEq.(5).Wecomputedthe
updating t toincreasenumericalstabilityinwhich200updateswereperformed meangridscoresandbootstrap95%CIsoverallconditionsandsimulationruns.
simultaneously.Thelearningrateηforbatchtimetfollowedanannealing Wealsocomputedthemeanandbootstrap95%CIsovereachcondition.
schedule:
η
η t ¼ 1þ 0 ρ(cid:3)t ; ð3Þ Classificationandpercentageofgridcell-likemaps.Toassesswhetheracti-
vationmapsshowedaregularhexagonalpatternthatwouldbeclassifiedasa‘grid
whereη
0
istheinitiallearningratesetto0.25andρistheannealingratesetto0.02. cell’accordingtocriteriasetinempiricalstudies,andtocomparethepercentageof
grid-likeactivationmapsfromourclusteringmodeltothepercentageofgridcells
Assessingregularityofclusterpositions.Toassesswhetherclusterpositions
foundinthemEC,weusedashufflingproceduretofindthestatisticalthresholdof
formedaregularhexagonalstructurewithlearninginacomparablemannerwayto
thegridscorethatpassesthecriterionfora‘gridcell’describedinWillsetal.52.
gridcellsfoundinthemedialentorhinalcortex(mEC),wefollowedthemethodof Theprocedurewasperformedonspatialautocorrelogramsoftheactivation
Haftingetal.5andPerez-Escobaretal.35. mapsproducedonthetestphase,whereclusterpositionswerefixed.Sincecluster
InHaftingetal.5,rodentstraversedcircularandsquareenvironmentswhilst activationsweregeneratedinrelationtotheagent’slocationduringmovement,
theyrecordedelectrophysiologicalsignalsfrommECneurons.Theyfoundcells theyweretemporallycorrelated.Therefore,tobreakthelocation-activation
thatdisplayedmultiplefiringfieldsandresembledagridofregularlytessellating relationship,thevectorofactivationswererandomlyshuffledintime,andwe
trianglesspanningtherecordedenvironment.Toassessthisregularity ensuredthateachlocationwasatleast20trialsfromitsoriginalposition.The
quantitatively,theycomputedthespatialautocorrelogramofthefiringratemap.If activationmapwassmoothed(Gaussiankernel,SD=1)thenthegridscorewas
thefieldswerearrangedinaregulargrid,thecenterpeakoftheautocorrelogram computed.Foreachcondition,thisshufflingprocedurewasperformed500times
shouldbesurroundedbysixequidistancepeaks,formingaregularhexagon.The
oneachsimulationrun(onasubsetof200simulations).Thethresholdwasdefined
spatialautocorrelogramwascomputedasfollows.Withλ ðx;yÞdenotingthe asthe95thpercentileofthe500shuffledgridscores,giving200thresholdvalues
clusteractivationatlocationðx;yÞ,theautocorrelationwith 1 spatiallagsofτ andτ (fromeachsimulationrun)percondition(numberofclusters).Thehighest
x y
wasestimatedas: thresholdvalue(mostconservative)wasusedasthethresholdforeachcondition.
P Inthefigureinthemaintext(Fig.3d,e),thethresholdsplottedarethehighest
n P λ 1 ðx;y P Þλ 2 ðx(cid:2)τ x ;y(cid:2)τ y Þ (mostconservative)thresholdsacrossallconditionsinthatparticularenvironment.
(cid:2) λ ðx;yÞ λðx(cid:2)τ ;y(cid:2)τ Þ Foreachcondition,wecomputedthepercentageofactivationmapsthat
rðτ x ;τ y Þ¼
qffiffiffiPffiffiffiffiffiffiffiffiffiffiffi
q
ffiffiffiffiffi
ffi
n ffi
ffi
ffi
ffi P
ffi
ffi
ffi
ffi1
ffi
ffiffi
ffi
ffi
ffi λ
ffi
ffi
ffi
ffi1
ffi
ffi
ffi
ffi ð
ffi
ffi
ffi
ffi x
ffi
ffi
ffi
ffi
ffi
; ffi
ffi
ffi
ffi
ffi y
ffi
ffi
ffi
ffi Þ
ffi
ffi
ffi
ffi 2
ffi
ffi
ffi
ffi
2ffi
ffi (cid:2)
ffi
ffi
ffi
ffi
ffi
ffi
ffi
ffi ð
ffi
ffi
ffi
ffi
P ffi
ffi
ffi
ffiP
ffi
ffi
ffi
ffi
ffi
ffi λ ffi
ffi
ffi
ffix
ffi
ffi
1ffi
ffi
ffi
ffi
ð ffi
ffi
x
ffi
ffi
ffi
ffi
ffi
ffi ;
ffi
ffi
ffi
ffi y
ffi
ffi
ffi
ffi Þ
ffi
ffi
ffi
ffi Þ
ffi
ffi
yffi
ffi 2
ffi
ffi
ffi
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
; ð4Þ
m
c
e
e
x
e
l
c
l
a
e
s
n
’
ed
fo
p
e
r
e
d
r
e
c
t
a
h
e
c
n
e
h
t
s
a
h
c
g
o
u
e
n
f
a
fl
d
c
e
i
r
t
d
o
io
s
g
n
s
ri
c
(
d
o
n
n
u
sc
d
m
o
it
r
b
i
e
o
er
n
th
s
o
.
r
f
es
c
h
lu
o
s
l
t
d
e
.
rs
W
)
e
se
c
p
o
a
m
ra
p
te
u
l
t
y
ed
an
t
d
he
th
p
e
e
n
rc
c
e
o
n
m
ta
p
g
u
e
t
o
ed
f‘
t
g
h
r
e
id
´ n λ ðx(cid:2)τ ;y(cid:2)τ Þ2(cid:2)ð λðx(cid:2)τ ;y(cid:2)τ ÞÞ2
2 x y 2 x y
whererðτ ; τ Þistheautocorrelationbetweenbinsoffsetofτ andτ,λ ðx;yÞand
x y x y 1
λðx;yÞareequivalentforanautocorrelationindicatestheaveragefiringrateofthe Gridnessintrapezoidenvironments.Tosimulatetheeffectofasymmetric
ce 2 llineachlocationðx;yÞ,andnisthenumberofspatialbinsoverwhichthe boundariesinatrapezoidenclosureongridness36,wetookclusterpositionsfrom
estimationwasmade. simulationsafterlearninginsquareenvironments,andrananadditionallearning
Toquantifythedegreeofthisregularity,a‘gridscore’iscommonlyused35by phasefor250,000trials.Inthisnewlearningphase,theshapeoftheenvironment
computingthecorrelationbetweenthecenterregionofthespatialautocorrelogram wasnowatrapezoid(theagentcouldonlymovetothoselocations),andthe
(amaskedregionincludingthesixsurroundingpeaksbutexcludingthecentre annealedlearningrateschedulecontinued(startingat0.0025,reducingto0.002at
peak)anda60°and120°rotatedversion(toassessthesix-foldhexagonal theend).Thetrapezoiddimensionswere5×24×50pixels,closelymatchingthe
symmetry)minusthecorrelationbetweenthespatialautocorrelogramsanda30°, proportionsin36(0.2×0.9×1.9meters;multipliedby(50/1.9)equalsto5.26,23.7,
90°,and150°rotatedversion(wherethereshouldbealowcorrelation): and50).
Inordertotestwhethertheasymmetricboundariesofthetrapezoidaffected
ðr
60(cid:4)
þr
120(cid:4)
Þ
(cid:2)
ðr
30(cid:4)
þr
90(cid:4)
þr
150(cid:4)
Þ
ð5Þ gridness,thetrapezoidwassplitintotwohalvesandwecomputedthegridscorefor
2 3 thespatialautocorrelogramontheleft(wide)andright(narrow)sideoftheshape.
Toassesstheregularityoftheclusterpositionsinagivenenvironmentinthe Duetodiscretization,wesplititasclosetoequalaspossible.Thewidehalf
currentstudyandcompareourresultswithempiricalfindings,wefollowedthe extendedfromtheleftmostpixelstothe17thpixel(338pixels),andthenarrow
methoddescribedabove.Wefirstcomputedactivationmapstoemulatefiringrate sideextendedfromthe18thpixeltothe50thpixel(339pixels).
mapsinempiricalneuronalrecordings,andcomputedthespatialautocorrelogram Duetotheasymmetricalshapeofthetrapezoidenvironment,theprocedurefor
toobtainthegridscore. generatingamovementtrajectoryaboveleadstoaslightlybiasedsamplingofthe
widepartofthetrapezoid,andlessexplorationofthemiddleandtoppartsofthe
Assessingchangeingridnessduringandafterlearning.Tocharacterizehow shape.Todealwiththis,wemadeaslightchangetothepossiblestepsafter
generatingastepthatbringstheagentoutoftheenvironment,describedbelow.For
clusterpositionschangedovertimeinthelearningphase,activationmapswere
eachtrial,thestepwasgeneratedasbefore.Ifthegeneratedstepwasoutofthe
computedovertrialsduringlearninginasetof200simulationruns.Trialswere
environment,thestepwascancelled,andthenextstepwasdeterminedasfollows.If
binnedinto20equallyspacedtimebinswith50,000trialsineachtimebin.We
thestepgeneratedwouldhavebroughttheagentoutofthebottomofthetrapezoid,
assumedthattheactivationstrengthofthewinningclusterwasaGaussianfunction
thenextstepwassampledfrom[0,0,1,1](stayorup).Ifthestepbringstheagent
ofdistancefromtheagent:
outtothetop,thenextstepwassampledfrom[−1,−1,0,0](downorstay).When
act i ¼pffi 2 1ffiffi π ffiffi 2 ffiffie(cid:2)1 2dist2 i ; ð6Þ t s h am es p t l e e p d t o a n ke t s he th h e o a r g iz e o n n t ta o l u a t x o is f w th e e re le [ f 0 t , o 1 f , t 1 h , e 2 t , r 4 a ] p , e t z o o w id a , rd th s e t n he th in e n n e e r x p t o s r t t e i p on to of be the
whereact i isclusteri’sactivationstrength.Tocomputeactivationmapsforeach e n n e v x i t ro st n e m p e w n a t s .I g f e t n h e e ra s t t e e d p a t s oo b k ef t o h r e e, a f g r e o n m to [− ut 4 o , f − t 2 h , e − ri 1 g , h − ts 1 i , d 0 e , o 1 f , t 1 h , e 2 t , r 4 a ] p . e T zo h i i d s , i t s he
timebin,activationswerecomputedateachlocationandnormalizedbythe
becausewhentheagentisoutofthetrapezoidonthehorizontal(left-right)axis,
numberofvisitsbytheagent(asdoneinempiricalstudies)tocreateanormalized
activationmap.Themapsweresmoothed(Gaussiankernel,SD=1),spatial theagentcouldstillbeinthemiddleoftheshapeontheverticalaxis,sincethe
shapebecomesmorenarrowasitreachestheright.Finally,whenitlandsexactlyin
autocorrelogramswerecomputed,andgridscoreswerecomputedforeachtime
bin.Astheclustersmovedcontinuouslyovertime(notdefinedbythetimebins), t
n
h
e
e
xt
m
s
i
t
d
e
d
p
le
to
of
b
t
e
h
s
e
a
h
m
o
p
ri
l
z
e
o
d
n
f
t
r
a
o
l
m
axi
o
s
n
,b
t
u
h
t
e
is
ve
o
r
u
ti
t
c
o
a
f
l
t
a
h
x
e
is
sh
is
ap
[−
e(
1
o
,
n
0,
th
1
e
].
horizontalaxis),the
activationmapschangedovereachtimebin.
Totestwhethergridnessincreasedovertime,weusedalinearmodeltoestimate
theslope(betavalue)ofthegridscoreofactivationmapsovereachtimebin
(20bins)foreachsimulationrunduringthelearningphase.Foreachcondition Reportingsummary.Furtherinformationonresearchdesignisavailablein
(numberofclusters),weestimatedtheslopefor200simulationruns,giving theNatureResearchReportingSummarylinkedtothisarticle.
NATURECOMMUNICATIONS| (2019) 10:5685 |https://doi.org/10.1038/s41467-019-13760-8|www.nature.com/naturecommunications 7

ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-13760-8
Code and data availability 32. Dordek,Y.,Meir,R.&Derdikman,D.Extractinggridcharacteristicsfromspatially
Allsimulationcodeandplottingscriptsareavailableathttps://github.com/robmok/ distributedplacecellinputsusingnon-negativePCA.Elife5,e10094(2016).
code_gridCell.Datageneratedandusedforthismanuscriptisavailableathttps://osf.io/ 33. Wei,X.-X.,Prentice,J.&Balasubramanian,V.Aprincipleofeconomy
2dz3x/. predictsthefunctionalarchitectureofgridcells.Elife4,e08362(2015).
34. Krupic,J.,Burgess,N.&O’Keefe,J.Neuralrepresentationsoflocation
composedofspatiallyperiodicbands.Science337,853–857(2012).
Received: 5October 2018; Accepted: 24November 2019;
35. Perez-Escobar,J.A.,Kornienko,O.,Latuske,P.,Kohler,L.&Allen,K.Visual
landmarkssharpengridcellmetricandconfercontextspecificitytoneurons
ofthemedialentorhinalcortex.Elife5,e16937(2016).
36. Krupic,J.,Bauza,M.,Burton,S.,Barry,C.&O’Keefe,J.Gridcellsymmetryis
shapedbyenvironmentalgeometry.Nature518,232–235(2015).
References 37. Wood,E.R.,Dudchenko,P.A.,Robitsek,R.J.&Eichenbaum,H.
1. Barsalou,L.W.Groundedcognition.Annu.Rev.Psychol.59,617–645(2008). Hippocampalneuronsencodeinformationaboutdifferenttypesofmemory
2. Boroditsky,L.Metaphoricstructuring:understandingtimethroughspatial
episodesoccurringinthesamelocation.Neuron27,623–633(2000).
metaphors.Cognition75,1–28(2000). 38. Grieves,R.M.,Wood,E.R.&Dudchenko,P.A.Placecellsonamazeencode
3. Buzsáki,G.&Moser,E.I.Memory,navigationandthetarhythminthe routesratherthandestinations.Elife5,e15986(2016).
hippocampal-entorhinalsystem.NatureNeuroscience16,130–138(2013). 39. Keene,C.S.etal.Complementaryfunctionalorganizationofneuronalactivity
4. O’Keefe,J.&Nadel,L.TheHippocampusasaCognitiveMap.(Oxford patternsintheperirhinal,lateralentorhinal,andmedialentorhinalcortices.J.
UniversityPress,Oxford,1978).
Neurosci.36,3660–3675(2016).
5. Hafting,T.,Fyhn,M.,Molden,S.,Moser,M.B.&Moser,E.I.Microstructure 40. Eichenbaum,H.Ontheintegrationofspace,time,andmemory.Neuron95,
ofaspatialmapintheentorhinalcortex.Nature436,801–806(2005). 1007–1018(2017).
6. Doeller,C.F.,Barry,C.&Burgess,N.Evidenceforgridcellsinahuman 41. Eichenbaum,H.&Cohen,N.J.FromConditioningtoConsciousRecollection:
memorynetwork.Nature463,657–661(2010). MemorySystemsoftheBrain.(OxfordUniversityPress,Oxford,2001).
7. Horner,A.J.,Bisby,J.A.,Zotow,E.,Bush,D.&Burgess,N.Grid-like 42. Schapiro,A.C.,Rogers,T.T.,Cordova,N.I.,Turk-Browne,N.B.&Botvinick,
processingofimaginednavigation.Curr.Biol.26,842–847(2016). M.M.Neuralrepresentationsofeventsarisefromtemporalcommunity
8. Tolman,E.C.Cognitivemapsinratsandmen.Psychol.Rev.55,189–208 structure.Nat.Neurosci.16,486–492(2013).
(1948). 43. Dayan,P.Improvinggeneralizationfortemporaldifferencelearning:the
9. Epstein,R.A.,Patai,E.Z.,Julian,J.B.&Spiers,H.J.Thecognitivemapin
successorrepresentation.NeuralComput.5,613–624(1993).
humans:spatialnavigationandbeyond.Nat.Neurosci.20,1504–1513(2017). 44. Momennejad,I.&Howard,M.W.Predictingthefuturewithmulti-scale
10. Bellmund,J.L.S.,Gärdenfors,P.,Moser,E.I.&Doeller,C.F.Navigating successorrepresentations.Preprintathttps://www.biorxiv.org/content/
cognition:spatialcodesforhumanthinking.Science362,eaat6766(2018). 10.1101/449470v1(2018).
11. Burgess,N.,Maguire,E.A.&O’Keefe,J.Thehumanhippocampusandspatial 45. deCothi,W.&Barry,C.Neurobiologicalsuccessorfeaturesforspatialnavigation.
andepisodicmemory.Neuron35,625–641(2002). Preprintathttps://www.biorxiv.org/content/10.1101/789412v1(2019).
12. Constantinescu,A.O.,O’Reilly,J.X.&Behrens,T.E.J.Organizingconceptual 46. Whittington,J.C.etal.TheTolman-EichenbaumMachine:Unifyingspace
knowledgeinhumanswithagridlikecode.Science352,1464–1468(2016). andrelationalmemorythroughgeneralisationinthehippocampalformation.
13. Aronov,D.,Nevers,R.&Tank,D.W.Mappingofanon-spatialdimensionby Preprintathttps://www.biorxiv.org/content/10.1101/770495v2(2019).
thehippocampal-entorhinalcircuit.Nature543,719–722(2017). 47. Catani,M.,Howard,R.J.,Pajevic,S.&Jones,D.K.Virtualinvivointeractive
14. Stachenfeld,K.L.,Botvinick,M.M.&Gershman,S.J.Thehippocampusasa
dissectionofwhitematterfasciculiinthehumanbrain.Neuroimage17,77–94
predictivemap.Nat.Neurosci.20,1643–1653(2017). (2002).
15. Behrens,T.E.J.etal.Whatisacognitivemap?Organizingknowledgefor 48. Martino,J.etal.Cortex-sparingfiberdissection:animprovedmethodforthe
flexiblebehavior.Neuron100,490–509(2018). studyofwhitematteranatomyinthehumanbrain.J.Anat.219,531–541
16. Rosch,E.&Mervis,C.B.Familyresemblances:studiesintheinternal (2011).
structureofcategories.Cogn.Psychol.7,573–605(1975). 49. Nosofsky,R.M.Attention,similarity,andtheidentification-categorization
17. Love,B.C.,Medin,D.L.&Gureckis,T.M.SUSTAIN:anetworkmodelof relationship.J.Exp.Psychol.Gen.(1986).
categorylearning.Psychol.Rev.111,309–332(2004). 50. Love,B.C.Thealgorithmiclevelisthebridgebetweencomputationandbrain.
18. Anderson,J.R.Theadaptivenatureofhumancategorization.Psychol.Rev.98,
Top.Cogn.Sci.7,230–242(2015).
409–429(1991). 51. Krupic,J.,Bauza,M.,Burton,S.,Lever,C.&O’Keefe,J.Howenvironment
19. Mack,M.L.,Love,B.C.&Preston,A.R.Dynamicupdatingofhippocampal geometryaffectsgridcellsymmetryandwhatwecanlearnfromit.Philos.
objectrepresentationsreflectsnewconceptualknowledge.Proc.NatlAcad.Sci. Trans.R.Soc.BBiol.Sci.369,20130188(2014).
113,13203–13208(2016). 52. Wills,T.J.,Cacucci,F.,Burgess,N.&O’Keefe,J.Developmentofthe
20. Davis,T.,Love,B.C.&Preston,A.R.Learningtheexceptiontotherule:
hippocampalcognitivemapinpreweanlingrats.Science328,1573–1576(2010).
model-basedfMRIrevealsspecializedrepresentationsforsurprisingcategory 53. Wills,T.J.,Barry,C.&Cacucci,F.Theabruptdevelopmentofadult-likegrid
members.Cereb.Cortex22,260–273(2012). cellfiringinthemedialentorhinalcortex.Front.NeuralCircuits6,21(2012).
21. QuianQuiroga,R.Conceptcells:thebuildingblocksofdeclarativememory 54. Bonnevie,T.etal.Gridcellsrequireexcitatorydrivefromthehippocampus.
functions.Nat.Rev.Neurosci.13,587–597(2012). Nat.Neurosci.16,309–317(2013).
22. Quiroga,R.Q.,Kreiman,G.,Koch,C.&Fried,I.Sparsebutnot 55. Hales,J.B.etal.Medialentorhinalcortexlesionsonlypartiallydisrupt
‘Grandmother-cell’codinginthemedialtemporallobe.TrendsCogn.Sci.12, hippocampalplacecellsandhippocampus-dependentplacememory.Cell
87–91(2008). Rep.9,893–901(2014).
23. Mack,M.L.,Love,B.C.&Preston,A.R.Buildingconceptsoneepisodeata 56. Derdikman,D.etal.Fragmentationofgridcellmapsinamulticompartment
time:Thehippocampusandconceptformation.Neurosci.Lett.680,31–38 environment.Nat.Neurosci.12,1325–1332(2009).
(2017). 57. Dupret,D.,O’Neill,J.,Pleydell-Bouverie,B.&Csicsvari,J.Thereorganization
24. Nadel,L.&Moscovitch,M.Memoryconsolidation,retrogradeamnesiaand andreactivationofhippocampalmapspredictspatialmemoryperformance.
thehippocampalcomplex.Curr.Opin.Neurobiol.7,217–227(1997). Nat.Neurosci.13,995–1002(2010).
25. Tulving,E.&Markowitsch,H.J.Episodicanddeclarativememory:roleofthe 58. Boccara,C.N.,Nardin,M.,Stella,F.,O’Neill,J.&Csicsvari,J.Theentorhinal
hippocampus.Hippocampus8,198–204(1998). cognitivemapisattractedtogoals.Science363,1443–1447(2019).
26. Kohonen,T.Self-organizedformationoftopologicallycorrectfeaturemaps. 59. Butler,W.N.,Hardcastle,K.&Giocomo,L.M.Rememberedrewardlocations
Biol.Cybern.43,59–69(1982). restructureentorhinalspatialmaps.Science363,1447–1452(2019).
27. Lloyd,S.P.LeastsquaresquantizationinPCM.IEEETrans.Inf.Theory28, 60. Hollup,S.A.,Molden,S.,Donnett,J.G.,Moser,M.B.&Moser,E.I.
129–137(1982). Accumulationofhippocampalplacefieldsatthegoallocationinanannular
28. Hales,T.etal.AformalproofoftheKeplerconjecture.ForumMath.Pi5,
watermazetask.J.Neurosci.21,1635–1644(2001).
1–29(2017). 61. Hok,V.etal.Goal-relatedactivityinhippocampalplacecells.J.Neurosci.27,
29. Du,Q.,Faber,V.&Gunzburger,M.CentroidalVoronoitessellations:
472–482(2007).
applicationsandalgorithms.SIAMRev.41,637–676(1999). 62. Diehl,G.W.,Hon,O.J.,Leutgeb,S.&Leutgeb,J.K.Gridandnongridcellsin
30. Kropff,E.&Treves,A.Theemergenceofgridcells:Intelligentdesignorjust medialentorhinalcortexrepresentspatiallocationandenvironmentalfeatures
adaptation?Hippocampus(2008).
withcomplementarycodingschemes.Neuron94,83–92.E6(2017).
31. Mathis,A.,Stemmier,M.B.&Herz,A.V.M.Probablenatureofhigher- 63. Brandon,M.P.,Koenig,J.,Leutgeb,J.K.&Leutgeb,S.Newanddistinct
dimensionalsymmetriesunderlyingmammaliangrid-cellactivitypatterns. hippocampalplacecodesaregeneratedinanewenvironmentduringseptal
Elife4,e05979(2015).
inactivation.Neuron82,789–796(2014).
8 NATURECOMMUNICATIONS| (2019) 10:5685 |https://doi.org/10.1038/s41467-019-13760-8|www.nature.com/naturecommunications

ARTICLE
NATURECOMMUNICATIONS|https://doi.org/10.1038/s41467-019-13760-8
64. Rueckemann,J.W.etal.Transientoptogeneticinactivationofthemedial CorrespondenceandrequestsformaterialsshouldbeaddressedtoR.M.M.orB.C.L.
entorhinalcortexbiasestheactivepopulationofhippocampalneurons.
Hippocampus82,246–260(2016). PeerreviewinformationNatureCommunicationsthankstheanonymousreviewers
fortheircontributiontothepeerreviewofthiswork.Peerreviewerreportsare
available.
Acknowledgements
WethankallmembersoftheLoveLabforvaluableinput.WethankRoddyGrievesfor Reprintsandpermissioninformationisavailableathttp://www.nature.com/reprints
hisadviceonanalysisofgridmeasuresandmembersoftheInstituteofBehavioural
Neuroscience(IBN)atUCLforvaluableinputanddiscussions.Thisworkwasfundedby Publisher’snoteSpringerNatureremainsneutralwithregardtojurisdictionalclaims
theNationalInstitutesofHealth[grantnumber1P01HD080679];aRoyalSociety inpublishedmapsandinstitutionalaffiliations.
WolfsonFellowship[18302]toBradleyC.Love;andaWellcomeTrustSeniorInvesti-
gatorAward[WT106931MA]toBradleyC.Love.
Open Access This article is licensed under a Creative Commons
Author contributions Attribution 4.0 International License, which permits use, sharing,
R.M.M.:conceptualization,formalanalysis,methodology,software,visualization,writing adaptation,distributionandreproductioninanymediumorformat,aslongasyougive
—originaldraft,writing—review&editing.B.C.L.:conceptualization,formalanalysis, appropriatecredittotheoriginalauthor(s)andthesource,providealinktotheCreative
fundingacquisition,methodology,resources,supervision,visualization,writing—original Commonslicense,andindicateifchangesweremade.Theimagesorotherthirdparty
draft,writing—review&editing. materialinthisarticleareincludedinthearticle’sCreativeCommonslicense,unless
indicatedotherwiseinacreditlinetothematerial.Ifmaterialisnotincludedinthe
Competing interests
article’sCreativeCommonslicenseandyourintendeduseisnotpermittedbystatutory
regulationorexceedsthepermitteduse,youwillneedtoobtainpermissiondirectlyfrom
Theauthorsdeclarenocompetinginterests.
thecopyrightholder.Toviewacopyofthislicense,visithttp://creativecommons.org/
licenses/by/4.0/.
Additional information
Supplementaryinformationisavailableforthispaperathttps://doi.org/10.1038/s41467-
©TheAuthor(s)2019
019-13760-8.
NATURECOMMUNICATIONS| (2019) 10:5685 |https://doi.org/10.1038/s41467-019-13760-8|www.nature.com/naturecommunications 9
