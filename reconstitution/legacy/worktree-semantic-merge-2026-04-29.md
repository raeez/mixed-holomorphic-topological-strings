# Worktree Semantic Merge Ledger

Date: 2026-04-29.

Scope: current-state audit of `master`, local branches, registered worktrees,
loose `/private/tmp/topological-strings-*` material, and the latest critique
source before pushing the reconstituted manuscript.

## Baseline

Current `master` is `117d794`:

- `8b9e5ac` commits the reconstituted manuscript, critique materials,
  primary sources, scripts, theorem lanes, ledgers, appendices, and the
  vendored `raeez-math-template.sty`.
- `25febff` updates the reconstitution verification plan.
- `117d794` adds the Wave-5 closure reports, including the fresh-clone smoke
  test.

The working tree is clean after these commits. The branch is ahead of
`origin/master` by three commits.

## Latest critique source

The mutable Desktop critique file was checked against the repository copy.
Both have SHA-256

`819fde50bb45bf30ae70114e85a91182e7664913c6c16cc727f0bd7175482c84`.

The canonical copies are:

- `materials/raw/2026-04-28-1750-whitepaper-critical-analysis.pdf`
- `materials/processed/2026-04-28-1750-whitepaper-critical-analysis.txt`

The old 09:03 attack artifact is absent from `materials/`. The 08:36 and
undated 2026-04-28 copies remain archival, not authoritative.

## Registered worktrees and branches

Current `git worktree list --porcelain` contains only:

- `/Users/raeez/topological-strings` on `master` at `117d794`;
- `/Users/raeez/topological-strings/.claude/worktrees/ts-b-w2` on `ts-b-w2`
  at `7b828ee`.

`ts-b-w2` is already an ancestor of `master`: `git rev-list --left-right
--count master...ts-b-w2` returns `32 0`, and `git diff --stat
master...ts-b-w2` is empty. No merge is required.

Current local branch refs are only `master` and `ts-b-w2`. `git branch --all
--no-merged master` returns no branch. There is no committed local or remote
branch head outside `master` requiring integration.

## `/private/tmp` material

The former swarm worktree directories under `/private/tmp` are no longer
registered worktrees. The surviving directories are either empty carrier
directories with only the `latex-template` symlink or build/inspection scratch
directories containing logs, PDFs, aux files, rendered-page images, or copied
TeX snapshots.

The substantive patch and worktree evidence from those paths is already
preserved in the repository:

- first attack patches:
  `reconstitution/private-tmp-artifacts-2026-04-28/patches/`;
- Wave-2--Wave-4 worktree diffs:
  `reconstitution/private-tmp-artifacts-2026-04-28/worktree-diffs/`;
- Wave-5 worktree diffs:
  `reconstitution/private-tmp-artifacts-2026-04-28/wave5-worktree-diffs/`;
- Wave-6 worktree diffs:
  `reconstitution/private-tmp-artifacts-2026-04-28/wave6-worktree-diffs/`;
- final lossless audit snapshots:
  `reconstitution/private-tmp-artifacts-2026-04-28/final-lossless-audit-081035/`;
- selected worker build logs and visual QA artifacts:
  `reconstitution/private-tmp-artifacts-2026-04-28/current-worker-builds/`
  and `reconstitution/private-tmp-artifacts-2026-04-28/visual/`.

The loose `/private/tmp/topological-strings-{crossvolume,hygiene-main,quantum,scalar,tate}.patch`
files match the preserved patch family. They target older pre-rearchitecture
text and are not applied mechanically.

## Semantic disposition by worktree family

| Family | Disposition |
|---|---|
| First attack: `crossvolume`, `hygiene`, `quantum`, `scalar`, `tate`, `trace` | Absorbed in stricter current form. The old patches are preserved, but applying them would reintroduce claims now demoted by the latest critique. |
| Wave 2 and Wave 3 rearchitecture | Absorbed through the current manuscript architecture: claim-strength ledger, theorem lanes, principles, local dictionary, appendices, open obligations, source ledger, and repaired main text. |
| Wave 4 anchoring and release QA | Absorbed through the primary-source bundle, source-convention ledger, macro/notation QA, visual QA, cross-repo firewall audit, referee report, and release QA artifacts. |
| Wave 5 remainder | Absorbed through the current reduced BV/QME, radial-parts, Rees/Fourier, quantum descendant, Tate-regulator, and cross-repo firewall reports and TeX repairs. |
| Wave 6 attack of the manuscript proper | Absorbed through the current casualty table and stricter theorem statuses: mixed brane-defect QME remains open, radial parts remain conditional, unweighted regulator endpoint is a no-go, and Costello graph realization is not asserted. |
| `ts-b-w2` | Already merged by ancestry; no uncommitted or unique content remains. |
| Build scratch directories | No independent mathematical content. Their useful evidence is represented by committed QA reports or preserved logs. |

## Critique-driven theorem status enforced

The current manuscript preserves the latest critique's main casualties as
explicit non-claims in `claim-strength-ledger.tex`:

- no full \(Z^{P_0}_{\mathrm{fact}}\) theorem;
- no full unreduced open BV identification;
- no conilpotent Koszul-duality theorem for the full formal Hamiltonian
  algebra outside the stated Tate-conilpotent or admissible-envelope
  hypotheses;
- no bare \(R\)-submodule Matlis annihilator formulation;
- no unconditional finite-\(N\) radial-parts theorem;
- no normalized-Moyal claim that the \(\hbar^2\) correction vanishes;
- no unconditional Costello graph theorem from reduced Wick diagrams;
- no "exactly three" QME classification.

The surviving core is the reduced CE/PV Hamiltonian comparison, the
finite algebraic scalar and Moyal calculations, the Matlis principal-part
cotangent module, the weighted finite-window Tate coefficient construction,
and the conditional/open obligations recorded in `open-obligations.tex` and
`theorem-lanes.tex`.

## Verification commands run in this pass

- `git worktree list --porcelain`
- `git branch --all --no-merged master`
- `git rev-list --left-right --count master...ts-b-w2`
- `git diff --stat master...ts-b-w2`
- `shasum -a 256` on the Desktop critique and canonical raw critique copy
- targeted `rg` checks for scalar-axis, Moyal, radial-parts, Tate
  conilpotence, Matlis, Costello graph, and QME-status language

No unresolved side branch or worktree content remains outside the recorded
repository artifacts.
