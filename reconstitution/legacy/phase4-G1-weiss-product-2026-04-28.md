# Phase-4 G1 Research Outline — R²×C² Weiss Product Stability

**Date.** 2026-04-28.
**Author.** Raeez Lorgat.
**Phase.** 4 (post-Wave-3 W37 certified convergence).
**Group.** G1 — Weiss / factorization beyond $\R$.
**Specific obligation.** R²×C² Weiss-product-stability (M-37
ingredient I-4); identifier `R-W3-W9-A` and its M-37 sharpening,
flagged beyond-reach by W9 §2.3.
**Mode.** **Proposal-only.** Research outline, not new
mathematics; not a theorem proof. No master-ledger overwrites.
**Schema.** Master ledger schema; new IDs prefix `P4-G1-`.
**Inputs (light).**

* `CLAUDE.md` (cross-volume rule, harness mode, voice).
* `reconstitution/wave3-W34-residual-catalog-2026-04-28.md`
  (G1 cluster summary; P3 prioritization).
* `reconstitution/wave3-W2-gaiotto-2026-04-28.md`
  (R²×C² genuine residual diagnosis; brane-line discharge;
  M-31 bulk-only scoping).
* `reconstitution/wave3-W9-drinfeld-definitions-2026-04-28.md`
  (Lurie / CG / BD primary-source closure status; (W-2D) precise
  formulation; Drinfeld stack interpretation of bi-infinite
  parent).
* `reconstitution/wave3-W11-beilinson-hypotheses-2026-04-28.md`
  (Lurie HA §5.5.4 hypothesis verification table;
  Beilinson-Drinfeld chiral algebra structure on factorization
  centre, W3-W11-05).
* `reconstitution/wave3-W24-thmE-steps-2026-04-28.md`
  (Theorem E proves on $\R$, not on $\R^2 \times \C^2$; W6 DAG
  vs manuscript-step cross-walk).

---

## §0. Charter

Phase-4 G1 research charter has six tasks T1–T6:

* **T1.** Restate the R²×C² Weiss-product-stability obligation in
  precise technical form. Define Weiss cover, total Čech complex,
  locally constant factorization, product factorization. State
  what (I-4) requires.
* **T2.** Inventory known results landscape with primary-source
  citations and gap-naming for our $\R^2 \times \C^2$ case.
* **T3.** Enumerate three to five viable attack avenues with
  prerequisites, expected difficulty, deciding evidence.
* **T4.** Connect to other Wave-3 findings (W3-W11-05 BD chiral
  unification; W3-W31 5d M-theory limit; W3-W26 column-Verma
  boundary-line module).
* **T5.** Outline a research program with milestones (3 mo / 6
  mo / 12 mo / 18 mo+), deliverables, collaboration, risk.
* **T6.** Primary-source study list with section / theorem
  cites.

The Phase-4 cycle is research-only; no master-ledger inscription
of new theorems and no manuscript edits flow from this document.
All deliverables are externally publishable research-program
plans.

---

## §T1. Precise problem statement

### T1.A. The obligation in technical form

**Setup.** Let $M = \R^2 \times \C^2$ (the bulk spacetime of
the local Hamiltonian BF theory of `main.tex`:1776–1797). Denote
the formal symplectic disk at the origin of $\C^2$ by
$\widehat{\C^2}_0 = \mathrm{Spf}\,\C[[z_1, z_2]]$, equipped with
the symplectic form $\omega = dz_1 \wedge dz_2$. Let
$\bar A = \C[z_1, z_2] / \C \cdot 1$ be the perfect Hamiltonian
Lie algebra under the Poisson bracket.

The bulk action is
$S = \int_{\R^2 \times \C^2} \langle \beta, (D - \hbar Q)\alpha
\rangle$ with $D = d_{\R^2} + \bar\partial_{\C^2}$ and $Q$ the
Hamiltonian BF interaction encoding the brane defect along
$\R \times \{0\} \subset \R^2 \times \{0\} \subset \R^2 \times
\C^2$. The unreduced classical observables prefactorization
algebra is
$\mathrm{Obs}^{\mathrm{cl}}_{\mathrm{closed},H}$ (notation per
W3-W9 §1.2).

**Definition T1.1 (Weiss cover, CG Vol. I §6.5 Def. 6.5.0.1).**
A *Weiss cover* of an open $V \subseteq M$ in a smooth manifold
$M$ is a collection $\mathcal U = \{U_\alpha \subseteq V\}$ such
that for every finite set $\{x_1, \dots, x_n\} \subset V$ there
is some $\alpha = \alpha(x_1, \dots, x_n)$ with
$\{x_1, \dots, x_n\} \subset U_\alpha$. Equivalently,
$\mathcal U$ generates the *Weiss topology* on $V$.

**Definition T1.2 (total Čech complex).** Given a
prefactorization algebra $\mathcal F$ on $M$, an open
$V \subseteq M$, and a Weiss cover $\mathcal U$ of $V$, the
*total Čech complex* is the totalisation
$\mathrm{Tot}\,\check{\mathrm C}^\bullet(\mathcal U; \mathcal F)$
of the simplicial double complex with $p$-simplices
$\bigotimes_{0 \le i \le p} \mathcal F(U_{\alpha_i})$ over
$p$-fold disjoint inclusions
$U_{\alpha_0} \sqcup \cdots \sqcup U_{\alpha_p} \subseteq V$ and
alternating extension-by-zero differential. Implicit interior
input: a presentable symmetric monoidal $\infty$-category
$\mathcal C$ targeting the prefactorization algebra (for us, the
admissible Tate envelope of `stmt:tate-model-envelope`).

**Definition T1.3 (locally constant factorization algebra,
Lurie HA §5.5.4 / CG Vol. I §6.4).** A prefactorization algebra
$\mathcal F$ on $\R^n$ is *locally constant* if for every
inclusion of disks $U \subset V$ in $\R^n$, the structure map
$\mathcal F(U) \to \mathcal F(V)$ is a quasi-isomorphism in
$\mathcal C$. By Lurie HA Theorem 5.5.4.10, locally constant
prefactorization algebras on $\R^n$ valued in
presentable-symmetric-monoidal $\mathcal C$ are equivalent to
$E_n$-algebras in $\mathcal C$. The locally constant condition
is *strictly weaker* than the Weiss-cosheaf condition; the
latter is descent for arbitrary Weiss covers, the former is
structure-map quasi-isomorphism on disk inclusions only.

**Definition T1.4 (product factorization algebra).** Given
factorization algebras $\mathcal F$ on $M$ and $\mathcal G$ on
$N$, both valued in $\mathcal C$, the *external product*
$\mathcal F \boxtimes \mathcal G$ on $M \times N$ is the
prefactorization algebra
$$(\mathcal F \boxtimes \mathcal G)(U_1 \sqcup \cdots \sqcup U_k)
  := \bigotimes_{i=1}^k \mathcal F(\pi_M(U_i)) \otimes
  \mathcal G(\pi_N(U_i))$$
on *product opens* $U_i = U_i^M \times U_i^N$. The Weiss
condition on the product is **separately** a condition; it does
not follow automatically from the Weiss condition on
$\mathcal F$ and on $\mathcal G$.

