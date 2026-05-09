# Phase 4 Execution / P4-A2primeT-Manuscript-Audit — Silent (A2$''_T$) Sugawara-descendant polynomial-degree usage audit

**Author.** Raeez Lorgat.
**Date.** 2026-04-28.
**Mode.** Proposal-only. No git commits, no edits to manuscript TeX.
**Lens.** Costello hypothesis discipline + Hypothesis-Master-Block inheritance graph.
**Scope.** Exhaustive scan of `main.tex`, `theorem-lanes.tex`,
`claim-strength-ledger.tex`, `appendix-unreduced-bv-qme.tex`,
`tate-T1-weighted-completion.tex` through `tate-T5-chain-level-primitive.tex`,
plus auxiliary `principles.tex`, `open-obligations.tex`,
`appendix-radial-parts-moyal.tex`, `appendix-matlis-principal-parts.tex`,
`appendix-factorization-current-conventions.tex`, `local-dictionary.tex`,
`abstract.tex`, `nomenclature.tex`, `notation.tex`.
**Trusted context.**
- `phase4-exec-G4-T22-virasoro-twist-2026-04-28.md` (1409 lines)
  introduces $(A2''_T)$ as the silent twisted-side strengthening of
  $(A2)$ on the conformal Virasoro side: extends the polynomial-degree
  class to include Virasoro descendants $L_{-n_1}\cdots L_{-n_k}$
  expressible polynomially in the Heisenberg modes via Sugawara
  $L_n=(1/(2k))\sum_m {:}J_{n-m}J_m{:}$.
- `phase4-exec-A1-hypothesis-audit-2026-04-28.md` and
  `phase4-exec-Hypothesis-Master-Block-2026-04-28.md` document the
  inscription draft and dependency table.

---

## §0 Executive verdict

**Total silent $(A2''_T)$ usages found in the manuscript: ZERO.**

The audit returns a **null result** for the conformal Virasoro side: no
manuscript inscription invokes the Sugawara construction, the Virasoro
current $T(z)$, Virasoro descendants $L_{-n}$, normal-ordered conformal
products $:JJ:$, or any conformal-VOA structure that would require
$(A2''_T)$ as a load-bearing hypothesis. The manuscript is consistently
the **topological / chain-level side** of the conformal-promotion
square specified in the G4-T2.2 dictionary.

Criticality: **NONE**. No silent strengthening to repair on the
manuscript side. The G4-T2.2 conformal Virasoro promotion lives
entirely in the Phase-4 EXEC reconstitution corpus and has not been
inscribed into the manuscript yet, so its hypothesis $(A2''_T)$ has no
candidate dependent inscription to audit.

**Inscription readiness shifts orientation accordingly.** The
recommended action is *not* "inscribe $(A2''_T)$ to repair existing
silent usage" (no such usage exists) but rather: **prepare $(A2''_T)$
as a future-conditional hypothesis declaration ready for the moment
the conformal Virasoro promotion functor $\tau_T$ is introduced into
the manuscript proper**.

The single mildly relevant subtlety is the manuscript's use of the
phrase "conformal-symplectic $\mathfrak{sl}_2$" in `tate-T2`
(§1, item AT.5 below), which is a terminological collision but **not**
a Sugawara-descendant invocation: it denotes the
$\mathfrak{sp}(2,\C)\cong\mathfrak{sl}_2$ subalgebra of quadratic
Hamiltonians on $\C^2$, an external $\mathfrak{sl}_2$ acting on the
Heisenberg target, not the Virasoro $\{L_{-1},L_0,L_1\}$ subalgebra.
This collision is documented in §2.6 below as a clarifying terminology
remark candidate — not a silent strengthening.

---

## §1 Manuscript scan results

### §1.1 Direct keyword sweep

**Sugawara.** Zero occurrences across all `.tex` files in the
manuscript root (excluding the `frontier_mnop_framing_volume.tex`
companion, which is not `\input`-ed by `main.tex` and is outside the
audit scope).

**Virasoro.** One occurrence: `frontier_mnop_framing_volume.tex:510`
"elliptic-curve uniqueness/Virasoro results in their stated scope" — a
biographical mention of Costello–Li 2012 in a companion file not
included in the manuscript build. Zero occurrences in `main.tex` and
all included files.

**stress tensor / stress-energy / $T(z)$ / $L_n$.** Zero occurrences.

**Spin-2 / spin tower / primary fields.** Zero occurrences in any
Virasoro-module sense.

**Conformal vector / conformal weight / central charge.** Zero
occurrences (one bibliography reference: Witten "Notes on conformal
field theory", `main.tex:6186`, which is an unused/stale citation
template — not invoked in any theorem statement).

**Free boson / free-field / background charge / Felder twist.** Zero
occurrences in any operative role. The string "Felder" appears only
as a bibliography author in `cattaneo-felder-bv` (Cattaneo–Felder
BV-quantization paper, not the Felder background-charge construction).

**VOA / vertex operator algebra / chiral algebra.** Zero occurrences as
operative invocation. "Chiral Algebras" appears as the title of the
Beilinson–Drinfeld bibliography entry at `main.tex:6246`; the entry is
not invoked as a load-bearing reference inside any theorem.

**$W_{1+\infty}(\epsilon_1,\epsilon_2)$ / $W$-algebras / Schiffmann–Vasserot
$c=(\epsilon_1+\epsilon_2)^2/(\epsilon_1\epsilon_2)$.** Zero occurrences.

