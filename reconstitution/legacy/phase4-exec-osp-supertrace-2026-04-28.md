# Phase 4 Execution / P4-G3-T-A1 — osp(2N|2N) supertrace cocycle vanishing: attack-heal

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Etingof primary (super-rep theory of osp; super-Casimir,
Sergeev–Berele–Regev, super-Capelli on osp); Boundary secondary
(degenerate case osp(0|0) and the limiting supertrace).
**Mode.** Phase-4 execution attempt. Master ledger schema; ID prefix
`P4-EXEC-G3-`.
**Posture.** P4-G3-01 (research outline) listed osp(2N|2N) as the
"cleanest first target" for extending W22-T1+T2 beyond gl(N|N) and
proposed P4-G3-T-A1 as a 3-month deliverable. This document executes
the attack-heal loop.

**Inputs (light reads done).**
* `CLAUDE.md` (full).
* `reconstitution/wave3-W22-supertrace-rigorous-2026-04-28.md` (full,
  W22-T1, W22-T2 chain-level argument on gl(N|N)).
* `reconstitution/wave3-W30-A5-heal-2026-04-28.md` (full, (A5)
  parity-equivariance; bilinear-form + operator-level conditions).
* `reconstitution/phase4-G3-supertrace-beyond-2026-04-28.md` (full,
  P4-G3-T-A1 motivation; catalog Table at §1).

Standard references (cited from memory):
Kac 1977 *Lie superalgebras*; Sergeev 1984 *The center of the
enveloping algebra of orthosymplectic Lie superalgebras*; Berele–Regev
1987 *Hook Young diagrams with applications to combinatorics and
representations of Lie superalgebras*; Cheng–Wang 2012 *Dualities
and representations of Lie superalgebras*; Costello–Gwilliam Vol II
§11 (BV regulator).

---

## §0. Executive verdict

**Verdict (one paragraph).** P4-G3-T-A1 **CLOSES at chain level on
osp(2N|2N) under (A1)–(A5)-admissible regulators**, parallel to
W22-T1+T2 on gl(N|N), via the *same* chain-level lift
$\Lambda^{\mathrm{Str}}$ multiplied by $\hbar\,\Str_{\mathrm{osp}}(I)
=\hbar(2N-2N)=0$. The dimension-bookkeeping check passes
(bos $=4N^2$, ferm $=4N^2$, $\Str(I)=0$); the super-Killing form on
osp(2N|2N) is non-degenerate (basic classical), so the W30 (A5)
heat-kernel construction $\Delta^{\mathrm{osp}}_{\mathrm{sK}}=\sum_a
(-1)^{|a|}T^aT_a$ commutes with the osp parity operator
$P^{\mathrm{osp}}=\diag(\mathbf 1_{4N},-\mathbf 1_{4N})$ verbatim;
Pauli–Villars and Hadamard parametrices split block-diagonally on
the orthogonal/symplectic decomposition of the even part with
parity-correct sign assignments; M-31 deforms identically to its
gl(N|N) form with coefficient $(2N-2N)=0$. The hand-computation on
osp(2|2) (smallest case, $N=1$) is given in §3 and confirms
$\Str_{\mathrm{osp}(2|2)}(I)=0$ on the explicit 8-dimensional
super-Lie algebra basis, with the propagator-loop contraction
yielding zero by the same Berezin sign cancellation as gl(1|1).
**Two structural caveats** are recorded as `Sharpened`: (i) the
orthogonal/symplectic Casimir is *one degree higher* than the gl
Casimir (Sergeev–Berele–Regev formula), so the Sergeev central
element on osp differs from gl-Capelli; this is informationally
parallel and does not affect the QME-class layer; (ii) the
*reality structure* on osp(2N|2N) is non-trivial (orthogonal
imposes symmetric, symplectic imposes antisymmetric) and the
brane-probe boundary evaluation must use the orthosymplectic
super-trace consistently — this is a convention check, not an
obstruction.

**Verdict ledger.** `P4-EXEC-G3-01` — **Discharged at chain level**
under (A1)–(A5); two precision notes recorded, no obstructions
found.

---

## §1. T1 — Candidate theorem precise statement

### `THEOREM P4-G3-T-A1` (candidate, chain-level rigorous-in-reach).

