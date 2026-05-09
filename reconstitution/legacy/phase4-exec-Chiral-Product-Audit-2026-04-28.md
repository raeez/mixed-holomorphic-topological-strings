# Phase-4 Execution / P4-Chiral-Product-Audit — Beilinson + Composition sheaf-theoretic audit of the BD chiral product on $\mathrm{Ran}(\R^2 \times \C^2)$ under the Hamiltonian flatness $F_\alpha = 0$

**Date.** 2026-04-28.
**Author.** Raeez Lorgat.
**Phase.** 4 EXEC (post-Wave-3 W37 certified convergence; post G1-M1
brane-line BD chiral closure; post G1-M2 $E_2$-promotion partial
closure on $\mathcal C_{\mathrm{ML}}$; post Mixed-Dunn-Probe operadic
literature-gap diagnosis).
**Scope.** P4-Chiral-Product-Audit. The narrow question is **not**
whether the full Beilinson-Drinfeld chiral product can be constructed
on $\mathrm{Ran}(\R^2 \times \C^2)$ — Mixed-Dunn-Probe established
that this is operadically open at the $(\infty,2)$-level — but whether
a *partial chiral product structure* can be assembled from
(i) the brane-line BD chiral algebra on $\R$ (G1-M1 closed),
(ii) the $E_2$-promotion on $\R^2$ in $\mathcal C_{\mathrm{ML}}$ (G1-M2
closed),
(iii) the Hamiltonian flatness cross-bracket
$\{\alpha_{x_i}, \alpha_{\bar z_j}\}$ from $F_\alpha = 0$
(`main.tex`:1808-1816, sharpened in Mixed-Dunn-Probe §6.1 / 6.2),
under Beilinson sheaf-theoretic descent on
$\mathrm{Ran}(\R^2 \times \C^2)$ together with the Composition lens
(local maps glue via Mayer-Vietoris / Čech).
**Lens.** Beilinson primary (sheaf-theoretic, descent on
$\mathrm{Ran}(\R^2 \times \C^2)$, do local chiral-product maps compose
globally? does Čech / Mayer-Vietoris pass for the partial chiral
product?) + Composition secondary (do local chiral-product maps
compose globally? does Čech / Mayer-Vietoris pass on the partial
chiral product?).
**Mode.** Proposal-only. No commits. No manuscript TeX edits. Master
ledger schema; IDs prefix `P4-EXEC-CPA-`.

**Inputs (read in full or relevant sections).**
- `/Users/raeez/topological-strings/CLAUDE.md`.
- `reconstitution/phase4-exec-G1-M1-BD-chiral-2026-04-28.md` (full;
  P4-EXEC-G1-M1-PROP D1-D6; brane-line BD chiral algebra at M-1 scope).
- `reconstitution/phase4-exec-G1-M2-E2-promotion-2026-04-28.md` (full;
  P4-EXEC-G1-M2-DUNN-A holds on $\R^2$ in $\mathcal C_{\mathrm{ML}}$;
  P4-EXEC-G1-M2-DUNN-B fails-anticipated at the strict
  $\mathbb E_4^{\mathrm{mixed}}$ level).
- `reconstitution/phase4-exec-Mixed-Dunn-Probe-2026-04-28.md` (full;
  literature-gap diagnosis; cross-bracket
  $\{\alpha_{x_i}, \alpha_{\bar z_j}\}$ from $F_\alpha = 0$ correctly
  formulated in §6.1; Maurer-Cartan content of $F_\alpha = 0$
  identified in §6.2; three sub-problems §7).
