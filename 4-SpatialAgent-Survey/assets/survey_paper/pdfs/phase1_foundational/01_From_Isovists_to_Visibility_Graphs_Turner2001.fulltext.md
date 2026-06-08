Title: b2684 103..122

Source PDF: /Users/mac/Documents/6-Research/4-SpatialAgent-Survey/assets/survey_paper/pdfs/phase1_foundational/01_From_Isovists_to_Visibility_Graphs_Turner2001.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T02:56:54+00:00
- page_count: 20
- status: ok
- text_char_count: 56940

Metadata:
- author: Pion Ltd
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Abstract (page 1)
- Introduction (page 1)
- Related work (page 2)
- Constructing an isovist graph (page 4)
- Neighbourhood size (page 7)
- Analysing the graph (page 7)
- Clustering coefficient (page 7)
- Mean shortest path length (page 12)
- Further work (page 16)
- Conclusion (page 17)
- References (page 18)

Markdown Content:

EnvironmentandPlanningB:PlanningandDesign 2001, volume 28, pages103^121
DOI:10.1068/b2684
From isovists to visibility graphs: a methodology for the
analysis of architectural space
AlasdairTurner
VRCentrefor the Built Environment; e-mail: alasdair.turner@ucl.ac.uk
Maria Doxa
Bartlett School of Graduate Studies; e-mail: m.doxa@ucl.ac.uk
David O’Sullivan
Centre for Advanced Spatial Analysis; e-mail: david.osullivan@ucl.ac.uk
Alan Penn
VRCentrefor the Built Environment; e-mail: a.penn@ucl.ac.uk
UniversityCollege London,1^19TorringtonPlace,GowerStreet,LondonWC1E 6BT,England
Received15 November1999; in revised form19 February 2000
Abstract.Anisovist,orviewshed,istheareainaspatialenvironmentdirectlyvisiblefromalocation
within the space. Here we show how a set of isovists can be used to generate a graph of mutual
visibilitybetweenlocations.Wedemonstratethatthisgraphcanalsobeconstructedwithoutreference
to isovists and that we are in fact invoking the more general concept of a visibility graph.Using the
visibilitygraph,wecanextendbothisovistandcurrentgraph-basedanalysesofarchitecturalspaceto
form a new methodology for the investigation of configurational relationships.The measurement of
localandglobalcharacteristicsofthegraph,foreachvertexorforthesystemasawhole,isofinterest
from an architectural perspective, allowing us to describe a configuration with reference to accessi-
bility and visibility,to compare from location to location within a system, and to compare systems
with different geometries. Finally we show that visibility graph properties may be closely related to
manifestationsofspatialperception,suchasway-finding,movement,and spaceuse.
Introduction
Theconceptofanisovisthashadalonghistoryinbotharchitectureandgeography,as
well as mathematics. Tandy (1967) appears to have been the originator of the term
‘isovist’. He presents isovists as a method of ‘‘taking away from the [architectural or
landscape] site a permanent record of what would otherwise be dependent on either
memory or upon an unwieldy number of annotated photographs’’ (page 9).The same
idea has a similarlylong history in the guise ofthe‘viewshed’ in the field oflandscape
architecture and planning (Amidon and Elsner, 1968; Lynch, 1976) and in terms of
‘intervisibility’ in computer topographic models (Gallagher,1972).
The appeal of the concept is that isovists are an intuitively attractive way of
thinking about a spatial environment, because they provide a description of the space
‘from inside’, from the pointofviewof individuals, as they perceive it, interact with it,
and move through it. As such, isovists have particular relevance to architectural
analysis. Benedikt (1979) introduced a set of analytic measurements of isovist proper-
tiestobeappliedtoachievequantitativedescriptionsofspatialenvironments.Benedikt
starts by considering the volume visible from a location and then simplifies this
representation by taking a horizontal slice through the‘isovist polyhedron’.The result-
ing ‘isovists’are always single polygons without holes, as shown in figure1 (see over).
Consequently, Benedikt considers geometric properties of isovists, such as area and
perimeter.Thushebegins toquantifyspace, or whatourperception ofspace mightbe,
and the potential for its use. Benedikt notes that, in order to quantify a whole config-
uration,morethanasingleisovistisrequiredandhesuggeststhatthewayinwhichwe
experience a space, and how we use it, is related tothe interplayof isovists.This leads

104 ATurner, MDoxa, D O’Sullivan,APenn
Generating
location
Radial
Figure1. An isovist polygon, incorporating thevisible
area from a generating location (or convergence loca-
tionofthe optic rays).
him to formulate an ‘isovist field’ of his measurements. Isovist fields record a single
isovist property for all locations in a configuration by using contours to plot the way
those features vary through space.The packing of the contours shows howquickly the
isovistpropertyischangingandthus,Benediktsuggests,relatestobothGibson’s(1979)
conception of ecological visual perception and Giedion’s (1971) classification of archi-
tectural types.
However, despite the elegance of Benedikt’s isovist methodology, and its close
relationship to theories of visual perception and spatial description, applications of
the isovist in architectural analysis have been limited to a small number of studies.
There appear to be two main reasons for this. First, the geometric formulation of
isovist measures means that they index purelylocal properties of space, and thevisual
relationship between the current location and the whole spatial environment is
missed(cid:246)including the fact that the internal visual relationships between locations
within the isovist are ignored. Second, Benedikt makes no propositions about how to
interpret usefully the result of his isovist measures, although Benedikt and Burnham
(1985) do show how perception of space is affected by various isovist attributes. In
other words, there is little in the way of a theoretical framework to allow one to say
how isovists relate to social or aesthetic matters. To overcome these limitations we
introduce a broader methodology, one that embraces how visual characteristics at
locations are related and one that has a potential ‘social’ interpretation.We draw on
graph-based representations used in social theories of networks, primarily the space
syntaxtheoryof Hillierand Hanson (1984) and the smallworlds analysis of Watts and
Strogatz (1998), which leads us to use isovists to derive a visibility graph of the envi-
ronment(cid:246)the graph of mutually visible locations in a spatial layout. Through this
representation we can obtain numerous measures of both local and global spatial
properties that seem likely to relate to our perception of the built environment. By
looking at these local and global properties, considering their meaning in terms of
spatial description, and comparing them with actual usage(cid:246)through movement and
occupationoftheenvironmentthatthegraphrepresents(cid:246)wehopetoshedlightonthe
effects of spatial structure on social function in architectural spaces.
Related work
Various authors have used Benedikt’s formulation in architectural case studies. For
example, Hanson (1994) uses isovists among other methods in order to investigate
several well-known architects’ houses. However, although Benedikt’s work has had
animpactontheway wethinkaboutspace,therehasbeenrelativelylittledevelopment
of the isovist concept or related methodologies in the architectural literature. Davis
and Benedikt (1979) make a moreformal mathematicalstudyof isovistgeneration and
location, and Benedikt and Burnham (1985) study the perceptual impact of isovist