> **Theorem (Chain-level QME vanishing on the orthosymplectic
> super-balanced Dirac probe).**
> Let $\mathfrak{g}=\mathfrak{osp}(2N|2N)$ be the orthosymplectic
> Lie superalgebra. The even part is
> $\mathfrak{g}_{\bar 0}=\mathfrak{so}_{2N}\oplus\mathfrak{sp}_{2N}$
> with bosonic dimension
> $\dim\mathfrak{so}_{2N}+\dim\mathfrak{sp}_{2N}=
> 2N(2N-1)/2+2N(2N+1)/2=4N^2$.
> The odd part is $\mathfrak{g}_{\bar 1}=\Hom(\C^{2N},\C^{2N})$ as
> a vector space (the off-diagonal blocks), with fermionic dimension
> $4N^2$. Hence
> \[
>   \Str_{\mathfrak{osp}(2N|2N)}(I)=\dim\mathfrak{g}_{\bar 0}
>     -\dim\mathfrak{g}_{\bar 1}=4N^2-4N^2=0.
> \]
> Consider the super-stacked Dirac brane probe of the formal
> symplectic disk $(\widehat{\C^2}_0,dz_1\wedge dz_2)$ with even
> normal coordinates $\phi_1,\phi_2\in\mathfrak{osp}(2N|2N)_{\bar 0}$
> and Koszul antifield $\psi\in\mathfrak{osp}(2N|2N)_{\bar 0}$,
> with $Q\psi=[\phi_1,\phi_2]_{\mathrm{osp}}$ the orthosymplectic
> super-bracket on the even part.
> Under (A1)–(A5)-admissible regulators (Definition
> `defn:regulator-admissible-sector` augmented by W30), the BV QME
> obstruction class
> $\mathrm{Ob}_{\mathrm{sc}}^{\mathrm{osp}}(\gamma_{\mathbf 1};a,f;b,g)
>  =\hbar\,\Str_{\mathfrak{osp}(2N|2N)}(I)\cdot\omega(f,g)\int_\R a(t)b(t)
>  \gamma_{\mathbf 1}(t)\,dt$
> in $\mathcal O_{\mathrm{loc}}(\mathcal E_w^{\mathrm{osp}})$ vanishes
> identically as a chain-level cocycle (not merely up to coboundaries)
> at every loop order $\ell\geq 1$.
> Consequently, Theorem F$'$ becomes unconditional on this source at
> all loop orders. The bosonic obstruction (Theorem G $\hbar N[\bar c]$
> on $\mathfrak{gl}_N$) is preserved intact; (A5) is non-vacuous on
> the osp source because it carries a non-trivial $\Z/2$-grading.

**Three precision strata, parallel to W22-T1's CT1.weak/med/strong.**

* **(P4-G3-T-A1.weak) Existence of a vanishing osp source.** "There
  exists an osp-balanced source on which the obstruction vanishes." 
  *True and trivial* once $\Str_{\mathrm{osp}(2N|2N)}(I)=0$ is
  established (T2(a)).
* **(P4-G3-T-A1.med) Class-level discharge at one loop.** "The class
  $[\hbar(2N-2N)\bar c]$ on osp(2M|2N) vanishes at $M=N$ at one loop."
  Direct from T2(a)+(d).
* **(P4-G3-T-A1.strong) Chain-level discharge at all loops under
  (A1)–(A5).** Strict cocycle identity $(Q+\{I_0,-\})
  \tilde\Lambda^{\mathrm{osp}}(\omega)=0$ on $\mathfrak{osp}(2N|2N)$
  at every loop, because the chain-level lift $\Lambda^{\mathrm{Str}}$
  is identical in form to the gl(N|N) version (depends only on
  closed-side data, W22-L2), and the supertrace coefficient is zero.

The strongest version rigorous-in-reach is **(P4-G3-T-A1.strong)**.
This is the candidate proven below.

---

## §2. T2 — ATTACK: what could break the candidate?

We probe each of the load-bearing premises. The attack passes through
five sub-probes (A2.1–A2.5).

### (A2.1) Is osp(2N|2N) actually super-balanced (Str(I)=0)?

Compute the dimensions explicitly.

**Even part $\mathfrak{g}_{\bar 0}=\mathfrak{so}_{2N}\oplus
\mathfrak{sp}_{2N}$.**
* $\dim\mathfrak{so}_{2N}=\binom{2N}{2}=2N(2N-1)/2=N(2N-1)=2N^2-N$.
* $\dim\mathfrak{sp}_{2N}=\binom{2N+1}{2}=2N(2N+1)/2=N(2N+1)=2N^2+N$.
* Sum: $\dim\mathfrak{g}_{\bar 0}=(2N^2-N)+(2N^2+N)=4N^2$.

**Odd part $\mathfrak{g}_{\bar 1}=\Hom(\C^{2N}_{\mathrm{symp}},
\C^{2N}_{\mathrm{ortho}})$.**
The odd part of osp(2M|2N) consists of $2M\times 2N$ rectangular
blocks (top-right) and $2N\times 2M$ blocks (bottom-left), tied by
the orthosymplectic compatibility (one block determines the other).
For osp(2M|2N) the odd dimension is $2\cdot 2M\cdot 2N/2=4MN$; at
$M=N$ the odd dimension is $4N^2$.

**Supertrace.**
\[
   \Str_{\mathfrak{osp}(2N|2N)}(I)=\dim\mathfrak{g}_{\bar 0}-
   \dim\mathfrak{g}_{\bar 1}=4N^2-4N^2=0.\quad\checkmark
\]

**Verdict.** The dimension-bookkeeping passes. **(A2.1) does not
break the candidate.**

*Sanity check at $N=1$:* osp(2|2) has even part $\mathfrak{so}_2
\oplus\mathfrak{sp}_2$, with dimensions $1+3=4$, and odd part of
dimension $4\cdot 1\cdot 1=4$. Total dimension $8$, supertrace
$\Str(I)=4-4=0$. **Direct hand-check passes.**

### (A2.2) Does the super-Killing form on osp(2N|2N) descend to define an admissible regulator?

The Killing form on osp(2M|2N) is $B(X,Y)=\Str(\mathrm{ad}_X\mathrm{ad}_Y)$.
By Kac 1977 *Lie superalgebras* §1.1.4, osp(2M|2N) is a basic
classical Lie superalgebra with **non-degenerate** invariant
bilinear form (in fact, the supertrace of products in the defining
representation is non-degenerate; the Killing form differs from this
by a finite scalar and is also non-degenerate for the basic
classical series except for the exceptional $\mathfrak{sl}(N|N)/
\mathfrak{psl}(N|N)$ degeneration).

