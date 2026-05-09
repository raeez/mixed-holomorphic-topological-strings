# Phase 4 Execution / P4-Brane-Species-Audit — Witten + Boundary typology of brane species per classical super-Lie family

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Witten primary (physical interpretation; topological sigma
models; mirror symmetry; D-brane / K-theory anomaly inflow); Boundary
secondary (precise statement of boundary condition for each brane;
topological obstruction classification; brane-defect comparison map
on $\R^2_{\mathrm{top}}\times\C^2_{\mathrm{hol}}$).
**Mode.** Phase-4 EXEC, proposal-only — no manuscript edits, no commits.
Master ledger schema; ID prefix `P4-EXEC-Brane-`. Writable surface:
this file only.
**Posture.** P4-EXEC-G3-M2 (1247 lines) catalogued the strategic
boundary symbolically: gl(N|N) and osp(2N|2N) DISCHARGE; psl(N|N)
DISCHARGES via lift; q(N) DISCHARGES at the ordinary supertrace
layer with parallel `otr` non-discharge (P4-EXEC-G3-M3); p(N) FAILS
at the (A5) parametrix step; sl(M|N) for $M\neq N$ FAILS by
construction. P4-EXEC-G3-M4 verified the symbolic verdict at chain
level on $N=2$ over 540 randomized instances. P4-EXEC-G4-M3 located
the spin-3 super-W vanishing at the orthosymplectic balance $M=N$.
This audit assigns a **brane species** to each family and exhibits
the physical interpretation of the three-tier strategic boundary
through the Witten / Boundary lens.

**Inputs (full reads or targeted reads as indicated).**
* `CLAUDE.md` (full).
* `reconstitution/phase4-exec-classical-super-extension-2026-04-28.md`
  (1247 lines; G3-M2 strategic boundary verdict).
* `reconstitution/phase4-exec-G3-M3-queer-trace-2026-04-28.md` (1108
  lines; q(N) `otr` parallel non-discharge).
* `reconstitution/phase4-exec-Theorem-G-otr-inscription-2026-04-28.md`
  (1374 lines; Theorem G^otr inscription proposal).
* `reconstitution/phase4-exec-G3-M4-super-numerical-sweep-2026-04-28.md`
  (542 lines; N=2 numerical sweep).
* `reconstitution/phase4-exec-G4-M3-W3-twist-2026-04-28.md` (1016
  lines; G3↔G4 cross-coupling, super-W_3 vanishing at $M=N$).
* `reconstitution/wave3-W2-gaiotto-2026-04-28.md` §0–§2 (defect-line
  decomposition, Weiss vs locally constant).
* `reconstitution/wave3-W31-5dM-obstructions-2026-04-28.md` §0–§2
  (CGW boundary VOA, type-clash to manuscript).
* `main.tex` lines 280–470 (Theorem G open/closed,
  `lem:omega-cocycle`, U(1)-center anomaly), 740–820 (mixed brane
  definition, local mixed model on $\R^2\times\C^2$).

**Standard primary-source references (cited from memory; not new
inscriptions).**
* E. Witten, *Topological sigma models*, Comm. Math. Phys.
  **118** (1988), 411–449.
* E. Witten, *Mirror manifolds and topological field theory*, in
  *Essays on Mirror Manifolds*, IP Press 1992 (foundational A/B-twist).
* E. Witten, *D-branes and K-theory*, JHEP **9812** (1998), 019.
* M. Kontsevich, *Homological algebra of mirror symmetry*, Proc.
  ICM 1994 (Birkhäuser 1995), 120–139.
* K. Costello, D. Gaiotto, B. Williams, *M-theory and twisted
  holomorphic field theories*, arXiv:2007.09497 (cited but not
  yet inscribed; see W31 §1 inscription residual).
* Aspinwall, Bridgeland, Craw, Douglas, Gross, Kapustin, Moore,
  Segal, Szendrői, Wilson, *Dirichlet branes and mirror symmetry*,
  Clay Math. Monographs **4**, AMS 2009.
* P. Etingof, V. Ostrik, *Finite tensor categories*, Mosc. Math. J.
  **4** (2004), 627–654.
* D. Gaiotto, G. Moore, A. Neitzke, *Spectral networks and snakes*,
  Annales Henri Poincaré **15** (2014), 61–141.
* A. Sen, *SO(32) spinors of type I and other solitons*, JHEP
  **9809** (1998), 023 (anti-brane / tachyon condensation).
* Strominger, Yau, Zaslow, *Mirror symmetry is T-duality*,
  Nucl. Phys. B **479** (1996), 243–259 (SYZ self-dual brane).
* M. Kontsevich, Y. Soibelman, *Notes on A-infinity algebras,
  A-infinity categories and non-commutative geometry I*, in
  *Homological mirror symmetry*, Lecture Notes in Phys. **757**,
  Springer 2009 (Fukaya / homotopy categories of branes).
* Cheng–Wang 2012 §1 (super-Lie families, brane catalog implicitly
  through finite tensor categories).
* Polishchuk–Schwarz 2003 (categories of holomorphic D-branes on
  CY).
* Gukov–Witten 2007 *Branes and quantization* (geometric quantization
  of brane phase space).

---

## §0. Executive verdict — three-tier brane-species typology

The G3-M2 strategic boundary cleanly partitions the classical
super-Lie families by the chain-level discharge mechanism. The
Witten / Boundary lens reads this partition as a **physical
brane-species typology**: each tier corresponds to a distinct class
of topological-string brane realizations on the manuscript's
local mixed model $\R^2_{\mathrm{top}}\times\C^2_{\mathrm{hol}}$.

| Tier | Algebraic verdict | Brane species | Witten interpretation |
|---|---|---|---|
| **(I) Standard discharge** | gl(N|N), osp(2N|2N), psl(N|N) via lift | (A) **Witten supersymmetric brane stack** with bosonic-fermionic charge cancellation; (B) for osp: **mirror-self-dual O-brane** in SYZ sense; (C) for psl: **central-projected D-brane** modulo $\C\cdot I$ Chan–Paton scalar | Anomaly inflow from bulk to boundary cancels via $\Str(I)=0$ super-balance. Brane-anti-brane systems with matched even/odd content; Witten 1998 *D-branes and K-theory* characterization holds verbatim. |
| **(II) Parallel anomaly (q(N))** | $\Str$-channel discharges; $\mathrm{otr}$-channel produces independent residue Theorem G^otr | **Doubled (Str-brane, otr-brane) pair**: the Str-brane is a standard diagonal brane modulo $I_{2N}$; the otr-brane is an **off-diagonal mixed-parity brane** witnessing the queer central direction $J\in\mathfrak q(N)_{\bar 1}$ | Witten lens: the q(N) brane stack is a **two-channel boundary state**; the second channel records a parastatistic (Sergeev-type) open-closed duality invisible to bosonic probes. Physical: parastatistic Gukov–Witten parastate brane, no bosonic dual. |
| **(III) Outright failure** | p(N), sl(M|N) M≠N | **No standard topological-string brane species realized**: p(N) is forbidden by the absence of an even ad-invariant form (no SYZ self-dual or A/B-brane structure); sl(M|N) M≠N carries a **non-cancelling brane charge** ($M-N$) that obstructs anomaly inflow | Witten lens: p(N) corresponds to an **odd-symmetric polarization** that no consistent topological brane stack can support without an orientifold-like projection (which breaks (A5) parity-equivariance, see §10 Att-2). sl(M|N), M≠N, is a **net D-brane charge** geometrically — a non-zero K-theory class that is the residue $\hbar(M-N)\bar c$ already named in the QME obstruction. |

**Convergence verdict.** The three-tier algebraic boundary lifts to
a three-tier brane-species typology consistent with: (i) Witten
1988 topological sigma models; (ii) Kontsevich 1994 homological
mirror symmetry; (iii) Sen 1998 / Witten 1998 brane–anti-brane and
K-theory; (iv) the manuscript's own brane-defect comparison map
(`main.tex` 354–393). **No tier requires structure beyond the
classical super-Lie source plus the manuscript's local mixed
model.**

**Per-target verdict.**

