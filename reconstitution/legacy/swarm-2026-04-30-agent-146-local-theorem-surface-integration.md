# Agent 146 Local Theorem-Surface Integration

Date: 2026-04-30.

Owned writable surface: `theorem-lanes.tex`, `claim-strength-ledger.tex`,
and this report.  No subagents were launched.  The checkout already had
staged and unstaged swarm edits in the first two files; this pass edited
on top of the current working tree and did not revert or stage other work.

## Evidence Read

Loaded `CLAUDE.md`, `AGENTS.md`, the ecosystem attack-heal protocol, the
Vol II chriss-ginzburg-rectify discipline, `main.tex`, `abstract.tex`,
`local-dictionary.tex`, `tate-T1-weighted-completion.tex`,
`tate-P1-hadamard-mittag-leffler.tex`,
`appendix-unreduced-bv-qme.tex`,
`appendix-factorization-current-conventions.tex`, and available reports
136, 137, 138, 139, and 141.

Reports 140 and 142--145 were not present under the permitted report
pattern in this checkout.  They were not used as evidence.

## Stable Core

The integrated theorem surface remains the formal-local mixed HT theory on
\[
  \mathbb R^2_{\mathrm{top}}\times
  \widehat{\mathbb C^2}_{0,\mathrm{hol}} .
\]
Compact Calabi--Yau, CoHA, quintic, OSV/GV, Abel--Jacobi, Igusa, BKM, and
global BCOV material is external comparison only.

Local branch statuses now recorded:

- Balanced scalar-contact projection: proved on balanced scalar-contact
  habitats and balanced graph/counterterm subhabitats; obstruction outside
  them is the first nonzero \(o_{\sigma,w}^{(r)}(I)\).
- Full-equivariant scalar shadow: proved on codimension-two closed
  finite-window marked Costello habitats with full-equivariant Brauer
  markers; missing boundary table, signs, marker transports, or closure
  equations block the theorem.
- Finite closed graph list: a conditional finite-window closure datum,
  not an all-graph summation theorem.
- Finite-window array order \(0/1\): order \(0\) row is zero; the
  one-cross scalar-contact row is computed; the minimal full-equivariant
  closed array has \(R^{\mathrm{ns}}_{1,M}=0\) and \(C_{1,M}=0\).  Larger
  packages are decided by the remaining row sum and its \(H^1\)/Roos
  classes.
- Regular-density curvature certificate: proved under the regular-density
  package certificate; the regular branch then has
  \(\eta,\kappa,\beta,\mu,\lambda=0\).  Without the certificate the exact
  obstruction is \(\eta^{\mathrm{reg}}_{n_0,M}\), then
  \(\kappa^{\mathrm{reg}}_{n_0}\).
