Title: Book Proceedings1

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/survey_paper/pdfs/phase1_foundational/03_Assisted_Agent_Based_Simulations_Koutsolampros2017.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T02:56:57+00:00
- page_count: 13
- status: ok
- text_char_count: 66980

Metadata:
- author: unknown
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Book Proceedings1
- Book Proceedings2 (page 1)

Markdown Content:

Proceedings of the 11th Space Syntax Symposium
#164
ASSISTED AGENT-BASED SIMULATIONS:
Fusing Non-Player Character Movement With Space Syntax
PETROS KOUTSOLAMPROS
Space Syntax Laboratory, University College London, London, United Kingdom
petros.koutsolampros.11@ucl.ac.uk
TASOS VAROUDIS
Space Syntax Laboratory, University College London, London, United Kingdom
t.varoudis@ucl.ac.uk
ABSTRACT
Agent-based simulation is one of the core tools of spatial analysis utilised to provide an
understandin(cid:137) o(cid:136) s(cid:146)ace (cid:153)hen co(cid:143)(cid:146)le(cid:154) (cid:146)ara(cid:143)eters co(cid:143)e into (cid:146)la(cid:155), such as ho(cid:153) the visi(cid:132)le s(cid:146)ace
changes while traversing a building, or what happens when there is a destination to be reached.
This type of simulation has a lot in common with techniques used in video games to create
movement trajectories for non-player characters. Although these techniques have been
developed over the years to provide more realistic and more “human-like” behaviour, they
are rarel(cid:155) (cid:153)oven (cid:132)ac(cid:141) into anal(cid:155)tical and si(cid:143)ulation tools(cid:484) As a first ste(cid:146) to re(cid:143)ed(cid:155) that, (cid:153)e
developed a new methodology that fuses non-player character movement from computer
(cid:137)a(cid:143)es (cid:153)ith si(cid:143)ulation techniques traditionall(cid:155) used (cid:136)or a(cid:137)ent(cid:486)(cid:132)ased anal(cid:155)sis in (cid:22)(cid:146)ace (cid:22)(cid:155)nta(cid:154)(cid:484)
(cid:23)his first atte(cid:143)(cid:146)t utilises a di(cid:417)erent t(cid:155)(cid:146)e o(cid:136) underl(cid:155)in(cid:137) re(cid:146)resentation o(cid:136) s(cid:146)ace, (cid:141)no(cid:153)n as a
navigation mesh.
(cid:26)e first e(cid:154)a(cid:143)ine in detail t(cid:153)o traditional techniques utilised in de(cid:146)th(cid:143)a(cid:146)(cid:27) a(cid:137)ent(cid:486)(cid:132)ased anal(cid:155)sis
and hi(cid:137)hli(cid:137)ht their stren(cid:137)ths and li(cid:143)itations(cid:484) (cid:26)e then descri(cid:132)e ho(cid:153) this technique di(cid:417)ers (cid:136)ro(cid:143)
the classic s(cid:146)ace s(cid:155)nta(cid:154) (cid:143)ethods, as (cid:153)ell as ho(cid:153) it can (cid:132)e co(cid:143)(cid:132)ined to create h(cid:155)(cid:132)rid anal(cid:155)tical
(cid:143)odels o(cid:136) (cid:143)ove(cid:143)ent(cid:484) (cid:23)he h(cid:155)(cid:132)rid (cid:143)odel develo(cid:146)ed in this case is that o(cid:136) a classic s(cid:146)ace s(cid:155)nta(cid:154)
a(cid:137)ent assisted (cid:132)(cid:155) the a(cid:136)ore(cid:143)entioned technique(cid:484) (cid:26)e then tested and evaluated the traditional
and ne(cid:153) (cid:143)odels (cid:136)or their ca(cid:146)acit(cid:155) to e(cid:154)(cid:146)lore t(cid:153)o (cid:137)aller(cid:155) s(cid:146)aces(cid:484)
(cid:23)he results e(cid:154)tracted (cid:136)ro(cid:143) the ne(cid:153) h(cid:155)(cid:132)rid si(cid:143)ulation (cid:143)odel de(cid:146)ict a(cid:137)ents (cid:153)ith (cid:143)ore ca(cid:146)acit(cid:155)
to e(cid:154)(cid:146)lore, a si(cid:137)nificant addition to the traditional s(cid:146)ace s(cid:155)nta(cid:154) a(cid:137)ent (cid:132)ased (cid:143)ethods(cid:484)
KEYWORDS
(cid:22)(cid:146)ace s(cid:155)nta(cid:154), a(cid:137)ent(cid:486)(cid:132)ased si(cid:143)ulation, navi(cid:137)ation (cid:143)esh
1. INTRODUCTION
(cid:26)ithin the field o(cid:136) (cid:22)(cid:146)ace s(cid:155)nta(cid:154) a(cid:137)ent(cid:486)(cid:132)ased (cid:143)odels have (cid:132)een e(cid:143)(cid:146)lo(cid:155)ed to (cid:146)rovide a stochastic
alternative to the deter(cid:143)inistic (cid:25)isi(cid:132)ilit(cid:155) (cid:10)ra(cid:146)h Anal(cid:155)sis, to stud(cid:155) ho(cid:153) hu(cid:143)an (cid:143)ove(cid:143)ent can (cid:132)e
a(cid:146)(cid:146)ro(cid:154)i(cid:143)ated, and to act as an alternative evaluation tool to o(cid:132)servations (cid:136)or understandin(cid:137)
the relationship of movement to the various metrics that describe space. An agent-based model
is an e(cid:154)a(cid:143)(cid:146)le o(cid:136) a si(cid:143)ulation in (cid:153)hich autono(cid:143)ous a(cid:137)ents are le(cid:136)t to (cid:153)ander a virtual s(cid:146)ace
having only a small set of simple rules to follow. Through this set of rules and the interactions
ASSISTED AGENT-BASED SIMULATIONS: 164.1
Fusing Non-Player Character Movement With Space Syntax

