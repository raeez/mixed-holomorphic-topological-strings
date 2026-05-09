# Agent 138 CoHA / Compact-CY Quarantine Report

## Scope

Writable surface: `claim-strength-ledger.tex`,
`open-obligations.tex`, and this report.

Read-only context used: `CLAUDE.md`, ecosystem attack-heal protocol,
Vol II `chriss-ginzburg-rectify` discipline,
`references/source-provenance.md`, and
`frontier_mnop_framing_volume.tex`.

Stable core: the active theorem surface is the formal-local mixed HT
theory on \(\mathbb R^2_{\mathrm{top}}\times\mathbb C^2_{\mathrm{hol}}\).
CoHA, compact Calabi--Yau, quintic, OSV/GV, Abel--Jacobi, MNOP,
Igusa/BKM, and global BCOV material is external comparison data only.

## Valid Attacks

`A1-138-01`

Severity: 2.
Target: `claim-strength-ledger.tex` proof route and status table.
Claim attacked: the firewall row was sufficient for compact-CY/CoHA
import.
Broken step: the ledger named compact Calabi--Yau, Vol III, Igusa/BKM,
and global BCOV, but did not explicitly quarantine CoHA, quintic, OSV/GV,
Abel--Jacobi, or MNOP from the local QME, Ext, cyclic, Weyl/Moyal,
radial-parts, and kernel theorem surfaces.
Evidence: `rg` hits before repair showed the firewall at the proof route
and final descent row but no full non-support sentence for these core
local theorem surfaces.
Minimal heal: add an explicit external-comparison quarantine and bind it
to the local theorem surfaces.
Status: healed.

`A1-138-02`

Severity: 3.
Target: `claim-strength-ledger.tex` Stage A7.
Claim attacked: the external matched-conventions descent row could be
read as a local-stage continuation.
Broken step: Stage A7 said only that it was not a consequence of local
stages; it did not say that the row is a quarantine gate rather than a
core proof prerequisite.
Minimal heal: state that A7 rows are quarantine gates, not prerequisites
for the core local theorem.
Status: healed.

`A1-138-03`

Severity: 2.
Target: `open-obligations.tex` introduction and global descent row.
Claim attacked: missing compact-target source fixtures could be mistaken
for core open obligations.
Broken step: the open-obligation surface described frontier extensions
and target descent, but did not front-load that compact-CY/CoHA lanes are
external comparison only and cannot support the local theorem.
Minimal heal: add a non-core obligation sentence at the top and repeat it
in the global descent row.
Status: healed.

## Repairs Made

`claim-strength-ledger.tex`

- Lines 57--63 now add an `External-comparison quarantine`: CoHA,
  compact Calabi--Yau/quintic, OSV/GV, Abel--Jacobi, MNOP, Igusa/BKM,
  and global BCOV data are external only.
- Lines 75--79 now say no such external claim supports or follows from
  the local QME, Ext, cyclic, Weyl/Moyal, radial-parts, or kernel theorem
  surface without a matched-conventions descent theorem.
- Lines 117--119 now make Stage A7 a quarantine gate, not a core local
  prerequisite.
- Lines 208--213 replace the old compact-CY fixture split status row by
  a compact-CY/CoHA external-comparison row with no transfer theorem.
- Lines 532--540 now require null-homotopies and comparison morphisms
  before any CoHA, compact BCOV, quintic, OSV/GV, Abel--Jacobi, MNOP,
  Vol III, Igusa/BKM, or global Calabi--Yau consequence is deduced.

`open-obligations.tex`

- Lines 9--13 now state that external compact Calabi--Yau, CoHA,
  quintic, OSV/GV, Abel--Jacobi, MNOP, Igusa, BKM, and global BCOV
  material is not a core local obligation.
- Lines 567--576 now state that external target theorems may use the
  formal-local theorem only after target obstruction, null-homotopy, and
  comparison-morphism data are supplied; missing external fixtures do not
  support the local QME, Ext, cyclic, Weyl/Moyal, radial-parts, or kernel
  theorem surfaces.

## Files Changed / Staged

- `claim-strength-ledger.tex`: modified. It already had staged changes
  on entry; Agent 138's delta is unstaged.
- `open-obligations.tex`: modified. It already had staged changes on
  entry; Agent 138's delta is unstaged.
- `reconstitution/swarm-2026-04-30-agent-138-coha-compactcy-quarantine.md`:
  added, unstaged.

No files were staged by Agent 138.

## Verification

- `git diff --check -- claim-strength-ledger.tex open-obligations.tex`:
  passed with no whitespace errors.
- `rg -n "CoHA|compact|quintic|OSV|GV|Abel|Igusa|BKM|MNOP|global BCOV|local QME, Ext, cyclic" claim-strength-ledger.tex open-obligations.tex`:
  verified the quarantine terms and local non-support rule on both
  surfaces.
- `pdflatex -halt-on-error -interaction=nonstopmode -draftmode -output-directory=/tmp/agent138-tex main.tex`:
  passed with exit code 0.  The draft pass reports ordinary unresolved
  references from the one-pass build and overfull hboxes outside the
  edited ledger/open-obligation lines.

## Remaining Obligations

No remaining Agent 138 repair is inside the assigned writable surface.

External matched-conventions theorems, compact-CY source fixtures,
Abel--Jacobi normalisations, conifold/Stokes rows, CoHA/centre
constructions, and Igusa/BKM comparisons remain external comparison
obligations only.  They are not core work for the
\(\mathbb R^2_{\mathrm{top}}\times\mathbb C^2_{\mathrm{hol}}\) local
QME, Ext, cyclic, Weyl/Moyal, radial-parts, or kernel theorem surface.
