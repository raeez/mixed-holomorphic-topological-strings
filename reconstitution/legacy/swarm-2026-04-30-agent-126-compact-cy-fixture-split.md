# Agent 126 Compact-CY Fixture Split Report, 2026-04-30

Lane: compact-CY source-fixture architecture after HKQ/CDGP/GV/OSV
source-lane materialisation.

Writable scope:

- `references/source-provenance.md`
- `references/primary-sources/compact-cy-source-fixture-split-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-126-compact-cy-fixture-split.md`

No TeX manuscript file was edited.

## Inputs Loaded

- `CLAUDE.md`.
- `~/ecosystem/INVARIANTS.md` voice and standalone rules.
- `~/ecosystem/AGENTS-HARNESS.md` self-reflection rubric.
- `attack-heal-swarm/SKILL.md` and shared `protocol.md`.
- Vol II `chriss-ginzburg-rectify/SKILL.md`.
- Existing CoHA, compact-CY control, quintic BCOV/GV, HKQ, CDGP, GV,
  and OSV fixtures.
- Agent reports 097, 101, 112, 113, 117, 120, and 122.
- `main.tex`, `open-obligations.tex`, and
  `frontier_mnop_framing_volume.tex` were read by `rg` only; not edited.

## Valid Attacks

```yaml
- id: A1-126-01
  severity: 2
  status: healed
  lens: source-fixture architecture
  target: compact-CY fixture routing
  claim: HKQ, CDGP, GV, OSV, Abel-Jacobi, and conifold/Stokes facts can remain in one loose compact-CY or CoHA-adjacent source bucket.
  broken_step: Separate mathematical domains have different primary sources, local mirror status, conventions, and non-support. CoHA supports only Hall/centre vocabulary.
  evidence_type: source_conflict
  evidence_ref: references/primary-sources/coha-center-source-anchors-2026-04-30.md; HKQ/CDGP/GV/OSV fixtures
  minimal_heal: Create a split fixture with lane-level admissibility and CoHA exclusion.
```

```yaml
- id: A1-126-02
  severity: 2
  status: healed
  lens: provenance freshness
  target: references/source-provenance.md
  claim: HKQ, CDGP, GV, and OSV still share the original quintic missing-source status.
  broken_step: HKQ, CDGP, and GV now have local primary mirrors; OSV has a remote-only fixture; Abel-Jacobi and conifold/Stokes remain absent.
  evidence_type: line_reference
  evidence_ref: shasum over HKQ/CDGP/GV mirrors; source fixture local-status paragraphs
  minimal_heal: Update the quintic/control rows and add separate split, CDGP, GV, and OSV provenance rows.
```

```yaml
- id: A1-126-03
  severity: 1
  status: healed
  lens: CDGP formula admissibility
  target: CDGP period-basis formulas
  claim: CDGP OCR text can support theorem-grade formula transcription.
  broken_step: The local text layer is OCR from a journal scan and does not fully recover displayed relation (3.23).
  evidence_type: source_quality
  evidence_ref: cdgp-nucl-phys-b359-1991.txt:1023-1028, :1778, :2405; Agent 120 report
  minimal_heal: Mark OCR-poor formulas as PDF-visual required and name exact deciding evidence.
```

```yaml
- id: A1-126-04
  severity: 1
  status: healed
  lens: OSV rate firewall
  target: OSV attractor lane
  claim: OSV sources the value 5 log 5 or fixed-class quintic coefficient growth.
  broken_step: The OSV fixture records no local mirror and a negative remote search for 5 log 5/log 5 in black.tex.
  evidence_type: unsupported
  evidence_ref: references/primary-sources/osv-attractor-rate-source-anchors-2026-04-30.md:91-93, :102, :112-113
  minimal_heal: Keep OSV remote-only and separate the arithmetic identity 5 log 5=-log(5^-5) from OSV source support.
```

```yaml
- id: A1-126-05
  severity: 2
  status: healed
  lens: missing fixture isolation
  target: Abel-Jacobi and conifold/Stokes lanes
  claim: CDGP/HKQ/GV partial facts close Abel-Jacobi or Stokes normalisation.
  broken_step: CDGP supplies periods, HKQ supplies gap/boundary data, and GV supplies Schwinger vocabulary; none supplies N_AJ, A_BCOV=A_Schwinger=A_period, or S_c=1.
  evidence_type: unsupported
  evidence_ref: split fixture lane matrix and residual source obligations
  minimal_heal: Record these as absent fixtures with exact theorem-grade deciding evidence.
```

