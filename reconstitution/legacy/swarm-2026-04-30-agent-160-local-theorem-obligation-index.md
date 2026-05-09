# Agent 160 Local Theorem-Obligation Index Report

Date: 2026-04-30.

Scope: write only
`reconstitution/local-theorem-obligations-2026-04-30.md` and this report.
No TeX manuscript files were edited.

## Evidence Loaded

- Repo and ecosystem instructions: `CLAUDE.md`, ecosystem invariants,
  attack-heal protocol, and Vol II rectification discipline.
- Control surface: `reconstitution/attack-heal-latest-2026-04-30.md`,
  `reconstitution/attack-heal-216-launch-manifest-2026-04-30.md`, and
  `reconstitution/swarm-live-launch-log-2026-04-30.md`.
- Local reports: Agents 069, 073, 074, 092--096, 099, 105, 118, 121,
  123, 130, 133, 139--151, 153--159, plus the relevant current TeX labels.

Agent 152's contracting-homotopy report and Agent 161's truncation-matrix
report are absent locally.  Agent 159's report is present locally but
untracked.  Agent 155 and Agent 156 reports, absent from Agent 157's read,
are now present and were incorporated.

## Valid Stale / Duplicate Obligations Found

- Compact/global fixture completion as a core obligation: stale for this
  paper.  It is quarantined as external comparison only.
- Agent 155/156 absence in the Agent 157 snapshot: stale.  Both reports are
  now locally present.
- Agent 159 live-only status in the launch log: stale locally.  The report is
  present, untracked, and leaves the VOA/OPE restriction theorem open.
- "No order-one scalar-zero row exists": false if labelled zero rows are
  retained.  Agent 153 supplies \(\alpha_{11}\) with
  \(\omega(z_1,z_1)=0\).  Nonzero order-one rows remain open.
- Minimal order-two/order-three finite-window uncertainty: stale after
  Agents 156 and 158.  The minimal full-equivariant package is all-order
  zero; larger packages still require actual graph data.
- Scalar cancellation as non-scalar QME theorem: false.  It is replaced by
  \(o_{\sigma,w}^{(r)}\) and
  \(H^1(\ker\widehat\sigma_{\mathrm{sc}},d_{\mathrm{QME}})\).
- Arbitrary \(\mathcal D'_c(I)\) graph theorem: false without new
  renormalization data; coincident delta labels are the counterexample.
- Wavefront smoothing into the regular-density branch: false.  The actual
  obstruction is \(\eta^{\mathrm{reg}}_{n_0,M}\); the primitive cone is an
  enlarged complex.
- All-\(N\) radial/Weyl trace theorem from finite checks: false.  The
  remaining datum is the moment-ideal/free-normal-form primitive.
- "Chiral" as a one-dimensional VOA/OPE result: false.  A complex-line or
  holomorphic-defect restriction tuple is still missing.

## Repairs Made

- Created `reconstitution/local-theorem-obligations-2026-04-30.md`.
- Collapsed duplicate QME, finite-window, wavefront, radial, and VOA items
  into ten finite local obligations.
- Incorporated Agent 155, 156, 158, and 159 evidence that postdates the
  Agent 157 latest snapshot.
- Kept compact-CY/CoHA/quintic/OSV/GV/Abel-Jacobi/MNOP/Vol III/Igusa/BKM
  out of the core list, with one external quarantine note.

## Final Finite Local Obligation List

1. Non-scalar quantum \(P_0\) / Costello QME realization.
2. Finite-window graph row arrays for larger packages.
3. Curved bulk-to-defect kernel and unreduced centrality homotopies.
4. Current-compatible Costello graph theorem for distributional labels.
5. Wavefront quotient exactness in the original complex.
6. Weighted Costello locality and analytic RG compatibility.
7. All-\(N\) radial/Weyl trace comparison.
8. Holomorphic-defect / complex-line restriction before VOA/OPE.
9. Tate/bar-cobar and mixed Koszul admissible envelopes.
10. Integration build and reference gate.

The detailed target theorem, proved branch, missing datum, obstruction
class, responsible surface, deciding evidence, and next lane for each item
are recorded in the index file.

## Files Changed / Staged

Changed by Agent 160:

- `reconstitution/local-theorem-obligations-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-160-local-theorem-obligation-index.md`

No TeX files were edited.

Staged after scoped verification:

- `reconstitution/local-theorem-obligations-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-160-local-theorem-obligation-index.md`

## Verification

Checks run:

```bash
git diff --check -- \
  reconstitution/local-theorem-obligations-2026-04-30.md \
  reconstitution/swarm-2026-04-30-agent-160-local-theorem-obligation-index.md

rg -n "[^\\x00-\\x7F]" \
  reconstitution/local-theorem-obligations-2026-04-30.md \
  reconstitution/swarm-2026-04-30-agent-160-local-theorem-obligation-index.md

# targeted compact/global import scan over the two owned files

git add -- \
  reconstitution/local-theorem-obligations-2026-04-30.md \
  reconstitution/swarm-2026-04-30-agent-160-local-theorem-obligation-index.md

git diff --cached --check -- \
  reconstitution/local-theorem-obligations-2026-04-30.md \
  reconstitution/swarm-2026-04-30-agent-160-local-theorem-obligation-index.md
```

Results: whitespace and cached-whitespace checks passed.  The ASCII scan
returned no hits after replacing the one non-ASCII name by `Hormander`.
Compact/global scans returned only stale-obligation or quarantine lines.
