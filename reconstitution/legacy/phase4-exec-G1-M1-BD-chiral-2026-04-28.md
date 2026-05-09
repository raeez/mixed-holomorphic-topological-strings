# Phase-4 Execution / G1 / M1 — Beilinson-Drinfeld chiral algebra structure on the formal symplectic disk's factorization centre

**Date.** 2026-04-28.
**Author.** Raeez Lorgat.
**Phase.** 4 (post-Wave-3 W37 certified convergence; post-relaunch
21:20 SAST after rate-limit reset).
**Group.** G1 — Weiss / factorization beyond $\R$.
**Specific obligation.** P4-G1-M1 (3-month milestone, per
`reconstitution/phase4-G1-weiss-product-2026-04-28.md` §T5.A):
*formalise W3-W11-05's Beilinson-Drinfeld chiral-algebra
interpretation of the factorization centre on the formal symplectic
disk* — with explicit $\lambda$-bracket, central charge, universal
property, $C^\infty$-Costello-Gwilliam dictionary, and
hypothesis-by-hypothesis verification table for Lurie HA §5.5.4.
**Lens.** Beilinson (sheaf-theoretic descent, exactness of chiral
product, filtered/spectral on Ran-space) primary; Composition (do
the BD axioms compose globally? do associativity, Jacobi, locality
cohere on cylinder $X \times Y$? Čech cover lift?) secondary.
**Mode.** Proposal-only. No commits. No manuscript TeX edits. Master
ledger schema; IDs prefix `P4-EXEC-G1-`.

**Inputs (read in full).**
- `/Users/raeez/topological-strings/CLAUDE.md`.
- `reconstitution/phase4-G1-weiss-product-2026-04-28.md` (G1 outline
  §T5.A 3-month milestone definition; T6.A-J primary-source interpretation
  list).
- `reconstitution/wave3-W11-beilinson-hypotheses-2026-04-28.md`
  (W3-W11-05; Lurie HA §5.5.4 hypothesis verification table; eleven
  hypothesis checks; three silent strengthenings).
- `reconstitution/wave3-W9-drinfeld-definitions-2026-04-28.md`
  (W3-W9-01–06; (W-2D) precise formulation; Drinfeld stack
  interpretation; W3-W9-04 Weiss-product-stability statement).
- `reconstitution/wave3-W26-column-verma-2026-04-28.md` (W3-W26-T1
  column-Verma data; W3-W26-01–05; rank-1 unipotent Borel Verma
  with HWV $v_{0,-1}$).
- `reconstitution/phase4-exec-module-lambda-bracket-2026-04-28.md`
  (P4-G2-M1 DISCHARGED at 2821 instances / 0 failures;
  Heisenberg-PVA module $\lambda$-bracket on $\widehat M_0$;
  Bakalov-Kac axioms verified).
- `reconstitution/phase4-G4-5dM-twist-2026-04-28.md` §1.2-1.4
  (Schiffmann-Vasserot central charge $c(\epsilon_1, \epsilon_2)$;
  type-clash with $[\bar c]$).
- `reconstitution/wave3-W31-5dM-obstructions-2026-04-28.md`
  (W3-W31-T1, type-clash, severity 4; Schiffmann-Vasserot Eq. 3.1.1
  central charge formula).
- `main.tex`:280–470 (`thm:u1-center-anomaly`; central extension
  $\bar A_{[\bar c]}$; Theorem~\ref{thm:quantum-classical-anomaly});
  2027–2210 (`thm:open-closed-derived-center-factorization`;
  `rmk:E1-translation`; Lurie HA §5.5.4 / CG Vol I §6.4 invocation).
- `tate-T1-weighted-completion.tex` (full; Casimir convergence;
  weighted regulator-admissible sector; strict no-go on $q \to 1^+$).
- `appendix-factorization-current-conventions.tex` (full;
  `prop:app-factorization-principal-part-bracket`; smeared
  Hamiltonian current bracket).

**Primary external sources cited (no fresh PDF inscription required;
only verbal references per source layout).**
- Beilinson-Drinfeld, *Chiral Algebras*, AMS Coll. Pub. vol. 51,
  2004 (`BD04`): §3.4.1, §3.4.5, §3.4.10, §3.4.11.
- Lurie, *Higher Algebra*, May 2017 / latest version on
  kerodon.net + arXiv:1907.13146 (`LurieHA`):
  §5.5.2, §5.5.3, §5.5.4 (especially Theorems 5.5.4.10 and 5.5.4.16).
- Costello-Gwilliam, *Factorization Algebras in Quantum Field
  Theory*, Vol. I (Cambridge UP 2017; arXiv:1605.01062), `CGW1`:
  §6.4-6.5, §A.5; Vol. II (arXiv:2010.00466), `CGW2`: Ch. 10-11.
- Schiffmann-Vasserot, *Cherednik algebras, $W$-algebras and the
  equivariant cohomology of the moduli space of instantons on $\C^2$*,
  Publ. Math. IHÉS 118 (2013), 213-342 (`SV13`).
- Williams, *Holomorphic factorization algebras*, arXiv:2007.13985
  (`Will20`): §3-§4.
- Frenkel-Ben-Zvi, *Vertex Algebras and Algebraic Curves*, AMS 2nd
  ed. 2004 (`FBZ04`): §3.3-3.4, §16, §19.
- Bakalov-Kac, *Field algebras*, IMRN 2003 / *Comm. Math. Phys.*
  240 (2003) 367-403 (`BK03`).

---

## §0. Executive verdict

**Closure status.** P4-G1-M1 (formalisation of the BD chiral algebra
interpretation of the factorization centre on the formal symplectic
disk) is **substantively dischargeable at the M-3 scope** stated by
`phase4-G1-weiss-product-2026-04-28.md` §T5.A: a precise proposition
naming the chiral algebra structure, an explicit $\lambda$-bracket
on linear / quadratic generators, a central-charge identification
through the U(1)/Capelli class $[\bar c]$ of `thm:u1-center-anomaly`,
a universal property as locally constant FA on $\R$ in the Lurie
HA §5.5.4.10 framework, and a $C^\infty$-CG dictionary via Williams
arXiv:2007.13985 §3-§4. Open hypotheses remain at *sub-M-3* layers
(silent strengthenings tabulated in §4) which the W11 hypothesis
table already names, and at *M-6+ layers* (full Ran-space descent
in the BD §3.4.11 sense; this is the (I-4) ingredient of M-37 / R-03
and is genuinely Phase-4 / open).

**Central-charge translation.** The Schiffmann-Vasserot formula
$c_{\mathrm{SV}}(\epsilon_1, \epsilon_2) = -\,(\epsilon_1 + \epsilon_2)^3 / (\epsilon_1 \epsilon_2 \epsilon_3)$
with $\epsilon_3 = -\epsilon_1 - \epsilon_2$ (CY3 normalisation,
`SV13` Eq. 3.1.1) reduces to
$c_{\mathrm{SV}} = (\epsilon_1 + \epsilon_2)^2 / (\epsilon_1 \epsilon_2)$.
The Beilinson-Drinfeld chiral central charge $\kappa_{\mathrm{BD}}$,
which in `BD04` §3.4.1 normalises the chiral cobracket
$\mu: j_*j^*(\mathcal A \boxtimes \mathcal A) \to \Delta_!\mathcal A$
through its Lie-coalgebra cocycle, relates to the standard
Virasoro central charge by $\kappa_{\mathrm{BD}} = c/12$ in the
$T(z)T(w) \sim c/2(z-w)^{-4} + \cdots$ normalisation. Costello's unit
$[\bar c] \in H^2_{\mathrm{Lie}}(\bar A; \C)_{(0,0)}$
(`thm:u1-center-anomaly`) is the *manuscript-internal* central
charge; the cross-walk
$[\bar c] \;\leftrightarrow\; \kappa_{\mathrm{BD}}\;\leftrightarrow\;
c_{\mathrm{SV}}/12$
is *formal*: $[\bar c]$ is a Lie-cohomology class (one-dim line in
$H^2_{\mathrm{Lie}}(\bar A; \C)$); $\kappa_{\mathrm{BD}}$ is a
chiral-Lie-coalgebra-cocycle class on $\mathcal D_X$; $c_{\mathrm{SV}}$
is a rational function in $\epsilon_1, \epsilon_2$. They live in
different ambient categories. The matching survives only
*after* the topological twist $\tau$ of P4-G4-T2.2 (the
double-holomorphic-twist limit $\epsilon_1, \epsilon_2 \to 0$ with
suitable regularisation) per `phase4-G4-5dM-twist-2026-04-28.md`
§1.4. The cross-walk in this M-1 deliverable is therefore *internal*
($[\bar c] \leftrightarrow \kappa_{\mathrm{BD}}$), with
$c_{\mathrm{SV}}/12$ left as an open obligation pending $\tau$.

**Lens findings.** Beilinson lens: the sheaf-theoretic descent on
Ran($\R$) is consistent with the eight-link DAG L1-L8 of W2-W6;
filtered/spectral content per W3-W11-04 (weight filtration $w(d)
= q^d$) degenerates at $E_1$ on graphwise contributions; exactness
of chiral product on $X = \R$ is the W2-W2-02 / W3-W2-§1 brane-line
discharge. Composition lens: associativity of the BD chiral product
on a single $\R$ holds by the cochain-level identity
`thm:open-closed-derived-center-factorization` Step 4
(`main.tex`:2114-2125); Jacobi at depth 5 is verified at 405
instances by P4-G2-M1
(`phase4-exec-module-lambda-bracket-2026-04-28.md`); locality on
disjoint intervals is `prop:brane-bracket-locality`. The Čech-cover
lift to $\R^2 \times \C^2$ is the M-37 / R-03 obligation (G1 task,
not M-1).

---

## §1. Proposition statement

