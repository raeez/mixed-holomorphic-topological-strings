# Agent 220 - Non-Scalar Costello/QME Construction Frontier

Status: report-only attack-heal ledger.  Writable surface respected:

- `reconstitution/nonscalar-costello-qme-construction-frontier-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-220-nonscalar-costello-qme-construction-frontier.md`

## Stable Core

The current criterion is valid only as a finite-window construction test.  It
does not build the Costello graph/QME solution.  The strongest true frontier is
the exact package of missing data:

- codimension-two closed marked graph rows;
- completed local-functional and Hom complexes;
- filtered scalar-contact chain projection;
- continuous bulk-to-defect kernel with actual graph weights;
- finite-window counterterm recursion \(A^Mc=-r^M\);
- truncation, primitive transport, and Roos compatibility;
- product and \(P_0\)-centrality homotopies, including \(Q_\Omega\)-basic
  primitives in the equivariant branch.

The canonical report is
`reconstitution/nonscalar-costello-qme-construction-frontier-2026-04-30.md`.

## Attack-Heal Ledger

```yaml
- id: A1-220-01
  severity: 1
  status: healed
  lens: habitat versus construction
  target: non-scalar Costello/QME criterion
  claim: Naming the native finite-window habitat proves the non-scalar QME.
  broken_step: A habitat lacks row values, scalar lift, bulk-to-defect kernel,
    counterterm primitives, truncation matrices, and centrality homotopies.
  evidence_type: line_reference
  evidence_ref: appendix-unreduced-bv-qme.tex:2142,2234; main.tex:8021
  minimal_heal: Recast the statement as a construction frontier whose curvature
    equation is solved only after all named data are supplied.
  residual: Full graph package remains unconstructed.

- id: A1-220-02
  severity: 1
  status: healed
  lens: Costello row calculus
  target: finite marked graph list
  claim: Scalar-zero row labels define a QME cochain automatically.
  broken_step: The marked list must contain field-differential, BV-edge,
    collision/contact, counterterm, and CE-source faces with signs and
    codimension-two closure.
  evidence_type: line_reference
  evidence_ref: appendix-unreduced-bv-qme.tex:1623-1780,1900-1955
  minimal_heal: List the four Costello row formulas and the source-face term
    as mandatory construction data.
  residual: Actual larger seed sets and row coordinates are still missing.

- id: A1-220-03
  severity: 1
  status: healed
  lens: scalar-contact filtration
  target: \widehat\sigma_{\mathrm{sc}}
  claim: Associated-graded scalar vanishing forms the non-scalar complex.
  broken_step: The kernel complex is defined only after a filtered chain
    projection exists; the obstruction tower \(o_{\sigma,w}^{(r)}\) may block it.
  evidence_type: proof_gap
  evidence_ref: main.tex:8021-8083; appendix-unreduced-bv-qme.tex:2709-2757
  minimal_heal: Name the scalar-lift obstruction theorem target.
  residual: For any enlarged package outside the full-equivariant marked
    habitat, compute the first nonzero \(o_{\sigma,w}^{(r)}\) or prove vanishing.

- id: A1-220-04
  severity: 1
  status: healed
  lens: bulk-to-defect kernel
  target: \kappa_{\hbar,w,I}
  claim: Weighted coefficient kernels and reduced principal-part currents
    already give the Costello bulk-to-defect kernel.
  broken_step: The Costello local-functional map from the current CE source to
    the brane-defect target is not constructed, especially for \(\mathcal D'_c\)
    labels.
  evidence_type: missing_data
  evidence_ref: main.tex:7494-7509; reconstitution/swarm-2026-04-30-agent-093-bulk-defect-kernel.md:22;
    references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md:156
  minimal_heal: Require a continuous kernel with zero-edge generator values and
    positive graph weights \(K^M_\Gamma=W^{R,M}_{\Gamma,L,w}\).
  residual: Prove current-compatible wavefront/counterterm rules or restrict
    to regular densities.

- id: A1-220-05
  severity: 1
  status: healed
  lens: finite-window recursion
  target: counterterm tower
  claim: Fixed-window exactness is enough for all-window QME.
  broken_step: Windowwise primitives may fail under truncation; the Roos
    \(\varprojlim^1H^0\) class is independent data.
  evidence_type: proof_gap
  evidence_ref: appendix-unreduced-bv-qme.tex:2302-2333;
    reconstitution/swarm-2026-04-30-agent-094-finite-window-counterterms.md:44
  minimal_heal: Require \(T r=r\), \(T A=A P\), and
    \([Pc_M-c_N]=0\).
  residual: Compute \(u,v,q,P\) matrices for every nonzero row family.

- id: A1-220-06
  severity: 1
  status: healed
  lens: theta3 obstruction
  target: first supplied order-three source-face row
  claim: The theta3 row is solved by the current data.
  broken_step: The supplied complex has \(K^0=0\), \(K^1=\mathbb C E_{\theta_3}\),
    \(d=0\); \(\ell(E_{\theta_3})=1\) is a finite-row cokernel certificate.
  evidence_type: proof
  evidence_ref: main.tex:8232-8345; scripts/finite_window_graph_array.py:1513-1529
  minimal_heal: Demand a CE ancestor, local counterterm primitive, or complete
    companion-face table with scalar-zero and transport gates.
  residual: Non-exactness in the full local-functional complex is not proved.

- id: A1-220-07
  severity: 1
  status: healed
  lens: centrality homotopies
  target: unreduced closed-open centrality
  claim: Scalar shadow zero gives product and \(P_0\)-centrality.
  broken_step: A centrality row in the kernel still needs an explicit primitive
    \(H_{x,y}\) and transition identities; equivariantly it must be basic.
  evidence_type: line_reference
  evidence_ref: appendix-unreduced-bv-qme.tex:3316-3554;
    reconstitution/swarm-2026-04-30-agent-165-curved-bulk-defect-centrality-homotopy.md:73
  minimal_heal: State the centrality row formula, scalar gate, primitive
    equation, Roos class, and \(L_{V_\Omega}H\) obstruction.
  residual: Larger packages must supply graph/source/bracket/counterterm rows
    and homotopy primitives.
```