Proceedings of the 11th Space Syntax Symposium
(cid:132)et(cid:153)een the a(cid:137)ents a co(cid:143)(cid:146)le(cid:154) s(cid:155)ste(cid:143) e(cid:143)er(cid:137)es(cid:484) (cid:5)att(cid:155) (cid:523)(cid:858)(cid:856)(cid:856)(cid:857)(cid:524) s(cid:146)ecificall(cid:155) hi(cid:137)hli(cid:137)hted a(cid:137)ent(cid:486)
based models as alternatives to large aggregative models which are built from the top down.
In parallel, video games have been utilising agent-simulation as a way to allow non-player
characters to move through the virtual game world, and thus provide interactivity to the
narrative of the medium. A common method used to allow for this kind of movement is path-
findin(cid:137) throu(cid:137)h a navi(cid:137)ation (cid:143)esh(cid:484) A navi(cid:137)ation (cid:143)esh is an underl(cid:155)in(cid:137) (cid:523)non(cid:486)visi(cid:132)le to the
(cid:146)la(cid:155)er(cid:524) re(cid:146)resentation o(cid:136) the (cid:494)(cid:153)al(cid:141)a(cid:132)le(cid:495) s(cid:146)ace in the (cid:137)a(cid:143)e (cid:153)orld, and it is co(cid:143)(cid:146)rised o(cid:136) a set o(cid:136)
conve(cid:154) (cid:146)ol(cid:155)(cid:137)ons that are inter(cid:486)connected(cid:484) As (cid:143)entioned (cid:132)(cid:155) (cid:22)noo(cid:141) (cid:523)(cid:858)(cid:856)(cid:856)(cid:856)(cid:524), its (cid:143)ain (cid:146)ur(cid:146)ose is to
allo(cid:153) (cid:136)or a crude a(cid:146)(cid:146)ro(cid:154)i(cid:143)ation o(cid:136) the virtual (cid:153)orld (cid:153)hich can in turn (cid:132)e used to calculate (cid:146)aths
quic(cid:141)l(cid:155)(cid:484) (cid:11)e states that (cid:498)the added (cid:132)onus is that our re(cid:146)lace(cid:143)ent (cid:136)or the (cid:858)(cid:7) (cid:137)rid can have cells
o(cid:136) irre(cid:137)ular sha(cid:146)e and si(cid:156)e, (cid:153)ind u(cid:146) and do(cid:153)n stairs and hills and even overla(cid:146) itsel(cid:136) on thin(cid:137)s
li(cid:141)e (cid:132)rid(cid:137)es and cat(cid:153)al(cid:141)s(cid:499)(cid:484) (cid:26)hile this a(cid:146)(cid:146)roach is es(cid:146)eciall(cid:155) (cid:132)eneficial as a (cid:859)(cid:7) re(cid:146)resentation,
the (cid:143)a(cid:140)orit(cid:155) o(cid:136) the (cid:22)(cid:146)ace (cid:22)(cid:155)nta(cid:154) research (cid:136)ocuses on t(cid:153)o di(cid:143)ensions and thus (cid:153)e onl(cid:155) utilise
(cid:858)(cid:7) instances(cid:484)
(cid:12)n the ne(cid:154)t t(cid:153)o sections (cid:153)e e(cid:154)a(cid:143)ine the develo(cid:146)(cid:143)ent and (cid:137)eneral (cid:132)ac(cid:141)(cid:137)round o(cid:136) the t(cid:153)o
re(cid:146)resentations, as (cid:153)ell as ho(cid:153) the(cid:155) are used toda(cid:155)(cid:484) (cid:23)he ne(cid:154)t section descri(cid:132)es a(cid:137)ent(cid:486)(cid:132)ased
analysis in general and where the direction decision making process happens, while the two after
that e(cid:154)a(cid:143)ine the t(cid:153)o (cid:22)(cid:146)ace (cid:22)(cid:155)nta(cid:154) (cid:494)loo(cid:141)(cid:495) (cid:143)ethods, and the ne(cid:153) su(cid:137)(cid:137)ested (cid:494)loo(cid:141)(cid:495) res(cid:146)ectivel(cid:155)(cid:484)
(cid:22)ection nu(cid:143)(cid:132)er seven descri(cid:132)es the (cid:143)ethod o(cid:136) evaluation (cid:136)or the three techniques as (cid:153)ell as
the results of this evaluation and the last section discusses the results and provides possible
directions for future research.
2. BACKGROUND: AGENT-BASED RESEARCH WITHIN SPACE SYNTAX
(cid:23)he (cid:22)(cid:146)ace (cid:22)(cid:155)nta(cid:154) field had a lon(cid:137) histor(cid:155) (cid:132)e(cid:136)ore a(cid:137)ent anal(cid:155)sis (cid:153)as introduced, (cid:153)ith roots at
(cid:11)illier and (cid:11)anson(cid:495)s (cid:494)(cid:23)he social lo(cid:137)ic o(cid:136) s(cid:146)ace(cid:495) (cid:523)(cid:857)(cid:865)(cid:864)(cid:860)(cid:524) (cid:153)hich considered the ele(cid:143)ents o(cid:136) s(cid:146)ace
(cid:523)roo(cid:143)s, lines o(cid:136) si(cid:137)ht(cid:524) as (cid:146)arts o(cid:136) a (cid:137)ra(cid:146)h, an a(cid:132)straction that allo(cid:153)ed (cid:143)a(cid:146)(cid:146)in(cid:137) on it di(cid:417)erent
conce(cid:146)ts such as social and (cid:146)h(cid:155)sical (cid:132)ehaviour(cid:484) (cid:23)his a(cid:132)straction (cid:153)as co(cid:143)(cid:132)ined (cid:153)ith (cid:10)i(cid:132)son(cid:495)s
theor(cid:155) o(cid:136) a(cid:417)ordances (cid:523)(cid:857)(cid:865)(cid:864)(cid:862)(cid:524) and (cid:5)enedi(cid:141)t(cid:495)s isovists (cid:523)(cid:857)(cid:865)(cid:863)(cid:865)(cid:524) to create (cid:153)hat is (cid:141)no(cid:153)n toda(cid:155) as
(cid:25)isi(cid:132)ilit(cid:155) (cid:10)ra(cid:146)h Anal(cid:155)sis (cid:523)(cid:25)(cid:10)A(cid:524)(cid:484) (cid:25)(cid:10)A is a (cid:136)ra(cid:143)e(cid:153)or(cid:141) that allo(cid:153)s the anal(cid:155)sis s(cid:146)ace (cid:132)(cid:155) dividin(cid:137) it
into cells and connectin(cid:137) these cells in a (cid:137)ra(cid:146)h i(cid:136) the(cid:155) are inter(cid:486)visi(cid:132)le(cid:484) (cid:25)(cid:10)A is deter(cid:143)inistic, in
that the sa(cid:143)e s(cid:146)atial confi(cid:137)uration (cid:153)ill al(cid:153)a(cid:155)s (cid:146)roduce the sa(cid:143)e result(cid:484)
(cid:23)urner and Penn (cid:523)(cid:858)(cid:856)(cid:856)(cid:858)(cid:524) identified the need (cid:136)or a (cid:143)odel o(cid:136) hu(cid:143)an (cid:143)ove(cid:143)ent that does not
follow a grand theory about the underlying space, but which regards “the environment as the
(cid:146)rovider o(cid:136) (cid:146)ossi(cid:132)ilities rather than a (cid:146)lace to (cid:132)e rationalised(cid:499) (cid:523)(cid:23)urner and Penn (cid:858)(cid:856)(cid:856)(cid:858), (cid:146)(cid:484)(cid:860)(cid:863)(cid:859)(cid:524)
and set out to identi(cid:136)(cid:155) (cid:153)hether it is (cid:146)ossi(cid:132)le, and to (cid:153)hat e(cid:154)tend, to use confi(cid:137)uration to e(cid:154)(cid:146)lain
(cid:143)ove(cid:143)ent (cid:132)(cid:155) usin(cid:137) one such (cid:143)odel(cid:484) (cid:23)he authors su(cid:137)(cid:137)ested that other e(cid:154)a(cid:143)(cid:146)les o(cid:136) a(cid:137)ent(cid:486)
(cid:132)ased (cid:143)odels (cid:153)hich de(cid:146)ended (cid:146)urel(cid:155) on the (cid:146)h(cid:155)sical dis(cid:146)lace(cid:143)ent o(cid:136) hu(cid:143)ans (cid:523)(cid:11)el(cid:132)in(cid:137) and
(cid:16)olnar (cid:857)(cid:865)(cid:865)(cid:864)(cid:524) or those that treated the (cid:146)ro(cid:132)le(cid:143) as one o(cid:136) least(cid:486)cost (cid:146)aths (cid:523)(cid:11)oo(cid:137)endoorn et al(cid:484)
(cid:858)(cid:856)(cid:856)(cid:858)(cid:524) created a(cid:137)ents that lac(cid:141)ed a (cid:132)asic driver (cid:136)or natural (cid:143)ove(cid:143)ent, the a(cid:132)ilit(cid:155) to see(cid:484)
(cid:23)urner and Penn considered this an o(cid:143)ission and created an e(cid:154)a(cid:143)(cid:146)le o(cid:136) a(cid:137)ent(cid:486)(cid:132)ased anal(cid:155)sis
that incor(cid:146)orated this a(cid:132)ilit(cid:155)(cid:484) (cid:23)he(cid:155) initiall(cid:155) (cid:136)ollo(cid:153)ed a s(cid:146)ecific idea, that (cid:153)hen en(cid:137)a(cid:137)in(cid:137) in
natural movement, a human will move towards further available space as determined by his
or her current visual field(cid:484) (cid:23)he researchers thus develo(cid:146)ed a (cid:143)odel (cid:153)ith an a(cid:137)ent that had a
s(cid:146)ecific visual field (cid:153)hich in its turn de(cid:146)ends on an E(cid:25)A (cid:523)E(cid:154)oso(cid:143)atic (cid:25)isual Architecture(cid:524), in this
case a (cid:25)isi(cid:132)ilit(cid:155) (cid:10)ra(cid:146)h as those su(cid:137)(cid:137)ested (cid:132)(cid:155) (cid:23)urner et al(cid:484) (cid:523)(cid:858)(cid:856)(cid:856)(cid:857)(cid:524)(cid:484) (cid:23)he underl(cid:155)in(cid:137) (cid:137)ra(cid:146)h had a
(cid:856)(cid:484)(cid:863)(cid:861) (cid:154) (cid:856)(cid:484)(cid:863)(cid:861) (cid:143) resolution (cid:137)rid to a(cid:146)(cid:146)ro(cid:154)i(cid:143)ate the avera(cid:137)e hu(cid:143)an ste(cid:146) len(cid:137)th(cid:483) (cid:856)(cid:484)(cid:863)(cid:863)(cid:143) (cid:523)(cid:22)utherland
et al(cid:484) (cid:857)(cid:865)(cid:865)(cid:860)(cid:524)(cid:484) (cid:23)he E(cid:25)A allo(cid:153)ed the a(cid:137)ents to (cid:146)ic(cid:141) a location out o(cid:136) the ones in their visual field,
take a step towards that location, change direction and repeat. The implementation favoured
the availability of space, thus the agents were more likely to turn and walk towards the areas
(cid:153)ithin their visual field that had (cid:143)ore s(cid:146)ace(cid:484) (cid:23)he al(cid:137)orith(cid:143) that (cid:143)ade this selection (cid:153)ill (cid:132)e
referred in this paper as the ‘standard look”.
ASSISTED AGENT-BASED SIMULATIONS: 164.2
Fusing Non-Player Character Movement With Space Syntax

