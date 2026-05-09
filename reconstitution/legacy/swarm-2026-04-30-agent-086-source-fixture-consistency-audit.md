# Agent 086 Source-Fixture Consistency Audit

Lane: final source-fixture consistency audit after Agents 070/080/082.

Write ownership:

- `reconstitution/swarm-2026-04-30-agent-086-source-fixture-consistency-audit.md`

No source fixture, manuscript source, or provenance file was edited.

## Commands Run

- `pwd`
- `git status --short`
- `sed -n '1,240p' CLAUDE.md`
- `sed -n '1,220p' /Users/raeez/ecosystem/INVARIANTS.md`
- `sed -n '1,260p' /Users/raeez/ecosystem/AGENTS-HARNESS.md`
- `nl -ba references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md`
- `nl -ba references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md`
- `nl -ba references/primary-sources/coha-center-source-anchors-2026-04-30.md`
- `nl -ba frontier_mnop_framing_volume.tex`
- `nl -ba references/source-provenance.md`
- `nl -ba reconstitution/swarm-2026-04-30-agent-070-coha-fixture-reconciliation.md`
- `nl -ba reconstitution/swarm-2026-04-30-agent-078-coha-quarantine-audit.md`
- `nl -ba reconstitution/swarm-2026-04-30-agent-080-fixture-index-reconciliation.md`
- `nl -ba reconstitution/swarm-2026-04-30-agent-082-source-provenance-coha-present.md`
- `rg --files references/primary-sources`
- `rg -n "frontier_mnop_framing_volume\\.tex:[0-9]+(?:--|-)[0-9]+|frontier_mnop_framing_volume\\.tex:[0-9]+" references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md references/primary-sources/coha-center-source-anchors-2026-04-30.md`
- `rg -n -i "(CoHA|cohomological Hall|Hall|centre|center|source-gap|Agent 070|Agent 078|HKQ|CDGP|OSV|GV|N_AJ|Ob_UKD|sigma_Q|E_2)" references/source-provenance.md`
- `rg -n -i "(missing|absent|gap|open obligation|remain|not supported|does not|no local mirror|stable identifier|unverified|conditional|target data|not theorem|not a theorem|not proof|not source-grade)" references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md references/primary-sources/coha-center-source-anchors-2026-04-30.md | head -n 260`
- First overclaim grep attempt failed with `zsh: unmatched "`. It was superseded by the corrected command below.
- `rg -n -i 'proves?.*(compact|global|transfer|F_X|sigma|Ob_UKD|E_2|centre|center)|constructs?.*(F_X|sigma|trace|compact)|vanish(es|ing|ed)?.*(Ob_UKD|obstruction)|kill(s|ed)?.*Ob_UKD|theorem-grade.*(CoHA|GV|HKQ|CDGP|OSV|global|compact)|source-grade.*(GV|HKQ|CDGP|OSV|global|compact)' references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md references/primary-sources/coha-center-source-anchors-2026-04-30.md frontier_mnop_framing_volume.tex references/source-provenance.md`
- `nl -ba frontier_mnop_framing_volume.tex | sed -n '54,172p'`
- `nl -ba frontier_mnop_framing_volume.tex | sed -n '214,356p'`
- `nl -ba frontier_mnop_framing_volume.tex | sed -n '542,823p'`
- `nl -ba references/primary-sources/coha-center-source-anchors-2026-04-30.md | sed -n '46,70p'`
- `nl -ba references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md | sed -n '30,68p'`
- `nl -ba references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md | sed -n '383,410p'`
- Local source-anchor spot checks:
  `nl -ba references/primary-sources/bcov-hep-th-9309140.txt | sed -n '23,33p'`,
  `220,233p`, `250,268p`, `285,289p`, `1986,2027p`,
  `4144,4163p`, `4273,4277p`, `4313,4317p`, `4343,4350p`,
  `5150,5187p`, `5208,5233p`, `5234,5253p`, `5282,5305p`,
  `5313,5384p`, `6833,6835p`.
- Local Costello--Li spot checks:
  `nl -ba references/primary-sources/costello-li-quantum-bcov-1201.4501.txt | sed -n '45,90p'`,
  `905,927p`, `3606,3607p`.
