# Swarm Report: Agent 256, Chiral Interface Insertion Coverage Audit

Date: 2026-04-30.

Owned writable files:

- `reconstitution/chiral-interface-insertion-coverage-audit-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-256-chiral-interface-insertion-coverage-audit.md`

No TeX, script, source, figure, or bibliography file was edited.

## Claim Attacked

Whether Agent 249's insertion spec should still be inserted into the live
TeX after Agent 250's ledger/dictionary integration and the main-thread
theorem/open-obligation additions.

## Evidence Read

- Repo instructions: `CLAUDE.md`, `AGENTS.md`.
- Ecosystem discipline: `~/ecosystem/INVARIANTS.md` section IV,
  `~/ecosystem/AGENTS-HARNESS.md` section VIII.
- Attack-heal protocol:
  `~/ecosystem/skills/claude-code/attack-heal-swarm-plugin/skills/attack-heal-swarm/SKILL.md`
  and shared protocol.
- Vol II rectification discipline:
  `~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`.
- Agent 249 files:
  `reconstitution/chiral-interface-manuscript-insertion-spec-2026-04-30.md`,
  `reconstitution/swarm-2026-04-30-agent-249-chiral-interface-manuscript-insertion-spec.md`.
- Agent 250 report:
  `reconstitution/swarm-2026-04-30-agent-250-chiral-interface-ledger-dictionary-integration.md`.
- Live TeX anchors:
  `theorem-lanes.tex:227-415`, `theorem-lanes.tex:698-1080`,
  `local-dictionary.tex:346-413`,
  `claim-strength-ledger.tex:326-347`,
  `claim-strength-ledger.tex:572-624`,
  `open-obligations.tex:154-183`,
  `open-obligations.tex:263-279`,
  `main.tex:1454-1531`,
  `abstract.tex:52-73`, `abstract.tex:207-212`,
  `principles.tex:272-276`.

## Stable Core

The live TeX already admits a constructed one-dimensional chiral algebra
only as reduced interface data:

```tex
\mathfrak I_{\mathrm{ch}}
=
(\mathcal R_{\C\times\R},
 \mathcal F_{\mathrm{red}},
 V_{\mathrm{red}},
 Q_{\mathrm{BRST}},
 \mathbf 1,T,Y,\operatorname{wt},
 \zeta_\hbar,H_{\mathrm{anom}}).
```

The stable firewall is also present: before the controlled
`C x R` reduction, a curve chiral algebra or Zhu bridge is false transfer;
after reduction it remains a theorem surface with missing construction,
not the native `C^2` holomorphic `E_2`/factorization object.

## Valid Attacks

