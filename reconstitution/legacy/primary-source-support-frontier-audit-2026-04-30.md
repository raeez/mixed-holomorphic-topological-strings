# Primary Source Support Frontier Audit, 2026-04-30

Agent: 323.

Scope: citation adequacy for current theorem surfaces around Costello graph/QME, BMK/Koppelman, Loday-Quillen-Tsygan, Hormander wavefront criteria, Weiss/Ran/stratified descent, and Tate bar-cobar/Quillen model-categorical grammar.  This audit reads source fixtures and manuscript theorem ledgers only.  It makes no TeX edits.

## Executive Verdict

The manuscript is mostly disciplined at the theorem frontier: the strongest local statements are usually carried by internal computation, open-obligation habitats, or conditional recognition criteria rather than by imported citations.  The remaining citation risk is not a false imported theorem so much as an insufficiently explicit source boundary in a few places.

Primary sources are adequate for:

- Universal Costello finite-scale elliptic BV/RG/QME grammar and obstruction language.
- Classical BMK/Koppelman kernel and Dolbeault homotopy formula under its analytic hypotheses.
- Loday-Quillen-Tsygan stable primitive/cyclic homology theorem as a source template.
- Ordinary bar-cobar, Koszul, Quillen equivalence, and model-category grammar in their standard finite or conilpotent settings.
- Weiss/Ran/factorization and stratified factorization-homology vocabulary, descent shapes, and sheafification grammar.
- Hormander microlocal operation criteria as a grammar for restrictions, products, pushforwards, and kernels, with page-level primary verification still incomplete in the fixture.

Primary sources are source template only for:

- Costello-Li flat BCOV/HCS and open-closed BCOV results.  They do not prove the present Hamiltonian mixed HT brane-defect theorem surfaces.
- Classical BMK formulas.  They do not prove cutoff current limits, finite moment projections, collar quotients, arity-two Hamiltonian actions, BV propagators, or Costello graph/QME statements.
- LQT/Tsygan stable Lie homology.  It does not prove finite-window Eulerian projections, the local dg algebra `A_psi`, scalar quotients, or the Dirac/Koszul trace theorem.
- Weiss/Ran/AFT/Boavida-Weiss descent.  These support descent and stratified-factorization grammar, not the manuscript's mixed HT brane-defect prefactorization functor or QME.
- Tate bar-cobar and Quillen references.  These support ordinary and model-categorical grammar, not the manuscript's admissible Tate Hamiltonian envelope without the stated local lower-central, ML, Roos, and continuity checks.

Local first-principles computation must carry:

- The CE/PV coordinate maps, Hamiltonian brackets, reduced kernels, and admissible-completion tests.
- BMK finite-window moment projections and the all-window obstruction vector.
- The stable Eulerian finite-window LQT projection and its scalar quotient.
- The Tate bar-cobar admissibility gates for `g_adm`, completed PBW/Koszul duality, and strict endpoint kernels.
- Current-valued Costello BV kernels, wavefront restrictions, scalar projection lifts, counterterms, graph rows, and QME recognition criteria.
- Moyal/Weyl/radial-parts coefficients and trace normalizations.
- Normal Omega reduction, stratified brane trace states, and any physical large-N trace identification.

## Source Fixture Status

### Costello Graph/QME

Fixtures read:

- `references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md`
- `references/primary-sources/local-costello-bv-kernel-source-anchors-2026-04-30.md`

Adequate support:

- Costello's renormalization book supports finite-scale heat-kernel propagators, regularized BV Laplacians, RG flow, the scale-dependent QME, local functionals, counterterms, and graph-asymptotic obstruction calculus.
- Costello-Li supports BCOV/open-closed BCOV axioms, the use of `H^1` as the anomaly-obstruction degree, and the flat odd-dimensional `gl(N|N)` open-closed BCOV/HCS theorem as an explicit comparison or exclusion datum.

Not supported by citation alone:

