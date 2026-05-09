# Radial decorated PBW/Stokes computational frontier audit

Date: 2026-04-30.

## Status

The bidegrees
\[
  (6,8),\qquad (8,6),\qquad (7,7)
\]
are computational frontier cases in the current free normal-diagram basis.
They are not known obstruction rows.

Agents 289 and 296 identified the exact obstruction theorem.  Agents 303
and 314 pushed finite certificates through total degree \(13\), and Agent
303 lifted the total-degree \(14\) cases
\[
  (3,11),(11,3),(4,10),(10,4),(5,9),(9,5).
\]
The first undecided total-degree \(14\) systems are exactly
\((6,8),(8,6),(7,7)\).  Agent 303 reports timeout at the 180-second
per-case alarm, with no left-cokernel row and no inconsistency value.

My bounded reruns support that classification.  For all three frontier
cases the ordinary cyclic boundary equation closes immediately.  The
current bottleneck appears before a proof-grade obstruction solve:
expansion of the Weyl/Moyal target into free indexed normal diagrams
did not finish under a 20-second per-case alarm.

No manuscript TeX or script file was edited.

## Files read

- `CLAUDE.md`.
- `~/ecosystem/INVARIANTS.md`, especially the voice and attacker-ledger
  verification rules.
- `~/ecosystem/AGENTS-HARNESS.md`, especially the high-stakes
  self-reflection and proof-obligation rules.
- `~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`.
- `appendix-radial-parts-moyal.tex`.
- `scripts/check_moyal_coefficients.py`.
- `scripts/quantum_shear_primitive_search.py`.
- `scripts/quantum_shear_universal_formula.py`.
- `scripts/quantum_shear_trace_diagram_normal_form.py`.
- Agent reports 289, 296, 303, 314, both the compact swarm reports and
  the paired detailed reports where present.

## Exact theorem object

The current theorem surface is not a generic radial-parts appeal.  It is
the following finite-dimensional obstruction problem in each bidegree.

Let
\[
  M=YX-XY+\hbar NI,
\]
and let
\[
  C^+_{a,b}(W)
  =
  \pi_+\mathcal N_{\mathrm{free}}\operatorname{Tr}(WM).
\]
The cyclic target is
\[
  T_{a,b}
  =
  \sum_{j=0}^{b}[Y^jX^aY^{b-j}]
  -
  {b+1\over\binom{a+b}{a}}
  \sum_{U\in\operatorname{Sh}(a,b)}[U],
\]
and
\[
  E^+_{a,b}=\pi_+\mathcal N_{\mathrm{free}}(E_{a,b,N}).
\]
With
\[
  B_{a,b}(W)=(\partial W,C^+_{a,b}(W)),
  \qquad
  \eta_{a,b}=(T_{a,b},E^+_{a,b}),
\]
the obstruction class is
\[
  \Omega^{\mathrm{rad}}_{a,b}
  =
  [\eta_{a,b}]\in\operatorname{coker}B_{a,b}.
\]

After choosing a classical lift
\[
  \partial c^{\mathrm{cl}}_{a,b}=T_{a,b},
\]
put
\[
  R^{\mathrm{free}}_{a,b}
  =
  E^+_{a,b}-C^+_{a,b}(c^{\mathrm{cl}}_{a,b}).
\]
The ordinary square-cell mechanism gives
\[
  \ker\partial=\operatorname{im}\partial_2
\]
over \(\mathbb Q\).  Hence the deciding cellular map is
\[
  D^\square_{a,b}=C^+_{a,b}\partial_2.
\]
The all-bidegree theorem is
\[
  R^{\mathrm{free}}_{a,b}\in\operatorname{im}D^\square_{a,b}
  \quad\text{for all }a,b,
\]
equivalently
\[
  \lambda D^\square_{a,b}=0
  \Longrightarrow
  \lambda(R^{\mathrm{free}}_{a,b})=0.
\]

