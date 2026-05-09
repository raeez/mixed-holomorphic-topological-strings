# Agent 078 CoHA Quarantine Audit

Lane: CoHA quarantine / core-theorem leakage audit.

Verdict: no fatal CoHA/Hall leakage was found in the bound core theorem surface.  CoHA, Joyce/KPS Hall vocabulary, and the `E_2`-centre compact target appear only in the standalone compact-CY frontier file and the source-gap fixture/provenance layer.  The core files use "center/centre" for intrinsic reduced CE/PV central operations, the U(1) centre anomaly, or explicit unreduced factorization-centre open problems; these are not CoHA mechanisms.

## Commands Run

- `sed -n '1,240p' CLAUDE.md`
- `git status --short`
- `sed -n '1,220p' ~/ecosystem/INVARIANTS.md`
- `sed -n '1,260p' ~/ecosystem/AGENTS-HARNESS.md`
- `rg -n -i '\b(CoHA|cohomological Hall|Hall algebra|Hall|center|centre|central|source-gap|DT|PT|MNOP|Ob_UKD|CE/PV|Matlis|BV|QME|Moyal|radial|factorization|large-N|large N)\b' main.tex theorem-lanes.tex claim-strength-ledger.tex open-obligations.tex references/source-provenance.md references/primary-sources/coha-center-source-anchors-2026-04-30.md frontier_mnop_framing_volume.tex`
- `rg -n -i '(CoHA|cohomological Hall|Hall--|Hall algebra|Hall structures|Joyce|Gross--Joyce|Kinjo|Safronov|Lurie|E_2.?centre|E2.?centre|centre package|center package|Ob_UKD|C_\{?tar|PhiFA|sigma_[QX]|source-gap|source gap)' ...`
- `rg -n -i '\b(CoHA|cohomological Hall|Hall--|Hall algebra|Hall structures|Joyce|Kinjo|Safronov|Lurie)\b' main.tex theorem-lanes.tex claim-strength-ledger.tex open-obligations.tex`
- `rg -n -i '\b(CoHA|cohomological Hall|Hall--|Hall algebra|Hall structures|Joyce|Kinjo|Safronov|Lurie)\b' references/source-provenance.md references/primary-sources/coha-center-source-anchors-2026-04-30.md frontier_mnop_framing_volume.tex`
- `rg -n -i '(Ob_UKD|C_tar|C_\{\\mathrm\{tar\}\}|sigma_Q|sigma_X|PhiFA_3|F_X|Aut_\{E_2\}|Z_\{E_2\}|E_2)' ...`
- `nl -ba frontier_mnop_framing_volume.tex | sed -n '1,190p'`
- `nl -ba frontier_mnop_framing_volume.tex | sed -n '228,246p'`
- `nl -ba frontier_mnop_framing_volume.tex | sed -n '345,356p'`
- `nl -ba frontier_mnop_framing_volume.tex | sed -n '754,824p'`
- `nl -ba references/source-provenance.md | sed -n '1,12p'`
- `nl -ba references/primary-sources/coha-center-source-anchors-2026-04-30.md | sed -n '1,112p'`
- `nl -ba main.tex | sed -n '2760,2990p'`
- `nl -ba main.tex | sed -n '2987,3025p'`
- `nl -ba claim-strength-ledger.tex | sed -n '410,438p'`
- `nl -ba open-obligations.tex | sed -n '420,462p'`
- `nl -ba theorem-lanes.tex | sed -n '1276,1300p'`, `1348,1358p`, `1564,1584p`
- `rg -n -i '\bcenter\b|\bcentre\b|centrality|central-operation|factorization-centre|factorization-center|U\(1\) center|centre-of-mass' main.tex theorem-lanes.tex claim-strength-ledger.tex open-obligations.tex | head -n 220`

## Accepted Frontier Mentions

- `frontier_mnop_framing_volume.tex:46-51` states that the compact CY3 note is target data and not a consequence of the formal-local Hamiltonian BF/Moyal theorem.  This is the correct quarantine frame.
- `frontier_mnop_framing_volume.tex:54-68` names the CoHA/centre source-gap row but immediately says it is vocabulary and stable identifiers only, not a construction, and does not import `F_X`, trace maps, `sigma_Q`, `E_2` rigidity, `N_AJ`, or `Ob_UKD(C_tar)` null-homotopies.
- `frontier_mnop_framing_volume.tex:71-94` separates scalar DT/PT/GW source facts from the compact target datum `C_tar(X)` and states that the CoHA/centre fixture is only grammar and prerequisites for a possible construction.
- `frontier_mnop_framing_volume.tex:108-120` proves only the scalar DT/PT quintic factorisation and marks the PT/GW and HKQ material as conditional source obligation.
- `frontier_mnop_framing_volume.tex:130-136` cites Bridgeland's Hall-algebra theorem as an external DT/PT source theorem for a scalar identity and says the reconstructed CoHA fixture does not lift the identity to `F_Q`, trace maps, or a motivic/factorization-algebra identity.  Acceptable because this is frontier DT/PT source provenance, not a local CE/PV proof mechanism.
- `frontier_mnop_framing_volume.tex:146-158` states the `E2-centre MNOP package` as conjectural target data and explicitly denies construction of `sigma_Q` or `Aut_{E_2}` rigidity.
- `frontier_mnop_framing_volume.tex:161-172` records the Joyce--KPS line as source vocabulary and conditional target schema, not a theorem and not a Vol III transfer.
- `frontier_mnop_framing_volume.tex:237-242` uses the CoHA/centre fixture to record `N_AJ` and `Ob_UKD(C_tar)` firewalls.  Acceptable source-gap language.
- `frontier_mnop_framing_volume.tex:345-355` says no fixture supplies `N_AJ`; the CoHA/centre fixture records non-support.  Acceptable.
- `frontier_mnop_framing_volume.tex:761-769` and `820-823` keep the CoHA/`E_2`-centre package as source-gap-ledgered target data, with no `F_X`, trace maps, `sigma_Q`, rigidity theorem, or `Ob_UKD` null-homotopy.
- `references/primary-sources/coha-center-source-anchors-2026-04-30.md:3-16` is explicitly a source/gap ledger and denies construction of `C_tar` or vanishing of `Ob_UKD(C_tar)`.
- `references/primary-sources/coha-center-source-anchors-2026-04-30.md:25-27` classifies CoHA/centre as an obstruction/source component of the compact target datum, not a vanishing obstruction.
- `references/primary-sources/coha-center-source-anchors-2026-04-30.md:50-53` permits Lurie/Joyce/KPS only as grammar/source vocabulary and denies compact factorization algebra, trace maps, `sigma_Q`, `E_2`-centre identification, MNOP automorphism, and `Ob_UKD` null-homotopies.
- `references/primary-sources/coha-center-source-anchors-2026-04-30.md:72-106` lists explicit gaps and ends with the firewall: CoHA/centre and chiral-volume package is target data, not proof input for `main.tex`.