From isovists tovisibilitygraphs 105
properties. However, in the field of geoinformation science (GISci), the methodology
has been explored more thoroughly under the moniker ofviewshed analysis.Viewshed
analysis concentrates on landscape, rather than urban and architectural issues (for a
background to the technique, see Burrough, 1986, pages 39^56). Consequently, the
area a viewshed covers is not necessarily continuous. For example, an observer may
see over a ridge to a mountain in the distance, missing the intervening space. As for
the extension of the methodology, there is a technical literature investigating the
dependence of various viewshed characteristics on the accuracy of the underlying
elevation data (for example, see Fisher,1991; Huss and Pumar,1997) and correspond-
ing suggestions for the generation of ‘fuzzy’ viewsheds (Fisher, 1995). There also
continue to be innovations in algorithms for generating viewsheds (Mills et al, 1992;
Wang et al,1996) and new suggestions for variants on the basic idea which determine
the position ofhorizons,theverticaldisplacementofhorizonsfrom theviewpoint, and
‘offset viewsheds’ which take into account viewer height (Fisher, 1996). Of more
relevance to the current work is viewshed analysis in archaeology (Wheatley, 1995),
where the cumulative viewsheds over a region are used to determine the most visually
prominent locations.The‘prominence’value generated is related to the distribution of
different kinds of ancient monuments. More recent work looks set to extend this
analysis considerably, by using differential measures of viewshed fields to measure
more abstract concepts such as enclosure (Llobera, 1996). Llobera’s work is similar
in many respects to Benedikt’s isovist fields. Indeed, much of the viewshed literature
still concentrates on mapping the properties of single viewsheds as fields, not on the
relationships betweenviewsheds. In work applying such structures to the classification
of landscapes, Lee and Stucky (1998) have demonstrated the determination of routes
withdesirablevisualcharacteristics.Theirmethodfindstheshortestpath(accordingto
the metricunderconsideration) through an implicitgraph, in order to determine paths
with particular characteristics, for example, the most scenic or most concealed route
between two points.
Whereas in viewshed analysis graphs of visibility relationships are still implicit,
architectural analysis has had a long history of graph-based analysis. Steadman
(1973) demonstrates how graphs may be constructed of architectural arrangements,
considering relationships between architectural units (such as rooms or corridors),
although the original concept dates back further (for example, see March and Stead-
man, 1971; Ore, 1963). Kru«ger (1979) shows how similar graphs of the relationships
between urban units may be constructed. In contrast to forming edges between struc-
tural units, Hillier and Hanson (1984) introduce visibility relationships into graph
analysis of buildings and urban systems. They construct the set of axial lines for a
system, which are the fewest longest lines of sight and access in the system which
traverse all the convex spaces within that system (the convex spaces being a near-
minimal set of nonoverlapping convex polygons covering the space(1)).The axial lines
thusformasetofintersectinglineswhichrepresentallnontrivialringsofcirculationin
a system. By graphing the structure of axial lines (where each axial line is a vertex in
the system, and each intersection a node) Hillier and Hanson provide a description of
how the system can be traversed in terms of lines of sight, because we can say how
many changes ofdirection are required toreachanyspace from anyother space in the
system. The methodology may be extended by introducing new graph representations
capable of being automated, such as ‘all-line’ axial maps, in which all the lines that
(1) Constructingauniqueminimalsetofconvexpolygonsisnotpossiblein mostcases,oratany
rate not calculable in polynomial time (see deBerg etal, 1997, pages 45^61), but Hillier and
Hanson show that, in practice, it is simple to decide on a sensible spatial breakup for a given
morphologybychoosing the‘shortest and fattest’convexpolygons.

106 ATurner, MDoxa, D O’Sullivan,APenn
form a tangent between any pair of mutually visible vertices are drawn (Hillier and
Penn, 1992). This representation produces a more densely packed graph, with more
information about the relation of lines of sight in a system. Despite their general
applicability, the ability of these maps to represent and quantify spatial configurations
stillhasonemajordrawback:eachlineorconvexregionisrepresentedbyanodeinthe
graph, and so only a single graph measure can be defined for points along the whole
length of the line, or all points within the convex region. Hillier et al (1995) combine
line-of-sightmeasuresandtessellationofareastoresolvethisissue.However,asisovists
can be drawn at any location in space, a graph of lines-of-sight connections may be
constructed easily, at any required degree of spatial resolution, by using the visual
relationships between isovists. De Floriani et al (1994) propose such a form of graph,
avisibilitygraph,whichisidenticalinstructuretothatwhichweproposehere,albeitto
solve the problem of transmitter placement rather than analysis of the underlying
landscape properties and thus their approach is very different.
Constructing an isovist graph
Constructing an isovist graph of a spatial environment involves two distinct sets of
interrelated decisions. First, we must select an appropriate set of isovists (in fact an
appropriate set of generating locations, according to some criterion) to form the
vertices of the graph. Second, given a particular set of isovists, we must determine
which relations between them are significant, or are of interest, to form edges in the
graph. These steps are both theory laden and must be driven at least in part by
pragmatic considerations(cid:246)the size of the graphs which will be produced, and so on.
Here we explain the decisions we have made. The theoretical implications of these
decisions will become clearer in the presentation of the various graph-based measures
we have used. For now we acknowledge that there is no compelling way of choosing
oneparticularapproachoveranotherandwediscusssomeavenuesforfurtherresearch
later in the paper.
Ideally we would like to select some set of isovists that ‘fully describes’the spatial
system. In practice we must compromise and try to select a setofgenerating locations
that provides an acceptable‘near-full’description ofthe space. Following Benedikt, we
assume that isovists can be meaningfully generated throughout a space and further-
more that it is useful to examine isovist properties (whether local or relational)
throughout a system.Thus the most obvious approach is to generate isovists through-
out a spatial system atsome regularly spaced interval.This implies thatthe generating
locations will be at points defined by some sort of grid or regular lattice. The appro-
priate grid resolution must then be determined. If analysis is to relate to human
perception of an environment, then the resolution of this grid must be fine enough
to capture meaningful features of the environment. On the other hand, if we wish to
considerhumanusageofanenvironment,alowerresolution maybeused(forexample,
mapping only space that is humanly accessible). We have adopted the pragmatic
approach of using a ‘human-scale’ grid spacing of around one metre. This seems
reasonable given that our purpose is to understand spatial environments designed for
human occupation as they are used and perceived by individuals. However, ultimately,
the resolution of the analyses we present here is limited only by available computing
power.
Of course, a method approximating the underlying space such as this quickly
produces very large sets of generating locations. To remedy this we might try to find
a minimal covering set of isovists for the space. For example, we might start by
choosing the most ‘strategic’ location in the environment, then continue by selecting
additional locations which maximise the areaviewable from the set as each location is

