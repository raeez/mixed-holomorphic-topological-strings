# Adversarial attack ledger for the reconstitution

Date: 2026-04-28

Original purpose, historical: identify, without mercy and without
rhetorical compromise, every remaining structural, mathematical,
expository, and proof-status weakness that prevented the then-current
manuscript from realizing the full reconstitution architecture. Each
attack records what survives in stronger form.

This ledger is internal.  It is not a publication section.  Its job is to drive
the next inscription passes.

## Current Status Preamble

Status as of the Wave 4 ledger-healing pass on 2026-04-28: this file is
the first adversarial attack ledger after the initial reconstitution
pass. It is an evidentiary attack record, not a current defect list.
Occurrences of "current manuscript", "still", "not complete", "survives",
"required repair", and exact line anchors below describe the state
attacked by this ledger before the later Wave 2 and Wave 3 integrations.

Current source truth is the TeX source plus the later swarm log and
claim-strength ledger. The converged local core is a theorem-lane index
with a short summary corollary, a separated PBW/CE-PV/Matlis dictionary,
de Rham-current brane-line factorization sourced by
`u_{a(t)dt\otimes f}`, a reduced principal-part current model, and
conditional or open status for QME, regulator-independence, descendant,
Rees/Fourier, all-order Costello, and cross-volume claims. Old formulas
and line anchors quoted below are historical attack evidence unless a
later ledger entry or current source scan explicitly marks them live.

## Verdict

The first reconstitution pass materially strengthened the manuscript: it added a
status ledger, local dictionary, three-principle front matter, theorem lanes,
and open obligations; it demoted the old six-part main theorem into a summary
package; it corrected the factorization-current source convention; it separated
principal parts from polynomial descendants in the most visible places; and the
paper builds.

The work is not complete.  The strongest surviving problem is architectural:
the paper still carries old global ambition, umbrella-theorem habits, and
proof-by-forward-reference inside the new frame.  Supremum discipline requires
the manuscript to become harder, not merely better labeled: every theorem lane
must either have a standalone proof in its own local hypotheses or be explicitly
renamed as an index to a later proof; every physical principle must be separated
from the theorem that realizes it; every universal or canonical word must be
earned by a uniqueness theorem or cut.

## Severity scale

- P0: publication-blocking mathematical or structural fault.
- P1: serious rigor or claim-status fault; must be repaired before release.
- P2: expository, notation, or reader-trust fault that weakens the paper.
- P3: cleanup that prevents later drift.

## Historical scan anchors for the first repair pass

These are the first anchors to repair before broader prose work:

- `main.tex:12`: stale `\date{2018}`.
- `main.tex:82`, `main.tex:150`, `main.tex:584`: uniqueness and
  precision language before the corresponding uniqueness hypotheses are
  isolated.
- `main.tex:466`: stable bulk--boundary Koszul-duality conjecture appears
  before the local theorem is fully firewalled.
- `main.tex:1005-1027`: concrete dictionary maps
  `E_{k,l}\mapsto\Psi_{k,l}` close to closed-side dual notation, preserving a
  route back to the forbidden descendant/principal-part identification.
- `main.tex:1114`: the old theorem package survives as
  `Local Hamiltonian closed-open theorem package`.
- `claim-strength-ledger.tex:60-62`: weighted Tate row is stronger than the
  regulator-independence/QME obligations.
- `tate-P3-universality.tex:11`, `tate-P3-universality.tex:94`,
  `tate-P3-universality.tex:189`, `tate-P3-universality.tex:216-224`:
  universality and Dirac-thesis language remains too strong for an outlook.
- `tate-T1-weighted-completion.tex:418-458`: weighted cotangent-lift theorem
  mixes internal weighted statements with conditional QME language.
- `out/main.toc:4-63`: main sections render as `0.x`; the cross-volume
  appendix renders as `.1`, both of which look like draft counter drift.

## P0 attacks

### P0.1 The old umbrella theorem survives under a new name

Anchors:
- `main.tex` around the `\label{thm:main-local}` summary package.
- `theorem-lanes.tex`, which now precedes it but does not eliminate it.

