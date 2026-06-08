# 13_TudorCar2020_Conversational_Agents_Scoping_Review

Source PDF: `/Users/mac/Documents/6-Research/4-SpatialAgent-Survey/assets/survey_paper/pdfs/review_library/13_TudorCar2020_Conversational_Agents_Scoping_Review.pdf`

Extraction backend: `PyMuPDF`

## Page 1

Review
Conversational Agents in Health Care: Scoping Review and
Conceptual Analysis
Lorainne Tudor Car1,2, MD, MSc, PhD; Dhakshenya Ardhithy Dhinagaran1, BSc (hons); Bhone Myint Kyaw1, MBBS,
MSc, PhD; Tobias Kowatsch3,4,5, MSc, PhD; Shafiq Joty6, MSc, PhD; Yin-Leng Theng7, PhD; Rifat Atun8, MBBS,
MBA, FRCGP, FFPH, FRCP
1Family Medicine and Primary Care, Lee Kong Chian School of Medicine, Nanyang Technological University Singapore, Singapore
2Department of Primary Care and Public Health, School of Public Health, Imperial College London, London, United Kingdom
3Future Health Technologies programme, Campus for Research Excellence and Technological Enterprise (CREATE), Singapore-ETH Centre, Singapore
4Center for Digital Health Interventions, Department of Management, Technology, and Economics, ETH Zurich, Zurich, Switzerland
5Center for Digital Health Interventions, Institute of Technology Management, University of St Gallen, St Gallen, Switzerland
6School of Computer Sciences and Engineering, Nanyang Technological University Singapore, Singapore
7Centre for Healthy and Sustainable Cities, Nanyang Technological University, Singapore
8Department of Global Health and Population, Harvard T.H. Chan School of Public Health, Harvard University, Boston, MA, United States
Corresponding Author:
Lorainne Tudor Car, MD, MSc, PhD
Family Medicine and Primary Care
Lee Kong Chian School of Medicine
Nanyang Technological University Singapore
11 Mandalay Road
Singapore
Phone: 65 69041258
Fax: 65 69041258
Email: lorainne.tudor.car@ntu.edu.sg
Abstract
Background: Conversational agents, also known as chatbots, are computer programs designed to simulate human text or verbal
conversations. They are increasingly used in a range of fields, including health care. By enabling better accessibility, personalization,
and efficiency, conversational agents have the potential to improve patient care.
Objective: This study aimed to review the current applications, gaps, and challenges in the literature on conversational agents
in health care and provide recommendations for their future research, design, and application.
Methods: We performed a scoping review. A broad literature search was performed in MEDLINE (Medical Literature Analysis
and Retrieval System Online; Ovid), EMBASE (Excerpta Medica database; Ovid), PubMed, Scopus, and Cochrane Central with
the search terms “conversational agents,” “conversational AI,” “chatbots,” and associated synonyms. We also searched the gray
literature using sources such as the OCLC (Online Computer Library Center) WorldCat database and ResearchGate in April
2019. Reference lists of relevant articles were checked for further articles. Screening and data extraction were performed in
parallel by 2 reviewers. The included evidence was analyzed narratively by employing the principles of thematic analysis.
Results: The literature search yielded 47 study reports (45 articles and 2 ongoing clinical trials) that matched the inclusion
criteria. The identified conversational agents were largely delivered via smartphone apps (n=23) and used free text only as the
main input (n=19) and output (n=30) modality. Case studies describing chatbot development (n=18) were the most prevalent,
and only 11 randomized controlled trials were identified. The 3 most commonly reported conversational agent applications in
the literature were treatment and monitoring, health care service support, and patient education.
Conclusions: The literature on conversational agents in health care is largely descriptive and aimed at treatment and monitoring
and health service support. It mostly reports on text-based, artificial intelligence–driven, and smartphone app–delivered
conversational agents. There is an urgent need for a robust evaluation of diverse health care conversational agents’ formats,
focusing on their acceptability, safety, and effectiveness.
(J Med Internet Res 2020;22(8):e17158) doi: 10.2196/17158
J Med Internet Res 2020 | vol. 22 | iss. 8 | e17158 | p. 1
http://www.jmir.org/2020/8/e17158/
(page number not for citation purposes)
Tudor Car et al
JOURNAL OF MEDICAL INTERNET RESEARCH
XSL•FO
RenderX

## Page 2

KEYWORDS
conversational agents; chatbots; artificial intelligence; machine learning; mobile phone; health care; scoping review
Introduction
Background
Conversational agents or chatbots are computer programs that
simulate conversations with users [1]. They are increasingly
adopted in many different fields, including finance, commerce,
marketing, retail, and fitness, with favorable reception from
customers [2]. Conversational agents are often deployed via
messaging apps, a website, or a mobile phone app. They can
also be integrated into cars and television sets or in the form of
a stand-alone device such as speakers. They can converse
through a range of methods such as text, image, and voice.
Conversational agents that can interpret human speech and
respond via synthesized voices as well as manage tasks
requested by the user are also known as voice assistants. Some
of the most popular voice assistants include Apple’s Siri,
Amazon’s Alexa, Google Assistant, and Microsoft’s Cortana,
mostly delivered using voice-activated or smart speakers such
as Amazon’s Echo and Google Home. They are utilized for
aiding or executing tasks such as web-based shopping, control
of smart home devices, and disseminating news or for
entertainment [3-5].
Conversational agents cover a broad spectrum of aptitudes
ranging from simple to smart [2]. Simple conversational agents
are rule based, meaning that they depend on prewritten
keywords and commands programmed by the developer. The
user is therefore restricted to predetermined options when
answering questions posed by the conversational agents, and
there is little or no opportunity for free responses. If a user enters
a question or sentence without a single keyword, the
conversational agents will be unable to understand the input
and will respond with a default message such as “Sorry, I did
not understand” [2]. Despite these restrictions, simple
conversational agents are increasingly used in executing tasks
such as booking appointments, purchasing merchandise,
ordering food, and sharing information without the need for
human involvement [2].
In contrast, smart conversational agents do not respond with
preprepared answers but with adequate suggestions instead.
This is enabled by machine learning, a type of artificial
intelligence (AI), which allows for broadening of the computer
system’s capacity through its learning from data (in this case
conversations) without being explicitly programmed [2,6]. The
process whereby the machine translates human commands into
a form in which the computer can understand, process, and
revert to the user is called natural language processing (NLP)
[6] and natural language understanding or interpretation [6,7].
This degree of programming allows for personalized
conversational agents to be generated. Smart conversational
agents have the potential to undertake more complex tasks that
involve greater interaction, reasoning, prediction, and accuracy.
Although the technology behind smart conversational agents is
continuously developed, they currently do not have full
human-level language abilities, resulting in misunderstanding
and users’dissatisfaction [8]. Furthermore, as machine learning
algorithms develop, it is becoming increasingly challenging to
keep track of their development, evolution, and the reasoning
behind their responses. This is known as the black box effect
[9,10]. Although the black box effect appears to be an
unavoidable consequence of the use of AI, there is some
emerging research on making AI transparent and explainable
[11]. However, at the moment, its use may affect the safety and
accuracy of treatment and should be carefully monitored and
evaluated when used in health care [9].
The first conversational agent ELIZA was developed by
Weizenbaum [12] in 1966, with ELIZA taking on the role of a
person-centered Rogerian psychotherapist (Figure 1). This was
a groundbreaking contribution to the field of AI and was
reported to have a positive impact on patients who
communicated with the conversational agent [13]. A step up
from ELIZA was achieved when PARRY, a conversational agent
representing a simulated paranoid patient with schizophrenia,
was developed [14,15]. These first examples of conversational
agents, chatterbots (as they were referred to then), in health
care were valuable in demonstrating that virtual agents have the
potential to mimic human-human conversation and successfully
pass the Turing Test, a test of a machine’s ability to replicate
human intelligence, and the machine passes the test when the
tester cannot distinguish it from the human [16].
The literature over the next few decades does not explicitly
mention chatbots or conversational agents in health care, but
it does refer to talking computers [17-21], a less sophisticated
version of today’s conversational agents previously used for
conducting patient satisfaction surveys [17], altering adult eating
habits [18], aiding health care service delivery through diagnosis
aid [19], and promoting patient-physician communication [20].
Although not presented in the literature, chatbot Jabberwacky
was released in 1988. It was one of the first few AI agents
developed for human interaction and entertainment and
introduced the shift from text- to voice-operated conversational
agents. Soon after, ALICE gained plenty of attention in 1995,
after which it went on to win the Loebner Prize 3 times in 2000,
2001, and 2004.
J Med Internet Res 2020 | vol. 22 | iss. 8 | e17158 | p. 2
http://www.jmir.org/2020/8/e17158/
(page number not for citation purposes)
Tudor Car et al
JOURNAL OF MEDICAL INTERNET RESEARCH
XSL•FO
RenderX

## Page 3

Figure 1. Evolution of conversational agents from 1966 to 2019.
The next big milestone for conversational agents was in 2010
when Apple released Siri. The interest in conversational agents
increased exponentially at this point as evidenced by Google,
Amazon, and Microsoft all developing their own versions over
the coming years: Google now, Alexa, and Cortana, respectively
[14]. Year 2016 was named the Year of the Chatbot as a number
of major information technology companies started to use
conversational agents: Facebook launched its messenger
platform for conversational agents, Google announced its
procurement of the conversational agent development tool
API.ai, LinkedIn revealed its first messaging bot, and Viber
released Public Accounts for chatting with businesses [22-25].
Currently, the title of the world’s best conversational agent is
held by Mitsuku, a 4-time winner of the Loebner Prize, an
annual competition in AI [26].
Health care, which has seen a decade of text messaging on
smartphones, is an ideal candidate for conversational
agent–delivered interventions. Conversational agents enable
interactive, 2-way communication, and their text- or
speech-based method of communication makes it suitable for
a variety of target populations, ranging from young children to
older people. The concept of using mobile phone messaging as
a health care intervention has been present and increasingly
explored in health care research since 2002 [27]. A series of
systematic reviews on the use of text messaging for different
health disorders have shown that text messaging is an effective
and acceptable health care intervention [28,29]. With a global
penetration rate of 96% [28], mobile phones are ubiquitous and
avidly used, and can be efficiently harnessed in health care [30].
Conversational agents are increasingly used in diverse fields,
including health care, and there is a need to identify different
ways and outcomes of the use of conversational agents in health
care. Existing reviews on conversational agents focus on a
certain subtype of agents such as virtual coaches [31-33] or
embodied conversational agents (ECAs) [34] or on specific
functionalities of these agents such as behavior change [35] or
mental health applications [36,37]. Other reviews report solely
on the technical aspects of conversational agents such as system
architecture and dialogues [38] or on the funding component
of health care conversational interfaces [39].
Objectives
Our objective was to provide a comprehensive overview of the
existing research literature on the use of health care–focused
conversational agents. We aimed to examine how conversational
agents have been employed and evaluated in the literature to
date and map out their characteristics. Finally, in line with the
observed gaps in the literature, we sought to provide
recommendations for future conversational agent research,
design, and applications.
Methods
Search Strategy
We adopted methodological guidance from an updated version
of the Arksey and O’Malley framework with suggestions
proposed by Peters et al [40] in 2015 to conduct our scoping
review. To identify literature pertaining to the application of
conversational agents in health care, a broad literature search
was conducted in April 2019 in MEDLINE (Medical Literature
Analysis and Retrieval System Online; Ovid), EMBASE
(Excerpta Medica database; Ovid), PubMed, Scopus, and
Cochrane Central. Given the novelty of the field, the amount
of ongoing research happening in the area, and to increase
comprehensiveness, we also searched for the gray literature in
the OCLC WorldCat database, ResearchGate, Google Scholar,
OpenGrey, and the first 10 pages of Google.
We used an extensive list of 63 search terms, including various
synonyms for conversational agents (Multimedia Appendix 1).
These synonyms were generated using a web-based search and
by identifying specific terms or phrases used in the titles of
articles discussing health care conversational agents. The
reference list of relevant articles and systematic reviews were
also searched for further articles related to the review.
Inclusion and Exclusion Criteria
To map out the current conversational agent applications in
health care, we included primary research studies that had
conducted an evaluation and reported findings on a
conversational agent implemented for a health care–specific
purpose. We excluded articles that just presented a proposal for
conversational agent development, articles that mentioned
conversational agents briefly or as an insignificant part of a
review, as well as opinion pieces and articles where primary
research was not conducted or discussed. A further point of
exclusion was articles with poorly reported data on chatbot
assessments where there was minimal or no evaluation data. In
addition, we excluded articles concerning ECAs, relational
agents, animated conversational agents, or other conversational
agents with a visual or animated component.
J Med Internet Res 2020 | vol. 22 | iss. 8 | e17158 | p. 3
http://www.jmir.org/2020/8/e17158/
(page number not for citation purposes)
Tudor Car et al
JOURNAL OF MEDICAL INTERNET RESEARCH
XSL•FO
RenderX

## Page 4