From isovists tovisibilitygraphs 107
added. However, although finding a sufficient set by this method is possible, it is not
guaranteed to be a minimal covering set (Davis and Benedikt,1979). In addition, for
our purposes, a graph analysis of any such minimal set is likely to provide only
relatively obvious information about the environment, because locations at the end
of long corridors or at prominent street junctions will tend to be favoured. However,
note that this issue is central to problems considered in GISci, such as line-of-sight
communications.
Once we have selected a set of generating locations, which relationships between
different isovists in an environment should be included in an isovist graph? If we
consider the isovists to be polygons, the most obvious relationship to consider occurs
wheretwoisovistpolygonsintersectwithoneanother.Arguably,astrongerrelationship
between two isovists exists where they intersect and their generating locations are
mutually visible. We refer to this as a first-order relationship. In order to determine
this relationship we need not invoke isovists at all: we can simply make a graph with
physical locations as vertices, and form edge connections between pairs of locations if
theyaremutually visible.Thisisavisibilitygraphofthesystem(2).As,bydefinition,an
isovist from a given generating location contains all the locations visible from it, the
visibility graph is identical to our putative first-order isovist graph. An ‘isovist inter-
section graph’ is closely related: it can be formed by taking a visibility ‘step’ from
one isovist-generating location to an intervening location, and then a ‘step’ onto the
next isovist-generating location. Hence we refer to this as a second-order visibility
relationship (see figure 2). It is apparent from this description that a second-order
visibility or isovist intersection graph is a‘flattened’ form of the (first-order) visibility
graph,wherethesetofedgesistheunionofalltheone-stepandallthetwo-step edges.
Thus the first-order visibility graph contains all the information necessary to form the
second-order graph and therefore we will concentrate on the analysis of first-order
C
A
B
(a) (b)
Figure 2. (a)First-order and (b) second-order visibility relationships between isovists. The
second-order graph is just a‘flattened’ first-order graph(cid:246)A is linked directly to B, rather than
through C as it would be in the first-order case.
(2)ThetermvisibilitygraphwasintroducedtolandscapeanalysisbyDe Florianietal(1994)and
it is also prevalent in computational geometry and artificial intelligence (see deBerg etal,1997,
pages 305^315). Both of these forms of visibility graph are more sparsely connected than our
own,astheyincludeonlykeylocationsintheenvironment(inlandscapes,pointsselectedfroma
triangulated irregular network (TIN); in computational geometry, corners of two-dimensional
polygons).However,thearchitecturalvisibilitygraphalsousesselectedlocationsasverticesanda
mutualvisibility relationship toform edges, and thus all the graphs are of identical form.

108 ATurner, MDoxa, D O’Sullivan,APenn
Figure3.Anexampleofafirst-ordervisibilitygraph,show-
ingthepattern ofconnectionsfora simpleconfiguration.
visibility graphs in this study. Figure 3 shows an example graph made from thirty-six
point locations.
Note that, although we have discussed a graph in terms of visibility, and therefore
implicitly at eye level, the visibility graph can be formed by taking an isovist at any
height above the floor. As Hanson (1999, page 54) writes ‘‘In moving around in
buildings, people orientate themselves by reference to what they can see and where
they can go. [In addition,] in looking at the visual and volumetric qualities of archi-
tecture, we need not be constrained by the pragmatics of everyday space use and
movement. Indeed, we should notbe, since architectural speculation almost invariably
brings into play the relationship betweenvisibility (whatyou can see) and permeability
(whereyou cango).’’Thusitseems sensibleto extendouranalysis tobothvisibilityand
permeabilitygraphs ofsystems.Tobe clear, a‘permeabilitygraph’isthe specialcaseof
a visibility graph constructed at floor level. We will see how the permeability graph
varies according to whether furniture and other obstacles to accessibility are included
in the analysis of a system.
In mathematical terms, a graph consists of two sets: the set of the vertices in the
graph, labelled V, and the setofedge connections joining pairs ofvertices, labelled E
(for an introduction to graph theory, see, for example,Wilson, 1996). This informa-
tionissummarisedby writingthegraphasthepairofthesesets:G(V,E).Inthe case
of a visibility graph, the vertices represent the set of generating locations to be
considered:
V (cid:136) fv ,v ,v ,.::,v g.
1 2 3 n
The edges are pairs of mutually visible points.We will denote the edge joining v and
1
v , that is fv ,v g, as e .Thus the edge set will be of the form
2 1 2 12
E (cid:136) fe ,e ,.::,e g, where e ,e .
12 23 ij ij ji
Inarepresentationonatwo-dimensionalplane,thegraphedgesareundirected(thatis,
if v can see v , then v can see v ). However, in other representations visibility is not
1 2 2 1
necessarily mutual(cid:246)for example, viewshed analyses often consider viewer height. In
addition, even ignoring viewer height, we may want to construct an ‘accessibility’
graph, differentiating between, for example, escalators or entrances and exits. In such
cases, edges in the graph may be directed. Many possible measures of an undirected
graph are also applicable to a directed graph, including those we illustrate in this
paper, so that the generality of the method presented is unaffected.

