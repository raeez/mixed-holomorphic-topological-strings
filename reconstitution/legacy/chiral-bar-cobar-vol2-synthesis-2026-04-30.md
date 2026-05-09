# Chiral-Bar-Cobar Vol II Synthesis For Mixed HT Strings, 2026-04-30

This document absorbs the current contents of `~/chiral-bar-cobar-vol2`
into the topological-strings reconstitution programme.  It is not
manuscript prose.  It is a control document for proof construction.

Inputs:

- Active critique:
  `materials/raw/2026-04-30-mixed-holomorphic-topological-strings-critique.pdf`.
- Extracted critique:
  `materials/processed/2026-04-30-mixed-holomorphic-topological-strings-critique.txt`.
- Critique identity: 04:11:11 SAST, 923 pages, raw SHA-256
  `67ef2340542001a513b59689d273f08485afeb77cf279f67a3957b5c0d46fcdf`,
  text SHA-256
  `c0f3138eb8b22a88cb10bbe4ae1552e24fcfddd15e92651581c44c858dd6d0d2`.
- Vol II repository: `~/chiral-bar-cobar-vol2`.
- Vol II anchors:
  `README.md:6`, `README.md:31`, `README.md:42`,
  `README.md:50`, `README.md:59`, `metadata/theorem_registry.md:7`,
  `main.tex:1822`, `main.tex:1871`, `main.tex:1967`,
  `main.tex:2038`, `main.tex:2090`,
  `working_notes.tex:4525`, `working_notes.tex:13860`.

The critique and Vol II are evidence, not authority.  Every imported
structure below is admitted only after its own definitions, signs,
topologies, maps, and obstruction complexes are constructed in this
repository.

## Survivor

The survivor in this repository remains the reduced Hamiltonian
CE/PV--Matlis skeleton:
\[
  \mathfrak h=\mathbb C[[z_1,z_2]]/\mathbb C\cdot 1,\qquad
  P=\mathfrak h^\vee_{\mathrm{cont}}
    \cong\operatorname{Ann}_{res}(\mathbb C\cdot1).
\]
The coordinate theorem is
\[
  C^\bullet_{\mathrm{CE},coord}(\mathfrak h\ltimes P[1])
  \cong
  PV_{coord}(S(\mathfrak h)),
  \qquad c^I\mapsto\theta^I,\quad u_I\mapsto O_I .
\]
The 04:11 critique makes the type check non-negotiable:
the boundary Hamiltonian comes from \(u_I\), not from \(c^I\).

The full target is stronger than this local skeleton.  The local tuple
\[
  U^w_{\mathfrak h}
   =(\Phi_{\mathrm{coord}},\Phi^B_{P_0},C_{-,+},\Theta_{-,+},
      \Phi^{pp}_I,\Phi^{pp}_\hbar)
\]
must be realized inside actual mixed HT habitats before one may call it
a renormalized mixed holomorphic-topological string theorem.

## What Vol II Contributes

Vol II identifies the general 3D HT architecture:

1. The bar complex \(B(A)\) is an \(E_1\)-chiral coassociative coalgebra;
   its differential records holomorphic chiral products, and its
   deconcatenation coproduct records topological factorization.
   The \(\mathsf{SC}^{ch,top}\) structure lives on the chiral derived
   center \(C^\bullet_{ch}(A,A)\), and
   \((C^\bullet_{ch}(A,A),A)\) is the bulk-boundary datum
   (`README.md:6`).
2. The Vol II part structure places `SC^{ch,top}` foundations, the
   \(E_1\) ordered core, \(r(z)\)-faces, characteristic/modular data,
   the HT landscape, 3D quantum gravity, and frontier-to-theorem
   repair in one sequence (`README.md:31`).
3. Its architectural theorems include the `SC^{ch,top}` pentagon to
   heptagon, the `GRT_1(Q)` torsor of \(r(z)\)-faces, the
   \(E_3\) to \(E_\infty\) topologization ladder, the infinite
   fingerprint, and unified chiral quantum groups (`README.md:42`).
4. Its current frontier list is theorem-shaped: curved-Dunn \(H^2\)
   vanishing, DS-Hochschild bridge, periodic CDG, and associator
   independence (`README.md:50`).
5. Its theorem registry records 3,142 tagged claims, 2,345
   `ProvedHere`, 264 `ProvedElsewhere`, 258 `Conditional`, 256
   `Conjectured`, and 19 `Heuristic`
   (`metadata/theorem_registry.md:7`).

