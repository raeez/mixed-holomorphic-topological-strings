# Non-Scalar Costello/QME Construction Frontier

Status: report-only construction frontier.  No manuscript or script files were
edited.

## Verdict

The current non-scalar QME criterion is not a construction if it merely names a
habitat.  Its stable core is narrower and sharper: after a finite Costello row
table, scalar-contact chain projection, bulk-to-defect kernel, row bases,
counterterm candidates, truncation matrices, and primitive transports are
supplied, it decides whether the order-\(n\) curvature residual is killed.
Before those data exist, the strongest theorem surface is an obstruction
frontier.

The construction target is
\[
  \operatorname{Curv}_{\mathbf K}
    (\kappa_{\mathcal G,w,I}+C_{\hbar,w})=0
\]
in the completed native brane-defect Hom complex.  The corresponding
\(\Omega\)-equivariant target is the same equation over
\(R_\Omega^{N,M}[[\hbar_{\mathrm{QME}}]]\), after the scalar-projection Hom
obstructions and \(Q_\Omega\)-centrality obstructions vanish.

## Construction Frontier

1. Costello row table.

For each finite window one must construct a codimension-two closed marked list
\(\mathcal G_M^{\mathrm{mk}}\).  Its row types are exactly:
\[
  R^{\mathrm{row}}_{d\Gamma,M}
    =\varepsilon_\Gamma d_MK^M_\Gamma,
\]
\[
  R^{\mathrm{row}}_{\mathrm{CE}(\Gamma,\nu),M}
    =-\varepsilon^{\mathrm{CE}}_{\Gamma,\nu}K^M_\Gamma(\zeta_{M,\nu}),
\]
\[
  R^{\mathrm{row}}_{b(\Gamma_1,\Gamma_2),M}
    ={1\over2}\varepsilon_{\Gamma_1,\Gamma_2}
      \{K^M_{\Gamma_1},K^M_{\Gamma_2}\}_{\hbar,M},
\]
plus the lower-counterterm contribution
\[
  [\hbar^n]\left(d_MC_{<n,M}
  +{1\over2}\{C_{<n,M},C_{<n,M}\}_{\hbar,M}\right).
\]
The boundary table must include field-differential, BV-edge, collision/contact,
counterterm, and Hom source faces, with output graph, coefficient, marker
transport, incidence sign, and codimension-two closure.  Missing any one of
these entries blocks the graph complex itself.

2. Local-functional complex.

The target is the completed complex
\[
  \mathfrak Q^\bullet_{\mathcal G,M}(I)=
  \left(
  \mathcal O^{\mathrm{bd}}_{\mathrm{loc},\mathcal G,M}
  (\mathcal E_w^M|_I; A^{\mathrm{pp},w,M}_{\partial,\hbar}(I)),
  d_M=Q+\{I^w_{0,M},-\}_{\hbar,M}
  \right),
\]
completed in the \(\hbar\)-adic, scalar-contact, and finite-window
filtrations.  The Hom complex is
\[
  \mathbf K^\bullet_{\mathcal G,M}(I)
  =
  \operatorname{Hom}_{\mathrm{cont}}
  (C^\bullet_{\mathrm{lab}}(\mathcal G_M),
   \mathfrak Q^\bullet_{\mathcal G,M}(I)),
\]
with
\[
  d_{\mathbf K,M}T=d_MT-(-1)^{|T|}T\,d_{\mathrm{CE}},
  \qquad
  \operatorname{Curv}_{\mathbf K,M}(\kappa)
    =d_{\mathbf K,M}\kappa+{1\over2}[\kappa,\kappa]_{\mathbf K,M}.
\]

3. Scalar-contact lift.

