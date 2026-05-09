# Agent 314: radial all-N decorated PBW/Stokes attack-heal

Date: 2026-04-30.

Owned write paths:

- `reconstitution/radial-all-n-decorated-pbw-stokes-attack-heal-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-314-radial-all-n-decorated-pbw-stokes-attack-heal.md`

No manuscript TeX or script file was edited.

## Claim attacked

The target was the all-N radial-parts/Weyl-trace input behind the
degree-zero Moyal lane, including:

\[
  D^\square_{a,b}=C^+_{a,b}\partial_2,
  \qquad
  \Omega^{\mathrm{rad}}_{a,b}
  =
  [(T_{a,b},E^+_{a,b})]\in\operatorname{coker}B_{a,b},
\]

the signed dual row \((\phi,-\lambda)\in\ker B_{a,b}^*\), and the edge
families \((2,b)\), \((a,2)\).

## Result

Status: all-bidegree proof not closed; exact obstruction theorem surface
confirmed; no nonzero obstruction row found.

The proved finite and structural data are:

- formal Weyl/Moyal coefficients and odd-power constants;
- Capelli triangular normalization and contact shift \(YX-XY+\hbar NI\);
- free indexed normal-ordering formula;
- stable injectivity for free trace diagrams;
- all-edge PBW telescoping families \((2,b)\), \((a,2)\);
- all-N free corrections for \((4,4),(5,5),(6,6)\);
- total-degree \(13\) interior finite certificate checked in this pass.

The missing theorem is the decorated PBW Stokes identity:

\[
  \lambda D^\square_{a,b}=0
  \quad\Longrightarrow\quad
  \lambda(R^{\mathrm{free}}_{a,b})=0.
\]

Equivalently, every signed potential row
\[
  (\phi,-\lambda)\in\ker B_{a,b}^*
\]
must satisfy
\[
  \lambda(E^+_{a,b})=\phi(T_{a,b}).
\]
Failure is exactly a normalized row with value \(1\).

## Reports read

- Agent 289:
  `reconstitution/swarm-2026-04-30-agent-289-radial-dual-potential-identity-construction-push.md`.
- Agent 296:
  `reconstitution/swarm-2026-04-30-agent-296-radial-structural-hodge-proof-mechanism.md`.
- Agent 303: no matching report is present under `reconstitution/`.

## Commands run

All Python commands used `PYTHONDONTWRITEBYTECODE=1` and `python3 -B`.

```text
python3 -B -m py_compile scripts/check_moyal_coefficients.py \
  scripts/quantum_shear_primitive_search.py \
  scripts/quantum_shear_universal_formula.py \
  scripts/quantum_shear_trace_diagram_normal_form.py
```

Exit code `0`.

```text
python3 -B scripts/check_moyal_coefficients.py
```

Passed:

- `14641` monomial pairs, exponents `<= 10`, orders `<= 11`;
- `121` Capelli round trips;
- `80` direct `N=2` radial restrictions;
- `80` direct `N=3` radial restrictions;
- rank-2 radial commutator checks;
- open-line midpoint graph weights.

Checked odd coefficients:

\[
  1,\quad {1\over24},\quad {1\over1920},\quad
  {1\over322560},\quad {1\over92897280},\quad
  {1\over40874803200}.
\]

```text
python3 -B scripts/quantum_shear_trace_diagram_normal_form.py \
  --self-test --self-test-rank 2 --self-test-max-length 5 \
  --case 4,4 --classical-only --max-terms 8
```

The PBW self-test passed on `63` words.  The bare \((4,4)\) cyclic lift
failed with the expected four-term \(43/7\) residual:

```text
43/7 hbar^2 D[(X0>1,X1>2,Y2>3,Y3>0)]
-43/7 hbar^2 D[(X0>1,X2>3,Y1>2,Y3>0)]
-43/7 hbar^3 D[(X0>0) (Y0>0)]
43/7 hbar^3 N D[(X0>1,Y1>0)]
```

```text
python3 -B scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 4,4 --case 5,5 --case 6,6 \
  --kernel-correction --progress --max-terms 3
```

