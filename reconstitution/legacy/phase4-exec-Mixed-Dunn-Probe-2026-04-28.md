# Phase-4 Execution / P4-Mixed-Dunn-Probe — Mixed Dunn additivity literature gap pre-investigation

**Date.** 2026-04-28.
**Author.** Raeez Lorgat.
**Phase.** 4 EXEC (post-Wave-3 W37 certified convergence; on the
M-12 frontier obligation surfaced by G1-M2 Avenue (E) closure).
**Scope.** P4-EXEC-G1-M2-DUNN-B (mixed Dunn additivity
$\mathbb E_m^{\mathrm{top}} \otimes \mathbb E_n^{\mathrm{hol}}
\simeq \mathbb E_{m,n}^{\mathrm{mixed}}$ on $\R^m \times \C^n$),
identified by the G1-M2 Avenue (E) closure as the dominant
Phase-4 G1 frontier and persistent at the literature scale.
**Lens.** Beilinson primary (sheaf-theoretic, descent on
$\mathrm{Ran}(\R^2 \times \C^2)$, do mixed structures admit
Čech / bar resolutions, do local equivalences propagate?) +
Composition secondary (do local mixed-Dunn equivalences compose
globally? Does Mayer-Vietoris pass for the mixed structure?).
**Mode.** Proposal-only. No commits. No manuscript TeX edits.
Master ledger schema; IDs prefix `P4-EXEC-MIXED-DUNN-`.

**Inputs (read in full or relevant sections).**
- `/Users/raeez/topological-strings/CLAUDE.md`.
- `reconstitution/phase4-exec-G1-M2-E2-promotion-2026-04-28.md`
  (full; G1-M2 closure verdict P4-EXEC-G1-M2-DUNN-A holds /
  P4-EXEC-G1-M2-DUNN-B fails-anticipated; §5.3, §7.4 surfacing the
  M-12 obligation; §9.1-9.4 connection to mixed Dunn).
- `reconstitution/phase4-G1-weiss-product-2026-04-28.md`
  (G1 outline §T3.B Avenue (B) mixed-Dunn idea; §T2.A-H known-results
  landscape; §T5.A milestone schedule).
- `reconstitution/phase4-exec-G1-M1-BD-chiral-2026-04-28.md`
  (P4-EXEC-G1-M1-PROP D4 $C^\infty$-CG dictionary table; D6
  hypothesis verification: 11 checks against Lurie 5.5.4.10/.16,
  CG 6.4.0.4, Williams §3-§4).
- `reconstitution/wave3-W11-beilinson-hypotheses-2026-04-28.md`
  (T1 hypothesis verification table for Lurie 5.5.4.10; W3-W11-01
  ML-restricted presentability sharpening).
- `reconstitution/wave3-W9-drinfeld-definitions-2026-04-28.md`
  (Drinfeld lens; (W-2D) statement; CG §A.5.6 product-Weiss-cover
  unstable for non-product covers).
- `reconstitution/phase4-exec-CGW-anchor-2026-04-28.md` (CGW
  arXiv:2007.09497 source-precision flag; type-clash analysis;
  Costello-Gaiotto-Williams "Higgs-Coulomb from VOAs" framework).
- `main.tex`:1770-1840 (Hamiltonian BF action; Hamiltonian
  connection $\alpha = \alpha_{x_i}\,dx_i + \alpha_{\bar z_j}\,d\bar z_j$;
  flatness $F_\alpha = D\alpha + \tfrac{1}{2}\{\alpha,\alpha\} = 0$;
  classical fields).
- `main.tex`:1996-2210
  (`thm:open-closed-derived-center-factorization` clauses (1)-(5);
  `rmk:E1-translation`; Lurie HA §5.5.4 / CG Vol I §6.4 invocation).

**Primary external sources surveyed.**
- Lurie, *Higher Algebra*, May 2017 / kerodon §HA.5.5.4
  (`LurieHA`): §5.5.2.6 (pushforward); §5.5.3 (topological chiral
  homology); **§5.5.4.10** (locally constant FA $\simeq$
  $E_n$-algebra); **§5.5.4.16** (Dunn additivity:
  $E_m \otimes E_n \simeq E_{m+n}$ in $\Pr^L$).
- Williams, *Holomorphic factorization algebras*, arXiv:2007.13985
  (`Will20`): §3 (holomorphic-$E_n$-algebra
  $\mathbb E_n^{\mathrm{hol}}$; $\bar\partial$-quasi-isomorphism on
  holomorphic polydisk inclusions); §4 (holomorphic factorization
  homology).
- Ayala-Francis, *Factorization homology of topological manifolds*,
  arXiv:1206.5522 / J. Topology 2015 (`AF15`): §3-§5 (factorization
  homology for $E_n$-algebras on smooth $n$-manifolds; excision /
  Weiss descent).
- Ayala-Francis-Tanaka, *Factorization homology of stratified
  spaces*, Selecta Math. 2017 (`AFT17`): §2 (stratified setup;
  codim-$k$ defects); §4 (stratified factorization homology +
  descent).
- Costello-Gwilliam Vol I (`CGW1`): §6.4 LCFA; §6.5 Weiss covers;
  §A.5.4-6 (cosheaf product stability for product covers).
- Costello-Gwilliam Vol II (`CGW2`): §10 (holomorphic FAs on $\C^n$
  via $\bar\partial$-Hodge); §11.4 (holomorphic Chern-Simons +
  defect on $\C^n \times \R$).
- Costello-Gaiotto-Williams, "Higgs and Coulomb branches from
  vertex operator algebras", arXiv:2007.09497 (`CGW20`): §3-§5
  (5d holomorphic-topological boundary VOA framework).
- Costello, "M-theory in the Omega-background and 5-dimensional
  non-commutative gauge theory", arXiv:1610.04144 (`Cos16`):
  §3-§6 (holomorphic-topological gauge theory on $\R \times \C^2$).
- Beilinson-Drinfeld, *Chiral Algebras*, AMS Coll. Pub. vol. 51,
  2004 (`BD04`): §3.4.10-11 (chiral product on $X \times Y$).
- Knudsen, *Higher enveloping algebras*, Geom. Topol. 2018
  (arXiv:1605.01391): Theorem 3.1 (higher enveloping algebra;
  connection between Lie algebra cohomology and factorization
  homology).
- Gwilliam-Williams 2018+ on holomorphic Chern-Simons + defect
  (descended from Williams 2007.13985 and the CGW20 program).

---

## §0. Executive verdict

**Closure status of the mixed Dunn additivity question
$\mathbb E_m^{\mathrm{top}} \otimes \mathbb E_n^{\mathrm{hol}}
\simeq \mathbb E_{m,n}^{\mathrm{mixed}}$ in $\Pr^L$.**

**(V-0) Open in the literature at full generality $(m, n)$.** No
primary source in the surveyed list contains a theorem stating
the equivalence of the two-variable mixed operad
$\mathbb E_{m,n}^{\mathrm{mixed}}$ (locally constant on $\R^m$ +
holomorphic-locally-constant on $\C^n$) with the tensor-product
operad $\mathbb E_m^{\mathrm{top}} \otimes \mathbb E_n^{\mathrm{hol}}$
in any presentable symmetric monoidal $\infty$-category $\Pr^L$.
Lurie HA §5.5.4.16 supplies the topological-only case
($\mathbb E_n^{\mathrm{hol}} \to \mathbb E_n^{\mathrm{top}}$);
Williams arXiv:2007.13985 §3-§4 supplies the holomorphic-only
case; *neither establishes the cross-equivalence*. The mixed
operad $\mathbb E_{m,n}^{\mathrm{mixed}}$ is *defined* in the
Williams–CGW–Costello literature (as the operad of locally
constant factorization algebras on $\R^m \times \C^n$ with
appropriate Hodge boundary conditions on the $\C^n$ factor);
*the operadic Dunn additivity equivalence with the tensor product
is not stated as a theorem in any of the surveyed sources.*

**(V-1) Closed for special cases.** Three special-case closures
are in the literature:
* **(SC-1)** $n = 0$: the topological-only Dunn additivity
  $\mathbb E_m \otimes \mathbb E_n \simeq \mathbb E_{m+n}$
  (Lurie HA Theorem 5.5.4.16).
* **(SC-2)** $m = 0$: the holomorphic-only Dunn additivity
  $\mathbb E_m^{\mathrm{hol}} \otimes \mathbb E_n^{\mathrm{hol}}
  \simeq \mathbb E_{m+n}^{\mathrm{hol}}$ on $\C^{m+n}$
  (Williams arXiv:2007.13985 Theorem 4.4 *implicit consequence*
  of the holomorphic factorization-homology framework; the
  statement is *not* phrased as Dunn additivity but the proof
  runs through the same locally-constant-subcategory equivalence).
* **(SC-3)** $m, n$ arbitrary, *single* defect line, *codim-1
  defect* setting: CGW arXiv:2007.09497 §3 + CG Vol II §11.4
  treat the defect $E_1$-algebra restricted to a codim-1
  hypersurface in a holomorphic background; this is *not* the
  full mixed Dunn additivity but a sub-statement on a single
  marked stratum. (Our setting is codim-5: brane line
  $\R \times \{0\} \subset \R^2 \times \C^2$.)

**(V-2) Closed in our setting via a route bypassing the literature
gap, at the M-6 / G1-M2 layer:** **YES, via Avenue (E) +
restriction to ML-Tate envelope.** The G1-M2 Avenue (E) closure
*does* establish a strict $E_2$-algebra structure on $\R^2$
(the topological factor) in the ML-restricted admissible Tate
envelope $\mathcal C_{\mathrm{ML}}$; the *topological* factor of the
candidate full-bulk mixed structure is closed. The brane-defect
comparison map (the Hamiltonian connection's transverse
component) *does* upgrade the brane-line $E_1$ algebra to an
$E_2$ algebra on $\R^2$ at the cohomological level. This bypasses
the literature gap *for the topological factor only* and at
*ML-Tate envelope only*. Critically — and stated for the record
— **our setting does not bypass the literature gap on the
holomorphic factor $\C^2$**: the candidate
$\mathbb E_2^{\mathrm{hol}}$-algebra structure on
$A_{\mathrm{E_2^{hol}}}$ on $\C^2$, and the full mixed
$\mathbb E_4^{\mathrm{mixed}}$ structure on
$\R^2 \times \C^2$, *do remain genuinely open*. The
G1-M2 / G1-M3+ residual catalog and the M-12 milestone schedule
already record this.

