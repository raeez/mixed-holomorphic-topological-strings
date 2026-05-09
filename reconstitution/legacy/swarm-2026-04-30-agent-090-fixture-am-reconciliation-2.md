# Swarm Report, 2026-04-30, Agent 090

Lane: second-stage MNOP/quintic fixture `AM` reconciliation after Agent 086.

Write ownership:

- `references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md`
- `references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-090-fixture-am-reconciliation-2.md`

No theorem file or manuscript source file was edited.

## Loaded Context

- `CLAUDE.md`.
- `~/ecosystem/INVARIANTS.md` Section IV.
- `~/ecosystem/AGENTS-HARNESS.md` Section VIII.
- Agent 080 report:
  `reconstitution/swarm-2026-04-30-agent-080-fixture-index-reconciliation.md`.
- Agent 086 report:
  `reconstitution/swarm-2026-04-30-agent-086-source-fixture-consistency-audit.md`.
- Current staged and unstaged diffs for the two owned fixture files.
- Live line-map spot checks in `frontier_mnop_framing_volume.tex`.

## Staged vs Unstaged Diff Summary

Initial owned-fixture status was `AM` for both source fixtures.

Cached/index state:

- `references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md`
  was staged as a new source fixture with 411 inserted lines.
- `references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md`
  was staged as a new source fixture with 108 inserted lines.

Unstaged/worktree state:

- MNOP/PT/DT fixture: two line-anchor repairs, both
  `frontier_mnop_framing_volume.tex:762--769 -> 759--769`.
  The live file has `\section{Honest-status summary}` at line 759 and the
  first enumerated MNOP item at lines 761--769.
- Quintic BCOV/GV fixture: one line-anchor repair in the
  `BCOV-quintic-table` row,
  `frontier_mnop_framing_volume.tex:233-256 -> 244-256`.
  The live file has contextual firewall prose at lines 233--243 and the
  displayed numerical table at lines 244--256.

No unstaged hunk changed a source fact, missing-local-fixture obligation,
theorem status, firewall statement, or non-support boundary.

## Decision

Stage the unstaged fixture repairs.

Reason: Agent 086 identified these exact working-tree deltas as mechanical and
plausible, with staging deferred to an owning integration lane. The live line
map verifies them. They preserve the final source facts and exact gaps while
resolving the index/worktree mismatch.

No conflict was found.

## Staging Performed

Staged only owned paths:

- `references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md`
- `references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-090-fixture-am-reconciliation-2.md`

## Checks Run

```bash
git status --short -- references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md reconstitution/swarm-2026-04-30-agent-090-fixture-am-reconciliation-2.md
git diff -- references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md
git diff --cached -- references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md
git diff --check -- references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md reconstitution/swarm-2026-04-30-agent-090-fixture-am-reconciliation-2.md
git diff --cached --check -- references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md reconstitution/swarm-2026-04-30-agent-090-fixture-am-reconciliation-2.md
nl -ba frontier_mnop_framing_volume.tex | sed -n '225,260p'
nl -ba frontier_mnop_framing_volume.tex | sed -n '755,772p'
git add references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md
git add reconstitution/swarm-2026-04-30-agent-090-fixture-am-reconciliation-2.md
```

The pre-stage `git diff --check` and `git diff --cached --check` on owned paths
passed with no output. The final post-stage checks on owned paths passed with
no output.

## Residual Risk

The fixture anchors are line-number anchors into a concurrently edited
standalone frontier note. Later edits to `frontier_mnop_framing_volume.tex`
can stale them again.

The source gaps remain exactly as recorded: MNOP/PT/DT local mirrors are
absent; HKQ, CDGP, GV, OSV, Strominger, Vafa/Schwinger, Shenker-Marino, and
Cecotti--Codesido--Marino local fixtures are absent. No compact-CY transfer,
global BCOV/GV closure, `F_X`, trace-map, `sigma_Q`, or
`Ob_UKD(C_tar)` null-homotopy is supplied here.
