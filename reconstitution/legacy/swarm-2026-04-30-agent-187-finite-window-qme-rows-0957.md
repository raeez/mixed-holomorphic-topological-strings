# Agent 187 - Finite-Window QME Rows, 09:57 Refresh

Status: patched and staged owned surfaces; no commits or pushes.

## Stable Core

The finite-window non-scalar QME row machinery now has an executable
primitive-search interface.  After the scalar gate vanishes, a finite row
array supplies:

- a degree-one row presentation \(\rho_i\) containing graph differentials,
  CE-source faces, nonzero bracket rows, and lower counterterm rows;
- a degree-zero candidate counterterm presentation \(\eta_j\);
- the boundary matrix \(A_{ij}\) defined by
  \(d_{\mathrm{ns}}\eta_j=\sum_i A_{ij}\rho_i\);
- a residual vector \(r_i\) with \(R=\sum_i r_i\rho_i\);
- truncation blocks \(T^{M,N}\): identity/zero for computed rows, \(u\) for
  genuine seed rows, \(v\) for CE-source faces, and \(q\) for nonzero bracket
  rows.

The fixed-window counterterm criterion is the linear system
\[
  A^M c=-r^M.
\]
If no solution exists, a left-null covector
\(\ell A^M=0\), \(\ell(r^M)\neq0\) is a certificate for a nonzero finite-row
\(H^1\)-class.  If windowwise solutions exist, compatibility is the Roos
\(\varprojlim^1\) class represented by
\[
  [P^{M,N}c_M-c_N]\in H^0(\mathcal K^\bullet_{\mathrm{ns},N}(I)).
\]

For the current one-row \(\theta_3\) package the supplied finite row complex is
\[
  \mathcal K^0_{\theta_3,M}=0,\qquad
  \mathcal K^1_{\theta_3,M}=\C\mathsf E_{\theta_3,M},\qquad d=0.
\]
The scalar gate is zero, but the primitive-search matrix is \(1\times0\) and
the residual is the basis vector.  The covector
\(\ell_{\theta_3}(\mathsf E_{\theta_3,M})=1\) certifies
\[
  [\mathsf E_{\theta_3,M}]\neq0
  \quad\text{in the displayed finite row subcomplex.}
\]
This is exact for the finite subcomplex supplied by the row array.  It does
not rule out a primitive in a larger local-functional complex; such a
primitive must be supplied as an additional degree-zero row or replaced by
Hom-valued companion rows that change the residual vector.

## Valid Attacks

```yaml
- id: A1-187-01
  severity: 1
  status: healed
  lens: counterterm criterion
  target: finite-window row machinery
  claim: The row array names the obstruction once the scalar gate vanishes.
  broken_step: A scalar-zero row sum is only a cochain until a primitive search space and boundary matrix are supplied.
  evidence_type: proof_gap
  evidence_ref: prop:finite-row-primitive-search-interface
  minimal_heal: Add the finite linear system A c=-r and cokernel-covector certificate.
  residual: Full local-functional primitives outside the supplied finite row complex remain open.

- id: A1-187-02
  severity: 1
  status: healed
  lens: theta_3 obstruction
  target: prop:concrete-order-three-larger-package-row
  claim: No primitive is supplied, so theta_3 is merely symbolic.
  broken_step: In the displayed one-row finite complex, absence of degree-zero candidates is enough to prove a finite-row obstruction.
  evidence_type: proof
  evidence_ref: prop:theta-three-finite-row-obstruction
  minimal_heal: Add K^0=0, K^1=C E_theta3, the covector ell(E)=1, and the nonzero H^1 conclusion.
  residual: Actual Costello weight, closure proof from the Hom-valued Bianchi identity, and larger-complex primitive remain unsupplied.

- id: A1-187-03
  severity: 2
  status: healed
  lens: truncation and Roos compatibility
  target: u/v/q row tower
  claim: Fixed-window solvability is enough for a compatible counterterm tower.
  broken_step: Windowwise primitives can fail to commute with truncation even after fixed-window H^1 vanishes.
  evidence_type: proof_gap
  evidence_ref: prop:finite-row-primitive-search-interface
  minimal_heal: Add T r=r, T A=A P, and the Roos class [P c_M-c_N].
  residual: For future nonidentity primitives, H^0 tower and primitive transport matrices P^{M,N} must be supplied.

- id: A1-187-04
  severity: 2
  status: healed
  lens: script executability
  target: scripts/finite_window_graph_array.py
  claim: The script emits row labels but cannot decide primitive existence.
  broken_step: No executable linear algebra formed A, r, a primitive solution, or an obstruction covector.
  evidence_type: failing_interface
  evidence_ref: finite_row_primitive_search_results JSON key
  minimal_heal: Add rational RREF search, primitive solutions, and left-null obstruction certificates.
  residual: Numeric entries for genuine Costello graph packages still require actual row values and coordinate matrices.
```

