# Phase 4 EXEC — Editorial Inscription Specimen 2 — HKR Citation Pin (P4-EXEC-G6-S02)

**Date.** 2026-04-28.
**Initiator.** Phase-4 G6 execution agent (second editorial inscription
specimen).
**Lens.** Polyakov + Form. Polyakov supplies source-citation
discipline: a load-bearing algebraic identity on the brane side (the
Hochschild-cochain $\simeq$ polyvector identification on the
Tate-completed graded-commutative algebra $\widehat{\mathbf
S}(\mathfrak h_I)$) must be traced to the named primary theorem
rather than left as folklore. Form supplies the cotangent-form
discipline: the polyvector identification with Schouten bracket on
$\widehat{\mathbf S}(\mathfrak h_I)\widehat\otimes
\widehat{\mathbf S}(\mathfrak h_{I,\mathrm{cont}}^{\vee}[-1])$
must be pinned to classical HKR plus the windowwise Tate lift. Both
lenses converge on the W3-W17 finding: the manuscript silently
transfers classical HKR from finitely generated smooth
$\C$-algebras to a Tate-completed cosheaf-of-Lie evaluation; the
heal pins the windowwise classical statement (Hochschild–Kostant–
Rosenberg, Trans. AMS 102, 1962, Theorem 5.2) and lifts to the Tate
completion via Lurie HA Theorem 5.5.3.18 plus
`\lem:continuous-bar-cobar` Item 2.
**Mode.** PROPOSAL-ONLY. New IDs prefix `P4-EXEC-G6-`.
**Purpose.** Apply the §4.4 5-step scrub of the G6 editorial roadmap
to a citation-injection cluster: the three HKR pins at `main.tex`:2056,
2132, 2202 (W3-W17-01..03) plus the missing `\bib{hkr}{}` entry
(W3-W17-04). Companion to the first G6 specimen
(`phase4-exec-editorial-specimen-2026-04-28.md`, M-03 prose
insertion). The first specimen demonstrated structural-prose
insertion; this one demonstrates citation-pin injection. Differences
catalogued in §7.

---

## §1. T1 — Verbatim source draft prose and proposed citation pin

**Edit IDs (cluster).**
- P4-EXEC-G6-S02a (= P4-G6-02 = W3-W17-01): `main.tex`:2056 pin.
- P4-EXEC-G6-S02b (= P4-G6-03 = W3-W17-02): `main.tex`:2132 pin.
- P4-EXEC-G6-S02c (= P4-G6-04 = W3-W17-03): `main.tex`:2202 pin.
- P4-EXEC-G6-S02d (= P4-G6-01 = W3-W17-04): new `\bib{hkr}{}` entry.

**Source ledger.** `reconstitution/wave3-W17-hkr-thmA-2026-04-28.md`
§T6.
**Source attackers.** W3-W17-01..04, M-01, W6-02.
**Severity.** 3 (citation-injection; closes the load-bearing
primary-source gap noted by M-01 across three sites + adds the
missing `\bib{}` entry).

### §1.1 Verbatim source prose at the three pin sites

**Site 1: `main.tex`:2056 (Theorem E proof, Step 1).** Verbatim
from current state (lines 2049–2064):

```
\begin{proof}
  \emph{Step 1.} Identify the interval-wise central factorization
  algebra. ... is graded-commutative, with strict $P_0$ bracket
  inherited from $\mathfrak h_I$ as a biderivation. By the
  Hochschild--Kostant--Rosenberg theorem in the smooth/algebraic
  setting, applied here to the free graded-commutative algebra on
  the Tate vector space $\mathfrak h_I$, the Hochschild cochain
  complex ... is quasi-isomorphic to the polyvector fields ... with
  the Schouten bracket.
```

Pin target: insert one parenthetical sentence after "in the
smooth/algebraic setting" (line 2057).

**Site 2: `main.tex`:2132 (Theorem E proof, Step 5).** Verbatim from
lines 2127–2138:

```
  \emph{Step 5.} Quasi-isomorphism on each interval. ... with the
  same CE differential induced from the semidirect Lie bracket of
  $\mathfrak g_I$ (closed side: by definition; brane side: through
  the HKR identification of Step 1 and the Schouten bracket). ...
```