- Wavefront eta branch: obstruction theorem.  Non-smooth wavefront labels
  survive in \(\mathcal D'_c(I)/\mathcal D^{\mathrm{reg}}_c(I)\); the
  obstruction is
  \(\eta^{\mathrm{reg}}_{n_0,M}=
  [\mathfrak s^{\mathrm{WF}}_{n_0,M}]\), killed only by a degree-zero
  distributional primitive in the original quotient complex.
- Radial trace-diagram branch: formal Moyal coefficients and reduced
  open-line Wick weights are proved; all-\(N\) trace normalization remains
  the moment-ideal primitive problem
  \(E_{a,b,N}=\sum_{i,j}A^j{}_i(a,b,N)\widehat\mu^i{}_j\).

## Valid Attacks

`A146-01` Severity 2.  The componentwise quantum surface still read as if
balanced supertrace only killed the scalar symbol while the filtered
scalar projection remained entirely open.  Valid.  Healed by recording
the proved balanced scalar-contact, balanced graph/counterterm, and
full-equivariant finite-marked habitats.

`A146-02` Severity 2.  The finite graph and array lanes could be read as a
closed all-graph Costello package.  Valid.  Healed by separating the
finite closed graph list as a conditional closure datum and the finite
array as order \(0/1\) computed rows only.

`A146-03` Severity 1.  Regular-density and wavefront-labelled branches
could be conflated.  Valid.  Healed by putting the regular-density
certificate on the proved side and the wavefront quotient class
\(\eta^{\mathrm{reg}}_{n_0,M}\) on the obstruction side.

`A146-04` Severity 2.  The degree-zero Moyal/Weyl branch could be read as
an unconditional all-\(N\) radial trace theorem.  Valid.  Healed by naming
the exact radial trace-diagram obstruction as the class of \(E_{a,b,N}\)
in the chosen quantum moment-map quotient.

`A146-05` Severity 2.  The local branch catalogue needed an explicit
firewall against compact-CY/global comparison import.  Valid.  Healed by
stating the local geometry and external-comparison exclusions in the new
theorem-lane statement.

## Repairs Made

- Added `thm:lane-local-graph-qme-branch-catalogue` to
  `theorem-lanes.tex`.
- Added a `Local graph/QME branch statuses` table to
  `claim-strength-ledger.tex`.
- Upgraded the componentwise quantum coefficient surface ledger entry so
  the proved scalar-shadow habitats are not left as an open scalar-lift
  problem.

## Labels / Statuses Changed

- `thm:lane-local-graph-qme-branch-catalogue`: new local branch catalogue.
- Balanced scalar-contact projection: `proved on named habitats`.
- Full-equivariant marked scalar shadow: `proved on finite marked habitats`.
- Finite closed graph list: `conditional finite-window datum`.
- Finite-window array order \(0/1\): `proved for computed rows`.
- Regular-density curvature certificate: `proved under certificate`.
- Wavefront eta branch: `obstruction theorem`.
- Radial trace-diagram branch: `external-input-relative obstruction`.

## Verification

Commands run:

```bash
rg --files | rg '(^|/)(main|abstract|local-dictionary|theorem-lanes|claim-strength-ledger|tate-(T1|P1)|appendix-unreduced-bv-qme|appendix-factorization-current-conventions)\.tex$|^reconstitution/swarm-2026-04-30-agent-(13[6-9]|14[0-5]).*\.md$'
rg -n "balanced|full-equivariant|finite-window|regular-density|wavefront|eta|radial|scalar projection|array|curvature certificate" theorem-lanes.tex claim-strength-ledger.tex main.tex tate-T1-weighted-completion.tex tate-P1-hadamard-mittag-leffler.tex appendix-unreduced-bv-qme.tex appendix-factorization-current-conventions.tex
git diff --check -- theorem-lanes.tex claim-strength-ledger.tex
rg -n "local graph/QME branch catalogue|Local graph/QME branch statuses|Radial trace-diagram|Wavefront eta|Regular-density curvature|Full-equivariant scalar shadow|Finite-window array" theorem-lanes.tex claim-strength-ledger.tex
pdflatex -halt-on-error -interaction=nonstopmode -draftmode -output-directory=/tmp/topological-strings-agent146-build main.tex
```

Results:

- `git diff --check` passed.
- The label/status scan found the new theorem-lane and ledger rows.
- The `/tmp` draft `pdflatex` pass exited with status 0.  It reports
  ordinary one-pass undefined-reference warnings and nonfatal
  underfull/overfull box warnings; no fatal TeX error was introduced.

## Remaining Local Obligations

- Populate finite marked Costello seed sets, boundary tables, incidence
  signs, marker transports, and codimension-two closure equations for any
  larger graph package.
- Fill finite-window array rows beyond the order \(0\) current row and
  the order \(1\) scalar-contact row, including truncation matrices.
- Compute the non-scalar \(H^1\) and \(\varprojlim^1H^0\) obstruction
  classes for larger packages.
- For non-regular labels, decide whether
  \(\eta^{\mathrm{reg}}_{n_0,M}\) is a boundary in the original
  distributional quotient complex; adjoining the primitive cone is an
  extension, not a repair inside the original complex.
- Construct the all-\(N\) moment-ideal primitive for \(E_{a,b,N}\), or
  keep the radial trace comparison external-input-relative.
- Construct the curved bulk-to-defect kernel, centrality homotopies,
  bracket homotopies, and compatible finite-window counterterms needed to
  kill
  \([\operatorname{Ob}^{\mathrm{red}}_{w,\partial,\hbar}]\) in
  \(H^1(\ker\widehat\sigma_{\mathrm{sc}},d_{\mathrm{QME}})\).
