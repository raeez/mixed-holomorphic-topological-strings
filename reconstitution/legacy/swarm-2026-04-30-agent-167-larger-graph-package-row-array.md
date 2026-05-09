# Agent 167 - Larger Graph Package Row Array

Status: patched owned surfaces; no commits or pushes.

## Stable Core

The minimal full-equivariant finite-window non-scalar QME branch remains
proved all orders only in its minimal habitat.  A larger graph package now
has one executable row datum beyond that habitat:
\[
  \theta_3=\mathrm{CE}(\Theta_3,\nu_3),\qquad |\Theta_3|_\hbar=3.
\]
This is a Hom-valued CE-source face row for a genuine full-equivariant
marked seed.  It is not a scalar-contact closure composite and not a
bracket row.

The row fields are:

- graph type: \(\tau_{\theta_3}=\mathrm{CE}\), \(|\theta_3|_\hbar=3\);
- coefficient window: \(d_{\max}(\theta_3)=3\);
- edge labels:
  \(e_{\mathrm{pp}}:P_{\epsilon,L}^{w,M}\) with
  \(h_{2,1}=z_1^2z_2,\rho_{2,1}\),
  \(e_{\mathrm{ct}}:\Delta_{\epsilon,L}^{w,M}\) with
  \(h_{1,1}=z_1z_2,\rho_{1,1}\), and
  \(e_{\mathrm{W}}:E_{\mathrm{Weyl}}\) with \(z_1^2,z_2\);
- vertex labels:
  \(u_{a(t)dt\otimes z_1^2}\),
  \(u_{b(t)dt\otimes z_2}\),
  \(c_{B_\theta,\rho_{2,1}}\) with
  \(B_\theta\in\mathcal D^{\mathrm{reg}}_c(I)\),
  \(I^w_{0,M}\), and
  \(W^{R,M}_{\Theta_3,L,w}(B^\Theta_\bullet)\);
- marker tensor:
  \(\mathfrak m_{\theta_3}\in
  \mathcal M^{\mathrm{full}}(\C^{N|N})\), a full-equivariant signed
  Brauer marker with cyclic supertrace zero;
- CE-source sign:
  \(d_{\mathrm{CE}}\zeta_M=+\zeta_{M,\nu_3}+\cdots\);
- row incidence sign:
  \(-1\), from \(-\kappa(d_{\mathrm{CE}}\zeta_M)\);
- row value:
  \[
    R^{\mathrm{row}}_{\theta_3,M}
      =
    -K^M_{\Theta_3}(\zeta_{M,\nu_3})
      =:\mathsf E_{\theta_3,M}\neq0;
  \]
- closure datum:
  \(d_{\mathrm{ns},M}\mathsf E_{\theta_3,M}=0\);
- scalar gate:
  \[
    S_{\theta_3,M}
      =
    \widehat\sigma_{\mathrm{sc},M}(\mathsf E_{\theta_3,M})=0;
  \]
- truncation:
  \[
    \pi_{M,N}\mathsf E_{\theta_3,M}
      =
    \mathsf E_{\theta_3,N}\quad(N\ge3),\qquad
    \pi_{M,N}\mathsf E_{\theta_3,M}=0\quad(N<3),
  \]
  so \(t^{M,N}_{\theta_3\theta_3}=1\) for \(N\ge3\), all off-diagonal
  entries are zero, and every entry is zero for \(N<3\);
- class:
  \[
    \mathfrak o^{\mathrm{ns}}_{\theta_3,M}
      =
    [\mathsf E_{\theta_3,M}]
      \in
    H^1(\mathcal K^\bullet_{\mathrm{ns},M}(I),d_{\mathrm{ns},M}).
  \]

Decision: the row does not vanish as a local-functional cochain.  Its
scalar gate vanishes.  No primitive is supplied, so this is an explicit
symbolic obstruction datum.  A fixed-window counterterm exists exactly when
\[
  \mathfrak o^{\mathrm{ns}}_{\theta_3,M}=0,\qquad
  d_M C_{\theta_3,M}=-\mathsf E_{\theta_3,M}.
\]

