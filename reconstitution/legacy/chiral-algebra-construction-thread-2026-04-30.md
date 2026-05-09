# Chiral/Factorization Construction Thread, 2026-04-30

Purpose: navigation and proof-thread control only.  This file introduces no
new theorem claim.  It indexes the constructed local
chiral/factorization algebra in the current manuscript and records the
boundary with one-dimensional vertex/OPE assertions.

## Stable Core

The core object is local:
\[
  \mathbb R^2_{\mathrm{top}}\times
  \widehat{\mathbb C^2}_{0,\mathrm{hol}},
  \qquad \Omega_{\mathrm{loc}}=dz_1\wedge dz_2 .
\]
The constructed chiral/factorization algebra is
\[
  \mathcal F_{\mathrm{Ham}}^{\mathrm{hol}},
\]
the formal Hamiltonian holomorphic factorization algebra on the formal
symplectic disk.  Its mixed/current/Weyl-Moyal/defect avatars are part of
the local construction.  A one-dimensional VOA/OPE algebra is not part of
this construction unless an additional complex-line or holomorphic-defect
restriction theorem supplies the missing data listed below.

## 09:43 Critique Correction

The refreshed critique sharpens the word "chiral" in this repository.
The native object is a holomorphic \(E_2\)-type factorization algebra on
the complex surface \(\mathbb C^2\), equivalently the two-complex
dimensional CE/factorization object already recorded as
\[
  \mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}(B)
  =
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  \bigl(\Omega_c^{0,\bullet}(B)\widehat\otimes
  (\mathfrak h\ltimes P[1])\bigr),
  \qquad B\subset\mathbb C^2 .
\]
It should not be renamed into a curve vertex algebra.

The legitimate curve chiral algebra is a reduced object.  It requires a
controlled reduction from
\(\mathbb R^2_{\mathrm{top}}\times\mathbb C^2_{\mathrm{hol}}\) to
\(\mathbb R_t\times\mathbb C_z\), retaining the \(z_2\)-mode or
principal-part coefficient system.  On that reduced surface, the
minimal Dirac BRST vertex algebra has fields \(Z_1,Z_2,b,c\), singular
OPEs
\[
  Z_1{}^i{}_j(z)Z_2{}^k{}_\ell(w)
  \sim
  \frac{\hbar\,\delta^i_\ell\delta^k_j}{z-w},
  \qquad
  b^i{}_j(z)c^k{}_\ell(w)
  \sim
  \frac{\delta^i_\ell\delta^k_j}{z-w},
\]
and BRST current
\[
  j_{\mathrm{BRST}}
  =
  \operatorname{Tr}(c[Z_1,Z_2])
  +\frac12\operatorname{Tr}(b[c,c]).
\]
The reduced chiral algebra is
\[
  A_{\partial,N}^{\mathrm{Dir\text{-}ch}}
  =
  H^\bullet(V_N^{\mathrm{Dir}},Q_{\mathrm{BRST}}).
\]
This is a theorem surface to construct after reduction, not the native
\(\mathbb C^2\) factorization algebra itself.

## Definition Anchors

| Anchor | Role |
|---|---|
| `abstract.tex:25-40` | Foregrounds \(\mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}\), \(\mathcal F_{\mathrm{Ham}}^{\mathrm{mix}}\), Weyl/Moyal brane avatars, principal-part current avatars, and the separate VOA/OPE obligation. |
| `main.tex:915`, `def:local-holomorphic-string-sector` | Defines local holomorphic factorization: Dolbeault fields, holomorphic polydifferential interactions, holomorphic factorization products, antiholomorphic translations null-homotopic. |
| `main.tex:961`, `def:local-th-string` | Defines the mixed holomorphic-topological sector on \(M\times Y\), with de Rham topological direction and Dolbeault holomorphic direction. |
| `main.tex:1078`, `def:local-hamiltonian-chiral-factorization-algebra` | Names the constructed local object and separates its holomorphic, mixed-current, Weyl/Moyal brane, and defect-current avatars. |
| `main.tex:1142`, `prop:local-hamiltonian-factorization-observables` | Proves the CE/factorization observable assignment from the local mixed Hamiltonian BF fields. |
| `local-dictionary.tex:170-375` | Local taxonomy and the exact one-dimensional vertex/OPE restriction boundary. |
| `theorem-lanes.tex:227`, `thm:lane-local-chiral-taxonomy` | Theorem-lane taxonomy: four local objects, exclusions, proof inputs. |
| `theorem-lanes.tex:349`, `thm:lane-holomorphic-defect-voa-restriction` | Recovered construction first; five-part vertex/OPE boundary second. |

