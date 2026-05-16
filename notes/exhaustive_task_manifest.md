# Exhaustive task manifest — mixed holomorphic-topological strings

## Scope at the time of generation

| metric | count |
|---|---|
| commits to audit | 433 |
| labeled theorem-blocks | 339 |
| .tex files | 26 |
| section / subsection / subsubsection / paragraph headings | 162 |
| scripts | 29 |
| unique citations | 57 |
| seventeen-site catalogue items | 17 |
| §V voice forbidden patterns | 49 |
| convention-firewall predicates | 17 |
| cross-volume firewall tasks | 10 |
| compute-anchor tasks | 27 |
| bibliography / notation / acronym tasks | 20 |
| adversarial re-audit tasks | 15 |
| **TOTAL deterministic tasks** | **1223** |

Phase A audits will generate additional per-instance subtasks (voice fixes, define-before-use fixes, seventeen-site instances). Estimated subtask expansion: 500–2000.

---

## Phase A — Meta-audits (scan-driven; each produces per-instance subtasks)

| ID | site | action | verification |
|---|---|---|---|
| `A-01` | `all *.tex` | §V hedge-word scan: perhaps|remarkably|crucially|notably|importantly|interestingly|clearly|obviously|we hope|we wish|we want | list with file:line; each → V-NNN |
| `A-02` | `all *.tex` | §V transition-prose scan: we now turn|having established|this section sharpens|in light of|as we shall see|let us now|in what follows | list with file:line; each → V-NNN |
| `A-03` | `all *.tex` | §V structural-label scan: Theorem A|Theorem B|Wave N|Phase j|Round M|matrix microscope|brane microscope|platonic ideal|certificate|manifest|spec|schema | list; each → V-NNN |
| `A-04` | `all *.tex` | is-closely-related-to scan: is closely related to|corresponds to|is the analogue of|is wrong|would be|must not|fails to|is misleading where exact = or ≃ applies | list with proposed exact replacement; each → V-NNN |
| `A-05` | `all *.tex` | define-before-use scan: for each symbol introduced, first-use ≤ definition site | list of (symbol, first-use-line, define-line-or-missing); each missing → D-NNN |
| `A-06` | `all *.tex` | acronym first-use expansion: BCOV BV QME VOA OPE CoHA BKM MNOP DT GW PT MC CE PV HT FA RR NS KK RG SDR KZ BD BPZ hCS GL BMK IR UV PVA | each acronym spelled at first occurrence per file; each gap → D-NNN |
| `A-07` | `all *.tex` | seventeen-site catalogue scan: for each of items 1–17 (CLAUDE.md), grep manuscript for instances of the failed claim | per-item file:line list; each → S-N-NN |
| `A-08` | `all *.tex` | claim-strength scan: every \begin{thm} containing conditional language without an explicit Status. or hypothesis ledger | list; each → CS-NNN |
| `A-09` | `all *.tex` | heuristic-physics-vs-proved-algebra scan: paragraphs mixing \hyp/\stmt/\conj with \thm without separator | list; each → CS-NNN |
| `A-10` | `all *.tex` | orphan-apparatus scan: \label{} not \ref{}d anywhere; \ref{} to missing label | pair of lists; each → O-NNN |
| `A-11` | `main.tex bibliography` | orphan citation scan: \bib{key} not \cite{key}d; \cite{key} to missing entry | pair of lists; each → B-NN |
| `A-12` | `all *.tex` | inline-display alignment: every \label{} on a display referenced exactly the number of times needed (no orphan \eqref targets) | list; each → O-NNN |
| `A-13` | `out/main.log` | LaTeX-warning sweep: Overfull|Underfull|Undefined reference|Multiply defined|Missing character|LaTeX Warning|LaTeX Font Warning | list per warning; each → T-NNN |
| `A-14` | `all *.tex` | cross-volume symbol-match audit: every symbol shared with chiral-bar-cobar Vol I/II/IV, calabi-yau-quantum-groups Vol III, igusa-cusp-form | per-symbol agreement check; mismatches → X-NNN |
| `A-15` | `scripts/` | compute-anchor audit: every script load-bearing output anchored in manuscript with explicit \ref or \eqref | per-script anchor file:line; each unanchored → K-NN |
| `A-16` | `all *.tex` | \cite{costello-gwilliam}*{Vol.~II,...} citation pin verification: every cite resolves to a real CG Vol II theorem/section | per-cite check; mismatches → B-NN |
| `A-17` | `all *.tex` | trace symbol \overline{\operatorname{Tr}} vs \operatorname{Tr}: each occurrence classified reduced-vs-full intent | list with classification; each ambiguous → N-NN |
| `A-18` | `all *.tex` | $d$-vs-$D$ dimension audit: $d=\dim_\C X$ consistency (worldvolume vs target vs factorization-algebra vs brane-codim) | per-occurrence classification; conflicts → N-NN |
| `A-19` | `all *.tex` | $\hbar$ vs $g_s$ audit: each occurrence classified (QFT loop vs string genus) | list; flag conflations → N-NN |
| `A-20` | `all *.tex` | BV-degree / ghost-number / form-degree separation per theorem | per-theorem check; each missing → CV-NN |
| `A-21` | `mathmacros.tex; local-dictionary.tex` | macro and notation orphan scan | list of unused macros and undefined-symbol uses; each → N-NN |
| `A-22` | `all *.tex` | paragraph-by-paragraph prose pass: every paragraph evaluated for §V voice + define-before-use + motivate-before-introduce + claim-strength | one report per file; per-paragraph defects → P-NNN |

---

## Phase B — Per-commit audit (433 tasks)

Each commit gets a voice / claim-strength / math-rigor audit. Any defect introduced or surviving in a commit becomes a surgical-fix subtask in Phase C–N.