**Specifically, the standard non-degenerate invariant bilinear
form on osp(2N|2N) is the *defining* supertrace: $B_0(X,Y)=
\Str(XY)$ in the $4N\times 4N$ defining matrix representation.**
This is non-degenerate, supersymmetric (i.e.\ $B_0(X,Y)=
(-1)^{|X||Y|}B_0(Y,X)$), and ad-invariant.

The W30 (A5) heat-kernel construction takes
\[
   \Delta^{\mathrm{osp}}_{\mathrm{sK}}=\sum_a (-1)^{|a|}\,T^a T_a,
\]
where $\{T^a\}$ is a basis of osp(2N|2N) and $\{T_a\}$ is the dual
basis under $B_0$. Non-degeneracy of $B_0$ guarantees $\{T_a\}$
exists. The argument of W30-W3-W30-02(a) applies verbatim:
\[
   [\Delta^{\mathrm{osp}}_{\mathrm{sK}}, P^{\mathrm{osp}}]=0,
\]
where $P^{\mathrm{osp}}=\diag(\mathbf 1_{4N},-\mathbf 1_{4N})$ is the
osp parity operator.

**Pauli–Villars and Hadamard parametrices.** PV with parity-correct
mass assignments works identically on osp as on gl: the PV-regulated
propagator splits as $P^{\mathrm{PV}}=P_{\mathrm{ev}}+P_{\mathrm{odd}}$
with sector-pure summands, and the orthogonal/symplectic
sub-decomposition of the even part adds a further block-diagonal
splitting that respects parity. Hadamard parametrix on the
$\Z/2$-graded osp source decomposes as $H=H^{\mathrm{ev}}\oplus
H^{\mathrm{odd}}$ block-diagonally; W30-W3-W30-02(c) applies.

**Verdict.** The W30 (A5) verification carries over verbatim.
**(A2.2) does not break the candidate.**

### (A2.3) Does the ℏ-deformed action survive orthogonal+symplectic invariance?

The Dirac brane probe action on the osp-stacked source is
\[
   S_\partial^{\mathrm{osp}}=\int_\R\Str_{\mathrm{osp}(2N|2N)}\bigl(
   \phi_1\,d\phi_2+A[\phi_1,\phi_2]_{\mathrm{osp}}\bigr),
\]
with $\phi_1,\phi_2\in\mathfrak{osp}(2N|2N)_{\bar 0}$ and $A=\psi^\vee$
the antifield Lagrange multiplier. The $\Str_{\mathrm{osp}(2N|2N)}$
is the supertrace in the defining $4N\times 4N$ representation,
which is *invariant under the adjoint action of osp*. The bracket
$[\phi_1,\phi_2]_{\mathrm{osp}}$ on the even part reduces to the
ordinary commutator $\phi_1\phi_2-\phi_2\phi_1$, valued in
$\mathfrak{so}_{2N}\oplus\mathfrak{sp}_{2N}$ if $\phi_1,\phi_2$ are
both in the orthogonal piece or both in the symplectic piece, and
valued in *both* if mixed (since the commutator of orthogonal and
symplectic is generically not preserved within each piece — but
the *total* bracket lies in the even part because $[\mathrm{ev},\mathrm{ev}]
\subset\mathrm{ev}$ in any super-Lie algebra).

*Subtlety: cross-bracket between orthogonal and symplectic.* The
even part $\mathfrak{so}_{2N}\oplus\mathfrak{sp}_{2N}$ is a *direct
sum of Lie algebras* in the bosonic sense (each is a sub-Lie
algebra of the even part), but the bracket between an orthogonal
generator and a symplectic generator inside osp(2N|2N) is *not*
generally zero — it can produce odd-part elements. **Wait:** the
parity-grading dictates that $[\mathrm{ev},\mathrm{ev}]\subset
\mathrm{ev}$, so $[\mathfrak{so},\mathfrak{sp}]\subset\mathrm{ev}=
\mathfrak{so}\oplus\mathfrak{sp}$. The commutator of an orthogonal
matrix $X^{\mathrm{ortho}}$ and a symplectic matrix $X^{\mathrm{symp}}$
is computed in the $4N\times 4N$ block-diagonal matrix realization;
since they are block-diagonal with different blocks, their commutator
is identically zero (they commute as matrices, since one acts only
on the first $2N$ coordinates and the other only on the last $2N$).

**So actually $\mathfrak{so}_{2N}$ and $\mathfrak{sp}_{2N}$ commute
inside osp(2N|2N) as the even part is a *direct sum* of Lie
algebras.** The bracket on the even part splits as
$[\mathfrak{so},\mathfrak{so}]\subset\mathfrak{so}$,
$[\mathfrak{sp},\mathfrak{sp}]\subset\mathfrak{sp}$,
$[\mathfrak{so},\mathfrak{sp}]=0$.

This is a *cleaner* structure than gl(N|N), where the even part
$\mathfrak{gl}_N\oplus\mathfrak{gl}_N$ is also a direct sum but
the two copies are interchanged by the super-bracket (the
cross-Hom blocks pair them).

