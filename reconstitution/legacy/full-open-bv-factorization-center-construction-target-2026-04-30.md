# Full Open BV Factorization-Center Construction Target

Date: 2026-04-30.

Scope: formal-local mixed HT theory on
\[
  X=\mathbb R_t\times\mathbb R_s\times\widehat{\mathbb C^2}_{0},
  \qquad
  L=\mathbb R_t\times\{s=z_1=z_2=0\}.
\]
This file is a construction target and obstruction theorem for the full
open BV factorization center and the unreduced cotangent lift.  It does
not modify the manuscript.

## Stable Core

The proved local data are the following.

1. The closed Hamiltonian cotangent source is
\[
  \mathfrak h=\mathbb C[[z_1,z_2]]/\mathbb C\cdot 1,
  \qquad
  \mathfrak g=\mathfrak h\ltimes
    \mathfrak h^\vee_{\mathrm{cont}}[1].
\]

2. The continuous cotangent module is the reduced Matlis principal-part
module
\[
  \mathcal P
  =
  \operatorname{Ann}_{\mathrm{res}}(\mathbb C\cdot1)
  =
  \bigoplus_{\substack{a,b\ge 0\\a+b>0}}
  \mathbb C\,\rho_{a,b},
  \qquad
  \rho_{a,b}=z_1^{-a-1}z_2^{-b-1}\,dz_1dz_2.
\]
The residue pairing is
\[
  \langle \rho_{a,b},z_1^mz_2^n\rangle
  =
  \delta_{a,m}\delta_{b,n}.
\]
The Hamiltonian coadjoint action is
\[
  z_1^p z_2^q\cdot\rho_{a,b}
  =
  -(pb-qa+p-q)\rho_{a-p+1,b-q+1},
\]
with negative-index targets zero.

3. On an interval \(I\subset L\), the reduced current source is
\[
  \mathfrak g^{w,\mathrm{cur}}_{\hbar,I}
  =
  (\Omega^\bullet_c(I)\widehat\otimes\mathfrak h_{w,\hbar})
  \ltimes
  (\mathcal D'_c(I)\widehat\otimes
    \mathfrak h^{\vee,w}_{\hbar,\mathrm{cont}})[1].
\]
The current pairing is
\[
  \langle B\otimes\rho,\;a\otimes f\rangle
  =
  B(a)\operatorname{Res}(\rho f).
\]
The product \(aB\) is multiplication of a compactly supported
distribution by a smooth compactly supported function.  No product of
two distributions is formed in the reduced current model.

4. The reduced principal-part current target has strict brackets
\[
  \{B_f(a),B_g(b)\}_{\hbar}
  =
  B_{\{f,g\}_{\hbar}}(ab),
\]
\[
  \{B_f(a),\Theta_\rho(B)\}_{\hbar}
  =
  \Theta_{\operatorname{ad}^{\vee}_{f,\hbar}\rho}(aB),
  \qquad
  \{\Theta_\rho(B),\Theta_\sigma(C)\}_{\hbar}=0.
\]
This is a reduced current theorem.  It is not yet a morphism into the
full unreduced open BV factorization center.

5. The coefficient-current kernel exists:
\[
  \kappa^{\mathrm{coef}}_{\hbar,w,I}
  (u_{a(t)dt\otimes f})
  =
  \iota_I(B^w_f(a)),
  \qquad
  \kappa^{\mathrm{coef}}_{\hbar,w,I}(c_{B,\rho})
  =
  \iota_I(\Theta^w_\rho(B)).
\]
It is compatible with finite-window truncation and admissible weight
transport.  It gives zero product and \(P_0\)-defect homotopies only in
the freely adjoined coefficient-current target.

6. Polynomial one-\(\psi\) descendants do not realize the cotangent
module.  The averaged primitive descendant action is
\[
  F_{p,q}:\widetilde\Psi_{a,b}
  \longmapsto
  (pb-qa)\widetilde\Psi_{a+p-1,b+q-1},
\]
while the cotangent module carries the principal-part coadjoint action
above.  The two module structures are not isomorphic.  Thus a full
unreduced lift must retain the descendant module as separate data or
replace the target by a larger homotopy-coherent object.  It cannot
identify \(\Psi_{a,b}\) with \(\rho_{a,b}\) inside polynomial open BV
observables.

## Target Theorem

The desired theorem is the following construction.  Fix \(I,w,\hbar\)
and a finite-window tower \(M\).  Construct an enlarged unreduced brane
factorization target
\[
  A^{\mathrm{BV},+}_{\partial,\hbar,w}(I)
\]
containing:

