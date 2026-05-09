# Whitepaper Reconstitution Architecture

Internal execution architecture for reconstituting the local mixed
holomorphic-topological whitepaper from first principles.

This document is not manuscript prose. It records the proof-engineering
contract that governed the rewrite of `abstract.tex`, `main.tex`, and
the Tate residual files. It records what had to be proved, separated,
demoted to a problem, or removed from the local theorem.

## Current Status Preamble

Status as of the Wave 4 ledger-healing pass on 2026-04-28: this file is
the initial reconstitution architecture, not a current manuscript
diagnosis. Exact `main.tex:<line>` and `abstract.tex:<line>` anchors
below are historical attack anchors from the first architecture pass.
Phrases such as "currently", "still", "must", and "required changes"
record the obligations visible at that pass; they do not override the
later Wave 2 and Wave 3 convergence record or the current TeX source.

The current converged architecture is the stable local core: the theorem
lanes are an index with proof owners; `thm:main-local` is a summary
corollary; the CE/PV source convention is
`c^I -> \theta^I`, `u_I -> O_I`; brane-line factorization uses the de
Rham-current interval source and the shifted-cotangent coordinate
`u_{a(t)dt\otimes f}`; cotangent directions are Matlis
principal-part currents, not polynomial one-psi descendants; weighted
Tate, Costello graph/QME, regulator-independence, Rees/Fourier,
descendant, and cross-volume assertions remain conditional, open,
conjectural, or not asserted according to the claim-strength ledger.
Historical formulas quoted below are attack strings unless the current
source and ledger status explicitly reaffirm them.

## 1. Supremum Contract

The rewrite follows one rule: take the mathematically higher road even
when it is longer.

Consequences:

- No statement survives because it is rhetorically useful.
- No theorem is weakened silently. A false strong sentence is repaired
  into a true stronger theorem, split into exact true components, or
  fenced as a problem with its obstruction named.
- Every load-bearing identity gets at least two independent checks when
  possible: direct coordinate computation, conceptual proof, script,
  primary-source theorem, or compatibility with the field theory.
- Every statement carries a proof status: proved, computed, conditional,
  conjectural, heuristic, or open.
- The local theorem does not borrow truth from the cross-volume horizon.
  Vol III, Igusa, and twisted-M-theory motivation may guide convention
  checks, but no consequence transfers without a matched proof.
- The paper is rebuilt around its unique survivor, not around the
  historical order in which the current draft accumulated repairs.

## 2. Historical Failure Surface (Initial Snapshot)

In that snapshot, the manuscript contained the correct core theorem but
mixed distinct layers in a way that let the weakest layer govern the
strongest. The rewrite had to separate the layers without lowering the
ambition.

Historical attack anchors:

- `main.tex:1099` states the umbrella theorem as six interlocking
  assertions.
- `main.tex:1110` still defines
  `\mathfrak h_I=C^\infty_c(I)\widehat\otimes\mathfrak h`.
- `main.tex:1181` and `main.tex:2210` still map
  `(a\otimes f)^\vee[-1]` to the boundary observable `B_f(a)`.
- `main.tex:2451` contains the CE-source obstruction: boundary
  Hamiltonian functions are images of the shifted-cotangent CE
  coordinates `u_I`, not of Hamiltonian CE coordinates `c^I`.
- `main.tex:2499` contains the correct cochain-level CE/PV theorem:
  `c^I -> \theta^I`, `u_I -> O_I`.
- `main.tex:3852` separates the open descendant action from the closed
  coadjoint action, but `main.tex:3871` still calls the two bases of one
  module.
- `main.tex:3956` gives the principal-part coadjoint module and its
  explicit lowering formula.
- `main.tex:4071` still frames residue uniqueness as Schur-type
  rigidity; the stronger foundation is Matlis/local-cohomology duality.
- `main.tex:4179` states PBW versus deformation interpolation, but
  `main.tex:4222` again collapses the two sides into one module.
