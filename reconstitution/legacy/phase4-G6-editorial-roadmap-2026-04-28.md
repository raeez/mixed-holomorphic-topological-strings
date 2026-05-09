# Phase 4 — G6 Consolidated Editorial Roadmap

**Date.** 2026-04-28.
**Initiator.** Phase-4 G6 research initiator (editorial / dictionary cluster).
**Mode.** META-ORGANIZATION; proposal-only. No new mathematical content; no manuscript edits; no master-ledger overwrites. New identifiers use prefix `P4-G6-`.
**Charter.** Consolidate every prose-level heal proposed across wave-3 sub-ledgers (W17 HKR, W20 dictionary, W24 Theorem E steps, W27 M-03 promotion, W28 Obligation II, W30 (A5), and the W13 thirteen items absorbed in W32). Sequence by dependency. Provide author-style guidance per CLAUDE.md voice. Verify no process-leakage prose. Produce an authorization checklist by tier.

**Scope guarantee.** This document is editorial sequencing. It does not generate ledger entries, propose new mathematics, or overturn convergence verdicts. The mathematical heals already exist in the wave-3 sub-ledgers; this roadmap orders them.

---

## §0. Source documents read in full

- `/Users/raeez/topological-strings/CLAUDE.md` (50 lines).
- `/Users/raeez/topological-strings/reconstitution/wave3-FINAL-convergence-report-2026-04-28.md` (Tier A 47 ready-to-inscribe).
- `/Users/raeez/topological-strings/reconstitution/wave3-W32-editplan-2026-04-28.md` (60 proposed edits with full draft prose; the master edit document).
- `/Users/raeez/topological-strings/reconstitution/wave3-W17-hkr-thmA-2026-04-28.md` (HKR heals).
- `/Users/raeez/topological-strings/reconstitution/wave3-W20-dictionary-completeness-2026-04-28.md` (13 dictionary heals).
- `/Users/raeez/topological-strings/reconstitution/wave3-W34-residual-catalog-2026-04-28.md` (G6 cluster summary).

---

## §1. T1 — Consolidated edit inventory (Tier A, ready to inscribe)

The 47 Tier-A edits aggregated from W32 §2.1–§2.7. Each row cites the originating sub-ledger; no draft-prose is re-derived here.

### §1.1 Standalone editorial / bibliographic / dictionary (no upstream prose dependency)

| # | Source attacker | Target file | Target line | Severity | Edit type | One-line description |
|---|---|---|---|---|---|---|
| P4-G6-01 | W17 / W3-W17-04 | `main.tex` | 5926+ (bib block) | 3 | Bib add | New `\bib{hkr}{}` entry for Hochschild–Kostant–Rosenberg, Trans. AMS 102 (1962). |
| P4-G6-02 | W17 / W3-W17-01 | `main.tex` | 2056 | 3 | Citation pin | Pin Theorem E Step 1 HKR appeal to Lurie HA Thm 5.5.3.18 + windowwise classical HKR. |
| P4-G6-03 | W17 / W3-W17-02 | `main.tex` | 2132 | 3 | Citation pin | Same source pin at Theorem E Step 5 (inherits P4-G6-02). |
| P4-G6-04 | W17 / W3-W17-03 | `main.tex` | 2202 | 2 | Citation pin | HKR pin in `\rmk:E1-translation`. |
| P4-G6-05 | W17 / W3-W17-05 | `main.tex` | 3370 (`\lem:continuous-bar-cobar`) | 3 | Lemma item add | Add Tate-extension item to bar-cobar lemma (windowwise inverse-limit prose). |
| P4-G6-06 | W20 / P-W3-W20-01 | `local-dictionary.tex` | after D11 | 3 | Dict entry | `\widehat{\mathbf S}_{\rm Tate}(\mathfrak h)` Tate-completed symmetric algebra. |
| P4-G6-07 | W20 / P-W3-W20-02 | `local-dictionary.tex` | after D11 | 3 | Dict footnote | Tate-conilpotency hypothesis pointer to `\lem:continuous-bar-cobar`. |
| P4-G6-08 | W20 / P-W3-W20-03 | `local-dictionary.tex` | new block | 3 | Dict entry | Weighted Tate envelope $w(d)=q^d$, $q>1$ for Theorem C₂(W). |
| P4-G6-09 | W20 / P-W3-W20-04 | `local-dictionary.tex` | same block | 2 | Dict entry | `regulator-admissible-sector` for Theorem C₂(R). |
| P4-G6-10 | W20 / P-W3-W20-06 | `local-dictionary.tex` | new "Quantum reduction" block | 3 | Dict entry | Capelli element $c_C := YX - XY + \hbar N\,I$. |
| P4-G6-11 | W20 / P-W3-W20-07 | `local-dictionary.tex` | new line | 2 | Dict entry | Matlis duality one-liner with `\cite{matlis-injective}`. |
| P4-G6-12 | W20 / P-W3-W20-08 | `local-dictionary.tex` | after D9 | 2 | Dict entry | PBW raising action $F_{p,q}$. |
| P4-G6-13 | W20 / P-W3-W20-09 | `local-dictionary.tex` | new "Factorisation centre" block | 3 | Dict entry | $Z^{P_0}_{\rm fact}(A)$ local convention. |
| P4-G6-14 | W20 / P-W3-W20-10 | `local-dictionary.tex` | append to factorisation block | 2 | Dict entry | HKR row (depends on P4-G6-01). |
| P4-G6-15 | W20 / P-W3-W20-11 | `local-dictionary.tex` | append | 2 | Dict entry | $\mathrm{PV}(A_\partial)$ definition. |
| P4-G6-16 | W20 / P-W3-W20-13 | `local-dictionary.tex` | section header | 1 | Dict gloss | Abbrev gloss (CE / PV / HKR / BV). |
| P4-G6-17 | W20 / P-W3-W20-14 | `local-dictionary.tex` | PBW block | 2 | Dict entry | $\overline{\mathrm{Tr}}\,f$ scalar-reduced trace. |
| P4-G6-18 | W20 / P-W3-W20-16 | `local-dictionary.tex` | after D19 | 2 | Dict entry | T²-Cartan rigidity (replaces "Schur rigidity"). |
| P4-G6-19 | W20 / P-W3-W20-17 | `local-dictionary.tex` | extend D6 | 2 | Dict extend | $[\bar c]\leftrightarrow [\mathrm{Tr}\,\psi]_{\rm BV}$ chain-level identification. |
| P4-G6-20 | W20 / P-W3-W20-21 | `local-dictionary.tex` | append star to D20 | 1 | Dict footnote | Negative-index target zero by principal-part projection. |
| P4-G6-21 | W20 / P-W3-W20-22 | `local-dictionary.tex` | terminal line | 1 | Dict gloss | Note `thm:main-local` is `\begin{cor}`, not theorem. |

