# First-Principles Audit of the Mathematics and Physics — mixed-holomorphic-topological-strings

**Date:** 2026-07-10.
**State audited:** HEAD `7439716` ("release pdf", 2026-06-18) plus the
working tree (42 files modified; ~61K inserted lines uncommitted;
history shows a deliberate honesty repair `babcfef` "Correct
overclaims: honest trace-sector stalk theorem + global criteria").
Line numbers as of this read.
**Method:** two independent adversarial deep reads — (i) the main
formal-Darboux trace-sector stalk theorem (CE⊗Koszul model, Capelli
anomaly, Darboux pairing, HKR admissibility); (ii) the
obstruction-curvature taxonomy, determinant-line discipline, modular
lane, and cross-repo citations — with status conventions distrusted
and formulas recomputed. Companion audits in the four sibling repos
and `~/ecosystem/swarm-reports/`.

---

## 1. Executive verdict

**Overall grade: A−. The healthiest repository in the constellation.**
The proved core is real and survived every independent attack; the
scope discipline is exemplary (the failure modes a hostile referee
hunts for are each explicitly pre-empted in the text); the taxonomy is
mathematics, not an analogy table. Deductions are for altitude and
naming, not truth. Notably, this repo's CLAUDE.md *oversells* relative
to the more careful manuscript body — the inverse of the failure mode
found in Vols I–III.

## 2. Main theorem — grade **A−**

Statement `main.tex:10536` (proof 10853–10978, seven steps); intro
form `main.tex:369`; pillars: Koszul homotopy lemma 6985, reductive
exactness 5834, CE/PV ladder 10411, HKR target 10034, J-uniqueness
12000, Capelli section 17839–18423.

- **CE⊗Koszul model — SOUND.** Degrees correct (ghosts +1, ψ ∈
  gl_N[1] at −1, Q of degree +1); the gl_N-equivariance of
  Q — the condition making (d_CE + Q)² = 0 — is stated and proved
  (`main.tex:5886`), with invariants/cohomology commuting by linear
  reductivity, windowwise (5834–5906). Two traps a naive write-up
  would fall into are handled: the moment-map entries are *not* a
  regular sequence (N = 2: commuting variety dimension 6, codim 2,
  3 traceless equations, `main.tex:19201–19208` — referee's
  independent count agrees), so the cdga is the derived fibre; and
  the non-effective vs effective presentations differ by the genuine
  excess class [Tr ψ] (verified: no preimage by Koszul-weight
  counting). Referee redos passed: d² = 0 including the
  equivariance-dependent cross term; the Koszul homotopy identity
  with its no-extra-sign claim; the monomial bracket
  {J(z₁^a z₂^b), J(z₁^c z₂^d)} = (ad−bc)J(…) + N[{f,g}]₀ in three
  instances.
- **Capelli anomaly — SOUND at stated scope.** Both referees
  independently verified the normalization
  {Tr φ₁, Tr φ₂} = Σ_{i,k} δ^i_k δ^k_i = N and the quantum
  [Tr X, Tr Y] = ħ_W N with exact Moyal truncation for linear
  generators (`main.tex:18161–18236`); the cocycle lemma
  (17960–18030: ω = [{·,·}]₀ closed, exact on h_poly via
  η(f) = −[f]₀, non-exact on Ā since {z₁,z₂} = 1 ↦ 0) is correct;
  the congruence XY − YX + ħ_W N·I ≡ 0 mod 𝒲_N μ̂(sl_N) verifies.
  N = 1 reduction checks (gl₁ abelian, A^cl_{∂,1} = ℂ[φ₁,φ₂]⊗Λ,
  d = 0; manuscript's example 19158–19177 matches). Caveat: "Capelli"
  names only the order-one scalar shift ħN, and the text says so
  (18238–18243) — the headline word slightly oversells.
- **Darboux claim — SOUND, not decorative.** Two documented meanings
  with computed content: the chart torsor with change-of-chart
  transport (1406–1461) + uniqueness axioms (U1)–(U6) pinning J
  (12000–12117); and the actual degree-(−1) pairing
  {c^i, u_j} = δ^i_j, [θ^i, O_j] = δ^i_j (10143–10146). The strict
  pair does not carry the diagonal Casimir — hypothesis (C3)
  explicitly denies it, and the completed P₀ claim is correctly
  restricted to the weighted Tate tier (10786–10797).
- **HKR admissibility — SOUND but tautological-by-design.** Each
  finite window is polynomial, where classical HKR is genuine; the
  completed target is *defined* through the finite-window HKR maps
  and the text says exactly that (10082–10106), with the honest
  continuous-Hochschild comparison explicitly out of scope
  (10076–10079). One framing gap: CLAUDE.md calls the target "the
  admissible HKR model for the **chiral** Hochschild cohomology";
  the manuscript's target is the E₁/HKR model plus a separate
  holomorphic kernel operad, with the three E₂-structures explicitly
  *not* identified (`main.tex:168–177`). The body is more careful
  than its own summary file.
- **Convention flag:** "C•_CE(T*[1]𝔩)" places u in degree 0 rather
  than the standard +2; consistent as a regrading (it makes the PV
  comparison degree-preserving) but deserves a remark at the
  definition.

## 3. Taxonomy, determinant lines, modular lane — grade **A−**

Core: `appendix-master-deformation-complex.tex` (six native
deformation problems :157–256; four-mechanism theorem :314–424 with
six-row ledger :351–422; common-complex datum (K1)–(K4) :438–507;
Ω-localization collapse :749–861, a real localization homotopy;
six-coordinates-one-curvature :886–949). Determinant-line lane
`main.tex:17839–18423`; global comparison
`typed-boundary-open-closed.tex:4657–5275` with the ten-row typed
ledger :4763–4777.

- Five of the six ledger rows carry typed obstruction maps with
  stated source/target and in-repo anchored proofs (all six anchor
  labels resolve); the sixth (modular clutching) is the one lane
  with no in-repo typed morphism — and the manuscript says so,
  assigning the data to Vols II/III. Two formulas attacked from
  first principles verify exactly, including signs: the
  Bochner–Martinelli window-leak z₁^{N+2}·ρ_{N+1,0} = −(N+2)ρ_{0,1}
  with projected Jacobiator (N+1)(N+2)ρ_{0,1} ≠ 0
  (`tate-P1-hadamard-mittag-leffler.tex:2852–2929`), and the
  ħ_W N[c̄] cocycle chain.
- **Determinant-line discipline: observed, but the conditional
  theorem is definitionally vacuous.** No unconditional slip at any
  of nine sampled sites; the definition is honest ("constructs
  neither an object of 𝖫ine^∇_J nor the identification η_J",
  18326–18328). But `thm:capelli-projective-anomaly`'s conditional
  direction unwinds its own definition — η_J *is* the supplied
  identification, so nothing is computed (18393–18398). No
  Quillen/Bismut/BGS computation exists; no candidate line is
  constructed. The Capelli row of the taxonomy currently classifies
  without comparing. A genuine conditional theorem (e.g. Quillen
  curvature of a ∂̄-determinant on the trace chart = ħ_W N[c̄]) is
  absent and unclaimed — the honest next theorem to write.
- **Modular lane: correctly deferred.** Projective clutching law
  displayed as the *shape* of a deformation problem and immediately
  routed to Vols II/III; the only g ≥ 2 object is Φ₁₀ inside an
  explicitly open conjecture (19588–19639) with "does not prove a
  compact K3×E partition-function identity" (19626–19628). Defects:
  Ω_central used (`main.tex:11818, 19599`) but defined only in
  CLAUDE.md; "level-2" for 𝒜̄₂ conflates genus/degree with level
  structure.
- **Cross-repo hygiene: no laundering found.** Exactly one explicit
  volume citation in the body, routed through an in-repo typed
  obstruction; the K3×E tuple (0,0,3,5,24) appears only inside a
  conjecture with independently correct glosses; the
  Reference Dependency Ledger
  (`appendix-theorem-status-referee-checklist.tex:160–241`), stating
  for each external input what it is *not* used to prove, is
  exemplary and worth copying into the sibling repos.
- Caveats: the four-mechanism theorem is a near-tautological case
  division whose own caveat (:322–324) concedes it is not a
  partition without extra data; `prop:six-projections` is openly
  definitional; the referee appendix files that supplied-data
  criterion under "Proved" (:77–80) where "criterion" is accurate.

## 4. Systemic diagnosis

This repo demonstrates that the constellation's discipline *can* be
executed: hypothesis packages in-statement, typed obstructions for
everything not proved, negative results proved where cheap, an
explicit ledger of what each citation does NOT support, and a git
history containing its own overclaim-correction commit. Its residual
defects are the mirror image of the siblings': the summary layer
(CLAUDE.md) is the least reliable document in the repo — it names a
chiral target the body declines to claim, states a constellation
slogan ("modular structure = trace plus clutching") the body
correctly weakens, and defines a symbol (Ω_central) the body uses.

## 5. Triage (ordered)

1. Sync CLAUDE.md down to the body: chiral-Hochschild target →
   E₁/HKR + kernel operad phrasing; constellation slogan → the
   body's deferral statement; move Ω_central's definition into the
   manuscript.
2. Write the genuine conditional determinant-line theorem (Quillen
   curvature on the trace chart) or mark the Capelli taxonomy row
   "classification only, comparison open".
3. Add the u-degree regrading remark at the C•_CE(T*[1]𝔩)
   definition; fix "level-2" → genus-2/degree; reclassify the
   six-projections item from "Proved" to "criterion" in the referee
   appendix.
4. Optional altitude: the "Capelli"/"formal Darboux" naming — either
   earn the names (higher Capelli identities; a shifted-symplectic
   Darboux theorem) or add one sentence each scoping them.

**Provenance.** Both referees performed independent recomputations
(d² = 0, N = 1, monomial brackets, BM leak Jacobiator, cocycle
normalization — all pass); my own check of the {Tr φ₁, Tr φ₂} = N
normalization concurs. No mid-audit drift observed beyond the
pre-existing uncommitted working-tree state.

---

# Part II — Mathematical yield (fresh-eyes pass, same date)

Stricter second pass: referee forbidden from reading CLAUDE.md,
notes/, status appendices, or Part I; graded only
**true + proved + new** against the actual literature; hypothesis-
contains-conclusion = zero. Part I's A− was a *process* grade; this
is the mathematics grade.

**Yield grade: C.** No false claims found (confirming Part I). But
the unconditional core, measured against the literature, is the
**classical trace-sector layer of the twisted-M-theory Dirac-brane
dictionary** — the gl_N-BRST commuting-pair algebra, J(f) = Tr f,
{Tr f, Tr g} = Tr{f,g} + N[{f,g}]₀, the Capelli shift ħN via Moyal —
i.e. the tree-level layer of Costello (1610.04144, M2-brane paper),
Gaiotto–Oh, Budzik–Gaiotto, Gaiotto–Rapčák, with the central term N
known since collective field theory. That literature is cited only
as "physical motivation" (main.tex:8391–8397); Gaiotto, Budzik,
Rapčák, Gan–Ginzburg, Oh–Zhou are absent from the bibliography.
Additionally, the stable trace-sector computation
(`prop:brane-ops`, main.tex:7565–7607) **is** the
Berest–Khachatryan–Ramadoss stable representation-homology theorem
(Adv. Math. 2013) specialized to ℂ[x,y], combined with Loday's
HC(ℂ[x,y]) — entirely uncited (zero matches for
Berest/Ramadoss/representation homology).

**True + proved + NEW (strict, complete list):**
1. The **uniqueness theorem for J under (U1)–(U6)**
   (main.tex:12000–12344): existence by construction, uniqueness via
   Procesi + LQT primitivity + linear shears + the nonlinear flow
   z₁ ↦ z₁ − tz₂ᵏ; (U4),(U5) shown essential by explicit
   counterexamples, (U1)–(U3) shown to be codomain specifications.
   Verified line-by-line, no smuggled axiom. New (no published
   axiomatization of Tr f(X,Y) by formal-symplectomorphism
   naturality is known), correct — and lemma-to-small-proposition
   weight; strictly weaker than Costello's quantum rigidity. One
   gap in the *secondary* rigidity claim only (the "(U6) is
   redundant" induction, main.tex:12292–12295, is proved only in
   bidegree (1,1); the main theorem does not depend on it).
2. A **new combinatorial proof of a known theorem**: the one-ψ trace
   homology line via the cyclic-word cell complex and equivariant
   Abel map (main.tex:6855–6948) — the result itself is
   BKR/Loday (HC₁ of ℂ[x,y]).
3. The window-truncation obstruction with explicit Jacobiator
   (N+1)(N+2)ρ₀,₁ and the pro-Matlis repair (tate-P1:2790–2939) —
   correct, new-but-trivial (the truncated coadjoint tail is
   obviously not a submodule).
4. The weighted pro-Matlis continuity estimates
   (appendix-completion…:561–647) — correct, routine, new only in
   the sense that nobody bothered.

**What the main theorem unconditionally proves**, stripped: the
trace map descends to the derived commuting stack; its bracket is
J({f,g}) + N[{f,g}]₀; and after scalar reduction/stable trace
passage the CE model matches the polyvector model with J the
coordinate. The Hochschild/E₂/quantum tiers (H), (K), (Q) are
definitions of the data whose existence would be the interesting
theorem (main.tex:10668–10694, 10760–10763) — zero yield by the
strict rule, exactly as the abstract itself concedes.

**A CMP referee's summary:** a careful, correct,
completeness-obsessed exposition of the classical layer, containing
one new lemma-level characterization theorem, one new proof of a
known computation, and honest functional analysis; not acceptable as
a new-results paper without the novelty comparison against
Costello/Gaiotto-circle and BKR that the manuscript currently does
not attempt.

**Consequences for Part I:** the A− stands as a correctness/process
assessment; as mathematics the volume is a strong exposition plus
one new lemma. Triage additions: add the missing literature
(Costello 1610.04144 as content, Gaiotto–Oh, Budzik–Gaiotto,
Gaiotto–Rapčák, Berest–Khachatryan–Ramadoss, Loday) with an explicit
novelty delta; either promote the (U1)–(U6) theorem to a standalone
short paper or scope the manuscript as exposition-plus-lemma; prove
or drop the secondary (U6)-redundancy induction.

---

# Part III — Healing ledger (2026-07-10, same date)

All five repairs of the healing directive executed. Line numbers are
current as of this ledger. Both pdflatex draft passes exit 0 with zero
undefined references and zero undefined citations (667 pp).

## 1. Literature confrontation (uncited overlap) — DONE

**Bibliography** (8 new amsrefs entries, all bibliographic data
verified against arXiv/publisher before inscription):
`berest-khachatryan-ramadoss` (Adv. Math. 245 (2013) 625–689,
arXiv:1112.1449) main.tex:20109; `bismut-gillet-soule-III` (Comm.
Math. Phys. 115 (1988) 301–351) :20149;
`budzik-gaiotto-twisted-holography` (JHEP 12 (2023) 104,
arXiv:2211.01419) :20183; `costello-m2-koszul` ("Holography and
Koszul duality: the example of the M2 brane", arXiv:1705.02500)
:20271; `gaiotto-oh-omega` (JHEP 12 (2024) 184, arXiv:1907.06495)
:20395; `gaiotto-rapcak-miura` (JHEP 01 (2022) 086, arXiv:2012.04118)
:20406; `loday-cyclic-homology` (Grundlehren 301, 2nd ed. 1998)
:20636; `quillen-determinants-cr` (Funct. Anal. Appl. 19 (1985)
31–34) :20834. Costello 1610.04144 was already present as
`costello-twistedM`.

**Novelty-delta paragraph** — main.tex:206–262, block "Relation to
the literature: the novelty delta" in the Summary, immediately after
"New mathematical content". States: brane algebra + quantum rigidity
= Costello; classical trace dictionary incl.
{Tr f, Tr g} = Tr{f,g} + N[{f,g}]₀ and ħN shift = tree-level stratum
of Gaiotto–Oh / Budzik–Gaiotto / Gaiotto–Rapčák; prop:brane-ops = BKR
stable representation homology at A = ℂ[x,y] + Loday. Claims as new
exactly: (i) (U1)–(U6) uniqueness theorem, (ii) finite-window /
pro-Matlis completion analysis with continuity estimates
(thm:bmk-finite-window-obstruction,
prop:completion-promatlis-continuity), (iii) typed obstruction
ledger. Explicit non-claims closing sentence.

**Point citations at each overlap:**
- main.tex:8487–8508 — Costello paragraph rewritten from "physical
  motivation" to source-of-the-system confrontation
  (costello-twistedM + costello-m2-koszul quantum rigidity +
  the three brane-dictionary papers).
- main.tex:15059–15078 — new Remark `rmk:trace-dictionary-provenance`
  after cor:local-bulk-boundary-coupling: the bracket identity and
  its central refinement are the classical layer of the
  twisted-M-theory dictionary; proofs self-contained; identity not
  new; new = axiomatization + typed ledger.
- main.tex:18086–18098 — Capelli section head: ħ_W N shift "is not
  new" — central term of the brane trace algebra in
  costello-twistedM / costello-m2-koszul / gaiotto-oh-omega; the
  section's contribution scoped to cocycle-level bookkeeping.
- main.tex:7680–7702 — new Remark `rmk:brane-ops-bkr-loday` after
  prop:brane-ops: the statement is
  Sym(HC̄(A)) ≅ H(DRep_∞(A))^{GL_∞} (BKR) at A = ℂ[x,y] (DRep_N =
  derived commuting scheme) + Loday's HC̄₀, HC̄₁, HC̄_{≥2} of
  ℂ[x,y]; "the statement is not new", proofs independent.
- main.tex:7008–7020 — new Remark `rmk:one-psi-known-computation`
  after the cell-complex proof: new proof of a known computation;
  the one-ψ line in bidegree (k,l) is the bidegree-(k+1,l+1)
  component of HC̄₁(ℂ[x,y]) = Ω¹/dℂ[x,y] (checked: 2-dim forms mod
  1-dim exact = 1-dim line, matching all k,l ≥ 0 including axes).

## 2. Secondary rigidity induction (the proof gap) — CLOSED BY PROOF

main.tex:12433–12520 (thm:Jf-uniqueness-rigidity, item "Removing
(U6) with (U4) intact"). The asserted induction is replaced by a
complete two-step argument, per total degree k ≥ 2 in window W = k,
N ≥ k:
- Step 1 (axes): (U4) for the nonlinear flow z₁ ↦ z₁ − tz₂^k applied
  to the *linear* monomial z₁; the matrix side
  Tr(φ₁ − tφ₂^k) is manifestly single-trace, so matching the
  t¹-coefficient in the Procesi stable monomial basis kills the
  multi-trace part M_{0,k} and sets c_{0,k} = 1 in one stroke:
  J̃(z₂^k) = T_{0,k} exactly. Transposed flow: J̃(z₁^k) = T_{k,0}.
- Step 2 (transport): (U4) for the linear shear z₂ ↦ z₂ + tz₁
  applied to z₂^k (now pinned); expanding Tr((φ₂+tφ₁)^k) by Koszul
  descent and matching each t^j gives c_{j,k−j} = 1 and
  M_{j,k−j} = 0 at every mixed bidegree.
Soundness note recorded in-proof: neither step evaluates Φ_* on an
unknown multi-trace element (only on pinned single traces), so the
argument stays inside lem:formal-darboux-action-trace-sector; window
compatibility + m-adic continuity give J̃ = J. The old bidegree-(1,1)
α-family is retained as the illustrating instance. The theorem
statement ("given (U1)–(U5), (U6) is automatic") is now proved as
stated; no downgrade needed. Main uniqueness theorem untouched.

## 3. CLAUDE.md sync down to the body — DONE

- (a) CLAUDE.md "What this manuscript proves" (¶ after the display),
  "master architecture" closing line, chapter-5 line, and
  convention-layer CE/PV line: "admissible HKR model for the chiral
  Hochschild cohomology C•_ch(A_b,A_b)" replaced by the body's
  honest typing — admissible E₁/HKR polyvector model
  HH•_{adm,HKR}(A^st_{∂,H}, A^st_{∂,H}) via finite-window HKR +
  Roos limit; explicit disclaimer that the holomorphic kernel operad
  is separate data and the three E₂-structures are not identified.
- (b) Constellation slogan block rewritten: closed sector = *target*
  of the comparison, comparison = ten-row criterion; "modular
  structure = trace plus clutching" → clutching law displayed as
  shape, data deferred (conj:operator-modular-lift); scalar
  invariants only after the line datum.
- (c) Ω_central definition MOVED into the manuscript at first use:
  new Remark `rmk:omega-central-definition`, main.tex:11950–11977
  (Compact modular-line addendum) — Hodge determinant line λ on
  𝒜̄_g, Siegel forms of degree g weight k as sections of λ^k,
  Φ₁₀ = χ₁₀ ∈ H⁰(𝒜̄₂, λ¹⁰), Δ₅ branch on the paramodular cover.
  CLAUDE.md convention-layer entry now points at that remark instead
  of carrying the definition. Cross-references added at the other
  use sites (main.tex:19918, appendix-higher-factorization-
  categories.tex:2288).

## 4. Small manuscript fixes — DONE

- (a) u-degree regrading: new Remark `rmk:u-degree-regrading`,
  main.tex:10332–10360, after thm:coordinate-free-cotangent-ce-pv —
  standard Sym((k[1])∨) places u in degree +2; the manuscript
  regrades by −2·(u-weight); consistency (d_CE preserves u-weight)
  and purpose (degree-preserving Φ_𝔩 against |O_x| = 0) stated.
- (b) level/degree conflation: main.tex:968 ("degree-two scalar
  section", with explicit "degree (genus) 2 for the full group
  Sp₄(ℤ), not a form of higher level"); main.tex:19916 (conjecture:
  "degree-(2) projective modular class");
  appendix-higher-factorization-categories.tex:2291, 2358. The
  "level-1/level-2" occurrences at main.tex:9221/9244/19034 are the
  coordinate-tier/P₀-tier sense, not modular level — untouched.
  CLAUDE.md level-2 wordings fixed in the same sync (constellation
  table, architecture diagram, forbidden-patterns table).
- (c) appendix-theorem-status-referee-checklist.tex:77–81 — the
  conflated "Four-curvature taxonomy and six-coordinate obstruction
  projection / proved" row split: Proved table now carries only
  "Four-mechanism obstruction taxonomy — proved case division; a
  partition only after the comparison-unifying datum"; new row
  :94–103 in the Supplied-Data table: "Six-coordinate obstruction
  projection onto one curvature — supplied-data criterion" with the
  three required data named.
- (d) appendix-master-deformation-complex.tex:319–327 — exclusivity
  caveat promoted into the statement of thm:four-curvature-taxonomy:
  "The theorem asserts a case division, not a partition …", with the
  partition condition and "no such datum is constructed here"
  explicit in-statement.

## 5. Empty determinant-line cell — DONE (honest restatement + named problem)

- (a) thm:capelli-projective-anomaly statement (main.tex:18595–18617)
  and proof close (:18648–18659): the supplied-lift clause is now
  typed as definition-unwinding — η_J *is* the identification
  At_J(L,∇,ι) = ħ_W N[c̄], so the clause records the compatibility
  interface of the supplied datum and computes nothing; "no
  determinant line, metric, or connection is constructed here."
- (b) New `prob:quillen-curvature-trace-chart`
  (main.tex:18688–18746): Quillen curvature of the ∂̄-determinant
  line on the trace chart = ħ_W N[c̄]. Required data listed:
  (1) candidate line det Rπ_* of a family of ∂̄-operators coupled to
  the rank-N Chan–Paton bundle over the formal trace chart, with the
  finite-window / compactified-fibre replacement of compactness
  named; (2) Quillen metric; (3) Chern/Bismut–Freed connection;
  (4) evaluation of ι. Comparison route named: Quillen 1985 + BGS III
  (GRR integrand), matched against Nω(z₁,z₂) = N. Closing sentence
  records that a solution fills the comparison cell of the Capelli
  taxonomy row, "which at present classifies the anomaly without
  comparing." No proof inscribed — none exists; the named problem is
  the heal.

## Verification and leftovers

- Two draftmode pdflatex passes: exit 0, 667 pages, no undefined
  references, no undefined citations; verification build directory
  removed.
- All new labels unique; all referenced labels and cite keys resolve
  (checked mechanically).
- Not done, out of directed scope: Gan–Ginzburg and Oh–Zhou (named in
  Part II's diagnosis but not in the directed repair list or final
  triage sentence) were not added; the Part II suggestion "promote
  the (U1)–(U6) theorem to a standalone short paper" is an editorial
  decision left to the author; no operator-level Quillen computation
  was attempted beyond the named problem (completing it requires
  constructing the ∂̄-family over a formal pro-scheme — the exact
  obstruction is recorded inside prob:quillen-curvature-trace-chart).
