# Agent 285 - Non-Scalar Row-Matrix Script Evidence Audit

Status: report-only. No TeX, script, figure, bibliography, source fixture,
or build artifact was edited.

Companion report:

- `reconstitution/nonscalar-row-matrix-script-evidence-audit-2026-04-30.md`

## Scope

Audited `scripts/finite_window_graph_array.py` against the current TeX
surface for the non-scalar finite-row matrix claims:

- the primitive equation \(A^M c=-r^M\), and the centrality/homotopy variant
  \(A^M h^M=-r^M\);
- the minimal full-equivariant zero row;
- the one-row \(\theta_3\) obstruction matrix;
- the \(\theta_3\) primitive payload gates;
- the eight-face companion table and its lower-window transport;
- the Bianchi-exposed lower matrix \(A_D^2=(-2,2,1)^T\), where current TeX
  uses it.

## Verdict

No TeX/script mismatch was found for the outputs actually emitted by
`scripts/finite_window_graph_array.py`.

The important boundary is this: `finite_window_graph_array.py` does not emit
the Bianchi-exposed lower matrix \(A_D^2=(-2,2,1)^T\), the residual
\(r_2=(2,-2,0)^T\), the cokernel
\(\widetilde\lambda_{02,\mathfrak b}\), or the all-degree \(q_{2u}\)
source-envelope obstruction. Current TeX includes those statements, but their
evidence is the later theta3 Bianchi reports, especially Agents 270, 277, and
282, not this script. They must not be cited as script output.

The script also does not, by itself, prove the all-order minimal
full-equivariant theorem. It verifies the computed finite rows, the minimal
order-two zero primitive search, and the zero-row families used by the TeX
induction. The all-order statement in current TeX is a manuscript proof using
those row facts, not a direct executable output of the script.

## Script Facts Checked