ECAs are computer-generated virtual individuals with an
animated appearance to enable face-to-face interaction between
the user and the system [41]. Relational agents are a type of
ECA designed to create long-term deep and meaningful
relationships with individuals [42]. ECAs are similar to
conversational agents in that conversation is central to their
function; however, ECAs are more complex as hand movements
and facial expressions can be conveyed to the user as well [41].
The user’s interaction may be affected by nonverbal behaviors,
graphics, and layout of the program, and it was decided that the
complexities associated with ECAs are beyond the scope of this
review and were therefore excluded.
Screening, Data Extraction, and Analysis
Screening of articles for inclusion was performed in 2 stages:
title and abstract review and full article review, undertaken
independently by 2 reviewers. Following an initial screening
of titles and abstracts, full texts were obtained and screened by
2 reviewers. From the included studies, 2 reviewers
independently extracted relevant information in an Excel
(Microsoft) spreadsheet. We extracted data on the first author,
year of publication, source of literature, title of article, type of
literature, study design and methods, geographic focus, health
care sector, conversational agent name, accessibility of
conversational agent, dialogue technique, input and output
modalities, and nature of conversational agent’s end goal. We
piloted the data extraction sheet on at least five articles. Potential
discrepancies in the extracted data were discussed between the
authors and resolved through discussion and consensus.
We performed a narrative synthesis of the included literature
and presented findings on (1) study specifics, such as study
design, geographic focus, and type of literature; (2)
conversational agent specifics (ie, conversational agent delivery
channel, dialogue technique, personality, etc); (3) conversational
agent content analysis; and (4) study evaluation findings.
We used the principles of thematic analysis to analyze the
content, scope, and personality traits of the conversational
agents. Two researchers familiarized themselves with the
literature identified, generated the initial codes in relation to
personality and content analysis, applied the codes to the
included studies, compared their findings, and resolved any
discrepancies via discussion.
The need to present information on conversational agent
personality was motivated by the concepts presented in the study
by de Haan et al [43], which posits that personalities are not
just limited to humans but can be extended to nonhuman artifacts
to explain their actions and behavior [43]. Furthermore, it states
that personality traits are especially important in the design of
socially interactive robots, such as conversational agents. The
5 dimensions of personality presented in this paper were derived
from
the
following:
extraversion,
agreeableness,
conscientiousness, emotional stability, and culture. We have
used these headings to guide our analysis of the conversational
agents’ personality traits in this review. We also aimed to
identify and analyze the patterns in the description of
conversational agents pertaining to personality traits. Multiple
codes were sometimes assigned to the same agent where
necessary, but this was limited to a maximum of 3 codes to
maintain some degree of specificity.
Results
Search Findings
The initial database searches yielded 11,401 records, and another
28 records were retrieved through additional sources such as
the gray literature sources and screening of reference lists of
relevant studies. A total of 196 duplicates were identified and
removed, leaving 11,233 titles and abstracts that needed to be
screened. Title and abstract screening led to the exclusion of
11,099 records, resulting in 134 full texts that needed to be
assessed for eligibility. Of these, 87 articles were excluded,
resulting in a final pool of 47 reports comprising 45 studies and
2 ongoing trials (Figure 2).
J Med Internet Res 2020 | vol. 22 | iss. 8 | e17158 | p. 4
http://www.jmir.org/2020/8/e17158/
(page number not for citation purposes)
Tudor Car et al
JOURNAL OF MEDICAL INTERNET RESEARCH
XSL•FO
RenderX

## Page 5

Figure 2. PRISMA flow chart.
Characteristics of Included Studies
In this scoping review, 40 included studies were from
high-income countries (HICs) and 6 were from low- and
middle-income countries (LMICs). A total of 22 studies were
from European countries, including Italy [44,45], Switzerland
[30,46-52], France [53,54], Portugal [55], The Netherlands [56],
the United Kingdom [57-61], Spain [62,63], and Sweden [64].
Moreover, 8 studies originated from Asian countries: Philippines
[65], China [66], Japan [67,68], Pakistan [69], India [70,71],
and Hong Kong [72]. Other geographic regions acknowledged
in the studies of this review were Australia [73,74], Canada
[75], New Zealand [76,77], South Africa [78], and the United
States of America [79-89].
A variety of study designs were used in the included studies,
comprising
20
case
studies
[44,48,51,61-63,66,69,71,
73-79,82,84,85,89], 4 surveys [55,56,59,65], 3 observational
studies
[53,86,87],
11
randomized
controlled
trials
[46,49,50,57,64,67,72,80,81,83,88], 3 diagnostic accuracy
studies [58,60,68], 3 controlled before and after studies
[30,45,70], 2 ongoing trials [51,54], and 1 pilot study [47]
(Figure 3).
J Med Internet Res 2020 | vol. 22 | iss. 8 | e17158 | p. 5
http://www.jmir.org/2020/8/e17158/
(page number not for citation purposes)
Tudor Car et al
JOURNAL OF MEDICAL INTERNET RESEARCH
XSL•FO
RenderX

## Page 6

Figure 3. Bubble plots showing the distribution of identified study designs, types of conversational agents and healthcare topics in the included articles,
plotted against the year of the publication. The scale on the right indicates that the size of the bubble is associated with the number of studies whereby
the smallest denotes 1 study and the largest, 10 studies.
The types of literature included 25 journal articles
[44,48,55-57,61-65,67,69,72,74-76,80-87,89], 11 conference
abstracts [45,47,49,50,52,59,70,71,73,78,79], 4 conference
papers [30,46,66,77], 1 poster abstract [68], 4 electronic
preprints [53,58,60,88], and 2 clinical trial protocols [51,54].
There was an increase in the number of publications each year,
from 3 in 2015 to 5 in 2016, 10 in 2017, and 23 in 2018. Some
author groups were highly productive and published at least
two papers within 2 years. Kowatsch et al published 3 papers
between 2017 and 2018 based on their open source behavioral
intervention platform MobileCoach, which allows the authors
to design a text-based health care conversational agent for
obesity management and behavior change [30,46,90]. Griol et
al published articles on conversational agent for chronic
conditions, including chronic pulmonary disease [63] and
Alzheimer disease [62] in 2015 and 2016, respectively. Such
productive teams reiterate the research interest in this area of
conversational agents. Furthermore, the high frequency of
publication indicates the feasibility and support to conduct
research successfully in this area.
Characteristics of Conversational Agents in the
Included Studies
Conversational Agent Delivery Channel
Conversational agents were delivered through a variety of means
in the included studies. Most (n=23) were smartphone apps
[30,46-50,53,55,58-61,64,67,70,71,75,77,81,83,85,86,88]; web
based (n=5) [57,66,73,74,82]; desktop computer based (n=2)
[65,79]; used smartphone-embedded software (n=6; eg, Siri,
Google Assistant, Alexa, etc) [44,51,62,76,84,87], Telegram
[45,78], WeChat [72], SMS and multimedia messaging service
[89], Windows live messenger [56], or Facebook Messenger
[52,80]; and 4 were made available on more than 1 platform
[53,59,68,83]. Three studies did not specify the method of
conversational agent delivery [54,63,69].
Technical Development Approach
A total of 8 studies made a reference to the technical details of
the conversational agent development process. Some mentioned
specific tools such as C and MS Access [65]. Others discussed
the application of well-known concepts, to conversational agent
development such as using the Computers are Social Actors
paradigm to develop a health advice conversational agent, or
converting the structure association technique (SAT) into digital
SAT for implementation on a LINE platform [67,83]. Some
emphasized data set creation and sources for the knowledge
base [44]. Four studies provided an in-depth workflow with a
step-by-step explanation of the technical development of the
conversational agent. Cheng et al [79] provided a very detailed
technical explanation of the development process—broken down
and explained in parts: program development on Google’s home
device, webhook and internal logic, and web interface. Galescu
et al [82] described the CARDIAC system architecture including
a knowledge base, task models, dialogue management, speech
recognition, and language generation. Griol et al [63] presented
a spoken dialogue system with specific details of the proposed
emotion recognizer. For example, it considers pitch, frequency,
energy, and rhythm of speech input from the user. Joerin et al
[75] provided a less technically dense explanation for chatbot
conversational agent development but mentioned technologies
used in the process, such as emotion algorithms and machine
learning techniques [75].
Input and Output Modalities
The conversational agents could be categorized according to
whether the user input was fixed (ie, predetermined text) or
unrestricted (ie, free text/speech). A total of 10 studies employed
fixed text user inputs [30,46,47,49,50,52,54,58,83,88], with 2
additional studies enabling fixed text and image inputs [67,68].
Moreover, 19 studies allowed free text user inputs
[45,48,51,56,57,60,61,66,69,70,72,74,77,78,80,81,85,86,89],
and 4 studies used both fixed and free text user inputs
J Med Internet Res 2020 | vol. 22 | iss. 8 | e17158 | p. 6
http://www.jmir.org/2020/8/e17158/
(page number not for citation purposes)
Tudor Car et al
JOURNAL OF MEDICAL INTERNET RESEARCH
XSL•FO
RenderX

## Page 7

[53,64,65,73].
Speech
was
enabled
in
8
studies
[44,55,63,71,76,79,82,84], whereas free text and speech were
employed in 3 studies [62,75,87]. The method of user input was
unspecified in 1 study [59] (Multimedia Appendix 2).
Similarly, output modalities largely employed text alone (n=30)
[45-47,49-51,53,54,56-58,60,61,64-66,68-70,72-74,77,78,80,81,83,85,88,89];
text and speech (n=5) [48,55,63,71,87]; speech alone (n=4)
[44,79,82,84]; text and images (n=4) [30,67,75,86]; text, speech,
and images [62]; or text, speech, images, and videos [52,76].
The input and output methods were not specified in 1 of the
studies [59] (Multimedia Appendix 2).
Conversational Agent Personality
We condensed the descriptive terms used in individual studies
to present the conversational agents into a list of 9 relevant
personality traits as presented in Table 1.
The conversational agents in the included studies were health
care professional like [57,58,62,66,71,73,74,86], informal
[46,52,53,56,61,65,81,85], coach like [47,49,52,64,66,70,80],
knowledgeable [56,60,68,72,89], human like [48,78,79,88],
culture specific [47,48,53], factual [68,76], gender specific
[46,78], and some identified explicitly as a conversational agent
[46,65].
One article [78] reported on a conversational agent personality
that was criticized for being overly formal, and some articles
did not report on the personality of the conversational agent at
all [30,44,45,50,51,54,55,59,63,67,69,75,77,82-84,87].
Table 1. Personality codes derived for the conversational agents included in this review, adapted from Haan et al.
Descriptions
Personality codes
Encouraging, motivating, and nurturing
Coach like
Explicitly identifies as a conversational agent
Conversational agent identity
Speaks the native language or has native names
Culture specific
Nonjudgmental, no personal opinions, and responses based on facts or
observations
Factual
Male and female versions available
Gender specific
Designed to be a doctor or expert, that is, mimics a health care professional
Health care professional like
Tries to emulate humans, for example, participants reported feeling like
they were talking to another human or researchers used features like
“typing” to make the conversation more human like
Human like
Informal, like talking to a friend. Uses exclamations, abbreviations, and
emoticons
Informal
Content created or informed by medical experts
Knowledgeable
Human Involvement
A health care administrator or professional was available via
the conversational agent for the user to communicate with in
some studies. The role of the human varied from an
administrator who could be contacted via a dedicated chat
channel for the user to ask questions or an individual whose
role was to monitor the user’s activity on the conversational
agent and provide personalized feedback to them. Seven studies
[30,46,47,70,72,78,85] reported on human involvement in the
conversation and the remaining articles did not.
Conversational Agent Goals
All the conversational agents in this review were identified as
goal oriented. Goal-oriented conversational agents have a clearly
defined end point and are employed to execute a specific
function, unlike chit chat agents that have no specific end goal,
do not delve into the details of any topic, and have a primary
aim of merely keeping the conversation going [91].
Goal-oriented conversational agents were further divided into
those that yielded long- or short-term outcomes. Of the included
studies, 22 articles focused on conversational agents with
long-term goals and 23 with short-term goals (Multimedia
Appendix 3 [30,44-89]). Two studies reported on conversational
agents with both short-term and long-term goals [45,56], for
example, answering immediate queries (short) and providing
education and increasing users’ knowledge on the topic over
time (long) [56]. Conversational agents with short-term scope
provided users with a response or service almost instantaneously,
such as answering health-related queries [84]. Conversely, those
with long-term scope needed to build a relationship with the
user, over time, to help them overcome health-related issues
such as smoking cessation [72] or working through a mental
health problem [80].
Conversational Agent Content Analysis
Five distinct themes were identified in terms of conversational
agent content: treatment and monitoring (ie, treatment
implementation, management, adherence, support, and
monitoring), health service support (ie, connecting patients to
health care services), education (ie, provision of health
care–related information), lifestyle behavior change (ie,
supporting users in tackling various modifiable health risk
factors), and diagnosis (ie, identification of the nature of a
disease or a condition). A number of included conversational
J Med Internet Res 2020 | vol. 22 | iss. 8 | e17158 | p. 7
http://www.jmir.org/2020/8/e17158/
(page number not for citation purposes)
Tudor Car et al
JOURNAL OF MEDICAL INTERNET RESEARCH
XSL•FO
RenderX

## Page 8

