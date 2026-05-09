# Wave 3 / W9 — Drinfeld + Definitions Lens

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Drinfeld (moduli, stacks, chiral/factorization structures,
canonical constructions, hidden groupoids) + Definitions (every
object defined before use; stability of definitions under
operations).
**Inputs.** Master ledger
`reconstitution/attack-heal-platonic-2026-04-28.md` items M-14,
M-29, M-37, R-W4-A, R-W6-Weiss-defect, R-03; Wave-3 W2 deliverable
`reconstitution/wave3-W2-gaiotto-2026-04-28.md` §0–§9 (the residual
identification: the Weiss condition on $\R^2\times\C^2$ for the
unreduced FA stays open, with the M-37 four-ingredient
decomposition); Wave-2 W6
`reconstitution/wave2-W6-beilinson-2026-04-28.md` §0–§9 (the
eight-link DAG; W6-04 hypothesis paragraph for Lurie 5.5.4; W6-07
sharpened R-03); Wave-2 W2
`reconstitution/wave2-W2-drinfeld-2026-04-28.md` §1–§6 (Drinfeld's
Tannakian moduli interpretation; volume-datum canonicity; Theorem D split);
Wave-3 W6 `wave3-W6-costello-composition-2026-04-28.md`
W3-W6-04 (regulator-class canonicity);
`appendix-factorization-current-conventions.tex` (full);
`tate-T3-quillen-equivalence.tex` lines 510–589;
`appendix-matlis-principal-parts.tex` lines 1–130;
`main.tex` 2050–2230, 2680–2756.
**Mode.** Proposal-only. No commits. Master ledger schema; IDs
prefix `W3-W9-`.
**Independence.** The W2 Wave-3 split (brane-line $\R$ Weiss
**discharged**; ambient $\R^2\times\C^2$ Weiss **stays open** with
M-37 four-ingredient decomposition) is taken as **input under
attack** through the Drinfeld + Definitions lens. The
deliverable is a precise problem statement for the
$\R^2\times\C^2$ Weiss condition, a primary-source citation
audit (Lurie HA §5.5.4; Costello–Gwilliam Vol. I §6.4–§6.5,
Vol. II §11.4 + §A.5; Beilinson–Drinfeld *Chiral Algebras*
§3.4 + §3.4.10), a Drinfeld-stack interpretation of the
bi-infinite parent, and a canonicity audit cross-walked
against W3-W6-04.

---

## §0. Lens calibration: what Drinfeld + Definitions buys

A Drinfeld interpretation of a factorization-algebra construction asks
five questions:

(D1) *What is the Ran space / underlying stratification?* For a
factorization algebra on $\R^2\times\C^2$ the Ran space is
$\mathrm{Ran}(\R^2\times\C^2) = \bigsqcup_n
(\R^2\times\C^2)^n / S_n$, the moduli of finite non-ordered
collections of points. The Weiss topology is the natural
topology on the Ran space.

(D2) *What is the canonical construction (no choices)?* A
Beilinson–Drinfeld factorization algebra is canonical from a
chiral algebra, and a chiral algebra is canonical from a
chiral coalgebra; the dictionary is *factorization product
$\leftrightarrow$ chiral cobracket on $\Delta^*\mathcal F$*
(BD §3.4).

(D3) *Which moduli stack hosts the construction?* The
factorization centre on $\R^2\times\C^2$ is a global section of
a stack on $\mathrm{Ran}(\R^2\times\C^2)$; identifying that
stack and its monodromy makes the construction canonical.

(D4) *Are there hidden groupoids?* When a "choice" appears, the
groupoid of choices and the action on the construction must
be tracked. In particular, regulators, Weiss covers, and Tate
windows all sit in groupoids.

(D5) *Do the definitions compose?* The Definitions lens checks
whether the objects defined in one definition are valid inputs
to the next, especially across category boundaries (TateVec
vs $\Cat{Vect}$; ind-finite vs pro-finite).

The five questions structure the §1–§4 targets.

---

## §1. Target T1 — The R²×C² Weiss condition: precise statement

**The locus.** `prop:weiss-cosheaf-residual` in
`tate-T3-quillen-equivalence.tex` lines 530–562 (cited in
`main.tex` inside `thm:open-closed-derived-center-derived` proof);
already updated in spirit by W6-07 / M-37 to four ingredients;
W3-W2 §1 verified the brane-line-only piece is discharged.

### §1.1 Definitions audit (Definitions lens)

**Definition 1 (Weiss cover).** Following Costello–Gwilliam,
*Factorization Algebras in Quantum Field Theory*, Vol. I §6.5
Definition 6.5.0.1: a *Weiss cover* of an open $V\subseteq M$
in a manifold $M$ is a collection
$\mathcal U=\{U_\alpha\subseteq V\}$ such that for every finite
collection $\{x_1,\ldots,x_n\}\subset V$ there exists
$\alpha=\alpha(x_1,\ldots,x_n)$ with $\{x_1,\ldots,x_n\}\subset
U_\alpha$. (Equivalently: $\mathcal U$ generates the Weiss
topology on $V$.) Stable under restriction; not stable under
arbitrary product (see §1.3).

**Definition 2 (Weiss-cosheaf condition).** CG Vol. I §6.5
Definition 6.5.0.5 / §A.5.4: for a prefactorization algebra
$\mathcal F$ on $M$ and $V\subseteq M$, $\mathcal F$ satisfies
the *Weiss-cosheaf condition* on $V$ if for every Weiss cover
$\mathcal U$ of $V$ the natural map
$$\mathrm{Tot}\,\check{\mathrm C}^\bullet(\mathcal U;\mathcal F)
  \xrightarrow{\sim}\mathcal F(V)$$
