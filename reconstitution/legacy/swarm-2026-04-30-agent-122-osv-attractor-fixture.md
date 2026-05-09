# Agent 122 OSV Attractor-Rate Fixture Report, 2026-04-30

Lane: OSV attractor comparison and physical rate normalisation, separated
from CoHA.

Writable surface:

- `references/primary-sources/osv-attractor-rate-source-anchors-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-122-osv-attractor-fixture.md`

No manuscript source, source-provenance file, PDF, TeX source mirror, or
other fixture was edited.

## Attack Ledger

```yaml
id: A1-122-01
severity: 2
status: healed
lens: local-source admissibility
target: references/primary-sources/osv-attractor-rate-source-anchors-2026-04-30.md
claim: The frontier note has source support for the OSV attractor comparison.
broken_step: No OSV primary mirror exists under references/primary-sources.
evidence_type: missing_source
evidence_ref: "find references/primary-sources -maxdepth 1 with OSV/Ooguri/Strominger/0405146 patterns returned no local OSV mirror"
files_read:
  - CLAUDE.md
  - AGENTS.md
  - references/primary-sources/compact-cy-source-fixture-control-surface-2026-04-30.md
  - references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md
  - references/primary-sources/compact-cy-bcov-hkq-source-anchors-2026-04-30.md
  - references/primary-sources/gopakumar-vafa-bps-source-anchors-2026-04-30.md
  - references/primary-sources/mirror-quintic-cdgp-period-source-anchors-2026-04-30.md
  - frontier_mnop_framing_volume.tex
tools_used:
  - sed
  - nl
  - rg
  - find
  - curl
  - gunzip
  - pdfinfo
  - shasum
confidence: high
blast_radius: OSV could be treated as local source-grade support when it is still remote-only.
minimal_heal: Add an OSV fixture with stable identifiers, remote arXiv-source anchors, local status, and import obligations.
residual: Import local OSV PDF/source/text mirrors and re-anchor locally.
deciding_evidence: Tracked local OSV files with checksums and repository-local line anchors.
```

```yaml
id: A1-122-02
severity: 1
status: healed
lens: numerical-rate support
target: frontier_mnop_framing_volume.tex:314-315 and :348-349
claim: OSV sources the comparison value 5 log 5.
broken_step: The inspected OSV source stream supports the mixed attractor comparison but contains no 5 log 5, log 5, or 5\log term.
evidence_type: unsupported
evidence_ref: "rg -n -F -e '5 log 5' -e 'log 5' -e '\\log 5' -e '5\\log' /tmp/black.tex returned no hits"
files_read:
  - frontier_mnop_framing_volume.tex
  - /tmp/black.tex
tools_used:
  - rg
  - nl
confidence: high
blast_radius: The frontier note could falsely promote a local arithmetic/conifold number to OSV source support.
minimal_heal: Fixture states that OSV does not source 5 log 5 and requires a separate arithmetic/source ledger if the number remains.
residual: Decide whether 5 log 5 is merely -log(5^-5) from the CDGP conifold coordinate or has another primary physical source.
deciding_evidence: A local computation/source fixture deriving the rate with matched conventions.
```

```yaml
id: A1-122-03
severity: 2
status: healed
lens: ensemble-strength audit
target: frontier_mnop_framing_volume.tex:623-627
claim: OSV supplies a coefficient-growth or convergence theorem for the quintic BPS series.
broken_step: OSV defines a mixed black-hole ensemble and says microcanonical entropy is not the mixed entropy except in a large-charge steepest-descent approximation.
evidence_type: source_conflict
evidence_ref: "remote arXiv source black.tex:693-729"
files_read:
  - frontier_mnop_framing_volume.tex
  - /tmp/black.tex
tools_used:
  - nl
  - sed
confidence: high
blast_radius: A physics mixed-ensemble conjecture could be misread as theorem-grade fixed-class quintic asymptotics.
minimal_heal: Claim map separates OSV attractor vocabulary from convergence and coefficient-growth obligations.
residual: Separate coefficient-growth theorem or computation remains required.
deciding_evidence: Primary theorem/source or local derivation of the BPS-series convergence scale.
```

```yaml
id: A1-122-04
severity: 2
status: healed
lens: convention normalisation
target: frontier_mnop_framing_volume.tex:597-620
claim: OSV normalisations can be compared directly with CDGP/HKQ/GV variables.
broken_step: OSV uses variables CX=p+i phi/pi, cal F=-pi Im F(...,256), t^A=(p^A+i phi^A/pi)/(p^0+i phi^0/pi), and g_top=+-4 pi i/(p^0+i phi^0/pi). These must be matched before any numerical comparison.
evidence_type: line_reference
evidence_ref: "remote arXiv source black.tex:645-684 and :763-868"
files_read:
  - references/primary-sources/gopakumar-vafa-bps-source-anchors-2026-04-30.md
  - references/primary-sources/mirror-quintic-cdgp-period-source-anchors-2026-04-30.md
  - /tmp/black.tex
tools_used:
  - sed
  - nl
confidence: high
blast_radius: Missing factors of pi, 2 pi i, or gauge variables can move the claimed rate.
minimal_heal: Fixture records a physical normalisation ledger and makes matched-conventions proof an import obligation.
residual: No matched OSV/CDGP/GV/frontier convention proof exists in this lane.
deciding_evidence: A local convention note proving the variable bridge.
```