**Subtotal §1.1: 21 edits, all Tier A standalone.**

### §1.2 Statement-level prose heals (depend on dictionary entries / bib being inscribed)

| # | Source attacker | Target file | Target line | Severity | Edit type | One-line description |
|---|---|---|---|---|---|---|
| P4-G6-22 | W32 / W3-W32-S5 = W27 §6.1, §6.2 | `main.tex` | 127 (Thm A preface) and ~419-469 (Thm G area) | 4 | Statement preface | M-03 derived-intersection promotion (Premet 2003; Vasconcelos 1994). |
| P4-G6-23 | W32 / W3-W32-S6 | `open-obligations.tex` (Obligation V) | end | 4 | Caveat | Graphwise-bounded $\neq$ renormalizable. |
| P4-G6-24 | W32 / W3-W32-S7 | `open-obligations.tex` (Obligation V) | after S6 | 3 | Caveat | Costello-Li five-step non-applicability. |
| P4-G6-25 | W32 / W3-W32-D24 | `open-obligations.tex` (Obligation IV) | end | 4 | Caveat | Regularization-compatible $\neq$ anomaly-cancelled (M-32 distinction). |
| P4-G6-26 | W32 / W3-W32-D9 | `principles.tex` (Principle 1) | end | 3 | Derivation insert | Why constants are killed: divergence-free + Poincaré lemma. |
| P4-G6-27 | W32 / W3-W32-D10 | `main.tex` (Thm A skeleton) | post-`196` | 3 | Derivation insert | A-brane $\otimes$ B-brane $\otimes$ Koszul ⇒ ghost-zero field $A+\phi_1\epsilon_1+\phi_2\epsilon_2$. |
| P4-G6-28 | W32 / W3-W32-S2 | `main.tex` (Thm A actions) | post-`202` | 3 | Action item | Local-operator Euler contraction $[d_R,\iota_{\partial_t}]=\partial_t$. |
| P4-G6-29 | W32 / W3-W32-D8 | `main.tex` (Thm A actions) | post-`202` | 3 | Action item | Quotient-stack vs invariant-reduction distinction. |
| P4-G6-30 | W32 / W3-W32-D20 | `main.tex` (Thm G area) | ~449 | 2 | Lemma append | Weight-bidegree decomposition lemma per M-09. |
| P4-G6-31 | W32 / W3-W32-D21 | `open-obligations.tex` (Obligation III) | reword | 3 | Reword | Strict $q\to 1^+$ unweighted limit forbidden by `\thm:strict-unweighted-no-go` (M-11). |
| P4-G6-32 | W32 / W3-W32-D22 | `main.tex` (Thm A) | one-sentence | 1 | Remark | Bosonic vs $\mathfrak{gl}(N\|N)$ disclaimer per M-13. |
| P4-G6-33 | W24 / W3-W32-W24.1 | `main.tex` Theorem E Step 4 | ~2095 | 2 | Step heal | Biderivation induction prose tightening. |
| P4-G6-34 | W24 / W3-W32-W24.2 | `main.tex` Theorem E Step 5 | ~2130 | 3 | Step heal | Bidirectional symmetric filtration (W3-W6-01). |
| P4-G6-35 | W24 / W3-W32-W24.3 | `main.tex` Theorem E Step 6 | + `lem:n-tuple-coassoc` | 3 | Step heal | n-tuple coassociativity (sharpens M-24). |
| P4-G6-36 | W24 / W3-W32-W24.4 | `main.tex` Theorem E Step 7 | ~2179 | 4 | Step heal | Cohomological local-constancy degree correction (degree 1 in $H^*_c(\R)$). |
| P4-G6-37 | W24 / W3-W32-W24.5 | `main.tex` Theorem E Step 8 | ~2215 | 3 | Step heal | Tate-window × stalk-limit interchange. |
| P4-G6-38 | W32 / W3-W32-S4 | `appendix-factorization-current-conventions.tex` (sign-convention) | +subsection | 3 | Subsection | Explicit BF-pairing-degree subsection: $|\alpha|+|\beta|+\text{top form}=-1$. |
| P4-G6-39 | W32 / W3-W32-D5 | same appendix | after S4 | 2 | Subsection | Uniform $[1]$ shift convention; BV ghost $[2]$ at line 1302 reconciled (W17 §T5 verdict). |
| P4-G6-40 | W32 / W3-W32-D13 | same appendix | after S4 | 2 | Subsection | Negative-index zero-target convention (`π_{pp}` projection). |
| P4-G6-41 | W32 / W3-W32-D14 | `main.tex` notation index | row append | 3 | Notation row | $\Theta_\rho$ parity / pairing convention disambiguation. |
| P4-G6-42 | W32 / W3-W32-D16 | same appendix | after S4 | 3 | Subsection | $\psi$-degree statement explicit. |
| P4-G6-43 | W32 / W3-W32-D26 | `open-obligations.tex` (Obl VII) | structural | 3 | Structural argument | Distribution-product avoidance per M-36. |

**Subtotal §1.2: 22 edits, Tier A but downstream of dictionary / bib inscriptions.**

### §1.3 Structural splits (the load-bearing severity-5 edits)

| # | Source attacker | Target file | Target line | Severity | Edit type | One-line description |
|---|---|---|---|---|---|---|
| P4-G6-44 | W32 / W3-W32-D17 + W6 sharpenings | `main.tex` Theorem C area + `theorem-lanes.tex` + `claim-strength-ledger.tex` | ~1700 area | 5 | Theorem split | Theorem C 5-way split per M-26: C₁ᶠʷ, C₁ᶜᵒᵐᵖ, C₂(NT), C₂(W), C₂(R). |
| P4-G6-45 | W32 / W3-W32-D18 = W28-T4 | `open-obligations.tex` Obligation II | 159–181 | 5 | Obligation reformulation | Obligation II reformulation with named no-go + 3 escape routes. |
| P4-G6-46 | W32 / W3-W32-D15 | `main.tex` §7 N1 | toy lemma | 4 | Numbered lemma | Promote finite-Lie toy lemma to numbered statement per C243. |
| P4-G6-47 | W32 / W3-W32-D23 + D27 | `open-obligations.tex` Obligation VII | expand | 3 | Structural | Weiss-cosheaf-descent four-ingredient adoption per M-14, M-37. |