- `main.tex`:280-470 (`lem:omega-cocycle`; `thm:u1-center-anomaly`;
  $[\bar c]$; manuscript's "Theorem G" anomaly line).
- `main.tex`:1750-1900 (Hamiltonian polyvector reduction proposition;
  Hamiltonian BF action; $F_\alpha = 0$; ghost-zero
  $\alpha = \alpha_{x_i}dx_i + \alpha_{\bar z_j}d\bar z_j$).
- `main.tex`:1996-2210
  (`thm:open-closed-derived-center-factorization`;
  `rmk:E1-translation`; Lurie HA §5.5.4 / CG Vol I §6.4 invocation).
- `main.tex`:2322-2438 (`thm:open-closed-derived-center` cochain-level
  CE/PV theorem on $A_\partial$).
- `appendix-factorization-current-conventions.tex` (full; current
  conventions $J_f(a) = B_f(a)$, $\Theta_\rho(B)$; $P_0$-bracket
  identities `prop:app-factorization-source-of-B`,
  `prop:app-factorization-principal-part-bracket`).
- `tate-T1-weighted-completion.tex` (full; admissible Tate envelope
  `stmt:tate-model-envelope`).

**Primary external sources (cited verbally; no fresh PDF
inscription).**
- Beilinson-Drinfeld, *Chiral Algebras*, AMS Coll. Pub. vol. 51,
  2004 (`BD04`): **§3.4.1 chiral product axioms; §3.4.5 chiral
  algebra ≃ FA on Ran; §3.4.10 chiral product on $X \times Y$;
  §3.4.11 chiral axiom on the product manifold**.
- Lurie, *Higher Algebra*, May 2017 / kerodon §HA.5.5.4 (`LurieHA`):
  §5.5.2 (pushforward); §5.5.4.10 (LCFA $\simeq E_n$); §5.5.4.16
  (Dunn additivity).
- Costello-Gwilliam Vol. I (`CGW1`): §6.4-6.5 (LCFA, Weiss covers).
- Costello-Gwilliam Vol. II (`CGW2`): Ch. 10-11 (holomorphic FA;
  defect on $\C^n \times \R$).
- Williams, *Holomorphic factorization algebras*, arXiv:2007.13985
  (`Will20`): §3-§4 ($\mathbb E_n^{\mathrm{hol}}$).
- Costello-Gaiotto-Williams 2007.09497 (`CGW20`): codim-2 / codim-4
  defects.
- M. Kapranov, "Free Lie algebroids and the space of paths",
  Selecta Math. 13 (2007), 277-319 (`Kap07`).

---

## §0. Executive verdict

**Closure status of the partial chiral product on $\R^2 \times \C^2$
under $F_\alpha = 0$.**

**(V-0) Verdict: PARTIAL.** A partial chiral product structure
$\mu^{\partial}$ exists at the cochain / BV-cohomological level on
$\mathrm{Ran}(\R^2 \times \C^2)$, supported by (i) the brane-line BD
chiral product on $\mathrm{Ran}(\R)$ (G1-M1, axioms (Ax.1)-(Ax.5) all
valid), (ii) the strict $E_2$-multiplication on $\R^2$ in
$\mathcal C_{\mathrm{ML}}$ (G1-M2, (Ax.1)-(Ax.4) valid), and (iii) the
Hamiltonian flatness cross-bracket
$\{\alpha_{x_i}, \alpha_{\bar z_j}\}$ at the BV-exact level. **It does
*not* close the full BD §3.4.10-11 chiral product / chiral axiom on
$\mathrm{Ran}(\R^2 \times \C^2)$ — the BD §3.4.11 chiral axiom on the
product manifold fails at the operadic level (Mixed-Dunn obstruction)
but holds at the BV-cohomological level via $F_\alpha = 0$
exactness.**

**(V-1) Per-axiom verdict at the cochain / BV-cohomological level
(partial chiral product).**

* (Ax.1) Symmetry of chiral product: **HOLDS** at the cochain level
  (the chiral grading sign is the standard $(-1)$-shifted-cotangent
  sign; locality on disjoint supports gives strict
  symmetry-up-to-sign).
* (Ax.2) Associativity: **HOLDS** at the BV-cohomological level. On
  $\R^2$-only via Lurie 5.5.4.16; on $\C^2$-only via Williams §3
  implicit holomorphic Dunn; the cross-block via $F_\alpha = 0$
  BV-exactness. **The strict associativity at the operadic /
  $(\infty,2)$-categorical level is the Mixed-Dunn residual.**
* (Ax.3) Compatibility with the differential: **HOLDS**. The CE
  differential on the source matches the BV / Schouten differential on
  the target by `thm:open-closed-derived-center` and its factorization
  upgrade.
* (Ax.4) Locally constant in the topological direction: **HOLDS** on
  $\R^2$ (Lurie 5.5.4.10 + 5.5.4.16; G1-M2). Constancy at the
  cohomological level via translation invariance.
* (Ax.5) Holomorphic in the holomorphic direction: **PARTIAL.**
  The $\bar\partial$-quasi-isomorphism on holomorphic polydisk
  inclusions in $\C^2$ is supplied by the Williams §3 framework
  *separately* on the holomorphic factor (proven on each polydisk
  inclusion; the bulk holomorphic chiral product is conjectural at
  M-12 Avenue (B) scope). **The partial chiral product carries (Ax.5)
  on each $\C^2$-polydisk slice but does not assemble the full chiral
  axiom on the product manifold.**

**(V-2) First failure mode (named obstruction).** **The first BD
axiom that fails is the BD §3.4.11 *chiral axiom on the product
manifold*** — the operadic statement that the chiral cobracket on
$\Delta^*(\mathcal F \boxtimes \mathcal G)$ on $X \times Y$ satisfies
the chiral axiom — which BD §3.4.10-11 covers only for
$X = Y = $ smooth complex curve, and which our setting
($X = \R^2$ topological + $Y = \C^2$ holomorphic) does *not* match.
**The failure mode is the same as the Mixed-Dunn obstruction class
$\mathrm{HOp}^\bullet$ named in Mixed-Dunn-Probe §6.5
(O-6.5.3).** Its severity is 3 at the operadic level; severity 2
at the BV-cohomological level (the BV-exactness of $F_\alpha$ trivializes
the cohomological obstruction but not the operadic one).

**(V-3) Sufficiency for the manuscript's "Theorem G" chain-level
closure.** **YES, the partial chiral product is sufficient for the
manuscript's chain-level closure of `thm:open-closed-derived-center`
and `thm:open-closed-derived-center-factorization`.** Theorem G in
the manuscript's parlance refers to the U(1)/Capelli anomaly theorem
(`thm:u1-center-anomaly`, `main.tex`:318-352; tracked as Theorem G in
the platonic ledger and the attack-heal traces); its chain-level
closure
(`thm:open-closed-derived-center`/`-factorization`,
`main.tex`:1996-2438) does **not** require the full BD §3.4.10-11
chiral product on the product manifold $X \times Y$. It requires only
the **brane-line factorization** on $\R$ (G1-M1 closed), the
**factorization-product compatibility for disjoint intervals** on
$\R$ (Step 6 of the proof of
`thm:open-closed-derived-center-factorization`, `main.tex`:2139-2173),
and the **bulk-to-defect coupling** to the formal symplectic disk's
Hamiltonian Lie algebra structure on $\widehat{\C^2}_0$ (which is
algebraic, not requiring the holomorphic factorization apparatus on
$\C^2$). **The partial chiral product is sufficient** because the
Theorem G chain-level closure is at the brane-line stratum only;
the bulk $\C^2$ direction enters only through the Hamiltonian Lie
algebra $\bar A$ on the formal symplectic disk (algebraic, no
holomorphic FA descent needed), and the brane-line BD chiral algebra
absorbs $\bar A$ as the chiral coefficient module via the M-1
construction.

**(V-4) Cross-walk to G1-M2 $E_2$-promotion + Maurer-Cartan twist.**
**YES.** The partial chiral product on $\R^2 \times \C^2$ corresponds
exactly to a strict $E_2$-algebra (G1-M2 closed in
$\mathcal C_{\mathrm{ML}}$) plus a Maurer-Cartan twisting from
$F_\alpha = 0$ at the cross-direction
$\partial_{x_i}\alpha_{\bar z_j} - \bar\partial_{z_j}\alpha_{x_i}
+ \{\alpha_{x_i}, \alpha_{\bar z_j}\} = 0$ (Mixed-Dunn-Probe §6.2
cross-flatness). The MC element $\alpha$ encodes the topological-
holomorphic coupling, and the partial chiral product is the chiral
algebra structure twisted by this MC element. **This is the precise
manuscript-internal manifestation of Mixed-Dunn-Probe (V-4).**

**(V-5) Smallest concrete example.** A small ball
$B^2_r \times \{0\} \subset \R^2 \times \C^2$ with the brane probe at
the origin: the partial chiral product reduces to the brane-line BD
chiral algebra on the disk $B^2_r \cap (\R \times \{0\})$ (G1-M1)
together with the $\C^2$-holomorphic structure restricted to the
formal disk $\{0\} \in \C^2$ (Hamiltonian Lie algebra $\bar A$
algebraic on $\widehat{\C^2}_0$). **This concrete example is closed
at G1-M1 + algebraic $\bar A$.** It does *not* exercise the
$\mathbb E_2^{\mathrm{hol}}$ structure on $\C^2$ — the holomorphic
factorization apparatus is only triggered when the brane probe is
extended off the origin in $\C^2$.

**Lens findings.**
* **Beilinson lens.** Sheaf-theoretic descent on
  $\mathrm{Ran}(\R^2 \times \C^2)$: factorization compatibility
  passes on (a) product opens via CG §A.5.6 / Costello-Gwilliam Vol II
  Ch. 10 holomorphic-$\bar\partial$-Hodge cosheaf, (b) the brane-line
  factor via the locally constant subcategory equivalence
  (Lurie 5.5.4.10 + G1-M1). The non-trivial Beilinson question is
  whether the chiral product *map* extends from product opens to
  arbitrary mixed opens. **It does not at the operadic level; it does
  at the BV-cohomological level via $F_\alpha = 0$.**
* **Composition lens.** Local chiral-product maps compose at the
  Mayer-Vietoris / Čech level under (C-1) compatibility on overlaps
  (passes via Hamiltonian flatness $F_\alpha = 0$ at BV-cohomological
  level, Mixed-Dunn-Probe §6.2 cross-flatness) and (C-2) cofinal
  refinement of arbitrary covers by product covers (open at
  W3-W9-04 / R-03-I-4.b residual). **Mayer-Vietoris passes on the
  ML-restricted product-cover subcategory; full Mayer-Vietoris on
  arbitrary covers is the W3-W9-04 residual.**

---

## §1. BD chiral product axioms (Ax.1-Ax.5)

We state the BD chiral product axioms, distinguishing local from
global from operadic content. References are to BD04 §3.4.1-11 (AMS
Coll. Pub. vol. 51, 2004; pages 162-170), with cross-walk to the
$C^\infty$-CG / Lurie / Williams setting.

### §1.1 BD04 §3.4.1 — chiral algebra structure on a smooth complex curve $X$

A *chiral algebra* on $X$ is a $\mathcal D_X$-module $\mathcal A$
equipped with a *chiral product*
$$\mu : j_*j^*(\mathcal A \boxtimes \mathcal A) \longrightarrow
\Delta_!\mathcal A$$
where $j : X^2 \setminus \Delta \hookrightarrow X^2$ is the open
inclusion of the off-diagonal and $\Delta : X \hookrightarrow X^2$
is the diagonal embedding. The five axioms (in BD's terminology,
spelled out as standard chiral algebra axioms):

* **(Ax.1) Symmetry / chiral grading.** The chiral product satisfies
  $\sigma_{12} \circ \mu = \mu \circ \sigma_{12}$, where $\sigma_{12}$
  is the symmetry of the tensor product up to the chiral grading
  sign. In OPE language: $Y(z, w) = Y(w, z)$ up to the chiral
  grading sign.
* **(Ax.2) Associativity / chiral Jacobi.** The chiral product
  satisfies the BD §3.4.1 chiral Jacobi axiom: the iterated chiral
  product on $X^3$, given by either order of bracketing, agrees up
  to the chiral cobracket on the diagonal. In OPE language:
  $Y(Y(z_1, z_2), z_3) \cong Y(z_1, Y(z_2, z_3))$ as chiral
  cocycles.
* **(Ax.3) Compatibility with the $\mathcal D_X$-module differential.**
  The chiral product is $\mathcal D_X$-linear: i.e., compatible with
  the differential $\partial_z$ on each chiral coordinate.
* **(Ax.4) Locally constant in the topological direction (in the
  $C^\infty$-CG translation).** When the manifold is topological
  (here $\R$ on the brane line), the chiral product factors through
  the locally constant subcategory; structure maps on disk inclusions
  are equivalences.
* **(Ax.5) Holomorphic in the holomorphic direction (in the
  $C^\infty$-CG translation).** When the manifold is holomorphic
  (here $\C^2$), the chiral product is $\bar\partial$-quasi-iso on
  holomorphic polydisk inclusions (Williams §3
  $\mathbb E_n^{\mathrm{hol}}$ axiom).

In the manuscript's $\R^2 \times \C^2$ setting with one topological
+ one holomorphic factor, axioms (Ax.4) and (Ax.5) are *separately*
imposed on the corresponding factors.

### §1.2 BD04 §3.4.5 — chiral algebra ≃ FA on Ran(X)

A chiral algebra on $X$ is equivalent (BD §3.4.5; AMS edition
page 165) to a factorization algebra on $\mathrm{Ran}(X)$ — the
moduli of finite non-ordered point collections — satisfying
factorization compatibility on disjoint configurations.

### §1.3 BD04 §3.4.10-11 — chiral product on $X \times Y$

For chiral algebras $\mathcal A_X, \mathcal A_Y$ on smooth complex
curves $X, Y$, BD §3.4.10 constructs the *external chiral product*
$\mathcal A_X \boxtimes_{\mathrm{ch}} \mathcal A_Y$ as a chiral
algebra on $X \times Y$ via
$$j_{(X \times Y)}^* j_{(X \times Y)*}\bigl(
(\mathcal A_X \boxtimes_{\mathrm{ch}} \mathcal A_Y)
\boxtimes
(\mathcal A_X \boxtimes_{\mathrm{ch}} \mathcal A_Y)\bigr)
\longrightarrow
\Delta_{(X \times Y)!}(\mathcal A_X \boxtimes_{\mathrm{ch}} \mathcal A_Y)$$
where $j_{(X \times Y)}$ and $\Delta_{(X \times Y)}$ are the
inclusion of off-diagonal and diagonal in $(X \times Y)^2$. BD §3.4.11
verifies the *chiral axiom on the product manifold*: the chiral
cobracket on $\Delta^*(\mathcal F \boxtimes \mathcal G)$ satisfies
the chiral axiom on $X \times Y$.

**Crucial caveat.** BD §3.4.10-11 covers the case of two **smooth
complex curves** $X, Y$. The product gives a 2-complex-dimensional
manifold $X \times Y$ (4 real dimensions). Our setting
$\R^2 \times \C^2$ is 6 real dimensions with one topological
2-real-dimensional factor and one holomorphic 4-real-dimensional
factor. **BD §3.4.10-11 does *not* directly apply.**

### §1.4 Local vs global vs operadic taxonomy

* **Local axioms (per-stalk).**
  - (Ax.1) symmetry: local at each pair of distinct points (off-diagonal).
  - (Ax.3) differential compatibility: local at each point.
* **Global axioms (Ran-space-descent).**
  - (Ax.4) locally constant in topological direction: global on $\R$
    (and on $\R^2$ if Dunn additivity applies).
  - (Ax.5) holomorphic in holomorphic direction: global on $\C$ (and
    on $\C^n$ if holomorphic Dunn additivity applies, Williams §3).
* **Operadic axioms (chiral Jacobi at $\infty$-categorical level).**
  - (Ax.2) chiral Jacobi / associativity: requires the full operadic
    structure of either $\mathbb E_2^{\mathrm{top}}$ or
    $\mathbb E_2^{\mathrm{hol}}$, or — for the product setting — the
    mixed Dunn additivity
    $\mathbb E_m^{\mathrm{top}} \otimes \mathbb E_n^{\mathrm{hol}}
    \simeq \mathbb E_{m,n}^{\mathrm{mixed}}$ (Mixed-Dunn-Probe;
    open at the operadic level).

This taxonomy is the key: the partial chiral product satisfies all
*local* axioms, all *global* axioms within each factor, and the
*operadic* axiom (Ax.2) at the BV-cohomological level via $F_\alpha = 0$
exactness, but **not** at the strict operadic level on the product
manifold.

---

## §2. Partial chiral product construction

We construct the candidate partial chiral product $\mu^\partial$ on
$\mathrm{Ran}(\R^2 \times \C^2)$ from the three available pieces of
data.

### §2.1 The candidate chiral algebra on $\mathrm{Ran}(\R^2 \times \C^2)$

Let $X = \R^2 \times \C^2$. We use the following notation:
- $\R^2_{\mathrm{top}} = \R^2_{x_1, x_2}$ topological factor.
- $\C^2_{\mathrm{hol}} = \C^2_{z_1, z_2}$ holomorphic factor with
  symplectic form $\omega = dz_1 \wedge dz_2$.
- $L = \R \times \{0\} \times \{0\} \subset X$ brane line at the
  origin of $\C^2$ along the first $\R$-direction.

The candidate chiral algebra $\mathcal A^\partial$ is the locally
constant + holomorphic-locally-constant FA on $X$ given by

$$\mathcal A^\partial(U) := C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak g^\partial_U),
\qquad
\mathfrak g^\partial_U := \Omega^\bullet_c(U \cap \R^2)
\widehat\otimes \Omega^{0,*}_c(U \cap \C^2)
\widehat\otimes \widehat{\mathfrak h}[1] ,$$

