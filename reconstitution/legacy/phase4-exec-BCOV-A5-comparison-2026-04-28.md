# Phase-4 EXEC P4-BCOV-A5 — Chain-level comparison of BCOV 1994 anomaly to our (A5) + (A2$'$) machinery

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Polyakov + Invariants — anomaly as cohomology class,
regulator independence, scaling under specific normalisations.
"What is preserved? What is gauged away? Which class survives the
comparison map?"
**Mode.** Proposal-only. NO git commits, NO TeX edits to manuscript.
Audit lives at this path ONLY.
**Mandate.** Compare the BCOV 1994 chain-level holomorphic anomaly
machinery (Costello–Li 2012 reformulation; Costello–Li 2016 anomaly
cancellation) to the manuscript's (A5) + (A2$'$) discharge of
Theorem G's residue $\hbar N[\bar c]$. Report the comparison map,
the structural firewall, and the smallest matching example or
named obstruction.

**Inputs (loaded prior to mathematical reasoning).**
- `reconstitution/phase4-exec-A5-anomaly-ledger-2026-04-28.md`
  (1162 lines) — twelve load-bearing constants L1–L12; the anomaly
  class $\hbar\,\mathrm{Str}(I)\,[\bar c]$.
- `reconstitution/phase4-exec-A1-hypothesis-audit-2026-04-28.md`
  (976 lines) — (A1)–(A5) plus silent (A2$'$) inheritance graph.
- `reconstitution/phase4-exec-W30-M2-regulator-branches-2026-04-28.md`
  (830 lines) — four-regulator audit (R1)–(R4); all agree on
  $[\bar c]$.
- `reconstitution/wave3-W22-supertrace-rigorous-2026-04-28.md`
  (W22-T1 chain-level one-loop; W22-T2 all-loop on $\mathfrak{gl}(N|N)$).
- `main.tex` 280–470 (Theorem G triplet:
  `thm:u1-center-anomaly`, `thm:u1-center-anomaly-open`,
  `thm:quantum-classical-anomaly`); 5125–5175
  (`stmt:costello-bv-package`, `stmt:costello-li-flat-bcov`);
  5380–5394 (Convention firewall remark); 5890–5915 (Cross-volume
  firewall section).
- `appendix-unreduced-bv-qme.tex` (full, 179 lines).
- `CLAUDE.md` (cross-volume firewall to Vol III
  calabi-yau-quantum-groups).

**Primary external sources cited.**
- M. Bershadsky, S. Cecotti, H. Ooguri, C. Vafa, "Kodaira-Spencer
  theory of gravity and exact results for quantum string amplitudes",
  *Comm. Math. Phys.* **165** (1994), 311–427, arXiv:hep-th/9309140
  — primary BCOV paper; §6 "Holomorphic anomaly equation",
  Eq. (6.10)–(6.12); §8 "Large complex structure limit".
- M. Bershadsky, S. Cecotti, H. Ooguri, C. Vafa, "Holomorphic
  anomalies in topological field theories", *Nucl. Phys.*
  **B405** (1993), 279–304 — companion paper.
- K. Costello, S. Li, "Quantum BCOV theory on Calabi–Yau manifolds
  and the higher genus B-model", arXiv:1201.4501 (2012) — chain-level
  rigorous reformulation of BCOV; Definitions 5.1, 5.7, 5.10 of the
  BCOV BV theory; Theorem 6.6 (quantum master equation modulo
  anomalies).
- K. Costello, S. Li, "Quantization of open-closed BCOV theory, I",
  arXiv:1505.06703 (2015) — open-closed extension on flat $\C^d$
  with $\mathfrak{gl}(N|N)$ open algebra, $d$ odd.
- K. Costello, S. Li, "Anomaly cancellation in the topological
  string", arXiv:1605.09073 (2016) — chain-level anomaly
  cancellation argument; Theorem A on flat $\C^d$.
- K. Costello, *Renormalization and Effective Field Theory*, AMS
  Math. Surveys and Monographs **170** (2011), Ch. 4 §4.4
  (BV anomaly classes).
- E. Witten, "Topological sigma models", *Comm. Math. Phys.*
  **118** (1988), 411–449 — A-model / B-model topological twist.
- A. Polyakov, "Quantum geometry of bosonic strings", *Phys. Lett.*
  **B103** (1981), 207–210 — Liouville / conformal anomaly.

---

## §0. Executive verdict — does (A5) + (A2$'$) match BCOV at one loop on a smallest example?

**Three-line bottom line.**

1. **Verdict: PARTIAL with FIREWALL-PERMANENT structural caveat.**
   On the *intersection* example — flat $\C^2 \subset \C^d$ for $d$
   odd, with open gauge algebra $\mathfrak{gl}(N|N)$ — the BCOV 1994
   one-loop holomorphic anomaly equation, in its Costello–Li 2012
   chain-level reformulation, is **definitionally compatible** with
   our (A5) + (A2$'$) chain-level discharge: both record a class
   $\hbar\,\mathrm{Str}(I)\,[\text{vertex cocycle}]$ that vanishes
   when $\mathrm{Str}(I) = N - M = 0$. The two classes live in
   *different* obstruction complexes and the matching is via
   coefficient-coupling rather than a chain-level isomorphism. The
   Costello–Li 2016 anomaly cancellation argument provides the
   chain-level vertex match for our W22-T1 / W22-T2.

2. **Cross-volume firewall is structurally permanent at the
   load-bearing layer.** BCOV 1994 lives on a *compact* Calabi–Yau
   threefold with a Kähler form and a Beltrami differential
   parameterising deformations of complex structure; our local
   model lives on $\R^2 \times \widehat{\C^2}_0$ formal symplectic
   with a holomorphic symplectic form $\omega = dz_1 \wedge dz_2$
   and **no** Kähler structure, **no** Beltrami differential, and
   **no** compact CY$_3$ datum. The Polyakov-class anomaly cocycle
   $[\bar c]\in H^2_{\mathrm{Lie}}(\bar A,\C)$ is a *Lie-algebraic*
   class on the formal disk; the BCOV anomaly is a *holomorphic
   anomaly* on a compact threefold's moduli space. The smallest
   firewall-lifting candidate is the Costello–Li 2015 / 2016
   open-closed BCOV theory on flat $\C^d$ for $d$ odd — but $d=3$
   (not $d=2$), and the smooth partial sweep through $d=3$ to our
   $d=2$ surface model is governed by the manuscript's existing
   `stmt:costello-li-flat-bcov` (`main.tex`:5155) and
   `rmk:convention-firewall` (`main.tex`:5380–5394).

3. **Smallest matching example.** The flat open-closed BCOV theory
   on $\C^3$ with open algebra $\mathfrak{gl}(N|N)$ (Costello–Li 2015
   Definition 1.1; 2016 Theorem A) computes a one-loop chain-level
   anomaly that vanishes by exactly the coupling
   $\hbar\,\mathrm{Str}(I) = \hbar(N-N) = 0$ on the super-balanced
   probe — which is *the same coefficient mechanism* as our W22-T1.
   The two computations occur in different complexes (BCOV: HCS
   chain-level on $\C^3$; ours: brane-defect chain-level on
   $\R^2 \times \widehat{\C^2}_0$) but share the structural
   common ancestor: $\mathrm{Str}_{\mathfrak{gl}(N|N)}(I) = 0$
   under (A2$'$) via the supertrace's parity-equivariance under (A5).
   This is **not** a chain-level isomorphism; it is a coefficient
   coupling under a structural common ancestor.

**One-line invariant.** The dominant invariant preserved on both
sides under regulator change and rebasing is the
representation-theoretic constant $\mathrm{Str}_{\mathfrak{gl}(N|N)}(I)
= 0$. (A5) + (A2$'$) ensures the regulator preserves this on our
side; the Costello–Li 2015 / 2016 framework makes the parallel
statement on the BCOV side. The cross-volume firewall is permanent
because the underlying *complexes* (HCS vs brane-defect) are
structurally distinct, but the *coefficient mechanism* shares a
common representation-theoretic ancestor.

---

## §1. BCOV 1994 anomaly statement (chain-level via Costello–Li 2012)

### 1.1. BCOV 1994 §6 holomorphic anomaly equation

BCOV 1994 §6 establishes the holomorphic anomaly equation for the
one-loop free energy $F_g(t,\bar t)$ on a compact Calabi–Yau
threefold $X$ with Kähler moduli $(t,\bar t)$. Equation (6.11)
(and its higher-genus generalisation (6.12)) reads
\[
\frac{\partial}{\partial \bar t^{\bar i}}\,F_g(t,\bar t)
\;=\;
\frac{1}{2}\,\bar C_{\bar i}{}^{jk}\Bigl(
D_j D_k F_{g-1}
\;+\;
\sum_{r=1}^{g-1} D_j F_r\,D_k F_{g-r}
\Bigr),
\]
where $\bar C_{\bar i}{}^{jk}$ is the anti-holomorphic Yukawa
coupling, $D_j$ is the Kähler-covariant derivative on the moduli
space, and $F_g$ is the genus-$g$ B-model free energy. At $g=1$
the equation reads
\[
\frac{\partial}{\partial \bar t^{\bar i}}\,F_1
\;=\;
\frac{1}{2}\,\bar C_{\bar i}{}^{jk}\,G_{jk}
\;-\;
\bigl(\tfrac{\chi(X)}{24}-1\bigr)\,G_{i\bar i},
\]
with $G_{jk}$ the Zamolodchikov metric and $\chi(X)$ the Euler
characteristic. The right-hand side is **not** identically zero;
the holomorphic anomaly *is* the assertion that $F_g$ is *not*
holomorphic in the moduli — it has a controlled anti-holomorphic
piece.

### 1.2. Chain-level reformulation (Costello–Li 2012)

Costello–Li 2012 (arXiv:1201.4501) reformulates BCOV theory as a
chain-level BV theory. The central object is the BCOV BV theory
\[
\mathrm{BCOV}(X) \;=\; \mathrm{PV}^{*,*}(X)[[t]],
\]
where $\mathrm{PV}^{*,*}(X) = \Omega^{0,*}(X, \wedge^* TX)$ are
polyvector fields and $t$ is a formal parameter (Costello–Li 2012
Definition 5.1). The classical action is the BCOV action
\[
S_{\mathrm{BCOV}}(\mu)
\;=\;
\frac{1}{2}\,\langle \mu, \bar\partial \mu \rangle
\;+\;
\frac{1}{6}\,\langle \mu, \{\mu, \mu\} \rangle
\;+\;
\cdots,
\]
with $\langle\cdot,\cdot\rangle$ the Calabi–Yau pairing using the
holomorphic volume form $\Omega_X$, and $\{\cdot,\cdot\}$ the
Schouten–Nijenhuis bracket on polyvectors. The Beltrami
differential $\mu \in \Omega^{0,1}(X, TX)$ encodes deformations of
complex structure.

The **one-loop anomaly** is the obstruction to solving the
quantum master equation
\[
(\bar\partial + \{S, -\})\,W \;+\; \hbar\,\Delta W \;=\; 0
\]
modulo $\hbar^2$, where $W$ is the renormalised effective action
and $\Delta$ is the BV Laplacian. The anomaly cohomology class
lives in $H^1(\mathcal{O}_{\mathrm{loc}}(\mathrm{BCOV}(X)),
\bar\partial + \{S, -\})$ and is given (Costello–Li 2012
Theorem 6.6) by the integrated divergence of the Hamiltonian
vector field along the heat kernel; concretely, it pairs with
the Calabi–Yau pairing to yield
\[
[\mathrm{Anomaly}]_{\mathrm{BCOV},\,1\text{-loop}}
\;=\;
\bigl[\hbar\,\mathrm{Tr}_{\mathrm{loop}}(I)\,\bar\partial
\text{-coboundary}\bigr]
\;\in\;
H^1\bigl(\mathcal{O}_{\mathrm{loc}}, \bar\partial + \{S,-\}\bigr).
\]
The coefficient $\mathrm{Tr}_{\mathrm{loop}}(I)$ is the trace of
the identity on the matrix factor of the open algebra inserted
into the loop closure of the BCOV propagator.

### 1.3. BCOV anomaly cohomology class

The **BCOV anomaly cohomology class** is therefore the loop-closure
trace coefficient $\mathrm{Tr}(I)$ paired with the structural
$\bar\partial$-coboundary representative in the BV obstruction
complex. On the closed BCOV side (without an open brane probe),
the class is governed by the Euler characteristic correction
$\chi(X)/24 - 1$ of BCOV 1994 Eq. (6.11). On the open-closed side
(Costello–Li 2015 / 2016), the open-brane probe inserts a matrix
factor $\mathfrak{gl}(N|N)$, and the loop closure on the open
algebra contributes $\mathrm{Str}(I) = N - M$.

**Key Costello–Li 2016 statement (Theorem A).** On flat $\C^d$
for $d$ odd, the open-closed BCOV theory with open algebra
$\mathfrak{gl}(N|N)$ admits a unique (up to BV equivalence)
quantisation in which the one-loop anomaly cancels. The
cancellation mechanism is precisely
$\mathrm{Str}_{\mathfrak{gl}(N|N)}(I) = 0$ on the open-loop
closure.

---

## §2. Our (A5) + (A2$'$) chain-level discharge statement

### 2.1. Manuscript Theorem G triplet

The manuscript inscribes three theorems carrying the U(1) anomaly
class $\hbar N[\bar c]$:

* **`lem:omega-cocycle`** (`main.tex`:284–315). The cocycle
  $\omega(f,g) = [\{f,g\}]_0$ is a Lie 2-cocycle on the polynomial
  Hamiltonian Lie algebra $\mathfrak{h}_{\mathrm{poly}} =
  \C[z_1,z_2]$; on the scalar-reduced quotient
  $\bar A = \mathfrak{h}_{\mathrm{poly}} / \C \cdot 1$, it
  represents a non-trivial class
  $[\bar c] \in H^2_{\mathrm{Lie}}(\bar A, \C)$.

* **`thm:u1-center-anomaly-open`** (`main.tex`:354–393). At finite
  $N$, the trace algebra Lie bracket on
  $\C[\mathfrak{gl}_N \oplus \mathfrak{gl}_N]^{GL_N}$ satisfies
  $\{\mathrm{Tr}\,\phi_1, \mathrm{Tr}\,\phi_2\} = N$ in the unreduced
  ring. The scalar-axis central extension class is the image of
  $[\bar c]$ under the boundary evaluation map
  $\partial_{\mathrm{bb},N}^{\mathrm{full}}: f \mapsto
  \mathrm{Tr}\,f(\phi_1, \phi_2)$.

* **`thm:quantum-classical-anomaly`** (`main.tex`:412–464). The
  classical Poisson cocycle $\omega$ and the quantum Capelli shift
  $\hbar N$ represent the *same* cohomology class
  $[\bar c] \in H^2_{\mathrm{Lie}}(\bar A, \C)$ under
  classical-to-quantum reduction via the Rees deformation
  $U_\hbar(\bar A_{[\bar c]})$.

### 2.2. The chain-level QME obstruction representative

`appendix-unreduced-bv-qme.tex` (lines 93–158) inscribes
`prop:app-scalar-contact-qme-class`:
\[
\mathrm{Ob}_{\mathrm{sc}}(\gamma_{\mathbf 1}; a, f; b, g)
\;=\;
\hbar N\,\omega(f,g)\,\int_\R a(t)b(t)\gamma_{\mathbf 1}(t)\,dt.
\]
The associated graded CE class is $\hbar N[\bar c]$. This class
is **not exact** in the scalar-reduced Hamiltonian source
(`prop:app-scalar-contact-qme-class` proof, lines 144–157;
`rmk:app-scalar-contact-escape-routes`, lines 160–178).

### 2.3. The (A5) + (A2$'$) super-balanced discharge

**(A2$'$) [silent].** On a $\Z/2$-graded super-Lie algebra
$\mathfrak g$, there exists an even non-degenerate ad-invariant
supersymmetric bilinear form $g$ used to construct the BV
pairing. (Audit
`reconstitution/phase4-exec-A1-hypothesis-audit-2026-04-28.md`
§1.6.)

**(A5) [proposed inscription].** With $P =
\mathrm{diag}(\mathbf 1_N, -\mathbf 1_M)$ the parity operator on
$\mathfrak{gl}(N|M)$, the bilinear form $g$ is parity-equivariant:
$g(PX, PY) = g(X, Y)$. The associated regulator data — heat operator
$K_t$, gauge fixing $Q^{\mathrm{GF}}$, regularised propagator
$P_{\epsilon,L} = Q^{\mathrm{GF}}\int_\epsilon^L K_t\,dt$ — commute
with $P$ at the operator level
($[K_t, P] = [Q^{\mathrm{GF}}, P] = [P_{\epsilon,L}, P] = 0$).
On a parity-trivial source, (A5) is vacuous.

**W22-T1 (one-loop, chain-level).** Under (A1)–(A5) plus (A2$'$),
the chain-level QME obstruction on the super-stacked Dirac probe
becomes
\[
\mathrm{Ob}_{\mathrm{sc}}^{\mathrm{super}}
\;=\;
\hbar\,\mathrm{Str}_{\mathfrak{gl}(N|M)}(I)\,
\omega(f,g)\,\int_\R a\,b\,\gamma_{\mathbf 1}\,dt
\;=\;
\hbar(N-M)\cdot\Lambda^{\mathrm{Str}}(\omega).
\]
At super-balance $N = M$, the right-hand side is **chain-level
zero** — not merely a cohomology zero
(`reconstitution/wave3-W22-supertrace-rigorous-2026-04-28.md`
§W3-W22-04, lines 432–533).

**W22-T2 (all-loop, conditional on (A5) + (A2$'$)).** Each
$\ell$-loop diagram contracts to a product
$\prod_i \mathrm{Str}(I^{k_i}) = (N-M)^{\ell_{\mathrm{loops}}}$.
At super-balance, every connected propagator-loop subdiagram
vanishes via L8: $\mathrm{Str}(I^k) = N - M = 0$ for all $k \geq 1$.

### 2.4. The residue class and its class identifications

The "residue $\hbar N[\bar c]$" is, in the manuscript's notation
(`appendix-unreduced-bv-qme.tex`:124), the associated graded CE
class of $\mathrm{Ob}_{\mathrm{sc}}$. Its formal home is
$H^1(\mathcal{O}_{\mathrm{loc}}(\mathcal E_w),
Q + \{I_0, -\})$ — the local-functional QME obstruction complex
inside the admissible regulator class
(`tate-T1-weighted-completion.tex`:596–632
`defn:regulator-admissible-sector`).

**Image identifications.**

* Closed side: $[\bar c] \in H^2_{\mathrm{Lie}}(\bar A, \C)$.
* Open finite-$N$ image: $\mathrm{Tr}(I) \cdot N = N$ on
  bosonic $\mathfrak{gl}_N$ (`thm:u1-center-anomaly-open`).
* Quantum image: $\hbar N$ as the Capelli shift in the
  Weyl-quantised moment relation
  (`thm:quantum-classical-anomaly`).
* Super-extension image: $\hbar(N-M)$ on $\mathfrak{gl}(N|M)$;
  zero at super-balance (W22-T1).

---

## §3. Comparison map under the cross-volume firewall

### 3.1. The structural common ancestor

The matching mechanism is a **representation-theoretic common
ancestor**: both the BCOV anomaly (in its Costello–Li 2015 / 2016
chain-level open-closed extension) and our W22 chain-level
discharge route through the *same coefficient*
\[
\mathrm{Str}_{\mathfrak{gl}(N|M)}(I) \;=\; N - M.
\]
This coefficient is a representation-theoretic constant on the
super-Lie algebra; it is independent of:

(a) the spacetime in which the gauge theory lives (BCOV: $\C^3$ or
    compact CY$_3$; ours: $\R^2 \times \widehat{\C^2}_0$);
(b) the regulator scheme used to define the chain-level
    propagator (R1–R4 ledger of W30-M2);
(c) the choice of vertex cocycle ($[\bar c]$ on
    $\bar A$ for us; the BCOV $\bar\partial$-coboundary class for
    BCOV).

**This is what makes the comparison structurally possible.** Both
sides require an open-loop trace of the identity matrix; both
sides discharge via super-balance. Without (A2$'$) the form $g$
required to construct the BV pairing does not exist; without (A5)
the regulator could mix even and odd sectors.

### 3.2. The comparison map

Define the *coefficient comparison*
\[
\Phi_{\mathrm{coef}}\colon\quad
\hbar\,\mathrm{Str}_{\mathfrak{gl}(N|N)}(I)
\;\longmapsto\;
\hbar\,\mathrm{Str}_{\mathfrak{gl}(N|N)}(I).
\]
This is the *only* map between the two computations that preserves
chain-level structural meaning. It is the identity on
representation-theoretic data and a *coupling-coefficient
intertwiner* between the two distinct obstruction complexes:

* BCOV side: $H^1(\mathcal{O}_{\mathrm{loc}}^{\mathrm{BCOV}}(X),
  \bar\partial + \{S_{\mathrm{BCOV}}, -\})$ on a (compact or flat)
  Calabi–Yau threefold $X$, valued in polyvector fields with the
  Schouten–Nijenhuis bracket.
* Our side: $H^1(\mathcal{O}_{\mathrm{loc}}(\mathcal E_w),
  Q + \{I_0, -\})$ on $\R^2 \times \widehat{\C^2}_0$ formal
  symplectic, valued in Hamiltonian BF fields with the polynomial
  Hamiltonian bracket.

The map $\Phi_{\mathrm{coef}}$ is **not** an isomorphism of
complexes; it is a **coefficient-coupling identification** at the
representation-theoretic layer.

### 3.3. Conditions under which the comparison commutes

The comparison commutes under all of:

(C-1) **Common open algebra.** Both sides use $\mathfrak{gl}(N|N)$
(or, more generally, an algebra in which (A2$'$) holds and the
super-Killing form is non-degenerate; on osp(2N|2N) and q(N) the
parallel structure holds — see P4-EXEC-G3 closure).

(C-2) **Common parity grading.** Both sides take the parity
operator $P = \mathrm{diag}(\mathbf 1_N, -\mathbf 1_M)$ as a
structural symmetry of the open algebra. (A5) is the required
compatibility on our side; the Costello–Li 2015 super-extension
of BCOV requires parity preservation on theirs (Costello–Li
2015 Definition 1.1 implicit; manuscript inscribes this on
`stmt:costello-li-flat-bcov`, `main.tex`:5155).

(C-3) **Common super-balance.** Both sides require $N = M$ for the
chain-level cancellation. On bosonic ($M = 0$), neither side
cancels.

(C-4) **Regulator-class compatibility.** Both sides require a
chain-level regulator that preserves the parity grading. Our
audit (W30-M2, all four regulator branches agree) constructs
this; Costello–Li 2012 / 2015 / 2016 use a heat-kernel
regulator with parity-equivariant matrix factor. **(R1) is
the natural meeting point.**

### 3.4. Does the comparison require the firewall to lift?

**No, and yes — depending on level.**

* **Coefficient level (representation-theoretic):** No. The
  coefficient $\hbar(N-M)$ is independent of the spacetime and the
  vertex cocycle. The firewall is *not load-bearing* for the
  coefficient match.

* **Chain-level (BV complex):** Yes. The two BV complexes are
  structurally distinct (HCS on a CY$_3$ vs brane-defect on
  $\R^2 \times \widehat{\C^2}_0$). A chain-level isomorphism would
  require lifting the firewall — i.e., constructing a
  matched-conventions theorem comparing the two complexes. This
  is *exactly* the cross-volume firewall the manuscript inscribes
  at `main.tex`:5380–5394 (`rmk:convention-firewall`) and
  5890–5915 (`ssec:cross-volume-horizon`).

* **Cohomology-class level:** Conditional on the firewall. The
  match between the BCOV anomaly cohomology class and our
  $[\bar c]$ requires either (i) the firewall to lift via a
  matched-conventions theorem (no such theorem is currently
  inscribed in the manuscript), or (ii) interpretation both sides at the
  *coupling coefficient* level and not as cohomology classes in a
  single complex.

**Verdict.** The manuscript's `stmt:costello-li-flat-bcov` is the
*partial firewall lift* that exists: on flat $\C^d$ for $d$ odd
(specifically $d = 3$), the Costello–Li 2015 quantisation and the
Costello–Li 2016 anomaly cancellation give a chain-level
formulation in which the open-loop $\mathrm{Str}(I)$ appears as the
coefficient. Our $d = 2$ surface model is **not** within their
theorem (the manuscript explicitly notes this at `main.tex`:5163).
The full firewall lift to a chain-level isomorphism between BCOV
on $\C^3$ and our local model on $\R^2 \times \widehat{\C^2}_0$
is a separate Phase-5 obligation, not currently inscribed.

---

## §4. Structural differences inventory (firewall topology)

### 4.1. Spacetime / source

| Feature | BCOV 1994 | Costello–Li 2012/2015/2016 (BCOV-rigorous) | Our manuscript |
|---|---|---|---|
| Spacetime | Compact CY$_3$ | Flat $\C^d$, $d$ odd; or compact CY$_3$ | $\R^2 \times \widehat{\C^2}_0$ formal local |
| Complex dimension | $d_\C = 3$ | $d_\C = 3$ (odd) | $d_\C = 2$ (target); $d_\R = 2$ (worldsheet factor) |
| Form structure | Calabi–Yau volume $\Omega$, Kähler form $J$ | $\Omega$, $J$ on $\C^d$ | Holomorphic symplectic $\omega = dz_1\wedge dz_2$ on $\widehat{\C^2}_0$ |
| Moduli | Kähler moduli $(t,\bar t)$ | Kähler / complex structure moduli on $\C^d$ | $(\varepsilon_1, \varepsilon_2)$ via $\hbar^2 = \varepsilon_1\varepsilon_2$; no Kähler moduli |
| Beltrami differential | $\mu \in \Omega^{0,1}(X, TX)$ | $\mu \in \Omega^{0,1}(\C^d, T\C^d)$ | **None** — no complex-structure deformation parameterised |

### 4.2. Field content

| Feature | BCOV / Costello–Li | Our manuscript |
|---|---|---|
| Closed fields | Polyvector fields $\mathrm{PV}^{*,*}(X)[[t]]$ | Hamiltonian BF: $\alpha \in \widehat{\mathfrak h}[1]$, $\beta \in \widehat{\mathfrak h}^\vee_{\mathrm{cont}}[2]$ |
| Bracket | Schouten–Nijenhuis on polyvectors | Polynomial Hamiltonian bracket $\{f,g\} = \partial_{z_1}f\partial_{z_2}g - \partial_{z_2}f\partial_{z_1}g$ |
| Differential | $\bar\partial$ on Dolbeault | $D = d_{\R^2} + \bar\partial_{\C^2}$ (mixed) |
| Open algebra | $\mathfrak{gl}(N\|N)$ (Costello–Li 2015) | $\mathfrak{gl}_N$ (manuscript core) and $\mathfrak{gl}(N\|N)$ (W22 super-balanced extension) |

### 4.3. Anomaly class topology

| Feature | BCOV / Costello–Li | Our manuscript |
|---|---|---|
| Anomaly home | $H^1(\mathcal{O}_{\mathrm{loc}}^{\mathrm{BCOV}}, \bar\partial + \{S, -\})$ | $H^1(\mathcal{O}_{\mathrm{loc}}(\mathcal E_w), Q + \{I_0, -\})$ |
| Vertex cocycle | $\bar\partial$-coboundary on polyvectors | CE 2-cocycle $[\bar c] \in H^2_{\mathrm{Lie}}(\bar A, \C)$ |
| Non-vanishing cocycle | Yes ($\bar\partial$-class non-trivial) | Yes ($[\bar c]$ non-trivial; `lem:omega-cocycle`) |
| Coefficient | $\mathrm{Tr}(I)$ in closed; $\mathrm{Str}(I) = N-M$ in open-closed | $\mathrm{Tr}(I) = N$ in bosonic; $\mathrm{Str}(I) = N-M$ in super-balanced |
| Cancellation mechanism | $\mathrm{Str}(I) = 0$ on $\mathfrak{gl}(N\|N)$ open algebra | $\mathrm{Str}(I) = N-M = 0$ at super-balance via (A5) + (A2$'$) |

### 4.4. Regulator-class compatibility

| Feature | BCOV / Costello–Li | Our manuscript |
|---|---|---|
| Regulator | Heat-kernel + Schouten Casimir on polyvectors | (A1)–(A5)+(A2$'$) admissible: heat-kernel from super-Killing, PV, Hadamard, dim-reg (parity-fixed) |
| Parity preservation | Costello–Li 2015 implicit (sector-separated) | (A5) explicit: $[K_t, P] = 0$ |
| Bilinear form | Calabi–Yau pairing via $\Omega_X$ | Super-Killing on $\mathfrak{gl}(N\|N)$ via (A2$'$); Lie pairing on $\bar A$ |

### 4.5. Smallest matching example

The smallest pair where both sides compute the same number is the
*open-closed BCOV theory on flat $\C^3$* (Costello–Li 2015) probed
by an open brane on a Lagrangian submanifold $L \subset \C^3$ with
open algebra $\mathfrak{gl}(N|N)$. **At one loop**, the
chain-level anomaly cancellation in Costello–Li 2016 Theorem A
gives
\[
\mathrm{Anomaly}_{\mathrm{BCOV/HCS},\,1\text{-loop}}^{\mathrm{open-closed}}
\;=\;
\hbar\cdot\mathrm{Str}_{\mathfrak{gl}(N|N)}(I)\cdot[\text{HCS vertex}]
\;=\;
0,
\]
which on our side is the W22-T1 chain-level discharge
\[
\mathrm{Ob}_{\mathrm{sc}}^{\mathrm{super}}\big|_{N=M}
\;=\;
\hbar\cdot 0\cdot\Lambda^{\mathrm{Str}}(\omega)
\;=\;
0.
\]
Both vanish via the same coefficient. The BCOV $[\text{HCS vertex}]$
class and our $[\bar c]$ live in different complexes.

---

## §5. Costello–Li 2016 cross-walk

### 5.1. Costello–Li 2016 anomaly cancellation argument

The Costello–Li 2016 (arXiv:1605.09073) anomaly cancellation
argument on flat $\C^d$ for $d$ odd proceeds (sketch):

1. **Setup.** Open-closed BCOV theory on $\C^d$ with open gauge
   algebra $\mathfrak{gl}(N|N)$ and Lagrangian submanifold
   $L \subset \C^d$ supporting the open brane.

2. **One-loop anomaly representative.** Compute the one-loop QME
   obstruction
   \[
   \mathrm{Ob}^{\mathrm{BCOV}}_{1\text{-loop}}
   \;=\;
   \hbar\,\mathrm{Str}_{\mathfrak{gl}(N|N)}(I)\cdot
   [\mathrm{HCS\,vertex}],
   \]
   where the loop closure on the matrix factor produces
   $\mathrm{Str}(I) = 0$ at super-balance.

3. **Class-level vanishing.** The class is identically zero
   because the coupling coefficient is zero. This is the direct
   parallel of W22-T1.

4. **All-loop extension.** Use the supertrace's preservation under
   the Costello–Gwilliam Vol II §11 BV regulator (heat-kernel)
   to extend to all loops. This is the parallel of W22-T2 + W30
   regulator-independence.

### 5.2. Match against W22-T1 / W22-T2

| Step | Costello–Li 2016 | Our W22-T1 / W22-T2 |
|---|---|---|
| (1) Setup | $\mathfrak{gl}(N\|N)$ open on $\C^d$ Lagrangian | $\mathfrak{gl}(N\|N)$ super-stacked Dirac probe on $\R \times \widehat{\C^2}_0$ |
| (2) One-loop coefficient | $\hbar\cdot\mathrm{Str}(I) = 0$ | $\hbar\cdot\mathrm{Str}(I) = 0$ — **MATCH** |
| (3) Class-level vanishing | Direct from coefficient | Direct from coefficient — **MATCH** |
| (4) All-loop extension | Heat-kernel preserves $\mathrm{Str}$ | (A5) preserves $\mathrm{Str}$ on (A1)–(A5) admissible; W22-T2 — **MATCH** |
| Vertex class | $[\mathrm{HCS\,vertex}]$ on $\bar\partial$-cohomology of $\C^d$ | $[\bar c]$ on Lie cohomology of $\bar A$ — **DISTINCT** |

### 5.3. The structural alignment

The Costello–Li 2016 argument *is* a chain-level parallel of our
W22-T1 / W22-T2: same coefficient mechanism, same regulator-class
preservation, same all-loop extension. The structural alignment
is at the *coupling coefficient* + *parity-equivariance regulator*
layer, not at the vertex-class layer.

**The two arguments share:**

* the supertrace vanishing identity $\mathrm{Str}(I) = 0$ on
  $\mathfrak{gl}(N|N)$;
* the regulator-class admissibility framework (Costello 2011 Ch. 4
  / CG Vol II §11);
* the parity-equivariance of the matrix-factor regulator;
* the all-loop closure via the Berezin / supertrace identity
  $\mathrm{Str}(I^k) = N - M$ for all $k \geq 1$.

**The two arguments do not share:**

* the vertex cocycle (BCOV $\bar\partial$-coboundary vs our
  $[\bar c] \in H^2_{\mathrm{Lie}}(\bar A, \C)$);
* the spacetime (CY$_3$ or flat $\C^3$ vs $\R^2 \times \widehat{\C^2}_0$);
* the form structure (Calabi–Yau pairing via $\Omega_X$ vs
  holomorphic symplectic $dz_1 \wedge dz_2$);
* the field content (polyvector fields vs Hamiltonian BF).

**Verdict.** Costello–Li 2016 *matches* our W22-T1 / W22-T2 at the
coefficient and regulator-class level. The match does **not**
extend to a chain-level isomorphism of complexes; it is a
parallel mechanism on parallel structures.

---

## §6. Firewall persistence verdict

### 6.1. Firewall structure

The cross-volume firewall in `CLAUDE.md` and in
`main.tex`:5894 (`ssec:cross-volume-horizon`) is structurally
permanent at the load-bearing layer for three reasons:

(F-1) **Spacetime mismatch.** BCOV is on a CY$_3$ (or flat $\C^3$);
   we are on $\R^2 \times \widehat{\C^2}_0$. The dimensions and
   structure groups do not match.

(F-2) **Form-structure mismatch.** BCOV uses the Calabi–Yau
   holomorphic volume form; we use a holomorphic symplectic form.
   These are not the same datum.

(F-3) **Field-content mismatch.** BCOV fields are polyvector fields
   with the Schouten–Nijenhuis bracket; ours are Hamiltonian BF
   fields with the polynomial Hamiltonian bracket. The brackets
   are structurally distinct.

### 6.2. Conditions under which the firewall lifts

The firewall lifts at a level less than chain-level:

(L-1) **Coefficient level.** The firewall is *not load-bearing* for
   the coefficient match $\hbar(N-M)$. This is a
   representation-theoretic statement on the open algebra,
   independent of the firewall structure.

(L-2) **Regulator-class level.** The firewall is *not load-bearing*
   for the regulator-class compatibility on the matrix factor.
   Both sides use parity-equivariant heat-kernel regulators.

(L-3) **Vertex-class level.** The firewall **is** load-bearing.
   The BCOV vertex class and our $[\bar c]$ live in
   structurally distinct complexes; matching them requires a
   matched-conventions theorem.

(L-4) **Chain-level isomorphism level.** The firewall **is**
   load-bearing. A chain-level isomorphism would require a
   functor between the BCOV BV theory on $\C^3$ (or CY$_3$) and
   our Hamiltonian BF theory on $\R^2 \times \widehat{\C^2}_0$.
   No such functor is currently inscribed in the manuscript.

### 6.3. The Costello–Li 2015 partial lift

The manuscript's `stmt:costello-li-flat-bcov` (`main.tex`:5155–5166)
imports Costello–Li 2015 as the *one* major flat BCOV/HCS instance
that covers part of the cross-volume firewall: open-closed BCOV on
$\C^d$ with $d$ odd and open algebra $\mathfrak{gl}(N|N)$. **This
is a partial firewall lift on the BCOV side, not a chain-level
isomorphism with our model.** The manuscript explicitly notes
(`main.tex`:5163):

> "Ordinary $\mathfrak{gl}_N$ and the mixed $\R^2 \times \C^2$
> Hamiltonian brane model are not covered by this theorem without
> an additional reduction or summand argument."

**Verdict.** **The firewall is structurally permanent at the
chain-level / vertex-class layer; it is operationally lifted at
the coefficient / regulator-class layer.** The
Costello–Li 2015 / 2016 framework provides the closest currently
available partial lift.

### 6.4. Phase-5 obligations for full firewall lift

A full firewall lift (chain-level isomorphism) would require:

(P5-1) A matched-conventions theorem comparing BCOV on $\C^3$ (or
   $\C^d$, $d$ odd) to our Hamiltonian BF on
   $\R^2 \times \widehat{\C^2}_0$, accounting for the
   form-structure shift (Calabi–Yau volume to holomorphic
   symplectic) and the field-content shift (polyvectors to
   Hamiltonian BF).

(P5-2) A reduction argument from $\mathfrak{gl}(N|N)$ to
   $\mathfrak{gl}_N$ (or vice versa), since BCOV's open algebra
   is super-balanced by Costello–Li 2015 while our manuscript's
   default is bosonic with the super-balanced extension as a
   parallel theorem.

(P5-3) A functorial dictionary translating BCOV moduli (Kähler
   $(t, \bar t)$) into our moduli ($\hbar^2 =
   \varepsilon_1\varepsilon_2$ rebasing of G4-M2). The G4-M2
   Heisenberg twist
   (`reconstitution/phase4-exec-G4-M2-Heisenberg-twist-2026-04-28.md`)
   provides a *partial* dictionary; full equivalence is an open
   Phase-5 obligation.

These three Phase-5 obligations are **not currently discharged**
and are the named obstruction to lifting the firewall at the
chain-level / vertex-class layer.

---

## §7. Smallest matching example or named obstruction

### 7.1. Smallest matching example (coefficient + regulator level)

**Example.** On flat $\C^3$ with open algebra
$\mathfrak{gl}(N|N)$, the Costello–Li 2015 / 2016 chain-level
quantisation of open-closed BCOV theory and our W22-T1 chain-level
QME discharge on the super-balanced Dirac probe of
$\R^2 \times \widehat{\C^2}_0$ both compute the same number at one
loop:
\[
\hbar\,\mathrm{Str}_{\mathfrak{gl}(N|N)}(I)\;=\;\hbar(N-N)\;=\;0.
\]

This is the smallest match at the *coefficient* level. The match
is not a chain-level isomorphism; it is a *coupling coefficient
agreement* mediated by the structural common ancestor
$\mathrm{Str}(I) = N - M$ and (A5) + (A2$'$).

### 7.2. Named obstruction at chain-level

**Obstruction.** No matched-conventions theorem exists between:

* (BCOV side) Open-closed BCOV BV theory on $\C^3$ with open
  algebra $\mathfrak{gl}(N|N)$ and Calabi–Yau volume form;
* (Our side) Mixed holomorphic-topological Hamiltonian BF theory on
  $\R^2 \times \widehat{\C^2}_0$ with holomorphic symplectic form
  and super-stacked Dirac probe.

A chain-level isomorphism between these complexes would require
the three Phase-5 obligations (P5-1)–(P5-3) listed in §6.4.
**These are not discharged in the manuscript or in the Phase-4
EXEC ledgers.**

The named obstruction is therefore **the absence of a
matched-conventions functor** between the BCOV BV theory on $\C^3$
(Costello–Li 2012/2015/2016) and our Hamiltonian BF theory on
$\R^2 \times \widehat{\C^2}_0$. This obstruction is **structural,
not technical**: it reflects the form-structure mismatch
(Calabi–Yau volume vs holomorphic symplectic), the field-content
mismatch (polyvectors vs Hamiltonian BF), and the dimension
mismatch ($d_\C = 3$ vs $d_\C = 2$).

### 7.3. Operational interpretation of the obstruction

The chain-level firewall is not a defect of either framework; it
is a **structural feature** of the research constellation. The
manuscript explicitly accommodates this in
`rmk:convention-firewall` (`main.tex`:5380–5394):

> "This local Hamiltonian BF sector is not a compact Calabi-Yau
> output of a $\Phi_d$ functor, [...] and is not evidence for
> compact CY$_3$ BCOV anomaly cancellation. The Moyal computation
> below is local deformation quantization of a formal symplectic
> disk."

The named obstruction is *exactly* the obligation noted in this
remark: a $\Phi_d$ functor (or its analogue) is required to lift
the firewall. **Such a functor is the Phase-5 frontier, not a
Phase-4 obligation.**

---

## §8. Anti-attack scan responses

### 8.1. Att-1: BCOV uses Beltrami $\mu$; we have no Beltrami. Does this break the comparison structurally?

**Verdict: it changes the coefficient layer but not the
representation-theoretic ancestor.**

BCOV 1994 §6 uses the Beltrami differential $\mu \in
\Omega^{0,1}(X, TX)$ to parameterise complex structure
deformations; the holomorphic anomaly equation Eq. (6.11) reads
the obstruction to $\bar\partial$-closedness of the free energy
$F_g(t,\bar t)$ in terms of $\mu$.

Our manuscript has **no Beltrami differential** because we are not
parameterising complex structure deformations of a CY$_3$ — we are
on a *fixed* formal symplectic disk
$(\widehat{\C^2}_0, \omega = dz_1 \wedge dz_2)$. The
manuscript's $\alpha_{\bar z_j}d\bar z_j$ at `main.tex`:1832 is
locally a Beltrami-like field, but it is the *Hamiltonian
connection's anti-holomorphic component on the formal disk*, not
a global Beltrami differential on a compact threefold.

**Why this does not break the comparison.** The Beltrami $\mu$
parameterises the *moduli direction* of the BCOV anomaly equation;
the open-loop matrix-factor coefficient $\mathrm{Str}(I)$ is
*orthogonal* to this moduli parameterisation. Costello–Li 2015 /
2016 establish the matrix-factor coefficient at fixed moduli;
the moduli dependence is what BCOV 1994 §6 is fundamentally
about, but the *one-loop matrix-factor coefficient* is a
structurally separable component.

**On our side**, the absence of Beltrami means we have no analogue
of Eq. (6.11) — we have only the matrix-factor coefficient at
fixed (formal) symplectic structure. The comparison is at the
matrix-factor coefficient level, not at the moduli-equation level.

**Polyakov-lens interpretation.** The Beltrami is the *moduli direction*;
the matrix-factor coefficient is the *symmetry coupling*. Polyakov's
question "what changes under regulator change?" answers identically
on both sides: the matrix-factor coefficient is regulator-invariant.

### 8.2. Att-2: BCOV is one-loop exact on the holomorphic side; we have all-loop $(N-M)^{\ell_{\text{loops}}}\hbar^\ell$ via W22-T2. Are these compatible at one loop?

**Verdict: compatible at one loop; consistent at all loops; the
"one-loop exactness" is a moduli statement, not a chain-level
statement.**

The BCOV "one-loop exactness" is the statement that, on the
holomorphic anomaly equation, the one-loop free energy $F_1$
satisfies a particular form (BCOV 1994 §6.1) and higher-genus
contributions $F_g$ for $g \geq 2$ obey their own anomaly equations
that are *not* governed by $F_1$ alone but by the full Yukawa
coupling structure. **The "one-loop exactness" refers to the
specific structure of $F_1$ in the moduli parameterisation, not
to the BV chain-level anomaly cancellation.**

Costello–Li 2012 / 2015 / 2016, by contrast, work at the
chain-level BV layer, where the one-loop anomaly is the *primary*
QME obstruction and higher-loop anomalies are governed by the
all-order extension of the matrix-factor coefficient. **This is
precisely our W22-T2 setup**: each $\ell$-loop diagram contracts to
a product $\prod_i \mathrm{Str}(I^{k_i}) = (N-M)^{\ell_{\mathrm{loops}}}$.

**At one loop:** Both sides give $\hbar(N-M) = 0$ at super-balance.
**MATCH.**

**At higher loops:** Costello–Li 2016's all-loop extension
parallels our W22-T2. Both rely on $\mathrm{Str}(I^k) = N - M$
preserving zero at every $k$ under super-balance. **MATCH.**

The "one-loop exactness" of BCOV 1994 §6 is in a *different*
direction from what either Costello–Li 2016 or our W22-T2 records:
BCOV 1994's exactness is a moduli-parameterisation statement,
while the chain-level all-loop extension is a propagator-loop
contraction statement. **The two are not in conflict**: they are
about different layers of the BV machinery.

### 8.3. Att-3: BCOV depends on Kähler moduli $(t,\bar t)$; we depend on $(\varepsilon_1, \varepsilon_2)$. Do these match under any limit?

**Verdict: PARTIAL — only via the G4-M2 Heisenberg twist, not at
chain-level.**

The G4-M2 Heisenberg sub-VOA twist
(`reconstitution/phase4-exec-G4-M2-Heisenberg-twist-2026-04-28.md`)
rebases our $\hbar$-deformation parameter onto the
$\Omega$-background couplings via $\hbar^2 = \varepsilon_1\varepsilon_2$.
This matches the standard BCOV / Costello–Gwilliam-Williams
dictionary on the moduli-parameter side.

**Match level.** The match is at the **deformation parameter**
level: $\hbar$ on our side becomes $\sqrt{\varepsilon_1\varepsilon_2}$
in the rebased convention. On the BCOV side, the Kähler moduli
$(t, \bar t)$ enter the holomorphic anomaly equation as
parameterising the metric on moduli space; the
$\Omega$-deformation parameters $(\varepsilon_1, \varepsilon_2)$
in the topological string are the equivariant parameters of the
torus action on the worldsheet.

**Non-match level.** The Kähler moduli $(t, \bar t)$ are
specifically the *moduli of the CY$_3$*; the
$(\varepsilon_1, \varepsilon_2)$ are the *equivariant parameters
of the torus on the worldsheet*. These parameterise *different*
deformations: moduli of the target vs equivariant parameters of
the worldsheet.

**Verdict.** The match is at the deformation-parameter rebasing
level (P4-A5-LEDGER §N+2: anomaly class survives rebasing as
$\sqrt{\varepsilon_1\varepsilon_2}\,(N-M)\,[\bar c]$). It is **not**
a match at the moduli-parameterisation level. The Kähler moduli
$(t, \bar t)$ of BCOV do not have a chain-level analogue in our
local model.

### 8.4. Att-4: Costello–Li 2012's chain-level rigorisation may introduce different (A_k) hypotheses than (A1)–(A5)+(A2$'$). Identify any silent strengthening.

**Verdict: Costello–Li 2012's hypotheses are a structurally
parallel admissibility framework; one silent strengthening
identified on each side.**

**Costello–Li 2012 hypotheses (Definition 5.7).**

(CL-1) Calabi–Yau pairing via $\Omega_X$ on polyvectors.
(CL-2) Heat-kernel regulator preserving the BV pairing.
(CL-3) Cohomological gauge fixing via the divergence operator
       $\partial_\Omega$.
(CL-4) BV admissibility class compatible with the renormalisation
       group flow.

**Our hypotheses (A1)–(A5) + (A2$'$).**

(A1) Truncation discipline (degreewise surjective transitions).
(A2) Vertexwise polynomial-degree-bounded legs.
(A2$'$) Existence of even non-degenerate ad-invariant
        supersymmetric bilinear form (silent).
(A3) Diagonal weight-rescaling.
(A4) Admissible filtered cohomology.
(A5) Parity-equivariance.

**Silent strengthening on Costello–Li side.** The CY pairing
condition (CL-1) presupposes a non-degenerate top-form $\Omega_X$;
on flat $\C^d$ this is $\Omega = dz_1 \wedge \cdots \wedge dz_d$.
On a compact CY$_3$ this is the unique global holomorphic top form
(unique up to scale by Yau's theorem on Calabi–Yau structures).
The "graded extension" of this pairing to the open algebra
$\mathfrak{gl}(N|N)$ uses the supertrace, which **silently
requires (A2$'$)** — the existence of an even non-degenerate
supersymmetric ad-invariant bilinear form. On $\mathfrak{gl}(N|N)$
this is the supertrace pairing $B_0(X, Y) = \mathrm{Str}(XY)$,
which exists tautologically. **Silent strengthening on
Costello–Li side: the implicit (A2$'$).** (Same silent
strengthening as on our side.)

**Silent strengthening on our side.** Our (A1)–(A5) + (A2$'$) is
declared on the manuscript's regulator-class definition
(`tate-T1-weighted-completion.tex`:596–632). The silent
strengthening identified in
`reconstitution/phase4-exec-A1-hypothesis-audit-2026-04-28.md`
§1.7 is the **Costello regulator-class compatibility
meta-hypothesis**: that the Costello 2011 framework (ungraded BV)
extends to graded BV via the supertrace replacement. This is
*verified informally* on three named regulators (W30-M2 ledger)
but is **not formally verified** against Costello 2011 §5.2
graded-case statement.

**Match.** Both sides have the same silent strengthening pattern:

| Side | Silent strengthening |
|---|---|
| Costello–Li 2012/2016 | Implicit (A2$'$) on the open algebra |
| Our manuscript | Implicit (A2$'$); plus Costello regulator-class compatibility on graded sources |

**Verdict.** The hypotheses are *structurally parallel*; both sides
silently strengthen via (A2$'$). Our (A5) is the *operator-level
explicit* version of what Costello–Li 2015 / 2016 implicitly
require (parity-preservation of the heat-kernel regulator on the
matrix factor).

### 8.5. Att-5 (additional): does the comparison involve the cross-volume firewall?

**Verdict: PARTIALLY at chain-level; NO at coefficient level.**

The comparison does involve the firewall *only at the chain-level
isomorphism layer*. The coefficient match $\hbar(N-M) = 0$ is
firewall-independent. The vertex-class match is firewall-dependent.
The full chain-level isomorphism between BCOV BV on $\C^3$ and
Hamiltonian BF on $\R^2 \times \widehat{\C^2}_0$ is the
firewall-permanent obstruction.

**Polyakov interpretation.** Polyakov's question "which class is preserved
across the comparison?" answers: **the coupling coefficient
$\hbar(N-M)$ is preserved**; the vertex cocycle changes
($[\bar c]$ on our side; $\bar\partial$-coboundary on BCOV side);
the ambient complex changes structurally.

**Invariants interpretation.** The dominant invariant under the
comparison is $\mathrm{Str}_{\mathfrak{gl}(N|N)}(I) = 0$, the
representation-theoretic constant on the open algebra. Both sides
preserve it; (A5) + (A2$'$) on our side, Costello–Li 2015 / 2016
on theirs. The firewall does not threaten this invariant.

---

## §9. Residuals + deciding evidence

### 9.1. Residuals

**(R-1) The BCOV moduli equation.** BCOV 1994 §6 holomorphic
anomaly equation involves the Beltrami differential $\mu$ and the
Yukawa coupling $\bar C_{\bar i}{}^{jk}$. Our local model has no
analogue of this moduli-parameterised structure; the comparison
therefore **does not extend** to the moduli direction. The
manuscript's `rmk:convention-firewall` (`main.tex`:5380–5394)
explicitly disclaims this extension. **Residual confirmed.**

**(R-2) The full chain-level isomorphism.** Phase-5 obligations
(P5-1)–(P5-3) listed in §6.4 are not currently discharged.
A full chain-level isomorphism between BCOV BV theory on $\C^3$
and Hamiltonian BF theory on $\R^2 \times \widehat{\C^2}_0$ is
*not* available. **Residual confirmed; this is the named
obstruction.**

**(R-3) The Costello–Li 2012 regulator-class admissibility match.**
Our (A1)–(A5) + (A2$'$) is the manuscript's regulator class.
Costello–Li 2012 Definition 5.7 is theirs. The two are
*structurally parallel* but **not formally identified**. A
matched-conventions audit at the regulator-class level is a
Phase-5 obligation. **Residual confirmed.**

### 9.2. Deciding evidence

The deciding evidence on the comparison verdict is:

(D-1) **Costello–Li 2016 Theorem A.** On flat $\C^d$ for $d$ odd
   with $\mathfrak{gl}(N|N)$ open algebra, the chain-level anomaly
   cancellation argument computes $\hbar\,\mathrm{Str}(I) = 0$ at
   one loop and extends to all loops via the Costello–Gwilliam
   Vol II §11 BV regulator. **This is the BCOV-side chain-level
   parallel of our W22-T1 + W22-T2.**

(D-2) **Our W22-T1 + W22-T2 chain-level discharge.** On
   $\R^2 \times \widehat{\C^2}_0$ super-stacked Dirac probe with
   $\mathfrak{gl}(N|N)$ open algebra under (A1)–(A5) + (A2$'$),
   the chain-level QME obstruction on the super-balanced source is
   $\hbar(N-M) = 0$ at one loop and extends to all loops via L8
   $\mathrm{Str}(I^k) = N - M = 0$ for all $k \geq 1$.

(D-3) **The structural common ancestor.** Both (D-1) and (D-2)
   route through $\mathrm{Str}_{\mathfrak{gl}(N|N)}(I) = 0$ on the
   open-loop closure. (A5) + (A2$'$) on our side, Costello–Li 2015
   / 2016 on theirs.

(D-4) **The cross-volume firewall.** The manuscript's
   `rmk:convention-firewall` and `ssec:cross-volume-horizon`
   declare the firewall structurally permanent at the chain-level
   isomorphism layer. The Costello–Li 2015 partial lift covers
   $d = 3$ on $\mathfrak{gl}(N|N)$ open algebra; our $d = 2$
   surface model is not within their theorem.

### 9.3. Final verdict

**(A5) + (A2$'$) matches BCOV / Costello–Li at the coefficient
level on the smallest example (flat $\C^3$ open-closed BCOV with
$\mathfrak{gl}(N|N)$ open algebra) at one loop, with all-loop
extension parallel to W22-T2 / Costello–Li 2016 Theorem A. The
match is mediated by the structural common ancestor
$\mathrm{Str}_{\mathfrak{gl}(N|N)}(I) = 0$ under (A5) + (A2$'$).**

**The cross-volume firewall is structurally permanent at the
chain-level isomorphism layer.** Lifting it to a chain-level
isomorphism requires Phase-5 obligations (P5-1)–(P5-3). The named
obstruction is the absence of a matched-conventions functor
between BCOV BV theory on $\C^3$ and Hamiltonian BF theory on
$\R^2 \times \widehat{\C^2}_0$.

**Smallest matching example.** Flat $\C^3$ open-closed BCOV /
Costello–Li 2015 / 2016 with $\mathfrak{gl}(N|N)$ open algebra at
super-balance. Both sides compute $\hbar(N-N) = 0$ at one loop.

**Smallest non-match.** Bosonic $\mathfrak{gl}_N$ on either side:
both sides compute non-zero $\hbar N$, but the bosonic comparison
does not invoke (A5) (which is vacuous) or (A2$'$) (which is
trivially satisfied via the Killing form on $\mathfrak{gl}_N$).
The bosonic comparison is a *separate* match that does not
involve the (A5) + (A2$'$) machinery.

**Polyakov + Invariants final interpretation.** The dominant invariant
preserved across the comparison is the representation-theoretic
constant $\mathrm{Str}_{\mathfrak{gl}(N|N)}(I) = 0$. (A5) + (A2$'$)
ensures the regulator preserves this on our side; Costello–Li 2015
/ 2016 ensure it on theirs. The vertex cocycles differ; the
ambient complexes differ; the spacetime / form structure differs.
The match is at the *coefficient* + *regulator-class* layer,
firewall-independent. The match at the *vertex-class* /
*chain-level isomorphism* layer is firewall-dependent and remains
a Phase-5 obligation.

---

## Appendix A — Cross-reference index

| Reference | Manuscript / Ledger location | Used in §§ |
|---|---|---|
| `lem:omega-cocycle` | `main.tex`:284–315 | §2.1, §3.1 |
| `thm:u1-center-anomaly-open` | `main.tex`:354–393 | §2.1 |
| `thm:quantum-classical-anomaly` | `main.tex`:412–464 | §2.1 |
| `prop:app-scalar-contact-qme-class` | `appendix-unreduced-bv-qme.tex`:93–158 | §2.2 |
| `rmk:app-scalar-contact-escape-routes` | `appendix-unreduced-bv-qme.tex`:160–178 | §2.2 |
| `defn:regulator-admissible-sector` | `tate-T1-weighted-completion.tex`:596–632 | §2.4, §8.4 |
| `stmt:costello-bv-package` | `main.tex`:5136–5152 | §1.2 |
| `stmt:costello-li-flat-bcov` | `main.tex`:5155–5166 | §1.3, §3.4, §6.3 |
| `rmk:convention-firewall` | `main.tex`:5380–5394 | §6.1, §7.3, §9.1 |
| `ssec:cross-volume-horizon` | `main.tex`:5894–5914 | §6.1 |
| W22-T1 (chain-level one-loop) | `wave3-W22-supertrace-rigorous-2026-04-28.md` §W3-W22-04 | §2.3, §5.2 |
| W22-T2 (all-loop) | `wave3-W22-supertrace-rigorous-2026-04-28.md` §W3-W22-05 | §2.3, §5.2 |
| L7 / L8 (Str identities) | `phase4-exec-A5-anomaly-ledger-2026-04-28.md` §7, §8 | §2.3, §5.2 |
| L11 / L12 (BV regulator + anomaly class) | `phase4-exec-A5-anomaly-ledger-2026-04-28.md` §11, §12 | §1.3, §3.2 |
| (A2$'$) audit | `phase4-exec-A1-hypothesis-audit-2026-04-28.md` §1.6 | §2.3, §8.4 |
| (A5) audit | `phase4-exec-A1-hypothesis-audit-2026-04-28.md` §1.5 | §2.3, §3.3 |
| Costello regulator-class meta-hypothesis | `phase4-exec-A1-hypothesis-audit-2026-04-28.md` §1.7 | §8.4 |
| (R1)–(R4) regulator branches | `phase4-exec-W30-M2-regulator-branches-2026-04-28.md` | §3.3, §5.2 |
| G4-M2 Heisenberg twist | `phase4-exec-G4-M2-Heisenberg-twist-2026-04-28.md` | §8.3 |
| `bcov` bibliography entry | `main.tex`:5926–5938 | §1.1 |
| `costello-li-quantum-bcov` bibliography entry | `main.tex`:6081–6087 | §1.2 |
| `costello-li-open-closed-bcov` bibliography entry | `main.tex`:6090–6096 | §3.4, §5.1, §6.3 |

---

**End of report.**
