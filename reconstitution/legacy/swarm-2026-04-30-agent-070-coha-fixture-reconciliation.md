# Swarm Report, 2026-04-30, Agent 070

Lane: CoHA/centre source-fixture reconciliation after Agent 064 found
local absence.

Writable scope:

- `references/primary-sources/coha-center-source-anchors-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-070-coha-fixture-reconciliation.md`

No manuscript source file or shared provenance ledger was edited.

## Inputs Loaded

- `CLAUDE.md`
- `~/ecosystem/INVARIANTS.md`, especially Section IV
- `~/ecosystem/AGENTS-HARNESS.md`, especially Section VIII
- `reconstitution/swarm-2026-04-30-agent-064-source-provenance-correction.md`
- `reconstitution/swarm-live-launch-log-2026-04-30.md`
- `frontier_mnop_framing_volume.tex`
- `references/source-provenance.md`
- `references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md`
- `references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md`
- `references/primary-sources/costello-cg-source-anchors-2026-04-28.md`

Required-but-absent inputs after filesystem and index verification:

- Agent 057 report:
  `reconstitution/swarm-2026-04-30-agent-057-coha-center-fixture.md`
- Agent 057 fixture:
  `references/primary-sources/coha-center-source-anchors-2026-04-30.md`
  before this reconstruction
- Agent 054 plan:
  `reconstitution/swarm-2026-04-30-agent-054-mnop-source-fixture-plan.md`
- Habitat anchor:
  `references/primary-sources/habitat-source-anchors-2026-04-30.md`

## Existence Check

Observed from the checkout and index:

- `find reconstitution -maxdepth 1` found Agent 064 only among
  `054/057/064` report patterns.
- `find references -maxdepth 3` found no `coha`, `center`, `centre`, or
  `habitat` source file.
- `git ls-files -s -- ...coha-center... ...agent-057... ...agent-054...`
  returned only the existing Agent 064 report.
- `reconstitution/swarm-live-launch-log-2026-04-30.md:305-324` records
  Agent 054 and Agent 057 as completed and names their expected report
  paths.  The files are not present locally.
- `references/source-provenance.md:8` and Agent 064's report record the
  same local absence.

Conclusion: the CoHA/centre fixture and Agent 057 report did not exist in
this checkout/index.  The correct action was reconstruction of a precise
source/gap fixture, not a duplicate or an inference from the launch log.

## Exact Fixture Edits

Created
`references/primary-sources/coha-center-source-anchors-2026-04-30.md`.

The fixture records:

- stable primary identifiers for Lurie, Joyce, Gross--Joyce--Tanaka,
  Joyce--Upmeier, Kinjo--Park--Safronov, HKQ, CDGP, OSV, and GV;
- present local support from BCOV, Costello--Li, and
  Costello--Gwilliam only as background vocabulary;
- claim-to-source boundaries for `frontier_mnop_framing_volume.tex`;
- explicit non-support for `F_X`, trace maps, `sigma_Q`, `E_2` rigidity,
  `N_AJ`, and `Ob_UKD(C_tar)`.

No `references/source-provenance.md` edit was made because this lane did
not own that file.

## Source Facts And Gaps

Source facts now recorded:

- Lurie supplies centre/factorization grammar by stable official source,
  not a compact CY3 construction.
- Joyce/Gross--Joyce--Tanaka supply vertex/Hall source vocabulary for
  homology of moduli stacks, not the repository's `E_2` centre theorem.
- Joyce--Upmeier and KPS mark orientation data as a prerequisite for 3CY
  CoHA constructions; they do not supply local orientation compatibility.
- HKQ, CDGP, OSV, and GV remain stable-identifier rows until local
  mirrors and line anchors are imported.
- Local BCOV/Costello--Li/Costello--Gwilliam sources support only
  framework and vocabulary already recorded in earlier fixtures.

Gaps kept explicit:

