# Missing Primary Source Fixture Plan

Date: 2026-04-30

Agent: 253

Scope: report-only conversion of Agent 246's source-support audit into an
actionable primary-source fixture plan.  No TeX, bibliography, script, source
fixture, or PDF asset was edited.  No browsing was used.

## Controls

- `CLAUDE.md` and `AGENTS.md`.
- `~/ecosystem` attack-heal protocol.
- `~/ecosystem/INVARIANTS.md` voice and source discipline.
- `~/ecosystem/AGENTS-HARNESS.md` self-reflection rubric.
- Vol II `chriss-ginzburg-rectify` discipline as a control surface.
- Agent 246 reports:
  `reconstitution/primary-source-theorem-support-audit-2026-04-30.md` and
  `reconstitution/swarm-2026-04-30-agent-246-primary-source-theorem-support-audit.md`.

## Verdict

Agent 246's audit is correct: the missing work is source granularity, not
claim demotion.  The next source pass should add five local fixtures:

1. `references/primary-sources/lqt-tsygan-source-anchors-2026-04-30.md`.
2. `references/primary-sources/tate-barcobar-quillen-source-anchors-2026-04-30.md`.
3. `references/primary-sources/hormander-wavefront-source-anchors-2026-04-30.md`.
4. `references/primary-sources/weiss-ran-stratified-descent-source-anchors-2026-04-30.md`.
5. `references/primary-sources/bmk-koppelman-source-anchors-2026-04-30.md`.

Each fixture must record the local mirror path when one is imported,
checksums, exact theorem/page anchors, hypotheses, positive support, and
non-support.  A later bibliography/provenance pass may cite the fixtures.
This report does not edit `main.tex`, `references/source-provenance.md`, or
the bibliography.

## Fixture Standard

Every source fixture should contain:

- source row: author, title, venue, year, DOI/arXiv/publisher identifier;
- local mirror row, if imported: PDF/text path and SHA-256;
- exact theorem, definition, proposition, page, or equation anchors;
- hypotheses required by the source theorem;
- supported manuscript theorem surface;
- explicit non-support boundary;
- decision: cite external theorem, derive internally, or use as convention only;
- verification commands used to locate anchors.

Do not record invented theorem numbers.  If an exact theorem/page anchor is not
verified, the fixture must say `anchor still unverified` and keep the manuscript
claim out of the stable source core.

## MS-001: Loday--Quillen--Tsygan

Current manuscript anchors:

- `main.tex:1745-1777` states LQT as an external template.
- `theorem-lanes.tex:2072` requires a finite-window LQT comparison.
- `main.tex:8854-8870` already has bibliography entries for
  `loday-quillen` and `tsygan`.

Missing exact sources:

- Jean-Louis Loday and Daniel Quillen, "Cyclic homology and the Lie algebra
  homology of matrices", `Comment. Math. Helv.` 59 (1984), 565--591,
  DOI `10.1007/BF02566367`.
- Boris L. Tsygan, "The homology of matrix Lie algebras over rings and the
  Hochschild homology", `Russian Math. Surveys` 38:2 (1983), 198--199,
  DOI `10.1070/RM1983v038n02ABEH003481`.
- Jean-Louis Loday, `Cyclic Homology`, 2nd ed., only as a modern convention
  check for shifts/signs if needed.  It is not the primary theorem source.

Theorem supported:

```text
Prim H_*^CE(gl_infty(A); C) ~= HC_{*-1}(A)
```

and equivalently the connected Hopf algebra form

```text
H_*^CE(gl_infty(A); C) ~= S(HC_{*-1}(A))
```

over characteristic zero, under the source's hypotheses on `A`.

Cite or derive:

- Cite Loday--Quillen and Tsygan for the stable matrix Lie homology/cyclic
  homology theorem only.
- Derive internally the Dirac/Koszul stable trace theorem, the
  Procesi--Razmyslov stable range, the scalar-word convention, one-psi
  primitive homology, and any completed finite-window LQT map for
  `A_psi = T(x,y,psi), d psi = xy-yx`.

