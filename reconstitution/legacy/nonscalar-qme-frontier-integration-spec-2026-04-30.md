# Non-scalar QME Frontier Integration Spec

Date: 2026-04-30.
Status: report-only integration specification. No manuscript TeX was edited.

## Verdict

The theorem now proved is the finite-window local-functional obstruction
criterion, together with the minimal full-equivariant zero branch in its
named habitat. The larger non-scalar Costello graph/QME realization remains a
construction target.

The integration rule is strict. The minimal zero branch may be stated as a
theorem only for the minimal marked full-equivariant finite-window package.
Any larger package must pass the scalar projection lift, finite row, matrix,
transport, and Roos obstruction tests before it is called a QME solution.

## Proved Theorem Surface

The admissible habitat is the restricted finite-window local-functional
complex
\[
  \mathfrak Q^\bullet_{\mathcal G,\Lambda,M}(I)
  =
  \left(
  \mathcal O^{\mathrm{bd}}_{\mathrm{loc},\mathcal G,\Lambda,M}
  (\mathcal E_w^M|_I;A^{\mathrm{pp},w,M}_{\partial,\hbar}(I)),
  d_M=Q+\{I^w_{0,M},-\}_{\hbar,M}
  \right),
\]
completed in the \(\hbar\)-adic, scalar-contact, and finite-window
filtrations. The label class is not all of \(\mathcal D'_c(I)\). It is
regular compactly supported densities, graphwise wavefront-admissible tuples
\(\mathcal D'_{c,\mathrm{WF}}(I;\Gamma,M)\), or the sign-conic finite-scaling
classes \(\mathcal D'_{c,\Lambda_\pm,\mathrm{fs}}(I)\) where the ordinary
collision-conormal criterion applies.

The Hom-valued kernel complex is
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
The source-face term \(-\kappa d_{\mathrm{CE}}\) is part of the differential.

The non-scalar complex exists only after a filtered chain scalar projection
\[
  \widehat\sigma_{\mathrm{sc},M}\colon
  \mathfrak Q^\bullet_{\mathcal G,\Lambda,M}(I)
  \longrightarrow
  C^\bullet_{\mathrm{Lie}}(\bar A;\C\gamma_{\mathbf 1})[1][[\hbar]]
\]
has been constructed. Then
\[
  \mathcal K^\bullet_{\mathrm{ns},M}(I)
  =
  \ker\widehat\sigma_{\mathrm{sc},M},
  \qquad
  d_{\mathrm{ns},M}=d_M|_{\mathcal K_{\mathrm{ns},M}}.
\]
If \(\widehat\sigma_{\mathrm{sc},M}\) is only an associated-graded scalar
symbol, the non-scalar QME complex has not been formed.

At order \(n\), after lower counterterms \(C_{<n,M}\), the admissible row
types are
\[
  R^{\mathrm{row}}_{d\Gamma,M}
  =
  \varepsilon_\Gamma d_MK^M_\Gamma,
  \qquad
  R^{\mathrm{row}}_{\mathrm{CE}(\Gamma,\nu),M}
  =
  -\varepsilon^{\mathrm{CE}}_{\Gamma,\nu}K^M_\Gamma(\zeta_{M,\nu}),
\]
\[
  R^{\mathrm{row}}_{b(\Gamma_1,\Gamma_2),M}
  =
  \frac12\varepsilon_{\Gamma_1,\Gamma_2}
  \{K^M_{\Gamma_1},K^M_{\Gamma_2}\}_{\hbar,M},
\]
together with
\[
  [\hbar^n]\left(
    d_MC_{<n,M}
    +\frac12\{C_{<n,M},C_{<n,M}\}_{\hbar,M}
  \right).
\]
The scalar gate is
\[
  \mathfrak s_{n,M}
  =
  \sum_{\alpha\in\mathsf A^{\mathrm{fw}}_{n,M}}
  \widehat\sigma_{\mathrm{sc},M}(R^{\mathrm{row}}_{\alpha,M}).
\]
Only when \(\mathfrak s_{n,M}=0\) may one form
\[
  R^{\mathrm{ns}}_{n,M}=\sum_i r_i^M\rho_i^M
  \in Z^1(\mathcal K^\bullet_{\mathrm{ns},M}(I)).
\]
With primitive candidates \(\eta^M_j\),
\[
  d_{\mathrm{ns},M}\eta^M_j=\sum_iA^M_{ij}\rho_i^M,
  \qquad
  A^Mc_M=-r^M.
\]
Failure is certified by
\[
  \ell A^M=0,\qquad \ell(r^M)\ne0.
\]
The inverse-limit theorem additionally requires
\[
  T^{M,N}r^M=r^N,\qquad
  T^{M,N}A^M=A^NP^{M,N},\qquad
  [P^{M,N}c_M-c_N]=0
  \in H^0(\mathcal K^\bullet_{\mathrm{ns},N}(I)).
\]
The finite-window obstruction pair is
\[
  \mathfrak O_n^{\mathrm{ns}}
  =
  \bigl(([\mathfrak o^{\mathrm{ns}}_{n,M}])_M,\lambda_n\bigr).
\]

## Minimal Full-equivariant Branch

The proved positive branch is:
\[
  \mathcal G^{\mathrm{mk},0}_M
  =
  \langle
  \text{strict current-interface rows},\,
  \alpha_{\mathrm{sc}},\,
  \text{subset-deletion closure}
  \rangle
\]
in the full-equivariant marked branch \(V=\C^{N|N}\), with no additional
positive-order seed graph, no CE-source face, no graph-counterterm face, and
no nonzero scalar-zero row.

In that habitat, for every \(n\ge1\),
\[
  R^{\mathrm{ns}}_{n,M}=0,\qquad
  \mathfrak o^{\mathrm{ns}}_{n,M}=0,\qquad
  C_{n,M}=0.
\]
The binary centrality row is
\[
  A^M_{\min}:0\to0,\qquad
  r^M_{\min}=0,\qquad
  h^M_{\min}=0,
\]
with zero Roos class. This theorem supplies no row values, graph weights,
source faces, primitive columns, or transport matrices for a larger package.

## Larger Construction Target

The unproved theorem is the full non-scalar Costello graph/QME realization:
construct a restricted local-functional graph package and counterterms such
that
\[
  \operatorname{Curv}_{\mathbf K}
  (\kappa_{\mathcal G,w,I}+C_{\hbar,w})=0
\]
in the completed brane-defect kernel complex, with finite-window and
admissible-weight compatibility.

The missing data are:

- a codimension-two closed marked Costello list \(\mathcal G_M^{\mathrm{mk}}\);
- a filtered chain scalar projection \(\widehat\sigma_{\mathrm{sc},M}\);
- regular-density or wavefront-admissible graph contractions;
- positive-edge weights \(K^M_\Gamma=W^{R,M}_{\Gamma,L,w}(B^\Gamma_\bullet)\);
- source-face signs \(\varepsilon^{\mathrm{CE}}_{\Gamma,\nu}\);
- row bases and primitive columns;
- transition matrices \(u^{M,N},v^{M,N},q^{M,N},T^{M,N},P^{M,N}\);
- vanishing of the fixed-window \(H^1\) classes and the Roos
  \(\varprojlim^1H^0\) classes;
- if closed exchange is used, a tower \(\mathcal X^\bullet_{w,M}(I)\),
  maps \(\Xi_M\), and \(W_{n_0,M}\) killing
  \((\beta^{\mathrm{cl}},\mu^{\mathrm{cl}},\lambda^{\mathrm{cl}})\).

## Theta3 Classes To Reference

The first supplied larger-row obstruction is
\[
  \mathsf E_{\theta_3,M}
  =
  -K^M_{\Theta_3}(\zeta_{M,\nu_3}),\qquad
  \widehat\sigma_{\mathrm{sc},M}(\mathsf E_{\theta_3,M})=0.
\]
In the current one-row scalar-zero complex
\[
  \mathcal Q^0_{\theta_3,M}=0,\qquad
  \mathcal Q^1_{\theta_3,M}=\C\mathsf E_{\theta_3,M},\qquad d_M=0,
\]
the class
\[
  \mathfrak o^{\mathrm{ns}}_{\theta_3,M}
  =
  [\mathsf E_{\theta_3,M}]
\]
is nonzero, certified by
\[
  \ell_{\theta_3}(\mathsf E_{\theta_3,M})=1.
\]
Equivalently,
\[
  A^M_{\theta_3}=[\,]_{1\times0},\qquad r^M=(1).
\]

The direct accepted column would be
\[
  A^M_{\theta_3,C}=(-1),\qquad
  d_MC_{\theta_3,M}=-\mathsf E_{\theta_3,M},
\]
with scalar-zero value, locality or wavefront admissibility, \(TA=AP\), and
zero Roos class.

The pure two-\(u\) source envelope obstruction is
\[
  q_{2u}
  =
  e^*_{((H_{0,1},H_{2,0}),c_{\rho_{2,1}})}
  -\frac12
  e^*_{((H_{0,1},H_{0,1}),c_{\rho_{0,2}})},
\]
\[
  q_{2u}d_{\mathrm{CE}}=0,\qquad
  q_{2u}(\zeta_{M,\nu_3})=1.
\]
This blocks ordinary pure two-\(u\) CE ancestors in every finite Hamiltonian
degree. It is not a universal no-go for marked-source, Hom-valued companion,
or local-functional counterterm habitats.

The tested eight-face expression has row vector
\[
  (2,-2,3,2,-1,1,-2,-3)
\]
on
\[
  E_{\nu_{02}},E_{\nu_{20}},E_{\nu_{03}},
  E_{\nu_{12}^{(1)}},E_{\nu_{12}^{(2)}},
  E_{\theta_3},E_{\nu_{21}^{(2)}},E_{\nu_{30}}.
\]
Diagonal transport to \(N=2\) leaves
\[
  2E^2_{\nu_{02}}-2E^2_{\nu_{20}}.
\]
The expression remains rejected until a marked Costello incidence/weight table,
codimension-two closure, and lower-window zero residual are supplied.

## Lower Bianchi Classes To Reference

The lower source-coordinate candidate is
\[
  \zeta^0_2=u_{a,H_{1,0}}u_{b,H_{0,1}},\qquad
  D^2_{02,20}=K^2_{\Theta_3}(\zeta^0_2),
\]
with
\[
  d_{\mathrm{CE}}\zeta^0_2
  =
  2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}}.
\]
This is source exactness only. The local-functional Bianchi defect is
\[
  \mathfrak b^2_{02,20}
  =
  d_{\mathrm{ns},2}K^2_{\Theta_3}(\zeta^0_2)
  -
  K^2_{\Theta_3}(d_{\mathrm{CE}}\zeta^0_2),
\]
so
\[
  d_{\mathrm{ns},2}D^2_{02,20}
  =
  -2E^2_{\nu_{02}}+2E^2_{\nu_{20}}
  +\mathfrak b^2_{02,20}.
\]
In the basis
\[
  (E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20}),
\]
the available column and residual are
\[
  A_D^2=(-2,2,1)^T,\qquad r_2=(2,-2,0)^T.
\]
The cokernel certificate is
\[
  \widetilde\lambda_{02,\mathfrak b}
  =
  \frac12(E^2_{\nu_{02}})^*
  +(\mathfrak b^2_{02,20})^*,
\]
\[
  \widetilde\lambda_{02,\mathfrak b}A_D^2=0,\qquad
  \widetilde\lambda_{02,\mathfrak b}(r_2)=1.
\]
The desired Bianchi-killing target is
\[
  -\mathfrak b^2_{02,20}=(0,0,-1)^T,\qquad
  \widetilde\lambda_{02,\mathfrak b}((0,0,-1)^T)=-1.
\]
The minimal controlled enlargement is a genuine scalar-zero local-functional
column
\[
  A_B^2=(0,0,-1)^T,\qquad
  d_{\mathrm{ns},2}B^2_{02,20}
  =
  -\mathfrak b^2_{02,20}.
\]
For a tower, the Bianchi transport cocycle is
\[
  \Delta^1_{M,N}
  =
  -\pi_{M,N}\mathfrak b^M+\mathfrak b^N.
\]
A compatible family must satisfy
\[
  \Delta^1_{M,N}
  =
  d_{\mathrm{ns},N}(\pi_{M,N}B^M-B^N),
\]
then kill the resulting \(H^1\) Bianchi transport class and the secondary
\(\varprojlim^1H^0\) primitive-compatibility class.

