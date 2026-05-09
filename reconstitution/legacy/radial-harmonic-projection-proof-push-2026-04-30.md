# Radial harmonic projection proof push

Date: 2026-04-30.

## Stable conclusion

The all-bidegree radial/Weyl theorem was not proved in this pass.  The
exact obstruction has been sharpened to a single finite-dimensional cokernel
class in each bidegree.  No computed row produced a nonzero obstruction.

The obstruction is not the ordinary necklace graph.  The ordinary graph
Green operator solves only
\[
  \partial c=T_{a,b}.
\]
The quantum correction equation sees PBW contractions, split trace diagrams,
and the Capelli term.  It is
\[
  C^+_{a,b}(K)=R^{\mathrm{free}}_{a,b},
  \qquad K\in\ker\partial.
\]

## The big cokernel object

Let
\[
  \mathsf W_{a,b}=\mathbb Q\langle X,Y\rangle_{a-1,b-1},
  \qquad
  \mathsf V_{a,b}=\mathsf{Cyc}_{a,b}.
\]
The incidence map is
\[
  \partial W=[WYX]-[WXY].
\]
Let
\[
  C^+_{a,b}(W)=
  \pi_+\mathcal N_{\mathrm{free}}\operatorname{Tr}(WM),
  \qquad M=YX-XY+\hbar NI.
\]
Define
\[
  B_{a,b}\colon\mathsf W_{a,b}\to
  \mathsf V_{a,b}\oplus\mathsf{Diag}_{a,b},
  \qquad
  B_{a,b}(W)=(\partial W,C^+_{a,b}(W)).
\]
Put
\[
  T_{a,b}=
  \sum_{j=0}^{b}[Y^jX^aY^{b-j}]
  -{b+1\over\binom{a+b}{a}}
  \sum_{U\in\operatorname{Sh}(a,b)}[U],
\]
and
\[
  E^+_{a,b}=\pi_+\mathcal N_{\mathrm{free}}(E_{a,b,N}).
\]
Then the exact obstruction class is
\[
  \Omega^{\mathrm{rad}}_{a,b}
  =
  [(T_{a,b},E^+_{a,b})]\in\operatorname{coker}B_{a,b}.
\]

This is equivalent to the appendix Hodge obstruction.  If
\(\partial c^{\mathrm{cl}}=T_{a,b}\), then
\[
  R^{\mathrm{free}}_{a,b}=E^+_{a,b}-C^+_{a,b}(c^{\mathrm{cl}}),
  \qquad
  A_{a,b}=C^+_{a,b}|_{\ker\partial},
\]
and
\[
  \Omega^{\mathrm{rad}}_{a,b}=0
  \Longleftrightarrow
  R^{\mathrm{free}}_{a,b}\in\operatorname{im}A_{a,b}
  \Longleftrightarrow
  \Pi^{\mathrm{harm}}_{a,b}R^{\mathrm{free}}_{a,b}=0.
\]

When the projection vanishes, the canonical correction is
\[
  K_{a,b}=
  A_{a,b}^*(A_{a,b}A_{a,b}^*)^{-1}R^{\mathrm{free}}_{a,b},
\]
with the inverse on \(\operatorname{im}A_{a,b}\).

## Dual obstruction row

A dual row is a pair
\[
  (\phi,\lambda)\in
  \mathsf V_{a,b}^*\oplus\mathsf{Diag}_{a,b}^*
\]
such that
\[
  \lambda C^+_{a,b}(W)=\phi(\partial W)
  \qquad(W\in\mathsf W_{a,b}).
\]
Equivalently, the edge cochain \(W\mapsto\lambda C^+_{a,b}(W)\) has zero
period on every cycle of the two-colour necklace graph, hence is a vertex
potential difference.  This is the potential form already recorded in the
appendix.

The theorem to prove is
\[
  \lambda(E^+_{a,b})=\phi(T_{a,b})
  \qquad\text{for every dual row }(\phi,\lambda).
\]
If a row violates this equality, then
\[
  \lambda(E^+_{a,b})-\phi(T_{a,b})
\]
is the exact obstruction theorem in bidegree \((a,b)\).  It is the same
class as the nonzero harmonic projection.