agents spanned several different themes (Multimedia
Appendices 3 and 4 [30,44-89]).
Treatment and Monitoring
Overall, 17 articles reported on conversational agents that
focused on treatment, monitoring, or rehabilitation of patients
with specific conditions. One study reported on a conversational
agent to help preserve cognitive abilities in those with Alzheimer
disease [62]. Two other studies focused on conversational agents
to provide support and treatment for metabolic conditions such
as type 2 diabetes [70] and obesity [46]. Eight studies presented
conversational agents for managing mental health using
techniques such as counseling [67]; cognitive behavioral therapy
(CBT) [64,80] method of levels therapy [57]; positive
psychology [61]; provision of a virtual companion [66]; and a
combination of modalities such as CBT with mindfulness-based
therapy, emotionally focused therapy, and motivational
interviewing [75,81]. One study each reported on the use of a
conversational agent for monitoring patients with asthma [85],
HIV [45], heart failure [82], and chronic respiratory disease
management [63]. Non–disease-specific conversational agents
were used as a health information advisor [83] and pediatric
generic medicine consultant [65].
Health Care Services Support
Overall, 19 studies reported on conversational agents used to
support or complement existing health care services. These
tasks included remote delivery of health care services for mental
health support [67,75,81], breast cancer [53,54], dysarthria [44],
obesity [50], diabetes management [79], chronic respiratory
diseases [63], asthma [85], heart failure [82], and HIV
management [45]. Other studies discussed conversational agents
automating health care services such as patient history taking
[48,77], providing health advice [83], symptom checking [58],
and triaging and diagnosis support [60,69,74].
Education
We found 13 articles in which conversational agents were used
primarily for educating patients or users. Education focused on
topics such as sexual health [59,76] including information on
HIV [78], overcoming unhealthy habits such as alcohol misuse
[73] and smoking cessation [72], improving well-being [88],
diabetes management [79], breast cancer [53,54], and
medication-related queries [55] as well as general health
[56,84,87], which covered more than 1 topic of focus, for
example, education on sex, drugs, and alcohol for adolescents.
Lifestyle Behavioral Changes
We identified 12 studies with conversational agents for healthy
lifestyle behavior change in the general population as well as
overweight and obese individuals. Two studies discussed
conversational agents for the management of obesity in younger
patients, including adolescents [46,50]. They largely employed
a coach-like conversational agent to promote physical activity
[51] and healthy eating [52], sometimes with incentive
provision, and provided techniques on how to reverse obesity
[30,47,49,71]. Other behavioral change interventions used a
social media–driven conversational agent for smoking cessation
[72], a health coach for diabetes prevention [86], a reflection
companion to encourage physical activity in adults [89], and
emotionally intelligent agents to improve mental health [61]
and well-being [88].
Diagnosis
Seven articles presented health care conversational agents with
a primary purpose of establishing a diagnosis. Three articles
reported on conversational agents’ triage, diagnosis, or a
combination of both, mainly employing a symptom checker
function [58,60,74]. Three more studies reported purely on the
diagnostic accuracy of 2 conversational agents [69,71,77]. One
article reported on a conversational agent for diagnosing
sexually transmitted infections to overcome barriers such as
social stigma, embarrassment, and discomfort associated with
traditional diagnostic approaches that require a medical
interview with a health care professional [68].
Conversational Agent Evaluation
Included studies that evaluated conversational agents reported
on their accuracy (in terms of information retrieval, diagnosis,
and triaging), user acceptability, and effectiveness. Some studies
reported on more than 1 outcome, for example, acceptability
and effectiveness. In general, evaluation data were mostly
positive, with a few studies reporting the shortcomings of the
conversational agent or technical issues experienced by users.
Seventeen studies presented self-reported data from participants
in the form of surveys, questionnaires, etc. In 16 studies, the
data were objectively assessed in the form of changes in BMI,
number of user interactions, etc. In 12 studies, there was a
mixture of self-reported and objectively assessed outcomes and
outcomes were not reported in the two ongoing trials
(Multimedia Appendix 4).
Accuracy: Information, Diagnosis, and Triaging
Eleven studies reported on the accuracy of conversational agents
[44,58,60,66,68,69,71,74,76,77,82] (Multimedia Appendix 4).
Middleton et al [58] and Razzaki et al [60] evaluated 2 versions
of the Babylon conversational agent, respectively: Babylon
check and Babylon chatbot for triage and diagnosis. In both
studies, the conversational agents were tested on their triage
and diagnostic accuracy using clinical vignettes as in the
Membership of the Royal College of General Practitioners
exams, and their performance was compared with that of
doctors. The conversational agents were found to be more
accurate, faster, and provided safer triage and diagnosis
compared with doctors and nurses. Similarly, Ghosh et al [74]
and Danda et al [71] assessed conversational agents on their
general diagnostic accuracy, and these had a precision rate of
82% and 86%, respectively. Ni et al [77] assessed Chatbot
MANDY, designed to automate patient intake, on its ability to
adequately diagnose the patient based on their symptoms. There
was a prediction accuracy of 100%, 64%, 25%, and 14% for
respiratory issues, chest pain, headache, and dizziness,
respectively [77]. Furthermore, 2 studies tested the accuracy of
conversational agents employed for sexual health purposes
[68,76]. The conversational agent used by Kobori et al [68]
diagnosed sexually transmitted infections with an accuracy of
77.7% and had high effectiveness (97.7%) in encouraging
patients to visit the clinic earlier. In contrast, Wilson et al [76]
compared smart assistants—Google Assistant, Siri, and Google
J Med Internet Res 2020 | vol. 22 | iss. 8 | e17158 | p. 8
http://www.jmir.org/2020/8/e17158/
(page number not for citation purposes)
Tudor Car et al
JOURNAL OF MEDICAL INTERNET RESEARCH
XSL•FO
RenderX

## Page 9

search—to determine their accuracy in responding to queries
around sexual health. The Google search option was found to
provide the best answers and also had the lowest failure rate
[76]. Another study compared 3 known virtual assistants—Siri,
Google Assistant, and Amazon Alexa—on their abilities to
recognize speech from individuals with dysarthria [44]. They
all performed similarly (50-60% recognition), with Siri being
the only agent attempting to parse all the dialogue inputted [44].
Two studies discussed the accuracy of 2 conversational agents
in making diagnoses in children and adolescents [66,69].
Teenchat had a 78.34% precision rate in diagnosing stress [66],
whereas Aquabot had an accuracy of 85%, 86.64%, and 87.2%
(3 groups aged 18-28 years) for achluophobia and 88%, 87.6%,
and 87.53% (3 patient groups aged 1-7 years) for autism [69].
Finally, Galescu et al [82] discussed the accuracy of a
conversational agent CARDIAC in speech recognition for heart
failure patients. A significant number of errors were detected
and attributed to insufficient vocabulary coverage in the
language model as evidenced by an out-of-vocab rate of 3%
[82].
Effectiveness
The effectiveness of health care conversational agents was
assessed in 8 studies [47,52,57,61,70,75,81,84]. Furthermore,
10 studies reported on the effectiveness and acceptability, of
which 5 are presented here [49,64,67,80,86] and the remainder
are presented under Acceptability (Multimedia Appendix 4).
Five studies described conversational agents targeting a healthy
lifestyle change specifically for healthy eating [52], active
lifestyle [49], obesity [47], and diabetes management [70,86].
Casas et al [52] reported improvements in food consumption,
whereas Stasinaki [47] and Heldt et al [49] noted increases in
physical activity performance with high compliance. Shaikh et
al [70] reported successful reduction in HbA1c (glycated
hemoglobin) levels postengagement with Wellthy diabetes,
whereas Stein et al [86] reported successful weight loss (2.38%)
and satisfaction was high, rated at 87% for the diabetes
prevention chatbot.
Eight studies noted the effectiveness of conversational agents
for mental health applications [57,61,64,67,75,80,81,84]. The
conversational agent Tess by Fulmer et al [81] initiated a
statistically significant improvement in depression and anxiety
compared with the control group. Two studies looked at the use
of machine learning–based conversational agents for CBT in
young adults [64,80]. The conversational agent was both
effective (reduced levels of depression and perceived stress and
improved psychological well-being) and well received (high
engagement with the chat app and high levels of satisfaction)
[64,80]. This positive effect was reproduced by Joerin et al [75],
where emotional support from Tess decreased symptoms of
anxiety and depression by 18% and 13%, respectively [75].
Inkster et al [61] employed the Patient Health Questionnaire-9
self-reported depression scale to note significant improvements
in depression scores in the high user group compared with the
low user group [61]. In addition, 67.7% of users found the app
usage to be helpful and encouraging [61]. In the study by Kamita
et al [67], the counseling bot encouraged significant
improvements in users’ self-esteem, anxiety, and depression
compared with the control condition. Besides effectiveness,
user ratings of acceptability, using the technology acceptance
model, were higher in the conversational agent condition
compared with the control [67]. Gaffney et al [57] proposed a
conversational agent MYLO that was significantly better than
the existing conversational agent ELIZA in problem solving
and helpfulness, but both were equally effective in lowering
distress. Miner et al [84] compared Apple’s Siri, Microsoft’s
Cortana, Samsung’s S Voice, and Google Now on their abilities
to respond to questions about mental health, interpersonal
violence, and physical health. Siri responded appropriately and
empathetically to issues concerning depression and physical
health, and Cortana responded appropriately and empathetically
to matters involving interpersonal violence [84].
Acceptability
A total of 26 studies commented on the acceptability of
conversational agents (Multimedia Appendix 4). Five studies
commenting on acceptability and effectiveness were discussed
above [49,64,67,80,86] (see the Effectiveness section), and the
remaining
21
studies
are
presented
here
[30,45,46,48,50,53,55,56,59,62,63,65,72,73,78,79,83,85,87-89].
Several studies (n=6) were targeted at children or adolescents.
Three studies discussed conversational agents for health
education on medication, asthma management, drugs, sex, and
alcohol [56,65,85]. Acceptability was generally denoted by high
response rates and scores like strongly agree or agree for
user-friendliness, appropriateness, consistency, and speed of
response [65]. In addition, users in the study by Crutzen et al
[56] favored the conversational agent over existing methods of
information provision. In another 3 studies, conversational
agents were employed for the management of obesity in
adolescents [30,46,50]. Acceptability was high in all studies,
as evidenced by enjoyment of the chats; bonding; formation of
social and emotional relationships; and high perceived ease of
use, usefulness, and intention to use [30,46,50]. In the study by
L’Allemand et al [50], high compliance was attributed to the
rewarding game system.
In 4 studies, health care conversational agents were targeted at
chronic conditions [55,62,63,79]. The specific conditions
addressed were Alzheimer disease, diabetes, heart failure, and
chronic respiratory disease. In the study by Cheng et al [79],
users responded positively, particularly to features of
conversational agents that allowed for personalization and the
conversational agent’s ability to understand and respond to
natural conversation flow. Some difficulties included learning
commands, restricted answer options, slow processing speed,
and some problematic responses [79]. Lobo et al [55] reported
user acceptability in the form of usability, where the
conversational agent had a system usability score of 88, which
was considered very good. Griol et al [62] considered the
Alzheimer patients’ caregiver’s perspective when judging the
acceptability of the conversational agent. The global rate for
the system (on a scale from 0 to 10) was 8.6, and the application
was thought to be attractive, adequate, and appropriate for its
purpose. In another study, Griol et al [63] employed an
emotionally sensitive conversational agent for chronic
respiratory disease patients who rated this agent significantly
higher for interaction rate, frequency, and empathy than the
baseline version.
J Med Internet Res 2020 | vol. 22 | iss. 8 | e17158 | p. 9
http://www.jmir.org/2020/8/e17158/
(page number not for citation purposes)
Tudor Car et al
JOURNAL OF MEDICAL INTERNET RESEARCH
XSL•FO
RenderX

## Page 10

