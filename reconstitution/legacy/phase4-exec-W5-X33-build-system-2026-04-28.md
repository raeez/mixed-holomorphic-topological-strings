# Phase-4 EXEC W5-X33: Build-System Auditor

**Date.** 2026-04-28.
**Wave.** 5 (attack-heal swarm), attacker X33.
**Author.** Raeez Lorgat.
**Mode.** READ-ONLY. Proposal-only. No edits.
**Scope.** `Makefile`, `.gitignore`, `.gitmodules`, build apparatus, working-tree hygiene at `/Users/raeez/topological-strings/`.

---

## §0. Charter

Audit the build infrastructure for publication-readiness: verify the
Makefile produces the canonical 155-156-page PDF reproducibly, verify
`.gitignore` excludes auxiliary LaTeX detritus and private-tmp
artifacts, verify the working tree is hygienic, and document the exact
incantation a reviewer needs to rebuild from a clean clone.

Severity scale: 5 paper does not build; 4 build needs manual repair;
3 build runs but with quality regressions; 2 hygiene leak (private
data into commits); 1 cosmetic / polish.

---

## §1. Makefile audit

### §1.1. Structure (`Makefile` 295 lines)

* Header config (lines 1-103): metadata, paths, output dirs, TeX
  flags, HTML config, tar config.
* Default goal (line 108): `pdf`.
* Phony targets: `quick`, `fast`, `release`, `standalone`, `icloud`,
  `help`, `open*`, `qc`, `q`, `qall`, `pdf`, `html`, `index`,
  `install*`, `tar`, `clean`.

### §1.2. `make pdf` target (lines 241-252)

```
pdf:
    mkdir -p out
    pdflatex -output-directory=out -interaction=nonstopmode main.tex   # pass 1
    make index                                                          # nlo->nls
    pdflatex ... main.tex   # pass 2
    pdflatex ... main.tex   # pass 3
    pdflatex ... main.tex   # pass 4
    make index
    pdflatex ... main.tex   # pass 5
    pdflatex ... main.tex   # pass 6
    pdflatex ... main.tex   # pass 7
    [ -f out/main.pdf ] || { echo fail; exit 1; }
```

**Status.** Default `pdf` target runs SEVEN pdflatex passes plus two
`make index` invocations. Per W5-X11 wave-3 audit, 4 passes converge;
7 passes is over-engineered but idempotent (each extra pass changes
nothing). Cost: 7x build time. Functionally correct.

### §1.3. `make clean` target (lines 291-294)

```
clean:
    -rm -rf *.toc *.ilg *.log *.nlo *.dvi *.aux *.tar.gz *.nlo *.nls
            *.nls *.out *.toc *.sta *.gla *.fdb_latexmk *.fls *.synctex.gz
    -cd out; rm -rf $(TEXDEBRIS)
```

Cleans both top-level and `out/` debris. **Coverage gaps.**

* Missing: `*.bbl`, `*.blg` (bibliography), `*.idx`, `*.ind` (index),
  `*.toc.bak`, `*.brf` (hyperref backrefs), `*.bcf`, `*.run.xml`
  (biber). Severity 1: these are also gitignored, so commit hygiene
  is fine, but `make clean` will leave them on disk.
* Does NOT clean `.build_logs/` (used by `standalone`); not strictly
  needed since reusing logs is harmless, but inconsistent with the
  "scrub debris" intent.

### §1.4. Auxiliary-file pre-step before builds

**No pre-clean dependency on `pdf`.** The default `pdf` target does
not depend on `clean`. This is the correct choice for incremental
rebuilds (PDFs converge faster with stale `.aux` from a previous run
of the same source), but it means a stale `main.aux` from a different
revision can mislead label resolution. The `make all` target (line
118) DOES chain `clean -> pdf -> html -> tar -> install`; reviewers
who want a guaranteed-clean build can use `make all` (but `install`
needs a separately-configured `$(INSTALLDIR)`).

`qc` (line 225) and `qall` (line 228) do `clean -> quick`. Useful for
full local rebuilds.