- `test -e reconstitution/swarm-2026-04-30-agent-086-source-fixture-consistency-audit.md && echo exists || echo absent`
- `git status --short -- reconstitution/swarm-2026-04-30-agent-086-source-fixture-consistency-audit.md references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md references/primary-sources/coha-center-source-anchors-2026-04-30.md references/source-provenance.md frontier_mnop_framing_volume.tex`
- `git diff --cached --name-status -- references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md references/primary-sources/coha-center-source-anchors-2026-04-30.md references/source-provenance.md frontier_mnop_framing_volume.tex`
- `git diff --name-status -- references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md references/primary-sources/coha-center-source-anchors-2026-04-30.md references/source-provenance.md frontier_mnop_framing_volume.tex`
- `git diff -- references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md`
- `git diff -- references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md`
- `git diff --cached -- references/primary-sources/coha-center-source-anchors-2026-04-30.md | sed -n '1,220p'`
- `git diff --cached -- references/source-provenance.md | sed -n '1,160p'`
- `git diff --check -- reconstitution/swarm-2026-04-30-agent-086-source-fixture-consistency-audit.md`
- `nl -ba reconstitution/swarm-2026-04-30-agent-086-source-fixture-consistency-audit.md | sed -n '1,260p'`
- `nl -ba reconstitution/swarm-2026-04-30-agent-086-source-fixture-consistency-audit.md | sed -n '260,340p'`
- `git diff -- reconstitution/swarm-2026-04-30-agent-086-source-fixture-consistency-audit.md | sed -n '1,260p'`
- `git add reconstitution/swarm-2026-04-30-agent-086-source-fixture-consistency-audit.md`
- `git diff --cached --check -- reconstitution/swarm-2026-04-30-agent-086-source-fixture-consistency-audit.md`
- `git status --short -- reconstitution/swarm-2026-04-30-agent-086-source-fixture-consistency-audit.md references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md references/primary-sources/coha-center-source-anchors-2026-04-30.md references/source-provenance.md frontier_mnop_framing_volume.tex`
- `git diff --cached --name-status -- reconstitution/swarm-2026-04-30-agent-086-source-fixture-consistency-audit.md`
- `git diff --name-status -- reconstitution/swarm-2026-04-30-agent-086-source-fixture-consistency-audit.md`

## Fixture Consistency Verdict

Verdict: conditionally consistent, with CoHA claim-map repairs required
before final source-fixture closure.

The scalar MNOP/PT/DT fixture and the quintic BCOV/GV fixture do not
contradict each other.  They separate source-backed scalar facts from
compact target data: DT/PT MacMahon factorisation is scalar theorem-grade;
PT/GW, HKQ, CDGP, GV, OSV, conifold resurgence, Abel--Jacobi
normalisation, and compact factorization-algebra data remain explicit
gaps.

The CoHA fixture is quarantined in substance.  It repeatedly says that
Lurie/Joyce/Gross--Joyce--Tanaka/Joyce--Upmeier/Kinjo--Park--Safronov
provide grammar, stable identifiers, or prerequisites only.  It does not
claim construction of `F_X`, trace maps, `sigma_Q`, `E_2` rigidity,
`N_AJ`, or `Ob_UKD(C_tar)=0`.  The current
`references/source-provenance.md` row, after Agent 082, agrees: CoHA is
frontier/source-gap context only, not core theorem evidence.

No source claim was found that proves compact/global transfer into
`main.tex`.  The overclaim grep returned denials, firewall statements,
or conjectural/target language, not positive compact/global proof claims.

Residual integration risk: the working tree is still split.  The audit
read the working-tree contents.  At audit time
`references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md` and
`references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md`
were `AM`: staged as new fixtures with later unstaged anchor corrections.
Those unstaged corrections are mechanical and plausible, but they should
be staged by an owning integration lane, not by this report lane.

## Source-by-Source Findings

### MNOP/PT/DT Fixture

Status: consistent.

The local claim map at
`references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md:383-410`
matches the current frontier line map:

- `frontier_mnop_framing_volume.tex:54--68` is the source-fixture status
  firewall.
- `frontier_mnop_framing_volume.tex:73--86` names compact target data as
  target data, not constructed source facts.
