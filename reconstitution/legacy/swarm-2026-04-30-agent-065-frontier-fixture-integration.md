# Swarm Report, 2026-04-30, Agent 065

Lane: standalone MNOP/framing frontier fixture integration.

Writable scope:

- `frontier_mnop_framing_volume.tex`
- `reconstitution/swarm-2026-04-30-agent-065-frontier-fixture-integration.md`

No `main.tex` edit was made.

## Load Status

Loaded local harness files: `CLAUDE.md`, `~/ecosystem/INVARIANTS.md`,
and `~/ecosystem/AGENTS-HARNESS.md`.

Loaded present source reports and fixtures:

- `reconstitution/swarm-2026-04-30-agent-055-mnop-pt-dt-fixture.md`
- `reconstitution/swarm-2026-04-30-agent-056-quintic-bcov-gv-fixture.md`
- `references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md`
- `references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md`
- `frontier_mnop_framing_volume.tex`

The requested Agent 018, 049, 054, and 057 report files were not present
in this checkout after targeted `find`/`rg` checks. The requested CoHA
fixture `references/primary-sources/coha-center-source-anchors-2026-04-30.md`
was also absent. `references/source-provenance.md` records that absence
and forbids importing Lurie/Joyce/Kinjo--Park--Safronov centre support,
compact-target `F_X`, trace maps, `\sigma_Q`, `E_2` rigidity, or
`Ob_UKD` null-homotopies from that lane.

## Claims Integrated

1. Scalar DT/PT theorem-grade claim retained:
   `Z_DT(Q;q)=M(-q)^{chi(Q)} Z_PT(Q;q)` with `chi(Q)=-200`.
   The note now points to the MNOP/PT/DT fixture and spells out the
   reduced/unreduced decomposition.
2. Compact target data separated:
   `C_tar(X)=(F_X,M_DT,M_PT,M_GW,Tr_DT,Tr_PT,Tr_GW,sigma_X)` is now a
   named target datum, not a constructed object.
3. PT/GW and MNOP substitution kept conditional:
   KKV/HKQ/PT-GW rows remain missing-source obligations; no finite-genus
   quintic theorem is imported.
4. Quintic numerical evidence integrated with exact source status:
   BCOV supports entries `N<=9`; the displayed `N=10` row remains
   conditional on HKQ. Tail-fit and raw period arithmetic are retained
   as arithmetic evidence.
5. Raw period value corrected from `7.599` to `7.5909`, matching the
   quintic fixture arithmetic:
   `omega_0(5^-5)=1.070725350970`,
   `omega_1(5^-5)=-8.127765022685`,
   `|omega_1/omega_0|=7.590896223126`.
6. Abel--Jacobi bridge gap marked:
   the missing `N_AJ` normalisation is now explicit; raw CDGP period data
   are not asserted to be a Hodge-normalised Abel--Jacobi norm.
7. BCOV/GV/conifold/Stokes bridge preserved as conditional schema:
   BCOV/Costello--Li framework and conifold vocabulary are source-backed;
   HKQ, CDGP, GV, OSV, Strominger, Vafa/Schwinger, Shenker--Marino, and
   Cecotti--Codesido--Marino rows remain open.
8. CoHA/Joyce/KPS centre line demoted to absent-fixture target schema:
   no centre, trace-map, `sigma_Q`, rigidity, or Vol III transfer is
   claimed.

## Fixture Anchors Used

- MNOP fixture:
  `references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md`,
  especially primary rows for Behrend--Fantechi Hilbert schemes,
  Bridgeland Hall curve-counting, Toda DT/PT, MNOP I/II, PT stable
  pairs, and the local claim-to-source map.
- Agent 055 report:
  scalar `chi(Q)=-200`, reduced DT/PT theorem status, and explicit
  non-support for compact `F_X`, modules, trace maps, `sigma_Q`, and
  `Ob_UKD` null-homotopies.
- Quintic fixture:
  `references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md`,
  especially local source inventory, captured BCOV/Costello--Li facts,
  local arithmetic checks, missing local fixture obligations, and firewall
  status.
- Agent 056 report:
  BCOV table support only through `N=9`, exact arithmetic values, and
  missing HKQ/CDGP/GV/OSV/resurgence obligations.
