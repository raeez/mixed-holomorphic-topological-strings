# Swarm 2026-04-30 Agent 333: BMK Source-Boundary Heal

Agent: 333.

Scope: BMK/Koppelman source-boundary patch only in `main.tex`,
`theorem-lanes.tex`, plus this report.  No radial, theta3, or LQT surface
was edited.

## Inputs Checked

- `CLAUDE.md`
- `AGENTS.md`
- `~/ecosystem/INVARIANTS.md`
- `~/ecosystem/AGENTS-HARNESS.md`
- `~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `reconstitution/swarm-2026-04-30-agent-330-primary-source-support-integration-verification.md`
- `reconstitution/primary-source-support-integration-verification-2026-04-30.md`
- `references/primary-sources/bmk-koppelman-source-anchors-2026-04-30.md`
- Current BMK windows in `main.tex` and `theorem-lanes.tex`

## Claim Attacked

BMK/Koppelman primary sources must not be read as proving the native
finite-window current theorem, the one-pair analytic pro-Matlis theorem,
or the six-entry all-window obstruction surface.

## Patch

- `main.tex`: the displayed \(K_{\mathrm{BM}}\) kernel now cites
  Laurent--Thi\'ebaut only for the pre-cutoff kernel and component
  \(\bar\partial\)-identity, and Ruppenthal only for the classical
  smooth-domain Koppelman homotopy formula.
- `main.tex`: the proof now states that the cutoff derivative, annular
  diagonal current, finite moments, and Matlis orientation are local
  checks.
- `main.tex`: the one-pair analytic quotient is explicitly local; its
  representative quotient, normalized contraction, and pro-Matlis moment
  map are not imported from BMK/Koppelman sources.
- `theorem-lanes.tex`: the lane-level kernel display carries the same
  source boundary, and the one-pair analytic pro-Matlis retract is marked
  as the manuscript's internal construction.
- `main.tex`: two bibliography entries were added for the exact modern
  anchors used by the patch.

## Boundary After Heal

External sources support:

- pre-cutoff BMK kernel;
- component \(\bar\partial\)-identity away from the diagonal;
- classical Koppelman homotopy formula on bounded \(C^1\) domains for
  \(C^1\) forms.

Internal theorem surface remains:

- cutoff-current limit \(H_\chi\);
- annular diagonal-current sign and scalar;
- finite moment projection \(p_N\);
- residue-current section \(i_N\);
- collar quotient and factorization compatibility;
- Hamiltonian/Matlis arity-two action;
- one-pair analytic pro-Matlis retract;
- six-entry all-window obstruction vector.

## Verification

`git diff --check -- main.tex theorem-lanes.tex` passed after the patch.
Because this report is new and untracked,
`git diff --check --no-index -- /dev/null reconstitution/swarm-2026-04-30-agent-333-bmk-source-boundary-heal.md`
was also run and produced no whitespace errors.
