# Swarm Report, 2026-04-30, Agent 064

Lane: source-provenance correction after report-order mismatch.

Writable scope:

- `references/source-provenance.md`
- `reconstitution/swarm-2026-04-30-agent-064-source-provenance-correction.md`

No manuscript source file was edited.

## Inputs Loaded

- `CLAUDE.md`
- `~/ecosystem/INVARIANTS.md`, especially Section IV
- `~/ecosystem/AGENTS-HARNESS.md`, especially Section VIII
- `reconstitution/swarm-2026-04-30-agent-055-mnop-pt-dt-fixture.md`
- `reconstitution/swarm-2026-04-30-agent-056-quintic-bcov-gv-fixture.md`
- `reconstitution/swarm-2026-04-30-agent-063-source-provenance-fixtures-assets.md`
- `references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md`
- `references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md`
- `references/source-provenance.md`
- `reconstitution/swarm-live-launch-log-2026-04-30.md`, for Agent 053, 057, and 060 status lines

Required-but-absent inputs after filesystem and index verification:

- `reconstitution/swarm-2026-04-30-agent-053-legacy-figure-archive.md`
- `references/legacy-figure-assets/2018-feynman-diagram-sketches/README.md`
- `reconstitution/swarm-2026-04-30-agent-057-*.md`, no Agent 057 report found
- `references/primary-sources/coha-center-source-anchors-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-060-agent-docs-legacy-assets.md`

## Stale Rows Attacked

| Row | Attack | Result |
|---|---|---|
| Legacy 2018 figure archive / Agent 053 | Agent 063 recorded pending evidence because Agent 053 and Agent 060 outputs had not reached the checkout. Recheck current working tree and index. | Still pending locally. Launch log says Agent 053 and Agent 060 completed, but the expected reports and archive README are absent. The six root assets remain tracked. |
| CoHA / centre / chiral-volume fixture / Agent 057 | Agent 063 recorded pending evidence because the CoHA fixture had not reached the checkout. Recheck current working tree and index. | Still pending locally. Launch log marks Agent 057 live, and no CoHA fixture file or Agent 057 report is present. |
| MNOP/PT/DT / Agent 055 | Check whether the completed row is supported by current files. | Completed local source-fixture evidence is present. The row remains scalar only. |
| Quintic BCOV/GV / Agent 056 | Check whether the completed row is supported by current files. | Completed local source-gap fixture evidence is present. The row remains finite-source only, not theorem closure. |

## Exact Corrections

- Rewrote the Agent 053 legacy-archive provenance note so the status reads as current filesystem/index evidence: pending local provenance despite launch-log completion.
- Named the expected Agent 060 report exactly as `reconstitution/swarm-2026-04-30-agent-060-agent-docs-legacy-assets.md`.
- Rewrote the Agent 055 row status as completed local source-fixture evidence, while preserving the gaps: no local source mirrors, bibliography keys, compact-CY factorization algebra, trace map, `\sigma_Q`, or `Ob_UKD` null-homotopy.
- Rewrote the Agent 056 row status as completed local source-gap fixture evidence, while preserving HKQ, CDGP, GV, OSV, conifold-resurgence/Stokes, historical low-degree sources, and committed numerical-ledger obligations.
- Rewrote the Agent 057 row status as pending local provenance tied to current working tree/index absence, not only report-order lag.

## Completed Versus Pending

Completed in current checkout/index:

- Agent 055 MNOP/PT/DT scalar source fixture:
  `references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md`
  and `reconstitution/swarm-2026-04-30-agent-055-mnop-pt-dt-fixture.md`.
- Agent 056 quintic BCOV/GV source-gap fixture:
  `references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md`
  and `reconstitution/swarm-2026-04-30-agent-056-quintic-bcov-gv-fixture.md`.

Pending in current checkout/index:

- Agent 053 legacy archive evidence: report absent, archive README absent,
  six root assets still tracked.
- Agent 060 stale path cleanup evidence: expected report absent;
  `CLAUDE.md` and `AGENTS.md` still cite the root assets.
- Agent 057 CoHA/centre fixture: source-anchor file absent and report absent.

## Checks Run

