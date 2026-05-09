# Agent 074 Quantum Surface Propagation Report

## Sections Attacked

- `theorem-lanes.tex`: quantum theorem lane around the degree-zero
  Moyal/Weyl sector and the new componentwise quantum coefficient
  surface.
- `claim-strength-ledger.tex`: admissibility stages, status table, and
  theorem-data ledger.
- `open-obligations.tex`: mixed brane-defect QME and obstruction-complex
  control surface.

## Exact Edits

- Added a theorem-lane statement for
  `thm:quantum-coefficient-surface`, with status ``proved
  componentwise; non-scalar obstruction problem open''.
- Recorded the four proved components:
  weighted BV coefficient-kernel convergence and graphwise boundedness;
  balanced-supertrace scalar QME cancellation; reduced weighted Moyal
  principal-part current brackets; and the conditional degree-zero
  Moyal trace comparison.
- Replaced stale degree-zero wording that left the Moyal principal-part
  target merely isolated from the theorem surface.  The degree-zero lane
  now points to the componentwise theorem while preserving the exclusion
  of polynomial one-\(\psi\) transport.
- Split ledger Stage A6 into A6a, the proved componentwise quantum
  coefficient surface, and A6b, the open non-scalar Costello/QME
  construction problem.
- Replaced the status-table row for conditional Costello graph/QME
  realization with a proved componentwise quantum coefficient row and an
  open non-scalar construction row.
- Added the named obstruction complex
  \(\mathfrak Q^\bullet_{w,\partial,\hbar}(I)\), scalar projection
  \(\widehat\sigma_{\mathrm{sc}}\), and non-scalar class
  \[
    [\operatorname{Ob}^{\mathrm{red}}_{w,\partial,\hbar}]
      \in
      H^1(\ker\widehat\sigma_{\mathrm{sc}},d_{\mathrm{QME}})
  \]
  to both the theorem lane and open-obligations surface.

## Theorem-Status Recommendation

Promote `thm:quantum-coefficient-surface` as a proved componentwise
quantum coefficient theorem.  Do not promote it to a graph-level
non-scalar Costello/QME construction.

The next theorem obligation is precise: construct the filtered
local-functional complex, scalar-contact filtration and projection,
finite-window counterterms, and bulk-to-defect kernel, then prove that
the non-scalar obstruction class vanishes.

## Files Changed

- `theorem-lanes.tex`
- `claim-strength-ledger.tex`
- `open-obligations.tex`
- `reconstitution/swarm-2026-04-30-agent-074-quantum-surface-propagation.md`

## Checks Run

- `git diff --check -- theorem-lanes.tex claim-strength-ledger.tex open-obligations.tex`: clean.
- `git diff --check`: clean.
- `git diff --cached --check`: clean after staging owned paths.
- Targeted stale greps for the old conditional-realization surface:
  no matches.
- Targeted positive greps for the componentwise surface and obstruction
  class: intended hits only.

## Remaining Proof Obligations

- Construct \(\operatorname{Ob}_{w,\partial,\hbar}\) in
  \(\mathfrak Q^\bullet_{w,\partial,\hbar}(I)\) with zero scalar
  projection in the balanced supertrace branch.
- Construct compatible finite-window local counterterms
  \(C_{\Gamma,w}^{w_0}(\epsilon)\).
- Construct the curved bulk-to-defect kernel \(\kappa_{\hbar,w}\).
- Prove finite-window compatibility and kill
  \([\operatorname{Ob}^{\mathrm{red}}_{w,\partial,\hbar}]\) in
  \(H^1(\ker\widehat\sigma_{\mathrm{sc}},d_{\mathrm{QME}})\).
