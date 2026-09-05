# Mathematical contract

Read the relevant sections before mathematical edits or cross-volume comparison.
Paths below are relative to the repository root unless marked otherwise.
The master diagram describes comparison targets. Its arrows require the supplied data stated below.

## What this manuscript proves

The **formal-Darboux trace-sector stalk theorem for the Mixed Holomorphic-Topological Deligne problem** at $N$ Dirac branes:
\[
A^{\mathrm{cl}}_{\partial, N} = C^\bullet_{\mathrm{CE}}\bigl(\mathfrak{gl}_N,\; \mathrm{Kosz}([\phi_1, \phi_2])\bigr),\qquad
J(f) = \mathrm{Tr}\,f(\phi_1, \phi_2),\qquad
c_f \mapsto \theta_f,\quad u_f \mapsto J(f).
\]
The trace map $J$ supplies the formal Darboux coordinate on the scalar-reduced stable trace-sector polyvector model.
Its ordinary $E_1$/HKR comparison is the zero-Poisson special fibre $HH^\bullet_{\mathrm{adm},\mathrm{HKR},0}$.
That comparison requires a cofinal coordinate system, compatible transition maps and HKR homotopies, and exactness of the supplied Roos system.
See `prop:continuous-admissible-hkr-trace-target` in `main.tex`.
For a nonzero linear Poisson tensor, supply the continuous filtered twisted formality and PBW datum of `defn:admissible-twisted-formality-pbw`.
This datum includes the deformed product, PBW equivalence, and compatibility with scalar reduction, stable traces, coordinate projections, and Roos totalization.
Ordinary HKR alone does not compare the nonzero Poisson differential with Hochschild cochains. The manuscript does **not** claim this target is the chiral Hochschild cohomology $C^\bullet_{\mathrm{ch}}(A_b, A_b)$: the holomorphic kernel operad is separate supplied data, and the three $E_2$-structures ($E_2^{\mathrm{top}}$, $E_2^{\mathrm{ch,hol}}$, $E_2^{\mathrm{HT}}$) are not identified without a topologisation or restriction datum (`main.tex` $E_2$-notation block). The finite-$N$ Capelli scalar $\hbar N[\bar c]$ is the projective Lie anomaly of the trace representation; it is determinant-line or modular-line curvature only after the corresponding line, connection, and Atiyah-class pullback have been supplied (the constructed-line question is `prob:quillen-curvature-trace-chart`). The obstruction-curvature taxonomy classifies the global comparison problem.

The constellation-level master picture, of which this manuscript proves **only** the scalar-reduced stable trace-sector formal-Darboux stalk — every other clause below is a criterion, a displayed shape, or a deferral, not a theorem of this repo:

> Closed sector $=$ the target $Z^{\mathrm{der},\mathrm{Mor}}_{E_2^{\mathrm{HT}}}(\mathcal{C}^{\mathrm{op}}_\partial)$ of the global comparison; the comparison itself is the ten-row supplied datum $\mathfrak{D}^{\mathrm{HT}}_N$ (criterion). Modular structure: the projective clutching law is displayed as the *shape* of a deformation problem, with its data deferred to the compact comparison (`conj:operator-modular-lift`); no clutching theorem is proved here. Quantum and global obstructions $=$ the typed obstruction ledger. Scalar invariants $=$ sections of the modular line $\Omega_{\mathrm{central}}$ on the period domain only after the line datum is constructed.

This manuscript supplies the local trace-sector input to the mixed holomorphic-topological chiral $E_d$ Deligne problem.

---

## The constellation