A further 3 studies were concerned with sexual health and/or
HIV management [45,59,78]. They indicated that in this field,
conversational agents could be used for a variety of functions
such as booking an appointment, getting test results, therapy,
and event reminders [45]. In addition, the conversational agent
in the study by van Heerden et al [78] was well received when
used as a counseling tool because it was given an avatar-like
profile image and the conversation was embedded in a familiar
chat interface, which users associated with talking to another
human being. In the study by Nadarzynski et al [59], users
favored the conversational agent because of its ubiquity as a
convenient smartphone app and its ability to perform remote
services such as video consultation, potentially alleviating any
inhibitions users may have around discussing sexual health in
person.
Two studies employed an emotionally sensitive conversational
agent for mental health counselling and general health
information advice [83,88]. In the study by Liu et al [83], the
sympathetic conversational agent was rated more positively
than the advice-only condition. Another conversational agent
for well-being improvement procured positive feedback from
participants who thought it was an interesting experience, pretty
quick, and fun [88].
In 3 studies, conversational agents were used for healthy
behavior change, specifically targeting smoking cessation,
alcohol misuse treatment, and physical activity promotion
[72,73,89]. For smoking cessation, participants indicated
enjoyment when conversing with the conversational agent, and
effectiveness was also insinuated by 38.3% reporting not having
smoked in the past week and 69.4% admitting to a reduction in
smoking frequency [72]. In the study by Elmasri et al [73], the
participants (young adults) reported a higher satisfaction rate
with the use of the conversational agent to manage and treat
alcohol misuse. For physical activity promotion through the use
of a reflection companion, response rates were high (96% at
baseline, 90% at follow-up), insinuating high engagement
throughout the study. Furthermore, use of the system beyond
the stipulated study period was an indicator of viability.
Moreover, 16 of the 33 participants opted to continue without
any reward, suggesting participants found some added value in
using the conversational system [89].
Two studies examined the acceptability of conversational agents
for health care service delivery [48,87]. Outcomes were reported
qualitatively, including comments on ease of use, humanity of
the chatbot, and users’ comfort with the input functionalities
available to them as well as criticisms on technical difficulties
[48]. Bickmore et al [87] more specifically compared
conversational assistants Siri, Alexa, and Google Assistant on
their provision of health information and found satisfaction to
be lowest with Alexa and highest with Siri. Overall, there was
a neutral rating for satisfaction, with a median score of 4 (IQR
1-6) [87].
One study discussed a condition-specific conversational agent
application targeted at improving the quality of life and
medication adherence of breast cancer patients [53]. Participants
implied a positive experience when interacting with the
conversational agent, whereby 88% said it provided them with
support in tracking their treatment and mentioned that they
would recommend the conversational agent to their friends.
There was an overall satisfaction of 94% [53].
Discussion
Principal Findings
Our scoping review identified 45 studies and 2 ongoing clinical
trials. Although conversational agents have been widely
employed in various fields, their use in health care is still in its
infancy, as evidenced by the study findings that indicate much
of the literature being published recently (2016-2018). Most
conversational agents used text input and were machine learning
based and mobile app delivered. The 3 most commonly reported
themes in the health care conversational agent–related literature
were treatment and monitoring, health services support, and
patient education. Results from the studies evaluating
conversational agents were generally positive, reporting
effectiveness, accuracy, and acceptability of the conversational
agent. However, there is currently a dearth of robust evaluations
and a predominance of small case studies.
Our review shows that most of the health care conversational
agents reported in the literature used machine learning and were
long-term goal oriented. This suggests that conversational agents
are evolving from conducting simple transactional tasks toward
more involved end points such as long-term disease management
[80] and behavior change [30]. The majority of the
conversational agents identified in this review targeted patients,
with only a few aimed at health care professionals, for example,
by automating patient intake or aiding in patient triage and
diagnosis. In addition, research into the use of conversational
agents to support both formal and informal caregivers is limited
and could be a productive area to explore, given that previous
systematic reviews on the use of digital technology for
caregivers of patients with psychosis [92] or dementia [93] have
shown positive outcomes.
Our findings show a predominance of text-based conversational
agents, with only a few apps using speech as the main mode of
communication. Yet, certain populations, such as older people,
may be more comfortable interacting via speech, as some
individuals may find the dexterity involved with typing on small
keypads on smartphones challenging and time consuming.
Furthermore, most conversational agents included in our review
were app based. Research shows that the use of apps (which
need to be downloaded and regularly updated) is often associated
with high dropout rates and low utilization [94]. Such
disadvantages do not seem to apply to messaging apps such as
Facebook Messenger, iMessage, Telegram, WeChat, or
WhatsApp, which are already commonly used in the general
population. Future research should aim to overcome this
limitation brought on by smartphone apps by embedding future
health care conversational agents in platforms, which the target
population already uses regularly. The advantage of having
numerous publishing platform options is the novelty of
conversational agents over smartphone apps, and this should
be further explored.
J Med Internet Res 2020 | vol. 22 | iss. 8 | e17158 | p. 10
http://www.jmir.org/2020/8/e17158/
(page number not for citation purposes)
Tudor Car et al
JOURNAL OF MEDICAL INTERNET RESEARCH
XSL•FO
RenderX

## Page 11

A recent systematic review on the effectiveness of ECAs and
other conversational agents noted a lack of an established
method for evaluating health care conversational agents in health
care and a dearth of data on adverse effects [32]. This
corresponds to our findings, with most studies being case studies
and lacking information on potential adverse effects. Side effects
to consider may relate to the content of the conversational agent
conversations, which may not be accurate, evidence based, or
suitable for the specific circumstance. For example, if a mental
health conversational agent user has suicidal tendencies, the
conversational agent may not be best equipped to handle such
a situation and may provide inappropriate advice, leaving the
user at fatal risk. Additional unwanted effects could arise from
the black box effect associated with the use of machine
learning–based conversational agents, whereby their suggestions
are somewhat unpredictable [95]. Furthermore, conversational
agents allowing for free text input may lead to significant
privacy concerns, especially for vulnerable populations, as
individuals can share private and sensitive data in conversations
[96]. There is a need for stringent certification from a regulatory
board in cases where conversational agents are given roles akin
to health care professionals.
The health care sectors for conversational agent application
identified in the review were generally very broad, with
references to only a few specialties including mental health
[97], neurodegeneration [62], metabolic medicine (obesity [47]
and diabetes [70,79]), and sexual health [68]. Future applications
could expand toward other health care fields where evidence
has suggested potential for digital health interventions such as
dermatology [98], primary care [99], geriatrics [100], and
oncology [101].
There is also a need for more geographically diverse research.
Although our review identified 12 articles with a geographical
focus in Asia, the evidence stemming from middle-income
countries was scarce, and there were no studies from a
low-income country. However, digital health initiatives are
becoming more common in developing countries, often with a
different, context-specific scope, such as ensuring access to
health care using social media [102]. To ensure safe and
effective use of solutions developed in HIC settings, there is a
need for more research to corroborate the safety, effectiveness,
and acceptability of these agents in LMICs too. Furthermore,
it is important to explore the integration of conversational agents
into the existing health systems and services. A hybrid system,
where digital technology supplements health care services, is
increasingly seen as the optimal solution [103]. This mirrors
our acknowledgment that conversational agents will be most
advantageous in supporting rather than substituting health care
professionals. In most studies, conversational agents were
developed and presented independently, unsupported by humans,
and separate from the existing health care delivery models,
which may prove unsustainable in the long run. Future research
should consider evaluating hybrid systems encompassing
conversational agents in their health care delivery, as reported
in some of the included studies where conversational agents
were complemented by frequent meetings and phone calls with
the physicians.
Although the studies reported accuracy, efficacy, effectiveness,
and acceptability as outcomes, there were no measurements of
cost, efficiency, or how the solution led to improved productivity
when used instead of or to augment the work of a health
professional. Therefore, it was not possible to ascertain whether
the solutions developed were cost-effective compared with
alternative approaches.
Strengths and Limitations
We conducted a comprehensive literature search of multiple
databases, including gray literature sources. We prioritized
sensitivity over specificity in our search strategy to capture a
holistic representation of conversational agent usage uptake in
health care. However, given the novelty of the field and the
employed terminology, some unpublished studies discussed at
niche conferences or meetings may have been omitted.
Furthermore, although classification of the themes of our
conversational agents was based on thorough analysis, team
discussions, and consensus, it might not be all inclusive and
may require further development with the advent of new
conversational agents. In addition, although some conversational
agents belong to more than 1 theme, we mostly classified them
based on the dominant mode of application for the sake of
clarity. Finally, we excluded articles with poorly reported data
on chatbot assessments; therefore, we may have missed some
health care conversational agents (Multimedia Appendix 5
[36,97,104-188]). We decided to exclude these because they
did not appear to contribute anything additional or noteworthy
to our review. The personality traits presented were guided by
a reference paper on chatbot personality assignment [43] and
also a condensation of descriptive terms from several articles.
The lack of depth and breadth in the description of the content
and development of many conversational agents led us to
organically develop a framework for this paper. This framework
is, therefore, still exploratory and adapted to suit the purposes
of this review and may well be explored and further refined
with more in-depth analysis such as previously published
frameworks [189].
Conclusions
Conversational agents are an up-and-coming form of technology
to be used in health care, which has yet to be robustly assessed.
Most conversational agents reported in the literature to date are
text based, machine learning driven, and mobile app delivered.
Future research should focus on assessing the feasibility,
acceptability, safety, and effectiveness of diverse conversational
agent formats aligned with the target population’s needs and
preferences. There is also a need for clearer guidance on health
care –related conversational agents’development and evaluation
and further exploration on the role of conversational agents
within existing health systems.
J Med Internet Res 2020 | vol. 22 | iss. 8 | e17158 | p. 11
http://www.jmir.org/2020/8/e17158/
(page number not for citation purposes)
Tudor Car et al
JOURNAL OF MEDICAL INTERNET RESEARCH
XSL•FO
RenderX

## Page 12

Acknowledgments
This research is supported by the Ageing Research Institute for Society and Education (ARISE), Nanyang Technological University,
Singapore. This study is also supported by the National Research Foundation, Prime Minister’s Office, Singapore under its
Campus for Research Excellence and Technological Enterprise (CREATE) program.
Authors' Contributions
LTC conceived the idea for this study. DD, BK, and LC screened the articles. DD, BK, and LC extracted and analyzed the data.
DD and LC wrote the manuscript. BK, TK, JR, RA, and YLT revised the manuscript critically.
Conflicts of Interest
TK is affiliated with the Center for Digital Health Interventions, a joint initiative of the Department of Management, Technology,
and Economics at ETH Zurich and the Institute of Technology Management at the University of St. Gallen, which is funded in
part by the Swiss health insurer CSS. TK is also a cofounder of Pathmate Technologies, a university spin-off company that creates
and delivers digital clinical pathways. Other authors declare that they have no competing interests.
Multimedia Appendix 1
Search strategy.
[DOCX File , 18 KB-Multimedia Appendix 1]
Multimedia Appendix 2
Types of user input (blue) and output (green) in the conversational agents.
[DOCX File , 32 KB-Multimedia Appendix 2]
Multimedia Appendix 3
Characteristics of conversational agents reported in the included studies.
[DOCX File , 44 KB-Multimedia Appendix 3]
Multimedia Appendix 4
Characteristics of included studies.
[DOCX File , 45 KB-Multimedia Appendix 4]
Multimedia Appendix 5
List of excluded studies and reasons for exclusion.
[DOCX File , 30 KB-Multimedia Appendix 5]
References
1.
Chatbot. Oxford Living Dictionaries. 1990. URL: https://en.oxforddictionaries.com/definition/chatbot [accessed 2020-07-18]
2.
Veretskaya O. What is a Chatbot and How to Use It for Your Business. Medium. 2017. URL: https://medium.com/swlh/
what-is-a-chatbot-and-how-to-use-it-for-your-business-976ec2e0a99f [accessed 2020-07-18]
3.
Smart Speaker Sales More Than Tripled in 2017. Billboard. 2017. URL: https://www.billboard.com/articles/business/
8085524/smart-speaker-sales-tripled-25-million-year-2017 [accessed 2020-07-18]
4.
Perez S. 39 Million Americans Now Own a Smart Speaker, Report Claims. Tech Crunch. 2018. URL: https://techcrunch.
com/2018/01/12/39-million-americans-now-own-a-smart-speaker-report-claims/ [accessed 2020-07-18]
5.
Smart Speakers 2018: World Market Forecast to 2023 - Key Vendors Covered include Alphabet, Amazon, Harman Intl,
Alibaba and Sonos. Cision PR Newswire. 2018. URL: https://www.prnewswire.com/news-releases/
smart-speakers-2018-world-market-forecast-to-2023---key-vendors-covered-include-alphabet-amazon-harman-intl-alibaba-and-sonos-300676460.
html [accessed 2020-07-18]
6.
Saeed H. Developing a Chatbot? Learn the Difference between AI, Machine Learning, and NLP. Chatbots Life. 2016. URL:
https://chatbotslife.com/developing-a-chatbot-learn-the-difference-between-ai-machine-learning-and-nlp-40a3f745aec4
[accessed 2020-07-18]
7.
Seeman P. Natural language generation: an overview. J Comput Sci Res 2012;1(3):50-57 [FREE Full text] [doi:
10.1093/oxfordhb/9780199276349.013.0015]
8.
What is a Chatbot? All You Need to Know About Chatbots!. Botpress: Open-Source Conversational AI Platform. 2018.
URL: https://botpress.io/learn/what-and-why/ [accessed 2020-07-18] [WebCite Cache ID 746pXZ3d7]
J Med Internet Res 2020 | vol. 22 | iss. 8 | e17158 | p. 12
http://www.jmir.org/2020/8/e17158/
(page number not for citation purposes)
Tudor Car et al
JOURNAL OF MEDICAL INTERNET RESEARCH
XSL•FO
RenderX

## Page 13