## Constructed Objects

1. Holomorphic factorization object.
\[
  \mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}(B)
  =
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  \bigl(\Omega_c^{0,\bullet}(B)\widehat\otimes\mathfrak g\bigr),
  \qquad
  \mathfrak g=\mathfrak h\ltimes
  \mathfrak h^\vee_{\mathrm{cont}}[1],
  \quad
  \mathfrak h=\mathbb C[[z_1,z_2]]/\mathbb C\cdot1 .
\]

2. Mixed topological-current enhancement.
\[
  \mathcal F_{\mathrm{Ham}}^{\mathrm{mix}}(U\times B)
  =
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  \bigl(
    \Omega_c^\bullet(U)\widehat\otimes
    \Omega_c^{0,\bullet}(B)\widehat\otimes\mathfrak g
  \bigr).
\]
It is locally constant in \(U\subset\mathbb R^2_{\mathrm{top}}\) and
holomorphic in \(B\subset\mathbb C^2_{\mathrm{hol}}\).

3. Weyl/Moyal brane avatar.
\[
  P=\partial_{z_1}\otimes\partial_{z_2}
   -\partial_{z_2}\otimes\partial_{z_1},\qquad
  f*g=m\circ\exp\!\left(\frac{\hbar}{2}P\right)(f\otimes g),
\]
\[
  \{f,g\}_\hbar=\hbar^{-1}(f*g-g*f).
\]
At finite \(N\) the matrix Weyl relations are
\[
  [(\phi_1)^i{}_j,(\phi_2)^k{}_l]
  =\hbar\,\delta^i_l\delta^k_j .
\]
The cyclic and supercyclic bar-cobar objects are trace-bookkeeping
avatars for matrix or supermatrix branes.  They are not CoHA, compact-CY
chiral homology, or BKM data.

4. Defect/principal-part current avatar.
\[
  \mathfrak h_I=\Omega^\bullet_c(I)\widehat\otimes\mathfrak h,\qquad
  \mathcal P_I=\mathcal D'_c(I)\widehat\otimes\mathcal P,\qquad
  \mathfrak g_I=\mathfrak h_I\ltimes\mathcal P_I[1],
\]
\[
  A^{\mathrm{pp}}_\partial(I)
  =
  \widehat{\mathbf S}(\Omega_c^0(I)\widehat\otimes\bar A)
  \widehat\otimes
  \widehat{\mathbf S}(\mathcal D'_c(I)\widehat\otimes\mathcal P[1]).
\]
The reduced brackets are
\[
  \{B_f(a),B_g(b)\}=B_{\{f,g\}}(ab),\qquad
  \{B_f(a),\Theta_\rho(B)\}=\Theta_{f\cdot\rho}(aB),\qquad
  \{\Theta_\rho(B),\Theta_\sigma(C)\}=0 .
\]
The quantum current surface replaces \(f\cdot\rho\) by
\(\operatorname{ad}^{\vee}_{f,\hbar}\rho\).

## Proof Dependency Index

| Dependency | Current anchor |
|---|---|
| Local Hamiltonian/unimodular input | `local-dictionary.tex:13-124`; `main.tex:1061-1092`; `appendix-factorization-current-conventions.tex:122-188` |
| Holomorphic and mixed factorization habitats | `def:local-holomorphic-string-sector`; `def:local-th-string` |
| CE observable construction | `prop:local-hamiltonian-factorization-observables` |
| Formal-disk CE/PV comparison | `theorem-lanes.tex:828`, `thm:formal-disk-completed-ce-pv`; `main.tex:3319`, `thm:reduced-ce-pv-central-operation` |
| Interval current source and target | `main.tex:2785`, `constr:interval-fact-algebras`; `main.tex:2942`, `thm:hamiltonian-current-factorization` |
| Principal-part current brackets | `main.tex:5793`, `thm:reduced-principal-part-boundary-current`; `appendix-factorization-current-conventions.tex:413`, `thm:app-factorization-universal-current-interface`; `appendix-factorization-current-conventions.tex:371`, `cor:app-factorization-principal-part-current-brackets` |
| Weyl/Moyal coefficients | `main.tex:7221-7245`; `main.tex:7245`, `prop:moyal-monomial` |
| Finite-\(N\) reduced Moyal comparison | `main.tex:6548`, `thm:finite-n-reduced-moyal` |
| Componentwise quantum current surface | `main.tex:7363`, `thm:quantum-coefficient-surface` |
| One-dimensional vertex/OPE boundary | `local-dictionary.tex:290-373`; `theorem-lanes.tex:444-501`; Agent 155 report; Agent 162 report |

## Report Thread

| Report | Integration use |
|---|---|
| Agent 149 | Supplies the first taxonomy: local holomorphic factorization, mixed current enhancement, Weyl/Moyal brane algebra, defect/principal-part currents; excludes VOA, CoHA, compact chiral homology, BKM. |
| Agent 155 | Supplies the five data required for a genuine one-dimensional vertex/OPE specialization and proves the current manuscript does not supply them. |
| Agent 159 | Foregrounds \(\mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}\) in the abstract and introduction, and separates the avatars in the main narrative. |
| Agent 162 | Repairs the overbroad obstruction reading: no VOA/OPE theorem is present, but the local chiral/factorization construction is present. |

