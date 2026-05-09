# Chiral Interface Consistency Audit

Date: 2026-04-30.
Agent: 254.
Writable scope: this report and `reconstitution/swarm-2026-04-30-agent-254-chiral-interface-consistency-audit.md`.

## Scope

Audited files:

- `local-dictionary.tex`
- `claim-strength-ledger.tex`
- `open-obligations.tex`
- `theorem-lanes.tex`

No TeX file was edited.

## Stable Core

The integrated interface has a nonempty stable core.

1. The native object remains the two-complex-dimensional Hamiltonian holomorphic factorization algebra on `C^2`.
   Anchors: `local-dictionary.tex:189-215`, `theorem-lanes.tex:565-636`.
2. A curve chiral algebra enters only as `V_{\mathrm{red}}` in `\mathfrak I_{\mathrm{ch}}`, after controlled retained-mode reduction.
   Anchors: `local-dictionary.tex:375-413`, `open-obligations.tex:154-183`, `theorem-lanes.tex:1027-1079`.
3. The reduction must retain the `z_2` mode or full two-index principal-part coefficient system.
   Anchors: `local-dictionary.tex:390-397`, `open-obligations.tex:167-171`, `theorem-lanes.tex:1042-1048`.
4. No audited line asserts that the curve chiral algebra is native to `C^2`.
   Negative anchors: `claim-strength-ledger.tex:609-624`, `theorem-lanes.tex:1027-1079`, `local-dictionary.tex:410-413`.

The obstruction vector has the same displayed order in the four audited surfaces:
`\operatorname{Ob}_{\mathfrak I_{\mathrm{ch}}}=(\operatorname{Ob}_{\mathrm{red}},\operatorname{Ob}_{\mathrm{vert}},\operatorname{Ob}_{\mathrm{Zhu}},\operatorname{Ob}_{\mathrm{nat}})`.
Anchors: `local-dictionary.tex:401-408`, `claim-strength-ledger.tex:339-347`, `claim-strength-ledger.tex:614-621`, `open-obligations.tex:171-179`, `theorem-lanes.tex:1065-1073`.

## Valid Attacks

### A254-01: Controlled-reduction datum has split notation

Severity: 2.
Status: valid.

`claim-strength-ledger.tex` names the controlled reduction datum as
`\mathfrak R_{\C\times\R}` and gives the tuple
`(\pi,\mathcal B_{z_2},\pi_!,\mathcal K_{\mathrm{red}},L_{\mathrm{red}},\langle-,-\rangle_{\mathrm{red}},H_{\mathrm{anom}})`.
Anchors: `claim-strength-ledger.tex:572-581`.

The theorem lane and the newly integrated interface use
`\mathcal R_{\C\times\R}` with
`(\pi,\kappa_{\mathrm{top}},\kappa_{\mathrm{hol}},B_{z_2},\pi_!,L_{\mathrm{red}},\langle-,-\rangle_{\mathrm{red}},\{-,-\}_{\mathrm{red}},H_{\mathrm{anom}})`.
Anchors: `theorem-lanes.tex:715-723`, `theorem-lanes.tex:1033-1045`, `local-dictionary.tex:379-397`, `open-obligations.tex:158-169`.

Broken step: the same admission gate is named by two symbols and carries different entries. This is not a mathematical contradiction yet, because the ledger row is descriptive, but it is a real notation conflict.

Proposed repair: standardize the ledger row to `\mathcal R_{\C\times\R}` and use the theorem-lane tuple. If `\mathcal K_{\mathrm{red}}` is intended to package analytic kernels, define it inside `\operatorname{Ob}_{\mathrm{red}}` or as an auxiliary component of `\kappa_{\mathrm{top}},\kappa_{\mathrm{hol}}`, not as a second reduction datum.

### A254-02: `\mathcal F_{\mathrm{red}}` appears only as a tuple entry

Severity: 3.
Status: valid.

The symbol `\mathcal F_{\mathrm{red}}` appears in the interface tuple in all four audited surfaces, but no audited file defines it outside the tuple.
Anchors: `local-dictionary.tex:381-383`, `claim-strength-ledger.tex:329-333`, `open-obligations.tex:158-165`, `theorem-lanes.tex:1033-1041`.

Broken step: the tuple contains a factor whose construction target is not explicitly named. A reader can infer that it is the pushed-forward reduced factorization algebra, but the line-by-line interface should not rely on inference.

