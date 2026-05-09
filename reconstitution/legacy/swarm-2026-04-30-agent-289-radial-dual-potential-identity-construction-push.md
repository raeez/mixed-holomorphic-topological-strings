# Agent 289: radial dual-potential identity construction push

Date: 2026-04-30.

Owned write paths:

- `reconstitution/radial-dual-potential-identity-construction-push-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-289-radial-dual-potential-identity-construction-push.md`

No TeX or script file was edited.

## Loaded Context

Read `CLAUDE.md`, `AGENTS.md`, `~/ecosystem/INVARIANTS.md`,
`~/ecosystem/AGENTS-HARNESS.md`, the local `chriss-ginzburg-rectify` skill,
and the Vol II rectification harness.  Read the radial appendix, theorem
lane, open-obligation radial row, claim-strength radial rows,
`reconstitution/radial-harmonic-projection-proof-push-2026-04-30.md`,
`reconstitution/radial-all-interior-necklace-homotopy-push-2026-04-30.md`,
`reconstitution/radial-edge-pbw-telescoping-theorem-2026-04-30.md`, and the
radial/Weyl scripts.

Important local anchors:

- `appendix-radial-parts-moyal.tex`: Moyal convention, Capelli
  triangularization, quantum shear primitive, free indexed normal diagrams,
  decorated Hodge obstruction, potential form, edge PBW telescoping, and
  finite certificates.
- `theorem-lanes.tex:2471-2610`: degree-zero Moyal/Weyl sector and radial
  obstruction gate.
- `theorem-lanes.tex:3483-3523`: radial trace-diagram theorem lane.
- `open-obligations.tex:1237-1306`: radial/Weyl finite certificates and
  uniform homotopy gate.
- `claim-strength-ledger.tex:876-920` and `claim-strength-ledger.tex:1113-1147`:
  finite certificates plus exact uniform-homotopy obstruction.
- `scripts/quantum_shear_trace_diagram_normal_form.py`: free diagram basis,
  Moyal target, normal form of \(\operatorname{Tr}(WM)\), and
  kernel-correction solve.

The worktree already contains modified TeX and added script files outside
this lane.  They were read, not reverted or overwritten.

## Claim Attacked

For every dual row
\[
  (\phi,\lambda)\in
  \mathsf V_{a,b}^*\oplus\mathsf{Diag}_{a,b}^*
\]
with
\[
  \lambda C^+_{a,b}(W)=\phi(\partial W)
  \qquad(W\in\mathsf W_{a,b}),
\]
prove
\[
  \lambda(E^+_{a,b})=\phi(T_{a,b}).
\]
If this fails, exhibit the exact signed obstruction row in
\(\ker B^*_{a,b}\).

## Result

Status: all-bidegree proof not closed; exact obstruction theorem proved; no
finite violating row found.

The dual-potential identity is equivalent to
\[
  \Omega^{\mathrm{rad}}_{a,b}
  =
  [(T_{a,b},E^+_{a,b})]\in\operatorname{coker}B_{a,b}
\]
being zero.  After a classical lift
\(\partial c^{\mathrm{cl}}_{a,b}=T_{a,b}\), this is equivalent to
\[
  R^{\mathrm{free}}_{a,b}
  =
  E^+_{a,b}-C^+_{a,b}(c^{\mathrm{cl}}_{a,b})
  \in\operatorname{im}
  (C^+_{a,b}|_{\ker\partial}).
\]
It is also equivalent to vanishing of the decorated harmonic projection.

If the theorem fails, finite-dimensional duality gives the obstruction row:
\[
  (\phi,-\lambda)\in\ker B^*_{a,b},
  \qquad
  \lambda(E^+_{a,b})-\phi(T_{a,b})\ne0.
\]
Equivalently, in the potential-row convention used by the radial ledger,
\((\phi,\lambda)\) satisfies \(\lambda C^+_{a,b}(W)=\phi(\partial W)\).
This row is the exact obstruction, and may be normalized to have value
\(1\).  No such row appeared in the bounded computations.

## New Report

The detailed proof ledger was written to
`reconstitution/radial-dual-potential-identity-construction-push-2026-04-30.md`.
It contains:

- the exact dual theorem and proof;
- the potential interpretation on the two-colour necklace graph;
- the failure point of the all-bidegree decorated Stokes proof;
- direct \(B_{a,b}\)-membership computations;
- command outputs;
- the next construction target.

## Computations Run

All Python commands used `PYTHONDONTWRITEBYTECODE=1` and `python3 -B`.

1. Syntax check:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B -m py_compile \
  scripts/check_moyal_coefficients.py \
  scripts/quantum_shear_primitive_search.py \
  scripts/quantum_shear_universal_formula.py \
  scripts/quantum_shear_trace_diagram_normal_form.py
```

Output: exit code `0`, no stdout.

2. Moyal/Capelli/radial finite harness:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B scripts/check_moyal_coefficients.py
```

Key output:

```text
Moyal sweep: checked 14641 monomial pairs, exponents <= 10, orders <= 11.  PASS.
Capelli triangular round-trip: checked 121 monomials with a, b <= 10.  PASS.
N=2 radial restriction: checked 80 operator/test-polynomial pairs.  PASS.
N=3 radial restriction: checked 80 operator/test-polynomial pairs.  PASS.
Rank-2 radial-parts commutator: all listed pairs PASS.
ALL CHECKS PASS.
```

3. Bare classical lift control failure:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 4,4 --classical-only --max-terms 8
```

Output:

```text
FAIL a=4 b=4 mode=classical-only target_terms=39 candidate_terms=9 residual_terms=4
43/7 hbar^2 D[(X0>1,X1>2,Y2>3,Y3>0)]
-43/7 hbar^2 D[(X0>1,X2>3,Y1>2,Y3>0)]
-43/7 hbar^3 D[(X0>0) (Y0>0)]
43/7 hbar^3 N D[(X0>1,Y1>0)]
```

4. Decorated kernel corrections:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 4,4 --case 5,5 --case 6,6 \
  --kernel-correction --progress --max-terms 1
```

Output:

```text
(4,4): residual_terms=4, correction_terms=4, rank=10, rows=49, cols=20, corrected_residual_terms=0
(5,5): residual_terms=22, correction_terms=16, rank=29, rows=143, cols=70, corrected_residual_terms=0
(6,6): residual_terms=96, correction_terms=54, rank=93, rows=446, cols=252, corrected_residual_terms=0
PASS: all requested kernel-correction obstruction classes vanish.
```

5. Interior strip checks:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 3,10 --case 10,3 --case 4,9 --case 9,4 \
  --kernel-correction --progress --max-terms 1
```

Output:

```text
(3,10): residual_terms=0, correction_terms=0, rank=21, rows=104, cols=55, corrected_residual_terms=0
(10,3): residual_terms=0, correction_terms=0, rank=21, rows=104, cols=55, corrected_residual_terms=0
(4,9): residual_terms=10, correction_terms=12, rank=57, rows=285, cols=165, corrected_residual_terms=0
(9,4): residual_terms=10, correction_terms=12, rank=57, rows=285, cols=165, corrected_residual_terms=0
PASS: all requested kernel-correction obstruction classes vanish.
```

6. Direct big-\(B\) membership check:

```text
case=(2,8) consistent=True rank=4 rows=13 cols=8 visible_left_nullity=9 support=4
case=(3,6) consistent=True rank=9 rows=34 cols=21 visible_left_nullity=25 support=9
case=(4,4) consistent=True rank=10 rows=39 cols=20 visible_left_nullity=29 support=10
case=(5,5) consistent=True rank=29 rows=117 cols=70 visible_left_nullity=88 support=29
case=(4,9) consistent=True rank=57 rows=230 cols=165 visible_left_nullity=173 support=57
case=(9,4) consistent=True rank=57 rows=230 cols=165 visible_left_nullity=173 support=57
```

These rows directly test \((T_{a,b},E^+_{a,b})\in\operatorname{im}B_{a,b}\).
They prove the dual-potential identity for every row in the tested finite
systems.

## Attack-Heal Ledger

```yaml
- id: A289-01
  severity: 2
  status: valid-not-closed
  lens: all-bidegree decorated Stokes identity
  target: lambda(E^+_{a,b}) = phi(T_{a,b})
  broken_step: no matching-family Stokes theorem was constructed for
    multi-letter interior PBW contractions and split-trace diagrams
  repair: prove the exact equivalence with Omega^rad_{a,b}=0 and identify
    the signed obstruction row in ker B^*_{a,b}
  residual: construct the decorated Stokes/Hodge homotopy or extract the
    first nonzero dual row

- id: A289-02
  severity: 3
  status: healed-finite
  lens: tested bidegrees
  target: direct B-membership and kernel-correction rows
  finding: all tested rows are consistent; no violating dual row appears
  residual: finite checks remain certificates, not the uniform theorem

- id: A289-03
  severity: 2
  status: valid
  lens: ordinary incidence Green operator
  target: bare classical lift in (4,4)
  finding: the four-term 43/7 positive residual is nonzero
  repair: keep the decorated correction map C^+|ker(partial), not the
    ordinary graph Green operator, as the theorem object
```

## Remaining Obligation

Build the decorated Stokes theorem for PBW matching strata:
if \(W\mapsto\lambda C^+_{a,b}(W)\) is a potential difference on
\(G_{a,b}\), then the Moyal shear target evaluates by the same potential on
the classical shear chain.  If this fails, print the first exact signed row
\((\phi,-\lambda)\in\ker B^*_{a,b}\) with nonzero
\(\lambda(E^+_{a,b})-\phi(T_{a,b})\).

Files changed:

- `reconstitution/radial-dual-potential-identity-construction-push-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-289-radial-dual-potential-identity-construction-push.md`
