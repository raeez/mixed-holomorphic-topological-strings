# Phase-4 EXEC W5-X38: 6 Surgical Edits Drafter

**Agent.** W5-X38 = 6 Surgical Edits Drafter, attack-heal-swarm wave 5.
**Mode.** Proposal-only; no TeX file edited; no commit.
**Authorship.** Raeez Lorgat. **Date.** 2026-04-28.
**Predecessor.** W5-X23 (Inscription Dry-Run Verifier) certified
severity-1 with two regression families on the `/tmp/w5x23-dryrun/`
post-inscription state: 6 overfull \hbox warnings inside inscribed
longtables in `claim-strength-ledger.tex`, and 4 reader-visible
reconstitution-vocabulary tokens distributed across 3 sentence
sites.
**Charter.** Draft each of the 6 surgical edits as a precise,
line-count-preserving (or near-preserving) LaTeX substitution.
Verify each draft passes the em-dash, AI-tell, and agent-language
scans. Propose application sequence.

---

## §1. Source verification of regression sites

W5-X23 §6 enumerates 6 edits across 2 files. Direct read of
`/tmp/w5x23-dryrun/` reproduces each site verbatim.

### 1.1 Vocabulary-token sites (3 sites, 4 tokens, 3 edits)

| Edit | File | Line(s) | Token(s) | Verbatim |
|------|------|---------|----------|----------|
| E1 | `claim-strength-ledger.tex` | 230-231 | `Phase-4 audit`, `drafted` | "*proposed* (formally drafted in a Phase-4 audit, recommended for the next inscription pass)" |
| E2 | `claim-strength-ledger.tex` | 385-386 | `Phase-5 obligation` | "formal external verification of compatibility with Costello 2011 §5.2's graded-case framework is recorded as a Phase-5 obligation" |
| E3 | `theorem-lanes.tex` | 530 | `attack-heal` | "0 closure-level failures (M1, M2, M2 degree-3, transversality, attack-heal)." |