Pin target: replace "the HKR identification of Step 1" by "the
windowwise HKR + Lurie HA identification of Step 1".

**Site 3: `main.tex`:2202 (`\rmk:E1-translation`).** Verbatim from
lines 2193–2210:

```
\begin{rmk}[Locally constant equivalence and $E_1$-algebra
translation]\label{rmk:E1-translation}
  ... For graded-commutative $E_1$ algebras (which the open
  Hamiltonian stalk is, in the reduced model), the Hochschild
  cochain complex is quasi-isomorphic to polyvector fields by
  HKR, and its strict $P_0$ subalgebra ...
\end{rmk}
```

Pin target: replace "by HKR" with the named primary-source
parenthetical.

### §1.2 Canonical citation pin (reused across sites)

The W3-W17 audit identifies the closure path as **(i) classical HKR
in finite-dimensional Tate windows + (ii) windowwise lift via
`\lem:continuous-bar-cobar` Item 2 + (iii) Lurie HA Theorem 5.5.3.18
for the locally constant `E_1`-factorization-`E_1`-algebra
equivalence**. This canonical form is reused verbatim with light
parenthetical adaptation at each site.

### §1.3 Proposed `\bib{}` entry (W3-W17-04)

```latex
\bib{hkr}{article}{
   author={Hochschild, G.},
   author={Kostant, B.},
   author={Rosenberg, A.},
   title={Differential forms on regular affine algebras},
   journal={Trans. Amer. Math. Soc.},
   volume={102},
   date={1962},
   pages={383--408},
   doi={10.1090/S0002-9947-1962-0142598-8},
}
```

---

## §2. T2 — The 5-step process-tag scrub, applied to each insertion

**Common audit across all four units.** Steps 1–4 are uniformly
no-op for this cluster (the W17 source draft is already at
manuscript-prose register: no scaffolding tags, no em-dashes, no
hedges, no passive narration). Step 5 (named-attribution audit) is
the load-bearing step; it passes for all four units. Per-insertion
detail follows.

### §2.1 Insertion 1 — `main.tex`:2056 pin (P4-EXEC-G6-S02a)

- **Step 1 (process tags).** Hits: zero. The W17 §T6 W3-W17-01 draft
  is a single parenthetical pin without ledger pointers. **No-op.**
- **Step 2 (em-dashes).** Zero. The triple "Hochschild–Kostant–
  Rosenberg" uses en-dashes (typographical convention), rendered in
  LaTeX as `--`. **No-op.**
- **Step 3 (hedges).** Zero. **No-op.**
- **Step 4 (voice).** Zero. The participle "lifted to the Tate-
  completed cosheaf-of-Lie evaluation by the windowwise inverse
  limit" is acceptable in citation-pin register: the construction
  is the agent. **No-op.**
- **Step 5 (attribution).** **Pass.** Three named pins on a single
  parenthetical: `\cite{hkr}*{Theorem 5.2}`, `\cite{lurie-ha}*{Theorem
  5.5.3.18}`, `\ref{lem:continuous-bar-cobar}`. The "in finite-
  dimensional Tate windows" qualifier explicitly marks the
  hypothesis-domain (where classical HKR applies) and discloses
  the windowwise Tate lift honestly.

#### §2.1.1 Final inscribable pin for `main.tex`:2056 (boxed)

```latex
+--------------------------------------------------------------------+
|                                                                    |
|   ... is graded-commutative, with strict $P_0$ bracket inherited   |
|   from $\mathfrak h_I$ as a biderivation. By the                   |
|   Hochschild--Kostant--Rosenberg theorem in the smooth/algebraic   |
|   setting (\cite{hkr}*{Theorem 5.2}, in finite-dimensional Tate    |
|   windows; lifted to the Tate completion by the windowwise         |
|   inverse limit using \ref{lem:continuous-bar-cobar} Item 2 and    |
|   \cite{lurie-ha}*{Theorem 5.5.3.18} for the locally constant      |
|   $E_1$-factorization--$E_1$-algebra equivalence), applied here    |
|   to the free graded-commutative algebra on the Tate vector        |
|   space $\mathfrak h_I$, the Hochschild cochain complex ...        |
|                                                                    |
+--------------------------------------------------------------------+
```