**The obligation (W-2D), boxed (W3-W9-01).** *For every open
$V \subseteq \R^2 \times \C^2$ and every Weiss cover
$\mathcal U = \{U_\alpha\}$ of $V$, the natural map*
$$\mathrm{Tot}\,\check{\mathrm C}^\bullet
  (\mathcal U;
   \mathrm{Obs}^{\mathrm{cl}}_{\mathrm{closed},H})
  \xrightarrow{\sim}
  \mathrm{Obs}^{\mathrm{cl}}_{\mathrm{closed},H}(V).
\tag{W-2D}$$

**(W-2D) decomposes (M-37, W6-07) into four ingredients:**

* (I-1) *Heat-kernel propagator* $P_{\epsilon, L}^{\R^2 \times
  \C^2}$ separated into $\R$-topological + $\bar\partial$-Hodge
  transverse with brane line excised (Costello, *RG and EFT*,
  2011, Ch. 9–10; CG Vol. II §11.4 holomorphic Chern-Simons +
  defect).
* (I-2) *Defect boundary condition* for the brane line
  $\R \times \{0\} \hookrightarrow \R^2 \times \C^2$ from the
  brane Lagrangian (`main.tex`:1830–1836).
* (I-3) *Bulk-to-defect kernel* $K_{\mathrm{bd}}$ compatible
  with the Theorem D residue calculus and M-23 distribution-
  product avoidance.
* **(I-4)** *Mittag-Leffler resolution transverse to the brane
  on defect-localised distributions, plus product-stability of
  the Weiss cosheaf condition across non-product Weiss covers
  of $\R^2 \times \C^2$.* This is the genuinely beyond-reach
  ingredient.

### T1.B. What (I-4) precisely requires

(I-4) has two coupled subproblems:

**(I-4.a) Transverse Mittag-Leffler on defect-localised
distributions.** The principal-part fields
$\rho_{a,b}$ (`appendix-matlis-principal-parts.tex`:74–104) are
residue currents on the codim-4 holomorphic subspace $\R \times
\{0\} \subset \R \times \C^2$. Their Mittag-Leffler resolution
requires either (i) a $\bar\partial$-Hodge construction
transverse to the brane (which is non-trivially obstructed by
support on the codim-4 subspace), or (ii) a chiral-algebra
factorization via Beilinson-Drinfeld §3.4.

**(I-4.b) Weiss-product-stability across non-product covers.**
Even if Weiss descent holds separately on $\R^2$ and on $\C^2$,
the external tensor product $\mathcal F^{\R^2} \boxtimes
\mathcal F^{\C^2}$ is not automatically Weiss-cosheaf on
$\R^2 \times \C^2$ for *non-product* Weiss covers. A Weiss cover
of $\R^2 \times \C^2$ may include thin tubular neighborhoods of
non-axis-aligned curves, against which the external-product
construction is not stable in the strong descent sense (W3-W9 §1.1
"Stability under operations").

The obligation `R-W3-W9-A` (W3-W34 catalog T1.C row "Weiss-product-
stability across non-product covers (open)") is exactly
(I-4.b); the M-37 four-ingredient sharpening of R-03 / R-W6-Weiss-
defect packages (I-4.a) and (I-4.b) together as the genuinely
beyond-reach component.

**P4-G1-T1 (precise problem).** Establish (or rule out
constructively) the statement

> *Let $\mathcal C$ be a presentable symmetric monoidal
> $\infty$-category, let $\mathcal F$ be a Weiss-cosheaf on
> $M$ and $\mathcal G$ a Weiss-cosheaf on $N$, both valued in
> $\mathcal C$. Is the external tensor product
> $\mathcal F \boxtimes \mathcal G$ a Weiss-cosheaf on
> $M \times N$ for all (not necessarily product) Weiss covers
> of $M \times N$?*

Specialised to the manuscript: $M = \R^2$, $N = \C^2$ in the
mixed topological-holomorphic setting, with the unreduced
Hamiltonian BF observables prefactorization algebra. Even the
abstract general question above is open in the literature; the
manuscript's specific specialisation is the genuinely beyond-
reach piece.

---

## §T2. Known-results landscape

### T2.A. Lurie HA §5.5.4 (Higher Algebra, May 2017)

**Theorem 5.5.4.10 (`select-fact-locallyconstant`).**
For a presentable symmetric monoidal $\infty$-category
$\mathcal C^\otimes$, the natural functor
$\Alg_{E_n}(\mathcal C) \to \mathrm{Fact}^{\mathrm{lc}}(\R^n;
\mathcal C)$ exhibits the right side as a localization of the
left side; on the locally constant subcategory it is an
equivalence.

**What it covers.** Locally constant factorization algebras
on $\R^n$ in a presentable-symmetric-monoidal target. Strictly
*topological* setting; no holomorphic or mixed factor.

**Gap for our case.**
* Our setup has a *holomorphic* factor $\C^2$ in addition to
  the topological $\R^2$. Lurie's theorem does not directly
  apply because $\bar\partial$-cosheaves on $\C^n$ are not
  locally constant in the topological sense.
* Even on $\R^n$, Lurie 5.5.4.10 does *not* prove Weiss-cosheaf
  descent on arbitrary Weiss covers of $\R^n$; the locally
  constant condition is a structure-map condition, strictly
  weaker than Weiss descent. The Weiss condition is built into
  Lurie's *definition* of factorization algebra (via factorizable
  presheaves), but the equivalence with $E_n$-algebras lives on
  the locally constant subcategory.

**Theorem 5.5.4.16 (Dunn additivity).**
$E_m \otimes E_n \simeq E_{m+n}$ holds in $\mathcal P r^L$
(presentable $\infty$-categories). This gives product
stability *on locally constant $E_n$-algebras*, which are
equivalent to Weiss FAs on $\R^n$ by 5.5.4.10 — *but only for
the disk-translation-invariant subcategory*, and only via
product Weiss covers.

**Gap for our case.**
* Dunn additivity gives
  $\mathrm{Fact}^{\mathrm{lc}}(\R^m) \otimes
  \mathrm{Fact}^{\mathrm{lc}}(\R^n) \simeq
  \mathrm{Fact}^{\mathrm{lc}}(\R^{m+n})$, but only on the
  *locally constant* subcategory and only on *product covers*.
* Our factorization algebra is locally constant in the $\R^2$
  factor (topological) but *not* locally constant in the $\C^2$
  factor (holomorphic). Lurie 5.5.4.16 does not extend to the
  mixed setting.

**Hypothesis package (W3-W11-01).** Even within Lurie's setting,
Theorem 5.5.4.10's hypothesis H2 (tensor product preserves all
small colimits separately) is verified for the manuscript's
admissible Tate envelope only on *Mittag-Leffler colimits*. The
strict-arbitrary-colimit version of H2 is not proved.

### T2.B. Costello-Gwilliam *Factorization Algebras in QFT*

**Vol. I §6.4 (Locally constant prefactorization algebras).**
Definition 6.4.0.1 (locally constant); Proposition 6.4.0.4
(locally constant prefactorization algebra on $\R$ ≃ associative
algebra in $\Cat{Ch}$); Example 6.4.0.5 (constant-disk-image
factorization algebra of an associative algebra). Strictly
topological-on-$\R$.

**Gap for our case.**
* CG §6.4 covers the brane-line $\R$ piece (already discharged
  by W3-W2-02–03 via Roos ML on the symmetric-algebra functor).