is a quasi-isomorphism. Here the Čech complex is built from
multi-disjoint inclusions $U_{\alpha_0}\sqcup\cdots\sqcup
U_{\alpha_p}\subseteq V$ with the alternating extension-by-zero
differential.

**Definition 3 (factorization algebra).** CG Vol. I §3.1: a
prefactorization algebra $\mathcal F$ on $M$ is a multifunctor
$\mathcal F:\mathrm{Disj}(M)\to\Cat C$ satisfying the
disjointness factorization map
$\mathcal F(U_1)\otimes\cdots\otimes\mathcal F(U_n)
\to\mathcal F(V)$ for $U_1\sqcup\cdots\sqcup U_n\subseteq V$. It
is a factorization algebra if it satisfies the Weiss-cosheaf
condition.

**Stability under operations (Definitions lens check).**
* *Restriction to open* $V\subseteq M$: Weiss covers restrict to
  Weiss covers; FAs restrict. **Stable.**
* *Product on subsets of distinct manifolds.* If $\mathcal F$
  on $M$ and $\mathcal G$ on $N$, the external tensor product
  $\mathcal F\boxtimes\mathcal G$ on $M\times N$ is the
  prefactorization algebra
  $(\mathcal F\boxtimes\mathcal G)(U_1\sqcup\cdots\sqcup U_n) =
  \bigotimes_i \mathcal F(\pi_M(U_i))\otimes\mathcal G(\pi_N(U_i))$
  for **product opens** $U_i = U_i^M\times U_i^N$. **Stable as
  prefactorization algebra**, but a **product Weiss cover** of
  $V_M\times V_N$ is generally **not** a Weiss cover of the
  product (see §1.3 below). The Weiss condition does **not**
  factor through the product without extra input.
* *Push-forward along $f:M\to N$.* If $f$ is proper, the
  push-forward $f_*\mathcal F$ on $N$ exists; in general only the
  derived push-forward, not stable under finite-dim hypothesis.

**Conclusion (Definitions audit).** Definitions 1–3 are the CG
canonical definitions. Stability under restriction holds. Stability
under external product fails at the level of Weiss covers — the
critical observation for R-W6-Weiss-defect.

### §1.2 Precise statement of the residual

**W3-W9-01 (precise R-W6-Weiss-defect statement).** For
$M = \R^2\times\C^2$ and the unreduced classical observables
prefactorization algebra
$\mathrm{Obs}^{\mathrm{cl}}_{\mathrm{closed},H}$ defined on the
Hamiltonian BF theory of `main.tex`:1776–1797 (with action
$S = \int_{\R^2\times\C^2}\langle\beta,(D-\hbar Q)\alpha\rangle$,
$D = d_{\R^2}+\bar\partial_{\C^2}$, $Q$ the Hamiltonian BF
interaction), the **R²×C² Weiss condition** is the assertion:

*For every open $V\subseteq\R^2\times\C^2$ and every Weiss cover
$\mathcal U=\{U_\alpha\}$ of $V$, the natural map*
$$\boxed{\;\mathrm{Tot}\,\check{\mathrm C}^\bullet
  \bigl(\mathcal U;\mathrm{Obs}^{\mathrm{cl}}_{\mathrm{closed},H}\bigr)
  \xrightarrow{\sim}
  \mathrm{Obs}^{\mathrm{cl}}_{\mathrm{closed},H}(V).\;}
\tag{W-2D}$$

Where (W-2D) is interpreted in the chosen presentable Tate
$\infty$-category envelope (Lurie HA §5.5.4 hypothesis package per
W6-04).

**Compared to (W-1d) on the brane line.** The brane-line Weiss
condition on $\R$ (W3-W2-02–03) is **discharged**: the brane-line
FA $A_\partial^{\mathrm{Ham}}$ is built from the cosheaf
$\mathfrak h_I = \Omega^\bullet_c(I)\widehat\otimes\bar A$, and
$\Omega^\bullet_c$ is a cosheaf on $\R$ with extension-by-zero
structure maps; the symmetric-algebra functor commutes with Čech
totalisation under Roos ML (CG Vol. I §A.5.4); Weiss-on-$\R$ for
$A_\partial^{\mathrm{Ham}}$ reduces to Weiss-on-$\R$ for
$\mathfrak h$, which holds.

