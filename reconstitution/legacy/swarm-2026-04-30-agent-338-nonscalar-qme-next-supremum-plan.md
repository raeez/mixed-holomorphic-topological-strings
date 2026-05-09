# Agent 338: Non-Scalar Costello/QME Next Supremum Plan

## Verdict

The present manuscript has a proved componentwise coefficient surface and a
proved minimal full-equivariant finite-window non-scalar branch. It does not
yet have a larger non-scalar Costello graph/QME construction. The obstruction is
not one scalar anomaly. It is the ordered construction stack
\[
\widehat\sigma_{\mathrm{sc}}
\;\longrightarrow\;
\mathcal G^{\mathrm{mk}}_M,\mathsf A^{\mathrm{fw}}_{n,M}
\;\longrightarrow\;
A^M c=-r^M
\;\longrightarrow\;
(T^{M,N},P^{M,N}),\lambda
\;\longrightarrow\;
H^{\mathrm{cent}}
\;\longrightarrow\;
\operatorname{Curv}(\kappa+C)=0 .
\]

Supremum target: do not demote the non-scalar QME theorem. Build the missing
finite-window local-functional column for the first certified larger row
\(\theta_3\), then propagate it through the transition/Roos tower. The next
upgradeable statement is a finite-window \(\theta_3\) Bianchi-counterterm
theorem, not the full all-graph Costello theorem.

## Anchors

- `main.tex:8618`: the non-scalar Costello graph/QME frontier is formulated as
  a filtered local-functional vanishing problem, not as a consequence of the
  componentwise surface.
- `main.tex:8633`: the scalar-symbol projection is only associated graded until
  it is lifted through the scalar-contact filtration.
- `main.tex:8680`: after the scalar lift, the branch requires a continuous
  bulk-to-defect kernel \(\kappa_{\hbar,w,I}\).
- `main.tex:8726`: counterterms close the first non-scalar order exactly on
  the vanishing locus of \(\mathfrak O^{\mathrm{ns}}_{n_0}\).
- `main.tex:8733`: a closed-exchange repair requires extra complexes
  \(\mathcal X^\bullet_{w,M}(I)\), maps \(\Xi_M\), and the branch equation.
- `main.tex:8790`: unreduced centrality is the same finite-window matrix
  problem \(A^Mh^M=-r^M\).
- `main.tex:8815`: the desired construction is
  \(\operatorname{Curv}(\kappa_{\hbar,w,I}+C_{\hbar,w})=0\), with finite-window
  compatibility.
- `main.tex:8852`: the \(\theta_3\) acceptance gate gives the first certified
  larger-row test.
- `appendix-unreduced-bv-qme.tex:2078`: the non-scalar complex is
  \(\ker\widehat\sigma_{\mathrm{sc},M}\) and exists only if the scalar
  projection is a filtered chain map.
- `appendix-unreduced-bv-qme.tex:2248`: the constructive finite-row criterion
  gives the theorem-grade matrix problem and Roos obstruction.
- `appendix-unreduced-bv-qme.tex:2501`: the lower \(\theta_3\) Bianchi gate
  supplies the concrete next matrix target.
- `claim-strength-ledger.tex:221`: the quantum coefficient surface is proved
  componentwise, not graph/QME.
- `claim-strength-ledger.tex:500`: the larger non-scalar Costello/QME branch is
  a construction target with exact obstruction pair.

## Attack

1. Componentwise data do not define the larger non-scalar complex. The surface
   \[
   \mathfrak S_{\hbar,w}(I)=
   \mathcal K^w_{\mathrm{BV}}\times\{0_{\mathrm{sc}}\}
   \times A^{\mathrm{pp},w}_{\partial,\hbar}(I)
   \times T_{\mathrm{Ham},\hbar}
   \]
   is proved, but the manuscript explicitly says this is not a Costello
   graph/QME construction (`open-obligations.tex:498`, `open-obligations.tex:543`).

2. The first gate is scalar projection lift. A filtered chain projection
   \[
   \widehat\sigma_{\mathrm{sc}}\colon
   \mathfrak Q^\bullet_{w,\partial,\hbar}(I)\to
   C^\bullet_{\mathrm{Lie}}(\bar A;\C\gamma_{\mathbf1})[1][[\hbar]]
   \]
   exists only after the successive classes
   \[
   o_{\sigma,w}^{(r)}(I)\in
   H^1\!\left(
   \operatorname{Hom}(\operatorname{gr}_F\mathfrak Q^\bullet_{w,\partial,\hbar}(I),
   C^\bullet_{\mathrm{Lie}}(\bar A;\C\gamma_{\mathbf1})[1][[\hbar]])_{-r}
   \right)
   \]
   vanish compatibly (`main.tex:8636`, `main.tex:8653`;
   `appendix-unreduced-bv-qme.tex:185`). On balanced scalar-contact habitats
   this is solved by \(\widehat\sigma_{\mathrm{bal,sc}}=0\). On a full
   graph/counterterm habitat the relative defects
   \(\delta^{(0)}_{\mathrm{Cost},\sigma}\) and
   \(\mathfrak o^{(r)}_{\mathrm{Cost},\sigma}\) must be killed
   (`appendix-unreduced-bv-qme.tex:1038`).

