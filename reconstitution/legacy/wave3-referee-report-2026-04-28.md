# Wave 3 referee report: convergence after wave-two integration

Date: 2026-04-28  
Role: W3-H06 convergence referee  
Writable surface: `reconstitution/wave3-referee-report-2026-04-28.md` only

## Verdict

**Converged for the stable local core.** I find no remaining severity 1--3
attack inside the manuscript's stable core. The wave-two healing has either
healed, invalidated, or explicitly moved out of core every prior high-severity
attack I could reproduce.

This is not a claim that all advertised future mathematics is proved. The
current manuscript is converged because the surviving theorem-grade statements
are local, algebraic, and status-scoped, while the unreduced quantum,
regulator-independence, all-order Costello-graph, Rees/Fourier, and global
transfer claims are marked as conditional, conjectural, or open.

## Stable Core

The stable core I inspected is the following.

- **Finite Dirac / brane probe algebra.** The finite algebraic open-sector
  construction and scalar-reduced trace algebra remain proof-bearing and are
  not used to assert a cotangent-module identification.
- **Stable PBW trace and one-psi shadow.** The `\Psi_{k,l}` labels are now
  consistently treated as PBW / special-fibre labels. They are not identified
  with CE cotangent coordinates or Matlis principal parts
  (`local-dictionary.tex:42-47`, `local-dictionary.tex:73-77`,
  `local-dictionary.tex:145-152`, `main.tex:1029-1081`).
- **CE/PV cotangent identity.** The continuous dual coordinates `u_I` and odd
  variables `c^I` are separated from PBW labels and matched to the PV side only
  in the shifted-cotangent CE model (`claim-strength-ledger.tex:36-42`,
  `theorem-lanes.tex:88-138`).
- **Matlis principal-part module.** The principal-part completion is now
  handled as its own topological module, with residue pairing and coadjoint
  action proved separately, and with polynomial realization explicitly ruled
  out (`appendix-matlis-principal-parts.tex:39-62`,
  `appendix-matlis-principal-parts.tex:113-155`,
  `appendix-matlis-principal-parts.tex:186-227`).
- **Reduced brane-line / defect-current comparison.** The factorization-current
  discussion is restricted to the compact-current source and reduced
  post-contraction consequences; unreduced centrality homotopies remain outside
  the proved core (`appendix-factorization-current-conventions.tex:1-170`,
  `theorem-lanes.tex:188-291`).
- **Degree-zero Moyal / radial-parts comparison.** The Moyal comparison is a
  finite algebraic, degree-zero statement, backed by the local coefficient
  computation and a conditional external radial-parts input. It does not prove
  a descendant or all-order graph lift (`claim-strength-ledger.tex:70-75`,
  `appendix-radial-parts-moyal.tex:35-73`,
  `appendix-radial-parts-moyal.tex:156-211`,
  `appendix-radial-parts-moyal.tex:254-283`).
- **Weighted Tate formalism.** The weighted category controls internal finite
  windows and graphwise locality, but regulator independence and full QME
  descent are not claimed as proved (`tate-T1-weighted-completion.tex:15-23`,
  `tate-T1-weighted-completion.tex:488-550`,
  `tate-T1-weighted-completion.tex:571-585`).
- **Cross-volume firewall.** Vol III, compact CY, BKM, Borcherds, and Igusa
  consequences are no longer exported from the local theorem package
  (`tate-P5-cross-volume.tex:18-49`).

The former umbrella theorem has been reduced to a summary corollary of named
local proof owners (`main.tex:1132-1193`). The theorem-lane file now declares
itself an index rather than a proof-bearing substitute (`theorem-lanes.tex:1-10`).

## Unhealed severity 1--3 attacks

None inside the stable core.

The remaining serious mathematical items are not unhealed attacks against the
current core, because they are explicitly outside the proved surface:

- unreduced cotangent factorization-center morphism and centrality homotopies;
- one-antifield / descendant quantum lift;
- mixed brane-defect QME and regulator independence;
- all-order Costello graph realization beyond the checked low-order tests;
- Rees/Fourier bridge from PBW `\Psi` labels to Matlis principal parts;
- compact-CY, Vol III, BKM, Borcherds, or Igusa transfer.

