# Swarm Report, 2026-04-30, Agent 089

Lane: narrow CoHA fixture to the Hall/centre domain after Agent 084.

Writable scope:

- `references/primary-sources/coha-center-source-anchors-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-089-coha-fixture-narrowing.md`

No manuscript source, provenance ledger, or split compact-CY fixture was
edited.

## Inputs Loaded

- `CLAUDE.md`
- `~/ecosystem/INVARIANTS.md`, especially Section IV and git discipline.
- `~/ecosystem/AGENTS-HARNESS.md`, especially Section VIII.
- `reconstitution/swarm-2026-04-30-agent-084-noncoha-compact-cy-fixture-split-plan.md`
- `reconstitution/swarm-2026-04-30-agent-078-coha-quarantine-audit.md`
- `references/primary-sources/coha-center-source-anchors-2026-04-30.md`
- `frontier_mnop_framing_volume.tex`, read-only, for the CoHA source-status
  anchors.
- Local manuscript context: `main.tex`, `mathmacros.tex`, and `commands.tex`.

## Rows Narrowed Or Removed

- Header/status narrowed from a mixed CoHA plus compact-CY source bucket to a
  Hall/CoHA/centre fixture only.
- Source inventory retained only `lurie-higher-algebra`,
  `joyce-vertex-algebra`, `gross-joyce-tanaka`,
  `joyce-upmeier-orientations`, `kinjo-park-safronov-coha`, and the
  vocabulary-only `costello-gwilliam` row.
- Source inventory removed the non-CoHA rows `huang-klemm-quackenbush`,
  `candelas-de-la-ossa-green-parkes`, `ooguri-strominger-vafa`,
  `gopakumar-vafa-I-II`, `bcov-hep-th-9309140`, and
  `costello-li-quantum-bcov`.
- Captured facts removed `hkq-compact-bcov`, `cdgp-periods`,
  `osv-attractor`, and `local-arithmetic`.
- Claim map removed the compact-CY/chiral-volume rows anchored at
  `frontier_mnop_framing_volume.tex:214-238`, `262-309`, `566-603`, and
  `741-801`.  The retained map is only `54-68`, `73-94`, and `146-172`.
- Explicit gaps removed the `N_AJ` and habitat rows from the CoHA gap list.
  They are out of this fixture domain.
- Firewall status no longer claims local BCOV/Costello--Li framework evidence,
  quintic source facts, arithmetic checks, CDGP/OSV/GV source facts, or
  Abel-Jacobi normalisation as CoHA fixture content.

## Retained CoHA Source Facts And Gaps

Retained facts:

- Lurie supplies centre/centralizer and factorization-algebra grammar only.
- Joyce and Gross--Joyce--Tanaka supply Hall/vertex vocabulary for moduli-stack
  homology.
- Joyce--Upmeier and KPS supply orientation-data vocabulary and prerequisites
  for 3CY Hall/CoHA constructions.
- KPS supplies the stable source identifier for 3CY CoHA constructions under
  strong orientation hypotheses.
- Costello--Gwilliam remains only as a local factorization-algebra vocabulary
  fixture; it does not verify an unrestricted centre theorem.

Retained gaps:

- No construction of `F_X=PhiFA_3(Perf(X))` or compact-CY factorization image.
- No construction of `Tr_DT`, `Tr_PT`, or `Tr_GW`.
- No chain-level `sigma_Q` or `sigma_X` in an `E_2` centre.
- No `Aut_{E_2}` rigidity theorem.
- No verification that Joyce--Upmeier or KPS orientation data are chosen and
  matched to the frontier target trace normalisations.
- No null-homotopy or vanishing proof for `Ob_UKD(C_tar)`.
- No local mirrors yet for Lurie, Joyce, Gross--Joyce--Tanaka,
  Joyce--Upmeier, or KPS.

## Checks Run

- `git diff --check`: clean.
- `git diff --check -- references/primary-sources/coha-center-source-anchors-2026-04-30.md`:
  clean.
- Source-row stale-domain grep:
  `rg -n -i '^\|.*(huang|candelas|ooguri|strominger|gopakumar|vafa|bcov|costello--li|costello-li|hkq|cdgp|osv|gv|local-arithmetic|quintic|period|attractor|bps)' references/primary-sources/coha-center-source-anchors-2026-04-30.md`.
  After the final narrowing, no source-inventory or captured-fact rows carry
  non-CoHA compact-CY source entries.
- Fixture out-of-domain grep:
  `rg -n -i -e 'HKQ' -e 'CDGP' -e 'OSV' -e 'Gopakumar' -e 'GV' -e 'N_AJ' -e 'N_\{\\AJ\}' -e 'Abel-Jacobi' -e 'chiral-volume' references/primary-sources/coha-center-source-anchors-2026-04-30.md`.
  Hits remain only in the explicit out-of-domain split-obligations section.
- Core leakage grep:
  `rg -n -i -e '\bCoHA\b' -e 'cohomological Hall' -e 'Hall--' -e 'Hall algebra' -e '\bJoyce\b' -e '\bKinjo\b' -e '\bSafronov\b' -e '\bLurie\b' main.tex theorem-lanes.tex claim-strength-ledger.tex open-obligations.tex`.
  Hits are Lurie factorization-algebra references in `main.tex`, not
  CoHA/Hall/Joyce/KPS leakage.
- Stale-domain grep:
  `rg -n -i -e 'HKQ/CDGP/OSV/GV' -e 'chiral-volume comparison rows' references/primary-sources/coha-center-source-anchors-2026-04-30.md frontier_mnop_framing_volume.tex`.
  The narrowed CoHA fixture has no hit.  The read-only frontier file still has
  stale references at `frontier_mnop_framing_volume.tex:64` and `:240`.

## Files Changed

- `references/primary-sources/coha-center-source-anchors-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-089-coha-fixture-narrowing.md`

## Remaining Split-Fixture Obligations

- Create a compact BCOV/HKQ fixture for modularity, boundary conditions,
  finite-genus quintic data, and the `N=10` row.
- Create a CDGP mirror-quintic period fixture for Picard-Fuchs, mirror-map,
  period-basis, conifold-coordinate, and Abel-Jacobi comparison inputs.
- Create an OSV attractor-rate fixture for the black-hole/topological-string
  comparison and any physical rate formulae.
- Create a GV BPS/resummation fixture for GV I/II, sine expansion,
  integrality status, convergence, and non-perturbative closure claims.
- Create a chiral-volume Abel-Jacobi normalisation fixture for `N_AJ`, Hodge
  metric conventions, `2 pi i` monodromy, and CDGP-period comparison data.
- Create a conifold resurgence/Stokes fixture for the compact-CY resurgence
  and Stokes-normalisation obligations.
- Update `frontier_mnop_framing_volume.tex:64` and `:240` in a later lane:
  both still say the CoHA fixture records HKQ/CDGP/OSV/GV rows.  This lane
  left that file read-only.
- Reconcile `references/source-provenance.md` in a provenance lane if it still
  describes the CoHA fixture as absent or mixed-domain.