**Why (W-2D) is genuinely different.**
(a) The ambient $\mathrm{Obs}^{\mathrm{cl}}_{\mathrm{closed},H}$ is
**not** an external product
$\mathcal F^{\R^2}\boxtimes\mathcal F^{\C^2}\boxtimes\mathfrak h$:
the brane line $\R\times\{0\}\hookrightarrow\R^2\times\C^2$ is a
codim-5 defect, and the bulk-to-defect kernel
$K_{\mathrm{bd}}$ couples bulk fields to defect observables.
(b) The bulk side has $D=d_{\R^2}+\bar\partial_{\C^2}$
differential, not separated by direction; the Hamiltonian BF
interaction couples the $\R^2$ topological direction to the $\C^2$
holomorphic direction through the brane line. The Hamiltonian
appears as a connection (`main.tex`:1830–1836, "$\alpha$ as a
Hamiltonian function on $\C^2$ ... defines a connection on
$\R^2$ valued in Hamiltonian vector fields on $\C^2$").
(c) The principal-part fields $\rho_{a,b}$ are residue currents
on the codim-4 holomorphic subspace $\R\times\{0\}\subset\R\times\C^2$
inside $\R^2\times\C^2$ (`appendix-matlis-principal-parts.tex`:74–104,
basis labelled by $(a,b)\in\Z^2_{\ge 0}\setminus\{(0,0)\}$). Weiss
descent of these defect-localised distributions is *not* a CG
Vol. I §6.5 routine; it is a chiral-algebra factorization problem.

**(W-2D) decomposes into the M-37 four ingredients.**
(I-1) Heat-kernel propagator $P_{\epsilon,L}^{\R^2\times\C^2}$
separated into directions: $\R$-topological + $\bar\partial$-Hodge
transverse with brane line excised (Costello *RG and EFT* 2011
Ch. 9–10; CG Vol. II §11.4 holomorphic-Chern-Simons + defect).
(I-2) Defect boundary condition for $\R\times\{0\}\hookrightarrow
\R^2\times\C^2$ from the brane Lagrangian (`main.tex`:1830–1836).
(I-3) Bulk-to-defect kernel $K_{\mathrm{bd}}$ compatible with
Theorem D residue calculus and M-23 distribution-product avoidance.
(I-4) Mittag-Leffler resolution transverse to the brane: the
genuinely beyond-reach piece, recorded as R-W6-Weiss-defect.

**Cross-check against W3-W2-02–03.** W2 used the
symmetric-algebra-Čech commutation (Roos ML applied to
$\widehat{\mathbf S}$ acting on a cosheaf with surjective extension
maps and ML on the directed system) to discharge Weiss-on-$\R$.
On $\R^2\times\C^2$ the *underlying cosheaf* fails to be the
naive product cosheaf because (b) and (c) above forbid separation
of variables. Roos ML is therefore not directly applicable; the
heat-kernel propagator (I-1) is what supplies the analytic
glue that the cosheaf machinery alone cannot.

**Adjudication.** Definitions audit confirms the M-37
decomposition. The boxed statement (W-2D) is the precise
Drinfeld-canonical residual; the M-37 four ingredients are the
named obstructions; and (I-4) — the transverse Mittag-Leffler
on defect-localised distributions — is exactly the Beilinson–Drinfeld
chiral-algebra factorization problem.

---

## §2. Target T2 — Lurie HA §5.5.4 / Costello-Gwilliam §6.4 verification: does product stability hold?

**The question.** For the product
$\Omega^\bullet_c(\R^2)\widehat\otimes\Omega^\bullet_c(\C^2)
\widehat\otimes\bar A$ on $\R^2\times\C^2$, does Weiss on each
factor imply Weiss on the product? This is the open
*Weiss-product-stability* question.

### §2.1 Lurie HA §5.5.4 audit

**§5.5.4.10 (paraphrase).** Locally constant FAs on $\R^n$ are
equivalent to $E_n$-algebras in $\mathcal P r^L$; the equivalence
is via the disk frame bundle / Kan extension argument. The
*locally constant* condition on inclusions of disks $U\subseteq V$
is invoked, not the Weiss condition directly.

**Critical Lurie observation.** Lurie HA §5.5.4.10 establishes
*locally constant* FA $\simeq$ $E_n$-algebra; the Weiss condition
is built into Lurie's definition of factorization algebra via
factorizable presheaves, but the $E_n$-equivalence is on the
locally constant subcategory. **§5.5.4.10 does not itself prove
Weiss-product-stability**: it presupposes Weiss in the source.

**§5.5.4.16 (Lurie HA, May 2017 version).** The product
$E_m\otimes E_n \simeq E_{m+n}$ (Dunn additivity) holds in
$\mathcal P r^L$. This is product stability **on locally constant
$E_n$-algebras**, which are equivalent to Weiss FAs on $\R^n$ by
5.5.4.10 — *but only for the disk-translation-invariant subcategory*.
Lurie's proof requires the disk-frame-bundle Kan extension and
the locally constant condition on each factor.

**W3-W9-02 (product stability under Lurie 5.5.4).** *Locally
constant FAs* on $\R^m$ and $\R^n$ have product-stability
equivalence via Dunn additivity (Lurie HA §5.5.4.16); this gives
$\mathrm{Fact}^{\mathrm{lc}}(\R^m)\otimes
\mathrm{Fact}^{\mathrm{lc}}(\R^n)\simeq
\mathrm{Fact}^{\mathrm{lc}}(\R^{m+n})$. **For the manuscript's
mixed holomorphic-topological setting** $M = \R^2\times\C^2$, the
$\R^2$ factor is locally constant (topological) but the $\C^2$
factor is **holomorphic**, not topological: the
factorization algebra is *not* locally constant on the $\C^2$
factor. Lurie 5.5.4.16 **does not directly apply** — the
holomorphic-factorization side requires a different equivalence.

### §2.2 Costello-Gwilliam Vol. I §6.4 / Vol. II §11 audit

**CG Vol. I §6.4 / Example 6.4.0.5** (locally constant FA on $\R$
$\simeq E_1$-algebra): proven for the topological factor only.
Does **not** address holomorphic factorization or product
stability across mixed holomorphic-topological factors.

**CG Vol. II Ch. 10–11.** Holomorphic factorization algebras on
$\C^n$ via $\bar\partial$-Hodge propagator. The *holomorphic
locally constant* condition (factorization product on coordinate
polydisks via $\bar\partial$-quasi-isomorphism) is proved for the
holomorphic Chern–Simons + defect setup at CG Vol. II §11.4. This
is the analog of CG Vol. I §6.4 in the holomorphic direction.

**CG Vol. II §A.5.** Cosheaves on a manifold; Weiss-cosheaf
condition lifted to derived $\infty$-category. Provides product
stability **for cosheaves** under a list of hypotheses (proper
support, ML on directed systems, presentability of target).

**Does CG verify Weiss product stability for our setting?**
The relevant question is: for
$\Omega^\bullet_c(\R^2)\widehat\otimes\Omega^{0,\bullet}_c(\C^2)
\widehat\otimes\bar A$ as a cosheaf on $\R^2\times\C^2$, does
Weiss on each factor imply Weiss on the product?

* **Topological factor $\Omega^\bullet_c(\R^2)$.** Weiss on $\R^2$
  by CG Vol. I §A.5.4 (cosheaf of compactly supported de Rham
  forms is a cosheaf in the Weiss sense; structure maps
  surjective with ML).
* **Holomorphic factor $\Omega^{0,\bullet}_c(\C^2)$.** Weiss on
  $\C^2$ in the *holomorphic* sense by CG Vol. II §11.4
  ($\bar\partial$-Hodge cosheaf with compactly supported
  Dolbeault forms; structure maps inverse limits with ML on
  ascending Tate windows).
* **Product on $\R^2\times\C^2$.** *Naive product* of cosheaves
  is **not** automatically Weiss-cosheaf on the product, because
  Weiss covers of a product space are **not** generated by
  product Weiss covers. A point $(x,z)\in\R^2\times\C^2$ may
  be covered by a Weiss element of $\R^2\times\C^2$ that is
  *not* a product $U^{\R^2}\times U^{\C^2}$; e.g., a thin
  tubular neighbourhood of a non-axis-aligned curve.

**W3-W9-03 (Weiss-product-stability is OPEN).** Neither Lurie
HA §5.5.4 nor CG Vol. I §6.4 / Vol. II §11.4 / §A.5 directly
verifies that the external tensor product of two Weiss cosheaves
on $M$ and $N$ is a Weiss cosheaf on $M\times N$ in the strong
sense required for descent on **non-product** Weiss covers of
$M\times N$. The product theorem holds **for product Weiss
covers only**, not for arbitrary Weiss covers of the product.

**Source verification.**
- Lurie HA §5.5.4.16 (Dunn additivity) handles locally constant
  $E_n$-algebra products, hence **product Weiss covers** on
  locally constant FAs only. Does not extend to non-product
  covers.
- CG Vol. I §A.5.4 handles cosheaves on a single manifold; the
  product-on-the-product is in §A.5.6, but again at the level of
  product Weiss covers.
- BD *Chiral Algebras* §3.4.10 (product of chiral algebras) gives
  the chiral-product on $X\times Y$ from chiral structures on $X$
  and $Y$, but the descent on $X\times Y$ is a **separate
  theorem** (§3.4.11) requiring the chiral cobracket on
  $\Delta^*(\mathcal F\boxtimes\mathcal G)$ to satisfy the chiral
  axiom; this is **not** automatic.

**W3-W9-04 (precise problem statement of Weiss-product-stability).**
*Let $\mathcal F$ be a Weiss-cosheaf on $M$ and $\mathcal G$ a
Weiss-cosheaf on $N$, both valued in a presentable symmetric
monoidal $\infty$-category $\mathcal C$. Is the external tensor
product $\mathcal F\boxtimes\mathcal G$ a Weiss-cosheaf on $M\times
N$ for arbitrary Weiss covers of $M\times N$ (not necessarily
product covers)?* This is open in CG; partially addressed in BD
§3.4.10–11 under additional chiral-algebra hypotheses.

**For the manuscript:** the question reduces to whether
$\Omega^\bullet_c(\R^2)\widehat\otimes\Omega^{0,\bullet}_c(\C^2)
\widehat\otimes\bar A$ is a Weiss-cosheaf on $\R^2\times\C^2$
under arbitrary Weiss covers — the **same problem as M-37
ingredient 1**, the heat-kernel propagator, which is what
*supplies* the cross-axis descent inputs.

### §2.3 Disposition

**The residual stands and is sharpened.** Neither Lurie nor CG
verifies Weiss-product-stability for non-product covers. A fresh
proof is required for the manuscript's setting; the M-37
four-ingredient list (heat-kernel propagator, defect boundary
condition, bulk-to-defect kernel, transverse Mittag-Leffler) is
the correct decomposition.

**W3-W9-05 (citation precision).** In the heal patch for
`prop:weiss-cosheaf-residual`, cite:
- Lurie HA §5.5.4.16 (Dunn additivity for *locally constant*
  $E_n$, **not** the present mixed setting);
- CG Vol. II §11.4 (holomorphic FAs with defect; the closest
  analog);
- BD *Chiral Algebras* §3.4.10–11 (chiral-product descent
  hypotheses);
- Costello *RG and EFT* 2011 §10 (heat-kernel propagator).

The within-reach part of (W-2D) is M-37 (I-1)–(I-3); the
beyond-reach part is (I-4) = R-W6-Weiss-defect. *No primary-source
theorem closes the residual.*

---

## §3. Target T3 — Drinfeld stack interpretation of the bi-infinite parent (R-W4-A)

The Wave-2 W4 universal categorical no-go (M-29) identified the
PBW polynomial side and Matlis principal-part side as the
**positive and negative cones of one bi-infinite parent module
on $\Z^2$**. The W3-W2 §3.1 (W3-W2-09–10) interpretation:
formal-disk-to-punctured-disk interface in the local Hamiltonian
BF cannot be a deformation-theoretic single-object interface; it
is a $\Z^2$-graded bi-infinite parent with two cones (PBW raising
on positive cone, Matlis coadjoint on negative cone). R-W4-A
records the open question of whether a Hamiltonian-equivariant
splitting of the bi-infinite parent exists.

### §3.1 The Drinfeld stack candidate

**W3-W9-06 (canonical stack candidate).** Under the Drinfeld
moduli lens, the bi-infinite parent should be a quasi-coherent
sheaf on a moduli stack of formal symplectic disks. The natural
candidate:

$$\mathfrak{M}_{\mathrm{Symp},\C^2,0} :=
  \big[\mathrm{Spf}\,\C[[z_1,z_2]]\,\big/\,
  \mathrm{Symp}_{\mathrm{form}}(\C^2,0)\big],$$

the stack-theoretic quotient of the formal symplectic disk by
the formal symplectic loop group (cf. W2-04 wave-2,
`prop:matlis-symp-functorial`; this is the **Drinfeld classifying
stack of formal symplectic disks at a point**). The bi-infinite
$\Z^2$-graded parent on $\Z^2$ is the Borel-Moore homology of
the punctured disk fibered over $\mathfrak{M}_{\mathrm{Symp},\C^2,0}$:

$$\mathcal M_{\mathrm{bi-inf}} =
  H^{\mathrm{BM}}_\bullet\bigl(\widehat{\C^2}_0\setminus\{0\},
  \mathcal O\bigr)/\bigl(\mathcal O(\widehat{\C^2}_0)\cdot
  dz_1 dz_2\bigr),$$

(cf. R-W4-A statement, master ledger lines 1914–1920;
$\widetilde{\mathcal M}$ = bi-infinite parent of W4 §2). The
two cones:
* **Positive cone** $\mathcal M_{\mathrm{bi-inf}}^+ \cong
  \bar A = \C[z_1,z_2]/\C\cdot 1$, the polynomial Hamiltonian
  side (PBW);
* **Negative cone** $\mathcal M_{\mathrm{bi-inf}}^- \cong
  \mathcal P = H^2_{\mathfrak m}(R)\cdot dz_1 dz_2 / \C\cdot
  \rho_{0,0}$, the Matlis principal-part side.

The **residue duality** $\sigma:(a,b)\mapsto(-a-1,-b-1)$ is
the involution of the bi-infinite lattice $\Z^2\to\Z^2$
exchanging the two cones; in stack terms it is the
**Cousin/local-cohomology Serre dual** on the punctured disk, by
Hartshorne *Residues and Duality*, III.2.

### §3.2 Properties of the candidate stack

**W3-W9-07 (stack properties — Definitions audit).**
* **Smooth.** $\mathfrak{M}_{\mathrm{Symp},\C^2,0}$ is a
  *formal* stack, and $\mathrm{Symp}_{\mathrm{form}}(\C^2,0)$ is
  a pro-algebraic group (every truncation
  $\mathrm{Symp}_{\mathrm{form}}/\mathrm{Symp}_{\mathrm{form},\ge N}$
  is a finite-dim algebraic group). Smoothness holds at the level
  of formal completions on jets; **smooth in the formal sense**.
* **Finite-dimensional fibres.** Each stratum
  $\mathfrak{M}^{(N)}_{\mathrm{Symp},\C^2,0} := [\mathrm{Spf}\,
  \C[[z_1,z_2]]/\mathfrak m^{N+1}\,/\,\mathrm{Symp}_{\mathrm{form}}^{(N)}]$
  is a quotient of a finite-dim formal-disk-truncation by a
  finite-dim group, hence has *finite-dim fibres*. **Holds
  windowwise.**
* **Pro-algebraic structure.** $\mathfrak{M}_{\mathrm{Symp},\C^2,0}
  = \varprojlim_N \mathfrak{M}^{(N)}_{\mathrm{Symp},\C^2,0}$ in
  formal stacks; the inverse limit is along surjective
  truncation maps (ML on the inverse system). **Holds, by
  the Tate windowing of the manuscript.**
* **Hidden groupoid.** The action groupoid of
  $\mathrm{Symp}_{\mathrm{form}}(\C^2,0)$ on
  $\mathrm{Spf}\,\C[[z_1,z_2]]$ supplies the hidden groupoid;
  morphisms are formal symplectomorphisms.

**Stability (Definitions lens).** The bi-infinite parent
$\mathcal M_{\mathrm{bi-inf}}$ is a $\Z^2$-graded sheaf on
$\mathfrak{M}_{\mathrm{Symp},\C^2,0}$ stable under the
$\mathrm{Symp}_{\mathrm{form}}$-action by W2-04
(Symp-equivariance of the residue pairing) and W2-05
(socle-canonicity). **The construction is canonical at the
stack level.**

### §3.3 Does R-W4-A admit a Drinfeld-style resolution?

**W3-W9-08 (R-W4-A reformulated as a stack-cohomology
question).** The R-W4-A residual asks for a
Hamiltonian-equivariant splitting of the bi-infinite parent
$\mathcal M_{\mathrm{bi-inf}}$ into PBW positive cone +
Matlis-coadjoint negative cone. Under the Drinfeld stack lens,
this splitting question becomes:

*Does the natural exact triangle
$\mathcal M_{\mathrm{bi-inf}}^+\to\mathcal M_{\mathrm{bi-inf}}
\to\mathcal M_{\mathrm{bi-inf}}^-$ in
$\mathrm{QCoh}(\mathfrak{M}_{\mathrm{Symp},\C^2,0})$ split as a
$\mathrm{Symp}_{\mathrm{form}}$-equivariant exact triangle in
$\mathrm{QCoh}(\mathfrak{M}_{\mathrm{Symp},\C^2,0})$?*

The answer is **no, by M-29 universal no-go**: the splitting
would supply an $\hbar$-flat module with both cone fibres
simultaneously, which M-29 forbids. The residue duality
$\sigma$ is not a splitting; it exchanges the two cones rather
than separating them.

**Adjudication.** R-W4-A is **not** discharged by the Drinfeld
stack lens; it is *recast* as a non-existence of an equivariant
splitting in $\mathrm{QCoh}(\mathfrak{M}_{\mathrm{Symp},\C^2,0})$.
This is consistent with the W3-W2-09–10 Gaiotto interface
interpretation: M-29 closes the splitting in the negative.

**W3-W9-09 (Drinfeld stack interpretation reinforces M-29).**
The bi-infinite parent corresponds to a canonical sheaf on a
canonical Drinfeld stack with the expected smoothness /
finite-dim-fibres / pro-algebraic structure / hidden symplectic
groupoid; the impossibility of a Hamiltonian-equivariant
splitting (R-W4-A open) is the stack-cohomological avatar of the
M-29 universal categorical no-go.

**No new residual.** The Drinfeld stack interpretation does not
discharge R-W4-A but supplies a precise geometric framework. The
residual continues at the chiral-algebra factorization level
(BD §3.4 + Costello *RG and EFT* 2011 §10), reachable in Phase 4.

---

## §4. Target T4 — Canonicity of the factorization construction

Under the Drinfeld lens, factorization structures are CANONICAL
(no choices). Test: does the manuscript's factorization centre
$Z^{P_0}_{\mathrm{fact}}(A_\partial^{\mathrm{Ham}})$ depend on a
regulator choice, weight function, or completion choice?

### §4.1 Audit of choices in the construction

**Step-by-step inspection (Definitions lens).**

* **Choice (C1) — Tate envelope.**
  `thm:tate-model-structure` and `thm:tate-bar-cobar-quillen`
  (T3 lines 257–589): the admissible Tate envelope is generated
  by cofibrant generation `lem:transferred-model` +
  `lem:tate-conilp-model`. This is the **canonical presentable
  envelope** of the Tate vector spaces; not a choice in the
  Drinfeld sense — it is the **unique** presentable closure
  (Lurie HA A.2.6.8). **Canonical.**

* **Choice (C2) — Volume datum.** $\Omega = dz_1\wedge dz_2$.
  W2-04 (wave-2 W2 Drinfeld findings): $\Omega$ is canonically
  determined by $\omega = dz_1\wedge dz_2$ in $\dim_\C = 2$
  (Symp = SDiff). $\Omega$ is fixed by all of
  $\mathrm{Symp}_{\mathrm{form}}(\C^2,0)$. **Canonical.**

* **Choice (C3) — Regulator scheme.** Heat-kernel propagator
  $P_{\epsilon,L}^{\R^2\times\C^2}$ depends on the choice of
  regulator (heat-kernel vs Pauli-Villars vs Hadamard
  parametrix). W3-W6-04 (Wave-3 W6 Costello-Composition):
  *the M-26 split is canonical inside the admissible class of
  weights, but not across regulator-class boundaries*. The
  R-W3-W6-04 residual records cross-regulator-class canonicity
  as open. **NOT canonical at the regulator-scheme level**;
  canonical only inside the admissible class.

* **Choice (C4) — Weight function.** For the weighted Tate
  completion (T1), the weight $w(d) = q^d$ (or any admissible
  weight) is a choice; W3-W6-04 records this is canonical
  *within the admissible class*. **NOT canonical** without the
  admissibility hypothesis.

* **Choice (C5) — Completion (m-adic vs Tate).** The brane-line
  $\mathfrak h_I = \Omega^\bullet_c(I)\widehat\otimes\bar A$
  uses the Tate completion of $\bar A$ in degree zero. The
  Matlis dual side uses the $\mathfrak m$-adic completion of $R
  = \C[[z_1,z_2]]$. The two completions are related by
  Matlis-Grothendieck local-cohomology duality
  (`appendix-matlis-principal-parts.tex` Definition 2.4 +
  Proposition 2.6). The two-completion structure is *intrinsic*
  to the factorization construction (M-29 / W4-06 universal
  categorical no-go: PBW and Matlis are positive/negative cones
  of bi-infinite parent, residue-dual via Hartshorne III). The
  **dual completion structure is canonical**, not a choice.

* **Choice (C6) — Cosheaf vs prefactorization vs FA.** CG Vol. I
  §3.1: prefactorization on the Disj operad; FA = Weiss-cosheaf
  prefactorization. **Definitionally canonical** (no choice
  beyond the Disj operad, which itself is canonical).

### §4.2 Canonicity verdict

**W3-W9-10 (canonicity audit).** Of six potential choice points:

| Choice | Canonical? | Reference |
|--------|-----------|-----------|
| C1 Tate envelope | yes (Lurie A.2.6.8) | T3 lines 321–346 |
| C2 Volume datum | yes (Symp-fixed in $\dim_\C=2$) | W2-04 wave-2 |
| C3 Regulator scheme | **inside admissible class only** | W3-W6-04 wave-3 |
| C4 Weight function | **admissible class only** | W3-W6-04 wave-3 |
| C5 Completion structure | yes (residue-duality) | M-29 wave-2 |
| C6 Cosheaf operad | yes (CG Vol. I §3.1) | CG primary |

Four of six: canonical without qualification. Two (C3, C4):
canonical only **inside the admissible class** of regulators
(R-W3-W6-04). The factorization centre is **canonical-up-to-
admissible-class-equivalence**, not pointwise canonical across
all regulator schemes.

**Cross-walk to W3-W6-04 finding.**
W3-W6-04 already names this: "M-26 split is regulator-class-
canonical *inside* the admissible class. Costello-canonicity
*across* regulator schemes is **not** a theorem of M-26."

The Drinfeld lens reinforces this observation by demanding more:
a *truly* canonical (no choices) factorization structure would
require a regulator-independent description, e.g., a chiral
algebra construction directly on the Ran space without analytic
regularization. The manuscript is honest about this: it stays
in the admissible-class equivalence and records R-W3-W6-04 as
the open question.

**W3-W9-11 (factorization centre is canonical at the
stack level, regulator-class-canonical at the analytic level).**
The factorization centre $Z^{P_0}_{\mathrm{fact}}$ is canonical
in the algebraic / stack sense (C1, C2, C5, C6 all canonical) and
canonical-up-to-admissible-class-equivalence at the analytic
level (C3, C4). This is consistent with Drinfeld-canonicity
in the chiral-algebra sense plus a regulator-class layer at the
Costello-RG analytic interface. **No contradiction with the
Drinfeld desideratum**, but the qualification is real.

### §4.3 Heal proposal

**Heal W3-W9-H1 (canonicity acknowledgment in the manuscript).**
In the Theorem C / `thm:open-closed-derived-center-factorization`
preamble, after the statement, add a one-paragraph
canonicity note:

> "The factorization-centre construction is canonical at the
> Tate-algebraic and stack-cohomological levels: the Tate
> envelope is the unique presentable closure (Lurie HA A.2.6.8);
> the volume datum $\Omega = dz_1\wedge dz_2$ is fixed by
> $\mathrm{Symp}_{\mathrm{form}}(\C^2,0)$ in $\dim_\C = 2$; the
> dual completion structure (m-adic on the Matlis side, Tate on
> the brane-line side) is determined by residue-duality
> (Hartshorne, *Residues and Duality*, III.2). At the
> Costello-RG analytic interface the construction is canonical
> within the admissible class of regulators (Definition
> `defn:regulator-admissible-sector`); cross-regulator-class
> canonicity is the open Phase-4 question R-W3-W6-04."

**Inscribed in:** master-ledger §A under M-26 (already mentions
W3-W6-04); cross-link to Theorem C statement; cross-link to
appendix-factorization-current-conventions intro.

---

## §5. Cross-target audit and primary-source citations

### §5.1 Primary-source citation table

| Item | Source | Section |
|------|--------|---------|
| Locally constant FA on $\R^n$ $\simeq E_n$-alg | Lurie *Higher Algebra* (May 2017) | §5.5.4.10 |
| Dunn additivity $E_m\otimes E_n\simeq E_{m+n}$ | Lurie *HA* | §5.5.4.16 |
| Weiss cover definition | Costello-Gwilliam *FA in QFT* Vol. I | §6.5 Def 6.5.0.1 |
| Weiss-cosheaf condition | CG Vol. I | §6.5 Def 6.5.0.5 |
| Cosheaves on manifolds | CG Vol. I | §A.5.4 |
| Locally constant FA on $\R$ $\simeq E_1$-alg | CG Vol. I | §6.4 / Ex 6.4.0.5 |
| Holomorphic factorization, Chern-Simons | CG Vol. II | Ch. 10–11 |
| Holomorphic FAs with defect, §11.4 | CG Vol. II | §11.4 |
| Ran space / chiral algebra | Beilinson-Drinfeld *Chiral Algebras* | §3.4 |
| Chiral-product on $X\times Y$ | BD | §3.4.10–11 |
| Cousin / Serre dual on punctured disk | Hartshorne *Residues and Duality* | III.2 |
| Heat-kernel BV regularization | Costello *RG and EFT* (AMS 2011) | Ch. 5–10 |
| Twisted M-theory + defects (5d) | Costello-Gaiotto-Williams arXiv 2007.09497 | §3–§5 |

### §5.2 Cross-target audit

* **T1** (precise statement of (W-2D)): boxed; M-37 four
  ingredients are the precise decomposition; brane-line piece
  discharged (W3-W2-02–03).
* **T2** (Lurie 5.5.4 / CG verify Weiss-product-stability?):
  **NO**. Neither source closes the residual; W3-W9-04 is the
  precise problem statement.
* **T3** (Drinfeld stack interpretation of bi-infinite parent /
  R-W4-A): the natural stack
  $\mathfrak{M}_{\mathrm{Symp},\C^2,0}$ has all expected
  properties (W3-W9-07); R-W4-A reformulated as
  non-existence of equivariant splitting (W3-W9-08); reinforces
  M-29 (W3-W9-09).
* **T4** (canonicity of factorization construction): four of
  six canonical; two (regulator C3, weight C4) canonical-up-to-
  admissible-class-equivalence; cross-walk to W3-W6-04 confirms
  the qualification (W3-W9-10–11). Heal W3-W9-H1 proposed.

**No fatal attack on stable core.** The W2 Wave-3 split
(brane-line discharged; R²×C² stays open) is verified
unmodified. The M-37 four-ingredient list is the correct
decomposition. The R-W6-Weiss-defect residual stands; it is
sharpened by the Definitions lens into the precise
Weiss-product-stability problem (W3-W9-03–04) and by the
Drinfeld lens into a Beilinson-Drinfeld chiral-algebra
factorization problem on $\mathrm{Ran}(\R^2\times\C^2)$.

---

## §6. Heal proposals (W3-W9 originated)

| ID | Severity | Target | Action |
|----|----------|--------|--------|
| W3-W9-H1 | 2 (canonicity prose) | Theorem C statement / preamble | Add one-paragraph canonicity note distinguishing stack-canonical from regulator-class-canonical, with R-W3-W6-04 cross-link. |
| W3-W9-H2 | 2 (citation precision) | `prop:weiss-cosheaf-residual` (T3 530–562); already-proposed W6-07 sharpening | In the W6-07 sharpened text, expand the citation list to: Lurie HA §5.5.4.16 (Dunn additivity, NOT directly applicable since holomorphic factor is not locally constant); CG Vol. II §11.4 (holomorphic FA + defect, closest analog); BD *Chiral Algebras* §3.4.10–11 (chiral-product descent, partial); Costello *RG and EFT* §10 (heat-kernel). One-sentence note: "*No primary-source theorem closes the residual; a fresh proof of Weiss-product-stability across non-product covers of $\R^2\times\C^2$ is required.*" |
| W3-W9-H3 | 1 (Drinfeld-framing, optional) | `appendix-matlis-principal-parts.tex` after `prop:app-matlis-realization` | Add one-paragraph remark identifying the bi-infinite $\Z^2$-graded parent with a quasi-coherent sheaf on $\mathfrak{M}_{\mathrm{Symp},\C^2,0} = [\mathrm{Spf}\,\C[[z_1,z_2]]\,/\,\mathrm{Symp}_{\mathrm{form}}(\C^2,0)]$, with PBW positive cone and Matlis-coadjoint negative cone exchanged by Hartshorne residue duality III.2. Cite as "Drinfeld stack of formal symplectic disks at a point". |

All three are editorial. W3-W9-H1 sharpens canonicity; W3-W9-H2
sharpens citations in the existing W6-07 heal text; W3-W9-H3
adds Drinfeld-framing of R-W4-A as a stack-cohomological
question.

---

## §7. New residuals (W3-W9 originated)

* **W3-W9-R1 (Weiss-product-stability across non-product
  covers).** Genuinely new, low-medium severity. Lurie HA
  §5.5.4.16 (Dunn additivity) and CG §A.5.6 verify Weiss
  product stability for **product Weiss covers** but not for
  arbitrary Weiss covers of the product. For
  $\R^2\times\C^2$ in the manuscript's mixed
  topological-holomorphic setting, the resolution requires
  M-37 ingredients (I-1)–(I-3); the genuinely beyond-reach
  ingredient is (I-4) (R-W6-Weiss-defect proper). **No primary
  source closes this**; it is the precise statement of the
  open piece. Phase-4 outlook.

* **W3-W9-R2 (Drinfeld stack of formal symplectic disks).**
  The natural stack
  $\mathfrak{M}_{\mathrm{Symp},\C^2,0}$ identified in W3-W9-06
  has not been constructed elsewhere in the manuscript; it
  appears here as an interpretive frame, not as a
  manuscript object. Whether the moduli stack is
  *the* canonical object hosting the bi-infinite parent (as
  opposed to some refinement, e.g., a derived enhancement) is
  open. Editorial / Phase-4 outlook only.

No other new residuals. No invalidation of any existing master-
ledger entry.

---

## §8. Stable core verdict

**Wave-2 stable core preserved unmodified.** The W3-W9
analysis through the Drinfeld + Definitions lens does not
invalidate any item of master ledger §D. The
factorization theorem, the M-29 universal categorical no-go,
the W3-W2 brane-line Weiss discharge, and the M-37
four-ingredient decomposition all remain valid.

**Three new clarifications (additive):**

1. The Weiss condition on $\R^2\times\C^2$ is precisely
   formulated as the boxed (W-2D) (W3-W9-01–04).
2. Lurie HA §5.5.4 / CG Vol. I §6.4 / Vol. II §11.4 / BD §3.4
   *do not* close the residual; W3-W9-03–05 makes the
   citation gap explicit.
3. The Drinfeld stack
   $\mathfrak{M}_{\mathrm{Symp},\C^2,0}$ is the natural
   geometric host for the bi-infinite parent (W3-W9-06–09),
   reinforcing M-29.

**Adjudication on residual disposition.**
* R-W6-Weiss-defect: **unchanged in scope**, sharpened by
  Drinfeld + Definitions analysis. The M-37 four-ingredient
  decomposition stands; (I-4) is the genuinely beyond-reach
  piece. Phase-4 research: chiral-algebra factorization
  technique a la BD §3.4 + Costello *RG and EFT* §10 +
  Costello-Gaiotto-Williams *Twisted M-Theory* §3–§5.
* R-W4-A: **reformulated**, not discharged, as a
  stack-cohomological question (W3-W9-08); Drinfeld lens
  reinforces M-29 (W3-W9-09). Phase-4 outlook.
* R-W3-W6-04 (regulator-class-canonicity): **cross-confirmed**
  by W3-W9-10–11; the manuscript is honest about
  admissible-class canonicity at the analytic level.

---

## §9. Summary

The Drinfeld + Definitions lens applied to the Wave-3 W2
residual (R²×C² Weiss condition, M-37 ingredient 3 — the
bulk-to-defect Weiss kernel) produces:

1. **Precise statement of the residual** (W3-W9-01): the boxed
   (W-2D) is the canonical Drinfeld-style formulation,
   cross-walked against the M-37 four-ingredient decomposition.
2. **Citation audit** (W3-W9-02–05): Lurie HA §5.5.4.16 (Dunn
   additivity) and CG Vol. II §11.4 / BD §3.4.10–11 *do not*
   close Weiss-product-stability for non-product covers; a
   fresh proof is required.
3. **Drinfeld stack interpretation** (W3-W9-06–09): the natural
   stack $\mathfrak{M}_{\mathrm{Symp},\C^2,0}$ has the expected
   smoothness / finite-dim-fibres / pro-algebraic / hidden
   symplectic groupoid structure; it hosts the bi-infinite
   parent of M-29; R-W4-A is reformulated as a non-existence
   of equivariant splitting in $\mathrm{QCoh}$ of the stack.
4. **Canonicity audit** (W3-W9-10–11): four of six choice
   points canonical; two (regulator scheme C3, weight C4)
   canonical-up-to-admissible-class-equivalence per W3-W6-04;
   cross-walk consistent.

**Verdict on R-W6-Weiss-defect.** **Sharpened, not
discharged.** The residual's precise statement is the
boxed (W-2D); its decomposition is the M-37 four ingredients;
its primary-source closure status is open across all of
Lurie HA, CG, BD; its geometric setting is the Drinfeld stack
of formal symplectic disks. Phase-4 research, reachable via
Beilinson-Drinfeld chiral algebra factorization (BD §3.4.10–11)
plus Costello-RG heat-kernel apparatus on the bulk
(Costello *RG and EFT* §10) plus the
Costello-Gaiotto-Williams 5d twisted-M-theory analytic
machinery (CGW arXiv 2007.09497 §3–§5) — explicitly the
working analytic apparatus for codim-5 defects in mixed
holomorphic-topological factorization theories.

**Three editorial heals proposed** (W3-W9-H1 canonicity prose;
W3-W9-H2 citation precision in W6-07 text; W3-W9-H3 Drinfeld
stack remark). **Two new residuals** (W3-W9-R1
Weiss-product-stability open; W3-W9-R2 Drinfeld stack
canonicity, editorial outlook). **No fatal attack** on
Wave-2 stable core.

End of W3 / W9 report.