Attack:
The architectural diagnosis was that the original six-part theorem made proved
algebra, reduced models, conditional analytic claims, and open quantum problems
hostage to one statement.  The current paper has improved the status language,
but the summary package still reproduces the old large multi-part structure as
a corollary-like theorem.  A hostile reader can still attack the package rather
than the individual lanes.

Required repair:
Replace the large summary package by a short "Main local theorem package"
corollary of at most one page.  It should contain only:

1. a sentence naming the six standalone theorems,
2. the reduced closed-open consequence common to them,
3. a pointer to the status ledger for hypotheses and open obligations.

Move all substantive statements and proofs into the individual theorem lanes.

Stronger surviving form:
The main claim becomes not weaker but less vulnerable: a finite family of
independently checkable local theorems, plus a derived-center corollary.

### P0.2 The theorem lanes are not yet theorem-grade independent

Anchors:
- `theorem-lanes.tex`.
- Proofs that say "This is Theorem ..." and forward-reference later text.

Attack:
The theorem lanes state the desired architecture, but several proofs are still
index proofs rather than mathematical proofs.  That is acceptable for a roadmap
section, not for theorem lanes carrying the paper's claim strength.

Required repair:
Choose one of two honest forms:

1. Rename the file and section to "Theorem-lane index" and explicitly say the
   section is a navigational table of proved statements.
2. Upgrade every lane to a standalone theorem with hypotheses, definitions,
   proof, and exact dependence on later lemmas.

Supremum discipline selects option 2 unless length makes it unreadable, in which
case the index must be non-theorem text and the real theorem statements must
live where the proofs live.

Stronger surviving form:
The six-lane architecture survives.  What dies is theorem inflation without
local proof ownership.

### P0.3 The polynomial-descendant and principal-part dictionaries still touch

Anchors:
- `main.tex` around the concrete closed-open dictionary following
  `\label{conj:ks-bulk-boundary}`.
- Lines containing `E_{k,\ell}\mapsto \Psi_{k,\ell}` and identification of
  `\mathfrak h^\vee` with descendant labels.
- `local-dictionary.tex`.

Attack:
The manuscript now says in many places that `\Psi_{a,b}` and `\rho_{a,b}` are
different realizations, not the same module.  But the introduction still places
the stable trace dictionary and the cotangent/principal-part dictionary close
enough that a reader can reconstruct the forbidden idea: closed cotangent basis
equals polynomial descendant basis.  That is exactly the no-go theorem's target.

Required repair:
Split the dictionary into three disjoint blocks:

1. PBW special-fibre open trace labels:
   `H_{a,b}` and `\Psi_{a,b}`.
2. Closed Hamiltonian CE/PV labels:
   `c^I` and `u_I`.
3. Defect-local cotangent current labels:
   `\rho_{a,b}` as reduced Matlis dual / local cohomology basis.

State explicitly that the map from (1) to (3) is not an
`\mathfrak h`-module isomorphism and that any Rees/Fourier
`D_\hbar` interpolation is a separate conjectural analytic theorem.

Stronger surviving form:
The label-set coincidence survives as an organizing mnemonic.  The false module
identification dies.

### P0.4 "Forced", "unique", and "canonical" are used before uniqueness is proved

Anchors:
- `principles.tex` statements that the local model is "forced".
- `main.tex` early sections using "unique first-order action",
  "unique covariant choice", "factorisation-algebra structure is forced",
  and "closed observables are precisely".

Attack:
First-principles exposition is not a license to overstate.  A physical
principle can motivate a structure; only a theorem with hypotheses proves
uniqueness.  The current language sometimes blurs that line.

Required repair:
For every use of "forced", "unique", "canonical", and "precisely", classify it:

1. proved uniqueness up to a named normalization,
2. naturality under a named class of allowed transformations,
3. physical selection principle,
4. convention.

Only class (1) may keep "unique".  Class (2) may keep "canonical" only with the
qualifier.  Classes (3) and (4) must be rewritten.

Stronger surviving form:
The Dirac-Witten-Grothendieck principles survive as selection principles.  The
paper gains actual uniqueness theorems where it wants inevitability.

