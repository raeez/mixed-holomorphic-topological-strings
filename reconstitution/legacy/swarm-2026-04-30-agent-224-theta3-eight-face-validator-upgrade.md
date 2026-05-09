# Agent 224 - Theta3 Eight-Face Validator Upgrade

Status: implemented in `scripts/finite_window_graph_array.py`.  No TeX,
manuscript, or control files were edited.

## Stable Core

The primitive gates are unchanged.  The CE-ancestor and local-counterterm
fixtures are accepted only when the supplied degree-zero row has
`dC=-E_theta_3`, scalar projection zero, identity/zero transport satisfying
`T A = A P`, and zero Roos class.  Payloads without the differential entry
still reject.

The companion-face gate is stricter.  A source-algebraic residual table is
not a theorem-grade Costello cancellation until it also supplies the marked
incidence/weight table, codimension-two closure, and lower-window transport
cancellation.

## Eight-Face Obstruction Recorded

The validator now records the Agent 215/221 candidate residual
\[
  R_{\Theta_3,M}^{\mathrm{cand}}
  =
  2E_{\nu_{02}}-2E_{\nu_{20}}+3E_{\nu_{03}}
  +2E_{\nu_{12}^{(1)}}-E_{\nu_{12}^{(2)}}
  +E_{\theta_3}-2E_{\nu_{21}^{(2)}}-3E_{\nu_{30}} .
\]
Its scalar coefficient sum is zero, but its row-vector residual is nonzero
in the declared basis.  The validator therefore rejects it as a cancellation
theorem.

The diagonal source-face transport is recorded as
`v^{M,N}_{nu;nu'}=1` for `nu=nu'` and `degree(nu)<=N`, otherwise zero.  Its
cocycle identity is accepted.  Its `N=2` projection is explicitly recorded
as
\[
  2E_{\nu_{02}}^2-2E_{\nu_{20}}^2,
\]
so the missing lower-window identity is exactly
`E^2_nu02=E^2_nu20` in the chosen row basis, or a recomputed lower-window
presentation.

The missing marked Costello datum is recorded as:

- labelled `d_CE zeta_M` with the `B_theta`, `a`, and `b` current labels;
- Costello orientation/Koszul signs `epsilon^CE_{Theta_3,nu}`;
- renormalized weights `K^M_{Theta_3}(zeta_{M,nu})` in one row basis;
- marked output graph and marker transport `mu_nu` for every face;
- basis-reduced `v^{M,N}_{nu;nu'}` projection coordinates;
- codimension-two incidence table `C^{(2)}_{nu,nu'}`.

## Validator Decisions

- `theta3_eight_face_candidate_source_algebraic_obstruction`: rejected,
  eight faces recorded, exact residual and `N=2` obstruction recorded.
- `theta3_complete_companion_faces_supplied_exact_payload`: now rejected;
  a syntactic zero residual is insufficient without the marked Costello
  incidence/weight table and lower-window cancellation.
- `theta3_ce_ancestor_supplied_exact_payload`: still accepted.
- `theta3_counterterm_supplied_exact_payload`: still accepted.

## Verification

Commands run:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py >/tmp/finite-window-agent224.json
python3 -m json.tool /tmp/finite-window-agent224.json >/tmp/finite-window-agent224.pretty.json
python3 - <<'PY'
import json
with open('/tmp/finite-window-agent224.json') as f:
    data = json.load(f)
print('primitive payloads')
for row in data['theta_3_primitive_payload_checks']:
    if row['case'] in {
        'theta3_ce_ancestor_supplied_exact_payload',
        'theta3_counterterm_supplied_exact_payload',
        'theta3_ce_ancestor_without_differential_entry',
        'theta3_counterterm_without_differential_entry',
    }:
        print(row['case'], row['accepted'], row['differential_entry_value'])
print('companion payloads')
for row in data['theta_3_companion_face_payload_checks']:
    if row['case'].startswith('theta3_eight') or row['case'].startswith('theta3_complete'):
        print(row['case'], row['accepted'], row['face_count'], row['missing_fields'])
check = data['theta_3_eight_face_candidate_obstruction_check']
print('eight_face', check['accepted'], check['face_count'], check['candidate_residual_coefficient_sum'])
print('n2', check['diagonal_v_transport']['n_2_residual_vector'])
print('missing_table', check['marked_costello_table']['codimension_two_closure_supplied'])
PY
git diff --check -- scripts/finite_window_graph_array.py
```

The focused JSON inspection returned:

```text
theta3_ce_ancestor_without_differential_entry False 0
theta3_ce_ancestor_supplied_exact_payload True -1
theta3_counterterm_without_differential_entry False 0
theta3_counterterm_supplied_exact_payload True -1
theta3_eight_face_candidate_source_algebraic_obstruction False 8 [...]
theta3_complete_companion_faces_supplied_exact_payload False 2 [...]
eight_face False 8 0
n2 [['E_nu02', '2'], ['E_nu20', '-2']]
missing_table False
```

`py_compile`, JSON emission, JSON parsing, focused gate inspection, and
`git diff --check` passed.

## Files Changed

- `scripts/finite_window_graph_array.py`
- `reconstitution/swarm-2026-04-30-agent-224-theta3-eight-face-validator-upgrade.md`
