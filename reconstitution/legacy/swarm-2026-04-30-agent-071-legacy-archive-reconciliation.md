# Swarm Report, 2026-04-30, Agent 071

Lane: legacy figure archive reconciliation after Agent 064 found local
evidence pending.

Writable scope:

- The six legacy root figure assets, if still present.
- `references/legacy-figure-assets/2018-feynman-diagram-sketches/README.md`.
- `reconstitution/swarm-2026-04-30-agent-071-legacy-archive-reconciliation.md`.

No manuscript source, control document, or unrelated provenance file was
edited.

## Inputs Loaded

- `CLAUDE.md`.
- `AGENTS.md`.
- `~/ecosystem/INVARIANTS.md`, including destructive-git and voice rules.
- `~/ecosystem/AGENTS-HARNESS.md`, especially scope and self-reflection rules.
- `reconstitution/swarm-2026-04-30-agent-064-source-provenance-correction.md`.
- `reconstitution/swarm-live-launch-log-2026-04-30.md`, for Agent 047, 053,
  060, 064, and 071 status lines.
- `main.tex` and `Makefile` usage greps as needed.

Required prior-agent reports checked and absent:

- `reconstitution/swarm-2026-04-30-agent-047-legacy-figure-assets.md`.
- `reconstitution/swarm-2026-04-30-agent-053-legacy-figure-archive.md`.
- `reconstitution/swarm-2026-04-30-agent-060-agent-docs-legacy-assets.md`.

Present prior-agent report loaded:

- `reconstitution/swarm-2026-04-30-agent-064-source-provenance-correction.md`.

## Existence And Status Checks

Observed before the move:

- `find reconstitution -maxdepth 1 -type f \( -name '*agent-047*' -o -name '*agent-053*' -o -name '*agent-060*' -o -name '*agent-064*' \) -print | sort`
  returned only
  `reconstitution/swarm-2026-04-30-agent-064-source-provenance-correction.md`.
- `find references -path '*legacy-figure-assets*' -maxdepth 5 -print | sort`
  returned no archive paths.
- `git ls-files --stage -- firstorder.svg thirdordera.svg thirdorderb.svg firstorder.png thirdordera.png thirdorderb.png ...`
  listed all six assets at the repository root and no archive README or
  archive copies.
- `git status --short -- firstorder.svg thirdordera.svg thirdorderb.svg firstorder.png thirdordera.png thirdorderb.png references/legacy-figure-assets/2018-feynman-diagram-sketches/README.md reconstitution/swarm-2026-04-30-agent-071-legacy-archive-reconciliation.md`
  returned no local changes under the assigned paths.
- The global working tree already had unrelated modified, staged, and
  untracked files. They were not edited or restaged by this lane.

Agent 064's report stated the same local absence: Agent 053's archive report
and archive README were absent, Agent 060's expected report was absent, and
the six root assets remained tracked.

Decision: Agent 053's legacy archive move was absent from the current
checkout/index. The move was mechanically safe because the six root assets
were tracked and clean, the target archive directory was absent, and no
direct manuscript use of these asset names was found in `main.tex`.

## Moves Performed

Created the archive directory:

```bash
mkdir -p references/legacy-figure-assets/2018-feynman-diagram-sketches
```

Moved the six tracked assets with `git mv`:

```bash
git mv firstorder.svg thirdordera.svg thirdorderb.svg firstorder.png thirdordera.png thirdorderb.png references/legacy-figure-assets/2018-feynman-diagram-sketches/
```

The cached diff reports content-preserving renames:

| Status | Source | Destination |
|---|---|---|
| `R100` | `firstorder.png` | `references/legacy-figure-assets/2018-feynman-diagram-sketches/firstorder.png` |
| `R100` | `firstorder.svg` | `references/legacy-figure-assets/2018-feynman-diagram-sketches/firstorder.svg` |
| `R100` | `thirdordera.png` | `references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdordera.png` |
| `R100` | `thirdordera.svg` | `references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdordera.svg` |
| `R100` | `thirdorderb.png` | `references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdorderb.png` |
| `R100` | `thirdorderb.svg` | `references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdorderb.svg` |

