from __future__ import annotations

import csv
import json
import math
import re
import shutil
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches


ROOT = Path(__file__).resolve().parents[2]
RUNS = ROOT / "sim" / "runs"
FIG_DIR = ROOT / "paper" / "figures"
LATEX_FIG_DIR = ROOT / "paper" / "latex" / "figures"

COLORS = {
    "current": "#2ca25f",
    "stale": "#de2d26",
    "unknown": "#9aa0a6",
    "speech": "#e68613",
    "hold": "#3567c7",
    "source": "#8e63c7",
    "broadcast": "#2b8cbe",
    "baseline": "#6b7280",
    "grid": "#d9dee7",
    "ink": "#232631",
}

T_CRIT_95 = {
    1: 0.0,
    2: 12.706,
    3: 4.303,
    4: 3.182,
    5: 2.776,
    6: 2.571,
    7: 2.447,
    8: 2.365,
    9: 2.306,
    10: 2.262,
}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def aggregate(rel: str) -> dict:
    return load_json(RUNS / rel / "aggregate.json")


def run_rates(agg: dict, key: str = "current") -> list[float]:
    vals = []
    for row in agg["rows"]:
        total = row["agent_count"]
        vals.append(100.0 * row["currency_interview"][key] / total)
    return vals


def run_counts(agg: dict, key: str = "current") -> list[float]:
    return [row["currency_interview"][key] for row in agg["rows"]]


def mean_ci(vals: list[float]) -> tuple[float, float]:
    arr = np.array(vals, dtype=float)
    if len(arr) == 0:
        return 0.0, 0.0
    if len(arr) == 1:
        return float(arr[0]), 0.0
    sem = float(arr.std(ddof=1) / math.sqrt(len(arr)))
    t = T_CRIT_95.get(len(arr), 1.96)
    return float(arr.mean()), t * sem


def style_axes(ax, ylabel: str | None = None, ylim: tuple[float, float] = (0, 105)):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#8d96a8")
    ax.spines["bottom"].set_color("#8d96a8")
    ax.grid(axis="y", color=COLORS["grid"], linewidth=0.8, alpha=0.8)
    ax.set_ylim(*ylim)
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=9)
    ax.tick_params(labelsize=8)


def save(fig, name: str):
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    LATEX_FIG_DIR.mkdir(parents=True, exist_ok=True)
    out = FIG_DIR / name
    fig.savefig(out, dpi=320, bbox_inches="tight")
    plt.close(fig)
    shutil.copyfile(out, LATEX_FIG_DIR / name)


def save_summary(rows: list[dict]):
    path = FIG_DIR / "figure_data_summary.csv"
    fields = ["figure", "panel", "condition", "metric", "mean", "ci95", "n", "notes"]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def draw_network(ax, center=(0.5, 0.45), radius=0.22, n=12, color="#5b8bd8"):
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
    pts = []
    for i, a in enumerate(angles):
        r = radius * (0.78 + 0.22 * ((i * 7) % 5) / 4)
        x = center[0] + r * math.cos(a)
        y = center[1] + r * math.sin(a)
        pts.append((x, y))
    for i, p in enumerate(pts):
        q = pts[(i * 5 + 3) % len(pts)]
        ax.annotate("", xy=q, xytext=p, arrowprops=dict(arrowstyle="-", lw=0.8, color="#bcc6d4"))
    for p in pts:
        ax.add_patch(patches.Circle(p, 0.024, fc=color, ec="white", lw=1.0))