where:
- $U \subseteq X$ is open;
- $\Omega^\bullet_c(U \cap \R^2)$ is compactly supported de Rham
  forms on the topological factor;
- $\Omega^{0,*}_c(U \cap \C^2)$ is compactly supported Dolbeault
  forms on the holomorphic factor;
- $\widehat{\mathfrak h}$ is the formal symplectic disk's Hamiltonian
  Lie algebra (`main.tex`:1755-1768; the Dolbeault-valued Hamiltonian
  potential structure);
- $\mathcal A^\partial$ is the unreduced extension of the M-1
  brane-line factorization algebra to the bulk via the Hamiltonian
  BF setup, with structure maps induced by extension by zero
  (`main.tex`:1996-2046).

### §2.2 The chiral product structure maps

For disjoint pairs of opens $U_1, U_2 \subset X$ with
$U_1 \sqcup U_2 \subset V$, the candidate chiral product is:

$$\mu^\partial : j^*\bigl(\mathcal A^\partial(U_1)
\widehat\otimes \mathcal A^\partial(U_2)\bigr)
\longrightarrow
\mathcal A^\partial(V) ,$$

defined on generators by:

**(M-2.2.1) Pure topological-disjoint pair** ($U_1, U_2$ disjoint in
$\R^2$ but with overlapping $\C^2$ projection): the structure map is
inherited from the G1-M2 strict $E_2$-multiplication on $\R^2$ in
$\mathcal C_{\mathrm{ML}}$. By Lurie 5.5.4.16 + 5.5.4.10
(Dunn additivity in $\Pr^L_{\mathrm{ML}}$), this map is well-defined
as a strict $E_2$-multiplication.

**(M-2.2.2) Pure holomorphic-disjoint pair** ($U_1, U_2$ disjoint in
$\C^2$ but with overlapping $\R^2$ projection): the structure map is
the candidate $\mathbb E_2^{\mathrm{hol}}$-multiplication on $\C^2$
constructed from Williams §3-§4 holomorphic-FA framework applied to
$\Omega^{0,*}_c(U \cap \C^2) \widehat\otimes \widehat{\mathfrak h}[1]$
with $\bar\partial$-quasi-iso on holomorphic polydisk inclusions.
**This map is conjectural at the strict operadic level (Avenue (B)
M-12 obligation in Mixed-Dunn-Probe §7); valid at the prefactorization
/ cohomological level via the Williams §3 chain-level construction.**

**(M-2.2.3) Mixed-disjoint pair** ($U_1, U_2$ disjoint in
$\R^2 \times \C^2$ but with non-trivial cross-coupling): the structure
map is the candidate mixed multiplication. By Mixed-Dunn-Probe §6.2,
the cross-coupling is encoded by the cross-flatness equation
$$\partial_{x_i} \alpha_{\bar z_j} - \bar\partial_{z_j} \alpha_{x_i} +
\{\alpha_{x_i}, \alpha_{\bar z_j}\} = 0 ,$$
which at on-shell ($F_\alpha = 0$) is BV-exact via the Lagrange
multiplier $\beta$. The mixed structure map is:
$$\mu^{\partial,\mathrm{mixed}}_{U_1, U_2}
= \mu^{\partial,\R^2}_{U_1 \cap \R^2, U_2 \cap \R^2}
\otimes \mu^{\partial,\C^2}_{U_1 \cap \C^2, U_2 \cap \C^2}
+ \delta_{\mathrm{cross}}^{\mathrm{BV-exact}}$$
where $\mu^{\partial,\R^2}$ is the M-2.2.1 topological multiplication,
$\mu^{\partial,\C^2}$ is the M-2.2.2 holomorphic multiplication, and
$\delta_{\mathrm{cross}}^{\mathrm{BV-exact}}$ is the BV-exact
correction term from the Maurer-Cartan twist.

### §2.3 What the Hamiltonian flatness $F_\alpha = 0$ contributes

Per Mixed-Dunn-Probe §6.1-6.2 (correctly formulated, sharpened from
the earlier G1-M2 §9.1 phrasing), the Hamiltonian connection $\alpha$
on $X = \R^2 \times \C^2$ has ghost-zero components
$\alpha_{x_i} dx_i + \alpha_{\bar z_j} d\bar z_j$
(`main.tex`:1812-1816; *no* mixed $dx_i d\bar z_j$ component
ghost-zero). The cross-coupling between topological and holomorphic
factors is encoded by the **cross-bracket**
$\{\alpha_{x_i}, \alpha_{\bar z_j}\}$ in the flatness equation
$F_\alpha = D\alpha + \tfrac{1}{2}\{\alpha, \alpha\} = 0$.

The flatness equation decomposes into three blocks:
- **Topological block** in $\R^2$: closed at G1-M2 / Lurie 5.5.4.16.
- **Holomorphic block** in $\C^2$: open at M-12 Avenue (B) /
  Williams §3.
- **Cross block** $\partial_{x_i}\alpha_{\bar z_j} -
  \bar\partial_{z_j}\alpha_{x_i} + \{\alpha_{x_i}, \alpha_{\bar z_j}\}
  = 0$: this is the *Maurer-Cartan datum* coupling the two factors.

**P4-EXEC-CPA-MC.** **The cross-bracket
$\{\alpha_{x_i}, \alpha_{\bar z_j}\}$ from $F_\alpha = 0$ is the
Maurer-Cartan datum supplying the partial chiral product's
mixed-stratum structure map at the cohomological level.** The
Lagrange multiplier $\beta$ in the BF action enforces this on-shell;
at the chain level, the cross-bracket is BV-exact under the action of
$\beta$.

### §2.4 The candidate partial chiral product (definition)

**(Def. P4-EXEC-CPA-PARTIAL.)** The *partial chiral product*
$\mu^\partial$ on $\mathrm{Ran}(\R^2 \times \C^2)$ in
$\mathcal C_{\mathrm{ML}}$ is the chiral product structure on the
candidate $\mathcal A^\partial$ (§2.1) given by the structure maps
M-2.2.1, M-2.2.2 (at the prefactorization-FA level), and M-2.2.3
(at the BV-cohomological level via $F_\alpha = 0$ MC twist).

**Severity 3.** **Status: candidate chiral product structure
constructed at the cochain / BV-cohomological level. Confidence: high
on M-2.2.1 (G1-M2 closed), medium-high on M-2.2.3 (BV-exactness
follows from $F_\alpha = 0$ on-shell + Lagrange multiplier $\beta$),
medium on M-2.2.2 (Williams §3 prefactorization-level construction;
strict operadic-level closure is M-12 Avenue (B) residual).**