* CG §6.4 says nothing about holomorphic factorization or about
  products across mixed holomorphic-topological factors.

**Vol. I §6.5 (Weiss covers).** Definition 6.5.0.1 (Weiss
cover); Definition 6.5.0.5 (Weiss-cosheaf condition);
construction of factorization algebras from cosheaves. Provides
the *language* for the residual but no theorem closing the
$\R^2 \times \C^2$ Weiss obligation.

**Vol. I §A.5 (cosheaves on manifolds).** §A.5.4 provides
single-manifold cosheaf descent under proper-support and ML
hypotheses; §A.5.6 gives product stability for *product Weiss
covers*. No theorem covering arbitrary Weiss covers of a
product manifold.

**Vol. II Ch. 10–11 (holomorphic factorization).** §10
constructs holomorphic factorization algebras on $\C^n$ via
$\bar\partial$-Hodge propagator. §11 (`Holomorphic Chern-Simons
and twisted supergravity`) constructs holomorphic factorization
algebras with defects: §11.4 specifically addresses
holomorphic-Chern-Simons + defect on $\C^n \times \R$.

**Gap for our case.**
* CG Vol. II §11.4 is the *closest* literature analogue to our
  setting: holomorphic Chern-Simons on $\C^n$ with a defect on a
  $\R$-line.
* However, the manuscript's Hamiltonian BF theory has additional
  topological factor $\R^2$ (not just $\R$ defect line in
  $\C^n$); the bulk action mixes $\R^2$-topological with
  $\C^2$-holomorphic via the Hamiltonian connection
  (`main.tex`:1830–1836); and the Weiss descent on the bulk
  cosheaf at non-product covers is not addressed.

### T2.C. Beilinson-Drinfeld *Chiral Algebras* (AMS 2004)

**§3.4 (Chiral algebras and factorization algebras).** §3.4.1
defines chiral algebras on a smooth complex curve $X$ as
$\mathcal D_X$-modules with chiral OPE bracket
$\mu: j_*j^*(\mathcal A \boxtimes \mathcal A) \to \Delta_!
\mathcal A$. §3.4.5 establishes the equivalence with
factorization algebras on the Ran space $\mathrm{Ran}(X)$.

**§3.4.10–11 (chiral product on $X \times Y$).** Constructs the
chiral-product factorization algebra on $X \times Y$ from chiral
algebras on $X$ and $Y$, *with additional hypotheses*: the
chiral cobracket on $\Delta^*(\mathcal F \boxtimes \mathcal G)$
must satisfy the chiral axiom on $X \times Y$.

**Gap for our case.**
* BD's chiral product is *almost* a Weiss-product-stability
  theorem, but in the algebraic-geometric (not analytic) setting
  on smooth complex curves and their products. Adapting to the
  $C^\infty$ / mixed setting is non-trivial.
* The chiral axiom on $X \times Y$ in §3.4.11 is verified under
  separate hypotheses (cohomological boundedness, $\mathcal D$-
  module finiteness) that do not hold for the principal-part
  cosheaf on the brane line.
* BD §3.4 is in the *complex-analytic* setting on a single
  curve, not on a 4-real-dimensional complex surface
  $\C^2 \cong \R^4$. The 1-curve specialisation does not
  immediately upgrade to a complex surface.

### T2.D. Ayala-Francis on factorization homology

**Ayala-Francis,** *Factorization homology of topological
manifolds* (arXiv:1206.5522, J. Topology 2015). Theorem 4.5
(via Lurie HA 5.5.2) establishes factorization homology
$\int_M \mathcal F$ for $E_n$-algebras $\mathcal F$ on smooth
$n$-manifolds $M$ (not necessarily $\R^n$). The Weiss-cosheaf
descent is intrinsic; product stability holds for product
manifolds via Dunn additivity.

**Gap for our case.**
* Ayala-Francis covers *topological* manifolds; the holomorphic
  $\C^2$ factor is again outside the scope.
* The Weiss descent in their setting is in the locally-constant
  subcategory, not on arbitrary Weiss covers.

### T2.E. Lurie HA §5.5.2 (Pushforward of factorizable structures)

**§5.5.2.6 (`select-pushforward-fact`).** For a smooth
submersion $f: M \to N$ of topological manifolds and a
factorizable structure on $M$, the pushforward $f_*$ to $N$
preserves factorizability under suitable hypotheses (proper-
support / locally-constant). The product setting fits as
$f: M \times N \to \mathrm{pt}$ with both factors carrying
factorization structures.

**Gap for our case.**
* The submersion / pushforward apparatus does not address
  *non-product* Weiss covers of the product manifold. It
  computes factorization homology on the product via product
  covers only.

### T2.F. Costello *Renormalization and EFT* (AMS 2011)

**Ch. 9–10 (Heat-kernel propagator, BV regularization).**
Constructs heat-kernel propagator $P_{\epsilon, L}$ on $\R^n$
and proves graphwise BV-quantization compatibility. On $\R^2
\times \C^2$ the heat-kernel apparatus would *separate*: $\R^2$
direction is topological heat-kernel; $\C^2$ direction is
$\bar\partial$-Hodge.

**Gap for our case.**
* Costello provides the analytic glue (M-37 ingredient I-1) for
  the *graphwise* perturbative computation, not Weiss descent
  on the cosheaf-of-observables across non-product covers.

### T2.G. Costello-Gaiotto-Williams *Twisted Supergravity* (arXiv:2007.09497)

**§3–§5 (5d twisted M-theory; defects).** Provides analytic
machinery for codim-2, codim-4, codim-5 defects in the holomorphic-
topologically-twisted 5d theory on $\R \times \C^2$. The
brane-line defect at codim-5 in $\R^2 \times \C^2$ (or codim-4
in $\R \times \C^2$) is exactly this setup with one extra
topological factor.

**Gap for our case.**
* CGW §3–§5 provides the *physics-motivated* Weiss-defect
  machinery; their concrete defect-cohomology computations do
  not provide a closed Weiss-product-stability theorem in
  Beilinson-Drinfeld-clean form.
* Cross-volume firewall (M-34, M-52) requires matched-conventions
  theorem before any CGW result can be imported as a manuscript
  claim.

### T2.H. Adjudication

**No primary-source theorem closes the residual.** Across the
seven sources reviewed (Lurie HA §5.5.4, §5.5.2; CG Vol. I §6.4,
§6.5, §A.5; CG Vol. II §10–11; BD §3.4; Ayala-Francis;
Costello *RG and EFT*; CGW *Twisted Supergravity*), the
Weiss-product-stability question for the mixed topological-
holomorphic $\R^2 \times \C^2$ setting on *non-product Weiss
covers* is genuinely open. The closest analogues (CG Vol. II
§11.4, BD §3.4.10–11) cover restricted settings and require
fresh adaptation.

---

## §T3. Attack avenues

Five viable attack avenues, each with prerequisites, expected
difficulty, and deciding evidence.

### T3.A. Avenue (A) — Direct Čech-cohomology computation on adapted covers

