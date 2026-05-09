# Non-scalar Costello QME Frontier Attack-Heal

Date: 2026-04-30.
Status: report-only. No manuscript TeX, scripts, figures, sources, or build
files were edited.

## Claim Attacked

The attacked claim is that the current finite-row and Costello source data
already prove the full non-scalar Costello graph/QME realization for the local
mixed holomorphic-topological model on
\[
  \mathbb R^2_{\mathrm{top}}\times \mathbb C^2_{\mathrm{hol}}.
\]

That claim is false. The strongest theorem surface now admissible is the native
finite-window local-functional obstruction theorem, with a proved minimal
full-equivariant zero branch in its named habitat and a sharp obstruction class
for every larger graph/counterterm package until the missing construction data
are supplied.

## Source Floor

Costello's finite-scale BV/RG/QME graph calculus supports heat-kernel
propagators, regularized BV Laplacians, graphwise local counterterms, RG/QME
compatibility, and local obstruction classes. The local source fixture records
this support at
`references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md:40-130`.
It also records the non-support: no automatic current-valued target, no theorem
for arbitrary \(\mathcal D'_c(I)\)-labelled defect graphs, and no automatic
bulk-to-defect kernel
(`references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md:156-240`).

The manuscript already contains the correct obstruction grammar:

- `main.tex:8428-8662`: non-scalar quantum \(P_0\) and Costello graph/QME
  obstruction complex.
- `main.tex:8664-8931`: \(\theta_3\) finite-window acceptance gate and lower
  Bianchi obstruction.
- `theorem-lanes.tex:3318-3555`: local graph/QME branch catalogue.
- `open-obligations.tex:458-906`: non-scalar construction obligations and
  \(\theta_3\) finite-row obstruction.
- `claim-strength-ledger.tex:104-122`, `claim-strength-ledger.tex:216-234`,
  `claim-strength-ledger.tex:487-537`: claim-strength controller for the
  minimal branch and larger non-scalar Costello/QME package.
- `appendix-unreduced-bv-qme.tex:1998-2075`: full-equivariant marked scalar
  shadow vanishing.
- `appendix-unreduced-bv-qme.tex:2077-2232`: non-scalar kernel complex and
  native finite-window realization habitat.
- `appendix-unreduced-bv-qme.tex:2234-2385`: constructive non-scalar
  Costello/QME realization criterion.
- `appendix-factorization-current-conventions.tex:992-1277`: unreduced
  current lift, convolution habitat, coefficient-current kernel, and
  Hom-valued obstruction class.
- `appendix-factorization-current-conventions.tex:1279-1860`: regular-density,
  wavefront-admissible, and sign-conic graph-current habitats.
- `tate-P1-hadamard-mittag-leffler.tex:379-696`: finite-window graph/QME
  package, finite-window assembly, and inverse-limit obstruction.
- `tate-T1-weighted-completion.tex:1172-1327`: non-scalar finite-window tower
  and counterterm criterion.

## Strongest Admissible Theorem Surface

The theorem surface is the following finite-window obstruction theorem.

Fix a finite Hamiltonian window \(M\), interval \(I\), admissible degree weight
\(w\), and finite connected graph package \(\mathcal G_M\). The only
currently defensible local-functional habitat is
\[
  \mathfrak Q^\bullet_{\mathcal G,\Lambda,M}(I)
  =
  \left(
  \mathcal O^{\mathrm{bd}}_{\mathrm{loc},\mathcal G,\Lambda,M}
  (\mathcal E_w^M|_I;A^{\mathrm{pp},w,M}_{\partial,\hbar}(I)),
  d_M
  \right),
  \qquad
  d_M=Q+\{I^w_{0,M},-\}_{\hbar,M}.
\]
The completion is the \(\hbar\)-adic, scalar-contact, and finite-window
completion. The defect-current labels are restricted to regular compactly
supported densities, graphwise wavefront-admissible tuples
\(\mathcal D'_{c,\mathrm{WF}}(I;\Gamma,M)\), or one-sided finite-scaling
sign-conic classes \(\mathcal D'_{c,\Lambda_\pm,\mathrm{fs}}(I)\) when the
ordinary collision-conormal criterion applies. There is no theorem for all
\(\mathcal D'_c(I)\).

The Hom-valued graph kernel habitat is
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
  [T_1,T_2]_{\mathbf K,M}
  =
  [-,-]_{\hbar,M}\circ(T_1\widehat\otimes T_2)\circ\Delta_{\mathrm{CE}},
\]
and
\[
  \operatorname{Curv}_{\mathbf K,M}(\kappa)
  =
  d_{\mathbf K,M}\kappa+\frac12[\kappa,\kappa]_{\mathbf K,M}.
\]
The source-face term \(-\kappa d_{\mathrm{CE}}\) is part of the QME
differential.

The zero-edge kernel values are fixed by the coefficient-current layer:
\[
  \kappa^{\mathrm{coef},M}_{\hbar,w,I}(u_{a(t)dt\otimes f})
  =
  \iota_I(B^{w,M}_f(a)),
  \qquad
  \kappa^{\mathrm{coef},M}_{\hbar,w,I}(c_{B,\rho})
  =
  \iota_I(\Theta^{w,M}_\rho(B)).
\]
Positive-edge values are not formal names. They must be actual renormalized
graph weights
\[
  K^M_\Gamma=W^{R,M}_{\Gamma,L,w}(B^\Gamma_\bullet)
\]
with the support, wavefront, finite-scaling, interval-extension,
finite-window, and weight-transport compatibility data recorded in the
finite-window package.

Before a non-scalar complex exists, the scalar projection must be a filtered
chain map:
\[
  \widehat\sigma_{\mathrm{sc},M}\colon
  \mathfrak Q^\bullet_{\mathcal G,\Lambda,M}(I)
  \longrightarrow
  C^\bullet_{\mathrm{Lie}}(\bar A;\mathbb C\gamma_{\mathbf 1})[1][[\hbar]].
\]
Then
\[
  \mathcal K^\bullet_{\mathrm{ns},M}(I)
  =
  \ker\widehat\sigma_{\mathrm{sc},M},
  \qquad
  d_{\mathrm{ns},M}=d_M|_{\mathcal K_{\mathrm{ns},M}}
\]
is a complex. If \(\widehat\sigma_{\mathrm{sc},M}\) is only an associated
graded scalar symbol, \(\ker\widehat\sigma_{\mathrm{sc},M}\) is not a QME
complex. The scalar-contact lift obstructions are the classes
\[
  o_{\sigma,w}^{(r)}(I)
  \in
  H^1\!\left(
    \operatorname{Hom}(
      \operatorname{gr}_F\mathfrak Q^\bullet_{w,\partial,\hbar}(I),
      C^\bullet_{\mathrm{Lie}}(\bar A;\mathbb C\gamma_{\mathbf 1})[1][[\hbar]]
    )_{-r}
  \right),
  \qquad r>0.
\]
They vanish on the full-equivariant marked habitat only after the
codimension-two marked Costello list and full-equivariant marker tensors have
been supplied. Outside that habitat they are open obstruction classes.

At order \(n\), after lower counterterms \(C_{<n,M}\), the mandatory row types
are
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
Only when \(\mathfrak s_{n,M}=0\) is the non-scalar residual formed:
\[
  R^{\mathrm{ns}}_{n,M}
  =
  \sum_i r_i^M\rho_i^M
  \in Z^1(\mathcal K^\bullet_{\mathrm{ns},M}(I)).
\]
With degree-zero primitive candidates \(\eta_j^M\),
\[
  d_{\mathrm{ns},M}\eta_j^M=\sum_i A^M_{ij}\rho_i^M.
\]
The fixed-window counterterm exists exactly when
\[
  A^Mc_M=-r^M.
\]
Failure is certified by a left cokernel
\[
  \ell A^M=0,\qquad \ell(r^M)\neq0.
\]
An inverse-limit theorem additionally requires
\[
  T^{M,N}r^M=r^N,\qquad
  T^{M,N}A^M=A^NP^{M,N},\qquad
  [P^{M,N}c_M-c_N]=0
  \in H^0(\mathcal K^\bullet_{\mathrm{ns},N}(I)).
\]
Equivalently, the finite-window obstruction pair is
\[
  \mathfrak O^{\mathrm{ns}}_n
  =
  \bigl(([\mathfrak o^{\mathrm{ns}}_{n,M}])_M,\lambda_n\bigr),
\]
where \(\lambda_n\in\varprojlim^1_MH^0(\mathcal K^\bullet_{\mathrm{ns},M})\)
is the primitive-compatibility class.

A closed-exchange repair is not a scalar-QME slogan. It is the extra tower
\(\mathcal X^\bullet_{w,M}(I)\), compatible cochain maps
\[
  \Xi_M\colon \mathcal X^\bullet_{w,M}(I)\to\mathcal K^\bullet_{\mathrm{ns},M}(I),
\]
and cocycles \(W_{n_0,M}\) satisfying
\[
  \mathfrak o^{\mathrm{ns}}_{n_0,M}
  +\Xi_M(W_{n_0,M})
  +d_MC_{n_0,M}=0.
\]
The inverse-limit obstruction is
\[
  (\beta^{\mathrm{cl}}_{n_0},\mu^{\mathrm{cl}}_{n_0},\lambda^{\mathrm{cl}}_{n_0}),
\]
with \(\beta^{\mathrm{cl}}\) the cokernel of
\(\varprojlim H^1(\Xi_M)\), \(\mu^{\mathrm{cl}}\in\varprojlim^1H^0(\mathcal X)\),
and \(\lambda^{\mathrm{cl}}\in\varprojlim^1H^0(\mathcal K_{\mathrm{ns}})\).

This is the strongest admissible theorem: a constructive finite-window
obstruction criterion. The full non-scalar graph/QME theorem is proved only
after every obstruction in this theorem surface vanishes by supplied data.

## Proved Positive Branch

The minimal full-equivariant finite-window branch is proved in its named
habitat. In the minimal marked list generated by the strict current-interface
rows, the one-cross scalar-contact row, and subset-deletion closure, the
full-equivariant \(\mathfrak{gl}(N|N)\) marker tensor has zero cyclic
supertrace, and every retained positive-order non-scalar row has zero
local-functional value. Thus
\[
  R^{\mathrm{ns}}_{n,M}=0,\qquad
  \mathfrak o^{\mathrm{ns}}_{n,M}=0,\qquad
  C_{n,M}=0
\]
for every \(n\geq1\) in that minimal habitat. The binary centrality row there
is
\[
  A^M_{\min}:0\to0,\qquad r^M_{\min}=0,\qquad h^M_{\min}=0,
\]
with zero Roos class. This theorem does not apply to a larger package with
new positive-order seeds, new CE-source rows, new graph-counterterm faces,
nonzero scalar-zero rows, or nonminimal lower counterterms.

## Exact Obstruction Surface

The first supplied larger-row obstruction is the \(\theta_3\) source-face row.
The current finite-row subcomplex is
\[
  \mathcal Q^0_{\theta_3,M}=0,\qquad
  \mathcal Q^1_{\theta_3,M}=\mathbb C\mathsf E_{\theta_3,M},\qquad d_M=0,
\]
with
\[
  \mathsf E_{\theta_3,M}
  =
  -K^M_{\Theta_3}(\zeta_{M,\nu_3}),\qquad
  \widehat\sigma_{\mathrm{sc},M}(\mathsf E_{\theta_3,M})=0.
\]
The covector
\[
  \ell_{\theta_3}(\mathsf E_{\theta_3,M})=1
\]
detects the nonzero fixed-window class. In row-matrix form,
\[
  A^M_{\theta_3}=[\,]_{1\times0},\qquad r^M=(1),
\]
so the fixed-window equation has no solution.

The row is killed precisely by one of three kinds of supplied data:
\[
  \text{direct column:}\quad
  A^M_{\theta_3,C}=(-1),\qquad
  d_MC_{\theta_3,M}=-\mathsf E_{\theta_3,M},
\]
with scalar-zero value and zero Roos class;
\[
  \text{marked source ancestor:}\quad
  d_{\mathrm{CE}}\eta_{\theta_3,M}=\zeta_{M,\nu_3},
  \qquad
  d_MK^M_{\Theta_3}(\eta_{\theta_3,M})=-\mathsf E_{\theta_3,M},
\]
with Hom-valued Bianchi closure, codimension-two closure, scalar-zero value,
and compatible transport; or a complete companion-face table with signed row
sum zero and transport-preserved zero residual.

The ordinary pure two-\(u\) CE-source route is blocked in the current source
envelope. The covector
\[
  q_{2u}
  =
  e^*_{((H_{0,1},H_{2,0}),c_{\rho_{2,1}})}
  -\frac12 e^*_{((H_{0,1},H_{0,1}),c_{\rho_{0,2}})}
\]
satisfies
\[
  q_{2u}d_{\mathrm{CE}}=0,\qquad q_{2u}(\zeta_{M,\nu_3})=1.
\]
Thus no ordinary pure two-\(u\) degree enlargement supplies the needed
ancestor. This is an obstruction theorem for that source envelope only; it
does not exclude marked-source, Hom-valued companion, or local-functional
counterterm habitats.

The tested eight-face companion expression has row vector
\[
  (2,-2,3,2,-1,1,-2,-3)
\]
on
\[
  E_{\nu_{02}},E_{\nu_{20}},E_{\nu_{03}},
  E_{\nu_{12}^{(1)}},E_{\nu_{12}^{(2)}},
  E_{\theta_3},E_{\nu_{21}^{(2)}},E_{\nu_{30}}.
\]
Its coefficient sum is zero, but it is not the zero row. Diagonal transport
to \(N=2\) leaves
\[
  2E^2_{\nu_{02}}-2E^2_{\nu_{20}}.
\]
The marked Costello incidence/weight table is also absent: the source
coefficients do not determine graph weights, marker transport, signs, or
codimension-two closure.

The lower source-coordinate candidate is
\[
  \zeta^0_2=u_{a,H_{1,0}}u_{b,H_{0,1}},\qquad
  D^2_{02,20}=K^2_{\Theta_3}(\zeta^0_2),
\]
with
\[
  d_{\mathrm{CE}}\zeta^0_2=2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}}.
\]
This proves source exactness only. In the local-functional complex,
\[
  \mathfrak b^2_{02,20}
  =
  d_{\mathrm{ns},2}K^2_{\Theta_3}(\zeta^0_2)
  -
  K^2_{\Theta_3}(d_{\mathrm{CE}}\zeta^0_2),
\]
and
\[
  d_{\mathrm{ns},2}D^2_{02,20}
  =
  -2E^2_{\nu_{02}}+2E^2_{\nu_{20}}+\mathfrak b^2_{02,20}.
\]
In the Bianchi-exposed basis
\[
  (E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20}),
\]
the available column and residual are
\[
  A_D^2=(-2,2,1)^T,\qquad r_2=(2,-2,0)^T.
\]
The left cokernel
\[
  \widetilde\lambda_{02,\mathfrak b}
  =
  \frac12(E^2_{\nu_{02}})^*
  +(\mathfrak b^2_{02,20})^*
\]
satisfies
\[
  \widetilde\lambda_{02,\mathfrak b}A_D^2=0,\qquad
  \widetilde\lambda_{02,\mathfrak b}(r_2)=1.
\]
The current habitat also contains no column killing the Bianchi defect. The
target
\[
  -\mathfrak b^2_{02,20}=(0,0,-1)^T
\]
is not in the image of \(A_D^2\), since
\[
  \widetilde\lambda_{02,\mathfrak b}((0,0,-1)^T)=-1.
\]
The minimal controlled enlargement must add a genuine scalar-zero
local-functional column
\[
  A_B^2=(0,0,-1)^T,\qquad
  d_{\mathrm{ns},2}B^2_{02,20}=-\mathfrak b^2_{02,20},
\]
with regular-density or wavefront-admissible locality and compatible
finite-window transport:
\[
  d_{\mathrm{ns},N}(\pi_{M,N}B^M-B^N)
  =
  -\pi_{M,N}\mathfrak b^M+\mathfrak b^N,
\]
followed by vanishing of the resulting \(H^1\) Bianchi transport class and
secondary \(\varprojlim^1H^0\)-class.

