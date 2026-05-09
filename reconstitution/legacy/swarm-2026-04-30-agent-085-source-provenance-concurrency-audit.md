# Swarm Report, 2026-04-30, Agent 085

Lane: source-provenance concurrent-edit audit after Agents 079 and 082.

Writable scope:

- `reconstitution/swarm-2026-04-30-agent-085-source-provenance-concurrency-audit.md`

No source file, provenance ledger, fixture, asset, or unrelated report was
edited.

## Inputs Loaded

- `CLAUDE.md`
- `~/ecosystem/INVARIANTS.md` Section IV
- `~/ecosystem/AGENTS-HARNESS.md` Section VIII
- `reconstitution/swarm-2026-04-30-agent-079-source-provenance-legacy-coha-correction.md`
- `reconstitution/swarm-2026-04-30-agent-082-source-provenance-coha-present.md`
- current staged diff for `references/source-provenance.md`
- current unstaged diff for `references/source-provenance.md`
- current `references/source-provenance.md`
- supporting local evidence for the legacy archive row and the CoHA row

## Current Source-Provenance Status

Verdict: pass. Agents 079 and 082 produced a coherent final
`references/source-provenance.md` state.

Observed state:

- `references/source-provenance.md` is modified only in the index:
  `git status --short references/source-provenance.md` reports
  `M  references/source-provenance.md`.
- There is no unstaged diff for `references/source-provenance.md`.
- The worktree blob and staged index blob are identical:
  `ab88f19234d1c318c305a8a7bb240d6ac235b397`.
- The staged ledger diff is four inserted rows: legacy archive, MNOP/PT/DT,
  quintic BCOV/GV, and CoHA/centre.
- Agents 079 and 082 reports are both staged as added files.

The current relevant rows are:

- `references/source-provenance.md:5`: one legacy 2018 Feynman diagram
  asset archive row.
- `references/source-provenance.md:6`: one MNOP/PT/DT primary-source
  fixture row.
- `references/source-provenance.md:7`: one quintic BCOV/GV numerical-source
  fixture row.
- `references/source-provenance.md:8`: one CoHA/centre source-gap fixture
  row.

No duplicated legacy or CoHA row is present. The repeated
`/Users/raeez/Desktop/Whitepaper Critical Analysis.pdf` rows are older
timestamped critique registrations and are not duplicate rows introduced by
Agents 079/082.

## Coherence Checks

Legacy status is coherent.

- The ledger says the archive is materialized locally in this checkout/index.
- The staged state records the archive README as added and six `R100` renames:
  `firstorder.{png,svg}`, `thirdordera.{png,svg}`, and
  `thirdorderb.{png,svg}` moved into
  `references/legacy-figure-assets/2018-feynman-diagram-sketches/`.
- The archive directory contains exactly the README and those six assets.
- The six old root asset paths are absent from the working tree.
- The row's remaining-weakness language concerns missing Agent 053/060
  reports and stale control-document mentions, not a contradiction of archive
  materialization.

CoHA status is coherent.

- The ledger says the CoHA fixture is present locally as Agent 070's
  reconstructed source-gap ledger, not theorem support.
- The fixture
  `references/primary-sources/coha-center-source-anchors-2026-04-30.md`
  is staged as added.
- Agent 070 and Agent 078 reports are staged as added.
- Agent 057's report remains absent. This is explicitly separated from the
  fixture-present claim and is not a contradiction.
- The row states `Core theorem evidence: none from CoHA` and denies compact
  `F_X`, trace maps, `\sigma_Q`, `E_2` rigidity, `N_AJ`, GV/HKQ/CDGP/OSV line
  anchors, and `Ob_UKD(C_tar)` support. This agrees with Agent 078's
  quarantine audit.

Stale pending language check:

- No stale legacy phrases remain: no "pending local provenance", no
  "current tracked copies still", no "Do not cite the archive path", and no
  "git ls-files still lists the six root assets" in the provenance ledger.
- No stale CoHA fixture-absence language remains: no "No CoHA/centre source
  fixture", "That fixture is absent", "pre-Agent-070", or equivalent claim in
  the provenance ledger.
- The only relevant `absent` language is intentional: Agent 057 remains absent
  and Agent 053/060 reports remain absent.

## Contradictions

No contradiction found in the final `references/source-provenance.md` state.

No duplicated rows found for the Agent 079/082-owned subjects. No index/worktree
mismatch found for `references/source-provenance.md`. No stale pending language
survives except intentional report-absence statements.

## Recommended Repair

No immediate repair is required for `references/source-provenance.md`.

Recommended future cleanups, outside this audit lane:

1. Split non-CoHA compact-CY source-gap material
   (HKQ/CDGP/OSV/GV and chiral-volume normalization) into a separate
   compact-CY fixture if the ledger is further refined.
2. Keep Agent 057 absence explicit unless the report is later materialized and
   audited.
3. Update stale root asset mentions in `CLAUDE.md` and `AGENTS.md` only in a
   control-document lane; the current provenance row already records the
   mismatch.
4. Do not upgrade the CoHA row beyond source-gap/quarantine status until local
   mirrors, line-level anchors, and the compact target datum are actually
   supplied.

## Commands Run