def fig1_setup():
    fig, ax = plt.subplots(figsize=(7.2, 2.65))
    ax.set_axis_off()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    panels = [
        (0.02, 0.12, 0.29, 0.78, "1. Inject"),
        (0.355, 0.12, 0.29, 0.78, "2. Relay"),
        (0.69, 0.12, 0.29, 0.78, "3. Probe"),
    ]
    for x, y, w, h, title in panels:
        ax.add_patch(
            patches.FancyBboxPatch(
                (x, y), w, h, boxstyle="round,pad=0.012,rounding_size=0.018",
                fc="#f7f9fc", ec="#c9d2e3", lw=1.0
            )
        )
        ax.text(x + 0.015, y + h - 0.055, title, fontsize=8.4, fontweight="bold", color=COLORS["ink"])

    # Inject
    x, y, w, h, _ = panels[0]
    ax.add_patch(patches.Circle((x + 0.105, y + 0.36), 0.028, fc=COLORS["source"], ec="white", lw=1))
    for px, py in [(0.19, 0.34), (0.15, 0.48), (0.23, 0.50), (0.21, 0.25), (0.11, 0.22), (0.27, 0.33), (0.17, 0.27)]:
        ax.add_patch(patches.Circle((x + px, y + py), 0.018, fc="#78a6dc", ec="white", lw=0.8))
    ax.add_patch(
        patches.FancyBboxPatch(
            (x + 0.05, y + 0.59), 0.20, 0.12, boxstyle="round,pad=0.010,rounding_size=0.012",
            fc="#fff7e8", ec=COLORS["speech"], lw=1.1
        )
    )
    ax.text(x + 0.15, y + 0.662, "truth update", ha="center", va="center",
            fontsize=6.9, fontweight="bold", color=COLORS["speech"])
    ax.text(x + 0.15, y + 0.622, "stale -> current", ha="center", va="center", fontsize=6.6)
    ax.annotate("", xy=(x + 0.105, y + 0.395), xytext=(x + 0.15, y + 0.58),
                arrowprops=dict(arrowstyle="-|>", lw=1.4, color=COLORS["speech"]))
    ax.text(x + 0.145, y + 0.16, "one seeded source; 25 agents", ha="center", fontsize=6.6, color="#4b5263")

    # Relay
    x, y, w, h, _ = panels[1]
    draw_network(ax, center=(x + 0.145, y + 0.43), radius=0.105, n=12)
    ax.add_patch(
        patches.FancyBboxPatch(
            (x + 0.055, y + 0.61), 0.19, 0.13, boxstyle="round,pad=0.012,rounding_size=0.012",
            fc="#eef5ff", ec="#6696df", lw=1.0
        )
    )
    ax.text(x + 0.15, y + 0.69, '"Sunday"', ha="center", va="center", fontsize=7.5, color="#243a56")
    ax.text(x + 0.15, y + 0.645, 'vs "Saturday"', ha="center", va="center", fontsize=7.5, color="#243a56")
    ax.text(x + 0.15, y + 0.19, "pairwise meetings + reflection memory", ha="center", fontsize=6.3, color="#4b5263")
    ax.text(x + 0.15, y + 0.125, "SAY: meeting utterances", ha="center", fontsize=6.8,
            color=COLORS["speech"], fontweight="bold")

    # Probe
    x, y, w, h, _ = panels[2]
    ax.text(x + 0.145, y + 0.675, "interview every agent", ha="center",
            fontsize=6.7, color=COLORS["ink"])
    ax.text(x + 0.145, y + 0.635, '"when/where now?"', ha="center",
            fontsize=6.7, color=COLORS["ink"])
    cols = [(COLORS["current"], "current"), (COLORS["stale"], "stale"), (COLORS["unknown"], "unknown")]
    for i, (c, lab) in enumerate(cols):
        bx = x + 0.045 + i * 0.085
        ax.add_patch(
            patches.FancyBboxPatch(
                (bx, y + 0.29), 0.055, 0.19, boxstyle="round,pad=0.008,rounding_size=0.01",
                fc="white", ec=c, lw=1.1
            )
        )
        ax.text(bx + 0.0275, y + 0.51, lab, ha="center", fontsize=6.6, color=c, fontweight="bold")
        for j in range(3 if lab != "unknown" else 6):
            ax.add_patch(patches.Circle((bx + 0.016 + (j % 3) * 0.016, y + 0.325 + (j // 3) * 0.045),
                                        0.0065, fc=c, ec=c))
    ax.text(x + 0.145, y + 0.16, "HOLD: later interview answer", ha="center",
            fontsize=6.8, color=COLORS["hold"], fontweight="bold")

    for a, b in [(0.315, 0.355), (0.65, 0.69)]:
        ax.annotate("", xy=(b - 0.01, 0.51), xytext=(a + 0.01, 0.51),
                    arrowprops=dict(arrowstyle="-|>", lw=1.5, color="#7a8599"))

    save(fig, "fig1_setup.png")


def count_value_speech(cond: str) -> dict[int, dict[str, int | float]]:
    base = RUNS / "m4_rebroadcast" / cond / "gpt-5.4-mini" / "ga"
    current = ["sunday", "community center"]
    stale = ["saturday", "front porch"]
    per_round: dict[int, dict[str, int | float]] = {}
    for r in range(5):
        cur = stale_count = valued = 0
        for path in sorted(base.glob(f"run_*/round_{r:03d}.json")):
            data = load_json(path)
            for enc in data["encounters"]:
                for utt in enc["utterances"]:
                    text = utt["text"].lower()
                    has_cur = any(m in text for m in current)
                    has_stale = any(m in text for m in stale)
                    if has_cur:
                        cur += 1
                    if has_stale:
                        stale_count += 1
                    if has_cur or has_stale:
                        valued += 1
        rate = 100.0 * cur / valued if valued else 0.0
        per_round[r + 1] = {"current": cur, "stale": stale_count, "valued": valued, "rate": rate}
    return per_round


def fig2_dissociation(summary_rows: list[dict]):
    conds = ["baseline", "source", "broadcast"]
    labels = ["Baseline", "Source", "Broadcast"]
    speech = {c: count_value_speech(c) for c in conds}
    hold = {c: aggregate(f"m4_rebroadcast/{c}") for c in conds}

    fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.55), gridspec_kw={"width_ratios": [1.25, 1]})
    ax = axes[0]
    for c, lab, color in zip(conds, labels, [COLORS["baseline"], COLORS["source"], COLORS["broadcast"]]):
        xs = list(speech[c].keys())
        ys = [speech[c][r]["rate"] for r in xs]
        ax.plot(xs, ys, marker="o", lw=1.8, label=lab, color=color)
        summary_rows.append({
            "figure": "fig2", "panel": "A", "condition": c, "metric": "final SAY current among valued utterances",
            "mean": f"{ys[-1]:.1f}", "ci95": "", "n": "5", "notes": f"{speech[c][5]['current']} current-coded / {speech[c][5]['valued']} valued utterances"
        })
    style_axes(ax, "current-valued speech (%)")
    ax.set_xticks([1, 2, 3, 4, 5])
    ax.set_xlabel("round", fontsize=9)
    ax.set_title("A. Speech moves", fontsize=9, loc="left", fontweight="bold")
    ax.legend(frameon=False, fontsize=7, loc="lower right")

    ax = axes[1]
    x = np.arange(len(conds))
    w = 0.34
    say_final = [speech[c][5]["rate"] for c in conds]
    hold_mean = []
    hold_ci = []
    for c in conds:
        mean, ci = mean_ci(run_rates(hold[c], "current"))
        hold_mean.append(mean)
        hold_ci.append(ci)
        summary_rows.append({
            "figure": "fig2", "panel": "B", "condition": c, "metric": "held current",
            "mean": f"{mean:.1f}", "ci95": f"{ci:.1f}", "n": str(len(hold[c]["rows"])), "notes": ""
        })
    ax.bar(x - w / 2, say_final, width=w, color=COLORS["speech"], label="SAY")
    ax.bar(x + w / 2, hold_mean, width=w, color=COLORS["hold"], label="HOLD", yerr=hold_ci,
           error_kw=dict(lw=0.8, capsize=2, capthick=0.8, ecolor="#222"))
    for i, (s, h) in enumerate(zip(say_final, hold_mean)):
        ax.text(i - w / 2, s + 3, f"{s:.0f}", ha="center", fontsize=7, color=COLORS["speech"])
        ax.text(i + w / 2, h + 3, f"{h:.0f}", ha="center", fontsize=7, color=COLORS["hold"])
    style_axes(ax, "current truth (%)")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_title("B. Belief stays low", fontsize=9, loc="left", fontweight="bold")
    ax.legend(frameon=False, fontsize=7, loc="upper left")
    fig.suptitle("Speech vs. belief", fontsize=11, fontweight="bold", y=1.04)
    fig.tight_layout()
    save(fig, "fig2_speech_belief.png")


