# Agent 230: radial all-interior necklace homotopy push

Date: 2026-04-30.

Owned write paths:

- `reconstitution/radial-all-interior-necklace-homotopy-push-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-230-radial-all-interior-necklace-homotopy-push.md`

No manuscript or script file was edited.

## Loaded protocol

Read `CLAUDE.md`, `AGENTS.md`, `~/ecosystem/INVARIANTS.md`,
`~/ecosystem/AGENTS-HARNESS.md`, the local `chriss-ginzburg-rectify` skill,
and the Vol II rectify skill.  Read the radial appendix, the normal-form
script, and prior radial reports from Agents 152, 172, 191, 203, 217, and
218.

## Claim pushed

The proved edge theorem leaves the all-interior bidegrees \(a,b\geq3\).
The strongest theorem surface is not another table.  It is:

\[
  R^{\mathrm{free}}_{a,b}\in
  \operatorname{im}\left(
    \mathcal C_{a,b}\colon\ker\partial\to\mathsf{Diag}_{a,b}
  \right)
  \quad(a,b\geq3),
\]
equivalently every stable left-cokernel functional
\(\lambda\mathcal C_{a,b}|_{\ker\partial}=0\) satisfies
\(\lambda(R^{\mathrm{free}}_{a,b})=0\).

## New formulation

The report reinterprets \(\partial W=[WYX]-[WXY]\) as the incidence map of
a graph \(G_{a,b}\):

- vertices: cyclic words with \(a\) letters \(X\), \(b\) letters \(Y\);
- oriented edges: source words \(W\) with \(a-1\) \(X\)'s and \(b-1\)
  \(Y\)'s, from \([WXY]\) to \([WYX]\);
- \(\ker\partial=H_1(G_{a,b})\).

This gives the associated-graded two-colour necklace habitat.  The
candidate homotopy is the decorated necklace Hodge homotopy
\[
  H^{\mathrm{neck}}_{a,b,q}
  =
  \iota_{a,b}\Delta^{-1}_{a,b,q}d^*_{a,b,q}\pi_{a,b,q}
\]
on positive PBW contraction degree.  The exact obstruction, if it exists,
is the harmonic projection
\[
  \Pi^{\mathrm{harm}}_{a,b}R^{\mathrm{free}}_{a,b}\neq0,
\]
or equivalently a stable left null row of the tagged kernel-correction
matrix with nonzero target pairing.

## New finite evidence

All commands were run with `PYTHONDONTWRITEBYTECODE=1` and `python3 -B`.

Total degree \(13\) non-edge strip:

```text
(3,10), (10,3): residual_terms=0, correction_terms=0
(4,9),  (9,4):  residual_terms=10, correction_terms=12
(5,8):          residual_terms=78, correction_terms=46
(8,5):          residual_terms=90, correction_terms=49
(6,7):          residual_terms=165, correction_terms=83
(7,6):          residual_terms=170, correction_terms=79
```

Every corrected residual vanished.  This extends the previous non-edge
finite window from total degree \(12\) to \(13\).

Width-one interior strips:

```text
(3,b), 3<=b<=12, and (a,3), 4<=a<=12:
residual_terms=0, correction_terms=0.
```

Width-two \(a=4\) strip:

```text
(4,4) through (4,11): every corrected residual vanished.
(4,12): stopped after no row returned; not used as evidence.
```

## Valid attacks

```yaml
- id: A230-01
  severity: 2
  status: healed-to-formulation
  target: all-interior radial/Weyl closure
  finding: the exact theorem is left-cokernel vanishing for the decorated
    two-colour necklace graph, not finite table extension
  residual: prove the harmonic projection of the Moyal residual is zero

- id: A230-02
  severity: 2
  status: valid-not-closed
  target: functorial homotopy
  finding: the Hodge homotopy is the right candidate, but Step 3 requires
    a proof that every potential left functional pairs correctly with the
    Moyal shear target
  residual: prove the potential identity or produce the first harmonic row

- id: A230-03
  severity: 3
  status: healed-finite
  target: total-degree 13 interior strip
  finding: exact kernel-correction solves vanish in all non-edge cases
  residual: finite evidence only; no all-bidegree theorem follows from it
```

## Remaining obligation

Prove the decorated-necklace left-cokernel theorem:
\[
  \lambda\mathcal C_{a,b}|_{\ker\partial}=0
  \Longrightarrow
  \lambda(R^{\mathrm{free}}_{a,b})=0
  \qquad(a,b\geq3).
\]
If it fails, record the first stable harmonic functional as the obstruction
theorem.  The next finite checks are \((4,12)\), \((7,7)\), and total
degree \(14\), but they are checks, not substitutes for the homotopy.
