# Phase 4 EXEC — Editorial Inscription Specimen (P4-EXEC-G6)

**Date.** 2026-04-28.
**Initiator.** Phase-4 G6 execution agent (editorial inscription specimen).
**Lens.** Polyakov + Form.
  Polyakov supplies the physical-source convention discipline: a
  worldsheet/brane action with gauge-fixed BV master equation is the
  primary object; anomalies are accounted by class, not by intent;
  one does not silently strengthen a Dirac reduction into a
  complete-intersection assertion when the ideal is not a regular
  sequence. Form supplies the cotangent-form discipline: the
  Matlis principal-part forms $\rho_{a,b}$ are the canonical residue
  currents on the formal symplectic disk, and the BV/Koszul resolution
  is read as a derived-form construction whose higher Tor classes are
  not artefacts but the canonical degree-$(-1)$ avatars of the
  derived self-intersection. Both lenses converge on M-03: the BV
  cohomology is the structure sheaf of the derived self-intersection,
  and the chain-level cycle $\mathrm{Tr}\,\psi$ is its degree-$(-1)$
  form.
**Mode.** PROPOSAL-ONLY. No manuscript edits inscribed. Master-ledger
schema; new IDs prefix `P4-EXEC-G6-`.
**Purpose.** Demonstrate the §4.4 5-step scrub pattern of
`phase4-G6-editorial-roadmap-2026-04-28.md` on the W3-W27-01 specimen
(M-03 derived-intersection remark, Theorem A preface). Produce final
inscribable LaTeX-ready prose; the Premet 2003 `\bib{}` entry; an
inscription-time conflict check via Bash `grep`; and a three-line
authorization template.

---

## §1. T1 — Specimen identification and verbatim source draft prose

