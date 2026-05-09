# Wave 3 / W2 — Gaiotto + Boundary Lens

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Gaiotto (defects, interfaces, generalized symmetries,
category-valued structures, dimensional reduction, boundary VOAs)
+ Boundary (zero/infinity, empty input, singular strata, partial
migrations).
**Inputs.** Master ledger
`reconstitution/attack-heal-platonic-2026-04-28.md` items M-14,
M-19, M-31, M-37, R-W6-Weiss-defect, R-03; W6 wave-2 report
(`reconstitution/wave2-W6-beilinson-2026-04-28.md`) §0–§5;
`appendix-factorization-current-conventions.tex` (full);
`tate-T3-quillen-equivalence.tex` 510–589;
`tate-P5-cross-volume.tex`; `principles.tex`;
`main.tex` 247–472, 1908–2218, 2741–2756, 3580–3700;
`open-obligations.tex` items 5, 6, 8.
**Mode.** Proposal-only. No commits. Master ledger schema; IDs
W3-W2-NN.
**Independence.** Wave-2 W6's eight-link DAG (M-33) is taken as
**input under attack** through the Gaiotto/Boundary lens. The
deliverable is a defect-line decomposition of the Weiss-cosheaf
condition with explicit zero / infinity / partial-migration audit,
and a precise statement of where the M-31 BV/CE identification fails
to extend to defect cohomology.

---

## §0. Distinguishing two locality conditions: Weiss vs locally constant

The wave-2 W6 deliverable conflates two distinct cosheaf conditions
in places where the Gaiotto lens demands they be separated.

**Locally constant condition (Lurie HA §5.5.4 / CG Vol. I §6.4).**
On $\R$: a prefactorization algebra $\mathcal F$ is locally constant
if every interval inclusion $I'\hookrightarrow I$ induces a
quasi-isomorphism $\mathcal F(I')\xrightarrow{\sim}\mathcal F(I)$.
This is a **structure-map condition on intervals**, no covers
involved. It is the one used in Steps 6–7 of
`thm:open-closed-derived-center-factorization`
(`main.tex`:2174–2184) and in W6-L6 / W6-L8.

**Weiss cosheaf condition (CG Vol. I §6.5, Vol. II §A.5).**
For a Weiss cover $\mathcal U$ of $V$ (a cover such that every
finite collection of points of $V$ lies in some $U\in\mathcal U$),
the natural map
$$\check{\mathrm C}^\bullet(\mathcal U;\mathcal F)
  \xrightarrow{\sim}\mathcal F(V)$$
is a quasi-isomorphism. This is a **descent condition on Weiss
covers**, a strictly stronger requirement than locally constant
descent on intervals. It is what `prop:weiss-cosheaf-residual`
(T3 lines 530–563) flags as residual on $\R^2\times\C^2$.

**W3-W2-01 (lens-driven distinction).** W6's L6 (locally constant
descent on $\R$, `main.tex`:2174–2184) is *not* the Weiss-cosheaf
condition. L6 is verified at the cohomological level by
`lem:derivative-jets`. The Weiss condition on $\R$ for the same FA
is a separate, in-principle stronger statement — but it reduces to
the locally constant condition once the FA has been promoted to a
cosheaf on the open intervals via extension by zero, **provided
that disjoint-support locality holds** (W6-L7,
`prop:brane-bracket-locality`, `main.tex`:1965–1979). On $\R$ this
reduction is in CG Vol. I §6.4–6.5 and does not require the
heat-kernel propagator. **On $\R^2\times\C^2$ the Weiss condition
genuinely requires more (the analytic propagator and the defect
boundary condition).**

Conclusion: the Weiss condition for the brane-line factorization on
$\R$ alone is *not* an outstanding obligation; it is healed by
combining W6-L6 with W6-L7, both of which W6 verified. What
remains as `R-W6-Weiss-defect` is genuinely the higher-dimensional
$\R^2\times\C^2$ Weiss problem, which is what M-37 named four
ingredients for. **The W3 contribution here is to make this
separation explicit and to flag a prose risk in the manuscript.**

**Manuscript prose risk.** `main.tex`:1996–2191
(`thm:open-closed-derived-center-factorization` proof Step 7,
particularly lines 2174–2184) writes:

> "Hence the structure maps for inclusions of intervals are
> quasi-isomorphisms on both sides; the $E_1$-equivalent associative
> algebra structure is the underlying graded-commutative product on
> the stalk".

This proves locally constant; it does not prove Weiss descent. If
a future reader confuses the two, they may believe Step 7 has
proved more than it has. The fix is editorial: insert one sentence
distinguishing the two notions (proposed as W3-W2-H1 below).

---

## §1. Target T1 — R-W6-Weiss-defect: the precise condition

### §1.1 The Weiss condition for the locally constant FA on $\R$