- `frontier_mnop_framing_volume.tex:108--119` states the scalar DT/PT
  quintic theorem and marks PT/GW as conditional.
- `frontier_mnop_framing_volume.tex:122--136` proves only the scalar
  Hall-integrated identity and explicitly denies a lift to `F_Q`.
- `frontier_mnop_framing_volume.tex:146--158` is the guarded
  `E_2`-centre target, with no direct scalar-fixture support.
- `frontier_mnop_framing_volume.tex:161--172` is the Joyce--KPS target
  schema and Vol III firewall.
- `frontier_mnop_framing_volume.tex:759--769` and `809--823` are the
  honest-status/firewall summary.

The only observed staged-vs-working-tree change is the correction
`762--769 -> 759--769`, which is plausible because the honest-status
section begins at line 759 and the first item spans 761--769.

No repair is required in this fixture beyond staging the already-present
working-tree anchor correction in the proper owning lane.

### Quintic BCOV/GV Fixture

Status: consistent with one brittle background row.

Local primary-source anchors checked in `bcov-hep-th-9309140.txt` and
`costello-li-quantum-bcov-1201.4501.txt` are plausible:

- BCOV framework/anomaly/quintic-table/conifold/period-vocabulary anchors
  land on the asserted source material.
- Costello--Li anchors land on generalized BCOV theory, quantization,
  QME/locality, and the elliptic-curve uniqueness theorem in their stated
  scope.
- BCOV table lines support genus-zero entries `N=1,...,9`, not `N=10`.
- Local arithmetic rows remain conditional on table provenance, especially
  `n_10^0`.

The current unstaged correction
`frontier_mnop_framing_volume.tex:233-256 -> 244-256` in the
`BCOV-quintic-table` row is plausible: lines 244--256 are exactly the
displayed numerical table; lines 233--243 are contextual firewall
language.

Suspect/brittle row:

- `references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md:36`
  records BCOV constant-map facts and maps them to
  `frontier_mnop_framing_volume.tex:73-94`, `329-355`, and `542-568`.
  These frontier lines are firewall/background lines, not a direct
  constant-map claim in the note.  This is not a contradiction, because
  the row says the constant-map calculation is not the DT MacMahon factor
  and does not prove MNOP/PT/DT.  It is nevertheless too indirect for
  final source-fixture closure.

Recommended repair for that row: either retitle its local use as
`background only; no direct frontier claim currently uses the constant-map
formula`, or add a precise direct frontier anchor if a later source lane
inscribes a constant-map sentence.  Do not let this row be read as support
for DT degree-zero MacMahon factorization.

### CoHA / Centre Fixture

Status: quarantined in substance, but the claim-to-source map has stale
or shifted anchors.

Accepted quarantine statements:

- `coha-center-source-anchors-2026-04-30.md:3-16` says this is a
  source/gap ledger and does not construct `C_tar` or kill `Ob_UKD`.
- `:25-27` says CoHA/centre remains an obstruction/source component, not
  a vanishing obstruction.
- `:50-57` permits only grammar, source vocabulary, stable identifiers,
  or local arithmetic evidence; each row states explicit non-support.
- `:72-106` lists gaps and closes with "not proof input for `main.tex`."
- `references/source-provenance.md:8` matches Agent 082's corrected
  status: fixture present as reconstructed source-gap ledger, Agent 057
  report absent, no theorem support from CoHA.

Suspect rows/anchors:

1. `coha-center-source-anchors-2026-04-30.md:51`

   The local-use anchor for "Joyce vertex algebra on the derived moduli
   stack" is `frontier_mnop_framing_volume.tex:151-159`.  Current lines
   151--159 are the `sigma_Q` automorphism target, not the Joyce--KPS
   remark.  The plausible target is
   `frontier_mnop_framing_volume.tex:161-172`.

2. `coha-center-source-anchors-2026-04-30.md:63`

   The claim shape says "No CoHA/centre fixture was present; no
   Lurie/Joyce/KPS centre support is imported."  Current frontier lines
   54--64 say the reconstructed CoHA/centre fixture is present and supplies
   source vocabulary/stable identifiers.  The boundary is correct, but the
   claim shape is stale after Agent 070/082.