Proposed repair: add a defining sentence at `theorem-lanes.tex:1042` or `local-dictionary.tex:390`:
`\mathcal F_{\mathrm{red}}` is the factorization algebra on `Y=\R_t\times\C_{z_1}` obtained from `\mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}` by the retained-mode pushforward `\mathcal R_{\C\times\R}`, with coefficient system `\mathfrak g_{\mathrm{red}}=\mathfrak h_{\mathrm{red}}\ltimes\mathcal P_{\mathrm{red}}[1]`; before the reduction obstruction vanishes, it is a target symbol, not constructed native data.

### A254-03: Generic `V_L` boundary and retained-mode `V_{\mathrm{red}}` interface need an explicit subordination sentence

Severity: 3.
Status: valid as a clarity attack; no false theorem found.

The dictionary and theorem lanes retain an older generic vertex-boundary notation
`\mathfrak R_L`, `V_L`, and `\zeta_{L,\hbar}`.
Anchors: `local-dictionary.tex:290-318`, `local-dictionary.tex:320-373`, `theorem-lanes.tex:516-525`, `theorem-lanes.tex:638-695`, `claim-strength-ledger.tex:590-608`.

The new ingress theorem uses `V_{\mathrm{red}}` and `\zeta_\hbar` inside `\mathfrak I_{\mathrm{ch}}`.
Anchors: `local-dictionary.tex:375-413`, `theorem-lanes.tex:1027-1079`.

Broken step: the generic `V_L` boundary is gated, but if read in isolation it looks like a second route to a curve vertex algebra that does not explicitly pass through the retained `z_2` coefficient system. This risks weakening the intended rule: curve chiral algebra means `V_{\mathrm{red}}` after retained-mode reduction.

Proposed repair: after `theorem-lanes.tex:690-695` and in the dictionary row at `local-dictionary.tex:290-318`, add that `\mathfrak R_L` is only a generic vertex-boundary datum; in this manuscript's `C\times R` interface it is admissible only when it factors through `\mathcal R_{\C\times\R}` and is identified with `V_{\mathrm{red}}` in `\mathfrak I_{\mathrm{ch}}`.

### A254-04: `\operatorname{Ob}_{\mathrm{Zhu}}` gloss drops HKR outside theorem-lanes

Severity: 4.
Status: valid.

The theorem lane records the comparison chain through Hochschild/HKR and says the Zhu component includes Capelli/HKR comparison.
Anchors: `theorem-lanes.tex:998-1017`, `theorem-lanes.tex:1074-1078`.

The open-obligations row says the Zhu component measures zero-mode/Zhu multiplicativity and the Capelli shift, but omits HKR.
Anchor: `open-obligations.tex:180-183`.

The dictionary and ledger use shorter glosses.
Anchors: `local-dictionary.tex:398-400`, `claim-strength-ledger.tex:335-338`.

Broken step: the displayed vector order is consistent, but the component semantics are not fully synchronized. The theorem lane is stronger and should govern.

Proposed repair: normalize the gloss everywhere:
`\operatorname{Ob}_{\mathrm{Zhu}}` contains zero-mode definition, Zhu/Moyal multiplicativity, Capelli shift, and the completed stable Hochschild/HKR/CE-PV comparison required by the typed chain.

## Rejected Attacks

No line in the audited files makes the curve chiral algebra native. The potentially dangerous sentences are fenced:

- `local-dictionary.tex:410-413`: `V_{\mathrm{red}}` is a reduced shadow, not native `C^2` data.
- `claim-strength-ledger.tex:609-624`: external chiral algebra enters only as `V_{\mathrm{red}}` after retained-mode reduction.
- `open-obligations.tex:167-183`: the interface is not the native `C^2` holomorphic `E_2` object.
- `theorem-lanes.tex:1027-1079`: admission requires vanishing of `\operatorname{Ob}_{\mathfrak I_{\mathrm{ch}}}`.

## Verification

Commands run:

```bash
rg -n -F '\mathfrak I' local-dictionary.tex claim-strength-ledger.tex open-obligations.tex theorem-lanes.tex
rg -n -F '\mathfrak R' local-dictionary.tex claim-strength-ledger.tex open-obligations.tex theorem-lanes.tex
rg -n -F '\mathcal R' local-dictionary.tex claim-strength-ledger.tex open-obligations.tex theorem-lanes.tex
rg -n -F '\mathcal F_{\mathrm{red}}' local-dictionary.tex claim-strength-ledger.tex open-obligations.tex theorem-lanes.tex
rg -n -F 'HKR' local-dictionary.tex claim-strength-ledger.tex open-obligations.tex theorem-lanes.tex
git diff --check -- local-dictionary.tex claim-strength-ledger.tex open-obligations.tex theorem-lanes.tex
```

`git diff --check` reported no whitespace errors on the audited TeX files. No TeX build was run; this was a report-only consistency audit.