For the brane-line FA $A_\partial^{\mathrm{Ham}}(I) =
\widehat{\mathbf S}(\mathfrak h_I)$ with $\mathfrak h_I =
\Omega^\bullet_c(I)\widehat\otimes\bar A$
(`main.tex`:1914–1962, `appendix-factorization-current-conventions.tex`:12–35)
and Weiss cover $\mathcal U = \{U_\alpha\}$ of an open
$V\subset\R$, the Weiss-cosheaf condition reads
$$\mathrm{Tot}\,\check{\mathrm C}^\bullet
  \bigl(\mathcal U;A_\partial^{\mathrm{Ham}}\bigr)
  \xrightarrow{\sim}A_\partial^{\mathrm{Ham}}(V),
\tag{W-1d}$$
where the Čech complex is the bar resolution of multi-disjoint
inclusions $U_{\alpha_0}\sqcup\cdots\sqcup U_{\alpha_p}\subset V$
with the alternating differential of multi-disjoint extension by
zero.

**W3-W2-02 (verification of (W-1d)).** Both sides of (W-1d) are
free graded-commutative on completed Tate vector spaces:
$\widehat{\mathbf S}(\mathfrak h_V)$ on the right;
$\mathrm{Tot}\,\check{\mathrm C}^\bullet(\mathcal U;\mathfrak h)$
on the left, where the cosheaf is
$U\mapsto\mathfrak h_U=\Omega^\bullet_c(U)\widehat\otimes\bar A$.
**Key reduction:** the symmetric-algebra functor
$\widehat{\mathbf S}$ commutes with the totalisation of the Čech
double complex when applied to a cosheaf with surjective extension
maps and Mittag-Leffler condition on the directed system (Roos
1961; CG Vol. I §A.5.4). Applying this:
$$\mathrm{Tot}\,\check{\mathrm C}^\bullet
  \bigl(\mathcal U;\widehat{\mathbf S}(\mathfrak h_-)\bigr)
  \;\simeq\;
  \widehat{\mathbf S}\bigl(\mathrm{Tot}\,
    \check{\mathrm C}^\bullet(\mathcal U;\mathfrak h_-)\bigr).$$
Now (W-1d) reduces to verifying the underlying Weiss-cosheaf
condition for the cosheaf $\mathfrak h_-$ on $\R$:
$$\mathrm{Tot}\,\check{\mathrm C}^\bullet
  \bigl(\mathcal U;\mathfrak h\bigr)
  \xrightarrow{\sim}\mathfrak h_V.
\tag{W-1d-h}$$
Because $\Omega^\bullet_c$ is a cosheaf in the sense of CG Vol. I
§A.5 (with extension by zero as cosheaf structure maps and the
Čech complex computing $\Omega^\bullet_c(V)$ from any open cover),
and because $\bar A$ is a discrete vector space, the completed
tensor product $\Omega^\bullet_c\widehat\otimes\bar A$ inherits the
cosheaf condition. Hence **(W-1d-h) holds**, and therefore (W-1d)
holds.