The associated-graded scalar symbol is not enough.  One must choose a complete
\(d_{\mathrm{QME}}\)-stable scalar-contact filtration and construct a filtered
chain map
\[
  \widehat\sigma_{\mathrm{sc},M}\colon
  \mathfrak Q^\bullet_{\mathcal G,M}(I)
  \to C^\bullet_{\mathrm{Lie}}(\bar A;\mathbb C\gamma_{\mathbf 1})[1][[\hbar]].
\]
The exact obstruction theorem target is: the first nonzero class
\[
  o_{\sigma,w}^{(r)}(I)\in
  H^1\operatorname{Hom}
  (\operatorname{gr}_F\mathfrak Q^\bullet_{w,\partial,\hbar}(I),
   C^\bullet_{\mathrm{Lie}}(\bar A;\mathbb C\gamma_{\mathbf 1})[1][[\hbar]])_{-r}
\]
blocks formation of \(\ker\widehat\sigma_{\mathrm{sc}}\).  In the
full-equivariant marked habitat this lift is the zero projection only after
the finite marked list and Brauer marker transport are supplied.

4. Bulk-to-defect kernel.

The source must be a current source such as
\[
  \mathfrak g^{w,\mathrm{cur}}_{\hbar,I}
  =
  (\Omega^\bullet_c(I)\widehat\otimes\mathfrak h_{w,\hbar})
  \ltimes
  (\mathcal D'_c(I)\widehat\otimes
    \mathfrak h^{\vee,w}_{\hbar,\mathrm{cont}})[1],
\]
or the theorem must restrict to regular densities.  The kernel is a continuous
cochain map candidate
\[
  \kappa_{\hbar,w,I}\colon
  C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak g^{w,\mathrm{cur}}_{\hbar,I})
  \to \mathfrak Q^\bullet_{w,\partial,\hbar}(I),
\]
with zero-edge values
\[
  u_{a(t)dt\otimes f}\mapsto \iota_I(B_f^{w,M}(a)),\qquad
  c_{B,\rho}\mapsto\iota_I(\Theta_\rho^{w,M}(B)).
\]
The positive-edge values are actual renormalized weights
\[
  K^M_\Gamma=W^{R,M}_{\Gamma,L,w}(B^\Gamma_\bullet).
\]
Costello supplies the general finite-scale elliptic BV/RG/QME vocabulary, not
this current-valued Hamiltonian kernel.  The exact obstruction target is the
curvature class in
\[
  H^1(\ker\widehat\sigma_{\mathrm{sc}},d_{\mathrm{QME}}).
\]

5. Counterterm recursion and Roos compatibility.

After the scalar gate
\[
  \mathfrak s_{n,M}=\sum_{\alpha\in\mathsf A^{\mathrm{fw}}_{n,M}}S_{\alpha,M}=0
\]
has vanished, the residual is
\[
  R^{\mathrm{ns}}_{n,M}
  =\sum_{\alpha\in\mathsf A^{\mathrm{fw}}_{n,M}}R^{\mathrm{row}}_{\alpha,M}
  \in\mathcal K^1_{\mathrm{ns},M}(I).
\]
With row basis \(\rho_i^M\) and primitive basis \(\eta_j^M\),
\[
  R^{\mathrm{ns}}_{n,M}=\sum_i r_i^M\rho_i^M,\qquad
  d_{\mathrm{ns},M}\eta_j^M=\sum_i A^M_{ij}\rho_i^M.
\]
The fixed-window equation is
\[
  A^Mc=-r^M.
\]
Failure is certified by \(\ell A^M=0\), \(\ell(r^M)\neq0\).  Windowwise
solutions become a compatible tower only after
\[
  T^{M,N}r^M=r^N,\qquad T^{M,N}A^M=A^NP^{M,N},
\]
and the Roos class
\[
  [P^{M,N}c_M-c_N]\in H^0(\mathcal K^\bullet_{\mathrm{ns},N}(I))
\]
vanishes.  Equivalently, the exact order-\(n\) obstruction is
\[
  \mathfrak O^{\mathrm{ns}}_n
  =
  \bigl(([\mathfrak o^{\mathrm{ns}}_{n,M}])_M,\lambda_n\bigr).
\]

The missing projection matrices are not formal decoration: \(u^{M,N}\) for
genuine seed rows, \(v^{M,N}\) for CE-source faces, \(q^{M,N}\) for nonzero
bracket rows, and \(P^{M,N}\) for primitive rows must be computed from actual
row coordinates.