def load_trajectories(cond: str) -> list[list[dict]]:
    base = RUNS / "fig2_r30" / cond / "gpt-5.4-mini" / "ga"
    out = []
    for path in sorted(base.glob("run_*/trajectory.json")):
        out.append(load_json(path)["trajectory"])
    return out


def trajectory_mean(cond: str, key: str) -> tuple[list[int], list[float]]:
    trajs = load_trajectories(cond)
    rounds = [p["round"] for p in trajs[0]]
    vals = []
    for i in range(len(rounds)):
        vals.append(100.0 * np.mean([t[i]["tally"][key] / 25 for t in trajs]))
    return rounds, vals


def fig3_decay(summary_rows: list[dict]):
    conds = ["baseline", "source", "broadcast"]
    labels = ["Baseline", "Source", "Broadcast"]
    colors = [COLORS["baseline"], COLORS["source"], COLORS["broadcast"]]

    fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.55), gridspec_kw={"width_ratios": [1.55, 1]})
    ax = axes[0]
    for c, lab, color in zip(conds, labels, colors):
        rounds, cur = trajectory_mean(c, "current")
        ax.plot(rounds, cur, color=color, lw=1.9, label=lab)
        peak = max(cur)
        peak_round = rounds[cur.index(peak)]
        summary_rows.append({
            "figure": "fig3", "panel": "A", "condition": c, "metric": "peak held current",
            "mean": f"{peak:.1f}", "ci95": "", "n": str(len(load_trajectories(c))), "notes": f"round {peak_round}"
        })
    ax.axvline(5, color="#bcc6d4", lw=0.8, ls="--")
    ax.text(5.2, 89, "r5 snapshot", fontsize=7, color="#687386")
    style_axes(ax, "held current (%)")
    ax.set_xlabel("round", fontsize=9)
    ax.set_title("A. Early peak", fontsize=9, loc="left", fontweight="bold")
    ax.legend(frameon=False, fontsize=7, loc="center right")

    ax = axes[1]
    x = np.arange(len(conds))
    bottom = np.zeros(len(conds))
    for key, color, label in [
        ("current", COLORS["current"], "current"),
        ("stale", COLORS["stale"], "stale"),
        ("unknown", COLORS["unknown"], "unknown"),
    ]:
        vals = []
        for c in conds:
            trajs = load_trajectories(c)
            vals.append(100.0 * np.mean([t[-1]["tally"][key] / 25 for t in trajs]))
        ax.bar(x, vals, bottom=bottom, color=color, label=label, width=0.55)
        bottom += vals
    ax.set_xticks(x)
    ax.set_xticklabels(["Base", "Source", "Broad."], fontsize=8)
    style_axes(ax, "final composition (%)")
    ax.set_title("B. Unknown dominates", fontsize=9, loc="left", fontweight="bold")
    ax.legend(frameon=False, fontsize=7, loc="lower right")
    fig.tight_layout()
    save(fig, "fig3_decay.png")