No asset was deleted as evidence. The root-path removals are the source side
of the recorded renames.

## Hashes And Provenance

Pre-move Git blob identifiers:

| Root path | Git blob |
|---|---|
| `firstorder.png` | `10f4a555f228ef03a6cef81e3a0d1267ef941d63` |
| `firstorder.svg` | `4bc2e45731d0d1e2e58279de2310381483352b79` |
| `thirdordera.png` | `945d0aaec4361052b4235ec3b52ff0008a21bb31` |
| `thirdordera.svg` | `0e53d44a4e14794757e32517261e684ea5f6f1ce` |
| `thirdorderb.png` | `0284d1d24c4b9357598e7b407bffe5ecb3ae0193` |
| `thirdorderb.svg` | `41f4c8d4f64d3f5772e024aebe317586a6474b0a` |

Post-move SHA-256 content digests:

| Archive path | SHA-256 |
|---|---|
| `references/legacy-figure-assets/2018-feynman-diagram-sketches/firstorder.png` | `bd9ae2e9fbed719c50214f3022f94945b924a59351cf16b08b804f39638c824b` |
| `references/legacy-figure-assets/2018-feynman-diagram-sketches/firstorder.svg` | `5e10c16ddb780e011103db7bb9428a6ff96abf0961026433153eb52f74314206` |
| `references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdordera.png` | `2816c5237ab87afa35754496d6f77ead9de8dea269e8ebe24a667b973698c49b` |
| `references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdordera.svg` | `ea073e1f1826ff2ede60b492dcc099054b8e92772d24bf5fe28ca29b6556bdc4` |
| `references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdorderb.png` | `4df740d828c89eb6660435558a99a995d8ca41ff796b428f50f10ad81b350cfc` |
| `references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdorderb.svg` | `45ed8819f4c22335fb6c8e8507cc657feadfe1d74e1315a7c2619a83dc9c4adc` |

Post-move `git ls-files --stage` lists the same Git blobs at the archive
paths.

## Usage Greps

- `rg -n "includegraphics|graphicspath|firstorder|thirdordera|thirdorderb|\\.png|\\.svg" main.tex Makefile`
  found no `main.tex` hits for these assets. It found only generic PNG
  handling in `Makefile:281-282`.
- `rg -n "firstorder|thirdordera|thirdorderb|legacy-figure-assets|2018-feynman-diagram-sketches" main.tex Makefile CLAUDE.md AGENTS.md reconstitution references .gitignore`
  found no direct current manuscript use, but did find stale control-doc
  root-path mentions in `CLAUDE.md:16` and `AGENTS.md:213`.
- `references/source-provenance.md:5` still recorded the Agent 064 pending
  status before this reconciliation. That file was outside this lane's write
  ownership and was not edited.

## Files Changed

- Renamed `firstorder.png` to
  `references/legacy-figure-assets/2018-feynman-diagram-sketches/firstorder.png`.
- Renamed `firstorder.svg` to
  `references/legacy-figure-assets/2018-feynman-diagram-sketches/firstorder.svg`.
- Renamed `thirdordera.png` to
  `references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdordera.png`.
- Renamed `thirdordera.svg` to
  `references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdordera.svg`.
- Renamed `thirdorderb.png` to
  `references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdorderb.png`.
- Renamed `thirdorderb.svg` to
  `references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdorderb.svg`.
- Added `references/legacy-figure-assets/2018-feynman-diagram-sketches/README.md`.
- Added this report.

## Checks Run

