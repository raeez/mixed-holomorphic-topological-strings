# Wave 3 W34 — Residual Catalog and Phase-4 Thematic Organization

**Date.** 2026-04-28.
**Wave.** 3, worker W34 (relaunched after rate-limit).
**Lens.** Kapranov + Functoriality (target-category structure +
equivariance).
**Mode.** META-ORGANIZATION; proposal-only.  No new mathematical
content; no manuscript edits; no master-ledger overwrites.  All new
identifiers prefix `W3-W34-` per master-ledger schema.
**Charter.** Organize residual catalog into Phase-4 thematic groups,
mark dependencies, propose research priorities.  Cross-volume flags
audited.  Output is a hand-off section for the FINAL consolidator and
a master-ledger summary entry.

**Sources.**
- `CLAUDE.md` (platonic ideal voice, harness mode, cross-volume rules)
- `reconstitution/attack-heal-platonic-2026-04-28.md` (master ledger,
  wave-1/2/3 partial; ~3182 lines)
- `open-obligations.tex` (manuscript-internal obligations)
- `reconstitution/platonic-ideal-plan-2026-04-28.md §4`
  (open-obligations package)
- `reconstitution/wave3-W{1..32}*.md` (residual sections only)

---

## §0. Charter

T1 enumerate all residuals (R-01..R-07 + wave-2 + 22+ wave-3).
T2 thematic grouping G1-G8.
T3 dependency DAG.
T4 prioritization P1/P2/P3.
T5 cross-volume flags.
T6 hand-off section for FINAL consolidator.
T7 master-ledger summary entry.

The Kapranov lens forces target-category accounting (which residual
lives in Lie-Mod, which in $L_\infty$-Mod, which in chiral algebra,
which in Tate vector spaces, which in $D_\hbar$-modules); the
Functoriality lens forces equivariance accounting (Symp$_{\rm form}$
canonical vs GL$_2 \times T^2$ equivariant vs admissible-class
canonical vs cross-class).

---

## §T1. Enumeration — every residual at one glance

The catalog below enumerates every residual the master ledger names
across waves 1, 2, and 3 (partial integration to W20 + freshly-launched
W21–W32).  Each row carries provenance (which W produced it), status
(proposal text in the originating sub-ledger), and a one-line
description.

### T1.A. Wave-1 residuals (R-01..R-07)

Source: master ledger §4 (lines 1203–1232).

