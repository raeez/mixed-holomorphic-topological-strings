# Swarm Report, 2026-04-30, Agent 091

Lane: tiny frontier wording repair after CoHA fixture narrowing.

Writable scope:

- `frontier_mnop_framing_volume.tex`, only the stale CoHA-fixture
  description lines around 64 and 240.
- `reconstitution/swarm-2026-04-30-agent-091-frontier-coha-wording-repair.md`

## Inputs Loaded

- `CLAUDE.md`.
- `~/ecosystem/INVARIANTS.md`, Section IV.
- `~/ecosystem/AGENTS-HARNESS.md`, Section VIII.
- `reconstitution/swarm-2026-04-30-agent-089-coha-fixture-narrowing.md`.
- `references/primary-sources/coha-center-source-anchors-2026-04-30.md`.
- `frontier_mnop_framing_volume.tex:54-70`.
- `frontier_mnop_framing_volume.tex:230-250`.

## Exact Edits

- `frontier_mnop_framing_volume.tex:61-65`: replaced the claim that the
  reconstructed CoHA/centre row supplies the
  `HKQ/CDGP/OSV/GV chiral-volume comparison rows` with the narrowed
  statement that it supplies only Hall/CoHA/centre vocabulary and stable
  identifiers: Lurie centre grammar, Joyce/Gross--Joyce--Tanaka
  Hall--vertex structures, and Joyce--Upmeier/Kinjo--Park--Safronov
  orientation/CoHA prerequisites. Added that HKQ, CDGP, OSV, and GV data
  require separate domain fixtures.
- `frontier_mnop_framing_volume.tex:241-243`: replaced the claim that the
  CoHA/centre fixture records the same HKQ/CDGP/OSV/GV rows as stable
  identifiers and adds the `N_{\AJ}` and
  `Ob_UKD(C_tar)` firewalls with the narrowed statement that it records
  only Hall/CoHA/centre vocabulary and its non-import firewall, not HKQ,
  CDGP, OSV, or GV data. Added that those data require separate domain
  fixtures.

No theorem status, conditional numerical table, or broader compact-CY
frontier claim was changed.

## Checks Run

- `git diff --check`: clean.
- `git diff --cached --check -- frontier_mnop_framing_volume.tex reconstitution/swarm-2026-04-30-agent-091-frontier-coha-wording-repair.md`:
  clean after staging owned paths.
- `rg -n -e 'HKQ/CDGP/OSV/GV' -e 'chiral-volume comparison rows' -e 'records the same HKQ' frontier_mnop_framing_volume.tex references/primary-sources/coha-center-source-anchors-2026-04-30.md`:
  no hits.
- `pdflatex -output-directory="$TMPDIR" -interaction=nonstopmode -halt-on-error frontier_mnop_framing_volume.tex`:
  passed in a temporary directory. Existing hyperref, underfull/overfull,
  rerun, and unresolved-reference warnings remain; no fatal TeX error.

## Files Changed

- `frontier_mnop_framing_volume.tex`.
- `reconstitution/swarm-2026-04-30-agent-091-frontier-coha-wording-repair.md`.

## Residual Risk

- Separate HKQ, CDGP, OSV, GV, Abel--Jacobi, and compact BCOV source
  fixtures remain open obligations outside this lane.
- The edited frontier file still contains broader conjectural compact-CY
  target data. This lane only repaired stale CoHA-fixture wording after
  the fixture narrowing.
