# Primary Source Theorem Support Audit

Date: 2026-04-30

Agent: 246

Scope: audit of the sharpened theorem surfaces for primary-source support,
missing citation anchors, and claims that must be proved internally.  No
TeX/manuscript files were edited.  No web browsing was used.

## Verdict

The current theorem surfaces mostly have the right proof-strength grammar:
Costello, LQT, Tate bar-cobar, Matlis, Hormander, Weiss/Ran, and radial
sources are not being asked to prove the whole local mixed
holomorphic-topological theorem by citation.  The remaining problem is source
granularity.  Several surfaces cite a correct tradition but lack a local
primary-source fixture with exact theorem/page anchors, while the hardest
surfaces are not citable at all and must be derived inside this manuscript.

Stable source support:

- Costello supports the finite-scale elliptic BV/RG/QME graph calculus only:
  heat kernels, regularized BV Laplacians, graph expansion, counterterms,
  locality, and obstruction complexes.
- Matlis/local cohomology/residue support is closed for
  `E_R(k) ~= H^2_m(C[[z1,z2]]) dz1 dz2` and the Cech/residue basis.
- Procesi/Razmyslov support stable matrix trace invariant theory, not the
  derived Koszul/one-psi calculation by themselves.
- Radial-parts sources support the Harish-Chandra/Wallach/Levasseur-Stafford
  radial-component package, not the manuscript's exact Weyl-trace generator
  normalization.

Missing or incomplete primary-source support:

- Loday--Quillen--Tsygan: bibliography entries exist, but no local primary
  fixture/PDF/text line anchors are present.
- Tate bar-cobar/Quillen/model-category transfer: bibliography entries exist,
  but no local source fixture fixes the exact theorem anchors used by the
  admissible envelope.
- Hormander wavefront calculus: bibliography entry exists, but there is no
  local anchor file for product, pullback/pushforward, and non-characteristic
  hypotheses.
- Weiss/Ran/stratified descent: the current local anchors are mostly
  Costello--Gwilliam metadata and a separate `omega-stratified` analogy
  fixture.  A theorem-grade descent source package is still missing.
- Bochner--Martinelli--Koppelman: the manuscript contains a finite-window
  construction, but the classical BMK identity and normalization need a
  primary several-complex-variables source anchor.

The following claims must be derived internally rather than cited:

- the Hamiltonian brane-defect Costello specialization, including the
  `D'_c` current graph target, scalar-contact chain projection,
  bulk-to-defect kernel, finite-window row table, theta3 row, and
  non-scalar counterterm tower;
- the actual stable trace/Koszul calculation for the Dirac brane model,
  including one-psi primitive homology and finite stable range;
- the admissible Tate completion, lower-central pronilpotence, Roos/Milnor
  exactness, strict product/direct-sum obstruction, and exact continuous
  duality package;
- the CE/PV coordinate comparison and every completion, equivariant, and
  factorization/descent upgrade beyond finite coordinates;
- the Matlis Hamiltonian coadjoint formula and the no-go for same-action
  PBW/Matlis descendants;
- the BMK finite-window transfer estimates, collar terms, arity-two
  comparison, and all-window obstruction vector;
- the wavefront-admissible current graph calculus and the no-canonical-product
  obstruction for arbitrary compactly supported distributions;
- the exact Weyl/Moyal coefficients, the bivariate triangular trace formula,
  the exact all-`N` radial normalization, edge PBW telescoping, and the
  all-interior decorated-necklace homotopy;
- the brane-preserving normal `Omega` background, residue/Euler
  normalization, stratified trace state, physical large-`N` state, and Ward
  identities in this local model.

## Exact Missing-Source List

### MS-001: Loday--Quillen--Tsygan primary fixture

Current anchors:

- `main.tex:1745-1782` states LQT as an external template.
- `theorem-lanes.tex:2017` requires a finite-window LQT comparison in the
  open acceptance target.
- `main.tex:8854-8870` contains `loday-quillen` and `tsygan` bibliography
  entries.

Missing source:

- Add a primary fixture for Loday--Quillen 1984 and Tsygan 1983 with exact
  theorem/page anchors for
  `Prim H_*^CE(gl_infty(A)) ~= HC_{*-1}(A)`.
- Loday--Vallette, Ch. 13 may remain a secondary operadic packaging source,
  not the primary theorem source.

Use boundary:

- Cite LQT only for the stable matrix Lie homology/cyclic homology theorem.
- Derive internally the Dirac/Koszul stable trace theorem, Procesi/Razmyslov
  stable range, one-psi primitive homology, scalar-word convention, and
  any completed finite-window LQT map.

