# Agent 128 OSV Local Import Report, 2026-04-30

Lane: OSV attractor comparison and physical rate normalisation, separated
from CoHA.

Writable surface used:

- `references/primary-sources/osv-attractor-rate-source-anchors-2026-04-30.md`
- `references/primary-sources/osv-hep-th-0405146.pdf`
- `references/primary-sources/osv-hep-th-0405146.tex`
- `references/primary-sources/osv-hep-th-0405146.txt`
- `reconstitution/swarm-2026-04-30-agent-128-osv-local-import.md`

No TeX manuscript file and no `references/source-provenance.md` edit was
made in this pass.

## Stable Core

OSV is now repository-local primary evidence for:

- the conjectural relation `Z_BH=|Z_top|^2`;
- the mixed ensemble with magnetic charges fixed and electric charges
  summed against potentials;
- the corrected black-hole free energy and Legendre-transform relation;
- the attractor variables `C X^Lambda=p^Lambda+i phi^Lambda/pi`;
- the topological-string normalisation
  `t^A=(p^A+i phi^A/pi)/(p^0+i phi^0/pi)` and
  `g_top=+-4 pi i/(p^0+i phi^0/pi)`;
- the background-dependence warning.

OSV is not evidence for `5 log 5`, fixed-class quintic coefficient
growth, GV/HKQ/CDGP normalisation, compact-CY closure, or any CoHA claim.

## Attack Ledger

```yaml
id: A1-128-01
severity: 2
status: healed
lens: local-source admissibility
target: references/primary-sources/osv-attractor-rate-source-anchors-2026-04-30.md
claim: The OSV fixture can be used as local source support.
broken_step: Agent 122's fixture explicitly recorded local mirrors as absent and used remote arXiv-source anchors.
evidence_type: missing_source
evidence_ref: "pre-edit fixture Local status; git status showed only the markdown fixture, no osv-hep-th-0405146.{pdf,tex,txt}"
files_read:
  - CLAUDE.md
  - references/primary-sources/osv-attractor-rate-source-anchors-2026-04-30.md
  - reconstitution/swarm-2026-04-30-agent-122-osv-attractor-fixture.md
tools_used:
  - sed
  - git status
confidence: high
blast_radius: Remote-only facts could be cited as repository-local primary evidence.
minimal_heal: Import local PDF, TeX source, and PDF-text mirror; record checksums and local line anchors.
residual: Future source-provenance row belongs to the main thread, not this agent.
deciding_evidence: Local files and checksums recorded below.
```

```yaml
id: A1-128-02
severity: 2
status: healed
lens: anchor locality
target: OSV source-fact rows
claim: OSV facts are anchored locally.
broken_step: The fact rows cited `black.tex` remote line numbers rather than paths under references/primary-sources.
evidence_type: line_reference
evidence_ref: "nl -ba references/primary-sources/osv-hep-th-0405146.tex over OSV source ranges"
files_read:
  - references/primary-sources/osv-hep-th-0405146.tex
  - references/primary-sources/osv-hep-th-0405146.txt
tools_used:
  - nl
  - rg
  - pdftotext
confidence: high
blast_radius: Later theorem lanes could lose reproducibility if remote arXiv formatting changes.
minimal_heal: Re-anchor each source fact to the local TeX mirror, with PDF-text anchors where useful.
residual: Exact displayed glyphs remain TeX/PDF controlled, not PDF-text controlled.
deciding_evidence: Fixture rows `OSV-id-abstract` through `OSV-quintic-only-background-example`.
```