## Core Mentions Checked

- `main.tex:2769-2775`, `2960-2985`, and `2987-2995` use Lurie only for one-dimensional locally constant factorization-algebra grammar and explicitly state that no unrestricted Costello--Gwilliam central-operations theorem is used in the reduced Hamiltonian proof.
- `main.tex:3000-3018` is the Hamiltonian-current central operation theorem.  Its proof mechanism is reduced CE/PV/P0 algebra, not CoHA.
- `theorem-lanes.tex:1276-1290`, `1293-1298`, and `1350-1352` isolate reduced current statements and exclude unreduced BV/factorization-centre morphisms and centrality homotopies.  No CoHA/Hall vocabulary occurs.
- `theorem-lanes.tex:1564-1584` treats the U(1) centre-of-mass anomaly and Capelli contact term.  This is local scalar anomaly bookkeeping, not compact CY CoHA.
- `claim-strength-ledger.tex:423-438` and `open-obligations.tex:424-460` introduce a generic matched-conventions target datum `mathfrak C_tar` and obstruction vector for any cross-volume transfer.  No CoHA/Hall vocabulary occurs; the vector is a firewall, not a proof input.

## Suspect Or Brittle Mentions

- `references/source-provenance.md:8` is stale relative to the current working tree: it says the CoHA fixture is absent from the checkout and index, while `references/primary-sources/coha-center-source-anchors-2026-04-30.md` now exists and is staged as an added file.  This is not core-theorem leakage, but it is provenance drift and should be reconciled.
- `frontier_mnop_framing_volume.tex:118-119`, `237-242`, and `761-769` let the CoHA fixture also carry HKQ/CDGP/OSV/GV/chiral-volume source-gap rows.  This remains quarantined in the frontier file, but it broadens "CoHA" into a general compact-CY source-gap bucket.  Prefer a separate compact-CY source-gap fixture for HKQ/CDGP/OSV/GV and reserve the CoHA fixture for Lurie/Joyce/GJT/Joyce--Upmeier/KPS centre/Hall vocabulary.
- `frontier_mnop_framing_volume.tex:146-158` is a conjecture environment named `E2-centre MNOP package`.  The body is correctly quarantined as target data.  If this file is ever bound into `main.tex`, rename or preface it so no reader treats it as a theorem lane for CE/PV, Matlis, BV/QME, Moyal/radial-parts, factorization currents, large-N, or `Ob_UKD(C_tar)`.
- `references/primary-sources/coha-center-source-anchors-2026-04-30.md:25-27` says the CoHA/centre package is an `ob_Src,CoHA` and `ob_UKD` component.  The intended meaning is non-vanishing obstruction bookkeeping.  Tighten the sentence to say explicitly that it neither defines nor kills `Ob_UKD(C_tar)` and is not an input to the local theorem.

## Recommended Quarantine Edits

- Update `references/source-provenance.md:8` to reflect the present state: fixture file present; Agent 057 report still absent unless later created; local mirrors still absent; status remains source-gap only.
- Split non-CoHA compact-CY gaps out of the CoHA fixture.  Move HKQ/CDGP/OSV/GV/chiral-volume source identifiers to the quintic/frontier fixture, leaving CoHA/centre as Lurie/Joyce/GJT/Joyce--Upmeier/KPS only.
- Add a one-line firewall near `frontier_mnop_framing_volume.tex:146`: "This conjecture is not bound into `main.tex` and is not a mechanism for the formal-local theorem."  This is redundant with lines 46-51 but protects against later extraction.
- Keep all CoHA/Hall terms out of `main.tex`, `theorem-lanes.tex`, `claim-strength-ledger.tex`, and `open-obligations.tex` except as explicitly marked external frontier/source-gap language.  Current audit found no violation.

## Residual Risk

- The checkout is actively dirty from other agents.  Line anchors are exact for the working tree observed during this audit, but may shift before integration.
- The provenance row and fixture disagree about existence state.  Until reconciled, future agents may either ignore the fixture or over-trust it.
- "Centre" remains a legitimate word in the core manuscript for reduced CE/PV central operations and the U(1) centre anomaly.  Future grep-only audits must distinguish this intrinsic local terminology from external CoHA/`E_2`-centre compact-CY technology.
- No source files were edited.  This report is the only owned write for Agent 078.
