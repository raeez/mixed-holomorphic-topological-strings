# Swarm Report, 2026-04-30, Agent 063

Lane: source-provenance update for legacy asset archive and new
source-fixture lanes.

Writable scope:

- `references/source-provenance.md`
- `reconstitution/swarm-2026-04-30-agent-063-source-provenance-fixtures-assets.md`

No manuscript source file was edited.

## Inputs Loaded

- `CLAUDE.md`
- `references/source-provenance.md`
- `reconstitution/swarm-live-launch-log-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-055-mnop-pt-dt-fixture.md`
- `references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-056-quintic-bcov-gv-fixture.md`
- `references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md`
- `~/ecosystem/INVARIANTS.md` Section IV
- `~/ecosystem/AGENTS-HARNESS.md` Section VIII

Agent 056 landed during verification and was loaded before finalizing the
provenance row.  Agent 053, Agent 057, Agent 060, and the legacy archive
README were not present in this checkout.

## Provenance Rows Added

Added four rows at the top of `references/source-provenance.md`.

| Row | Status recorded | Evidence |
|---|---|---|
| Legacy 2018 Feynman diagram asset archive lane, Agent 053 | Pending evidence closure. | Launch log says Agent 053 completed, but `reconstitution/swarm-2026-04-30-agent-053-legacy-figure-archive.md` and `references/legacy-figure-assets/2018-feynman-diagram-sketches/README.md` are absent; `git ls-files` still lists the six root assets. |
| MNOP/PT/DT primary-source fixture, Agent 055 | Completed locally as scalar source-row fixture only. | Agent 055 report and `references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md` are present.  The row preserves the gaps: no local source mirrors, no compact-CY factorization algebra, no trace map, no `\sigma_Q`, no `Ob_UKD` null-homotopy. |
| Quintic BCOV/GV numerical-source fixture, Agent 056 | Completed locally as source-gap fixture, not theorem closure. | Agent 056 report and `references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md` are present.  The row records BCOV/Costello-Li local anchors and arithmetic checks, while keeping HKQ, CDGP, GV, OSV, conifold-resurgence/Stokes sources, historical low-degree sources, and a committed numerical ledger open. |
| CoHA / centre / chiral-volume source fixture lane, Agent 057 | Pending. | No Agent 057 report and no `references/primary-sources/coha-center-source-anchors-2026-04-30.md` are present.  The row forbids importing Lurie/Joyce/Kinjo-Park-Safronov centre support, compact-target `F_X`, trace maps, `\sigma_Q`, `E_2` rigidity, or `Ob_UKD` null-homotopies from this lane. |

No existing provenance row was deleted.

## Legacy Asset Evidence

The archive move is not evidence-closed in this checkout.

`git ls-files` still reports:

- `firstorder.png`
- `firstorder.svg`
- `thirdordera.png`
- `thirdordera.svg`
- `thirdorderb.png`
- `thirdorderb.svg`

Current SHA-256 hashes of those root assets:

| File | SHA-256 |
|---|---|
| `firstorder.png` | `bd9ae2e9fbed719c50214f3022f94945b924a59351cf16b08b804f39638c824b` |
| `firstorder.svg` | `5e10c16ddb780e011103db7bb9428a6ff96abf0961026433153eb52f74314206` |
| `thirdordera.png` | `2816c5237ab87afa35754496d6f77ead9de8dea269e8ebe24a667b973698c49b` |
| `thirdordera.svg` | `ea073e1f1826ff2ede60b492dcc099054b8e92772d24bf5fe28ca29b6556bdc4` |
| `thirdorderb.png` | `4df740d828c89eb6660435558a99a995d8ca41ff796b428f50f10ad81b350cfc` |
| `thirdorderb.svg` | `45ed8819f4c22335fb6c8e8507cc657feadfe1d74e1315a7c2619a83dc9c4adc` |

Stale root-path references remain in `CLAUDE.md` and `AGENTS.md`.
Those files were outside this lane's write ownership.

## Pending-Versus-Completed Status

Completed:

- Agent 055 scalar MNOP/PT/DT source fixture is locally present.
- Agent 056 quintic BCOV/GV source-gap fixture is locally present.

Pending:

- Agent 053 legacy archive evidence: report and archive README absent;
  root assets still tracked.
- Agent 060 stale-path cleanup evidence: report absent; `CLAUDE.md` and
  `AGENTS.md` still mention root asset paths.
- Agent 057 CoHA/centre fixture: report and source anchor file absent.

## Files Changed

- Modified `references/source-provenance.md`.
- Added `reconstitution/swarm-2026-04-30-agent-063-source-provenance-fixtures-assets.md`.

## Checks Run

- `git diff --check -- references/source-provenance.md`
- `git diff --cached --check`
- `git diff --check`
- `git diff --cached --name-status`
- `git status --short --untracked-files=all`
- `rg --files -uu | rg '(swarm-2026-04-30-agent-0(53|56|57|60)|legacy-figure-assets|quintic-bcov-gv-source|coha-center-source|2018-feynman-diagram-sketches/README\.md)'`
- `git ls-files | rg '(firstorder|thirdorder|legacy-figure-assets)'`
- `rg -n "legacy-figure-assets|2018-feynman|firstorder|thirdordera|thirdorderb|quintic-bcov-gv-source|coha-center-source|swarm-2026-04-30-agent-0(53|56|57|60)" CLAUDE.md AGENTS.md references/source-provenance.md reconstitution/swarm-live-launch-log-2026-04-30.md -S`
- `shasum -a 256 firstorder.png firstorder.svg thirdordera.png thirdordera.svg thirdorderb.png thirdorderb.svg`

Staging note: this lane staged only `references/source-provenance.md` and
`reconstitution/swarm-2026-04-30-agent-063-source-provenance-fixtures-assets.md`.
Other staged and unstaged paths from concurrent lanes were present at final
status and were left untouched.

## Remaining Provenance Obligations

1. Land or restore Agent 053's report and the legacy archive README, or
   explicitly revise the launch-log completion claim.  Then update tracked
   paths so root assets and archive paths agree.
2. Land or restore Agent 060's report before treating the stale-path
   cleanup as complete.  `CLAUDE.md` and `AGENTS.md` still need the asset
   path state reconciled by that lane or a later owner.
3. Keep the Agent 055 row scalar: import durable MNOP/PT/DT source mirrors
   and line anchors before claiming local source-mirror closure.
4. Keep the Agent 056 row finite-source only: HKQ, CDGP, GV, OSV,
   conifold-resurgence/Stokes, historical low-degree sources, and a
   committed numerical ledger remain open.
5. Complete the Agent 057 CoHA/centre fixture before citing Lurie, Joyce,
   or Kinjo-Park-Safronov centre results as source-backed support for
   compact `F_X`, trace maps, `\sigma_Q`, `E_2` rigidity, or
   `Ob_UKD(C_tar)=0`.
