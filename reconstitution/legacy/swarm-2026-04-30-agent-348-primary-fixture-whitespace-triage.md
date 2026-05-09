# Agent 348 primary-fixture whitespace triage

Date: 2026-04-30.

Assignment: report-only triage of the primary-source fixture
whitespace/EOF issues recorded by Agent 342. No existing file was edited.

## Verdict

Observed. Agent 342's `git diff --cached --check` finding is real for the
staged primary-source TeX mirrors:

- `references/primary-sources/gv-hep-th-9809187.tex`: blank line at EOF.
- `references/primary-sources/gv-hep-th-9812127.tex`: blank line at EOF.
- `references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex`:
  trailing whitespace on arXiv-source lines recorded by Agent 342.
- `references/primary-sources/osv-hep-th-0405146.tex`: trailing whitespace
  on six arXiv-source lines recorded by Agent 342.

Classification:

- Manuscript build: no blocker. These files are not input by `main.tex`.
- Commit hygiene: blocker only if the integration gate requires a global or
  staged `git diff --check` pass over raw fixtures.
- Raw source fixture integrity: preserve by default. The whitespace is part
  of the mirrored arXiv TeX-source bytes currently recorded by checksum
  ledgers. Normalizing it would change the fixture hashes and would require
  a deliberate fixture-regeneration patch, not a casual whitespace cleanup.

## Evidence

Agent 342 anchor:

- `reconstitution/swarm-2026-04-30-agent-342-final-build-readiness-audit.md`
  records the four staged fixture paths and the exact whitespace/EOF
  failures under its `git diff --check` section.

Current verification:

- `git diff --cached --check -- references/primary-sources/gv-hep-th-9809187.tex references/primary-sources/gv-hep-th-9812127.tex references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex references/primary-sources/osv-hep-th-0405146.tex`
  failed with the same classes of findings: two EOF blank-line findings,
  HKQ trailing-whitespace findings, and OSV trailing-whitespace findings.
- `git diff --check --` on the same four paths produced no output. The issue
  is in the staged additions, not an unstaged later edit.
- `git diff --cached --name-status --` on the same four paths reports all
  four as `A`, i.e. added source fixtures.
- `rg -n -F 'references/primary-sources' main.tex` returned no hits.
- `rg -n -F '\include{' main.tex` returned no hits.
- `rg -n -F '\input{' main.tex` lists the current direct root inputs; none
  is one of the primary-source fixture paths.

Checksum verification:

```text
ddf1727d45b1def42ea9090af3c1301fd6c18af4af279dbf92a250040b9d5c16  references/primary-sources/gv-hep-th-9809187.tex
4687315b433ff4ec6ba753809d7ba7f8f48aff44276836faef80dde7c94b1650  references/primary-sources/gv-hep-th-9812127.tex
26f95d4dbb5f0d8985023bb4e4353c3d882ec08e8fb7908732fc07ce6ff4910d  references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex
e9b25649b656597dae7f7ade2964700d399135b6ab555f44a88018f49b67405f  references/primary-sources/osv-hep-th-0405146.tex
```

These are the same source-stream hashes recorded in the GV, HKQ, OSV, and
compact-CY split fixture ledgers. Therefore the whitespace findings are not
evidence of a manuscript typo. They are evidence that raw mirrored TeX
payloads violate the repository's ordinary whitespace gate.

## Integration recommendation

Do not edit the four source fixtures for this issue during manuscript build
readiness. Treat them as raw source fixtures unless the integration owner
chooses a repository-wide rule that imported source mirrors must be
normalized.

If the integration owner chooses normalization, the patch must update the
corresponding checksum ledgers and should record that the local mirrors are
normalized copies, not byte-for-byte arXiv source streams. Without that
decision, the correct action is to exempt or separately review these raw
fixtures when applying `git diff --check` as a commit hygiene gate.

## Post-write verification

`git diff --cached --check -- reconstitution/swarm-2026-04-30-agent-348-primary-fixture-whitespace-triage.md`
passed after staging this report.

## Commands run

```bash
sed -n '1,220p' CLAUDE.md
sed -n '1,220p' /Users/raeez/ecosystem/INVARIANTS.md
sed -n '1,260p' /Users/raeez/ecosystem/AGENTS-HARNESS.md
sed -n '1,240p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
git status --short
sed -n '1,220p' reconstitution/swarm-2026-04-30-agent-342-final-build-readiness-audit.md
git diff --cached --check -- references/primary-sources/gv-hep-th-9809187.tex references/primary-sources/gv-hep-th-9812127.tex references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex references/primary-sources/osv-hep-th-0405146.tex
git diff --check -- references/primary-sources/gv-hep-th-9809187.tex references/primary-sources/gv-hep-th-9812127.tex references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex references/primary-sources/osv-hep-th-0405146.tex
git diff --cached --name-status -- references/primary-sources/gv-hep-th-9809187.tex references/primary-sources/gv-hep-th-9812127.tex references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex references/primary-sources/osv-hep-th-0405146.tex
shasum -a 256 references/primary-sources/gv-hep-th-9809187.tex references/primary-sources/gv-hep-th-9812127.tex references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex references/primary-sources/osv-hep-th-0405146.tex
wc -l -c references/primary-sources/gv-hep-th-9809187.tex references/primary-sources/gv-hep-th-9812127.tex references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex references/primary-sources/osv-hep-th-0405146.tex
tail -n 8 references/primary-sources/gv-hep-th-9809187.tex | sed -n 'l'
tail -n 8 references/primary-sources/gv-hep-th-9812127.tex | sed -n 'l'
sed -n '190,207l;832,860l;1186,1193l;3487,3496l' references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex
sed -n '1252,1258l;1508,1530l;1549,1554l;1708,1713l' references/primary-sources/osv-hep-th-0405146.tex
rg -n -F 'references/primary-sources' main.tex
rg -n -F '\include{' main.tex
rg -n -F '\input{' main.tex
git diff --check --no-index -- /dev/null reconstitution/swarm-2026-04-30-agent-348-primary-fixture-whitespace-triage.md
git add reconstitution/swarm-2026-04-30-agent-348-primary-fixture-whitespace-triage.md
git diff --cached --check -- reconstitution/swarm-2026-04-30-agent-348-primary-fixture-whitespace-triage.md
```
