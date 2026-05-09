# Wave 3 — W1 Attack Report — Kapranov + Definitions Lens

**Date.** 2026-04-28.
**Author.** Raeez Lorgat.
**Wave.** 3, agent W1.
**Lens.** Kapranov (higher-categorical coherence, derived geometry,
operadic packaging, descent obstructions) + Definitions (are objects
defined before use, and stable under the operations later applied?).
**Mode.** Read-only / proposal-only.
**Posture against waves 1 and 2.** Wave 1 declared a stable core
conditional on the C/Obligation-II/Schur heals. Wave 2 sharpened the
C-block from a 2-way to a 5-way split (M-26), promoted the universal
categorical no-go to the residue-duality framing (M-29), and
declared the eight-link DAG acyclic (M-33). The wave-2 master ledger
declares post-heal stable core with no residual fatal attacks. This
wave 3 W1 report probes that declaration through Kapranov's lens of
operadic / higher-categorical coherence and a mechanical
"defined-before-used" audit. The deliverable is **two new severity-3
attacks (W3-W1-01 and W3-W1-02), three sharpenings of wave-2
verdicts, and one confirmed residual** that the wave-2 declaration
does not yet name.

---

## §0. Files read (before mathematical work)

* `/Users/raeez/topological-strings/CLAUDE.md` (project instructions).
* `/Users/raeez/topological-strings/reconstitution/attack-heal-platonic-2026-04-28.md`
  (master ledger, 2194 lines: wave-1 M-01–M-25 + wave-2 M-26–M-37).
* `/Users/raeez/topological-strings/reconstitution/platonic-ideal-plan-2026-04-28.md`
  (lines 1–200; §3 theorem package via grep).
* `/Users/raeez/topological-strings/reconstitution/wave2-W1-costello-2026-04-28.md`
  (full, 710 lines; 5-way C₁/C₂ split details).
* `/Users/raeez/topological-strings/reconstitution/wave2-W6-beilinson-2026-04-28.md`
  (full, 604 lines; eight-link DAG L1–L8).
* `/Users/raeez/topological-strings/reconstitution/wave2-W4-etingof-2026-04-28.md`
  (universal no-go §3 lines 220–305; residue-duality §4 lines 276–305).
* `/Users/raeez/topological-strings/main.tex`:54 (`\alpharef` macro);
  1900–1994 (`constr:interval-fact-algebras`,
  `prop:brane-bracket-locality`); 2196–2220 (definitional reframe for
  $Z^{P_0}_{\mathrm{fact}}$); 2274–2305 (`prop:ce-source-obstruction`);
  2307–2320 (`rmk:ce-source-obstruction-disk`, perfectness);
  2322–2438 (Theorem C statement and proof);
  3323–3479 (`lem:continuous-bar-cobar` + `lem:linear-poisson-schouten`);
  3481–3522 (`prop:ce-koszul`); 3791–4205
  (Matlis principal-part block: `prop:principal-part-coadjoint`,
  `thm:canonical-residue-pairing`,
  `thm:principal-part-coadjoint-uniqueness`,
  `thm:no-polynomial-realization-categorical`).
* `/Users/raeez/topological-strings/local-dictionary.tex` (full).
* `/Users/raeez/topological-strings/principles.tex` (full).
* `/Users/raeez/topological-strings/theorem-lanes.tex` (full).
* `/Users/raeez/topological-strings/appendix-matlis-principal-parts.tex`
  (lines 1–455, all definitions and the Fourier-Rees bridge).
* `/Users/raeez/topological-strings/tate-T1-weighted-completion.tex`
  (lines 1–230, weighted construction); 184–220 (the
  product-coefficient asymmetry).
* `/Users/raeez/topological-strings/tate-T2-nilpotent-truncation.tex`
  (lines 400–579, $\mathfrak m^3$ truncation, Costello–Li precedent,
  summary).
* `/Users/raeez/topological-strings/tate-T3-quillen-equivalence.tex`
  (lines 46–150 admissible envelope; 280–470 Quillen equivalence,
  $\infty$-promotion, P₀-self-duality citation; 530–589
  Weiss-cosheaf residual).

---

## §1. Per-target attack findings

### Target T1 — The 5-way C₁/C₂ split (M-26)

The wave-2 split into C₁ᶠʷ, C₁ᶜᵒᵐᵖ, C₂(NT), C₂(W), C₂(R) is
operadically meaningful at the cochain level on the formal symplectic
disk. It is **not** uniformly meaningful as a statement about the same
target $\infty$-category of $P_0$-algebras, because the **target
category itself depends on which window is in force**. The Kapranov
lens locates one new defect and one sharpening.

#### W3-W1-01 — The five C-statements live in **five different
target $\infty$-categories**, only three of which have admissible
$P_0$-algebra structures inscribed

**Severity 3. Status valid. Confidence high.**
**Lens.** Kapranov primary; Definitions secondary.
**Provenance.** New, this wave. Sharpens M-26 / W1-04.
**Target.** Wave-2 master ledger §D / `lem:tate-mittag-leffler-dictionary`
plus the "five named theorems with disjoint admissibility" framing of
M-26 (master ledger 1431–1462, 1986–1998); the wave-1 / wave-2 prose
talks about "Theorem C" as a single Quillen equivalence promoted to
locally constant FAs via Lurie §5.5.4
(`tate-T3`:354–394, 442–467).
**Claim under attack.** Wave 2 claims (master ledger lines 1986–2007)
that C₂(NT), C₂(W), and C₂(R) are sibling theorems each carrying its
own "admissibility hypothesis" but each producing the same kind of
output — a $P_0$-algebra equivalence inside the admissible Tate
envelope of `stmt:tate-model-envelope`.
**Broken step.** The five sub-statements **do not share a target
category**, and three of the five are not currently equipped with the
$\infty$-categorical machinery the manuscript invokes.

* **C₁ᶠʷ.** Output is a strict cochain identity at finite CE-length.
  This is **prior** to any $\infty$-category structure; it is a
  generator-level identity in $\Cat{TateVec}$ chains. Calling it a
  "$P_0$-algebra equivalence" is a category mistake until the algebra
  on each side is completed. Kapranov: the operadic packaging
  $P_0=\mathrm{Comm}\circ\Lambda^\bullet[-,-]_S$ requires the
  underlying algebra to be a *complete* dg-commutative; finite-word
  truncations do not carry the operadic structure.