## Why the current data do not close the theorem

The scripts solve exact rational finite systems in the free indexed diagram
basis.  They produce certificates.  The linear algebra is pivot-gauge
Gaussian elimination.  It is not a natural homotopy in \((a,b)\).

The \((4,4)\) control failure shows the point:
\[
\begin{aligned}
R^{\mathrm{cl}}_{4,4}
={43\over 7}\bigl(
&\hbar^2D[X_{0\to1}X_{1\to2}Y_{2\to3}Y_{3\to0}]
-\hbar^2D[X_{0\to1}X_{2\to3}Y_{1\to2}Y_{3\to0}]\\
&-\hbar^3D[X_{0\to0}\mid Y_{0\to0}]
+\hbar^3N D[X_{0\to1}Y_{1\to0}]
\bigr).
\end{aligned}
\]
This residual is killed by a decorated cycle correction, but it is not
killed by the ordinary incidence lift.  Thus the missing all-bidegree
object is genuinely decorated.

## Computation ledger

Completed exact rows with zero corrected residual:

```text
(4,4):  residual=4,   correction=4,  rank=10,  rows=49,  cols=20
(5,5):  residual=22,  correction=16, rank=29,  rows=143, cols=70
(6,6):  residual=96,  correction=54, rank=93,  rows=446, cols=252

(3,10): residual=0,   correction=0,  rank=21,  rows=104, cols=55
(10,3): residual=0,   correction=0,  rank=21,  rows=104, cols=55
(4,9):  residual=10,  correction=12, rank=57,  rows=285, cols=165
(9,4):  residual=10,  correction=12, rank=57,  rows=285, cols=165
(5,8):  residual=78,  correction=46, rank=111, rows=542, cols=330
(8,5):  residual=90,  correction=49, rank=111, rows=542, cols=330
(6,7):  residual=165, correction=83, rank=154, rows=744, cols=462
(7,6):  residual=170, correction=79, rank=154, rows=744, cols=462

(3,11): residual=0,   correction=0,  rank=25,  rows=123, cols=66
(11,3): residual=0,   correction=0,  rank=25,  rows=123, cols=66
(4,10): residual=13,  correction=16, rank=76,  rows=376, cols=220
(10,4): residual=13,  correction=14, rank=76,  rows=376, cols=220
(5,9):  residual=107, correction=68, rank=161, rows=781, cols=495
(9,5):  residual=134, correction=65, rank=161, rows=781, cols=495
```

The near-balanced \((6,8)\) probe timed out after 240 seconds.  The
\((8,6)\) and \((7,7)\) probe was stopped afterward and supplies no
evidence.

Finite-rank covariant check:

```text
N=2, a=b=4: PASS, defect_terms=280,  rank=27, rows=1062,  cols=76
N=3, a=b=4: PASS, defect_terms=9713, rank=35, rows=35339, cols=76
```

This finite-rank check is only a falsification test.  The theorem surface
uses the free indexed diagram basis and stable injectivity.

## Next theorem target

Construct a decorated Stokes theorem for PBW matchings:

For every diagram functional \(\lambda\), if the decorated edge cochain
\[
  W\mapsto\lambda C^+_{a,b}(W)
\]
is a potential difference on \(G_{a,b}\), then its evaluation on the Moyal
shear target equals the potential evaluation on the classical shear vertex
chain:
\[
  \lambda E^+_{a,b}=\phi_\lambda(T_{a,b}).
\]

This is the proof obligation.  A larger finite table is useful only as a
falsification device.  The computational companion target is a dual-row
extraction mode for the sparse solver: on inconsistency it should output
\((\phi,\lambda)\in\ker B_{a,b}^*\) and the scalar
\(\lambda E^+_{a,b}-\phi(T_{a,b})\).  That row would be the first exact
obstruction theorem if the all-bidegree statement fails.
