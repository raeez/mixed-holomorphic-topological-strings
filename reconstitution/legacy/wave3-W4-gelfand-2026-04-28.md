# Wave 3 / W4 — Gelfand + Hypotheses lens (Raeez Lorgat)

**Date.** 2026-04-28.
**Author.** Raeez Lorgat.
**Lens.** Primary: Gelfand (concrete examples first; representation-theoretic
structure; distributions and functional analysis). Secondary: Hypotheses
(hidden, weakened, strengthened, or silently transferred hypotheses).
**Mandate.** Stress-test the Wave-2 sharpenings of Theorem D
(D₁/D₂/D₃ split, master entry M-28), the weighted Tate completion
ledger (T1–T5), the PBW vs coadjoint symbol action of M-15 and
W2-08 corollary, and the Schwartz/distributional content of the
locally constant principal-part factorization algebra of Theorem E.
Wave-1 declared a stable core; Wave-2 sharpened it with eight new
ledger entries (M-26 through M-37). W4 attacks four specific Wave-2
sharpenings concretely.

---

## §0. Summary

W4 finds the Wave-2 sharpenings substantially correct, with three
sharpenings of its own and one new residual. Net verdict: the D₁/D₂/D₃
split is well-posed and computes correctly on the explicit example
$z_1^2 z_2 \cdot \rho_{1,1}$. The PBW raising / coadjoint lowering
mismatch is dramatic (W4-01 below: $F_{2,1}$ raises $\Psi_{1,1}$ to
$\Psi_{2,1}$; the dual $z_1^2 z_2$ lowers $\rho_{1,1}$ to
$-2\rho_{0,1}$ — opposite directions on the lattice, opposite signs).
This is the sharpest possible counterexample to the proposed module
identification at length one.

The weighted Tate completion of T1 has a single explicit weight
hypothesis (Definition `defn:wt-degree-weight`, conditions W1
bracket-tame, W2 windowwise coadjoint-continuity, W3 Mittag-Leffler
coevaluation), with the canonical $w(d) = q^d$ working choice,
$q > 1$, concretely $q = 2$. T2–T5 are compatible with this weight
hypothesis but in different operational regimes; one shadow strengthening
inside T3 is **internally consistent** but worth flagging (W4-02).

W4 confirms the distribution discipline of Theorem E is correct in
the Schwartz / Hörmander sense: the abelian-ideal property of
$\mc P_I[1]$ inside $\mathfrak g_I$ (M-36) eliminates the only
ill-defined distributional product that would otherwise arise. No
nuclearity hypothesis is silently invoked.

W4 inscribes four ledger entries:

* **W3-W4-01** (severity 2, additive): explicit numerical computation
  of $F_{2,1}$ on the $\widetilde\Psi_{a,b}$ lattice and of
  $z_1^2 z_2$ on the $\rho_{a,b}$ lattice, confirming the coadjoint
  lowering / PBW raising separation of `thm:pbw-vs-deformation` at
  the simplest non-trivial bidegree $(1,1)$ and at the constant target
  $(0,0)$ — the latter recovering the constant-Hamiltonian removal
  consistent with M-31's $[\mathrm{Tr}\,\psi] \leftrightarrow [\bar c]$
  identification (W3 Witten lens).

* **W3-W4-02** (severity 2, sharpening): a mild **shadow weight
  hypothesis** appears in the Quillen-equivalence theorem of T3
  (`thm:tate-bar-cobar-quillen-equivalence`) when applied to the
  symmetric monoidal structure on the **product** Tate side. T3's
  admissible envelope is purely categorical; T1's exponential weight
  is the analytic regulator. The two are compatible only when the
  envelope is restricted to objects whose Tate filtration is
  **compatible with the bracket-tame condition W1**. T1 should
  cite T3 explicitly as the categorical home, and T3 should add a
  one-sentence note that the Tate tensor product on Mittag-Leffler
  systems is the W1-compatible one in T1's coefficient module.

* **W3-W4-03** (severity 2, confirmation + sharpening): the D₁/D₂/D₃
  split passes the concrete-example test. The simplest non-trivial
  example $z_1^2 z_2 \cdot \rho_{1,1} = -2\rho_{0,1}$ is verifiable
  by D₂ alone (the explicit residue formula); D₁ supplies the
  isomorphism $\rho_{a,b} \leftrightarrow \delta_{a,b}$ used to
  interpret the formula on the Taylor-dual side; D₃ is what blocks the
  parallel polynomial-realization route. The three subtheorems have
  disjoint hypotheses; they are not independent statements — D₁ is
  a categorical fact that gates D₂ and D₃ — and the partial order
  is **D₁ → (D₂ ∥ D₃)**. The Wave-2 phrasing "logically separable"
  is correct; "logically independent" would have been an
  overstatement.