* **C₁ᶜᵒᵐᵖ.** Output is a strict cochain identity on completed
  algebras under a symmetric-filtration hypothesis. The completed
  algebras are objects of $\Cat{TateChain}_{\geq 0}^{\mathrm{adm}}$
  (`stmt:tate-model-envelope`, lines 46–57), and the model structure
  of `thm:tate-model-structure` is the right ambient for promotion.
  The Cattaneo–Felder $P_0$-Koszul-self-duality
  (`tate-T3`:447–449) is invoked at the operadic level; this requires
  the operad $P_0$ to be $\Sigma$-cofibrant in
  $\Cat{TateChain}_{\geq 0}^{\mathrm{adm}}$, which the manuscript
  asserts but does not prove. **Definition gap.**

* **C₂(NT).** $\mathfrak m^3/\mathfrak m^{N+1}$ is finite-dimensional
  and Tate-conilpotent (`tate-T2`:411–432). The output of C₂(NT) is a
  cochain isomorphism on each truncation; the "promotion" via
  inverse limit (`prop:colim-recovery`) requires the surjective
  transition system to be Mittag-Leffler — but C₂(NT)'s target Lie
  algebra is $\mathfrak m^3$, **not** $\mathfrak h$. So C₂(NT)
  inscribes $\Phi_{\mathfrak m^3}$, the cochain identification on the
  *truncated source*, not on $\mathfrak h$. The reader is left to
  infer that "C₂ on $\mathfrak h$" is the Tate inverse limit — but
  `rmk:colim-does-not-recover-full` (`tate-T2`:434–461) explicitly
  warns that this **does not recover** the low-degree sectors $H_1
  \oplus H_2$. So the target Lie algebra of C₂(NT) is **not the same
  Lie algebra as the target of C₂(W) or C₂(R)**.

* **C₂(W).** The weighted Tate pair
  $(\mathfrak h^w, \mathfrak h^{\vee, w}_{\mathrm{cont}})$
  (`tate-T1`:184–221) lives in **a different Tate coefficient
  category**: "the second factor is a product coefficient module,
  not the strict continuous dual" (T1:206–221). C₂(W)'s target
  $\infty$-category is therefore an $\infty$-category of $P_0$-
  algebras over the weighted-Tate envelope, *not* over the strict
  envelope of `stmt:tate-model-envelope`. Whether the model structure
  of `thm:tate-model-structure` and the Quillen equivalence of
  `thm:tate-bar-cobar-quillen` survive base change to the weighted
  envelope is **not proved**. T1's weighted construction proves the
  Casimir converges and gives a finite-window cochain identification;
  the $\infty$-promotion of T3 is not re-derived in the weighted
  envelope. **Definition gap.**

* **C₂(R).** Regulator-independent finite-window. This is a statement
  about *equivalence classes of local observables*, not about a Lie
  algebra (master ledger 270–273, R-W1-02). It does not output a
  $P_0$-algebra at all; it outputs a colimit of $P_0$-algebra
  fragments under a regulator-independence equivalence relation. The
  $\infty$-categorical structure of "regulator-independent local
  observables" is **nowhere defined in the manuscript**. **Definition
  gap.**

So the five sub-statements live in five different categorical homes,
with the operadic / model-categorical machinery *inscribed only for
C₁ᶜᵒᵐᵖ on the original strict Tate envelope*. C₂(NT) lives in a
truncated category; C₂(W) lives in a weighted category whose model
structure is asserted but not transferred from T3; C₂(R) lives in a
category of equivalence classes that is undefined.

**Evidence type.** definition_gap; missing_source.
**Evidence ref.** `tate-T3`:46–57 (admissible envelope, strict);
`tate-T1`:184–221 (weighted pair, different category);
`tate-T2`:434–461 (truncation excludes $H_1 \oplus H_2$);
master ledger 270–273 (R-W1-02 admits the unification problem);
`tate-T3`:442–449 (Cattaneo–Felder $P_0$ duality cited, not proved
in the Tate operad context); `tate-T3`:441 (the $P_0$ structure is
"transported via $\Phi$" — but transport requires the equivalence
to already be there).
**Files read.** As listed in §0.
**Confidence.** High.
**Blast radius.** The wave-2 declaration that the post-split C-block
"is stable" is precise *only for C₁ᶜᵒᵐᵖ on the formal symplectic
disk* and *for C₂(NT) at fixed N inside the truncation envelope*. The
*unified* statement "Theorem C is stable across all five
sub-statements" is **not a theorem** in the manuscript: it is five
separate theorems, three of which have target categories whose
$\infty$-categorical structure is asserted but not constructed.
**Minimal heal.**

* **WP3-W1-01-A.** In the wave-2 sharpening of M-26 / R-W1-02, mark
  C₂(W) as living in a **weighted Tate envelope** distinct from
  `stmt:tate-model-envelope`; require either a model-structure
  transfer lemma analogous to `lem:transferred-model` for the
  weighted envelope, or an explicit downgrade of C₂(W) from
  "$\infty$-categorical equivalence of $P_0$-algebras" to
  "model-categorical equivalence of cochain complexes plus
  finite-window Casimir convergence."

* **WP3-W1-01-B.** Promote `prop:colim-recovery` (the inverse limit
  on $\mathfrak m^3/\mathfrak m^{N+1}$) to a *named theorem* with
  explicit statement of which Lie algebra it lives on, and add a
  one-sentence remark that C₂(NT) is therefore a theorem about
  $\Phi_{\mathfrak m^3}$, not about $\Phi_{\mathfrak h}$.

* **WP3-W1-01-C.** For C₂(R), supply the missing definition: the
  $\infty$-category of "regulator-independent local observables" is
  $\mathrm{colim}_{q > 1}\,N_\Delta(P_0\text{-Alg}(\text{weighted env}_q))$
  along the comparison maps between weights, modulo the equivalence
  relation that two algebras agree iff every finite Taylor window
  agrees. Either inscribe this definition as a numbered Statement
  in `tate-T1` or `tate-P5`, or downgrade C₂(R) from "stable
  theorem" to "named obligation" until the colimit-of-categories
  machinery is supplied.