**Normal-ordered products $:JJ:$, $:J^n:$.** Zero occurrences in any
CFT/Sugawara sense. The string "normal-ordered" does appear, but
exclusively in the **matrix Weyl algebra** sense (Capelli /
Razmyslov–Procesi normal ordering of $\mathrm{Tr}(\phi_1^a\phi_2^b)$
in $\mathcal W_N$), not the Sugawara $:J(z)J(w):$ sense. Verified at
`main.tex:418, 444, 4665, 4762-4818, 4839, 4857, 4876, 4906`. See
§2.7 below.

**$\tau_T$ functor.** Zero occurrences. The conformal-promotion functor
documented in `phase4-exec-G4-T22-virasoro-twist-2026-04-28.md` is
**not** present as a manuscript-level construction; it lives entirely
in the reconstitution corpus pending future inscription.

### §1.2 Hypothesis (A2) anchor scan

The manuscript's inscribed (A2) lives in
`tate-T1-weighted-completion.tex:606-613` inside
`defn:regulator-admissible-sector` (clause (A2)):

> "At each fixed $\hbar$-order and for each fixed Costello graph, the
> coefficient expression uses only vertexwise polynomial-degree-bounded
> Hamiltonian and cotangent legs."

The `\bar A`-direction "polynomial-degree" here is *exclusively* the
polynomial degree in the Heisenberg-Hamiltonian generators $z_1, z_2$
(monomials $z_1^a z_2^b$, equivalently the $\bar A = \C[z_1,z_2]/\C\cdot 1$
basis). It is **not** a polynomial-degree statement in $J$-modes of a
free-boson Heisenberg current algebra, and **not** a Sugawara-descendant
class. Therefore the inscribed (A2) is the **topological/chain-level
$(A2)$**, not the Virasoro-twisted $(A2''_T)$.

### §1.3 Polynomial-degree dependent inscriptions

Tracing all sites where the polynomial-degree class is invoked:

| Site | File:line | Polynomial-degree class | Source flavour |
|------|-----------|------------------------|----------------|
| (A2) inscription | `tate-T1-weighted-completion.tex:611-613` | Heisenberg $z_1^a z_2^b$ Hamiltonian + cotangent legs | topological / chain-level |
| `thm:wt-rg-compatibility` (uses (A2)) | `tate-T1:451-454` | "vertexwise polynomial-degree-bounded interactions" | topological |
| `thm:wt-cotangent-lift` (downstream) | `tate-T1:466-491` | weighted Tate cochain map on $\bar A$ | topological |
| `thm:app-unreduced-polynomial-centrality-no-go` | `appendix-unreduced-bv-qme.tex:33-53` | "$Q$-stable subcomplex of the unreduced polynomial open BV observables in which every element has finite polynomial degree in $\phi_1,\phi_2,\psi$" | matrix-Weyl / open-side polynomial |
| `prob:tate-coefficient-descendant-lift` | `main.tex:5518` | polynomial one-$\psi$ descendants $\widetilde\Psi_{a,b}$ | matrix-Weyl PBW shadow |

**None of these polynomial-degree invocations refers to Virasoro
descendants.** The Heisenberg here is the **target-space** Heisenberg
Lie algebra of $(\phi_1,\phi_2)$ at the brane (matrix Weyl / formal
symplectic disk), not a worldsheet Heisenberg current algebra
$\widehat{\mathfrak{gl}}_1$ acting at level $k$. The Sugawara
construction $L_n = (1/(2k))\sum_m {:}J_{n-m}J_m{:}$ requires the
worldsheet flavour; the manuscript never enters that flavour.

### §1.4 Schiffmann–Vasserot / $W_{1+\infty}$ central-charge sweep

Att-4 of the attack-angle list asks: does the
Schiffmann–Vasserot formula $c = (\epsilon_1+\epsilon_2)^2/(\epsilon_1\epsilon_2)$
appear in `main.tex` anywhere in a load-bearing way? **Verified absent.**
The G4-T2.2 reconstitution document derives this $c$ via a cross-check
with the Sugawara central charge of a single boson in a rebased
Heisenberg level $k = -(\epsilon_1+\epsilon_2)/(\epsilon_1\epsilon_2)$, but
neither the formula nor any equivalent appears anywhere in the
manuscript. The G1-M1 closure documented in
`phase4-exec-G1-M1-BD-chiral-2026-04-28.md` lives in the Phase-4 EXEC
corpus, not in the inscribed manuscript.

### §1.5 Conformal-VOA Costello sub-framework sweep

Att-3 asks: does any inscription cite a Bousfield localisation,
$E_2$-promotion of a conformal VOA, or a Costello chain-level CFT
regulator, that could implicitly require $(A2''_T)$? **Verified absent.**
The manuscript's Costello regulator class is the topological/holomorphic
mixed-kinematic Costello regulator (Costello 2011 Ch. 4-5;
Costello–Gwilliam Vol. II §11) on $\R^2 \times \C^2$ with brane
$\R \times p$. There is no conformal VOA / Costello §5.2 chiral-CFT
regulator invocation. `stmt:costello-bv-package` (`main.tex:5136-5152`)
is the universal RG-flow effective interaction with heat kernel and
counterterms — purely topological/holomorphic, no conformal twist.

---

## §2 Per-candidate analysis

The task identified six candidate inscriptions for targeted
examination. Each is dispatched verbatim below.

### §2.1 `lem:omega-cocycle` (`main.tex:284-316`)

**Claim verbatim.**

> "$\omega$ is a Lie 2-cocycle on $\mathfrak h_{\mathrm{poly}}$. On
> $\mathfrak h_{\mathrm{poly}}$ itself it is a coboundary; on the
> scalar-reduced quotient $\bar A=\mathfrak h_{\mathrm{poly}}/\C\cdot 1$
> the same formula represents a nontrivial class
> $[\bar c]\in H^2_{\mathrm{Lie}}(\bar A,\C)$."

