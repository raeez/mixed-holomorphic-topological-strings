# Agent 337: open-obligations radial heal

Date: 2026-04-30.

Owned write paths:

- `open-obligations.tex`
- `reconstitution/swarm-2026-04-30-agent-337-open-obligations-radial-heal.md`

## Claim attacked

`open-obligations.tex` still presented the radial/Weyl obligation through
the stale uniform-homotopy/free-normal-diagram surface.  The accepted
surface is
\[
  \Omega^{\mathrm{rad}}_{a,b}
  =
  [(T_{a,b},E^+_{a,b})]\in\operatorname{coker}B_{a,b},
  \qquad
  B_{a,b}(W)=(\partial W,C^+_{a,b}(W)).
\]
It vanishes exactly when the decorated PBW Stokes problem closes, written
in the square-cell model as
\[
  D^\square_{a,b}H_{a,b}=R^{\mathrm{free}}_{a,b},
  \qquad
  D^\square_{a,b}=C^+_{a,b}\partial_2 .
\]
Failure is a signed dual row
\[
  (\phi,-\lambda)\in\ker B_{a,b}^*
  \quad\text{with}\quad
  \lambda(E^+_{a,b})-\phi(T_{a,b})\ne0.
\]

## Patch

The componentwise summary now names the radial/Weyl
dual-potential decorated-Stokes gate.

The radial/Weyl obligation item now puts \(B_{a,b}\), \(\eta_{a,b}\),
\(\Omega^{\mathrm{rad}}_{a,b}\), the decorated PBW Stokes equation, and
the signed-row criterion before the subordinate
\(\mathcal C_{a,b}\) certificate model.

The finite-certificate paragraph records the current total-degree \(14\)
frontier:
\[
  (6,8),(8,6),(7,7).
\]
These are timeout/frontier computations in the current basis.  No
obstruction row is known.  Nonzero corrections at \((5,5)\) and \((6,6)\)
are stated as corrections, not obstructions.

The source-firewall layout region near `open-obligations.tex:1230`,
owned by Agent 334, was read for concurrency awareness and not edited.

## Files read

- `CLAUDE.md`
- `~/ecosystem/INVARIANTS.md`
- `~/ecosystem/AGENTS-HARNESS.md`
- `~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `main.tex`
- `preamble.tex`
- `commands.tex`
- `mathmacros.tex`
- `notation.tex`
- `open-obligations.tex`
- `reconstitution/radial-summary-afterpatch-verification-2026-04-30.md`
- `reconstitution/radial-decorated-stokes-computational-frontier-audit-2026-04-30.md`
- `reconstitution/radial-dual-potential-identity-construction-push-2026-04-30.md`

## Verification

Commands:

```text
git diff --check -- open-obligations.tex
git diff --no-index --check -- /dev/null \
  reconstitution/swarm-2026-04-30-agent-337-open-obligations-radial-heal.md
```

Result: no whitespace warnings.  The tracked-file check returned clean;
the `--no-index` report-file check emitted no warnings, with the ordinary
nonzero diff status for comparing `/dev/null` to an added file.

No build was run; the assignment requested the targeted diff check.
