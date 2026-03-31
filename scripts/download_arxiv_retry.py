import urllib.request, time, shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEST_DIR = REPO_ROOT / "spatial-agent" / "references" / "pdfs"

papers = {
    "04_NPC_Dialogue_Behavior/05_Character_LLM_Shao2023.pdf": "https://export.arxiv.org/pdf/2310.10158",
    "07_Evaluation_Methodology/01_GVGAI_LLM_Li2025.pdf": "https://export.arxiv.org/pdf/2508.08501",
    "07_Evaluation_Methodology/03_Survey_LLM_as_Judge_2024.pdf": "https://export.arxiv.org/pdf/2411.15594",
    "07_Evaluation_Methodology/07_Network_Formation_LLMs_Papachristou2025.pdf": "https://export.arxiv.org/pdf/2402.10659",
    "04_NPC_Dialogue_Behavior/01_LLM_Driven_NPCs_Song2025.pdf": "https://export.arxiv.org/pdf/2504.13928",
    "04_NPC_Dialogue_Behavior/02_Deflanderization_Buakhaw2025.pdf": "https://export.arxiv.org/pdf/2510.13586",
    "04_NPC_Dialogue_Behavior/04_Fixed_Persona_SLMs_Braas2025.pdf": "https://export.arxiv.org/pdf/2511.10277",
}

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

print("Retrying arXiv via export.arxiv.org...")
for rel_path, url in papers.items():
    dest = DEST_DIR / rel_path
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 100000:
        continue # Already downloaded properly
        
    print(f"Downloading {rel_path}...")
    success = False
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=120) as r, open(dest, 'wb') as f:
                shutil.copyfileobj(r, f)
            if dest.stat().st_size > 50000:
                print(f" ✔ Success: {dest.name}")
                success = True
                break
        except Exception as e:
            print(f" ✗ Attempt {attempt+1} failed: {e}")
        time.sleep(2)
    if not success:
        print(f" ✗ Failed completely: {rel_path}")

