# Non-scalar Costello Graph/QME Realization Next Construction Push

Date: 2026-04-30.
Status: report-only construction push.  No TeX, script, figure, source, or
build file was edited.

## Claim Attacked

The attacked claim is that the script-backed minimal/binary finite rows
already realize the full non-scalar Costello graph/QME theorem.

That claim is false.  The script certifies finite row algebra after the
row table, scalar projection, row bases, primitive columns, and transport
matrices are supplied.  It does not construct the Costello local-functional
graph package itself.

## Stable Floor

The stable script-backed floor is:

- In the minimal full-equivariant branch, the order-two residual and
  primitive bases are empty.  The fixed-window primitive exists, the
  counterterm is zero, and the Roos class is zero.
- The retained scalar-zero row \(\alpha_{11}\) and all bracket rows
  containing the zero scalar-contact rows vanish as local functionals.
- The first supplied nonzero row is
  \[
    \theta_3=\mathrm{CE}(\Theta_3,\nu_3),\qquad
    \mathsf E_{\theta_3,M}=-K^M_{\Theta_3}(\zeta_{M,\nu_3}),
    \qquad \widehat\sigma_{\mathrm{sc},M}(\mathsf E_{\theta_3,M})=0 .
  \]
  In the supplied one-row complex
  \[
    \mathcal Q^0_{\theta_3,M}=0,\qquad
    \mathcal Q^1_{\theta_3,M}=\C\mathsf E_{\theta_3,M},\qquad d_M=0,
  \]
  the primitive matrix is \(1\times0\), \(r^M=(1)\), and
  \(\ell_{\theta_3}(\mathsf E_{\theta_3,M})=1\) detects the nonzero
  fixed-window \(H^1\)-class.

Executable check:

```text
minimal_full_equivariant_order_2_zero True () () () () 0 ()
theta_3_current_finite_row_subcomplex False ((),) (('E_theta_3', '1'),) (('E_theta_3', '-1'),) (('E_theta_3', '1'),) 1 ()
```

The payload validator accepts a CE ancestor or local counterterm only when
the payload has differential coefficient \(-1\), zero scalar projection,
the matrix identity \(TA=AP\), and zero Roos class.  It rejects the current
data because the degree-zero column is absent.

## Theorem-grade Habitat Constructed

The next theorem-grade habitat is the native finite-window realization
datum
\[
  \mathfrak Q^\bullet_{\mathcal G,M}(I)
  =
  \left(
  \mathcal O^{\mathrm{bd}}_{\mathrm{loc},\mathcal G,M}
  (\mathcal E_w^M|_I;A^{\mathrm{pp},w,M}_{\partial,\hbar}(I)),
  d_M=Q+\{I^w_{0,M},-\}_{\hbar,M}
  \right),
\]
completed in the \(\hbar\)-adic, scalar-contact, and finite-window
filtrations, together with
\[
  \mathbf K^\bullet_{\mathcal G,M}(I)
  =
  \operatorname{Hom}_{\mathrm{cont}}
  (C^\bullet_{\mathrm{lab}}(\mathcal G_M),
   \mathfrak Q^\bullet_{\mathcal G,M}(I)).
\]
Its differential and curvature are
\[
  d_{\mathbf K,M}T=d_MT-(-1)^{|T|}Td_{\mathrm{CE}},
  \qquad
  \operatorname{Curv}_{\mathbf K,M}(\kappa)
  =
  d_{\mathbf K,M}\kappa+\frac12[\kappa,\kappa]_{\mathbf K,M}.
\]

This habitat is theorem-grade only after the finite marked graph list
\(\mathcal G^{\mathrm{mk}}_M\) is codimension-two closed and the scalar
projection is an actual filtered chain map
\[
  \widehat\sigma_{\mathrm{sc},M}\colon
  \mathfrak Q^\bullet_{\mathcal G,M}(I)
  \to C^\bullet_{\mathrm{Lie}}(\bar A;\C\gamma_{\mathbf 1})[1][[\hbar]].
\]
The associated-graded scalar symbol is not enough.  If
\(\widehat\sigma_{\mathrm{sc},M}\) is not a chain map,
\(\ker\widehat\sigma_{\mathrm{sc},M}\) is not a non-scalar QME complex.