Proceedings of the 11th Space Syntax Symposium
The original implementation introduced some limitations to account for the corporeal nature of
human beings, i.e. it did not allow two agents to be on the same cell of the graph, or walk or see
through walls. These limitations introduced possible gridlocks where the agent had no available
s(cid:146)ace in the visual field(cid:484) (cid:12)n this case the visual field o(cid:136) the a(cid:137)ent (cid:153)as e(cid:154)(cid:146)anded to (cid:859)(cid:862)(cid:856)(cid:955) and a ne(cid:153)
(cid:146)i(cid:154)el (cid:153)as chosen throu(cid:137)h the (cid:153)hole isovist(cid:484) (cid:23)urner and Penn (cid:146)roceeded to test this ne(cid:153) (cid:143)ethod
a(cid:137)ainst o(cid:132)served (cid:143)ove(cid:143)ent ca(cid:146)tured earlier (cid:523)(cid:23)urner and Penn (cid:857)(cid:865)(cid:865)(cid:865)(cid:524) (cid:153)ith the ai(cid:143) o(cid:136) findin(cid:137)
the co(cid:143)(cid:132)ination (cid:132)et(cid:153)een nu(cid:143)(cid:132)er o(cid:136) ste(cid:146)s and field o(cid:136) vie(cid:153) that had the (cid:132)est correlation (cid:153)ith
the observed data. The combination that best correlated with human movement was found to
(cid:132)e (cid:859) ste(cid:146)s (cid:132)e(cid:136)ore a chan(cid:137)e o(cid:136) direction and a field o(cid:136) vie(cid:153) o(cid:136) (cid:857)(cid:863)(cid:856) de(cid:137)rees(cid:484) (cid:23)urner and Penn also
tested an implementation of the algorithm that chose directions at random but found that it
did not correlate well with the observed data.
(cid:12)n a later stud(cid:155) (cid:523)(cid:23)urner and Penn (cid:858)(cid:856)(cid:856)(cid:863)(cid:524) the authors su(cid:137)(cid:137)ested that an a(cid:137)ent (cid:136)ollo(cid:153)in(cid:137) a natural
(cid:143)ove(cid:143)ent sche(cid:143)a (cid:143)a(cid:155) o(cid:146)t to (cid:136)ollo(cid:153) s(cid:146)ecific (cid:146)aths that o(cid:146)en ne(cid:153) (cid:146)ossi(cid:132)ilities (cid:136)or e(cid:154)(cid:146)loration (cid:484)
(cid:12)n order to encode this t(cid:155)(cid:146)e o(cid:136) a(cid:417)ordance into their (cid:143)odel, the researchers e(cid:154)tended the a(cid:137)ents(cid:495)
availa(cid:132)le in(cid:146)ut to include line(cid:486)o(cid:136)(cid:486)si(cid:137)ht (cid:523)(cid:15)o(cid:22)(cid:524) in(cid:136)or(cid:143)ation(cid:484) (cid:23)he a(cid:137)ents could thus identi(cid:136)(cid:155), (cid:153)ithin
their immediate environment, in what direction they could see further and choose to turn and
(cid:153)al(cid:141) in that direction(cid:484) (cid:23)his al(cid:137)orith(cid:143) (cid:153)ill (cid:132)e re(cid:136)erred in the rest o(cid:136) this (cid:146)a(cid:146)er as (cid:494)(cid:15)o(cid:22) loo(cid:141)(cid:495)(cid:484)
(cid:5)oth (cid:143)ethods (cid:153)ere tested (cid:136)or correlation a(cid:137)ainst data collected throu(cid:137)h o(cid:132)servation in the
(cid:23)ate (cid:5)ritain (cid:10)aller(cid:155) in (cid:15)ondon(cid:484) (cid:5)oth the (cid:494)standard loo(cid:141)(cid:495) and the (cid:494)(cid:15)o(cid:22) loo(cid:141)(cid:495) (cid:153)ere (cid:136)ound to
correlate (cid:153)ell (cid:153)ith the o(cid:132)served data (cid:153)ith coe(cid:421)cients (cid:523)(cid:21)(cid:858)(cid:524) o(cid:136) (cid:856)(cid:484)(cid:863)(cid:865) and (cid:856)(cid:484)(cid:863)(cid:864) res(cid:146)ectivel(cid:155) (cid:136)or
(cid:859)(cid:486)ste(cid:146) (cid:143)ove(cid:143)ent(cid:484) (cid:23)urner and Penn also calculated t(cid:153)o e(cid:154)tra (cid:143)easures, the (cid:494)total covera(cid:137)e
o(cid:136) roo(cid:143)s(cid:495) (cid:153)hich (cid:153)ere visited (cid:132)(cid:155) at least one a(cid:137)ent and the (cid:494)(cid:146)er(cid:486)a(cid:137)ent cu(cid:143)ulative isovist(cid:495), the
mean fraction of building area that could have been viewed by an agent during its visit, had
it had (cid:859)(cid:862)(cid:856) de(cid:137)ree vision(cid:484) (cid:23)he(cid:155) su(cid:137)(cid:137)ested that the cu(cid:143)ulative isovist (cid:137)ave an idea a(cid:132)out ho(cid:153)
o(cid:146)ti(cid:143)ised an a(cid:137)ent is in ter(cid:143)s o(cid:136) e(cid:154)(cid:146)lorative a(cid:132)ilit(cid:155)(cid:484)
(cid:12)n a stud(cid:155) (cid:132)(cid:155) Penn and (cid:23)urner (cid:523)(cid:858)(cid:856)(cid:856)(cid:857)(cid:524) a si(cid:143)ilar a(cid:137)ent (cid:143)odel (cid:153)as tested, onl(cid:155) this ti(cid:143)e the a(cid:137)ents
had access to the (cid:494)clusterin(cid:137) coe(cid:421)cient(cid:495) (cid:143)etric o(cid:136) the underl(cid:155)in(cid:137) visi(cid:132)ilit(cid:155) (cid:137)ra(cid:146)h(cid:484) (cid:23)his (cid:146)rovided
them with a way to distinguish junctions in the space and move towards them. The new model
(cid:153)as tested, alon(cid:137) (cid:153)ith the (cid:494)standard loo(cid:141)(cid:495) one, a(cid:137)ainst o(cid:132)served trails in a de(cid:146)art(cid:143)ent store(cid:484)
(cid:23)he (cid:494)standard loo(cid:141)(cid:495) (cid:143)odel out(cid:146)er(cid:136)or(cid:143)ed the ne(cid:153) (cid:143)odel (cid:143)ost li(cid:141)el(cid:155) due to the (cid:136)act that the
ne(cid:154)t rando(cid:143) ste(cid:146) is chosen (cid:136)ro(cid:143) the field o(cid:136) vie(cid:153) and is thus (cid:143)ore li(cid:141)el(cid:155) to sta(cid:155) alon(cid:137) lon(cid:137) lines
of sight.
(cid:16)ost o(cid:136) these (cid:143)odels have (cid:132)een tested on e(cid:154)hi(cid:132)ition or retail s(cid:146)aces (cid:136)or (cid:153)hich the (cid:153)ords o(cid:136)
(cid:10)i(cid:132)son (cid:146)ro(cid:146)erl(cid:155) descri(cid:132)e hu(cid:143)an (cid:132)ehaviour(cid:483) (cid:498)(cid:26)hen no constraints are (cid:146)ut on the visual s(cid:155)ste(cid:143),
we look around, walk up to something interesting and move around it so as to see it from all
sides, and (cid:137)o (cid:136)ro(cid:143) one vista to another(cid:484) (cid:23)hat is natural vision(cid:484)(cid:484)(cid:484)(cid:499) (cid:523)(cid:10)i(cid:132)son (cid:857)(cid:865)(cid:864)(cid:862), (cid:146)(cid:484)(cid:857)(cid:524)(cid:484) (cid:22)o(cid:143)e studies
(cid:146)rovided the a(cid:137)ents (cid:153)ith the (cid:141)no(cid:153)led(cid:137)e o(cid:136) ori(cid:137)ins and destinations to si(cid:143)ulate this e(cid:417)ect(cid:484)
(cid:9)er(cid:137)uson et al(cid:484) (cid:523)(cid:858)(cid:856)(cid:857)(cid:858)(cid:524) re(cid:146)orted t(cid:153)o li(cid:143)itations (cid:153)ith (cid:146)revious (cid:143)odels(cid:484) (cid:23)he ori(cid:137)inal E(cid:25)A (cid:143)odels
used the a(cid:143)ount o(cid:136) visi(cid:132)le s(cid:146)ace in (cid:136)ront o(cid:136) the a(cid:137)ent to deter(cid:143)ine the ne(cid:154)t destination and
would change direction every three steps. The agents in this model would therefore favour big
open spaces simply because an agent standing at the edge of such a space would have the
biggest amount of visible space toward the centre. A change to the model suggested by Turner
(cid:523)(cid:858)(cid:856)(cid:856)(cid:860)(cid:524) (cid:146)artiall(cid:155) solved that (cid:146)ro(cid:132)le(cid:143) (cid:132)(cid:155) requirin(cid:137) the a(cid:137)ents to reach a visi(cid:132)le destination (cid:132)e(cid:136)ore
changing direction, but since open spaces are a large percentage of all spaces in a building most
destinations (cid:153)ould still (cid:132)e in the(cid:143)(cid:484) (cid:23)here(cid:136)ore (cid:9)er(cid:137)uson et al(cid:484) (cid:523)(cid:858)(cid:856)(cid:857)(cid:858)(cid:524) su(cid:137)(cid:137)ested to co(cid:143)(cid:146)le(cid:143)ent
the E(cid:25)A (cid:143)odel (cid:153)ith a second loo(cid:141)u(cid:146) ta(cid:132)le o(cid:136) ori(cid:137)ins and destinations that re(cid:426)ect each activities
at those locations. An agent can then use this information to choose a direction based on how
closer it takes him or her to the assigned destination, making this destination a form of attractor.
Implementation of many of the above mentioned methods can currently be found in an open
source so(cid:136)t(cid:153)are tool called de(cid:146)th(cid:143)a(cid:146)(cid:27) (cid:523)(cid:25)aroudis (cid:858)(cid:856)(cid:857)(cid:858)(cid:524)(cid:484) (cid:23)his tool is currentl(cid:155) used (cid:132)(cid:155) the (cid:22)(cid:146)ace
(cid:22)(cid:155)nta(cid:154) co(cid:143)(cid:143)unit(cid:155) to carr(cid:155) out a(cid:137)ent anal(cid:155)sis and enca(cid:146)sulates (cid:143)an(cid:155) o(cid:136) the ideas (cid:136)or this and
other t(cid:155)(cid:146)es o(cid:136) anal(cid:155)sis(cid:484) (cid:23)he ori(cid:137)inal i(cid:143)(cid:146)le(cid:143)entation (cid:153)as develo(cid:146)ed (cid:153)ithin UC(cid:15) (cid:132)(cid:155) (cid:23)urner (cid:523)(cid:858)(cid:856)(cid:856)(cid:863)(cid:524)
and (cid:153)as eventuall(cid:155) re(cid:486)en(cid:137)ineered and o(cid:146)en sourced (cid:132)(cid:155) (cid:25)aroudis (cid:523)(cid:858)(cid:856)(cid:857)(cid:858)(cid:524)(cid:484)
ASSISTED AGENT-BASED SIMULATIONS: 164.3
Fusing Non-Player Character Movement With Space Syntax

Proceedings of the 11th Space Syntax Symposium
3. BACKGROUND: VIDEO GAME PATHFINDING AND NAVIGATION MESHES
Like the above-highlighted research, video game development required ways to interact
(cid:153)ith virtual s(cid:146)ace(cid:484) Es(cid:146)eciall(cid:155) (cid:153)ith the advent o(cid:136) three(cid:486)di(cid:143)ensional co(cid:143)(cid:146)uter (cid:137)ra(cid:146)hics, s(cid:146)ace
became the primary environment a player navigates, and in order to build believable stories
non-player characters were eventually introduced. For the stories to be immersive, video games
also required these characters to move naturally so that they can lead players through a space,
or act against them. In contrast to research though, video games required this to happen in real
ti(cid:143)e and could not de(cid:146)end on (cid:137)rid(cid:486)(cid:132)ased solutions li(cid:141)e the ones develo(cid:146)ed in the field o(cid:136) (cid:22)(cid:146)ace
(cid:22)(cid:155)nta(cid:154)(cid:484) (cid:23)here(cid:136)ore, other solutions (cid:153)ere develo(cid:146)ed that (cid:153)ere (cid:143)ore li(cid:137)ht(cid:153)ei(cid:137)ht and (cid:146)rovided
(cid:137)ood a(cid:146)(cid:146)ro(cid:154)i(cid:143)ations o(cid:136) natural (cid:143)ove(cid:143)ent(cid:484)
(cid:18)ne o(cid:136) these solutions (cid:153)as a navi(cid:137)ation (cid:143)esh (cid:523)(cid:9)i(cid:137)ure (cid:857), le(cid:136)t(cid:524)(cid:484) (cid:9)irst (cid:143)entioned (cid:132)(cid:155) (cid:22)noo(cid:141) (cid:523)(cid:858)(cid:856)(cid:856)(cid:856)(cid:524)
a navi(cid:137)ation (cid:143)esh is a set o(cid:136) conve(cid:154) (cid:146)ol(cid:155)(cid:137)ons that si(cid:137)nifies the s(cid:146)ace an a(cid:137)ent (cid:143)i(cid:137)ht (cid:153)al(cid:141) on(cid:484)
(cid:22)noo(cid:141) s(cid:146)ecificall(cid:155) su(cid:137)(cid:137)ested this as a (cid:153)a(cid:155) to (cid:146)rovide a crude re(cid:146)resentation o(cid:136) a (cid:494)(cid:153)al(cid:141)a(cid:132)le(cid:495)
area, which is not as detailed as the virtual world and can be used to determine where an agent
can walk.
(cid:9)i(cid:137)ure (cid:857) (cid:486) (cid:7)e(cid:146)th on a navi(cid:137)ation (cid:143)esh (cid:523)le(cid:136)t(cid:524) and (cid:25)isual (cid:16)ean (cid:7)e(cid:146)th on a (cid:137)rid (cid:523)ri(cid:137)ht(cid:524)(cid:484) (cid:9)ro(cid:143) dee(cid:146)er (cid:523)se(cid:137)re(cid:137)ated(cid:524) areas
sho(cid:153)n in red, to shallo(cid:153)er (cid:523)inte(cid:137)rated(cid:524) sho(cid:153)n in (cid:132)lue
(cid:23)his (cid:143)esh o(cid:136) (cid:146)ol(cid:155)(cid:137)ons can also (cid:132)e thou(cid:137)ht o(cid:136) as a (cid:137)ra(cid:146)h(cid:484) Each (cid:146)ol(cid:155)(cid:137)on is a node and i(cid:136) t(cid:153)o
are adjacent, they are connected through an edge. This allows for creation of metrics similar
to (cid:25)(cid:10)A, such as the (cid:143)ean de(cid:146)th (cid:136)ro(cid:143) an(cid:155) (cid:146)ol(cid:155)(cid:137)on to all others, (cid:153)hich can (cid:132)e seen in (cid:9)i(cid:137)ure
(cid:857) (cid:523)le(cid:136)t(cid:524) in co(cid:143)(cid:146)arison to the (cid:25)(cid:10)A (cid:25)isual (cid:143)ean de(cid:146)th (cid:523)ri(cid:137)ht(cid:524)(cid:484) A navi(cid:137)ation (cid:143)esh also acts as an
E(cid:25)A (cid:136)or non(cid:486)(cid:146)la(cid:155)er characters to utilise, traditionall(cid:155) a (cid:146)ath(cid:486)findin(cid:137) (cid:143)ethod(cid:484) (cid:23)he underl(cid:155)in(cid:137)
traversal al(cid:137)orith(cid:143), t(cid:155)(cid:146)icall(cid:155) A(cid:535) (cid:523)(cid:11)art et al(cid:484) (cid:857)(cid:865)(cid:862)(cid:864)(cid:524), is used to identi(cid:136)(cid:155) a series o(cid:136) consecutive
(cid:146)ol(cid:155)(cid:137)ons (cid:523)nodes(cid:524) to (cid:137)o throu(cid:137)h in order (cid:136)or the a(cid:137)ent to reach another area in the (cid:143)a(cid:146)(cid:484)
Another algorithm then provides an actual line-path through these polygons, such as a ‘Funnel
al(cid:137)orith(cid:143)(cid:495)(cid:484) Cui and (cid:22)hi (cid:523)(cid:858)(cid:856)(cid:857)(cid:858)(cid:524) (cid:146)rovide an e(cid:154)a(cid:143)(cid:146)le that descri(cid:132)es the (cid:153)hole (cid:146)rocess(cid:484) (cid:12)n their
simplest implementations most of these algorithms create paths that join the centres of
polygons, or the midpoints of the edges.
(cid:23)he lac(cid:141) o(cid:136) re(cid:137)ularit(cid:155) o(cid:136) the (cid:146)ol(cid:155)(cid:137)ons in a navi(cid:137)ation (cid:143)esh (cid:146)rovides s(cid:146)ecific stren(cid:137)ths and
(cid:153)ea(cid:141)nesses(cid:484) (cid:12)t allo(cid:153)s us to descri(cid:132)e the s(cid:146)ace in (cid:143)ore detail, (cid:136)or e(cid:154)a(cid:143)(cid:146)le it is (cid:143)uch easier
to determine where an opening is, given that its vertices are used to generate the mesh. The
(cid:146)reviousl(cid:155) (cid:143)entioned (cid:137)rid re(cid:146)resentation su(cid:417)ers (cid:136)ro(cid:143) t(cid:153)o related (cid:146)ro(cid:132)le(cid:143)s(cid:484) (cid:12)(cid:136) a s(cid:143)all cell si(cid:156)e
is chosen that provides a lot of detail, analysing that grid will require a lot of computational
(cid:146)o(cid:153)er due to the sheer nu(cid:143)(cid:132)er o(cid:136) cells(cid:484) (cid:12)(cid:136) that is not availa(cid:132)le, then a lar(cid:137)er cell si(cid:156)e can (cid:132)e
selected which will require less computational power but will also provide less detail, and thus
more potential for error. On the other hand, the perfect regularity of the grid allows for much
cleaner analysis, since all the elements are the same, while analysis of a navigation mesh will
need to control (cid:136)or their si(cid:156)e and sha(cid:146)e(cid:484)
ASSISTED AGENT-BASED SIMULATIONS: 164.4
Fusing Non-Player Character Movement With Space Syntax

