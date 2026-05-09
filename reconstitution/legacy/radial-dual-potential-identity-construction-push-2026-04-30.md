# Radial dual-potential identity construction push

Date: 2026-04-30.

## Status

The all-bidegree identity
\[
  \lambda(E^+_{a,b})=\phi(T_{a,b})
\]
was not proved in this pass.  No bounded computation produced a violating
dual row.  The exact result proved here is the linear-dual obstruction
theorem: failure in bidegree \((a,b)\) is equivalent to a signed row
\[
  (\phi,-\lambda)\in\ker B^*_{a,b}
\]
with nonzero value
\[
  \lambda(E^+_{a,b})-\phi(T_{a,b}).
\]
This row is the same obstruction as the nonzero decorated harmonic projection
of \(R^{\mathrm{free}}_{a,b}\).

The finite rows tested below satisfy direct membership
\[
  (T_{a,b},E^+_{a,b})\in\operatorname{im}B_{a,b}.
\]
Thus every dual row in those finite systems satisfies the potential identity,
including systems with nontrivial visible left nullity.

## Setup

Let
\[
  \mathsf W_{a,b}=\mathbb Q\langle X,Y\rangle_{a-1,b-1},
  \qquad
  \mathsf V_{a,b}=\mathsf{Cyc}_{a,b}.
\]
The ordinary incidence map is
\[
  \partial W=[WYX]-[WXY].
\]
Let \(\mathsf{Diag}_{a,b}\) be the positive free indexed normal-diagram
target, and put
\[
  C^+_{a,b}(W)
  =
  \pi_+\mathcal N_{\mathrm{free}}\operatorname{Tr}(WM),
  \qquad
  M=YX-XY+\hbar NI.
\]
The big map is
\[
  B_{a,b}\colon\mathsf W_{a,b}\to
  \mathsf V_{a,b}\oplus\mathsf{Diag}_{a,b},
  \qquad
  B_{a,b}(W)=(\partial W,C^+_{a,b}(W)).
\]
With this sign convention, a potential row written as
\((\phi,\lambda)\) is the signed dual vector \((\phi,-\lambda)\in
\ker B^*_{a,b}\); equivalently it satisfies
\(\lambda C^+_{a,b}(W)=\phi(\partial W)\).  This is the convention used
below.
The target is
\[
  \eta_{a,b}=(T_{a,b},E^+_{a,b}),
\]
where
\[
  T_{a,b}
  =
  \sum_{j=0}^b[Y^jX^aY^{b-j}]
  -{b+1\over\binom{a+b}{a}}
  \sum_{U\in\operatorname{Sh}(a,b)}[U],
\]
and
\[
  E^+_{a,b}=\pi_+\mathcal N_{\mathrm{free}}(E_{a,b,N}).
\]
The obstruction class is
\[
  \Omega^{\mathrm{rad}}_{a,b}
  =
  [\eta_{a,b}]\in\operatorname{coker}B_{a,b}.
\]

## Exact Dual Theorem

**Proposition.**  For fixed \((a,b)\), the following are equivalent.

1. \(\Omega^{\mathrm{rad}}_{a,b}=0\).
2. For every pair
   \[
     (\phi,\lambda)\in
     \mathsf V_{a,b}^*\oplus\mathsf{Diag}_{a,b}^*
   \]
   satisfying
   \[
     \lambda C^+_{a,b}(W)=\phi(\partial W)
     \qquad(W\in\mathsf W_{a,b}),
   \]
   one has
   \[
     \lambda(E^+_{a,b})=\phi(T_{a,b}).
   \]
3. After any choice of \(c^{\mathrm{cl}}_{a,b}\) with
   \(\partial c^{\mathrm{cl}}_{a,b}=T_{a,b}\), the residual
   \[
     R^{\mathrm{free}}_{a,b}
     =
     E^+_{a,b}-C^+_{a,b}(c^{\mathrm{cl}}_{a,b})
   \]
   lies in
   \[
     \operatorname{im}\bigl(C^+_{a,b}|_{\ker\partial}\bigr).
   \]