```yaml
id: A1-128-03
severity: 1
status: healed
lens: numerical-rate support
target: frontier_mnop_framing_volume.tex:314-315 and :348-349
claim: OSV sources the comparison value `5 log 5`.
broken_step: The local OSV source and PDF text contain no `5 log 5`, `log 5`, `5\\log`, or `5^{-5}` occurrence.
evidence_type: unsupported
evidence_ref: "rg -n -F negative search over references/primary-sources/osv-hep-th-0405146.{tex,txt}"
files_read:
  - references/primary-sources/osv-hep-th-0405146.tex
  - references/primary-sources/osv-hep-th-0405146.txt
  - frontier_mnop_framing_volume.tex
tools_used:
  - rg
  - nl
confidence: high
blast_radius: A CDGP-coordinate arithmetic value could be falsely promoted to OSV entropy-rate source support.
minimal_heal: State that `5 log 5=-log(5^{-5})` is a CDGP-coordinate arithmetic identity if used, not an OSV source fact.
residual: Separate arithmetic/source ledger for `5 log 5`.
deciding_evidence: A matched-conventions derivation or a different primary source.
```

```yaml
id: A1-128-04
severity: 2
status: healed
lens: fixed-class asymptotics
target: frontier_mnop_framing_volume.tex:623-627
claim: OSV proves fixed-class quintic BPS coefficient growth or convergence.
broken_step: OSV defines a mixed black-hole ensemble and explicitly distinguishes mixed entropy from microcanonical entropy except in a large-electric-charge steepest-descent approximation.
evidence_type: source_conflict
evidence_ref: "references/primary-sources/osv-hep-th-0405146.tex:693-729; negative rg for growth/convergence/fixed-class quintic asymptotics"
files_read:
  - references/primary-sources/osv-hep-th-0405146.tex
  - references/primary-sources/osv-hep-th-0405146.txt
tools_used:
  - rg
  - nl
confidence: high
blast_radius: A mixed ensemble conjecture could be misread as theorem-grade asymptotics for `n_d^0`.
minimal_heal: Fixture states that a saddle/Laplace-inversion theorem is required before any fixed-class coefficient-growth use.
residual: Coefficient-growth or convergence theorem remains open.
deciding_evidence: A proof relating OSV mixed black-hole degeneracies to fixed quintic BPS coefficients with matched variables.
```

```yaml
id: A1-128-05
severity: 2
status: healed
lens: convention normalisation
target: OSV/CDGP/GV/HKQ/frontier comparison
claim: OSV variables can be compared numerically with CDGP/GV/HKQ/frontier variables without a bridge.
broken_step: OSV uses `C X`, electric potentials divided by `pi`, `g_top=+-4 pi i/(...)`, and a mixed ensemble; CDGP/HKQ/GV/frontier fixtures use mirror-period, `2 pi i`, BPS-table, and exponential conventions that are not automatically identical.
evidence_type: line_reference
evidence_ref: "references/primary-sources/osv-hep-th-0405146.tex:645-868; GV/CDGP/HKQ fixture convention ledgers"
files_read:
  - references/primary-sources/osv-attractor-rate-source-anchors-2026-04-30.md
  - references/primary-sources/gopakumar-vafa-bps-source-anchors-2026-04-30.md
  - references/primary-sources/mirror-quintic-cdgp-period-source-anchors-2026-04-30.md
  - references/primary-sources/compact-cy-bcov-hkq-source-anchors-2026-04-30.md
tools_used:
  - sed
  - rg
confidence: high
blast_radius: Missing factors of `pi`, `2 pi i`, branch, sign, or ensemble could move the claimed rate.
minimal_heal: Fixture records the exact seven-item convention bridge required before numerical theorem use.
residual: The bridge is not yet proved.
deciding_evidence: A local convention note proving the OSV/CDGP/GV/HKQ/frontier identifications.
```

```yaml
id: A1-128-06
severity: 3
status: healed
lens: swarm ownership
target: references/source-provenance.md and TeX files
claim: This pass should update source provenance or manuscript wording directly.
broken_step: User scope assigned `references/source-provenance.md` to Agent 126 and forbade TeX manuscript edits.
evidence_type: line_reference
evidence_ref: "current user scope; git status shows unrelated TeX and source-provenance changes already present"
files_read:
  - frontier_mnop_framing_volume.tex
tools_used:
  - git status
  - nl
confidence: high
blast_radius: Cross-agent overwrite or ownership violation.
minimal_heal: Do not edit those files; record residual main-thread updates.
residual: Manuscript still has wording saying OSV source row/mirror is missing even though the mirror is now local.
deciding_evidence: Integration-owner TeX/source-provenance pass.
```