9.
Understanding the ‘Black Box’of Artificial Intelligence. Reddit. 2018. URL: https://www.reddit.com/r/artificial/comments/
9iapbc/understanding_the_black_box_of_artificial/ [accessed 2020-07-18] [WebCite Cache ID 746puKdDT]
10.
Lewis C, Monnet D. AI and Machine Learning Black Boxes: The Need for Transparency and Accountability. KDnuggets
News. 2017. URL: https://www.kdnuggets.com/2017/04/ai-machine-learning-black-boxes-transparency-accountability.
html [accessed 2020-07-18]
11.
Holm EA. In defense of the black box. Science 2019 Apr 5;364(6435):26-27. [doi: 10.1126/science.aax0162] [Medline:
30948538]
12.
Weizenbaum J. ELIZA---a computer program for the study of natural language communication between man and machine.
Commun ACM 2012;9(1):36-45. [doi: 10.1145/365153.365168]
13.
Deryugina OV. Chatterbots. Sci Tech Inf Proc 2010 Sep 5;37(2):143-147. [doi: 10.3103/s0147688210020097]
14.
The History of Chatbots. Futurism: Science and Technology News and Videos. 2016. URL: https://futurism.com/images/
the-history-of-chatbots-infographic/ [accessed 2020-07-21]
15.
Colby K. Artificial Paranoia: A Computer Simulation of Paranoid Processes. New York, USA: Elsevier; 2013.
16.
McTear M, Callejas Z, Griol D. The Conversational Interface: Talking to Smart Devices. Switzerland: Springer International
Publishing; 2016.
17.
Rose Medical Center. Letting fingers do the talking. Computer makes patient satisfaction surveys a snap. Rose Medical
Center, Denver, CO. Profiles Healthc Mark 1992(48):40-44. [Medline: 10120010]
18.
Delichatsios HK, Friedman RH, Glanz K, Tennstedt S, Smigelski C, Pinto BM, et al. Randomized trial of a 'talking computer'
to improve adults' eating habits. Am J Health Promot 2001;15(4):215-224. [doi: 10.4278/0890-1171-15.4.215] [Medline:
11349340]
19.
Friedman E. Your friendly neighborhood diagnosis-aiding talking computer. Hospitals 1981 Oct 16;55(20):105-6, 108,
113. [Medline: 7275074]
20.
Friedman RB, Newsom RS, Entine SM, Cheung S, Schultz JV. A simulated patient-physician encounter using a talking
computer. J Am Med Assoc 1977 Oct 31;238(18):1927-1929. [Medline: 578551]
21.
Migneault JP, Farzanfar R, Wright JA, Friedman RH. How to write health dialog for a talking computer. J Biomed Inform
2006 Oct;39(5):468-481 [FREE Full text] [doi: 10.1016/j.jbi.2006.02.009] [Medline: 16564749]
22.
Mayo J. 2016: The Year When Chatbots Were Hot. Chatbots Life. 2016. URL: https://chatbotslife.com/
2016-the-year-when-chatbots-were-hot-3d61046527f9 [accessed 2020-07-18]
23.
Bruner J. Why 2016 is Shaping Up to Be the Year of the Bot. O’Reilly Media Inc. 2016. URL: https://www.oreilly.com/
ideas/why-2016-is-shaping-up-to-be-the-year-of-the-bot [accessed 2020-07-18]
24.
Goebel T. 2016 – The Year of the Chatbot. Aspect Blog. 2016. URL: https://blogs.aspect.com/2016-the-year-of-the-chatbot/
[accessed 2020-07-18]
25.
Stormon A. The Uncomfortable Truth About Bots: 3 Reasons Why They’re Failing Miserably. Chatbots Magazine. 2017.
URL: https://chatbotsmagazine.com/3-uncomfortable-reasons-why-chatbots-are-failing-8913901a29e5 [accessed 2020-07-18]
26.
Prize L. Mitsuku Wins 2019 Loebner Prize and Best Overall Chatbot at AISB X. AISB – The Society for the Study of
Artificial Intelligence and Simulation of Behaviour. 2019. URL: https://aisb.org.uk/new_site/?p=350 [accessed 2020-07-18]
27.
Neville R, Greene A, McLeod J, Tracey A, Tracy A, Surie J. Mobile phone text messaging can help young people manage
asthma. Br Med J 2002 Sep 14;325(7364):600 [FREE Full text] [doi: 10.1136/bmj.325.7364.600/a] [Medline: 12228151]
28.
Hall AK, Cole-Lewis H, Bernhardt JM. Mobile text messaging for health: a systematic review of reviews. Annu Rev Public
Health 2015 Mar 18;36:393-415 [FREE Full text] [doi: 10.1146/annurev-publhealth-031914-122855] [Medline: 25785892]
29.
Rathbone AL, Prescott J. The use of mobile apps and SMS messaging as physical and mental health interventions: systematic
review. J Med Internet Res 2017 Aug 24;19(8):e295 [FREE Full text] [doi: 10.2196/jmir.7740] [Medline: 28838887]
30.
Kowatsch T, Volland D, Shih I, Rüegger D, Künzler F, Barata F. Design and Evaluation of a Mobile Chat App for the
Open Source Behavioral Health Intervention Platform MobileCoach. In: Chatbots International Conference on Design
Science Research in Information System and Technology. 2017 Presented at: DESRIST 2017; May 30-June 1, 2017;
Karlsruhe, Germany. [doi: 10.1007/978-3-319-59144-5_36]
31.
Tropea P, Schlieter H, Sterpi I, Judica E, Gand K, Caprino M, et al. Rehabilitation, the great absentee of virtual coaching
in medical care: scoping review. J Med Internet Res 2019 Oct 1;21(10):e12805 [FREE Full text] [doi: 10.2196/12805]
[Medline: 31573902]
32.
Laranjo L, Dunn AG, Tong HL, Kocaballi AB, Chen J, Bashir R, et al. Conversational agents in healthcare: a systematic
review. J Am Med Inform Assoc 2018 Sep 1;25(9):1248-1258 [FREE Full text] [doi: 10.1093/jamia/ocy072] [Medline:
30010941]
33.
Kocaballi AB, Berkovsky S, Quiroz JC, Laranjo L, Tong HL, Rezazadegan D, et al. The personalization of conversational
agents in health care: systematic review. J Med Internet Res 2019 Nov 7;21(11):e15360 [FREE Full text] [doi: 10.2196/15360]
[Medline: 31697237]
34.
Provoost S, Lau HM, Ruwaard J, Riper H. Embodied conversational agents in clinical psychology: a scoping review. J
Med Internet Res 2017 May 9;19(5):e151 [FREE Full text] [doi: 10.2196/jmir.6553] [Medline: 28487267]
35.
Pereira J, Díaz O. Using health chatbots for behavior change: a mapping study. J Med Syst 2019 Apr 4;43(5):135. [doi:
10.1007/s10916-019-1237-1] [Medline: 30949846]
J Med Internet Res 2020 | vol. 22 | iss. 8 | e17158 | p. 13
http://www.jmir.org/2020/8/e17158/
(page number not for citation purposes)
Tudor Car et al
JOURNAL OF MEDICAL INTERNET RESEARCH
XSL•FO
RenderX

## Page 14

36.
Hoermann S, McCabe KL, Milne DN, Calvo RA. Application of synchronous text-based dialogue systems in mental health
interventions: systematic review. J Med Internet Res 2017 Jul 21;19(8):e267 [FREE Full text] [doi: 10.2196/jmir.7023]
[Medline: 28784594]
37.
Vaidyam AN, Wisniewski H, Halamka JD, Kashavan MS, Torous JB. Chatbots and conversational agents in mental health:
a review of the psychiatric landscape. Can J Psychiatry 2019 Jul;64(7):456-464 [FREE Full text] [doi:
10.1177/0706743719828977] [Medline: 30897957]
38.
Montenegro J, da Costa CA, da Rosa Righi R. Survey of conversational agents in health. Expert Syst Appl 2019 Sep
7;129(11):56-67. [doi: 10.1016/j.eswa.2019.03.054]
39.
Xing Z, Yu F, Du J, Walker JS, Paulson CB, Mani NS, et al. Conversational interfaces for health: bibliometric analysis of
grants, publications, and patents. J Med Internet Res 2019 Nov 18;21(11):e14672 [FREE Full text] [doi: 10.2196/14672]
[Medline: 31738171]
40.
Peters MD, Godfrey CM, Khalil H, McInerney P, Parker D, Soares CB. Guidance for conducting systematic scoping
reviews. Int J Evid Based Healthc 2015 Sep;13(3):141-146. [doi: 10.1097/XEB.0000000000000050] [Medline: 26134548]
41.
Embodied Conversational Agent. Chatbots. URL: https://www.chatbots.org/embodied_conversational_agent/ [accessed
2020-07-18]
42.
Bickmore T. Relational Agents. Northeastern University. URL: http://www.ccs.neu.edu/home/bickmore/agents/ [accessed
2020-07-18]
43.
de Haan H, Snijder J, van Nimwegen C, Beun R. Chatbot Personality and Customer Satisfaction. Info Support Research.
2018. URL: https://research.infosupport.com/wp-content/uploads/
Chatbot-Personality-and-Customer-Satisfaction-Bachelor-Thesis-Information-Sciences-Hayco-de-Haan.pdf [accessed
2020-07-18]
44.
Ballati F, Corno F, de Russis L. 'Hey Siri, do you understand me?': Virtual Assistants and Dysarthria. In: 7th International
Workshop on the Reliability of Intelligent Environments. 2018 Presented at: WoRIE'18; June 25-28, 2018; Rome, Italy
URL: https://www.researchgate.net/publication/
325466714_Hey_Siri_do_you_understand_me_Virtual_Assistants_and_Dysarthria
45.
Vita S, Marocco R, Pozzetto I, Morlino G, Vigilante E, Palmacci V. The 'doctor apollo' chatbot: a digital health tool to
improve engagement of people living with HIV. J Int AIDS Soc 2018 Oct;21(Suppl 8):e25187 [FREE Full text] [doi:
10.1002/jia2.25187] [Medline: 30362663]
46.
Kowatsch T, Nißen M, Shih C, Rüegger D, Volland D, Filler A. Text-Based Healthcare Chatbots Supporting Patient and
Health Professional Teams: Preliminary Results of a Randomized Controlled Trial on Childhood Obesity. In: 17th
International Conference on Intelligent Virtual Agents. 2017 Presented at: IVA'17; August 27-30, 2017; Stockholm, Sweden
URL: https://tinyurl.com/yxpmarws
47.
Stasinaki A, Brogle B, Buchter D, Shih CHI, Heldt K, White C, et al. A novel digital health intervention improves physical
performance in obese youth. Swiss Medical Weekly 2018 May;148:10s-10s [FREE Full text]
48.
Denecke K, Hochreutener SL, Pöpel A, May R. Self-anamnesis with a conversational user interface: concept and usability
study. Methods Inf Med 2018 Nov;57(5-06):243-252. [doi: 10.1055/s-0038-1675822] [Medline: 30875703]
49.
Heldt K, Buchter D, Brogle B, Shih C, Ruegger D, Filler A. Telemedicine therapy for overweight adolescents: first results
of a novel smartphone app intervention using a behavioural health platform. Obesity Facts 2018 May 11(Suppl 1):214-215
[FREE Full text]
50.
L'Allemand D, Shih C, Heldt K, Buchter D, Brogle B, Ruegger D. Design and interim evaluation of a smartphone app for
overweight adolescents using a behavioural health intervention platform. Obesity Reviews 2018 Dec 19(Suppl 1):102.
51.
Can a smartphone app that includes a chatbot-based coaching and incentives increase physical activity in healthy adults?
Clinical Trials. 2017. URL: https://clinicaltrials.gov/ct2/show/NCT03384550 [accessed 2020-07-18]
52.
Casas J, Mugellini E, Abou Khaled O. Food Diary Coaching Chatbot. In: Proceedings of the 2018 ACM International Joint
Conference and 2018 International Symposium on Pervasive and Ubiquitous Computing and Wearable Computers. 2018
Presented at: UbiComp'18; October 8-12, 2018; Singapore p. 1676-1680. [doi: 10.1145/3267305.3274191]
53.
Chaix B, Bibault JE, Pienkowski A, Delamon G, Guillemassé A, Nectoux P, et al. When chatbots meet patients: one-year
prospective study of conversations between patients with breast cancer and a chatbot. JMIR Cancer 2019 May 2;5(1):e12856
[FREE Full text] [doi: 10.2196/12856] [Medline: 31045505]
54.
Artificial Intelligence vs Physicians for Breast Cancer Patients' Information. Clinical Trials. 2018. URL: https://clinicaltrials.
gov/ct2/show/NCT03556813 [accessed 2018-07-18]
55.
Lobo J, Ferreira L, Ferreira A. CARMIE: a conversational medication assistant for heart failure. Int J E-Health Med Commun
2017;8(4):21-37. [doi: 10.4018/ijehmc.2017100102]
56.
Crutzen R, Peters GJ, Portugal SD, Fisser EM, Grolleman JJ. An artificially intelligent chat agent that answers adolescents'
questions related to sex, drugs, and alcohol: an exploratory study. J Adolesc Health 2011 May;48(5):514-519. [doi:
10.1016/j.jadohealth.2010.09.002] [Medline: 21501812]
57.
Gaffney H, Mansell W, Edwards R, Wright J. Manage Your Life Online (MYLO): a pilot trial of a conversational
computer-based intervention for problem solving in a student sample. Behav Cogn Psychother 2014 Nov;42(6):731-746.
[doi: 10.1017/S135246581300060X] [Medline: 23899405]
J Med Internet Res 2020 | vol. 22 | iss. 8 | e17158 | p. 14
http://www.jmir.org/2020/8/e17158/
(page number not for citation purposes)
Tudor Car et al
JOURNAL OF MEDICAL INTERNET RESEARCH
XSL•FO
RenderX

## Page 15

