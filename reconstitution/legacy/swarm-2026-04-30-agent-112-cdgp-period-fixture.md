# Agent 112 CDGP Period Fixture Report, 2026-04-30

Scope. Owned writable surfaces:

- `references/primary-sources/mirror-quintic-cdgp-period-source-anchors-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-112-cdgp-period-fixture.md`

Read-only context included `CLAUDE.md`, `AGENTS.md`, the shared
attack-heal protocol, the compact-CY control surface, the quintic BCOV/GV
fixture, `frontier_mnop_framing_volume.tex`, and source-provenance style rows.
No manuscript source file was edited.

## Attack Ledger

```yaml
- id: A1-112-01
  severity: 2
  status: healed
  lens: primary-source admissibility
  target: CDGP period source row
  claim: The frontier note can use CDGP period conventions as sourced data.
  broken_step: No tracked primary CDGP mirror existed under references/primary-sources.
  evidence_type: missing_source
  evidence_ref: "rg --files references/primary-sources | rg -i '(candelas|cdgp|mirror)' returned no CDGP primary mirror"
  files_read:
    - references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md
    - references/primary-sources/compact-cy-source-fixture-control-surface-2026-04-30.md
  tools_used:
    - rg
    - curl
    - pdftotext
  confidence: high
  blast_radius: Raw period ratio, Picard-Fuchs convention, mirror map, prepotential, and period-basis claims remain source-gap obligations.
  minimal_heal: Create a CDGP-only fixture with stable identifiers, remote import anchors, local cross-checks, and non-support.
  residual: Local primary CDGP PDF/text still absent.
  deciding_evidence: Commit a local CDGP mirror and re-anchor equations locally.

- id: A1-112-02
  severity: 2
  status: healed
  lens: variable convention
  target: frontier_mnop_framing_volume.tex:330-332 and :738-742
  claim: The displayed Picard-Fuchs operators use the CDGP convention.
  broken_step: The z-operator is source-compatible after translating z=(5 psi)^(-5); the psi-operator is not source-grade if psi denotes CDGP's original family parameter.
  evidence_type: source_conflict
  evidence_ref: "remote CDGP PDF text lines 275-282, 767-793, 804-836; HKQ secondary lines 846-864, 875-899"
  files_read:
    - frontier_mnop_framing_volume.tex
    - references/primary-sources/hkq-compact-cy-hep-th-0612125.txt
  tools_used:
    - sed
    - nl
  confidence: high
  blast_radius: Mirror-period recovery conjecture may import the wrong operator variable.
  minimal_heal: Fixture records the convention translation and flags the psi-display as an import/rewrite obligation.
  residual: Manuscript text was read-only for this agent.
  deciding_evidence: Main-thread edit renames that operator variable to z or rewrites it in original psi.

- id: A1-112-03
  severity: 2
  status: healed
  lens: normalization
  target: frontier_mnop_framing_volume.tex:304-338
  claim: "|t(z_c)|=|omega_1/omega_0|(5^-5)=7.5909 is a CDGP source fact."
  broken_step: CDGP sources the period formula and mirror-map normalization; the numerical value is a local computation, and the raw unnormalised logarithmic ratio differs from the normalized mirror coordinate by a 2 pi i convention.
  evidence_type: unsupported
  evidence_ref: "remote CDGP PDF text lines 1643-1813; existing quintic fixture raw arithmetic row"
  files_read:
    - frontier_mnop_framing_volume.tex
    - references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md
  tools_used:
    - rg
    - sed
  confidence: high
  blast_radius: The finite chiral-volume comparison can be overstated as period-source theorem support.
  minimal_heal: Fixture separates source-supported formulas from local arithmetic and from normalized mirror-coordinate claims.
  residual: A committed arithmetic ledger/script should own the numerical boundary evaluation.
  deciding_evidence: Local script with precision/tail control and source-accepted period convention.

- id: A1-112-04
  severity: 2
  status: healed
  lens: non-support firewall
  target: frontier_mnop_framing_volume.tex:357-369, :676-705, :818-821
  claim: CDGP periods support Abel-Jacobi normalization, OSV rate, Stokes normalization, or conifold trinity.
  broken_step: CDGP supplies mirror periods, conifold monodromy, prepotential, and Yukawa expansion; it does not supply this repository's N_AJ, OSV, Schwinger, Stokes, GV, CoHA, or Ob_UKD data.
  evidence_type: unsupported
  evidence_ref: "remote CDGP anchors plus compact-CY control surface lines 34-39"
  files_read:
    - references/primary-sources/compact-cy-source-fixture-control-surface-2026-04-30.md
    - frontier_mnop_framing_volume.tex
  tools_used:
    - rg
    - sed
  confidence: high
  blast_radius: False transfer into CoHA/centre or compact-CY target theorem.
  minimal_heal: Fixture lists exact non-support and routes adjacent domains to separate fixtures.
  residual: Separate N_AJ, OSV, GV, and conifold-resurgence fixtures remain open.
  deciding_evidence: Domain fixtures with local primary anchors and matched conventions.
```