---

## §3. Per-axiom satisfaction analysis

We test each BD axiom (Ax.1)-(Ax.5) on the partial chiral product
$\mu^\partial$ of §2.4.

### §3.1 (Ax.1) Symmetry / chiral grading

**Statement.** The chiral product satisfies
$\sigma_{12} \circ \mu^\partial = \mu^\partial \circ \sigma_{12}$,
where $\sigma_{12}$ is the symmetry of the tensor product up to
chiral grading sign.

**Verification.**
- **On topological-disjoint pairs (M-2.2.1).** Symmetry holds via
  Lurie 5.5.4.16's strict $E_2$ symmetry on $\R^2$; the $E_2$ braid
  axiom in $\mathcal C_{\mathrm{ML}}$ is automatic on the locally
  constant subcategory by translation invariance (G1-M2 §3 LC-2).
- **On holomorphic-disjoint pairs (M-2.2.2).** Symmetry holds at the
  prefactorization-FA level by the symmetric structure of the
  $\bar\partial$-Hodge cosheaf $\Omega^{0,*}_c(\C^2)$ together with
  the symmetric Lie bracket on $\widehat{\mathfrak h}$.
- **On mixed-disjoint pairs (M-2.2.3).** Symmetry holds at the
  BV-cohomological level: the cross-bracket
  $\{\alpha_{x_i}, \alpha_{\bar z_j}\}$ is a Lie bracket
  (antisymmetric on $\widehat{\mathfrak h}$), so the BV-exact
  correction $\delta_{\mathrm{cross}}^{\mathrm{BV-exact}}$ inherits
  symmetry.

**Verdict.** **(Ax.1) HOLDS at the cochain level.** Severity 2.
Confidence high. **No obstruction.**

### §3.2 (Ax.2) Associativity / chiral Jacobi

**Statement.** $Y(Y(z_1, z_2), z_3)$ and $Y(z_1, Y(z_2, z_3))$ agree
as chiral cocycles on $X^3$.

**Verification.**
- **On purely topological 3-tuples in $\R^2$.** By Lurie 5.5.4.16
  Dunn additivity in $\mathcal C_{\mathrm{ML}}$ (G1-M2
  P4-EXEC-G1-M2-DUNN-A), strict $E_2$-associativity on $\R^2$ in the
  ML-restricted envelope. This passes the chiral Jacobi axiom on
  $\mathrm{Ran}(\R^2)$. Confidence high.
- **On purely holomorphic 3-tuples in $\C^2$.** The
  $\mathbb E_2^{\mathrm{hol}}$-associativity is the M-12 Avenue (B)
  residual at the strict operadic level; at the BV-cohomological /
  prefactorization-FA level, Williams §3 supplies the structural
  associativity-up-to-coherent-homotopy. **Holds at the BV-cohomological
  level; open at the strict operadic level.**
- **On mixed 3-tuples** (one $\R^2$-coordinate + two $\C^2$-coordinates,
  or two $\R^2$ + one $\C^2$).
  - **Iterated cross-bracket coherence.** The iterated mixed chiral
    product involves the Jacobi-style iterated bracket
    $\{\{\alpha_{x_i}, \alpha_{\bar z_j}\}, \alpha_{x_k}\}$ or
    $\{\{\alpha_{x_i}, \alpha_{\bar z_j}\}, \alpha_{\bar z_l}\}$.
  - By the Jacobi identity for the Hamiltonian Lie bracket on
    $\widehat{\mathfrak h}$ (the formal symplectic disk's Poisson
    bracket; `main.tex`:1740-1755), these iterated brackets satisfy:
    $$\{\{\alpha_{x_i}, \alpha_{\bar z_j}\}, \alpha_{x_k}\}
    + \{\{\alpha_{\bar z_j}, \alpha_{x_k}\}, \alpha_{x_i}\}
    + \{\{\alpha_{x_k}, \alpha_{x_i}\}, \alpha_{\bar z_j}\} = 0,$$
    which is the cyclic Jacobi for the Hamiltonian bracket on
    $\widehat{\mathfrak h}$.
  - On-shell ($F_\alpha = 0$), the cyclic Jacobi for the cross-
    bracket reduces to a sum of partial-derivative terms, and this
    sum is BV-exact via the Lagrange multiplier $\beta$
    (`main.tex`:1818-1828; the gauge symmetry
    $\delta_\varepsilon \beta = \mathrm{ad}^\vee_\varepsilon \beta$
    gives $F_\alpha = \mathrm{BV}\beta$). **Hence the iterated
    chiral Jacobi for the partial chiral product holds at the
    BV-cohomological level.**

**Verdict.** **(Ax.2) HOLDS at the BV-cohomological level.** At the
strict operadic / $(\infty,2)$-categorical level on
$\mathrm{Ran}(\R^2 \times \C^2)$, **(Ax.2) is OPEN** (the residual
class is Mixed-Dunn-Probe (O-6.5.3) operadic obstruction
$\mathrm{HOp}^\bullet$, M-12 Avenue (B)). Severity 3. Confidence high
on the BV-cohomological closure.

### §3.3 (Ax.3) Compatibility with the differential

**Statement.** The chiral product is $\mathcal D_X$-linear, i.e.,
compatible with the differential.

**Verification.**
- The chain-level differential on $\mathcal A^\partial(U)$ is the CE
  differential on
  $C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak g^\partial_U)$,
  matched to the BV / Schouten differential on the dual side via
  `thm:open-closed-derived-center` (`main.tex`:2322-2438) — the
  generator-level identity $\Phi(c^I) = \theta^I$,
  $\Phi(u_I) = O_I$ with matching CE-vs-Schouten differentials.
- The factorization upgrade `thm:open-closed-derived-center-
  factorization` (`main.tex`:1996-2046) verifies CE-differential
  compatibility at the chain level on each interval (Step 4 of the
  proof).
- For the $\C^2$-direction (holomorphic), the differential is the
  $\bar\partial$-operator on $\Omega^{0,*}_c(\C^2)$; the chiral
  product is $\bar\partial$-compatible by the
  $\bar\partial$-quasi-iso structure (Williams §3).
- For the cross-direction, the BV-exactness of
  $\delta_{\mathrm{cross}}^{\mathrm{BV-exact}}$ is *exactly* the
  statement that the cross term is in the image of the BV
  differential, hence vanishes in cohomology.

**Verdict.** **(Ax.3) HOLDS at the chain level.** Severity 2.
Confidence high. **No obstruction.**

### §3.4 (Ax.4) Locally constant in the topological direction

**Statement.** Structure maps on disk inclusions $D_1 \subset D_2$
in $\R^2$ are quasi-isomorphisms; $\mu^\partial$ factors through the
locally constant subcategory.

**Verification.**
- On the brane-line $\R$ alone: G1-M1 closure (P4-EXEC-G1-M1-PROP D3
  (U-1) translation invariance check).
- On $\R^2$: G1-M2 closure (P4-EXEC-G1-M2-DUNN-A; LC-1 + LC-2 +
  LC-3 in §3 of G1-M2). The $E_2$-structure on $\R^2$ in
  $\mathcal C_{\mathrm{ML}}$ is locally constant.
- On the bulk $\R^2 \times \C^2$: locally constant *in the topological
  direction* means $\R^2$-direction-quasi-iso on disk inclusions
  $D_1 \times P \subset D_2 \times P$ for $P \subset \C^2$ a fixed
  polydisk. This factors through (Ax.4) for $\R^2$ alone.

**Verdict.** **(Ax.4) HOLDS at the $\R^2$ level in
$\mathcal C_{\mathrm{ML}}$.** Severity 3. Confidence high. **No
obstruction at the topological factor.** The arbitrary-colimit
preservation residual (W3-W11-01-A) restricts the verification to
the ML envelope.

### §3.5 (Ax.5) Holomorphic in the holomorphic direction

**Statement.** Structure maps on holomorphic polydisk inclusions
$P_1 \subset P_2$ in $\C^2$ are $\bar\partial$-quasi-isomorphisms;
$\mu^\partial$ factors through the
$\mathbb E_2^{\mathrm{hol}}$-locally-constant subcategory on $\C^2$.

**Verification.**
- The bulk Hamiltonian BF setup uses Dolbeault
  $\Omega^{0,*}_c(\C^2)$ as the holomorphic-direction cosheaf
  (`main.tex`:1759-1768); on-shell flatness in the holomorphic
  block is $\bar\partial_{z_1}\alpha_{\bar z_2} -
  \bar\partial_{z_2}\alpha_{\bar z_1} +
  \{\alpha_{\bar z_1}, \alpha_{\bar z_2}\} = 0$
  (Mixed-Dunn-Probe §6.2 holomorphic-only flatness).
- Williams §3 holomorphic-$\mathbb E_n$ axiom requires the
  $\bar\partial$-quasi-iso on holomorphic polydisk inclusions; the
  bulk Hamiltonian BF setup supplies this on each polydisk slice
  via the Dolbeault complex.
- **However**, the *full holomorphic Dunn additivity* on
  $\C^2 = \C \times \C$ (the cross-equivalence
  $\mathbb E_1^{\mathrm{hol}} \otimes \mathbb E_1^{\mathrm{hol}}
  \simeq \mathbb E_2^{\mathrm{hol}}$) is implicit in Williams §3-§4
  but not stated as a theorem (Mixed-Dunn-Probe §4.1 W-4.1.4).