* **W3-W4-04** (severity 1, distribution discipline): on the brane
  line $\R$, the smearing $\Theta_\rho(B) = B \otimes \rho[1]$
  pairs $\mathcal D'_c(I)$ with the discrete graded vector space
  $\mc P[1]$. The completed tensor product
  $\mathcal D'_c(I) \widehat\otimes \mc P[1]$ is the projective tensor
  product on a strict (LF) space tensored with a graded discrete
  space, well-defined without nuclearity invocation because the
  $\mc P[1]$-factor is finite-dimensional **degree by degree**. The
  Wave-2 finding M-36 (distribution-product avoidance is structural
  by abelian-ideal) is confirmed; the further functional-analytic
  point is that the locally constant cosheaf descent does not require
  nuclearity of the Tate factor either. This is purely a clarifying
  remark, not a defect.

**Residual proposal.** R-W3-W4-A: full distribution-class statement
for the brane-line factorization algebra at the level of
$\mathcal D'_c$-currents. The current statement is internally consistent
(M-36 + W4-04). A rigorous wave-front-set statement on the brane line
should be added as part of the Phase-4 closure plan (M-37 ingredient 4).

---

## §1. Concrete computations: the example $z_1^2 z_2$ acting on $\rho_{1,1}$ and on $\widetilde\Psi_{1,1}$

This is the simplest non-trivial example that exercises **all three
subtheorems** D₁, D₂, D₃ simultaneously.

### 1.1 PBW symmetric raising on $\widetilde\Psi_{1,1}$ (D₃ side: polynomial PBW shadow)

The formula from `prop:open-descendant-action`:
$$F_{p,q} : \widetilde\Psi_{a,b} \longmapsto (pb - qa)\,\widetilde\Psi_{a+p-1,\,b+q-1}.$$

For $(p,q,a,b) = (2,1,1,1)$:
- coefficient $= 2\cdot 1 - 1\cdot 1 = 1$,
- target index $= (1+2-1, 1+1-1) = (2,1)$.

So $F_{2,1}: \widetilde\Psi_{1,1} \mapsto \widetilde\Psi_{2,1}$.

This is **raising**: total bidegree $1+1 = 2$ goes to $2+1 = 3$.

The chain-level computation by `scripts/check_one_psi_homology.py`
(verified independently here):
- target word basis: `['xxy', 'xyx', 'yxx']` (3 words);
- raw chain-level bracket vector: `[0, 2, 0]` in this basis;
- expected total-symmetrization scale (single homology class): $1\cdot 2/3 = 2/3$;
- difference $[0-2/3, 2-2/3, 0-2/3] = [-2/3, 4/3, -2/3]$ lies in the
  d₂-image (verified by rank computation in the script).

So the chain-level bracket is $\mathrm{Tr}\,\psi$-cohomologous to
$1 \cdot \widetilde\Psi_{2,1}$. **Match.**

### 1.2 Coadjoint lowering on $\rho_{1,1}$ (D₂ side: principal-part coadjoint)

The formula from `thm:principal-part-coadjoint-uniqueness`:
$$z_1^p z_2^q \cdot \rho_{a,b} = -(pb - qa + p - q)\,\rho_{a-p+1,\,b-q+1},$$
with negative-index targets zero.

For $(p,q,a,b) = (2,1,1,1)$:
- coefficient $= -(2 - 1 + 2 - 1) = -2$;
- target index $= (1-2+1, 1-1+1) = (0,1)$.

So $z_1^2 z_2 \cdot \rho_{1,1} = -2\,\rho_{0,1}$.

This is **lowering**: total bidegree $1+1 = 2$ goes to $0+1 = 1$.

Direct Poisson check (coordinate calculation):
- Hamiltonian vector field $X_{z_1^2 z_2} = (\partial_{z_1}(z_1^2 z_2)) \partial_{z_2} - (\partial_{z_2}(z_1^2 z_2)) \partial_{z_1} = 2 z_1 z_2\,\partial_{z_2} - z_1^2\,\partial_{z_1}$;
- $X_{z_1^2 z_2}(z_1^{-2} z_2^{-2}) = 2 z_1 z_2 \cdot (-2) z_1^{-2} z_2^{-3} - z_1^2 \cdot (-2) z_1^{-3} z_2^{-2}$
  $= -4 z_1^{-1} z_2^{-2} + 2 z_1^{-1} z_2^{-2} = -2 z_1^{-1} z_2^{-2}$;
- multiplying by $dz_1 dz_2$: $-2\,\rho_{0,1}$. **Match.**

### 1.3 D₁ side: the Matlis identification $\rho_{a,b} \leftrightarrow \delta_{a,b}$

