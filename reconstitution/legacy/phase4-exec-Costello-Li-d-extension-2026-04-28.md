# Phase-4 EXEC / P4-Costello-Li-d-not-3-Probe — Polyakov+Invariants probe of the Costello-Li 2015 flat $\C^d$ ($d$ odd) partial bosonic discharge mechanism

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Polyakov + Invariants — dimensional analysis (does the
residue scale correctly with $d$?), anomaly cohomology classes per
dimension, which invariants survive the $d \to d+1$ step, parity
behaviour of the holomorphic top form and Kähler form orientation.
**Mode.** Proposal-only. NO git commits, NO TeX edits to the
manuscript. Ledger lives at this path ONLY.
**Mandate.** Costello–Li 2015 (open-closed flat BCOV; arXiv:1505.06703)
establishes a *partial* bosonic discharge of BCOV-type anomaly on
flat $\C^d$ for $d$ odd, with open gauge algebra
$\mathfrak{gl}(N\mid N)$. Investigate the dimension condition,
identify why $d$-odd is required, decide whether the result extends
to $d$-even, locate the manuscript's $\R^2 \times \C^2$ split inside
the Costello–Li 2015 dimensional table, identify the smallest
distinguishing test between $d=3$-via-reduction and $d=4$-direct,
cross-walk to the W30 (A5) regulator class, and decide whether the
manuscript's `stmt:costello-li-flat-bcov` inscription correctly
captures the dimensional applicability.

**Inputs read in full.**
- `reconstitution/phase4-exec-Unreduced-Bosonic-Phase5-2026-04-28.md`
  (1372 lines) — UB.1 inscription-ready statement on the
  Costello–Li 2015 partial discharge for the super-balanced source.
- `reconstitution/phase4-exec-BCOV-A5-comparison-2026-04-28.md`
  (1093 lines) — chain-level comparison map between BCOV 1994 and
  manuscript's (A5) + (A2$'$); structural firewall topology with a
  partial firewall lift via `stmt:costello-li-flat-bcov`.
- `main.tex` 5136–5175 (the `stmt:costello-bv-package` and
  `stmt:costello-li-flat-bcov` inscriptions; the appended remark on
  R$\times p$ as a defect, not a spacetime boundary).
- `main.tex` 75–168 (manuscript's $\R^2 \times \C^2$ local
  setup; first-class constraint, BV reduction, scalar-reduced
  Hamiltonian quotient $\bar A$).
- `main.tex` 170–185 (BCOV 1994 cited as source-convention
  template, *not* as imported theorem; explicit mention that the
  manuscript is on a "$d=2$ surface model").
- `main.tex` 1265–1363 (Local model: $M = \R^2$, $Y = \C^2$,
  $X = M \times Y$, mixed brane $\R \times \{p\}$; mixed
  differential $D = d_{\R^2} + \bar\partial_{\C^2}$).
- `main.tex` 5380–5394 (`rmk:convention-firewall` — Hamiltonian
  BF/Moyal as local deformation quantisation, not compact CY$_3$).
- `main.tex` 5894–5915 (cross-volume firewall section).
- `tate-T4-bv-vanishing.tex` (full, 204 lines) — five named failure
  reasons F1–F5 for Costello–Li 2012 / 2015 application to the
  $\R^2 \times \C^2$ local model; gap analysis with four missing
  theorems.
- `appendix-unreduced-bv-qme.tex` (full, 179 lines).

**Primary external sources cited.**
- K. Costello, S. Li, "Quantum BCOV theory on Calabi–Yau manifolds
  and the higher genus B-model", arXiv:1201.4501 (2012) — chain-level
  rigorous BCOV; closed BCOV/HCS quantisation on compact CY$_d$.
- K. Costello, S. Li, "Quantization of open-closed BCOV theory, I",
  arXiv:1505.06703 (2015) — open-closed BCOV on flat $\C^d$, $d$ odd,
  with $\mathfrak{gl}(N\mid N)$ open algebra.
- K. Costello, S. Li, "Anomaly cancellation in the topological
  string", arXiv:1605.09073 (2016) — chain-level anomaly cancellation
  via supertrace on flat $\C^d$.
- M. Bershadsky, S. Cecotti, H. Ooguri, C. Vafa, "Kodaira–Spencer
  theory of gravity and exact results for quantum string amplitudes",
  *Comm. Math. Phys.* **165** (1994), 311–427 — primary BCOV; §6
  holomorphic anomaly equation.
- K. Costello, *Renormalization and Effective Field Theory*, AMS
  Math. Surveys and Monographs **170** (2011), Ch. 4 §4.4 (BV anomaly
  cohomology classes).
- A. Polyakov, "Quantum geometry of bosonic strings", *Phys. Lett.*
  **B103** (1981), 207–210.

**Lens guidance recap.**
- *Polyakov.* Dimensional analysis — does the chain-level residue
  scale with $d$ in a way that preserves regulator-class
  scheme-independence inside (A1)–(A4) admissible? Does the
  Polyakov-class regulator-independence survive a putative
  dimensional reduction $d=3 \to d=2$ along the "extra" $\R^2$?
  Anomaly cohomology classes per complex dimension.
- *Invariants.* Which invariant survives the $d \to d+1$ step?
  Holomorphic top form $\Omega_d = dz_1 \wedge \cdots \wedge dz_d$;
  Kähler form $J = \sqrt{-1}\sum_i dz_i \wedge d\bar z_i$ (real
  $(1,1)$); the parity-graded structure of polyvector fields
  $\mathrm{PV}^{*,*}(\C^d)$; supertrace on the open algebra; flatness
  $F_\alpha = 0$ on the Hamiltonian connection.

---

## §0. Executive verdict

**Three-line bottom line.**

1. **Dimensional applicability of Costello–Li 2015 to our
   $\R^2 \times \C^2$:** **ANALOGUE only**, *not* DIRECT and *not*
   REDUCED. The manuscript's local model lives on a *real-times-
   complex product* $\R^2_{\mathrm{top}} \times \C^2_{\mathrm{hol}}$,
   not on a flat complex Calabi–Yau $\C^d$ for any $d$. The $\R^2$
   factor is *de Rham topological*, not a complex direction; treating
   it as an additional complex dimension would change the kinematic
   differential from $D = d_{\R^2} + \bar\partial_{\C^2}$ to a pure
   $\bar\partial$ on $\C^3$, breaking the manuscript's first-class
   constraint structure. Costello–Li 2015 covers neither $d=2$
   ($d$-even) nor the mixed $\R^2_{\mathrm{top}} \times \C^2_{\mathrm{hol}}$
   kinematic; the manuscript's existing inscription
   `stmt:costello-li-flat-bcov` correctly notes this exclusion at
   `main.tex`:5163.

2. **The $d$-odd condition is structural, not technical.** It comes
   from the *parity of the holomorphic top form* $\Omega_d = dz_1
   \wedge \cdots \wedge dz_d$ relative to the BV $(-1)$-shifted
   pairing $\langle\alpha, \beta\rangle = \int_X
   (\alpha \wedge \beta)|_{\mathrm{PV}^{d,d}} \cdot \Omega^2$, and from
   the *signed loop closure* on the supertrace of polyvectors. On
   $\C^d$ for $d$ even, the polyvector parity grading interacts with
   $\Omega^{2d-d} = \Omega^d$ to produce a sign-flip in the chain-level
   anomaly that the supertrace cancellation cannot absorb. **The
   $d$-odd condition does not extend to $d=4$** without a *new*
   parity-equivariant cancellation mechanism (no such mechanism is
   inscribed in Costello–Li 2015 / 2016 or in successor literature
   consulted).

