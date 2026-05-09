# Agent 352: radial certificate bound propagation

Date: 2026-04-30.

## Claim attacked

Agent 345 found a propagation lag: the short `main.tex` summaries still
said the radial finite certificates reached only all non-edge bidegrees of
total degree at most \(12\), while `open-obligations.tex` recorded later
total-degree \(13\) and partial total-degree \(14\) closures.

## Current bound

The current certificate surface is:

- Proposition~\ref{prop:app-edge-pbw-telescoping} closes the edge strips
  \((2,b)\) and \((a,2)\) for all \(a,b\).
- The finite certificates close the balanced diagonal through \((6,6)\).
- The finite certificates close all non-edge bidegrees of total degree at
  most \(13\), explicitly
  \[
    (3,10),(10,3),(4,9),(9,4),(5,8),(8,5),(6,7),(7,6)
  \]
  in total degree \(13\).
- The total-degree \(14\) certificates close
  \[
    (3,11),(11,3),(4,10),(10,4),(5,9),(9,5).
  \]
- The first undecided total-degree \(14\) systems are
  \[
    (6,8),(8,6),(7,7).
  \]
  These are timeout/frontier computations in the current exact free
  normal-diagram basis.  The ordinary cyclic boundary equation closes and
  no signed obstruction row is known.

This matches `open-obligations.tex:1394`--`open-obligations.tex:1414`,
Agent 303's square-cell report, Agent 321's frontier audit, Agent 337's
open-obligations heal, and Agent 345's consistency note.

## Patch

I made the authorized tiny certificate-count correction in `main.tex`.
The two stale summaries now state total degree \(13\), the six closed
total-degree \(14\) cases, and the undecided frontier
\((6,8),(8,6),(7,7)\):

- `main.tex:2451`--`main.tex:2458`.
- `main.tex:2786`--`main.tex:2795`.

No theorem strength was increased: the all-interior theorem remains the
dual-potential/decorated PBW Stokes problem
\(\Omega^{\mathrm{rad}}_{a,b}=0\), equivalently
\(D^\square_{a,b}=C^+_{a,b}\partial_2\), with failure detected by a
signed row in \(\ker B_{a,b}^*\).

## Script checks

Compiled the current radial/Moyal scripts:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B -m py_compile \
  scripts/quantum_shear_trace_diagram_normal_form.py \
  scripts/quantum_shear_primitive_search.py \
  scripts/quantum_shear_universal_formula.py \
  scripts/check_moyal_coefficients.py
```

Exit code: `0`.

Ran the formal Moyal/Capelli/radial finite harness:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B scripts/check_moyal_coefficients.py
```

Result: `ALL CHECKS PASS`; the run checked `14641` monomial pairs,
`121` Capelli round trips, direct `N=2` and `N=3` radial restrictions,
rank-2 radial commutators, open-line midpoint weights, and even-order
vanishing through `r=10`.

Ran the total-degree \(13\) kernel-correction check:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 3,10 --case 10,3 --case 4,9 --case 9,4 \
  --case 5,8 --case 8,5 --case 6,7 --case 7,6 \
  --kernel-correction --progress --max-terms 0
```

Result: all eight cases passed with `corrected_residual_terms=0`; the
final line was `PASS: all requested kernel-correction obstruction classes
vanish.`

Ran the completed total-degree \(14\) kernel-correction check:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 3,11 --case 11,3 --case 4,10 --case 10,4 \
  --case 5,9 --case 9,5 \
  --kernel-correction --progress --max-terms 0
```

Result: all six cases passed with `corrected_residual_terms=0`; the final
line was `PASS: all requested kernel-correction obstruction classes
vanish.`

Ran the frontier cyclic-boundary check:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  scripts/quantum_shear_trace_diagram_normal_form.py \
  --case 6,8 --case 8,6 --case 7,7 \
  --solve-classical --progress --max-terms 0
```

Result: the classical boundary equations pass with
`rank=216 rows=217 cols=792` for \((6,8)\) and \((8,6)\), and
`rank=245 rows=246 cols=924` for \((7,7)\).  This supports the current
classification: undecided decorated target solve, not known obstruction.

## Files changed

- `main.tex`
- `reconstitution/swarm-2026-04-30-agent-352-radial-certificate-bound-propagation.md`

No build was run; the assignment requested the targeted propagation check.

## Verification

```text
git diff --check -- main.tex
git diff --no-index --check -- /dev/null \
  reconstitution/swarm-2026-04-30-agent-352-radial-certificate-bound-propagation.md
```

Result: no whitespace errors.  The added-report check has the ordinary
`--no-index` difference status for comparing `/dev/null` with a new file.
