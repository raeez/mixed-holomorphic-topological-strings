# Swarm Report, 2026-04-30, Agent 084

Lane: non-CoHA compact-CY source fixture split plan.

Writable scope:

- `reconstitution/swarm-2026-04-30-agent-084-noncoha-compact-cy-fixture-split-plan.md`

No manuscript source file, provenance ledger, or source fixture was edited.

## Inputs Loaded

- `CLAUDE.md`
- `~/ecosystem/INVARIANTS.md`, especially Section IV and git discipline.
- `~/ecosystem/AGENTS-HARNESS.md`, especially Section VIII and shared-checkout scope discipline.
- `reconstitution/swarm-2026-04-30-agent-070-coha-fixture-reconciliation.md`
- `reconstitution/swarm-2026-04-30-agent-082-source-provenance-coha-present.md`
- `references/primary-sources/coha-center-source-anchors-2026-04-30.md`
- `references/source-provenance.md`
- `frontier_mnop_framing_volume.tex`
- Supporting local context: Agent 078 quarantine audit, Agent 076 frontier follow-up, Agent 079 provenance correction, `references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md`, `references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md`, and Vol III chiral-volume anchors in `~/calabi-yau-quantum-groups`.

## Verdict

The split is necessary. The current CoHA/centre fixture correctly quarantines
CoHA from `main.tex`, but it also carries unrelated compact-CY rows:
HKQ, CDGP, OSV, GV, local arithmetic, and the chiral-volume
Abel-Jacobi normalization gap. This makes "CoHA fixture" read as a general
compact-CY source bucket. That is the wrong domain boundary.

After migration, the CoHA fixture should contain only:

- Lurie centre/centralizer and factorization-algebra grammar.
- Joyce and Gross--Joyce--Tanaka Hall/vertex vocabulary.
- Joyce--Upmeier orientation data as prerequisite language.
- Kinjo--Park--Safronov 3CY CoHA vocabulary.
- Costello--Gwilliam centre/factorization vocabulary only if it is used to
  delimit centre grammar.

It should not contain HKQ, CDGP, OSV, GV, BCOV arithmetic, `N_AJ`,
chiral-volume asymptotics, conifold resurgence, or historical rational-curve
counts.

## Rows To Split

