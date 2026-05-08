Title: Integrating space syntax with spatial interaction

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/survey_paper/pdfs/phase1_foundational/04_Integrating_Space_Syntax_with_Spatial_Interaction_Batty2022.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T02:56:59+00:00
- page_count: 23
- status: ok
- text_char_count: 86016

Metadata:
- author: Michael Batty
- doi: 10.1007/s44212-022-00004-2
- keywords: Spatial interaction;Space syntax;Density;Accessibility;Primal and dual representations;Applications to greater London
- subject: Urban Informatics, https://doi.org/10.1007/s44212-022-00004-2

Outline:
- Integrating space syntax with spatial interaction (page 1)
  - Abstract (page 1)
  - 1 Preamble: the problem context (page 1)
  - 2 The generic representation of the network (page 3)
  - 3 Distance: the key to explaining movement in space syntax and spatial interaction (page 6)
  - 4 Models for predicting movement and location (page 9)
    - 4.1 A probabilistic interpretation of distance and connectivity (page 10)
    - 4.2 A comparison of distance and probability measures (page 12)
    - 4.3 An empirical demonstration of primal-dual integration (page 13)
    - 4.4 An integrated approach (page 19)
  - 5 Conclusions: next steps (page 21)
  - Acknowledgements (page 23)
  - References (page 23)

Markdown Content:

Batty Urban Informatics (2022) 1:4
https://doi.org/10.1007/s44212-022-00004-2 Urban Informatics
ORIGINAL ARTICLE Open Access
Integrating space syntax with spatial
interaction
Michael Batty*
Abstract
In this paper, we attempt to compare space syntax with spatial interaction. At one level, these two approaches to
urban spatial structure are non-comparable. Space syntax is largely a descriptive technique for visualising spatial
relations at the level of connections between places while spatial interaction is a predictive model that forecasts how
much travel there will be between places. Space syntax articulates the system in terms of whether or not a physical
link, usually at the level of the street, exists while spatial interaction predicts movements between all origins and desti-
nations which are places often anchored in terms of the street network, but which at the level of prediction, assume
connections between all places. Space syntax is grounded at a fine spatial scale while spatial interaction defines
places as aggregates of activity in larger zones than the scale of the street system. The main output of space syntax
is a connectivity matrix of step lengths between streets whereas in spatial interaction, such networks are predeter-
mined, measurable in terms of Euclidean distance or generalised cost of travel, and the output is the volume of travel
prior to this being assigned usually to a street network.
There is however a fundamental way of relating the implicit network graph of spatial interaction to the explicit planar
graph of the street network. We begin by assuming the planar graph of the network is conceived of as a primal prob-
lem of spatial interaction while the dual graph linking streets in the planar graph is the graph which is used in space
syntax. We exploit this duality and show how we can move easily between spatial interaction as the primal and space
syntax as the dual. This is rooted in a more fundamental graph – the bipartite graph which is a list of streets/arcs and
their intersections/nodes from which the primal and dual emerge naturally. We explore various accessibility measures
and show how they relate and correlate. We then go one step further and consider how various processes of random
walking take place in these networks examining the steady states of the primal and dual problems in terms of the
likelihood of a random walker visiting any node or street. We thus define primal and dual Markov chains that enable
us to generate these probabilities. This provides a basic framework for comparing primal and dual in comparing
spatial interaction with space syntax. We illustrate these measures on simple and easy to articulate graphs, extending
this to a synthetic network of nearest neighbour links in Greater London based on 699 nodes and 1972 symmetric
‘streets’ between zones. This is a preliminary attack on the problem of linking these two approaches although many
challenges remain.
Keywords: Spatial interaction, Space syntax, Density, Accessibility, Primal and dual representations, Applications to
Greater London
1 Preamble: the problem context
Space syntax is a descriptive technique for working out
the relative accessibility or nearness of a set of spaces,
*Correspondence: m.batty@ucl.ac.uk often defined as streets, to one another. This enables
comparisons of their relative nearness to the movement
CASA, University College London, 90 Tottenham Court Road, London W1T
4TJ, UK associated with each space or street. The assumption is
© The Author(s) 2022. Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which
permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the
original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or
other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line
to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory
regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this
licence, visit http:// creat iveco mmons. org/ licen ses/ by/4. 0/.

Batty Urban Informatics (2022) 1:4 Page 2 of 23
that movement increases linearly with accessibility while however are measures of (trip-making) activity at differ-
accessibility in this context is often called integration. It is ent locations, generalised distance between locations,
defined by first identifying a set of streets which are usually and parameters that define the relative weight of these
lines of unobstructed movement, sometimes called axial activities and distances. Space syntax is more parsimo-
lines, and then observing whether or not any one street is nious being based on logical links between spaces and
connected to any other which is defined if any two streets forming accessibilities from these. Its only independ-
are connected (Hillier, 1996). The set of links between ent variable is the defined topology of the links which in
streets forms an interaction matrix which can be viewed as some instances have been extended to other geometric
a topological or binary graph on which various operations properties such as street orientation based on angular
can take place, for example, to find shortest routes from variations. These might be parameterised (weighted) but
any link to any other which are then used to define the rel- there are few if any examples which follow in this direc-
ative importance or accessibility of one link to any other. tion. After the model has been built, accessibilities are
When these accessibilities are summed for each particular then compared with movement; if a strong linear rela-
link, this gives the relative accessibility of a link. One of the tionship exists, then occasionally the model has been
features of space syntax is that it works with binary (0–1) used to predict movement, usually in situations where
links between streets and Euclidean distance or cost is not new street links are added as part of a design.
a feature of the analysis. The model is only predictive when There are hints in the wider literature involving trans-
the accessibility values for each street are associated with portation, traffic assignment, and flows on networks of
observed movement in each street which is occasionally ways in which spatial interaction models might be linked
used to build a predictive model. to space syntax but the difficulties of doing so have defi-
Spatial interaction models, on the other hand, pre- nitely thwarted such developments. As we argue here,
dict movement directly between a set of locations that such an integration involves going one step back and
can sometimes be interpreted as intersections between finding a common form of representation for networks
streets but are usually more generic – centroids defin- from which consistent comparisons and integrations can
ing a location or area – and apply at different spatial be made and this is the core of the argument here. In the
scales. Interaction or movement is directly proportional wider field, there is a focus on pedestrian movement on
to activities that are located at different locations and streets involving such models which link graph theory
inversely proportional to some measure of the length of (Sevtsuk, 2021), on using syntax to compare different
the street measured as some generalised metric incor- modes of transport (Law et al., 2012), but the main devel-
porating physical distance, travel cost and/or travel time. opments have come from Korean researchers who have
The model thus predicts movement as a function of these broached the flow model based on gravity and its discrete
independent variables. Accessibility measures consist- choice equivalents in linking spatial interaction to space
ent with the model’s predictions can be derived but these syntax (Jang, 2019, Kim et al., 2016).
pertain to locations, not streets or links between these The key link here between the two types of model
locations. The models are parameterised in such a way relates to the underlying network between locations.
that movement is estimated to be as close as possible to Both techniques begin with the physical network. Spa-
observed data flows and in this sense, the focus is on pre- tial interaction models predict flows directly from this
diction rather than description. and other locational data. Space syntax works out acces-
There are several key differences between space syn- sibilities from this network and then compares these to
tax and spatial interaction. Space syntax is essentially a real data and if the correlation is good, a linear model
descriptive measure of street accessibility which is related can be fitted and used for prediction. The common key
to movement in a comparative rather than predictive way. is the network but there the similarity ends. In spatial
It is not parameterised and as such, there is no estima- interaction, a network is defined as a set of intersections
tion or calibration procedure used to operationalise the between segments – nodes and arcs – which is meas-
model. There is nothing in the technique that generates ured by some generalised distance or cost. The network
movement as in spatial interaction models. Space syn- does not privilege nodes or arcs in any particular way
tax does not deal with locations but with links between as this is the assumed backcloth on which spatial inter-
locations – streets – which in turn are defined as linear action takes place. In space syntax, one begins with the
spaces. Links between these spaces are represented not same network but from these, sets of segments that have
in terms of distance but as logical links which define a their own integrity are defined as sequences of links.
topological network. And space syntax does not incor- These form ‘streets’ and are in general composed of more
porate any measures of activity associated with locations. than one segment. Once these streets have been defined,
The independent variables in spatial interaction models space syntax defines connections between streets as the