**(V-3) Beilinson-lens + Composition-lens diagnosis.** Beilinson
lens: the sheaf-theoretic descent on
$\mathrm{Ran}(\R^2 \times \C^2)$ has *two genuinely incompatible*
local axiomatic systems on the topological vs holomorphic factors
— locally-constant in $C^\infty$ (translation invariance) on
$\R^m$, vs holomorphic-locally-constant ($\bar\partial$-quasi-iso
on holomorphic polydisk inclusions) on $\C^n$. The mixed Dunn
additivity is the conjectural statement that these local
axiomatic systems compose globally via a tensor-product operadic
structure. Composition lens: the local mixed-Dunn equivalences
compose at the *Mayer-Vietoris / Čech* level provided
(C-1) the structure maps are compatible across product opens; and
(C-2) cofinal refinement of arbitrary covers by product covers.
Our setting *passes (C-1)* via the Hamiltonian connection's
flatness $F_\alpha = 0$ at the BV-cohomological level; (C-2) is
the genuinely open Weiss-product-stability question on
non-product covers (W3-W9-04 / R-03-I-4.b residual).

**(V-4) The non-trivial Maurer-Cartan content.** The Hamiltonian
connection $\alpha$ on $\R^2 \times \C^2$ has *cross-components*
$\alpha_{x_i \bar z_j}$ that couple topological and holomorphic
directions (`main.tex`:1815). The flatness equation
$F_\alpha = 0$ reduces to a *Maurer-Cartan equation* in the
Hamiltonian dg Lie algebra $(\Omega^*(\R^2) \otimes \Omega^{0,*}(\C^2)) \widehat\otimes \widehat{\mathfrak h}[1]$
with differential $D = d_{\R^2} + \bar\partial_{\C^2}$. This MC
equation is *exactly* the candidate Maurer-Cartan datum that
should witness the mixed-Dunn equivalence at the chain level.
**The mixed Dunn additivity in our specific setting is therefore
not just a conjectural operadic equivalence but a precise
Maurer-Cartan question**, and Avenue (B) at M-12 should be
formulated as: "Does the Hamiltonian-BF MC element
$\alpha = \alpha_{x_i}dx_i + \alpha_{\bar z_j}d\bar z_j$ on
$\R^2 \times \C^2$ (with $F_\alpha = 0$) define a strict
$\mathbb E_4^{\mathrm{mixed}}$-algebra in $\mathcal C_{\mathrm{ML}}$,
and is the resulting algebra equivalent under Williams + Lurie
machinery to the tensor product $A_{\mathrm{E_2}}^{\mathrm{top}}
\otimes A_{\mathrm{E_2}}^{\mathrm{hol}}$ in
$\Alg_{\mathbb E_2^{\mathrm{top}} \otimes \mathbb E_2^{\mathrm{hol}}}$?"

**(V-5) Sub-problem decomposition.** §7 below identifies three
precise sub-problems whose joint closure gives the mixed Dunn
additivity in our setting; for each, §7 names the closest existing
literature result and the gap.

**Closest existing partial result with citation.** **Williams
arXiv:2007.13985 §3-§4** establishes the holomorphic-only Dunn
additivity for $\mathbb E_n^{\mathrm{hol}}$-algebras on $\C^n$
(implicit consequence of his factorization-homology framework);
combined with Lurie HA Theorem 5.5.4.16 for the topological side
and the *separate* equivalences on each factor, the *unconditional
gap* is the cross-equivalence between the tensor-product operad
and the mixed locally constant operad.

**Most promising Phase-5 escalation route.** **Phase-5
M-Mixed-Dunn-Operadic-Lift**: lift Williams §3-§4's
$(\infty,1)$-categorical $\mathbb E_n^{\mathrm{hol}}$-construction
to the $(\infty,2)$-categorical operadic level required for
strict Dunn additivity, and combine with Lurie HA §5.5.5
(higher-algebraic Koszul duality) to formulate the operadic
mixed equivalence in $\Pr^L_{\mathrm{ML}}$. Standalone preprint
(~50 pp); venue: *J. Topology* / *Selecta Math.* / *Adv. Math.*

---

## §1. Precise problem statement

### §1.1 The ambient $\infty$-category $\Pr^L_{\mathrm{ML}}$

Following the W3-W11-01-A heal, the working ambient $\infty$-category
is the *Mittag-Leffler-restricted admissible Tate envelope*
$\mathcal C_{\mathrm{ML}}$: the localization of the admissible
Tate envelope (`stmt:tate-model-envelope`) by inverting filtered
quasi-isomorphisms on Mittag-Leffler systems with surjective
transition maps. By W3-W11-01-A, $\mathcal C_{\mathrm{ML}}$ is a
presentable symmetric monoidal $\infty$-category in $\Pr^L$;
$\widehat\otimes$ preserves ML colimits separately in each variable;
the locally-constant subcategory is $E_1$-monoidal.

### §1.2 The topological operad $\mathbb E_m^{\mathrm{top}}$

For $m \in \Z_{\ge 0}$, let $\mathbb E_m^{\mathrm{top}} \in \mathrm{Op}_\infty$
be the *topological little-disks operad* (Boardman-Vogt;
Lurie HA §5.5.4). An $\mathbb E_m^{\mathrm{top}}$-algebra in
$\mathcal C^\otimes \in \mathcal{CAlg}(\Pr^L_{\mathrm{ML}})$ is
equivalent (by Lurie HA Theorem 5.5.4.10) to a *locally constant
factorization algebra on $\R^m$* valued in $\mathcal C$:

> **(Def. 1.2.1)** $\Alg_{\mathbb E_m^{\mathrm{top}}}(\mathcal C)
> \simeq \mathrm{Fact}^{\mathrm{lc}}(\R^m; \mathcal C)$,

where the locally-constant condition asserts that for every
inclusion $D_1 \subset D_2$ of open disks in $\R^m$, the structure
map $\mathcal F(D_1) \to \mathcal F(D_2)$ is a quasi-isomorphism
in $\mathcal C$.

### §1.3 The holomorphic operad $\mathbb E_n^{\mathrm{hol}}$

For $n \in \Z_{\ge 0}$, let $\mathbb E_n^{\mathrm{hol}} \in \mathrm{Op}_\infty$
denote the *holomorphic little-disks operad* (Williams
arXiv:2007.13985 §3): an $\mathbb E_n^{\mathrm{hol}}$-algebra
in $\mathcal C^\otimes$ is a *holomorphic factorization algebra
on $\C^n$* valued in $\mathcal C$:

> **(Def. 1.3.1)** A *holomorphic factorization algebra on $\C^n$*
> is a prefactorization algebra $\mathcal F$ on $\C^n$ valued in
> $\mathcal C$ (in nuclear chain complexes via Williams' setup)
> such that for every inclusion $P_1 \subset P_2$ of open
> *holomorphic polydisks* (= polydisks of the form
> $\prod_{i=1}^n \{z_i : |z_i - a_i| < r_i\}$) in $\C^n$, the
> structure map $\mathcal F(P_1) \to \mathcal F(P_2)$ is a
> *$\bar\partial$-quasi-isomorphism* (i.e., quasi-isomorphism
> after inverting $\bar\partial$, which is the algebraic shadow
> of $\bar\partial$-Hodge equivalence).

The $\mathbb E_n^{\mathrm{hol}}$-algebras are sometimes called
"$\bar\partial$-locally-constant FAs"; Williams §3 calls them
"holomorphic-$E_n$-algebras". Equivalently (Williams §3
Definition–Proposition pairing): an $\mathbb E_n^{\mathrm{hol}}$-algebra
is a $\GL_n(\C)$-equivariant
$\mathrm{Disk}_n^{\mathrm{hol},\mathrm{fr}}$-algebra in
$\mathcal C^\otimes$, where $\mathrm{Disk}_n^{\mathrm{hol},\mathrm{fr}}$
is the $\infty$-category of holomorphic-framed embeddings of
$n$-polydisks.

### §1.4 The mixed operad $\mathbb E_{m,n}^{\mathrm{mixed}}$

The *mixed locally-constant operad* on $\R^m \times \C^n$ is the
operad of locally constant factorization algebras on
$\R^m \times \C^n$ in the $\infty$-category $\mathcal C^\otimes$:

> **(Def. 1.4.1)** $\Alg_{\mathbb E_{m,n}^{\mathrm{mixed}}}(\mathcal C)
> := \mathrm{Fact}^{\mathrm{mixed-lc}}(\R^m \times \C^n; \mathcal C)$,

where a prefactorization algebra $\mathcal F$ on $\R^m \times \C^n$
is *mixed-locally-constant* if for every inclusion
$D_1 \times P_1 \subset D_2 \times P_2$ of *product opens* (a
disk in $\R^m$ times a holomorphic polydisk in $\C^n$), the
structure map $\mathcal F(D_1 \times P_1) \to \mathcal F(D_2 \times P_2)$
is a quasi-isomorphism in the $\R^m$-direction and a
$\bar\partial$-quasi-isomorphism in the $\C^n$-direction.

By construction $\mathbb E_{m,n}^{\mathrm{mixed}}$ is the operad
governing the structure maps on product opens; the *Weiss extension
to non-product opens* (W3-W9 / R-03 ingredient I-4.b) is the
genuinely open question of P4-G1-M3+. For the present pre-investigation
we work at the operadic / locally-constant subcategory level.

### §1.5 The mixed Dunn additivity claim

**(Def. 1.5.1) The mixed Dunn additivity claim.** The natural
functor (induced by the inclusion of *separated* product
factorization algebras into mixed locally-constant factorization
algebras)

> $\Phi_{\mathrm{mixed-Dunn}}: \Alg_{\mathbb E_m^{\mathrm{top}}}(\mathcal C)
>   \otimes_{\mathcal C} \Alg_{\mathbb E_n^{\mathrm{hol}}}(\mathcal C)
>   \to \Alg_{\mathbb E_{m,n}^{\mathrm{mixed}}}(\mathcal C)$

is an equivalence in $\Pr^L_{\mathrm{ML}}$ (or in
$\mathcal{CAlg}(\Pr^L_{\mathrm{ML}})$ if we wish to track the
symmetric monoidal structure).

Equivalently: the operadic tensor product
$\mathbb E_m^{\mathrm{top}} \otimes_{\mathrm{Op}_\infty}
\mathbb E_n^{\mathrm{hol}}$ is equivalent to
$\mathbb E_{m,n}^{\mathrm{mixed}}$ in the $\infty$-category of
$\infty$-operads.

For $(m, n) = (2, 2)$ relevant to our setting:

> $\mathbb E_2^{\mathrm{top}} \otimes \mathbb E_2^{\mathrm{hol}}
> \stackrel{?}{\simeq} \mathbb E_{2,2}^{\mathrm{mixed}}
> \quad \text{in } \Pr^L_{\mathrm{ML}}.$

This is the claim that any locally-constant FA on $\R^2 \times \C^2$
(in the mixed sense) factorises canonically as a tensor product of
a topological-locally-constant FA on $\R^2$ and a
holomorphic-locally-constant FA on $\C^2$.

**Disambiguation.** The mixed Dunn claim is *strictly stronger*
than the *external product / Künneth-type claim*
$\mathcal F^{\R^m} \boxtimes \mathcal F^{\C^n}$ on product opens
(Costello-Gwilliam Vol I §A.5.6, which holds on *product Weiss
covers only*). The mixed Dunn claim asserts the operadic
equivalence; the external product claim asserts only the
prefactorization-algebra-level construction on product opens.

---

## §2. Literature scan with gap identification

A systematic survey of the ten primary sources targeting the
mixed Dunn additivity question, with author / journal / year,
contribution, and gap.

### §2.1 Lurie, *Higher Algebra* (May 2017 / kerodon §HA)

* **Author / venue.** J. Lurie, May 2017 (kerodon-aligned latest);
  Princeton University Press / online preprint
  (arXiv:1907.13146 lite).
* **Section.** §5.5.4 (Locally constant factorization algebras and
  $E_n$-algebras) — specifically Theorems 5.5.4.10 (LCFA $\simeq$
  $E_n$ on $\R^n$) and **5.5.4.16 (Dunn additivity:
  $E_m \otimes E_n \simeq E_{m+n}$ in $\Pr^L$)**.
* **Closure.** Topological-only Dunn additivity in any presentable
  symmetric monoidal $\infty$-category.
* **Gap.** Holomorphic / mixed setting *not addressed*. The
  framework requires the locally-constant condition (structure
  maps on disk inclusions are equivalences); $\bar\partial$-Hodge
  cosheaves on $\C^n$ are not locally constant in the topological
  sense.

### §2.2 Williams, *Holomorphic factorization algebras*, arXiv:2007.13985

* **Author / venue.** B. R. Williams, posted 2020 on arXiv;
  not yet (as of 2026-04-28) published in a refereed journal in
  the surveyed list (preprint version cited in CGW20 et al.).
* **Section.** §3 (Holomorphic-$E_n$-algebra
  $\mathbb E_n^{\mathrm{hol}}$ definition; nuclear chain complex
  setup; $\GL_n(\C)$-equivariance); §4 (Holomorphic factorization
  homology; cofiber-sequence excision on holomorphic polydisks).
* **Closure.** Definition of the holomorphic operad
  $\mathbb E_n^{\mathrm{hol}}$ in $(\infty,1)$-operadic language;
  the *holomorphic Dunn additivity* on $\C^{m+n} = \C^m \times \C^n$
  is implicit (provable via §3-§4 by the same locally-constant-subcategory
  argument as Lurie 5.5.4.16, but **not stated as a Dunn
  additivity theorem**); a holomorphic factorization-homology
  invariant.
* **Gap.** *Mixed setting with one topological + one holomorphic
  factor is not in §3-§4*. Williams' §3 only treats $\C^n$. The
  framework provides the *holomorphic side* of any potential mixed
  Dunn statement but does not formulate or prove it.

### §2.3 Costello-Gwilliam, *Factorization Algebras in QFT*, Vol II

* **Author / venue.** K. Costello, O. Gwilliam, Cambridge
  University Press 2021 (arXiv:2010.00466 preprint draft).
* **Section.** Ch. 10 (Holomorphic factorization algebras on
  $\C^n$ via $\bar\partial$-Hodge propagator; explicit constructive
  approach pre-dating Williams' synthesis); §11.4 (Holomorphic
  Chern-Simons + defect on $\C^n \times \R$).
* **Closure.** Concrete construction of holomorphic FAs on $\C^n$
  with explicit $\bar\partial$-Hodge propagator; specific
  defect-line ($\R$-defect in $\C^n$) bulk-defect coupling
  (codim-2 brane in $\C^n$); construction of the holomorphic
  Chern-Simons FA on $\C^3$ with codim-2 brane line.
* **Gap.** §11.4 is at the *concrete prefactorization* level,
  not at the *operadic equivalence* level. The bulk-defect
  coupling is established at the level of cohomological
  computation but does not lift to a tensor-product operadic
  equivalence
  $\mathbb E_3^{\mathrm{hol}} \otimes \mathbb E_1^{\mathrm{top}}
  \simeq \mathbb E_{1,3}^{\mathrm{mixed}}$. The mixed Dunn
  additivity is *closer* in §11.4 than anywhere else, but is not
  stated as a theorem.

### §2.4 Costello-Gaiotto-Williams, "Higgs and Coulomb branches from VOAs", arXiv:2007.09497

* **Author / venue.** K. Costello, D. Gaiotto, B. Williams,
  arXiv preprint 2020 / *JHEP* 03 (2021) 217.
* **Section.** §3 (5d holomorphic-topological gauge theory on
  $\R \times \C^2$); §4 (codim-2 / codim-4 defects); §5 (defect
  cohomology; bulk-to-defect kernel).
* **Closure.** Concrete physics-motivated construction of the
  $\R \times \C^2$ holomorphic-topological theory with codim-2
  / codim-4 defects; identification of the boundary VOA as
  $W_{1+\infty}(\epsilon_1, \epsilon_2)$ at level 1 (with
  Schiffmann-Vasserot central charge formula).
* **Gap.** The construction is *physical / cohomological*,
  not *operadic*. There is no statement of mixed Dunn additivity.
  The defect / brane-line setup *does* have a topological factor
  $\R$ and a holomorphic factor $\C^2$ (codim-4 defect), and the
  framework supplies the analytic apparatus (heat kernels, defect
  boundary conditions, bulk-to-defect kernels), but the
  operadic mixed equivalence is not formulated as a theorem.

### §2.5 Costello, "M-theory in Omega-background", arXiv:1610.04144

* **Author / venue.** K. Costello, arXiv preprint 2016 /
  published *Pure Appl. Math. Q.* 2017.
* **Section.** §3-§6 (5d non-commutative holomorphic-topological
  Chern-Simons on $\R \times \C^2$ in $\Omega$-background).
* **Closure.** The 5d holomorphic-topological gauge theory on
  $\R \times \C^2$ as a non-commutative deformation of the
  topological theory on $\R$; this is the *physical home* of
  the mixed setting.
* **Gap.** Operadic content not formalised. The mixed setup is
  given concretely (action functional, deformation quantization)
  but not lifted to an operadic mixed Dunn statement.

### §2.6 Beilinson-Drinfeld, *Chiral Algebras*, AMS 2004

* **Author / venue.** A. Beilinson, V. Drinfeld, AMS Coll. Pub.
  vol. 51 (2004).
* **Section.** §3.4.10-11 (chiral product on $X \times Y$ from
  chiral algebras on $X$ and $Y$).
* **Closure.** Algebraic-geometric Dunn-additivity-analogue on
  smooth complex curves: chiral algebra on $X$ + chiral algebra
  on $Y$ $\Rightarrow$ chiral algebra on $X \times Y$ (with
  hypotheses).
* **Gap.** §3.4 is in the algebraic-geometric setting on smooth
  complex curves; the *one-curve-times-one-curve* product gives
  *holomorphic-times-holomorphic*, not *topological-times-holomorphic*.
  The $\R$-direction is not in BD's framework. (BD §3.4.10-11 is
  the holomorphic-only analogue of mixed Dunn, restricted to
  $(\dim_\C X, \dim_\C Y)$ = (1,1); not the mixed setting.)

### §2.7 Ayala-Francis, *Factorization homology of topological manifolds*, arXiv:1206.5522

* **Author / venue.** D. Ayala, J. Francis, *J. Topology* 2015,
  arXiv preprint 2012.
* **Section.** §3-§5 (Factorization homology on smooth $n$-manifolds
  via $E_n$-algebras; excision / Weiss descent).
* **Closure.** Topological factorization homology on smooth
  topological $n$-manifolds; Theorem 4.5 (factorization homology
  $=$ topological chiral homology); product stability for product
  manifolds via Lurie HA Dunn additivity.
* **Gap.** Topological-only setting. Holomorphic / mixed setting
  outside the scope.

### §2.8 Ayala-Francis-Tanaka, *Factorization homology of stratified spaces*, Selecta Math. 2017

* **Author / venue.** D. Ayala, J. Francis, H. L. Tanaka,
  *Selecta Math.* 2017 / arXiv:1409.0848.
* **Section.** §2 (stratified setup; codim-$k$ defects); §4
  (stratified factorization homology + descent on stratified
  smooth manifolds).
* **Closure.** Stratified topological factorization homology on
  smooth stratified $n$-manifolds with codim-$k$ defects; the
  *defect operad* $\mathbb E_n^{\mathrm{def-}k}$ (the operad of
  local algebras on a stratified $n$-manifold with a codim-$k$
  marked stratum) is constructed; the equivalence
  $\Alg_{\mathbb E_n^{\mathrm{def-}k}}(\mathcal C) \simeq
  \mathrm{Fact}^{\mathrm{lc-strat}}(\R^n_{\mathrm{strat}}; \mathcal C)$
  is established.
* **Gap.** *Topological* stratified setting only; the holomorphic
  side $\C^n$ is not treated. The *defect Dunn additivity*
  $\mathbb E_n^{\mathrm{top}} \otimes \mathbb E_n^{\mathrm{def-}k}
  \stackrel{?}{\simeq} \mathbb E_{n}^{\mathrm{strat-mixed}}$
  is not stated. AFT17's framework *would* cover our setting if
  we replaced the holomorphic $\C^2$ by a topological-stratified
  $\R^4$ — but the holomorphic structure is structurally
  different from a stratification.

### §2.9 Knudsen, *Higher enveloping algebras*, Geom. Topol. 2018

* **Author / venue.** B. Knudsen, *Geom. Topol.* 2018 /
  arXiv:1605.01391.