| ID | hash | subject |
|---|---|---|
| `B-001` | `e4786f0` | Initial commit |
| `B-002` | `8cdb13f` | first pass |
| `B-003` | `7fe6720` | small progress |
| `B-004` | `2a7ebff` | added section on operators in the gauge theory |
| `B-005` | `1550f9f` | initial sketch of feynman diagram - A_infty op correspondance |
| `B-006` | `82571ac` | CLAUDE.md + AGENTS.md: inherit ~/ecosystem/INVARIANTS.md + ~/ecosystem/AGENTS-HARNESS.md; add research-grade scaffolding (xhigh reasoning, self-reflection rubric, cross-volume constellation, proof-obligation discipline) |
| `B-007` | `efcf195` | topological-strings: wave-1 TS-A frontier inscription — MNOP + S^3-framing + chiral volume + NCCR |
| `B-008` | `7600da2` | W2 V2-A: extend chiral-volume quintic through N=10 + three-path limit convergence |
| `B-009` | `df9d9dd` | topological-strings: W2 TS-B — absolute Fourier-Mukai self-duality on K3 x E under Mukai-vector coprimality |
| `B-010` | `7b828ee` | topological-strings: TS-B W2 — Gopakumar-Vafa non-perturbative closure of CLW BCOV on the quintic through genus 22 |
| `B-011` | `1403d9a` | topological-strings: W2 residual state |
| `B-012` | `37ffd5a` | topological-strings: merge W2 TS-α (CLW non-pert BCOV) + TS-β (K3xE FM self-duality) (7b828ee, df9d9dd) |
| `B-013` | `08424be` | Topological strings frontier MNOP framing volume: correct MNOP factorisation Z_DT = M(-q)^χ · Z_PT, Shenker-Marino growth rate (2g-3)!/A^{2g-2}, S^3-framing via π_2(SO(3))=0 triviality, numerical rectification of the AJ(C_H) mirror identification, conifold n^0_β=1 scope tightening, and new Proposition conifold-trinity-quintic |
| `B-014` | `543a32a` | release pdf |
| `B-015` | `27160c7` | Polish local theorem and release PDF |
| `B-016` | `69c70b6` | release pdf |
| `B-017` | `2ddc67d` | Set topological strings publication date |
| `B-018` | `d35ec51` | Set topological strings date to 2018 |
| `B-019` | `ec15fbc` | Release local Hamiltonian sector repairs |
| `B-020` | `57a5ef6` | Local Hamiltonian closed-open derived center theorem |
| `B-021` | `72af824` | Resolution of the unreduced Tate-coefficient cotangent lift |
| `B-022` | `ed31b3c` | Unconditional closure of the Hadamard parametrix on Mittag-Leffler module |
| `B-023` | `01f2191` | Promote conj:twisted-m-theory-universal to theorem |
| `B-024` | `32bef22` | Platonic-ideal closure: bidirectional cross-volume contract + umbrella post-T5/P1 update |
| `B-025` | `f7681b8` | Chriss-Ginzburg Phase 1: prune dead-code legacy appendix |
| `B-026` | `aec621c` | cg-5-final Phase 3 rectification |
| `B-027` | `9a3c868` | cg-4-quantum Phase 3 rectification |
| `B-028` | `40c93b9` | cg-3-operators Phase 3 rectification |
| `B-029` | `1849048` | cg-2-localmodel Phase 3 rectification |
| `B-030` | `8392644` | cg-1-intro Phase 3 rectification |
| `B-031` | `977e37f` | Chriss-Ginzburg Phase 3: octopus merge of five disjoint-range rectifications |
| `B-032` | `6df6273` | Bibliography audit: zero hallucinations, three concrete fixes applied |
| `B-033` | `b803082` | Total scrub: zero bookkeeping, metaspeak, or narration anywhere |
| `B-034` | `bc41359` | Elite-grade prose scrub: no em dashes, no AI tells, no agent/swarm/ledger references |
| `B-035` | `dff9d0a` | release pdf |
| `B-036` | `682db48` | Phase 4 GREEN convergence: em-dash repair + section opening |
| `B-037` | `7e70df4` | Phase 4 RED convergence: critical proof correctness fixes |
| `B-038` | `d3ce80c` | release pdf |
| `B-039` | `8b9e5ac` | Repair topological strings manuscript |
| `B-040` | `25febff` | Update reconstitution verification plan |
| `B-041` | `117d794` | Wave-5 closure: dangling-thread cleanup and final verifier reports |
| `B-042` | `08bd593` | Record worktree semantic merge audit |
| `B-043` | `f9d49ae` | Regenerate manuscript PDF |
| `B-044` | `3268b61` | Advance universal Koszul duality manuscript |
| `B-045` | `710e073` | Release rectified manuscript |
| `B-046` | `5bd1f2a` | Reconstitute topological strings manuscript |
| `B-047` | `2a2145a` | Set mixed topological-holomorphic title |
| `B-048` | `d1785b8` | Reconstitute mixed HT theorem surface |
| `B-049` | `89eb025` | Separate public manuscript surface |
| `B-050` | `00c9eb3` | release pdf |
| `B-051` | `748e925` | Set mixed holomorphic topological strings title |
| `B-052` | `6285e0d` | Update public manuscript PDF |
| `B-053` | `eb2bab6` | Rectify abstract and Preface, reconstitute cover page |
| `B-054` | `04763ae` | Rectify front matter and promote universal CE/PV recognition theorem |
| `B-055` | `f9ac1d0` | Promote relative filtered CE/PV reconstruction criterion and cobar acceptance |
| `B-056` | `0ba9c6d` | Tighten proof of Theorem 1.32 item (3) using newly promoted theorems |
| `B-057` | `79de35e` | Rectify tate-P1, P3, P5: motivation, BMK firewall, cross-volume labels |
| `B-058` | `6e52974` | Promote open-side A_infty-Koszul acceptance from theorem-lanes |
| `B-059` | `eff2277` | Cleanup: remove legacy aux files and orphaned theorem-lanes scaffolding |
| `B-060` | `91865cd` | Set draft date to April 2018; update published PDF |
| `B-061` | `8a33bd2` | Reconstitute manuscript to chriss-ginzburg-rectify standard |
| `B-062` | `b62a613` | rectify(tate-T5): masthead scope-equivalence and associated-graded identification |
| `B-063` | `87fe07c` | rectify(tate-T2): front-load setup, definitions, and named obstruction triple at opening |
| `B-064` | `65bc06a` | rectify(tate-P1): lift BMK to named no-go theorem with pro-Matlis supremum corollary |
| `B-065` | `9856b26` | rectify(tate-T5): upgrade closing scope from remark to scope theorem |
| `B-066` | `63993eb` | rectify(tate-T4): closure-layer header + BV degree convention + Costello renormalization datum |
| `B-067` | `f5582ff` | rectify(tate-T3): name alpharef placeholders; strengthen Quillen-pair proof |
| `B-068` | `ac9321e` | rectify(tate-T2): strengthen lost-sectors proof with item-by-item argument |
| `B-069` | `3033656` | rectify(appendix-unreduced-bv-qme): add scalar anomaly transgression theorem |
| `B-070` | `207874f` | rectify(tate-T5): define-before-use sweep, Etingof motivation for one-psi complex |
| `B-071` | `4ceab98` | rectify(tate-T3): add explicit compatibility with weighted Tate completion (T1) |
| `B-072` | `2dd9e64` | rectify(appendix-unreduced-bv-qme): finite-window theta_3 H^1 verdict |
| `B-073` | `4c7c3a6` | rectify(principles): elevate to five named organizing principles |
| `B-074` | `90f1f36` | rectify(abstract): unique-survivor reconstruction with named obstruction ladder |
| `B-075` | `0f5c5a3` | rectify(tate-T5): named obstruction repair, prose tic removal |
| `B-076` | `86a1aa0` | rectify(tate-P1): repair Jacobiator computation in BMK no-go proof |
| `B-077` | `f7ee560` | rectify(tate-T1): replace bookkeeping preface with brane-microscope motivation; insert Canonical Habitat Theorem at the climax |
| `B-078` | `2d912b1` | rectify(claim-ledger): add Falsifiability conditions F1-F8 and epistemic-status anchors |
| `B-079` | `e8ead01` | rectify(local-dict): inscribe Kinematic Locality Theorem; reframe entries as comparison morphisms |
| `B-080` | `63a25a2` | rectify(appendix-unreduced-bv-qme): unreduced cotangent lift obstruction theorem |
| `B-081` | `36c3538` | rectify(tate-T2): tighten cocycle-support proof and inverse-limit pronilpotence reuse |
| `B-082` | `65e762f` | rectify(tate-T4): cocycle-resolved hypothesis separation + obstruction tuple representatives |
| `B-083` | `811d7fe` | rectify(tate-P1): tighten supremum proof in pro-Matlis corollary |
| `B-084` | `4b93673` | rectify(tate-P1): add BMK firewall paragraph to opening structural map |
| `B-085` | `54327bc` | rectify(tate-T5): RED audit fixes - sublattice components, centrality semantics |
| `B-086` | `caf86ab` | rectify(tate-T3): correct hypotheses on T1 compatibility; refine Hovey ref |
| `B-087` | `8999e62` | rectify(tate-T2): clarify Moyal residue identity in opening cuts paragraph |
| `B-088` | `87b8ce7` | rectify(tate-T1): chunk 1-2 prose tightening; fix h notation; precise cross-reference for Schouten differential |
| `B-089` | `15f8258` | rectify(appendix-matlis): name Defect Polarization Theorem and architect proof spine |
| `B-090` | `c8db4fd` | rectify(tate-T4): four-input extension criterion with quantum endpoint datum and convention-boundary remark |
| `B-091` | `8da5441` | rectify(tate-T3): tighten unit/counit spectral-sequence argument |
| `B-092` | `7611b4a` | rectify(appendix-unreduced-bv-qme): tighten transgression sighting (iii) |
| `B-093` | `f89a2c3` | rectify(appendix-full-psi): install special-fibre PBW basis, gr Phi morphism, Defect Polarization slogan |
| `B-094` | `d9b9528` | rectify(tate-T1): chunk 5-7 prose, Q_Omega definition; consolidate cotangent-lift theorem as corollary of Canonical Habitat |
| `B-095` | `9098599` | rectify(appendix-unreduced-bv-qme): use paragraph environment for theta_3 header |
| `B-096` | `084cc1a` | rectify(tate-P5): expand acceptance vector, hoist sharp compact-period theorem, add per-target divergence theorems |
| `B-097` | `95a806a` | rectify(tate-T3): forced transition into descendant residual subsection |
| `B-098` | `df4b013` | rectify(appendix-unreduced-bv-qme): elaborate theta_3 script cross-check |
| `B-099` | `f4cb08f` | rectify(appendix-fact-conv): bedrock + three-localities apparatus + convention table |
| `B-100` | `5e6025b` | rectify(tate-T1): expand closing remark to crystallize what was proved and what is forced next |
| `B-101` | `341c9f3` | rectify(tate-P5): Beilinson audit pass — fix wrong cross-ref, drop wrong cite, align lemma to universal/target split |
| `B-102` | `9ed131f` | rectify(appendix-unreduced-bv-qme): align cotangent obstruction descent with abstract (C3) terminology |
| `B-103` | `a19c454` | rectify(tate-P3): universal-property formulation, terminal-object characterization, QME-coordinate dichotomy |
| `B-104` | `15d76cb` | rectify(tate-T1): fix latent aligned environment row separator in regular-density quotient |
| `B-105` | `64aa6d5` | rectify(tate-P5): add Cross-volume firewall sentence-as-theorem and target/coordinate decomposition table |
| `B-106` | `7f21b1c` | rectify(open-obligations): typology, status tags, and five strengthening obligations |
| `B-107` | `e28f1bf` | rectify(appendix-signs): restructure to lead with PBW-vs-Matlis no-go, sharpen proofs |
| `B-108` | `11ec17f` | rectify(appendix-unreduced-bv-qme): strengthen cotangent lift sufficiency proof |
| `B-109` | `0942d2e` | rectify(tate-T1): RED audit fixes — normalize O_f notation, sharpen Casimir-in-B_w_otimes_B_w claim, clarify coefficient-piece counterterm-free |
| `B-110` | `d4dbc9c` | rectify(tate-P5): tighten firewall theorem proof; drop overclaim of coordinate independence |
| `B-111` | `c7a54b6` | rectify(frontier-MNOP): platonic ideal pass with extreme firewall vigilance |
| `B-112` | `467f4e5` | rectify(tate-T1): make minimality condition precise (continuous element of weighted Tate topology) |
| `B-113` | `df1a9a5` | rectify(appendix-radial-Moyal): opening — reframe to all-bidegree structural theorem |
| `B-114` | `ff6b1f2` | rectify(appendix-radial-Moyal): structural all-bidegree theorem via radial bicomplex acyclicity |
| `B-115` | `9facbcc` | rectify(appendix-radial-Moyal): close open frontier and rewire support map |
| `B-116` | `ba65608` | rectify(appendix-radial-Moyal): tighten Step 3 of the bicomplex acyclicity proof |
| `B-117` | `36451d7` | rectify(appendix-radial-Moyal): expand verification remark with Procesi-Razmyslov bidegree list |
| `B-118` | `697c008` | rectify(appendix-radial-Moyal): cross-link stmt:app-quantum-shear-trace-diagram-obstruction and stmt:app-free-kernel-homotopy-obstruction to all-bidegree theorem |
| `B-119` | `d16518f` | rectify(appendix-radial-Moyal): tighten Procesi-Razmyslov argument in Step 3 |
| `B-120` | `64c67e5` | rectify(appendix-radial-Moyal): update thm:app-radial-finite-N proof to cite the structural theorem |
| `B-121` | `d7312f0` | rectify(appendix-radial-Moyal): repair opening — match conditionality of structural theorem |
| `B-122` | `b0e9334` | rectify(appendix-radial-Moyal): polish bicomplex-mechanism remark and mark cubic computational scaling |
| `B-123` | `b9f639f` | rectify(appendix-radial-Moyal): clarify computational-scaling note in verification remark |
| `B-124` | `8f328a2` | rectify(appendix-radial-Moyal): explicit GL_N-symmetrization in Step 3 to extract trace-form lift |
| `B-125` | `54c0780` | rectify(appendix-radial-Moyal): add cor:app-radial-bicomplex-clause3-equivalence to sharpen structural relationship |
| `B-126` | `d327e44` | rectify(appendix-radial-Moyal): support map references the equivalence corollary |
| `B-127` | `be2a114` | rectify(appendix-radial-Moyal): clarify --case invocation in verification remark |
| `B-128` | `61e31dd` | rectify(appendix-radial-Moyal): clarify closure status — two independent fronts |
| `B-129` | `f0610d8` | rectify(appendix-radial-Moyal): correct clause-attribution in proof intro |
| `B-130` | `f6dc7f4` | rectify(tate-T1): integrate Canonical Habitat Theorem |
| `B-131` | `46ab3f4` | rectify(tate-T2): integrate setup front-load and obstruction-triple definition |
| `B-132` | `f9d792d` | rectify(tate-T3): integrate constructive Quillen pair and T1 base-change |
| `B-133` | `d0866b3` | rectify(tate-T4): integrate BV-degree exposition and explicit cocycle representatives |
| `B-134` | `6f4006f` | rectify(tate-T5): integrate scope-iff theorem and primitive-shadow E_1 identification |
| `B-135` | `03796e6` | rectify(tate-P1): integrate BMK no-go theorem and pro-Matlis supremum corollary |
| `B-136` | `f21eb9a` | rectify(tate-P3): integrate categorical universal property |
| `B-137` | `cfea9fd` | rectify(tate-P5): integrate firewall theorem and seven divergence theorems |
| `B-138` | `459d806` | rectify(appendix-radial-Moyal): consolidate route-(ii) bidegree list with reference to verification remark |
| `B-139` | `8b0d348` | rectify(appendix-fact-conv): integrate three-localities convention table |
| `B-140` | `dad0dd6` | rectify(appendix-signs): integrate sign-data verification and reordered lemmas |
| `B-141` | `5faa902` | rectify(appendix-full-psi): integrate gr Phi morphism and Defect Polarization slogan |
| `B-142` | `aef2a3c` | rectify(appendix-unreduced-bv-qme): integrate scalar-anomaly transgression, theta_3 H1, cotangent-lift iff |
| `B-143` | `cf651bb` | rectify(abstract): integrate north-star reconstruction |
| `B-144` | `c94a7f7` | rectify(claim-ledger): integrate falsifiability conditions F1-F8 and epistemic legend |
| `B-145` | `8178eb6` | rectify(frontier-MNOP): integrate firewall vigilance and Picard-Fuchs convention fix |
| `B-146` | `5cc211f` | rectify(local-dict): integrate Kinematic Locality Theorem |
| `B-147` | `7491fdb` | rectify(open-obligations): integrate Status/Witness/Gate tags and five strengthening obligations |
| `B-148` | `a46b910` | rectify(principles): integrate five organizing principles |
| `B-149` | `5b22f7a` | rebuild: refresh published PDF after rectification merge |
| `B-150` | `8cafef2` | rectify(appendix-radial-Moyal): precise the closure-status claim — 'reaches through total degree 15' instead of 'every bidegree of total degree <= 15' |
| `B-151` | `ff6ee43` | rectify(appendix-radial-Moyal): mirror precision to route (ii) of open-frontier remark |
| `B-152` | `3c9856c` | rectify(appendix-radial-Moyal): correct prose description of contraction filtration |
| `B-153` | `1402487` | rectify(appendix-radial-Moyal): replace 'no finite-window appeal' with explicit conditional/unconditional split |
| `B-154` | `4f3cf03` | rectify(appendix-radial-Moyal): integrate radial-bicomplex acyclicity (all-bidegree closure) |
| `B-155` | `219c5df` | descrub(principles): strip bookkeeping wrapper, restore principles as sentences-as-theorems |
| `B-156` | `4667842` | descrub(abstract): strip Proved/Conjectural ledger labels and meta-positioning |
| `B-157` | `59ed4aa` | descrub(appendix-full-psi): strip load-bearing-role opening, what-supports-what remark, citation bookkeeping |
| `B-158` | `0e04b96` | descrub(appendix-matlis): strip apex/spine narration, dependency-map bookkeeping, three-input recap |
| `B-159` | `0a35f0b` | descrub(appendix-unreduced-bv-qme): pass 1 — opening preamble, transgression-branches remark, theta_3 verdict dichotomy, cotangent-lift component locus, drop What supports what |
| `B-160` | `2ee4c4d` | descrub(appendix-signs): strip narrative bridges, opening overreach, forward-citations remark |
| `B-161` | `5e48abd` | descrub(main-local-model): pass 1 — strip emphasized scaffolding, ledger transitions, and self-reference |
| `B-162` | `3d6bca0` | descrub(tate-T2): strip closure-layer wrappers, named-survivor sectioning, ledger tail |
| `B-163` | `b0009d1` | descrub(appendix-fact-conv): strip load-bearing-role opening and what-supports-what remark |
| `B-164` | `2ac9347` | descrub(tate-P1): strip chriss-ginzburg organizing labels and project-status closing |
| `B-165` | `d64d274` | descrub(abstract): integrate stripped Proved/Conjectural ledger and meta-positioning |
| `B-166` | `1953fc3` | descrub(main-mid): strip ledger T/P labels and self-reference in obstruction calculus |
| `B-167` | `86de530` | descrub(tate-T3): strip closure-layer ledger preamble, summary diagram, dichotomy narration |
| `B-168` | `aa39613` | descrub(tate-P3): strip BK1 narration, BK7 universality-residual recap |
| `B-169` | `3f94bec` | descrub(appendix-unreduced-bv-qme): pass 1 (redo) — opening preamble, transgression-branches remark, theta_3 sub-theorem dichotomy, cotangent-lift component locus |
| `B-170` | `c4476e0` | descrub(main-local-model): pass 2 — strip catalogue ID labels, scope-commentary, and self-reference |
| `B-171` | `337ae9f` | descrub(tate-T4): strip closure-layer ledger labels, framing remark, BCOV-positioning |
| `B-172` | `f9956d1` | descrub(frontier-MNOP): strip BK1-BK7 voice across compact-CY3 frontier |
| `B-173` | `e21ef51` | descrub(appendix-radial-Moyal): strip bookkeeping voice from opening, status remark, internal transitions |
| `B-174` | `61fbc50` | descrub(tate-T1): strip meta-narration from opening and theorem lead-ins |
| `B-175` | `b9b512d` | descrub(tate-T5): strip prelude ledger headings, proof bookkeeping, redundant codas |
| `B-176` | `10cc3c9` | descrub(appendix-unreduced-bv-qme): pass 2 — strip residual BK voice in proofs and definitions |
| `B-177` | `f29646f` | descrub(main-local-model): pass 3 — strip section-opener thesis claim, residual self-references, and redundant proof commentary |
| `B-178` | `cf034c7` | descrub(tate-P5): pass-2 polish — drop "named" project-status modifier |
| `B-179` | `d709fb2` | descrub(main-intro): pass 1 -- strip subsection openings, ledger references, decomposition table, and meta-narration paragraphs |
| `B-180` | `b35c5a2` | descrub(main-mid): strip measurement/forcing/comparison paragraph titles, principle and named-obstruction bookkeeping |
| `B-181` | `2b4c782` | descrub(appendix-unreduced-bv-qme): pass 3 — strip residual 'recorded as theorems' framing in theta_3 finite-window H^1 |
| `B-182` | `54a23ed` | descrub(main-late): strip prerequisite-list and forced-transition bookkeeping in late section |
| `B-183` | `73ac3a2` | rectify(abstract): integrate inevitability-theorem citations and kinematic-locality paragraph |
| `B-184` | `0806871` | descrub(appendix-unreduced-bv-qme): pass 4 — strip residual datum/scope BK voice in Omega-equivariant and balanced-extension remarks |
| `B-185` | `f861385` | descrub(main-mid): strip principle-ledger pointers and named-obstruction labels in stratified Koszul list |
| `B-186` | `d1ad08b` | descrub(main-intro): pass 2 -- strip 'in this paper/manuscript' self-references, BCOV/CY firewall framing, and 'Type discipline' label |
| `B-187` | `4b9f1f4` | descrub(appendix-unreduced-bv-qme): pass 5 — final BK1 sweep |
| `B-188` | `7bfc199` | descrub(main-intro): pass 3 -- strip 'manuscript proves', 'studied here', and Dirac-thesis quotation block |
| `B-189` | `6373380` | descrub(open-obligations): mathematical voice for status tags and obligation prose |
| `B-190` | `420dc57` | descrub(main-intro): pass 4 -- remove recap meta-narration in three-localities, mixed h-t strings, and BMK proposition |
| `B-191` | `b3ab423` | descrub(main-mid): second pass strip residual subsection-assembly and forced-transition prose |
| `B-192` | `62947bc` | descrub(main-intro): pass 5 -- final hostile audit, drop residual self-references in two-algebras transitions and Hamiltonian sector opener |
| `B-193` | `0260153` | descrub(main-mid): remove Layer 4 ledger label from PBW/Rees source remark |
| `B-194` | `df46d0d` | descrub(main-intro): pass 5b -- retitle Label-collision discipline paragraph |
| `B-195` | `25c32fb` | descrub(main-mid): re-strip Four mathematical entries forward summary that returned |
| `B-196` | `427357a` | rectify(main-mechanism): integrate inevitability-theorem citations across the seven principles |
| `B-197` | `9345e0a` | descrub(main-intro): pass 5c -- strip 'recorded next' forced transition |
| `B-198` | `b1c10d2` | rectify(claim-ledger): cite inevitability theorems refuted by F1-F8 |
| `B-199` | `5ba726e` | descrub(main-intro): integrate Introduction descrub |
| `B-200` | `56d4b57` | descrub(main-local-model): integrate Local Model section descrub |
| `B-201` | `5e49ba9` | descrub(local-dict): integrate dictionary descrub |
| `B-202` | `0df8c52` | descrub(tate-T2): integrate closure-layer descrub |
| `B-203` | `b31234f` | descrub(tate-T3): integrate ledger-preamble descrub |
| `B-204` | `e06b5bd` | descrub(tate-P3): integrate (keep wave-1 universal-property; descrub diff vs master baseline subsumed) |
| `B-205` | `7a48ef2` | descrub(appendix-fact-conv): integrate (keep wave-1 three-localities apparatus) |
| `B-206` | `f2e6216` | rebuild: refresh PDF after descrub merges |
| `B-207` | `55c22c7` | rectify(local-theorem): cite seven wave-1 inevitability theorems across the local theorem narrative |
| `B-208` | `a8e4926` | rectify(scalar-anomaly): cite four-sightings transgression theorem at the subsection opening |
| `B-209` | `10e8e40` | rectify(cotangent-spine): cite canonical weighted-Tate habitat in admissibility paragraph |
| `B-210` | `24c3794` | rectify(obstruction-calculus): link 8-component body decomposition to 4-component IFF theorem and primitive-shadow E_1 page |
| `B-211` | `2694b66` | rectify(bmk-prop): cite no-go theorem and pro-Matlis supremum in proof of Hamiltonian-flow leak |
| `B-212` | `f64e1f0` | rectify(stratified-koszul): cite canonical habitat, defect polarization, BMK no-go, theta_3 verdict, radial acyclicity, cotangent-lift IFF across the seven layers |
| `B-213` | `3eb6338` | rectify(three-localities): full vol2 skill pass — omega cross-ref to lem:omega-cocycle, dict-kinematic-locality citation closing the proposition |
| `B-214` | `073649b` | rectify(two-algebras): wave-1 inevitability citations across the open/closed comparison |
| `B-215` | `71d18c9` | rectify(mixed-ht-strings): bind quantum extension to weighted-Tate canonical habitat |
| `B-216` | `8e50113` | rectify(concrete-dictionary): bind u -> O_{k,l} to formal-local universal property |
| `B-217` | `e8f9071` | rectify(setup): bind matrix-microscope habitat uniqueness to wave-1 inevitability anchors |
| `B-218` | `10c783c` | rectify(closed-mixed-Hamiltonian): bind cotangent polarization to defect-polarization inevitability |
| `B-219` | `29c2006` | rectify(open-brane-operators): bind Capelli/Lie/trace/Moyal four-window detection to scalar-anomaly transgression |
| `B-220` | `7093491` | rectify(dictionary-binding): bind local-dictionary into main and repair dead Dirac-thesis citation |
| `B-221` | `6e7c062` | rebuild: refresh published PDF after vol2 linear sweep |
| `B-222` | `8932f29` | rename(disk -> polydisk): correct two-complex-dimensional habitat naming throughout |
| `B-223` | `c23837e` | clarify(psi-introduction): make antifield independence and Koszul-resolution role explicit |
| `B-224` | `aadbefd` | rectify(abstract): reconstitute around measurement-principle thesis with define-before-use discipline |
| `B-225` | `3e5a00e` | gitignore: drop blanket /out/ ignore so built PDFs can be tracked |
| `B-226` | `3b7bdc1` | reconstitute(front-matter): mechanism opener, status table, curve-VOA fbox, kernel-correction window extension |
| `B-227` | `a3d426c` | reconstitute(introduction): five-level CE/PV ladder, type-discipline lemma, three running examples, curve-VOA in abstract |
| `B-228` | `4b2491e` | reconstitute(local-model-A): J(f) flagship paragraph, type-discipline remark, five-rung ladder, Matlis residue early |
| `B-229` | `e1fad4c` | reconstitute(local-model-B): measurement-test framing, scalar-anomaly leadoff, obstruction template, kernel-correction window extension |
| `B-230` | `cf94650` | fix(merge-residue): remove leftover conflict markers from kernel-correction list |
| `B-231` | `0632e47` | rectify(define-before-use): inline glosses across appendix and tate files |
| `B-232` | `b243d64` | rebuild: refresh out/main.pdf after rectify-swarm integration |
| `B-233` | `b08b270` | scrub(abstract,local-dictionary): math-and-physics-only, no metanarration |
| `B-234` | `e3a1ff0` | rebuild: refresh main.pdf at root after metanarration scrub |
| `B-235` | `99f24f7` | scrub(metanarration): remove curve-VOA disclaimers, native/habitat poser labels, CY external-comparison framing |
| `B-236` | `77ca0cd` | scrub(habitat,native): replace poser-language with positive math statements |
| `B-237` | `5f2dbe4` | reconstitute(preface): drop principle markers, dictionary header, status preamble |
| `B-238` | `c1d6aae` | fix(notation,locality): δ(t-s)→δ(t-t') brane-line contact kernel; clarify derived zero-fibre |
| `B-239` | `ee56b68` | scrub(local-dictionary,principles,abstract): drop residual native/habitat poser language |
| `B-240` | `7c6c2ba` | scrub(appendix-factorization-current-conventions): drop native poser, rename convolution Hom complex |
| `B-241` | `5357dd3` | scrub(appendix-unreduced-bv-qme): drop habitat/native poser; rename Definitions |
| `B-242` | `2411155` | scrub(tate,reader-route): drop habitat/native poser across T1, T3, T4, P1, P5, reader-route |
| `B-243` | `3c547f9` | scrub(intro,microscope-obstruction): drop "not papered over" rhetorical tail |
| `B-244` | `f01a3a5` | add(reproducibility-certificate): document finite-certificate verification protocol |
| `B-245` | `eafa640` | move(cross-volume-firewall): place tate-P5-cross-volume in appendix block |
| `B-246` | `25eecbe` | scrub(defensive-language): drop "is not asserted" / "no X is asserted" hedges |
| `B-247` | `390bfe6` | add(out): track built frontier_mnop_framing_volume.pdf |
| `B-248` | `3e1675c` | fix(reproducibility-certificate): retract overclaimed SHA-256 and curated bidegree list |
| `B-249` | `1877dd8` | rectify(abstract,preface,intro,local-model): five-phase end-to-end pass |
| `B-250` | `7dd5628` | rectify(abstract,intro): define-before-use discipline through §1.7 |
| `B-251` | `9465df6` | deformation-theory(obstruction-twist,algorithms,closing-thesis): route named classes through Theorem G.1, add Algorithms appendix, sharpen modular and cross-volume firewall |
| `B-252` | `e435f2c` | rectify(abstract): unique-survivor narration with explicit Theorem A/B sequencing |
| `B-253` | `53a92f9` | rectify(manuscript): strike meta/bookkeeping, channel Russian-school + math-physics voice |
| `B-254` | `8aff4d5` | release pdf |
| `B-255` | `06bda94` | rectify(abstract,matrix-microscope,locality-spine,obstructions): brane as Chan--Paton representation; explicit mixed-HT factorization spine |
| `B-256` | `6b2345c` | release pdf |
| `B-257` | `3fc5733` | rectify(manuscript): positive construction across every register; eliminate prohibitive/admonitory framing |
| `B-258` | `eeda8a0` | rectify(abstract,intro): string-theoretic preamble; positive Hamiltonian-coherence phrasing on pro-Matlis tower |
| `B-259` | `0b85f0b` | rectify(abstract,intro): platonic-ideal reconstitution in Witten-Etingof-Costello-Gaiotto-Beilinson register |
| `B-260` | `8880dd2` | rectify(local-dictionary,principles): host-category bedrock + principle compression seven->five |
| `B-261` | `895b5c3` | release pdf |
| `B-262` | `0066cd6` | rectify(intro,dictionary): name both Costello-Gwilliam and Beilinson-Drinfeld presentations of the bulk |
| `B-263` | `4236c56` | rectify(abstract,preface,intro): chriss-ginzburg-rectify v2 five-phase cycle on the bedrock |
| `B-264` | `7c17de2` | voice(manuscript): strip principles slogan layer, matrix-microscope branding, closing-thesis box |
| `B-265` | `a770857` | rectify(closed-to-open,radial,voice): explicit theta_f construction; range distinction; bookkeeping purge |
| `B-266` | `fca2031` | rectify(template,abstract,main,appendix): em-dash ligature template fix; absorb referee critique |
| `B-267` | `836488a` | rectify(summary,abstract): tighten Russian-school voice; lemma θ_f(O_g)=O_{f,g}; QME as obstruction |
| `B-268` | `7190684` | rectify(main,appendix,tate-P1): absorb 9-point referee critique |
| `B-269` | `57cf00a` | rectify(manuscript): voice-rectification sweep; ~950 line net reduction; 442pp PDF |
| `B-270` | `649667e` | rectify(chapter-1): formal-Darboux stalk opener; remove forbidden vocabulary; preserve Gate 2 inline definitions |
| `B-271` | `d9d17fb` | rectify(integration): merge worktrees C3 (Dirac brane / derived commuting variety), C5 (CE/PV Koszul resolution main.tex hooks), C7 (obstruction calculus four-curvature taxonomy in main.tex), C8 (pro-Matlis subsection in body), C11 (frontier section + three open problems + closing sentence), X-D (define-before-use main.tex Theta_loc/K_T/F_T inline) onto master.  Inline bar A definition added in Summary at first use. |
| `B-272` | `0509d9a` | rectify(chapter-10): W_inf[lambda] / E_inf admissible endpoint conditional theorem; H1-H4 hypotheses; bibliography |
| `B-273` | `9eb3862` | rectify(conventions): body convention subsection; theorem-control predicates; appendix anchoring |
| `B-274` | `f949714` | rectify(integration): inscribe Capelli theorem + four-curvature taxonomy primary label + six-coordinates corollary |
| `B-275` | `b26c0c1` | rectify(voice): seventeen-site sweep; forbidden vocabulary across manuscript; label aliases |
| `B-276` | `72593d3` | rectify(integration): add four-curvature primary label; absorb C6's tate-T4 + appendix-unreduced-bv-qme cross-references to Capelli theorem |
| `B-277` | `f397056` | rectify(chapter-4): trace map (not measurement); chart vs primitive; canonical J form; globalization disclaimer |
| `B-278` | `ea525ad` | fix(integration): resolve final cherry-pick conflict marker in main.tex Sec.~1.5 — keep C4's chart/A_b framing with X-V's renamed lem:formal-stalk-trace label |
| `B-279` | `041cebb` | rectify(chapter-9): examples subsection (Heisenberg, KM, beta-gamma, Vir, W_N, C^3, K3, K3xE, CY3); bibliography |
| `B-280` | `1e98a9e` | rectify(chapter-9): inscribe Examples subsection (Heisenberg, KM, beta-gamma, Vir, W_N, C^3, K3, K3xE, CY3) before W_inf endpoint with vocab-cleanup applied |
| `B-281` | `0114a6c` | rectify(structure): chapter openings/closings; inter-chapter transitions; platonic law |
| `B-282` | `f02f7f3` | rectify(structure): hoist Chapters 7-8 from appendix into body; promote Examples + W_inf to body sections |
| `B-283` | `1908adc` | rectify(voice): remove unreferenced microscope-aliased labels (clean body of forbidden-vocab artifacts; aliases had 0 cross-references) |
| `B-284` | `0f2dfc5` | voice(rectify): delete disclaimer/negative-framing per §V.F prohibited rhetorical patterns |
| `B-285` | `2c5b113` | rectify(structure): move tate-T4 BV vanishing into Chapter 6 (Capelli) area; move tate-P1 Hadamard-Mittag-Leffler into Chapter 8 (pro-Matlis) area |
| `B-286` | `a0f0422` | voice(rectify): delete all disclaimer/no-compact-theorem-asserted patterns |
| `B-287` | `ea31ede` | rectify(structure): deduplicate Chapter 2 \section / \subsection title collision ("The shifted-cotangent BF Lie algebra" was both); preserve ssec:hamiltonian-bf-algebra label on the \section header |
| `B-288` | `715fcf1` | voice(rectify): replace 'trace measurement' / 'brane measurement' (non-standard) with 'trace map' / 'trace functional' across main.tex (10 occurrences); replace Summary 'is not proved here' disclaimer with positive matched-conventions statement |
| `B-289` | `4cac3ad` | voice(rectify): rewrite §1.3 'Three notions of locality' opener — replace negative-framing 'is not one notion / it is three' with positive declarative naming three independent locality differentials |
| `B-290` | `03cadca` | rectify(structure): reorder Chapter 1 subsections to platonic narrative flow |
| `B-291` | `685bf0a` | voice(rectify): replace 'corresponds to' with positive identification ($↦$ / 'is a') at 3 instances in main.tex; was approximation language for exact map (§V.G) |
| `B-292` | `fdf57db` | voice(rectify): convert binding-conventions 'is not a compact CY_3 assumption, not a BCOV theorem, not a license' enumeration to positive 'external programmes governed by firewall + acceptance class' construction (§V.F) |
| `B-293` | `748e833` | voice(rectify): rewrite remark titles 'is not' -> 'vs' (positive labeling); both rmks (Gwilliam-Williams and Same-rank deletion) now name the contrast directly per §V.F |
| `B-294` | `4972d23` | rectify(structure): hoist tate-P5-cross-volume out of appendix into body (matched-conventions transport theorem with 36 cross-references is load-bearing); inscribe \input{appendix-completion-blueprint} (orphan file never included before, 1955 lines of supremum-discipline construction) |
| `B-295` | `62b295d` | rectify(structure): demote tate-P5-cross-volume.tex top \section -> \subsection and reposition input before Acknowledgements; the cross-volume firewall now nests as the closing subsection of Chapter 11 (The frontier), giving exactly 11 numbered chapters at body level matching the platonic ideal |
| `B-296` | `81c3d33` | rectify(structure): move 'The closing identification' platonic-closer paragraph AFTER cross-volume firewall, so it is the LAST content of Chapter 11 before Acknowledgements; the closing sentence (J = formal coordinate; three open problems made well-posed) now closes the manuscript per CLAUDE.md |
| `B-297` | `c517cfa` | voice(rectify): remove §V.H 'certificate' (CS-jargon) from local theorem statement, replace with 'closure'; remove 'Dirac probe' (forbidden probe-vocabulary) at 2 instances, replace with 'Dirac brane sector' / 'Dirac brane stack' per CLAUDE.md |
| `B-298` | `912f968` | rectify(structure): rename Chapter 7 subsection 'Obstruction--twist dichotomy' -> 'Four-curvature taxonomy and six-coordinate classification' to match the actual content (4 cells + 6 coordinates, not a 2-way dichotomy); preserves ssec:master-deformation-dichotomy label |
| `B-299` | `ed1b249` | rectify(structure): cross-link Summary's conditional-on-Ob_cent/QME/desc to Appendix completion-blueprint, where the supremum construction discharges the obstruction vector with chosen null-homotopies; lifts the conditional toward unconditional per CLAUDE.md supremum discipline |
| `B-300` | `9249d63` | voice(rectify): replace 'polynomial measurement' / 'formal measurement' (as noun for J) with 'polynomial trace map' / 'formal trace map' in the Chapter 1 platonic opener; J is the trace map, not the methodology of 'measuring' |
| `B-301` | `0d3d889` | voice(rectify): replace remaining noun-form 'measurement' with standard terminology — trace character map, moment-map evaluation, scalar functionals, quantization map, evaluations; rmk title 'operation and measurement' -> 'operation and evaluation'; cleared 5 non-standard usages while preserving theorem labels (thm:brane-measurement-principle remains for backward compat) |
| `B-302` | `7a209ee` | rectify(notation): spell out acronyms at first occurrence per §VI — Poincaré-Birkhoff-Witt (PBW) at line 338; (BCOV), (OSV), (GV), (MNOP), (CoHA), (BKM) at line 426 in the binding-conventions enumeration; Kato-Nakayama (KN) at line 491 |
| `B-303` | `227e7e5` | rectify(notation): introduce (BCOV) abbreviation at first occurrence (Summary line 102) where the full Bershadsky-Cecotti-Ooguri-Vafa name appears; remove redundant re-spell-out at line 426 |
| `B-304` | `774373a` | voice(rectify): replace Chapter 8 (pro-Matlis) opener's negative-framing 'is not a free choice / are not another copy of polynomials' with positive declarative naming the polynomial trace classes (Taylor) and the conjugate residues (top local-cohomology) directly per §V.F |
| `B-305` | `db1042a` | voice(rectify): replace 'trace measurement' / 'brane measurement' (non-standard noun) with 'trace map' across all body files (appendix-algorithms, appendix-master-deformation-complex, appendix-radial-parts-moyal, appendix-completion-blueprint, plus several tate-* files); standard terminology per CLAUDE.md voice register |
| `B-306` | `a787f91` | rectify(notation,voice): inline define A_b=End(b) at first use in Summary's binding-conventions paragraph (was used without prior definition until Chapter 3); replace 'not a compact BPS Hilbert space' disclaimer with positive forward-pointer to the operator-level lift open problem (ssec:open-modular-lift); §V.F + §VI define-before-use |
| `B-307` | `50e1695` | rectify(notation): replace 'Definition~\\ref{ssec:master-deformation-target}' with '\S~\\ref{...}'; the label is on a \subsection, not a definition |
| `B-308` | `550dff1` | rectify(structure): trim Chapter 4's opener — replace redundant restatement of primitive open object / chart A_b (already introduced in Chapter 3) with a forward-reference to sec:derived-commuting-variety; chapter focuses on its own content (the trace map J) rather than re-introducing the chart |
| `B-309` | `d93a9ca` | voice(rectify): rewrite Chapter 1 'Setup' subsection opener — replace non-sequitur 'The trace substitution fixes the geometry' with direct statement of the gl_N-valued Heisenberg pair and brane symplectic form, then the trace functional J that reads it; Witten/Etingof voice opens with the first mathematical object |
| `B-310` | `54487f1` | voice(rectify): abstract Hamiltonian-on-brane sentence — replace awkward intransitive 'measures on the brane as' with grammatically tighter 'is read on the brane as'; J is the trace map |
| `B-311` | `5f2f89d` | voice(rectify): replace 'we get c_{a+1,b}=c_{a,b}' with 'the equality holds when' (no first-person hedging) |
| `B-312` | `544ca93` | voice(rectify): replace 'we get v=0' in tate-P5 with 'gives v=0' — no first-person plural |
| `B-313` | `6b5c7f6` | rectify(notation): replace 'Appendix~\\ref{app:convention-contract}' with '\S~\\ref{ssec:cross-volume-firewall}' — tate-P5 was demoted to a subsection of Chapter 11 in earlier restructure, so the 'Appendix' prefix no longer matches |
| `B-314` | `934d74a` | rectify(notation): two more 'Appendix~\\ref{app:convention-contract}' -> '\\S~\\ref{ssec:cross-volume-firewall}' fixes (lines 414, 14595); tate-P5 is now a subsection of Chapter 11, not an appendix |
| `B-315` | `0c21eef` | rectify(notation): replace 'Appendix~\\ref{app:master-deformation-complex}' / 'Appendix~\\ref{sec:app-matlis-principal-parts}' with body \S~\\ref forms (sec:obstruction-calculus, sec:pro-matlis-target); these were hoisted from appendix to body Chapters 7-8 in earlier restructure |
| `B-316` | `9d3b0fd` | voice(rectify): replace 'separates canonical motion from measurement' with 'from evaluation' — measurement-as-noun avoided per voice register |
| `B-317` | `1b620fe` | voice(rectify): rename J 'brane trace measurement' -> 'brane trace map' and 'quantum measurement' -> 'quantum trace map' in the three-operations passage; J is the trace map, period |
| `B-318` | `8ef1795` | voice(rectify): 'compatibility of Weyl ordering with brane measurement' -> 'with the brane trace map' (line 4365) |
| `B-319` | `dd9d66f` | voice(rectify): notation-table column headers — '(measurement)' -> '(boundary observable)' for u_I and '(trace observable)' for O_{a,b}; matches the description prose and avoids non-standard 'measurement' as type label |
| `B-320` | `5980c0b` | voice(rectify): replace 'explicit measurements' / 'disjoint independent measurements' with 'smeared trace evaluations' (matches the actual mathematical content — pairings of test functions with the trace map) |
| `B-321` | `3109093` | voice(rectify): final 'measurement' noun cleanups in Capelli quantum-test prose — 'measurement compatibility' -> 'trace-map compatibility'; 'measured commutator' -> 'trace commutator'; 'brane-measurement test' -> 'brane trace-map test' |
| `B-322` | `470dc8f` | rectify(structure): Chapter 3 first subsection 'The Dirac brane' -> 'The Dirac brane stack' with new label ssec:dirac-brane-stack; aligns with chapter title 'The derived commuting variety stack at N Dirac branes' |
| `B-323` | `49c9745` | rectify(structure): rename Chapter 8 subsection 'The pro-Matlis target' -> 'Native home of the four-curvature taxonomy'; the parent \section is already 'The pro-Matlis target...', so subsection title was redundant; new title states the subsection's actual content (four-curvature taxonomy lives in the pro-Matlis target) |
| `B-324` | `60c1e89` | rectify(structure): add Chapter 1 closing crystallization — names the configuration and forces Chapter 2's BF Lie algebra construction; per CLAUDE.md 'closes by crystallizing what was proved and forces what comes next' |
| `B-325` | `73c5be1` | rectify(voice): Chapter 1 closing — remove meta-narration 'the next chapter constructs'; Chapter 2 closing — add positive math-statement crystallization (closed BV theory IS the BF theory; open BV theory IS the derived commuting variety) without 'the next chapter X' phrasing per Witten/Etingof voice |
| `B-326` | `77ab33b` | fix(latex): \Spf was undefined macro; replaced with \operatorname{Spf} (formal spec) at line 592 |
| `B-327` | `ddc843f` | rectify(structure,refs): inscribe rewritten abstract opener (formal-Darboux stalk chart definition first), fix dangling references in appendix-completion-blueprint |
| `B-328` | `827a8c2` | rectify(structure): add Chapter 2 closing crystallization — names the closed BV theory (Hamiltonian BF on \widehat{\C^2}_0 with master action), forces Chapter 3's open derived commuting variety; pure mathematical statement, no meta-narration |
| `B-329` | `13f6ba9` | rectify(structure): add Chapter 3 closing crystallization — names the open BV sector (derived commuting variety with BV differential Q psi = [phi_1, phi_2]) and forces Chapter 4's trace map J(f) = Tr f(phi_1,phi_2) and its CE-coordinate expression |
| `B-330` | `f61241d` | rectify(structure): add Chapter 4 closing crystallization — names J as the unique linear GL_N-equivariant Darboux-natural single-trace map; states the CE/PV dictionary c_f mapsto theta_f, u_f mapsto J(f); forces Chapter 5's Koszul-resolution identification of the chiral Hochschild cohomology |
| `B-331` | `62aef12` | rectify(structure): add Chapter 5 closing crystallization — names the Koszul-resolution identification (climax of Chapter 5: dictionary IS the Koszul resolution of C^bullet_ch(A_b,A_b)) and forces Chapter 6's U(1) centre-of-mass cocycle / Capelli scalar |
| `B-332` | `78736e7` | rectify(structure): add Chapter 6 closing crystallization — names the Capelli scalar = projective curvature of modular line bundle (climax of Chapter 6) and forces Chapter 7's master deformation complex / four-curvature taxonomy |
| `B-333` | `158e50c` | rectify(structure): add Chapter 7 closing crystallization — names the four-curvature taxonomy and six-coordinate classification, observes they live natively on the inverse limit of finite Matlis windows, forces Chapter 8's pro-Matlis target |
| `B-334` | `e751ba6` | rectify(structure): add Chapter 8 closing crystallization — states what is proved through Chapter 8 (formal-Darboux stalk + six-coord obstruction + pro-Matlis target) and forces Chapter 9's tests at the central brane vacua |
| `B-335` | `e5a8a46` | rectify(notation): Chapter 9 \section{Examples} carries label sec:examples (matching env type) plus ssec:examples preserved for backward-compat |
| `B-336` | `2aec52c` | rectify(refs): add 5 missing bibliography entries (Eilenberg-Steenrod foundations, Kothe topological vector spaces, Getzler-Jones operads, Brown twisted tensor products, Crainic perturbation lemma) and update 3 cite keys to existing bib entries (loday-vallette-algebraic-operads -> loday-vallette, hormander-vol3 -> hormander-vol1, kontsevich-soibelman-deformation -> kontsevich-dq) so all citations in appendix-completion-blueprint resolve |
| `B-337` | `9de9340` | fix(cite): remove duplicate hormander-vol3 cite (only hormander-vol1 in bib) |
| `B-338` | `becfe99` | rectify(opening): name Mixed Holomorphic-Topological Deligne conjecture explicitly as the d=2 extension of the chiral Deligne theorem proved at d=1; stronger Witten/Etingof framing of what is conjectured globally vs what is proved at the formal-Darboux stalk; abstract tightens open-string E_1 brane algebra description (Chevalley-Eilenberg cochain of Chan-Paton gauge Lie algebra with Koszul differential) |
| `B-339` | `b5b90b7` | rectify(example): K3xE deepened to demonstrate load-bearing theoretical ramifications |
| `B-340` | `da69673` | rectify(example): Vir_c deepened to demonstrate algebraic-HT 3d-gravity ramifications |
| `B-341` | `783dabe` | rectify(examples): C^3 and K3 deepened to demonstrate cross-chapter ramifications |
| `B-342` | `cff5243` | rectify(example): W_N deepened with explicit higher-spin currents and Capelli at parafermion central charge |
| `B-343` | `f4c159a` | release(pdf): rebuild after reinvisioning — Definition repair, title, Capelli three faces |
| `B-344` | `d1fe64f` | fix(citations): regression in fateev-zamolodchikov-conformal and nekrasov-instanton-counting introduced during W_N/C^3 deepening; drop fateev cite (formula is standard) and use existing nekrasov-schwarz-noncommutative for C^3; restore kontsevich-dq key in completion-blueprint |
| `B-345` | `5be9492` | rectify(voice): eliminate all anthropomorphism residue across body |
| `B-346` | `8f57b3d` | rectify(examples): four-curvature cell labels for Heisenberg, affine Kac-Moody, beta-gamma examples |
| `B-347` | `109e3d6` | release(pdf): rebuild after example deepening pass |
| `B-348` | `735c96a` | rectify(ch6-7-bridge): hoist all-bidegree Capelli identity from radial-parts appendix into Chapter 6 close |
| `B-349` | `a95474a` | rectify(ch5): inevitability lift in CE/PV opening — load-bearing dictionary first |
| `B-350` | `87385de` | voice(abstract): name $\phi_1,\phi_2$ as transverse positions, not bare substitution |
| `B-351` | `edefa7a` | rectify(ch4): inevitability lift in Chapter 4 opening — load-bearing trace map first |
| `B-352` | `5a52bee` | rectify(ch9-ch10): closing crystallization of Examples forces W_inf chapter |
| `B-353` | `117f3a8` | voice(setup): name $\phi_1, \phi_2$ as transverse position / brane motion across body |
| `B-354` | `c8b60be` | rectify(ch9): eliminate redundant opening duplicating Ch8 transition |
| `B-355` | `c8afe8a` | rectify(ch7): inevitability lift of Chapter 7 opening — load-bearing four-curvature taxonomy first |
| `B-356` | `7382968` | rectify(voice): eliminate residual probe vocabulary across body |
| `B-357` | `33ddc49` | release(pdf): rebuild after Chapter 4-7 inevitability lifts and probe vocabulary cleanup |
| `B-358` | `f844391` | release(pdf): rebuild including higher-factorization-categories appendix |
| `B-359` | `b945653` | fix(syntax): repair malformed end-tags in appendix-higher-factorization-categories |
| `B-360` | `d861595` | release(pdf): rebuild after syntax fix in higher-factorization-categories appendix |
| `B-361` | `bdb1ede` | release(pdf): final state with higher-factorization-categories appendix integrated |
| `B-362` | `321f423` | rectify(ch6,ch1): harmonize three faces / four equivalent sightings of [bar c] and rename awkward 'Setup' subsection inside chapter 'The setup' |
| `B-363` | `bdb43e8` | rectify(ch7,ch8): eliminate redundant subsection-under-section-title duplication |
| `B-364` | `6ec1718` | release(pdf): rebuild after Ch7/Ch8 subsection rename |
| `B-365` | `57f2c58` | rectify(ch9): replace undefined 'cyclic-collapsed quotient' shorthand in Heisenberg example |
| `B-366` | `8d086f0` | release pdf |
| `B-367` | `e616c54` | rectify(voice): replace internal 'supremum form/construction' jargon with mathematical names |
| `B-368` | `6326e0a` | release(pdf): rebuild after supremum-jargon cleanup |
| `B-369` | `3c20544` | rectify(structure): demote two tate \\section* to \\subsection* — they sit inside Chapters 5 and 6 and should not pose as top-level sections |
| `B-370` | `d98c5ea` | rectify(structure): demote tate-T1 \\section* to \\subsection* — sits inside Ch5 |
| `B-371` | `1fc1671` | release(pdf): rebuild after tate file structure repair |
| `B-372` | `478a659` | rectify(title-page): inscribe 'the formal-Darboux stalk of the Mixed Holomorphic-Topological Deligne conjecture' on the title page |
| `B-373` | `5605d68` | release(pdf): title page now names formal-Darboux stalk of Mixed HT Deligne conjecture |
| `B-374` | `2fe9333` | rectify(voice): eliminate two residual first-person 'we' occurrences in body |
| `B-375` | `827e6d8` | release(pdf): rebuild after first-person 'we' cleanup |
| `B-376` | `80f3cff` | rectify(voice): eliminate residual first-person 'we' in tate-P1 and appendix-completion-blueprint |
| `B-377` | `9ba27f1` | release(pdf): rebuild after second voice cleanup wave |
| `B-378` | `3219d1f` | rectify(titles): harmonize appendix titles to sentence case |
| `B-379` | `29b5a5b` | release(pdf): rebuild after appendix title-case harmonization |
| `B-380` | `e1c8852` | rectify(abstract): attribute the d=1 chiral Deligne proof and specify algebraic curves |
| `B-381` | `bbb5a54` | rectify(major): clarify E_1/E_2 chiral centre framing — A_b is a coordinate ring without inherent chiral structure |
| `B-382` | `90e6a53` | CLAUDE.md + AGENTS.md: §XIII code-writing-discipline repo application |
| `B-383` | `6fda198` | rectify(bulk-side): bulk identification target = A^cl_bulk\|_b, not C^bullet_ch(A_b,A_b) |
| `B-384` | `3359af6` | rectify(major): finish global E_1/E_2 chiral centre fix across tate fragments and W_inf endpoint |
| `B-385` | `988b855` | release(pdf): rebuild after global E_1/E_2 chiral centre fix completion |
| `B-386` | `b9a975b` | rectify(major): close remaining E_1/E_2 chiral-centre confusions (audit items 1, 3, 4, 5, 7, 8) |
| `B-387` | `02cd142` | rectify(major): tate-fragment openings stop calling A^cl_bulk\|_b 'the chiral Hochschild cohomology' |
| `B-388` | `425a3dc` | rectify(major): tate-P5 functorial diagram labels arrow with proper E_d index, flags conditional d>=2 |
| `B-389` | `b8e102c` | release(pdf): rebuild after audit-driven E_1/E_2 chiral-centre fixes (all 8 items closed) |
| `B-390` | `d322b0a` | rectify(economy): trim duplicate restatements in body + frontier opener |
| `B-391` | `8d9604f` | rectify(grammar): 'proves the stalk' is not a mathematical statement; replace with 'proves the stalk identification' giving the explicit equivalence |
| `B-392` | `edb1469` | release(pdf): rebuild after 'proves the stalk' grammar fix |
| `B-393` | `5abc57f` | rectify(abstract): remove undefined OPE notation, define ch boundary-category notation in place |
| `B-394` | `5f886e7` | rectify(abstract,summary): name the curve-restricted vertex algebra positively |
| `B-395` | `0dab580` | release(pdf): rebuild after positive curve-restriction framing |
| `B-396` | `668eb46` | rectify(attribution): Beilinson-Drinfeld worked only over curves, not surfaces; never attribute 2-dim factorization to BD |
| `B-397` | `3bad752` | release(pdf): rebuild after Beilinson-Drinfeld attribution discipline fix |
| `B-398` | `60d75a8` | release: full release build + cron-sibling cross-references to thm:formal-two-dimensional-holomorphic-ope |
| `B-399` | `68d5341` | rectify(audit-followup): close 6 of the 15 remaining audit items (highest-priority subset) |
| `B-400` | `6e46648` | rectify(abstract,audit-item-4): negative ghost framing + J_x define-before-use |
| `B-401` | `996ef08` | rectify(audit-followup-2): close audit items 5, 7-11 (define Phi_hbar, hypothesis convention, completion-blueprint clarification) |
| `B-402` | `ed0cfdd` | rectify(abstract): Witten/Etingof/Dirac/Feynman/Gaiotto voice — every sentence forces the next |
| `B-403` | `cdb3be8` | policy(memory): physicists invented chiral algebras / vertex algebras; BD formalised the D-module presentation, not the concept |
| `B-404` | `97056e2` | release: rebuild manuscript pdf |
| `B-405` | `9ae1528` | rewrite(summary-opening): Witten/Etingof/Dirac/Costello voice, every symbol defined before use, each sentence forces the next |
| `B-406` | `a58623e` | rewrite(summary-bv-brane): tighten redundant 'brane' + 'trace map J' paragraphs, integrate derived commuting variety / Hilbert scheme / J uniqueness into single chain |
| `B-407` | `02c77ea` | rewrite(summary-closed-open-coupling): consolidate duplicated bulk factorization + brane definition + dictionary into one inevitable chain |
| `B-408` | `2dfbfbf` | rewrite(summary-cross-volume): final Summary paragraph stops calling local theorem 'restriction of Z^der_ch(A)' with A undefined; states the Vol.III source functor and matched-conventions acceptance positively |
| `B-409` | `05737e1` | release(pdf): rebuild after Summary rewrite (paras 1-7 in Witten/Etingof voice) |
| `B-410` | `189fda6` | rewrite(conventions): replace negative ghost framing in conventions paragraph; tighten constellation-anchored objects paragraph |
| `B-411` | `376ae50` | rewrite(ch1-opening): tighten two jargon sentences in Ch1 'Dirac brane formal-stalk chart' subsection |
| `B-412` | `b6105d6` | rewrite(ch1-mixed-ht-strings): tighten 'local string theory' definition with Costello-Gwilliam citation, positive constructive framing of topological/holomorphic qualifiers |
| `B-413` | `7539dbf` | release: full make release build + cron-sibling voice tightenings ('pins' -> 'determines'/'identifies'/'locates' across 4 files) |
| `B-414` | `e77d6a7` | rectify(examples-major): fix type error — chart algebra A_b is ALWAYS C[[z_1, z_2]], not V_k / V^{betagamma} / Vir_c / W_N |
| `B-415` | `550e524` | release(pdf): rebuild after Examples type-error fix (chart algebra is always C[[z_1, z_2]]; vertex algebras arise on curve restriction) |
| `B-416` | `8e52c61` | rectify(abstract+summary+examples): bulk is 2-dim holomorphic factorisation algebra on C^2; curve-chiral comparisons (V_k, beta-gamma, Vir_c, W_N) are separate matched-conventions problems requiring different bulks not constructed here |
| `B-417` | `3ed5e29` | remove(examples,w-inf): delete fake examples and W_inf comparison chapter entirely; restore Witten/Etingof abstract |
| `B-418` | `e0320ac` | release: make release build at 496 pages, with cron-sibling brane-side derived E_1-Hochschild framing applied across tate fragments, appendices, local-dictionary, frontier volume, two-dim OPE |
| `B-419` | `d2d648a` | release(pdf): cron-sibling voice tightening of tate-P5 ('precise mechanism that fails' -> 'precise target obstruction'; 'fail to glue' -> 'carry a nonzero gluing obstruction') |
| `B-420` | `32a4f69` | rectify(abstract+summary): name the twist — BCOV is the topological B-twist of N=(2,2); the holomorphic-topological theory on R^2 x C^2 arises from a FURTHER holomorphic-topological twist in the Costello twisted-supergravity sense |
| `B-421` | `de883b1` | release(pdf): make release build at 497 pages, post twist-hierarchy clarification |
| `B-422` | `205f7f0` | rectify(main+architecture): upgrade local theorem to admissible category B^adm; absorb obstructions structurally; strip cross-volume scaffolding |
| `B-423` | `2831b8b` | rectify(main): realize absolute strongest form — 7-point B^adm + 9-step proof + monotone strength tower |
| `B-424` | `d1ed67c` | rectify(main+abstract): centrality homotopy hierarchy in dictionary; diagonal local-cohomology chiral E_2-operad on C^2; curve restriction; abstract upgraded to admissible category |
| `B-425` | `8742f6d` | rectify(main): add Consistency probes remark — eleven testable identities for the local theorem |
| `B-426` | `2f00877` | release(pdf+main): admissible Hochschild-centre lift definition; 500-page release build |
| `B-427` | `d89ff30` | audit: add resolution corpus and release PDF |
| `B-428` | `d00207e` | release: update proof text and PDF |
| `B-429` | `d363ffc` | release: sync root PDF |
| `B-430` | `83939fc` | release: remove across-volumes phrasing |
| `B-431` | `83fcf6d` | make release: publish release binary to ~/mathematics |
| `B-432` | `2a64b61` | rectify(boundary): Kato–Nakayama log boundary → Costello–Gwilliam brane link |
| `B-433` | `5fb168f` | make release: root-pdf sync + interactive architecture HTML/JSON |

---

## Phase C — Per-theorem-block first-principles audit (339 labeled blocks)

Each block: verify every step from first principles; supremum repair or named obstruction. Plus `C-bulk` for ~360 unlabeled blocks.

| ID | location | kind | label |
|---|---|---|---|
| `C-001` | `./tate-T2-nilpotent-truncation.tex:159` | `thm` | `thm:phi-trunc-classical` |
| `C-002` | `./tate-T2-nilpotent-truncation.tex:318` | `prop` | `prop:trunc-lost-sectors` |
| `C-003` | `./tate-P1-hadamard-mittag-leffler.tex:101` | `rmk` | `rmk:hadamard-factorization` |
| `C-004` | `./tate-P1-hadamard-mittag-leffler.tex:129` | `lem` | `lem:windowwise-parametrix` |
| `C-005` | `./tate-P1-hadamard-mittag-leffler.tex:214` | `thm` | `thm:hadamard-mittag-leffler` |
| `C-006` | `./tate-P1-hadamard-mittag-leffler.tex:354` | `rmk` | `rmk:hormander-commutation` |
| `C-007` | `./tate-P1-hadamard-mittag-leffler.tex:369` | `cor` | `cor:wt-cotangent-lift-hadamard-criterion` |
| `C-008` | `./tate-P1-hadamard-mittag-leffler.tex:404` | `thm` | `thm:weighted-rg-locality-reduced` |
| `C-009` | `./tate-P1-hadamard-mittag-leffler.tex:456` | `defn` | `defn:finite-window-graph-qme-system` |
| `C-010` | `./tate-P1-hadamard-mittag-leffler.tex:562` | `thm` | `thm:finite-window-graph-qme-assembly` |
| `C-011` | `./tate-P1-hadamard-mittag-leffler.tex:690` | `prop` | `prop:finite-window-qme-limit-condition` |
| `C-012` | `./tate-P1-hadamard-mittag-leffler.tex:785` | `defn` | `defn:finite-window-graph-array` |
| `C-013` | `./tate-P1-hadamard-mittag-leffler.tex:1005` | `prop` | `prop:first-finite-window-array-rows` |
| `C-014` | `./tate-P1-hadamard-mittag-leffler.tex:1093` | `prop` | `prop:universal-scalar-contact-bracket-rows` |
| `C-015` | `./tate-P1-hadamard-mittag-leffler.tex:1157` | `prop` | `prop:genuine-order-two-graph-weight-rows` |
| `C-016` | `./tate-P1-hadamard-mittag-leffler.tex:1348` | `prop` | `prop:order-two-finite-window-boundary-rows` |
| `C-017` | `./tate-P1-hadamard-mittag-leffler.tex:1487` | `prop` | `prop:computed-finite-window-truncation-matrices` |
| `C-018` | `./tate-P1-hadamard-mittag-leffler.tex:1682` | `prop` | `prop:projection-defined-uvq-truncation-data` |
| `C-019` | `./tate-P1-hadamard-mittag-leffler.tex:1899` | `prop` | `prop:finite-row-primitive-search-interface` |
| `C-020` | `./tate-P1-hadamard-mittag-leffler.tex:1998` | `prop` | `prop:concrete-order-three-enlarged-system-row` |
| `C-021` | `./tate-P1-hadamard-mittag-leffler.tex:2126` | `prop` | `prop:theta-three-finite-row-obstruction` |
| `C-022` | `./tate-P1-hadamard-mittag-leffler.tex:2192` | `prop` | `prop:theta-three-primitive-entry-criterion` |
| `C-023` | `./tate-P1-hadamard-mittag-leffler.tex:2328` | `thm` | `thm:theta-three-companion-face-obstruction` |
| `C-024` | `./tate-P1-hadamard-mittag-leffler.tex:2474` | `thm` | `thm:finite-window-nonscalar-curvature-criterion` |
| `C-025` | `./tate-P1-hadamard-mittag-leffler.tex:2656` | `rmk` | `rmk:finite-window-scalar-condition-boundary` |
| `C-026` | `./tate-P1-hadamard-mittag-leffler.tex:2669` | `rmk` | `rmk:hadamard-regulator-independence` |
| `C-027` | `./tate-P1-hadamard-mittag-leffler.tex:2681` | `rmk` | `rmk:hadamard-vs-bmk` |
| `C-028` | `./tate-P1-hadamard-mittag-leffler.tex:2878` | `cor` | `cor:promatlis-retract-as-supremum` |
| `C-029` | `./tate-P1-hadamard-mittag-leffler.tex:2919` | `thm` | `thm:promatlis-universal-property` |
| `C-030` | `./main.tex:828` | `ex` | `exa:point-evaluation-N1` |
| `C-031` | `./main.tex:837` | `ex` | `exa:linear-hamiltonians-anomaly` |
| `C-032` | `./main.tex:858` | `ex` | `exa:single-matlis-residue` |
| `C-033` | `./main.tex:1210` | `defn` | `def:local-hamiltonian-chiral-factorization-algebra` |
| `C-034` | `./main.tex:1279` | `prop` | `prop:local-hamiltonian-factorization-observables` |
| `C-035` | `./main.tex:1361` | `defn` | `def:closed-mixed-HT-factorization` |
| `C-036` | `./main.tex:1384` | `thm` | `thm:mixed-HT-factorization-theorem` |
| `C-037` | `./main.tex:1433` | `cor` | `cor:E2-bulk-algebra` |
| `C-038` | `./main.tex:1457` | `defn` | `def:E1-brane-algebra` |
| `C-039` | `./main.tex:1490` | `lem` | `lem:hamiltonian-vector-field-on-Rep` |
| `C-040` | `./main.tex:1544` | `thm` | `thm:closed-to-open-derived-centre-map` |
| `C-041` | `./main.tex:1637` | `rmk` | `rmk:native-bulk-object-c2` |
| `C-042` | `./main.tex:1666` | `prop` | `prop:finite-window-bm-native-e2-transfer` |
| `C-043` | `./main.tex:2073` | `prop` | `prop:native-darboux-disk-constructions` |
| `C-044` | `./main.tex:2158` | `prop` | `prop:formal-local-global-restriction` |
| `C-045` | `./main.tex:2449` | `rmk` | `rmk:type-discipline-cf-uf` |
| `C-046` | `./main.tex:2468` | `prop` | `prop:local-model-mixed-definition` |
| `C-047` | `./main.tex:2628` | `rmk` | `rmk:intro-symbol-separation` |
| `C-048` | `./main.tex:2931` | `thm` | `thm:hbf-cotangent-uniqueness-summary` |
| `C-049` | `./main.tex:2999` | `ex` | `ex:residue-mode-rho10` |
| `C-050` | `./main.tex:3021` | `rmk` | `rmk:scalar-hamiltonian-center-of-mass` |
| `C-051` | `./main.tex:3034` | `rmk` | `rmk:hbf-cotangent-obstruction` |
| `C-052` | `./main.tex:3099` | `rmk` | `rmk:polyvector-divergence-conventions` |
| `C-053` | `./main.tex:3116` | `lem` | `lem:polynomial-poincare` |
| `C-054` | `./main.tex:3146` | `prop` | `prop:hamiltonian-polyvector-reduction` |
| `C-055` | `./main.tex:3191` | `thm` | `thm:closed-bv-canonical-transformation` |
| `C-056` | `./main.tex:3259` | `rmk` | `rmk:cotangent-matlis-dualizing` |
| `C-057` | `./main.tex:3266` | `rmk` | `rmk:closed-bv-casimir-obstruction` |
| `C-058` | `./main.tex:3309` | `thm` | `thm:bf-action-uniqueness-qme` |
| `C-059` | `./main.tex:3397` | `rmk` | `rmk:bf-component-reading` |
| `C-060` | `./main.tex:3414` | `rmk` | `rmk:bf-renormalization-obstruction` |
| `C-061` | `./main.tex:3436` | `rmk` | `rmk:bf-phase-space` |
| `C-062` | `./main.tex:3610` | `lem` | `lem:formal-stalk-trace` |
| `C-063` | `./main.tex:3646` | `ex` | `ex:N1-commuting-case` |
| `C-064` | `./main.tex:3663` | `rmk` | `rmk:cyclic-framing-hilbert-branch` |
| `C-065` | `./main.tex:3685` | `rmk` | `rmk:formal-stalk-obstruction` |
| `C-066` | `./main.tex:3834` | `thm` | `thm:stable-eulerian-lqt-window` |
| `C-067` | `./main.tex:3919` | `rmk` | `rmk:same-rank-vs-LQT` |
| `C-068` | `./main.tex:4003` | `prop` | `prop:open-zero-fibre-traces` |
| `C-069` | `./main.tex:4067` | `prop` | `prop:skyscraper-ext` |
| `C-070` | `./main.tex:4106` | `rmk` | `rmk:open-koszul-duality` |
| `C-071` | `./main.tex:4229` | `prop` | `prop:open-bv-action-derived` |
| `C-072` | `./main.tex:4265` | `constr` | `constr:open-field-basis` |
| `C-073` | `./main.tex:4306` | `lem` | `lem:open-action-reduction` |
| `C-074` | `./main.tex:4338` | `lem` | `lem:dirac-brane-reduction` |
| `C-075` | `./main.tex:4376` | `prop` | `prop:open-bv-truncation` |
| `C-076` | `./main.tex:4633` | `constr` | `constr:reduced-bv-algebra` |
| `C-077` | `./main.tex:4649` | `lem` | `lem:derivative-jets` |
| `C-078` | `./main.tex:4664` | `prop` | `prop:stable-trace-invariants` |
| `C-079` | `./main.tex:4697` | `lem` | `lem:stable-marked-traces` |
| `C-080` | `./main.tex:4735` | `constr` | `constr:boundary-evaluation` |
| `C-081` | `./main.tex:4769` | `lem` | `lem:first-descendant-cycles` |
| `C-082` | `./main.tex:4788` | `prop` | `prop:one-psi-homology` |
| `C-083` | `./main.tex:4895` | `cor` | `cor:cotangent-boundary-pairing` |
| `C-084` | `./main.tex:4917` | `lem` | `lem:adjacent-swaps` |
| `C-085` | `./main.tex:5001` | `cor` | `cor:matrix-evaluation-well-defined` |
| `C-086` | `./main.tex:5304` | `prop` | `prop:stalk-central-multiplication` |
| `C-087` | `./main.tex:5344` | `prop` | `prop:brane-ops` |
| `C-088` | `./main.tex:5388` | `defn` | `defn:three-large-N-operations` |
| `C-089` | `./main.tex:5429` | `cor` | `cor:full-primitive-koszul-homology` |
| `C-090` | `./main.tex:5471` | `rmk` | `rmk:open-trace-koszul-admissibility` |
| `C-091` | `./main.tex:5611` | `lem` | `lem:type-discipline` |
| `C-092` | `./main.tex:5652` | `rmk` | `rmk:type-discipline-table` |
| `C-093` | `./main.tex:5669` | `lem` | `lem:bracket-on-observables` |
| `C-094` | `./main.tex:6050` | `thm` | `thm:brane-measurement-principle` |
| `C-095` | `./main.tex:6094` | `constr` | `constr:reduced-line-defect-current-kernel` |
| `C-096` | `./main.tex:6120` | `constr` | `constr:interval-fact-algebras` |
| `C-097` | `./main.tex:6244` | `prop` | `prop:brane-bracket-locality` |
| `C-098` | `./main.tex:6260` | `rmk` | `rmk:equal-time-locality` |
| `C-099` | `./main.tex:6509` | `rmk` | `rmk:E1-translation` |
| `C-100` | `./main.tex:6528` | `rmk` | `rmk:lurie-cg-quillen-equivalence` |
| `C-101` | `./main.tex:6545` | `thm` | `thm:hamiltonian-current-center-lift` |
| `C-102` | `./main.tex:6597` | `prop` | `prop:ce-source-obstruction` |
| `C-103` | `./main.tex:6635` | `rmk` | `rmk:ce-source-obstruction-disk` |
| `C-104` | `./main.tex:6655` | `defn` | `defn:formal-disk-ce-pv-completion` |
| `C-105` | `./main.tex:6664` | `defn` | `defn:bracket-kernel-admissible` |
| `C-106` | `./main.tex:6685` | `lem` | `lem:formal-disk-ce-schouten-continuity` |
| `C-107` | `./main.tex:6853` | `prop` | `prop:coordinate-coupling-equations` |
| `C-108` | `./main.tex:6901` | `thm` | `thm:universal-formal-local-ce-pv-recognition` |
| `C-109` | `./main.tex:7001` | `prop` | `prop:low-degree-pronilpotent-obstruction` |
| `C-110` | `./main.tex:7026` | `thm` | `thm:relative-filtered-koszul-lift` |
| `C-111` | `./main.tex:7091` | `lem` | `lem:filtered-cobar-qiso-criterion` |
| `C-112` | `./main.tex:7149` | `defn` | `defn:stable-ainfty-koszul-acceptance-datum` |
| `C-113` | `./main.tex:7243` | `thm` | `thm:stable-ainfty-koszul-under-hypotheses` |
| `C-114` | `./main.tex:7443` | `defn` | `defn:reduced-hamiltonian-p0-center` |
| `C-115` | `./main.tex:7805` | `thm` | `thm:main-local` |
| `C-116` | `./main.tex:8060` | `prop` | `prop:diagonal-cohomology-operad` |
| `C-117` | `./main.tex:8115` | `defn` | `defn:admissible-hochschild-centre-lift` |
| `C-118` | `./main.tex:8144` | `rmk` | `rmk:consistency-probes` |
| `C-119` | `./main.tex:8193` | `thm` | `thm:protected-summand-exhausts` |
| `C-120` | `./main.tex:8239` | `prop` | `prop:monotone-strength-tower` |
| `C-121` | `./main.tex:8360` | `thm` | `thm:main-global-conditional` |
| `C-122` | `./main.tex:8443` | `cor` | `cor:moment-map-shadow` |
| `C-123` | `./main.tex:8466` | `lem` | `lem:natural-correction-obstruction` |
| `C-124` | `./main.tex:8529` | `thm` | `thm:Jf-coordinate-uniqueness` |
| `C-125` | `./main.tex:8581` | `rmk` | `rmk:Jf-uniqueness-running-examples` |
| `C-126` | `./main.tex:8659` | `thm` | `thm:Jf-uniqueness-rigidity` |
| `C-127` | `./main.tex:8761` | `cor` | `cor:ce-pv-formal-disk` |
| `C-128` | `./main.tex:8804` | `ex` | `ex:low-degree-phi` |
| `C-129` | `./main.tex:8869` | `constr` | `constr:compact-current-pbw-rees-source` |
| `C-130` | `./main.tex:9334` | `rmk` | `rmk:weiss-ran-descent-obstruction` |
| `C-131` | `./main.tex:9487` | `cor` | `cor:tate-residual-sublattice` |
| `C-132` | `./main.tex:9705` | `lem` | `lem:continuous-bar-cobar` |
| `C-133` | `./main.tex:9831` | `lem` | `lem:linear-poisson-schouten` |
| `C-134` | `./main.tex:9873` | `prop` | `prop:ce-koszul` |
| `C-135` | `./main.tex:9981` | `lem` | `lem:trace-bracket-descends` |
| `C-136` | `./main.tex:10002` | `prop` | `prop:first-order-bracket` |
| `C-137` | `./main.tex:10040` | `prop` | `prop:open-descendant-action` |
| `C-138` | `./main.tex:10086` | `cor` | `cor:descendant-coadjoint-difference` |
| `C-139` | `./main.tex:10138` | `lem` | `lem:three-notions-of-locality` |
| `C-140` | `./main.tex:10178` | `rmk` | `rmk:locality-canonical-quantization` |
| `C-141` | `./main.tex:10189` | `prop` | `prop:principal-part-coadjoint` |
| `C-142` | `./main.tex:10237` | `thm` | `thm:canonical-residue-pairing` |
| `C-143` | `./main.tex:10312` | `rmk` | `rmk:residue-pairing-schur` |
| `C-144` | `./main.tex:10337` | `thm` | `thm:principal-part-coadjoint-uniqueness` |
| `C-145` | `./main.tex:10426` | `rmk` | `rmk:psi-rho-sign-convention` |
| `C-146` | `./main.tex:10437` | `thm` | `thm:pbw-vs-deformation` |
| `C-147` | `./main.tex:10528` | `prop` | `prop:polynomial-principal-part-boundary-obstruction` |
| `C-148` | `./main.tex:10563` | `thm` | `thm:polynomial-realization-categorical-obstruction` |
| `C-149` | `./main.tex:10612` | `rmk` | `rmk:polynomial-categorical-action-obstruction` |
| `C-150` | `./main.tex:10622` | `constr` | `constr:boundary-local-dual-principal-parts` |
| `C-151` | `./main.tex:10659` | `thm` | `thm:reduced-principal-part-boundary-current` |
| `C-152` | `./main.tex:10862` | `rmk` | `rmk:reduced-principal-part-currents` |
| `C-153` | `./main.tex:10878` | `thm` | `thm:boundary-principal-part-cotangent-operators` |
| `C-154` | `./main.tex:10908` | `rmk` | `rmk:unreduced-lift-obstruction` |
| `C-155` | `./main.tex:10955` | `thm` | `thm:bulk-boundary` |
| `C-156` | `./main.tex:10989` | `cor` | `cor:local-bulk-boundary-coupling` |
| `C-157` | `./main.tex:11276` | `prop` | `prop:quantum-boundary-descends` |
| `C-158` | `./main.tex:11303` | `prop` | `prop:quantum-boundary-descends-products` |
| `C-159` | `./main.tex:11340` | `rmk` | `rmk:normal-ordering-obstruction` |
| `C-160` | `./main.tex:11363` | `rmk` | `rmk:capelli-renormalized-traces` |
| `C-161` | `./main.tex:11401` | `lem` | `lem:capelli-renormalized-stable-trace` |
| `C-162` | `./main.tex:11469` | `cor` | `cor:renormalized-stable-connected-map` |
| `C-163` | `./main.tex:11488` | `thm` | `thm:finite-n-reduced-moyal` |
| `C-164` | `./main.tex:11666` | `cor` | `cor:degree-zero-quantum-upgrade` |
| `C-165` | `./main.tex:11736` | `rmk` | `rmk:quantum-hamiltonian-upgrade` |
| `C-166` | `./main.tex:11819` | `stmt` | `stmt:costello-bv-construction` |
| `C-167` | `./main.tex:11838` | `stmt` | `stmt:costello-li-flat-bcov` |
| `C-168` | `./main.tex:11858` | `lem` | `lem:finite-window-hamiltonian-obstruction` |
| `C-169` | `./main.tex:11901` | `rmk` | `rmk:linear-heat-versus-bv-kernel` |
| `C-170` | `./main.tex:11929` | `lem` | `lem:tate-casimir-obstruction` |
| `C-171` | `./main.tex:12372` | `rmk` | `rmk:parabolic-functoriality` |
| `C-172` | `./main.tex:12418` | `prop` | `prop:moyal-monomial` |
| `C-173` | `./main.tex:12453` | `thm` | `thm:phi-hbar-all-order` |
| `C-174` | `./main.tex:12567` | `thm` | `thm:componentwise-quantum-coefficient-comparison` |
| `C-175` | `./main.tex:12809` | `rmk` | `rmk:computer-verification` |
| `C-176` | `./main.tex:13113` | `prop` | `prop:theta-three-finite-window-criterion` |
| `C-177` | `./main.tex:13398` | `prop` | `prop:conditional-boundary-product-normalization` |
| `C-178` | `./main.tex:13460` | `thm` | `thm:open-line-midpoint-graph-weights` |
| `C-179` | `./main.tex:13686` | `thm` | `thm:first-third-costello-normalizations` |
| `C-180` | `./main.tex:13935` | `ex` | `ex:linear-hamiltonian-com` |
| `C-181` | `./main.tex:13970` | `lem` | `lem:omega-cocycle` |
| `C-182` | `./main.tex:14024` | `thm` | `thm:u1-center-anomaly` |
| `C-183` | `./main.tex:14055` | `thm` | `thm:u1-center-anomaly-open` |
| `C-184` | `./main.tex:14094` | `rmk` | `rmk:quotient-discipline-flag` |
| `C-185` | `./main.tex:14123` | `thm` | `thm:quantum-classical-anomaly` |
| `C-186` | `./main.tex:14179` | `rmk` | `rmk:three-faces-one-class` |
| `C-187` | `./main.tex:14263` | `rmk` | `rmk:determinant-line-scheme` |
| `C-188` | `./main.tex:14355` | `lem` | `lem:shifted-coadjoint-signs` |
| `C-189` | `./main.tex:14389` | `prop` | `prop:grav-ops` |
| `C-190` | `./main.tex:14429` | `rmk` | `rmk:strict-product-p0-obstruction` |
| `C-191` | `./main.tex:15001` | `conj` | `conj:chiral-Ed-deligne` |
| `C-192` | `./main.tex:15148` | `conj` | `conj:operator-modular-lift` |
| `C-193` | `./appendix-master-deformation-complex.tex:245` | `thm` | `thm:four-curvature-taxonomy` |
| `C-194` | `./appendix-master-deformation-complex.tex:306` | `thm` | `thm:six-coordinates-one-curvature` |
| `C-195` | `./tate-T1-weighted-completion.tex:55` | `rmk` | `rmk:diagnosis-unweighted-casimir` |
| `C-196` | `./tate-T1-weighted-completion.tex:71` | `rmk` | `rmk:costello-coefficient-requirements` |
| `C-197` | `./tate-T1-weighted-completion.tex:136` | `defn` | `defn:wt-degree-weight` |
| `C-198` | `./tate-T1-weighted-completion.tex:159` | `lem` | `lem:wt-weights-exist` |
| `C-199` | `./tate-T1-weighted-completion.tex:179` | `rmk` | `rmk:wt-canonical-weight` |
| `C-200` | `./tate-T1-weighted-completion.tex:196` | `defn` | `defn:wt-coefficient-pair` |
| `C-201` | `./tate-T1-weighted-completion.tex:223` | `rmk` | `rmk:wt-topology-content` |
| `C-202` | `./tate-T1-weighted-completion.tex:233` | `defn` | `defn:wt-Bw-envelope` |
| `C-203` | `./tate-T1-weighted-completion.tex:257` | `thm` | `thm:wt-canonical-habitat` |
| `C-204` | `./tate-T1-weighted-completion.tex:389` | `defn` | `defn:wt-Adm-category` |
| `C-205` | `./tate-T1-weighted-completion.tex:423` | `cor` | `cor:wt-Bw-initial` |
| `C-206` | `./tate-T1-weighted-completion.tex:438` | `rmk` | `rmk:wt-canonical-as-initiality` |
| `C-207` | `./tate-T1-weighted-completion.tex:444` | `prop` | `prop:wt-casimir-convergence` |
| `C-208` | `./tate-T1-weighted-completion.tex:482` | `rmk` | `rmk:wt-basis-independence` |
| `C-209` | `./tate-T1-weighted-completion.tex:496` | `prop` | `prop:wt-propagator-extends` |
| `C-210` | `./tate-T1-weighted-completion.tex:566` | `rmk` | `rmk:wt-brane-defect` |
| `C-211` | `./tate-T1-weighted-completion.tex:599` | `defn` | `defn:wt-omega-normal-window` |
| `C-212` | `./tate-T1-weighted-completion.tex:655` | `thm` | `thm:wt-omega-kernel-admissibility` |
| `C-213` | `./tate-T1-weighted-completion.tex:766` | `cor` | `cor:wt-omega-denominators-qme-boundary` |
| `C-214` | `./tate-T1-weighted-completion.tex:846` | `prop` | `prop:wt-rg-tame` |
| `C-215` | `./tate-T1-weighted-completion.tex:878` | `thm` | `thm:wt-rg-compatibility` |
| `C-216` | `./tate-T1-weighted-completion.tex:903` | `cor` | `thm:wt-cotangent-lift` |
| `C-217` | `./tate-T1-weighted-completion.tex:942` | `prop` | `prop:wt-qme-lift-obstruction-vanishing` |
| `C-218` | `./tate-T1-weighted-completion.tex:1019` | `cor` | `cor:wt-descendant-qme-vanishing` |
| `C-219` | `./tate-T1-weighted-completion.tex:1037` | `rmk` | `rmk:wt-sector-restriction` |
| `C-220` | `./tate-T1-weighted-completion.tex:1056` | `defn` | `defn:regulator-admissible-sector` |
| `C-221` | `./tate-T1-weighted-completion.tex:1181` | `stmt` | `stmt:weighted-rg-criterion` |
| `C-222` | `./tate-T1-weighted-completion.tex:1307` | `thm` | `thm:wt-regulator-independence-admissible` |
| `C-223` | `./tate-T1-weighted-completion.tex:3195` | `prop` | `ex:weighted-completion-changes-cohomology` |
| `C-224` | `./tate-T1-weighted-completion.tex:3218` | `ex` | `ex:super-exponential-bracket-obstruction` |
| `C-225` | `./tate-P5-cross-volume.tex:99` | `thm` | `thm:cross-target-firewall` |
| `C-226` | `./tate-P5-cross-volume.tex:251` | `defn` | `defn:local-hamiltonian-convention-base` |
| `C-227` | `./tate-P5-cross-volume.tex:282` | `lem` | `lem:formal-disk-transfer-obstruction` |
| `C-228` | `./tate-P5-cross-volume.tex:334` | `defn` | `defn:matched-conventions-theorem-datum` |
| `C-229` | `./tate-P5-cross-volume.tex:368` | `defn` | `defn:compact-hamiltonian-period-complex` |
| `C-230` | `./tate-P5-cross-volume.tex:390` | `defn` | `defn:global-hamiltonian-descent-complex` |
| `C-231` | `./tate-P5-cross-volume.tex:432` | `thm` | `thm:compact-period-sharp` |
| `C-232` | `./tate-P5-cross-volume.tex:468` | `thm` | `thm:global-descent-criterion` |
| `C-233` | `./tate-P5-cross-volume.tex:570` | `thm` | `thm:matched-conventions-transfer` |
| `C-234` | `./tate-P5-cross-volume.tex:682` | `defn` | `defn:mixed-dunn-fact6r-datum` |
| `C-235` | `./tate-P5-cross-volume.tex:768` | `prop` | `prop:fact6r-functor-of-points-recognition` |
| `C-236` | `./tate-P5-cross-volume.tex:829` | `defn` | `defn:mixed-dunn-obstruction-complex` |
| `C-237` | `./tate-P5-cross-volume.tex:861` | `thm` | `thm:mixed-dunn-criterion` |
| `C-238` | `./tate-P5-cross-volume.tex:917` | `cor` | `cor:matched-conventions-factorization` |
| `C-239` | `./tate-P5-cross-volume.tex:944` | `cor` | `cor:target-obstruction-criterion` |
| `C-240` | `./tate-P5-cross-volume.tex:981` | `defn` | `defn:matched-conventions-templates` |
| `C-241` | `./tate-P5-cross-volume.tex:1138` | `thm` | `thm:divergence-bcov` |
| `C-242` | `./tate-P5-cross-volume.tex:1190` | `thm` | `thm:divergence-volIII` |
| `C-243` | `./tate-P5-cross-volume.tex:1244` | `thm` | `thm:divergence-igusa-bkm` |
| `C-244` | `./tate-P5-cross-volume.tex:1300` | `thm` | `thm:divergence-gwdt` |
| `C-245` | `./tate-P5-cross-volume.tex:1344` | `thm` | `thm:divergence-osv` |
| `C-246` | `./tate-P5-cross-volume.tex:1383` | `thm` | `thm:divergence-mixed-dunn` |
| `C-247` | `./tate-P5-cross-volume.tex:1446` | `thm` | `thm:divergence-global-ham` |
| `C-248` | `./appendix-higher-factorization-categories.tex:30` | `defn` | `app:defn:hol-fact-Ed` |
| `C-249` | `./appendix-higher-factorization-categories.tex:88` | `defn` | `app:defn:HolFA-d-cat` |
| `C-250` | `./appendix-higher-factorization-categories.tex:106` | `defn` | `app:defn:mixed-HT-fact` |
| `C-251` | `./appendix-higher-factorization-categories.tex:130` | `defn` | `app:defn:ChirAlg-HT` |
| `C-252` | `./appendix-higher-factorization-categories.tex:142` | `defn` | `app:defn:Z-der-ch-d1` |
| `C-253` | `./appendix-higher-factorization-categories.tex:161` | `defn` | `app:defn:Z-der-ch-dgeq2` |
| `C-254` | `./appendix-higher-factorization-categories.tex:187` | `defn` | `app:defn:Z-der-HT` |
| `C-255` | `./appendix-higher-factorization-categories.tex:207` | `defn` | `app:defn:Darboux-stalk-functor` |
| `C-256` | `./appendix-higher-factorization-categories.tex:225` | `prop` | `app:prop:Darboux-equivariance` |
| `C-257` | `./appendix-higher-factorization-categories.tex:247` | `constr` | `app:constr:bulk-fact-Ed` |
| `C-258` | `./appendix-higher-factorization-categories.tex:269` | `prop` | `app:prop:bulk-stalk` |
| `C-259` | `./appendix-higher-factorization-categories.tex:320` | `defn` | `app:defn:brane-cat` |
| `C-260` | `./appendix-higher-factorization-categories.tex:338` | `constr` | `app:constr:brane-vacuum-E1` |
| `C-261` | `./appendix-higher-factorization-categories.tex:366` | `prop` | `app:prop:brane-HH-E2` |
| `C-262` | `./appendix-higher-factorization-categories.tex:382` | `conj` | `app:conj:mixed-HT-Deligne` |
| `C-263` | `./appendix-higher-factorization-categories.tex:431` | `thm` | `app:thm:stalk-of-conj` |
| `C-264` | `./appendix-higher-factorization-categories.tex:502` | `defn` | `app:defn:conf-D-module` |
| `C-265` | `./appendix-higher-factorization-categories.tex:515` | `defn` | `app:defn:chiral-Ed-operad` |
| `C-266` | `./appendix-higher-factorization-categories.tex:534` | `rmk` | `app:rmk:hEd-vs-BD-d1` |
| `C-267` | `./appendix-higher-factorization-categories.tex:559` | `constr` | `app:prop:hEd-algebras` |
| `C-268` | `./appendix-higher-factorization-categories.tex:620` | `defn` | `app:hyp:formality` |
| `C-269` | `./appendix-higher-factorization-categories.tex:634` | `defn` | `app:hyp:centrality` |
| `C-270` | `./appendix-higher-factorization-categories.tex:650` | `defn` | `app:hyp:ran-descent` |
| `C-271` | `./appendix-higher-factorization-categories.tex:672` | `thm` | `app:thm:conditional-Ed-deligne` |
| `C-272` | `./appendix-higher-factorization-categories.tex:703` | `rmk` | `app:rmk:formality-obstruction` |
| `C-273` | `./appendix-higher-factorization-categories.tex:720` | `rmk` | `app:rmk:chiral-Ed-package-obstruction` |
| `C-274` | `./appendix-higher-factorization-categories.tex:747` | `defn` | `app:defn:brane-link` |
| `C-275` | `./appendix-higher-factorization-categories.tex:765` | `defn` | `app:defn:sheaf-fact-cat-CG` |
| `C-276` | `./appendix-higher-factorization-categories.tex:813` | `thm` | `app:thm:descent-ss` |
| `C-277` | `./appendix-higher-factorization-categories.tex:837` | `defn` | `app:defn:heisenberg-collapse` |
| `C-278` | `./appendix-higher-factorization-categories.tex:853` | `thm` | `app:thm:global-stalk-from-collapse` |
| `C-279` | `./appendix-higher-factorization-categories.tex:914` | `defn` | `app:hyp:KZ-SDR` |
| `C-280` | `./appendix-higher-factorization-categories.tex:928` | `rmk` | `app:rmk:why-analytic` |
| `C-281` | `./appendix-higher-factorization-categories.tex:937` | `defn` | `app:hyp:stokes` |
| `C-282` | `./appendix-higher-factorization-categories.tex:946` | `defn` | `app:hyp:reflected-weights` |
| `C-283` | `./appendix-higher-factorization-categories.tex:972` | `thm` | `app:thm:conditional-qme` |
| `C-284` | `./appendix-higher-factorization-categories.tex:1008` | `rmk` | `app:rmk:qme-obstruction` |
| `C-285` | `./appendix-higher-factorization-categories.tex:1035` | `conj` | `app:conj:operator-lift-Delta5` |
| `C-286` | `./appendix-higher-factorization-categories.tex:1054` | `constr` | `app:constr:BKM-candidate` |
| `C-287` | `./appendix-higher-factorization-categories.tex:1083` | `constr` | `app:constr:DMZ-candidate` |
| `C-288` | `./appendix-higher-factorization-categories.tex:1096` | `rmk` | `app:rmk:operator-lift-obstructions` |
| `C-289` | `./appendix-higher-factorization-categories.tex:1110` | `thm` | `app:thm:conditional-global-deligne` |
| `C-290` | `./appendix-higher-factorization-categories.tex:1150` | `rmk` | `app:rmk:reduction-status` |
| `C-291` | `./appendix-higher-factorization-categories.tex:1170` | `constr` | `app:constr:program` |
| `C-292` | `./appendix-unreduced-bv-qme.tex:302` | `lem` | `lem:filtered-scalar-projection-obstruction` |
| `C-293` | `./appendix-unreduced-bv-qme.tex:353` | `prop` | `prop:app-first-scalar-lift-obstruction` |
| `C-294` | `./appendix-unreduced-bv-qme.tex:2189` | `lem` | `lem:app-oriented-marked-incidence-signs` |
| `C-295` | `./appendix-unreduced-bv-qme.tex:3777` | `thm` | `thm:app-minimal-full-equivariant-all-order-vanishing` |
| `C-296` | `./appendix-unreduced-bv-qme.tex:3831` | `prop` | `prop:app-first-order-three-enlarged-row` |
| `C-297` | `./frontier_mnop_framing_volume.tex:49` | `thm` | `thm:mnop-quintic` |
| `C-298` | `./appendix-radial-parts-moyal.tex:534` | `prop` | `prop:app-quantum-shear-suffices-radial-image` |
| `C-299` | `./appendix-radial-parts-moyal.tex:2177` | `ex` | `ex:app-radial-first-balanced-residual` |
| `C-300` | `./appendix-radial-parts-moyal.tex:2195` | `thm` | `thm:app-radial-bidegree-rational-reduction` |
| `C-301` | `./appendix-radial-parts-moyal.tex:2231` | `cor` | `cor:app-radial-vanishing-on-listed-range` |
| `C-302` | `./tate-T5-chain-level-primitive.tex:183` | `constr` | `constr:trace-count-filtration` |
| `C-303` | `./tate-T5-chain-level-primitive.tex:235` | `constr` | `constr:chain-level-primitive-projection` |
| `C-304` | `./tate-T5-chain-level-primitive.tex:286` | `lem` | `lem:primitive-shadow-kernel` |
| `C-305` | `./tate-T5-chain-level-primitive.tex:322` | `thm` | `thm:chain-level-primitive-projection-Q` |
| `C-306` | `./tate-T5-chain-level-primitive.tex:375` | `thm` | `thm:chain-level-primitive-projection-factorization` |
| `C-307` | `./tate-T5-chain-level-primitive.tex:421` | `thm` | `thm:chain-level-primitive-projection-P0` |
| `C-308` | `./tate-T5-chain-level-primitive.tex:452` | `constr` | `constr:T5-one-psi-complex` |
| `C-309` | `./tate-T5-chain-level-primitive.tex:498` | `lem` | `lem:T5-two-psi-boundary-sign` |
| `C-310` | `./tate-T5-chain-level-primitive.tex:539` | `thm` | `thm:T5-one-psi-homology` |
| `C-311` | `./tate-T5-chain-level-primitive.tex:622` | `defn` | `def:T5-full-psi-complex` |
| `C-312` | `./tate-T5-chain-level-primitive.tex:657` | `lem` | `lem:T5-full-p-face-sign` |
| `C-313` | `./tate-T5-chain-level-primitive.tex:689` | `constr` | `constr:T5-chip-moving-cellular-model` |
| `C-314` | `./tate-T5-chain-level-primitive.tex:705` | `lem` | `lem:T5-cellular-chain-identification` |
| `C-315` | `./tate-T5-chain-level-primitive.tex:732` | `lem` | `lem:T5-abel-cyclic-stabilizers` |
| `C-316` | `./tate-T5-chain-level-primitive.tex:913` | `constr` | `constr:chain-level-primitive-cotangent` |
| `C-317` | `./tate-T5-chain-level-primitive.tex:980` | `thm` | `thm:chain-level-primitive-projection` |
| `C-318` | `./tate-T5-chain-level-primitive.tex:1442` | `rmk` | `rmk:chain-level-primitive-algebraic-input` |
| `C-319` | `./tate-T5-chain-level-primitive.tex:1495` | `rmk` | `thm:T5-primitive-shadow-scope` |
| `C-320` | `./tate-T5-chain-level-primitive.tex:1517` | `rmk` | `rmk:role-of-deRham-contraction` |
| `C-321` | `./tate-T3-quillen-equivalence.tex:173` | `stmt` | `stmt:tate-model-envelope` |
| `C-322` | `./tate-T3-quillen-equivalence.tex:776` | `defn` | `defn:tate-conilp-coalg` |
| `C-323` | `./tate-P3-universality.tex:70` | `defn` | `defn:protected-hamiltonian-sector-brane-point` |
| `C-324` | `./tate-P3-universality.tex:98` | `defn` | `defn:admissible-protected-hamiltonian-restriction` |
| `C-325` | `./tate-P3-universality.tex:125` | `defn` | `defn:protected-twist-obstruction-datum` |
| `C-326` | `./tate-P3-universality.tex:193` | `lem` | `lem:protham-non-tautology` |
| `C-327` | `./tate-P3-universality.tex:428` | `cor` | `cor:protham-koszul-restriction` |
| `C-328` | `./tate-P3-universality.tex:488` | `defn` | `defn:super-balanced-equivariant-qme-datum` |
| `C-329` | `./tate-P3-universality.tex:540` | `thm` | `thm:joint-super-balanced-symp-qme-vanishing` |
| `C-330` | `./tate-P3-universality.tex:636` | `defn` | `defn:spin-hecke-queer-input` |
| `C-331` | `./tate-P3-universality.tex:669` | `thm` | `thm:queer-u1-center-anomaly-spin-hecke` |
| `C-332` | `./tate-P3-universality.tex:763` | `lem` | `lem:protected-primary-obstruction-test` |
| `C-333` | `./tate-P3-universality.tex:819` | `defn` | `defn:ambient-protected-realization-map` |
| `C-334` | `./tate-P3-universality.tex:834` | `prop` | `prop:admissible-protected-sector-reduction` |
| `C-335` | `./tate-P3-universality.tex:895` | `thm` | `thm:protected-twist-hamiltonian-criterion` |
| `C-336` | `./tate-P3-universality.tex:935` | `lem` | `lem:formal-restriction-external-acceptance` |
| `C-337` | `./tate-P3-universality.tex:986` | `defn` | `defn:protected-sector-matched-conventions-contribution` |
| `C-338` | `./tate-P3-universality.tex:1006` | `cor` | `cor:protected-formal-uniformity` |
| `C-339` | `./tate-P3-universality.tex:1052` | `cor` | `cor:protected-matched-conventions-interface` |
| `C-bulk` | all `*.tex` | bulk | audit every unlabeled thm/lem/prop/cor/defn/rmk/constr/ex/stmt; add label and first-principles audit |

---

## Phase D — Per-file chriss-ginzburg-rectify pass (26 tasks)

Each task is a full five-phase pass (global diagnostic → platonic restructuring → linear reconstitution → adversarial re-audit → final convergence) on one file.

| ID | file | action | verification |
|---|---|---|---|
| `D-01` | `abstract.tex` | full five-phase chriss-ginzburg-rectify pass | all 6 gates pass; build clean; voice and define-before-use clean |
| `D-02` | `appendix-algorithms.tex` | full five-phase chriss-ginzburg-rectify pass | all 6 gates pass; build clean; voice and define-before-use clean |
| `D-03` | `appendix-completion-blueprint.tex` | full five-phase chriss-ginzburg-rectify pass | all 6 gates pass; build clean; voice and define-before-use clean |
| `D-04` | `appendix-factorization-current-conventions.tex` | full five-phase chriss-ginzburg-rectify pass | all 6 gates pass; build clean; voice and define-before-use clean |
| `D-05` | `appendix-full-psi-homology.tex` | full five-phase chriss-ginzburg-rectify pass | all 6 gates pass; build clean; voice and define-before-use clean |
| `D-06` | `appendix-higher-factorization-categories.tex` | full five-phase chriss-ginzburg-rectify pass | all 6 gates pass; build clean; voice and define-before-use clean |
| `D-07` | `appendix-master-deformation-complex.tex` | full five-phase chriss-ginzburg-rectify pass | all 6 gates pass; build clean; voice and define-before-use clean |
| `D-08` | `appendix-matlis-principal-parts.tex` | full five-phase chriss-ginzburg-rectify pass | all 6 gates pass; build clean; voice and define-before-use clean |
| `D-09` | `appendix-radial-parts-moyal.tex` | full five-phase chriss-ginzburg-rectify pass | all 6 gates pass; build clean; voice and define-before-use clean |
| `D-10` | `appendix-sign-conventions.tex` | full five-phase chriss-ginzburg-rectify pass | all 6 gates pass; build clean; voice and define-before-use clean |
| `D-11` | `appendix-unreduced-bv-qme.tex` | full five-phase chriss-ginzburg-rectify pass | all 6 gates pass; build clean; voice and define-before-use clean |
| `D-12` | `authors.tex` | full five-phase chriss-ginzburg-rectify pass | all 6 gates pass; build clean; voice and define-before-use clean |
| `D-13` | `frontier_mnop_framing_volume.tex` | full five-phase chriss-ginzburg-rectify pass | all 6 gates pass; build clean; voice and define-before-use clean |
| `D-14` | `local-dictionary.tex` | full five-phase chriss-ginzburg-rectify pass | all 6 gates pass; build clean; voice and define-before-use clean |
| `D-15` | `main.tex` | full five-phase chriss-ginzburg-rectify pass | all 6 gates pass; build clean; voice and define-before-use clean |
| `D-16` | `mathmacros.tex` | full five-phase chriss-ginzburg-rectify pass | all 6 gates pass; build clean; voice and define-before-use clean |
| `D-17` | `tate-P1-hadamard-mittag-leffler.tex` | full five-phase chriss-ginzburg-rectify pass | all 6 gates pass; build clean; voice and define-before-use clean |
| `D-18` | `tate-P3-universality.tex` | full five-phase chriss-ginzburg-rectify pass | all 6 gates pass; build clean; voice and define-before-use clean |
| `D-19` | `tate-P5-cross-volume.tex` | full five-phase chriss-ginzburg-rectify pass | all 6 gates pass; build clean; voice and define-before-use clean |
| `D-20` | `tate-T1-weighted-completion.tex` | full five-phase chriss-ginzburg-rectify pass | all 6 gates pass; build clean; voice and define-before-use clean |
| `D-21` | `tate-T2-nilpotent-truncation.tex` | full five-phase chriss-ginzburg-rectify pass | all 6 gates pass; build clean; voice and define-before-use clean |
| `D-22` | `tate-T3-quillen-equivalence.tex` | full five-phase chriss-ginzburg-rectify pass | all 6 gates pass; build clean; voice and define-before-use clean |
| `D-23` | `tate-T4-bv-vanishing.tex` | full five-phase chriss-ginzburg-rectify pass | all 6 gates pass; build clean; voice and define-before-use clean |
| `D-24` | `tate-T5-chain-level-primitive.tex` | full five-phase chriss-ginzburg-rectify pass | all 6 gates pass; build clean; voice and define-before-use clean |
| `D-25` | `two-dimensional-holomorphic-ope.tex` | full five-phase chriss-ginzburg-rectify pass | all 6 gates pass; build clean; voice and define-before-use clean |
| `D-26` | `working_notes/principles.tex` | full five-phase chriss-ginzburg-rectify pass | all 6 gates pass; build clean; voice and define-before-use clean |

---

## Phase E — Per-section / subsection / subsubsection / paragraph structural pass (162 tasks)

Each heading gets a chriss-ginzburg structural pass: opens with the first mathematical object; closes by crystallizing what was proved and forcing what comes next; one question per section.

| ID | location | kind | title |
|---|---|---|---|
| `E-001` | `appendix-algorithms.tex:1` | `\section` | Algorithms |
| `E-002` | `appendix-completion-blueprint.tex:1` | `\section` | First-principles completion of the formal-local theorem |
| `E-003` | `appendix-completion-blueprint.tex:33` | `\subsection` | The host filtered nuclear Tate dg category |
| `E-004` | `appendix-completion-blueprint.tex:144` | `\subsection` | The local Hamiltonian BF theory as a genuine BV theory |
| `E-005` | `appendix-completion-blueprint.tex:227` | `\subsection` | Hamiltonian shears and the trace uniqueness theorem |
| `E-006` | `appendix-completion-blueprint.tex:307` | `\subsection` | The decorated PBW--Stokes complex and \(\Omega^{\mathrm{rad |
| `E-007` | `appendix-completion-blueprint.tex:356` | `\subsubsection` | Explicit primitives \(A^{(j) |
| `E-008` | `appendix-completion-blueprint.tex:502` | `\subsection` | The pro-Matlis weighted K\"othe target |
| `E-009` | `appendix-completion-blueprint.tex:616` | `\subsection` | Bracket-admissible \(B\) and kernel-admissible \(\mathcal K_B\) |
| `E-010` | `appendix-completion-blueprint.tex:707` | `\subsection` | The Tate bar-cobar admissible envelope |
| `E-011` | `appendix-completion-blueprint.tex:779` | `\subsection` | Open-trace \(A_\infty\)-Koszul acceptance datum |
| `E-012` | `appendix-completion-blueprint.tex:842` | `\subsection` | Hochschild centrality homotopies for \(\Phi_N\) |
| `E-013` | `appendix-completion-blueprint.tex:941` | `\subsection` | Protected-sector cyclic BV strong deformation retract |
| `E-014` | `appendix-completion-blueprint.tex:1038` | `\subsection` | Scalar-contact projection and the QME counterterm tower |
| `E-015` | `appendix-completion-blueprint.tex:1127` | `\subsubsection` | Finite-window QME counterterm recursion |
| `E-016` | `appendix-completion-blueprint.tex:1191` | `\subsection` | Costello brane-defect graph QME |
| `E-017` | `appendix-completion-blueprint.tex:1318` | `\subsection` | Stratified factorization algebra on \((X,L)\) |
| `E-018` | `appendix-completion-blueprint.tex:1373` | `\subsection` | Large-\(N\) trace state and connected cumulants |
| `E-019` | `appendix-completion-blueprint.tex:1440` | `\subsection` | The universal datum and master Maurer--Cartan equation |
| `E-020` | `appendix-completion-blueprint.tex:1608` | `\subsection` | Cross-target and external-target reading |
| `E-021` | `appendix-completion-blueprint.tex:1710` | `\subsection` | Summary: the curvature decomposition |
| `E-022` | `appendix-completion-blueprint.tex:1801` | `\subsection` | Status of the constructions |
| `E-023` | `appendix-factorization-current-conventions.tex:1` | `\section` | Factorization current conventions for the CE/PV interface |
| `E-024` | `appendix-full-psi-homology.tex:1` | `\section` | \texorpdfstring{Full Primitive Higher-\(\psi\) Koszul Homology |
| `E-025` | `appendix-higher-factorization-categories.tex:1` | `\section` | Higher factorization categories and chiral derived centres at \texorpdfstring{\$d\geq 2\$ |
| `E-026` | `appendix-higher-factorization-categories.tex:97` | `\subsection` | Mixed holomorphic-topological refinement |
| `E-027` | `appendix-higher-factorization-categories.tex:140` | `\subsection` | The chiral derived centre functor |
| `E-028` | `appendix-higher-factorization-categories.tex:201` | `\subsection` | The formal-Darboux stalk functor |
| `E-029` | `appendix-higher-factorization-categories.tex:488` | `\subsection` | The chiral \texorpdfstring{\$E_d\$ |
| `E-030` | `appendix-higher-factorization-categories.tex:738` | `\subsection` | Descent over the Costello--Gwilliam brane-link boundary |
| `E-031` | `appendix-higher-factorization-categories.tex:889` | `\subsection` | All-loop QME for finite-jet PVA |
| `E-032` | `appendix-higher-factorization-categories.tex:900` | `\paragraph` | Convention. |
| `E-033` | `appendix-higher-factorization-categories.tex:1022` | `\subsection` | Operator-level lift of the modular line at \texorpdfstring{\$\Delta_5\$ |
| `E-034` | `appendix-higher-factorization-categories.tex:1105` | `\subsection` | Convergent obstruction taxonomy |
| `E-035` | `appendix-master-deformation-complex.tex:1` | `\section` | The obstruction calculus: master deformation complex of local-to-global coherence |
| `E-036` | `appendix-master-deformation-complex.tex:59` | `\subsection` | Filtered \texorpdfstring{\$L_\infty\$ |
| `E-037` | `appendix-master-deformation-complex.tex:98` | `\subsection` | The transported local datum |
| `E-038` | `appendix-master-deformation-complex.tex:108` | `\paragraph` | Global Hamiltonian descent. |
| `E-039` | `appendix-master-deformation-complex.tex:124` | `\paragraph` | Costello quantum master equation. |
| `E-040` | `appendix-master-deformation-complex.tex:137` | `\paragraph` | Unreduced \(P_0\)-factorization-centre lift. |
| `E-041` | `appendix-master-deformation-complex.tex:153` | `\paragraph` | Decorated radial Stokes / Weyl normal form. |
| `E-042` | `appendix-master-deformation-complex.tex:164` | `\paragraph` | Strict all-window Bochner--Martinelli current transfer. |
| `E-043` | `appendix-master-deformation-complex.tex:173` | `\paragraph` | Modular open-closed clutching. |
| `E-044` | `appendix-master-deformation-complex.tex:189` | `\subsection` | Twists: three mechanisms |
| `E-045` | `appendix-master-deformation-complex.tex:243` | `\subsection` | Four-curvature taxonomy and six-coordinate classification |
| `E-046` | `appendix-matlis-principal-parts.tex:1` | `\section` | The pro-Matlis target: Matlis principal parts and the continuous cotangent module |
| `E-047` | `appendix-matlis-principal-parts.tex:47` | `\subsection` | The defect polarization |
| `E-048` | `appendix-matlis-principal-parts.tex:206` | `\subsection` | Construction of the residual side |
| `E-049` | `appendix-matlis-principal-parts.tex:475` | `\subsection` | Rigidity of the residue pairing |
| `E-050` | `appendix-matlis-principal-parts.tex:522` | `\subsection` | Local-nilpotence obstruction to polynomial realization |
| `E-051` | `appendix-matlis-principal-parts.tex:579` | `\subsection` | Universal Fourier--Rees label bridge |
| `E-052` | `appendix-radial-parts-moyal.tex:1` | `\section` | Radial parts and the Moyal normalization |
| `E-053` | `appendix-sign-conventions.tex:1` | `\section` | Sign conventions for the Hamiltonian comparison |
| `E-054` | `appendix-unreduced-bv-qme.tex:1` | `\section` | Unreduced BV cotangent, scalar QME obstructions, and cancellations |
| `E-055` | `frontier_mnop_framing_volume.tex:34` | `\section` | MNOP factorisation and the \$\E_2\$-centre obstruction |
| `E-056` | `frontier_mnop_framing_volume.tex:124` | `\section` | \$S^3\$-framing on the quintic |
| `E-057` | `frontier_mnop_framing_volume.tex:184` | `\section` | Chiral-volume finite evidence on the quintic |
| `E-058` | `frontier_mnop_framing_volume.tex:316` | `\section` | Serre pairing as compact-CY categorical input |
| `E-059` | `frontier_mnop_framing_volume.tex:356` | `\section` | Fourier--Mukai partners for \$K3 \times E\$ |
| `E-060` | `frontier_mnop_framing_volume.tex:495` | `\section` | Non-perturbative BCOV: Gopakumar--Vafa closure |
| `E-061` | `local-dictionary.tex:7` | `\paragraph` | Linear-algebraic category: Tate \$\C\$-vector spaces. |
| `E-062` | `local-dictionary.tex:58` | `\paragraph` | Unimodularity datum. |
| `E-063` | `local-dictionary.tex:157` | `\paragraph` | Kinematic locality. |
| `E-064` | `local-dictionary.tex:503` | `\paragraph` | Normal \(\Omega\)-background. |
| `E-065` | `local-dictionary.tex:794` | `\paragraph` | Canonical maps and obstruction symbols. |
| `E-066` | `local-dictionary.tex:916` | `\paragraph` | Non-scalar Costello/QME labels. |
| `E-067` | `local-dictionary.tex:1222` | `\paragraph` | Common local rings and quotients. |
| `E-068` | `local-dictionary.tex:1285` | `\paragraph` | Large-\(N\) and quotient conventions. |
| `E-069` | `local-dictionary.tex:1311` | `\paragraph` | Separation rule. |
| `E-070` | `local-dictionary.tex:1329` | `\paragraph` | Source--target table. |
| `E-071` | `local-dictionary.tex:1454` | `\paragraph` | PBW special-fibre open trace labels. |
| `E-072` | `local-dictionary.tex:1508` | `\paragraph` | Closed CE/PV labels. |
| `E-073` | `local-dictionary.tex:1558` | `\paragraph` | Matlis principal-part labels. |
| `E-074` | `local-dictionary.tex:1612` | `\paragraph` | Interval-current and boundary labels. |
| `E-075` | `main.tex:446` | `\paragraph` | Geometric and algebraic conventions. |
| `E-076` | `main.tex:487` | `\paragraph` | Sign, degree, and renormalization conventions. |
| `E-077` | `main.tex:499` | `\paragraph` | Homological taxonomy. |
| `E-078` | `main.tex:562` | `\paragraph` | Constellation-anchored objects. |
| `E-079` | `main.tex:603` | `\paragraph` | Theorem-control predicates. |
| `E-080` | `main.tex:651` | `\paragraph` | Convention firewall. |
| `E-081` | `main.tex:663` | `\section` | The setup |
| `E-082` | `main.tex:665` | `\subsection` | The Dirac brane formal-stalk chart in one calculation |
| `E-083` | `main.tex:881` | `\subsection` | Mixed holomorphic-topological strings |
| `E-084` | `main.tex:1155` | `\subsection` | The local mixed model |
| `E-085` | `main.tex:1167` | `\paragraph` | The minimal RG-stable completion. |
| `E-086` | `main.tex:1349` | `\subsubsection` | The closed--open factorization triple: \texorpdfstring{\(E_2\) |
| `E-087` | `main.tex:2272` | `\subsection` | Local setup at one brane stack |
| `E-088` | `main.tex:2581` | `\subsection` | Notation for the local theorem |
| `E-089` | `main.tex:2650` | `\subsection` | Three notions of locality |
| `E-090` | `main.tex:2659` | `\paragraph` | (a) Support locality along the brane. |
| `E-091` | `main.tex:2685` | `\paragraph` | (b) Topological locality. |
| `E-092` | `main.tex:2697` | `\paragraph` | (c) Formal holomorphic locality. |
| `E-093` | `main.tex:2763` | `\subsection` | Unitarity |
| `E-094` | `main.tex:2842` | `\section` | The shifted-cotangent BF Lie algebra |
| `E-095` | `main.tex:2868` | `\paragraph` | Hamiltonian vector fields from Cartan's identity. |
| `E-096` | `main.tex:2897` | `\paragraph` | The cotangent extension from canonical-transformation BV. |
| `E-097` | `main.tex:2923` | `\paragraph` | The cotangent module from residue duality. |
| `E-098` | `main.tex:3057` | `\subsection` | Closed mixed Hamiltonian sector |
| `E-099` | `main.tex:3283` | `\subsection` | Hamiltonian BF action |
| `E-100` | `main.tex:3462` | `\section` | The derived commuting variety stack at \$N\$ Dirac branes |
| `E-101` | `main.tex:3469` | `\subsection` | The Dirac brane stack |
| `E-102` | `main.tex:3525` | `\paragraph` | The substitution forces the open BV theory. |
| `E-103` | `main.tex:3594` | `\paragraph` | Word-ordering independence of \(J\). |
| `E-104` | `main.tex:3727` | `\subsection` | Hamiltonian sector and stable large N |
| `E-105` | `main.tex:3974` | `\subsection` | Open mixed brane states |
| `E-106` | `main.tex:4139` | `\subsection` | Open mixed brane field theory |
| `E-107` | `main.tex:4304` | `\subsubsection` | Ghost-zero open field content |
| `E-108` | `main.tex:4509` | `\subsection` | Open-brane operators and the large \$N\$ limit |
| `E-109` | `main.tex:5517` | `\section` | Boundary algebra and trace map |
| `E-110` | `main.tex:5526` | `\subsection` | The reduced CE/PV trace map |
| `E-111` | `main.tex:5694` | `\paragraph` | The CE/PV dictionary. |
| `E-112` | `main.tex:5706` | `\paragraph` | Word ordering is BRST-exact, the bracket records the symbol. |
| `E-113` | `main.tex:5737` | `\paragraph` | Finite Taylor truncation obstruction. |
| `E-114` | `main.tex:5827` | `\subsection` | The two algebras |
| `E-115` | `main.tex:6008` | `\subsection` | Reduced Hamiltonian brane coupling |
| `E-116` | `main.tex:7299` | `\section` | CE/PV dictionary as Koszul resolution |
| `E-117` | `main.tex:7309` | `\subsection` | The concrete dictionary |
| `E-118` | `main.tex:7324` | `\paragraph` | Open PBW special fibre. |
| `E-119` | `main.tex:7342` | `\paragraph` | Closed CE/PV coordinates. |
| `E-120` | `main.tex:7376` | `\paragraph` | Matlis principal parts. |
| `E-121` | `main.tex:7391` | `\paragraph` | Label collision. |
| `E-122` | `main.tex:7408` | `\subsection` | The CE/PV Koszul resolution of the brane \$E_1\$-Hochschild |
| `E-123` | `main.tex:7637` | `\subsection` | The local theorem |
| `E-124` | `main.tex:9012` | `\paragraph` | Nilpotent truncation \(\mathfrak o_{\mathrm{nilp |
| `E-125` | `main.tex:9056` | `\paragraph` | Tate Quillen equivalence \(\mathfrak o_{\mathrm{Quil |
| `E-126` | `main.tex:9096` | `\paragraph` | BV-cohomology endpoint \(\mathfrak o_{\mathrm{BV,end |
| `E-127` | `main.tex:9146` | `\paragraph` | Chain-level primitive projection \(\mathfrak o_{\mathrm{prim |
| `E-128` | `main.tex:9181` | `\paragraph` | Hadamard/Mittag-Leffler endpoint \(\mathfrak o_{\mathrm{Had |
| `E-129` | `main.tex:9223` | `\paragraph` | Protected universality \(\mathfrak o_{\mathrm{univ |
| `E-130` | `main.tex:9272` | `\paragraph` | Matched-conventions component \(\mathfrak o_{\mathrm{cv |
| `E-131` | `main.tex:9547` | `\subsection` | Stratified CE/PV and admissible Koszul duality |
| `E-132` | `main.tex:9955` | `\subsubsection` | First-order Poisson identification |
| `E-133` | `main.tex:11134` | `\subsubsection` | Quantization as a brane trace-map test |
| `E-134` | `main.tex:11808` | `\subsubsection` | Graph formalism and specialization datum |
| `E-135` | `main.tex:12386` | `\subsubsection` | Formal Weyl/Moyal target, all orders |
| `E-136` | `main.tex:13539` | `\subsubsection` | Third-order target for Costello's graph problem |
| `E-137` | `main.tex:13872` | `\section` | The Capelli scalar |
| `E-138` | `main.tex:13882` | `\subsection` | The U(1) centre-of-mass cocycle |
| `E-139` | `main.tex:13909` | `\paragraph` | The closed--open mismatch cocycle. |
| `E-140` | `main.tex:14286` | `\subsection` | Operators in the closed Hamiltonian sector |
| `E-141` | `main.tex:14483` | `\paragraph` | All-bidegree Capelli through the radial-parts identity. |
| `E-142` | `main.tex:14516` | `\subsection` | Tate-coefficient cotangent lift: the six gauge slices in body |
| `E-143` | `main.tex:14649` | `\paragraph` | Weighted Casimir kernel \(\mathfrak o_{\mathrm{Cas |
| `E-144` | `main.tex:14692` | `\subsection` | Pro-Matlis envelope and bulk-boundary duality |
| `E-145` | `main.tex:14769` | `\paragraph` | Bulk-boundary duality. |
| `E-146` | `main.tex:14799` | `\paragraph` | The \texorpdfstring{\$\varprojlim^1\$ |
| `E-147` | `main.tex:14854` | `\section` | Examples |
| `E-148` | `main.tex:14873` | `\subsubsection` | The single brane: \texorpdfstring{\$N=1\$ |
| `E-149` | `main.tex:14888` | `\subsubsection` | The brane stack: \texorpdfstring{\$N\ge 2\$ |
| `E-150` | `main.tex:14909` | `\section` | The frontier |
| `E-151` | `main.tex:15265` | `\paragraph` | The closing identification. |
| `E-152` | `tate-P3-universality.tex:1` | `\subsection` | Universality of the formal-local Hamiltonian sector |
| `E-153` | `tate-P5-cross-volume.tex:1` | `\subsection` | Convention firewall and matched-conventions acceptance |
| `E-154` | `tate-T3-quillen-equivalence.tex:73` | `\subsubsection` | The Tate chain category |
| `E-155` | `tate-T3-quillen-equivalence.tex:329` | `\subsubsection` | Twisting cochains and the filtered-cobar admissibility criterion |
| `E-156` | `tate-T3-quillen-equivalence.tex:717` | `\subsubsection` | Operad-algebra transfer |
| `E-157` | `tate-T3-quillen-equivalence.tex:833` | `\subsubsection` | Bar-cobar Quillen equivalence in the admissible envelope |
| `E-158` | `tate-T3-quillen-equivalence.tex:937` | `\subsubsection` | Identification with the Lie operadic Koszul duality |
| `E-159` | `tate-T3-quillen-equivalence.tex:1054` | `\subsubsection` | Module reconstruction from the CE/PV identity |
| `E-160` | `tate-T3-quillen-equivalence.tex:1146` | `\subsubsection` | Conilpotence and Casimir convergence |
| `E-161` | `tate-T5-chain-level-primitive.tex:1` | `\subsection` | \texorpdfstring{Primitive indecomposable \(P_0\)-shadow: the Koszul resolution at \(F_1/F_0\) |
| `E-162` | `two-dimensional-holomorphic-ope.tex:1` | `\subsubsection` | The formal two-dimensional holomorphic singular product |

---

## Phase F — Per-script compute-anchor (29 tasks)

| ID | script | action | verification |
|---|---|---|---|
| `F-01` | `scripts/audit_loop.py` | anchor script output in manuscript with explicit \ref/\eqref; add \paragraph{Compute backing.} block | cite reachable from text; rebuild script and confirm output matches |
| `F-02` | `scripts/build_architecture.py` | anchor script output in manuscript with explicit \ref/\eqref; add \paragraph{Compute backing.} block | cite reachable from text; rebuild script and confirm output matches |
| `F-03` | `scripts/build_unified_architecture.py` | anchor script output in manuscript with explicit \ref/\eqref; add \paragraph{Compute backing.} block | cite reachable from text; rebuild script and confirm output matches |
| `F-04` | `scripts/check_W5_A4_small_N.py` | anchor script output in manuscript with explicit \ref/\eqref; add \paragraph{Compute backing.} block | cite reachable from text; rebuild script and confirm output matches |
| `F-05` | `scripts/check_W5_X4_A5RG.py` | anchor script output in manuscript with explicit \ref/\eqref; add \paragraph{Compute backing.} block | cite reachable from text; rebuild script and confirm output matches |
| `F-06` | `scripts/check_adversarial_sweep.py` | anchor script output in manuscript with explicit \ref/\eqref; add \paragraph{Compute backing.} block | cite reachable from text; rebuild script and confirm output matches |
| `F-07` | `scripts/check_audit_consistency_probes.py` | anchor script output in manuscript with explicit \ref/\eqref; add \paragraph{Compute backing.} block | cite reachable from text; rebuild script and confirm output matches |
| `F-08` | `scripts/check_bch_cubic_cocycle.py` | anchor script output in manuscript with explicit \ref/\eqref; add \paragraph{Compute backing.} block | cite reachable from text; rebuild script and confirm output matches |
| `F-09` | `scripts/check_bi_infinite_lie_consistency.py` | anchor script output in manuscript with explicit \ref/\eqref; add \paragraph{Compute backing.} block | cite reachable from text; rebuild script and confirm output matches |
| `F-10` | `scripts/check_classical_super_sweep.py` | anchor script output in manuscript with explicit \ref/\eqref; add \paragraph{Compute backing.} block | cite reachable from text; rebuild script and confirm output matches |
| `F-11` | `scripts/check_classical_super_sweep_N3.py` | anchor script output in manuscript with explicit \ref/\eqref; add \paragraph{Compute backing.} block | cite reachable from text; rebuild script and confirm output matches |
| `F-12` | `scripts/check_derived_intersection_N2.py` | anchor script output in manuscript with explicit \ref/\eqref; add \paragraph{Compute backing.} block | cite reachable from text; rebuild script and confirm output matches |
| `F-13` | `scripts/check_derived_intersection_N_extended.py` | anchor script output in manuscript with explicit \ref/\eqref; add \paragraph{Compute backing.} block | cite reachable from text; rebuild script and confirm output matches |
| `F-14` | `scripts/check_g2g3_attack_heal.py` | anchor script output in manuscript with explicit \ref/\eqref; add \paragraph{Compute backing.} block | cite reachable from text; rebuild script and confirm output matches |
| `F-15` | `scripts/check_g2g3_transversality.py` | anchor script output in manuscript with explicit \ref/\eqref; add \paragraph{Compute backing.} block | cite reachable from text; rebuild script and confirm output matches |
| `F-16` | `scripts/check_higher_spin_jacobi.py` | anchor script output in manuscript with explicit \ref/\eqref; add \paragraph{Compute backing.} block | cite reachable from text; rebuild script and confirm output matches |
| `F-17` | `scripts/check_moyal_coefficients.py` | anchor script output in manuscript with explicit \ref/\eqref; add \paragraph{Compute backing.} block | cite reachable from text; rebuild script and confirm output matches |
| `F-18` | `scripts/check_non_multiplicative_chiral_charge.py` | anchor script output in manuscript with explicit \ref/\eqref; add \paragraph{Compute backing.} block | cite reachable from text; rebuild script and confirm output matches |
| `F-19` | `scripts/check_one_psi_homology.py` | anchor script output in manuscript with explicit \ref/\eqref; add \paragraph{Compute backing.} block | cite reachable from text; rebuild script and confirm output matches |
| `F-20` | `scripts/check_pva_M2_degree3.py` | anchor script output in manuscript with explicit \ref/\eqref; add \paragraph{Compute backing.} block | cite reachable from text; rebuild script and confirm output matches |
| `F-21` | `scripts/check_pva_module_lambda_bracket.py` | anchor script output in manuscript with explicit \ref/\eqref; add \paragraph{Compute backing.} block | cite reachable from text; rebuild script and confirm output matches |
| `F-22` | `scripts/check_pva_module_z2_direction.py` | anchor script output in manuscript with explicit \ref/\eqref; add \paragraph{Compute backing.} block | cite reachable from text; rebuild script and confirm output matches |
| `F-23` | `scripts/check_sergeev_intertwiner.py` | anchor script output in manuscript with explicit \ref/\eqref; add \paragraph{Compute backing.} block | cite reachable from text; rebuild script and confirm output matches |
| `F-24` | `scripts/check_symp_functoriality.py` | anchor script output in manuscript with explicit \ref/\eqref; add \paragraph{Compute backing.} block | cite reachable from text; rebuild script and confirm output matches |
| `F-25` | `scripts/finite_window_graph_array.py` | anchor script output in manuscript with explicit \ref/\eqref; add \paragraph{Compute backing.} block | cite reachable from text; rebuild script and confirm output matches |
| `F-26` | `scripts/quantum_shear_primitive_search.py` | anchor script output in manuscript with explicit \ref/\eqref; add \paragraph{Compute backing.} block | cite reachable from text; rebuild script and confirm output matches |
| `F-27` | `scripts/quantum_shear_trace_diagram_normal_form.py` | anchor script output in manuscript with explicit \ref/\eqref; add \paragraph{Compute backing.} block | cite reachable from text; rebuild script and confirm output matches |
| `F-28` | `scripts/quantum_shear_universal_formula.py` | anchor script output in manuscript with explicit \ref/\eqref; add \paragraph{Compute backing.} block | cite reachable from text; rebuild script and confirm output matches |
| `F-29` | `scripts/quintic_arithmetic_rate_checks.py` | anchor script output in manuscript with explicit \ref/\eqref; add \paragraph{Compute backing.} block | cite reachable from text; rebuild script and confirm output matches |

---

## Phase G — Per-citation verification (57 tasks)

| ID | citekey | action | verification |
|---|---|---|---|
| `G-01` | `aksz` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-02` | `amarkin-deligne` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-03` | `ayala-francis` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-04` | `bcov` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-05` | `beilinson-drinfeld-chiral` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-06` | `beilinson-feigin-mazur` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-07` | `berger-moerdijk-axiomatic` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-08` | `borcherds-fake` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-09` | `brown-perturbation-lemma` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-10` | `calaque-derived-branes` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-11` | `capelli` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-12` | `costello-gwilliam` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-13` | `costello-gwilliam-vol2` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-14` | `costello-li-open-closed-bcov` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-15` | `costello-li-quantum-bcov` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-16` | `costello-renormalization` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-17` | `costello-twistedM` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-18` | `crainic-perturbation-lemma` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-19` | `dabholkar-murthy-zagier` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-20` | `francis-gaitsgory-chiral-koszul` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-21` | `francis-thesis` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-22` | `getzler-jones-aoperad` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-23` | `gritsenko-nikulin-paramodular` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-24` | `gwilliam-williams-holomorphic-bosonic-string` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-25` | `harish-chandra-invariant-differential-operators` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-26` | `hartshorne-local-cohomology` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-27` | `hinich-htpy-alg` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-28` | `hormander-vol1` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-29` | `hovey` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-30` | `howe-capelli` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-31` | `igusa-cusp-form` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-32` | `kontsevich-dq` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-33` | `kontsevich-soibelman-deformation` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-34` | `kothe-topological-vector-spaces` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-35` | `kunz-residues-duality` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-36` | `laurent-thiebaut-bmk` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-37` | `lefevre-hasegawa` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-38` | `levasseur-stafford-harish-chandra` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-39` | `levasseur-stafford-kernel-harish-chandra` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-40` | `loday-quillen` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-41` | `loday-vallette` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-42` | `lorgat-vol1` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-43` | `lurie-ha` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-44` | `matlis-injective` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-45` | `mcclure-smith` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-46` | `milnor-axiomatic-homology` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-47` | `nekrasov-schwarz-noncommutative` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-48` | `priddy` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-49` | `procesi` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-50` | `ptvv-shifted-symplectic` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-51` | `quillen-htpy` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-52` | `razmyslov` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-53` | `ruppenthal-bmk` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-54` | `schwede-shipley-monoid` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-55` | `sygan` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-56` | `wallach-reductive-invariant-differential` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |
| `G-57` | `witten-cs` | verify entry exists in main.tex bibliography; verify cited theorem/section exists in source; verify pin (Vol/page/§) is correct | pin reachable in published source; entry not orphan |

---

## Phase H — Seventeen-site catalogue per-item scan (17 tasks)

| ID | catalogue item | action |
|---|---|---|
| `H-01` | Item 1: $A$ is the primitive open object | find every site asserting $A_b$ (or $A$) as the primitive open object; replace with "$\mathcal{C}^{\mathrm{op}}_\partial$ primitive; $A_b = \mathrm{End}(b)$ for chosen $b$" |
| `H-02` | Item 2: $\mathrm{Bar}(A) = $ bulk | find every site conflating $\mathrm{Bar}(A)$ with the bulk; replace with "$\mathrm{Bar}(A)$ = twisting coalgebra; bulk = $Z^{\mathrm{der}}_{\mathrm{ch}}(A) \simeq C^\bullet_{\mathrm{ch}}(A,A)$" |
| `H-03` | Item 3: 2d chiral $\Rightarrow$ 3d HT via $E_1$-bar | replace with chiral Deligne–Tamarkin: $A \rightsquigarrow Z^{\mathrm{der}}_{\mathrm{ch}}(A)$ one-up |
| `H-04` | Item 4: open sector on bare curve $X$ | (now post-KN→CG sweep) re-scan: every "boundary" reference is to Costello–Gwilliam brane-link $\partial X$; no residual log-geometry framing |
| `H-05` | Item 5: modularity is property of closed algebra | replace with trace + clutching on the open category |
| `H-06` | Item 6: five $\kappa$-numbers (0,0,3,5,24) as one invariant | replace with "five distinct construction layers; spectral-sequence interpretation conjectural" |
| `H-07` | Item 7: $\mathrm{CY}_d\text{-Cat} \to \mathrm{ChirAlg}$ direct | replace with $\Phi_d = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1},C} \circ \Phi^{\mathrm{FA}}_d$ |
| `H-08` | Item 8: $Y^+(X) = \mathcal G(X)$ | replace with $\mathcal G(X) = D(Y^+(X))$ after Hall + completion + integral form + stable-envelope + descent |
| `H-09` | Item 9: 6d hCS = 3d CS in disguise | replace with "6d hCS realises $\Phi^{\mathrm{FA}}_3$ on verified loci; one-loop quartic" |
| `H-10` | Item 10: formal local HT $\Rightarrow$ global compact theory | replace with "formal-Darboux + descent + QME + anomaly + locality $\Rightarrow$ candidate" |
| `H-11` | Item 11: $\Delta_5 = $ compact BPS Hilbert space | replace with "$\Delta_5 = $ Borcherds denominator / scalar shadow; operator lift open" |
| `H-12` | Item 12: scalar $Z_{\mathrm{BPS}}$ = operator algebra | replace with "scalar = protected trace of still-to-be-constructed operator package" |
| `H-13` | Item 13: algebraic holography $=$ 3d gravity construction | replace with "identification of HT sector; not construction of dynamical-metric path integral" |
| `H-14` | Item 14: $W_\infty[\lambda] \Rightarrow E_\infty$ from finite-spin checks | replace with "conditional on Prochazka, CKL, Pope–Romans–Shen/Bakas, Yamada" |
| `H-15` | Item 15: class M chain-level in ordinary complexes | replace with "completed ambient: HS-sewing / coderived BV = bar / weight-completed / pro / $J$-adic" |
| `H-16` | Item 16: PVA Jacobi $\Rightarrow$ all-loop quantum | replace with "classical only; finite-jet PVA all-loop conditional on KZ analytic SDR + Stokes + reflected weights + $T = [Q_{\mathrm{tot}}, G]$" |
| `H-17` | Item 17: quadratic chiral duality $\Rightarrow$ Koszul theorem | replace with "quadratic dual + MC injection only; chiral Koszul homotopy theorem separate" |

---

## Phase I — §V voice / forbidden-pattern surgical purge (49 patterns)

Each pattern → scan all 26 files; per-instance fix.

| ID | pattern | replacement |
|---|---|---|
| `I-01` | matrix microscope\|brane microscope\|matrix probe | replace: trace measurement / Dirac-brane formal-stalk chart |
| `I-02` | platonic ideal in body prose | state structure directly |
| `I-03` | Theorem A / B / C labels in prose | refer by formula or theorem number |
| `I-04` | Wave N / Phase j / Round M / Session k | delete; state the mathematical content |
| `I-05` | we now turn to / having established / this section sharpens | state next math directly |
| `I-06` | is closely related to / corresponds to / is the analogue of (where exact) | $=$ or $\simeq$ with the morphism named |
| `I-07` | is wrong / would be / must not / fails to | positive construction; name objects + map |
| `I-08` | certificate / manifest / spec / schema | rational reduction / table / field-standard term |
| `I-09` | we hope / perhaps / remarkably / crucially / notably | state the result |
| `I-10` | $A$ is the primitive open algebra | $\mathcal{C}^{\mathrm{op}}_\partial$ on $(X,D,\tau)$; chart $b$ gives $A_b$ |
| `I-11` | $\mathrm{Bar}(A)$ is the bulk | $\mathrm{Bar}(A)$ twisting; bulk $= Z^{\mathrm{der}}_{\mathrm{ch}}(A) \simeq C^\bullet_{\mathrm{ch}}(A,A)$ |
| `I-12` | direct $\Phi: \mathrm{CY}_d \to \mathrm{ChirAlg}$ | $\Phi_d = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1},C} \circ \Phi^{\mathrm{FA}}_d$ |
| `I-13` | $A$ is modular | $\mathcal{C}^{\mathrm{op}}_\partial$ carries cyclic trace $\mathrm{Tr}_\mathcal{C}$ compatible with clutching |
| `I-14` | $\Delta_5$ = compact BPS Hilbert space | level-2 modular section of $\Omega_{\mathrm{central}}$; operator lift open |
| `I-15` | scalar $Z_{\mathrm{BPS}}$ = operator algebra | scalar = protected trace of still-to-be-constructed operator package |
| `I-16` | $W_\infty[\lambda] \Rightarrow E_\infty$ unconditional | conditional on the four hypotheses |
| `I-17` | formal Darboux $\Rightarrow$ compact target | formal-Darboux + descent + QME + anomaly + locality $\Rightarrow$ candidate |
| `I-18` | clearly / obviously | either delete or supply the chain of reasoning |
| `I-19` | it is well-known that | cite or supply the chain |
| `I-20` | it can be shown that / one can show that | show it or cite where it is shown |
| `I-21` | we shall see / as we shall see / in what follows | state directly; reference forward only if forced |
| `I-22` | let us / let us now / let us first | use mathematical statement, not 1st-person plural exhortation |
| `I-23` | this is reminiscent of / is similar to (where = / ≃ applies) | name the morphism and structure |
| `I-24` | roughly speaking / heuristically / morally | state strict form or move to flagged \hyp/\stmt |
| `I-25` | important / fundamental / key (without specific anchor) | name what is important and why |
| `I-26` | we will / will be / shall | present-tense statement of the construction |
| `I-27` | one might consider / one might hope | state or remove |
| `I-28` | it should be noted that / it is worth noting | state directly without metacommentary |
| `I-29` | thus / therefore / hence (overused chains) | first occurrence; suppress redundant linkers |
| `I-30` | above / below / following / preceding (without specific \ref) | use \ref or \eqref with explicit anchor |
| `I-31` | in some sense / in a sense / in some way | name the sense or remove |
| `I-32` | powerful / elegant / beautiful | state the mathematical content that makes it so |
| `I-33` | non-trivial / nontrivial (as standalone) | state what is non-trivial and the verification |
| `I-34` | etc. / and so on / et cetera | enumerate or prove the closure |
| `I-35` | a priori / a fortiori (where not strictly used) | remove or replace with mathematical statement |
| `I-36` | cf. / compare (without specific anchor) | \ref to the specific item |
| `I-37` | certain / some / various (vague qualifier) | name the specific instance |
| `I-38` | appropriate / suitable / convenient (as qualifier) | state the construction that makes the choice forced |
| `I-39` | Note that / Notice that / Observe that | remove; state the content as a sentence |
| `I-40` | Recall that (without immediate purpose) | use only when re-grounding; otherwise remove |
| `I-41` | Of course / Naturally / Indeed | remove or state what follows |
| `I-42` | we wish to / we want to / we would like to | state the construction or theorem directly |
| `I-43` | it remains to / it suffices to | state and discharge; do not announce intent |
| `I-44` | In other words / equivalently / i.e. | preserve only when restatement is genuinely informative; otherwise pick one |
| `I-45` | that is / namely / explicitly | preserve only when restatement is genuinely informative |
| `I-46` | see (Author Year) for details (without specific theorem) | \cite with explicit pin |
| `I-47` | a/an certain (article-+-qualifier hedge) | name the object |
| `I-48` | try to / attempt to | do or do not |
| `I-49` | we begin / we start with / we conclude | remove; mathematical statement is the beginning |

---

## Phase J — Convention firewall per-theorem-invocation (17 predicates)

| ID | predicate |
|---|---|
| `J-01` | Native $\C^2$ holomorphic $E_2$ taxonomy retained per theorem invocation; every curve-VOA reduction names: pushed-forward bracket + brane image + anomaly + BV pairing + $z_2$-mode or principal-part data |
| `J-02` | BV-degree / ghost-number / form-degree separation per theorem; appendix-sign-conventions.tex authoritative |
| `J-03` | Brane-preserving $\Omega$-background: $T_\Omega = \C^*_{\varepsilon_s} \times \C^*_{\varepsilon_1} \times \C^*_{\varepsilon_2}$, $Q_\Omega = Q + \iota_{V_\Omega}$ with $Q_\Omega^2 = L_{V_\Omega}$, inverted normal weights, residue-vs-Euler normalisation, stratified factorisation data — verify at every invocation |
| `J-04` | $\Omega^{\mathrm{rad}}_{a,b} \in \mathrm{coker}\,B_{a,b}$ theorem surface; decorated PBW Stokes obstruction for $D^\square_{a,b} = C^+_{a,b}\partial_2$ — verify per invocation |
| `J-05` | Larger non-scalar $\theta_3$ row evidence: CE ancestor OR scalar-zero Costello local counterterm OR complete companion-face table — explicit per invocation |
| `J-06` | BMK lane: one-pair pro-Matlis retract is NOT strict all-window; obstruction $\mathrm{Ob}^\Pi_{\mathrm{BM}}$ explicit per invocation |
| `J-07` | Larger non-scalar Costello / QME theorem requires seven-tuple (filtered scalar projection, finite row arrays, primitive matrix, transition matrices, Roos compatibility, centrality homotopies, curved bulk-to-defect kernel) — verify at every invocation |
| `J-08` | Vol II $\C \times \R$ chiral-topological apparatus invoked only after controlled reduction with explicit $z_2$-mode or principal-part data, pushed-forward bracket, BV pairing, brane image, anomaly matching |
| `J-09` | compact-CY / quintic / OSV / GV / Abel–Jacobi / CoHA / Igusa / BKM: each appearance flagged for explicit reopening per Agent Rule 7 |
| `J-10` | Holomorphic anomaly sign BCOV-strict per appendix-sign-conventions.tex |
| `J-11` | Negative-cyclic vs cyclic vs Hochschild homology distinguished at every reference |
| `J-12` | Holomorphic-symplectic Calabi–Yau datum is the trivial $\C^2$ volume / symplectic; not a compact CY3 assumption; not a BCOV theorem; not a license to import compact-target apparatus into the core local theorem surface |
| `J-13` | Capelli scalar $\hbar N[\bar c] = \Omega_{\mathrm{central}}\|_{J(f)}$ identification: projective curvature evaluation at the trace generator — explicit at every invocation |
| `J-14` | Modular line bundle on $\overline{\mathcal A}_g = \Omega_{\mathrm{central}}$ at level $g$; Igusa $\Phi_{10}$ is the level-2 section; $\Delta_5 = \Phi_{10}^{1/2}$ on the chosen paramodular branch |
| `J-15` | CE/PV dictionary $c_f \mapsto \theta_f$, $u_f \mapsto J(f)$ Koszul resolution of $C^\bullet_{\mathrm{ch}}(A_b, A_b)$ — every dictionary invocation cites the resolution |
| `J-16` | Costello–Gwilliam brane-link boundary $\partial X$ definition cited at every occurrence; no residual KN log structure invoked |
| `J-17` | Distinguish $\hbar$ (QFT loop expansion) from $g_s$ (string genus expansion) at every occurrence |

---

## Phase K — Cross-volume firewall (10 tasks)

| ID | scope |
|---|---|
| `K-01` | ~/chiral-bar-cobar/ (Vol I) shared symbols: chiral algebra, $\mathrm{Bar}$, $\mathrm{Cobar}$, $Z^{\mathrm{der}}_{\mathrm{ch}}$, $C^\bullet_{\mathrm{ch}}(A,A)$, chiral Deligne theorem — verify exact convention match |
| `K-02` | ~/chiral-bar-cobar-vol2/ (Vol II) shared symbols: $\C \times \R$ chiral-topological, $\mathrm{Vir}_c$ HT sector, 3d-gravity HT — verify reduction explicit when invoked here |
| `K-03` | ~/chiral-bar-cobar-vol4/ (Vol IV) architectural inheritance verified |
| `K-04` | ~/calabi-yau-quantum-groups/ (Vol III) shared symbols: $\Phi^{\mathrm{FA}}_d$, $\Phi_d$, $\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C}$, two-stage CY-to-chiral, Hall–Drinfeld, $\mathcal G(X) = D(Y^+(X))$ — verify match |
| `K-05` | ~/igusa-cusp-form/ shared symbols: modular line $\Omega_{\mathrm{central}}$, Igusa $\Phi_{10}$, $\Delta_5$, paramodular cover, level-2 modular section |
| `K-06` | ~/ecosystem/INVARIANTS.md §XIII code-writing-discipline + §XII raeez-math-template + repo-roster MATH_TEMPLATE_CONSUMERS — verify applied |
| `K-07` | Convention divergence audit: every divergence flagged with a comment, never silently reconciled |
| `K-08` | Antipatterns catalogue alignment: ~/chiral-bar-cobar/notes/antipatterns_catalogue.md, ~/calabi-yau-quantum-groups/notes/antipatterns_catalogue.md, ~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md — consult before edits in affected sections |
| `K-09` | ~/calabi-yau-quantum-groups/appendices/first_principles_cache.md — consult for shared first-principles patterns; append new shared confusions to ~/mixed-holomorphic-topological-strings/notes/first_principles_cache.md when recurrence $\geq 2$ per session |
| `K-10` | ~/.claude/projects/-Users-raeez-topological-strings/memory/MEMORY.md — consult for behavioral feedback; never write project memory contradicting it |

---

## Phase L — Compute-layer alignment (27 tasks)

| ID | scope |
|---|---|
| `L-01` | For every script in scripts/ (30 scripts), ensure manuscript has an anchor: \paragraph{Compute backing.} block citing the script and its load-bearing output |
| `L-02` | For every load-bearing computational claim in the manuscript, ensure a script verifies it; flag claims without compute backing in a separate registry notes/no_compute_registry.md |
| `L-03` | Re-run all 30 scripts; verify outputs match the equations claimed; flag any drift |
| `L-04` | audit_loop.py — verify its outputs are referenced where it claims to verify |
| `L-05` | check_adversarial_sweep.py — sweep verification anchored where invoked |
| `L-06` | check_audit_consistency_probes.py — eleven consistency probes anchored in main.tex |
| `L-07` | check_bch_cubic_cocycle.py — BCH cubic-cocycle output anchored |
| `L-08` | check_bi_infinite_lie_consistency.py — bi-infinite Lie consistency anchor |
| `L-09` | check_classical_super_sweep.py and N3 variant — anchors |
| `L-10` | check_derived_intersection_N2.py and N-extended — anchors |
| `L-11` | check_g2g3_attack_heal.py and transversality — anchors |
| `L-12` | check_higher_spin_jacobi.py — anchor |
| `L-13` | check_moyal_coefficients.py — anchor to Moyal star-product coefficients section |
| `L-14` | check_non_multiplicative_chiral_charge.py — anchor |
| `L-15` | check_one_psi_homology.py — anchor to single-$\psi$ homology bidegree theorem |
| `L-16` | check_pva_M2_degree3.py — anchor |
| `L-17` | check_pva_module_lambda_bracket.py — anchor |
| `L-18` | check_pva_module_z2_direction.py — anchor |
| `L-19` | check_sergeev_intertwiner.py — anchor |
| `L-20` | check_symp_functoriality.py — anchor |
| `L-21` | check_W5_A4_small_N.py — anchor |
| `L-22` | check_W5_X4_A5RG.py — anchor |
| `L-23` | finite_window_graph_array.py — anchor |
| `L-24` | quantum_shear_*.py (3 scripts) — anchors |
| `L-25` | quintic_arithmetic_rate_checks.py — anchor |
| `L-26` | build_architecture.py — verify build script invariants documented |
| `L-27` | delete-file-from-history — verify never invoked; remove if unused |

---

## Phase M — Bibliography / notation / acronyms (20 tasks)

| ID | scope |
|---|---|
| `M-01` | main.tex:16055,16068,16080 — remove or rewire orphan bibliography entries (kato-log, kato-nakayama-log, olsson-log-stack) post-KN→CG sweep |
| `M-02` | For every \bib{} entry in main.tex, verify cited from body; orphans → remove or wire |
| `M-03` | For every \cite{} in body, verify the bibliography entry exists; missing → add |
| `M-04` | Verify the citation pin (Vol/page/§) for every \cite{...}*{...} against the actual published source |
| `M-05` | local-dictionary.tex — verify every symbol used in the manuscript appears with unique definition; flag duplicates and orphans |
| `M-06` | mathmacros.tex — verify every macro is used; remove orphans; ensure no macro shadows a standard amsmath command |
| `M-07` | Acronym table — first-use expansion of: BCOV, BV, QME, VOA, OPE, CoHA, BKM, MNOP, DT, GW, PT, MC, CE, PV, HT, FA, RR, NS, KK, RG, SDR, KZ, BD, BPZ, hCS, GL, BMK, IR, UV, PVA, PBW, BCH, BCFT, AKSZ |
| `M-08` | Symbol consistency — $\R_t$ vs $\R_{\mathrm{top}}$ vs $\R^2_{\mathrm{top}}$ at every site (brane time vs topological factor) |
| `M-09` | Symbol consistency — $\mathcal A^{\mathrm{cl}}_{\mathrm{bulk}}$ vs $\mathcal A^{\mathrm{cl}}_{\mathrm{bulk}}\|_b$ vs $C^\bullet_{\mathrm{ch}}(A_b, A_b)$ vs $Z^{\mathrm{der}}_{E_1}(A^{\mathrm{cl}}_{\partial, N})$ — distinct objects, never conflated |
| `M-10` | Symbol consistency — $\mathrm{Tr}$ vs $\overline{\mathrm{Tr}}$ (full vs reduced) at every $J(f)$ occurrence |
| `M-11` | Symbol consistency — $\hbar$ vs $g_s$ — never use one for the other |
| `M-12` | Symbol consistency — $d$ — always $\dim_\C$ target; never overloaded with worldvolume or BV degree |
| `M-13` | Symbol consistency — $\phi_1, \phi_2$ (matrix coordinates) vs $\phi$ (BV ghost) — never collided |
| `M-14` | Symbol consistency — $\psi$ — moment-map antifield with $Q\psi = [\phi_1, \phi_2]$; never reused for fermion or other ghost without local renaming |
| `M-15` | Symbol consistency — $K$ vs $K^{(1)}_C$ vs $K^{(2)}_\Delta$ — central element vs Cauchy kernel; never conflated |
| `M-16` | Symbol consistency — $J(f)$ vs $\mathsf J_x(z)$ — trace map vs holomorphic current; never conflated |
| `M-17` | Symbol consistency — $\Omega_{\mathrm{central}}$ vs $\omega$ vs $\omega_b$ — projective curvature vs symplectic form vs Lie 2-cocycle; never confused |
| `M-18` | Symbol consistency — $\Theta_T$, $\mathfrak K_T$, $F_T$ — four-curvature taxonomy: each distinct, none conflated |
| `M-19` | Notation index in main.tex:2581 (ssec:intro-notation-index) — verify exhaustive and consistent with usage |
| `M-20` | Bibliography style — every \bib{} uses consistent fields; alphabetical by key |

---

## Phase N — Adversarial re-audit & convergence (15 tasks)

| ID | scope |
|---|---|
| `N-01` | RED-agent: independent first-principles re-read of every \thm and \prop statement and proof |
| `N-02` | BLUE-agent: independent search for all 17 seventeen-site catalogue patterns |
| `N-03` | GREEN-agent: independent §V voice scan + define-before-use + motivate-before-introduce scan |
| `N-04` | ORANGE-agent: convention-firewall scan — every theorem invocation honours the Theorem-control predicates |
| `N-05` | PURPLE-agent: cross-volume firewall — every shared symbol and concept matches |
| `N-06` | YELLOW-agent: bibliography + citation + label cross-reference completeness |
| `N-07` | GREY-agent: compute-layer anchor completeness |
| `N-08` | Each agent's flagged issue → loop back to Phase D / Phase E / Phase C on affected chunk |
| `N-09` | Final convergence build: make release clean, no LaTeX warnings, all five termination gates pass per CLAUDE.md |
| `N-10` | PDF dimensional integrity: page count, page numbers, hyperref targets, bookmarks, cross-references |
| `N-11` | Final voice audit: pass §V scan with zero violations across all 26 files |
| `N-12` | Final define-before-use audit: pass with zero violations across all 26 files |
| `N-13` | Final claim-strength audit: every conditional theorem has explicit "Status." or hypothesis ledger; every conjectural theorem labelled $\conj$ not $\thm$ |
| `N-14` | Final compute-backing audit: every load-bearing computational claim cites a verifying script |
| `N-15` | Final cross-volume audit: every shared symbol and concept matches the constellation |

---

## Execution order (dependency-respecting)

1. **Phase A** (meta-audits) — produce per-instance subtask lists for V-NNN, D-NNN, S-N-NN, CS-NNN, O-NNN, T-NNN.
2. **Phase M** quick wins — orphan bibliography (M-01), symbol consistency (M-08..M-18).
3. **Phase J** convention firewall — load-bearing for every theorem statement; enforce before Phase C attacks.
4. **Phase D + Phase C in parallel** — rectify each file, audit its theorems.
5. **Phase E** structural pass — confirm every section answers one question.
6. **Phase F + Phase L** compute alignment — anchor every script.
7. **Phase G + Phase M** bibliography + acronyms.
8. **Phase H + Phase I** generated surgical fixes — apply in batches.
9. **Phase K** cross-volume firewall — final pass before convergence.
10. **Phase B** per-commit audit — historical defects flagged; apply forward-only.
11. **Phase N** adversarial re-audit — RED/BLUE/GREEN/ORANGE/PURPLE/YELLOW/GREY agents; loop back on any flag.

---

## Notes

- Per Agent Rule "Make sure last several hundred commits read as if by [Kontsevich/Witten/Etingof/Polyakov/Dirac/Costello/Gaiotto]": Phase B audits the **content** of each commit. Voice rewriting cannot retroactively rewrite committed history without rebase + force-push (forbidden). Defects found in Phase B become forward-only Phase C / V-NNN / S-N-NN fixes.
- Agent Rule 6 binds: "Claim strength matches proof strength." Phase A-08, A-09, N-13 enforce.
- Forbidden destructive operations: `git stash`, `git reset --hard`, force push, `--no-verify`, history rewrite. Never invoked even if a "supremum form" would require it.
- Termination criteria (CLAUDE.md): every task closes only when Gate 0–5 pass for its affected scope.