## Theta3 Decision

Current data remain obstructed as a finite-row subcomplex:
\[
  \mathsf E_{\theta_3,M}=-K^M_{\Theta_3}(\zeta_{M,\nu_3}),\qquad
  \ell_{\theta_3}(\mathsf E_{\theta_3,M})=1.
\]
The script accepts CE-ancestor and counterterm payloads only in interface
fixtures where the differential entry is explicitly \(-1\).  Those fixtures do
not assert present construction.  The Agent 215 companion-face attempt
(`reconstitution/swarm-2026-04-30-agent-215-theta3-companion-face-construction-attempt.md:7`)
supplies a
candidate source table shape, but not the required Costello row weights,
marker transports, signed zero sum, or lower-window cancellation.

## Files Changed

- `reconstitution/nonscalar-costello-qme-construction-frontier-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-220-nonscalar-costello-qme-construction-frontier.md`

## Verification

Commands to run from the repo root:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py >/tmp/finite-window-agent220.json
python3 -m json.tool /tmp/finite-window-agent220.json >/tmp/finite-window-agent220.pretty.json
rg -n "native-finite-window-realization-habitat|constructive-nonscalar-costello-qme-realization|theta-three-finite-window-acceptance-gate|app-qomega-centrality-homotopy-criterion" appendix-unreduced-bv-qme.tex main.tex
rg -n "theta_3_current_finite_row_subcomplex|theta3_ce_ancestor_supplied_exact_payload|theta3_complete_companion_faces_supplied_exact_payload" scripts/finite_window_graph_array.py
git diff --check -- reconstitution/nonscalar-costello-qme-construction-frontier-2026-04-30.md reconstitution/swarm-2026-04-30-agent-220-nonscalar-costello-qme-construction-frontier.md
grep -n '[[:blank:]]$' reconstitution/nonscalar-costello-qme-construction-frontier-2026-04-30.md reconstitution/swarm-2026-04-30-agent-220-nonscalar-costello-qme-construction-frontier.md
git add reconstitution/nonscalar-costello-qme-construction-frontier-2026-04-30.md reconstitution/swarm-2026-04-30-agent-220-nonscalar-costello-qme-construction-frontier.md
git diff --cached --check -- reconstitution/nonscalar-costello-qme-construction-frontier-2026-04-30.md reconstitution/swarm-2026-04-30-agent-220-nonscalar-costello-qme-construction-frontier.md
git status --short -- reconstitution/nonscalar-costello-qme-construction-frontier-2026-04-30.md reconstitution/swarm-2026-04-30-agent-220-nonscalar-costello-qme-construction-frontier.md
```

Observed results before staging:

- `py_compile` passed.
- Full script JSON emission and `json.tool` parsing passed.
- Focused script inspection kept
  `theta_3_current_finite_row_subcomplex` obstructed with obstruction value
  `1` and covector `E_theta_3 -> 1`.
- CE-ancestor and counterterm interface fixtures were accepted only with
  differential value `-1`.
- Incomplete and CE-unverified companion-face payloads were rejected; the
  complete interface fixture was accepted as interface-only.
- Anchor scans found the expected TeX labels and script cases.
- `git diff --check` passed on the two owned reports.
- Trailing-whitespace scan returned no hits.