| Target | Brane species | Witten/Boundary verdict | Confidence |
|---|---|---|---|
| (B.1) per-family identification | three-tier typology | aligned with G3-M2 | high |
| (B.2) gl(N\|N) boundary condition | mixed B-brane in the Witten 1992 sense (Dolbeault-direction), supersymmetric stack of N D-branes | A/B mixed; topological in $\R$, formal-holomorphic in $\C^2$ | high |
| (B.3) osp(2N\|2N) self-duality | SYZ mirror-self-dual O-brane (orientifold-self-mirror) | mirror-self-dual under axis swap $z_1\leftrightarrow z_2$; consistent with W23 σ_swap | medium |
| (B.4) psl(N\|N) central projection | D-brane mod $\C\cdot I$ Chan–Paton; lift to gl Chan–Paton "reaches around" the central scalar | obstruction class $[I]\in H^2_{\mathrm{Lie}}(\bar A,\C\cdot I)$ trivial after projection | medium-high |
| (B.5) q(N) two-supertrace doubled brane | Str-brane (diagonal) and otr-brane (off-diagonal mixed-parity); related by parity twist via $J$ | otr-brane is a Sergeev-type parastate brane | medium |
| (B.6) p(N) non-standard realization | NONE in standard topological-string framework; orientifold attempt breaks (A5) | no canonical brane species | high (no-go) |
| (B.7) sl(M\|N) M≠N residue charge | net D-brane charge $\hbar(M-N)$ on $\R^2\times\C^2$; matches Witten 1998 K-theory class | active anomaly inflow, no brane-side cancellation | high (failure) |
| (B.8) G4-M3 super-W_3 truncation at M=N | spin-tower truncation correlates with orthosymplectic balance brane condition | spin-tower closure forced by M=N brane species | medium |

---

## §1. (B.1) Per-family brane-species identification

### §1.1 The manuscript's brane setup

The manuscript constructs a stack of $N$ topological branes on
$\R\times p$, where $p\in\C^2$ is a brane point and the formal
local model is $\R^2_{\mathrm{top}}\times\C^2_{\mathrm{hol}}$
(`main.tex` 740–820). The brane probe carries a Chan–Paton bundle
of rank $N$, and the open-string field algebra is
$\C[\lie{gl}_N\oplus\lie{gl}_N]^{GL_N}$ (`main.tex` 122–128).

The U(1)-center anomaly class $[\bar c]\in H^2_{\mathrm{Lie}}(\bar A,\C)$
of `lem:omega-cocycle` is **the algebraic shadow of the Chan–Paton
center** ($\C\cdot I\subset\mathfrak{gl}_N$): the anomaly is a
**brane-charge obstruction** to splitting the central extension
$\mathfrak h_{\mathrm{poly}}\to\bar A$ on the closed side, mirrored
on the open side as the bracket $\{\Tr\,\phi_1,\Tr\,\phi_2\}=N$
(`main.tex` 354–369). This is the **prototype** for our brane
species typology: each super-Lie source $\mathfrak g$ supplies a
distinct Chan–Paton bundle, and the central directions of $\mathfrak g$
(the centre of the matrix algebra restricted to $\mathfrak g$)
classify the anomaly classes.

### §1.2 Brane species per super-Lie family

Each classical super-Lie family corresponds to a brane species
labelled by:
* the dimensions $(\dim\mathfrak g_{\bar 0}, \dim\mathfrak g_{\bar 1})$
  (Chan–Paton parities);
* the centre of the matrix algebra restricted to $\mathfrak g$
  (number of central directions = dimension of brane-charge anomaly
  space);
* the trace channel(s) ($\Str$, $\mathrm{otr}$, both, neither);
* the parity-equivariance of the relevant heat-kernel parametrix
  (whether unsigned (A5), signed (A5)^otr, or no consistent class
  exists).

The standard Witten / Kontsevich brane species are realized as:

| Family | $\dim\mathfrak g_{\bar 0}$ | $\dim\mathfrak g_{\bar 1}$ | Centre dim | Trace channels | Witten species |
|---|---|---|---|---|---|
| gl(N\|N) | $2N^2$ | $2N^2$ | $\C\cdot I_{2N}$ (1-dim) | $\Str$ only | **B-brane stack** with $\Str$-cancellation |
| osp(2N\|2N) | $2N^2+N$ | $2N^2$ | $\C\cdot I$ (1-dim) | $\Str$ only | **SYZ-self-dual O-brane** |
| psl(N\|N) | $2N^2-1$ | $2N^2$ | trivial (modded) | $\Str$ via lift | **central-projected D-brane** |
| q(N) | $N^2$ | $N^2$ | $\C\cdot I_{2N}\oplus\C\cdot J$ (2-dim) | $\Str$ AND $\mathrm{otr}$ | **(Str-brane, otr-brane) doubled brane** |
| p(N) | $N^2$ | $N^2$ | trivial (no even invariant) | NONE | **NO standard species** |
| sl(M\|N), M≠N | $M^2+N^2$ | $2MN$ | $\C\cdot I_{M+N}$ (1-dim, but $\Str=M-N$) | $\Str$ but NON-CANCELLING | **net D-brane charge** $\hbar(M-N)$ |

These six rows are the per-family brane-species identification.
The Witten lens organizes them in three tiers by whether the brane
species is consistent (tier I), doubled (tier II), or absent /
charge-residual (tier III).

---

## §2. (B.2) gl(N|N) brane species — supersymmetric B-brane stack

### §2.1 Boundary condition

The gl(N|N) brane probe is a **stack of N+N D-branes** on
$\R\times p\subset\R^2\times\C^2$, with $N$ even (bosonic) branes
and $N$ odd (fermionic) anti-branes. The Chan–Paton bundle is
$\C^{N|N}=\C^N\oplus\Pi\C^N$, and the open-string field algebra is
$\C[\mathfrak{gl}(N|N)\oplus\mathfrak{gl}(N|N)]^{GL(N|N)}$ — the
super-invariant ring of pairs of supermatrices.

**Witten 1992 / 1998 interpretation.** This is a **B-brane stack** in the
mixed sense of `def:local-th-string` (`main.tex` 745): topological
along the $\R$-direction, formal-holomorphic in the $\C^2$-direction
(Dolbeault model). The supersymmetric structure realizes Witten
1998's brane–anti-brane pair: the bosonic $N$ branes carry charge
$+1$, the fermionic $N$ anti-branes carry charge $-1$, and the
**net K-theory class is zero** by the supertrace cancellation
$\Str(I)=N-N=0$.

The boundary condition is:
* In the topological direction ($\R$): de Rham / topological boundary
  state, locally constant factorization (Lurie HA §5.5.4.10).
* In the holomorphic direction ($\C^2$): Dolbeault / formal-holomorphic
  boundary state, $\bar\partial$-cohomology with values in $\End(\C^{N|N})$.

### §2.2 The role of $\Str$ in anomaly inflow

The supertrace is the **K-theory pairing**: it classifies the net
brane charge of the $\C^{N|N}$ Chan–Paton bundle. Witten 1998
*D-branes and K-theory* establishes that:
* $K^0(\mathrm{point})=\Z$ generated by the rank;
* a stack of branes-anti-branes carries class $[\C^N]-[\Pi\C^N]\in
  K^0$, computed by the supertrace of the identity;
* the brane charge $\Str(I)=N-N=0$ at super-balance means the stack
  is **K-theoretically equivalent to the empty brane** — the
  anomaly inflow vanishes.

This is exactly the W22-T1+T2 chain-level statement: the QME
obstruction class $\hbar\Str(I)\cdot\Lambda^{\Str}(\omega)=0$
because $\Str(I)=0$, which is the K-theory shadow of the brane
charge cancellation.

### §2.3 Verdict on (B.2)

**Verdict.** gl(N|N) realises a **mixed B-brane stack** in the sense
of `def:local-th-string` (`main.tex` 745–777), with bosonic-fermionic
charge cancellation via $\Str(I)=0$. The boundary condition is:
*(i)* topological / locally constant in the $\R$-direction;
*(ii)* Dolbeault / formal-holomorphic in the $\C^2$-direction;
*(iii)* supersymmetric (graded) Chan–Paton bundle $\C^{N|N}$;
*(iv)* trace channel $\Str$ controls the K-theory anomaly inflow,
which **vanishes at super-balance**.

**Confidence.** High. The Witten 1998 K-theory characterization is
verbatim, and the manuscript's `def:local-th-string` mixed brane
already provides the framework. The new content is the explicit
mapping from W22-T1+T2 chain-level discharge to K-theory-class
brane-charge cancellation.