### P0.5 The introduction still places the stable Koszul-duality conjecture too early

Anchors:
- `main.tex`, the `Stable bulk--boundary Koszul duality` conjecture.

Attack:
The conjecture is important, but in the current flow it appears before the
reader has a clean proof-status separation.  It contaminates the local theorem
with the global ambition the reconstitution was designed to firewall.

Required repair:
Move the stable bulk-boundary Koszul-duality conjecture after the local theorem
package and after the proof-status ledger has done its work, or restate it in
the introduction as a one-paragraph motivation with no theorem environment.

Stronger surviving form:
The conjecture survives as the strategic horizon.  It stops underwriting the
proved local theorem.

## P1 attacks

### P1.1 The abstract is still too compressed to carry proof status cleanly

Anchors:
- `abstract.tex`.

Attack:
The rewritten abstract is stronger than the old one, but it still asks a short
space to carry physics principles, theorem statements, factorization, Moyal,
principal parts, and open obligations.  The result risks sounding like a stack
of solved problems.

Required repair:
Make the abstract two paragraphs only:

1. Physical selection problem and local model.
2. Exact theorem-status inventory: proved local CE/PV, proved principal-part
   module, proved reduced Moyal degree-zero sector, conditional graph/QME and
   unreduced cotangent lifts.

No "full", "universal", "complete", or "precisely" unless the sentence gives
the local hypotheses.

Stronger surviving form:
The abstract becomes harder to misread and more defensible to referees.

### P1.2 The status ledger has a few entries stronger than the proofs support

Anchors:
- `claim-strength-ledger.tex`.

Attack:
The ledger is a good idea, but a ledger must be more conservative than the
body, not more ambitious.  Entries such as weighted Tate regulator and
all-order reduced quantum statements need sharper internal/external boundaries.

Required repair:
Rewrite each status into one of:

- proved in the finite algebraic model,
- proved in the weighted Tate coefficient model,
- proved degreewise stable,
- computed to stated order,
- conditional on named QME/radial-parts/regulator-independence theorem,
- conjectural,
- not asserted.

Stronger surviving form:
The ledger becomes a referee weapon in our favor rather than a new attack
surface.

### P1.3 The weighted Tate material risks being mistaken for regulator independence

Anchors:
- `tate-T1-weighted-completion.tex`.
- `claim-strength-ledger.tex` weighted Tate row.
- `open-obligations.tex` regulator-independence obligation.

Attack:
The weighted completion is a useful analytic regulator and coefficient
replacement.  It is not, by itself, a theorem that the original unweighted
closed-open theory is regulator independent.

Required repair:
Every weighted Tate theorem must declare whether it is:

1. internal to the weighted category,
2. an approximation statement at finite scale,
3. a conjectural regulator-independent statement,
4. a conditional statement assuming QME and convergence.

Stronger surviving form:
Weighted Tate survives as a serious regulated model, not as hidden analytic
wishful thinking.

### P1.4 The degree-zero Moyal theorem needs a standalone proof spine

Anchors:
- `main.tex` around the reduced Moyal theorem and radial-parts discussion.
- `scripts/check_moyal_coefficients.py`.

Attack:
The script check is useful evidence, but the paper cannot rest an all-order
degree-zero theorem on a computational sanity check plus prose.  The Capelli
normalization, radial-parts identity, and scalar class quotient must be stated
as a closed algebraic proof.

Required repair:
Add an appendix or subsection with:

1. the Weyl algebra and trace-normalization conventions,
2. the finite-`N` radial-parts identity,
3. the stable limit,
4. the scalar `U(1)` quotient,
5. the exact relation to the script ranges checked.

Stronger surviving form:
The Moyal result becomes a theorem with computational verification as a
secondary independent check.

### P1.5 Costello graph and QME language still invites all-order interpretation

Anchors:
- `main.tex` quantum sections.
- `tate-T1-weighted-completion.tex`.
- `open-obligations.tex`.

Attack:
Matching low-order graph computations is not the same as an all-order Costello
renormalization theorem.  Any language that reads as "the graph realization is
done" is too strong unless the QME and counterterm recursion are proved.