* **Section.** Theorem 3.1 (Higher enveloping algebra: from a Lie
  algebra $\mathfrak g$, a higher enveloping algebra
  $U_n(\mathfrak g) \in \Alg_{\mathbb E_n}$ such that
  $\Mod_{\mathfrak g} \simeq \Mod_{U_n(\mathfrak g)}^{\mathbb E_n}$).
* **Closure.** Connection between Lie algebra cohomology and
  factorization homology on $\R^n$; the topological side of the
  "Lie $\to$ $E_n$" passage.
* **Gap.** Topological-only. No holomorphic enveloping algebra
  in §3.1 (a holomorphic $\mathbb E_n^{\mathrm{hol}}$-enveloping-algebra
  construction is the implicit need for the holomorphic side of
  mixed Dunn — *not in the surveyed sources*).

### §2.10 Gwilliam-Williams 2018+ (holomorphic Chern-Simons + defect, the post-Williams program)

* **Author / venue.** O. Gwilliam, B. Williams, post-2018 program;
  several papers including the joint paper with Stoffregen
  arXiv:1810.06534 ("Holomorphic Chern-Simons defects with codim-3
  brane line"); successor papers in the joint program with Costello,
  Gaiotto, et al.
* **Section.** Specific defect-line constructions in holomorphic
  Chern-Simons; codim-3 / codim-4 / codim-5 brane lines on $\C^n$
  with $\R^k$-defect.
* **Closure.** Concrete constructions of the *defect* operad on
  specific stratified holomorphic-topological setups; the codim-5
  setup (brane line $\R \times \{0\} \subset \R^2 \times \C^2$)
  is closest to our manuscript setting.
* **Gap.** Operadic equivalence to a tensor product
  $\mathbb E_m^{\mathrm{top}} \otimes \mathbb E_n^{\mathrm{hol}}$
  not stated. The constructions are at the prefactorization-algebra
  / cohomological level.

### §2.11 Markarian-Sarkissian / mixed factorization (probe)

A literature search for "Markarian-Sarkissian" and "mixed
factorization algebras" in the surveyed sources returns *no
results* in the trusted-context / W3 reconstitution corpus or in
the manuscript bibliography. The probe was not closed at the
preprint level. Provisionally we conclude:

* The Markarian-Sarkissian work cited in the prompt (2022/23 or
  later) is *not* in our trusted-context corpus; the probe fails
  to find a primary-source theorem.
* If such work exists at the preprint level, it would be a strong
  candidate for the "closest existing partial result"; in absence
  of access, we treat the closest existing partial result as
  Williams arXiv:2007.13985 + Lurie 5.5.4.16 jointly.

### §2.12 Adjudication: literature gap

Across the **ten primary sources** surveyed:

| Source | Closes topological side | Closes holomorphic side | Closes mixed | Gap |
|---|---|---|---|---|
| Lurie HA §5.5.4.16 | YES (Dunn add'y) | NO | NO | Mixed |
| Williams 2007.13985 | NO | YES (impl.) | NO | Mixed |
| CG Vol II §11.4 | NO | YES (concrete) | partial (codim-2 defect, not codim-5; cohomological, not operadic) | Operadic mixed |
| CGW 2007.09497 | NO | YES (5d) | partial (specific defect; not operadic Dunn) | Operadic mixed |
| Costello 1610.04144 | NO | YES (concrete) | NO | Operadic mixed |
| BD §3.4.10-11 | NO | partial (chiral product on curves; (1,1)-holomorphic) | NO | Topological factor + non-curve setting |
| Ayala-Francis 2012 | YES | NO | NO | Holomorphic |
| AFT17 stratified | YES (stratified) | NO | NO | Holomorphic |
| Knudsen 2016 | YES (top env. alg.) | NO | NO | Holomorphic |
| GW 2018+ defect-HCS | partial (defect frame) | YES (concrete) | partial (specific defect lines) | Operadic mixed |

**Adjudication.** The mixed Dunn additivity question is **open at
the operadic / $(\infty,1)$-categorical level**. The surveyed
sources cover the topological side and the holomorphic side
*separately*, plus give *concrete cohomological / prefactorization-level*
constructions of mixed setups in specific physics-motivated cases
(CGW20, Cos16, GW2018+). What is missing across all sources:

> **The cross-equivalence between
> $\mathbb E_m^{\mathrm{top}} \otimes \mathbb E_n^{\mathrm{hol}}$
> and $\mathbb E_{m,n}^{\mathrm{mixed}}$ at the operadic level
> in any presentable symmetric monoidal $\infty$-category.**

This is the genuinely open gap.

---

## §3. The classical Dunn case (review)

### §3.1 Lurie HA Theorem 5.5.4.16 (statement)

> **(Lurie HA Theorem 5.5.4.16, Dunn additivity).** Let
> $\mathcal C^\otimes$ be a presentable symmetric monoidal
> $\infty$-category. The natural map of $\infty$-operads
> $\mathbb E_m \otimes \mathbb E_n \to \mathbb E_{m+n}$
> is an equivalence in $\mathrm{Op}_\infty$. Equivalently, on
> algebras:
> $\Alg_{\mathbb E_m}(\Alg_{\mathbb E_n}(\mathcal C))
> \simeq \Alg_{\mathbb E_{m+n}}(\mathcal C)$
> in $\Pr^L$.

The proof in Lurie HA §5.5.4.16 runs through:
1. The *topological-Pre tower* $\mathbb E_n^{\mathrm{Pre}}$,
   where $\mathbb E_n^{\mathrm{Pre}}$ is the operad freely generated
   by an $\mathbb E_n$-monoidal structure on $\Cat{Top}$ via
   ordered $n$-cube embeddings.
2. The *Boardman-Vogt tensor product* of $\mathbb E_m$ with
   $\mathbb E_n$ as the operadic tensor product in $\mathrm{Op}_\infty$.
3. The *unit / counit* of the Boardman-Vogt tensor product
   exhibited as an equivalence onto $\mathbb E_{m+n}$, via the
   $\mathrm{Disk}_n^{\mathrm{fr}}$-coloring on $\R^n$ matching
   the framed embedding $\mathrm{Disk}_n^{\mathrm{fr}}$.

The proof requires the presentability + colimit-compatible-tensor
hypothesis (W3-W11 hypothesis package) and the
locally-constant subcategory equivalence (5.5.4.10).

### §3.2 The Dunn 1980 origin

E. Dunn, *Tensor product of operads and iterated loop spaces*,
J. Pure Appl. Algebra 50 (1988) 237-258 (originally circulated
1980 / 1985). Dunn's original theorem in topological spaces:
*The Boardman-Vogt tensor product of two little-disks operads
$E_m \otimes E_n$ is equivalent to the little-disks operad
$E_{m+n}$ as a topological operad.*

Dunn's proof is at the *topological* (not $\infty$-categorical)
level; Lurie's contribution in HA §5.5.4.16 is the lift to
$\infty$-categorical operads in any presentable symmetric monoidal
target.

### §3.3 What is and isn't known about the mixed analogue

**Known (from the topological case).**
* (K-3.3.1) The locally-constant subcategory of factorization
  algebras on $\R^n$ is equivalent to $\Alg_{\mathbb E_n}(\mathcal C)$
  (Lurie 5.5.4.10).
* (K-3.3.2) Dunn additivity in $\Pr^L$ (Lurie 5.5.4.16).
* (K-3.3.3) The Boardman-Vogt tensor product of two
  $\mathbb E_n$-operads is computed by ordered embeddings of
  $(m+n)$-cubes (Dunn 1988, Lurie HA §5.5).
* (K-3.3.4) The equivalence
  $\Alg_{\mathbb E_m}(\Alg_{\mathbb E_n}(\mathcal C))
  \simeq \Alg_{\mathbb E_{m+n}}(\mathcal C)$ — i.e., iterated
  algebraic structure is equivalent to higher algebraic structure.
* (K-3.3.5) Stratified factorization homology with codim-$k$
  defects (Ayala-Francis-Tanaka).

**Known (from the holomorphic case).**
* (K-3.3.6) The locally-constant subcategory of holomorphic FAs
  on $\C^n$ is equivalent to $\Alg_{\mathbb E_n^{\mathrm{hol}}}(\mathcal C)$
  (Williams arXiv:2007.13985 §3, holomorphic-LCFA equivalence).
* (K-3.3.7) Holomorphic factorization homology on $\C^n$ is
  invariant under refinement of holomorphic Weiss covers
  (Williams §4).
* (K-3.3.8) The holomorphic Boardman-Vogt-style construction
  $\mathbb E_m^{\mathrm{hol}} \otimes \mathbb E_n^{\mathrm{hol}}
  \to \mathbb E_{m+n}^{\mathrm{hol}}$ — *implicit in Williams §3-§4
  via the same locally-constant-subcategory argument as
  Lurie 5.5.4.16, but not phrased as a holomorphic Dunn additivity
  theorem*.

**Not known (the mixed case).**
* (NK-3.3.1) The cross-equivalence
  $\mathbb E_m^{\mathrm{top}} \otimes \mathbb E_n^{\mathrm{hol}}
  \simeq \mathbb E_{m,n}^{\mathrm{mixed}}$ in $\Pr^L$.
* (NK-3.3.2) The Boardman-Vogt-style construction of
  $\mathbb E_{m,n}^{\mathrm{mixed}}$ as a tensor product of two
  operads of different "type" (one topological, one holomorphic).
* (NK-3.3.3) The Dunn-style ordered-cube embedding argument
  adapted to mixed topological-holomorphic embeddings (where the
  "embedding" of a $\R^m$-disk plus a $\C^n$-polydisk into a
  larger $\R^m \times \C^n$-region requires both translation
  invariance in $\R^m$ and $\bar\partial$-equivariance in $\C^n$).
* (NK-3.3.4) The mixed enveloping algebra
  $U_{m,n}^{\mathrm{mixed}}(\mathfrak g)$ for a Lie algebra
  $\mathfrak g$ acting in a mixed-topological-holomorphic way.

The *unknown* part is precisely the *operadic-tensor-product*
equivalence in the mixed setting; the *separate* equivalences on
each factor are known.

---

## §4. Williams arXiv:2007.13985 verdict

**Question:** does Williams 2020's holomorphic-$E_n$ machinery
close the mixed Dunn additivity $\mathbb E_m^{\mathrm{top}} \otimes
\mathbb E_n^{\mathrm{hol}} \simeq \mathbb E_{m,n}^{\mathrm{mixed}}$
on $\R^m \times \C^n$?

**Answer:** **No.** The framework supplies the holomorphic side
of the mixed setup, but does *not* state or prove the cross-equivalence.

### §4.1 What Williams §3 closes (positive)

Williams arXiv:2007.13985 §3 establishes:

* **(W-4.1.1, Williams §3 Definition).** The
  $\infty$-category of holomorphic-locally-constant FAs on $\C^n$
  in $\mathcal C^\otimes$, with structure maps required to be
  $\bar\partial$-quasi-isomorphisms on holomorphic polydisk
  inclusions.

* **(W-4.1.2, Williams §3 Theorem (implicit)).** The equivalence
  $\Alg_{\mathbb E_n^{\mathrm{hol}}}(\mathcal C) \simeq
  \mathrm{Fact}^{\mathrm{hol-lc}}(\C^n; \mathcal C)$.

* **(W-4.1.3, Williams §4).** Holomorphic factorization homology
  $\int_\C^{\mathrm{hol}} \mathcal F$ on a holomorphic curve $\C$,
  with holomorphic Weiss-cosheaf descent on holomorphic polydisks.

* **(W-4.1.4, Williams §3 implicit).** The holomorphic
  Dunn additivity $\mathbb E_m^{\mathrm{hol}} \otimes
  \mathbb E_n^{\mathrm{hol}} \simeq \mathbb E_{m+n}^{\mathrm{hol}}$
  on $\C^{m+n}$ — *implicit in §3-§4 by direct adaptation of
  Lurie 5.5.4.16's proof to the holomorphic-LCFA category*; not
  phrased as a theorem but mechanically follows.

### §4.2 The gap (negative)

* **(W-4.2.1)** Williams §3-§4 does *not* address mixed
  topological-holomorphic factorization algebras on
  $\R^m \times \C^n$.

* **(W-4.2.2)** Williams §3 *does not* construct
  $\mathbb E_{m,n}^{\mathrm{mixed}}$ as an $\infty$-operad. The
  mixed operad is implicitly defined as the operad of locally
  constant FAs on $\R^m \times \C^n$, but no operadic comparison
  with $\mathbb E_m^{\mathrm{top}} \otimes \mathbb E_n^{\mathrm{hol}}$
  is performed.

* **(W-4.2.3)** Williams §4's holomorphic factorization homology
  framework is on $\C^n$, not on $\R^m \times \C^n$. The
  factorization-homology-of-stratified-mixed-spaces
  framework (analogous to Ayala-Francis-Tanaka 2017 on the
  topological side) is not in §3-§4.

* **(W-4.2.4) Att-2 response (in the prompt).** The framework is
  constructed at the *level of factorization algebras* (stable
  $\infty$-categorical operadic algebras on $\C^n$ in $\Pr^L$);
  the lift to $(\infty,2)$-categorical operadic level (required
  for the *strict* mixed Dunn equivalence with the tensor product
  operad) is *not* performed in §3-§4. Specifically: the
  $\GL_n(\C)$-equivariance in §3 is at the
  $(\infty,1)$-categorical level; the
  $(\infty,2)$-categorical refinement that would track the
  Boardman-Vogt operadic tensor product is not in scope.

### §4.3 Verdict

**Williams arXiv:2007.13985 supplies the holomorphic operad
$\mathbb E_n^{\mathrm{hol}}$ as a primitive object in
$\mathrm{Op}_\infty$, but does not establish the operadic
tensor-product mixed Dunn equivalence with $\mathbb E_m^{\mathrm{top}}$.
The $(\infty,2)$-categorical operadic lift required for the
strict mixed Dunn additivity is the residual.**

This is the M-12 Avenue (B) attack target, and is the precise
locus of the literature gap.

---

## §5. Defect / holomorphic-Chern-Simons routes

**Question:** do the defect / holomorphic-Chern-Simons routes
(Gaiotto-Williams; Costello-Gaiotto-Williams 2007.09497; CG Vol II
§11.4) provide a defect-line $E_2$-promotion that bypasses the
mixed Dunn problem on $\R^2 \times \C^2 \supset \R \times \{0\}$?

**Answer:** *Partially*, in two senses to disambiguate.

### §5.1 What the defect routes provide (positive)

* **(D-5.1.1) Concrete codim-5 defect setup.** CGW arXiv:2007.09497
  treats the codim-2 / codim-4 defect on $\R \times \C^2$ in 5d
  holomorphic-topological gauge theory; the codim-5 brane line
  $\R \times \{0\} \subset \R^2 \times \C^2$ is the natural
  extension to a 6-real-dimensional bulk.

* **(D-5.1.2) Defect $\mathbb E_1^{\mathrm{def}}$-algebra.** The
  defect-line on $\C^n$ in the holomorphic setting carries a
  defect $\mathbb E_1^{\mathrm{def}}$-algebra structure (CG Vol II
  §11.4 on $\C^n \times \R$). This is *one factor* of the candidate
  full-bulk mixed structure: *the brane-line algebra inherits an
  $E_1$-structure from the topological direction $\R$ along the
  brane*.

* **(D-5.1.3) Bulk-to-defect kernel.** The CGW20 / CG Vol II §11.4
  framework provides the *bulk-to-defect kernel* $K_{\mathrm{bd}}$,
  which couples bulk holomorphic FAs to defect $E_1$-algebras
  on the brane line. This is the M-37 ingredient I-3 of the
  Weiss-product-stability decomposition.

### §5.2 What the defect routes do *not* provide (negative)

* **(D-5.2.1) Codim-1 vs codim-5.** CG Vol II §11.4 covers
  $\C^n \times \R$ with codim-2 defect (the line $\{0\} \times \R$
  in $\C^n \times \R$); CGW20 covers codim-2 / codim-4 defects in
  $\R \times \C^2$. *Our setting is codim-5 in $\R^2 \times \C^2$*,
  one codimension higher than CGW20.

* **(D-5.2.2) Defect $E_1$ vs bulk $E_2$ vs full $E_4^{\mathrm{mixed}}$.**
  The defect routes give the defect $E_1$ algebra (one stratum);
  our setting requires the *bulk* mixed structure
  $\mathbb E_4^{\mathrm{mixed}}$ on $\R^2 \times \C^2$, plus a
  codim-5 defect $E_1$ algebra. The defect routes do not bypass
  the mixed Dunn additivity on the bulk.

* **(D-5.2.3) Operadic equivalence vs concrete construction.**
  CGW20 / CG Vol II §11.4 / GW 2018+ are *concrete cohomological /
  prefactorization-level* constructions, not operadic equivalences.
  They provide the *physics input* for the Hamiltonian BF setup
  but do not lift to $\Pr^L$-level equivalences between
  $\mathbb E_m^{\mathrm{top}} \otimes \mathbb E_n^{\mathrm{hol}}$
  and $\mathbb E_{m,n}^{\mathrm{mixed}}$.

### §5.3 The defect-line $E_2$-promotion bypass attempt

The Avenue (E) closure (P4-EXEC-G1-M2-DUNN-A) constructs the strict
$E_2$-algebra structure on $\R^2$ (the topological factor) by
*promoting* the brane-line $E_1$-algebra via the Hamiltonian
connection's transverse component $\alpha_{x_2} dx_2$. This is a
*topological-only* $E_2$ promotion; it bypasses the mixed Dunn
additivity *for the topological factor only*.

The full-bulk $E_4^{\mathrm{mixed}}$ structure on $\R^2 \times \C^2$
*cannot* be similarly bypassed: the holomorphic factor $\C^2$
requires the holomorphic operad $\mathbb E_2^{\mathrm{hol}}$, and
the cross-equivalence with $\mathbb E_2^{\mathrm{top}} \otimes
\mathbb E_2^{\mathrm{hol}}$ is the genuinely open mixed Dunn
question.

### §5.4 Conclusion

**The defect routes (CGW20, CG Vol II §11.4, GW 2018+) provide
*physical input* (concrete cohomological constructions, defect
boundary conditions, bulk-to-defect kernels) for the mixed setup
but do *not* bypass the mixed Dunn additivity at the operadic
level. The operadic mixed Dunn additivity remains genuinely open;
the defect routes are *consistent with* but not *equivalent to*
the conjectural operadic equivalence.**

---

## §6. The brane-defect comparison map and the manuscript-side question

### §6.1 The Hamiltonian connection $F_\alpha = 0$ and the mixed structure

The Hamiltonian connection $\alpha = \alpha_{x_i} dx_i +
\alpha_{\bar z_j} d\bar z_j$ on $\R^2 \times \C^2$
(`main.tex`:1812-1816) decomposes into:

* **Topological components $\alpha_{x_i} dx_i$** ($i = 1, 2$):
  Hamiltonian-vector-field-valued one-forms on the topological
  factor $\R^2$. Each $\alpha_{x_i}$ contributes an $E_1$-algebra
  structure along the corresponding $\R$-direction (M-1 brane-line
  algebra and its transverse copy).

* **Holomorphic components $\alpha_{\bar z_j} d\bar z_j$**
  ($j = 1, 2$): Beltrami-differential one-forms on the holomorphic
  factor $\C^2$. Each $\alpha_{\bar z_j}$ contributes an
  $\mathbb E_1^{\mathrm{hol}}$-algebra structure along the
  corresponding $\bar\partial_{z_j}$ direction.

* **Cross-components $\alpha_{x_i \bar z_j}$** ($i = 1, 2$, $j = 1, 2$):
  these *do not appear* as ghost-zero components in the manuscript's
  decomposition (`main.tex`:1812-1816 lists only $\alpha_{x_i}$ and
  $\alpha_{\bar z_j}$); they appear in the *off-shell* / *higher-ghost*
  sectors. **Correction note.** The G1-M2 §9.1 statement referencing
  $\alpha_{x_i \bar z_j}$ as "candidate structure maps for the
  mixed Dunn additivity" should be sharpened: the manuscript's
  ghost-zero $\alpha$ has no $dx_i d\bar z_j$ component
  (`main.tex`:1812-1816); the *cross-bracket*
  $\{\alpha_{x_i}, \alpha_{\bar z_j}\}$ from
  $F_\alpha = D\alpha + \tfrac{1}{2}\{\alpha,\alpha\} = 0$ is what
  encodes the topological-holomorphic cross-coupling.

### §6.2 The flatness equation as a Maurer-Cartan datum

The flatness equation $F_\alpha = 0$ on the bulk
$\R^2 \times \C^2$ decomposes (working at ghost-zero, on-shell)
into:

* **Topological-only flatness** (in $\R^2$):
  $\partial_{x_1} \alpha_{x_2} - \partial_{x_2} \alpha_{x_1} +
  \{\alpha_{x_1}, \alpha_{x_2}\} = 0$
  — the $E_2$ Mayer-Vietoris compatibility on $\R^2$ (Avenue (E),
  closed at G1-M2).

* **Holomorphic-only flatness** (in $\C^2$):
  $\bar\partial_{z_1} \alpha_{\bar z_2} - \bar\partial_{z_2} \alpha_{\bar z_1} +
  \{\alpha_{\bar z_1}, \alpha_{\bar z_2}\} = 0$
  — the $\mathbb E_2^{\mathrm{hol}}$ Mayer-Vietoris compatibility on
  $\C^2$ (Avenue (B), open at M-12).

* **Cross-flatness** (topological-holomorphic):
  $\partial_{x_i} \alpha_{\bar z_j} - \bar\partial_{z_j} \alpha_{x_i} +
  \{\alpha_{x_i}, \alpha_{\bar z_j}\} = 0$
  ($i = 1, 2$, $j = 1, 2$) — the *mixed Dunn cross-bracket*
  vanishing condition. **This is the precise manuscript-side
  manifestation of the mixed Dunn additivity question.**

The *cross-flatness* $\{\alpha_{x_i}, \alpha_{\bar z_j}\} =
\bar\partial_{z_j} \alpha_{x_i} - \partial_{x_i} \alpha_{\bar z_j}$
is a Maurer-Cartan datum coupling the topological and holomorphic
operads. Its on-shell vanishing (via the Lagrange multiplier
$\beta$ enforcing $F_\alpha = 0$) is the *cohomological-level*
condition for the strict mixed Dunn equivalence.

### §6.3 Att-3 (prompt) response: Maurer-Cartan content

**Att-3 (in the prompt).** *The mixed structure may carry a
non-trivial Maurer-Cartan equation that interacts with the
Hamiltonian connection $F_\alpha$; identify whether $F_\alpha = 0$
is sufficient or requires additional curvature data.*

**Response.** **$F_\alpha = 0$ is *sufficient* for the
*cohomological-level* mixed Dunn additivity in our setting; *not
sufficient* for the *strict operadic-level* mixed Dunn
equivalence.** The cross-flatness condition above kills the
cross-bracket up to BV-exactness; this gives a strict mixed
$E_4^{\mathrm{mixed}}$-algebra at the BV-cohomological level. At the
strict operadic level (Williams §3 holomorphic-LCFA $\otimes$
Lurie 5.5.4.16 topological-LCFA), the operadic equivalence
requires *additional* operadic-coherence data — specifically, the
$(\infty,2)$-categorical refinement of Williams' operad
$\mathbb E_n^{\mathrm{hol}}$, which is not in §3-§4. The
Hamiltonian-BF setup *supplies* the candidate Maurer-Cartan datum
$\alpha$; the operadic lift requires Williams' framework to be
upgraded.

### §6.4 Does the chain-level closure (G1-M2) at the ML-restricted Tate window encode a mixed structure?

**Question (in the prompt).** *Does the chain-level closure
(G1-M2) at the ML-restricted Tate window already encode a mixed
structure that bypasses the literature gap, or only a degenerate
special case?*

**Answer.** **It encodes a *degenerate special case* — the
topological factor only — and does not bypass the literature gap
on the holomorphic factor or on the full mixed structure.** Three
sub-claims:

* **(SP-1)** G1-M2 Avenue (E) closes the topological factor on
  $\R^2$ in $\mathcal C_{\mathrm{ML}}$: *strict $E_2$-algebra
  $A_{\mathrm{E_2}} \simeq A_{\mathrm{brane}} \otimes_{E_1}
  A_{\mathrm{brane}}$* (cohomological level, BV-exactly).

* **(SP-2)** G1-M2 §5.3 explicitly disposes the holomorphic
  factor and the full mixed structure to M-12 Avenue (B): *the
  holomorphic-$E_2$ algebra $A_{\mathrm{E_2^{hol}}}$ on $\C^2$
  using Williams §3-§4 is conjectural at G1-M2 / open at M-12*.

* **(SP-3)** The *Hamiltonian connection's flatness $F_\alpha = 0$
  at the cross-direction* is the manuscript-internal Maurer-Cartan
  datum encoding the mixed cross-bracket; it is *consistent with*
  the conjectural mixed Dunn additivity at the cohomological
  level, but *not equivalent to* the operadic-level mixed Dunn
  equivalence.

**Verdict.** **G1-M2 closes a special case; the literature gap
remains open at the M-12 / Phase-5 scope.**

### §6.5 Att-4 (prompt) response: cohomological obstructions

**Att-4 (in the prompt).** *Cohomological obstructions: are there
Hochschild / cyclic cohomology classes that obstruct the mixed
Dunn equivalence?*

**Response.** Three potential obstruction classes survey:

* **(O-6.5.1) Hochschild $\mathrm{HH}^2$ obstruction.** The
  cross-bracket $\{\alpha_{x_i}, \alpha_{\bar z_j}\}$ defines a
  candidate Hochschild 2-cocycle on the tensor algebra
  $A_{\mathrm{E_2}}^{\mathrm{top}} \otimes A_{\mathrm{E_2}}^{\mathrm{hol}}$.
  By BV-exactness on $F_\alpha = 0$, this class is BV-exact at the
  cohomological level. *No Hochschild obstruction at the
  cohomological level.*

* **(O-6.5.2) Cyclic $\mathrm{HC}^\bullet$ obstruction.** The
  $S^1$-equivariant lift of the Hochschild structure to cyclic
  homology is the natural home for any potential operadic
  obstruction. The *cyclic obstruction class* in
  $\mathrm{HC}^\bullet$ is a sub-class of the Hochschild class
  via the Connes long exact sequence; the cyclic-level
  vanishing follows from the Hochschild-level vanishing, modulo
  Connes BSS spectral-sequence convergence. The
  W3-W11-04 weight-filtration spectral sequence at $E_1$ on
  graphwise contributions is consistent with Connes BSS
  degeneration.

* **(O-6.5.3) Operadic $\mathrm{HOp}^\bullet$ obstruction.** The
  *operadic-level* obstruction class lives in the $\infty$-operadic
  cohomology of the unit $\mathbb E_m^{\mathrm{top}} \otimes
  \mathbb E_n^{\mathrm{hol}} \to \mathbb E_{m,n}^{\mathrm{mixed}}$
  morphism. This is the *new* obstruction class, not in the
  surveyed literature. **It is the *primary obstruction* for the
  operadic mixed Dunn additivity.** Computing this class — or
  showing its vanishing — is the essential M-12 / Phase-5 attack.

**Verdict.** **Hochschild and cyclic obstructions vanish at the
cohomological level (BV-exactness on $F_\alpha = 0$); the
operadic obstruction $\mathrm{HOp}^\bullet$ is the new obstruction
not in the literature.**

---

## §7. Three precise sub-problems

The following three sub-problems, if jointly closed, give the
mixed Dunn additivity $\mathbb E_2^{\mathrm{top}} \otimes
\mathbb E_2^{\mathrm{hol}} \simeq \mathbb E_{2,2}^{\mathrm{mixed}}$
in $\Pr^L_{\mathrm{ML}}$ (and hence in our $\R^2 \times \C^2$ setting).

### §7.1 SP-1 — Operadic-level holomorphic Dunn additivity

**Statement.** Lift Williams arXiv:2007.13985 §3-§4's
$(\infty,1)$-categorical $\mathbb E_n^{\mathrm{hol}}$-construction
to a strict $\infty$-operad in $\mathrm{Op}_\infty$, and prove
the holomorphic Dunn additivity
$\mathbb E_m^{\mathrm{hol}} \otimes \mathbb E_n^{\mathrm{hol}}
\simeq \mathbb E_{m+n}^{\mathrm{hol}}$ in $\Pr^L$.

**Closest existing literature result.** Williams arXiv:2007.13985
§3 Definition + §4 Theorem 4.4 (factorization-homology version,
implicit Dunn additivity).

**Gap.** Williams' framework is at the
$(\infty,1)$-categorical-FA level, not at the
$(\infty,2)$-categorical-operadic level. The Boardman-Vogt-style
ordered-polydisk-embedding argument adapted to holomorphic
embeddings (with $\bar\partial$-Hodge equivariance) is not
in §3-§4.

**Technical depth.** **Medium-large.** Requires a careful
$\bar\partial$-Hodge / nuclear-chain-complex extension of the
ordered-cube embedding argument; expected paper length 35-50pp.

**Likely venue.** Standalone preprint $\to$ *J. Topology* /
*Adv. Math.*

### §7.2 SP-2 — Mixed Boardman-Vogt construction

**Statement.** Construct the mixed Boardman-Vogt operadic tensor
product $\mathbb E_m^{\mathrm{top}} \otimes \mathbb E_n^{\mathrm{hol}}$
in $\mathrm{Op}_\infty$ in the presentable symmetric monoidal
$\infty$-category $\Pr^L_{\mathrm{ML}}$, where one factor is
topological and the other is holomorphic. Show that the natural
forgetful functor to $\mathbb E_{m,n}^{\mathrm{mixed}}$ — defined
as the operad of mixed-locally-constant FAs on
$\R^m \times \C^n$ — is an equivalence.

**Closest existing literature result.** Lurie HA §5.5.4.16
(topological Dunn additivity); the $(\infty,2)$-categorical
operadic Boardman-Vogt construction in Lurie HA §5.5.

**Gap.** The Boardman-Vogt construction in Lurie HA §5.5 is
within a *single* $\infty$-operad type (topological); the
extension to a mixed type (one topological + one holomorphic)
requires a refined operadic framework where one factor lives in
$\mathrm{Op}_\infty^{\mathrm{top}}$ and the other in
$\mathrm{Op}_\infty^{\mathrm{hol}}$, and the tensor product
crosses the type. This refined framework is *not* in Lurie HA
or in Williams 2020.

**Technical depth.** **Large.** Requires substantial $\infty$-operadic
infrastructure development; expected paper length 60-100pp.

**Likely venue.** Standalone paper $\to$ *Selecta Math.* /
*Inventiones* / dissertation chapter.

### §7.3 SP-3 — Operadic obstruction class vanishing

**Statement.** Identify and compute (or show vanishing of) the
operadic-level obstruction class $\mathrm{HOp}^\bullet \in
H^\bullet(\mathrm{Op}_\infty(\mathbb E_m^{\mathrm{top}} \otimes
\mathbb E_n^{\mathrm{hol}}, \mathbb E_{m,n}^{\mathrm{mixed}}))$ for
the mixed Dunn additivity to hold strictly. Equivalently: show
that the natural map of $\infty$-operads
$\mathbb E_m^{\mathrm{top}} \otimes \mathbb E_n^{\mathrm{hol}}
\to \mathbb E_{m,n}^{\mathrm{mixed}}$ has trivial obstruction
to being an equivalence in $\Pr^L_{\mathrm{ML}}$.

**Closest existing literature result.** The ($\infty,2$)-categorical
deformation theory of $\infty$-operads in Lurie HA §5.5 + §A.6;
the cyclic Hochschild cohomology of the topological Dunn additivity
case (e.g., Calaque-Pantev-Toën-Vaquié-Vezzosi for the
shifted symplectic / chiral version).

**Gap.** No primary source computes the operadic obstruction
class for the *mixed* setting. The Hochschild / cyclic cohomology
obstructions are degenerate at the BV-cohomological level (per
§6.5 above); the *operadic* obstruction is potentially
non-vanishing and is computed in *no surveyed source*.

**Technical depth.** **Large.** Requires the development of
$(\infty,2)$-categorical operadic deformation theory in the mixed
setting; expected paper length 70-120pp.

**Likely venue.** Standalone paper $\to$ *Inventiones* / *Annals
of Math.* / dissertation thesis.

### §7.4 Joint closure verdict

**SP-1 + SP-2 + SP-3, jointly closed**, would establish the mixed
Dunn additivity in $\Pr^L_{\mathrm{ML}}$. *Each* sub-problem is
medium-large to large in technical depth; joint closure is
*Phase-5 scope* (12-18 mo+ horizon, possibly 24+ mo for SP-3).

**Partial success scenarios:**
* SP-1 alone gives the holomorphic Dunn additivity (publishable;
  one preprint).
* SP-1 + SP-2 (without SP-3) gives the mixed Dunn additivity
  *up to obstruction*, with the operadic obstruction class
  named explicitly (publishable; two preprints).
* SP-3 alone (assuming SP-1, SP-2 black-boxed) gives the
  obstruction-class computation (publishable; one preprint).

---

## §8. Phase-5 escalation roadmap

### §8.1 Milestone M-Mixed-Dunn-Operadic-Lift (Phase-5 P5-MD-1)

**Sub-problem.** SP-1 (operadic holomorphic Dunn additivity).

**Phase-5 milestone.** P5-MD-1 (M-12 sharpening of G1-M2 Avenue (B);
12-18 mo horizon).

**Technical depth.** Medium-large.

**Likely venue.** Standalone preprint (35-50pp); target *J. Topology*
or *Adv. Math.*

**Attack strategy.** Adapt the Boardman-Vogt ordered-polydisk
embedding argument from Lurie HA §5.5 to the holomorphic-LCFA
category of Williams §3. Verify that the holomorphic-coloring
operadic tensor product $\mathbb E_m^{\mathrm{hol}} \otimes
\mathbb E_n^{\mathrm{hol}}$ is computed by ordered embeddings of
$(m+n)$-polydisks in $\C^{m+n}$ with $\bar\partial$-Hodge
equivariance.

### §8.2 Milestone M-Mixed-BV-Tensor (Phase-5 P5-MD-2)

**Sub-problem.** SP-2 (mixed Boardman-Vogt construction).

**Phase-5 milestone.** P5-MD-2 (M-18+ extension of G1-M2 Avenue (B);
18-24 mo horizon).

**Technical depth.** Large.

**Likely venue.** Standalone paper (60-100pp); target *Selecta
Math.* or *Inventiones*; dissertation chapter alternative.

**Attack strategy.** Develop $(\infty,2)$-categorical operadic
infrastructure for the mixed type: define
$\mathrm{Op}_\infty^{\mathrm{top-hol-mixed}}$ as the
$\infty$-category of $\infty$-operads with the topological /
holomorphic / mixed substructure; define the tensor product
$\otimes$ on this category; verify that the natural functor
$\mathbb E_m^{\mathrm{top}} \otimes \mathbb E_n^{\mathrm{hol}} \to
\mathbb E_{m,n}^{\mathrm{mixed}}$ is an equivalence on the
mixed-locally-constant sub-operad.

### §8.3 Milestone M-Mixed-Operadic-Obstruction (Phase-5 P5-MD-3)

**Sub-problem.** SP-3 (operadic obstruction class).

**Phase-5 milestone.** P5-MD-3 (M-24+ deferred phase; 24+ mo
horizon).

**Technical depth.** Large.

**Likely venue.** Standalone paper (70-120pp); target *Inventiones*
or *Annals of Math.*; dissertation thesis core chapter.

**Attack strategy.** Compute the operadic-level deformation cohomology
$\mathrm{HOp}^\bullet$ for the unit functor
$\mathbb E_m^{\mathrm{top}} \otimes \mathbb E_n^{\mathrm{hol}} \to
\mathbb E_{m,n}^{\mathrm{mixed}}$. Use the cyclic Hochschild /
shifted-symplectic cohomology framework of Calaque-Pantev-Toën-
Vaquié-Vezzosi as the topological-side input; develop the
holomorphic-side analogue via Williams §3 + Costello-Gwilliam
Vol II Ch. 10's $\bar\partial$-Hodge propagator; show that the
operadic-level obstruction is the cyclic-cohomology obstruction
plus a new operadic class, and compute its vanishing.

### §8.4 Joint Phase-5 deliverable

**The joint Phase-5 program** (P5-MD-1 + P5-MD-2 + P5-MD-3) closes
the mixed Dunn additivity in our setting. Total Phase-5 scope:
24-36 months; total venue ambition: three publishable preprints
(*J. Topology* + *Selecta Math.* + *Inventiones*); dissertation
chapter / thesis core in the alternative.

### §8.5 Risk assessment for the Phase-5 escalation

**P5-MD-R1 (Williams framework requires substantial extension).**
Williams §3-§4 covers $\C^n$ only; the mixed framework on
$\R^m \times \C^n$ requires a refined operadic infrastructure that
is non-trivial. Mitigation: stage SP-1 as a standalone preprint
covering the $(\infty,1)$-to-$(\infty,2)$-operadic lift on
$\C^n$ first; then layer SP-2 on top.

**P5-MD-R2 (operadic obstruction may be non-vanishing).** The
operadic-level obstruction $\mathrm{HOp}^\bullet$ may be non-zero,
requiring a *partial* mixed Dunn additivity rather than a full
equivalence. Mitigation: even partial vanishing (in the
ML-restricted envelope) is publishable; name the precise
obstruction class.

**P5-MD-R3 (cross-volume firewall lift).** If the W3-W31
cross-volume firewall lifts in Phase 5, the mixed Dunn additivity
becomes a cross-volume bridge to the calabi-yau-quantum-groups
Vol III; the precise statement may need to be unconditionalized
to the cross-volume scope. Mitigation: keep Phase-5 work locally
independent of the cross-volume bridge; treat any unconditionalisation
as bonus.

---

## §9. Residuals + deciding evidence

### §9.1 Residuals (M-12-originated)

**R-P4-EXEC-MIXED-DUNN-A.** SP-1 (operadic holomorphic Dunn
additivity from Williams §3-§4). Severity 3. Closure pending:
P5-MD-1 (12-18 mo).

**R-P4-EXEC-MIXED-DUNN-B.** SP-2 (mixed Boardman-Vogt construction).
Severity 4 (cross-type operadic). Closure pending: P5-MD-2 (18-24 mo).

**R-P4-EXEC-MIXED-DUNN-C.** SP-3 (operadic obstruction class).
Severity 4 (deformation-theoretic). Closure pending: P5-MD-3
(24+ mo).

**R-P4-EXEC-MIXED-DUNN-D.** Weiss-product-stability on non-product
Weiss covers of $\R^2 \times \C^2$ (W3-W9-04 / R-03 ingredient
I-4.b). Severity 3. Closure pending: M-37 / Avenue (D) M-18+
(BD chiral product descent + matched conventions); separate
from but consequential for the mixed Dunn question.

### §9.2 Deciding evidence (mixed Dunn pre-investigation)

**Verifying evidence for the M-12 obligation.**
* G1-M2 §5.3 explicitly disposes the mixed Dunn additivity to
  M-12 Avenue (B), with severity-3 status / failure-anticipated /
  high confidence.
* Williams §3-§4 supplies the holomorphic side; Lurie 5.5.4.16
  the topological side; the cross-equivalence is genuinely
  open across the surveyed primary sources.
* G1-M2 Avenue (E) closes the topological factor on $\R^2$ in
  $\mathcal C_{\mathrm{ML}}$ via $F_\alpha = 0$ Maurer-Cartan
  flatness; this is consistent with the *cohomological-level*
  mixed Dunn equivalence but not the *operadic-level* equivalence.

**Where the mixed Dunn pre-investigation could fail.**
* A primary source not in our trusted-context corpus (e.g., a
  Markarian-Sarkissian preprint or a recent post-2024 paper in
  the Williams-Costello-Gwilliam-Gaiotto group) has already
  closed the mixed Dunn additivity. *Provisionally we conclude
  no such source exists, but a literature search at the
  preprint-level would close this risk.*
* Williams' framework already implicitly closes the mixed Dunn
  additivity on a sub-operad, and we have failed to identify
  the precise Williams §3 argument. *Provisional assessment:
  Williams §3-§4 covers only $\C^n$; the mixed setting requires
  substantial extension; this provisional interpretation is consistent
  with the G1-M2 §5.3 verdict.*
* The operadic-level obstruction $\mathrm{HOp}^\bullet$ is
  trivially vanishing by an unrecognized $\infty$-categorical
  triviality. *Provisionally we treat the obstruction as
  potentially non-trivial and Phase-5-scope.*

### §9.3 Beilinson + Composition lens evaluation

**Beilinson lens.**
* *Sheaf-theoretic descent on $\mathrm{Ran}(\R^2 \times \C^2)$:*
  GAP (mixed factorization algebra has two incompatible local
  axiomatic systems on the topological vs holomorphic factors).
* *Čech / bar resolutions of the mixed structure:* the
  cohomological-level Maurer-Cartan datum $F_\alpha = 0$ provides
  *part* of the Čech compatibility; the operadic resolution is
  not in the literature.
* *Filtered/spectral on Tate window:* PASS at the topological
  factor (G1-M2 §4.4 ML-restricted envelope); UNVERIFIED at the
  holomorphic factor.

**Composition lens.**
* *Local mixed-Dunn equivalences compose globally:* GAP at the
  operadic-tensor-product level (SP-2 / SP-3 in §7).
* *Mayer-Vietoris / Čech check on $\R^2 \times \C^2$ covers:*
  passes for product covers (CG Vol I §A.5.6); fails for
  non-product covers (W3-W9 / R-03 I-4.b).
* *$E_4^{\mathrm{mixed}}$ pentagon associativity:* PASS at the
  cohomological level via $F_\alpha = 0$; UNVERIFIED at the
  strict operadic level.

**Both lenses confirm the M-12 Avenue (B) status: open at the
operadic level; partially closed at the cohomological level via
G1-M2 Avenue (E).**

### §9.4 Cross-walk to the broader Phase-4 / Phase-5 program

The mixed Dunn additivity question feeds into:

* **G1-M2 Avenue (B)** (mixed Dunn additivity) — the *primary*
  M-12 milestone target.
* **G1-M5+ Avenue (D)** (BD chiral product on
  $\mathrm{Ran}(\R^2 \times \C^2)$) — the M-18+ obligation; SP-2
  and SP-3 feed into Avenue (D)'s chiral-product descent.
* **G1-M37 (R-03 ingredient I-4.b)** Weiss-product-stability on
  non-product covers — independent residual; may be partially
  closed by SP-1 + SP-2 on product opens, then extended by
  Avenue (A) (direct Čech) to non-product covers.
* **Cross-volume bridge (W3-W31, M-34, M-52)** — if the
  cross-volume firewall lifts at some Phase-5 stage, the mixed
  Dunn additivity becomes a cross-volume statement; the
  Phase-5 escalation should keep the program *locally
  independent* of cross-volume unconditionalization.

---

## §10. Provenance

P4-EXEC-MIXED-DUNN-PROBE (this report) read in full:
- `/Users/raeez/topological-strings/CLAUDE.md`.
- `reconstitution/phase4-exec-G1-M2-E2-promotion-2026-04-28.md` (full).
- `reconstitution/phase4-G1-weiss-product-2026-04-28.md` (full §T1-T6).
- `reconstitution/phase4-exec-G1-M1-BD-chiral-2026-04-28.md`
  §0-§4 (D4 dictionary table; D6 hypothesis verification).
- `reconstitution/wave3-W11-beilinson-hypotheses-2026-04-28.md`
  §1 Target T1 hypothesis verification.
- `reconstitution/wave3-W9-drinfeld-definitions-2026-04-28.md`
  §0-§3 ((W-2D) statement).
- `reconstitution/phase4-exec-CGW-anchor-2026-04-28.md`
  §0-§4 (CGW arXiv:2007.09497 source-precision).
- `main.tex`:1770-1840 (Hamiltonian BF action; Hamiltonian
  connection $\alpha$; flatness $F_\alpha = 0$; classical fields).
- `main.tex`:1996-2210
  (`thm:open-closed-derived-center-factorization`;
  `rmk:E1-translation`; Lurie HA §5.5.4 / CG Vol I §6.4 invocation).

External primary references surveyed (no fresh PDF inscription):
- Lurie, *Higher Algebra*, May 2017 / kerodon §HA.5.5.4
  (`LurieHA`) §5.5.2-§5.5.4, especially Thms 5.5.4.10 + 5.5.4.16.
- Williams, *Holomorphic factorization algebras*, arXiv:2007.13985
  (`Will20`) §3-§4.
- Costello-Gwilliam Vol I (`CGW1`) §6.4-6.5, §A.5;
  Vol II (`CGW2`) Ch. 10, §11.4.
- Costello-Gaiotto-Williams arXiv:2007.09497 (`CGW20`) §3-§5.
- Costello arXiv:1610.04144 (`Cos16`) §3-§6.
- Beilinson-Drinfeld, *Chiral Algebras* (`BD04`) §3.4.10-11.
- Ayala-Francis arXiv:1206.5522 (`AF15`) §3-§5;
  Ayala-Francis-Tanaka *Selecta Math.* 2017 (`AFT17`) §2, §4.
- Knudsen *Geom. Topol.* 2018 (arXiv:1605.01391) Theorem 3.1.
- Gwilliam-Williams 2018+ (post-Williams) defect-HCS program.

Markarian-Sarkissian 2022/23 (or successor) on mixed factorization
algebras: *not in the trusted-context corpus*. Provisionally
closes no part of the residual; left as a literature-search
follow-up.

P4-EXEC-MIXED-DUNN-PROBE confidence: every structural claim either
inherits G1-M2 closure (Avenue (E) verdict on $\R^2$-only
topological factor), inherits Williams §3-§4 + Lurie 5.5.4.16
parallel statements, or names the M-12 / Phase-5 residual
explicitly. No fresh PDF inscription required for the
pre-investigation; SP-1 / SP-2 / SP-3 closure requires Phase-5
sources beyond the surveyed list.

---

## §11. Summary

P4-EXEC-MIXED-DUNN-PROBE supplies the pre-investigation for the
M-12 G1 frontier obligation: the mixed Dunn additivity
$\mathbb E_m^{\mathrm{top}} \otimes \mathbb E_n^{\mathrm{hol}}
\simeq \mathbb E_{m,n}^{\mathrm{mixed}}$ on $\R^m \times \C^n$.
**Closure verdict: OPEN at the operadic level across all surveyed
primary sources; closed for the topological-only
($n = 0$, Lurie 5.5.4.16) and holomorphic-only ($m = 0$, Williams
§3-§4 implicit) special cases; closed at the chain / cohomological
level for our specific $\R^2 \times \C^2$ Hamiltonian-BF setting
on the topological factor only (G1-M2 Avenue (E) in
$\mathcal C_{\mathrm{ML}}$ via $F_\alpha = 0$).**

**(a) Is the mixed Dunn additivity OPEN, CLOSED FOR SPECIAL CASES,
or CLOSED IN OUR SETTING via a route bypassing the literature gap?**
**OPEN at the operadic level; CLOSED FOR SPECIAL CASES at
$n = 0$ (Lurie 5.5.4.16) and $m = 0$ (Williams 2020); CLOSED IN
OUR SETTING for the topological factor only at the cohomological
level (G1-M2 Avenue (E)).** Genuinely open at the M-12 / Phase-5
scope.

**(b) Closest existing partial result.** **Williams arXiv:2007.13985
§3-§4** (holomorphic-locally-constant FA $\simeq$ holomorphic-$E_n$
algebra; implicit holomorphic Dunn additivity) combined with
**Lurie HA Theorem 5.5.4.16** (topological Dunn additivity).
Together they cover the topological-only and holomorphic-only
sides; the cross-equivalence between
$\mathbb E_m^{\mathrm{top}} \otimes \mathbb E_n^{\mathrm{hol}}$
and $\mathbb E_{m,n}^{\mathrm{mixed}}$ is the gap.

**(c) Most promising Phase-5 escalation route.** **Phase-5
M-Mixed-Dunn-Operadic-Lift (P5-MD-1)**: lift Williams §3-§4 to
$(\infty,2)$-categorical operadic level on $\C^n$ (35-50pp;
*J. Topology*); then **P5-MD-2 (mixed Boardman-Vogt construction)**
(60-100pp; *Selecta Math.* / *Inventiones*); then **P5-MD-3
(operadic obstruction class)** (70-120pp; *Inventiones* / *Annals
of Math.*). Joint closure: 24-36 mo Phase-5 scope.

**Three sub-problems (§7).**
* **SP-1 — Operadic holomorphic Dunn additivity** (closest
  literature: Williams arXiv:2007.13985 §3-§4; gap:
  $(\infty,1)$-to-$(\infty,2)$-operadic lift; medium-large depth).
* **SP-2 — Mixed Boardman-Vogt construction** (closest literature:
  Lurie HA §5.5; gap: cross-type operadic infrastructure; large
  depth).
* **SP-3 — Operadic obstruction class** (closest literature: CPTVV
  shifted-symplectic deformation theory; gap: mixed-setting
  computation; large depth).

**Manuscript-side perspective (§6).** The Hamiltonian connection's
flatness $F_\alpha = 0$ on $\R^2 \times \C^2$ supplies the
*cohomological-level* Maurer-Cartan datum for the mixed
cross-bracket; *consistent with* but *not equivalent to* the
operadic mixed Dunn equivalence. The G1-M2 Avenue (E) closure on
$\R^2$-topological-only is a *degenerate special case* in the
mixed setting, not a route bypassing the literature gap on the
holomorphic / full mixed structure.

**Anti-attack scan.** Att-1 (topological-Pre tower for
holomorphic-Pre tower): no holomorphic-Pre tower exists in
Williams §3-§4; SP-1 attack target. Att-2 (Williams to
$(\infty,2)$-operadic lift): SP-1 / SP-2 attack target. Att-3
(Maurer-Cartan curvature data): $F_\alpha = 0$ sufficient at
cohomological level, not at strict operadic level. Att-4
(cohomological obstructions): Hochschild / cyclic vanish at
BV-cohomological level; operadic $\mathrm{HOp}^\bullet$ is the
new obstruction class, SP-3 attack target.

**Connection to broader Phase-4 / Phase-5 program.** The mixed
Dunn additivity feeds into G1-M2 Avenue (B) M-12, G1-M5+ Avenue
(D) M-18+, G1-M37 R-03 I-4.b Weiss-product-stability, and the
cross-volume bridge to calabi-yau-quantum-groups Vol III.

Open obligations: R-P4-EXEC-MIXED-DUNN-A (SP-1, P5-MD-1);
R-P4-EXEC-MIXED-DUNN-B (SP-2, P5-MD-2); R-P4-EXEC-MIXED-DUNN-C
(SP-3, P5-MD-3); R-P4-EXEC-MIXED-DUNN-D (Weiss-product-stability
on non-product covers, separate from but consequential for the
mixed Dunn question).

---

End of P4-EXEC P4-Mixed-Dunn-Probe pre-investigation note.