| repository | role |
|---|---|
| `~/mixed-holomorphic-topological-strings/` | this manuscript — trace-sector formal-Darboux stalk |
| `~/chiral-bar-cobar/` (Vol I) | $d = 1$ chiral Koszul; bar / cobar / centre distinction |
| `~/chiral-bar-cobar-vol2/` (Vol II) | $d = 1$ algebraic 3d-gravity HT sector at $A = \mathrm{Vir}_c$ |
| `~/chiral-bar-cobar-vol4/` (Vol IV) | architectural inheritance |
| `~/calabi-yau-quantum-groups/` (Vol III) | $d \geq 2$; two-stage CY-to-chiral; Hall–Drinfeld |
| `~/igusa-cusp-form/` | degree-2 (genus-two) modular section of $\Omega_{\mathrm{central}}$ on $K3 \times E$ |
| `~/ecosystem/` | discipline layer; `INVARIANTS.md` binds |

Cross-volume firewall: convention divergence is load-bearing — flag, do not silently reconcile. Every shared symbol and every shared concept has the same definition.

---

## Two principles, seventeen sites

**P1.** Primitive $\neq$ chart.
**P2.** Shadow $\neq$ object.

Seventeen sites where these have been violated; each carries a corrected form.

| # | failed claim | corrected form |
|---|---|---|
| 1 | $A$ is the primitive open object | $\mathcal{C}^{\mathrm{op}}_\partial$ primitive; $A_b = \mathrm{End}(b)$ for chosen $b$ |
| 2 | $\mathrm{Bar}(A) = $ bulk | $\mathrm{Bar}(A) = $ twisting coalgebra; $Z^{\mathrm{der}}_{\mathrm{ch}}(A) \simeq C^\bullet_{\mathrm{ch}}(A, A) = $ bulk |
| 3 | 2d chiral $\Rightarrow $ 3d HT via $E_1$-bar | chiral Deligne–Tamarkin: $A \rightsquigarrow Z^{\mathrm{der}}_{\mathrm{ch}}(A)$ one-up |
| 4 | open sector on bare curve $X$ | open sector on $\partial X^{\mathrm{KN}}$ for Kato–Nakayama log $(X, D, \tau)$ |
| 5 | modularity is property of closed algebra | trace + clutching on the open category |
| 6 | five $\kappa$-numbers $(0, 0, 3, 5, 24)$ are one invariant | five distinct construction layers; spectral-sequence interpretation conjectural |
| 7 | $\mathrm{CY}_d\text{-Cat} \to \mathrm{ChirAlg}$ direct | $\Phi_d = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C} \circ \Phi^{\mathrm{FA}}_d$ |
| 8 | $Y^+(X) = \mathcal{G}(X)$ | $\mathcal{G}(X) = D(Y^+(X))$ after Hall pairing / completion / integral form / stable-envelope transport / descent |
| 9 | 6d hCS = 3d CS in disguise | 6d hCS realizes $\Phi^{\mathrm{FA}}_3$ on verified loci; one-loop $\int_X \mathrm{Tr}^{\mathrm{ad}}(A(F_A)^3)$ quartic |
| 10 | formal local HT $\Rightarrow $ global compact theory | formal-Darboux + descent + QME + anomaly + locality $\Rightarrow $ candidate |
| 11 | $\Delta_5 = $ compact BPS Hilbert space | $\Delta_5 = $ Borcherds denominator / scalar shadow; operator lift open |
| 12 | scalar $Z_{\mathrm{BPS}} = $ operator algebra | scalar $= $ protected trace of still-to-be-constructed operator package |
| 13 | algebraic holography $= $ 3d gravity construction | identification of HT sector; not construction of dynamical-metric path integral |
| 14 | $W_\infty[\lambda] \Rightarrow E_\infty$ from finite-spin checks | conditional on Prochazka, Creutzig–Kanade–Linshaw, Pope–Romans–Shen/Bakas, Yamada |
| 15 | class M chain-level in ordinary complexes | completed ambient: HS-sewing / coderived BV $= $ bar / weight-completed / pro / $J$-adic |
| 16 | PVA Jacobi $\Rightarrow $ all-loop quantum | classical only; finite-jet PVA all-loop conditional on KZ analytic SDR + Stokes + reflected weights + $T = [Q_{\mathrm{tot}}, G]$ |
| 17 | quadratic chiral duality $\Rightarrow $ Koszul theorem | quadratic dual + MC injection only; chiral Koszul homotopy theorem separate |

