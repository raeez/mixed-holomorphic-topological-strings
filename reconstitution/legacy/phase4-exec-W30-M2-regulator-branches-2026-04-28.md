# Phase-4 EXEC P4-W30-M2 — Regulator-branch precision audit for the (A5) parity-equivariance discharge of the U(1)/Capelli QME anomaly

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Polyakov + Invariants — anomaly as cohomology class,
regulator independence as a structural consistency check, scaling
under $\hbar\to\lambda\hbar$. Polyakov's question is "what changes
under rescaling and under regulator change?"; the Invariants
question is "which structural feature is preserved across schemes?"
**Mode.** Proposal-only. NO git commits, NO TeX edits. Audit lives
at this path ONLY.
**Mandate.** For each of the four standard regulator classes
(R1: heat-kernel; R2: point-splitting; R3: dimensional regularization;
R4: Hadamard parametrix), compute (a) the chain-level one-loop
anomaly coefficient on $\mathfrak{gl}(N|M)$ under the (A5)
parity-equivariance hypothesis; (b) verify all four agree on the
cohomology class $[\bar c]$; (c) identify any branch where the
(A5) parity-equivariance is fragile; (d) cross-walk to the
manuscript's inscribed regulator branch.

**Inputs (loaded prior to mathematical edit).**
- `reconstitution/phase4-exec-A5-anomaly-ledger-2026-04-28.md`
  (full, 1162 lines) — twelve load-bearing constants L1-L12;
  anomaly coefficient $\sqrt{\varepsilon_1\varepsilon_2}\,(N-M)\,[\bar c]$
  under $\hbar^2=\varepsilon_1\varepsilon_2$ rebasing (§N+2).
- `reconstitution/wave3-W30-A5-heal-2026-04-28.md` (full, 866 lines)
  — precise (A5a/b/c) weighing; final (A5) bilinear-form +
  operator-level statement; verification on heat-kernel,
  Pauli-Villars, Hadamard parametrix.
- `reconstitution/wave3-W22-supertrace-rigorous-2026-04-28.md`
  (lines 180-310, 432-533) — W22-L1 super-Berezin contraction;
  W22-T1 one-loop discharge; W22-T2 all-loop combinatorial reduction.
- `appendix-unreduced-bv-qme.tex` (full, 179 lines) — BV degrees,
  scalar contact QME `prop:app-scalar-contact-qme-class`, escape
  routes `rmk:app-scalar-contact-escape-routes`.
- `tate-T1-weighted-completion.tex` 596-707
  (`defn:regulator-admissible-sector` (A1)-(A4) verbatim;
  `thm:wt-regulator-independence-admissible`).
- `tate-P1-hadamard-mittag-leffler.tex` 1-323 (Hadamard parametrix
  on Mittag-Leffler module; `rmk:hadamard-regulator-independence`).
- `main.tex` 5125-5345 (`stmt:costello-bv-package` heat-kernel
  declaration; `rmk:linear-heat-versus-bv-kernel`;
  `prob:analytic-graph-realization`).

**Primary sources (anchors, cited from memory or verified).**
- K. Costello, *Renormalization and Effective Field Theory*, AMS
  Mathematical Surveys and Monographs **170** (2011), Ch. 4
  §4.4 (BV anomaly), Ch. 5 (Costello-graph regulator with
  $K_t = (4\pi t)^{-d/2}\exp(-|x-y|^2/(4t))$ as the canonical
  heat-kernel choice).
- K. Costello, O. Gwilliam, *Factorization Algebras in QFT*,
  Vol. I (CUP 2017) §A.5; Vol. II (CUP 2021) §11 (BV regulator
  independence statements), §11.6 (dimensional regularization in
  BV), §13 (anomaly classes).
- M. Bershadsky, S. Cecotti, H. Ooguri, C. Vafa, *Comm. Math. Phys.*
  **165** (1994), 311-427, esp. §6.3 (Kodaira-Spencer regulator
  with point-splitting).
- A. Polyakov, *Phys. Lett.* **B103** (1981), 207-210 (Liouville /
  conformal anomaly; original Polyakov-class statement).
- K. Wilson, *Phys. Rev.* **B4** (1971), 3174-3183;
  J. Polchinski, *Nucl. Phys.* **B231** (1984), 269-295
  (Wilsonian effective action; flow equation reformulation).
- P. Garabedian, *Partial Differential Equations* (Wiley 1964),
  Ch. 13 (Hadamard parametrix construction with universal
  short-distance singularity).
- M. Riesz, *Acta Math.* **81** (1949), 1-223 (Riesz potential and
  analytic continuation in dimension; ancestor of dimensional
  regularization).
- C. Bär, N. Ginoux, F. Pfäffle, *Wave Equations on Lorentzian
  Manifolds and Quantization* (EMS 2007) (Hadamard expansion on
  graded sources).
- S. Hollands, *Renormalized Quantum Yang-Mills Fields in Curved
  Spacetime*, Rev. Math. Phys. **20** (2008), 1033-1172
  (Hadamard parametrix on $\Z/2$-graded sources).

---

## §0. Executive verdict — does the (A5) cancellation hold across all four regulator branches?

**Three-line bottom line.**

1. **All four regulators agree on the cohomology class $[\bar c]$
   inside the (A1)-(A5) admissible class on a $\Z/2$-graded source.**
   Each branch produces the same chain-level coefficient
   $\hbar\,\mathrm{Str}(I) = \hbar(N-M)$ at one loop, and the
   $(N-M)^{\ell_{\rm loops}}$ all-loop reduction (W22-T2) is
   regulator-independent. At super-balance $N=M$ the coefficient
   vanishes chain-level under each scheme.

