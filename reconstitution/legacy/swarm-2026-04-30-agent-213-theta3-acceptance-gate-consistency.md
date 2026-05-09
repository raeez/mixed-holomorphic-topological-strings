# Agent 213 - Theta3 Acceptance-Gate Consistency

Status: report-only audit.  No TeX or script files were edited.  The working
tree was concurrent; anchors below refer to the working tree observed during
this audit.

## Claim Status

The shared theta row is
\[
  d_{\mathrm{CE}}\zeta_M=+\zeta_{M,\nu_3}+\cdots,\qquad
  \mathsf E_{\theta_3,M}
    =
  -K^M_{\Theta_3}(\zeta_{M,\nu_3}),
  \qquad
  \widehat\sigma_{\mathrm{sc},M}(\mathsf E_{\theta_3,M})=0.
\]
The current one-row finite complex has no primitive:
\[
  K^0_{\theta_3,M}=0,\qquad
  K^1_{\theta_3,M}=\mathbb C\mathsf E_{\theta_3,M},\qquad
  r^M=(1),\qquad
  \ell_{\theta_3}(\mathsf E_{\theta_3,M})=1.
\]

## Findings

1. Notation repair required in `main.tex`.

   `main.tex:8113` and `main.tex:8128` use
   \(\zeta_{\nu_3,M}\).  Tate, the script, Agent 197, and Agent 207 use
   \(\zeta_{M,\nu_3}\).  Exact repair:

   ```tex
   \zeta_{\nu_3,M} -> \zeta_{M,\nu_3}
   ```

2. Companion-face validator gap.

   `scripts/finite_window_graph_array.py:1323-1328` sums only
   `face.residual_coordinates`; it does not check `face.ce_coefficient`.
   An adversarial payload with `ce_coefficient=99` but cancelling signed
   residual coordinates was accepted.  Exact repair: add
   `signed_coordinates_verified_from_ce_coefficients` to
   `Theta3CompanionFacePayload`, require it in
   `theta3_companion_face_payload_check`, and report
   `CE coefficients matched to signed residual coordinates` when absent.

## Consistency Checks

- \(A^M c=-r^M\) and \(A^M_{\theta_3,C}=-1\) agree: with
  \(\rho^M_1=\mathsf E_{\theta_3,M}\), \(r^M=(1)\), the coefficient
  \(-1\) and \(c_M=1\) solve the finite-row equation.
- Primitive payloads require \(d_{\mathrm{ns},M}C_{\theta_3,M}
  =-\mathsf E_{\theta_3,M}\), scalar projection zero, \(T A=A P\), and zero
  Roos class.
- A complete companion-face table is not a primitive.  It cancels before the
  primitive search by replacing the one-face residual with the full signed
  CE-source-face sum.  No primitive Roos class is formed.

## Validator Output

```text
common_row E_theta_3=-K^M_{Theta_3}(zeta_{M,nu_3})
theta_3_current_finite_row_subcomplex False 1 []
theta3_ce_ancestor_without_differential_entry False 0 False True True True
theta3_ce_ancestor_supplied_exact_payload True -1 True True True True
theta3_counterterm_without_differential_entry False 0 False True True True
theta3_counterterm_supplied_exact_payload True -1 True True True True
theta3_companion_faces_incomplete_one_face False [['E_theta_3', '1']] not reached
theta3_complete_companion_faces_supplied_exact_payload True [] primitive Roos class is not formed; source-face tower compatibility is represented by the supplied v-cocycle
agent213_malformed_ce_coefficient_same_signed_coordinates accepted= True residual= () missing= ()
```

## Commands Run

```bash
sed -n '1,220p' CLAUDE.md
sed -n '1,260p' AGENTS.md
sed -n '1,240p' /Users/raeez/topological-strings/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '1,260p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '1,220p' /Users/raeez/ecosystem/INVARIANTS.md
sed -n '1,260p' /Users/raeez/ecosystem/AGENTS-HARNESS.md
git status --short
rg -n -F -e 'zeta_{\nu_3,M}' -e 'zeta_{M,\nu_3}' -e 'zeta_M_nu_3' main.tex tate-P1-hadamard-mittag-leffler.tex scripts/finite_window_graph_array.py reconstitution/theta3-source-to-construction-spec-2026-04-30.md reconstitution/swarm-2026-04-30-agent-197-theta3-source-to-construction-spec.md reconstitution/swarm-2026-04-30-agent-201-theta3-row-data-generator.md reconstitution/swarm-2026-04-30-agent-207-theta3-validator-manuscript-integration.md
rg -n -F -e '-K^M_{\Theta_3}(\zeta' -e 'd_{\mathrm{CE}}\eta_{\theta_3,M}' -e 'd_{\mathrm{ns},M}C' -e 'A^M_{\theta_3,C}=-1' -e 'A^M c=-r^M' -e 'TA=AP' -e 'T A=A P' -e 'primitive Roos class is not formed' -e 'not a primitive' main.tex tate-P1-hadamard-mittag-leffler.tex scripts/finite_window_graph_array.py reconstitution/swarm-2026-04-30-agent-197-theta3-source-to-construction-spec.md reconstitution/swarm-2026-04-30-agent-201-theta3-row-data-generator.md reconstitution/swarm-2026-04-30-agent-207-theta3-validator-manuscript-integration.md
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py
```

Primary report:
`reconstitution/theta3-acceptance-gate-consistency-2026-04-30.md`.
