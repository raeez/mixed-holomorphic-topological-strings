# Worker 6 cross-repo firewall attack-heal report

Date: 2026-04-28.

Worktree: `/private/tmp/topological-strings-remainder-wave5-20260428-061212/crossrepo`.

## Claim attacked

The vulnerable claim shape was:

> The local Dirac-brane/formal Hamiltonian theorem, or its admissible
> protected-sector formulation, exports a compact Calabi-Yau threefold,
> global BCOV, Vol III CY-to-chiral/chiral-homology, Igusa, Borcherds,
> BKM, or K3xE theorem.

This claim is false as stated. The local theorem remembers a formal
Hamiltonian disk, a point-brane Ext algebra, a brane-line
factorization-current convention, and a scalar anomaly quotient. It
does not remember the compact topology, negative-cyclic Calabi-Yau
class, BCOV propagator and gauge fixing, holomorphic anomaly equation,
worldsheet or specialization curve, framing, Borcherds input Jacobi
form, Weyl chamber, compact Hall orientation, or Vol III
factorization-homology data required by the sibling projects.

## False-transfer modes

1. Twisted-M universality could be misread as a globalization functor
   from ambient backgrounds to compact CY3/BCOV claims.
2. A local BCOV/Kodaira-Spencer source convention could be misread as
   proving global BCOV amplitudes or holomorphic anomaly equations.
3. Vol III notation such as `\Phi_d`, `\SpCh`, or Stage 2 specialization
   could be imported without the matched compact object, trace pairing,
   curve, and specialization datum.
4. The Igusa/Borcherds/BKM route could be inferred from the scalar
   anomaly number, although the local theorem supplies no Jacobi form,
   denominator identity, Weyl chamber, primitive recognition theorem,
   compact Hall source, orientation character, or CHL/K3xE host.
5. Vol I/II trace identities could be collapsed from scoped
   three-factor statements to unrestricted two-factor or local-disk
   consequences.

## Healed local language

The repair inscribes two explicit no-transfer statements and a theorem
template firewall.

- `tate-P3-universality.tex`: added
  `Lemma~\ref{lem:admissibility-not-globalization}`. It states that
  admissible protected-sector reduction is not a functor from ambient
  twisted-M backgrounds, compact CY3 geometry, Vol III CY-to-chiral
  data, or Igusa/BKM data. Its proof identifies exactly which local data
  survive the restriction and which global data are absent.
- `tate-P5-cross-volume.tex`: added
  `Lemma~\ref{lem:no-formal-disk-transfer}`. It states that the local
  formal-disk theorem does not determine compact CY3, global BCOV, Vol
  III, chiral-homology, Igusa, Borcherds, BKM, or K3xE specializations.
- `tate-P5-cross-volume.tex`: added
  `Definition~\ref{defn:matched-conventions-theorem-datum}`. Any future
  transfer theorem must state the dimension, ambient object, curve,
  brane/boundary condition, trace pairing, framing, coefficient
  topology, anomaly normalization, deformation parameter,
  QME/obstruction hypothesis, and comparison morphism.
- `tate-P5-cross-volume.tex`: added
  `Remark~\ref{rmk:matched-conventions-templates}`. It gives separate
  templates for Vol III CY-to-chiral, compact BCOV, and Igusa/BKM
  transfers, and marks them as templates rather than proved theorems.
- `claim-strength-ledger.tex` now records cross-volume consequences as
  `not asserted`, with both no-transfer lemmas as the reason.
- `open-obligations.tex` now points future cross-volume work to the
  matched-conventions datum and templates.

No sibling repository was edited.

## Sibling anchors read

Read-only anchors used for the attack:

- `~/calabi-yau-quantum-groups/FRONTIER.md`, especially the two-stage
  `\Phi_d` factorization, the scoped trace identity, the distinct
  `0,3,5,24` constructions, and the open BKM/bracket-level questions.
- `~/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex`,
  especially the object-level versus functorial `\Phi_d` distinction
  and the requirement for witnessed K3-fibre/Borcherds loci.