**Subtotal §1.3: 4 edits, Tier A structural.**

**Aggregate §1: 47 Tier-A edits across 11 target files.**

---

## §2. T2 — Sequencing proposal (four phases by dependency)

The 47 edits separate into four phases by edit-DAG dependency. Within a phase, edits are independent and parallelizable.

### §2.1 Phase 1 — Standalone editorial (no dependencies; 21 edits)

These edits do not depend on any other prose change. They can be inscribed in any order and verified individually.

**Members.** P4-G6-01 (HKR `\bib{}`), P4-G6-02..05 (HKR citation pins, Tate-HKR lemma item — all internal to Theorem E and `\lem:continuous-bar-cobar`), P4-G6-06..21 (16 dictionary entries / footnotes / glosses).

**Why first.** Bibliography and dictionary entries are supply-side: every later phrase in Phases 2-4 that names an HKR appeal, a Tate-completed symmetric algebra, a regulator-admissible sector, or a Capelli element references these definitions. Inscribing them first ensures that the statement-level prose in Phase 2 has its referents in scope.

**Internal dependencies inside Phase 1.**
- P4-G6-14 (HKR dictionary row) cites P4-G6-01 (the new `\bib{hkr}{}` entry); inscribe P4-G6-01 first.
- All other Phase-1 entries are independent.

**Estimated edit budget.** ~22 single-row table additions in `local-dictionary.tex`; one new `\bib{}` block; three citation-pin sentences in `main.tex`; one Tate-extension footnote in `\lem:continuous-bar-cobar`. No proof rewrites.

### §2.2 Phase 2 — Statement-level prose (depends on Phase 1 dictionary; 22 edits)

These edits insert or rewrite paragraphs at theorem statements, action-item lists, and obligation prose. Each references one or more Phase-1 entries.

**Members.** P4-G6-22..43.

**Why second.** P4-G6-22 (M-03 derived intersection) names `\bar A_{\rm desc}` (D5), the Capelli element (P4-G6-10), and the $[\bar c]\leftrightarrow[\mathrm{Tr}\,\psi]_{\rm BV}$ identification (P4-G6-19). P4-G6-25 (regularization vs anomaly cancellation) names the Capelli class. P4-G6-30 (weight-bidegree lemma) names the dictionary's bidegree language. The Theorem E step heals (P4-G6-33..37) inscribe the HKR-pinned citations from Phase 1.

**Internal dependencies inside Phase 2.**
- P4-G6-22 (M-03 promotion) is the load-bearing item — Theorem A preface and Theorem G re-narration. Once inscribed, P4-G6-25..30 reference it implicitly through the derived-intersection vocabulary.
- P4-G6-38, P4-G6-39, P4-G6-40, P4-G6-42 are the **sign-appendix stack**: all four edits land in `appendix-factorization-current-conventions.tex` as adjacent subsections; batch-inscribe as one subsection block with internal cross-references.
- P4-G6-23 / P4-G6-24 are sequential appends in `open-obligations.tex` Obligation V (S6 then S7).
- P4-G6-43 / P4-G6-31 are sequential in Obligation III / VII.

**Estimated edit budget.** ~18 paragraph insertions; 4 reword passes; 1 lemma append. No new theorem statements except the W3-W32-D15 toy lemma promotion (which is in Phase 3).

### §2.3 Phase 3 — Structural splits (depends on Phases 1-2; 4 edits)

These edits restructure load-bearing statements. They cannot land before the dictionary and statement-level prose absorbs the new vocabulary — otherwise the split fragments will reference undefined terms.

**Members.** P4-G6-44 (Theorem C 5-way split), P4-G6-45 (Obligation II reformulation), P4-G6-46 (D15 toy lemma promotion), P4-G6-47 (Obligation VII four-ingredient).

**Why third.** Theorem C's 5-way split (P4-G6-44) names $w(d)=q^d$, regulator-admissible-sector, the Tate-conilpotency hypothesis, and `\lem:tate-mittag-leffler-dictionary` — all four definitions land in Phase 1. The split also names the M-01 perfectness obstruction in its critical disclaimer; the disclaimer fits cleanly only after Phase-2 has installed the M-03 / regularization-vs-anomaly vocabulary that contextualizes "no claim is made for the strict unweighted limit."

Obligation II reformulation (P4-G6-45) names the bi-infinite parent, the four-cone filtration, the column-Verma identification, the universal categorical no-go, and the three escape routes — these names appear in Phase-1 dictionary entries (P4-G6-19 partial; P4-G6-09 regulator-admissible-sector for escape route iii) and in Phase-2 prose (Theorem A preface).

**Internal dependencies inside Phase 3.**
- P4-G6-44 must precede the seven downstream Phase-4 cross-references that refer to the new C₁/C₂ lane labels (these are all Tier-B in the W32 schema).
- P4-G6-45 must precede the W28.2 downstream propagation (Tier-B).
- P4-G6-46 and P4-G6-47 are independent of P4-G6-44/45.

**Estimated edit budget.** One ~25-line theorem split (P4-G6-44 across `main.tex`, `theorem-lanes.tex`, `claim-strength-ledger.tex`); one ~84-line obligation reformulation block (P4-G6-45); one numbered lemma promotion; one structural expansion in `open-obligations.tex`.

### §2.4 Phase 4 — Cross-references (depends on Phases 1-3; Tier B from W32, 8 edits)

These are downstream propagation edits that update lane files, the claim-strength ledger, and `principles.tex` to reflect the new Theorem C labels and Obligation II reformulation. They are listed as Tier B in W32 §2 because each requires Phase-3 to land first.

**Members (carry forward W32 Tier-B IDs; not in the 47 Tier-A count).**
- W3-W32-W6.1..W6.5 (5 edits): propagate Theorem C lane sharpenings to `theorem-lanes.tex` Lane 3, `claim-strength-ledger.tex` C₂ entries, and the tate-T*.tex files. Specifically T1 gets the C₂(W) bidirectional update (W3-W6-01); T3 gets C₂(R) regulator-class-canonicity language; T5 gets the bidirectional symmetric filtration update.
- W3-W32-W27.3: propagate M-03 derived-intersection language into `principles.tex` Witten section and `theorem-lanes.tex` Theorem A / G blocks.
- W3-W32-W28.2: propagate Obligation II reformulation into `theorem-lanes.tex` Lane 6 and `claim-strength-ledger.tex`.
- W3-W32-D11: §7 N1 toy paragraph expansion (Symp covariance call-out) — depends on P4-G6-44 Theorem C split.
- W3-W32-D12: §5 voice apologetic-phrasing scrub — depends on the new theorem-status language landing.
- W3-W32-D25: Symp$_{\rm form}$ per-theorem statement, depends on P4-G6-44 and the dictionary symbol decision (Tier C).