The row types in this habitat are exactly
\[
  R^{\mathrm{row}}_{d\Gamma,M}
  =
  \varepsilon_\Gamma d_MK^M_\Gamma,
\]
\[
  R^{\mathrm{row}}_{\mathrm{CE}(\Gamma,\nu),M}
  =
  -\varepsilon^{\mathrm{CE}}_{\Gamma,\nu}
  K^M_\Gamma(\zeta_{M,\nu}),
\]
\[
  R^{\mathrm{row}}_{b(\Gamma_1,\Gamma_2),M}
  =
  \frac12\varepsilon_{\Gamma_1,\Gamma_2}
  \{K^M_{\Gamma_1},K^M_{\Gamma_2}\}_{\hbar,M},
\]
plus the homogeneous lower-counterterm terms
\[
  [\hbar^n]\left(d_MC_{<n,M}
  +\frac12\{C_{<n,M},C_{<n,M}\}_{\hbar,M}\right).
\]
These formulas construct the next row habitat.  They do not fill the row
values.

## Attack: Gap To Full Costello Realization

The gap has five independent components.

First, the finite graph list is not present for general rows.  A genuine
row requires output graph, coefficient, orientation/Koszul sign, marker
transport, source face, and codimension-two closure.  Without this,
\(d_{\mathrm{mk}}^2=0\) and the Hom Bianchi identity are not constructed.

Second, scalar projection is a chain-level datum.  The balanced
supertrace zero projection is proved on balanced scalar-contact habitats,
not on arbitrary graph/counterterm habitats.

Third, the bulk-to-defect kernel is not the reduced current bracket.  It is
a continuous Hom-valued kernel whose zero-edge values reduce to
\(B_f(a)\) and \(\Theta_\rho(B)\), and whose positive-edge values are
renormalized graph weights
\[
  K^M_\Gamma=W^{R,M}_{\Gamma,L,w}(B^\Gamma_\bullet).
\]