Required repair:
Every graph statement must specify:

- graph order,
- propagator normalization,
- counterterm assumptions,
- whether it is a computation, theorem, or conjectural extension.

Stronger surviving form:
The first- and third-order computations become load-bearing evidence instead of
being overburdened by an all-order claim.

### P1.6 Twisted-M "universality" remains an overclaim even inside an outlook

Anchors:
- `tate-P3-universality.tex`, title and statements containing
  "universality" or "universal generality".

Attack:
The reconstitution moved this material behind a firewall, but the word
"universality" still overstates the relationship between a local protected
sector model and twisted M-theory.

Required repair:
Retitle and rewrite as "Admissible protected-sector reduction" or "Protected
twisted-M motivation".  Replace universal statements by conditional reductions:
if a protected sector satisfies hypotheses H1-Hn, then the local Dirac-Witten
theorem applies to that sector.

Stronger surviving form:
The physical motivation survives without becoming a false global theorem.

### P1.7 Cross-volume appendix remains too large for a local theorem paper

Anchors:
- `tate-P5-cross-volume.tex`.

Attack:
Although now firewalled, the cross-volume appendix still names too many remote
programs and transfer profiles.  Its mere size tells a referee the paper is
still trying to export local results into Vol III / BKM / Igusa territory.

Required repair:
Compress to a one- or two-page convention firewall, or move the detailed file
out of the manuscript into an internal note.  The main paper should only say:
no compact CY3, no BKM, no Igusa, no Vol III consequence is asserted here.

Stronger surviving form:
Cross-volume awareness survives as a boundary condition.  Cross-volume ambition
leaves the local theorem.

### P1.8 The principal-part theorem needs the Matlis/local-cohomology proof to be central

Anchors:
- `main.tex` principal-part sections.
- `theorem-lanes.tex` principal-part lane.
- `local-dictionary.tex`.

Attack:
The principal-part replacement is one of the most important repairs.  It cannot
be just a corrected dictionary.  The paper must prove that the reduced Matlis
dual is the right continuous dual and that no polynomial descendant model
realizes the coadjoint module.

Required repair:
Promote the proof to a central theorem block:

- define the topology on `\mathfrak h`,
- identify the continuous dual,
- compute the residue action,
- prove the local-cohomology uniqueness,
- prove the no-go theorem for polynomial descendants.

Stronger surviving form:
The no-go theorem becomes a positive structural theorem, not merely a caution.

### P1.9 Factorization-current conventions need a density/sign audit

Anchors:
- `theorem-lanes.tex` factorization-current lane.
- `main.tex` interval factorization sections.

Attack:
The source correction from `(a\otimes f)^\vee[-1]` to `u_{a\otimes f}` is
necessary, but not sufficient.  The interval-current construction involves
compactly supported de Rham forms, currents, shifts, pairings, and signs.  A
wrong density or degree convention would recreate the old source mismatch in a
more subtle form.

Required repair:
Add a convention box:

- `\mathfrak h_I = \Omega^\bullet_c(I)\otimes\mathfrak h`,
- precise continuous dual/current object,
- degree of `u_{a(t)dt\otimes f}`,
- pairing normalization,
- source of the `B_f(a)` operation,
- sign under interval orientation reversal.

Stronger surviving form:
The factorization equivalence survives with a checkable current-level source.

### P1.10 Section numbering visibly starts at `0.x` and appendix numbering as `.1`

Anchors:
- rendered table of contents and section numbers after the reconstitution.
- `out/main.toc:4-63`.

Attack:
The new paper currently displays sections like `0.1`.  This looks like a draft
artifact and undermines reader trust before the mathematics begins.  The
cross-volume appendix then renders as `.1`, which is even more visibly broken.

Required repair:
Fix the document class/counter setup so the main paper sections are numbered
`1`, `2`, `3`, ... and appendices are numbered `A`, `B`, ...; or explicitly
introduce a numbered Part/Chapter structure.

Stronger surviving form:
The document stops looking like a stitched appendix and reads as a finished
paper.

### P1.11 The manuscript date is stale

Anchors:
- `main.tex`, `\date{2018}`.

