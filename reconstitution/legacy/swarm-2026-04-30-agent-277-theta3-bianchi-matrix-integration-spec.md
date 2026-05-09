# Agent 277 - Theta3 Bianchi Matrix Integration Spec

Status: report-only.  No TeX, script, figure, build artifact, bibliography,
or source fixture was edited.  No PDF build was run.

Companion specification:

- `reconstitution/theta3-bianchi-matrix-integration-spec-2026-04-30.md`

## Claim Integrated

Agent 270 proves a sharper obstruction for the lower-window theta3 repair.
The source-coordinate primitive
\[
  D^2_{02,20}
  =
  K^2_{\Theta_3}(u_{a,H_{1,0}}u_{b,H_{0,1}})
\]
is a genuine source primitive because
\[
  d_{\mathrm{CE}}(u_{a,H_{1,0}}u_{b,H_{0,1}})
  =
  2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}}.
\]
It is not a genuine local-functional primitive in the present data-derived
habitat.  The missing datum is exactly the Hom-valued Bianchi row
\[
  \mathfrak b^2_{02,20}
  =
  d_{\mathrm{ns},2}K^2_{\Theta_3}(u_{a,H_{1,0}}u_{b,H_{0,1}})
  -
  K^2_{\Theta_3}\!\left(
    d_{\mathrm{CE}}(u_{a,H_{1,0}}u_{b,H_{0,1}})
  \right).
\]

In the Bianchi-exposed basis
\[
  (E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20}),
\]
the matrix data are
\[
  A_D^2=(-2,2,1)^T,\qquad r_2=(2,-2,0)^T.
\]
The equation \(A_D^2c=-r_2\) is inconsistent.  The cokernel
\[
  \widetilde\lambda_{02,\mathfrak b}
  =
  \frac12(E^2_{\nu_{02}})^*
  +(\mathfrak b^2_{02,20})^*
\]
satisfies
\[
  \widetilde\lambda_{02,\mathfrak b}A_D^2=0,\qquad
  \widetilde\lambda_{02,\mathfrak b}(r_2)=1.
\]

This replaces the weaker lower-row statement "the source primitive kills the
transported residual if the Bianchi defect vanishes" with the exact
Bianchi-exposed obstruction theorem: the route is source-exact but not
local-functional-exact unless \(\mathfrak b^2_{02,20}\) is killed.

## Manuscript Targets

The exact integration spec is in the companion file.  Required targets:

- `main.tex`: strengthen `prop:theta-three-finite-window-acceptance-gate`
  near `main.tex:8450-8472`, and add the matrix/cokernel proof paragraph
  near `main.tex:8487-8500`.
- `theorem-lanes.tex`: replace the lower primitive paragraph near
  `theorem-lanes.tex:3370-3391` with the source-exact versus
  local-functional-exact lane statement.
- `open-obligations.tex`: replace the lower primitive tail near
  `open-obligations.tex:821-832`, add the Bianchi transport gate, and keep
  \(\lambda^{(2)}_{\nu_{02}}\) only as the empty primitive-slot certificate.
- `claim-strength-ledger.tex`: update the theta3 primitive item near
  `claim-strength-ledger.tex:459-474` and the model-case paragraph near
  `claim-strength-ledger.tex:816-835`.

## Distinction To Preserve

Source exactness:
\[
  d_{\mathrm{CE}}\zeta^0_2
  =
  2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}}.
\]

Local-functional exactness:
\[
  d_{\mathrm{ns},2}P^2_{02,20}
  =
  -2E^2_{\nu_{02}}+2E^2_{\nu_{20}}
\]
for a scalar-zero local functional \(P^2_{02,20}\), with locality or
wavefront admissibility and compatible transport.  The current candidate
has
\[
  d_{\mathrm{ns},2}D^2_{02,20}
  =
  -2E^2_{\nu_{02}}+2E^2_{\nu_{20}}
  +\mathfrak b^2_{02,20}.
\]
Thus \(P^2_{02,20}=D^2_{02,20}\) is valid only after the Bianchi row is
zero.  Otherwise the repair must add \(B^2_{02,20}\) with
\[
  d_{\mathrm{ns},2}B^2_{02,20}=-\mathfrak b^2_{02,20},
\]
or supply a marked non-diagonal transport/codimension-two table.

For towers, the primitive compatibility condition must include
\[
  d_{\mathrm{ns},N}(\pi_{M,N}D^M-D^N)
  =
  \pi_{M,N}\mathfrak b^M_{\mathrm{cand}}
  -\mathfrak b^N_{\mathrm{cand}}.
\]
Without strict transport of the Bianchi defects, or an explicit boundary
for the displayed right side, the Roos primitive class is not closed.

## Attack-Heal Outcome

Valid attack: previous manuscript-facing language risked treating
source-exactness as evidence for a local-functional counterterm.  This is
false in the Bianchi-exposed row complex.

Heal: the report gives exact insertion/replacement blocks that preserve the
strong theorem surface.  The theta3 row is not downgraded.  It becomes an
exact obstruction theorem with named repair data:

1. prove \(\mathfrak b^2_{02,20}=0\), with scalar-zero and transport checks;
2. construct \(B^2_{02,20}\) with
   \(d_{\mathrm{ns},2}B^2_{02,20}=-\mathfrak b^2_{02,20}\), scalar-zero
   value, locality or wavefront admissibility, and compatible transport;
3. construct marked non-diagonal transport satisfying
   \[
     3v_3+2v_4-v_5+v_6-2v_7-3v_8=(-2,2)^T,
   \]
   with projected renormalized weights, lower row-basis reduction, and
   codimension-two closure.

## Verification

Read:

- `CLAUDE.md`
- `AGENTS.md`
- `~/ecosystem/INVARIANTS.md`
- `~/ecosystem/AGENTS-HARNESS.md`
- `~/topological-strings/.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `reconstitution/swarm-2026-04-30-agent-270-theta3-bianchi-defect-closure-push.md`
- `reconstitution/theta3-bianchi-defect-closure-push-2026-04-30.md`
- current anchors in `main.tex`, `theorem-lanes.tex`,
  `open-obligations.tex`, and `claim-strength-ledger.tex`

Matrix verification command output:

```text
A_D= [-2, 2, 1]
r= [2, -2, 0]
ellA= 0
ellr= 1
coordinate_forced_c= [1, 1, 0]
residual_after_c1= [0, 0, 1]
```

Status of the current checkout: many pre-existing staged and modified swarm
files are present.  This agent owns and stages only:

- `reconstitution/swarm-2026-04-30-agent-277-theta3-bianchi-matrix-integration-spec.md`
- `reconstitution/theta3-bianchi-matrix-integration-spec-2026-04-30.md`