If the theorem fails, the exact obstruction is a normalized row
\[
  \lambda\in\ker(D^\square_{a,b})^*
  \quad\text{with}\quad
  \lambda(R^{\mathrm{free}}_{a,b})=1,
\]
equivalently a signed potential row
\[
  (\phi,-\lambda)\in\ker B_{a,b}^*
  \quad\text{with}\quad
  \lambda(E^+_{a,b})-\phi(T_{a,b})=1.
\]
No such row is known in the named reports or in my bounded checks.

## Frontier arithmetic

The current script expands the Weyl trace normal form by summing over
all shuffles:
\[
  \operatorname{Weyl}_{p,q}^{\mathrm{nf}}
  =
  {1\over\binom{p+q}{p}}
  \sum_{U\in\operatorname{Sh}(p,q)}
  \mathcal N_{\mathrm{free}}\operatorname{Tr}(U).
\]
For the quantum shear target in bidegree \((a,b)\), the odd Moyal orders
use
\[
  (p,q)=(a+1-r,b+1-r),\qquad r=1,3,5,\ldots .
\]
Thus the frontier target-expansion counts are:

| Bidegree | word columns \(\binom{a+b-2}{a-1}\) | cyclic rows/rank | Moyal shuffle trace words | bounded target normal form |
|---|---:|---:|---:|---|
| \((6,8)\) | 792 | 217 / 216 | 3229 | timeout \(>20\) s |
| \((8,6)\) | 792 | 217 / 216 | 3229 | timeout \(>20\) s |
| \((7,7)\) | 924 | 246 / 245 | 3706 | timeout \(>20\) s |

For comparison, the already reported total-degree \(13\) central cases
\((6,7)\) and \((7,6)\) have 462 word columns and 1853 Moyal shuffle
trace words.  The jump to total degree \(14\) is therefore a real basis
and target-expansion frontier, not evidence of a cokernel class.

The ordinary cycle dimensions after the classical boundary solve are:

| Bidegree | cyclic vertices | based word edges | cycle dimension \(E-V+1\) |
|---|---:|---:|---:|
| \((6,8)\) | 217 | 792 | 576 |
| \((8,6)\) | 217 | 792 | 576 |
| \((7,7)\) | 246 | 924 | 679 |

This suggests a better exact formulation: solve the decorated correction
on a cycle basis, not on the full word span with cyclic constraints and
not on an overcomplete square-cell set.

## Commands run

All Python commands used `PYTHONDONTWRITEBYTECODE=1` and `python3 -B`.

Syntax:

```text
python3 -B -m py_compile \
  scripts/check_moyal_coefficients.py \
  scripts/quantum_shear_primitive_search.py \
  scripts/quantum_shear_universal_formula.py \
  scripts/quantum_shear_trace_diagram_normal_form.py
```

Result: exit code `0`.

Formal Moyal/Capelli/radial finite harness:

```text
python3 -B scripts/check_moyal_coefficients.py
```

Key output:

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

Bare \((4,4)\) control failure:

```text
python3 -B scripts/quantum_shear_trace_diagram_normal_form.py \
  --self-test --self-test-rank 2 --self-test-max-length 5 \
  --case 4,4 --classical-only --max-terms 8
```

Output:

```text
PASS self-test rank=2 max_length=5 checked=63
FAIL a=4 b=4 mode=classical-only target_terms=39 candidate_terms=9 residual_terms=4
      43/7 * hbar^2 D[(X0>1,X1>2,Y2>3,Y3>0)]
     -43/7 * hbar^2 D[(X0>1,X2>3,Y1>2,Y3>0)]
     -43/7 * hbar^3 D[(X0>0) (Y0>0)]
      43/7 * hbar^3 N D[(X0>1,Y1>0)]
```

Frontier cyclic boundary solve:

```text
python3 -B scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 6,8 --case 8,6 --case 7,7 \
  --solve-classical --progress --max-terms 1
```

Output:

```text
PASS a=6 b=8 mode=classical-solve support=216 rank=216 rows=217 cols=792
PASS a=8 b=6 mode=classical-solve support=216 rank=216 rows=217 cols=792
PASS a=7 b=7 mode=classical-solve support=245 rank=245 rows=246 cols=924
PASS: all requested cyclic boundary equations have rational lifts.
```

Bounded frontier-stage probe:

```text
python3 -B - <<'PY'
...
PY
```

The probe imported `solve_classical_case`, `shear_defect_normal_form`,
and `normal_form_word_times_moment`, with `signal.alarm(20)` around the
expensive stages.  Output:

```text
CASE (6, 8) words=792
  classical_solve: ok 0.03s (True, 216, 217, 792, 216)
  target_nf: timeout>20s after 20.00s
  first20_columns_nf: ok 0.01s 704
CASE (8, 6) words=792
  classical_solve: ok 0.05s (True, 216, 217, 792, 216)
  target_nf: timeout>20s after 20.01s
  first20_columns_nf: ok 0.00s 647
CASE (7, 7) words=924
  classical_solve: ok 0.04s (True, 245, 246, 924, 245)
  target_nf: timeout>20s after 20.00s
  first20_columns_nf: ok 0.00s 677
```

The first-20-column timing is not a global column-construction estimate:
the failed target expansion populates some `lru_cache` entries before
the alarm fires.  It is still useful as a stage separator.  The target
normal-form expansion is already too expensive in the current shuffle
basis before the left-cokernel question is reached.

## Faster exact route

1. Replace the shuffle-by-shuffle target expansion in
   `scripts/quantum_shear_trace_diagram_normal_form.py:371-396` by an
   orbit-compressed exact formula
   \[
     \mathcal W_{p,q}^{\mathrm{nf}}
     =
     {1\over\binom{p+q}{p}}
     \sum_{[U,\Gamma]}
     m_{p,q}(U,\Gamma)(-\hbar)^{|\Gamma|}
     N^{e(U,\Gamma)}\mathsf D(U,\Gamma),
   \]
   where \([U,\Gamma]\) runs over cyclic isomorphism classes of shuffle
   words decorated by PBW inversion matchings.  This keeps the same free
   normal form but sums multiplicities before canonicalizing diagrams.

2. Split the computation after the classical solve.  Compute a sparse
   rational cycle basis for \(\ker\partial\) of dimension \(E-V+1\), then
   solve
   \[
     C^+_{a,b}(K)=R^{\mathrm{free}}_{a,b}
   \]
   on that basis.  This avoids repeatedly carrying the cyclic rows inside
   the positive-diagram solve.  If a square-cell witness is needed, use
   the proved ordinary identity \(\ker\partial=\operatorname{im}\partial_2\)
   to lift the resulting cycle to square cells afterward.

3. Add modular sparse membership and left-cokernel extraction to
   `scripts/quantum_shear_primitive_search.py:347-419`.  The current
   `solve_sparse` performs full rational row reduction over all rows.
   For this frontier the decisive output is membership or a left row, not
   a pretty pivot-gauge primitive.  A finite-field row-space test can
   either reconstruct a rational certificate or print a candidate
   left-cokernel row for exact verification.

4. Add an explicit failure mode to
   `scripts/quantum_shear_trace_diagram_normal_form.py:973-989`: on
   inconsistency, print a normalized row
   \[
     \lambda\in\ker(D^\square_{a,b})^*,
     \qquad
     \lambda(R^{\mathrm{free}}_{a,b})=1,
   \]
   or, in the larger system,
   \[
     (\phi,-\lambda)\in\ker B_{a,b}^*,
     \qquad
     \lambda(E^+_{a,b})-\phi(T_{a,b})=1.
   \]
   Without this, a failed large solve is only a runtime event.

5. Audit the \(X/Y\) symmetry before duplicating work on \((6,8)\) and
   \((8,6)\).  A symplectic signed involution should relate the two
   systems after tracking the sign of \(M=YX-XY+\hbar NI\), cyclic
   orientation, and the Moyal shear normalization.  Do not use the
   symmetry as a theorem until those signs are checked.