This is not a license to import results.  It is the correct categorical
and operadic grammar for the missing `Koszul_HT` habitat.

## Vol II Rectify Harness

For writing, rewriting, or reconstituting manuscript-proper text in this
repository, the required structural harness is:

`~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`.

This is not a theorem source.  It is the rewrite discipline for turning
attack evidence into manuscript prose: diagnose the organizing question,
find the unique survivor, rebuild the structure, rewrite rather than
patch broken architecture, then audit.  It is applied under Supremum
Discipline: the target is the strongest true theorem with the missing
habitat, topology, map, obstruction class, computation, or source fixture
supplied.

## Vol II Spine

### Open Primitive

Vol II begins with the statement that a 3D HT theory on
\(\mathbb C_z\times\mathbb R_t\) is not first an algebra but an
open/closed factorization dg-category.  A vacuum object produces an
\(A_\infty\)-chiral algebra as a chart; the Morita class is the
invariant.  The governing operad is the two-coloured
\(\mathsf{SC}^{ch,top}\), with closed colour
\(\mathrm{FM}_k(\mathbb C)\) and open colour \(E_1(m)\).
The bar complex is a coalgebraic shadow, not the bulk.  The bulk is the
chiral derived centre (`main.tex:1822`).

Topological-strings consequence: the brane-line algebra in this
repository must be treated as an open chart.  Its reduced current
algebra cannot be promoted to the unreduced bulk or factorization
center unless the derived-center universal property and centrality
homotopies are explicitly built.

### Ordered \(E_1\) Core

Vol II separates the symmetric closed-colour bar construction from the
ordered open-colour bar construction.  The ordered bar keeps the
\(R\)-matrix, KZ associator, and Yangian deformation; the symmetric
projection kills this extra structure in the pole-free reduction
(`main.tex:1871`).

Topological-strings consequence: an admissible large-\(N\) algebraic
shadow and a physical large-\(N\) theory are different objects.  Stable
trace/PBW data sit on an ordered/open algebraic side.  A closed
CE/PV-derived-center theorem sits on a different side.  A theorem that
identifies them must exhibit the comparison map and the ambient
two-colour Koszul model.

### Characteristic Datum And Derived Centre

Vol II describes the universal MC element \(\Theta_A\), the modular
convolution dg Lie algebra, and the chiral derived centre as the
universal bulk.  The pair \((Z^{der}_{ch},A)\) is the terminal local
open/closed datum (`main.tex:1967`).

Topological-strings consequence: the mixed MC kernel
\(\Theta_{-,+}\) in this repository must live in a completed
convolution dg Lie algebra, not in a formal display.  Its MC equation is
meaningful only after the completion, differential, bracket, and kernel
convergence are specified.

### Standard HT Landscape And BV

Vol II's HT landscape packages boundary, bulk, and line sectors as a
single modular MC element \(\Theta^{oc}\), with Costello-Gwilliam and
Costello-Gaiotto sources for physical HT theories (`main.tex:2038`).
It also includes the 6d hCS \(E_3\) chiral avatar and Feynman
coefficient chapters (`main.tex:2078`).

Topological-strings consequence: `BV^w_HT` should be defined as an
actual Costello-style object:
\[
  (E,Q,\omega,I,Q^{GF},K_t,P_{\epsilon,L},I^{ct},\Delta_L,Ob_n).
\]
Formal Moyal coefficients do not supply heat kernels, counterterms, RG
flow, locality, or QME null-homotopies.

### Three-Dimensional Quantum Gravity

Vol II evaluates the universal holography functor on Virasoro, identifies
bulk observables with the chiral derived centre, and uses chiral Higher
Deligne plus DS-Hochschild to control the \(E_3\)-chiral brace action
(`main.tex:2090`).

Topological-strings consequence: the "bulk equals derived centre of
boundary" pattern is a theorem only after the boundary category, the
bulk factorization algebra, and the functor realizing the equivalence
are supplied.  It is not a slogan one may apply to the reduced current
model.

## Two Vol II Warnings Now Binding Here

### Chiral Tamarkin

Vol II separates two codimension-one operations:

- Swiss-cheese centre: chiral Hochschild cochains form the terminal
  local `SC^{ch,top}`-algebra and add the topological direction.
- Modular convolution: the Getzler-Kapranov modular cooperad controls
  the genus direction and the BV operator \(\hbar\Delta\)
  (`working_notes.tex:4525`).