The script compiles and emits JSON:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py
```

Focused inspection gives these decisive records.

1. Primitive-search schema. The script defines
   \(A_{ij}\) by
   \(d_{\mathrm{ns},M}\eta_j=\sum_i A_{ij}\rho_i\), records
   \(R_M=\sum_i r_i\rho_i\), and solves \(Ac=-r\). It also requires
   \(T^{M,N}r_M=r_N\) and \(T^{M,N}A_M=A_NP^{M,N}\) before Roos
   compatibility is tested. This matches
   `tate-P1-hadamard-mittag-leffler.tex:1816-1875`,
   `appendix-unreduced-bv-qme.tex:2302-2318`,
   `open-obligations.tex:592-619`, `principles.tex:238-260`, and
   `theorem-lanes.tex:2958-2969`.

2. Minimal zero row. The emitted case
   `minimal_full_equivariant_order_2_zero` has empty degree-zero basis,
   empty degree-one basis, empty residual vector, empty target vector,
   `primitive_exists=true`, obstruction value `0`, and zero Roos class.
   This matches the minimal zero-row TeX statements at
   `tate-P1-hadamard-mittag-leffler.tex:1266-1402`,
   `tate-P1-hadamard-mittag-leffler.tex:1404-1597`, and
   `theorem-lanes.tex:3279-3303`, subject to the all-order caveat above.

3. Current \(\theta_3\) one-row subcomplex. The emitted case
   `theta_3_current_finite_row_subcomplex` has
   degree-zero basis `[]`, degree-one basis `[E_theta_3]`, differential
   matrix `[[]]`, residual vector `[(E_theta_3,1)]`, target vector
   `[(E_theta_3,-1)]`, `primitive_exists=false`, obstruction covector
   `[(E_theta_3,1)]`, and obstruction value `1`. This exactly matches
   `tate-P1-hadamard-mittag-leffler.tex:2026-2079`,
   `theorem-lanes.tex:3307-3326`, `open-obligations.tex:715-758`,
   `local-dictionary.tex:1030-1050`, and `abstract.tex:183-205`.

4. \(\theta_3\) row transport. The script records the common row
   \(E_{\theta_3}=-K^M_{\Theta_3}(\zeta_{M,\nu_3})\), scalar projection
   `0`, identity transport for \(N\ge3\), and zero transport for \(N<3\).
   This matches `tate-P1-hadamard-mittag-leffler.tex:1898-2024`.

5. Primitive payload gates. The absent and missing-differential payloads
   reject. The CE-ancestor and counterterm exact payloads accept only when
   the supplied column has differential entry `-1`, scalar projection zero,
   \(TA=AP\), and zero Roos class. The script marks both accepted exact
   payloads as interface fixtures "not present in the current data".
   Current TeX preserves this boundary at
   `tate-P1-hadamard-mittag-leffler.tex:2092-2224` and
   `open-obligations.tex:733-758`.

6. Companion-face gate. The current script rejects
   `theta3_complete_companion_faces_supplied_exact_payload` unless the marked
   Costello incidence/weight table and transported lower-window residual
   zero are supplied. It also rejects the eight-face source-algebraic
   candidate as theorem-grade cancellation.

7. Eight-face candidate. The emitted vector is
   \[
     (2,-2,3,2,-1,1,-2,-3)
   \]
   on
   \[
     E_{\nu_{02}},E_{\nu_{20}},E_{\nu_{03}},
     E_{\nu_{12}^{(1)}},E_{\nu_{12}^{(2)}},
     E_{\theta_3},E_{\nu_{21}^{(2)}},E_{\nu_{30}}.
   \]
   The coefficient sum is `0`, but the row vector is nonzero. Diagonal
   \(v\)-transport has a verified cocycle identity and sends the row at
   \(N=2\) to \(2E_{\nu_{02}}-2E_{\nu_{20}}\). The marked Costello
   incidence/weight table is absent. This matches
   `tate-P1-hadamard-mittag-leffler.tex:2226-2368`,
   `theorem-lanes.tex:3346-3378`, and `open-obligations.tex:779-810`.

## TeX Boundary Findings

### \(A^M h^M=-r^M\)

The script emits the generic primitive equation as \(Ac=-r\). Current TeX
uses \(A^M h^M=-r^M\) only in the binary centrality/homotopy setting, where
`main.tex:8316-8339` defines
\[
  H^M_{x,y}=\sum_j h^M_j\eta^M_j.
\]
Thus \(h^M\) is the coefficient vector for homotopy candidates, while \(c\)
is the generic counterterm coefficient vector in the script. This is a
notation change, not a mathematical mismatch. It should not be described as
a literal script string.

### Minimal zero row

The current TeX zero-row statement
\[
  A^M_{\min}:0\to0,\qquad r^M_{\min}=0,\qquad h^M_{\min}=0
\]
matches the script's minimal empty-row primitive search after zero rows are
suppressed. If labelled zero rows are retained, the script records identity
transport for retained scalar-contact/scalar-zero labels, and zero
truncation for bracket rows containing zero local-functional inputs. Current
TeX records the same convention.

The all-order minimal theorem in `appendix-unreduced-bv-qme.tex:3152-3203`
and `theorem-lanes.tex:3286-3298` is stronger than the script's explicit
minimal order-two JSON record. It is acceptable only as a TeX proof by
induction from the zero-row facts, not as an executable script result.

### \(\theta_3\) primitive and companion rows

Current TeX does not promote the script's accepted interface fixtures into
present data. It says a primitive payload would need
\[
  A^M_{\theta_3,C}=-1,\qquad
  d_MC_{\theta_3,M}=-\mathsf E_{\theta_3,M},
\]
with scalar-zero and Roos compatibility, and then immediately records that
the current data do not contain such a payload. This matches the script.

The eight-face companion row is also handled correctly: current TeX states
that source coefficients alone do not give a marked Costello cancellation,
that the row vector is nonzero in the displayed basis, and that diagonal
transport leaves the \(N=2\) residual.

### Bianchi-exposed lower matrix

Current TeX contains the sharper lower-window matrix
\[
  A_D^2=(-2,2,1)^T,\qquad r_2=(2,-2,0)^T,
\]
with cokernel
\[
  \widetilde\lambda_{02,\mathfrak b}
  =
  \frac12(E^2_{\nu_{02}})^*+(\mathfrak b^2_{02,20})^*.
\]
This is not emitted by `scripts/finite_window_graph_array.py`. It is
supported by the Bianchi reports:

- `reconstitution/swarm-2026-04-30-agent-277-theta3-bianchi-matrix-integration-spec.md`
- `reconstitution/theta3-bianchi-matrix-integration-spec-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-282-theta3-bianchi-counterterm-construction-push.md`
- `reconstitution/theta3-bianchi-counterterm-construction-push-2026-04-30.md`

Those reports record the calculation
\[
  \widetilde\lambda_{02,\mathfrak b}A_D^2=0,\qquad
  \widetilde\lambda_{02,\mathfrak b}(r_2)=1.
\]
The finite-window graph-array script can be cited for the \(N=2\) residual
that motivates this lower repair, but not for the Bianchi-exposed matrix
itself.

## Stale Report Hazard

Older report `reconstitution/swarm-2026-04-30-agent-201-theta3-row-data-generator.md`
records `theta3_complete_companion_faces_supplied_exact_payload accepted=true`.
The current script no longer has that decision: Agent 224 strengthened the
validator, and the current script rejects that companion fixture unless the
marked Costello incidence/weight table and lower-window zero are supplied.
Current TeX follows the strengthened validator. Do not reuse the Agent 201
companion acceptance line as current evidence.

## Files Audited

- `scripts/finite_window_graph_array.py`
- `tate-P1-hadamard-mittag-leffler.tex`
- `appendix-unreduced-bv-qme.tex`
- `theorem-lanes.tex`
- `open-obligations.tex`
- `claim-strength-ledger.tex`
- `local-dictionary.tex`
- `abstract.tex`
- `principles.tex`
- `main.tex`

## Verification Commands

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py | python3 -c 'import json,sys; d=json.load(sys.stdin); print(d["finite_row_primitive_search_results"])'
python3 scripts/finite_window_graph_array.py | python3 -c 'import json,sys; d=json.load(sys.stdin); print(d["theta_3_primitive_payload_checks"]); print(d["theta_3_companion_face_payload_checks"])'
rg -n -F -e 'A^M h' -e 'h^M_{min}' -e 'A^M c' -e 'A^M_{\theta_3,C}' --glob '*.tex'
rg -n -F -e 'A_D^2' -e 'D^2_{02,20}' -e 'q_{2u}' -e '\widetilde\lambda' scripts reconstitution --glob '*.py' --glob '*.md'
```

No build was run. This was a report-only audit with no manuscript edits.
