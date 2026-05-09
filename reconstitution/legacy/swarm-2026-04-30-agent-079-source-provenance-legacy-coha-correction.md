# Swarm Report, 2026-04-30, Agent 079

Lane: source-provenance correction after the legacy archive materialized and
the CoHA quarantine audit landed.

Writable scope:

- `references/source-provenance.md`
- `reconstitution/swarm-2026-04-30-agent-079-source-provenance-legacy-coha-correction.md`

No manuscript source, fixture file, archive asset, control document, or
unrelated report was edited.

## Inputs Loaded

- `CLAUDE.md`
- `~/ecosystem/INVARIANTS.md`, especially the no-destructive-git and voice
  rules.
- `~/ecosystem/AGENTS-HARNESS.md`, especially scope ownership and the
  self-reflection rubric.
- `reconstitution/swarm-2026-04-30-agent-071-legacy-archive-reconciliation.md`
- `references/legacy-figure-assets/2018-feynman-diagram-sketches/README.md`
- `reconstitution/swarm-2026-04-30-agent-073-attack-heal-latest-refresh.md`
- `reconstitution/swarm-2026-04-30-agent-078-coha-quarantine-audit.md`
- `references/source-provenance.md`
- `references/primary-sources/coha-center-source-anchors-2026-04-30.md`
- CoHA follow-up context from
  `reconstitution/swarm-2026-04-30-agent-070-coha-fixture-reconciliation.md`
  and `reconstitution/swarm-2026-04-30-agent-076-frontier-coha-followup.md`

Agent 078 is present locally as
`reconstitution/swarm-2026-04-30-agent-078-coha-quarantine-audit.md`.

## Rows Corrected

| Row | Correction |
|---|---|
| `references/source-provenance.md:5` | Replaced the stale pending legacy-archive row with the current materialized state: Agent 071 reconstructed the archive move; the archive README is present; the six legacy assets are staged as `R100` renames into `references/legacy-figure-assets/2018-feynman-diagram-sketches/`; root asset paths are absent from the working tree. |
| `references/source-provenance.md:8` | Replaced the stale absent-CoHA-fixture row with the current source-gap/quarantine state: Agent 070's fixture is present; Agent 078's audit is present; Agent 057's report remains absent; CoHA is external frontier/source-gap context only, not core theorem evidence. |

The MNOP/PT/DT fixture row and the quintic BCOV/GV fixture row were preserved
without edit.

## Exact Current File-State

Observed before Agent 079 edits:

- `references/source-provenance.md` was already staged as modified from the
  earlier source-fixture rows, and had no unstaged delta before this lane.
- `references/legacy-figure-assets/2018-feynman-diagram-sketches/README.md`
  was staged as added.
- The six legacy figure assets were staged as `R100` renames:
  `firstorder.{png,svg}`, `thirdordera.{png,svg}`, and
  `thirdorderb.{png,svg}` moved into
  `references/legacy-figure-assets/2018-feynman-diagram-sketches/`.
- `references/primary-sources/coha-center-source-anchors-2026-04-30.md` was
  staged as added.
- `reconstitution/swarm-2026-04-30-agent-078-coha-quarantine-audit.md` was
  staged as added.

Owned staged name-status after Agent 079 staging:

```text
A	reconstitution/swarm-2026-04-30-agent-079-source-provenance-legacy-coha-correction.md
M	references/source-provenance.md
```

Concurrent same-file note. During final verification,
`reconstitution/swarm-2026-04-30-agent-082-source-provenance-coha-present.md`
was first observed as an untracked report outside this lane and later appeared
as a staged added file under concurrent lane activity. Its compatible
source-provenance refinement was already in `references/source-provenance.md`:
the CoHA row now also says that HKQ/CDGP/OSV/GV and chiral-volume
normalization may need a future split into a separate compact-CY fixture. This
same-file content was preserved. Agent 079 did not edit or stage Agent 082's
report.

Concurrent staged path outside Agent 079 ownership, observed at final check:

```text
A	reconstitution/swarm-2026-04-30-agent-082-source-provenance-coha-present.md
```

Relevant evidence state preserved from other agents:

```text
A	reconstitution/swarm-2026-04-30-agent-078-coha-quarantine-audit.md
A	references/legacy-figure-assets/2018-feynman-diagram-sketches/README.md
R100	firstorder.png	references/legacy-figure-assets/2018-feynman-diagram-sketches/firstorder.png
R100	firstorder.svg	references/legacy-figure-assets/2018-feynman-diagram-sketches/firstorder.svg
R100	thirdordera.png	references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdordera.png
R100	thirdordera.svg	references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdordera.svg
R100	thirdorderb.png	references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdorderb.png
R100	thirdorderb.svg	references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdorderb.svg
A	references/primary-sources/coha-center-source-anchors-2026-04-30.md
```

The archive directory currently contains exactly the README plus the six
legacy assets. The root paths `firstorder.png`, `firstorder.svg`,
`thirdordera.png`, `thirdordera.svg`, `thirdorderb.png`, and
`thirdorderb.svg` are absent from the working tree.

## CoHA Quarantine Wording

The provenance row now records:

- Core theorem evidence: none from CoHA.
- Frontier/source-gap context only: Lurie centre grammar,
  Joyce/Gross--Joyce--Tanaka Hall vocabulary, Joyce--Upmeier and
  Kinjo--Park--Safronov orientation/CoHA prerequisites, and named compact-CY
  comparison gaps.