## Exact TeX Patch Targets

No TeX patch should be applied without explicit authorization. If editing is
authorized, these are the exact targets.

1. `main.tex:8488-8722`. Keep
   `prob:quantum-p0-operation-realization` as an obstruction-complex problem.
   Patch only to normalize the restricted label habitat:
   \[
     \mathfrak Q^\bullet_{\mathcal G,\Lambda,M}(I)
   \]
   and to state that arbitrary \(\mathcal D'_c(I)\)-labelled graph kernels are
   not part of the proved theorem.

2. `main.tex:8724-8991`. Keep
   `prop:theta-three-finite-window-acceptance-gate` as an obstruction theorem.
   The admissible positive insertions are exactly
   \(A^M_{\theta_3,C}=(-1)\), a marked CE ancestor with
   \(d_{\mathrm{CE}}\eta_{\theta_3,M}=\zeta_{M,\nu_3}\) and Hom-valued
   Bianchi closure, a transport-compatible companion table, or
   \(A_B^2=(0,0,-1)^T\) with
   \(d_{\mathrm{ns},2}B^2_{02,20}=-\mathfrak b^2_{02,20}\).

3. `theorem-lanes.tex:3334-3572`. Keep
   `thm:lane-local-graph-qme-branch-catalogue` as a finite-window branch
   catalogue. Normalize the habitat to the restricted
   \(\Lambda\)-label version if the notation is changed in `main.tex`. Do not
   promote the eight-face row to a theorem.

4. `open-obligations.tex:505-915`. Consolidate the construction tuple as
   \[
     (\mathcal G_M^{\mathrm{mk}},
      \widehat\sigma_{\mathrm{sc},M},
      \kappa_{\hbar,w,I},
      R^{\mathrm{row}}_{\alpha,M},
      A^M,T^{M,N},P^{M,N},\lambda_n)
   \]
   plus one accepted theta3 or lower-Bianchi healing datum.

5. `claim-strength-ledger.tex:496-546`. Keep the status as construction target
   with exact obstruction pair. Harmonize the pure two-\(u\) language with
   `main.tex:8801-8819`: it is an obstruction for the ordinary pure two-\(u\)
   source envelope in every finite Hamiltonian degree, not a universal no-go.

6. `appendix-unreduced-bv-qme.tex:2142-2385`. If notation is normalized, add
   the \(\Lambda\)-restricted local-functional habitat or a sentence pointing
   to the regular-density/wavefront restriction.

7. `appendix-unreduced-bv-qme.tex:2873-3314`. Use
   `thm:app-minimal-full-equivariant-kernel-vanishing`,
   `thm:app-minimal-full-equivariant-all-order-vanishing`, and
   `prop:app-first-order-three-larger-package-datum` as the positive minimal
   branch and larger-package boundary. Do not weaken these statements.

## Verification

Commands run:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py
```

The script reports: minimal full-equivariant order-two branch solved by zero
counterterm with zero Roos class; theta3 one-row subcomplex obstructed by
\(\ell_{\theta_3}\); exact theta3 payload fixtures accepted only when
\(dC=-E\), scalar-zero value, \(TA=AP\), and Roos zero are supplied; eight-face
candidate rejected by the nonzero \(N=2\) residual and missing marked Costello
table.
