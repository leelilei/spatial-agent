Title: Introduction

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/survey_paper/pdfs/phase1_adjacent/06_Language_Models_Represent_Space_Time_Gurnee2023.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T02:55:11+00:00
- page_count: 21
- status: ok
- text_char_count: 47419

Metadata:
- author: unknown
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Introduction (page 1)
- Empirical Overview (page 2)
  - Space and Time Raw Datasets (page 2)
  - Models and Methods (page 3)
  - Evaluation (page 3)
- Linear Models of Space and Time (page 3)
  - Existence (page 3)
  - Linear Representations (page 4)
  - Sensitivity to Prompting (page 4)
- Robustness Checks (page 6)
  - Verification via Generalization (page 6)
  - Dimensionality Reduction (page 7)
- Space and Time Neurons (page 8)
- Related Work (page 8)
- Discussion (page 9)
- Datasets (page 13)
- Neuron Ablations and Interventions (page 15)
- Additional Results (page 17)

Markdown Content:

PublishedasaconferencepaperatICLR2024
LANGUAGE MODELS REPRESENT SPACE AND TIME
WesGurnee&MaxTegmark
MassachusettsInstituteofTechnology
{wesg, tegmark}@mit.edu
ABSTRACT
The capabilities of large language models (LLMs) have sparked debate over
whether such systems just learn an enormous collection of superficial statistics
orasetofmorecoherentandgroundedrepresentationsthatreflecttherealworld.
We find evidence for the latter by analyzing the learned representations of three
spatial datasets (world, US, NYC places) and three temporal datasets (historical
figures,artworks,newsheadlines)intheLlama-2familyofmodels. Wediscover
that LLMs learn linear representations of space and time across multiple scales.
These representations are robust to prompting variations and unified across dif-
ferententitytypes(e.g. citiesandlandmarks). Inaddition,weidentifyindividual
“spaceneurons”and“timeneurons”thatreliablyencodespatialandtemporalco-
ordinates.Whilefurtherinvestigationisneeded,ourresultssuggestmodernLLMs
learn rich spatiotemporal representations of the real world and possess basic in-
gredientsofaworldmodel.
1 INTRODUCTION
Despite being trained to just predict the next token, modern large language models (LLMs) have
demonstratedanimpressivesetofcapabilities(Bubecketal.,2023;Weietal.,2022),raisingques-
tions and concerns about what such models have actually learned. One hypothesis is that LLMs
learn a massive collection of correlations but lack any coherent model or “understanding” of the
underlying data generating process given text-only training (Bender & Koller, 2020; Bisk et al.,
2020). An alternative hypothesis is that LLMs, in the course of compressing the data, learn more
compact,coherent,andinterpretablemodelsofthegenerativeprocessunderlyingthetrainingdata,
i.e., a world model. For instance, Li et al. (2022) have shown that transformers trained with next
tokenpredictiontoplaytheboardgameOthellolearnexplicitrepresentationsofthegamestate,with
Nandaetal.(2023)subsequentlyshowingtheserepresentationsarelinear. Othershaveshownthat
LLMstrackbooleanstatesofsubjectswithinthecontext(Lietal.,2021)andhaverepresentations
thatreflectperceptualandconceptualstructureinspatialandcolordomains(Patel&Pavlick,2021;
Abdouetal.,2021). BetterunderstandingofifandhowLLMsmodeltheworldiscriticalforrea-
soning about the robustness, fairness, and safety of current and future AI systems (Bender et al.,
2021;Weidingeretal.,2022;Bommasanietal.,2021;Hendrycksetal.,2023;Ngoetal.,2023).
Inthiswork,wetakethequestionofwhetherLLMsformworld(andtemporal)modelsasliterallyas
possible—weattempttoextractanactualmapoftheworld! Whilesuchspatiotemporalrepresenta-
tionsdonotconstituteadynamiccausalworldmodelintheirownright,havingcoherentmulti-scale
representationsofspaceandtimearebasicingredientsrequiredinamorecomprehensivemodel.
Specifically,weconstructsixdatasetscontainingthenamesofplacesoreventswithcorresponding
spaceortimecoordinatesthatspanmultiplespatiotemporalscales:locationswithinthewholeworld,
theUnitedStates,andNewYorkCityinadditiontothedeathyearofhistoricalfiguresfromthepast
3000years,thereleasedateofartandentertainmentfrom1950sonward,andthepublicationdateof
newsheadlinesfrom2010to2020. UsingtheLlama-2(Touvronetal.,2023)andPythiaBiderman
etal.(2023)familyofmodels,wetrainlinearregressionprobes(Alain&Bengio,2016;Belinkov,
2022)ontheinternalactivationsofthenamesoftheseplacesandeventsateachlayertopredicttheir
real-worldlocation(i.e.,latitude/longitude)ortime(numerictimestamp).
These probing experiments reveal evidence that models build spatial and temporal representations
throughouttheearlylayersbeforeplateauingataroundthemodelhalfwaypointwithlargermodels
1
4202
raM
4
]GL.sc[
3v70220.0132:viXra

PublishedasaconferencepaperatICLR2024
Figure1: SpatialandtemporalworldmodelsofLlama-2-70b. Eachpointcorrespondstothelayer
50 activations of the last token of a place (top) or event (bottom) projected on to a learned linear
probedirection. Allpointsdepictedarefromthetestset.
consistentlyoutperformingsmallerones(§3.1). Wethenshowtheserepresentationsare(1)linear,
giventhatnonlinearprobesdonotperformbetter(§3.2),(2)fairlyrobusttochangesinprompting
(§ 3.3), and (3) unified across different kinds of entities (e.g. cities and natural landmarks). We
thenconductaseriesofrobustnesscheckstounderstandhowourprobesgeneralizeacrossdifferent
datadistributions(§4.1)andhowprobestrainedonthePCAcomponentsperform(§4.2). Finally,
weuseourprobestofindindividualneuronswhichactivateasafunctionofspaceortimeanduse
basic causal interventions to verify their importance in spatiotemporal modeling, providing strong
evidencethatthemodelistrulyusingthesefeatures(§5).
2 EMPIRICAL OVERVIEW
2.1 SPACEANDTIMERAWDATASETS
To enable our investigation, we construct six datasets of names of entities (people, places, events,
etc.) withtheirrespectivelocationoroccurrenceintime,eachatadifferentorderofmagnitudeof
scale. Foreachdataset,weincludedmultipletypesofentities,e.g.,bothpopulatedplaceslikecities
and natural landmarks like lakes, to study how unified representations are across different object
types. Furthermore,wemaintainorenrichrelevantmetadatatoenableanalyzingthedatawithmore
detailedbreakdowns,identifysourcesoftrain-testleakage,andsupportfutureworkonfactualrecall
withinLLMs. Wealsoattempttodeduplicateandfilteroutobscureorotherwisenoisydata.
Space Weconstructedthreedatasetsofplacenameswithintheworld,theUnitedStates,andNew
YorkCity. OurworlddatasetisbuiltfromrawdataqueriedfromDBpediaLehmannetal.(2015).
Inparticular,wequeryforpopulatedplaces,naturalplaces,andstructures(e.g. buildingsorinfras-
tructure).WethenmatchtheseagainstWikipediaarticles,andfilteroutentitieswhichdonothaveat
least5,000pageviewsoverathreeyearperiod. OurUnitedStatesdatasetisconstructedfromDB-
Pediaandacensusdataaggregator, andincludesthenamesofcities, counties, zipcodes, colleges,
naturalplaces, andstructureswheresparselypopulatedorviewedlocationsweresimilarlyfiltered
out.Finally,ourNewYorkCitydatasetisadaptedfromtheNYCOpenDatapointsofinterestdataset
(NYCOpenData,2023)containinglocationssuchasschools,churches,transportationfacilities,and
publichousingwithinthecity.
2

PublishedasaconferencepaperatICLR2024
Time Our three temporal datasets consist of (1) the names and occupations of historical fig-
ureswhodiedbetween1000BCand2000ADadaptedfrom(Annamoradnejad&Annamoradnejad,
2022); (2)thetitlesandcreatorsofsongs,movies,andbooksfrom1950to2020constructedfrom
DBpediawiththeWikipediapageviewsfilteringtechnique;and(3)NewYorkTimesnewsheadlines
from2010-2020fromnewsdesksthatwriteaboutcurrentevents,adaptedfrom(Bandy,2021).
Table1: Entitycountandrepresentativeexamplesforeachofourdatasets.
Dataset Count Examples
World 39585 “LosAngeles”,“St. Peter’sBasilica”,“CaspianSea”,“CanaryIslands”
USA 29997 “FenwayPark”,“ColumbiaUniversity”,“RiversideCounty”
NYC 19838 “BordenAvenueBridge”,“TrumpInternationalHotel”
Figures 37539 “Cleopatra”,“DanteAlighieri”,“CarlSagan”,“BlancheofCastile”
Art 31321 “StephenKing’sIt”,“Queen’sBohemianRhapsody”
Headlines 28389 “Pilgrims,FewerandSociallyDistanced,ArriveinMeccaforAnnualHajj”
2.2 MODELSANDMETHODS
Data Preparation All of our experiments are run with the base Llama-2 (Touvron et al., 2023)
seriesofauto-regressivetransformerlanguagemodels,spanning7billionto70billionparameters.
For each dataset, we run every entity name through the model, potentially prepended with a short
prompt,andsavetheactivationsofthehiddenstate(residualstream)onthelastentitytokenforeach
layer. Forasetofnentities,thisyieldsann×d activationdatasetforeachlayer.
model
Probing To find evidence of spatial and temporal representations in LLMs, we use the standard
technique of probing Alain & Bengio (2016); Belinkov (2022), which fits a simple model on the
network activations to predict some target label associated with labeled input data. In particular,
given an activation dataset A ∈ Rn×dmodel, and a target Y containing either the time or two-
dimensionallatitudeandlongitudecoordinates,wefitlinearridgeregressionprobes
Wˆ =argmin∥Y −AW∥2+λ∥W∥2 =(ATA+λI)−1ATY
2 2
W
yieldingalinearpredictorYˆ =AWˆ . Highpredictiveperformanceonout-of-sampledataindicates
that the base model has temporal and spatial information linearly decodable in its representations,
althoughthisdoesnotimplythatthemodelactuallyusestheserepresentations(Ravichanderetal.,
2020). In all experiments, we tune λ using efficient leave-out-out cross validation (Hastie et al.,
2009)ontheprobetrainingset.
2.3 EVALUATION
To evaluate the performance of our probes we report standard regression metrics such as R2 and
Spearman rank correlation on our test data (correlations averaged over latitude and longitude for
spatialfeatures).Anadditionalmetricwecomputeistheproximityerrorforeachprediction,defined
asthefractionofentitiespredictedtobeclosertothetargetpointthanthepredictionofthetarget
entity. The intuition is that for spatial data, absolute error metrics can be misleading (a 500km
errorforacityontheEastCoastoftheUnitedStatesisfarmoresignificantthana500kmerrorin
Siberia),sowhenanalyzingerrorsperprediction,weoftenreportthismetrictoaccountforthelocal
differencesindesiredprecision.
3 LINEAR MODELS OF SPACE AND TIME
3.1 EXISTENCE
Wefirstinvestigatethefollowingempiricalquestions: domodelsrepresenttimeandspaceatall? If
so,whereinternallyinthemodel? Doestherepresentationqualitychangesubstantiallywithmodel
scale? In our first experiment, we train probes for every layer of Llama-2-{7B, 13B, 70B} and
3

PublishedasaconferencepaperatICLR2024
Figure2: Out-of-sampleR2forlinearprobestrainedoneverymodel,dataset,andlayer.
Pythia-{160M, 410M, 1B, 1.4B, 2.8B, 6.9B} for each of our space and time datasets. Our main
results, depicted in Figure 2, show fairly consistent patterns across datasets. In particular, both
spatialandtemporalfeaturescanberecoveredwithalinearprobe, theserepresentationssmoothly
increaseinqualitythroughoutthefirsthalfofthelayersofthemodelbeforereachingaplateau,and
therepresentationsaremoreaccuratewithincreasingmodelscale. ThegapbetweentheLlamaand
Pythia models is especially striking, and we suspect is due to the large difference in pre-training
corpussize(2Tand300Btokensrespectively). Forthisreason,wereporttherestofourresultson
justtheLlamamodels.
ThedatasetwiththeworstperformanceistheNewYorkCitydataset. Thiswasexpectedgiventhe
relative obscurity of most of the entities compared with other datasets. However, this is also the
datasetwherethelargestmodelhasthebestrelativeperformance,suggestingthatsufficientlylarge
LLMscouldeventuallyformdetailedspatialmodelsofindividualcities.
3.2 LINEARREPRESENTATIONS
Withintheinterpretabilityliterature,thereisagrowingbodyofevidencesupportingthelinearrep-
resentationhypothesisthatfeatureswithinneuralnetworksarerepresentedlinearly,thatis,thepres-
enceorstrengthofafeaturecanbereadoutbyprojectingtherelevantactivationontosomefeature
vector (Mikolov et al., 2013b; Olah et al., 2020; Elhage et al., 2022b). However, these results are
almostalwaysforbinaryorcategoricalfeatures,unlikethecontinuousfeaturesofspaceortime.
Totestwhetherspatialandtemporalfeaturesarerepresentedlinearly,wecomparetheperformance
of our linear ridge regression probes with that of substantially more expressive nonlinear MLP
probesoftheformW ReLU(W x+b )+b with256neurons. Table2reportsourresultsand
2 1 1 2
showsthatusingnonlinearprobesresultsinminimalimprovementtoR2 foranydatasetormodel.
Wetakethisasstrongevidencethatspaceandtimearealsorepresentedlinearly(orattheveryleast
arelinearlydecodable),despitebeingcontinuous.
3.3 SENSITIVITYTOPROMPTING
Anothernaturalquestionisifthesespatialortemporalfeaturesaresensitivetoprompting, thatis,
can the context induce or suppress the recall of these facts? Intuitively, for any entity token, an
autoregressivemodelisincentivizedtoproducearepresentationsuitableforaddressinganyfuture
possiblecontextorquestion.
4

PublishedasaconferencepaperatICLR2024
Figure3: Out-of-sampleR2whenentitynamesareincludedindifferentpromptsforLlama-2-70b.
Tostudythis,wecreatenewactivationdatasetswhereweprependdifferentpromptstoeachofthe
entity tokens, following a few basic themes. In all cases, we include an “empty” prompt contain-
ing nothing other than the entity tokens (and a beginning of sequence token). We then include a
promptwhichasksthemodeltorecalltherelevantfact,e.g.,“Whatisthelatitudeandlongitudeof
<place>” or “What was the release date of <author>’s <book>.” For the United States and
NYCdatasetswealsoincludeversionsofthesepromptsaskingwhereintheUSorNYCthisloca-
tionis,inanattempttodisambiguatecommonnamesofplaces(e.g. CityHall). Asabaselinewe
includeapromptof10randomtokens(sampledforeachentity). Todetermineifwecanobfuscate
thesubject,forsomedatasetswefullycapitalizethenamesofallentities. Lastly,fortheheadlines
dataset,wetryprobingonboththelasttokenandonaperiodtokenappendedtotheheadline.
Wereportresultsforthe70BmodelinFigure3andallmodelsinFigure8. Wefindthatexplicitly
promptingthemodelfortheinformation, orgivingdisambiguationhintslikethataplaceisinthe
USorNYC,makeslittletonodifferenceinperformance.However,weweresurprisedbythedegree
to which random distracting tokens degrades performance. Capitalizing the entities also degrades
performance,thoughlessseverelyandlesssurprisingly,asthislikelyinterfereswith“detokenizing”
theentity(Elhageetal.,2022a;Gurneeetal.,2023;Gevaetal.,2023). Theonemodificationthat
did notably improve performance is probing on the period token following a headline, suggesting
thatperiodsareusedtocontainsomesummaryinformationofthesentencestheyend.
Table 2: Out-of-sample R2 of linear and nonlinear (one layer MLP) probes for all models and
featuresat60%layerdepth.
Dataset
Model Probe World USA NYC Historical Entertainment Headlines
Llama-2-7b Linear 0.881 0.799 0.219 0.785 0.788 0.564
MLP 0.897 0.819 0.204 0.775 0.746 0.467
Llama-2-13b Linear 0.896 0.825 0.237 0.804 0.806 0.645
MLP 0.916 0.824 0.230 0.818 0.808 0.656
Llama-2-70b Linear 0.911 0.864 0.359 0.835 0.885 0.746
MLP 0.926 0.869 0.312 0.839 0.884 0.739
5

PublishedasaconferencepaperatICLR2024
4 ROBUSTNESS CHECKS
The previous section has shown that the true point in time or space of diverse types of events or
locationscanbelinearlyrecoveredfromtheinternalactivationsofthemid-to-latelayersofLLMs.
However,thisdoesnotimplyif(orhow)amodelactuallyusesthefeaturedirectionlearnedbythe
probe, astheprobeitselfcouldbelearningsomelinearcombinationofsimplerfeatureswhichare
actuallyusedbythemodel.
4.1 VERIFICATIONVIAGENERALIZATION
Block holdout generalization To illustrate a potential issue with our results, consider the task
of representing the full world map. If the model has, as we expect it does, an almost orthogonal
binaryfeatureforis in country X,thenonecouldconstructahighqualitylatitude(longitude)
probe by summing these orthogonal feature vectors for each country with coefficient equal to the
latitude (longitude) of that country. Assuming a place is in only one country, such a probe would
placeeachentityatitscountrycentroid.However,inthiscase,themodeldoesnotactuallyrepresent
space,onlycountrymembership,anditisonlytheprobewhichlearnsthegeometryofthedifferent
countriesfromtheexplicitsupervision.
Tobetterdistinguishthesecases, weanalyzehowtheprobesgeneralizewhenholdingoutspecific
blocksofdata.Inparticular,wetrainaseriesofprobes,whereforeachone,weholdoutonecountry,
state,borough,century,decade,oryearfortheworld,USA,NYC,historicalfigure,entertainment,
and headlines dataset respectively. We then evaluate the probes on the held out block of data. In
Table 3, we report the average proximity error for the block of data when completely held out,
comparedtotheerrorofthetestpointsfromthatblockinthedefaulttrain-testsplit,averagedover
allheldoutblocks.
Wefindthatwhilegeneralizationperformancesuffers,especiallyforthespatialdatasets,itisclearly
better than random. By plotting the predictions of the held out states or countries in Figures 11
and12, aqualitativelyclearerpictureemerges. Thatis, theprobecorrectlygeneralizesbyplacing
thepointsinthecorrectrelativeposition(asmeasuredbytheanglebetweenthetrueandpredicted
centroid) but not in their absolute position. We take this as weak evidence that the probes are
extracting explicitly learned features by the model, but are memorizing the transformation from
modelcoordinatestohumancoordinates.However,thisdoesnotfullyruleouttheunderlyingbinary
features hypothesis, as there could be a hierarchy of such features that do not follow country or
decadeboundaries.
Table 3: Average proximity error across blocks of data (e.g., countries, states, decades) when in-
cludedinthetrainingdatacomparedtocompletelyheldout. Randomperformanceis0.5.
Dataset
Model Block World USA NYC Historical Entertainment Headlines
Llama-2-7b nominal 0.071 0.144 0.331 0.129 0.147 0.258
heldout 0.170 0.192 0.473 0.133 0.158 0.264
Llama-2-13b nominal 0.068 0.144 0.319 0.121 0.141 0.223
heldout 0.156 0.189 0.470 0.126 0.152 0.235
Llama-2-70b nominal 0.071 0.121 0.262 0.115 0.105 0.182
heldout 0.164 0.188 0.433 0.119 0.122 0.200
Crossentitygeneralization Implicitinourdiscussionsofaristheclaimthatthemodelrepresents
the space or time coordinates of different types of entities (like cities or natural landmarks) in a
unified manner. However, similar to the concern that a latitude probe could be a weighted sum of
membershipfeatures,alatitudeprobecouldalsobethesumofdifferent(orthogonal)directionsfor
thelatitudesofcitiesandforthelatitudesofnaturallandmarks.
6

PublishedasaconferencepaperatICLR2024
Similartotheabove,wedistinguishthesehypothesesbytrainingaseriesofprobeswherethetrain-
testsplitisperformedtoholdoutallpointsofaparticularentityclass.1 Table4reportstheproximity
errorfortheentitiesinthedefaulttestsplitcomparedtowhenheldout,averagedoverallsuchsplits
asbefore. Theresultssuggestthattheprobeslargelygeneralizeacrossentitytypes, withthemain
exceptionoftheentertainmentdataset.2
Table4: Averageproximityerroracrossentitysubtypes(e.g. booksandmovies)whenincludedin
thetrainingdatacomparedtobeingfullyheldout. Randomperformanceis0.5.
Dataset
Model Entity World USA NYC Historical Entertainment Headlines
Llama-2-7b nominal 0.120 0.206 0.313 0.164 0.224 0.199
heldout 0.151 0.262 0.367 0.168 0.305 0.289
Llama-2-13b nominal 0.117 0.197 0.310 0.153 0.207 0.171
heldout 0.147 0.259 0.377 0.159 0.283 0.266
Llama-2-70b nominal 0.113 0.173 0.266 0.149 0.159 0.144
heldout 0.147 0.203 0.322 0.149 0.271 0.219
4.2 DIMENSIONALITYREDUCTION
Despitebeinglinear,ourprobesstillhaved learnableparameters(rangingfrom4096to8192
model
forthe7Bto70Bmodels),enablingittoengageinsubstantialmemorization. Asacomplementary
formofevidencetothegeneralizationexperiments,wetrainprobeswith2to3ordersofmagnitude
fewerparametersbyprojectingtheactivationdatasetsontotheirklargestprincipalcomponents.
Figure 4 illustrates the test R2 for probes trained on each model and dataset over a range of k
values, as compared to the performance of the full d -dimensional probe. We also report the
model
test Spearman correlation in Figure 13 which increases much more rapidly with increasing k than
theR2. Notably,theSpearmancorrelationonlydependsontherankorderofthepredictionswhile
R2alsodependsontheiractualvalue.Weviewthisgapasfurtherevidencethatthemodelexplicitly
representsspaceandtimeasthesefeaturesmustaccountforenoughvariancetobeinthetopdozen
principal components, but that the probe requires more parameters to convert from the model’s
coordinatesystemtoliteralspatialcoordinatesortimestamps.Wealsoobservedthatthefirstseveral
principal components clustered the different entity types within the dataset, explaining why more
thanafewareneeded.
Figure 4: Test R2 for probes trained on activations projected onto k largest principal components
foreachdatasetandmodelcomparedtotrainingonthefullactivations.
1Weonlydothisentitieswhichdonotmakeupthemajorityofthetrainingdata(e.g.,asisthecasewith
populatedplacesfortheworlddatasetandsongsfortheentertainmentdataset)whichispartiallyresponsible
forthediscrepanciesinthenominalcasesforTables3and4.
2WenoteinthiscasetheSpearmancorrelationisstillhigh,suggestingthisisanissuewithbiasgeneraliza-
tion,asthedifferententitytypesarenotuniformlydistributedintime.
7

PublishedasaconferencepaperatICLR2024
Figure 5: Space and time neurons in Llama-2 models. Depicts the result of projecting activation
datasetsontoneuronweightscomparedtotruespaceortimecoordinateswithSpearmancorrelation
byentitytype.
5 SPACE AND TIME NEURONS
Whilethepreviousresultsaresuggestive,noneofourevidencedirectlyshowsthatthemodeluses
the features learned by the probe. To address this, we search for individual neurons with input or
outputweightsthathavehighcosinesimilaritywiththelearnedprobedirection. Thatis,wesearch
forneuronswhichreadfromorwritetoadirectionsimilartotheonelearnedbytheprobe.
Wefindthatwhenweprojecttheactivationdatasetsontotheweightsofthemostsimilarneurons,
these neurons are indeed highly sensitive to the true location of entities in space or time (see Fig-
ure 5). In other words, there exist individual neurons within the model that are themselves fairly
predictivefeatureprobes. Moreover,theseneuronsaresensitivetoalloftheentitytypeswithinour
datasets,providingstrongerevidencefortheclaimtheserepresentationsareunified.
Ifprobestrainedwithexplicitsupervisionareanapproximateupperboundontheextenttowhicha
modelrepresentsthesespatialandtemporalfeatures,thentheperformanceofindividualneuronsis
alowerbound. Inparticular,wegenerallyexpectfeaturestobedistributedinsuperposition(Elhage
et al., 2022b), making individual neurons the wrong level of analysis. Nevertheless, the existence
oftheseindividualneurons,whichreceivednosupervisionotherthanfromnext-tokenprediction,is
verystrongevidencethatthemodelhaslearnedandmakesuseofspatialandtemporalfeatures.
WealsoperformaseriesofneuronablationandinterventionexperimentsinAppendixBtoverify
theimportanceoftheseneuronsinspatialandtemporalmodeling.
6 RELATED WORK
Linguistic Spatial Models Prior work has shown that natural language encodes geographic in-
formation(Louwerse&Zwaan,2009;Louwerse&Benesh,2012)andthatrelativecoordinatescan
be approximately recovered with simple techniques like multidimensional scaling, co-occurrence
statistics, or probing word embeddings (Louwerse & Zwaan, 2009; Mikolov et al., 2013a; Gupta
etal.,2015;Konkoletal.,2017). However,thesestudiesonlyconsiderafewhundredwellknown
cities and obtain fairly weak correlations. Most similar to our work is (Lie´tard et al., 2021) who
probewordembeddingsandsmalllanguagemodelsforthecoordinatesofglobalcitiesandwhether
8

PublishedasaconferencepaperatICLR2024
countries share a border, but conclude the amount of geographic information learned is “limited,”
likelybecausethelargestmodeltheystudywas345Mparameters(500xsmallerthanLlama70B).
NeuralWorldModels Weconsideraspatiotemporalmodeltobeanecessaryingredientwithina
largerworldmodel.Theclearestevidencethatsuchmodelsarelearnablefromnext-tokenprediction
comesfromGPT-stylemodelstrainedonchess(Toshniwaletal.,2022)andOthellogames(Lietal.,
2022)whichwereshowntohaveexplicitrepresentationsoftheboardandgamestate,withfurther
workshowingtheserepresentationsarelinear(Nandaetal.,2023). IntrueLLMs, Lietal.(2021)
showthatanentity’sdynamicpropertiesorrelationscanbelinearlyreadoutfromrepresentations
atdifferentpointsinthecontext. Abdouetal.(2021)andPatel&Pavlick(2021)showLLMshave
representationsthatreflectperceptualandconceptualstructureincolorandspatialdomains.
Factual Recall The point in time or space of an event or place is a particular kind of fact. Our
investigationisinformedbypriorworkonthemechanismsoffactualrecallinLLMs(Mengetal.,
2022a;b;Gevaetal., 2023)indicatingthatearly-to-midMLPlayersareresponsible foroutputting
informationaboutfactualsubjects,typicallyonthelasttokenofthesubject. Manyoftheseworks
alsoshowlinearstructure,forexampleinthefactualityofastatement(Burnsetal.,2022)orinthe
structureofsubject-objectrelations(Hernandezetal.,2023). Toourknowledge,ourworkisunique
inconsideringcontinuousfacts.
Interpretability More broadly, our work draws upon many results and ideas from the inter-
pretabilityliterature(Ra¨ukeretal.,2023),especiallyintopicsrelatedtoprobing(Belinkov,2022),
BERTology(Rogersetal.,2021),thelinearityhypothesisandsuperposition(Elhageetal.,2022b),
andmechanisticinterpretability(Olahetal.,2020).Morespecificresultsrelatedtoourworkinclude
Hanna et al. (2023) who find a circuit implementing greater-than in the context of years, and Goh
etal.(2021)whofind“region”neuronsinmultimodalmodelsthatresembleourspaceneurons.
7 DISCUSSION
We have demonstrated that LLMs learn linear representations of space and time that are unified
acrossentitytypesandfairlyrobusttoprompting, andthatthereexistsindividualneuronsthatare
highlysensitivetothesefeatures. Weconjecture,butdonotshow,thesebasicprimitivesunderliea
morecomprehensivecausalworldmodelusedforinferenceandprediction.
Ouranalysisraisesmanyinterestingquestionsforfuturework. Whileweshowedthatitispossible
to linearly reconstruct a sample’s absolute position in space or time, and that some neurons use
theseprobedirections, thetrueextentandstructureofspatialandtemporalrepresentationsremain
unclear. We conjecture that the most canonical form of this structure is a discretized hierarchical
mesh, where any sample is represented as a linear combination of its nearest basis points at each
level of granularity. Moreover, the model can and does use this coordinate system to represent
absolute position using the correct linear combination of basis directions in the same way a linear
probewould. Weexpectthatasmodelsscale,thismeshisenhancedwithmorebasispoints,more
scalesofgranularity(e.g. neighborhoodsincities),andmoreaccuratemappingofentitiestomodel
coordinates (Michaudet al., 2023). This suggestsfuture work on extractingrepresentations in the
model’scoordinatesystemratherthantryingtoreconstructhumaninterpretablecoordinates,perhaps
withsparseautoencoders(Cunninghametal.,2023).
We also barely scratched the surface of understanding how these spatial and temporal models are
learned, recalled, and used internally, or to what extent these representations exist within a more
comprehensiveworldmodel. Bylookingacrosstrainingcheckpoints,itmaybepossibletolocalize
a point in training when a model organizes constituent is in place X features into a coherent
geometry or else conclude this process is gradual (Liu et al., 2021). We expect that the model
componentswhichconstructtheserepresentationsaresimilaroridenticaltothoseforfactualrecall
(Mengetal.,2022a;Gevaetal.,2023).
Finally, we note that the representation of space and time has received much more attention in
biological neural networks than artificial ones (Buzsa´ki & Llina´s, 2017; Schonhaut et al., 2023).
Placeandgridcells(O’Keefe&Dostrovsky,1971;Haftingetal.,2005)inparticularareamongthe
mostwell-studiedinthebrainandmaybeafruitfulsourceofinspirationforfutureworkonLLMs.
9

PublishedasaconferencepaperatICLR2024
ACKNOWLEDGEMENTS
TheauthorswouldliketothankSamMarks,EricMichaud,ZimingLiu,JaniceYang,andespecially
NeelNandafortheirhelpfuldiscussionsandfeedback. W.G.wassupportedbyDimitrisBertsimas
andanOpenPhilanthropyearlycareergrantthroughthecourseofthiswork.
REFERENCES
Mostafa Abdou, Artur Kulmizev, Daniel Hershcovich, Stella Frank, Ellie Pavlick, and Anders
Søgaard. Can language models encode perceptual structure without grounding? a case study
incolor. arXivpreprintarXiv:2109.06129,2021.
Guillaume Alain and Yoshua Bengio. Understanding intermediate layers using linear classifier
probes. arXivpreprintarXiv:1610.01644,2016.
IssaAnnamoradnejadandRahimberdiAnnamoradnejad.Agedataset:Astructuredgeneral-purpose
datasetonlife,work,anddeathof1.22milliondistinguishedpeople. InternationalAAAIConfer-
enceonWebandSocialMedia(ICWSM),16,2022.
JackBandy. Threedecadesofnewyorktimesheadlines,2021. URLhttps://www.kaggle.
com/datasets/johnbandy/new-york-times-headlines. Kaggledataset.
Yonatan Belinkov. Probing classifiers: Promises, shortcomings, and advances. Computational
Linguistics,48(1):207–219,2022.
Emily M Bender and Alexander Koller. Climbing towards nlu: On meaning, form, and under-
standing in the age of data. In Proceedings of the 58th annual meeting of the association for
computationallinguistics,pp.5185–5198,2020.
Emily M Bender, Timnit Gebru, Angelina McMillan-Major, and Shmargaret Shmitchell. On the
dangersofstochasticparrots: Canlanguagemodelsbetoobig? InProceedingsofthe2021ACM
conferenceonfairness,accountability,andtransparency,pp.610–623,2021.
StellaBiderman,HaileySchoelkopf,QuentinGregoryAnthony,HerbieBradley,KyleO’Brien,Eric
Hallahan,MohammadAflahKhan,ShivanshuPurohit,USVSNSaiPrashanth,EdwardRaff,etal.
Pythia: Asuiteforanalyzinglargelanguagemodelsacrosstrainingandscaling. InInternational
ConferenceonMachineLearning,pp.2397–2430.PMLR,2023.
YonatanBisk,AriHoltzman,JesseThomason,JacobAndreas,YoshuaBengio,JoyceChai,Mirella
Lapata,AngelikiLazaridou,JonathanMay,AleksandrNisnevich,etal. Experiencegroundslan-
guage. arXivpreprintarXiv:2004.10151,2020.
Rishi Bommasani, Drew A Hudson, Ehsan Adeli, Russ Altman, Simran Arora, Sydney von Arx,
MichaelSBernstein,JeannetteBohg,AntoineBosselut,EmmaBrunskill,etal. Ontheopportu-
nitiesandrisksoffoundationmodels. arXivpreprintarXiv:2108.07258,2021.
Se´bastien Bubeck, Varun Chandrasekaran, Ronen Eldan, Johannes Gehrke, Eric Horvitz, Ece Ka-
mar, Peter Lee, Yin Tat Lee, Yuanzhi Li, Scott Lundberg, et al. Sparks of artificial general
intelligence: Earlyexperimentswithgpt-4. arXivpreprintarXiv:2303.12712,2023.
CollinBurns, HaotianYe, DanKlein, andJacobSteinhardt. Discoveringlatentknowledgeinlan-
guagemodelswithoutsupervision. arXivpreprintarXiv:2212.03827,2022.
Gyo¨rgy Buzsa´ki and Rodolfo Llina´s. Space and time in the brain. Science, 358(6362):482–485,
2017.
HoagyCunningham, AidanEwart, LoganRiggs, RobertHuben, andLeeSharkey. Sparseautoen-
coders find highly interpretable features in language models. arXiv preprint arXiv:2309.08600,
2023.
10

PublishedasaconferencepaperatICLR2024
NelsonElhage,TristanHume,CatherineOlsson,NeelNanda,TomHenighan,ScottJohnston,Sheer
ElShowk,NicholasJoseph,NovaDasSarma,BenMann,DannyHernandez,AmandaAskell,Ka-
mal Ndousse, Andy Jones, Dawn Drain, Anna Chen, Yuntao Bai, Deep Ganguli, Liane Lovitt,
ZacHatfield-Dodds,JacksonKernion,TomConerly,ShaunaKravec,StanislavFort,SauravKa-
davath, Josh Jacobson, Eli Tran-Johnson, Jared Kaplan, Jack Clark, Tom Brown, Sam McCan-
dlish,DarioAmodei,andChristopherOlah. Softmaxlinearunits. TransformerCircuitsThread,
2022a. https://transformer-circuits.pub/2022/solu/index.html.
NelsonElhage,TristanHume,CatherineOlsson,NicholasSchiefer,TomHenighan,ShaunaKravec,
ZacHatfield-Dodds,RobertLasenby,DawnDrain,CarolChen,etal. Toymodelsofsuperposi-
tion. arXivpreprintarXiv:2209.10652,2022b.
Mor Geva, Jasmijn Bastings, Katja Filippova, and Amir Globerson. Dissecting recall of factual
associationsinauto-regressivelanguagemodels. arXivpreprintarXiv:2304.14767,2023.
GabrielGoh,NickCammarata,ChelseaVoss,ShanCarter,MichaelPetrov,LudwigSchubert,Alec
Radford, and Chris Olah. Multimodal neurons in artificial neural networks. Distill, 6(3):e30,
2021.
AbhijeetGupta,GemmaBoleda,MarcoBaroni,andSebastianPado´. Distributionalvectorsencode
referential attributes. In Proceedings of the 2015 Conference on Empirical Methods in Natural
LanguageProcessing,pp.12–21,2015.
WesGurnee, NeelNanda, MatthewPauly, KatherineHarvey, DmitriiTroitskii, andDimitrisBert-
simas. Finding neurons in a haystack: Case studies with sparse probing. arXiv preprint
arXiv:2305.01610,2023.
TorkelHafting,MarianneFyhn,SturlaMolden,May-BrittMoser,andEdvardIMoser. Microstruc-
tureofaspatialmapintheentorhinalcortex. Nature,436(7052):801–806,2005.
MichaelHanna,OllieLiu,andAlexandreVariengien.Howdoesgpt-2computegreater-than?:Inter-
pretingmathematicalabilitiesinapre-trainedlanguagemodel. arXivpreprintarXiv:2305.00586,
2023.
Trevor Hastie, Robert Tibshirani, Jerome H Friedman, and Jerome H Friedman. The elements of
statisticallearning: datamining,inference,andprediction,volume2. Springer,2009.
Dan Hendrycks, Mantas Mazeika, and Thomas Woodside. An overview of catastrophic ai risks.
arXivpreprintarXiv:2306.12001,2023.
EvanHernandez,ArnabSenSharma,TalHaklay,KevinMeng,MartinWattenberg,JacobAndreas,
YonatanBelinkov,andDavidBau.Linearityofrelationdecodingintransformerlanguagemodels.
arXivpreprintarXiv:2308.09124,2023.
MichalKonkol,Toma´sˇBrychc´ın,MichalNykl,andToma´sˇHercig.Geographicalevaluationofword
embeddings. InProceedingsoftheEighthInternationalJointConferenceonNaturalLanguage
Processing(Volume1: LongPapers),pp.224–232,2017.
Jens Lehmann, Robert Isele, Max Jakob, Anja Jentzsch, Dimitris Kontokostas, Pablo N. Mendes,
Sebastian Hellmann, Mohamed Morsey, Patrick van Kleef, So¨ren Auer, and Christian Bizer.
Dbpedia - a large-scale, multilingual knowledge base extracted from wikipedia, 2015. URL
http://dbpedia.org. Version2023.
Belinda Z Li, Maxwell Nye, and Jacob Andreas. Implicit representations of meaning in neural
languagemodels. arXivpreprintarXiv:2106.00737,2021.
KennethLi,AspenKHopkins,DavidBau,FernandaVie´gas,HanspeterPfister,andMartinWatten-
berg. Emergentworldrepresentations: Exploringasequencemodeltrainedonasynthetictask.
arXivpreprintarXiv:2210.13382,2022.
BastienLie´tard,MostafaAbdou,andAndersSøgaard. Dolanguagemodelsknowthewaytorome?
arXivpreprintarXiv:2109.07971,2021.
11

PublishedasaconferencepaperatICLR2024
LeoZLiu,YizhongWang,JungoKasai,HannanehHajishirzi,andNoahASmith. Probingacross
time: Whatdoesrobertaknowandwhen? arXivpreprintarXiv:2104.07885,2021.
Max M Louwerse and Nick Benesh. Representing spatial structure through maps and language:
Lord of the rings encodes the spatial structure of middle earth. Cognitive science, 36(8):1556–
1569,2012.
Max M Louwerse and Rolf A Zwaan. Language encodes geographical information. Cognitive
Science,33(1):51–73,2009.
KevinMeng,DavidBau,AlexAndonian,andYonatanBelinkov. Locatingandeditingfactualasso-
ciationsingpt. AdvancesinNeuralInformationProcessingSystems,35:17359–17372,2022a.
KevinMeng,ArnabSenSharma,AlexAndonian,YonatanBelinkov,andDavidBau. Mass-editing
memoryinatransformer. arXivpreprintarXiv:2210.07229,2022b.
Eric J Michaud, Ziming Liu, Uzay Girit, and Max Tegmark. The quantization model of neural
scaling. arXivpreprintarXiv:2303.13506,2023.
TomasMikolov,IlyaSutskever,KaiChen,GregSCorrado,andJeffDean. Distributedrepresenta-
tionsofwordsandphrasesandtheircompositionality.Advancesinneuralinformationprocessing
systems,26,2013a.
Toma´sˇ Mikolov, Wen-tau Yih, and Geoffrey Zweig. Linguistic regularities in continuous space
wordrepresentations. InProceedingsofthe2013conferenceofthenorthamericanchapterofthe
associationforcomputationallinguistics: Humanlanguagetechnologies,pp.746–751,2013b.
NeelNanda,AndrewLee,andMartinWattenberg. Emergentlinearrepresentationsinworldmodels
ofself-supervisedsequencemodels. arXivpreprintarXiv:2309.00941,2023.
RichardNgo,LawrenceChan,andSo¨renMindermann.Thealignmentproblemfromadeeplearning
perspective,2023.
NYC OpenData. Points of interest, 2023. URL https://data.cityofnewyork.us/
City-Government/Points-Of-Interest/rxuy-2muj. Accessed: 2023-07-01.
JohnO’KeefeandJonathanDostrovsky. Thehippocampusasaspatialmap: preliminaryevidence
fromunitactivityinthefreely-movingrat. Brainresearch,1971.
Chris Olah, Nick Cammarata, Ludwig Schubert, Gabriel Goh, Michael Petrov, and Shan Carter.
Zoomin: Anintroductiontocircuits. Distill,5(3):e00024–001,2020.
RomaPatelandElliePavlick. Mappinglanguagemodelstogroundedconceptualspaces. InInter-
nationalConferenceonLearningRepresentations,2021.
TilmanRa¨uker,AnsonHo,StephenCasper,andDylanHadfield-Menell. Towardtransparentai: A
surveyoninterpretingtheinnerstructuresofdeepneuralnetworks. In2023IEEEConferenceon
SecureandTrustworthyMachineLearning(SaTML),pp.464–483.IEEE,2023.
AbhilashaRavichander,YonatanBelinkov,andEduardHovy. Probingtheprobingparadigm: Does
probingaccuracyentailtaskrelevance? arXivpreprintarXiv:2005.00719,2020.
AnnaRogers,OlgaKovaleva,andAnnaRumshisky. Aprimerinbertology: Whatweknowabout
howbertworks.TransactionsoftheAssociationforComputationalLinguistics,8:842–866,2021.
DanielRSchonhaut,ZahraMAghajan,MichaelJKahana,andItzhakFried. Aneuralcodefortime
andspaceinthehumanbrain. CellReports,42(11),2023.
Shubham Toshniwal, Sam Wiseman, Karen Livescu, and Kevin Gimpel. Chess as a testbed for
languagemodelstatetracking. InProceedingsoftheAAAIConferenceonArtificialIntelligence,
volume36,pp.11385–11393,2022.
HugoTouvron,LouisMartin,KevinStone,PeterAlbert,AmjadAlmahairi,YasmineBabaei,Niko-
layBashlykov,SoumyaBatra,PrajjwalBhargava,ShrutiBhosale,etal. Llama2: Openfounda-
tionandfine-tunedchatmodels. arXivpreprintarXiv:2307.09288,2023.
12

PublishedasaconferencepaperatICLR2024
Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yo-
gatama,MaartenBosma,DennyZhou,DonaldMetzler,etal.Emergentabilitiesoflargelanguage
models. arXivpreprintarXiv:2206.07682,2022.
Laura Weidinger, Jonathan Uesato, Maribeth Rauh, Conor Griffin, Po-Sen Huang, John Mellor,
AmeliaGlaese,MyraCheng,BorjaBalle,AtoosaKasirzadeh,etal. Taxonomyofrisksposedby
languagemodels. InProceedingsofthe2022ACMConferenceonFairness,Accountability,and
Transparency,pp.214–229,2022.
A DATASETS
We describe the construction and post-processing of our data in more detail in addition to
known limitations. All datasets and code are available at https://github.com/wesg52/
world-models.
WorldPlaces Weranthreeseparatequeriestoobtainthenames,location,country,andassociated
Wikipediaarticleofallphysicalplaces,naturalplaces,andstructureswithintheDBPediadatabase
Lehmannetal.(2015). UsingtheWikipediaarticlelink,wejoinedthisinformationwithdatafrom
theWikipediapageviewstatisticsdatabase3 toqueryhowmanytimesthispagewasaccessedover
2018-2020. WeusethisasaproxyforwhetherweshouldexpectanLLMtoknowofthisplaceor
not,andfilterthosewithlessthan5000viewsoverthistimeperiod.
Severallimitationareworthhighlighting. First, ourdataonlycomesfromEnglishWikipedia, and
henceisskewedtowardstheAnglosphere. Additionally, thedistributionofentitytypesisnotuni-
form,e.g. wenoticedtheUnitedKingdomhasmanymorerailwaystationsthananyothercountry,
whichcouldintroduceunwantedcorrelationsinthedatathatmayaffecttheprobes. Finally,about
25%ofthesampleshadsomesortofstateorprovincemodifierattheendlike“DallasCounty,Iowa”.
Becausemanyoftheselocationsweremoreobscureorwouldbeambiguouswithoutthemodifier,
so we chose to rearrange the string to be of the from “Iowa’s Dallas County” such the entity is
disambiguatedbutthatwearenotprobingonatokenthatisacommoncountryorstatename.
USA Places The United States places dataset uses structures and natural places within the US
from the world places dataset as a starting point, in addition to another DBPedia for US colleges.
Wethencollectthename,populationtotal,andstateforeverycounty4,zipcode5,andcity6 froma
censusdataaggregator.Wethenremoveallduplicatecountyorcitynames(thereare31Washington
countiesintheUS!),thoughwekeepanyduplicatesthathave2xthepopulationhasthenextlargest
placeofthesamename. Wealsofilteroutcitieswithfewerthan500people, zipcodeswithfewer
than10000(orwithpopulationdensitygreaterthan50andpopulationgreaterthan2000),andany
placenotinthelower48contiguousstates(orWashingtonD.C.).
NYC Places Our New York City dataset is adapted from the NYC Open Date points of interest
dataset(NYCOpenData,2023)containingthenamesoflocationstrackedbythecitygovernment.
Thisincludesthenamesofschools,placesofworship,transitlocations,importantroadsorbridges,
governmentbuildings,publichousing,andmore. EachoftheseplacescomeswithacomplexIDfor
locations comprised of multiple such buildings (e.g. New York University or LaGuardia airport).
Weconstructourtesttrainsplitstomakesurethatalllocationswithinthesamecomplexareputin
thesamesplittoavoidtest-trainleakage. Wefilteredoutalargenumberoflocationsdescribingthe
positionofbouysinthemultiplewaterwayssurroundingNYC.
HistoricalFigures Ourhistoricalfiguresdatasetcontainsthenamesandoccupationofhistorical
figures who died between 1000BC-2000AD adapted from (Annamoradnejad & Annamoradnejad,
2022). We filtered the dataset to only contain the 350 most famous people who died from each
decade,imperfectlymeasuredbytheindexoftheirWikidataentityidentifier.
3https://en.wikipedia.org/wiki/Wikipedia:Pageview_statistics
4https://simplemaps.com/data/us-counties
5https://simplemaps.com/data/us-zips
6https://simplemaps.com/data/us-cities
13

PublishedasaconferencepaperatICLR2024
Figure6: Distributionofsamplesinspaceortimeforalldatasets.
ArtandEntertainment Ourartandentertainmentdatasetconsistsofthenamesofsongs,movies,
and books with their corresponding artist, director, and author release date. We constructed this
dataset from DBpedia and similarly filtered out entities which had received less than 5000 page
views over 2018-2020. Because many songs or books have fairly generic titles, we include the
creator’s name in the prompt to disambiguate (e.g. “Stephen Kings’ It” for the empty prompt).
However, because some artists or authors release many songs or books, we sample our test-train
splitbycreatortoavoidleakage.
Headlines OurheadlinesdatasetisadaptedfromascrapeofallNewYorkTimesheadlinesofthe
past 30 years (Bandy, 2021). In an attempt to filter out headlines which do not describe an event
thatcouldbelocalizedintime,weemployanumberofstrategies. Firstwefilteranythingwhichis
notwithinthefirst10pagesoftheprintedition. Secondwefilteroutarticlesthatdon’tcomefrom
theForeign,National,Politics,Washington,orObitsnewsdesks. Thirdweremovedanytitlesthat
containedaquestionmark.
14

PublishedasaconferencepaperatICLR2024
B NEURON ABLATIONS AND INTERVENTIONS
TobetterunderstandtheroleofspaceandtimeneuronsinLLMs,weconductseveralneuronablation
andinterventionexperiments.
TimeIntervention Westudytheeffectofinterveningonasingletimeneuron(L19.3610;correla-
tionwithartandentertainmentreleasedateof0.77)withinLlama-2-7b. Givenapromptoftheform
<media> by <creator> was written in 19, we pin the activation of the time neuron
onalltokensandsweepoverarangeofpinnedvalues,andtrackthepredictedprobabilityofthetop
fivetokens. ResultsaredepictedinFigure7andshowthatjustadjustingthetimeneuronactivation
canchangethenexttokenpredictioninallcases.
Figure 7: Prediction of decade of publication for a famous song, movie, and book when a time
neuron(L19.3610)ispinnedtoaparticularvalue,comparedto9randomneuronswithinthesame
layer(L19.[0-8])ofLlama-2-7b.
NeuronAblations Wealsostudytheeffectofzeroablatingneurons,andthecontextsforwhich
the loss increases the most. For a subset of Wikipedia which includes articles corresponding to
worldplacesandcontemporaryartandentertainment,wefirstrunLlama-2-7basnormalandrecord
the loss. Then, for two space neurons and two time neurons, we run the model with the neuron
activationpinnedto0(wealwayspinexactlyoneneuronto0). Foreachneuron,wereportthetop
10contextsinwhichthelossmostincreasedforthenexttokenpredictioninTables5-8.
15

PublishedasaconferencepaperatICLR2024
context truetoken lossincrease
BomJesushasaratherdrytropicalsavannaclimate(Ko¨ppen Aw 2.107
linetropicalmonsoon/humidsubtropicalclimate(Ko¨ppen Am 2.035
of. Thehighesttemperaturesarereachedattheendofthedryseasonin March 1.960
8.9°C.InJanuary,theaveragetemperatureis1 8 1.930
aTropicalwet-and-dryclimate(Ko¨ppenclimateclassification Aw 1.876
Gorokahasarelativelycooltropicalmonsoonclimate(Ko¨ppen Am 1.854
ierangefrom26.4°FinJanuaryto7 0 1.835
wetsummersandwarm,verywetwinters(Ko¨ppenclimateclassification Am 1.807
tropicalwetanddryclimate/semi-aridclimate(Ko¨ppen Aw 1.783
ablymild,tropical-maritimeclimate,(Ko¨ppenclimateclassification Aw 1.762
Table5: ContextswiththehighestlosswhenablatingspaceneuronL20.7573fromLlama-2-7b.
context truetoken lossincrease
markisMountEtna,oneofthetallestactivevolcanoesin Europe 1.971
2,800years,makingitoneoftheoldestcitiesin Europe 1.676
keeperwith63capsforPortugalincludingparticipationinthe198 4 1.631
15. Tenerifealsohasthelargestnumberofendemicspeciesin Europe 1.512
Georgiatothesouth-west. MountElbrus,thehighestmountainin Europe 1.246
Atonepoint,thevillageboastedthelongestaluminiumrollingmillin Western 1.219
centreandtheleadingeconomichuboftheIberianPeninsulaandof Southern 1.181
aticanCity,asovereignstate—andpossiblythesecondlargestin Europe 1.103
name. ThisisbecausetheBritishIsleswerelikelyrepopulatedfromthe I 1.082
Category4stadiumbyUEFA,hostedmatchesatthe199 8 1.072
Table6: ContextswiththehighestlosswhenablatingspaceneuronL20.7423fromLlama-2-7b.
context truetoken lossincrease
wasreleasedinJune1993asthefourthsinglefromthealbum He 2.254
wasreleasedinNovember1992asthesecondsinglefromheralbum He 1.973
93. Yearwood’sversionwasthethirdsinglefromheralbum He 1.749
HotCountrySingles&Trackschart,behindShaniaTwain’s¨ Any 1.574
wasreleasedinFebruary1992asthethirdsinglefromthealbum What 1.559
andprovidedadditionalproductiononhersingles”LikeAPrayer”and” Express 1.481
wasreleasedinMay1992asthefourthsinglefromthealbum What 1.367
filmmakerRameshAravindinTelugucinema. P. L 1.328
993byrecordlabelColumbiaasthesecondsinglefromtheirsecondstudioalbum Gold 1.272
Gesslefortheduo’s1991album, Joy 1.253
Table7: ContextswiththehighestlosswhenablatingtimeneuronL18.9387fromLlama-2-7b.
context truetoken lossincrease
016asthethirdsinglefromReyesdebutstudioalbum,Louder ! 1.082
asthesecondradiosingleinsupportoftheband’sthirdstudioalbum, Life 0.996
Song,butultimatelylosttheawardtoBarbraStreisand’s” The 0.965
Releasedasthefirstsinglefromthegroup’sseventhstudioalbum, Super 0.961
original30CarryOnfilms(1958–19 7 0.912
. AfterlisteningtoNoDoubt’s2002single” Under 0.867
ix9ineforhisdebutmixtapeDay69(201 8 0.866
BA.Itwasoriginallyfeaturedonthegroup’sfifthstudioalbum,The Album 0.864
ckthatappearedinthePorkyPigcartoonsIt’s an 0.805
waswrittenbyAndrewLloydWebberandTimRiceandproducedby Fel 0.805
Table8: ContextswiththehighestlosswhenablatingtimeneuronL19.3610fromLlama-2-7b.
16

PublishedasaconferencepaperatICLR2024
C ADDITIONAL RESULTS
Figure8: Out-of-sampleR2whenentitynamesareincludedindifferentpromptsforallmodels.
17

PublishedasaconferencepaperatICLR2024
Figure9: Llama-2-70blayer50modeloftheUnitedstates. Pointsareprojectionsofactivationsof
heldoutUSplacesontolearnedlatitudeandlongitudedirectionscoloredbytruestate,withmedian
statepredictionenlarged. Allpointsdepictedarefromthetestset.
Figure10:Llama-2-70blayer50modeloftheworld.Pointsareprojectionsofactivationsofheldout
world places onto learned latitude and longitude directions colored by true continent. All points
depictedarefromthetestset.
18

PublishedasaconferencepaperatICLR2024
Figure 11: Out-of-sample predictions for each country when the probe training data contains no
samples from the country as compared to true locations and the mean of the training data. The
results imply that the learned feature direction correctly generalizes to the relative position of a
countrybutthattheprobesmemorizestheabsolutepositions.
19

PublishedasaconferencepaperatICLR2024
Figure12:Out-of-samplepredictionsforeachstatewhentheprobetrainingdatacontainsnosamples
from the state as compared to true locations and the mean of the training data. The results imply
thatthelearnedfeaturedirectioncorrectlygeneralizestotherelativepositionofacountrybutthat
theprobesmemorizestheabsolutepositions.
20

PublishedasaconferencepaperatICLR2024
Figure13: TestSpearmanrankcorrelationforprobestrainedonactivationsprojectedontoklargest
principalcomponents.
21