- Source provenance:
  pending CoHA/centre fixture row, used as negative evidence only.

## Exact Edits

- `frontier_mnop_framing_volume.tex:54-64`: added source-fixture status
  remark naming the two present fixtures and the absent CoHA fixture.
- `frontier_mnop_framing_volume.tex:68-98`: replaced canonical
  dualisable `F_X` module assertions with scalar source rows plus target
  datum `C_tar(X)`.
- `frontier_mnop_framing_volume.tex:100-134`: kept scalar DT/PT
  factorisation theorem; rewrote proof around Bridgeland, Behrend--
  Fantechi, Toda auxiliary status, and no factorisation-algebra lift.
- `frontier_mnop_framing_volume.tex:137-158`: made the `E_2` centre
  package and Joyce--KPS line explicitly conditional on absent CoHA
  source data.
- `frontier_mnop_framing_volume.tex:219-337`: made the quintic table
  conditional at `N=10`, corrected the period arithmetic, and inserted
  the `N_AJ` Abel--Jacobi normalisation gap.
- `frontier_mnop_framing_volume.tex:525-690`: attached BCOV/GV/conifold
  claims to the quintic fixture and marked all missing HKQ/CDGP/GV/OSV/
  resurgence rows as conditional target data.
- `frontier_mnop_framing_volume.tex:694-738`: made mirror-period
  recovery conditional on CDGP/GV source rows and removed theorem-grade
  historical low-degree claims.
- `frontier_mnop_framing_volume.tex:741-800`: updated the honest-status
  summary with fixture-backed scalar theorem status and exact source/gap
  boundaries.

## Overclaim Checks

- No compact CY/global BCOV theorem was imported into `main.tex`.
- No Vol III theorem, BKM/Igusa consequence, or compact-CY transfer was
  promoted.
- No CoHA centre support was claimed from the absent Agent 057 fixture.
- No `F_X`, trace-map, `sigma_Q`, `E_2` rigidity, or `Ob_UKD`
  null-homotopy was asserted as constructed.
- The only retained theorem-grade frontier claim from the new fixtures is
  scalar DT/PT factorisation. Quintic `N=10`, CDGP period normalisation,
  GV expansion, OSV rate, and Stokes normalization remain conditional.

## Checks Run

- `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/agent065-frontier-texcheck frontier_mnop_framing_volume.tex`
  was run twice with `TEXINPUTS=.:`.
  Result: PDF produced successfully. Remaining warnings are existing-style
  hyperref PDF-string warnings, underfull boxes, and one `0.9504pt`
  overfull hbox near the conifold evidence paragraph; no fatal TeX error.
- `rg` over the frontier note for CoHA/centre, compact/global, HKQ/CDGP/
  GV/OSV/Stokes, theorem-grade, and fixture-status terms was reviewed to
  check that positive claims now carry conditional or missing-source
  status where required.
- `git diff --check -- frontier_mnop_framing_volume.tex
  reconstitution/swarm-2026-04-30-agent-065-frontier-fixture-integration.md`
  passed with no whitespace errors.
- After staging the owned paths, full `git diff --check` and
  `git diff --cached --check` also passed with no whitespace errors.

## Files Changed

- `frontier_mnop_framing_volume.tex`
- `reconstitution/swarm-2026-04-30-agent-065-frontier-fixture-integration.md`

## Remaining Frontier Obligations

1. Supply or recover Agent 018, 049, 054, and 057 reports if their
   findings are to be integrated.
2. Add the missing CoHA/centre fixture before any Lurie/Joyce/KPS
   centre, compact `F_X`, trace-map, `sigma_Q`, rigidity, or
   `Ob_UKD`-null-homotopy statement is upgraded.
3. Add HKQ local source mirrors for the `N=10` row and genus-22 claims.
4. Add CDGP period/prepotential source mirrors and an `N_AJ`
   normalisation ledger before identifying raw mirror periods with
   Hodge-normalised Abel--Jacobi norms.
5. Add GV, OSV, Strominger, Vafa/Schwinger, Shenker--Marino, and
   Cecotti--Codesido--Marino source fixtures before treating BCOV/GV
   closure or conifold Stokes normalization as more than conditional
   target data.
6. Keep the `main.tex` firewall intact until matched-conventions descent
   and all named obstruction null-homotopies are actually constructed.