def fig4_failed_levers(summary_rows: list[dict]):
    panels = [
        ("A. Capability", [
            ("mini", "p3_power/m0_mini"),
            ("gpt-5.4", "p3_power/m0_gpt54"),
            ("gpt-5.5", "p3_power/m0_gpt55"),
        ]),
        ("B. Connectivity", [
            ("m=1", "p3_power/m1_mini_m1"),
            ("m=2", "p3_power/m0_mini"),
            ("m=3", "p3_power/m1_mini_m3"),
        ]),
        ("C. Memory", [
            ("GA", "m3_verify/ga_m2"),
            ("currency", "m3_verify/smga3g_m2"),
        ]),
        ("D. Authority", [
            ("baseline", "m4_rebroadcast/baseline"),
            ("source", "m4_rebroadcast/source"),
            ("broadcast", "m4_rebroadcast/broadcast"),
        ]),
    ]
    fig, axes = plt.subplots(2, 2, figsize=(7.2, 4.35))
    for ax, (title, items) in zip(axes.flat, panels):
        labels = [i[0] for i in items]
        means, cis, ns = [], [], []
        for lab, rel in items:
            agg = aggregate(rel)
            mean, ci = mean_ci(run_rates(agg, "current"))
            means.append(mean)
            cis.append(ci)
            ns.append(len(agg["rows"]))
            summary_rows.append({
                "figure": "fig4", "panel": title[:1], "condition": lab, "metric": "held current",
                "mean": f"{mean:.1f}", "ci95": f"{ci:.1f}", "n": str(len(agg["rows"])), "notes": rel
            })
        colors = [COLORS["hold"]] * len(labels)
        if title.startswith("D"):
            colors = [COLORS["baseline"], COLORS["source"], COLORS["broadcast"]]
        ax.bar(np.arange(len(labels)), means, yerr=cis, color=colors, width=0.58,
               error_kw=dict(lw=0.8, capsize=2, ecolor="#222"))
        ax.axhline(99.2, color=COLORS["current"], lw=0.9, ls=":", alpha=0.8)
        ax.text(-0.38, 99.5, "broadcast upper bound", fontsize=6.7, color=COLORS["current"], va="bottom")
        style_axes(ax, "held current (%)" if title.startswith(("A", "C")) else None)
        ax.set_xticks(np.arange(len(labels)))
        ax.set_xticklabels(labels, fontsize=7.5)
        ax.set_title(title, fontsize=9, loc="left", fontweight="bold")
        for i, m in enumerate(means):
            ax.text(i, m + cis[i] + 3, f"{m:.0f}", ha="center", fontsize=7)
    fig.suptitle("Natural levers fail", fontsize=11, fontweight="bold", y=1.02)
    fig.tight_layout()
    save(fig, "fig4_failed_levers.png")