B atty Urban Informatics (2022) 1:4 Page 3 of 23
existence (1) or not (0) of a node in the original network third dimension, includes one way movements, or segments
that defines whether or not the streets are connected. In that cross one another without intersecting. In this context,
some sense, this is the dual of the original network which we will deal exclusively with networks in two dimensional
we might think of as the primal but as streets can be con- space where distance is measured using Euclidean geom-
structed from more than one segment, this need not be a etries and the graph is planar (Barthélemy, 2011) The basic
strict dual. We will however refer to the space syntax net- common ground between these two approaches is essen-
work as the dual and the original street segment network tially a structural network of locations and paths of move-
as the primal for in some senses, this is the key difference ment between: it is a graph whose elements are unweighted
contained in the distinction between the two approaches. binary links. There is nothing else which is common to the
In fact, whether one uses the dual or the primal in space two models and space syntax only uses this graph to derive
syntax does not make that much difference to the ulti- many kinds of prediction and insight from the model. Spa-
mate computations of accessibility (see Batty, 2013 for tial interaction takes this graph as a skeletal network, loads
a detailed explanation and comparison) but it is not our or weights it with Euclidean distances or costs along its
main purpose here to focus on these empirical differ- segments, then if incomplete, works out shortest routes to
ences and similarities. Our quest is to see how close the produce a full distance or travel cost matrix and then pro-
two models are and how one might be linked to the other. ceeds to use this as one of the basic inputs to the model that
In the sequel, we will begin with the common key to both predicts flows between locations. In short, space syntax is
space syntax and spatial interaction which is the network. very different from spatial interaction and it might be sup-
We will first develop a generic representation of the network posed that there is little point in trying to compare these as
from which the space syntax and spatial interaction variants their basic networks of interaction are not the same. But as
can be defined. In essence, we invoke the idea of a pre-graph we will see, there is some interest in making a comparison
– a bipartite graph linking intersections/nodes/junctions or because both models deal with location and movement,
zone centroids to segments/links or arcs that are some form and thus it is worth attempting to see how spatial interac-
of route such as streets. From this bipartite graph, all else can tion ideas can inform space syntax and vice versa.
be derived but it is important to note that these tools and To provide the requisite intuition for the problem, let
models are a limited set of possible forms that can be defined us propose a hypothetical planar graph of a street system
as graphs, and the way its links can be measured. Other con- where the nodes are the intersections between the lines
ceptions and variables based on locations associated with an (arcs or segments) which are the streets. In Fig. 1 (a), we
underlying generic network can be defined but these are not show such a street network which is composed of N 5
=
directly related to space syntax (Marshall, 2015). intersections and L 8 streets. This network is highly
=
simplified: it is symmetric, that is the graph G(N, L) is
2 The generic representation of the network
non-directed and there are no self-loops. We have not
Networks in space syntax and spatial interaction are usually specified any weights for the links in this graph and thus
embedded in two-dimensional space defined by locations it relates only to the system’s topology.
which are points where street or route segments intersect. Clearly the planar graph which is Fig. 1(a) links the 8
In general, these networks are planar graphs although this streets through 5 intersections which are numbered by
can be complicated if the representation extends into the the dark circles with the solid line representing street
a b
Fig. 1 The Primal (a) and Dual (b) Graphs and Adjacency Matrices of an Hypothetical Street Network. Note that the primal links nodes which are
street intersections to one another through streets while the dual links streets to one another through nodes or street intersections

Batty Urban Informatics (2022) 1:4 Page 4 of 23
segments. In Fig. 1(b), the streets are numbered by the V = ATA
jℓ j jk kℓ (2)
dark squares and a solid line is drawn if two streets are
(cid:31)
connected through a common intersection. In the pri-
Expressed in matrix notation eqs. (1) and (2) can be
mal problem, each street has no more than two intersec- written as U AAT and V ATA.
tions where it joins other streets while in the dual each = =
To provide some sense of what the primal and dual of
street only intersects once with another street. It is this
these operations means, it is best that we introduce a
that can be relaxed in space syntax where a single street
simple worked example where we anticipate that the spa-
segment can intersect with several different street seg-
tial interaction matrix is one where each line links two
ments and this changes the meaning of intersections. In
and only two nodes i.e. there are only ever two nodes
fact, in this paper, arguably the graphs we define, which
which represent the beginning and end of each line,
do not allow a street to have more than 2 intersections,
while the space syntax matrix (associated with this spatial
miss some of the key elements of urban structure but it
interaction problem) is the opposite – the dual – where
is a generic criticism of space syntax anyway in that the
each line is now considered as a node and from two such
starting point is always a planar graph of local or near-
nodes, there is only one line. To derive the general space
est neighbour links. If the planar graph has N nodes,
syntax problem we need to relax this requirement but to
there are always many less than N2 links, that is L < < N2.
produce the clearest example, we will adopt this simpli-
What we require is a method for building primal and
fication, and there is no loss of generality in proceeding
dual network graphs from the same basis and to this end,
this way. Now the matrix A can be graphically displayed
we begin with the planar graph and a list of nodes that
as a bipartite graph (Borgatti & Everett, 1997) where we
are associated (or not) with a list of streets. The starting
link nodes to lines – street intersections to streets. The
point for both techniques is thus the skeletal network of
example we used in Fig. 1(a) has N 5 nodes and L 8
links between N nodes each of which we will define as = =
lines whose matrix and bipartite graph are defined as.
i 1, 2, 3, …, N, and L lines (segments or arcs) defined as
=
j 1, 2, 3, …, L. The basic representation is given by the Note we define the 5 nodes as 1, 2, …, 5 and the 8 lines
=
matrix A {A } which is a binary matrix where A 1 if as 1,2, …, 8 with no ambiguity from the above definitions.
= ij ij=
node i is linked to line j and A 0 if no such link exists. The matrix, as we have been at pains to point out, simply
ij=
From this matrix, we can define the two basic matrices records which street node or street intersection is associ-
used in spatial interaction and space syntax. First the ated with which each street line.
skeletal spatial interaction matrix which we call the pri- The two spatial models that we are examining take this
mal counts the links between nodes as information and deal with it in consistent but different
ways. The spatial interaction model works by defining a
U = A AT
ik j ij jk (1) matrix of interactions between intersections which are
assumed to be centroids around an areal location and uses
where the transpose operator T reorders the basic matrix this matrix to predict the amount of movement. Then from
A as A T. The space syntax matrix is the dual of this oper- eq. (1) using the above bipartite graph we form the interac-
ation and is formed as tion matrix U (as)

B atty Urban Informatics (2022) 1:4 Page 5 of 23
This is the primal problem. The dual involves defining how
each street line is connected to any other, thus forming an inter-
action matrix V between street lines rather than street nodes
and this defines a related graph. Then from eq. (2) we get.
It is quite clear that if these operations are accom-
If we compare the matrices U and V with the left and
plished, the matrices U and V are sliced to remove the
right matrices in Fig. 1, then we can easily see that these are
path lengths and ensure that the matrices remain binary,
the same except the main diagonal elements of each of these
leading to the matrices X and Y. These are the same as
matrices are equal to zero. In fact the main diagonal ele-
those in Fig. 1 which we repeat here as
ment reflects the number of paths in the graph to get from
one node to the same. In the definition of U above, you can ⎡ 01110 ⎤
10101
see that there are 3 steps to go from node 1 to itself and so ⎢ ⎥
X =⎢11011⎥
on which are displayed from the juxtaposition of the two
⎢10101⎥
bipartite graphs and matrices A and A T. For V, there are 2 ⎢ ⎥
⎣01110⎦
steps to get from node 1 to node 1 via two lines and so on.
One final step remains to get the skeletal configuration
and
matrices used for the two models and to do this, we need to
01111000
slice out any links with more than one path and get rid of the ⎡ ⎤
self-links. Then the two matrices in question which define
⎢10110110⎥
⎢11000011⎥
the primal and dual problems can be formed as follows: ⎢11001110⎥
Y =⎢ ⎥
X = 1if U ik ≥1,i�=k ⎢ 10010101 ⎥
ik 0if U >0,i=k ⎢01011011⎥
ik
� 1if V ≥1,j �=ℓ  (3) ⎢01110101⎥
Y jℓ = 0if V jℓ >0,j =ℓ  ⎢ ⎣00101110 ⎥ ⎦
jℓ
�


Batty Urban Informatics (2022) 1:4 Page 6 of 23
3 Distance: the key to explaining movement where w 1 U >w 2 U >w 3 U >... Note that we order these so
in space syntax and spatial interaction
closer/lower step lengths have more weight and these are
The matrices U and V give the number of paths of one then applied to the number of paths at each step. The sec-
step between their respective nodes and X and Y show ond distance measure is thus
the one step paths excluding the self-loops. The sim-
n
plest way of forming a distance between any two nodes δ i U k (n)= z=1 w z UU ik (z) (8)
in either the spatial interaction or the space syntax prob-
(cid:31)
lem is to use a very well-known technique which involves and the other three measures can be defined accordingly
computing these from powers of these matrices. As these δ i X k (n),δ j V ℓ (ℓ),δ j Y ℓ (ℓ) .
operations are identical for any square matrix, we will It is now worth demonstrating what these two sets of
only illustrate them for one of these – the U matrix – and distance measures actually show for our hypothetical
simply state the related results for the other matrices. example. The simplest distance measures are the step-
Then the number of paths of two step length between any distances where the value of the link between any two
two nodes is given by powering the number of one step nodes is the number of steps a walker would have to
paths in matrix U(1) = U by U, that is make between one node and any other (for X via the
street system) and between any street and any other
U(2)=U(1)U =U2
(4)
(for Y via the intersection nodes). These matrices are
easy to compute from the algorithm implied by eq. (7)
and by recursion, the number of n path lengths is
for our example. Then these step distances are
U(n)=U(n−1)U =Un
(5)
21112
12121
All the other results follow and we can state them as
DX = DX =11211
ik
V(ℓ)==Vℓ; X(n)==Xn; Y(ℓ)==Yℓ
(6) 
12121

