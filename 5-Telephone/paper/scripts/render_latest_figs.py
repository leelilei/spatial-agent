#!/usr/bin/env python3
"""Render the current main-text figures from the latest ledger data (2026-06-26).

Sources: RESULTS.md ledger — M0-M4/G2 (levers), M4 (dissociation),
C5 (architecture), C14 n=8 (capability), C16 (adversarial), C17b n=5 (comms curve).
Outputs PNGs into ../figures/ with fig_*.png names (does not overwrite the older fig1-6).
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parents[1] / "figures"
TEAL, GRAY, RED, BLUE = "#1D9E75", "#B4B2A9", "#E24B4A", "#378ADD"
GE, TE, RE = "#888780", "#0F6E56", "#A32D2D"
plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                     "axes.spines.right": False, "figure.dpi": 150})


def save(fig, name):
    fig.savefig(OUT / name, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print("wrote", name)


# 1 — failed levers (M0-M4/G2)
fig, ax = plt.subplots(figsize=(6.2, 3.6))
labels = ["baseline", "+capability", "+memory", "+persona", "+source", "broadcast\n(spoon-feed)"]
vals = [14, 21, 18, 14, 15, 99]
ax.bar(labels, vals, color=[GRAY]*5+[TEAL], edgecolor=[GE]*5+[TE])
for i, v in enumerate(vals):
    ax.text(i, v+2, str(v), ha="center", fontsize=9)
ax.set_ylabel("held-current (%)"); ax.set_ylim(0, 108)
ax.set_title("Failed natural levers — only broadcast lifts held truth")
plt.setp(ax.get_xticklabels(), fontsize=9)
save(fig, "fig_failed_levers.png")

# 2 — say vs hold dissociation (M4)
fig, ax = plt.subplots(figsize=(6, 3.6))
x = np.arange(3); w = 0.38
ax.bar(x-w/2, [56, 83, 99], w, label="SAID (utterance)", color=BLUE)
ax.bar(x+w/2, [12, 15, 99], w, label="HELD (interview)", color=TEAL)
ax.set_xticks(x); ax.set_xticklabels(["baseline", "source", "broadcast"])
ax.set_ylabel("current (%)"); ax.set_ylim(0, 108); ax.legend(frameon=False)
ax.set_title("Speech is not belief — source moves SAID, not HELD")
save(fig, "fig_say_vs_hold.png")

# 3 — P1-rec tombstone. The original timing contrast was retracted after an
# injection-index audit; keep the stable filename but make accidental reuse safe.
fig, ax = plt.subplots(figsize=(5.6, 3.6))
ax.axis("off")
ax.text(
    0.5, 0.58, "RETRACTED", ha="center", va="center",
    fontsize=22, fontweight="bold", color=RED, transform=ax.transAxes,
)
ax.text(
    0.5, 0.36,
    "P1-rec used an invalid late-injection index.\n"
    "It provides no evidence about recency or entrenchment.",
    ha="center", va="center", fontsize=11, color="#444", transform=ax.transAxes,
)
ax.set_title("Timing contrast excluded after configuration audit")
save(fig, "fig_entrenchment.png")

# 4 — architecture comparison (C5)
fig, ax = plt.subplots(figsize=(6, 3.6))
labels = ["Raw", "Mem0", "A-MEM", "GA", "GA-curr", "MemBank", "PROV"]
vals = [14, 18, 19, 22, 25, 25, 57]
ax.barh(labels, vals, color=[GRAY]*6+[TEAL], edgecolor=[GE]*6+[TE])
for i, v in enumerate(vals):
    ax.text(v+1, i, str(v), va="center", fontsize=9)
ax.set_xlabel("held-current (%)"); ax.set_xlim(0, 66); ax.invert_yaxis()
ax.set_title("Controlled memory comparison (n=8)")
save(fig, "fig_architecture.png")

# 5 — capability check (C14, n=8)
fig, ax = plt.subplots(figsize=(6, 3.6))
x = np.arange(2); w = 0.38
ga, pv = [21.5, 15.5], [57, 64]
ga_err = [[21.5-13, 15.5-10], [30-21.5, 21-15.5]]
pv_err = [[57-49, 64-58], [65-57, 70-64]]
ax.bar(x-w/2, ga, w, yerr=ga_err, label="GA", color=GRAY, capsize=4, ecolor="#555")
ax.bar(x+w/2, pv, w, yerr=pv_err, label="PROV", color=TEAL, capsize=4, ecolor="#555")
ax.set_xticks(x); ax.set_xticklabels(["mini", "DeepSeek-V4-Flash"])
ax.set_ylabel("held-current (%)"); ax.set_ylim(0, 80); ax.legend(frameon=False)
ax.set_title("Capability check (n=8) — cure survives model family")
save(fig, "fig_capability_c14.png")

# 6 — adversarial liar (C16)
fig, ax = plt.subplots(figsize=(6.4, 3.6))
x = np.arange(4); w = 0.38
ax.bar(x-w/2, [57, 33, 64, 64], w, label="held-current", color=TEAL)
ax.bar(x+w/2, [11, 57, 0, 0], w, label="stale (hijacked)", color=RED)
ax.set_xticks(x)
ax.set_xticklabels(["PROV\nno-adv", "PROV\nliar", "APM\nno-adv", "APM\nliar"], fontsize=9)
ax.set_ylabel("% of agents"); ax.set_ylim(0, 75); ax.legend(frameon=False)
ax.set_title("Origin anchoring prevents adversarial hijack")
save(fig, "fig_apm_adversarial.png")

# 7 — comms-sufficiency curve (C17b, n=5)
fig, ax = plt.subplots(figsize=(6.6, 4))
X = [0, 0.03, 0.05, 0.07, 0.1, 0.15, 0.2, 0.25, 0.3, 0.5, 0.8]
M = [11, 16, 23, 38, 40, 49, 74, 87, 87, 100, 100]
HI = [15, 25, 33, 46, 54, 62, 95, 95, 97, 100, 100]
LO = [7, 7, 13, 31, 27, 36, 52, 79, 77, 100, 100]
ax.fill_between(X, LO, HI, color=TEAL, alpha=0.18, label="95% CI")
ax.plot(X, M, "-o", color=TEAL, lw=2, ms=5, label="held-current")
ax.plot(X, [0]*len(X), "--s", color=RED, lw=1.8, ms=4, label="stale")
ax.set_xlabel("mention probability (sparse → dense)")
ax.set_ylabel("% of agents"); ax.set_ylim(0, 105); ax.set_xlim(0, 0.85)
ax.legend(frameon=False)
ax.set_title("APM communication-sufficiency curve (n=5) — non-saturating, stale≡0")
save(fig, "fig_apm_comms_curve.png")

print("ALL DONE ->", OUT)