Therefore a BCOV-like genus recursion in this repository cannot be
called a chiral factorization theorem.  It belongs to a modular
operadic/obstruction complex until the factorization-algebra and
clutching data are both constructed.

### Two-Colour Koszul Duality

Vol II explicitly distinguishes:

- closed colour: symmetric chiral bar on Ran, Verdier duality, chiral
  algebra output;
- open colour: ordered bar on ordered configurations, linear duality,
  Yangian/\(E_1\)-spectral output;
- pure \(E_1\): tensor coalgebra and ordinary \(A_\infty\) output
  (`working_notes.tex:13860`).

The two-coloured quadratic dual of Swiss-cheese is not literally the
same operad.  Closed, open, and mixed sectors dualize differently.

Topological-strings consequence: `Koszul_HT` must be built as a
two-coloured operadic object with operation spaces, orientations,
compositions, dual cooperad, and convolution dg Lie algebra.  It cannot
be inferred from the coordinate CE/PV theorem, PBW theorem, or stable
trace theorem.

## Crosswalk To The Six Named Habitats

### `Coeff_{q_-,q_+}`

Local construction required here:
\[
  H_\pm=\{f=\sum_I f_IH_I:\sum_I |f_I|q_\pm^{|I|}(1+|I|)^s<\infty
  \text{ for all }s\ge0\},
\]
\[
  P_+=H_+' ,\qquad P_-=H_-',
  \qquad 1<q_-<q_+ .
\]
Vol II supplies the habit of weight-completed ambients and explicit
completion discipline.  It does not supply these formal-disk weights.
This repository must prove bracket continuity, coadjoint continuity,
diagonal kernel convergence, and MC-kernel convergence directly.

### `BV^w_HT`

Local construction required here:
\[
  E_{cl}=\Omega^\bullet(\mathbb R^2)\otimes
  \Omega^{0,\bullet}(\mathbb C^2)\otimes(H_+[1]\oplus P_-[2]).
\]
Vol II supplies the Costello-Gwilliam/HT grammar and the warning that
formal algebra is not quantization.  This repository must build the BV
pairing, gauge fixing, heat kernel, propagator, counterterms, and
non-scalar QME obstruction complex.

### `FactCenter^pp`

Local construction required here:
\[
  Obs^{pp}_{\partial,N}(I)
  =
  Obs^{cl}_{open,N}(I)\otimes
  S(C^{dR}_{c,cur}(I)\otimes P_+[1]).
\]
Vol II supplies the derived-centre doctrine: bulk is recovered from
open data by a universal centre, not by forgetting categories to
algebras.  This repository must prove compact-support functoriality,
centrality homotopies, \(Q\)-compatibility, and factorization
coherence.  The reduced current brackets are only a post-contraction
target.

### `Koszul_HT`

Local construction required here:
\[
  Def_{mix}(B,A)=
  Conv(SC_{HT}^{\ash},End_{B,A}).
\]
Vol II supplies the closest existing architecture:
\(\mathsf{SC}^{ch,top}\), chiral Higher Deligne, the heptagon, and the
two-colour Koszul warning.  This repository must define the mixed
holomorphic-topological operation spaces on
\(\mathbb R^2_{top}\times\mathbb C^2_{hol}\), their signs,
orientations, compositions, dual cooperad, MC equation, and universal
mixed centre.

### `BVFactState_{1/N}`

Local construction required here:
\[
  (Obs_N,Q_N,\Delta_N,I_N,\mu_N,\omega_N,\nu_N,T_N)_{N\ge1},
\]
with trace-test maps, connected cumulants, \(1/N\) expansion, QME Ward
identities, and convergence topology.

Vol II's universal holography and theorem registry show how physical
HT claims are separated from algebraic bar-cobar shadows.  This
repository must not identify \(A^{alg}_{st}\) or
\(A^{Kos}_{\infty,\hbar}\) with \(A^{phys}_\infty\) without states,
normalization, cumulants, planar scaling, anomaly control, QME, and
convergence.

### `GlobDesc`

Local construction required here:
\[
  C_{tar}=(X,\omega,\Omega,U,\{E_i,Q_i,\omega_i,I_i\},
  \{\phi_{ij}\},\{\phi_{ijk}\},Per,Anom,QME,Conv,Hyp,Op),
\]
and
\[
  Ob_{UKD}(C_{tar})=
  (Ob_{C_{tar}},[d\Theta_{KD}+\tfrac12[\Theta_{KD},\Theta_{KD}]]).
\]
Vol II supplies stage-discipline: Stage-1 factorization data and
Stage-2 curve-level specialization are different.  This repository
must not export local formal-disk facts to compact CY, BCOV, MNOP, Vol
III, Igusa/BKM, or sister-volume theorems without this global datum and
chosen null-homotopies.

