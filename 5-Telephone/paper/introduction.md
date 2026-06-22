# Introduction Draft Notes

Working title: **When Truth Loses Its Source: Provenance-Aware Memory for Socially Distributed Agents**

## Human-Society Analogy

A true update can become unreliable without ever becoming intentionally false. In human
societies, a message may be accurate when first announced, but after several retellings
people often remember the content while losing track of who said it, when it was updated,
or whether it superseded an older version. This is the familiar telephone-game failure:
the social channel does not merely transmit content; it also drops source, timing, and
authority cues.

This analogy is central rather than incidental. LLM-agent societies reproduce a familiar
social failure in an instrumented setting. Unlike human rumor chains, an agent society lets
us observe every utterance, every injected update, every memory snapshot, and every final
answer. The paper's contribution is therefore not simply that agents "make mistakes" or
that transmitted messages degrade. It is that we can separate and measure three objects
that are usually conflated:

- **Reach:** whether the current update appears in the social transcript.
- **Speech:** whether agents later utter the current value.
- **Held answer:** whether agents answer with the current value when probed after
  transmission.

The key empirical pattern is that reach and speech can improve without durable held
truth. This is why "information spread" is not enough as an evaluation target for
agent societies.

There is an important tension here. If the goal is descriptive social simulation, reproducing
the telephone effect is a feature: agents become more human-like by selectively absorbing,
compressing, and reinterpreting messages. But if the goal is reliable coordination among agents,
human-likeness is not sufficient. Human societies also lose provenance, entrench outdated
claims, and mistake repeated rumor for reliable truth. The paper should therefore not say that
telephone effects are simply "bad." It should say that they are a natural social-memory
phenomenon that becomes a failure mode when the society is expected to maintain a changing fact.

## Source/Version As The Missing Social Signal

The working hypothesis is:

> Truth does not merely decay because content changes. Truth decays because content loses
> its source.

In ordinary natural-language memory, an agent may hear many statements:

```text
The repair drive is Saturday at the front porch.
The repair drive is Sunday at the community center.
Rosa said Sunday.
Someone mentioned the porch.
```

Without source/version tracking, these statements compete as undifferentiated text. The
old version can win because it was established early, repeated often, or retrieved more
easily. A later correction becomes just another sentence in the memory stream.

Source/version changes the social state representation. It lets agents ask not only
"what have I heard?" but also:

- Who did this claim come from?
- Is it an official/source update or a second-hand relay?
- Does this claim supersede an older version?
- Should a less frequent but newer/source-grounded claim override a more common stale one?

Human communication often uses these provenance cues explicitly:

```text
The school just sent an updated notice.
Rosa got the official update this morning.
Ignore the old group-chat message; the latest announcement says Sunday.
I checked with the organizer directly.
```

These are not hidden metadata channels. They are natural-language provenance markers.
The open design question for LLM-agent societies is whether such markers are preserved
by default, and if not, whether communication and memory interfaces should require them.

## Is Source/Version A Memory Improvement?

Yes, but only if we define "memory" broadly enough. Source/version is not a larger memory
buffer, a better embedding retriever, or a stronger reflection prompt. It is a **belief
revision structure** for social memory: the agent stores not only the claim text but also
the claim's provenance and revision order.

More precisely, source/version is a memory improvement at the **representation and
integration** layer:

- **Representation:** memories store claim, source, and version rather than claim text
  alone.
- **Integration:** when claims conflict, the agent can prefer newer/source-grounded
  updates over older frequent relays.
- **Retrieval:** the agent can surface the current source-grounded claim rather than a
  stale but semantically similar event.
- **Communication:** if the memory exposes provenance in the utterance, other agents can
  inherit the same revision cue.

So source/version is not "more memory." It is a different memory semantics: provenance-aware
social belief revision.

This distinction matters for the paper's honesty. Structured PROV should not be described
as a fully naturalistic cure. It is an upper-bound mechanism: if provenance is preserved
through the social channel, the society can repair truth decay. The PROV-text experiment
tests the harder question: whether ordinary LLM dialogue preserves those cues as text.

## Structured PROV, PROV-Text, And Broadcast

Broadcast and PROV answer different questions.

**Broadcast** directly writes the current fact into every agent. It bypasses social
transmission and therefore functions as an overwrite ceiling.

**Structured PROV** still requires social propagation. Only agents who hear the update can
adopt and relay it. But it assumes a reliable provenance channel, so it is best framed as
an idealized communication protocol or upper bound.

**PROV-text-free** removes the hidden channel and asks whether agents naturally preserve
source/version language in ordinary conversation. The initial result is negative: agents
do not spontaneously keep source/version phrases, so provenance does not propagate.

The next realistic variant is **PROV-text-norm**: require agents to communicate updates
with explicit attribution in text, such as:

```text
Source: Rosa received the official update.
Version: latest update.
Current value: Sunday at the community center.
```

This is not broadcast, because only agents who hear the message receive it. It is also not
unstructured natural conversation. It is a provenance-preserving communication norm. If it
outperforms GA while remaining below structured PROV or broadcast, the story becomes:

> Agent societies need not only better individual memory capacity, but social memory
> interfaces that preserve provenance through communication.

The first strong-norm result is best treated carefully: it shows that explicit text attribution
can repair held truth, but it is too protocolized to be called ordinary human conversation. Its
role is an upper bound for text-only provenance. The more realistic question is whether lighter
attribution habits -- "Rosa said the organizer updated it to Sunday" rather than a rigid
`Official round 1 update` label -- preserve enough provenance to help.

## Intro Spine

1. Human communication already teaches the lesson: true updates can become unreliable
   once source and version are lost.
2. LLM-agent societies inherit this social problem, but make it measurable because every
   utterance and memory state can be logged.
3. Prior agent-society work often treats spread as success; we evaluate fidelity of held
   answers after transmission.
4. Baseline GA societies show speech-belief dissociation: the current truth can appear in
   speech without becoming durable held truth.
5. Provenance-aware memory identifies the missing mechanism: social facts need source and
   version, not only text.
6. Structured PROV is an idealized upper bound; PROV-text tests whether provenance can
   survive as natural-language attribution; PROV-text-norm is the realistic design target.