Proceedings of the 11th Space Syntax Symposium
4. AGENT-BASED ANALYSIS: OVERVIEW
A(cid:137)ent(cid:486)(cid:132)ased anal(cid:155)sis in the (cid:22)(cid:146)ace (cid:22)(cid:155)nta(cid:154) field is currentl(cid:155) done usin(cid:137) the so(cid:136)t(cid:153)are tool
de(cid:146)th(cid:143)a(cid:146)(cid:27) (cid:523)(cid:25)aroudis (cid:858)(cid:856)(cid:857)(cid:858)(cid:524), althou(cid:137)h (cid:136)or this stud(cid:155) (cid:153)e du(cid:146)licated the al(cid:137)orith(cid:143)s in a di(cid:417)erent
a(cid:146)(cid:146)lication that allo(cid:153)s (cid:136)or (cid:143)ore (cid:426)e(cid:154)i(cid:132)ilit(cid:155) in the dis(cid:146)la(cid:155) o(cid:136) the (cid:143)etrics(cid:484) (cid:23)he si(cid:143)ulation is t(cid:155)(cid:146)icall(cid:155)
run (cid:153)ith a lar(cid:137)e nu(cid:143)(cid:132)er o(cid:136) (cid:494)a(cid:137)ents(cid:495) that (cid:146)er(cid:136)or(cid:143) a s(cid:146)ecific (cid:146)rocess(cid:484) Each a(cid:137)ent is (cid:137)iven a certain
field o(cid:136) visi(cid:132)ilit(cid:155) and is le(cid:136)t to roa(cid:143) a s(cid:146)ace (cid:136)or a s(cid:146)ecific a(cid:143)ount o(cid:136) ti(cid:143)e(cid:484) (cid:21)oa(cid:143)in(cid:137) involves the
a(cid:137)ent decidin(cid:137) a direction, (cid:494)(cid:153)al(cid:141)in(cid:137)(cid:495) in that direction (cid:132)(cid:155) ta(cid:141)in(cid:137) a (cid:146)redefined nu(cid:143)(cid:132)er o(cid:136) ste(cid:146)s
and then repeating the process.
(cid:21)es(cid:146)onsi(cid:132)le (cid:136)or choosin(cid:137) a direction is a (cid:494)loo(cid:141)(cid:495) al(cid:137)orith(cid:143)(cid:484) (cid:23)his al(cid:137)orith(cid:143) ta(cid:141)es the a(cid:137)ent(cid:495)s
(cid:146)osition, orientation and environ(cid:143)ent (cid:523)E(cid:25)A(cid:524) into account and decides (cid:153)hat the ne(cid:153) direction
should (cid:132)e(cid:484) (cid:23)he a(cid:137)ent(cid:495)s visi(cid:132)ilit(cid:155) s(cid:155)ste(cid:143) uses a set o(cid:136) (cid:859)(cid:858) (cid:494)(cid:132)ins(cid:495), a radial assort(cid:143)ent o(cid:136) the (cid:146)i(cid:154)els
around a s(cid:146)ecific cell accordin(cid:137) to the an(cid:137)le the(cid:155) are (cid:136)ound, as seen in (cid:9)i(cid:137)ure (cid:858)(cid:484) (cid:23)he loo(cid:141)
al(cid:137)orith(cid:143) selects a (cid:132)in and a rando(cid:143) direction (cid:153)ithin that (cid:132)in to (cid:494)ste(cid:146)(cid:495) to(cid:153)ards(cid:484) (cid:23)he various
loo(cid:141) al(cid:137)orith(cid:143)s hel(cid:146) choose the (cid:132)in (cid:132)(cid:155) (cid:153)ei(cid:137)htin(cid:137) each one o(cid:136) the(cid:143) accordin(cid:137) to di(cid:417)erent
parameters. This study is interested in the direction decision-making process and thus all other
parameters are kept the same throughout all tests.
(cid:9)i(cid:137)ure (cid:858) (cid:486) Cells around a central cell (cid:523)(cid:132)lac(cid:141)(cid:524) (cid:137)rou(cid:146)ed in (cid:132)ins(cid:484) Ad(cid:140)acent (cid:132)ins in di(cid:417)erent shades o(cid:136) (cid:137)re(cid:155)(cid:484) Counter(cid:486)
cloc(cid:141)(cid:153)ise in to(cid:146)(cid:486)ri(cid:137)ht quadrant, (cid:132)ins(cid:483) (cid:859)(cid:858) (cid:523)hori(cid:156)ontal le(cid:136)t(cid:524), (cid:857), (cid:858), (cid:859), (cid:860) (cid:523)to(cid:146)(cid:486)ri(cid:137)ht dia(cid:137)onal(cid:524), (cid:861), (cid:862), (cid:863), (cid:864) (cid:523)vertical to(cid:146)(cid:524)(cid:484)
5. REVIEW OF EXISTING ‘LOOK’ METHODS
(cid:23)his section (cid:153)ill (cid:136)ocus on the t(cid:153)o (cid:494)loo(cid:141)(cid:495) (cid:143)ethods alread(cid:155) (cid:143)entioned in the literature (cid:494)standard(cid:495)
and (cid:494)(cid:15)o(cid:22)(cid:495)(cid:484) As (cid:153)e descri(cid:132)ed a(cid:132)ove, each (cid:143)ethod utilises the underl(cid:155)in(cid:137) E(cid:25)A to (cid:143)a(cid:141)e a decision
about which bins to favour more out of the 32 available.
5.1 STANDARD LOOK
(cid:12)n the (cid:494)standard loo(cid:141)(cid:495) (cid:523)(cid:23)urner and Penn (cid:858)(cid:856)(cid:856)(cid:858)(cid:524) al(cid:137)orith(cid:143) (cid:523)(cid:9)i(cid:137)ure (cid:859)(cid:524) (cid:132)e(cid:136)ore ever(cid:155) ste(cid:146) a (cid:146)ool
of choices is created that contains as many bin choices, as there are cells within that bin. A
selection is made at random from this pool that indicates which direction to follow. The bins
that contain many cells are thus more likely to be selected given that they were placed in the
(cid:146)ool (cid:143)ore ti(cid:143)es(cid:484) (cid:23)his has the e(cid:417)ect o(cid:136) drivin(cid:137) the a(cid:137)ents to(cid:153)ards the lar(cid:137)est s(cid:146)aces (cid:153)ithin
their visi(cid:132)ilit(cid:155) field(cid:484)
ASSISTED AGENT-BASED SIMULATIONS: 164.5
Fusing Non-Player Character Movement With Space Syntax

Proceedings of the 11th Space Syntax Symposium
(cid:9)i(cid:137)ure (cid:859) (cid:486) (cid:23)he (cid:146)ath (cid:523)in red(cid:524) o(cid:136) a sin(cid:137)le a(cid:137)ent utilisin(cid:137) (cid:494)standard loo(cid:141)(cid:495) (cid:132)in (cid:153)ei(cid:137)htin(cid:137) in a roo(cid:143) (cid:153)ith t(cid:153)o doors(cid:484) (cid:7)ecision
(cid:146)oints noted as radial sets o(cid:136) (cid:132)lue lines re(cid:146)resentin(cid:137) each (cid:132)in and each line(cid:495)s len(cid:137)th the (cid:153)ei(cid:137)ht (cid:137)iven (cid:132)(cid:155) the al(cid:137)orith(cid:143)
to that s(cid:146)ecific (cid:132)in
(cid:23)he e(cid:417)ect o(cid:136) this loo(cid:141) technique can (cid:132)e seen at (cid:9)i(cid:137)ure (cid:860)(cid:484) As e(cid:154)(cid:146)ected, cells that are close to
the (cid:153)alls (cid:146)oint to(cid:153)ards the centre o(cid:136) the roo(cid:143), (cid:153)hile ones closer to the centre have an e(cid:417)ect
that s(cid:146)reads in all directions(cid:484) (cid:23)he e(cid:154)istence o(cid:136) an o(cid:146)enin(cid:137) in this case that leads to (cid:143)ore s(cid:146)ace
(cid:132)e(cid:155)ond eventuall(cid:155) (cid:146)ulls the relevant (cid:132)ins in that direction(cid:484) (cid:12)n (cid:9)i(cid:137)ure (cid:860) (cid:523)ri(cid:137)ht(cid:524) (cid:153)e can see that this
al(cid:137)orith(cid:143) su(cid:417)ers (cid:136)ro(cid:143) a lo(cid:153) resolution in the underl(cid:155)in(cid:137) (cid:137)rid(cid:484) (cid:7)irections that are equidistant to
the (cid:153)alls can have ver(cid:155) di(cid:417)erent (cid:143)ulti(cid:146)liers due to the underl(cid:155)in(cid:137) re(cid:146)resentation(cid:484)
(cid:9)i(cid:137)ure (cid:860) (cid:486) (cid:494)(cid:22)tandard loo(cid:141)(cid:495) at all (cid:146)ositions (cid:523)le(cid:136)t(cid:524) and visualisation o(cid:136) (cid:132)ins (cid:136)or
a s(cid:146)ecific (cid:146)oint (cid:523)ri(cid:137)ht(cid:524)
ASSISTED AGENT-BASED SIMULATIONS: 164.6
Fusing Non-Player Character Movement With Space Syntax