58.
Middleton K, Butt M, Hammerla N, Hamblin S, Mehta K, Parsa A. Sorting out symptoms: design and evaluation of the
'babylon check' automated triage system. Cornell University. URL: https://arxiv.org/abs/1606.02041 [accessed 2020-07-22]
59.
Nadarzynski T, Miles O, Cowie A, Ridge D. Acceptability of artificial intelligence (AI)-led chatbot services in healthcare:
a mixed-methods study. Digit Health 2019;5:2055207619871808 [FREE Full text] [doi: 10.1177/2055207619871808]
[Medline: 31467682]
60.
Razzaki S, Baker A, Perov Y, Middleton K, Baxter J, Mullarkey D, et al. A comparative study of artificial intelligence and
human doctors for the purpose of triage and diagnosis. Cornell University. URL: https://arxiv.org/abs/1806.10698 [accessed
2020-07-22]
61.
Inkster B, Sarda S, Subramanian V. An empathy-driven, conversational artificial intelligence agent (Wysa) for digital
mental well-being: real-world data evaluation mixed-methods study. JMIR Mhealth Uhealth 2018 Nov 23;6(11):e12106
[FREE Full text] [doi: 10.2196/12106] [Medline: 30470676]
62.
Griol D, Callejas Z. Mobile conversational agents for context-aware care applications. Cogn Comput 2015 Aug
21;8(2):336-356. [doi: 10.1007/s12559-015-9352-x]
63.
Griol D, Molina JM, Callejas Z. Towards Emotionally Sensitive Conversational Interfaces for E-therapy. In: Artificial
Computation in Biology and Medicine: International Work-Conference on the Interplay Between Natural andArtificial
Computation, IWINAC 2015, Elche, Spain, June 1-5, 2015, Proceedings, Part I. Berlin: Springer; 2015.
64.
Ly KH, Ly AM, Andersson G. A fully automated conversational agent for promoting mental well-being: a pilot RCT using
mixed methods. Internet Interv 2017 Dec;10:39-46 [FREE Full text] [doi: 10.1016/j.invent.2017.10.002] [Medline: 30135751]
65.
Comendador BE, Francisco BB, Medenilla JS, Mae S. Pharmabot: A Pediatric Generic Medicine Consultant Chatbot.
Journal of Automation and Control Engineering. 2015. URL: http://www.joace.org/index.
php?m=content&c=index&a=show&catid=42&id=218 [accessed 2020-07-22]
66.
Huang J, Li Q, Xue Y, Cheng T, Xu S, Jia J, et al. TeenChat: A Chatterbot System for Sensing and Releasing Adolescents’
Stress. In: International Conference on Health Information Science. Heidelberg: Springer; May 2015:133-145.
67.
Kamita T, Ito T, Matsumoto A, Munakata T, Inoue T. A Chatbot System for Mental Healthcare Based on SAT Counseling
Method. Mobile Information Systems 2019 Mar 03;2019(2):1-11. [doi: 10.1155/2019/9517321]
68.
Kobori Y, Osaka A, Soh S, Okada H. MP15-03 Novel application for sexual transmitted infection screening with an AI
chatbot. J Urol 2018 Apr 03;199(4S):1-11. [doi: 10.1016/j.juro.2018.02.516]
69.
Mujeeb S, Hafeez M, Arshad T. Aquabot: a diagnostic chatbot for achluophobia and autism. Int J Adv Comput Sci Appl
2017 Dec;8(9):39-46. [doi: 10.14569/IJACSA.2017.080930]
70.
Sosale A, Shaikh M, Shah A, Chawla R, Makkar B, Kesavadev J, et al. Real-world effectiveness of a digital therapeutic in
improving glycaemic control in south asians living with type 2 diabetes. Diabetes 2018 May;67(Supplement 1):866-P-86640.
[doi: 10.2337/db18-866-P]
71.
Danda P, Srivastava BML, Shrivastava M. Vaidya: A Spoken Dialog System for Health Domain. In: Proceedings of the
13th International Conference on Natural Language Processing. 2015 Presented at: International Conference on Natural
Language Processing; 2016; Varanasi, India.
72.
Wang H, Zhang Q, Ip M, Fai Lau J. Social media–based conversational agents for health management and interventions.
Computer 2018 Aug 03;51(8):26-33. [doi: 10.1109/MC.2018.3191249]
73.
Elmasri D, Maeder A. A Conversational Agent for an Online Mental Health Intervention. In: Brain Informatics and Health.
Cham: Springer; Sep 23, 2016.
74.
Ghosh S, Bhatia S, Bhatia A. Quro: facilitating user symptom check using a personalised chatbot-oriented dialogue system.
Stud Health Technol Inform 2018;252:51-56. [Medline: 30040682]
75.
Joerin A, Rauws M, Ackerman ML. Psychological artificial intelligence service, Tess: delivering on-demand support to
patients and their caregivers: technical report. Cureus 2019 Jan 28;11(1):e3972 [FREE Full text] [doi: 10.7759/cureus.3972]
[Medline: 30956924]
76.
Wilson N, MacDonald EJ, Mansoor OD, Morgan J. In bed with Siri and Google Assistant: a comparison of sexual health
advice. BMJ 2017 Dec 13;359:j5635. [doi: 10.1136/bmj.j5635] [Medline: 29237603]
77.
Ni L, Lu C, Liu N, Liu J. MANDY: towards a smart primary care chatbot application. In: Knowledge and Systems Sciences.
Heidelberg: Springer; 2017.
78.
van Heerden A, Ntinga X, Vilakazi K. The potential of conversational agents to provide a rapid HIV counseling and testing
services. In: International Conference on the Frontiers and Advances in Data Science (FADS). 2016 Presented at: 2017
International Conference on the Frontiers and Advances in Data Science (FADS); 2017; Xi'an, China. [doi:
10.1109/FADS.2017.8253198]
79.
Cheng A, Raghavaraju V, Kanugo J, Handrianto YP. Development and evaluation of a healthy coping voice interface
application using the Google home for elderly patients with type 2 diabetes. 2018 Presented at: 15th IEEE Annual Consumer
Communications & Networking Conference; Jan, 12-15; Las Vegas, NV, USA. [doi: 10.1109/CCNC.2018.8319283]
80.
Fitzpatrick KK, Darcy A, Vierhile M. Delivering cognitive behavior therapy to young adults with symptoms of depression
and anxiety using a fully automated conversational agent (Woebot): a randomized controlled trial. JMIR Ment Health 2017
Jun 06;4(2):e19 [FREE Full text] [doi: 10.2196/mental.7785] [Medline: 28588005]
J Med Internet Res 2020 | vol. 22 | iss. 8 | e17158 | p. 15
http://www.jmir.org/2020/8/e17158/
(page number not for citation purposes)
Tudor Car et al
JOURNAL OF MEDICAL INTERNET RESEARCH
XSL•FO
RenderX

## Page 16

81.
Fulmer R, Joerin A, Gentile B, Lakerink L, Rauws M. Using psychological artificial intelligence (Tess) to relieve symptoms
of depression and anxiety: randomized controlled trial. JMIR Ment Health 2018 Dec 13;5(4):e64 [FREE Full text] [doi:
10.2196/mental.9782] [Medline: 30545815]
82.
Galescu L, Allen J, Ferguson G, Quinn J, Swift M. Speech recognition in a dialog system for patient health monitoring.
2009 Presented at: 2009 IEEE International Conference on Bioinformatics and Biomedicine Workshops; November 1-4,
2009; Washington, DC, USA. [doi: 10.1109/BIBMW.2009.5332111]
83.
Liu B, Sundar SS. Should machines express sympathy and empathy? Experiments with a health advice chatbot. Cyberpsychol
Behav Soc Netw 2018 Oct;21(10):625-636. [doi: 10.1089/cyber.2018.0110] [Medline: 30334655]
84.
Miner AS, Milstein A, Schueller S, Hegde R, Mangurian C, Linos E. Smartphone-based conversational agents and responses
to questions about mental health, interpersonal violence, and physical health. JAMA Intern Med 2016 May 01;176(5):619-625
[FREE Full text] [doi: 10.1001/jamainternmed.2016.0400] [Medline: 26974260]
85.
Rhee H, Allen J, Mammen J, Swift M. Mobile phone-based asthma self-management aid for adolescents (mASMAA): a
feasibility study. Patient Prefer Adherence 2014;8:63-72 [FREE Full text] [doi: 10.2147/PPA.S53504] [Medline: 24470755]
86.
Stein N, Brooks K. A fully automated conversational artificial intelligence for weight loss: longitudinal observational study
among overweight and obese adults. JMIR Diabetes 2017 Nov 01;2(2):e28 [FREE Full text] [doi: 10.2196/diabetes.8590]
[Medline: 30291087]
87.
Bickmore TW, Trinh H, Olafsson S, O'Leary TK, Asadi R, Rickles NM, et al. Patient and consumer safety risks when using
conversational assistants for medical information: an observational study of Siri, Alexa, and google assistant. J Med Internet
Res 2018 Sep 04;20(9):e11510 [FREE Full text] [doi: 10.2196/11510] [Medline: 30181110]
88.
Ghandeharioun A, McDuff D, Czerwinski M, Rowan K. EMMA: An Emotionally Intelligent Personal Assistant for
Improving Wellbeing. Researchgate. URL: https://www.researchgate.net/publication/
330035444_EMMA_An_Emotionally_Intelligent_Personal_Assistant_for_Improving_Wellbeing [accessed 2020-07-22]
89.
Kocielnik R, Xiao L, Avrahami D, Hsieh G. Reflection Companion: a conversational system for engaging users in reflection
on physical activity. Proc ACM Interact Mob Wearable Ubiquitous Technol 2018 Jul 05;2(2):1-26. [doi: 10.1145/3214273]
90.
Kowatsch T, Nißen M, Rüegger D, Stieger M, Flückiger C, Allemand M. The impact of interpersonal closeness cues in
text-based healthcare chatbots on attachment bond and the desire to continue interacting: an experimental design. University
of Zurich. URL: https://www.zora.uzh.ch/id/eprint/158352/1/
Kowatsch%2520et%2520al%25202018%2520InterPersCloseness-of-THCB.pdf [accessed 2020-07-22]
91.
ReDial: Recommendation dialogs for bridging the gap between chit-chat and goal-oriented chatbots. Microsoft. URL:
https://www.microsoft.com/en-us/research/blog/
redial-recommendation-dialogs-for-bridging-the-gap-between-chit-chat-and-goal-oriented-chatbots/ [accessed 2020-07-22]
92.
Onwumere J, Amaral F, Valmaggia LR. Digital technology for caregivers of people with psychosis: systematic review.
JMIR Ment Health 2018 Sep 05;5(3):e55 [FREE Full text] [doi: 10.2196/mental.9857] [Medline: 30185402]
93.
Ruggiano N, Brown EL, Li J, Scaccianoce M. Rural Dementia Caregivers and Technology: What Is the Evidence? Res
Gerontol Nurs 2018 Jul 01;11(4):216-224. [doi: 10.3928/19404921-20180628-04] [Medline: 30036405]
94.
Lee K, Kwon H, Lee B, Lee G, Lee JH, Park YR, et al. Effect of self-monitoring on long-term patient engagement with
mobile health applications. PLoS One 2018;13(7):e0201166 [FREE Full text] [doi: 10.1371/journal.pone.0201166] [Medline:
30048546]
95.
Coiera E. Paper Review: the Babylon Chatbot. Wordpress. URL: https://coiera.com/2018/06/29/
paper-review-the-babylon-chatbot/ [accessed 2020-07-22]
96.
Thompson D, Baranowski T. Chatbots as extenders of pediatric obesity intervention: an invited commentary on 'Feasibility
of Pediatric Obesity & Pre-Diabetes Treatment Support through Tess, the AI Behavioral Coaching Chatbot'. Transl Behav
Med 2019 May 16;9(3):448-450. [doi: 10.1093/tbm/ibz065] [Medline: 31094432]
97.
D'Alfonso S, Santesteban-Echarri O, Rice S, Wadley G, Lederman R, Miles C, et al. Artificial intelligence-assisted online
social therapy for youth mental health. Front Psychol 2017;8:796 [FREE Full text] [doi: 10.3389/fpsyg.2017.00796]
[Medline: 28626431]
98.
Spinazze P, Bottle A, Car J. Digital health sensing for personalized dermatology. Sensors (Basel) 2019 Aug 5;19(15):3426.
[doi: 10.3390/s19153426] [Medline: 31387237]
99.
Pal K, Dack C, Ross J, Michie S, May C, Stevenson F, et al. Digital health interventions for adults with type 2 diabetes:
qualitative study of patient perspectives on diabetes self-management education and support. J Med Internet Res 2018 Jan
29;20(2):e40 [FREE Full text] [doi: 10.2196/jmir.8439]
100. Bhattarai P, Phillips JL. The role of digital health technologies in management of pain in older people: an integrative review.
Arch Gerontol Geriatr 2017;68:14-24. [doi: 10.1016/j.archger.2016.08.008]
101. Devine KA, Viola AS, Coups EJ, Wu YP. Digital health interventions for adolescent and young adult cancer survivors.
JCO Clin Cancer Inform 2018;2:1-15. [doi: 10.1200/CCI.17.00138]
102. Amrita DB. Health care social media: expectations of users in a developing country. Med 2 0 2013;2(2):e4 [FREE Full
text] [doi: 10.2196/med20.2720] [Medline: 25075239]
103. Kerr D, Axelrod C, Hoppe C, Klonoff DC. Diabetes and technology in 2030: a utopian or dystopian future? Diabet Med
2018 Apr;35(4):498-503. [doi: 10.1111/dme.13586] [Medline: 29356078]
J Med Internet Res 2020 | vol. 22 | iss. 8 | e17158 | p. 16
http://www.jmir.org/2020/8/e17158/
(page number not for citation purposes)
Tudor Car et al
JOURNAL OF MEDICAL INTERNET RESEARCH
XSL•FO
RenderX