By D₁ (Matlis-module identification), $\rho_{1,1} \leftrightarrow \delta_{1,1}$
and $\rho_{0,1} \leftrightarrow \delta_{0,1}$. The coadjoint formula on the
$\delta$-side is the dual of the Poisson bracket:
$$(\mathrm{ad}^\vee_{z_1^2 z_2}\,\delta_{1,1})(z_1^m z_2^n)
  = -\delta_{1,1}(\{z_1^2 z_2,\, z_1^m z_2^n\}).$$
Computing $\{z_1^2 z_2, z_1^m z_2^n\} = (2 z_1 z_2)(n z_1^m z_2^{n-1}) - (z_1^2)(m z_1^{m-1} z_2^n)$
$= (2n - m) z_1^{m+1} z_2^n$. The right-hand side is nonzero only when
$(m+1, n) = (1,1)$, i.e. $m = 0$, $n = 1$, giving coefficient $2 \cdot 1 - 0 = 2$.
So $(\mathrm{ad}^\vee_{z_1^2 z_2}\,\delta_{1,1})(z_2) = -2$. Equivalently
$\mathrm{ad}^\vee_{z_1^2 z_2}\,\delta_{1,1} = -2\,\delta_{0,1}$. **Match.**

The three subtheorems are internally consistent on this example.

### 1.4 Diagnostic: PBW raising and coadjoint lowering are not even
**directionally** the same module action

Side-by-side at $(p,q) = (2,1)$ for several $(a,b)$:

| $(a,b)$ | $F_{2,1} \cdot \widetilde\Psi_{a,b}$ (raising) | $z_1^2 z_2 \cdot \rho_{a,b}$ (lowering) |
|---------|-----------------------------------------------|-----------------------------------------|
| $(0,0)$ | $0\cdot \widetilde\Psi_{1,0} = 0$              | (target $-1 < 0$): $0$                  |
| $(0,1)$ | $2\,\widetilde\Psi_{1,1}$                       | (target $-1 < 0$): $0$                  |
| $(0,2)$ | $4\,\widetilde\Psi_{1,2}$                       | (target $-1 < 0$): $0$                  |
| $(1,0)$ | $-1\,\widetilde\Psi_{2,0}$                      | $0\cdot \rho_{0,0} = 0$                 |
| $(1,1)$ | $1\,\widetilde\Psi_{2,1}$                       | $-2\,\rho_{0,1}$                        |
| $(2,0)$ | $-2\,\widetilde\Psi_{3,0}$                      | $1\,\rho_{1,0}$                         |

The directions move oppositely: raising (D₃ side) versus lowering
(D₂ side). The two $(0,b)$ rows show the dramatic asymmetry — for
$b \geq 1$ the PBW side gives a non-zero raising while the coadjoint
side is identically zero (negative target index). This is the structural
content of `thm:no-polynomial-realization-categorical` (D₃) at the
level of explicit numerical pairing.