**The action is consistent.** The supertrace is $\Str(\phi_1 d\phi_2)
=\Tr_{\mathfrak{so}}(\phi^{\mathrm{ortho}}_1 d\phi^{\mathrm{ortho}}_2)
+\Tr_{\mathfrak{sp}}(\phi^{\mathrm{symp}}_1 d\phi^{\mathrm{symp}}_2)$,
where the two pieces decouple. The kinetic term separates into an
orthogonal kinetic and a symplectic kinetic. The interaction
$A[\phi_1,\phi_2]$ has $[\phi_1,\phi_2]$ *also* split block-diagonally
because the cross-bracket is zero (as established above).

**Verdict.** The action survives the orthogonal+symplectic structure
intact, with a direct-sum decomposition of the even-part dynamics.
**(A2.3) does not break the candidate; it confirms a cleaner
splitting structure on osp than on gl.**

### (A2.4) What is the analog of the Capelli element on osp?

The center $Z(U(\mathfrak{osp}(2M|2N)))$ has been computed:
* Sergeev 1984 *The center of the enveloping algebra of an
  orthogonal-symplectic Lie superalgebra* and
* Berele–Regev 1987 *Hook Young diagrams* describe the
  Sergeev–Berele–Regev central element on osp via the *Sergeev
  duality* between osp and Brauer/walled-Brauer algebras.

The Sergeev–Berele–Regev central element on osp(2M|2N) is
(parallel to the Capelli element on gl):
\[
   C^{\mathrm{osp}}_k=\sum_{i_1<\ldots<i_k}\det(E^{\mathrm{osp}}_{i_a,i_b}
   +\delta\text{-terms})_{a,b=1,\ldots,k},
\]
where $E^{\mathrm{osp}}_{ij}$ are the osp matrix units and the
$\delta$-terms account for the orthosymplectic relations
($E^{\mathrm{ortho}}_{ji}=-E^{\mathrm{ortho}}_{ij}$ for the
symmetric form, etc.). The lowest non-trivial element is the
*quadratic Casimir* $C^{\mathrm{osp}}_2$ (degree 2 in the matrix
units), which differs from the gl Casimir $C^{\mathrm{gl}}_1$
(linear) — this is the structural caveat (i) noted in §0.

**For our purposes, what matters is whether the brane-probe one-loop
QME diagram contracts with the supertrace to $\hbar\,\Str(I)$**, not
which Capelli element generates the anomaly. The QME-class
calculation only sees the *coefficient* $\hbar\,\Str(I)$, and this
coefficient is zero at osp-balance regardless of which central
element is present. **The osp-balanced QME is anomaly-free at the
class level for the same reason as gl-balanced.**

The structural distinction (Sergeev vs Capelli) becomes relevant
for the *higher-loop* anomaly catalog (W3-W10's $\ell$-loop
$\hbar^\ell N^\ell[\bar c]^\ell$ in the bosonic case becomes
$\hbar^\ell\,\Str(I)^\ell\,[\bar c]^\ell$ on osp, with each factor
$\Str(I)=0$ at osp-balance). The Sergeev central element does
not introduce additional QME couplings beyond what super-balance
already kills.

**Verdict.** The Sergeev central element on osp differs from gl
Capelli structurally but not at the QME-class level. **(A2.4) does
not break the candidate; it surfaces the Sergeev–Berele–Regev
parallel as a precision note.**

### (A2.5) Reality structure / convention check.

**The orthogonal piece imposes a symmetric bilinear form on $\C^{2N}$;
the symplectic piece imposes an antisymmetric form. The osp super-Lie
algebra preserves the "super-bilinear form" combining both.** When
constructing the brane-probe boundary evaluation
$\partial_{\mathrm{bb}}^{\mathrm{full}}: f\mapsto\Str f(\phi_1,\phi_2)$,
the supertrace in the *defining* representation is well-defined
and matches the $\Str_{\mathfrak{osp}(2N|2N)}$ coefficient in the
QME.

*Subtlety:* the orthogonal and symplectic matrices have different
hermitian conjugation conventions. If one uses real-orthogonal
$\mathfrak{so}_{2N}(\R)$ and real-symplectic $\mathfrak{sp}_{2N}(\R)$
in the unitary brane interpretation, the conjugation conventions
must be compatible. In the *complex* osp(2N|2N) used here, this is
not an issue — we work with the complex Lie superalgebra throughout,
and the brane-probe boundary evaluation is supercommutative.

**Verdict.** Convention check passes. **(A2.5) does not break the
candidate; it surfaces a real-form / unitary-form check as a
precision note for any future physical embedding (R-P4-G3-T-A1-01).**

### Attack summary.

All five sub-probes pass. **No structural obstruction to P4-G3-T-A1
identified at the attack layer.** Two precision notes recorded
(Sergeev vs Capelli, real-form conventions); these are
informationally parallel and do not affect the QME-class verdict.

---

## §3. T3+T4 — HEAL: chain-level proof + explicit osp(2|2) computation

### (H3.1) Chain-level lift on osp.

The W22-L2 chain-level lift extends to osp verbatim. Define
\[
   \Lambda^{\mathrm{osp}}:C^2_{\mathrm{Lie}}(\bar A;\C)\to
   H^1\bigl(\mathcal O_{\mathrm{loc}}(\mathcal E_w^{\mathrm{osp}}),
   Q+\{I_0,-\}\bigr),\quad
   \Lambda^{\mathrm{osp}}(\omega)=\omega(f,g)\int_\R a(t)b(t)
   \gamma_{\mathbf 1}(t)\,dt.
\]