```yaml
id: A1-122-05
severity: 3
status: healed
lens: CoHA separation
target: references/primary-sources/compact-cy-source-fixture-control-surface-2026-04-30.md:36 and :49
claim: CoHA/Hall/centre fixtures can carry OSV attractor-rate source facts.
broken_step: The compact-CY control surface routes OSV to a non-CoHA fixture and explicitly excludes OSV attractor-rate statements from the CoHA fixture.
evidence_type: line_reference
evidence_ref: "compact-cy-source-fixture-control-surface-2026-04-30.md OSV row and CoHA exclusion list"
files_read:
  - references/primary-sources/compact-cy-source-fixture-control-surface-2026-04-30.md
tools_used:
  - sed
confidence: high
blast_radius: False transfer from Hall/centre vocabulary into compact-CY black-hole physics.
minimal_heal: OSV fixture states that no Hall, CoHA, or centre claim is supported.
residual: None for this fixture boundary.
deciding_evidence: Future provenance row remains separated from CoHA.
```

## Repairs Made

Added
`references/primary-sources/osv-attractor-rate-source-anchors-2026-04-30.md`
with:

- stable OSV identifiers: arXiv `hep-th/0405146`, arXiv DOI
  `10.48550/arXiv.hep-th/0405146`, Phys. Rev. D 70, 106007, DOI
  `10.1103/PhysRevD.70.106007`, and report numbers;
- remote arXiv-source inspection ledger for the single-file `black.tex`
  payload, plus checksums for the e-print, extracted TeX, and PDF;
- remote source-fact rows for the OSV conjecture, attractor equations,
  corrected free energy, mixed ensemble, topological-string
  normalisation, heuristic warning, index check, and background
  dependence;
- physical normalisation ledger for `CX`, `phi`, `cal F`, the Legendre
  transform, mixed ensemble, and `Z_BH=|Z_top|^2`;
- claim-to-source map for the frontier OSV/rate anchors;
- explicit non-support list, especially no source support for `5 log 5`;
- import obligations for local mirrors, local line anchors, and a separate
  rate computation/source ledger.

## Verification Run

Commands run:

```bash
sed -n '1,220p' /Users/raeez/ecosystem/skills/claude-code/attack-heal-swarm-plugin/skills/attack-heal-swarm/SKILL.md
sed -n '1,260p' /Users/raeez/ecosystem/skills/shared/attack-heal-swarm/protocol.md
sed -n '1,220p' CLAUDE.md
sed -n '1,240p' AGENTS.md
sed -n '1,260p' references/primary-sources/compact-cy-source-fixture-control-surface-2026-04-30.md
sed -n '1,280p' references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md
sed -n '1,260p' references/primary-sources/compact-cy-bcov-hkq-source-anchors-2026-04-30.md
sed -n '1,260p' references/primary-sources/gopakumar-vafa-bps-source-anchors-2026-04-30.md
sed -n '1,240p' references/primary-sources/mirror-quintic-cdgp-period-source-anchors-2026-04-30.md
nl -ba frontier_mnop_framing_volume.tex | sed -n '270,370p'
nl -ba frontier_mnop_framing_volume.tex | sed -n '580,635p'
nl -ba frontier_mnop_framing_volume.tex | sed -n '730,840p'
rg --files references/primary-sources | rg -i '(0405146|osv-black-hole-attractors).*\.(pdf|tex|txt)$'
curl -L --fail --silent --show-error https://arxiv.org/e-print/hep-th/0405146v2 -o /tmp/osv-v2.eprint
gunzip -c /tmp/osv-v2.eprint > /tmp/black.tex
nl -ba /tmp/black.tex | sed -n '270,390p;522,720p;720,900p;900,1120p;1150,1225p;1280,1320p;1680,1819p'
curl -L --fail --silent --show-error 'https://export.arxiv.org/api/query?id_list=hep-th/0405146'
curl -L --fail --silent --show-error https://api.crossref.org/works/10.1103/PhysRevD.70.106007
curl -L --fail --silent --show-error https://arxiv.org/pdf/hep-th/0405146v2 -o /tmp/osv122-osv-v2.pdf
pdfinfo /tmp/osv122-osv-v2.pdf
shasum -a 256 /tmp/osv-v2.eprint /tmp/black.tex /tmp/osv122-osv-v2.pdf
rg -n -F -e '5 log 5' -e 'log 5' -e '\\log 5' -e '5\\log' /tmp/black.tex
```

Results:

- No local OSV PDF, TeX source, or text mirror was found under
  `references/primary-sources`. The markdown fixture is a routing file,
  not a primary-source mirror.
- The arXiv e-print payload is a gzipped single TeX source named
  `black.tex`, 1915 lines.
- The arXiv PDF is PDF 1.4, 32 pages.
- arXiv and Crossref metadata agree on the title, authors, arXiv ID,
  journal reference, and DOI.
- The OSV source anchors support the mixed attractor comparison and
  physical normalisations recorded in the fixture.
- The `5 log 5` search over `black.tex` returned no hits.

No TeX build was run; this was a markdown source-fixture pass only.

## Residual Theorem Obligations

1. Import the OSV PDF, TeX source, and text extraction locally and
   re-anchor the fixture to repository-local lines.
2. Add a separate arithmetic/source ledger for `5 log 5` if the frontier
   note keeps that number.
3. Prove or source the convention bridge from OSV variables to CDGP,
   GV, HKQ, and the frontier note's period variables before using OSV
   as numerical theorem support.
4. Supply a coefficient-growth or convergence theorem before treating
   the OSV mixed ensemble as a fixed-class quintic asymptotic rate.
5. Keep OSV outside CoHA/Hall/centre and outside
   `Ob_UKD(C_tar)=0` until a separate compact-CY target construction and
   matched-conventions proof are supplied.