---

## §3. (B.3) osp(2N|2N) brane species — SYZ-self-dual O-brane

### §3.1 The orthosymplectic balanced structure

osp(2N|2N) preserves an even non-degenerate **graded-symmetric**
bilinear form on $\C^{2N|2N}$:
* The bosonic part is symmetric (orthogonal $O(2N)$);
* The fermionic part is antisymmetric (symplectic $Sp(2N)$).

This balanced structure realizes a **graded self-duality**: under
the SYZ axis swap $z_1\leftrightarrow z_2$, the symplectic form
$\omega=dz_1\wedge dz_2$ is anti-invariant, and the orthosymplectic
form pairs bosons with fermions in a way that respects the swap.

### §3.2 SYZ self-dual orientifold construction

Strominger–Yau–Zaslow 1996 *Mirror symmetry is T-duality* shows
that mirror symmetry on a Calabi–Yau is realized fibrewise by
T-duality on the SYZ Lagrangian fibration. A **self-dual brane**
under SYZ is one that is fixed (as an object in the brane category)
under the T-duality transform.

The osp(2N|2N) brane is **mirror-self-dual** in the following sense:
the bosonic-fermionic pairing is symmetric under the SYZ axis swap
because the orthosymplectic form is graded-invariant (orthogonal on
even, symplectic on odd, with the symplectic anti-symmetry compensating
for the parity sign). The Chan–Paton bundle $\C^{2N|2N}$ with
orthosymplectic structure is **self-conjugate** under SYZ.

This identifies the osp(2N|2N) brane as a **SYZ-self-dual O-brane**
(orientifold of the mirror-self-dual locus). The standard
construction:
* The orthosymplectic group $OSp(2N|2N)$ is the gauge group of an
  orientifold projection of $GL(2N|2N)$;
* The orientifold projection is by the involution that swaps even
  and odd subspaces while flipping the symplectic-orthogonal
  structure;
* The self-dual locus is fixed by this involution, giving a
  brane species that is its own SYZ mirror.

### §3.3 Cross-walk to W23 σ_swap (Att-3)

W23 §I-4 (cited in W31 §1.2 line 124) flags the σ_swap (axis swap
$\epsilon_1\leftrightarrow\epsilon_2$) as a **mirror symmetry**
candidate for the manuscript's mixed cones $C^{+-}, C^{-+}$. The
osp(2N|2N) brane species realizes this σ_swap **at the algebraic
level**: the orthosymplectic form is the symmetry datum that makes
the brane stack invariant under the swap.

Under the W22-T1+T2 chain-level discharge, the osp QME class is
zero because $\Str_{\mathrm{osp}(2N|2N)}(I)=2N-2N=0$. This is the
**brane-charge cancellation** for the SYZ-self-dual O-brane:
the orientifold projection equates particle and anti-particle
contributions, and the K-theory class is zero.

### §3.4 Verdict on (B.3)

**Verdict.** osp(2N|2N) realises a **SYZ-self-dual O-brane** in the
mixed Witten sense: a brane stack with orthosymplectic Chan–Paton
gauge group, self-conjugate under axis swap (= local SYZ mirror
symmetry on the formal $\C^2$ disk), with K-theory class zero by
the orthosymplectic supertrace cancellation. The boundary condition
is the orthosymplectic-invariant version of the gl(N|N) boundary
condition: **(i)** topological in $\R$; **(ii)** Dolbeault in $\C^2$;
**(iii)** orthosymplectic Chan–Paton bundle $\C^{2N|2N}$ with
graded-invariant form; **(iv)** SYZ-self-dual.

**Confidence.** Medium. The SYZ-self-dual identification is
algebraically clean (orthosymplectic is graded-invariant under the
symplectic axis swap), but the precise SYZ T-duality cross-check
on the formal disk requires the SYZ Lagrangian fibration structure
on $\C^2$ (which is trivially the projection $\C^2\to\R^2$), and a
matched-conventions verification with the manuscript's σ_swap is
W23 / W31 territory not closed at this level.

---

## §4. (B.4) psl(N|N) brane species — central-projected D-brane

### §4.1 The lift-to-gl(N|N) construction

psl(N|N) is the simple quotient of sl(N|N) by its 1-dimensional
center $\C\cdot I_{2N}$. The G3-M2 §1 verdict establishes that the
chain-level discharge mechanism on psl(N|N) operates **via lift to
gl(N|N)**, not natively on psl. The brane-species interpretation is:

> The psl(N|N) brane is a **gl(N|N) brane stack with the
> central Chan–Paton scalar quotiented out**. The lift "reaches
> around" the central scalar by working on the unprojected gl(N|N)
> source, where the U(1)-center anomaly of `thm:u1-center-anomaly-open`
> is zero ($\Str_{\mathrm{gl}(N|N)}(I)=0$) and the projection to psl
> is by quotienting the central scalar direction.

### §4.2 Topological obstruction class

The obstruction class for the central projection lives in
$H^2_{\mathrm{Lie}}(\bar A,\C\cdot I)$ — the $\C\cdot I$-coefficient
Lie 2-cohomology. This is **trivially zero** because:
* The central scalar $I\in\mathfrak{sl}(N|N)\subset\mathfrak{gl}(N|N)$
  has $\Str(I)=N-N=0$;
* The projection $\mathfrak{sl}(N|N)\to\mathfrak{psl}(N|N)$ kills
  $\C\cdot I$ exactly — no residual obstruction;
* The lifted source's W22-T1+T2 discharge restricts to psl with
  zero residual.

The structurally surprising finding (G3-M2 §1.7 verified at $N=2$
in G3-M4 §3): the **adjoint-rep supertrace** on psl(2|2) is
$-2\neq 0$, while the **defining-rep supertrace** is $0$. The W22
mechanism uses the defining-rep supertrace, so the discharge holds;
but the adjoint-rep non-zero supertrace records a residual
"non-basic-classical-ness" of psl that the brane-species interpretation
absorbs into the **central projection** step.

### §4.3 Witten interpretation: a D-brane "modulo Chan–Paton scalar"

The psl brane is a **D-brane stack on which the Chan–Paton scalar
$\C\cdot I$ is gauge-equivalent to the identity**. Physically:
* On the lift gl(N|N), there is a U(1) gauge field on the brane
  stack representing the Chan–Paton scalar direction;
* Quotienting to psl gauge-fixes this U(1) to zero;
* The remaining gauge group on the brane is $PSL(N|N)$ (the
  projective unitary supergroup).

This is **not** an orientifold — orientifolds quotient by a $\Z/2$
involution, not a U(1). It is a **central gauge fixing**: the
overall U(1) Chan–Paton scalar is fixed to zero, leaving a
"projective" brane.

The Witten lens sees this as: the brane-defect comparison map
(`main.tex` 354–369) on psl is the same as on gl modulo the
central direction. The U(1)-center anomaly $[\bar c]$ is **zero**
on the central direction $\C\cdot I_{2N}$ (because $\Str(I_{2N})=0$
on the lift), so projecting to psl preserves the anomaly cancellation.

### §4.4 Verdict on (B.4)

**Verdict.** psl(N|N) realises a **central-projected D-brane** —
the gl(N|N) brane stack with the U(1) Chan–Paton scalar
gauge-fixed to zero. The lift to gl(N|N) "reaches around" the
central scalar in the sense that the W22 chain-level discharge
operates on the lift, not natively on psl, and the obstruction
class for the central projection is identically zero in
$H^2_{\mathrm{Lie}}(\bar A,\C\cdot I)$. The boundary condition is
the gl(N|N) boundary condition with $PSL(N|N)$ gauge group instead
of $GL(N|N)$.

**Confidence.** Medium-high. The central-projection picture is
clean (it matches the algebraic lift-and-discharge structure), and
the Witten 1998 D-brane / K-theory framework supports this
identification: gauge-fixing the U(1) Chan–Paton scalar is a
standard maneuver in topological-string D-brane constructions
(c.f. Aspinwall et al. 2009 Ch. 5).

---

## §5. (B.5) q(N) brane species — doubled (Str-brane, otr-brane) pair

### §5.1 The two-channel boundary state