- `pwd && git status --short && rg --files | rg '(^CLAUDE\\.md$|^AGENTS\\.md$|^main\\.tex$|^Makefile$|^reconstitution/.*agent-0(47|53|60|64).*\\.md$|^(firstorder|thirdordera|thirdorderb)\\.(svg|png)$|^references/legacy-figure-assets/2018-feynman-diagram-sketches/)'`
- `sed -n '1,220p' CLAUDE.md`
- `sed -n '1,260p' AGENTS.md`
- `sed -n '1,220p' ~/ecosystem/INVARIANTS.md`
- `rg -n "Self-reflection|rubric|VIII|Correctness|Rigor|Attribution|Standalone|revert|stash|stage|commit" ~/ecosystem/AGENTS-HARNESS.md`
- `sed -n '130,162p' ~/ecosystem/AGENTS-HARNESS.md`
- `sed -n '45,62p' ~/ecosystem/AGENTS-HARNESS.md`
- `sed -n '180,190p' ~/ecosystem/AGENTS-HARNESS.md`
- `find reconstitution -maxdepth 1 -type f \( -name '*agent-047*' -o -name '*agent-053*' -o -name '*agent-060*' -o -name '*agent-064*' \) -print | sort`
- `sed -n '1,180p' reconstitution/swarm-2026-04-30-agent-064-source-provenance-correction.md`
- `sed -n '260,315p' reconstitution/swarm-live-launch-log-2026-04-30.md`
- `sed -n '315,345p' reconstitution/swarm-live-launch-log-2026-04-30.md`
- `sed -n '340,382p' reconstitution/swarm-live-launch-log-2026-04-30.md`
- `find references -path '*legacy-figure-assets*' -maxdepth 5 -print | sort`
- `git ls-files --stage -- firstorder.svg thirdordera.svg thirdorderb.svg firstorder.png thirdordera.png thirdorderb.png references/legacy-figure-assets/2018-feynman-diagram-sketches/README.md references/legacy-figure-assets/2018-feynman-diagram-sketches/firstorder.svg references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdordera.svg references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdorderb.svg references/legacy-figure-assets/2018-feynman-diagram-sketches/firstorder.png references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdordera.png references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdorderb.png`
- `shasum -a 256 firstorder.svg thirdordera.svg thirdorderb.svg firstorder.png thirdordera.png thirdorderb.png`
- `rg -n "includegraphics|graphicspath|firstorder|thirdordera|thirdorderb|\\.png|\\.svg" main.tex Makefile`
- `sed -n '1,180p' Makefile`
- `git status --short -- firstorder.svg thirdordera.svg thirdorderb.svg firstorder.png thirdordera.png thirdorderb.png references/legacy-figure-assets/2018-feynman-diagram-sketches/README.md reconstitution/swarm-2026-04-30-agent-071-legacy-archive-reconciliation.md`
- `mkdir -p references/legacy-figure-assets/2018-feynman-diagram-sketches`
- `git mv firstorder.svg thirdordera.svg thirdorderb.svg firstorder.png thirdordera.png thirdorderb.png references/legacy-figure-assets/2018-feynman-diagram-sketches/`
- `git status --short -- firstorder.svg thirdordera.svg thirdorderb.svg firstorder.png thirdordera.png thirdorderb.png references/legacy-figure-assets/2018-feynman-diagram-sketches/`
- `shasum -a 256 references/legacy-figure-assets/2018-feynman-diagram-sketches/firstorder.svg references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdordera.svg references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdorderb.svg references/legacy-figure-assets/2018-feynman-diagram-sketches/firstorder.png references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdordera.png references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdorderb.png`
- `git ls-files --stage -- references/legacy-figure-assets/2018-feynman-diagram-sketches/firstorder.svg references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdordera.svg references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdorderb.svg references/legacy-figure-assets/2018-feynman-diagram-sketches/firstorder.png references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdordera.png references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdorderb.png`
- `git diff --cached --name-status -M -- firstorder.svg thirdordera.svg thirdorderb.svg firstorder.png thirdordera.png thirdorderb.png references/legacy-figure-assets/2018-feynman-diagram-sketches/`
- `find references/legacy-figure-assets/2018-feynman-diagram-sketches -maxdepth 1 -type f -print | sort`
- `rg -n "Agent 047|Agent 053|Agent 060|Agent 064|legacy figure|legacy-asset|legacy asset|legacy archive" reconstitution/swarm-live-launch-log-2026-04-30.md reconstitution/swarm-2026-04-30-agent-064-source-provenance-correction.md references/source-provenance.md CLAUDE.md AGENTS.md`
- `git diff --check -- references/legacy-figure-assets/2018-feynman-diagram-sketches/README.md reconstitution/swarm-2026-04-30-agent-071-legacy-archive-reconciliation.md`
- `git diff --cached --check -- firstorder.svg thirdordera.svg thirdorderb.svg firstorder.png thirdordera.png thirdorderb.png references/legacy-figure-assets/2018-feynman-diagram-sketches/`
- `for f in firstorder.svg thirdordera.svg thirdorderb.svg firstorder.png thirdordera.png thirdorderb.png; do test ! -e "$f" || printf 'root-present %s\n' "$f"; done; find references/legacy-figure-assets/2018-feynman-diagram-sketches -maxdepth 1 -type f -print | sort`
- `git add references/legacy-figure-assets/2018-feynman-diagram-sketches/README.md reconstitution/swarm-2026-04-30-agent-071-legacy-archive-reconciliation.md`
- `git status --short -- firstorder.svg thirdordera.svg thirdorderb.svg firstorder.png thirdordera.png thirdorderb.png references/legacy-figure-assets/2018-feynman-diagram-sketches/ reconstitution/swarm-2026-04-30-agent-071-legacy-archive-reconciliation.md`
- `git diff --cached --check -- firstorder.svg thirdordera.svg thirdorderb.svg firstorder.png thirdordera.png thirdorderb.png references/legacy-figure-assets/2018-feynman-diagram-sketches/ reconstitution/swarm-2026-04-30-agent-071-legacy-archive-reconciliation.md`
- `git diff --check -- firstorder.svg thirdordera.svg thirdorderb.svg firstorder.png thirdordera.png thirdorderb.png references/legacy-figure-assets/2018-feynman-diagram-sketches/ reconstitution/swarm-2026-04-30-agent-071-legacy-archive-reconciliation.md`
- `git diff --cached --name-status -M -- firstorder.svg thirdordera.svg thirdorderb.svg firstorder.png thirdordera.png thirdorderb.png references/legacy-figure-assets/2018-feynman-diagram-sketches/ reconstitution/swarm-2026-04-30-agent-071-legacy-archive-reconciliation.md`
- `git ls-files --stage -- firstorder.svg thirdordera.svg thirdorderb.svg firstorder.png thirdordera.png thirdorderb.png references/legacy-figure-assets/2018-feynman-diagram-sketches/README.md references/legacy-figure-assets/2018-feynman-diagram-sketches/firstorder.svg references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdordera.svg references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdorderb.svg references/legacy-figure-assets/2018-feynman-diagram-sketches/firstorder.png references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdordera.png references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdorderb.png reconstitution/swarm-2026-04-30-agent-071-legacy-archive-reconciliation.md`
- `rg -n "includegraphics|graphicspath|firstorder|thirdordera|thirdorderb|\\.png|\\.svg" main.tex Makefile`

No PDF build was run. The moved assets are not direct `main.tex` inputs in
this checkout.

## Residual Archive Obligations

1. `references/source-provenance.md:5` should be updated by an owning lane or
   integration thread; it still records the pre-reconciliation pending state.
2. `CLAUDE.md:16` and `AGENTS.md:213` still mention the old root asset paths.
   Agent 060 owned those control-doc edits; its report is absent locally.
3. Agent 047, Agent 053, and Agent 060 reports remain absent locally despite
   launch-log completion lines. This report and the archive README reconstruct
   the local evidence for the archive move, but they do not recover the missing
   prior-agent reports.
4. Historical reports and private audit artifacts that mention the root assets
   remain preserved as historical evidence. They were not rewritten.
