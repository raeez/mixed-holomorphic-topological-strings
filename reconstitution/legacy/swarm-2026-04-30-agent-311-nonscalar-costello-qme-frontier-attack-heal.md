# Agent 311 Non-scalar Costello QME Frontier Attack-Heal

Status: report-only. No TeX, script, figure, source, or build file was edited.

Owned detailed report:
`reconstitution/nonscalar-costello-qme-frontier-attack-heal-2026-04-30.md`.

## Result

The full non-scalar Costello graph/QME realization is not proved. The strongest
admissible theorem surface is the finite-window local-functional obstruction
criterion plus the proved minimal full-equivariant zero branch in its named
habitat.

The theorem-grade habitat is
\[
  \mathfrak Q^\bullet_{\mathcal G,\Lambda,M}(I)
  =
  \left(
  \mathcal O^{\mathrm{bd}}_{\mathrm{loc},\mathcal G,\Lambda,M}
  (\mathcal E_w^M|_I;A^{\mathrm{pp},w,M}_{\partial,\hbar}(I)),
  d_M=Q+\{I^w_{0,M},-\}_{\hbar,M}
  \right),
\]
with labels restricted to regular densities, graphwise wavefront-admissible
tuples, or sign-conic finite-scaling classes. The Hom complex is
\[
  \mathbf K^\bullet_{\mathcal G,\Lambda,M}(I)
  =
  \operatorname{Hom}_{\mathrm{cont}}
  (C^\bullet_{\mathrm{lab}}(\mathcal G_M),
   \mathfrak Q^\bullet_{\mathcal G,\Lambda,M}(I)),
\]
with
\[
  d_{\mathbf K,M}T=d_MT-(-1)^{|T|}T\,d_{\mathrm{CE}},
  \qquad
  \operatorname{Curv}_{\mathbf K,M}(\kappa)
  =
  d_{\mathbf K,M}\kappa+\frac12[\kappa,\kappa]_{\mathbf K,M}.
\]
The source-face term is part of the QME differential.

The non-scalar complex is formed only after a filtered chain scalar projection
\[
  \widehat\sigma_{\mathrm{sc},M}\colon
  \mathfrak Q^\bullet_{\mathcal G,\Lambda,M}(I)
  \to C^\bullet_{\mathrm{Lie}}(\bar A;\mathbb C\gamma_{\mathbf 1})[1][[\hbar]]
\]
has been constructed. Then
\[
  \mathcal K^\bullet_{\mathrm{ns},M}(I)=\ker\widehat\sigma_{\mathrm{sc},M}.
\]
Outside the balanced/full-equivariant marked habitat the scalar-projection
lift tower \(o_{\sigma,w}^{(r)}(I)\) remains an obstruction.

## Exact Obstruction

The current \(\theta_3\) one-row subcomplex is
\[
  \mathcal Q^0_{\theta_3,M}=0,\qquad
  \mathcal Q^1_{\theta_3,M}=\mathbb C\mathsf E_{\theta_3,M},\qquad d_M=0,
\]
with
\[
  \mathsf E_{\theta_3,M}=-K^M_{\Theta_3}(\zeta_{M,\nu_3}),\qquad
  \ell_{\theta_3}(\mathsf E_{\theta_3,M})=1.
\]
Thus \(A^M=[\,]_{1\times0}\), \(r^M=(1)\), and no fixed-window primitive
exists in the supplied row complex.

The direct repair is a genuine scalar-zero column
\[
  A^M_{\theta_3,C}=(-1),\qquad
  d_MC_{\theta_3,M}=-\mathsf E_{\theta_3,M},
\]
with locality, scalar-zero value, \(TA=AP\), and zero Roos class.

The lower Bianchi route currently has
\[
  d_{\mathrm{ns},2}D^2_{02,20}
  =
  -2E^2_{\nu_{02}}+2E^2_{\nu_{20}}+\mathfrak b^2_{02,20},
\]
\[
  A_D^2=(-2,2,1)^T,\qquad r_2=(2,-2,0)^T,
\]
and cokernel
\[
  \widetilde\lambda_{02,\mathfrak b}
  =
  \frac12(E^2_{\nu_{02}})^*
  +(\mathfrak b^2_{02,20})^*,
  \qquad
  \widetilde\lambda_{02,\mathfrak b}A_D^2=0,\quad
  \widetilde\lambda_{02,\mathfrak b}(r_2)=1.
\]
The missing column is
\[
  A_B^2=(0,0,-1)^T,\qquad
  d_{\mathrm{ns},2}B^2_{02,20}=-\mathfrak b^2_{02,20}.
\]

The eight-face companion attempt remains rejected: its residual vector is
\[
  (2,-2,3,2,-1,1,-2,-3),
\]
and diagonal transport to \(N=2\) leaves \(2E^2_{\nu_{02}}-2E^2_{\nu_{20}}\).
The marked Costello incidence/weight table is absent.

## Patch Targets

- `main.tex:8428-8662`: keep the larger non-scalar Costello/QME claim as the
  filtered obstruction criterion; add the \(\Lambda\)-restricted habitat only
  if manuscript edits are authorized.
- `main.tex:8664-8931`: keep \(\theta_3\) as an obstruction theorem; the only
  admissible positive additions are \(C_{\theta_3}\), a marked source
  ancestor, a complete companion table, or \(B^2_{02,20}\) with the displayed
  differential and transport.
- `theorem-lanes.tex:3318-3555`: local graph/QME branch catalogue should remain
  a finite-window row-data catalogue, not an all-graph QME theorem.
- `open-obligations.tex:502-906`: consolidate the required data
  \((\mathcal G_M^{\mathrm{mk}},\widehat\sigma_{\mathrm{sc},M},
  \kappa_{\hbar,w,I},A^M,T^{M,N},P^{M,N},\lambda_n)\).
- `claim-strength-ledger.tex:503-537`: align the pure two-\(u\) obstruction
  wording with the current main-text statement.

## Verification

Ran:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py
```

The script reports the minimal full-equivariant order-two branch as zero, the
\(\theta_3\) one-row subcomplex as obstructed, exact payload fixtures as
accepted only when \(dC=-E\), scalar-zero, \(TA=AP\), and Roos zero are
supplied, and the eight-face companion route as rejected.

No PDF build was run because this was report-only.