� � 21112
 
These equations give the number of path lengths with  
and without the original self-loop and although we and
might conjecture that the number of path lengths co-
⎡21111 222⎤
varies with the accessibility or centrality of a node or ⎢ ⎥
⎢12112112⎥
street, then we still need to provide some measure of this ⎢ ⎢11222211 ⎥ ⎥
a p c a c th es l s e i n bi g l t it h y s t fr h o a m t a r t e h e p s o e s i l t e iv n e g , t h th s e . n I n w e fa n c e t e t d o to ge p n o e w ra e t r e th al e l DY= � D j Y 𝓁 � = ⎢ ⎢ ⎢ ⎢ 1 1 1 2 2 2 2 1 1 2 1 1 1 2 2 1 ⎥ ⎥ ⎥ ⎥
matrices up to N or L to make sure we get all of these.
⎢
⎢
21211211⎥
⎥
We can form two kinds of distance from these path
⎢
⎢
21112121⎥
⎥
lengths. First we want to find the shortest path length
⎢ ⎣22121112⎥
⎦
for any pair of nodes and use this as a measure of dis-
and it is easy to confirm that these simple path lengths
tance. To do this we examine the number of path
with no more than 2 steps are those that result from cas-
lengths at any iteration of eq. (4) and if this number is
ual inspection of the graphs in Fig. 1.
different from zero when the number of path lengths on
These matrices are clearly very crude measures of
the previous iteration is zero, we set the distance to the
accessibility but as they are very simple graphs and only
value of the power – the step length. Then for U
based on binary relations, this is to be expected. The
if U ik (n)>0 and U ik (n−1)=0 then D i U k =n numbers of path computations are more detailed and
(7) these literally explode as we take more and more powers
and all the other step-length distances follow as D V, of the matrix for in bigger graphs, there is an exponen-
D X, D Y. This is a rather blunt measure in that it is con- tially growing number of circuits. To show this, we indi-
cate the number of paths for the matrices U(N 5) U 5
sistent with binary step lengths but does not incor- = =
and for V(L 8) V 8. These are computed as
porate actual travel times or costs, or even Euclidean = =
distances or travel costs which we will note a little later 20191897292918971776
but for the time being this can be regarded as our first 18972019292917761897
measure of accessibility or integration as it is sometimes
U5 =29292929466029292929
18971776292920191897
called in space syntax. The second measure is based on  
17761897292918972019
a weighted sum of the path lengths. Let us assume a set  
of weights one for each step length and we call these w z U  

B atty Urban Informatics (2022) 1:4 Page 7 of 23
and destination (nodes) while space syntax is associated with
flows along streets that need to be aggregated from the
⎡12461505116515051165142414241084 ⎤
⎢ ⎥ relative positioning of any one street connected to all
⎢15051938150518971424185718971424 ⎥
⎢ ⎥ others. In short, both models make use of accessibilities
⎢11651505124614241084142415051165 ⎥
V8= ⎢ ⎢15051897142419381505189718571424 ⎥ ⎥ which are summations of interactions; in spatial inter-
⎢ ⎢11651424108415051246150514241165 ⎥ ⎥ action, we predict flows from information about i ↔ k
⎢14241857142418971505193818971505 ⎥ nodes as well as flows into i and k whereas in space syn-
⎢ ⎥
⎢ ⎢ 14241897150518571424189719381505 ⎥ ⎥ tax, the flows between streets j ↔ ℓ have no meaning
⎢ ⎣10841424116514241165150515051246⎥
⎦ and what we need to do is model the notional flows that
take place on each street j and ℓ. Thus it is accessibilities
The weights for combining the path numbers up to the
that we need to be concerned with here. As these are all
total number of steps U(N = 5) = U 5 and V(L = 8) = V 8 defined the same way as summations of distance meas-
are based on the simple expediency of making the
ures into nodes whether these nodes be intersections or
weight proportional to the total maximum path lengths
streets, then we will just illustrate these for the step dis-
N or L less the step length being considered, that is, tances D U and D V. As space syntax uses the step distance
w i U(n)∝N −n+1 or w i V(ℓ)∝L−ℓ+1 . The weighted measures D V as the core element in its tool box, we first
distances for the spatial interaction and space syntax var- define the total step distance for street j as d j V and nor-
iants are thus computed as
malise this by the maximum step distance m as
dˆ
j
V
so that
194176269176159 comparisons can be made between systems with different
176194269159176 numbers of streets; these measures are
δU(5)= δU(5) =269269437269269 
ik dV = DV
176159269194176 j ℓ jℓ
 
� �   159176269176194   dˆV = d j V (cid:31)= ℓ D j V ℓ (cid:30) (9)
  j m (cid:31) m
and
1273016167125941616712594160301603012457
1616720712161672064316030205752064316030
1259416167127301603012457160301616712594 
1616720643160302071216167206432057516030
δV(8)= δV(8) = 
ik 1259416030124571616712730161671603012594 
 
� �   1603020575160302064316167207122064316167  
1603020643161672057516030206432071216167 
 
1245716030125941603012594161671616716167 
 
 
We are at last in a position to say something about These measures although referred to as measures of
these distances/path numbers/step lengths relative to integration by Hillier and Hanson (1985) are in fact
the problem shown in Fig. 1. It is very clear that there is measures of ‘inaccessibility’ and in most space syntax
little discrimination between the relative positioning of applications, the inverse of this measure is used to define
the nodes as intersections in the primal and the nodes as what they call integration. In most recent applications,
streets in the dual. That is, the graphs are symmetric and the measure integration appears to have been dropped
strongly connected and intuitively if we were to measure and the more common measure of accessibility following
the relative importance of the nodes in each graph, their conventional usage in spatial interaction and transporta-
in-degrees (and out-degrees as the graphs are symmet- tion modelling after Hansen (1959) is now being used. In
ric) would not show much variation. In the primal it is fact the measure is usually taken as the inverse of depth
clear that the central node 3 seems most important while d j V or dˆ j V and normalised to sum to 1, that is
in the dual, nodes 1, 4, 6 and 7 form a central block that
1/dV
has more importance than the outer block that consists d¯V = j , d¯V =1
of nodes 1, 3, 5 and 8. j ℓ 1/d ℓ V j j (10)
(cid:30)
Spatial interaction models usually predict both the
(cid:31)
relative flows between nodes that take place along streets This measure is sometimes referred to as real relative
as well as the total flows destined for each origin and asymmetry although it is unclear where the term comes

Batty Urban Informatics (2022) 1:4 Page 8 of 23
from and what the asymmetry is that is being referred to show variations in intensity for both the distance-step
(Bafna, 2003). What happens in space syntax is that as matrices and their accessibilities. We will not explore the
the measure in eq. (10) is associated with the street sys- weighted path number distances in eqs. (8) at this point
tem, the relative variations in the measure (which is the here but keep these in mind for later applications.
average or total depth of any one street to all others) is You can see clear relations between the primal – the
plotted for each street across the red-yellow-green-blue spatial interaction problem – and the dual – the space
colour spectrum to produce the typical space syntax syntax problem – where we simply map the accessibili-
map. The primal problem has accessibilities associated ties into street intersections and street segments in the
with the nodes which are locations at street intersections. primal and dual respectively but on the planar graph of
In exactly the same way, we form the same accessibilities the network which we show in Fig. 3. It is essential to
and for completeness we define these as follows note that there is an intrinsic asymmetry between spa-
d i U= � k D i U k ; d̂ i U= d n k U = ∑ k n D i U k; d̄ i U=∑ 1 k ∕ 1 d ∕ k U d k U , � i d̄ i U=1 (11) t n i a a r l g in r t a e p r h a c w ti h o i n c h a n li d es s a p t a t c h e e s b y a n s t i a s x o i f n t h t e h a n t e w tw e o u rk se i n th s e p a p t l i a a - l
interaction to represent both problems. In short, in space
The accessibilities show the relative intensity of flows syntax we collapse the movement onto nodes that define
at an intersection. If it is required to examine particular the streets whereas in spatial interaction we deal directly
flows as in the space syntax dual, then the actual distance with movement on streets as we will elaborate below.
measures need to be used to make these comparisons but
this has not been done in space syntax for in comput-
ing these distance matrices, few have broached the kind
of predictive modelling that spatial interaction requires.
In short although space syntax focuses primarily on the
geometry and topology of the street network, the street
network is simply the starting point for spatial interac-
tion and the accessibility measures – in fact an essential
part of spatial interaction modelling – are used quite
differently from those in space syntax. At this point, we
have a common framework for computing relative meas-
Fig. 3 Accessibility Levels for the Primal and Dual Problems on the
ures of nearness or accessibility in both the primal and Planar Network
the dual and in Fig. 2 we show how we can map these to
Fig. 2 The Primal and Dual Spatial Graphs and Their Accessibilities. The Nodes in the Primal are Street Intersections and the Nodes in the Dual are
the Streets