**Idea.** Construct a concrete Weiss cover of $\R^2 \times \C^2$
adapted to the brane-line stratification (e.g., $\epsilon$-tubular
neighbourhoods of the brane line, plus complement covers in
$\R^2 \times \C^2 \setminus (\R \times \{0\})$) and compute the
total Čech complex
$\mathrm{Tot}\,\check{\mathrm C}^\bullet(\mathcal U;
\mathrm{Obs}^{\mathrm{cl}}_{\mathrm{closed},H})$ explicitly.
Show the natural map to
$\mathrm{Obs}^{\mathrm{cl}}_{\mathrm{closed},H}(V)$ is a
quasi-isomorphism on this adapted cover, then argue that any
Weiss cover refines an adapted cover (so descent on the adapted
cover suffices for Weiss descent in general).

**Prerequisites.**
* Concrete description of $\mathrm{Obs}^{\mathrm{cl}}_{\mathrm{closed},H}$
  on small open balls of $\R^2 \times \C^2$ (free graded-commutative
  on the symplectic potential / current cosheaf).
* Refinement lemma: every Weiss cover of $V \subseteq \R^2
  \times \C^2$ admits a Weiss-cofinal refinement that is
  "stratification-adapted" (separates brane-line points from
  bulk points).
* ML conditions on the principal-part cosheaf transverse to
  the brane line (residue currents on codim-4 subspace).

**Expected difficulty.** **High.** The principal-part residue
currents on the codim-4 subspace are exactly the obstruction in
(I-4.a); their Mittag-Leffler resolution transverse to the
brane requires either a $\bar\partial$-Hodge construction (which
is non-trivially obstructed by the codim-4 support) or a chiral-
algebra factorization argument. The refinement lemma itself
requires a non-trivial topological-stratification argument.

**Deciding evidence.** A concrete computation showing total Čech
on the adapted cover gives the right cohomology; verification
that the structure maps from a generic Weiss cover refine into
the adapted cover; explicit example computation on a model
$V = $ small ball intersected with brane line.

**Risk.** Concrete computations risk hiding silent hypotheses
(e.g., regulator-class dependence per W3-W6-04). Need explicit
admissibility statement.

### T3.B. Avenue (B) — Lurie HA §5.5.4.16 Dunn-additivity adaptation

**Idea.** Generalise Dunn additivity from
$E_m \otimes E_n \simeq E_{m+n}$ in the *locally constant*
setting (Lurie 5.5.4.16) to a *mixed locally constant* /
*holomorphic* setting where one factor is $E_2$ (topological,
$\R^2$) and the other is *holomorphic-locally-constant* on
$\C^2$. The holomorphic-locally-constant factorization algebra
on $\C^n$ is equivalent to a CG-Vol-II §10.2 *holomorphic*
$E_n$-algebra (= $\mathbb E^{\mathrm{hol}}_n$-algebra) — see
Williams, `Holomorphic factorization algebras`,
arXiv:2007.13985, for a precise definition.

The conjecture: there is a mixed-Dunn-additivity-style equivalence
$\mathbb E_m^{\mathrm{top}} \otimes \mathbb E_n^{\mathrm{hol}}
\simeq \mathbb E^{\mathrm{mixed}}_{m, n}$
in $\mathcal P r^L$, and this implies Weiss-product-stability
on the product manifold $\R^m \times \C^n$.

**Prerequisites.**
* Williams' holomorphic-$E_n$-algebra apparatus
  (arXiv:2007.13985 §3–§4).
* Dunn additivity for mixed setting (formal-$E_n$-algebra
  language extended to mixed locally constant /
  holomorphic-locally-constant); not yet in literature.
* Lurie's $\mathcal P r^L$-tensor-product machinery
  (HA §4.8–4.9).

**Expected difficulty.** **Medium-high.** The framework is
within reach: Williams + Knudsen + Ayala-Francis have established
the holomorphic side; Dunn additivity is well-established on
the topological side. The mixed Dunn additivity is a
conjectural extension that requires careful $\bar\partial$-Hodge
adaptation.

**Deciding evidence.** Statement and proof of the mixed Dunn
additivity:
$$\mathbb E_m^{\mathrm{top}} \otimes \mathbb E_n^{\mathrm{hol}}
  \simeq \mathbb E^{\mathrm{mixed}}_{m, n}
  \text{ in } \mathcal P r^L,$$
plus verification that Weiss-cosheaf descent on the mixed
factorization algebra on $\R^m \times \C^n$ is equivalent to
the locally-constant condition on each factor (the mixed
analogue of Lurie 5.5.4.10).

**Risk.** The mixed setting may not be a clean Dunn-additivity
extension; the holomorphic factor may force a different
operadic structure. Needs careful $E$-theory / operadic
verification.

### T3.C. Avenue (C) — Hochschild homology / factorization homology technique

**Idea.** Compute factorization homology
$\int_{\R^2 \times \C^2}
\mathrm{Obs}^{\mathrm{cl}}_{\mathrm{closed},H}$ via
factorization-homology / topological chiral homology technique
of Ayala-Francis / Lurie HA §5.5.3. The factorization homology
is invariant under refinement of Weiss covers (it is the
homotopy-colimit over the Ran space of the prefactorization
algebra), so its existence and well-definedness is *equivalent*
to Weiss-cosheaf descent on the chosen target $\infty$-category.

**Prerequisites.**
* Ayala-Francis factorization-homology framework
  (arXiv:1206.5522 §3, J. Topology 2015).
* Lurie HA §5.5.3 (factorization homology = topological chiral
  homology).
* Knudsen's *Higher enveloping algebras* (Geom. Topol. 2018) for
  the connection between Lie algebra cohomology and factorization
  homology.

**Expected difficulty.** **Medium.** The factorization-homology
technique is well-developed for topological manifolds; adapting
to the mixed topological-holomorphic setting requires
holomorphic-factorization-homology machinery (Williams,
arXiv:2007.13985).

**Deciding evidence.** Computation of
$\int_{\R^2 \times \C^2}$ as a homotopy colimit over
$\mathrm{Ran}(\R^2 \times \C^2)$, with Weiss-cosheaf descent
on a class of "test Weiss covers" (cofinally refining all Weiss
covers); identification of the result with the manuscript's
$\mathrm{Obs}^{\mathrm{cl}}_{\mathrm{closed},H}(\R^2 \times
\C^2)$.

**Risk.** Factorization homology is well-defined for $E_n$-
algebras on $n$-manifolds; the holomorphic factor changes the
target operadic structure. The relationship between
factorization homology and Weiss descent is tight in the locally
constant setting, less clear in the mixed setting.

### T3.D. Avenue (D) — Beilinson-Drinfeld chiral-product descent + matched conventions

**Idea.** Use BD §3.4.10–11's chiral-product construction. The
factorization centre on the formal symplectic disk is implicitly
a Beilinson-Drinfeld chiral algebra (W3-W11-05) with $\lambda$-
bracket = $P_0$-bracket and central charge = U(1)/Capelli class.
The Weiss-product-stability question reduces to: does the chiral-
product on $X \times Y$ (BD §3.4.10) descend Weiss-cosheaf-
admissibly across non-product covers?

The natural setting: on a complex curve $X$ (e.g., the brane
line viewed as $\C \cap \R$ via real structure, or directly on
$X = \C \subset \C^2$), the chiral algebra structure exists; the
product theorem in BD §3.4.10–11 gives the Weiss-cosheaf
descent in the *chiral* (D-module) sense; the issue is whether
this lifts to the $\R^2$ topological factor.