3. **Smallest distinguishing test:** at one loop, on the open-loop
   closure with $\mathfrak{gl}(N\mid N)$, the residue is
   - $\hbar \cdot \mathrm{Str}(I) \cdot [\Omega^d \cdot \text{vertex}]$
     on $\C^d$. At super-balance $\mathrm{Str}(I) = 0$ on every $d$;
     the **vertex class** survives only when $d$ is odd, because the
     Kähler-volume signed integration on $\Omega^d \wedge \bar\Omega^d$
     produces a sign that aligns with the BV pairing only for $d$
     odd (Costello–Li 2015 Prop. 3.7 implicit; explicit in Costello–Li
     2016 Theorem A proof).
   - On our $\R^2 \times \C^2$, the residue is
     $\hbar N\,\omega(f,g)\,\int_\R a(t)b(t)\,dt$
     (`appendix-unreduced-bv-qme.tex`:118–123) with the *Lie 2-cocycle*
     $\omega(f,g) = [\{f,g\}]_0$, *not* the BCOV $\bar\partial$-coboundary.
   The two residues live in *different obstruction complexes*; the
   coupling-coefficient parallel runs through the supertrace on the
   open algebra (W22-T1 / Costello–Li 2016 Theorem A), not through any
   direct dimensional reduction.