**Hypothesis dependence.** Depends on (A2) **alone** (admissible
inscribed) — and only weakly, via the *finite-degree* monomial
spanning of $\mathfrak h_{\mathrm{poly}} = \C[z_1,z_2]$. The cocycle
calculation is the Jacobi identity for the Poisson bracket on
polynomials, evaluated at the constant Taylor coefficient. No
Virasoro structure is invoked. The bracket
$\{f,g\}=\partial_{z_1}f \,\partial_{z_2}g - \partial_{z_2}f \,\partial_{z_1}g$
is the standard polynomial Poisson bracket, not a $\lambda$-bracket on
a chiral algebra.

**Cross-reference chain.** The proof references only Jacobi on
polynomials, antisymmetry of the bracket, the constant Taylor
coefficient $[\,\cdot\,]_0$, and the abelian extension
$0 \to \C \to \mathfrak h_{\mathrm{poly}} \to \bar A \to 0$. None of
these dependencies routes through a Sugawara construction.

**Verdict.** **No silent (A2$''_T$) usage.**

### §2.2 `thm:u1-center-anomaly` (`main.tex:318-352`)

**Claim verbatim.**

> "The class $[\bar c]\in H^2_{\mathrm{Lie}}(\bar A,\C)$ of
> Lemma~\ref{lem:omega-cocycle} is the scalar-axis obstruction class to
> lifting the Lie algebra structure on $\bar A$ to the Lie algebra
> structure on the unreduced polynomial Hamiltonians
> $\mathfrak h_{\mathrm{poly}}$ along the abelian extension … The class
> $[\bar c]$ spans the one-dimensional sub-line of
> $H^2_{\mathrm{Lie}}(\bar A,\C)$ attached to this constant-Hamiltonian
> extension."

**Hypothesis dependence.** Depends on (A2) **alone** in its
finite-polynomial flavour. The closure invokes:
- Chevalley–Eilenberg classification of central extensions of $\bar A$
  by $\C$;
- the Poisson bracket on monomials $\{z_1^k z_2^l, z_1^m z_2^n\}
  = (kn-lm) z_1^{k+m-1} z_2^{l+n-1}$;
- projection to the constant Taylor coefficient.

**No Sugawara descendant is invoked.** The "spin tower" the theorem
implicitly works with is the *bidegree* tower
$\{H_{a,b} = z_1^a z_2^b\}$ — a polynomial spanning of the formal
symplectic Hamiltonian Lie algebra, **not** a $\mathbb Z_{\geq 0}$-graded
conformal-weight tower of Virasoro descendants $L_{-n_1}\cdots L_{-n_k}$.

**Cross-reference chain.** The proof references only `lem:omega-cocycle`
and the Chevalley–Eilenberg framework. No path to a Virasoro current
or to a $T(z)$ stress tensor.

**Verdict.** **No silent (A2$''_T$) usage.**

### §2.3 `thm:open-closed-derived-center` (`main.tex:2322-2349`)

**Claim verbatim.**

> "Let $\mathfrak h$ be any pro-finite-dimensional Lie algebra in
> $\Cat{TateVec}$ over $\C$, concentrated in degree zero, satisfying
> the Tate-conilpotency hypothesis of `lem:continuous-bar-cobar`. Let
> $\mathfrak g=\mathfrak h\ltimes\mathfrak h^\vee_{\mathrm{cont}}[1]$
> be the shifted-cotangent extension. Let
> $A_\partial=\widehat{\mathbf S}_{\mathrm{Tate}}(\mathfrak h)$ be the
> Tate-completed Kirillov–Poisson algebra of
> `lem:linear-poisson-schouten`. Then there is a canonical isomorphism
> of completed dg graded-commutative $P_0$-algebras
> $\Phi: C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak g)
> \xrightarrow{\sim} \mathrm{PV}(A_\partial)$, determined on generators
> by $\Phi(c^I)=\theta^I$, $\Phi(u_I)=O_I$ … the cochain-level
> open-closed derived center isomorphism in the formal/local sector."

**Hypothesis dependence.** Tate-conilpotency hypothesis (formalised in
`lem:continuous-bar-cobar`) and (A1)+(A4) (truncation discipline +
admissible filtered cohomology). The proof reduces to a generator-level
verification of the CE differential vs Schouten differential using
structure constants alone:
- $d_{\mathrm{CE}} c^K = -\tfrac12 C^K_{IJ} c^I c^J$
- $d_{\mathrm{CE}} u_K = C^L_{KJ} u_L c^J$
- $d_\pi \theta^K = -\tfrac12 C^K_{IJ} \theta^I \theta^J$
- $d_\pi O_K = C^L_{KJ} O_L \theta^J$

**Spin tower invoked: trivial.** $\Phi$ is built solely from the
Lie-algebra structure constants $C^K_{IJ}$ of $\mathfrak h$. It does
not invoke any conformal weight grading, primary-field decomposition,
or Virasoro module structure. The "tower" of generators is the dual
Taylor basis $\{\delta_I\}$ on $\mathfrak h^\vee$, not a Virasoro
descendant tower.

**Cross-reference chain.** Proof depends on
`lem:continuous-bar-cobar` (Tate-conilpotent bar-cobar),
`lem:linear-poisson-schouten` (linear Poisson-Schouten bracket
identity on the Kirillov coalgebra), and the standard Chevalley–Eilenberg
sign conventions of Loday-Vallette. None reaches Sugawara.