| Current CoHA fixture anchor | Present row or passage | Mathematical domain | Migration target |
|---|---|---|---|
| `references/primary-sources/coha-center-source-anchors-2026-04-30.md:3-16` | Scope/status says the CoHA fixture records HKQ/CDGP/OSV chiral-volume comparison data and lists HKQ, CDGP, OSV, GV beside Lurie/Joyce/KPS. | Mixed domain header. | Rewrite in a CoHA-narrowing lane so the header lists only centre/Hall/CoHA sources; point out-of-domain readers to the compact-CY fixture suite. |
| `:38` | `huang-klemm-quackenbush`. | Compact BCOV holomorphic-anomaly bootstrap and finite-genus quintic data. | `references/primary-sources/compact-cy-bcov-hkq-source-anchors-2026-04-30.md` |
| `:39` | `candelas-de-la-ossa-green-parkes`. | Mirror-quintic periods, Picard-Fuchs equation, mirror map, conifold coordinate, prepotential conventions. | `references/primary-sources/mirror-quintic-cdgp-period-source-anchors-2026-04-30.md` |
| `:40` | `ooguri-strominger-vafa`. | Black-hole/topological-string attractor comparison and physical rate language. | `references/primary-sources/osv-attractor-rate-source-anchors-2026-04-30.md` |
| `:41` | `gopakumar-vafa-I-II`. | GV BPS interpretation and sine-expansion resummation. | `references/primary-sources/gopakumar-vafa-bps-source-anchors-2026-04-30.md` |
| `:42-43` | BCOV and Costello--Li background rows. | BCOV framework and perturbative quantization background. | Keep in `references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md`; remove from CoHA except for a cross-reference. |
| `:54` | `hkq-compact-bcov` captured fact. | HKQ table, modularity, boundary/gap conditions, genus range. | `compact-cy-bcov-hkq-source-anchors-2026-04-30.md` |
| `:55` | `cdgp-periods` captured fact. | CDGP period basis and mirror-quintic conventions. | `mirror-quintic-cdgp-period-source-anchors-2026-04-30.md`; the Abel-Jacobi comparison part goes to the `N_AJ` fixture. |
| `:56` | `osv-attractor` captured fact. | OSV attractor and black-hole entropy comparison. | `osv-attractor-rate-source-anchors-2026-04-30.md` |
| `:57` | `local-arithmetic` captured fact. | Local numerical verification, not primary source evidence. | `references/computations/quintic-chiral-volume-arithmetic-ledger-2026-04-30.md` or a dedicated script lane; do not keep as a CoHA source row. |
| `:67` | Chiral-volume scalar input and genus-zero table through `N=10`. | Quintic enumerative table plus HKQ missing row. | Existing quintic fixture plus `compact-cy-bcov-hkq-source-anchors-2026-04-30.md`. |
| `:68` | Tail fit and raw CDGP period comparison. | Computation plus CDGP periods plus OSV comparison plus `N_AJ`. | Computation ledger, CDGP fixture, OSV fixture, and `chiral-volume-abel-jacobi-normalization-source-anchors-2026-04-30.md`. |
| `:69` | Conditional GV non-perturbative closure. | GV expansion, compact BCOV/HKQ finite evidence, conifold resurgence/Stokes. | GV fixture, HKQ fixture, CDGP fixture, and `conifold-resurgence-stokes-source-anchors-2026-04-30.md`. |
| `:70` | Honest-status summary joining CoHA and chiral-volume normalization. | Provenance summary, not a source domain. | Update `references/source-provenance.md` after the split; CoHA row should no longer carry compact-CY rows. |
| `:83-87` | `N_AJ`, `Ob_UKD`, and local-mirror gaps for HKQ/CDGP/OSV/GV/Joyce/KPS/Lurie. | Mixed obstruction ledger. | `N_AJ` goes to the Abel-Jacobi normalization fixture; HKQ/CDGP/OSV/GV go to their domain fixtures; Joyce/KPS/Lurie remain CoHA; `Ob_UKD(C_tar)` stays an obstruction/theorem-lane item, not a source fixture. |
| `:100-105` | Firewall status joins CoHA and chiral-volume package. | Mixed firewall. | Split into CoHA-only firewall in the CoHA fixture and compact-CY firewalls in the domain fixtures/provenance row. |

## Proposed Fixture Files

### 1. CoHA/centre, narrowed

Path: `references/primary-sources/coha-center-source-anchors-2026-04-30.md`

Domain: centre, Hall, orientation, and 3CY CoHA grammar only.

Allowed source keys:

- `lurie-higher-algebra`
- `joyce-vertex-algebra`
- `gross-joyce-tanaka`
- `joyce-upmeier-orientations`
- `kinjo-park-safronov-coha`
- optional `costello-gwilliam` cross-reference for centre/factorization vocabulary.

Forbidden rows:

- HKQ, CDGP, OSV, GV, BCOV arithmetic, Costello--Li compact BCOV, `N_AJ`,
  conifold resurgence, chiral-volume asymptotics.

Local anchors after narrowing:

- `frontier_mnop_framing_volume.tex:54-68`
- `frontier_mnop_framing_volume.tex:73-94`
- `frontier_mnop_framing_volume.tex:146-172`

The narrowed fixture may still say that it does not construct `F_X`,
trace maps, `sigma_Q`, `E_2` rigidity, or `Ob_UKD(C_tar)`. It must not
use those negatives to carry unrelated compact-CY source names.

### 2. Compact BCOV / HKQ finite-genus fixture

Path:
`references/primary-sources/compact-cy-bcov-hkq-source-anchors-2026-04-30.md`