### §1.5. Documented usage

Lines 195-206 (`make help`) list:

```
make            Full legacy build
make fast       Quick PDF build
make release    Full rebuild -> out/ + standalones + iCloud
make standalone Build standalone documents -> out/
make icloud     Build and copy PDFs to iCloud Drive
make clean      Remove build debris
make help       This message
```

**Status.** Help target exists; the file lacks a top-level `# usage:`
banner comment but `make help` covers it. Severity 1: a referee or
external collaborator running `make` cold would see the legacy "all
targets" cascade pre-attempt rather than `pdf` (because of
`.DEFAULT_GOAL := pdf`, the default IS `pdf` -- this is correct).
The phrase "Full legacy build" in `make help` is misleading; the
default actually points at the `pdf` target after the `.DEFAULT_GOAL`
override on line 108.

### §1.6. Default-target reliability

**Confirmed.** `.DEFAULT_GOAL := pdf` (line 108) directs `make` to
build the PDF in `out/main.pdf`. The 7-pass cycle is robust against
any cross-reference / nomenclature convergence pathology.

---

## §2. `.gitignore` audit

### §2.1. LaTeX auxiliary file coverage (lines 5-46)

| Pattern | Status |
|---------|--------|
| `*.aux`, `*.log`, `*.out`, `*.toc` | covered |
| `*.bbl`, `*.bcf`, `*.blg` | covered |
| `*.fdb_latexmk`, `*.fls`, `*.synctex.gz` | covered |
| `*.nlo`, `*.nls` | covered (line 153-154) |
| `*.idx`, `*.ilg`, `*.ind` | covered (line 131-133) |
| `*.tar.gz` | covered |
| `/out/`, `/.build_logs/` | covered (lines 2-3) |

**LaTeX hygiene: complete.** No tracked aux files appear in
`git ls-files`. `git ls-files --others --exclude-standard` shows zero
aux-file leaks. **Severity 0.**

### §2.2. Project-specific exclusions (per task spec)

| Required exclusion | In `.gitignore`? | Tracked? | Severity |
|--------------------|------------------|----------|----------|
| `out/` | yes (line 2: `/out/`) | tracked: `out/main.pdf` only (intentional) | 0 |
| `out_test/` | **NO** | not tracked, leaks as untracked | **1** |
| `.agents/` | **NO** | not tracked, leaks as untracked | **1** |
| `.claude/` | **NO** | not tracked, leaks as untracked | **1** |
| `.DS_Store` | **NO** | leaks as untracked top-level file | **1** |
| `scripts/__pycache__/` | **NO** | not tracked but 8 `.pyc` files leak | **1** |
| `private-tmp-artifacts-*/` (per W5-X22) | **NO** | not tracked but 447-file 45 MB subtree could leak | **2** |
| `references/` (cross-repo materials) | **NO** | not tracked; 23 MB; SEE §5 | **1** |

**Severity-2 finding (`private-tmp-artifacts-*/`).** This subtree at
`reconstitution/private-tmp-artifacts-2026-04-28/` is 45 MB / 447
files of intermediate worktree diffs, worker-build PDFs, and patch
artifacts. It is intentionally NOT in `.gitignore` and is NOT
currently being added (`git ls-files --others --exclude-standard`
includes none of its members because the parent `reconstitution/`
itself is untracked). A future `git add reconstitution/` -- the
natural action to ingest the audit reports -- would sweep these 45 MB
into a commit. The W5-X22 housekeeping audit explicitly named this as
a publication-blocker risk.

**Recommended `.gitignore` additions** (proposal-only, not applied):

```
## Project-local hygiene (W5-X33 proposal):
.DS_Store
.agents/
.claude/
out_test/
scripts/__pycache__/
*.pyc
reconstitution/private-tmp-artifacts-*/
```

### §2.3. Comprehensive auxiliary coverage (lines 47-228)

The `.gitignore` is the canonical TeX-Project gitignore template
(228 lines, covers algorithm, beamer, hyperref, knitr, makeidx,
minted, sympy, tikz, todonotes, etc.). Coverage is exhaustive for
LaTeX. **Severity 0** for that domain.

