#!/usr/bin/env python3
"""
SpatialAgent Paper Downloader
Downloads the curated paper set described in docs/references/paperrefence.md.
"""

import os
import time
import urllib.request
import urllib.error
import re
from pathlib import Path

# ── Output root ──────────────────────────────────────────────────────────────
REPO_ROOT = Path(__file__).resolve().parent.parent
BASE_DIR = REPO_ROOT / "assets" / "papers" / "pdfs"
REPORT_DIR = REPO_ROOT / "assets" / "papers" / "generated"

# ── Paper catalogue ──────────────────────────────────────────────────────────
# Each entry: (filename_stem, primary_url, fallback_url_or_None)
# arxiv abs  →  pdf  auto-converted in resolve_url()
PAPERS = {

    # ── Category 1: LLM-based game agents ────────────────────────────────────
    "01_LLM_Game_Agents": [
        (
            "01_Generative_Agents_Park2023",
            "https://arxiv.org/abs/2304.03442",
            None,
        ),
        (
            "02_Survey_LLM_Game_Agents_Hu2024",
            "https://arxiv.org/abs/2404.02039",
            None,
        ),
        (
            "03_Affordable_Generative_Agents_Yu2024",
            "https://arxiv.org/abs/2402.02053",
            None,
        ),
        (
            "04_Project_Sid_Altera2024",
            "https://arxiv.org/abs/2411.00114",
            None,
        ),
        (
            "05_LIGS_Emergent_Narrative_Jeong2025",
            "https://arxiv.org/abs/2503.04999",   # CHI EA 2025 preprint
            None,
        ),
        (
            "06_MultiAgentBench_Zhu2025",
            "https://arxiv.org/abs/2503.01935",
            None,
        ),
        (
            "07_Artificial_Leviathan_Dai2024",
            "https://arxiv.org/abs/2406.14373",
            None,
        ),
    ],

    # ── Category 2: Space Syntax ──────────────────────────────────────────────
    "02_Space_Syntax": [
        (
            "01_Social_Logic_of_Space_Hillier1984",
            "https://www.cambridge.org/core/books/social-logic-of-space/6B0A078C79A74F0CC615ACD8B250A985",
            None,   # book – will fail gracefully
        ),
        (
            "02_Space_is_the_Machine_Hillier1996",
            "https://patterns.architexturez.net/system/files/SITM.pdf",
            "https://spaceisthemachine.com/",
        ),
        (
            "03_Isovists_to_Visibility_Graphs_Turner2001",
            "http://discovery.ucl.ac.uk/160/1/turner-doxa-osullivan-penn-2001.pdf",
            "https://doi.org/10.1068/b2684",
        ),
        (
            "04_Space_Syntax_Agent_Simulation_Penn2001",
            "https://discovery.ucl.ac.uk/2027/1/penn.pdf",
            "https://www.academia.edu/276347/Space_Syntax_Based_Agent_Simulation",
        ),
        (
            "05_Space_Syntax_Methodology_AlSayed2014",
            "https://www.researchgate.net/publication/295855785_Space_Syntax_methodology",
            None,
        ),
        (
            "06_Agent_Based_Urban_Spaces_Esposito2020",
            "https://www.mdpi.com/2071-1050/12/11/4625/pdf",
            "https://www.mdpi.com/2071-1050/12/11/4625",
        ),
        (
            "07_Computational_Analytical_Methods_Ostwald2023",
            "https://www.mdpi.com/2075-5309/13/7/1613/pdf",
            "https://www.mdpi.com/2075-5309/13/7/1613",
        ),
        (
            "08_Pedestrian_Volume_Models_Wolpert2024",
            "https://www.sciencedirect.com/science/article/abs/pii/S0198971524001674",
            None,
        ),
        (
            "09_Spatial_Visual_Perception_Streets_2025",
            "https://www.nature.com/articles/s41598-025-03189-z.pdf",
            "https://www.nature.com/articles/s41598-025-03189-z",
        ),
        (
            "10_VGA_vs_Human_Mobility_Askarizad2026",
            "https://link.springer.com/chapter/10.1007/978-3-031-97654-4_4",
            None,
        ),
    ],

    # ── Category 3: Spatially-aware LLM agents ───────────────────────────────
    "03_Spatially_Aware_LLM_Agents": [
        (
            "01_When_LLMs_Recognize_Space_Oh2025",
            "https://pubmed.ncbi.nlm.nih.gov/41052126/",
            None,
        ),
        (
            "02_SARAH_Spatially_Aware_Humans_Ng2026",
            "https://arxiv.org/abs/2602.18432",
            None,
        ),
        (
            "03_Advancing_Spatial_Reasoning_Li2024_AAAI",
            "https://arxiv.org/abs/2401.03991",
            None,
        ),
        (
            "04_SpatialVLM_Chen2024_CVPR",
            "https://arxiv.org/abs/2401.12168",
            "https://spatial-vlm.github.io/",
        ),
        (
            "05_Reframing_Spatial_Reasoning_Li2024_IJCAI",
            "https://www.ijcai.org/proceedings/2024/0701.pdf",
            None,
        ),
    ],

    # ── Category 4: NPC dialogue and behavior ─────────────────────────────────
    "04_NPC_Dialogue_Behavior": [
        (
            "01_LLM_Driven_NPCs_Song2025",
            "https://arxiv.org/abs/2504.13928",
            None,
        ),
        (
            "02_Deflanderization_Buakhaw2025",
            "https://arxiv.org/abs/2510.13586",
            None,
        ),
        (
            "03_Tricking_LLM_NPCs_Shiomi2025",
            "https://arxiv.org/abs/2508.19288",
            None,
        ),
        (
            "04_Fixed_Persona_SLMs_Braas2025",
            "https://arxiv.org/abs/2511.10277",
            None,
        ),
        (
            "05_Character_LLM_Shao2023",
            "https://arxiv.org/abs/2310.10158",
            None,
        ),
    ],

    # ── Category 5: Multi-agent social simulation ─────────────────────────────
    "05_Multi_Agent_Social_Simulation": [
        (
            "01_Language_Agents_RL_Werewolf_Xu2023",
            "https://arxiv.org/abs/2310.18940",
            None,
        ),
        (
            "02_LSPO_Werewolf_Xu2025_ICML",
            "https://arxiv.org/abs/2502.04686",
            None,
        ),
        (
            "03_ProAgent_Zhang2024_AAAI",
            "https://arxiv.org/abs/2308.11339",
            None,
        ),
        (
            "04_S3_Social_Network_Simulation_Gao2023",
            "https://arxiv.org/abs/2307.14984",
            None,
        ),
        (
            "05_SOTOPIA_Zhou2024_ICLR",
            "https://arxiv.org/abs/2310.11667",
            None,
        ),
        (
            "06_AgentSociety_Piao2025",
            "https://arxiv.org/abs/2502.08691",
            None,
        ),
    ],

    # ── Category 6: Agent memory and cognitive architecture ───────────────────
    "06_Agent_Memory_Cognitive": [
        (
            "01_AgeMem_Yu2026",
            "https://arxiv.org/abs/2601.01885",
            None,
        ),
        (
            "02_MemGPT_Packer2023",
            "https://arxiv.org/abs/2310.08560",
            None,
        ),
        (
            "03_Reflexion_Shinn2023_NeurIPS",
            "https://arxiv.org/abs/2303.11366",
            None,
        ),
        (
            "04_AMEM_Xu2025",
            "https://arxiv.org/abs/2502.12110",
            None,
        ),
        (
            "05_Vector_Navigation_Grid_Cells_Banino2018",
            "https://www.nature.com/articles/s41586-018-0102-6",
            None,
        ),
        (
            "06_Place_Grid_Cells_Memory_Moser2015",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC4315928/pdf/cshperspect-MEM-021808.pdf",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC4315928/",
        ),
        (
            "07_Non_Spatial_Place_Grid_Cells_Love2019",
            "https://www.nature.com/articles/s41467-019-13760-8.pdf",
            "https://www.nature.com/articles/s41467-019-13760-8",
        ),
    ],

    # ── Category 7: Evaluation methodology ───────────────────────────────────
    "07_Evaluation_Methodology": [
        (
            "01_GVGAI_LLM_Li2025",
            "https://arxiv.org/abs/2508.08501",
            None,
        ),
        (
            "02_LLM_as_Judge_MT_Bench_Zheng2023_NeurIPS",
            "https://arxiv.org/abs/2306.05685",
            None,
        ),
        (
            "03_Survey_LLM_as_Judge_2024",
            "https://arxiv.org/abs/2411.15594",
            None,
        ),
        (
            "04_Navigates_Like_Me_Milani2023_CHI",
            "https://dl.acm.org/doi/pdf/10.1145/3544548.3581348",
            "https://dl.acm.org/doi/fullHtml/10.1145/3544548.3581348",
        ),
        (
            "05_Turings_Test_Believable_AI_Livingstone2006",
            "https://dl.acm.org/doi/pdf/10.1145/1111293.1111303",
            "https://dl.acm.org/doi/10.1145/1111293.1111303",
        ),
        (
            "06_Assessing_Believability_Togelius2013",
            "https://link.springer.com/chapter/10.1007/978-3-642-32323-2_9",
            None,
        ),
        (
            "07_Network_Formation_LLMs_Papachristou2025",
            "https://arxiv.org/abs/2402.10659",
            None,
        ),
        (
            "08_Collective_Behaviors_LLM_Agents_2025",
            "https://www.sciencedirect.com/science/article/pii/S2543925125000154",
            None,
        ),
    ],
}