Domain: Huang--Klemm--Quackenbush compact Calabi-Yau topological-string
bootstrap, modularity, boundary/gap conditions, finite-genus quintic
evidence, and the `N=10` genus-zero table row.

Claim anchors:

- `frontier_mnop_framing_volume.tex:115-119`
- `frontier_mnop_framing_volume.tex:233-256`
- `frontier_mnop_framing_volume.tex:279-325`
- `frontier_mnop_framing_volume.tex:584-607`
- `frontier_mnop_framing_volume.tex:774-783`

Required contents:

- Stable HKQ identifier, local mirror status, text-extraction status.
- Exact table/equation anchors for the `n_10^0` value if imported.
- Exact genus/degree range. The current note says genus `22`; that must be
  checked against the source before any theorem-grade statement.
- Boundary/gap condition anchors.
- Non-support: no `F_X`, no trace maps, no `sigma_Q`, no `N_AJ`, no GV
  convergence, no global Stokes sheaf.

### 3. Mirror-quintic CDGP period fixture

Path:
`references/primary-sources/mirror-quintic-cdgp-period-source-anchors-2026-04-30.md`

Domain: Candelas--de la Ossa--Green--Parkes mirror-quintic data.

Claim anchors:

- `frontier_mnop_framing_volume.tex:289-296`
- `frontier_mnop_framing_volume.tex:314-325`
- `frontier_mnop_framing_volume.tex:591-597`
- `frontier_mnop_framing_volume.tex:712-741`
- `frontier_mnop_framing_volume.tex:744-756`

Required contents:

- Picard-Fuchs operator and variable convention.
- `psi` versus `z`, including the conifold point and whether the local
  convention is `z=5^-5`.
- Period basis, mirror map, logarithmic period, and prepotential formula.
- Which normalized periods are source facts and which numerical evaluations
  are local computations.
- Non-support: CDGP periods do not by themselves give the Hodge-normalized
  Abel-Jacobi norm `N_AJ`.

### 4. GV BPS/resummation fixture

Path:
`references/primary-sources/gopakumar-vafa-bps-source-anchors-2026-04-30.md`

Domain: Gopakumar--Vafa I/II, BPS-state interpretation, GV sine expansion,
summation indices, and variable conventions.

Claim anchors:

- `frontier_mnop_framing_volume.tex:570-582`
- `frontier_mnop_framing_volume.tex:584-607`
- `frontier_mnop_framing_volume.tex:613-620`
- `frontier_mnop_framing_volume.tex:712-739`
- `frontier_mnop_framing_volume.tex:795-806`

Required contents:

- GV I/II stable identifiers and local mirror status.
- Exact form of the sine expansion and the variable `lambda`/`g_s`
  convention.
- Status of BPS integrality: physics proposal, theorem in restricted cases,
  or open compact-CY input.
- Non-support: no coefficient-growth theorem, no convergence domain, no
  global non-perturbative closure, no CoHA centre automorphism.

### 5. OSV attractor-rate fixture

Path:
`references/primary-sources/osv-attractor-rate-source-anchors-2026-04-30.md`

Domain: Ooguri--Strominger--Vafa black-hole/topological-string attractor
comparison and its role as a physical rate comparison.

Claim anchors:

- `frontier_mnop_framing_volume.tex:299-302`
- `frontier_mnop_framing_volume.tex:329-335`
- `frontier_mnop_framing_volume.tex:584-588`
- `frontier_mnop_framing_volume.tex:774-783`
- `frontier_mnop_framing_volume.tex:812-823`

Required contents:

- OSV stable identifier, local mirror status, and exact attractor formula
  anchors.
- Separate local derivation ledger for any displayed `5 log 5` rate if the
  manuscript keeps that number.
- Non-support: OSV does not identify the raw CDGP period ratio with a
  Hodge-normalized Abel-Jacobi norm and does not prove chiral-volume
  asymptotics.

### 6. Chiral-volume Abel-Jacobi normalization fixture

Path:
`references/primary-sources/chiral-volume-abel-jacobi-normalization-source-anchors-2026-04-30.md`

