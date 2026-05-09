# Agent 117 GV Local Import Report, 2026-04-30

Scope. Writable surface restricted to:

- `references/primary-sources/gopakumar-vafa-bps-source-anchors-2026-04-30.md`
- `references/primary-sources/gv-hep-th-9809187.pdf`
- `references/primary-sources/gv-hep-th-9809187.tex`
- `references/primary-sources/gv-hep-th-9809187.txt`
- `references/primary-sources/gv-hep-th-9812127.pdf`
- `references/primary-sources/gv-hep-th-9812127.tex`
- `references/primary-sources/gv-hep-th-9812127.txt`
- `reconstitution/swarm-2026-04-30-agent-117-gv-local-import.md`

No source-provenance row was edited. The main thread owns provenance.

## Attack Ledger

```yaml
id: A1-117-01
severity: 2
status: healed
lens: local-source closure
target: references/primary-sources/gopakumar-vafa-bps-source-anchors-2026-04-30.md
claim: The GV fixture can support the BPS and sine-expansion rows locally.
broken_step: Agent 113 left only remote TeX-stream anchors and explicitly marked local mirrors absent.
evidence_type: missing_source
evidence_ref: Agent 113 report; fixture local-status paragraph before import
files_read:
  - CLAUDE.md
  - AGENTS.md
  - references/primary-sources/gopakumar-vafa-bps-source-anchors-2026-04-30.md
  - reconstitution/swarm-2026-04-30-agent-113-gv-bps-fixture.md
tools_used:
  - sed
  - rg
  - curl
  - gunzip
  - pdftotext
  - shasum
confidence: high
blast_radius: Any theorem or fixture row citing GV would remain remote-only.
minimal_heal: Import local PDF, TeX, text files; record checksums; replace remote TeX anchors by local TeX line anchors.
residual: None for local-source closure.
deciding_evidence: Six local files with SHA-256 checksums and local line anchors.
```

```yaml
id: A1-117-02
severity: 2
status: healed
lens: source-line reproducibility
target: GV I/II arXiv e-print payloads
claim: The remote line anchors from Agent 113 reproduce locally.
broken_step: The fixture did not yet prove that the local files preserve the same TeX line structure.
evidence_type: line_reference
evidence_ref: nl -ba over gv-hep-th-9809187.tex and gv-hep-th-9812127.tex
files_read:
  - references/primary-sources/gv-hep-th-9809187.tex
  - references/primary-sources/gv-hep-th-9812127.tex
tools_used:
  - nl
  - sed
  - rg
confidence: high
blast_radius: Formula and BPS-index citations could drift from the checked source.
minimal_heal: Re-anchor every source-fact row to local TeX lines.
residual: None for GV TeX source anchors.
deciding_evidence: Local anchors listed below.
```

```yaml
id: A1-117-03
severity: 1
status: healed
lens: theorem-strength firewall
target: GV fixture claim-to-source map and non-support list
claim: GV I/II source theorem-grade integrality, PT/GW/MNOP/KKV, convergence, or conifold Stokes data.
broken_step: GV II gives physics BPS-index integers and the sine expansion; it is not a theorem-grade source for enumerative integrality or compact-quintic global analytic claims.
evidence_type: unsupported
evidence_ref: gv-hep-th-9812127.tex:462-535; fixture Exact Non-Support Statements
files_read:
  - references/primary-sources/gv-hep-th-9812127.tex
  - references/primary-sources/gopakumar-vafa-bps-source-anchors-2026-04-30.md
tools_used:
  - rg
  - sed
confidence: high
blast_radius: False transfer into compact-CY, MNOP/PT, CDGP, and conifold-resurgence lanes.
minimal_heal: Preserve the firewall: GV supports physics BPS/sine-expansion facts only.
residual: Separate theorem-grade sources remain required.
deciding_evidence: Dedicated PT/GW/MNOP/KKV, convergence, CDGP, and Stokes fixtures with matched hypotheses.
```