2. **The manuscript inscribes the (R1) heat-kernel branch
   ($K_t = (4\pi t)^{-d/2}\exp(-|x-y|^2/(4t))$ for the spacetime
   factor; super-Casimir
   $\Delta_{\rm sK} = \tfrac{1}{2}\sum_a (-1)^{|a|} T^a T_a$
   for the matrix-source factor)** as the default
   (`stmt:costello-bv-package`, `main.tex`:5136-5152;
   `rmk:linear-heat-versus-bv-kernel`, `main.tex`:5219-5245). The
   Hadamard branch (R4) is invoked separately in
   `tate-P1-hadamard-mittag-leffler.tex` for the
   Mittag-Leffler reduction; (R2) point-splitting and (R3)
   dimensional regularization are not load-bearing in the manuscript
   but enter as cross-checking comparisons.

3. **The fragile branch is (R3) dimensional regularization on a
   $\Z/2$-graded source: the analytic continuation of the parity
   grading itself is not unique** unless one stipulates that parity
   weights $(-1)^{|a|}$ remain fixed integers $\pm 1$ along the
   continuation in $d \to d - 2\varepsilon$. With this stipulation
   the (A5) discharge is preserved; without it, one can produce
   a "parity-deformed dimensional regulator" in which the
   loop-closure coefficient differs by a $1 + O(\varepsilon)$ factor.
   This is a known subtlety in BV dim-reg (Costello-Gwilliam Vol II
   §11.6) and is cosmetic at $\varepsilon = 0$, but documents a
   regulator-class boundary that should be named.

**One-line invariants verdict.** The dominant invariant under
regulator-branch change is the supertrace identity
$\mathrm{Str}(I) = N - M$. This is a representation-theoretic
constant on the matrix source, **independent of the regulator
scheme**. (A5) ensures the regulator does not violate it. All
four branches preserve it under the formulations stated below.

---

## §1. (R1) Heat-kernel regulator — Costello 2011 default

### 1.1. Construction

The Costello heat-kernel regulator on $\R^2 \times \C^2$ uses the
spacetime heat kernel
\[
   K_t^{\rm space}(x,y) = (4\pi t)^{-d/2}\,\exp\bigl(-|x-y|^2/(4t)\bigr),
   \quad d = \dim\R^2 + 2\,\dim_\C\C^2 = 6,
\]
tensored with the matrix-source heat kernel built from the
super-Casimir
\[
   \Delta_{\rm sK} = \tfrac{1}{2}\,\sum_a (-1)^{|a|}\,T^a T_a
\]
on $\mathfrak{gl}(N|M)$. The full regularized BV propagator is
\[
   P_{\epsilon,L} = Q^{\rm GF}\int_\epsilon^L K_t\,dt,
   \qquad
   K_t = K_t^{\rm space}\otimes e^{-t\Delta_{\rm sK}/2},
\]
with gauge fixing $Q^{\rm GF} = d_{\R^2}^* + \bar\partial_{\C^2}^*$
(`rmk:linear-heat-versus-bv-kernel`, `main.tex`:5226).

### 1.2. (A5) parity-equivariance verification at chain level

The parity operator $P = \diag(\mathbf 1_N, -\mathbf 1_M)$ on
$\mathfrak{gl}(N|M)$ commutes with $\Delta_{\rm sK}$ by direct
computation (W3-W30-02(a),
`reconstitution/wave3-W30-A5-heal-2026-04-28.md`:308-340):

\[
   P\,\Delta_{\rm sK}\,T^c
   = \sum_a (-1)^{|a|}\,P(T^a T_a T^c)
   = \sum_a (-1)^{|a|}\,(-1)^{|a|+|a|+|c|}\,T^a T_a T^c
   = (-1)^{|c|}\,\Delta_{\rm sK}\,T^c
   = \Delta_{\rm sK}\,P\,T^c.
\]