Attack:
A rebuilt 2026 local theorem with 2018 date signals uncontrolled provenance.

Required repair:
Either remove the date or set a current manuscript date appropriate to the
research record.

Stronger surviving form:
The document metadata matches the actual reconstitution.

## P2 attacks

### P2.1 The local dictionary is useful but not exhaustive enough

Anchors:
- `local-dictionary.tex`.

Attack:
The dictionary lists central symbols, but the paper still has several nearby
objects whose distinctions matter:

- `\mathfrak h = \mathbb C[z_1,z_2]/\mathbb C` versus formal completions,
- `A`, `\bar A`, and maximal ideals,
- polynomial labels versus principal-part labels,
- scalar quotient versus `U(1)` anomaly line,
- shifted duals versus de Rham-current duals.

Required repair:
Expand the dictionary into a full notation table and make it the canonical
source for scalar quotients, completions, topologies, and shifts.

Stronger surviving form:
Notation becomes a proof device rather than a reader aid.

### P2.2 The open obligations section is not yet complete

Anchors:
- `open-obligations.tex`.

Attack:
The current open obligations are good, but they omit several obligations the
attack has exposed:

- theorem-lane standalone proof upgrade,
- sign and convention appendix,
- Matlis/local-cohomology proof centralization,
- radial-parts proof appendix,
- rendered PDF/table/figure quality assurance,
- notation and macro hygiene,
- primary-source anchoring.

Required repair:
Add these as named obligations, each with exact non-goals.

Stronger surviving form:
The paper controls its frontier instead of merely listing the famous open
problems.

### P2.3 The proof-status language should be mechanically searchable

Anchors:
- `abstract.tex`, `claim-strength-ledger.tex`, theorem statements, outlook.

Attack:
The paper uses many status words: proved, computed, conditional, expected,
conjectural, open, heuristic, not asserted.  If they are not standardized, drift
will return.

Required repair:
Define a small status vocabulary and use only those terms in theorem boxes and
the ledger.  Add a final grep checklist before release.

Stronger surviving form:
Claim strength becomes auditable.

### P2.4 Macro and notation support files contain stale TODO and informal text

Anchors:
- `commands.tex`.
- `notation.tex`.
- `mathmacros.tex`.
- `nomenclature.tex`.

Attack:
Even if some support files are not rendered, the repository is part of the
research artifact.  Stale TODOs, duplicated macro definitions, and informal
phrases such as "blah" or "everyone's favourite" are hostile-review liabilities.

Required repair:
Audit rendered and unrendered support files.  Remove informal text, delete dead
notation, deduplicate macros, and keep only publication-grade definitions.

Stronger surviving form:
The repository becomes as disciplined as the PDF.

### P2.5 Figure/proof alignment has not been reaudited after the rewrite

Anchors:
- first- and third-order figure sources.
- quantum correction prose.

Attack:
The build passes, but a PDF build is not a mathematical check that figures,
graph labels, signs, and prose still agree.  A figure disagreement is usually a
computation disagreement.

Required repair:
Do a rendered PDF and source-figure audit:

- first-order figure label equals formula label,
- third-order graph labels equal coefficients,
- captions state computed order and hypothesis,
- no figure is used as evidence for an all-order claim.

Stronger surviving form:
Figures become verified computations, not decoration.

### P2.6 The title is strong but should not outpace the local hypotheses

Anchors:
- `main.tex` title.

Attack:
"Closed Hamiltonian BF Theory as the Derived Poisson Center of a Dirac Brane
Probe" is the right direction, but only if every occurrence of the title's
thesis is local, formal, reduced or qualified exactly as the theorem proves.

Required repair:
Ensure the subtitle and abstract say "formal local" and "reduced/local theorem"
clearly enough that the title is read in the correct scope.

Stronger surviving form:
The title stays ambitious while the subtitle carries the hypotheses.

### P2.7 The manuscript still mixes proof order and motivation order

Anchors:
- `principles.tex`.
- `main.tex` introduction.
- `theorem-lanes.tex`.

Attack:
A physics-first opening is valuable, but if theorem statements precede all
definitions and proof objects, the reader cannot verify them locally.

