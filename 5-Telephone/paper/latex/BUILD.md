# Building the LaTeX paper

## Requirements
pdflatex + bibtex (TeX Live). The AAAI 2027 style (`aaai2027.sty`) does
`\RequirePackage{newtxtext}`, which is **not** in the TeX Live "basic" scheme. If the system
TeX tree is not writable (no admin), install the missing packages into the **user tree** via
`tlmgr` user-mode — no admin required.

## One-time dependency install (user-mode, no admin)
```bash
tlmgr init-usertree                                           # once, if ~/Library/texmf not set up
tlmgr --usermode install newtx tex-gyre kastrup placeins xstring
```
These land in `$TEXMFHOME` (e.g. `~/Library/texmf`) and are picked up automatically by pdflatex.

## Build
```bash
./build.sh      # pdflatex -> bibtex -> pdflatex x2  ->  main.pdf
```

## Why each dependency
- **newtx** — the Times-like text font `aaai2027.sty` requires (this was the original blocker).
- **tex-gyre** — provides the `qtm*` (TeX Gyre Termes) fonts newtx maps onto; without it the
  build fails with a missing `ts1-qtmr` TFM.
- **kastrup** — provides `binhex.tex` (number/font macros pulled in transitively).
- **placeins**, **xstring** — small package dependencies of the template / newtx.

## Status
The block recorded earlier ("blocked by newtx, no admin") is resolved by the user-mode install
above. `build.sh` produces a 10-page AAAI PDF. NOTE: `main.tex` currently holds the older
diagnosis+PROV draft; the up-to-date content (incl. the APM architecture arc and the new
`fig_*.png`) lives in `../draft_v1.md` and still needs to be migrated into `main.tex`.