## Page 17

104. Mascitti I, Feituri M, Funghi F, Correnti S. COACH BOT: Modular e-course with virtual coach tool support. In: Proceedings
of the International Conference on Agents and Artificial Intelligence. 2010 Jul 01 Presented at: International Conference
on Agents and Artificial Intelligence; 2010; January, 22-24. [doi: 10.5220/0002589901150120]
105. Abashev A, Grigoryev R, Grigorian K, Boyko V. Programming tools for messenger-based chatbot system organization:
implication for outpatient and translational medicines. BioNanoSci 2016 Nov 22;7(2):403-407. [doi:
10.1007/S12668-016-0376-9]
106. Ahmad NS, Sanusi MH, Abd Wahab MH, Mustapha A, Sayadi ZA, Saringat MZ. Conversational bot for pharmacy: a
natural language approach. 2018 Presented at: 2018 IEEE Conference on Open Systems (ICOS ); 21-22 Nov, 2018; Langkawi
Island, Malaysia, Malaysia. [doi: 10.1109/ICOS.2018.8632700]
107. Alexander JA. Computer assisted optometry--a tutorial with examples. Am J Optom Arch Am Acad Optom 1973
Sep;50(9):730-736. [doi: 10.1097/00006324-197309000-00007] [Medline: 4584475]
108. Chatbots Meet eHealth: Automatizing Healthcare. University of Naples. URL: http://ceur-ws.org/Vol-1982/paper6.pdf
[accessed 2020-07-22]
109. Atay C, Ireland D, Liddle J, Wiles J, Vogel A, Angus D, et al. P3-404: can a smartphone-based chatbot engage older
community group members? The impact of specialised content. Alzheimers Demen 2016 Jul 01;12:P1005-P1006. [doi:
10.1016/j.jalz.2016.06.2070]
110. Improving adherence in automated e-coaching. In: Persuasive Strategies To Improve Driving Behaviour Of Elderly Drivers
By A Feedback Approach. Cham: Springer; 2016.
111. Brixey J, Hoegen R, Lan W, Rusow J, Singla K, Yin X. Shihbot: A facebook chatbot for sexual health information on
hiv/aids. In: Proceedings of the 18th Annual SIGdial Meeting on Discourse and Dialogue. 2017 Presented at: 18th Annual
SIGdial Meeting on Discourse and Dialogue Cite this publication; 2017; Saarbrücken, Germany. [doi: 10.18653/v1/W17-5544]
112. Callejas Z, Griol D, McTear F, López-Cózar R. A virtual coach for active ageing based on sentient computing and m-health.
Ambient Assisted Living and Daily Activities 2014:-. [doi: 10.1007/978-3-319-13105-4_10]
113. Cameron G, Cameron D, Megaw G, Bond R, Mulvenna M, O'Neill S. Towards a chatbot for digital counselling. In:
Proceedings of the 31st British Computer Society Human Computer Interaction Conference. 2017 Presented at: 31st British
Computer Society Human Computer Interaction Conference; 3-6 July, 2017; University of Sunderland, UK. [doi:
10.14236/ewic/HCI2017.24]
114. Cameron G, Cameron D, Megaw G, Bond R. Best Practices for Designing Chatbots in Mental Healthcare–A Case Study
on iHelpr. In: Proceedings of the 32nd International BCS Human Computer Interaction Conference. 2018 Presented at:
British HCI Conference 2018; 2018; Belfast. [doi: 10.14236/ewic/HCI2018.129]
115. Chung K, Park RC. Chatbot-based heathcare service with a knowledge base for cloud computing. Cluster Comput 2018
Mar 16;22(S1):1925-1937. [doi: 10.1007/s10586-018-2334-5]
116. Cooper A, Ireland D. Designing a chat-bot for non-verbal children on the autism spectrum. Stud Health Technol Inform
2018;252:63-68. [Medline: 30040684]
117. Denecke K, Lutz Hochreutener S, Poepel A, May R. Talking to Ana: A Mobile Self-Anamnesis Application with
Conversational User Interface. Cluster Comput 2019 Jan;22(1):-. [doi: 10.1145/3194658.3194670]
118. Dharwadkar R, Deshpande NA. A Medical ChatBot. Int J Comp Trends Technol 2018;60(1):- [FREE Full text]
119. Divya S, Indumathi V, Ishwarya S, Priyasankari M, Devi SK. A self-diagnosis medical chatbot using artificial intelligence.
Journal of Web Development and Web Designing 2018;3(1):-.
120. Do HI, Fu WT. Empathic Virual Assistant for Healthcare Information with Positive Emotional Experience. 2016 Presented
at: 2016 IEEE International Conference on Healthcare Informatics; 2016; United States.
121. Dubosson F, Schaer R, Savioz R, Schumacher M. Going beyond the relapse peak on social network smoking cessation
programmes: ChatBot opportunities. Swiss Med Informatics 2017 Sep 20:-. [doi: 10.4414/smi.33.00397]
122. Fadhil A, Gabrielli S. Addressing challenges in promoting healthy lifestyles: the al-chatbot approach. In: Proceedings of
the 11th EAI International Conference on Pervasive Computing Technologies for Healthcare. 2017 Presented at: International
Conference on Pervasive Computing Technologies for Healthcare; May 23-26, 2017; Barcelona, Spain. [doi:
10.1145/3154862.3154914]
123. Fadhil A, Villafiorita A. An adaptive learning with gamification & conversational UIs: The rise of CiboPoliBot. 2017
Presented at: 25th Conference on User Modeling, Adaptation and Personalization; 9-12th July, 2017; Bratislava, Slovakia.
[doi: 10.1145/3099023.3099112]
124. Fadhil A, Diaconu M, Gabrielli S, Villafiorita A. CoachAI: A conversational UI assisted e-coaching platform. Cornell
Univeristy. 2017. URL: https://arxiv.org/abs/1904.11961 [accessed 2020-07-22]
125. Beyond Patient Monitoring: Conversational Agents Role in Telemedicine & Healthcare Support For Home-Living Elderly
Individuals. Cornell University. URL: https://arxiv.org/abs/1803.06000 [accessed 2020-07-22]
126. Can a Chatbot Determine My Diet?: Addressing Challenges of Chatbot Application for Meal Recommendation. Cornell
Univeristy. URL: https://arxiv.org/abs/1802.09100 [accessed 2020-07-22]
127. A Conversational Interface to Improve Medication Adherence: Towards AI Support in Patient's Treatment. Cornell University.
URL: https://arxiv.org/abs/1803.09844 [accessed 2020-07-22]
J Med Internet Res 2020 | vol. 22 | iss. 8 | e17158 | p. 17
http://www.jmir.org/2020/8/e17158/
(page number not for citation purposes)
Tudor Car et al
JOURNAL OF MEDICAL INTERNET RESEARCH
XSL•FO
RenderX

## Page 18

128. Fadhil A, Wang Y, Reiterer H. Assistive conversational agent for health coaching: a validation study. Methods Inf Med
2019 Jun;58(1):9-23. [doi: 10.1055/s-0039-1688757] [Medline: 31117129]
129. CARDIAC: An intelligent conversational assistant for chronic heart failure patient heath monitoring. Researchgate. URL:
https://www.researchgate.net/publication/
228374471_CARDIAC_An_intelligent_conversational_assistant_for_chronic_heart_failure_patient_heath_monitoring
[accessed 2020-07-22]
130. Ferguson G, Quinn J, Horwitz C, Swift M, Allen J, Galescu L. Towards a personal health management assistant. J Biomed
Inform 2010 Oct;43(5 Suppl):S13-S16 [FREE Full text] [doi: 10.1016/j.jbi.2010.05.014] [Medline: 20937478]
131. Implementation and feasibility study of a tailored health education bot in Telegram for mothers of children with obesity
and overweight. Researchgate. URL: https://tinyurl.com/y49e6xsj [accessed 2020-07-22]
132. From Books to Bots: Using Medical Literature to Create a Chat Bot. Researchgate. URL: https://www.researchgate.net/
publication/304358640_From_Books_to_Bots_Using_Medical_Literature_to_Create_a_Chat_Bot [accessed 2020-07-22]
133. SLOWBot (chatbot) Lifestyle Assistant. ACM Digital Library. URL: https://dl.acm.org/doi/10.1145/3240925.3240953
[accessed 2020-07-22]
134. Conversational System to Assist the User when Accessing Web Sources in the Medical Domain. ResearchGate. URL:
https://www.researchgate.net/publication/
261031810_Conversational_System_to_Assist_the_User_when_Accessing_Web_Sources_in_the_Medical_Domain
[accessed 2020-07-22]
135. Hassoon A, Schrack J, Naiman D, Lansey D, Baig Y, Stearns V, et al. Increasing physical activity amongst overweight and
obese cancer survivors using an alexa-based intelligent agent for patient coaching: protocol for the physical activity by
technology help (PATH) trial. JMIR Res Protoc 2018 Feb 12;7(2):e27 [FREE Full text] [doi: 10.2196/resprot.9096] [Medline:
29434016]
136. Allergybot: A chatbot technology intervention for young adults with food allergies dining out. Proceedings of the 2017
CHI Conference Extended Abstracts on Human Factors in Computing Systems. 2017. URL: https://www.semanticscholar.org/
paper/A-Conversational-System-to-Assist-the-User-when-Web-Gatius-Namsrai/b6e0f6874204f77fea2b57005470f17e1d5f8d3f
[accessed 2020-07-22]
137. Cooper A, Ireland D. Designing a chat-bot for non-verbal children on the autism spectrum. Stud Health Technol Inform
2018;252:63-68. [Medline: 30040684]
138. Chat-Bots for People with Parkinson's Disease: Science Fiction or Reality? Studies in health technology and informatics.
URL: https://www.researchgate.net/publication/
280726980_Chat-Bots_for_People_with_Parkinson's_Disease_Science_Fiction_or_Reality [accessed 2020-07-22]
139. Hello Harlie: Enabling Speech Monitoring Through Chat-Bot Conversations. Studies in health technology and informatics.
URL: https://www.researchgate.net/publication/
323104602_Hello_Harlie_Enabling_Speech_Monitoring_Through_Chat-Bot_Conversations [accessed 2020-07-22]
140. Kanagarajan K, Saradha A. An intelligent conversation agent for health care domain. IJSC 2014 Apr 01;4(3):772-776. [doi:
10.21917/ijsc.2014.0110]
141. Kramer JN, Künzler F, Mishra V, Presset B, Kotz D, Smith S, et al. Investigating intervention components and exploring
states of receptivity for a smartphone app to promote physical activity: protocol of a microrandomized trial. JMIR Res
Protoc 2019 Jan 31;8(1):e11540 [FREE Full text] [doi: 10.2196/11540] [Medline: 30702430]
142. Oh KJ, Lee DK, Ko BS, Hyeon J, Choi HJ. Empathy bot: conversational service for psychiatric counseling with chat
assistant. Stud Health Technol Inform 2017;245:1235. [Medline: 29295322]
143. Lee D, Oh KJ, Choi HJ. The chatbot feels you - a counseling service using emotional response generation. 2017 Presented
at: IEEE International Conference on Big Data and Smart Computing (BigComp); February 13-16, 2017; Jeju Island, Korea.
[doi: 10.1109/BIGCOMP.2017.7881752]
144. Lokman AS, Zain JM. One-match and all-match categories for keywords matching in chatbot. Am J Appl Sci 2010 Oct
01;7(10):1406-1411. [doi: 10.3844/ajassp.2010.1406.1411]
145. An architectural design of Virtual Dietitian (ViDi) for diabetic patients. IEEE Explore. 2009. URL: https://ieeexplore.
ieee.org/document/5234671?reload=true&arnumber=5234671 [accessed 2020-07-22]
146. Designing a Chatbot for diabetic patients. International Conference on Software Engineering & Computer Systems. URL:
https://www.researchgate.net/publication/266872926_Designing_a_Chatbot_for_Diabetic_Patients [accessed 2020-07-22]
147. A novel approach for medical assistance using trained chatbot. ResearchGate. URL: https://www.researchgate.net/publication/
318474956_A_novel_approach_for_medical_assistance_using_trained_chatbot [accessed 2020-07-22]
148. Marciel KK, Saiman L, Quittell LM, Dawkins K, Quittner AL. Cell phone intervention to improve adherence: cystic fibrosis
care team, patient, and parent perspectives. Pediatr Pulmonol 2010 Feb;45(2):157-164 [FREE Full text] [doi:
10.1002/ppul.21164] [Medline: 20054860]
149. The use of a chatbot in radiology education. European Society of Radiology. URL: https://epos.myesr.org/poster/esr/
ranzcr2018/R-0095 [accessed 2020-07-22]
J Med Internet Res 2020 | vol. 22 | iss. 8 | e17158 | p. 18
http://www.jmir.org/2020/8/e17158/
(page number not for citation purposes)
Tudor Car et al
JOURNAL OF MEDICAL INTERNET RESEARCH
XSL•FO
RenderX