3. The finite row array is missing unless every graph face is supplied.
   A larger package must give a codimension-two closed marked Costello list
   \(\mathcal G^{\mathrm{mk}}_M\) with output graph, coefficient, marker
   transport, incidence sign, and lower-window truncation for each
   field-differential, BV-edge, collision/contact, counterterm, and CE-source
   face (`open-obligations.tex:546`; `appendix-unreduced-bv-qme.tex:2142`).
   Without this table there is no defined \(H^1/\varprojlim^1\) non-scalar
   class.

4. Once the scalar gate vanishes, the finite problem is linear algebra:
   \[
   R^{\mathrm{ns}}_{n,M}=\sum_i r^M_i\rho^M_i,\qquad
   d_{\mathrm{ns},M}\eta^M_j=\sum_iA^M_{ij}\rho^M_i,\qquad
   A^Mc=-r^M .
   \]
   Failure is certified by \(\ell A^M=0,\ \ell(r^M)\ne0\)
   (`open-obligations.tex:671`; `appendix-unreduced-bv-qme.tex:2316`).
   In a tower one must also construct
   \[
   T^{M,N}r^M=r^N,\qquad T^{M,N}A^M=A^NP^{M,N},\qquad
   [P^{M,N}c_M-c_N]=0\in H^0(\mathcal K^\bullet_{\mathrm{ns},N}(I)).
   \]

5. The \(\theta_3\) row is the first certified larger obstruction. In the
   supplied one-row complex
   \[
   \mathcal Q^0_{\theta_3,M}=0,\qquad
   \mathcal Q^1_{\theta_3,M}=\C\mathsf E_{\theta_3,M},\qquad d_M=0,
   \]
   with
   \[
   \mathsf E_{\theta_3,M}=-K^M_{\Theta_3}(\zeta_{M,\nu_3}),\qquad
   \ell_{\theta_3}(\mathsf E_{\theta_3,M})=1,
   \]
   the class is nonzero (`main.tex:8852`; `appendix-unreduced-bv-qme.tex:2401`).
   A named \(C_{\theta_3}\) is not a counterterm unless
   \[
   d_MC_{\theta_3,M}=-\mathsf E_{\theta_3,M},\qquad
   \widehat\sigma_{\mathrm{sc},M}(C_{\theta_3,M})=0,
   \]
   and the tower class
   \[
   [\pi_{M,N}C_{\theta_3,M}-C_{\theta_3,N}]=0
   \in H^0(\mathcal Q^\bullet_{w,N}(I))
   \]
   vanishes (`main.tex:8888`, `main.tex:8905`).

6. The tested source routes are obstructed. In the ordinary pure two-\(u\)
   source envelope, \(q_{2u}d_{\mathrm{CE}}=0\) and
   \(q_{2u}(\zeta_{M,\nu_3})=1\), so no pure CE ancestor exists there
   (`open-obligations.tex:838`; `theorem-lanes.tex:3493`). The eight-face
   companion row transports to \(2E^2_{\nu_{02}}-2E^2_{\nu_{20}}\) and is
   detected by \(\lambda^{(2)}_{\nu_{02}}\) (`open-obligations.tex:858`;
   `theorem-lanes.tex:3511`). These are exact obstructions for the tested
   habitats, not universal no-go theorems.

## Next Construction

Construct the scalar-zero Bianchi counterterm column for the lower
\(\theta_3\) gate, then lift it through the finite-window tower.

