#!/usr/bin/env python3
"""Build the five CityIntent v1.1 manuscript figures from audited artifacts."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import gridspec
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle
import numpy as np
import pandas as pd


plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Arial", "DejaVu Sans", "Liberation Sans"]
plt.rcParams["svg.fonttype"] = "none"
plt.rcParams["pdf.fonttype"] = 42
plt.rcParams.update({
    "font.size": 7,
    "axes.titlesize": 8,
    "axes.labelsize": 7,
    "xtick.labelsize": 6.5,
    "ytick.labelsize": 6.5,
    "legend.fontsize": 6.5,
    "axes.linewidth": 0.7,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "legend.frameon": False,
})

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "paper" / "figures" / "main"
SOURCE = ROOT / "paper" / "figures" / "source_data"
OUT.mkdir(parents=True, exist_ok=True)
SOURCE.mkdir(parents=True, exist_ok=True)

C = {
    "dark": "#30334F",
    "blue": "#637DB7",
    "blue_soft": "#B9C7E8",
    "rose": "#C98295",
    "rose_soft": "#E7C6D0",
    "teal": "#5B9EA0",
    "teal_soft": "#B9DADB",
    "gold": "#C4A45B",
    "grey": "#8A8A8A",
    "light": "#E6E6E6",
    "pale": "#F3F3F3",
    "red": "#B65050",
    "green": "#4E8B62",
    "white": "#FFFFFF",
}

MODEL_ORDER = ["Claude", "DeepSeek", "Qwen"]
POLICY_ORDER = ["PlanExec", "ReAct"]
CONSTRUCT_ORDER = [
    "disruption_recovery", "time_window_scheduling",
    "resource_budget_allocation", "poi_availability_service_evidence",
    "memory_conditioned_preference", "social_coordination_copresence",
    "multi_party_commitment", "compound_long_horizon",
]
CONSTRUCT_SHORT = ["Disruption", "Time", "Resource", "POI", "Memory", "Social", "Multi-party", "Compound"]


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def panel(ax, label):
    ax.text(-0.08, 1.04, label, transform=ax.transAxes, fontweight="bold",
            fontsize=9, va="bottom", ha="left")


def save(fig, name):
    fig.savefig(OUT / f"{name}.svg", bbox_inches="tight")
    fig.savefig(OUT / f"{name}.pdf", bbox_inches="tight")
    fig.savefig(OUT / f"{name}.png", dpi=300, bbox_inches="tight")
    fig.savefig(OUT / f"{name}.tiff", dpi=600, bbox_inches="tight",
                pil_kwargs={"compression": "tiff_lzw"})
    plt.close(fig)


def model_name(raw):
    if raw.startswith("claude"):
        return "Claude"
    if raw.startswith("deepseek"):
        return "DeepSeek"
    if raw.startswith("qwen"):
        return "Qwen"
    return raw


def policy_name(raw):
    return "ReAct" if "react" in raw else "PlanExec"


def load_wave3_traces():
    dirs = [
        ROOT / "results/cityintent_v1_1_candidate/native_wave3_public_v0_final_48_2026-08-06/traces.json",
        ROOT / "results/cityintent_v1_1_candidate/native_wave3_public_v1_final_48_2026-08-06/traces.json",
        ROOT / "results/cityintent_v1_1_candidate/native_wave3_public_v2_final_48_2026-08-06/traces.json",
    ]
    rows = []
    for world_index, path in enumerate(dirs):
        for row in read_json(path):
            rows.append({
                "world": f"v{world_index}",
                "scenario_id": row["scenario_id"],
                "construct": row["family"],
                "model": model_name(row["model_info"]["model"]),
                "policy": policy_name(row["agent_type"]),
                "agent_type": row["agent_type"],
                "task_completion": row["metrics"]["task_completion"],
                "trace_feasibility": row["metrics"]["trace_feasibility"],
                "intention_consistency": row["metrics"]["intention_consistency"],
                "full_task": float(row["metrics"]["task_completion"] == 1.0),
                "trace": row["trace"],
                "final_state": row["final_state"],
                "failure_taxonomy": row.get("failure_taxonomy") or {},
            })
    return pd.DataFrame(rows)


def bootstrap_ci(values, seed=20260806, n_boot=5000):
    values = np.asarray(values, dtype=float)
    rng = np.random.default_rng(seed)
    draws = rng.choice(values, size=(n_boot, len(values)), replace=True).mean(axis=1)
    return values.mean(), *np.quantile(draws, [0.025, 0.975])


def placeholder(ax, title, lines):
    ax.set_axis_off()
    ax.add_patch(Rectangle((0.03, 0.08), 0.94, 0.82, transform=ax.transAxes,
                           facecolor="none", edgecolor=C["grey"], lw=0.8,
                           linestyle=(0, (3, 2))))
    ax.text(0.5, 0.68, title, transform=ax.transAxes, ha="center", va="center",
            fontsize=8, fontweight="bold", color=C["dark"])
    ax.text(0.5, 0.48, "Data collection pending", transform=ax.transAxes,
            ha="center", va="center", fontsize=7.5, color=C["red"])
    ax.text(0.5, 0.28, "\n".join(lines), transform=ax.transAxes,
            ha="center", va="center", fontsize=6.5, color=C["grey"])


def figure1():
    fig = plt.figure(figsize=(7.2, 6.15))
    gs = gridspec.GridSpec(2, 6, height_ratios=[1.25, 1], hspace=0.38, wspace=0.45)
    ax = fig.add_subplot(gs[0, :]); ax.set_axis_off(); panel(ax, "a")
    nodes = [
        (0.02, "Private\nintention", C["rose_soft"]),
        (0.20, "Blind agent\npolicy", C["blue_soft"]),
        (0.39, "Action\nprotocol", C["blue_soft"]),
        (0.58, "Dynamic city\nsimulator", C["teal_soft"]),
        (0.78, "Evidence trace\n& scorer", C["rose_soft"]),
    ]
    for x, text, color in nodes:
        box = FancyBboxPatch((x, 0.40), 0.15, 0.25, boxstyle="round,pad=0.012,rounding_size=0.015",
                             transform=ax.transAxes, facecolor=color, edgecolor=C["dark"], lw=0.8)
        ax.add_patch(box); ax.text(x+0.075, 0.525, text, ha="center", va="center", transform=ax.transAxes)
    for i in range(len(nodes)-1):
        x1 = nodes[i][0] + 0.15; x2 = nodes[i+1][0]
        ax.add_patch(FancyArrowPatch((x1+0.008, 0.525), (x2-0.008, 0.525),
                                    transform=ax.transAxes, arrowstyle="-|>", mutation_scale=9,
                                    lw=0.8, color=C["dark"]))
    event = FancyBboxPatch((0.49, 0.78), 0.18, 0.13, boxstyle="round,pad=0.01",
                           transform=ax.transAxes, facecolor=C["pale"], edgecolor=C["gold"], lw=1)
    ax.add_patch(event); ax.text(0.58, 0.845, "Public events\nclosures · updates · windows",
                                ha="center", va="center", transform=ax.transAxes, fontsize=6.5)
    ax.add_patch(FancyArrowPatch((0.58, 0.78), (0.655, 0.66), transform=ax.transAxes,
                                arrowstyle="-|>", mutation_scale=9, lw=0.8, color=C["gold"]))
    ax.text(0.5, 0.14, "Verified outcome, not plausible narration", transform=ax.transAxes,
            ha="center", color=C["dark"], fontsize=8, fontweight="bold")

    axb = fig.add_subplot(gs[1, :2]); axb.set_axis_off(); panel(axb, "b")
    axb.set_title("Scenario anatomy", pad=4)
    anatomy = [("Intent", C["rose_soft"]), ("World", C["teal_soft"]),
               ("Event", "#E7DAB9"), ("Constraints", C["blue_soft"]),
               ("Oracle", "#CBE0CE"), ("Negative", "#E7C8C8")]
    for i, (label, color) in enumerate(anatomy):
        y = 0.85 - i*0.14
        axb.add_patch(Rectangle((0.08, y-0.06), 0.22, 0.09, transform=axb.transAxes,
                                facecolor=color, edgecolor="none"))
        axb.text(0.19, y-0.015, label, ha="center", va="center", transform=axb.transAxes)
        axb.plot([0.33, 0.88], [y-0.015, y-0.015], transform=axb.transAxes,
                 color=C["light"], lw=3, solid_capstyle="round")

    axc = fig.add_subplot(gs[1, 2:4]); axc.set_axis_off(); panel(axc, "c")
    axc.set_title("Eight intention constructs", pad=4)
    for i, label in enumerate(CONSTRUCT_SHORT):
        r, c = divmod(i, 2); x = 0.05 + c*0.49; y = 0.82-r*0.21
        color = [C["blue_soft"], C["teal_soft"], C["rose_soft"], "#E7DAB9"][r]
        axc.add_patch(FancyBboxPatch((x, y-0.11), 0.42, 0.13, boxstyle="round,pad=0.008",
                                    transform=axc.transAxes, facecolor=color, edgecolor="none"))
        axc.text(x+0.21, y-0.045, label, transform=axc.transAxes, ha="center", va="center")

    axd = fig.add_subplot(gs[1, 4:]); panel(axd, "d")
    matrix = np.array([[1,1,1,0,0], [1,1,1,0,0], [1,1,1,0,0], [0,0,0,0,0]])
    cmap = matplotlib.colors.ListedColormap([C["pale"], C["teal"]])
    axd.imshow(matrix, cmap=cmap, vmin=0, vmax=1, aspect="auto")
    axd.set_xticks(range(5), ["Public 1", "Public 2", "Public 3", "Private 1", "Private 2"], rotation=35, ha="right")
    axd.set_yticks(range(4), ["Base", "Wave-2", "Wave-3", "Wave-4"])
    for j in range(3):
        axd.add_patch(Rectangle((j-0.47, 3-0.47), 0.94, 0.94, fill=False,
                                edgecolor=C["gold"], lw=1.2, linestyle="--"))
    axd.text(1, 3, "design", ha="center", va="center", fontsize=6, color=C["gold"])
    axd.set_title("Mechanism × world construction", pad=4)
    axd.tick_params(length=0)
    for spine in axd.spines.values(): spine.set_visible(False)
    fig.suptitle("CityIntent evaluates evidence-grounded intention execution", fontsize=10, y=0.99)
    fig.subplots_adjust(left=0.05, right=0.98, bottom=0.08, top=0.94)
    save(fig, "fig1_benchmark_architecture")


def figure2(traces):
    traces[["world", "scenario_id", "construct", "model", "policy",
            "task_completion", "trace_feasibility", "intention_consistency",
            "full_task"]].to_csv(SOURCE / "fig2_wave3_system_item_metrics.csv", index=False)
    fig = plt.figure(figsize=(7.2, 6.2))
    gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1.12], hspace=0.42, wspace=0.38)
    system_order = [f"{m} · {p}" for m in MODEL_ORDER for p in POLICY_ORDER]
    traces["system"] = traces["model"] + " · " + traces["policy"]
    colors = [C["blue_soft"], C["blue"], C["rose_soft"], C["rose"], C["teal_soft"], C["teal"]]

    ax = fig.add_subplot(gs[0, 0]); panel(ax, "a")
    stats = []
    for i, system in enumerate(system_order):
        values = traces.loc[traces.system == system, "task_completion"]
        mean, lo, hi = bootstrap_ci(values, seed=20260806+i)
        stats.append((system, mean, lo, hi))
    y = np.arange(len(stats))[::-1]
    for yi, (_, mean, lo, hi), color in zip(y, stats, colors):
        ax.plot([lo, hi], [yi, yi], color=color, lw=1.8)
        ax.scatter(mean, yi, s=25, color=color, edgecolor=C["dark"], linewidth=0.4, zorder=3)
    ax.set_yticks(y, [s[0] for s in stats]); ax.set_xlim(0, 1)
    ax.set_xlabel("Task completion (mean, bootstrap 95% CI)")
    ax.set_title("Six-system benchmark")

    axb = fig.add_subplot(gs[0, 1]); panel(axb, "b")
    pivot = traces.pivot_table(index="system", columns="construct", values="task_completion", aggfunc="mean")
    pivot = pivot.reindex(index=system_order, columns=CONSTRUCT_ORDER)
    im = axb.imshow(pivot.values, vmin=0, vmax=1, cmap="Blues", aspect="auto")
    axb.set_yticks(range(6), system_order); axb.set_xticks(range(8), CONSTRUCT_SHORT, rotation=40, ha="right")
    for i in range(6):
        for j in range(8):
            axb.text(j, i, f"{pivot.iloc[i,j]:.2f}", ha="center", va="center", fontsize=5.4,
                     color="white" if pivot.iloc[i,j] > 0.58 else C["dark"])
    cb = fig.colorbar(im, ax=axb, fraction=0.045, pad=0.02); cb.set_label("Mean task completion")
    axb.set_title("Capability profile by construct")
    for spine in axb.spines.values(): spine.set_visible(False)

    axc = fig.add_subplot(gs[1, 0]); panel(axc, "c")
    deltas = []
    for model in MODEL_ORDER:
        p = traces[traces.model == model].pivot_table(index="scenario_id", columns="policy", values="task_completion")
        vals = (p["ReAct"] - p["PlanExec"]).dropna().values
        deltas.append(vals)
    parts = axc.violinplot(deltas, positions=np.arange(3), showextrema=False, widths=0.7)
    for body, color in zip(parts["bodies"], [C["blue"], C["rose"], C["teal"]]):
        body.set_facecolor(color); body.set_edgecolor(C["dark"]); body.set_alpha(0.45)
    rng = np.random.default_rng(11)
    for i, vals in enumerate(deltas):
        axc.scatter(i+rng.normal(0,0.045,len(vals)), vals, s=9, alpha=0.55,
                    color=[C["blue"], C["rose"], C["teal"]][i], edgecolor="none")
        axc.scatter(i, np.mean(vals), marker="D", s=28, color=C["dark"], zorder=4)
    axc.axhline(0, color=C["grey"], lw=0.8, linestyle="--")
    axc.set_xticks(range(3), MODEL_ORDER); axc.set_ylabel("ReAct − PlanExec task completion")
    axc.set_title("Paired policy effect (n = 24 items/model)")

    axd = fig.add_subplot(gs[1, 1]); panel(axd, "d")
    metrics = ["task_completion", "trace_feasibility", "intention_consistency", "full_task"]
    labels = ["Task", "Feasibility", "Intention", "Full task"]
    for i, system in enumerate(system_order):
        means = traces.loc[traces.system == system, metrics].mean().values
        x = np.arange(len(metrics)) + (i-2.5)*0.055
        axd.plot(x, means, marker="o", ms=3, lw=0.8, color=colors[i], label=system)
    axd.set_xticks(range(4), labels); axd.set_ylim(0,1.03); axd.set_ylabel("Mean score")
    axd.set_title("Outcome and execution quality")
    axd.legend(ncol=2, loc="lower left", fontsize=5.5)
    fig.suptitle("Model and policy effects on Wave-3 public items", fontsize=10, y=0.99)
    fig.subplots_adjust(left=0.10, right=0.97, bottom=0.10, top=0.93)
    save(fig, "fig2_model_policy_benchmark")


def load_analysis(path, wave, world):
    rows = read_json(path)["item_analysis"]
    out = pd.DataFrame(rows)
    out["wave"] = wave; out["world"] = world
    return out


def figure3():
    specs = []
    base_paths = [
        "native_time_v7_public_v0_analysis_48_2026-08-04",
        "native_time_v7_public_v1_analysis_48_2026-08-04",
        "native_time_v7_public_v2_analysis_48_2026-08-04",
    ]
    wave2_paths = [
        "native_wave2_public_v0_hardened2_analysis_48_2026-08-04",
        "native_wave2_public_v1_hardened5_rescore_analysis_48_2026-08-05",
        "native_wave2_public_v2_hardened4_rescore_analysis_48_2026-08-05",
    ]
    wave3_paths = [f"native_wave3_public_v{i}_final_analysis_48_2026-08-06" for i in range(3)]
    for wave, paths in [("Base",base_paths),("Wave-2",wave2_paths),("Wave-3",wave3_paths)]:
        for i, name in enumerate(paths):
            specs.append(load_analysis(ROOT/"results/cityintent_v1_1_candidate"/name/"analysis.json", wave, f"v{i}"))
    data = pd.concat(specs, ignore_index=True)
    data.to_csv(SOURCE / "fig3_item_quality_across_waves.csv", index=False)
    fig = plt.figure(figsize=(7.2, 6.0)); gs = gridspec.GridSpec(2,2,hspace=0.42,wspace=0.35)

    ax = fig.add_subplot(gs[0,0]); panel(ax,"a")
    wave_order=["Base","Wave-2","Wave-3"]
    vals=[data.loc[data.wave==w,"mean_task"].values for w in wave_order]
    bp=ax.boxplot(vals,positions=range(3),widths=.55,patch_artist=True,showfliers=False)
    for box,color in zip(bp["boxes"],[C["blue_soft"],C["rose_soft"],C["teal_soft"]]): box.set_facecolor(color)
    for i,v in enumerate(vals): ax.scatter(np.full(len(v),i)+np.linspace(-.14,.14,len(v)),v,s=9,color=C["dark"],alpha=.45)
    ax.set_xticks([0,1,2,3],["Base","Wave-2","Wave-3","Wave-4"])
    ax.add_patch(Rectangle((2.72,0.02),.56,.94,fill=False,edgecolor=C["gold"],linestyle="--",lw=1))
    ax.text(3,.5,"data\npending",ha="center",va="center",color=C["gold"])
    ax.set_ylim(0,1); ax.set_ylabel("Item mean task completion"); ax.set_title("Mechanism-wave difficulty")

    axb=fig.add_subplot(gs[0,1]); panel(axb,"b")
    mat=data.pivot_table(index="wave",columns="world",values="mean_task",aggfunc="mean").reindex(index=wave_order,columns=["v0","v1","v2"])
    mat=np.vstack([mat.values,np.full(3,np.nan)])
    cmap=plt.get_cmap("BuPu").copy(); cmap.set_bad(C["pale"])
    im=axb.imshow(mat,vmin=.35,vmax=.75,cmap=cmap,aspect="auto")
    axb.set_yticks(range(4),["Base","Wave-2","Wave-3","Wave-4"]); axb.set_xticks(range(3),["Dense grid","Radial","Polycentric"])
    for i in range(3):
        for j in range(3): axb.text(j,i,f"{mat[i,j]:.2f}",ha="center",va="center",fontsize=6,color="white" if mat[i,j]>.58 else C["dark"])
    for j in range(3): axb.text(j,3,"pending",ha="center",va="center",fontsize=6,color=C["grey"])
    fig.colorbar(im,ax=axb,fraction=.045,pad=.02,label="Mean task completion")
    axb.set_title("Mechanism × city topology")
    for spine in axb.spines.values(): spine.set_visible(False)

    axc=fig.add_subplot(gs[1,0]); panel(axc,"c")
    w3=data[data.wave=="Wave-3"]
    world_colors={"v0":C["blue"],"v1":C["rose"],"v2":C["teal"]}
    for world,g in w3.groupby("world"):
        axc.scatter(g.mean_task,g.corrected_item_total_correlation,s=28,color=world_colors[world],label=world,alpha=.8,edgecolor=C["dark"],linewidth=.35)
    axc.axvspan(.2,.9,color=C["teal_soft"],alpha=.2); axc.axhline(.2,color=C["red"],lw=.8,linestyle="--")
    axc.axvline(.2,color=C["grey"],lw=.6,linestyle=":"); axc.axvline(.9,color=C["grey"],lw=.6,linestyle=":")
    axc.set_xlim(0,1); axc.set_ylim(0,1.05); axc.set_xlabel("Item mean task completion"); axc.set_ylabel("Corrected item–total r")
    axc.set_title("Wave-3 item quality gate"); axc.legend(title="World",ncol=3,loc="lower center")

    axd=fig.add_subplot(gs[1,1]); panel(axd,"d")
    stages=["Generated","Oracle +\nnegative","Six-system\ncoverage","Promoted"]
    counts=[24,24,24,24]
    axd.plot(range(4),counts,color=C["teal"],lw=2,marker="o",ms=6)
    for i,v in enumerate(counts): axd.text(i,v+.7,str(v),ha="center",fontweight="bold")
    axd.set_xticks(range(4),stages); axd.set_ylim(0,28); axd.set_ylabel("Wave-3 public items")
    axd.set_title("Cross-world promotion funnel")
    fig.suptitle("Mechanism diversity and cross-world validity",fontsize=10,y=.99)
    fig.subplots_adjust(left=.09,right=.97,bottom=.10,top=.92)
    save(fig,"fig3_mechanism_world_validity")


def time_minutes(value):
    h,m=map(int,value.split(":")); return h*60+m


def figure4(traces):
    target_constructs=["disruption_recovery","resource_budget_allocation","social_coordination_copresence"]
    titles=["Route disruption","Event-revealed reservation","Updated social co-presence"]
    action_color={"move":C["blue"],"enter":C["blue_soft"],"dwell":C["gold"],"message":C["rose"],
                  "interact":C["red"],"buy":C["teal"],"use_service":C["green"],"recall":C["grey"],"finish":C["dark"]}
    selected=[]
    for construct in target_constructs:
        g=traces[traces.construct==construct]
        pivot=g.pivot_table(index=["scenario_id","model"],columns="policy",values="task_completion").dropna()
        pivot["gap"]=pivot["ReAct"]-pivot["PlanExec"]
        sid,model=pivot.gap.idxmax()
        for policy in ["PlanExec","ReAct"]:
            selected.append(g[(g.scenario_id==sid)&(g.model==model)&(g.policy==policy)].iloc[0])
    pd.DataFrame([{k:r[k] for k in ["scenario_id","construct","model","policy","task_completion","trace_feasibility"]} for r in selected]).to_csv(SOURCE/"fig4_selected_trace_pairs.csv",index=False)
    fig,axes=plt.subplots(3,1,figsize=(7.2,5.9),sharex=False)
    for idx,(ax,title) in enumerate(zip(axes,titles)):
        panel(ax,chr(97+idx)); pair=selected[idx*2:idx*2+2]
        all_times=[]
        for lane,row in enumerate(pair):
            y=lane
            for record in row["trace"]:
                t=time_minutes(record["start_time"])
                kind=record["action"]["kind"]
                if kind not in action_color: continue
                all_times.append(t)
                ax.scatter(t,y,s=28,color=action_color[kind],marker="o" if lane else "s",edgecolor=C["dark"],linewidth=.35,zorder=3)
            ax.text(1.005,y,f"task={row['task_completion']:.2f}",transform=ax.get_yaxis_transform(),va="center",fontsize=6.5)
        scenario=read_json(ROOT/"benchmarks/cityintent_v0/v1_1/native_pilot/expansion_wave3/scenarios"/f"{pair[0]['scenario_id']}.json")
        for event_index, event in enumerate(scenario.get("events",[])):
            et=time_minutes(event["time"]); ax.axvline(et,color=C["red"],lw=1,linestyle="--")
            event_label = {
                "route_closure": "route closure",
                "reservation_price_update": "reservation update",
                "meeting_relocation": "venue update",
                "confirmation_deadline": "confirmation deadline",
            }.get(event["type"], event["type"].replace("_", " "))
            ax.text(et,1.19 + 0.12*(event_index % 2),event_label,
                    ha="right" if event_index % 2 == 0 else "left",
                    va="bottom",fontsize=5.3,color=C["red"])
        ax.set_yticks([0,1],[f"{pair[0]['model']} PlanExec",f"{pair[1]['model']} ReAct"])
        lo=min(all_times)-3; hi=max(all_times)+5; ax.set_xlim(lo,hi)
        ticks=np.linspace(lo,hi,5,dtype=int); ax.set_xticks(ticks,[f"{t//60:02d}:{t%60:02d}" for t in ticks])
        ax.set_title(title,loc="left",pad=4); ax.set_xlabel("Episode time")
        ax.grid(axis="x",color=C["light"],lw=.5)
    handles=[plt.Line2D([0],[0],marker="o",color="none",markerfacecolor=color,markeredgecolor=C["dark"],markersize=5,label=kind.replace("_"," ")) for kind,color in action_color.items()]
    fig.legend(handles=handles,ncol=5,loc="upper center",bbox_to_anchor=(.53,.94),fontsize=5.8)
    fig.suptitle("Dynamic updates expose stale commitments in execution traces",fontsize=10,y=.995)
    fig.subplots_adjust(left=.19,right=.91,bottom=.08,top=.84,hspace=.70)
    save(fig,"fig4_dynamic_adaptation_traces")


def figure5():
    report=read_json(ROOT/"benchmarks/cityintent_v0/v1_1/native_pilot/expansion_wave3/acceptance_report.json")
    oracle=pd.DataFrame(report["results"])
    analyses=[]
    for world in range(3):
        a=read_json(ROOT/f"results/cityintent_v1_1_candidate/native_wave3_public_v{world}_final_analysis_48_2026-08-06/analysis.json")
        d=pd.DataFrame(a["item_analysis"]); d["world"]=f"v{world}"; analyses.append(d)
    items=pd.concat(analyses,ignore_index=True)
    oracle.to_csv(SOURCE/"fig5_oracle_negative_results.csv",index=False)
    items.to_csv(SOURCE/"fig5_item_quality.csv",index=False)
    fig=plt.figure(figsize=(7.2,5.6)); gs=gridspec.GridSpec(2,2,hspace=.38,wspace=.35)
    ax=fig.add_subplot(gs[0,0]); panel(ax,"a")
    x=np.arange(len(oracle)); ax.scatter(x,oracle.oracle_task_completion,s=16,color=C["teal"],label="Oracle")
    ax.scatter(x,oracle.negative_task_completion,s=16,color=C["rose"],label="Matched negative")
    ax.vlines(x,oracle.negative_task_completion,oracle.oracle_task_completion,color=C["light"],lw=.7,zorder=0)
    ax.set_ylim(-.03,1.05); ax.set_xlabel("Wave-3 item"); ax.set_ylabel("Task completion"); ax.set_title("Oracle–negative separation")
    ax.legend(loc="lower right")

    axb=fig.add_subplot(gs[0,1]); panel(axb,"b")
    metrics=["mean_task","range","corrected_item_total_correlation"]
    labels=["Difficulty\n(mean)","System\nrange","Corrected\nitem–total r"]
    vals=[items[m].values for m in metrics]
    bp=axb.boxplot(vals,patch_artist=True,widths=.55,showfliers=False)
    for box,color in zip(bp["boxes"],[C["blue_soft"],C["teal_soft"],C["rose_soft"]]): box.set_facecolor(color)
    for i,v in enumerate(vals): axb.scatter(np.full(len(v),i+1)+np.linspace(-.13,.13,len(v)),v,s=8,color=C["dark"],alpha=.4)
    axb.axhline(.2,color=C["red"],lw=.7,linestyle="--"); axb.set_xticks([1,2,3],labels); axb.set_ylim(0,1.05)
    axb.set_ylabel("Score"); axb.set_title("Empirical item quality")

    axc=fig.add_subplot(gs[1,0]); panel(axc,"c")
    placeholder(axc,"Human scoring agreement",["Target: n = 72 stratified traces","2 independent annotators","Exact agreement · Cohen’s κ · evidence sufficiency"])
    axd=fig.add_subplot(gs[1,1]); panel(axd,"d")
    placeholder(axd,"Public–private generalization",["Target: 48 private-test scenarios","Public/private rank correlation","Generalization gap by construct"])
    fig.suptitle("Current validity evidence and preregistered release gates",fontsize=10,y=.99)
    fig.subplots_adjust(left=.09,right=.97,bottom=.08,top=.91)
    save(fig,"fig5_benchmark_validity")


def main():
    traces=load_wave3_traces()
    assert len(traces)==144 and traces.scenario_id.nunique()==24
    figure1(); figure2(traces.copy()); figure3(); figure4(traces); figure5()
    print(json.dumps({"figures":5,"wave3_traces":len(traces),"output":str(OUT)},ensure_ascii=False))


if __name__ == "__main__":
    main()