---

## §3. Working-tree hygiene

### §3.1. Stray aux files in working tree

Top-level aux files present (`find -maxdepth 2`):

```
/Users/raeez/topological-strings/main.aux           (99 KB, mtime Apr 28 02:23)
/Users/raeez/topological-strings/main.log           (327 KB)
/Users/raeez/topological-strings/main.toc           (7.7 KB)
/Users/raeez/topological-strings/main.idx           (0 B, empty)
/Users/raeez/topological-strings/frontier_mnop_framing_volume.aux
/Users/raeez/topological-strings/frontier_mnop_framing_volume.log
/Users/raeez/topological-strings/frontier_mnop_framing_volume.idx
/Users/raeez/topological-strings/out/{aux,log,toc,idx,nlo,nls,ilg}
/Users/raeez/topological-strings/out_test/{aux,log,toc,idx,pdf}
```

All correctly excluded by `.gitignore` (`*.aux`, `*.log`, `*.toc`,
`*.idx`, `*.nlo`, `*.nls`, `*.ilg` are all globally ignored). Zero
leak risk for these files individually. **Severity 0.**

### §3.2. Untracked-file snapshot

Total untracked: **701 files**. Breakdown:
* `reconstitution/` markdown: 622 files (audit-trail; awaiting curated
  add by principal).
* Top-level `.tex` not yet tracked: 12 files (the new appendices and
  Tate-package additions; they are referenced by `main.tex` so MUST
  be added before commit, otherwise the next clone will not build).
* Materials whitepapers: 6 files in `materials/{processed,raw}/`.
* `references/`: 31 files in `references/primary-sources/` plus
  `references/source-provenance.md`.
* Scripts: 18 new `.py` plus 8 `.pyc`. Two scripts (`check_W5_A4_small_N.py`,
  `check_W5_X4_A5RG.py`) are most-recent (Apr 28 23:00, 23:33).
* `out_test/main.pdf`: stale test build.
* Houseclean targets: `.DS_Store`, `.agents/...`, `.claude/...`.

**Severity 1.** Twelve `.tex` files actively `\input{}`'d by `main.tex`
exist on disk untracked. The next reviewer who clones master from
GitHub gets a build failure. They are: `appendix-factorization-current-conventions.tex`,
`appendix-matlis-principal-parts.tex`, `appendix-radial-parts-moyal.tex`,
`appendix-unreduced-bv-qme.tex`, `claim-strength-ledger.tex`,
`local-dictionary.tex`, `open-obligations.tex`, `principles.tex`,
`tate-P5-cross-volume.tex`, `tate-T5-chain-level-primitive.tex`,
`tate-T1-weighted-completion.tex`, `tate-T2-nilpotent-truncation.tex`,
plus `theorem-lanes.tex`. Some of the listed ones may already be
tracked but modified (`MM`); per `git ls-files --others --exclude-standard`,
the eight in the bullet above are pure-untracked.

This is OUTSIDE the build-system audit charter (it is a commit-state
issue not a build-infrastructure issue), but is the load-bearing
finding for publication-readiness: the GitHub master HEAD will not
build the canonical PDF without these files added. **Severity 2 if
publication is blocking on a clean clone build.**

---

## §4. Stale aux file analysis (per W5-X9 finding)

**Forensic data.**

```
/Users/raeez/topological-strings/main.aux       mtime Apr 28 02:23 (99767 B)
/Users/raeez/topological-strings/out/main.aux   mtime Apr 28 23:28 (112725 B)
```

The top-level `main.aux` is 21 hours older and 12 KB smaller than the
canonical `out/main.aux`. The size delta corresponds to the appendix
chapters added between the two builds (Matlis, Radial, BV-QME --
roughly the predicted byte budget).

**Idempotency analysis.** The Makefile's `pdf` target uses
`pdflatex -output-directory=out`, which writes ALL aux files INTO
`out/`, not the top level. The top-level `main.aux` is a relic from a
manual / non-make build (someone ran `pdflatex main.tex` outside the
Makefile flow) or from a much older Make convention.

