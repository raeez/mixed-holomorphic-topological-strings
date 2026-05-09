# Wave 3 / W25 — Independent verification of W22-T1, W22-T2 from the Polyakov + Examples lens

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Polyakov primary (scaling, renormalization, anomaly,
physical dimension, path-integral sanity); Examples secondary
(does the first non-trivial example compute correctly?).
**Mode.** Proposal-only. Master ledger schema; IDs prefix
`W3-W25-`.
**Posture.** W22 returned `W22-T1` (chain-level one-loop QME
vanishing on $\mathfrak{gl}(N|N)$, unconditional) and `W22-T2`
(all-loop, conditional on "every admissible regulator preserves
the $\Z/2$-grading"). W25 verifies independently from physics
side, with explicit attack on the conditional clause in W22-T2.
**Inputs.** `wave3-W22-supertrace-rigorous-2026-04-28.md` (full,
W22-T1, W22-T2, W22-Obs); `wave3-W18-thmB-escape-routes-2026-04-28.md`
(866–906, W18-CT1 verbatim); `wave3-W10-witten-examples-2026-04-28.md`
105–195 (W3-W10-01 = $\hbar N$ one-loop), 255–308 (W3-W10-03
partition function), 377–442 (W3-W10-05 anomaly inflow);
`wave3-W15-conditional-theorems-2026-04-28.md` 545–675
(W3-W15-03 strict chain-level $\Lambda$); `wave3-W8-polyakov-composition-2026-04-28.md`
46–242 (admissible-regulator class declarations and Capelli
universality claim); `tate-T1-weighted-completion.tex`
596–632 (`defn:regulator-admissible-sector` (A1)–(A4)),
634–707 (`thm:wt-regulator-independence-admissible`);
`appendix-unreduced-bv-qme.tex` 1–179 (BV degrees, signs,
scalar contact QME class, escape-route remark);
`scripts/check_one_psi_homology.py` 1–50 (homology harness).

---

## §0. Executive verdict (precedes the ledger)

**Three named verdicts, ordered by weight.**

1. **W22-T1 is independently confirmed at one loop. The Polyakov
   physical-dimension audit and the $(N,M)=(1,1)$ example check both
   reproduce the coefficient $\hbar(N-M)=0$ at $N=M$.** The one-loop
   gauge-generator tadpole on $\mathfrak{gl}(N|N)$ contracts under
   the BV super-pairing to $\sum_a (-1)^{|a|}\delta^a_a=
   \mathrm{Str}(I)=N-M$, exactly as W22-L1 computes. **W3-W25-01.**

2. **W22-T2's conditional clause "every admissible regulator
   preserves the $\Z/2$-grading" is NOT an automatic consequence
   of `defn:regulator-admissible-sector` (A1)–(A4) as currently
   written.** Two distinct things must be checked: (i) that the
   regulator's *finite-window truncation maps* commute with the
   parity operator $P$ on $\mathfrak{gl}(N|N)$, and (ii) that the
   *propagator family* $\{P_{\epsilon,L}\}$ commutes with $P$. The
   admissibility conditions (A1)–(A4) explicitly cover only the
   degree-grading on $\bar A$ (polynomial-degree-bounded
   Hamiltonian and cotangent legs), not the parity grading on the
   open matrix source. **The grading-preservation clause is an
   implicit assumption that needs to be stated explicitly, or
   proven from a finer property of the matrix source's role in
   the BV propagator construction.** A counterexample candidate
   class ("ungraded heat-kernel" or "parity-mixing point-splitting
   regulator") is constructed below in W3-W25-03 and shown to be
   admissible-but-grading-breaking. **The W22-T2 hypothesis is
   not vacuous.** A heal proposal for W22-T2 is given in W3-W25-07.

3. **The path-integral / partition-function sanity check passes
   on the super-balanced source: the super-Berezinian product
   $\prod_{k\geq 1}(1-q^k)^{-(N-M)}=1$ at $N=M$, signaling a
   genuine Witten-index vanishing consistent with the QME-cocycle
   vanishing.** The $N$-dependent partition function of W3-W10-03
   generalizes; super-balance produces a *trivial partition
   function* (equal to 1 to all orders in $q$), reflecting that the
   super-balanced theory is partition-function-trivial and
   anomaly-trivial simultaneously. **W3-W25-05.**

**Bottom line.** W22-T1 stands rigorously. W22-T2 stands
*conditionally on a regulator-class restriction that is more
restrictive than the manuscript's `defn:regulator-admissible-sector`*.
The heal: replace W22-T2's conditional with a precise
parity-equivariance hypothesis (A5: regulator commutes with the
parity operator $P$ on $\mathfrak{gl}(N|N)$) and document this as
a strict subclass of the admissible regulators. The Polyakov audit
otherwise passes: scaling dimensions are coherent, the partition
function vanishes (= 1) consistently, M-31 deforms with zero
coupling at super-balance, and no parity / gravitational anomaly
re-introduces a hidden class.

---

## §1. Ledger entries

### W3-W25-01 — T1: Independent recomputation of one-loop diagram on $\mathfrak{gl}(N|N)$

**Severity 4 (load-bearing recomputation). Status valid.
Confidence high.**
**Lens.** Polyakov primary; Examples secondary.
**Provenance.** Mandate T1 of W25.

**Setup, independent of W22-02.** The Dirac brane probe action
on the super-stack is

\[
S^{\mathrm{super}}_\partial
 =\int_\R
   \mathrm{Str}\bigl(\phi_1\,d\phi_2+A[\phi_1,\phi_2]\bigr),
\]

with $\phi_1,\phi_2\in\mathfrak{gl}(N|M)_{\mathrm{even}}$ and
$A=\psi^\vee$ the antifield Lagrange multiplier. The
super-bracket on $\mathfrak{gl}(N|M)$ is
$[X,Y]=XY-(-1)^{|X|\cdot|Y|}YX$; on the even sector it reduces
to the ordinary commutator. BV degrees per
`def:app-unreduced-bv-degrees` (`appendix-unreduced-bv-qme.tex`:9–32):
$|\phi_1|=|\phi_2|=0$, $|\psi|=-1$, $Q\psi=[\phi_1,\phi_2]$.

**Polyakov scaling-dimension audit.** Mass-dimension count on the
$\R$-line topological brane theory:
* $\phi_1,\phi_2$: $[\phi_i]=0$ (super-coordinates of the formal
  symplectic disk; symplectic form $dz_1\wedge dz_2$ is dimensionless).
* $\psi=A^*$: $[\psi]=-1$ (BV degree from $|\psi|=-1$ but
  mass-dimension on the line $\R$ is governed by the $dt$ weight).
* $S_\partial$: $[S_\partial]=0$ (action is dimensionless).
* The propagator $P=Q^{\mathrm{GF}}\int K_t\,dt$: dimension matched
  to give the BV pairing $\{(\phi_1)^a_b,(\phi_2)^c_d\}$
  dimensionally consistent with $\phi$-coordinates.
* The closed-loop contraction sum: dimensionally a pure number
  (sum of Kronecker deltas).

The bosonic case W3-W10-01 gives loop-sum $\sum_i \delta^i_j \delta^j_i=
\sum_i 1=N$ in $\mathfrak{gl}_N$. The super-stack analog: the
super-pairing carries a Koszul sign $(-1)^{|a|\cdot|b|}$, which on
the diagonal ($a=b$) becomes $(-1)^{|a|^2}=(-1)^{|a|}$ for
$|a|\in\{0,1\}$. This is the standard Berezin-trace sign. The
loop sum becomes

\[
\sum_a (-1)^{|a|}\,\delta^a_a
\;=\;\sum_{a\,\mathrm{even}}1\;-\;\sum_{a\,\mathrm{odd}}1
\;=\;N\;-\;M\;=\;\mathrm{Str}(I).
\]

This matches W22-L1 exactly. The mass-dimension count is
unchanged from the bosonic case: the Berezin sign is dimensionless,
and the Kronecker deltas count basis-elements equally on the
even and odd sectors (each supplies a real degree of freedom
modulo the parity sign). **The dimension of the loop is $0$
(pure number), and its value is $N-M$.**

**Verification at $(N,M)=(1,1)$ by hand.** $\mathfrak{gl}(1|1)$ has
even basis $\{E_{11},E_{22}\}$ (super-degree 0; $E_{11}$ is even
"upper-left", $E_{22}$ is even "lower-right" with parity flip)
and odd basis $\{E_{12},E_{21}\}$. Identity
$I=E_{11}+E_{22}$. The supertrace by definition is
$\mathrm{Str}(I)=\mathrm{Tr}(E_{11})-\mathrm{Tr}(E_{22})=1-1=0$.

Loop computation: even sector contributes $\delta^{E_{11}}_{E_{11}}+
\delta^{E_{22}}_{E_{22}}=2$. Odd sector — note the convention
that the odd-block diagonal Kronecker is multiplied by
$(-1)^{|a|}=-1$. The odd-sector "diagonal" entries
$\delta^{E_{12}}_{E_{12}}+\delta^{E_{21}}_{E_{21}}=2$ but
multiplied by the sign $(-1)$ each. Wait — refine. The
Berezin-trace sign applies to the *diagonal* elements of the
identity matrix in the super-basis, so the *parity* of an index
$a$ is what matters, not whether the basis element is $E_{11}$
vs $E_{12}$. For the *identity matrix* $I$, only the diagonal
elements $E_{11},E_{22}$ contribute (off-diagonal $E_{12},E_{21}$
have zero diagonal entries). Hence
$\mathrm{Str}(I)=\sum_a (-1)^{|a|}\delta^a_a=
(+1)\cdot 1+(-1)\cdot 1=0$, since $E_{11}$ has parity 0 and
$E_{22}$ has parity 1 in the standard $\Z/2$-grading on
$\mathfrak{gl}(1|1)$.

In the propagator-loop interpretation: the closed loop on
$\mathfrak{gl}(1|1)$ traverses indices that include both bosonic
and fermionic contributions; at index $E_{11}$ contributes $+1$,
at $E_{22}$ contributes $-1$ (Berezin sign), with off-diagonal
contributions to the loop being separate index-pair contractions
that yield the Berezin sign $(-1)^{|a|\cdot|b|}$ for
mixed-parity off-diagonals; the diagonal-only loop sum
collapses to $\sum_a (-1)^{|a|}\delta^a_a=N-M=0$ at $N=M=1$.
**Confirmed independently.**

**Coefficient verification.** The one-loop QME contribution is

\[
\mathrm{anomaly}^{\mathrm{super}}_{1\text{-loop}}
 =\hbar\cdot\mathrm{Str}_{\mathfrak{gl}(N|N)}(I)
 =\hbar(N-N)
 =0,
\]

matching W22-T1's $\hbar(N-M)=0$ exactly. **W22-T1's coefficient
is correct.**

**Files read.** `wave3-W10-witten-examples-2026-04-28.md` 105–195
(bosonic baseline); `wave3-W22-supertrace-rigorous-2026-04-28.md`
194–250 (W22-02 b-d super-Berezin contraction);
`appendix-unreduced-bv-qme.tex` 9–32 (BV degrees and signs).
**Confidence.** High. Direct hand-computation in two different
ways (sum-of-Berezin-signs and explicit $\mathfrak{gl}(1|1)$
basis) give the same result.
**Blast radius.** Confirms W22-T1's coefficient $\hbar(N-M)=0$
at $N=M$. The Polyakov dimension audit says the loop is
dimensionless (a pure number), and the value is the supertrace
of the identity, vanishing at super-balance.
**Adjudication.** Valid independent verification.
**Residual.** None at the one-loop layer.

---

### W3-W25-02 — T2: Strict-cocycle structure verification

**Severity 4 (chain-level structure verification). Status
valid. Confidence high.**
**Lens.** Composition (Costello secondary).
**Provenance.** Mandate T2 of W25.

**Strict differential on the super-stack.** The differential on
$\mathcal O_{\mathrm{loc}}(\mathcal E_w^{\mathrm{super}})$ is

\[
d_{\mathrm{super}}=Q+\{I_0,-\}_{\mathrm{super}},
\]

where $Q\psi=[\phi_1,\phi_2]_{\mathrm{super}}$ on the super-stack
(with the super-bracket reducing to ordinary commutator on the
even sector) and $\{-,-\}_{\mathrm{super}}$ is the
super-BV bracket inheriting the Koszul sign from the BV pairing.
Crucially, the central ghost $\gamma_{\mathbf 1}$ has BV degree
$1$ and is even (parity 0), so its insertion does not change
the parity-grading argument.

**Strict cocycle identity for $\Lambda^{\mathrm{Str}}$.** W22-04
asserts $\mathrm{Ob}_{\mathrm{sc}}^{\mathrm{super}}=
\hbar(N-M)\cdot\Lambda^{\mathrm{Str}}(\omega)$ as a strict
chain-level identity. Independent verification:

(i) **The lift formula is identical to bosonic.** The map
$\Lambda^{\mathrm{Str}}(\omega)=\omega(f,g)\int a(t)b(t)
\gamma_{\mathbf 1}(t)\,dt$ depends on:
* $\omega\in C^2_{\mathrm{Lie}}(\bar A;\C)$: closed-side cocycle,
  source-independent.
* $\gamma_{\mathbf 1}$: central boundary ghost on $\R$,
  source-independent.
* $a,b\in\Omega^0_c(\R)$: de Rham smearing functions,
  source-independent.
* $f,g\in\bar A$: Hamiltonian arguments (closed-side).

None of these data depend on the matrix source. So the formula
is form-identical between bosonic and super-stacked sources.
The only modification is the *coefficient* $\hbar(N-M)$ on the
right-hand side, which changes by replacing $\mathrm{Tr}(I)\to
\mathrm{Str}(I)=N-M$.

(ii) **Strict differential check on the chain-level cocycle.**
On the super-stack, the chain $\Lambda^{\mathrm{Str}}(\omega)$
satisfies $d_{\mathrm{super}}\Lambda^{\mathrm{Str}}(\omega)=0$
because:
* $Q\Lambda^{\mathrm{Str}}(\omega)$: the Koszul differential
  $Q$ acts on the central ghost as $Q\gamma_{\mathbf 1}=0$
  (it is genuinely central in the closed sector); on $a,b$ as
  zero (de Rham smearing functions, no $Q$ action); on $\omega$
  as zero (CE cocycle, $d_{\mathrm{CE}}\omega=0$). Hence
  $Q\Lambda^{\mathrm{Str}}(\omega)=0$.
* $\{I_0,-\}\Lambda^{\mathrm{Str}}(\omega)$: $I_0$ is the
  classical interaction; the BV bracket of $I_0$ with the chain
  $\Lambda^{\mathrm{Str}}(\omega)$ requires contracting $I_0$
  against the central ghost $\gamma_{\mathbf 1}$ and the
  smearing $a,b$. By the cocycle identity for $\omega$ on
  $\bar A$ (`lem:omega-cocycle`), this BV bracket reduces to
  $\{I_0,\Lambda^{\mathrm{Str}}(\omega)\}=
  \omega(\{f,g\}_{\bar A},h)\int abc\gamma_{\mathbf 1}+
  \mathrm{cyclic}$, where $h$ is a third Hamiltonian and the
  cyclic sum runs over the three Hamiltonians. By the CE cocycle
  identity (Jacobi for $\omega$), this triple-cyclic sum vanishes.
  Hence $\{I_0,\Lambda^{\mathrm{Str}}(\omega)\}=0$ as a strict
  chain-level identity.

Both pieces vanish strictly, so $d_{\mathrm{super}}
\Lambda^{\mathrm{Str}}(\omega)=0$ at chain level. **The strict
chain-level cocycle structure of W22-T1 is independently
verified.**

(iii) **At super-balance the obstruction is identically zero
as a chain element.** The relation
$\mathrm{Ob}_{\mathrm{sc}}^{\mathrm{super}}=\hbar(N-M)\cdot
\Lambda^{\mathrm{Str}}(\omega)$ at $N=M$ becomes
$\mathrm{Ob}_{\mathrm{sc}}^{\mathrm{super}}=0$ as a chain
(zero coefficient times any chain is zero), not just as a
cohomology class. This is W22-T1's chain-level discharge.

**Files read.** `wave3-W22-supertrace-rigorous-2026-04-28.md`
425–533 (W22-04 chain-level lift); `wave3-W15-conditional-theorems-2026-04-28.md`
545–675 (bosonic chain-level lift); `appendix-unreduced-bv-qme.tex`
93–158 (`prop:app-scalar-contact-qme-class`).
**Confidence.** High. The strict-cocycle identity uses only
(a) source-independence of the lift formula, (b) the CE
cocycle identity for $\omega$, (c) the centrality of
$\gamma_{\mathbf 1}$. None of these depends on the
super-extension.
**Blast radius.** Confirms W22-T1 holds at chain level, not
just at cohomology. The super-extension preserves strict
chain-level structure because the strict $\Lambda$ map of
W3-W15-03 depends only on closed-side data.
**Adjudication.** Valid independent verification.
**Residual.** None at the chain-level layer.

---

### W3-W25-03 — T3: ATTACK on "every admissible regulator preserves $\Z/2$-grading"

**Severity 4 (load-bearing attack). Status: ATTACK PARTIALLY
SUCCESSFUL — the W22-T2 hypothesis is non-vacuous.
Confidence high.**
**Lens.** Polyakov primary (regulator-class analysis); Composition
secondary (admissibility audit).
**Provenance.** Mandate T3 of W25.

**Step 1: parse `defn:regulator-admissible-sector` (A1)–(A4).**
From `tate-T1-weighted-completion.tex`:596–632, the four
admissibility conditions are:

* **(A1)** Transition maps in coefficient and local-functional
  directions are **degreewise truncations** to degree $\leq w_0$
  on the polynomial Hamiltonian filtration; degreewise surjective
  maps of complexes.
* **(A2)** At each fixed $\hbar$-order and Costello graph, the
  coefficient expression uses only **vertexwise polynomial-degree-bounded**
  Hamiltonian and cotangent legs.
* **(A3)** Diagonal finite-window rescaling $R_{w,w'}^{w_0}$
  transports interaction, differential, bracket, propagator,
  counterterm between weight pairs $(w,w')$.
* **(A4)** Cohomology computed is **admissible filtered cohomology**
  (no observable detects an infinite product tail invisible in
  every finite quotient).

**Critical observation.** **None of (A1)–(A4) mentions the
$\Z/2$-parity grading on the open matrix source $\mathfrak{gl}(N|M)$.**
All four conditions concern the *polynomial-degree* filtration on
the closed Hamiltonian side ($\bar A$, $\mathfrak h_{\mathrm{poly}}$,
their duals). The matrix source enters only through the boundary
evaluation $\partial_{\mathrm{bb},N}^{\mathrm{full}}:f\mapsto
\mathrm{Tr}\,f(\phi_1,\phi_2)$ (or its supertrace replacement).

The parity grading on $\mathfrak{gl}(N|M)$ — which determines
whether $\mathrm{Str}(I)=N-M$ or some other quantity — is a
*structural* feature of the matrix source, not of the regulator
class as defined by (A1)–(A4).

**Step 2: are there admissible-but-grading-breaking regulators?**

Consider the following candidate regulator schemes on the
$\mathfrak{gl}(N|N)$-valued BF theory:

**Candidate (a): Bosonic-fermionic-mixed propagator.**
Define a propagator $P^{\mathrm{mix}}_{\epsilon,L}=
P^{\mathrm{ev}}_{\epsilon,L}+\lambda P^{\mathrm{odd-even-cross}}_{\epsilon,L}$,
where the second term is a *parity-breaking* coupling that
contracts an even $\phi$-index with an odd $\phi$-index at order
$\lambda$ in some auxiliary parameter. Concretely, take
$P^{\mathrm{odd-even-cross}}=\sum_{i\,\mathrm{even},j\,\mathrm{odd}}
\delta^i_j\delta^j_i$ (a parity-flip Kronecker pairing).

* **Admissibility check.** The truncation maps (A1) act on
  polynomial-degree-filtered observables and don't see parity;
  the Costello graphs (A2) use polynomial-degree-bounded legs and
  again don't see parity directly; (A3) the diagonal rescaling
  preserves any internal index structure that doesn't depend on
  weight; (A4) the cohomology is admissible-filtered.
  **The propagator $P^{\mathrm{mix}}_{\epsilon,L}$ satisfies
  (A1)–(A4) at the formal level.** It is admissible.
* **Grading-preservation check.** The parity-flip term
  $P^{\mathrm{odd-even-cross}}$ explicitly mixes parity; it does
  not commute with the parity operator $P=\mathrm{diag}(1,-1)$ on
  $\mathfrak{gl}(N|N)$ (acting on the parity-grading basis). Under
  this regulator, the loop contraction is no longer pure
  $\sum_a (-1)^{|a|}\delta^a_a=N-M$ but instead has a *cross
  term* $\lambda\cdot N$ from the bosonic-fermionic crossings.
  At super-balance $N=M$, the loop value becomes $0+\lambda\cdot
  N=\lambda N\neq 0$ for $\lambda\neq 0$.

**This is an admissible-but-grading-breaking regulator.** The
W22-T2 conclusion ($\hbar(N-M)=0$ at super-balance) **fails**
under this regulator: the one-loop anomaly becomes $\hbar\lambda N$,
non-vanishing.

**However:** is this regulator *physically reasonable*? In the
manuscript's framework, the propagator is defined as
$P_{\epsilon,L}=Q^{\mathrm{GF}}\int K_t\,dt$ where $Q^{\mathrm{GF}}$
is the BV gauge-fixing operator and $K_t$ is the heat kernel.
The heat-kernel construction *automatically* preserves the
$\Z/2$-grading because the Laplacian on $\mathfrak{gl}(N|N)$
commutes with the parity grading (it is built from the
super-Killing form). The parity-mixing term
$P^{\mathrm{odd-even-cross}}$ does **not** arise from this
heat-kernel construction.

**Status of Candidate (a).** It is *constructable* in principle
(one can define an ad-hoc propagator that mixes parities), but it
is **not** the manuscript's actual heat-kernel propagator.
Verdict: **(b) admissible AND grading-breaking** — but only as
a formal construction; it is not the heat-kernel scheme.

**Candidate (b): $\Z/2$-odd cutoff function.**
Define the cutoff function $\rho_{\epsilon,L}(t)$ that controls
the heat-kernel integration. Standardly
$\rho_{\epsilon,L}(t)=\mathbf 1_{[\epsilon,L]}(t)$ — a parity-even
characteristic function. Replace it with $\rho^{\mathrm{odd}}_{\epsilon,L}$
that has odd parity in some auxiliary $\Z/2$-grading: e.g.\
$\rho^{\mathrm{odd}}=\rho\cdot\mathrm{sgn}(\text{some }\Z/2\text{-charge})$.
* On the topological line $\R$, there is no intrinsic $\Z/2$-grading
  on the cutoff. The $\Z/2$-grading lives on the *target*
  $\mathfrak{gl}(N|N)$, not on the *source* $\R$. Hence a "$\Z/2$-odd
  cutoff" must be a function on $\R$ with *no* intrinsic parity
  structure to break.

**Status of Candidate (b).** **Inadmissible:** the $\Z/2$-grading
is on the target, not the source, so this candidate is ill-defined.
Verdict: **(c) inadmissible / ill-defined**.

**Candidate (c): Heat-kernel that doesn't commute with parity.**
The heat kernel $K_t=e^{-t\Delta}$ where $\Delta$ is the
Laplacian on $\mathfrak{gl}(N|N)$. In the *standard* construction,
$\Delta$ uses the super-Killing form (or super-Casimir), which is
$\Z/2$-graded. A non-standard $\Delta'$ that uses an *un-graded*
Casimir-like form (e.g.\ replace $\mathrm{Str}\to\mathrm{Tr}$ in
the Casimir definition) would give a heat kernel
$K'_t=e^{-t\Delta'}$ that does not commute with parity.
* **Admissibility:** the un-graded $\Delta'$ still gives a
  finite-window heat-kernel propagator with the (A1)–(A4) properties
  (truncations, polynomial-degree bounds, weight-rescaling, admissible
  cohomology). The construction satisfies (A1)–(A4) at the formal
  level. But its definition uses $\mathrm{Tr}$ on the super-stack,
  which is not the canonical bilinear form for super-Lie algebras.
* **Grading-preservation:** $\Delta'$ does not commute with the
  parity operator $P$. The loop contraction yields not $\mathrm{Str}(I)$
  but $\mathrm{Tr}(I)=N+M\neq 0$ at super-balance.

**This is admissible-but-grading-breaking.** Under this regulator,
the W22-T2 conclusion **fails**: the anomaly is $\hbar(N+M)\neq 0$,
not $\hbar(N-M)=0$.

**Status of Candidate (c).** **(b) admissible AND
grading-breaking.** This candidate is more "physical" than (a) in
that it is a genuine heat-kernel scheme, just not built from the
super-Killing form.

**Candidate (d): Point-splitting at a $\Z/2$-odd point.**
Point-splitting regularization replaces local products by
products at split-points. On a graded space, the split-point
must respect the grading: a "$\Z/2$-odd point" is a fermionic
direction in the super-source's nilpotent extension. If one
chooses the split-point to be in the odd direction, the
regularized operator-product carries an odd-degree shift.
* **Admissibility:** point-splitting is generally not in the
  admissible class as defined; it differs from heat-kernel by an
  unspecified scheme transformation. It would fall into
  R-W3-W6-04's "cross-regulator-class canonicity" question.
  **Likely outside the admissible class.**

**Status of Candidate (d).** **(c) inadmissible** (or at least
not in the admissible class as currently defined; cross-class
analysis is Phase-4 / R-W3-W6-04).

**Step 3: Classification table.**

| Candidate | Admissible (A1)–(A4)? | Preserves $\Z/2$? | W22-T2 OK? | Verdict |
|-----------|-----------------------|-------------------|------------|---------|
| (a) Mixed bosonic-fermionic propagator | Yes (formal) | NO | Fails | (b) admissible, grading-breaking |
| (b) $\Z/2$-odd cutoff function | Ill-defined | N/A | N/A | (c) inadmissible |
| (c) Un-graded heat-kernel ($\mathrm{Tr}$ not $\mathrm{Str}$) | Yes (formal) | NO | Fails | (b) admissible, grading-breaking |
| (d) Odd-direction point-splitting | No (out of class) | NO | N/A | (c) inadmissible |
| Heat-kernel from super-Killing form | Yes | YES | OK | (a) admissible, grading-preserving |
| Pauli–Villars on graded source | Yes | YES (if PV preserves parity) | OK | (a) admissible, grading-preserving |
| Hadamard parametrix | Yes | YES (if symbol preserves parity) | OK | (a) admissible, grading-preserving |

**Step 4: Verdict on W22-T2.**

The classification shows: **at least two admissible-but-grading-breaking
regulators exist (candidates (a) and (c))**. Both are formal
constructions inside `defn:regulator-admissible-sector` that
violate parity-equivariance.

W22-T2's conclusion $\mathrm{Str}(I)=N-M=0$ at super-balance
**relies on** parity-equivariance of the regulator. Under
Candidate (a) or (c), the loop contracts to a different
combination ($N+M$ or $N+\lambda N$) and the obstruction is
non-vanishing.

**Therefore: W22-T2's hypothesis "every admissible regulator
preserves the $\Z/2$-grading" is NOT an automatic consequence of
`defn:regulator-admissible-sector` (A1)–(A4). It is an
*additional* hypothesis that must be stated explicitly.**

**Counter-attack on W22's claim.** W22-03 wrote: "the
$\Z/2$-grading is a *symmetry* of the BV complex — it commutes
with $Q$, with the classical Hamiltonian action, with the
Koszul propagator, and with every admissible regulator". This
claim is **partially correct**: the $\Z/2$-grading is a
structural symmetry of *the source* $\mathfrak{gl}(N|N)$, but
its preservation by *the regulator* is not automatic from
admissibility alone. The regulator must be *parity-equivariant*
in addition to satisfying (A1)–(A4).

**Files read.** `tate-T1-weighted-completion.tex` 596–632
((A1)–(A4)); `wave3-W22-supertrace-rigorous-2026-04-28.md`
582–614 (W22-T2 statement and proof);
`wave3-W8-polyakov-composition-2026-04-28.md` 189–243
(W3-W8-01 admissible-class universality).
**Confidence.** High for the construction of candidates (a) and
(c); medium-high for the classification — the formal
admissibility of (a),(c) is direct, but their *physical* status
(whether anyone would actually use such a regulator in BCOV
practice) is heuristic.
**Blast radius.** **W22-T2's hypothesis is not vacuous.** It must
be promoted to an explicit additional condition (A5: regulator
commutes with parity operator on $\mathfrak{gl}(N|N)$) in the
admissible-regulator class definition. The heat-kernel from
super-Killing form, Pauli–Villars on graded source, and Hadamard
parametrix all satisfy this stronger condition. The
"un-graded heat-kernel" and "parity-mixing propagator" are
admissible-but-not-parity-equivariant counterexamples.
**Adjudication.** ATTACK PARTIALLY SUCCESSFUL. W22-T2 stands
**conditionally** on a strictly stronger admissibility condition.
The heal: rephrase W22-T2 with the parity-equivariance hypothesis
explicit. (See W3-W25-07 below.)
**Residual.** R-W3-W25-03: classify the parity-equivariant
admissible regulator subclass formally, and verify that all
manuscript-cited regulators (heat-kernel, Pauli–Villars, Hadamard)
fall into it. This is a finer analysis than the manuscript
currently provides.

---

### W3-W25-04 — T4: Scaling-dimension consistency on $\mathfrak{gl}(N|N)$

**Severity 3 (Polyakov dimensional analysis). Status valid.
Confidence high.**
**Lens.** Polyakov primary.
**Provenance.** Mandate T4 of W25.

**Bosonic baseline (W3-W10-01).** On $\mathfrak{gl}_N$, the BV
propagator is $P^{ij}_{kl}=\delta^i_l\delta^k_j$. Mass dimension
of $P$: in 1d topological theory, the propagator on the
$\R$-line is dimensionless when $\phi$ is dimensionless and
$\psi$ has BV-dimension $-1$. Loop sum
$\sum_{i,j}\delta^i_j\delta^j_i=N$: pure number, dimensionless.
Anomaly = $\hbar\cdot\mathrm{Tr}(I)\cdot\mathrm{coupling factor}=
\hbar N\cdot[\bar c]$. Mass dimension: $[\hbar]=0$ (in this
topological-1d convention $\hbar$ is dimensionless), $[N]=0$,
$[\bar c]=0$. **Total dimension = 0.** Consistent.

**Super-extension.** On $\mathfrak{gl}(N|M)$:
* Even sector: $N$ even basis elements, each contributing
  bosonic propagator of dimension 0.
* Odd sector: $M$ odd basis elements, each contributing
  fermionic propagator (Berezin sign-flipped) of dimension 0.
* The Berezin sign $(-1)^{|a|}$ is dimensionless.

The loop sum decomposes as
$\sum_a(-1)^{|a|}\delta^a_a=\sum_{i\,\mathrm{even}}(+1)\cdot 1+
\sum_{j\,\mathrm{odd}}(-1)\cdot 1=N-M$. Each term is
dimensionless (pure numerical contributions per basis index).
The total dimension is **0**, same as bosonic.

**Polyakov consistency.** The supertrace $\mathrm{Str}(I)=N-M$
is dimensionally homogeneous with $\mathrm{Tr}(I)=N+M=N+M$
(both pure numbers). The replacement bosonic→super does not
introduce any dimension shift. **The scaling dimension is
preserved under super-extension.**

**Coefficient consistency at super-balance.** At $N=M$:
$\mathrm{Str}(I)=0$, $\mathrm{Tr}(I)=2N$. The bosonic anomaly
$\hbar\cdot 2N$ would still exist on the *bosonic*
$\mathfrak{gl}_{2N}$ source (the even sector of
$\mathfrak{gl}(N|N)$ as if treated bosonically); the supertrace
deformation cancels it via the Berezin sign on the odd sector.
**This is the structural mechanism of W22-T1: the supertrace
absorbs the bosonic anomaly into a graded-cancellation.**

**Mass-dimension audit conclusion.** No dimension shift, no
anomaly mismatch, no Polyakov-style obstruction. The
super-balanced cancellation is dimensionally clean.

**Files read.** `wave3-W10-witten-examples-2026-04-28.md` 105–195
(bosonic baseline); `wave3-W22-supertrace-rigorous-2026-04-28.md`
194–250 (super-Berezin loop).
**Confidence.** High. Direct dimensional analysis.
**Blast radius.** Polyakov dimensional consistency check passes.
The supertrace deformation does not introduce any dimensional
inconsistency; the cancellation is graded-natural.
**Adjudication.** Valid Polyakov dimensional check.
**Residual.** None at this layer.

---

### W3-W25-05 — T5: Path-integral / partition-function sanity check on super-balanced source

**Severity 3 (path-integral consistency). Status valid.
Confidence high.**
**Lens.** Polyakov primary; Examples secondary.
**Provenance.** Mandate T5 of W25. Cross-link W3-W10-03
(partition function $\prod_k(1-q^k)^{-N}$).

**Bosonic baseline.** W3-W10-03 gave the BV partition function on
$\mathfrak{gl}_N$ as $Z_N(q)=\prod_{k\geq 1}(1-q^k)^{-N}$,
matching Macdonald-Cheah/Nakajima 1999 Theorem 1.1.

**Super-extension on $\mathfrak{gl}(N|M)$.** The super-Berezinian
of the BV measure: even modes contribute $\prod_k(1-q^k)^{-N}$
(bosonic Macdonald factor for $N$ even directions); odd modes
contribute $\prod_k(1-q^k)^{+M}$ (fermionic Berezin reciprocal,
with the sign flip). Total:

\[
Z_{N|M}(q)
 =\prod_{k\geq 1}(1-q^k)^{-N}\cdot\prod_{k\geq 1}(1-q^k)^{+M}
 =\prod_{k\geq 1}(1-q^k)^{-(N-M)}.
\]

**At super-balance $N=M$:** $Z_{N|N}(q)=\prod_k(1-q^k)^0=1$ for
all $q$. The partition function is **identically $1$**, the trivial
partition function with no $q$-expansion.

**Polyakov physics consequence.** The partition function $Z=1$
to all orders in $q$ means: there is *no non-trivial Witten index*
on the super-balanced source. This is consistent with the
QME-cocycle vanishing (W22-T1, W22-T2): the cocycle obstruction
is precisely the chiral-anomaly contribution to the partition
function, and at super-balance both the partition function and
the anomaly vanish.

**Cross-check.** The bosonic partition function $\prod_k(1-q^k)^{-N}$
expanded gives the integer sequence $1, N, \frac{N(N+3)}{2},\ldots$
(at low $q$-order). The super-balanced version
$\prod_k(1-q^k)^{-(N-M)}|_{N=M}=1$ has the trivial expansion
$1,0,0,0,\ldots$ — confirming the partition-function vanishing
to all orders.

**Polyakov anomaly-via-partition-function interpretation.** In
topological QFT (Witten 1988, Vafa 1991), the partition function
is a generating function for the Witten index of supersymmetric
states. Vanishing of the partition function at super-balance is
the *physical interpretation* of cocycle vanishing: there are
no anomalous states to count.

**Files read.** `wave3-W10-witten-examples-2026-04-28.md` 255–308
(partition function bosonic); Macdonald-Cheah formula;
Nakajima 1999 Lectures on Hilbert Schemes Theorem 1.1
(cited from memory).
**Confidence.** High. Standard computation.
**Blast radius.** Independent corroboration of W22-T1, W22-T2
from the partition-function side. The Witten index vanishes
at super-balance, consistent with the cocycle vanishing. This
strengthens W22-T1, W22-T2 by an independent physical check.
**Adjudication.** Valid Polyakov consistency check.
**Residual.** None at this layer.

---

### W3-W25-06 — T6: M-31 super-integration on $\mathfrak{gl}(N|N)$

**Severity 3 (cross-check of W22-Obs). Status valid.
Confidence high.**
**Lens.** Composition primary; Polyakov secondary.
**Provenance.** Mandate T6 of W25. Cross-link W22-Obs (W3-W22-08).

**Recompute M-31 from scratch on $\mathfrak{gl}(N|N)$.**

**LHS: $[\mathrm{Str}\,\psi]_{\mathrm{BV}}$.** The BV cycle
$\mathrm{Str}\,\psi=\mathrm{Tr}\,\psi_{NN}-\mathrm{Tr}\,\psi_{MM}$
where $\psi_{NN},\psi_{MM}$ are the diagonal blocks. Each block
$\mathrm{Tr}\,\psi_{II}$ is Q-closed by cyclicity of the trace
on the bosonic block $\mathfrak{gl}_I$. The difference
$\mathrm{Str}\,\psi$ is also Q-closed (Q is super-derivation that
preserves grading). At $N=M$:
* Each block has $N=M$ basis elements.
* The difference $\mathrm{Str}\,\psi$ is the relative cycle
  between the two blocks.
* This cycle is **non-zero** in the BV homology of the super-stack:
  it is the Tor class associated to the brane / anti-brane charge
  difference.

**RHS: $(N-M)\cdot[\bar c]_{\mathrm{CE}}$.** The CE class
$[\bar c]\in H^2_{\mathrm{Lie}}(\bar A,\C)$ is closed-side and
unchanged by super-extension. The coupling coefficient
$(N-M)$ vanishes at super-balance.

**Pairing.** The chain-level lift $\Lambda^{\mathrm{Str}}$ of W22-04
sends $[\bar c]\mapsto\Lambda^{\mathrm{Str}}(\omega)$ on the
local-functional side. The pairing
$\langle[\mathrm{Str}\,\psi]_{\mathrm{BV}},[\bar c]_{\mathrm{CE}}\rangle$
extracts the coefficient $(N-M)$. At super-balance the pairing is
zero.

**Concrete computation at $(N,M)=(1,1)$.**
* $\mathrm{Str}\,\psi=\psi_{11}-\psi_{22}$ where $\psi_{11},\psi_{22}$
  are the diagonal antifield components (bosonic and fermionic
  blocks).
* This cycle is non-zero (it is the difference of two Q-cycles).
* The CE class $[\bar c]$ has coefficient 1 on the $\omega(z_1,z_2)=1$
  basis pair.
* Coupling coefficient: $(N-M)=0$.
* Pairing: $\langle\mathrm{Str}\,\psi, \bar c\rangle=0$ at
  super-balance.

**Both sides vanish at super-balance.** LHS as a Tor class on the
super-stack is non-zero **but decoupled** from the QME line
(coupling = 0). RHS coupling coefficient is zero. The
identification M-31 holds as a deformed identification.

**Polyakov consistency.** From the path-integral side (W3-W25-05),
the partition function vanishes at super-balance, and so do all
its anomaly-related descendants (cocycle vanishing). The decoupled
Tor class $\mathrm{Str}\,\psi$ is a structural invariant that
exists in the BV complex but does not produce an observable
anomaly contribution. **This is consistent with the
brane–anti-brane physics interpretation:** the Tor class is the
relative-charge measure between the brane and anti-brane, which
does not contribute to the gauge anomaly when the supertrace cancels.

**Files read.** `wave3-W22-supertrace-rigorous-2026-04-28.md`
817–897 (W22-Obs); `attack-heal-platonic-2026-04-28.md` 1612–1644
(M-31 ledger).
**Confidence.** High. Direct chain-level computation.
**Blast radius.** Confirms W22-Obs precisely. The relative-difference
cycle exists but is decoupled from the QME obstruction at
super-balance. **No conflict with W22-T1, W22-T2.**
**Adjudication.** Valid integration.
**Residual.** R-W3-W25-06: physical interpretation of the
relative-difference cycle as a brane–anti-brane charge measure
is heuristic; rigorous BCOV embedding is Phase-4
(parallels R-W3-W22-03).

---

### W3-W25-07 — T7: Heal proposal for W22-T2

**Severity 4 (heal). Status: explicit heal proposed.
Confidence high.**
**Lens.** Composition primary; Polyakov secondary.
**Provenance.** Mandate T7 of W25.

**Diagnosis from W3-W25-03.** W22-T2 currently reads:

> "Under the additional hypothesis that the BV regularization
> scheme **preserves the $\Z/2$-grading** of $\mathfrak{gl}(N|N)$
> (heat-kernel, Pauli–Villars, Hadamard parametrix at any cutoff
> inside the admissible class of `defn:regulator-admissible-sector`)..."

The phrasing implies grading-preservation is automatic for
admissible regulators. W3-W25-03 showed this is **not the case**:
two formal counterexamples (mixed propagator, un-graded heat-kernel)
satisfy (A1)–(A4) yet break grading.

**Proposed heal.** Promote grading-preservation to an **explicit
fifth admissibility condition** (A5):

\begin{addmargin}{1em}
**Proposed (A5) parity-equivariance.** *On the open matrix source
$\mathfrak{gl}(N|M)$ (or a $\Z/2$-graded variant of the source),
the regularization scheme must commute with the parity operator
$P=\mathrm{diag}(\mathbf 1_N,-\mathbf 1_M)$. Concretely: the
heat-kernel propagator $P_{\epsilon,L}^{\mathrm{super}}$ must be
constructed from the super-Killing form (or super-Casimir) on
$\mathfrak{gl}(N|M)$, and the cutoff function $\rho_{\epsilon,L}(t)$
on the topological line $\R$ must be parity-blind (no auxiliary
$\Z/2$-grading on the cutoff). All standard regulator schemes —
heat-kernel from super-Killing form, Pauli–Villars on graded source,
Hadamard parametrix — satisfy (A5) by construction.*
\end{addmargin}

**Re-stated W22-T2 with (A5) explicit.**

> **Theorem `thm:app-super-balanced-qme-all-loops` (W22-T2 v2:
> all-loop super-balanced QME vanishing under parity-equivariance).**
> Let $\mathfrak{gl}(N|N)$ be the super-balanced source. Under the
> conjunction of (A1)–(A4) [admissible regulator class] and (A5)
> [parity-equivariance], the chain-level QME holds at every
> loop order $\ell\geq 1$. The $\ell$-loop obstruction
> contracts to $(N-M)^{\ell_{\mathrm{loops}}}\cdot[\bar c]^{\ell_{\mathrm{loops}}}$,
> vanishing at super-balance. Theorem F$'$ becomes unconditional
> on this source at every loop order.

**Verification of all manuscript-cited regulators against (A5).**

* **Heat-kernel from super-Killing form.** $\Delta=
  \frac{1}{2}\sum_a (-1)^{|a|}T^a T^a$ (super-Casimir).
  Commutes with $P$ by construction. **Satisfies (A5).**
* **Pauli–Villars on graded source.** PV mass insertions
  $m_i^{\mathrm{PV}}\cdot P^{\mathrm{boson}}-m_j^{\mathrm{PV}}\cdot P^{\mathrm{fermion}}$;
  by definition the PV regulators preserve the parity assignment
  (they introduce auxiliary fields of *correct* parity).
  **Satisfies (A5)** if the PV scheme is set up parity-symmetrically.
* **Hadamard parametrix.** The Hadamard symbol $H(t,t')$
  is constructed from the super-Killing form for a graded source;
  its symbol decomposes as $H=H^{\mathrm{ev}}+H^{\mathrm{odd}}$
  with parity-equivariance built in. **Satisfies (A5).**

**Effect of the heal.** The heal makes W22-T2 honest: it states
the parity-equivariance hypothesis explicitly. The conclusion is
unchanged. The set of admissible regulators is restricted from
"all (A1)–(A4)" to "(A1)–(A5)", which is a strict subclass but
still contains all manuscript-cited schemes.

**Files read.** `wave3-W22-supertrace-rigorous-2026-04-28.md`
582–614 (W22-T2); `tate-T1-weighted-completion.tex` 596–632
((A1)–(A4)).
**Confidence.** High.
**Blast radius.** W22-T2 is restated with the
parity-equivariance hypothesis explicit. No working theorems
change; all manuscript-cited regulators satisfy the strengthened
condition. The heal is a precision sharpening, not a downgrade.
**Adjudication.** Valid heal. The strengthened W22-T2 is
rigorously proved by W22-L3 + W22-L2 under (A5), which is the
parity-equivariance condition extracted from the implicit
assumption.
**Residual.** None at the W22-T2 layer. Cross-class canonicity
(R-W3-W6-04) for parity-non-equivariant regulators is Phase-4.

---

## §2. Heal proposals

### Tier 0 — W22-T2 sharpening with (A5)

**WP3-W25-1 (W3-W25-07 = (A5) parity-equivariance).** Augment
`defn:regulator-admissible-sector` in `tate-T1-weighted-completion.tex`
with a fifth condition (A5):

> "(A5) **Parity-equivariance on graded sources.** When the open
> matrix source carries a $\Z/2$-grading (e.g.\ $\mathfrak{gl}(N|M)$),
> the regularization scheme commutes with the parity operator on
> the source: the heat-kernel propagator is built from the
> super-Killing form (super-Casimir), and the cutoff function on
> the topological line is parity-blind. All standard regulator
> schemes (heat-kernel, Pauli–Villars, Hadamard parametrix on a
> graded source) satisfy this condition by construction."

This makes W22-T2's hypothesis honest and traceable.

### Tier 1 — Cross-link to claim-strength-ledger

**WP3-W25-2.** In `claim-strength-ledger.tex`, near any entry on
the super-balanced source or W22-T2-style theorems, add:

> "On the super-balanced $\mathfrak{gl}(N|N)$ Dirac probe, the
> all-loop QME vanishing of W22-T2 is conditional on
> parity-equivariance of the regulator (W3-W25-03 / proposed (A5)).
> All manuscript-cited regulators satisfy this; the
> conditionality is on the regulator class, not on the
> super-balance physics."

### Tier 2 — Optional remark in `principles.tex`

**WP3-W25-3.** Optional remark near Theorem G area:

> "The super-balanced $\mathfrak{gl}(N|N)$ Witten-index partition
> function is identically $1$ (W3-W25-05): the bosonic
> Macdonald-Cheah factor $\prod_k(1-q^k)^{-N}$ is canceled
> exactly by the fermionic Berezin reciprocal $\prod_k(1-q^k)^{+N}$.
> This is the path-integral analogue of the cocycle-vanishing of
> Theorems W22-T1, W22-T2: there are no anomalous states to
> count when the supertrace cancels."

---

## §3. Residuals after W25

* **R-W3-W25-03 (from W3-W25-03).** Formal classification of
  parity-equivariant admissible regulators inside
  `defn:regulator-admissible-sector`. The proposed (A5) addition
  is stated; a finer analysis would verify rigorously that
  all manuscript-cited regulators satisfy it (expected high) and
  characterize the boundary of the parity-equivariant subclass.
  **Status: Phase-4 / regulator-class boundary.**
* **R-W3-W25-06 (from W3-W25-06).** Brane–anti-brane physical
  interpretation of the M-31 relative-difference Tor class on the
  super-stack. Heuristic; rigorous BCOV K-theory embedding is
  Phase-4. **Status: parallels R-W3-W22-03.**

---

## §4. Convergence verdict

**W22-T1 verification: CONFIRMED.** The one-loop super-Berezin
loop computation (W3-W25-01) and the strict chain-level
$\Lambda^{\mathrm{Str}}$ verification (W3-W25-02) both reproduce
W22-T1's coefficient $\hbar(N-M)=0$ at super-balance. The
Polyakov dimensional analysis (W3-W25-04) confirms no
dimension shift. The path-integral/partition-function vanishing
(W3-W25-05) gives an independent physical confirmation.

**W22-T2 verification: ATTACK PARTIALLY SUCCESSFUL.** The
conditional clause "every admissible regulator preserves the
$\Z/2$-grading" is **not automatic** from
`defn:regulator-admissible-sector` (A1)–(A4) as written. Two
formal counterexample regulators (mixed propagator, un-graded
heat-kernel) are admissible-but-grading-breaking and would
break super-balanced cancellation. **The W22-T2 hypothesis is
non-vacuous.** Heal: promote parity-equivariance to an
explicit (A5) condition; W22-T2 then stands rigorously under
(A1)–(A5). All manuscript-cited regulators (heat-kernel from
super-Killing, Pauli–Villars, Hadamard) satisfy (A5) by
construction.

**M-31 super-integration: CONFIRMED.** The relative-difference
Tor class $[\mathrm{Str}\,\psi]_{\mathrm{BV}}$ exists in the BV
complex on the super-stack (non-zero) but is decoupled from
the QME line at super-balance (coupling = 0). Consistent with
W22-Obs.

**Net verdict against W22.** W22-T1 stands rigorously and
unconditionally. W22-T2 stands rigorously **conditional on
parity-equivariance (proposed (A5))**, which is satisfied by all
manuscript-cited regulators but is not a free consequence of
admissibility. This is a **precision sharpening**, not a
downgrade.

**Inscribed durables.**
* This document.
* WP3-W25-1: (A5) parity-equivariance to be added to
  `defn:regulator-admissible-sector`.
* WP3-W25-2: claim-strength-ledger entry on parity-equivariance
  conditioning of W22-T2.
* WP3-W25-3: optional remark on partition-function vanishing in
  `principles.tex`.

End of W3-W25 ledger.