**Prerequisites.**
* BD *Chiral Algebras* §3.3–3.4 (chiral algebra; chiral-product
  on $X \times Y$).
* W3-W11-05 explicit BD chiral algebra interpretation of the
  formal-symplectic-disk factorization centre.
* Real structure on $X = \C \subset \C^2$: how does the chiral
  algebra on $\C$ restrict to $\R \subset \C$? Connection to
  W3-W26 column-Verma boundary line module.

**Expected difficulty.** **High.** BD's framework is in the
algebraic-geometric setting on smooth complex curves; adapting
to a $C^\infty$ / mixed setting on a complex surface is a
substantial undertaking. However, this is the *natural* home
for the residual according to W9-§5 + W11-T5: "the genuinely
hard ingredient (Mittag-Leffler resolution transverse to the
brane on defect-localised distributions) is exactly the *Ran-
space descent* of the BD chiral algebra, which is non-standard
for Costello-RG and standard for BD."

**Deciding evidence.**
* Explicit BD chiral-algebra description of the factorization
  centre on the formal symplectic disk (W3-W11-05's interpretive
  claim, formalised).
* Application of BD §3.4.11's chiral-product axiom to verify the
  axiom on the product $\R^2 \times \C^2$ (translated into an
  appropriate $C^\infty$ adaptation).
* Compatibility with the M-31 BV/CE bulk identification and the
  M-37 brane-line defect data.

**Risk.** Cross-volume / language drift: BD is in the algebraic-
geometric world; manuscript is in the $C^\infty$ / Costello-
Gwilliam world. The translation introduces silent hypotheses;
need careful matched-conventions theorem (W28 template).

### T3.E. Avenue (E) — Reduction to $E_2$ algebra structure on the brane line

**Idea.** Use Lurie HA §5.5.4.10 / Dunn additivity for $n = 2$:
the brane-line factorization algebra on $\R$ is an $E_1$-algebra
in the admissible Tate envelope (W3-W2 §1 discharge); the
ambient bulk factorization algebra on $\R^2 \times \C^2$ should
restrict to an $E_2$-algebra on the brane stratum
$\R \times \{0\}$ when the $\R$ topological direction in $\R^2$
combines with the brane line direction. Weiss-product-stability
on $\R^2 \times \C^2$ reduces (via the brane stratification
+ holomorphic transverse direction) to Dunn additivity for $E_2$.

The reduction: $\R^2 \times \C^2 = \R \times \R \times \C^2$;
the brane line is one $\R$ factor; the other $\R$ factor combines
with the holomorphic $\C^2$ via the Hamiltonian connection
(which provides an $E_2$-promotion of the $E_1$ brane-line
algebra to a $\R \times \R$-direction algebra).

**Prerequisites.**
* W3-W2 brane-line $\R$ Weiss discharge.
* Lurie HA §5.5.4.16 Dunn additivity in the locally constant
  setting on $\R^2$.
* Promotion of the $E_1$ brane-line algebra to $E_2$ via the
  Hamiltonian connection's transverse $\R$ direction
  (`main.tex`:1830–1836); explicit construction needed.
* Suspended question: the $\C^2$ holomorphic factor's
  contribution to the Weiss descent; possibly via W3-W11-05's
  chiral-algebra interpretation.

**Expected difficulty.** **Medium.** The $E_1 \to E_2$ promotion
via the topological Hamiltonian connection is the cleanest part
of the avenue; the holomorphic $\C^2$ factor and the brane
codim-5 stratification add complexity. This avenue may be the
most tractable starting point because it stays inside
established Lurie / CG language.

**Deciding evidence.**
* Explicit construction of the $E_2$-algebra on $\R^2$ extending
  the $E_1$ brane-line algebra.
* Verification of Dunn additivity application:
  $\R^2 \times \C^2$-Weiss-cosheaf-descent equivalent to
  ($E_2$ on $\R^2$) $\otimes$ (holomorphic factorization algebra
  on $\C^2$) under matched-conventions hypothesis.
* Cross-walk to W3-W11-05 BD chiral interpretation: the $E_2$
  algebra is conjecturally a topological / vertex-style chiral
  algebra in the brane-line direction, with central charge
  consistent with M-31's anomaly line.

**Risk.** The Hamiltonian-connection $E_2$-promotion may have
hidden cohomological obstructions (e.g., unmatched
$\bar\partial$-cohomology in the $\C^2$ direction). Need careful
analytic verification at the propagator (I-1) and bulk-to-defect
kernel (I-3) levels.

### T3.F. Cross-avenue summary

| Avenue | Difficulty | Time horizon | Deciding evidence |
|--------|-----------|--------------|-------------------|
| (A) Direct Čech | High | 18 mo+ | Concrete computation + refinement lemma |
| (B) Mixed Dunn additivity | Medium-high | 12–18 mo | Mixed-$E_{m,n}$ equivalence theorem |
| (C) Factorization homology | Medium | 6–12 mo | $\int_{\R^2 \times \C^2}$ computation + cofinality |
| (D) BD chiral product | High | 18 mo+ | BD §3.4.11 axiom + matched conventions |
| (E) $E_2$ reduction on brane | Medium | 6–12 mo | $E_2$-promotion + Dunn application |

**P4-G1-T3 (recommendation).** Pursue (E) and (B) in parallel
in the early phase (6–12 mo); they share the
$E_2$/Dunn-additivity machinery and may converge. Use (C) as a
sanity-check via factorization homology computation. Pursue
(D) in the middle-late phase (12–18 mo+) once the chiral-algebra
language has been formalised in the manuscript. Pursue (A) as a
last-resort direct attack if all structural avenues fail.

---

## §T4. Connections to other Wave-3 findings

### T4.A. W3-W11-05 — BD chiral algebra unification

**The W3-W11-05 finding (severity 2 sharpening).** The
factorization centre on the formal symplectic disk is implicitly
a Beilinson-Drinfeld chiral algebra:

* Underlying vector space: $\mathcal A = C^\bullet_{\mathrm{CE},
  \mathrm{cont}}(\mathfrak g_I)$ for $I$ small open interval.
* $\lambda$-bracket: the $P_0$-bracket of
  `prop:app-factorization-principal-part-bracket`.
* Central charge: $[\bar c] \in H^2_{\mathrm{Lie}}(\bar A;
  \C)_{(0,0)}$ = U(1)/Capelli class.
* Universal property: the locally-constant-FA equivalence
  Lurie 5.5.4.10 in the brane-line direction.

**Implication for G1.** The chiral-product descent (Avenue D
above) inherits *directly* from W3-W11-05's BD interpretation.
If the factorization centre is genuinely a BD chiral algebra
on the brane line, then BD §3.4.10–11's chiral-product theorem
applies (with appropriate $C^\infty$ adaptation), and the
Weiss-product-stability on $\R^2 \times \C^2$ becomes a chiral-
product descent question on $\mathrm{Ran}(\R^2 \times \C^2)$.

**Cross-cite.** P4-G1-T4-1: the BD chiral interpretation
(W3-W11-05) is the structural bridge from the *locally constant
factorization algebra on $\R$* (closed by W3-W2) to the
*chiral product factorization algebra on $\R^2 \times \C^2$*
(open, our G1 obligation). The gap to close is the
$C^\infty$-vs-algebraic-geometric translation and the four-real-
dimensional adaptation of the one-curve BD framework.

