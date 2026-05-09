# Swarm Report, 2026-04-30, Agent 075

Lane: notified-report/file materialization audit after source fixture
mismatches.

Writable scope:

- `reconstitution/swarm-2026-04-30-agent-075-materialization-audit.md`

No theorem file, manuscript source file, source fixture, control document, or
provenance ledger was edited.

## Scope

This is a materialization audit only.  It checks whether the reports and files
named by the launch log, Agent 064, Agent 065, and the current notification
lane are present in this checkout and index.  It does not reconstruct missing
content and does not adjudicate the mathematics of any fixture.

Target set:

- Agent 018 report.
- Agent 049 report.
- Agent 054 report.
- Agent 055 report and MNOP/PT/DT fixture.
- Agent 056 report and quintic BCOV/GV fixture.
- Agent 057 report and CoHA/center fixture.
- Agent 063, 064, and 065 reports.
- Recovery-lane materialization for Agent 070 CoHA reconstruction and Agent
  071 legacy-archive reconciliation.
- Legacy figure archive evidence: archive README and six `firstorder` /
  `thirdorder*` assets.

## Commands Run

```bash
sed -n '1,240p' CLAUDE.md
sed -n '1,260p' reconstitution/swarm-live-launch-log-2026-04-30.md
nl -ba reconstitution/swarm-live-launch-log-2026-04-30.md | sed -n '240,620p'
nl -ba reconstitution/swarm-live-launch-log-2026-04-30.md | sed -n '380,435p'
git status --short
git status --short --untracked-files=all -- reconstitution/swarm-live-launch-log-2026-04-30.md
find reconstitution -maxdepth 3 -type f -print | sort
find references/primary-sources -maxdepth 3 -type f -print | sort
sed -n '1,240p' reconstitution/swarm-2026-04-30-agent-055-mnop-pt-dt-fixture.md
sed -n '1,240p' reconstitution/swarm-2026-04-30-agent-056-quintic-bcov-gv-fixture.md
sed -n '1,220p' reconstitution/swarm-2026-04-30-agent-063-source-provenance-fixtures-assets.md
sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-064-source-provenance-correction.md
sed -n '1,280p' reconstitution/swarm-2026-04-30-agent-065-frontier-fixture-integration.md
sed -n '1,220p' reconstitution/swarm-2026-04-30-agent-070-coha-fixture-reconciliation.md
sed -n '1,240p' reconstitution/swarm-2026-04-30-agent-071-legacy-archive-reconciliation.md
find reconstitution -maxdepth 1 -type f \( -name '*agent-018*' -o -name '*agent-049*' -o -name '*agent-054*' -o -name '*agent-057*' -o -name '*agent-053*' -o -name '*agent-060*' -o -name '*agent-070*' -o -name '*agent-071*' -o -name '*agent-075*' \) -print | sort
find references -maxdepth 5 -type f \( -iname '*coha*' -o -iname '*center*' -o -iname '*centre*' -o -iname '*legacy*' -o -iname '*feynman*' -o -iname '*mnop*' -o -iname '*quintic*' \) -print | sort
find references/legacy-figure-assets/2018-feynman-diagram-sketches -maxdepth 1 -type f -print | sort
find . -maxdepth 1 -type f \( -name 'firstorder.*' -o -name 'thirdordera.*' -o -name 'thirdorderb.*' \) -print | sort
git status --porcelain=v1 --untracked-files=all -- <target report and fixture paths>
git status --short --untracked-files=all -- <target report and fixture paths>
git ls-files --stage -- <target report and fixture paths>
git diff --cached --name-status -M -- <target report and fixture paths>
git diff --name-status -- <target report and fixture paths>
rg -n "Agent 0?(18|49|54|57|70|71)|agent-0?(18|49|54|57|70|71)|CoHA|coha|centre|center|legacy archive|legacy figure" reconstitution/swarm-live-launch-log-2026-04-30.md reconstitution/swarm-2026-04-30-agent-064-source-provenance-correction.md reconstitution/swarm-2026-04-30-agent-065-frontier-fixture-integration.md reconstitution/swarm-2026-04-30-agent-070-coha-fixture-reconciliation.md reconstitution/swarm-2026-04-30-agent-071-legacy-archive-reconciliation.md references/source-provenance.md
```

One early variant-path probe also checked noncanonical shorthand names such as
`agent-049-coha-centre-fixture`, `agent-054-legacy-archive-evidence`, and
`agent-057-coha-centre-fixture`.  Those variants were absent.  The table below
uses the exact launch-log paths where the launch log gives one.

## Present/Absent Table

Snapshot basis: `git status --short --untracked-files=all`, targeted
`find`, targeted `git ls-files --stage`, and targeted cached/unstaged diffs.
The checkout is concurrent; this table records the state observed immediately
before writing this report.