- `~/calabi-yau-quantum-groups/chapters/examples/cy_d_kappa_stratification.tex`,
  especially the separation of `\kappa_{\mathrm{BKM}}`, chiral, BCOV,
  and Hodge-theoretic invariants, and the failed additive split.
- `~/chiral-bar-cobar/CLAUDE.md`, especially the Vol III two-stage
  specialization discipline, E1-shadow language, universal Borcherds
  weight identity, and scoped three-factor trace identity.
- `~/chiral-bar-cobar-vol2/CLAUDE.md`, especially the rule that Stage 2
  specialization is never inversion and the scoped trace identity.
- `~/igusa-cusp-form/CLAUDE.md` and `~/igusa-cusp-form/AGENTS.md`,
  especially the instruction that the Igusa paper is a structural
  sibling and that Borcherds/BKM claims must remain consistent with Vol
  III and BCOV conventions.
- `~/igusa-cusp-form/main.tex` and the local Igusa primitive-recognition
  reports, especially the statements that the Borcherds determinant does
  not itself provide compact Hall constants, brackets, parities, Hopf
  pairings, orientations, or compact BPS OPE data.

## Changed files

- `tate-P3-universality.tex`
- `tate-P5-cross-volume.tex`
- `claim-strength-ledger.tex`
- `open-obligations.tex`
- `references/source-provenance.md`
- `reconstitution/attack-heal-wave5-crossrepo-2026-04-28.md`

## Commands run

- `sed -n ...` and `nl -ba ... | sed -n ...` to read local governance,
  manuscript fragments, owned files, and sibling anchors.
- `rg -n ...` to locate BCOV, CY3, Vol III, Igusa, Borcherds, BKM,
  `\Phi_d`, `\kappa`, trace-identity, and include-line claims. One
  overescaped `\Phi` pattern produced an `rg` parse error and was rerun
  with a safe pattern.
- `git status --short -- ...` to inspect only the owned write surface.
- `git diff --check -- tate-P3-universality.tex tate-P5-cross-volume.tex
  claim-strength-ledger.tex open-obligations.tex
  reconstitution/attack-heal-wave5-crossrepo-2026-04-28.md
  references/source-provenance.md`; it passed.
- `pdflatex -interaction=nonstopmode -halt-on-error -draftmode
  -output-directory=/tmp/topological-strings-crossrepo-worker6-tex
  main.tex`, which failed because the tmp worktree has a broken
  `raeez-math-template.sty` symlink.
- `TEXINPUTS=.:/Users/raeez/latex-template//: pdflatex
  -interaction=nonstopmode -halt-on-error -draftmode
  -output-directory=/tmp/topological-strings-crossrepo-worker6-tex
  main.tex`, run twice. Both runs completed successfully; the first
  resolved the new forward references, and the second had only ordinary
  typography/font warnings.
- After the main thread repaired
  `/private/tmp/topological-strings-remainder-wave5-20260428-061212/latex-template`
  as a symlink to `/Users/raeez/latex-template`, `make pdf` was run
  from this worktree. It completed successfully and wrote
  `out/main.pdf` with 140 pages. `out/main.log` contains no unresolved
  reference, fatal-error, emergency-stop, undefined-control-sequence, or
  changed-label marker by the final grep check.

## Remaining open questions

1. Vol III should continue to carry any compact CY3 or global
   CY-to-chiral theorem internally, with its own matched compact object,
   trace pairing, specialization curve, and factorization-homology data.
2. Any compact BCOV consequence still needs a separate theorem with
   compact geometry, volume form, propagator, gauge fixing, anomaly
   equation, zero-mode treatment, and counterterms.
3. Igusa/BKM consequences still require the compact Hall/chiral source,
   orientation character, primitive recognition theorem, Jacobi input,
   Weyl chamber, and scalar DT/PT/OP normalization. The local
   Dirac-brane theorem supplies none of these.
4. The main thread repaired the tmp parent template symlink; no further
   template-path follow-up remains for this worker.