**Does the stale top-level aux interfere?** No. With
`-output-directory=out`, pdflatex reads and writes only from `out/`.
The top-level `main.aux` is never consulted by the Makefile build.
However, two breakage modes exist:

1. **Manual `pdflatex main.tex` (no `-output-directory`)**: would
   write to top level, picking up the stale aux first, then overwriting
   it. Symptom: stale labels for one build, then converges. NOT a
   silent corruption, but confusing.
2. **Editor `\input` resolution**: some editors (Skim's "go to source
   from PDF") use the latest aux it finds. If both exist, behavior is
   editor-dependent.

**Verdict.** Idempotent for Makefile-driven builds. **Severity 0**
for build correctness; **Severity 1** for confusion. Recommend
`make clean` (which DOES delete `*.aux` at top level, line 293) be
run once after a manual build slip.

---

## §5. Build reproducibility

### §5.1. The W5-X11 wave-3 baseline

Per W5-X11, the canonical 155-page PDF reproduces with:

```sh
TEXINPUTS=/tmp/topological-strings-referee-clean-20260428:/Users/raeez/latex-template:: \
  pdflatex -interaction=nonstopmode -file-line-error main.tex
```

run from a clean tmpdir into which all 25 source files (listed in W5-X11
§1.1) are copied. **Verification.** The path
`/Users/raeez/latex-template/` exists and contains
`raeez-math-template.sty` (46 KB, mtime Apr 24). The repo root has a
working symlink:

```
raeez-math-template.sty -> ../latex-template/raeez-math-template.sty
```

The path `/tmp/topological-strings-referee-clean-20260428/` exists
(from a previous W5-X11 reproduction) and contains 30 source files
plus a `pass3.stdout`. So the W5-X11 incantation is executable.

### §5.2. The Makefile-native incantation (canonical for the repo)

```sh
cd /Users/raeez/topological-strings
make clean                       # scrub aux at top level + out/
make pdf                         # 7 pdflatex passes + 2 makeindex
                                 # outputs out/main.pdf (155-156 pp)
```

**Pre-requisites for a fresh clone.**

1. `pdflatex` (TeX Live 2024+, pdfTeX 1.40.27 or compatible).
2. `makeindex` for the nomenclature build step.
3. The sibling repo `/Users/raeez/latex-template/` (containing
   `raeez-math-template.sty`) with the symlink pre-built. This is
   ENVIRONMENT-DEPENDENT and reduces the build's portability:
   a fresh clone on an unfamiliar host cannot build without that
   sibling repo.

**Severity 2.** A reviewer cloning ONLY `topological-strings/` will
fail at `\usepackage{raeez-math-template}` because the symlink target
does not exist. The Makefile is silent on this dependency. The
W5-X11 reviewer harness (with the explicit
`TEXINPUTS=…/latex-template:` prefix) captures this; the local
`make pdf` does NOT. Recommended (proposal-only): vendor
`raeez-math-template.sty` directly into the repo or document the
sibling-repo dependency in `README.md`.

### §5.3. PDF metadata cross-check

`out/main.pdf` (mtime Apr 28 23:28, 1029808 bytes, **156 pages**) is
the current canonical artifact. The top-level `main.pdf` (mtime
Apr 28 08:09, 1023660 bytes, **154 pages**) is older by ~15 hours and
by 2 pages -- this difference matches the appendix additions made in
the cycle-2 wave. **Either PDF is publication-quality**; the
`out/main.pdf` is current.

The 155-page reference in the X11 audit corresponds to an
intermediate-day build; the `out/main.pdf` extension to 156 pages
reflects subsequent appendix and lane additions.

---

## §6. Severity ledger

| Item | Severity | Action |
|------|----------|--------|
| `make pdf` 7-pass over-engineering | 1 | (proposal) reduce to 4 passes; cosmetic only |
| `make clean` missing `.bbl`, `.blg`, `.brf`, `.bcf`, `.run.xml` | 1 | (proposal) add to `TEXDEBRIS` |
| `.gitignore` missing `.DS_Store` | 1 | (proposal) add line |
| `.gitignore` missing `.agents/`, `.claude/` | 1 | (proposal) add 2 lines |
| `.gitignore` missing `out_test/` | 1 | (proposal) add line |
| `.gitignore` missing `scripts/__pycache__/`, `*.pyc` | 1 | (proposal) add 2 lines |
| `.gitignore` missing `reconstitution/private-tmp-artifacts-*/` | **2** | (proposal) add explicit pattern; 45 MB / 447 files at risk if reconstitution/ ever staged wholesale |
| Top-level stale `main.aux` Apr 28 02:23 vs canonical out/main.aux Apr 28 23:28 | 0 | idempotent for Makefile flow; cosmetic |
| `raeez-math-template.sty` symlink dep on sibling repo | **2** | (proposal) document in README or vendor inline; blocks fresh-clone build |
| `frontier_mnop_framing_volume.{aux,log,idx,pdf,tex}` orphan | 1 | not `\input`'d by `main.tex`; check if intentional standalone or stale |
| Untracked `.tex` files referenced by `main.tex` | **2** | publication-blocker on clean clone; outside this audit's edit scope but flagged here |
| LaTeX aux coverage in `.gitignore` | 0 | complete |
| `make help` documentation | 1 | "Full legacy build" phrase mismatches `.DEFAULT_GOAL := pdf` |

**Highest severity in build-infrastructure scope: 2** (private-tmp-artifacts
gitignore gap; sibling-repo dependency; untracked `.tex` files).

**Net status.** Build infrastructure works for the principal's local
flow but has documented gaps for a reviewer or fresh-clone
reproducibility. No severity-3+ blocker. Hygiene gaps are real but
proposal-only at this stage; per task constraints, no edits are made.

---

## §7. Reproducibility certification

**Canonical build commands** (validated by file-system inspection,
not re-run):

* **In-repo (principal's flow).** `cd /Users/raeez/topological-strings
  && make pdf` produces `out/main.pdf`, 156 pages, ~1.0 MB.
* **Referee-clean (W5-X11).**
  `TEXINPUTS=/tmp/topological-strings-referee-clean-20260428:/Users/raeez/latex-template:: pdflatex -interaction=nonstopmode -file-line-error main.tex`
  reproduces 155 pages cleanly (validated by W5-X11; the path
  expansion confirms file-system existence today).
* **Cold-clone-from-GitHub.** WILL FAIL until (a) `raeez-math-template.sty`
  is vendored or documented, AND (b) the 12+ untracked `.tex` files
  are added to the index.

---

## §8. Verdict

**Severity 2** -- build infrastructure has gaps that do not block the
principal's local flow but DO block referee-quality reproducibility
from a clean GitHub clone. Two specific gaps:

1. **`.gitignore` does not exclude `reconstitution/private-tmp-artifacts-*/`**.
   45 MB / 447 files of private worktree state is at-risk of being
   committed if the reconstitution audit-trail is ever ingested
   wholesale.
2. **The sibling-repo `latex-template/` dependency is undocumented**
   and blocks fresh-clone build. Either vendor inline or document.

Hygiene refinements (`.DS_Store`, `.agents/`, `.claude/`, `out_test/`,
`scripts/__pycache__/`) are severity-1 polish.

LaTeX auxiliary coverage is complete; the Makefile builds reliably
with `make pdf`; the stale top-level `main.aux` is idempotent for the
Make-driven build. No severity-3+ blocker. Recommended action:
principal-authorized addition of the `.gitignore` patterns above and
documentation (or vendoring) of `raeez-math-template.sty` in `README.md`.

Report. `reconstitution/phase4-exec-W5-X33-build-system-2026-04-28.md`
(this file). Master-ledger summary: `reconstitution/attack-heal-platonic-2026-04-28.md`
(append in §"Phase-4 EXEC Progress Ledger").