| Item | Launch-log or report expectation | Filesystem state | Index/status state | Audit result |
|---|---|---:|---:|---|
| Launch log | `reconstitution/swarm-live-launch-log-2026-04-30.md` | Present | `??` untracked | Present but not in index. It changed during this audit: Agent 070 is now closed with report path; Agent 071 remains live. |
| Agent 018 report | `reconstitution/swarm-2026-04-30-agent-018-mnop-firewall.md` | Absent | Not in index; no status line | Launch log says completed, but no local report materialized. |
| Agent 049 report | `reconstitution/swarm-2026-04-30-agent-049-mnop-source-fixture-audit.md` | Absent | Not in index; no status line | Launch log says completed, but no local report materialized. |
| Agent 054 report | `reconstitution/swarm-2026-04-30-agent-054-mnop-source-fixture-plan.md` | Absent | Not in index; no status line | Launch log says completed, but no local report materialized. |
| Agent 055 report | `reconstitution/swarm-2026-04-30-agent-055-mnop-pt-dt-fixture.md` | Present | `A` staged add | Materialized locally. |
| Agent 055 MNOP/PT/DT fixture | `references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md` | Present | `AM` staged add plus unstaged modifications | Materialized, but index and worktree differ. |
| Agent 056 report | `reconstitution/swarm-2026-04-30-agent-056-quintic-bcov-gv-fixture.md` | Present | `A` staged add | Materialized locally. |
| Agent 056 quintic fixture | `references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md` | Present | `AM` staged add plus unstaged modifications | Materialized, but index and worktree differ. |
| Agent 057 report | `reconstitution/swarm-2026-04-30-agent-057-coha-center-fixture.md` | Absent | Not in index; no status line | Original Agent 057 report remains missing. |
| Agent 057 CoHA/center fixture | `references/primary-sources/coha-center-source-anchors-2026-04-30.md` | Present | `A` staged add | Now materialized by Agent 070 reconstruction, not by an Agent 057 report. |
| Agent 063 report | `reconstitution/swarm-2026-04-30-agent-063-source-provenance-fixtures-assets.md` | Present | `A` staged add | Materialized locally. |
| Agent 064 report | `reconstitution/swarm-2026-04-30-agent-064-source-provenance-correction.md` | Present | `A` staged add | Materialized locally. |
| Agent 065 report | `reconstitution/swarm-2026-04-30-agent-065-frontier-fixture-integration.md` | Present | `A` staged add | Materialized locally. |
| Agent 070 report | `reconstitution/swarm-2026-04-30-agent-070-coha-fixture-reconciliation.md` | Present | `A` staged add | Recovery-lane report materialized; launch log now records Agent 070 closed. |
| Agent 071 report | `reconstitution/swarm-2026-04-30-agent-071-legacy-archive-reconciliation.md` | Present | `A` staged add | Recovery-lane report materialized even though launch log still records Agent 071 live. |
| Legacy archive README | `references/legacy-figure-assets/2018-feynman-diagram-sketches/README.md` | Present | `A` staged add | Legacy archive evidence now present through Agent 071. |
| Legacy asset `firstorder.png` | root path to archive path | Archive path present; root file absent from worktree | `R100 firstorder.png -> references/legacy-figure-assets/2018-feynman-diagram-sketches/firstorder.png` staged | Materialized as content-preserving staged rename. |
| Legacy asset `firstorder.svg` | root path to archive path | Archive path present; root file absent from worktree | `R100 firstorder.svg -> references/legacy-figure-assets/2018-feynman-diagram-sketches/firstorder.svg` staged | Materialized as content-preserving staged rename. |
| Legacy asset `thirdordera.png` | root path to archive path | Archive path present; root file absent from worktree | `R100 thirdordera.png -> references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdordera.png` staged | Materialized as content-preserving staged rename. |
| Legacy asset `thirdordera.svg` | root path to archive path | Archive path present; root file absent from worktree | `R100 thirdordera.svg -> references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdordera.svg` staged | Materialized as content-preserving staged rename. |
| Legacy asset `thirdorderb.png` | root path to archive path | Archive path present; root file absent from worktree | `R100 thirdorderb.png -> references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdorderb.png` staged | Materialized as content-preserving staged rename. |
| Legacy asset `thirdorderb.svg` | root path to archive path | Archive path present; root file absent from worktree | `R100 thirdorderb.svg -> references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdorderb.svg` staged | Materialized as content-preserving staged rename. |

## Staged And Untracked Status

Audited staged additions:

- `reconstitution/swarm-2026-04-30-agent-055-mnop-pt-dt-fixture.md`
- `reconstitution/swarm-2026-04-30-agent-056-quintic-bcov-gv-fixture.md`
- `reconstitution/swarm-2026-04-30-agent-063-source-provenance-fixtures-assets.md`
- `reconstitution/swarm-2026-04-30-agent-064-source-provenance-correction.md`
- `reconstitution/swarm-2026-04-30-agent-065-frontier-fixture-integration.md`
- `reconstitution/swarm-2026-04-30-agent-070-coha-fixture-reconciliation.md`
- `reconstitution/swarm-2026-04-30-agent-071-legacy-archive-reconciliation.md`
- `references/primary-sources/coha-center-source-anchors-2026-04-30.md`
- `references/legacy-figure-assets/2018-feynman-diagram-sketches/README.md`

Audited staged additions with unstaged modifications:

- `references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md`
- `references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md`

Audited staged renames:

- `firstorder.png` to
  `references/legacy-figure-assets/2018-feynman-diagram-sketches/firstorder.png`
- `firstorder.svg` to
  `references/legacy-figure-assets/2018-feynman-diagram-sketches/firstorder.svg`
- `thirdordera.png` to
  `references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdordera.png`
- `thirdordera.svg` to
  `references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdordera.svg`
- `thirdorderb.png` to
  `references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdorderb.png`
- `thirdorderb.svg` to
  `references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdorderb.svg`

Audited untracked file:

- `reconstitution/swarm-live-launch-log-2026-04-30.md`

Other unrelated modified, staged, and untracked files exist in the shared
checkout.  They were not audited beyond the initial `git status --short` and
were not restaged by this lane.

## Mismatch Explanation

Agent 065's statement that Agent 018, 049, 054, and 057 reports were absent
remains true in the current checkout and index.  Targeted `find` found no
Agent 018, 049, 054, 057, 053, or 060 report variants.  The exact launch-log
paths for Agents 018, 049, 054, and 057 are absent.

Agent 065's statement that the CoHA fixture was absent is stale relative to
the current index, because Agent 070 has since staged
`references/primary-sources/coha-center-source-anchors-2026-04-30.md` and its
own reconciliation report.  That is a reconstruction lane, not recovery of
the missing Agent 057 report.  `references/source-provenance.md` still contains
pre-Agent-070 wording saying the CoHA fixture is absent, and
`frontier_mnop_framing_volume.tex` still reflects Agent 065's pre-Agent-070
negative evidence.  Both files are outside this lane's write ownership.

Agent 064's legacy-archive pending statement was correct for its snapshot:
the Agent 053 report and archive README were absent, Agent 060's expected
report was absent, and the six legacy assets were still root-tracked.  The
current index now contains Agent 071's reconciliation report, a staged archive
README, and six staged `R100` renames into
`references/legacy-figure-assets/2018-feynman-diagram-sketches/`.  The original
Agent 047, Agent 053, and Agent 060 reports remain absent locally.

The launch log itself is untracked and changed during this audit.  At the
latest read, it records Agent 070 as completed and closed with its report path,
but Agent 071 still live despite the staged Agent 071 report and archive
evidence.  Treat launch-log status as a live control surface, not as committed
evidence.

## Recommended Recovery Actions

1. Recover the exact missing reports from worker logs or rerun narrow
   report-only materialization lanes for:
   `agent-018-mnop-firewall`, `agent-049-mnop-source-fixture-audit`,
   `agent-054-mnop-source-fixture-plan`, and `agent-057-coha-center-fixture`.
   If recovery is impossible, update the launch log and provenance ledger to
   say those reports are absent rather than completed-locally.

2. Treat Agent 070 as a CoHA fixture reconstruction, not as the Agent 057
   report.  Integration should review the staged CoHA fixture and then update
   `references/source-provenance.md` and any frontier note statements that
   still say the fixture is absent.

3. Treat Agent 071 as a legacy archive reconstruction, not as recovery of
   Agent 047, Agent 053, or Agent 060 reports.  Integration should decide
   whether those missing reports are still required; if not, record that the
   archive evidence now comes from Agent 071.

4. Resolve the `AM` state on the MNOP/PT/DT and quintic source-anchor files.
   Their staged blobs and worktree contents differ; an owning fixture or
   integration lane must either stage the worktree edits or split them into a
   later change.

5. Keep absent-report facts negative.  No theorem, compact-CY transfer, CoHA
   center claim, trace map, `sigma_Q`, `E_2` rigidity, or `Ob_UKD` null-homotopy
   should be upgraded from notification text alone.

## Files Changed By Agent 075

- Added this report only:
  `reconstitution/swarm-2026-04-30-agent-075-materialization-audit.md`.

Staging instruction for this lane: stage only this report after whitespace
check.