**Phase 4 is not part of the 47 Tier-A count.** It is the downstream propagation budget the user authorizes after Tier-A inscription is verified.

---

## §3. T3 — Style guidance (Russian school + mathematical-physics frontier)

CLAUDE.md §IV mandates the Russian mathematical-school voice with the mathematical-physics-frontier register. The wave-3 sub-ledgers contain heavy process language ("wave", "swarm", "agent", "ledger", "M-XX", "P4-G6-XX") that **must not appear in reader-visible manuscript prose**. The author scrub layer below specifies what to keep and what to drop.

### §3.1 Sentence-level voice

**Declarative, not hedged.** "The bi-infinite parent is $\widetilde{\mathcal M} = \C[z_1^{\pm 1}, z_2^{\pm 1}]/\C$" — not "We propose to interpret the bi-infinite parent as..." Russian-school discipline: state the object, give the formula.

**Named attribution at the inscription site.** Every load-bearing claim cites the named theorem at first occurrence. M-03 promotion (P4-G6-22) cites Premet 2003 and Vasconcelos 1994 in the preface paragraph itself, not in a footnote. HKR pins (P4-G6-02..04) cite Hochschild–Kostant–Rosenberg, Trans. AMS 102 (1962), Theorem 5.2, plus Lurie HA 5.5.3.18 and Costello–Gwilliam Vol II §3 — all three in the same sentence.

**Honest epistemic status, no false certainty.** Theorem C 5-way split (P4-G6-44) prose explicitly lists which lane is hypothesis-free (C₁ᶠʷ), which depends on `\lem:tate-mittag-leffler-dictionary` (C₁ᶜᵒᵐᵖ), which is conditional on `prob:weighted-rg-locality` (C₂(W)-q), and which is admissible-class-canonical-not-Costello-canonical (C₂(R)). The critical disclaimer paragraph names the M-01 perfectness obstruction and states "no claim is made for the strict unweighted limit." This is not hedging; it is precise stating-of-the-claim.

**Physical intuition coexists with formal rigor.** P4-G6-26 (divergence-free + Poincaré lemma) and P4-G6-27 (A-brane $\otimes$ B-brane $\otimes$ Koszul) are physics derivations of the manuscript's mathematical objects. They sit in `principles.tex` and `main.tex` at the action-item layer, not the proof layer; they explain the construction without subordinating it.

### §3.2 Avoid

- **Em-dashes.** Recent commit history (`bc41359 Elite-grade prose scrub: no em dashes...`) shows the author has scrubbed em-dashes from the manuscript. Inscribed prose must use commas, semicolons, colons, or sentence breaks instead. The W32 draft prose contains em-dashes (e.g., the Obligation II "**Open question (orientation: groundbreaking-or-impossible-agnostic).**" prose); these must be re-cast at inscription time.
- **Hedged language.** "We propose," "It would seem," "perhaps," "may possibly." Every Russian-school inscription is declarative.
- **AI tells.** "As an AI," "I cannot," "let me note that..." None present in the wave-3 draft prose; verified.
- **Process-tag language in reader prose.** "wave 3," "the W17 audit," "P4-G6-XX," "swarm," "agent," "ledger." Reader-visible prose names mathematical objects, theorems, and primary sources — not the internal coordination machinery. **Note.** Provenance tags like "(W3-W13-9)" appear in many of the wave-3 draft prose snippets (e.g., "**Why constants are killed (W3-W13-9).**"); these are scaffolding for traceability and **must be stripped at inscription**. The inscribed paragraph is "**Why constants are killed.**" with no parenthetical wave tag.
- **Apologetic phrasing.** "Note that...," "It should be observed that...," "Of course." These dilute the declarative voice.

### §3.3 Prefer

- **Precise mathematical objects with formulas.** P4-G6-26 prose: "$d(\iota_X \omega) = 0$. By the formal Poincaré lemma applied to $\C[[z_1, z_2]]$, every closed 1-form is exact: $\iota_X \omega = -df$ for some $f \in \C[[z_1, z_2]]$, equivalently $X = X_f$."
- **Concrete examples / counts.** The wave-3 final convergence report contains many of these. Bi-infinite parent verified at 169,176+ commutator instances across W3, W12, W21, W23. Algebraic Moyal core: 14,641 + 121 + 160 + 7 explicit script-grade verifications. These quantitative honesty notes belong in claim-strength-ledger and inline at the strengthened theorems, not in reader prose at the action-item or obligation layer.
- **Named theorems with primary-source pins.** Premet 2003; Vasconcelos 1994; Hochschild–Kostant–Rosenberg 1962, Theorem 5.2; Lurie HA 5.5.3.18; Costello–Gwilliam Vol II §3; Costello-Li *Twisted supergravity* 2016; Beilinson–Drinfeld factorization. Each name carries its discipline-cohort weight; use it.
- **The M-29 / Theorem-G structural-claim pattern.** "There is no $\C[[\hbar]]$-linear additive category..." (assertion). "Survives every tensor-categorical attack: ..." (lens enumeration). "Severity 5 confirmation." (named status). This is the platonic-ideal Russian-school math style for stating a no-go.

---

## §4. T4 — Process-leakage scan

Each wave-3 sub-ledger is, by construction, a coordination document; process-tag language is appropriate inside the sub-ledger. The scan below identifies which prose **as drafted** still carries process tags, and what must be scrubbed at inscription.

### §4.1 Phase-1 prose (dictionary / bibliography)

- **HKR `\bib{}` entry (P4-G6-01).** Pure bibliography; no process language. **Scrub status: clean.**
- **HKR citation pins (P4-G6-02..04).** Draft prose at W17 §T6 contains "by the windowwise inverse limit using `\lem:continuous-bar-cobar` Item~2 and Lurie *Higher Algebra* Theorem 5.5.3.18 for the locally constant `E_1`-factorization-`E_1`-algebra equivalence." **Scrub status: clean.** No process-tag language; named-theorem citations only.
- **Tate-extension lemma item (P4-G6-05).** Draft prose at W17 §T6 W3-W17-05 is purely mathematical. **Scrub status: clean.**
- **Dictionary entries (P4-G6-06..21).** Each draft prose at W20 §7 P-W3-W20-XX is a single-row table addition with mathematical content. The entries do **not** name process tags. **Scrub status: clean.**
  - Exception: P4-G6-19 draft prose ends "Cohomologically equal to `[Tr ψ]_BV` under the chain-level identification of M-31 / W3-03." The "M-31 / W3-03" citation is a ledger pointer, not a paper citation; **scrub at inscription** to either drop the trailing tag or re-cast as "(see `\thm:quantum-classical-anomaly`)."