- `main.tex:4257` and `main.tex:4290` prove the no-polynomial-realization
  obstruction; this must become a structural theorem, not a local caveat.
- `main.tex:4382` constructs the reduced principal-part current
  factorization algebra; `main.tex:4511` correctly states that this is
  reduced and not an unreduced BV/factorization construction.
- `tate-T5-chain-level-primitive.tex:353` extends the primitive
  projection by sending one-psi classes to principal parts. This is the
  remaining dangerous point: it should become a primitive
  indecomposable shadow, not an unreduced cotangent lift.
- `main.tex:5039` proves the reduced all-`N` Moyal commutator theorem.
  Its status depends on a fully explicit radial-parts proof, not on
  finite script checks alone.
- `main.tex:5427` correctly isolates the Hamiltonian specialization of
  Costello perturbative BV as an open graph/QME problem.
- `abstract.tex:39` through `abstract.tex:43` still says the Rees
  parameter interpolates the PBW descendants and principal parts.
- `abstract.tex:91` through `abstract.tex:95` imports cross-volume
  convention contracts into the abstract. This weakens the local theorem.

## 3. Unique Survivor

The unique survivor is the Dirac-Witten-Matlis local theorem.

The brane is a Dirac constrained matrix probe of the formal symplectic
disk. Closed Hamiltonian fields act on open observables as derived
Poisson-central operations. The cotangent closed modes are Matlis-dual
residue currents at the defect, not polynomial descendants. The
cochain-level identity

```tex
C^\bullet_{\mathrm{CE},\mathrm{cont}}
  (\mathfrak h\ltimes\mathfrak h^\vee_{\mathrm{cont}}[1])
  \cong
\mathrm{PV}(\widehat{\mathbf S}_{\mathrm{Tate}}(\mathfrak h))
```

is the spine. Everything else is a dependency, a shadow, a deformation,
or an open analytic realization problem.

The paper must therefore be organized around the following exact type
system.

## 4. Correct Type System

### 4.1 Hamiltonian functions

Object:

```tex
\mathfrak h=\mathbb C[[z_1,z_2]]/\mathbb C\cdot 1.
```

Role:

- infinitesimal canonical transformations of the formal symplectic disk;
- source of the open zero-psi Hamiltonian trace classes;
- Lie algebra in the CE/PV theorem.

Interval form:

```tex
\mathfrak h_I=\Omega^\bullet_c(I)\widehat\otimes\mathfrak h
```

whenever locally constant factorization, de Rham contraction, or
Costello-Gwilliam locality is being asserted. Plain `C^\infty_c(I)` may
only appear when the text explicitly restricts to degree-zero test
densities inside the de Rham cosheaf.

### 4.2 Shifted-cotangent CE coordinates

Object:

```tex
u_I \in
C^\bullet_{\mathrm{CE},\mathrm{cont}}
(\mathfrak h\ltimes\mathfrak h^\vee_{\mathrm{cont}}[1]).
```

Role:

- source of boundary Hamiltonian functions under the CE/PV map;
- correct input for factorization-center length-one maps;
- Witten centrality made algebraic.

Invariant:

```tex
\Phi(c^I)=\theta^I,\qquad \Phi(u_I)=O_I.
```

Therefore the factorization-current source must be written in the
`u`-coordinate, not as `(a\otimes f)^\vee[-1]` unless that notation has
first been explicitly identified with the shifted-cotangent coordinate.

### 4.3 Principal-part cotangent currents

Object:

```tex
\mathcal P=\operatorname{Ann}(1)\subset
H^2_{\mathfrak m}(\mathbb C[z_1,z_2])\,dz_1dz_2
=
\bigoplus_{a+b>0}\mathbb C\,\rho_{a,b},
\qquad
\rho_{a,b}=z_1^{-a-1}z_2^{-b-1}dz_1dz_2.
```

Role:

- reduced Matlis dual of `\mathfrak h`;
- deformation-compatible coadjoint module;
- defect-local cotangent current sector.

Action:

```tex
z_1^p z_2^q\cdot\rho_{a,b}
=-(pb-qa+p-q)\rho_{a-p+1,b-q+1}.
```

Proof routes to inscribe:

- residue integration by parts;
- Matlis/local-cohomology duality;
- direct monomial computation;
- script check as reproducibility, not proof.

### 4.4 PBW one-psi descendants

Object:

```tex
\Psi_{a,b}
```

Role:

- stable primitive one-psi Koszul classes in the open model;
- PBW special-fibre representatives;
- open shadow of the cotangent label set.

They are not a polynomial realization of `\mathcal P`.

Invariant:

```tex
\Psi_{a,b}\not\cong_{\mathfrak h}\rho_{a,b}.
```

The strongest true statement is:

> The PBW one-psi classes and the principal-part currents carry the same
> index set and pair through the stable primitive quotient, but they
> carry different `\mathfrak h`-actions. A Rees/Fourier `D_\hbar` bridge
> between them is a separate theorem, not part of the present local
> theorem.

### 4.5 Reduced principal-part boundary model

Object:

```tex
A_\partial^{\mathrm{pp}}(I)
=
\widehat{\mathbf S}(\mathfrak h_I)
\widehat\otimes
\widehat{\mathbf S}(\mathcal P_I[1]).
```

Role:

- reduced post-de Rham defect-current model;
- algebraic recipient of the principal-part coadjoint action;
- not an unreduced BV observable algebra unless an unreduced chain model
  and centrality homotopies are constructed.

Invariant:

The phrase "open observable algebra" must not be used for this object
without the adjective "reduced" and the defect-current qualifier.

## 5. Theorem Lanes

The umbrella theorem must be replaced by theorem lanes. The lanes are
not equal in status. The CE/PV theorem is central; the others are
dependencies, consequences, shadows, or open analytic lifts.

### Lane A. Dirac Brane Probe

Statement:

```tex
S_\partial
=
\int_\mathbb R \mathrm{Tr}(\phi_1\,d\phi_2+A[\phi_1,\phi_2]),
\qquad
Q\psi=[\phi_1,\phi_2].
```

Status:

proved in the local mechanical model.

Proof obligations:

- derive the symplectic potential from the formal normal disk;
- show conjugation invariance gives the first-class constraint;
- identify the Koszul/BV variable and its degree;
- compute the induced equal-time bracket.

Hostile attacks:

- wrong BV degree for `\psi`;
- missing scalar mode;
- confusing gauge multiplier with physical cotangent mode;
- claiming a global brane theory where only a local probe model is built.

### Lane B. Stable Hamiltonian Trace and One-Psi Shadow

Statement:

The stable connected open sector is the PBW special-fibre Hamiltonian
trace sector, with one-psi primitive Koszul classes as open descendants.

Status:

proved degreewise stable, subject to the existing Procesi-Razmyslov and
one-psi homology computations.

Proof obligations:

- keep the zero-psi trace sector separate from the one-psi sector;
- state the stable range;
- cite the script check as reproducibility for bounded cases;
- isolate the exact algebraic proof from the finite computation.

Hostile attacks:

- finite-`N` trace identities outside stable range;
- descendant classes smuggled into the coadjoint module;
- multi-trace products mistaken for primitive generators.

### Lane C. CE/PV Derived Center

Statement:

```tex
C^\bullet_{\mathrm{CE},\mathrm{cont}}
(\mathfrak h\ltimes\mathfrak h^\vee_{\mathrm{cont}}[1])
\cong
\mathrm{PV}(\widehat{\mathbf S}_{\mathrm{Tate}}(\mathfrak h))
\simeq
Z^{P_0}_{\mathrm{fact}}
(\widehat{\mathbf S}_{\mathrm{Tate}}(\mathfrak h)).
```