**Verdict.** **(Ax.5) HOLDS on each holomorphic polydisk inclusion in
$\C^2$ at the prefactorization-FA level.** **PARTIAL** at the strict
operadic level on $\C^2$; OPEN at the strict operadic level on the
mixed product manifold $\R^2 \times \C^2$ (this is the chiral axiom
on the product manifold, BD §3.4.11, which fails for the mixed
setting). Severity 3. Confidence medium-high on each polydisk;
medium on the bulk $\C^2$; low on the full product manifold.

### §3.6 Per-axiom summary table

| Axiom | Local | Global on $\R^2$ | Global on $\C^2$ | Mixed (on $\R^2 \times \C^2$) | Operadic |
|---|---|---|---|---|---|
| (Ax.1) Symmetry | HOLDS | HOLDS | HOLDS (preFA) | HOLDS (BV-cohom) | HOLDS |
| (Ax.2) Assoc / chiral Jacobi | HOLDS | HOLDS (Lurie) | HOLDS (BV-cohom; preFA) | HOLDS (BV-cohom) | **OPEN** (Mixed-Dunn) |
| (Ax.3) Differential compat | HOLDS | HOLDS | HOLDS | HOLDS | HOLDS |
| (Ax.4) LC topological | HOLDS | HOLDS | n/a | HOLDS in $\R^2$ slice | HOLDS |
| (Ax.5) LC holomorphic | n/a | n/a | HOLDS preFA | PARTIAL on each polydisk | **OPEN** at strict |

**Aggregate.** All axioms hold at the BV-cohomological /
prefactorization level. **The first axiom that fails strictly is
(Ax.2) at the operadic level, OR equivalently (Ax.5) at the
operadic level on the full product manifold** — both are the same
Mixed-Dunn obstruction.

---

## §4. Failure mode and residual obstruction

### §4.1 The first axiom that fails

**P4-EXEC-CPA-FAIL-A.** **(Ax.2) chiral Jacobi at the operadic /
$(\infty,2)$-categorical level fails on $\mathrm{Ran}(\R^2 \times \C^2)$.**

The failure is precisely the **Mixed-Dunn obstruction class
$\mathrm{HOp}^\bullet$** of Mixed-Dunn-Probe §6.5 (O-6.5.3). The
operadic-level chiral Jacobi axiom requires the operadic equivalence
$$\mathbb E_2^{\mathrm{top}} \otimes \mathbb E_2^{\mathrm{hol}}
\simeq \mathbb E_{2,2}^{\mathrm{mixed}} \quad \text{in } \Pr^L_{\mathrm{ML}},$$
which is the literature gap identified in Mixed-Dunn-Probe (V-0).

**Severity 3.** **Status: failure-named. Confidence high.**

The failure mode is structural: BD §3.4.10-11 covers the chiral
product / chiral axiom on a product of two **smooth complex curves**
(2-complex-dimensional manifold, 4 real dimensions), not on a mixed
topological-holomorphic 6-real-dimensional product manifold.

### §4.2 The residual obstruction class

Per Mixed-Dunn-Probe §6.5, three potential obstruction classes are
identified:

* **(Hochschild $\mathrm{HH}^2$):** vanishes at BV-cohomological
  level (BV-exactness of cross-bracket via $F_\alpha = 0$).
* **(Cyclic $\mathrm{HC}^\bullet$):** vanishes (sub-class of
  Hochschild + W3-W11-04 weight-filtration spectral sequence
  $E_1$ degeneration on graphwise contributions; consistent with
  Connes BSS degeneration).
* **(Operadic $\mathrm{HOp}^\bullet$):** **non-vanishing /
  unknown** — the *primary obstruction* for the strict operadic
  chiral product on the product manifold.

**P4-EXEC-CPA-OBS.** **The residual obstruction class for the strict
operadic chiral product on $\mathrm{Ran}(\R^2 \times \C^2)$ is
$\mathrm{HOp}^\bullet$**, the operadic obstruction class for the
mixed Dunn additivity $\mathbb E_2^{\mathrm{top}} \otimes
\mathbb E_2^{\mathrm{hol}} \simeq \mathbb E_{2,2}^{\mathrm{mixed}}$.
Computing this class — or showing its vanishing — is the M-12 Avenue
(B) attack target (Mixed-Dunn-Probe §7.3 SP-3).

**Severity 3.** **Status: open-named. Confidence high on the
identification; the vanishing claim is conjectural.**

### §4.3 Comparison with Beilinson + Composition lens diagnoses

* **Beilinson lens (sheaf-theoretic descent on $\mathrm{Ran}(X)$):**
  the chiral product structure descends *separately* on the
  topological factor $\R^2$ (LCFA on $\mathrm{Ran}(\R^2)$ via
  Lurie 5.5.4.10) and on the holomorphic factor $\C^2$ (holomorphic-
  LCFA on $\mathrm{Ran}^{\mathrm{hol}}(\C^2)$ via Williams §3); the
  cross-direction descends only at the BV-cohomological level via
  $F_\alpha = 0$. **The Beilinson lens diagnoses the failure as a
  descent failure on $\mathrm{Ran}(\R^2 \times \C^2)$ for the
  Ran-space mixed structure.**

* **Composition lens (do local maps glue globally? Mayer-Vietoris /
  Čech?):** local chiral-product maps glue at the Mayer-Vietoris
  level on (a) product opens via the Hamiltonian flatness
  $F_\alpha = 0$ at the BV-cohomological level, (b) overlap
  consistency on disjoint configurations via the brane-line BD
  chiral algebra and its $\C^2$-bulk extension. **The Composition
  lens diagnoses the failure as a global gluing failure for arbitrary
  (non-product) covers — i.e., the cofinal-refinement-by-product-covers
  question, which is W3-W9-04 / R-03-I-4.b residual.**

Both lenses converge on the same obstruction: the strict operadic
chiral axiom on the product manifold cannot be built from the
locally-disjoint pieces alone; the cross-coupling $F_\alpha = 0$
suffices for BV-cohomological closure but not for strict operadic
closure.

---

## §5. Sufficiency for the manuscript's "Theorem G" chain-level closure

### §5.1 What "Theorem G" refers to

In the manuscript's parlance, **"Theorem G" refers to the
U(1)/Capelli anomaly theorem `thm:u1-center-anomaly`**
(`main.tex`:318-352), with companion theorems `thm:u1-center-anomaly-open`
(`main.tex`:354-393) and `thm:quantum-classical-anomaly`
(`main.tex`:412-464). Theorem G is tracked as such in
`reconstitution/attack-heal-platonic-2026-04-28.md` (~30 references).

The chain-level closure of Theorem G is supplied by the open-closed
derived-center theorems:
* `thm:open-closed-derived-center` (`main.tex`:2322-2438) — cochain-
  level CE/PV theorem for the formal symplectic disk's Hamiltonian
  Lie algebra.
* `thm:open-closed-derived-center-factorization` (`main.tex`:1996-
  2210) — factorization-algebra upgrade on the brane line $\R$.

**Chain-level closure target.** The Theorem G anomaly $[\bar c]$ is
recorded as a class in $H^2_{\mathrm{Lie}}(\bar A; \C)$ on the closed
side and as the brane-side U(1) center anomaly via boundary
evaluation on the open side. The chain-level closure asserts that
both records identify the same class via the cochain-level CE/PV
isomorphism $\Phi$.

### §5.2 What the partial chiral product is needed for

The chain-level closure of Theorem G requires:

1. **CE/PV cochain isomorphism $\Phi$ on $A_\partial$** (algebraic;
   `thm:open-closed-derived-center` `main.tex`:2322-2438). **No
   chiral product on $\R^2 \times \C^2$ needed**; this is purely
   algebraic on the formal symplectic disk's Hamiltonian Lie algebra.

2. **Factorization upgrade on the brane line $\R$**
   (`thm:open-closed-derived-center-factorization`,
   `main.tex`:1996-2210). The Steps 1-8 of the proof require:
   - HKR for $\widehat{\mathbf S}(\mathfrak h_I)$ (Step 1).
   - Continuous bar-cobar (Step 2).
   - Generator dictionary $c \mapsto \theta$, $u \mapsto O$ (Step 3).
   - CE differential compatibility on each interval $I \subset \R$
     (Step 4).
   - Quasi-isomorphism on each interval (Step 5).
   - **Factorization product compatibility for disjoint intervals**
     $I_1 \sqcup I_2 \subset V$ on $\R$ (Step 6,
     `main.tex`:2139-2173). **This requires the chiral-product
     structure on $\R$ alone** (M-1 G1-M1 closed), not the full
     chiral product on $\R^2 \times \C^2$.
   - Local constancy on $\R$ (Step 7).
   - Stalk recovery (Step 8).

3. **Bulk-to-defect coupling.** The Theorem G closed-side chain-
   level closure on the formal symplectic disk
   $\widehat{\C^2}_0$ uses the Hamiltonian Lie algebra structure on
   $\bar A = \mathfrak h_{\mathrm{poly}} / \C \cdot 1$ algebraically;
   the bulk $\C^2$ direction enters through this Hamiltonian Lie
   algebra, **not** through the holomorphic factorization apparatus
   on $\C^2$.