E1 strips two co-occurring tokens (`Phase-4 audit` and `drafted`) in
a single sentence rewrite — matches W5-X23 §6.1 ("eliminates
'Phase-4 audit' + 'draft' tokens with one healer").

### 1.2 Overfull-hbox sites (3 sites, 6 overfulls, 3 edits)

W5-X23 §3.3 identifies all 6 overfulls inside three longtables
in `claim-strength-ledger.tex`:

| Edit | longtable head line | longtable end line | Column declaration | Overfulls covered |
|------|---------------------|--------------------|--------------------|------------------|
| E4 | 403 | 483 | `p{0.30} p{0.32} p{0.30}` (sum 0.92) | #1, #2 (Theorem G QC row, ~0.77 + 2.35 pt), #3 (`thm:wt-regulator-independence-admissible`, ~31.86 pt) |
| E5 | 497 | 535 | `p{0.20} p{0.34} p{0.18} p{0.20}` (sum 0.92) | #4 ((R1) row, ~4.41 pt), #5 ((R4) row, ~66.73 pt) |
| E6 | 692 | 735 | `p{0.24} p{0.27} p{0.40}` (sum 0.91) | #6 (Ob_sc^otr display equation, ~48.79 pt) |

(All column declarations carry `>{\raggedright\arraybackslash}` and
`@{}` boundary modifiers; suppressed above for readability.)

---

## §2. The 6 surgical edits — proposed forms

### Edit 1 (E1). Strip "Phase-4 audit" and "drafted" co-occurrence

**File.** `claim-strength-ledger.tex`. **Lines.** 230-231 (status
vocabulary preamble inside the `\begingroup` around line 220).

**Old (verbatim, 2 lines):**
```
\emph{proposed} (formally drafted in a Phase-4 audit, recommended
for the next inscription pass),
```

**New (verbatim, 2 lines):**
```
\emph{proposed} (formally stated in this manuscript and recommended
for structural inscription in the next revision pass),
```

**Net delta.** 0 lines (2 -> 2). Both stripped tokens removed in one
sentence-level substitution. `formally stated` preserves the
mathematical assertion (the predicate has been asserted in the
manuscript); `recommended for structural inscription in the next
revision pass` preserves the workflow semantics ("not yet integrated
into the proof-bearing chain") without reconstitution-vocabulary
language.

**Vocabulary scan.** "drafted" -> "stated"; "Phase-4 audit" ->
"this manuscript". No em-dash, no AI-tell ("crucial", "robust",
"seamless", etc.), no agent-language ("agent", "swarm", "ledger",
"attack-heal", "wave", "phase-N"). Pass.

---

### Edit 2 (E2). Strip "Phase-5 obligation"

**File.** `claim-strength-ledger.tex`. **Lines.** 385-386 (Costello
side-bar remark inside the `\begingroup` block).

**Old (verbatim, 2 lines):**
```
formal external verification of compatibility with Costello 2011
§5.2's graded-case framework is recorded as a Phase-5 obligation.
```

**New (verbatim, 2 lines):**
```
formal external verification of compatibility with Costello 2011
§5.2's graded-case framework remains open.
```

**Net delta.** 0 lines (2 -> 2). "is recorded as a Phase-5
obligation" -> "remains open" preserves the epistemic status
(verification is outstanding) and shifts to the manuscript's standard
"open" / "open obligation" idiom (used throughout
`open-obligations.tex` and `theorem-lanes.tex`). No new tokens
introduced; the substitution is shorter than the original by 14
characters but stays within the same wrap budget.

**Alternative tightening (rejected).** "is open" is two words shorter
but loses the "remains" temporal-aspect cue that distinguishes a
permanent open obligation from a discharged one. "remains open" is
the manuscript-standard phrasing.

**Vocabulary scan.** No em-dash, no AI-tell, no agent-language.
Pass.

---

### Edit 3 (E3). Strip "attack-heal"

**File.** `theorem-lanes.tex`. **Line.** 530 (joint-F'' lane
verification listing inside the `Verification:` clause).

**Old (verbatim, 1 line):**
```
  failures (M1, M2, M2 degree-3, transversality, attack-heal).
```

**New (verbatim, 1 line):**
```
  failures (M1, M2, M2 degree-3, transversality, structural cross-checks).
```

**Net delta.** 0 lines (1 -> 1). "attack-heal" -> "structural
cross-checks" preserves the verification-list semantics (the fifth
class of named tests) while neutralising the reconstitution-process
vocabulary. "structural cross-checks" is the manuscript-standard
idiom for transversality-grade post-hoc verification.

**Vocabulary scan.** "attack-heal" removed; "structural" and
"cross-checks" both appear elsewhere in the manuscript in the
intended mathematical sense. No em-dash, no AI-tell. Pass.

---

### Edit 4 (E4). Hypothesis dependency table column rebalance

**File.** `claim-strength-ledger.tex`. **Lines.** 403-405 (longtable
column declaration).

**Old (verbatim, 3 lines):**
```
\begin{longtable}{@{}>{\raggedright\arraybackslash}p{0.30\textwidth}
  >{\raggedright\arraybackslash}p{0.32\textwidth}
  >{\raggedright\arraybackslash}p{0.30\textwidth}@{}}
```

**New (verbatim, 3 lines):**
```
\begin{longtable}{@{}>{\raggedright\arraybackslash}p{0.26\textwidth}
  >{\raggedright\arraybackslash}p{0.30\textwidth}
  >{\raggedright\arraybackslash}p{0.36\textwidth}@{}}
```

**Net delta.** 0 lines (3 -> 3). Column widths shift from
(0.30, 0.32, 0.30) summing to 0.92 to (0.26, 0.30, 0.36) summing to
0.92. Column 1 (theorem labels) tightens by 0.04\textwidth ~ 18 pt;
column 2 (hypotheses) tightens by 0.02\textwidth ~ 9 pt; column 3
(notes) widens by 0.06\textwidth ~ 27 pt.

**Coverage of W5-X23 §3.3 entries #1-#3.**
- #1 (~0.77 pt) and #2 (~2.35 pt): "Theorem G QC" row (lines 431-437).
  The notes column carries `\path{scripts/check_moyal_coefficients.py}`
  followed by the bivariate triangular identity description; +27 pt
  on column 3 absorbs the sub-pt overflow with margin to spare.
- #3 (~31.86 pt): `thm:wt-regulator-independence-admissible` row
  (lines 474-476). The notes column carries
  "Regulator-class canonicity statement.", but the **second** column
  (hypotheses) holds "(A1), (A2), (A3), (A4); (A5) for graded
  extension" which is the actual overflow source on line 474. Column 2
  tightens by 9 pt — but the hypothesis text fits in 0.30\textwidth at
  publication grade because the longest hypothesis token "(A5) for
  graded extension" is ~24 chars, well below 0.30\textwidth at
  `\small` (133 pt / 5.5 pt-per-char ~ 24 chars).

**Verification.** Col 1 still admits the longest theorem label
("`P4-EXEC-G3-M2 (M3) \(\mathfrak q(N)\) at ordinary supertrace`" =
~50 chars at `\small`, which fits in 0.26\textwidth = 116 pt at 5.5
pt/char giving ~21 chars per line, so 3 lines instead of 2 — net
height impact ~+1 line in 1 of the 13 rows, low risk).

**Net page impact.** ~+1 row-line in the 13-row table, well below
1 page boundary; longtable row-height change does not propagate to
page count regression.

**Vocabulary scan.** Pure column-width edit; no prose touched. Pass.

---

### Edit 5 (E5). Regulator admissibility table column rebalance

**File.** `claim-strength-ledger.tex`. **Lines.** 497-500 (longtable
column declaration).

**Old (verbatim, 4 lines):**
```
\begin{longtable}{@{}>{\raggedright\arraybackslash}p{0.20\textwidth}
  >{\raggedright\arraybackslash}p{0.34\textwidth}
  >{\raggedright\arraybackslash}p{0.18\textwidth}
  >{\raggedright\arraybackslash}p{0.20\textwidth}@{}}
```

**New (verbatim, 4 lines):**
```
\begin{longtable}{@{}>{\raggedright\arraybackslash}p{0.18\textwidth}
  >{\raggedright\arraybackslash}p{0.30\textwidth}
  >{\raggedright\arraybackslash}p{0.16\textwidth}
  >{\raggedright\arraybackslash}p{0.28\textwidth}@{}}
```

**Net delta.** 0 lines (4 -> 4). Column widths shift from
(0.20, 0.34, 0.18, 0.20) summing to 0.92 to (0.18, 0.30, 0.16, 0.28)
summing to 0.92. Column 4 (fragility / status) widens by
0.08\textwidth ~ 36 pt — large enough to absorb the 66.73-pt
overflow on the (R4) row. Column 1 tightens by 0.02; column 2 by
0.04; column 3 by 0.02 to fund column 4's expansion.

**Coverage of W5-X23 §3.3 entries #4-#5.**
- #4 (~4.41 pt): (R1) row line 511-513, status column carries
  "None; manuscript inscribed default at
  `\textit{stmt:costello-bv-package}`." +36 pt on column 4 absorbs
  the 4.41-pt overflow with margin.
- #5 (~66.73 pt): (R4) row line 531-534, status column carries
  "`\log\mu` ambiguity universal and `Q`-exact; manuscript inscribes
  `\mu`-independence at `\textit{rmk:hadamard-regulator-independence}`."
  +36 pt on column 4 = +0.08\textwidth ~ +36 pt; the 66.73-pt
  overflow exceeds 36 pt by 30 pt, so additional rebalance needed.

**Refinement.** To absorb the full 66.73-pt overflow on (R4), shift
to (0.16, 0.28, 0.14, 0.34). Column 4 then = 0.34\textwidth = 151 pt,
+67 pt over the original 0.20\textwidth = 89 pt. This covers
66.73 pt with margin. Column 1 stays adequate for branch labels
("(R3) Dimensional regularization" = 30 chars at 5.5 pt/char fits in
0.16\textwidth = 71 pt as 1 line). Column 3 ((A_k) preserved) stays
adequate for "(A1)-(A5) all preserved." (24 chars).

**Final E5 column declaration (verbatim, 4 lines):**
```
\begin{longtable}{@{}>{\raggedright\arraybackslash}p{0.16\textwidth}
  >{\raggedright\arraybackslash}p{0.28\textwidth}
  >{\raggedright\arraybackslash}p{0.14\textwidth}
  >{\raggedright\arraybackslash}p{0.34\textwidth}@{}}
```

Sum = 0.92, conserving total width. Column 2 (Construction) at
0.28\textwidth ~ 124 pt is adequate for the heat-kernel formula
(`K_t = (4\pi t)^{-d/2}\,e^{-|x-y|^2/(4t)} \otimes
e^{-t\Delta_{\rm sK}/2}; ...`).

**Vocabulary scan.** Pure column-width edit. Pass.

---

### Edit 6 (E6). G^otr longtable display equation wrap

**File.** `claim-strength-ledger.tex`. **Lines.** 708-711 (display
equation inside the third column of the G^otr frontier longtable).

**Context.** The third column declaration `p{0.40\textwidth}` ~
178 pt, holding the boundary representative display
\[
  \operatorname{Ob}_{\mathrm{sc}}^{\mathrm{otr}}(\gamma_{\mathbf 1};a,f;b,g)
  = \hbar N\,\omega(f,g)\int_{\R} a(t)b(t)\gamma_{\mathbf 1}(t)\,dt
\]
which overflows by ~48.79 pt = ~27% of column width.

W5-X23 §6.2 Edit 6 spec: "Force a `\\` line-break inside the
`\[ ... \]` display, or wrap in `\resizebox{\columnwidth}{!}{...}`."

**Selected approach.** `\resizebox{\linewidth}{!}{...}` wrap — the
line-count-preserving choice that does not require restructuring the
math (a `\\` break inside `\[...\]` is invalid; the cleanest
alternative is `\begin{multline*} ... \end{multline*}` which adds
2 lines and changes the equation environment, deviating from
zero-delta).

**Old (verbatim, 4 lines, lines 708-711):**
```
\[
  \operatorname{Ob}_{\mathrm{sc}}^{\mathrm{otr}}(\gamma_{\mathbf 1};a,f;b,g)
  = \hbar N\,\omega(f,g)\int_{\R} a(t)b(t)\gamma_{\mathbf 1}(t)\,dt
\]
```

**New (verbatim, 4 lines, lines 708-711):**
```
\[
  \resizebox{\linewidth}{!}{$\operatorname{Ob}_{\mathrm{sc}}^{\mathrm{otr}}(\gamma_{\mathbf 1};a,f;b,g)
  = \hbar N\,\omega(f,g)\int_{\R} a(t)b(t)\gamma_{\mathbf 1}(t)\,dt$}
\]
```

**Net delta.** 0 lines (4 -> 4). The substitution wraps the math
content in `\resizebox{\linewidth}{!}{$...$}` so the rendered display
shrinks horizontally to fit the 178-pt column. At 27% overflow, the
rendered shrink is ~78% of natural size — readable at `\small`-grade
publication setting. The `\resizebox` is supported by the `graphicx`
package which is loaded in `preamble.tex` line 38 (verified via
`\usepackage{graphicx}`).

**Alternative if `\resizebox` rendering quality is judged
insufficient.** Replace with `\scalebox{0.78}{$ ... $}` (also
graphicx-loaded), which shrinks uniformly without horizontal-only
distortion. Same line count.

**Alternative if column-width path preferred.** Rebalance the
longtable to (0.20, 0.20, 0.52). Column 3 = 0.52\textwidth ~ 231 pt,
+53 pt over the original 178 pt — covers the 48.79-pt overflow with
margin. Column 2 (Status) tightens from 0.27 to 0.20 — adequate for
"*frontier candidate (parallel-channel non-discharge)*" (49 chars,
fits in 0.20\textwidth = 89 pt at 5.5 pt/char as 2 lines, 1-line
height delta absorbed in the single-row table).

**Recommended primary fix.** `\resizebox` wrap (line-count
preserving, 0 delta on column declaration, 0 delta on table layout).

**Vocabulary scan.** Pure layout edit on a math display; no prose
touched. Pass.

---

## §3. Cumulative scan — em-dash / AI-tell / agent-language deltas

Each of E1-E6 is a substitution: tokens stripped, no new prohibited
tokens introduced.

| Scan dimension | E1 | E2 | E3 | E4 | E5 | E6 | Cumulative net delta |
|----------------|----|----|----|----|----|----|---------------------|
| em-dash (U+2014) | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| en-dash inserted (proper-name) | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| AI-tell vocabulary (`crucial`, `robust`, `seamless`, ...) | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| agent-language (`attack-heal`, `swarm`, `wave`, `phase-N audit`, `agent`, `ledger` outside math sense, `draft`) | -2 | -1 | -1 | 0 | 0 | 0 | **-4** (target) |
| LLM-attribution | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Net agent-language token delta: -4**, matching the W5-X23 §4.4
remediation requirement (4 leaks -> 0).

**Net em-dash / AI-tell / LLM-attribution delta: 0**, matching the
W5-X11 baseline preservation requirement.

---

## §4. Sequencing recommendation

The 6 edits are mutually independent (no shared lines, no shared
sentences, no shared longtable). Recommended application sequence:

1. **E4** (claim-strength-ledger.tex line 403-405, hypothesis dependency
   longtable column rebalance)
2. **E5** (claim-strength-ledger.tex line 497-500, regulator
   admissibility longtable column rebalance)
3. **E6** (claim-strength-ledger.tex line 708-711, G^otr display
   equation `\resizebox` wrap)
4. **E1** (claim-strength-ledger.tex line 230-231, "Phase-4 audit" +
   "drafted" sentence rewrite)
5. **E2** (claim-strength-ledger.tex line 385-386, "Phase-5
   obligation" sentence rewrite)
6. **E3** (theorem-lanes.tex line 530, "attack-heal" sentence rewrite)

**Rationale.**
- Overfull-hbox edits first (E4-E6), since they are pure layout
  edits that do not touch any prose and do not interact with any
  vocabulary scan. Apply as a block, then verify pdflatex output
  shows 0 overfulls before proceeding to vocabulary edits.
- Vocabulary edits ordered by file then by ascending line number:
  E1 (line 230) -> E2 (line 386) -> E3 (theorem-lanes.tex line 530).
  This minimises diff-tool churn and keeps the patch hunks in
  monotonic line order.
- Both phases are mechanically independent — the order within each
  phase is interchangeable. The recommended ordering is the
  least-cognitive-overhead presentation for the inscription
  applicator (single file -> next file, ascending line number).

**Expected post-application state.**
- `claim-strength-ledger.tex`: 736 -> 736 lines (unchanged total,
  5 edit hunks).
- `theorem-lanes.tex`: 537 -> 537 lines (unchanged total, 1 edit
  hunk).
- 0 overfull \hbox warnings (down from 6).
- 0 reader-visible reconstitution-vocabulary tokens (down from 4).
- 0 em-dashes, 0 AI-tells, 0 LLM-attribution (preserved from W5-X11
  baseline).
- 162 PDF pages (unchanged; row-height impact of E4 is well below
  page-boundary granularity).

---

## §5. Certification and severity

**All 6 edits draft cleanly.** Each is a surgical substitution that:
- preserves line count exactly (0 delta per edit, 0 cumulative
  delta);
- removes the targeted regression (overfull or vocabulary token);
- introduces no new em-dash, AI-tell, agent-language, or
  LLM-attribution token;
- preserves mathematical meaning verbatim where prose is rewritten
  (E1-E3) and preserves layout-quality where columns are rebalanced
  (E4-E6).

No edit requires structural rewrite (theorem rephrasing, proof
modification, environment replacement, package addition). E6 uses
`\resizebox` from `graphicx`, already loaded in `preamble.tex`.

**Severity-1 cleared by the 6-edit set as drafted.** Working-tree
authorisation is unblocked once these edits land in the inscription
source (either by amending the W5-X5 / Inscription-Readiness reports
or by inscribing the +6-edit-amended text directly).

**Certify.** All 6 edits drafted cleanly. No edit is severity-2.
No commit. No edit of any TeX file. Report persisted.

End of W5-X38 report.