**Source.** CG Vol. I §6.4 Example 6.4.0.5 (locally constant FAs
on $\R$ are Weiss); §6.5 (Weiss covers); §A.5.4 (cosheaves on
manifolds). Lurie HA §5.5.4.10 (locally constant FAs on $\R^n$
$\simeq E_n$-algebras, hence automatically Weiss because Weiss is
implicit in Lurie's definition via factorizable presheaves).

**W3-W2-03 (discharge).** R-W6-Weiss-defect, **as stated for the
brane-line factorization on $\R$**, is **discharged**: (W-1d-h)
and the symmetric-algebra commutation give (W-1d) directly, with
no extra analytic input. The genuine residual lives at the
ambient $\R^2\times\C^2$ level, which is what the wave-2 W6-07 /
M-37 sharpening already restated: the four ingredients name what
is missing for $V\subset\R^2\times\C^2$, and the genuinely
obstructed piece is transverse Mittag-Leffler on
defect-localised distributions (the codim-4 holomorphic resolution
problem).

### §1.2 What survives as R-W6-Weiss-defect

The **residual proper** is the Weiss-cosheaf condition on
$\R^2\times\C^2$ for the unreduced factorization algebra
$\mathrm{Obs}^{\mathrm{cl}}_{\mathrm{closed},H}$. The brane-line FA
on $\R$ is fine. The standing M-37 four-ingredient list is the
correct statement of what's needed.

**W3-W2-04 (sharpening of M-37 ingredient 4).** The transverse
Mittag-Leffler ingredient is the *only* one that is genuinely
beyond standard Costello-RG. The other three (heat-kernel
propagator, defect boundary condition, bulk-to-defect kernel) are
present in Costello *Renormalization and Effective Field Theory*
2011, Ch. 9–10 (heat-kernel apparatus on $\R^n$),
Costello–Gwilliam Vol. II Ch. 11 (holomorphic Chern–Simons +
defect), and Costello–Gaiotto–Williams *Twisted Supergravity*
arXiv:2007.09497 (5d twisted M-theory + defects). The fourth is a
**Beilinson–Drinfeld chiral-algebra factorization** problem:
principal-part fields $\rho_{a,b}$ are residue currents on the
codim-4 holomorphic subspace $\R\times\{0\}\subset\R\times\C^2$,
and their Mittag-Leffler resolution requires either a
$\bar\partial$-Hodge construction transverse to the brane (which
is non-trivially obstructed by support on the codim-4 subspace) or
a chiral-algebra factorization via BD §3.4.

**No change to W6-07 / M-37.** This sharpening confirms the
within-reach / beyond-reach decomposition; it does not require
re-statement of the residual.

### §1.3 What's actually verified in the manuscript

Tracing line by line through the manuscript proofs:

* **W6-L1 (cosheaf-of-Lie):** verified, `constr:interval-fact-algebras`
  `main.tex`:1914–1935.
* **W6-L7 (disjoint-support locality):** verified,
  `prop:brane-bracket-locality` `main.tex`:1965–1979 and
  `rmk:equal-time-locality` `main.tex`:1981–1994.
* **W6-L6 (locally constant descent):** verified at the
  cohomological level via `lem:derivative-jets` (in
  `thm:open-closed-derived-center-factorization` Step 7,
  `main.tex`:2174–2184).
* **Weiss for brane-line on $\R$:** **discharged here**
  (W3-W2-02, W3-W2-03) via the symmetric-algebra/cosheaf reduction
  + Roos ML.

The path Weiss-on-$\R$ → unreduced-Weiss-on-$\R^2\times\C^2$
remains genuinely open (R-W6-Weiss-defect proper); the four
ingredients of M-37 stand.

---

## §2. Target T2 — Brane defect locality (Diracian principle II)

The Dirac principle (`principles.tex`:13–55) supplies a
constrained probe with $Q\psi = [\phi_1,\phi_2]$ and moment map
$\mu_\epsilon = -\mathrm{Tr}(\epsilon[\phi_1,\phi_2])$. The
question: is the brane-defect locality actually proved, and does
the M-31 BV/CE identification ($[\mathrm{Tr}\,\psi]_{\mathrm{BV}}
\leftrightarrow [\bar c]_{\mathrm{CE}}$) extend to defect
cohomology?

### §2.1 Locality of the Dirac-probe defect

**What "defect locality" means.** Three notions, per
`main.tex`:520–586:
* (a) Support locality along the brane line: bracket of disjoint
  smearings is zero (proved by `prop:brane-bracket-locality`).
* (b) Topological locality in the brane direction:
  $L_v = [Q,\iota_v]$, positive jets exact (proved by
  `lem:derivative-jets`).
* (c) Formal holomorphic locality in $\C^2$: completed at $p$,
  $\bar\partial$-translations $Q$-exact (proved at the formal
  jet level, not the analytic propagator level).

**W3-W2-05 (locality (a) and (b) are proved, (c) is *formal*
locality, not analytic locality).** The defect-locality of the
Dirac probe is proved in (a)–(b) at the level of equal-time
brackets and jet contraction; (c) is proved only at the formal
disk level, not at any propagator scale. The M-37 ingredient 1
heat-kernel propagator is exactly what's needed to upgrade (c)
from formal to analytic locality on a Weiss cover of
$\R^2\times\C^2$. Inside the brane line $\R\times\{p\}$, (a) and
(b) suffice.

**Manuscript locus check.** `main.tex`:520–586 lists the three
notions and asserts their derivation; `principles.tex`:148–154
records the QME obstruction (the $\hbar N[\bar c]$ class). Wave-1
M-20 (already inscribed in the consolidation as healed) added an
explicit derivation of each locality notion from $Q$-exact
translation. The defect-locality proof is therefore complete *for
the brane-line FA*.

**No new defect-locality residual on $\R$.** Discharged.

### §2.2 Does $[\mathrm{Tr}\,\psi]_{\mathrm{BV}} \leftrightarrow
[\bar c]_{\mathrm{CE}}$ extend to defect cohomology?

The M-31 identification (`reconstitution/attack-heal-platonic-2026-04-28.md`:1612–1643)
states that the two sides are the **same anomaly line**: the
bidegree $(0,0)$ class in $H^2_{\mathrm{Lie}}(\bar A;\C)$ on the
closed CE side coincides with the BV class
$[\mathrm{Tr}\,\psi]_{\mathrm{BV}}$ on the open Dirac-probe side.
This is a **bulk identification**: Theorem C ($c^I\mapsto
\theta^I$, $u_I\mapsto O_I$) at the CE/PV level
(`main.tex`:1064–1070).

**W3-W2-06 (the crucial observation).** Defect cohomology is a
**different cohomology** from bulk CE / BV cohomology. Specifically:

* *Bulk BV cohomology:* $H^\bullet(\mathcal R_N^{GL_N}, Q)$
  computed at a fixed brane point. The class
  $[\mathrm{Tr}\,\psi]_{\mathrm{BV}}\in H^{-1}$ is a connected
  primitive odd class living in the unreduced (with-scalar-trace)
  cohomology (`main.tex`:2862–2864).
* *Defect cohomology* (in the Gaiotto sense): observables
  *attached to* the codim-5 defect $\R\times\{0\}\subset
  \R^2\times\C^2$, computed in the limit where the defect line
  is contracted to a point in the ambient theory. This is the
  *boundary VOA / vertex algebra of operators stuck to the
  defect*. It involves bulk-to-defect operations that the
  manuscript does not construct.

**The M-31 identification is a bulk-bulk identification.** The
closed CE class $[\bar c]$ is bulk on the closed (Hamiltonian BF)
side; $[\mathrm{Tr}\,\psi]_{\mathrm{BV}}$ is "bulk" on the open
side relative to the brane line (it's a boundary observable
*evaluated at a single point of the brane line*, which is the
zero-dimensional intersection of the brane with a generic
spectator point of $\R$). The identification asserts these two
0-dimensional classes correspond.

**Defect cohomology question.** A genuine defect-cohomology
extension would need:
1. A bulk-to-defect kernel $K_{\mathrm{bd}}$ on $\R^2\times\C^2$
   (which is M-37 ingredient 3).
2. A defect-localised class
   $[c]_{\mathrm{def}}\in H^\bullet(K_{\mathrm{bd}}^*\mathrm{Obs}^{\mathrm{cl}}_{\mathrm{closed},H})$
   on the brane line, recovered from $[\bar c]_{\mathrm{CE}}$
   under the kernel.
3. Verification that the open-side class
   $[\mathrm{Tr}\,\psi]_{\mathrm{BV}}$, viewed as a defect class
   under the brane-line stratification, matches.

None of (1)–(3) is proved in the manuscript. Specifically,
M-37 ingredient 3 (the bulk-to-defect kernel) is exactly the
piece that's beyond the locally proved core.

**W3-W2-07 (sharpened scope of M-31).** The M-31 identification
$[\mathrm{Tr}\,\psi]_{\mathrm{BV}}\leftrightarrow [\bar c]_{\mathrm{CE}}$
is **bulk-only**: it holds at the level of single-point
evaluations on the brane line $\R\times\{p\}$ and matches the
0-dimensional Lie-cohomological line on the closed side, via
Theorem C / `main.tex`:1066–1070. **It does not extend to a
defect-cohomology identification** in the Gaiotto sense (cosheaf
of vertex-algebra-like observables stuck to the codim-5 defect),
because no bulk-to-defect kernel has been constructed. Closure is
gated on M-37 ingredient 3 (= R-W6-Weiss-defect via R-03).

**Heal proposal W3-W2-H2 (sharpening of M-31 scope).** Add to the
M-31 inscription in the master ledger and to its anchor in
`principles.tex` Principle 1 / Theorem G remark:

> "The identification $[\mathrm{Tr}\,\psi]_{\mathrm{BV}}
> \leftrightarrow [\bar c]_{\mathrm{CE}}$ is at the bulk level
> (single-point evaluation on the brane line). A
> defect-cohomology identification — observables attached to the
> codim-5 defect $\R\times\{0\}\subset\R^2\times\C^2$ via a
> bulk-to-defect kernel — requires the kernel of M-37 ingredient
> 3 and is gated on R-W6-Weiss-defect. The bulk identification
> proved here is independent of that defect extension."

This does not invalidate M-31; it precisely scopes its claim.
**No new residual** beyond R-W6-Weiss-defect (which already
records the gated piece).

### §2.3 The brane defect probe and the locally constant condition

**W3-W2-08 (Boundary-lens check: empty input / partial migration).**
What happens to the Dirac probe at the boundary of input data?

* *Empty interval $I = \emptyset$*: $\mathfrak h_\emptyset =
  \Omega^\bullet_c(\emptyset)\widehat\otimes\bar A = 0$
  (`appendix-factorization-current-conventions.tex`:13–18 reads
  $\Omega^\bullet_c(I)$, but cosheaves require $\mathcal F(\emptyset)
  = $ unit object); $A_\partial^{\mathrm{Ham}}(\emptyset) =
  \widehat{\mathbf S}(0) = \C$ (the unit). **Consistent** with FA
  conventions.
* *Singleton interval $I = \{t_0\}$*: cosheaf via colim along
  shrinking intervals; $\Omega^\bullet_c(\{t_0\})$ is empty as a
  function space, but the *stalk* of the FA at $t_0$ is recovered
  by the locally constant condition (W6-L6) via shrinking
  intervals. This is exactly the Step 8 stalk recovery
  (`main.tex`:2185–2190), which gives
  $\Phi^{\mathrm{Ham}}_{\mathrm{fact}}|_{t_0} = L_{B_f}\in
  \mathrm{Hoch}^0(A_N^{\mathrm{pt}})$. **Consistent.**
* *Defect at $\infty$ on the brane line*: the brane line is
  $\R\cong\{\R\times\{p\}\}\hookrightarrow\R^2\times\C^2$, with
  $\R$ extending to $\pm\infty$. At the boundary $\partial\R\cup
  \{\infty\}$ of the one-point compactification, the
  cosheaf-of-Lie condition extends only if all observables are
  compactly supported, which is the manuscript's convention
  ($\Omega^\bullet_c$, $\mathcal D'_c$,
  `appendix-factorization-current-conventions.tex`:14, 47).
  **Consistent.**
* *Partial migration of brane line $\R\times\{p\}\to
  \R\times\{p'\}$*: this is the Hamiltonian flow of a closed
  Hamiltonian on $\C^2$; under the formal-disk model, all
  observables are completed at the original brane point $p$, so
  partial migration is *not* an operation in the formal disk
  model. **Outside the manuscript's scope**; would require a
  different completion. Not a defect of the formal model; the
  brane is *fixed* at $p\in\C^2$.

The Boundary-lens audit produces no new residual; all four
boundary conditions are consistent with the formal-disk model.

---

## §3. Target T3 — Interface and dimensional reduction

### §3.1 Interface to the punctured disk

The formal symplectic disk
$\widehat{\C^2}_0 = \mathrm{Spf}\,\C[[z_1,z_2]]$ has a natural
**interface** to the punctured disk
$\widehat{\C^2}_0\setminus\{0\}$. On the punctured disk, the
relevant Hamiltonian Lie algebra is
$\mathfrak h^\circ = \Gamma(\widehat{\C^2}_0\setminus\{0\},
\mathcal O)/\C$, which contains the negative powers
$z_1^{-a}z_2^{-b}$ that are formally dual to the
principal-part module $\mathcal P$ of Theorem D
(`main.tex`:1075–1077, 3697–3700).

**W3-W2-09 (interface coherence question).** Under the Gaiotto
interface lens, an interface from $\widehat{\C^2}_0$ to
$\widehat{\C^2}_0\setminus\{0\}$ should give a functor between
their respective factorization centres. The closed-side claim of
the manuscript is:
$$Z^{P_0}_{\mathrm{fact}}(A_\partial^{\mathrm{Ham}})\big|_{\widehat{\C^2}_0}
  \simeq C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak g),
  \quad
  \mathfrak g = \mathfrak h\ltimes\mathcal P[1].$$
On the punctured disk, the analogous CE-cochain object would use
$\mathfrak h^\circ\ltimes\mathcal P^\circ[1]$ where $\mathcal
P^\circ$ is the cotangent module on the punctured disk. Under
residue duality (M-29 / W4 universal categorical no-go,
`reconstitution/attack-heal-platonic-2026-04-28.md`:1560–1564),
$\mathfrak h$ and $\mathcal P$ are positive/negative cones of one
**bi-infinite parent** module on $\Z^2$; the interface to the
punctured disk would have to glue these two cones into a single
$\Z^2$-graded object.

**The M-29 no-go is decisive here.** It says no
$\C[[\hbar]]$-linear additive category $\mathcal C$ with a
forgetful functor to $\bar A_\hbar$-Lie-Mod can host an
$M_\hbar$ with both fibre conditions (PBW $z_i$-multiplication and
Matlis coadjoint). This **is** the interface obstruction in the
Gaiotto sense: the interface from formal disk to punctured disk
would require precisely the bi-infinite parent module to be
present in a single category, and M-29 closes that in the
negative.

**W3-W2-10 (Gaiotto-lens interpretation of M-29).** The wave-2 M-29
universal categorical no-go has a Gaiotto interpretation: the
formal-disk-to-punctured-disk interface in the local Hamiltonian
BF theory cannot be a deformation-theoretic single-object
interface; it is at best a $\mathbb Z^2$-graded bi-infinite parent
with two cones (PBW raising on positive cone, Matlis coadjoint on
negative cone), no single-object glue. This is exactly the
R-W4-A residual (bi-infinite parent
Hamiltonian-equivariant splitting,
`reconstitution/attack-heal-platonic-2026-04-28.md`:1914–1920).

**No new residual.** The Gaiotto-lens interpretation of M-29 / R-W4-A
adds interpretive weight but no new mathematical obligation.

### §3.2 Dimensional reduction: compactify one $\C$-direction

**Test.** Compactify one of the holomorphic directions, say
$z_2$, by replacing $\widehat{\C}_0$ with
$\widehat{\C^\times}_0 = \mathrm{Spf}\,\C[[z_2,z_2^{-1}]]$ (or
take a circle compactification so the corresponding mode becomes
discrete-spectrum). The reduced theory should be a 1d theory on
the brane line $\R$ with extended internal symmetry coming from
the $z_2$-Fourier modes.

**W3-W2-11 (1d reduction is degenerate).** On the formal disk,
"compactify" is not literally a geometric operation (the formal
disk is not a global geometric object). The closest formal
analogue is **filtration by $z_2$-degree**: write
$\bar A = \bigoplus_{l\ge 0}\bar A^{(l)}$ where $\bar A^{(l)} =
z_1^*z_2^l\cdot\C$-span at $z_2$-degree $l$, and consider the
reduction at $l$-degree zero
$\bar A^{(0)} = \C[z_1]/\C\cdot 1$. This is a 1-variable
Hamiltonian Lie algebra in **one** holomorphic variable.

* The closed Hamiltonian Lie algebra of a 1-variable disk
  $\widehat{\C}_0$ is *abelian*: $\{z_1^k, z_1^m\} = 0$ because
  the symplectic form $\omega = dz_1\wedge dz_2$ requires both
  variables to produce a nonzero bracket. So
  $\bar A^{(0)} = \C[z_1]/\C\cdot 1$ is abelian.
* The closed CE cochains on $\bar A^{(0)}\ltimes
  (\bar A^{(0)})^\vee[1]$ are tensors in two abelian factors;
  they are the de Rham complex on the formal 1-disk plus
  cotangent shift, but the bracket is trivial, so the CE
  differential vanishes.
* On the open side, the reduction at $l = 0$ is the open
  Dirac-probe theory with one matrix field $\phi_1$, no
  $\phi_2$. Then $Q\psi = [\phi_1,\phi_2] = 0$ identically (no
  $\phi_2$ to commute with), so $\psi$ is closed and primitive.
  The BV reduction is **degenerate**.

**W3-W2-12 (degenerate 1d coherence verdict).** The 1d
reduction at $z_2$-degree 0 is *degenerate* (closed and open
sides both abelian / trivial-bracket). The 2d theorem
$\Phi^{\mathrm{Ham}}_{\mathrm{fact}}$ restricts on this
degenerate slice to a tautology: both sides are free
graded-commutative algebras on the Tate vector space $\bar A^{(0)}
\oplus(\bar A^{(0)})^\vee[1]$ with zero CE differential, so the
isomorphism is the identity on a free graded-commutative algebra.
**Coherent, but it does not test the 2d structure.**

A *non-trivial* 1d reduction would replace the $z_2$-direction
with a circle of finite radius, producing a tower of Fourier
modes that interact through the Hamiltonian bracket. This is not
a formal-disk operation — it is a global operation on
$\widehat{\C^\times}\times\widehat{\C}_0$, which the manuscript
does not consider. **Outside the local theorem's scope.**

**No new residual.** The dimensional-reduction test under the
Gaiotto lens produces only the degenerate-1d slice, which is
trivially coherent. A genuine non-trivial dimensional reduction
requires going beyond the formal-disk model.

### §3.3 Survival of the factorization centre under reduction

**W3-W2-13 (factorization centre under degenerate reduction).**
On the degenerate slice $z_2$-degree 0, the factorization centre
$Z^{P_0}_{\mathrm{fact}}(A_\partial^{\mathrm{Ham}})$ becomes
$Z^{P_0}_{\mathrm{fact}}$ of a free graded-commutative algebra on
$\Omega^\bullet_c(I)\widehat\otimes\C[z_1]/\C$, which in turn is
a free graded-commutative algebra on the same vector space (the
$P_0$ centre of a free graded-commutative algebra on a
Tate-finite vector space is itself, by a standard CE/PV
argument). The centre is preserved.

The non-trivial direction is the 2-variable theorem; the
1-variable slice is not informative. Coherence holds trivially.

---

## §4. Target T4 — Generalized symmetry of the factorization centre

### §4.1 The U(1) symmetry on the factorization centre

The U(1) Capelli anomaly (`main.tex`:247–472) operates on the
factorization centre by:
* On closed side: scaling $f \mapsto e^{i\theta} f$ on
  $\bar A$, with the unique U(1)-invariant constant
  Hamiltonians excluded (they're killed by scalar reduction).
  The 2-cocycle $[\bar c]\in H^2_{\mathrm{Lie}}(\bar A;\C)$ is
  U(1)-equivariant (in fact U(1)$_z$-invariant where U(1)$_z$
  scales the central direction).
* On open side: $\mathrm{Tr}(\psi)$ is the U(1) charge generator
  of $\C\cdot I\subset\mathfrak{gl}_N$ (the central direction).
  Capelli shift $\hbar N$ is the U(1) charge of $I$.

**W3-W2-14 (higher-form U(1) view of Capelli).** Under the
Gaiotto generalized-symmetry lens, the U(1) action on the brane
factorization algebra has a **higher-form structure**: the
$\mathfrak{gl}_N$ algebra acts with U(1) center (1-form symmetry
in the standard SUSY-physics sense), and Capelli's shift
$\hbar N$ is the *anomaly* of this 1-form symmetry on the
quantum reduction. This is the standard 't Hooft anomaly
language for a center symmetry in 1d field theory.

**Compatibility check.** The M-31 identification asserts $[\bar c]
\leftrightarrow \hbar N \leftrightarrow [\mathrm{Tr}\,\psi]_{\mathrm{BV}}$
are the same anomaly line. Under the Gaiotto higher-form lens:
* $[\bar c]$ is the closed-side anomaly of the U(1)$_z$
  scalar-axis symmetry.
* $\hbar N$ is the quantum Capelli shift, the central-extension
  anomaly of the U(1)-center of $\mathfrak{gl}_N$.
* $[\mathrm{Tr}\,\psi]_{\mathrm{BV}}$ is the BV-side primitive
  class generating the same U(1)-charge measurement on the
  Dirac-probe brane (the central-direction Koszul class).

**All three are U(1)-charges.** Their identification
M-31 = M-32 = Theorem G is consistent with the Gaiotto
higher-form view: a single 't Hooft anomaly of the center U(1)
shows up classically on the closed side, quantum-mechanically as
the Capelli shift, and BV-cohomologically as the Koszul primitive
$\mathrm{Tr}\,\psi$.

**W3-W2-15 (no contradiction; new clarification).** The Gaiotto
higher-form lens *clarifies* the M-31 identification but does
not modify it. The single anomaly line classified by
$H^2_{\mathrm{Lie}}(\bar A;\C)\cong\C$ is exactly the 't Hooft
anomaly of the U(1)-center symmetry; no further structure is
added. **This is a phrasing improvement, not a defect**.

**Heal proposal W3-W2-H3 (Gaiotto framing of M-31, optional).**
Add to M-31 ledger and to `principles.tex` Theorem G remark a
parenthetical:

> "(Gaiotto framing: the line $[\bar c]\leftrightarrow\hbar N
> \leftrightarrow [\mathrm{Tr}\,\psi]_{\mathrm{BV}}$ is the
> 't Hooft anomaly of the U(1)-center 1-form symmetry of the
> Dirac-probe matrix model; classical / quantum / BV are three
> presentations of the same single anomaly class.)"

This sharpens the physics narrative without introducing new
mathematical content. **Optional editorial**; can be deferred.

### §4.2 Compatibility with the higher-form symmetry view

**W3-W2-16 (the empty trace as a 1-form symmetry generator).**
The unit $1\in\bar A_\hbar$ on the closed side and
$\mathrm{Tr}_N(1) = N$ on the open side are removed by scalar
reduction (`main.tex`:247–472). Under the higher-form lens:
* The empty trace $\mathrm{Tr}_N(1) = N$ is the
  U(1)-charge of the matrix vacuum.
* Its removal by scalar reduction corresponds to gauging the
  U(1)-center 1-form symmetry, leaving the SU($N$)-quotient
  matrix theory.
* The Capelli shift $\hbar N$ is the *gauging anomaly*: it's
  the obstruction to gauging the U(1)-center quantum-mechanically
  without a counterterm.

**Cross-check: Theorem G's classification.** The closed cocycle
$\omega(z_1, z_2) = 1$ produces the unique nontrivial cohomology
class spanning the line $\C\cdot[\bar c]\subset H^2_{\mathrm{Lie}}(\bar A;\C)$
(`main.tex`:281–290, `lem:omega-cocycle`). This is the unique
anomaly of the scalar-axis U(1) — exactly what the higher-form
lens predicts. **No new constraint.**

**W3-W2-17 (1-form U(1) compatibility verdict).** The M-31
identification is fully compatible with the Gaiotto higher-form
symmetry view. No discrepancy; no missing structure. The
Capelli/$\hbar N$ shift is the standard 't Hooft anomaly of a
central 1-form U(1) gauged by scalar reduction. **Discharged.**

---

## §5. Cross-target audit: factorization centre survival

Combining T1–T4:

* **T1 Weiss on brane-line $\R$:** discharged (W3-W2-02–03).
  R-W6-Weiss-defect proper survives only at the
  $\R^2\times\C^2$ level, which is the M-37 four-ingredient
  residual.
* **T2 brane defect locality on $\R$:** proved (a)–(b) at jet /
  smearing level. M-31 bulk identification correct; defect
  cohomology extension gated on M-37 ingredient 3
  (W3-W2-06–07). Heal H2 proposed.
* **T3 interface/dim reduction:** M-29 universal no-go is the
  Gaiotto interface obstruction (W3-W2-09–10). Dimensional
  reduction at $z_2$-degree 0 is degenerate-coherent
  (W3-W2-11–13). No new residual.
* **T4 1-form U(1):** fully compatible with M-31; H3 phrasing
  optional.

**No new fatal attack.** No wave-2 master ledger entry is
invalidated. Five clarifications:
1. Weiss vs locally constant separation (W3-W2-01).
2. Weiss-on-$\R$ discharge via cosheaf+symmetric-algebra reduction
   (W3-W2-02–03).
3. M-31 bulk-only scope sharpening (W3-W2-06–07; H2).
4. M-29 = Gaiotto interface obstruction interpretation (W3-W2-09–10).
5. Higher-form U(1) framing of Theorem G compatible with M-31
   (W3-W2-14–17; H3 optional).

---

## §6. Verdict on wave-2 stable core

The wave-2 stable core (master ledger §D, lines 1976–2050) is
**preserved unmodified** by the Gaiotto+Boundary lens.

* Theorems A–G stable and unchanged.
* M-37 four-ingredient closure plan for R-03 valid; the W2
  re-examination separates the on-$\R$ piece (discharged) from
  the on-$\R^2\times\C^2$ piece (genuinely residual).
* M-31 BV/CE identification valid in bulk; defect-cohomology
  extension stays gated on R-W6-Weiss-defect.

**No downgrade required.** The Gaiotto+Boundary lens adds
interpretive depth (interface obstruction = M-29; 1-form U(1) =
Capelli) but produces no fatal attack on the stable core.

---

## §7. Heal proposals

| ID | Severity | Target | Action |
|----|----------|--------|--------|
| W3-W2-H1 | 1 (clarification) | `thm:open-closed-derived-center-factorization` Step 7 (`main.tex`:2174–2184) | Add one sentence distinguishing locally constant condition (proved here) from Weiss-cosheaf condition (not proved here in the higher-dim sense; Weiss-on-$\R$ follows from L6 + L7 via cosheaf-sym-algebra reduction, recorded in W3-W2-02). |
| W3-W2-H2 | 2 (scoping) | M-31 anchor in `principles.tex` Principle 1 / Theorem G remark; M-31 master-ledger entry | Add bulk-only scoping: "The identification is at the bulk level (single-point evaluation on the brane line). A defect-cohomology extension via a bulk-to-defect kernel is gated on M-37 ingredient 3 / R-W6-Weiss-defect." |
| W3-W2-H3 | 1 (Gaiotto-framing, optional) | `principles.tex` Theorem G remark | Add Gaiotto higher-form framing parenthetical: "the line $[\bar c]\leftrightarrow\hbar N\leftrightarrow[\mathrm{Tr}\,\psi]_{\mathrm{BV}}$ is the 't Hooft anomaly of the U(1)-center 1-form symmetry of the Dirac-probe matrix model." |

All three are editorial. None requires new mathematical content.
H1 sharpens a prose risk in the manuscript proof; H2 precisely
scopes M-31; H3 adds physics framing without changing
mathematics.

---

## §8. New residuals (W3 originated)

* **W3-W2-R1 (genuinely new, low severity).** The Gaiotto
  higher-form view of the M-31 anomaly line as a 't Hooft anomaly
  of the U(1)-center 1-form symmetry is consistent with the
  classical / quantum / BV trichotomy. A direct proof of this
  anomaly's matching across all three sectors via the
  Costello–Gaiotto–Williams 5d twisted-M-theory framework would
  *clarify* the source of the Capelli shift physically. **This is
  motivational** and not required for the local theorem; it is a
  Phase-4 outlook only.

No other new residuals.

---

## §9. Summary

The Gaiotto + Boundary lens applied to the wave-2 stable core
produces:

1. **Discharge of R-W6-Weiss-defect on the brane line $\R$**
   (§1.1, W3-W2-02–03): Weiss-on-$\R$ follows from L6+L7 via
   cosheaf+symmetric-algebra commutation + Roos ML; the genuine
   residual is on $\R^2\times\C^2$ (M-37 four ingredients).
2. **Sharpening of M-31 to bulk-only scope** (§2.2, W3-W2-06–07):
   defect-cohomology extension gated on M-37 ingredient 3
   (bulk-to-defect kernel). Heal H2 proposed.
3. **Interpretation of M-29 as the Gaiotto interface obstruction**
   (§3.1, W3-W2-09–10): the universal categorical no-go is
   exactly the formal-disk-to-punctured-disk interface
   obstruction; no new residual.
4. **Degenerate-coherent dimensional reduction** (§3.2,
   W3-W2-11–13): $z_2$-degree-0 slice collapses to abelian
   1-variable theory, trivially coherent; non-trivial reduction
   outside the formal-disk scope.
5. **1-form U(1) compatibility** (§4, W3-W2-14–17): Capelli
   anomaly = 't Hooft anomaly of U(1)-center; H3 phrasing
   optional.

**Verdict on wave-2 stable core.** Preserved unmodified. No new
fatal attack. Three editorial heals proposed (H1 prose risk in
factorization theorem; H2 M-31 scope; H3 Gaiotto framing
optional). One new residual (W3-W2-R1) at the level of physics
clarification only.

The Gaiotto + Boundary lens strengthens the manuscript's claim
structure by separating bulk from defect cohomology and by
verifying that the higher-form symmetry view of Capelli is fully
compatible with the M-31 unification of the anomaly line. The
genuine residual (R-W6-Weiss-defect on $\R^2\times\C^2$) is
unchanged in scope; it is given clearer Gaiotto-physics
interpretation as a transverse-Mittag-Leffler defect resolution
in the chiral-algebra factorization sense (M-37 ingredient 4),
exactly what BD chiral algebras §3.4 + Costello–Gaiotto–Williams
twisted-M-theory provides the working analytic apparatus for.

End of W3 / W2 report.