- Current-valued targets `D'_c`.
- Bulk-to-defect kernels.
- Hamiltonian brane-defect graph/QME recognition.
- Scalar projection from non-scalar graph distributions.
- The finite-window `H^1` and `lim^1` vanishings required in the manuscript.

Patch frontier:

- `main.tex:7672-7689` is citation-adequate for a universal Costello BV package, provided it remains universal.
- `main.tex:7814-7975`, `open-obligations.tex:585-614`, and `theorem-lanes.tex:3339-3715` must remain local construction/recognition obligations.  No primary source currently proves these Hamiltonian current-valued surfaces.
- `main.tex:2469-2485`, `main.tex:9335-9390`, and `main.tex:9441-9470` are correctly conditional.  Keep the Costello citation as formalism, not as proof of graph realization.

### BMK/Koppelman

Fixture read:

- `references/primary-sources/bmk-koppelman-source-anchors-2026-04-30.md`

Adequate support:

- Laurent-Thiebaut 2011 Definition 1.2 and equation (1.1) support the BMK kernel family and normalization class.
- Laurent-Thiebaut Lemma 1.3 supports the component `\bar\partial_z`/`\bar\partial_\zeta` identity.
- Ruppenthal, Section 5, Theorem 5.2 and equation (10), support the classical BMK/Koppelman homotopy formula for bounded `C^1` domains and `C^1` forms.

Source template only:

- Martinelli, Bochner, and Koppelman historical references currently support lineage only unless exact formula anchors are added.
- Classical BMK sources do not prove the manuscript's cutoff-current, finite-moment, collar-quotient, arity-two Hamiltonian, or BV/QME claims.

Local computation required:

- Orientation/sign matching for the manuscript's `(2\pi i)^{-2}` convention.
- The cutoff current limit.
- The finite-window moment projection.
- The pro-Matlis and all-window obstruction vector.
- Any graph/QME use of the BMK kernel.

Exact TeX patch targets:

- `main.tex:1280-1294`: add one source-boundary sentence after the displayed BMK kernel or before the classical transfer statement:
  - proposed content: "Classical BMK/Koppelman sources supply only the kernel and smooth-domain homotopy formula; the cutoff-current limit, moment projection, and collar quotient below are local constructions."
- `theorem-lanes.tex:481-493`: same boundary should be visible in the BMK lane, especially before the statement is used as a local normal form.
- `main.tex:1420-1425`: if the one-pair analytic identity is kept as a theorem target, state that it is not inherited from BMK references until the collar contraction and diagonal orientation are checked locally.
- Bibliography target `main.tex:9565-9990`: add Laurent-Thiebaut and Ruppenthal BMK entries before any explicit BMK citation is inserted.

### Loday-Quillen-Tsygan

Fixture read:

- `references/primary-sources/lqt-tsygan-source-anchors-2026-04-30.md`

Adequate support:

- Loday-Quillen 1984 Theorem 6.2 supports `Prim H_n(gl(A)) = HC_{n-1}(A)` for unital associative algebras over a characteristic-zero field.
- The symmetric-Hopf-algebra form follows from standard connected graded cocommutative Hopf algebra structure once the primitive theorem is in place.
- Loday-Quillen 1984 Theorem 6.9 supports homological-degree stabilization.
- Tsygan 1983 supports provenance and the primitive/free-cocommutative mechanism, not the manuscript's finite-window formula by itself.

Source template only:

- LQT/Tsygan do not prove the finite-window map `lambda_{LQT,K,L}`, the local dg algebra `A_psi`, the connected single-trace projection, scalar quotient, or any BV/QME statement.

Local computation required:

- The stable Eulerian finite-window projection.
- The explicit scalar quotient and connected single-trace projection.
- The transfer from local Dirac/Koszul data to cyclic traces.

Exact TeX patch targets:

