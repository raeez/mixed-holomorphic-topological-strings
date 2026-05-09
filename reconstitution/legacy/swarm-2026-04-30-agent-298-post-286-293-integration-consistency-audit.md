# Agent 298 Post-286-293 Integration Consistency Audit

Status: report-only.  No TeX was edited.  No build was run.

Owned write paths:

- `reconstitution/post-286-293-integration-consistency-audit-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-298-post-286-293-integration-consistency-audit.md`

## Claim Attacked

After the BMK, theta3, LQT, radial, and stratified Weiss/Omega upgrades,
the control surface should contain no stale theorem strengths, parameter
collisions, missing ledger propagation, or Supremum-violating demotions.

## Result

Four issues remain.

1. BMK transfer language is stale.  `main.tex:2672-2676`,
   `theorem-lanes.tex:381-384`, `theorem-lanes.tex:472-514`, and
   `claim-strength-ledger.tex:319-325`, `608-625` still speak as if a
   finite-window BMK transfer/homotopy is proved.  The true post-286/292
   surface is current-limit data, finite Matlis moments, and arity-two
   output projection \(p_N[ix,iy]\), with strict finite-current transfer
   obstructed by \(\operatorname{Ob}^{\mathrm{BMK-curr}}_N\) and the
   escape-return Jacobi obstruction.

2. The LQT control files still mix the one-bound \(W\) abbreviation with
   separate \(K,L\) data.  `theorem-lanes.tex:2088-2113`,
   `open-obligations.tex:143-172`, and
   `claim-strength-ledger.tex:392-408` should use
   \(\Theta_{N,K,L}\), \(\lambda_{\mathrm{LQT},K,L}\), and
   \(N\ge\max(K,L+2)\) as the base theorem, with \(W\) only as a
   specialization.

3. The stratified Weiss component is not fully propagated as the Cech/Roos
   obstruction.  `theorem-lanes.tex:3120-3156`,
   `open-obligations.tex:1047-1050`, `open-obligations.tex:1147-1158`,
   and `claim-strength-ledger.tex:805-835` should replace the generic
   \(\delta_{\mathrm{Weiss}}\) vector entry by
   \(\delta_{\mathrm{Weiss}}^{\check C/R}\) and include both the cone
   cohomology and Roos compatibility class.

4. `open-obligations.tex:1319-1324` demotes the radial edge theorem to
   finite evidence through \(b=12\).  This should say the edge families
   \((2,b)\), \((b,2)\) are proved for all \(b\) by the PBW telescoping
   theorem, while the listed interior rows remain finite certificates.

## Cleared Checks

- The Omega/QME parameter collision at the QME residual is repaired in the
  current checkout: `theorem-lanes.tex:2971-2978` uses
  \(\hbar_{\mathrm{QME}}\).
- The theta3 lane is internally consistent with the no-\(B^2_{02,20}\)
  obstruction in the current habitat and the controlled-enlargement target:
  `main.tex:8625-8880`, `open-obligations.tex:731-878`, and
  `claim-strength-ledger.tex:480-514`, `861-918`.

Detailed proposed replacements are in
`reconstitution/post-286-293-integration-consistency-audit-2026-04-30.md`.