4. The decorated harmonic projection of \(R^{\mathrm{free}}_{a,b}\) is zero.

**Proof.**  A potential row \((\phi,\lambda)\) with
\(\lambda C^+_{a,b}(W)=\phi(\partial W)\) is, in the literal dual of
\(B_{a,b}(W)=(\partial W,C^+_{a,b}(W))\), the row \((\phi,-\lambda)\).
It annihilates every \(B_{a,b}(W)\).  Hence
\[
  (\phi,-\lambda)(\eta_{a,b})
  =
  \phi(T_{a,b})-\lambda(E^+_{a,b})
\]
and the vanishing condition is exactly
\(\lambda(E^+_{a,b})=\phi(T_{a,b})\).  Since all spaces are finite
dimensional in fixed bidegree,
\[
  \eta_{a,b}\in\operatorname{im}B_{a,b}
  \quad\Longleftrightarrow\quad
  \ell(\eta_{a,b})=0
  \text{ for every }\ell\in\ker B_{a,b}^*.
\]
This proves the equivalence of (1) and (2).

Choose \(c^{\mathrm{cl}}_{a,b}\) with \(\partial c^{\mathrm{cl}}=T_{a,b}\).
Then
\[
  \eta_{a,b}-B_{a,b}(c^{\mathrm{cl}}_{a,b})
  =
  (0,R^{\mathrm{free}}_{a,b}).
\]
Adding \(B_{a,b}(K)\) with \(K\in\ker\partial\) changes only the positive
diagram component by \(C^+_{a,b}(K)\).  Thus \(\eta_{a,b}\in\operatorname{im}
B_{a,b}\) if and only if \(R^{\mathrm{free}}_{a,b}\in
\operatorname{im}(C^+_{a,b}|_{\ker\partial})\).  The Hodge formulation is
the finite-dimensional decomposition
\[
  \mathsf{Diag}_{a,b}
  =
  \operatorname{im}(C^+_{a,b}|_{\ker\partial})
  \oplus
  \ker(C^+_{a,b}|_{\ker\partial})^*.
\]

## Potential Form

The graph \(G_{a,b}\) has vertices the cyclic words in
\(\mathsf V_{a,b}\), and an edge
\[
  e_W\colon[WXY]\to[WYX].
\]
For \(a,b>0\) this graph is connected.  If
\[
  \lambda C^+_{a,b}(W)=\phi(\partial W),
\]
then the edge cochain \(W\mapsto\lambda C^+_{a,b}(W)\) has zero period on
each cycle and is a potential difference:
\[
  \lambda C^+_{a,b}(W)
  =
  \phi([WYX])-\phi([WXY]).
\]
The additive constant in \(\phi\) does not affect \(\phi(T_{a,b})\), since
the total coefficient of \(T_{a,b}\) is zero.

The missing all-bidegree theorem is therefore exactly the decorated Stokes
identity: every such potential must evaluate the Moyal shear target by the
same boundary formula,
\[
  \lambda(E^+_{a,b})=\phi(T_{a,b}).
\]

## What Was Proved

The identity is proved for every bidegree in which \(\Omega^{\mathrm{rad}}\)
is already killed by an explicit primitive.

- Edge strips \((2,b)\) and \((a,2)\): proved by the PBW telescoping theorem.
- Certified rows with direct \(B_{a,b}\)-membership below: proved by exact
  rational free normal-diagram linear algebra.
- General interior all-bidegree: not proved.  The missing object is a
  functorial decorated Stokes/Hodge homotopy, not a larger finite table.

Direct \(B_{a,b}\)-membership tests:

```text
case=(2,8) consistent=True rank=4 rows=13 cols=8 visible_left_nullity=9 support=4
case=(3,6) consistent=True rank=9 rows=34 cols=21 visible_left_nullity=25 support=9
case=(4,4) consistent=True rank=10 rows=39 cols=20 visible_left_nullity=29 support=10
case=(5,5) consistent=True rank=29 rows=117 cols=70 visible_left_nullity=88 support=29
case=(4,9) consistent=True rank=57 rows=230 cols=165 visible_left_nullity=173 support=57
case=(9,4) consistent=True rank=57 rows=230 cols=165 visible_left_nullity=173 support=57
```