These appear as open obligations or conditional lanes, not as unsupported
theorems (`open-obligations.tex:33-70`, `open-obligations.tex:80-104`,
`claim-strength-ledger.tex:77-98`, `claim-strength-ledger.tex:100-114`).

## New attacks introduced by healing

No new severity 1--3 mathematical attack was introduced by the wave-two
healing. I do see three lower-severity follow-up issues.

1. **Generated artifact hygiene.** The worktree's checked/generated auxiliary
   files were stale relative to the current TeX source. A clean `/tmp` build
   succeeds, so this is not a source-level convergence failure, but the final
   integration checkout should refresh generated artifacts from a clean build.
2. **Layout polish.** A clean build reports one overfull hbox in
   `tate-T3-quillen-equivalence.tex:84-92`. This is release polish, not a
   mathematical blocker.
3. **External theorem anchoring.** The radial-parts appendix explicitly marks
   its radial-parts theorem as conditional on the standard external input. That
   is an acceptable status downgrade for convergence, but a publication pass
   should add the final primary-source convention ledger.

## Verification gaps

The following gaps remain after convergence, but none is currently used as a
load-bearing proved claim.

- visual/page-level QA of the 137-page PDF;
- primary-source equation-number anchoring for all external normalization
  inputs;
- final clean rebuild in the shared integration checkout to eliminate stale
  auxiliary-file noise;
- optional line-wrap repair for the single overfull hbox;
- future mathematical cycles only if the manuscript promotes one of the open
  QME, regulator, descendant, Rees/Fourier, or cross-volume items into the
  theorem-grade core.

## Commands and results

Read-only/source-inspection commands:

- `sed -n ... CLAUDE.md`, `sed -n ... ~/ecosystem/INVARIANTS.md`,
  `sed -n ... ~/ecosystem/AGENTS-HARNESS.md`: loaded repository and harness
  rules before inspection.
- `rg --files`: enumerated source, report, script, and appendix surfaces.
- `rg ...` scans for stale process language, overclaim terms, PBW/Matlis
  identifications, cross-volume transfer assertions, theorem-lane status, and
  open-obligation markers.
- `sed -n ...` on the current TeX sources and prior ledgers: inspected the
  healed theorem package, abstract, claim-strength ledger, local dictionary,
  theorem lanes, weighted Tate files, cross-volume firewall, and new appendices.

Executable verification:

- `python3 scripts/check_one_psi_homology.py`: pass. It checked primitive
  one-psi homology in 36 bidegrees, open Hamiltonian action in 240 cases, and
  closed/principal-part coadjoint formulas in 1225 cases.
- `python3 scripts/check_moyal_coefficients.py`: pass. It checked the Moyal
  coefficient sweep, odd coefficient normalizations through order 11, Capelli
  triangular round-trip, radial-parts rank-2 tests, connected cumulant bracket,
  midpoint graph weights, and even-order vanishing through order 10.
- Clean `/tmp` TeX build with copied current sources and
  `TEXINPUTS=/tmp/topological-strings-referee-clean-20260428:/Users/raeez/latex-template:`:
  three `pdflatex` passes produced a 137-page PDF with no unresolved references
  or citations. Final log scan found one overfull hbox only.

Auxiliary-artifact note:

- Direct build in the worktree was polluted by stale generated files, including
  an old malformed `main.aux`. The clean `/tmp` build isolates the source state
  and verifies that the current source compiles.

## Required next-cycle lenses

No further attack-heal cycle is required for convergence of the stable core.
If the principal chooses another cycle, it should be a release/anchoring cycle,
not a mathematical rescue cycle:

- clean-build and generated-artifact hygiene;
- visual PDF QA and TOC/page-number audit;
- primary-source normalization ledger for imported radial-parts, Costello, and
  BV conventions;
- optional line-wrap polish;
- renewed attack only if an open conditional item is promoted to theorem status.

## Files changed

- `reconstitution/wave3-referee-report-2026-04-28.md`

No manuscript TeX was edited.

## Residual blockers

No residual severity 1--3 blocker against the stable local core. The only
residual blockers are for future scope expansion or release polish: unreduced
QME/regulator/descendant/Rees/Fourier/global-transfer proofs, stale generated
artifacts in the integration checkout, and the single overfull hbox.