Proceedings of the 11th Space Syntax Symposium
5.2 LINE OF SIGHT LOOK
(cid:23)he (cid:15)(cid:18)(cid:22) (cid:523)(cid:23)urner and Penn (cid:858)(cid:856)(cid:856)(cid:863)(cid:524) al(cid:137)orith(cid:143) on the other hand (cid:153)ei(cid:137)hs the (cid:132)ins accordin(cid:137) to
the (cid:143)a(cid:154)i(cid:143)u(cid:143) distance visi(cid:132)le (cid:136)ro(cid:143) (cid:153)ithin the (cid:132)in(cid:484) (cid:23)his distance is calculated (cid:132)(cid:155) ta(cid:141)in(cid:137) the
distance of the cell the agent is on to the cell that is furthest away from it within each bin. The
(cid:132)in selection (cid:146)rocess is the sa(cid:143)e as the one (cid:136)or the (cid:494)standard loo(cid:141)(cid:495) (cid:132)ut in this case the al(cid:137)orith(cid:143)
makes the bins that have cells furthest away more likely to be selected.
(cid:23)he overall e(cid:417)ect can (cid:132)e seen in (cid:9)i(cid:137)ure (cid:861)(cid:484) (cid:18)nce a(cid:137)ain, the cells that are closer to the (cid:153)all tend to
have bins that point toward the centre, while cells that approach the centre tend to have more
distri(cid:132)uted (cid:132)in (cid:153)ei(cid:137)htin(cid:137)(cid:484) (cid:12)n contrast to the (cid:494)standard loo(cid:141)(cid:495) al(cid:137)orith(cid:143) the (cid:494)(cid:15)o(cid:22) loo(cid:141)(cid:495) al(cid:137)orith(cid:143)
does not su(cid:417)er (cid:136)ro(cid:143) lo(cid:153) resolution as (cid:143)uch, althou(cid:137)h it can still s(cid:141)e(cid:153) the results dra(cid:143)aticall(cid:155)
as soon as ne(cid:153) (cid:146)i(cid:154)els are visi(cid:132)le(cid:484)
(cid:9)i(cid:137)ure (cid:861) (cid:486) (cid:15)ine o(cid:136) (cid:22)i(cid:137)ht (cid:523)(cid:15)o(cid:22)(cid:524) loo(cid:141) at all (cid:146)ositions (cid:523)le(cid:136)t(cid:524) and visualisation o(cid:136)
(cid:132)ins and distances (cid:136)ro(cid:143) a s(cid:146)ecific (cid:146)oint (cid:523)ri(cid:137)ht(cid:524)
6. UTILISING THE NAVIGATION MESH IN DECIDING A DIRECTION
(cid:18)ne o(cid:136) the core (cid:136)eatures o(cid:136) the (cid:17)avi(cid:137)ation (cid:16)esh is that it can descri(cid:132)e the surroundin(cid:137)s o(cid:136)
the virtual (cid:153)orld in ter(cid:143)s o(cid:136) conve(cid:154) (cid:146)ol(cid:155)(cid:137)ons(cid:484) (cid:23)his allo(cid:153)s us to find (cid:153)hether a s(cid:146)ecific trian(cid:137)le
side (cid:132)elon(cid:137)s to a (cid:153)all (cid:523)not connected to another trian(cid:137)le(cid:524), is (cid:146)art o(cid:136) the roo(cid:143) (cid:523)connected to
another (cid:136)ull(cid:155) visi(cid:132)le trian(cid:137)le(cid:524) or a (cid:146)assa(cid:137)e (cid:523)connected to a non(cid:486)(cid:136)ull(cid:155)(cid:486)visi(cid:132)le trian(cid:137)le(cid:524)(cid:484) Usin(cid:137) this
cate(cid:137)orisation (cid:153)e can identi(cid:136)(cid:155) (cid:153)here a s(cid:146)ecific a(cid:137)ent (cid:143)a(cid:155) enter another roo(cid:143)(cid:484) (cid:23)his in(cid:136)or(cid:143)ation
can act as an inter(cid:143)ediar(cid:155) ste(cid:146) to the (cid:146)reviousl(cid:155) (cid:143)entioned (cid:494)loo(cid:141)(cid:495) (cid:143)ethods(cid:484) (cid:12)t is in(cid:136)or(cid:143)ation
local to the room which points to possible ways out but deals with the actual visible surface
instead o(cid:136) the a(cid:143)ount o(cid:136) s(cid:146)ace or lon(cid:137)est line o(cid:136) si(cid:137)ht(cid:484) (cid:14)no(cid:153)led(cid:137)e o(cid:136) this in(cid:136)or(cid:143)ation (cid:523)doors or
(cid:494)(cid:137)ates(cid:495) (cid:132)et(cid:153)een s(cid:146)aces(cid:524) can act as another (cid:494)a(cid:417)ordance(cid:495) used to navi(cid:137)ate, as the ones descri(cid:132)ed
(cid:132)(cid:155) (cid:10)i(cid:132)son(cid:523)(cid:857)(cid:865)(cid:863)(cid:863)(cid:524)(cid:484) (cid:23)he navi(cid:137)ation (cid:143)esh re(cid:146)resentation is not discrete (cid:523)does not use a (cid:137)rid(cid:524) (cid:132)ut
each point lies on continuous space.
ASSISTED AGENT-BASED SIMULATIONS: 164.7
Fusing Non-Player Character Movement With Space Syntax

Proceedings of the 11th Space Syntax Symposium
6.1 ASSISTED STANDARD LOOK
(cid:23)he (cid:153)ei(cid:137)hin(cid:137) is (cid:132)ased on the an(cid:137)le a (cid:132)in has (cid:136)ro(cid:143) a s(cid:146)ecific (cid:146)oint(cid:484) (cid:12)(cid:136) there are (cid:143)ulti(cid:146)le (cid:146)assa(cid:137)es
then all o(cid:136) the(cid:143) contri(cid:132)ute to the (cid:153)ei(cid:137)htin(cid:137)(cid:484) (cid:10)iven that this re(cid:146)resentation is continuous (cid:153)e
(cid:136)ound it fittin(cid:137) to use a continuous (cid:143)ethod o(cid:136) (cid:153)ei(cid:137)htin(cid:137) to also avoid the (cid:146)it(cid:136)alls o(cid:136) discretisation
such as slight inaccuracies or problems created from low resolution.
(cid:22)(cid:146)ecificall(cid:155), a (cid:132)in is (cid:153)ei(cid:137)hted (cid:143)ore heavil(cid:155) i(cid:136) a radial line startin(cid:137) (cid:136)ro(cid:143) the cell the a(cid:137)ent is
standing on and passing through the middle of the bin is at a closer angle to the line with the
sa(cid:143)e startin(cid:137) (cid:146)oint, (cid:132)ut an endin(cid:137) at the (cid:143)iddle o(cid:136) the (cid:146)assa(cid:137)e(cid:484) (cid:23)he (cid:146)o(cid:153)er o(cid:136) the e(cid:417)ect is linear
(cid:523)a (cid:132)in at t(cid:153)ice the an(cid:137)le (cid:136)ro(cid:143) the (cid:146)assa(cid:137)e (cid:153)ill (cid:137)ain hal(cid:136) the (cid:153)ei(cid:137)htin(cid:137)(cid:524), (cid:132)ut an(cid:155) other (cid:136)unction
could be used to achieve more or less focus towards a passage.
(cid:9)i(cid:137)ure (cid:862) (cid:486) Passa(cid:137)e (cid:523)heav(cid:155) (cid:132)lac(cid:141) line, le(cid:136)t(cid:524) and e(cid:417)ect on each (cid:132)in (cid:523)ri(cid:137)ht(cid:524)
Instead of applying this weighting on its own we tested a fused methodology which takes into
account (cid:132)oth the (cid:494)standard loo(cid:141)(cid:495) (cid:153)ei(cid:137)htin(cid:137) and the one descri(cid:132)ed a(cid:132)ove(cid:484) (cid:26)e (cid:153)ill re(cid:136)er to this
a(cid:146)(cid:146)roach as (cid:494)assisted standard loo(cid:141)(cid:495)(cid:484) (cid:15)i(cid:141)e the (cid:494)standard loo(cid:141)(cid:495) al(cid:137)orith(cid:143), each (cid:132)in is added to a
selection pool as many times as it has cells, but this time for each bin this number is multiplied by
the (cid:153)ei(cid:137)htin(cid:137)(cid:484) (cid:23)here(cid:136)ore, in a sin(cid:137)le(cid:486)(cid:146)assa(cid:137)e e(cid:154)a(cid:143)(cid:146)le (cid:132)ins that are al(cid:143)ost (cid:146)er(cid:146)endicular to the
door will keep about the same weight, the ones that point towards the passage will have their
weight increased while the ones that point away from the door will have their weight decreased.
(cid:23)he e(cid:417)ect is sho(cid:153)n (cid:143)ore clearl(cid:155) in (cid:9)i(cid:137)ure (cid:863) (cid:153)here the (cid:494)standard loo(cid:141)(cid:495) in the (cid:146)reviousl(cid:155) sho(cid:153)n
roo(cid:143) is a(cid:417)ected(cid:484) (cid:23)he overall e(cid:417)ect o(cid:136) the roo(cid:143) re(cid:143)ains (cid:523)(cid:146)ull to the centre(cid:524) (cid:132)ut the (cid:132)ins that
point to the door are now more heavily weighted.
ASSISTED AGENT-BASED SIMULATIONS: 164.8
Fusing Non-Player Character Movement With Space Syntax