### T4.B. W3-W31-T2 — 5d twisted M-theory limit

**The W3-W31 conjecture (severity 4 cross-volume, conditional).**
The Costello-Gaiotto-Williams 5d twisted M-theory on
$\R \times \C^2$ provides the analytic apparatus for codim-4
defects in mixed holomorphic-topological factorization theories.
W3-W31 names five obstruction sites (CV-5dM-1 through CV-5dM-5)
required before any cross-volume manuscript claim can be made.

**Implication for G1.** If the limit theory of 5d twisted M-theory
*is* the local Hamiltonian BF on $\R^2 \times \C^2$ (in some
appropriate degeneration), then CGW's analytic framework
(arXiv:2007.09497 §3–§5) provides:
* The heat-kernel propagator on $\R \times \C^2$ (M-37 ingredient
  I-1) — needs adaptation for the additional $\R$ topological
  factor in $\R^2 \times \C^2$.
* The defect boundary condition (I-2) — directly via the
  CGW codim-4 brane-line setup.
* The bulk-to-defect kernel (I-3) — directly via the CGW
  defect-cohomology formalism.

The CGW framework does *not* resolve (I-4) — Weiss-product-
stability — without additional input.

**Cross-cite.** P4-G1-T4-2: the 5d twisted M-theory bridge,
once unconditionalized, would supply M-37 ingredients (I-1)–(I-3)
analytically and reduce the G1 obligation to (I-4) alone.
Cross-volume firewall (M-34, M-52) requires matched-conventions
theorem before any CGW result can be imported. **P4-G1 work is
locally independent of the CGW bridge** — we should not gate
G1 progress on cross-volume unconditionalization. But should the
bridge unconditionalize, the G1 obligation simplifies.

### T4.C. W3-W26-T1 — Column-Verma functoriality

**The W3-W26 finding (severity 2-3, R-W3-W26-A).** The column-
Verma decomposition of the bi-infinite parent module on the
boundary line $\R \subset \C$ produces a Symp$_{\mathrm{form}}$-
natural realization of the four-cone canonical filtration
(M-50). The boundary-line module side of this decomposition is
the brane-line factorization algebra restricted to its boundary
line.

**Implication for G1.** The column-Verma boundary-line module
is the *locally constant factorization algebra on the brane
line* (W3-W2 §1 discharge); its extension to the bulk
$\R^2 \times \C^2$ via the M-37 four-ingredient setup is
exactly the G1 obligation.

**Cross-cite.** P4-G1-T4-3: the column-Verma decomposition
provides a *categorically clean* description of the brane-line
factorization algebra; lifting it to a bulk Weiss-cosheaf on
$\R^2 \times \C^2$ requires the four ingredients of M-37 with
W3-W26's column-Verma functoriality preserved. The functoriality
constraint:

* Symp$_{\mathrm{form}}(\widehat{\C^2}_0)$-equivariance on the
  closed (Hamiltonian BF) side.
* GL$_2 \times T^2$-equivariance on the open (Dirac probe) side.

is preserved by the M-37 four ingredients (Symp-form-canonical
heat kernel; Symp-form-canonical defect boundary condition;
Symp-form-canonical bulk-to-defect kernel; Symp-form-canonical
ML transverse to the brane).

### T4.D. W3-W14 — Mixed cones / 5d brane configuration realization

**The W3-W14 finding (severity 2-3, R-W3-W14-B).** The mixed
cones $C^{+-}$ and $C^{-+}$ in the four-cone canonical
filtration (M-50) are Wakimoto-type tensor-factorized parabolic-
induced modules; the brane-configuration realization in 5d
twisted M-theory is conjectural (R-W3-W14-B).

**Implication for G1.** The mixed cones live on the bi-infinite
parent module's $\Z^2$ lattice; their physical realization as
brane configurations in 5d twisted M-theory — should this
unconditionalize — would supply concrete Weiss covers of
$\R^2 \times \C^2$ adapted to the brane-stratum cones. This
intersects with Avenue (A) (direct Čech on adapted covers).

### T4.E. Cross-walk summary

| W3 finding | Severity | G1 impact |
|------------|----------|-----------|
| W3-W11-05 BD chiral | 2 | Avenue (D) inherits structural framework |
| W3-W31-T2 5d M-theory | 4 (cross-volume) | Avenues (A)–(E) inherit M-37 (I-1)–(I-3) analytics if unconditionalized |
| W3-W26-T1 column-Verma | 2-3 | Functoriality constraints on M-37 ingredients |
| W3-W14-B mixed cones | 2-3 | Avenue (A) gets adapted-cover candidates from brane configurations |

---

## §T5. Research program proposal

### T5.A. Milestone schedule

**Three-month milestone (M-3).** *Foundation.*
* Complete a literature audit: read in full Lurie HA §5.5.2,
  §5.5.3, §5.5.4 (especially 5.5.4.10, 5.5.4.16); CG Vol. I
  §6.4–6.5, §A.5; CG Vol. II §10–11; BD §3.4.1, 3.4.5,
  3.4.10–11; Ayala-Francis §3–§5; Williams arXiv:2007.13985.
* Draft a 30-page expository note formalising P4-G1-T1 (precise
  problem statement) with full primary-source apparatus.
* Formalise W3-W11-05's BD chiral interpretation: write a
  precise proposition stating the factorization centre on the
  formal symplectic disk *is* a BD chiral algebra in
  $C^\infty$-Costello-Gwilliam translation, with explicit
  $\lambda$-bracket, central charge, universal property.
* **Deliverable.** Expository note + W3-W11-05 formalisation
  (publishable as arXiv preprint).

**Six-month milestone (M-6).** *First attack waves.*
* Avenue (E) — $E_2$-promotion construction. Construct the
  $E_2$-algebra on $\R^2$ extending the brane-line $E_1$-
  algebra via the Hamiltonian connection. Verify cohomological
  stability of the promotion at fixed Tate window. Cross-walk
  to W3-W26's column-Verma functoriality.
* Avenue (C) — factorization-homology computation of
  $\int_{\R^2 \times \C^2}$ via Ayala-Francis machinery. Test
  cofinality of "stratification-adapted" Weiss covers in the
  Ran space.
* **Deliverable.** Two preprints (one per avenue), separately
  publishable. Either avenue's success closes part of (I-4.b);
  failure modes named explicitly.

**Twelve-month milestone (M-12).** *Avenue convergence.*
* Avenue (B) — mixed Dunn additivity. Stated and partial proof
  of $\mathbb E_m^{\mathrm{top}} \otimes \mathbb E_n^{\mathrm{hol}}
  \simeq \mathbb E^{\mathrm{mixed}}_{m, n}$ in $\mathcal P r^L$,
  using Williams' holomorphic-$E_n$-algebra apparatus.
* Avenue (A) — direct Čech computation on a model
  $V \subset \R^2 \times \C^2$ (e.g., a small ball intersected
  with brane line). Concrete numerical verification on low-
  dimensional Tate windows.
* **Deliverable.** Mixed-Dunn-additivity preprint; direct-Čech
  model computation preprint. If both avenues succeed,
  Weiss-product-stability for product Weiss covers extended to
  a class of "almost-product" non-product covers.

