# Theta3 Acceptance-Gate Consistency Audit

Status: report-only audit.  No TeX or script files were edited.

## Verdict

The main theorem form is consistent on the sign of the theta row, the
linear-system gate, the scalar-zero condition, the primitive Roos gate, and
the companion-face/non-primitive distinction.  Two repairs are needed for
strict acceptance-gate consistency.

## Findings

1. `main.tex` uses the reversed source-face index order.

   Current anchors:

   - `main.tex:8113`: `-K^M_{\Theta_3}(\zeta_{\nu_3,M})`
   - `main.tex:8128`: `d_{\mathrm{CE}}\eta_{\theta_3,M}=\zeta_{\nu_3,M}`

   The Tate theorem, script, and reports use the window-first convention:

   - `tate-P1-hadamard-mittag-leffler.tex:1949`: `+\zeta_{M,\nu_3}`
   - `tate-P1-hadamard-mittag-leffler.tex:1965`: `-K^M_{\Theta_3}(\zeta_{M,\nu_3})`
   - `tate-P1-hadamard-mittag-leffler.tex:2103`: `d_{\mathrm{CE}}\eta_{\theta_3,M}=\zeta_{M,\nu_3}`
   - `scripts/finite_window_graph_array.py:989`: `E_theta_3=-K^M_{Theta_3}(zeta_{M,nu_3})`
   - `scripts/finite_window_graph_array.py:1045`, `1060`, `1165`: `zeta_M_nu_3`
   - Agent 197: `reconstitution/swarm-2026-04-30-agent-197-theta3-source-to-construction-spec.md:13`, `49`
   - Agent 207: `reconstitution/swarm-2026-04-30-agent-207-theta3-validator-manuscript-integration.md:9`

   Exact repair:

   ```tex
   \zeta_{\nu_3,M} -> \zeta_{M,\nu_3}
   ```

   at `main.tex:8113` and `main.tex:8128`.

2. The companion-face validator stores `ce_coefficient` but does not enforce
   it in the residual cancellation check.

   Anchors:

   - `scripts/finite_window_graph_array.py:234-237`: `Theta3CompanionFace` has
     `ce_coefficient` and `residual_coordinates`.
   - `scripts/finite_window_graph_array.py:1323-1328`: `coordinate_entries`
     are formed only from `face.residual_coordinates`.
   - `scripts/finite_window_graph_array.py:1329-1363`: acceptance depends on
     the resulting residual vector, scalar gates, `v` data, and closure table.

   Hostile probe run in this audit:

   ```text
   agent213_malformed_ce_coefficient_same_signed_coordinates accepted= True residual= () missing= ()
   ```

   Thus a malformed table with `ce_coefficient=99` on both faces but cancelling
   signed residual coordinates still passes.  This is not a contradiction in
   the present theorem payload if `residual_coordinates` are declared to be
   already signed CE residual coordinates.  It is a validator/theorem wording
   gap, because the Tate proposition says every CE coefficient is part of the
   accepted complete table.

   Exact repair for theorem-grade validation: add a payload-level field
   `signed_coordinates_verified_from_ce_coefficients: bool`, require it in
   `theta3_companion_face_payload_check`, and set it true only for a complete
   table whose signed residual coordinates have been computed from the listed
   CE coefficients.  The missing-fields list should include
   `CE coefficients matched to signed residual coordinates` when false.

## Consistent Gates

- Sign.  The shared sign is
  \[
    d_{\mathrm{CE}}\zeta_M=+\zeta_{M,\nu_3}+\cdots,\qquad
    \mathsf E_{\theta_3,M}=-K^M_{\Theta_3}(\zeta_{M,\nu_3}).
  \]
  It comes from the curvature summand
  \(-\kappa^M_{\mathcal G,w,I}(d_{\mathrm{CE}}\zeta_M)\).

- Primitive equation.  With ordered residual row
  \(\rho^M_1=\mathsf E_{\theta_3,M}\) and \(r^M=(1)\), the finite-row search is
  \[
    A^M c=-r^M.
  \]
  A supplied primitive is accepted exactly when its column has
  \[
    A^M_{\theta_3,C}=-1,\qquad
    d_{\mathrm{ns},M}C_{\theta_3,M}=-\mathsf E_{\theta_3,M},
    \qquad c_M=1.
  \]

- Scalar gate.  The row has
  \[
    \widehat\sigma_{\mathrm{sc},M}(\mathsf E_{\theta_3,M})=0.
  \]
  Primitive payloads also require scalar projection zero.

- Roos gate.  Primitive payloads require
  \[
    T^{M,N}A^M=A^N P^{M,N},\qquad [P^{M,N}c_M-c_N]=0.
  \]
  For the accepted identity/zero transport fixtures the Roos class is zero.

- Companion-face gate.  A complete companion-face table is not a primitive.
  It replaces the residual by the full signed CE source-face sum and is
  accepted only when that signed sum, every scalar gate, the \(v^{M,N}\)
  cocycle, and codimension-two closure data are supplied.  No primitive Roos
  class is formed in this case.

## Shared Theorem Form

For \(M\ge 3\), the current theta row is a closed scalar-zero one-row
finite-window obstruction:
\[
  \mathcal K^0_{\theta_3,M}=0,\qquad
  \mathcal K^1_{\theta_3,M}=\mathbb C\mathsf E_{\theta_3,M},\qquad
  d=0,\qquad
  \mathsf E_{\theta_3,M}=-K^M_{\Theta_3}(\zeta_{M,\nu_3}).
\]
The covector \(\ell_{\theta_3}(\mathsf E_{\theta_3,M})=1\) certifies the
current fixed-window obstruction.  The obstruction is killed only by a
supplied CE ancestor, a supplied local counterterm primitive, or a complete
companion-face table satisfying the gates above.

## Commands

```bash
rg -n -F -e 'theta-three-finite-window-acceptance-gate' -e 'theta-three-payload-acceptance-gate' -e 'E_{\theta_3' -e 'E_\theta_3' -e 'zeta_{\nu_3,M}' -e 'zeta_{M,\nu_3}' -e 'zeta_M_nu_3' -e 'A^M c=-r^M' -e 'A^M_{\theta_3,C}=-1' -e 'scalar-zero' -e 'Roos' -e 'companion-face' -e 'not a primitive' main.tex tate-P1-hadamard-mittag-leffler.tex scripts/finite_window_graph_array.py reconstitution/swarm-2026-04-30-agent-197-theta3-source-to-construction-spec.md reconstitution/swarm-2026-04-30-agent-201-theta3-row-data-generator.md reconstitution/swarm-2026-04-30-agent-207-theta3-validator-manuscript-integration.md
python3 -m py_compile scripts/finite_window_graph_array.py
python3 - <<'PY'
import json
import subprocess

completed = subprocess.run(
    ['python3', 'scripts/finite_window_graph_array.py'],
    check=True,
    capture_output=True,
    text=True,
)
payload = json.loads(completed.stdout)
print(payload['theta_3_common_finite_window_record']['row_value'])
for row in payload['theta_3_primitive_payload_checks']:
    print(row['case'], row['accepted'], row['differential_entry_value'])
for row in payload['theta_3_companion_face_payload_checks']:
    print(row['case'], row['accepted'], row['residual_vector'])
PY
```
