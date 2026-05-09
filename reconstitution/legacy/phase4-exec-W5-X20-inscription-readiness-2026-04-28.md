# Phase-4 EXEC W5-X20: Inscription Readiness Validator

**Date.** 2026-04-28.
**Author.** Raeez Lorgat.
**Role.** Attacker W5-X20 (Inscription Readiness Validator), attack-heal-swarm wave 5.
**Mode.** Read-only on the working tree. NO commit; NO edit of any TeX file.
**Target.** Independently re-verify W5-X15's claim that 0 / 472 mandatory wave-5 inscription has reached the working tree, attest the locations and write-ordering required to inscribe, and stage the post-inscription verification plan.

---

## 0. Bottom-line

W5-X15 is corroborated in full. Independent grep on the working
tree at 2026-04-28 returns **zero hits** for every surface marker
that would indicate the wave-4 base or wave-5 mandatory delta is
inscribed. The seven mandatory atomic deltas (5 wave-4 base sites +
3 wave-5 mandatory sites) are all REMAINING. The 155-page working
tree growth is fully attributable to conditionalisation, apparatus
binding, the U(1)-anomaly subsection in `main.tex`, and the
cross-volume firewall rewrite (P5, P3) — not to the proposed
+472-line W5-X5 synthesis target.

Inscription would be 100% additive (no rewrites of existing prose),
but introduces a strict **acyclic dependency chain across five
files** that fixes the write order (preamble → ledger → main.tex
references → main.tex remarks → theorem-lanes augment). At one
ordering decision (Stage 5 versus Stage 7) the order is locally
free; everywhere else it is dictated by `\newtheorem` declaration
preceding `\begin{hyp}` usage and by `\ref{...}` consumers
inscribing after their target labels.

**Verdict: Inscription is READY but UNAUTHORIZED.** The dependency
chain is short, the verification plan is mature, the surface scans
on the proposed text pass. Awaiting user authorisation; the working
tree builds at publication grade without it.

---

## 1. Independent grep verification (W5-X15 §1.1 reproduction with fresh eyes)

For each surface marker named in the W5-X20 mandate, the live
working-tree result is:

| # | Marker | Search domain | Hits | Status |
|---|--------|---------------|------|--------|
| 1 | `\newtheorem{hyp}` | `preamble.tex` | 0 | REMAINING |
| 2 | `rmk:costello-class-meta` (or `costello-class-meta`) | all `*.tex` | 0 | REMAINING |
| 3 | `four meta-hypothes` (any case) | all `*.tex` | 0 | REMAINING |
| 4 | `Quillen equivalence` (or `Quillen-equivalence`) | `main.tex` lines 2222-2246 | 0 | REMAINING |
| 5 | `F''` theorem block (or `Theorem F''`, `MHB-A1`, `column-Verma`, `widehat M_0`) | `claim-strength-ledger.tex` | 0 | REMAINING |
| 6 | `parabolic stabili` / `P_{(z_1)}` / `m-adic ideal` / `outer-twist` | `claim-strength-ledger.tex` | 0 | REMAINING |
| 7 | `Decoupling` / `decoupling` / `chain-level closure` / `brane-line factorization` (decoupling sense) | `theorem-lanes.tex` U(1)-anomaly lane lines 419-455 | 0 | REMAINING |
| 8 | `\begin{hyp}` / `\end{hyp}` (env usage) | all `*.tex` | 0 | REMAINING (would error-compile if 1 were not REMAINING also) |
| 9 | `firewall-typology` | all `*.tex` | 0 | REMAINING |
| 10 | `Costello-class` / `Costello class` | all `*.tex` | 0 | REMAINING |

**Result: 10 / 10 markers absent. W5-X15's "all REMAINING" verdict is
CONFIRMED at the byte level.**

### 1.1 Sub-verification: U(1)-anomaly lane Residuals block

`theorem-lanes.tex:452-455` reads exactly:

```
\emph{Residuals.} The lane does not lift the reduced comparison to the
unreduced scalar direction and does not imply compact Calabi--Yau,
BKM, Igusa, or sister-volume anomaly statements.
\end{stmt}
```