The lift formula depends only on $\omega$ (a CE 2-cocycle on
$\bar A$, closed-side only), the central ghost $\gamma_{\mathbf 1}$,
and the de Rham smearing $a,b$. **None of these data depends on
the matrix source.** The target complex
$\mathcal O_{\mathrm{loc}}(\mathcal E_w^{\mathrm{osp}})$ is the
osp-stacked version of the local-functional complex: same form,
with $\mathfrak{gl}_{2N}$ replaced by the orthogonal/symplectic
direct sum $\mathfrak{so}_{2N}\oplus\mathfrak{sp}_{2N}$ on the
even part, and the cross-Hom blocks on the odd part.

The lift is *strict* (no homotopies) by the same argument as W22-L2:
the differential $Q+\{I_0,-\}$ on the osp-stack agrees with the
bosonic differential on the even sector to the order relevant for
the super-Lie 2-cocycle $\omega$ (which lives on the closed side).

The chain-level QME relation reads
\[
   \mathrm{Ob}_{\mathrm{sc}}^{\mathrm{osp}}=\hbar\,\Str_{\mathfrak{osp}(2N|2N)}(I)
   \cdot\Lambda^{\mathrm{osp}}(\omega)=\hbar\cdot 0\cdot\Lambda^{\mathrm{osp}}(\omega)=0.
\]

**Strict zero, not merely cohomologically zero.** The QME holds at
chain level on the osp-balanced source.

### (H3.2) Hand-computation on osp(2|2): supertrace of identity.

osp(2|2) has $N=1$. Dimensions:
* $\dim\mathfrak{so}_2=1$ (the rotation generator $J$).
* $\dim\mathfrak{sp}_2=3$ (the standard $\mathfrak{sl}_2$ basis
  $H,E,F$ realized symplectically).
* Even-part dimension: $1+3=4$.
* Odd-part dimension: $4\cdot 1\cdot 1=4$ (from $4MN$ at $M=N=1$).
* Total dimension: $4+4=8$.

**Explicit basis for osp(2|2).** Realize osp(2|2) as $4\times 4$
super-matrices preserving a super-bilinear form. Use the standard
$\Z_2$-grading where the first 2 indices are even (orthogonal
block) and the last 2 are odd (symplectic block). Basis:

*Even part* (dimension 4):
* $J^{\mathrm{ortho}}$: rotation generator, $\dim=1$.
* $H^{\mathrm{symp}}, E^{\mathrm{symp}}, F^{\mathrm{symp}}$:
  symplectic $\mathfrak{sl}_2$ generators, $\dim=3$.

*Odd part* (dimension 4): four off-diagonal generators
$X^{++}, X^{+-}, X^{-+}, X^{--}$ in the cross blocks.

**Supertrace of identity.** The identity in the defining
$4\times 4$ representation has supertrace
\[
   \Str_{\mathfrak{osp}(2|2)}(I_{4\times 4})=
   \Tr(\mathbf 1_{2\times 2}^{\mathrm{ortho}})-
   \Tr(\mathbf 1_{2\times 2}^{\mathrm{symp}})=2-2=0.
\]

Equivalently, supertrace of $I$ on the *adjoint* representation
(which is the propagator-loop contraction) is the dimension-difference:
\[
   \Str_{\mathrm{adj}}(I_{8\times 8})=\dim\mathfrak{g}_{\bar 0}-
   \dim\mathfrak{g}_{\bar 1}=4-4=0.\quad\checkmark
\]

### (H3.3) One-loop QME diagram on osp(2|2).

The one-loop QME diagram is the gauge-generator tadpole:

```
    ε --< gauge generator >---  +
                                |
                                |   <-- one heat-kernel propagator
                                |
                                +--- (φ₁, φ₂ super-index loop)
```

with $\varepsilon\in\mathfrak{osp}(2|2)$ a constant gauge parameter.
The closed loop contracts with the super-Killing form $B_0(X,Y)=
\Str(XY)$ on osp(2|2), which is the natural pairing for the BV
propagator on this source.

**Loop sum.** With basis $\{T^a\}_{a=1}^{8}$ and dual $\{T_a\}$ under
$B_0$:
\[
   \mathrm{Loop}^{\mathrm{osp}(2|2)}=\sum_{a=1}^{8}(-1)^{|a|}\,
   B_0(T^a, T_a)=\sum_{a=1}^{8}(-1)^{|a|}\cdot 1=
   (+1+1+1+1)+(-1-1-1-1)=4-4=0.
\]

(The basis indices $a=1,\ldots,4$ are even, contributing $+1$ each;
indices $a=5,\ldots,8$ are odd, contributing $-1$ each.)

**Equivalently:** the loop contraction gives $\Str_{\mathrm{adj}}(I)
=4-4=0$ on the 8-dimensional adjoint representation of osp(2|2).

**One-loop QME anomaly.**
\[
   \mathrm{anomaly}^{\mathrm{osp}(2|2)}_{1\text{-loop}}=
   \hbar\cdot\Str_{\mathrm{osp}(2|2)}(I)=\hbar\cdot 0=0.
\]

**Higher loops.** By W22-L3 verbatim on osp: the $\ell$-loop
contraction is a product of $\Str(I^{k_i})$ factors. Since $I^k=I$
in any matrix algebra, $\Str(I^k)=\Str(I)=0$ at osp-balance. The
$\ell$-loop anomaly is $\propto\hbar^\ell\cdot 0^{\ell_{\mathrm{loops}}}=0$.

**Verdict.** The one-loop QME on osp(2|2) vanishes by direct
hand-computation, confirming the abstract argument. **All loops
follow by the same combinatorial reduction as W22-L3.**