# ── Helpers ──────────────────────────────────────────────────────────────────

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept": "application/pdf,text/html,*/*",
}


def arxiv_pdf_url(url: str) -> str:
    """Convert an arxiv /abs/ URL to its /pdf/ equivalent."""
    return re.sub(r"arxiv\.org/abs/", "arxiv.org/pdf/", url)


def resolve_url(url: str) -> str:
    """Return the best direct-download URL we can derive from the given URL."""
    if "arxiv.org/abs/" in url:
        return arxiv_pdf_url(url)
    return url


def download(url: str, dest: Path) -> bool:
    """Attempt to download *url* to *dest*.  Returns True on success."""
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            content_type = resp.headers.get("Content-Type", "")
            data = resp.read()

        # Accept only PDF or reasonably sized HTML (some open-access journals)
        if "pdf" in content_type or url.endswith(".pdf"):
            dest = dest.with_suffix(".pdf")
        elif len(data) < 5_000:
            # Tiny response → likely a redirect / login page, not the paper
            return False

        dest.write_bytes(data)
        return True

    except Exception as exc:  # noqa: BLE001
        print(f"    ✗  {exc}")
        return False


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    results = {"ok": [], "fail": []}

    for category, papers in PAPERS.items():
        cat_dir = BASE_DIR / category
        cat_dir.mkdir(parents=True, exist_ok=True)
        print(f"\n{'═'*60}")
        print(f"  {category}")
        print(f"{'═'*60}")

        for stem, primary, fallback in papers:
            dest = cat_dir / stem
            print(f"\n  ▸ {stem}")

            # ── try primary URL ───────────────────────────────────────────────
            url = resolve_url(primary)
            print(f"    → {url}")
            ok = download(url, dest)

            # ── try fallback URL ──────────────────────────────────────────────
            if not ok and fallback:
                url2 = resolve_url(fallback)
                print(f"    ↳ fallback: {url2}")
                ok = download(url2, dest)

            if ok:
                print(f"    ✔  saved → {dest.name}.*")
                results["ok"].append(stem)
            else:
                print(f"    ✗  FAILED (manual download required)")
                results["fail"].append((stem, primary))

            time.sleep(1.5)  # be polite to servers

    # ── Summary ───────────────────────────────────────────────────────────────
    print(f"\n\n{'═'*60}")
    print(f"  SUMMARY")
    print(f"{'═'*60}")
    print(f"  ✔  Downloaded : {len(results['ok'])}")
    print(f"  ✗  Failed     : {len(results['fail'])}")

    if results["fail"]:
        print("\n  Papers requiring manual download:")
        for stem, url in results["fail"]:
            print(f"    • {stem}")
            print(f"      {url}")

    # Write a simple report
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    report_path = REPORT_DIR / "download_report.md"
    with open(report_path, "w") as f:
        f.write("# SpatialAgent Paper Download Report\n\n")
        f.write(f"**Downloaded:** {len(results['ok'])} papers  \n")
        f.write(f"**Failed:** {len(results['fail'])} papers  \n\n")
        if results["fail"]:
            f.write("## Papers Requiring Manual Download\n\n")
            for stem, url in results["fail"]:
                f.write(f"- **{stem}**  \n  URL: <{url}>\n\n")
    print(f"\n  Report saved to: {report_path}")


if __name__ == "__main__":
    main()