- `main.tex:1955-1984`: the external LQT theorem statement is acceptable.  Strengthen by adding "source template only" language after `\cite{loday-quillen,tsygan}` if the subsequent finite-window theorem might be read as a citation consequence.
- `main.tex:1985-2034`: keep this theorem proof local.  Do not add LQT as a proof citation for the finite-window formula.
- `open-obligations.tex:143-190` and `claim-strength-ledger.tex:376-446`: current conditional/internal classification is adequate.

### Hormander Wavefront Criteria

Fixture read:

- `references/primary-sources/hormander-wavefront-source-anchors-2026-04-30.md`

Adequate support:

- The fixture supports the microlocal grammar: wavefront set, pullback/restriction transversality, tensor/product criteria, pushforward/direct image, and kernel action/composition criteria.

Remaining source gap:

- Several exact page and theorem anchors are still secondary-confirmed rather than primary page-verified.  The source fixture is enough for manuscript grammar, but not enough for exact page-number precision unless those anchors are upgraded.

Not supported by citation alone:

- Graph-by-graph wavefront calculations.
- Scaling-degree or counterterm classification for the present current-valued kernels.
- Scalar-contact quotient.
- Roos or finite-window inverse-limit claims.
- Brane-defect QME.

Exact TeX patch targets:

- `claim-strength-ledger.tex:556-574`: keep Hormander as operation criteria only.  Do not let the ledger imply that Hormander proves the graph-QME branch.
- `open-obligations.tex:594-599`: current placement as an open current/wavefront restriction is correct.
- `theorem-lanes.tex:3616-3637`: keep this as a graph-row habitat and local verification obligation.  Cite Hormander only for the microlocal admissibility tests.

### Weiss/Ran/Stratified Descent

Fixtures read:

- `references/primary-sources/weiss-ran-stratified-descent-source-anchors-2026-04-30.md`
- `references/primary-sources/omega-stratified-source-anchors-2026-04-30.md`

Adequate support:

- Costello-Gwilliam author/preprint anchors support Weiss covers, homotopy factorization algebras, local dg Lie observables, and factorizing-basis extension grammar.
- Boavida-Weiss supports `J_k` sheafification, good covers, and configuration/Ran-style finite-point product grammar.
- Ayala-Francis-Tanaka supports stratified factorization-homology grammar, `Disk(B)` algebras, excision, and continuity.
- The Omega-stratified fixture gives adjacent-model vocabulary only.

Source template only:

- Costello-Gwilliam CUP metadata and local Cambridge mirrors are not enough for exact published theorem/page claims.
- Weiss/Ran/AFT/Boavida-Weiss do not prove the manuscript's mixed HT brane-defect prefactorization functor, collar modules, centrality homotopies, normal Omega trace state, or QME.
- CFG and Costello-M2 style trace comparisons are external related-model templates only.

Exact TeX patch targets:

- `main.tex:3781-3784`: keep the Costello-Gwilliam citation at terminology/vocabulary strength.  Prefer "standard factorization-algebra terminology" over any claim that a published theorem there proves the local current statement.
- `main.tex:3969-3993`: state explicitly that the central operations in this model are local constructions; Weiss/Ran descent supplies only the descent grammar.
- `open-obligations.tex:996-1233`, especially `open-obligations.tex:1227-1233`: current firewall is good.  Preserve it.
- `theorem-lanes.tex:2867-3337` and `claim-strength-ledger.tex:837-889`: keep normal Omega/stratified trace claims as construction obligations, not source-derived consequences.
- Bibliography target `main.tex:9565-9990`: add Boavida-Weiss and Ayala-Francis-Tanaka keys only if the manuscript cites those templates directly.

### Tate Bar-Cobar, Quillen, and Model-Categorical Grammar

Fixture read:

- `references/primary-sources/tate-barcobar-quillen-source-anchors-2026-04-30.md`

Adequate support:

- Priddy supports Koszul/PBW source vocabulary.
- Adams supports classical cobar lineage.
- Quillen 1969 supports rational homotopy DGL/DGC equivalence in its verified Theorem I range.
- Lefevre-Hasegawa supports conilpotent/cocomplete dg coalgebras and bar-cobar Quillen equivalence.
- Hinich supports operadic algebra model structures under its hypotheses.
- Schwede-Shipley supports monoidal model-category criteria, modules, and algebras under monoid-axiom hypotheses.
- Hovey supports the general model-category and Quillen-equivalence grammar.
- Drinfeld supplies Tate vector-space vocabulary.

Source template only:

- These sources do not prove `g_adm`, lower-central Tate pronilpotence of the Hamiltonian algebra, `AdmTateLie_LC`, strict endpoint kernels, completed Hamiltonian envelopes, exact continuous dualization, finite-window ML/Roos vanishing, `P_0` transfer, cyclic trace compatibility, or Costello/QME compatibility.

Remaining source gaps:

- Quillen 1967 exact anchors, Quillen 1969 Part II anchors, published Schwede-Shipley page anchors, Dwyer-Kan original anchors, and Roos/Jensen anchors remain incomplete or absent.
- Roos/Jensen should not be cited for theorem-level inverse-limit statements until anchored.

Exact TeX patch targets:

- `main.tex:5634-5706` and `main.tex:5734-5748`: current proof correctly treats the Tate passage as internal.  If edited, add a short sentence: "The cited bar-cobar sources are ordinary/conilpotent source templates; the Tate inverse-limit and lower-central hypotheses are exactly the local content of the lemma."
- `theorem-lanes.tex:1968-2019` and `open-obligations.tex:102-142`: keep these as local admissibility criteria.  Do not cite ordinary bar-cobar sources as proof of the completed Hamiltonian endpoint.
- Bibliography target `main.tex:9565-9990`: add Adams 1956, Quillen 1969, and Drinfeld 2006 only if they are explicitly cited in the manuscript.  Do not add Jensen/Roos theorem citations until source anchors are upgraded.

## Manuscript Surface Classification

### Adequate As Written

- `main.tex:186-230`: BCOV and bar-cobar are already separated from the present local geometry.
- `main.tex:679-699`: stable large-N admissibility is framed as a target, not as imported theorem.
- `main.tex:1342-1392`: BMK finite-window obstruction vector is internal.
- `main.tex:1955-2034`: LQT template and local finite-window theorem are separated well enough; optional sharpening noted above.
- `main.tex:2469-2485`: Costello graph analytic problem is correctly externalized.
- `main.tex:2501-2522` and `main.tex:2549-2564`: BMK lane status is honest.
- `main.tex:2566-2673`: coordinate CE/PV and admissible Koszul criterion are internal/conditional.
- `main.tex:4129-4153`: coordinate CE/PV theorem carries no overstrong Tate conclusion.
- `main.tex:4526-4655`: unreduced factorization-center lift and Weiss/Ran obstruction are locally stated.
- `main.tex:7621-7702`: Costello/Costello-Li source boundary is clean.
- `main.tex:7755-7975`: kernel, Tate Casimir, and Hamiltonian Costello specialization remain local.
- `main.tex:9127-9202`: reduced open-line Wick theorem is internal.
- `main.tex:9335-9470`: first/third recognition criteria are conditional and source-bounded.
- `theorem-lanes.tex:152-225`, `theorem-lanes.tex:2021-2138`, and `theorem-lanes.tex:2525-2868`: local computations are separated from source templates.
- `open-obligations.tex:1-13`, `open-obligations.tex:420-640`, and `open-obligations.tex:1439-1501`: firewalls are adequate.
- `claim-strength-ledger.tex:1-160`, `claim-strength-ledger.tex:915-945`, and `claim-strength-ledger.tex:1278-1434`: claim strength mostly matches proof strength.

### Needs Source-Boundary Sharpening