### §4.2 Phase-2 prose (statement-level)

- **M-03 promotion (P4-G6-22).** Draft prose at W3-W27 §6.1, §6.2 is mathematical: "**Derived-intersection remark (M-03 / W3-W27-01).** For $N \ge 2$ the commuting variety…" The leading "**(M-03 / W3-W27-01).**" tag must be **dropped at inscription**. The trailing $\Delta(N)=N$ formula is fine. **Scrub status: scrub leading tag.**
- **Graphwise-bounded $\neq$ renormalizable caveat (P4-G6-23).** Draft prose at W32 §1.1 contains "**Caveat — graphwise-bounded ≠ renormalizable (W3-W13-6).**" The em-dash in the title and the "(W3-W13-6)" tag must both be **scrubbed**. Replacement: "**Caveat: graphwise-bounded does not imply renormalizable.**" or simply "**Graphwise control vs renormalizability.**" The body prose names "Costello, *Renormalization and Effective Field Theory*, 2011" — clean.
- **Costello-Li non-applicability (P4-G6-24).** Draft prose names Costello-Li *Twisted supergravity* 2016 and the five reduction steps; the "**Costello-Li non-applicability (W3-W13-7).**" header tag must be scrubbed. The body prose references "M-13" — replace with "the bosonic vs $\mathfrak{gl}(N\|N)$ disclaimer."
- **Regularization vs anomaly cancellation (P4-G6-25).** Draft prose at W32 §1.2 W3-W32-D24: "**Regularization-compatibility vs anomaly-cancellation (W3-W13-24 / M-32).** The $U(1)_{\rm ghost}$ anomaly class $[\bar c]$ is **regularization-compatible**: every Costello-class heat-kernel BV regulator preserves the $U(1)_{\rm ghost}$ grading on $\mathcal R_N$ (Costello, *RenEFT*, 2011, §5.3; Henneaux-Teitelboim, *Quantization of Gauge Systems*, 1992, §18.3)." The leading "(W3-W13-24 / M-32)" tag must be scrubbed. Body cites Costello + Henneaux-Teitelboim — clean.
- **Why constants are killed (P4-G6-26).** Draft prose at W32 §1.2 W3-W32-D9: "**Why constants are killed (W3-W13-9).** A divergence-free vector field..." Scrub the "(W3-W13-9)" tag.
- **A-brane $\otimes$ B-brane $\otimes$ Koszul (P4-G6-27).** Draft prose at W32 §1.2 W3-W32-D10: "**Open-string state space from A-brane $\otimes$ B-brane $\otimes$ Koszul resolution (W3-W13-10).**" Scrub the "(W3-W13-10)" tag. The body cites the field content; clean.
- **Local-operator Euler contraction (P4-G6-28).** "**- Local-operator Euler contraction (W3-W13-2 / W3-W32-S2).**" Scrub both ledger tags.
- **Quotient-stack vs invariant-reduction (P4-G6-29).** "**- Quotient-stack vs invariant-reduction (W3-W13-8 / W3-W32-D8).**" Scrub.
- **Theorem E step heals (P4-G6-33..37).** Draft prose at W3-W24 lines 482, 579, 703, 813, 906 is mathematical step-by-step prose. **Scrub status: verified clean** by interpretation W3-W24 step prose; no process tags appear in the actual paragraph bodies.
- **Sign-appendix stack (P4-G6-38..40, 42).** Draft prose at W32 §1.1 / §1.2 names "(W3-W13-4)," "(W3-W13-19 / M-07)," and similar — all to be scrubbed at inscription.

### §4.3 Phase-3 prose (structural splits)

- **Theorem C 5-way split (P4-G6-44).** Draft prose at W32 §1.2 D17. The proposed replacement opens with "### Theorem C — CE/PV derived-centre theorem (5-way split per M-26)". The "(5-way split per M-26)" subtitle tag must be scrubbed; replacement title: "### Theorem C — CE/PV derived-centre theorem." Body prose names the five lanes C₁ᶠʷ, C₁ᶜᵒᵐᵖ, C₂(NT), C₂(W), C₂(R) with "**Status:** *hypothesis-free*" / "**Status:** *hypothesis package = `\lem:tate-mittag-leffler-dictionary`*" / "**Status:** proved windowwise" / "**Status:** classical part proved (C₂(W)-cl); quantum part (C₂(W)-q) conditional on `prob:weighted-rg-locality` per W3-W6-05" / "**Status:** *admissible-class-canonical, not Costello-canonical*; per W3-W6-04." The "per W3-W6-05" / "per W3-W6-04" tags must be scrubbed. Replacement: cross-reference to the proof inside `tate-T*.tex` ("see Theorem T1.X") or to `claim-strength-ledger.tex`.
  - Critical disclaimer paragraph: "The strict perfect Hamiltonian … does **not** satisfy the Tate-conilpotency hypothesis required by C₁ᶜᵒᵐᵖ; the M-01 perfectness obstruction $[\mathfrak h, \mathfrak h] = \mathfrak h$ forces the truncation/regulator route C₂(NT/W/R). No claim is made for the strict unweighted limit." Scrub "M-01" reference; replace with "the perfectness obstruction $[\mathfrak h, \mathfrak h] = \mathfrak h$ of `\rmk:ce-source-obstruction-disk`." This is a manuscript-internal cross-reference and is acceptable.