6. Theta3 model obstruction.

The present one-row order-three subcomplex is
\[
  \mathcal K^0_{\theta_3,M}=0,\qquad
  \mathcal K^1_{\theta_3,M}=\mathbb C\mathsf E_{\theta_3,M},\qquad d=0,
\]
with
\[
  \mathsf E_{\theta_3,M}=-K^M_{\Theta_3}(\zeta_{M,\nu_3}),\qquad
  \widehat\sigma_{\mathrm{sc},M}(\mathsf E_{\theta_3,M})=0.
\]
The covector \(\ell_{\theta_3}(\mathsf E_{\theta_3,M})=1\) proves a nonzero
finite-row class in the displayed subcomplex.  The row is killed only by one
of:

- a CE ancestor \(\eta_{\theta_3,M}\) with
  \(d_{\mathrm{CE}}\eta_{\theta_3,M}=\zeta_{M,\nu_3}\) and
  \(d_MK^M_{\Theta_3}(\eta_{\theta_3,M})=-\mathsf E_{\theta_3,M}\);
- a local counterterm \(C^{\mathrm{ct}}_{\theta_3,M}\) with
  \(d_MC^{\mathrm{ct}}_{\theta_3,M}=-\mathsf E_{\theta_3,M}\),
  scalar projection zero, and transport;
- a complete companion-face table whose signed CE-source residual is zero,
  with \(v\)-transport and codimension-two closure.

A named \(C_{\theta_3}\) without \(dC=-E\), scalar-zero value, and tower
compatibility is not evidence.

7. Centrality homotopies.

For \(x,y\in\{u_{a(t)dt\otimes f},c_{B,\rho}\}\), the centrality row is
\[
\begin{aligned}
  R^{\mathrm{cent}}_{x,y,M}
  ={}&
  \sum_{\Gamma\in\mathsf A^d_{x,y,M}}\varepsilon_\Gamma d_MK^M_\Gamma
  -\sum_{\Gamma\in\mathsf A^{\mathrm{CE}}_{x,y,M}}
    \varepsilon^{\mathrm{CE}}_\Gamma K^M_\Gamma(\zeta_{\Gamma,x,y})\\
  &+{1\over2}\sum_{(\Gamma_1,\Gamma_2)\in\mathsf A^{\mathrm{br}}_{x,y,M}}
    \varepsilon_{\Gamma_1,\Gamma_2}
    \{K^M_{\Gamma_1},K^M_{\Gamma_2}\}_{\hbar,M}
  +R^{\mathrm{ct}}_{x,y,M}.
\end{aligned}
\]
Only after its scalar gate vanishes does it define
\(\mathfrak o^{\mathrm{cent}}_{x,y,M}\).  The homotopy datum is an explicit row
\[
  H^M_{x,y}\in\mathcal K^{|x|+|y|-1}_{\mathrm{ns},M}(I),
  \qquad
  R^{\mathrm{cent}}_{x,y,M}+d_MH^M_{x,y}=0,
\]
compatible with finite windows and weights.  In the \(\Omega\)-equivariant
case the primitive must be \(T_\Omega\)-invariant and must kill the secondary
class \([L_{V_\Omega}H]\).

## Obstruction Theorem Targets

- Finite-row completeness obstruction: a missing output graph, coefficient,
  sign, marker transport, source face, or codimension-two closure entry means
  \(d_{\mathrm{mk}}^2\) and the Hom Bianchi identity have not been constructed.
- Scalar-lift obstruction: the first nonzero \(o_{\sigma,w}^{(r)}\), or
  \(o^{(r)}_{\Omega,\sigma,M}\) equivariantly, blocks the non-scalar kernel.