When any pattern appears in a draft: replace with the corrected form.

---

## The master architecture

```
                Stage 1 (CY)             Stage 2 (chiral)         Stage 3 (Hall double)
            ┌──────────────┐         ┌────────────────┐         ┌──────────┐
CY_d-Cat ─Φ^FA→│ E_d-HolFA(X) │─∫_Σ───→│ ChirAlg(C)     │──Hall──→│ D(Y^+(X))│
            └──────┬───────┘         └────────┬───────┘         └──────────┘
                   │                          │
                   │ boundary value           │ chosen vacuum b
                   │ on ∂X^KN (Kato–Nakayama) │
                   ▼                          ▼
              ┌───────────┐               ┌──────┐
              │ C^op_∂    │── chart b ──→ │ A_b  │
              └─────┬─────┘               └───┬──┘
                    │                         │
                    │ derived E_d-centre      │ chiral Hochschild
                    └─────────────────────────┘
                                │
                                ▼
              Z^der_{E_d^ch}(C^op_∂) ≃ C^•_ch(A_b, A_b)
                                │
                                ▼
                    modular line bundle
                       = Ω_central
                                │
                                ▼
                  Δ_5 (degree-2 modular section
                       on K3 × E)
```

Every constellation volume populates one node. **This manuscript supplies the scalar-reduced stable trace-sector formal-Darboux stalk at the Dirac brane node. Its ordinary $E_1$/HKR interpretation is restricted to the zero-Poisson special fibre with the compatible exact Roos system above. Nonzero linear-Poisson comparison requires the supplied twisted formality and PBW datum.** Comparison with $C^\bullet_{\mathrm{ch}}(A_b, A_b)$ and identification of the three $E_2$-structures require separate supplied data.

---

## The platonic chapter sequence

Eleven chapters; each forced by the previous; each section either constructs the local centre, identifies an obstruction, or computes an example.

1. **The setup.** $\mathbb{R}^2_{\mathrm{top}} \times \mathbb{C}^2_{\mathrm{hol}}$ with brane stacks at holomorphic-symplectic points; the Mixed HT Deligne problem; the trace-sector local stalk question.
2. **The shifted-cotangent BF Lie algebra.** $\mathfrak{h} = \mathbb{C}[[z_1, z_2]] / \mathbb{C}$, $\mathfrak{g} = \mathfrak{h} \ltimes \mathfrak{h}^\vee_{\mathrm{cont}}[1]$; Hamiltonian BF action.
3. **The derived commuting variety stack at $N$ Dirac branes.** $[\mu^{-1}_{\mathrm{der}}(0) / \mathrm{GL}_N]$, $Q\psi = [\phi_1, \phi_2]$.
4. **Boundary algebra and trace map.** $A^{\mathrm{cl}}_{\partial, N}$, $J(f) = \mathrm{Tr}\,f(\phi_1, \phi_2)$.
5. **CE/PV dictionary as Koszul coordinate model.** $c_f \mapsto \theta_f$, $u_f \mapsto J(f)$ identifies the scalar-reduced stable trace-sector polyvector coordinate. Ordinary $E_1$/HKR comparison requires the zero-Poisson special fibre and compatible exact Roos system. Nonzero linear-Poisson comparison requires the supplied twisted formality and PBW datum.
6. **The Capelli scalar.** $\hbar N[\bar c]$ as projective Lie anomaly of the trace representation; determinant-line or modular-line curvature only after the line, connection, and Atiyah-class pullback are supplied.
7. **The obstruction calculus.** $\mathfrak{K}_{\mathrm{HT}}$, $\Theta_{\mathrm{OCA}}$, \(F_{\mathrm{HT}}\), and the four obstruction-curvature rows. Six native obstructions become projections of one curvature only after the comparison-unifying datum is supplied.
8. **The pro-Matlis target.** $N$-tower categorical home; Matlis duality at finite presentation.
9. **Examples.** Heisenberg, $\hat{\mathfrak{g}}_k$, $\beta\gamma$, $\mathrm{Vir}_c$ (algebraic HT holographic reading; identification, not construction), $W_N$, $\mathbb{C}^3$, $K3$, $K3 \times E$, generic compact CY3.
10. **The $W_\infty[\lambda] / E_\infty$ admissible endpoint.** Conditional theorem; Prochazka triangular truncation, Creutzig–Kanade–Linshaw parafermion compatibility, Pope–Romans–Shen/Bakas, Yamada weight-window.
11. **The frontier.** MNOP / framing on $S^3$; Hall–Drinfeld–Borcherds compact-CY3 comparison; gravitational lift of $\Phi_{10}$. Three open problems: chiral $E_d$ Deligne at $d \geq 2$; Hall–Drinfeld–Borcherds spectral sequence on compact non-toric CY3; operator-level lift of the modular line.