Proceedings of the 11th Space Syntax Symposium
(cid:9)i(cid:137)ure (cid:863) (cid:486) (cid:494)(cid:22)tandard loo(cid:141)(cid:495) (cid:523)le(cid:136)t(cid:524), e(cid:417)ect o(cid:136) an(cid:137)le(cid:486)to(cid:486)(cid:146)assa(cid:137)e on (cid:494)standard loo(cid:141)(cid:495) (cid:523)centre(cid:524), and closer
ins(cid:146)ection o(cid:136) the e(cid:417)ect (cid:523)ri(cid:137)ht(cid:524) (cid:153)ith (cid:146)ositive e(cid:417)ect (cid:523)lines (cid:143)ade lon(cid:137)er, (cid:137)reen(cid:524) and ne(cid:137)ative e(cid:417)ect (cid:523)lines
(cid:143)ade shorter, red(cid:524)
This hybrid look algorithm allows the passage to function like a local attractor no matter how
(cid:143)uch e(cid:143)(cid:146)t(cid:155) s(cid:146)ace there is (cid:132)ehind it(cid:484) (cid:12)t can there(cid:136)ore s(cid:146)ecificall(cid:155) address (cid:153)hat (cid:23)urner and
Penn (cid:523)(cid:858)(cid:856)(cid:856)(cid:858)(cid:524) identified as a (cid:146)ossi(cid:132)le li(cid:143)itation o(cid:136) the (cid:143)ethods that use line(cid:486)o(cid:136)(cid:486)si(cid:137)ht or (cid:153)al(cid:141)a(cid:132)le
sur(cid:136)ace as a(cid:417)ordances(cid:483) (cid:498)(cid:18)ur (cid:143)odel uses infinite si(cid:137)ht, and there(cid:136)ore an infinitel(cid:155) lon(cid:137) corridor
with respect to side corridors would drive all movement continuously along that corridor,
(cid:153)hereas (cid:153)e (cid:143)i(cid:137)ht e(cid:154)(cid:146)ect a hu(cid:143)an to ta(cid:141)e an e(cid:154)it so(cid:143)e (cid:153)a(cid:155) alon(cid:137) the corridor(cid:498) (cid:523)(cid:23)urner and
Penn (cid:858)(cid:856)(cid:856)(cid:858), (cid:146)(cid:484)(cid:860)(cid:864)(cid:857)(cid:524)
7. EVALUATION: AIMING FOR EXPLORATION
(cid:12)n order to (cid:132)uild so(cid:143)e (cid:146)reli(cid:143)inar(cid:155) confidence a(cid:132)out the ne(cid:153) (cid:143)ethodolo(cid:137)(cid:155) (cid:153)e develo(cid:146)ed t(cid:153)o
ne(cid:153) visual(cid:486)a(cid:137)ent (cid:143)etrics to (cid:143)easure the success o(cid:136) the al(cid:137)orith(cid:143), the s(cid:146)eed o(cid:136) e(cid:154)(cid:146)loration
and the (cid:146)ercenta(cid:137)e o(cid:136) stuc(cid:141) ste(cid:146)s(cid:484) (cid:12)n the first case (cid:153)e defined an a(cid:137)ent as success(cid:136)ul i(cid:136) the(cid:155)
(cid:143)ana(cid:137)ed to e(cid:154)(cid:146)lore a lar(cid:137)e a(cid:143)ount o(cid:136) s(cid:146)ace, (cid:143)uch li(cid:141)e (cid:23)urner and Penn(cid:495)s (cid:523)(cid:858)(cid:856)(cid:856)(cid:858)(cid:524) (cid:146)er(cid:486)a(cid:137)ent
cu(cid:143)ulative isovist(cid:484) (cid:23)he (cid:143)etric is s(cid:146)ecificall(cid:155) defined as the nu(cid:143)(cid:132)er o(cid:136) unique cells (cid:494)seen(cid:495), that
is, ne(cid:153) cells that a(cid:146)(cid:146)eared (cid:153)ithin an a(cid:137)ent(cid:495)s visual field as the(cid:155) too(cid:141) a ne(cid:153) ste(cid:146), divided (cid:132)(cid:155) the
number of steps taken.
(cid:26)e tested (cid:136)our i(cid:143)(cid:146)le(cid:143)entations, the standard loo(cid:141), (cid:15)o(cid:22), assisted standard and assisted
standard (cid:153)ith (cid:146)o(cid:153)er o(cid:136) e(cid:417)ect at (cid:858), across t(cid:153)o (cid:132)uildin(cid:137)s, the (cid:17)ational (cid:10)aller(cid:155) and the (cid:23)ate
(cid:5)ritain (cid:10)aller(cid:155) (cid:132)oth in (cid:15)ondon(cid:484) (cid:23)he field o(cid:136) vie(cid:153) and nu(cid:143)(cid:132)er o(cid:136) ste(cid:146)s o(cid:136) the a(cid:137)ents (cid:132)e(cid:136)ore
a ne(cid:153) (cid:494)loo(cid:141)(cid:495) (cid:153)ere set as in the ori(cid:137)inal studies (cid:132)(cid:155) (cid:23)urner and Penn (cid:523)(cid:858)(cid:856)(cid:856)(cid:858)(cid:482) (cid:858)(cid:856)(cid:856)(cid:863)(cid:524) at (cid:857)(cid:863)(cid:856)(cid:955) and
3 steps respectively. In contrast to the original studies, we are not comparing the agents to
real (cid:146)eo(cid:146)le there(cid:136)ore (cid:153)e did not (cid:136)ull(cid:155) ta(cid:141)e into account the hu(cid:143)ans(cid:495) cor(cid:146)oreal nature(cid:484) (cid:26)hile
the agents could still not pass or see through walls, we did not disallow them to step on a cell
already occupied by another agent. Therefore this simulation can only be thought of as a test
o(cid:136) the a(cid:137)ents(cid:495) navi(cid:137)atin(cid:137) and e(cid:154)(cid:146)lorin(cid:137) a(cid:132)ilities and (cid:143)a(cid:155) onl(cid:155) (cid:146)rovide insi(cid:137)hts a(cid:132)out hu(cid:143)an
behaviour in an abstract sense.
ASSISTED AGENT-BASED SIMULATIONS: 164.9
Fusing Non-Player Character Movement With Space Syntax

Proceedings of the 11th Space Syntax Symposium
(cid:9)i(cid:137)ure (cid:864) (cid:486) a(cid:524) (cid:15)e(cid:136)t to ri(cid:137)ht(cid:483) standard and (cid:15)o(cid:22) (cid:523)to(cid:146)(cid:524) (cid:146)ortals and (cid:146)ortals(cid:820)(cid:858) (cid:523)(cid:132)otto(cid:143)(cid:524) (cid:136)or (cid:17)ational (cid:10)aller(cid:155) (cid:132)(cid:524)
(cid:7)istri(cid:132)ution o(cid:136) e(cid:154)(cid:146)loration s(cid:146)eed (cid:523)to(cid:146)(cid:524) and (cid:146)ercenta(cid:137)e o(cid:136) stuc(cid:141) cells (cid:523)(cid:132)otto(cid:143)(cid:524) (cid:143)etric (cid:136)or the (cid:523)le(cid:136)t to ri(cid:137)ht(cid:524)
(cid:22)tandard, (cid:15)o(cid:22), Assisted standard, Assisted standard (cid:523)(cid:858)(cid:524) (cid:136)or the (cid:17)ational (cid:10)aller(cid:155) (cid:523)le(cid:136)t (cid:136)our(cid:524) and (cid:23)ate (cid:5)ritain
(cid:523)ri(cid:137)ht (cid:136)our(cid:524)
ASSISTED AGENT-BASED SIMULATIONS: 164.10
Fusing Non-Player Character Movement With Space Syntax