- **Obligation II reformulation (P4-G6-45).** Draft prose at W3-W28 §4.4 (lines 407-509). Six paragraphs:
  - Paragraph 1 names "the Fourier-Rees bridge of `\thm:app-matlis-rees-fourier-bridge`" — clean (manuscript-internal label).
  - Paragraph 2 names "involution $\sigma: (a,b) \mapsto (-a-1, -b-1)$; four cones; corrected Cech SES" — clean.
  - Paragraph 3 names "M-29 / W3-W7-01..10" tag — must be scrubbed; replacement: "(see `\thm:universal-categorical-no-go` and the ten attack channels enumerated in its proof)."
  - Paragraph 4 names "(i) bi-infinite local-cohomology / Drinfeld stack (W3-W9-08), (ii) $L_\infty$-categorified bracket with q-difference avenue (W3-W7-05), (iii) supertrace route discharges different obligation, not II." Scrub "(W3-W9-08)" and "(W3-W7-05)" tags; replace with manuscript-internal pointers (or drop entirely if the open-obligations.tex section is self-contained).
  - Paragraph 5 names "(21-case sweep + 165,600-case bi-infinite Lie consistency + per-axis local-nilpotence)" — these are quantitative-honesty notes; verify they match the master ledger / `claim-strength-ledger.tex` figures and inscribe with simple parenthetical (e.g., "(per the verifications inscribed in `scripts/check_bi_infinite_lie_consistency.py`)").
  - Paragraph 6 names "critic's intent" — adversarial-process language; scrub. Replacement: just state the open question declaratively without "critic's intent" framing.
- **Toy lemma promotion (P4-G6-46).** Numbered `lem:` block; the numbering action itself is structural. No process leakage.
- **Obligation VII four-ingredient (P4-G6-47).** Names M-14, M-37 in tags; scrub at inscription.

### §4.4 Process-leakage scrub master pattern

For every Phase-2 / Phase-3 inscription, the author should run:
1. **Strip leading parenthetical tags** of the form "(W3-W13-X)," "(W3-W2X-XX)," "(M-XX / W3-WXX-YY)," "(W3-W32-DXX)," "(P4-G6-XX)." These are scaffolding.
2. **Strip "M-XX" body references**, replacing with manuscript-internal label cross-references (e.g., `\thm:strict-unweighted-no-go` rather than "M-11").
3. **Strip em-dashes**; replace with comma + clause, semicolon, colon, or sentence break.
4. **Strip bracket-numbered references** like "[W3-W7-05]" or "[per W3-W6-04]"; replace with named primary-source citation or manuscript-internal label.
5. **Verify no "wave"/"swarm"/"agent"/"ledger" word appears in the inscribed paragraph.**

Verification check: after scrubbing, the paragraph should read as if written by a single author with deep knowledge of the manuscript's internal labels (theorems, lemmas, propositions, scripts) and the relevant primary sources, with no trace of multi-agent coordination.

---

## §5. T5 — Authorization checklist for user

Three tiers, mapped to the 47 Tier-A + 8 Tier-B + 2 Tier-C count from W32 final consolidation. The user authorizes by tier; G6 inscription proceeds in dependency order.

### §5.1 Tier A (47 edits) — single-batch authorization recommended

**What user authorizes.** All 47 mechanical inscriptions (Phases 1, 2, 3 of §2 above). Each has draft-verified prose at the wave-3 sub-ledger level. Inscription is paragraph-level paste-with-scrub per §4.4 above.

**Tier-A subdivisions (for sanity-check study order).**

| Tier-A bucket | Count | Phase | Files affected |
|---|---|---|---|
| Phase 1: Bib + dictionary | 21 | Phase 1 | `main.tex` (bib block + Theorem E + `\lem:continuous-bar-cobar`); `local-dictionary.tex` (sole) |
| Phase 2: Statement-level prose | 22 | Phase 2 | `main.tex` (Thm A, Thm G, Thm E steps); `principles.tex` (Principle 1); `open-obligations.tex` (Obls III, IV, V, VII); `appendix-factorization-current-conventions.tex` (sign appendix) |
| Phase 3: Structural splits | 4 | Phase 3 | `main.tex` (Theorem C area); `theorem-lanes.tex`; `claim-strength-ledger.tex`; `open-obligations.tex` (Obligation II) |

**Authorization signal.** "Authorize Tier A: inscribe all 47 mechanical edits per the wave-3 final convergence report and W32 edit plan, scrubbing process tags per the Phase-4 G6 roadmap §4."

**Wave-closure consequence.** Tier-A inscription closes 47 sub-ledger residuals at the prose level. The wave-closure verdict from W32 §6.3 then becomes "STABLE CORE INSCRIBED. Wave 3 closed at the manuscript level."

### §5.2 Tier B (8 edits) — sequenced post-Tier-A

**What user authorizes.** Eight downstream propagation edits (Phase 4 in §2.4 above). Each requires a specific Tier-A edit to be inscribed first; verification that the Tier-A inscription landed cleanly is the gate.

**Tier-B members (W32 IDs preserved).**
- W3-W32-W6.1, W6.2, W6.4, W6.5 — Theorem C lane sharpenings to T1 / T3 / T5 / `claim-strength-ledger.tex` (5 edits; gate: P4-G6-44 inscribed).
- W3-W32-W6.3 — `tate-T1` / `tate-P1` dictionary-lemma sharpening (1 edit; gate: Phase 1 dictionary entries inscribed).
- W3-W32-D11 — §7 N1 Symp covariance call-out (1 edit; gate: P4-G6-44).
- W3-W32-D12 — §5 voice apologetic-phrasing scrub (1 edit; gate: Phase-2 prose landed).
- W3-W32-D25 — Symp$_{\rm form}$ per-theorem statement (1 edit; gate: P4-G6-44 + Tier-C Symp_form decision).
- W3-W32-W27.3 — M-03 propagation to `principles.tex` Witten section + `theorem-lanes.tex` (1 edit; gate: P4-G6-22).
- W3-W32-W28.2 — Obligation II propagation to `theorem-lanes.tex` + `claim-strength-ledger.tex` (1 edit; gate: P4-G6-45).

**Authorization signal.** "Authorize Tier B sequenced after Tier A: inscribe the 8 downstream propagation edits per W32 §2.2-§2.7."

### §5.3 Tier C (5 edits) — requires user decision

**What user authorizes.** Five edits requiring a notation-discipline or scope decision before inscription. Each is independent of the others; the user can authorize any subset.