The opening sentence (Chapter 1):

> *Mixed holomorphic-topological string theory on $\mathbb{R}^2_{\mathrm{top}} \times \mathbb{C}^2_{\mathrm{hol}}$ has, at each formal holomorphic-symplectic brane point, a local Deligne problem comparing Hamiltonian BF bulk observables with the Morita chiral \(E_2\)-centre of the boundary category; this manuscript computes the scalar-reduced stable trace-sector formal-Darboux coordinate of that problem at \(N\) Dirac branes.*

The closing sentence (Chapter 11):

> *The trace map $J(f) = \mathrm{Tr}\,f(\phi_1, \phi_2)$ is the scalar-reduced stable trace-sector coordinate at one Dirac brane vacuum; the global identification, the operator-level lift of the modular line, and the chiral $E_d$ Deligne theorem at $d \geq 2$ are the open problems this formal-Darboux stalk makes precise.*

---

## Convention layer (binding)

- $d = \dim_{\mathbb{C}} X$ for target complex dimension.
- Local geometry is $\mathbb{R}^2_{\mathrm{top}} \times \mathbb{C}^2_{\mathrm{hol}}$ at a brane. The only Calabi-Yau datum is the trivial holomorphic volume / symplectic on $\mathbb{C}^2$, used for BV pairing, divergence-free Hamiltonian fields, cyclic trace densities. **Not** a compact CY$_3$ assumption; **not** a BCOV theorem; **not** a license to import quintic / OSV / GV / MNOP / Abel–Jacobi / CoHA / Igusa / BKM into the core local theorem surface.
- Native object: holomorphic $E_2$ / factorization algebra on $\mathbb{C}^2$,
\[
\Omega^{0, \bullet}_c(B) \,\widehat{\otimes}\, \mathfrak{g},\qquad
\mathfrak{g} = \mathfrak{h} \ltimes \mathfrak{h}^\vee_{\mathrm{cont}}[1],\qquad
\mathfrak{h} = \mathbb{C}[[z_1, z_2]] / \mathbb{C}.
\]
Curve vertex algebra / Zhu algebra / Vol II $\mathbb{C} \times \mathbb{R}$ chiral-topological theorems enter only after a controlled reduction with explicit $z_2$-mode or principal-part data, pushed-forward bracket, BV pairing, brane image, anomaly matching.
- Worldsheet $\Sigma$ — complex curve, possibly with boundary or marked points.
- Framing on $S^3$ stated when invoked; deviation flagged.
- BV degree, ghost number, form degree tracked separately. Koszul sign and Gerstenhaber bracket signs fixed in `appendix-sign-conventions.tex`.
- Propagator weight in heat-kernel renormalization explicit.
- $\hbar$ versus $g_s$: distinguish — $\hbar$ for QFT loops, $g_s$ for string genus expansion.
- Holomorphic anomaly sign: BCOV-strict per `appendix-sign-conventions.tex`.
- Negative-cyclic / cyclic / Hochschild homology distinguished.
- $\mathcal{C}^{\mathrm{op}}_\partial = \Phi^{\mathrm{FA}}_d(\mathcal{A})\big|_{\partial X^{\mathrm{KN}}}$ on the Kato–Nakayama log boundary.
- $\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C}(\mathcal{F}) = \int_{\Sigma_{d-1}} \mathcal{F}\big|_C$ — Lurie–Ayala–Francis factorization homology.
- "Dirac brane stack" $= [\mu^{-1}_{\mathrm{der}}(0) / \mathrm{GL}_N]$ — derived commuting variety stack; the brane reading is the physical realization.
- Capelli scalar $\hbar N[\bar c]$ — the Capelli identification is the projective Lie anomaly of the trace representation. A determinant-line or modular-line curvature interpretation requires the corresponding line, connection, and Atiyah-class pullback.
- $\Omega_{\mathrm{central}}$ is **defined in the manuscript**: `main.tex`, Remark `rmk:omega-central-definition` (Compact modular-line addendum) — the Hodge determinant line $\lambda = \det \pi_* \Omega^1$ on $\overline{\mathcal{A}}_g$, whose weight-$k$ degree-$g$ sections are the Siegel modular forms. $\Phi_{10}$ is its degree-2 (genus-two, full-level $\mathrm{Sp}_4(\mathbb{Z})$) weight-10 section; $\Delta_5 = \Phi_{10}^{1/2}$ on the paramodular cover. This file points at that definition; it no longer carries it.
- CE/PV dictionary $c_f \mapsto \theta_f$, $u_f \mapsto J(f)$ is the Koszul coordinate model for the scalar-reduced stable trace-sector polyvectors. Ordinary $E_1$/HKR comparison applies on the zero-Poisson special fibre with compatible exact Roos data. Supply twisted formality and PBW data for nonzero linear-Poisson comparison.