## Vertex/OPE Boundary

A one-dimensional vertex/OPE theorem requires all five additional data:

1. A holomorphic line or defect germ
\[
  \iota_L\colon L=\operatorname{Spf}\mathbb C[[w]]
  \hookrightarrow\widehat{\mathbb C^2}_0 .
\]
The brane interval \(I\subset\mathbb R_{\mathrm{brane}}\) is a real
topological current direction, not this complex line.

2. A transverse boundary condition or normal vacuum \(\mathcal B_\perp\)
and a restriction functor
\[
  \mathsf R_{L,\mathcal B_\perp}
  (\mathcal F_{\mathrm{Ham}}^{\mathrm{hol}})
  =
  \mathcal F_{L,\mathcal B_\perp}.
\]
The functor must prove independence of normal choices, compatibility with
disjoint disks in \(L\), and translation covariance in \(w\).

3. A factorization-to-vertex comparison producing
\[
  V_L,\qquad \mathbf 1_L,\qquad T_L .
\]

4. Finite Laurent OPE modes
\[
  Y_L(a,w)b=\sum_{n\in\mathbb Z}(a_{(n)}b)w^{-n-1},
  \qquad a_{(n)}b=0\quad(n\gg0),
\]
with vacuum, translation, and locality.

5. Weyl/Moyal compatibility through a zero-mode or Zhu map
\[
  \zeta_{L,\hbar}\colon
  (\bar A_\hbar,*)\longrightarrow \operatorname{Zhu}(V_L),
\]
or fields \(J_f(w)\) with specified singular product, central level, and
zero-mode action
\[
  [J_{f,(0)},\Theta_\rho]
  =
  \Theta_{\operatorname{ad}^{\vee}_{f,\hbar}\rho}.
\]

Until these data are constructed, the manuscript may assert the local
two-complex-dimensional holomorphic factorization algebra and its mixed,
brane, and current avatars, but not a one-dimensional VOA/OPE algebra.

## Stale and Duplicate Descriptions

- Stale: `reconstitution/attack-heal-latest-2026-04-30.md` and Agent 157
  describe Agent 155 as absent/live.  The Agent 155 report is present and
  has been read for this index.
- Stale: Agent 160 records Agent 159 as present but untracked.  Current
  `git status --short` shows the Agent 159 report staged.
- Duplicate but consistent: the local chiral/factorization taxonomy now
  appears in the abstract, `main.tex`, `local-dictionary.tex`, and
  `theorem-lanes.tex`.  This file is the integration index for those
  duplicated descriptions; no TeX edit is made here.
- Healed by Agent 162: "no VOA/OPE theorem" is not an obstruction to the
  constructed local chiral/factorization algebra.  It is only the boundary
  for a stronger one-dimensional specialization.

## Remaining Obligations

- Prove the complex-line or holomorphic-defect restriction theorem before
  asserting a vertex algebra, OPE mode algebra, Zhu map, or \(J_f(w)\)
  current algebra.
- For the refreshed Dirac BRST curve algebra, first prove the reduction
  datum, retained coefficient system, \(Q_{\mathrm{BRST}}^2=0\), Zhu
  algebra, Capelli/Weyl shift, and Hochschild/HKR/CE-PV comparison.
- Keep compact-CY chiral homology, CoHA, quintic/GV/OSV,
  Abel-Jacobi, Igusa, Borcherds, and BKM material outside the core local
  theorem unless a separate matched-conventions theorem is supplied.
- Do not identify the real brane interval current algebra with a complex
  line OPE.  The interval current brackets are support-local \(P_0\)
  brackets, not Laurent singular OPE expansions.