Proceedings of the 11th Space Syntax Symposium
tendency for the agents to roam the same rooms or get stuck more. The other three solutions
had (cid:143)uch hi(cid:137)her (cid:143)eans, and s(cid:143)aller di(cid:417)erences (cid:132)et(cid:153)een the(cid:143)(cid:484) (cid:12)t see(cid:143)s that (cid:494)(cid:15)o(cid:22) loo(cid:141)(cid:495) is
indeed an e(cid:417)ective e(cid:154)(cid:146)loration strate(cid:137)(cid:155), althou(cid:137)h not as e(cid:417)ective as the ne(cid:153) assisted standard,
or the sli(cid:137)htl(cid:155) (cid:143)ore e(cid:154)tre(cid:143)e assisted standard (cid:153)ith a (cid:146)o(cid:153)er o(cid:136) t(cid:153)o(cid:484)
(cid:23)he second (cid:143)etric e(cid:154)a(cid:143)ined (cid:153)as the nu(cid:143)(cid:132)er o(cid:136) ti(cid:143)es the a(cid:137)ents (cid:137)ot (cid:494)stuc(cid:141)(cid:495) and had to o(cid:146)en
their field o(cid:136) vie(cid:153) to (cid:859)(cid:862)(cid:856)(cid:955) to continue(cid:484) (cid:23)his can ha(cid:146)(cid:146)en i(cid:136) an a(cid:137)ent hits a (cid:153)all or (cid:153)al(cid:141)s into a
niche in such a (cid:153)a(cid:155) that its (cid:136)ull field o(cid:136) vision is (cid:132)loc(cid:141)ed and has no(cid:153)here to (cid:137)o(cid:484) A(cid:146)art (cid:136)ro(cid:143)
the fact that such a behaviour would be counter-intuitive for a human, it is not a strategy that
o(cid:146)ti(cid:143)ises (cid:136)or e(cid:154)(cid:146)loration and thus unli(cid:141)el(cid:155) to allo(cid:153) the a(cid:137)ent to vie(cid:153) (cid:143)ore s(cid:146)ace(cid:484) (cid:23)here(cid:136)ore an
a(cid:137)ent and in e(cid:154)tension the si(cid:143)ulation that had less (cid:136)ailed ste(cid:146)s (cid:153)as dee(cid:143)ed (cid:143)ore success(cid:136)ul in
e(cid:154)(cid:146)lorin(cid:137) the availa(cid:132)le environ(cid:143)ent(cid:484)
(cid:23)he overall (cid:143)ean (cid:146)ercenta(cid:137)e o(cid:136) stuc(cid:141) ste(cid:146)s (cid:153)as (cid:863)(cid:484)(cid:856)(cid:940) (cid:136)or the (cid:17)ational (cid:10)aller(cid:155) and (cid:863)(cid:484)(cid:861)(cid:940) (cid:136)or
the (cid:23)ate (cid:5)ritain (cid:10)aller(cid:155)(cid:484) (cid:12)n (cid:132)oth (cid:137)alleries e(cid:154)a(cid:143)ined the e(cid:417)ects are the sa(cid:143)e(cid:484) A(cid:137)ents (cid:153)ith the
(cid:494)standard loo(cid:141)(cid:495) al(cid:137)orith(cid:143) tended to (cid:137)et stuc(cid:141) a lot (cid:143)ore than the (cid:15)o(cid:22) and the t(cid:153)o assisted
standard looks, missing on average 12% / 13% of their steps in contrast to the rest which were
around (cid:861)(cid:486)(cid:862)(cid:940)(cid:484) (cid:18)nce a(cid:137)ain, the (cid:494)assisted standard loo(cid:141)(cid:495) al(cid:137)orith(cid:143) (cid:523)around (cid:861)(cid:940)(cid:524) (cid:136)ared sli(cid:137)htl(cid:155)
(cid:132)etter than the (cid:494)(cid:15)o(cid:22) loo(cid:141)(cid:495) (cid:523)(cid:862)(cid:940)(cid:524), (cid:132)ut the e(cid:417)ect (cid:153)as lo(cid:153)est at (cid:153)hen the (cid:146)o(cid:153)er o(cid:136) the al(cid:137)orith(cid:143)
(cid:153)as increased to (cid:858), althou(cid:137)h (cid:143)ar(cid:137)inall(cid:155)(cid:484) (cid:23)his e(cid:417)ect is li(cid:141)el(cid:155) to also cause the lo(cid:153)er values
o(cid:132)served in the first (cid:143)etric(cid:484) A(cid:137)ents that (cid:137)et stuc(cid:141) have to reset their field o(cid:136) vision (cid:523)turn around(cid:524)
due to the fact that they have no available choices to walk towards, meaning that most likely
(cid:136)or the (cid:146)ast (cid:136)e(cid:153) ste(cid:146)s the(cid:155) have (cid:132)een narro(cid:153)in(cid:137) their field o(cid:136) vie(cid:153) (cid:143)ovin(cid:137) to(cid:153)ards a (cid:153)all or
corner.
8. DISCUSSION AND FUTURE PLANS
(cid:23)his stud(cid:155) (cid:153)as a (cid:136)ra(cid:137)(cid:143)ent o(cid:136) e(cid:154)(cid:146)lorator(cid:155) research that ai(cid:143)ed to understand the al(cid:137)orith(cid:143)s
used (cid:136)or a(cid:137)ent(cid:486)(cid:132)ased anal(cid:155)sis (cid:153)ithin the field o(cid:136) (cid:22)(cid:146)ace (cid:22)(cid:155)nta(cid:154) and identi(cid:136)(cid:155) (cid:146)otential (cid:153)a(cid:155)s to
e(cid:154)(cid:146)and the(cid:143), ta(cid:141)in(cid:137) into consideration the advances in co(cid:143)(cid:146)uter(cid:486)(cid:137)a(cid:143)es research(cid:484) (cid:21)elevant
develo(cid:146)(cid:143)ents in video (cid:137)a(cid:143)e research (cid:153)ere discussed that o(cid:417)er ne(cid:153) (cid:146)ers(cid:146)ectives to the over(cid:486)
archin(cid:137) ai(cid:143), to si(cid:143)ulate natural hu(cid:143)an (cid:143)ove(cid:143)ent(cid:484) (cid:26)e (cid:146)resented an evolution o(cid:136) the (cid:22)(cid:146)ace
(cid:22)(cid:155)nta(cid:154) (cid:143)ethods (cid:153)ith techniques (cid:136)ro(cid:143) these ne(cid:153) (cid:146)ers(cid:146)ectives in the (cid:136)or(cid:143) o(cid:136) an (cid:494)assisted
standard loo(cid:141)(cid:495) al(cid:137)orith(cid:143)(cid:484)
(cid:26)e e(cid:154)a(cid:143)ined and descri(cid:132)ed the inner details o(cid:136) t(cid:153)o traditional al(cid:137)orith(cid:143)s descri(cid:132)ed (cid:132)(cid:155) (cid:23)urner
and Penn (cid:523)(cid:858)(cid:856)(cid:856)(cid:858)(cid:482) (cid:858)(cid:856)(cid:856)(cid:863)(cid:524), hi(cid:137)hli(cid:137)hted their (cid:146)otential and li(cid:143)itations and (cid:146)rovided (cid:146)ossi(cid:132)le (cid:153)a(cid:155)s
to introduce novel (cid:143)ethods (cid:136)ro(cid:143) video (cid:137)a(cid:143)e research(cid:484) (cid:26)e used an underl(cid:155)in(cid:137) navi(cid:137)ation (cid:143)esh
re(cid:146)resentation to allo(cid:153) (cid:136)or the identification o(cid:136) (cid:146)assa(cid:137)es (cid:153)hen an a(cid:137)ent is located in a roo(cid:143),
and a ne(cid:153), h(cid:155)(cid:132)rid loo(cid:141) al(cid:137)orith(cid:143) that a(cid:417)ects the (cid:494)standard loo(cid:141)(cid:495) (cid:153)ith an an(cid:137)le(cid:486)to(cid:486)(cid:146)assa(cid:137)e
weighting.
(cid:26)e then (cid:146)resented a ne(cid:153) al(cid:137)orith(cid:143)ic (cid:143)ethodolo(cid:137)(cid:155) tied s(cid:146)ecificall(cid:155) to a tas(cid:141) (cid:486)to e(cid:154)(cid:146)lore (cid:143)ore
s(cid:146)ace(cid:486) and tested the various (cid:494)loo(cid:141)(cid:495) (cid:143)ethods a(cid:137)ainst it(cid:484) (cid:26)e (cid:136)ound that (cid:153)hile the results are
not e(cid:154)tre(cid:143)el(cid:155) di(cid:417)erent (cid:132)et(cid:153)een the various loo(cid:141) al(cid:137)orith(cid:143)s, (cid:153)e could o(cid:132)serve su(cid:132)stantial
di(cid:417)erences, es(cid:146)eciall(cid:155) (cid:132)et(cid:153)een the (cid:494)standard loo(cid:141)(cid:495) al(cid:137)orith(cid:143) and the rest(cid:484) (cid:23)he di(cid:417)erences
identified (cid:153)ere that a(cid:137)ents (cid:153)ith the (cid:494)assisted standard loo(cid:141)(cid:495) tended to e(cid:154)(cid:146)lore (cid:143)ore cells, and
get stuck less than the ones with the traditional algorithms. This reminding us more the feeling
hu(cid:143)ans have (cid:153)hile e(cid:154)(cid:146)lorin(cid:137) ne(cid:153), never seen (cid:132)e(cid:136)ore, to(cid:146)o(cid:486)(cid:137)eo(cid:143)etric la(cid:155)outs and constantl(cid:155)
loo(cid:141)in(cid:137) (cid:136)or the thresholds to ne(cid:153) areas (cid:136)or e(cid:154)(cid:146)loration(cid:484)
(cid:18)n the other hand, the si(cid:143)ilarit(cid:155) o(cid:136) the results (cid:153)hen usin(cid:137) the ne(cid:153) al(cid:137)orith(cid:143) and (cid:15)(cid:18)(cid:22) does
not clearly point to one of them as the best. If the discussed methods of evaluation are to be
used in a di(cid:417)erent anal(cid:155)sis, the choice o(cid:136) al(cid:137)orith(cid:143) (cid:143)a(cid:155) need to co(cid:143)e do(cid:153)n to other (cid:136)actors,
such as the availa(cid:132)le hard(cid:153)are, si(cid:156)e o(cid:136) the (cid:143)odel or other data(cid:484) (cid:23)he underl(cid:155)in(cid:137) (cid:137)rid used in
the (cid:15)(cid:18)(cid:22) al(cid:137)orith(cid:143) can (cid:143)a(cid:141)e calculation e(cid:154)tre(cid:143)el(cid:155) heav(cid:155) (cid:136)or lar(cid:137)er (cid:143)odels (cid:132)ut it is a si(cid:143)(cid:146)ler
representation and thus likely to be followed by other datasets. Other validation methods such
as comparisons with real gate counts and movement traces will also be tested in the future to
(cid:136)urther hi(cid:137)hli(cid:137)ht di(cid:417)erences and si(cid:143)ilarities (cid:132)et(cid:153)een these (cid:143)ethods(cid:484)
ASSISTED AGENT-BASED SIMULATIONS: 164.11
Fusing Non-Player Character Movement With Space Syntax

Proceedings of the 11th Space Syntax Symposium
(cid:23)he (cid:494)standard loo(cid:141)(cid:495) and (cid:494)line(cid:486)o(cid:136)(cid:486)si(cid:137)ht loo(cid:141)(cid:495) al(cid:137)orith(cid:143)s are (cid:140)ust t(cid:153)o o(cid:136) the (cid:143)an(cid:155) al(cid:137)orith(cid:143)s in
de(cid:146)th(cid:143)a(cid:146)(cid:27) utilised (cid:132)(cid:155) the (cid:22)(cid:146)ace (cid:22)(cid:155)nta(cid:154) co(cid:143)(cid:143)unit(cid:155)(cid:484) (cid:12)n the (cid:136)uture (cid:153)e (cid:146)lan to create detailed
descri(cid:146)tions o(cid:136) these techniques to (cid:137)ain insi(cid:137)hts on their (cid:146)ossi(cid:132)ilities and li(cid:143)itations(cid:484) (cid:26)e also
plan to create implementations of the traditional techniques that avoid the pitfalls of the
discretisation, by substituting the grid for visibility in continuous space. These implementations
will then be used as bases for new hybrid techniques that take into account other elements of
space such as passages, or even transparencies.
(cid:23)his stud(cid:155) relied on evaluation techniques that ai(cid:143)ed solel(cid:155) (cid:136)or e(cid:154)(cid:146)loration(cid:484) (cid:23)his t(cid:155)(cid:146)e o(cid:136)
evaluation is use(cid:136)ul (cid:136)or a s(cid:146)ecific su(cid:132)set o(cid:136) s(cid:146)aces (cid:523)i(cid:484)e(cid:484) (cid:137)alleries(cid:524) and thus (cid:143)ore evaluation
(cid:143)etrics need to (cid:132)e e(cid:154)a(cid:143)ined, in fields (cid:132)e(cid:155)ond (cid:22)(cid:146)ace (cid:22)(cid:155)nta(cid:154)(cid:484) An e(cid:154)a(cid:143)(cid:146)le o(cid:136) this (cid:153)ould (cid:132)e
a(cid:146)(cid:146)l(cid:155)in(cid:137) a(cid:137)ent(cid:486)si(cid:143)ulation in (cid:153)or(cid:141)s(cid:146)aces (cid:153)here the sta(cid:417) is (cid:136)a(cid:143)iliar (cid:153)ith the s(cid:146)ace and the(cid:155)
are (cid:143)ore li(cid:141)el(cid:155) to ai(cid:143) to reach their destination (cid:523)(cid:141)itchens, toilets(cid:524) as (cid:136)ast as (cid:146)ossi(cid:132)le(cid:484) (cid:23)hus,
a future implementation will involve the development of techniques that allow the agents to
travel throu(cid:137)h s(cid:146)ace in search o(cid:136) s(cid:146)ecific destinations(cid:484)
ASSISTED AGENT-BASED SIMULATIONS: 164.12
Fusing Non-Player Character Movement With Space Syntax