Here `visible_left_nullity=rows-rank` counts the left-null directions seen
on the finite row support of the tested system.  Consistency proves that
all those rows annihilate \((T_{a,b},E^+_{a,b})\).

## Failed All-Bidegree Proof Attempt

The natural strategy is to decompose \(E^+_{a,b}\) by PBW matching type and
show that each matching family is a decorated divergence over \(G_{a,b}\).
The edge proof succeeds because there is only one moving letter.  The column
\(\mathcal N_{\mathrm{free}}\operatorname{Tr}(W_rM)\) has a four-term form,
and the Moyal target has the same discrete derivative with weight
\(b-1-2r\).

For \(a,b\ge3\), matchings can split traces and interact with more than one
cyclic separation.  No natural matching involution was constructed which
sends every positive PBW target diagram either to a decorated edge column or
to a cancelled Moyal odd coefficient.  The \((4,4)\) control failure shows
that the ordinary incidence Green operator is insufficient:

```text
43/7 * hbar^2 D[(X0>1,X1>2,Y2>3,Y3>0)]
-43/7 * hbar^2 D[(X0>1,X2>3,Y1>2,Y3>0)]
-43/7 * hbar^3 D[(X0>0) (Y0>0)]
43/7 * hbar^3 N D[(X0>1,Y1>0)]
```

This residual is killed by the decorated square correction \(K_{4,4}\), but
that correction is not supplied by the ordinary graph Laplacian.

## Exact Obstruction Row If Theorem Fails

If the identity fails in bidegree \((a,b)\), finite-dimensional duality gives
a row
\[
  (\phi,\lambda)\in
  \mathsf V_{a,b}^*\oplus\mathsf{Diag}_{a,b}^*
\]
such that
\[
  \lambda C^+_{a,b}(W)=\phi(\partial W)
  \qquad(W\in\mathsf W_{a,b})
\]
and
\[
  \delta_{a,b}:=
  \lambda(E^+_{a,b})-\phi(T_{a,b})\ne0.
\]
After rescaling, one may impose \(\delta_{a,b}=1\).  This is the exact
signed row
in \(\ker B^*_{a,b}\).  Equivalently, after a classical lift,
\(\lambda\in\ker(C^+_{a,b}|_{\ker\partial})^*\) and
\[
  \lambda(R^{\mathrm{free}}_{a,b})\ne0.
\]
This row is the obstruction theorem.  It is not a numerical hint and not a
finite-rank artifact; it is the dual representative of the cokernel class
\(\Omega^{\mathrm{rad}}_{a,b}\).  No such row was found in the bounded
computations run here.

## Commands Run

All Python commands were run with `PYTHONDONTWRITEBYTECODE=1` and `python3
-B`.  No bytecode, TeX, PDF, or script output file was intentionally written.

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B -m py_compile \
  scripts/check_moyal_coefficients.py \
  scripts/quantum_shear_primitive_search.py \
  scripts/quantum_shear_universal_formula.py \
  scripts/quantum_shear_trace_diagram_normal_form.py
```

Output: exit code `0`, no stdout.

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B scripts/check_moyal_coefficients.py
```

Output:

```text
[1] Moyal sweep: checked 14641 monomial pairs, exponents <= 10, orders <= 11.  PASS.
[2] Capelli triangular round-trip (J -> T -> J = id): checked 121 monomials with a, b <= 10.  PASS.
[4] Direct N=2 and N=3 radial-parts restriction:
     N=2: checked 80 operator/test-polynomial pairs.  PASS.
     N=3: checked 80 operator/test-polynomial pairs.  PASS.
[5] Rank-2 radial-parts commutator: all seven listed pairs PASS.
[7] Open-line midpoint graph weights: all listed pairs PASS.
[8] Even orders r=2,4,6,8,10 vanish in the star commutator on every monomial pair tested.
ALL CHECKS PASS.
```

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 4,4 --classical-only --max-terms 8
```

Output:

```text
FAIL a=4 b=4 mode=classical-only target_terms=39 candidate_terms=9 residual_terms=4
terms=4
      43/7 * hbar^2 D[(X0>1,X1>2,Y2>3,Y3>0)]
     -43/7 * hbar^2 D[(X0>1,X2>3,Y1>2,Y3>0)]
     -43/7 * hbar^3 D[(X0>0) (Y0>0)]
      43/7 * hbar^3 N D[(X0>1,Y1>0)]
FAIL: 1 check(s) have nonzero free trace-diagram residuals.
```

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 4,4 --case 5,5 --case 6,6 \
  --kernel-correction --progress --max-terms 1
```

Output:

```text
PASS a=4 b=4 mode=kernel-correction classical=ok classical_terms=9 residual_terms=4 correction=ok correction_terms=4 rank=10 rows=49 cols=20 corrected_residual_terms=0
PASS a=5 b=5 mode=kernel-correction classical=ok classical_terms=25 residual_terms=22 correction=ok correction_terms=16 rank=29 rows=143 cols=70 corrected_residual_terms=0
PASS a=6 b=6 mode=kernel-correction classical=ok classical_terms=79 residual_terms=96 correction=ok correction_terms=54 rank=93 rows=446 cols=252 corrected_residual_terms=0
PASS: all requested kernel-correction obstruction classes vanish.
```

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 3,10 --case 10,3 --case 4,9 --case 9,4 \
  --kernel-correction --progress --max-terms 1
```

Output:

```text
PASS a=3 b=10 mode=kernel-correction classical=ok classical_terms=21 residual_terms=0 correction=ok correction_terms=0 rank=21 rows=104 cols=55 corrected_residual_terms=0
PASS a=10 b=3 mode=kernel-correction classical=ok classical_terms=21 residual_terms=0 correction=ok correction_terms=0 rank=21 rows=104 cols=55 corrected_residual_terms=0
PASS a=4 b=9 mode=kernel-correction classical=ok classical_terms=54 residual_terms=10 correction=ok correction_terms=12 rank=57 rows=285 cols=165 corrected_residual_terms=0
PASS a=9 b=4 mode=kernel-correction classical=ok classical_terms=54 residual_terms=10 correction=ok correction_terms=12 rank=57 rows=285 cols=165 corrected_residual_terms=0
PASS: all requested kernel-correction obstruction classes vanish.
```

Direct \(B_{a,b}\)-membership snippet:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B - <<'PY'
...
PY
```

Output:

```text
case=(2,8) consistent=True rank=4 rows=13 cols=8 visible_left_nullity=9 support=4
case=(3,6) consistent=True rank=9 rows=34 cols=21 visible_left_nullity=25 support=9
case=(4,4) consistent=True rank=10 rows=39 cols=20 visible_left_nullity=29 support=10
case=(5,5) consistent=True rank=29 rows=117 cols=70 visible_left_nullity=88 support=29
case=(4,9) consistent=True rank=57 rows=230 cols=165 visible_left_nullity=173 support=57
case=(9,4) consistent=True rank=57 rows=230 cols=165 visible_left_nullity=173 support=57
```

## Next Construction Target

The next proof object is a decorated Stokes theorem for PBW matching
families.  It must construct, for every matching stratum and every diagram
functional \(\lambda\), a potential evaluation formula whose sum is
\[
  \lambda(E^+_{a,b})=\phi_\lambda(T_{a,b}).
\]
If that construction fails, the next computational target is a dual-row
extraction mode for the sparse solver: on inconsistency it must print the
signed row \((\phi,-\lambda)\in\ker B^*_{a,b}\) and the nonzero scalar
\(\lambda(E^+_{a,b})-\phi(T_{a,b})\).