### MS-002: Tate bar-cobar / Quillen / admissible model envelope anchors

Current anchors:

- `main.tex:5200-5461` states the Tate CE, completed PBW, and admissible
  Koszul criterion.
- `open-obligations.tex:102-142` and `claim-strength-ledger.tex:914-930`
  record the admissible Tate bar-cobar/Quillen envelope.
- Bibliography entries are present at `main.tex:9104-9265`.

Missing source:

- Add a source fixture with exact anchors for Priddy 1970, Loday--Vallette
  bar-cobar/PBW signs, Quillen homotopical algebra, Hinich transfer,
  Hovey's model-category adjoint-functor criteria, Lefevre-Hasegawa
  `A_infty`/conilpotent coalgebra conventions, Schwede--Shipley monoids in
  monoidal model categories, and the precise Lurie/Dwyer-Kan localization
  statement actually used.

Use boundary:

- These sources can support standard bar-cobar and model-category grammar.
- They do not supply the manuscript's admissible Tate category, weighted
  coefficient pair, lower-central Tate-pronilpotence, strict
  product/direct-sum Casimir obstruction, finite-window Roos classes, or
  exact continuous-dualization theorem.  Those are internal theorem data.

### MS-003: Hormander wavefront calculus fixture

Current anchors:

- `reconstitution/regular-density-wavefront-current-graph-branch-construction-target-2026-04-30.md`
  names the product/pushforward/non-characteristic wavefront conditions.
- Bibliography contains `hormander-vol1`.

Missing source:

- Add a local anchor file for Hormander, Vol. I, Ch. 8, with exact theorem
  anchors for wavefront set, product of distributions, pullback/pushforward
  or non-characteristic restrictions, and operations under proper maps.
- If the graph theorem uses finite scaling degree/extension across
  diagonals as an external theorem, add a separate primary source for that
  extension theorem.  Otherwise prove the needed extension directly in the
  Costello current graph habitat.

Use boundary:

- Hormander supplies criteria for when products and functorial operations on
  distributions are defined.
- The manuscript must compute or bound the wavefronts of its own kernels,
  current labels, configuration-space maps, diagonal extensions, and
  counterterms.  Arbitrary `D'_c(I)` labels cannot be admitted by citation.

### MS-004: Weiss/Ran and stratified descent anchors

Current anchors:

- `main.tex:4118-4247`, `open-obligations.tex:757-888`, and
  `theorem-lanes.tex:2922-2980` state Weiss/Ran and stratified descent
  obstruction surfaces.
- `references/primary-sources/omega-stratified-source-anchors-2026-04-30.md`
  records AFT stratified factorization homology and related analogies.
- Costello--Gwilliam local Cambridge mirrors verify metadata/vocabulary only.

Missing source:

- Add theorem-grade sources for the precise descent formalism being used:
  Costello--Gwilliam theorem anchors for factorization algebras and Weiss
  descent, Ayala--Francis--Tanaka for stratified factorization homology if
  the `Disk^{str}` language is used, and a Ran-space/chiral source such as
  Beilinson--Drinfeld only where the Ran formalism is actually invoked.
- Add bibliography keys for AFT and any Weiss/Boavida de Brito--Weiss source
  if those results are cited, not just mentioned in a source fixture.

Use boundary:

- External sources can define the descent grammar.
- The mixed `R^2_top x C^2_hol` product-disk site, stratified brane pair
  `(X,L)`, collar modules, products, centrality homotopies, QME curvature,
  finite normal localization ring, and physical trace state must be built
  internally.  AFT/CG/BD do not prove them for this model.

### MS-005: Bochner--Martinelli--Koppelman source anchor

Current anchors:

- `main.tex:1242-1494` proves a finite-window BMK transfer statement.
- `theorem-lanes.tex:381-527` records the native `E_2` lane and BMK
  obligation.
- `claim-strength-ledger.tex:318-538` records the all-window BM transfer
  as a construction target.

Missing source:

- Add a primary several-complex-variables anchor for the BMK kernel,
  Koppelman identity, normalization `(2*pi*i)^{-2}`, and current/regularity
  assumptions.

Use boundary:

- A BMK source may support the classical Dolbeault homotopy identity.
- It will not prove the manuscript's finite-window moment projection,
  cutoff collar calculus, extension-by-zero factorization compatibility,
  two-variable principal-part face, or all-window obstruction vector
  `Ob_BM^infty`.