## Theorem-control predicates (binding)

- Native $\mathbb{C}^2$ holomorphic $E_2$ taxonomy retained before any curve-chiral reduction.
- BMK lane: one-pair analytic pro-Matlis retract is **not** strict native all-window support-local current transfer; obstruction $\mathrm{Ob}^\Pi_{\mathrm{BM}}$.
- Larger non-scalar $\theta_3$ row is evidence only with: a CE ancestor, or a scalar-zero Costello local counterterm, or a complete companion-face table; tower compatibility through $\Delta^1_{M, N} = -\pi_{M, N}\mathfrak{b}^M + \mathfrak{b}^N$ plus the secondary $\varprojlim^1 H^0$ primitive class.
- Radial / Weyl theorem surface is $\Omega^{\mathrm{rad}}_{a, b}$, equivalently decorated PBW Stokes for $D^\square_{a, b} = C^+_{a, b} \partial_2$, with failure exactly a signed row in $\ker B^*_{a, b}$.
- Larger non-scalar Costello / QME theorem requires: filtered scalar projection, finite row arrays, primitive matrix $A^M c = -r^M$, transition matrices, Roos compatibility, centrality homotopies, curved bulk-to-defect kernel.
- Brane-preserving $\Omega$-background: normal scaling on $N_L X = \mathbb{R}_s \oplus \mathbb{C}_{z_1} \oplus \mathbb{C}_{z_2}$ with $t$ fixed; $T_\Omega = \mathbb{C}^*_{\varepsilon_s} \times \mathbb{C}^*_{\varepsilon_1} \times \mathbb{C}^*_{\varepsilon_2}$. Literal $(t, s)$-rotation does not preserve the brane line; not native unless a different fixed-locus problem is defined. Theorem surface includes $Q_\Omega = Q + \iota_{V_\Omega}$, $Q_\Omega^2 = L_{V_\Omega}$, inverted normal weights, residue-vs-Euler normalization, stratified factorization data.

---