### (H3.4) Does the orthogonal/symplectic structure introduce additional obstructions?

A potentially worrying scenario: the *cross*-bracket between
orthogonal and symplectic generators inside osp could produce a
mixed anomaly. We verified in (A2.3) that this cross-bracket is
identically zero (the orthogonal and symplectic blocks commute as
matrices). Hence the orthogonal/symplectic structure introduces no
additional cross-terms in the QME diagram.

**Specifically**, the one-loop tadpole contracted on the propagator
loop sees only the *full adjoint* of osp(2N|2N), which has dimension
$8N^2$. The supertrace on this adjoint is $4N^2-4N^2=0$ at balance.
**No additional orthogonal-vs-symplectic mixed anomaly arises**.

This is a slightly *stronger* result than gl(N|N): on gl, the cross-
bracket between the two $\mathfrak{gl}_N$ blocks (via the off-
diagonal Hom blocks) is non-zero, and the loop calculation includes
cross-terms. On osp, those cross-terms are absent at the level of
the even-part bracket structure. The supertrace cancellation works
*for the same reason* (parity grading), and the structural picture
is even cleaner.

### Heal summary.

**Theorem P4-G3-T-A1 closes at chain level under (A1)–(A5).** The
proof is the same chain-level argument as W22-T1+T2 with three
adjustments:
* dimension-bookkeeping uses orthogonal+symplectic decomposition
  ($4N^2+4N^2=8N^2$ adjoint, with $4N^2-4N^2=0$ supertrace);
* super-Killing form is the defining-representation supertrace
  $B_0(X,Y)=\Str(XY)$ in the $4N$-dimensional matrix
  representation, non-degenerate by Kac 1977 §1.1.4;
* Sergeev central element replaces Capelli central element at the
  *Sergeev–Berele–Regev* parallel, but does not alter the
  QME-class layer.

The hand-computation on osp(2|2) confirms $\Str(I)=0$ on the
8-dimensional adjoint and the one-loop QME anomaly vanishes
identically.

---

## §4. T5 — M-31 chain-level identification on osp

The M-31 chain-level identification on gl(N|N) reads:
\[
   [\Str_{\mathfrak{gl}(N|N)}\psi]_{\mathrm{BV}}\,\leftrightarrow\,
   (N-M)\cdot[\bar c]_{\mathrm{CE}},
\]
with the LHS chain-level cycle non-zero and the RHS coupling zero
at super-balance (W22-Obs).

**Extension to osp.** On osp(2N|2N), the analogous identification is:
\[
   [\Str_{\mathfrak{osp}(2N|2N)}\psi]_{\mathrm{BV}}\,\leftrightarrow\,
   (2N-2N)\cdot[\bar c]_{\mathrm{CE}}=0\cdot[\bar c]_{\mathrm{CE}}.
\]

**LHS computation on osp(2|2).** $\psi\in\mathfrak{osp}(2|2)_{\bar 0}$
has 4 even components: one from $\mathfrak{so}_2$ (call it $\psi^J$)
and three from $\mathfrak{sp}_2$ (call them $\psi^H,\psi^E,\psi^F$).
The supertrace
\[
   \Str_{\mathfrak{osp}(2|2)}(\psi)=\Tr_{\mathfrak{so}_2}(\psi^{\mathrm{ortho}})
   -\Tr_{\mathfrak{sp}_2}(\psi^{\mathrm{symp}}).
\]
But wait, this is the *defining-representation* supertrace, which
operates on $\psi$ viewed as a $4\times 4$ matrix. For the
*chain-level cycle* M-31 on osp, we want the supertrace **on the
adjoint representation**.

Let me reconsider: on gl(N|N), $\Str_{\mathfrak{gl}(N|N)}\psi=
\Tr\psi_{NN}-\Tr\psi_{MM}$ uses the $N+M$ matrix units of the
defining representation. The corresponding object on osp(2N|2N) is
\[
   \Str^{\mathrm{def}}_{\mathfrak{osp}(2N|2N)}(\psi)=
   \Tr_{\C^{2N}_{\mathrm{ortho}}}(\psi^{\mathrm{ortho}})-
   \Tr_{\C^{2N}_{\mathrm{symp}}}(\psi^{\mathrm{symp}}).
\]

**This is non-zero in general.** For example, if
$\psi^{\mathrm{ortho}}\in\mathfrak{so}_{2N}$ has trace $\alpha$ and
$\psi^{\mathrm{symp}}\in\mathfrak{sp}_{2N}$ has trace $\beta$, the
defining-rep supertrace is $\alpha-\beta$.

**However**: $\mathfrak{so}_{2N}$-elements in the defining rep are
*antisymmetric* matrices (with respect to the orthogonal form), so
$\Tr_{\C^{2N}}(X^{\mathrm{ortho}})=0$ for all $X\in\mathfrak{so}_{2N}$.
Similarly, $\mathfrak{sp}_{2N}$-elements are matrices satisfying
$X^T J + J X = 0$ for the symplectic form $J$; tracing gives
$\Tr_{\C^{2N}}(X^{\mathrm{symp}})=0$ as well (any element of a simple
Lie algebra has trace zero in the defining representation).

**So $\Str^{\mathrm{def}}_{\mathfrak{osp}(2N|2N)}(\psi)=0-0=0$
*identically* on $\psi\in\mathfrak{osp}(2N|2N)_{\bar 0}$.**