- Current-kernel obstruction: absent wavefront/counterterm rules for
  \(\mathcal D'_c(I)\) labels force restriction to regular densities or a new
  current-compatible Costello theorem.
- Bulk-to-defect obstruction: the class of
  \(d_{\mathrm{QME}}\kappa+\frac12[\kappa,\kappa]\) in
  \(H^1(\ker\widehat\sigma_{\mathrm{sc}},d_{\mathrm{QME}})\) must vanish.
- Counterterm tower obstruction: the first nonzero
  \(\mathfrak O^{\mathrm{ns}}_n\) blocks the recursive QME solution.
- Theta3 obstruction: until a CE ancestor, local counterterm primitive, or
  complete companion-face table is supplied, \(\ell_{\theta_3}\) is a finite-row
  cokernel certificate.
- Centrality obstruction: the classes
  \(\mathfrak o^{\mathrm{cent}}_{x,y,M}\) and the corresponding
  \(\varprojlim^1H^{|x|+|y|-1}\) primitive-compatibility class must vanish.

## Anchors

- `main.tex:7260`: Costello BV package used only under its hypotheses.
- `main.tex:7402`: Hamiltonian specialization datum and required graph data.
- `main.tex:8021`: non-scalar \(P_0\)-operation obstruction complex.
- `main.tex:8232`: theta3 finite-window acceptance gate.
- `appendix-unreduced-bv-qme.tex:1623`: finite-window marked Costello list.
- `appendix-unreduced-bv-qme.tex:1900`: marked habitat and Hom source-face compatibility.
- `appendix-unreduced-bv-qme.tex:2142`: native finite-window realization habitat.
- `appendix-unreduced-bv-qme.tex:2234`: constructive row criterion.
- `appendix-unreduced-bv-qme.tex:2387`: theta3 one-row obstruction.
- `appendix-unreduced-bv-qme.tex:2487`: normal \(\Omega\)-equivariant kernel datum.
- `appendix-unreduced-bv-qme.tex:2709`: equivariant brane-defect QME obstruction criterion.
- `appendix-unreduced-bv-qme.tex:3316`: marked-row centrality homotopy test.
- `appendix-unreduced-bv-qme.tex:3431`: \(Q_\Omega\)-centrality homotopy criterion.
- `scripts/finite_window_graph_array.py:922`: concrete order-three CE source row.
- `scripts/finite_window_graph_array.py:1462`: finite-row primitive-search schema.
- `scripts/finite_window_graph_array.py:1539`: missing larger-package row types.
- `reconstitution/swarm-2026-04-30-agent-198-nonscalar-costello-qme-realization.md:65`: finite-row criterion.
- `reconstitution/swarm-2026-04-30-agent-204-nonscalar-qme-integration-consistency.md:8`: consistency audit.
- `reconstitution/swarm-2026-04-30-agent-214-omega-qme-appendix-repair.md:27`: Omega/QME repair anchors.
- `reconstitution/theta3-source-to-construction-spec-2026-04-30.md:23`: theta3 construction payloads.
- `references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md:38`: source support boundary.

## Verification Commands

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py >/tmp/finite-window-agent220.json
python3 -m json.tool /tmp/finite-window-agent220.json >/tmp/finite-window-agent220.pretty.json
rg -n "native-finite-window-realization-habitat|constructive-nonscalar-costello-qme-realization|theta-three-finite-window-acceptance-gate|app-qomega-centrality-homotopy-criterion" appendix-unreduced-bv-qme.tex main.tex
rg -n "theta_3_current_finite_row_subcomplex|theta3_ce_ancestor_supplied_exact_payload|theta3_complete_companion_faces_supplied_exact_payload" scripts/finite_window_graph_array.py
git diff --check -- reconstitution/nonscalar-costello-qme-construction-frontier-2026-04-30.md reconstitution/swarm-2026-04-30-agent-220-nonscalar-costello-qme-construction-frontier.md
grep -n '[[:blank:]]$' reconstitution/nonscalar-costello-qme-construction-frontier-2026-04-30.md reconstitution/swarm-2026-04-30-agent-220-nonscalar-costello-qme-construction-frontier.md
git status --short -- reconstitution/nonscalar-costello-qme-construction-frontier-2026-04-30.md reconstitution/swarm-2026-04-30-agent-220-nonscalar-costello-qme-construction-frontier.md
```