**Residual.** The above three heals are editorial-plus: WP3-W1-01-A
requires a small Tate-categorical transfer lemma; WP3-W1-01-C is
genuinely new content and may be relegated to Phase-4. The cleanest
posture is: **"C₁ᶜᵒᵐᵖ is the only sub-statement currently equipped
with the full $\infty$-categorical promotion of T3; C₂(NT) is at the
finite-truncation cochain level only; C₂(W) is at the weighted
cochain level only; C₂(R) is a colimit definition that needs to be
inscribed."**

**Adjudication.** Valid; sharpens M-26's R-W1-02 from "a unified
statement is not a Phase-1 deliverable" to a precise list of three
distinct definition gaps. Wave-2 verdict that "the C-block is stable"
is **partially overclaimed** — true for C₁ᶠʷ (no operadic structure
needed) and C₁ᶜᵒᵐᵖ (where T3 supplies machinery), but the C₂'s have
target-category gaps the wave-2 ledger does not name.

**Deciding evidence.** Either the three heals above, or an explicit
acknowledgment in §D / §E of the wave-2 ledger that "C₂(NT), C₂(W),
C₂(R) are cochain-level theorems; their $\infty$-categorical
promotions await separate transfer lemmas / colimit-of-categories
definitions."

#### W3-W1-02 — Hidden circular dependency: T3's admissible envelope cites $\alpharef$ item 1, which the dictionary lemma was supposed to replace

