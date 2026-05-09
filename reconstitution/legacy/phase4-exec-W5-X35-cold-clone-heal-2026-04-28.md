# Phase-4 EXEC W5-X35: Cold-Clone Reproducibility Heal Drafter

**Author.** Raeez Lorgat
**Mode.** Proposal-only. No commits. No edits to source files.
**Date.** 2026-04-28
**Inheritance.** W5-X33 surfaced two severity-2 cold-clone reproducibility blockers; this drafter proposes the mechanical heals.

---

## 1. Verification of W5-X33 findings

### 1.1 Symlink blocker (severity 2)

```
$ ls -la raeez-math-template.sty
lrwxr-xr-x@ 1 raeez staff 41 Apr 28 01:22 raeez-math-template.sty -> ../latex-template/raeez-math-template.sty
```

**Confirmed.** `raeez-math-template.sty` is a symlink pointing outside the repository tree to `/Users/raeez/latex-template/raeez-math-template.sty` (1242 lines, 46 734 bytes; package mtime 2026-04-24 21:28). The sibling repository has remote `https://github.com/raeez/amstex-template.git` (note: same remote name as this repo's origin, indicating both share the upstream template lineage but live in separate working copies).

Loaded by `main.tex:4`:

```
\usepackage{raeez-math-template}
```

A cold `git clone` of `topological-strings` will preserve the symlink as a dangling pointer into a non-existent path. `pdflatex main.tex` will fail at `\usepackage{raeez-math-template}` with a `LaTeX Error: File 'raeez-math-template.sty' not found.`

### 1.2 Untracked `.tex` files (severity 2)

```
$ git ls-files | grep -E "(claim-strength-ledger|local-dictionary|open-obligations|principles|theorem-lanes|tate-|appendix-)\.tex"
[no output for the 12 target files]
```

The grep returns the seven `tate-{P1,P3,P5,T1,T2,T3,T4,T5}-*.tex` files that **are** tracked, but the W5-X33 list of 12 untracked files is confirmed missing from `git ls-files`. Cross-checked against `\input{...}` directives in `main.tex`:

| File | Size (bytes) | `\input{}` site in main.tex |
|---|---|---|
| `claim-strength-ledger.tex` | 8 603 | `\input{claim-strength-ledger.tex}` |
| `local-dictionary.tex` | 7 169 | `\input{local-dictionary.tex}` |
| `principles.tex` | 8 593 | `\input{principles.tex}` |
| `theorem-lanes.tex` | 21 787 | `\input{theorem-lanes.tex}` |
| `tate-T1-weighted-completion.tex` | 41 469 | `\input{tate-T1-weighted-completion}` |
| `tate-T2-nilpotent-truncation.tex` | 28 715 | `\input{tate-T2-nilpotent-truncation}` |
| `tate-T5-chain-level-primitive.tex` | 37 912 | `\input{tate-T5-chain-level-primitive}` |
| `tate-P5-cross-volume.tex` | 6 690 | `\input{tate-P5-cross-volume}` |
| `open-obligations.tex` | 11 131 | `\input{open-obligations.tex}` |
| `appendix-matlis-principal-parts.tex` | 17 959 | `\input{appendix-matlis-principal-parts}` |
| `appendix-factorization-current-conventions.tex` | 6 519 | `\input{appendix-factorization-current-conventions}` |
| `appendix-unreduced-bv-qme.tex` | 7 046 | `\input{appendix-unreduced-bv-qme}` |
| `appendix-radial-parts-moyal.tex` | 14 437 | `\input{appendix-radial-parts-moyal}` |

**Total.** 13 files, ~218 KB. (Inventory of 12 in W5-X33 was off-by-one; the full set spans 4 appendices + 5 tate-prep files + 4 scaffold files. All 13 are load-bearing for `main.tex`.)

**Confirmed.** Cold clone produces a tree where `main.tex` references thirteen `\input{}` targets that do not exist on disk. `pdflatex` will halt at the first missing `\input` with `! LaTeX Error: File 'claim-strength-ledger.tex' not found.`

---

## 2. Symlink remediation: option analysis and recommendation

### Option A — Vendor the .sty file in-tree (copy as a regular tracked file)

**Mechanism.** Replace the symlink with a regular file containing the byte-identical contents of `/Users/raeez/latex-template/raeez-math-template.sty`. Track it.

- **Pros.** Cold clone works without external prerequisites. The repository becomes self-contained per Russian-school standalone discipline. No environmental drift between developer machines. arXiv submission tarball is straightforward (pdflatex + tracked .sty resolves entirely from the repository).
- **Cons.** When `latex-template` evolves upstream, `topological-strings` must explicitly resync. Divergence is detectable but not automatic. The .sty becomes a vendored artifact that sibling repos may drift from.

### Option B — Document the prerequisite in README

**Mechanism.** Keep the symlink. Add a README section instructing the user to clone `https://github.com/raeez/amstex-template.git` (or an equivalent provider) into `../latex-template/` before building.

- **Pros.** Single source of truth for the .sty package. No vendor drift. Clean.
- **Cons.** Cold clone still requires manual setup. arXiv submission is nontrivial (must bundle the .sty separately and rewrite the symlink at submission time). Reviewers and collaborators face a setup tax that violates standalone discipline. Symlinks-into-`..` are also a portability hazard on case-insensitive filesystems and on Windows hosts.

### Option C — Hybrid: vendor + sibling-sync workflow

**Mechanism.** Vendor the .sty as in Option A. Also add a `make sync-template` target that compares the in-tree copy against `../latex-template/raeez-math-template.sty` and either rsyncs from the sibling or surfaces a diff. Document the sync convention in README.

- **Pros.** All Option A benefits. Adds an explicit, scriptable bridge for upstream propagation. Drift is detectable rather than silent.
- **Cons.** Adds Makefile surface that depends on the sibling repo path. The sync target is host-specific (`/Users/raeez/latex-template`) unless parameterized.

### Recommendation

**Option C, with Option A as the immediate next step and Option C as the polish.**

Russian-school standalone discipline (per `~/ecosystem/INVARIANTS.md` and the every-file-into-the-repo rule) requires that the tree be self-contained, reproducible from a clean clone, and free of environmental dependencies that aren't either standard system tooling (TeX Live, GNU make) or explicitly tracked. A symlink into an untracked sibling path violates this on every dimension. Vendoring is mandatory.

The sibling-sync workflow then preserves the engineering benefit of single-source-of-truth for the .sty package across Raeez's repos, surfaces drift explicitly via diff, and allows a cleanly-scriptable propagation when the template evolves. The cost is one Makefile target.

**Concrete heal for the next phase (NOT executed here):**

1. Remove the symlink: `rm raeez-math-template.sty`.
2. Copy in: `cp /Users/raeez/latex-template/raeez-math-template.sty raeez-math-template.sty`.
3. `git add raeez-math-template.sty`.
4. Add Makefile target (proposal):

```makefile
LATEX_TEMPLATE_SIBLING := /Users/raeez/latex-template/raeez-math-template.sty

.PHONY: sync-template diff-template
sync-template:
	@if [ -f "$(LATEX_TEMPLATE_SIBLING)" ]; then \
		cp "$(LATEX_TEMPLATE_SIBLING)" raeez-math-template.sty && \
		echo "  ok  raeez-math-template.sty synced from sibling"; \
	else \
		echo "  fail  sibling not found at $(LATEX_TEMPLATE_SIBLING)"; \
		exit 1; \
	fi

diff-template:
	@if [ -f "$(LATEX_TEMPLATE_SIBLING)" ]; then \
		diff -u raeez-math-template.sty "$(LATEX_TEMPLATE_SIBLING)" || true; \
	else \
		echo "  (no sibling at $(LATEX_TEMPLATE_SIBLING))"; \
	fi
```

5. Document in README that the canonical upstream is the sibling repo and that drift is detected via `make diff-template`.

---

## 3. Untracked .tex remediation: explicit `git add` invocation

**Proposed `git add` command (NOT executed here).** Names each file explicitly to avoid `-A` / `.` accidents:

```bash
git add \
  appendix-factorization-current-conventions.tex \
  appendix-matlis-principal-parts.tex \
  appendix-radial-parts-moyal.tex \
  appendix-unreduced-bv-qme.tex \
  claim-strength-ledger.tex \
  local-dictionary.tex \
  open-obligations.tex \
  principles.tex \
  tate-P5-cross-volume.tex \
  tate-T1-weighted-completion.tex \
  tate-T2-nilpotent-truncation.tex \
  tate-T5-chain-level-primitive.tex \
  theorem-lanes.tex
```

**File size sanity check.** Largest is `tate-T1-weighted-completion.tex` at 41 469 bytes (40 KB); smallest is `tate-P5-cross-volume.tex` at 6 690 bytes. All thirteen are plain LaTeX text under 50 KB. None resemble binary blobs, secrets, or unusually large files. Total added bytes: ~218 KB. Safe for git history.

---

## 4. `.gitignore` extension proposal

The current `.gitignore` covers LaTeX auxiliary debris exhaustively (aux, log, bbl, etc.) but does not cover the agent-harness artifacts, OS clutter, Python bytecode, or the per-day private artifact archives. Append a new section:

```
## ----------------------------------------------------------------------------
## Local agent harness, OS clutter, build experiments, private artifacts:

# macOS Finder metadata
.DS_Store

# Multi-agent harness state (.agents/ skills, .claude/ scheduled tasks and worktrees)
.agents/
.claude/

# Build experiments separate from the canonical out/ directory
out_test/

# Python bytecode caches from scripts/
scripts/__pycache__/
*.pyc

# Per-day private scratch archives under reconstitution/ (multi-MB, machine-local)
reconstitution/private-tmp-artifacts-*/
```

**Verification of sizes.**

- `.DS_Store`: 6 148 bytes (single file, but spawns recursively; needs ignore).
- `.agents/`: 4 KB.
- `.claude/`: 12 MB (worktrees + commands + scheduled_tasks.lock).
- `out_test/`: 224 KB (PDF + log + aux from a debug build).
- `scripts/__pycache__/`: 400 KB (compiled Python 3.14 bytecode).
- `reconstitution/private-tmp-artifacts-2026-04-28/`: 45 MB (the dominant blocker; per-day so the glob `private-tmp-artifacts-*` is correct).

The regex `reconstitution/private-tmp-artifacts-*/` excludes the per-day archives without excluding the markdown ledgers in `reconstitution/`, which are intelligence we must propagate per `~/ecosystem/INVARIANTS.md`.

---

## 5. Makefile `TEXDEBRIS` extension

Current line:

```makefile
TEXDEBRIS := *.toc *.ilg *.log *.nlo *.dvi *.aux *.tar.gz *.nlo *.nls *.nls *.out *.toc *.sta *.gla *.fdb_latexmk *.fls *.synctex.gz
```

(Note: `*.toc`, `*.nlo`, `*.nls` are duplicated; harmless but cosmetic.)

**Proposed extension** to cover bibliography and crossref auxiliaries that the current build leaves behind:

```makefile
TEXDEBRIS := *.toc *.ilg *.log *.nlo *.dvi *.aux *.tar.gz *.nlo *.nls *.nls *.out *.toc *.sta *.gla *.fdb_latexmk *.fls *.synctex.gz *.bbl *.blg *.brf *.bcf *.run.xml *.idx
```

Adds:

- `*.bbl` — biblatex/biber bibliography output (bibliography body the build re-emits each pass).
- `*.blg` — biblatex log.
- `*.brf` — hyperref back-references.
- `*.bcf` — biblatex control file (biber input).
- `*.run.xml` — biblatex auxiliary XML for biber.
- `*.idx` — makeindex raw index (the .ilg / .ind pair for nomencl is already covered).

These are all listed under the "Bibliography auxiliary files" and "makeidx" sections of the existing `.gitignore`, so they are already untracked; the Makefile change ensures `make clean` removes them from disk after a build. Both top-level and `out/` are swept since `clean` runs `$(KILL) $(TEXDEBRIS)` then descends into `$(OUTDIR)`.

---

## 6. README.md scaffold

**Proposed full replacement** for the current `amstex-template` boilerplate (lines 1-26 of `README.md`):

```markdown
# Topological Strings — Kodaira–Spencer gravity and quantum amplitudes

Computations and remarks on Kodaira–Spencer gravity and quantum string amplitudes
in topological string theory, extending the Bershadsky–Cecotti–Ooguri–Vafa
(BCOV, 1993) framework for the closed topological B-model on Calabi–Yau
threefolds. Sole author: Raeez Lorgat (`raeez.lorgat@gmail.com`). The compiled
manuscript lives at `out/main.pdf` and is a continuously revised research
document; see `claim-strength-ledger.tex` and `open-obligations.tex` for the
current epistemic state of each result.

## Build

```
make pdf       # full multi-pass build via pdflatex (writes out/main.pdf)
make fast      # single-pass build for incremental editing
make release   # full rebuild + standalone documents + iCloud copy
make clean     # remove LaTeX debris
make help      # full target list
```

The build requires a standard TeX Live installation (or MacTeX) with
`pdflatex`, `makeindex`, and `nomencl`. See `Makefile` for full configuration.

## Prerequisites

- TeX Live 2023+ or MacTeX with `pdflatex`, `makeindex`.
- GNU `make`.
- The package `raeez-math-template.sty` is **vendored in this repository** as
  a tracked file (see Option C in `reconstitution/phase4-exec-W5-X35-...`).
  The canonical upstream is the sibling repository at
  `https://github.com/raeez/amstex-template.git`; use `make diff-template`
  against a local sibling clone to detect drift.

## arXiv submission

The repository is self-contained: a fresh clone plus `make pdf` produces
`out/main.pdf` without external setup. For arXiv submission, the source
tarball should include `main.tex`, all `*.tex` inputs (preamble, abstract,
notation, principles, claim-strength-ledger, local-dictionary, theorem-lanes,
open-obligations, the `tate-*.tex` files, and the `appendix-*.tex` files),
`raeez-math-template.sty`, the `*.png` / `*.svg` figure assets, and the bib
file if present. `make tar` produces a timestamped archive in `out/`.

## License

(To be confirmed by the author. Default assumption: research preprint, all
rights reserved unless explicitly stated otherwise in `main.tex`.)

## Research constellation

This repository is the physics companion to the volume-III CY-to-chiral
frontier held in `~/calabi-yau-quantum-groups`. Convention agreement on
$d = \dim_{\mathbb{C}} X$, the worldsheet $\Sigma$, and framing data on $S^3$
must be load-bearing-explicit when both are cited; divergences are reported,
not silently reconciled. The modular-form bridge to `~/igusa-cusp-form` via
the Borcherds / BKM route is heuristic and convention-checking, not
inference-strength.

See `CLAUDE.md` and `~/ecosystem/INVARIANTS.md` for the canonical voice and
build-discipline rules.
```

The scaffold replaces the generic "amstex-template" / "build targets are { tar, pdf, html }" prose with an honest description of the manuscript, build instructions matching the existing Makefile, prereq notes that align with the recommended Option-C vendor + sibling-sync workflow, an arXiv-submission checklist that lists every load-bearing input file, and a placeholder license statement requiring author confirmation.

---

## 7. Verification plan: cold-clone reproducibility

Once the heals from sections 2-6 are landed (in a separate exec wave, not in this proposal), the following sequence proves cold-clone reproducibility:

```bash
# 1. Fresh clone in a scratch directory, no environmental setup.
TMPDIR=$(mktemp -d /tmp/topstrings-cold-clone.XXXXXX)
cd "$TMPDIR"
git clone https://github.com/raeez/topological-strings.git
cd topological-strings

# 2. Verify no symlinks remain in the working tree.
find . -type l -not -path './.git/*' | tee symlinks.txt
test ! -s symlinks.txt && echo "  ok  no symlinks" || { echo "  fail  symlinks remain"; cat symlinks.txt; exit 1; }

# 3. Verify all main.tex \input{} targets resolve.
grep -oE '\\input\{[^}]+\}' main.tex | sed -E 's/\\input\{([^}]+)\}/\1/' | while read f; do
  base="${f%.tex}"
  if [ ! -f "${base}.tex" ] && [ ! -f "$f" ]; then
    echo "  fail  missing \\input target: $f"
    exit 1
  fi
done
echo "  ok  all \\input targets resolve"

# 4. Verify raeez-math-template.sty is a regular file, not a symlink.
test -f raeez-math-template.sty && test ! -L raeez-math-template.sty \
  && echo "  ok  raeez-math-template.sty is a regular tracked file"

# 5. Build.
make pdf

# 6. Verify the PDF exists and matches the expected page count.
test -f out/main.pdf && echo "  ok  out/main.pdf produced"
PAGES=$(mdls -name kMDItemNumberOfPages out/main.pdf 2>/dev/null | awk '{print $3}')
echo "  pages: $PAGES (current canonical: 156)"
test "$PAGES" -ge 150 && echo "  ok  page count in expected range" \
  || { echo "  warn  unexpected page count $PAGES (expected ~156)"; }

# 7. Run make clean and confirm no orphan debris.
make clean
ls *.aux *.log *.bbl *.bcf *.run.xml *.idx 2>/dev/null | tee debris.txt
test ! -s debris.txt && echo "  ok  clean target sweeps all debris" \
  || { echo "  fail  debris remains:"; cat debris.txt; }
```

**Pass criteria.**

- Step 2: `find -type l` returns empty.
- Step 3: every `\input` target resolves to a tracked file.
- Step 4: `raeez-math-template.sty` is `-rw-r--r--`, not `lrwxr-xr-x`.
- Step 5: `pdflatex` exits 0 on the final pass.
- Step 6: `out/main.pdf` exists; page count ≥ 150 (current canonical 156, with tolerance for revision).
- Step 7: `make clean` leaves no `.aux`, `.log`, `.bbl`, `.bcf`, `.run.xml`, or `.idx` files.

If any step fails, the heal is incomplete and the cold-clone blocker remains.

---

## 8. Persistence and propagation

This document persists at:

- `/Users/raeez/topological-strings/reconstitution/phase4-exec-W5-X35-cold-clone-heal-2026-04-28.md` (this file).

A 250-word summary will be appended to `attack-heal-platonic-2026-04-28.md` under section heading "Phase-4 EXEC W5-X35: Cold-Clone Reproducibility Heal Drafter".

**No commits. No edits to source files.** The drafter delivers proposals; the next exec wave applies them.
