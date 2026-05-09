# Agent 296: radial structural Hodge/PBW proof mechanism

Date: 2026-04-30.

Owned write paths:

- `reconstitution/radial-structural-hodge-proof-mechanism-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-296-radial-structural-hodge-proof-mechanism.md`

No TeX or script file was edited.

## Loaded Context

Read `CLAUDE.md`, `AGENTS.md`, `~/ecosystem/INVARIANTS.md`,
`~/ecosystem/AGENTS-HARNESS.md`, the local `chriss-ginzburg-rectify` skill,
and the delegated Vol II rectification skill.  Read the named radial reports,
the radial appendix, theorem-lane and open-obligation radial rows,
claim-ledger radial rows, and the radial/Weyl scripts.

The checkout is heavily dirty from concurrent agents.  I did not revert,
overwrite, stage, or edit any path outside the two owned reports.

## Claim Attacked

The target was the all-bidegree dual-potential identity
\[
  \lambda(E^+_{a,b})=\phi_\lambda(T_{a,b})
\]
for every decorated row satisfying
\[
  \lambda C^+_{a,b}(W)=\phi_\lambda(\partial W).
\]
The requested route was structural Hodge/PBW/telescoping, not bounded
enumeration.

## Result

Status: all-bidegree proof not closed; exact structural obstruction theorem
sharpened.

The proved structural part is the ordinary cycle mechanism.  Based binary
words form the distributive-lattice cube complex of the rectangle
\([a]\times[b]\); adjacent swaps are one-cells and commuting adjacent swaps
give square cells.  After rational cyclic quotient, transfer gives
\[
  H_1(C^\square_\bullet(a,b);\mathbb Q)=0,
\]
so \(\partial_2:C^\square_2(a,b)\to\ker\partial\) is onto.  Hence every
kernel correction can be written as a square-cell transgression
\[
  K_{a,b}=\partial_2H_{a,b}.
\]

Define
\[
  D^\square_{a,b}=C^+_{a,b}\partial_2:
  C^\square_2(a,b)\to\mathsf D^+_{a,b}.
\]
Then the exact obstruction is
\[
  [R^{\mathrm{free}}_{a,b}]\in\operatorname{coker}D^\square_{a,b},
\]
or equivalently the harmonic projection for
\[
  \Delta^\square_{a,b}
  =
  D^\square_{a,b}(D^\square_{a,b})^*.
\]

The missing theorem is the decorated PBW Stokes identity: every
\(\lambda\) with \(\lambda D^\square_{a,b}=0\) must satisfy
\(\lambda(R^{\mathrm{free}}_{a,b})=0\).  This was not proved.  The block is
PBW-decorated, not topological: contractions may identify nonadjacent
vertices and split traces, and no all-bidegree square-cell weight formula was
constructed.

## Exact Failure Criterion

If the all-bidegree theorem fails in bidegree \((a,b)\), the obstruction is
a functional
\[
  \lambda\in\ker(D^\square_{a,b})^*
\]
with
\[
  \lambda(R^{\mathrm{free}}_{a,b})\ne0.
\]
Equivalently, it is a signed row
\[
  (\phi,-\lambda)\in\ker B_{a,b}^*
\]
with
\[
  \lambda(E^+_{a,b})-\phi(T_{a,b})\ne0.
\]
After rescaling, the obstruction value can be normalized to `1`.  No such
row appeared in the bounded computations checked in this pass or in the
named prior reports.

## Computations Run

All Python commands used `PYTHONDONTWRITEBYTECODE=1` and `python3 -B`.

- `py_compile` on the four radial/Moyal scripts: exit code `0`.
- `scripts/check_moyal_coefficients.py`: all checks passed; Moyal sweep
  covered `14641` monomial pairs through order `11`; Capelli round-trip
  covered `121` monomials; direct `N=2` and `N=3` radial restrictions each
  checked `80` pairs.
- `scripts/quantum_shear_trace_diagram_normal_form.py --self-test ... --case
  4,4 --classical-only`: self-test passed, and the classical-only row failed
  with the known four-term \(43/7\) residual.
- `scripts/quantum_shear_trace_diagram_normal_form.py --case 4,4 --case 5,5
  --kernel-correction`: both rows passed with corrected residual zero;
  supports were `4` and `16`.

## Insertion Recommendation

Insert the square-cell refinement after the potential-form remark in
`appendix-radial-parts-moyal.tex`, then reference
\(D^\square_{a,b}=C^+_{a,b}\partial_2\) in the theorem lane and
open-obligation radial rows.  Do not claim all-bidegree vanishing until the
decorated PBW Stokes identity is proved or a normalized obstruction row is
exhibited.

Files changed:

- `reconstitution/radial-structural-hodge-proof-mechanism-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-296-radial-structural-hodge-proof-mechanism.md`