| Tier-C edit | Decision needed | Recommendation (G6 lens) |
|---|---|---|
| **W3-W32-W20.5** (Symp_form symbol) | Inscribe `Symp_{\rm form}(\C^2, 0)` once in dictionary + once at Theorem D₁, OR retain "formal symplectomorphism" prose throughout. Symbol currently used **nowhere** in manuscript. | Inscribe the symbol. Cross-volume firewall (W3-W34 §T5) and master-ledger M-28/M-35 carry "Symp$_{\rm form}$-equivariance" claims; without the symbol the dictionary cannot mediate cross-volume transfer. |
| **W3-W32-W20.12** ($\mathsf F_{\rm Rees}$ symbol) | Retire dictionary symbol (replace with descriptive prose), OR import it into `appendix-matlis-principal-parts.tex` so it earns its keep. | Either is acceptable; G6 lens recommends importing the symbol (lower edit cost, preserves the cross-cite the dictionary entry implies). |
| **W3-W32-W30.1** (regulator-admissible-sector (A5) clause) | Add the parity-equivariance condition $[R_{\epsilon,L}, P]=0$ in `tate-T1-weighted-completion.tex` `\defn:regulator-admissible-sector`. | Authorize. (A5) is verified for every manuscript-cited regulator (W3-W30-02); without (A5), W22-T2 supertrace claim has unspecified parity hypothesis. |
| **W3-W32-W30.2** ((A5) verification) | Verify heat-kernel super-Killing, Pauli–Villars, Hadamard parametrix all satisfy (A5). | Authorize. Routine inscription post W30.1. |
| **W3-W32-W30.3** ((A5) status update) | Update `appendix-unreduced-bv-qme.tex` + W22-T2 status to mark unconditional on $\mathfrak{gl}(N\|N)$ super-balanced. | Authorize. Direct consequence of W30.1 + W30.2. |

**Authorization signal.** "Authorize Tier C subset: {W20.5: inscribe / decline}, {W20.12: retire / wire}, {W30.1, W30.2, W30.3: authorize batch}."

### §5.4 Aggregate authorization plan

A clean three-line authorization completes Wave 3 inscription:

1. "Authorize Tier A (47 edits, Phases 1-3 of the G6 roadmap; scrub process tags per §4)."
2. "Authorize Tier B (8 downstream propagation edits, sequenced after Tier A verification)."
3. "Authorize Tier C: W20.5 inscribe Symp_form; W20.12 wire F_Rees into appendix; W30.1–3 batch (A5) heal."

---

## §6. T6 — Repo hygiene companion items

The session-start `git status` shows a substantial untracked-files list. The G6 editorial pass should be accompanied by, but not blocked on, the following hygiene actions.

### §6.1 Tracking and committing

**Files currently untracked but presumably ready to commit.**
- `appendix-factorization-current-conventions.tex` — sign-appendix that hosts P4-G6-38..40, 42.
- `appendix-matlis-principal-parts.tex` — referenced by P4-G6-11 (Matlis duality dictionary entry).
- `appendix-radial-parts-moyal.tex` — referenced by Theorem F unconditional inscription target (W32 A.4).
- `appendix-unreduced-bv-qme.tex` — referenced by W22-T1 / W22-T2 inscription target (W32 A.2) and W30.3 status update.
- `claim-strength-ledger.tex` — Tier-A receiver for stable-core declaration (W32 A.4) and Tier-B receivers for Theorem C lane sharpenings.
- `local-dictionary.tex` — primary Tier-A receiver (16 dictionary entries P4-G6-06..21).
- `open-obligations.tex` — Tier-A receiver for Obligations II, III, IV, V, VII edits.
- `principles.tex` — Tier-A receiver for P4-G6-26 (Principle 1 divergence-free derivation) and Tier-B for W27.3.
- `theorem-lanes.tex` — Tier-A receiver for Theorem C 5-way split; Tier-B receiver for W6.X lane sharpenings.

**Recommendation.** Before any Tier-A inscription begins, commit the current state of these files (whatever "current" means for each — many appear to be created during wave-3 sub-ledger work). This establishes a clean base for the editorial pass and makes it possible to diff the inscription against the pre-inscription baseline.

### §6.2 Files to scrub or relocate

- `.DS_Store` — macOS Finder artifact; `.gitignore` should exclude.
- `.agents/` — likely worktree coordination scratch; verify against `~/ecosystem/INVARIANTS.md` standalone-documents discipline. If `.agents/` contains private scratch, ensure `.gitignore` lists it; if it contains durable coordination artifacts, move into `reconstitution/` per the every-file-into-the-repo rule (CLAUDE.md inheritance).
- `.claude/` — Claude Code session config; verify `.gitignore` excludes.
- `out/`, `out_test/` — build artifacts; `.gitignore` should exclude (the canonical built PDF lives at `main.pdf` in repo root per Makefile).
- `scripts/__pycache__/` — Python bytecode cache; `.gitignore` should exclude.
- `materials/raw/2026-04-28-*.pdf` and `materials/processed/2026-04-28-*.txt` — primary-source PDFs and their processed text. These are referenced by W3-W23-A "CGW PDF inscription" residual; per CLAUDE.md every-file-into-the-repo rule, they should be tracked. Verify the PDFs are not under separate licensing constraints.
- `frontier_mnop_framing_volume.tex` — flagged as dangling artifact in R-W5-A; per R-W5-A heal, relocate to `reconstitution/` or commit with a clear status (lemma-stub or scratch).

### §6.3 Modified files in the manuscript proper

Per session-start `git status`, the following files have uncommitted modifications (`MM` = staged + unstaged; ` M` = unstaged):
- `abstract.tex`, `commands.tex`, `mathmacros.tex`, `nomenclature.tex`, `notation.tex`, `main.tex`, `main.pdf`, `out/main.pdf`
- `tate-P1-hadamard-mittag-leffler.tex`, `tate-P3-universality.tex`, `tate-P5-cross-volume.tex`
- `tate-T1-weighted-completion.tex` through `tate-T5-chain-level-primitive.tex`
- `scripts/check_moyal_coefficients.py`, `scripts/check_one_psi_homology.py`

**Recommendation.** Before Tier-A inscription, run a status check / diff review: are these modifications already aligned with wave-3 partial integration, or do they conflict? The editorial pass should land on top of a known-clean state. If the existing modifications represent partial wave-3 integration (which they likely do given the scale), commit them with a message naming "wave-3 partial integration" before starting the G6 pass.

### §6.4 Ledger / sub-ledger files

The reconstitution directory contains 70+ wave-1, wave-2, wave-3 sub-ledger files plus a few master-coordination files. None of these should be edited as part of the G6 editorial inscription pass; they are the source of truth for the inscriptions but are themselves write-once documents.

---

## §7. T7 — Git-level sequencing (proposal-only)

The user has not authorized commits as part of this roadmap. The hypothetical commit sequence below is offered for planning, not execution.

### §7.1 Recommended granularity: small commits per phase, not one large per phase

A single mega-commit per phase loses traceability when a downstream Tier-B edit conflicts; a too-fine commit per individual edit creates 47 commits to review. The middle path: cluster commits by **target file** within each phase.