- `F_X=PhiFA_3(Perf(X))`
- `Tr_DT`, `Tr_PT`, `Tr_GW`
- `sigma_Q` / `sigma_X`
- `E_2` automorphism rigidity
- `N_AJ`
- `Ob_UKD(C_tar)`
- HKQ `N=10`, CDGP period conventions, OSV rate, GV convergence, and
  global Stokes data

## Files Changed

- Added
  `references/primary-sources/coha-center-source-anchors-2026-04-30.md`.
- Added
  `reconstitution/swarm-2026-04-30-agent-070-coha-fixture-reconciliation.md`.
- Staged only these two owned paths.  Other staged paths already existed
  in the shared checkout and were not modified by this lane.

## Checks Run

- `find reconstitution -maxdepth 1 -type f \( -iname '*054*' -o -iname '*057*' -o -iname '*064*' \) -print | sort`
- `find references -maxdepth 3 -type f \( -iname '*coha*' -o -iname '*center*' -o -iname '*centre*' -o -iname '*habitat*' \) -print | sort`
- `git ls-files -s -- references/primary-sources/coha-center-source-anchors-2026-04-30.md references/primary-sources/habitat-source-anchors-2026-04-30.md reconstitution/swarm-2026-04-30-agent-057-coha-center-fixture.md reconstitution/swarm-2026-04-30-agent-054-mnop-source-fixture-plan.md reconstitution/swarm-2026-04-30-agent-064-source-provenance-correction.md`
- `rg -n "Agent 0?5[47]|agent-0?5[47]|CoHA|coha|centre|center|chiral-volume|fixture" reconstitution/swarm-live-launch-log-2026-04-30.md reconstitution/attack-heal-216-launch-manifest-2026-04-30.md`
- `rg -n -e 'F_X' -e '\\cF_X' -e 'sigma_Q' -e 'sigma_X' -e 'E_2' -e 'E2' -e 'trace maps' -e 'Tr_' -e 'Ob_UKD' -e 'N_AJ' -e 'Joyce' -e 'Kinjo' -e 'Safronov' -e 'Lurie' -e 'CoHA' -e 'centre' -e 'center' frontier_mnop_framing_volume.tex references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md references/source-provenance.md reconstitution/swarm-2026-04-30-agent-064-source-provenance-correction.md`
- `sed`/`nl -ba` reads of the loaded TeX and fixture files listed above.
- `git diff --check`: passed.
- `git diff --cached --check`: passed after staging.
- Targeted overclaim/stale-status grep across the owned files plus
  `references/source-provenance.md` and `frontier_mnop_framing_volume.tex`:
  hits in owned files are negative or gap statements.  It also confirms
  that `references/source-provenance.md` and
  `frontier_mnop_framing_volume.tex` still contain pre-Agent-070 absent
  wording; those files are outside this lane's write ownership.
- Targeted gap grep for `F_X`, `PhiFA_3`, trace maps, `sigma_Q`,
  `E_2`, `N_AJ`, and `Ob_UKD`: all required gaps are present in the
  fixture and report.

## Remaining Obligations

1. Import local mirrors and extracted text for Lurie, Joyce,
   Gross--Joyce--Tanaka, Joyce--Upmeier, KPS, HKQ, CDGP, OSV, and GV.
2. Add line-level theorem/equation anchors for those sources.
3. Construct or explicitly reject the compact target datum
   `C_tar=(F_X,M_DT,M_PT,M_GW,Tr_DT,Tr_PT,Tr_GW,sigma_X)`.
4. Prove or retain as open the `E_2` rigidity statement for `sigma_Q`.
5. Supply `N_AJ` before interpreting the raw CDGP period ratio as a
   Hodge-normalized Abel-Jacobi norm.
6. Prove a null-homotopy or nonvanishing statement for `Ob_UKD(C_tar)`.
7. Reconcile `references/source-provenance.md` in an owning lane, since
   it still records the Agent 057 fixture as absent before this Agent 070
   reconstruction.