Required repair:
After the principles, insert a compact "objects and hypotheses" section before
major theorem statements, or make each theorem lane carry its own definitions.

Stronger surviving form:
The paper keeps the Dirac voice while becoming easier to check line by line.

### P2.8 Primary-source anchoring is not systematic enough

Anchors:
- all claims invoking Witten centrality, Costello graph/QME methods, BCOV,
  Loday-Quillen-Tsygan, Procesi-Razmyslov, Matlis duality, and radial parts.

Attack:
The paper cannot rely on folklore names for load-bearing comparisons.  Every
borrowed theorem must be cited with enough precision for the reader to inspect
the exact convention transfer.

Required repair:
Add a citation ledger:

- source theorem,
- local convention translation,
- what is used,
- what is not used.

Stronger surviving form:
External literature becomes scaffolding, not authority by name.

## P3 attacks

### P3.1 Internal reconstitution files should distinguish architecture from manuscript

Anchors:
- `reconstitution/architecture.md`.
- this ledger.

Attack:
The internal files are useful, but they should never leak process language into
the paper.  The manuscript must not mention phases, rewrites, previous drafts,
or critique documents.

Required repair:
Keep all process artifacts in `reconstitution/` and ensure no process phrasing
appears in rendered TeX.

Stronger surviving form:
The repo retains the audit trail while the paper remains standalone.

### P3.2 Build success is necessary but not sufficient

Anchors:
- `make pdf` result.
- rendered `out/main.pdf`.

Attack:
A successful LaTeX build does not prove tables fit, front matter reads well,
or new sections are visually acceptable.

Required repair:
After the next inscription pass, render-inspect at least:

- title and abstract pages,
- status ledger,
- local dictionary,
- three principles,
- theorem lanes,
- open obligations.

Stronger surviving form:
The front matter becomes publication-grade, not merely compilable.

### P3.3 The critique source should be archived with provenance

Anchors:
- `materials/raw/2026-04-28-whitepaper-critical-analysis.pdf`.
- `materials/processed/2026-04-28-whitepaper-critical-analysis.txt`.

Attack:
The critique is now part of the research process.  If retained in repo, it
needs provenance and a statement that it is not part of the paper's claims.

Required repair:
Add a short materials README or provenance note if these files remain tracked.

Stronger surviving form:
The research archive is reproducible without confusing critique material with
manuscript evidence.

## Cross-cutting repair program

The next inscription pass should proceed in this order:

1. Fix visible document integrity: section numbering, date, and front-matter
   table rendering.
2. Collapse the old summary package into a short corollary and move all
   substance into standalone theorem blocks.
3. Split the PBW, CE/PV, and principal-part dictionaries so the no-go theorem
   is structurally impossible to misread.
4. Rewrite all "forced", "unique", "canonical", and "precisely" language using
   a proof-status vocabulary.
5. Demote the stable Koszul-duality conjecture from early theorem environment
   to motivation or move it after the local theorem.
6. Retitle and demote twisted-M universality to protected-sector motivation.
7. Compress or externalize the cross-volume appendix.
8. Promote Matlis/local-cohomology, factorization-current conventions, and
   radial-parts/Capelli normalization to standalone proof appendices.
9. Expand open obligations to include every remaining proof and convention
   gap.
10. Audit macros, notation, figures, citations, and rendered PDF pages.

## What survives

The strongest form that survives the attack is:

- a formal local Dirac brane probe theorem,
- a stable PBW special-fibre trace theorem,
- a CE/PV derived Poisson center theorem,
- a reduced Matlis-dual principal-part cotangent theorem,
- a de Rham-current interval factorization theorem,
- a degree-zero Weyl/Moyal theorem with a proved radial-parts spine,
- a scalar anomaly line with exact quotient conventions,
- a weighted Tate regulator treated as a regulated coefficient model,
- a protected-sector physical motivation, not a universal M-theory theorem,
- an explicit firewall against CY3, BKM, Igusa, and Vol III consequences.

Everything else must either be proved in its own hypotheses, marked as an open
obligation, or moved out of the manuscript.