3. `coha-center-source-anchors-2026-04-30.md:65`

   The row anchors `sigma_Q in Aut_{E_2}(Z_{E_2}(F_Q))` and rigidity to
   `frontier_mnop_framing_volume.tex:137-148`.  Current lines 137--142
   are the end of the DT/PT proof sketch, and line 148 only begins the
   compact target sentence.  The plausible anchor is
   `frontier_mnop_framing_volume.tex:146-158`.

4. `coha-center-source-anchors-2026-04-30.md:66`

   The row anchors "Generic compact CY3 via Joyce--KPS vertex algebra" to
   `frontier_mnop_framing_volume.tex:151-159`.  Current lines 151--159 are
   still the `sigma_Q` target.  The plausible anchor is
   `frontier_mnop_framing_volume.tex:161-172`.

5. `coha-center-source-anchors-2026-04-30.md:67`

   The row anchors "Chiral-volume scalar input and genus-zero table through
   `N=10`" to `frontier_mnop_framing_volume.tex:214-238`.  Lines 214--221
   are the preceding `S^3`-framing target, and the anchor stops before the
   displayed `N=10` table at lines 244--256.  The plausible anchor is
   `frontier_mnop_framing_volume.tex:225-256`, or `233-256` if the row is
   meant to capture only scalar table input.

6. `coha-center-source-anchors-2026-04-30.md:68`

   The tail-fit/raw-period row uses `frontier_mnop_framing_volume.tex:262-309`.
   This catches the statement of the numerical proposition but misses the
   proof's raw period values at lines 321--323.  If the row is meant to
   include the arithmetic proof, use `frontier_mnop_framing_volume.tex:279-325`.

7. `coha-center-source-anchors-2026-04-30.md:70`

   The honest-status row uses `frontier_mnop_framing_volume.tex:741-801`.
   The honest-status summary proper is `frontier_mnop_framing_volume.tex:759-823`.
   If the row also wants the preceding chiral-volume relation, split it
   into two rows rather than using a broad range.

These defects are anchor/wording defects, not source-support leakage.
Every suspect row still carries an explicit boundary denying compact
construction or theorem-grade transfer.

## Recommended Repairs

1. Repair the CoHA fixture claim map before final closure:
   - `:51` anchor `151-159 -> 161-172`.
   - `:63` claim shape should say the reconstructed CoHA/centre fixture is
     present but imports only vocabulary/stable identifiers and no theorem
     support.
   - `:65` anchor `137-148 -> 146-158`.
   - `:66` anchor `151-159 -> 161-172`.
   - `:67` anchor `214-238 -> 225-256` or `233-256`.
   - `:68` anchor `262-309 -> 279-325` if arithmetic proof lines are
     intended.
   - `:70` anchor `741-801 -> 759-823`, or split the relation-to-chiral
     volume material from the honest-status summary.

2. Split non-CoHA compact-CY source-gap identifiers out of the CoHA row
   when a future owning lane refines provenance.  HKQ/CDGP/OSV/GV appear
   in both the quintic fixture and the CoHA fixture.  Current wording keeps
   them as missing-source rows, so there is no contradiction; the split
   would reduce future over-read risk.

3. Tighten the BCOV constant-map row in the quintic fixture.  Mark it as
   background-only unless a direct frontier sentence uses the constant-map
   formula.  Keep the existing non-support sentence that it is not the DT
   MacMahon factor and not an MNOP/PT/DT theorem source.

4. Stage the existing working-tree anchor corrections to the MNOP/quintic
   fixtures in an owning integration lane.  This report did not stage them.

5. Do not import any CoHA, HKQ/CDGP/OSV/GV, Abel--Jacobi, compact BCOV,
   global Stokes, `F_X`, trace-map, `sigma_Q`, or `Ob_UKD` claim into
   `main.tex` as theorem input until local mirrors, line-level anchors,
   and the missing constructions/null-homotopies are supplied.

## Final Audit State

No fatal source contradiction found.

No compact/global transfer claim found.

CoHA remains quarantined in the frontier/source-gap layer.

Final closure requires the CoHA anchor repairs above and a decision about
splitting non-CoHA compact-CY source gaps out of the CoHA fixture.