### MS-006: Costello theorem-number and Costello--Gwilliam theorem anchors

Current anchors:

- `references/primary-sources/local-costello-bv-kernel-source-anchors-2026-04-30.md`
  is the current local Costello boundary.
- `references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md`
  records line anchors in the arXiv mirror.

Missing source:

- If the manuscript cites exact AMS book theorem numbers, import or record
  a published-book page/theorem-number mirror.  Until then use the existing
  arXiv text anchors.
- Costello--Gwilliam theorem-level anchors are still absent for unrestricted
  factorization descent, Noether currents, and anomalies.  The Cambridge
  HTML mirrors are metadata/vocabulary support only.

Use boundary:

- Costello supports the universal finite-scale BV/RG/QME package.  He does
  not supply the current-valued Hamiltonian brane-defect graph theorem.

### MS-007: Exact radial/Weyl-trace normalization source

Current anchors:

- `references/primary-sources/radial-parts-capelli-source-anchors-2026-04-28.md`
  records the current radial source boundary.
- `main.tex:6700-7218` and `main.tex:8521-8771` contain the radial/Moyal
  and first/third coefficient surfaces.
- `reconstitution/radial-edge-pbw-telescoping-theorem-2026-04-30.md` and
  `reconstitution/radial-all-interior-necklace-homotopy-push-2026-04-30.md`
  record the current radial proof frontier.

Missing source:

- No primary source in the local fixture states the exact all-`N`
  Weyl-trace image
  `Rad_0(J_N(f)) = Delta^{-1} S_N(f) Delta`
  with the manuscript's `Y=-hbar d_X^t`, `z_2=-hbar d_lambda`, total Weyl
  ordering, and trace generator convention.

Use boundary:

- Harish-Chandra, Wallach, and Levasseur--Stafford support the radial
  component framework, kernel/image lineage, and discriminant conjugation
  context.
- The exact bivariate triangular trace formula, pure-power/shear reduction,
  edge PBW telescope, interior decorated-necklace homotopy, and finite
  certificates must be internal.  If the all-`N` normalization is not
  internally proved, it remains an explicit external input.

### MS-008: Omega/stratified trace source integration

Current anchors:

- `references/primary-sources/omega-stratified-source-anchors-2026-04-30.md`
  records AFT, Costello Omega-M-theory, Costello M2/Koszul, and CFG
  Chern--Simons trace analogies.
- `local-dictionary.tex:631-662`, `open-obligations.tex:916-954`, and
  `theorem-lanes.tex:2922-2980` state the local Omega/trace obligations.

Missing source:

- If these analogies are cited in the manuscript, add bibliography keys and
  exact citation targets for AFT stratified factorization, Costello's
  Omega-background paper, the M2/Koszul paper, and CFG only in their stated
  scopes.

Use boundary:

- These sources give vocabulary and comparison models.
- They do not prove the brane-preserving normal scaling torus,
  `Q_Omega=Q+i_V`, normal-weight contraction, residue/Euler normalization,
  `R_Omega^{N,M}` coefficient ring, stratified current brackets, QME
  quantization, or physical large-`N` trace state in this paper.

## Surface-By-Surface Audit Matrix