## Script Decisions

Command:

```bash
python3 scripts/finite_window_graph_array.py
```

Decisive primitive-search rows:

```text
minimal_full_equivariant_order_2_zero:
  primitive_exists = true
  obstruction_value_on_residual = 0

theta_3_current_finite_row_subcomplex:
  primitive_exists = false
  obstruction_covector = E_theta_3 -> 1
  obstruction_value_on_residual = 1

theta_3_with_supplied_candidate_C_theta_3:
  primitive_exists = true
  primitive_coefficients = C_theta_3 -> 1
```

## Verification

Commands run:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py >/tmp/finite-window-agent187.json
python3 -m json.tool /tmp/finite-window-agent187.json >/tmp/finite-window-agent187.pretty.json
python3 - <<'PY'
import json
with open('/tmp/finite-window-agent187.json') as f:
    data=json.load(f)
for row in data['finite_row_primitive_search_results']:
    print(row['case'], row['primitive_exists'],
          row['obstruction_value_on_residual'],
          row['primitive_coefficients'], row['obstruction_covector'])
PY
git diff --check -- tate-P1-hadamard-mittag-leffler.tex scripts/finite_window_graph_array.py
grep -n '[[:blank:]]$' tate-P1-hadamard-mittag-leffler.tex scripts/finite_window_graph_array.py || true
rg -n "finite-row-primitive-search-interface|theta-three-finite-row-obstruction|finite_row_primitive_search" tate-P1-hadamard-mittag-leffler.tex scripts/finite_window_graph_array.py
lacheck tate-P1-hadamard-mittag-leffler.tex
chktex -q tate-P1-hadamard-mittag-leffler.tex | rg -n "181[0-9]|182[0-9]|183[0-9]|184[0-9]|185[0-9]|186[0-9]|187[0-9]|188[0-9]|189[0-9]|190[0-9]|191[0-9]|192[0-9]|193[0-9]|194[0-9]|195[0-9]|196[0-9]|197[0-9]|198[0-9]|199[0-9]|200[0-9]|201[0-9]|202[0-9]|203[0-9]|204[0-9]|205[0-9]|206[0-9]|207[0-9]|208[0-9]|209[0-9]" -C 1 || true
```

Results:

- `py_compile` passed.
- JSON emitted the primitive-search schema and the three decisions above.
- `git diff --check` passed.
- trailing-whitespace grep returned no hits.
- label/key scans found the new TeX propositions and script payload.
- `lacheck` reports only the pre-existing nonbreaking-space suggestions at
  lines 39, 218, and 221.
- the targeted `chktex` scan over the new proposition range returned no hits.
- `make pdf` was not run: the shared checkout has broad concurrent staged
  manuscript edits and tracked build output outside this agent's ownership.

## Files Changed/Staged

- `tate-P1-hadamard-mittag-leffler.tex`
- `scripts/finite_window_graph_array.py`
- `reconstitution/swarm-2026-04-30-agent-187-finite-window-qme-rows-0957.md`

## Remaining Obligations

1. Supply the actual renormalized Costello weight
   \(K^M_{\Theta_3}=W^{R,M}_{\Theta_3,L,w}(B^\Theta_\bullet)\).
2. Prove \(d_{\mathrm{ns},M}\mathsf E_{\theta_3,M}=0\) from the Hom-valued
   Bianchi identity, or add the missing companion rows that make the full
   order-three residual closed.
3. Search a larger degree-zero primitive basis in the local-functional
   complex.  The current obstruction is exact only for the displayed
   finite row subcomplex.
4. For larger order-two packages, provide numerical or symbolic row values,
   scalar gates, source-face matrices \(v\), genuine seed matrices \(u\),
   bracket matrices \(q\), primitive transports \(P^{M,N}\), and the
   resulting Roos class.