**Verdict.** **No silent (A2$''_T$) usage.**

### §2.4 `thm:open-closed-derived-center-factorization` (`main.tex:1996-2191`)

**Claim verbatim** (item 1, the load-bearing morphism).

> "There is a continuous interval-wise morphism of $P_0$ factorization
> algebras
> $\Phi^{\mathrm{Ham}}_{\mathrm{fact}}:
> \mathrm{Obs}^{\mathrm{cl}}_{\mathrm{closed},H,\mathrm{Ham}}|_{\R\times p}
> \to \mathrm Z^{P_0}_{\mathrm{fact}}(A_\partial^{\mathrm{Ham}})$,
> whose underlying CE cochain map on each interval $I$ is given on the
> shifted-cotangent length-one CE coordinates by
> $u_{a(t)dt\otimes f} \mapsto B_f(a)
>  := \int_I a(t)\,\overline{\mathrm{Tr}\,f(\phi_1(t),\phi_2(t))}\,dt$;"

**Hypothesis dependence.** (A1), (A2), (A4) plus the locality input
$\{(\phi_1)^i{}_j(t),(\phi_2)^k{}_l(s)\}=\delta^i_l\delta^k_j\delta(t-s)$.
The factorization proof additionally invokes:
- HKR theorem for the free graded-commutative algebra on
  $\mathfrak h_I$;
- Costello-Gwilliam Vol I §6.4 locally-constant factorization-algebra
  vocabulary;
- Lurie HA §5.5 $E_1$-translation.

**Spin tower invoked: bidegree.** Same as §2.3: the only "tower" is the
Taylor bidegree on $\bar A$. The interval-smearing extension
$\mathfrak h_I = \Omega^\bullet_c(I) \widehat\otimes \mathfrak h$ adds
a de Rham coordinate, not a conformal weight. The brane-line
factorization algebra is locally-constant on $\R$ (topological),
**not** conformal — there is no holomorphic structure on the brane line
that would invite Virasoro reparametrization on it.

**Cross-reference chain.** Routes through `prop:grav-ops`,
`prop:stalk-central-multiplication`, `prop:brane-bracket-locality`,
`lem:continuous-bar-cobar`, `cor:local-bulk-boundary-coupling`,
`thm:open-closed-derived-center` (§2.3 above). None reaches Sugawara.

**Verdict.** **No silent (A2$''_T$) usage.**

### §2.5 `stmt:costello-bv-package` (`main.tex:5136-5152`)

**Claim verbatim.**

> "For an elliptic BV theory with a gauge fixing, heat kernel $K_t$,
> propagator $P_{\epsilon,L}=\int_\epsilon^L Q^{\GF} K_t\,dt$, and a
> renormalization scheme, Costello constructs finite-scale effective
> interactions by the RG operator
> $W(P_{\epsilon,L},I[\epsilon]) =
>  \hbar\log(\exp(\hbar\partial_{P_{\epsilon,L}})\exp(I[\epsilon]/\hbar))$.
> The renormalized interaction is obtained by adding local counterterms
> and taking the $\epsilon\to 0$ limit. It has the connected-graph
> expansion … satisfies RG flow and locality, and satisfies the quantum
> master equation when the obstruction classes vanish."

**Hypothesis dependence.** Costello 2011 Ch. 4 §4.4 (counterterm
finiteness, admissible regulator class), Costello-Gwilliam Vol II §11
(BV regulator). This is precisely the source of the (A1)–(A4) inscribed
hypotheses. **No conformal twist.** The framework is the *general*
elliptic BV-Costello regulator class; whether the underlying theory is
topological, holomorphic, or chiral-CFT is determined by the source
theory's specification, not by `stmt:costello-bv-package`.

**Cross-reference chain.** This is an *imported* statement. Its only
upstream is the cited Costello-Gwilliam framework. Its downstream is
the manuscript's mixed brane-defect Costello obstruction at
`prob:weighted-rg-locality` and the descendant graph realization at
`prob:analytic-graph-realization`. None of these downstream
applications invokes a conformal twist.

**Verdict.** **No silent (A2$''_T$) usage.** The Costello BV package is
generic and does not by itself impose or assume a Virasoro structure.
A conformal twist would require a separate `stmt:costello-cft-regulator`
import (Costello 2011 Ch. 5 §5.2) which is **not present** in the
manuscript.

### §2.6 Tate-T1 through Tate-T5

Examined exhaustively for any Sugawara-mode invocation:

| File | Sugawara/Virasoro/Stress-tensor invocation? | Notes |
|------|---------------------------------------------|-------|
| `tate-T1-weighted-completion.tex` | **None.** | Weighted Tate completion on the Heisenberg-Hamiltonian Lie algebra; (A1)-(A4) hypotheses inscribed in `defn:regulator-admissible-sector`, all on the topological/chain-level side. The "polynomial-degree-bounded vertices" at line 19 and the "vertexwise polynomial-degree-bounded interactions" at line 452 are in the $z_1, z_2$ monomial sense — *not* in the $J$-mode Sugawara sense. The Casimir convergence theorem is on $\mathfrak h_w \widehat\otimes \mathfrak h^{\vee,w}_{\mathrm{cont}}$ where $\mathfrak h_w$ is the weighted Heisenberg-Hamiltonian Lie algebra — no $L_n$ modes appear. |
| `tate-T2-nilpotent-truncation.tex` | **None.** | Nilpotent truncation $\mathfrak h_{\leq N} = \mathfrak m^3 / \mathfrak m^{N+1}$ on the Heisenberg-Hamiltonian Lie algebra. The phrase "conformal-symplectic $\mathfrak{sl}_2$" appearing at lines 80, 132, 322, 453, 470, 488, 545, 563 refers to the $H_2 = \mathrm{span}\{z_1^2, z_1 z_2, z_2^2\} \cong \mathfrak{sl}_2$ Lie subalgebra of *quadratic Hamiltonians* — i.e., the *linear symplectomorphism* $\mathfrak{sp}(2,\C) \cong \mathfrak{sl}_2$ acting on $\C^2$, **not** the Virasoro $\mathfrak{sl}_2 = \{L_{-1}, L_0, L_1\}$ subalgebra. See §2.6.1 below for the terminology-collision flag. |
| `tate-T3-quillen-equivalence.tex` | **None.** | Tate-conilpotent bar-cobar Quillen equivalence in an admissible bounded-below Mittag-Leffler envelope; pure Loday-Vallette / Hinich model-categorical machinery. |
| `tate-T4-bv-vanishing.tex` | **None.** | Costello-Li 2012 BV-cohomology-vanishing route applicability check. The five failure modes (F1)-(F5) are non-compactness, topological-holomorphic mixing, brane defect, $\mathfrak{gl}_N$ vs $\mathfrak{gl}(N\mid N)$, and coefficient-Tate vs worldsheet-Tate direction. None invokes Virasoro. |
| `tate-T5-chain-level-primitive.tex` | **None.** | Chain-level primitive projection on the polynomial one-$\psi$ open-BV side. "Descendant" here means the one-$\psi$ PBW special-fibre class $\widetilde\Psi_{a,b}$, **not** Virasoro descendant. |

#### §2.6.1 Terminology collision flag (informational, not a silent strengthening)

`tate-T2-nilpotent-truncation.tex:80-81` uses the phrase "conformal-symplectic
generators $H_2 = \mathrm{span}\{z_1^2, z_1 z_2, z_2^2\} \cong \mathfrak{sl}_2$".
This terminology is mathematically standard for the Lie algebra of
linear symplectomorphisms of $(\C^2, dz_1 \wedge dz_2)$, which
abstractly is $\mathfrak{sp}(2,\C) \cong \mathfrak{sl}_2$. However,
because the Phase-4 reconstitution corpus uses "conformal" to denote
the **conformal Virasoro** structure on the twisted side after
$\tau_T$, and because the abstract isomorphism
$\mathfrak{sp}(2,\C) \cong \mathfrak{sl}_2 \cong
\mathrm{span}\{L_{-1}, L_0, L_1\} \subset \mathfrak{Vir}$ is a real
mathematical identity (the Möbius subalgebra of $\mathfrak{Vir}$ acts
by the conformal $\mathfrak{sl}_2$), a future reader could **mistakenly**
conflate the two notions of "conformal $\mathfrak{sl}_2$".

**This is a clarity issue, not a silent (A2$''_T$) usage.** No
Sugawara construction is invoked: the Lie algebra $H_2$ acts as
*ambient symplectomorphisms* of the target $\C^2$, not as the Möbius
$\mathfrak{sl}_2 \subset \mathfrak{Vir}$ on a worldsheet. The
non-conilpotency obstruction documented in `tate-T2-nilpotent-truncation.tex:484-498`
is precisely the algebraic fact $[\mathfrak{sl}_2, \mathfrak{sl}_2] =
\mathfrak{sl}_2$, which is the Lie-algebra-level statement —
identical regardless of which concrete realization of $\mathfrak{sl}_2$
one has in mind. So the manuscript's argument is correct; only the
terminology might collide with future $(A2''_T)$-related text.

**Recommendation.** When $(A2''_T)$ is eventually inscribed (post
G4-T2.2 introduction), accompany it with a one-line clarifying remark
distinguishing:
- "conformal-symplectic $\mathfrak{sl}_2$" = $\mathrm{span}\{z_1^2,
  z_1 z_2, z_2^2\}$ subalgebra of *target-space* quadratic
  Hamiltonians;
- "conformal Virasoro $\mathfrak{sl}_2$" = $\mathrm{span}\{L_{-1}, L_0,
  L_1\}$ Möbius subalgebra of *worldsheet* Virasoro.

This is a §6 inscription-readiness recommendation, not a silent
strengthening repair.

### §2.7 Normal-ordered products in the matrix Weyl algebra

A second potential collision deserves explicit dispatch: the manuscript
uses "normal-ordered" in connection with the Capelli identity and
Razmyslov-Procesi. Sites:
- `main.tex:418` "normal-ordered quantum comoment imposes …";
- `main.tex:444-445` "normal-ordered moment relation
  $Y_\hbar X_\hbar - X_\hbar Y_\hbar + \hbar N\,I \equiv 0$";
- `main.tex:4665-4671` "the normal-ordered quantum comoment is
  $\widehat\mu_\epsilon = -\mathrm{Tr}([\epsilon,\phi_1]\phi_2)$";
- `main.tex:4762-4818` `rmk:normal-ordering-obstruction` and
  `rmk:capelli-renormalized-traces`;
- `main.tex:4839-4910` Capelli renormalized stable connected trace.

**Every "normal-ordered" usage is in the matrix Weyl algebra
$\mathcal W_N$ sense:** the convention picks a fixed left-to-right
ordering of $\phi_1$ vs $\phi_2$ inside finite words
$\mathrm{Tr}(\phi_1^a \phi_2^b)$, with the Capelli/Wick contraction
$[X,Y] = \hbar N$ rearranging traces. This is **not** the Sugawara
$:J(z) J(w):$ normal ordering, which is a CFT-level removal of the OPE
short-distance singularity in radial-ordered products of currents on a
worldsheet.