- Quarantine boundary: CoHA, Joyce/KPS Hall vocabulary, and the
  `E_2`-centre compact target are confined to the standalone compact-CY
  frontier file plus source-gap/provenance layer. They are not a mechanism
  for `main.tex` or the formal-local theorem.
- Non-support: no compact `F_X`, trace maps, `\sigma_Q`, `E_2` rigidity,
  `N_AJ`, GV/HKQ/CDGP/OSV line anchors, or
  `Ob_UKD(C_tar)` null-homotopy follows from the CoHA fixture.
- Refinement preserved in the current row: non-CoHA compact-CY source-gap
  names carried by the CoHA row, including HKQ/CDGP/OSV/GV and chiral-volume
  normalization, may need a future split into a separate compact-CY fixture.

## Checks Run

- `git status --short`
- `rg --files | rg '(^CLAUDE\.md$|^references/source-provenance\.md$|^references/primary-sources/coha-center-source-anchors-2026-04-30\.md$|reconstitution/.*(agent-071|agent-073|agent-078|source-provenance|snapshot)|archive.*README|README.*archive|legacy.*README)'`
- `find . -maxdepth 4 \( -iname '*agent*071*' -o -iname '*agent*073*' -o -iname '*agent*078*' -o -iname '*source-provenance*' -o -iname '*archive*README*' -o -iname '*README*archive*' -o -iname '*legacy*README*' \) -print`
- `sed` reads of every required input listed above.
- `git diff --cached -- references/source-provenance.md`
- `git diff -- references/source-provenance.md`
- `find reconstitution -maxdepth 1 -type f \( -iname '*agent-078*' -o -iname '*078*' \) -print | sort`
- Targeted CoHA grep across the provenance file, CoHA fixture, Agents 070,
  073, 076, 078, and `frontier_mnop_framing_volume.tex`.
- Targeted legacy/root-asset file-state commands:
  `git status --short -- ...`, `git diff --cached --name-status -M -- ...`,
  `git ls-files --stage -- ...`, `find references/legacy-figure-assets/2018-feynman-diagram-sketches -maxdepth 1 -type f -print | sort`,
  and a root-path existence loop for the six legacy assets.
- Post-edit stale-status grep:
  `rg -n "pending local provenance|current tracked copies still|neither is present|Do not cite the archive path|git ls-files still lists the six root assets|No CoHA/centre source fixture|That fixture is absent" references/source-provenance.md`.
- Post-edit core leakage grep:
  `rg -n -i '\b(CoHA|cohomological Hall|Hall--|Hall algebra|Hall structures|Joyce|Kinjo|Safronov)\b' main.tex theorem-lanes.tex claim-strength-ledger.tex open-obligations.tex`.
- Post-edit root-asset grep:
  `rg -n "firstorder|thirdordera|thirdorderb|legacy-figure-assets|2018-feynman-diagram-sketches" main.tex Makefile CLAUDE.md AGENTS.md references/source-provenance.md references/legacy-figure-assets/2018-feynman-diagram-sketches/README.md`.
- `git diff --check`
- `git diff --cached --check`
- `git diff --check -- references/source-provenance.md reconstitution/swarm-2026-04-30-agent-079-source-provenance-legacy-coha-correction.md`
- `git diff --cached --check -- references/source-provenance.md reconstitution/swarm-2026-04-30-agent-079-source-provenance-legacy-coha-correction.md`

Results:

- `git diff --check` passed.
- `git diff --cached --check` passed.
- The stale-status grep returned no hits in `references/source-provenance.md`.
- The core CoHA/Hall leakage grep returned no hits in `main.tex`,
  `theorem-lanes.tex`, `claim-strength-ledger.tex`, or
  `open-obligations.tex`.
- The root-asset existence loop returned `root-absent` for all six old root
  paths.
- The root-asset grep found only the corrected provenance row, the archive
  README, and the already-known stale control-document mentions at
  `CLAUDE.md:16` and `AGENTS.md:213`; it found no direct `main.tex` asset use.

No PDF build was run; this lane changed only Markdown provenance.

## Files Changed

- `references/source-provenance.md`
- `reconstitution/swarm-2026-04-30-agent-079-source-provenance-legacy-coha-correction.md`

Only these two owned paths were staged by Agent 079.

## Remaining Provenance Obligations

1. Agent 053 and Agent 060 reports remain absent locally. The materialized
   archive state is reconstructed by Agent 071, not recovered from those
   missing reports.
2. `CLAUDE.md` and `AGENTS.md` still mention old root asset paths. Those
   control-document edits are outside this lane.
3. Agent 057's CoHA report remains absent. Agent 070 reconstructed the fixture
   as a source/gap ledger.
4. CoHA/Hall source material still needs local mirrors and line-level anchors
   for Lurie, Joyce, Gross--Joyce--Tanaka, Joyce--Upmeier, and
   Kinjo--Park--Safronov before it can support more than vocabulary.
5. HKQ/CDGP/OSV/GV and chiral-volume source rows should be split into a
   compact-CY source-gap fixture rather than carried by the CoHA fixture.
6. The compact target datum `C_tar`, trace maps, `sigma_Q`, `E_2` rigidity,
   `N_AJ`, and `Ob_UKD(C_tar)` remain unconstructed.