## Local Checksums And Anchors

| File | SHA-256 | Notes |
|---|---|---|
| `references/primary-sources/osv-hep-th-0405146.pdf` | `c112f937de2d795722676958080bd709fc8cc8a0aa6f9af8add0027b35681faa` | arXiv v2 PDF, 32 pages, 300806 bytes. |
| `references/primary-sources/osv-hep-th-0405146.tex` | `e9b25649b656597dae7f7ade2964700d399135b6ab555f44a88018f49b67405f` | gzipped arXiv source payload extracted from original `black.tex`, 1915 lines. |
| `references/primary-sources/osv-hep-th-0405146.txt` | `cc8fc4890065a492b4c23252a778a01cc7772bef3a1a31ee91957335ccfc67e2` | `pdftotext -layout` extraction, 1378 lines. |
| `/tmp/osv-hep-th-0405146v2.eprint` | `9120c64fdf9c57bbb0fd3d1421295be9c25ac0b4889087524a7e86b2f2241a90` | transient arXiv e-print payload. |

Primary local anchors:

- OSV abstract: `references/primary-sources/osv-hep-th-0405146.tex:277-288`.
- Main conjecture and attractor variables:
  `references/primary-sources/osv-hep-th-0405146.tex:338-356`;
  `:363-364`.
- Semiclassical attractor equations:
  `references/primary-sources/osv-hep-th-0405146.tex:522-594`.
- Corrected free energy and Legendre transform:
  `references/primary-sources/osv-hep-th-0405146.tex:617-691`.
- Mixed ensemble and microcanonical warning:
  `references/primary-sources/osv-hep-th-0405146.tex:693-729`.
- Topological-string normalisation:
  `references/primary-sources/osv-hep-th-0405146.tex:763-868`.
- Simplified-derivation warning:
  `references/primary-sources/osv-hep-th-0405146.tex:874-884`;
  `:932-941`.
- Beta-zero index check:
  `references/primary-sources/osv-hep-th-0405146.tex:1155-1216`;
  `:1280-1316`.
- Polarisation/chemical-potential bridge:
  `references/primary-sources/osv-hep-th-0405146.tex:1523-1583`;
  `:1586-1645`.
- Background-dependence warning:
  `references/primary-sources/osv-hep-th-0405146.tex:1688-1801`.
- Quintic-only background example:
  `references/primary-sources/osv-hep-th-0405146.tex:1764-1773`.

Local PDF-text anchors were also recorded in the fixture for the main
conjecture, mixed ensemble, normalisation, beta-zero check, and
background-dependence passages.

## Repairs Made

1. Imported the OSV arXiv v2 PDF, TeX source, and PDF-text extraction
   into `references/primary-sources`.
2. Replaced the remote-only OSV fixture with a local mirror ledger,
   checksums, local TeX anchors, and PDF-text anchors.
3. Preserved the valid Agent 122 firewall: OSV supports the mixed
   attractor comparison and normalisations, not `5 log 5` or coefficient
   growth.
4. Added the exact convention bridge needed before comparing OSV to
   CDGP/GV/HKQ/frontier data.
5. Recorded that `references/source-provenance.md` and TeX updates remain
   out of scope for this agent.

## Files Changed And Staged

Staged by this pass:

- `references/primary-sources/osv-attractor-rate-source-anchors-2026-04-30.md`
- `references/primary-sources/osv-hep-th-0405146.pdf`
- `references/primary-sources/osv-hep-th-0405146.tex`
- `references/primary-sources/osv-hep-th-0405146.txt`
- `reconstitution/swarm-2026-04-30-agent-128-osv-local-import.md`