## Manuscript wording

The theorem surface should say:

> The formal Weyl/Moyal coefficients, Capelli triangular normalization,
> reduced open-line Wick weights, free indexed normal-ordering formula,
> stable trace-diagram injectivity, edge PBW telescoping strip, \(K_{4,4}\),
> and the named finite certificates are proved.  The all-interior
> radial/Weyl trace comparison is the decorated PBW Stokes problem
> \(D^\square_{a,b}H_{a,b}=R^{\mathrm{free}}_{a,b}\), equivalently
> \(\lambda D^\square_{a,b}=0\Rightarrow
> \lambda(R^{\mathrm{free}}_{a,b})=0\).  The first undecided bidegrees in
> the present exact free-diagram basis are \((6,8),(8,6),(7,7)\).  They
> are computationally undecided and carry no known nonzero obstruction
> row.  A failure theorem must exhibit a normalized signed row
> \((\phi,-\lambda)\in\ker B_{a,b}^*\) with
> \(\lambda(E^+_{a,b})-\phi(T_{a,b})=1\).

Do not write that the finite table proves the all-bidegree theorem.  Do
not write that \((6,8),(8,6),(7,7)\) are obstructed.  Do not leave the
frontier described only as \((7,7)\).

## Patch targets

- `appendix-radial-parts-moyal.tex:820-963`: after the decorated Hodge
  obstruction theorem, insert the cellular square complex and the exact
  \(D^\square_{a,b}\)-Hodge formulation from Agent 296.
- `appendix-radial-parts-moyal.tex:965-1027`: sharpen the
  dual-potential proposition so the square-cell map is not only mentioned
  but stated as the equivalent finite-dimensional obstruction complex.
- `appendix-radial-parts-moyal.tex:1061-1111`: distinguish ordinary
  square-cell generation of \(\ker\partial\) from decorated PBW/Stokes
  vanishing in \(\mathsf{Diag}_{a,b}\).
- `appendix-radial-parts-moyal.tex:1658-1713`: update finite exact
  arithmetic anchors to record the total-degree \(14\) frontier
  \((6,8),(8,6),(7,7)\) as timeout/frontier cases, not obstruction rows.
- `theorem-lanes.tex:2530-2558` and `theorem-lanes.tex:2591-2607`:
  make \(D^\square_{a,b}=C^+_{a,b}\partial_2\) and the left-cokernel
  criterion the displayed all-interior gate.
- `open-obligations.tex:1388-1402`: replace the current wording that
  singles out only \((7,7)\) with the exact frontier list
  \((6,8),(8,6),(7,7)\), unless a later agent supplies command evidence
  closing \((6,8)\) and \((8,6)\).
- `open-obligations.tex:1404-1440`: replace the generic
  "associated-graded Hodge homotopy" phrase by the square-cell
  obstruction
  \[
    \Pi^\square_{a,b}R^{\mathrm{free}}_{a,b}=0.
  \]
- `claim-strength-ledger.tex:993-1030`: add the same \(D^\square\)
  cellular formulation and frontier status.
- `scripts/quantum_shear_trace_diagram_normal_form.py:371-396`:
  replace shuffle-by-shuffle Weyl target expansion with exact orbit
  aggregation.
- `scripts/quantum_shear_trace_diagram_normal_form.py:745-801`: add a
  cycle-basis correction mode.
- `scripts/quantum_shear_primitive_search.py:347-419`: add modular sparse
  row-space membership and normalized left-row extraction.

## Verdict

The unresolved bidegrees are timeout/frontier cases in the current exact
formulation.  The next useful computation is not a longer unstructured
run.  It is an exact target-normal-form compression plus a sparse
membership/left-cokernel solver.  The manuscript should state the
decorated PBW Stokes theorem as the remaining all-interior theorem and
should classify \((6,8),(8,6),(7,7)\) as computationally undecided until
one of two proof-grade outputs exists: a square-cell certificate or a
normalized obstruction row.
