# Agent 269: radial harmonic projection proof push

Date: 2026-04-30.

Owned write paths:

- `reconstitution/swarm-2026-04-30-agent-269-radial-harmonic-projection-proof-push.md`
- `reconstitution/radial-harmonic-projection-proof-push-2026-04-30.md`

No TeX or script file was edited.

## Loaded context

Read `CLAUDE.md`, `AGENTS.md`, `~/ecosystem/INVARIANTS.md`,
`~/ecosystem/AGENTS-HARNESS.md`, the local `chriss-ginzburg-rectify` skill,
and the Vol II rectify skill.  Read the radial appendix, theorem lane,
open-obligations ledger, the quantum shear scripts, and prior radial reports
from Agents 191, 203, 209, 230, 248, and 255.

## Claim attacked

The all-bidegree radial/Weyl closure would follow from
\[
  \Pi^{\mathrm{harm}}_{a,b}R^{\mathrm{free}}_{a,b}=0
  \qquad(a,b\ge 1),
\]
equivalently from a functorial splitting of
\[
  A_{a,b}=C^+_{a,b}|_{\ker\partial}\colon
  \ker\partial\longrightarrow \mathsf{Diag}_{a,b}.
\]
The current appendix proves the finite-dimensional Hodge equivalence.  It
does not prove this projection vanishes.

## Result

Status: exact obstruction class sharpened; all-bidegree vanishing not proved.
No stable left-cokernel functional with nonzero pairing was found in the
new finite probes.

The strongest exact formulation is the big cokernel class
\[
  \Omega^{\mathrm{rad}}_{a,b}
  =
  [(T_{a,b},E^+_{a,b})]\in\operatorname{coker}B_{a,b},
  \qquad
  B_{a,b}(W)=(\partial W,C^+_{a,b}(W)).
\]
Here
\[
  T_{a,b}=
  \sum_{j=0}^{b}[Y^jX^aY^{b-j}]
  -{b+1\over\binom{a+b}{a}}
  \sum_{U\in\operatorname{Sh}(a,b)}[U],
\]
and \(E^+_{a,b}=\pi_+\mathcal N_{\mathrm{free}}(E_{a,b,N})\).
Vanishing of \(\Omega^{\mathrm{rad}}_{a,b}\) is equivalent to the kernel
correction equation.  After choosing any classical lift
\(\partial c^{\mathrm{cl}}_{a,b}=T_{a,b}\), it is the same obstruction as
\[
  \Pi^{\mathrm{harm}}_{a,b}
  \bigl(E^+_{a,b}-C^+_{a,b}(c^{\mathrm{cl}}_{a,b})\bigr).
\]

The dual exact obstruction is a pair
\[
  (\phi,\lambda)\in \mathsf V_{a,b}^*\oplus\mathsf{Diag}_{a,b}^*
  \quad\text{with}\quad
  \lambda C^+_{a,b}(W)=\phi(\partial W)
  \quad\text{for all }W,
\]
such that
\[
  \lambda(E^+_{a,b})-\phi(T_{a,b})\ne0.
\]
This is the precise left-cokernel row to exhibit if the theorem fails.  The
all-bidegree proof is exactly the universal potential identity
\[
  \lambda(E^+_{a,b})=\phi(T_{a,b})
\]
for every such pair \((\phi,\lambda)\).

## Anchors

- `appendix-radial-parts-moyal.tex:559`: quantum shear primitive and
  trace-diagram obstruction.
- `appendix-radial-parts-moyal.tex:669`: free indexed normal diagrams and
  PBW normal-ordering.
- `appendix-radial-parts-moyal.tex:820`: decorated necklace complex,
  \(C^+_{a,b}\), \(A_{a,b}\), and \(\mathfrak o_{a,b}\).
- `appendix-radial-parts-moyal.tex:888`: decorated Hodge obstruction theorem.
- `appendix-radial-parts-moyal.tex:965`: potential form and failure of the
  bare graph Green operator.
- `appendix-radial-parts-moyal.tex:1017`: all-edge PBW telescoping theorem.
- `theorem-lanes.tex:2471`: degree-zero Moyal/Weyl theorem lane.
- `open-obligations.tex:1198`: radial/Weyl finite certificates and uniform
  homotopy gate.
- `scripts/quantum_shear_trace_diagram_normal_form.py:342`: free trace-word
  normal form.
- `scripts/quantum_shear_trace_diagram_normal_form.py:355`: normal form of
  \(\operatorname{Tr}(WM)\).
- `scripts/quantum_shear_trace_diagram_normal_form.py:382`: Moyal trace
  target.
- `scripts/quantum_shear_trace_diagram_normal_form.py:745`: tagged
  kernel-correction solve.
- `scripts/quantum_shear_primitive_search.py:347`: rational sparse solver;
  this is pivot-gauge evidence, not a functorial homotopy.

## Computations run

All commands were run with `PYTHONDONTWRITEBYTECODE=1` and `python3 -B`
where Python was used.  No bytecode, TeX, PDF, or script output file was
intentionally written.

1. Free normal-form self-test and built-in candidates:

```text
python3 -B scripts/quantum_shear_trace_diagram_normal_form.py \
  --self-test --self-test-rank 2 --self-test-max-length 6 --max-terms 0

PASS self-test rank=2 max_length=6 checked=127
PASS: all requested candidates have zero free trace-diagram residual.
```

2. Control failure of the bare classical lift:

```text
python3 -B scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 4,4 --classical-only --max-terms 8

FAIL a=4 b=4 mode=classical-only residual_terms=4
43/7*hbar^2 D[X0>1,X1>2,Y2>3,Y3>0]
-43/7*hbar^2 D[X0>1,X2>3,Y1>2,Y3>0]
-43/7*hbar^3 D[X0>0|Y0>0]
43/7*hbar^3 N D[X0>1,Y1>0]
```