Generator dictionary:

```tex
c^I\mapsto\theta^I,\qquad u_I\mapsto O_I.
```

Status:

proved at cochain level by direct generator computation. The
conilpotent bar-cobar theorem is a conceptual template under its own
hypotheses, not a substitute for the generator calculation in the full
Hamiltonian algebra.

Proof obligations:

- direct CE differential versus Schouten differential check;
- coordinate-free shifted-cotangent explanation;
- continuity/completion statement in the Tate category;
- separate lower-central conilpotence hypotheses from the formal
  Hamiltonian algebra itself.

Hostile attacks:

- source coordinate error `c^I` versus `u_I`;
- treating a function as a closed CE one-cochain;
- importing bar-cobar conilpotence beyond its hypotheses.

### Lane D. Matlis Principal-Part Cotangent

Statement:

```tex
\mathfrak h^\vee_{\mathrm{cont}}
\cong
\operatorname{Ann}(1)\subset
H^2_{\mathfrak m}(\mathbb C[z_1,z_2])\,dz_1dz_2.
```

Status:

proved after replacing Schur rigidity by Matlis/local-cohomology
duality and the explicit residue computation.

Proof obligations:

- define the topology on `\mathfrak h`;
- compute the continuous dual of the reduced formal power series ring;
- identify it with the reduced top local cohomology residue module;
- derive the lowering action;
- prove uniqueness as Matlis duality, not as an informal Schur lemma.

Hostile attacks:

- including `\rho_{0,0}` after quotienting constants;
- sign error in the lowering formula;
- treating the module as polynomial;
- topological dual taken in the wrong category.

### Lane E. Factorization-Current Theorem

Statement:

On intervals,

```tex
\mathfrak h_I=\Omega^\bullet_c(I)\widehat\otimes\mathfrak h,
\qquad
\mathfrak g_I=\mathfrak h_I\ltimes\mathcal P_I[1],
```

and the length-one central operation is sourced by the shifted cotangent
coordinate:

```tex
u_{a(t)dt\otimes f}\longmapsto B_f(a).
```

Status:

proved after source and de Rham-current correction.

Proof obligations:

- de Rham cosheaf and extension-by-zero maps;
- equal-time delta bracket;
- support locality on disjoint intervals;
- compatibility between factorization products and CE coproducts;
- precise relation between degree-zero test functions and de Rham
  densities.

Hostile attacks:

- writing `C^\infty_c` where a de Rham cosheaf is required;
- mapping Hamiltonian CE coordinates rather than cotangent CE
  coordinates;
- declaring local constancy without the de Rham contraction.

### Lane F. Primitive Indecomposable Shadow

Statement:

The chain-level primitive projection is a strict projection to the
indecomposable `P_0` shadow of the stable boundary algebra. It does not
by itself construct an unreduced cotangent closed-open factorization
center.

Status:

proved for the primitive Hamiltonian shadow and one-psi indecomposable
shadow; unreduced cotangent centrality remains conditional unless the
missing homotopies are constructed.

Required rewrite:

- rename the theorem lane away from "unreduced lift";
- replace strict `\Psi -> \rho` language by a shadow-pairing statement;
- remove any conclusion that the chain-level projection closes the full
  unreduced cotangent factor.

Hostile attacks:

- conflating primitive quotient with factorization center;
- treating a cumulant projection as a morphism of full observable
  algebras;
- using the no-polynomial theorem and then immediately violating it.

### Lane G. Scalar U(1) Anomaly

Statement:

The scalar Hamiltonian/center-of-mass mode gives a distinguished anomaly
line represented classically by the Poisson cocycle and quantumly by the
Capelli shift.

Status:

proved as a distinguished line modulo the scalar class, not as an
unqualified spanning theorem unless the cohomology calculation is
included.

Proof obligations:

- state the exact Lie algebra cohomology group being used;
- compute the cocycle;
- compare with the Capelli normal-ordering shift;
- state precisely what quotient removes the scalar.

Hostile attacks:

- "spans" without computing the whole cohomology group;
- mixing the classical scalar cocycle with the quantum Capelli contact
  term without a basis-change statement.

### Lane H. Weyl/Moyal Degree-Zero Quantum Theorem

Statement:

The Capelli/Weyl-renormalized stable trace realizes the Moyal bracket in
degree zero.

Status:

proved if the radial-parts theorem is fully inscribed and cited at the
level claimed; otherwise conditional. Script checks are reproducibility
anchors, not the all-`N` proof.

Proof obligations:

- define `J_N(f)` and the quantum moment-map ideal;
- prove or cite the Harish-Chandra radial-parts identity with the
  Vandermonde conjugation convention;
- show the defect lies in the moment-map ideal;
- prove connected projection absorbs Capelli triangular terms;
- separate degree-zero Hamiltonian quantum closure from descendant and
  Costello graph lifts.

Hostile attacks:

- finite checks used as proof of an infinite theorem;
- scalar `\hbar N` term treated as extra anomaly instead of basis
  change;
- descendant sector upgraded without a continuous-dual boundary model.

### Lane I. Weighted Tate Regulator and Costello Graph Problem

Statement:

Weighted Tate completion supplies a regulator and coefficient kernel for
graphwise control. It is not the original unweighted cotangent theory
unless regulator independence is proved.

Status:

conditional/open in the unreduced brane-defect QME direction.

Proof obligations:

- state the weighted coefficient category;
- prove formal Casimir convergence in that category;
- identify which BV propagator data become available;
- state regulator independence as a conjecture or theorem with proof;
- keep Costello graph realization as an open specialization problem
  until the obstruction class is killed.

Hostile attacks:

- changing coefficient category while claiming to prove the original
  theory;
- using operator-level heat homotopy as a BV kernel;
- claiming Costello-Li flat BCOV/HCS covers this mixed ordinary
  `\mathfrak{gl}_N` defect without a reduction theorem.

## 6. Manuscript Architecture

The reconstructed manuscript should have the following mathematical
shape.

### Abstract

Two paragraphs plus a compact claim ledger.

Paragraph one:

- Dirac constrained probe;
- Witten centrality;
- Matlis/Grothendieck residue currents.

Paragraph two:

- CE/PV theorem;
- principal-part coadjoint theorem;
- factorization-current theorem after de Rham/source correction;
- degree-zero Moyal theorem with exact status;
- scalar anomaly line;
- explicit open problems.

Delete from the abstract:

- `\Psi`/`\rho` Rees interpolation as if already theorem;
- cross-volume convention contracts;
- any assertion that the primitive projection closes the unreduced
  cotangent lift.

### Opening Principles

A short section before the current introduction.

Principle 1. Dirac constrained probe.

- start from the formal symplectic disk;
- derive the first-order action;
- identify the moment-map constraint and Koszul/BV variable.

Principle 2. Witten centrality.

- a closed insertion approaching the brane defines a central operation,
  not merely a boundary value;
- algebraic target is the derived `P_0` factorization center.

Principle 3. Grothendieck-Matlis cotangent currents.

- cotangent fields are residue currents supported at the defect;
- the polynomial descendant sector is only the PBW shadow.

Each principle must end with the theorem lane it forces.

### Main Theorem

Replace the umbrella theorem by a theorem-spine statement plus theorem
lane references.

The main theorem should assert only the proved local spine:

- Dirac brane probe;
- CE/PV derived center;
- Matlis principal-part cotangent;
- factorization-current theorem after source correction;
- stable PBW open shadow;
- degree-zero Moyal theorem if fully proven;
- scalar anomaly line.

It should explicitly exclude:

- unreduced cotangent factorization centrality;
- quantum descendant lift;
- Costello graph realization;
- cross-volume consequences.