## Repairs Made

Imported local mirrors:

| File | Role | SHA-256 |
|---|---|---|
| `references/primary-sources/gv-hep-th-9809187.pdf` | GV I arXiv PDF mirror, 15 pages. | `864ed0b76d9889e14ac40d39a0d733b58f275f9239ba32220a882ad200a2578b` |
| `references/primary-sources/gv-hep-th-9809187.tex` | GV I single-file arXiv TeX stream. | `ddf1727d45b1def42ea9090af3c1301fd6c18af4af279dbf92a250040b9d5c16` |
| `references/primary-sources/gv-hep-th-9809187.txt` | GV I PDF-derived text from `pdftotext -layout`. | `e67fa3fb642ba100444dbbb2bc81b41fee1361b56b677ff5c2354df409501749` |
| `references/primary-sources/gv-hep-th-9812127.pdf` | GV II arXiv PDF mirror, 20 pages. | `adb9fa3dc3966cf1d02a9d767ccceb1d7318303661f05cf43162d8a176b125c2` |
| `references/primary-sources/gv-hep-th-9812127.tex` | GV II single-file arXiv TeX stream. | `4687315b433ff4ec6ba753809d7ba7f8f48aff44276836faef80dde7c94b1650` |
| `references/primary-sources/gv-hep-th-9812127.txt` | GV II PDF-derived text from `pdftotext -layout`. | `53521081494256978a8807658c71efe6e29499616ea6117cf1ceca5dcf9cad13` |

The arXiv e-print payloads were single gzipped TeX streams. No multi-file
bundle was present. The original source names recorded by Agent 113 were
`9809187.tex` for GV I and `mth2.tex` for GV II; these were mirrored as
the stable local filenames above.

Updated
`references/primary-sources/gopakumar-vafa-bps-source-anchors-2026-04-30.md`
to:

- replace remote TeX-stream anchors by local TeX line anchors;
- record PDF/source/text checksums;
- state that text files are PDF-derived extractions;
- mark the local import obligations complete;
- preserve the non-support firewall for theorem-grade integrality,
  PT/GW/MNOP/KKV, convergence, CDGP periods, OSV/Abel--Jacobi data,
  conifold Stokes constants, and CoHA/Hall/centre claims.

## Local Anchors

- GV I identity and abstract: `references/primary-sources/gv-hep-th-9809187.tex:7-10`, `:19-38`.
- GV I Schwinger determinant and non-perturbative pair creation:
  `references/primary-sources/gv-hep-th-9809187.tex:495-523`,
  `:560-569`, conclusion `:708-736`.
- GV II identity and abstract:
  `references/primary-sources/gv-hep-th-9812127.tex:7-10`,
  `:19-27`.
- GV II partition function convention:
  `references/primary-sources/gv-hep-th-9812127.tex:120-147`.
- GV II five-dimensional BPS index and integer coefficients:
  `references/primary-sources/gv-hep-th-9812127.tex:395-418`,
  `:421-437`, `:462-493`.
- GV II sine multi-cover expansion:
  `references/primary-sources/gv-hep-th-9812127.tex:496-522`.
- GV II physics integrality packaging and inductive extraction:
  `references/primary-sources/gv-hep-th-9812127.tex:524-535`,
  `:540-557`.
- GV II geometric BPS-counting proposal:
  `references/primary-sources/gv-hep-th-9812127.tex:573-580`,
  `:688-710`, `:762-824`, `:864-994`.

## Import Commands