B atty Urban Informatics (2022) 1:4 Page 9 of 23
4 Models for predicting movement and location a street as d j V = ℓ D j V ℓ , then the interactions between
Operations on the primal and dual network graphs do streets D j V ℓ are act (cid:31) ually flows. In spatial interaction mod-
not lead to predictions of movement but to measures of elling, however the flows are always unambiguously
connectivity which define indices of accessibility and dis- associated with movements as measured by vehicular
tance. These indices might then be considered as being passenger traffic, migration, freight and so on. There is
variables that can be associated or compared with activi- a third problem that is more generic. In spatial interac-
ties at locations or movement along streets between tion modelling, flows are predicted between all intersec-
locations but this is an additional stage in the analysis. tions or nodes in the street network whereas in space
In spatial interaction modelling for example, distances syntax, the underlying planar graph does not connect
are central to predicting movements but these are usu- everywhere with everywhere else directly and thus flows
ally defined a priori and although measures such as the can only be measured on the direct links in the graph.
step distance (or the path) matrices D U, D X and their In short whereas in spatial interaction modelling as we
accessibilities d U, d X could be used as independent vari- have direct links such as ik and kz, we also have iz which
able inputs, they are not quite in the form required for does not necessarily exist as a line segment in the planar
the standard models. In terms of the distance matrices street graph. In short, in space syntax, we only examine
D V, D Y and their accessibilities d V, d Y for the dual space direct links in the graph which are associated with nodes
syntax problem, these are the only elements that can be j and thus many possible links do not appear in the graph
used to predict movement, and in this case, the distance whereas the implicit graph in spatial interaction model-
matrices simply indicate notional flows or interactions ling is completely connected. In short, in spatial interac-
between streets, that is D j V ℓ which do not have the mean- tion modelling, we distribute trips to all possible links
ing of actual flows of traffic per se. Only when these are between intersections or nodes regardless of whether a
aggregated to d j V are we able to compare these to the flow separate physical link exists whereas in space syntax, the
on the relevant street segments i ↔ k in order to see how flows are implicitly associated with those on a segment
good the fit is to real data. that are measures of traffic. Spatial interaction distributes
There are two problems with doing this however. First trips whereas space syntax assumes these trips have been
using the step lengths, the range of step lengths whereby already assigned to a physical network based on direct
a network becomes completely connected might be very street segments.
narrow. If you look at Fig. 1(b), the dual graph, then as we In fact what has been done in space syntax is to con-
have already worked out, there are only two step lengths struct models that explain movement as function of the
– 1, 2 – before the dual is completely connected; this is direct street segments in the graph using street acces-
far too small a variation to use in computing accessibili- sibility. Defining the observed movement in a street as
ties even though the range widens once the number of T i o k bs , we assume a simple regression such as
nodes is increased. In fact in a large network in the form
Tobs =α+βdV wherejisthesameasi↔k
of a chain, then the range of accessibilities would vary as ik j (12)
the number of nodes. However in typical networks which
tend to be at best a small set of large monocentric clus- Hillier et al. (1993) refer to this relationship as that gov-
ters at whatever scale of town one is looking at, the range erning ‘natural movement’ and their work shows that the
is much narrower than we might expect would explain only flows that are compared with accessibility are those
variations in movement. This is a major problem in space that are measured as composite totals on each link. These
syntax and is seen in the fact that when comparisons are not broken down into flows between all nodes in the
of accessibility measures from the dual are made with street graph, and thus implicitly occur after spatial inter-
movements along street segments, the scatter graphs are actions have been assigned to network links. This paper
characterised by a small number of measures of accessi- also reveals the problem of striation referred to above
bility all at integer value, and a much larger number of which concerns the fact that the accessibility values are
measures of movement. The appearance of these graphs integers and cover a narrow range. The levels of variance
in fact is not a random scatter but more a structured explained associated with these kinds of regressions are
striation. rarely more than 0.6 and due to the nature of the data and
The second problem is that the accessibilities which very often the small number of distinct observations, this
assume that a street is a node in the dual, are derived would not be regarded as a satisfactory predictive model.
from links to other streets – other nodes in the dual – In my view, the advantages of space syntax lie elsewhere
and that this implies some sort of flow from these other in much more qualitative but structured discussion of
streets. In short it is not clear that if we aggregate, say, how space is formed and how it is moulded with respect
the step distances in the dual to get the accessibility of to generic human interactions. In this context, it plays an

Batty Urban Informatics (2022) 1:4 Page 10 of 23
important role but essentially as we implied at the out- and this can be calibrated in the same way as above. This
set, it is not a predictive model and should not be used method of coupling spatial interaction to space syntax
as such. through the widely used measure of integration (accessi-
Notwithstanding this rather negative consequence, we bility) shows one way of integrating the two models but
will argue below that as it is virtually impossible to take due to the ambiguities about this index, we consider this
the standard spatial interaction model and derive space to be a weak method. Essentially spatial interaction relies
syntax from this and vice versa, it is still possible to make much more on Euclidean distance as some function of
progress by making changes to the formulation of both the generalized cost of travel. Nevertheless we could use
spatial interaction and space syntax and casting these in the number of paths from the space syntax problem V
a form where direct comparison and derivations of one or Y and the accessibilities formed from these, weighted
from the other can be made. However before this is illus- over many step lengths or simply based on some high
trated, we need to introduce spatial interaction as a pre- step length. This might be a preferable variant to eq. (15)
dictive model because it is still possible to use measures which we can write as
from the primal to structure its predictive capabilities.
The clearest way of introducing one of the many variants p =
exp −(cid:31)
ℓ
Vjℓ
wherejisthesameasi↔k
of spatial interaction is in conditional probability terms. k|i z ex (cid:31) p − (cid:30) (cid:31) ℓ V (cid:29)zℓ
Then (cid:30) (cid:31) (cid:30) (cid:29) (16)
This is closer to the model in eqs. (13) and (14) where
T =Ep
E i = k ik T ik = i E k i |i k p k|i (cid:30) where k p k|i =1 (13) w m e e a u s s u e r e g e o n f e d ra is li t s a e n d c e tr b av u e t l i c t o i s s t s w ti h ll i c a h v i e n r c y o w rp e o a r k a t c e o s u s p o li m ng e
(cid:29)
(cid:31) (cid:31) and is unlikely to find favour with those who consider
T is the flow or trips from zone or intersection i to
ik that much more powerful functions of deterrence need
k, E is some measure of the size of activity at location/
i to be used.
intersection i which is the flow to be distributed as trip
It is most unlikely that we can do better than this at
interactions, and p is the probability or fraction of E
k ∣ i i this stage for what we need is a much stronger method of
which is distributed as trips to k. This probability model
integration. We already have the key to this for it resides
is usually configured as the product of an attractor of
in the coupling of the bipartite graph whose matrix is A
the zone k, F and some function of the generalised dis-
k which separates nodes from lines in the original planar
tance/travel cost c from i to k which we hypothesise as
ik street network. At this point, let us speculate that the way
p = F k exp(−(cid:31)c ik ) forward lies in this approach and what we need to do is
k|i z F z exp(−(cid:31)c iz ) (14) find much better measures of distance that take account
of this coupling other than those based on step lengths.
(cid:31)
The independent variables are F and c and the The method we will adopt has been used before in sev-
k ik
model is calibrated by finding the value of the parame- eral contexts by the author (Batty, 2013) and it consists
ter λ which minimises some statistic of difference in slightly changing the nature of the two models so that
between observed and predicted trips g T i o k bs−T ik . In they intersect in a much more basic way. This we will
terms of the operations on the primal (cid:31)network gr(cid:30)aph, broach in the next section before we produce an inte-
grated model, ultimately demonstrating this on a large
then it is easy to see that c could be one of the meas-
ik
but simplified network of links and zones in Greater
ures derived earlier so in this form, additional variables
London.
are defined, or at least there needs to be a driver for
trip-making or movement such as E. There are many
i
variants of these models and the model in this form is 4.1 A probabilistic interpretation of distance
called singly-or origin-constrained (Wilson, 1970). and connectivity
In fact we might use the accessibility values for the We can first convert the raw interaction matrices U and
dual in eq. (14), rather than the distance values in the V into stochastic matrices where we interpret the cells as
primal and where we to drop the attractor, the equation being the probability of a node relating to another node
for the spatial interaction model becomes and the probability of a street relating to another street
respectively. Then we define these probabilities as
exp −(cid:31)dV
j
p k|i =
z
ex(cid:31)p −(cid:31)d(cid:30)
z
V wherejisthesameasi↔k P
ik
= U i
U
k ,
k
P
ik
=1
(17)
k ik
(cid:29) (cid:28) (cid:27) (15) (cid:30)
(cid:31)

