# Agent 113 GV BPS Fixture Report, 2026-04-30

Scope. Writable surface restricted to:

- `references/primary-sources/gopakumar-vafa-bps-source-anchors-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-113-gv-bps-fixture.md`

No other file was edited.

## Source Facts

Local search found no GV I/II mirror under `references/primary-sources`.
The only durable source status available in this checkout is therefore
remote-candidate status.

Remote arXiv records inspected:

- `GV-I`: Gopakumar--Vafa, "M-Theory and Topological Strings--I",
  arXiv `hep-th/9809187`, DataCite DOI
  `10.48550/arXiv.hep-th/9809187`, report `HUTP-98/A069`.
- `GV-II`: Gopakumar--Vafa, "M-Theory and Topological Strings--II",
  arXiv `hep-th/9812127`, DataCite DOI
  `10.48550/arXiv.hep-th/9812127`, report `HUTP-98/A070`.

Remote TeX stream facts:

- GV I `9809187.tex:495-523` and `:560-569` support the Schwinger
  determinant and pair-creation physical mechanism.
- GV II `mth2.tex:421-437` and `:462-493` support the BPS-index
  interpretation with integer coefficients `alpha_r^(n_i)`.
- GV II `mth2.tex:496-522` supports the sine multi-cover formula with
  `1/k`, `(2 sin(k lambda/2))^(2r-2)`, and
  `exp[-2 pi k sum_i n_i t_i]`.
- GV II `mth2.tex:524-535` supports only the physics-source integrality
  packaging in terms of BPS-index integers.

## Attack Ledger

```yaml
id: A1-113-01
severity: 2
status: healed
lens: source-control / local-vs-remote
target: references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md:24 and frontier_mnop_framing_volume.tex:585-592
claim: The frontier note can cite the GV sine expansion.
broken_step: No local GV mirror exists, so citation alone is not local source-grade.
evidence_type: missing_source
evidence_ref: find references/primary-sources -maxdepth 1 -type f with GV/Gopakumar/Vafa/9809187/9812127 patterns; arXiv source streams inspected remotely
files_read:
  - CLAUDE.md
  - AGENTS.md
  - references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md
  - references/primary-sources/compact-cy-source-fixture-control-surface-2026-04-30.md
  - frontier_mnop_framing_volume.tex
tools_used:
  - rg
  - find
  - curl
  - gunzip
  - nl
confidence: high
blast_radius: Any theorem-grade import of GV formula into main.tex would be unsupported locally.
minimal_heal: Add a GV fixture with stable remote identifiers, exact remote anchors, and local import obligations.
residual: Import local GV PDF/source/text mirrors and checksums.
deciding_evidence: Local files under references/primary-sources with line anchors reproducing the remote TeX anchors.
```

```yaml
id: A1-113-02
severity: 2
status: healed
lens: convention audit
target: frontier_mnop_framing_volume.tex:585-592
claim: The displayed frontier formula matches the GV source formula.
broken_step: GV II writes exp[-2 pi k sum_i n_i t_i], while the frontier writes exp[-m beta dot t]; GV II uses alpha_r^(n_i), not n_beta^g.
evidence_type: source_conflict
evidence_ref: GV II arXiv source mth2.tex:496-522
files_read:
  - frontier_mnop_framing_volume.tex
  - /tmp extracted GV II source stream
tools_used:
  - curl
  - gunzip
  - nl
confidence: high
blast_radius: A silent convention mismatch can alter exponential scales and period comparisons.
minimal_heal: Record the six import conventions needed before theorem use.
residual: Principal must decide whether frontier t absorbs 2 pi and how alpha_r^(n_i) is named.
deciding_evidence: A local convention paragraph or formula row after GV import.
```

```yaml
id: A1-113-03
severity: 1
status: healed
lens: theorem-strength firewall
target: frontier_mnop_framing_volume.tex:593 and :617-620
claim: GV source facts prove n_beta^g in Z and equality in Z[[e^-t]] after KKV normalisation.
broken_step: GV II supplies physical BPS-index integers alpha_r^(n_i); it does not prove mathematical GV/PT/GW/MNOP integrality or the KKV normalisation.
evidence_type: unsupported
evidence_ref: GV II mth2.tex:524-535; MNOP/PT/DT fixture non-support rows for PT/GW theorem-grade support
files_read:
  - references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md
  - references/primary-sources/compact-cy-bcov-hkq-source-anchors-2026-04-30.md
tools_used:
  - rg
  - sed
confidence: high
blast_radius: False theorem import into compact-CY or Vol III comparison lanes.
minimal_heal: Mark GV integrality as physics-source support only and list PT/GW/MNOP/KKV as separate obligations.
residual: Separate theorem-grade source lane for mathematical integrality and PT/GW.
deciding_evidence: Local imported PT/GW/KKV/MNOP theorem source with hypotheses matched to the quintic.
```