Fixture actions:

- Import official/publisher or DOI-resolved copies if accessible; otherwise
  record exact publisher metadata and page anchors without mirroring.
- Extract text only if legally available and technically clean.
- Verify the degree shift `HC_{*-1}` versus cochain conventions used in
  `main.tex:1756-1770`.
- Add a non-support row: LQT does not prove the local Hamiltonian
  brane-defect trace/Koszul theorem.

## MS-002: Tate Bar-Cobar / Quillen Envelope

Current manuscript anchors:

- `main.tex:5200-5461` states the completed CE/PV, Tate CE, PBW, and
  admissible Koszul criterion.
- `open-obligations.tex:102-142` and `claim-strength-ledger.tex:946-958`
  record the admissible Tate bar-cobar/Quillen envelope.
- `main.tex:9104-9265` contains several relevant bibliography entries, but
  no local primary fixture gives theorem anchors.

Missing exact sources:

- Stewart B. Priddy, "Koszul resolutions", `Trans. Amer. Math. Soc.` 152
  (1970), 39--60, DOI `10.1090/S0002-9947-1970-0265437-8`.
- J. F. Adams, "On the cobar construction", `Proc. Nat. Acad. Sci. U.S.A.`
  42 (1956), 409--412.  Use only after exact bibliographic and theorem
  anchors are verified.
- Daniel G. Quillen, `Homotopical Algebra`, Lecture Notes in Mathematics 43,
  Springer, 1967.
- Daniel G. Quillen, "Rational homotopy theory", `Ann. of Math.` 90 (1969),
  205--295, if the fixture uses Quillen's dg Lie / coalgebra bar-cobar
  rational-homotopy package rather than only model-category grammar.
- Vladimir Hinich, "Homological algebra of homotopy algebras",
  `Comm. Algebra` 25:10 (1997), 3291--3323, DOI
  `10.1080/00927879708826055`, arXiv `q-alg/9702015`.
- Mark Hovey, `Model Categories`, AMS Mathematical Surveys and Monographs
  63, 1999, DOI `10.1090/surv/063`.
- Kenji Lefevre-Hasegawa, `Sur les A_infty-categories`, thesis, 2003,
  arXiv `math/0310337`.
- Stefan Schwede and Brooke Shipley, "Algebras and modules in monoidal
  model categories", `Proc. London Math. Soc.` 80:2 (2000), 491--511,
  DOI `10.1112/S002461150001220X`.
- William G. Dwyer and Daniel M. Kan, "Simplicial localizations of
  categories", `J. Pure Appl. Algebra` 17:3 (1980), 267--284, and
  "Calculating simplicial localizations", `J. Pure Appl. Algebra` 18:1
  (1980), 17--35, only if the manuscript invokes Dwyer--Kan localization.
- Jacob Lurie, `Higher Algebra`, official PDF already cited in the
  bibliography, only for presentable symmetric monoidal infinity-categorical
  grammar when that grammar is actually used.
- Vladimir Drinfeld, "Infinite-dimensional vector bundles in algebraic
  geometry: an introduction", if a later pass wants an external Tate-vector
  source rather than a fully internal finite-window Tate definition.
- Bousfield--Kan, Roos, Jensen, or another exact derived-inverse-limit source
  only if the manuscript chooses to cite `lim^1`/Mittag--Leffler exactness
  rather than proving the finite-window ML assertions internally.

Theorems supported:

- Standard Koszul resolution and Koszul duality grammar.
- Classical bar/cobar constructions and bar-cobar comparison in finite or
  conilpotent settings.
- Model-category and Quillen-adjunction vocabulary.
- Transfer of algebra/module model structures under stated monoidal
  hypotheses.
- `A_infty` and conilpotent coalgebra conventions.
- Localization grammar, only where explicitly invoked.

Cite or derive:

- Cite these sources for standard bar-cobar, PBW/Koszul, model-category,
  localization, and operadic convention grammar.
- Derive internally the actual admissible Tate category, the weighted
  coefficient pair, lower-central Tate-pronilpotence, exact continuous
  dualization, finite-window ML/Roos gates unless externally anchored,
  strict product/direct-sum Casimir obstruction, and the completed
  Hamiltonian envelope used in this manuscript.

Fixture actions:

- Split rows into `primary theorem`, `modern convention`, and `optional
  infinity-categorical grammar`.
- Do not let `Loday--Vallette` replace primary sources; use it for signs and
  operadic packaging after primary anchors are present.
- Add a non-support row: no listed source constructs
  `g_adm = h_adm semidirect D_cont[1]` or proves the manuscript's strict
  endpoint obstruction.

## MS-003: Hormander Wavefront Calculus

Current manuscript anchors:

- `theorem-lanes.tex:3372-3389` records the wavefront eta obstruction.
- `claim-strength-ledger.tex:461-469` records the regular-density and
  wavefront-current graph branches.
- Agent 237 records the graphwise admissibility boundary and the obstruction
  for arbitrary `D'_c(I)` labels.
- `main.tex:9205-9214` has `hormander-vol1`, but no local theorem fixture.

Missing exact sources:

- Lars Hormander, `The Analysis of Linear Partial Differential Operators. I:
  Distribution Theory and Fourier Analysis`, Classics in Mathematics,
  Springer, 2003 reprint of the second edition.  Fixture target: Chapter 8.
- Optional only if external diagonal-extension/scaling-degree technology is
  used: Brunetti--Fredenhagen style microlocal renormalization or an
  Epstein--Glaser/scaling-degree source.  If not used, leave this out and
  prove the extension inside the Costello current graph habitat.

Theorems supported:

- Definition and basic properties of wavefront sets.
- Product criterion for distributions: no opposite covectors over the same
  point.
- Pullback/restriction criterion under non-characteristic maps.
- Pushforward/proper direct image wavefront estimate.
- External tensor product and composition estimates, if used in graph
  contractions.

Cite or derive:

- Cite Hormander for the microlocal criteria governing whether products,
  restrictions, pullbacks, and pushforwards of distributions are defined.
- Derive internally the wavefronts of the manuscript's propagators, current
  labels, configuration-space maps, diagonal extensions, and counterterms.
- Derive internally the no-canonical-product obstruction for arbitrary
  `D'_c(I)` labels.  Hormander supplies the obstruction criterion, not the
  graph theorem.

Fixture actions:

- Locate exact Chapter 8 theorem numbers/pages for product, pullback,
  pushforward, and restriction.
- Record the hypotheses in the same variables used by the graph branch:
  finite graph, configuration map, current label tuple, diagonal, and
  properness/support condition.
- Add a non-support row: `hormander-vol1` does not provide Costello
  counterterms, scalar-contact projection, Roos compatibility, or
  brane-defect QME cancellation.

## MS-004: Weiss/Ran And Stratified Descent

Current manuscript anchors:

- `main.tex:4171-4247` isolates the Weiss/Ran descent obstruction complex.
- `open-obligations.tex:890-1021` records stratified Weiss covers,
  centrality homotopies, QME curvature, and the source-primary audit
  obstruction.
- `references/primary-sources/omega-stratified-source-anchors-2026-04-30.md`
  already records AFT and Omega/trace analogies, but it is not integrated as
  a theorem-grade descent source package.

Missing exact sources:

- Kevin Costello and Owen Gwilliam, `Factorization Algebras in Quantum Field
  Theory`, Vol. I, Cambridge University Press, 2017.  Needed fixture target:
  exact definition/theorem anchors for prefactorization algebras,
  factorization algebras as Weiss cosheaves, and descent.
- Kevin Costello and Owen Gwilliam, Vol. II, only for quantum observables,
  Noether/anomaly vocabulary, and only after exact theorem anchors are
  verified.