Domain: the `N_AJ` normalization problem: Abel-Jacobi map, Hodge metric on
`J^2(X)`, `2 pi i` monodromy convention, and comparison of a CDGP period
basis with the chiral-volume right-hand side.

Claim anchors in this repository:

- `frontier_mnop_framing_volume.tex:223-231`
- `frontier_mnop_framing_volume.tex:344-355`
- `frontier_mnop_framing_volume.tex:744-756`
- `frontier_mnop_framing_volume.tex:774-783`
- `frontier_mnop_framing_volume.tex:812-823`

Vol III anchors for convention matching:

- `~/calabi-yau-quantum-groups/FRONTIER.md:85-93`
- `~/calabi-yau-quantum-groups/notes/wave12_a14_chiral_volume.tex:156-180`
- `~/calabi-yau-quantum-groups/notes/wave12_a14_chiral_volume.tex:190-212`
- `~/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:3117-3148`
- `~/calabi-yau-quantum-groups/chapters/theory/introduction.tex:2546-2562`

Required contents:

- Primary Griffiths/normal-function source status, if imported.
- Exact Hodge metric convention and normalization of `Omega`.
- Explicit comparison datum between CDGP periods and `|AJ(C_H)|`.
- Status of the factor `(2 pi)^-1`.
- Non-support: this fixture does not source HKQ tables, GV expansion, OSV
  attractor formulae, or any CoHA/centre construction.

### 7. Conifold resurgence/Stokes fixture

Path:
`references/primary-sources/conifold-resurgence-stokes-source-anchors-2026-04-30.md`

Domain: conifold large-order behavior, Schwinger poles, Strominger
hypermultiplet mechanism, Shenker--Marino growth, Cecotti--Codesido--Marino
resurgence, and local/global Stokes normalization.

Claim anchors:

- `frontier_mnop_framing_volume.tex:540-568`
- `frontier_mnop_framing_volume.tex:613-658`
- `frontier_mnop_framing_volume.tex:661-693`
- `frontier_mnop_framing_volume.tex:696-709`
- `frontier_mnop_framing_volume.tex:795-800`

Required contents:

- Separate source rows for Strominger, Vafa/Schwinger, Shenker--Marino, and
  Cecotti--Codesido--Marino.
- Local versus global Stokes distinction.
- Exact status of `S_c=1` and `A_BCOV=A_Schwinger=A_period`.
- Non-support: no global resurgent sheaf and no compact-CY closure theorem.

### 8. Historical low-degree quintic fixture

Path:
`references/primary-sources/quintic-low-degree-enumerative-source-anchors-2026-04-30.md`

Domain: Schubert, Katz, Ellingsrud--Stromme, Kontsevich, Givental, and
other historical direct-count or mirror-theorem sources for low-degree
quintic counts.

Claim anchors:

- `frontier_mnop_framing_volume.tex:329-341`
- `frontier_mnop_framing_volume.tex:737-741`
- `references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md:88-90`

Required contents:

- Exact source for each historical branch assertion retained in the note.
- Separation between direct Fano-geometric counts and BCOV/HKQ table data.
- Non-support: no large-`N` chiral-volume limit and no compact source
  closure.

### 9. Local computation ledger, not a primary-source fixture

Path:
`references/computations/quintic-chiral-volume-arithmetic-ledger-2026-04-30.md`

Optional companion script:
`scripts/check_quintic_chiral_volume_arithmetic.py`

Domain: reproducible arithmetic only.

Claim anchors:

- `frontier_mnop_framing_volume.tex:244-323`
- `references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md:49-54`

Required contents:

- `a_N=N^-1 log n_N`.
- Tail fit residuals.
- Raw period formula evaluation after CDGP convention is accepted.
- `chi(Q)=-200`.
- Non-support: computations do not source HKQ/CDGP/OSV/GV facts and do
  not prove the chiral-volume limit.

## Claim-To-Source Domain Map