The G3-M3 verdict establishes that q(N) carries **two distinct
trace channels** ($\Str$ and $\mathrm{otr}$), with **two
correspondingly distinct anomaly classes**:
* $\Str$-channel: discharges via W22-T1/T2 (since $\Str(I_{2N})=0$
  on q(N));
* $\mathrm{otr}$-channel: produces non-trivial residue
  $\hbar N[\bar c]^{\mathrm{otr}}$ (Theorem G^otr).

The Witten lens reads this as a **doubled brane** on q(N): the
brane-stack realization has *two* boundary states, one for each
trace channel. Concretely:

**Str-brane** ("diagonal brane"):
* Chan–Paton bundle: $\C^{2N}=\C^N\oplus\Pi\C^N$ with the **diagonal**
  embedding (treating $\mathfrak q(N)\subset\mathfrak{gl}(N|N)$ as
  the diagonal-block subalgebra).
* Boundary condition: standard mixed B-brane on $\R\times p$ with
  $GL(N)$ gauge group acting diagonally (since the q(N) even part
  is $\mathfrak{gl}_N$, not $\mathfrak{gl}_N\oplus\mathfrak{gl}_N$).
* Trace channel: $\Str=\Tr_{\bar 0}-\Tr_{\bar 1}$ (vanishes on the
  q(N) identity since the even-block trace equals the odd-block
  trace).
* K-theory class: zero (anomaly inflow cancelled).

**otr-brane** ("off-diagonal mixed-parity brane"):
* Chan–Paton bundle: $\C^{2N}$ with the **off-diagonal** embedding
  via the queer central element $J=((0,I_N),(-I_N,0))$ — the
  Chan–Paton direction has a parity flip implemented by $J$.
* Boundary condition: parastatistic / Sergeev-type boundary, with
  parity-flipping operator $\tau$ (= conjugation by $J$); the
  parametrix satisfies the **signed** parity-equivariance
  $\tau\Delta\tau^{-1}=-\Delta$ (G3-M3 §3.3).
* Trace channel: $\mathrm{otr}=\Tr|_{\bar 1}$ (lands in $\Pi\C$,
  evaluating on the queer central direction $J$ to give $N$).
* K-theory class: **non-trivial** in the **odd-shifted** K-theory
  $K^1(\mathrm{point})=0$ — wait, this is zero in standard
  K-theory; the residue lives in a parity-shifted variant. Concretely,
  the otr-class is in $H^2_{\mathrm{Lie}}(\bar A,\Pi\C)_{\bar 1}$,
  which is the **Sergeev-extended** brane-charge anomaly space.

### §5.2 Are the two branes related by a parity-twist?

**Yes, by conjugation with $J$.** The off-diagonal embedding of the
otr-brane is obtained from the diagonal embedding of the Str-brane
by **conjugation with the queer central element** $J$:
\[
   T\mapsto J T J^{-1}, \qquad J^{-1}=-J\quad\text{(since }J^2=-I).
\]
This is a parity-flipping automorphism of $\mathfrak q(N)$ (G3-M3
§3.1 lines 314–348 verify $JAJ=A$ for $A$ even and $JBJ=-B$ for $B$
odd, where the bracket-action ground the structure). The
corresponding **brane-stack twist** is the parity-shift
\[
   \tau:\C^{2N}\to\Pi\C^{2N}, \qquad\tau^2=\mathrm{id}\cdot(-1).
\]
i.e., $\tau$ is a "square root of the parity-flipping involution".

The two branes (Str-brane and otr-brane) are exchanged by $\tau$
in the sense that:
* The Str-brane sees the diagonal (parity-preserving) Chan–Paton
  embedding;
* The otr-brane sees the $\tau$-twisted (parity-flipping)
  Chan–Paton embedding;
* They are images of each other under conjugation by $J$.

This is a physical realization of **parastatistics** (Sergeev 1983,
1985): the two branes are particle and parastate companions.

### §5.3 Off-diagonal mixed-parity brane interpretation

The otr-brane is **realizable as an off-diagonal mixed-parity
Dirichlet brane**:
* The Chan–Paton bundle has parity-mixed structure: even-direction
  carries $\C^N$, odd-direction carries $\Pi\C^N$ — *and* the
  off-diagonal blocks (which encode the queer-central direction
  $J$) carry **parity-flipping intertwiners**.
* The Dirichlet boundary condition pins the brane to the locus
  $\R\times p\subset\R^2\times\C^2$, but the parity-flipping
  intertwiners on the off-diagonal blocks force the boundary state
  to mix even and odd field content.
* The trace channel $\mathrm{otr}$ is precisely the projection onto
  these off-diagonal blocks ($B$-block in the q(N) matrix
  realization, Cheng–Wang Ch. 6).

This is consistent with the Cheng–Wang Ch. 6 finite-tensor-category
description of $\mathfrak q(N)$-modules, which includes
parity-mixed (queer) blocks. The otr-brane corresponds to the
parity-mixed block in the Etingof–Ostrik 2004 finite tensor category
on degenerate stacks.

### §5.4 Verdict on (B.5)

**Verdict.** q(N) realises a **doubled brane** consisting of:
* a **Str-brane** (diagonal mixed B-brane stack with $GL_N$ Chan–Paton,
  K-theory class zero);
* an **otr-brane** (off-diagonal mixed-parity Dirichlet brane,
  Chan–Paton bundle with parity-flipping intertwiners on
  off-diagonal blocks, trace channel $\mathrm{otr}$ landing in
  $\Pi\C$).

The two branes are related by **parity-twist via conjugation with
the queer central element $J$**. The otr-brane is realizable as an
off-diagonal mixed-parity Dirichlet brane in the Cheng–Wang
finite-tensor-category sense; physically, this is a **parastate
brane** witnessing a Sergeev-type open-closed duality invisible to
bosonic probes.

The independent residue $\hbar N[\bar c]^{\mathrm{otr}}$ of Theorem
G^otr is the **brane-charge anomaly of the otr-brane**: a non-zero
K-theory-shifted class in $H^2_{\mathrm{Lie}}(\bar A,\Pi\C)_{\bar 1}$.

**Confidence.** Medium. The doubled-brane interpretation is
algebraically clean (the q(N) two-supertrace structure is well-known,
Cheng–Wang Ch. 6), but the precise identification of the otr-brane
as a "parastate brane" in the Witten / Kontsevich brane catalog
requires further matched-conventions verification. The off-diagonal
mixed-parity Dirichlet brane realization is consistent with
Etingof–Ostrik 2004 finite tensor categories but the rigorous
construction within the manuscript's local mixed model is Phase-5
work (cross-walks to G5 frontier).

---

## §6. (B.6) p(N) brane species — no standard topological-string
brane realization

### §6.1 The (A2') failure

p(N) preserves an **odd** symmetric bilinear form on $\C^{N|N}$
(Cheng–Wang §1.1.5). The G3-M2 §2 verdict establishes that there is
**no even non-degenerate ad-invariant supersymmetric bilinear form
on p(N)**. The (A5) parametrix construction
$\Delta_{\mathrm{sK}}=\sum_a(-1)^{|a|}T^aT_a$ requires an even
non-degenerate dual basis under an even non-degenerate form — this
fails on p(N).

The Witten / Boundary lens reads this as: **p(N) does not realize
any standard topological-string brane species.** The reasoning:

* In Witten 1992 *Mirror manifolds and topological field theory*,
  the A-brane and B-brane structures rely on **even** (ungraded)
  bilinear forms (the Kähler form on the symplectic side, the
  holomorphic top form on the complex side). The p(N) odd
  symmetric form has no analog in the Witten 1992 framework.
* In Kontsevich 1994 *Homological algebra of mirror symmetry*, the
  Fukaya category and the derived category of coherent sheaves both
  take values in **even-graded** Hom complexes (with Maslov shift
  in the Fukaya case, but always even-totaled grading). The p(N)
  odd-graded bilinear form is incompatible.
* In Witten 1998 *D-branes and K-theory*, the K-theory pairing is
  a $\Z/2$-graded but even-cocycle pairing. The p(N) odd cocycle
  has no K-theory analog.

### §6.2 Could an orientifold construction save p(N)?

**Att-2 from prompt.** Orientifolds quotient by an involution that
preserves the brane structure but flips orientation. Could an
orientifold variant of p(N) admit a brane species?