```yaml
id: A1-113-04
severity: 2
status: healed
lens: asymptotic and Stokes firewall
target: frontier_mnop_framing_volume.tex:623-634 and :655-708
claim: GV I/II source the convergence and conifold Stokes normalisation targets.
broken_step: GV I/II source the Schwinger mechanism and sine formula, but not a genus-zero BPS convergence theorem, CDGP period normalisation, Strominger conifold identification, large-order constant, or S_c=1.
evidence_type: unsupported
evidence_ref: rg over GV I/II source streams for convergence/Stokes/resurgence terms; existing quintic/HKQ fixtures list these as missing
files_read:
  - references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md
  - references/primary-sources/compact-cy-bcov-hkq-source-anchors-2026-04-30.md
  - frontier_mnop_framing_volume.tex
tools_used:
  - rg
  - sed
confidence: high
blast_radius: Would falsely erase compact-CY target obstruction components.
minimal_heal: Fixture lists convergence, CDGP, OSV, Strominger, Schwinger/Vafa, Shenker--Marino, and Cecotti--Codesido--Marino as non-support.
residual: Dedicated conifold-resurgence and CDGP fixtures remain required.
deciding_evidence: Local source fixtures for those rows with exact formula and normalisation anchors.
```

```yaml
id: A1-113-05
severity: 3
status: healed
lens: CoHA separation
target: references/primary-sources/compact-cy-source-fixture-control-surface-2026-04-30.md:35 and frontier_mnop_framing_volume.tex:812-817
claim: GV BPS source facts can be routed through CoHA/centre evidence.
broken_step: The control surface explicitly routes GV BPS/resummation to a non-CoHA fixture.
evidence_type: line_reference
evidence_ref: compact-cy-source-fixture-control-surface-2026-04-30.md GV target row and CoHA exclusion list
files_read:
  - references/primary-sources/compact-cy-source-fixture-control-surface-2026-04-30.md
tools_used:
  - sed
confidence: high
blast_radius: CoHA fixture would carry compact-CY physics facts it does not source.
minimal_heal: New GV fixture states no Hall, CoHA, or E_2-centre support.
residual: None for this source-control surface.
deciding_evidence: Fixture remains separated and source-provenance merge adds a distinct GV row.
```

## Repairs Made

Added `references/primary-sources/gopakumar-vafa-bps-source-anchors-2026-04-30.md`
with:

- stable GV I/II identifiers and remote source payload status;
- exact remote TeX-stream anchors for BPS interpretation, Schwinger
  mechanism, sine expansion, and physics integrality packaging;
- a convention ledger comparing GV source variables with the frontier
  formula;
- claim-to-source map for the relevant frontier anchors;
- exact non-support list for integrality/PT/GW/convergence/CDGP/OSV/Stokes
  and CoHA leakage;
- local import obligations.

Added this report with attack-ledger entries and residual obligations.

## Verification Run

Commands run:

```bash
sed -n '1,220p' CLAUDE.md
sed -n '1,260p' AGENTS.md
sed -n '1,260p' references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md
sed -n '1,280p' references/primary-sources/compact-cy-source-fixture-control-surface-2026-04-30.md
nl -ba frontier_mnop_framing_volume.tex | sed -n '540,830p'
curl -L --fail --silent --show-error https://arxiv.org/e-print/hep-th/9809187 -o /tmp/gv113/gv1/eprint
gunzip -c /tmp/gv113/gv1/eprint | nl -ba
curl -L --fail --silent --show-error https://arxiv.org/e-print/hep-th/9812127 -o /tmp/gv113b/gv2/eprint
gunzip -c /tmp/gv113b/gv2/eprint | nl -ba
rg -n "sin|BPS|integer|integrality|Schwinger|M2|D2|wrapped|topological string|lambda|F_g|multi" /tmp/gv113/gv1/9809187.tex /tmp/gv113b/gv2/9812127.tex -S
find references/primary-sources -maxdepth 1 -type f \( -iname '*gopakumar*' -o -iname '*vafa*' -o -iname '*gv*' -o -iname '*9809187*' -o -iname '*9812127*' \) -print | sort
```

Result: source facts are remote-candidate only; local GV mirror absent.
The formula and BPS-index rows are anchored in the remote GV II TeX
stream. The non-support firewall is consistent with the existing quintic,
HKQ, MNOP/PT/DT, and compact-CY control fixtures.

No TeX build was run. The deliverable is a source fixture and report only.

## Residual Source Obligations

1. Import GV I/II PDF, TeX, extracted text, and checksums locally.
2. Re-anchor all GV rows to committed local file lines.
3. Decide the `2 pi` and Kähler-coordinate convention before importing the
   frontier formula into theorem-grade prose.
4. Decide the notation bridge from `alpha_r^(n_i)` to `n_beta^g`.
5. Keep mathematical integrality, PT/GW, KKV, convergence, CDGP, OSV, and
   conifold Stokes data outside the stable core until separately sourced.
6. Add the future source-provenance row in the main thread; this agent did
   not edit provenance by instruction.
