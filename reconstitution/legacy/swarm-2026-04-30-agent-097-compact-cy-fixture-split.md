# Swarm Report, 2026-04-30, Agent 097

Lane: compact-CY fixture split after CoHA narrowing.

Writable scope:

- `frontier_mnop_framing_volume.tex`
- `references/primary-sources/coha-center-source-anchors-2026-04-30.md`
- `references/source-provenance.md`
- `reconstitution/swarm-2026-04-30-agent-097-compact-cy-fixture-split.md`
- new fixture under `references/primary-sources/`

## Inputs Loaded

- `CLAUDE.md`.
- `AGENTS.md`.
- `~/ecosystem/INVARIANTS.md`, especially no-destructive-git and voice.
- `~/ecosystem/AGENTS-HARNESS.md`, especially attack-heal and scope discipline.
- `/Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`.
- `frontier_mnop_framing_volume.tex`.
- `references/primary-sources/coha-center-source-anchors-2026-04-30.md`.
- `references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md`.
- `references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md`.
- `references/source-provenance.md`.
- Agent 084, 089, and 091 reports.

## Attack

The CoHA fixture had been narrowed, but it still contained an
out-of-domain split-obligation section listing compact-CY source rows.
That preserved the firewall in prose, but left non-CoHA compact-CY facts
under the CoHA filename.  The source-provenance CoHA row also named
non-CoHA domains directly.

Failure mode: a later reader could cite the CoHA fixture as a general
compact-CY source bucket.  That violates the trusted context: CoHA is
Hall/centre vocabulary only.

## Heal

- Removed the named compact-CY split list from
  `references/primary-sources/coha-center-source-anchors-2026-04-30.md`.
- Added
  `references/primary-sources/compact-cy-source-fixture-control-surface-2026-04-30.md`
  as the non-CoHA routing surface for HKQ, CDGP, GV, OSV,
  Abel-Jacobi normalisation, conifold/Stokes data, arithmetic ledgers,
  and historical quintic source rows.
- Updated `frontier_mnop_framing_volume.tex` so the CoHA source-status
  paragraph names only Hall/CoHA/centre vocabulary and points to the
  separate compact-CY control surface for the rest.
- Updated `references/source-provenance.md` so the CoHA row no longer
  carries non-CoHA names, and added an Agent 097 compact-CY control row.

## Claim Status

Converged for the fixture split.  The CoHA fixture is vocabulary and
firewall only.  The compact-CY control surface is a routing blueprint,
not theorem support and not source closure.

Remaining obligations:

- Import line-level local mirrors for the named compact-CY fixtures.
- Add the arithmetic ledger if the finite numerical proposition is to be
  promoted beyond local checked arithmetic.
- Keep all compact-CY target claims out of `main.tex` until matched
  conventions and null-homotopies are proved.

## Verification

Commands run:

- `rg -n -i -e 'HKQ' -e 'CDGP' -e 'OSV' -e 'Gopakumar' -e '\bGV\b' -e 'Abel-Jacobi' -e 'N_AJ' -e 'N_\{\\AJ\}' -e 'conifold' -e 'Stokes' references/primary-sources/coha-center-source-anchors-2026-04-30.md`
  returned no hits.  The CoHA fixture no longer carries the named
  non-CoHA compact-CY rows.
- `rg -n -i -e 'CoHA.*(HKQ|CDGP|OSV|GV|Abel-Jacobi|conifold|Stokes)' -e '(HKQ|CDGP|OSV|GV|Abel-Jacobi|conifold|Stokes).*CoHA' frontier_mnop_framing_volume.tex references/source-provenance.md`
  returned no hits.  The frontier/provenance control surface no longer
  places CoHA and the non-CoHA domains on the same canonical row.
- `rg -n 'compact-cy-source-fixture-control-surface-2026-04-30.md' frontier_mnop_framing_volume.tex references/source-provenance.md references/primary-sources/coha-center-source-anchors-2026-04-30.md`
  found the intended routing anchors in the frontier note, the CoHA
  domain-boundary paragraph, and the provenance ledger.
- `git diff --check -- frontier_mnop_framing_volume.tex references/primary-sources/coha-center-source-anchors-2026-04-30.md references/primary-sources/compact-cy-source-fixture-control-surface-2026-04-30.md references/source-provenance.md reconstitution/swarm-2026-04-30-agent-097-compact-cy-fixture-split.md`
  returned clean.
- `pdflatex -output-directory=/tmp -interaction=nonstopmode -halt-on-error frontier_mnop_framing_volume.tex`
  passed.  Existing-style hyperref, underfull/overfull, rerun, and
  missing-destination warnings remain; no fatal TeX error.