```bash
curl -L --fail --silent --show-error https://arxiv.org/pdf/hep-th/9809187 -o references/primary-sources/gv-hep-th-9809187.pdf
curl -L --fail --silent --show-error https://arxiv.org/pdf/hep-th/9812127 -o references/primary-sources/gv-hep-th-9812127.pdf
curl -L --fail --silent --show-error https://arxiv.org/e-print/hep-th/9809187 | gunzip -c > references/primary-sources/gv-hep-th-9809187.tex
curl -L --fail --silent --show-error https://arxiv.org/e-print/hep-th/9812127 | gunzip -c > references/primary-sources/gv-hep-th-9812127.tex
pdftotext -layout references/primary-sources/gv-hep-th-9809187.pdf references/primary-sources/gv-hep-th-9809187.txt
pdftotext -layout references/primary-sources/gv-hep-th-9812127.pdf references/primary-sources/gv-hep-th-9812127.txt
```

## Verification Run

Commands run:

```bash
file references/primary-sources/gv-hep-th-9809187.pdf references/primary-sources/gv-hep-th-9809187.tex references/primary-sources/gv-hep-th-9812127.pdf references/primary-sources/gv-hep-th-9812127.tex
wc -l references/primary-sources/gv-hep-th-9809187.tex references/primary-sources/gv-hep-th-9812127.tex
pdftotext -layout references/primary-sources/gv-hep-th-9809187.pdf references/primary-sources/gv-hep-th-9809187.txt
pdftotext -layout references/primary-sources/gv-hep-th-9812127.pdf references/primary-sources/gv-hep-th-9812127.txt
pdfinfo references/primary-sources/gv-hep-th-9809187.pdf
pdfinfo references/primary-sources/gv-hep-th-9812127.pdf
shasum -a 256 references/primary-sources/gv-hep-th-9809187.pdf references/primary-sources/gv-hep-th-9809187.tex references/primary-sources/gv-hep-th-9809187.txt references/primary-sources/gv-hep-th-9812127.pdf references/primary-sources/gv-hep-th-9812127.tex references/primary-sources/gv-hep-th-9812127.txt
nl -ba references/primary-sources/gv-hep-th-9809187.tex | sed -n '1,45p;490,575p;704,740p'
nl -ba references/primary-sources/gv-hep-th-9812127.tex | sed -n '1,35p;115,155p;390,540p'
nl -ba references/primary-sources/gv-hep-th-9812127.tex | sed -n '568,585p;688,710p;760,824p;864,994p'
rg -n "Local mirror absent|local mirror absent|Remote Source Facts|not mirrored locally" references/primary-sources/gopakumar-vafa-bps-source-anchors-2026-04-30.md
git diff --cached --check -- references/primary-sources/gopakumar-vafa-bps-source-anchors-2026-04-30.md references/primary-sources/gv-hep-th-9809187.pdf references/primary-sources/gv-hep-th-9809187.tex references/primary-sources/gv-hep-th-9809187.txt references/primary-sources/gv-hep-th-9812127.pdf references/primary-sources/gv-hep-th-9812127.tex references/primary-sources/gv-hep-th-9812127.txt reconstitution/swarm-2026-04-30-agent-117-gv-local-import.md
```

Results:

- GV I PDF: PDF 1.4, 15 pages; GV II PDF: PDF 1.4, 20 pages.
- GV I TeX: ASCII TeX, 841 lines; GV II TeX: ASCII TeX, 1012 lines.
- All six SHA-256 checksums are recorded in the fixture and above.
- Local line anchors reproduce the Agent 113 remote source ranges.
- The stale "local mirror absent" status was removed from the GV fixture.
- `git diff --cached --check` reports preserved blank lines at EOF in the
  two imported arXiv TeX streams. They were left unnormalised to preserve
  the source payloads.
- No TeX manuscript build was run; this was a source-fixture import only.

## Residual Theorem Obligations

GV I/II now give local source-grade support for the physical BPS
interpretation, Schwinger one-loop mechanism, sine multi-cover formula,
and integer BPS-index coefficients in GV's variables. They do not prove
mathematical GV integrality, PT/GW or MNOP equivalence, KKV
normalisation, compact-quintic all-genus BCOV equality, convergence,
CDGP period recovery, OSV or Abel--Jacobi normalisations, conifold
Stokes constants, or any Hall/CoHA/centre statement. Those remain
separate source lanes.
