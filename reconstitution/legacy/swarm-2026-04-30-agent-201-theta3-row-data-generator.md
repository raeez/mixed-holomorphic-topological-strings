# Finite-Window Theta3 Row-Data Generator

## Status

Current data remain obstructed.  The row array still has
\[
  K^0_{\theta_3,M}=0,\qquad
  K^1_{\theta_3,M}=\mathbb C E_{\theta_3},\qquad
  R_{\theta_3}=E_{\theta_3},
\]
so `theta_3_current_finite_row_subcomplex` has no primitive:
`primitive_exists=false`, obstruction covector `E_theta_3 -> 1`, and
obstruction value `1`.

Supplied primitive payloads are accepted only when the actual differential
entry `dC=-E` is present.  The accepted interface cases are not current
constructions; they are exact machine-checks for future supplied data.

## Changed Functions

- `theta3_common_finite_window_record`: records the fixed theta3 row,
  scalar-zero datum, inherited labels, and identity/zero truncation.
- `theta3_primitive_payloads`,
  `theta3_primitive_payload_check`,
  `theta3_primitive_payload_checks`: add CE-ancestor and local-counterterm
  payload constructors and validators.
- `theta3_support_data_verified`: verifies
  `d_CE eta_theta_3 = zeta_M_nu_3` for CE payloads and locality support for
  counterterm payloads.
- `theta3_transport_identity_verified`: verifies the finite-window
  `T A = A P` identity for the supplied primitive transport.
- `theta3_companion_face_payloads`,
  `theta3_companion_face_payload_check`,
  `theta3_companion_face_payload_checks`: represent absent, incomplete, and
  complete companion-face tables; complete tables must have zero signed
  residual, scalar-zero faces, supplied `v` truncation/cocycle data, and
  codimension-two closure.
- `primitive_search_results`: replaces the old generic
  `theta_3_with_supplied_candidate_C_theta_3` case with exact payload cases.
- `internal_consistency_checks`: makes the CLI fail if the current
  obstruction heals accidentally, if a missing-differential payload is
  accepted, or if the complete companion-face fixture stops validating.
- `main`: emits `theta_3_common_finite_window_record`,
  `theta_3_primitive_payload_checks`, and
  `theta_3_companion_face_payload_checks`.

## Case Decisions

```text
theta_3_current_finite_row_subcomplex          primitive_exists=false  obstruction=1
theta3_ce_ancestor_absent_payload              accepted=false
theta3_ce_ancestor_without_differential_entry  accepted=false
theta3_ce_ancestor_supplied_exact_payload      accepted=true   dC=-E
theta3_counterterm_absent_payload              accepted=false
theta3_counterterm_without_differential_entry  accepted=false
theta3_counterterm_supplied_exact_payload      accepted=true   dC=-E
theta3_companion_faces_incomplete_one_face     accepted=false  residual=E_theta_3
theta3_complete_companion_faces_supplied_exact_payload accepted=true
```

The companion-face accepted case is an interface payload only: it changes
the residual vector by a supplied complete face table.  It is not a
primitive and does not assert that the current manuscript already contains
the missing face `nu_i`.

## Commands Run

```bash
sed -n '1,220p' CLAUDE.md
sed -n '1,220p' /Users/raeez/topological-strings/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '1,220p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
git status --short
sed -n '129,170p' /Users/raeez/ecosystem/INVARIANTS.md
sed -n '143,170p' /Users/raeez/ecosystem/AGENTS-HARNESS.md
sed -n '1,360p' reconstitution/theta3-source-to-construction-spec-2026-04-30.md
sed -n '1,260p' main.tex
sed -n '1,260p' commands.tex
sed -n '1,260p' mathmacros.tex
sed -n '1,220p' notation.tex
sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-187-finite-window-qme-rows-0957.md
sed -n '1,280p' reconstitution/swarm-2026-04-30-agent-193-theta3-companion-primitive-search-0957.md
sed -n '1,320p' reconstitution/swarm-2026-04-30-agent-197-theta3-source-to-construction-spec.md
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py >/tmp/finite-window-agent201.json
python3 -m json.tool /tmp/finite-window-agent201.json
python3 scripts/finite_window_graph_array.py >/tmp/finite-window-agent201-final.json
python3 -m json.tool /tmp/finite-window-agent201-final.json >/tmp/finite-window-agent201-final.pretty.json
python3 - <<'PY'
from scripts.finite_window_graph_array import (
    primitive_search_results,
    theta3_companion_face_payload_checks,
    theta3_primitive_payload_checks,
)
for row in primitive_search_results():
    if row.case.startswith('theta'):
        print(row.case, row.primitive_exists,
              row.obstruction_value_on_residual,
              row.primitive_coefficients)
for row in theta3_primitive_payload_checks():
    print(row.case, row.accepted,
          row.support_data_verified,
          row.differential_entry_value,
          row.missing_fields)
for row in theta3_companion_face_payload_checks():
    print(row.case, row.accepted,
          row.residual_zero_verified,
          row.missing_fields)
PY
git diff --check -- scripts/finite_window_graph_array.py
git diff --check -- scripts/finite_window_graph_array.py reconstitution/swarm-2026-04-30-agent-201-theta3-row-data-generator.md
```

`py_compile`, full JSON emission, JSON parsing, focused case inspection,
and `git diff --check` all passed.

No TeX file was edited.