## Page 19

150. Morris RR, Kouddous K, Kshirsagar R, Schueller SM. Towards an artificially empathic conversational agent for mental
health applications: system design and user perceptions. J Med Internet Res 2018 Jun 26;20(6):e10148 [FREE Full text]
[doi: 10.2196/10148] [Medline: 29945856]
151. A Chatbot for Psychiatric Counseling in Mental Healthcare Service Based on Emotional Dialogue Analysis and Sentence
Generation. IEEExplore. URL: https://ieeexplore.ieee.org/document/7962482 [accessed 2020-07-22]
152. Likita: A Medical Chatbot To Improve HealthCare Delivery In Africa. Extended Abstracts of the 2018 CHI Conference
on Human Factors in Computing Systems. URL: https://www.researchgate.net/publication/
330522151_Likita_A_Medical_Chatbot_To_Improve_HealthCare_Delivery_In_Africa [accessed 2020-07-22]
153. Chatbot Dimensions that Matter: Lessons from the Trenches. Web Engineering. URL: https://link.springer.com/chapter/
10.1007/978-3-319-91662-0_9 [accessed 2020-07-22]
154. Automated Medical Chatbot. SSRN. URL: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3090881 [accessed
2020-07-22]
155. Proposal for the development of a mobile virtual assistant for treatment of tuberculosis (2018). Repositório da Produção
USP. URL: https://repositorio.usp.br/item/002939130 [accessed 2020-07-22]
156. SleepBot: encouraging sleep hygiene using an intelligent chatbot. ResearchGate. URL: https://www.researchgate.net/
publication/331428159_SleepBot_encouraging_sleep_hygiene_using_an_intelligent_chatbot [accessed 2020-07-22]
157. HomeNL: Homecare Assistance in Natural Language. An Intelligent Conversational Agent for Hypertensive Patients
Management. Centre pour la Communication Scientifique Directe. URL: https://hal.archives-ouvertes.fr/inria-00519752/
[accessed 2020-07-22]
158. Chatbot Utilization for Medical Consultant System. IEEEXplore. URL: https://ieeexplore.ieee.org/document/8621678
[accessed 2020-07-22]
159. Sanative Chatbot For Health Seekers. International Journal of Engineering and Computer Science. URL: http://www.ijecs.in/
index.php/ijecs/article/view/720 [accessed 2020-07-22]
160. MamaBot: a System based on ML and NLP for supporting Women and Families during Pregnancy. Semantic Scholar.
URL: https://www.semanticscholar.org/paper/
MamaBot%3A-a-System-based-on-ML-and-NLP-for-Women-and-Vaira-Bochicchio/
c6ac5cdb449e1e08bc0321a675e88d95b1dc88b6 [accessed 2020-07-22]
161. Chatbots and Conversational Interfaces: Three Domains of Use. CEUR Workshop Proceedings. URL: http://ceur-ws.org/
Vol-2101/paper8.pdf [accessed 2020-07-22]
162. Blanson Henkemans OA, van der Boog PJ, Lindenberg J, van der Mast CA, Neerincx MA, Zwetsloot-Schonk BJ. An online
lifestyle diary with a persuasive computer assistant providing feedback on self-management. Technol Health Care
2009;17(3):253-267. [doi: 10.3233/THC-2009-0545] [Medline: 19641261]
163. Towards Fully Automated Psychotherapy for Adults - BAS - Behavioral Activation Scheduling Via Web and Mobile Phone.
Semantic Scholar. URL: https://www.semanticscholar.org/paper/
Towards-Fully-Automated-Psychotherapy-for-Adults-Griffioen-Both-Cuijpers/43b3c78317a273c7ec46c1696370bf68e42b30fb
[accessed 2020-07-22]
164. Allen J, Ferguson G, Blaylock N, Byron D, Chambers N, Dzikovska M, et al. Chester: towards a personal medication
advisor. J Biomed Inform 2006 Oct;39(5):500-513 [FREE Full text] [doi: 10.1016/j.jbi.2006.02.004] [Medline: 16545620]
165. Bickmore TW, Schulman D, Sidner C. Automated interventions for multiple health behaviors using conversational agents.
Patient Educ Couns 2013 Aug;92(2):142-148 [FREE Full text] [doi: 10.1016/j.pec.2013.05.011] [Medline: 23763983]
166. Evaluating Quality of Chatbots and Intelligent Conversational Agents. arXiv. URL: https://arxiv.org/ftp/arxiv/papers/1704/
1704.04579.pdf [accessed 2020-07-22]
167. Conversational Agents and Mental Health: Theory-Informed Assessment of Language and Affect. Stanford Univeristy.
URL: http://ilpubs.stanford.edu:8090/1141/1/healthDialog.pdf [accessed 2020-07-22]
168. Rizzo AA, Lange B, Buckwalter JG, Forbell E, Kim J, Sagae K, et al. An intelligent virtual human system for providing
healthcare information and support. Stud Health Technol Inform 2011;163:503-509. [Medline: 21335847]
169. Different measurements metrics to evaluate a chatbot system. ACM Digital Library. URL: https://dl.acm.org/doi/10.5555/
1556328.1556341 [accessed 2020-07-22]
170. Dr. Vdoc: A Medical Chatbot that Acts as a Virtual Doctor. Research & Reviews: Journal of Medical Science and Technology.
URL: http://medicaljournals.stmjournals.in/index.php/RRJoMST/article/view/30 [accessed 2020-07-22]
171. Kazi H, Chowdhry B, Memon Z. MedChatBot: an UMLS based chatbot for medical students. IJCA 2012 Oct 20;55(17):1-5.
[doi: 10.5120/8844-2886]
172. Coach Me: A Platform For Promoting Healthy Lifestyle. ResearchGate. URL: https://www.researchgate.net/publication/
307573372_Coach_Me_A_Platform_For_Promoting_Healthy_Lifestyle [accessed 2020-07-22]
173. Bickmore TW, Pfeifer LM, Byron D, Forsythe S, Henault LE, Jack BW, et al. Usability of conversational agents by patients
with inadequate health literacy: evidence from two clinical trials. J Health Commun 2010;15 Suppl 2:197-210. [doi:
10.1080/10810730.2010.499991] [Medline: 20845204]
J Med Internet Res 2020 | vol. 22 | iss. 8 | e17158 | p. 19
http://www.jmir.org/2020/8/e17158/
(page number not for citation purposes)
Tudor Car et al
JOURNAL OF MEDICAL INTERNET RESEARCH
XSL•FO
RenderX

## Page 20

174. Lindenberg K, Moessner M, Harney J, McLaughlin O, Bauer S. E-health for individualized prevention of eating disorders.
Clin Pract Epidemiol Ment Health 2011;7:74-83 [FREE Full text] [doi: 10.2174/1745017901107010074] [Medline:
21687562]
175. Dowling M, Rickwood D. Exploring hope and expectations in the youth mental health online counselling environment.
Comp Hum Behav 2016 Feb;55:62-68. [doi: 10.1016/j.chb.2015.08.009]
176. Dowling M, Rickwood D. Investigating individual online synchronous chat counselling processes and treatment outcomes
for young people. Adv Ment Health 2015 Jan 30;12(3):216-224. [doi: 10.1080/18374905.2014.11081899]
177. Dowling M, Rickwood D. A naturalistic study of the effects of synchronous online chat counselling on young people's
psychological distress, life satisfaction and hope. Couns Psychother Res 2015 Jul 14;15(4):274-283. [doi: 10.1002/capr.12037]
178. Azevedo RF, Morrow D, Graumlich J, Willemsen-Dunlap A, Hasegawa-Johnson M, Huang TS, et al. Using conversational
agents to explain medication instructions to older adults. AMIA Annu Symp Proc 2018;2018:185-194 [FREE Full text]
[Medline: 30815056]
179. Brown RL, McDermott RJ, Marty PJ. A conversational information computer system for health and safety operation: the
occupational surveillance interactive system (OSIS). Am Ind Hyg Assoc J 1981 Nov;42(11):824-830. [doi:
10.1080/15298668191420756] [Medline: 7315741]
180. Crutzen R, Bosma H, Havas J, Feron F. What can we learn from a failed trial: insight into non-participation in a chat-based
intervention trial for adolescents with psychosocial problems. BMC Res Notes 2014 Nov 20;7:824 [FREE Full text] [doi:
10.1186/1756-0500-7-824] [Medline: 25409911]
181. Denecke K, Tschanz M, Dorner TL, May R. Intelligent conversational agents in healthcare: hype or hope? Stud Health
Technol Inform 2019;259:77-84. [Medline: 30923277]
182. Designing for Health Chatbots. Cornell University. URL: https://arxiv.org/abs/1902.09022 [accessed 2020-07-22]
183. Mindbot: A Social-Based Medical Virtual Assistanta. IEEEXplore. URL: https://ieeexplore.ieee.org/document/
7776377?reload=true [accessed 2020-07-22]
184. Stieger M, Nißen M, Rüegger D, Kowatsch T, Flückiger C, Allemand M. PEACH, a smartphone- and conversational
agent-based coaching intervention for intentional personality change: study protocol of a randomized, wait-list controlled
trial. BMC Psychol 2018 Sep 04;6(1):43 [FREE Full text] [doi: 10.1186/s40359-018-0257-9] [Medline: 30180880]
185. Palanica A, Flaschner P, Thommandram A, Li M, Fossat Y. Physicians' perceptions of chatbots in health care: cross-sectional
web-based survey. J Med Internet Res 2019 Apr 05;21(4):e12887 [FREE Full text] [doi: 10.2196/12887] [Medline: 30950796]
186. Intelligent chatbot for analysis and diagnosis of the psychiatric disorders. ResearchGate. URL: https://www.researchgate.net/
publication/
329416982_INTELLIGENT_CHATBOT_FOR_ANALYSIS_AND_DIAGNOSIS_OF_THE_PSYCHIATRIC_DISORDERS
[accessed 2020-07-22]
187. Designing Just-in-time Adaptive Interventions and Healthcare Chatbots with the Open Source Platform MobileCoach.
University of St. Gallen. URL: https://www.alexandria.unisg.ch/255053/ [accessed 2020-07-22]
188. Chatbots and the new world of HCI. Interactions. URL: https://interactions.acm.org/archive/view/july-august-2017/
chatbots-and-the-new-world-of-hci [accessed 2020-07-22]
189. Garcia DM, Lopez SS, Donis H. Voice activated virtual assistants personality perceptions and desires- comparing personality
evaluation frameworks. 2018 Presented at: British Human Computer Interaction Conference; July 2018; Belfast. [doi:
10.14236/ewic/HCI2018.40]
Abbreviations
AI: artificial intelligence
CBT: cognitive behavioral therapy
ECA: embodied conversational agent
EMBASE: Excerpta Medica database
HIC: high-income country
LMIC: low- and middle-income country
MEDLINE: Medical Literature Analysis and Retrieval System Online
NLP: natural language processing
OCLC: Online Computer Library Center
SAT: structure association technique
J Med Internet Res 2020 | vol. 22 | iss. 8 | e17158 | p. 20
http://www.jmir.org/2020/8/e17158/
(page number not for citation purposes)
Tudor Car et al
JOURNAL OF MEDICAL INTERNET RESEARCH
XSL•FO
RenderX

## Page 21

Edited by G Eysenbach; submitted 22.11.19; peer-reviewed by A Kocaballi, E Judica; comments to author 09.12.19; revised version
received 11.04.20; accepted 13.06.20; published 07.08.20
Please cite as:
Tudor Car L, Dhinagaran DA, Kyaw BM, Kowatsch T, Joty S, Theng YL, Atun R
Conversational Agents in Health Care: Scoping Review and Conceptual Analysis
J Med Internet Res 2020;22(8):e17158
URL: http://www.jmir.org/2020/8/e17158/
doi: 10.2196/17158
PMID: 32763886
©Lorainne Tudor Car, Dhakshenya Ardhithy Dhinagaran, Bhone Myint Kyaw, Tobias Kowatsch, Shafiq Joty, Yin-Leng Theng,
Rifat Atun. Originally published in the Journal of Medical Internet Research (http://www.jmir.org), 07.08.2020. This is an
open-access
article
distributed
under
the
terms
of
the
Creative
Commons
Attribution
License
(https://creativecommons.org/licenses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium,
provided the original work, first published in the Journal of Medical Internet Research, is properly cited. The complete bibliographic
information, a link to the original publication on http://www.jmir.org/, as well as this copyright and license information must be
included.
J Med Internet Res 2020 | vol. 22 | iss. 8 | e17158 | p. 21
http://www.jmir.org/2020/8/e17158/
(page number not for citation purposes)
Tudor Car et al
JOURNAL OF MEDICAL INTERNET RESEARCH
XSL•FO
RenderX
