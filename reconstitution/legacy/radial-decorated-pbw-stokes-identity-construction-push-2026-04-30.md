# Radial decorated PBW Stokes identity construction push

Date: 2026-04-30.

## Status

The all-bidegree decorated PBW Stokes identity was not proved in this
pass.  The finite square-cell construction did lift every decided residual:
all bidegrees of total degree at most \(13\), and the total-degree \(14\)
cases
\[
  (3,11),(11,3),(4,10),(10,4),(5,9),(9,5).
\]
No square-cell cokernel row was found.

The first bidegree not lifted by this pass is \((6,8)\), because exact
free-diagram enumeration exceeded the \(180\)-second per-case alarm.  This
is a computational frontier, not an obstruction row.  The first genuine
mathematical obstruction bidegree remains unknown.

No TeX or script file was edited.

## Anchors

- `appendix-radial-parts-moyal.tex:559-645`: free trace-diagram obstruction and the first \(K_{4,4}\) correction.
- `appendix-radial-parts-moyal.tex:669-739`: free indexed PBW normal-ordering formula.
- `appendix-radial-parts-moyal.tex:820-963`: decorated Hodge obstruction theorem.
- `appendix-radial-parts-moyal.tex:965-1111`: dual-potential obstruction and the stated \(D^\square_{a,b}=C^+_{a,b}\partial_2\) theorem target.
- `appendix-radial-parts-moyal.tex:1113-1259`: proved edge PBW telescoping strip.
- `open-obligations.tex:1284-1370`: radial/Weyl finite certificates and the uniform homotopy gate.
- `scripts/quantum_shear_trace_diagram_normal_form.py:276-360`: PBW matching enumeration and the column \(C^+_{a,b}(W)\).
- `scripts/quantum_shear_trace_diagram_normal_form.py:745-801`: kernel-correction solve used as the baseline.

## Square-Cell Complex Used

For fixed \(a,b\), a based vertex is a word with \(a\) letters \(X\) and
\(b\) letters \(Y\).  A square cell is a pair of commuting adjacent
swaps in a word
\[
  uXYvXYw.
\]
With orientation
\[
  uXYvXYw\to uYXvXYw\to uYXvYXw\to uXYvYXw\to uXYvXYw,
\]
each side is cut immediately after the swapped pair, giving an edge word
\(W\in\mathsf W_{a,b}\).  The resulting boundary lies in
\(\ker\partial\).  The decorated square column is
\[
  D^\square_{a,b}(\sigma)
  =
  C^+_{a,b}(\partial_2\sigma)
  =
  \sum_W(\partial_2\sigma)_W\,
  \mathcal N_{\mathrm{free}}\operatorname{Tr}(WM).
\]
The inline exact scripts used the based square cells as an overcomplete
spanning set for the cyclic quotient.  Consistency of these systems proves
membership in the square-cell image for the tested bidegrees.

## Decided Window

The square-cell solve used the lexicographic classical lift produced by
`solve_classical_case`, formed
\[
  R^{\mathrm{free}}_{a,b}
  =
  E^+_{a,b}-C^+_{a,b}(c^{\mathrm{cl}}_{a,b}),
\]
and solved \(D^\square_{a,b}H=R^{\mathrm{free}}_{a,b}\) over \(\mathbb Q\).

Selected nonzero residuals:

| Bidegree | Residual terms | Square cells | Rank | Square support | Corrected residual |
|---|---:|---:|---:|---:|---:|
| \((4,4)\) | 4 | 29 | 1 | 1 | 0 |
| \((4,5),(5,4)\) | 4 | 60 | 1 | 1 | 0 |
| \((4,6),(6,4)\) | 7 | 103 | 2 | 2 | 0 |
| \((5,5)\) | 22 | 140 | 4 | 4 | 0 |
| \((4,8),(8,4)\) | 10 | 249 | 3 | 3 | 0 |
| \((5,7)\) | 50 | 504 | 9 | 9 | 0 |
| \((7,5)\) | 62 | 504 | 9 | 9 | 0 |
| \((6,6)\) | 96 | 621 | 14 | 14 | 0 |
| \((4,9),(9,4)\) | 10 | 360 | 3 | 3 | 0 |
| \((5,8)\) | 78 | 840 | 13 | 13 | 0 |
| \((8,5)\) | 90 | 840 | 13 | 13 | 0 |
| \((6,7)\) | 165 | 1260 | 23 | 23 | 0 |
| \((7,6)\) | 170 | 1260 | 23 | 23 | 0 |
| \((4,10),(10,4)\) | 13 | 491 | 4 | 4 | 0 |
| \((5,9)\) | 107 | 1320 | 19 | 19 | 0 |
| \((9,5)\) | 134 | 1320 | 19 | 19 | 0 |