This reproduces the obstruction to the bare incidence Green operator.

3. Decorated kernel corrections on the balanced diagonal:

```text
python3 -B scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 4,4 --case 5,5 --case 6,6 \
  --kernel-correction --progress --max-terms 0

(4,4): residual_terms=4,  correction_terms=4,  rank=10, rows=49,  cols=20
(5,5): residual_terms=22, correction_terms=16, rank=29, rows=143, cols=70
(6,6): residual_terms=96, correction_terms=54, rank=93, rows=446, cols=252
```

Every corrected residual vanished.

4. Total-degree 13 interior strip:

```text
python3 -B scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 3,10 --case 10,3 --case 4,9 --case 9,4 \
  --case 5,8 --case 8,5 --case 6,7 --case 7,6 \
  --kernel-correction --progress --max-terms 0
```

Result:

```text
(3,10): residual_terms=0,   correction_terms=0,  rank=21,  rows=104, cols=55
(10,3): residual_terms=0,   correction_terms=0,  rank=21,  rows=104, cols=55
(4,9):  residual_terms=10,  correction_terms=12, rank=57,  rows=285, cols=165
(9,4):  residual_terms=10,  correction_terms=12, rank=57,  rows=285, cols=165
(5,8):  residual_terms=78,  correction_terms=46, rank=111, rows=542, cols=330
(8,5):  residual_terms=90,  correction_terms=49, rank=111, rows=542, cols=330
(6,7):  residual_terms=165, correction_terms=83, rank=154, rows=744, cols=462
(7,6):  residual_terms=170, correction_terms=79, rank=154, rows=744, cols=462
```

Every corrected residual vanished.

5. Finite-rank covariant primitive check for \((4,4)\):

```text
python3 -B scripts/quantum_shear_primitive_search.py \
  --case 2,4,4 --case 3,4,4 --no-generic --max-terms 0

PASS N=2 a=4 b=4 mode=covariant-trace defect_terms=280  rank=27 rows=1062  cols=76 support=9
PASS N=3 a=4 b=4 mode=covariant-trace defect_terms=9713 rank=35 rows=35339 cols=76 support=10
```

This is finite-rank evidence only.

6. Bounded total-degree 14 probe:

```text
(3,11): residual_terms=0,   correction_terms=0,  rank=25,  rows=123, cols=66
(11,3): residual_terms=0,   correction_terms=0,  rank=25,  rows=123, cols=66
(4,10): residual_terms=13,  correction_terms=16, rank=76,  rows=376, cols=220
(10,4): residual_terms=13,  correction_terms=14, rank=76,  rows=376, cols=220
(5,9):  residual_terms=107, correction_terms=68, rank=161, rows=781, cols=495
(9,5):  residual_terms=134, correction_terms=65, rank=161, rows=781, cols=495
```

Every completed row had zero corrected residual.  The near-balanced
\((6,8)\) row hit a 240 second timeout before a result.  The follow-on
\((8,6)\) and \((7,7)\) frontier probe was stopped after the \((6,8)\)
timeout; it supplies no evidence.

## Attack-heal ledger

```yaml
- id: A269-01
  severity: 2
  status: valid-not-closed
  lens: all-bidegree harmonic projection
  target: stmt:app-free-kernel-homotopy-obstruction
  claim: finite decorated kernel corrections prove Pi_harm R=0 for all bidegrees
  broken_step: the sparse solver gives bidegree certificates, not a natural
    splitting of A_{a,b} or a proof of the dual potential identity
  repair: sharpen the obstruction to Omega_rad=[(T,E+)] in coker B and the
    detecting row (phi,lambda)
  residual: prove lambda(E+)=phi(T) for every dual row, or exhibit the first
    row with nonzero pairing

- id: A269-02
  severity: 3
  status: healed-finite
  lens: first possible low-degree obstruction
  target: total degrees 13 and partial 14
  finding: no left-cokernel obstruction appears in the completed exact rows
  residual: the near-balanced degree-14 rows remain computational frontier,
    beginning with (6,8), (8,6), and (7,7)

- id: A269-03
  severity: 2
  status: valid
  lens: bare Green operator
  target: ordinary necklace incidence complex
  finding: the bare classical lift fails already in (4,4) by the four-term
    43/7 positive residual
  repair: keep the decorated Hodge operator A A^*, not the ordinary graph
    Laplacian, as the correction object
```

## Next construction target

Do not extend the finite table as a substitute for proof.  The next theorem
target is the universal decorated Stokes identity:

For every \((\phi,\lambda)\) with
\[
  \lambda C^+_{a,b}(W)=\phi([WYX])-\phi([WXY]),
\]
prove
\[
  \lambda\pi_+\mathcal N_{\mathrm{free}}(E_{a,b,N})
  =
  \phi\!\left(
    \sum_{j=0}^{b}[Y^jX^aY^{b-j}]
    -{b+1\over\binom{a+b}{a}}
    \sum_{U\in\operatorname{Sh}(a,b)}[U]\right).
\]

If this identity fails, the exact obstruction theorem is the first row
\((\phi,\lambda)\in\ker B_{a,b}^*\) with nonzero value on
\((T_{a,b},E^+_{a,b})\).  The computational next target is therefore not a
larger certificate table but a row-extraction mode for `solve_sparse` that
prints such a dual functional when a case fails.

Files changed:

- `reconstitution/swarm-2026-04-30-agent-269-radial-harmonic-projection-proof-push.md`
- `reconstitution/radial-harmonic-projection-proof-push-2026-04-30.md`