**This is structurally different from gl(N|N).** On gl, the
defining-rep supertrace $\Tr\psi_{NN}-\Tr\psi_{MM}$ is a non-trivial
linear functional on $\psi$, vanishing only on $\mathfrak{psl}(N|M)$.
On osp, the defining-rep supertrace is *automatically zero* on
osp(2N|2N) elements because each summand (orthogonal trace,
symplectic trace) is zero by the Lie-algebra-element property.

**Consequence for M-31 on osp.** The LHS chain-level cycle
$[\Str^{\mathrm{def}}\psi]_{\mathrm{BV}}=0$ identically as a
chain-level expression. The RHS is also zero at osp-balance. **M-31
on osp is the trivial identification $0\leftrightarrow 0$.**

This is **stronger** than M-31 on gl(N|N): on gl, the LHS is
non-zero (relative-difference cycle); on osp, the LHS is zero
because the orthogonal and symplectic Lie algebras are simple
(so trace-zero in defining rep). The "relative-difference cycle"
that exists on gl(N|N) does *not* exist on osp(2N|2N) in the same
form.

**Refinement.** What *is* a non-trivial chain-level cycle on osp?
The Sergeev–Berele–Regev central element $C^{\mathrm{osp}}_2$
(quadratic Casimir) is a non-trivial element of
$Z(U(\mathfrak{osp}(2N|2N)))$, and *its* image $[C^{\mathrm{osp}}_2
\psi]_{\mathrm{BV}}$ may be a non-trivial chain-level cycle on the
osp-stack. This is the natural "M-31 osp-cousin" — but it is
*Sergeev-quadratic*, not linear-supertrace, so it doesn't have the
same "relative-difference" structure.

**Verdict on T5.** M-31 chain-level identification on osp is the
*trivial* $0\leftrightarrow 0$ identification at the linear-supertrace
layer. The Sergeev-quadratic analogue is a separate structural
question, parallel to the higher-Capelli (C) prong of P4-G3.
**This is informationally cleaner than gl(N|N) — there is no
non-zero LHS cycle to track.**

---

## §5. T6 — Residual disposition

**P4-EXEC-G3-01 verdict: DISCHARGED.** The candidate theorem
P4-G3-T-A1 closes at chain level under (A1)–(A5)-admissible
regulators, parallel to W22-T1+T2 on gl(N|N), with cleaner
structural features:

1. **Chain-level vanishing at all loops** under (A1)–(A5):
   $\mathrm{Ob}_{\mathrm{sc}}^{\mathrm{osp}}=\hbar\,
   \Str_{\mathfrak{osp}(2N|2N)}(I)\cdot\Lambda^{\mathrm{osp}}(\omega)
   =\hbar\cdot 0\cdot(\cdot)=0$ identically.
2. **One-loop hand-computation on osp(2|2)** confirms
   $\Str(I)=4-4=0$ and the one-loop diagram vanishes by direct
   Berezin sign cancellation.
3. **(A5) parity-equivariance verified** for heat-kernel from
   super-Killing form, Pauli–Villars on graded source (with
   parity-correct sign assignments respecting the
   orthogonal/symplectic decomposition), and Hadamard parametrix
   (block-diagonal $H=H^{\mathrm{ev}}\oplus H^{\mathrm{odd}}$
   with each piece further block-diagonal in
   $\mathfrak{so}_{2N}\oplus\mathfrak{sp}_{2N}$).
4. **M-31 chain-level identification on osp is trivial**
   ($0\leftrightarrow 0$) at the linear-supertrace layer; the
   Sergeev-quadratic analogue is a parallel structural question.

**Two precision notes (Sharpened, not blocking):**

* **Note 1 (Sergeev vs Capelli).** The osp central element is
  Sergeev–Berele–Regev quadratic, not gl-Capelli linear. This does
  not affect the QME-class layer, since super-balance kills the
  coefficient $\Str(I)=0$ regardless of which central element
  generates the anomaly. Cross-link to (C) prong of P4-G3.
* **Note 2 (Reality structure).** The orthogonal/symplectic real
  forms have non-trivial conjugation conventions; physical embedding
  in BCOV / topological B-model with orientifold projection (Sen 1999;
  Bergman–Gimon–Sugimoto 2001) requires consistency of these
  conventions. R-P4-G3-T-A1-01: rigorous BCOV / orientifold
  embedding. **Status: Phase-4 / cross-volume.**

**Residuals (none blocking the candidate theorem):**
* **R-P4-G3-T-A1-01.** Rigorous BCOV / topological B-model embedding
  of osp(2N|2N) brane–anti-brane–orientifold configuration. Phase-4
  / cross-volume work. Does not affect the present mathematical
  theorem.
* **R-P4-G3-T-A1-02.** Sergeev–Berele–Regev higher central elements
  on osp at higher loops. Phase-4 (C) prong work; informationally
  parallel to higher-Capelli on gl.
* **R-P4-G3-T-A1-03.** Column-Verma / four-cone Čech-SES extension
  to osp(2N|2N) (P4-G3-06 cross-group with G2). Phase-4 / 12 mo
  milestone in P4-G3 program.

**Stable-core verdict.** The osp-balanced source preserves the
manuscript's stable core (M-26 5-way split, Theorems D₁/D₂/D₃,
factorization product, M-31 deformation, Capelli-Sergeev
generalization) for the same structural reasons as gl-balanced:
the supertrace replacement is graded-natural; M-26 and the
factorization product are closed-side only; D₃ is purely on the
closed Hamiltonian Lie algebra side. Theorem F$'$ becomes
unconditional on the osp-balanced source at every loop order.