### §5.3 The partial chiral product is sufficient

**P4-EXEC-CPA-SUFF.** **The partial chiral product structure
constructed in §2.4 is sufficient for the chain-level closure of
Theorem G in the manuscript.**

**Severity 3.** **Status: valid. Confidence high.**

The argument:
- **(S-5.3.1)** Theorem G's chain-level closure on the closed side
  requires only `thm:open-closed-derived-center`'s cochain-level
  CE/PV identity, which is algebraic on $\bar A$ + shifted-cotangent
  duality. No chiral product on $\R^2 \times \C^2$ is invoked.
- **(S-5.3.2)** The factorization upgrade
  `thm:open-closed-derived-center-factorization` is on the brane
  line $\R$ alone (`main.tex`:1996-2046; structure maps induced by
  extension by zero on $\Omega^\bullet_c(I)$). This is the M-1
  G1-M1 brane-line BD chiral algebra deliverable. **Closed at
  G1-M1.**
- **(S-5.3.3)** The bulk $\R^2 \times \C^2$ extension of the
  brane-line factorization algebra (the unreduced lift, currently
  open per `rmk:unreduced-lift-status` and tracked as the M-37
  / R-03 obligation) is **not required** for the Theorem G
  chain-level closure. Theorem G is an anomaly statement about
  $\bar A$ on the formal symplectic disk; its proof never invokes
  the bulk factorization algebra on $\R^2 \times \C^2$.
- **(S-5.3.4)** The partial chiral product of §2.4 in fact
  *strengthens* the M-1 G1-M1 deliverable by extending it to the
  bulk at the BV-cohomological level. **The strengthening is not
  needed for Theorem G** but is consistent with it; it is needed
  for the W3-W9-04 (W-2D) bulk Weiss-cosheaf assertion (M-37 / R-03
  open obligation).

**Disposition.** Theorem G chain-level closure is **already
complete** at the manuscript-internal layer (G1-M1 + algebraic CE/PV
in `thm:open-closed-derived-center`). The partial chiral product
supplies *additional structure* for the M-12+ obligations (mixed
Dunn additivity; bulk Weiss product) but is not load-bearing for
Theorem G itself.

### §5.4 What the partial chiral product *does* close

The partial chiral product of §2.4 closes:
- (CL-1) The brane-line layer of (W-2D) on $\R$: the factorization
  algebra structure (G1-M1).
- (CL-2) The strict $E_2$-promotion on $\R^2$ in
  $\mathcal C_{\mathrm{ML}}$ (G1-M2).
- (CL-3) The Maurer-Cartan twist coupling topological and holomorphic
  factors at the BV-cohomological level (Mixed-Dunn-Probe §6.2,
  P4-EXEC-CPA-MC).

It does *not* close:
- (NCL-1) The strict operadic chiral product on the product manifold
  (M-12 Avenue (B) Mixed-Dunn).
- (NCL-2) The arbitrary-cover Weiss-cosheaf assertion (W3-W9-04 /
  R-03-I-4.b).
- (NCL-3) The conformal Virasoro stress tensor cross-walk
  (P4-G4-T2.2 type-clash; topological twist $\tau$).

---

## §6. Cross-walk to G1-M2 $E_2$-promotion + Maurer-Cartan twist

### §6.1 The strict $E_2$ factor on $\R^2$ (G1-M2 closed)

Per G1-M2 (P4-EXEC-G1-M2-DUNN-A), the brane-line $E_1$ algebra
$A_{\mathrm{brane}}$ on $\R$ tensors with its transverse copy
$A_\perp = A_{\mathrm{brane}}$ on the second $\R$-direction to give
a strict $E_2$-algebra $A_{\mathrm{E_2}} \simeq A_{\mathrm{brane}}
\otimes_{E_1} A_{\mathrm{brane}}$ on $\R^2$ in
$\mathcal C_{\mathrm{ML}}$, by Lurie 5.5.4.16 Dunn additivity in
the locally-constant subcategory.

The strict $E_2$ structure provides the topological half of the
partial chiral product: structure maps M-2.2.1 are exactly the
$E_2$-multiplication maps from G1-M2.

### §6.2 The Maurer-Cartan twist from $F_\alpha = 0$

Per Mixed-Dunn-Probe §6.2, the cross-flatness equation
$$\partial_{x_i}\alpha_{\bar z_j} -
\bar\partial_{z_j}\alpha_{x_i} +
\{\alpha_{x_i}, \alpha_{\bar z_j}\} = 0
\quad (i = 1, 2;\ j = 1, 2)$$
is a **Maurer-Cartan equation** in the Hamiltonian dg Lie algebra
$$\mathfrak L = \bigl(\Omega^*(\R^2) \otimes \Omega^{0,*}(\C^2)\bigr)
\widehat\otimes \widehat{\mathfrak h}[1]$$
with differential $D = d_{\R^2} + \bar\partial_{\C^2}$. The
ghost-zero Hamiltonian connection
$\alpha = \alpha_{x_i}dx_i + \alpha_{\bar z_j}d\bar z_j$ is the
candidate MC element; its on-shell flatness $F_\alpha = 0$ is the
MC equation; the Lagrange multiplier $\beta$ enforces this MC
equation at the chain level (`main.tex`:1818-1828; the gauge
symmetry $\delta_\varepsilon \beta = \mathrm{ad}^\vee_\varepsilon
\beta$ gives $F_\alpha = \mathrm{BV}\beta$).

**P4-EXEC-CPA-CW.** **The partial chiral product on $\R^2 \times \C^2$
is exactly the strict $E_2$-algebra (G1-M2 closed in
$\mathcal C_{\mathrm{ML}}$) twisted by the Maurer-Cartan element
$\alpha$ from $F_\alpha = 0$ at the cross-direction.** The twist
is by the cross-bracket
$\delta^{\mathrm{MC}} = \{\alpha_{x_i}, \alpha_{\bar z_j}\}$,
which deforms the strict $E_2$ structure on $\R^2$ by the
$\C^2$-direction Hamiltonian Lie bracket. At the BV-cohomological
level (on-shell, $F_\alpha = 0$), this twist is BV-exact, hence
the partial chiral product is cohomologically equivalent to the
strict $E_2$-algebra plus an explicit MC twist.

**Severity 3.** **Status: valid. Confidence high.**

### §6.3 The MC-twist sub-categorical sharpening

The MC twist $\alpha$ is a derived element in
$\mathrm{MC}(\mathfrak L)$, the Maurer-Cartan space of the dg Lie
algebra $\mathfrak L$. Per Costello-Gwilliam Vol I §3-§4 (deformation
quantization via Maurer-Cartan elements), an MC element on a dg
Lie algebra gives a *deformation* of the underlying chain complex by
twisting the differential. In our setting, the twist deforms:
- The strict $E_2$-multiplication on $\R^2$ (G1-M2) by the
  cross-bracket $\delta^{\mathrm{MC}}$.
- The (conjectural) holomorphic-$E_2$-multiplication on $\C^2$
  (Williams §3) by the cross-bracket $\delta^{\mathrm{MC}}$.

The result is the partial chiral product $\mu^\partial$ on
$\R^2 \times \C^2$ at the BV-cohomological level.

### §6.4 The cross-walk verdict

**P4-EXEC-CPA-CW-VERDICT.** **The partial chiral product on
$\R^2 \times \C^2$ corresponds exactly to a strict $E_2$-algebra
on $\R^2$ in $\mathcal C_{\mathrm{ML}}$ (G1-M2 closed) plus a
Maurer-Cartan twisting by $\alpha$ from $F_\alpha = 0$ at the
cross-direction. This cross-walk is the manuscript-internal
manifestation of the Mixed-Dunn additivity question
(Mixed-Dunn-Probe (V-4)).**

The cross-walk is *valid at the BV-cohomological level*; it does
*not* lift to the strict operadic level (the M-12 Avenue (B)
residual).

### §6.5 Connection to W3-W26 column-Verma data

The W3-W26 column-Verma vacuum module $\widehat M_0$ from G1-M1 is
an $E_1$-module of $A_{\mathrm{brane}}$ on $\R$. Per G1-M2 §6.2,
$\widehat M_0$ inherits an $E_2$-module structure of
$A_{\mathrm{E_2}}$ on $\R^2$ at the rank-1 unipotent Borel HWV
$v_{0, -1}$ stratum. The MC-twist by $\alpha$ acts trivially on
the HWV $v_{0, -1}$ (since the cross-bracket
$\{z_2, \alpha_{\bar z_j}\}$ kills the column-shifter $z_2$ at the
HWV level, by W3-W26-T1 §1.3). **Hence the column-Verma module
$\widehat M_0$ is an admissible chiral module of the partial chiral
product at the brane-line stratum.**

---

## §7. Smallest concrete example: small ball $B^2_r \times \{0\} \subset \R^2 \times \C^2$ with brane probe at the origin

### §7.1 The configuration

Let $B^2_r = \{(x_1, x_2) \in \R^2 : x_1^2 + x_2^2 < r^2\}$ be the
open ball of radius $r$ in the topological factor, located at the
origin. The configuration is:
- Bulk slice: $B^2_r \times \{0\} \subset \R^2 \times \C^2$ (so the
  $\C^2$-coordinate is fixed at the origin $\{0\} \in \C^2$).