| ID    | One-line                                                   | Status (post-wave-3-partial)                                  |
|-------|------------------------------------------------------------|----------------------------------------------------------------|
| R-01  | Tate-categorical bar-cobar surviving perfectness            | Partially healed (C₂(R) reformulation + M-27); R-W1-01 successor |
| R-02  | Category-changing $D_\hbar$-module realization              | Closed in negative by M-29; replaced by R-W4-A/B/C            |
| R-03  | Weiss-cosheaf descent on $\R^2 \times \C^2$                | Sharpened by M-37 four ingredients; R-W6-Weiss-defect successor |
| R-04  | Full one-loop QME calculation                               | Sharpened by M-48 sheaf-theoretic descent; $\hbar N$ class fixed by M-47 |
| R-05  | Mittag-Leffler resolution in T3                             | Healed by M-27 `lem:tate-mittag-leffler-dictionary`           |
| R-06  | Standalone Radial–Moyal proof (Theorem F$'$)                | Gated on G escape route per M-51; obstructed at one loop      |
| R-07  | Mixed brane-defect QME + Costello graph realization         | Unchanged; load-bearing Phase-4                               |

### T1.B. Wave-2 residuals (R-W{1,2,4,5,6}-*)

Source: master ledger §C (lines 1885–1972).

| ID                  | One-line                                                            | Status                                  |
|---------------------|---------------------------------------------------------------------|-----------------------------------------|
| R-W1-01             | Symmetric-filtration hypothesis on Tate filtration                  | Expanded to bidirectional by M-43       |
| R-W1-02             | Unified C₂ statement / regulator-independent envelope               | Sharpened by M-45 W-then-RG order       |
| R-W2-A              | Higher-symplectic-dim Symp-equivariance (Hartshorne III.10.10)      | Phase-4; unchanged                      |
| R-W2-B              | (∞,1)-coherence question for moduli stack of branes                | Phase-4; unchanged                      |
| R-W2-C              | PBW-vs-Matlis equivariance asymmetry                                | Editorial Phase-1; unchanged            |
| R-W4-A              | Bi-infinite local-cohomology Hamiltonian-equivariant splitting      | Largely realized (M-40, M-50); residue R-W3-W9-B |
| R-W4-B              | $L_\infty$-categorified bi-residue bracket                          | Phase-4; scope clarified by M-38        |
| R-W4-C              | Unreduced BV factorization-centre lift (= Obligation I)             | Unchanged; load-bearing Phase-4         |
| R-W5-A              | `frontier_mnop_framing_volume.tex` dangling artifact                | Editorial; move to `reconstitution/`    |
| R-W5-B              | Sharpen `lem:no-formal-disk-transfer`                               | Editorial; one-line                     |
| R-W6-Weiss-defect   | Transverse Mittag-Leffler on defect-localised distributions         | Partial discharge by M-39 (Weiss-on-$\R$ done) |

### T1.C. Wave-3 residuals (W1..W32; 22+ entries integrated + relaunched)

Source: master ledger §G partial integration (lines 3081–3122) plus
W21–W32 sub-ledger residual blocks (read directly from sub-ledger
files).

#### Already in master ledger §G (partial integration through W20)

| ID                  | Provenance | One-line                                                                | Severity |
|---------------------|------------|-------------------------------------------------------------------------|----------|
| R-W3-W1-01          | W1         | C-block five different target categories                                | 2-3      |
| R-W3-W1-02          | W1         | Dictionary lemma forward-reference circle (split into exactness + lift) | 2        |
| R-W3-W1-03          | W1         | DAG composition is implication, not derived natural transformation     | 2        |
| R-W3-W1-04          | W1         | Symmetric-filtration hypothesis exterior face                          | 2        |
| R-W3-W1-05          | W1         | M-29 universal scope is Lie-Mod-preserving only                        | 2        |
| R-W3-W2-A           | W2         | Defect-cohomology extension of M-31 — gated on bulk-to-defect kernel   | 3        |
| R-W3-W3-A           | W3         | Bi-infinite parent realized but does not lie in Lie-Mod                | 2        |
| R-W3-W4-A           | W4         | Rigorous wave-front-set on brane line                                  | 3        |
| R-W3-W6-A (=W6-04)  | W6         | Cross-regulator-class canonicity (heat-kernel vs ζ vs PV)              | 3        |
| R-W3-W6-B (=W6-05)  | W6         | C₂(W) quantum extension conditional on weighted-RG locality            | 3        |
| R-W3-W8-A           | W8         | Cross-scheme regulator canonicity beyond admissible class              | 3        |
| R-W3-W8-B           | W8         | W-then-RG order discipline declaration                                 | 1        |
| R-W3-W9-A           | W9         | Weiss-product-stability across non-product covers (open)               | 2        |
| R-W3-W9-B           | W9         | Drinfeld stack / chiral-algebra global section interpretation          | 1-2      |
| R-W3-W10-A          | W10        | Supertrace escape route (resolved by W22 partial)                      | 3        |
| R-W3-W10-B          | W10        | High-N verification script generalization                              | 2        |
| R-W3-W11-A          | W11        | Lurie 5.5.4.10 H2 beyond ML colimits                                   | 3        |
| R-W3-W11-B          | W11        | PV/CE descent diagram (sheaf-theoretic / spectral sequence)            | 2        |
| R-W3-W11-C          | W11        | BD chiral-algebra explicit construction                                 | 3        |
| R-W3-W14-A          | W14        | Wakimoto interpretation of mixed cones                                 | 2 (closed by W21-T1) |
| R-W3-W14-B          | W14        | Brane-configuration realization in 5d twisted M-theory                  | 2-3      |
| R-W3-W15-A          | W15        | F$'$ QME extension closure (gated on G escape route)                    | 3        |
| R-W3-W17-A          | W17        | HKR primary-source bibliography                                         | 1        |
| R-W3-W17-B          | W17        | Tate-extension reasoning formalized                                     | 2        |
| R-W3-W20-A          | W20        | 5 deferred lower-priority dictionary heals                              | 1-2      |

#### Wave-3 W21–W32 (relaunch wave; not yet in master ledger §G)

Read directly from sub-ledger residual blocks; status per W29
coherence audit.

| ID                  | Provenance | One-line                                                                | Severity |
|---------------------|------------|-------------------------------------------------------------------------|----------|
| R-W3-W21-A          | W21        | Čech-equivariance verification of column-Verma                          | 2        |
| R-W3-W21-B          | W21        | Free-field β–γ realization of $\bar A$                                  | 3        |
| R-W3-W21-C          | W21        | $D$-module residue-currents identification of $C^{+-}, C^{-+}$         | 3        |
| R-W3-W21-D          | W21        | Borel-Verma column decomposition categorification                       | 2        |
| R-W3-W22-01         | W22        | Physical embedding into BCOV anti-brane stack ($\mathfrak{gl}(N|N)$)    | 3        |
| R-W3-W22-02         | W22        | All-loop hypothesis on super-balanced QME (cross-class outside admissible) | 3    |
| R-W3-W22-03         | W22        | Chain-level extension of supertrace cancellation                         | 2-3      |
| R-W3-W22-05         | W22        | Physical embedding (parallels R-W3-W22-01)                              | 2        |
| R-W3-W23-A          | W23        | CGW arXiv:2007.09497 PDF inscription                                    | 1        |
| R-W3-W23-B          | W23        | Five-obstruction conditional bridge (5d twisted M-theory)               | 3        |
| R-W3-W23-C          | W23        | $C^{--}$ cone identification with anti-brane sector                     | 3        |
| R-W3-W24-01..05     | W24        | Theorem E Step 4..8 editorial heals (biderivation, bidirectional, etc.) | 1-2      |
| R-W3-W25-03         | W25        | Parity-equivariant regulator class classification                        | 2        |
| R-W3-W25-06         | W25        | Brane–anti-brane physical interpretation                                 | 2        |
| R-W3-W26-A          | W26        | Symp$_{\mathrm{form}}$-natural realization of column-Verma redirect      | 3        |
| R-W3-W26-B          | W26        | Categorification of column-Verma decomposition                           | 2        |
| R-W3-W26-C          | W26        | Higher-order Borel attribution                                           | 3        |
| R-W3-W29-A          | W29        | Cross-walk W14 four-cone vs W22 super-extension (orthogonality)         | 1        |
| R-W3-W29-B          | W29        | W19 algebraic-Moyal strict M-31 vs W21 column-Verma at $z_1 z_2$        | 2        |
| R-W3-W29-C          | W29        | Explicit σ_swap action on $\mathrm{Str}\,\psi$ at $\mathfrak{gl}(1|1)$  | 1        |
| R-W3-W30-A          | W30        | Cross-class canonicity outside (A1)–(A5) admissible class                | 3        |
| R-W3-W30-B          | W30        | Combined (A5) + bilinear-form-derived sufficiency verification          | 2        |
| R-W3-W31-A          | W31        | 5d twisted M-theory bridge (five-obstruction conditional)                | 4        |
| R-W3-W31-B          | W31        | Topological-twist obstruction                                            | 4        |
| R-W3-W31-C          | W31        | $\hbar \leftrightarrow$ spectral-parameter dimensional bridge            | 3        |
| R-W3-W18-01..07     | W18        | CT1 super-balanced Phase-3/4 follow-ups (Theorem B + escape routes)     | 2-3      |
| R-W3-W12-A          | W12        | Four-cone explicit verification (165,600 instances inscribed; durable)  | 1 (closed) |

**Total enumerated:** 7 (R-01..07) + 11 (R-W{1,2,4,5,6}-*) + 50+
(R-W3-W*-*) ≈ 70 residuals across all three waves.

---

## §T2. Thematic grouping G1..G8 (Kapranov + Functoriality lens)

The Kapranov lens reveals that residuals naturally cluster by
*target category* and *equivariance class*.  Eight thematic groups
emerge.

### G1. Weiss / factorization beyond $\R$ (target category: cosheaf on $\R^2 \times \C^2$ codim-4 strata)

**Members.**
- R-03 (wave-1; sharpened to four ingredients by M-37)
- R-W6-Weiss-defect (wave-2; partial discharge by M-39)
- R-W3-W2-A (defect-cohomology extension of M-31 — gated)
- R-W3-W4-A (rigorous wave-front-set on brane line)
- R-W3-W9-A (Weiss-product-stability across non-product covers)
- R-W3-W11-C (BD chiral-algebra explicit construction)
- R-W3-W24-04 (Theorem E Step 7 prose: "degree zero" precision)

**Common structure.**  Move from brane-line $\R$ (discharged) to
ambient $\R^2 \times \C^2$.  Residue currents on a codim-4
holomorphic subspace.  Beilinson–Drinfeld chiral-algebra
factorization is the candidate framework; $E_1$-degeneration of the
weight spectral sequence (M-48 W3-W11-04) is the hypothesis-bearer.

**Functoriality.**  Symp$_{\mathrm{form}}(\widehat{\C^2}_0)$
canonical on closed side; GL$_2 \times T^2$-equivariant on open
side per M-42.  Cross-class behaviour outside admissible regulator
is governed by R-W3-W6-A (= W6-04).

### G2. Bi-infinite parent / $\Z^2$ cones (target category: Z²-graded vector spaces with cone-by-cone Lie-module structure)

**Members.**
- R-02 (wave-1; closed in negative for Lie-Mod)
- R-W4-A (wave-2; largely realized; chiral-algebra residue R-W3-W9-B)
- R-W4-B ($L_\infty$-categorified bi-residue bracket)
- R-W3-W3-A (bi-infinite parent does not lie in Lie-Mod)
- R-W3-W3-B (positive realization as Laurent$/\C$)
- R-W3-W3-C (mixed-cone Z²-graded subspaces NEW)
- R-W3-W14-A (Wakimoto interpretation; closed by W21-T1)
- R-W3-W14-B (5d brane-configuration realization)
- R-W3-W21-A/B/C/D (column-Verma + free-field + D-module residues + categorification)
- R-W3-W26-A/B/C (Symp$_{\rm form}$-natural redirect; categorification; higher-order Borel)
- R-W3-W29-A (W14-cone × W22-super orthogonality)
- R-W3-W29-B (W19-Moyal × W21-column-Verma at $z_1 z_2$)

**Common structure.**  Four-cone canonical filtration of bi-infinite
parent on $\Z^2 \setminus \{(0,0)\}$ per M-50: only $C^{++}$ is
sub-Lie-module; $C^{--}$ closed quotient; mixed cones $C^{+-},
C^{-+}$ Wakimoto-type tensor-factorized parabolic-induced modules.
$\sigma$-conjugacy exchanges mixed cones at the second filtration
step.  Residue-pairing realized at 165,600 commutator instances
(M-49 / W12 inscription).

**Functoriality.**  T²-Cartan rigidity preserved across all four
cones (M-28 D₂ + W7 deep confirmation).  M-29 strengthened to
mixed cones via per-axis local-nilpotence argument (M-50).

### G3. Supertrace / QME on super-balanced (target category: $\mathfrak{gl}(N|M)$-modules; (A5) heal; super-coefficient layer)

**Members.**
- R-04 (wave-1; full one-loop QME)
- R-07 (wave-1; mixed brane-defect QME)
- R-W3-W6-B (= W6-05; C₂(W) quantum gated on weighted-RG locality)
- R-W3-W10-A (supertrace escape route)
- R-W3-W10-B (high-N verification script generalization)
- R-W3-W15-A (F$'$ QME extension closure)
- R-W3-W18-01..07 (CT1 super-balanced Phase-3/4 follow-ups)
- R-W3-W22-01/02/03/05 (super-balanced QME; physical embedding; chain-level)
- R-W3-W25-03/06 (parity-equivariant regulator; brane–anti-brane interpretation)
- R-W3-W30-A/B (cross-class canonicity outside (A1)–(A5); combined verification)
- R-W3-W29-C (σ_swap on $\mathrm{Str}\,\psi$ at $\mathfrak{gl}(1|1)$)

**Common structure.**  M-47 / W3-W10-01 closes
`prob:weighted-rg-locality` in the negative on standard $\mathfrak{gl}_N$:
one-loop anomaly = $\hbar N$ exactly = the $[\bar c]$ class.
Three named escape routes per `rmk:app-scalar-contact-escape-routes`:
(a) super-balanced $\mathfrak{gl}(N|N)$ via supertrace (W22, W25
verify at chain level on parity-equivariant admissible regulator);
(b) central-character $\chi(I) = 0$ (Etingof escape, partially
verified by W22/W30 (A5) heal); (c) unreduced primitive (Phase-4
research).

**Functoriality.**  Super-balanced canonical at the coefficient
layer; cross-class behaviour outside admissible regulator inherits
R-W3-W6-A territory.

### G4. Cross-volume / 5d M-theory (target category: comparison stack; matched-conventions theorem datum)

**Members.**
- R-W5-A (`frontier_mnop_framing_volume.tex` dangling)
- R-W5-B (sharpen `lem:no-formal-disk-transfer`)
- R-W3-W16-A/B/C/D/E/F (8 D-divergence sites for cross-volume firewall)
- R-W3-W18-07 (BCOV physical interpretation — cross-volume gate)
- R-W3-W22-01 (BCOV anti-brane physical embedding)
- R-W3-W23-A (CGW 2007.09497 PDF inscription)
- R-W3-W23-B (5d twisted M-theory five-obstruction conditional)
- R-W3-W23-C (anti-brane / $C^{--}$ cone identification)
- R-W3-W31-A (5d twisted M-theory bridge — five-obstruction conditional)
- R-W3-W31-B (topological-twist obstruction)
- R-W3-W31-C ($\hbar \leftrightarrow$ spectral-parameter dimensional bridge)

**Common structure.**  CLAUDE.md cross-volume rule is unambiguous:
treat as context unless local theorem proves precise comparison.
M-34 (W5) cross-volume firewall, sharpened by M-52 (W3-W16) at 8
named D-divergence sites, names exactly which slot / dimension /
direction is in force on the TS side.  None of these residuals
imply a consequence of the local Hamiltonian BF/Moyal calculation
in absence of a separate matched-conventions theorem.

**Functoriality.**  Symp$_{\rm form}$ does NOT lift to Aut(K3)
(M-42 / W3-W5-03/04 cross-confirmed by W3-W16-D6); only
GL$_2 \times T^2$ subgroup transfers.  All cross-volume residuals
inherit this limited functoriality.

**Cross-volume firewall status.** **INTACT.**  Per W3-W29 coherence
audit: zero residual asserts a cross-volume consequence.

### G5. Conditional theorems unconditionalization (F$'$ escape routes; F lives inside F$'$ status)

**Members.**
- R-06 (wave-1; standalone Radial–Moyal)
- R-W3-W15-A (F$'$ QME extension closure on G escape route)
- R-W3-W18-01..07 (CT1 super-balanced — same boundary as F$'$)
- R-W3-W19-01..03 (M-31 chain-level extensibility; Harish-Chandra–Wallach radial; descendant lift)
- R-W3-W22-02 (all-loop super-balanced QME hypothesis)

**Common structure.**  M-51 (W15) classification: F unconditional
inside algebraic finite model; F$'$ gated on
`prob:weighted-rg-locality`; G unconditional.  M-54 (W19) sharpens
M-31 to chain-level strict identification on algebraic Moyal core.
F lives inside F$'$ as $\hbar = 0$ associated graded.  Discharge
of F$'$ requires either (a) an admissible-class regulator with
escape route (super-balanced verified by W22-T1, W22-T2;
central-character partial via W30); or (b) cross-class extension
of admissibility (R-W3-W6-A territory).

**Functoriality.**  Algebraic Moyal core is GL$_2 \times T^2$-
equivariant; descendant sector inherits same equivariance ceiling
(M-42).

### G6. Editorial / dictionary (target category: prose; macro hygiene; bibliography)

**Members.**
- R-W2-C (PBW-vs-Matlis equivariance asymmetry; editorial Phase-1)
- R-W5-A (`frontier_mnop_framing_volume.tex` dangling artifact)
- R-W5-B (sharpen `lem:no-formal-disk-transfer`)
- R-W3-W8-B (W-then-RG order declaration)
- R-W3-W9-B (Drinfeld stack canonicity prose; 1-paragraph note)
- R-W3-W17-A (HKR primary-source bibliography)
- R-W3-W17-B (Tate-extension reasoning formalized)
- R-W3-W20-A (5 deferred lower-priority dictionary heals)
- R-W3-W23-A (CGW 2007.09497 PDF inscription)
- R-W3-W24-01..05 (Theorem E Step 4..8 editorial heals)
- R-W3-W29-A/B/C (W29 coherence cross-walks; non-core)

**Common structure.**  Manuscript editorial work that does not
introduce new mathematical content.  All inscribable inside Phase-1
(immediate) or Phase-2 (manuscript-prose).

**Functoriality.**  Local-dictionary terms must be inscribed in
their canonical equivariance class: $\widehat{\mathbf S}_{\rm Tate}$,
Symp$_{\rm form}$, Capelli, T²-Cartan rigidity, $[\bar c] \leftrightarrow
[\mathrm{Tr}\,\psi]_{\rm BV}$ all carry equivariance metadata that
must travel with the term in any cross-cite.

### G7. Obligation II reformulation (covered by W28)

**Members.**
- R-02 (wave-1; closed in negative)
- R-W4-A (wave-2; bi-infinite parent realized M-40)
- R-W4-B ($L_\infty$-categorified)
- R-W4-C (unreduced BV factorization-centre lift = Obligation I)
- R-W3-W3-B/C (positive realization; mixed-cone subspaces NEW)
- R-W3-W9-B (chiral-algebra global section reformulation)

**Common structure.**  W28 sub-ledger explicitly covers the
Obligation II reformulation.  Two genuine open Phase-4 questions
remain (per W28 §6 verbatim):  (i) bi-infinite parent realized as
explicit local-cohomology construction (Drinfeld stack
reformulation); (ii) categorical extensions to $L_\infty$-Mod
where M-29 universal no-go does not apply.

**Functoriality.**  W28 redirects R-W4-A from "open speculation" to
"explicit construction outside Lie-Mod"; the residual is whether the
construction factors through any of the five named extensions of
M-29 (which it does not in Lie-Mod, but might in $L_\infty$-Mod or
chiral algebra).

### G8. Other / coherence cross-walks / target-category bookkeeping

**Members.**
- R-W1-01 (symmetric-filtration hypothesis on Tate)
- R-W1-02 (regulator-independent envelope)
- R-W2-A (higher-symplectic-dim Symp-equivariance)
- R-W2-B (∞,1-coherence question for moduli stack)
- R-W3-W1-01 (C-block five different target categories)
- R-W3-W1-02 (dictionary lemma forward-reference circle)
- R-W3-W1-03 (DAG composition is implication)
- R-W3-W1-04 (symmetric filtration on exterior face)
- R-W3-W1-05 (M-29 universal scope is Lie-Mod-preserving only)
- R-W3-W6-A (cross-regulator-class canonicity)
- R-W3-W6-B (C₂(W) quantum extension)
- R-W3-W8-A (cross-scheme regulator canonicity)
- R-W3-W11-A (Lurie 5.5.4.10 H2 beyond ML)
- R-W3-W11-B (PV/CE descent diagram)

**Common structure.**  Target-category bookkeeping and coherence
between the C-block five splits, dictionary-lemma layering, DAG
phrasing, regulator-class boundary semantics.  These are the
Kapranov-lens residuals proper: not "what is missing from a proof"
but "which target ∞-category does this statement live in, and is
it the same as that one's target."

**Functoriality.**  Regulator-class canonicity is the
functoriality boundary inside admissible class (W3-W6-04 / W3-W8-05);
cross-class behaviour is genuinely open Phase-4.

---

## §T3. Dependency DAG

The dependency relations between groups, marked at the residual
level.  Notation: **A → B** means residual A is a precondition for
residual B (B cannot close until A is at least partially discharged).

### T3.A. Within-group dependencies (selected)

**G1 (Weiss):** R-03 → M-37 four ingredients → R-W6-Weiss-defect →
{R-W3-W2-A, R-W3-W4-A, R-W3-W9-A, R-W3-W11-C, R-W3-W24-04}.
Ingredient 4 (transverse ML) is the genuinely beyond-reach
component.

**G2 (Z² cones):** R-02 closed-in-negative → R-W4-A realized
(M-40, M-50) → {R-W3-W3-B/C, R-W3-W14-A/B, R-W3-W21-A/B/C/D,
R-W3-W26-A/B/C}.  M-29 universal no-go bounds the entire group
at Lie-Mod level; R-W4-B / chiral-algebra (R-W3-W9-B) is the
target-category escape.

**G3 (Supertrace / QME):** M-47 closes
`prob:weighted-rg-locality` → R-04 / R-07 sharpened to require
escape route → {R-W3-W6-B, R-W3-W10-A/B, R-W3-W15-A,
R-W3-W18-01..07, R-W3-W22-01..05, R-W3-W25-03/06, R-W3-W30-A/B}.
W22 super-balanced + W30 (A5) heal partial discharge at chain
level.

**G4 (Cross-volume):** R-W5-A/B → M-34 firewall → M-52 (W16) 8
divergence sites → {R-W3-W16-A..F, R-W3-W23-A/B/C, R-W3-W31-A/B/C}.
None imply a manuscript claim absent matched-conventions theorem.

**G5 (Conditional unconditionalization):** R-06 → F$'$ gated on G
→ {R-W3-W15-A, R-W3-W18-01..07, R-W3-W19-01..03, R-W3-W22-02}.
G3 escape routes are the discharge pathway.

**G6 (Editorial):** independent of mathematical residuals; close
in Phase-1 / Phase-2.

**G7 (Obligation II):** R-02 closed → R-W4-A realized →
{R-W4-B, R-W4-C, R-W3-W3-B/C, R-W3-W9-B}.  W28 covers reformulation.

**G8 (Coherence):** R-W1-01 → C-block stability → {R-W3-W1-01..05,
R-W3-W6-A/B, R-W3-W8-A, R-W3-W11-A/B}.  Layered dictionary lemma
(M-27 → exactness + lift split) is the structural backbone.

### T3.B. Cross-group dependencies (Kapranov + Functoriality)

```
                                ┌── G7 (Obligation II) ────┐
                                │   R-W4-{A,B,C}, M-29     │
                                │                          │
                                ▼                          │
G2 (Z² cones) ───────────► G1 (Weiss / factorization) ◄────┤
  R-W4-A realized              R-03 → M-37                 │
  M-29 mixed cones             R-W6-Weiss-defect           │
  M-50 4-cone filtration       R-W3-W2-A bulk-to-defect    │
                                │                          │
                                ▼                          │
                              G5 (F$'$ unconditionalization)│
                                F$'$ gated on G            │
                                │                          │
                                ▼                          │
                              G3 (Supertrace / QME)        │
                                M-47 ℏN closure            │
                                W22 / W25 / W30 heal       │
                                R-W3-W6-B QME extension    │
                                                           │
G8 (Coherence) ◄────── feeds all groups via target-category
  R-W1-01, R-W3-W1-{01..05}, R-W3-W6-{A,B}, R-W3-W8-A,
  R-W3-W11-{A,B}                                           │
                                                           │
G4 (Cross-volume) ◄─── orthogonal; firewall intact ◄───────┘
  R-W3-W16-{A..F}, R-W3-W23-{A,B,C}, R-W3-W31-{A,B,C}
  M-34, M-52
                                                           
G6 (Editorial) ◄─── orthogonal; Phase-1 / Phase-2          
```

**Cross-group implications.**

1. **G2 → G1.** The bi-infinite parent's chiral-algebra
   reformulation (R-W3-W9-B) is a *necessary precursor* for the
   BD chiral-algebra explicit construction in G1 (R-W3-W11-C):
   the codim-4 transverse ML ingredient lives precisely on the
   bi-infinite Z² lattice.

2. **G2 + G1 → G7.** Obligation II's reformulation as
   chiral-algebra-on-$\mathrm{Ran}(\C^2)$ stack-cohomology problem
   (W28 + M-46 / W9) requires both the bi-infinite parent (G2)
   and the Weiss-defect / chiral-algebra factorization (G1).

3. **G3 → G5.** F$'$ unconditionalization requires G3 escape
   route (super-balanced; central-character; unreduced primitive).
   M-51 / W15 establishes the gating; W22 / W25 / W30 partial
   discharge.

4. **G8 → all.** Coherence residuals (target-category, regulator-
   class) feed into every other group as exterior-face hypotheses.
   Any quantum extension of any other-group claim inherits
   R-W3-W6-A/B and R-W3-W8-A territory.

5. **G4 ⊥ all.** Cross-volume residuals are orthogonal to the
   manuscript proper.  Discharging any of them requires a separate
   matched-conventions theorem (W28-template); does not feed back
   into the local stable core.

6. **G6 ⊥ all (mathematical).** Editorial residuals are orthogonal
   to mathematical content; their discharge unlocks Phase-1 /
   Phase-2 manuscript inscription.

---

## §T4. Prioritization P1 / P2 / P3

Three priority tiers, ordered by load-bearing weight on the
manuscript's stable core.

### P1 — load-bearing for the stable core (Phase-1 / Phase-2 inscription)

These residuals are precise, have known closure pathways, and their
discharge is required for the stable core to be cleanly stated in
the manuscript.  Inscribing the heals is editorial / proof-prose
work, not new research.

| Priority | ID                    | Group | Why P1                                                                |
|----------|-----------------------|-------|-----------------------------------------------------------------------|
| P1.1     | R-W3-W17-A/B          | G6    | HKR primary-source bibliography (5 one-line heals; M-53)              |
| P1.2     | R-W3-W20-A            | G6    | 5 deferred dictionary heals (Phase-1 closure of naming-convention drift) |
| P1.3     | R-W3-W24-01..05       | G6    | Theorem E Step 4..8 editorial heals (biderivation, bidirectional, n-tuple) |
| P1.4     | R-W3-W8-B             | G6/G8 | W-then-RG order declaration (load-bearing for any quantum lane narration) |
| P1.5     | R-W3-W1-02            | G8    | Dictionary lemma split (exactness + lift); fixes M-27 forward-reference |
| P1.6     | R-W1-01 (bidirectional)| G8   | Symmetric-filtration hypothesis (M-43 expansion); exterior face of C₁ᶜᵒᵐᵖ |
| P1.7     | R-W3-W6-B             | G3/G8 | C₂(W)-q gating on weighted-RG locality; reach-state of stable core    |
| P1.8     | R-W3-W11-B            | G8    | PV/CE descent diagram (sheaf-theoretic; Phase-2 prose)                |
| P1.9     | R-W5-A/B              | G6    | Dangling artifact relocation; one-line `lem:no-formal-disk-transfer` heal |
| P1.10    | R-W3-W12-A            | G2    | Inscribe `scripts/check_bi_infinite_lie_consistency.py` durably (closed) |

**P1 closure objective.**  Inscribe these heals into the manuscript
or cross-volume inheritance documents, completing the stable-core
declaration with all admissibility hypotheses on exterior faces.

### P2 — important but not load-bearing (Phase-2 / Phase-3 inscription)

These residuals sharpen the stable core or add to its robustness;
not strictly required for the stable core to ship.

| Priority | ID                    | Group | Why P2                                                                |
|----------|-----------------------|-------|-----------------------------------------------------------------------|
| P2.1     | R-W3-W3-A             | G2    | Bi-infinite parent does not lie in Lie-Mod (consistent with M-29)     |
| P2.2     | R-W3-W14-A (closed)   | G2    | Wakimoto interpretation closed by W21-T1                              |
| P2.3     | R-W3-W21-A            | G2    | Čech-equivariance verification of column-Verma                        |
| P2.4     | R-W3-W21-D            | G2    | Borel-Verma column decomposition categorification                     |
| P2.5     | R-W3-W26-B            | G2    | Categorification of column-Verma decomposition                        |
| P2.6     | R-W3-W29-A/B/C        | G2/G6 | W29 cross-walk verification (orthogonality, $z_1 z_2$, σ_swap)        |
| P2.7     | R-W3-W4-A             | G1    | Rigorous wave-front-set on brane line                                 |
| P2.8     | R-W3-W10-B            | G3    | High-N verification script generalization                              |
| P2.9     | R-W3-W18-01..04       | G3/G5 | Theorem B + escape routes follow-ups (CT1 super-balanced)             |
| P2.10    | R-W3-W22-03           | G3    | Chain-level extension of supertrace cancellation                      |
| P2.11    | R-W3-W25-03/06        | G3    | Parity-equivariant regulator + brane–anti-brane interpretation        |
| P2.12    | R-W3-W30-B            | G3    | Combined (A5) + bilinear-form-derived sufficiency verification        |
| P2.13    | R-W2-A/B/C            | G6/G8 | Higher-dim Symp; ∞-coherence; PBW-vs-Matlis editorial                 |
| P2.14    | R-W3-W1-01/03/04/05   | G8    | C-block target-category gaps; DAG phrasing; M-29 scope                |

### P3 — Phase-4 frontier research (no immediate inscription)

These residuals are genuine research problems; their discharge
requires new mathematical content (not editorial / prose work).

| Priority | ID                       | Group | Why P3                                                              |
|----------|--------------------------|-------|---------------------------------------------------------------------|
| P3.1     | R-03 / R-W6-Weiss-defect | G1    | Transverse ML on defect-localised distributions (codim-4)           |
| P3.2     | R-W3-W2-A                | G1    | Defect-cohomology extension of M-31 (gated on bulk-to-defect kernel)|
| P3.3     | R-W3-W9-A                | G1    | Weiss-product-stability across non-product covers                   |
| P3.4     | R-W3-W11-A               | G1/G8 | Lurie 5.5.4.10 H2 beyond ML colimits                                |
| P3.5     | R-W3-W11-C               | G1    | BD chiral-algebra explicit construction                              |
| P3.6     | R-W4-B                   | G2    | $L_\infty$-categorified bi-residue bracket                           |
| P3.7     | R-W4-C / R-07 (Obl I)    | G7    | Unreduced BV factorization-centre lift                              |
| P3.8     | R-W3-W3-C                | G2    | Mixed-cone Z²-graded subspaces NEW (combinatorial structure)        |
| P3.9     | R-W3-W21-B/C             | G2    | Free-field β–γ realization; D-module residue currents               |
| P3.10    | R-W3-W22-01/02/05        | G3    | Physical embedding into BCOV anti-brane; all-loop super-balanced    |
| P3.11    | R-W3-W26-A/C             | G2/G3 | Symp$_{\rm form}$-natural redirect; higher-order Borel              |
| P3.12    | R-W3-W30-A               | G3/G8 | Cross-class canonicity outside (A1)–(A5) admissible class           |
| P3.13    | R-W3-W6-A                | G8    | Cross-regulator-class canonicity (heat-kernel vs ζ vs PV)           |
| P3.14    | R-W3-W8-A                | G8    | Cross-scheme regulator canonicity beyond admissible class           |
| P3.15    | R-W3-W15-A / R-06        | G5    | F$'$ QME extension closure (gated on G3 escape route)               |
| P3.16    | R-W3-W19-01..03          | G3/G5 | M-31 chain-level extensibility; Harish-Chandra–Wallach radial       |
| P3.17    | R-04 / R-07              | G3/G5 | Full one-loop QME + Costello graph realization                       |
| P3.18    | R-W3-W31-A/B/C           | G4    | 5d twisted M-theory bridge; topological-twist; spectral-parameter   |
| P3.19    | R-W3-W23-B/C             | G4    | Five-obstruction conditional bridge; anti-brane / $C^{--}$ identification |
| P3.20    | R-W3-W16-A..F            | G4    | 8 D-divergence sites for cross-volume firewall                       |
| P3.21    | R-W3-W18-05..07          | G3/G4 | Conjecture W18-C3 parallel Costello-RG factorization; BCOV physical |

---

## §T5. Cross-volume flags

Per CLAUDE.md cross-volume rule, cross-volume residuals are flagged
explicitly.  None imply a manuscript-internal claim.

### T5.A. Vol III (calabi-yau-quantum-groups; CY-to-chiral frontier)

| Flag ID                  | Residual              | Cross-volume status                              |
|--------------------------|-----------------------|--------------------------------------------------|
| CV-VolIII-1              | R-W5-A                | Editorial: relocate dangling Vol-III-referencing artifact |
| CV-VolIII-2              | R-W5-B                | Editorial: sharpen `lem:no-formal-disk-transfer` |
| CV-VolIII-3              | R-W3-W16-A            | Poisson sign vs Schouten degree divergence       |
| CV-VolIII-4              | R-W3-W16-B            | $\hbar$ as adimensional vs spectral              |
| CV-VolIII-5              | R-W3-W16-C            | $\mathfrak{gl}_N$ vs $\mathfrak{sl}_N$ scalar    |
| CV-VolIII-6              | R-W3-W16-D            | Symp$_{\rm form}$ vs Aut(K3) functoriality       |
| CV-VolIII-7              | R-W3-W16-E            | Tate vs $\Z$-graded vs cohomological             |
| CV-VolIII-8              | R-W3-W16-F            | Cyclic/trace pairing sign                        |
| CV-VolIII-9              | R-W3-W18-07           | BCOV physical interpretation of CT1 super-balanced |
| CV-VolIII-10             | R-W3-W22-01           | Physical embedding into BCOV anti-brane stack    |
| CV-VolIII-11             | R-W3-W23-C            | $C^{--}$ cone identification with anti-brane sector |

### T5.B. 5d twisted M-theory (CGW arXiv:2007.09497)

| Flag ID                  | Residual              | Cross-volume status                              |
|--------------------------|-----------------------|--------------------------------------------------|
| CV-5dM-1                 | R-W3-W23-A            | Inscribe primary-source PDF in `materials/raw/`  |
| CV-5dM-2                 | R-W3-W23-B            | Five-obstruction conditional bridge              |
| CV-5dM-3                 | R-W3-W31-A            | 5d twisted M-theory bridge — five-obstruction conditional |
| CV-5dM-4                 | R-W3-W31-B            | Topological-twist obstruction                    |
| CV-5dM-5                 | R-W3-W31-C            | $\hbar \leftrightarrow$ spectral-parameter       |
| CV-5dM-6                 | R-W3-W14-B            | Brane-configuration realization in 5d twisted M-theory |

### T5.C. Igusa $\Delta_5$ / BKM / Borcherds (igusa-cusp-form)

No active residuals at this layer.  Per CLAUDE.md modular-form
frontier paragraph: heuristic and convention-checking bridge only;
no theorems imported.  W3-W34 audit confirms no Igusa / BKM /
Borcherds invocation in any wave-1/2/3 residual.

### T5.D. Firewall verdict

**Cross-volume firewall: INTACT.**  Per W3-W29 coherence audit and
W3-W34 cross-walk:
- Zero residual asserts a cross-volume consequence as a manuscript
  claim.
- Every cross-volume residual is named exactly as a divergence
  site, dangling artifact, primary-source inscription gap, or
  conditional bridge.
- W28 obligations-template ensures any future cross-volume transfer
  begins from a separately matched-conventions theorem.

---

## §T6. Hand-off section for FINAL consolidator

The FINAL consolidator should expect the following actionables from
W34's organization.

### T6.A. Master-ledger inscription ordering (proposal)

When inscribing W3-W34 into the master ledger §G (or §H if W29 occupies
§G), use the following sequence:

1. **§G-W34-1 — Thematic group statement.** One paragraph naming
   G1..G8.
2. **§G-W34-2 — Dependency DAG figure.** Inscribe the cross-group
   diagram in §T3.B above.
3. **§G-W34-3 — Prioritization table.** Inscribe P1/P2/P3 tables in
   §T4 above.
4. **§G-W34-4 — Cross-volume firewall verdict.** Reaffirm INTACT
   per §T5.D.
5. **§G-W34-5 — Phase-4 research roadmap.** Translate P3 entries into
   a research roadmap addressed to the next year's labour budget.

### T6.B. Sub-ledger corrections and discharges to inscribe

The FINAL consolidator should inscribe the following discharges (per
W29 / W22 / W21 / W26 cross-walks already established):

1. **R-W3-W14-A discharge** by W21-T1 (column-Verma) and W26-T1
   (Symp$_{\rm form}$-natural partial); redirect as R-W3-W26-A.
2. **R-W3-W6-B partial closure** by W22-T1, W22-T2 super-balanced
   QME on parity-equivariant admissible regulator (verified at chain
   level); residue is cross-class canonicity (R-W3-W6-A territory).
3. **R-W4-A largely realized** by M-40 + M-50; chiral-algebra
   global-section formulation continues as R-W3-W9-B.
4. **R-05 closed** by M-27 (`lem:tate-mittag-leffler-dictionary`).
5. **R-02 closed in negative** by M-29 universal categorical no-go;
   R-W4-A/B/C are the precise successors.

### T6.C. Pending sub-ledger integration

The FINAL consolidator should integrate the following wave-3 sub-
ledgers if they have not yet been absorbed at master-ledger §G:

- **W13** (critique-fidelity): stalled and relaunched; defer.
- **W18** (Theorem B + escape routes): cross-walk against
  M-04/M-05/M-35 and QME escape routes; integrate as M-XX.
- **W21** (Wakimoto): integrate as M-XX with R-W3-W14-A discharge.
- **W22** (supertrace): integrate as M-XX with R-W3-W10-A partial
  discharge.
- **W23** (5d M-theory σ-swap): integrate as M-XX (cross-volume,
  firewall-respecting).
- **W24** (Theorem E steps): integrate as M-XX with editorial heals.
- **W25** (supertrace verification): integrate as M-XX.
- **W26** (column-Verma): integrate as M-XX with R-W3-W14-A
  discharge classification.
- **W27** (M-03 BV-derived): integrate as M-XX.
- **W28** (Obligation II): integrate as M-XX with reformulation
  verbatim.
- **W29** (coherence audit): integrate as the meta-audit covering
  W12 / W14 / W26 cross-walks.
- **W30** (A5 heal): integrate as M-XX with R-W3-W30-A/B residuals.
- **W31** (5d M-theory obstructions): integrate as M-XX with
  R-W3-W31-A/B/C residuals.
- **W32** (edit plan): integrate as Phase-2 inscription plan.

### T6.D. Phase-4 research roadmap (P3 translation)

For the next Phase-4 research cycle, the highest-impact residuals
are (in order of mathematical centrality):

1. **G7 / R-W4-C (Obligation I — unreduced BV factorization-centre lift).**  Solving this unifies G2 (bi-infinite parent) with G1 (Weiss-defect) at the structural level and discharges R-04 + R-07.  The W28 reformulation as chiral-algebra-on-$\mathrm{Ran}(\C^2)$ stack-cohomology problem provides the framework.

2. **G3 / R-04 (full one-loop QME + super-balanced extension).**  W22 / W25 / W30 partial discharge on parity-equivariant admissible regulator is the chain-level path; cross-class extension is genuinely open (R-W3-W6-A).  Solving this discharges F$'$ unconditionalization (G5).

3. **G1 / R-03 ingredient 4 (transverse ML on codim-4 holomorphic subspace).**  Beilinson–Drinfeld chiral-algebra factorization is the candidate framework; explicitly stated by M-37 / M-46 / M-48.  Solving this discharges defect-cohomology extension (R-W3-W2-A) and full Weiss-cosheaf descent.

4. **G2 / R-W4-B ($L_\infty$-categorified bi-residue bracket).**  Per M-38 scope clarification, $L_\infty$-Mod sits outside the M-29 universal no-go.  This is the legitimate target-category escape from R-02; constructing the $L_\infty$ deformation discharges Obligation II's categorical-extension question.

5. **G4 / R-W3-W31-A (5d twisted M-theory bridge).**  Five-obstruction conditional per W31 §T1; not load-bearing on local stable core but a separate frontier.  Discharge requires CGW PDF inscription (CV-5dM-1) + matched-conventions theorem.

---

## §T7. Master-ledger summary entry (proposed)

**Schema-compliant entry for inclusion in master ledger §G or §H.**

### M-XX (W3-W34) — Residual catalog and Phase-4 thematic organization

**Severity 2 (META-organization, not new mathematics). Status valid. Confidence high.**
**Lens.** Kapranov + Functoriality.
**Provenance.** wave3-W34. Organizes residuals from R-01..R-07 + 11 wave-2 + 50+ wave-3 entries into eight thematic groups (G1..G8).
**Cross-walk.** Sharpens master ledger §C, §G, and W29 coherence audit by adding target-category and equivariance-class metadata to every residual; produces dependency DAG, P1/P2/P3 prioritization, and cross-volume firewall verdict.
**Findings.**
* W3-W34-T1: ~70 residuals total enumerated; zero overturns; full provenance preserved.
* W3-W34-T2: eight thematic groups: G1 (Weiss/factorization beyond $\R$), G2 (bi-infinite parent / $\Z^2$ cones), G3 (supertrace/QME on super-balanced), G4 (cross-volume / 5d M-theory), G5 (conditional theorems unconditionalization), G6 (editorial/dictionary), G7 (Obligation II reformulation, covered by W28), G8 (other / coherence cross-walks).
* W3-W34-T3: dependency DAG: G2 → G1 (chiral-algebra precursor); G2 + G1 → G7 (Obligation II reformulation); G3 → G5 (F$'$ gating); G8 feeds all (target-category exterior face); G4 ⊥ all (firewall intact); G6 ⊥ all (editorial).
* W3-W34-T4: prioritization P1 (10 entries, Phase-1/2 editorial / proof-prose); P2 (14 entries, Phase-2/3 sharpening); P3 (21 entries, Phase-4 research).
* W3-W34-T5: cross-volume flags: 11 Vol III + 6 5d M-theory + 0 Igusa; firewall INTACT.
* W3-W34-T6: hand-off includes 5 already-established discharges (R-W3-W14-A, R-W3-W6-B partial, R-W4-A largely realized, R-05 closed, R-02 closed in negative).
**Heal proposals.** WP3-W34-T1 (inscribe G1..G8 thematic statement at master ledger §G); WP3-W34-T2 (inscribe dependency DAG figure at master ledger §G); WP3-W34-T3 (translate P3 entries into Phase-4 research roadmap).
**Residuals.** No new residual; W3-W34 is META-organizational and produces no new mathematical content. Zero claims overturned; zero stable-core perturbation.
**Pointer.** `reconstitution/wave3-W34-residual-catalog-2026-04-28.md`.

---

## §T8. 200-word summary

W34 cross-walks ~70 residuals (R-01..R-07 + 11 wave-2 + 50+ wave-3
across W1–W32) under the Kapranov + Functoriality lens.  Eight
thematic groups emerge:  G1 Weiss/factorization beyond $\R$; G2
bi-infinite parent/$\Z^2$ cones; G3 supertrace/QME on
super-balanced; G4 cross-volume/5d M-theory; G5 conditional
theorems unconditionalization; G6 editorial/dictionary; G7
Obligation II reformulation (covered by W28); G8 other/coherence
cross-walks.  Dependency DAG:  G2 → G1 (chiral-algebra precursor);
G2 + G1 → G7; G3 → G5 (F$'$ gating); G8 feeds all (target-category
exterior face); G4 ⊥ all (firewall INTACT); G6 ⊥ all.
Prioritization:  P1 ten entries (Phase-1/2 editorial), P2 fourteen
entries (Phase-2/3 sharpening), P3 twenty-one entries (Phase-4
research).  Highest-impact P3 entries:  Obligation I (G7),
super-balanced QME extension (G3), transverse ML codim-4 (G1),
$L_\infty$-Mod escape (G2), 5d M-theory bridge (G4 frontier).
Cross-volume firewall verified intact at all 11 + 6 + 0 sites.
Output:  proposal-only catalog; zero overturns; zero stable-core
perturbation; ready for FINAL consolidator inscription as M-XX
master entry.

---

End of W34 residual catalog.