B atty Urban Informatics (2022) 1:4 Page 11 of 23
and yet. Our purpose here is to work with relations where we
define the probabilities at a more elemental level.
V
jℓ
Q jℓ = ℓ V jℓ , ℓ Q jℓ =1 (18) tu T re o t i h n a t t r o d d e u te c r e m th in e e s s e , d w is e ta c n a c n e d m e e fi a n s e u r t e h s e o p n r o t b h a e b u il n it d y e s r t ly ru in c g -
(cid:30)
(cid:31) graph in terms of the basic data matrix A. Let us define the
We can interpret these as follows. If a walker starts at
probability of a node belonging to a street as
a node i, and then with probability P moves to node k,
ik
then the probability of that same walker visiting a node z A ij
G = , G =1
on the next step is given as ∑ k P ik P kz which is the respec- ij j A ij j ij (19)
tive element of the second power of the matrix. Then on (cid:30)
(cid:31)
the n’th step of the walk, we can compute the probability and
as P iz (n) = ∑ k P ik (n − 1)P kz which in matrix terms is given a street belonging to a node as
as P n P n − 1 P. This sequence defines a discrete Markov
= AT
chain and if the matrix P is strongly connected which it jk
C = , C =1
must be for the problem to be meaningful and the street jk AT k jk (20)
k jk
system connected, then it is well known that the limit of (cid:30)
(cid:31)
this sequence is a fixed point vector which we can call p. Now these matrices are stochastic and by concatenating
In short, if we begin the walk with a probability vector them to form the primal and dual probabilities, we define
p(1), the sequence updating this vector can be written as
p(n) = p(n − 1)P = p(1)P n − 1. As this vector converges to Pˆ ik = j G ij C jk , k Pˆ ik =1 (21)
p, then in the limit we can solve for p from p = pP. (cid:31) (cid:31)
An exactly analogous process exists if we begin with a and
walker on a street j who visits another street ℓ with prob-
Qˆ = C G , Qˆ =1
ability Q jℓ . In the limit, we can solve for the steady state jℓ k jk kℓ ℓ jℓ (22)
probability vector q qQ and this gives the overall prob- (cid:31) (cid:31)
=
ability of any walker visiting a street if the walk continues These matrices have the following interpretation which
Pˆ
indefinitely. As in all Markov chains, the initial distribution are further measures of distance. The matrix records
of probabilities washes out and this is something that we the probability of a walker at node i accessing another
Qˆ
are not sure is desirable for it implies that the initial struc- node k via any street j while the matrix gives the prob-
ture exerts a decreasing effect on the final state. In this ability of moving from a street j to another street ℓ via
steady state, a walker has the same chance as any other of any node k. To detail this, a walker at any node i has a
visiting a node or street regardless of where they started probability of accessing each street j and from each of
from. The key issue is what these vectors actually imply. In these streets, he/she has a probability of reaching another
fact, they are measures of the number of walkers travelling node k. The same type of fixed point vectors result from
to different places in the system; as such, these may corre- this process of continually moving from node to node or
late with any of the distance measures introduced earlier street to street as we indicated above for the processes
and we will test this correlation in another worked example based on P and Q. This washes out the initial urban
below. For the moment, let us simply note that p and q are structure and insofar as we can define the resultant prob-
accessibility vectors for intersections and streets defined abilities in the steady state as accessibilities, these are
pˆ =pˆPˆ qˆ =qˆQˆ
from the random walks associated with the different prob- defined from and .
ability processes P and Q. We can in fact define associated These primal and dual processes hold the key to the
processes based on the sliced data matrices X and Y but we integration between spatial interaction through the pri-
will not do so here as these are close to processes defined mal and space syntax through the dual. Let us write
on the raw interaction data. There is one last point before the steady state equation for intersection nodes as
pˆ =pˆPˆ =pˆGC
we move to a deeper view of these processes: clearly as . Now if we post-multiply this by G,
U AA T and V A T A, then the primal and dual processes we get pˆG =pˆGCG =pˆGQˆ . Now as the steady state
P = and Q are rela = ted. We can write these as P δ p AA T and vector qˆ associated with Qˆ is unique, it is clear that
Q δ q A T A where δ p and δ q are diagonal mat = rices defined pˆG =pˆGQˆ =qˆ =qˆQˆ . Thus it is clear that qˆ =pˆG
= pˆ =qˆC
to ensure that P and Q are row stochastic. Some manipula- and in like manner, . This is a very clear rela-
tion of these relations suggests that there are more explicit tion between the two processes and it is the simplest way
links between their steady state vectors in terms of the ini- they interlock. What they mean is as follows: writing the
tial matrices A and A T but we have not taken this further as steady state relations in full as.

Batty Urban Informatics (2022) 1:4 Page 12 of 23
∑ ∑
p̂ k = j q̂ j C jk andq̂ j = i p̂ i G ij 6. ∆ sli Y ce = d 1/ inve D rs Y e step lengths ∆X i =1/ k D i X k
j ℓ jℓ
(cid:31)
then if you are at a node k, then the probability of being 7. aggregate (cid:31) probabilities p i q j
there is equal to the probability of being on any street 8. disaggregate probabilities
pˆ
i
qˆ
j
which is connected to that node, while if you are on a
street, the probability of being there is equal to the prob- There is one last measure that we will introduce. So
ability of being at any node that is associated with that far none of our measures incorporate any measure of
street. Euclidean distance. In fact for each street segment j,
we can define a measure of distance of generalised
travel cost d. We now augment our raw data matri-
j
4.2 A comparison of distance and probability measures ces by weighting each node-street link ij by d and we
j
We are now in a position to compare all these meas- now form a new raw matrix (and its transpose follows
ures and to this end, we will introduce a second more directly from this) as
A¯
ij
=A
ij
exp −(cid:31)d
j . We use these
structured graph so that we are able to develop some matrices to construct new values fo (cid:31) r the (cid:30) matrices G and
intuition about the relatively positioning of streets and C and from this, we compute new steady states which
p¯ q¯
their intersections/nodes. This is shown in Fig. 4(a) we call and . These form our ninth measure:
where it is clear that nodes 6 and 9 and possibly 4 are
the most central and connected while streets 6 and 9, 9. weighted probabilities
p¯
i
q¯
j
then 7 and 8 seem the most accessible, although this is
harder to guess from the configuration. However this is In this formulation, we now have a parameter λ which
to be tested below using the various accessibility meas- we can use to moderate the effect of distance. Moreo-
ures. It is now worth stating the distance measures that ver for any of the limit probabilities we can take the
we will compute from all those introduced in the pre- probabilities that pertain to any power z of the matri-
vious sections. We will list these, noting that for many ces in question (for measures 7–9) and also use this as
of these measures, these are identical when defined for a parameter; that is, choose the relevant probabilities
either origin or destination nodes or streets due to the that optimise the fit of the model to data but more of
fact that the interaction matrices are symmetric. We this later when we come to empirical applications.
will define the measures for the primal and dual on We have computed all these measures for the graph in
the same line below and annotate them with respect to Fig. 4(a) and to compare them, we will correlate them. So
their meaning: for the primal problem measures, we show these correla-
tions in Table 1(a) and for the dual in Table 1(b).
1. basic in-degrees u ∑ U v ∑V In both problems, the measure which correlates most
i= k ik j= ℓ jℓ
2. sliced in-degrees x ∑ X y ∑Y with all 8 other measures is in fact the in-degree for the
3. weighted paths δ i U i = = k k δ ik i U k δ j= j V = ℓ jℓ ℓ δ j V ℓ basic matrices U and V. However, we have chosen the
4 5. . s in li v c e e r d s e w s e te ig p h l t e e n d g t p h a s t ∆ hs U i (cid:31) δ i X = = 1/ (cid:31) k k δ D i X k i U k δ (cid:31) j ∆ Y V j = = (cid:31) 1 ℓ / δ j Y ℓ ℓ D j V ℓ i a n n v d e r w se e s h t a e v p e l e p n lo g t t t h e d fr o th m e t v h a e lu s e l s ic o ed f t d h a e t s a e m in a t F r i i g c . e s 4 ( X b ) a . n O d u Y r
(cid:31) (cid:31)
Fig. 4 The Planar Graph/Street Network: a) Nodes and Arcs Labelled b) Nodes and Arcs Coloured According to Inverse Step (Accessibility) Values

