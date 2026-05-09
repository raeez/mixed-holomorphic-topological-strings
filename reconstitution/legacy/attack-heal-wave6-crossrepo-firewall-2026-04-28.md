# Worker 6 wave 6 cross-repo firewall re-attack

Date: 2026-04-28.

Worktree:
`/private/tmp/topological-strings-remainder-wave6-20260428-073738/crossrepo-firewall`.

## Claim Attacked

The attacked false-transfer shape was:

> The local Hamiltonian BF/Moyal theorem, the admissible protected-sector
> reduction, or the Costello graph normalization implies a compact
> Calabi--Yau threefold theorem, a global BCOV theorem, a Vol III
> CY-to-chiral/chiral-homology theorem, an Igusa/Borcherds/BKM theorem,
> a \(K3\times E\) theorem, or a sister-volume theorem.

Status: cleared locally after re-attack. The manuscript denies this
transfer in the abstract, the local theorem discussion, the Costello
specialization problem, the weighted Tate firewall, the protected-sector
appendix, the claim-strength ledger, the open-obligations list, and the
cross-volume convention appendix.

## False-Transfer Modes Checked

1. Twisted-M protected-sector language read as a globalization theorem.
   Cleared: `tate-P3-universality.tex` now states that admissibility is
   neither a globalization functor nor a comparison map.
2. BCOV/Costello--Li source theorems read as compact CY3 or global BCOV
   output. Cleared: `main.tex:5090-5174`, `main.tex:5278-5394`, and
   `tate-T4-bv-vanishing.tex:17-198` keep them as source packages with
   missing specialization, QME, propagator, and anomaly data.
3. Vol III notation `\Phi_d`, `\kappa_{\mathrm{ch}}`,
   `\kappa_{\mathrm{BKM}}`, Stage-1/Stage-2 read as a theorem exported
   from the formal disk. Cleared: `tate-P5-cross-volume.tex` now requires
   an exact comparison morphism, claim status, and the precise role of
   the local theorem.
4. Igusa/Borcherds/BKM consequences inferred from the scalar anomaly or
   Moyal coefficient. Cleared: `claim-strength-ledger.tex` and
   `open-obligations.tex` now state that the local result may be cited
   only as a \(d=2\) normalization after the target volume supplies its
   own proof.
5. Templates read as theorems. Healed: the matched-conventions templates
   are now explicitly failure tests and open obligations.
6. Standalone compact-CY frontier notes read as active manuscript export.
   Cleared for this worktree: `frontier_mnop_framing_volume.tex` is not
   input by `main.tex`, and `make pdf` does not load it. It contains
   compact-CY frontier claims as a separate standalone note, not as a
   consequence of the local Hamiltonian BF/Moyal theorem. It was left
   unchanged because it is outside the specified wave6 heal list.

## Local Anchors

- `abstract.tex:33-41`: compact Calabi--Yau, BKM/Igusa, and
  sister-volume transfers are not asserted.
- `main.tex:170-178`, `main.tex:689-696`: BCOV is a source-convention
  template, not an imported theorem.
- `main.tex:619-629`: local string-field-theoretic language is not a
  global worldsheet or anomaly theory.
- `main.tex:830-907`: the maximal global statement is local Hamiltonian
  restriction and period obstruction, not global factorization-center
  descent.
- `main.tex:5090-5174`: Costello and Costello--Li inputs do not identify
  the mixed Hamiltonian BF defect.
- `main.tex:5278-5394`: analytic graph realization remains conditional;
  the convention firewall blocks `\Phi_d`, `\kappa`, Igusa, Borcherds,
  BKM, compact CY3, and Stage-1/Stage-2 exports.
- `tate-T1-weighted-completion.tex`, `tate-T4-bv-vanishing.tex`: regulator
  and BV routes are local or conditional, not compact-CY transfer
  theorems.
- `tate-P3-universality.tex`: protected-sector admissibility is local
  formal-disk restriction only.
- `tate-P5-cross-volume.tex`: convention firewall and matched-conventions
  theorem templates.
- `claim-strength-ledger.tex` and `open-obligations.tex`: cross-volume
  consequences are not asserted.
- `frontier_mnop_framing_volume.tex:1-10`: standalone frontier note, not
  bound into `main.tex`; scanned as a possible local out-of-scope audit
  target and left unchanged.

