# Agent 161 - Truncation Matrices for Graph Rows

Status: patched owned surfaces; no commits or pushes.

## Stable Core

The computed finite-window row families now have explicit truncation
matrices under \(\pi_{M,N}\).  The repaired manuscript adds
Proposition~\(\ref{prop:computed-finite-window-truncation-matrices}\), which
fixes a label-retaining convention for rows with \(d_{\max}\leq N\), proves
stability under \(M\to N\to P\), and isolates the remaining larger-package
entries as named matrices.

The closed matrices are:

\[
  t^{M,N}_{\alpha_{\mathrm{sc}}\alpha_{\mathrm{sc}}}=1,\qquad
  t^{M,N}_{\alpha_{\mathrm{sc}}\alpha'}=0
  \quad(\alpha'\neq\alpha_{\mathrm{sc}})
\]
for \(M\geq N\geq1\).  This is the label-retaining transport of the
one-cross scalar-contact row.  In the full-equivariant branch the row value
is already zero, but the retained label is transported by the identity row.

\[
  t^{M,N}_{\alpha_{11}\alpha_{11}}=1,\qquad
  t^{M,N}_{\alpha_{11}\alpha'}=0
  \quad(\alpha'\neq\alpha_{11})
\]
for the retained scalar-zero row \(\alpha_{11}\).  If zero rows are
suppressed, this row and its matrix are empty.

For the two codimension-two scalar-contact composites
\(\gamma_{21}=(\beta_2|\beta_1,\beta_1)\) and
\(\gamma_{12}=(\beta_1|\beta_2,\beta_2)\),
\[
  t^{M,N}_{\gamma_{21}\gamma_{21}}=1,\qquad
  t^{M,N}_{\gamma_{12}\gamma_{12}}=1,
\]
with all off-diagonal entries from these rows equal to zero whenever the
lower window contains the degree-one Hamiltonian labels.  Pair cancellation
is stable.

For every bracket row \(b\) containing a retained zero row
\(\alpha_0\in\{\alpha_{\mathrm{sc}},\alpha_{11}\}\),
\[
  t^{M,N}_{bb'}=0
  \qquad\text{for every lower-window bracket row }b'.
\]

For genuine \(|\Gamma|_\hbar=2\) rows the minimal package has an empty
matrix.  A larger package must supply
\[
  t^{M,N}_{d\Gamma,d\Gamma'}=u^{M,N}_{\Gamma\Gamma'}
\]
and, for CE source faces,
\[
  t^{M,N}_{\mathrm{CE}(\Gamma,\nu),
  \mathrm{CE}(\Gamma',\nu')}
  =
  v^{M,N}_{\Gamma,\nu;\Gamma',\nu'}.
\]
Stability is exactly
\[
  u^{M,P}_{\Gamma\Gamma''}
  =
  \sum_{\Gamma'}u^{M,N}_{\Gamma\Gamma'}u^{N,P}_{\Gamma'\Gamma''},
\]
\[
  v^{M,P}_{\Gamma,\nu;\Gamma'',\nu''}
  =
  \sum_{\Gamma',\nu'}
  v^{M,N}_{\Gamma,\nu;\Gamma',\nu'}
  v^{N,P}_{\Gamma',\nu';\Gamma'',\nu''}.
\]

Nonzero bracket rows \(b(\beta_1,\beta_2)\) with
\(\beta_i\notin\{\alpha_{\mathrm{sc}},\alpha_{11}\}\) remain larger-package
data.  Their missing matrix entries are the coefficients
\[
  q^{M,N}_{\beta_1,\beta_2;\beta'_1,\beta'_2}
\]
defined by projecting the normalized bracket row to the lower-window bracket
row basis.

## Valid Attacks

```yaml
- id: A1-161-01
  severity: 2
  status: healed
  lens: finite-window truncation
  target: prop:first-finite-window-array-rows
  claim: The computed scalar-contact row is compatible under truncation without an explicit matrix.
  broken_step: The row-array definition requires coefficients t^{M,N}_{alpha alpha'}; the proposition did not supply them.
  evidence_type: proof_gap
  evidence_ref: defn:finite-window-graph-array
  minimal_heal: Add the label-retaining identity row for alpha_sc and prove stability.
  residual: none for the computed scalar-contact row.

- id: A1-161-02
  severity: 2
  status: healed
  lens: scalar-zero row propagation
  target: alpha_11 row family
  claim: The scalar-zero alpha_11 row had a lower-window matrix in the Tate finite-window surface.
  broken_step: The datum existed only in appendix-unreduced-bv-qme.tex; the owned Tate row theorem and script did not emit it.
  evidence_type: line_reference
  evidence_ref: prop:app-first-scalar-zero-order-one-row
  minimal_heal: Import the row as a computed scalar-zero family and record t^{M,N}_{alpha_11,alpha_11}=1 when retained.
  residual: if zero rows are suppressed, the row is empty by convention.

- id: A1-161-03
  severity: 2
  status: healed
  lens: bracket rows
  target: order-two larger-package residual
  claim: Every bracket row not containing alpha_sc remains missing.
  broken_step: Bracket rows containing retained alpha_11 also vanish, because K^M_{alpha_11}=0.
  evidence_type: proof
  evidence_ref: prop:app-first-scalar-zero-order-one-row; prop:computed-finite-window-truncation-matrices
  minimal_heal: Narrow the missing bracket matrices to q-entries with beta_i not in {alpha_sc, alpha_11}.
  residual: all such q entries remain missing until the added order-one rows are supplied.

- id: A1-161-04
  severity: 1
  status: healed
  lens: genuine hbar-two rows
  target: prop:genuine-order-two-graph-weight-rows
  claim: Truncation of genuine seed rows follows from cutoff alone.
  broken_step: Projected normalized weights and CE source faces can decompose into lower-window row combinations.
  evidence_type: proof_gap
  evidence_ref: prop:genuine-order-two-graph-weight-rows
  minimal_heal: State u and v as the required matrices and add their cocycle conditions.
  residual: actual u and v entries are missing until the seed list, weights, d_M expansions, and CE signs are supplied.
```

## Repaired Labels And Script Keys

- `prop:computed-finite-window-truncation-matrices` added.
- `prop:order-two-finite-window-boundary-rows` refined so missing bracket
  rows exclude retained zero rows such as \(\alpha_{11}\).
- `scripts/finite_window_graph_array.py` now emits
  `order_1_scalar_zero_rows` and `computed_truncation_matrix_families`.

## Script Output

Command:

```bash
python3 scripts/finite_window_graph_array.py
```

Decisive output entries:

```text
omega_z1_z1: 0
order_1_scalar_zero_rows[0].row_label: alpha_11
order_1_scalar_zero_rows[0].truncation_matrix:
  if retained and M>=N>=1:
  t^{M,N}_{alpha_11,alpha_11}=1 and
  t^{M,N}_{alpha_11,alpha'}=0 for alpha'!=alpha_11
computed_truncation_matrix_families:
  alpha_sc: identity row
  alpha_11: identity row if retained, empty if suppressed
  gamma_21,gamma_12: diagonal identity
  brackets containing alpha_sc or alpha_11: zero row
  genuine dGamma/CE rows: t=u and t=v, empty in the minimal package
  nonzero added brackets: missing q entries
```

## Verification

Commands run:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py
git diff --check -- tate-P1-hadamard-mittag-leffler.tex scripts/finite_window_graph_array.py
grep -n '[[:blank:]]$' tate-P1-hadamard-mittag-leffler.tex scripts/finite_window_graph_array.py
rg -n -F "computed-finite-window-truncation-matrices" tate-P1-hadamard-mittag-leffler.tex
rg -n -F "computed_truncation_matrix_families" scripts/finite_window_graph_array.py
lacheck tate-P1-hadamard-mittag-leffler.tex
chktex -q tate-P1-hadamard-mittag-leffler.tex
```

Results:

- `py_compile` passed.
- The script emitted the alpha_11 row and computed truncation matrix
  families.
- `git diff --check` passed.
- trailing-whitespace grep returned no hits.
- label/key scans found the new proposition and script payload key.
- `lacheck` reports only the pre-existing nonbreaking-space suggestions at
  lines 39, 218, and 221.
- `chktex` reports nonfatal style warnings, mostly pre-existing table,
  parenthesis, and spacing warnings; no fatal TeX syntax error was detected
  by the scoped check.
- `make pdf` was not run because the shared checkout has concurrent staged
  edits and the build writes tracked output outside this agent's owned paths.

## Files Changed/Staged

Changed:

- `tate-P1-hadamard-mittag-leffler.tex`
- `scripts/finite_window_graph_array.py`
- `reconstitution/swarm-2026-04-30-agent-161-truncation-matrices-for-graph-rows.md`

Staged after scoped verification.

## Remaining Theorem Obligations

1. Supply the actual larger finite seed list
   \(\mathcal G^{\mathrm{gen}}_{2,M}\).
2. Supply normalized weights \(K^M_\Gamma\), full \(d_MK^M_\Gamma\)
   expansions, and orientation/Koszul/symmetry coefficients.
3. Supply CE-source decompositions and signs unless strict CE-cycle
   evaluation removes them.
4. Prove full-equivariant marked-habitat membership row by row, or provide
   scalar projections.
5. Populate \(u^{M,N}\), \(v^{M,N}\), and the nonzero-bracket matrix
   \(q^{M,N}\), then compute the resulting \(H^1\) and Roos classes.