**Detailed analysis.** Orientifold projections in the Witten /
Kontsevich frameworks preserve the **even** bilinear form by
combining a $\Z/2$ involution with a sign-flip of the form. This
preserves (A5) parity-equivariance because the involution commutes
with the parity operator (it is itself parity-respecting).

For p(N), the natural orientifold candidate is: combine the periplectic
$\Z/2$ involution (swapping even and odd parts of $\C^{N|N}$) with
a sign-flip of the odd symmetric form. This produces an *even*
form on the orientifold quotient — but the quotient is not p(N)
itself; it is a *different* algebra (closer to gl(N|N) modulo a
$\Z/2$).

**Crucial obstruction.** The (A5) parity-equivariance of the W30
heat-kernel construction requires the parametrix to commute with
the parity operator. The orientifold $\Z/2$ involution **swaps**
parity sectors (it interchanges even and odd field content). So
the parametrix on the orientifold quotient satisfies
$\sigma\Delta\sigma^{-1}=\sigma\Delta\sigma^{-1}$ where $\sigma$ is
the orientifold involution; for this to commute with the parity
operator $P$, one needs $[\sigma, P]=0$.

In the periplectic case, $\sigma$ is the **parity-swap**
$\sigma=\diag(0,I_N;I_N,0)$ (a permutation of the $\C^{N|N}$ basis),
and $P=\diag(I_N,-I_N)$. Direct computation:
\[
   \sigma P \sigma^{-1}=\diag(-I_N,I_N)=-P.
\]
**The orientifold involution $\sigma$ anticommutes with the parity
operator.** So the parametrix on the orientifold quotient does not
commute with the parity operator — **(A5) fails on the orientifold**.

This **breaks the (A5) parity-equivariance** in our framework. The
orientifold attempt produces a "parametrix" that is anti-parity-
equivariant, requiring a signed (A5)' analogous to the q(N) (A5)^otr
case, but with a different signing structure (one tied to the
orientifold $\sigma$ rather than the queer $J$).

**Verdict on Att-2.** Orientifolds **do not** preserve the (A5)
parity-equivariance in our framework on p(N). Any p(N)-orientifold
construction would require a separate parity-equivariance
admissibility class, parallel to (A5)^otr but distinct from it.

### §6.3 The Coulembier 2018 periplectic-Brauer route

A non-standard route that has been studied: Coulembier 2018
*Periplectic Brauer algebras* characterizes the centre of $U(\mathfrak p(N))$
via the periplectic Brauer algebra (the odd analog of the Brauer
algebra). This is a **representation-theoretic** discharge route, not
a brane-species realization.

The Coulembier framework would identify p(N)-modules as objects in
a certain finite tensor category (Etingof–Ostrik 2004 generalizes).
Such modules might be assigned **non-standard** boundary conditions
(parastate-like, similar to the q(N) otr-brane but distinct), but
this is **not** a standard A/B-brane in the Witten / Kontsevich
sense, and it lies in Phase-5 territory.

### §6.4 Verdict on (B.6)

**Verdict.** p(N) **does not realize any standard topological-string
brane species** in the Witten 1988 / Witten 1992 / Kontsevich 1994
frameworks. The fundamental obstruction is the **absence of an even
non-degenerate ad-invariant supersymmetric bilinear form** on p(N)
(G3-M2 §2.3 / Cheng–Wang §1.1.5 Prop. 1.34), which precludes the
A/B-brane pairing structure used by the standard frameworks.

**Orientifold attempt fails (A5)**: the periplectic orientifold
involution $\sigma$ anticommutes with the parity operator $P$, so
the orientifold parametrix violates the unsigned (A5)
parity-equivariance condition. Any p(N)-orientifold construction
would require a new admissibility class.

**Non-standard Coulembier 2018 / Etingof–Ostrik 2004 representation-
theoretic route** exists in principle but is Phase-5 territory and
does not produce a standard brane species.