### Body Sections

1. Dirac brane probe and open BV/Koszul model.
2. Closed Hamiltonian BF and shifted cotangent Lie algebra.
3. CE/PV derived center theorem.
4. Matlis principal parts and the no-polynomial theorem.
5. Stable open traces and primitive one-psi PBW shadow.
6. Factorization on the brane line with de Rham currents.
7. Scalar anomaly and Capelli normalization.
8. Degree-zero Weyl/Moyal quantum theorem.
9. Weighted Tate regulator and analytic graph problem.
10. Boundary of the theorem: exact list of open problems.

### Appendices

Appendix A. Sign, degree, CE, Schouten, BV conventions.

Appendix B. Matlis duality and residue currents.

Appendix C. Reproducibility scripts and finite checks.

Appendix D. Harish-Chandra radial parts and Capelli-renormalized traces.

Appendix E. Notation index and overloaded-term glossary.

Appendix F. Cross-volume convention firewall, if retained at all. This
appendix must not read as a theorem or implication.

## 7. File-Level Execution Map

### `abstract.tex`

Rewrite completely after the theorem lanes are fixed.

Required changes:

- install the two-paragraph physical/mathematical abstract;
- add a claim-strength ledger;
- delete Rees interpolation as a proved `\Psi`/`\rho` module bridge;
- delete cross-volume contract language;
- state graph/QME and descendant lifts as open or conditional.

### `main.tex`

Required changes:

- insert the principles section before the current theorem statement;
- replace the umbrella theorem by theorem-spine plus lanes;
- change interval factorization objects to de Rham-current language;
- replace every factorization source map of the form
  `(a\otimes f)^\vee[-1] -> B_f(a)` by the shifted-cotangent source
  notation;
- move or compress cross-volume horizon material;
- reframe weighted Tate as regulator;
- keep Costello graph realization as open until the obstruction class is
  closed.

### `tate-T5-chain-level-primitive.tex`

Required changes:

- rename the cotangent extension as a primitive indecomposable shadow;
- remove the implication that one-psi classes are a polynomial
  realization of principal parts;
- state precisely what the cumulant projection proves;
- delete or demote the corollary closing the unreduced lift unless a
  separate unreduced centrality theorem is provided.

### `tate-T1-weighted-completion.tex`

Required changes:

- state weighted completion as regulator/coefficient replacement;
- add regulator-independence as an explicit theorem if proved, otherwise
  a conjecture or problem;
- prevent the weighted model from being read as the original unweighted
  cotangent theory.

### `tate-T2-nilpotent-truncation.tex`

Required changes:

- keep the obstruction calculation in the main narrative;
- move the full truncation computation to an appendix or retained
  technical subsection;
- state which Hamiltonians are removed by truncation.

### `tate-T3-quillen-equivalence.tex`

Required changes:

- keep as appendix-level categorical enhancement;
- in the main body, use only the strict cochain-level theorem unless the
  conilpotence hypotheses are met.

### `tate-P3-universality.tex`

Required changes:

- move out of the local theorem lane;
- retain only as physical origin or conditional admissibility statement;
- remove any implication that twisted M-theory proves the local theorem.

### `tate-P5-cross-volume.tex`

Required changes:

- remove from the shipping mathematical theorem unless explicitly needed
  as a convention firewall;
- if retained, rewrite as non-transferability guardrails only.

### `scripts/check_one_psi_homology.py`

Use as reproducibility evidence for:

- primitive one-psi homology;
- open Hamiltonian action;
- closed coadjoint Taylor-dual action;
- principal-part coadjoint action.

Do not cite finite checks as substitutes for proofs.

### `scripts/check_moyal_coefficients.py`

Use as reproducibility evidence for:

- Moyal odd-order coefficients;
- vanishing even terms in checked windows;
- rank-two radial checks;
- Capelli round-trip checks.