Fourth, current labels are only safe in the regular-density branch or in a
named wavefront-admissible subspace.  The Costello source fixtures do not
provide a theorem for arbitrary \(B\in\mathcal D'_c(I)\).

Fifth, counterterm recursion is a matrix problem, not a slogan.  After the
scalar gate
\[
  \mathfrak s_{n,M}
  =
  \sum_{\alpha\in\mathsf A^{\mathrm{fw}}_{n,M}}
  \widehat\sigma_{\mathrm{sc},M}(R^{\mathrm{row}}_{\alpha,M})
  =0
\]
has passed, the residual
\[
  R^{\mathrm{ns}}_{n,M}=\sum_i r_i^M\rho_i^M
\]
is killed in the supplied finite row span exactly when
\[
  d_M\eta^M_j=\sum_iA^M_{ij}\rho_i^M,\qquad
  A^Mc=-r^M
\]
is solvable, with
\[
  T^{M,N}r^M=r^N,\qquad T^{M,N}A^M=A^NP^{M,N},
  \qquad [P^{M,N}c_M-c_N]=0.
\]

## Heal Attempt

The direct \(\theta_3\) heal would add one scalar-zero degree-zero column:
\[
  A^M_{\theta_3,C}=(-1),\qquad
  d_MC_{\theta_3,M}=-\mathsf E_{\theta_3,M}.
\]
Then \(A^Mc=-r^M\) is solved by \(c=1\).  This is theorem-grade only if
one of the following is actually constructed:

1. A marked CE ancestor
   \[
     \eta^{\mathrm{mark}}_{\theta_3,M},\qquad
     d_{\mathrm{CE}}\eta^{\mathrm{mark}}_{\theta_3,M}=\zeta_{M,\nu_3},
   \]
   outside the ordinary pure two-\(u\) source algebra, with
   \(d_MK^M_{\Theta_3}(\eta^{\mathrm{mark}}_{\theta_3,M})
   =-\mathsf E_{\theta_3,M}\), scalar-zero value, codimension-two closure,
   Hom-valued Bianchi cancellation, and transport.
2. A Costello local counterterm
   \(C^{\mathrm{ct}}_{\theta_3,M}\in\mathcal Q^0_{w,M}(I)\) with
   \(d_MC^{\mathrm{ct}}_{\theta_3,M}=-\mathsf E_{\theta_3,M}\), scalar-zero
   value, locality or wavefront admissibility, and zero Roos class.
3. A complete marked companion-face table whose signed residual is zero in
   one marked Costello row basis and whose \(v\)-transport keeps it zero in
   every lower window.

The ordinary pure two-\(u\) CE ancestor route is blocked.  The covector
\[
  q_{2u}
  =
  e^*_{((H_{0,1},H_{2,0}),c_{\rho_{2,1}})}
  -\frac12e^*_{((H_{0,1},H_{0,1}),c_{\rho_{0,2}})}
\]
satisfies \(q_{2u}d_{\mathrm{CE}}=0\) and
\(q_{2u}(\zeta_{M,\nu_3})=1\).  Enlarging only the polynomial degree
cutoff cannot produce the ancestor.

The eight-face source-algebraic companion candidate is also not a theorem.
It has vector
\[
  r_8=(2,-2,3,2,-1,1,-2,-3)^T
\]
on
\[
  E_{\nu_{02}},E_{\nu_{20}},E_{\nu_{03}},
  E_{\nu_{12}^{(1)}},E_{\nu_{12}^{(2)}},
  E_{\theta_3},E_{\nu_{21}^{(2)}},E_{\nu_{30}},
\]
with coefficient sum zero, but it is not the zero row vector.  Diagonal
transport to \(N=2\) leaves
\[
  2E^2_{\nu_{02}}-2E^2_{\nu_{20}}.
\]
The missing marked table consists of labelled \(d_{\mathrm{CE}}\zeta_M\),
Costello orientation/Koszul signs, weights
\(K^M_{\Theta_3}(\zeta_{M,\nu})\) in one row basis, marker transports,
basis-reduced \(v^{M,N}\), and codimension-two incidence.

## Exact Next Matrix Equation

Full realization still fails.  The next finite-window matrix equation is
the two-level \(\theta_3\) repair system.

At the top window \(M\ge3\), construct a genuine column
\[
  A^M_{\theta_3,C}=(-1),\qquad r^M=(1),
\]
with \(C\) one of the marked ancestor or local counterterm primitives
above, and prove
\[
  T^{M,N}A^M=A^NP^{M,N},\qquad [P^{M,N}c_M-c_N]=0.
\]

For the companion/lower-window route, the transported \(N=2\) residual is
\[
  r_2=(2,-2,0)^T
\]
in the Bianchi-exposed basis
\[
  (E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20}).
\]
The source primitive
\[
  \zeta^0_2=u_{a,H_{1,0}}u_{b,H_{0,1}},\qquad
  D^2_{02,20}=K^2_{\Theta_3}(\zeta^0_2)
\]
satisfies
\[
  d_{\mathrm{CE}}\zeta^0_2
  =
  2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}},
\]
but in the local-functional complex
\[
  d_{\mathrm{ns},2}D^2_{02,20}
  =
  -2E^2_{\nu_{02}}+2E^2_{\nu_{20}}
  +\mathfrak b^2_{02,20}.
\]
With only \(D^2_{02,20}\), the matrix
\[
  A_D^2=(-2,2,1)^T,\qquad r_2=(2,-2,0)^T
\]
has no solution.  The cokernel
\[
  \widetilde\lambda_{02,\mathfrak b}
  =
  \frac12(E^2_{\nu_{02}})^*
  +(\mathfrak b^2_{02,20})^*
\]
kills \(A_D^2\) and evaluates to \(1\) on \(r_2\).