## Source Facts

Stable CDGP identifiers were recorded: DOI `10.1016/0550-3213(91)90292-6`,
ScienceDirect PII `0550-3213(91)90292-6`, Crossref work metadata, and AMS/IP
reprint DOI `10.1090/amsip/009/02`.

Remote CDGP PDF inspection supplied import anchors for:

- the family `sum x_i^5 - 5 psi prod x_i = 0`;
- the true coordinate `psi^5`;
- conifold branch `psi^5=1`, with branch `psi=1`;
- modern frontier coordinate `z=(5 psi)^(-5)`, hence `z_c=5^{-5}`;
- fundamental period coefficients `(5n)!/(n!)^5`;
- the z-form Picard-Fuchs operator after convention translation;
- branch periods, conifold logarithm, and integral symplectic period basis;
- prepotential/mirror-map construction;
- Yukawa instanton expansion and Table 4.

Local support remains bibliographic or secondary only: Costello--Li and BCOV cite
CDGP; the working-tree HKQ text restates formulas while citing CDGP, but HKQ is
not primary for this lane and is untracked in the current checkout.

## Repairs Made

Added
`references/primary-sources/mirror-quintic-cdgp-period-source-anchors-2026-04-30.md`
with:

- stable primary identifiers and remote PDF checksum;
- reproducible remote inspection command;
- remote source-fact table;
- local secondary cross-check table;
- convention translation `psi`/`z` and conifold `z_c=5^{-5}`;
- raw period ratio status;
- claim-to-source map for the frontier anchors;
- exact import obligations and non-support firewall.

This heals the source-control surface without claiming local primary source
closure.

## Verification Run

Commands run:

```bash
sed -n '1,240p' CLAUDE.md
sed -n '1,260p' AGENTS.md
sed -n '1,260p' /Users/raeez/ecosystem/skills/shared/attack-heal-swarm/protocol.md
sed -n '1,220p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
rg --files references/primary-sources | rg -i '(candelas|cdgp|green|parkes|quintic|mirror|period)'
rg -n 'CDGP|Candelas|Green|Parkes|period|Picard|quintic|mirror map|Yukawa|conifold' frontier_mnop_framing_volume.tex
curl -L -s -o /tmp/cdgp-cogp.pdf https://www.staff.science.uu.nl/~beuke106/HypergeometricFunctions/COGP.pdf
pdftotext -layout /tmp/cdgp-cogp.pdf /tmp/cdgp-cogp.txt
sha256sum /tmp/cdgp-cogp.pdf /tmp/cdgp-cogp.txt
curl -L -s 'https://api.crossref.org/works/10.1016/0550-3213(91)90292-6'
curl -L -s https://api.crossref.org/works/10.1090/amsip/009/02
git status --short
```

No TeX build was run; this was a markdown source-fixture pass.

## Residual Theorem Obligations

1. Import a local primary CDGP mirror and re-anchor equations locally.
2. Reconcile the frontier `psi`-Picard--Fuchs display with CDGP's original
   `psi` variable or rename it to the large-radius `z`.
3. Add a committed arithmetic ledger/script for the raw boundary period ratio.
4. Supply `N_AJ` before identifying the raw CDGP ratio with a Hodge-normalized
   Abel--Jacobi norm.
5. Supply separate OSV, GV, and conifold-resurgence/Stokes fixtures before any
   compact-CY closure, conifold trinity, or Stokes normalization is theorem-grade.
6. Keep CDGP outside CoHA: it supplies period/prepotential data, not Hall,
   centre, compact target, trace-map, rigidity, or `Ob_UKD(C_tar)` data.