Notes: amsrefs `\cite{...}*{...}` substring convention matches
`\cite{costello-gwilliam}*{Vol.~I \S 6.4}` at line 2198.
`\ref{lem:continuous-bar-cobar}` resolves at `main.tex`:3370.

### §2.2 Insertion 2 — `main.tex`:2132 pin (P4-EXEC-G6-S02b)

- **Step 1.** Zero process tags in the W17 W3-W17-02 substring
  substitution. **No-op.**
- **Steps 2–4.** No-op.
- **Step 5.** **Pass.** "windowwise HKR + Lurie HA identification of
  Step 1" inherits the full named-attribution pinned at Insertion
  1; the back-reference to "Step 1" is sufficient for the second
  occurrence within the same proof.

#### §2.2.1 Final inscribable pin for `main.tex`:2132 (boxed)

In-place substring substitution within the existing parenthetical:

```latex
+--------------------------------------------------------------------+
|                                                                    |
|  ... with the same CE differential induced from the semidirect     |
|  Lie bracket of $\mathfrak g_I$ (closed side: by definition;       |
|  brane side: through the windowwise HKR + Lurie HA                 |
|  identification of Step 1 and the Schouten bracket). The map       |
|                                                                    |
+--------------------------------------------------------------------+
```

The substring "the HKR identification of Step 1" → "the windowwise
HKR + Lurie HA identification of Step 1". Surrounding sentence
unchanged.

### §2.3 Insertion 3 — `main.tex`:2202 pin (P4-EXEC-G6-S02c)

- **Step 1.** Zero process tags in the W17 W3-W17-03 substitution.
  **No-op.**
- **Steps 2–4.** No-op. The remark uses the indicative active.
- **Step 5.** **Pass.** Three named pins on the substitution
  parenthetical: `\cite{hkr}*{Theorem 5.2}`, `\cite{lurie-ha}*{Theorem
  5.5.3.18}`, `\cite{costello-gwilliam-vol2}*{\S 3}`. Two equivalent
  closure routes named (windowwise inverse limit vs. Lurie+CGW2
  stalk); reader can verify either. The
  `\bib{costello-gwilliam-vol2}{}` entry exists at line 6110.

#### §2.3.1 Final inscribable pin for `main.tex`:2202 (boxed)

```latex
+--------------------------------------------------------------------+
|                                                                    |
|  ... For graded-commutative $E_1$ algebras (which the open         |
|  Hamiltonian stalk is, in the reduced model), the Hochschild       |
|  cochain complex is quasi-isomorphic to polyvector fields          |
|  (\cite{hkr}*{Theorem 5.2}, in finite-dimensional Tate windows;    |
|  for the $\widehat{\mathbf S}$ completion on a Tate vector space   |
|  take the windowwise inverse limit, or equivalently use            |
|  \cite{lurie-ha}*{Theorem 5.5.3.18} together with the              |
|  Hochschild-centre stalk computation of                            |
|  \cite{costello-gwilliam-vol2}*{\S 3}), and its strict $P_0$       |
|  subalgebra of multiplication operators ...                        |
|                                                                    |
+--------------------------------------------------------------------+
```

