# Agent 120 CDGP Local Import Report, 2026-04-30

Scope. Owned writable surfaces:

- `references/primary-sources/mirror-quintic-cdgp-period-source-anchors-2026-04-30.md`
- `references/primary-sources/cdgp-nucl-phys-b359-1991.pdf`
- `references/primary-sources/cdgp-nucl-phys-b359-1991.txt`
- `reconstitution/swarm-2026-04-30-agent-120-cdgp-local-import.md`

No source-provenance row or manuscript source file was edited.

## Valid Attacks

```yaml
- id: A2-120-01
  severity: 2
  status: healed
  lens: local primary-source admissibility
  target: Agent 112 CDGP fixture
  claim: CDGP period conventions can be locally source-graded.
  broken_step: Agent 112 had only remote PDF anchors, no tracked local CDGP PDF or text extraction.
  evidence_type: missing_source
  evidence_ref: "Agent 112 report A1-112-01; fixture local status before this pass"
  files_read:
    - reconstitution/swarm-2026-04-30-agent-112-cdgp-period-fixture.md
    - references/primary-sources/mirror-quintic-cdgp-period-source-anchors-2026-04-30.md
  tools_used:
    - curl
    - pdftotext
    - shasum
    - nl
  confidence: high
  blast_radius: Picard-Fuchs, conifold, branch-period, period-basis, mirror-map, and Table 4 claims remained remote-only.
  minimal_heal: Import local PDF/text, record checksums, and replace remote anchors with local file anchors.
  residual: Publisher PDF provenance is still blocked; local source comes from a public Utrecht mirror.
  deciding_evidence: Publisher or AMS/IP PDF import, if access later becomes available.

- id: A2-120-02
  severity: 3
  status: healed
  lens: provenance
  target: CDGP PDF source choice
  claim: A publisher or AMS/IP source should be preferred when accessible.
  broken_step: ScienceDirect and AMS/IP access did not yield an importable PDF from this environment.
  evidence_type: other
  evidence_ref: "ScienceDirect article and pdfft endpoints returned HTTP 403; AMS/IP DOI resolved to https://www.ams.org/amsip/009, then HTTP 403; guessed AMS chapter PDF URLs returned HTTP 403"
  files_read: []
  tools_used:
    - curl -I
    - web search
  confidence: high
  blast_radius: Provenance cannot be called publisher-downloaded.
  minimal_heal: Import the Utrecht mirror, record exact URL, redirect, checksums, PDF metadata, and limitation.
  residual: Publisher/AMS import remains a better provenance target.
  deciding_evidence: Successful download from ScienceDirect, AMS/IP, or another publisher-authorized source.

- id: A2-120-03
  severity: 2
  status: healed
  lens: extraction quality
  target: local CDGP text anchors
  claim: The local text extraction can support exact formula transcription.
  broken_step: The PDF text layer is OCR from a journal scan; several displayed formulas are garbled or elided.
  evidence_type: other
  evidence_ref: "cdgp-nucl-phys-b359-1991.txt:1023-1028, :1778, :2405 for the incomplete (3.23) recovery"
  files_read:
    - references/primary-sources/cdgp-nucl-phys-b359-1991.txt
  tools_used:
    - rg
    - nl
  confidence: high
  blast_radius: Formula-level theorem use cannot rely on OCR text alone for every displayed equation.
  minimal_heal: Record local line anchors and state that the local PDF controls exact glyph checks.
  residual: Clean text/TeX-grade transcription for equation (3.23) and other OCR-poor displays remains outside this fixture's stable core.
  deciding_evidence: Visual PDF transcription checked against the scan, or a cleaner legitimate source.
```

## Repairs Made

Imported the local CDGP journal scan:

```bash
curl -L --fail --show-error -o references/primary-sources/cdgp-nucl-phys-b359-1991.pdf https://www.staff.science.uu.nl/~beuke106/HypergeometricFunctions/COGP.pdf
pdftotext -layout references/primary-sources/cdgp-nucl-phys-b359-1991.pdf references/primary-sources/cdgp-nucl-phys-b359-1991.txt
```

Checksums:

```text
5c5033bfe291e9a8f77e1d6543aa9be9134681c93106c8258fe9375926d8d617  references/primary-sources/cdgp-nucl-phys-b359-1991.pdf
c07473e9a72595b712a839a8cd35c1938d04e3b5469be7e68a5604afe785cc9a  references/primary-sources/cdgp-nucl-phys-b359-1991.txt
```

PDF metadata:

- title: `PII: 0550-3213(91)90292-6`
- pages: `54`
- file size: `3889562` bytes
- PDF version: `1.2`
- encrypted: `no`

Text extraction size: `2700` lines, `136819` bytes.

Updated
`references/primary-sources/mirror-quintic-cdgp-period-source-anchors-2026-04-30.md`
to record local checksums, blocked publisher/AMS attempts, the Utrecht mirror
provenance, and local source anchors.

## Local Anchors

