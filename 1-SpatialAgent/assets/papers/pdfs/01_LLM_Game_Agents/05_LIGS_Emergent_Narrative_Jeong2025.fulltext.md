Title: Modeling Asteroseismic Yields for the Roman Galactic Bulge Time-Domain Survey

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/papers/pdfs/01_LLM_Game_Agents/05_LIGS_Emergent_Narrative_Jeong2025.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T03:06:32+00:00
- page_count: 17
- status: ok
- text_char_count: 62745

Metadata:
- author: Trevor J. Weiss; Noah J. Downing; Marc H. Pinsonneault; Joel C. Zinn; Dennis Stello; Timothy R. Bedding; Kaili Cao; Marc Hon; Claudia Reyes; B. Scott Gaudi; Robert F. Wilson; Daniel Huber; Sanjib Sharma
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Introduction (page 1)
  - Background on Asteroseismology (page 2)
  - Background on Roman/GBTDS (page 3)
  - Predicting Roman Asteroseismic Yields (page 3)
- Simulated Light Curves and Detection Probabilities (page 3)
  - Simulated Light Curves (page 3)
    - Amplitude Adjustment (page 4)
    - Photometric Noise (page 4)
  - Calculating Signal-to-Noise Ratio and Detection Probability (page 4)
  - Detection Probability Results (page 5)
- Asteroseismic Yields (page 9)
  - Stellar Population Model (page 9)
  - Survey Parameters (page 10)
  - Asteroseismic Detection (page 10)
  - Detection Results (page 11)
- Discussion (page 11)
  - Noise Modeling (page 11)
  - Roman Parameters (page 11)
  - Extinction (page 12)
  - Sample Characteristics (page 12)
- Conclusion (page 14)

Markdown Content:

5202
luJ
1
]RS.hp-ortsa[
3v99940.3052:viXra
Draft version July 3, 2025
TypesetusingLATEXtwocolumnstyleinAASTeX631
Modeling Asteroseismic Yields for the Roman Galactic Bulge Time-Domain Survey
Trevor J. Weiss†,1 Noah J. Downing†,2 Marc H. Pinsonneault,2 Joel C. Zinn,1 Dennis Stello,3
Timothy R. Bedding,4 Kaili Cao,5,6 Marc Hon,7 Claudia Reyes,8 B. Scott Gaudi,2 Robert F. Wilson,9,10
Daniel Huber,11,4 and Sanjib Sharma12
1Department of Physics and Astronomy, California State University, Long Beach, Long Beach, CA 90840, USA
2Department of Astronomy, The Ohio State University, Columbus, OH 43210, USA
3School of Physics, University of New South Wales, NSW 2052, Australia
4Sydney Institute for Astronomy (SIfA), School of Physics, University of Sydney, NSW 2006, Australia
5Center for Cosmology and AstroParticle Physics (CCAPP), The Ohio State University, 191 West Woodruff Ave, Columbus, OH 43210,
USA
6Department of Physics, The Ohio State University, 191 West Woodruff Ave, Columbus, OH 43210, USA
7Kavli Institute for Astrophysics and Space Research, Massachusetts Institute of Technology, Cambridge, MA 02139, USA
8Research School of Astronomy & Astrophysics, Australian National University, Canberra ACT 2611, Australia
9Department of Astronomy, University of Maryland, College Park, MD 20742, USA
10NASA Goddard Space Flight Center, Greenbelt, MD 20771, USA
11Institute for Astronomy, University of Hawai’i, 2680 Woodlawn Drive, Honolulu, HI 96822, USA
12Space Telescope Science Institute, 3700 San Martin Drive, Baltimore, MD 21218, USA
ABSTRACT
The Galactic Bulge Time-Domain Survey (GBTDS) of the Roman Space Telescope will take high-
cadence data of the Galactic bulge. We investigate the asteroseismic potential of this survey for red
giants. We simulate the detectability of global asteroseismic frequencies, ν and ∆ν, by modify-
max
ing Kepler data to match nominal GBTDS observing strategies, considering different noise models,
observingcadences, anddetectionalgorithms. Ourbaselinecase, usingconservativeassumptions, con-
sistently leads to asteroseismic ν detection probabilities above 80% for red clump and red giant
max
branch stars brighter than 16th magnitude in Roman’s F146 filter. We then inject these detection
probabilities into a Galaxia model of the bulge to estimate asteroseismic yields. For our nominal case,
wedetect290,000starsintotal,with185,000detectionsinthebulge. Differentassumptionsgivebulge
yields from 135,000 to 349,000 stars. For stars with measured ν , we find that we can recover ∆ν
max
in 21% to 42% of red clump stars, and 69% to 92% of RGB stars. The expected yield and stellar pa-
rameterprecisionwepredictforRomanasteroseismologypromisetocharacterizeplanet-hostingstellar
populations and to resolve questions regarding the formation history of the bulge.
Keywords: Galactic bulge(2041)—Asteroseismology(73) — Stellar ages(1581)
1. INTRODUCTION stellar populations (Miglio et al. 2013; Silva-Aguirre
et al. 2015; Pinsonneault et al. 2018). Asteroseismic
Time-domain space photometry missions enable a
data can also be used as a training set to infer ages for
broad range of science, frequently involving topics quite
much larger data sets (Martig et al. 2016; Ness et al.
distinct from the main mission goals. The Kepler
2016; MacKereth et al. 2019). However, these indirect
Mission, for example, was designed to study transit-
techniques struggle to recover ages for the oldest stars
ing exoplanets (Borucki et al. 1997, 2010), but has
and for those not in the training set (Ting & Rix 2019;
proved extremely valuable for studying stellar oscilla-
Ciuc˘a et al. 2021; Leung et al. 2023). Therefore, it is
tions (Gilliland et al. 2010; Kurtz 2022).
highly desirable to obtain more asteroseismic data out-
The study of stellar oscillations—asteroseismology—
side of the solar neighborhood to study stellar popula-
canbeusedtoinferstellarmass,radius,andageforlarge
tions across the Galaxy.
The Nancy Grace Roman Space Telescope’s Galactic
1 † Firstco-authorship. bulge Time-Domain Survey (GBTDS) is one of three

2
Core Community Surveys using the Wide Field Instru- define selection/completeness functions for the Roman
ment. Its primary purpose is to detect planets through asteroseismic sample.
microlensing (Penny et al. 2019, Spergel et al. 2015). The remainder of this section discusses the science
However,highqualityandrapidcadenceofthephotom- and background of using asteroseismology with Roman
etry will also enable detections of solar-like oscillations, under differing assumptions for its photometric perfor-
making Roman uniquely suited to advancing Galactic mance. Section 2 describes our methodology for simu-
science. Roman will yield catalogs of asteroseismic stel- lating asteroseismic detections. Section 3 describes our
lar parameters for the Galactic bulge, offering insights methodology for modeling yields and populations. In
that will impact a wide range of astrophysical fields Section4,wediscussthedifferentyieldsandthecharac-
(Gould et al. 2015, Huber et al. 2023, hereafter G15 teristics of our simulated sample. Section 5 summarizes
and H23, respectively). our results and discusses next steps for the project.
The GBTDS will enable the detection of oscillations
in red giant branch (RGB) and red clump (RC) stars in 1.1. Background on Asteroseismology
the densely populated Galactic bulge, providing crucial For solar-like oscillators, turbulence near the stellar
insights intotheunderlying stellarpopulations. Astero- surface creates standing wave patterns within the en-
seismologyallowsfortheprecisedeterminationsofmass, tire star at characteristic frequencies that depend sen-
radius,andageinevolvedstars(Chaplin&Miglio2013; sitively on mass and radius. When large numbers of
Jackiewicz 2021), making it a powerful tool for address- stars are involved, it is conventional to use two charac-
inglong-standingquestionsaboutthebulge’sformation teristic frequencies to measure stellar parameters in a
and evolution. In particular, recent studies have sug- process known as “global asteroseismology”. We char-
gested the presence of a young stellar population in the acterize the observed pattern with a frequency of max-
bulge (see, e.g., Bensby et al. 2017; Joyce et al. 2023), imum power, ν , and the frequency spacing between
max
a hypothesis that asteroseimic age measurements could modes with the same spherical harmonic degree ℓ, ∆ν.
directly test. Theformerisrelatedtothesurfacegravity(Brownetal.
Red giants oscillate on timescales of hours to days, 1991; Kjeldsen & Bedding 1995; Belkacem et al. 2011;
with amplitudes sufficient for detections at large dis- Hekker 2020) and the latter is related to the mean den-
tances (Miglio et al. 2021; Hey et al. 2023). The central sity (Ulrich 1986); they can therefore be combined to
Milky Way is known to contain significant populations infermassandradius(Stelloetal.2008;Kallingeretal.
of RC stars (Girardi 2016; Ness & Lang 2016; Abbott 2010):
et al. 2017), making the bulge an ideal target for as-
teroseismic studies. In addition to resolving the age R (cid:18) ν (cid:19)(cid:18) ∆ν (cid:19)−2(cid:18) T (cid:19)1/2
= f max f eff
distribution of the bulge, asteroseismic constraints on R νmaxν ∆ν∆ν T
⊙ max,⊙ ⊙ eff,⊙
helium abundance, which is otherwise difficult to dis- (1)
entangle from age effects (e.g., Nataf 2015), and radial M (cid:18) ν (cid:19)3(cid:18) ∆ν (cid:19)−4(cid:18) T (cid:19)3/2
= f max f eff
abundance gradients (e.g., Hayden et al. 2015) could M νmaxν ∆ν∆ν T
⊙ max,⊙ ⊙ eff,⊙
refine models of chemical evolution. Moreover, as one (2)
of the GBTDS’s primary science goals is the detection With an independent radius measurement one can in-
ofmicrolensedexoplanets,asteroseismologywillprovide stead infer mass using either of the following equations
hoststarages,offeringvaluableconstraintsonplanetary (Ash et al. 2025):
evolution models (e.g. Berger et al. 2020; David et al.
2021). M (cid:18) ∆ν (cid:19)2(cid:18) R (cid:19)3
= f (3)
Aprimarygoalofthisworkistoidentifywhichstellar M ∆ν∆ν R
⊙ ⊙ ⊙
populations in the bulge are detectable with asteroseis-
mology for use in constructing an asteroseismic target M (cid:18) ν (cid:19)(cid:18) T (cid:19)1/2(cid:18) R (cid:19)2
= f max eff (4)
list. Given the ∼ 100 million unique bulge stars ex- M νmaxν T R
⊙ max,⊙ eff,⊙ ⊙
pectedtobeobservedwithRoman(Wilsonetal.2023),
We include the correction factors f and f : f
an asteroseismic target list conditioned on the stellar νmax ∆ν νmax
is an empirical correction based on calibration to Gaia
colors and magnitudes accessible to asteroseismology
radii and f is computed theoretically from stellar
will be important to reduce the false positive rate and ∆ν
models(Whiteetal.2011;Sharmaetal.2016);bothcor-
conserve computational resources. As discussed in Sec-
rection factors deviate from unity at the percent level.
tion5,sciencewiththissamplewillalsobenefitfromthe
NotethatthecorrectionfactorsasusedhereandbyPin-
stellarpopulationsimulationsdescribedhereinorderto
sonneault et al. (2025) are the inverse of the correction

3
factors as defined by White et al. (2011); Sharma et al. 1.3. Predicting Roman Asteroseismic Yields
(2016); Li et al. (2023). To be able to determine stellar
This work expands on G15 and H23, which both pro-
age, a mass may be derived from either of the above
vided preliminary simulations of asteroseismic detec-
scalingrelations—inbothcases,themassestimatecan
tionsandpopulationyieldsfortheGBTDS.Suchstudies
beusedtoperformastellaragelookupusingstellarevo-
areessentialfordevelopingpotentialtargetlistsandun-
lutionary tracks evaluated at a given temperature and
derstandingtheselectionfunctionsofthesample,which
metallicity.
will be the focus of future work. However, they were
Asteroseismology has been revolutionized by space-
both limited in scope. G15 employed a semi-analytic
based time domain missions like CoRoT, Kepler/K2,
noisemodelappliedtoonlyafewindividualstars(rather
and TESS, which have measured precise masses, radii,
than a larger, statistically significant sample), demon-
andagesforthousandsofstars. However,thesemissions
stratingthatasteroseismologymaybepossiblewithRo-
did not observe the bulge. The exception is K2 Cam-
man, but requiring more detailed simulations. H23 ex-
paign 9, but Kepler’s large pixels meant the field was
pandedonthisbyexploringcadencevariationsandmore
too crowded to deliver sufficiently precise light curves
sophisticated models for source counts, but it still used
forindividualstars. Therehasbeenworkdonetostudy
the semi-analytic detection model from G15.
the bulge with ground-based surveys (e.g., Soszyn´ski
This work expands on G15 and H23 by sampling a
et al. 2013; Hey et al. 2023), but it was restricted to
wider range of stellar parameter space and considering
themostluminousredgiants(theso-calledsemi-regular
updatednoisemodels,asdescribedbelow. Insimulating
variables). We explore here the degree to which the
light curves, we used Roman’s F146 filter instead of the
GBTDS will be able to measure the two global astero-
2MASSH-bandapproximationusedinG15. Weutilized
seismic frequencies.
dust maps to simulate realistic interstellar dust in the
GBTDS fields and generated synthetic stellar popula-
tions under various survey strategies. We also reckoned
1.2. Background on Roman/GBTDS the final detection counts using an SNR-based method,
as well as an empirical approach. This provided a holis-
NASA’s next flagship mission, the Nancy Grace Ro-
ticsampleofexpectedasteroseismicyieldsforbothν
man Space Telescope, will begin taking science obser- max
and ∆ν given a range of choice for extinction, field se-
vations in 2027 using two instruments: a wide field im-
lection,noiseproperties,anddetectionmethod,building
ager and a coronagraph. The Wide Field Instrument
has an effective field of view of 0.281 deg2 and a plate on and expanding the work of G15 and H23.
scale of 0.11”/pixel. With its Wide Field Instrument,
2. SIMULATED LIGHT CURVES AND
infrared optics and seven filters, Roman will be able to
DETECTION PROBABILITIES
take high-resolution, red-optical to near-IR images with
2.1. Simulated Light Curves
roughly 100 times the FOV of Hubble in one pointing
(Spergel et al. 2015). The GBTDS will have 6 observ- Our approach is modeled on that of G15, with up-
ing seasons of up to ≈ 72 days in length, for a total of dated information on the properties of the GBTDS. We
≈432daysofobservationsspreadovera5yearmission. used Kepler light curves as the basis for the asteroseis-
Each field will be observed at approximately 15-minute mic signals. To do so, we selected 100 RC stars and
cadence but the exact value is yet to be decided, so we 100 RGB stars from the APOKASC-3 Catalog (Pinson-
explore yields given two different cadence scenarios. neault et al. 2025) Gold sample spanning ν values
max
The primary goal of the GBTDS is quality imaging from ∼ 3 µHz to ∼ 110 µHz to form a representative
and data collection of the Galactic bulge, a population sample for our simulations. We generated two rank-
forwhichitisdifficulttoestimateprecisestellarmasses ordered lists in ν and uniformly sampled the dis-
max
andagesduetohighextinctionandcrowdedfields(e.g., tributions to choose our targets, restricting the list to
Stanek et al. 1997). Kepler sampled relatively nearby targets with a full set (18 quarters) of Kepler data. We
stars, K2wasrestrictedtotheeclipticplane, and, while downloaded Kepler light curves for each star through
TESS surveys the entire sky, it is much shallower. The the lightkurve (LightkurveCollaboration 2018) pack-
bulge will likewise not be accessible to the upcoming age. Wethen(1)spliteachKepler lightcurveintothree
PLAnetary Transits and Oscillations of stars (PLATO) 450-day sections, so each would follow the full duration
mission (Nascimbeni et al. 2022). The GBTDS will of the GBTDS; (2) adjusted the amplitude of oscilla-
therefore provide the deepest look into the Galaxy to tions to account for the change between Kepler’s band-
date and will provide the only survey of the bulge at pass and Roman’s F146 wide-filter (Lund 2019; Sreeni-
such high cadence. vas et al. 2025); and (3) injected realistic photometric

4
noise from two different noise models, adjusting for the Weinjectednoiseintooursimulatedlightcurvesusing
two assumed cadences (7.5-minute and 15-minute). both the Wilson and Penny models through the follow-
ing modified version of equation 19 of G15:
2.1.1. Amplitude Adjustment
(cid:18) (cid:19)
σ
To make the amplitude adjustment we used the tool F =(F −F )A +N 0,√ , (6)
F146,i Kp,i Kp F146/Kp
Gadfly (Morris & Huber in prep), which can gener- 2
ate synthetic power spectra by scaling the solar power
where F is the ith observed Kepler flux measure-
Kp,i
spectrum given input stellar parameters. In particu-
ment,F isthemeanoftheKepler fluxmeasurements,
Kp
lar, we utilized the amplitude with wavelength func-
A is the amplitude ratio defined in equation 5,
tion, which determines the amplitude ratio by inte- F146/Kp
and N(x,y) is a Gaussian random variable with mean
grating a black body spectrum at a given T over
eff x and variance y2. We injected noise through the σ
a specified filter and the SOHO VIRGO PMO6 filter.
term of equation 6, where σ is the noise amplitude of
We obtained an amplitude ratio A by divid-
F146/Kp a given noise model pictured in Figure 1. We included
ing A by A which are given by the √
F146/PM06 Kp/PM06 the 2reductiontophotometricnoiseinequation19of
amplitude with wavelength function over a range of
G15 because the GBTDS will have a nominal cadence
temperatures. The amplitude ratio of the F146 filter
of 15 minutes – half of Kepler’s. This reduction reflects
over the Kepler Kp-band as a function of temperature
theshorterintegrationtimeperexposure,whichreduces
is described by the following equation:
the variance of random noise. We further reduced the
√
A =0.493+0.058(T )+0.018(T )2, (5) photometric noise by an additional factor of 2 to sim-
F146/Kp 5000 5000
ulate a two times faster sampling strategy (7.5-minute
where T ≡ T /5000 K. This relationship ranges cadence).
5000 eff
between A /A ≈ 0.540 and A /A ≈ 0.575 In Figure 2 we plot a representative set of Fourier
F146 Kp F146 Kp
over T ranging from 3500 K to 5500 K. power spectra of the simulated light curves. The low-
eff
luminosity RGB spectrum (top row) is challenging to
2.1.2. Photometric Noise detect across all noise models, while the more luminous
The photon noise floor for the selected Kepler obser- RGBandRCspectra(bottomtworows)areclearlyseen
vations is significantly lower than that of the noise floor inallcases. Thelower-luminosityRCspectrum(second
projected for Roman, so the noise in the Kepler light row) is located closer to the noise floor. The RC is the
curves can be neglected. We used two models to inject main target population, so we can draw two immediate
noise at the expected level for Roman into the Kepler conclusions from this exercise: at least some RC stars
lightcurves. Poissonnoisedominatesforfainterstarsin should be detectable, and the yields will be sensitive
both,butthefirstmodelfromPennyetal.(2019)(here- to the noise properties. Fortunately, more luminous RC
after referred to as the Penny model) assumed a noise stars(ν max ∼25−30µHz)areconsistentlydetectableby
floor of ∼1mmag for saturated stars. The second model eye. It is also seen that a faster cadence can make the
(Wilson et al. 2023, hereafter referred to as the Wilson oscillation signals more clear. Precise detection prob-
model) assumed we can recover more information from abilities and yields are discussed in more quantitative
saturated stars. The Wilson model was computed by detail in the following sections.
simulating a series of small image cutouts and extract-
2.2. Calculating Signal-to-Noise Ratio and Detection
ingtheuncertaintyfromeachepochofPSFphotometry.
Probability
The instrument model used to create these simulations
utilizes ramp-fitting, but ignores several detector effects Asteroseismology relies on the measurement of ν
max
thatarelikelytodegradethequalityofobservationsfor and ∆ν to determine stellar parameters as discussed in
stars with brightnesses of F146 < 15–16, such as non- Section 1. Stellar mass can be determined with just
linearities and charge leakage. As a result, the Wilson ν or just ∆ν if there is an independent radius mea-
max
model is akin to assuming that such effects can be pre- surement. If both are available, an independent radius
cisely calibrated, which would lead to the photometric is not required. With a noise floor close to the oscil-
noise per pixel being capped at just under the Poisson lation signals, it is important to quantify our ability to
limit at full well depth. We compare the noise models measureν and∆ν,becauseitisnotimmediatelyap-
max
in Figure 1. They diverge brighter than magnitude 16, parent we will detect oscillations in most cases. In this
which is important for our simulations because there is sectionweoutlinehowwedeterminedetectionprobabil-
a large population of bulge giants in the 12–15 F146 ities of ν using two methods and how we determine
max
magnitude range. detections of ∆ν in our simulations.

5
where y is defined as
y =(1+SNR )/(1+SNR ), (10)
thresh tot
Γ is the gamma function, and SNR is determined us-
tot
ing Equation 7. This gives us a probability of detect-
ing solar-like oscillations. In Figure 3 we visualize the
detection probabilities from the Chaplin method using
the ν -magnitude diagram introduced by Stello et al.
max
(2017).
We also calculated detection probabilities using a
pipeline (hereafter referred to as the Hon pipeline) in
which oscillations are detected from images of power
spectraplottedinlog-logspaceusingconvolutionalneu-
ral network classifiers as described in Hon et al. (2018).
Figure 1. Noise models of the simulations. The red curve
The classifiers used are similar to that from Hon et al.
shows the Penny noise model, which has a 1 mmag noise
(2019), in which 4-year Kepler power spectra were used
floor. The black points show the Wilson noise model, which
as a training set. Compared to the Chaplin method,
is based on simulations of saturated star photometry with
Roman. The dot-dash orange line shows the noise model which is a strictly statistical criterion, the Hon pipeline
described by equation 18 of G15. reproducesthedetectioncriteriaofthetrainedeye. The
classifiersdirectlyidentifywhetherthepowerexcesscan
Our first method (hereafter referred to as the Chap- be detected from observed power spectra. Detection
lin method) computes the signal-to-noise based on the probabilities using the Hon pipeline are visualized in
height of the oscillation power excess above the back- Figure 3.
ground (Chaplin et al. 2011). Because the method by Hon et al. (2019) only gives
Signal-to-Noise ratios (SNRs) were calculated using the probability of detecting ν max we also ran the SYD
the following steps. First we smoothed a given power pipeline (Huber et al. 2009) to obtain measurements of
spectrum using a Gaussian filter of width equal to ∆ν. ∆ν, which we vetted using the automated method by
Then we inserted a ±4∆ν gap into the smoothed curve Reyes et al. (2022). Detections of ∆ν are visualized in
aroundν andfittedthegapwithastraightlineinlog- Figure 4.
max
spacetoremovetheoscillationsignalfromthesmoothed
2.3. Detection Probability Results
spectrum. Since the smoothed spectrum then contains
onlythegranulationpowerandwhitenoise,wecalculate In Figure 3 we can see the differences in detection
the SNR using the following equation probabilities between the Chaplin method and the Hon
pipeline,aswellashowcadenceimpactsthoseprobabil-
SNR= 1 (cid:88) N P i −n i (7) ities.
N n The Chaplin method is always more optimistic than
i
i=1
the Hon pipeline, but they both agree that ν should
max
where N is the number of frequency bins in the power be detected in bright RGB and RC stars. This is ex-
spectrum, P is the raw power spectrum, and n is the pected, since the amplitudes drop in less luminous gi-
smoothed oscillation-free spectrum. We require that ants, making yields there more sensitive to noise prop-
the observed SNR is greater than a SNR threshold, erties. RC stars also have lower amplitude modes com-
SNR thresh , defined using a fractional false-alarm prob- paredtoRGBstars,explainingthedifferenceinν max de-
ability of p=0.01 which corresponds to the equation tectionlimits. TheHonpipelineshowsthatsignalsmay
be harder to recover in faint stars than what the formal
P(SNR′ ≥SNR ,N)=p, (8) Chaplin SNR calculation suggests. The Hon method
thresh
also shows that luminous giants may be harder to re-
where SNR′ is an arbitrary SNR and N is the number cover than the Chaplin method predicts. A decrease in
of frequency bins within ±3∆ν around ν max . Then the the detection probabilities near ν max ∼ 10µuHz is a fea-
probability that an observed SNR, SNR tot , is greater turepreviouslyseeninthismachinelearningHondetec-
than SNR thresh is given by tion method (Hon et al. 2021), which does not perform
(cid:90) ∞ exp(−y′) as well for luminous stars. Were this gap not present,
P = y′(N−1)dy′ (9) the yields would be larger by ≈ 1%, which is compara-
final Γ(N)
y

6
Figure 2. Power spectra of Kepler observations and GBTDS simulations as follows (from left to right): Kepler 30 minute
cadence, Wilson model 7.5 minute cadence, Wilson model 15 minute cadence, Penny model 7.5 minute cadence, and Penny
model 15 minute cadence. Each Kepler star used for the simulations is labeled with their respective Kepler Input Catalog
(Brownetal.2011;STScI2011)number(KIC)inthelegendsoftheleft-mostcolumn. Fromtoptobottomthesestarsrepresent
thefollowingcases: low-luminosityRGB(KIC6034166),low-luminosityRC(KIC6465610),high-luminosityRC(KIC10468528,
and high-luminosity RGB (KIC 2695975). The simulated power spectra were all generated at magnitude 15 in the F146 filter.
ThecoloredpowerspectraaresmoothedusingaGaussianfilterofwidth0.001µHzandtheblacklineshowsthepowerspectra
smoothed with a width of 1 µHz. The dashed line shows the measured ν for each star in APOKASC3 (Pinsonneault et al.
max
2025).
ble to variations in yield estimates due to choice in in- RGB, allowing for more detections. Because the Hon
terpolation methods. Although more noticeable in the method is more conservative overall, we adopt it as our
Chaplin detection probabilities, both show a diagonal, model for detecting ν .
max
ν andmagnitude-dependentcutoffindetectionsthat In Figure 4 we show the probability of detecting ∆ν
max
reflectsthecombinedeffectsof(1)decreasingamplitude in the stars, given a detection of ν . The sharp drop
max
of oscillation with increasing ν and (2) increasing in probability in the lower right corner of the plots in
max
noise with increasing magnitude. In both methods, im- thebottomrowofFigure4occursbecausetherewereno
plementing a faster sampling speed increases detection starswithadetectedν inthoseregions,soweinputa
max
probabilities at faint magnitudes for both the RC and ∆ν detection probability of zero. This is also why there

7
Figure 3. Probability of detection of oscillations as a function of ν and H magnitude for different methods and cadences.
max
ThetoptworowsshowresultsusingtheChaplinmethod;thebottomtworowsshowresultsfromtheHonmethod. Ineachpair,
the left panel corresponds to a 7.5-minute cadence and the right to a 15-minute cadence. RC (red clump) stars and RGB (red
giant branch) stars are shown separately. Brighter regions indicate a higher probability of detection. ν values are adopted
max
from APOKASC-3. Individual points represent simulated stars, not Galaxia-generated stars discussed elsewhere. The Hon
method exhibits limited detection beyond H ≈ 20, reflected in the different detection limits between methods.
are no ∆ν detections for magnitudes greater than 17 in they have smaller oscillation amplitudes, which com-
RGBstarsat15-minutecadence. Wefindthattheprob- pounds this issue. Mixed modes are also present in RC
ability of detecting ∆ν is largely independent of mag- stars, which can explain the relatively small ∆ν detec-
nitude for both the RC and RGB samples, except for a tion fractions we see in that population. Mixed mode
dropnearthefaintedgeofν detections. Wedo,how- coupling strengths are several times larger in RC stars
max
ever,seeaclear∆ν detectiondependenceonν . This thanintheRGBsamplethathaveν detectionsinour
max max
is because high ν RGB stars exhibit mixed modes sample;thisresultsinmorepronouncedmixed-modeap-
max
making ∆ν harder to measure (Stello et al. 2013) and pearancesinthefrequencyspectraforRCstars(Mosser

8
Figure4. Probabilityof∆ν detectionofthenominalcase,plottedonν andHmag,usingtheSYDpipeline. ν valuesare
max max
adoptedfromAPOKASC-3. Thebrightertheregion,themorelikely∆ν isdetectedgivenν andHmag,andthedarkerthe
max
region,thelesslikely∆ν isdetected. Notethatthevisiblepointsrepresentindividualsimulatedstars,notthestarsgeneratedby
Galaxiaasdiscussedinlatersections. The1Dhistogramshowstheexpectedrecoveryfractionsassumingauniformdistribution
in magnitude.
et al. 2017). Coupling strengths are also large at the in those bins due to the difficulty of estimating ν at
max
base of the RGB, but these stars are inaccessible to Ro- lower frequencies. Note that the majority of the RC de-
manν detection. RCstarsalsogenerallyhaveoverall tections are found in power-to-background ratios that
max
loweroscillationamplitudes(forthesameν ;Yuetal. are less than 0.5, and so do not occupy the same dy-
max
2018), leading to a more difficult interpretation of the namicrangeofpower-to-backgroundratioasRGBstars
powerspectra,whichthenlowers∆νdetections. Asseen in Figure 5.
in the histograms of Figure 4, a higher cadence leads to We use these deviations from ‘truth’ to infer the
higher ∆ν detection probabilities in regions where ∆ν expected measurement uncertainty using an outlier-
was already detected, as well as new detections at high insensitive median absolute deviation,
ν where ∆ν was not detected with lower cadence.
max (cid:104) (cid:16)(cid:12) (cid:12)(cid:17)(cid:105)
This faster cadence affects the signal-to-noise ratio of σ = median (cid:12)X −X˜(cid:12) ∗1.4826, (11)
(cid:12) i (cid:12)
our objects, increasing the number of detections. The
maximum ∆ν detection fractions, ranging from 21% for where X˜ is the median of the sample, X is a sample
i
RC stars and 90% for RGB stars with a 15-minute ca- point, and the constant is a scaling factor. Typical un-
dence, are comparable, and even surpass 1-2 sectors of certaintiesforRGBstarsatpower-to-backgroundratios
TESS data (Stello et al. 2022). This is expected given of 0.5 are 3.7% for ν and 0.74% for ∆ν. RC star
max
the longer time series of our Roman GBTDS simula- uncertainties are better for ν at 1.9%, but slightly
max
tions, leading to higher frequency resolution and sam- worsen for ∆ν at 1.0%.
pling of more oscillation cycles. For select figures in We expect approximately 30% of the Roman astero-
this paper (e.g., Figures 6 and 15), a 1% uncertainty seismic yield will have both a ∆ν and a ν detection,
max
was added to the results purely for visual clarity. This showninFigure6. Inthiscase,massescanbecomputed
smoothing does not affect the underlying data or alter directly via the standard asteroseismic scaling relation
any scientific findings. (refer to Equation 2). We note that metallicity and
Figure 5 shows the distribution of the fractional devi- T are still required to interpret the frequency spac-
eff
ation in recovered ν and ∆ν as a function of power- ings and to obtain mass, radius, and age. Given the
max
to-background ratio, which essentially is another means typical uncertainties of ν and ∆ν we find, the mass
max
ofasignal-to-noiseratiobutusingcalculationsbasedon uncertainty would be 5.7% for RC and 8.1% for RGB,
the Chaplin method. Many of our low ν objects in implying age uncertainties of approximately 17% and
max
Figure5lieinhigherpower-to-backgroundratioregions, 25% respectively, assuming negligible temperature un-
and can be seen heavily skewing our RGB uncertainties certainties (e.g., 1%). With the remaining objects that

9
0.10
0.05
0.00
0.05
0.10
0.0 0.5 1.0 1.5 2.0 2.5
Power-to-Background Ratio
eurt
/)eurt
sbo
(
RC : 0.010
RGB : 0.0074 0.10
0.05
0.00
0.05
0.10
0.0 0.5 1.0 1.5 2.0 2.5
Power-to-Background Ratio
eurt,xam
/)eurt,xam
sbo,xam
(
RC max: 0.019
RGB max: 0.037
Figure 5. Left: Fractional deviation of observed ∆ν relative to the ‘true’ APOKASC-3 value, as a function of power-to-
background ratio, for RC and RGB stars. Error bars are the uncertainties taken from bins, measured by using the median
absolute deviation. The uncertainty value used, shown in the legend for RC and RGB, is taken from the bin closest to 0.5 for
both cases. Right: Same as the left panel, but instead with observed ν relative to the ‘true’ APOKASC-3 value.
max
104
103
102
101
100
0 1 2 3 4 5 6
Mass [M ]
niB
rep
sratS
fo
#
tobelessprecisethanthesub-microarcsecondlevelthat
was predicted by Gould et al. 2015.
Combining the radius with a surface gravity from the
M max+ : 31.5%
ν scalingrelationthenyieldsamass, showninequa-
M max+ : 68.5%
ti
m
o
a
n
x
4. For a temperature uncertainty of 1%, the re-
sulting masses would have a ∼4.5% uncertainty due to
temperaturealone. Withtypicalν precisionsof2.9%
max
for the RC, the mass uncertainty comes to ∼5.4%. For
this reason, we expect it will be more advantageous to
calculate asteroseismic ages with this mass scale, which
would deliver statistical uncertainties in age of closer to
15% instead of the above-reported 25% with asteroseis-
mologyalone. Notethatthisdoesnotincludeuncertain-
tiesduetochemicalcompositionorstellarmodelchoice,
Figure 6. The dark blue histogram shows the distribution
of stellar masses for stars which will have detctions in both the latter of which can be particularly significant (e.g.
∆νandν . WhencombinedwithanestimateofT ,these Tayar et al. 2022).
max eff
stars will have inferred stellar masses and radii. The green
3. ASTEROSEISMIC YIELDS
histrogramshowsthedistributionofstellarmassesforthose
stars that will have detections in ν max only. For these stars, Having explored the general trends of detection in
anexternalestimateofbothT eff andRisneededtoestimate ν max -∆ν-magnitude space, we now turn to simulated
the mass.
asteroseismic yields using the above detection methods.
Our yield calculations depend on both the stellar pop-
do not have ∆ν detections (70% of our detected sam-
ulations in the GBTDS fields and the line-of-sight ex-
ple),wecanusetheStefan-Boltzmannlawtodetermine
tinction. Thelattercanvaryonsmallspatialscalesand
R:
theextinctionlawintheGalacticbulgemaynotexactly
L
(cid:18)
R
(cid:19)2(cid:18)
T
(cid:19)4
matchthatofthesolarvicinity,thoughforourpurposes
= , (12)
L R T we make the assumption that they are the same. The
⊙ ⊙ ⊙
Roman mission will greatly improve our understanding
where L can be determined with photometric data, an
ofextinctioninthese fields. Webeginby describingour
extinction model, and a trigonometric parallax, ϖ. In
baselinepopulationmodelandtheassociatedyieldsun-
addition to existing parallaxes from Gaia, Roman is ex-
der different detectability scenarios. We then follow up
pectedtodeliverpreciserelativeparallaxesfortheentire
by testing the robustness of our results against changes
asteroseismic sample, with precisions of 0.3µas (Gould
in the stellar population model.
et al. 2015). For the typical bulge star, the parallax
3.1. Stellar Population Model
uncertainty is therefore negligible, and temperature un-
certainties dominate. Nevertheless, as yet unknown as- To model the Roman fields, we generated synthetic
trometric systematics may cause the Roman parallaxes stellar populations using Galaxia (Sharma et al. 2011).

10
Galaxia creates a synthetic survey of stars in the Milky
Way given a field of view and assumed limiting magni-
tude. Stars are drawn with phase space density consis-
tent with the Besan¸con Milky Way model for the disk 4
(Robin et al. 2003), including a bar-shaped bulge (Blitz
et al. 1993). The assumed ages for stellar populations 2
in the thin disc vary with metallicity from -0.57 to 0.13.
The thick disc is assumed to have an age of 11 Gyr and 0
metallicityof-0.78±0.3. Thebulgeisassumedtohave
an age of 10 Gyr and metallicity of 0.0 ± 0.4. There 2
is also a halo component, which populates lower metal-
licites. 4
4.6 4.4 4.2 4.0 3.8 3.6 3.4
Individual stars are populated according to Padova log Teff/K
isochrones(Bertellietal.1994;Marigoetal.2008),with
initialmassfunctionsthatvaryaccordingtotheGalactic
component (thick disc, bulge, etc.). We refer the reader
to Sharma et al. (2011) for further details.
As inputs, we specify the limiting magnitude of the
desired survey, the fields of view, as well as a star-by-
star model of the extinction. We then convolve this
simulatedpopulationwithourdetectionprobabilitiesto
infer yields.
We adopt Galaxia because it allows for modification
oftheinputpopulation,suchasage-metallicityrelations
forbulgestars,andithaspreviouslybeenusedtomodel
asteroseismic yields (Sharma et al. 2016).1
Figure 7. Simulatedfieldsofviewfora15-minuteGBTDS
strategy, reproduced from the Roman Galactic Bulge Time-
Domain Survey Definition Committee Report1. Each black
polygonrepresentsaRomanpointing. Thebackgroundrep-
resents reddening from Marshall et al. (2006).
3.2. Survey Parameters
ForourGalaxia simulations,weadoptedfieldsofview
consistent with those proposed in the most recent Ro-
manCoreCommunityreport(seeFigure7). Thesurvey
1 https://asd.gsfc.nasa.gov/roman/comm forum/forum 17/
Core Community Survey Reports-rev03-compressed.pdf
L/L
gol
1.2M
1.8M
Figure 8. HR diagram of full Galaxia simulation, within
nominal field of view set by Roman Core Community sug-
gestions. Theredandblacklinesareevolutionarytracksfor
different stellar masses, shown in the legend.
is implemented in Galaxia using seven circular patches
of the sky, each with area 0.281 deg2 (the footprint size
of a single Roman pointing, referred in this work as
a field of view [FoV]; Cromey et al. 2023). All the
combined footprints, each with area 0.281 deg2, span
−0.22◦ <l<1.82◦ and −1.64◦ <b<−0.85◦. Note
thatthesimulatedfieldsinGalaxia arenotquitethecor-
rect shape, but this will only have a small effect on our
yields. Additionally,therehasbeenrecentinterestinin-
cludingafieldattheGalacticcenter(Terryetal.2023),
so an additional field centered at (0,0) was considered.
We used a limiting magnitude of 25, using 2MASS H-
bandasaproxyforRoman’sF146filter. Allmagnitudes
are AB unless otherwise stated. The entire simulation,
in the nominal region and with the listed parameters,
produces ≈ 18 million objects, seen in Figure 8.
3.3. Asteroseismic Detection
Wesetasteroseismicdetectioncriteriaforobjectswith
T ≤5250K, which covers the T domain within al-
eff eff
most all solar-like oscillators detected in the Kepler and
K2 samples. The amplitude depends on ν and the
max
noise properties are sensitive to apparent magnitude, so
we account for both in our yields. To do so, we inter-
polated probabilities, calculated with the Hon method,
of the survey, using given H-band magnitudes from the
survey and calculating ν according to (Brown et al.
max
1991, Kjeldsen & Bedding 1995):
(cid:18)
g
(cid:19)(cid:18)
T
(cid:19)−1/2
ν =ν eff . (13)
max max,⊙ g T
⊙ eff,⊙
We employ scipy’s LinearNDInterpolator (Virtanen
et al. 2020), though variations in yields due to inter-
polator scheme choice are at the percent level. Using

11
the resulting detection probabilities for each star in the
Galaxia simulation, we then randomly draw a represen-
tative ‘detection’ sample. 3000
3.4. Detection Results 2500
We constructed 8 possible detection samples, varying 2000
the cadence, detection method, and noise model. In
Table 1 we present the total number of asteroseismic 1500
detections, and those of them that belong to the bulge
1000
population, for each of the 8 cases.
We select the fourth row (in bold) as our nominal 500
scenario since it is the most conservative estimate. The
table can be read as follows: the first column lists the 12 13 14 15 16 17 18
simulated cadence, the second column lists the method H [AB mag]
usedtodetermineν detectionprobabilities,thethird
max
columnliststheadoptednoisemodel,thefourthcolumn
liststhetotalnumberofdetections,andthefifthcolumn
liststhesubsetofthosedetectionsfoundtobelongtothe
bulge population.
We adjusted the Galaxia models to account for age-
metallicity relations recently inferred for the Galactic
bulge (Joyce et al. 2023). Compared to the nominal
Galaxia bulgepopulation, thiscasehasalargerpropor-
tion of younger ages with higher metallicities. Due to
the higher metallicities in the bulge, the resulting de-
tection sample was larger in comparison to the nominal
Galaxia bulgestellarpopulation, whichhasmorelower-
metallicitystars. LowermetallicityRCstarsaretoohot
tosupportsolar-likeoscillations,whichexplainsthisdif-
ference. We discuss this more in 4.4.
For our nominal case, we predict a yield of 290,000
stars,with185,000detectedbelongingtothebulgepop-
ulation. Inallcases,theGBTDSispredictedtosurpass
existing asteroseismic sample sizes. To maintain a con-
servative approach, we show figures using the nominal
case.
4. DISCUSSION
Depending on the modeling choices, the detection
yields range from approximately 200,000 to nearly
650,000. Thefollowingsectionwilldiscussthesechoices
in detail and their influence on yield outcomes.
4.1. Noise Modeling
We find the selected noise model is important in sim-
ulatingdetectionsofsaturatedstars. Romanislikelyto
perform better than the Penny noise model we present
inthispaper, butworsethantheWilsonmodel. Wesee
this in Table 1, where the Hon detection method is sen-
sitive to the adopted noise model at the 10–30% level.
TheChaplinmethodisrelativelyinsensitivetothenoise
modelbecauseevenlowsignal-to-noisecasesaredeemed
detectable.
niB
rep
sratS
fo
#
Detections
Bulge
Figure9. Theapparentmagnitudedistributionofthenom-
inal detection yields nears the saturation limit for Roman
(≈15), and does not extend beyond ≈18 due to noise.
At the time of writing, the expected performance of
saturatedstarsinRomanisnotyetsettled,butitseems
possible that precise photometry may be possible up to
14th magnitude. As shown in Figure 9, the majority
of the asteroseismic sample falls between 15th and 16th
magnitude, where stars begin to saturate, making this
an important consideration.
4.2. Roman Parameters
Our yields depend on the specific fields chosen and
the observing strategy; neither has been finalized at the
time of writing. We have therefore considered different
scenarios for evaluating yields. For the 7.5-minute ca-
dence, we assumed that each field would be observed
twice in a given cycle, which corresponds to fewer fields
but more exposure time per field. For the nominal 15-
minutecadencewehavemoretotaldetectionssincemore
fieldscanbeobserved,whilethe7.5-minutecadencehas
more detections per field, leading to a more representa-
tive sample, as shown in Figure 10. From the figure, we
see an evident increase of recoverability per FoV from
15-min cadence to 7.5-min cadence. However, due to
constraints for the viewing time with Roman, the 7.5-
min cadence is limited to only 4 fields (highlighted in
yellow), meaning our total count of detections, and in
turn our total subset count in the bulge population, is
shown to be larger with the 15-min cadence as we are
abletoobserveallfieldsofview. AsshowninFigure10,
each field contains a comparable number of simulated
objects, with the exception of the Galactic center. Ad-
ditional simulations across other regions suggest that,
providedextinctionremainsrelativelyuniform,thestel-
lardensityperfieldremainsconsistent. Implementinga

12
Specifications of Simulated Detections and Bulge Counts
Cadence Detection Method Noise Model Detection Total Detections in Bulge
15-Min Cadence Chaplin Wilson 648,000 358,000
15-Min Cadence Chaplin Penny 624,000 349,000
15-Min Cadence Hon Wilson 417,000 253,000
15-Min Cadence Hon Penny 290,000 185,000
7.5-Min Cadence Chaplin Wilson 425,000 232,000
7.5-Min Cadence Chaplin Penny 415,000 229,000
7.5-Min Cadence Hon Wilson 342,000 195,000
7.5-Min Cadence Hon Penny 205,000 135,000
Table 1. A summary of GBTDS cases. ‘Cadence’ refers to how frequently Roman will observe each field (here we simulate a
15- and 7.5-minute cadence). ‘Detection Method’ refers to how we determine ν detection probabilities (either the Chaplin
max
method or Hon pipeline as described in Section 2.2). ‘Noise Model’ refers to the model we adopt for photometric noise (either
the Penny model or Wilson model as described in Section 2.1.2). ‘Detection Total’ is the total number of objects detected to
haveasteroseismology,and‘DetectionsinBulge’isasubsetofthoseidentifiedtobeofthebulgepopulation. Thenominalcase
quoted throughout, and which serves as the basis for figures in the text, is highlighted in bold.
100000
80000
60000
40000
20000
0
1 2 3 4 5 6 7
Field ID
snoitceteD
15-Min Cadence 7.5-Min Cadence
Nominal FoV 100000 Nominal FoV
Galactic Center Galactic Center
7.5-Min Strategy
80000
60000
40000
20000
0
1 2 3 4 5 6 7
Field ID
Figure 10. Counts of detections per target field, for both a 15-minute cadence and 7.5-minute cadence of the nominal case.
The yellow highlighted bars are the regions that are used in the 7.5-minute cadence survey. Field IDs are as listed in Fig. 7.
Althoughthe7.5-minutecadencerecoversmoreasteroseismicdetectionsperFoV,itisabletoonlybeusedforalimitednumber
of fields, and excludes the Galactic center, as indicated with the yellow highlights. The 15-minute cadence is able to observe in
nearly double the number of fields, including the Galactic center.
faster cadence would also improve the quality of astero- where the most dust is found and therefore the fewest
seismic parameters ∆ν as shown in Figure 4. detections.
4.3. Extinction 4.4. Sample Characteristics
When calculating extinction values from dust maps, The nominal asteroseismic detection yields contain a
we found the difference between Schlegel et al. (1998) significant number of RC stars. This can be seen with
and Marshall et al. (2006) only impacts the yields mini- the higher detection probabilities in comparison to the
mally. As mentioned before, Marshall extinction values totalandRGBinFigure11andtheresultingprominent
were used to stay consistent with simulations by Penny peak in the luminosity distribution at log L ≈ 1.7 in
L⊙
et al. (2019). The marginal differences are primarily Figure 12. Conversely, we see that RGB stars have a
due to the placement of the fields of view, which hap- lower probability of detection, shown in Figure 11. The
pen to be in a region with low extinction. The largest RC population is also evident in the radius distribution
discrepancies in yields are found at the Galactic center, of the sample, corresponding to a peak of ∼ 11R in
⊙

13
1.0
0.8
0.6
0.4
0.2
0.0
0.0 0.2 0.4 0.6 0.8 1.0
Detection Probability
ytilibaborP
evitalumuC
Combined
RC
RGB
Figure11. Cumulativedistributionplotoftheprobabilities
ofdetectionofthenominalcase. Thisreferstothelikelihood
(‘CumulativeProbability’)ofanobjecthavingaprobability
(‘DetectionProbability’)tohaveameasurableasteroseismic
signal. The ‘Combined’ function is of the ‘RC’ and ‘RGB’
cumulative plots.
3.0
2.5
2.0
1.5
3.7503.7253.7003.6753.6503.6253.600
log T /K
eff
L/L
gol
1.0
0.5
0.0
1.2M
1.8M
Det
Prob
10000
8000
6000
4000
2000
10 15 20 25 30
Stellar Radius [R ]
Figure12. HRdiagramofthenominalcase,color-codedby
theinterpolateddetectionprobability. Collapsedhistograms
showthemarginalizedtemperatureandluminositydistribu-
tions. Example solar-metallicity Padova evolutionary tracks
areprovidedforreference. Thebandedstructureoftheprob-
ability detection visible in the figure is primarily due to the
variation in detection probability as a function of ν seen
max
in Fig. 3.
Figure 13. Nevertheless, RGB stars comprise 40% of
the sample.
With regard to H-band distribution, we see a promi-
nent peak just below 16th magnitude (Figure 9), which
reflectsthemagnitudeofatypicalclumpstaratthecen-
ter of the bulge. With a faster cadence, we would see a
significant number of fainter objects being detected, ex-
tending Figure 9. If the 7.5-minute cadence strategy in-
cludedtheGalacticcenter, manyoftheseobjectswould
populate that region, because of the significant extinc-
niB
rep
sratS
fo
#
Detections
Bulge
Figure 13. Histogram of both the nominal detections and
detectionsinthebulgeasafunctionofradius,showingthat
stars at the red clump and below comprise the majority of
the expected asteroseismic yields from Roman.
Detections Varying Extinction and AMR
Schlegel Marshall
Adjusted Default Adjusted Default
283,000 305,000 290,000 312,000
Table 2. Asteroseismic yields for nominal scenario with
Schlegel et al. (1998) and Marshall et al. (2006), both with
(‘Adjusted’) and without (‘Default’) modifications to the
bulge age-metallicity relation (AMR). See text for details.
tion at the Galactic center. The 15-minute cadence is
less sensitive to regions with higher extinction, making
it more difficult to recover fainter objects, especially at
the Galactic center.
All of our simulation cases assume an age-metallicity
relation (AMR) consistent with recent work from Joyce
etal.(2023). Toaccountforvariationsinageandmetal-
licity,wesimulatedthreebulgepopulations,oneforeach
metallicity bin in the Joyce et al. (2023) age-metallicity
relation, combining them in proportion to the number
of objects in each bin. Note that this adjustment ap-
plies only to the bulge population. For reference, a case
without AMR was also run, using the Galaxia default
parametersforthebulge: ageof10Gyr±0.0andmetal-
licityof0.0[Fe/H]±0.4fortheentirebulgepopulation.
Thedifferenceintheresultingasteroseismicyieldswhen
not assuming Galaxia’s default ages and metallicities of
thebulgeisshowninFigure14,whereweseethatthere
are more metal-poor stars in the updated AMR. Never-
theless,thenumberofmetal-poorstarsdetectedremains
lowbecauseatlowmetallicity,core-heliumburningstars

14
3000
2500
2000
1500
1000
500
0
2.0 1.5 1.0 0.5 0.0 0.5 1.0 1.5
[Fe/H]
niB
rep
sratS
fo
#
Adjusted Bulge AMR Default Bulge AMR
Total Detections Total Detections
Bulge Bulge
Red Clump Red Clump
Red Giant Branch Red Giant Branch
2.0 1.5 1.0 0.5 0.0 0.5 1.0 1.5
[Fe/H]
Figure14. HistogramoftheasteroseismicyieldswithandwithoutmodificationstothedefaultGalaxiaage-metallicityrelation
for the bulge, showing modest differences in the resulting metallicity distributions of the yields
.
250
200
150
100
50
3000 4000 5000 6000 7000 8000
Teff [K]
niB
rep
sratS
fo
#
[Fe/H] < -1 -1 [Fe/H] 0.5 [Fe/H] > 0.5
Galaxia 12000 Galaxia 3000 Galaxia
10000 2500
8000 2000
6000 1500
4000 1000
2000 500
3000 4000 5000 6000 7000 8000 3000 4000 5000 6000 7000 8000
Teff [K] Teff [K]
Figure 15. DistributionsofsimulatedGalaxia populationtemperaturesfordifferentmetallicitybinsshowwhylow-metallicity
stars are preferentially lost in the asteroseismic yields: their temperatures are largely hotter than our adopted 5250K limit for
solar-like oscillations (note the differing y-axis scales). A 1% uncertainty is applied to the plots.
transition to the blue horizontal branch instead of the serving cadence, as well as an additional 7.5-minute ca-
RC, becoming too hot to exhibit solar-like oscillations. dence, to demonstrate the impact of cadence on yields.
Thistransitionintemperatureasafunctionofmetallic- We also injected white noise following a conservative
ity is demonstrated in Figure 15. noise floor of ∼ 1mmag for saturated stars and a more
optimistic noise model with improved saturated star
5. CONCLUSION photometry. We derived detection probabilities of the
global asteroseismic frequencies, ν and ∆ν, by using
In this paper, we have simulated realistic time-series max
traditionalSNRcalculationsfromChaplinetal.(2011),
data of red giant stars exhibiting solar-like oscillations
a neural-network based asteroseismic detection pipeline
for the Roman Galactic Bulge Time-Domain Survey
(Hon et al. 2018), and the SYD pipeline (Huber et al.
(GBTDS).WeusedKeplerlightcurvesof100redclump
2009). We then applied these detection probabilities to
and 100 RGB stars from APOKASC-3 as a basis for
a simulated survey based on GBTDS strategies using
our simulations. We applied modifications to the light
Galaxia tomodelasampleofstellarobjectswhereν
curves assuming the GBTDS’s nominal 15-minute ob- max

15
was detected. We further tested our results by varying Seeing that it is possible to measure ν for a large
max
properties of the Galactic bulge and checking the im- number of stars and ∆ν for a subset of that popula-
pact on yields under both the Schlegel et al. (1998) and tion, it is necessary to determine our ability to measure
Marshall et al. (2006) dust maps and use of a modi- T and R in the bulge. Roman multiband photom-
eff
fiedage-metallicityrelationshipdescribedinJoyceetal. etry, grism spectroscopy, and precise astrometry could
(2023). We obtained the following results: be useful in this regard (G15; Roman Core Community
report).
• Wefoundthatimplementinga7.5-minutecadence
Our simulated yields prove the transformative poten-
canincreaseyieldsbyupto50%perobservedfield.
tial of asteroseismology with the Roman GBTDS. Stel-
However,the7.5-mincadencewillhavefewerfields
lar ages with competitive uncertainties will be available
compared to the 15-minute cadence, leading to an
for the first time for hundreds of thousands of red gi-
overalldropindetections,albeitathigherquality.
ants in the bulge, and should enable a number of stellar
population and Galactic archaeology applications.
• Since the bulk of our Galaxia simulated sample
is saturated in the Roman detectors, the photo-
ACKNOWLEDGMENTS
metric noise performance has a significant impact
This work was supported by NASA award
ondetections. Wefounda∼44%increaseintotal
80NSSC24K0091. This work was partially supported
detectionscomparedtoournominal(conservative)
by funding from the Department of Astronomy of the
casewhenweimplementedamoreoptimisticnoise
Ohio State University. This paper includes data col-
model.
lected by the Kepler mission and obtained from the
• In contrast, varying the locations of the fields of MAST data archive at the Space Telescope Science In-
stitute(STScI).WethankMatthewPennyandJennifer
viewandextinctionchoicehadminimalimpacton
Johnsonfortheircontributionsandadvisementthrough-
the total number of detected objects.
out the duration of the work. We thank Tom Barclay,
• Wefoundthat∼1/3ofoursamplewillhaveboth Joshua Schlieder, and the Roman Team for their in-
ν and ∆ν detections, though using ν mea- sight on the project. We acknowledge support from the
max max
surementsaloneincombinationwithparallaxfrom Australian Research Council for D.S. (DP190100666)
Roman and/or Gaia will result in more competi- and T.R.B. (FL220100117). B.S.G. was supported by
tive precisions in mass and age. the Thomas Jefferson Chair for Discovery and Space
Exploration Endowment.
• Adjusting the age-metallicity relation has a lim-
Software: Galaxia (Sharma et al. 2011), SciPy
ited, but measurable, affect on the asteroseismic
(Virtanen et al. 2020), astropy (Astropy Collaboration
yields.
et al. 2013, 2018, 2022), mwdust (Bovy et al. 2016),
• Givenournominalstrategy,wefound 290,000to- LightKurve (LightkurveCollaboration 2018), pandas
(pandas development team 2020), Matplotlib (Hunter
tal detections, with 185,000 of those detections
2007), seaborn (Waskom 2021), numpy (Harris et al.
in the Galactic bulge. By varying the selected ca-
2020)
dence, noise model, and detection algorithm, we
found total detections as low as 205,000 and as
highas648,000,correspondingtobulgedetections
of 135,000 and 358,000, respectively.
In future work, we plan on cross-matching our simu-
lated results with data collected by Gaia (Gaia Collab-
oration et al. 2016, Gaia Collaboration et al. 2023) and
2MASS (Skrutskie et al. 2006), which will be useful in
constructing an asteroseismic target list in preparation
for Roman’s launch. The stellar population simulations
presented here complement this effort by providing an
estimate of the completeness of the Roman asteroseis-
mic yields, which will be crucial for exoplanet-hosting
population characterization and studies of the age dis-
tributions of bulge stars.

16
REFERENCES
Abbott, C. G., Valluri, M., Shen, J., et al. 2017, MNRAS, Gaia Collaboration, Vallenari, A., Brown, A. G. A., et al.
470, 1526, doi: 10.1093/mnras/stx1262 2023, A&A, 674, 22 pp,
Ash, A. L., Pinsonneault, M. H., Vrard, M., & Zinn, J. C. doi: 10.1051/0004-6361/202243940
2025, ApJ, 979, 135, doi: 10.3847/1538-4357/ad9b18 Gilliland, R., Brown, T., Christensen-Dalsgaard, J., et al.
Astropy Collaboration, Robitaille, T. P., Tollerud, E. J., 2010, PASP, 122, 131, doi: 10.1086/650399
et al. 2013, A&A, 558, A33, Girardi, L. 2016, ARAA, 54, 95,
doi: 10.1051/0004-6361/201322068 doi: 10.1146/annurev-astro-081915-023354
AstropyCollaboration,Price-Whelan,A.M.,Sipo˝cz,B.M., Gould, A., Huber, D., Penny, M., & Stello, D. 2015, JKAS,
et al. 2018, AJ, 156, 123, doi: 10.3847/1538-3881/aabc4f 48, 93, doi: 10.5303/JKAS.2015.48.2.93
Astropy Collaboration, Price-Whelan, A. M., Lim, P. L., Harris, C. R., Millman, K. J., van der Walt, S. J., et al.
etal.2022,ApJ,935,167,doi:10.3847/1538-4357/ac7c74 2020, Nature, 585, 357, doi: 10.1038/s41586-020-2649-2
Hayden, M., Bovy, J., Holtzman, J., et al. 2015, ApJ, 808,
Belkacem, K., Goupil, M. J., Dupret, M. A., et al. 2011,
18, doi: 10.1088/0004-637X/808/2/132
A&A, 530, A142, doi: 10.1051/0004-6361/201116490
Hekker, S. 2020, Frontiers in Astronomy and Space
Bensby, T., Feltzing, S., Gould, A., et al. 2017, A&A, 605,
Sciences, 7, 3, doi: 10.3389/fspas.2020.00003
34, doi: 10.1051/0004-6361/201730560
Hey, D., Huber, D., Shappee, B., et al. 2023, AJ, 166, 12,
Berger, T., Huber, D., Gaidos, E., et al. 2020, The
doi: 10.3847/1538-3881/ad01bf
Astronomical Journal, 160, 108B,
Hon, M., Huber, D., Kuszlewicz, J. S., et al. 2021, ApJ,
doi: 10.3847/1538-3881/aba18a
919, 18, doi: 10.3847/1538-4357/ac14b1
Bertelli, G., Bressan, A., Chiosi, C., et al. 1994, Astronomy
Hon, M., Stello, D., Garc´ıa, R., et al. 2019, MNRAS, 485,
& Astrophysics Suppl., 106, 275
5616, doi: 10.1093/mnras/stz622
Blitz, L., Binney, J., Lo, K., et al. 1993, Nature, 361, 417,
Hon, M., Stello, D., & Yu, J. 2018, MNRAS, 476, 3233,
doi: 10.1038/361417a0
doi: 10.1093/mnras/sty483
Borucki, W., Koch, D., Basri, G., et al. 2010, Science, 327,
Huber, D., Pinsionneault, M., Beck, P., et al. 2023, eprint
977, doi: 10.1126/science.1185402
arXiv, doi: 10.48550/arXiv.2307.03237
Borucki, W., Koch, D., Dunham, E., & Jenkins, J. 1997,
Huber, D., Stello, D., Bedding, T., et al. 2009, CoAst, 160,
ASP, 119, 153, doi: 1997ASPC..119..153B
74, doi: 10.48550/arXiv.0910.2764
Bovy, J., Rix, H.-W., Green, G. M., et al. 2016, ApJ, 818,
Hunter,J.D.2007,ComputinginScience&Engineering,9,
130, doi: 10.3847/0004-637X/818/2/130
90, doi: 10.1109/MCSE.2007.55
Brown, T., Gilliland, R., Noyes, R., & Ramsey, L. 1991,
Jackiewicz, J. 2021, Frontiers in Astronomy and Space
ApJ, 368, 599, doi: 10.1086/169725
Sciences, 7, 102, doi: 10.3389/fspas.2020.595017
Brown,T.M.,Latham,D.W.,Everett,M.E.,&Esquerdo,
Joyce, M., Johnson, C. I., Marchetti, T., et al. 2023, ApJ,
G. A. 2011, AJ, 142, 112,
946, 31, doi: 10.3847/1538-4357/acb692
doi: 10.1088/0004-6256/142/4/112
Kallinger, T., Weiss, W., Barban, C., et al. 2010, A&A,
Chaplin, W., Kjeldsen, H., Bedding, T., et al. 2011, ApJ,
509, A77, doi: 10.1051/0004-6361/200811437
732, 9, doi: 10.1088/0004-637X/732/1/54
Kjeldsen, H., & Bedding, T. 1995, A&A, 293, 87,
Chaplin, W., & Miglio, A. 2013, ARAA, 51, 353,
doi: 10.48550/arXiv.astro-ph/9403015
doi: 10.1146/annurev-astro-082812-140938
Kurtz, D. 2022, ARAA, 60, 31,
Ciuca˘, I., Kawata, D., Miglio, A., et al. 2021, MNRAS, 503, doi: 10.1146/annurev-astro-052920-094232
2814, doi: 10.1093/mnras/stab639 Leung, H. W., Bovy, J., Mackereth, J. T., et al. 2023,
Cromey, B., Handorf, R. V., Pedroncelli, J., et al. 2023, MNRAS, 522, 4577, doi: 10.1093/mnras/stad1272
Proceeding of the SPIE, 12676, 12 pp, Li,Y.,Bedding,T.R.,Stello,D.,etal.2023,MNRAS,523,
doi: 10.1117/12.2676488 916, doi: 10.1093/mnras/stad1445
David, T., Contardo, G., Sandoval, A., et al. 2021, The LightkurveCollaboration. 2018, Astrophysics Source Code
Astronomical Journal, 161, 265, Library, doi: 2018ascl.soft12013L
doi: 10.3847/1538-3881/abf439 Lund, M. N. 2019, MNRAS, 489, 1072,
Gaia Collaboration, Brown, A. G. A., Vallenari, A., et al. doi: 10.1093/mnras/stz2010
2016, A&A, 595, 23 pp, MacKereth, J. T., Bovy, J., Leung, H. W., et al. 2019,
doi: 10.1051/0004-6361/201629512 MNRAS, 489, 176, doi: 10.1093/mnras/stz1521

17
Marigo, P., Girardi, L., Bressan, A., et al. 2008, Astronomy Skrutskie, M. F., Cutris, R. M., Stiening, R., et al. 2006,
& Astrophysics, 482, 883, The Astronomical Journal, 131, 1163,
doi: 10.1051/0004-6361:20078467 doi: 10.1086/498708
Marshall, D. J., Robin, A. C., Reyl´e, C., et al. 2006, A&A, Soszyn´ski, I., Udalski, A., Szyman´ski, M. K., et al. 2013,
453, 635, doi: 10.1051/0004-6361:20053842
Acta Astronomica, 63, 21, doi: 10.48550/arXiv.1304.2787
Martig, M., Fouesneau, M., Rix, H.-W., et al. 2016,
Spergel, D., Gehrels, N., Baltay, C., et al. 2015, eprint
MNRAS, 456, 3655, doi: 10.1093/mnras/stv2830
arXiv, doi: 10.48550/arXiv.1503.03757
Miglio, A., Chiappini, C., Mackereth, J. T., et al. 2021,
Sreenivas, K. R., Bedding, T. R., Huber, D., et al. 2025,
A&A, 645, 24, doi: 10.1051/0004-6361/202038307
arXiv e-prints, arXiv:2502.01899,
Miglio, A., Chiappini, C., Morel, T., et al. 2013, MNRAS,
429, 423, doi: 10.1093/mnras/sts345 doi: 10.48550/arXiv.2502.01899
Morris, B., & Huber, D. in prep, doi: https: Stanek, K. Z., Udalski, A., SzymaN´ski, M., et al. 1997,
//github.com/bmorris3/gadfly?tab=readme-ov-file ApJ, 477, 163, doi: 10.1086/303702
Mosser, B., Pinc¸on, C., Belkacem, K., et al. 2017, A&A, Stello, D., Bruntt, H., Preston, H., & Buzasi, D. 2008, ApJ
600, 10, doi: 10.1051/0004-6361/201630053 Letters, 674, L53, doi: 10.1086/528936
Nascimbeni, V., Piotto, G., Bo¨rner, A., et al. 2022, A&A, Stello, D., Huber, D., Bedding, T., et al. 2013, ApJ, 765, 5,
658, A31, doi: 10.1051/0004-6361/202142256
doi: 10.1088/2041-8205/765/2/L41
Nataf, D. M. 2015, Astronomical Society of the Pacific
Stello, D., Saunders, N., Grunblatt, S., et al. 2022,
Conference Series, 491, 174
MNRAS, 512, 1677, doi: 10.1093/mnras/stac414
Ness, M., Hogg, D. W., Rix, H.-W., et al. 2016, ApJ, 823,
Stello, D., Zinn, J., Elsworth, Y., et al. 2017, ApJ, 835, 83,
19 pp., doi: 10.3847/0004-637X/823/2/114
doi: 10.3847/1538-4357/835/1/83
Ness, M., & Lang, D. 2016, The Astronomical Journal, 152,
STScI. 2011, Kepler/KIC, STScI/MAST,
4 pp., doi: 10.3847/0004-6256/152/1/14
pandas development team, T. 2020, pandas-dev/pandas: doi: 10.17909/T9059R
Pandas, latest, Zenodo, doi: 10.5281/zenodo.3509134 Tayar, J., Clator, Z. R., Huber, D., & van Saders, J. 2022,
Penny, M. T., Gaudi, B., Kerins, E., et al. 2019, ApJ ApJ, 927, 11, doi: 10.3847/1538-4357/ac4bbc
SupplementSeries,241,3,doi:10.3847/1538-4365/aafb69 Terry, S., Hosek, M., Lu, J., et al. 2023, eprint arXiv,
Pinsonneault, M., Zinn, J., Tayar, J., et al. 2025, ApJ doi: 10.48550/arXiv.2306.12485
Supplement Series, doi: 10.3847/1538-4365/ad9fef
Ting, Y.-S., & Rix, H.-W. 2019, ApJ, 878, 16,
Pinsonneault, M. H., Elsworth, Y. P., Tayar, J., et al. 2018,
doi: 10.3847/1538-4357/ab1ea5
ApJ Supplemental Series, 239, 32 pp.,
Ulrich, R. 1986, ApJ Letters, 306, L37, doi: 10.1086/184700
doi: 10.3847/1538-4365/aaebfd
Virtanen, P. T., Gommers, R., Oliphant, T. E., et al. 2020,
Reyes, C., Stello, D., Hon, M., et al. 2022, MNRAS, 511,
NatureMethods,17,261,doi:10.1038/s41592-019-0686-2
5578, doi: 10.1093/mnras/stac445
Waskom, M. L. 2021, Journal of Open Source Software, 6,
Robin,A.C.,Reyl´e,C.,Derri`ere,S.,etal.2003,A&A,409,
523, doi: 10.1051/0004-6361:20031117 3021, doi: 10.21105/joss.03021
Schlegel, D. J., Finkbeiner, D. P., & Davis, M. 1998, ApJ, White, T., Bedding, T., Stello, D., et al. 2011, ApJ, 743,
500, 525, doi: 10.1086/305772 13, doi: 10.1088/0004-637X/743/2/161
Sharma, S., Bland-Hawthorn, J., Johnston, K. V., et al. Wilson, R., Barclay, T., Powell, B., et al. 2023, ApJ
2011, ApJ, 730, 20 pp, doi: 10.1088/0004-637X/730/1/3 Supplement Series, 269, 37,
Sharma, S., Stello, D., Bland-Hawthorn, J., et al. 2016, doi: 10.3847/1538-4365/acf3df
ApJ, 822, 15 pp, doi: 10.3847/0004-637X/822/1/15
Yu, J., Huber, D., Bedding, T. R., et al. 2018, MNRAS,
Silva-Aguirre, V., Davies, G., Basu, S., et al. 2015,
480, L48, doi: 10.1093/mnrasl/sly123
MNRAS, 452, 2127, doi: 10.1093/mnras/stv1388