```yaml
- id: A256-01
  severity: 1
  status: valid
  lens: duplicate theorem surface
  claim: Agent 249's theorem-lane block is still missing and should be inserted verbatim.
  broken_step: The live TeX already contains label thm:lane-constructed-chiral-interface at theorem-lanes.tex:1027-1080.
  evidence_type: line_reference
  evidence_ref: theorem-lanes.tex:1027-1080
  files_read: [theorem-lanes.tex, reconstitution/chiral-interface-manuscript-insertion-spec-2026-04-30.md]
  tools_used: [rg, sed, nl]
  confidence: high
  blast_radius: Duplicate theorem label, repeated tuple, and repeated reduction/BRST/Zhu formulas.
  minimal_heal: Do not duplicate. If needed, patch the existing statement with missing subcomponent names.
  residual: Full Agent 249 obstruction subcomponent vectors are not displayed in the live constructed-interface statement.
  deciding_evidence: A later TeX diff adding only subcomponent names to the existing statement or obligation row.

- id: A256-02
  severity: 2
  status: valid
  lens: dictionary and ledger duplication
  claim: The dictionary row and failed-surface ledger row remain absent.
  broken_step: Agent 250 already integrated them in substance.
  evidence_type: line_reference
  evidence_ref: local-dictionary.tex:375-413; claim-strength-ledger.tex:326-347
  files_read: [local-dictionary.tex, claim-strength-ledger.tex, reconstitution/swarm-2026-04-30-agent-250-chiral-interface-ledger-dictionary-integration.md]
  tools_used: [rg, nl]
  confidence: high
  blast_radius: Duplicate longtable row and duplicate failed-surface item.
  minimal_heal: Leave as covered; if desired later, rename the broad ledger heading rather than adding a new item.
  residual: Ledger heading is broader than Agent 249's proposed heading.
  deciding_evidence: Editorial decision on whether the heading itself matters.

- id: A256-03
  severity: 2
  status: valid
  lens: supremum-controller merge
  claim: The supremum-controller constructed-interface row must be added as a new item.
  broken_step: Its content is already merged into the reduced Dirac BRST/Zhu controller row.
  evidence_type: line_reference
  evidence_ref: claim-strength-ledger.tex:590-624
  files_read: [claim-strength-ledger.tex]
  tools_used: [nl, rg]
  confidence: high
  blast_radius: Ledger inflation and repeated false-transfer classification.
  minimal_heal: Do not add a duplicate. Split the existing item only if a future layout pass demands a separate heading.
  residual: No separate heading "Constructed chiral algebra interface tuple."
  deciding_evidence: Future ledger-layout instruction.

- id: A256-04
  severity: 2
  status: valid
  lens: open-obligation placement
  claim: The constructed-interface open obligation is absent because it is not after the one-antifield Moyal target.
  broken_step: The row exists, but it was inserted earlier in the obligation list.
  evidence_type: line_reference
  evidence_ref: open-obligations.tex:154-183; open-obligations.tex:263-279
  files_read: [open-obligations.tex]
  tools_used: [nl, rg]
  confidence: high
  blast_radius: Adding the same obligation after the one-antifield target would produce two copies.
  minimal_heal: If ordering matters, move the existing row; do not duplicate it.
  residual: Placement differs from Agent 249's spec.
  deciding_evidence: Future TeX-layout instruction.

- id: A256-05
  severity: 3
  status: valid
  lens: main-body anchor
  claim: Agent 249's main-text remark is already present.
  broken_step: No label rmk:constructed-chiral-interface-target exists, and main.tex passes directly from the Darboux package proof to the external firewall remark.
  evidence_type: line_reference
  evidence_ref: main.tex:1529-1531
  files_read: [main.tex]
  tools_used: [rg, nl]
  confidence: high
  blast_radius: Low mathematical blast radius; the content is covered elsewhere, but the requested body pointer is absent.
  minimal_heal: If TeX editing is reopened, add only a short cross-reference sentence or compact remark.
  residual: Missing as a distinct insertion block.
  deciding_evidence: Future TeX patch adding a concise pointer after prop:native-darboux-theorem-package.
```

## Coverage Result

Covered:

- The theorem-lane constructed-interface statement exists.
- The dictionary row exists.
- The failed-surface ledger row is covered in substance.
- The supremum-controller classification is covered by merge.
- The open-obligation row exists, with different placement.

Missing:

- The compact main-text remark after
  `prop:native-darboux-theorem-package`.
- Exact Agent 249 subcomponent vectors for `Ob_red`, `Ob_vert`,
  `Ob_Zhu`, and `Ob_nat`.
- The displayed `zeta_hbar(f*g)=zeta_hbar(f)zeta_hbar(g)` equation and
  Hochschild cocycle `ob_Zhu(f,g)`.
- The explicit "Vol II control" paragraph.  This should remain report
  context unless a manuscript cross-volume comparison is assigned.

## Repairs Made

Only the two requested Markdown reports were written.

## Verification

Read-only verification commands used:

```bash
git status --short
sed -n '1,320p' reconstitution/chiral-interface-manuscript-insertion-spec-2026-04-30.md
sed -n '1,280p' reconstitution/swarm-2026-04-30-agent-249-chiral-interface-manuscript-insertion-spec.md
sed -n '1,280p' reconstitution/swarm-2026-04-30-agent-250-chiral-interface-ledger-dictionary-integration.md
rg -n -F -e 'mathfrak I_{\mathrm{ch}}' -e 'Ob}_{\mathfrak I_{\mathrm{ch}}}' -e 'V_{\mathrm{red}}' -e 'Q_{\mathrm{BRST}}' --glob '*.tex'
nl -ba theorem-lanes.tex | sed -n '620,1080p'
nl -ba local-dictionary.tex | sed -n '300,430p'
nl -ba claim-strength-ledger.tex | sed -n '318,350p'
nl -ba claim-strength-ledger.tex | sed -n '570,630p'
nl -ba open-obligations.tex | sed -n '140,285p'
nl -ba main.tex | sed -n '1360,1545p'
```

No TeX build was run because this pass is report-only and did not alter
TeX sources.