| Surface | Source support | Missing citation anchor | Must be internal |
|---|---|---|---|
| Costello finite-scale BV/QME | Supported by Costello arXiv anchors for `P(eps,T)`, `Delta_t`, RG/QME, local functionals, counterterms, graph asymptotics, and obstruction calculus. | Published Costello theorem numbers and CG theorem-level descent anchors remain incomplete. | Hamiltonian current target, `D'_c` wavefront theorem, bulk-to-defect kernel, scalar lift, finite row table, theta3, non-scalar counterterms. |
| LQT/stable cyclic | Bibliography has Loday--Quillen and Tsygan; Costello--Li contains a useful secondary/thematic LQT use. | Local primary fixture for LQ84/Tsy83 theorem and exact shifted cyclic convention. | Dirac/Koszul stable trace theorem, one-psi homology, scalar convention, finite stable range, completed LQT acceptance map. |
| Tate bar-cobar/Quillen | Bibliography has the right source family. | Fixture with theorem anchors for Priddy, Loday--Vallette, Quillen, Hinich, Hovey, Lefevre-Hasegawa, Schwede--Shipley, and Lurie. | Admissible Tate envelope, lower-central condition, completed PBW in this topology, exact continuous dualization, Roos/Milnor gates, endpoint obstruction. |
| CE/PV | The coordinate proof is self-contained on finite windows. | Optional standard PV/Schouten source only if a non-coordinate convention is invoked. | Bracket-admissible completion, equivariant refined bracket, kernel admissibility, global factorization/descent upgrade. |
| Matlis principal parts | Matlis/Hartshorne/Kunz source fixture closes the residue/top-local-cohomology source row. | None for the displayed Cech/residue basis. | Reduced non-`R`-submodule statement, coadjoint formula, residue rigidity, PBW/Matlis no-go. |
| Wavefront/current graphs | Hormander is in bibliography; construction reports state the correct criteria. | Local Hormander Ch. 8 fixture and possibly scaling-degree extension source. | Kernel wavefronts, admissible current subspaces, graph products, diagonal extensions, counterterms, arbitrary-`D'_c` obstruction. |
| Weiss/Ran descent | CG metadata and AFT analogy fixture supply vocabulary only. | CG theorem anchors, AFT bibliography/source, Weiss/Ran precise source package. | Mixed product-disk site, stratified pair `(X,L)`, collar modules, centrality homotopies, descent vector, trace state. |
| BMK/native `E_2` | Local finite-window proof exists. | Primary BMK/Koppelman source for the classical identity and normalization. | Cutoff/collar estimates, finite moment projection, arity-two transfer, all-window `Ob_BM^infty`. |
| Weyl/Moyal/radial | Formal Moyal computation and radial framework sources exist. | Exact Weyl-trace all-`N` source absent. | Triangular formula, radial normalization or conditional gate, edge theorem, interior necklace homotopy, finite scripts. |
| Omega/physical trace | AFT/Costello/CFG analogies recorded in source fixture. | Bibliography keys and exact anchors if used in manuscript. | Normal scaling, `Q_Omega`, localized coefficient ring, residue/Euler normalization, stratified trace class, physical state. |

## Citation Anchors That Are Safe Now

Use these only within their support boundary.

- Costello 2011/arXiv `0706.1533`: finite-scale propagator
  `references/primary-sources/costello-renormalisation-bv-0706.1533.txt:77-90`,
  heat kernels `:1549-1558`, regularized BV Laplacian `:407-423`,
  local functionals `:1122-1151`, counterterm theorem `:1746-1807`,
  RG/locality `:1967-2001`, graph expansion `:3610-3625`, graph
  asymptotics `:3547-3568` and `:3660-3679`, obstruction calculus
  `:2376-2420`, `:2469-2483`, `:2975-3014`.
- Costello--Li: obstruction-degree convention at
  `references/primary-sources/costello-li-quantum-bcov-1201.4501.txt:2493-2505`;
  open-closed BCOV scope and anomaly warnings only as quarantine/exclusion
  evidence.
- Matlis/local cohomology/residue:
  `references/primary-sources/matlis-local-cohomology-residue-anchor.md`.
- Radial framework:
  `references/primary-sources/radial-parts-capelli-source-anchors-2026-04-28.md`.
- Omega/stratified analogies:
  `references/primary-sources/omega-stratified-source-anchors-2026-04-30.md`.

## Non-Citable Construction Claims

The following should not be repaired by adding citations.  They need proof,
finite computation, or an exact obstruction theorem in the manuscript:

1. `Curv_K(kappa_G + C_hbar)=0` for the non-scalar Costello brane-defect
   Hom complex.
2. Existence of the `D'_c` current-valued Costello target for arbitrary
   compactly supported distributions.
3. Vanishing of theta3 and companion finite-window graph rows.
4. Vanishing of scalar-contact lift obstructions
   `o_{sigma,w}^{(r)}` and the equivariant analogues.
5. Exactness of the open `A_infty`/cyclic/Koszul acceptance cone.
6. The strict product/direct-sum formal disk as a valid Tate kernel habitat.
7. All-window BMK transfer and all-window native `E_2` homotopy transfer.
8. The physical large-`N` trace state and protected brane correlators.
9. The exact all-`N` radial Weyl-trace image normalization.
10. The all-interior radial decorated-necklace harmonic vanishing theorem.

## Attack-Heal Conclusion

No theorem surface should be weakened merely because a citation is missing.
The repair is sharper:

- add primary source fixtures for LQT, Tate/Quillen, Hormander,
  Weiss/Ran/stratified descent, and BMK;
- use the existing Costello, Matlis, radial, and Omega fixtures only within
  their stated boundaries;
- prove the local Hamiltonian, current-valued, finite-window, radial, BMK,
  and trace-state claims internally, or state the exact obstruction class
  that blocks them.