The source-coordinate primitive is known:
\[
\zeta^0_2=u_{a,H_{1,0}}u_{b,H_{0,1}},\qquad
D^2_{02,20}=K^2_{\Theta_3}(\zeta^0_2),\qquad
d_{\mathrm{CE}}\zeta^0_2=2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}} .
\]
It is only source exactness. The local-functional Bianchi defect is
\[
\mathfrak b^2_{02,20}
=d_{\mathrm{ns},2}K^2_{\Theta_3}(\zeta^0_2)
-K^2_{\Theta_3}(d_{\mathrm{CE}}\zeta^0_2).
\]
In the basis
\((E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20})\),
\[
A_D^2=(-2,2,1)^T,\qquad r_2=(2,-2,0)^T .
\]
The equation \(A_D^2c=-r_2\) is inconsistent; the cokernel
\[
\widetilde\lambda_{02,\mathfrak b}
=\frac12(E^2_{\nu_{02}})^*+(\mathfrak b^2_{02,20})^*
\]
satisfies
\[
\widetilde\lambda_{02,\mathfrak b}A_D^2=0,\qquad
\widetilde\lambda_{02,\mathfrak b}(r_2)=1 .
\]
The exact next column is therefore
\[
A_B^2=(0,0,-1)^T,\qquad
d_{\mathrm{ns},2}B^2_{02,20}=-\mathfrak b^2_{02,20},\qquad
\widehat\sigma_{\mathrm{sc},2}(B^2_{02,20})=0,
\]
with locality or graphwise wavefront admissibility. Then
\[
d_{\mathrm{ns},2}(D^2_{02,20}+B^2_{02,20})
=-2E^2_{\nu_{02}}+2E^2_{\nu_{20}}=-r_2 .
\]
This is the first upgradeable fixed-window theorem (`appendix-unreduced-bv-qme.tex:2501`;
`main.tex:9087`).

For the inverse system, construct \(B^M\) and prove
\[
\Delta^1_{M,N}:=-\pi_{M,N}\mathfrak b^M+\mathfrak b^N
=d_{\mathrm{ns},N}(\pi_{M,N}B^M-B^N),
\]
then kill the secondary primitive class in
\[
\varprojlim\nolimits^1_N H^0(\mathcal K^\bullet_{\mathrm{ns},N}(I)).
\]
Without these two gates the fixed-window Bianchi column is not a Costello/QME
counterterm tower (`appendix-unreduced-bv-qme.tex:2581`).

## Upgrade Path

1. Prove the relative scalar projection lift for the intended
   graph/counterterm habitat:
   \[
   \delta^{(0)}_{\mathrm{Cost},\sigma}=0,\qquad
   \mathfrak o^{(r)}_{\mathrm{Cost},\sigma}=0\quad(r>0).
   \]
   Status: construction target. This is required before forming the larger
   \(\ker\widehat\sigma_{\mathrm{sc}}\).

2. Build the finite marked row table containing the \(\theta_3\) source face,
   the lower Bianchi column \(B^M\), all companion faces, signs, and transport
   matrices. Status: exact finite data target.

3. Solve the fixed-window matrix by adding the column \(A_B^2=(0,0,-1)^T\),
   then propagate it:
   \[
   T^{M,N}r^M=r^N,\qquad T^{M,N}A^M=A^NP^{M,N},\qquad
   [P^{M,N}c_M-c_N]=0 .
   \]
   Status: first theorem upgrade after construction.

4. Add centrality homotopy rows only after the same finite table is present:
   \[
   R^{\mathrm{cent}}_{x,y,M}
   =
   \operatorname{Curv}_{\mathbf K,M}(\kappa^M_{\mathcal G,w,I})(x\wedge y),
   \qquad
   R^{\mathrm{cent}}_{x,y,M}+d_MH^M_{x,y}=0.
   \]
   Status: zero only in the minimal branch; enlarged packages must provide
   row values, scalar gate, primitive, and transition coefficients
   (`appendix-unreduced-bv-qme.tex:3473`).

5. Only then assert the curved bulk-to-defect kernel:
   \[
   \operatorname{Curv}(\kappa_{\hbar,w,I}+C_{\hbar,w})
   =
   d_{\mathrm{QME}}(\kappa_{\hbar,w,I}+C_{\hbar,w})
   +\frac12[\kappa_{\hbar,w,I}+C_{\hbar,w},
   \kappa_{\hbar,w,I}+C_{\hbar,w}]_\hbar=0 .
   \]
   Status: full construction target, not currently proved.

## Statement To Upgrade Next

Upgrade next: the \(\theta_3\) finite-window acceptance gate, by adjoining a
theorem-grade local-functional Bianchi counterterm \(B^M_{02,20}\) with
scalar-zero value, locality or wavefront habitat, transition identity, and zero
Roos class. This upgrades the current exact obstruction statement to a solved
finite-window \(\theta_3\) counterterm-column theorem. It does not claim the
full Costello graph/QME solution.

Do not upgrade next: the whole componentwise quantum coefficient surface to a
full graph/QME theorem. That would skip the scalar projection lift, finite row
array closure, centrality homotopies, and curved bulk-to-defect kernel.

## Report Status

Files changed: this report only.

TeX/scripts changed: none.