- Brane line: $L = (B^2_r \cap (\R \times \{0\})) \times \{0\} \subset
  B^2_r \times \{0\}$ — the brane probe along the first
  $\R$-direction passing through the origin.
- Hamiltonian connection: $\alpha = \alpha_{x_1}(x_1, x_2)dx_1 +
  \alpha_{x_2}(x_1, x_2)dx_2$ on $B^2_r \times \{0\}$ (no
  $d\bar z_j$ component since $\C^2$ is at the origin only;
  $\alpha_{\bar z_j}$ enters only at the formal Taylor expansion at
  $\{0\} \in \C^2$).
- $F_\alpha = 0$: the topological-only flatness
  $\partial_{x_1}\alpha_{x_2} - \partial_{x_2}\alpha_{x_1} +
  \{\alpha_{x_1}, \alpha_{x_2}\} = 0$ on $B^2_r$.

### §7.2 The chiral product structure on this slice

The candidate chiral algebra on this slice is:
$$\mathcal A^\partial(B^2_r \times \{0\})
= C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak g^\partial_{B^2_r \times \{0\}}),
\qquad
\mathfrak g^\partial_{B^2_r \times \{0\}}
= \Omega^\bullet_c(B^2_r) \widehat\otimes \widehat{\mathfrak h}[1]$$
(the $\C^2$-direction collapses to the formal Taylor algebra at the
origin $\{0\} \in \C^2$, which is $\bar A$ algebraically).

This is **exactly the locally constant FA on $\R^2$ from G1-M2** —
no holomorphic factorization apparatus on $\C^2$ is invoked, since
the holomorphic structure is entirely captured by the formal disk's
Hamiltonian Lie algebra $\bar A$.

### §7.3 Why this example is concretely computable

The chiral product on this slice is **closed at G1-M2** (Avenue (E)
P4-EXEC-G1-M2-DUNN-A). The structure maps are:
- $E_2$-multiplication on disjoint disks in $B^2_r$ via
  Lurie 5.5.4.16.
- Algebraic Hamiltonian Lie bracket on
  $\widehat{\mathfrak h}$ on the $\C^2$-direction (formal Taylor at
  the origin).

The chiral Jacobi axiom (Ax.2) holds via the M-1 P4-G2-M1 verification
at 405 instances / 0 failures (cf. G1-M1 §3.4-4.2). The locally
constant axiom (Ax.4) holds via Lurie 5.5.4.10 + 5.5.4.16. The
holomorphic axiom (Ax.5) is *trivial* on this slice (the holomorphic
structure is collapsed to a single point).

### §7.4 What this example tests / does not test

**Tests passed:**
- (P-7.4.1) Chiral product structure on $\R^2$ topological factor.
- (P-7.4.2) Compatibility with the brane-line BD chiral algebra
  (G1-M1).
- (P-7.4.3) Maurer-Cartan twist trivializing on the $\C^2$-collapsed
  slice.
- (P-7.4.4) Column-Verma module structure on the HWV stratum
  (G1-M2 §6.2 + W3-W26-T1).

**Tests not exercised (because $\C^2$ collapsed):**
- (NP-7.4.1) Holomorphic-LCFA descent on $\C^2$ (Williams §3).
- (NP-7.4.2) Mixed Dunn additivity on $\R^2 \times \C^2$ proper.
- (NP-7.4.3) BD §3.4.10-11 chiral product on the curve product.

### §7.5 The next-to-smallest example

**The smallest example that exercises (Ax.5) holomorphic descent.**
Take $B^2_r \times P_\rho$ where
$P_\rho = \{(z_1, z_2) \in \C^2 : |z_1| < \rho, |z_2| < \rho\}$ is a
small holomorphic polydisk. The chiral product on this slice
includes:
- $E_2$-multiplication on $\R^2$ via Lurie 5.5.4.16.
- Holomorphic-$E_2$-multiplication on $\C^2$ via the candidate
  Williams §3 framework (M-12 Avenue (B) open at strict operadic
  level; closed at prefactorization-FA level on each polydisk
  inclusion).
- Cross-bracket twist $\{\alpha_{x_i}, \alpha_{\bar z_j}\}$ at the
  BV-cohomological level (Mixed-Dunn-Probe §6.2).

The **next-to-smallest example exercises (Ax.5) on each polydisk
$P_\rho$** but **does not exercise the strict operadic chiral
axiom on the product manifold** (which is the M-12 Avenue (B)
residual).

### §7.6 The computability summary

* **Smallest example** ($B^2_r \times \{0\}$): closed at G1-M2 +
  algebraic $\bar A$. **Concretely computable.**
* **Next-to-smallest example** ($B^2_r \times P_\rho$): partial
  closure at the BV-cohomological level via $F_\alpha = 0$.
  **Concretely computable at the BV-cohomological level**; strict
  operadic version is M-12 Avenue (B) open.
* **Full example** (arbitrary open $U \subseteq \R^2 \times \C^2$):
  M-12 Avenue (B) open at strict operadic level; closed at
  BV-cohomological level on the ML envelope.

---

## §8. Anti-attack scan: responses to (Att-1)-(Att-4)

### §8.1 (Att-1) BD §3.4.1 chiral product is defined for chiral algebras on a curve; does the chiral-product structure adapt sensibly to a higher-dim base?

**Response.** **Partially yes.**

* **(Y-Att-1)** The chiral product structure adapts at the
  *cohomological / prefactorization-FA level* via
  Lurie 5.5.4.10 + 5.5.4.16 (topological factor) and Williams §3
  (holomorphic factor). The brane-line BD chiral algebra (G1-M1) is
  on $X = \R$; its bulk extension via the Hamiltonian connection is
  the partial chiral product of §2.4.
* **(N-Att-1)** The chiral product structure does **not** adapt at
  the **strict operadic level** to the mixed product manifold. BD
  §3.4.10-11 covers two smooth complex curves $X, Y$ giving a
  2-complex-dimensional manifold; our setting is 6 real dimensions
  with mixed topological + holomorphic factors. This is the
  Mixed-Dunn obstruction (Mixed-Dunn-Probe (V-0)).

The taxonomy:
- BD's original framework: $X, Y$ both 1-complex-dimensional curves.
- Williams §3: $\C^n$ holomorphic-only.
- Lurie 5.5.4.16: $\R^n$ topological-only.
- *No literature*: mixed $\R^m \times \C^n$.

The adaptation to higher-dim base happens *on each factor separately*;
the cross-direction adaptation is the genuinely open question.

### §8.2 (Att-2) The Hamiltonian flatness $F_\alpha = 0$ is a Maurer-Cartan equation; does it produce a chiral product or only a partial Čech-compatible structure?

**Response.** **Only a partial Čech-compatible structure at the
BV-cohomological level.**

Per Mixed-Dunn-Probe §6.3 (Att-3 response there), $F_\alpha = 0$ is
**sufficient for the cohomological-level chiral product** (BV-exact
cross-bracket) but **insufficient for the strict operadic-level
chiral product** (the operadic obstruction class
$\mathrm{HOp}^\bullet$ remains non-trivial / unknown).

The partial chiral product of §2.4 is the **best available**
chiral-product-like structure on $\R^2 \times \C^2$ given only
$F_\alpha = 0$; it satisfies (Ax.1)-(Ax.5) at the BV-cohomological /
prefactorization-FA level (Mayer-Vietoris on product covers passes;
Čech compatibility on overlaps via $F_\alpha = 0$ BV-exactness).

The Maurer-Cartan structure of $F_\alpha = 0$ (Mixed-Dunn-Probe §6.2)
**provides the cross-direction structure map** at the BV-cohomological
level, but does not lift to the strict $\infty$-operadic structure
required for the full BD §3.4.11 chiral axiom on the product manifold.

### §8.3 (Att-3) The brane-defect along $L = \R \times \{0\}$ is a codimension-3 defect; how does the chiral product interact with the defect?

**Response.** **The brane defect is naturally absorbed into the
brane-line BD chiral algebra (G1-M1).**

Note on codimension count. In $X = \R^2 \times \C^2$ (6 real
dimensions), the brane line $L = \R \times \{0\} \times \{0\} \subset
X$ has 1 real dimension, hence codimension 5 in $X$ (cf. the
manuscript reduced line-defect current kernel
`constr:reduced-line-defect-current-kernel`,
`main.tex`:1881-1900). [The prompt's "codim-3" appears to be a
miscount; per Mixed-Dunn-Probe §1, GW's setting on $\R \times \C^2$
has codim-2 / codim-4 defects; in our 6-real-dim setting on
$\R^2 \times \C^2$, the brane $L = \R \times \{0\}_{x_2} \times \{0\}_{\C^2}$
is codim 5. We treat the defect as codim-5 here.]

The defect interaction:
* **(D-Att-3-1) Defect $E_1$-algebra.** The brane-line factorization
  algebra $\mathcal A_{\mathrm{fact}}$ on $\R$ (G1-M1) is the
  defect $E_1$-algebra structure on $L$. This is the brane-line
  chiral algebra layer.
* **(D-Att-3-2) Bulk-to-defect kernel.** The bulk Hamiltonian BF
  setup couples the bulk $\R^2 \times \C^2$ Hamiltonian connection
  to the brane-line via the matrix-valued normal-coordinate
  evaluation $z_i \mapsto \phi_i$ and trace
  (`main.tex`:1864-1879). This is the bulk-to-defect kernel
  $K_{\mathrm{bd}}$.