Passed:

```text
(4,4): residual_terms=4,  correction_terms=4,  rank=10, rows=49,  cols=20,  corrected_residual_terms=0
(5,5): residual_terms=22, correction_terms=16, rank=29, rows=143, cols=70,  corrected_residual_terms=0
(6,6): residual_terms=96, correction_terms=54, rank=93, rows=446, cols=252, corrected_residual_terms=0
```

```text
python3 -B scripts/quantum_shear_trace_diagram_normal_form.py \
  --family-only --edge-family-max 9 --kernel-correction --progress --max-terms 1
```

All edge cases \((2,b)\), \((b,2)\), \(2\le b\le9\), passed with zero
residual and zero correction.

```text
python3 -B scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 3,10 --case 10,3 --case 4,9 --case 9,4 \
  --case 5,8 --case 8,5 --case 6,7 --case 7,6 \
  --kernel-correction --progress --max-terms 1
```

Passed:

```text
(3,10): residual_terms=0,   correction_terms=0,  rank=21,  rows=104, cols=55,  corrected_residual_terms=0
(10,3): residual_terms=0,   correction_terms=0,  rank=21,  rows=104, cols=55,  corrected_residual_terms=0
(4,9):  residual_terms=10,  correction_terms=12, rank=57,  rows=285, cols=165, corrected_residual_terms=0
(9,4):  residual_terms=10,  correction_terms=12, rank=57,  rows=285, cols=165, corrected_residual_terms=0
(5,8):  residual_terms=78,  correction_terms=46, rank=111, rows=542, cols=330, corrected_residual_terms=0
(8,5):  residual_terms=90,  correction_terms=49, rank=111, rows=542, cols=330, corrected_residual_terms=0
(6,7):  residual_terms=165, correction_terms=83, rank=154, rows=744, cols=462, corrected_residual_terms=0
(7,6):  residual_terms=170, correction_terms=79, rank=154, rows=744, cols=462, corrected_residual_terms=0
```

## Attack-heal conclusion

The all-N theorem cannot be upgraded from finite certificates.  The exact
accepted target is:

\[
  \Omega^{\mathrm{rad}}_{a,b}=0
  \quad\text{for all }a,b,
\]

or, in square-cell form,

\[
  \Pi^\square_{a,b}R^{\mathrm{free}}_{a,b}=0
  \quad\text{for all }a,b.
\]

The exact obstruction, if it exists, is:

\[
  (\phi,-\lambda)\in\ker B_{a,b}^*,
  \qquad
  \lambda(E^+_{a,b})-\phi(T_{a,b})=1.
\]

## TeX patch targets

No TeX patch was made.  The next manuscript patch should target:

- `appendix-radial-parts-moyal.tex:965-1059`: insert the square-cell complex,
  \(\operatorname{im}\partial_2=\ker\partial\), \(D^\square\), and the
  square-cell Hodge obstruction theorem.
- `appendix-radial-parts-moyal.tex:1061-1111`: sharpen the potential remark:
  ordinary square cells generate cycles, but decorated PBW contractions decide
  the obstruction.
- `theorem-lanes.tex:2509-2669`: keep all-bidegree status open and state the
  \(D^\square\) left-cokernel criterion.
- `open-obligations.tex:1304-1391`: make the acceptance gate either all
  \(\Pi^\square R=0\) or the first normalized signed obstruction row.
- `claim-strength-ledger.tex:957-1015`: record \(D^\square\) as the deciding
  decorated map, not as proof of vanishing.
- `main.tex:2328-2350` and `main.tex:2640-2675`: summary is accurate; if
  tightened, phrase the frontier as the \(D^\square\) decorated Stokes problem.

## Remaining obligations

1. Prove the decorated PBW Stokes identity for all bidegrees.
2. Add sparse-solver dual-row extraction for inconsistent finite systems.
3. Prove a closed formula for the width-one interior strips \(a=3\) or
   \(b=3\), where finite checks show zero correction.
4. Keep this algebraic radial/Weyl gate separate from Costello graph/QME,
   one-antifield principal-part, and physical trace-state claims.