- Pedro Boavida de Brito and Michael Weiss, "Manifold calculus and homotopy
  sheaves", `Homology Homotopy Appl.` 15:2 (2013), 361--383.  Needed for
  Weiss topology/homotopy sheaf grammar if that route is cited.
- Michael Weiss, "Embeddings from the point of view of immersion theory. I",
  `Geom. Topol.` 3 (1999), 67--101, for the manifold-calculus/Weiss-cover
  source lineage.
- David Ayala, John Francis, and Hiro Lee Tanaka, "Factorization homology of
  stratified spaces", `Selecta Math. (N.S.)` 23 (2017), 293--362, arXiv
  `1409.0848`.  The existing local fixture already records Definition 2.14,
  Theorem 2.15, Definition 2.37, Corollary 2.40, Theorem 2.43, Corollary
  0.3, Proposition 4.8, and Proposition 4.13 as useful anchors.
- Alexander Beilinson and Vladimir Drinfeld, `Chiral Algebras`, AMS, 2004,
  only where the Ran formalism itself is invoked.  Do not cite BD for a
  native `C^2` mixed HT descent theorem.
- Jacob Lurie, `Higher Algebra` or `Higher Topos Theory`, only for
  infinity-categorical descent or locally constant `E_n` grammar when the
  manuscript explicitly uses that level of language.

Theorems supported:

- Factorization algebras as local-to-global cosheaf objects for Weiss covers.
- Homotopy sheaf/descent formalism for Weiss topology.
- Stratified factorization homology from `Disk`-algebras, excision, and
  continuity.
- Ran-space/chiral language, only for actual Ran/chiral statements.

Cite or derive:

- Cite CG/Boavida--Weiss/Weiss/AFT/BD for descent grammar and the formal
  external source theorem when its hypotheses are verified.
- Derive internally the mixed product-disk site for
  `R^2_top x C^2_hol`, the stratified pair `(X,L)`, collar modules,
  product and `P_0` centrality homotopies, `delta_Weiss`, brane-defect QME
  curvature, normal Omega coefficient ring, and trace state.
- Do not use AFT or CG to prove the local brane-defect trace theorem by
  analogy.

Fixture actions:

- Promote the existing AFT row from the Omega analogy fixture into a dedicated
  descent fixture, or cross-reference it without duplication.
- Import exact CG theorem anchors beyond current Cambridge metadata.
- Add a source-boundary table separating `Weiss`, `Ran`, and `stratified`
  uses; these are not interchangeable.
- Add a non-support row: none of the external descent sources supplies the
  mixed Dolbeault/de Rham coefficient system or its QME.

## MS-005: Bochner--Martinelli--Koppelman

Current manuscript anchors:

- `main.tex:1242-1420` states the finite-window BMK transfer.
- `main.tex:1422-1452` uses the Koppelman identity in the proof.
- `main.tex:1494-1501` records the all-window transfer as the next theorem
  target.
- Agent 206 and Agent 222 identify the classical kernel source gap and keep
  the all-window obstruction internal.

Missing exact sources:

- Enzo Martinelli, "Alcuni teoremi integrali per le funzioni analitiche di
  piu variabili complesse", `Mem. R. Accad. d'Italia, Cl. Sci. Fis. Mat.
  Nat.` 9 (1938), 269--283.  Verify exact accents, title, and pagination
  before citation.
- Salomon Bochner, "Analytic and meromorphic continuation by means of
  Green's formula", `Ann. of Math.` 44 (1943), 652--673.  Verify exact role
  for the Bochner--Martinelli kernel before citation.
- Wolfgang Koppelman, "The Cauchy integral for differential forms".  The
  fixture must verify the exact venue, pages, and whether the usable theorem
  appears in the announcement or a longer paper before this is cited.
- R. Michael Range, `Holomorphic Functions and Integral Representations in
  Several Complex Variables`, Springer GTM 108, 1986, or
  Henkin--Leiterer, `Theory of Functions on Complex Manifolds`, only as a
  modern theorem/normalization check if the primary originals are too terse.

Theorems supported:

- Classical Bochner--Martinelli kernel and integral formula.
- Koppelman formula for differential forms.
- Normalization of the Dolbeault homotopy kernel, including the
  `(2*pi*i)^(-2)` convention after verification.
- Regularity/current assumptions for applying the homotopy formula.

Cite or derive:

- Cite BMK/Koppelman sources for the classical `bar partial` homotopy
  identity and kernel normalization.
- Derive internally the finite-window moment projection `p_N`, the
  support-at-zero current representatives `Delta_{a,b}`, cutoff collar
  terms, arity-two Hamiltonian/Matlis comparison, two-variable
  principal-part face, and the all-window obstruction vector
  `Ob_BM^infty`.

Fixture actions:

- Do not cite the Koppelman identity in the manuscript until the fixture
  verifies the exact source theorem and normalization.
- If the exact historical source is inaccessible, cite Range or
  Henkin--Leiterer for the formula and record the historical sources as
  lineage, not theorem support.
- Add a non-support row: classical BMK sources do not prove a native `E_2`
  factorization transfer or uniform all-window estimates for this paper.

## Work Order

1. Build the LQT/Tsygan fixture first.  It is already bibliographically
   present and has the smallest theorem surface.
2. Build the Hormander fixture second.  It blocks the current-valued graph
   calculus from admitting arbitrary distributions by slogan.
3. Build the BMK fixture third.  The manuscript already uses the Koppelman
   identity in a proof, so the classical kernel source should be anchored
   before any TeX citation-strength increase.
4. Build the Tate bar-cobar/Quillen fixture fourth.  It is broader and must
   be split into primary finite/conilpotent algebra, model-category grammar,
   and manuscript-internal Tate envelope.
5. Build the Weiss/Ran/stratified descent fixture fifth.  It should reuse the
   existing AFT row and import exact CG/Weiss/BD anchors only for the
   language actually used.

## Internal Derivation Boundary

No source fixture should be allowed to prove the following by citation:

- the Hamiltonian current-valued Costello graph/QME theorem;
- graph products and counterterms for arbitrary `D'_c` labels;
- scalar-contact projection and non-scalar counterterm tower;
- Dirac/Koszul one-psi stable trace computation;
- completed finite-window LQT acceptance map;
- admissible Tate envelope and strict endpoint obstruction;
- finite-window BMK transfer beyond the classical homotopy identity;
- all-window native `E_2` BMK transfer;
- mixed product-disk Weiss/Ran descent;
- stratified brane centrality homotopies and QME curvature;
- physical or protected large-`N` trace state.

These are manuscript theorem data.  If a construction fails, the report should
name the exact obstruction class or finite-window equation rather than lower
the theorem to analogy.

## Verification Used

Commands used in this pass included:

```bash
sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-246-primary-source-theorem-support-audit.md
sed -n '1,520p' reconstitution/primary-source-theorem-support-audit-2026-04-30.md
sed -n '8848,8874p' main.tex
sed -n '9100,9270p' main.tex
nl -ba main.tex | sed -n '1240,1505p'
nl -ba main.tex | sed -n '1738,1788p'
nl -ba main.tex | sed -n '5200,5468p'
nl -ba theorem-lanes.tex | sed -n '3350,3485p'
nl -ba open-obligations.tex | sed -n '880,1025p'
rg -n "Loday|Tsygan|Quillen|Priddy|Hinich|Hovey|Lefevre|Hormander|Weiss|Ran|Ayala|Francis|Tanaka|Bochner|Martinelli|Koppelman|BMK" main.tex theorem-lanes.tex claim-strength-ledger.tex open-obligations.tex local-dictionary.tex references/source-provenance.md references/primary-sources
```

No web lookup was used.  Existing URLs or DOI/arXiv identifiers above are
taken from local bibliography/source fixtures where present, or are marked
for later verification where not locally anchored.