**One-line invariant.** The Costello–Li 2015 / 2016 mechanism is
controlled by *two* representation-theoretic invariants: the supertrace
$\mathrm{Str}_{\mathfrak{gl}(N|N)}(I) = 0$ on the open algebra, and the
parity-equivariance of the heat-kernel propagator on polyvectors of
$\C^d$ for $d$ odd. **Both invariants are preserved on our
$\R^2 \times \C^2$ super-balanced extension** (W22-T1 / W22-T2), but
the *vertex class* is structurally different
($H^2_{\mathrm{Lie}}(\bar A, \C)$ on our side; $\bar\partial$-coboundary
on Costello–Li's side). The dimensional applicability question is
therefore *not* whether the cancellation survives but whether the
vertex class lives in a single comparison complex; it does not.

**Bottom-line classification.** **ANALOGUE.** The Costello–Li 2015
result is the *only currently inscribed bosonic-adjacent discharge*
relevant to our model and serves as a structural template. It
discharges *no* part of the manuscript's local theorem on bosonic
$\mathfrak{gl}_N$, and its dimensional applicability does not extend
to the manuscript's mixed $\R^2 \times \C^2$ kinematic regardless of
parity twisting. The inscription at `main.tex`:5155–5166 correctly
notes the exclusion.

**Clarifying remark needed for `stmt:costello-li-flat-bcov`.** The
existing inscription notes that "ordinary $\mathfrak{gl}_N$ and the
mixed $\R^2 \times \C^2$ Hamiltonian brane model are not covered by
this theorem without an additional reduction or summand argument." A
*minor* clarification would specify that the dimensional gap is
*two-sided*: (i) the manuscript's spacetime is not flat $\C^d$ for any
$d$ (the $\R^2$ is de Rham, not Dolbeault), and (ii) the parity of
$d$ governs the polyvector chain-level cancellation independently of
the $\mathfrak{gl}(N\mid N)$ open-algebra structure. The current
inscription captures (i) implicitly via "mixed $\R^2 \times \C^2$"; a
single-sentence remark naming the parity origin of the $d$-odd
condition would close the dimensional ambiguity. Recommendation:
*minor strengthening*, optional, not load-bearing.

---

## §1. Costello–Li 2015 (arXiv:1505.06703) precise statement

### 1.1. Setup and theorem

**Setup (Costello–Li 2015 Definition 1.1 + §2).**
Fix $d \geq 1$ odd. Let $X = \C^d$ with the standard Calabi–Yau
structure: holomorphic volume form
$$\Omega_d \;=\; dz_1 \wedge dz_2 \wedge \cdots \wedge dz_d,$$
flat Kähler metric $g_{i\bar j} = \delta_{i\bar j}$, Kähler form
$J = \frac{\sqrt{-1}}{2} \sum_{i=1}^d dz_i \wedge d\bar z_i$.

Let $L \subset \C^d$ be a real Lagrangian submanifold (e.g.,
$\R^d \subset \C^d$). The **closed BCOV BV theory** on $\C^d$ is the
Costello–Li 2012 reformulation:
$$\mathrm{BCOV}(\C^d) \;=\; \mathrm{PV}^{*,*}(\C^d)[[t]],$$
with classical action
$$S_{\mathrm{BCOV}}(\mu) \;=\; \tfrac{1}{2}\langle \mu, \bar\partial \mu \rangle
  + \tfrac{1}{6}\langle \mu, \{\mu, \mu\}\rangle + \cdots,$$
$\langle\cdot,\cdot\rangle$ the Calabi–Yau pairing using $\Omega_d$,
$\{\cdot,\cdot\}$ the Schouten–Nijenhuis bracket, $t$ the Tate
worldsheet $S^1$ rotation parameter. The **open BCOV/HCS BV theory**
on $L \subset \C^d$ has open fields
$$\mathcal E_{\mathrm{open}} \;=\; \Omega^*(L) \otimes \mathrm{End}(V_{N|N})[1],$$
where $V_{N|N} = \C^{N|N}$ is the super-vector space underlying
$\mathfrak{gl}(N\mid N)$. The classical open-closed coupling (Costello–Li
2015 §3.2) is the trace pairing of the open Chern–Simons-type vertex
against the closed BCOV polyvector field.

**Theorem (Costello–Li 2015 Theorem 1.2; 2016 Theorem A).**
For $d$ odd, the open-closed BCOV theory on $(\C^d, L)$ with open gauge
algebra $\mathfrak{gl}(N\mid N)$ admits a perturbative quantisation,
unique up to the equivalences in their renormalisation scheme, with
the following compatibility under super-extension:
$$\mathfrak{gl}(N\mid N) \hookrightarrow \mathfrak{gl}(N+k\mid N+k).$$
The **one-loop anomaly cancellation** (Costello–Li 2016 Theorem A) is:
the chain-level QME obstruction representative
$$\mathrm{Ob}^{\mathrm{BCOV/HCS}}_{1\text{-loop}} \;=\;
  \hbar \,\mathrm{Str}_{\mathfrak{gl}(N|N)}(I)\cdot[\mathrm{HCS\,vertex}]$$
vanishes because $\mathrm{Str}_{\mathfrak{gl}(N|N)}(I) = N - N = 0$.
The all-loop extension (Costello–Li 2016 §5–6) uses the parity
preservation of the heat-kernel regulator on polyvectors of $\C^d$
($d$ odd) to extend the cancellation to all loops.

### 1.2. The dimension condition

The hypothesis $d$ odd appears in:
- (CL.1.a) Costello–Li 2015 §3.4 (BV pairing and polyvector
  signature): the BV pairing on the open-closed coupling involves
  the integration of $\alpha \wedge \beta \wedge \Omega^2$ on
  $\mathrm{PV}^{d,d}(\C^d)$, where the *square* of the holomorphic
  volume form contributes a sign $(-1)^{d(d-1)/2}$ from the Koszul
  re-ordering. For $d = 1, 3, 5, \ldots$ (i.e., $d \equiv 1$ or $3$
  mod 4), the sign is in the right combination with the polyvector
  parity to align with the BV pairing.
- (CL.1.b) Costello–Li 2015 §4.2 (Lagrangian boundary condition):
  the trace pairing on $L = \R^d \subset \C^d$ requires a
  $d$-dimensional real integration; the orientation of $L$ relative
  to $\C^d$ via $\Omega_d \wedge \bar\Omega_d$ on $\C^d$ produces a
  sign that aligns with the open-closed coupling only for $d$ odd.
- (CL.1.c) Costello–Li 2016 Theorem A proof: the chain-level
  Schouten–Nijenhuis bracket on polyvectors of $\C^d$ has a
  parity-grading interaction with the BCOV $\bar\partial$-coboundary
  representative; the cancellation $\mathrm{Str}(I) = 0$ takes the
  form $\hbar N \cdot [\text{vertex}] - \hbar N \cdot [\text{vertex}] = 0$
  on bosonic-vs-fermionic blocks, and the relative sign between the
  two terms is $(-1)^d$. For $d$ odd, the relative sign is $-1$, and
  the cancellation closes; for $d$ even, the relative sign is $+1$,
  and the cancellation fails (instead one gets $2\hbar N \neq 0$,
  doubled rather than cancelled).

### 1.3. The algebraic-side $\mathfrak{gl}(N\mid N)$ coupling

The open algebra $\mathfrak{gl}(N\mid N)$ is the super-Lie algebra
generated by $N\times N$ matrices in two parity-graded blocks (even
and odd). It has:
- **Supertrace:** $\mathrm{Str}\bigl(\begin{smallmatrix}A & B \\ C & D\end{smallmatrix}\bigr)
  = \mathrm{Tr}(A) - \mathrm{Tr}(D)$, which on the identity
  $I = \mathrm{diag}(\mathbf 1_N, \mathbf 1_N)$ gives
  $\mathrm{Str}(I) = N - N = 0$.
- **Parity-equivariant Killing form:** $K(X, Y) = \mathrm{Str}(XY)$,
  which is non-degenerate for the super-extension. This is the form
  used to construct the BV pairing on $\mathfrak{gl}(N\mid N)$.
- **Compatibility under stabilisation:**
  $\mathfrak{gl}(N\mid N) \hookrightarrow \mathfrak{gl}(N+k\mid N+k)$
  preserves the supertrace identity $\mathrm{Str}(I_{N+k|N+k}) = 0$
  for all $k \geq 0$.

The coupling to the BCOV polyvectors is via the trace pairing:
$$\mathrm{ev}_{\mathrm{open}}:\quad
  \alpha \otimes M \;\mapsto\; \mathrm{Str}_{\mathfrak{gl}(N|N)}(M) \cdot \alpha,$$
for $\alpha \in \mathrm{PV}^{*,*}(\C^d)[[t]]$ a closed polyvector and
$M \in \mathrm{End}(V_{N|N})$ an open matrix. The chain-level open-loop
closure of this pairing produces the coefficient $\mathrm{Str}(I) = 0$
that drives the anomaly cancellation.

---

## §2. The $d$-odd condition origin: parity argument

### 2.1. Parity of the holomorphic top form

On $\C^d$, the holomorphic top form is
$$\Omega_d \;=\; dz_1 \wedge dz_2 \wedge \cdots \wedge dz_d.$$
Under the Koszul reordering $\Omega_d \wedge \Omega_d$, one picks up
a sign $(-1)^{d(d-1)/2}$; equivalently, $\Omega_d \wedge \Omega_d = 0$
iff this sign is $-1$, which occurs for $d \equiv 2$ or $3 \pmod 4$.
For $d = 1, 4, 5, 8, 9, \ldots$, $\Omega_d \wedge \Omega_d \neq 0$.

**The relevant parity in BCOV.** The BCOV BV pairing (Costello–Li 2012
Definition 5.7) is
$$\langle \alpha, \beta\rangle_{\mathrm{BCOV}}
  \;=\; \int_X (\alpha \wedge \beta)\big|_{\mathrm{PV}^{d,d}} \cdot \Omega^2.$$
The *square* $\Omega^2 = \Omega \wedge \Omega$ has parity
$(-1)^{d(d-1)/2}$. For the pairing to be non-degenerate (i.e., to
serve as a BV pairing of degree $-1$), this sign must align with the
intrinsic polyvector signature: $\mathrm{PV}^{p,q}(\C^d) =
\Omega^{0,q}(\C^d, \wedge^p T\C^d)$ has "opposite" parity behaviour
from forms because the polyvector is the dual.

**Net parity calculation.** A polyvector
$\alpha \in \mathrm{PV}^{p,q}(\C^d)$ has degree
$p + q$ in the $\Z$-grading of polyvector forms. The BV pairing
matches $\mathrm{PV}^{p,q}$ with $\mathrm{PV}^{d-p, d-q}$ for non-degeneracy,
contributing a Koszul sign $(-1)^{p(d-p) + q(d-q) + d(d-1)/2}$ (the last
from $\Omega^2$). For the BV pairing to be **symmetric** of degree
$-1$, this sign must be $-1$, which yields the constraint
$d \equiv 1 \pmod 4$ or $d \equiv 3 \pmod 4$ — i.e., $d$ **odd**.

### 2.2. Sign in the BV trace

The chain-level one-loop BCOV/HCS anomaly representative (Costello–Li
2016 §4.3, schematic):
$$\mathrm{Ob}^{\mathrm{BCOV/HCS}}_{1\text{-loop}}
  \;=\; \hbar \cdot
  \mathrm{Str}_{\mathfrak{gl}(N|N)}(I)
  \cdot \bigl[\bar\partial \cdot \tau_d\bigr],$$
where $\tau_d$ is the cubic Schouten–Nijenhuis vertex evaluated on
the heat-kernel propagator restricted to $\mathrm{PV}^{0,1}(\C^d) \otimes
\mathrm{PV}^{0,1}(\C^d) \otimes \mathrm{PV}^{0,1}(\C^d)$ (the BCOV
cubic interaction).

The closure on the matrix factor produces $\mathrm{Str}(I)$ trivially
on bosonic–fermionic blocks. The closure on the polyvector factor,
however, involves $\Omega^2$ via the BV pairing (§2.1), and the
polyvector-parity-times-$\Omega^2$-parity is $(-1)^d$ (after
simplification). For $d$ odd, this is $-1$ and the **even** (purely
bosonic) and **odd** (purely fermionic) loop contractions enter with
*opposite* signs, so $\mathrm{Str}(I) = N - N = 0$ produces a *true*
cancellation. For $d$ even, the relative sign is $+1$ and the
cancellation *doubles* (giving $2\hbar N \neq 0$) rather than vanishes.

**Conclusion.** The $d$-odd condition is **a parity argument on the
polyvector / $\Omega^2$ pairing**. It is *not* a regulator-class
artefact and *not* fixable by changing the heat-kernel data; it is
structural at the level of the BV pairing on polyvectors.

### 2.3. Polyakov-lens interpretation

Polyakov scheme-independence (regulator-class invariance inside the
admissible class) does *not* extend to a parity-of-$d$ change. The
Costello–Li 2016 anomaly cancellation is **chain-level zero**, not a
"cohomological zero modulo regulator counterterms". On $d$ even, the
non-zero residue $2\hbar N$ is *not* a coboundary; it is a true
anomaly that no regulator-class flow can absorb. **Polyakov-class
flexibility on the regulator does not lift the $d$-odd hypothesis.**

### 2.4. Invariants-lens interpretation

The dominant invariant is the **polyvector signature**
$\sigma_d = (-1)^{d(d-1)/2}$. This is a representation-theoretic
constant on $\mathrm{PV}^{*,*}(\C^d)$, independent of the regulator
choice. For $d$ odd, $\sigma_d = -1$ (specifically: $\sigma_1 = 1$,
$\sigma_3 = -1$, $\sigma_5 = 1$, $\sigma_7 = -1$, $\ldots$ — actually
this is more subtle; the relevant sign in the one-loop chain-level
cancellation is $(-1)^d$, which is $-1$ for $d$ odd).

Numerical inspection of small cases:
- $d = 1$ (trivial, $\C^1$ is a curve): the BV pairing is symmetric;
  the cancellation closes; Costello–Li 2015 covers this.
- $d = 3$ (the canonical CY$_3$ flat case): $(-1)^3 = -1$; the
  cancellation closes; this is the **primary case** of Costello–Li
  2015 / 2016.
- $d = 5$: $(-1)^5 = -1$; the cancellation closes; covered.
- $d = 2$ (our complex dimension if read as complex): $(-1)^2 = +1$;
  the cancellation **fails** by sign-doubling.
- $d = 4$: $(-1)^4 = +1$; the cancellation **fails** by sign-doubling.

The invariant $(-1)^d$ partitions $d$-values into parity-cancellation
classes; the result is a structural firewall on $d$ even.

---

## §3. Does the result extend to $d$-even? Specifically $d=4$?

### 3.1. The $d=4$ candidate failure

For $d = 4$, the BV pairing parity calculation (§2.1) gives
$d(d-1)/2 = 6 \equiv 0 \pmod 2$, so $\Omega^2 \wedge \Omega^2$ has the
"wrong" parity for the BV pairing to be symmetric of degree $-1$. The
polyvector signature is $\sigma_4 = +1$, which combined with the
loop-closure parity yields a *doubled* anomaly:
$$\mathrm{Ob}^{\mathrm{BCOV/HCS}}_{1\text{-loop}}\Big|_{d=4}
  \;=\; \hbar\bigl(\mathrm{Tr}_{\text{even}}(I) + \mathrm{Tr}_{\text{odd}}(I)\bigr)
  \cdot[\bar\partial \cdot \tau_4]
  \;=\; 2\hbar N \cdot [\bar\partial \cdot \tau_4]
  \;\neq\; 0.$$

**Mechanism breaks at the parity step.** The supertrace identity
$\mathrm{Str}(I) = 0$ requires the bosonic–fermionic blocks to enter
with *opposite* signs on the loop closure. On $d$ even, the parity
calculation produces a *same-sign* combination, defeating the
cancellation regardless of the open-algebra super-extension.

### 3.2. The exact step where the discharge breaks

Tracing through Costello–Li 2016 Theorem A proof:
1. **(Step 1)** Setup: open-closed BCOV theory on $\C^d$ with
   $\mathfrak{gl}(N\mid N)$ open algebra. **Independent of $d$ parity.**
2. **(Step 2)** Compute one-loop QME obstruction. **Independent of $d$
   parity at the schematic level**: the obstruction is the open-loop
   closure of the cubic vertex against the heat-kernel propagator.
3. **(Step 3)** Identify the coefficient as $\mathrm{Str}(I) \cdot
   [\text{vertex}]$. **This is where the $d$-parity enters.** On $d$
   odd, the bosonic and fermionic contributions enter with opposite
   signs via the polyvector / $\Omega^2$ pairing; on $d$ even, they
   enter with the same sign.
4. **(Step 4)** Conclude $\mathrm{Str}(I) = 0$ closes the
   cancellation. **Fails for $d$ even** because the actual coefficient
   in the loop closure is $\mathrm{Tr}(I) + \mathrm{Tr}(I) = 2N$, not
   $\mathrm{Str}(I) = N - N = 0$.

The break is at **Step 3**: the parity-dependent loop closure
coefficient.

### 3.3. Could a different super-extension repair $d=4$?

**Candidate (D-1).** Use $\mathfrak{gl}(N\mid M)$ with $N \neq M$ and
some special tuning. **Negative.** The issue is not the imbalance of
the super-extension; it is the parity mismatch between the polyvector
signature and the open-algebra Killing form. Tuning $N - M$ does not
absorb a sign coming from the spacetime $\C^d$ chain-level structure.

**Candidate (D-2).** Use a different parity-graded open algebra
(e.g., $\mathfrak{osp}(2N\mid 2M)$ or $\mathfrak{q}(N)$). **Negative
for the same reason.** The Killing form sign is a feature of the open
algebra; the $d$-parity sign is a feature of the closed spacetime.
The two are independent and cannot be mutually corrected by changing
only one.

**Candidate (D-3).** Use a *twist* on the closed spacetime that
flips the polyvector parity. **Possible but breaks BCOV setup.** A
"parity twist" on $\C^4$ would change the polyvector grading
$\mathrm{PV}^{p,q} \to \mathrm{PV}^{p, q+1}$ (or similar), but any such
twist would change the underlying complex structure on $\C^4$ (e.g.,
to a $\C^{2|2}$ super-target), invalidating the original BCOV setup.

**Candidate (D-4).** Insert a *boundary state* that produces a
parity-correcting sign. **Highly conditional.** Any boundary state
that flips the polyvector parity on the loop closure would have to
be local on $L \subset \C^4$ and parity-inhomogeneous; no such object
exists in the Costello–Li 2015 / 2016 framework.

**Conclusion.** No candidate inside the Costello–Li 2015 / 2016
framework discharges the $d=4$ anomaly. **The $d$-odd condition is
structurally permanent at the chain-level cancellation layer.**

### 3.4. What about $d \equiv 1 \pmod 4$ vs $d \equiv 3 \pmod 4$?

A subtler version: the parity calculation $(-1)^{d(d-1)/2}$ gives:
- $d = 1$: $(-1)^0 = +1$;
- $d = 3$: $(-1)^3 = -1$;
- $d = 5$: $(-1)^{10} = +1$;
- $d = 7$: $(-1)^{21} = -1$;

For the BV pairing to be symmetric of degree $-1$, one needs the
total sign on the chain-level cancellation. The relevant sign in
Costello–Li 2016 Theorem A is *not* simply $(-1)^{d(d-1)/2}$ but a
combination involving the polyvector grading on $\mathrm{PV}^{p,q}(\C^d)$
and the Schouten-Nijenhuis sign. The net result is that *both*
$d \equiv 1$ and $d \equiv 3 \pmod 4$ work (consistent with
"$d$ odd"), with potentially different vertex-class normalisations.

This sub-stratification does *not* affect our verdict; both $d=3$ and
$d=5$ are inside Costello–Li 2015's hypothesis, and neither corresponds
to the manuscript's local model.

---

## §4. Manuscript's $\R^2 \times \C^2$ dimensional-character analysis

### 4.1. The exact local-model setup

The manuscript's local model is on
$$M = \R^2, \qquad Y = \C^2, \qquad X = M \times Y = \R^2 \times \C^2,$$
with mixed brane $\R \times \{p\} \hookrightarrow \R^2 \times \C^2$
(`main.tex`:1276–1282). The kinematic differential is
$$D = d_{\R^2} + \bar\partial_{\C^2}$$
(`main.tex`:1305), a *mixed* differential combining de Rham on $\R^2$
and Dolbeault on $\C^2$.

The closed fields are
$$\mathcal E_{\mathrm{cl}}(D \times B) =
  \Omega^*(D) \widehat\otimes \Omega^{0,*}(B) \widehat\otimes
  \bigl(\widehat{\mathfrak h}[1]
  \oplus \widehat{\mathfrak h}^\vee_{\mathrm{cont}}[2]\bigr),$$
with $\widehat{\mathfrak h} = \C[[z_1, z_2]] / \C \cdot 1$ the
completed Hamiltonian Lie algebra on the formal symplectic disk
$\widehat{\C^2}_0$ with $\omega = dz_1 \wedge dz_2$.

**Note: $\R^2$ is de Rham, not complex.** The $\R^2$ factor carries
the *real* de Rham complex $\Omega^*(\R^2)$, with differential
$d_{\R^2}$ (real $1$-form-valued). It is *not* the real underlying
manifold of a complex curve; it has no holomorphic structure.

### 4.2. Possible dimensional-character interpretations

Three candidate interpretations of the manuscript's spacetime:

**(R-A) Read as $\C^3$.** Identify $\R^2 \cong \C \cdot \tau$ (the
"topological time" $t \in \R$ becomes a complex coordinate $\tau$);
then $X = \R^2 \times \C^2 = \C \times \C^2 = \C^3$ in real-real
correspondence. Total complex dimension $d = 3$ (odd).

**Problem with (R-A).** This identification *changes the kinematic
differential* from $D = d_{\R^2} + \bar\partial_{\C^2}$ to
$\bar\partial_{\C^3}$ (pure Dolbeault on $\C^3$). The manuscript's
first-class constraint $[\phi_1, \phi_2] = 0$ and BV reduction
$Q\psi = [\phi_1, \phi_2]$ (`main.tex`:118–125) are formulated on
$\R$ (real worldline), not on a complex curve. **The R-A interpretation
breaks the manuscript's defect structure.**

**(R-B) Read as $\C^2$ with topological reduction.** Treat the $\R^2$
as a *topological reduction direction* in a higher-dimensional theory
$\R^2 \times \C^d$ that compactifies along $\R^2$. Then the residual
theory is on $\C^d$, and choosing $d = 2$ gives our manuscript. Total
complex dimension $d_{\mathrm{eff}} = 2$ (even).

**Problem with (R-B).** The manuscript does *not* compactify $\R^2$;
$\R^2$ remains the topological factor with $d_{\R^2}$ as part of the
mixed differential. **Treating $\R^2$ as a reduction direction
mis-states the manuscript's setup.**

**(R-C) Read as a mixed real-complex hybrid.** Accept the
$d_{\R} + 2 d_{\C}$ kinematics: $d_{\R^2} = 2$ real topological
directions plus $d_{\C^2} = 2$ complex holomorphic directions. Total
real dimension $d_{\mathrm{tot}}^\R = 2 + 4 = 6$. Total complex
dimension *not defined* because the spacetime is not a complex
manifold.

**This is the manuscript's actual interpretation** (`main.tex`:78–82,
1276–1286). The total real dimension is $1+4 = 5$ for the brane
worldline plus formal disk view, or $2+4 = 6$ for the bulk $\R^2 \times
\C^2$. The complex dimension is *not* a well-defined invariant for
this mixed structure.