B atty Urban Informatics (2022) 1:4 Page 13 of 23
Table 1 Correlations Between Selected Distance Measures for the a) Primal Spatial Interaction and b) Dual Space Syntax Problems
a) 1 2 3 4 5 6 7 8 9
1 1.00
2 0.97 1.00
3 0.86 0.72 1.00
4 0.85 0.72 0.99 1.00
5 0.71 0.76 0.52 0.58 1.00
6 0.90 0.89 0.73 0.76 0.80 1.00
7 1.00 0.97 0.86 0.85 0.71 0.90 1.00
8 0.97 1.00 0.72 0.72 0.76 0.89 0.97 1.00
9 0.74 0.63 0.81 0.80 0.54 0.70 0.74 0.63 1.00
b) 1 2 3 4 5 6 7 8 9
1 1.00
2 0.93 1.00
3 0.89 0.85 1.00
4 0.72 0.76 0.95 1.00
5 0.62 0.72 0.57 0.59 1.00
6 0.77 0.85 0.72 0.69 0.96 1.00
7 1.00 0.93 0.89 0.72 0.62 0.77 1.00
8 0.92 0.75 0.70 0.48 0.51 0.63 0.92 1.00
9 0.08 0.13 0.24 0.30 0.11 0.19 0.08 0.11 1.00
−
initial intuition on the relative importance of the nodes 4.3 An empirical demonstration of primal‑dual integration
is clearly born out with node 6 occupying a pivotal posi- As we have emphasised, space syntax and spatial inter-
tion and 7 and 8 next with 9 close behind. The less con- action represent space at different scales with space syn-
nected and more extreme nodes such as 1 and 10 are the tax dealing with the literal physical connections between
least important. Although this is not a definitive dem- places while spatial interaction deals with generic move-
onstration of the relatedness between nodes and streets, ments between origins and destinations which can then
the space syntax measures show that streets 6 and 9 are be assigned to the finer scale physical network that space
the most important with 4, 5, 7 and 8 being the next syntax takes as its starting point. Spatial interaction
important. These mirror the nodal structure also shown deals with all flows between origins and destinations of
in Fig. 4(b). It is worth noting that the last measures – magnitude N2 whereas space syntax deals with a subset
the ninth based on p¯ and q¯ – have been defined using of these flows L < < N2 where only those on the physical
random distances, that is d rand (100), and it is no links of the network are considered. However as we have
j=
surprise that the lowest correlations with the other meas- already illustrated, to compare the two approaches, we
ures occur here. In fact the steady states of the probabil- need to begin with a common network and to this end
ity measures 7 and 8 are quite highly correlated with the we have constructed a physical network of links from
other measures but note that for measure 7, this has com- the generalised travel cost and distances between some
plete correlation with the in-degree measure 1 for both 633 zones which comprise the Greater London Author-
the primal and duals while measure 8 has a complete ity (GLA) area. These zones are based on wards, the most
correlation with the sliced in-degree with the primal. In basic electoral districts which are associated with the 33
fact what is clear from this is that if we have a very sim- boroughs that make up the area, with on average each of
ple structure where the number of in-degrees is the same these zones containing 11,330 resident population and
for each node, then the probability measures are likely to 7181 employment. We show the zones and their cen-
have a very high correlation with these in-degrees (Batty, troids in Fig. 5(a) where we indicate the GLA area in its
2016). This can be very problematic where we control the wider zonal context.
nodes or where we limit the connections. It means that The level of detail of the street network is well below
the less we differentiate urban structure through connec- this scale so in this application, what we will do is con-
tivity, the less differences there are between the measures struct a synthetic network from the distance links that
of accessibility, a problem that is quite significant in the are used to form the generalised travel cost matrix [c ].
ik
empirical applications that now follow. To build this network, we first take the 5 shortest links

Batty Urban Informatics (2022) 1:4 Page 14 of 23
zones. In this sense, the network can be referred to as a
‘nearest neighbour’ network and we show its form in
Fig. 5(b).
From the previous hypothetical example, the sliced in-
degree measures 1 and 2 are the most highly correlated
with all others and we consider these to be a natural base-
line for planar graphs in terms of their direct accessibili-
ties. Moreover it is very clear that these measures pick up
local structure although all the other measures are based
on indirect as well as direct links some with an appropri-
ate weighting. We show the sliced in-degrees for nodes
x ∑ X and intersections y ∑ Y which reflect the
i= k ik j= ℓ jℓ
primal and dual problems respectively in Fig. 6(a) and
(b) and it is immediately obvious that these measures
reflect the fact that the network has been constructed
using a rule of thumb starting with 5 links per node. This
is likely to give a much more muted distribution of acces-
sibilities for nodes and well as paths and this is in fact the
case in Fig. 6. Moreover the local structure is picked up
very clearly in street accessibilities in the dual in Fig. 6(b)
while the accessibility in the nodes is dominated by a
Fig. 5 The Zoning System, Centroids, and Network Links for the
London Area. a)The zones in the GLA Area are coloured grey while
in (b) the nodes external to the area but within the network are
coloured black
for each zone i and in cases where this does not lead to
symmetric links, that is where we have a shortest link c
ik
but do not have a link c , we add this link to the network,
ki
thus giving us at least 5 links from every origin to its
nearest neighbour destinations. We also need to ensure
that on the edge of the area, we also take 5 such links
and thus we have a ring of centroids in zones outside the
GLA area which connect to the 633 zones inside the area.
This increases the number of zones to 699, with some 66
acting as edge zones outside the area. In total, we define
3944 links from these 699 zones giving an average in-
degree (and out-degree) of 5.64, a little greater than the
5 chosen initially for each zone. The total number of links
is a small percentage of the total possible links, the ratio
being less than 1% (0.008 3944/N2 3944/488,601)
= =−
which is an extremely sparse matrix. It is arguable as to
whether or not this network is sufficiently rich to pick up
Fig. 6 Nodes (a) and Street Accessibilities (b), Based on In-degree
the urban structure and connectivity of London but at
Accessibility Measures
least the links chosen do exist largely between adjacent

B atty Urban Informatics (2022) 1:4 Page 15 of 23
handful of local nodes that because of their physical jux- The most basic measure used in space syntax is the
taposition come out as being more central than the oth- step length and here we compute step lengths in their
ers. It is worth noting that the in-degree structure based inverse form for the primal and dual problems. We will
on x and y are equivalent to the steady state vectors from define these measures again as ∆X i =1/ k D i X k and
q t ˆ h = e a q g ˆQ g ˆ regate steady state probability vectors pˆ =pˆPˆ and ∆Y j =1/ ℓ D j Y ℓ and we show their form in (cid:31) Figs. 7(a)
. and (b). This is much more intuitively satisfying as a
(cid:31)
Fig. 7 Nodes (a) and Street Accessibilities (b), Based on the Inverse Step Length Accessibility Measures

Batty Urban Informatics (2022) 1:4 Page 16 of 23
representation of nearness between node centroids in the Of course when we reach the point where the cells of the
primal and streets in the dual, and a visual comparison of step length matrix are positive, then we would need to
nodes with streets seems to confirm that these patterns work with the total numbers of path lengths, weighted
of accessibility are close to one another. However what or otherwise, as in eq. (8). We show these trajectories in
these measures reveal is that first there are profound Fig. 8.
edge effects which have probably been exacerbated by To see how these make a much bigger difference, we
the way we have built the network to its edges – that is, turn to our last exploration of accessibility in the primal
the edge nodes are simply in the network so that they can and dual problems where we formulate the problem in
meet the requirement of each non-edge node having at probability terms. The steady state equations which we
pˆ =pˆPˆ qˆ =qˆQˆ
least 5 links to other nodes. Second, the fact that we deal defined earlier as and define processes
with what is essentially a circular system means that the where a walker starting from any position in the system
most accessible points are towards the centre of the sys- – in the primal from any node and in the dual from any
tem. This is a generic problem in all spatial analysis, and street, moves from node to node or from street to street
it relates to the basic issue of closing the system at some with the probabilities of moving from one to another
point to the outside world. Third there is the issue of local gradually reflecting the overall structure of nodes or
versus global connectivity in such a network and it clear streets with the initial probabilities washing out, dif-
that the more links that are taken into account, the more fusing if you like. In a system with very little structure
the structure at its most local scale is compromised. If we which to an extent is our example – and this means we
compare Figs. 6 and 7, then we can see how local struc- need a much better and fuller test of these ideas – then
ture evolves to global structure as the measure of acces- the probabilities of each node or street in the steady
sibility is based on wider and wider link effects. In fact state are likely to be fairly similar. In short these Markov
for the step lengths, the number of matrix powers that processes wash away the original probabilities and what
is needed to span the entire system is some 29 for nodal remains is the ‘true’ or ‘pure’ structure. We illustrated
connectivity and 27 for street connectivity. The computa- in earlier examples quite a high correlation between the
tion of these step lengths using the matrix power method steady states and the local structure but these were very
as implied by eqs. (4) to (7) is quite time-consuming for simple graphs with exaggerated structure. Where one has
699 699 and 1972 1972 matrices (all night on my PC large swathes of metropolitan area with similar struc-
× ×
Vaio VPCZ21M9E) and when we reach the point where it ture in terms of the street network, then it is likely that
takes at least 29 or 27 steps to reach any and every node the steady state is somewhat less distinct then the step
or street, this is still an arbitrary cut off. In fact it is worth method of accessibility just illustrated.
showing how fast this computation is noting that at any We show the node and street accessibility patterns based
pˆ qˆ
point up to n 29, we could take the step length matrix on and in Fig. 9(a) and (b). Because the nodal struc-
=
as a basis for the computation of accessibility measures. ture is quite flat, we have scaled the values and then ranked
Fig. 8 Convergence to the Step Length Limit for the Primal and Dual Problems