**Severity 3. Status valid. Confidence high.**
**Lens.** Definitions primary; Kapranov secondary.
**Provenance.** New, this wave. Cross-link to M-27 (Tate
Mittag-Leffler dictionary) and the wave-2 W6-02 HKR finding.
**Target.** `tate-T3`:46–57 (`stmt:tate-model-envelope`), 109–115
(`thm:tate-model-structure` proof item~(ii)), 301–303
(`thm:tate-bar-cobar-quillen` proof for the unit), 313 (proof for
the counit), 488–499 (`prop:quillen-vs-casimir`),
512–514 (proof of Casimir-independence).
**Claim under attack.** Master ledger M-27 says: author
`lem:tate-mittag-leffler-dictionary` and **redirect** every
`\alpharef\ item~1` invocation to the new dictionary lemma. The
wave-2 ledger declares R-05 healed by this redirection.
**Broken step.** I traced every `\alpharef\ item~1` in `tate-T3`,
not only in `tate-P1` (which W1's wave-2 finding handled). Three
invocations are *inside the proofs* of the model-categorical
infrastructure that the dictionary lemma itself would depend on:

1. `tate-T3`:114, in the proof that "every map in J-cell is a weak
   equivalence": "the filtered colimit of windowwise acyclic
   cofibrations is acyclic by Mittag-Leffler exactness in the Tate
   filtration (`\alpharef\ item~1`)."
2. `tate-T3`:301–303, in `thm:tate-bar-cobar-quillen` proof, item~(3)
   (unit weak equivalence): "Mittag-Leffler exactness in the Tate
   filtration (`\alpharef\ item~1`) lifts the windowwise qiso to a
   global filtered qiso."
3. `tate-T3`:313, in `thm:tate-bar-cobar-quillen` proof, item~(3)
   (counit weak equivalence): "The same Mittag-Leffler argument
   propagates to the abutment."

If `lem:tate-mittag-leffler-dictionary` is a **new lemma in
`tate-T3`** (as M-27 proposes), and the model structure of
`thm:tate-model-structure` is **used in the proof of the dictionary
lemma's promotion items (2)–(3)** (lift to filtered qiso), then we
have a circle: the model structure depends on Mittag-Leffler
exactness which depends on the dictionary lemma which depends on the
model structure for item (3) ("Tate-windowed quasi-isomorphisms lift
to filtered quasi-isomorphisms on $\varprojlim_w V_w$").

The circle is breakable: the dictionary lemma items (1) and (2)
are pure homological algebra (Roos / Grothendieck), and only item
(3) involves model-categorical lifting. So one can layer the proof
as: (i) prove dictionary items (1)–(2) without invoking the model
structure; (ii) use those to prove `thm:tate-model-structure`; (iii)
then prove dictionary item (3) using the now-existing model
structure. But the wave-2 / W1 phrasing of the dictionary lemma
states all three items together and cites Roos / Grothendieck for
all three. **Item (3) is not in Roos / Grothendieck**: it is a
filtered model-categorical lifting statement.

**Evidence type.** circular_dependency; proof_gap.
**Evidence ref.** `tate-T3`:114, 301–303, 313 (three `\alpharef`
invocations *inside the model-categorical proofs*); W1's wave-2
WP2-1 (lines 391–402) wording of the dictionary lemma item (3):
"Tate-windowed quasi-isomorphisms lift to filtered
quasi-isomorphisms on $\varprojlim_w V_w$"; this is a model-categorical
lift, not a homological-algebra Mittag-Leffler exactness.
**Files read.** Wave-2 W1 ledger; `tate-T3` lines 46–315.
**Confidence.** High.
**Blast radius.** The wave-2 declaration that R-05 is healed by
inserting the dictionary lemma is correct **only if** the dictionary
lemma is split into a homological-algebra core (items 1–2) and a
model-categorical extension (item 3). Without the layering,
inserting the unified dictionary lemma in `tate-T3` creates a
forward-reference cycle.
**Minimal heal.**

* **WP3-W1-02-A.** Restate `lem:tate-mittag-leffler-dictionary` as
  *two* lemmas:
  * `lem:tate-mittag-leffler-exactness` (items 1–2): pure
    homological algebra, citing Roos / Grothendieck Tôhoku Ch.~1.
    This is the lemma the model-structure existence proof and the
    Quillen-equivalence proof cite.
  * `lem:tate-mittag-leffler-lift` (item 3): the filtered
    model-categorical lift, proved *after* `thm:tate-model-structure`
    using the long exact sequence of the filtration plus
    two-out-of-three on weak equivalences (Hovey, *Model
    Categories*, §1.2).

* **WP3-W1-02-B.** Redirect the three `\alpharef\ item~1` invocations
  in `tate-T3`:114, 301, 313 to `lem:tate-mittag-leffler-exactness`
  (the homological-algebra core); redirect the seventeen other
  invocations across `tate-T3` and `tate-P1` per their content (most
  are item-(2) invocations and go to the core; a small number invoke
  item-(3) lift and should redirect to `lem:tate-mittag-leffler-lift`).

**Residual.** None at the layering level; the layered proof closes
without circular dependency. The remaining content is the explicit
verification at each `\alpharef` site that the surjective-transition
hypothesis holds.

**Adjudication.** Valid. Sharpens M-27 from "single dictionary
lemma" to "two-layer dictionary," exposing a forward-reference
hazard the wave-2 ledger does not explicitly name.

**Deciding evidence.** The two-layer dictionary lemma authored, with
the seventeen-plus three invocations redirected per item.

#### Confirmed-stable observations on T1

The wave-2 finding that **C₁ᶠʷ is hypothesis-free at the
finite-word generator level** (W1-01) survives the Kapranov probe.
Operadically, finite-word generator identity is a statement in the
free-operad-algebra category prior to completion, and Schouten /
CE differentials are derivations of degree 1 with explicit Koszul
signs (`lem:linear-poisson-schouten` lines 3440–3478, mechanical
verification). This level is below the operadic packaging issue of
W3-W1-01.

The wave-2 finding that **the formal symplectic disk has
filtration-tame structure constants** $C^L_{(a,b),(c,d)} = (ad-bc)
\delta_{L=(a+c-1, b+d-1)}$ landing in degree $a+b+c+d-2$
(`cor:derived-center-formal-disk` lines 2470–2503) survives. This is
the explicit symmetric-filtration verification W1's WP1-2 calls for,
and Kapranov's higher-coherence framing adds nothing — the
verification is a cochain calculation.

### Target T2 — The 8-link DAG (M-33)

The wave-2 W6 declaration of the eight-link DAG L1–L8 is acyclic
(W6-01) is **correct as a partial-order statement** but the
"morphisms" between links are not uniformly higher-functorial. The
Kapranov lens locates one new defect.

#### W3-W1-03 — DAG composition is set-theoretic implication, not natural transformation; "compose L_i and L_{i+1}" is not a single derived natural transformation in any inscribed sense

**Severity 2. Status valid. Confidence high.**
**Lens.** Kapranov primary.
**Provenance.** New, this wave. Cross-link to M-33 / W6-01.
**Target.** Wave-2 W6 §1 lines 118–149 (DAG declared acyclic);
master ledger §A M-33 (lines 1678–1715).
**Claim under attack.** The DAG L1 → L3 → L5 → L6 → L8 is
"acyclic" and the manuscript "composes" the chain.
**Broken step.** Wave-2 W6's DAG is set-theoretic: each link's
output is the next link's hypothesis, with the morphisms
**unspecified**. The links are not all of the same type:

* L1 (cosheaf-of-Lie) outputs an *object* (a cosheaf of dg Lie
  algebras on $\R$).
* L2 (dictionary) outputs a *morphism* (the source-convention
  generator dictionary).
* L3 (interval-wise CE/PV) outputs a *strict cochain isomorphism*
  $\Phi$.
* L4 (Tate conilpotency) outputs a *property* (windowwise
  conilpotency).
* L5 (Mittag-Leffler) outputs a *lift* of the windowwise iso to a
  filtered iso.
* L6 (locally constant cosheaf descent) outputs a *property* (cohomological
  local-constancy).
* L7 (disjoint-support locality) outputs a *property* (strict
  factorization product).
* L8 (Lurie HA §5.5.4 / CG Vol. I §6.4) outputs an *equivalence in
  an $\infty$-category*.

"Composing" L_i and L_{i+1} therefore mixes object-level, morphism-
level, property-level, and natural-transformation-level data. The
wave-2 W6 prose talks about "every output of a link is exactly the
hypothesis of the next" (lines 145–149) — but a property-level output
is not a hypothesis-level input in the same syntactic class without a
named functor that promotes property-to-hypothesis.

Kapranov: in derived geometry the correct shape is a single
**natural transformation of presheaves** of the relevant categories,
not a chain of implications. The wave-2 DAG is a partial order on
*claims*; it is not a diagram in any inscribed $\infty$-category.

The cleanest fix is to say: the chain is a sequence of conditional
implications between named statements, and the *target* of the
composition is the statement of `thm:open-closed-derived-center-derived`
(`tate-T3`:398–468). At that target, the natural transformation
exists (the explicit $\widetilde\Phi$ of T3); the eight links are
the **proof that this natural transformation is well-defined and
an equivalence**. The current wave-2 phrasing is suggestive of a
single derived 2-arrow that does not exist.

**Evidence type.** classification (the eight links are not of
uniform type); proof_gap (the "compose" wording is suggestive of
$\infty$-categorical structure not inscribed).
**Evidence ref.** Wave-2 W6 lines 36–115 (eight-link descriptions);
master ledger 1689–1714 (M-33 phrasing).
**Files read.** Wave-2 W6 full; master ledger §A M-33.
**Confidence.** High.
**Blast radius.** Editorial. The DAG is a correct dependency
diagram for the *proofs* of the eight statements; it is not, by
itself, a single $\infty$-categorical natural transformation. The
wave-2 verdict that "the chain composes" survives at the
proof-dependency level. The Kapranov-flavor concern is purely
about phrasing.
**Minimal heal.**

* **WP3-W1-03-A.** In any future inscription of the DAG into the
  manuscript or into the master ledger, replace "compose L_i and
  L_{i+1}" with "the proof of L_{i+1} uses the conclusion of L_i as
  a hypothesis." Reserve "compose" for the explicit
  $\widetilde\Phi$ of `thm:open-closed-derived-center-derived`.

**Residual.** None.

**Adjudication.** Valid as classification. The wave-2 W6 DAG is
correct; the "compose" wording is a Kapranov-level imprecision,
not a proof error.

**Deciding evidence.** The phrasing change.

#### Confirmed-stable observations on T2

The acyclicity of L1–L8 (W6-01) survives. The HKR risk inside L3 /
Step 1 (W6-02) is correctly named; this confirms the wave-2
diagnosis that the M-08 path (excise HKR, use local
$\mathrm{PV}$ definition) repairs L3 cleanly.

### Target T3 — Definitions health on stable-core dependencies

The Definitions lens audits whether the most load-bearing definitions
are inscribed before use and stable under the operations applied.
Five definitions audited:

#### Audit D-1 — $Z^{P_0}_{\mathrm{fact}}$

**Status: defined before use; stable.**
* Defined: `main.tex`:2212–2220 (definitional reframe; not an
  imported Costello–Gwilliam theorem).
* Used: `thm:open-closed-derived-center` (line 2346),
  `thm:hamiltonian-current-center-lift` (line 2225),
  `thm:open-closed-derived-center-factorization` (line 2018).
* Stable under: cochain isomorphism (Theorem C), interval
  factorization, locally constant FA promotion.
* **No defect.** Wave-1 W1-07 confirmed the definitional reframe is
  already in place; wave-3 W1 audit confirms no later silent
  upgrade.

#### Audit D-2 — Symbol algebra $\widehat{\mathbf S}_{\mathrm{Tate}}(\mathfrak h)$

**Status: defined before use; stable on the formal disk.**
* Defined implicitly via `lem:continuous-bar-cobar` item~(4)
  (`main.tex`:3365–3370): the PBW filtration's associated graded.
* Used: throughout Theorems C, D, E.
* Stable under: bar-cobar Quillen equivalence (T3); finite-window
  truncation (T2); weighted regulator (T1).
* **Minor defect (already named).** The completed-Tate symmetric
  algebra is not given a primary numbered definition; it is
  defined as the associated graded of $\widehat U(\mathfrak g)$. A
  reader looking for a first-principles definition has to derive
  it from the lemma. Not a fatal gap. Cross-link to W6-04
  presentability hypothesis (already inscribed in wave 2).

#### Audit D-3 — CE/PV derived-centre map $\Phi$

**Status: defined before use, except for one Kapranov defect.**
* Defined: `main.tex`:2337–2338 (on generators);
  2351–2367 (free extension to completed graded-commutative algebra
  on each side); 2381–2396 (extension to completed cochain identity).
* Used: every Theorem C consequence; T3's $\widetilde\Phi$
  promotion.
* **Kapranov defect (W3-W1-04).** The "free extension to completed
  graded-commutative algebra on each side" (line 2363–2367) treats
  $\Phi$ as a *unique* extension of the generator assignment — but
  there are two completed algebra structures on each side
  (filtration-by-CE-length vs filtration-by-Tate-window), and the
  uniqueness statement is only against one of them. The wave-2 W1-02
  (A1-08, inverse-map continuity) names this; the W1's WP1-1 heal
  proposes to make the symmetric filtration explicit on the
  exterior face. **The wave-3 audit confirms WP1-1 is necessary,
  not just cosmetic.**
* **Not a new attack** — sharpens W1-02 by noting that the
  Definitions lens reads the Theorem C statement at line 2363–2367
  and finds the uniqueness datum genuinely missing.

#### Audit D-4 — Matlis principal-parts module $\mathcal P$

**Status: defined before use; stable; one classification subtlety.**
* Defined: `appendix-matlis-principal-parts.tex`:74–104
  (`def:app-matlis-principal-parts`); 107–122
  (`prop:app-matlis-realization`).
* Used: `principles.tex` Principle 3; Theorems D₁/D₂/D₃; Theorem E
  cotangent factor; the universal categorical no-go (M-29).
* Stable under: residue calculus (Theorem D₁), T²-Cartan rigidity
  (Theorem D₂), `\mathfrak h`-action (`prop:app-matlis-coadjoint-action`),
  current extension $\mathcal P_I = \mathcal D'_c(I) \widehat\otimes
  \mathcal P$ (`local-dictionary.tex`:159–163).
* **Subtlety.** $\mathcal P$ is described in `appendix-matlis-principal-parts.tex`:117–122
  as "not asserted to be an $R$-submodule … the $\C$-linear scalar-
  annihilator dual to $\mathfrak h = R/\C \cdot 1$ … stable for the
  Hamiltonian coadjoint action." Definitions audit: the *vector
  space* $\mathcal P$ is well-defined; the *$\mathfrak h$-module
  structure* on it is **defined separately** by the residue pairing
  (`prop:app-matlis-coadjoint-action`); the *current
  extension* $\mathcal P_I$ tensors with compactly supported
  distributions. Each layer's Definitions are stable, but the
  compositional flow ("vector space → $\mathfrak h$-module →
  current extension") is not stated as a single named functor.
  Editorial only.

#### Audit D-5 — Residue pairing $\langle \rho, f \rangle = \mathrm{Res}_0(f \cdot \rho)$

**Status: defined before use; stable.**
* Defined: `appendix-matlis-principal-parts.tex`:97–103.
* Used: Theorem D₂, Theorem E current dual, residue duality of
  W4.
* Stable under: Symp_form-equivariance (M-05 / Theorem D heal,
  hypothesis-explicit per W2 audit).

#### Audit D-6 — Formal symplectomorphism action

**Status: defined before use, *partially stable*; one new defect.**
* Defined: `appendix-matlis-principal-parts.tex`:107–204 implicitly
  via the residue pairing's invariance; W2-04 / M-35 Symp-equivariance
  classification.
* Used: Theorem D's coordinate-independence; Theorem C's
  intrinsic Symp_form-equivariance; M-35 per-theorem catalogue.
* **Definitions defect.** The action of
  $\mathrm{Symp}_{\mathrm{form}}(\C^2, 0)$ on each object in the
  manuscript is **per-theorem** (M-35 catalogue, master ledger
  1744–1776), but no single object is given a "Symp_form-equivariant
  structure" as a numbered Definition. The wave-2 W2-04 heal calls
  for `prop:matlis-symp-functorial` in
  `appendix-matlis-principal-parts.tex`; this is **the missing
  definition**, not just a missing proposition. The wave-2 master
  ledger names this heal but does not flag it as a Definitions
  gap.
* **Cross-link.** This is a sharpening, not a new attack: the heal
  is already proposed in M-05 / WP-11. The Definitions audit just
  emphasises that it is a Definition gap, not just a missing
  proposition.

**Aggregate Definitions verdict.** Five of six definitions are
stable under the operations applied in stable-core dependencies. One
defect is a *sharpening* of a wave-2 heal: WP1-1's symmetric-filtration
hypothesis on $\Phi$ is necessary for D-3 to be a Definition rather
than an undisciplined extension. One subtlety (D-4) and one classification
gap (D-6) are editorial. **No new fatal Definitions defect emerges.**

### Target T4 — Universal categorical no-go (M-29)

The Wave-2 W4 universal no-go declares: any $\C[[\hbar]]$-linear
additive category $\mathcal C$ with a forgetful functor to
$\bar A_\hbar$-Lie-Mod cannot host an $M_\hbar$ with both fibre
conditions; the obstruction is at the Lie-module level.
The Kapranov lens probes whether a tensor-categorical / operadic
context can break the no-go.

#### W3-W1-05 — The universal no-go is universal **only on additive categories with a forgetful functor to Lie-Mod that preserves the Lie action on each fibre**

**Severity 3 (sharpening). Status valid. Confidence high.**
**Lens.** Kapranov primary.
**Provenance.** New, this wave. Sharpens M-29 / W4-06.
**Target.** Wave-2 master ledger lines 1532–1578 (M-29);
W4 ledger §3 lines 234–272 (universal no-go statement).
**Claim under attack.** "Any $\C[[\hbar]]$-linear additive category
$\mathcal C$ with a forgetful functor $\mathcal C \to \bar A_\hbar$-
Lie-Mod cannot host an $M_\hbar$ with both fibre conditions."
**Broken step.** The W4 statement's forgetful functor *preserves the
Lie action on each fibre* — i.e., the forgetful functor is required
to land in Lie-Mod with the **standard** action of $\bar A_\hbar$ on
both fibres. If one allows the forgetful functor to land in Lie-Mod
with a **deformed** Lie bracket on $\bar A_\hbar$ (say, the
Moyal/star bracket), then the no-go does not directly apply: the
PBW raising and Matlis lowering are then both formulas in a
Moyal-deformed Lie module, and the residue-duality sign-flip can be
absorbed into the deformation if the deformation has a Massey-product
expansion that interpolates raising and lowering at higher orders.

This is exactly the W4 R-W4-B (Bi-residue $L_\infty$-categorified
bracket) residual: a Tamarkin / Kontsevich-style $L_\infty$
deformation of $\bar A$'s Lie bracket allowing higher Massey-product
corrections. W4 names this as Phase-4 / open. The wave-3 sharpening:
**the universal no-go is universal *only at the Lie level*; it does
not extend to $L_\infty$-categorified brackets, and the W4 statement
should make this explicit.**

Specifically, the universal no-go works because every named
extension factors through Lie-Mod: derived $D_\hbar$-modules use
*polynomial multiplication* not Hamiltonian vector field; chiral
algebras use *vacuum vs Verma*; factorization use *bracket
deformation, not module deformation*; microsheaves use
*multiplication, not Hamiltonian vector field*; Tate enlargement
uses *standard local nilpotence*. The factoring through Lie-Mod
means the additive category sees the action through the standard
Lie bracket. An $L_\infty$-categorical extension does not factor
through Lie-Mod (the action lives in an $L_\infty$-module category,
which is *not* Lie-Mod), so the no-go does not apply.

**Tensor-categorical context where the no-go does not apply.**
Consider the dg category of $L_\infty$-modules over the
$L_\infty$-algebra $\bar A_\infty = (\bar A, [-,-]_S, m_3, m_4, ...)$
where the higher operations $m_k$ for $k \geq 3$ deform the Lie
bracket by the Kontsevich graph series. By Tamarkin's theorem
(Tamarkin, *Another proof of M. Kontsevich formality theorem*,
math/9803025), this $L_\infty$-deformation exists for any Poisson
manifold; for $\bar A$ the $L_\infty$-deformation gives the
quasi-classical limit of the Moyal star product. In this category,
the bi-infinite Lie module $\bar M$ of W4 §4 (lines 278–282) lifts
to a single $L_\infty$-module whose two specializations (positive
cone $\bar M^+$ and negative cone $\bar M^-$) coincide as
$L_\infty$-modules but appear as different cones at the level of the
underlying Lie module. The residue-duality sign-flip is then the
isomorphism between the two cones in the deformed category.

This is a *sketch*, not a construction; verification against the
21-case sweep at the $m_3$ level is required. But the sketch is
enough to show the no-go is universal **only on Lie-Mod, not on
$L_\infty$-Mod**.

**Evidence type.** sharpening; meta-level (the no-go's universality
quantifier is over Lie-Mod, not over $L_\infty$-Mod).
**Evidence ref.** W4 ledger lines 240, 255–270 (proof sketch, all
six cases factor through Lie-Mod); R-W4-B residual (lines 326–329).
**Files read.** Wave-2 W4 full.
**Confidence.** High.
**Blast radius.** The wave-2 declaration that "Obligation II is
closed in the negative for the four named extensions" survives.
The wave-2 phrasing of M-29 in the master ledger 1542 ("any
$\C[[\hbar]]$-linear additive category $\mathcal C$ with a
forgetful functor $\mathcal C \to \bar A_\hbar$-Lie-Mod") implicitly
restricts to Lie-Mod factorings, but does not say so explicitly. A
reader could mistake the universal quantifier for "any
$\C[[\hbar]]$-linear additive category whatsoever," which would
falsely close R-W4-B.
**Minimal heal.**

* **WP3-W1-05-A.** In M-29's statement, replace "any
  $\C[[\hbar]]$-linear additive category $\mathcal C$ with a
  forgetful functor $\mathcal C \to \bar A_\hbar$-Lie-Mod" with
  "any $\C[[\hbar]]$-linear additive category $\mathcal C$
  equipped with a forgetful functor to $\bar A_\hbar$-Lie-Mod
  that preserves the standard Lie action on each fibre." This
  makes the universal quantifier explicit on what kind of
  forgetful functor is in force.

* **WP3-W1-05-B.** Add a one-paragraph remark explicitly noting
  R-W4-B as outside the scope of M-29: "$L_\infty$-categorified
  modules with deformed bracket are not covered by this no-go;
  see R-W4-B."

**Residual.** None at the M-29 level. R-W4-B remains the open
question (already named).

**Adjudication.** Valid sharpening. The wave-2 universal no-go is
correct; the wave-3 attack is on the **scope of the universal
quantifier**, which the wave-2 phrasing leaves implicit.

**Deciding evidence.** The phrasing change (WP3-W1-05-A) plus the
explicit R-W4-B remark.

#### Confirmed-stable observations on T4

The W4 universal no-go survives the Kapranov probe **at the
Lie-module level**. The five named categorical extensions all
factor through Lie-Mod, and the Lie-Mod no-go applies. This is the
load-bearing wave-2 contribution; wave-3 W1 cannot break it within
the named scope.

The bi-infinite parent / residue-duality reframe of W4 §4 (lines
276–305) also survives. Operadically the bi-infinite parent $\bar
M$ is a single Lie module on $\Z^2$; the positive and negative
cones are subobjects, related by residue duality. This is
internally consistent and Kapranov-clean.

---

## §2. Confirmed-stable observations (where the wave-2 verdict held)

The wave-3 W1 probe **confirms the following wave-2 verdicts**:

* **C₁ᶠʷ stable, hypothesis-free** at the finite-word generator
  level (M-26 / W1-01). Operadically below the packaging issue.
* **C₁ᶜᵒᵐᵖ stable on formal symplectic disk** by direct
  symmetric-filtration verification (W1's WP1-2). Filtration-tame
  structure constants.
* **C₂(NT) stable on $\mathfrak m^3$**: cochain isomorphism on each
  truncation, inverse limit for the truncated Lie algebra. Modulo
  W3-W1-01 clarification that this is *not* on $\mathfrak h$.
* **C₂(R) is admissibility-only**, no $q \to 1^+$ limit (M-11).
  Strict-no-cy theorem holds.
* **R-05 healed** by `lem:tate-mittag-leffler-dictionary` (M-27),
  modulo W3-W1-02 layering.
* **8-link DAG acyclic** (M-33), modulo W3-W1-03 phrasing.
* **Universal no-go** at the Lie-Mod level (M-29), modulo
  W3-W1-05 quantifier scope.
* **Theorem D split into D₁/D₂/D₃** (M-28). Audited per Definitions
  D-4 and D-5; stable.
* **Theorem A finite-N derived intersection** (M-30 / W3 script).
  Outside Kapranov scope; verified by independent computation.
* **Cross-volume firewall** intact (M-34). Outside this report's
  scope.
* **Distribution-product avoidance structural** (M-36 / W6-08).
  Confirmed by audit of $P_0$-bracket on the abelian odd ideal.
* **R-03 four-ingredient closure plan** (M-37 / W6-07). Sharpened
  but unbroken by Kapranov probe.

---

## §3. New residuals (wave-3 originated)

* **R-W3-W1-01** (from W3-W1-01 / WP3-W1-01-A,B,C). Three
  Definition gaps: (i) C₂(W) needs a model-structure transfer to
  the weighted Tate envelope, or an explicit downgrade to
  cochain-level; (ii) C₂(NT) lives on $\mathfrak m^3$, not
  $\mathfrak h$, and the inverse-limit recovery should be promoted
  to a named theorem with explicit Lie-algebra target; (iii) C₂(R)
  needs a colimit-of-categories definition for "regulator-independent
  local observables." None of these is fatal at the cochain level.
  All three are Phase-1 / Phase-2 editorial-plus.

* **R-W3-W1-02** (from W3-W1-02 / WP3-W1-02-A,B). The
  Mittag-Leffler dictionary should be authored as **two layered
  lemmas**: a homological-algebra core (items 1–2) usable in the
  proofs of `thm:tate-model-structure` and
  `thm:tate-bar-cobar-quillen`, and a model-categorical lift (item
  3) proved after the model structure exists. This avoids a
  forward-reference circle that the wave-2 M-27 single-lemma
  formulation creates.

* **R-W3-W1-03** (from W3-W1-03 / WP3-W1-03-A). The wave-2 W6 DAG
  composition wording suggests a single derived natural
  transformation that does not exist. The DAG composes at the
  proof-dependency level only; the single $\widetilde\Phi$ of T3 is
  the actual natural transformation. Editorial only.

* **R-W3-W1-04** (Definitions D-3 sharpening of W1-02 / WP1-1).
  The symmetric-filtration hypothesis on $\Phi$ is a Definitions
  gap, not just a continuity gap. Wave-2 already calls for the
  heal; wave-3 emphasises that without it, the "extension to
  completed algebras" in `thm:open-closed-derived-center` proof
  (lines 2381–2396) is not a uniquely defined map.

* **R-W3-W1-05** (from W3-W1-05 / WP3-W1-05-A,B). M-29's universal
  quantifier is over additive categories with **standard
  Lie-Mod-preserving** forgetful functor. The phrasing should make
  this explicit; R-W4-B ($L_\infty$-categorified) remains outside
  scope.

---

## §4. Wave-3 minimal-heal proposals

### Tier 1 — Phrasing edits to wave-2 master ledger

**WP3-W1-T1-1** (W3-W1-03 / R-W3-W1-03). In master ledger M-33
(lines 1689–1714) and any future inscription of the eight-link DAG,
replace "compose L_i and L_{i+1}" with "the proof of L_{i+1} uses
the conclusion of L_i as a hypothesis." Reserve "compose" for the
explicit $\widetilde\Phi$ of `thm:open-closed-derived-center-derived`.

**WP3-W1-T1-2** (W3-W1-05 / R-W3-W1-05). In master ledger M-29
(lines 1542–1547) and W4 ledger §3 line 240, change "any
$\C[[\hbar]]$-linear additive category $\mathcal C$ with a
forgetful functor $\mathcal C \to \bar A_\hbar$-Lie-Mod" to
"any $\C[[\hbar]]$-linear additive category $\mathcal C$ equipped
with a forgetful functor to $\bar A_\hbar$-Lie-Mod that preserves
the standard Lie action on each fibre." Append a one-sentence remark
naming R-W4-B as out of scope.

### Tier 2 — Two-layer dictionary lemma (R-05 closure refinement)

**WP3-W1-T2-1** (W3-W1-02 / R-W3-W1-02). Replace M-27 / W1-WP2-1
single-lemma formulation by:

* `lem:tate-mittag-leffler-exactness` (homological-algebra core).
  Statement: under surjective transition with finite-dimensional
  pieces, $\varprojlim^{(1)} = 0$ and $\varprojlim$ is exact. Proof:
  Roos / Grothendieck Tôhoku Ch. 1.

* `lem:tate-mittag-leffler-lift` (model-categorical lift). Statement:
  under the model structure of `thm:tate-model-structure`, windowwise
  filtered quasi-isomorphisms lift to filtered quasi-isomorphisms on
  the inverse limit. Proof: long exact sequence of the filtration
  + two-out-of-three (Hovey *Model Categories* §1.2).

Order of presentation: exactness first, then model structure, then
lift. Redirect every `\alpharef\ item~1` invocation per content:
exactness invocations to the core; lift invocations to the lift.

### Tier 3 — C-block target-category honesty (M-26 sharpening)

**WP3-W1-T3-1** (W3-W1-01 / R-W3-W1-01). Replace the wave-2 master
ledger §D line 1986–2007 phrasing by:

> The post-split C-block, with explicit target categories:
> * **C₁ᶠʷ.** Cochain identity on finite-word truncations in
>   $\Cat{TateChain}_{\geq 0}^{\mathrm{adm}}$. No operadic packaging
>   required.
> * **C₁ᶜᵒᵐᵖ.** Cochain identity on completed dg-commutative
>   $P_0$-algebras in `stmt:tate-model-envelope`, under the
>   symmetric-filtration hypothesis (R-W1-01 / R-W3-W1-04).
>   Promotes via T3 to $\widetilde\Phi$ in
>   $\mathrm{Ho}(\mathrm{TateConilpCoAlg})$.
> * **C₂(NT).** Cochain identity on $\mathfrak m^3 / \mathfrak m^{N+1}$
>   for each $N$ and inverse limit on $\mathfrak m^3$. **Lives on
>   $\mathfrak m^3$, not $\mathfrak h$.** Operadic packaging via T3
>   model structure on the truncated Tate envelope.
> * **C₂(W).** Cochain identity on $(\mathfrak h^w, \mathfrak h^{\vee, w}_{\mathrm{cont}})$
>   in the **weighted Tate envelope** of T1. Whether the Quillen
>   equivalence of T3 transfers to the weighted envelope is open
>   (R-W3-W1-01-A); without it, C₂(W) is a cochain-level identity,
>   not an $\infty$-categorical equivalence.
> * **C₂(R).** Statement about *equivalence classes* of finite-window
>   local observables modulo regulator-independence. The
>   $\infty$-category of regulator-independent local observables is
>   not currently inscribed (R-W3-W1-01-C). Without it, C₂(R) is
>   an obligation, not a stable theorem.

This phrasing is honest about what is proved and where the
$\infty$-categorical promotion holds.

### Tier 4 — Definitions D-3 / D-6 inscriptions

**WP3-W1-T4-1** (Definitions D-3 / R-W3-W1-04). On the exterior face
of `thm:open-closed-derived-center` (`main.tex`:2322), insert the
symmetric-filtration hypothesis (W1's WP1-1). Replace "Tate
completeness of both sides plus continuity" (line 2394) with explicit
naming of the symmetric filtration on
$\widehat{\mathbf S}_{\mathrm{Tate}}(\mathfrak h) \widehat\otimes
\widehat\Lambda(\theta^I)$.

**WP3-W1-T4-2** (Definitions D-6). Author the missing Definition
in `appendix-matlis-principal-parts.tex`: "$\mathrm{Symp}_{\mathrm{form}}(\C^2, 0)$-equivariant
structure on $\mathcal P$" as a numbered Definition referencing
Hartshorne *Residues and Duality* III §10. This is M-05 / WP-11
sharpened to a Definition gap.

---

## §5. Wave-3 W1 verdict

The wave-2 stable-core declaration **survives at the cochain level
and on the formal symplectic disk**, but the Kapranov + Definitions
probe **sharpens** the verdict in three directions and **adds two
new severity-3 attacks** to the wave-2 master ledger:

* **W3-W1-01 (severity 3)**: C₁ᶠʷ, C₁ᶜᵒᵐᵖ, C₂(NT), C₂(W), C₂(R)
  live in five different target categories. Only C₁ᶜᵒᵐᵖ on the
  strict envelope has the full $\infty$-categorical machinery
  inscribed. C₂(W) needs a model-structure transfer to the weighted
  envelope; C₂(R) needs a colimit-of-categories definition. The
  wave-2 phrasing that the post-split C-block is uniformly stable
  is partially overclaimed.

* **W3-W1-02 (severity 3)**: M-27's single Mittag-Leffler dictionary
  lemma creates a forward-reference circle in `tate-T3` because
  three `\alpharef\ item~1` invocations sit *inside* the proofs of
  the model structure and the Quillen equivalence — and those
  proofs are needed for the dictionary lemma's item (3) lift. Layer
  the dictionary as exactness (homological algebra) + lift
  (model-categorical) and the circle is broken.

The wave-3 probe **confirms** ten wave-2 verdicts — including the
universal categorical no-go (M-29), the eight-link DAG acyclicity
(M-33), the Theorem D split (M-28), the cross-volume firewall (M-34),
and the distribution-product structural avoidance (M-36). The
universal no-go's quantifier scope (Lie-Mod, not $L_\infty$-Mod) is
implicit in the wave-2 phrasing; WP3-W1-T1-2 makes it explicit.

The wave-3 probe **adds** five new residuals (R-W3-W1-01 through
R-W3-W1-05), all editorial-plus or Phase-1 / Phase-2 inscriptions.
None is fatal.

The wave-2 stable-core verdict is **confirmed and sharpened**, not
broken. The five-way C-split survives but with explicit target
categories per sub-statement; the universal no-go survives but with
explicit Lie-Mod scope; the eight-link DAG survives but at the
proof-dependency level only.

---

## §6. Summary (200 words)

This W3-W1 Kapranov + Definitions probe of the wave-2 master
ledger's "stable core" verdict produced two new severity-3 attacks
and three sharpenings without breaking the verdict. **W3-W1-01**
locates that the five C-statements (C₁ᶠʷ, C₁ᶜᵒᵐᵖ, C₂(NT), C₂(W),
C₂(R)) live in five distinct target categories: only C₁ᶜᵒᵐᵖ on the
strict envelope has the full $\infty$-categorical apparatus
inscribed; C₂(W)'s weighted envelope needs a model-structure
transfer; C₂(R) needs a colimit-of-categories definition. **W3-W1-02**
locates a forward-reference hazard in M-27: the proposed
Mittag-Leffler dictionary lemma's items (1)–(2) are pure homological
algebra (Roos / Grothendieck), but item (3) is a model-categorical
lift used inside the very proofs of the model structure and the
Quillen equivalence the lift depends on; layer the dictionary into
two lemmas. **W3-W1-03** clarifies the W6 eight-link DAG composes at
the proof-dependency level, not as a single derived natural
transformation. **W3-W1-04** sharpens W1-02 / WP1-1 from "continuity
gap" to "Definitions gap." **W3-W1-05** sharpens M-29's universal
quantifier to Lie-Mod-only forgetful functors. The wave-2 stable
core is **confirmed and sharpened**, not broken. Full file at
`/Users/raeez/topological-strings/reconstitution/wave3-W1-kapranov-2026-04-28.md`.

---

End of W3-W1 report.
