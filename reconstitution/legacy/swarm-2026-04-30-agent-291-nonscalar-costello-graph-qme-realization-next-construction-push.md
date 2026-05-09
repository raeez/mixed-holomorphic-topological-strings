# Agent 291 Non-scalar Costello Graph/QME Realization Push

Status: report-only.  No TeX, script, figure, source, or build file was
edited.

Owned report:
`reconstitution/nonscalar-costello-graph-qme-realization-next-construction-push-2026-04-30.md`.

## Result

The full non-scalar Costello graph/QME realization is not closed.  The
strongest true theorem surface is the native finite-window
local-functional habitat plus the matrix obstruction criterion.  The
script-backed minimal/binary rows are real, but they do not supply the
marked Costello row table, scalar projection, bulk-to-defect kernel, row
bases, counterterm columns, or transport matrices needed for the full
QME equation.

The executable floor is:

```text
minimal_full_equivariant_order_2_zero True () () () () 0 ()
theta_3_current_finite_row_subcomplex False ((),) (('E_theta_3', '1'),) (('E_theta_3', '-1'),) (('E_theta_3', '1'),) 1 ()
```

The \(\theta_3\) row remains the first supplied nonzero scalar-zero
obstruction in the current row package:
\[
  A^M_{\theta_3}=[\,]_{1\times0},\qquad r^M=(1),\qquad
  \ell_{\theta_3}(\mathsf E_{\theta_3,M})=1.
\]

## Constructed Habitat

The next theorem-grade habitat is the finite-window complex
\[
  \mathfrak Q^\bullet_{\mathcal G,M}(I)
  =
  \left(
  \mathcal O^{\mathrm{bd}}_{\mathrm{loc},\mathcal G,M}
  (\mathcal E_w^M|_I;A^{\mathrm{pp},w,M}_{\partial,\hbar}(I)),
  d_M=Q+\{I^w_{0,M},-\}_{\hbar,M}
  \right)
\]
with Hom kernel complex
\[
  \mathbf K^\bullet_{\mathcal G,M}(I)
  =
  \operatorname{Hom}_{\mathrm{cont}}
  (C^\bullet_{\mathrm{lab}}(\mathcal G_M),
   \mathfrak Q^\bullet_{\mathcal G,M}(I)).
\]
This is usable only after a codimension-two closed marked graph list,
chain scalar projection \(\widehat\sigma_{\mathrm{sc},M}\), continuous
bulk-to-defect kernel, row bases, primitive columns, and transports are
supplied.

## Exact Next Equation

The direct top-window repair is the column
\[
  A^M_{\theta_3,C}=(-1),\qquad r^M=(1),\qquad c=1,
\]
where \(C\) is either a marked CE ancestor or a Costello local counterterm
with \(d_MC=-\mathsf E_{\theta_3,M}\), zero scalar projection, \(TA=AP\),
and zero Roos class.

For the companion/lower-window route, the current matrix is
\[
  A_D^2=(-2,2,1)^T,\qquad r_2=(2,-2,0)^T,
\]
in the basis
\((E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20})\), and it has no
solution.  The next matrix that can close the row is
\[
  A^2_{D,B}
  =
  \begin{pmatrix}
  -2&0\\
  2&0\\
  1&-1
  \end{pmatrix},
  \qquad
  A^2_{D,B}
  \begin{pmatrix}1\\1\end{pmatrix}
  =
  -(2,-2,0)^T,
\]
where the new column is a scalar-zero local counterterm
\[
  B^2_{02,20},\qquad
  d_{\mathrm{ns},2}B^2_{02,20}=-\mathfrak b^2_{02,20}.
\]

## Missing Data

The missing construction data are the marked Costello incidence/weight
table, Hom-valued Bianchi closure, scalar projection on the graph habitat,
regular-density or wavefront-admissible current graph contractions,
projection matrices \(u,v,q\), primitive transports \(P\), and the direct
\(\theta_3\) or lower Bianchi-killing counterterm column.

The eight-face candidate remains rejected: its residual vector is
\[
  (2,-2,3,2,-1,1,-2,-3),
\]
its coefficient sum is \(0\), but diagonal transport to \(N=2\) leaves
\[
  2E^2_{\nu_{02}}-2E^2_{\nu_{20}}.
\]

## Checks

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 - <<'PY'
# selected finite_window_graph_array.py primitive, payload, eight-face,
# and missing-row checks
PY
```

No build was run.
