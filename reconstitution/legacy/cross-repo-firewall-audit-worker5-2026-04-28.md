# Cross-Repo Firewall Audit - Worker 5

Date: 2026-04-28

Scope: local false-transfer audit for `topological-strings` against
`~/chiral-bar-cobar`, `~/chiral-bar-cobar-vol2`,
`~/calabi-yau-quantum-groups`, and `~/igusa-cusp-form`. Writable surface:
local firewall, ledger, and audit files only.

## Claim Attacked

Attack target: the local formal Hamiltonian BF/Moyal theorem on
`\R x \widehat{\C^2}_0` might be read as proving a compact CY3, global
BCOV, Vol III chiral-homology, Igusa/Borcherds/BKM, or `K3 x E`
consequence.

Status: false transfer blocked locally after patch. The local theorem is
only a `d=2` formal-disk theorem and a convention check for adjacent
programmes.

## Failure / Proof

Local proof of firewall: `main.tex:5895-5913` already states that the
theorem is local and not a compact Calabi-Yau, Borcherds/BKM, or global
twisted-M theorem; `tate-P5-cross-volume.tex:23-49` now explicitly adds
global BCOV amplitudes and compact-CY3 chiral homology to the
non-assertion list; `claim-strength-ledger.tex:112-116` and
`open-obligations.tex:84-88` now name the same excluded exports.

Failure mode found: not a local theorem overclaim, but sibling-side
overstrength. Vol III contains both a correct open comparison firewall
and stronger topological-string language elsewhere. Vol II has an active
proved Row 14 BKM identification. These claims may have independent
proof obligations, but they cannot be inherited from this local theorem.

## Local Anchors

- `claim-strength-ledger.tex:112-116`: cross-volume consequences are
  not asserted; now names global BCOV, Vol III chiral homology,
  Borcherds/BKM, Igusa, and `K3 x E`.
- `open-obligations.tex:84-89`: any compact CY, global BCOV, Vol III
  chiral-homology, `\Phi_d`, Igusa/BKM/Borcherds, `K3 x E`, or
  higher-dimensional derived-centre consequence requires a separate
  matched-conventions theorem.
- `tate-P3-universality.tex:168-176`: protected twisted-M reduction
  remains local and supplies no compact-CY3 chiral homology, global
  BCOV amplitude, or BKM denominator identity.
- `tate-P5-cross-volume.tex:23-50`: appendix is a non-transfer
  boundary; no sibling theorem may use this local result as a substitute
  for dimension, curve, trace, framing, topology, anomaly, deformation,
  or QME data.
- `reconstitution/source-convention-ledger-2026-04-28.md`: no-transfer
  firewall and sibling-side risk notes updated.

## Cross-Repo Anchors

- Vol III:
  `/Users/raeez/calabi-yau-quantum-groups/main.tex:1824-1826` actively
  includes `modular_trace`, `modular_koszul_bridge`, and
  `bar_cobar_bridge`.
- Vol III correct firewall:
  `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/modular_trace.tex:223`
  says the shadow-tower/topological-string genus comparison is separate
  and open for `g >= 2`.
- Vol III stronger language:
  `/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:1290`
  says the topological string partition function admits a genus-by-genus
  derivation from the shadow obstruction tower.
- Vol III stronger language:
  `/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:1727`
  says the instanton gap determines the exact topological string free
  energy through the Borel-KS pipeline.
- Vol II:
  `/Users/raeez/chiral-bar-cobar-vol2/main.tex:2244` includes
  `appendices/cfg_side_by_side`; `cfg_side_by_side.tex:659-697` states
  a proved Row 14 BKM identification.
- Vol II scope discipline:
  `/Users/raeez/chiral-bar-cobar-vol2/FRONTIER.md:60-66` retracts plain
  BKM-side shortcuts and puts BKM non-abelianity under vertex-operator
  closure.
- Igusa:
  `/Users/raeez/igusa-cusp-form/CLAUDE.md:9-19` treats
  `topological-strings` as structural/physics-dual context.
  `agent_material/15_compact_finite_first_E3_source_attack_heal.tex:478-489`
  reads the local topological-string comparison as heuristic and
  convention-checking, not a compact source theorem.
- Vol I:
  `/Users/raeez/chiral-bar-cobar/AGENTS.md:364-372` names
  `topological-strings` as adjacent physics context; no active import of
  this local theorem into the bound root manuscript was found in the
  checked anchors.

## Exact Firewall Language

Patched local firewall:

`No compact Calabi--Yau, global BCOV, Vol III, chiral-homology,
Borcherds, BKM, Igusa, \(K3\times E\), or sister-volume theorem
follows from this local Hamiltonian BF/Moyal calculation without a
separate matched-conventions proof.`

Operational rule:

Sibling volumes may cite the local theorem only as a `d=2` formal-disk
normalization and convention check unless they supply their own matched
proof.

## Claim-Status Recommendation

- Local theorem: proved only in the local scopes named by the
  claim-strength ledger.
- Cross-volume consequences: not asserted.
- Vol III global BCOV/topological-string claims: sibling-side audit
  target; read under `modular_trace.tex:223` until an internal Vol III
  matched theorem is supplied.
- Vol II Row 14 BKM identification: sibling-side audit target; cannot
  inherit the local Costello graph-normalization computation as an
  all-order BKM or compact `K3 x E` source theorem.
- Igusa compact realization: no local action; current checked material
  is conditional enough relative to this theorem.

## Files Changed

- `claim-strength-ledger.tex`
- `open-obligations.tex`
- `tate-P3-universality.tex`
- `tate-P5-cross-volume.tex`
- `reconstitution/source-convention-ledger-2026-04-28.md`
- `reconstitution/cross-repo-firewall-audit-worker5-2026-04-28.md`

## Commands Run

- `git status --short`
- `sed -n '1,260p' CLAUDE.md`
- `sed -n '1,220p' /Users/raeez/ecosystem/INVARIANTS.md`
- `sed -n '1,260p' /Users/raeez/ecosystem/AGENTS-HARNESS.md`
- `rg -n -i "Vol III|Igusa|BKM|Borcherds|K3|compact CY|CY_3|global BCOV|chiral homology|CY-to-chiral|Delta_5|sister-volume|cross-volume|firewall|consequence|outlook|transfer|follows|implies" main.tex tate-P5-cross-volume.tex tate-P3-universality.tex open-obligations.tex claim-strength-ledger.tex reconstitution/source-convention-ledger-2026-04-28.md`
- Targeted `nl -ba ... | sed -n ...` reads for all local and cross-repo
  anchors named above.
- Targeted `rg -n` scans in the four sibling repositories for
  `topological-strings`, `BCOV`, `BKM`, `Borcherds`, `Igusa`,
  `compact CY`, `K3`, `Phi_d`, and global topological-string language.
- `pdflatex -interaction=nonstopmode -halt-on-error -draftmode
  -output-directory=/tmp/topological-strings-worker5-tex main.tex`
  exited 0; it reported one-pass undefined-reference warnings and
  pre-existing font/box warnings.

## Remaining Open Questions

- Vol III must decide whether `bar_cobar_bridge.tex:1290` and
  `modular_koszul_bridge.tex:1727` are theorem-grade or must be demoted
  under `modular_trace.tex:223`.
- Vol II must decide whether Row 14 has an independent CFG/Vol II proof
  or should be downgraded to conditional/open.
- No sibling repository was edited in this pass.