## Sibling Anchors Read

- `/Users/raeez/calabi-yau-quantum-groups/FRONTIER.md:27-92`: two-stage
  `\Phi_d`, distinct `\kappa` invariants, BKM open questions, and
  cross-volume discipline.
- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/modular_trace.tex:220-223`:
  genus-expansion comparison is open for \(g\ge2\).
- `/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:1287-1290`
  and `modular_koszul_bridge.tex:1725-1727`: sibling-side stronger
  topological-string language remains a sibling audit target and cannot
  be sourced from this local theorem.
- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex`:
  object-level versus functorial `\Phi_d`, witnessed \(K3\)-fibre data,
  and non-automatic Borcherds lift discipline.
- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/cy_d_kappa_stratification.tex`:
  separation of `\kappa_{\mathrm{ch}}`, `\kappa_{\mathrm{cat}}`,
  `\kappa_{\mathrm{BKM}}`, and BCOV curving.
- `/Users/raeez/chiral-bar-cobar/AGENTS.md:364-372`: Vol I treats
  `topological-strings` as a physics-dual cross-volume anchor, not a
  theorem import.
- `/Users/raeez/chiral-bar-cobar-vol2/FRONTIER.md:58-68`,
  `/Users/raeez/chiral-bar-cobar-vol2/main.tex:1512-1571`, and
  `/Users/raeez/chiral-bar-cobar-vol2/appendices/cfg_side_by_side.tex:659-697`:
  Vol II BKM/Hall assertions are sibling-internal obligations.
- `/Users/raeez/igusa-cusp-form/CLAUDE.md:9-19`,
  `/Users/raeez/igusa-cusp-form/AGENTS.md:203-224`, and
  `/Users/raeez/igusa-cusp-form/agent_material/15_protected_integration_orientation_character_attack_heal.tex:383-544`:
  Igusa compact realization requires finite-first Hall, orientation,
  primitive recognition, and Hopf-pairing data.

## Files Changed

- `tate-P3-universality.tex`
- `tate-P5-cross-volume.tex`
- `claim-strength-ledger.tex`
- `open-obligations.tex`
- `references/source-provenance.md`
- `reconstitution/attack-heal-wave6-crossrepo-firewall-2026-04-28.md`

No sibling repository was edited.

## Commands Run

- `sed -n` and `nl -ba ... | sed -n ...` to read `CLAUDE.md`,
  `AGENTS.md`, ecosystem invariants/harness text, local TeX fragments,
  and sibling anchors.
- `rg -n` and `rg -n -i -C 2` to scan for compact CY, global BCOV,
  Vol III, CY-to-chiral, chiral homology, `\Phi_d`, `\kappa`, Igusa,
  Borcherds, BKM, `K3`, consequence, transfer, export, and implication
  language. Two overescaped regex scans failed and were rerun with
  fixed-string or safe regex patterns.
- `apply_patch` to update the owned local files and create this report.
- `git status --short -- ...` to verify the changed-file set without
  staging or committing.
- `git diff --check -- ...` for tracked diffs and
  `rg -n "[ \t]$" ...` across all edited files to check for whitespace
  damage.
- `make pdf`, which completed and wrote `out/main.pdf`; a final
  `rg -n "Fatal error|Emergency stop|Undefined control sequence|There were undefined references|Label\(s\) may have changed|Rerun to get cross-references right" out/main.log`
  scan found no fatal, unresolved-reference, or rerun marker.
- `rg -n "frontier_mnop|mnop|framing_volume" main.tex *.tex` to check
  that `frontier_mnop_framing_volume.tex` is not bound into the active
  manuscript.

## Remaining Sibling Follow-Ups

1. Vol III: `bar_cobar_bridge.tex:1287-1290` and
   `modular_koszul_bridge.tex:1725-1727` remain sibling-side audit
   targets unless Vol III supplies its own matched compact BCOV /
   topological-string theorem.
2. Vol II: Row 14 BKM identification in
   `appendices/cfg_side_by_side.tex:659-697` cannot cite the local
   Hamiltonian BF/Moyal theorem as evidence for full BKM realization.
3. Igusa: compact \(K3\times E\) realization remains gated by the
   finite-first Hall source, orientation character, primitive recognition,
   and Hopf-pairing data.