Do not cite finite checks as substitutes for the all-`N`
Harish-Chandra/radial-parts proof.

## 8. Execution Order

### Pass 1. Architecture and Claim Ledger

Deliverables:

- this architecture document;
- a manuscript-facing claim ledger;
- a map from every current umbrella assertion to a theorem lane or
  problem.

Exit condition:

Every load-bearing claim in the current abstract and umbrella theorem
has a target status.

### Pass 2. Type-System Correction Cascade

Deliverables:

- de Rham interval objects where factorization requires them;
- shifted-cotangent source maps in factorization statements;
- removal of `\Psi`/`\rho` same-module language;
- reduced principal-part model terminology.

Exit condition:

No occurrence remains where a Hamiltonian CE coordinate, PBW descendant,
or principal-part current is assigned the wrong type.

### Pass 3. Foundational Opening

Deliverables:

- principles section;
- theorem-spine statement;
- claim ledger in front matter;
- title/abstract rewrite after the technical corrections are in place.

Exit condition:

A cold reader can tell on the first pages which statements are proved,
which are conditional, and why the CE/PV theorem is the spine.

### Pass 4. Cotangent Hardening

Deliverables:

- Matlis/local-cohomology proof;
- no-polynomial theorem promoted and integrated;
- PBW shadow theorem;
- primitive-projection theorem rewritten to avoid false cotangent lift.

Exit condition:

The cotangent sector can no longer be attacked by the
`\Psi`/`\rho` module objection.

### Pass 5. Quantum Hardening

Deliverables:

- degree-zero Weyl/Moyal theorem stated with exact hypotheses;
- radial-parts proof either fully inscribed or status marked
  conditional;
- Capelli basis-change statement separated from scalar anomaly;
- descendant quantum lift fenced as a problem.

Exit condition:

The quantum theorem says exactly what is proved and no more.

### Pass 6. Analytic and Regulator Boundary

Deliverables:

- weighted Tate as regulator;
- unweighted Casimir obstruction preserved;
- Costello graph/QME problem stated with precise missing data;
- regulator-independence status made explicit.

Exit condition:

No reader can infer that weighted completion or imported Costello
formalism proves the unweighted brane-defect graph theorem.

### Pass 7. Horizon Quarantine

Deliverables:

- cross-volume material removed from theorem-bearing narrative;
- convention firewall retained only if useful;
- Vol III/Igusa/BKM/twisted-M claims marked non-transferable without
  matched proofs.

Exit condition:

The local theorem is self-contained and cannot export false consequences
to adjacent repositories.

### Pass 8. Verification

Deliverables:

- targeted `rg` scans for forbidden old claims;
- script runs for reproducibility anchors;
- `make pdf` after the manuscript changes stabilize;
- final theorem-lane audit.

Exit condition:

The PDF builds, old false patterns are absent, finite computation
anchors reproduce, and every theorem lane has the declared status.

## 9. Claim Ledger Template

Each claim inserted into the manuscript must be recorded in this form:

| Claim | Status | Proof route | File anchors | Attack surface | Resolution |
|---|---|---|---|---|---|
| Dirac probe action | proved | constrained mechanics + BV/Koszul computation | `main.tex` | BV degree, scalar mode | local theorem |
| CE/PV center | proved | generator computation + shifted cotangent formalism | `main.tex:2499` | `c`/`u` source swap | theorem spine |
| Principal parts | proved after hardening | residue + Matlis duality + monomial formula | `main.tex:3956` | Schur language, sign | theorem lane |
| Factorization current | proved after correction | de Rham cosheaf + equal-time bracket | `main.tex:2103` | `C^\infty_c`, wrong source | theorem lane |
| PBW one-psi shadow | proved as shadow | homology + stable trace | `tate-T5` | false cotangent realization | shadow theorem |
| Degree-zero Moyal | proved/conditional by radial proof status | radial parts + Capelli + script | `main.tex:5039` | finite checks overused | theorem/problem split |
| Costello graph lift | open | missing brane-defect QME obstruction | `main.tex:5427` | imported theorem overreach | problem |
| Cross-volume horizon | heuristic/convention | matched-proof requirement | `tate-P5` | false transfer | quarantine |