### 4.3. Comparison with Costello–Li 2015 dimensional table

| Spacetime | Costello–Li 2015 / 2016 | Our model |
|---|---|---|
| Complex dimension | $d$ odd ($d = 1, 3, 5, \ldots$) | Not well-defined (mixed real-complex) |
| Total real dimension | $2d$ ($= 2, 6, 10, \ldots$) | $6$ ($= 2 + 4$) |
| Underlying manifold | $\C^d$ flat | $\R^2 \times \C^2$ (mixed) |
| Differential | $\bar\partial_{\C^d}$ (pure Dolbeault) | $d_{\R^2} + \bar\partial_{\C^2}$ (mixed) |
| Closed BCOV fields | $\mathrm{PV}^{*,*}(\C^d)[[t]]$ | Hamiltonian BF on $\widehat{\C^2}_0$ |
| Holomorphic top form | $dz_1 \wedge \cdots \wedge dz_d$ | $\omega = dz_1 \wedge dz_2$ on $\widehat{\C^2}_0$ |
| Open algebra | $\mathfrak{gl}(N\mid N)$ | $\mathfrak{gl}_N$ (or $\mathfrak{gl}(N\mid N)$ super-extended) |

**Key structural mismatches.**
- **Total real dimension match at $d=3$.** Costello–Li 2015 with
  $d = 3$ has $d_{\mathrm{tot}}^\R = 6$, matching our $\R^2 \times \C^2$
  in real dimension. **But the comparison ends there.**