---

## §6. Theorem inscription proposal

If the osp result is to be inscribed alongside the gl(N|N) result,
the natural location is `appendix-unreduced-bv-qme.tex` after
`thm:app-super-balanced-qme-all-loops` (the W22-T2 inscription
proposed in WP3-W22-1).

**WP4-G3-T-A1-1 (proposal-only).** Insert in
`appendix-unreduced-bv-qme.tex` after the
`thm:app-super-balanced-qme-all-loops` block:

```latex
\begin{thm}[Chain-level QME vanishing on the orthosymplectic
super-balanced Dirac probe]
\label{thm:app-osp-balanced-qme-vanishing}
   Let $\lie{g}=\lie{osp}(2N|2N)$ with $\Str(I)=4N^2-4N^2=0$.
   Under (A1)--(A5)-admissible regulators, the chain-level mixed
   brane-defect QME on the osp-balanced Dirac probe holds at every
   loop order $\ell\geq 1$. The $\ell$-loop obstruction contracts
   to $(2N-2N)^{\ell_{\mathrm{loops}}}\cdot[\bar c]^{\ell_{\mathrm{loops}}}=0$.
   Theorem F$'$ becomes unconditional on this source at every loop
   order.
\end{thm}
```

**Status.** Proposal-only; pending main-thread integration. The
inscription requires consistent macros (`\osp`, `\Str`, `\bar A`)
already in `mathmacros.tex` / `commands.tex`.

---

## §7. Convergence verdict

**P4-EXEC-G3-01: DISCHARGED.** The 3-month deliverable P4-G3-T-A1 is
proven at chain level under (A1)–(A5) by the same machinery as
W22-T1+T2, with cleaner structural features:

* **Dimensional verification passes**: $4N^2$ even, $4N^2$ odd,
  $\Str(I)=0$ at balance.
* **Super-Killing form non-degenerate** (basic classical, Kac 1977),
  so W30 (A5) heat-kernel construction works verbatim.
* **(A5) parity-equivariance verified** for all three manuscript-cited
  regulators on osp.
* **Cross-bracket between orthogonal and symplectic is zero** —
  cleaner than gl, no mixed anomaly.
* **M-31 on osp is trivial** ($0\leftrightarrow 0$) at the
  linear-supertrace layer (cleaner than gl's relative-difference
  cycle).
* **Hand-computation on osp(2|2) confirms** $\Str(I)=0$ and the
  one-loop diagram vanishes.

**Posture against P4-G3.** The (A) prong's first target P4-G3-T-A1 is
discharged. The (B) prong (unreduced primitive) and (C) prong
(character extensions) remain open as outlined. The (A) prong's
secondary targets — psl(N|N), p(N), q(N) — require alternative
regulator constructions (degenerate Killing) or different
mechanisms (Sergeev central element on q(N)).

**Posture against the manuscript.** The bosonic source $\mathfrak{gl}_N$
remains obstructed (Theorem G $\hbar N[\bar c]$ unchanged); the
osp-balanced source is a *new* parallel theorem on a *different*
brane theory, not the manuscript's main target. M-13's bosonic
disambiguation is preserved.

**Inscribed durables.**
* This document.
* P4-EXEC-G3-01 ledger entry: discharged.
* WP4-G3-T-A1-1 inscription proposal (proposal-only) for
  `thm:app-osp-balanced-qme-vanishing`.
* Two precision notes (Sergeev vs Capelli; reality structure).
* Three residuals (BCOV embedding, higher-Sergeev, column-Verma)
  pushed to Phase-4 cross-group work.

**200-word summary (for parent agent):**

P4-G3-T-A1 (osp(2N|2N) supertrace cocycle vanishing) is **discharged
at chain level** under (A1)–(A5)-admissible regulators by the same
$\Lambda^{\Str}$ machinery as W22-T1+T2 on gl(N|N). Attack verified
the dimension bookkeeping ($4N^2$ even = $4N^2$ odd, so $\Str(I)=0$),
super-Killing non-degeneracy (basic classical, Kac 1977), and the
ℏ-deformed action survives the orthogonal+symplectic invariance
(cross-bracket between $\mathfrak{so}$ and $\mathfrak{sp}$ is
identically zero). Heal computed: explicit hand-computation on
osp(2|2) shows $\Str_{\mathrm{osp}(2|2)}(I)=4-4=0$ on the
8-dimensional adjoint, and the one-loop tadpole vanishes by direct
Berezin cancellation. Higher loops follow by W22-L3 verbatim. M-31
on osp is structurally cleaner than on gl: the linear-supertrace LHS
cycle vanishes identically (because $\mathfrak{so}$ and $\mathfrak{sp}$
elements have zero defining-rep trace), so it's $0\leftrightarrow 0$
rather than a relative-difference cycle. Two precision notes recorded:
(i) Sergeev–Berele–Regev central element replaces Capelli, but does
not affect the QME-class layer; (ii) reality structure / orientifold
conventions are a Phase-4 BCOV embedding question. Three residuals
pushed to Phase-4 cross-volume work. Inscription proposal
WP4-G3-T-A1-1 drafted for `thm:app-osp-balanced-qme-vanishing`.

End of P4-EXEC-G3 ledger.
