# Agent 093 Bulk-Defect Kernel Attack-Heal

Status: obstruction ledger converged; non-scalar Costello graph/QME theorem blocked.

## Claim Attacked

The attacked claim was that the reduced factorization-current theorem,
the weighted quantum coefficient surface, and the scalar QME cancellation
already supply the unreduced non-scalar Costello graph/QME realization.

They do not.  The reduced theorem is strict only after scalar reduction,
de Rham-current contraction, and passage to the added principal-part
current target.  The Costello theorem still needs an unreduced
local-functional kernel and QME solution.

## Failure And Surviving Statement

The strongest true statement is a necessary-and-sufficient datum,
conditional on constructing the Costello finite-scale BV package in the
chosen weighted coefficient category.

The source current complex must be
\[
  \mathfrak g^{w,\mathrm{cur}}_{\hbar,I}
  =
  (\Omega^\bullet_c(I)\widehat\otimes\mathfrak h_{w,\hbar})
  \ltimes
  (\mathcal D'_c(I)\widehat\otimes
    \mathfrak h^{\vee,w}_{\hbar,\mathrm{cont}})[1],
\]
or the central-character replacement before scalar reduction.

The target must be the mixed brane-defect local-functional complex
\[
  \mathfrak Q^\bullet_{w,\partial,\hbar}(I)=
  \left(
  \mathcal O_{\mathrm{loc}}^{\mathrm{bd}}
  (\mathcal E_w|_I;A^{\mathrm{pp},w}_{\partial,\hbar}(I)),
  Q+\{I_0^w,-\}_\hbar
  \right),
\]
with the finite-scale BV Laplacian and propagator present when the
scale-\(L\) QME is not absorbed into the differential.

The missing kernel is a continuous curved map
\[
  \kappa_{\hbar,w,I}\colon
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  (\mathfrak g^{w,\mathrm{cur}}_{\hbar,I})
  \to
  \mathfrak Q^\bullet_{w,\partial,\hbar}(I)
\]
with generator values
\[
  u_{a(t)dt\otimes f}\mapsto B_f^{\mathrm{BV}}(a),
  \qquad
  c_{B,\rho}\mapsto\Theta_\rho^{\mathrm{BV}}(B).
\]

The obstruction maps are:
\[
  \widehat\sigma_{\mathrm{sc}}
  \left(d_{\mathrm{QME}}\kappa_{\hbar,w,I}
  +\frac12[\kappa_{\hbar,w,I},\kappa_{\hbar,w,I}]_\hbar\right)=0,
\]
\[
  [d_{\mathrm{QME}}\kappa_{\hbar,w,I}
  +\tfrac12[\kappa_{\hbar,w,I},\kappa_{\hbar,w,I}]_\hbar]
  \in H^1(\ker\widehat\sigma_{\mathrm{sc}},d_{\mathrm{QME}}),
\]
and the generator-level bracket defects
\[
  D_{f,g}=\{B_f^{\mathrm{BV}}(a),B_g^{\mathrm{BV}}(b)\}_\hbar
  -B_{\{f,g\}_\hbar}^{\mathrm{BV}}(ab),
\]
\[
  D_{f,\rho}=
  \{B_f^{\mathrm{BV}}(a),\Theta_\rho^{\mathrm{BV}}(B)\}_\hbar
  -\Theta_{\operatorname{ad}^{\vee}_{f,\hbar}\rho}^{\mathrm{BV}}(aB),
\]
\[
  D_{\rho,\sigma}=
  \{\Theta_\rho^{\mathrm{BV}}(B),\Theta_\sigma^{\mathrm{BV}}(C)\}_\hbar.
\]
They must be killed by \(d_{\mathrm{QME}}\)-homotopies compatible with
interval inclusions, disjoint factorization products, and finite-window
regulator maps.

## Heal Inscribed

Edited `appendix-factorization-current-conventions.tex` only.

- Added `def:app-unreduced-nonscalar-current-lift-datum`.
- Added `prop:app-nonscalar-current-lift-obstructions`.

This pins the source complex, target defect algebra, bulk-to-defect
kernel, scalar projection, centrality homotopies, and QME obstruction
class without asserting the missing graph theorem.

## Local Anchors

- `appendix-factorization-current-conventions.tex:24`: reduced interval
  Hamiltonian current source.
- `appendix-factorization-current-conventions.tex:61`: distributional
  Matlis current dual.
- `appendix-factorization-current-conventions.tex:190`: strict reduced
  algebraic current interface.
- `appendix-factorization-current-conventions.tex:374`: new unreduced
  non-scalar current lift datum.
- `appendix-factorization-current-conventions.tex:441`: new obstruction
  maps.
- `appendix-unreduced-bv-qme.tex:92`: polynomial unreduced centrality
  no-go.
- `appendix-unreduced-bv-qme.tex:375`: scalar contact QME obstruction.
- `appendix-unreduced-bv-qme.tex:470`: central-character source
  replacement.
- `appendix-unreduced-bv-qme.tex:553`: balanced supertrace scalar
  cancellation.
- `main.tex:5627`: reduced support-local principal-part current datum.
- `main.tex:5876`: unreduced lift obstruction datum.
- `main.tex:6783`: Costello Hamiltonian specialization datum.
- `main.tex:7177`: componentwise quantum coefficient surface.
- `main.tex:7334`: non-scalar quantum \(P_0\)-operation obstruction complex.
- `tate-T1-weighted-completion.tex:439`: weighted coefficient Casimir and
  propagator package.
- `tate-T5-chain-level-primitive.tex:1065`: reduced Moyal principal-part
  target.

## Source Anchors

- `references/primary-sources/costello-cg-source-anchors-2026-04-28.md:23`:
  exact Costello theorem-number caution; use heat-kernel/RG/locality
  package as vocabulary unless separately anchored.
- `references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt:1896`:
  scale-\(L\) open-closed QME definition.
- `references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt:1937`:
  RG flow compatibility with QME.
- `references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt:2338`:
  obstruction-deformation complex by local functionals.
- `references/primary-sources/costello-li-quantum-bcov-1201.4501.txt:917`:
  QME/RG/locality package.
- `references/primary-sources/costello-li-quantum-bcov-1201.4501.txt:2493`:
  \(H^1\) of the local-functional complex contains obstructions.

## Commands

Read and search commands included `sed -n`, `nl -ba`, `rg -n`, and
`git status --short` over the manuscript controls, target appendix,
unreduced QME appendix, theorem lanes, open obligations, weighted Tate
completion, quantum descendant target, Costello source ledgers, and
primary-source mirrors.

Verification commands are recorded after the patch in the session log:
`git diff --check` and targeted status/diff checks on the owned paths.
No full `make pdf` was run because it writes `out/main.pdf`, which is
outside this agent's ownership while other agents are editing.

## Residuals

The theorem remains open until a later agent constructs:

1. finite-scale Costello BV propagator and BV Laplacian for the weighted
   bulk-defect current complex;
2. wavefront and locality rules for \(\mathcal D'_c\)-valued
   principal-part current coefficients, or a restriction to regular
   densities;
3. finite-window counterterms \(C_{\Gamma,w}^{w_0}(\epsilon)\) satisfying
   projection and weight-transport compatibility;
4. product and \(P_0\)-bracket centrality homotopies for
   \(D_{f,g}\), \(D_{f,\rho}\), and \(D_{\rho,\sigma}\);
5. vanishing of the residual class in
   \(H^1(\ker\widehat\sigma_{\mathrm{sc}},d_{\mathrm{QME}})\).