| Claim shape | Correct support domain | Explicit non-support |
|---|---|---|
| `Z_{E_2}(F_X)`, `sigma_Q`, `E_2` rigidity as target grammar | CoHA/centre fixture only for language: Lurie, Joyce/GJT, Joyce--Upmeier, KPS. | No HKQ/CDGP/GV/OSV row supports centre construction. |
| Quintic genus-zero table through `N=10` | BCOV table for `N<=9`; HKQ fixture for `N=10` if imported. | CoHA fixture cannot support numerical table rows. |
| Tail fit `L=7.593` and residuals | Local computation ledger, conditional on table provenance. | Computation does not source the table or the large-`N` limit. |
| Raw mirror period `|omega_1/omega_0|(5^-5)` | CDGP period fixture plus local computation. | CDGP period ratio is not an Abel-Jacobi norm without `N_AJ`. |
| OSV comparison value and attractor language | OSV fixture plus separate derivation ledger for `5 log 5`. | OSV does not prove chiral-volume asymptotics. |
| GV sine expansion | GV fixture. | No convergence theorem, global Stokes sheaf, or CoHA automorphism follows. |
| `N_AJ` | Chiral-volume Abel-Jacobi normalization fixture. | HKQ/CDGP/OSV/GV do not supply this by themselves. |
| `Ob_UKD(C_tar)` | Theorem-lane/open-obligation ledger, not a source fixture. | Do not encode it as killed by any source row. |

## Local Anchors

- Agent 070 recorded that the reconstructed CoHA fixture lists Lurie,
  Joyce/GJT, Joyce--Upmeier, KPS, HKQ, CDGP, OSV, and GV together:
  `reconstitution/swarm-2026-04-30-agent-070-coha-fixture-reconciliation.md:63-71`.
- Agent 070 also recorded that HKQ/CDGP/OSV/GV are only stable identifiers:
  `reconstitution/swarm-2026-04-30-agent-070-coha-fixture-reconciliation.md:80-89`.
- Agent 078 identified the brittle broadening and recommended the split:
  `reconstitution/swarm-2026-04-30-agent-078-coha-quarantine-audit.md:58-66`.
- Agent 082 preserved the same future split obligation in provenance:
  `reconstitution/swarm-2026-04-30-agent-082-source-provenance-coha-present.md:62-76`.
- Current provenance row still records the mixed state:
  `references/source-provenance.md:8`.
- Current CoHA fixture rows to split:
  `references/primary-sources/coha-center-source-anchors-2026-04-30.md:3-16`,
  `:38-43`, `:54-57`, `:67-70`, `:83-87`, `:100-105`.
- Existing quintic fixture already owns most non-CoHA source-gap language:
  `references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md:1-13`,
  `:22-28`, `:49-68`, `:70-108`.
- Frontier anchors requiring migration:
  `frontier_mnop_framing_volume.tex:54-68`, `:115-119`, `:223-243`,
  `:279-325`, `:344-355`, `:540-568`, `:570-607`, `:623-658`,
  `:661-693`, `:712-756`, `:761-823`.
- Vol III chiral-volume convention anchors:
  `~/calabi-yau-quantum-groups/FRONTIER.md:85-93`,
  `~/calabi-yau-quantum-groups/notes/wave12_a14_chiral_volume.tex:156-180`,
  `~/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:3117-3148`,
  `~/calabi-yau-quantum-groups/chapters/theory/introduction.tex:2546-2562`.

## Recommended Implementation Lanes

1. `CoHA-narrowing lane`

   Write ownership:
   `references/primary-sources/coha-center-source-anchors-2026-04-30.md`
   and a report only.

   Task: remove HKQ/CDGP/OSV/GV/local-arithmetic/chiral-volume rows from
   the CoHA fixture, preserve only centre/Hall/CoHA grammar, and leave
   cross-reference placeholders to the new compact-CY fixtures. Do not edit
   `frontier_mnop_framing_volume.tex` or `references/source-provenance.md`
   in this lane.