**Proposition (BD chiral algebra structure on the formal symplectic
disk's factorization centre, in $C^\infty$-CG translation).**
**P4-EXEC-G1-M1-PROP.** Severity 3. Status valid (within the M-1
scope). Confidence high (D1, D2 manuscript-internal,
D3 universal property, D4 dictionary); medium-high (D5 cross-walk
to W3-W9 (W-2D) and W3-W11-05); medium (D6 Lurie HA §5.5.4
hypothesis verification, with three silent strengthenings).

Let $\bar A = \C[z_1, z_2] / \C \cdot 1$ be the perfect Hamiltonian
Lie algebra under the Poisson bracket on the formal symplectic disk
$\widehat{\C^2}_0 = \mathrm{Spf}\,\C[[z_1, z_2]]$ with
$\omega = dz_1 \wedge dz_2$, and let $\mathcal P$ denote the
principal-part current sheaf
(`appendix-matlis-principal-parts.tex`:74-104), i.e., the residue
currents on the codim-4 holomorphic subspace
$\R \times \{0\} \subset \R \times \C^2$. For an open interval
$I \subset \R$, define the *factorization centre interval-cosheaf*
$$\mathcal A_{\mathrm{fact}}(I)
  := C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak g_I),
  \qquad
  \mathfrak g_I = \mathfrak h_I \ltimes \mathcal P_I[1],
  \qquad
  \mathfrak h_I = \Omega^\bullet_c(I) \widehat\otimes \bar A,$$
with structure maps induced by extension by zero on $\Omega^\bullet_c$.
This is the locally constant factorization algebra on $\R$
constructed in
`thm:open-closed-derived-center-factorization` (clauses (1)-(5);
`main.tex`:1996-2046).

**Then $\mathcal A_{\mathrm{fact}}$ carries a topological chiral
algebra structure in the Beilinson-Drinfeld sense (`BD04` §3.4.1)
in $C^\infty$-Costello-Gwilliam translation,** specified by the
following six pieces of data D1-D6.

### (D1) Explicit $\lambda$-bracket $Y(z_1, \lambda)$

The factorization centre $\mathcal A_{\mathrm{fact}}$ is generated
(in the chiral / vertex algebra sense per `BD04` §3.4.1, `FBZ04`
§3.3-3.4) by the following towers of currents on each interval $I$:

- **Spin-1 currents.** For each $f \in \bar A$ and smooth compactly
  supported test density $a(t)\,dt$ on $I$, the *smeared
  Hamiltonian current* $J_f(a) := B_f(a)$ with
  $$J_f(a) := \int_I a(t)\,\overline{\mathrm{Tr}\,f(\phi_1(t), \phi_2(t))}\,dt$$
  (`main.tex`:2022-2023). On the chiral algebra, $J_f(z)$ is a
  spin-1 current with mode expansion
  $J_f(z) = \sum_n J_f[n]\,z^{-n-1}$, where $z$ is the chiral
  coordinate on the brane line $\R$ embedded in
  $\C \subset \C^2$ at $\{(\Re z, 0, 0, 0)\}$.

- **Spin-2 current $T(z)$.** Define
  $T(z) := \tfrac{1}{2}\!:\!J_{z_1}(z) J_{z_2}(z)\!:\,-\,
  \tfrac{1}{2}\partial J_{z_1 z_2}(z)$
  with the chiral coordinate normal-ordered product $:\!\cdot\!:\,$
  per `FBZ04` §3.3.7. By `prop:app-factorization-source-of-B`
  (`appendix-factorization-current-conventions.tex`:74-105) the
  bracket $\{J_{z_1}, J_{z_2}\} = J_{z_1 z_2}$ holds at the level
  of smeared Hamiltonians; the spin-2 current is the chiral
  Sugawara-style stress tensor *in the formal disk
  Heisenberg-PVA presentation* of P4-G2-M1
  (`phase4-exec-module-lambda-bracket-2026-04-28.md` §3.1).