**Confidence.** High (no-go). The (A2') failure is structural and
not regulator-class-dependent; the orientifold attempt has a
provable (A5) obstruction; and the Coulembier route, while
mathematically valid, does not produce a brane species in the
standard topological-string framework.

---

## §7. (B.7) sl(M|N), M≠N — net D-brane charge $\hbar(M-N)$

### §7.1 The non-cancelling brane charge

sl(M|N) for $M\neq N$ has $\Str(I)=M-N\neq 0$. The W22-T1+T2 chain-level
contraction yields the QME obstruction class
$[\hbar(M-N)\bar c]\neq 0$, which is the **active anomaly inflow**.

The Witten lens reads $\hbar(M-N)$ as a **net D-brane charge**:
the Chan–Paton bundle $\C^{M|N}$ has $M$ branes and $N$ anti-branes,
giving net charge $M-N$ in $K^0(\mathrm{point})\cong\Z$. This is the
**failure mode** of brane-anti-brane cancellation (Sen 1998 / Witten
1998): when the K-theory class is non-zero, the brane stack carries
a non-zero net charge that contributes to the anomaly inflow.

### §7.2 Cohomological classification

The brane charge $\hbar(M-N)$ is classified cohomologically:
* **K-theory class:** $[\C^{M|N}]\in K^0(\mathrm{point})\cong\Z$,
  represented by the integer $M-N$.
* **Lie 2-cohomology class:** $\hbar(M-N)[\bar c]\in
  H^2_{\mathrm{Lie}}(\bar A,\C)_{\bar 0}$, the U(1)-center anomaly
  with non-zero coefficient.
* **BV obstruction class:** $\mathrm{Ob}_{\mathrm{sc}}=\hbar(M-N)
  \omega(f,g)\int_\R a(t)b(t)\gamma_{\mathbf 1}(t)\,dt\in
  \mathcal O_{\mathrm{loc}}(\mathcal E_w)_{\bar 0}$, non-trivial
  on the brane probe.

### §7.3 Anomaly inflow on $\R^2\times\C^2$

The manuscript's local mixed model $\R^2\times\C^2$ has:
* Topological direction $\R^2$ (the brane line $\R\times p$ extended
  to a thickened topological factor);
* Holomorphic direction $\C^2$ (the formal symplectic disk).

The brane charge $\hbar(M-N)$ is **localized on the brane line**
$\R\times p$, and produces an anomaly inflow from the bulk (the
$\R^2\times\C^2$ closed-string sector) to the boundary (the
brane-line open-string sector). The W22 chain-level argument
verifies this: the QME obstruction is precisely the bulk-to-boundary
anomaly current.

**Cross-walk to Witten 1998 K-theory anomaly.** Witten 1998 §3.3
records the anomaly inflow for D-branes with non-zero K-theory
class as a Wess–Zumino term on the brane worldvolume, with
coefficient given by the K-theory pairing. The manuscript's
$\hbar(M-N)$ is the local-Hamiltonian analog of this Wess–Zumino
coefficient, on the formal local model $\R\times p$.

### §7.4 Verdict on (B.7)

**Verdict.** sl(M|N) for $M\neq N$ realizes a **brane stack with
net D-brane charge $M-N$**, manifesting as the active QME obstruction
$\hbar(M-N)[\bar c]$ on the manuscript's local model. The brane
charge is cohomologically classified by:
* K-theory class $M-N\in K^0(\mathrm{point})\cong\Z$;
* Lie 2-cohomology class $\hbar(M-N)[\bar c]\in
  H^2_{\mathrm{Lie}}(\bar A,\C)_{\bar 0}$;
* BV obstruction class on the brane line.

The anomaly inflow on $\R^2\times\C^2$ is the local-Hamiltonian
analog of the Witten 1998 D-brane Wess–Zumino term, with the
brane line $\R\times p$ as the worldvolume.

**Confidence.** High. The Witten 1998 K-theory characterization is
verbatim; the manuscript's W22-T1+T2 chain-level argument is the
explicit derivation of this anomaly inflow on the local model.

---

## §8. (B.8) Cross-walk to G4-M3 super-W_3 vanishing at M=N

### §8.1 The spin-tower truncation question

P4-EXEC-G4-M3 (lines 564–680) establishes that the super-W_3
on osp(2N|2N) at the **balanced** configuration $M=N$ has spin-3
cocycle class **zero** by the chain-level argument:
$[c^{(3,\mathrm{osp})}]\propto\hbar\cdot\Str(I)=0$.

This is in contrast to the bosonic spin-3 cocycle on
$W_{1+\infty}(\epsilon_1,\epsilon_2)$, which is *non-zero* at the
rebasing $\hbar^2=\epsilon_1\epsilon_2,\lambda=1$:
$[c^{(3)}]=2[\omega^{(3)}]$ (Costello unit).

The brane-species lens asks: **physically, why does the spin-tower
truncate at the orthosymplectic balance $M=N$, and what brane
condition does this correspond to?**

### §8.2 The SYZ-self-dual O-brane spin-tower truncation

The orthosymplectic balanced configuration $M=N$ is precisely the
configuration where the osp(2N|2N) brane species is **SYZ-self-dual**
(B.3). Under SYZ self-duality:
* The brane stack is fixed by the axis swap $z_1\leftrightarrow z_2$;
* The orthosymplectic Chan–Paton bundle is self-conjugate;
* The K-theory class is zero (orientifold cancellation).

**Why does the spin-tower truncate?** The spin-$s$ generators
$J^{(s)}(z)$ in $W_{1+\infty}(\epsilon_1,\epsilon_2)$ are **not all
SYZ-self-dual** at generic $(\epsilon_1,\epsilon_2)$. At the balanced
configuration, the SYZ self-duality forces a *truncation*:
* Spin-1 (Heisenberg) is SYZ-symmetric;
* Spin-2 (Virasoro) is forgotten by the Bousfield localisation
  (`tau_h`) anyway;
* Spin-$s$ for $s\geq 3$: the brane-stack self-conjugacy under
  axis swap forces the spin-tower contribution to **cancel** in
  pairs (via the orthosymplectic supertrace), giving zero net
  spin-$s$ cocycle at $M=N$.

This is the **physical mechanism** for the spin-tower truncation
identified as Interpretation A in G4-M3 §5.4: it is **not** ad hoc; it is
forced by the SYZ-self-dual O-brane condition.

### §8.3 Brane condition for spin-tower truncation

**The brane condition is: the brane stack is SYZ-self-dual, i.e.,
the Chan–Paton group is orthosymplectic, the K-theory class is
zero, and the spin-tower contributions cancel pairwise under the
axis swap.**

This is the brane-side translation of the orthosymplectic balanced
configuration $M=N$:
* Algebraic:  $\Str_{\mathrm{osp}(2N|2N)}(I)=0$;
* Brane-physical: SYZ-self-dual O-brane with vanishing K-theory class;
* Cohomological: $[c^{(s,\mathrm{osp})}]=0$ for all $s\geq 1$ at
  $M=N$.

### §8.4 Cross-link to W3-W31-T2 topological-twist conjecture

W3-W31-T2 (W31 §4.4) conjectures that a regularised double
holomorphic-twist limit of the CGW boundary VOA recovers the
manuscript's $[\bar c]$. The G4-M3 §5.4 Interpretation A says this
requires a *spin-tower truncation* killing $J^{(s)}$ for $s\geq 2$.
The brane condition identified here is **the precise truncation
mechanism**: the SYZ-self-dual O-brane structure on osp(2N|2N) at
$M=N$ truncates the spin-tower automatically by orthosymplectic
supertrace cancellation.

**This is a non-trivial physical mechanism for W3-W31-T2.** It says
the topological twist of the CGW boundary VOA is realized when the
brane species is the orthosymplectic SYZ-self-dual O-brane — the
super-extension of the manuscript's bosonic gl-brane to osp.

### §8.5 Verdict on (B.8)

**Verdict.** The G4-M3 super-W_3 vanishing at $M=N$ corresponds to
the **SYZ-self-dual O-brane brane condition** on osp(2N|2N): under
self-duality, the orthosymplectic Chan–Paton structure forces
spin-tower contributions to cancel pairwise via supertrace,
truncating the spin-tower at every level $s\geq 1$. This is the
brane-physical mechanism for the W3-W31-T2 topological-twist
conjecture's spin-tower truncation, identified as Interpretation A in
G4-M3 §5.4.

**Confidence.** Medium. The SYZ-self-dual / spin-tower-truncation
correspondence is structurally clean (orthosymplectic supertrace
cancellation at $M=N$ is rigorous in P4-EXEC-G3-T-A1; the spin-tower
extension follows by the chain-level argument extension of W22-T2
to the spin-3+ generators, which is sketched in G4-M3 §6 but not
fully closed). The cross-link to W3-W31-T2 requires the CGW
PDF inscription and a matched-conventions verification.

---

## §9. Mirror-symmetry / duality cross-walk between Str-branes and otr-branes

### §9.1 The Str-otr duality on q(N)

The two-supertrace structure $(\Str,\mathrm{otr})$ on q(N) defines
**two distinct boundary evaluations** on the same q(N) brane probe:
* $\partial_{\mathrm{bb},N}^{\Str}: f\mapsto\Str\,f(\phi_1,\phi_2)$;
* $\partial_{\mathrm{bb},N}^{\mathrm{otr}}: f\mapsto\mathrm{otr}\,f(\phi_1,\phi_2)$.

The Witten lens identifies a candidate duality between the Str-channel
and the otr-channel: **mirror symmetry on q(N)**. The conjecture is:

> **Conjecture (q-mirror).** On the q(N) brane probe, mirror
> symmetry exchanges the Str-brane and the otr-brane; equivalently,
> mirror symmetry exchanges the bosonic boundary evaluation
> $\partial^{\Str}$ with the parastatistic boundary evaluation
> $\partial^{\mathrm{otr}}$.

### §9.2 Att-3: Mirror symmetry exchanges A-branes and B-branes

**Att-3 from prompt.** Mirror symmetry exchanges A-branes and
B-branes; does it exchange the standard branes (Str-discharge) with
the queer branes (otr-Theorem G^otr)?

**Detailed analysis.** Mirror symmetry in Kontsevich 1994 *Homological
algebra of mirror symmetry* exchanges:
* The Fukaya category of A-branes (Lagrangian submanifolds with
  graded local systems) on $X$;
* The derived category of B-branes (coherent sheaves) on the mirror
  $\hat X$.

For the manuscript's local mixed model, the analog is:
* **A-brane direction**: the topological / locally constant factor
  $\R^2$ (de Rham / Floer-like);
* **B-brane direction**: the formal-holomorphic factor $\C^2$
  (Dolbeault / coherent-sheaf-like).

The mixed brane is *both* A-side along $\R^2$ and B-side along $\C^2$
(`def:local-th-string`).

**On q(N)**, the Str-channel and otr-channel are not, naively,
A-side / B-side images of each other. Both channels live on the
same mixed brane (topological-along-$\R$, holomorphic-along-$\C^2$).
The exchange is *along the parity direction*, not along the
A/B-direction.

**Refined conjecture.** Mirror symmetry on q(N) exchanges the
Str-brane and otr-brane via a **parity-mirror symmetry**, not
(A↔B)-mirror symmetry. The parity-mirror is realized by conjugation
with the queer central element $J$ (§5.2), which is itself a
parity-swap automorphism. This is a **new variant** of mirror
symmetry, parallel to but distinct from the Kontsevich 1994
A/B-mirror.

**Convergence with Sergeev 1985 duality.** Sergeev 1985
*Tensor algebra of identity rep as Gl(n|m) and Q(n) module* (Mat.
Sb. 51) establishes the **q-duality** between $\mathfrak q(N)$ and
the Hecke–Clifford superalgebra $\mathcal{HC}_n$, parallel to the
Schur–Weyl duality between $\mathfrak{gl}_N$ and $S_n$. The
parity-mirror conjectured here is the **brane-side shadow** of this
q-duality: the Str-brane is the analog of the standard Schur–Weyl
brane, the otr-brane is the analog of the Hecke–Clifford brane.

### §9.3 Status of the parity-mirror conjecture

**Honest epistemic status.** The parity-mirror is a *conjecture*,
not a theorem. The Witten / Boundary lens supports it (the
two-supertrace structure naturally yields two boundary evaluations,
related by conjugation with $J$), but a rigorous statement and
proof require:
* A precise definition of "mirror symmetry" on the local mixed
  model (the manuscript's framework does not include a global
  mirror symmetry; SYZ T-duality on the formal disk is trivial);
* A matched-conventions verification with Cheng–Wang 2012 §6
  finite-tensor-category structure on q(N)-modules;
* A check against Sergeev 1985 q-duality at the brane-stack level.

This is **Phase-5 work**, parallel to the Theorem G^otr inscription.

### §9.4 Verdict on §9

**Verdict.** Mirror symmetry on q(N) exchanges the Str-brane and
otr-brane via a **parity-mirror symmetry** realized by conjugation
with the queer central element $J$. This is **not** the Kontsevich
1994 A/B-mirror (which exchanges A-branes and B-branes along
A/B-axis), but a **parity-axis** mirror parallel to it. The
brane-side shadow of Sergeev 1985 q-duality.

The conjecture is **Phase-5 frontier**, requiring matched-conventions
verification and a precise mirror-symmetry definition on the local
mixed model. Tabled as **R-P4-EXEC-Brane-Q-mirror-01**.

**Confidence.** Medium-low. The parity-mirror is structurally clean
(both channels use the same q(N) source, related by conjugation
with $J$), but the mirror-symmetry framework on the local mixed
model is not fully developed in the manuscript. Cross-walk to
Cheng–Wang and Sergeev requires Phase-5 inscription and
verification.

---

## §10. Anti-attack scan responses

### §10.1 (Att-1) CGW-specific brane realization on q(N)

**Attack.** Does the Costello–Gaiotto–Williams 5d twisted-M-theory
framework (CGW arXiv:2007.09497) realize a *specific brane* with
the q(N) two-supertrace structure?

**Response.** CGW 2007.09497 constructs **bulk + boundary VOA + surface
defect** structure for 5d HT-CS on $\R\times\C^2$. The boundary VOA
is $W_{1+\infty}(\epsilon_1,\epsilon_2)$, and the surface defects
are holomorphic surface defects on $\R\times\{z_2=0\}$ (W31 §1.1
quotation).

**Does CGW realize a queer (otr-channel) defect?** Within the bosonic
$W_{1+\infty}$ framework, no — the CGW boundary VOA is bosonic.
However:
* CGW 2007.09497 §5–6 (according to W31 §1.1 interpretation) does
  construct **fermionic** defect spectra in some cases;
* The orthosymplectic super-extension of $W_{1+\infty}$, namely
  the super-$W_{1+\infty}$ on osp(2N|2N) (per G4-M3 §6), would
  realize the **Str-channel** of a super-q(2N|2N) defect, but
  not the otr-channel separately.

**Conclusion on Att-1.** CGW 2007.09497 does **not** explicitly
realize the q(N) two-supertrace doubled brane in the form named in
this audit. The CGW framework is bosonic at its core; the queer /
otr-channel structure is a *new* observation not yet matched to a
CGW defect. This is consistent with W31's verdict that the CGW
side is bosonic-only and the queer extensions are
parastatistic-only.

**Discharge.** Att-1 is answered with the **explicit gap statement**:
the otr-channel realization on a CGW defect is an **open question**
(R-P4-EXEC-Brane-CGW-otr-01), parallel to but distinct from the
manuscript's Theorem G^otr inscription, and requires CGW PDF
inscription plus a matched-conventions verification on q(N).

### §10.2 (Att-2) Orientifold preservation of (A5) parity-equivariance on p(N)

**Attack.** The G3-M2 failure on p(N) might be circumventable via
an orientifold construction; identify whether orientifolds preserve
(A5) parity-equivariance.

**Response.** §6.2 above. The periplectic orientifold involution
$\sigma=\diag(0,I_N;I_N,0)$ (the parity-swap of $\C^{N|N}$
basis) **anticommutes** with the parity operator
$P=\diag(I_N,-I_N)$:
\[
   \sigma P \sigma^{-1}=-P.
\]
This is the precise (A5) violation: the orientifold parametrix on
the p(N)-orientifold is *anti-parity-equivariant* under the standard
parity operator, requiring a signed (A5)' admissibility class.

**Distinction from q(N) (A5)^otr.** The q(N) signed (A5)^otr is
generated by conjugation with the queer central element $J$
(odd-parity, in $\mathfrak q(N)_{\bar 1}$); the p(N) signed (A5)'
attempt is generated by the orientifold involution $\sigma$
(a $\Z/2$-permutation of the basis, **not** in any natural Lie
superalgebra direction). These are **different algebraic objects**,
so the (A5) violation on p(N) is not the same as on q(N), and the
two cannot be unified into a single signed admissibility class.

**Conclusion on Att-2.** Orientifolds **do not** preserve unsigned
(A5) on p(N); the orientifold attempt fails by a different
mechanism than the q(N) (A5)^otr. Both fail unsigned (A5), but
in algebraically distinct ways.

**Discharge.** Att-2 is answered with the **explicit (A5) violation
calculation**: the periplectic orientifold $\sigma$ anticommutes
with the parity $P$, so the orientifold parametrix violates unsigned
(A5). Any p(N)-orientifold construction would require a new
signed admissibility class, distinct from the q(N) (A5)^otr.

### §10.3 (Att-3) Mirror symmetry exchanges Str-branes and otr-branes

**Attack.** Does mirror symmetry exchange the standard branes
(Str-discharge) with the queer branes (otr-Theorem G^otr)?

**Response.** §9.2 above. **Yes, in a parity-mirror sense**, but
**not in the Kontsevich 1994 A/B-mirror sense**:
* Kontsevich 1994 A/B-mirror exchanges A-branes (Lagrangian) and
  B-branes (coherent sheaves) along the A/B-axis (topological vs
  holomorphic).
* The Str / otr exchange on q(N) is along the **parity axis**
  (even / odd parity sectors of the BV cohomology), realized by
  conjugation with the queer central element $J$.

The **q-duality of Sergeev 1985** is the algebraic shadow of this
parity-mirror: it exchanges the standard $\mathfrak q(N)$-rep
category with the Hecke–Clifford category $\mathcal{HC}_n$.

**Conclusion on Att-3.** The parity-mirror is conjecturally realized
by Sergeev 1985 q-duality at the algebraic level; its brane-stack
interpretation is **Phase-5 frontier**, not closed at this audit
level. Tabled as R-P4-EXEC-Brane-Q-mirror-01.

**Discharge.** Att-3 is answered with the **structural clarification**:
the Str ↔ otr exchange is a parity-mirror, not an A/B-mirror. The
parity-mirror is real (algebraically, Sergeev 1985), but its
brane-stack realization is Phase-5 work.

### §10.4 (Att-4) Brane-species typology and the open-closed comparison map

**Attack.** Does the brane-species typology encode the dimension
constraints for the open-closed comparison map in the manuscript's
main statement?

**Response.** The manuscript's main statement (`thm:bulk-boundary`,
referenced via `lem:omega-cocycle` and `thm:u1-center-anomaly-open`)
records the open-closed comparison map for the bosonic $\mathfrak{gl}_N$
brane species. The brane-species typology established here
**determines the dimension of the comparison map's target** for
each super-Lie source:

| Family | Comparison map target dimension | Mechanism |
|---|---|---|
| gl(N\|N) | 1 (single Str-channel, single $[\bar c]$) | standard |
| osp(2N\|2N) | 1 (Str-channel, SYZ-self-dual) | standard with self-duality |
| psl(N\|N) | 1 (via lift, central projection trivial) | standard via lift |
| q(N) | **2** (Str + otr channels, two classes $[\bar c]\oplus[\bar c]^{\mathrm{otr}}$) | **doubled** |
| p(N) | 0 (no comparison map; (A2') failure) | absent |
| sl(M\|N), M≠N | 1 with non-zero coefficient $\hbar(M-N)$ | active anomaly |

**Conclusion on Att-4.** Yes, the brane-species typology **does**
encode the dimension constraints. The q(N) entry is the **only
non-standard** entry: it carries a **doubled** comparison map,
producing a 2-dimensional target. This is the brane-side shadow of
Theorem G^otr's two-supertrace independence (§3.4 of inscription
proposal).

**Discharge.** Att-4 is answered with the **table** above. The
typology is consistent with the manuscript's open-closed comparison
map at every tier; the only structural extension required is the
q(N) doubled-brane → 2-dimensional comparison map target, which
matches the Theorem G^otr inscription proposal.

---

## §11. Residuals + deciding evidence

### §11.1 Residuals introduced by this audit

* **R-P4-EXEC-Brane-Q-mirror-01** (severity 3, sharpening). The
  parity-mirror conjecture exchanging Str-branes and otr-branes on
  q(N) (§9). Deciding evidence: matched-conventions verification
  with Sergeev 1985 q-duality and Cheng–Wang Ch. 6
  finite-tensor-category structure; precise definition of mirror
  symmetry on the local mixed model.

* **R-P4-EXEC-Brane-CGW-otr-01** (severity 3, inscription). The
  realization of the q(N) otr-brane on a CGW 2007.09497 boundary
  defect (§10 Att-1). Deciding evidence: CGW PDF inscription per
  W31 §2.1; explicit identification of a fermionic / parastatistic
  defect in CGW §5–6 that matches the otr-channel structure.

* **R-P4-EXEC-Brane-osp-SYZ-02** (severity 3, sharpening). The
  SYZ-self-dual O-brane identification on osp(2N|2N) at $M=N$
  (§3, §8). Deciding evidence: SYZ T-duality realization on the
  formal $\C^2$ disk (trivially the projection $\C^2\to\R^2$); precise
  cross-check with W23 σ_swap mirror; cohomological verification
  that the orthosymplectic Chan–Paton bundle is self-conjugate in
  the brane category.

* **R-P4-EXEC-Brane-p-orientifold-03** (severity 4, no-go
  hardening). The (A5) violation on the periplectic orientifold
  (§6.2, §10 Att-2). Deciding evidence: this is essentially closed
  by direct computation $\sigma P\sigma^{-1}=-P$; no further
  evidence required, but the no-go could be hardened by a precise
  Witten 1992 / Aspinwall et al. 2009 cross-check.

* **R-P4-EXEC-Brane-spin-truncation-04** (severity 3, sharpening).
  The SYZ-self-dual O-brane spin-tower truncation mechanism (§8).
  Deciding evidence: chain-level extension of W22-T2 / G4-M3 to
  spin-3+ generators with explicit super-Casimir computation; CGW
  PDF inscription for the bosonic spin-tower comparison.

### §11.2 Phase-4 closure status

This audit produces:
* **Closed in this audit** (no further evidence required at Phase-4
  level): the three-tier typology (§0); per-family identification
  (§1); gl(N|N) B-brane species (§2); psl central-projected D-brane
  (§4); p(N) no-go via (A5) violation on orientifold (§6, §10 Att-2);
  sl(M|N) M≠N net D-brane charge (§7).

* **Phase-5 frontier** (residuals above): osp SYZ-self-dual O-brane
  rigorously verified; q(N) parity-mirror conjecture; CGW otr-brane
  realization; spin-tower truncation mechanism rigor.

### §11.3 Inscription readiness

**No new manuscript inscription is required by this audit.** The
brane-species typology is consistent with existing manuscript
content (`def:local-th-string` mixed brane; `thm:u1-center-anomaly-open`
U(1)-center anomaly; `thm:bulk-boundary` open-closed comparison
map). The Phase-5 frontier candidates (Q-mirror, CGW-otr,
SYZ-self-dual rigour, spin-truncation rigour) are tabled as
residuals for future Phase-5 inscription proposals, parallel to
the Theorem G^otr inscription proposal.

---

## §12. Cross-volume firewall implications for Vol III calabi-yau-quantum-groups

### §12.1 The standing firewall posture

Per `CLAUDE.md`, the cross-volume firewall states that "no statement
in this repository implies a compact CY$_3$, Vol III, or global BCOV
theorem without a separate matched-conventions proof." All physical
and brane-stack content in this audit is **on the formal local
mixed model** $\R^2\times\C^2$, **not** on a compact CY$_3$.

### §12.2 What this audit does NOT imply about Vol III

This audit does **not** establish:
* Any global compact-CY$_3$ statement about brane categories;
* Any Vol III BKM / Igusa modular-form statement;
* Any global SYZ T-duality statement (only formal-local);
* Any compact-CY$_3$ Witten 1998 K-theory statement;
* Any compact-CY$_3$ Kontsevich 1994 mirror-symmetry statement.

All physical interpretations in this audit are **local**
(formal-disk in $\C^2$, locally-constant in $\R^2$) and follow the
manuscript's own footprint.

### §12.3 What this audit DOES imply for Vol III as context

The audit establishes:
* The classical super-Lie families catalogued in G3-M2 each
  correspond to a formal-local brane species, with three tiers
  (standard / parallel-anomaly / outright-failure);
* The q(N) two-supertrace doubled brane is the **algebraic shadow**
  of a parastatistic open-closed duality, parallel to the
  Sergeev 1985 q-duality and Cheng–Wang 2012 Ch. 6 finite-tensor-
  category structure;
* The p(N) no-go is structural (no even ad-invariant form, no
  orientifold rescue);
* The sl(M|N) M≠N residue is the local-Hamiltonian shadow of a
  Witten 1998 K-theory class.

These are **formal-local** statements, **not** Vol III statements.
They provide **convention-checking interface** with Vol III
constructions where the queer / parastatistic / orthosymplectic
structures may appear (e.g., Cheng–Wang Ch. 6 for chiral algebras
on degenerate CY$_3$).

**Cross-volume firewall preserved.** The audit makes no Vol III
claim; it provides formal-local typology and brane-species
identification that may inform future Vol III matched-conventions
work. The boundary remains rigid: no CY$_3$ compactness, no global
BCOV, no global modular-form statement.

### §12.4 Cross-walk to Igusa modular-form frontier

Per `CLAUDE.md` modular-form frontier: "generating functions in
topological-string theory motivate comparison with the Igusa cusp
form $\Delta_5$ construction in `~/igusa-cusp-form` via the
Borcherds / BKM route. This is a heuristic and convention-checking
bridge here."

The brane-species typology established here is **silent** on the
Igusa modular-form frontier. The Vol III BKM / Igusa route would
require global compact-CY$_3$ context, which this audit does not
provide. The **only** cross-link is via convention-checking: the
super-Lie family typology provides candidate symmetry algebras for
chiral algebras on Vol III, but no Igusa-form statement follows.

---

## §13. Summary: load-bearing verdicts

* **Three-tier typology established.** Standard discharge (gl, osp,
  psl via lift); parallel anomaly (q(N), two-channel); outright
  failure (p, sl(M|N) M≠N).
* **gl(N|N) is a B-brane stack.** Topological-along-$\R$,
  Dolbeault-along-$\C^2$, supersymmetric Chan–Paton bundle, K-theory
  class zero by Witten 1998 cancellation.
* **osp(2N|2N) is a SYZ-self-dual O-brane.** Orthosymplectic
  Chan–Paton, self-conjugate under axis swap, K-theory class zero
  by orthosymplectic supertrace.
* **psl(N|N) is a central-projected D-brane.** Lift to gl(N|N) plus
  $\C\cdot I$ central scalar gauge-fixing.
* **q(N) is a doubled (Str-brane, otr-brane) pair.** Off-diagonal
  mixed-parity Dirichlet brane realization for otr-brane, related
  to Str-brane by parity-twist via $J$. Independent residue
  $\hbar N[\bar c]^{\mathrm{otr}}$ is the otr-brane charge anomaly.
* **p(N) admits no standard brane realization.** Orientifold
  attempt explicitly fails (A5) via $\sigma P\sigma^{-1}=-P$.
* **sl(M|N) M≠N carries net K-theory class $M-N$.** Active anomaly
  inflow on $\R^2\times\C^2$ matching Witten 1998.
* **Spin-tower truncation at $M=N$** corresponds to SYZ-self-dual
  O-brane condition; orthosymplectic supertrace cancellation
  truncates spin-tower at every level.
* **Mirror symmetry on q(N)** is parity-mirror (Sergeev 1985
  q-duality shadow), not Kontsevich A/B-mirror; Phase-5 frontier.
* **Open-closed comparison map** dimension is 1 for tier (I), 2
  for tier (II) q(N), 0 for tier (III) p(N), 1 with active
  anomaly for tier (III) sl(M|N).

**Phase-4 closure.** This audit produces the three-tier brane-species
typology consistent with the G3-M2 strategic boundary, with five
named residuals tabled for Phase-5 work. **No manuscript inscription
required at this level.** The audit is proposal-only and respects
the cross-volume firewall.

---

**End of P4-EXEC-Brane-Species-Audit-2026-04-28.**