2. `HKQ compact-BCOV lane`

   Write ownership:
   `references/primary-sources/compact-cy-bcov-hkq-source-anchors-2026-04-30.md`
   and a report only.

   Task: create the HKQ fixture. Import or record local-mirror absence for
   `hep-th/0612125`; do not claim line anchors unless a local mirror and
   text extraction exist.

3. `CDGP period lane`

   Write ownership:
   `references/primary-sources/mirror-quintic-cdgp-period-source-anchors-2026-04-30.md`
   and a report only.

   Task: create the CDGP fixture for Picard-Fuchs, periods, mirror map,
   prepotential, conifold coordinates, and convention matching. Keep
   Abel-Jacobi normalization out except as explicit non-support.

4. `GV/OSV split lanes`

   Write ownership:
   `references/primary-sources/gopakumar-vafa-bps-source-anchors-2026-04-30.md`,
   `references/primary-sources/osv-attractor-rate-source-anchors-2026-04-30.md`,
   and one report per lane.

   Task: keep GV expansion and OSV attractor physics separate. Neither lane
   may claim `N_AJ`, convergence, or CoHA centre support.

5. `Chiral-volume normalization lane`

   Write ownership:
   `references/primary-sources/chiral-volume-abel-jacobi-normalization-source-anchors-2026-04-30.md`
   and a report only.

   Task: define the source-gap status for `N_AJ`; check Vol III conventions;
   identify primary Abel-Jacobi/Hodge-metric sources still missing. Do not
   import HKQ/CDGP/GV/OSV rows except as external dependencies.

6. `Conifold-resurgence lane`

   Write ownership:
   `references/primary-sources/conifold-resurgence-stokes-source-anchors-2026-04-30.md`
   and a report only.

   Task: split Strominger, Vafa/Schwinger, Shenker--Marino, and
   Cecotti--Codesido--Marino rows away from the quintic BCOV fixture.
   Preserve the local/global Stokes distinction.

7. `Computation-ledger lane`

   Write ownership:
   `references/computations/quintic-chiral-volume-arithmetic-ledger-2026-04-30.md`,
   optional `scripts/check_quintic_chiral_volume_arithmetic.py`, and a
   report only.

   Task: make the `a_N`, tail fit, residuals, raw period arithmetic, and
   `chi(Q)` checks reproducible. Keep the ledger subordinate to source
   fixtures.

8. `Integration lane`

   Write ownership:
   `frontier_mnop_framing_volume.tex`, `references/source-provenance.md`,
   and a report only.

   Task: after the fixture files exist, update `frontier_mnop_framing_volume.tex:54-68`,
   `:115-119`, `:237-242`, `:344-355`, `:761-783`, and the provenance row so
   the CoHA fixture is no longer described as carrying HKQ/CDGP/OSV/GV or
   chiral-volume normalization. This lane must run a targeted grep showing
   no HKQ/CDGP/OSV/GV/chiral-volume strings remain in the CoHA fixture except
   in an explicit "out of domain" sentence.

## Migration Prompts

### CoHA narrowing prompt

You own only `references/primary-sources/coha-center-source-anchors-2026-04-30.md`
and your report. Load Agent 084, Agent 078, Agent 082, the current CoHA
fixture, and `frontier_mnop_framing_volume.tex`. Narrow the CoHA fixture to
Lurie/Joyce/Gross--Joyce--Tanaka/Joyce--Upmeier/Kinjo--Park--Safronov and
optional Costello--Gwilliam centre vocabulary. Remove HKQ, CDGP, OSV, GV,
BCOV arithmetic, local arithmetic, and chiral-volume normalization as source
rows. Add one out-of-domain pointer to the compact-CY fixture suite. Stage
only the fixture and your report.

### HKQ prompt

You own only
`references/primary-sources/compact-cy-bcov-hkq-source-anchors-2026-04-30.md`
and your report. Load Agent 084, the quintic BCOV/GV fixture, and
`frontier_mnop_framing_volume.tex`. Create a HKQ-only source-gap fixture for
compact-CY holomorphic-anomaly recursion, modularity, boundary/gap
conditions, genus/degree range, and the `N=10` quintic row. If the local HKQ
mirror is absent, record stable identifier only and do not invent line
anchors. Stage only your fixture and report.

