# Lossless Semantic Merge Mandate

Date: 2026-04-28  
Repository: `/Users/raeez/topological-strings`

## Instruction

All side trees, worktrees, dangling threads, and uncommitted work are to be merged only by deep semantic merge. Mathematical content is lossless: no proof idea, counterexample, computation, obstruction, source anchor, or conditional construction is discarded merely because it is stale, contradicted, inconvenient, or located in a side tree.

Contradictory mathematical content is not collapsed by choosing a side. It is resolved as one of:

- a theorem with repaired hypotheses and proof;
- a counterexample that destroys the claim;
- a conditional statement with the exact external input named;
- an open obligation with the obstruction stated;
- a rejected route preserved in the reconstitution record.

## Current Inventory Snapshot

Commands run from the shared checkout:

```text
git worktree list --porcelain
git branch --no-merged master --format='%(refname:short)'
git worktree list --porcelain | ... status --short --branch
```

Observed state:

- registered worktrees: `38`;
- side branches ahead of `master`: `0`;
- tracked changed-file entries across registered worktrees: `500`;
- untracked-file entries across registered worktrees: `2214`;
- `.claude/worktrees/ts-b-w2`: clean;
- first attack branches and `ts-b-w2`: behind the current `master`;
- wave2 through wave6 branches: at `master`, with their material still visible as worktree diffs and untracked files;
- shared checkout: dirty and remains the integration surface.

The pre-17:50 worktree and `/private/tmp` material was already audited in:

- `reconstitution/dangling-worktree-integration-2026-04-28.md`;
- `reconstitution/current-six-agent-integration-2026-04-28.md`;
- `reconstitution/final-lossless-merge-audit-2026-04-28.md`;
- `reconstitution/private-tmp-artifacts-2026-04-28/`.

Those ledgers remain binding, but the 17:50 critique and the cycle-2 manuscript-proper swarm supersede any earlier statement that the manuscript is converged as a shippable paper.

## Appropriate Moment

The appropriate moment for the next integration is after the 17:50 manuscript-proper repair wave has rewritten the theorem-status surface. Mechanical application of old side-worktree patches before that repair would reintroduce pre-critique theorem language and obscure the new casualties.

The next merge wave must therefore proceed in this order:

1. Treat `reconstitution/attack-heal-manuscript-proper-1750-cycle2-consolidation-2026-04-28.md` as the active attack ledger.
2. Repair the manuscript proper against the severity-1 and severity-2 casualties in that ledger.
3. For every side worktree patch, compare against the repaired shared checkout hunk by hunk.
4. Classify each hunk as absorbed, novel-valid, novel-counterexample, contradicted, or stale.
5. Inscribe every novel-valid mathematical item in the manuscript/support files or preserve it as an explicit obligation.
6. Preserve every contradicted mathematical item as a rejected route or counterexample in `reconstitution/`.
7. Only after this semantic pass, run targeted scans and `make pdf`.

## Non-Negotiable Merge Rules

- No wholesale file-copy for files modified on both sides.
- No `reset`, `stash`, `checkout`, `restore`, `rebase`, destructive worktree cleanup, or forced branch deletion.
- No deletion of mathematical content without a replacement theorem, counterexample, obstruction record, or provenance entry.
- No theorem promotion by majority of agents or by repeated wording across side trees.
- No external-facing process labels, route codes, local paths, or stale theorem names in the final manuscript.
- If a side-tree claim conflicts with the 17:50 casualty ledger, the conflict is preserved and adjudicated; it is not silently reconciled.

## Integration Surface

The shared checkout remains the target surface. Existing dirty files are not assumed correct merely because they are central. They are the current composed draft and must be attacked against the 17:50 critique before final build.

The old side worktrees remain evidence stores. Their mathematical substance is not lost when an old patch is not mechanically applied; it is either already integrated, explicitly rejected, or still to be compared during the next hunk-level pass.