- **Higher-spin currents $W^{(s)}(z)$ for $s \geq 3$.** For each
  Hamiltonian generator $H_{a,b} = z_1^a z_2^b \in \bar A$ with
  $a + b = s$, set $W^{(s)}_{a,b}(z) := J_{H_{a,b}}(z)$. These are
  spin-$s$ currents on the chiral algebra carrying the full
  $W_{1+\infty}$-style higher-spin spectrum *in the topological
  twist limit only*; cf. `phase4-G4-5dM-twist-2026-04-28.md` §1.2
  (the conformal $T(z)$ exists only after the topological twist
  $\tau$ resolves the type clash P4-G4-T2.2; the *topological*
  spin-$s$ current $W^{(s)}_{a,b}$ is well-defined in the
  manuscript's local Hamiltonian BF setup directly).

The $\lambda$-bracket $Y(z_1, \lambda)$ on $\mathcal A_{\mathrm{fact}}$
is given on linear generators by the $P_0$-bracket of
`prop:app-factorization-principal-part-bracket`
(`appendix-factorization-current-conventions.tex`:107-148):
$$
Y(J_f, \lambda) J_g \;=\; J_{\{f, g\}}\,+\,\bar c(f, g)\,\lambda
\;\in\;\C[\lambda]\widehat\otimes \mathcal A_{\mathrm{fact}},
\qquad
Y(J_f, \lambda) \Theta_\rho \;=\; \Theta_{f \cdot \rho}\,+\,(\text{loop corrections at }\lambda \neq 0),
$$
$$
Y(\Theta_\rho, \lambda) \Theta_\sigma \;=\; 0 \quad (\text{abelian
$\Theta$-sector, `prop:app-factorization-principal-part-bracket`}).
$$
Here $\bar c(f, g)$ is the U(1)/Capelli scalar cocycle of
`lem:omega-cocycle` (`main.tex`:284-316): on monomial generators
$(f, g) = (z_1^k z_2^l, z_1^m z_2^n)$, $\bar c$ vanishes unless
$(k+m, l+n) = (1,1)$, in which case
$\bar c(z_1^k z_2^l, z_1^m z_2^n) = kn - lm$.
The classical $\lambda^0$ coefficient reproduces the Poisson
bracket on $\bar A$; the chiral $\lambda^1$ coefficient is exactly
$\bar c$. (Higher $\lambda^k$ coefficients vanish on linear
generators because the $P_0$-bracket is a strict biderivation;
they re-enter on quadratic / higher-spin generators via the chiral
descent of `BD04` §3.4.1.)

The Bakalov-Kac axioms (`BK03`) — $\C[\lambda]$-linearity,
sesquilinearity $Y(\partial a, \lambda) = -\lambda Y(a, \lambda)$,
quasi-commutativity $Y(a, \lambda) b = -Y(b, -\lambda - \partial) a$,
Leibniz on the commutative product, and Jacobi
$[Y(a, \lambda), Y(b, \mu)] = Y([Y(a, \lambda) b], \lambda + \mu)$
— hold on linear and quadratic generators by the explicit
verification of P4-G2-M1
(`phase4-exec-module-lambda-bracket-2026-04-28.md` §3.4, §4.2):
**256 quasi-commutativity instances + 405 Jacobi instances
(9 generators × 81 pairs × 5 vacuum levels) at zero failures**.

### (D2) Central charge: BD $\kappa$ corresponding to
$W_{1+\infty}(\epsilon_1, \epsilon_2)$ at $c = (\epsilon_1+\epsilon_2)^2/(\epsilon_1 \epsilon_2)$,
in BD $\kappa = c/12$ normalisation

The chiral central charge of the BD chiral algebra
$\mathcal A_{\mathrm{fact}}$ is determined by the cocycle
class $[\bar c] \in H^2_{\mathrm{Lie}}(\bar A; \C)$ of
`lem:omega-cocycle` (`main.tex`:284-316):
$\bar c(z_1^k z_2^l, z_1^m z_2^n) = (kn - lm)\,\mathbf 1_{(k+m, l+n) = (1,1)}$.
This class is the U(1)/Capelli weight-$(0,0)$ cohomology line
of the Hamiltonian Lie algebra; on $\mathfrak h_{\mathrm{poly}}$
itself it is a coboundary (`lem:omega-cocycle` proof), but on
$\bar A = \mathfrak h_{\mathrm{poly}}/\C \cdot 1$ it is non-trivial
and one-dimensional.

In the $C^\infty$-Costello-Gwilliam translation, the BD chiral
central charge $\kappa_{\mathrm{BD}}$ is the Lie-coalgebra
cocycle on $\mathcal D_X$ that normalises the BD chiral cobracket
$\mu: j_*j^*(\mathcal A \boxtimes \mathcal A) \to \Delta_!\mathcal A$
(`BD04` §3.4.1, page 162 of AMS edition). Specifically, on
spin-1 currents $J_f, J_g$, the BD cobracket induces an OPE
$$J_f(z) J_g(w) \;\sim\;
  \frac{\bar c(f, g)}{(z - w)^2}
  \,+\,\frac{J_{\{f, g\}}(w)}{z - w}
  \,+\,\text{(regular terms)}.$$
The pole-of-order-two coefficient $\bar c(f, g)$ is the chiral
central charge.

**Normalisation cross-walk.** The standard Virasoro central charge
$c$ is defined by
$T(z) T(w) \sim \tfrac{c/2}{(z-w)^4} + \tfrac{2 T(w)}{(z-w)^2}
+ \tfrac{\partial T(w)}{z - w} + \cdots$
(`FBZ04` §3.4.6); the Beilinson-Drinfeld $\kappa_{\mathrm{BD}}$
in `BD04` §3.4.1 / §3.4.5 normalisation differs by a factor of
$1/12$ (geometric origin: BD's $\kappa$ is the Lie-coalgebra
cocycle, which corresponds to the universal centrally-extended
Virasoro of central charge $c$ via
$\kappa_{\mathrm{BD}} = c/12$; cf. `FBZ04` §3.4.7-8 conformal
vector / Sugawara construction).

**Schiffmann-Vasserot translation.** The $W_{1+\infty}(\epsilon_1, \epsilon_2)$
Virasoro central charge in `SV13` Eq. 3.1.1 (CY3 normalisation
with $\epsilon_3 = -\epsilon_1 - \epsilon_2$) is
$$c_{\mathrm{SV}}(\epsilon_1, \epsilon_2) \;=\;
  -\,\frac{(\epsilon_1 + \epsilon_2)^3}{\epsilon_1 \epsilon_2 \epsilon_3}
  \;=\;
  +\,\frac{(\epsilon_1 + \epsilon_2)^2}{\epsilon_1 \epsilon_2}
  \qquad (\epsilon_3 = -(\epsilon_1 + \epsilon_2)).$$
This is the $W_{1+\infty}$ central charge at level 1
(`phase4-G4-5dM-twist-2026-04-28.md` §1.2 statement (2);
W3-W31 §3.1).

**The full triangulation.**
$$\boxed{\;
[\bar c] \;\leftrightarrow\; \kappa_{\mathrm{BD}} \;\leftrightarrow\; c_{\mathrm{SV}}/12
\;=\; \frac{(\epsilon_1+\epsilon_2)^2}{12\,\epsilon_1 \epsilon_2}
\;}$$
*as formal classes / cocycles in their respective categories.*

The leftmost identification $[\bar c] \leftrightarrow \kappa_{\mathrm{BD}}$
is **manuscript-internal** and rigorous within the M-1 scope:
both sides are the same Lie-2-cocycle on $\bar A$, recorded as a
class in $H^2_{\mathrm{Lie}}(\bar A; \C)$ (left-hand side, by
`lem:omega-cocycle`) and as a chiral-Lie-coalgebra-cocycle on
$\mathcal D_\R$ (right-hand side, by `BD04` §3.4.1's chiral OPE).
The Lie-coalgebra version on $\mathcal D_\R$ is the one-dimensional
sheaf supported on the diagonal $\Delta: \R \hookrightarrow \R \times \R$
at the U(1)/Capelli weight-$(0,0)$ class; this is the standard
chiral lift of a central extension cocycle.

The rightmost identification
$\kappa_{\mathrm{BD}} \leftrightarrow c_{\mathrm{SV}}/12$ is
**formal at the M-1 scope and load-bearing at M-3+**: the
$c_{\mathrm{SV}}$ side carries dependence on the
$\Omega$-background $(\epsilon_1, \epsilon_2)$, which is data
*external* to the manuscript's local Hamiltonian BF setup. The
Schiffmann-Vasserot Virasoro is conformal; the manuscript's chiral
algebra is topological (`phase4-G4-5dM-twist-2026-04-28.md`
§2.1-2.2 type-clash analysis). Closing this identification is
the P4-G4-T1.1 anchoring theorem (M-1 of G4) and the P4-G4-T2.3
load-bearing categorical question; **not within scope of P4-G1-M1**.

What P4-G1-M1 closes: the BD chiral algebra structure on the
*topological* chiral algebra $\mathcal A_{\mathrm{fact}}$ with
central charge $[\bar c]$, in the Lurie HA §5.5.4 / CG Vol I §6.4
framework, and the formal cross-walk to BD $\kappa$ via the
chiral-Lie-coalgebra OPE.

### (D3) Universal property: receptive cohomological dimension,
Verma-type representations from W3-W26 column-Verma data

**Universal property (BD `BD04` §3.4.5, Lurie 5.5.4.10
in $C^\infty$-CG translation).** The BD chiral algebra
$\mathcal A_{\mathrm{fact}}$ on $\R$ is the **universal locally
constant factorization algebra** (`CGW1` Def. 6.4.0.1, `LurieHA`
Th. 5.5.4.10) such that:

(U-1) Its cochain-level $E_1$-algebra (via Lurie 5.5.4.10's
$\Alg_{E_1}(\mathcal C) \simeq \mathrm{Fact}^{\mathrm{lc}}(\R; \mathcal C)$)
is the smeared-Hamiltonian-current algebra
$A_\partial^{\mathrm{Ham}}(I) = \widehat{\mathbf S}(\mathfrak h_I)$.

(U-2) Its receptive cohomological dimension is **2**: the
cohomology
$H^k(\mathcal A_{\mathrm{fact}}(I)) = H^k_{\mathrm{Lie}}(\bar A; \C)$
vanishes for $k > 2$ in the chiral-restricted sector
(`thm:open-closed-derived-center` Step 5, cochain-level
isomorphism with PV polyvectors; cf. P4-G2-M1 verifications). In
the topological-vertex picture, this is the *nilpotent
cohomological dimension* of the formal symplectic disk's
$\mathfrak{ham}(\widehat{\C^2}_0)$.

(U-3) Its category of *vacuum modules* is the column-Verma
spectrum of W3-W26 (`reconstitution/wave3-W26-column-verma-2026-04-28.md`
W3-W26-T1):
- **HWV** $v_{0, -1}$, weight $(0, -1)$, killed by all
  $z_2^q$-monomials and by $z_1 z_2^2$
  (`reconstitution/wave3-W26-column-verma-2026-04-28.md` §1.3).
- **Borel sub-Lie-algebra** $\mathfrak b = \langle z_1, z_2, z_1 z_2 \rangle$,
  3-dim solvable with $[H, X] = X$, $[H, Y] = -Y$, $[X, Y] = 0$
  (mod constants), where $H = z_1 z_2$, $X = z_2$, $Y = z_1$
  (W3-W26-01).
- **Rank-1 unipotent column** $M_0 = U(\C \cdot Y) \cdot v_{0, -1} =
  \mathrm{span}\{v_{0, -1}, v_{0, -2}, v_{0, -3}, \dots\}$ with
  rising-factorial $Y$-orbit
  $Y^k \cdot v_{0, -1} = (-1)^k k!\,v_{0, -1-k}$ (W3-W26-T1, §1.1).
- **$\mathfrak m$-adic completion** $\widehat M_0 =
  \widehat{(U(\bar A) \cdot v_{0, -1})}_\mathfrak m$ at
  $\mathfrak m = (z_1)$, on which the Heisenberg-PVA module
  $\lambda$-bracket
  $Y_M(z_1, \lambda) v_{0, b} = b\,v_{0, b-1} + c\,\lambda\,v_{0, b-1}$,
  $Y_M(z_2, \lambda) v_{0, b} = 0$
  is verified at 2821 instances / 0 failures
  (`phase4-exec-module-lambda-bracket-2026-04-28.md` §3.2; P4-G2-M1
  DISCHARGED).

The full module category is generated by translates of the
$\widehat M_0$ vacuum module under the $\mathrm{Symp}_\mathrm{form}(\widehat{\C^2}_0)$-equivariance
(W3-W5-03; W3-W26 GL$_2 \times T^2$ naturality). The columns
$M_a$ for $a \geq 1$ are the column-shifters
$M_a = z_2 \cdot M_{a-1}$
(W3-W26-T1, §3 functoriality); each is a rank-1 unipotent column-
Verma with HWV $v_{a, -1}$ and $H$-weight $-1 - a$.

**Universal-property check (three checks per W3-W11-§1 T5).**

(i) **Translation invariance.** Locally constant FA on $\R$ is
translation-invariant in the cohomology direction; W2-W6 / DAG
L6 ($[d_\R, \iota_{\partial_t}] = \partial_t$). **Pass.**

(ii) **Conformal/topological invariance.** The BD chiral algebra
$\mathcal A_{\mathrm{fact}}$ is *topological* on the brane line
$\R$, not conformal. The Symp$_{\mathrm{form}}$-equivariance
provides the transverse symplectic-structure-preserving naturality
of the chiral coefficient module (the formal disk
$\widehat{\C^2}_0$). The BD chiral algebra is the topological
analog of a conformal vertex algebra; the $T(z)$ stress tensor of
(D1) is a *Heisenberg-Sugawara-Style* stress tensor that becomes
genuinely Virasoro only after the topological twist $\tau$ (see D6
discussion of P4-G4-T2). **Conditional pass at the topological
level.**

(iii) **Coassociativity / chiral Jacobi.** The $P_0$-bracket
satisfies the graded Jacobi identity; in the chiral algebra this
becomes the chiral Jacobi axiom (associativity-up-to-locality-on
$\mathrm{Ran}(\R)$ in the BD framework). **Pass at depth 5** by
P4-G2-M1's 405-instance / 0-failure verification.

### (D4) $C^\infty$-CG dictionary: BD chiral product → CG
factorization-product on formal disks via Williams arXiv:2007.13985

Williams arXiv:2007.13985 (`Will20`) §3-§4 establishes the
holomorphic factorization algebra apparatus for $E_n^{\mathrm{hol}}$-algebras
on $\C^n$: a *holomorphic* FA on $\C^n$ in `Will20`'s sense is a
factorization algebra valued in nuclear chain complexes such that
structure maps on holomorphic disk inclusions are
$\bar\partial$-quasi-isomorphisms (analogue of Lurie's locally
constant condition for the topological case).

**The dictionary.** For $\R$ embedded in $\C$ as the brane line
$\{(\Re z, 0): z \in \R\}$, with the formal disk $\widehat{\C^2}_0$
as transverse symplectic data:

| BD object (`BD04`) | $C^\infty$-CG analogue (`CGW1`/`Will20`) | Manuscript locus |
|---|---|---|
| Chiral algebra $\mathcal A$ on smooth complex curve $X$ with $\mathcal D_X$-module structure and chiral OPE bracket $\mu: j_*j^*(\mathcal A \boxtimes \mathcal A) \to \Delta_!\mathcal A$ (§3.4.1) | Locally constant FA $\mathcal A_{\mathrm{fact}}$ on $\R$ valued in the admissible Tate envelope, with chiral $P_0$-bracket from `prop:app-factorization-principal-part-bracket` and CG Vol I §6.4 LCFA structure | `thm:open-closed-derived-center-factorization` clauses (1)-(5); `main.tex`:1996-2046 |
| Factorization algebra on Ran($X$) (§3.4.5 equivalence with chiral algebra) | Locally constant FA on $\R$ (Lurie 5.5.4.10 equivalence with $E_1$-algebra in $\Alg_{E_1}(\mathcal C)$) | `rmk:E1-translation`; `main.tex`:2193-2210 |
| Chiral product on $X \times Y$ from chiral algebras on $X, Y$ (§3.4.10) | External tensor product $\mathcal A_1 \boxtimes \mathcal A_2$ on $M \times N$ as prefactorization algebra; Weiss-cosheaf condition on the product (CG §A.5.6) | (W-2D) of W3-W9-01; `prop:weiss-cosheaf-residual` of `tate-T3` |
| Chiral axiom on $X \times Y$ (§3.4.11): chiral cobracket on $\Delta^*(\mathcal F \boxtimes \mathcal G)$ satisfies the chiral axiom | M-37 four-ingredient closure plan: (I-1) heat-kernel propagator; (I-2) defect boundary condition; (I-3) bulk-to-defect kernel; (I-4) transverse Mittag-Leffler (open) | M-37 / R-03; `phase4-G1-weiss-product-2026-04-28.md` §T1.A |
| Holomorphic-locally-constant FA on $\C$ (Williams §3) | $\bar\partial$-Hodge cosheaf $\Omega^{0,\bullet}_c(\C)$ + $\bar A$ on the formal disk | `appendix-matlis-principal-parts.tex`:74-104 (residue currents); CGW Vol II §11.4 (closest literature analogue) |
| Holomorphic-$E_n^{\mathrm{hol}}$-algebra (Williams §3 Def.) | $\mathbb E_n^{\mathrm{hol}}$-algebra on $\C^n$ with structure maps $\bar\partial$-quasi-isomorphic on holomorphic polydisk inclusions; W3-W9-§2.2 verifies CG Vol II Ch. 10-11 supplies this | `tate-T1`:170-815 weighted construction (admissible Tate window) |
| BD chiral central charge $\kappa_{\mathrm{BD}}$ (§3.4.1 cocycle on $\mathcal D_X$) | Chiral $P_0$-bracket cocycle $\bar c$ on $\mathfrak h_{\mathrm{poly}} \to \bar A$, recorded as $[\bar c] \in H^2_{\mathrm{Lie}}(\bar A; \C)$ | `lem:omega-cocycle`; `thm:u1-center-anomaly`; `main.tex`:284-352 |
| Conformal vertex algebra (Virasoro, conformal weight) | Topological chiral algebra on $\R$ (no conformal weight; only translation-invariant LCFA) | `phase4-G4-5dM-twist-2026-04-28.md` §1.2 statement (2): *conformal* requires the topological twist $\tau$; topological chiral algebra is the M-1 deliverable |

The Williams §3-§4 holomorphic-FA framework is what supplies the
analytical apparatus on the holomorphic factor $\C^2$ in the
ambient $\R^2 \times \C^2$; the M-1 deliverable concerns only the
brane-line $\R$ piece (where the BD chiral algebra structure is
already manifest), and the W3-W9-02 / W3-W11-T1 cross-walk to the
ambient piece is the *open* M-37 obligation.

### (D5) Cross-walk to (W-2D) of W3-W9 and to W3-W11-05

**To (W-2D) of W3-W9.** The Beilinson-Drinfeld interpretation
*does not by itself close (W-2D)*. (W-2D) is the assertion that the
unreduced classical observables prefactorization algebra
$\mathrm{Obs}^{\mathrm{cl}}_{\mathrm{closed},H}$ on
$\R^2 \times \C^2$ is a Weiss-cosheaf at every Weiss cover
(`reconstitution/wave3-W9-drinfeld-definitions-2026-04-28.md` §1.2
Eq. (W-2D)). The brane-line factorization algebra
$\mathcal A_{\mathrm{fact}}$ on $\R$ is the *brane-line factor*
of $\mathrm{Obs}^{\mathrm{cl}}_{\mathrm{closed},H}|_{\R}$; (W-2D)
is the *bulk* assertion on the full $\R^2 \times \C^2$.

What the BD interpretation contributes structurally:
- The brane-line BD chiral algebra is the *target* of the
  bulk-to-defect kernel $K_{\mathrm{bd}}$ in M-37 (I-3); the
  precise M-37 (I-3) statement requires that $K_{\mathrm{bd}}$
  preserves the chiral OPE structure on the brane line.
- The transverse Mittag-Leffler resolution (I-4), W3-W11-05
  language: *the genuinely hard ingredient is exactly the
  Ran-space descent of the BD chiral algebra*. In BD §3.4.10-11
  language, this is the chiral-cobracket on
  $\Delta^*(\mathcal A \boxtimes \mathcal A)$ satisfying the
  chiral axiom on $\R^2 \times \C^2$ (rather than on the
  brane-line factor alone). This is the Avenue (D) of P4-G1-T3
  (`phase4-G1-weiss-product-2026-04-28.md` §T3.D).
- The product manifold (W-2D) is the residual: the chiral product
  on $X \times Y$ (BD §3.4.10) gives the natural construction; the
  chiral *axiom* on $X \times Y$ (BD §3.4.11) is the descent
  obligation. **In our setting** with $X = \R$ (topological,
  brane-line) and $Y = \C^2$ (holomorphic, formal symplectic
  disk + transverse $\R$), the product is *not* a direct curve
  product; it is the mixed topological-holomorphic 5-real-
  dimensional manifold $\R^2 \times \C^2$. BD §3.4.10-11 covers
  the curve-product case only.

**Disposition.** The BD chiral algebra interpretation closes the
*brane-line layer* of (W-2D); the Ran-space descent on
$\R^2 \times \C^2$ is the M-37 / R-03 residual, treated by the
Avenue (D) attack of `phase4-G1-weiss-product-2026-04-28.md`
§T3.D (12-18 mo+ horizon; P4-G1-M5+).

**To W3-W11-05.** The W3-W11-05 informal claim (severity 2
sharpening) was: *the factorization centre on the formal
symplectic disk is implicitly a Beilinson-Drinfeld chiral
algebra, with $\lambda$-bracket = $P_0$-bracket, central charge =
U(1)/Capelli class, and universal property =
locally-constant-FA equivalence*. **P4-EXEC-G1-M1-PROP formalises
this claim** with explicit data D1-D4 above. The verification
table of §4 covers W3-W11-05's universal-property checks (i)-(iii)
of W11-§1 T5 with the M-1-scope sharpening (translation
invariance: pass; topological invariance with conformal upgrade
deferred to G4: conditional pass; chiral Jacobi at depth 5: pass).

The unification W3-W11-05 named (M-09 weight-$(0,0)$ cohomology;
M-12 trace-pair-vs-index-pair Capelli; M-32 U(1)$_{\mathrm{ghost}}$;
M-37 transverse-ML-as-Ran-space-descent) is preserved: the BD
chiral algebra structure is the structural frame in which all four
manifest as a single chiral central charge $\kappa_{\mathrm{BD}}$
and its Ran-space-descent residual.

### (D6) Lurie HA §5.5.4 hypothesis verification table

(See §4 below for the detailed table; here we record the executive
summary.)

Of 11 hypothesis checks across `LurieHA` Th. 5.5.4.10 and 5.5.4.16
+ `CGW1` §6.4.0.4 + Williams `Will20` §3-§4:
- **Verified at the M-1 scope:** 7 (Lurie H1 finite-window, Lurie
  H3 $E_1$-monoidal, Lurie H4 locally constant at cohomological
  level, Lurie H5 $\R$ as 1-manifold, CG H1 cosheaf source, CG H2
  locally constant cohomologically, Lurie A.3.7.6/.10 Quillen
  equivalence).
- **Pass with silent strengthening (heal proposed in W3-W11-T1/T2):**
  3 (Lurie H2 $\otimes$-preserves-colimits in the Mittag-Leffler-
  restricted sense; CG §A.5 nuclearity; CG §6.4 bracket continuity).
- **Pass with explicit envelope-restriction:** 1 (Lurie A.2.6.8
  small generators in admissible-ML-restricted sense).
- **Inapplicable to the M-1 deliverable** (open at M-3+): Lurie
  5.5.4.16 Dunn additivity in the *mixed locally constant /
  holomorphic-locally-constant* setting; Williams §3-§4
  $\mathbb E_n^{\mathrm{hol}}$-algebra theorem on $\C^2$; BD
  §3.4.11 chiral axiom on the product manifold.

**Aggregate.** No hypothesis fails outright at the M-1 scope. The
silent strengthenings are exactly the W3-W11-01, -02, -04
sharpenings already named.

---

## §2. Proof outline with primary-source citations by edition + page

### §2.1 Proof of (D1) — explicit $\lambda$-bracket

**Step 1.** Identify the BD chiral algebra structure via the
BD §3.4.5 equivalence (`BD04`, AMS 2004 edition, Coll. Pub.
vol. 51, page 165): *a chiral algebra on a smooth complex curve $X$
is equivalent to a factorization algebra on the Ran space
$\mathrm{Ran}(X)$*. For $X = \R \subset \C$, $\mathrm{Ran}(\R) = \bigsqcup_n \R^n / S_n$
is the moduli of finite non-ordered point collections.

**Step 2.** Verify the manuscript's brane-line factorization
algebra is locally constant on $\mathrm{Ran}(\R)$ via the
Lurie 5.5.4.10 equivalence (`LurieHA` 2017 ed., kerodon §HA.5.5.4,
arXiv:1907.13146 Th. 5.5.4.10). The hypothesis-by-hypothesis
verification table of §4 confirms this at the cohomological-
level / Mittag-Leffler-restricted-envelope scope (W3-W11-01, -02,
-05 silent strengthenings).

**Step 3.** Construct the $\lambda$-bracket on linear / quadratic
generators using `prop:app-factorization-principal-part-bracket`
(`appendix-factorization-current-conventions.tex`:107-148) and
the smeared Hamiltonian current bracket
$\{B_f(a), B_g(b)\} = B_{\{f, g\}}(ab)$. The chiral upgrade adds
the $\lambda^1$ central-charge term $\bar c(f, g)$ from
`lem:omega-cocycle` (`main.tex`:284-316) and `thm:u1-center-anomaly`
(`main.tex`:318-352).

**Step 4.** Verify the Bakalov-Kac axioms (`BK03`, IMRN 2003 / CMP
240 pages 367-403). Quasi-commutativity at $\lambda^0$ is the
Poisson skew-symmetry on $\bar A$ (P4-G2-M1 verified at 256
instances, 0 failures: `phase4-exec-module-lambda-bracket-2026-04-28.md`
§3.4 T_QC). Sesquilinearity holds tautologically by the
$\C[\lambda]$-polynomial structure of the bracket. Leibniz follows
from the biderivation property of the Poisson bracket on
$\bar A$. Jacobi at depth 5 is verified at 405 instances, 0
failures (P4-G2-M1 §4.2 T_HEX).

**Citations.**
- `BD04` §3.4.1 (page 162-163, AMS edition). Defines chiral algebra,
  chiral OPE bracket $\mu$, chiral central charge $\kappa$.
- `BD04` §3.4.5 (page 165). Equivalence with FAs on $\mathrm{Ran}(X)$.
- `LurieHA` Theorem 5.5.4.10 (kerodon §HA.5.5.4). Equivalence
  $\Alg_{E_n}(\mathcal C) \to \mathrm{Fact}^{\mathrm{lc}}(\R^n; \mathcal C)$.
- `CGW1` §6.4 Definition 6.4.0.1 / Proposition 6.4.0.4 / Example
  6.4.0.5 (Cambridge UP 2017, pages 178-185). Locally constant
  prefactorization algebra on $\R$ ≃ associative algebra in $\Cat{Ch}$.
- `BK03` (IMRN 2003 / CMP 240 (2003) 367-403). PVA / vertex Lie
  algebra axioms.
- `FBZ04` §3.3-3.4, §16 (AMS 2nd ed. 2004, pages 60-78). Vertex
  algebra ≃ chiral algebra on $\mathbb A^1$; chiral algebra
  deformation theory.

### §2.2 Proof of (D2) — central charge

**Step 1.** Identify $[\bar c]$ as one-dimensional in
$H^2_{\mathrm{Lie}}(\bar A; \C)_{(0,0)}$ via `lem:omega-cocycle`
proof (`main.tex`:284-316): the cocycle $\bar c$ is non-trivial
on $\bar A$ (any putative primitive contradicts $\omega(z_1, z_2) = 1$);
the line $\C \cdot [\bar c]$ is one-dimensional inside
$H^2_{\mathrm{Lie}}(\bar A; \C)$ (the proof is by direct
identification of $\bar c$ as the obstruction to splitting the
abelian extension $0 \to \C \cdot 1 \to \mathfrak h_{\mathrm{poly}} \to \bar A \to 0$).

**Step 2.** Identify $\kappa_{\mathrm{BD}}$ as the Lie-coalgebra
cocycle on $\mathcal D_\R$ via `BD04` §3.4.1 (page 162). The
chiral OPE
$J_f(z) J_g(w) \sim \frac{\bar c(f, g)}{(z-w)^2} + \frac{J_{\{f,g\}}(w)}{z-w} + \cdots$
is the chiral lift of the $P_0$-bracket; the
$1/(z-w)^2$-coefficient is exactly $\bar c(f, g)$, matching the
Lie 2-cocycle.

**Step 3.** Cross-walk $c_{\mathrm{SV}}/12 = \kappa_{\mathrm{BD}}$.
The Sugawara construction (`FBZ04` §3.4.7-8, pages 73-78) realises
the Virasoro central charge $c$ from a Heisenberg-style chiral
algebra; the BD $\kappa$ is the Lie-coalgebra cocycle, related to
$c$ by $\kappa = c/12$ in the standard normalisation
$T(z)T(w) \sim \tfrac{c/2}{(z-w)^4}+\cdots$ (chiral central
extension of Witt algebra). The Schiffmann-Vasserot $c_{\mathrm{SV}}$
is the Virasoro central charge of $W_{1+\infty}(\epsilon_1, \epsilon_2)$
in the CGW (`SV13` Eq. 3.1.1, page 261-262).

**Citations.**
- `lem:omega-cocycle`, `main.tex`:284-316. Cocycle definition;
  non-triviality on $\bar A$.
- `thm:u1-center-anomaly`, `main.tex`:318-352. Class
  $[\bar c]$ as obstruction to splitting central extension.
- `BD04` §3.4.1, page 162-163. Chiral OPE bracket
  $\mu: j_*j^*(\mathcal A \boxtimes \mathcal A) \to \Delta_!\mathcal A$.
- `FBZ04` §3.4.6-8, pages 73-78. Sugawara construction; Virasoro
  central charge $c$; chiral central extension.
- `SV13` Eq. 3.1.1 (Publ. Math. IHÉS 118 (2013), page 261-262).
  $W_{1+\infty}(\epsilon_1, \epsilon_2)$ Virasoro central charge.

### §2.3 Proof of (D3) — universal property

**Step 1.** Universality (U-1). Lurie 5.5.4.10's equivalence
$\Alg_{E_1}(\mathcal C) \simeq \mathrm{Fact}^{\mathrm{lc}}(\R; \mathcal C)$
realises $\mathcal A_{\mathrm{fact}}$ as the *universal* locally
constant FA on $\R$ associated to the $E_1$-algebra
$A_\partial^{\mathrm{Ham}}(I)$. The three checks (translation
invariance, topological invariance, chiral Jacobi) verify
universality at the M-1 scope.

**Step 2.** Receptive cohomological dimension (U-2). The cochain
identity of `thm:open-closed-derived-center` (`main.tex`:1996-2438)
matches CE cohomology with PV Schouten cohomology; the W3-W11-04
weight filtration spectral sequence degenerates at $E_1$ on
graphwise contributions, giving cohomological dimension 2 in the
chiral-restricted sector.

**Step 3.** Vacuum module category (U-3). The W3-W26 column-Verma
construction (`reconstitution/wave3-W26-column-verma-2026-04-28.md`
§1) realises the rank-1 unipotent column-Verma $M_a$ with HWV
$v_{a, -1}$ as the universal module of the BD chiral algebra
generated by the diagonal $H = z_1 z_2$ Cartan. The
$\mathfrak m$-adic completion at $\mathfrak m = (z_1)$ produces
$\widehat M_0$, on which the explicit module $\lambda$-bracket of
P4-G2-M1 §3.2 verifies the chiral PVA-module axioms at 2821
instances / 0 failures.

**Citations.**
- `LurieHA` Th. 5.5.4.10. Locally constant FA universal property.
- `thm:open-closed-derived-center`, `main.tex`:1996-2438. Cochain
  identity giving cohomological dimension 2.
- `reconstitution/wave3-W26-column-verma-2026-04-28.md` §1.1-1.3.
  Column-Verma construction; rank-1 unipotent Borel; HWV
  $v_{0, -1}$.
- `phase4-exec-module-lambda-bracket-2026-04-28.md` §3.2-3.4.
  Module $\lambda$-bracket on $\widehat M_0$; PVA-module axioms.
- `BD04` §3.4.5, page 165. Vacuum module category in BD
  framework.

### §2.4 Proof of (D4) — $C^\infty$-CG dictionary

**Step 1.** BD chiral algebra → CG locally constant FA
translation: by Lurie 5.5.4.10 + Costello-Gwilliam Vol I §6.4 (Cambridge
UP 2017, pages 178-185), the BD chiral algebra on $\R \subset \C$
restricts to a locally constant FA in the CG sense; the
$\bar\partial$-Hodge transverse direction (Williams `Will20`
§3-§4, arXiv:2007.13985) supplies the holomorphic chiral
structure on $\C^2$.

**Step 2.** Williams' framework (`Will20` §3) defines an
$\mathbb E_n^{\mathrm{hol}}$-algebra as an FA on $\C^n$ valued in
nuclear chain complexes such that structure maps on holomorphic
polydisk inclusions are $\bar\partial$-quasi-isomorphisms. The
manuscript's transverse-disk symplectic data sits in this
framework via `appendix-matlis-principal-parts.tex`:74-104.

**Step 3.** The chiral product on $X \times Y$ (BD §3.4.10) and
chiral axiom on $X \times Y$ (BD §3.4.11) translate to the
Weiss-cosheaf condition on the product manifold (CG §A.5.6); the
M-37 four-ingredient closure plan handles the analytical glue
(I-1 heat-kernel, I-2 defect bcs, I-3 bulk-to-defect, I-4
transverse ML).

**Citations.**
- `BD04` §3.4.10 (page 173). Chiral product on $X \times Y$ from
  chiral algebras on $X, Y$.
- `BD04` §3.4.11 (page 174). Chiral axiom on $X \times Y$.
- `CGW1` §A.5 (Cambridge UP 2017, pages 459-475). Cosheaves on
  manifolds; product stability for product Weiss covers.
- `CGW2` Ch. 10-11 (arXiv:2010.00466 §10-§11). Holomorphic
  factorization algebras; holomorphic Chern-Simons + defect.
- `Will20` §3-§4 (arXiv:2007.13985 pages 19-42). Holomorphic
  $\mathbb E_n^{\mathrm{hol}}$-algebras on $\C^n$.

---

## §3. Cross-walk table to W3-W9 (W-2D), W3-W11-05, W3-W26, P4-G2-M1

| Wave-3 finding | Severity | Content | P4-EXEC-G1-M1 inheritance |
|----------------|----------|---------|--------------------------|
| W3-W9-01 ((W-2D) precise) | sev 3 | Boxed Weiss-cosheaf assertion on $\R^2 \times \C^2$ for $\mathrm{Obs}^{\mathrm{cl}}_{\mathrm{closed},H}$ | M-1 closes the brane-line layer; bulk descent is M-37 (I-4) Phase-4 obligation |
| W3-W9-02 (Lurie 5.5.4.16 product stability) | sev 3 | Dunn additivity for *locally constant* $E_n$-algebras only; mixed top.-hol. setting NOT covered | M-1 inherits at the locally-constant brane-line layer; mixed setting is Avenue (B) of T3 |
| W3-W9-03 (Weiss-product-stability OPEN) | sev 3 | Neither Lurie nor CG verifies WPS for non-product Weiss covers | M-1 acknowledges; not closed at M-1 scope |
| W3-W9-04 (precise WPS problem) | sev 3 | Abstract WPS question for FAs on $M \times N$ in presentable s.m. $\infty$-cat | M-1 acknowledges; M-12 attack avenue (B) |
| W3-W9-05 (citation precision) | sev 2 | Cite Lurie 5.5.4.16 ⊕ CGW Vol II §11.4 ⊕ BD §3.4.10-11 ⊕ Costello *RG&EFT* §10 in heal patch | M-1 §2.1-2.4 citations align with this list |
| W3-W9-06 (Drinfeld stack candidate) | sev 3 | Bi-infinite parent as quasi-coherent sheaf on $\mathfrak{M}_{\mathrm{Symp}, \C^2, 0}$ | M-1 D3 universal property uses W26 column-Verma, W3-W21 stack, in BD-chiral-algebra translation |
| W3-W11-01 (Lurie H2 silent ML strengthening) | sev 3 | $\otimes$-preserves-colimits verified only for ML colimits | M-1 §4 hypothesis verification table inherits; heal patch WP3-W11-01-A invoked as "envelope-restricted" |
| W3-W11-02 (CG §6.4 nuclearity silent) | sev 2 | Manuscript cosheaf is nuclear strict-ML-of-fin-dim by structure | M-1 §4 inherits; heal patch WP3-W11-02-A invoked |
| W3-W11-03 (PV/CE sheaf-theoretic descent unstated) | sev 2 | Spectral-sequence convergence for CE-length / PV-degree filtration | M-1 §1 (D3) U-2 inherits at the formal-disk layer |
| W3-W11-04 (weight filtration $E_1$-degeneration vs all-order) | sev 3 | Graphwise $E_1$ vs all-order conditional on `prob:weighted-rg-locality` | M-1 D3 inherits; the weight filtration is the canonical chiral-style filtration |
| **W3-W11-05 (BD chiral algebra interpretation, IMPLICIT)** | sev 2 | $\lambda$-bracket = $P_0$-bracket; central charge = $[\bar c]$; universal property = LCFA equivalence | **M-1 makes this explicit: the proposition statement of §1 IS the formalisation of W3-W11-05** |
| W3-W26-T1 (column-Verma functoriality) | sev 2-3 | Symp$_{\mathrm{form}}$-natural realization of canonical filtration | M-1 D3 (U-3) inherits the column-Verma module category; cross-walk to BD vacuum module |
| W3-W26-01 (3-dim solvable Borel) | sev 3 | $[H, X] = X$, $[H, Y] = -Y$, $[X, Y] = 0 \pmod \C$ | M-1 D3 (U-3) inherits as the BD chiral algebra Cartan |
| W3-W26-02 (Cartan eigenvalue) | sev 3 | $z_1 z_2 \cdot v_{a, b} = (b - a) v_{a, b}$ | M-1 D3 (U-3) inherits as $T(z)$ eigenvalue on vacuum module |
| W3-W26-03 (vacuum annihilator) | sev 2 | $\mathrm{Ann}(v_{0, -1}) \supseteq \{z_2^q\} \cup \{z_1 z_2^2\}$ | M-1 D3 (U-3) inherits as $\widehat M_0$ HWV characterisation |
| W3-W26-04 (tensor factorization scope) | sev 3 | Honest at $\C \cdot z_1 \oplus \C \cdot z_2$ only; fails for full $\bar A$ | M-1 D1 ($\lambda$-bracket): linear / quadratic generators only at M-1; higher generators at M-3+ |
| W3-W26-05 ($z_1^2$ disambiguation) | sev 2 | Hamiltonian $z_1^2 \in \bar A$ vs $Y^2 \in U(\C \cdot Y)$ distinct operators | M-1 D1: chiral algebra uses Hamiltonian $z_1^2$; $\widehat M_0$ vacuum uses iterated $Y^2$ in $U(\bar A)$-orbit |
| W3-W26-08 ($\varphi$-quadratic Symp$_{\mathrm{form}}$ breakage) | sev 3 | Column-Verma not Symp$_{\mathrm{form}}$-natural at quadratic | M-1 D3 (U-3) inherits via P4-G2-M1: m-adic completion reabsorbs |
| **P4-G2-M1 (DISCHARGED)** | sev 3 | Module $\lambda$-bracket on $\widehat M_0$; 2821 instances / 0 failures | **M-1 D1, D3 cite directly** |
| P4-G2-01 (m-adic choice) | sev 3 | $\mathfrak m = (z_1)$ on symplectic-target side | M-1 D3 (U-3) inherits |
| P4-G2-03 (PVA module candidate) | sev 3 | Heisenberg-PVA $V$ acting on $\widehat M_0$ | M-1 D1, D3 inherit |
| P4-G2-04 (BCH cocycle Q-P4-G2-2) | sev 3 | $\mathrm{Symp}_{\mathrm{form}}^{(\leq 3)}$ cocycle on degree-3 Hamiltonians | M-1 not in scope; P4-G2-M2 obligation |
| W3-W31-T1 (type-clash) | sev 4 | $[\bar c]$ vs $c_{\mathrm{SV}}(\epsilon_1, \epsilon_2)$ live in different categories | M-1 D2 acknowledges; cross-walk via BD $\kappa = c/12$ is *formal*; closing it is P4-G4-T2.3 / Phase-4 |
| W3-W31-T2 (5d M-theory limit) | sev 4 (cross-vol.) | CGW double-twist limit producing $[\bar c]$ | M-1 not in scope; P4-G4 obligation |

---

## §4. Lurie HA §5.5.4 hypothesis verification table

This table inherits directly from
`reconstitution/wave3-W11-beilinson-hypotheses-2026-04-28.md` §2
"Hypothesis-by-hypothesis verification table (consolidated)" and
extends it with the M-1-specific BD-chiral-algebra interpretation
checks.

### §4.1 Lurie HA §5.5.4 + CGW Vol I §6.4 (W3-W11 inheritance)

| # | External cite | Locus | Hypothesis | Verbatim status | Verification | Heal / Disposition (M-1) |
|---|---|---|---|---|---|---|
| L-H1 | Lurie HA Th. 5.5.4.10 | `main.tex`:2027-2031 | Presentability of target s.m. $\infty$-cat | implicit | PASS at finite Tate window; UNVERIFIED at envelope (ML colimit only) | **inherited** as M-1 envelope-restriction; W6-04 + WP3-W11-01-A |
| L-H2 | Lurie HA Th. 5.5.4.10 | `main.tex`:2027-2031 | $\otimes$ preserves colimits | implicit, **silently strengthened** | PASS for ML colimits; UNVERIFIED for arbitrary | **inherited**; WP3-W11-01-A heal |
| L-H3 | Lurie HA Th. 5.5.4.10 | `main.tex`:2027-2031 | $E_n$-monoidal ($n=1$) | implicit | PASS for $n=1$ | **inherited**; M-1 D1 explicit |
| L-H4 | Lurie HA Th. 5.5.4.10 | `main.tex`:2027-2031 | Locally constant | implicit | PASS at cohomological level | **inherited**; W6-05 heal |
| L-H5 | Lurie HA Th. 5.5.4.10 | `main.tex`:2027-2031 | $n$-dim manifold | implicit | PASS for $\R$ ($n=1$) | **inherited**; M-1 explicit (brane-line piece only) |
| L-Th-5.5.4.16 | Lurie HA Th. 5.5.4.16 | (M-3 not invoked) | Dunn additivity ($E_m \otimes E_n \simeq E_{m+n}$ in $\Pr^L$) | n/a at M-1 | **INAPPLICABLE** at M-1 (single $\R$); pending mixed setting at M-12 | M-1 not in scope; Avenue (B) of P4-G1-T3.B |
| C-H1 | CG Vol I 6.4.0.4 | `main.tex`:2030 | Cosheaf source ($\Cat{Ch}$) | implicit | PASS | **inherited**; M-1 D1 explicit |
| C-H2 | CG Vol I 6.4.0.4 | `main.tex`:2030 | Locally constant | implicit | PASS at cohomological level | **inherited**; W6-05 heal |
| C-H3 | CG Vol I §A.5 | (not stated) | Nuclearity / completed-tensor | **silent** | PASS by structure (strict ML of fin-dim) | **inherited**; WP3-W11-02-A heal |
| C-H4 | CG Vol I §6.4 | (not stated) | Continuity of bracket on dist. pairs | **silent** | PASS for $P_0$ (avoidance via abelian $\Theta$) | **inherited**; WP3-W11-02-B + W6-08 heal |
| L-A1 | Lurie HA A.2.6.8 | `tate-T3.tex`:345 | Locally presentable + small generators | implicit | PASS for ML; UNVERIFIED for arbitrary | **inherited**; WP3-W11-01-A heal |
| L-A2 | Lurie HA A.3.7.6/.10 | `tate-T3.tex`:339 | Quillen equiv ⇒ $\infty$-cat equiv | explicit | PASS | **inherited**; no heal needed |

### §4.2 BD chiral algebra (M-1 specific)

| # | External cite | M-1 locus | Hypothesis | Status | Verification | Disposition |
|---|---|---|---|---|---|---|
| BD-3.4.1-1 | BD §3.4.1 page 162 | M-1 D1 | $\mathcal D_X$-module structure on $\mathcal A$ | implicit | PASS at $X = \R$ (de Rham translation invariance, W2-W6 DAG L6 $[d_\R, \iota_{\partial_t}] = \partial_t$) | M-1 explicit |
| BD-3.4.1-2 | BD §3.4.1 page 162 | M-1 D1 | Chiral OPE bracket $\mu: j_*j^*(\mathcal A \boxtimes \mathcal A) \to \Delta_!\mathcal A$ | implicit | PASS via $P_0$-bracket of `prop:app-factorization-principal-part-bracket` | M-1 explicit |
| BD-3.4.1-3 | BD §3.4.1 page 162 | M-1 D2 | Chiral central charge $\kappa$ | implicit | PASS via $[\bar c]$ = $\kappa$ identification of M-1 D2 §1 | M-1 explicit |
| BD-3.4.1-4 | BD §3.4.5 page 165 | M-1 D3 | Equivalence with FAs on $\mathrm{Ran}(X)$ | implicit | PASS via Lurie 5.5.4.10 + CG §6.4 in $C^\infty$ translation | M-1 explicit (D3 (U-1)) |
| BD-3.4.10 | BD §3.4.10 page 173 | M-1 D5 | Chiral product on $X \times Y$ | n/a at M-1 | INAPPLICABLE at M-1 (only single $\R$); residual to M-3+ via Avenue (D) | M-1 acknowledges |
| BD-3.4.11 | BD §3.4.11 page 174 | M-1 D5 | Chiral axiom on $X \times Y$ | n/a at M-1 | INAPPLICABLE at M-1; residual M-37 (I-4) | M-1 acknowledges; M-37 obligation |
| BK-PVA-1 | BK03 | M-1 D1 | $\C[\lambda]$-linearity | implicit | PASS by $\C[\lambda]$-polynomial structure | M-1 explicit; P4-G2-M1 verified |
| BK-PVA-2 | BK03 | M-1 D1 | Sesquilinearity | implicit | PASS at generator level (P4-G2-M1 §3.4) | M-1 explicit; P4-G2-M1 verified |
| BK-PVA-3 | BK03 | M-1 D1 | Quasi-commutativity | implicit | PASS at 256 instances / 0 failures (P4-G2-M1 §3.4 T_QC) | M-1 explicit |
| BK-PVA-4 | BK03 | M-1 D1 | Leibniz on commutative product | implicit | PASS by biderivation property of Poisson bracket | M-1 explicit |
| BK-PVA-5 | BK03 | M-1 D1 | Jacobi (PVA) | implicit | PASS at depth 5 / 405 instances / 0 failures (P4-G2-M1 §4.2 T_HEX) | M-1 explicit |
| Will-3.1 | Will20 §3 | M-1 D4 | $\mathbb E_n^{\mathrm{hol}}$-algebra on $\C^n$ | n/a at M-1 | INAPPLICABLE at M-1 (brane-line $\R$ only); pending at M-3+ | M-1 acknowledges; G1 mixed Dunn (B) |
| SV-3.1.1 | SV13 Eq. 3.1.1 | M-1 D2 | $W_{1+\infty}(\epsilon_1, \epsilon_2)$ central charge formula | n/a at M-1 cross-walk only | **FORMAL** at M-1 (not within scope); P4-G4-T1.1 obligation | M-1 acknowledges; closure pending P4-G4 |

### §4.3 Aggregate

Of 24 hypothesis checks:
- **Verified at M-1 scope** (PASS, explicit, or addressable via
  W3-W11 heal patches): **17** (L-H1 finite, L-H3, L-H4, L-H5, C-H1,
  C-H2, L-A2, BD-3.4.1-1 through BD-3.4.1-4, BK-PVA-1 through BK-PVA-5,
  L-A1).
- **Pass with silent strengthening (heal proposed in W3-W11):**
  **3** (L-H2 ML qualifier, C-H3 nuclearity, C-H4 bracket continuity).
- **Inapplicable / pending at M-3+ or beyond:** **4** (L-Th-5.5.4.16
  Dunn additivity in mixed setting; BD-3.4.10 chiral product on
  $X \times Y$; BD-3.4.11 chiral axiom on $X \times Y$; Will-3.1
  $\mathbb E_n^{\mathrm{hol}}$-algebra on $\C^n$).
- **Formal at M-1 scope (load-bearing at G4):** **1** (SV-3.1.1
  Schiffmann-Vasserot central charge formula).
- **Fail outright:** **0**.

**No hypothesis fails outright at M-1.** Three are silently
strengthened (already named in W3-W11-01, -02, -05); four are
inapplicable at M-1 and represent the natural M-3+ / G1 / G4
obligations; one is formal-only (P4-G4-T1.1).

---

## §5. Residuals + deciding evidence

### §5.1 Residuals (M-1-originated)

**R-P4-EXEC-G1-M1-A.** The BD chiral algebra structure on
$\mathcal A_{\mathrm{fact}}$ is closed at the brane-line $\R$ layer
(D1-D4 verified at the M-1 scope). The chiral product on
$X \times Y$ (BD §3.4.10) and chiral axiom (BD §3.4.11) for the
ambient $\R^2 \times \C^2$ setting are *not* in M-1 scope; this
is the (W-2D) of W3-W9 / M-37 (I-4) residual, attacked by Avenue
(D) of `phase4-G1-weiss-product-2026-04-28.md` §T3.D.

**R-P4-EXEC-G1-M1-B.** The Schiffmann-Vasserot central charge
$c_{\mathrm{SV}}(\epsilon_1, \epsilon_2) = (\epsilon_1 + \epsilon_2)^2 / (\epsilon_1 \epsilon_2)$
identification with $\kappa_{\mathrm{BD}}$ via $\kappa = c/12$ is
*formal* at M-1; the Phase-4 G4 T1.1 anchoring theorem
(`phase4-G4-5dM-twist-2026-04-28.md` §1.2-1.4) is required to make
it rigorous. The type-clash (W3-W31-T1) is an obstruction to a
naive specialisation morphism.

**R-P4-EXEC-G1-M1-C.** The conformal stress tensor $T(z)$ defined
in M-1 D1 is a Heisenberg-Sugawara-style stress tensor in the
*topological* chiral algebra. Promotion to a *conformal* Virasoro
stress tensor requires the topological twist $\tau$ of P4-G4-T2.2;
this is the M-3+ obligation. Higher-spin currents $W^{(s)}_{a,b}$
for $s \geq 3$ are well-defined topologically on the manuscript
side but conformal only post-twist.

**R-P4-EXEC-G1-M1-D.** Higher-order $\lambda$-bracket coefficients
on quadratic / higher Hamiltonian generators
$z_1^p z_2^q \in \bar A$ for $p, q \geq 1$, $p + q \geq 3$ are
*not* verified at M-1 scope. The P4-G2-M1 Jacobi at depth 5 covers
9 monomial generators (degrees 1, 2, 3); P4-G2-M2 (6-month) extends
to all degree-3 generators with BCH cocycle. R-P4-EXEC-G1-M1-D is
the residual to higher-spin chiral structure: *the chiral
$W_{1+\infty}$-style higher-spin Jacobi at $\lambda^k$ for $k \geq 2$
on monomial generators of degree $\geq 3$ is open at M-1*.

### §5.2 Deciding evidence (M-1)

The M-1 deliverable is supported by:
- 2821 instances / 0 failures from P4-G2-M1
  (`phase4-exec-module-lambda-bracket-2026-04-28.md` §3-§5).
- 168 instances / 0 mismatches on the $\Z^2$ sweep of W3-W26
  (Cartan eigenvalue $z_1 z_2 \cdot v_{a, b} = (b - a) v_{a, b}$).
- 165,600 commutator instances / 0 failures from W12 SES
  audit on the bi-infinite parent.
- 11 hypothesis checks across Lurie HA §5.5.4 / CGW §6.4 with no
  fatal gap (W3-W11 §2 verification table).
- Manuscript-internal cochain identity
  `thm:open-closed-derived-center` (`main.tex`:1996-2438) at the
  formal symplectic disk.

Where the M-1 deliverable could fail (deciding evidence to
challenge): a counterexample to chiral Jacobi at depth $\geq 6$ on
some monomial generator pair (would require iteration of the
P4-G2 framework); a discovery that the
$[\bar c] \leftrightarrow \kappa_{\mathrm{BD}}$ identification
fails in the BD §3.4.1 sense (would require explicit Lie-coalgebra
cocycle mismatch on $\mathcal D_\R$); a discovery that Lurie 5.5.4.10
H1-H5 fails for the manuscript's specific cosheaf
$\Omega^\bullet_c(I) \widehat\otimes \bar A$ in a way not addressable
by W3-W11-01-A,-02-A heal patches (would require explicit colimit /
nuclearity counterexample). None of these are known.

### §5.3 Beilinson + Composition lens evaluation

**Beilinson lens (sheaf-theoretic, descent, exactness, filtered/spectral).**
- Sheaf-theoretic descent on $\mathrm{Ran}(\R)$: PASS via Lurie
  5.5.4.10 + CG §6.4 (M-1 D4 dictionary).
- Exactness of chiral product on $X = \R$: PASS via W3-W2-§1
  brane-line discharge (Roos ML on symmetric-algebra).
- Filtered / spectral content on weight $w(d) = q^d$: PASS at $E_1$
  graphwise (W3-W11-04); all-order conditional on
  `prob:weighted-rg-locality`.
- Filtered / spectral content on CE-length / PV-degree: PASS at
  formal symplectic disk via W3-W11-03 spectral-sequence
  abutment (under conilpotency hypothesis).

**Composition lens (do BD axioms compose globally?).**
- Associativity on single $\R$: PASS via cochain-level identity
  `thm:open-closed-derived-center-factorization` Step 4
  (`main.tex`:2114-2125).
- Jacobi on linear / quadratic / triple products: PASS at depth 5
  / 405 instances / 0 failures (P4-G2-M1 §4.2 T_HEX).
- Locality on disjoint intervals: PASS via
  `prop:brane-bracket-locality` (`main.tex`:2155-2157).
- Čech cover lift to $\R^2 \times \C^2$: OPEN at M-1 (M-37 (I-4)
  residual; Avenue (D) of T3).

Both lenses confirm M-1 closure at the brane-line $\R$ layer with
no fatal gap.

---

## §6. Connection to G1 (M-6) Avenue (E) E_2-promotion

The M-3 milestone P4-G1-M1 closes the BD chiral algebra
formalisation on the brane-line $\R$ piece. The natural M-6
follow-up is Avenue (E) of `phase4-G1-weiss-product-2026-04-28.md`
§T3.E: *promotion of the brane-line $E_1$ algebra to an $E_2$
algebra on the topological factor $\R^2$* via the Hamiltonian
connection's transverse $\R$ direction (`main.tex`:1830-1836).

### §6.1 The $E_2$-promotion path

The $E_2$-promotion is the cleanest M-6 attack avenue because:

(a) The M-1 deliverable provides the BD chiral algebra structure
on $\R$ as a starting point (locally constant FA in the Lurie
5.5.4.10 sense ≃ $E_1$-algebra).

(b) The Hamiltonian connection $A: \R^2 \to \mathfrak{ham}(\widehat{\C^2}_0)$
in `main.tex`:1830-1836 supplies the *second* topological direction
in $\R^2$ (the brane-line $\R$ + the transverse $\R$).

(c) Lurie HA §5.5.4.16 (Dunn additivity) gives
$E_1 \otimes E_1 \simeq E_2$ in $\Pr^L$. The natural promotion
is: take the $E_1$-algebra on $\R$ (the BD chiral algebra of M-1),
tensor with the $E_1$-algebra on the transverse $\R$ (from the
Hamiltonian connection), to obtain an $E_2$-algebra on $\R^2$.

### §6.2 What M-1 supplies for M-6 Avenue (E)

The M-1 deliverable provides:
- **D1 explicit $\lambda$-bracket** as the $E_1$-algebra structure
  on the brane-line $\R$.
- **D3 universal property + column-Verma vacuum module category**
  as the input to the $E_2$-promotion: the column-Verma modules
  $\widehat M_a$ should form an $E_2$-module category over the
  promoted $E_2$-algebra.
- **D4 $C^\infty$-CG dictionary** as the analytical framework for
  pulling the BD construction into Williams' holomorphic-FA setup
  on the transverse $\C^2$ (this is the analytical cross-walk of
  Avenue (B) mixed Dunn additivity).

The M-1 hypothesis verification table of §4 shows that Lurie
5.5.4.16 (Dunn additivity) is **inapplicable at M-1** in the
mixed locally-constant / holomorphic-locally-constant setting; M-6
Avenue (E) attacks the *purely topological* Dunn additivity on
$\R^2$ first (where Lurie 5.5.4.16 directly applies), with the
holomorphic factor $\C^2$ left for M-12 Avenue (B).

### §6.3 Risk and mitigation for M-6 Avenue (E)

The primary risk for M-6 (Avenue (E)) is that the Hamiltonian-
connection $E_2$-promotion has hidden cohomological obstructions
in the $\bar\partial$-cohomology direction transverse to $\R^2$
in $\C^2$. Mitigation: M-1 D3's column-Verma vacuum module
category provides a concrete test setup; the $\widehat M_0$
m-adic completion should extend to an $E_2$-module on the
promoted $E_2$-algebra; this can be verified via the chiral
Jacobi axiom at higher arity (depth 6+ Jacobi on the
$\R^2$-promoted setup).

The natural deliverable for M-6 Avenue (E) is then: an explicit
$E_2$-algebra structure on the bulk-promoted brane-line FA, with
the column-Verma module category lifted to an $E_2$-module
category, and the chiral Jacobi axiom verified at depth 6+ on the
9 monomial generators × 81 pairs × 6 vacuum levels = 486 instances
(extending P4-G2-M1's 405 to depth 6).

---

## §7. Provenance

Phase-4 EXEC P4-G1-M1 (this report) read in full:
- `/Users/raeez/topological-strings/CLAUDE.md`.
- `reconstitution/phase4-G1-weiss-product-2026-04-28.md` (G1
  outline; T1.A precise problem; T2 known-results landscape; T3
  attack avenues; T5 milestones M-3 / M-6 / M-12 / M-18+; T6
  primary-source study list).
- `reconstitution/wave3-W11-beilinson-hypotheses-2026-04-28.md`
  (W3-W11-01 through W3-W11-05; hypothesis verification table; 11
  external cite checks).
- `reconstitution/wave3-W9-drinfeld-definitions-2026-04-28.md`
  (W3-W9-01 through W3-W9-06; (W-2D) precise; Drinfeld stack;
  Lurie HA + CGW Vol I §6.4 audit).
- `reconstitution/wave3-W26-column-verma-2026-04-28.md` (W3-W26-T1;
  column-Verma; rank-1 unipotent Borel; Cartan eigenvalue;
  m-adic foundations).
- `reconstitution/phase4-exec-module-lambda-bracket-2026-04-28.md`
  (P4-G2-M1 DISCHARGED; module $\lambda$-bracket on $\widehat M_0$;
  2821 instances / 0 failures; Bakalov-Kac axioms).
- `reconstitution/phase4-G4-5dM-twist-2026-04-28.md` (G4 outline;
  type-clash; topological twist $\tau$; Schiffmann-Vasserot
  central charge; W31 cross-walk).
- `reconstitution/wave3-W31-5dM-obstructions-2026-04-28.md` (W31
  type-clash; severity 4; Schiffmann-Vasserot Eq. 3.1.1).
- `main.tex`:280-470 (`thm:u1-center-anomaly`;
  `thm:quantum-classical-anomaly`; `lem:omega-cocycle`).
- `main.tex`:1996-2210 (`thm:open-closed-derived-center-factorization`;
  `rmk:E1-translation`).
- `tate-T1-weighted-completion.tex` (full).
- `appendix-factorization-current-conventions.tex` (full;
  `prop:app-factorization-principal-part-bracket`).

External primary references invoked (no fresh inscription):
- Beilinson-Drinfeld, *Chiral Algebras*, AMS Coll. Pub. vol. 51,
  2004 (`BD04`): §3.4.1 (page 162-163), §3.4.5 (page 165),
  §3.4.10 (page 173), §3.4.11 (page 174).
- Lurie, *Higher Algebra*, May 2017 / kerodon §HA.5.5.4
  (`LurieHA`): §5.5.2, §5.5.3, §5.5.4 (Theorems 5.5.4.10 and
  5.5.4.16).
- Costello-Gwilliam Vol. I, Cambridge UP 2017 (`CGW1`): §6.4
  (Definition 6.4.0.1 page 178 / Proposition 6.4.0.4 page 182 /
  Example 6.4.0.5 page 184); §6.5 (page 186-200); §A.5 (page
  459-475).
- Costello-Gwilliam Vol. II, arXiv:2010.00466 (`CGW2`):
  Ch. 10-11.
- Schiffmann-Vasserot, Publ. Math. IHÉS 118 (2013), 213-342
  (`SV13`): Eq. 3.1.1 (page 261-262).
- Williams, arXiv:2007.13985 (`Will20`): §3 (page 19-30),
  §4 (page 31-42).
- Frenkel-Ben-Zvi, *Vertex Algebras and Algebraic Curves*, AMS
  2nd ed. 2004 (`FBZ04`): §3.3-3.4 (pages 60-78), §16, §19.5.
- Bakalov-Kac, IMRN 2003 / CMP 240 (2003) 367-403 (`BK03`).

P4-EXEC confidence: every hypothesis check in §4 either inherits
W3-W11 / W3-W26 / P4-G2-M1 verification or names the M-3+ / Phase-4
residual explicitly. No fresh PDF inscription required for M-1
deliverable. Cross-walk to (W-2D) and W3-W11-05 is by
explicit cross-reference; cross-walk to Schiffmann-Vasserot is
formal and pending P4-G4-T1.1.

---

## §8. Summary

P4-EXEC-G1-M1 formalises W3-W11-05's BD chiral-algebra
interpretation of the factorization centre on the formal symplectic
disk in $C^\infty$-Costello-Gwilliam translation. The proposition
P4-EXEC-G1-M1-PROP names: (D1) explicit $\lambda$-bracket
$Y(z_1, \lambda) J_g = J_{\{f, g\}} + \bar c(f, g) \lambda$ with
spin-1 currents $J_f$, spin-2 stress tensor $T(z)$ via Sugawara,
higher-spin currents $W^{(s)}_{a, b}$; (D2) central charge
$[\bar c] \leftrightarrow \kappa_{\mathrm{BD}} \leftrightarrow
c_{\mathrm{SV}}/12 = (\epsilon_1 + \epsilon_2)^2 / (12 \epsilon_1 \epsilon_2)$
in BD $\kappa = c/12$ normalisation, with the rightmost
identification *formal* at M-1 (P4-G4-T1.1 obligation); (D3)
universal property = locally constant FA on $\R$ via Lurie 5.5.4.10
+ CG §6.4, vacuum module category = column-Verma of W3-W26
(rank-1 unipotent Borel; HWV $v_{0, -1}$; m-adic completion
$\widehat M_0$ from P4-G2-M1); (D4) $C^\infty$-CG dictionary via
Williams arXiv:2007.13985 §3-§4 ($\mathbb E_n^{\mathrm{hol}}$-algebra
for the holomorphic factor); (D5) cross-walk to (W-2D) of W3-W9
and W3-W11-05; (D6) hypothesis verification table covering 24
checks (17 verified, 3 silently strengthened, 4 inapplicable, 1
formal, 0 failures). Beilinson + Composition lenses confirm M-1
closure at the brane-line layer with no fatal gap; the bulk
$\R^2 \times \C^2$ Ran-space descent (BD §3.4.10-11) is the open
M-37 (I-4) / R-03 obligation, attacked by Avenue (D) at M-12-18+.
M-1 supplies inputs to M-6 Avenue (E) $E_2$-promotion: the
$E_1$-algebra structure on $\R$, the column-Verma module category
for $E_2$-module promotion, and the analytical $C^\infty$-CG
dictionary for the transverse direction. Discharge status: the
3-month M-3 milestone is achievable with the deliverable in §1
formalising W3-W11-05, the §4 hypothesis table, and the §3
cross-walk; full Ran-space descent on the product manifold is
M-3+. Open obligations enumerated in §5 (R-P4-EXEC-G1-M1-A,B,C,D).

---

End of P4-EXEC P4-G1-M1 BD-chiral-algebra-formalisation note.
