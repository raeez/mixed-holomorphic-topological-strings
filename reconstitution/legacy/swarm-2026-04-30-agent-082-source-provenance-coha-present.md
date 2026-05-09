# Swarm Report, 2026-04-30, Agent 082

Lane: source-provenance correction after Agent 078 CoHA quarantine audit.

Writable scope:

- `references/source-provenance.md`
- `reconstitution/swarm-2026-04-30-agent-082-source-provenance-coha-present.md`

No manuscript source file, fixture file, or unrelated report was edited.

## Inputs Loaded

- `CLAUDE.md`
- `~/ecosystem/INVARIANTS.md` Section IV
- `~/ecosystem/AGENTS-HARNESS.md` Section VIII
- `reconstitution/swarm-2026-04-30-agent-070-coha-fixture-reconciliation.md`
- `reconstitution/swarm-2026-04-30-agent-076-frontier-coha-followup.md`
- `reconstitution/swarm-2026-04-30-agent-078-coha-quarantine-audit.md`
- `references/primary-sources/coha-center-source-anchors-2026-04-30.md`
- `references/source-provenance.md`

## Stale Row Corrected

Corrected the CoHA/centre row in `references/source-provenance.md`.
The stale staged baseline recorded the Agent 057 lane as pending and said
the expected CoHA fixture was not present.  The current evidence is the
opposite: Agent 070 reconstructed
`references/primary-sources/coha-center-source-anchors-2026-04-30.md`,
and Agent 078 audited it as quarantined frontier/source-gap context.

MNOP/PT/DT and quintic BCOV/GV rows were preserved.

## Exact Wording

The corrected CoHA/centre row now reads:

```markdown
| 2026-04-30 | CoHA / centre source-gap fixture, Agent 070 reconstruction with Agent 078 quarantine audit | `references/primary-sources/coha-center-source-anchors-2026-04-30.md`; reports `reconstitution/swarm-2026-04-30-agent-070-coha-fixture-reconciliation.md` and `reconstitution/swarm-2026-04-30-agent-078-coha-quarantine-audit.md`; Agent 057 report remains absent | Current status: fixture present locally as Agent 070's reconstructed source-gap ledger, not theorem support. Agent 078 found no fatal CoHA/Hall leakage in the bound core theorem surface: CoHA, Joyce/KPS Hall vocabulary, and the `E_2`-centre compact target are quarantined to the standalone compact-CY frontier file plus source-gap/provenance layer. Core theorem evidence: none from CoHA. Frontier/source-gap context only: Lurie centre grammar, Joyce/Gross--Joyce--Tanaka Hall vocabulary, Joyce--Upmeier and Kinjo--Park--Safronov orientation/CoHA prerequisites, and named compact-CY comparison gaps. Non-CoHA compact-CY source-gap names currently carried by this row, including HKQ/CDGP/OSV/GV and chiral-volume normalization, may need a future split into a separate compact-CY fixture. Do not use this row to claim compact `F_X`, trace maps, `\sigma_Q`, `E_2` rigidity, `N_AJ`, GV/HKQ/CDGP/OSV line anchors, or an `Ob_UKD(C_tar)` null-homotopy. |
```

## Checks Run

- `rg -n -i "pending local provenance|neither is present|fixture.*absent|absent.*fixture|Agent 057.*live|found no CoHA|No CoHA/centre source fixture|That fixture is absent|pre-Agent-070|missing Agent 057|not present in the current working tree|no CoHA/centre fixture" references/source-provenance.md references/primary-sources/coha-center-source-anchors-2026-04-30.md reconstitution/swarm-2026-04-30-agent-070-coha-fixture-reconciliation.md reconstitution/swarm-2026-04-30-agent-076-frontier-coha-followup.md reconstitution/swarm-2026-04-30-agent-078-coha-quarantine-audit.md`
- `rg -n -i "pending local provenance|neither is present|Agent 057.*live|found no CoHA|not present in the current working tree|No CoHA/centre source fixture|That fixture is absent" references/source-provenance.md`
- `rg -n -i "CoHA|cohomological Hall|Hall|centre|center|source-gap|Agent 070|Agent 078|HKQ|CDGP|OSV|GV|N_AJ|Ob_UKD|sigma_Q|E_2" references/source-provenance.md`
- `git diff --check`
- `git diff --cached --check`

Result: the targeted stale-status grep on `references/source-provenance.md`
returned no hits.  Both diff whitespace checks passed.

## Files Changed

- `references/source-provenance.md`
- `reconstitution/swarm-2026-04-30-agent-082-source-provenance-coha-present.md`

Staging note: `references/source-provenance.md` already carried staged
provenance rows from earlier lanes.  Agent 082 edited only the CoHA row
and the report above.

## Remaining Provenance Obligations

1. Import local mirrors and line-level source anchors for Lurie, Joyce,
   Gross--Joyce--Tanaka, Joyce--Upmeier, Kinjo--Park--Safronov, HKQ,
   CDGP, OSV, and GV.
2. Split non-CoHA compact-CY source-gap rows, especially
   HKQ/CDGP/OSV/GV and chiral-volume normalization, into a separate
   compact-CY fixture if the provenance ledger is refined.
3. Keep CoHA/centre technology quarantined as frontier/source-gap
   context, not as a core theorem mechanism for `main.tex`.
4. Keep the Agent 057 report absence explicit unless that report is
   later materialized and audited.
5. Construct or reject compact `F_X`, trace maps, `\sigma_Q`,
   `E_2` rigidity, `N_AJ`, and `Ob_UKD(C_tar)` in their proper theorem
   lanes before any upgrade beyond source-gap status.