| Fact | Local anchors |
|---|---|
| Family and true coordinate | `references/primary-sources/cdgp-nucl-phys-b359-1991.txt:163-184`; `:275-282` |
| Conifold branch and shrinking cycle | `references/primary-sources/cdgp-nucl-phys-b359-1991.txt:313-328`; `:1201-1206`; `:1968-1975` |
| Period series and Picard-Fuchs equation | `references/primary-sources/cdgp-nucl-phys-b359-1991.txt:767-793`; `:804-836` |
| Barnes continuation and branch periods | `references/primary-sources/cdgp-nucl-phys-b359-1991.txt:880-906`; `:913-984` |
| Integral period basis and monodromy | `references/primary-sources/cdgp-nucl-phys-b359-1991.txt:1023-1069`; `:1078-1115` |
| Prepotential and mirror map | `references/primary-sources/cdgp-nucl-phys-b359-1991.txt:1119-1179`; `:1643-1813` |
| Yukawa expansion and Table 4 | `references/primary-sources/cdgp-nucl-phys-b359-1991.txt:1332-1367`; `:1824-1832`; `:1893-1953` |

Extraction limitation. The local text anchor stream is formula-poor. It is good
for navigation, section/equation labels, and local provenance. Exact glyphs for
OCR-poor displayed formulas remain PDF-controlled. The displayed relation
(3.23) is not fully recovered by `pdftotext -layout`; the text gives the
surrounding discussion at `:1023-1028` and later references at `:1778`, `:2405`.

## Convention Status

Local CDGP anchors support the mirror-quintic family, the true `psi^5`
coordinate, the conifold branch `psi=1`, the branch-period/monodromy mechanism,
and the genus-zero mirror-map/Yukawa package. After translating to the frontier
coordinate `z=(5 psi)^(-5)`, the conifold branch is `z_c=5^{-5}`.

The frontier `z`-Picard-Fuchs display is convention-compatible after this
translation. The frontier `psi`-Picard-Fuchs display remains non-source-grade if
`psi` denotes CDGP's original family parameter; it should be renamed to `z` or
rewritten in the original `psi` variable by the main thread.

## Verification Run

```bash
sed -n '1,260p' CLAUDE.md
sed -n '1,260p' AGENTS.md
sed -n '1,260p' /Users/raeez/ecosystem/skills/shared/attack-heal-swarm/protocol.md
sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-112-cdgp-period-fixture.md
curl -L -I --max-time 30 https://www.sciencedirect.com/science/article/pii/0550321391902926
curl -L -I --max-time 30 'https://www.sciencedirect.com/science/article/pii/0550321391902926/pdfft?isDTMRedir=true&download=true'
curl -L -I --max-time 30 https://doi.org/10.1090/amsip/009/02
curl -L -I --max-time 30 https://www.ams.org/books/amsip/009/amsip009-02.pdf
curl -L -I --max-time 30 https://www.ams.org/books/amsip/009/amsip-009-02.pdf
curl -L -I --max-time 30 https://www.staff.science.uu.nl/~beuke106/HypergeometricFunctions/COGP.pdf
curl -L --fail --show-error -o references/primary-sources/cdgp-nucl-phys-b359-1991.pdf https://www.staff.science.uu.nl/~beuke106/HypergeometricFunctions/COGP.pdf
pdftotext -layout references/primary-sources/cdgp-nucl-phys-b359-1991.pdf references/primary-sources/cdgp-nucl-phys-b359-1991.txt
pdfinfo references/primary-sources/cdgp-nucl-phys-b359-1991.pdf
file references/primary-sources/cdgp-nucl-phys-b359-1991.pdf
shasum -a 256 references/primary-sources/cdgp-nucl-phys-b359-1991.pdf
shasum -a 256 references/primary-sources/cdgp-nucl-phys-b359-1991.txt
wc -l -c references/primary-sources/cdgp-nucl-phys-b359-1991.txt
rg -n 'x_i\^5|psi|Picard|Fuchs|hypergeometric|varpi|prepotential|Yukawa|Table 4|rational curves|conifold|S3|S 3|monodromy|symplectic|instanton' references/primary-sources/cdgp-nucl-phys-b359-1991.txt
rg -n '\(3\.23\)|\(2\.11\)|relation \(3\.23\)|relation of the form|CYCLES CORRESPONDING' references/primary-sources/cdgp-nucl-phys-b359-1991.txt
```

No TeX build was run; this pass changed source fixtures and imported primary
source files only.

## Residual Theorem Obligations

1. Replace the Utrecht mirror with a publisher or AMS/IP PDF if access becomes
   available.
2. Perform a visual PDF transcription check for equation (3.23) and any other
   OCR-poor displayed formulas before theorem-grade use.
3. Main thread must repair the frontier `psi`-Picard-Fuchs display by renaming
   the variable to `z` or rewriting it in CDGP's original `psi` coordinate.
4. Keep `|Omega_1/Omega_0|(5^{-5})=7.590896...` as local arithmetic, not a CDGP
   source fact, until a committed arithmetic ledger/script owns it.
5. Abel--Jacobi normalization, OSV rate, GV/PT integrality, and conifold
   Stokes/resurgence remain separate source obligations.

## Files Changed

- `references/primary-sources/mirror-quintic-cdgp-period-source-anchors-2026-04-30.md`
- `references/primary-sources/cdgp-nucl-phys-b359-1991.pdf`
- `references/primary-sources/cdgp-nucl-phys-b359-1991.txt`
- `reconstitution/swarm-2026-04-30-agent-120-cdgp-local-import.md`