**Verdict.** **No silent (A2$''_T$) usage.** The matrix-Weyl normal
ordering and the Sugawara CFT normal ordering are unrelated; the
manuscript invokes only the former.

### §2.8 Theorem-lanes index (`theorem-lanes.tex`)

Examined all 9 theorem-lanes (lines 12–456): Dirac brane probe, stable
trace and one-$\psi$ PBW shadow, CE/PV derived centre, Matlis principal-part
cotangent module, brane-line factorization currents, reduced
principal-part defect currents, degree-zero Moyal/Weyl sector and graph
boundary, scalar $U(1)$ anomaly. **None** invokes Sugawara, Virasoro,
$T(z)$, or any conformal-VOA structure. Each lane's "Local assertion"
and "Proof dependency map" stays inside the
Heisenberg-Hamiltonian / matrix-Weyl / formal-symplectic-disk world.

### §2.9 Claim-strength ledger (`claim-strength-ledger.tex`)

Examined all 14 claim entries (lines 27-141). **None** invokes
Virasoro/Sugawara content. The "Degree-zero Moyal/Weyl quantization"
entry (lines 73-78) explicitly fixes the "Capelli/Weyl normalization
and formal Moyal commutator" — which is the matrix-Weyl algebra
flavour, not a worldsheet conformal flavour. The "Cross-volume
consequences" entry (lines 130-139) is explicitly a *firewall*
declaration that no compact CY, BCOV, BKM, Igusa transfer is asserted —
this further excludes conformal-CFT content from the claim package.

### §2.10 Open-obligations (`open-obligations.tex`)

Examined all 14 enumerated obligations. The "Mixed brane-defect QME"
obligation (lines 123-151) and "All-order Costello graph realization"
(lines 153-157) reference the Costello regulator class but stay
topological/holomorphic. No conformal CFT obligation is named.

### §2.11 Appendix-unreduced-bv-qme (`appendix-unreduced-bv-qme.tex`)

Examined all 179 lines. The "Polynomial unreduced centrality no-go"
(`thm:app-unreduced-polynomial-centrality-no-go`, lines 33-91) uses
"finite polynomial degree in $\phi_1, \phi_2, \psi$" — purely
matrix-side polynomial. The "Scalar contact QME class"
(`prop:app-scalar-contact-qme-class`, lines 93-126) uses
$\omega(f,g) = [\{f,g\}]_0$ Lie 2-cocycle and the matrix-Weyl Capelli
shift $\hbar N\,\mathrm{Tr}(A)$. No Sugawara invocation.

---

## §3 Inscription-readiness recommendations

Because the audit returns a null result, the recommendation is **not**
to repair existing silent usage but to **prepare** $(A2''_T)$ for
future inscription, *contingent* on the manuscript's eventual scope
broadening to include the conformal Virasoro promotion functor
$\tau_T$.

### §3.1 Defer $(A2''_T)$ inscription to post-G4-T2.2-uplift

The G4-T2.2 conformal Virasoro promotion lives entirely in the
reconstitution corpus. Until the manuscript is extended to include:
- a manuscript-level definition of $\tau_T$ (the conformal-promotion
  functor);
- a manuscript-level theorem inscribing the Sugawara-form $T(z)$ on
  the Heisenberg-Hamiltonian factorization centre;
- a manuscript-level Schiffmann-Vasserot / $W_{1+\infty}$ central-charge
  formula;

…there is **no candidate dependent inscription** on which $(A2''_T)$
could become silently load-bearing. The hypothesis stays in the
Phase-4 EXEC corpus as a *declared standby*.

### §3.2 Prepare a future-conditional $(A2''_T)$ stub in `tate-T1`

When the conformal Virasoro promotion is eventually inscribed, the
declaration block should be added immediately after the inscribed (A2)
in `defn:regulator-admissible-sector`. The exact LaTeX block is the
one drafted in `phase4-exec-Hypothesis-Master-Block-2026-04-28.md` lines
180-204 (the
`hyp:A2-prime-prime-T-sugawara` block). For convenience, here is the
block verbatim from the master block:

```latex
\begin{hyp}[(A2\(^{\prime\prime}_T\)) Sugawara polynomial-degree extension on the conformal Virasoro side]\label{hyp:A2-prime-prime-T-sugawara}
When the conformal Virasoro structure is in scope (i.e., on the
twisted side after the conformal promotion functor \(\tau_T\)), the
polynomial-degree-bounded class of (A2) is extended to include the
Virasoro descendants \(L_{-n_1} L_{-n_2} \cdots L_{-n_k}\) with
\(n_i \geq 1\); each such descendant is polynomial-degree-bounded
in the underlying Heisenberg modes via the Sugawara expansion
\(L_n = (1/(2k))\sum_{m \in \Z}{:}J_{n-m} J_m{:}\) (degree two in
the \(J\)-modes per descendant). On the topological side prior to
\(\tau_T\), and on any Felder-twisted free-field realisation with
non-trivial background charge \(\alpha_0\), this extension is not
automatic: the manuscript's working regime is the Sugawara
construction without Felder twist, and (A2\(^{\prime\prime}_T\))
is the operative discipline for that regime.
\end{hyp}
```

Primary-source anchor: Frenkel-Ben-Zvi 2004 §3.4.6-§3.4.8;
Pressley-Segal 1986 §4.2; Sugawara 1968 *Phys. Rev.* 170, 1659-1662.

### §3.3 Inscription firewall