def fig5_mechanism(summary_rows: list[dict]):
    items = [
        ("baseline: narrow early", "m4_rebroadcast/baseline", COLORS["baseline"]),
        ("source: narrow repeated", "m4_rebroadcast/source", COLORS["source"]),
        ("late all-agent broadcast", "p1rec/r5_broadcast", COLORS["stale"]),
        ("early all-agent broadcast", "p1rec/r1_broadcast", COLORS["current"]),
        ("every-round broadcast", "m4_rebroadcast/broadcast", COLORS["broadcast"]),
    ]
    means, cis = [], []
    for lab, rel, _ in items:
        agg = aggregate(rel)
        mean, ci = mean_ci(run_rates(agg, "current"))
        means.append(mean)
        cis.append(ci)
        summary_rows.append({
            "figure": "fig5", "panel": "A", "condition": lab.replace("\n", " "),
            "metric": "held current", "mean": f"{mean:.1f}", "ci95": f"{ci:.1f}",
            "n": str(len(agg["rows"])), "notes": rel
        })

    fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.55), gridspec_kw={"width_ratios": [1.35, 1]})
    ax = axes[0]
    y = np.arange(len(items))[::-1]
    ax.barh(y, means, xerr=cis, color=[c for _, _, c in items], height=0.58,
            error_kw=dict(lw=0.8, capsize=2, ecolor="#222"))
    ax.set_xlim(0, 105)
    ax.grid(axis="x", color=COLORS["grid"], linewidth=0.8, alpha=0.8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#8d96a8")
    ax.spines["bottom"].set_color("#8d96a8")
    ax.set_xlabel("held current (%)", fontsize=9)
    ax.tick_params(labelsize=8)
    ax.set_yticks(y)
    ax.set_yticklabels([i[0] for i in items], fontsize=7.2)
    ax.set_title("A. Timing", fontsize=9, loc="left", fontweight="bold")
    for yi, m, ci in zip(y, means, cis):
        ax.text(min(m + ci + 3, 102), yi, f"{m:.0f}", va="center", fontsize=7)

    ax = axes[1]
    ax.set_axis_off()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.text(0.5, 0.95, "B. Entrenchment rule", ha="center", fontsize=9, fontweight="bold")
    ax.text(0.08, 0.67, "early", fontsize=8, color="#4b5263")
    ax.text(0.08, 0.28, "late", fontsize=8, color="#4b5263")
    ax.text(0.34, 0.08, "narrow", fontsize=8, color="#4b5263", ha="center")
    ax.text(0.72, 0.08, "broad", fontsize=8, color="#4b5263", ha="center")
    cells = [
        (0.24, 0.55, 0.23, 0.23, "single\nsource", "low", COLORS["baseline"]),
        (0.60, 0.55, 0.23, 0.23, "all agents\nat r1", "high", COLORS["current"]),
        (0.24, 0.18, 0.23, 0.23, "source\nrepeated", "low", COLORS["source"]),
        (0.60, 0.18, 0.23, 0.23, "all agents\nat r5", "low", COLORS["stale"]),
    ]
    for x0, y0, w, h, title, outcome, color in cells:
        ax.add_patch(patches.FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0.01,rounding_size=0.02",
                                            fc="#f7f9fc", ec=color, lw=1.2))
        ax.text(x0 + w / 2, y0 + 0.145, title, ha="center", fontsize=7)
        ax.text(x0 + w / 2, y0 + 0.055, outcome, ha="center", fontsize=8, color=color, fontweight="bold")
    ax.annotate("truth persists only when it is established early and broadly",
                xy=(0.72, 0.68), xytext=(0.51, 0.9), fontsize=7, color=COLORS["current"],
                arrowprops=dict(arrowstyle="->", color=COLORS["current"], lw=1.0))
    fig.tight_layout()
    save(fig, "fig5_mechanism.png")


