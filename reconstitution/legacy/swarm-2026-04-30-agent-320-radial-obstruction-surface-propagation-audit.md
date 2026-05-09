# Agent 320: radial obstruction surface propagation audit

Date: 2026-04-30.

Owned write paths:

- `reconstitution/radial-obstruction-surface-propagation-audit-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-320-radial-obstruction-surface-propagation-audit.md`

No TeX or script file was edited.

## Loaded Context

Read `CLAUDE.md`, `AGENTS.md`, `~/ecosystem/INVARIANTS.md`,
`~/ecosystem/AGENTS-HARNESS.md`, and
`~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`.
Read the requested files:

- `appendix-radial-parts-moyal.tex`
- `main.tex`
- `theorem-lanes.tex`
- `open-obligations.tex`
- `claim-strength-ledger.tex`
- Agent 289 report
- Agent 296 report
- Agent 314 report

The checkout was already heavily dirty from concurrent agents.  I did not
revert, overwrite, stage, or edit any manuscript path.

## Claim Attacked

Every reader-facing radial/Weyl theorem surface should propagate Agent 314's
accepted theorem surface:
\[
  \Omega^{\mathrm{rad}}_{a,b}
  =
  [(T_{a,b},E^+_{a,b})]\in\operatorname{coker}B_{a,b},
\]
\[
  \Omega^{\mathrm{rad}}_{a,b}=0
  \quad\Longleftrightarrow\quad
  \text{decorated PBW Stokes vanishing for }
  D^\square_{a,b}=C^+_{a,b}\partial_2.
\]
Failure is exactly
\[
  (\phi,-\lambda)\in\ker B_{a,b}^*,
  \qquad
  \lambda(E^+_{a,b})-\phi(T_{a,b})\ne0.
\]

## Result

Status: partial propagation.  Core surfaces are repaired; secondary
reader-facing summaries remain stale.

Correctly propagated:

- `appendix-radial-parts-moyal.tex:965-1027`.
- `main.tex:2727-2749`.
- `theorem-lanes.tex:2525-2550`.
- `open-obligations.tex:1355-1437`.
- `claim-strength-ledger.tex:984-1043`.

Stale or incomplete surfaces:

- `appendix-radial-parts-moyal.tex:888-939`:
  Hodge theorem still states only \(\mathcal C_{a,b}\)-cokernel/harmonic
  projection.  Add \(\Omega^{\mathrm{rad}}\), \(B_{a,b}\), and signed-row
  equivalence.
- `appendix-radial-parts-moyal.tex:965-1027`:
  \(D^\square\) is named but the square-cell complex, ordinary cycle
  theorem \(\operatorname{im}\partial_2=\ker\partial\), and
  \(D^\square\)-left-cokernel criterion are not formally stated.
- `main.tex:1046-1064`:
  frontmatter quantum-data summary is still in \(\mathcal C_{a,b}\)
  splitting language.
- `main.tex:7379-7410`:
  theorem statement has signed row but omits
  \(\Omega^{\mathrm{rad}}\) and \(D^\square\).
- `main.tex:7552-7597`:
  degree-zero status remark omits the signed \(B^*\)-row and
  \(D^\square\) formulation.
- `main.tex:8219-8270`:
  `thm:phi-hbar-all-order` item (3) omits the accepted dual-potential
  obstruction surface.
- `main.tex:8372-8380`:
  componentwise coefficient surface still says homotopy or left-cokernel
  theorem only.
- `theorem-lanes.tex:2665-2674`:
  scope clause still uses old \(\operatorname{coker}\mathcal C\)
  obstruction language.
- `theorem-lanes.tex:2765-2771`:
  componentwise proof-input paragraph cites only the older radial gate.
- `theorem-lanes.tex:3634-3674`:
  radial trace-diagram theorem lane needs the full
  \(\Omega^{\mathrm{rad}}\)/\(D^\square\)/signed-row formulation.
- `open-obligations.tex:500-526`:
  componentwise theorem datum summary uses old splitting language.
- `claim-strength-ledger.tex:207-215`:
  top claim table's radial/Weyl row omits the accepted obstruction surface.
- `claim-strength-ledger.tex:300-308`:
  radial trace-diagram branch row uses old homotopy/left-cokernel language.
- `claim-strength-ledger.tex:577-585`:
  frontier item "Radial all-N image and all-bidegree homotopy" uses old
  \(\mathcal C\)-only phrasing.
- `claim-strength-ledger.tex:1238-1270`:
  quantum Hamiltonian/Moyal sector item omits the dual-potential and
  \(D^\square\) gate.

## Patch Target

Patch the stale surfaces to use the same normal form:

\[
  B_{a,b}(W)=(\partial W,C^+_{a,b}(W)),\qquad
  \eta_{a,b}=(T_{a,b},E^+_{a,b}),
\]
\[
  \Omega^{\mathrm{rad}}_{a,b}=[\eta_{a,b}]\in\operatorname{coker}B_{a,b}.
\]
Then state:

1. Positive closure is \(\Omega^{\mathrm{rad}}_{a,b}=0\) for all
   bidegrees.
2. Equivalently, after the ordinary square-cell cycle mechanism,
   the decorated PBW Stokes map
   \(D^\square_{a,b}=C^+_{a,b}\partial_2\) has no residual left-cokernel
   value on \(R^{\mathrm{free}}_{a,b}\).
3. Failure is exactly a signed row
   \((\phi,-\lambda)\in\ker B_{a,b}^*\) with
   \(\lambda(E^+_{a,b})-\phi(T_{a,b})\ne0\).

## Commands Run

- `wc -l` on the requested TeX files and reports.
- `nl -ba` on the requested TeX files and reports.
- `rg` for radial/Weyl, \(\Omega^{\mathrm{rad}}\), \(D^\square\),
  \(\mathcal C_{a,b}\), left-cokernel, and signed-row language.
- `git status --short`.

No build was run because the task forbade TeX edits and requested report
files only.

## Files Changed

- `reconstitution/radial-obstruction-surface-propagation-audit-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-320-radial-obstruction-surface-propagation-audit.md`
