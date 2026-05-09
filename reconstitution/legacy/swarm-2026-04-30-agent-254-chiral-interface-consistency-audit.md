# Swarm Report: Agent 254, Chiral Interface Consistency Audit

Date: 2026-04-30.

Owned writable files:

- `reconstitution/chiral-interface-consistency-audit-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-254-chiral-interface-consistency-audit.md`

TeX write policy: read-only. No TeX files edited.

## Claim Attacked

The newly integrated constructed chiral algebra interface
`\mathfrak I_{\mathrm{ch}}` must be consistent across `local-dictionary.tex`,
`claim-strength-ledger.tex`, `open-obligations.tex`, and `theorem-lanes.tex`.
The curve chiral algebra must appear only as `V_{\mathrm{red}}` after retained-mode `C\times R` reduction, never as the native `C^2` holomorphic factorization algebra.

## Stable Core

Stable. The audited files consistently keep the native object as
`\mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}` on `C^2` and fence the curve/VOA/Zhu package behind `\mathfrak I_{\mathrm{ch}}`.

Core anchors:

- `local-dictionary.tex:375-413`
- `open-obligations.tex:154-183`
- `claim-strength-ledger.tex:326-347`
- `claim-strength-ledger.tex:590-624`
- `theorem-lanes.tex:1027-1079`

## Valid Attacks Found

1. `claim-strength-ledger.tex:572-581` uses `\mathfrak R_{\C\times\R}`, `\mathcal B_{z_2}`, and `\mathcal K_{\mathrm{red}}`, while `theorem-lanes.tex:715-723` and the interface rows use `\mathcal R_{\C\times\R}` with `\kappa_{\mathrm{top}}`, `\kappa_{\mathrm{hol}}`, `B_{z_2}`, and `\{-,-\}_{\mathrm{red}}`. Repair: standardize to the theorem-lane tuple or explicitly define the ledger tuple as an abbreviation.
2. `\mathcal F_{\mathrm{red}}` is in every interface tuple but is not defined in the audited files. Anchors: `local-dictionary.tex:381-383`, `claim-strength-ledger.tex:329-333`, `open-obligations.tex:158-165`, `theorem-lanes.tex:1033-1041`. Repair: define it as the retained-mode pushed-forward factorization algebra on `Y=\R_t\times\C_{z_1}` with coefficient system `\mathfrak h_{\mathrm{red}}\ltimes\mathcal P_{\mathrm{red}}[1]`.
3. Generic `V_L` boundary notation remains beside the new `V_{\mathrm{red}}` interface. Anchors: `local-dictionary.tex:290-373`, `theorem-lanes.tex:516-525`, `theorem-lanes.tex:638-695`, `claim-strength-ledger.tex:590-608`. Repair: add that the generic vertex-boundary datum is admissible for this interface only when it factors through `\mathcal R_{\C\times\R}` and is identified with `V_{\mathrm{red}}` in `\mathfrak I_{\mathrm{ch}}`.
4. `\operatorname{Ob}_{\mathrm{Zhu}}` has synchronized order but slightly different glosses. `theorem-lanes.tex:998-1017` and `theorem-lanes.tex:1074-1078` include HKR; `open-obligations.tex:180-183` omits it. Repair: normalize `\operatorname{Ob}_{\mathrm{Zhu}}` as zero-mode, Zhu/Moyal multiplicativity, Capelli shift, and completed stable Hochschild/HKR/CE-PV comparison.

## No Fatal Native-Transfer Claim

No audited sentence says a curve chiral algebra is the native object. The strongest protection is at `theorem-lanes.tex:1027-1079`; the dictionary repeats it at `local-dictionary.tex:410-413`.

## Files Changed

Reports only:

- `reconstitution/chiral-interface-consistency-audit-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-254-chiral-interface-consistency-audit.md`

## Verification

Ran targeted `rg` scans for `\mathfrak I_{\mathrm{ch}}`, `V_{\mathrm{red}}`, `\mathfrak R`, `\mathcal R`, `\mathcal F_{\mathrm{red}}`, `V_L`, and `HKR`.
Ran `git diff --check -- local-dictionary.tex claim-strength-ledger.tex open-obligations.tex theorem-lanes.tex`; no whitespace errors reported.

No TeX build was run. The assignment was audit-only and report-only.