All cases with zero residual lift trivially with \(H=0\).  This includes
the edge strip in the proved edge gauge and the tested width-one interior
strip \((3,b),(b,3)\) through \((3,11),(11,3)\).

The timed-out cases were
\[
  (6,8),\qquad (8,6),\qquad (7,7).
\]
They produced no row and no inconsistency value.

## First Square Lift

In bidegree \((4,4)\), the residual
\[
\begin{aligned}
R^{\mathrm{free}}_{4,4}
  &=
  \frac{43}{7}\hbar^2D(X_{0\to1}X_{1\to2}Y_{2\to3}Y_{3\to0})\\
  &\quad-\frac{43}{7}\hbar^2D(X_{0\to1}X_{2\to3}Y_{1\to2}Y_{3\to0})\\
  &\quad-\frac{43}{7}\hbar^3D(X_{0\to0}\mid Y_{0\to0})
  +\frac{43}{7}\hbar^3N\,D(X_{0\to1}Y_{1\to0})
\end{aligned}
\]
is the image of one square cell:
\[
  H_{4,4}=\frac{43}{14}\,\sigma(XXXYYXYY;2,5),
\]
where positions are zero-indexed and
\[
  \partial_2\sigma(XXXYYXYY;2,5)
  =
  -YXXXYY+YXXYXY+YXYYXX-YYXYXX.
\]
Thus
\[
  D^\square_{4,4}H_{4,4}=R^{\mathrm{free}}_{4,4}.
\]
This is a genuine square transgression, not merely an abstract
\(\ker\partial\) correction.  It is gauge-equivalent to the \(K_{4,4}\)
correction already in the appendix.

## Balanced Test

The first balanced case with a larger residual is \((5,5)\).  One square
lift found by exact elimination is
\[
\begin{aligned}
H_{5,5}
  &=
  \frac{13}{9}\sigma(XXXXYYXYYY;3,6)
  +\frac{293}{42}\sigma(XXXXYYYXYY;3,7)\\
  &\quad
  +\frac{1409}{126}\sigma(XXXXYYYYXY;3,8)
  -\frac{121}{63}\sigma(XXXYXYYXYY;2,7),
\end{aligned}
\]
and \(D^\square_{5,5}H_{5,5}=R^{\mathrm{free}}_{5,5}\).  The coefficients
are pivot-gauge data, not yet a natural formula.

## Failed All-Bidegree Proof Step

The finite results support the stronger theorem but do not prove it.  The
missing object is a uniform decorated Stokes formula:
for every PBW matching stratum, one must assign a signed square-cell
current whose decorated boundary reproduces the Moyal odd coefficient and
the Capelli endpoint cancellations.

The edge proof works because each column has the four-term form
\[
  \Theta_r-\Theta_{r+1}-\hbar\Phi_r+\hbar\Phi_{b-1-r}.
\]
Interior bidegrees have nonadjacent PBW matchings, trace splittings, and
several independent cyclic separations.  The square-cell solves show that
these terms are square curvatures in the tested window, but no closed
matching-stratum formula was constructed.

## Exact Obstruction Row

If the decorated PBW Stokes theorem fails in bidegree \((a,b)\), the exact
obstruction is a row
\[
  \lambda\in\ker(D^\square_{a,b})^*
\]
with
\[
  \lambda(R^{\mathrm{free}}_{a,b})\ne0.
\]
Equivalently, after extending the row to a vertex potential,
\[
  (\phi,-\lambda)\in\ker B_{a,b}^*,
  \qquad
  B_{a,b}(W)=(\partial W,C^+_{a,b}(W)),
\]
one has
\[
  \lambda(E^+_{a,b})-\phi(T_{a,b})\ne0.
\]
After rescaling, the obstruction value can be normalized to \(1\).  No
such row was produced in this pass.

## Commands Run

All Python commands used `PYTHONDONTWRITEBYTECODE=1` and `python3 -B`;
the total-degree \(14\) probe used `python3 -u -B` to flush progress.

```text
python3 -B -m py_compile \
  scripts/quantum_shear_trace_diagram_normal_form.py \
  scripts/quantum_shear_primitive_search.py \
  scripts/quantum_shear_universal_formula.py \
  scripts/check_moyal_coefficients.py
```

Output: exit code `0`.

Inline exact Python imports constructed square-cell boundaries, formed
\(D^\square\)-columns from
`normal_form_word_times_moment`, and solved the rational systems with
`solve_sparse`.  They wrote no files and produced the tables above.