From isovists tovisibilitygraphs 109
Analysing the graph
Havingderivedavisibilitygraphforaspatialenvironmentwecananalyseitbymaking
use of some of the many measures developed for investigating graph properties across
a number of disciplines [Wilson and Beineke (1979) give an idea of the range of
measures available].We focus on three measures of graph structural properties.These
are the local properties neighbourhood size and clustering coefficient, and the global
property mean shortest path length. The clustering coefficient and mean shortest path
length have previously been used together to characterise graph systems as a whole
(see Watts and Strogatz, 1998) and we discuss how this characterisation might be
applied to visibility graphs of environments in further work. However, for the current
study,weconsidereach measurefromthepointofviewofeachvertexinthegraphand
we examine the pattern of their distribution across systems. This is readily done by
mapping the values of measures at each generating location by using some colour
scale.Inthesectionsthatfollow,wedescribethemeasures indetail,discusstheirlikely
usefulness and implications, and present some cases based on the analysis of various
relatively simple examples.
Neighbourhood size
The neighbourhood of avertex is the set ofvertices immediately connected through an
edge. Expressed in terms of graph notation, the neighbourhood N of a location v is
i i
the set of directly visible vertices:
N (cid:136) fv :e 2Eg.
i j ij
Now if the set of generating locations covers the entire space (at some uniform
resolution, so that for our purposes it fully describes the space), then this set can be
thoughtofasequivalenttotheisovistitself.Hencethereisaone-to-one correspondence
between the neighbourhood of a vertex in a visibility graph and the isovist from the
location represented by that vertex. (Note that the neighbourhood of a location does
not include itself. Technically we should write that N [v, not N, corresponds to an
i i i
isovist.) Thus we can attach a meaningful spatial description to the neighbourhood
size: itislinearlyrelatedtothe isovistarea,thatisthe area A oftheisovistatlocation
i
v is directly proportional to the neighbourhood size k of the vertex v:
i i i
A /(cid:133)k (cid:135)1(cid:134), where k (cid:136) jN j.
i i i i
(We assume adequate coverage of generating locations throughout the system. In
figure 3 the coverage is not sufficient and the isovist area no longer corresponds
perfectly to the neighbourhood size.)
We can plot the values of neighbourhood size for all the physical locations
representedbyverticesinthegraph.ThiskindofplothasdirectrelevancetoBenedikt’s
description of space by isovist fields(cid:246)a plot of the isovist field of the area property
drawscontoursofequalviewableareaacrossaspace.Infigure 4(seeover)weshowthe
isovistfieldofisovistareaforasimplespatialconfiguration,andbesideittheneighbour-
hoodsizeplottedbyusingascalefromblack(minimumarea)towhite(maximumarea).
Notethattheisovistfieldlinesarecontinuous,whereasthediscretegeneratinglocations
used to construct the visibility graph can be seen in the second diagram.
Clustering coefficient
The clustering coefficient is defined as the number ofedges between all the vertices in
the neighbourhood of the generating vertex (that is, the number of lines of sight
between all the locations forming the isovist) divided by the total number of possible
connections with that neighbourhood size. In isovistterms this is equivalentto finding

110 ATurner, MDoxa, D O’Sullivan,APenn
(a) (b)
Figure 4. (a) An isovist field of isovist area, and (b) aplotof neighbourhood sizevalues.
the mean area of intersection between the generating isovist and all the isovists visible
fromit,asaproportionoftheareaofthegeneratingisovist.Insetterms,theclustering
coefficient C for the neighbourhood N of location v is
i i i
jfe : v ,v 2 N ^e 2 Egj
C (cid:136) jk j k i jk ,
i k (cid:133)k (cid:255)1(cid:134)
i i
where k is the neighbourhood size.
i
At first sight this measure relates to the convexity (or conversely the‘spikiness’) of
the isovist at the generating location v. If the isovist being considered is almost a
i
convex polygon, then almost all the point locations within the neighbourhood will be
able to see each other, and hence C will tend to one. If, on the other hand, the isovist
i
is very‘spiky’ (not at all convex) then many points within the isovist will notbevisible
from each other, and C will tend to zero. Figure 5(a) shows C mapped for a simple
i i
spatial configuration, for a graph with 2260 vertices.
Further consideration reveals that the clustering coefficient gives a measure of the
proportion of intervisible space within the visibility neighbourhood of a point. It
indicates how much of an observer’s visual field will be retained or lost as he or she
moves away from that point. If the neighbourhood of a point approximates a convex
p p
1 2
(a) (b)
Figure 5. (a)Clustering coefficient values for a simple configuration. (b) The clustering coeffi-
cient is increased when many points within the isovist are mutually visible, regardless of the
convexityofthe geometric isovist polygon.

From isovists tovisibilitygraphs 111
polygon, then the clustering coefficient is high and moving from that location in any
direction will not cause any great loss of visual information. However, at a junction
with multidirectional visual fields, C will be low as moving from that location will
i
involve loss of part of the currently visible area. Because movement in some sense
involves making decisions about which parts of one’s current visual information to
leave behind, the clustering coefficient is potentially related to the decisionmaking
process in way-finding and navigation and certainly marks out key decision points
within complex configurations. Further, if we regard vertices in the graph as poten-
tiallyoccupiedbypeople, C valuesindicatethepotential forperceivable copresencein
i
a space and therefore the potential to form groups or to interact(3). In a closed convex
area there is some potential for interaction, whereas in a junction there are numerous,
but different, opportunities to form intervisible links. This seems likely to prove a
useful property in studying the perception of spaces and may also be useful in behav-
iouralstudies. For example, Benedikt and Burnham (1985) show thatperception ofthe
size ofa space is affected bythevariance ofthe radials ofan isovist and the perimeter
(both indicators of convexity). In addition, de Arruda Campos (1997) finds good
correlation with the number of axial lines intersecting at an urban space (implying a
multidirectional visual field, that is, low C) and the number of people making infor-
i
mal use of the square, and Conroy (2000) notes correspondence between ‘junctions’
and places where people pause on journeys.
We use the clustering coefficient to analyse two houses as examples: Alvar Aalto’s
VillaMairea andMiesvander Rohe’sFarnsworthHouse (forbackground information
on the houses, see Curtis,1996). Figure 6 shows the pattern of C values produced for
i
the interior spaces oftheVilla Mairea.Thevisibilitygraph is formedbytakinga1.0 m
grid on a section of the plan at eye level on each floor, then linking vertices on the
staircases across the two levels to produce a single graph. Afterwards, C values are
i
calculated at each location. The figure shows that the most private spaces, such as
bedrooms and study rooms, are highly clustered whereas social spaces, such as the
living rooms on each floor and ground-floor sitting rooms offer multidirectional fields
of view and therefore low C, values, hinting at(cid:246)without intruding on(cid:246)the range of
i
the more private spaces.
(a) (b)
Figure 6.The clusteringcoefficientmeasuredforAalto’sVillaMairea.Thetwofloorshavebeen
linkedviathe stairwells.
(3)We realise that any population of a space will interfere with visual fields, and thus C.
i
However, the presence of individuals is transient and, as lines of sight are restored with move-
ment (of both the observer and the observed), we believe appreciation of the built form as a
forum for interaction remains possible.

112 ATurner, MDoxa, D O’Sullivan,APenn
Theresultsofclusteringcoefficientanalysisarerelatedtotheendpointpartitioning
proposed by Peponis et al (1997).The spaces defined by endpoint partitions, e-spaces,
are mathematically well defined and lead to a unique spatial description.They define
‘informationally stable’ units with respect to form, by considering the visibility of
discontinuities of shape, such as corners and edges of wall surfaces. Being dependent
on discontinuities, they are affected by the complexity of the plan and the degree of
detail in the representations of shapes. As a spatial description, e-spaces present a
different approach to visibility graphs, primarily because they are derived by relating
space to built form, rather than derived from the space as it might be experienced.
However,e-spacesand C valuesbothprovideanindicationoftheinternalcohesionof
i
the overallspace at any point withinthatspace. Peponis et alpresented results oftheir
analysis for a simplified plan of Farnsworth House, and their diagram (page 772)
shows strictly delineated areas of informational stability. In contrast, analysis of a
plan of Farnsworth House with C values results in a gradual partitioning of space,
i
where information is seen to vary continuously across the space and within e-spaces
[figure 7(a)]. Althoughthere is‘informationalstability’with respecttoverticalsurfaces
there are clear variations in the internal relational properties of the isovists within
thesespaces.ConsideringtheC valuesin moredetail,thereisamaximumatlocations
i
closer to the central element, which is more self-contained, with almost convex visual
fields. The lowest values occur further away where isovists are multidirectional (and
Hillier and Hanson’s convex partitioning schema is difficult to apply). In these loca-
tions, the placement of the furniture by the users reorganises the spatial layout
by relating accessibility and/or permeability to the lived use of space(cid:246)as shown
in figure 7(b), which demonstrates clustering coefficient permeability analysis of
Farnsworth House with its furniture.
(a) (b)
Figure 7. (a) Clustering coefficient values for a simplified Mies van der Rohe’s Farnsworth
House, analysed for visibility with the e-partitions of Peponis etal overlaid; and (b) clustering
coefficient values for thebuilding furnished and analysed for permeability.

From isovists tovisibilitygraphs 113
Note that the clustering coefficient might be considered similar to a convexity
measure of an isovist polygon, such as some combination of Benedikt’s measures of
variance of the radials M and perimeter P. However, the C measure is in fact more
2 i
subtle than this, precisely because the geometry of the isovist polygon has been
discarded. Any pair of mutually visible locations within the isovist area contribute to
the overall C value; thus anysystemwith‘visibilityloops’will displayhigher C values
i i
thanthosewithout.Forexample, both figures 5(a) and5(b)plotC valuesbyusingthe
i
samescale.Theisovistpolygonatp ismoreconvex(intermsofM andP)thanthatat
1 2
p , yet the value of C at p is higher. Hence the clustering coefficient is not strictly a
2 i 2
convexitymeasure, butperhapsmorerelatedtohow‘self-contained’the information in
aparticularisovistis.Thus,becauseC isnotjustameasureofgeometric‘spikiness’,but
i
also a measure ofhow much objects ofvarying sizes disruptthe space, it may improve
ourunderstandingofhowaspaceisperceived.Forexample,althoughaddingapillarto
a space will increase the spikiness ofan isovist dramatically, people will notusuallybe
fooled by such an addition [figure 5(b)]. Through movement they will still be able to
perceive the space as a whole, and this is reflected in the clustering coefficient value.
The sensitivityof clustering coefficient analysis to the size ofobject in the environ-
ment would have a significant impact if we were to consider not just the internal
relationships in Farnsworth House, but also its relationship to the surrounding envi-
ronment.Further,theanalysiswehavemadehasnotconsideredthebuiltfabric,orthe
relation of the interior to the building’s context. So far, we have taken no account of
the fact that the external envelope of Farnsworth House is made entirely ofglass, and
this raises interesting questions with respect to visibility relations between ‘inside’and
‘outside’.We might consider the surrounding space (the stepped terraces and the land-
scape) and include visibility connections through the glass walls. As one approaches
the house, it features as an object in the landscape and, on looking through the glass
external wall, one finds that the core becomes an object within an object. At a
distance, the clustering coefficient will remain relativelyhigh, because the connections
betweenisovistsoneithersideofthehousearerealisedinalooparoundit[figure 8(a)].
As we move towards the entrance, through the terraces, the space becomes gradually
more clustered and only the central core inside the building, visible through the glass,
features as an object [figure 8(b)]. As we enter, the clustering coefficient increases
L
2
L
2
L
1
P
P
P
(a) (b) (c)
Figure 8. DirectconnectionsbetweenpointsoneithersideofanisovistfromP,completingloops
behind the Farnsworth House (L) and (assuming ‘visibility’ into but not out of the glass
1
envelope) its central core element (L ). In (a) both loops are completed, in (b) loop L cannot
2 2
be completed owing to obstructions in the surrounding environment, and in (c) neither loop is
completed.

114 ATurner, MDoxa, D O’Sullivan,APenn
further towards the core element, which now becomes an architectural element artic-
ulating the interior space around it. In fact, if once inside we consider the walls as
containing our ‘visibility’ (or at least our sense of enclosure), then there is no location
within the house where the points of an isovist on either side of the core element
connect in a loop behind it [figure 8(c)]. In this sense the clustering measure may
capture the transition between architecture considered as a disposition of objects and
architecture as a space-defining configuration, a transition which is dependent on the
relative location of the viewer.
Mean shortest path length
The shortest path between two vertices in a graph is the least number of edges that
need to be traversed to get from one vertex to the other. The mean shortest path
length for avertex is simply the average of the shortest path lengths from that vertex
to every other vertex in the system, and so represents an average of the number of
turns (plus one) required forany journey within the system. Formallydefined, a path
from v to v is a sequence of unique intervening vertices between v and
i j i
v (v ,.::,v ,.::,v ), such that consecutive vertices in the sequence are joined by an
j i n j
edge in the graph, thatis, e is a memberof E.Thelengthofapath is the number
n;n(cid:135)1
ofedgesittraverses,andthedistanced betweenv andv isthelengthoftheshortest
ij i j
available path between them.Thus the mean shortest path length L(cid:22) for a location v
i i
in terms of graph notation is:
L(cid:22) (cid:136) 1 Xv j 2V d .
i jVj ij
j
Figure 9(a) shows the mean shortest path length mapped for a simple spatial config-
uration, for a graph with 2000 vertices.The lower L(cid:22) values are coloured white in the
i
figure, whereas higher L(cid:22) values are black.
i
Note that the measurement of mean shortest path length has direct parallels with
Hillier and Hanson’s approach. Hillier and Hanson quantify the visual accessibility of
spaces (through the number of turns connecting those spaces), whereas we quantify
the visual accessibility of every location in the spatial system (through the number of
turns plus one). Hence our analysis extends the Hillier and Hanson method to (near)
continuous space and enables the resulting locations within a space to be mapped
across thatspace. Indeed, because this more direct representation quantifies thevisual
(a) (b)
Figure 9. (a) Mean values of the shortest path length for a simple configuration. (b) The area
undertheT-crossbarhashigherL(cid:22) valuesbecauseofatwo-steprelationshipwiththeareaabove
i
the crossbar.

From isovists tovisibilitygraphs 115
accessibility of every location in the spatial system, it has a significant advantage over
axial and convex configurational analysis, which, for example, is unable to identify
variation across‘open-plan’ layouts.
As the mean shortest path length measures configuration by considering locations
withrespecttoeachotherlocationinthesystem,globalrelationshipsbetweenlocations
inthesystembecomeapparent.Forexample,thepointslocatedbelowtheT-crossbarin
figure 9(a)formdistinctlycolouredtriangularregionsaccordingtotheirL(cid:22) values.This
i
is due to the second-order effect of spaces two steps away. In this case, because they
cannot ‘see’the top spaces of the configuration, an individual occupying that location
would notknow thatthere mightbe aplace‘aroundthe corner’. Ifanindividualleaves
one ofthese triangular zones, then theyare entering a zone where, one step away, they
can see a larger area, as shown in figure 9(b).Thus the pattern of L(cid:22) values classifies
i
locationsaccordingtoglobalconfigurationalproperties.Asinthecaseofthetriangular
regionsoftheT-shapeexampleabove,thiskindofpartitioningdoesnotshowupinany
obvious first-order partition, including such detailed descriptions as those of endpoint
partitionsbyPeponiset al.Thissuggeststhatbyusingthevisibilitygraphtechniquewe
obtainanalternativespatialdescriptiontothosepreviouslyavailablebypartitioningthe
spaceintermseitheroflocalgeometricpropertiesofvisualfieldsasBenediktdoes,orof
formal discontinuities and adjacency properties as Peponis et al do.
As a built example, we consider the configurational characteristics of the spaces
in Mies van der Rohe’s Barcelona Pavilion. The pavilion was built in 1929 for the
German participation in the Barcelona exhibition and demolished afterwards. It was
retrieved through photographs and plans, to be rebuilt in 1986 (for a detailed dis-
cussion, see Futagawa and Neumeyer,1995). Benedikt uses the plans of this building
to investigate isovist^field contour maps, demonstrating that the area of the visual
field changes continuously with movement, as surfaces disappear and others come
into view. We construct both a permeability graph as well as the visibility graph
[compare figures 10(b) and 10(c)]. To create these figures we used a 0.5 m grid of
vertices covering all accessible areas in the pavilion, forming two different graphs
taken at eye height and floor height. In the visibility case, for example, edges are
formed between points visible across the pool, or on opposite sides of a piece of
pool pool pool
pool
pool pool
(a) (b) (c)
Figure10. MiesvanderRohe’sBarcelonaPavilionshowing(a)neighbourhoodsize,(b)visibility
mean shortest path length analysis, and (c) accessibility mean shortest path length analysis.

116 ATurner, MDoxa, D O’Sullivan,APenn
furniture, whereas no connection is made in the permeability graph. In both cases,
path length analysisproduces apatternthatresembles thatofneighbourhood size, or
area of visual fields, and therefore is similar to Benedikt’s area measurement, owing
to the fact that this is a small or shallow system where the architect introduces
partitionstostructurethespacewithoutdisturbingtoomuchitscontinuity(cid:246)compare
the k values in figure10(a) with L(cid:22) values shown in figures10(b) and10(c). However,
i i
path length analysis still enables us to look at the relationship between specific
locations in the space and the configuration as a whole. The main difference in the
configurationalpatternsgeneratedresultsfromthewaythelargepoolisanalysed.The
comparison shows how the space has been manipulated by the architect to arrange
viewsacross the pool andthe movement around it.Thus, inthevisibility model, L(cid:22) is
i
maximised at the edges of the system around the pool. When analysed in terms of
accessibility,however,the coreL(cid:22) valuesareshiftedtothe centralspacethatlinksthe
i
two locations with the richest accessibility fields and spreads towards the far side
offering views to the smaller pool and statue.
Inlargerandmore complexsystemsthantheBarcelona Pavilion,thelocal(suchas
k ) and global (such as L(cid:22)) characteristics vary considerably from each other. As an
i i
example of a more involved system we analyse the Tate Gallery on Millbank in
London, in which there are many rooms consisting of both gallery space and major
movement routes through the building. Figure11(a) shows neighbourhood size and
figure11(b) shows the pattern of L(cid:22) values for the main level of the Tate Gallery,
i
and the difference between the local and the global spatial measure is very obvious,
now that many changes of direction are required for full exploration of the space.
(a) (b)
Figure11.Visibility graph analysis of theTate Gallery showing (a) the neighbourhood size, and
(b) the pattern of mean shortest path length in the publiclyaccessible first-floor spaces.
However, we need notconstrain mean shortestpath length analysis toa qualitative
discussion of spatial description. In a study of the Tate Gallery, Hillier et al (1996)
demonstrate that there is a correlation between‘pesh’analysis (an L(cid:22)-type measure for
i
spaceswithinaconfiguration;seeHillieret al,1995)andthenumberofpeoplemoving
between predefined areas in the building.This indicates that comparing the L(cid:22) values
i
acrossthevisibilitygraphwithpeoplemovementpatternsmaybefruitful.Forexample,
figure12(a) shows the movement patterns over the first ten minutes of a visit to the
Tate Gallery. Comparing this with L(cid:22) values shown in figure11(b), there appears tobe
i
a qualitative correspondence between the two. Correspondence can also be observed
when we compare L(cid:22) values against average room occupancies during the day. Figure
i
12(b)shows theoccupancylevel per room,withdatafrom theHillieret al(1996) study

of theTate Gallery, where the spaces were observed five times in a day and averaged
across the day. The correspondence is demonstrated more clearly by inspection of a
scatter plot of observed room occupancy against L(cid:22) (see figure13). In order to obtain
i
the plotshown, the L(cid:22) values ofthe locations within each space have been averaged to
i
give a single value per room(4). A best-fit line through the data gives a reasonable
exponential correlation between the two variables and it is noticeable that the only
significant outlier found is the Tate Gallery shop, which is the only room that is not
used as gallery space. Although a correspondence of this sort might be expected in
viewofthefactthat we are mapping a measure ofcentrality, it is worth demonstrating
thatthis is not a necessary result. Figure14 (see over) shows a Euclideanversion of L(cid:22)
i
analysis (which, for each location, measures the mean Euclidean distance to all other
locations in the space, on the same grid as before), applied as na|«vely as L(cid:22) visibility
i
(4)Note that the yaxis shows the average occupancy in each room, not the average occupancy
density.Thefactthatourmeasurestillcorrelatesmightbeexpected,ask (which,withinaroom,
is roughly proportional to the areaofthe room) has the mostsignifican i teffecton L(cid:22).
i
level
ycnapucco
mooR
From isovists tovisibilitygraphs 117
(a) (b)
Figure12. (a)Firstten-minutemovementtracesofpeoplethroughthegallery(Hillieretal,1996,
page 20), and (b) the average observed occupancylevels ofrooms during the day.
50
Shop
40
30
20
10
0
3.0 4.0 5.0 6.0 7.0 8.0
Mean shortest path length
Figure13. A scatter plot showing the room occupancy level (average number of people at any
instant) against the mean shortest path length. [An exponential regression line (R2 (cid:136) 0:63) is
shown.]

118 ATurner, MDoxa, D O’Sullivan,APenn
Figure14. MeanEuclideanshortestpathlengthsforthe
Tate Gallery (average distance from each grid location
to all other grid locations in the system).
graph analysis, and the result shows no obvious correspondence to either the first
ten-minute movement or the average occupancy of the rooms.
Wehope that in the future we maybe able to relate correspondences such as those
foundintheTatetosomehumancognitivemodel.BenediktcitesGibson’s(1979)model
of visual perception as one of the major reasons for constructing contours in isovist
fields, reasoning that movement decisions should be made at times of rapid change in
isovist area values. Similarly we can propose tentative hypotheses. For example, if
individuals are random agents in the environment, moving towards open space, then
they would tend to coalesce in areas of high visual accessibility. As the agents’general
movement is directed along lines of sight, more lines of sight meeting at a location
would lead to a higher congregation of individuals at that location (a result mirrored
by de Arruda Campos’s findings). Although this is obviously a gross simplification of
any actual interaction of individuals with a spatial system, it shows a clear way in
which simple predictive models can be made and tested with the visibility graph
method.
Further work
Although the characterisation of space in this way is interesting, much work on the
application of the analysis is still required. Most importantly we need to develop a
more systematic method of selecting and generating point locations. At the very least,
the effectofthegenerating pointlocations ongraph measures mustbe researched.The
grids we currently use are dependent mainlyon the power of the computers we use to
analyse them. Nevertheless, however powerful the computer, we can never achieve
‘perfect’resolution to representthe spatial environment. Necessarily we must compro-
mise on the graph structure we choose and it would be preferable to have a firmer
theoretical basis for this choice. According to van Fraassen’s scientific empiricism
(1980, pages 76^91) our interpretation of any graph will be limited by the ability of
ourmeasurestodistinguishbetweendifferentconfigurations,sowecanonlydescribea
graph through the number of metrics we invent to classify it. One hypothesis is that
above a certain isovist coverage of a space any graph measures we take will become
invariant (or vary only as a simple function of the set size). Determining such a
characteristic limit to‘graph measure invariance’ in specific cases would set a ‘natural’
upperlimitonthe numberoflocations thatneedtobeused and itwould also allow us
to look at the effect of using, for example, distorted rather than regular grids. In
addition, if it is possible to find such characteristic values for a system, then it would
openup avenues to comparewhole spatial environmentswith one another. Aswehave
noted, average clustering coefficient and the characteristic path length (the average of

From isovists tovisibilitygraphs 119
the mean shortest path length for the whole system) have been used by Watts and
Strogatz(1998)toanalyse smallworlds networks. Bytaking measuressuchas thesefor
the whole system, we might hope to discover new characterisations for architectural
types, and to classify their configurations.
Conclusion
Inthispaper wehavepresented anewapproachtotheapplicationofisovistsinspatial
systems.Ratherthaninvestigatethepropertiesofsingleisovists,ashasbeenconsidered
in the literature, we have constructed a graph by using isovist-generating locations as
vertices, and visibility relationships between isovists as edges.The resulting graph is a
visibility graph of locations within the space. By reinterpreting the set of isovists as a
graph we have made the system more amenable to a new set of analytic tools, while
retaining a mapping backto the original isovist interpretation through the neighbour-
hoodsizek ofavertex.Thisallowsustodiscussanymeasurementofthegraphinterms
i
of its spatial meaning.We have proposed two further measurements of the graph that
may be useful for understanding the perception and use of architectural spaces. The
measures arejustifiedto some extentbythe application ofsimilar metrics tographs of
urbanandbuildingenvironments,andbytheirrelevancetoongoingresearch;however,
they are also intended as examples of the wider set of graph measures available. The
clustering coefficient C demonstrates a local measure of the graph, since it depends
i
only on the relation between vertices in a neighbourhood, whereas the mean shortest
path length L(cid:22) demonstrates a global measure of the graph, in that for each vertex it
i
depends on the relative placement of all other vertices in the graph.We have shown
resultscomparing the levelofoccupation ofrooms found in abuilding with the results
of an L(cid:22) analysis of that building and we have demonstrated that there is some
i
quantitative correspondence between the two.
In architectural composition, a process of visualisation of space as being poten-
tiallyoccupied bygroups ofoccupants and sequences ofevents is essential, though not
necessarily conscious. Hill (1998, page140) writes: ‘‘The architect and user both pro-
duce architecture, the former by design, the latter by inhabitation. As architecture is
designedandexperienced,theuserhasascreativearoleasthearchitect.’’Inthissense,
sets of locations within the isovist of a point determine conditions of copresence of
occupants and hence potential action and interaction.The isovists we employare used
to derivethegraph ofintervisiblelocations and hencethevisibilitygraph is atoolwith
which we can begin consciously to explore the visibility and permeability relations in
spatial systems.We must of course be careful to note that any population of a space
willleadtochangesinthevisualfieldwhichwehave notconsidered andthat members
of the population will experience a space through their personal memory of the
previous spaces they themselves have moved through. However, bylooking atrelation-
ships atboth a local and aglobal level, wehope to capture the common experience of
that space, and so visibility graph analysis may represent a step towards exploring the
relationship between architects, as designers ofspaces, and users, as architects oftheir
own experience of space.
Acknowledgements. The authors would like to thank Dave Chapman and Fotini Kontou who
helpedwiththeearlydevelopmentofvisibilitygraphanalysis,theSpaceSyntaxLaboratory,UCL,
whichhelpedwithtesting,andthe anonymousreferees fortheircomments andsuggestions.The
VRCentrefortheBuiltEnvironmentisfundedbytheOfficeofScienceandTechnologythrough
a Foresight Challenge Award. David O’Sullivan is supported byan EPSRC Studentship held at
the Bartlett Facultyof the Built Environment administered by the Centre for Advanced Spatial
Analysis.

120 ATurner, MDoxa, D O’Sullivan,APenn
References
AmidonEL,ElsnerGH,1968,‘‘Delineatinglandscapeviewareas:acomputerapproach’’,Forest
ResearchNotePSW-180,USDepartmentofAgriculture,Washington,DC
BenediktML,1979,‘‘Totakeholdofspace:isovistsandisovistfields’’EnvironmentandPlanning B
647^65
BenediktML,BurnhamCA,1985,‘‘Perceivingarchitecturalspace:fromopticraystoisovists’’,
inPersistenceandChangeEdsWH Warren,REShaw(LawrenceErlbaumAssociates,
London)
BurroughPA,1986PrinciplesofGeographicalInformationSystemsforLandResourcesAssessment
(ClarendonPress,Oxford)
ConroyR,2000SpatialNavigationinImmersiveVirtualEnvironmentsPhDthesis,BartlettFaculty
oftheBuiltEnvironment,UniversityCollegeLondon,London
CurtisWJR,1996ModernArchitectureSince1900(Phaidon,London)
DavisLS,BenediktML,1979,‘‘Computationalmodelsofspace:isovistsandisovistfields’’
ComputerGraphicsandImageProcessing11(3)49^72
deArrudaCamposMB,1997,‘‘Strategicspace:patternsofuseinpublicsquaresofthecityof
London’’,inProceedingsoftheFirstInternationalSymposiumonSpaceSyntaxSpaceSyntax
Laboratory,BartlettSchoolofGraduateStudies,UniversityCollegeLondon,London
deBergM,KreveldvanM,OvermarsM,SchwarzkopfO,1997ComputationalGeometry(Springer,
Berlin)
DeFlorianiL,MarzanoP,PuppoE,1994,‘‘Line-of-sightcommunicationonterrainmodels’’
InternationalJournalofGeographicalInformationSystems8329^342
FisherPF,1991,‘‘Firstexperimentsinviewsheduncertainty:theaccuracyoftheviewshedarea’’
PhotogrammetricEngineeringandRemoteSensing571321^1327
FisherPF,1995,‘‘Anexplorationofprobableviewshedsinlandscapeplanning’’Environment
andPlanning B:PlanningandDesign22527^546
FisherPF,1996,‘‘Extendingtheapplicabilityofviewshedsinlandscapeplanning’’Photogrammetric
EngineeringandRemoteSensing621297^1302
FutagawaY,NeumeyerF,1995MiesvanderRohe:GermanPavilion,InternationalExposition,
Barcelona,Spain,1928^29(reconstructed1986),TugendhatHouse,Brno,Czecho,1928^30
(ADAEdita,Tokyo)
GallagherGL,1972,‘‘Acomputertopographicmodelfordeterminingintervisibility’’,inThe
MathematicsofLargeScaleSimulationEd.PBrock(SimulationCouncils,LaJolla,CA)
pp3^16
GibsonJJ,1979TheEcologicalApproachtoVisualPerception(HoughtonMifflin,Boston,MA)
GiedionS,1971ArchitectureasthePhenomenaofTransition(HarvardUniversityPress,Cambridge,
MA)
HansonJ,1994,‘‘‘Deconstructing’architects’houses’’EnvironmentandPlanning B:Planning
andDesign21675^704
HansonJ,1999DecodingHomesandHouses(CambridgeUniversityPress,Cambridge)
HillJ,1998OccupyingArchitecture(Routledge,London)
HillierB,HansonJ,1984TheSocialLogicofSpace(CambridgeUniversityPress,Cambridge)
HillierB,PennA,1992,‘‘Densecivilisations:theshapeofcitiesinthe21stcentury’’Applied
Energy43(1)41^66
HillierB,PennA,HansonJ,GrajewskiT,XuJ,1993,‘‘Naturalmovement:or,configuration
andattractioninurbanpedestrianmovement’’EnvironmentandPlanning B:Planningand
Design2029^66
HillierB,PennA,DaltonN,ChapmanD,RedfernF,1995,‘‘Graphicalknowledgeinterfaces:
theextensiveandintensiveuseofprecedentdatabasesinarchitectureandurbandesign’’,in
VisualDatabasesinArchitectureEds AKoutamanis,HTimmermans,I Vermeulen(Avebury,
Aldershot,Hants)pp197^227
HillierB,MajorMD,DesyllasJ,KarimiK,CamposB,StonorT,1996,‘‘TateGallery,Millbank:
astudyoftheexistinglayoutandnewmasterplanproposal’’,technicalreport,BartlettSchool
ofGraduateStudies,UniversityCollegeLondon,London
HussRE,PumarMA,1997,‘‘Effectofdatabaseerrorsonintervisibilityestimation’’
PhotogrammetricEngineeringandRemoteSensing63415^424
Kru«gerMJT,1979,‘‘Anapproachtobuilt-formconnectivityatanurbanscale:systemdescription
anditsrepresentation’’EnvironmentandPlanning B667^88
LeeJ,StuckyD,1998,‘‘Onapplyingviewshedanalysisfordeterminingleast-costpathsondigital
elevationmodels’’InternationalJournalofGeo-InformationScience12891^905

From isovists tovisibilitygraphs 121
LloberaM,1996,‘‘Exploringthetopographyofmind:GIS,socialspaceandarchaeology’’
Antiquity70612^622
LynchK,1976ManagingtheSenseofRegion(MITPress,Cambridge,MA)
MarchL,SteadmanP,1971TheGeometryofEnvironment(Methuen,London)
MillsK,FoxG,HeimbachR,1992,‘‘Implementinganintervisibilityanalysismodelonaparallel
computingsystem’’ComputersandGeosciences181047^1054
OreO,1963GraphsandTheirUses(RandomHouse,NewYork)
PeponisJ,WinemanJ,RashidM,HongKimS,BafnaS,1997,‘‘Onthedescriptionofshapeand
spatialconfigurationinsidebuildings:convexpartitionsandtheirlocalproperties’’Environment
andPlanning B:PlanningandDesign24761^781
SteadmanP,1973,‘‘Graphtheoreticrepresentationofarchitecturalarrangement’’Architectural
ResearchandTeaching2161^172
TandyCRV,1967,‘‘Theisovistmethodoflandscapesurvey’’,inSymposium:MethodsofLandscape
AnalysisEd.HCMurray(LandscapeResearchGroup,London)pages 9^10
vanFraassenBC,1980TheScientificImage(ClarendonPress,Oxford)
WangJJ,RobinsonGJ,WhiteK,1996,‘‘Afastsolutiontolocalviewshedcomputationusing
grid-baseddigitalelevationmodels’’PhotogrammetricEngineeringandRemoteSensing62
1157^1164
WattsDJ,StrogatzSH,1998,‘‘Collectivedynamicsof‘small-world’networks’’Nature393440^442
WheatleyD,1995,‘‘Cumulativeviewshedanalysis:aGISbasedmethodofinvestigating
intervisibilityanditsarchaeologicalapplication’’,inArchaeologyandGIS:AEuropean
PerspectiveEds GLock,ZStancic(TaylorandFrancis,London)
WilsonRJ,1996IntroductiontoGraphTheory(Longman,Harlow,Essex)
WilsonRJ,BeinekeLW(Eds),1979ApplicationsofGraphTheory(AcademicPress,London)

(cid:223)2001aPion publicationprintedinGreatBritain