### CDGP prompt

You own only
`references/primary-sources/mirror-quintic-cdgp-period-source-anchors-2026-04-30.md`
and your report. Load Agent 084, the quintic BCOV/GV fixture, and
`frontier_mnop_framing_volume.tex`. Create a CDGP-only fixture for the mirror
quintic Picard-Fuchs operator, `psi`/`z` convention, conifold point, period
basis, mirror map, and prepotential. Record that CDGP periods do not supply
the Hodge-normalized Abel-Jacobi datum `N_AJ`. Stage only your fixture and
report.

### GV prompt

You own only
`references/primary-sources/gopakumar-vafa-bps-source-anchors-2026-04-30.md`
and your report. Load Agent 084, the MNOP/PT/DT fixture, the quintic BCOV/GV
fixture, and `frontier_mnop_framing_volume.tex`. Create a GV-only fixture for
the sine expansion, BPS interpretation, summation indices, variable
conventions, and theorem/physics status. Do not claim convergence, global
Stokes data, OSV attractor formulae, or CoHA centre support. Stage only your
fixture and report.

### OSV prompt

You own only
`references/primary-sources/osv-attractor-rate-source-anchors-2026-04-30.md`
and your report. Load Agent 084, the quintic BCOV/GV fixture, and
`frontier_mnop_framing_volume.tex`. Create an OSV-only fixture for the
black-hole/topological-string attractor comparison. If the number `5 log 5`
is retained, record it as a separate derivation obligation unless the source
itself supplies the exact value in the local convention. Do not claim
Abel-Jacobi normalization or chiral-volume asymptotics. Stage only your
fixture and report.

### Abel-Jacobi normalization prompt

You own only
`references/primary-sources/chiral-volume-abel-jacobi-normalization-source-anchors-2026-04-30.md`
and your report. Load Agent 084, `frontier_mnop_framing_volume.tex`, and the
Vol III chiral-volume anchors named in Agent 084. Create a source-gap fixture
for `N_AJ`, the Hodge metric on `J^2(X)`, the `2 pi i` monodromy convention,
and the comparison between CDGP periods and `|AJ(C_H)|`. Record missing
primary Griffiths/normal-function sources if no local mirrors exist. Stage
only your fixture and report.

### Integration prompt

You own only `frontier_mnop_framing_volume.tex`,
`references/source-provenance.md`, and your report. Load Agent 084 and the
completed split fixtures. Update the frontier source-fixture paragraph and
provenance row so CoHA/centre is strictly Lurie/Joyce/GJT/Joyce--Upmeier/KPS
grammar. Point HKQ, CDGP, GV, OSV, `N_AJ`, conifold resurgence, historical
counts, and arithmetic to their domain fixtures. Run targeted greps proving
the CoHA fixture no longer carries compact-CY source rows. Stage only owned
paths.

## Checks Run

- Required `sed`/`nl` reads of Agent 070, Agent 082, the CoHA fixture,
  source provenance, and `frontier_mnop_framing_volume.tex`.
- Targeted `rg` for HKQ/CDGP/OSV/GV/chiral-volume/`N_AJ`/`Ob_UKD` across
  the CoHA fixture, source provenance, frontier note, Agent 070, Agent 078,
  and Agent 082.
- Read-only checks of the existing MNOP/PT/DT and quintic BCOV/GV fixtures.
- Read-only Vol III convention checks for compact CY-A3 and chiral-volume
  anchors.
- `test -e reconstitution/swarm-2026-04-30-agent-084-noncoha-compact-cy-fixture-split-plan.md`
  returned absent before this report was written.

## Files Changed

- Added
  `reconstitution/swarm-2026-04-30-agent-084-noncoha-compact-cy-fixture-split-plan.md`.

No source fixture, manuscript source, or provenance ledger was edited.