**Eighteen-month-plus milestone (M-18+).** *Synthesis or
obstruction crystallisation.*
* Avenue (D) — BD chiral product descent on $\mathrm{Ran}(\R^2
  \times \C^2)$. Adapt BD §3.4.10–11 to the $C^\infty$ setting
  with W3-W11-05's chiral interpretation. Verify the chiral
  axiom on the product manifold.
* Synthesis: combine outputs of avenues (A)–(E) into a
  proposed Weiss-product-stability theorem (or a clean
  obstruction statement showing where it fails).
* If the theorem closes: inscribe at master-ledger level as a
  manuscript-internal theorem, with full convention block, full
  hypothesis list, and cross-walked to M-37 ingredient I-4.
* If the theorem does not close: name the precise obstruction
  (which non-product Weiss cover, which residue-current
  cohomology class) and propose a Phase-5 follow-up.
* **Deliverable.** Either a closure paper (~70 pages) or a
  precise-obstruction paper (~30 pages) in a leading journal.

### T5.B. Primary deliverables

| Milestone | Deliverable | Estimated length | Venue |
|-----------|-------------|------------------|-------|
| M-3 | Foundation expository note + W3-W11-05 BD formalisation | 30 + 20 pp | arXiv preprint(s) |
| M-6 | Avenue (E) preprint + Avenue (C) preprint | 40 + 30 pp | arXiv |
| M-12 | Avenue (B) mixed Dunn additivity + Avenue (A) model Čech | 50 + 25 pp | J. Topology / Adv. Math. |
| M-18+ | Synthesis closure or precise obstruction | 30–70 pp | Selecta Math. / IHES Publ. |

### T5.C. Collaboration requirements

**Primary expert input.**
* **Holomorphic factorization expert.** Brian Williams
  (arXiv:2007.13985 author) for holomorphic-$E_n$-algebra
  apparatus. Or: Owen Gwilliam (CG Vol. II §11.4 author) for
  defect / holomorphic-Chern-Simons machinery.
* **Higher-categorical / Lurie expert.** Hiro Lee Tanaka or
  Andrew Blumberg for Dunn-additivity adaptations and
  mixed-$E$-theory. Or: Kerodon-team contributor for hands-on
  $\infty$-category technical questions.
* **BD chiral algebra expert.** Sam Raskin, Dennis Gaitsgory,
  or another Beilinson-Drinfeld-tradition algebraic geometer for
  BD §3.4.10–11 adaptation.
* **5d twisted M-theory bridge.** Davide Gaiotto (CGW
  arXiv:2007.09497 co-author) for cross-volume bridge — only if
  the W3-W31 cross-volume firewall lifts at some point.

**Secondary expert input.**
* Costello-RG analytics (Kevin Costello himself or one of his
  former students).
* Tate vector space / Mittag-Leffler expert (e.g., Mikhail
  Kapranov, Vladimir Drinfeld).

**Workshop / conference engagement.**
* Submit an abstract to *Higher Structures* or
  *Factorization Algebras Workshop* at IHES / Banff for
  M-6 / M-12 deliverables.
* Aim for talks at *Fields Medal Symposium* (Bondi style) or
  *PIMS Summer School* on relevant year.

### T5.D. Risk assessment

**Primary risk: P4-G1-T5-R1 (residual is genuinely beyond all
five avenues).** The (I-4) ingredient may genuinely be beyond
present technique; all five avenues may stall or partially
succeed without closing the Weiss-product-stability question.

*Mitigation.* Even partial success on each avenue produces a
publishable result: Avenue (B) mixed Dunn additivity is a
self-contained $\infty$-categorical theorem; Avenue (C)
factorization homology computation is independently valuable;
Avenue (E) $E_2$-promotion is a manuscript-internal sharpening.
*Failure to close the residual is itself a result* — naming the
precise obstruction (e.g., a specific residue-current cohomology
class that fails ML transverse to the brane) is publishable.

**Secondary risk: P4-G1-T5-R2 (cross-volume firewall lifts and
forces re-scoping).** If the W3-W31 cross-volume firewall lifts
(through W3-W31-A/B/C unconditionalization in CGW), the G1
obligation simplifies: M-37 ingredients (I-1)–(I-3) become
inheritable from CGW, and (I-4) alone remains.

*Mitigation.* Plan G1 work to be locally independent of the
cross-volume bridge; treat any CGW unconditionalization as
*bonus simplification*, not as a prerequisite. Cross-volume
firewall checks per W28 template at every milestone.

**Tertiary risk: P4-G1-T5-R3 (regulator-class boundary widens
mid-research).** If R-W3-W6-04 (cross-regulator-class canonicity)
is partially closed during the G1 research period (e.g., via a
new admissibility class), the G1 statement may need to be
restated for the wider class.

*Mitigation.* State G1 results in the *admissible-class envelope*
explicitly (per W3-W6-04 / W3-W9-H1 canonicity prose); reach to
the wider class is a Phase-5 obligation.

**Quaternary risk: P4-G1-T5-R4 (BD framework adaptation
introduces silent hypotheses).** Avenue (D) translates BD's
algebraic-geometric framework into the $C^\infty$ Costello-
Gwilliam world. The translation may introduce hypotheses
silently (e.g., D-module finiteness silently strengthened from
algebraic to analytic).

*Mitigation.* Hypothesis-by-hypothesis verification table at
the start of any BD-derived theorem (W3-W9 §1 / W3-W11 §1
template). Open-obligations transparency at every step.

---

## §T6. Primary-source study list

The following theorems / sections from primary sources are
required interpretation for the Phase-4 G1 research program. Cited by
author / year / section / theorem-number per CLAUDE.md voice.

### T6.A. Higher-algebra apparatus

* **Lurie, *Higher Algebra*** (May 2017 / latest version,
  available as kerodon.net + arXiv:1907.13146 / Wiki):
  - §4.8 (Tensor product of $\infty$-categories).
  - §4.9 (Pr$^L$ and presentable $\infty$-categories).
  - §5.5.1 (Symmetric monoidal $\infty$-categories).
  - §5.5.2 (Operadic Kan extensions; pushforward).
  - §5.5.3 (Topological chiral homology = factorization
    homology).
  - **§5.5.4.10** (locally constant factorization algebra ≃
    $E_n$-algebra).
  - **§5.5.4.16** (Dunn additivity: $E_m \otimes E_n \simeq
    E_{m+n}$).
  - §A.2.6.8 (Presentability of localization).
  - §A.3.7.6 / A.3.7.10 (Quillen-equivalent
    $\infty$-categories).

### T6.B. Costello-Gwilliam apparatus

* **Costello-Gwilliam, *Factorization Algebras in Quantum
  Field Theory*, Vol. I** (Cambridge UP 2017; available
  arXiv:1605.01062):
  - §3.1 (Prefactorization algebra; Disj operad).
  - **§6.4** (Locally constant prefactorization algebras;
    Definition 6.4.0.1 / Proposition 6.4.0.4 / Example
    6.4.0.5).
  - **§6.5** (Weiss covers; Definitions 6.5.0.1 / 6.5.0.5).
  - **§A.5.4 / A.5.6** (Cosheaves on manifolds; product
    stability for product Weiss covers).
  - §7.2 (Extension from a basis vocabulary).