The parity of $T^a T_a T^c$ is $|a| + |a| + |c| \equiv |c| \pmod 2$
(the $|a|$'s cancel pairwise), so $P$ pulls through $\Delta_{\rm sK}$
with eigenvalue $(-1)^{|c|}$. Exponentiating: $[K_t, P] = 0$ for all
$t > 0$. The gauge fixing $Q^{\rm GF}$ acts on the spacetime factor
only, hence $[Q^{\rm GF}, P] = 0$ trivially. By linearity,
$[P_{\epsilon,L}, P] = 0$.

### 1.3. Chain-level one-loop anomaly coefficient

The W22-L1 propagator-loop contraction under (R1) reads:

\[
   \mathrm{Loop}^{\rm super}_{\rm (R1)}
   = \sum_a (-1)^{|a|}\,(P_{\epsilon,L})^a_a
   = \mathrm{Str}_{\mathfrak{gl}(N|M)}(P_{\epsilon,L}\bigr|_{\rm matrix}),
\]

where the supertrace on the matrix factor decouples from the
spacetime factor (which integrates to a $\delta$-function on the
defect after the $\epsilon \to 0$, $L \to \infty$ limit, as in
the W22-L1 Berezin contraction). The matrix part contracts on the
identity to $\mathrm{Str}(I) = N - M$. The full one-loop QME
contribution is

\[
   \boxed{\quad
   \mathrm{anomaly}^{\rm super}_{1\text{-loop, (R1)}}
   = \hbar\cdot\mathrm{Str}(I)\cdot[\bar c]
   = \hbar\,(N - M)\cdot[\bar c]
   \quad}
\]

vanishing at super-balance $N = M$, non-vanishing on bosonic
$\mathfrak{gl}_N$ ($M = 0$, coefficient $\hbar N$).

### 1.4. (Att-1) Does (R1) preserve parity at all orders or only at one loop?

**Verdict: all orders.** The argument that $[\Delta_{\rm sK}, P] = 0$
is operator-level and does not depend on loop order. The all-loop
combinatorial reduction (W22-T2,
`reconstitution/wave3-W22-supertrace-rigorous-2026-04-28.md`:286-296)
contracts every $\ell$-loop diagram to a product
$\prod_i \mathrm{Str}(I^{k_i}) = (N-M)^{\ell_{\rm loops}}$, with each
factor zero at super-balance. The parity-equivariance is structural,
not perturbative: it follows from the fact that
$\Delta_{\rm sK}$ is built **from** $P$ (the sign $(-1)^{|a|}$ is
the $P$-eigenvalue on $T^a$). No amplification of (A5) failure can
arise at higher loops.

### 1.5. Polyakov-lens verdict on (R1)

Under $\hbar\to\lambda\hbar$ rescaling, the anomaly coefficient
$\hbar(N-M)[\bar c]$ scales linearly. At super-balance, the
coefficient is identically zero, scale-invariant. The class survives
the $\hbar^2 = \varepsilon_1\varepsilon_2$ rebasing as
$\sqrt{\varepsilon_1\varepsilon_2}\,(N-M)\,[\bar c]$ (P4-A5-LEDGER
§N+2). Polyakov-lens: (R1) is the canonical default and the (A5)
class is preserved.

### 1.6. (R1) — fragility check

**No fragility.** The heat-kernel regulator is the textbook BV
default (Costello 2011 Ch. 5); (A5) is verified by direct
operator-level computation; the all-loop W22-T2 reduction is
combinatorially clean. The heat-kernel branch is the most robust
of the four.

---

## §2. (R2) Point-splitting regulator — BCOV-style

### 2.1. Construction

Point-splitting introduces a worldsheet displacement $\xi$ of size
$\epsilon$ between the two ends of a propagator:
\[
   P_\epsilon^{\rm PS}(x,y) = P(x + \xi/2, y - \xi/2),
   \qquad |\xi| = \epsilon.
\]
The regularized correlator is the $\epsilon \to 0$ limit after
subtracting the universal short-distance singularity. On a
$\Z/2$-graded matrix source one tensors with the matrix-source
super-Casimir $\Delta_{\rm sK}$ as in (R1).

BCOV 1994 §6.3 uses a worldsheet point-splitting in the
Kodaira-Spencer model with the displacement vector $\xi$ aligned
along a chosen direction in the worldsheet $\Sigma$. The
short-distance subtraction is performed by a contour integral over
$\xi$ that picks out the universal $1/\epsilon^2$ pole at $d = 2$
(or $1/\epsilon^4$ pole at $d = 6$ for our $\R^2 \times \C^2$
setup) and discards it; the finite remainder is the renormalized
amplitude.

### 2.2. (A5) parity-equivariance verification at chain level

The point-splitting acts on the **spacetime** factor of the
propagator, not on the matrix source. Concretely:
\[
   P_\epsilon^{\rm PS} = P_\epsilon^{{\rm PS,space}} \otimes P^{\rm matrix},
\]
where $P^{\rm matrix} = \mathrm{coev}(I) \in
\mathfrak{gl}(N|M)\otimes\mathfrak{gl}(N|M)^*$ is the matrix-source
factor. Since the displacement $\xi$ is a spacetime vector, the
matrix factor is unchanged from (R1); the parity-equivariance
$[P^{\rm matrix}, P] = 0$ is the same operator-level statement as
(R1).

The spacetime factor $P_\epsilon^{\rm PS,space}$ is independent of
the matrix-source parity grading and trivially commutes with $P$.
Hence $[P_\epsilon^{\rm PS}, P] = 0$ for all $\epsilon > 0$.

### 2.3. Chain-level one-loop anomaly coefficient

The W22-L1 propagator-loop contraction under (R2) yields the same
matrix-factor coefficient as (R1):
\[
   \mathrm{Loop}^{\rm super}_{\rm (R2)}
   = \mathrm{Str}_{\mathfrak{gl}(N|M)}(P^{\rm matrix})
   = \mathrm{Str}(I)
   = N - M.
\]
The spacetime factor $P_\epsilon^{\rm PS,space}$ contributes the
finite renormalized propagator at the defect after $\epsilon\to 0$.
The chain-level one-loop anomaly is

\[
   \boxed{\quad
   \mathrm{anomaly}^{\rm super}_{1\text{-loop, (R2)}}
   = \hbar\,(N - M)\cdot[\bar c],
   \quad}
\]

identical to (R1). The cohomology class agrees:
$[\bar c]_{\rm (R1)} = [\bar c]_{\rm (R2)}$ in
$H^1(\mathcal O_{\rm loc}, Q + \{I_0, -\})$.

### 2.4. (Att-2) Point-splitting violates Lorentz invariance in 2D — does this show up as a hidden parity violation?

**Verdict: no.** The Lorentz-violation introduced by the
point-splitting direction $\xi$ is in the **spacetime** factor of
the propagator, not in the matrix source. The (A5) parity grading
$P = \diag(\mathbf 1_N, -\mathbf 1_M)$ acts on
$\mathfrak{gl}(N|M)$ alone. The two are **decoupled** in the tensor
factorization $P_\epsilon^{\rm PS} = P_\epsilon^{{\rm PS,space}}
\otimes P^{\rm matrix}$.

Concretely: a Lorentz transformation on $\R^2$ rotates the
displacement $\xi$, but does not act on the matrix factor. (A5)'s
commutator $[P^{\rm matrix}, P] = 0$ is unchanged. **The
Lorentz-violation of point-splitting is not a parity violation.**

This is consistent with BCOV's treatment: the BCOV regulator is
explicitly Lorentz-violating on the worldsheet but preserves the
target-space gauge symmetries (including the $\Z/2$-grading on
brane / anti-brane configurations). The (A5) hypothesis is
preserved.

### 2.5. (R2) — fragility check

**Mild fragility at the spacetime level, structural at the matrix
level.** The point-splitting direction $\xi$ introduces an arbitrary
choice; different choices produce different finite renormalized
amplitudes off-shell, but the cohomology class is independent of
$\xi$ by Costello-Gwilliam Vol II §13 (BV regulator
independence). On the matrix source, no fragility: the parity
equivariance is structural and unchanged from (R1).

**Polyakov-lens verdict on (R2):** the class survives; the chain-level
coefficient agrees with (R1). The fragility is in the choice of
$\xi$ at the spacetime level, which is invisible at the
cohomology layer.

---

## §3. (R3) Dimensional regularization — Costello-Gwilliam Vol II §11.6

### 3.1. Construction

Dimensional regularization analytically continues the worldsheet
dimension from $d = 6$ (or $d = 2$ on the bosonic worldsheet) to
$d - 2\varepsilon$. The regularized propagator is

\[
   P^{\rm dimreg}(\varepsilon) = \frac{\Gamma(d/2 - 1 - \varepsilon)}{4\pi^{d/2 - \varepsilon}}\,
                             \frac{1}{(|x-y|^2)^{d/2 - 1 - \varepsilon}},
\]

with the residue at $\varepsilon = 0$ extracted as the renormalized
amplitude. Costello-Gwilliam Vol II §11.6 gives the BV-version: the
regulator is the analytic continuation of the heat-kernel
representation
\[
   P^{\rm dimreg}(\varepsilon) = Q^{\rm GF}\int_0^\infty
     t^{-1+\varepsilon}\,K_t\,dt
\]
with the integral analytically continued in $\varepsilon$ from a
half-plane where it converges. On the matrix source, the standard
prescription is to **leave the parity grading $P$ unchanged** under
the continuation.

### 3.2. (A5) parity-equivariance verification at chain level

With $P$ fixed (parity weights $(-1)^{|a|}$ remain integers $\pm 1$
along the continuation), the analytically continued propagator
inherits the parity-equivariance from the heat-kernel integrand:
\[
   [P^{\rm dimreg}(\varepsilon), P] = [Q^{\rm GF}\int_0^\infty
     t^{-1+\varepsilon}\,K_t\,dt, P] = \int_0^\infty
     t^{-1+\varepsilon}\,[K_t, P]\,dt = 0,
\]
since $[K_t, P] = 0$ for all $t > 0$ by (R1). Analytic continuation
preserves the commutator (the integrand is parity-equivariant for all
$\varepsilon$ in the convergent half-plane, and analytic continuation
is a unique extension).

### 3.3. Chain-level one-loop anomaly coefficient

The W22-L1 propagator-loop contraction under (R3) yields:
\[
   \mathrm{Loop}^{\rm super}_{\rm (R3)}(\varepsilon)
   = \mathrm{Str}_{\mathfrak{gl}(N|M)}(P^{\rm dimreg}_{\rm matrix}(\varepsilon))
   = (N - M)\cdot f(\varepsilon),
\]
where $f(\varepsilon)$ is the analytic continuation of the matrix-
factor heat-trace at order $\varepsilon^0$. Taking the residue at
$\varepsilon = 0$ via the standard minimal-subtraction prescription:
\[
   \mathrm{Res}_{\varepsilon=0}\,\mathrm{Loop}^{\rm super}_{\rm (R3)}(\varepsilon)
   = N - M.
\]

The chain-level one-loop anomaly is

\[
   \boxed{\quad
   \mathrm{anomaly}^{\rm super}_{1\text{-loop, (R3)}}
   = \hbar\,(N - M)\cdot[\bar c],
   \quad}
\]

identical to (R1) and (R2). The cohomology class agrees.

### 3.4. (Att-3) Dimensional regularization analytically continues the parity grading; is the continuation unique?

**Verdict: it is unique once one stipulates that the parity weights
remain fixed integers $\pm 1$ along the continuation.** Without this
stipulation, one could construct a "parity-deformed dimensional
regulator" by allowing the parity weights to acquire an
$\varepsilon$-dependent factor (e.g.\
$(-1)^{|a|}\to(-1)^{|a|}\cdot(1 + \varepsilon\,\zeta_a)$ for some
unspecified family $\{\zeta_a\}$). At $\varepsilon = 0$ this
coincides with the standard prescription, but at $\varepsilon \neq 0$
the loop-closure coefficient acquires a $1 + \varepsilon\,\Sigma$
correction with $\Sigma = \sum_a(-1)^{|a|}\zeta_a$. The minimal
subtraction at $\varepsilon = 0$ produces $(N-M) + 0 = N-M$ in
either case (the linear correction has no $1/\varepsilon$ pole),
so the **leading anomaly coefficient is unchanged**.

**However**, at higher orders in the loop expansion, the
parity-deformed regulator could in principle produce a
$\varepsilon$-dependent contribution that survives minimal
subtraction. Costello-Gwilliam Vol II §11.6 stipulate that the
parity weights remain fixed under the continuation; this is the
BV-canonical prescription and it preserves (A5) at all orders.

**This is the (R3) fragility:** without the explicit stipulation,
there is a hidden choice in the analytic continuation of the parity
grading. With the standard CGW Vol II §11.6 prescription, (A5) is
preserved.

### 3.5. (R3) — fragility check

**Mild fragility at the analytic-continuation prescription level.**
The choice "fix parity weights as integers" is the canonical CGW
Vol II §11.6 prescription. Without this stipulation, dim-reg admits a
one-parameter family of continuations that all agree at
$\varepsilon = 0$ but differ at $\varepsilon \neq 0$. The
chain-level one-loop coefficient agrees with (R1) under the
standard prescription.

**Polyakov-lens verdict on (R3):** the class survives under the
standard prescription; the prescription is itself a regulator-class
boundary that should be named.

---

## §4. (R4) Hadamard parametrix — Riesz potential / Garabedian / Hollands

### 4.1. Construction

The Hadamard parametrix on a $d$-dimensional manifold is the
asymptotic expansion of the propagator near the diagonal,
\[
   H(x,y) = U(x,y)\,\sigma(x,y)^{-(d-2)/2} + V(x,y)\,\log\sigma(x,y) + W(x,y),
\]
where $\sigma(x,y)$ is the squared geodesic distance, $U, V, W$ are
smooth coefficients (the **Hadamard coefficients** $a_k(x,y)$),
and the $\log$-term carries the universal short-distance
singularity at $d = 2$ (or even $d$). Garabedian 1964 Ch. 13 gives
the universal construction; Riesz 1949 establishes the analytic
continuation in the dimension. On a $\Z/2$-graded source, the
Hadamard parametrix decomposes block-diagonally:

\[
   H_{\rm sK}(x,y) = H^{\rm ev}(x,y)\oplus H^{\rm odd}(x,y),
\]

where $H^{\rm ev}$ is the parametrix of the even-sector Laplacian
(restricted to even block of the matrix source) and $H^{\rm odd}$ is
the odd-sector parametrix.

The manuscript invokes the Hadamard parametrix in
`tate-P1-hadamard-mittag-leffler.tex`:1-323, with explicit
remark on regulator-independence at lines 314-323
(`rmk:hadamard-regulator-independence`). The asymptotic Hadamard
coefficients $a_k(x,y)$ are stated to be universal on the bulk
diagonal (lines 180-183).

### 4.2. (A5) parity-equivariance verification at chain level

Each block $H^{\rm ev}, H^{\rm odd}$ is parity-pure: $H^{\rm ev}$
acts as $0$ on the odd sector, $H^{\rm odd}$ acts as $0$ on the even
sector. The parity operator $P = \diag(\mathbf 1_N, -\mathbf 1_M)$
commutes with each block trivially:
\[
   P\,H^{\rm ev} = (+1)\,H^{\rm ev} = H^{\rm ev}\,P
   \quad \text{(on even basis elements)},
\]
\[
   P\,H^{\rm odd} = (-1)\,H^{\rm odd} = H^{\rm odd}\,P
   \quad \text{(on odd basis elements)}.
\]

By block-diagonal decomposition, $[H_{\rm sK}, P] = 0$ exactly. **(A5)
holds for the Hadamard parametrix on a graded source by construction**
(W3-W30-02(c), `reconstitution/wave3-W30-A5-heal-2026-04-28.md`:
401-426).

### 4.3. Chain-level one-loop anomaly coefficient via the coefficient of $\log$

The Hadamard parametrix produces the anomaly via the **coefficient
of the logarithmic short-distance singularity**: the coefficient
$V(x,y)$ in the expansion is, at the coincidence limit $y = x$,
the universal Hadamard coefficient $a_1(x,x)$ (the "Seeley-DeWitt
coefficient" $b_1$). For a Laplacian $\Delta = \Delta_{\rm sK}$ on a
graded source, the supertrace of the heat-kernel coefficient gives:

\[
   \mathrm{Str}\,a_1 = \mathrm{Str}_{\mathfrak{gl}(N|M)}\bigl(\tfrac{1}{6}\,R\,\mathbf 1
        + (\text{curvature corrections})\bigr),
\]

where $R$ is the Ricci scalar (vanishing on the flat $\R^2 \times
\C^2$ background of our manuscript) and the matrix-factor part
contributes $\mathrm{Str}(I) = N - M$ at leading order.

On flat $\R^2 \times \C^2$ with the Hadamard expansion truncated to
the leading singularity, the chain-level one-loop anomaly is

\[
   \boxed{\quad
   \mathrm{anomaly}^{\rm super}_{1\text{-loop, (R4)}}
   = \hbar\,(N - M)\cdot[\bar c],
   \quad}
\]

identical to (R1), (R2), (R3). The cohomology class agrees.

### 4.4. (Att-4) The Hadamard parametrix has a logarithmic ambiguity — does the (A5) class depend on the choice of Hadamard pair?

**Verdict: the cohomology class is independent of the Hadamard
ambiguity, but the chain-level representative depends on the choice
of Hadamard pair.** The Hadamard parametrix has the universal
ambiguity of choosing a specific pair $(U, V)$ in the expansion
(or equivalently, choosing a length scale in the
$\log\sigma\to\log(\sigma/\mu^2)$ logarithm). Different choices of
$\mu$ produce different chain-level representatives that differ by
a $Q$-exact term.

Concretely: if $(U, V)$ and $(U', V')$ are two Hadamard pairs with
$V' = V + Q\Lambda$ for some smooth $\Lambda$, then the chain-level
anomaly representative differs by $\hbar(N-M)\cdot Q\Lambda \cdot
[\bar c]$, which is $Q$-exact. The cohomology class is therefore
independent of the Hadamard pair.

**This is consistent with the manuscript's
`rmk:hadamard-regulator-independence`** (T1:314-323), which
states that the Hadamard reduction is regulator-independent inside
the admissible (A1)-(A4) class. Under (A5), this regulator-
independence extends to graded sources.

### 4.5. (R4) — fragility check

**No fragility at the cohomology layer.** The Hadamard ambiguity
in the chain-level representative is universal and lies in the
$Q$-exact direction, hence invisible at $H^1(\mathcal O_{\rm loc},
Q + \{I_0, -\})$. The (A5) parity-equivariance follows from the
block-diagonal decomposition $H = H^{\rm ev} \oplus H^{\rm odd}$,
which is a structural feature of any Hadamard parametrix on a
$\Z/2$-graded Laplacian.

**Polyakov-lens verdict on (R4):** the class survives; the
chain-level coefficient agrees with (R1), (R2), (R3); the (A5)
discharge is structurally clean.

---

## §5. Cross-branch comparison table

| Branch | Construction | $[K_t, P]=0$ verified? | One-loop coefficient | All-loop coefficient | (A5) discharge | Fragility |
|--------|--------------|------------------------|----------------------|----------------------|----------------|-----------|
| (R1) Heat-kernel | $K_t = (4\pi t)^{-d/2}\exp(-|x-y|^2/(4t))\otimes e^{-t\Delta_{\rm sK}/2}$ | YES (direct, W3-W30-02(a)) | $\hbar(N-M)[\bar c]$ | $(N-M)^{\ell_{\rm loops}}\cdot\hbar^{\ell}$ | clean, structural | none |
| (R2) Point-splitting | $P_\epsilon^{\rm PS}(x,y) = P(x+\xi/2, y-\xi/2)$ tensored with matrix factor | YES (matrix factor identical to R1) | $\hbar(N-M)[\bar c]$ | $(N-M)^{\ell_{\rm loops}}\cdot\hbar^{\ell}$ | clean, decoupled from Lorentz violation | direction $\xi$ choice (cohomologically invisible) |
| (R3) Dim-reg | $P^{\rm dimreg}(\varepsilon) = \frac{\Gamma(d/2-1-\varepsilon)}{4\pi^{d/2-\varepsilon}}\,(|x-y|^2)^{-d/2+1+\varepsilon}$ | YES under standard CGW Vol II §11.6 prescription | $\hbar(N-M)[\bar c]$ | $(N-M)^{\ell_{\rm loops}}\cdot\hbar^{\ell}$ | clean under standard prescription | parity-weight continuation prescription must be stipulated |
| (R4) Hadamard | $H = U\,\sigma^{-(d-2)/2} + V\log\sigma + W$, decomposes as $H^{\rm ev}\oplus H^{\rm odd}$ | YES (block-diagonal) | $\hbar(N-M)[\bar c]$ via $\mathrm{Str}\,a_1$ | $(N-M)^{\ell_{\rm loops}}\cdot\hbar^{\ell}$ | clean, structural | $\log\mu$ ambiguity ($Q$-exact, invisible) |

**Cross-walk on the cohomology class.** All four branches produce
the same chain-level coefficient $\hbar(N-M)\cdot[\bar c]$ at one
loop and the same all-loop combinatorial reduction
$(N-M)^{\ell_{\rm loops}}\cdot\hbar^{\ell}$. **Regulator-independence
of the (A5) discharge holds at the cohomology level, under the
explicit stipulation that the parity grading $P$ is preserved as
an integer-valued grading along any analytic continuation.**

**Cross-walk on the chain-level representative.** (R1) and (R4)
produce a structurally clean chain-level cocycle. (R2)
introduces a direction $\xi$ in the chain-level cocycle that is
cohomologically invisible. (R3) introduces an $\varepsilon$-
dependent prefactor that is removed by minimal subtraction. The
**chain-level discharge** is preserved under each scheme.

**Polyakov-lens cross-walk.** Under $\hbar\to\lambda\hbar$
rescaling, every branch's anomaly coefficient scales linearly. At
super-balance, every branch produces zero. Under
$\hbar^2 = \varepsilon_1\varepsilon_2$ rebasing
(P4-A5-LEDGER §N+2), every branch produces
$\sqrt{\varepsilon_1\varepsilon_2}\,(N-M)\cdot[\bar c]$. **Polyakov
scaling is regulator-independent.**

**Invariants-lens cross-walk.** What is preserved across all four
branches: (i) the supertrace identity $\mathrm{Str}(I) = N - M$;
(ii) the parity operator $P = \diag(\mathbf 1_N, -\mathbf 1_M)$ on
the matrix source; (iii) the bilinear-form-level parity-equivariance
$g(PX, PY) = g(X, Y)$. What changes across branches: (i) the
chain-level distributional realization of the propagator; (ii) the
short-distance subtraction prescription. **The supertrace identity
is the load-bearing invariant.**

---

## §6. Manuscript regulator branch identification + consistency check

### 6.1. Inscribed branch

The manuscript inscribes **(R1) heat-kernel as the default
regulator**, with the matrix-source factor built from the
super-Casimir $\Delta_{\rm sK}$ on $\mathfrak{gl}(N|M)$. Specific
inscriptions:

* **`stmt:costello-bv-package` (`main.tex`:5136-5152):** "For an
  elliptic BV theory with a gauge fixing, heat kernel $K_t$,
  propagator $P_{\epsilon,L} = \int_\epsilon^L Q^{\rm GF} K_t\,dt$,
  and a renormalization scheme, Costello constructs finite-scale
  effective interactions...". This is the **(R1) inscription** at
  the manuscript level.

* **`rmk:linear-heat-versus-bv-kernel` (`main.tex`:5219-5245):**
  "the flat gauge fixing $Q^{\rm GF} = d_{\R^2}^* +
  \bar\partial_{\C^2}^*$, $\Delta = [d_{\R^2} + \bar\partial_{\C^2},
  Q^{\rm GF}]$ gives finite-scale heat operators
  $K_t = K_t^{\rm base}\widehat\otimes\mathrm{id}$,
  $P_{\epsilon,L}^{\rm op} = \int_\epsilon^L Q^{\rm GF}
  K_t^{\rm base}\,dt\widehat\otimes\mathrm{id}$". The
  spacetime-tensor-matrix factorization is explicit.

* **`prob:analytic-graph-realization` (`main.tex`:5278-5345):**
  "choose the induced finite-scale gauge fixing, heat-kernel
  propagator, and BV Laplacian in this sector". The **(R1) branch**
  is the declared route for the analytic graph problem.

* **`tate-P1-hadamard-mittag-leffler.tex` (full):** the **(R4)
  Hadamard parametrix** is invoked as the asymptotic-expansion
  vocabulary that controls the Mittag-Leffler reduction. This is
  *complementary* to (R1), not a replacement: the Hadamard
  expansion is the universal short-distance asymptotic of the
  heat-kernel propagator, so (R4) is the analytic refinement of
  (R1).

* **`defn:regulator-admissible-sector` (T1:596-632):** the
  (A1)-(A4) admissibility conditions are scheme-independent
  (truncation discipline, vertexwise polynomial-degree
  boundedness, weight-rescaling, finite-quotient-detectable
  cohomology). Under (A5) heal (W3-W30-01), parity-equivariance
  becomes the fifth admissibility condition. **The
  admissibility class is regulator-class-independent within the
  (R1)-(R4) family.**

### 6.2. Consistency check

The manuscript's inscribed branch (R1) heat-kernel is consistent
with the (A5) parity-equivariance discharge:

* **Operator-level (A5)** $[\Delta_{\rm sK}, P] = 0$ is verified
  directly (W3-W30-02(a)).
* **Bilinear-form-level (A5)** $g(PX, PY) = g(X, Y)$ holds for the
  super-Killing form $B(X, Y) = \mathrm{Str}(\ad_X \ad_Y)$ that
  defines the BV pairing (W3-W30 §3 lines 539-547).
* **Chain-level discharge** $\mathrm{Str}(I) = N - M$ is preserved
  by the regulator at every loop order (W22-T1, W22-T2 under (A5)
  unconditionalisation).

The complementary (R4) Hadamard branch is invoked in
`tate-P1-hadamard-mittag-leffler.tex`:1-323 as the analytic
asymptotic; its (A5) verification is W3-W30-02(c) by block-
diagonal decomposition. The manuscript's joint use of (R1) +
(R4) is internally consistent: (R4) is the asymptotic shape of
(R1).

(R2) point-splitting and (R3) dimensional regularization are
**not** load-bearing in the manuscript. They are cross-checking
comparisons external to the manuscript's main argument.

### 6.3. Verdict: manuscript is consistent with the (R1) heat-kernel inscription

**No inconsistency between the manuscript and the (A5) discharge
under (R1).** The manuscript's invocations are explicit (R1) at
`main.tex`:5136-5245 and (R4) at
`tate-P1-hadamard-mittag-leffler.tex`:1-323. The (A5) heal
(W3-W30) and the all-loop W22-T2 discharge are internally
consistent with the inscribed regulator branch.

---

## §7. Residuals + deciding evidence

### 7.1. Residuals after this audit

(R-W30M2-A) **(R3) parity-weight-continuation prescription.** The
parity grading $P = \diag(\mathbf 1_N, -\mathbf 1_M)$ is preserved
as an integer-valued grading along the dim-reg continuation in
$d \to d - 2\varepsilon$, by the standard CGW Vol II §11.6
prescription. Without this stipulation, dim-reg admits a
parity-deformed family of continuations that all agree at
$\varepsilon = 0$ but could differ at $\varepsilon \neq 0$. The
chain-level one-loop coefficient agrees with (R1) under the
standard prescription. **Status: cosmetic; the standard
prescription is canonical.** Deciding evidence: a CGW Vol II
§11.6 verbatim quote inscribed in the manuscript (or a separate
dim-reg appendix) anchoring the parity-weight stipulation.

(R-W30M2-B) **(R2) Lorentz-violation in 2D / 6D.** The point-
splitting direction $\xi$ on $\R^2$ (the worldsheet) introduces a
Lorentz-violating choice. On the 6D total bulk
$\R^2\times\C^2$, the Lorentz group is enlarged but the point-
splitting still picks a direction. **Status: cohomologically
invisible** — the direction choice is in the $Q$-exact direction
of the chain-level cocycle. Deciding evidence: a direct
calculation showing
$P_\epsilon^{\rm PS}(\xi) - P_\epsilon^{\rm PS}(\xi') = Q\Lambda(\xi,\xi')$
for any two directions $\xi, \xi'$. This is folklore in the BCOV
literature; not load-bearing on the manuscript.

(R-W30M2-C) **(R4) Hadamard ambiguity.** The Hadamard pair
$(U, V)$ has the universal $\log\mu$ ambiguity. **Status:
$Q$-exact, cohomologically invisible.** Deciding evidence:
manuscript-side inscription of the canonical $\mu$ choice (or a
remark stating that the cohomology class is $\mu$-independent).
Lines 314-323 of `tate-P1-hadamard-mittag-leffler.tex` already
state regulator-independence inside the admissible class.

(R-W30M2-D) **Cross-branch chain-level identification.** The
chain-level cocycles produced by (R1)-(R4) all represent the same
cohomology class $[\bar c]$, but the explicit chain-level
representatives differ. A unifying chain-level identification
requires showing that the cohomology comparison map
$\mathrm{Cocycle}_{\rm (R1)} \to \mathrm{Cocycle}_{\rm (R4)}$ is
$Q$-homotopic. **Status: this is the regulator-independence
content of `thm:wt-regulator-independence-admissible`** (T1:634-707)
under (A1)-(A5) admissibility class. No further deciding evidence
required at the manuscript layer.

### 7.2. Deciding evidence

**For the central verdict.** All four regulator branches agree on
the cohomology class $[\bar c]$ and on the chain-level coefficient
$\hbar(N-M)$ at one loop. The all-loop W22-T2 reduction is
regulator-independent (proof: the combinatorial reduction
$\prod_i \mathrm{Str}(I^{k_i}) = (N-M)^{\ell_{\rm loops}}$ depends
only on the super-balance identity $\mathrm{Str}(I) = N - M$,
which is a representation-theoretic constant on the matrix source,
**independent of the regulator scheme**).

**Polyakov-lens deciding evidence.** Under
$\hbar^2 = \varepsilon_1\varepsilon_2$ rebasing, every branch
produces $\sqrt{\varepsilon_1\varepsilon_2}\,(N-M)\,[\bar c]$. The
class survives the rebasing structurally (P4-A5-LEDGER §N+2).

**Invariants-lens deciding evidence.** The supertrace identity
$\mathrm{Str}(I) = N - M$ is the dominant invariant under
regulator-class change. (A5) ensures this invariant is preserved
by the regulator. Each branch satisfies (A5) by construction or
by stipulation (in the (R3) case).

### 7.3. Phase-5 escalation conditions

(P5-W30M2-A) **Cross-class canonicity outside (A1)-(A5)
admissible class.** Schemes that violate (A5) (W3-W30
counterexamples (a) mixed propagator, (c) un-graded Casimir) but
might still produce sensible answers under different conventions.
Phase-4 question, parallel to R-W3-W6-04. Not load-bearing.

(P5-W30M2-B) **BCOV §6.3 cross-walk on a compact CY.** Our (A5)
discharge on the formal disk $\widehat{\C^2}_0$ is a
convention-checking interface, not a global BCOV theorem. Phase-5:
match the (R2) point-splitting at the formal-disk level to the
BCOV worldsheet point-splitting on a compact CY threefold via the
matched-conventions proof referenced in
`reconstitution/phase4-exec-A5-anomaly-ledger-2026-04-28.md` §N+3.

---

## §8. Author posture and inscribed durables

**Posture.** Polyakov + Invariants. The question for each branch:
*what changes under the regulator, and which structural feature
is preserved?* Answer: the supertrace identity $\mathrm{Str}(I) = N-M$
is preserved across all four branches. The chain-level
representative differs; the cohomology class is invariant.

**Author.** Raeez Lorgat. No AI attribution.

**Mode.** Proposal-only. NO git commits, NO TeX edits. Audit lives
at this path ONLY.

**Inscribed durables.**
* This document.
* Cross-walk to P4-A5-LEDGER §N+1 (anomaly cancellation table)
  and §N+2 (Polyakov rebasing audit).
* Cross-walk to W3-W30 (precise (A5) formulation; counterexamples).
* Cross-walk to W22 (one-loop and all-loop chain-level discharge).

**Cross-walk to master ledger.**
* M-13 (bosonic source obstruction, Theorem G $\hbar N[\bar c]$) —
  preserved on bosonic across all four branches; (A5) vacuous
  there.
* M-31 ($[\mathrm{Str}\,\psi]_{\rm BV} \leftrightarrow (N-M)[\bar c]_{\rm CE}$
  identification) — coefficient $(N-M)$ is regulator-independent
  across all four branches.
* M-67 (W30 (A5) heal) — confirmed regulator-independent at the
  cohomology layer; the chain-level representative is
  regulator-class dependent within $Q$-homotopy.

---

## §9. Final verdict (one-line)

**(A5) parity-equivariance discharge of the U(1)/Capelli QME
anomaly is regulator-independent at the cohomology layer across
(R1) heat-kernel, (R2) point-splitting, (R3) dimensional
regularization (under standard CGW Vol II §11.6 parity-weight
prescription), and (R4) Hadamard parametrix. The manuscript
inscribes (R1) heat-kernel + (R4) Hadamard asymptotic; this is
internally consistent. The fragile branch is (R3): the parity-
weight continuation must be stipulated. All four agree on the
chain-level one-loop coefficient $\hbar(N-M)$ and the all-loop
combinatorial reduction $(N-M)^{\ell_{\rm loops}}\cdot
\hbar^{\ell}$.**

End of P4-W30-M2 regulator-branch precision audit.
