# Agent 321: radial decorated PBW/Stokes computational frontier audit

Date: 2026-04-30.

Owned write paths:

- `reconstitution/radial-decorated-stokes-computational-frontier-audit-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-321-radial-decorated-stokes-computational-frontier-audit.md`

No manuscript TeX or script file was edited.

## Claim attacked

After Agents 303 and 314, the undecided bidegrees were
\[
  (6,8),\qquad (8,6),\qquad (7,7).
\]
The audit question was whether these are obstruction cases or only
computational frontier cases in the current exact free normal-diagram
basis.

## Result

Status: computational frontier.  No obstruction row is known.

The exact theorem object remains the decorated PBW Stokes problem
\[
  D^\square_{a,b}H_{a,b}=R^{\mathrm{free}}_{a,b},
  \qquad
  D^\square_{a,b}=C^+_{a,b}\partial_2.
\]
Equivalently,
\[
  \lambda D^\square_{a,b}=0
  \Longrightarrow
  \lambda(R^{\mathrm{free}}_{a,b})=0.
\]
Failure is precisely a normalized row
\[
  \lambda\in\ker(D^\square_{a,b})^*,
  \qquad
  \lambda(R^{\mathrm{free}}_{a,b})=1,
\]
or, in the larger potential system,
\[
  (\phi,-\lambda)\in\ker B_{a,b}^*,
  \qquad
  \lambda(E^+_{a,b})-\phi(T_{a,b})=1.
\]

Agents 289 and 296 prove this obstruction formulation.  Agent 303
reports that \((6,8),(8,6),(7,7)\) timed out at the total-degree \(14\)
square-cell frontier, with no cokernel row.  Agent 314 confirms the same
all-bidegree theorem surface and no nonzero obstruction row.

## Local checks

Syntax:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B -m py_compile \
  scripts/check_moyal_coefficients.py \
  scripts/quantum_shear_primitive_search.py \
  scripts/quantum_shear_universal_formula.py \
  scripts/quantum_shear_trace_diagram_normal_form.py
```

Exit code `0`.

Formal finite harness:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B scripts/check_moyal_coefficients.py
```

Passed: `14641` monomial pairs through order `11`, `121` Capelli round
trips, `80` direct `N=2` radial restrictions, `80` direct `N=3` radial
restrictions, rank-2 Cartan commutators, open-line midpoint weights, and
even-order vanishing through `r=10`.

Control failure:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  scripts/quantum_shear_trace_diagram_normal_form.py \
  --self-test --self-test-rank 2 --self-test-max-length 5 \
  --case 4,4 --classical-only --max-terms 8
```

The self-test passed on `63` words.  The bare \((4,4)\) classical lift
failed with the expected four-term \(43/7\) residual:

```text
43/7 hbar^2 D[(X0>1,X1>2,Y2>3,Y3>0)]
-43/7 hbar^2 D[(X0>1,X2>3,Y1>2,Y3>0)]
-43/7 hbar^3 D[(X0>0) (Y0>0)]
43/7 hbar^3 N D[(X0>1,Y1>0)]
```

Frontier cyclic solve:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  scripts/quantum_shear_trace_diagram_normal_form.py \
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

Bounded stage probe with `signal.alarm(20)`:

```text
CASE (6, 8) words=792
  classical_solve: ok 0.03s (True, 216, 217, 792, 216)
  target_nf: timeout>20s after 20.00s
CASE (8, 6) words=792
  classical_solve: ok 0.05s (True, 216, 217, 792, 216)
  target_nf: timeout>20s after 20.01s
CASE (7, 7) words=924
  classical_solve: ok 0.04s (True, 245, 246, 924, 245)
  target_nf: timeout>20s after 20.00s
```

The obstruction solve is not being reached in these bounded probes.  The
target normal-form expansion is the first wall.

## Exact bottleneck

The frontier target expansion contains:

| Bidegree | word columns | cyclic rows/rank | Moyal shuffle trace words |
|---|---:|---:|---:|
| \((6,8)\) | 792 | 217 / 216 | 3229 |
| \((8,6)\) | 792 | 217 / 216 | 3229 |
| \((7,7)\) | 924 | 246 / 245 | 3706 |

For comparison, \((6,7)\) and \((7,6)\) have `462` columns and `1853`
Moyal shuffle trace words.  Total degree \(14\) therefore crosses a real
combinatorial threshold in the current formulation.

## Faster exact formulation

1. Aggregate
   \[
     \mathcal N_{\mathrm{free}}\operatorname{Weyl}_{p,q}
   \]
   by PBW matching orbits instead of expanding each shuffle word
   separately.  Patch target:
   `scripts/quantum_shear_trace_diagram_normal_form.py:371-396`.

2. After the classical solve, replace the full word-span correction solve
   by a cycle-basis solve for \(C^+_{a,b}|_{\ker\partial}\).  The cycle
   dimensions are `576`, `576`, and `679` for the three frontier cases.
   Patch target:
   `scripts/quantum_shear_trace_diagram_normal_form.py:745-801`.

3. Add modular sparse membership and left-row extraction to the rational
   solver.  Patch target:
   `scripts/quantum_shear_primitive_search.py:347-419`.

4. On inconsistency, print the normalized obstruction row.  A failed
   runtime is not a mathematical obstruction.

## Manuscript patch targets

- `appendix-radial-parts-moyal.tex:820-1027`: insert the square-cell
  complex and exact \(D^\square\)-Hodge formulation.
- `appendix-radial-parts-moyal.tex:1658-1713`: record
  \((6,8),(8,6),(7,7)\) as the total-degree \(14\) computational
  frontier.
- `theorem-lanes.tex:2530-2607`: state the all-interior gate as the
  decorated PBW Stokes criterion for \(D^\square_{a,b}\).
- `open-obligations.tex:1388-1402`: do not list only \((7,7)\) as open;
  the current frontier list is \((6,8),(8,6),(7,7)\), unless later
  command evidence closes the first two.
- `claim-strength-ledger.tex:993-1030`: add the \(D^\square\) cellular
  obstruction form and the same frontier status.

## Recommendation

The manuscript theorem surface should say: proved finite algebraic model
plus exact decorated PBW/Stokes obstruction theorem; total-degree \(14\)
frontier \((6,8),(8,6),(7,7)\) undecided by timeout; no nonzero
obstruction row known.  The next computation should be target
normal-form compression plus sparse membership/left-cokernel extraction,
not a longer run of the current shuffle-expanded solver.

Files changed:

- `reconstitution/radial-decorated-stokes-computational-frontier-audit-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-321-radial-decorated-stokes-computational-frontier-audit.md`