## Admitted Local Algebra

The following are presently admissible as local algebraic data, subject
to line-by-line proof in the manuscript:

1. The reduced Hamiltonian Lie algebra
   \(\mathfrak h=\mathbb C[[z_1,z_2]]/\mathbb C1\).
2. The monomial bracket
   \[
     [H_{a,b},H_{c,d}]=(ad-bc)H_{a+c-1,b+d-1}.
   \]
3. The Matlis principal-part basis
   \(\rho_{a,b}=z_1^{-a-1}z_2^{-b-1}dz_1dz_2\), \(a+b>0\).
4. The negative-transpose coadjoint action
   \[
     z_1^pz_2^q\cdot\rho_{a,b}
      =-(pb-qa+p-q)\rho_{a-p+1,b-q+1}.
   \]
5. The coordinate CE/PV generator map
   \(c_{a,b}\mapsto\theta_{a,b}\), \(u_{a,b}\mapsto O_{a,b}\).
6. The no-identification theorem:
   \[
     Span\{\Psi_{a,b}\}\not\cong_{\mathfrak h}P
   \]
   for the same action, by local nilpotence versus principal-part
   growth.
7. The weighted diagonal kernel after the \(H_\pm,P_\pm\) topology is
   explicitly defined and the projective tensor estimates are proved.

## Not Admitted

The following are not admitted as theorems:

1. finite Taylor windows are finite Lie quotients;
2. coordinate CE/PV is a global completed \(P_0\)-algebra;
3. \(\Psi=\rho\);
4. reduced current target is the unreduced factorization center;
5. Moyal coefficients are Costello quantization;
6. stable invariant theory is physical large \(N\);
7. Vol II `SC^{ch,top}` theorems automatically prove this repository's
   `Koszul_HT`;
8. Vol II or Vol III global claims follow from the local Hamiltonian
   formal disk.

## Supremum Repair Target

The correct repair is not demotion.  The theorem this repository wants
is stronger than the current local algebraic skeleton:

> A weighted mixed holomorphic-topological BV theory on
> \(\mathbb R^2_{top}\times\mathbb C^2_{hol}\), with principal-part
> brane current center and mixed Swiss-cheese Koszul MC data, realizes
> the local Hamiltonian CE/PV--Moyal skeleton; its scalar anomaly is
> handled by a specified branch, its non-scalar QME obstruction vanishes,
> its physical large-\(N\) states converge when such a limit is asserted,
> and its global descent obstruction vanishes when global transfer is
> asserted.

This is the platonic target.  Until the habitats exist, conditional
status is a proof ledger, not the final statement.

The 04:11 refresh adds the metacognitive rule that the next swarm must
attack habitats rather than rhetorical claims.  Each agent reports the
habitat, source/target, basis, topology, first coordinate computation,
obstruction complex, and inscription path.  The controlling document is
`reconstitution/attack-heal-216-metacognitive-controller-2026-04-30.md`.

## On-Disk Consequences

1. `reconstitution/latest-critique-claim-construction-catalogue-2026-04-30.md`
   is updated to the 04:11 artifact and now points here for the Vol II
   synthesis.
2. `references/source-provenance.md` records the 04:11 hashes, page
   count, and line count.
3. `reconstitution/roadmap-index-2026-04-30.md` supersedes the 2026-04-28
   index for active reconstitution work.
4. `~/chiral-bar-cobar-vol2/notes/vol1_control_surface_import_manifest_2026_04_30.md`
   records that both Vol I control surfaces have been made visible in
   Vol II: the antipattern registry and the first-principles cache.
   The exact mirrors are
   `notes/vol1_imported_antipatterns_catalogue_2026_04_30.md` and
   `notes/vol1_imported_first_principles_cache_comprehensive_2026_04_30.md`;
   the live Vol II files also contain appended import blocks.  These are
   attack-heal controls, not theorem imports.
5. Future manuscript-proper writing, rewriting, or reconstitution must
   use
   `~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`
   under Supremum Discipline.
6. Future manuscript edits should introduce a real `Koszul_HT` section
   only by constructing the two-colour operad/cooperad/convolution
   package, not by naming it.
7. Future attack-heal cycles use Supremum Discipline: the repair target
   is the strongest true theorem, and any conditional statement is only
   a temporary proof-status ledger.
