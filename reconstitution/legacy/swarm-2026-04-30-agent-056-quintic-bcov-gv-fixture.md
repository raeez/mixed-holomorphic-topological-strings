# Swarm Report, 2026-04-30, Agent 056

Lane: quintic BCOV/GV numerical-source fixture implementation.

Writable scope:

- `references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-056-quintic-bcov-gv-fixture.md`

No manuscript source file was edited.

## Source Facts Captured

Created the dedicated source fixture at
`references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md`.
Captured the following local facts with line anchors:

| Fact | Anchors | Local role |
|---|---|---|
| BCOV framework: higher-loop topological amplitudes, master anomaly, KS theory, mirror-map curve-counting role. | `references/primary-sources/bcov-hep-th-9309140.txt:23-33`, `:220-233`, `:250-268`, `:285-289` | Supports BCOV framework vocabulary in `frontier_mnop_framing_volume.tex:592-602`, not a compact quintic all-genus theorem. |
| BCOV holomorphic anomaly recursion and master equation. | `references/primary-sources/bcov-hep-th-9309140.txt:1986-2027` | Supports the BCOV anomaly-equation source role in `frontier_mnop_framing_volume.tex:600-602`, `:643-645`, `:681-683`. |
| BCOV constant-map computation. | `references/primary-sources/bcov-hep-th-9309140.txt:4144-4150`, `:4159-4163`, `:4273-4277`, `:4313-4317`, `:4343-4350` | Supports the constant-map role; explicitly separated from the DT degree-zero MacMahon factor. |
| BCOV quintic family and conifold point. | `references/primary-sources/bcov-hep-th-9309140.txt:5150-5167`, `:5168-5175` | Supports `psi=1` conifold vocabulary used in the frontier note. |
| BCOV Yukawa/conifold behavior. | `references/primary-sources/bcov-hep-th-9309140.txt:5176-5187`, `:5208-5233` | Supports conifold-local asymptotic vocabulary, not Stokes normalization. |
| BCOV mirror-period vocabulary. | `references/primary-sources/bcov-hep-th-9309140.txt:5234-5253`, `:5282-5305` | Supports period/mirror-map vocabulary only; exact CDGP convention remains missing. |
| BCOV quintic table. | `references/primary-sources/bcov-hep-th-9309140.txt:5313-5345`, `:5355-5384` | Supports genus-zero entries `N=1,...,9` used in `frontier_mnop_framing_volume.tex:287-306`; does not support `N=10`. |
| Costello-Li BCOV quantization framework. | `references/primary-sources/costello-li-quantum-bcov-1201.4501.txt:45-80`, `:88-90`, `:905-927` | Supports `frontier_mnop_framing_volume.tex:595-599` and the non-support firewall for compact quintic all-genus claims. |

## Missing Local Source Obligations

No local HKQ, CDGP, GV, OSV, Strominger, Vafa/Schwinger,
Shenker-Marino, Cecotti--Codesido--Marino, Schubert, Katz,
Ellingsrud-Stromme, Kontsevich, or Givental mirror was found under
`references/primary-sources`.

Precise obligations recorded in the fixture:

- HKQ `arXiv:hep-th/0612125`: needed for Table 1, the `N=10` value, and the
  stated finite BCOV anomaly-recursion range.
- CDGP 1991: needed for the Picard-Fuchs operator, `psi`/`z` convention,
  conifold point, period basis, mirror map, prepotential, and the formulas for
  `omega_0`, `omega_1`.
- GV I/II: needed for the sine expansion and BPS interpretation.
- OSV plus a local derivation ledger: needed for the `5 log 5` rate.
- Strominger 1995, Vafa/Schwinger, Shenker-Marino, and
  Cecotti--Codesido--Marino: needed for the conifold-trinity and `S_c=1`
  normalization claims.
- Low-degree historical sources: needed if the Schubert/Katz/Ellingsrud-
  Stromme/Kontsevich/Givental attributions remain theorem-grade.
- A committed numerical ledger or script: needed before the finite fit and
  period arithmetic are imported into the bound manuscript.

## Claim-To-Source Map