B atty Urban Informatics (2022) 1:4 Page 17 of 23
Fig. 9 Steady State Nodal and Street Structure a) absolute values of pˆ . b) absolute values of qˆ c) ranking of pˆ
them as we show in Fig. 9(c) but this does little to sharpen ranked the street lines. The strongest correlation is low at
the structure. In fact in Fig. 9(b), the pattern is completely 0.34 between the in-degrees and the inverse step lengths
flat for the accessibility of streets with the edge nodes soak- while that between the probabilities as inverse step lengths
ing up the probabilities in an obscure manner. It is worth and the probabilities and in-degrees are both negative but
comparing these patterns formally and in Fig. 10 we have less than 0.25. This as we have argued above is due to the
re-plotted the nodal patterns as thematic maps where each nature of the diffusion of probabilities on the particular
centroid is associated with each zone. This makes the pat- localised street graph that we have used.
terns much easier to grasp intuitively. It is quite clear that Our last issue with respect to the measures developed so
the in-degrees are identical to the probabilistic steady far is to provide a partial test of how good the accessibility
state vectors with a correlation of 1 (Fig. 10(a) compared values are where we are able to match them against activi-
to 10(c)). The correlation between the in-degrees and the ties/trips associated with nodes and streets. The easiest test
inverse step length (10(a) cf. 10(b)) is modest at 0.48 while is to see how close the nodal accessibility values are to the
that between in-degrees and the ranked probabilistic observed activity totals associated with the set of centroids.
steady state vectors is 0.86. If we examine the dual street These observed activity totals are origin employment and
patterns, we have similar correlations but we have not resident working populations which are formed from
Fig. 10 Comparisons of Nodal Accessibility Vectors. a) In-degrees b) Inverse Step Lengths c) Steady State d) Ranked Steady State

Batty Urban Informatics (2022) 1:4 Page 18 of 23
Eobs = Tobs are much lower with no significance. The probabilistic
i k ik
Pobs = Tobs (23) measure from the steady state accessibilities pˆ is equiv-
k (cid:31) i ik (cid:30)
alent to the in-degrees. In fact we consider the correla-
(cid:31)
There is an immediate issue in terms of making com- tions with the inverse step lengths to be significant and
parisons at this level for it is not clear if the various when we examine plots of these values, it is clear there
access measures are more related to explaining employ- are positive relationships with employment having a very
ment or population. In fact there is a negative correla- characteristic scatter which is almost super-exponential.
tion of 0.217 between employment and population We show these plots in Figs. 11(a) and (b). To an extent,
−
which is quite consistent with the spatial structure of it is a little surprising that our measures correlate so well
largely monocentric cities with low population densi- with densities for the underlying accessibility measures
ties and high employment densities at and around their based on crude step lengths whose basic data range from
centres. There is another issue. The zonal structure is 1 to 29 in value are relatively unsophisticated indices.
organised so that populations in each zones are as close We can now explore the question of observed move-
to one another as possible. Although this is not strictly ments on the space syntax street links. In fact, we know
enforced as in the US where redistricting of electoral dis- a priori that we do not have the actual trip movements on
tricts takes place after each election, there is momentum each link for all we have are generic interactions between
to make sure that there are no big differences between origins and destinations that in fact have to be mapped
the electoral population in each ward. This means that a or assigned to the network before we can produce actual
measure such as the inverse step length Δ X which from trips on the network. Thus it is likely that any analysis of
Fig. 7(a) which increases as one gets closer to the cen- origin-destination trip movements on specific network
tre would not explain the spatial structure of population links is likely to be flawed. For each street j in the system
which is more uneven. which is associated with a link between intersections ik,
So what we do here to normalise these spatial equali- we can compare the accessibility on that link with respect
ties is to compare the accessibility vectors to the employ- to the flow between an origin and destination from the
ment and population densities which we compute as observed matrix of flows T i o k bs , notwithstanding the
E i obs/Area i and P k obs/Area i and use these to make com- fact that these are quite different from the actual flows.
parisons with the accessibility vectors. The correlation The problem as we have pointed out earlier is that the
between these densities is still low with virtually no cor- observed values we have are not those that are actually
relation at 0.055. Nevertheless the predictions are better observed on any link ik for these values combine many
than expected. In fact we compare only the 633 zones in trips between origins and destinations which are assigned
terms of the accessibilities and activity density vectors to the link in question. The data too is only a 10% sample
leaving out the 66 external edge of area zones. The two from the 2001 Population Census. Moreover the actual
correlations between inverse step length and employ- network structure that we have developed is a nearest
ment and population are both positive with population neighbour network and it does not include long links
higher at 0.555 than employment at 0.371 and if we then such as motorways and other major roads with restricted
compare them with the in-degrees x, these correlations access. If our threshold on links were to be relaxed and
Fig. 11 Empirical Comparisons of the Inverse Step Length with a) Population Density and b) Employment Density

B atty Urban Informatics (2022) 1:4 Page 19 of 23
the notion of streets with more than two intersections know that the Pˆ matrix in the examples so far in this
with other streets to be invoked, we might improve the paper is very sparse as it is a nearest neighbour network
comparison but this requires testing and further devel- but if we assume it is sufficiently rich to detect urban
opment on a much richer and more detailed network. structure, then the spatial interaction model follows
In terms of the correlations, the in-degree and inverse directly from eqs. (24). Note that the vectors e [E]
= i
step lengths have barely any correlation with observed and ρ [ρ ] are not the steady state vectors but origin
= k
trips at − 0.073 and − 0.097 (noting that the in-degree and estimation vectors which we can interpret in spa-
and inverse step lengths correlate at 0.342). The correla- tial interaction terms as employment and population.
tion between observed trips and the probabilistic access In matrix terms we write the model in eq. (24) as
measure is actually very slightly negative at 0.064 but
essentially there is no correlation. Despite th − ese results ρ =ePˆ =eGC (25)
being somewhat disappointing, they are entirely explica-
which is the primal spatial interaction and then by apply-
ble in terms of the data used and the fact that these data
ing the matrix G to this equation, we generate the dual
does not contain anything other than nearest neighbour
space syntax model as
links to explain urban structure. In the next and last sec-
tion of the paper, we will explore a way forward. ρG =ePˆG =eGCG =eGQ
(26)
4.4 An integrated approach r =sQ=ρG =eGQ
(27)
The key to an integration of space syntax and spa-
tial interaction has already been defined through the where it is now clear that r and s are the equivalent to
two operations on the basic matrix A which give rise population and employment (counts or densities) respec-
to the primal and dual interaction matrices U AA T tively but now spread to the street network; that is, r and
=
and V A T A. The distances at different step lengths s are the population and employment equivalents that
=
although related from U n and V n by U n A T AY n, have simply relate these to the streets. What this means is that
=
to be normalised for interpretation. However if we population and employment are spread from locations to
work with the dual normalisation of the basic matrix their connected street lines. The predictions of ρ and r
as row stochastic probability matrices G [G ] and are thus entirely consistent with one another and can be
= ij
C [C ] from eqs. (19) and (20) which we restate below derived from one another as eq. (27) reveals.
= jk
as We have tested eqs. (25) to (27) on our Greater London
G ij = A j i A j ij , j G ij =1 [(19)] network and essentially what we do is take the employ-
AT ment for each location and work out the population
C jk =(cid:31) j A k T , (cid:31) k C jk =1 [(20)] using the matrix Pˆ as in eq. (25). We do this for both the
k jk
(cid:31) (cid:31) count and density employments and the data that we use
then successive powers of the probability matrices is shown in Fig. 12.
Pˆ =GC and Qˆ =CG give very clear steady state rela- The relative concentrations in Fig. 12 are consistent
tions pˆG =qˆ and pˆ =qˆC . We have, however, demon- with the fact that the population (and its density) are
strated that these steady state relations wash away the much more spread out than employment counts and
structure that we need to preserve as a key determinant densities. In essence, what the model does is translate in
of the relevant accessibilities of nodes/centroids and primal form, the employment counts and densities in the
streets, thus we begin with the matrices Pˆ and Qˆ . upper row of Fig. 12 to their population equivalents in the
Pˆ
Thus a more basic approach is to assume that the proba- lower row using the matrix . We show these predictions
bility matrix Pˆ defines the singly constrained trip equation in Fig. 13 where we plot counts and densities in the upper
which we stated earlier in eq. (13) and now elaborate as row and show their form in the lower row through rank-
ing which reduces the spread of these thematic maps.
T ik =E i p k|i =E i Pˆ ik It is very clear that the translation from employment
E i = k T ik =E i k Pˆ ik  where k Pˆ ik =1 counts and employment densities uses a probability
ρ k = � i T ik = �i E i Pˆ ik  � matrix which has so little structure within it – from the
(24) raw planar graph – that it hardly translates employment
� � 
into population, the results for both counts and densities
Without elaborating the density version of the
being very close to the original distributions of employ-
model as above, we will substitute employment den-
ment. If you compare the employment maps in Fig. 12
sity E/Area for the employment count and test both
i i
with the population in the upper row of Fig. 13, the cor-
counts and densities in the following application. We
relation between the two is very high. The correlations

Batty Urban Informatics (2022) 1:4 Page 20 of 23
Fig. 12 The Distribution of Aggregated Trips at Origins (Employment) and at Destinations (Population) as Counts and Densities
Fig. 13 Predicted Population Counts and Densities from the Primal Interaction Model