- `main.tex:1280-1294` and `theorem-lanes.tex:481-493`: BMK source boundary should be explicit.
- `main.tex:1955-1984`: optional LQT source-template sentence to prevent spillover into the finite-window theorem.
- `main.tex:3781-3784` and `main.tex:3969-3993`: Costello-Gwilliam/Weiss/Ran support should be held to terminology and descent grammar.
- `claim-strength-ledger.tex:556-574` and `theorem-lanes.tex:3616-3637`: Hormander should be stated as operation criteria, not graph-QME proof.
- `main.tex:5634-5706` and `main.tex:5734-5748`: optional Tate source-template sentence if future edits add more citations.

### Must Remain Local First-Principles Theorems Or Open Obligations

- `main.tex:7814-7975`
- `main.tex:9127-9202`
- `main.tex:9335-9470`
- `theorem-lanes.tex:2867-3337`
- `theorem-lanes.tex:3339-3715`
- `open-obligations.tex:102-190`
- `open-obligations.tex:420-640`
- `open-obligations.tex:996-1233`
- `claim-strength-ledger.tex:837-889`
- `claim-strength-ledger.tex:1142-1158`
- `claim-strength-ledger.tex:1278-1434`

No current fixture proves these surfaces externally.

## Bibliography Frontier

Current bibliography support is adequate for Costello, Costello-Li, Costello-Gwilliam, Loday-Quillen, Tsygan, Priddy, Loday-Vallette, Hinich, Hovey, Lefevre-Hasegawa, Lurie, Quillen 1967, Schwede-Shipley, and Hormander.

Bibliography additions should be staged only when the corresponding citation text is inserted:

- BMK/Koppelman: Laurent-Thiebaut 2011 and Ruppenthal 2008 are the strongest exact anchors.  Historical Martinelli/Bochner/Koppelman should remain lineage until exact formula anchors are available.
- Weiss/Ran/stratified descent: Boavida-Weiss and Ayala-Francis-Tanaka may be added for descent grammar.  They should not be cited as proof of the local mixed HT brane theorem.
- Tate bar-cobar: Adams 1956, Quillen 1969, and Drinfeld 2006 may be added for historical/model vocabulary.  Roos/Jensen should wait for exact source anchors.
- External trace/Omega comparisons: Costello-M2 and CFG-style sources are related-model templates only.

## Attack-Heal Ledger

Attack: Can Costello sources prove the present Hamiltonian current-valued QME?

Heal: No.  They provide the universal elliptic BV/RG/QME formalism.  The manuscript correctly lists current-valued targets, wavefront restrictions, scalar projections, and finite graph rows as local obligations.

Attack: Can BMK references prove the finite-window Hamiltonian transfer?

Heal: No.  They support the kernel and classical smooth-domain homotopy.  The finite-window and collar-current statements must be proved locally.  Add a source-boundary sentence at the BMK theorem surface.

Attack: Can LQT/Tsygan prove the stable Eulerian finite-window projection?

Heal: No.  LQT/Tsygan are source templates for stable primitive/cyclic homology only.  The finite-window theorem remains a local computation; the manuscript largely says this already.

Attack: Can Hormander wavefront criteria close the graph-QME wavefront branch?

Heal: No.  They supply operation criteria.  Graph-by-graph admissibility and counterterms are local computations, and some exact page anchors still need upgrading.

Attack: Can Weiss/Ran/AFT descent prove the brane-defect prefactorization or normal Omega trace?

Heal: No.  They supply descent grammar.  The local mixed HT prefactorization, centrality homotopies, QME, and trace state remain construction obligations.

Attack: Can ordinary bar-cobar/Quillen sources prove the admissible Tate Hamiltonian envelope?

Heal: No.  They supply grammar under ordinary/conilpotent/model-categorical hypotheses.  The completed Tate passage is exactly the local theorem content.

## Final Status

No TeX was edited.  The precise citation frontier is:

- external sources may be cited for grammar and standard theorems in their native hypotheses;
- the manuscript's local Hamiltonian, finite-window, current-valued, stratified-brane, and graph-QME claims must be carried by local computation or left as explicit construction obligations;
- the most important patch is a BMK source-boundary sentence near `main.tex:1280-1294` and `theorem-lanes.tex:481-493`.
