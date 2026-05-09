# Agent 235 Report: Open A-infinity Koszul Cyclic Acceptance

Task: attack and heal the open-string `A_\infty` / Koszul / cyclic
comparison theorem surface for the local mixed HT model on
`\R^2_top x \C^2_hol`. No manuscript edits made. Companion construction
target:
`reconstitution/open-ainfty-koszul-cyclic-acceptance-construction-target-2026-04-30.md`.

## Claim Attacked

The threatened claim is that the stable open trace/Koszul algebra of the
Dirac brane is already the Koszul dual, cyclic/LQT large-`N` object, or
factorization-centre source for the closed Hamiltonian CE/PV observables.

Status after attack: false in that raw form. The healed target is exact:
prove an accepted open `A_\infty` datum `K1--K7` in an admissible
finite-window topology, or prove the obstruction theorem for the
nonvanishing cone/Roos/LQT/Psi-rho/Casimir component.

## File Anchors

- Open Dirac/BV model:
  `main.tex:118-144`, `main.tex:2609-2671`, `main.tex:2673-2784`,
  `claim-strength-ledger.tex:866-878`.
- Stable cyclic trace model:
  `main.tex:4298-4315`, `main.tex:4422-4512`,
  `main.tex:4650-4712`, `main.tex:4801-4825`,
  `main.tex:4975-5050`, `main.tex:5061-5099`,
  `theorem-lanes.tex:55-150`.
- CE/PV and admissible Koszul layer:
  `main.tex:157-168`, `main.tex:204-234`,
  `main.tex:5223-5294`, `main.tex:5411-5460`,
  `theorem-lanes.tex:152-180`, `theorem-lanes.tex:1875-2133`,
  `open-obligations.tex:102-116`.
- Trace, Ext, topology dictionary:
  `local-dictionary.tex:99-114`, `local-dictionary.tex:1226-1257`.
- Claim ledger status:
  `claim-strength-ledger.tex:344-349`, `claim-strength-ledger.tex:842-887`.
- Vol II control surface:
  `/Users/raeez/chiral-bar-cobar-vol2/notes/antipatterns_catalogue.md:9919-10029`.
- Source bibliography anchors:
  `main.tex:8853-8870` for Loday-Quillen/Tsygan,
  `main.tex:9104-9122` for Priddy/Loday-Vallette,
  `main.tex:9230-9250` for Lefevre-Hasegawa/Quillen.

## Valid Attacks

1. PBW special fibre is not deformation-level Koszul duality. The
   proved stable trace algebra is degreewise and associated-graded.
   A filtered deformation theorem needs the actual open `A_\infty`
   algebra, cobar morphism, and exact completion data.

2. The polynomial one-psi class `Psi_{a,b}` is not the Matlis
   principal part `rho_{a,b}`. The manuscript proves the module-action
   obstruction, and the script gives explicit Moyal mismatches.

3. Full cyclic normal ordering is obstructed. Killing psi-words would
   kill nonzero primitive one-psi homology; hence no full contraction
   `QK+KQ=id-iN` exists on the cyclic complex.

4. LQT is not yet integrated. The current theorem surface uses
   Procesi-Razmyslov stable invariant theory and a cyclic-word model.
   A genuine LQT clause must specify `gl_\infty(A_psi)`, the reduced
   cyclic complex, finite-window stable range, scalar quotient, and
   compatibility with `A_\infty` transfer.

5. The strict formal disk does not satisfy the needed kernel or
   pronilpotence hypotheses. The strict Casimir obstruction and the
   low-degree non-pronilpotent splitting obstruction block the raw
   bar-cobar upgrade.

6. Degreewise stable large `N` is not a physical large-`N` state. It
   supplies candidate primitive labels only. A physical statement still
   needs state, topology, normalization, QME, and convergence data.

## Healed Construction Target

Build the accepted comparison in the complete finite-window ML category.
The datum must contain:

- source one-object cyclic dg categories with
  `Omega_c^*(I) \otimes Lambda(epsilon_1,epsilon_2) \otimes End(C^N)`;
- Dirac/Koszul reduction `Q psi=[phi_1,phi_2]` and scalar line bookkeeping;
- reduced cyclic dg algebra `A_psi=T(x,y,psi)`, `d psi=xy-yx`, plus full
  reduced cyclic complex, not only the necklace `H_0` shadow;
- LQT map from primitive stable CE chains of `gl_\infty(A_psi)` to cyclic
  chains, in fixed word degree and stable range `N >= d`;
- transferred complete cyclic `A_\infty` algebra `A_op`;
- closed target `B_CE/PV=C^bullet_CE,cont(g_adm)` in an admissible
  relative/weighted envelope;
- twisting cochain `tau_op` with the full `A_\infty` Maurer-Cartan
  equation;
- exact cone/Roos obstruction complex and exact continuous dualization.

The raw PBW trace source can enter only as associated graded. For the
closed cotangent side, either replace it by a principal-part/Fourier-Rees
open source or prove a new bridge; the direct label map `Psi -> rho` is
blocked.

## Obstruction Theorem

For the raw polynomial stable PBW source and the strict formal disk
target, the universal property is obstructed by

```text
(O_cyc, O_Psi-rho, O_Cas, O_lc,
 H^*Cone(gr kappa_tau),
 lim^1 source, lim^1 target,
 H^*Cone(lambda_LQT)).
```

The first four components are already witnessed locally:

- `O_cyc`: `main.tex:4801-4825`.
- `O_Psi-rho`: `theorem-lanes.tex:1813-1848` and
  `scripts/check_one_psi_homology.py:627-651`.
- `O_Cas`: `theorem-lanes.tex:1785-1811`.
- `O_lc`: `theorem-lanes.tex:1850-1873`.

Thus the next theorem is not a weak conditional. It is the construction
of the admissible object killing this tuple, or the obstruction theorem
showing which component survives in every admissible attempt.

## Verification

Commands run:

```bash
python3 scripts/check_one_psi_homology.py
python3 scripts/check_derived_intersection_N2.py
rg -n -F -e 'A_\infty' -e 'Koszul' -e 'cyclic' -e 'Loday' -e 'Quillen' -e 'Tsygan' -e 'large-N' -e 'Ext' main.tex theorem-lanes.tex local-dictionary.tex open-obligations.tex claim-strength-ledger.tex mathmacros.tex commands.tex
```

Results:

- one-psi script passed all advertised finite checks and found the
  explicit PBW-vs-Moyal obstruction
  `ad^*_{z1^4}(delta_1,1) = -24 hbar^2 delta_0,4` versus
  `Psi_1,1 -> 4 Psi_4,0`.
- N=2 derived-intersection script passed and verified `Q(Tr psi)=0`,
  with `dim Tor^1 >= 1` witnessed by `[Tr psi]`.
- `python3 scripts/check_moyal_coefficients.py --help` was terminated
  after no useful output; no report claim depends on it.

Files changed and staged target: the two `reconstitution/` reports only.