When $(A2''_T)$ is inscribed, a *firewall remark* must accompany it
declaring that **no manuscript theorem proved prior to that inscription
relies on $(A2''_T)$**. The cleanest place is a small subsection at the
top of the (eventually-inscribed) conformal-promotion section, e.g.:

> "Remark (Topological-side independence). All theorems of the present
> manuscript (Theorems A through G, Lemmas, Propositions, and the
> derived-centre and factorization assertions of §[ssec:tate-residual-resolution])
> are stated and proved on the *topological / chain-level* side and
> require only $(A1)$, $(A2)$, $(A3)$, $(A4)$ in the
> inscribed-admissible-regulator-sector. The hypothesis $(A2''_T)$
> defined below, the conformal Virasoro promotion functor $\tau_T$,
> and the Sugawara form on Virasoro descendants are required
> exclusively on the *twisted side*, in the conformal Virasoro
> promotion of the chain-level $T(z) = J^{(2)}(z)$. No prior theorem
> in this manuscript silently depends on $(A2''_T)$."

This firewall is the audit's positive recommendation: it makes the
null-result of the present audit a load-bearing meta-statement
once $(A2''_T)$ enters the manuscript.

---

## §4 Cross-walk to (A2$'$) joint-dependency

**(A2$'$)** is the silent existence of an even non-degenerate
ad-invariant supersymmetric bilinear form on graded sources, currently
presupposed by the supertrace / queer-trace work in W22-L1, W22-L2,
P4-G3-T-A1, P4-G3-M2 (per
`phase4-exec-A1-hypothesis-audit-2026-04-28.md` §1.6).

**Joint-dependency cases on $(A2''_T)$ and (A2$'$): NONE in the
manuscript.**

In the reconstitution corpus, the cross-walk is documented at
`phase4-exec-G4-T22-virasoro-twist-2026-04-28.md:665-703`:

> "After $\tau_T$, the Virasoro descent is governed by the **Sugawara
> form** on the Virasoro descendants:
> $g_{\mathrm{Sug}}(L_{-n}, L_{-m}) = (k+h^\vee)\delta_{n+m,0} \cdot
> \mathrm{(weight\ factor)}$ … This form is even, non-degenerate,
> ad-invariant, and supersymmetric (bosonic case trivial). On the
> super-W extension to $\mathrm{osp}(2N|2N)$ … the super-Sugawara form
> is the orthosymplectic super-Killing form."

In other words, on the *super-W extension*, $(A2''_T)$ and (A2$'$)
become **simultaneously load-bearing**: the polynomial-degree class
must include $L_{-n}$ Virasoro descendants (A2$''_T$), and the
non-degenerate Sugawara form must serve as the BV pairing (A2$'$).

**However,** the manuscript currently inscribes neither the conformal
Virasoro promotion nor the super-W extension. So **no joint silent
dependency exists in the manuscript**. The joint dependency lives in
the reconstitution corpus only, awaiting eventual inscription.

**Recommendation.** When both $(A2''_T)$ and (A2$'$) are eventually
inscribed (post G3-supertrace and post G4-T2.2 manuscript uplift),
their joint-load-bearing role on the super-W twisted side should be
declared together in a single coherence remark in the
hypothesis-dependency table.

---

## §5 $\tau_T$ implicit invocation map

**$\tau_T$-implicit invocations in the manuscript: NONE.**

The conformal-promotion functor $\tau_T$ documented in
`phase4-exec-G4-T22-virasoro-twist-2026-04-28.md:213-318` constructs:
- the conformal Virasoro structure $T = J^{(2)}$ on $\mathcal A_{\mathrm{fact}}$;
- the OPE descent at central charge $c = (\epsilon_1+\epsilon_2)^2/(\epsilon_1\epsilon_2)$;
- the Sugawara form on Virasoro descendants;
- the right-adjoint to a forgetful functor from conformal-VOA back to
  factorization-algebra-on-$\R$.

**No manuscript theorem invokes $\tau_T$, its Sugawara form, its OPE
descent, or its central charge.** The factorization-algebra-on-$\R$
side stays purely topological in the manuscript: see §2.4 above
($\mathfrak h_I = \Omega^\bullet_c(I) \widehat\otimes \mathfrak h$ is
the *de Rham* current convention, not a holomorphic
$\mathfrak h$-valued $\bar\partial$-current convention).

The Bousfield-localisation candidate for $\tau_T$ identified in
`phase4-exec-G4-T22-virasoro-twist-2026-04-28.md:380-410` is also not
inscribed in the manuscript. So no Bousfield-localisation step in any
manuscript proof implicitly depends on $\tau_T$.

**Conclusion.** The $\tau_T$ implicit-invocation map is **empty**.
Every manuscript inscription stays on the topological / chain-level
side of the conformal-promotion square.

---

## §6 Smallest declaration set

Because §0–§5 establish that *no* silent $(A2''_T)$ usage exists in
the manuscript, the smallest set of *additional inscription
declarations* needed to "make every silent $(A2''_T)$ usage
explicit" is:

**The empty set.**

There are zero silent usages, hence zero new declarations are required
to repair them.

The only declaration that *would* be useful is the **firewall remark**
recommended in §3.3: a one-paragraph statement on the topological-side
independence of all currently-inscribed theorems from $(A2''_T)$. This
remark belongs at the top of any future conformal-promotion section,
and serves as the positive load-bearing claim issued by the present
audit. **Word count of recommended firewall: ≈90 words.**

For completeness, a recommended **future-deferred inscription set**,
to be activated only when the conformal Virasoro promotion is brought
into the manuscript:

| # | Declaration | File:section (proposed) | Status |
|---|-------------|-----------------------|--------|
| 1 | $(A2''_T)$ Sugawara polynomial-degree extension hypothesis block (verbatim, §3.2 above) | new conformal-promotion section, immediately after `defn:regulator-admissible-sector` | future-deferred |
| 2 | Topological-side independence firewall (≈90 words, §3.3 above) | top of new conformal-promotion section | future-deferred (becomes load-bearing once #1 is inscribed) |
| 3 | "Conformal-symplectic vs conformal Virasoro $\mathfrak{sl}_2$" terminology clarification (≈40 words, §2.6.1 above) | in `tate-T2-nilpotent-truncation.tex` near the conformal-symplectic generators introduction (line ~80), or in `notation.tex` | future-deferred (clarity-only, recommended as soon as $(A2''_T)$ enters the manuscript) |

**Total deferred declarations: 3.** All are conditional on a future
manuscript-level inscription of the G4-T2.2 conformal Virasoro
promotion.

---

## §7 Anti-attack scan responses

### (Att-1) Sugawara $T = (1/(2(k+h^\vee))){:}J\cdot J{:}$ implicit in any Virasoro central-charge formula

**Scan result.** No Virasoro central-charge formula appears anywhere in
the manuscript. The Schiffmann-Vasserot $c =
(\epsilon_1+\epsilon_2)^2/(\epsilon_1\epsilon_2)$ does not appear. The
Sugawara central-charge formula $c = k\,\dim\mathfrak g / (k+h^\vee)$
does not appear. The free-boson Sugawara $c = 1$ does not appear.

**Verdict.** No silent Sugawara invocation via central-charge
arithmetic.

### (Att-2) $(A2''_T)$ extension changes polynomial-degree class to include arbitrary $:J^n:$ composites

**Scan result.** No use of normal-ordered $J$-mode composites in any
inscription. The "polynomial degree" in the manuscript is consistently
the *target-space* polynomial degree in $z_1, z_2$ (Heisenberg-Hamiltonian
generators on $\C^2$), not in $J$-modes. The matrix-Weyl normal ordering
of §2.7 is not a $J$-mode normal ordering: it acts on
$\mathrm{Tr}(\phi_1^a \phi_2^b)$ inside $\mathcal W_N$, which has no
worldsheet-mode interpretation in the manuscript.

**Verdict.** No silent $:J^n:$ composite invocation.

### (Att-3) $\tau_T$ right-adjoint via Sugawara, Bousfield-localisation citation could implicitly require $(A2''_T)$

**Scan result.** No Bousfield-localisation invocation in any
manuscript inscription. The categorical machinery at use is:
- Tate-conilpotent bar-cobar Quillen equivalence (`tate-T3`);
- Loday-Vallette Algebraic Operads model structure;
- Hinich transfer theorem;
- Costello-Gwilliam locally-constant factorization-algebra vocabulary;
- Lurie HA §5.5.

None of these is a Bousfield-localisation **of the type that would
factor through Sugawara**. (The Tate-conilpotent Quillen equivalence
is internal to the topological/chain-level side.)

**Verdict.** No silent $\tau_T$ right-adjoint invocation.

### (Att-4) Schiffmann-Vasserot $c = (\epsilon_1+\epsilon_2)^2/(\epsilon_1\epsilon_2)$ implicit in G1-M1

**Scan result.** The G1-M1 closure documented in
`phase4-exec-G1-M1-BD-chiral-2026-04-28.md` derives the formula in the
reconstitution corpus, **not** in the manuscript. The manuscript's
G1-class (degree-zero Moyal/Weyl sector and graph boundary,
`thm:lane-moyal-degree-zero` in `theorem-lanes.tex`) computes only
the first and third Costello graph normalizations on the open-line
boundary product, with no central-charge formula. Concretely:
- `prop:unconditional-boundary-product-normalization` and
  `prop:open-line-midpoint-graph-weights` compute reduced open-line
  coefficients $\hbar P(f,g)$ and $\hbar^3 P^3(f,g)/24$ — these are
  Moyal coefficients, not Schiffmann-Vasserot central charges.

**Verdict.** No silent Schiffmann-Vasserot invocation.

### Anti-attack summary

All four attack angles return **negative**. The manuscript's separation
from the conformal Virasoro side is clean, defended by the
target-space polynomial flavour of (A2), the matrix-Weyl normal
ordering of (A2)-adjacent quantum statements, and the absence of any
$\tau_T$ / Bousfield / central-charge invocation.

---

## §8 Closing remark — what this null result means

The present audit establishes a **non-trivial epistemic boundary**:
the manuscript is *currently* clean of the silent strengthening
$(A2''_T)$. This is not a vacuous statement — given the layered
hypothesis structure (A1)–(A5)+(A2$'$)+(A2$''_T$), the existence of a
silent strengthening is *normally* the default state, and absence
requires verification. The audit verifies the absence.

**Strategic implication.** When the manuscript is extended to include
the G4-T2.2 conformal Virasoro promotion (post P5 or P6, depending on
the planned uplift cadence), the firewall remark in §3.3 becomes
load-bearing: it converts the present null-result audit into a
*positive* meta-claim — that the topological-side theorems are
$(A2''_T)$-independent, hence robust under any change to the conformal
Virasoro side that preserves the topological side via the
$\tau_T$-restriction-to-topological functor.

This is the only positive yield of the audit, and is purely
preparatory for future inscription. The present manuscript requires
**zero edits** to be $(A2''_T)$-clean.

---

**End of audit. Total silent (A2$''_T$) usages: 0. Total recommended
manuscript edits at this time: 0. Future-deferred inscription set: 3
(all activated conditional on G4-T2.2 manuscript uplift).**