The substring "by HKR" → the parenthetical citation block.
Surrounding sentence ("...quasi-isomorphic to polyvector fields ...
and its strict $P_0$ ...") preserved.

### §2.4 Insertion 4 — `\bib{hkr}{}` entry (P4-EXEC-G6-S02d)

- **Steps 1–4.** N/A or no-op (bibliography metadata).
- **Step 5.** **Pass.** Author triple, title, journal, volume, year,
  page range, doi all verified against the published Trans. AMS 102
  (1962), 383–408 record. Field order matches `\bib{loday-quillen}{}`
  (lines 5941–5950) and `\bib{kontsevich-dq}{}` (lines 6010–6021).

(Final inscribable form reproduced in §4 below.)

---

## §3. T3 — Voice check vs CLAUDE.md (Polyakov + Form lens)

Each insertion is checked against Russian-school discipline,
named-attribution, declarative form, and honest epistemic status.

**Insertion 1 (line 2056).** Declarative ("the Hochschild cochain
complex ... is quasi-isomorphic to ..."); three named pins on a
single parenthetical (`\cite{hkr}*{Theorem 5.2}`,
`\cite{lurie-ha}*{Theorem 5.5.3.18}`, `\ref{lem:continuous-bar-cobar}`);
concrete construction-handles ("finite-dimensional Tate windows",
"windowwise inverse limit", "locally constant `E_1`-factorization-
`E_1`-algebra equivalence"); honest epistemic status (the windowed
qualifier discloses where classical HKR applies vs. where the lift
is needed). **Pass.**

**Insertion 2 (line 2132).** Declarative noun phrase ("the
windowwise HKR + Lurie HA identification of Step 1"); inherits full
named-attribution from Insertion 1 (Russian-school + amsrefs
convention does not require re-pinning at every back-reference within
a single proof). **Pass.**

**Insertion 3 (line 2202).** Declarative ("the Hochschild cochain
complex is quasi-isomorphic to polyvector fields ..."); three named
pins; two equivalent closure routes named (windowwise inverse limit
vs. Lurie+CGW2 stalk); honest epistemic status. **Pass.**

**Insertion 4 (`\bib{hkr}{}`).** N/A (bibliography metadata);
field-order consistency confirmed against existing entries. **Pass.**

**Process-leakage post-scan.** After Step-1 scrub, post-scrub text
contains zero instances of `wave`, `swarm`, `agent`, `ledger`, `M-XX`,
`W3-WXX-YY`, `P4-G6-XX`, `R-W3-WXX`, `attacker`, `worker`. Verified
by inspection of the four boxed final inscribable forms in §2.

**Russian-school + Polyakov + Form lens summary.** Each pin names
the primary theorem (HKR 1962, Theorem 5.2), the lift theorem (Lurie
HA Theorem 5.5.3.18), and the manuscript-internal mediating lemma
(`\lem:continuous-bar-cobar` Item 2). The Polyakov-lens interpretation: the
brane-side Hochschild $\simeq$ polyvector identification is the named
algebraic backbone of the open-closed derived-centre theorem; the
Form-lens interpretation: the Schouten bracket on the polyvector side is
the cotangent-Poisson avatar paired against the CE differential on
the closed side. Both lenses converge on the W17 closure path.

---

## §4. T4 — `\bib{hkr}{}` entry (boxed, ready to inscribe)

```latex
+--------------------------------------------------------------------+
|                                                                    |
| \bib{hkr}{article}{                                                |
|    author={Hochschild, G.},                                        |
|    author={Kostant, B.},                                           |
|    author={Rosenberg, A.},                                         |
|    title={Differential forms on regular affine algebras},          |
|    journal={Trans. Amer. Math. Soc.},                              |
|    volume={102},                                                   |
|    date={1962},                                                    |
|    pages={383--408},                                               |
|    doi={10.1090/S0002-9947-1962-0142598-8},                        |
| }                                                                  |
|                                                                    |
+--------------------------------------------------------------------+
```

**Placement (recommended).** After `\bib{tsygan}{}` (ends line 5961),
before `\bib{witten-cs}{}` (begins line 5963). The `\bib{tsygan}{}`
title also names "Hochschild homology", clustering the two entries
in the Hochschild block. Insertion as new lines 5962a..5962j with a
trailing blank line.

**Citation key rationale.** `hkr` matches the W17 §T6 W3-W17-04
draft; short and conventional, matching the
`bcov`/`tsygan`/`lurie-ha` short-key style.

---

## §5. T5 — Inscription-time conflict check (Bash grep)

### §5.1 Line-number context verification

```bash
sed -n '2050,2056p; 2128,2134p; 2196,2206p' \
    /Users/raeez/topological-strings/main.tex
```

Verifies:
- Line 2056: "Hochschild--Kostant--Rosenberg theorem in the
  smooth/algebraic" — pin target.
- Line 2132: "(closed side: by definition; brane side: through
  the HKR" — confirms "the HKR identification of Step 1" spans
  lines 2132–2133.
- Line 2202: "quasi-isomorphic to polyvector fields by HKR" —
  pin target.

All three target lines verified.

### §5.2 No existing `\bib{hkr}{}` entry

```bash
grep -n "hkr\|hochschild\|kostant\|rosenberg" \
    /Users/raeez/topological-strings/main.tex
```

Returns 17 prose-level hits (per W17 §T1); zero `\bib{hkr}{}` or
`\bib{hochschild-...}{}` or `\bib{kostant-...}{}` entries. Insertion
of P4-EXEC-G6-S02d is the first occurrence.

### §5.3 Bibliography placement slot

```bash
grep -n "^\\\\bib{" /Users/raeez/topological-strings/main.tex | head -10
```

Output:
```
5926:\bib{bcov}{article}{
5941:\bib{loday-quillen}{article}{
5952:\bib{tsygan}{article}{
5963:\bib{witten-cs}{article}{
5978:\bib{gwilliam-williams-holomorphic-bosonic-string}{article}{
...
```

The `\bib{tsygan}{}` block runs lines 5952–5961; line 5962 is
blank; `\bib{witten-cs}{}` begins line 5963. Slot at 5962 is vacant
and suitable.

### §5.4 Verdict

Inscription has zero conflicts at all four targets. The four
insertion units are inscription-ready.

---

## §6. T6 — Three-line authorization template

```
+--------------------------------------------------------------------+
|                                                                    |
| Authorize inscription of P4-EXEC-G6-S02a/b/c (HKR citation pins    |
| at main.tex:2056, 2132, 2202) per                                  |
| phase4-exec-editorial-specimen-2-HKR-2026-04-28.md §2.1.1, §2.2.1, |
| §2.3.1.                                                            |
|                                                                    |
| Authorize inscription of P4-EXEC-G6-S02d (\bib{hkr}{} entry) at    |
| main.tex line 5962, between \bib{tsygan} and \bib{witten-cs},      |
| per §2.4.1 / §4.                                                   |
|                                                                    |
| Order of inscription: \bib{hkr}{} first (no dependencies), then    |
| the three pin insertions (each cites \bib{hkr}{} via               |
| \cite{hkr}*{Theorem 5.2}).                                         |
|                                                                    |
+--------------------------------------------------------------------+
```

The three lines correspond to: (a) the three pin insertions as a
unit (shared canonical form; inscribe together for consistency); (b)
the `\bib{hkr}{}` entry, independently authorizable; (c) the
dependency note: amsrefs resolves `\cite{hkr}*{}` only after the
`\bib{hkr}{}` entry is in scope.

---

## §7. T7 — Cross-walk with the first G6 specimen (P4-EXEC-G6-S01)

The first G6 specimen
(`phase4-exec-editorial-specimen-2026-04-28.md`, P4-EXEC-G6-S01)
inscribed the M-03 derived-intersection remark — a structural-prose
insertion adding a new bold-leadered paragraph (plan-Markdown) and a
new `\begin{rmk}[Derived intersection]` block (manuscript LaTeX).
The present specimen (P4-EXEC-G6-S02) is a citation-injection
cluster: three in-place phrase substitutions plus one `\bib{}`
entry. The same 5-step §4.4 scrub applies to both, but the
characteristic patterns differ.

### §7.1 Difference table

| Dimension | S01 (M-03 prose) | S02 (HKR pin) |
|-----------|--------------------|------------------|
| **Edit type** | New paragraph / new `\begin{rmk}` block | In-place substring substitution × 3 + new `\bib{}` |
| **Insertion size** | ~150 words new prose; ~25 LaTeX lines | ~30 words across 3 sites; ~10 LaTeX lines for `\bib{}` |
| **Source** | W3-W27-01 / W3-W13-5 / M-03 | W3-W17-01..04 / M-01 / W6-02 |
| **Step 1** | Stripped `(M-03 / W3-W27-01)` leading and `(W3-W10-02)` embedded | No-op |
| **Steps 2–4** | No-op | No-op |
| **Step 5** | 4 named pins (Motzkin–Taussky 1955; Gerstenhaber 1961; Vasconcelos 1994; Premet 2003) + script paths | 3 named pins per insertion (HKR 1962; Lurie HA; CGW2) |
| **Bib entries** | 1 new (`premet-nilpotent-commuting`) + 3 companion drafts | 1 new (`hkr`); reuses existing `lurie-ha`, `costello-gwilliam-vol2` |
| **Conflict checks** | Empty grep × 3 | Filled grep × 1 (17 prose hits, no `\bib`), empty grep × 1 (no `\bib{hkr}`), placement-slot vacant |
| **Authorization** | 3 lines: plan-Markdown + Premet `\bib{}` + deferred LaTeX | 3 lines: 3 pins + `\bib{hkr}{}` + ordering |

### §7.2 Why the same 5-step scrub adapts to both

The 5-step scrub is the **citation-into-Russian-school-prose
projection**: it maps any source-ledger draft (which carries
process-tag scaffolding by construction) onto a manuscript-prose
form. In S01 the projection is non-trivial at Step 1 (two scaffolding
tags stripped). In S02 the projection is trivial at Step 1: the
W17 draft was already authored at the manuscript-prose register
(single-sentence citation pins, not a multi-paragraph remark with
internal cross-references to other sub-ledger entries).

Shared pattern: Step 1 (process tags) discriminates ledger-internal
scaffolding from inscribable prose. Step 2 (em-dashes) enforces the
no-em-dash commit-history rule (commit `bc41359`). Step 3 (hedges)
enforces the declarative-active register. Step 4 (voice) enforces
Russian-school active voice; the citation-pin register (S02) admits
noun-phrase forms not present in the paragraph-prose register (S01).
Step 5 (attribution) is the load-bearing audit.

### §7.3 New patterns demonstrated by S02

1. **Citation-pin canonical form reuse.** The W3-W17 pins share a
   canonical form (HKR Theorem 5.2 windowwise + Lurie HA Theorem
   5.5.3.18 + `\lem:continuous-bar-cobar`); the 5-step scrub is run
   once per site to verify the canonical form adapts to each site's
   grammatical context (parenthetical inside prose at site 1,
   substring substitution within an existing parenthetical at site
   2, substring substitution within a remark sentence at site 3).
2. **Bib-entry inscription as a separate scrub unit.** The `\bib{}`
   entry runs the 5-step scrub trivially (Steps 1–4 no-op; Step 5
   verifies bibliographic-data correctness). This pattern will recur
   for the P4-G6-06..21 dictionary entries (sixteen entries, each
   requiring a Step-5 audit of the symbol / formula / cross-reference
   triple).

### §7.4 Adaptation rules for future specimens

For future P4-EXEC-G6-S03..N specimens covering the remaining 47
Tier-A edits:

- **Step 1** is non-trivial whenever the source is a multi-paragraph
  wave-3 sub-ledger entry (W27, W28, W32 master plan); typically
  trivial when the source is a single-sentence pin (W17, much of
  W20).
- **Step 2** is non-trivial only when the source contains em-dashes
  (W17 / W20 / W27 are em-dash-free; W32 has at least one em-dash
  flagged in the G6 roadmap §4.2).
- **Step 5** is the audit step, always load-bearing. For
  citation-injection specimens (HKR-class), Step 5 is the only
  load-bearing step. For prose-insertion specimens (M-03-class),
  Steps 1 and 5 are co-load-bearing.

---

## §8. Specimen completeness ledger

| Item | Status | Notes |
|------|--------|-------|
| T1 — Verbatim source draft prose | Complete | §1.1 verbatim from `main.tex`; §1.2 canonical pin; §1.3 bib entry. |
| T2 — 5-step scrub, four units | Complete | §2.1–§2.4. Steps 1–4 no-op; Step 5 pass. |
| T3 — Voice check | Complete | §3 Russian-school + Polyakov + Form lens; process-leakage zero. |
| T4 — `\bib{hkr}{}` entry | Complete | §4 boxed; placement at line 5962. |
| T5 — Conflict check | Complete | §5.1–§5.3; zero conflicts. |
| T6 — Authorization template | Complete | §6: pins + bib + ordering. |
| T7 — Cross-walk with first specimen | Complete | §7 difference table + adaptation rules. |

---

## §9. Provenance and lens-cross-walk

**Polyakov + Form convergence.** Polyakov supplies source-citation
discipline: classical HKR (1962, finitely generated smooth $\C$-
algebras) is not the same theorem as the manuscript's appeal
(Tate-completed graded-commutative algebra on a cosheaf-of-Lie
evaluation); the difference is load-bearing and must be pinned.
Form supplies cotangent-form discipline: the polyvector
identification $\widehat{\mathbf S}(\mathfrak h_I)\widehat\otimes
\widehat{\mathbf S}(\mathfrak h^{\vee}_{I,\mathrm{cont}}[-1])$ with
Schouten bracket is the cotangent-form side of the Hochschild-
cochain complex; the Schouten bracket is the cotangent-Poisson
avatar that the open-closed derived-centre theorem matches against
the CE differential on the closed side. Both lenses converge on the
W3-W17 closure path: classical HKR in finite-dimensional Tate
windows + `\lem:continuous-bar-cobar` Item 2 (windowwise inverse
limit) + Lurie HA Theorem 5.5.3.18 (locally constant `E_1`-
factorization-`E_1`-algebra equivalence).

**Wave-3 cross-confirmation.** Specimen prose from W3-W17 §T6
(W17 attacker draft). Cross-confirmed against:
- HKR primary source: *Trans. AMS* 102 (1962), 383–408, Theorem 5.2
  (verified by W17 §T2 hypothesis-by-hypothesis audit).
- Lurie *Higher Algebra*, Theorem 5.5.3.18 (existing
  `\bib{lurie-ha}{}` at line 6326).
- Costello–Gwilliam Vol II §3 (existing `\bib{costello-gwilliam-vol2}{}`
  at line 6110).

**Files read in full.**
- `/Users/raeez/topological-strings/CLAUDE.md`.
- `/Users/raeez/topological-strings/reconstitution/phase4-G6-editorial-roadmap-2026-04-28.md`.
- `/Users/raeez/topological-strings/reconstitution/wave3-W17-hkr-thmA-2026-04-28.md`.
- `/Users/raeez/topological-strings/reconstitution/phase4-exec-editorial-specimen-2026-04-28.md`.

**Files inspected (relevant excerpts).**
- `/Users/raeez/topological-strings/main.tex` lines 2040–2260
  (Theorem E proof region, all three HKR pin sites);
  lines 5926–6358 (bibliography section).

---

## §10. 200-word summary

The Phase-4 EXEC second G6 specimen takes the W3-W17 HKR audit
findings and applies the §4.4 5-step scrub to four insertion units:
three citation-pin substitutions at `main.tex`:2056 (Theorem E proof
Step 1), `main.tex`:2132 (Step 5), and `main.tex`:2202
(`\rmk:E1-translation`); plus one new `\bib{hkr}{}` entry between
`\bib{tsygan}{}` (line 5961) and `\bib{witten-cs}{}` (line 5963). T1
quotes the verbatim source prose at all three pin sites and the
canonical pin form (HKR Theorem 5.2 windowwise + Lurie HA Theorem
5.5.3.18 + `\lem:continuous-bar-cobar`). T2 runs Steps 1–5 on each
of the four units: Steps 1–4 no-op (the W17 draft is at
manuscript-prose register, em-dash-free, hedge-free, declarative);
Step 5 audits and passes all named-attribution claims. T3 confirms
Russian-school + Polyakov + Form-lens + honest-epistemic-status
discipline; process-leakage post-scan zero. T4 boxes the `\bib{hkr}{}`
entry. T5 runs three Bash conflict checks (line-number verification,
no prior bib entry, placement slot vacant); zero conflicts. T6
supplies the three-line authorization template (pins cluster + bib
+ ordering). T7 cross-walks against the first G6 specimen (M-03
prose), tabulating where the citation-injection pattern (S02) differs
from the structural-prose pattern (S01) and naming the adaptation
rules for future specimens. PROPOSAL-ONLY; nothing inscribed.

---

End of P4-EXEC-G6-S02 editorial inscription specimen (Polyakov + Form
lens; 2026-04-28).