This is the wave-3 residual text only. The W5-A6 SH-1 / SH-2 / SH-3
decoupling block is not present.

### 1.2 Sub-verification: `rmk:E1-translation` body (`main.tex:2229-2246`)

The body reads (lines 2230-2246) the locally-constant /
Costello--Gwilliam / HKR / PV identification text from wave-3. The
sentence "the open polynomial Hamiltonian sector is the
Quillen-equivalent strict $P_0$ subalgebra ... in the sense of HA
\S A.3.7" is absent.

### 1.3 Sub-verification: claim-strength-ledger.tex structural state

204 lines total: a preamble paragraph (lines 1-19), a longtable
"Main theorem-status exclusions" (lines 21-78), a longtable "Claim
ledger" (lines 80-203), and `\endgroup` at 204. **No master
hypothesis block, no Theorem F'' inscription, no Theorem $G^{\rm
otr}$ inscription, no parabolic-stabiliser sentence, no (A2$'$)
outer-twist comment.**

### 1.4 Sub-verification: preamble.tex

200 lines total. Theorem environments declared: `thm`, `prop`,
`lem`, `cor`, `rmk`, `defn`, `ex`, `exc`, `conj`, `prob`, `oprob`,
`stmt`, `qn`, `ans`, `constr`. **`hyp` is not declared.** The
nearest insertion site is after line 149 (`\newtheorem{constr}`).

---

## 2. Exact insertion points (file:line)

For each remaining mandatory delta, the proposal-only insertion
site is given below. Each is verified as structurally well-formed
in the sense that the surrounding `\begin{...}\end{...}` wrap
holds (no orphaned nesting) and the LaTeX scope is correct.

### 2.1 Stage 0: `preamble.tex` — `\newtheorem{hyp}` declaration

- **File.** `/Users/raeez/topological-strings/preamble.tex`.
- **Insert after line.** 149 (after `\newtheorem{constr}[thm]{Construction}`).
- **Lines added.** +2.
- **Surrounding scope.** Outside any `\begin{document}`; well-formed top-level preamble block.
- **Block.**
  ```latex
  \theoremstyle{definition}
  \newtheorem{hyp}[thm]{Hypothesis}
  ```

### 2.2 Stage 1: `claim-strength-ledger.tex` — Master hypothesis block

- **File.** `/Users/raeez/topological-strings/claim-strength-ledger.tex`.
- **Insert after line.** 19 (after the status-vocabulary list, before `\subsection*{Main theorem-status exclusions}` at line 21).
  ALTERNATIVE: append at end of file before `\endgroup` at line 204 (also structurally well-formed; matches wave-4 base draft preference).
- **Lines added.** +267 (master hypothesis block: 7 `\hyp` blocks plus 2 longtable blocks plus anti-attack scan side-bar plus Costello-class compatibility remark).
- **Surrounding scope.** Inside the `\begingroup ... \endgroup` envelope (lines 4-204). Insertion preserves the envelope.
- **Pre-requisite.** Stage 0 (`\newtheorem{hyp}` in preamble) must be inscribed FIRST.

### 2.3 Stage 2: `claim-strength-ledger.tex` — Theorem F'' block

- **File.** Same.
- **Insert after.** Stage 1 master block (i.e., at line 19 + 267 = 286 of the post-Stage-1 file).
- **Lines added.** +56.
- **Block.** Theorem F'' (Bezrukavnikov-class column-Verma identification) plus claim-strength row entry.
- **Pre-requisite.** Stage 1 must be inscribed (the F'' theorem references the (A1)-(A5) hypothesis labels).

### 2.4 Stage 3: `claim-strength-ledger.tex` — Theorem $G^{\rm otr}$ frontier reference

- **File.** Same.
- **Insert at.** End of file, before `\endgroup` at the post-Stage-2 line ~342.
- **Lines added.** +2.

### 2.5 Stage 4: `open-obligations.tex` — Phase-5 residual updates

- **File.** `/Users/raeez/topological-strings/open-obligations.tex`.
- **Insert at.** End of `\begin{enumerate}...\end{enumerate}` envelope (currently ends at line 223).
- **Lines added.** +24 (4 new `\item` entries listing Theorem $G^{\rm otr}$ discharge, structural inscription, etc.).
- **Surrounding scope.** Inside `\begin{enumerate}` (line 8) ... `\end{enumerate}` (line 223). Insertion preserves the envelope.

### 2.6 Stage 5: `theorem-lanes.tex` — Cross-walk update + decoupling base

- **File.** `/Users/raeez/topological-strings/theorem-lanes.tex`.
- **Insert at.** Line 454 (before `\end{stmt}` at line 455 of `thm:lane-u1-anomaly`).
- **Lines added.** +30 (cross-walk update plus +11-line wave-4 base decoupling-clause draft).
- **Surrounding scope.** Inside the `\begin{stmt}[Index lane: scalar U(1) anomaly]` (line 419) ... `\end{stmt}` (line 455) envelope. The +30 lines extend the existing `\emph{Residuals.}` block.

### 2.7 Stage 6: `main.tex` — Citation references

- **File.** `/Users/raeez/topological-strings/main.tex`.
- **Insert at.** 7 distinct `\ref{...}` updates spread across the manuscript (W5-X5 §1.5.0 enumerates these; primarily near `thm:open-closed-derived-center-factorization` proof body and the `claim-strength-ledger` cross-references at lines 508 / 1171 / 1202).
- **Lines added.** +7.
- **Pre-requisite.** Stages 1, 2, 5 must be inscribed FIRST (otherwise the `\ref{}` resolves to "??").

### 2.8 Stage 7: `main.tex` — `rmk:costello-class-meta`

- **File.** Same.
- **Insert at.** Line 2227 (immediately after `\end{proof}` of `thm:open-closed-derived-center-factorization`) and before `\begin{rmk}[Locally constant ...]` at line 2229.
- **Lines added.** +10.
- **Surrounding scope.** Outside the proof envelope (proof closes at 2227); outside the next `\begin{rmk}` (opens at 2229). Structurally a free insertion site at top-level section scope.

### 2.9 Stage 8: `main.tex` — Quillen-equivalence sentence inside `rmk:E1-translation`

- **File.** Same.
- **Insert at.** Line 2245, immediately before `\end{rmk}` at line 2246.
- **Lines added.** +3.
- **Surrounding scope.** Inside the `\begin{rmk}[Locally constant ...]\label{rmk:E1-translation}` (line 2229) ... `\end{rmk}` (line 2246) envelope. Insertion extends the remark body.

### 2.10 Stage 9: `claim-strength-ledger.tex` (line-delta 56 of NEW F'' block) — parabolic stabiliser sentence

- **File.** Same as Stage 2.
- **Insert at.** Inside the F'' theorem block (Stage 2) at the post-Stage-2 line ~340 of the file (offset 56 inside the F'' block).
- **Lines added.** +3.
- **Pre-requisite.** Stage 2 inscribed.

### 2.11 Stage 10: `claim-strength-ledger.tex` (line-delta 267 of NEW master hyp block) — (A2$'$) outer-twist comment

- **File.** Same.
- **Insert at.** Inside the (A2$'$) silent-strengthening block of Stage 1 at post-Stage-1 line ~285 of the file.
- **Lines added.** +5.
- **Pre-requisite.** Stage 1 inscribed.

### 2.12 Stage 11: `theorem-lanes.tex` — SH-1 / SH-2 / SH-3 decoupling sharpening

- **File.** Same as Stage 5.
- **Insert at.** Inside the augmented Residuals block from Stage 5, before `\end{stmt}` at the post-Stage-5 line ~485.
- **Lines added.** +7 (incremental beyond the Stage 5 +11 wave-4 base).
- **Pre-requisite.** Stage 5 inscribed (SH-1/SH-2/SH-3 reference the decoupling-clause base text).

---

## 3. Minimum sequential write-ordering (no intermediate compile break)

The constraints are:

- **C1.** `\newtheorem{hyp}` must precede any `\begin{hyp}` (Stage 0 before Stage 1).
- **C2.** `\ref{label}` must follow the line declaring `\label{label}` in the multi-pass LaTeX flow. In practice, LaTeX builds in two passes; a single intermediate stage with a forward `\ref` produces a "??" stub but does NOT break the compile. Strictly, only a `\newtheorem` requires forward declaration; `\ref` with a missing target produces a warning + "??", not a fatal error.
- **C3.** Any `\input{file}` consumer requires `file` to exist (all five files already exist; no new input files are introduced).
- **C4.** `\begin{X}...\end{X}` must remain balanced after each stage (each stage is purely additive within an open envelope and closes the envelope it opens; no stage straddles).

Given C1-C4, the unique write-ordering up to commutation is:

| Stage order | File | Action | Why this position |
|-------------|------|--------|-------------------|
| **0** | `preamble.tex` | `\newtheorem{hyp}` | C1: must precede Stage 1's `\begin{hyp}` |
| **1** | `claim-strength-ledger.tex` | Master hyp block | Provides `hyp:A1-truncation`, ..., `hyp:A5-admissibility` labels for downstream consumers |
| **2** | `claim-strength-ledger.tex` | Theorem F'' block | Consumes hyp labels from Stage 1 |
| **3** | `claim-strength-ledger.tex` | Theorem $G^{\rm otr}$ frontier ref | Independent; can commute with Stage 2 |
| **4** | `open-obligations.tex` | Phase-5 residual updates | Independent; can commute with Stages 1-3 |
| **5** | `theorem-lanes.tex` | Cross-walk + decoupling base | Independent; can commute with Stages 1-4 |
| **6** | `main.tex` | Citation references | Soft-depends on Stages 1, 2, 5 (forward `\ref` would warn but not fatal); recommended after Stage 5 |
| **7** | `main.tex` | `rmk:costello-class-meta` | New label; provides `rmk:costello-class-meta` for Stage 9-11 if any cross-reference lands |
| **8** | `main.tex` | Quillen-eq sentence in `rmk:E1-translation` | Independent of Stage 7; can commute |
| **9** | `claim-strength-ledger.tex` | F'' parabolic stabiliser sentence | Internal to Stage 2 block; must follow Stage 2 |
| **10** | `claim-strength-ledger.tex` | (A2$'$) outer-twist comment | Internal to Stage 1 block; must follow Stage 1 |
| **11** | `theorem-lanes.tex` | SH-1/SH-2/SH-3 decoupling | Internal to Stage 5 block; must follow Stage 5 |

**Strict acyclic ordering (collapsed to file-level commits).** Five
file-level edits suffice if each edit collects all stages
targeting that file:

1. `preamble.tex` (Stage 0).
2. `claim-strength-ledger.tex` (Stages 1+2+3+9+10 in one merged edit; the file is rewritten with all four wave-4 base inscriptions plus the wave-5 wave-internal sentences).
3. `open-obligations.tex` (Stage 4).
4. `theorem-lanes.tex` (Stages 5+11 in one merged edit).
5. `main.tex` (Stages 6+7+8 in one merged edit; Stages 7 and 8 do not depend on Stage 6 but the `\ref` updates of Stage 6 reference the new ledger labels and so must wait for the ledger commit).

**Compile-safety at each intermediate step.** After step 1, the
preamble compiles; the manuscript compiles unchanged (no usage of
`hyp` yet). After step 2, the master hyp block and F'' compile
locally inside `claim-strength-ledger.tex`; main.tex compiles with
forward-`\ref` warnings only (no fatal). After step 3, no compile
change. After step 4, theorem-lanes compiles with the new
decoupling block. After step 5, all `\ref` resolve.

**Only Stage 0 -> Stage 1 is hard-blocking.** All other orderings
are compile-soft (warnings, not errors).

---

## 4. Risk analysis

### 4.1 Cross-reference breakage

- **R1.** Stage 6 inscribes 7 new `\ref{...}` citations in `main.tex` pointing at labels that exist only after Stages 1, 2, 5 commit. **Mitigation.** Order: file-level commits 2 and 4 before file-level commit 5. If file-level commit 5 lands first, LaTeX produces a "??" rendered warning but compiles successfully; a second-pass build resolves on the next invocation. **Severity.** Low (warning, not fatal).

- **R2.** Stage 9-10-11 are interior to Stage 1-2-5 blocks. If a stage-aware editor inserts at the wrong line offset (e.g., line 56 of the OLD F'' block instead of line 56 of the NEW F'' block), the inscription lands inside an unrelated block. **Mitigation.** Each stage names its anchor by surrounding text (e.g., "after the 'Symp_form acts on the second tensor factor' sentence") rather than by absolute line number. **Severity.** Low (semantic, not compile-fatal; would render but in the wrong place).

- **R3.** `\label{rmk:costello-class-meta}` (Stage 7) and `\label{rmk:firewall-typology}` (in the W5-X5 optional ceiling) collide with no existing label. Verified by grep. **Severity.** Zero.

### 4.2 Compile-order dependency

- **R4.** **The hardest constraint.** `\newtheorem{hyp}` (Stage 0, in `preamble.tex`) must be inscribed before any commit that contains a `\begin{hyp}` block. If steps 1 and 2 above are reversed (i.e., `claim-strength-ledger.tex` master block is committed before `preamble.tex` is updated), the build fails with `Environment hyp undefined`. **Mitigation.** Hard sequence step 1 -> step 2; do not commit step 2 alone. **Severity.** High if violated; Zero if step order followed.

- **R5.** `\input{...}` apparatus binding sites (`main.tex:66` for ledger, `main.tex:1174` for theorem-lanes, `main.tex:5931` for open-obligations) are unchanged by the inscription. The five apparatus files continue to be sourced in the same positions. No re-binding needed. **Severity.** Zero.

- **R6.** The `commands.tex` and `mathmacros.tex` macro packs supply `\C`, `\R`, `\mathbf`, etc. Verified by grep that no new macro is introduced; the inscription uses existing macros only. **Severity.** Zero.

### 4.3 Page-break disruption

- **R7.** Inscription adds approximately +472 manuscript lines, which at the current density is roughly +12 to +18 PDF pages. Existing page-break-anchored cross-references (PDF page anchors, externally cited "see page N" mentions) would shift by approximately the same amount. **Mitigation.** Verified by grep that no `\pageref{...}` is in active use in any TeX file (zero hits in main.tex; Costello-Gwilliam / Lurie page numbers are inside `\cite{...}*{Vol.~I \S 6.4}` style, not `\pageref`). External materials (referee letters, materials/processed/) cite labelled theorems by `\ref{thm:xyz}`, not by page number. **Severity.** Zero (no active `\pageref` consumers).

- **R8.** The `tableofcontents` page count shifts by approximately +1 page if new sections like `\section*{Hypothesis declaration ledger}` are added (Stage 1). Verified that the existing TOC is regenerated each build (`\tableofcontents` at `main.tex:68`). **Severity.** Zero (TOC auto-regenerates).

### 4.4 Voice / scan regressions

- **R9.** The proposed inscription text has been pre-scanned in W5-X5 §0 and W5-A1/A2/A6 reports for em-dash, AI-tells, and `agent / swarm / reconstitution / wave / phase / ledger` vocabulary. All scans PASS on the LaTeX surface to be inscribed. **Mitigation.** Re-run scans after each file-level commit (see §5). **Severity.** Low if pre-inscribed text is used verbatim from the W5-X5 master draft; Medium if edits are made during inscription that introduce inadvertent vocabulary regressions.

- **R10.** The Russian-school voice and named attribution discipline (Bershadsky-Cecotti-Ooguri-Vafa, Witten, Costello, Polyakov, Drinfeld, Beilinson, Lurie) is preserved by the W5-X5 master draft. No new named attribution is needed for wave-5 inscription. **Severity.** Zero.

### 4.5 Macro / preamble interactions

- **R11.** The `nomencl` package is loaded (`preamble.tex:31`). New nomenclature entries are NOT introduced by the inscription. **Severity.** Zero.

- **R12.** The `tikz-cd` and `tikz` packages load arrows and decorations. The inscription does not introduce new TikZ diagrams. **Severity.** Zero.

- **R13.** `\usepackage[subpreambles=true]{standalone}` (line 4) and `\usepackage{import}` (line 5) keep apparatus files compatible with standalone compilation. The `\input{...}` chain is preserved by the inscription. **Severity.** Zero.

### 4.6 Aggregate risk verdict

| Risk class | Count | Highest severity |
|------------|-------|------------------|
| Cross-reference breakage | 3 | Low (warning, second-pass-resolved) |
| Compile-order dependency | 3 | **High if R4 ordering violated; Zero if respected** |
| Page-break disruption | 2 | Zero |
| Voice / scan regressions | 2 | Low if W5-X5 verbatim |
| Macro / preamble interactions | 3 | Zero |

**Single highest-leverage risk: R4** (`\newtheorem{hyp}` before
`\begin{hyp}`). All other risks are low or zero given the W5-X5
master draft is used verbatim and the file-commit order in §3 is
respected.

---

## 5. Post-inscription verification plan

After file-level commits 1-5 in §3 are landed (or equivalently
the 12-stage sequence), the verification protocol is:

### 5.1 Pre-build sanity scans

Run the following grep scans on the post-inscription working tree
to confirm the inscription landed at the correct sites:

```
grep -n "newtheorem{hyp" preamble.tex                    # expect 1 hit at line 150
grep -n "rmk:costello-class-meta" main.tex               # expect 1 hit (Stage 7)
grep -n "Quillen equivalence" main.tex                   # expect 1 hit (Stage 8)
grep -n "F''\|theorem F''" claim-strength-ledger.tex     # expect Stage 2 block
grep -n "parabolic stabili\|P_{(z_1)}" claim-strength-ledger.tex  # expect Stage 9
grep -n "outer-twist\|inner-twist" claim-strength-ledger.tex      # expect Stage 10
grep -n "Decoupling\|chain-level closure" theorem-lanes.tex       # expect Stages 5+11
grep -nE "\\begin{hyp}" claim-strength-ledger.tex        # expect 7 hits (A1, A2, A2', A2''_T, A3, A4, A5)
```

Pass criterion: every grep returns the expected hit count.

### 5.2 Voice / scan regression suite

Re-run the scans that established Russian-school voice and
no-AI-tells discipline:

```
# Em-dash scan (forbidden):
grep -nE "—| -- " *.tex  # zero hits expected

# AI-tells scan (forbidden):
grep -nEi "let'?s|here'?s a|i'?ll|i'?ve|in this paper, we|we hope that|we believe that" *.tex
# zero hits expected on the inscribed surface (background hits in pre-existing prose are pre-passed)

# Agent / swarm / phase / ledger / reconstitution / wave vocabulary (forbidden in manuscript):
grep -nEi "\bagent\b|\bswarm\b|\bphase[ -]?[0-9]|\bledger\b|\breconstitution\b|\bwave[ -]?[0-9]" *.tex
# zero hits expected

# attack / heal vocabulary (forbidden in manuscript):
grep -nEi "attack[ -]?heal|attack/heal" *.tex
# zero hits expected
```

Pass criterion: all four scans return zero hits on the post-inscription
working tree.

### 5.3 Cross-reference integrity scan

```
# All \label{...} declarations:
grep -hoE "\\label\{[^}]*\}" *.tex | sort -u > /tmp/labels.txt

# All \ref{...} consumers:
grep -hoE "\\(ref|alpharef|hyperref|eqref|cref)\{[^}]*\}" *.tex | sort -u > /tmp/refs.txt

# Diff: refs not declared as labels:
diff /tmp/labels.txt /tmp/refs.txt | grep "^>" | head
```

Pass criterion: no `\ref{...}` consumer references a label not
declared.

### 5.4 Clean-build verification

```
cd /Users/raeez/topological-strings
rm -f main.aux main.bbl main.blg main.idx main.ilg main.ind main.log main.nlo main.nls main.toc
make 2>&1 | tee /tmp/post-inscription-build.log
```

Pass criteria:
- `pdflatex` exits zero on the first AND second pass.
- No `! LaTeX Error: Environment hyp undefined`.
- No `! Undefined control sequence`.
- No `! Missing \begin{document}` or other catastrophic errors.
- `Overfull \hbox` and `LaTeX Warning: Reference ... undefined` warnings are tolerated only on the FIRST pass; the second pass must resolve all `\ref`.
- Final PDF page count: 155 pages + approximately +12 to +18 = approximately 167-173 pages (the W5-X5 estimate).

### 5.5 Computation script regression suite

The 21 verification scripts under `scripts/` should continue to
exit zero:

```
cd /Users/raeez/topological-strings/scripts
for f in check_*.py; do
  echo "=== $f ==="
  python3 "$f" 2>&1 | tail -3
done
```

Pass criterion: every script that was passing pre-inscription
continues to pass. No script result depends on TeX state, so
regressions should be zero by construction.

### 5.6 Standalone document compilation

Verify that the standalone files still compile in their
"subpreambles=true" mode:

```
cd /Users/raeez/topological-strings/standalone  # if standalone subdir exists
# or test the appendix files individually:
pdflatex appendix-matlis-principal-parts.tex
pdflatex appendix-factorization-current-conventions.tex
pdflatex appendix-unreduced-bv-qme.tex
pdflatex appendix-radial-parts-moyal.tex
```

Pass criterion: each standalone exits zero.

### 5.7 Visual / page-anchor verification

Open `main.pdf` and confirm:

- The Hypothesis declaration ledger appears as a new section after the claim-strength ledger.
- Theorem F'' renders as a proper `\begin{thm}...\end{thm}` block.
- `rmk:costello-class-meta` renders between the proof close and the locally-constant remark in the right typographic context.
- The Decoupling block renders within the U(1)-anomaly lane Residuals section.
- Page numbers in the table of contents update consistently.
- No `??` stubs in any cross-reference.

Pass criterion: all visual anchors render correctly.

### 5.8 Final certification

If §5.1-§5.7 all pass, the inscription is certified at:

- 0 / 0 mandatory wave-4 / wave-5 inscription remaining.
- +472 mandatory lines inscribed (line-delta sum from `git diff --stat HEAD` should match approximately).
- 167-173 page final build.
- Zero scan regressions.
- Zero cross-reference breakages.

The inscription closure can then be appended to the platonic ledger
as "Phase-4 EXEC W5-X20-INSCRIBED" with the certified line-delta
and page-count.

---

## 6. Verdict

**Severity: 0 (clean validation; W5-X15 is corroborated; inscription
plan is publication-ready awaiting authorisation).**

- W5-X15's "all REMAINING" verdict is **CONFIRMED** at the byte
  level by 10 / 10 independent grep scans returning zero hits.
- The wave-4 base +444 lines and the wave-5 mandatory +28 lines
  combine to **+472 mandatory lines REMAINING** across 5 files.
- The minimum sequential write-order is 5 file-level commits or
  equivalently 12 atomic stages, with **Stage 0 -> Stage 1 the
  unique hard-blocking dependency**; all other stages compile-soft.
- The risk profile is **R4-dominated**: violate `\newtheorem{hyp}`
  precedes `\begin{hyp}` and the build fatals; respect it and the
  build is compile-clean from step 1 onward.
- The post-inscription verification plan is mature: 7 scan
  classes, all automatable, all with pre-defined pass criteria.

**Recommendation.** When the user authorises, commit in the file
order (1) preamble.tex, (2) claim-strength-ledger.tex,
(3) open-obligations.tex, (4) theorem-lanes.tex, (5) main.tex.
Each commit is self-consistent (compiles cleanly with at most
forward-`\ref` warnings on the intermediate state) and the
sequence terminates at full +472 inscription with a clean build
and zero scan regressions.

No commit. No edit of any TeX file.

End of W5-X20 report.
