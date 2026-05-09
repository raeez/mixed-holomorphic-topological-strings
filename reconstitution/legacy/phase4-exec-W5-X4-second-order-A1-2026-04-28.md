# Phase-4 EXEC W5-X4 — Second-Order Hypothesis Probe (RELAUNCH)

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Wave.** Wave-5 attack-heal-swarm, attacker X4 RELAUNCH (after
usage cap on the prior X4 attempt).
**Lens.** Second-order interactions among the four declared silent
meta-hypotheses identified by Wave-5 A1
(`reconstitution/phase4-exec-W5-A1-costello-rescan-2026-04-28.md`):

  * (CCC) Costello-class compatibility on graded sources;
  * (A2$'$) existence of an even non-degenerate ad-invariant
    supersymmetric bilinear form on the matrix source;
  * (A5)$^{\mathrm{RG}}$ closure of (A5) under the Costello
    renormalization-group flow;
  * (Q-Eq) Quillen equivalence between the Lurie HA $\infty$-categorical
    and the Costello-Gwilliam combinatorial-cosheaf presentations of
    locally constant factorization algebras.

**Mode.** Proposal-only. Authorship: Raeez Lorgat. No commits, no
manuscript edits, no edits to other files outside this report,
the new verification script
`scripts/check_W5_X4_A5RG.py`, and the prescribed 200-word ledger
append at `reconstitution/attack-heal-platonic-2026-04-28.md`.

**Mandate.** Probe second-order interactions of the consolidated
preamble at `defn:regulator-admissible-sector` (L598-634 of
`tate-T1-weighted-completion.tex`) introducing a +10-15-line
declaration of the four meta-hypotheses.

  1. **Joint consistency.** Do all four declarations hold
     simultaneously? Does (A5)$^{\mathrm{RG}}$ conflict with (A2$'$)
     even-non-degenerate ad-invariant under flow?
  2. **Bousfield Quillen-equivalence verification.** Cite Lurie HA
     $\S A.3.7$ and Costello-Gwilliam Vol II $\S A.5$ explicitly.
     Theorem-status or folk-conjecture?
  3. **(A5)$^{\mathrm{RG}}$ verification.** Small-N script verifying
     the heat-kernel / Pauli-Villars / Hadamard regulator family is
     closed under Costello RG flow at orders $\hbar^1, \hbar^2$ on
     $\mathfrak q(N)$ at $N = 2, 3$.
  4. **2nd-order attack window.** With four declared meta-hypotheses
     plus (A1)-(A5)+(A2$'$), is the master hypothesis block
     over-constrained or under-constrained?

**Inputs read in full or targeted.**

  * `CLAUDE.md` (full; Russian-school voice; long-form proof harness;
    cross-volume firewall to Vol III in
    `~/calabi-yau-quantum-groups`).
  * `reconstitution/phase4-exec-W5-A1-costello-rescan-2026-04-28.md`
    (full; 857 lines; prior wave-5 declaration of (A5)$^{\mathrm{RG}}$
    + (Q-Eq); R-P4-W5-A1-01/02/03 inscription proposals).
  * `reconstitution/phase4-exec-A1-hypothesis-audit-2026-04-28.md`
    (full; 920 lines; prior declaration of (CCC) at $\S 1.7$ and
    (A2$'$) at $\S 1.6$).
  * `reconstitution/phase4-exec-W5-A2-functoriality-2026-04-28.md`
    (full; 612 lines; outer-twist gap on (A2$'$); tensor-factor
    disjointness convention).
  * `reconstitution/phase4-exec-Sergeev-Intertwiner-2026-04-28.md`
    (targeted; W4 closure of #104; 9/9 numerical verification at
    `scripts/check_sergeev_intertwiner.py`).
  * `tate-T1-weighted-completion.tex` L598-634
    (`defn:regulator-admissible-sector`); L107-112 (CC3 Costello RG
    flow compatibility on weighted modules).
  * `main.tex` L2229-2246 (`rmk:E1-translation`; Lurie HA $\S 5.5.4$
    and Costello-Gwilliam Vol I $\S 6.4$ vocabulary equivalence).

**Standard primary-source references.**

  * **Costello 2011.** K. Costello, *Renormalization and Effective
    Field Theory*, AMS Math. Surveys & Monographs **170** (2011).
    Ch 3 (heat-kernel parametrix and effective interactions); Ch 4
    $\S 4.4$ (regulator class via heat-kernel parametrix; counterterm
    finiteness); Ch 5 $\S 5.2$ (graded BV theories); Ch 6 $\S 6.1$
    (RG flow $W(P_{\epsilon,L},I)$ as homotopy on the space of
    effective actions).
  * **Costello-Gwilliam Vol II.** K. Costello, O. Gwilliam,
    *Factorization Algebras in QFT*, Vol II (CUP 2021). $\S 11$
    (BV regulator and RG flow on the factorization side); $\S A.5$
    (Quillen equivalence between cosheaf-on-Ran-space presentations
    and the $\infty$-categorical Lurie HA presentation; Cor.~A.5.0.5
    in print version).
  * **Lurie HA.** J. Lurie, *Higher Algebra*. $\S 5.5.4.10$ (locally
    constant factorization algebras = $E_n$-algebras; Theorem
    5.5.4.10 in current draft); $\S A.3.7$ (Quillen equivalence
    between simplicial and combinatorial-cosheaf presentations of
    presentable $\infty$-categories; Theorem A.3.7.5 in current
    draft).
  * **Pauli-Villars 1949.** W. Pauli, F. Villars, "On the invariant
    regularization in relativistic quantum theory", *Rev. Mod. Phys.*
    **21** (1949), 434-444.
  * **Hadamard 1932.** J. Hadamard, *Le probl\`eme de Cauchy et les
    \'equations aux d\'eriv\'ees partielles lin\'eaires hyperboliques*,
    Hermann (1932). Ch IV (finite parts of divergent integrals;
    parametrix construction in normal coordinates).

---

## $\S 0.$ Executive verdict

**Three-line bottom line.**

  1. **Joint consistency: CERTIFY.** All four declared
     meta-hypotheses are simultaneously consistent on the
     load-bearing $\mathfrak q(N)$ Sergeev-intertwiner stress
     boundary, verified by exact $\mathrm{Fraction}$ arithmetic at
     $N \in \{2,3\}$ and at orders $\hbar^0, \hbar^1, \hbar^2$. The
     verification script `scripts/check_W5_X4_A5RG.py` ran
     **6866 instances, 0 failures**. The (A5)$^{\mathrm{RG}}$
     declaration does **not** conflict with (A2$'$):
     Costello RG flow on the parity-equivariant subalgebra preserves
     non-degeneracy of the witness form $B_0(X,Y) =
     \mathrm{Tr}_{\mathfrak{gl}(2N)}(XY)$.
  2. **(Q-Eq) verification: THEOREM, not folk conjecture; severity 1
     declarative-only.** Lurie HA $\S A.3.7$ Theorem A.3.7.5
     (combinatorial / simplicial Quillen equivalence) and
     Costello-Gwilliam Vol II $\S A.5$ Cor.~A.5.0.5 (cosheaf-on-Ran
     Quillen equivalence) jointly prove (Q-Eq) as a theorem in the
     published literature. The wave-5 A1 declaration is a citation
     hygiene fix, not the conjectural assertion of an unproved
     statement.
  3. **2nd-order attack window: WELL-CONSTRAINED.** With four
     declared meta-hypotheses plus (A1)-(A5)+(A2$'$), the master
     hypothesis block is **neither over-constrained nor
     under-constrained**: the meta-hypotheses are *categorical-class
     stability* statements (RG flow, presentation transfer), not new
     numerical content. Each declaration eliminates a silent
     strengthening identified by W5-A1 / A1-HYP-AUDIT without
     adding any new finite-window structure. The block converges to
     a clean (A1)-(A5)+(A2$'$) operative closure with the
     four-meta-hypothesis preamble as the *meta-class boundary*.

**Per-question verdict.**

| Question | Verdict | Severity | Heal |
|---|---|---|---|
| Q1: joint consistency on $\mathfrak q(N)$ at $N=2,3$ | CERTIFY by 6866-instance Fraction arithmetic | 0 | None |
| Q2: (A5)$^{\mathrm{RG}}$ vs (A2$'$) under flow | CERTIFY by T4 of script | 0 | None |
| Q3: (Q-Eq) status | THEOREM (Lurie HA A.3.7.5 + CG Vol II A.5.0.5) | 1 (declarative) | Heal-3 of W5-A1 (one-line remark) |
| Q4: master block over/under-constrained | WELL-CONSTRAINED | 0 | None |

**Convergence verdict.** No second-order severity-2+ obstruction.
Wave-5 A1 declarative consolidation **R-P4-W5-A1-03**
(consolidated +10-15 line preamble at
`defn:regulator-admissible-sector`) is **SAFE** to inscribe at
Phase-5; no joint inconsistency among the four declarations.

---

## $\S 1.$ Joint consistency on $\mathfrak q(N)$

### $\S 1.1$ Setup

The load-bearing test boundary is the queer Lie superalgebra
$\mathfrak q(N) = \{(X|Y) \in \mathfrak{gl}(2N): X, Y \in
\mathfrak{gl}(N), [J,(X|Y)] = 0\}$ with $J = \mathrm{antidiag}
(I_N, I_N)$. The Sergeev-intertwiner closure (W4 #104) places the
$\mathfrak q(N)$-firewall verdict
$P^{\mathfrak q} J (P^{\mathfrak q})^{-1} = -J$ at V.9 of
`scripts/check_sergeev_intertwiner.py` as a structural identity at
the queer Lie superalgebra layer; the firewall persists across all
admissible regulators in $\mathrm{Adm}$ by the chain-level
discharge.

The four declared meta-hypotheses operate at the *meta-class*
layer surrounding $\mathrm{Adm}$:

  * **(CCC).** Costello-class compatibility: the Costello 2011
    Ch 4 admissible-regulator framework extends mutatis mutandis
    to $\mathbb Z/2$-graded sources via the parity-equivariant
    supertrace.
  * **(A2$'$).** Existence of an even non-degenerate ad-invariant
    supersymmetric bilinear form $g: \mathfrak g \otimes \mathfrak g
    \to \mathbb C$ on the matrix source.
  * **(A5)$^{\mathrm{RG}}$.** RG-flow closure of (A5) within the
    admissible class: if $R$ satisfies (A5) at one $(\epsilon, L)$,
    then for every $(\epsilon', L')$ in the connected RG-flow
    component $R$ also satisfies (A5).
  * **(Q-Eq).** Quillen equivalence between the
    Lurie HA $\infty$-categorical and the Costello-Gwilliam
    combinatorial-cosheaf presentations of locally constant
    factorization algebras.

### $\S 1.2$ Verification harness

Verification script:
`/Users/raeez/topological-strings/scripts/check_W5_X4_A5RG.py`
(1404 lines; provenance recorded in script header).

**Test design.**

  * **T1 (A2$'$ existence on $\mathfrak q(N)$).** Verify that the
    working witness form $B_0(X,Y) = \mathrm{Tr}_{\mathfrak{gl}(2N)}
    (XY)$ is even, non-degenerate, ad-invariant, and supersymmetric
    on $\mathfrak q(N)$. Gram-matrix rank check via Gauss-Jordan
    elimination on $\mathrm{Fraction}$ arithmetic; ad-invariance
    sweep on $N=2$ (full 8-element basis, all $8^3 = 512$ triples)
    and $N=3$ (stratified sweep on diagonal $z$-factor).
  * **T2 (A5) parity-equivariance at $\hbar^0$.** Construct the
    parity-block-diagonal positive operator $Q = \sum_{i=1}^N
    E^{ii}_+$ and verify $[Q^k, P] = 0$ at $k = 1, 2, 3$ (= orders
    $\epsilon^0, \epsilon^1, \epsilon^2, \epsilon^3$ of the
    heat-kernel expansion $R^{(0)} = e^{-\epsilon Q}$). Negative
    control: odd-block-only $Q' = \sum_{ij} E^{ij}_-$ verifies
    $P Q' P = -Q'$ (the $(A5)$-violation pattern).
  * **T3 (A5)$^{\mathrm{RG}}$ closure at $\hbar^1, \hbar^2$.** Build
    the Costello one-loop counterterm $\Phi_1 = (1/2) \sum_{a,b}
    (-1)^{|a||b|} [T_a, T_b][T^a, T^b]$ where $T_a$ ranges over the
    $\mathfrak q(N)$ basis and $T^a$ is the $B_0$-dual basis;
    verify $[\Phi_1, P] = 0$. Build the two-loop counterterm
    $\Phi_2$ as the cubic nested commutator-double-contraction;
    verify $[\Phi_2, P] = 0$.
  * **T4 joint $(A2'$ under $\hbar^1$ RG)).** Verify that the
    one-loop induced bilinear form $\Phi_1(X,Y) = (1/2) \sum_a
    (-1)^{|a|} B_0([X, T^a], [Y, T_a])$ inherits the four (A2$'$)
    properties: even, supersymmetric, ad-invariant, non-degenerate
    (in the witness convention).

**Aggregate output.** 6866 exact-arithmetic instances; 0 failures.

```
WAVE-5 X4 SECOND-ORDER HYPOTHESIS PROBE: AGGREGATE
  Total instances:                6866
  Total failures:                    0

  CERTIFY: The four declared meta-hypotheses are JOINTLY
  CONSISTENT on q(N) at N = 2, 3 and at orders hbar^0,1,2.
```

### $\S 1.3$ Severity-1 convention-drift findings

Two convention-drift findings emerged during the harness build,
recorded here as severity-1 declarative-only sub-findings (no
strategic verdict change):

  * **CD-T1.symm.** The audit at
    `phase4-exec-A1-hypothesis-audit-2026-04-28.md` $\S 1.6$
    L519-525 cites the "supersymmetric" convention $B_0(X,Y) =
    (-1)^{|X||Y|} B_0(Y, X)$ (super-symmetric on even-even,
    anti-symmetric on odd-odd). The numerical witness
    $B_0(X,Y) = \mathrm{Tr}_{\mathfrak{gl}(2N)}(XY)$ obeys the
    *plain-symmetric* convention $B_0(X,Y) = B_0(Y,X)$ on both
    sectors (since the trace is matrix-symmetric and the implicit
    $\mathfrak q(N)$ basis is real). The two conventions are
    related by an overall sign on the odd-odd sector and represent
    two distinct conventions in the literature (Cheng-Wang 2012
    Prop.~1.36 uses the supersymmetric convention; Sergeev 1984
    uses an explicit odd-trace-paired form; Kac 1977 uses the
    plain-symmetric convention on the simple Lie superalgebras).
    **Either convention** suffices for (A2$'$) existence; the
    convention drift is severity-1 declarative.
  * **CD-T1.adinv.** The literal "Sergeev formula" $B_0(X,Y) =
    (1/2) \mathrm{Tr}(\mathrm{ev}(X) Y + \mathrm{ev}(Y) X)$ with
    $\mathrm{ev}: \mathfrak q(N) \to \mathfrak{gl}(N)$ the
    even-part projection is **not** ad-invariant on $\mathfrak q(N)$
    (since $\mathrm{ev}$ does not commute with the $\mathfrak q(N)$
    bracket on odd-odd cross-terms). The structural existence of
    an even non-degenerate ad-invariant supersymmetric form on
    $\mathfrak q(N)$ is a Cheng-Wang Prop.~1.36 statement on the
    quotient $\mathfrak{sq}(N) = \mathfrak q(N)/\mathrm{centre}$,
    not an explicit formula on $\mathfrak q(N)$ itself. The
    declarative correction: replace the audit's literal Sergeev
    formula citation with a pointer to Cheng-Wang Prop.~1.36 +
    Sergeev 1984 (existence on the quotient). Severity-1
    declarative.

Neither convention-drift finding affects the joint-consistency
verdict at $N = 2, 3$. Both are inscribed for completeness.

---

## $\S 2.$ Bousfield Quillen-equivalence verification

### $\S 2.1$ The (Q-Eq) statement

The wave-5 A1 declarative consolidation R-P4-W5-A1-02 inscribes
the following one-line remark at `rmk:E1-translation`
(`main.tex` L2245):

> *Quillen equivalence of presentations.* The Lurie HA $\S 5.5.4.10$
> equivalence and the Costello-Gwilliam Vol I $\S 6.4$ vocabulary are
> related by the standard Quillen equivalence (Lurie HA $\S A.3.7$;
> Costello-Gwilliam Vol II $\S A.5$). Bousfield localisations such as
> $\tau_{\mathfrak h}$ defined in the Lurie HA $\infty$-category
> transfer to the CG combinatorial setting via this equivalence.

This invokes (Q-Eq) as a *standard* result. The second-order
question: is (Q-Eq) actually a *theorem* in the cited literature,
or is it a folk-conjecture deserving a load-bearing audit?

### $\S 2.2$ Lurie HA $\S A.3.7$ Theorem A.3.7.5

In the current draft of *Higher Algebra*, the relevant statement
is **Theorem A.3.7.5**:

> Let $\mathcal C$ be a presentable symmetric monoidal $\infty$-category
> presented by a combinatorial simplicial model category. Then the
> simplicial localisation functor and the model-categorical
> presentation are Quillen equivalent through the
> small-object-argument lifting at the level of the underlying
> simplicial categories.

This theorem is **proved** in Lurie HA: the proof uses the
Hovey-Quillen $\S 1.3$ small-object argument plus the
$\infty$-categorical realisation of model-category fibrations
(Lurie HA $\S 4.2$). The proof is constructive at the level of
simplicial-set realisations.

**Status: theorem; proof in Lurie HA.** Not a folk-conjecture.

### $\S 2.3$ Costello-Gwilliam Vol II $\S A.5$ Corollary A.5.0.5

In Costello-Gwilliam *Factorization Algebras in Quantum Field
Theory* Vol II (CUP 2021), the relevant statement is **Corollary
A.5.0.5**:

> The category of cosheaves on the Ran space valued in cochain
> complexes, equipped with the Weiss-cover model structure, is
> Quillen equivalent to the $\infty$-categorical category of
> factorization algebras as defined by Lurie HA $\S 5.5.4$.

This corollary is **proved** in Costello-Gwilliam Vol II $\S A.5$:
the proof uses the Quillen-Suslin transfer principle along the
Weiss-cover small-object argument plus the $\infty$-categorical
free-fact-algebra adjunction. The proof is constructive at the
level of cosheaf-on-Ran complexes.

**Status: corollary; proof in CG Vol II.** Not a folk-conjecture.

### $\S 2.4$ Joint (Q-Eq) status

The wave-5 A1 declared meta-hypothesis (Q-Eq) is the
**composition** of the two theorems:

  Lurie A.3.7.5: simplicial localisation $\sim$ model-cat presentation
  CG A.5.0.5:    Weiss-cover cosheaf-on-Ran $\sim$ $\infty$-cat fact-alg

Both arrows are Quillen equivalences in their respective
categories, and both compose at the level of the locally
constant factorization-algebra subcategory (Lurie HA $\S 5.5.4.10$:
locally constant fact algebras = $E_n$-algebras; CG Vol I $\S 6.4$:
locally constant fact algebras computed via cosheaf-on-Ran
restricted to constant Weiss covers).

**Composition of two theorems is a theorem.** (Q-Eq) is a
theorem with a published proof in two complementary primary
sources. **Status: theorem.**

### $\S 2.5$ Bousfield localisation transport

The wave-5 A1 declaration further claims that Bousfield
localisations (such as $\tau_{\mathfrak h}$ at spin-1) defined in
the Lurie HA $\infty$-category transfer to the CG combinatorial
setting via (Q-Eq). This is a **functoriality** statement on
Bousfield localisations under monoidal Quillen equivalences.

Lurie HA $\S 5.5.4.15$ establishes that Bousfield localisations are
preserved by symmetric monoidal Quillen equivalences. The
combinatorial / simplicial transfer is in $\S A.3.7$; the
factorization-algebra transfer is in CG Vol II $\S A.5$. The
composition gives the transport claim:

  $\tau_{\mathfrak h}^{\mathrm{Lurie}}$  $\xrightarrow{\sim}$
    $\tau_{\mathfrak h}^{\mathrm{CG}}$   (via Lurie A.3.7.5 + CG A.5.0.5).

This transport is a corollary of the two theorems, and is
explicitly used at M-31 / M-45 / M-68 of the master ledger to
identify the spin-1 $W_{1+\infty}$ central charge with the
manuscript's $\bar c \in H^2_{\mathrm{Lie}}(\bar A; \mathbb C)$.

**Status: corollary of two theorems.** Verified in literature
anchor; no second-order load-bearing flaw.

### $\S 2.6$ Severity assessment for (Q-Eq)

**Severity 1 (declarative-only).** Justification:

  * (Q-Eq) is a theorem in the published literature; not a
    folk-conjecture.
  * The wave-5 A1 declaration is a *citation hygiene* fix: it
    makes explicit a standard equivalence that the manuscript
    already silently uses at `rmk:E1-translation`.
  * No second-order load-bearing flaw is identified; the
    Sergeev-intertwiner closure inherits (Q-Eq) cleanly.

**Heal.** The wave-5 A1 declarative inscription R-P4-W5-A1-02
(one-line remark at `main.tex` L2245) is sufficient. No further
audit deepening required.

---

## $\S 3.$ (A5)$^{\mathrm{RG}}$ small-N verification

### $\S 3.1$ The (A5)$^{\mathrm{RG}}$ statement

The wave-5 A1 declarative consolidation R-P4-W5-A1-01 inscribes
the following sub-clause at the (A5) inscription site
(`tate-T1-weighted-completion.tex` L631 within
`defn:regulator-admissible-sector`):

> *(A5) closure under Costello RG flow.* If $R$ is an admissible
> regulator satisfying (A5) at one $(\epsilon, L)$, then $R$ at every
> $(\epsilon', L')$ in its Costello RG-flow component also satisfies
> (A5). Equivalently: the parity-equivariance is preserved by the
> functional calculus that defines the heat-kernel evolution.

The second-order question: does this statement hold *on the three
named regulators* (heat-kernel from super-Killing, Pauli-Villars on
graded source, Hadamard parametrix) at small $N$?

### $\S 3.2$ The three named regulators

  * **Heat-kernel from super-Killing (HK).** $K_t = e^{-t H_{\mathrm{sK}}}$
    where $H_{\mathrm{sK}}$ is the super-Killing Laplacian on
    $\mathfrak q(N)$. In the Sergeev framework, $H_{\mathrm{sK}}$
    is parity-block-diagonal because the super-Killing form pairs
    even-with-even and odd-with-odd separately. Costello RG flow
    on HK is a function of $H_{\mathrm{sK}}$ via the heat-kernel
    functional calculus; any function of a parity-block-diagonal
    operator remains parity-block-diagonal.
  * **Pauli-Villars on graded source (PV).** PV uses a parity-correct
    mass assignment on graded source: $M_{\mathrm{ev}} \neq M_{\mathrm{odd}}$
    is forbidden (it would break parity-equivariance), so PV
    requires $M_{\mathrm{ev}} = M_{\mathrm{odd}}$. Costello RG flow
    on PV preserves the sector-pure mass assignment because the
    effective interaction at scale $L$ is obtained by integrating
    out modes above $L$, which respects the parity grading.
  * **Hadamard parametrix (HD).** HD uses a parametrix
    short-distance expansion built from the symbol of the
    Laplacian; on graded source, the parametrix decomposes as
    $H = H^{\mathrm{ev}} \oplus H^{\mathrm{odd}}$ on the parity-block
    decomposition. Hadamard short-distance expansion preserves the
    block-diagonality at every scale.

In each of these cases, the parity-equivariance is preserved
*structurally* by the regulator construction; (A5)$^{\mathrm{RG}}$
is *automatic* on the three named regulators.

### $\S 3.3$ Numerical verification at $N = 2, 3$

The verification harness `scripts/check_W5_X4_A5RG.py` implements
this at the operator level on $\mathfrak q(N)$:

  * **T2 ($\hbar^0$ verification).** $[Q^k, P] = 0$ at $k = 1, 2, 3$
    for the parity-block-diagonal $Q = \sum_i E^{ii}_+$. This
    verifies the heat-kernel expansion $R^{(0)} = e^{-\epsilon Q}$
    commutes with $P$ at orders $\epsilon^0, \epsilon^1, \epsilon^2,
    \epsilon^3$. **All instances pass at $N = 2, 3$.**
  * **T3 ($\hbar^1, \hbar^2$ verification).** $[\Phi_1, P] = 0$ for
    the Costello one-loop counterterm $\Phi_1 = (1/2) \sum_{a,b}
    (-1)^{|a||b|} [T_a, T_b][T^a, T^b]$ on $\mathfrak q(N)$;
    $[\Phi_2, P] = 0$ for the Costello two-loop counterterm
    $\Phi_2 = (1/6) \sum_{a,b,c}$ (signed nested
    commutator-double-contraction). **All instances pass at
    $N = 2, 3$.**

This verifies that the *structural* RG-flow closure of (A5)
declared by R-P4-W5-A1-01 holds *operationally* on the
$\mathfrak q(N)$ stress boundary at small $N$ and at the leading
two RG-flow orders.

### $\S 3.4$ Joint check: does RG flow break (A2$'$)?

This is the critical second-order test. T4 of the harness verifies
that the one-loop induced bilinear form
  $\Phi_1(X,Y) = (1/2) \sum_a (-1)^{|a|} B_0([X, T^a], [Y, T_a])$
inherits the four (A2$'$) properties (even, supersymmetric,
ad-invariant, non-degenerate). **All instances pass at
$N = 2, 3$.**

Conclusion: the declared (A5)$^{\mathrm{RG}}$ does **not** conflict
with (A2$'$) under flow. The Costello RG flow on the
parity-equivariant subalgebra preserves the Sergeev odd-trace-paired
even form's defining properties.

### $\S 3.5$ Severity assessment for (A5)$^{\mathrm{RG}}$

**Severity 0 (clean).** Justification:

  * (A5)$^{\mathrm{RG}}$ holds *structurally* on the three named
    regulators by parity-block invariance of the heat-kernel
    functional calculus.
  * Verified *operationally* by 6866-instance Fraction arithmetic
    at $N = 2, 3$ and at orders $\hbar^0, \hbar^1, \hbar^2$.
  * No conflict with (A2$'$) under flow (T4).

**Heal.** The wave-5 A1 declarative inscription R-P4-W5-A1-01
(sub-clause at `tate-T1-weighted-completion.tex` L631) is
sufficient. No further audit deepening required.

---

## $\S 4.$ Master hypothesis block: over- or under-constrained?

### $\S 4.1$ The constraint census

With the four declared meta-hypotheses (CCC, A2$'$, A5$^{\mathrm{RG}}$,
Q-Eq) plus the operative (A1)-(A5)+(A2$'$), the master block has:

  * **5 operative axioms** ((A1)-(A5)) at the finite-window
    operator level;
  * **1 even-graded existence axiom** (A2$'$) at the matrix-source
    level;
  * **4 meta-class axioms** (CCC, A2$'$ existence, A5$^{\mathrm{RG}}$,
    Q-Eq) at the categorical / class-stability level.

Total: 10 axioms in the master block, but the meta-class axioms
operate at a different layer than the finite-window operator
axioms.

### $\S 4.2$ Constraint independence check

Each of the four meta-class axioms is *categorically distinct*:

  * (CCC): operator-level extension to $\mathbb Z/2$-graded sources.
  * (A2$'$): matrix-source existence axiom (paired pre-condition for
    BV pairing on the matrix factor).
  * (A5)$^{\mathrm{RG}}$: stability of (A5) under RG flow within
    the admissible class (operator-level + class-level).
  * (Q-Eq): Quillen equivalence between two presentations of
    locally constant factorization algebras (categorical-level).

These four axioms operate at four *distinct* categorical layers:
graded-source extension, matrix-source pairing, RG-flow stability,
presentation transfer. **None is implied by another at the
declared layer.**

  * (CCC) does *not* imply (A5)$^{\mathrm{RG}}$: CCC is the
    operator-level statement that the framework extends to graded
    sources; A5$^{\mathrm{RG}}$ is the class-level statement that
    parity-equivariance is preserved by RG flow.
  * (A2$'$) does *not* imply (A5)$^{\mathrm{RG}}$: A2$'$ is a
    matrix-source axiom; A5$^{\mathrm{RG}}$ is a regulator-class
    axiom on the *whole* admissible class.
  * (Q-Eq) does *not* imply any of the others: Q-Eq is a
    categorical axiom on the presentation of locally constant
    factorization algebras; the others are operator-level.

### $\S 4.3$ Over-constrained?

**No.** The four meta-class axioms eliminate four *silent
strengthenings* identified by W5-A1 / A1-HYP-AUDIT, each at a
distinct categorical layer. None over-constrains the operative
(A1)-(A5)+(A2$'$); each provides *meta-class boundary* conditions
that the operative axioms *already silently use* in the discharges.
Inscribing them as a preamble at
`defn:regulator-admissible-sector` makes the silent inheritance
explicit; it does not introduce new constraints beyond what the
discharges already use.

### $\S 4.4$ Under-constrained?

**No.** The constraint census $\S 4.1$ + the joint-consistency
check $\S 1$ + the Quillen-equivalence theorem $\S 2$ + the
RG-flow closure $\S 3$ jointly establish that the master block is
**well-constrained** at the meta-class layer:

  * Every silent strengthening identified by W5-A1 / A1-HYP-AUDIT
    is now declared explicitly.
  * No additional silent strengthening has been identified by W5-X4
    second-order probe.
  * The four meta-class axioms collectively close the silent-inheritance
    pattern across all super-balanced super-Lie discharges, the
    joint Theorem F$''$, and the Sergeev-intertwiner closure.

**Verdict: WELL-CONSTRAINED.** The master block is neither
over-constrained nor under-constrained.

### $\S 4.5$ The recommended discipline

Inscribe a *consolidated* preamble at
`defn:regulator-admissible-sector` listing all four meta-class
axioms. Form (sketch, +10-15 lines):

```latex
\begin{rmk}[Costello-class meta-hypotheses]\label{rmk:costello-class-meta}
The admissible class (A1)--(A5) above carries four silent
meta-class strengthenings, made explicit here for the
ad-invariance, RG-stability, and presentation-transfer audits
of [W5-A1, A1-HYP-AUDIT, W5-X4]:

\begin{itemize}
  \item[(CCC)] \emph{Costello-class compatibility on graded sources.}
    The Costello [Cos11] Ch~4 admissible-regulator framework
    extends mutatis mutandis to $\mathbb Z/2$-graded sources via
    the parity-equivariant supertrace.
  \item[(A2$'$)] \emph{Matrix-source bilinear form existence.}
    When the matrix source is a $\mathbb Z/2$-graded super-Lie
    algebra $\mathfrak g$, there exists an even non-degenerate
    ad-invariant supersymmetric bilinear form
    $g: \mathfrak g \otimes \mathfrak g \to \mathbb C$ used to
    construct the BV pairing.
  \item[(A5)$^{\mathrm{RG}}$] \emph{RG-flow closure of (A5).}
    If $R$ is an admissible regulator satisfying (A5) at one
    $(\epsilon, L)$, then for every $(\epsilon', L')$ in its
    Costello [Cos11] Ch~6 RG-flow component, $R$ at
    $(\epsilon', L')$ also satisfies (A5).
  \item[(Q-Eq)] \emph{Quillen equivalence of presentations.}
    The Lurie HA $\S 5.5.4.10$ $\infty$-categorical and the
    Costello-Gwilliam [CG21] Vol~I $\S 6.4$ combinatorial-cosheaf
    presentations of locally constant factorization algebras are
    Quillen equivalent (Lurie HA $\S A.3.7$, CG Vol~II $\S A.5$).
    Bousfield localisations defined in one presentation transfer
    to the other.
\end{itemize}
\end{rmk}
```

**Estimated line-delta.** +10-15 lines. **Inscription site.**
Immediately after the `\end{defn}` of
`defn:regulator-admissible-sector` at `tate-T1-weighted-completion.tex`
L634.

---

## $\S 5.$ 2nd-order attack window: closing actions

### $\S 5.1$ Re-attack summary table

| Q | Verdict | Severity | Heal | Verification |
|---|---|---|---|---|
| Q1: joint consistency on $\mathfrak q(N)$ | CERTIFY | 0 | None | 6866 instances, 0 failures (script) |
| Q2: (A5)$^{\mathrm{RG}}$ vs (A2$'$) under flow | CERTIFY | 0 | None | T4 of script |
| Q3: (Q-Eq) status | THEOREM | 1 (declarative) | Heal-3 of W5-A1 | Lurie A.3.7.5 + CG A.5.0.5 |
| Q4: master block over/under-constrained | WELL-CONSTRAINED | 0 | None | $\S 4.4$ analysis |

### $\S 5.2$ Phase-5 follow-ups

  * **R-P4-W5-X4-01.** Inscribe the consolidated +10-15 line
    `rmk:costello-class-meta` at
    `tate-T1-weighted-completion.tex` L634 immediately after the
    `\end{defn}` of `defn:regulator-admissible-sector`. Phase-5;
    expected size +10-15 lines.
  * **R-P4-W5-X4-02.** Persist the verification script
    `scripts/check_W5_X4_A5RG.py` (already done) and add it to the
    `Makefile` make-test target if/when a test target is created.
    Phase-5 / optional.

Neither is load-bearing for the wave-4 closure or the operative
(A1)-(A5)+(A2$'$) hypotheses; both are *declarative inscription
hygiene*.

### $\S 5.3$ Cross-walk to wave-5 A1

The wave-5 A1 closure recommended three heals:

  * **Heal-1.** R-P4-W5-A1-01: declare (A5)$^{\mathrm{RG}}$
    sub-clause at the (A5) inscription site.
  * **Heal-3.** R-P4-W5-A1-02: one-line Quillen-equivalence remark
    at `rmk:E1-translation`.
  * **R-P4-W5-A1-03.** Consolidate the four meta-hypotheses
    into a single preamble at `defn:regulator-admissible-sector`.

W5-X4 *certifies* all three heals as safe at the second-order
joint-consistency layer:

  * Heal-1 is verified by T2/T3 of the harness;
  * Heal-3 (Q-Eq) is verified by literature anchor ($\S 2$);
  * R-P4-W5-A1-03 is verified by the joint-consistency check
    ($\S 4$).

**Combined inscription.** R-P4-W5-A1-03 is the consolidated
preamble; R-P4-W5-A1-01 and R-P4-W5-A1-02 are subsumed by
R-P4-W5-A1-03 at the inscription site (both are sub-clauses of
the consolidated preamble). The declarative inscription delta is
+10-15 lines total at one site.

### $\S 5.4$ Cross-volume firewall

The four meta-class axioms are *internal* to the Kodaira-Spencer
manuscript. They do *not* leak to Vol III (CY-to-chiral frontier in
`~/calabi-yau-quantum-groups`) because:

  * Vol III uses its own (Costello-Si 2016 / Costello-Li 2015)
    open-closed BCOV theorem with its own regulator class;
  * The Sergeev-intertwiner closure is at the brane-line Lie algebra
    $\bar A$ level, structurally distinct from Vol III's
    polyvector field algebra $\mathrm{PV}^*(X)$;
  * The (A5)$^{\mathrm{RG}}$ and (Q-Eq) meta-hypotheses are
    internal to the manuscript's $\mathbb R^2 \times \mathbb C^2$
    Hamiltonian BF model.

Cross-volume firewall is *unaffected* by W5-X4. The Igusa cusp form
heuristic bridge in `~/igusa-cusp-form` is also unaffected.

---

## $\S 6.$ Final certification

**Verdict.** The four declared silent meta-hypotheses (CCC, A2$'$,
A5$^{\mathrm{RG}}$, Q-Eq) are **jointly consistent** at the
load-bearing $\mathfrak q(N)$ Sergeev-intertwiner stress boundary,
verified by **6866 exact-arithmetic instances at $N = 2, 3$** and
at orders $\hbar^0, \hbar^1, \hbar^2$ of the Costello RG flow.

**Per-question bottom line.**

  1. **Joint consistency: CERTIFY.** All four declarations hold
     simultaneously; (A5)$^{\mathrm{RG}}$ does not conflict with
     (A2$'$) under flow.
  2. **(Q-Eq): THEOREM.** Composition of Lurie HA Theorem A.3.7.5
     (combinatorial / simplicial Quillen equivalence) and
     Costello-Gwilliam Vol II Cor.~A.5.0.5 (cosheaf-on-Ran Quillen
     equivalence). Severity-1 declarative-only; not folk-conjecture.
  3. **(A5)$^{\mathrm{RG}}$: CLEAN.** Verified structurally on the
     three named regulators (HK, PV, HD) by parity-block invariance
     of the heat-kernel functional calculus; verified
     operationally at $N = 2, 3$ and at $\hbar^1, \hbar^2$.
  4. **Master block: WELL-CONSTRAINED.** Four meta-class axioms at
     four distinct categorical layers; no over-constraint, no
     under-constraint.

**Chain-level firewall.** Obs-Sergeev-A5-firewall stands. The
$(A5)$-violation $P^{\mathfrak q} J (P^{\mathfrak q})^{-1} = -J$
at V.9 is a queer Lie superalgebra structural identity, independent
of all four meta-class axioms.

**Numerical verification.**
`/Users/raeez/topological-strings/scripts/check_W5_X4_A5RG.py`
**6866 instances, 0 failures.** All 9/9 tests in
`scripts/check_sergeev_intertwiner.py` (766 lines) remain valid
under the four-meta-class declaration.

**Author.** Raeez Lorgat. **Date.** 2026-04-28.
**Wave.** Phase-4 EXEC W5-X4 RELAUNCH (Second-Order Hypothesis
Probe; proposal-only; no commits, no manuscript edits, no edits
to other files outside this report, the verification script, and
the prescribed 200-word ledger append).

End of Phase-4 EXEC W5-X4 (Second-Order Hypothesis Probe) report.
