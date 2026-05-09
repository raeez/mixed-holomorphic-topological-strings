# Agent 244 - Non-scalar counterterm matrix construction push

Status: report-only attack-heal pass.  Owned files:

- `reconstitution/nonscalar-counterterm-matrix-construction-push-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-244-nonscalar-counterterm-matrix-construction-push.md`

No TeX, script, source, figure, or build file was edited.

## Claim attacked

The attacked claim was that the finite-window non-scalar QME counterterm
matrix can already be constructed for the first unsolved non-scalar rows.

## Result

The construction does not close from current data.  The exact current
obstruction is the one-row \(\theta_3\) matrix:
\[
  \mathcal K^0_{\theta_3,M}=0,\qquad
  \mathcal K^1_{\theta_3,M}=\C\mathsf E_{\theta_3,M},\qquad
  \mathsf E_{\theta_3,M}=-K^M_{\Theta_3}(\zeta_{M,\nu_3}).
\]
The scalar gate is zero.  The primitive matrix is \(1\times0\),
\[
  A^M=[\,]_{1\times0},\qquad r^M=(1),
\]
and
\[
  \ell_{\theta_3}A^M=0,\qquad
  \ell_{\theta_3}(r^M)=1.
\]
Thus \(\ell_{\theta_3}\) is a finite-row cokernel certificate.

A positive counterterm matrix would need a new degree-zero column with
\[
  A^M_{\theta_3,C}=-1,\qquad
  d_{\mathrm{ns},M}C_{\theta_3,M}=-\mathsf E_{\theta_3,M}.
\]
With identity/zero primitive transport, \(c_M=1\) solves the fixed-window
equation and the Roos class is zero.  The script accepts this as a guarded
interface fixture, not as current data.

## Attack-heal ledger

```yaml
- id: A1-244-01
  severity: 1
  status: valid
  lens: finite-row primitive matrix
  target: theta_3 current finite row subcomplex
  claim: The current package contains a counterterm primitive for the first unsolved row.
  broken_step: The supplied complex has no degree-zero basis row.
  evidence_type: computation
  evidence_ref: "python3 scripts/finite_window_graph_array.py: theta_3_current_finite_row_subcomplex primitive_exists=false, A=[[]], r=E_theta_3, ell(E_theta_3)=1"
  minimal_heal: "Add C_theta_3 with dC=-E_theta_3, scalar projection zero, T A=A P, and zero Roos class."
  residual: "Existence in the full local-functional complex remains open."

- id: A1-244-02
  severity: 1
  status: valid
  lens: CE-source ancestor
  target: finite two-u source envelope
  claim: A pure CE ancestor d_CE eta=zeta_{M,nu_3} is present in the first finite source envelope.
  broken_step: A left-cokernel functional detects the target.
  evidence_type: finite_linear_algebra
  evidence_ref: "symmetric envelope: 45 columns, 304 rows, q d_CE=0, q(nu_3)=1; ordered envelope: 81 columns, 562 rows, q_ord d_CE=0, q_ord(nu_3)=1"
  minimal_heal: "Enlarge the source habitat and rerun the CE, Bianchi, scalar, transport, and Roos gates."
  residual: "This is not a universal no-go theorem outside the finite envelope."

- id: A1-244-03
  severity: 1
  status: valid
  lens: companion-face cancellation
  target: theta_3 eight-face source-algebraic table
  claim: The eight-face table cancels the theta residual.
  broken_step: The row-vector residual is nonzero in the declared basis and diagonal transport leaves an N=2 residual.
  evidence_type: script_output
  evidence_ref: "theta_3_eight_face_candidate_obstruction_check accepted=false; residual=(2,-2,3,2,-1,1,-2,-3); N=2 residual=(2,-2)"
  minimal_heal: "Supply the marked Costello incidence/weight table, codimension-two closure, and lower-window identity E^2_nu02=E^2_nu20 or a new row presentation."
  residual: "Source coefficients alone are not row cancellation."

- id: A1-244-04
  severity: 2
  status: valid
  lens: current/wavefront locality
  target: distributional labels in graph weights
  claim: The matrix problem is formed for arbitrary D'_c(I) labels.
  broken_step: Arbitrary distributional graph contractions may fail Hormander product and diagonal-extension conditions before row values exist.
  evidence_type: line_reference
  evidence_ref: "regular-density-wavefront-current-graph-branch-construction-target-2026-04-30.md"
  minimal_heal: "Restrict to regular densities or a named wavefront-admissible subspace; otherwise record eta^reg or the microlocal no-canonical-product obstruction."
  residual: "No arbitrary D'_c graph theorem is supplied."
```

## Command results

`python3 -m py_compile scripts/finite_window_graph_array.py` passed.

`python3 scripts/finite_window_graph_array.py` was emitted to
`/tmp/finite-window-agent244.json` and parsed with `json.tool`.  Focused
results:

```text
minimal_full_equivariant_order_2_zero:
  primitive_exists=True, A=[], r=[], ell_r=0, Roos=0

theta_3_current_finite_row_subcomplex:
  primitive_exists=False, A=[[]], r=E_theta_3:1,
  target=E_theta_3:-1, ell=E_theta_3:1, ell_r=1

theta3_ce_ancestor_supplied_exact_payload:
  accepted=True only with differential value -1

theta3_counterterm_supplied_exact_payload:
  accepted=True only with differential value -1

theta3_eight_face_candidate_source_algebraic_obstruction:
  accepted=False,
  residual=(2E_nu02,-2E_nu20,3E_nu03,2E_nu12_1,
            -E_nu12_2,E_theta_3,-2E_nu21_2,-3E_nu30),
  coefficient_sum=0,
  N=2 residual=(2E_nu02,-2E_nu20)
```

Finite CE source probe:

```text
H_basis=9
symmetric columns=45
symmetric output rows=304
symmetric nonzero matrix entries=380
q d_CE nonzero count=0
q(target)=1
ordered columns=81
ordered output rows=562
ordered nonzero matrix entries=752
q_ordered d_CE nonzero count=0
q_ordered(target)=1
```

## Proposed next theorem insertion

The next theorem should be an obstruction proposition, not a construction
claim.  It should state the one-row matrix \(A^M=[\,]_{1\times0}\),
\(r^M=(1)\), \(\ell_{\theta_3}(r^M)=1\); then state the exact positive
escape conditions:

1. a scalar-zero CE-ancestor or local counterterm column with
   \(A_{\theta_3,C}=-1\), \(TA=AP\), and zero Roos class;
2. a complete marked companion-face table with zero signed row vector and
   zero lower-window residual;
3. a current-compatible regular-density or wavefront-admissible graph
   habitat in which all row values are actually defined.

The canonical statement is drafted in
`reconstitution/nonscalar-counterterm-matrix-construction-push-2026-04-30.md`.

## Files changed

- `reconstitution/nonscalar-counterterm-matrix-construction-push-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-244-nonscalar-counterterm-matrix-construction-push.md`