- `sed -n '1,220p' CLAUDE.md`
- `rg --files reconstitution | rg 'agent-0(79|82)|source-provenance'`
- `git status --short`
- `git diff -- references/source-provenance.md`
- `git diff --cached -- references/source-provenance.md`
- `sed -n '1,260p' references/source-provenance.md`
- `sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-079-source-provenance-legacy-coha-correction.md`
- `sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-082-source-provenance-coha-present.md`
- `git status --short references/source-provenance.md`
- `git diff --name-status -- references/source-provenance.md`
- `git diff --cached --name-status -- references/source-provenance.md`
- `git ls-files -s references/source-provenance.md`
- `sed -n '/^## IV\\./,/^## V\\./p' /Users/raeez/ecosystem/INVARIANTS.md`
- `sed -n '/^## VIII\\./,/^## IX\\./p' /Users/raeez/ecosystem/AGENTS-HARNESS.md`
- `nl -ba references/source-provenance.md | sed -n '1,28p'`
- `rg -n -i "pending local provenance|current tracked copies still|neither is present|Do not cite the archive path|git ls-files still lists|No CoHA/centre source fixture|That fixture is absent|fixture.*absent|absent.*fixture|pre-Agent-070|Agent 057.*live|not present in the current working tree|pending" references/source-provenance.md`
- `rg -n "Legacy 2018|CoHA / centre|MNOP/PT/DT|Quintic BCOV/GV|Agent 070|Agent 078|Agent 057|Core theorem evidence|not theorem support|materialized locally|R100|HKQ/CDGP/OSV/GV" references/source-provenance.md`
- `git hash-object references/source-provenance.md`
- `git rev-parse :references/source-provenance.md`
- `git diff --check -- references/source-provenance.md`
- `git diff --cached --check -- references/source-provenance.md`
- `git diff --cached --stat -- references/source-provenance.md`
- `git diff --cached --name-status -M -- references/legacy-figure-assets/2018-feynman-diagram-sketches/README.md firstorder.png firstorder.svg thirdordera.png thirdordera.svg thirdorderb.png thirdorderb.svg references/legacy-figure-assets/2018-feynman-diagram-sketches/firstorder.png references/legacy-figure-assets/2018-feynman-diagram-sketches/firstorder.svg references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdordera.png references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdordera.svg references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdorderb.png references/legacy-figure-assets/2018-feynman-diagram-sketches/thirdorderb.svg`
- `find references/legacy-figure-assets/2018-feynman-diagram-sketches -maxdepth 1 -type f -print | sort`
- `for p in firstorder.png firstorder.svg thirdordera.png thirdordera.svg thirdorderb.png thirdorderb.svg; do if [ -e "$p" ]; then printf 'root-present %s\n' "$p"; else printf 'root-absent %s\n' "$p"; fi; done`
- `git status --short -- references/primary-sources/coha-center-source-anchors-2026-04-30.md reconstitution/swarm-2026-04-30-agent-070-coha-fixture-reconciliation.md reconstitution/swarm-2026-04-30-agent-078-coha-quarantine-audit.md reconstitution/swarm-2026-04-30-agent-057-coha-center-fixture.md`
- `git ls-files -s -- references/primary-sources/coha-center-source-anchors-2026-04-30.md reconstitution/swarm-2026-04-30-agent-070-coha-fixture-reconciliation.md reconstitution/swarm-2026-04-30-agent-078-coha-quarantine-audit.md reconstitution/swarm-2026-04-30-agent-057-coha-center-fixture.md`
- `rg --files reconstitution references/primary-sources | rg '(agent-0(57|70|78)|coha-center-source-anchors-2026-04-30)'`
- `sed -n '1,220p' reconstitution/swarm-2026-04-30-agent-078-coha-quarantine-audit.md`
- `sed -n '1,220p' reconstitution/swarm-2026-04-30-agent-070-coha-fixture-reconciliation.md`
- `git status --short -- reconstitution/swarm-2026-04-30-agent-079-source-provenance-legacy-coha-correction.md reconstitution/swarm-2026-04-30-agent-082-source-provenance-coha-present.md references/source-provenance.md`
- `rg --files reconstitution | rg 'swarm-2026-04-30-agent-0(79|82)-source-provenance'`
- `rg -n "pending|absent|not theorem support|Core theorem evidence: none from CoHA|materialized locally|Remaining provenance weakness" references/source-provenance.md`
- `awk -F'|' 'NR>=5 && /^\\|/ {gsub(/^ +| +$/, "", $3); print NR ":" $3}' references/source-provenance.md`
- `test -e reconstitution/swarm-2026-04-30-agent-085-source-provenance-concurrency-audit.md && printf 'exists\n' || printf 'absent\n'`
- `git status --short -- reconstitution/swarm-2026-04-30-agent-085-source-provenance-concurrency-audit.md`
- `sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-085-source-provenance-concurrency-audit.md`
- `git diff --check -- reconstitution/swarm-2026-04-30-agent-085-source-provenance-concurrency-audit.md`
- `git diff -- reconstitution/swarm-2026-04-30-agent-085-source-provenance-concurrency-audit.md`
- `git status --short -- reconstitution/swarm-2026-04-30-agent-085-source-provenance-concurrency-audit.md references/source-provenance.md`
- `git add -- reconstitution/swarm-2026-04-30-agent-085-source-provenance-concurrency-audit.md`

One exploratory command with an unquoted zsh glob for an Agent 057 path failed
with `no matches found`; the corrected explicit-path `git status` and
`git ls-files` commands above established the intended absence.
