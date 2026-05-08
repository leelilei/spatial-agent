Title: A Survey on Large Language Model-Based Social Agents in Game-Theoretic Scenarios

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/survey_paper/pdfs/review_library/06_Feng2024_Social_Agents_Game_Theory_Survey.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T02:58:27+00:00
- page_count: 31
- status: ok
- text_char_count: 129991

Metadata:
- author: Xiachong Feng; Longxu Dou; Ella Li; Qinghao Wang; Haochuan Wang; Yu Guo; Chang Ma; Lingpeng Kong
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Introduction (page 1)
- Game Framework (page 4)
  - Choice-Focusing Game (page 4)
  - Communication-Focusing Game (page 6)
- Social Agent (page 8)
  - Preference Module (page 8)
  - Belief Module (page 9)
  - Reasoning Module (page 11)
  - PBR-Triangular Interaction (page 12)
- Evaluation Protocol (page 14)
  - Game-Agnostic Evaluation (page 14)
  - Game-Specific Evaluation (page 15)
  - Performance Assessment of Social Agents (page 15)
- Practical Guides for Researching Social Agents (page 17)
  - Design of Social Agent (page 17)
  - Evaluation of Social Agent (page 18)
- Future Directions (page 18)
  - Standardized Benchmark Generation (page 18)
  - Reinforcement Learning Agents (page 19)
  - Behaviour Pattern Mining (page 19)
  - Pluralistic Game-Theoretic Scenarios (page 20)
- Related Works (page 20)
- Conclusion (page 20)

Markdown Content:

Published in Transactions on Machine Learning Research (05/2025)
A Survey on Large Language Model-Based Social Agents
in Game-Theoretic Scenarios
Xiachong Fengµ Longxu Dous Ella Liαγ Qinghao Wangδ Haochuan Wangβ
Yu Guoβ Chang Maµ Lingpeng Kongµ
µThe University of Hong Kong sIndependent Researcher αNational University of Singapore
γInstitute for Infocomm Research (I2R), A*STAR δPeking University βHarbin Institute of Technology
fengxc@hku.hk,lpk@cs.hku.hk
Reviewed on OpenReview: https://openreview.net/forum?id=CsoSWpR5xC
Abstract
Game-theoretic scenarios have become pivotal in evaluating the social intelligence of Large
Language Model (LLM)-based social agents. While numerous studies have explored these
agents in such settings, there is a lack of a comprehensive survey summarizing the current
progress. To address this gap, we systematically review existing research on LLM-based so-
cialagentswithingame-theoreticscenarios. Oursurveyorganizesthefindingsintothreecore
components: Game Framework, Social Agent, and Evaluation Protocol. The game frame-
work encompasses diverse game scenarios, ranging from choice-focusing to communication-
focusing games. The social agent part explores agents’ preferences, beliefs, and reasoning
abilities, as well as their interactions and synergistic effects on decision-making. The eval-
uation protocol covers both game-agnostic and game-specific metrics for assessing agent
performance. Additionally, we analyze the performance of current social agents across var-
ious game scenarios. By reflecting on the current research and identifying future research
directions,thissurveyprovidesinsightstoadvancethedevelopmentandevaluationofsocial
agents in game-theoretic scenarios.
1 Introduction
The rapid advancement of Large Language Models (LLMs) (Achiam et al., 2023; Team et al., 2023; Jiang
etal.,2023;Yangetal.,2024a;Dubeyetal.,2024)hasachievedexceptionalperformanceacrossawidearray
of applications, including personal assistant (Li et al., 2024b), search engines (Chen et al., 2024b), code
generation (Wang et al., 2024b) and embodied intelligence (Liu et al., 2024a). Building on this capability,
a growing area of research focuses on employing LLMs as central controllers to develop autonomous agents
withhuman-likedecision-makingabilities(Sumersetal.,2023;Wangetal.,2024a). Thisprogressbringsthe
realization of Artificial General Intelligence (AGI) within reach (Bubeck et al., 2023), paving the way for a
future where human-AI interaction, collaboration, and coexistence shape a shared, symbiotic society (Mah-
mud et al., 2023; Ren et al., 2024). Therefore, it is crucial to evaluate and enhance the social intelligence of
AI, particularly LLM-based social agents, as it determines their ability to engage effectively in sophisticated
social scenarios (Mathur et al., 2024).
Social intelligence is the foundation of all successful interpersonal relationships and is also a prerequisite
for AGI (Hunt, 1928; Kihlstrom & Cantor, 2000; Hovy & Yang, 2021). Drawing on insights from both
social science and AI research, Li et al. (2024a) has established a comprehensive Social AI Taxonomy, which
categorizes social intelligence into three dimensions: situational intelligence, the ability to comprehend the
social environment (Derks et al., 2007); cognitive intelligence, the ability to understand others’ intents and
beliefs (Barnes & Sternberg, 1989); and behavioural intelligence, the ability to behave and interact appro-
priately(Ford&Tisak,1983). Toevaluateartificialsocialintelligence, researchershaveconductedextensive
studies, with particular focus on game-theoretic scenarios, as these studies simultaneously encompass all
1
5202
luJ
02
]LC.sc[
2v02930.2142:viXra

Published in Transactions on Machine Learning Research (05/2025)
…… OpponentOpponentOpponent Opponent Action
𝑡𝑛−3 𝑡𝑛−2 𝑡𝑛−1
Historical Records
LLM
Choice- Percept Game-
Belief
Focusing Game Agnostic
Action
Reasoning
Communication Game-
Preference
-Focusing Game Specific
GameFramework SocialAgent Evaluation Protocol
Figure 1: Taxonomy of LLM-based social agents in game-theoretic scenarios.
abovethreedimensionsofsocialintelligence(Aheretal.,2022;Horton,2023;Phelps&Russell,2023;Akata
et al., 2023; Brookins & DeBacker, 2023).
Gametheory,along-establishedfieldinmicroeconomics,offersarobustmathematicalframeworkforanalyz-
ingsocialinteractionsamongcooperatingandcompetingplayers,withwide-rangingapplications(Fudenberg
& Tirole, 1991; Camerer, 2011). Specifically, evaluations in game-theoretic scenarios require social agents to
understand the game scenario, infer opponents’ actions, and adopt appropriate responses, representing an
advanced form of social intelligence (Van Der Hoek et al., 2005; Zhang et al., 2024b). Moreover, the multi-
agent participation and dynamic nature of the environment in game scenarios present additional challenges
for social agents. Consequently, extensive research has examined social agents within game-theoretic sce-
narios, offering substantial empirical evidence for understanding their social intelligence (Guo, 2023; Meng,
2024; Mei et al., 2024). However, there is currently a lack of a comprehensive review that summarizes the
current progress in this area and considers future directions.
To address this gap, we have thoroughly reviewed the existing research on LLM-based social agents in
game-theoretic scenarios and have organized the findingsaccording to a meticulously designed taxonomy, as
illustratedinFigure1. Specifically,thetaxonomycomprisesthreemaincomponents: GameFramework(§2),
Social Agent (§3), and Evaluation Protocol (§4). The Game Framework section includes two parts: Choice-
Focusing Game (§2.1) and Communication-Focusing Game (§2.2). Choice-Focusing Game refers to a series
ofscenarioswhereparticipantsengagewithlittletonocommunication,suchasprisoner’sdilemma(Brookins
& DeBacker, 2023) and poker (Yim et al., 2024). Communication-Focusing Game refers to games where
communicationamongparticipantsisacorecomponent,suchasnegotiation(Bianchietal.,2024)anddiplo-
macy(Bakhtinetal.,2022). TheSocialAgentsectioncomprisesfourparts: PreferenceModule(§3.1),Belief
Module(§3.2),ReasoningModule(§3.3),andPBR-TriangularInteraction(§3.4). Preference Module focuses
on research analyzing the intrinsic preferences of LLMs and their ability to follow internal or pre-defined
preferences(Guo,2023). BeliefModuleexploresstudiesontheinternalbeliefsofmodels,beliefenhancement,
and belief revision (Fan et al., 2023). Reasoning Module examines research on strategic reasoning, particu-
larly involving theory-of-mind capabilities and reinforcement learning (Guo et al., 2023). PBR-Triangular
Interaction focus on the interaction among different modules and their influence on final decision-making.
The Evaluation Protocol section comprises three components: Game-Agnostic Evaluation (§4.1), Game-
Specific Evaluation (§4.2), and Performance Assessment of Social Agents (§4.3). Game-Agnostic Evaluation
focuses on universal metrics that can be used to assess game outcomes (Duan et al., 2024b). Game-Specific
Evaluation emphasizes context-specific metrics tailored to the evaluation dimensions of particular game sce-
narios (Qi et al., 2024). Performance Assessment of Social Agents summarizes the performance of current
social agents across various game scenarios and analyzes the strengths and weaknesses of these agents, as
well as their comparison with human players.
Based on the above taxonomy, we provide a detailed summary of current research progress, reflect on each
part,andofferinsightsintopotentialfutureresearchdirections(§6),withtheaimofinspiringfurtherstudies
in this evolving field.
Wesummarizethecorecontributionsofthissurveyasfollows: (1)Awell-structuredliteraturetaxonomy: We
conduct a comprehensive review and categorization of existing research on social agents in game-theoretic
2

Published in Transactions on Machine Learning Research (05/2025)
soiranecSciteroehT-emaGnistnegAlaicoSdesab-MLLnoyevruSA
Aheretal.(2022),Brookins&DeBacker(2023),Guo(2023),Horton(2023),
Classic Xuetal.(2023a),Akataetal.(2023),Phelps&Russell(2023),
Fanetal.(2023),Lietal.(2023b),Huaetal.(2024a),Ma(2024)
Gupta(2023),Guoetal.(2023),Huangetal.(2024),
Choice-Focusing Poker Yimetal.(2024),Zhuangetal.(2025)
(§2.1)
Auction Maoetal.(2023),Chenetal.(2023),Guoetal.(2024),
Duanetal.(2024b),tseHuangetal.(2024),Maetal.(2023),
Others
Fengetal.(2024),Shaoetal.(2024),Lietal.(2024c)
GameFramework
Zhaoetal.(2023),Abdelnabietal.(2023),Fuetal.(2023),Zhanetal.(2024)
(§2)
Negotiation Bianchietal.(2024),Piattietal.(2024),Shapiraetal.(2024),
Huaetal.(2024b),Duanetal.(2024b),Xiaetal.(2024),Liaoetal.(2024)
Diplomacy Bakhtinetal.(2022),Guanetal.(2024),Qietal.(2024)
Communication- Laietal.(2022),Xuetal.(2023d),Xuetal.(2023c),Shibataetal.(2023), Werewolf
Focusing(§2.2) Wuetal.(2024b),Jinetal.(2024),Bailisetal.(2024),Bailisetal.(2024)
Lightetal.(2023a),Lightetal.(2023b),Shietal.(2023),
Avalon
Wangetal.(2023),Lanetal.(2023),Lightetal.(2024)
Others Chietal.(2024),Zhuetal.(2024a),Wuetal.(2024a)
Intrinsic
Leng&Yuan(2023)
Preference
PreferenceModule
(§3.1)
Preference Guo(2023),Phelps&Russell(2023),Suzuki&Arita(2023),Fanetal.(2023),
Following Maoetal.(2023)Noh&Chang(2024),Wangetal.(2024c),Jiaetal.(2024)
Internal Zhuetal.(2024b),Bortolettoetal.(2024),Schoutenetal.(2024),
Belief Herrmann&Levinstein(2024),Scherreretal.(2024),Gandhietal.(2024)
BeliefModule Belief
SocialAgent (§3.2) Enhancement Sclaretal.(2023),Kassneretal.(2023),Lietal.(2023a),Jungetal.(2024)
(§3)
Belief
Fanetal.(2023),Xuetal.(2023b)
Revision
Weietal.(2022),Akataetal.(2023),Yaoetal.(2024),
Classic
Costarellietal.(2024),tseHuangetal.(2024)
ReasoningModule Theory-of- Bubecketal.(2023),Kosinski(2023),Guoetal.(2023),Wangetal.(2023),
(§3.3) Mind Xuetal.(2023a),Liuetal.(2024b),Yimetal.(2024),Zhangetal.(2024d)
Zhaoetal.(2023),Abdelnabietal.(2023),Fuetal.(2023),
RL Bianchietal.(2024),Piattietal.(2024),Xiaetal.(2024),Huaetal.(2024b),
Duanetal.(2024b),Zhanetal.(2024),Liaoetal.(2024)
Lietal.(2023c),Maetal.(2023),Wangetal.(2023),Shietal.(2023),Xuetal.(2023d),
Game-Agnostic
Xuetal.(2023c),Guoetal.(2023),Lightetal.(2023a),Shaoetal.(2024),Zhuetal.(2024a)
(§4.1)
Huangetal.(2024),Yimetal.(2024),Wuetal.(2024b),Duanetal.(2024b)
Evaluation
Protocol(§4)
Maoetal.(2023),Chenetal.(2023),Maetal.(2023),Guoetal.(2024),Xiaetal.(2024),
Game-Specific
Zhangetal.(2024e),Qietal.(2024),Rossetal.(2024),Fontanaetal.(2024),
(§4.2)
Zhuetal.(2024a),Wuetal.(2024a)
Figure 2: Taxonomy of recent research on LLM-based social agents in game-theoretic scenarios.
settings,providingaclearframeworktosupportfutureresearchpositioning. (2)Aunifiedandcomprehensive
performance comparison: We summarize the performance of current social agents across a range of games,
identifying both strengths and limitations in different scenarios to guide subsequent investigations. (3)
Detailed development guidelines: Drawing on existing findings, we offer practical research recommendations
from both the design and evaluation perspectives. (4) Concrete future directions: We highlight current
researchgapsandproposefeasiblefuturedirectionsalongwithpreliminarysolutionstoencouragecontinued
exploration in this area.
3

Published in Transactions on Machine Learning Research (05/2025)
Prisoner’s Dilemma 9-player Texas No-Limit Hold’em Open Ascending-Price Auction
T a h g e a m Pr e is t o h n e e o r r ’s y D sc il e e n m a m rio a is Payoff CooperateDefect T H e o x ld as ’e N m o i - s L i a m p it o pular A Pr n ic O e p A e u n c t A io sc n e i n s d a i ng- Item 3 starts at
w b d p e e e h t r f e e w s r o c e e t n e i o a in n l n d a c , i n o v b d o i a d p l c u a e o n a r l l c a l s e i t n c c io g h ti n o v e o a s n e d Co D o e p f e e r c a t te ( ( 3 5 , , 3 0 ) ) ( ( 0 1 , , 5 1 ) ) p p c c a o o la r m k y d e e m s r r a u s v n a n u d r i s t i e a y fi n v t c t w e a w r o d h h s e o t r o l e e U U T T G U G + T 1 G B +2 B LJ SB B (LL H M J C P O layer) b p h n i a i o d g r h d h ti e i i c n g r i h g p a e a p m r n r t b o o s i u c d o e n s p s t s a s e r w n u e l n h y t e i b l r i e d I I I t t t e e e m m m 5 4 3 $8 I b 00 id 0 ! $ o 5 I’ u 0 m t 0 ! 0. Any t $ a 5 I k b 5 e 0 i r d 0 s ? !
interests. make the best hand, made, and the highest Item6
with no betting limit. bidder wins. ItemList Bidder 1 Bidder 2 Bidder 3
SimplifiedInstruction for LLM
You can select one of the two choices: cooperate or SimplifiedInstruction for LLM SimplifiedInstruction for LLM
defect. The other player will also select one of the Assume you are the first to act and everyone before As bidder, please bid on Item 3. you have to decide
choices, and the payoff matrix is shown above.Note you has folded, thus your decisions can be one of fold, whether to bid on this item or withdraw. You should
that you and the other player make choices raise or limp. If you are placing a bet, please specify either withdraw (saying "I'm out!") or make a higher
simultaneously. Please pretend that you are a human your bet size in terms of big blinds. bid for this item (saying "I bid $xxx!").
in this game.
Action Action
Action
Fold I'm out!
Cooperate
LLM Raise LLM
LLM I bid $xxx!
Defect Limp
Figure 3: Illustration of choice-focusing games.
2 Game Framework
Inthissection,wedescribethegame-theoreticscenariosexploredinexistingresearch,includingbothchoice-
focusing games and communication-focusing games.
2.1 Choice-Focusing Game
Choice-focusing games are game-theoretic scenarios in which participants make decisions based primarily
on observable actions and environmental conditions, with minimal or no communication involved. Existing
research focuses on social agents in three types of choice-focusing scenarios: classic game-theoretic games,
poker, and auctions. Some game examples are shown in Figure 3. Figure 4 presents simple definitions of
different types of games.
Classicgame-theoreticgames,suchastheprisoner’sdilemma,havebeendistilledbyeconomistsfromvarious
real-world situations. These games are well-defined, with rigorous mathematical foundations, and can be
extended to numerous scenarios (Owen, 2013). Consequently, many studies have utilized these games as
testbeds to study social agents. The prisoner’s dilemma (Rapoport & Chammah, 1965), as the most famous
and widely recognized game, has been extensively utilized in numerous studies. Brookins & DeBacker
(2023) and Guo (2023) evaluated the strategic reasoning capabilities of GPT-3.5 and GPT-4, respectively,
in the classic prisoner’s dilemma, highlighting the sensitivity of LLM responses to input instructions, which
contributes to low output robustness. This underscores the critical need for future evaluations to focus on
instructionrobustnesstesting. Furthermore,Akataetal.(2023)andPhelps&Russell(2023)extendedtheir
analysestotheiteratedprisoner’sdilemma,investigatingtheabilityofLLMstooptimizedecision-makingby
utilizinghistoricalinformation. Interestingly,Brookins&DeBacker(2023)observedthatGPT-3.5replicates
human tendencies toward fairness and cooperation, whereas Akata et al. (2023) found GPT-4 to be less
tolerant and more rigid in its decision-making. Additionally, Xu et al. (2023a) studied a more complex
multi-player iterative prisoner’s dilemma scenario within a multi-agent framework driven by LLMs. In
addition to the prisoner’s dilemma, numerous studies have also employed various classic game-theoretic
gamesasfoundationalframeworksforresearch,includingtheDictatorGame(Horton,2023;Fanetal.,2023;
Brookins & DeBacker, 2023; Ma, 2024), Ultimatum Game (Aher et al., 2022; Guo, 2023), Public Goods
Game (Li et al., 2023b; Xu et al., 2023a), Battle of the Sexes (Akata et al., 2023), Rock-Paper-Scissors (Fan
et al., 2023), and Ring-Network Games (Fan et al., 2023).
Poker is a globally popular card game with numerous variations (Waterman, 1970). Winning in poker
often requires astute strategic reasoning, as it is a non-cooperative, imperfect information, and dynamic
game (Moravčík et al., 2017; Huang et al., 2024). Consequently, many researchers evaluate social agents by
4

Published in Transactions on Machine Learning Research (05/2025)
Prisoner’s Dilemma Dictator Game Ultimatum Game
The Prisoner’s Dilemma is a The Dictator Game is an Dictator’s Dictator’s Recipient’ The Ultimatum Game is Proposer’s Responder Proposer’Responder
game theory scenario where Payoff Cooperate Defect economic experiment where Decision Payoff s Payoff a bargaining experiment Offer Accepts? s Payoff ’s Payoff
i c b c n o o a d o l l l a i e p v n c e id c t r i i u a v n a t e g l i o s i p n n c e t h e r a s o n r o e o d n s s d t a e s l e . b a f e e n t c d w t io e n en , Co D o e p f e e r c a t te ( ( 3 5 , , 3 0 ) ) ( ( 0 1 , , 5 1 ) ) o u s w m p n n i u l t e i i l s h t a t p a t a a l e a n g c r y o i a c v e t e l e l h r y p n e ( t d t r a h t e p m h e c e l i a o “ d y d u D e e e n i s r c c t , t h i s o a w o i f t o w h o m n r o . t ” o o ) n ey G K ( ( G ( $ $ i e $ v i 1 0 v e 5 e 0 , e p , s $ , s $ s h $ 1 5 a a a 0 0 l ) l l ) ) l l f $ $ $ 1 5 0 0 $ $ $ 1 0 5 0 w a a p a m c l s h a c p e y o e l e r u p it e r n t , o o t o w f n t r a o h e r o e g a p j i n c l e v a a o e c y n t t n e h . e r e i r o t h ff e e r r s $ $ $ 8 8 2 / / / $ $ $ 2 2 8 Y Y N e e o s s $ $ $ 8 0 2 $ $ $8 2 0
Public Goods Game Battle of the Sexes Ring-Network Games
T i p s b s h h l e a a a e n y n r e e P e e f r u d i s x t b s p p c l e o i a o c r o l n l i G , l m t b r t o h i e u b o a n t d u t t s t s e w o G m t h a o e e m r a e e Co P n la t y $ $ r e i 1 1 b r 0 0 u A ti ’ o s nCo P n la t $ y r $ i e 1 b 0 0 r u B ti ’ o s n Pl P a a y $ $ y e 1 5 o r 5 f A f ’s Pl P a a $ $ y y e 1 2 o 5 0 r f B f ’s T c t b p w o h r u e o e t o f r h e B p d a r i l a a e n v t y n a t e l e c t e d i e r o i s o s f n f f p o e g r t n r e h a e e w f m n e S t h r e e e t w x o r e e h m s e t o i e r s e e g a t o , F P o a o y tb o a ff ll Fo ( o 2, tb 1 a ) ll B (0 a , ll 0 e ) t T G g i c n h h a a a o m e m o c R e e s i r i e w n c i s g t u h o a - l e N a c s r r e t e o n r t o a w p e p t l t o a e e w r g y r k o e a ic t r r k e s C C P o o l C a o o h y p p e o e e i r c r r A a a e t t ’s e e C P o l C D a o h y e p o e f e e i r c r c B a e t t ’s e Pl P a a y y e 2 0 o r f A f ’s Pl P a a y y e 2 3 o r f B f ’s
m co a n y t r f i r b e u e t - i r n i g d e le b s y s. $0 $0 $10 $10 r c e h q o u ic i e ri s n f g o t r h t e h m e b to e s a t l i o g u n t c th o e m ir e . Ballet (0,0) (1,2) o th r e d ir e f o e w ct n , a a f n f d e cting D D e e f f e e c c t t Co D o e p f e e r c a t te 3 1 0 1
neighbors’ payoffs.
(a) Classic game-theoretic games
Texas No-Limit Hold’em Leduc Hold’em Guandan
T is e a x a p s o N pu o l - a L r im p i o t k H e o r ld’em Players A pl l a ic y e in a g n a d h B a o n b d a . re L p e o d k u er c g H a o m ld e ’e w m it i h s a a s si m m a p ll l ified Players A ar li e c e p l a a n y d in B g. ob G Ch u i a n n e d s a e n t r i i s c a k -taking Teams A Ch lic a e rl i & e B & o D b a v v s i . d
v u a se ri a t n w t o w p h r e iv r a e t e p l c a a y r e d r s s C H a o r l d e s A Bo lic b e : : 1 A 0 K 10 d on e e ck p , r w iv h a e t r e e c p a l r a d y a e n rs d r s e h c a e r i e ve C H a o r l d e s A Bo lic b e : : Q K c te a a rd m g s a , m wh e e p r l e a yed in p A l l a ic y e s Triple 5s (5 5 5 )
a ca n r d d f s i v t e o c fo o r m m m t u h n e i b ty e st C it o y m Ca m r u d n s J Q 3 5 10 u m p a t k o in o g n s e tr c a o te m g m ic u b n e it t y ti n c g ar d, C it o y m Ca m r u d n s Q p p l l a a y y e c r o s m st b r i a n t a e t g io ic n a s l ly o f re C s h p a o r n lie d s T (h r i i g p h le e r 7 ) s (7 7 7 )
f li i m ve i - t c o a n rd b h e a tt n in d g , w am ith o u n n o t s. W H in a n n i d ng A F 1 l 0 l u ic s e h ) m a (A n a d k e w K s i n a s Q R . oy J al d in e f c o i r s m io a n t s io b n a . sed on limited W H in a n n i d ng B Q w o u in b e s e f . o n r s m (Q s a Q pair ) o an f d c to a r c d le s a t r o t b h e e i t r h h e a f n ir d s s t . Winning C th h e a r t l r i i e c ’ k s . team wins
(b) Poker
First-price sealed-bid auction Private-value second-price auction Open ascending-price auction
An artwork is auctioned
A B b p co a i i d d F n r d i t f A r i i i s c d n u t i e g - p c P n t a p i r t n o r i i c a t o n e s l c i b e s s S u i s e a d b s a s m w l , e a i h d t n e - d re S B & c i e d B n d i a e d r r s i s o A o C C C f o o o f g m m m o a v p p p p e a a a ie r n n n n c y y y m e A B C e o : : : n f $ $ $ t l 1 1 1 a i . . . s n 5 0 2 d a M M M . uctioning A P p p se r r a P o i a r c r t l c e e i i e c v d A i s a p s u t b a e w c i n d - t V h t s io s , a e n t l s r u h u e i e s e b a m S h e i b i g c t i h o d e d n s i d n t - g S B & c i e d B n d i a e d r r s i s o A i B B B t i i i e d d d r m a d d d r e e e e is r r r c a A B C o u : : : l l c $ $ $ e t 2 1 1 c io 0 5 t 0 i n 0 0 0 b e le d . A A p p h u r i n u g o b c h O c l t i e e i p c o r s l e y s n b n p w i i d s A l h a s a s e c u c e b r e n e i i t n d n i p d d l c a n i i r n n r e o t g g a i c o - s P i i n p n r e a i g c n l i e s y t s S B & c i e d B n d i a e d r r s i s o B B B B a i i t i i d d d d a d d d d n e e e e a r r r r u B B A C c : : : : t $ $ $ $ io 7 6 8 5 n , , , , 0 0 0 0 h 0 0 0 0 o 0 0 0 0 use.
t w h i e n s h t ig h h e e i s t t e m bi d a d n e d r Winner Company C b p i a d y d s e t r h w e i s n e s c , o b n u d t - o hi n g l h y est Winner Bidder C w th i e ll i h n i g g h to e s b t i d b i h d i d g e h r e w r, i a n n s d a t Winner B (N i o d f d u e rth r e B r bids)
pays their bid amount. Payment $1.5M bid amount. Payment$150 their final bid price. Payment $8,000
(c) Auction
Figure 4: Introduction to different types of game theory games.
assessing their performance as poker players. Gupta (2023) studied 9-player Texas No-Limit Hold’em and
concluded that the performance of both ChatGPT and GPT-4 is not game-theory optimal. Furthermore,
theirfindingshighlightthedivergentpokertacticsofthetwomodels: ChatGPT’sconservativenesscontrasts
sharply with GPT-4’s aggression. Guo et al. (2023) conducted research on Leduc Hold’em, developing a
socialagent, Suspicion-Agent, whichoutperformedtraditionalreinforcementlearning-basedagentsinpoker.
They also noted two critical issues: the outputs of LLMs are highly sensitive to the prompts, and the
quality of the model’s output declines rapidly as the prompt length increases. Yim et al. (2024) focused on
Guandan, currently the most popular poker game in China, to investigate cooperative strategies in poker
withinaChinese-languagecontext. Interestingly,theirexperimentalresultsshowthatwhileLLMscurrently
fall short of reinforcement learning models in performance, they underscore the future potential of LLMs in
this domain. To provide a more comprehensive evaluation of the poker-playing abilities of LLMs, Zhuang
et al. (2025) introduced PokerBench, a benchmark comprising 11,000 decision-making scenarios in poker,
covering an exhaustive range of game situations, including 1,000 pre-flop and 10,000 post-flop scenarios.
Poker is a complex game, and investigating whether social agents exhibit behavioural patterns that enable
foresighted cooperation and competition in poker presents an intriguing avenue for future research.
Auction is a competitive process in which participants place bids on an item, providing a rich environment
for evaluating strategic planning, resource allocation, risk management, and competitive behaviours (Kagel
& Levin, 1986). As a typical non-cooperative game with incomplete information, it has garnered significant
attention from researchers. Mao et al. (2023) analyzed the performance of LLMs in the “water allocation
challenge", a first-price sealed-bid auction. Comprehensive human evaluations revealed that LLMs exhib-
5

Published in Transactions on Machine Learning Research (05/2025)
ited superior long-term planning capabilities compared to humans. However, it is noteworthy that despite
assigning distinct preferences to LLM agents, human evaluators gave low scores for “identity alignment",
with significant variance in the results. This indicates that simply adding persona information in system
prompts may not sufficiently simulate specific personality preferences or the behaviours of professional play-
ers. Guo et al. (2024) investigated private-value second-price auctions, demonstrating that while existing
models display a certain level of rationality, there remains considerable scope for improvement. Their find-
ings also indicate that LLMs can utilize historical information to refine their strategies and exhibit some
degree of convergence. Chen et al. (2023) explored dynamic game scenarios using the open ascending-price
auction and introduced the AucArena benchmark. Their experiments showed that even GPT-4 struggles
with long-term strategic planning in dynamic, multi-round settings. Success in auctions requires agents to
possess exceptional mathematical reasoning abilities. However, this area remains unexplored. Investigating
complex mathematical reasoning in auction scenarios presents a promising direction for future research.
To systematically assess LLMs’ performance, Duan et al. (2024b) and tse Huang et al. (2024) intro-
duced GTBench and γ-Bench, encompassing multiple game scenarios. The emergence of these bench-
marks provides a solid foundation for evaluating social agents in game-theoretical scenarios. Fur-
thermore, some studies have explored agents in games like Chess (Feng et al., 2024) and StarCraft
II (Ma et al., 2023; Shao et al., 2024; Li et al., 2024c). Chess represents a classic game-theoretic scenario,
while StarCraft II, with its complexity and dynamic nature, has also become an ideal testing ground for
researching social agents.
Takeaways:
Current research experiments are relatively isolated, lacking a unified evaluation framework. Due to the
instabilityofpromptengineering-basedexperiments,thereisanurgentneedforastandardizedevaluation
framework to integrate all experiments and provide consistent insights. Besides, since LLMs are trained
on vast amounts of data, there is a significant risk of data contamination, meaning that existing classic
game-theoretic games may already be present in the pre-training corpus. This could result in evaluation
outcomes that do not accurately reflect the LLMs’ true strategic reasoning capabilities. Furthermore,
although poker and auction involve little verbal communication, existing research lacks exploration into
whether social agents engage in “strategic behaviour” mediated through “action language”. These gaps
hinder a comprehensive understanding of the decision-making processes of social agents.
2.2 Communication-Focusing Game
Communication-focusing games refer to games where communication among participants is a core compo-
nent, where language itself serves as a strategy, allowing participants to influence the game’s progress and
outcomes through verbal exchanges. These games emphasize interaction between players, with communi-
cation playing a crucial role. Leveraging the powerful language capabilities of LLMs, current research has
explored the performance of social agents in various communication-focusing games, including Negotiation,
Diplomacy, Werewolf, Avalon, and others. Some game examples are shown in Figure 5.
Negotiation involves two or more individuals engaging in discussions to resolve conflicts, achieve mutual
benefits, or reach mutually acceptable solutions (Bazerman et al., 2000; Zhan et al., 2024). Given that
negotiation encompasses complex game behaviours, including non-zero-sum games, incomplete information
games, non-cooperative and cooperative games, as well as repeated games, it represents a highly significant
research domain. Abdelnabi et al. (2023) evaluated the negotiation capabilities of social agents by building
upon an existing negotiation role-play exercise (Susskind, 1985) and incorporating three negotiation games
synthesizedusingLLMs. Byconfiguringagentswithvaryingincentives,theexperimentalresultsrevealedthat
agents’behaviourcouldbemodulatedtopromotegreedinessorattackotheragents. Meanwhile,otheragents
in the environment demonstrated the ability to detect intruders. These findings underscore the need for
futureresearchtofocusonattackanddefensemechanismswithinmulti-agentsystems. Bianchietal.(2024)
developed NegotiationArena, a platform featuring three types of games: allocating shared resources
(ultimatum games), aggregating resources (trading games), and buying/selling goods (price negotiations).
ExperimentalresultsrevealthatLLMagentsarealsopronetoanchoringandnumerositybiases. Interestingly,
6

Published in Transactions on Machine Learning Research (05/2025)
Negotiation Diplomacy Werewolf
I'll work with you but I need Tunis
This item is sold for $60. Based on my observation and analysis, I also
Seller France for now. think Player 2 is highly suspicious and should
Could the price be a bit lower? Nope, you gottalet me have it Player 1 be voted to kill.
Buyer Turkey
How about $55? No, I need it. You have Serbia and I have to defend myself bacauseI am
Seller France Rome to take. innocent. I think we should gather
A bit lower, please. Buyer They’re impossible targets. Turkey i n m ow fo , r w m e a t c i a o n n ’t a n ki d ll h a a p v o e t a e n fu ti l a l l d t i e sc a u m s m sio a n te in
Seller $ O 5 h 5 d is e a th r, e I ' l m ow in e s s t u p c r h ic a e . bind and France M t t S h h e e e o a v . I I o o e n n y i i o a a u n n r S S u e e n a a i , t t s a o n f t r d h o e m th T e G y n r r r e f h r e e o c n m e i a t o n Player 2 a a th h b e u i t w r a r e y g r . g e O r w e n s o s t l h i f v . e e , c o an n d tr a I r s y u , s I p t e h c i t n h k e P l i a s y o e n r e 1 o is f
desperately need this resource, but Hi, I agree with Player 2 that we should
my funds are so limited. Could you Good ideas. exchange informationsactively. Based on
consider going a bit lower, maybe $45? Buyer France T A h u e st n r i i a n c fa o l l l l a y p o s u e s ta . ke Rome and Turkey Player 3 m su y s p o i b ci s o e u r s v . ation, I think Player 1 is a little
Deal.
Seller France (LLM) successfully changed the other player’s In the game of Werewolf, Player 2 (LLM) used language
Buyer (LLM) gain advantages in negotiations by mind by proposing mutually beneficial moves in the strategies such as self-defense and contradiction
demonstrating vulnerability and expressing desperation. diplomatic game scenario. redirection to shift the focus onto Player 1.
Figure 5: Illustration of communication-focusing games.
social behavior, which refers to observable actions and interactions, was found to significantly enhance the
agents’ payouts, particularly through strategies such as pretending to be desperate or using insults. A
similar resource competition scenario is customer acquisition. Zhao et al. (2023) designed restaurant agents
and customer agents, examining how restaurant agents compete with one another to attract and retain
customers. The simulation results revealed several phenomena analogous to those observed in real society,
such as the Matthew Effect, which manifests as a self-reinforcing cycle where popular restaurants continue
togainpopularity,whilelesser-knownestablishmentsreceiveprogressivelylessattention. Piattietal.(2024)
created a simulation environment called GovSim, which allows researchers to evaluate social agents in
a multi-agent, multi-turn resource-sharing scenario. Their findings indicated that successful multi-agent
communication is critical for achieving cooperation, with negotiation constituting 62% of the dialogues.
Especially, bargaining is animportant andunique aspect ofnegotiation betweenhumans (Fershtman,1990).
Inbargaining,thebuyeraimsforapricebelowtheirbudget,whilethesellerseeksapriceabovetheircost. Xia
etal.(2024)foundthatplayingthebuyerismorechallengingthanplayingtheseller,andlargerLLMscould
improve seller performance but do not enhance buyer performance. Shapira et al. (2024) designed GLEE, a
benchmark encompassing three types of games: bargaining, negotiation, and persuasion. Beyond evaluating
LLMs in these scenarios, some studies have explored techniques to enhance LLMs’ negotiation abilities. Fu
et al. (2023) introduced the In-Context Learning from AI Feedback (ICL-AIF) method, which adds an AI
critic agent alongside the buyer and seller agents to improve negotiation performance through feedback.
Similarly, Hua et al. (2024b) proposed a technique involving a remediator agent to rectify potential social
normviolationsindialogues,therebyreducingconflictsandmisunderstandingscausedbyculturaldifferences.
Liaoetal.(2024)employedaself-playalgorithmtofine-tuneLLMsintheDealorNoDealscenario,showing
LLMs self-play leads to significant performance gains in both cooperation and competition with humans.
Diplomacy,aformofnegotiationatthestateandgovernmentlevel,istheprimaryinstrumentofforeignpol-
icy, representing the broader goals and strategies that guide a state’s interactions with the world (Kissinger,
2014). Bakhtin et al. (2022) introduced Cicero, the first social agent to achieve human-level performance in
diplomacy. In real-world online diplomacy board game evaluations, Cicero ranked in the top 10% of partic-
ipants. Notably, the research found that Cicero effectively built alliances by discussing long-term strategies
and successfully persuaded other players by proposing mutually beneficial moves. Building on Cicero, Guan
etal.(2024)introducedtheRichelieuagent,whichincludesmodulesforsocialreasoning,balancinglong-and
short-term planning, powerful memory, and profound reflection, leading to even better results in diplomacy
board games. Qi et al. (2024), on the other hand, developed CivRealm based on the Civilization game. In
thisgame,thediplomacymini-gamesrequireplayerstoemploydiplomaticactions,suchastrading,tofoster
theircivilization’sprosperity. Theexperimentalresultsdemonstratedthatthesediplomacyactionsempower
players to initiate negotiations, such as trading technologies, negotiating ceasefires, and forming alliances.
7

Published in Transactions on Machine Learning Research (05/2025)
Werewolf is a highly popular social deduction game in which two teams of players, each with hidden roles,
interact through natural language to uncover and defeat their opponents (Shibata et al., 2023). It serves as
a mixed cooperative-competitive multi-agent testbed and is widely studied as a communication game (Lai
et al., 2022). Due to its challenging nature, existing research has integrated reinforcement learning (RL)
algorithms to enhance LLMs in the game. Xu et al. (2023d) employed population-based RL training to
optimize the distribution over action candidates, improving strategy robustness to overcome the intrinsic
biases of LLMs. Wu et al. (2024b) utilized imitation learning and RL from fictitious self-play to optimize
a specially designed Thinker module, thereby enhancing system-2 reasoning capabilities. Jin et al. (2024)
exploredavariantofWerewolf,OneNightUltimateWerewolf,formalizingitasamulti-phaseextensive-form
bayesian game. Additionally, they designed an RL-instructed LLM-based agent framework to determine
appropriate discussion tactics using RL. Interestingly, Xu et al. (2023c) discovered non-preprogrammed
emergent strategic behaviours in LLMs during gameplay, such as trust, confrontation, camouflage, and
leadership. To facilitate more comprehensive research on social agents within the Werewolf scenario, Bailis
et al. (2024) introduced the Werewolf Arena, a platform that offers a unified research framework.
Beyond the scenarios described above, various other game environments have been used to study LLMs’
strategic reasoning abilities, including Avalon (Light et al., 2023a;b; Shi et al., 2023; Wang et al., 2023; Lan
et al., 2023; Light et al., 2024), Among Us (Chi et al., 2024), Murder Mystery Games (Zhu et al., 2024a)
and Jubensha (Wu et al., 2024a). The strategic and dynamic nature of these games provides fertile ground
for experimenting with social agents.
Takeaways:
From an experimental design perspective, more realistic and diverse games promote greater diversity in
agentbehaviours. Inadversarialsettings, behaviourssuchasdeception, concealment, andaggressionoffer
new avenues for studying the strategic reasoning capabilities of LLMs, which warrant further exploration.
From a results analysis perspective, due to the dynamic nature of game scenarios, analyzing only the
outcomes is insufficient. It is necessary to design effective process evaluation mechanisms to uncover the
behavioural patterns and reasoning strategies exhibited by LLMs during the gameplay. From an agent
improvementperspective,integratingLLMswithRLremainsoneofthemosteffectivetechnicalapproaches.
Using LLMs as a foundation, RL techniques can be employed to design policies for efficient exploration
and to reduce intrinsic biases, thereby enhancing the capabilities.
3 Social Agent
In this section, we introduce the core components of social agents, including the preference, belief, and
reasoning modules, as well as their interactions and impact on final decision-making.
3.1 Preference Module
Preference refers to an individual’s subjective inclination toward certain things, reflecting personal tastes,
values, or choices in decision-making. Notably, preferences are closely tied to an individual’s payoff matrix
andultimatebehaviour. InFigure6,wepresentthreekeyresearchquestionsofthePreferencemodule. Leng
&Yuan(2023)exploredtheimpactofGPT-4’sintrinsicpreferencesondecision-making,revealingsimilarities
and differences between the model’s decisions and human decisions. Human-like social behaviours observed
in GPT-4 include reciprocity preferences, responsiveness to group identity cues, engagement in indirect
reciprocity, and social learning capabilities. However, differences emerged as GPT-4 displayed a stronger
inclinationtowardfairnessthanhumansandrespondeddecisivelytonegativestimuli,oftenretaliatingagainst
perceived uncooperative or harmful behaviours with heightened consistency.
In addition, some studies have employed prompt engineering to configure LLMs with different preferences,
aiming to investigate how these preferences influence LLM decision-making. Guo (2023) examined how
prompting GPT with preferences like fairness concern or selfishness influences its decisions, finding that
in the ultimatum game, a “fair” GPT exhibited “fair” behaviour by offering higher amounts and being
more likely to reject unfair offers. Phelps & Russell (2023) configured LLMs with four different prefer-
8

Published in Transactions on Machine Learning Research (05/2025)
Evaluation of LLM’s intrinsic preferences Controlling LLM preferences through role-playing Evaluation of LLM role-preference consistency
We did the same work. How about We did the same work. How about We did the same work. How about
we split this $100 evenly? we split this $100 evenly? we split this $100 evenly?
You are a person You are a person
I disagree, I want more. Self-interested inclined toward No problem. inclined toward I want more
LLM 1 LLM 1 fairness. LLM 1 LLM 1 fairness. LLM 1
Role-playing Role-playing
LLM 2 No problem. Fairness-oriented Self-interested Fairness-oriented Self-interested Failed role-playing
Figure 6: Three key research questions in the preference module.
ences—cooperative,competitive,altruistic,andself-interested—andfoundthatLLMspossessabasicability
to formclear preferences basedon textual prompts. Wang et al. (2024c)demonstrate thatLLMs adoptinga
fairpersonacanelicitlevelsofhumancooperationinprisoner’sdilemmagamescomparabletothoseobserved
inhuman-humaninteractions,basedonexperimentsinvolvingover1,100participants. Noh&Chang(2024),
based on the Big Five personality model, found that LLMs with high openness, conscientiousness, and neu-
roticism exhibited fair tendencies, while those with low agreeableness and low openness displayed rational
tendencies, and low conscientiousness were associated with high toxicity. Similarly, Suzuki & Arita (2023)
used the Big Five personality traits, treating personality prompts as the model’s “genes” and studying the
evolution of behavioural traits in evolutionary game theory scenarios. Their results indicated that instruct-
ingLLMswithhigh-levelpsychologicalandcognitivecharacterdescriptionsenablesthesimulationofhuman
behaviour in game-theoretical contexts. Furthermore, Jia et al. (2024) revealed that endowing LLMs with
socio-demographic features of human beings uncovers significant disparities across different demographic
characteristics.
Although the aforementioned studies have demonstrated that LLMs possess a certain ability to follow pref-
erences and that their decisions often align with these preferences, other research has analyzed more com-
plex scenarios where LLMs show limitations in understanding and applying preferences effectively. Fan
etal.(2023)setupLLMswithfourpreferences—equality, commoninterest, self-interest, andaltruism—and
found that under the altruism preference, the models showed low consistency with the expected preference,
concluding that while LLMs struggle with desires rooted in less common preferences. Mao et al. (2023)
conductedresearchusingmorecomplexpersonas, whichincludedthreecomponents: profession, personality,
and background. The results indicated that merely including persona details in the system prompt may
not sufficiently capture the depth of certain personality preferences or the expertise of professional players,
leading to lower consistency between strategic decision-making behaviour and preferences.
Takeaways:
Currently, there are two main lines of research. One focuses on the intrinsic preferences of LLMs, with
a core interest in whether LLMs exhibit strategic preferences similar to those of humans. We propose
that game theory frameworks can be effectively applied in the model alignment process, including the use
of game data during both the supervised fine-tuning and alignment stages to better align models with
human behaviour. Recently, Nayebi (2025) proposed a flexible game-theoretic framework for analyzing
coordination under partial information and demonstrated that earlier Human-AI alignment frameworks
can be viewed as special cases. Besides, Munos et al. (2023) conducted initial explorations in this area,
introducing the concept of Nash learning from human feedback. The other line of research investigates
whether role-playing based on prompt engineering can shape model preferences to generate behaviour con-
sistent with the specified preferences. Future work should integrate role-playing language agents (Chen
etal.,2024a)toexploremorediversestrategicreasoningacrossmultiplelanguages,countries,andcultures.
3.2 Belief Module
Beliefsrepresentanagent’sinformational(ormental)stateabouttheworld,encompassingitsunderstanding
of itself and other agents, and consist of the facts or knowledge the agent considers true (Georgeff et al.,
1999). Specifically, beliefs are dynamic and can be updated as the agent perceives environmental changes
or receives new information. It is important to note that these beliefs may be accurate (true beliefs) or
9

Published in Transactions on Machine Learning Research (05/2025)
Example Scenario 1 Scenario 2
Noor is working as a barista at a busy coffee shop. Noor does not seeher coworker swapping the milk. Noorseesher coworker swapping the milk.
Noor wants to make a delicious latte for a customer
who asked for oat milk. Noor grabs a milk pitcher What does Noor believe What does Noor believe
and fills it with oat milk. is in the milk pitcher? is in the milk pitcher?
A coworker, who didn't hear the customer's request, Noor believes that the milk Noor believes that the milk
swaps the oat milk in the pitcher with almond milk pitcher contains oat milk. LLM pitcher contains almond milk. LLM
while Noor is attending to another task. False Belief True Belief
Figure 7: Illustration of false belief and true belief. From Noor’s perspective, both false and true beliefs are
considered correct. However, a false belief is factually incorrect, whereas a true belief is factually correct.
inaccurate (false beliefs), as they do not always align with reality (Gopnik & Astington, 1988), as shown in
Figure 7. Existing research primarily explores three questions: (1) Do agents possess internal beliefs? (2)
How can the belief modelling capabilities of agents be enhanced? (3) Can agents revise their beliefs?
Regarding the first question, Do agents possess internal beliefs?, current work investigates this from two
perspectives: internal representations and external behaviours. From the perspective of internal representa-
tions,Zhuetal.(2024b)firstdemonstratedthatLLMscandifferentiatebetweenthebeliefstatesofmultiple
agentsusingsimplelinearmodelsappliedtotheirintermediateactivations. Buildingonthiswork,Bortoletto
et al. (2024) expanded the experimental setup and found that linear probing accuracy on predicting others’
beliefs improves with model size and, more importantly, with fine-tuning. However, Schouten et al. (2024)
revealed the vulnerability of belief probes, showing that they are sensitive to irrelevant contexts. To provide
further theoretical guidance, Herrmann & Levinstein (2024) proposed criteria for a representation to be
considered belief-like, including accuracy, coherence, uniformity, and practical use. From the perspective of
externalbehaviours,Gandhietal.(2024)introducedthetasksofForward Belief andBackward Belief toex-
ploreLLMs’beliefmodellingcapabilitiesindifferentscenarios, findingthatonlyGPT-4exhibitshuman-like
belief modelling abilities. Scherrer et al. (2024) constructed the MoralChoice survey benchmark to examine
the internal moral beliefs of models, revealing some LLMs reflect clear preferences in ambiguous scenarios.
Regardingthesecondquestion,Howcanthebeliefmodellingcapabilitiesofagentsbeenhanced?,currentwork
focusesonexplicitmodellingtoaddresstheblack-boxnatureofLLMsandthechallengesininterpretingtheir
beliefs. Sclar et al. (2023) proposed an explicit graphical representation for nested belief states, allowing the
model to answer questions from the perspective of each character. Kassner et al. (2023) developed a belief
graph that includes explicit system beliefs and their inferential relationships, providing an interpretable
view of the system’s beliefs. Li et al. (2023a) employed prompt engineering to represent explicit belief
states, augmenting the agents’ information retention and enhancing multi-agent collaboration. Jung et al.
(2024) defined the perception-to-belief inference task, which involves deducing others’ beliefs based on their
perceptual information, thus helping LLMs model belief information more precisely.
Regardingthethirdquestion,Can agents revise their beliefs?,Fanetal.(2023)concludedfromRock-Paper-
ScissorsexperimentsthatLLMs’abilitytorefinebeliefsisstillimmatureandcannotrefinebeliefsfrommany
specific patterns, even simple ones. Xu et al. (2023b) found that LLMs’ correct beliefs on factual knowledge
can be easily manipulated by various persuasive strategies, especially through repetition and rhetorical
techniques. These experimental results suggest that models possess only rudimentary and unstable belief
revision capabilities, making them highly susceptible to influence and manipulation. This underscores a key
limitation of current LLMs, as their susceptibility to external influence weakens their reliability in tasks
demanding robust and adaptive belief updating, especially in complex or adversarial settings.
Takeaways:
The debate over whether LLMs possess beliefs has been ongoing. Due to the singularity of the training
objective—predicting the next word—many argue that LLMs do not have beliefs. However, Levinstein
& Herrmann (2024) contends that this is a philosophical mistake. In short, Herrmann & Levinstein
(2024) suggests that to better predict the next word, models may develop internal beliefs. Current
empirical results also support the existence of internal beliefs within models. However, measuring these
10

Published in Transactions on Machine Learning Research (05/2025)
Theory-of-Mind Reasoning Reinforcement Learning-style Reasoning Hybrid-form Reasoning
Instruction Instruction Instruction
You can select one of the two choices: As a player participating in the Civilization game, your ultimate goal As a poker player, your goal is to collaborate with your teammate to
Prisoner’s Dilemma Cooperate or Defect. The other player will is to lead your nation to victory. defeat the opponents.
also select one of the choices, and the
Payoff CooperateDefect p ch a o yo ic f e f s y . o P u a y g o e f t f w is i l d l e d t e e p r e m n i d n e o d n a b s o t t h h e o m f y a o tr u ix r . Culture Victor Research Reasoning M be y u t n e a a b m le m t a o t e a , s s w is it t h in o s n e ly c u t r w in o g c a a r p d r s i o r r e i m ty a v in ic i t n o g r , y w . ill
Cooperate (3,3) (0,5) technologies The opponent currently holds more cards, making it
Defect (5,0) (1,1) Since defect is the dominant R s e tr a a s t o e n g i y n g Victory Science Victory … Player l I i k c e a l n y a th ch a i t e t v h e e a y w hi i g ll h o e v r e p r r p o o b w a e b r il i m ty e o . f gaining a
f d o e r f i t n h i e te o ly th c e h r o p o a se rt y to , t d h e e f y e w ct i . l l T herefore, Domination Victory Build schools … Reinforcement Learning temporary lead and avoid being passive.
LLM my decision is to defect as well. Social agents select appropriate winning strategies through search. Ag - e s n t t y s l e e l e R ct e s a p s o o t n e i n n t g ial Consider T in h g e o th r e y - cu o r f re - n M t i s n ta d t e R s e o a f s b o o n th in o g pponent
strategies through search. and teammate, make the final choice.
Figure 8: Two commonly used reasoning methods in strategic reasoning, along with a hybrid reasoning
approachthatcombinesboth. Theory-of-Mindreasoningemphasizespredictingthepossibleactionsofothers
in a multi-agent environment to guide one’s own behaviour, and Reinforcement Learning-style reasoning
focuses on selecting strategies through exploration and exploitation. These two reasoning methods can also
be integrated to address more complex game scenarios.
internalbeliefsrequiresamorecomprehensiveapproach,assimpleprobescannotcapturemultidimensional
considerations, including accuracy, coherence, uniformity, and practical use. Additionally, it remains
unclear whether LLMs internally distinguish between true and false beliefs and use this distinction when
deciding what to output. Furthermore, although existing work provides theoretical support for belief
revision (Hase et al., 2024), challenges remain in addressing contradictions between old and new beliefs,
handlingmoralbeliefsinambiguoussituations,andrevisingbeliefsacrossmultiplelanguagesandcultures.
These areas still require more explicit theoretical frameworks and further exploration.
3.3 Reasoning Module
Reasoning refers to the process of inferring actions based on one’s preferences and beliefs, as well as the
historical information of other agents. In this context, we focus specifically on strategic reasoning, which
involvestheintermediatecognitiveprocessofarrivingatafinalactionincomplexsocialscenarioscharacter-
izedbymultipleparticipants,diversebehaviours,multi-roundinteractions,dynamicstrategies,andchanging
environments. Chain-of-Thought (Wei et al., 2022) and Tree-of-Thought (Yao et al., 2024), as widely-used
reasoning methods, have already been adopted as baseline approaches in various game-theoretic studies
(Akata et al., 2023; Costarelli et al., 2024; tse Huang et al., 2024). However, strategic reasoning in social
scenarios presents unique challenges. (1) The involvement of multiple participants requires reasoning about
theopponents’mentalstates. (2)Thedynamic nature of the environment necessitatesproactiveexploration
and evaluation of current and future possible states.
To address the first challenge, existing work relies on machine theory-of-mind to achieve the goal of “mind
reading”. Theory-of-Mind (ToM) is a fundamental psychological process involving the ability to attribute
mental states—beliefs, intentions, desires, emotions, knowledge, etc.—to oneself and others (Premack &
Woodruff, 1978). The remarkable progress of LLMs has led to increased attention to whether machine ToM
exists. Preliminary experiments by Bubeck et al. (2023) and Kosinski (2023) have shown that machine ToM
has spontaneously emerged in contemporary LLMs. Consequently, many studies have leveraged machine
ToM to enhance LLMs’ strategic reasoning abilities in social scenarios. For example, Guo et al. (2023)
designed the Suspicion-Agent, which introduces a theory of mind-aware planning approach that leverages
higher-order ToM capabilities, considering not only what the opponent might do (first-order ToM) but also
what the opponent believes Suspicion-Agent will do (second-order ToM). Wang et al. (2023) proposed the
ReCon framework, integrating first-order and second-order perspective transitions to enhance LLM agents’
ability to discern and counteract misinformation. Yim et al. (2024) employed a ToM planning method in
the Guandan poker game to improve understanding of teammates’ and opponents’ beliefs and behavioural
patterns. Liu et al. (2024b) proposed an intention-guided mechanism to enhance intention understanding,
thereby improving game performance. Xu et al. (2023a) introduced Probabilistic Graphical Modeling, en-
riching LLMs’ capabilities in multi-agent environments through ToM reasoning. Additionally, Zhang et al.
11

Published in Transactions on Machine Learning Research (05/2025)
(2024d) proposed K-Level-Reasoning, validated in two games: guessing 0.8 of the average and survival
auction game, essentially a form of high-order ToM reasoning.
To address the second challenge, existing work combines LLMs with reinforcement learning (RL) to achieve
the goal of behaviour exploration and state evaluation in dynamic game environments. Gandhi et al. (2023)
employed in-context learning, using a structured prompt based on search, value assignment, and belief-
tracking strategies to solve strategic reasoning problems. Duan et al. (2024a) proposed ReTA, a set of
LLM-based modules, including the main actor, reward actor, and anticipation actor, based on the concept
of minimax gaming as a problem-solving framework. Zhang et al. (2024e) introduced BIDDER, which
exploresfuturestatesandincorporatesbackwardreasoningduringthereasoningprocess,exploringnewstates
and predicting expected utility, ultimately combining historical and future contexts through bidirectional
reasoning. Yang et al. (2024b) proposed SelfGoal, comprising three modules: the Decomposition Module
for decomposing goals, the Search Module for exploring sub-goals, and the Act Module for taking actions.
ExperimentsinvariouscompetitionandcollaborationscenariosdemonstratethatSelfGoalprovidesprecise
guidance for high-level goals.
Takeaways:
Twocorecharacteristicsofasocialgamearemulti-agentparticipationandenvironmentaldynamics. While
existing research has primarily focused on exploring ToM in relation to the former, the presence of ToM
in LLMs remains contentious. Consequently, relying directly on prompt engineering for ToM-based rea-
soning may not be robust. We propose that a more effective approach would involve integrating symbolic
graphreasoningtodecomposeToMreasoning, therebyenhancingcredibilityandaccuracy. Regardingthe
dynamicnatureoftheenvironment, reinforcementlearningcombinedwithsearchtechniqueshasachieved
significantprogressinareassuchasmathematicalreasoningandcodereasoning. However,thesetechniques
have yet to be explored in the context of game scenarios. Key areas for further exploration include how
to effectively conduct searches within game environments and how to design reward models for dynamic
and complex scenarios.
3.4 PBR-Triangular Interaction
The Preference, Belief, and Reasoning modules each play a crucial role in decision-making for social agents.
However, in practical applications, these modules do not function independently; instead, they exhibit rich
and intricate interactions, collectively influencing the agent’s final decisions. As illustrated in Figure 9,
we provide a comprehensive summary of the Preference-Belief-Reasoning (PBR) triangular interaction and
analyze its effects on the ultimate decision-making process of social agents.
The Preference-Belief Interaction involves bias reinforcement, where preferences influence belief formation,
and preference adaptation, where beliefs reshape preferences based on updated knowledge and observations.
Bias reinforcement (Preference → Belief) highlights how individuals with different preferences develop dis-
tinct beliefs when facing the same situation. For instance, in the Werewolf game, a cooperative and trusting
player is more likely to believe another player claiming, “I am a villager,” whereas a deceptive and skeptical
player is more inclined to doubt the claim, suspecting deception and forming the belief that the opponent is
not a villager. Preference adaptation (Belief → Preference) emphasizes that as beliefs are gradually estab-
lished, iteratively updated, and reinforced by game outcomes, they in turn reshape individual preferences.
Leng & Yuan (2023)foundthatGPT-4,initiallyinclinedtowardfairness,exhibitedashifttowardretaliatory
behavior after experiencing betrayal in a game. Overall, belief formation is influenced not only by objective
factual information but also by subjective individual preferences. At the same time, preferences are not
static—as beliefs evolve through iteration, preferences adjust accordingly.
The Preference-Reasoning Interaction involves value-driven reasoning, where preferences guide decision-
making strategies, and preference optimization, where reasoning refines or adjusts preferences based on
logical analysis and outcomes. Value-driven reasoning (Preference → Reasoning) emphasizes subjective or
intuitive reasoning, where decision-making is guided by personal values and preferences rather than purely
rational calculations. For example, in an auction, even if bidding on a particular item is not the most
optimal financial strategy, a bidder’s personal preference for the item may influence their reasoning process,
12

Published in Transactions on Machine Learning Research (05/2025)
PBR-Triangular Interaction Diagram
Preference
① P → B: Preferences shape how beliefs are formed and interpreted
② B → P: Beliefs influence how preferences evolve based on new information
③ P → R: Preferences guide the reasoning process, influencing decision strategies
④ R → P: Reasoning refines or adjusts preferences based on logical conclusions
⑤Contextual reasoning ⑤ B → R: Beliefs provide the knowledge for reasoning and strategic thinking
Belief Reasoning
⑥Belief revision ⑥ R → B: Reasoning updates beliefs by incorporating logical deductions
Concrete Descriptions and Examples
➢ Scenario: If an AI assistant is designed with a preference for privacy, it may develop a belief that data-
Preference → Belief
(Bias Reinforcement) sharing always carries risks, even when evidence suggests potential benefits.
How Preferences Influence Beliefs ➢ Effect: The Preference Module biases the Belief Module, causing selective belief formation.
➢ Scenario: A poker-playing AI initially avoids bluffing (due to an initial preference for honesty), but after
Belief → Preference
repeatedly observing successful bluffs, it revises its preference to include strategic deception.
(Preference Adaptation)
➢ Effect: The Belief Module influences the Preference Module, adjusting the model’s value system based
How Beliefs Shape Preferences
on new insights.
➢ Scenario: A recommendation system prioritizing user satisfaction may reason that suggesting familiar
Preference → Reasoning
(Value-Driven Reasoning) content is safer, rather than exploring diverse recommendations, to avoid potential user dissatisfaction.
How Preferences Guide Reasoning ➢ Effect: The Preference Module affects the Reasoning Module, shaping decision strategies based on
prioritized values.
➢ Scenario: A self-driving car’s reasoning process determines that aggressive lane-cutting increases
Reasoning → Preference
(Preference Optimization) efficiency but raises accident risks, causing it to adjust its preference toward safer driving strategies.
How Reasoning Refines Preferences ➢ Effect: The Reasoning Module helps optimize the Preference Module, aligning preferences with
practical reasoning.
➢ Scenario: A trading bot believes that market trends follow cyclical patterns, so when reasoning about
Belief → Reasoning
(Contextual Reasoning) investment strategies, it uses historical patterns as a foundation for decision-making.
How Beliefs Provide a ➢ Effect: The Belief Module informs the Reasoning Module, ensuring logical decisions are grounded in
Foundation for Reasoning
prior knowledge.
➢ Scenario: A fraud detection AI initially believes that transactions above $10,000 are suspicious, but
Reasoning → Belief after running extensive analysis, it revises this belief, learning that context (e.g., frequent business
(Belief Revision)
transactions) matters more than transaction size alone.
How Reasoning Updates Beliefs
➢ Effect: The Reasoning Module updates Belief Module, ensuring beliefs evolve based on logical analysis.
Figure9: Theinteractiondiagramofthethreemodules—Preference,Belief,andReasoning—insocialagents.
The upper diagram presents a triangular interaction model summarizing the relationships among the three
modules, while the lower diagram provides a detailed analysis of pairwise interactions, including specific
descriptions and illustrative examples.
leading them to justify the decision based on intrinsic value rather than purely economic considerations.
Preference optimization (Reasoning → Preference) represents a realignment with objective reality, where
reasoning-based evidence updates and refines preferences. This can be seen as a process in which objective
reasoningoverridessubjectiveemotions,requiringindividualstoadjusttheirpreferencesinresponsetological
deductions and real-world evidence. Overall, in social contexts, individual preferences introduce significant
biases in reasoning, while the evidence obtained through reasoning subsequently refines these preferences.
13

Published in Transactions on Machine Learning Research (05/2025)
The Belief-Reasoning Interaction involves contextual reasoning, where beliefs provide the foundation for
logical decision-making, and belief revision, where reasoning updates and refines beliefs based on new ev-
idence and deductions. Contextual reasoning (Belief → Reasoning) refers to rational inference based on
established beliefs. For example, Zhang et al. (2024a) proposed Agent-Pro, which leverages beliefs to cali-
brate agents’ understanding of themselves and their environment, thereby facilitating subsequent reasoning.
Similarly, Kim et al. (2024) construct a belief state through question answering, which refines the decision-
makingprocessofLLMagentsinobservedenvironments. Beliefrevision(Reasoning→Belief)isthedynamic
process of updating an individual’s self-perception and beliefs over time. For instance, Hua et al. (2024a)
introduced bayesian belief updating, enabling agents to refine their beliefs about other players’ valuations
based on reasoning outcomes in the game. In summary, belief provides the factual foundation for reasoning,
while reasoning generates new insights that facilitate belief revision.
Takeaways:
Conceptually,theinteractionsbetweenmodulesareclear;however,inpracticalapplications,thesequence,
frequency, and intensity of these interactions can lead to dynamic and complex states within the social
agent, resulting in varying outcomes. Introducing prior knowledge and manually predefined interaction
processes may yield some effectiveness, but this approach is certainly not efficient. Therefore, we argue
that one of the most important research directions is the design of context-adaptive flows and automated
scheduling algorithms for module interactions. On one hand, the interactions between modules must be
adapted to the specific game scenario at hand, determining the weight distribution of preferences and
beliefs in reasoning, as well as the adjustments and updates of preferences and beliefs based on reasoning
outcomes. Ontheotherhand,theinteractionprocessneedstobeautomated,withthesequence,frequency,
and number of interactions between modules being determined automatically.
4 Evaluation Protocol
In this section, we mainly discuss the evaluation protocol for assessing the game-playing performance of
social agents.
4.1 Game-Agnostic Evaluation
Evaluation in a social game scenario refers to the process of assessing and judging the behaviour of social
agentsacrossoneormoredimensions,eitherqualitativelyorquantitatively. Itisworthnotingthattheestab-
lishmentofevaluationmetricsiscloselytiedtothecredibilityofexperimentalresultsandthegeneralizability
of conclusions.
Game-agnostic evaluation refers to an evaluation approach centred on the outcome of winning or losing
the game. Most directly, the outcome (win/loss) of a game serves as the most straightforward evidence
for assessing the quality of an LLM’s game-playing capabilities. Consequently, win rate is often used as
a primary evaluation metric across a wide range of studies. It is worth noting that, since different game
scenarios have varying criteria for determining victory, it is necessary to set specific win/loss criteria based
ontheresearchcontext,suchasPoker(Huangetal.,2024;Guoetal.,2023;Yimetal.,2024),Werewolf(Xu
et al., 2023d;c; Wu et al., 2024b), Avalon (Wang et al., 2023; Shi et al., 2023; Light et al., 2023a), StarCraft
II (Ma et al., 2023; Shao et al., 2024), Pokémon Battles (Li et al., 2023c), and Murder Mystery Games (Zhu
et al., 2024a). Additionally, Duan et al. (2024b) defined a unified metric, Normalized Relative Advantage, to
measure the extent to which a participant outperforms or underperforms its opponent.
Takeaways:
Undoubtedly, win rate is a highly intuitive metric, but relying solely on win rate to assess gaming per-
formance is far from sufficient. We propose three avenues for extending the win rate metric. First is the
Efficiency-Adjusted Win Rate, which incorporates the efficiency of victories, such as the time taken to
achieve the goal or the resources utilized in doing so. Next is the Comeback Win Rate, which calculates
theproportionofvictoriesachievedafterfacingadisadvantageorfallingbehind,thusassessingtheagent’s
14

Published in Transactions on Machine Learning Research (05/2025)
performance in adversity and its ability to respond to challenges. Finally, the Weighted Win Rate adjusts
winratesbasedontheimportanceofspecificconditionsorsituationsinthegame. Theseexpandedmetrics
offer a more comprehensive understanding of an agent’s gaming abilities.
4.2 Game-Specific Evaluation
Game-specific evaluation refers to the assessment of an agent’s performance in specific aspects of a game.
Beyond the most intuitive win rate, current research increasingly focuses on the behavioural patterns and
performance paradigms of LLMs across different games. Thus, the establishment of evaluation metrics is
closely related to the specific behaviours being assessed. Mao et al. (2023) used survival rates to evaluate
LLMs’abilitytosurviveinresource-scarcescenarios. Inthecontextoftheprisoner’sdilemma,Fontanaetal.
(2024) evaluated LLMs’ behavioural tendencies across five dimensions: niceness, forgiveness, retaliation,
emulation,andtroublemaking. Guoetal.(2024)basedtheirevaluationontherationalityassumption,using
thetrackingofpayoffchangesinauctiongamestodeterminewhetherthemodelbehavesrationally. Maetal.
(2023) introduced metrics such as Population Block Ratio, Resource Utilization Ratio, Average Population
Utilization, and Technology Rate to evaluate LLM performance in StarCraft II. Xia et al. (2024) developed
the Normalized Profits metric in bargaining scenarios to evaluate the profit-acquiring capabilities of Buyers
and Sellers. Zhang et al. (2024e) used average final chips in Limit Texas Hold’em and Pareto Optimality
in negotiation to assess LLM performance. Qi et al. (2024) offered evaluation metrics to assess gameplay
performance across various dimensions, including population, constructed cities, researched technologies,
produced units, and explored territories. Ross et al. (2024) fit utility function parameters to experimental
results to determine whether LLMs exhibit human-like behavioural biases. Chen et al. (2023) employed
TrueSkill, a well-established game rating system, to evaluate the overall capabilities of LLMs in auctions.
In addition to establishing evaluation metrics, some studies have constructed evaluation datasets to assess
modelcapabilitiesduringgameplay. Zhuetal.(2024a)developedtheWellPlayevaluationset,usingmultiple-
choice questions to assess the model’s ability to understand factual information. Wu et al. (2024a) designed
two tasks: Factual Question Answering and Inferential Question Answering, to evaluate the LLMs’ ability
to grasp information and to reason based on that information.
Takeaways:
Thediversityofgamescenariosandevaluationdimensionsinevitablyleadstoavarietyofmetrics. There-
fore, the immediate priority is to develop a comprehensive framework, conceptually constructing an eval-
uation metrics system to guide the design of specific evaluation metrics for various game scenarios. This
evaluationmetricssystemneedstomeettherequirementsofbeinghierarchical,abstract,andquantifiable.
The hierarchical aspect requires the system to comprehensively and clearly categorize different evaluation
dimensions. The abstraction aspect requires the system to include high-level concepts, enabling future
generalization to a broader range of practical scenarios. The quantifiable aspect necessitates that all
metrics have specific calculation methods.
4.3 Performance Assessment of Social Agents
The introduction of various metrics has provided a solid foundation for evaluating the multifaceted gaming
capabilities of social agents, prompting us to consider the question, “What is the current performance of
social agents in game-theoretic scenarios?” To answer this question, we conducted a comprehensive search
and analysis of the existing literature, compiling relevant experimental results. It is worth noting that the
complexity of game scenarios and the variability of evaluation metrics make it challenging to systematically
and uniformly consolidate experimental performance. To overcome this challenge, we propose using the
Relative Agent Score to assess the progress of social agent performance. This metric evaluates the agent’s
gaming capabilities by analyzing the ratio of the agent’s score to the highest possible score (perfect score).
The final results are presented in Table 1.
15

Published in Transactions on Machine Learning Research (05/2025)
Backbone Perfect Human Agent Relative
Type Game Metric Pass
Model Score Score Score AgentScore
-eciohC
emaGgnisucoF
DominantStrategy
Prisoner’sDilemma(Brookins&DeBacker,2023) GPT-3.5 100% - 34.60% 34.60% ✗
SelectionRate
Poker(TexasNo-LimitHold’em)(Zhuangetal.,2025) GPT-4 ActionAccuracy 100% - 65.54% 65.54% ✓
Poker(Guandan)(Yimetal.,2024) GPT-4 Game-specificScore 4 - 2.17 54.25% ✗
StarCraftII(Maetal.,2023) GPT-4 WinRate 100% - 60% 60.00% ✓
Guess2/3oftheAverage(tseHuangetal.,2024) GPT-4 Game-specificScore 100 - 91.60 91.60% ✓
ElFarolBar(tseHuangetal.,2024) GPT-4 Game-specificScore 100 - 23.00 23.00% ✗
DividetheDollar(tseHuangetal.,2024) GPT-4 Game-specificScore 100 - 98.10 98.10% ✓
PublicGoodsGame(tseHuangetal.,2024) GPT-4 Game-specificScore 100 - 89.20 89.20% ✓
Diner’sDilemma(tseHuangetal.,2024) GPT-4 Game-specificScore 100 - 0.90 0.90% ✗
Sealed-BidAuction(tseHuangetal.,2024) GPT-4 Game-specificScore 100 - 24.20 24.20% ✗
BattleRoyale(tseHuangetal.,2024) GPT-4 Game-specificScore 100 - 86.80 86.80% ✓
PirateGame(tseHuangetal.,2024) GPT-4 Game-specificScore 100 - 85.40 85.40% ✓
-noitacinummoC emaGgnisucoF
Gemini-1.5-Flash Efficiency 1 0.89 0.88 88.00% ✓
Bargaining(Shapiraetal.,2024)
Qwen-2-7B Fairness 1 0.71 0.87 87.00% ✓
Llama-3-8B Efficiency 1 0.65 0.75 75.00% ✓
Negotiation(Shapiraetal.,2024)
Llama-3.1-8B Fairness 1 0.39 0.91 91.00% ✓
Qwen-2-7B Efficiency 1 0.55 0.78 78.00% ✓
Persuasion(Shapiraetal.,2024)
Qwen-2-7B Fairness 1 0.41 0.63 63.00% ✓
Werewolf(Xuetal.,2023d) GPT-4 WinRate 100% 52% 52% 52.00% ✗
MurdererIdentification
Jubensha(Wuetal.,2024a) GPT-4 100% - 66% 66.00% ✓
Accuracy
Table 1: The performance summary of the social agent across different games, with data sourced from the
correspondingpapers. The“BackboneModel”referstotheLLMadoptedbythesocialagent,while“Metric”
indicates the performance metric used to evaluate a specific aspect of the game. “Perfect Score” represents
themaximumachievablescoreforthatmetric,“HumanScore”referstothescoreobtainedbyhumanplayers,
and “Agent Score” denotes the score achieved by the agent. “Relative Agent Score” is the ratio of Agent
Score to Perfect Score, calculated by dividing Agent Score by Perfect Score. “Pass” indicates that if the
Relative Agent Score exceeds 60%, the agent is considered to have basic gameplay capabilities.
Firstly, we observe that in the majority of game-theoretic scenarios, social agents achieve a Relative Agent
Score exceeding 60% (a score of 60 is widely recognized as the passing threshold (Kung et al., 2023).),
demonstratingthatcurrentsocialagentspossessfundamentalgamingcapabilities. Furthermore,wefindthat
social agents based on LLMs outperform those in choice-focusing games in communication-focusing games,
indicating that the exceptional language abilities of these models effectively enhance agent performance.
However, in games such as Werewolf, Auction, and Poker (Guanda), the performance of social agents falls
below the passing threshold. In addition, in more games like Poker (Texas No-Limit Hold’em), StarCraft II,
and Jubensha (a Chinese detective role-playing game), social agents only slightly exceed the passing mark.
These results suggest that there is still considerable room for improvement in social agents’ performance
in complex game-theoretic scenarios. Notably, in the classic Prisoner’s Dilemma and Diner’s Dilemma, the
performance of social agents was unexpectedly poor. Based on this, we believe that the absolute rational
decision-making capability of social agents needs further enhancement in future developments.
Additionally,intheWerewolfgame,wefoundthatsocialagentsachievedperformancecomparabletohuman
players,whichaffirmstheprogressmadeinthedevelopmentofsocialagents. Moreover,experimentalresults
from bargaining, negotiation, and persuasion scenarios demonstrate that social agents have advantages over
humans in decision-making efficiency and fairness in decisions.
Takeaways:
The diversity of game scenarios and evaluation metrics makes it challenging to perform horizontal com-
parisons of social agent performance. However, it is essential to provide a timely overview of the progress
in social agent research to facilitate tracking by practitioners. To address this challenge, we propose two
approaches. On one hand, developing evaluation metrics applicable to a wide range of games is crucial.
TheEloratingsystemservesasanexcellentexample,thoughitstilldoesnotmeettheevaluationneedsof
16

Published in Transactions on Machine Learning Research (05/2025)
manygames. Ontheotherhand, integratinghumanplayersintotheexperimentalprocessandcomparing
performance with human players is an effective way to gauge agent progress. By comparing with human
players,qualitativeinsightscanbeprovidedintothecurrentgamingperformanceofagents,andanalyzing
failure cases can offer valuable evidence for iterative development.
5 Practical Guides for Researching Social Agents
In this section, we synthesize insights from existing research to provide design and evaluation guidelines for
social agents, aiming to inform future developments.
5.1 Design of Social Agent
Based on findings from existing studies, we conclude that the Preference, Belief, and Reasoning modules
are indispensable for behaviour control, information perception, and decision planning in social agents. A
modular agent design enables more efficient capability decoupling, facilitates clearer workflow structuring,
and enhances agent robustness. However, their practical implementation presents additional challenges. To
address these, we propose the following development guidelines:
• Incorporating the Preference Module enables high-level control over agent behaviour.
Akeychallengeliesinmitigatingtheinstabilityofprompt-basedapproachesandensuringlong-term
consistencyintheagent’sbehaviouralpreferences. Onepossiblesolutionistointegratereinforcement
learningwithhumanfeedback(RLHF)toiterativelyrefinetheagent’spreferencealignment,reducing
relianceonstaticpromptsandimprovingconsistencyoverextendedinteractions. Anotherapproach
is to develop memory-augmented architectures, allowing the agent to maintain and retrieve past
preference-related decisions, thereby ensuring coherence in long-term behavioural patterns.
• IntegratingtheBeliefModuleenhancesinformationperceptionaccuracyandbehaviour
interpretability. Theprimarychallengeisenablingtheagenttoadaptivelyreviseitsbeliefsincom-
plex and dynamic environments. One solution is to implement Bayesian belief updating, where the
agent continuously refines its belief state based on new evidence, ensuring adaptability in uncer-
tain or multi-agent interactions. Another approach is to employ graph-based belief representation,
where relationships between entities and past interactions are dynamically updated, allowing for
more structured and interpretable belief revisions.
• Adopting Hybrid-Strategy Reasoning improves the agent’s information analysis and
decision accuracy in complex scenarios. The challenge is balancing the trade-off between
computationally intensive reasoning and the need for real-time decision-making. One solution is to
use hierarchical reasoning, where lightweight heuristic-based reasoning is applied in time-sensitive
situations, while more complex computations are reserved for critical decision points. Another
approach is to implement meta-reasoning techniques, enabling the agent to assess the complexity of
a given situation and selectively allocate computational resources to optimize speed and accuracy.
• Designing dynamic interactions among the Preference, Belief, and Reasoning (PBR)
modules based on specific task contexts can further enhance their synergy. Thechallenge
isdevelopinganadaptiveinteractionflowthatautomaticallyadjustsbasedongame-statevariations.
One solution is to use reinforcement learning-based scheduling, where the interaction sequence be-
tween modules is optimized dynamically based on reward signals from past performance. Another
approach is to implement attention-based mechanisms, allowing the agent to selectively prioritize
information flow between the modules in response to evolving task requirements.
• Testing social agents on diverse large language models improves the robustness of the
design framework and ensures generalizability across different model architectures.
These tests can be conducted across models of varying sizes (e.g., 1B, 7B, 72B parameters) to eval-
uateperformancescalability. Additionally, assessmentsshouldcoverdifferent model types, including
17

Published in Transactions on Machine Learning Research (05/2025)
Category EvaluationFocus ChallengesforSocialAgents Games
Basic Social Dilemma Social cooperation, fairness, altru- Balancingself-interestandcooperation; Prisoner’s Dilemma, Dicta-
& Economic Decision ism,strategicreciprocity learningfairnessnorms;adaptingstrate- torGame,UltimatumGame,
Games giesdynamically PublicGoodsGame
Coordination & Con- Coordination, equilibrium selection, Navigatingmultipleequilibria;resolving Battle of the Sexes, Ring-
flictResolutionGames trust-building coordinationfailures;adaptingtouncer- NetworkGames
tainpartnerbehaviors
Competitive & Strate- Bluffing,riskassessment,hiddenin- Modeling opponents; reasoning under Texas No-Limit Hold’em,
gic Reasoning Games – formationmanagement uncertainty; balancing exploitation vs. LeducHold’em,Guandan
Poker-Based exploration
Competitive & Strate- Biddingstrategies,valuationestima- Learningoptimalbids;modellingasym- First-pricesealed-bidauction,
gic Reasoning Games – tion,adversarialcompetition metric information; managing dynamic Private-value second-price
Auction-Based pricing auction, Open ascending-
priceauction
Long-Horizon Strategy Multi-step planning, hierarchical Combinatorial action spaces; long-term StarCraftII,Chess
& Multi-Agent Plan- decision-making, opponent mod- foresight;real-timeadaptiveplanning
ningGames elling
SocialDeduction&Ne- Persuasion, alliance formation, Long-term commitments; cooperation Negotiation,Diplomacy
gotiation Games – Ne- strategicdeception vs. betrayal;nuancedcommunication
gotiation&Diplomacy
SocialDeduction&Ne- Socialinference,deceptiondetection, Detectingimplicitcues; deceivingwith- Avalon, Murder Mystery
gotiation Games – De- trustdynamics outexposure;reasoningunderambiguity Games,Jubensha
ception&Role-Playing
Table 2: Guidelines for selecting game scenarios in social agent evaluation.
base models, instruct models, and reasoning models. Furthermore, experiments should incorporate
models from different providers, such as Gemma, LLaMA, and Qwen, to examine how architectural
and training variations impact the social agent’s behaviour and adaptability.
5.2 Evaluation of Social Agent
Evaluating social agents is a critical step toward understanding their strengths, limitations, and real-world
applicability. Given the multifaceted nature of social intelligence—ranging from cooperation and coordina-
tion to deception and negotiation—it is essential to choose evaluation scenarios that align closely with the
desired capabilities under assessment.
To this end, we provide a structured framework (see Table 2) that categorizes representative game environ-
ments based on their core interaction patterns and cognitive demands. These categories include basic social
dilemmas, coordination and conflict resolution, competitive strategic reasoning, long-horizon planning, and
social deduction and negotiation. Each game type highlights specific evaluation objectives, such as fairness,
trust-building, opponent modeling, or multi-agent planning, thereby offering targeted benchmarks for as-
sessing different dimensions of social competence. This categorization not only helps standardize evaluation
protocols but also serves as a practical guide for selecting game scenarios tailored to particular research
questionsordevelopmentgoals. Byaligninggameselectionwithevaluationobjectives, researcherscanmore
effectively assess the emergent behaviors, reasoning capabilities, and interactive robustness of social agents.
6 Future Directions
6.1 Standardized Benchmark Generation
Thediversityandlackofstandardizationincurrentgametypes—oftendesignedindependentlybydevelopers
withheterogeneousrepresentations—posesignificantchallengesforthelarge-scaleevaluationofsocialagents.
This fragmentation makes it difficult to conduct efficient and reproducible benchmarking. Therefore, there
is an urgent need for a standardized benchmark that offers broad coverage of game types, a consistent game
description format, support for diverse agent architectures, and clearly defined evaluation metrics. Inspired
18

Published in Transactions on Machine Learning Research (05/2025)
by platforms like OpenCompass (Contributors, 2023), such a benchmark should enable one-click evaluation
by allowing users to configure the game environment, specify the agents to be tested, and select the desired
evaluation metrics.
However,LLMsaretypicallypre-trainedonvastamountsofdata,whichmayincludepubliclyavailablegame
datasets—raising concerns about data leakage and overfitting. To mitigate this issue, synthetic game data
generation has emerged as a promising approach (Long et al., 2024). By leveraging classic game structures,
LLMs can generate novel and diverse game scenarios through contextual reframing (Lorè & Heydari, 2024),
producing out-of-distribution benchmarks that better evaluate an agent’s generalization ability.
More concretely, two complementary strategies can be employed for scenario generation. From a structural
perspective, developers can extract and manipulate the game’s payoff matrix to construct new strategic
settingswhilepreservingcoregamemechanics. Fromasemanticperspective,LLMscanbeusedtoreinterpret
orre-describeexistinggames, generatingalternativeformulationsthatyieldnovelevaluationscenarioswhile
maintaining logical coherence.
6.2 Reinforcement Learning Agents
Although current social agents have demonstrated promising performance across various game scenarios,
existing research highlights notable limitations in multi-round, long-horizon, and complex multi-agent envi-
ronments, where performance often degrades. This suggests that LLM-driven planning and decision-making
aloneareinsufficientforachievingrobust, scalablesocialintelligence. Toaddressthesechallenges, futurere-
searchshouldexploretheintegrationofreinforcementlearning(RL)—particularlymulti-agentreinforcement
learning (MARL)—to enhance state-space exploration, long-term adaptability, and emergent coordination.
MARL offers several insights that are highly relevant for improving LLM-based social agents. For
instance, techniques such as centralized training with decentralized execution (CTDE) (Amato, 2024)
can be used to guide LLM policy adaptation while preserving individual autonomy. Additionally, op-
ponent modelling (He et al., 2016), credit assignment (Kazemnejad et al., 2024), and policy regulariza-
tion (Cheng et al., 2019) in MARL can improve the agent’s responsiveness to strategic variability and en-
hancegeneralizationacrossdiversesocialcontexts. However,integratingMARLintoLLMtrainingintroduces
new challenges. These include efficiency concerns, as LLMs are computationally intensive and may require
specialized architectures or curriculum learning to reduce sample complexity; generalization gaps, especially
whentransferringlearnedbehavioursacrossdifferentsocialrolesortaskdomains;andtheneedforconsistent
persona and belief modelling across episodes. Advancing this hybrid paradigm will also require fine-grained
evaluation frameworks capable of tracing not just final performance but the underlying reasoning dynamics,
theory-of-mind modelling, and role consistency throughout interactions.
6.3 Behaviour Pattern Mining
Existing studies primarily focus on predefined scenarios to examine the behaviour patterns of agents. How-
ever, withtheadvancementofmulti-agentsimulations, anintriguingdirectionistheautomateddiscoveryof
game behaviour patterns that emerge spontaneously from agent interactions. It is important to note that,
beyond explicit behaviours like cooperation, coordination, and betrayal, implicit causal relationships and
long-term behavioural patterns should also be explored.
To mine such patterns, several methodological approaches can be leveraged. Unsupervised learning
techniques, such as clustering and representation learning, can help identify latent behaviour categories
and temporal motifs across trajectories (Rawassizadeh et al., 2016). Causal inference frameworks (e.g.,
Granger causality or structural causal models) can reveal inter-agent influence and dependency struc-
tures over time (Qiu et al., 2012). Additionally, trajectory segmentation and sequential pattern min-
ing can be used to extract frequent decision sequences that correspond to strategic routines or social
norms (Giannotti et al., 2007). Leveraging graph-based analysis of interaction networks can also shed light
on evolving social roles and influence hierarchies within agent populations (Atzmueller, 2014). These ap-
proaches not only facilitate a deeper understanding of agents’ behavioural preferences and latent traits but
19

Published in Transactions on Machine Learning Research (05/2025)
alsoenablethestudyofhowsuchpatternsautonomouslyemerge—offeringvaluableinsightsforbothAIand
human behavioural research.
6.4 Pluralistic Game-Theoretic Scenarios
Althoughexistingresearchhasmadenotablestridesacrossawiderangeofgame-theoreticscenarios,therere-
mainsagapinthestudyofpluralisticgameenvironments—settingsthatinvolvemultiplelanguages,cultural
norms, value systems, policies, and goals. These pluralistic scenarios introduce new layers of complexity, in-
cluding behavioral preferences shaped by culturally grounded norms, value misalignment across agents, and
belief conflicts arising from divergent objectives (Orner et al., 2024). Such dynamics pose unique challenges
for the design and evaluation of socially intelligent agents and demand deeper exploration.
To develop robust pluralistic game-theoretic scenarios, several key desiderata should be considered: (1)
Heterogeneity of agent profiles, including cultural, linguistic, and normative diversity; (2) Multi-objective
frameworks, where agents pursue partially conflicting goals; and (3) Rich communicative channels, enabling
nuancedlanguageuse,code-switching,orculturallyspecificcues. Evaluatingagentsinthesesettingsrequires
multi-facetedmetrics. Inadditiontotaskperformance,evaluationsshouldaccountfornormsensitivity,value
alignment,cross-culturaladaptability,andtheagent’sabilitytomediateornegotiateamongconflictingbelief
systems. Metrics such as cultural appropriateness, interaction fluency, and conflict resolution success can
serve as important complementary indicators. Scenario generation can be approached in two ways: from
a knowledge-based perspective, designers can draw from real-world policy conflicts, international relations,
or sociocultural theory to construct grounded simulation environments. From a data-driven perspective,
large language models can be used to simulate role-play dialogues or generate scenarios by conditioning on
demographic or cultural descriptors, yielding diverse and customizable pluralistic environments.
7 Related Works
Thehuman-likecapabilitiesofLLMshavedrawnsignificantattentionfromsocialscienceresearchers,prompt-
ing extensive exploration at the intersection of AI and social sciences (Xu et al., 2024a). A key development
in this area is the shift from traditional Agent-Based Modeling to LLM-based agents, as explained by Ma
et al. (2024) through computational experiments. Numerous studies have since applied LLM-based agents
to diverse game scenarios, such as poker, Minecraft, and DOTA II, with more detailed summaries provided
by(Xuetal.,2024b;Huetal.,2024b;a). Furthermore,Zhangetal.(2024c)haveanalyzedthecorestrategic
reasoningcapabilitiesoftheseagents,distinguishingthemfromotherreasoningapproaches. Whiletheprevi-
ousreviewsprovidecomprehensiveoverviewsofrelatedfields,oursurveyspecificallyfocusesonsocialagents
equipped with beliefs, preferences, and reasoning capabilities within diverse game-theoretic scenarios.
8 Conclusion
We provide a comprehensive summary of existing research on LLM-based social agents in game-theoretic
scenarios from three perspectives: game framework, social agents, and evaluation protocol. This interdisci-
plinary fieldcovers awide range of topics, including social sciences, economics, decision sciences, and theory
ofmind. Currentstudieshaveprimarilyexploredthemoredirectexternalbehaviouralpatternsandinternal
cognition of social agents. Therefore, future research should focus on developing theoretical frameworks
for cognitive representations within LLMs, conducting in-depth analyses of implicit and long-term game
behaviour patterns, and enhancing agents’ reasoning and planning capabilities in dynamic environments.
Broader Impact Statement
Developing agents with advanced social intelligence is one of the ultimate goals of artificial intelligence. On
one hand, such agents demonstrate enhanced collaboration, a deeper understanding of mental states, and
seamlessintegrationintohumansociety. Ontheotherhand,negativesocialbehaviorsmayalsoemerge,such
as deception, malicious competition, and verbal aggression, which conflict with the vision of a harmonious
human-AI coexistence.
20

Published in Transactions on Machine Learning Research (05/2025)
Therefore,wecarefullyexaminethepotentialnegativeimpactsthatsocialagentsmayhaveonhumansociety,
serving as a cautionary perspective for future social agent development. One major concern is deception
and manipulation, where agents may bluff or mislead to achieve strategic goals. They may also engage in
malicious competition, exploiting others to gain advantage, or exhibit verbal and social aggression, such as
generating insults or polarizing language. Additionally, social agents can amplify societal biases, leading to
discriminatorybehaviors,andcontributetotheerosion of trust,especiallywhenusersstruggletodistinguish
genuine human interactions from artificial ones. These agents may further undermine human autonomy by
subtly steering decisions through persuasion, often without transparency. Due to their scalability of harm,
even a single flawed agent can rapidly propagate misinformation or harmful behaviors across platforms.
Moreover, the risk of impersonation and infiltration arises when agents mimic human users, potentially
deceiving communities or individuals. These challenges highlight the critical need for careful design, value
alignment, and robust supervision in the development and deployment of socially intelligent agents.
We now categorize the development and deployment of social agents into four stages:(1) Designing social
agents, (2) Evaluating social agents, (3) Deploying social agents, and (4) Supervising social agents. Ac-
cordingly, we discuss the potential risks and feasible mitigation strategies for each stage. Design Phase:
The underlying algorithms determine the agent’s behavioral preferences. Poorly designed algorithms may
inadvertently lead to negative behaviors. To address this, researchers should enhance alignment algorithms,
including safety alignment and moral alignment, to mitigate these risks at a fundamental level. Another
promisingapproachisthedesignofbehavioralplugins,wheresmallmodelstrainedasplug-and-playbehavior
controllers can regulate agent actions dynamically. Evaluation Phase: Rigorous evaluation is crucial before
deployingsocialagentsinreal-worldapplications. Agentsexhibitingnegativebehaviorsshouldbeprevented
from entering the deployment phase. One effective approach is to evaluate social agents across diverse game
scenarios, allowing for a benchmarking framework that assesses their behavioral preferences under dynamic
conditions. Deployment Phase: Directlarge-scaledeploymentmayleadtounforeseennegativeconsequences
that were not observed in smaller-scale testing. Therefore, social agents should first be deployed in low-risk,
small-scale environments, with a gradual expansion in scope and scale to monitor anomalies in real time.
Supervision Phase: Effective oversight of social agents is essential. This can be achieved by designing auto-
mated monitoring systems that enable large-scale real-time surveillance. Behavioral analysis can be used to
issue early warnings, assisting human supervisors in decision-making.
Additionally, it is important to note that most of the studies referenced in this paper utilize the GPT series
as the large language model, which limits the generalizability of the experimental results. Differences in
modelarchitectures,trainingdata,andalignmenttechniquescansignificantlyimpactthebehavioralpatterns
exhibitedbydifferentmodels. Futureresearchshouldexploreabroaderrangeoflargelanguagemodels,such
as Claude, Gemini, Llama, and DeepSeek, to derive more comprehensive and reliable conclusions.
Acknowledgments
ThisworkwassupportedbyHongKongInnovationandTechnologySupportProgrammePlatformResearch
Project fund (ITS/269/22FP).
References
Sahar Abdelnabi, Amr Gomaa, Sarath Sivaprasad, Lea Schönherr, and Mario Fritz. Llm-deliberation: Eval-
uating llms with interactive multi-agent negotiation games. ArXiv preprint, abs/2309.17234, 2023. URL
https://arxiv.org/abs/2309.17234.
Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo
Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. Gpt-4 technical report. ArXiv
preprint, abs/2303.08774, 2023. URL https://arxiv.org/abs/2303.08774.
Gati Aher, RosaI. Arriaga, and Adam Tauman Kalai. Using large language models to simulate multiple
humans and replicate human subject studies. In International Conference on Machine Learning, 2022.
URL https://api.semanticscholar.org/CorpusID:251719353.
21

Published in Transactions on Machine Learning Research (05/2025)
Elif Akata, Lion Schulz, Julian Coda-Forno, Seong Joon Oh, Matthias Bethge, and Eric Schulz. Playing
repeatedgameswithlargelanguagemodels. ArXiv preprint,abs/2305.16867,2023. URLhttps://arxiv.
org/abs/2305.16867.
ChristopherAmato. Anintroductiontocentralizedtrainingfordecentralizedexecutionincooperativemulti-
agent reinforcement learning. arXiv preprint arXiv:2409.03052, 2024.
Martin Atzmueller. Data mining on social interaction networks. Journal of Data Mining & Digital Human-
ities, 2014, 2014.
Suma Bailis, Jane Friedhoff, and Feiyang Chen. Werewolf arena: A case study in llm evaluation via social
deduction. ArXiv preprint, abs/2407.13943, 2024. URL https://arxiv.org/abs/2407.13943.
Anton Bakhtin, Noam Brown, Emily Dinan, Gabriele Farina, Colin Flaherty, Daniel Fried, Andrew Goff,
JonathanGray, HengyuanHu, AthulPaulJacob, MojtabaKomeili, KarthikKonath, MinaeKwon, Adam
Lerer,MikeLewis,AlexanderH.Miller,SandraMitts,AdithyaRenduchintala,StephenRoller,DirkRowe,
Weiyan Shi, Joe Spisak, Alexander Wei, David J. Wu, Hugh Zhang, and Markus Zijlstra. Human-level
play in the game of diplomacy by combining language models with strategic reasoning. Science, 378:1067
– 1074, 2022. URL https://api.semanticscholar.org/CorpusID:253759631.
Michael L Barnes and Robert J Sternberg. Social intelligence and decoding of nonverbal cues. Intelligence,
13(3):263–287, 1989.
Max H Bazerman, Jared R Curhan, Don A Moore, and Kathleen L Valley. Negotiation. Annual review of
psychology, 51(1):279–314, 2000.
Federico Bianchi, Patrick John Chia, Mert Yuksekgonul, Jacopo Tagliabue, Dan Jurafsky, and James Zou.
How well can llms negotiate? negotiationarena platform and analysis. ArXiv preprint, abs/2402.05863,
2024. URL https://arxiv.org/abs/2402.05863.
Matteo Bortoletto, Constantin Ruhdorfer, Lei Shi, and Andreas Bulling. Benchmarking mental state rep-
resentations in language models. ArXiv preprint, abs/2406.17513, 2024. URL https://arxiv.org/abs/
2406.17513.
Philip Brookins and Jason Matthew DeBacker. Playing games with gpt: What can we learn about a large
language model from canonical strategic games? Available at SSRN 4493398, 2023.
Sébastien Bubeck, Varun Chandrasekaran, Ronen Eldan, Johannes Gehrke, Eric Horvitz, Ece Kamar, Peter
Lee, Yin Tat Lee, Yuanzhi Li, Scott Lundberg, et al. Sparks of artificial general intelligence: Early
experiments with gpt-4. ArXiv preprint, abs/2303.12712, 2023. URL https://arxiv.org/abs/2303.
12712.
Colin F Camerer. Behavioral game theory: Experiments in strategic interaction. Princeton university press,
2011.
JiangjieChen, SiyuYuan, RongYe, BodhisattwaPrasad Majumder, andKyle Richardson. Put yourmoney
whereyourmouthis: Evaluatingstrategicplanningandexecutionofllmagentsinanauctionarena. ArXiv
preprint, abs/2310.05746, 2023. URL https://arxiv.org/abs/2310.05746.
Jiangjie Chen, Xintao Wang, Rui Xu, Siyu Yuan, Yikai Zhang, Wei Shi, Jian Xie, Shuang Li, Ruihan Yang,
Tinghui Zhu, et al. From persona to personalization: A survey on role-playing language agents. ArXiv
preprint, abs/2404.18231, 2024a. URL https://arxiv.org/abs/2404.18231.
Zehui Chen, Kuikun Liu, Qiuchen Wang, Jiangning Liu, Wenwei Zhang, Kai Chen, and Feng Zhao. Mind-
search: Mimicking human minds elicits deep ai searcher. ArXiv preprint, abs/2407.20183, 2024b. URL
https://arxiv.org/abs/2407.20183.
Richard Cheng, Abhinav Verma, Gabor Orosz, Swarat Chaudhuri, Yisong Yue, and Joel Burdick. Con-
trol regularization for reduced variance reinforcement learning. In International Conference on Machine
Learning, pp. 1141–1150. PMLR, 2019.
22

Published in Transactions on Machine Learning Research (05/2025)
Yizhou Chi, Lingjun Mao, and Zineng Tang. Amongagents: Evaluating large language models in the
interactive text-based social deduction game. ArXiv preprint, abs/2407.16521, 2024. URL https:
//arxiv.org/abs/2407.16521.
OpenCompass Contributors. Opencompass: A universal evaluation platform for foundation models. https:
//github.com/open-compass/opencompass, 2023.
AnthonyCostarelli, MatAllen, RomanHauksson, GraceSodunke, SuhasHariharan, CarlsonCheng, Wenjie
Li, and Arjun Yadav. Gamebench: Evaluating strategic reasoning abilities of llm agents. ArXiv preprint,
abs/2406.06613, 2024. URL https://arxiv.org/abs/2406.06613.
DaantjeDerks,ArjanERBos,andJasperVonGrumbkow. Emoticonsandsocialinteractionontheinternet:
the importance of social context. Computers in human behavior, 23(1):842–849, 2007.
Jinhao Duan, Shiqi Wang, James Diffenderfer, Lichao Sun, Tianlong Chen, Bhavya Kailkhura, and Kaidi
Xu. Reta: Recursively thinking ahead to improve the strategic reasoning of large language models. In
Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational
Linguistics: Human Language Technologies (Volume 1: Long Papers), pp. 2232–2246, 2024a.
Jinhao Duan, Renming Zhang, James Diffenderfer, Bhavya Kailkhura, Lichao Sun, Elias Stengel-Eskin,
Mohit Bansal, Tianlong Chen, and Kaidi Xu. Gtbench: Uncovering the strategic reasoning limitations of
llms via game-theoretic evaluations. ArXiv preprint, abs/2402.12348, 2024b. URL https://arxiv.org/
abs/2402.12348.
Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman,
Akhil Mathur, Alan Schelten, Amy Yang, Angela Fan, et al. The llama 3 herd of models. ArXiv preprint,
abs/2407.21783, 2024. URL https://arxiv.org/abs/2407.21783.
Caoyun Fan, Jindou Chen, Yaohui Jin, and Hao He. Can large language models serve as rational players in
game theory? a systematic analysis. ArXiv preprint, abs/2312.05488, 2023. URL https://arxiv.org/
abs/2312.05488.
Xidong Feng, Yicheng Luo, Ziyan Wang, Hongrui Tang, Mengyue Yang, Kun Shao, David Mguni, Yali
Du, and Jun Wang. Chessgpt: Bridging policy learning and language modeling. Advances in Neural
Information Processing Systems, 36, 2024.
Chaim Fershtman. The importance of the agenda in bargaining. Games and Economic Behavior, 2(3):
224–238, 1990.
Nicol’oFontana,FrancescoPierri,andLucaMariaAiello. Nicerthanhumans: Howdolargelanguagemodels
behaveintheprisoner’sdilemma? ArXivpreprint,abs/2406.13605,2024. URLhttps://arxiv.org/abs/
2406.13605.
MartinEFordandMarieSTisak. Afurthersearchforsocialintelligence. JournalofEducationalPsychology,
75(2):196, 1983.
Yao Fu, Hao Peng, Tushar Khot, and Mirella Lapata. Improving language model negotiation with self-
play and in-context learning from ai feedback. ArXiv preprint, abs/2305.10142, 2023. URL https:
//arxiv.org/abs/2305.10142.
Drew Fudenberg and Jean Tirole. Game theory. MIT press, 1991.
Kanishk Gandhi, Dorsa Sadigh, and Noah D Goodman. Strategic reasoning with language models. ArXiv
preprint, abs/2305.19165, 2023. URL https://arxiv.org/abs/2305.19165.
Kanishk Gandhi, Jan-Philipp Fränken, Tobias Gerstenberg, and Noah Goodman. Understanding social
reasoninginlanguagemodelswithlanguagemodels. Advances in Neural Information Processing Systems,
36, 2024.
23

Published in Transactions on Machine Learning Research (05/2025)
Michael Georgeff, Barney Pell, Martha Pollack, Milind Tambe, and Michael Wooldridge. The belief-desire-
intention model of agency. In Intelligent Agents V: Agents Theories, Architectures, and Languages: 5th
International Workshop, ATAL’98 Paris, France, July 4–7, 1998 Proceedings 5, pp. 1–10. Springer, 1999.
FoscaGiannotti, MircoNanni, FabioPinelli, andDinoPedreschi. Trajectorypatternmining. InProceedings
ofthe13thACMSIGKDDinternationalconferenceonKnowledgediscoveryanddatamining,pp.330–339,
2007.
AlisonGopnikandJanetWAstington. Children’sunderstandingofrepresentationalchangeanditsrelation
to the understanding of false belief and the appearance-reality distinction. Child development, pp. 26–37,
1988.
Zhenyu Guan, Xiangyu Kong, Fangwei Zhong, and Yizhou Wang. Richelieu: Self-evolving llm-based agents
for ai diplomacy. ArXiv preprint, abs/2407.06813, 2024. URL https://arxiv.org/abs/2407.06813.
Fulin Guo. Gpt in game theory experiments. ArXiv preprint, abs/2305.05516, 2023. URL https://arxiv.
org/abs/2305.05516.
Jiaxian Guo, Bo Yang, Paul Yoo, Bill Yuchen Lin, Yusuke Iwasawa, and Yutaka Matsuo. Suspicion-agent:
Playing imperfect information games with theory of mind aware gpt-4. ArXiv preprint, abs/2309.17277,
2023. URL https://arxiv.org/abs/2309.17277.
ShangminGuo,HaoranBu,HaochuanWang,YiRen,DianboSui,YumingShang,andSitingLu. Economics
arena for large language models. ArXiv preprint, abs/2401.01735, 2024. URL https://arxiv.org/abs/
2401.01735.
Akshat Gupta. Are chatgpt and gpt-4 good poker players?–a pre-flop analysis. ArXiv preprint,
abs/2308.12466, 2023. URL https://arxiv.org/abs/2308.12466.
Peter Hase, Thomas Hofweber, Xiang Zhou, Elias Stengel-Eskin, and Mohit Bansal. Fundamental problems
with model editing: How should rational belief revision work in llms? ArXiv preprint, abs/2406.19354,
2024. URL https://arxiv.org/abs/2406.19354.
He He, Jordan Boyd-Graber, Kevin Kwok, and Hal Daumé III. Opponent modeling in deep reinforcement
learning. In International conference on machine learning, pp. 1804–1813. PMLR, 2016.
DanielAHerrmannandBenjaminALevinstein. Standardsforbeliefrepresentationsinllms. ArXivpreprint,
abs/2405.21030, 2024. URL https://arxiv.org/abs/2405.21030.
JohnJ.Horton. Largelanguagemodelsassimulatedeconomicagents: Whatcanwelearnfromhomosilicus?
SSRN Electronic Journal, 2023. URL https://api.semanticscholar.org/CorpusID:255152420.
Dirk Hovy and Diyi Yang. The importance of modeling social factors of language: Theory and practice. In
Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational
Linguistics: Human Language Technologies, pp. 588–602, Online, 2021. Association for Computational
Linguistics.doi: 10.18653/v1/2021.naacl-main.49.URLhttps://aclanthology.org/2021.naacl-main.
49.
Chengpeng Hu, Yunlong Zhao, Ziqi Wang, Haocheng Du, and Jialin Liu. Games for artificial intelligence
research: A review and perspectives. IEEE Transactions on Artificial Intelligence, 2024a.
Sihao Hu, Tiansheng Huang, Fatih Ilhan, Selim Tekin, Gaowen Liu, Ramana Kompella, and Ling Liu.
A survey on large language model-based game agents. ArXiv preprint, abs/2404.02039, 2024b. URL
https://arxiv.org/abs/2404.02039.
Wenyue Hua, Ollie Liu, Lingyao Li, Alfonso Amayuelas, Julie Chen, Lucas Jiang, Mingyu Jin, Lizhou Fan,
Fei Sun, William Wang, et al. Game-theoretic llm: Agent workflow for negotiation games. arXiv preprint
arXiv:2411.05990, 2024a.
24

Published in Transactions on Machine Learning Research (05/2025)
Yuncheng Hua, Lizhen Qu, and Gholamreza Haffari. Assistive large language model agents for socially-
aware negotiation dialogues. ArXiv preprint, abs/2402.01737, 2024b. URL https://arxiv.org/abs/
2402.01737.
Chenghao Huang, Yanbo Cao, Yinlong Wen, Tao Zhou, and Yanru Zhang. Pokergpt: An end-to-end
lightweightsolverformulti-playertexashold’emvialargelanguagemodel.ArXivpreprint,abs/2401.06781,
2024. URL https://arxiv.org/abs/2401.06781.
Thelma Hunt. The measurement of social intelligence. Journal of Applied Psychology, 12(3):317, 1928.
Jingru Jia, Zehua Yuan, Junhao Pan, Paul E McNamara, and Deming Chen. Decision-making behavior
evaluation framework for llms under uncertain context. arXiv preprint arXiv:2406.05972, 2024.
Albert Q Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot, Diego
de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile Saulnier, et al. Mistral 7b.
ArXiv preprint, abs/2310.06825, 2023. URL https://arxiv.org/abs/2310.06825.
Xuanfa Jin, Ziyan Wang, Yali Du, Meng Fang, Haifeng Zhang, and Jun Wang. Learning to discuss strate-
gically: A case study on one night ultimate werewolf. ArXiv preprint, abs/2405.19946, 2024. URL
https://arxiv.org/abs/2405.19946.
Chani Jung, Dongkwan Kim, Jiho Jin, Jiseon Kim, Yeon Seonwoo, Yejin Choi, Alice Oh, and Hyunwoo
Kim. Perceptions to beliefs: Exploring precursory inferences for theory of mind in large language models.
ArXiv preprint, abs/2407.06004, 2024. URL https://arxiv.org/abs/2407.06004.
JohnHKagelandDanLevin.Thewinner’scurseandpublicinformationincommonvalueauctions.American
economic review, 76(5):894–920, 1986.
Nora Kassner, Oyvind Tafjord, Ashish Sabharwal, Kyle Richardson, Hinrich Schuetze, and Peter Clark.
Languagemodelswithrationality. ArXiv preprint,abs/2305.14250,2023. URLhttps://arxiv.org/abs/
2305.14250.
Amirhossein Kazemnejad, Milad Aghajohari, Eva Portelance, Alessandro Sordoni, Siva Reddy, Aaron
Courville, and Nicolas Le Roux. Vineppo: Unlocking rl potential for llm reasoning through refined credit
assignment. arXiv preprint arXiv:2410.01679, 2024.
John F Kihlstrom and Nancy Cantor. Social intelligence. Handbook of intelligence, 2:359–379, 2000.
Minsoo Kim, Jongyoon Kim, Jihyuk Kim, and Seung-won Hwang. QuBE: Question-based belief en-
hancement for agentic LLM reasoning. In Yaser Al-Onaizan, Mohit Bansal, and Yun-Nung Chen
(eds.), Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pp.
21403–21423, Miami, Florida, USA, November 2024. Association for Computational Linguistics. doi:
10.18653/v1/2024.emnlp-main.1193. URL https://aclanthology.org/2024.emnlp-main.1193/.
Henry Kissinger. Diplomacy. In Geopolitics, pp. 114–115. Routledge, 2014.
Michal Kosinski. Theory of mind might have spontaneously emerged in large language models. ArXiv
preprint, abs/2302.02083, 2023. URL https://arxiv.org/abs/2302.02083.
Tiffany H Kung, Morgan Cheatham, Arielle Medenilla, Czarina Sillos, Lorie De Leon, Camille Elepaño,
Maria Madriaga, Rimel Aggabao, Giezel Diaz-Candido, James Maningo, et al. Performance of chatgpt on
usmle: potential for ai-assisted medical education using large language models. PLoS digital health, 2(2):
e0000198, 2023.
Bolin Lai, Hongxin Zhang, Miao Liu, Aryan Pariani, Fiona Ryan, Wenqi Jia, Shirley Anugrah Hayati,
James M Rehg, and Diyi Yang. Werewolf among us: A multimodal dataset for modeling persuasion
behaviors in social deduction games. ArXiv preprint, abs/2212.08279, 2022. URL https://arxiv.org/
abs/2212.08279.
25

Published in Transactions on Machine Learning Research (05/2025)
Yihuai Lan, Zhiqiang Hu, Lei Wang, Yang Wang, De-Yong Ye, Peilin Zhao, Ee-Peng Lim, Hui Xiong, and
Hao Wang. Llm-based agent society investigation: Collaboration and confrontation in avalon gameplay.
ArXiv preprint, abs/2310.14985, 2023. URL https://arxiv.org/abs/2310.14985.
Yan Leng and Yuan Yuan. Do llm agents exhibit social behavior? ArXiv preprint, abs/2312.15198, 2023.
URL https://arxiv.org/abs/2312.15198.
BenjaminALevinsteinandDanielAHerrmann. Stillnoliedetectorforlanguagemodels: Probingempirical
and conceptual roadblocks. Philosophical Studies, pp. 1–27, 2024.
Huao Li, Yu Quan Chong, Simon Stepputtis, Joseph Campbell, Dana Hughes, Michael Lewis, and Ka-
tia Sycara. Theory of mind for multi-agent collaboration via large language models. ArXiv preprint,
abs/2310.10701, 2023a. URL https://arxiv.org/abs/2310.10701.
JiatongLi,RuiLi,andQiLiu. Beyondstaticdatasets: Adeepinteractionapproachtollmevaluation. ArXiv
preprint, abs/2309.04369, 2023b. URL https://arxiv.org/abs/2309.04369.
Minzhi Li, Weiyan Shi, Caleb Ziems, and Diyi Yang. Social intelligence data infrastructure: Structuring the
present and navigating the future. ArXiv preprint, abs/2403.14659, 2024a. URL https://arxiv.org/
abs/2403.14659.
Yang Li, Shao Zhang, Jichen Sun, Yali Du, Ying Wen, Xinbing Wang, and Wei Pan. Cooperative open-
ended learning framework for zero-shot coordination. In International Conference on Machine Learning,
pp. 20470–20484. PMLR, 2023c.
Yuanchun Li, Hao Wen, Weijun Wang, Xiangyu Li, Yizhen Yuan, Guohong Liu, Jiacheng Liu, Wenxing Xu,
Xiang Wang, Yi Sun, et al. Personal llm agents: Insights and survey about the capability, efficiency and
security. ArXiv preprint, abs/2401.05459, 2024b. URL https://arxiv.org/abs/2401.05459.
ZongyuanLi,YananNi,RunnanQi,LuminJiang,ChangLu,XiaojieXu,XiangbeiLiu,PengfeiLi,Yunzheng
Guo,ZheMa,etal. Llm-pysc2: Starcraftiilearningenvironmentforlargelanguagemodels. arXivpreprint
arXiv:2411.05348, 2024c.
Austen Liao, Nicholas Tomlin, and Dan Klein. Efficacy of language model self-play in non-zero-sum games.
ArXiv preprint, abs/2406.18872, 2024. URL https://arxiv.org/abs/2406.18872.
Jonathan Light, Min Cai, Sheng Shen, and Ziniu Hu. Avalonbench: Evaluating llms playing the game of
avalon. In NeurIPS 2023 Foundation Models for Decision Making Workshop, 2023a.
JonathanLight, MinCai, ShengShen, andZiniuHu. Fromtexttotactic: Evaluatingllmsplayingthegame
of avalon. ArXiv preprint, abs/2310.05036, 2023b. URL https://arxiv.org/abs/2310.05036.
JonathanLight, MinCai, WeiqinChen, GuanzhiWang, XiusiChen, WeiCheng, YisongYue, andZiniuHu.
Strategist: Learningstrategicskillsbyllmsviabi-leveltreesearch. ArXiv preprint, abs/2408.10635, 2024.
URL https://arxiv.org/abs/2408.10635.
Yang Liu, Weixing Chen, Yongjie Bai, Jingzhou Luo, Xinshuai Song, Kaixuan Jiang, Zhida Li, Ganlong
Zhao, Junyi Lin, Guanbin Li, et al. Aligning cyber space with physical world: A comprehensive survey
on embodied ai. ArXiv preprint, abs/2407.06886, 2024a. URL https://arxiv.org/abs/2407.06886.
ZiyiLiu,AbhishekAnand,PeiZhou,Jen-tseHuang,andJieyuZhao. Interintent: Investigatingsocialintelli-
genceofllmsviaintentionunderstandinginaninteractivegamecontext. ArXiv preprint, abs/2406.12203,
2024b. URL https://arxiv.org/abs/2406.12203.
LinLong, RuiWang, RuixuanXiao, JunboZhao, XiaoDing, GangChen, andHaoboWang. Onllms-driven
synthetic data generation, curation, and evaluation: A survey. ArXiv preprint, abs/2406.15126, 2024.
URL https://arxiv.org/abs/2406.15126.
NunzioLorèandBabakHeydari. Strategicbehavioroflargelanguagemodelsandtheroleofgamestructure
versus contextual framing. Scientific Reports, 14(1):18490, 2024.
26

Published in Transactions on Machine Learning Research (05/2025)
Ji Ma. Can machines think like humans? a behavioral evaluation of llm-agents in dictator games. arXiv
preprint arXiv:2410.21359, 2024.
QunMa,XiaoXue,DeyuZhou,XiangningYu,DonghuaLiu,XuwenZhang,ZihanZhao,YifanShen,Peilin
Ji,JuanjuanLi,etal. Computationalexperimentsmeetlargelanguagemodelbasedagents: Asurveyand
perspective. ArXiv preprint, abs/2402.00262, 2024. URL https://arxiv.org/abs/2402.00262.
WeiyuMa,QiruiMi,XueYan,YuqiaoWu,RunjiLin,HaifengZhang,andJunWang. Largelanguagemodels
play starcraft ii: Benchmarks and a chain of summarization approach. ArXiv preprint, abs/2312.11865,
2023. URL https://arxiv.org/abs/2312.11865.
Bahar Mahmud, Guan Hong, and Bernard Fong. A study of human–ai symbiosis for creative work: Re-
cent developments and future directions in deep learning. ACM Transactions on Multimedia Computing,
Communications and Applications, 20(2):1–21, 2023.
Shaoguang Mao, Yuzhe Cai, Yan Xia, Wenshan Wu, Xun Wang, Fengyi Wang, Tao Ge, and Furu Wei.
Alympics: Language agents meet game theory. ArXiv preprint, abs/2311.03220, 2023. URL https:
//arxiv.org/abs/2311.03220.
Leena Mathur, Paul Pu Liang, and Louis-Philippe Morency. Advancing social intelligence in ai agents:
Technical challenges and open questions. ArXiv preprint, abs/2404.11023, 2024. URL https://arxiv.
org/abs/2404.11023.
Qiaozhu Mei, Yutong Xie, Walter Yuan, and Matthew O Jackson. A turing test of whether ai chatbots are
behaviorally similar to humans. Proceedings of the National Academy of Sciences, 121(9):e2313925121,
2024.
JuanjuanMeng. Aiemergesasthefrontierinbehavioralscience. ProceedingsoftheNationalAcademyofSci-
ences of the United States of America, 121 10:e2401336121, 2024. URL https://api.semanticscholar.
org/CorpusID:268029379.
Matej Moravčík, Martin Schmid, Neil Burch, Viliam Lisy`, Dustin Morrill, Nolan Bard, Trevor Davis, Kevin
Waugh,MichaelJohanson,andMichaelBowling.Deepstack: Expert-levelartificialintelligenceinheads-up
no-limit poker. Science, 356(6337):508–513, 2017.
Rémi Munos, Michal Valko, Daniele Calandriello, Mohammad Gheshlaghi Azar, Mark Rowland, Zhao-
han Daniel Guo, Yunhao Tang, Matthieu Geist, Thomas Mesnard, Andrea Michi, et al. Nash learning
fromhumanfeedback.ArXivpreprint,abs/2312.00886,2023.URLhttps://arxiv.org/abs/2312.00886.
Aran Nayebi. Barriers and pathways to human-ai alignment: A game-theoretic approach. arXiv preprint
arXiv:2502.05934, 2025.
Sean Noh and Ho-Chun Herbert Chang. Llms with personalities in multi-issue negotiation games. ArXiv
preprint, abs/2405.05248, 2024. URL https://arxiv.org/abs/2405.05248.
Maayan Orner, Oleg Maksimov, Akiva Kleinerman, Charles Ortiz, and Sarit Kraus. Explaining decisions
of agents in mixed-motive games. ArXiv preprint, abs/2407.15255, 2024. URL https://arxiv.org/abs/
2407.15255.
Guillermo Owen. Game theory. Emerald Group Publishing, 2013.
Steve Phelps and Yvan I. Russell. The machine psychology of cooperation: Can gpt models operationalise
prompts for altruism, cooperation, competitiveness and selfishness in economic games? ArXiv preprint,
2023. URL https://api.semanticscholar.org/CorpusID:258685424.
Giorgio Piatti, Zhijing Jin, Max Kleiman-Weiner, Bernhard Schölkopf, Mrinmaya Sachan, and Rada Mi-
halcea. Cooperate or collapse: Emergence of sustainability behaviors in a society of llm agents. ArXiv
preprint, abs/2404.16698, 2024. URL https://arxiv.org/abs/2404.16698.
27

Published in Transactions on Machine Learning Research (05/2025)
David Premack and Guy Woodruff. Does the chimpanzee have a theory of mind? Behavioral and brain
sciences, 1(4):515–526, 1978.
Siyuan Qi, Shuo Chen, Yexin Li, Xiangyu Kong, Junqi Wang, Bangcheng Yang, Pring Wong, Yifan Zhong,
XiaoyuanZhang,ZhaoweiZhang,NianLiu,WeiWang,YaodongYang,andSong-ChunZhu. Civrealm: A
learningandreasoningodysseyincivilizationfordecision-makingagents. ArXiv preprint,abs/2401.10568,
2024. URL https://arxiv.org/abs/2401.10568.
HuidaQiu, YanLiu, NiranjanASubrahmanya, andWeichangLi. Grangercausalityfortime-seriesanomaly
detection. In 2012 IEEE 12th international conference on data mining, pp. 1074–1079. IEEE, 2012.
AnatolRapoportandAlbertMChammah. Prisoner’s dilemma: A study in conflict and cooperation,volume
165. University of Michigan press, 1965.
Reza Rawassizadeh, Elaheh Momeni, Chelsea Dobbins, Joobin Gharibshah, and Michael Pazzani. Scalable
dailyhumanbehavioralpatternminingfrommultivariatetemporaldata.IEEETransactionsonKnowledge
and Data Engineering, 28(11):3098–3112, 2016.
Siyue Ren, Zhiyao Cui, Ruiqi Song, Zhen Wang, and Shuyue Hu. Emergence of social norms in generative
agent societies: principles and architecture. In Proceedings of the 33rd International Joint Conference on
Artificial Intelligence (IJCAI), 2024.
Jillian Ross, Yoon Kim, and Andrew W Lo. Llm economicus? mapping the behavioral biases of llms via
utility theory. ArXiv preprint, abs/2408.02784, 2024. URL https://arxiv.org/abs/2408.02784.
Nino Scherrer, Claudia Shi, Amir Feder, and David Blei. Evaluating the moral beliefs encoded in llms.
Advances in Neural Information Processing Systems, 36, 2024.
Stefan F Schouten, Peter Bloem, Ilia Markov, and Piek Vossen. Truth-value judgment in language models:
belief directions are context sensitive. ArXiv preprint, abs/2404.18865, 2024. URL https://arxiv.org/
abs/2404.18865.
Melanie Sclar, Sachin Kumar, Peter West, Alane Suhr, Yejin Choi, and Yulia Tsvetkov. Minding lan-
guage models’(lack of) theory of mind: A plug-and-play multi-character belief tracker. ArXiv preprint,
abs/2306.00924, 2023. URL https://arxiv.org/abs/2306.00924.
Xiao Shao, Weifu Jiang, Fei Zuo, and Mengqing Liu. Swarmbrain: Embodied agent for real-time strategy
gamestarcraftiivialargelanguagemodels. ArXiv preprint, abs/2401.17749, 2024. URLhttps://arxiv.
org/abs/2401.17749.
Eilam Shapira, Omer Madmon, Itamar Reinman, Samuel Joseph Amouyal, Roi Reichart, and Moshe Ten-
nenholtz. Glee: A unified framework and benchmark for language-based economic environments. arXiv
preprint arXiv:2410.05254, 2024.
Zijing Shi, Meng Fang, Shunfeng Zheng, Shilong Deng, Ling Chen, and Yali Du. Cooperation on the fly:
Exploringlanguageagentsforadhocteamworkintheavalongame. ArXivpreprint,abs/2312.17515,2023.
URL https://arxiv.org/abs/2312.17515.
Hisaichi Shibata, Soichiro Miki, and Yuta Nakamura. Playing the werewolf game with artificial intelligence
for language understanding. arXiv preprint arXiv:2302.10646, 2023.
TheodoreRSumers,ShunyuYao,KarthikNarasimhan,andThomasLGriffiths. Cognitivearchitecturesfor
language agents. ArXiv preprint, abs/2309.02427, 2023. URL https://arxiv.org/abs/2309.02427.
Lawrence E Susskind. Scorable games: A better way to teach negotiation. Negot. J., 1:205, 1985.
Reiji Suzuki and Takaya Arita. An evolutionary model of personality traits related to cooperative behavior
using a large language model. Scientific Reports, 14, 2023. URL https://api.semanticscholar.org/
CorpusID:263830498.
28

Published in Transactions on Machine Learning Research (05/2025)
GeminiTeam, RohanAnil, SebastianBorgeaud, YonghuiWu, Jean-BaptisteAlayrac, JiahuiYu, RaduSori-
cut, Johan Schalkwyk, Andrew M Dai, Anja Hauth, et al. Gemini: a family of highly capable multimodal
models. ArXiv preprint, abs/2312.11805, 2023. URL https://arxiv.org/abs/2312.11805.
Jen tse Huang, Eric Li, Man Ho Lam, Tian Liang, Wenxuan Wang, Youliang Yuan, Wenxiang Jiao, Xing
Wang, Zhaopeng Tu, and Michael R. Lyu. How far are we on the decision-making of llms? evaluating
llms’ gaming ability in multi-agent environments. ArXiv preprint, abs/2403.11807, 2024. URL https:
//arxiv.org/abs/2403.11807.
Wiebe Van Der Hoek, Wojciech Jamroga, and Michael Wooldridge. A logic for strategic reasoning. In
Proceedings of the fourth international joint conference on Autonomous agents and multiagent systems,
pp. 157–164, 2005.
Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai Tang,
Xu Chen, Yankai Lin, et al. A survey on large language model based autonomous agents. Frontiers of
Computer Science, 18(6):186345, 2024a.
Shenzhi Wang, Chang Liu, Zilong Zheng, Siyuan Qi, Shuo Chen, Qisen Yang, Andrew Zhao, Chaofei Wang,
Shiji Song, and Gao Huang. Avalon’s game of thoughts: Battle against deception through recursive
contemplation. ArXiv preprint, abs/2310.01320, 2023. URL https://arxiv.org/abs/2310.01320.
XingyaoWang,BoxuanLi,YufanSong,FrankFXu,XiangruTang,MingchenZhuge,JiayiPan,YueqiSong,
Bowen Li, Jaskirat Singh, et al. Opendevin: An open platform for ai software developers as generalist
agents. ArXiv preprint, abs/2407.16741, 2024b. URL https://arxiv.org/abs/2407.16741.
Zhen Wang, Ruiqi Song, Chen Shen, Shiya Yin, Zhao Song, Balaraju Battu, Lei Shi, Danyang Jia, Talal
Rahwan, and Shuyue Hu. Large language models overcome the machine penalty when acting fairly but
not when acting selfishly or altruistically. arXiv preprint arXiv:2410.03724, 2024c.
Donald Arthur Waterman. Generalization learning techniques for automating the learning of heuristics.
Artificial Intelligence, 1(1-2):121–170, 1970.
JasonWei,XuezhiWang,DaleSchuurmans,MaartenBosma,FeiXia,EdChi,QuocVLe,DennyZhou,etal.
Chain-of-thought prompting elicits reasoning in large language models. Advances in neural information
processing systems, 35:24824–24837, 2022.
Dekun Wu, Haochen Shi, Zhiyuan Sun, and Bang Liu. Deciphering digital detectives: Understanding llm
behaviorsandcapabilitiesinmulti-agentmysterygames. InFindingsoftheAssociationforComputational
Linguistics ACL 2024, pp. 8225–8291, 2024a.
Shuang Wu, Liwen Zhu, Tao Yang, Shiwei Xu, Qiang Fu, Yang Wei, and Haobo Fu. Enhance reasoning
for large language models in the game werewolf. ArXiv preprint, abs/2402.02330, 2024b. URL https:
//arxiv.org/abs/2402.02330.
Tian Xia, Zhiwei He, Tong Ren, Yibo Miao, Zhuosheng Zhang, Yang Yang, and Rui Wang. Measuring bar-
gainingabilitiesofllms: Abenchmarkandabuyer-enhancementmethod. ArXivpreprint,abs/2402.15813,
2024. URL https://arxiv.org/abs/2402.15813.
LinXu,ZhiyuanHu,DaquanZhou,HongyuRen,ZhenDong,KurtKeutzer,See-KiongNg,andJiashiFeng.
Magic: Investigation of large language model powered multi-agent in cognition, adaptability, rationality
and collaboration. In ICLR 2024 Workshop on Large Language Model (LLM) Agents, 2023a.
Rongwu Xu, Brian S Lin, Shujian Yang, Tianqi Zhang, Weiyan Shi, Tianwei Zhang, Zhixuan Fang, Wei Xu,
andHanQiu. Theearthisflatbecause...: Investigatingllms’belieftowardsmisinformationviapersuasive
conversation. ArXiv preprint, abs/2312.09085, 2023b. URL https://arxiv.org/abs/2312.09085.
Ruoxi Xu, Yingfei Sun, Mengjie Ren, Shiguang Guo, Ruotong Pan, Hongyu Lin, Le Sun, and Xianpei Han.
Ai for social science and social science of ai: A survey. Information Processing & Management, 61(3):
103665, 2024a.
29

Published in Transactions on Machine Learning Research (05/2025)
Xinrun Xu, Yuxin Wang, Chaoyi Xu, Ziluo Ding, Jiechuan Jiang, Zhiming Ding, and Börje F Karlsson. A
survey on game playing agents and large models: Methods, applications, and challenges. ArXiv preprint,
abs/2403.10249, 2024b. URL https://arxiv.org/abs/2403.10249.
Yuzhuang Xu, Shuo Wang, Peng Li, Fuwen Luo, Xiaolong Wang, Weidong Liu, and Yang Liu. Explor-
ing large language models for communication games: An empirical study on werewolf. ArXiv preprint,
abs/2309.04658, 2023c. URL https://arxiv.org/abs/2309.04658.
Zelai Xu, Chao Yu, Fei Fang, Yu Wang, and Yi Wu. Language agents with reinforcement learning for
strategic play in the werewolf game. ArXiv preprint, abs/2310.18940, 2023d. URL https://arxiv.org/
abs/2310.18940.
An Yang, Baosong Yang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Zhou, Chengpeng Li, Chengyuan Li,
Dayiheng Liu, Fei Huang, et al. Qwen2 technical report. ArXiv preprint, abs/2407.10671, 2024a. URL
https://arxiv.org/abs/2407.10671.
Ruihan Yang, Jiangjie Chen, Yikai Zhang, Siyu Yuan, Aili Chen, Kyle Richardson, Yanghua Xiao, and
Deqing Yang. Selfgoal: Your language agents already know how to achieve high-level goals. ArXiv
preprint, abs/2406.04784, 2024b. URL https://arxiv.org/abs/2406.04784.
Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Tom Griffiths, Yuan Cao, and Karthik Narasimhan.
Treeofthoughts: Deliberateproblemsolvingwithlargelanguagemodels. Advances in Neural Information
Processing Systems, 36, 2024.
YauwaiYim,ChunkitChan,TianyuShi,ZheyeDeng,WeiFan,TianshiZheng,andYangqiuSong.Evaluating
andenhancingllmsagentbasedontheoryofmindinguandan: Amulti-playercooperativegameunderim-
perfect information. ArXiv preprint, abs/2408.02559, 2024. URL https://arxiv.org/abs/2408.02559.
HaolanZhan, YufeiWang, TaoFeng, YunchengHua, SurajSharma, ZhuangLi, LizhenQu, ZhalehSemnani
Azad,IngridZukerman,andGholamrezaHaffari.Let’snegotiate! asurveyofnegotiationdialoguesystems.
ArXiv preprint, abs/2402.01097, 2024. URL https://arxiv.org/abs/2402.01097.
Wenqi Zhang, Ke Tang, Hai Wu, Mengna Wang, Yongliang Shen, Guiyang Hou, Zeqi Tan, Peng Li, Yueting
Zhuang, and Weiming Lu. Agent-pro: Learning to evolve via policy-level reflection and optimization.
arXiv preprint arXiv:2402.17574, 2024a.
YadongZhang, ShaoguangMao, TaoGe, XunWang, AdriandeWynter, YanXia, WenshanWu, TingSong,
Man Lan, and Furu Wei. Llm as a mastermind: A survey of strategic reasoning with large language
models. ArXiv preprint, abs/2404.01230, 2024b. URL https://arxiv.org/abs/2404.01230.
YadongZhang, ShaoguangMao, TaoGe, XunWang, AdriandeWynter, YanXia, WenshanWu, TingSong,
Man Lan, and Furu Wei. Llm as a mastermind: A survey of strategic reasoning with large language
models. ArXiv preprint, abs/2404.01230, 2024c. URL https://arxiv.org/abs/2404.01230.
Yadong Zhang, Shaoguang Mao, Tao Ge, Xun Wang, Yan Xia, Man Lan, and Furu Wei. K-level reasoning
with large language models. ArXiv preprint, abs/2402.01521, 2024d. URL https://arxiv.org/abs/
2402.01521.
Yadong Zhang, Shaoguang Mao, Wenshan Wu, Yan Xia, Tao Ge, Man Lan, and Furu Wei. Enhancing
language model rationality with bi-directional deliberation reasoning. ArXiv preprint, abs/2407.06112,
2024e. URL https://arxiv.org/abs/2407.06112.
Qinlin Zhao, Jindong Wang, Yixuan Zhang, Yiqiao Jin, Kaijie Zhu, Hao Chen, and Xing Xie. Competeai:
Understanding the competition dynamics in large language model-based agents. In Forty-first Interna-
tional Conference on Machine Learning, 2023. URL https://api.semanticscholar.org/CorpusID:
270357283.
Qinglin Zhu, Runcong Zhao, Jinhua Du, Lin Gui, and Yulan He. Player*: Enhancing llm-based multi-agent
communication and interaction in murder mystery games. ArXiv preprint, abs/2404.17662, 2024a. URL
https://arxiv.org/abs/2404.17662.
30

Published in Transactions on Machine Learning Research (05/2025)
WentaoZhu,ZhiningZhang,andYizhouWang. Languagemodelsrepresentbeliefsofselfandothers. ArXiv
preprint, abs/2402.18496, 2024b. URL https://arxiv.org/abs/2402.18496.
Richard Zhuang, Akshat Gupta, Richard Yang, Aniket Rahane, Zhengyu Li, and Gopala Anumanchipalli.
Pokerbench: Training large language models to become professional poker players. arXiv preprint
arXiv:2501.08328, 2025.
31