B atty Urban Informatics (2022) 1:4 Page 21 of 23
between predicted and observed population counts is centroids or nodes into activity which is spread along the
negative at 0.150 while for densities, it is positive but links of the system which are streets. This population in
−
low at 0.119. To an extent, this reflects the major con- fact is r ρG while the employment is s eG. We could,
= =
clusion of this work: that in many space syntax analy- of course, had we estimates of these activities associated
ses, because the planar graph used is one based largely with streets, start with employment spread along streets
but not exclusively on nearest neighbours, there is not using Q to predict r from s but there is no tradition of
enough structure in this matrix to ensure that we get working in this manner. It is not out of the question how-
good predictions of locational activities which in turn ever to begin to collect activity along streets and pursue
are derived from trip movements. We will come back the analysis in this direction. If our streets are longer seg-
to this point as it is perhaps the most important find- ments with more than two intersections, this makes the
ing from this analysis in that it reflects the notion that analysis more convoluted but it is still possible to imagine
we need to think about space syntax in terms of other there are insights into urban structure to be achieved in
approaches and only then can we assess how appropriate this way. To conclude, we show the street flows of popula-
the approach is. tion activity r and employment activity s for both counts
In fact all is not lost even from this application, for and densities in Fig. 15. It is very clear that employment
when we rank the predicted population counts and den- dominates these spreads and because the basic prob-
sities, we do see some structure. Compare the observed ability matrices are so sparse and simply connected, the
population density with the ranked predicted population spread to population also mirrors employment. It is pos-
density – the bottom right hand map in Fig. 12 with its sible if we rank these links rather than use absolute val-
equivalent in Fig. 13 – and we see a much stronger cor- ues, that more structure could be extracted from these
relation which shows that there is some structure in the patterns. But this is just one of many explorations that
Pˆ
matrix . We can also get at this by comparing a loga- we could continue to make. However we consider that
rithmic transformation of the predicted and observed we have now pointed the direction and that a number of
densities as in Fig. 14 which reveals a stronger significant lines for future research have been established. We turn
correlation at 0.507. Doubtless, if we were to produce a to these by way of conclusion.
Pˆ2,
more structured basic probability matrix – perhaps
Pˆ3
, 5 Conclusions: next steps
etc. – then it is possible we would get better results
even with this simple and somewhat arbitrary example. The key issue in predicting urban movements in spatial
The last thing we will do is transform the primal spa- interaction models involves the independent variables
tial interaction model into its dual space syntax equiva- which represent the trade-off between measures of the
lent. Equations (26) and (27) illustrate that it is a simple size of locations and the cost or distance from a location
matter to convert employment and population activity at where movement is generated and a location to which it
Fig. 14 Logarithmic Predicted and Observed Population Densities

Batty Urban Informatics (2022) 1:4 Page 22 of 23
Fig. 15 Observed Employment and Predicted Population Counts and Densities for the Space Syntax Dual Formulation
is attracted. All of this information is represented in the with dimensions L2, involves non-trivial matrix compu-
Pˆ
probability matrix which we have articulated in primal tations in terms of size. Were we to have as many seg-
form as the interaction between the set of centroids/loca- ments as possible origin-destination interactions, our
tions and the streets or routes to which they are linked, dual matrices would be of the order N4 N2N2 which in
=
that is using the matrix A [A ]. The primal matrix the London example would be 488,601 x 488,601 giving
= ij
is dimensioned to represent all possible movements matrices with some 23,873,093,7201 (23 billion) cells.
between the nodes which is of the order N2 and this in Such matrices, frankly, are simply beyond our capabil-
turn is based on the number of street links or segments ity to work with. However, it is most unlikely that every
L which we have suggested is very much smaller than the street segment relates to every other which is what this
total number of movements. How good this structure of would imply, and thus this number of cells is a theoretical
streets is in representing all the nuances and biases in upper limit. But what it does show is that it is absolutely
urban structure depends to a large extent on this number. essential to get the structure of the basic graph correct
In the application to Greater London including external and it is quite clear that in this application, we have far
zones, there are N 699 nodes with a possible number too sparse primal and dual matrices. This suggests that
=
of trip movements 488,601 ( N2) whereas the nearest we need to pay particular attention in space syntax to the
=
neighbour street network has some 3944 ( L) which nature of the street matrix; and it also suggests that if we
=
means that the number of possible links on which trips are to link this to spatial interaction, we need to define
might be observed is only 0.008, not quite 1%. Were we the A matrix in much richer terms, taking account of size
to increase the number of possible links to N2, then we as well as connectivity.
would need to consider links between all these possible Throughout this paper, we have been at pains to state
streets. In fact, it is most unlikely that all possible trips that the configuration of the basic planar graph from
would use all possible links for different trips are assigned which the dual and primal interaction matrices are
to the local street segments in making a shortest route defined is critical to appropriate applications of both of
between origins and destinations. these approaches and particularly their integration. What
The way we have represented the problem in terms of we now need are better examples with richer structure
a primal matrix with dimensions N2 and the dual matrix and then we will be able to assess the extent to which our

B atty Urban Informatics (2022) 1:4 Page 23 of 23
measures of accessibility and the integrated model posed Borgatti, S. P., & Everett, M. G. (1997). Network analysis of 2-mode data. Social
Networks, 19, 243–269.
in the last section can be developed further. We also
Hansen, W. G. (1959). How accessibility shapes land use. Journal of the Ameri-
need to explore the extent to which the spatial system can Institute of Planners, 25, 73–76.
which is represented at the zonal and street scales can Hillier, B. (1996). Space is the machine. Cambridge: Cambridge University Press.
Hillier, B., & Hanson, J. (1985). The social logic of space. Cambridge: Cambridge
be reconciled and this probably means that we need to
University Press.
consider how trip movements are assigned to street seg- Hillier, B., Penn, A., Hanson, J., Grajewski, T., & Xu, J. (1993). Natural movement:
ments. This might in fact be a good criterion for defin- Or configuration and attraction in urban pedestrian movement. Environ-
ment and Planning B, 20, 29–66.
ing the connectivity matrix in the first instance but it also
Jang, J.-Y. (2019). A study on improvement of gravity model decay function of
requires considerable further research to bring this kind transporting demand forecasting considering space syntax. Journal of
of analysis to fruition. Last but not least, we need to say the Korea Academia-Industrial Cooperation Society, 20(3), 617–631.
Kim, J. H., Lee, M. Y., & L. M. (2016). Integration of space syntax theory and logit
something about whether or not we have made progress
model for walkability evaluation in urban pedestrian networks. The Jour-
with our integration of space syntax and spatial interac- nal of The Korea Institute of Intelligent Transport Systems, 15(5), 62–70.
tion here. What is clear is that we have clarified consider- Law, S., Chiaradia, A., & Schwander, C. (2012). Towards a multi-modal space
syntax analysis. A case study of the London street and underground net-
ably how we might develop any such integration but our
work. In M. Greene, J. Reyes, & A. Castro (Eds.), Eighth International Space
applications have been disappointing in that our example Syntax Symposium. Santiago: PUC.
is not rich enough to show good results involving predic- Lee, M. Y., Jong Hyung Kim, J. H., & Eun Jung Kim, E. J. (2015). A pedestrian
network assignment model considering space syntax. The Journal of The
tion. This is very much reflected in the data we have used,
Korea Institute of Intelligent Transport Systems, 14(6), 37–49.
particularly the street network but it has enabled us to Marshall, S. (2015). Line structure interpretation of networks: Relationships,
say something very significant about how we define the matrices and properties. Working paper 204, CASA, University College
London WC1E 7HB, UK.
networks used in space syntax. To progress these to the
Sevtsuk, A. (2021). Estimating pedestrian flows on street networks: Revisiting
point where they are useful for spatial interaction mod- the Betweenness index. Journal of the American Planning Association,
els, we must devise much clearer rules for the defini- 87(4), 512–526.
Wilson, A. G. (1970). Entropy in urban and regional modelling. London: Pion
tion of the basic network, its topology, and its density on
Press.
which the various accessibilities we have defined are to
be measured. Only then will we be able to progress space Publisher’s Note
syntax to the point where it is consistent with the use of Springer Nature remains neutral with regard to jurisdictional claims in pub-
spatial interaction modelling in prediction. lished maps and institutional affiliations.
Acknowledgements
The author thanks the Chinese University of Hong Kong for support which led
to an early version of this paper in 2018. This research has also been supported
by the EPSRC UK Regions Digital Research Facility (UK RDRF) Grant Number
EP/M023583/1 in 2018-2019 and latterly by the Alan Turing Institute under
QUANT2–Contract–CID–3815811 from 2019 to 2022.
Author’s contributions
The author(s) read and approved the final manuscript.
Declarations
Competing interests
Prof. Michael Batty is a regional Editor of Urban Informatics. He was not
involved in the peer-review or handling of the manuscript. The author has no
other competing interests to disclose.
Received: 9 June 2022 Revised: 11 July 2022 Accepted: 19 July 2022
References
Barthélemy, M. (2011). Spatial networks. Physics Reports, 499, 1–101.
Bafna, S. (2003). Space syntax: a brief introduction to its logic and analytical
techniques. Environment and Behavior, 35(1), 17–29.
Batty, M. (2013). The new science of cities. Cambridge: The MIT Press.
Batty, M. (2016). Evolving a plan: Design and planning with complexity. In J.
Portugali, & E. Stolk (Eds.), Complexity, cognition, urban planning and
design, Springer Proceedings in Complexity, Springer International
Publishing, Zurich, Switzerland, https:// doi. org/ 10. 1007/ 978-3- 319- 32653-
5_2, 21-42