- the genuine unreduced open BV observables
  \(\mathrm{Obs}^{\mathrm{BV}}_{\mathrm{open}}(I)\);
- the distributional principal-part current sector
  \(\mathcal D'_c(I)\widehat\otimes\mathcal P[1]\);
- a retained primitive one-\(\psi\) descendant module
  \(M_{\Psi,I}\), with its PBW action kept distinct from the
  principal-part coadjoint action.

Construct a filtered local-functional complex
\[
  \mathfrak Q^\bullet_{w,\partial,\hbar}(I)
  =
  \left(
  \mathcal O^{\mathrm{bd}}_{\mathrm{loc}}
  (\mathcal E_w|_I;A^{\mathrm{BV},+}_{\partial,\hbar,w}(I)),
  d_{\mathrm{QME}}=Q+\{I_0^w,-\}_{\hbar}
  \right),
\]
a filtered scalar-contact chain projection
\[
  \widehat\sigma_{\mathrm{sc}}\colon
  \mathfrak Q^\bullet_{w,\partial,\hbar}(I)
  \to
  C^\bullet_{\mathrm{Lie}}
  (\bar A;\mathbb C\gamma_{\mathbf 1})[1][[\hbar]],
\]
and a continuous bulk-to-defect kernel
\[
  \kappa_{\hbar,w,I}\colon
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  (\mathfrak g^{w,\mathrm{cur}}_{\hbar,I})
  \to
  \mathfrak Q^\bullet_{w,\partial,\hbar}(I).
\]
The generator values must be genuine boundary representatives
\[
  u_{a(t)dt\otimes f}\mapsto B_f^{\mathrm{BV}}(a),
  \qquad
  c_{B,\rho}\mapsto \Theta_\rho^{\mathrm{BV}}(B),
\]
whose reduced de Rham-current contraction is the proved current map
\[
  B_f^{\mathrm{BV}}(a)\mapsto B_f(a),
  \qquad
  \Theta_\rho^{\mathrm{BV}}(B)\mapsto\Theta_\rho(B).
\]

The theorem is complete exactly when the following data are supplied.

## Required Data

### Distributional Principal-Part Currents

The target must use
\[
  \mathcal P_I=\mathcal D'_c(I)\widehat\otimes\mathcal P.
\]
At the coefficient level the current action is
\[
  (a\otimes f)\cdot(B\otimes\rho)
  =
  (aB)\otimes(f\cdot\rho).
\]
At the graph level this is accepted only for regular densities or for a
proved wavefront-admissible class until the full \(\mathcal D'_c\)
brane-defect graph theorem is constructed.

### Boundary Representatives

The representatives \(B_f^{\mathrm{BV}}(a)\) and
\(\Theta_\rho^{\mathrm{BV}}(B)\) must be elements of the unreduced
local-functional target, not just symbols in the added reduced current
algebra.  They must satisfy:
\[
  d_{\mathrm{QME}}B_f^{\mathrm{BV}}(a)=0
  \quad\text{or a specified source differential image},
\]
\[
  d_{\mathrm{QME}}\Theta_\rho^{\mathrm{BV}}(B)=0
  \quad\text{or a specified source differential image},
\]
with exact finite-window and weight-transport compatibility.  Their
scalar, decomposable multi-trace, and descendant components must be
recorded before primitive projection.

### Descendant Module

The enlarged target must include a module
\[
  M_{\Psi,I}
  =
  \Omega^\bullet_c(I)\widehat\otimes
  \bigoplus_{a+b>0}\mathbb C\,[\widetilde\Psi_{a,b}]
\]
or a homotopy-coherent replacement.  It must not be identified with
\(\mathcal P_I\) as an \(\mathfrak h_\hbar\)-module.  The exact
construction target is a two-alphabet comparison:
\[
  M_{\Psi,I}
  \xleftarrow{\;N,i,H\;}
  \mathrm{Obs}^{\mathrm{BV}}_{\mathrm{open}}(I)
  \xrightarrow{\;\Theta\;}
  \mathcal P_I[1],
\]
where \(N,i,H\) give the allowed primitive or normal-ordering
contraction on the part where such a contraction exists, and \(\Theta\)
is a new distributional boundary representative.  A full cyclic
contraction killing all one-\(\psi\) classes is impossible because
\([\Psi_{a,b}]\ne0\).

### Product Centrality Homotopies

For each closed source generator \(x\) and arbitrary unreduced open
observable \(A\in A^{\mathrm{BV},+}_{\partial,\hbar,w}(I)\), construct
\[
  H^{\mathrm{prod},M}_{x,A}
  \in
  \mathfrak Q^{|x|+|A|-1}_{w,\partial,\hbar,M}(I)
\]
such that
\[
  d_M H^{\mathrm{prod},M}_{x,A}
  =
  \kappa_M(x)A
  -
  (-1)^{|x||A|}A\kappa_M(x).
\]
These homotopies must commute with interval inclusions, disjoint
factorization products, finite-window projections, and admissible
weight transports.

### \(P_0\)-Centrality Homotopies

The generator defects are
\[
  D^M_{f,g}(a,b)
  =
  \{B_f^{\mathrm{BV}}(a),B_g^{\mathrm{BV}}(b)\}_{\hbar}
  -
  B_{\{f,g\}_{\hbar}}^{\mathrm{BV}}(ab),
\]
\[
  D^M_{f,\rho}(a,B)
  =
  \{B_f^{\mathrm{BV}}(a),\Theta_\rho^{\mathrm{BV}}(B)\}_{\hbar}
  -
  \Theta_{\operatorname{ad}^{\vee}_{f,\hbar}\rho}^{\mathrm{BV}}(aB),
\]
\[
  D^M_{\rho,\sigma}(B,C)
  =
  \{\Theta_\rho^{\mathrm{BV}}(B),
    \Theta_\sigma^{\mathrm{BV}}(C)\}_{\hbar}.
\]
For every such pair \(x,y\), construct
\[
  H^M_{x,y}
  \in
  \ker\widehat\sigma_{\mathrm{sc},M}
  \cap
  \mathfrak Q^{|x|+|y|-1}_{w,\partial,\hbar,M}(I)
\]
with
\[
  \operatorname{Curv}_{\mathbf K,M}(\kappa_M)(x\wedge y)
  +
  d_MH^M_{x,y}=0.
\]
Equivalently, the three defects above must be \(d_M\)-exact after the
scalar gate has vanished.  The coefficient-current theorem supplies
\(H^M_{x,y}=0\) only in the freely adjoined current target, not in the
genuine unreduced open BV target.

### Coefficient Kernel And Brane-Defect Propagator

The coefficient-current kernel \(\kappa^{\mathrm{coef}}\) is already the
zero-edge part.  A full theorem must construct the positive-edge
Costello graph kernel:
\[
  K^M_\Gamma
  =
  W^{R,M}_{\Gamma,L,w}(B^\Gamma_\bullet)
\]
for every finite-window graph \(\Gamma\).  For distributional current
labels this requires:

- the finite-scale brane-defect propagator \(P^{w,M}_{\epsilon,L}\);
- H\"ormander wavefront transversality for products with pushed-forward
  current labels;
- local extension across all relevant small diagonals;
- counterterms \(C^M_{\Gamma,w}(\epsilon;B_\bullet)\);
- compatibility with interval extension by zero, \(\pi_{M,N}\), and
  \(R^M_{w,w'}\).

Without this theorem, the graph layer is restricted to regular compactly
supported densities or to explicitly wavefront-admissible tuples.

### QME Solution

In the completed convolution dg Lie algebra
\[
  \mathbf K^\bullet_{w,\partial,\hbar}(I)
  =
  \operatorname{Hom}_{\mathrm{cont}}
  \left(
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  (\mathfrak g^{w,\mathrm{cur}}_{\hbar,I}),
  \mathfrak Q^\bullet_{w,\partial,\hbar}(I)
  \right),
\]
with
\[
  d_{\mathbf K}T=d_{\mathrm{QME}}T-(-1)^{|T|}T\,d_{\mathrm{CE}},
\]
the full brane-defect QME equation is
\[
  \operatorname{Curv}_{\mathbf K}(\kappa+C)
  =
  d_{\mathbf K}(\kappa+C)
  +
  \frac12[\kappa+C,\kappa+C]_{\mathbf K}
  =
  0.
\]
At a finite window, the order-\(n\) residual is a finite row sum
\[
  R^{\mathrm{ns}}_{n,M}
  =
  \sum_{\alpha\in\mathsf A^{\mathrm{fw}}_{n,M}}
  R^{\mathrm{row}}_{\alpha,M}
  \in\ker\widehat\sigma_{\mathrm{sc},M}.
\]
A counterterm exists in a supplied primitive span exactly when
\[
  A^M c=-r^M
\]
is solvable.  The all-window solution also requires the corresponding
Roos primitive-compatibility class to vanish.

### Weiss/Ran Descent

A stalkwise formal-disk construction does not give a global
factorization-center morphism.  The stratified prefactorization object
on \((X,L)\) must satisfy Weiss/Ran descent.  For a cover
\(\mathcal U\) of a stratified open \(V\), the descent defect is
\[
  \delta_{\mathrm{Weiss}}(V,\mathcal U)
  =
  \mathcal F^{\mathrm{str}}(V)
  -
  \operatorname*{holim}_{U\in\mathcal U}
  \mathcal F^{\mathrm{str}}(U).
\]
The collar module, brane restriction maps, product maps, and centrality
homotopies must be part of the same stratified object.

## Obstruction Vector

The exact obstruction vector for the full open BV factorization center is
\[
  \operatorname{Ob}_{\mathrm{openBV}}
  =
  \left(
    \operatorname{ob}^{\mathrm{prod}}_{\mathrm{cent}},
    \operatorname{ob}^{P_0}_{\mathrm{cent}},
    \operatorname{ob}^{\mathrm{bd}}_{\mathrm{QME}},
    \delta_{\mathrm{Weiss}}
  \right).
\]

### Product Centrality Obstruction

For each finite window \(M\), source generator \(x\), and unreduced open
observable \(A\), define
\[
  R^{\mathrm{prod}}_{x,A,M}
  =
  \kappa_M(x)A
  -
  (-1)^{|x||A|}A\kappa_M(x).
\]
After scalar projection, the product-centrality obstruction is
\[
  \operatorname{ob}^{\mathrm{prod}}_{\mathrm{cent}}
  =
  \left(
  ([R^{\mathrm{prod}}_{x,A,M}])_M,\,
  \lambda^{\mathrm{prod}}_{x,A}
  \right),
\]
where
\[
  [R^{\mathrm{prod}}_{x,A,M}]
  \in
  H^{|x|+|A|}
  (\ker\widehat\sigma_{\mathrm{sc},M},d_M),
\]
and \(\lambda^{\mathrm{prod}}_{x,A}\) is the
\(\varprojlim^1H^{|x|+|A|-1}\) class measuring incompatibility of
chosen primitives under finite-window projection and weight transport.

### \(P_0\)-Centrality Obstruction

For source generators \(x,y\), the finite-window row is
\[
  R^{\mathrm{cent}}_{x,y,M}
  =
  \operatorname{Curv}_{\mathbf K,M}(\kappa_M)(x\wedge y).
\]
Equivalently it is the signed sum of target-differential rows,
CE-source rows, convolution-bracket rows, and counterterm rows.  Its
scalar gate is
\[
  S^{\mathrm{cent}}_{x,y,M}
  =
  \widehat\sigma_{\mathrm{sc},M}(R^{\mathrm{cent}}_{x,y,M}).
\]
Only if \(S^{\mathrm{cent}}_{x,y,M}=0\) does one obtain
\[
  \mathfrak o^{\mathrm{cent}}_{x,y,M}
  =
  [R^{\mathrm{cent}}_{x,y,M}]
  \in
  H^{|x|+|y|}
  (\ker\widehat\sigma_{\mathrm{sc},M},d_M).
\]
The obstruction is
\[
  \operatorname{ob}^{P_0}_{\mathrm{cent}}
  =
  \left(
    (\mathfrak o^{\mathrm{cent}}_{x,y,M})_M,\,
    \lambda^{P_0}_{x,y}
  \right),
\]
with \(\lambda^{P_0}_{x,y}\in\varprojlim^1
H^{|x|+|y|-1}\) the primitive-compatibility class for
\[
  R^{\mathrm{cent}}_{x,y,M}+d_MH^M_{x,y}=0.
\]

### Brane-Defect QME Obstruction

The QME obstruction is the package
\[
  \operatorname{ob}^{\mathrm{bd}}_{\mathrm{QME}}
  =
  \left(
    (o_{\sigma,w}^{(r)})_{r>0},
    \operatorname{ob}_{\mathcal D'_c\mathrm{-graph}},
    ([R^{\mathrm{ns}}_{n,M}])_M,
    \lambda_n,
    \operatorname{ob}_{\mathrm{scalar}}
  \right).
\]
Here:

- \(o_{\sigma,w}^{(r)}\) are the successive obstruction classes to
  constructing the filtered scalar-contact chain projection;
- \(\operatorname{ob}_{\mathcal D'_c\mathrm{-graph}}\) is the
  microlocal graph-extension and counterterm obstruction for arbitrary
  compactly supported distributional labels;
- \(([R^{\mathrm{ns}}_{n,M}])_M,\lambda_n)\) is the finite-window
  non-scalar counterterm obstruction at the first unsolved order;
- \(\operatorname{ob}_{\mathrm{scalar}}\) is the scalar branch
  obstruction.  In the ordinary scalar-reduced \(\mathfrak{gl}_N\)
  branch it contains the nonzero class \(\hbar N[\bar c]\) unless a
  central-character replacement, balanced supertrace branch, or typed
  closed-exchange class with leading value \(-\hbar N[\bar c]\) is
  constructed.

### Weiss/Ran Obstruction

The descent obstruction is
\[
  \delta_{\mathrm{Weiss}}
  \in
  \operatorname{Tot} C^\bullet_{\mathrm{WR}}
  \left(
  \operatorname{Ran}(L);
  \underline{\operatorname{RHom}}
  \left(
  \mathrm{Obs}^{\mathrm{cl}}_{\mathrm{closed},H},
  Z^{P_0}_{\mathrm{fact}}
  (\mathrm{Obs}^{\mathrm{BV},+}_{\mathrm{open}})
  \right)\right).
\]
Its first components are the local Hamiltonian period class, the
source-comparison defect, the cotangent boundary-realization defect, the
centrality-homotopy transition defects, and the stratified
prefactorization descent defect.

## Current Verdict

The positive full open BV factorization-center theorem is not complete
from the current data.  What is proved is stronger than a loose
conditional statement: the manuscript supplies the reduced current
theorem, the Matlis principal-part cotangent module, the coefficient
kernel, the polynomial descendant no-go theorem, the finite-window
QME/counterterm criterion, and the centrality row criterion.  The exact
remaining theorem targets are:

1. Distributional brane-defect graph theorem for \(\mathcal D'_c(I)\)
labels, including wavefront transversality, diagonal extension, and
compatible counterterms.
2. Boundary representative theorem constructing
\(B_f^{\mathrm{BV}}\) and \(\Theta_\rho^{\mathrm{BV}}\) in the genuine
unreduced local-functional target.
3. Descendant-retention theorem constructing a two-alphabet
homotopy-coherent target rather than identifying \(\Psi_{a,b}\) with
\(\rho_{a,b}\).
4. Product centrality obstruction theorem proving that
\(\operatorname{ob}^{\mathrm{prod}}_{\mathrm{cent}}=0\), or naming the
first nonzero class.
5. \(P_0\)-centrality obstruction theorem proving that
\(\operatorname{ob}^{P_0}_{\mathrm{cent}}=0\), or naming the first
nonzero finite-window row and its cokernel functional.
6. Brane-defect QME theorem solving
\(\operatorname{Curv}_{\mathbf K}(\kappa+C)=0\), or naming the first
nonzero scalar, microlocal, non-scalar \(H^1\), or Roos obstruction.
7. Stratified Weiss/Ran descent theorem proving
\(\delta_{\mathrm{Weiss}}=0\), or naming the first failed cover,
collar-module map, or transition homotopy.

Only after all four components of
\(\operatorname{Ob}_{\mathrm{openBV}}\) vanish does the construction give
a morphism
\[
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  (\mathfrak g^{w,\mathrm{cur}}_{\hbar,I})
  \longrightarrow
  Z^{P_0}_{\mathrm{fact}}
  (A^{\mathrm{BV},+}_{\partial,\hbar,w})(I)
\]
compatible with products, \(P_0\)-brackets, QME, principal-part
cotangent currents, descendants, finite windows, weights, and
Weiss/Ran descent.

## Local Anchors

- `main.tex`: Problem `prob:formal-factorization-center`,
  Remark `rmk:unreduced-lift-status`, Problem
  `prob:quantum-p0-operation-realization`.
- `appendix-matlis-principal-parts.tex`: reduced Matlis module,
  residue pairing, coadjoint action, polynomial descendant obstruction.
- `appendix-factorization-current-conventions.tex`: current source,
  reduced current interface, coefficient-current kernel, curved kernel
  centrality criterion.
- `appendix-unreduced-bv-qme.tex`: polynomial centrality no-go, scalar
  QME obstruction, finite-window graph/QME criterion, marked-row
  centrality test.
- `tate-T5-chain-level-primitive.tex`: primitive indecomposable shadow,
  one-\(\psi\) label shadow, and \(\hbar\)-adic obstruction for the
  one-\(\psi\) label map.
- `open-obligations.tex`: unreduced factorization-current lift,
  stratified brane prefactorization, centrality rows, and
  Weiss/Ran obstruction vector.