## Valid Attacks

```yaml
- id: A1-167-01
  severity: 1
  status: healed
  lens: larger-package executability
  target: tate-P1-hadamard-mittag-leffler.tex finite-window row array
  claim: Larger graph packages can remain formal residual symbols after the minimal all-order branch is proved.
  broken_step: A larger package has no obstruction class until at least one row supplies graph type, labels, marker, sign, value, scalar gate, truncation matrix, and class data.
  evidence_type: proof_gap
  evidence_ref: defn:finite-window-graph-array; prop:app-first-order-three-larger-package-datum
  confidence: high
  blast_radius: The row-array machinery remains abstract and cannot be used to test a larger package.
  minimal_heal: Add one concrete order-three full-equivariant CE-source row with all row fields and a machine-readable script payload.
  residual: Actual Costello integral and primitive remain unsupplied.

- id: A1-167-02
  severity: 1
  status: healed
  lens: scalar-gate firewall
  target: order-three full-equivariant row
  claim: Full-equivariant scalar-gate vanishing makes the larger row vanish.
  broken_step: The scalar projection kills only \(S_{\theta_3,M}\).  It does not kill the non-scalar local functional \(\mathsf E_{\theta_3,M}\).
  evidence_type: proof_gap
  evidence_ref: thm:app-full-equivariant-marked-shadow-vanishing; def:app-nonscalar-kernel-row-complex
  confidence: high
  blast_radius: A false all-order extension would erase the row-data obstruction problem.
  minimal_heal: State \(S_{\theta_3,M}=0\), keep \(\mathsf E_{\theta_3,M}\neq0\), and form \([\mathsf E_{\theta_3,M}]\) in \(H^1(\mathcal K_{\mathrm{ns},M})\).
  residual: Determine whether the displayed class is zero.

- id: A1-167-03
  severity: 2
  status: healed
  lens: cohomology class formation
  target: \(\mathfrak o^{\mathrm{ns}}_{\theta_3,M}\)
  claim: A CE-source face row automatically defines an \(H^1\)-class.
  broken_step: A row value defines an obstruction class only after the kernel closure equation is supplied.
  evidence_type: proof_gap
  evidence_ref: def:app-nonscalar-kernel-row-complex
  confidence: high
  blast_radius: Without closure, the object is only a cochain, not an obstruction class.
  minimal_heal: Add the row-closure datum \(d_{\mathrm{ns},M}\mathsf E_{\theta_3,M}=0\), and state that omitting it invalidates the obstruction row.
  residual: In a real package, prove this closure from the Hom-valued Bianchi identity or compute the missing companion rows.

- id: A1-167-04
  severity: 2
  status: healed
  lens: finite-window truncation
  target: \(t^{M,N}_{\theta_3\theta_3}\)
  claim: Truncation of the added order-three row follows from the abstract cutoff.
  broken_step: The row array requires explicit matrix entries.
  evidence_type: proof_gap
  evidence_ref: defn:finite-window-graph-array; prop:projection-defined-uvq-truncation-data
  confidence: high
  blast_radius: The finite-window tower and Roos class are undefined without row transport.
  minimal_heal: Supply the identity transport for \(N\ge3\), zero transport for \(N<3\), zero off-diagonal entries, and the cocycle condition.
  residual: None for this symbolic one-row tower.
```

## Repaired Labels

- `prop:concrete-order-three-larger-package-row`
- `scripts/finite_window_graph_array.py` key:
  `order_3_concrete_larger_package_row`

## Script Output

Command:

```bash
python3 scripts/finite_window_graph_array.py
```

Decisive JSON excerpt:

```json
{
  "order_3_concrete_larger_package_row": {
    "row_label": "theta_3=CE(Theta_3,nu_3)",
    "graph_type": "CE-source face of a genuine |Theta_3|_hbar=3 marked seed",
    "incidence_sign_in_row_value": -1,
    "row_value": "R_{theta_3,M}^{row}=-K^M_{Theta_3}(zeta_{M,nu_3})=:E^M_{theta_3}, declared nonzero as a local functional",
    "scalar_gate": "S_{theta_3,M}=0 in the full-equivariant marked habitat; the displayed Weyl scalar contact also has omega(z1^2,z2)=0",
    "truncation_matrix": "for M>=N: t^{M,N}_{theta_3,theta_3}=1 if N>=3; all off-diagonal entries are 0; if N<3 the row has no degree<=N representative and every t entry is 0",
    "class_in_K_ns": "o^{ns}_{theta_3,M}=[E^M_{theta_3}] in H^1(K^bullet_{ns,M}(I),d_{ns,M})",
    "decision": "nonzero cochain with zero scalar gate; no primitive is supplied, so the row remains an explicit symbolic obstruction datum"
  }
}
```

## Verification

Commands run:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py
git diff --check -- tate-P1-hadamard-mittag-leffler.tex scripts/finite_window_graph_array.py reconstitution/swarm-2026-04-30-agent-167-larger-graph-package-row-array.md
grep -n '[[:blank:]]$' tate-P1-hadamard-mittag-leffler.tex scripts/finite_window_graph_array.py reconstitution/swarm-2026-04-30-agent-167-larger-graph-package-row-array.md
rg -n "concrete-order-three-larger-package-row|theta_3|order_3_concrete_larger_package_row|ConcreteOrderThreeCESourceRow|A1-167" tate-P1-hadamard-mittag-leffler.tex scripts/finite_window_graph_array.py reconstitution/swarm-2026-04-30-agent-167-larger-graph-package-row-array.md
lacheck tate-P1-hadamard-mittag-leffler.tex
chktex -q tate-P1-hadamard-mittag-leffler.tex | rg -n "183[0-9]|184[0-9]|185[0-9]|186[0-9]|187[0-9]|188[0-9]|189[0-9]|190[0-9]|191[0-9]|192[0-9]|193[0-9]|194[0-9]|195[0-9]" -C 1
```

Results:

- `py_compile` passed.
- the script emitted the order-three row payload above;
- `git diff --check` passed;
- trailing-whitespace grep returned no hits;
- label/key scans found the TeX proposition and script payload;
- `lacheck` reports only the pre-existing nonbreaking-space suggestions at
  lines 39, 218, and 221;
- a targeted `chktex` scan over the new proposition range returned no hits;
- `make pdf` was not run because the shared checkout has concurrent staged
  manuscript edits and tracked build output.

## Files Changed/Staged

Changed:

- `tate-P1-hadamard-mittag-leffler.tex`
- `scripts/finite_window_graph_array.py`
- `reconstitution/swarm-2026-04-30-agent-167-larger-graph-package-row-array.md`

Staged after scoped verification.

## Remaining Theorem Obligations

1. Supply an actual renormalized Costello weight
   \(K^M_{\Theta_3}=W^{R,M}_{\Theta_3,L,w}(B^\Theta_\bullet)\) from a real
   finite graph package.
2. Prove the closure
   \(d_{\mathrm{ns},M}\mathsf E_{\theta_3,M}=0\) from the Hom-valued Bianchi
   identity, or add the missing companion rows that make the full order-three
   residual closed.
3. Compute whether
   \([\mathsf E_{\theta_3,M}]\) vanishes in
   \(H^1(\mathcal K^\bullet_{\mathrm{ns},M}(I),d_{\mathrm{ns},M})\).
4. If it vanishes, construct \(C_{\theta_3,M}\) and then compute the Roos
   \(\varprojlim^1H^0\) compatibility class for the finite-window tower.
5. Prove regular-density or wavefront-admissible locality for the selected
   external current labels of \(\Theta_3\).