The ledger becomes manuscript-facing only after it is cleaned into
publication prose. This internal table is the working control surface.

## 10. Forbidden Old Patterns

Before declaring the rewrite complete, targeted scans must find no
unfenced occurrence of the following patterns:

```text
two different bases of the same \mathfrak g-module
interpolated by the Rees parameter
(a\otimes f)^\vee[-1]\longmapsto B_f(a)
C_c^\infty(I)\widehat\otimes\mathfrak h
unreduced lift required in part (d) is constructed
chain-level primitive projection closes the cotangent factor
cross-volume convention contracts
spans H^2_{\mathrm{Lie}}
```

Some strings may survive inside a historical diagnosis or internal
architecture file. They must not survive as theorem-bearing manuscript
claims.

## 11. Adversarial Audit

Every pass is attacked along these axes.

Type attack:

- Is the source a Hamiltonian CE coordinate, shifted-cotangent CE
  coordinate, PBW descendant, or Matlis current?
- Is the target a function, vector field, polyvector, central operation,
  reduced current, or full BV observable?

Degree attack:

- Are shifts `[1]`, `[-1]`, BV degrees, and CE degrees consistent?
- Does the `P_0` bracket have the declared degree?

Topology attack:

- Is the dual algebraic, continuous, Tate, weighted Tate, distributional,
  or de Rham?
- Is a completed tensor product being used where the Casimir does not
  converge?

Locality attack:

- Is the locality support locality, topological locality, or formal
  holomorphic locality?
- Is the brane-line object a cosheaf/factorization object or only a
  stalk object?

Quantum attack:

- Is the theorem degree-zero, descendant, all-order, all-`N`, stable
  large-`N`, or graph-theoretic?
- Is a finite script check being asked to prove an infinite theorem?

Cross-volume attack:

- Does any sentence imply a Vol III, Igusa, BKM, or compact CY
  consequence?
- If so, is the matched-conventions proof present?

## 12. Definition of Done

The reconstitution is complete when the manuscript satisfies all of the
following.

- The first pages derive the paper from Dirac constrained probes,
  Witten centrality, and Matlis residue currents.
- The CE/PV theorem is visibly the mathematical spine.
- The abstract and introduction expose claim status without apology or
  fog.
- Every interval factorization statement uses the correct de Rham or
  degree-zero specialization.
- The boundary observable `B_f(a)` is sourced by the shifted-cotangent CE
  coordinate.
- No statement identifies `\Psi_{a,b}` and `\rho_{a,b}` as the same
  `\mathfrak h`-module.
- The principal-part module is justified by Matlis/local cohomology and
  residue calculus.
- The primitive projection is a primitive indecomposable shadow, not an
  unreduced cotangent centrality theorem.
- The degree-zero Moyal theorem is either fully proved or exactly marked
  conditional.
- The weighted Tate construction is a regulator unless regulator
  independence is proved.
- Costello graph realization remains a named problem until the
  brane-defect QME obstruction is closed.
- Cross-volume material is quarantined from theorem-bearing local
  claims.
- The reproducibility scripts run and are cited only for what they
  verify.
- The final PDF builds.

## 13. Immediate Next Action

After this architecture lands, the next edit should be the type-system
correction cascade, not prose polishing.

Order:

1. Correct the factorization source maps.
2. Replace factorization `C^\infty_c` objects by de Rham-current objects
   where required.
3. Remove `\Psi`/`\rho` same-module language.
4. Rewrite the primitive-projection cotangent extension as a shadow
   statement.
5. Only then draft the new front matter.

This order prevents the foundational opening from legitimizing theorem
statements that still carry the old type errors.