Proceedings of the 11th Space Syntax Symposium
REFERENCES
(cid:5)att(cid:155), (cid:16)(cid:484), (cid:523)(cid:858)(cid:856)(cid:856)(cid:857)(cid:524)(cid:484) A(cid:137)ent(cid:486)(cid:5)ased Pedestrian (cid:16)odelin(cid:137)(cid:484) Environment and Planning B: Planning and Design, (cid:858)(cid:864)(cid:523)(cid:859)(cid:524),
(cid:146)(cid:146)(cid:484)(cid:859)(cid:858)(cid:857)(cid:514)(cid:859)(cid:858)(cid:862)(cid:484)
(cid:5)enedi(cid:141)t, (cid:16)(cid:484)(cid:15)(cid:484), (cid:523)(cid:857)(cid:865)(cid:863)(cid:865)(cid:524)(cid:484) (cid:23)o ta(cid:141)e hold o(cid:136) s(cid:146)ace(cid:483) isovists and isovist fields(cid:484) , (cid:862)(cid:523)(cid:857)(cid:524), (cid:146)(cid:146)(cid:484)(cid:860)(cid:863)(cid:514)(cid:862)(cid:861)(cid:484)
Cui, (cid:27)(cid:484) and (cid:22)hi, (cid:11)(cid:484), (cid:523)(cid:858)(cid:856)(cid:857)(cid:858)(cid:524)(cid:484) An overvie(cid:153) o(cid:136) (cid:146)athfindin(cid:137) in navi(cid:137)ation (cid:143)esh(cid:484) IJCSNS, (cid:857)(cid:858)(cid:523)(cid:857)(cid:858)(cid:524), (cid:146)(cid:484)(cid:860)(cid:864)(cid:484)
(cid:9)er(cid:137)uson, P(cid:484), (cid:9)riedrich, E(cid:484) and (cid:14)ari(cid:143)i, (cid:14)(cid:484), (cid:523)(cid:858)(cid:856)(cid:857)(cid:858)(cid:524)(cid:484) (cid:18)ri(cid:137)in(cid:486)destination (cid:153)ei(cid:137)htin(cid:137) in a(cid:137)ent (cid:143)odellin(cid:137) (cid:136)or (cid:146)edestrian
movement forecasting. In Proceedings of the international space syntax symposium. p. 8153.
(cid:10)i(cid:132)son, (cid:13)(cid:484)(cid:13)(cid:484), (cid:523)(cid:857)(cid:865)(cid:864)(cid:862)(cid:524)(cid:484) The Ecological Approach To Visual Perception (cid:17)e(cid:153) edition(cid:484), Ps(cid:155)cholo(cid:137)(cid:155) Press(cid:484)
(cid:10)i(cid:132)son, (cid:13)(cid:484)(cid:13)(cid:484), (cid:523)(cid:857)(cid:865)(cid:863)(cid:863)(cid:524)(cid:484) (cid:23)he (cid:23)heor(cid:155) o(cid:136) A(cid:417)ordances(cid:484) Perceiving, acting, and knowing: Toward an ecological psychology,
(cid:146)(cid:146)(cid:484)(cid:862)(cid:863)(cid:514)(cid:864)(cid:858)(cid:484)
(cid:11)art, P(cid:484), (cid:17)ilsson, (cid:17)(cid:484) and (cid:21)a(cid:146)hael, (cid:5)(cid:484), (cid:523)(cid:857)(cid:865)(cid:862)(cid:864)(cid:524)(cid:484) A (cid:9)or(cid:143)al (cid:5)asis (cid:136)or the (cid:11)euristic (cid:7)eter(cid:143)ination o(cid:136) (cid:16)ini(cid:143)u(cid:143) Cost Paths(cid:484)
, (cid:860)(cid:523)(cid:858)(cid:524), (cid:146)(cid:146)(cid:484)(cid:857)(cid:856)(cid:856)(cid:514)(cid:857)(cid:856)(cid:863)(cid:484)
(cid:11)el(cid:132)in(cid:137), (cid:7)(cid:484) and (cid:16)olnar, P(cid:484), (cid:523)(cid:857)(cid:865)(cid:865)(cid:864)(cid:524)(cid:484) (cid:22)el(cid:136)(cid:486)(cid:18)r(cid:137)ani(cid:156)ation Pheno(cid:143)ena in Pedestrian Cro(cid:153)ds(cid:484) Physics.
(cid:11)illier, (cid:5)(cid:484) and (cid:11)anson, (cid:13)(cid:484), (cid:523)(cid:857)(cid:865)(cid:864)(cid:860)(cid:524)(cid:484) (cid:23)he social lo(cid:137)ic o(cid:136) s(cid:146)ace(cid:484)
(cid:11)oo(cid:137)endoorn, (cid:22)(cid:484)P(cid:484), (cid:5)ov(cid:155), P(cid:484)(cid:11)(cid:484) and (cid:7)aa(cid:143)en, (cid:26)(cid:484), (cid:523)(cid:858)(cid:856)(cid:856)(cid:858)(cid:524)(cid:484) (cid:16)icrosco(cid:146)ic (cid:146)edestrian (cid:153)a(cid:155)findin(cid:137) and d(cid:155)na(cid:143)ics (cid:143)odellin(cid:137)(cid:484)
, (cid:857)(cid:858)(cid:859), (cid:146)(cid:484)(cid:857)(cid:861)(cid:860)(cid:484)
Penn, A(cid:484) and (cid:23)urner, A(cid:484), (cid:523)(cid:858)(cid:856)(cid:856)(cid:857)(cid:524)(cid:484) (cid:22)(cid:146)ace s(cid:155)nta(cid:154) (cid:132)ased a(cid:137)ent si(cid:143)ulation(cid:484)
(cid:22)noo(cid:141), (cid:10)(cid:484), (cid:523)(cid:858)(cid:856)(cid:856)(cid:856)(cid:524)(cid:484) (cid:22)i(cid:143)(cid:146)lified (cid:859)(cid:7) (cid:143)ove(cid:143)ent and (cid:146)athfindin(cid:137) usin(cid:137) navi(cid:137)ation (cid:143)eshes(cid:484) (cid:12)n Game Programming Gems.
(cid:146)(cid:146)(cid:484) (cid:858)(cid:864)(cid:864)(cid:514)(cid:859)(cid:856)(cid:860)(cid:484)
(cid:22)utherland, (cid:7)(cid:484), (cid:14)au(cid:136)(cid:143)an, (cid:14)(cid:484) and (cid:16)oito(cid:156)a, (cid:13)(cid:484), (cid:523)(cid:857)(cid:865)(cid:865)(cid:860)(cid:524)(cid:484) (cid:14)ine(cid:143)atics o(cid:136) nor(cid:143)al hu(cid:143)an (cid:153)al(cid:141)in(cid:137)(cid:484) (cid:11)(cid:151)(cid:143)(cid:131)(cid:144)(cid:3)(cid:153)(cid:131)(cid:142)(cid:141)(cid:139)(cid:144)(cid:137), (cid:858), (cid:146)(cid:146)(cid:484)(cid:858)(cid:859)(cid:514)
(cid:860)(cid:860)(cid:484)
(cid:23)urner, A(cid:484) et al(cid:484), (cid:523)(cid:858)(cid:856)(cid:856)(cid:857)(cid:524)(cid:484) (cid:9)ro(cid:143) (cid:12)sovists to (cid:25)isi(cid:132)ilit(cid:155) (cid:10)ra(cid:146)hs(cid:483) A (cid:16)ethodolo(cid:137)(cid:155) (cid:136)or the Anal(cid:155)sis o(cid:136) Architectural (cid:22)(cid:146)ace(cid:484) ,
(cid:858)(cid:864)(cid:523)(cid:857)(cid:524), (cid:146)(cid:146)(cid:484)(cid:857)(cid:856)(cid:859)(cid:514)(cid:857)(cid:858)(cid:857)(cid:484)
(cid:23)urner, A(cid:484), (cid:523)(cid:858)(cid:856)(cid:856)(cid:863)(cid:524)(cid:484) UC(cid:15) (cid:7)e(cid:146)th(cid:143)a(cid:146) (cid:863)(cid:483) (cid:9)ro(cid:143) isovist anal(cid:155)sis to (cid:137)eneric s(cid:146)atial net(cid:153)or(cid:141) anal(cid:155)sis(cid:484) , (cid:146)(cid:146)(cid:484)(cid:860)(cid:859)(cid:486)(cid:486)(cid:861)(cid:857)(cid:484)
(cid:23)urner, A(cid:484), (cid:16)ottra(cid:143), C(cid:484) and Penn, A(cid:484), (cid:523)(cid:858)(cid:856)(cid:856)(cid:860)(cid:524)(cid:484) An Ecolo(cid:137)ical A(cid:146)(cid:146)roach to (cid:10)enerative (cid:7)esi(cid:137)n(cid:484) (cid:12)n (cid:13)(cid:484) (cid:22)(cid:484) (cid:10)ero, ed(cid:484) Design
Computing and Cognition ’04(cid:484) (cid:7)ordrecht(cid:483) (cid:22)(cid:146)rin(cid:137)er (cid:17)etherlands, (cid:146)(cid:146)(cid:484) (cid:858)(cid:861)(cid:865)(cid:514)(cid:858)(cid:863)(cid:860)(cid:484)
(cid:23)urner, A(cid:484) and Penn, A(cid:484), (cid:523)(cid:858)(cid:856)(cid:856)(cid:858)(cid:524)(cid:484) Encodin(cid:137) (cid:17)atural (cid:16)ove(cid:143)ent as an A(cid:137)ent(cid:486)(cid:5)ased (cid:22)(cid:155)ste(cid:143)(cid:483) An (cid:12)nvesti(cid:137)ation into
(cid:11)u(cid:143)an Pedestrian (cid:5)ehaviour in the (cid:5)uilt Environ(cid:143)ent(cid:484) Environment and Planning B: Planning and Design,
(cid:858)(cid:865)(cid:523)(cid:860)(cid:524), (cid:146)(cid:146)(cid:484)(cid:860)(cid:863)(cid:859)(cid:514)(cid:860)(cid:865)(cid:856)(cid:484)
(cid:23)urner, A(cid:484) and Penn, A(cid:484), (cid:523)(cid:858)(cid:856)(cid:856)(cid:863)(cid:524)(cid:484) Evolvin(cid:137) (cid:7)irect Perce(cid:146)tion (cid:16)odels o(cid:136) (cid:11)u(cid:143)an (cid:5)ehavior in (cid:5)uildin(cid:137) (cid:22)(cid:155)ste(cid:143)s(cid:484) (cid:12)n (cid:17)(cid:484)
(cid:26)aldau et al(cid:484), eds(cid:484) Pedestrian and Evacuation (cid:7)(cid:155)na(cid:143)ics (cid:858)(cid:856)(cid:856)(cid:861)(cid:484) (cid:5)erlin, (cid:11)eidel(cid:132)er(cid:137)(cid:483) (cid:22)(cid:146)rin(cid:137)er (cid:5)erlin (cid:11)eidel(cid:132)er(cid:137),
(cid:146)(cid:146)(cid:484) (cid:860)(cid:857)(cid:857)(cid:514)(cid:860)(cid:858)(cid:858)(cid:484)
(cid:23)urner, A(cid:484) and Penn, A(cid:484), (cid:523)(cid:857)(cid:865)(cid:865)(cid:865)(cid:524)(cid:484) (cid:16)a(cid:141)in(cid:137) isovists s(cid:155)ntactic(cid:483) isovist inte(cid:137)ration anal(cid:155)sis(cid:484)
(cid:25)aroudis, (cid:23)(cid:484), (cid:523)(cid:858)(cid:856)(cid:857)(cid:858)(cid:524)(cid:484) depthmapX–Multi-platform Spatial Network Analyses Software, (cid:18)(cid:146)en(cid:22)ource(cid:484)
ASSISTED AGENT-BASED SIMULATIONS: 164.13
Fusing Non-Player Character Movement With Space Syntax