The constant case $(a,b) = (0,0)$: PBW gives zero by the coefficient
$pb - qa = 0$; coadjoint gives zero because the target index $-1 < 0$.
The two zeros have **different reasons** — the PBW reason is that the
constant Hamiltonian generator $\widetilde\Psi_{0,0}$ has zero cyclic
derivative, and the coadjoint reason is that there is no
$\rho_{-1,b'}$. This double zero is exactly what M-31 (W3-03)
identified as the constant-Hamiltonian removal: both sides of CE/PV
remove the same line, viewed from the closed and open sides.

### 1.5 Quantum/Moyal attack: the no-go at the linear-Hamiltonian level

The script verifies: for the linear Hamiltonian $z_1$ ($p=q=1$ becomes
$p=1, q=0$), the PBW relabelled action is
$z_1: \rho_{a,b} \mapsto a\,\rho_{a-1,b}$ (relabelled from
$z_1: \widetilde\Psi_{a,b} \mapsto b\,\widetilde\Psi_{a,b-1}$ via the
identification $\rho \leftrightarrow \widetilde\Psi$, swapping
$a \leftrightarrow b$ since the labels in the PBW formula are
$a+p-1, b+q-1$ with $p=1,q=0$ giving $(a, b-1)$).

The Moyal coadjoint action at $\hbar^0$ leading order: $z_1 \cdot \rho_{a,b}
= -(b+1)\,\rho_{a,b+1}$, which is direction $b \mapsto b+1$, not
$b \mapsto b-1$.

**Already at $\hbar^0$ leading order**, the leading-term assumption
$\widetilde\Psi_{a,b} \mapsto \rho_{a,b} + O(\hbar)$ contradicts the
$\mathfrak h$-equivariance condition. This is the exact
content of `thm:no-hbar-primitive-descendant-intertwiner` of T5
(which is the stable-core attack on the Wave-1 M-02).

Wave-2 confirmation: the universal categorical no-go of M-29 (W4-06,
the Etingof wave) is correct. W4 of Wave 3 confirms it numerically at
the smallest possible bidegree.

---

## §2. The weighted Tate completion (T1) and its propagation through T2–T5

### 2.1 The explicit weight hypothesis in T1

The weight is defined in `defn:wt-degree-weight` (T1 lines 125–146):
a function $w : \Z_{\geq 1} \to \R_{>0}$ satisfying
- **W1 bracket-tame:** $w(p+q-2) \leq C_w\,w(p)w(q)$ for $p,q \geq 2$;
- **W2 windowwise coadjoint-continuity:** finite ratio bound on
  finite-window coadjoint shifts;
- **W3 Mittag-Leffler coevaluation:** truncation of the finite-window
  Casimir is compatible with surjective truncation maps.

The canonical choice is exponential: $w(d) = q^d$ with $q > 1$,
concretely $q = 2$ (Remark `rmk:wt-canonical-weight`). This satisfies
W1 with $C_w = q^{-2}$, W2 by finite-set finiteness, W3 by surjective
transition.

### 2.2 Cross-reference table: where weights appear in lanes T1–T5

| Lane file | Weight reference | Level | Compatibility with T1 W1/W2/W3 |
|-----------|-------------------|-------|--------------------------------|
| T1 | full definition `defn:wt-degree-weight`; canonical $w(d) = q^d$ | analytic regulator | self-consistent |
| T2 | route R2 (nilpotent truncation) is the **alternative** to weighted route R1. T2 mentions "weighted Tate completion (R1)" only at line 21 and explicitly states it is the alternative. T2 uses **finite-dimensional** $\mathfrak h_{\leq N}$ (no weight needed; the Casimir is a finite sum). | structural alternative | non-overlapping |
| T3 | "admissible envelope" `stmt:tate-model-envelope`; admissible filtered quasi-isomorphisms; Mittag-Leffler exactness invoked at lines 113, 189, 249, 301, 313, 369, 410, 480, 514, 523, 578. **No** explicit weight function $w$. | categorical envelope | compatible if W3 holds (see W4-02) |
| T4 | "weighted coefficient category" cited at lines 136, 138, 148; defers analytic content to T1 + Problem `prob:weighted-rg-locality`. | analytic regulator (defers to T1) | self-consistent |
| T5 | "Tate/weighted coefficient kernel" cited once at line 737. | structural reference | self-consistent |

### 2.3 Shadow weight hypothesis in T3 (W4-02)

T3 establishes the Quillen equivalence in the **admissible** Tate
envelope. The envelope is purely categorical (filtered
quasi-isomorphisms on every quotient and on associated graded; tensor
product completed on Mittag-Leffler systems; surjective filtered
inverse limits exact). T3 does **not** state any analytic weight
hypothesis.

But T3's tensor product on Mittag-Leffler systems is what allows the
W3 condition of T1 to function: surjective truncation maps in the
Tate filtration with finite-dimensional pieces. The compatibility is
**implicit**.

The shadow strengthening: T3 is self-contained at the categorical
level, but when applied to the **product** Tate factor
$\mathfrak h_w$ of T1, the relevant Tate windows are the
$\prod_{d \leq w_0}H_d^{(w)}$, which are finite-dimensional regardless
of the weight $w$. The bracket on these windows is **bracket-tame in
$w$ by W1**; this property is what makes the Lie bracket continuous in
the T3 tensor product. Without W1, T3's Quillen equivalence applied to
the weighted coefficient pair would not give a model-categorical
statement that respects the Lie bracket — it would only give a
linear-algebraic Quillen statement.

**Verdict.** T3 is correct at the model-categorical level (no
hidden hypothesis). When **combined with T1**, the W1 condition
provides the bracket continuity needed for the tensor product to be
a tensor product of dg Lie algebras. Wave-2 sharpening: add a
one-sentence cross-reference in T1 saying "the categorical home is
T3's `stmt:tate-model-envelope`, and the bracket on $\mathfrak h_w$
is continuous in the T3 Tate tensor product because of W1 above" and
in T3 saying "the Tate Lie algebras to which this Quillen equivalence
applies in this manuscript are the **weighted** $\mathfrak h_w$ of T1
+ the nilpotent truncations $\mathfrak h_{\leq N}$ of T2, both of
which satisfy the categorical envelope hypothesis."

This is **not** a defect of either lane file; it is a clarifying
cross-reference. Severity 2.

### 2.4 The strict unweighted no-go (T1 endpoint)

T1's `thm:strict-unweighted-no-go` is unconditional: in the strict
$\mathfrak h_\Pi \widehat\otimes D_\oplus$ pair, **no** Casimir-like
tensor with the right finite-window projections exists. Wave 2's M-26
five-way C₁/C₂ split codifies this. W4 confirms: the example
`ex:weighted-completion-changes-cohomology` of T1 lines 766–787
exhibits a sequence with one nonzero covector in every degree, whose
class in $D_{\Pi,w}/D_\oplus$ is nonzero. This **is** a tail state
absent from the strict continuous dual. The weighted theory and the
strict theory are not regulator-equivalent in ordinary cohomology
even though they are filtered weak equivalent in the admissible
envelope.

**Wave-2 sharpening verified.** The C₂(W) variant of M-26 (weighted
Tate, enlarged coefficient category) is genuinely a different theorem
from C₁ᶜᵒᵐᵖ (completed, symmetric-filtration) or C₂(R)
(regulator-independent finite-window): the cohomology classes detected
are different.

---

## §3. The D₁/D₂/D₃ partial order: D₁ gates D₂ and D₃

W2-08 split the unified `thm:principal-part-coadjoint-uniqueness` into
three:
- **D₁** Matlis-module identification: $\mc P \cong \mathfrak h^\vee_{\mathrm{cont}}$,
  natural under Symp$_{\mathrm{form}}$;
- **D₂** Residue-pairing T²-Cartan rigidity: explicit formula
  $\rho_{a,b} \leftrightarrow \delta_{a,b}$ unique up to scalar;
- **D₃** No-go for polynomial $\mathfrak h$-module realization.

W2 phrasing: "logically separable" (correct). W4 sharpening: the
three subtheorems are **not** logically independent.

**D₁ gates D₂** because D₂ is "the unique formula for the isomorphism
of D₁". Without D₁, D₂ has no isomorphism to normalize.

**D₁ gates D₃** because D₃ is "no polynomial realization of the
$\mathfrak h$-module $\mc P$ (defined via D₁'s Matlis identification)
exists". Without D₁, the $\mathfrak h$-module structure on $\mc P$
is not defined.

**D₂ ∥ D₃** in the sense that neither implies the other:
D₂ is rigidity-of-formula (categorical T²-rigidity);
D₃ is impossibility-of-pull-back (local nilpotence vs principal-part).
They use disjoint proof techniques (T²-Cartan rigidity vs locally
nilpotent linear Hamiltonian).

W4 verdict on the W2 split: **correct, well-posed, internally
consistent**. The partial-order clarification (D₁ gates the other two)
is a sharpening, not a correction.

### 3.1 Concrete example test of the split

Use the case computed in §1: $z_1^2 z_2 \cdot \rho_{1,1} = -2\,\rho_{0,1}$.

- **D₁ supplies:** the categorical identification $\mc P \cong \mathfrak h^\vee_{\mathrm{cont}}$, sending $\rho_{a,b} \mapsto \delta_{a,b}$. This identifies $\rho_{1,1}$ with the Taylor-coefficient functional $\delta_{1,1}$.
- **D₂ supplies:** the formula $\rho_{a,b} \mapsto \delta_{a,b}$ is the **unique** continuous $\mathfrak h$-equivariant isomorphism $\mc P \to \mathfrak h^\vee_{\mathrm{cont}}$ up to a single scalar $c$. With $c$ fixed by the residue normalization $\langle \rho_{0,0}, 1 \rangle = 1$ (or its reduced equivalent on $\mc P$), the formula is rigid. This justifies writing the result as $-2\,\rho_{0,1}$ rather than as $-2c\,\rho_{0,1}$ for some unknown $c$.
- **D₃ supplies:** no polynomial $\mathfrak h$-module $M$ with locally nilpotent linear Hamiltonians realizes this $\rho \to \rho$ action. The example $z_1\cdot\rho_{a,b} = -(b+1)\rho_{a,b+1}$ is **not locally nilpotent**: $z_1^N\cdot\rho_{0,0} = (-1)^N N!\,\rho_{0,N}$ is nonzero for every $N$.

The three subtheorems compose to: "the formula $z_1^2 z_2\cdot\rho_{1,1} = -2\rho_{0,1}$ is canonical, well-defined, and cannot be transferred to a polynomial Lie module with the same action". W4 verifies this on the concrete example and finds the split well-posed.

### 3.2 Caveat: Wave-2 M-28's "D₃ already in manuscript"

W2-08 states D₃ is `thm:no-polynomial-realization-categorical`. W4
verifies this label resolves to `main.tex`:4148 (the categorical
no-go theorem). The W4 interpretation: the **categorical** no-go is the
sharpest D₃ — it rules out the realization in the abelian category
$\mathsf P_{\mathrm{pol}}$ of all polynomial $\bar A$-bimodules with
locally nilpotent linear Hamiltonian. Wave 2's universal no-go M-29
(W4-06 of W4) extends this to **any $\C[[\hbar]]$-linear category
with a forgetful functor to Lie-Mod** — strictly stronger than D₃.

So: D₃ ⊂ M-29 universal categorical no-go. The Wave-2 ledger
correctly identifies this hierarchy: M-29 cross-confirms M-28 D₃
(see master ledger §A entry M-29 cross-walk).

---

## §4. Distribution discipline of Theorem E (M-36 sharpening + W4-04)

### 4.1 The setup

Theorem E (`prop:reduced-principal-part-boundary-current`) defines
a $P_0$ factorization algebra on the brane line $\R$ with prefactorization
data
$$\mathfrak J_\partial^{\mathrm{Ham}}(I) = \Omega^\bullet_c(I) \widehat\otimes \bar A,\qquad
\mathfrak J_\partial^{\mathrm{pp}}(I) = \mathcal D'_c(I) \widehat\otimes \mc P[1].$$

These are **mixed test-function/distribution** smearing of the
polynomial Hamiltonian sector ($\Omega^\bullet_c$, smooth) and the
principal-part sector ($\mathcal D'_c$, distributional).

The bracket structure:
$$\{B_f(a), B_g(b)\} = B_{\{f,g\}}(ab),\qquad
\{B_f(a), \Theta_\rho(B)\} = \Theta_{f \cdot \rho}(aB),\qquad
\{\Theta_\rho(B), \Theta_\sigma(C)\} = 0.$$

The third bracket is the M-36 sharpening: zero by structural
abelian-ideal of the semidirect Lie algebra $\bar A \ltimes \mc P[1]$,
not by fiat.

### 4.2 Distribution-product question

The **first** bracket multiplies $a, b \in \Omega^0_c(I)$; smooth
functions multiply pointwise — well-defined.

The **second** bracket multiplies $a \in \Omega^0_c(I)$ by
$B \in \mathcal D'_c(I)$. The product $aB$ is the standard Hörmander
multiplication of a distribution by a smooth function — well-defined
(no wave-front collision).

The **third** bracket would multiply $B, C \in \mathcal D'_c(I)$ in
the distributional sense — **ill-defined** in general (Schwartz
impossibility theorem; Hörmander wave-front criterion can rescue
specific pairs but not the abstract operation). M-36 (W6-08) observed
that the abelian-ideal property forces this bracket to **zero**, so
the formalism never encounters the distributional product.

### 4.3 Functional-analytic check (Gelfand lens)

The smearing $\Theta_\rho(B) = B \otimes \rho[1]$ takes
$B \in \mathcal D'_c(I)$ and pairs it with $\rho \in \mc P[1]$, where
$\mc P = \bigoplus_{a+b > 0} \C\,\rho_{a,b}$ is **discrete**: a
graded direct sum of one-dimensional pieces.

The completed tensor product $\mathcal D'_c(I) \widehat\otimes \mc P[1]$
in this manuscript means the bidegree-by-bidegree pair: each fixed
$(a,b)$ contributes a copy of $\mathcal D'_c(I)$, and the sum
ranges over $a+b > 0$. **No nuclearity argument is needed** because
the second factor is finite-dimensional in each fixed degree.

This is the right notion: at the level of the cosheaf data, only
finite-rank distribution sectors are involved per degree.

The locally constant cosheaf descent (T3 theorem
`thm:locally-constant-equivalence`) treats
$I \mapsto \Omega^\bullet_c(I)$ and $I \mapsto \mathcal D'_c(I)$ as
the standard de Rham and current cosheaves on $\R$, both
locally constant in the sense that the inclusion $J \hookrightarrow I$
of a smaller open into a larger one is the extension by zero — the
unit of the cosheaf structure. **No** nuclear topology is invoked;
the descent is at the level of the cosheaf of degree-graded vector
spaces.

W4 conclusion: M-36 (distribution-product avoidance is structural)
extends to a fuller statement: **no functional-analytic completion
beyond bidegree-by-bidegree is silently invoked**. The Gelfand interpretation
is clean.

### 4.4 Residual: full wave-front-set statement

What W4 does **not** verify (the residual R-W3-W4-A): a rigorous
wave-front-set statement on the brane-line factorization algebra
of the form "for $I_1 \cap I_2 = \emptyset$, the singular support of
$\Theta_\rho(B_1) \cdot O_f(a_2)$ is contained in
$\mathrm{supp}\,B_1 \cup \mathrm{supp}\,a_2$, which is disjoint;
hence the factorization product is well-defined". This is the
content M-37 ingredient 4 of the Phase-4 plan.

The Hadamard-Mittag-Leffler reduction of T1 already controls the
**bulk** wave-front, but the **brane-line** statement at the level
of $\mathcal D'_c$ requires the same machinery applied to the
defect direction.

---

## §5. Ledger entries

### W3-W4-01 — Concrete F_{2,1} on Ψ_{1,1} and z_1²z_2 on ρ_{1,1} verifies the D₂/D₃ separation
**Severity 2 (additive). Status valid. Confidence high.**
**Lens.** Gelfand (concrete example) + Hypotheses (verifying that the
formulas of D₂ and D₃ are not silent strengthenings of each other).
**Provenance.** Wave-2 W2-08 (D₁/D₂/D₃ split, M-28). W3-W4 explicit
computation.
**Target.** `main.tex` Theorem D area 3650–4115;
`scripts/check_one_psi_homology.py` (already inscribes the relabelled
PBW vs Moyal mismatch sweep).
**Computation.** $F_{2,1}\cdot \widetilde\Psi_{1,1} = \widetilde\Psi_{2,1}$
(raising; verified at chain level by 2 in word `xyx` mod boundaries).
$z_1^2 z_2 \cdot \rho_{1,1} = -2\,\rho_{0,1}$ (lowering; verified by
direct Poisson coordinate calculation $-4 z_1^{-1} z_2^{-2} + 2 z_1^{-1} z_2^{-2}$).
**Diagnostic.** The two formulas have **opposite directions on the
bidegree lattice** and **opposite signs** at the simplest case
$(p,q,a,b) = (2,1,1,1)$. This is the structural separation of
`thm:pbw-vs-deformation` at length one — already adequate to refute
the polynomial label-projection $\widetilde\Psi_{a,b} \mapsto \rho_{a,b}$.
**Cross-reference.** Confirms T5
`thm:no-hbar-primitive-descendant-intertwiner` at the smallest possible
bidegree.
**Minimal heal.** None needed; the manuscript already contains the
dual-direction formula. W4 contribution: explicit verification table
in this report (see §1.4 above) plus the constant-Hamiltonian double
zero observation (M-31 cross-link).
**Residual.** None.
**Adjudication.** Valid. Concrete-example test passes; Wave-2 D₂/D₃
split is computationally verified.
**Deciding evidence.** The §1 computation table.

### W3-W4-02 — T3 admissible envelope is bracket-aware only via T1 W1
**Severity 2 (sharpening cross-reference). Status valid. Confidence high.**
**Lens.** Hypotheses (silent compatibility between two lane files).
**Provenance.** W3-W4 interpretation of T1 vs T3 cross-references.
**Target.** `tate-T1-weighted-completion.tex` Definition `defn:wt-degree-weight`;
`tate-T3-quillen-equivalence.tex` Statement `stmt:tate-model-envelope`
(line 46) and the Quillen-equivalence theorem.
**Claim under attack.** That the T3 admissible Tate model envelope is
fully self-contained at the categorical level when applied to the
T1 weighted coefficient pair.
**Broken step.** None at the model-categorical level: T3's tensor
product on Mittag-Leffler systems is the right notion. But
**bracket continuity** — the property that the dg Lie algebra
structure on $\mathfrak h_w \ltimes \mathfrak h^{\vee,w}_{\mathrm{cont}}[1]$
is preserved by the Tate tensor product — requires **W1 bracket-tame**
of T1, not stated in T3.
**Minimal heal.** Add one cross-reference sentence to each:
- T1 (after `defn:wt-degree-weight` or
  `defn:wt-coefficient-pair`): "The categorical home of this
  weighted coefficient pair is the admissible Tate envelope of
  Statement~\ref{stmt:tate-model-envelope} of T3; condition W1 above
  is the bracket-tame condition that lifts the Tate tensor product to
  a tensor product of dg Lie algebras in that envelope."
- T3 (after the Quillen equivalence theorem or
  `stmt:tate-model-envelope`): "When applied to the weighted
  coefficient pair $(\mathfrak h_w, \mathfrak h^{\vee,w}_{\mathrm{cont}})$
  of T1 or to the nilpotent truncation $\mathfrak h_{\leq N}$ of T2,
  bracket continuity in the Tate tensor product is provided by W1
  (bracket-tame, T1) or by finite-dimensionality (T2), respectively."
**Residual.** None.
**Adjudication.** Valid clarifying cross-reference. Not a defect of
either file in isolation.
**Deciding evidence.** The cross-reference sentences.

### W3-W4-03 — D₁/D₂/D₃ partial order: D₁ gates D₂, D₃; D₂ ∥ D₃
**Severity 2 (sharpening). Status valid. Confidence high.**
**Lens.** Hypotheses (silent assumption about logical independence).
**Provenance.** W2-08 (Wave-2 phrasing "logically separable") and
W3-W4 partial-order analysis.
**Target.** `main.tex` D₁/D₂/D₃ split (post-W2 implementation);
`reconstitution/wave2-W2-drinfeld-2026-04-28.md` §3.
**Claim under attack.** That D₁, D₂, D₃ are "logically independent".
**Broken step.** D₂ depends on D₁ for the existence of the isomorphism
to be normalized; D₃ depends on D₁ for the $\mathfrak h$-module
structure on $\mc P$.
**Minimal heal.** Replace "logically independent" by "logically
separable, with partial order D₁ → (D₂ ∥ D₃) — D₁ gates D₂ and D₃,
which are mutually independent". Add to W2 §3 of
`wave2-W2-drinfeld-2026-04-28.md` a one-paragraph clarification of
the partial order.
**Residual.** None.
**Adjudication.** Valid sharpening.
**Deciding evidence.** The partial order observation in §3 above.

### W3-W4-04 — Theorem E distribution discipline: no nuclearity invoked
**Severity 1 (clarification). Status confirmed. Confidence high.**
**Lens.** Gelfand (Schwartz / functional analysis).
**Provenance.** Wave-2 M-36 (W6-08 distribution-product avoidance is
structural). W3-W4 functional-analytic verification.
**Target.** `main.tex` Theorem E area 4240–4380;
`appendix-factorization-current-conventions.tex`.
**Claim verified.** The completed tensor product
$\mathcal D'_c(I) \widehat\otimes \mc P[1]$ is well-defined as a
direct sum over $(a,b)$ with $a+b > 0$ of copies of $\mathcal D'_c(I)$,
because $\mc P[1]$ is discrete graded. **No nuclearity hypothesis is
silently invoked.**
**Mechanism.** The bidegree-by-bidegree completion is the right
notion in this paper because:
- the principal-part action $z_1^p z_2^q\cdot\rho_{a,b}
  = -(pb-qa+p-q)\rho_{a-p+1,b-q+1}$ is **finite** in the bidegree
  direction (single output bidegree per input);
- the $P_0$-bracket
  $\{O_{p,q}(a), \Theta_{a',b'}(B)\}$ involves multiplication of a
  smooth function $a$ by a distribution $B$ — well-defined;
- the bracket
  $\{\Theta_\rho(B), \Theta_\sigma(C)\}$ is zero by structural
  abelian-ideal (M-36 confirmation).
**Residual.** R-W3-W4-A: full wave-front-set statement on the
brane-line factorization algebra. Not in the present paper; flagged
as part of Phase-4 closure plan (M-37 ingredient 4).
**Adjudication.** Valid confirmation + clarification. M-36 sharpening
extends to: Theorem E uses no functional-analytic completion beyond
the bidegree-by-bidegree direct sum.
**Deciding evidence.** §4 above.

---

## §6. Verdict on Wave-2 sharpenings

W4 of Wave 3 verifies the four wave-2 sharpenings examined:

| Wave-2 entry | W4 verdict | Cross-reference |
|--------------|------------|-----------------|
| **M-28 (D₁/D₂/D₃ split)** | Correct, well-posed; concrete example $z_1^2 z_2\cdot\rho_{1,1}$ confirms internal consistency. Minor sharpening: D₁ gates the other two (W3-W4-03). | W3-W4-01, W3-W4-03 |
| **M-26 (5-way C₁/C₂ split)** | Correct, well-posed; the `ex:weighted-completion-changes-cohomology` of T1 confirms C₂(W) is genuinely different from C₂(R). | §2.4 |
| **M-29 (universal categorical no-go)** | Correct; numerical confirmation at the smallest non-trivial bidegree (PBW raises, coadjoint lowers, opposite directions). | §1.4 |
| **M-36 (distribution-product avoidance is structural)** | Correct; further functional-analytic confirmation that no nuclearity is silently invoked. | W3-W4-04 |

W4 inscribes one new sharpening cross-reference (W3-W4-02) between
T1 and T3 that does not change either lane statement but makes the
weighted-bracket-continuity link explicit. W4 inscribes one new
clarifying remark (W3-W4-04) on Theorem E distribution discipline.

W4 inscribes one new residual:
- **R-W3-W4-A:** rigorous wave-front-set statement on the brane-line
  factorization algebra at $\mathcal D'_c$-current level. Phase-4
  closure ingredient (consistent with M-37 ingredient 4).

W4 confirms the Wave-2 declaration of stable core. The platonic-ideal
manuscript closes its Theorem D and Theorem E content correctly under
the Wave-2 sharpenings; the M-29 universal no-go correctly
generalizes the categorical D₃; the M-36 distribution-product
avoidance is structural and the present functional-analytic
discipline (bidegree-by-bidegree direct sum) is sufficient.

---

## §7. Provenance

W4 wave-3 attack-heal entry, lensed by Gelfand (concrete example
first; representation-theoretic structure; functional analysis) +
Hypotheses (silent strengthening / weakening). Built on Wave-2
master-ledger entries M-26, M-28, M-29, M-36 and on direct inspection
of `main.tex` Theorem D area (lines 3295–4239), Theorem E area
(lines 4240–4380), `tate-T1-weighted-completion.tex` (full),
`tate-T2`–`tate-T5` (weight cross-references),
`appendix-matlis-principal-parts.tex` (full), and
`scripts/check_one_psi_homology.py` (executed, all checks pass).

Concrete computations performed in Python (Fraction arithmetic) and
by hand (coordinate-form Poisson bracket).

ID prefix `W3-W4-` for all wave-3 lens-W4 entries.

End of W4 wave-3 ledger fragment.