### §7.2 Hypothetical commit sequence

**Phase 0 (pre-inscription hygiene).**
1. `chore(repo): track wave-3 partial-integration artifacts` — commit the `??` files from §6.1 above (`local-dictionary.tex`, `claim-strength-ledger.tex`, `principles.tex`, `theorem-lanes.tex`, `open-obligations.tex`, `appendix-*.tex`) at their current state.
2. `chore(repo): commit wave-3 partial-integration to manuscript files` — commit the modifications to `main.tex`, `mathmacros.tex`, `nomenclature.tex`, `notation.tex`, `tate-T*.tex`, `tate-P*.tex`, etc., describing the wave-3 partial integration that has already landed.
3. `chore(repo): .gitignore for build artifacts and session scratch` — add `.DS_Store`, `out/`, `out_test/`, `scripts/__pycache__/`, `.claude/` to `.gitignore`.

**Phase 1 (bib + dictionary).**
4. `bib: add HKR primary-source bibliography entry` (P4-G6-01).
5. `cite: pin HKR appeals in Theorem E and remark E1-translation to Lurie HA + windowwise classical HKR` (P4-G6-02..04).
6. `lemma: extend lem:continuous-bar-cobar with windowwise Tate-HKR item` (P4-G6-05).
7. `dict: add 16 dictionary entries for Tate, weighted, regulator-admissible, Capelli, factorization-centre, T2-Cartan, scalar-reduced trace, PV, HKR, Matlis, PBW raising` (P4-G6-06..21, single commit since all hit `local-dictionary.tex`).

**Phase 2 (statement-level prose).**
8. `thm-A: M-03 derived intersection promotion at Theorem A preface and Theorem G re-narration` (P4-G6-22).
9. `principles: insert divergence-free + Poincare derivation justifying killed constants in Principle 1` (P4-G6-26).
10. `thm-A: insert A-brane otimes B-brane otimes Koszul derivation of ghost-zero field at Theorem A skeleton` (P4-G6-27).
11. `thm-A: insert local-operator Euler contraction and quotient-stack vs invariant-reduction action items` (P4-G6-28, P4-G6-29).
12. `thm-G: append weight-bidegree decomposition lemma per M-09` (P4-G6-30).
13. `obls: graphwise-bounded != renormalizable + Costello-Li non-applicability + reg-vs-anomaly + strict-unweighted forbidden + bosonic vs gl(N|N) disclaimer` (P4-G6-23, 24, 25, 31, 32) — single commit clustered by `open-obligations.tex` target.
14. `thm-E: tighten Steps 4..8 prose` (P4-G6-33..37).
15. `appendix-conventions: BF-pairing-degree, [1] shift, negative-index zero-target, psi-degree subsections` (P4-G6-38, 39, 40, 42).
16. `notation: append Theta_rho disambiguation row` (P4-G6-41).
17. `obls: structural distribution-product avoidance per M-36` (P4-G6-43).

**Phase 3 (structural splits).**
18. `thm-C: split into 5-way C1/C2 lanes per M-26` (P4-G6-44, single commit hitting `main.tex`, `theorem-lanes.tex`, `claim-strength-ledger.tex`).
19. `obl-II: reformulate per W28-T4 with named no-go and three open escape routes` (P4-G6-45).
20. `lem: promote finite-Lie toy paragraph to numbered lemma` (P4-G6-46).
21. `obl-VII: Weiss-cosheaf-descent four-ingredient adoption per M-14, M-37` (P4-G6-47).

**Phase 4 (Tier-B propagation).**
22-28. Seven commits for Tier-B downstream cross-references (one per Tier-B edit, by target-file cluster).

**Total: ~22 commits in the editorial pass.** Each is a small, reviewable diff; the sequence makes the wave-3 inscription history legible.

### §7.3 Why this granularity, not one mega-commit

- **Reviewability.** A diff per phase per file cluster is small enough to review against the W32 / W17 / W20 / W24 / W27 / W28 draft prose without losing context.
- **Reverse-direction safety.** If a Phase-3 inscription introduces a downstream conflict (e.g., the Theorem C 5-way split conflicts with an existing Theorem C cross-reference somewhere in `tate-T*`), the per-cluster commits make `git revert` precise.
- **Alignment with master ledger entries.** Each commit message references the master-ledger entry (M-XX) it inscribes; the ledger entry then carries the commit-SHA inscription seal in its provenance line, completing the wave-3 → manuscript trace.

### §7.4 What not to do

- **No `--amend` on the wave-3 partial-integration commits already in the history** (per `~/ecosystem/INVARIANTS.md` destructive-git rule). Add new commits.
- **No `--no-verify` on commit hooks** (commit-message format, no-em-dash check, etc., per recent commit history).
- **No "Co-Authored-By: Claude" footers** on Wave-3 inscription commits (per CLAUDE.md inherited rule "commits-carry-no-LLM-attribution").
- **No squashing** of the per-phase per-cluster commits into a mega-commit (loses traceability).

---

## §8. 200-word summary

This roadmap consolidates 47 Tier-A ready-to-inscribe edits aggregated from wave-3 sub-ledgers W17 (HKR), W20 (dictionary), W24 (Theorem E steps), W27 (M-03 promotion), W28 (Obligation II), W30 ((A5)), and the W32 master edit plan covering the 13 W13 dilutions / silent drops. Edits sequence into four phases: (1) bib + dictionary (21 edits, no dependencies), (2) statement-level prose (22 edits, depends on Phase 1 vocabulary), (3) structural splits — Theorem C 5-way and Obligation II reformulation (4 edits, depends on Phases 1-2), (4) Tier-B propagation (8 edits, depends on Phases 1-3). Author-style guidance per CLAUDE.md Russian-school + mathematical-physics-frontier voice: declarative, named-attribution, honest-epistemic-status; no em-dashes, no hedged language, no agent / swarm / wave / ledger / M-XX tags in inscribed prose. Process-leakage scan identifies the specific scaffolding prefixes ("(W3-WXX-YY)," "(M-XX)," section-header tags, ledger-pointer parentheticals) to scrub at inscription. Authorization checklist: Tier A as single 47-edit batch; Tier B sequenced post-Tier-A; Tier C three subsets (Symp_form, F_Rees, (A5) parity batch). Repo hygiene: track wave-3 partial-integration files, scrub `.DS_Store` / build artifacts / session scratch, commit `materials/` PDFs. Hypothetical git sequence: ~22 commits clustered by target-file within phase. Proposal-only.

---

End of Phase-4 G6 editorial roadmap.