The first matrix that can close this lower row is therefore
\[
  A^2_{D,B}
  =
  \begin{pmatrix}
  -2&0\\
  2&0\\
  1&-1
  \end{pmatrix},
  \qquad
  r_2=
  \begin{pmatrix}
  2\\-2\\0
  \end{pmatrix},
  \qquad
  A^2_{D,B}
  \begin{pmatrix}1\\1\end{pmatrix}
  =
  -r_2.
\]
The second column is a new scalar-zero local counterterm
\[
  B^2_{02,20},\qquad
  d_{\mathrm{ns},2}B^2_{02,20}=-\mathfrak b^2_{02,20}.
\]
Constructing this column requires locality or wavefront admissibility,
zero scalar projection, and transport
\[
  d_{\mathrm{ns},N}(\pi_{M,N}D^M-D^N)
  =
  \pi_{M,N}\mathfrak b^M_{\mathrm{cand}}
  -\mathfrak b^N_{\mathrm{cand}}
\]
to vanish or be killed by a supplied boundary.

## Source And Kernel Data Still Missing

The exact construction target is:

1. a codimension-two closed marked Costello table for the relevant finite
   row package;
2. an actual chain scalar projection \(\widehat\sigma_{\mathrm{sc},M}\) on
   that graph/counterterm habitat;
3. regular-density or named wavefront-admissible graph contractions for the
   cotangent current labels;
4. renormalized weights \(K^M_\Gamma\), source-face signs
   \(\varepsilon^{\mathrm{CE}}_{\Gamma,\nu}\), and row bases for all
   source-face and bracket rows used;
5. projection matrices \(u^{M,N}\), \(v^{M,N}\), \(q^{M,N}\), and primitive
   transports \(P^{M,N}\) computed from row coordinates, not chosen to kill
   the residual;
6. the direct \(\theta_3\) column \(A^M_{\theta_3,C}=-1\), or the lower
   Bianchi-killing column \(B^2_{02,20}\), with scalar-zero value,
   locality, and Roos compatibility.

Until these data exist, the correct theorem is the finite-window
obstruction theorem above.  The full Costello graph/QME realization is not
proved.

## Anchors Checked

- `main.tex:8142-8376`: non-scalar \(P_0\)-operation obstruction complex.
- `main.tex:8378-8604`: \(\theta_3\) finite-window acceptance gate and
  lower Bianchi obstruction.
- `theorem-lanes.tex:3208-3421`: local graph/QME branch catalogue.
- `open-obligations.tex:824-874`: Costello graph/QME brane-defect package
  ledger row.
- `claim-strength-ledger.tex:824-874`: claim-strength row for the
  Costello graph/QME package.
- `local-dictionary.tex:829-1050`: non-scalar Costello/QME dictionary.
- `appendix-unreduced-bv-qme.tex:2142-2385`: native finite-window
  realization habitat and constructive criterion.
- `appendix-factorization-current-conventions.tex:934-1025`: convolution
  habitat and bulk-to-defect kernel.
- `scripts/finite_window_graph_array.py:721-979`: genuine row and
  \(u,v,q\) projection rules.
- `scripts/finite_window_graph_array.py:1210-1314`: \(\theta_3\) payload
  acceptance gate.
- `scripts/finite_window_graph_array.py:1448-1562`: eight-face rejection
  and missing marked table.

## Verification

Commands run:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 - <<'PY'
# imported scripts/finite_window_graph_array.py and printed selected
# primitive, payload, eight-face, and missing-row records
PY
rg -n "non[- ]scalar|theta_3|Costello graph|finite-window|bulk-to-defect|counterterm" main.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex reconstitution
```

No PDF build was run because this was report-only and no TeX was edited.
