# Swarm Report, 2026-04-30, Agent 101

Lane: HKQ compact-BCOV/quintic source fixture.

Writable scope:

- `references/primary-sources/compact-cy-bcov-hkq-source-anchors-2026-04-30.md`
- `references/primary-sources/compact-cy-source-fixture-control-surface-2026-04-30.md`
- `references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md`
- `references/source-provenance.md`
- `reconstitution/swarm-2026-04-30-agent-101-hkq-fixture.md`

No manuscript TeX source was edited.

## Attack

The compact-CY control surface routed HKQ out of the CoHA fixture, but no
HKQ lane existed. The immediate risks were:

- the `N=10` quintic row remained an unmaterialized source obligation;
- the frontier phrase "HKQ genus 22" could be treated as sourced without a
  local or stable primary anchor;
- later readers could route compact-CY evidence back through the Hall/centre
  fixture.

## Heal

Created
`references/primary-sources/compact-cy-bcov-hkq-source-anchors-2026-04-30.md`
as a non-CoHA source-gap fixture. It records stable identifiers, remote
arXiv-source anchors, the exact `N=10` row, the gap and boundary-condition
anchors, and import obligations. It does not claim theorem support because
the HKQ source is not mirrored locally.

Updated the compact-CY control surface so HKQ is no longer merely routed;
it is a present source-gap fixture. Updated the quintic BCOV/GV fixture so
the HKQ row points to this dedicated fixture while preserving the local
mirror gap. Updated `references/source-provenance.md` with the new row.

## Source Anchors

Stable identifiers:

- arXiv: `hep-th/0612125`.
- arXiv DOI: `10.48550/arXiv.hep-th/0612125`.
- Published chapter: Huang--Klemm--Quackenbush, Lecture Notes in Physics
  757, pp. 45--102, 2009.
- Springer DOI: `10.1007/978-3-540-68030-7_3`.

Remote arXiv-source anchors inspected by:

```bash
curl -L -s https://arxiv.org/e-print/hep-th/0612125 | tar -xOzf - ccy.tex | nl -ba
```

Captured remote anchors:

| Fact | Remote anchor |
|---|---|
| Conifold gap formula and gap condition | `ccy.tex:320-338` |
| Quintic boundary-count formula | `ccy.tex:1718-1739` |
| Quintic BPS Table 1 | `ccy.tex:2280-2344` |
| `n^0_10=704288164978454686113488249750` | `ccy.tex:2317-2322` |
| Genus-51 boundary determination claim | `ccy.tex:2488-2506`; `:2680-2687` |
| Explicit quintic data to genus 20 plus external webpage | `ccy.tex:2688-2695`; bibliography `:3893` |

## Claim Status

The remote HKQ Table 1 row matches the frontier table:

```text
n^0_10 = 704288164978454686113488249750.
```

This is a source candidate, not local source-grade support, until the HKQ
paper is mirrored and text-extracted in `references/primary-sources`.

The inspected arXiv source supports "explicit quintic data to genus 20" and
"boundary determination through genus 51." It does not by itself support the
frontier's "genus 22" wording. That phrase remains an import obligation:
find a stable higher-genus-data source or correct the frontier wording.

## Non-Support List

The HKQ fixture does not support:

- all-genus compact quintic BCOV;
- GV sine expansion as primary-source fact;
- PT/GW equivalence or KKV integrality;
- CDGP period convention or raw period ratio;
- Abel--Jacobi normalisation or `N_AJ`;
- OSV rate normalisation;
- conifold resurgence, Schwinger/Stokes normalisation, or `S_c=1`;
- convergence or Borel/Stokes summability;
- compact target data, trace maps, centre automorphisms, rigidity, or
  `Ob_UKD(C_tar)=0`.

No Hall/centre/CoHA evidence was used.

## Files Changed

- Added `references/primary-sources/compact-cy-bcov-hkq-source-anchors-2026-04-30.md`.
- Updated `references/primary-sources/compact-cy-source-fixture-control-surface-2026-04-30.md`.
- Updated `references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md`.
- Updated `references/source-provenance.md`.
- Added this report.

## Verification

Commands run:

```bash
rg -n -i 'hep-th/0612125|10\.48550/arXiv\.hep-th/0612125|10\.1007/978-3-540-68030-7_3|n\^0_10|704288164978454686113488249750|genus 20|genus `20`|genus 51|genus `51`|genus 22|ccy\.tex:2317|gap condition|boundary-count|source-gap' references/primary-sources/compact-cy-bcov-hkq-source-anchors-2026-04-30.md references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md references/primary-sources/compact-cy-source-fixture-control-surface-2026-04-30.md references/source-provenance.md reconstitution/swarm-2026-04-30-agent-101-hkq-fixture.md
```

Result: found the intended stable identifiers, exact `N=10` row, genus
`20`/`51` status, `genus 22` non-support, and source-gap routing anchors.

```bash
rg -n -i 'CoHA|cohomological Hall|Hall|centre|center' references/primary-sources/compact-cy-bcov-hkq-source-anchors-2026-04-30.md reconstitution/swarm-2026-04-30-agent-101-hkq-fixture.md
```

Result: hits occur only in exclusion/non-support language. No Hall/centre
evidence is used for HKQ.

```bash
rg -n -i 'prove[sd]?|theorem-grade|source-grade|all-genus|global|Ob_UKD|Ob_\{UKD\}|null-homotopy|constructs?|establishes|certifies|kills' references/primary-sources/compact-cy-bcov-hkq-source-anchors-2026-04-30.md reconstitution/swarm-2026-04-30-agent-101-hkq-fixture.md
```

Result: hits are confined to non-support, import-obligation, or
source-grade-blocker statements.

```bash
rg -n '[ \t]$|\r' references/primary-sources/compact-cy-bcov-hkq-source-anchors-2026-04-30.md references/primary-sources/compact-cy-source-fixture-control-surface-2026-04-30.md references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md references/source-provenance.md reconstitution/swarm-2026-04-30-agent-101-hkq-fixture.md
git diff --check -- references/primary-sources/compact-cy-source-fixture-control-surface-2026-04-30.md references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md references/source-provenance.md
```

Result: no trailing whitespace or CR hits; `git diff --check` returned
clean for tracked owned-path edits.