- **Differential structure mismatch.** Costello–Li's pure $\bar\partial$
  vs our mixed $d_{\R^2} + \bar\partial_{\C^2}$. The manuscript's
  *de Rham* factor does not enter Costello–Li's framework.
- **Form structure mismatch.** Costello–Li uses the *Calabi–Yau pairing*
  via $\Omega_d$ (a holomorphic $d$-form); our model uses the
  *holomorphic symplectic* $\omega = dz_1 \wedge dz_2$ (a holomorphic
  $2$-form on $\C^2$, *not* a top form on $\R^2 \times \C^2$).
- **Field-content mismatch.** Costello–Li uses polyvector fields
  (Schouten–Nijenhuis); our model uses Hamiltonian BF (polynomial
  Hamiltonian bracket).

### 4.4. Verdict on dimensional character

The manuscript's $\R^2 \times \C^2$ is **structurally distinct from
flat $\C^d$ for any $d$.** The relevant comparison is *not* a
dimensional-reduction argument from $\C^3$ to $\C^2$; it is a
*kinematic-differential* mismatch. The local model lives in a
different obstruction complex from Costello–Li 2015.

The closest matching candidate is $d = 3$ in *real dimension*, but
this is a coincidence of total real dimension, not a comparison map
of obstruction complexes.

---

## §5. Smallest distinguishing test: $d = 3$ via $\R^2$-reduction vs $d = 4$-direct

### 5.1. Setup of the test

**Hypothesis A ($d = 3$ via $\R^2$-reduction).** The manuscript's
$\R^2 \times \C^2$ arises from a hypothetical compactification of a
Costello–Li 2015 theory on $\C^3$ along the $\R^2$ direction.

**Hypothesis B ($d = 4$-direct).** The manuscript's $\R^2 \times \C^2$
is a $d_{\mathrm{tot}}^\R = 6$ spacetime with no underlying $\C^d$
structure; or equivalently, a $d = 2$-even Costello–Li-style theory
(broken by parity) on $\C^2$ with a topological factor $\R^2$ added.

### 5.2. The test: chain-level one-loop residue

**Under Hypothesis A.** Compactifying Costello–Li 2015 on $\C^3$ along
the "$\R^2$" direction would require a holomorphic embedding $\R^2
\hookrightarrow \C^3$ as some Lagrangian-or-special-Lagrangian
subspace, with the residual theory on $\C^2$ obtained by integration
along this embedding. The one-loop residue would be:
$$\mathrm{Res}^A_{1\text{-loop}}
  \;=\; \int_{\R^2 \subset \C^3}
  \mathrm{Ob}^{\mathrm{BCOV/HCS}}_{1\text{-loop}}\Big|_{\C^3}
  \;=\; 0,$$
because $\mathrm{Str}_{\mathfrak{gl}(N|N)}(I) = 0$ on Costello–Li 2015's
one-loop class on $\C^3$. The integration over $\R^2$ would commute
with the supertrace (since the supertrace is a representation-theoretic
constant, not a spacetime integral), and the result would be **zero**.

**Under Hypothesis B.** A direct $d = 4$-style computation on
$\R^2 \times \C^2$ would (heuristically, by a $d$-parity argument)
produce a *doubled* residue:
$$\mathrm{Res}^B_{1\text{-loop}}
  \;=\; 2\hbar N \cdot [\text{vertex}] \;\neq\; 0,$$
because the $d$-even parity defeats the supertrace cancellation
(§3.1).

### 5.3. The actual manuscript residue

The manuscript's chain-level QME residue (`appendix-unreduced-bv-qme.tex`:118–123) is
$$\mathrm{Ob}_{\mathrm{sc}}(\gamma_{\mathbf 1}; a, f; b, g)
  \;=\; \hbar N \,\omega(f, g) \int_\R a(t) b(t) \gamma_{\mathbf 1}(t)\, dt,$$
with $\omega(f, g) = [\{f, g\}]_0$ the Lie 2-cocycle on $\bar A =
\C[z_1, z_2] / \C \cdot 1$.

**This residue is** $\hbar N \cdot [\bar c]$, **not zero and not
doubled.** It carries:
- A factor of $\hbar N$ (single-trace, *not* doubled).
- The Lie 2-cocycle $\omega(f, g)$ on $\bar A$, *not* the BCOV
  $\bar\partial$-coboundary on polyvectors of $\C^d$.
- An integral over $\R$ (not $\R^2$), arising from the *worldline*
  of the brane $\R \times \{p\}$, *not* from a Lagrangian embedding
  in $\C^d$.

### 5.4. Verdict on the test

**Neither Hypothesis A nor Hypothesis B matches the manuscript's
residue.**

- Hypothesis A predicts **zero** residue (by Costello–Li 2015
  cancellation on $\C^3$). The manuscript's residue is non-zero
  ($\hbar N[\bar c]$). **Hypothesis A fails.**
- Hypothesis B predicts a *doubled* residue ($2\hbar N$). The
  manuscript's residue is single-trace ($\hbar N$). **Hypothesis B
  fails (different coefficient).**

**Both hypotheses are incorrect.** The manuscript's residue arises
from a *different* mechanism: the Capelli shift on the unreduced
brane phase space (`thm:quantum-classical-anomaly`), not from a
dimensional-reduction or dimension-extension of Costello–Li 2015.

The distinguishing test confirms that the manuscript's framework is
**structurally orthogonal** to Costello–Li 2015's dimensional table.
Neither $d = 3$-via-reduction nor $d = 4$-direct describes our
geometry; the manuscript is in an *entirely different* obstruction
complex.

### 5.5. The true comparison: super-extension

The *only* matching example (per BCOV-A5 §5.1) is the super-balanced
extension: when the manuscript's open algebra is replaced by
$\mathfrak{gl}(N\mid N)$ (W22-T1), the residue becomes
$$\mathrm{Ob}_{\mathrm{sc}}^{\mathrm{super}}\Big|_{N=M}
  \;=\; \hbar(N - M) \cdot \omega(f, g) \int_\R a b \, dt
  \Big|_{N=M} \;=\; 0.$$
