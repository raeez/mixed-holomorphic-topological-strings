# Agent 303: radial decorated PBW Stokes identity construction push

Date: 2026-04-30.

Owned paths:

- `reconstitution/radial-decorated-pbw-stokes-identity-construction-push-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-303-radial-decorated-pbw-stokes-identity-construction-push.md`

No TeX or script file was edited.

## Claim Attacked

The target was the decorated PBW Stokes identity for
\[
  D^\square_{a,b}=C^+_{a,b}\partial_2,
\]
where \(\partial_2\) is the square-cell boundary for commuting adjacent
\(XY\leftrightarrow YX\) moves.  The identity would prove that every
dual potential row satisfies
\[
  \lambda(E^+_{a,b})=\phi_\lambda(T_{a,b})
\]
in all bidegrees.

## Result

Status: not proved in all bidegrees.  No obstruction row was found.

The exact square-cell solve lifted every decided residual through total
degree \(13\), and lifted \((4,10),(10,4),(5,9),(9,5)\) in total degree
\(14\).  The first unresolved bidegree in this pass is \((6,8)\), where
the exact free-diagram solve exceeded the \(180\)-second per-case alarm.
The symmetric case \((8,6)\) and the balanced case \((7,7)\) also timed
out.  These are computational frontiers, not cokernel rows.

The first interior square lift is explicit:
\[
  H_{4,4}=\frac{43}{14}\sigma(XXXYYXYY;2,5),
\]
with
\[
  \partial_2\sigma(XXXYYXYY;2,5)
  =
  -YXXXYY+YXXYXY+YXYYXX-YYXYXX,
\]
and
\[
  D^\square_{4,4}H_{4,4}=R^{\mathrm{free}}_{4,4}.
\]

The first larger balanced lift is
\[
\begin{aligned}
H_{5,5}
  &=
  \frac{13}{9}\sigma(XXXXYYXYYY;3,6)
  +\frac{293}{42}\sigma(XXXXYYYXYY;3,7)\\
  &\quad
  +\frac{1409}{126}\sigma(XXXXYYYYXY;3,8)
  -\frac{121}{63}\sigma(XXXYXYYXYY;2,7).
\end{aligned}
\]

## Failure Mode

The all-bidegree proof still lacks a natural matching-stratum Stokes
formula.  The finite square solves prove that the tested residuals are
square curvatures, but the coefficients are pivot-gauge data.  The missing
construction must assign PBW contractions, split-trace terms, and Capelli
endpoint cancellations to square-cell currents uniformly in \((a,b)\).

## Exact Obstruction If Theorem Fails

A genuine failure in bidegree \((a,b)\) is exactly a row
\[
  \lambda\in\ker(D^\square_{a,b})^*
\]
with
\[
  \lambda(R^{\mathrm{free}}_{a,b})\ne0.
\]
Equivalently, it is a signed potential row
\[
  (\phi,-\lambda)\in\ker B_{a,b}^*
\]
such that
\[
  \lambda(E^+_{a,b})-\phi(T_{a,b})\ne0.
\]
No such row exists in the decided finite systems.

## Evidence

- Read `CLAUDE.md`, `AGENTS.md`, the ecosystem proof/audit sections, the
  two prior radial reports, `appendix-radial-parts-moyal.tex`, and the
  relevant normal-form scripts.
- Verified the finite square-cell image directly, not only the abstract
  \(\ker\partial\) correction image.
- Compiled the relevant Python scripts with `py_compile`; exit code `0`.

## Commands Run

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B -m py_compile \
  scripts/quantum_shear_trace_diagram_normal_form.py \
  scripts/quantum_shear_primitive_search.py \
  scripts/quantum_shear_universal_formula.py \
  scripts/check_moyal_coefficients.py
```

Inline exact Python probes:

- square-cell solve for selected cases \((2,6),(3,3),(3,4),(4,3),(3,5),(5,3),(4,4),(3,6),(6,3),(5,5)\);
- sweep of all bidegrees \(a,b\ge2\) with \(a+b\le12\);
- sweep of total degree \(13\);
- bounded total-degree \(14\) probe with \(180\)-second per-case alarms;
- support extraction for \((4,4),(4,5),(5,4),(5,5)\).

All inline probes wrote no files.

Files changed: the two owned markdown reports above.