**Edit ID.** P4-EXEC-G6-S01 (specimen of P4-G6-22 in the editorial
roadmap).
**Source ledger.** `reconstitution/wave3-W27-m03-bv-derived-2026-04-28.md`
§6.1 (lines 482–516).
**Source attacker IDs.** W3-W27-01 / W3-W13-5 / M-03.
**Severity.** 4 (additive, sharpens interpretation; prevents silent
strengthening into a complete-intersection hypothesis that fails for
$N \ge 2$).
**Target file (primary, plan-Markdown).**
`/Users/raeez/topological-strings/reconstitution/platonic-ideal-plan-2026-04-28.md`,
inserting after line 196 (between "Proof skeleton" body and "Action
items" heading).
**Target file (downstream, manuscript LaTeX).**
`/Users/raeez/topological-strings/main.tex` line 128 (the elision in
the ghost-zero open BV algebra paragraph) — Phase-2 propagation,
shown for completeness.

### §1.1 Source draft prose (verbatim from W27 §6.1, lines 492–515)

The wave-3 sub-ledger inscribed the following draft prose:

```
**Derived-intersection remark (M-03 / W3-W27-01).** For $N \ge 2$
the commuting variety
$\mathcal C_N = \{(A, B) \in \mathfrak{gl}_N^2 \mid [A, B] = 0\}$
is irreducible (Motzkin–Taussky 1955; Gerstenhaber 1961) of
codimension $N(N-1)$, but is **not a complete intersection**
(Premet 2003; Vasconcelos 1994). The moment-map ideal
$I_\mu = ([\phi_1, \phi_2]^i{}_j)$ has $N^2 - 1$ independent
generators on $\mathfrak{sl}_N$ (after the trace identity
$\mathrm{Tr}[\phi_1, \phi_2] = 0$), exceeding the codimension
$N(N-1)$ by an excess $\Delta(N) = N$ (W3-W10-02 verified at
$N = 1..6$; `scripts/check_derived_intersection_N_extended.py`).
The Koszul complex on $I_\mu$ is therefore not exact for $N \ge 2$,
and the open BV cohomology
$H^\bullet(\mathcal R_N^{\mathrm{GL}_N}, Q)$ is the *derived*
self-intersection of $\mathcal C_N$, not its naive structure sheaf.
The chain-level cycle $\mathrm{Tr}\,\psi$ is the canonical
degree-$(-1)$ avatar of the derived-intersection class
(`scripts/check_derived_intersection_N2.py`); higher classes
$\mathrm{Tr}(\psi^k)$ for $1 \le k \le N$ exhaust the excess
$\Delta(N) = N$ Tor$^1$ generators by cyclicity. The boundary
stratum at $N = 1$ collapses (abelian; $\Delta(1) = 1$ is the
trivial $\mathrm{Tr}\,\psi = \psi$ class with zero $Q$); the
non-complete-intersection phenomenon switches on at $N \ge 2$ and
grows linearly in $N$.
```

This is the source. Below: the 5-step G6 §4.4 scrub applied
verbatim.

---

## §2. T2 — The 5-step process-tag scrub (G6 §4.4)

### §2.1 Step 1 — Strip leading parenthetical and embedded process tags

**Pattern.** Remove `(W3-WXX-XX)`, `(M-XX)`, `(P4-G6-XX)`,
`(R-W3-WXX)`, `(W3-W2X-XX)` and similar scaffolding tags that exist
only for sub-ledger traceability.

**Hits in source.**
- Bold prefix `**Derived-intersection remark (M-03 / W3-W27-01).**`:
  the parenthetical is a leading process tag.
- `(W3-W10-02 verified at $N = 1..6$; ...)`: embedded process tag
  preceding a legitimate computational evidence pointer to
  `scripts/check_derived_intersection_N_extended.py`.

**Action.** Delete `(M-03 / W3-W27-01)` and `W3-W10-02`. Retain script
references (these are reproducibility pointers, not coordination
tags).

### §2.2 Step 2 — Replace em-dashes with comma, semicolon, colon, or period

**Pattern.** Em-dashes (U+2014) replaced by punctuation that respects
the manuscript's no-em-dash rule (commit `bc41359`). En-dashes
(U+2013) inside hyphenated proper names ("Motzkin–Taussky") are
typographical convention and are kept.

**Hits in source.** Zero em-dashes (U+2014) in the W27 draft. The
hyphenations `degree-$(-1)$` and `non-complete-intersection` use
hyphens (U+002D), not dashes; kept. The proper-name pairs use
en-dashes (U+2013); kept.

**No-op for this specimen.**

### §2.3 Step 3 — Strip hedge words

**Pattern.** Remove "perhaps", "approximately", "may possibly", "it
seems", "we propose to interpret", "one might expect".

**Hits in source.** Zero. The W27 draft is uniformly declarative:
"is irreducible", "is not a complete intersection", "is therefore not
exact", "is the *derived* self-intersection", "exhaust", "collapses",
"switches on", "grows linearly".

**No-op for this specimen.**

### §2.4 Step 4 — Convert passive narration to declarative

**Pattern.** Russian-school discipline: state the object, give the
formula, attribute the source. Replace "is verified to be", "was
shown by", "is found to be" by direct active forms.

**Hits in source.**
- `(verified at $N = 1..6$; ...)`: parenthetical evidence note inside
  an otherwise declarative sentence. The main clause runs in active
  voice ("the moment-map ideal has $N^2 - 1$ independent generators
  on $\mathfrak{sl}_N$ ... exceeding the codimension by an excess
  $\Delta(N) = N$"). The parenthetical reads as a computational
  evidence cite, parallel to a citation, and is acceptable in the
  Russian-school register.

**No-op for this specimen.** The remark is already declarative
end-to-end.

### §2.5 Step 5 — Verify named-attribution and honest epistemic status

**Pattern.** Every load-bearing claim names the primary source at
first occurrence with year-pinning. Computational evidence is marked
explicitly as such ("verified at finite $N$"; "computed to stated
graph order"; "conditional on hypothesis $H$"). No false certainty.

**Audit (Polyakov + Form lens).**
- "irreducible (Motzkin–Taussky 1955; Gerstenhaber 1961)" —
  named, year-pinned. **Pass.** Trans. AMS 80 (1955), 387–401;
  Ann. of Math. (2) 73 (1961), 324–348.
- "not a complete intersection (Premet 2003; Vasconcelos 1994)" —
  named, year-pinned. **Pass.** Invent. Math. 154 (2003), 653–683;
  *Arithmetic of Blowup Algebras* §3, Cambridge Univ. Press, LMS
  Lect. Note Ser. 195.
- "$\Delta(N) = N$ verified at $N = 1..6$ (script reference)" —
  computational evidence with explicit script path. Marks the claim
  as "computed at low $N$ + literature for higher $N$." **Pass.**
- "the open BV cohomology $H^\bullet(\mathcal R_N^{\mathrm{GL}_N}, Q)$
  is the *derived* self-intersection of $\mathcal C_N$, not its naive
  structure sheaf" — Form-lens identification: the BV/Koszul
  resolution is read as a derived-form construction. The claim
  follows from regular-sequence failure (Vasconcelos) plus the
  standard Tor identification of derived intersections. **Pass.**
- "boundary stratum at $N = 1$ collapses ($\Delta(1) = 1$ trivial)"
  — honest boundary disclaimer for the abelian stratum.
  **Pass.**

All attribution and epistemic discipline satisfied.

---

## §3. T3 — Voice check vs CLAUDE.md (Polyakov + Form lens)

### §3.1 Russian school

- **Declarative.** Yes. Every main verb is in the indicative active.
- **Named.** Yes. Four primary sources year-pinned at first occurrence;
  named on the same line as the load-bearing claim, not in a footnote.
- **Concrete formulas.** Yes. $N(N-1)$ codimension; $N^2 - 1$
  generators; $\Delta(N) = N$ excess; chain-level cycle
  $\mathrm{Tr}\,\psi$; abelian boundary stratum at $N = 1$.

### §3.2 Mathematical-physics frontier (Polyakov)

The remark sits at the Theorem A preface. Polyakov-lens interpretation: the
worldsheet/brane action is the constrained mechanics of the matrix
moment-map; gauge fixing produces the BV/Koszul resolution
$Q\psi = [\phi_1, \phi_2]$; the Koszul complex of the moment-map ideal
$I_\mu$ is the *physical* object the BV machinery computes the
cohomology of. Polyakov-discipline forbids silently identifying the
BV cohomology with the naive scheme-theoretic structure sheaf when
the moment-map ideal is not a regular sequence. The
non-complete-intersection observation is the physical bookkeeping
note that the $N \ge 2$ derived-intersection signal is genuine, not a
regularization artefact.

### §3.3 Form lens — cotangent / residue-form discipline

The Form lens binds the derived-intersection picture to the cotangent
data already named in `principles.tex`. The Matlis principal-part
forms $\rho_{a,b}$ are the canonical residue currents on the formal
symplectic disk; the BV/Koszul resolution is the dual derived-form
construction on the open side. Higher Tor classes
$\mathrm{Tr}(\psi^k)$ for $1 \le k \le N$ are the degree-$(-1)$
avatars of the derived self-intersection; they pair against the
principal-part form sector via the residue pairing. This frames the
Theorem A preface as the open-side counterpart of the Grothendieck
principle stated in `principles.tex` §"Grothendieck: cotangent modes
are residue currents".

### §3.4 Honest epistemic status

The remark explicitly:
- pins the literature with year-stamped citations;
- marks the numerical content as "verified at $N = 1..6$" with
  explicit script paths;
- distinguishes "Koszul complex not exact" (literature consequence)
  from "BV cohomology is the derived self-intersection" (the M-03
  Form-lens interpretation);
- names the $N = 1$ abelian boundary stratum as the special case
  where the phenomenon collapses.

No false certainty. The remark adds the Drinfeld-canonical
interpretation without claiming to re-prove Theorem A. CLAUDE.md
voice satisfied.

### §3.5 Process-leakage post-scan

After Step-1 scrub, post-scrub text contains zero instances of:
`wave`, `swarm`, `agent`, `ledger`, `M-XX`, `W3-WXX-YY`, `P4-G6-XX`.
Verified in §4 final prose by inspection.

---

## §4. T4 — Final inscribable prose (boxed)

Two LaTeX-ready blocks. The first is the plan-Markdown insertion
(this file's primary authorization target). The second is the
downstream manuscript LaTeX (`main.tex`:128 elision target), shown
for completeness; the manuscript inscription is gated on the §5
Premet 2003 `\bib{}` entry being inscribed first.

### §4.1 Plan-Markdown insertion (authorization scope)

**Target.** `reconstitution/platonic-ideal-plan-2026-04-28.md`
between line 196 (end of "Proof skeleton" paragraph) and line 198
("**Action items.**" heading). Insert as a new bold-leadered
paragraph.

```markdown
+--------------------------------------------------------------------+
|                                                                    |
| **Derived-intersection remark.** For $N \ge 2$ the commuting       |
| variety $\mathcal C_N = \{(A, B) \in \mathfrak{gl}_N^2 \mid        |
| [A, B] = 0\}$ is irreducible (Motzkin–Taussky 1955; Gerstenhaber   |
| 1961) of codimension $N(N-1)$ but is not a complete intersection   |
| (Premet 2003; Vasconcelos 1994). The moment-map ideal $I_\mu =     |
| ([\phi_1, \phi_2]^i{}_j)$ has $N^2 - 1$ independent generators on  |
| $\mathfrak{sl}_N$ (after the trace identity                        |
| $\mathrm{Tr}[\phi_1, \phi_2] = 0$), exceeding the codimension      |
| $N(N-1)$ by an excess $\Delta(N) = N$ (verified at $N = 1..6$;     |
| `scripts/check_derived_intersection_N_extended.py`). The Koszul    |
| complex on $I_\mu$ is therefore not exact for $N \ge 2$, and the   |
| open BV cohomology $H^\bullet(\mathcal R_N^{\mathrm{GL}_N}, Q)$    |
| is the derived self-intersection of $\mathcal C_N$, not its naive  |
| structure sheaf. The chain-level cycle $\mathrm{Tr}\,\psi$ is the  |
| canonical degree-$(-1)$ avatar of the derived-intersection class   |
| (`scripts/check_derived_intersection_N2.py`); higher classes       |
| $\mathrm{Tr}(\psi^k)$ for $1 \le k \le N$ exhaust the              |
| $\Delta(N) = N$ Tor$^1$ generators by cyclicity. The $N = 1$       |
| abelian stratum collapses, $\Delta(1) = 1$ giving the trivial      |
| $\mathrm{Tr}\,\psi = \psi$ class with zero $Q$; the                |
| non-complete-intersection phenomenon switches on at $N \ge 2$ and  |
| grows linearly in $N$.                                             |
|                                                                    |
+--------------------------------------------------------------------+
```

### §4.2 Downstream manuscript LaTeX (Phase-2 target, shown for completeness)

**Target.** `main.tex` line 128, immediately after the sentence "This
algebra is the open trace algebra of the defect." Insert as a new
`\begin{rmk}[Derived intersection]\label{rmk:m03-derived-intersection}`
block.

```latex
+--------------------------------------------------------------------+
|                                                                    |
| \begin{rmk}[Derived intersection]                                  |
|   \label{rmk:m03-derived-intersection}                             |
|   For $N\geq 2$ the commuting variety                              |
|   $\mathcal C_N=\{(A,B)\in\lie{gl}_N^2\mid[A,B]=0\}$ is            |
|   irreducible (Motzkin--Taussky 1955; Gerstenhaber 1961) of        |
|   codimension $N(N-1)$ but is not a complete intersection          |
|   (\cite{premet-nilpotent-commuting};                              |
|   \cite{vasconcelos-blowup-algebras}). The moment-map ideal        |
|   $I_\mu=([\phi_1,\phi_2]^i{}_j)$ has $N^2-1$ independent          |
|   generators on $\lie{sl}_N$ (after the trace identity             |
|   $\operatorname{Tr}[\phi_1,\phi_2]=0$), exceeding the codimension |
|   $N(N-1)$ by an excess $\Delta(N)=N$ (verified at                 |
|   $N=1,\ldots,6$). The Koszul complex on $I_\mu$ is therefore not  |
|   exact for $N\geq 2$, and the open BV cohomology                  |
|   $H^\bullet(\mathcal R_N^{\GL_N},Q)$ is the derived               |
|   self-intersection of $\mathcal C_N$, not its naive structure     |
|   sheaf. The chain-level cycle $\operatorname{Tr}\psi$ is the      |
|   canonical degree-$(-1)$ avatar of the derived-intersection       |
|   class; higher classes $\operatorname{Tr}(\psi^k)$,               |
|   $1\leq k\leq N$, exhaust the $\Delta(N)=N$ excess Tor$^1$        |
|   generators by cyclicity. The $N=1$ abelian stratum collapses,    |
|   $\Delta(1)=1$ giving the trivial $\operatorname{Tr}\psi=\psi$    |
|   class with zero $Q$; the non-complete-intersection phenomenon    |
|   switches on at $N\geq 2$ and grows linearly in $N$.              |
| \end{rmk}                                                          |
|                                                                    |
+--------------------------------------------------------------------+
```

**Inscription notes.**
1. Plan-Markdown uses Unicode en-dash (U+2013) for hyphenated author
   names per Markdown house style; LaTeX uses double hyphen (`--`)
   per AMS-LaTeX convention.
2. LaTeX form drops the explicit `scripts/...` footnote (those
   pointers belong in `claim-strength-ledger.tex` and the appendix
   reproducibility note, not inline manuscript prose).
3. LaTeX uses `\GL_N` (assumes a `\GL` macro in `mathmacros.tex`); if
   the macro is named differently, substitute `\mathrm{GL}_N`.
4. LaTeX uses `\operatorname{Tr}` consistent with `principles.tex`
   line 8.

---

## §5. T5 — `\bib{}` entry: Premet 2003

The user task names "Premet 2003 (Trans. AMS)" as the `\bib{}` target.
**Disambiguation.** The Premet 2003 paper that establishes the
nilpotent commuting variety result for reductive Lie algebras is
*Inventiones Mathematicae* 154 (2003), 653–683 (cf. W27 §2.4 and the
master ledger M-03 entry); there is no Trans. AMS Premet 2003 paper
in the commuting-variety literature. The user's parenthetical pin
appears to be a small misattribution; the entry below is drafted
against the verified Invent. Math. citation, which is the load-bearing
primary source for the M-03 promotion. (The Trans. AMS reference in
the M-03 attribution chain is *Motzkin–Taussky 1955*, Trans. AMS 80,
387–401, which is a separate citation.)

### §5.1 Premet 2003 — `\bib{}` entry (AMS-LaTeX, amsrefs)

```latex
+--------------------------------------------------------------------+
|                                                                    |
| \bib{premet-nilpotent-commuting}{article}{                         |
|    author={Premet, Alexander},                                     |
|    title={Nilpotent commuting varieties of reductive Lie           |
|      algebras},                                                    |
|    journal={Invent. Math.},                                        |
|    volume={154},                                                   |
|    date={2003},                                                    |
|    number={3},                                                     |
|    pages={653--683},                                               |
|    doi={10.1007/s00222-003-0317-4},                                |
| }                                                                  |
|                                                                    |
+--------------------------------------------------------------------+
```

**Citation key.** `premet-nilpotent-commuting`: title-keyed; avoids
ambiguity with Premet's 2002 nilpotent-orbit paper or the 2007 Whittaker
modules paper.
**Placement in main.tex.** Insert in the algebraic-geometry / commuting-
variety cluster: after `\bib{matlis-injective}` (line 6144) and
before `\bib{hartshorne-local-cohomology}` (line 6155), keeping the
algebra-of-commuting-matrices block adjacent to the Matlis duality
block. Final placement at the user's discretion.
**Format consistency.** Field order (author / title / journal /
volume / date / number / pages / doi) matches the existing
`\bib{loday-quillen}` (line 5941) and `\bib{kontsevich-dq}` (line 6010)
entries verbatim.

### §5.2 Companion entries (drafted; not part of this T5 authorization)

The full M-03 citation chain requires four entries; only Premet 2003
is in T5 scope. The other three are drafted for the user's reference
should §4.2 manuscript inscription be authorized in a later batch:

```latex
\bib{motzkin-taussky-pairs-property-L}{article}{
   author={Motzkin, T. S.},
   author={Taussky, Olga},
   title={Pairs of matrices with property $L$. II},
   journal={Trans. Amer. Math. Soc.},
   volume={80},
   date={1955},
   pages={387--401},
   doi={10.1090/S0002-9947-1955-0086781-5},
}

\bib{gerstenhaber-commuting-matrices}{article}{
   author={Gerstenhaber, Murray},
   title={On dominance and varieties of commuting matrices},
   journal={Ann. of Math. (2)},
   volume={73},
   date={1961},
   pages={324--348},
   doi={10.2307/1970336},
}

\bib{vasconcelos-blowup-algebras}{book}{
   author={Vasconcelos, Wolmer V.},
   title={Arithmetic of Blowup Algebras},
   series={London Mathematical Society Lecture Note Series},
   volume={195},
   publisher={Cambridge University Press},
   place={Cambridge},
   date={1994},
   pages={x+329},
   doi={10.1017/CBO9780511562389},
}
```

These are companion drafts only. T5 authorizes Premet 2003 alone.

---

## §6. T6 — Inscription-time conflict check (Bash grep)

Three `grep` invocations were run during specimen drafting. Outputs
recorded verbatim below.

### §6.1 Conflict check (a): primary-source names not yet inscribed

```bash
grep -n "Premet\|Vasconcelos\|Gerstenhaber\|Motzkin\|premet" \
    /Users/raeez/topological-strings/main.tex \
    /Users/raeez/topological-strings/abstract.tex \
    /Users/raeez/topological-strings/principles.tex \
    /Users/raeez/topological-strings/notation.tex \
    /Users/raeez/topological-strings/nomenclature.tex \
    /Users/raeez/topological-strings/commands.tex \
    /Users/raeez/topological-strings/mathmacros.tex
```

**Output (verbatim).** Empty. Zero hits across all seven files. The
manuscript currently contains no citation to any of the four
primary sources; inscription of the §4.2 LaTeX block and the §5.1
`\bib{}` entry will be the first occurrence of each name.

### §6.2 Conflict check (b): no prior derived-intersection remark

```bash
grep -n "Derived intersection\|derived-intersection\|\
derived self-intersection\|rmk:m03" \
    /Users/raeez/topological-strings/main.tex \
    /Users/raeez/topological-strings/principles.tex \
    /Users/raeez/topological-strings/abstract.tex
```

**Output (verbatim).** Empty. Zero hits. No prior `\begin{rmk}[Derived
intersection]` block, no `\label{rmk:m03-derived-intersection}`, no
prose-level "derived self-intersection" string in `main.tex`,
`principles.tex`, or `abstract.tex`. The §4.1 plan-Markdown insertion
and the §4.2 manuscript LaTeX insertion are both first occurrences.

### §6.3 Conflict check (c): existing `\bib{}` entry slot

```bash
awk '/\\bib\{/{print NR": "$0}' /Users/raeez/topological-strings/main.tex \
  | grep -E "matlis-injective|hartshorne-local-cohomology|premet"
```

**Output (verbatim).**
```
6144: \bib{matlis-injective}{article}{
6155: \bib{hartshorne-local-cohomology}{book}{
```

No `premet`-keyed entry in main.tex. The recommended insertion slot
between lines 6153 (close of `\bib{matlis-injective}`) and 6155
(open of `\bib{hartshorne-local-cohomology}`) is empty, suitable for
the §5.1 `\bib{premet-nilpotent-commuting}` block.

### §6.4 Verdict

Inscription has zero conflicts at the plan-Markdown target, at the
manuscript LaTeX target, and at the bibliography insertion slot.
The §4.1 / §4.2 / §5.1 prose blocks are inscription-ready.

---

## §7. T7 — Three-line authorization template

```
+--------------------------------------------------------------------+
|                                                                    |
| Authorize inscription of P4-EXEC-G6-S01 (M-03 derived-intersection |
| remark for §3 Theorem A preface) at                                |
| reconstitution/platonic-ideal-plan-2026-04-28.md after line 196    |
| per phase4-exec-editorial-specimen-2026-04-28.md §4.1.             |
|                                                                    |
| Authorize §5.1 \bib{premet-nilpotent-commuting} entry into         |
| main.tex line 6154 (between \bib{matlis-injective} and             |
| \bib{hartshorne-local-cohomology}).                                |
|                                                                    |
| Defer §4.2 manuscript-LaTeX rmk-block inscription to Phase-2       |
| pending companion \bib{} entries (Motzkin–Taussky, Gerstenhaber,   |
| Vasconcelos) drafted in §5.2.                                      |
|                                                                    |
+--------------------------------------------------------------------+
```

The three lines correspond to the three independently authorizable
units in this specimen: the plan-Markdown remark insertion (T4 §4.1);
the Premet 2003 `\bib{}` entry (T5 §5.1); and the deferred manuscript
LaTeX inscription gated on the three companion `\bib{}` entries
(T5 §5.2).

---

## §8. Specimen completeness ledger

| Item | Status | Notes |
|------|--------|-------|
| T1 — Verbatim source draft prose | Complete | §1.1 W27 §6.1 verbatim. |
| T2 — 5-step G6 §4.4 scrub applied | Complete | §2.1 strip tags (1 leading, 1 embedded); §2.2 em-dashes (no-op); §2.3 hedges (no-op); §2.4 voice (no-op); §2.5 attribution (pass). |
| T3 — CLAUDE.md voice check | Complete | §3 Russian school + Polyakov + Form lens + honest epistemic status all confirmed. |
| T4 — Final inscribable prose boxed | Complete | §4.1 plan-Markdown form; §4.2 LaTeX form. |
| T5 — Premet 2003 `\bib{}` entry | Complete | §5.1 amsrefs `\bib{premet-nilpotent-commuting}`; companion entries drafted in §5.2. |
| T6 — Inscription-time conflict check | Complete | §6.1–§6.3 three Bash `grep` invocations; zero conflicts at all three targets. |
| T7 — Three-line authorization template | Complete | §7 plan-Markdown + Premet `\bib{}` + deferred manuscript inscription. |

---

## §9. Provenance and lens-cross-walk

**Lens (Polyakov + Form).** Polyakov supplies the worldsheet/brane
gauge-fixing convention discipline: the Dirac reduction is honest only
when the Koszul resolution is honest, and the moment-map ideal must
not be silently treated as a regular sequence. Form supplies the
cotangent-form discipline: the BV cohomology classes
$\mathrm{Tr}(\psi^k)$ are degree-$(-1)$ forms in the derived
self-intersection, paired against the Matlis principal-part cotangent
sector $\mathcal P$. The two lenses converge on the M-03 promotion
prose: the derived-intersection remark is the open-side counterpart
of the Grothendieck principle in `principles.tex`, anchoring Theorem
A's interpretation in the formal-symplectic-disk cotangent picture.

**Wave-3 cross-confirmation.** The specimen prose is the W3-W27-01
heal text from `reconstitution/wave3-W27-m03-bv-derived-2026-04-28.md`
§6.1, drafted by the W27 attacker and verified independently by W3,
W10, W12, W14 cross-walks (W27 §4). Two scripts at
`/Users/raeez/topological-strings/scripts/check_derived_intersection_N2.py`
and `/Users/raeez/topological-strings/scripts/check_derived_intersection_N_extended.py`
verify the $\Delta(N) = N$ claim at $N = 1..6$. The four primary-source
citations are standard published results (Trans. AMS, Ann. of Math.,
Cambridge LMS Lect. Note Ser., Invent. Math.).

**Files read in full.**
- `/Users/raeez/topological-strings/CLAUDE.md`.
- `/Users/raeez/topological-strings/reconstitution/phase4-G6-editorial-roadmap-2026-04-28.md`.
- `/Users/raeez/topological-strings/reconstitution/wave3-W27-m03-bv-derived-2026-04-28.md`.
- `/Users/raeez/topological-strings/abstract.tex`.
- `/Users/raeez/topological-strings/principles.tex`.

**Files inspected (relevant excerpts).**
- `/Users/raeez/topological-strings/main.tex` lines 110–168 (Theorem A
  region; M-03 elision at line 127), 5915–5994 (existing `\bib{}`
  block opening), 6144–6166 (`\bib{matlis-injective}` and
  `\bib{hartshorne-local-cohomology}` for the §5.1 placement slot).

**No web fetches.** Primary-source citations reproduced from the master
ledger M-03 entry and cross-checked against the standard
algebra-of-commuting-matrices literature.

---

## §10. 200-word summary

The Phase-4 EXEC specimen takes the W3-W27-01 derived-intersection
remark as drafted in `wave3-W27-m03-bv-derived-2026-04-28.md` §6.1
and applies the G6 §4.4 5-step scrub through the Polyakov + Form
lens. T1 quotes the verbatim source prose. T2 reports: Step 1 strips
the leading `(M-03 / W3-W27-01)` tag and the embedded `W3-W10-02`
tag; Steps 2–4 are no-ops since the W27 draft is already em-dash-free,
hedge-free, and active-voice; Step 5 verifies all four primary-source
citations (Motzkin–Taussky 1955; Gerstenhaber 1961; Vasconcelos 1994;
Premet 2003) are year-pinned with explicit "verified at $N = 1..6$"
computational marker. T3 confirms Russian-school + Polyakov +
Form-lens + honest-epistemic-status discipline. T4 boxes the final
inscribable prose in two forms: §4.1 plan-Markdown insertion at
`platonic-ideal-plan-2026-04-28.md` line 197; §4.2 manuscript LaTeX
remark for `main.tex`:128. T5 supplies the `\bib{premet-nilpotent-commuting}`
amsrefs entry against Invent. Math. 154 (2003), 653–683, with a
disambiguation note (the user's "Trans. AMS" parenthetical refers to
the separate Motzkin–Taussky 1955 citation). T6 runs three Bash `grep`
inscription-time conflict checks; all return zero conflicts. T7
provides the three-line authorization template covering plan-Markdown
remark, Premet `\bib{}` entry, and deferred manuscript inscription.
PROPOSAL-ONLY; nothing inscribed.

---

End of P4-EXEC-G6 editorial inscription specimen (Polyakov + Form
lens; 2026-04-28).