`references/source-provenance.md` was already modified/staged in the
shared worktree and remains untouched by this pass.

## Commands Run

Instruction and context reads:

```bash
sed -n '1,220p' CLAUDE.md
sed -n '1,220p' /Users/raeez/ecosystem/skills/claude-code/attack-heal-swarm-plugin/skills/attack-heal-swarm/SKILL.md
sed -n '1,260p' /Users/raeez/ecosystem/skills/shared/attack-heal-swarm/protocol.md
sed -n '1,240p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '129,205p' /Users/raeez/ecosystem/INVARIANTS.md
sed -n '143,170p' /Users/raeez/ecosystem/AGENTS-HARNESS.md
sed -n '1,220p' main.tex
sed -n '1,220p' commands.tex
sed -n '1,220p' mathmacros.tex
nl -ba frontier_mnop_framing_volume.tex | sed -n '290,360p;590,635p;730,840p'
```

Neighboring fixture and prior-report reads:

```bash
sed -n '1,260p' references/primary-sources/gopakumar-vafa-bps-source-anchors-2026-04-30.md
sed -n '1,260p' references/primary-sources/mirror-quintic-cdgp-period-source-anchors-2026-04-30.md
sed -n '1,260p' references/primary-sources/compact-cy-bcov-hkq-source-anchors-2026-04-30.md
sed -n '1,260p' references/primary-sources/osv-attractor-rate-source-anchors-2026-04-30.md
sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-122-osv-attractor-fixture.md
```

Import and checksum commands:

```bash
curl -L --fail --silent --show-error https://arxiv.org/pdf/hep-th/0405146v2 \
  -o references/primary-sources/osv-hep-th-0405146.pdf
curl -L --fail --silent --show-error https://arxiv.org/e-print/hep-th/0405146v2 \
  -o /tmp/osv-hep-th-0405146v2.eprint
gunzip -c /tmp/osv-hep-th-0405146v2.eprint \
  > references/primary-sources/osv-hep-th-0405146.tex
pdftotext -layout references/primary-sources/osv-hep-th-0405146.pdf \
  references/primary-sources/osv-hep-th-0405146.txt
shasum -a 256 \
  references/primary-sources/osv-hep-th-0405146.pdf \
  references/primary-sources/osv-hep-th-0405146.tex \
  references/primary-sources/osv-hep-th-0405146.txt \
  /tmp/osv-hep-th-0405146v2.eprint
wc -l -c references/primary-sources/osv-hep-th-0405146.tex \
  references/primary-sources/osv-hep-th-0405146.txt
pdfinfo references/primary-sources/osv-hep-th-0405146.pdf
```

Anchor and search commands:

```bash
nl -ba references/primary-sources/osv-hep-th-0405146.tex \
  | sed -n '270,390p;520,730p;760,935p;1150,1220p;1280,1320p;1685,1805p'
nl -ba references/primary-sources/osv-hep-th-0405146.tex \
  | sed -n '390,490p;930,950p;1520,1650p;1888,1915p'
nl -ba references/primary-sources/osv-hep-th-0405146.txt \
  | sed -n '80,170p;390,430p;535,570p;790,835p;1160,1200p;1210,1245p'
rg -n -i "Z_BH|Z_top|mixed|attractor|free energy|legendre|topological string|background|holomorphic anomaly|quintic|asymptotic|coefficient|entropy" \
  references/primary-sources/osv-hep-th-0405146.tex
rg -n -i "Z_BH|Z_top|mixed|attractor|free energy|legendre|topological string|background|holomorphic anomaly|quintic|asymptotic|coefficient|entropy" \
  references/primary-sources/osv-hep-th-0405146.txt
```

Negative-support commands:

```bash
rg -n -F -e '5 log 5' -e 'log 5' -e '\log 5' -e '5\log' \
  references/primary-sources/osv-hep-th-0405146.tex \
  references/primary-sources/osv-hep-th-0405146.txt
rg -n -F -e '5 log 5' -e '5\log 5' -e '5\log' -e '\log 5' \
  -e 'log(5' -e '5^{-5}' -e '5^-5' -e '5^(-5)' \
  references/primary-sources/osv-hep-th-0405146.tex \
  references/primary-sources/osv-hep-th-0405146.txt
rg -n -F -e 'growth' -e 'coefficient' -e 'coefficients' \
  -e 'asymptotic' -e 'asymptotics' -e 'convergence' -e 'converge' \
  -e 'radius' -e '5^' -e '5^{-5}' -e 'log 5' -e '5 log' -e '5\log' \
  references/primary-sources/osv-hep-th-0405146.tex \
  references/primary-sources/osv-hep-th-0405146.txt
rg -n -i "coefficient|growth|asymptotic|convergence|quintic" \
  references/primary-sources/osv-hep-th-0405146.tex \
  references/primary-sources/osv-hep-th-0405146.txt
```

One regex-form search with unescaped braces failed:

```bash
rg -n -i "growth|coefficient|coefficients|asymptotic|asymptotics|convergence|converge|radius|5\\^|5\\^\\{-5\\}|5\\^{-5\\}|log\\s*5|5\\s*log" \
  references/primary-sources/osv-hep-th-0405146.tex \
  references/primary-sources/osv-hep-th-0405146.txt
```

It was replaced by the fixed-string searches above.

Git and scope commands:

```bash
pwd
git status --short
git status --short -- references/primary-sources/osv-attractor-rate-source-anchors-2026-04-30.md \
  references/primary-sources/osv-hep-th-0405146.pdf \
  references/primary-sources/osv-hep-th-0405146.tex \
  references/primary-sources/osv-hep-th-0405146.txt \
  reconstitution/swarm-2026-04-30-agent-128-osv-local-import.md \
  references/source-provenance.md
git add -- references/primary-sources/osv-attractor-rate-source-anchors-2026-04-30.md \
  references/primary-sources/osv-hep-th-0405146.pdf \
  references/primary-sources/osv-hep-th-0405146.tex \
  references/primary-sources/osv-hep-th-0405146.txt \
  reconstitution/swarm-2026-04-30-agent-128-osv-local-import.md
git diff --cached --name-only -- references/primary-sources/osv-attractor-rate-source-anchors-2026-04-30.md \
  references/primary-sources/osv-hep-th-0405146.pdf \
  references/primary-sources/osv-hep-th-0405146.tex \
  references/primary-sources/osv-hep-th-0405146.txt \
  reconstitution/swarm-2026-04-30-agent-128-osv-local-import.md
git diff --cached --check -- references/primary-sources/osv-attractor-rate-source-anchors-2026-04-30.md \
  reconstitution/swarm-2026-04-30-agent-128-osv-local-import.md
```

Verification caveat: `git diff --cached --check` over the full owned set
flags trailing whitespace inside the imported arXiv TeX source at local
lines 1256, 1510, 1528, 1529, 1552, and 1711. These bytes were preserved
because `osv-hep-th-0405146.tex` is a primary-source mirror whose SHA-256
matches the arXiv e-print extraction. The authored markdown files pass
`git diff --cached --check`.

## Residual Theorem And Source Obligations

1. `5 log 5` still needs its own arithmetic/source ledger. OSV does not
   source it.
2. A matched OSV/CDGP/GV/HKQ/frontier convention bridge is required
   before any numerical comparison becomes theorem-grade.
3. A saddle or Laplace-inversion theorem is required before OSV's mixed
   ensemble can imply fixed-class quintic BPS coefficient growth.
4. The manuscript wording that calls the OSV source row/mirror missing
   is now stale, but TeX updates are outside this agent's scope.
5. `references/source-provenance.md` still needs any OSV row from the
   integration owner or Agent 126.