| Frontier anchor | Claim | Local support now | Status |
|---|---|---|---|
| `frontier_mnop_framing_volume.tex:287-306` | Quintic genus-zero table through `N=10`. | BCOV supports `N=1,...,9`; arithmetic checked from displayed table. | `N=10` remains HKQ-missing. |
| `frontier_mnop_framing_volume.tex:307-327` | `a_N` values, minimum at `N=3`, monotone tail. | Local arithmetic check. | Evidence only until source provenance for all table entries is complete. |
| `frontier_mnop_framing_volume.tex:329-379` | Tail fit, raw CDGP period value, OSV rate. | Local arithmetic confirms the fit and period evaluation from the displayed formulas. | HKQ/CDGP/OSV sources and committed numerical ledger still missing. |
| `frontier_mnop_framing_volume.tex:396-405` | Raw period is not an Abel-Jacobi norm without `N_AJ`. | Firewall statement confirmed by missing CDGP/Abel-Jacobi normalization data. | Keep as target problem. |
| `frontier_mnop_framing_volume.tex:592-629` | Costello-Li BCOV framework and GV package separation. | Costello-Li supports the framework; GV source is absent. | GV formula remains missing-local-fixture. |
| `frontier_mnop_framing_volume.tex:631-710` | Conditional BCOV/GV closure target. | BCOV supports anomaly/conifold vocabulary only. | HKQ/CDGP/GV/GW-PT/convergence/Stokes data remain target obligations. |
| `frontier_mnop_framing_volume.tex:712-750` | Conifold trinity and `S_c=1`. | BCOV supports `psi=1` conifold and pole behavior only. | Conjectural; source fixtures for large-order/Schwinger/Strominger/resurgence missing. |
| `frontier_mnop_framing_volume.tex:768-795` | Mirror-period recovery and small-degree fixture. | BCOV supports first three numerical entries and points to CDGP. | CDGP period/prepotential source absent; conditional status preserved. |
| `frontier_mnop_framing_volume.tex:813-872` | Honest-status summary. | Fixture supports finite-evidence/firewall classification. | Do not import as theorem input before missing fixtures and target data are supplied. |

## Files Changed

- Added `references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md`.
- Added `reconstitution/swarm-2026-04-30-agent-056-quintic-bcov-gv-fixture.md`.

## Checks Run

- `python3` arithmetic check for `a_N`, increments, least-squares tail fit,
  raw period evaluation, and `chi(Q)=-200`.
  Results:
  `L=7.592485639949`, `alpha=-3.320444733707`,
  `beta=0.447708390605`, max residual `4.620400846811e-06`;
  `omega_0(5^-5)=1.07072535097019855`,
  `omega_1(5^-5)=-8.12776502268470475`,
  `|omega_1/omega_0|=7.59089622312577943`;
  `chi(Q)=-200`.
- `git diff --check -- references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md reconstitution/swarm-2026-04-30-agent-056-quintic-bcov-gv-fixture.md`
  had no whitespace output before staging. After staging the owned new files,
  `git diff --cached --check -- ...` passed with no whitespace errors.
- Targeted overclaim grep:
  `rg -n "proves|proved|theorem-grade|all-genus|global Stokes|Ob_UKD.*0|certifies|kills|establishes" ...`.
  Matches were reviewed; each occurrence is in non-support, missing-source,
  or firewall context.
- Targeted missing-source grep:
  `rg -n "HKQ|CDGP|Gopakumar|Vafa|OSV|Strominger|Cecotti|Codesido|Marino|Shenker|missing|Missing|not support|not supplied|not proved|non-support|obligation" ...`.
  Matches confirm the intended missing-local-fixture ledger.

## Remaining Fixture Obligations

The fixture is a source-gap closure, not a theorem closure. Remaining work:

1. Mirror and extract HKQ/CDGP/GV/OSV/Strominger/resurgence sources.
2. Add a committed numerical ledger or script for the table-derived checks.
3. Add a separate MNOP/PT/DT fixture before relying on the MacMahon
   factorization in the standalone note.
4. Keep all compact-CY, global BCOV/GV, chiral-volume, Abel-Jacobi, and
   Stokes-sheaf claims behind `C_tar` and `Ob_UKD(C_tar)` until the target
   construction and source fixtures are complete.
