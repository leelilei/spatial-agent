Title: SARAH: Spatially Aware Real-time Agentic Humans

Source PDF: /Users/mac/Documents/6-Research/4-SpatialAgent-Survey/assets/survey_paper/pdfs/phase1_adjacent/02_SARAH_Ng2026.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T02:55:05+00:00
- page_count: 10
- status: ok
- text_char_count: 48260

Metadata:
- author: Evonne Ng; Siwei Zhang; Zhang Chen; Michael Zollhoefer; Alexander Richard
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Abstract (page 1)
- 1 Introduction (page 1)
- 2 Related work (page 2)
  - 2.1 Gestural motion generation. (page 2)
  - 2.2 Proxemics in interpersonal communication (page 2)
  - 2.3 Realtime causal generative modeling. (page 2)
- 3 Real-time, Auto-regressive Motion Synthesis (page 2)
  - 3.1 Motion Representation (page 3)
  - 3.2 Causal Transformer-based VAE (page 3)
  - 3.3 Motion Generator (page 4)
  - 3.4 Controllable Gaze Guidance (page 4)
  - 3.5 Dyadic conversational dataset (page 4)
- 4 Experiments (page 5)
  - 4.1 Quantitative Results (page 6)
  - 4.2 Gaze Control (page 7)
- 5 Conclusion (page 7)
- Acknowledgments (page 7)
- References (page 9)
- A Supplementary Material (page 10)
  - A.1 Video Results (page 10)
  - A.2 Training Details (page 10)
  - A.3 Inference Details (page 10)

Markdown Content:

SARAH: Spatially Aware Real-time Agentic Humans
EvonneNg SiweiZhang ZhangChen MichaelZollhoefer AlexanderRichard
MetaRealityLabs
Redmond,WA,USA
Top down POV Third person POV First person POV
Goal: Spatially Aware Conversational Motion Input: User positions + Audios Output: Agent 3D Motion
Figure1:Ourmethodgeneratesfull-body3Dmotionforavirtualagentthatisspatiallyawareoftheuserwhileengagingina
conversation.Giventheuser’sfloor-projectedheadtrajectoryanddyadicaudio,wegeneratetheagent’scomplete3Dmotion.
Trajectorycolorsindicatetime:blue→green(user)andyellow→red(agent).Seeprojectpageforresults.
Abstract towardtheirconversationalpartners,shiftpostureastheymove,
AsembodiedagentsbecomecentraltoVR,telepresence,anddigital andmodulategazetosignalengagement.Moreover,comfortin
humanapplications,theirmotionmustgobeyondspeech-aligned levelsofeyecontactvarywidely—shapedbypersonalpreference,
gestures:agentsshouldturntowardusers,respondtotheirmove- socialcontext,andculturalnorms.Forvirtualagentstoreplicate
ment,andmaintainnaturalgaze.Currentmethodslackthisspatial thisbehaviorandappearhumanlike,theirmotionmustbeboth
awareness.Weclosethisgapwiththefirstreal-time,fullycausal spatiallyawareandcontrollable—orientingtowardtheuserwhile
methodforspatially-awareconversationalmotion,deployableon adaptinggazetoindividualpreferences.Currentmethods,however,
astreamingVRheadset.Givenauser’spositionanddyadicaudio, focusonconversationalcontextsinisolation,producingagentsthat
ourapproachproducesfull-bodymotionthatalignsgestureswith lacksituatedreasoning.
speechwhileorientingtheagentaccordingtotheuser.Ourarchi- Wepresentamethodforgeneratingfull-bodymotionforavir-
tecturecombinesacausaltransformer-basedVAEwithinterleaved tualagentthatrespondstoboththeconversationandtheuser’s
latenttokensforstreaminginferenceandaflowmatchingmodel spatialmovement—allinreal-time.Achievingsuchmotionrequires
conditionedonusertrajectoryandaudio.Tosupportvaryinggaze satisfyingfourcriteriasimultaneously.First,itmustbeconversation-
preferences,weintroduceagazescoringmechanismwithclassifier- allyappropriate—gesturesshouldalignnaturallywithspeech.Sec-
freeguidancetodecouplelearningfromcontrol:themodelcaptures ond,itmustbespatiallyaware—theagentshouldorienttowardand
naturalspatialalignmentfromdata,whileuserscanadjusteyecon- reacttotheuser’smovement.Third,itmustbecontrollable—gaze
tactintensityatinferencetime.OntheEmbody3Ddataset,our engagementshouldbeadjustabletosuitdifferentcontextsandpref-
methodachievesstate-of-the-artmotionqualityatover300FPS—3× erences.Fourth,itmustbereal-time—generationmustbecausal
fasterthannon-causalbaselines—whilecapturingthesubtlespatial andstreaming,withnoaccesstofutureinformation.Achievingall
dynamicsofnaturalconversation.Wevalidateourapproachona fourremainsanopenchallenge:state-of-the-artmethodseither
liveVRsystem,bringingspatially-awareconversationalagentsto ignorespatialcontext,requirenon-causalaccesstofutureframes,
real-timedeployment.Seeourprojectpagefordetails. orrunfarbelowreal-timespeeds.Wepresentthefirstmethodto
closethisgap.
Existinggesturegenerationmethodsarepredominantlymonadic:
1 Introduction they synthesize motion for a single speaker conditioned on au-
dioortext,withnoawarenessofaninterlocutor[Alexanderson
Embodiedconversationalagentsarebecomingcentraltoimmersive
etal.2023;Nyatsangaetal.2023;Yietal.2023].Thefewdyadic
applications—from virtual reality companions and telepresence
methodsthatexisttypicallyassumestationary,forward-facingpar-
avatarstosocialrobotsanddigitalhumans.Fortheseagentsto
ticipants—mimickingvideocallsratherthandynamic,in-person
feeltrulypresent,speechaloneisnotenough.Considerinteracting
interactions [Ng et al. 2022, 2024]. Moreover, popular state-of-
withanagentthatonlystaresforwardasyouwalkaroundit,or
the-artgenerativemodelsareoftentooslowforreal-timedeploy-
anagentthatwandersoffasyouaremid-sentence.Suchbehavior
ment[Ngetal.2022,2024]orrequirenon-causalaccesstofuture
immediatelybreakstheillusionofpresence.Humansnaturallyturn
6202
beF
02
]VC.sc[
1v23481.2062:viXra

arXiv,2026, Ngetal.
frames[Alexandersonetal.2023],precludingstreaminginference. etal.2024a;Yuetal.2023;Zhietal.2023].Beyondaudio,recent
Compoundingthis,existingdyadicdatasetslackthespatialdynam- workhasinvestigatedtext-andsemantics-basedconditioningfor
icsneededtolearnreactivebehavior.Asaresult,generatedagents stylizedgesturegeneration[Chengetal.2024;Zhangetal.2024].
remainstationaryandrigidlyfaceoneanother—lackingthefluid However, all of these works notably focus only on speakers in
spatialdynamicsofrealconversation. monadicsettings.
Ourkeyinsightistodecouplelearningfromcontrol:welearnthe
naturaldistributionofspatialalignmentfromdata,capturinggaze 2.2 Proxemicsininterpersonalcommunication
behaviorsfromsustainedeyecontacttodeliberateaversion,then
Oculesics (eye gaze and contact [Kendon 1967]) and proxemics
applyalightweightguidancemechanismatinferencetocalibrate
(interpersonaldistance[ArgyleandDean1965])playcrucialroles
orientationbasedonuserpreference.Thisseparationallowsthe
inregulatingturn-taking,signalingattention,andcommunicating
modeltogeneratemotionthatisbothnaturalistic(drawnfromthe
intent.Thesesignalshavebeenusedaspriorsforpredictingsocial
learneddistribution)andcontrollable(steeredtowardadesiredgaze
formations [Alahi et al. 2016], trajectory forecasting [Xie et al.
intensity).Toachievethis,weproposeareal-time,causalarchitec-
2024;Yangetal.2024],egocentricposeestimation[Ngetal.2020;
turebuiltontwocorecomponents.First,acausaltransformer-based
Zhangetal.2022],socialbehavioranalysis[Treuilleetal.2006],
VAEcompressesmotionintoatemporally-stridedlatentsequence,
andactivityrecognition[Bagautdinovetal.2017;HuangandKitani
withinterleavedlatenttokensenablingstreaminginferencewith-
2014;Pellegrinietal.2010].Unlikemethodsthatuseoculesicand
outsacrificingtemporalcoherence.Second,aflowmatchingmodel
proxemicinformationaspriors,wedirectlypredictthesesignals.
generatesmotioninthislatentspace,conditionedontheuser’s
Fine-grainedgazeandheadmotionmodelinghasbeenstudied
trajectoryandbothspeakers’audio.Forfine-grainedcontrol,we
fordyadicconversationalmotion[Ahujaetal.2019;Leeetal.2019;
introduceagazeguidancemechanismbasedonclassifier-freeguid-
Ngetal.2022,2024].However,manyfocusonforward-facingvideo
ance,allowinguserstomodulateeyecontactintensityatinference.
callswhereproxemicinformationislost[Ngetal.2022,2024],or
UnderpinningthesecomponentsisafullyEuclideanmotionrep-
use datasets where dyadic pairs remain stationary [Ahuja et al.
resentationthatimprovestrainingstabilityandenablesprecise
2019;Leeetal.2019].Duetoscarcedatasetscapturingglobalprox-
end-effectorcontrol.
emics,recentapproachesleverageLLMstoreasonaboutproxemic
WeevaluateontheEmbody3Ddataset[McLeanetal.2025],the
cuesvialanguage.Forexample,[Zhangetal.2025]usesanLLM
firsttocapturerealisticproxemicsindynamicspatialinteractions.
forhigh-levelgaze,proxemics,andposeguidanceindyadicinter-
Ourmethodachievesstate-of-the-artmotionqualitywhilerun-
actions,while[Subramanianetal.2024]employsanLLMtorefine
ningatover300FPS,outperformingnon-causalbaselines(MDM,
posesofcloselyinteractingindividuals.Incontrast,weadopta
A2P)thatare3×slower.Notably,wematchthegazealignmentof
supervisedapproachtodirectlylearnfine-grainedproxemicin-
non-causalmethodswithoutaccesstofutureuserpositions,demon-
formation. Closely related, [Joo et al. 2019] addresses gaze and
stratingthatreactivespatialbehaviorcanbelearnedcausally.The
turn-takingpredictionbutdecomposestheproblemintosub-tasks
generatedmotionisalsocontrollable:userscanmodulateeyecon-
withoutfull-bodylocomotion.Thisisthefirstworktoexplicitly
tactintensityatinferencetosuittheirpreferences.Wedeployona
modelfine-grainedproxemicsindynamic,interactivedyadiccon-
real-timeavatarsystem,confirmingviabilityforproduction.
versations.
Insummary,wepresentthefirstreal-timesystemforspatially-
aware conversational motion, enabling virtual agents to partic-
2.3 Realtimecausalgenerativemodeling.
ipateindynamicinteractions.Ourapproachcombinesacausal
Recentadvancesingenerativemotionsynthesishavefocusedon
transformer-basedVAEwithinterleavedlatenttokensforstream-
acausalmethods,e.g.vanilladiffusion[Alexandersonetal.2023;
inginference,aEuclideansurface-pointrepresentationforstable
Tevetetal.2022;Zhongetal.2024],whichrequirebothpastand
trainingandpreciseend-effectorcontrol,andaclassifier-freegaze
future context and are unsuitable for real-time applications. To
guidancemechanismforuser-adjustableeyecontact.Weachieve
addressthis,someapproachescombinevector-quantization(VQ)
state-of-the-artperformanceontheEmbody3Ddataset[McLean
withcausaltransformersforfast,autoregressivegeneration[Guo
etal.2025]andsuccessfullydeployourmethodonareal-timeavatar
etal.2024;Jiangetal.2023;Liuetal.2024b].
system.
Morerecently,diffusionmodelshavebeenadaptedforcausal
generationviaconditioningonpastframes[Chenetal.2024b;Zhao
2 Relatedwork
etal.2024]ordiffusionforcing[Chenetal.2024a].However,these
2.1 Gesturalmotiongeneration. stillrequiremultipleevaluationsteps,makingthemslowerthan
real-time.Thevideodiffusioncommunityhasadopteddistillation
Mostpriorworkongesturalmotiongenerationhasfocusedon
tocompressmulti-stepmodelsintosingle-stepmodelsforreal-time
single-person,co-speechgesturesynthesis[Nyatsangaetal.2023],
streaming[Kodairaetal.2025;Linetal.2025].Motivatedbythese
generatinggesturesthatalignwithspeakeraudio.Earlymethods
advances,weintroduceanautoregressive,single-stepflow-based
employedrecurrentneuralnetworks[Ghorbanietal.2023]and
modelforreal-timemotionstreaming.
feed-forwardarchitectures[Ginosaretal.2019;Kucherenkoetal.
2020].Morerecentapproachesuseautoregressivetransformersto
3 Real-time,Auto-regressiveMotionSynthesis
producevector-quantizedmotiontokens[Yietal.2023]thatdecode
intocontinuousmotion.Conditionaldiffusionmodelshavealso GivenauserandAIagentinconversation,ourgoalistogenerate
becomeprominent[Alexandersonetal.2023;Aoetal.2023;Liu the agent’s motion conditioned on both individuals’ audio and

SARAH:SpatiallyAwareReal-timeAgenticHumans arXiv,2026,
Ground Truth
𝑡=1 2 3 4 5 6 7
Inputs: … Inputs:
User position =𝒩(0,1) 𝑡=0 1 2 3 …
𝒛𝝉
𝒑𝒚 Agent Audio User Audio
𝒂 𝒃 ℰ 𝒂
𝒃
𝜇1 𝜎1 …
𝒑𝒚
𝒢
(𝒈)
𝜇1 𝜎1 𝜇2 𝜎2 …
𝜏
𝒟
𝒢
𝒟
𝑡=0 1 2 3 4 𝒛𝟏
…
Output: VAE Latents
Output: 3D motion
Reconstructions
Figure2:Giventheuser’s3Dpositionanddyadicconversationalaudio,ourmodelgenerates3Dmotionthatisconversationally
andspatiallyaware(left).Weuseafullycausaltransformer-basedVAEwithinterleavedlatenttokensatafixedtemporalstride;
bothencoderanddecoderemploycausalattention,whereeach𝜇/𝜎tokenattendsonlytoprecedingframesandearlierlatents
(center).Theselatentsarepassedtoatransformer-basedflowmatchingmodelthatalsousescausalmaskingandoptionally
acceptsagazescoreforcontrollingtheagent’seyecontact(right).Ourlightweightarchitectureenablesreal-time,autoregressive
streamingwithoutdistillation.
the user’s motion. Let x ∈ R𝑇×𝐷𝑥 and y ∈ R𝑇×𝐷𝑥 denote the
motionsequencesoftheagentanduserrespectively,where𝑇 isthe Centroid =Π"
sequencelengthand𝐷 𝑥 isthemotiondimension.Inheadset-based ref.
𝑆𝑉𝐷 =Ω!
systems,fullbodyposeisoftenunavailablewhileheadposition
is always accessible. We therefore condition only on the user’s
floorprojectedheadpositionp𝑦 ∈R𝑇×2,computedasthemidpoint
betweentheleftandrighteyesandprojectedtotheground.Let
a,b ∈ R𝑇×𝐷𝑎 denotetheaudiofeaturesofagentanduser,where
𝐷 𝑎istheaudiodimension.Wemodelthegenerationas:
x=G(p𝑦 ,a,b), (1)
whereGisourgenerativemodel.Foraudioconditioning,weextract
HuBERTfeatures[Hsuetal.2021]fromeachaudiostreamtoobtain Figure3:Werepresenteachjoint𝑗 asa3Dicosahedron.The
aandb. centroidoftheverticesyieldstheglobalposition𝚷 𝑗,andwe
recovertheglobalorientation𝛀 𝑗 viaSVDagainstareference
3.1 MotionRepresentation icosahedron.
Traditionally,humanmotionisrepresentedbylocaljointrotations
𝜽 withroottransforms(𝑅,t).Manymethodspredict𝜽 and(𝑅,t)di- originfacingthe𝑧-axisat𝑡=1.AsshowninTab.1,thisrepresen-
rectly,usingforwardkinematicsandlinearblendskinningtoobtain tationleadstoimprovedperformanceovertraditionaljoint-angle
meshesM∈R𝑇×𝑉×3.WefindthatafullyEuclideanrepresentation
parameterizations.
leadstofasterconvergenceandmorestabletraining.
Toavoiderrorpropagationfromlocalrotations,weencodeeach 3.2 CausalTransformer-basedVAE
joint 𝑗 asa3Dicosahedron:thecentroidofits12verticesyields
We propose a causal VAE architecture to support streaming in-
world-spaceposition𝚷 𝑗,whileSVDagainstareferenceicosahe-
ference.UnliketypicaltransformerVAEsthatplacegloballatent
dronrecoversorientation𝛀 𝑗 (Fig.3).Eachposeisthusrepresented
as𝑥 𝑡 ∈R𝐽×12×3,where𝐽 isthenumberofjoints.Weadditionally t te o r k l e e n av s e at la s t e e q n u t e to n k ce en s s ta a r t t a (e fi n x a e b d lin te g m b p id o i r r a e l c s t t i r o i n de al 𝑠 a . ttention),wein-
includemesh𝑀 𝑡 asashellaroundthejointstocapturesurface Concretely,theencoderEreceivesinputorderedas:
geometry.Topreventunboundeddrift,wenormalizerotationand
translationwithrespecttothefirstframe,aligningtheagentatthe (x 1:𝑠 , 𝜇 1 ,𝜎 1 , x𝑠+1:2𝑠 , 𝜇 2 ,𝜎 2 , ...), (2)

arXiv,2026, Ngetal.
where𝜇
𝑘
,𝜎
𝑘
∈R𝐷𝑧 arethemeanandvariancetokensforblock𝑘,
and𝐷 𝑧isthelatentdimension.Weapplycausalself-attention:each 𝑝 𝑦
frameattendsonlytopastframes,andeach𝜇 𝑘/𝜎 𝑘 tokenattendsto
precedingframesandearlierlatenttokens.ThedecoderDmirrors
𝑑
𝑥
thispattern.SeeFig.2foranoverview. 𝑑
𝑦
WeoptimizetheVAEwithreconstructionandKLlosses:
ℎ
𝑓
𝐾
L VAE =∥x−xˆ∥2 2 +𝛽 ∑︁ KL (cid:0)𝑞 𝜙(𝑧 𝑘 |x 1:𝑘𝑠)∥N(0,I)(cid:1), (3) ℎ 𝑏
𝑘=1
𝑔=𝑑 ∙𝑑
where𝑞 𝜙(𝑧 𝑘 | x 1:𝑘𝑠) = N(𝜇 𝑘 ,𝜎 𝑘 2) is the approximate posterior, 𝑥 𝑦
𝛽 is the KL weight, 𝐾 = 𝑇/𝑠 is the number of blocks, xˆ is the
reconstruction,and𝑧 𝑘 ∈ R𝐷𝑧 isthesampledlatentforblock𝑘. Figure4:Ourtrainingdataspansawiderangeofgazebehav-
Aftertraining,weusetheencodertoobtainthelatentsequence iors,fromsustainedeyecontacttocompletegazeaversion
z=(𝑧
1
,...,𝑧 𝐾) ∈R𝐾×𝐷𝑧. (left).Toenablecontrollablegazeatinference,wecomputea
gazescore𝑔,whered𝑥 istheagent’sfacingdirectionandd𝑦
3.3 MotionGenerator pointstowardtheuser(right).Thescoreapproaches1when
facingtheuserdirectlyand−1whenfacingaway.
Weadoptatransformer-basedflowmatchingmodelforreal-time,
causalmotiongeneration.Flowmatchingtransportssamplesfrom
noise𝝐 ∼N(0,I)todatabypredictingavelocityfieldv𝜃(z𝜏,𝜏,c), Weencodegazebasedonheadorientationrelativetouserposi-
where𝜏 ∈ [0,1] isflowtime,z𝜏 istheinterpolatedlatent,andc tion(Fig.4).Letℎ 𝑓 ,ℎ 𝑏 ∈R3denotethefrontandbackoftheagent’s
denotesconditioning. head.Wedefinetheagent’sfacingdirectionas:
We condition on the user’s head position p𝑦 and both audio ℎ
𝑓
−ℎ
𝑏
𝜏 st , r w ea e m fo s r a m ,b : ,predictingtheagent’slatentz∈R𝐾×𝐷𝑧.Atflowtime 𝑑 𝑥 = ∥ℎ 𝑓 −ℎ 𝑏∥ , (6)
z 𝜏 =𝜏z+(1−𝜏)𝝐, 𝝐 ∼N(0,I). (4) andthedirectiontowardtheuseras:
W ne e l c d o im nc e a n te s n io a n te , a z𝜏 pp w ly it i h ng co m nd o i d ti a o li n t i y n - g sp c e = cifi [p c 𝑦 p ; o a s ; i b t ] io a n lo a n l g en th co e d c i h n a g n s - . 𝑑 𝑦 = ∥ 𝑝 𝑝 𝑦 𝑦 − − ℎ ℎ 𝑏 𝑏∥ , (7)
Duringtraining,weenforceclassifierfreeguidancedroppingeach Thegazescoreisthenthedotproductbetweentheseunitvectors:
m tim od e a st li e t p y 𝜏 in i d s e i p n e je n c d t e e n d tl v y ia w a i d th ap a tiv 5 e p l e a r y c e e r n n t o p r r m ob a a li b z i a l t it io y. n T [ h P e ee fl b o le w s 𝑔=𝑑 𝑥 ·𝑑 𝑦 . (8)
andXie2023].Using𝑥 -prediction,wetrain: Intuitively,𝑔approaches1whentheagentfacestheuserdirectly,0
1
L flow =E 𝜏,𝝐,z (cid:2) ∥G(z 𝜏,𝜏,c)−z∥2 2 (cid:3), (5) w ey h e e c n o l n o t o a k c i t n c g o p r e re rp sp en o d n i d c s u t la o r, m a a n x d im −1 iz w in h g e 𝑔 n . facingaway.Maximizing
where𝜏 ∼U[0,1]. Duringtraining,weconcatenatetheper-framegazescoreg∈
Forreal-timestreaming,weenforcestrictcausalityviacausal R𝑇×1 with the conditioning c = [p𝑦;a;b;g] along the channel
attentionmasking.Atinference,wegeneratemotionautoregres- dimension,andapplyclassifier-freeguidancebydroppinggwith
sivelybymaintainingahistorybufferofpreviouslypredictedla- 5percentprobability.Atinference,wespecifyatargetgazescore
tents.Ratherthanconditioningonpastmotionexplicitly—which tocontroleyecontactintensity.Crucially,guidancegentlysteers
ledtomodecollapse—weenforcetemporalconsistencythrough output toward the desired gaze range while preserving natural
imputation.Giventhepredictedhistoryz 1:𝑘−1 ,wecomputethe aversionsandvariation,yieldingrealisticanddiversemotion.
correspondingnoisylatentsviaEq.4andsamplefreshnoiseforthe
remainingsequence.Ateachdenoisingstep,wereplacethenoisy 3.5 Dyadicconversationaldataset
historytokenswiththeirimputedvaluesbeforeproceeding.After WeusethedyadicconversationsubsetoftheEmbody3Ddataset
denoising,weappendthenewlypredictedlatenttothehistory [McLeanetal.2025].Thissubsetcontainsaround50hourscaptured
bufferandslideforwardbyoneblock. inamultiviewdome.Theconversationscoveravastarrayoftopics,
includingcasualconversations,workdiscussions,andsocialinter-
3.4 ControllableGazeGuidance
actions.Thedemographicsarediverseacrossagegroups,genders,
Eye contact is a key non-verbal cue: more signals engagement, andethnicities.Weusetheaudioand3Dmotionannotationsfrom
whilelessmayindicatereserve.However,appropriateeyecontact thedataset.
varieswidely—dependingonpreference,socialcontext,andcultural Thisisthefirstdatasettocapture3Dspatialproxemicsincon-
norms.Thisvariabilitymotivatesmakinggazebehaviorexplicitly versation.PriormonadicdatasetssuchasSpeech2Gesture[Ginosar
controllableatinferencetime.Whileconditioningonuserposition etal.2019]andBEAT[Liuetal.2022]offerdiversemotionbut
enablesplausiblereactivemotion,itrestrictsoutputtothegaze lackspatialcontext,capturingasinglespeakerinisolation.Exist-
distributionintrainingdata(Sec.3.5).Toprovidefinercontrol,we ingdyadicdatasetssuchasAudio2Photoreal[Ngetal.2024]and
introduceatunablegazeguidancemechanismthatmodulateseye PanopticStudio[Jooetal.2019]capturetwo-personinteractions,
contactintensitybasedonuserpreference. butparticipantsremainstationaryandalwaysfaceoneanother.In

SARAH:SpatiallyAwareReal-timeAgenticHumans arXiv,2026,
contrast,Embody3Dcontainsscenarioswhereindividualswalk Thispoolingisnecessarybecauseindividualbatchesmaycontain
freely,shiftpositions,andengageinnatural,dynamicconversations. toofewclipsofonecategoryforreliablecovarianceestimation.
Asaconsequence,theper-batchaveragessystematicallyexceed
thepooledS/NSvaluesduetosmall-sample-sizebiasincovariance
4 Experiments estimation,andtheAvgisnotasimpleweightedcombinationofS
andNS.NotethatFGD issubstantiallyhigherforspeakingclips
Weevaluateourmodel’sabilitytogeneraterealistic,spatially-aware acc
thannon-speakingclips,reflectingincreasedgesturaldynamics
conversationalmotion.Followingpriorworks[Ngetal.2024;Yi
duringspeech.
etal.2023],wequantitativelymeasurerealismanddiversityagainst
groundtruth,andadditionallyassessgazealignmenttodetermine
whethertheagentappropriatelyorientstowardtheuserwithinthe Baselines and Ablations. Since no prior work addresses real-
distributionofnaturalconversationalbehavior.Ourresultsshow time,spatially-awareconversationalmotiongeneration,wecan-
thatourmodelgeneratesmotioncompetitivewithstate-of-the-art notdirectlycompareagainstexistingmethods.Toensureafair
methods—includingnon-causal,non-real-timeapproaches—while comparison, we retrain all prior works on our dataset and mo-
beingbothcausalandreal-time.Forqualitativeresults,please tionrepresentation(Sec.3.1).Wedeliberatelyselectfoundational
refertotheSupp.Video. architectures—diffusion-based,VQ-based,andhybridmethods—that
underpinmanyrecentstate-of-the-artsystems,ratherthantask-
ImplementationDetails. Wetrainourmodelandrunallexperi-
specificvariantswithadditionalmodules(e.g.,textencodersor
mentsonanA100GPU.Forallexperiments,wesetthesequence
domain-specific losses). This ensures a fair comparison of core
length𝑇 = 400.Videosaresampledat30fpswhiletheaudiois
generativecapabilities.Wecompareagainst:
sampledat48kHz.Forthemotionrepresentation,weuseMHR[Fer-
gusonetal.2025]whichallowsustorenderphotorealisticavatars. • Random:Randomlysamplesamotionsequencefromthe
ForourVAE,weastrideof𝑠 =4,andtheencoderanddecodereach
trainingset,providingalowerboundonperformance.
have9layerswith4attentionheadsandahiddendimensionof256. • NN:Anearest-neighborretrievalbaselinethatselectsmotion
Weset𝛽 =1𝑒−4fortheKLloss.Fortheflowmatchingmodel,we
basedontheconditioninginputs.Foraudiomatching,we
encodeeachmodalityusingalearnedpositionalencodingbefore
useHuBERTembeddings.Weusealibraryof2048motion
concatenatingthemalongthechanneldimension.Wethenuserope
sequencesrandomlysampledfromthetrainingsetandmatch
fortemporalpositionalencoding.Toincorporatethenoisetimestep,
acrossthefullclipratherthanviaslidingwindows,which
weuseAdaLNZero.Weuse4transformerlayerswith4attention
yieldedbettertemporalcoherenceandoverallperformance.
headsandhiddendimensionof1024.Wetrainwithlocalbatchsize • MDM[Tevetetal.2022]:Adiffusion-basedmodeloriginally
of16across8gpu’s.Duringinference,weuseacfgof1.3tocontrol
designedfortext-conditionedmotiongenerationthathas
theconditioningstrength.Sincenotallmethodsareautoregressive
sincebecomeafoundationformanysubsequentmethods
orcausal,wecalculatethemethod’sfpsbygeneratingall400frames
thathaveextendedittosupportvariousconditioningsignals.
inonegoandthendividingthetotaltimetakenby400.
WeadaptMDMtousethesameconditioninginputsforour
domain:agentaudio,useraudio,anduserheadtrajectory.It
EvaluationMetrics. Weevaluatemotionalongfiveaxes:
operatesnon-causallyanddoesnotruninreal-time.
(1) FGD(FréchetGestureDistance),whichmeasuresdistribu-
• A2P[Ngetal.2024]:AhybridapproachcombiningVQ-based
tionalsimilaritybetweengeneratedandground-truthposes
discreterepresentationswithdiffusion-basedrefinement.It
viatheFréchetdistanceoverthevertexpositionsofthemesh;
operatesautoregressivelybutisnotreal-timeduetoitsmulti-
(2) FGD ,thesamemetriccomputedonaccelerationtoassess
acc stagepipeline.
motionsmoothnessanddynamics;
• SHOW[Yietal.2023]:AVQ-basedautoregressivemodel
(3) FootSlide,thefractionofframeswherefeetarenearthe
designedtogenerateupper-body,conversational3Dmotion
ground(<5cm)yetmovinghorizontally(>3cm/s),indicat-
fromspeech.ItemploysseparateVQ-VAEsforarmandhand
ingskatingartifacts;
movements, followed by an autoregressive generator for
(4) WristVar,theaveragewristvelocitymeasuringgesture
fullupper-bodymotion.Withminimalmodificationtothe
expressiveness;and
originalarchitecture,weconditionSHOWonagentaudio
(5) HeadAng.,themeandotproductbetweentheagent’sfacing
alonetoevaluatehowexistingaudio-onlymethodsperform
directionandthevectortowardtheuser,quantifyinggaze
inspatially-awaresettings.
alignment(1=facinguser,−1=facingaway).
Weclassifyeachclipasspeaking(S)ornon-speaking(NS)based Wealsorunablationstudiestoisolatetwokeydesignchoices:
ontheagent’saudioenergy,andreportbothanoverallaverage ourmotionrepresentationandlatentcompressionviatheVAE.
andseparateS/NSvaluesforeachmetrictoenableanalysisacross
conversationalcontexts.Formostmetrics,theaveragereflectsa • OursinJointSpace(IK):InsteadofourEuclideanrepre-
weighted mean of the S and NS values. However, for FGD and sentation(Sec.3.1),weencodetraditionaljointangleswith
FGD ,thecomputationdiffers:theAvgcolumnreportsthemean theVAE.Meshpositionsarethenrecoveredviainversekine-
acc
ofper-batchFréchetdistances,whereastheSandNSvaluesareeach matics.
computedbyfirstpoolingallclipsofthatcategoryacrossallbatches, • Oursw/oVAE:WeremovethecausalVAE,directlypredict-
thenmeasuringasingleFréchetdistanceonthepooleddistribution. ingEuclideanpositionsfromthetransformer.

arXiv,2026, Ngetal.
Table1:Comparisonwithbaselinesandablations(abl.)on2048testsequences.C=causal,R=real-time.S=speaking(544seq.),
NS=non-speaking(1504seq.).↑higherisbetter,↓lowerisbetter.†Reducibleto600fpswithoutqualitydegradation.
FPS FGD↓(m×101) FGD
acc
↓(×105) FootSlide↓∈[0,1] WristVar↑ HeadAng.↑∈[−1,1]
C R Avg NS/S Avg NS/S Avg NS/S Avg NS/S Avg NS/S
GT – – – – – – – 0.01 0.01/0.01 137.6 122.3/179.7 0.81 0.80/0.84
senilesaB
Random ✗ ✓ 4K 1.06 0.30/0.28 1.83 0.31/3.38 0.01 0.01/0.01 188.1 190.5/181.6 0.28 0.27/0.32
NN ✗ ✓ 1K 0.90 0.19/0.16 0.77 0.02/0.51 0.01 0.01/0.01 97.0 85.7/128.2 0.59 0.57/0.64
MDM[Tevetetal.2022] ✗ ✗ 90 3.48 1.93/2.66 2.88 0.64/5.37 0.11 0.11/0.11 61.4 57.9/71.0 0.81 0.80/0.84
A2P[Ngetal.2024] ✗ ✗ 90 2.01 0.54/0.80 2.31 0.43/4.95 0.02 0.02/0.02 69.4 59.0/98.2 0.71 0.70/0.73
SHOW[Yietal.2023] ✓ ✓ 230 1.99 0.65/0.77 2.22 0.02/8.10 0.27 0.26/0.32 65.0 58.0/84.4 0.61 0.60/0.64
.lbA OursinJointSpace(IK) ✓ ✓ 300 2.35 0.40/0.81 2.26 0.01/7.93 0.03 0.03/0.04 87.1 80.4/105.7 0.72 0.71/0.75
Oursw/oVAE ✓ ✓ 150 1.95 0.42/0.76 2.24 0.01/8.08 0.01 0.01/0.01 96.9 90.3/115.2 0.78 0.77/0.81
Ours ✓ ✓ 300† 1.28 0.35/0.87 2.19 0.01/7.81 0.01 0.01/0.01 105.0 90.1/146.2 0.83 0.82/0.85
Table2:Effectofgazecontrolonmotion.∅denotesthatgaze
controlisdisabled. Generativebaselines. Toevaluateagainstnon-real-timestate-of-
the-artinthedyadic(two-person)setting,weadaptMDMand
𝑔 FGD↓ FGDacc ↓ FootSlide↓ WristVar↑ HeadAng.↑ A2Ptousethesameuser-awareconditioningasOurs:agentau-
∅ 1.28 2.19 0.01 105.0 0.83 dio,useraudio,anduserheadtrajectory.Whennaivelyadapted
toourdomain,MDMachievestheworstFGD(3.48)amongall
0.0 0.99 2.18 0.01 111.1 0.56
methods.AnalysisrevealsthatMDMproducesover-smoothedmo-
0.8 0.92 2.19 0.01 110.8 0.76
tion:itswristvariance(61.4)isonly45%ofGT(137.6),indicating
1.0 1.49 2.20 0.01 106.6 0.96
severelydampenedgestures.Thislikelyreflectsanarchitecture
mismatch:MDMwasdesignedfortext-to-motionwithcoarseac-
tiondescriptions,notfine-grainedaudio-gesturesynchronization
4.1 QuantitativeResults andmayfavorglobalmotioncoherenceoverlocaldynamics.MDM
Tab.1summarizesourmainresultsacrossfiveevaluationaxes.We appropriatelymatchesthegroundtruthgazealignment(0.81)per-
organizeouranalysisbyfirstexaminingretrievalbaselines,then fectly—perhapsduetoitsnon-causalarchitecturehavingaccessto
generativebaselines,andfinallyourablations. futureuserpositionstoallowittopreemptivelyreactaccordingly.
Incontrast,Oursachievessimilargazealignment(0.83)whileop-
eratingcausally,demonstratingthatgazealignmentcanbelearned
RetrievalBaselines(Random,NN). Theretrievalbaselinesachieve
withoutrequiringfutureinformation.MDMalsoexhibitssignifi-
thelowestFGDscores(Random:1.06,NN:0.90)sincetheysam-
cantfootsliding(0.11),suggestingthatdiffusiondirectlyoverthe
pledirectlyfromthetruedatadistribution—outperformingOurs
euclideanrepresentationactuallystrugglestomaintainphysical
(1.28)onthismetricalone.However,thisadvantageissuperficial:
constraintswithoutalearnedlatentprior.
retrievalmethodscannotjointlysatisfyallcriteria.Random’sgaze
A2PextendsMDMwithanadditionalVQ-basedstage:discrete
alignmentscore(0.28)iscatastrophiccomparedtoOurs(0.83)since
tokensarefirstgeneratedautoregressively,thenrefinedviadif-
randomlysampledmotionbearsnorelationtouserposition.NN
fusion. This two-stage approach reduces FGD and foot sliding
addressesthisbyjointlymatchingaudiofeatures(HuBERTem-
comparedtoMDM.However,A2Pstillfallsshortof Oursacross
beddings)anduserposition,improvingthegazealignmentto0.59.
allmetrics:higherFGD(2.01vs.1.28),lowerwristvariance(69.4
WhilebetterthanRandom,thisstillfallsshortof Ours(0.83)for
vs.105.0),andweakergazealignment(0.71vs.0.83).Qualitatively,
tworeasons:(1)jointlymatchingaudioandspatialfeaturesisnon-
wefindthatA2P’scoarseVQkeyframescanlagtemporally,forcing
trivial,asoptimizingforonemaycompromisetheother,and(2)
thediffusionstagetocorrectformisalignedtargets.Thisresults
noclipinthedatasetexactlymatchesthetargetusertrajectory.
indampenedgestures(lowerwristvariance)andtemporallyoffset
Whilebothretrievalmethodsachievenear-zerofootsliding(0.01)
gaze(lowergazealignment).Bothdiffusionmethodsalsorunat
bycopyingrealmotion(matchingOurs),theirwristvariancere-
only90FPS—3×slowerthanOurs—andtheirrelianceonfuture
vealsfurtherlimitations:Random(188.1)overshootsGT(137.6)
contextpreventsdeploymentinstreamingapplications.
duetocontext-agnosticsampling,whileNN(97.0)undershootsas
Unlikethediffusionmethods,SHOWoperatescausallyat230
retrievalfavorscommon,lessexpressiveclips.Ours(105.0)strikes
FPS,makingitthemostarchitecturallycomparablebaselinetoOurs.
abetterbalance.Theseresultshighlightakeydistinction:while
Weevaluateitwithoutuserconditioningtoserveasamonadic
retrieval achieves strong distributional metrics by construction,
(single-agent)baseline.However,SHOWstruggleseveninitsorigi-
it is fundamentally limited to what exists in the dataset. Ours
naldomain—suggestingfundamentalarchitecturallimitationseven
insteadgeneratesnovelmotionthatjointlyoptimizesforallcrite-
withoutuserconditioning.Onfootsliding,thegapisstark:SHOW
ria—achievingcompetitiveFGD(1.28)whiledramaticallyimproving
(0.27) is 27× worse than Ours (0.01), likely due to its separate
spatialawareness(0.83vs.NN’s0.59).

SARAH:SpatiallyAwareReal-timeAgenticHumans arXiv,2026,
4.2 GazeControl
Weevaluategazecontrollabilitybyvaryingtheguidanceparameter
𝑔attesttimeandapplyingclassifier-freeguidancetoenforcethe
desiredalignment(Tab.2).AsshowninFig.5,increasing𝑔from0.0
𝑔=∅ 𝑔=0.5 (lookingaway)to1.0(alwaysfacingtheuser)alsoincreasesgaze
alignmentaccordingly(0.56→0.96).Thisconfirmsourmethod’s
abilitytoexplicitlycontroloveragentorientation.At𝑔=0.8,which
bestmatchesgroundtruth(0.81),weevenoutperformthedefault
no-guidancecase(∅)withlowerFGD(0.92vs.1.28)andslightly
higherwristvariance.Thissuggeststhatmoderategazeguidance
𝑔=0.8 𝑔=1.0
providesusefulspatialgroundingthatimprovesoverallmotion
quality.At𝑔=1.0,gazealignmentreaches0.96butFGDrisesto1.49,
Figure5:Wevisualizetheagent’sfacingdirectionviapro-
reflectingthetrade-offbetweenstrictgazeadherenceandnatural
jectedlines(agent:yellow→red;user:blue→green).With
noalignment𝑔=∅,theagent’sgazeismorediverse;aswe
motionvariation.At𝑔=0.0,gazealignmentdropsto0.56ratherthan
increase𝑔,theagentincreasinglyturnstowardstheuser. zero,sincecompleteaversionisrareinthedataset—theagentturns
considerablyawayfromtheuserbutstilladherestothelearned
distribution.
VQ-VAEsforarmsandhands—originallydesignedforupper-body
5 Conclusion
motion—whichlackbody-groundcoordinationwhenextendedto
full-bodygeneration.Onexpressiveness,SHOW’swristvariance Wepresentedthefirstmethodforspatially-awareconversational
(65.0)fallswellbelowOurs(105.0).Qualitatively,SHOWproduces motion, enabling virtual agents to orient toward and react to a
sweepinggesturesbutstruggleswiththerapid,fine-grainedmo- movinguserinreal-timewhileproducingnatural,speech-aligned
tionimportantforexpressivespeech—dynamicsthatOurscaptures gestures.Thearchitecturepairsanovelcausaltransformer-based
throughitsflow-basedformulation.Asexpected,thelargestgap VAEwithaflowmatchingmodelconditionedonusertrajectory
isinspatialawareness:SHOW’sgazealignment(0.61)fallswell anddyadicaudio.Recognizingthatgazepreferencesvary,wein-
belowOurs(0.83).Thishighlightsakeylimitationofaudio-only troduceagazealignmentscoresteeredviaclassifier-freeguidance,
conditioning—theaudiosignaldoesnotencodeuserposition,sothe decouplinglearningfromcontrol.Experimentsshowstate-of-the-
modelcannotlearnappropriateorientation.Oursaddressesthisdi- artqualityatover300FPS,outperformingnon-causalbaselines3×
rectlythroughexplicituserconditioning,enablingspatially-aware slower.Thecausal,real-timenatureenablesdeploymentinstream-
generation. ingheadsetenvironments.
Ourmethodinheritstrainingdatabiases:underrepresentedspa-
Ablations. Weisolatethecontributionsofkeydesignchoices.
tialconfigurationsorgazebehaviorsmaygeneralizepoorly.While
OursinJointSpace(IK)replacesourEuclideansurface-point
wedemonstratecontrollablegaze,otherbehaviors—gesturestyle,
representationwithtraditionaljointangles,requiringinversekine-
locomotion—arenotyetcontrollable.Extendingtomulti-partycon-
maticstorecovermeshpositions.Acoreissueisthatjoint-angle
versationswouldrequirearchitecturalmodifications.
predictionsfaceinherentambiguity—multipleconfigurationscan
producesimilarend-effectorpositions.Thisdirectlyimpactsmet- Acknowledgments
ricsthatdependonprecisepositioning:gazealignmentdropsfrom
We would like to thank the Embody 3D team for making this
0.83to0.72(headorientation),andfootslidingincreasesfrom0.01
projectpossible.WewouldalsoliketothankAbhayMittal,Anasta-
to0.03(foot-groundcontact).Theambiguitymayalsoencourage
sisStathopoulos,andEthanWeberforhelpfuldiscussions.Thank
conservativepredictions,whichisreflectedinwristvariancede-
you,VasuAgrawal,MartinGleize,andSrivathsanGovindarajan
creasingfrom105.0to87.1—themodelproduceslessexpressive
formakingthedemopossible.
motionwhenend-effectortargetsareuncertain.Theseresultsmoti-
vateourEuclideansurface-pointapproach,whichdirectlyspecifies
end-effectorpositionswithoutambiguity.
Ours w/o VAE removes the causal VAE, directly predicting
motionfromthetransformer.WithouttheVAE’slearnedlatent
structure,themodelmustpredicthigh-dimensionalmotiondirectly,
makingithardertocapturethetruemotiondistribution—FGDrises
from1.28to1.95.However,physicalplausibilitymetricsremain
stable:footslidingstaysat0.01andwristvariance(96.9)remains
comparabletoOurs(105.0).ThisindicatesthattheVAE’sprimary
benefitisdistributional—matchingthemotionmanifold—rather
thanenforcingphysicalconstraints,whichourEuclideanrepresen-
tationseemstohandle.Inferencespeedalsohalves(300to150FPS),
aspredictinginthecompressedlatentspaceismoreefficientthan
directlygeneratinghigh-dimensionalmotion.

arXiv,2026, Ngetal.
V
O
P
n
o
sre
p
d
r3
V
O
P
n
o
sre
p
ts1
V
O
P
n
o
sre
p
d
r3
V
O
P
n
o
sre
p
ts1
V
O
P
n
o
sre
p
d
r3
V
O
P
n
o
sre
p
ts1
Figure6:Sequencesfromourreal-timedemosystem,renderedwithaphotorealisticavatar.Thetoprowvisualizestheuser’s
headsetlocationasasilversphere.Thebottomrowshowsthegeneratedavatarfromtheuser’s(headset)viewpoint.Ourmethod
generatesrealisticconversationalmotionthatisresponsivetotheuser’sspatialmotion.Fullvideosareavailableonourproject
page.

SARAH:SpatiallyAwareReal-timeAgenticHumans arXiv,2026,
References
body-fingermotionandaudioforconversationalmotionanalysisandsynthesis.In
ChaitanyaAhuja,ShugaoMa,Louis-PhilippeMorency,andYaserSheikh.2019.Toreact ProceedingsoftheIEEE/CVFInternationalConferenceonComputerVision.763–772.
ornottoreact:End-to-endvisualposeforecastingforpersonalizedavatarduring ShanchuanLin,XinXia,YuxiRen,CeyuanYang,XuefengXiao,andLuJiang.2025.
dyadicconversations.In2019InternationalConferenceonMultimodalInteraction. Diffusionadversarialpost-trainingforone-stepvideogeneration.arXivpreprint
74–84. arXiv:2501.08316(2025).
AlexandreAlahi,KratarthGoel,VigneshRamanathan,AlexandreRobicquet,LiFei-Fei, HaiyangLiu,XingchaoYang,TomoyaAkiyama,YuantianHuang,QiaogeLi,Shigeru
andSilvioSavarese.2016. Sociallstm:Humantrajectorypredictionincrowded Kuriyama,andTakafumiTaketomi.2024a.Tango:Co-speechgesturevideoreen-
spaces.InProceedingsoftheIEEEconferenceoncomputervisionandpatternrecogni- actmentwithhierarchicalaudiomotionembeddinganddiffusioninterpolation.
tion.961–971. arXivpreprintarXiv:2410.04221(2024).
SimonAlexanderson,RajmundNagy,JonasBeskow,andGustavEjeHenter.2023. HaiyangLiu,ZihaoZhu,GiorgioBecherini,YichenPeng,MingyangSu,YouZhou,
Listen,denoise,action!audio-drivenmotionsynthesiswithdiffusionmodels.ACM XuefeiZhe,NaoyaIwamoto,BoZheng,andMichaelJBlack.2024b.Emage:Towards
TransactionsonGraphics(TOG)42,4(2023),1–20. unifiedholisticco-speechgesturegenerationviaexpressivemaskedaudiogesture
TenglongAo,ZeyiZhang,andLibinLiu.2023.GestureDiffuCLIP:Gesturediffusion modeling.InProceedingsoftheIEEE/CVFConferenceonComputerVisionandPattern
modelwithCLIPlatents.arXivpreprintarXiv:2303.14613(2023). Recognition.1144–1154.
MichaelArgyleandJanetDean.1965.Eye-contact,distanceandaffiliation.Sociometry HaiyangLiu,ZihaoZhu,NaoyaIwamoto,YichenPeng,ZhengqingLi,YouZhou,
(1965),289–304. ElifBozkurt,andBoZheng.2022. BEAT:ALarge-ScaleSemanticandEmo-
TimurBagautdinov,AlexandreAlahi,FrançoisFleuret,PascalFua,andSilvioSavarese. tionalMulti-ModalDatasetforConversationalGesturesSynthesis.arXivpreprint
2017.Socialsceneunderstanding:End-to-endmulti-personactionlocalizationand arXiv:2203.05297(2022).
collectiveactivityrecognition.InIEEEConferenceonComputerVisionandPattern ClaireMcLean,MakenzieMeendering,TristanSwartz,OrriGabbay,AlexandraOlsen,
Recognition(CVPR). RachelJacobs,NicholasRosen,PhilippedeBree,TonyGarcia,GadsdenMerrill,
TimurBagautdinov,ChengleiWu,TomasSimon,FabianPrada,TakaakiShiratori, JakeSandakly,JuliaBuffalini,NehamJain,StevenKrenn,MoneishKumar,Dejan
Shih-EnWei,WeipengXu,YaserSheikh,andJasonSaragih.2021.Driving-signal Markovic,EvonneNg,FabianPrada,AndrewSaba,SiweiZhang,VasuAgrawal,
awarefull-bodyavatars.ACMTransactionsonGraphics(TOG)40,4(2021),1–17. TimGodisart,AlexanderRichard,andMichaelZollhoefer.2025. Embody3D:A
BoyuanChen,DiegoMartíMonsó,YilunDu,MaxSimchowitz,RussTedrake,and Large-scaleMultimodalMotionandBehaviorDataset. TechnicalReport.arXiv.
VincentSitzmann.2024a. Diffusionforcing:Next-tokenpredictionmeetsfull- https://arxiv.org/pdf/2510.16258arXivpreprint.
sequencediffusion.AdvancesinNeuralInformationProcessingSystems37(2024), EvonneNg,HanbyulJoo,LiwenHu,HaoLi,TrevorDarrell,AngjooKanazawa,and
24081–24125. ShiryGinosar.2022.Learningtolisten:Modelingnon-deterministicdyadicfacial
RuiChen,MingyiShi,ShaoliHuang,PingTan,TakuKomura,andXuelinChen.2024b. motion.InProceedingsoftheIEEE/CVFConferenceonComputerVisionandPattern
Tamingdiffusionprobabilisticmodelsforcharactercontrol.InACMSIGGRAPH Recognition.20395–20405.
2024ConferencePapers.1–10. EvonneNg,JavierRomero,TimurBagautdinov,ShaojieBai,TrevorDarrell,Angjoo
QingrongCheng,XuLi,andXinghuiFu.2024. Siggesture:Generalizedco-speech Kanazawa,andAlexanderRichard.2024. Fromaudiotophotorealembodiment:
gesturesynthesisviasemanticinjectionwithlarge-scalepre-trainingdiffusion Synthesizinghumansinconversations.InProceedingsoftheIEEE/CVFConference
models.InSIGGRAPHAsia2024ConferencePapers.1–11. onComputerVisionandPatternRecognition.1001–1010.
AaronFerguson,AhmedA.A.Osman,BertaBescos,CarstenStoll,ChrisTwigg, EvonneNg,DonglaiXiang,HanbyulJoo,andKristenGrauman.2020.You2me:Inferring
ChristophLassner,DavidOtte,EricVignola,FabianPrada,FedericaBogo,Igor bodyposeinegocentricvideoviafirstandsecondpersoninteractions.InProceedings
Santesteban,JavierRomero,JennaZarate,JeongseokLee,JinhyungPark,Jin- oftheIEEE/CVFconferenceoncomputervisionandpatternrecognition.9890–9900.
longYang,JohnDoublestein,KishoreVenkateshan,KrisKitani,LadislavKavan, SimbarasheNyatsanga,TarasKucherenko,ChaitanyaAhuja,GustavEjeHenter,and
MarcoDalFarra,MatthewHu,MatthewCioffi,MichaelFabris,MichaelRanieri, MichaelNeff.2023. Acomprehensivereviewofdata-drivenco-speechgesture
MohammadModarres,PetrKadlecek,RawalKhirodkar,RinatAbdrashitov,Ro- generation.InComputerGraphicsForum,Vol.42.WileyOnlineLibrary,569–596.
mainPrévost,RomanRajbhandari,RonaldMallet,RussellPearsall,SandyKao, WilliamPeeblesandSainingXie.2023.Scalablediffusionmodelswithtransformers.In
SanjeevKumar,ScottParrish,Shoou-IYu,ShunsukeSaito,TakaakiShiratori,Te-Li ProceedingsoftheIEEE/CVFinternationalconferenceoncomputervision.4195–4205.
Wang,TonyTung,YichenXu,YuanDong,YuhuaChen,YuanluXu,YutingYe,and StefanoPellegrini,AndreasEss,andLucVanGool.2010.Improvingdataassociation
ZhongshiJiang.2025. MHR:MomentumHumanRig. arXiv:2511.15586[cs.GR] byjointmodelingofpedestriantrajectoriesandgroupings.InEuropeanConference
https://arxiv.org/abs/2511.15586 onComputerVision(ECCV).
SaeedGhorbani,YlvaFerstl,DanielHolden,NikolausFTroje,andMarc-AndréCar- SanjaySubramanian,EvonneNg,LeaMüller,DanKlein,ShiryGinosar,andTrevor
bonneau.2023. ZeroEGGS:Zero-shotExample-basedGestureGenerationfrom Darrell.2024.PosePriorsfromLanguageModels.arxiv(2024).
Speech.InComputerGraphicsForum,Vol.42.WileyOnlineLibrary,206–216. GuyTevet,SigalRaab,BrianGordon,YonatanShafir,DanielCohen-Or,andAmitH
ShiryGinosar,AmirBar,GefenKohavi,CarolineChan,AndrewOwens,andJitendra Bermano.2022.Humanmotiondiffusionmodel.arXivpreprintarXiv:2209.14916
Malik.2019.Learningindividualstylesofconversationalgesture.InProceedingsof (2022).
theIEEE/CVFConferenceonComputerVisionandPatternRecognition.3497–3506. AdrienTreuille,SethCooper,andZoranPopović.2006.Continuumcrowds.(2006).
ChuanGuo,YuxuanMu,MuhammadGoharJaved,SenWang,andLiCheng.2024. JiajiaXie,ShengZhang,BeihaoXia,ZhuXiao,HongboJiang,SiwangZhou,Zheng
Momask:Generativemaskedmodelingof3dhumanmotions.InProceedingsofthe Qin,andHongyangChen.2024.Pedestriantrajectorypredictionbasedonsocial
IEEE/CVFConferenceonComputerVisionandPatternRecognition.1900–1910. interactionslearningwithrandomweights.IEEETransactionsonMultimedia26
Wei-NingHsu,BenjaminBolte,Yao-HungHubertTsai,KushalLakhotia,Ruslan (2024),7503–7515.
Salakhutdinov,andAbdelrahmanMohamed.2021.Hubert:Self-supervisedspeech JingYang,YuehaiChen,ShaoyiDu,BadongChen,andJoseCPrincipe.2024.IA-LSTM:
representationlearningbymaskedpredictionofhiddenunits.IEEE/ACMtransac- Interaction-awareLSTMforpedestriantrajectoryprediction.IEEEtransactionson
tionsonaudio,speech,andlanguageprocessing29(2021),3451–3460. cybernetics54,7(2024),3904–3917.
De-AnHuangandKrisMKitani.2014.Action-reaction:Forecastingthedynamicsof HongweiYi,HualinLiang,YifeiLiu,QiongCao,YandongWen,TimoBolkart,Dacheng
humaninteraction.InEuropeanConferenceonComputerVision(ECCV). Tao,andMichaelJBlack.2023.Generatingholistic3dhumanmotionfromspeech.In
BiaoJiang,XinChen,WenLiu,JingyiYu,GangYu,andTaoChen.2023.Motiongpt: ProceedingsoftheIEEE/CVFConferenceonComputerVisionandPatternRecognition.
Humanmotionasaforeignlanguage.AdvancesinNeuralInformationProcessing 469–480.
Systems36(2023),20067–20079. ZhentaoYu,ZixinYin,DeyuZhou,DuominWang,FinnWong,andBaoyuanWang.
HanbyulJoo,TomasSimon,MinaCikara,andYaserSheikh.2019. Towardssocial 2023.Talkingheadgenerationwithprobabilisticaudio-to-visualdiffusionpriors.In
artificialintelligence:Nonverbalsocialsignalpredictioninatriadicinteraction.In ProceedingsoftheIEEE/CVFInternationalConferenceonComputerVision.7645–7655.
ProceedingsoftheIEEE/CVFConferenceonComputerVisionandPatternRecognition. SiweiZhang,QianliMa,YanZhang,ZhiyinQian,TaeinKwon,MarcPollefeys,Federica
10873–10883. Bogo,andSiyuTang.2022.Egobody:Humanbodyshapeandmotionofinteracting
AdamKendon.1967. Somefunctionsofgaze-directioninsocialinteraction. Acta peoplefromhead-mounteddevices.InEuropeanconferenceoncomputervision.
psychologica26(1967),22–63. Springer,180–200.
AkioKodaira,TingboHou,JiHou,MasayoshiTomizuka,andYueZhao.2025.Streamdit: ZeyiZhang,TenglongAo,YuyaoZhang,QingzheGao,ChuanLin,BaoquanChen,
Real-timestreamingtext-to-videogeneration. arXivpreprintarXiv:2507.03745 andLibinLiu.2024. Semanticgesticulator:Semantics-awareco-speechgesture
(2025). synthesis.ACMTransactionsonGraphics(TOG)43,4(2024),1–17.
TarasKucherenko,PatrikJonell,SanneVanWaveren,GustavEjeHenter,SimonAlexan- ZeyiZhang,YanjuZhou,HeyuanYao,TenglongAo,XiaohangZhan,andLibinLiu.2025.
dersson,IolandaLeite,andHedvigKjellström.2020.Gesticulator:Aframeworkfor SocialAgent:MasteringDyadicNonverbalBehaviorGenerationviaConversational
semantically-awarespeech-drivengesturegeneration.InProceedingsofthe2020 LLMAgents.InSIGGRAPHAsia2025ConferencePapers(HongKong,China)(SA’25).
internationalconferenceonmultimodalinteraction.242–250. AssociationforComputingMachinery,NewYork,NY,USA,Article71,10pages.
GilwooLee,ZhiweiDeng,ShugaoMa,TakaakiShiratori,SiddharthaSSrinivasa,and doi:10.1145/3757377.3763879
YaserSheikh.2019.Talkingwithhands16.2m:Alarge-scaledatasetofsynchronized KaifengZhao,GenLi,andSiyuTang.2024.DartControl:Adiffusion-basedautore-
gressivemotionmodelforreal-timetext-drivenmotioncontrol. arXivpreprint

arXiv,2026, Ngetal.
A.2 TrainingDetails
arXiv:2410.05260(2024).
YihaoZhi,XiaodongCun,XuelinChen,XiShen,WenGuo,ShaoliHuang,and
Weprovideadditionaltraininghyperparametersanddetailsnot
ShenghuaGao.2023.LivelySpeaker:TowardsSemantic-AwareCo-SpeechGesture
Generation.InProceedingsoftheIEEE/CVFInternationalConferenceonComputer includedinthemaintext.
Vision(ICCV).20807–20817.
LeiZhong,YimingXie,VarunJampani,DeqingSun,andHuaizuJiang.2024.Smoodi: Optimization. WeusetheAdamWoptimizerwith𝛽 1 =0.9,𝛽 2 =
Stylizedmotiondiffusionmodel.InEuropeanConferenceonComputerVision. 0.999,andweightdecay1×10−4.Thelearningratefollowsalinear
Springer,405–421.
warmupoverthefirst1,000trainingsteps,peakingat1×10−4.The
VAEistrainedfor200Kiterationsbeforefreezing,afterwhichthe
flowmatchingmodelistrainedforanadditional300Kiterations.
A SupplementaryMaterial DataProcessing. Weusea80/10/10splitfortraining/validation/test.
Duringtraining,werandomlysampleafullsequencefromthetrain-
A.1 VideoResults
ingsetandfromthere,randomlysampleasubsequenceoflength
Pleasereferto5minutevideoforthissection. 𝑇 =400frames.Fortesttime,weuseaslidingwindowoflength
Westartwiththeproblemsetup(00:00–00:45)foradyadic 𝑇 =400andnooverlap.Weevaluateacrossthefullsetandgenerate
conversationbetweenauserandanagent.Giventheuser’s3D 2048sequencesintotal.
positionanddyadicaudio(frombothuserandagent),ourgoalisto Foraudiofeatures,weuseHuBERT-Large,whichisnotfully
generatespatially-aware3Dmotionfortheagentthatalignswith causal.Soattrainingtime,weessentiallydohavesomeinformation
theconversationandmovesaccordingtotheuser’s3Dposition. leakage.Inordertoensurethatitisfullycausalattesttime,weim-
Fromthegeneratedmotion,wecanthenrenderaphotorealistic plementthestreaminglogicsuchthatweneverpassintoHuBERT
avatar.Ourmodelislightweightandfastenoughtoenablestreaming, anyfutureframestoavoidthisleakage.Instead,wealwaysimple-
allowingreal-timeinteractionwiththeAIagentonVRplatforms. mentaslidingwindowlogicwherewepassinthecurrentcontext
Thestreamedresults(00:46–01:25)demonstratethatourmodel andthentheprevious𝑇 −𝑠 frames.Wefindthatshiftingtothis
produces conversationally-appropriate gestures while naturally fullycausalapproachattesttimedoesnotdegradeperformance.
turningtowardtheusertosignalsocialengagement.Theagent
seamlesslytransitionsbetweenspeakingandlisteningmodes,main- LatentDimension. TheVAElatentdimensionis𝐷 𝑧 =256.With
tainingdyanamicgestureswhenspeaking,andengagedidleges-
stride𝑠 =4andsequencelength𝑇 =400,thisproduces𝐾 =100
tureswhenlistening. latenttokenspersequence.
Ourmethodgeneralizesacrossdiverseemotionalcontexts,pro-
A.3 InferenceDetails
ducingcontextually-appropriatebodylanguage:handsonhipsand
lookingdownwhenstressedorrejected(01:26–02:00),livelyges- StreamingProtocol. Forreal-timedeployment,wegeneratemo-
tureswhenexcited(02:01–02:26),clenchedfistswhenangry(02:27 tioninchunksof𝑠 =4frames.Wethenkeepthelast2tokensand
–02:41),andexaggeratedbowingincelebratoryagreement(02:41– thenremoveallthepriorones.Inessence,wegenerateatotalof8
02:57). framesatatime.Asdiscussedinthemaintext(),weinpaintthe
Toensurethatourmodeliscontrollablewhenitcomestogaze historyframestomaintaintemporalconsistency.Foreachchunk,
preferences,wealsoincludeagazescorewhichwecantuneattest werunusingmidpointsolverwith4iterations(8nfesteps).Inthis
time.Forlowergazescores,theagentavoidsdirectfacingtheuser. setting,weareabletoachieve60fpsattesttime,whichallowsus
Fortheexactsameinputconditioning,increasingthegazescore toachievereal-timestreamingperformance.
resultsinmoredirectfacing(02:58–03:21).Whenwefullydrop
PhotorealisticRendering. Wefollow[Bagautdinovetal.2021],a
outthegazescore(𝑔=0),theagent’sgazejustfollowswhateveris
learningbasedmethod,torenderphotorealisticavatarsfromthe
in-distributionwiththetrainingdataset(03:22–03:38).
generatedjointparametermotions.Themodeltakesasinputone
Wealsocompareagainstexistingmethods.ComparedtoMDM
frameoffacialexpression,oneframeofbodypose,andaview-
[Tevetetal.2022]ourmethodproducesconsiderablymorelively
pointdirection.Weuseanofftheshelfmethodtogeneratefacial
gestures(03:39–03:52).ComparedtoAudio2Photoreal[Ngetal.
expressionparametersfromspeechaudio.Themodelthenoutputs
2024],ourmethodproducesmorerealisticmotion(03:53–04:07).
aregisteredgeometryandviewdependenttexture,whichisused
ForAudio2Photoreal,itseemsasiftheVQwillpredictslightly
tosynthesizeimagesviarasterization.Forfurtherdetails,please
delayedmotionwhichforcesthediffusionsidetocatchupwith,
referto[Bagautdinovetal.2021].
whichresultsindistoredmotion.ComparedtoTalkSHOW[Yietal.
2023],ourmethodproduceslessmotionartifactssincewepredict
the full-body motion in a single model (04:08 – 04:22). Instead,
TalkSHOW’sVQ-basedapproachresultsindistoredwristmotion
artifactsandamplefootsliding.
Thereal-timenatureofourmodelenablesfullyinteractiveAI
agentsinVR(04:23–end).Wegeneratedyadicconversationsusing
off-the-shelfLLMspairedwithtext-to-speechmodels—here,Chat-
GPTfordialogueandKyutaiforspeechsynthesis.Thisenables
applicationsrangingfromentertainment(e.g.,gamingNPCs)to
personalassistants.
