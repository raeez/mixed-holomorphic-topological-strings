# Swarm Report, 2026-04-30, Agent 080

Lane: MNOP/quintic source fixture staged-vs-unstaged reconciliation.

Writable scope:

- `references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md`
- `references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-080-fixture-index-reconciliation.md`

No theorem file or manuscript source file was edited.

## Loaded Context

- `CLAUDE.md`
- `~/ecosystem/INVARIANTS.md` Section IV
- `~/ecosystem/AGENTS-HARNESS.md` Section VIII
- Agent 055 report:
  `reconstitution/swarm-2026-04-30-agent-055-mnop-pt-dt-fixture.md`
- Agent 056 report:
  `reconstitution/swarm-2026-04-30-agent-056-quintic-bcov-gv-fixture.md`
- Agent 075 materialization audit:
  `reconstitution/swarm-2026-04-30-agent-075-materialization-audit.md`
- Current staged and unstaged diffs for the two owned fixture files.

The Agent 055 and 056 reports were present, so no notification fallback was
needed.

## Staged vs Unstaged Diff Summary

Initial status on the owned fixtures was `AM` for both files.

Cached/index state:

- `references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md`
  was staged as a new Agent 055 fixture: 409 inserted lines.
- `references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md`
  was staged as a new Agent 056 fixture: 108 inserted lines.

Unstaged/worktree state:

- MNOP/PT/DT fixture: 84 changed lines, 42 additions and 42 deletions in
  substance. The worktree retargeted `frontier_mnop_framing_volume.tex`
  anchors from the pre-integration line map to the current frontier note,
  and updated the claim map so source fixtures and compact-target gaps match
  the post-Agent-065/070 file.
- Quintic BCOV/GV fixture: 44 changed lines, 23 additions and 21 deletions in
  substance. The worktree retargeted BCOV, arithmetic, conifold, mirror-period,
  and honest-status anchors to the current frontier note.

The unstaged edits were legitimate later integration work in direction, but
several worktree anchor ranges were still mislanded after the current frontier
line map changed. I tightened those ranges in the owned fixture files before
staging.

## Decision

Stage the full final fixture files, after correcting the line-anchor drift.

Reason: the unstaged modifications preserve Agent 055/056 source facts and
exact missing-source gaps, and they update stale frontier-note anchors to the
current post-integration file. The residual mislanded ranges were mechanical
index/worktree drift, not competing mathematical content.

No staged source fact was discarded. No unsupported theorem upgrade was added.

## Staging Performed

Staged only the owned paths:

- `references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md`
- `references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-080-fixture-index-reconciliation.md`

## Checks Run

```bash
git status --short -- references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md reconstitution/swarm-2026-04-30-agent-080-fixture-index-reconciliation.md
git diff --cached -- references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md
git diff -- references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md
rg -n "frontier_mnop_framing_volume\\.tex:[0-9]+(--|-)[0-9]+|frontier_mnop_framing_volume\\.tex:[0-9]+" references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md
git diff --check -- references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md reconstitution/swarm-2026-04-30-agent-080-fixture-index-reconciliation.md
git diff --cached --check -- references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md reconstitution/swarm-2026-04-30-agent-080-fixture-index-reconciliation.md
```

Both `git diff --check` and `git diff --cached --check` passed before final
staging. They were rerun after final staging and passed with no output.

## Files Changed

- Updated `references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md`
  to stage the legitimate post-integration anchor reconciliation with corrected
  current-line ranges.
- Updated
  `references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md`
  to stage the legitimate post-integration anchor reconciliation with corrected
  current-line ranges.
- Added this report.

## Residual Risk

The fixture anchors remain line-number anchors into a concurrently edited
standalone frontier note. Further edits to `frontier_mnop_framing_volume.tex`
can make them stale again.

The source fixtures still record absent local mirrors for MNOP/PT/DT PDFs,
HKQ, CDGP, GV, OSV, Strominger, Vafa/Schwinger, Shenker-Marino, and
Cecotti--Codesido--Marino. No line-level primary-source audit for those absent
mirrors was closed here.

This lane did not verify theorem files, did not build TeX, and did not alter
`main.tex`.