* **(D-Att-3-3) Defect chiral product.** The chiral product on the
  defect $L$ is the brane-line BD chiral product (G1-M1). The bulk
  chiral product on $X \setminus L$ is the partial chiral product
  of §2.4; its restriction to a neighborhood of $L$ (after
  translation transverse to $L$) recovers the defect chiral product
  via the bulk-to-defect kernel.

**No new obstruction is introduced by the defect**: the defect is
naturally absorbed into the brane-line layer, which is closed at
G1-M1.

### §8.4 (Att-4) Williams §3-§4 holomorphic-LC FA may admit a partial chiral product on $\C^n$ that bypasses the operadic mixed Dunn obstruction; verify or deny.

**Response.** **Verified: Williams §3-§4 admits a partial chiral
product on $\C^n$, but this does *not* bypass the *mixed* Dunn
obstruction.**

Williams §3 admits a holomorphic-locally-constant FA structure on
$\C^n$ valued in nuclear chain complexes; this is at the
$(\infty,1)$-categorical level. The implicit holomorphic Dunn
additivity $\mathbb E_m^{\mathrm{hol}} \otimes \mathbb E_n^{\mathrm{hol}}
\simeq \mathbb E_{m+n}^{\mathrm{hol}}$ on $\C^{m+n}$
(Mixed-Dunn-Probe §3.3 K-3.3.6, K-3.3.8) follows from Williams §3-§4
by adapting Lurie 5.5.4.16's locally-constant-subcategory argument
to the holomorphic-LCFA category.

**However**: this only addresses the **holomorphic-only** Dunn
additivity. The **mixed** Dunn additivity
$\mathbb E_m^{\mathrm{top}} \otimes \mathbb E_n^{\mathrm{hol}}
\simeq \mathbb E_{m,n}^{\mathrm{mixed}}$ requires the cross-equivalence
between two operad **types** (one topological, one holomorphic),
which is **not** in Williams §3-§4 (Mixed-Dunn-Probe §4.2 W-4.2.1,
W-4.2.2).

**The Williams partial chiral product on $\C^n$ does not bypass the
mixed Dunn obstruction**; it provides the holomorphic side of the
mixed setup but leaves the cross-direction operadic equivalence as
the genuinely open question.

### §8.5 (Att-5, implied) Sheaf-theoretic descent on Ran(R^2 × C^2) and Čech compatibility

**Response.** **Beilinson lens diagnosis: the sheaf-theoretic
descent on $\mathrm{Ran}(\R^2 \times \C^2)$ closes on product Weiss
covers (CG §A.5.6) but is open on arbitrary Weiss covers (W3-W9-04 /
R-03-I-4.b residual).**

The Čech / Mayer-Vietoris compatibility of the partial chiral
product:
* **(C-1)** On product covers $\{D_\alpha \times P_\beta\}$ with
  $D_\alpha \subset \R^2$ disks and $P_\beta \subset \C^2$ holomorphic
  polydisks, Čech compatibility passes via the product structure
  (CG §A.5.6 product-cosheaf stability). **Closed.**
* **(C-2)** On non-product covers $\{U_\gamma\}$ with $U_\gamma$
  arbitrary opens in $\R^2 \times \C^2$, Čech compatibility requires
  the cofinal refinement by product covers (W3-W9-04 question).
  **Open at the manuscript M-37 / R-03-I-4.b layer.**

The partial chiral product **does** pass Čech compatibility on
product covers in $\mathcal C_{\mathrm{ML}}$ (the BV-cohomological
level + ML colimit preservation, W3-W11-01-A). It **does not** pass
Čech compatibility on arbitrary covers (this is precisely the W-2D
Weiss-product-stability question on non-product covers, the M-37 /
R-03 obligation).

The cross-bracket $\{\alpha_{x_i}, \alpha_{\bar z_j}\}$ from
$F_\alpha = 0$ at on-shell BV-exactness supplies the overlap
compatibility on product covers; **the cofinal-refinement step from
arbitrary covers to product covers is the genuinely open Beilinson-
descent question**.

---

## §9. Residuals + Phase-5 escalation conditions

### §9.1 Closed in the partial-chiral-product audit (P4-EXEC-CPA scope)

* **(CL-9.1.1)** Definition of the partial chiral product
  $\mu^\partial$ on $\mathrm{Ran}(\R^2 \times \C^2)$ in
  $\mathcal C_{\mathrm{ML}}$ (§2.4).
* **(CL-9.1.2)** Per-axiom satisfaction at the BV-cohomological /
  prefactorization-FA level (§3.6 table).
* **(CL-9.1.3)** Identification of the first failing axiom (Ax.2 /
  (Ax.5) at the operadic level on the product manifold) and the
  residual obstruction class ($\mathrm{HOp}^\bullet$, Mixed-Dunn-Probe
  (O-6.5.3)) (§4.1-4.2).
* **(CL-9.1.4)** Sufficiency for the manuscript's Theorem G chain-
  level closure (§5.3 P4-EXEC-CPA-SUFF).
* **(CL-9.1.5)** Cross-walk to G1-M2 $E_2$-promotion + MC twist by
  $\alpha$ from $F_\alpha = 0$ (§6, P4-EXEC-CPA-CW).
* **(CL-9.1.6)** Smallest concrete example: $B^2_r \times \{0\}$
  closed; $B^2_r \times P_\rho$ partial-closed (§7).
* **(CL-9.1.7)** Anti-attack responses to (Att-1)-(Att-4) (§8).

### §9.2 Open as Phase-5 escalation conditions

* **(R-9.2.1) Full BD §3.4.11 chiral axiom on the product manifold.**
  This is the strict operadic chiral product on
  $\mathrm{Ran}(\R^2 \times \C^2)$. **M-12 Avenue (B) target,
  Mixed-Dunn-Probe §7 SP-1, SP-2, SP-3.**
* **(R-9.2.2) Operadic obstruction class $\mathrm{HOp}^\bullet$
  vanishing.** The operadic-level obstruction to the mixed Dunn
  additivity. **Phase-5 M-Mixed-Dunn-Operadic-Lift target.**
* **(R-9.2.3) Cofinal refinement of arbitrary Weiss covers by
  product covers.** W3-W9-04 question, W-2D bulk Weiss-cosheaf
  stability. **M-37 / R-03-I-4.b residual.**
* **(R-9.2.4) Conformal Virasoro stress tensor cross-walk.**
  P4-G4-T2.2 type-clash, requires topological twist $\tau$.
* **(R-9.2.5) Strengthening to arbitrary-colimit-preserving envelope.**
  W3-W11-01 silent strengthening; sub-M-3 layer.

### §9.3 Phase-5 escalation conditions

The partial chiral product audit does *not* trigger an immediate
Phase-5 escalation at the manuscript-internal scope: the Theorem G
chain-level closure is sufficient with the brane-line BD chiral
algebra (G1-M1) and the algebraic CE/PV theorem
(`thm:open-closed-derived-center`) alone.

Phase-5 escalation is triggered by **(R-9.2.1)** + **(R-9.2.2)**: the
M-12 Avenue (B) attack target lifts to a standalone preprint
(Mixed-Dunn-Probe §7 SP-2 / SP-3, ~70-120pp) suitable for *Selecta
Math.* / *Inventiones* / *Annals of Math.* The escalation condition
is met when the W3-W9-04 / R-03-I-4.b cofinal refinement question
is approached at the descent-theoretic level.

### §9.4 Master ledger

| ID | Status | Severity | Confidence | Disposition |
|---|---|---|---|---|
| P4-EXEC-CPA-PARTIAL | Defined | 3 | High | §2.4 |
| P4-EXEC-CPA-MC | Valid | 3 | High | §2.3 |
| P4-EXEC-CPA-FAIL-A | Failure-named | 3 | High | §4.1, Mixed-Dunn |
| P4-EXEC-CPA-OBS | Open-named | 3 | High id'n | §4.2, M-12 Avenue (B) |
| P4-EXEC-CPA-SUFF | Valid | 3 | High | §5.3 |
| P4-EXEC-CPA-CW | Valid | 3 | High | §6.2 |
| P4-EXEC-CPA-CW-VERDICT | Valid | 3 | High | §6.4 |

### §9.5 Aggregate verdict

**The partial chiral product on $\mathrm{Ran}(\R^2 \times \C^2)$
under $F_\alpha = 0$ closes at the BV-cohomological /
prefactorization-FA level; satisfies all five BD axioms
(Ax.1)-(Ax.5) at this level; fails at the strict operadic / chiral-
axiom-on-the-product-manifold level; is sufficient for the
manuscript's Theorem G chain-level closure; corresponds exactly to
the strict $E_2$-algebra (G1-M2 closed in $\mathcal C_{\mathrm{ML}}$)
plus a Maurer-Cartan twist by $\alpha$ from $F_\alpha = 0$; is
concretely computable in the smallest configuration $B^2_r \times \{0\}$;
and leaves the genuinely open obstruction class $\mathrm{HOp}^\bullet$
(operadic mixed Dunn additivity) as the M-12 Avenue (B) / Phase-5
escalation target.**

The Beilinson + Composition lens diagnosis confirms that the partial
chiral product is the best available structure given only the
G1-M1 + G1-M2 + $F_\alpha = 0$ data; the strict operadic upgrade
requires the M-12 Avenue (B) literature gap to be closed.