- `find reconstitution -maxdepth 1 -type f \( -iname '*053*' -o -iname '*055*' -o -iname '*056*' -o -iname '*057*' -o -iname '*060*' -o -iname '*063*' \) -print | sort`
- `find references -type f \( -iname '*coha*' -o -iname '*center*' -o -iname '*centre*' -o -iname '*legacy*' -o -iname '*feynman*' -o -iname '*source-anchors-2026-04-30.md' \) -print | sort`
- `git ls-files -s -- references/source-provenance.md references/legacy-figure-assets/2018-feynman-diagram-sketches/README.md references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md references/primary-sources/coha-center-source-anchors-2026-04-30.md firstorder.png firstorder.svg thirdordera.png thirdordera.svg thirdorderb.png thirdorderb.svg reconstitution/swarm-2026-04-30-agent-053-legacy-figure-archive.md reconstitution/swarm-2026-04-30-agent-055-mnop-pt-dt-fixture.md reconstitution/swarm-2026-04-30-agent-056-quintic-bcov-gv-fixture.md reconstitution/swarm-2026-04-30-agent-057-coha-center-source-fixture.md reconstitution/swarm-2026-04-30-agent-060-agent-docs-legacy-assets.md reconstitution/swarm-2026-04-30-agent-063-source-provenance-fixtures-assets.md`
- `git status --short -- references/legacy-figure-assets references/primary-sources reconstitution/swarm-2026-04-30-agent-053-legacy-figure-archive.md reconstitution/swarm-2026-04-30-agent-057-coha-center-source-fixture.md reconstitution/swarm-2026-04-30-agent-060-stale-path-cleanup.md firstorder.png firstorder.svg thirdordera.png thirdordera.svg thirdorderb.png thirdorderb.svg`
- `rg -n "Agent 0?(53|57|60)|053|057|060|legacy|CoHA|coha|centre|center|stale" reconstitution/swarm-live-launch-log-2026-04-30.md reconstitution/attack-heal-216-launch-manifest-2026-04-30.md`
- `rg -n "firstorder|thirdordera|thirdorderb|legacy-figure-assets|2018-feynman|coha-center-source|CoHA|centre|center" CLAUDE.md AGENTS.md references/source-provenance.md`
- `find . -path './.git' -prune -o \( -path './references/legacy-figure-assets/2018-feynman-diagram-sketches/README.md' -o -path './references/primary-sources/coha-center-source-anchors-2026-04-30.md' -o -name 'swarm-2026-04-30-agent-053-*' -o -name 'swarm-2026-04-30-agent-057-*' -o -name 'swarm-2026-04-30-agent-060-*' \) -print | sort`
- `rg -n "Pending evidence closure|Agent 060's stale-path cleanup report|No Agent 057 report|Pending\\. No|Completed locally as|report-order lag|stale-path cleanup" references/source-provenance.md reconstitution/swarm-2026-04-30-agent-064-source-provenance-correction.md`
- `rg -n "Current status:|pending local provenance|completed local source|current working tree or index|source facts do not prove compact-CY transfer|source-fixture evidence|source-gap fixture" references/source-provenance.md reconstitution/swarm-2026-04-30-agent-064-source-provenance-correction.md`
- `git diff --check`
- `git diff --cached --check -- references/source-provenance.md reconstitution/swarm-2026-04-30-agent-064-source-provenance-correction.md`

## Files Changed

- Modified `references/source-provenance.md`.
- Added `reconstitution/swarm-2026-04-30-agent-064-source-provenance-correction.md`.

## Residual Provenance Obligations

1. Land or reconstruct Agent 053's legacy archive report and
   `references/legacy-figure-assets/2018-feynman-diagram-sketches/README.md`,
   or revise the launch-log completion claim. Until then the legacy archive
   lane remains pending in this checkout.
2. Land or reconstruct Agent 060's report and reconcile `CLAUDE.md` and
   `AGENTS.md` with the actual figure-asset path state. This lane did not own
   those files.
3. Land Agent 057's CoHA/centre source fixture before citing Lurie, Joyce, or
   Kinjo-Park-Safronov as local source support for compact `F_X`, trace maps,
   `\sigma_Q`, `E_2` rigidity, or `Ob_UKD(C_tar)=0`.
4. Import durable local MNOP/PT/DT source mirrors and line anchors before
   treating Agent 055 as local source-mirror closure.
5. Import HKQ, CDGP, GV, OSV, conifold-resurgence/Stokes, and historical
   low-degree sources, and add a committed numerical ledger, before treating
   Agent 056 as theorem or numerical-provenance closure.
6. Preserve the live theorem firewall: source facts do not prove compact-CY
   transfer, trace construction, `\sigma_Q`, or `Ob_UKD` null-homotopies.