* **Costello-Gwilliam, *Factorization Algebras in Quantum
  Field Theory*, Vol. II** (Cambridge UP 2021; available
  arXiv:2010.00466 / Vol. II preprints):
  - **Ch. 10** (Holomorphic factorization algebras on $\C^n$;
    $\bar\partial$-Hodge propagator).
  - **§11.4** (Holomorphic Chern-Simons + defect; closest
    literature analogue to our setting).

### T6.C. Beilinson-Drinfeld apparatus

* **Beilinson-Drinfeld, *Chiral Algebras*** (AMS Coll. Pub.
  vol. 51, 2004):
  - §3.3 (Factorization algebras on the Ran space).
  - **§3.4.1** (Chiral algebra on a smooth complex curve;
    chiral OPE bracket via $j_*j^*(\mathcal A \boxtimes
    \mathcal A) \to \Delta_!\mathcal A$).
  - **§3.4.5** (Equivalence with factorization algebras on
    $\mathrm{Ran}(X)$).
  - **§3.4.10** (Chiral product on $X \times Y$).
  - **§3.4.11** (Chiral axiom on $X \times Y$ from chiral
    algebras on $X$ and $Y$).

### T6.D. Holomorphic factorization apparatus

* **Williams, *Holomorphic factorization algebras***,
  arXiv:2007.13985:
  - §3 (Holomorphic-$E_n$-algebra; $\mathbb E^{\mathrm{hol}}_n$).
  - §4 (Holomorphic factorization homology).

* **Knudsen, *Higher enveloping algebras***, Geom. Topol.
  2018 (arXiv:1605.01391):
  - Theorem 3.1 (Higher enveloping algebra; connection between
    Lie algebra cohomology and factorization homology).

### T6.E. Factorization homology apparatus

* **Ayala-Francis, *Factorization homology of topological
  manifolds***, J. Topology 2015 (arXiv:1206.5522):
  - §3 (Factorization homology defined via $\mathrm{Disk}_n^{\mathrm{fr}}$).
  - **Theorem 4.5** (Factorization homology = topological
    chiral homology = Lurie HA §5.5.3).
  - §5 (Excision / Weiss descent).

* **Ayala-Francis-Tanaka, *Factorization homology of stratified
  spaces***, Selecta Math. 2017:
  - §2 (Stratified setup; codim-$k$ defects).
  - §4 (Stratified factorization homology + descent).

### T6.F. Costello-RG apparatus

* **Costello, *Renormalization and Effective Field Theory***
  (AMS Math. Surveys 170, 2011):
  - **Ch. 9** (Heat-kernel propagator; analytical apparatus).
  - **Ch. 10** (BV regularization; graphwise effective
    interaction).

### T6.G. 5d twisted M-theory apparatus (cross-volume)

* **Costello-Gaiotto-Williams, *Twisted Supergravity and
  Koszul Duality: A Case Study in $AdS_3 \times S^3$***,
  arXiv:2007.09497:
  - §3 (5d twisted M-theory on $\R \times \C^2$).
  - §4 (Codim-2 / codim-4 defects).
  - §5 (Defect cohomology; bulk-to-defect kernel).

  *Cross-volume firewall: per CLAUDE.md, treat as analytic
  apparatus only; no manuscript claim flows from CGW results
  without matched-conventions theorem (W28 template). Read for
  technique, not for theorem-import.*

### T6.H. Local-cohomology / residue duality apparatus

* **Hartshorne, *Residues and Duality***, Springer LNM 20,
  1966:
  - **III.2** (Local cohomology; Cousin / Serre dual on
    punctured disk).
  - III.10.10 (Higher-symplectic-dim duality).

* **Lipman, *Notes on Derived Categories and Derived
  Functors***, Springer LNM 1960, 2009:
  - §3.3 (Derived $\bar\partial$-Hodge apparatus on $\C^n$).

### T6.I. Russian-school chiral / vertex algebra apparatus

* **Frenkel-Ben-Zvi, *Vertex Algebras and Algebraic Curves***
  (AMS 2004):
  - §3.4 (Vertex algebra ≃ chiral algebra on $\mathbb A^1$).
  - §19.5 (Chiral algebra deformation theory).

* **Drinfeld, *DG Quotients of DG Categories***, J. Algebra
  2004 (arXiv:math/0210114):
  - §1–§3 (DG quotient apparatus; useful for Avenue (D)
    quotient construction).

### T6.J. Interpretation-priority recommendation

For a single-researcher first-year program, the study-priority
order:

1. (M-3 prereq) Lurie HA §5.5.4 + CG Vol. I §6.4–6.5
   (foundation; ~3 weeks).
2. (M-3 prereq) Williams arXiv:2007.13985 + Ayala-Francis
   J. Topology 2015 (factorization homology; ~2 weeks).
3. (M-3 prereq) BD *Chiral Algebras* §3.3–3.4 (chiral
   algebra; ~3 weeks).
4. (M-6 prereq) CG Vol. II Ch. 10–11 + Costello *RG and EFT*
   Ch. 9–10 (analytic apparatus; ~4 weeks).
5. (M-12 prereq) Knudsen + Ayala-Francis-Tanaka (stratified;
   ~2 weeks).
6. (M-18 prereq) Hartshorne *Residues and Duality* III.2 +
   Frenkel-Ben-Zvi (residue / vertex algebra; ~2 weeks).

Total foundational interpretation: ~16 weeks before sustained research
work begins. This is consistent with the M-3 milestone.

---

## §T7. 200-word summary

Phase-4 G1 research outline for the R²×C² Weiss-product-stability
obligation (M-37 ingredient I-4; identifier `R-W3-W9-A`),
flagged beyond-reach by Wave-3 W9. The obligation, boxed (W-2D)
per W9-§1.2, asserts Weiss-cosheaf descent on
$\R^2 \times \C^2$ for the unreduced classical observables FA;
its decomposition is the M-37 four ingredients, with (I-4) the
genuinely hard piece. Known-results landscape: Lurie HA §5.5.4
(locally constant + Dunn additivity) covers $\R^n$-only;
Costello-Gwilliam Vol. I §6.4–6.5 / Vol. II §11.4 covers
holomorphic Chern-Simons + defect; Beilinson-Drinfeld §3.4.10–11
gives chiral-product on smooth curves; Ayala-Francis covers
topological factorization homology. None close the
mixed-topological-holomorphic case on non-product Weiss covers.
Five attack avenues: direct Čech (A); mixed Dunn additivity
(B); factorization homology (C); BD chiral product (D); $E_2$
brane-line reduction (E). Recommended sequencing: (E) and (B)
in 6–12 mo; (C) sanity-check; (D) at 12–18 mo; (A) last-resort.
Connections to W3-W11-05 (BD chiral interpretation of
factorization centre) — direct structural inheritance for (D);
W3-W31-T2 (5d M-theory bridge) — would supply (I-1)–(I-3) if
unconditionalized; W3-W26-T1 (column-Verma functoriality) —
constrains M-37 ingredients. Risk assessment names four risk
classes; mitigation via partial-success publication. Total
foundational interpretation ~16 weeks; full program ~18 mo+.

---

End of Phase-4 G1 research outline.