## Attack-Heal Verdict

Constructed:

- The filtered local-functional habitat, after restricting current labels to
  regular, graphwise wavefront-admissible, or sign-conic finite-scaling
  classes.
- The Hom-valued graph/QME differential and curvature formula.
- The coefficient-current zero-edge bulk-to-defect kernel.
- The regular-density and wavefront-admissible graph kernel layers.
- The full-equivariant marked scalar-shadow vanishing theorem on complete
  finite marked habitats.
- The finite-window counterterm criterion
  \(\mathfrak O_n^{\mathrm{ns}}=0\).
- The minimal full-equivariant all-order zero branch in its named habitat.
- The exact one-row \(\theta_3\) obstruction and lower Bianchi matrix
  obstruction in the current finite-row habitat.

Not constructed:

- A full arbitrary-\(\mathcal D'_c(I)\) Costello graph theorem.
- A global all-graph summability datum.
- A filtered scalar projection on arbitrary enlarged graph/counterterm
  habitats.
- A complete codimension-two closed marked Costello table for the larger
  \(\theta_3\) package.
- A direct \(\theta_3\) scalar-zero local counterterm or marked source
  ancestor.
- The lower Bianchi-killing local-functional column \(B^2_{02,20}\).
- The closed-exchange tower \(\mathcal X^\bullet\), maps \(\Xi\), and class
  \(W\) mapping to the negative residual.

Therefore the full non-scalar Costello graph/QME realization remains an exact
construction target, not a theorem. The admissible theorem surface is the
finite-window obstruction criterion plus the named minimal zero branch.

## Exact TeX Patch Targets

No TeX patch was applied. If manuscript editing is authorized later, the exact
targets are:

1. `main.tex:8428-8662`. Retain the obstruction-complex status. Patch only to
   insert the restricted \(\Lambda\)-label habitat
   \(\mathfrak Q^\bullet_{\mathcal G,\Lambda,M}(I)\) and to state explicitly
   that the arbitrary \(\mathcal D'_c(I)\) graph theorem is false without
   wavefront/counterterm data.
2. `main.tex:8664-8931`. Keep the \(\theta_3\) proposition as an obstruction
   theorem. If expanded, add the direct top-window column
   \(A^M_{\theta_3,C}=(-1)\), the lower column
   \(A_B^2=(0,0,-1)^T\), and the finite-window transport equation in one
   displayed block.
3. `theorem-lanes.tex:3318-3555`. Align the local branch catalogue with the
   restricted label habitat and make the larger-package row-data obstruction
   the controlling statement. Do not promote the eight-face source row.
4. `open-obligations.tex:502-662` and `open-obligations.tex:750-906`.
   Consolidate the construction target as:
   \[
     (\mathcal G_M^{\mathrm{mk}},
      \widehat\sigma_{\mathrm{sc},M},
      \kappa_{\hbar,w,I},
      R^{\mathrm{row}}_{\alpha,M},
      A^M,
      T^{M,N},P^{M,N},
      \lambda_n)
   \]
   plus either \(C^{\mathrm{ct}}_{\theta_3,M}\),
   \(\eta^{\mathrm{mark}}_{\theta_3,M}\), a transport-compatible companion
   table, or \(B^2_{02,20}\).
5. `claim-strength-ledger.tex:503-537`. Harmonize the \(\theta_3\) source
   obstruction wording with `main.tex:8741-8759`: the pure two-\(u\) obstruction
   is for the ordinary pure two-\(u\) source envelope, not a universal no-go,
   and the current manuscript states it in every finite Hamiltonian degree.
6. `appendix-unreduced-bv-qme.tex:2142-2232` and
   `appendix-unreduced-bv-qme.tex:2234-2385`. If notation is normalized, add
   the \(\Lambda\)-subscript or a sentence pointing to the
   regular-density/wavefront label restriction.
7. `tate-P1-hadamard-mittag-leffler.tex:379-483`,
   `tate-P1-hadamard-mittag-leffler.tex:485-696`, and
   `tate-P1-hadamard-mittag-leffler.tex:698-880`. Normalize notation between
   \(\iota_{\alpha,M}K^M_\Gamma\) and
   \(-\varepsilon^{\mathrm{CE}}_{\Gamma,\nu}K^M_\Gamma(\zeta_{M,\nu})\) if an
   editor wants one sign convention throughout. This is notation, not a new
   theorem.

## Remaining Construction Obligations

1. Construct a codimension-two closed finite marked Costello list
   \(\mathcal G_M^{\mathrm{mk}}\) for the larger package, including every
   field-differential, BV-edge, collision/contact, counterterm, and CE-source
   face with output graph, coefficient, incidence sign, marker transport, and
   lower-window truncation.
2. Prove the scalar projection lift:
   \(o_{\sigma,w}^{(r)}(I)=0\) for the chosen graph/counterterm habitat, or
   compute the first nonzero class.
3. Construct the continuous bulk-to-defect graph kernel in the restricted
   local-functional habitat, with positive-edge values
   \(K^M_\Gamma=W^{R,M}_{\Gamma,L,w}(B^\Gamma_\bullet)\).
4. Fill row bases and matrices \(u^{M,N}\), \(v^{M,N}\), \(q^{M,N}\),
   \(T^{M,N}\), and \(P^{M,N}\) from actual row coordinates.
5. Supply one accepted \(\theta_3\) heal: direct local counterterm,
   marked-source ancestor, complete companion-face table, or lower
   Bianchi-killing counterterm \(B^2_{02,20}\).
6. Prove the Roos compatibility class vanishes after primitives are chosen.
7. If using closed exchange, construct \(\mathcal X^\bullet\), \(\Xi\), and
   \(W\) and kill
   \((\beta^{\mathrm{cl}},\mu^{\mathrm{cl}},\lambda^{\mathrm{cl}})\).

## Verification

Commands run:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py
rg -n "non[- ]scalar|Costello|QME|finite[- ]window|bulk-to-defect|counterterm|theta_3|scalar projection" main.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex reconstitution
```

Observed executable floor:

```text
minimal_full_equivariant_order_2_zero:
  primitive_exists true; residual empty; counterterm C_{2,M}=0; Roos class 0.
theta_3_current_finite_row_subcomplex:
  primitive_exists false; residual E_theta_3; left covector value 1.
theta3_exact_payload fixtures:
  accepted only when dC=-E, scalar projection zero, T A = A P, and Roos class 0 are supplied.
theta3_eight_face_candidate:
  rejected; residual vector (2,-2,3,2,-1,1,-2,-3), diagonal N=2 transport leaves 2E_nu02-2E_nu20, and the marked Costello incidence/weight table is absent.
```

No PDF build was run because no TeX was edited.