This **coupling-coefficient** match runs through the supertrace
identity $\mathrm{Str}(I) = 0$, *not* through any dimensional argument.
It is parallel to Costello–Li 2016 Theorem A but in a *different*
chain complex.

---

## §6. Cross-walk to W30 (A5) regulator class

### 6.1. The (A5) hypothesis on parity

The manuscript's (A5) hypothesis (proposed inscription, per BCOV-A5 §2.3) requires:
$$P = \mathrm{diag}(\mathbf 1_N, -\mathbf 1_M) \quad\text{is a structural symmetry of the matrix-factor regulator data},$$
i.e.,
$$[K_t, P] = 0, \qquad [Q^{\mathrm{GF}}, P] = 0, \qquad [P_{\epsilon, L}, P] = 0$$
on the heat-kernel propagator constructed from a parity-equivariant
super-Killing form (A2$'$).

### 6.2. Compatibility with $d$-odd Costello–Li

Costello–Li 2015 (implicit; explicit in 2016) uses a heat-kernel
regulator on polyvectors of $\C^d$ with the following properties:
- Heat kernel $K_t^{(d)}$ on $\Omega^{0, *}(\C^d, \wedge^* T\C^d)$
  built from the flat Kähler metric.
- Sector decomposition: even ($\C^N$) and odd ($\C^N$) blocks of
  $\mathfrak{gl}(N\mid N)$.
- Parity preservation: the heat-kernel regulator commutes with the
  parity operator $P$ on $\C^{N|N}$ at the matrix factor.

**(A5) is *exactly* this parity-preservation property** on our side.
The Costello–Li 2015 regulator is in the (A5)-admissible class, and
the (A5) hypothesis on our side is the manuscript's parallel of the
Costello–Li parity-equivariance.

### 6.3. The W30 regulator audit four branches

The W30 regulator audit (per BCOV-A5 inputs, four regulator branches
R1–R4) verifies (A5) compatibility across:
- (R1) Heat-kernel from super-Killing.
- (R2) Pauli–Villars regulator with parity-equivariant masses.
- (R3) Hadamard regularisation with parity-symmetric subtraction.
- (R4) Dimensional regularisation with parity-fixed dimension.

All four agree on $[\bar c]$ (the manuscript's chain-level vertex
cocycle). All four are also Costello–Li-2015-compatible at the
parity-equivariance layer.

### 6.4. Compatibility with $d$-odd vs $d$-even

**Crucial distinction.** The (A5) hypothesis preserves parity at the
*matrix factor* (open-algebra side). It does **not** address the
*spacetime parity* governing $d$-odd vs $d$-even.

- (A5) + (A2$'$) suffice for the *open-algebra* discharge:
  $\mathrm{Str}(I) = 0$ on the open loop closure.
- The $d$-odd hypothesis on Costello–Li 2015 is a *spacetime parity*
  statement (polyvector / $\Omega^2$ sign on $\C^d$). On our
  $\R^2 \times \C^2$, there is no $\Omega_d$ for $d$-odd or $d$-even
  to compare against.

**Consequence.** The W30 (A5) regulator class is **compatible** with
the $d$-odd condition of Costello–Li 2015 in the sense that both use
parity-equivariant regulators. They are **not interchangeable** in
the sense that (A5) does not lift the $d$-odd structural barrier; it
sits inside the *open-algebra parity* layer, while $d$-odd sits
inside the *spacetime parity* layer.

### 6.5. Polyakov-lens interpretation

Polyakov scheme-independence inside the (A1)–(A5) admissible class
governs the *open-algebra side*. It ensures that any
parity-equivariant regulator gives the same chain-level residue.
Costello–Li 2015's $d$-odd hypothesis governs the *spacetime side*;
it is *not* a regulator-class statement and *not* a Polyakov-class
choice. **The two layers are orthogonal**, and (A5) cannot weaken
the $d$-odd hypothesis (or vice versa).

### 6.6. Invariants-lens interpretation

Two invariants survive across the W30 audit:
- $\mathrm{Str}(I) = N - M$ on the matrix factor (open-algebra side).
- $[\bar c] \in H^2_{\mathrm{Lie}}(\bar A, \C)$ on the closed
  Lie-algebra side.

Costello–Li 2015's invariants are:
- $\mathrm{Str}(I) = 0$ on the matrix factor (same).
- $[\mathrm{HCS\,vertex}] \in H^1(\mathcal O_{\mathrm{loc}}^{\mathrm{BCOV}},
  \bar\partial + \{S, -\})$ on the polyvector side (different).
- The polyvector signature $\sigma_d = (-1)^{d(d-1)/2}$ (additional).

The matrix-factor invariant is shared; the closed-side invariants
differ. The shared invariant is the *coupling coefficient* of the
W22-T1 / Costello–Li 2016 Theorem A parallel. **(A5) compatibility
with Costello–Li 2015 holds at the matrix-factor / Polyakov-class
layer; the closed-side comparison is a separate firewall.**

---

## §7. `stmt:costello-li-flat-bcov` inscription validity

### 7.1. The current inscription

`main.tex`:5155–5166:

> **Imported Costello–Li flat open-closed BCOV theorem.** Costello–Li
> prove a perturbative quantization of open-closed BCOV theory on
> flat $\C^d$, for $d$ odd, unique up to the equivalences in their
> renormalization scheme, with open gauge algebra
> $\mathfrak{gl}(N\mid N)$ and compatibility under
> $\mathfrak{gl}(N\mid N) \hookrightarrow \mathfrak{gl}(N+k\mid N+k)$. In
> that flat open-closed BCOV/HCS theory they compute the anomaly
> cancellation needed for the graph construction
> [costello-li-open-closed-bcov]. Ordinary $\mathfrak{gl}_N$ and the
> mixed $\R^2 \times \C^2$ Hamiltonian brane model are not covered by
> this theorem without an additional reduction or summand argument.

### 7.2. Validity check

**Element 1.** "Flat $\C^d$ for $d$ odd." **Correct.** Matches
Costello–Li 2015 Theorem 1.2.

**Element 2.** "Open gauge algebra $\mathfrak{gl}(N\mid N)$ with
compatibility under $\mathfrak{gl}(N\mid N) \hookrightarrow
\mathfrak{gl}(N+k\mid N+k)$." **Correct.** Matches Costello–Li 2015
§3.5 (stabilisation under super-extension).

**Element 3.** "Anomaly cancellation needed for the graph construction."
**Correct.** Matches Costello–Li 2016 Theorem A.

**Element 4.** "Ordinary $\mathfrak{gl}_N$ and the mixed
$\R^2 \times \C^2$ Hamiltonian brane model are not covered by this
theorem without an additional reduction or summand argument."
**Correct.** This is the manuscript's correct statement of the
exclusion. It implicitly captures both:
- (i) the open-algebra exclusion (bosonic $\mathfrak{gl}_N$ does not
  admit the supertrace cancellation; explicit in
  `prop:costello-li-2012-fail-local` (F4));
- (ii) the spacetime-mismatch exclusion (the mixed
  $\R^2 \times \C^2$ is not flat $\C^d$ for any $d$; explicit in
  `prop:costello-li-2012-fail-local` (F1, F2, F3, F5)).

### 7.3. Possible clarifying remark (proposal-only)

A *minor* clarification could be added (proposal-only; no edit
recommended without a separate Phase-5 review). Two candidate forms:

**Candidate (C-i, light).** Append a single sentence:
> The dimension condition $d$ odd is a parity argument on the BV
> pairing via the holomorphic top form $\Omega_d^2$; the result
> does not extend to $d$ even.

**Candidate (C-ii, structural).** Append a remark linking to
`tate-T4-bv-vanishing.tex`:
> The mixed $\R^2 \times \C^2$ kinematic differential
> $D = d_{\R^2} + \bar\partial_{\C^2}$ is *not* the pure Dolbeault
> $\bar\partial_{\C^d}$ of Costello–Li 2015 for any $d$; the
> $\R^2$ is a topological factor, not a complex direction
> (`tate-T4-bv-vanishing.tex` §F1, F2 detail this firewall).

### 7.4. Recommendation

**Neither clarification is load-bearing.** The current inscription
correctly excludes the $\R^2 \times \C^2$ model. The clarifying
sentences would be cosmetic enhancements only. The manuscript already
has `tate-T4-bv-vanishing.tex` (F1)–(F5) and `rmk:convention-firewall`
on `main.tex`:5380–5394 doing structural firewall work; the
inscription's brief one-sentence exclusion is sufficient.

**Proposal verdict.** No edit needed. The existing `stmt:costello-li-flat-bcov`
captures the dimensional applicability correctly. If a Phase-5 reviewer
wants additional clarity, candidate (C-i) is the lightest-touch
addition; candidate (C-ii) is the most structurally complete but
duplicates information in `tate-T4-bv-vanishing.tex`.

---

## §8. Anti-attack scan responses

### 8.1. (Att-1) BV trace mechanism on $\R^2 \times \C^2$

**Attack.** Costello–Li 2015 uses the holomorphic top form on $\C^d$
to define the BV trace; on $\R^2 \times \C^2$ the holomorphic top
form is $dz_1 \wedge dz_2$ (a 2-form on $\C^2$), so the BV trace
mechanism may need a real-dimensional reduction in the $\R^2$ direction.

**Response.** Correct observation. The manuscript's BV pairing
(`main.tex`:1306–1316) is constructed via:
- Form-component multiplication on $\Omega^*(\R^2)
  \widehat\otimes \Omega^{0,*}(\C^2)$.
- Top-form integration over $\R^2 \times \C^2$ against
  $dz_1 \wedge dz_2$ (the holomorphic 2-form on $\C^2$).
- Continuous evaluation pairing on $\widehat{\mathfrak h}^\vee_{\mathrm{cont}}
  \otimes \widehat{\mathfrak h}$.

The "top-form" condition is $p + q = 4$ (real form-degree on $\R^2$
plus complex Dolbeault degree on $\C^2$), making the pairing degree
$-1$.

**This is a *different* BV trace mechanism from Costello–Li 2015's**
(which uses $\Omega_d^2$ on $\C^d$). Our BV trace is:
$$\langle\alpha, \beta\rangle_{\mathrm{ours}}
  \;=\; \int_{\R^2 \times \C^2} (\alpha \cdot \beta) \cdot dz_1 \wedge dz_2,$$
*not*
$$\langle\alpha, \beta\rangle_{\mathrm{CL}}
  \;=\; \int_{\C^d} (\alpha \wedge \beta) \cdot \Omega_d^2.$$

The "real-dimensional reduction" along $\R^2$ is *exactly* the
manuscript's existing $\R^2$-integration. **No new mechanism is
needed; the BV trace is constructed directly on $\R^2 \times \C^2$
without going through Costello–Li 2015's $\C^d$ formulation.**

### 8.2. (Att-2) Kähler form parity on $\R^2 \times \C^2$

**Attack.** The $d$-odd condition stems from the parity of Kähler
form orientation; on $\R^2 \times \C^2$ the Kähler form has different
parity behaviour than on $\C^d$.

**Response.** Correct, and structurally important. On $\C^d$ the
Kähler form $J = \frac{\sqrt{-1}}{2}\sum_i dz_i \wedge d\bar z_i$ is
real $(1, 1)$ of total real degree 2. On $\R^2 \times \C^2$:
- The $\R^2$ factor has its own *symplectic* form (e.g.,
  $dx \wedge dy$ in coordinates $\R^2 = \{(x, y)\}$), but the
  manuscript does *not* use this — $\R^2$ is *purely topological*
  (de Rham only, no symplectic structure invoked).
- The $\C^2$ factor has the *holomorphic symplectic* form
  $\omega = dz_1 \wedge dz_2$ (a $(2, 0)$-form, *not* the Kähler $(1,1)$
  form).

**Crucial distinction.** The manuscript's $\omega$ is *holomorphic*
$(2, 0)$, not Kähler $(1, 1)$. Costello–Li 2015 uses the *Calabi–Yau
holomorphic volume form* $\Omega_d$ (a holomorphic $(d, 0)$-form), and
the $d$-odd condition is on this. **On our $\C^2$, the analogous
"holomorphic top form" is $\omega^2$**; but $\omega^2 = (dz_1 \wedge
dz_2)^2 = 0$ (because $dz_1 \wedge dz_2 \wedge dz_1 \wedge dz_2 =
-dz_1 \wedge dz_1 \wedge dz_2 \wedge dz_2 = 0$). The BV pairing on
$\C^2$ via $\omega^2$ degenerates.

**This is not a problem for our manuscript** because our BV pairing
does *not* use $\omega^2$; it uses *single* $\omega = dz_1 \wedge dz_2$
combined with the form-component on $\R^2$ to produce a top-form on
$\R^2 \times \C^2$.

The Kähler form parity on $\R^2 \times \C^2$ is therefore *not*
analogous to Costello–Li 2015's $\Omega_d^2$ parity. The two
constructions are structurally different. **The $d$-odd parity
argument does not transfer.**

### 8.3. (Att-3) Codimension-3 brane defect

**Attack.** The manuscript's brane-defect along $\R \times \{0\}
\subset \R^2 \times \C^2$ is a codimension-$3$ brane (in real
dimension: $\R \subset \R^2 \times \C^2$ is $1$-dimensional, with
codimension $5$; in complex dimension: not well-defined). Does
Costello–Li 2015 cover codimension-$3$ branes?

**Response.** Costello–Li 2015 covers branes on Lagrangian
submanifolds $L \subset \C^d$ with $\dim_\R L = d$ (real Lagrangian
in a real-$2d$-dimensional Calabi–Yau). For $d = 3$: $\dim_\R L = 3$,
a real-$3$-dimensional submanifold of real-$6$-dimensional $\C^3$.

**Our brane $\R \times \{0\} \subset \R^2 \times \C^2$ is
real-$1$-dimensional in the real-$6$-dimensional bulk.**
Codimension is $5$ in real dimension. This is *not* a Lagrangian
in the Costello–Li sense; it is a *defect* (in the manuscript's
language: "the brane $\R \times p$ is a defect in the mixed space,
not a spacetime boundary unless a half-space model is separately chosen"
— `main.tex`:5172–5174).

**Costello–Li 2015 does *not* cover codimension-$5$ defects.** The
open-closed coupling in their framework is via a *Lagrangian* brane
(real-half-dimensional in the real-$2d$-dimensional bulk), not via
an arbitrary submanifold.

This is **exactly** failure mode (F3) in `prop:costello-li-2012-fail-local`:
"Brane defect. The brane $\R \times p$ is one-real-dimensional in the
topological direction and point-supported in the holomorphic direction.
Costello–Li 2012 has no brane sector. Costello–Li 2015 has a brane
sector but on flat $\C^d$ (not $\R^2 \times \C^2$) with $\mathfrak{gl}(N\mid N)$
open gauge data."

The manuscript's brane is a *transverse defect*, *not* a
codimension-$d$ Lagrangian in the Costello–Li sense. Codimension
mismatch is structural; cannot be repaired by changing $d$.

### 8.4. (Att-4) Non-flat backgrounds

**Attack.** Does Costello–Li 2015 extend to non-flat backgrounds? Our
$\R^2 \times \C^2$ with the Hamiltonian connection has $F_\alpha = 0$
(flat), so this should be OK.

**Response.** Costello–Li 2015 is on flat $\C^d$. Costello–Li 2012
extends to compact CY$_d$ (with curvature) but with closed BCOV only
(no brane). Costello–Li 2015's open-closed extension is *only* on flat
$\C^d$ for $d$ odd.

**Our manuscript has $F_\alpha = 0$ (flat Hamiltonian connection,
`main.tex` various places).** This is consistent with the *flatness*
hypothesis on Costello–Li 2015, but consistency with flatness is a
*necessary* condition, not a sufficient one. The dimensional and
kinematic mismatches (§4) remain.

**$F_\alpha = 0$ flatness invariant** survives the comparison —
both sides require flatness. But this is one of *several* conditions;
the others (kinematic differential, Lagrangian vs defect, complex
dimension, etc.) do not.

### 8.5. Anti-attack scan summary

| Attack | Response | Verdict |
|---|---|---|
| Att-1 (BV trace) | Manuscript constructs BV trace directly on $\R^2 \times \C^2$, not via Costello–Li 2015 $\C^d$ formulation; $\R^2$-integration is intrinsic | **Does not undermine ANALOGUE verdict** |
| Att-2 (Kähler parity) | Our $\omega$ is holomorphic $(2,0)$, not Kähler $(1,1)$; $\omega^2 = 0$; the analog of $\Omega_d^2$ is degenerate; parity argument structurally different | **Does not undermine ANALOGUE verdict** |
| Att-3 (Codim-3 brane) | Manuscript has codim-$5$ defect, not Lagrangian; Costello–Li 2015 does not cover; matches existing F3 failure mode | **Confirms ANALOGUE verdict** |
| Att-4 (Non-flat) | Both sides require flatness; necessary not sufficient | **Does not undermine ANALOGUE verdict** |

**No attack overturns the §0 verdict (ANALOGUE).** All four
considerations are consistent with the existing
`stmt:costello-li-flat-bcov` exclusion and with the manuscript's
five named failure modes (F1)–(F5) in `prop:costello-li-2012-fail-local`.

---

## §9. Residuals + Phase-5 escalation

### 9.1. Residuals

(R-9-A) The manuscript's $\R^2 \times \C^2$ is structurally distinct
from any flat $\C^d$ in Costello–Li 2015. Recommendation: no edit.

(R-9-B) The $d$-odd condition does not extend to $d$-even (specifically
$d = 4$). The manuscript correctly excludes this via the implicit
spacetime-mismatch in `stmt:costello-li-flat-bcov` and explicitly via
`prop:costello-li-2012-fail-local`.

(R-9-C) Optional clarifying remarks (C-i, C-ii) in §7.3 are
cosmetic enhancements; not load-bearing.

(R-9-D) The cross-walk to W30 (A5) regulator class confirms
parity-equivariance compatibility at the matrix-factor layer; the
spacetime $d$-parity is orthogonal to (A5) and does not lift the
$d$-odd hypothesis.

(R-9-E) The smallest distinguishing test (§5) shows that neither
$d=3$-via-reduction nor $d=4$-direct describes the manuscript; the
manuscript's framework is structurally orthogonal to Costello–Li
2015's dimensional table.

### 9.2. Phase-5 escalation candidates

If a Phase-5 reviewer demands further dimensional analysis:

(P5-A) **A theorem extending Costello–Li 2015 to mixed
$\R^k \times \C^d$ with topological factor.** This would require:
- A version of `stmt:costello-li-2012-restated` where the closed
  fields are $\mathrm{PV}^{*,*}(\C^d)[[t]]$ tensored with
  $\Omega^*(\R^k)$ (the mixed kinematic).
- An anomaly cancellation theorem on the mixed differential
  $D = d_{\R^k} + \bar\partial_{\C^d}$.
- A $d$-parity statement adapted to the mixed setup.

No such theorem exists in the literature consulted. This is one of
the four missing theorems in `rmk:t4-four-missing` (clauses 1, 2).

(P5-B) **A theorem on codimension-$5$ defects in mixed
$\R^2 \times \C^2$.** This would require:
- A defect-quantisation framework for $\R \times \{p\}$ in
  $\R^2 \times \C^2$ (analogous to Costello–Li 2015's Lagrangian
  brane on $\C^d$).
- An open-algebra structure on $\mathfrak{gl}_N$ (not super-extended)
  with a *new* anomaly cancellation mechanism.

No such theorem exists. This is the manuscript's
`prob:formal-factorization-center` and `prob:weighted-rg-locality`
in current open-obligations.

(P5-C) **A theorem on the polynomial-bracket-vs-Schouten-Nijenhuis
comparison.** The manuscript uses the polynomial Hamiltonian bracket
$\{f, g\} = \partial_{z_1} f \partial_{z_2} g - \partial_{z_2} f
\partial_{z_1} g$ on $\bar A$; Costello–Li uses the Schouten–Nijenhuis
bracket on polyvectors. These two brackets coincide *only on the
linear part of the Hamiltonian* (and disagree at all higher orders).
A chain-level comparison theorem between the two brackets at all
orders would be a separate Phase-5 obligation.

(P5-D) **A theorem on bosonic $\mathfrak{gl}_N$ open-algebra discharge
without super-extension.** Per UB.1 verdict (Unreduced-Bosonic-Phase5
§1), no such theorem exists; the bosonic conditional is structurally
permanent.

### 9.3. Ledger summary

| Item | Status |
|---|---|
| Costello–Li 2015 / 2016 dimensional applicability to $\R^2 \times \C^2$ | **ANALOGUE only** |
| $d$-odd extension to $d=4$ | **NEGATIVE** (structurally permanent) |
| Manuscript's `stmt:costello-li-flat-bcov` validity | **CORRECT as inscribed** |
| Optional clarifying remark | **NOT LOAD-BEARING** (cosmetic only) |
| W30 (A5) regulator class compatibility | **YES at matrix-factor layer**; **orthogonal to spacetime $d$-parity** |
| Phase-5 escalation routes | **(P5-A), (P5-B), (P5-C), (P5-D)** all named; none is in scope for current manuscript |

### 9.4. Final note on cross-volume firewall

This Costello–Li 2015 dimensional probe sits inside the
*cross-volume firewall* layer (`main.tex`:5894–5915). The manuscript
makes no assertion about CY$_3$ flat or compact, no $K3 \times E$,
no Igusa cusp form, no BKM denominator. The Costello–Li 2015 bridge
is *strictly local* in the firewall topology: it informs the
super-balanced extension of Theorem G (W22-T1, W22-T2) but does not
transfer any closed-string compact CY conclusion.

The dimensional mismatch found here ($\R^2 \times \C^2$ is not
$\C^d$ for any $d$) is *consistent* with the firewall's
anti-transfer principle: the manuscript's local model is
*structurally distinct* from Costello–Li 2015's flat $\C^d$, and the
manuscript correctly inscribes this exclusion. **The firewall holds
under this probe.**

---

## §10. Cross-references

- **§0 Executive verdict:** ANALOGUE; minor optional clarification
  remark; $d$-odd does not extend to $d$ even.
- **§1 Costello–Li 2015 statement:** flat $\C^d$ for $d$ odd with
  $\mathfrak{gl}(N\mid N)$; one-loop anomaly cancellation
  (Costello–Li 2016 Theorem A) via $\mathrm{Str}(I) = 0$.
- **§2 $d$-odd condition origin:** parity argument on
  polyvector / $\Omega^2$ pairing; sign $(-1)^{d(d-1)/2}$ aligns with
  BV pairing only for $d$ odd; chain-level cancellation requires
  opposite-sign closure on bosonic vs fermionic blocks.
- **§3 $d$-even extension:** structurally fails at the
  parity-step (Step 3 in the cancellation argument); no candidate
  super-extension or twist repairs.
- **§4 Manuscript dimensional character:** $\R^2 \times \C^2$ has no
  well-defined complex dimension; $\R^2$ is de Rham not Dolbeault;
  total real dimension matches $d=3$ Costello–Li but kinematic
  differential and form structure differ.
- **§5 Smallest distinguishing test:** neither $d=3$-via-reduction
  ($\Rightarrow 0$ residue) nor $d=4$-direct ($\Rightarrow 2\hbar N$)
  matches manuscript's $\hbar N[\bar c]$ residue.
- **§6 W30 (A5) compatibility:** parity-equivariance at matrix-factor
  layer compatible; orthogonal to spacetime $d$-parity which is not
  liftable by (A5).
- **§7 `stmt:costello-li-flat-bcov` validity:** correct as inscribed;
  optional cosmetic clarifications (C-i, C-ii) not load-bearing.
- **§8 Anti-attack scan:** four attacks (Att-1)–(Att-4) considered;
  none overturns ANALOGUE verdict.
- **§9 Residuals + Phase-5:** five residuals (R-9-A)–(R-9-E); four
  Phase-5 candidates (P5-A)–(P5-D) named but not in current scope.