def fig6_robustness(summary_rows: list[dict]):
    scenario_items = [
        ("repair", {
            "baseline": "m4_rebroadcast/baseline",
            "source": "m4_rebroadcast/source",
            "broadcast": "m4_rebroadcast/broadcast",
        }),
        ("book", {
            "baseline": "g1_scenarios/book_club_baseline",
            "source": "g1_scenarios/book_club_source",
            "broadcast": "g1_scenarios/book_club_broadcast",
        }),
        ("carpool", {
            "baseline": "g1_scenarios/carpool_baseline",
            "source": "g1_scenarios/carpool_source",
            "broadcast": "g1_scenarios/carpool_broadcast",
        }),
        ("thick\npersona", {
            "baseline": "g2_persona/baseline",
            "source": "g2_persona/source",
            "broadcast": "g2_persona/broadcast",
        }),
    ]
    conds = ["baseline", "source", "broadcast"]
    fig, axes = plt.subplots(1, 3, figsize=(7.2, 2.55), gridspec_kw={"width_ratios": [1.55, 0.9, 0.8]})

    ax = axes[0]
    x = np.arange(len(scenario_items))
    w = 0.23
    offsets = [-w, 0, w]
    colors = [COLORS["baseline"], COLORS["source"], COLORS["broadcast"]]
    for off, cond, color in zip(offsets, conds, colors):
        means, cis = [], []
        for scenario, rels in scenario_items:
            agg = aggregate(rels[cond])
            mean, ci = mean_ci(run_rates(agg, "current"))
            means.append(mean)
            cis.append(ci)
            summary_rows.append({
                "figure": "fig6", "panel": "A", "condition": f"{scenario}:{cond}",
                "metric": "held current", "mean": f"{mean:.1f}", "ci95": f"{ci:.1f}",
                "n": str(len(agg["rows"])), "notes": rels[cond]
            })
        ax.bar(x + off, means, yerr=cis, width=w, color=color, label=cond,
               error_kw=dict(lw=0.7, capsize=1.8, ecolor="#222"))
    style_axes(ax, "held current (%)")
    ax.set_xticks(x)
    ax.set_xticklabels([s[0] for s in scenario_items], fontsize=7.4)
    ax.set_title("A. Generality", fontsize=9, loc="left", fontweight="bold")
    ax.legend(frameon=False, fontsize=6.1, loc="upper center", ncol=3,
              bbox_to_anchor=(0.50, 1.00), columnspacing=0.7, handlelength=1.1)

    ax = axes[1]
    # Source effect as delta from baseline.
    deltas, cis = [], []
    labels = []
    for scenario, rels in scenario_items:
        b = run_rates(aggregate(rels["baseline"]), "current")
        s = run_rates(aggregate(rels["source"]), "current")
        n = min(len(b), len(s))
        diff = [s[i] - b[i] for i in range(n)]
        mean, ci = mean_ci(diff)
        labels.append(scenario)
        deltas.append(mean)
        cis.append(ci)
    ax.axhline(0, color="#4b5263", lw=0.8)
    ax.bar(np.arange(len(labels)), deltas, yerr=cis, color=COLORS["source"], width=0.55,
           error_kw=dict(lw=0.7, capsize=1.8, ecolor="#222"))
    style_axes(ax, "source - baseline (pp)", ylim=(-25, 30))
    ax.set_xticks(np.arange(len(labels)))
    ax.set_xticklabels(labels, fontsize=7.2)
    ax.set_title("B. Source gap", fontsize=9, loc="left", fontweight="bold")

    ax = axes[2]
    agreement = [99, 100, 100]
    judge_current = [12, 15.2, 99.2]
    x = np.arange(3)
    ax.bar(x - 0.16, agreement, width=0.32, color="#6baed6", label="agreement")
    ax.bar(x + 0.16, judge_current, width=0.32, color=COLORS["hold"], label="judge current")
    style_axes(ax, "%")
    ax.set_xticks(x)
    ax.set_xticklabels(["base", "source", "broad."], fontsize=7)
    ax.set_title("C. Judge check", fontsize=9, loc="left", fontweight="bold")
    ax.legend(frameon=False, fontsize=5.7, loc="upper center",
              bbox_to_anchor=(0.54, -0.18), ncol=1, handlelength=1.1)

    fig.tight_layout(rect=(0, 0.05, 1, 1))
    save(fig, "fig6_robustness.png")


def main():
    summary_rows: list[dict] = []
    fig1_setup()
    fig2_dissociation(summary_rows)
    fig3_decay(summary_rows)
    fig4_failed_levers(summary_rows)
    fig5_mechanism(summary_rows)
    fig6_robustness(summary_rows)
    save_summary(summary_rows)


if __name__ == "__main__":
    main()