## Repairs Made

- Added
  `references/primary-sources/compact-cy-source-fixture-split-2026-04-30.md`.
  It records lane-level admissibility, local checksums for HKQ/CDGP/GV
  mirrors, OSV remote-only status, Abel-Jacobi and conifold/Stokes
  absence, CDGP PDF-visual requirements, and a CoHA exclusion
  proposition.
- Updated `references/source-provenance.md`:
  - refreshed the original quintic BCOV/GV row so HKQ/CDGP/GV are no
    longer listed as open in the same way as absent lanes;
  - marked the Agent 097 control surface as the initial blueprint now
    refined by the Agent 126 split;
  - added rows for the Agent 126 split, CDGP local import, GV local
    import, and OSV remote-only fixture.
- Added this report.

## Files Changed And Staged

Changed in this pass:

- `references/source-provenance.md`
- `references/primary-sources/compact-cy-source-fixture-split-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-126-compact-cy-fixture-split.md`

The OSV fixture
`references/primary-sources/osv-attractor-rate-source-anchors-2026-04-30.md`
was already staged before this pass and was read but not edited.
`references/source-provenance.md` was also already staged with earlier
source rows; this pass edited that file in place and staged the resulting
owned updates without reverting the existing rows.

## Checks Run

```bash
shasum -a 256 references/primary-sources/hkq-compact-cy-hep-th-0612125.pdf references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex references/primary-sources/hkq-compact-cy-hep-th-0612125.txt references/primary-sources/cdgp-nucl-phys-b359-1991.pdf references/primary-sources/cdgp-nucl-phys-b359-1991.txt references/primary-sources/gv-hep-th-9809187.pdf references/primary-sources/gv-hep-th-9809187.tex references/primary-sources/gv-hep-th-9809187.txt references/primary-sources/gv-hep-th-9812127.pdf references/primary-sources/gv-hep-th-9812127.tex references/primary-sources/gv-hep-th-9812127.txt
wc -l -c references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex references/primary-sources/cdgp-nucl-phys-b359-1991.txt references/primary-sources/gv-hep-th-9809187.tex references/primary-sources/gv-hep-th-9812127.tex references/primary-sources/osv-attractor-rate-source-anchors-2026-04-30.md
rg -n "HKQ-gap-condition|HKQ-quintic-table-N10|CDGP-integral-period-basis|GV-II-sine-expansion|OSV-main-conjecture|Exact Non-Support|Import Obligations" references/primary-sources/compact-cy-bcov-hkq-source-anchors-2026-04-30.md references/primary-sources/mirror-quintic-cdgp-period-source-anchors-2026-04-30.md references/primary-sources/gopakumar-vafa-bps-source-anchors-2026-04-30.md references/primary-sources/osv-attractor-rate-source-anchors-2026-04-30.md
git diff --check -- references/source-provenance.md references/primary-sources/compact-cy-source-fixture-split-2026-04-30.md
rg -n "compact-cy-source-fixture-split|CDGP mirror-quintic|Gopakumar--Vafa|OSV attractor|OCR-poor|PDF-visual|required|remote-only|local primary mirrors" references/source-provenance.md references/primary-sources/compact-cy-source-fixture-split-2026-04-30.md
```

Results:

- HKQ, CDGP, and GV checksums match the lane fixtures.
- `git diff --check` returned clean for the edited provenance and split
  fixture.
- The split/provenance scans find the intended CDGP, GV, OSV,
  PDF-visual, remote-only, and CoHA-exclusion language.
- No TeX build was run; the owned surface is Markdown provenance and
  source fixtures only.

## Residual Source And Theorem Obligations

1. Import OSV PDF, TeX source, and text extraction locally; re-anchor
   OSV rows to repository-local lines.
2. Build the Abel--Jacobi normalisation fixture with `N_AJ`, period-basis
   compatibility, Hodge metric, and `2 pi i` convention.
3. Build the conifold/Stokes fixture with Strominger, Vafa/Schwinger,
   Shenker--Marino, and Cecotti--Codesido--Marino anchors.
4. Perform PDF-visual CDGP formula transcription before theorem-grade use
   of relation (3.23) or period-basis identities.
5. Add a committed arithmetic ledger for `a_N`, the tail fit, raw period
   evaluation, `5 log 5=-log(5^-5)`, and error control.
6. Keep all compact-CY source facts outside the CoHA/centre stable core
   until a separate compact target construction and matched-conventions
   proof exist.
