# Wave 3 — W11 Attack Report — Beilinson + Hypotheses Lens

**Date.** 2026-04-28.
**Author.** Raeez Lorgat.
**Wave.** 3, agent W11.
**Lens.** Beilinson (sheaf-theoretic, descent, filtrations, spectral
sequences, exactness) primary; Hypotheses (which theorem hypotheses
are missing, weakened, or silently strengthened?) secondary.
**Mode.** Read-only / proposal-only. Master ledger schema; IDs prefix
`W3-W11-`.
**Posture.** Five Wave-3 attackers (W1, W2, W4, W5, W6) returned;
the wave-2 declaration that the C-block, the eight-link DAG, and the
universal no-go are stable was *sharpened* by W3-W1 (5 distinct
target categories), W3-W6 (composition C₁/C₂), and others. This W11
report probes specifically the **Lurie HA §5.5.4** and
**Costello-Gwilliam Vol I §6.4** invocations against their precise
hypotheses, the **PV/CE coherence (R-04)** as a sheaf-theoretic
descent statement, the **filtration / spectral-sequence content**
under the canonical weight $w(d)=q^d$ (W4 Gelfand), and the
**chiral algebra structure** the formal symplectic disk's
factorization centre would need if Beilinson-Drinfeld factorization
were the right home.

The deliverable is **three new severity-3 attacks (W3-W11-01,
W3-W11-02, W3-W11-04), one severity-2 attack (W3-W11-03), one
severity-2 sharpening (W3-W11-05)**, and a **hypothesis-by-hypothesis
verification table** for the two external invocations.

---

## §0. Files read (before mathematical work)

* `/Users/raeez/topological-strings/CLAUDE.md`
* `/Users/raeez/topological-strings/reconstitution/attack-heal-platonic-2026-04-28.md`
  (lines 1–2200 by streamed read; M-25, M-32, M-33, M-37, R-04 anchors)
* `/Users/raeez/topological-strings/reconstitution/wave2-W6-beilinson-2026-04-28.md`
  (eight-link DAG L1–L8; Lurie 5.5.4 / CG 6.4 audit; W6-04, W6-05 heals)
* `/Users/raeez/topological-strings/reconstitution/wave3-W1-kapranov-2026-04-28.md`
  (5-distinct-target-categories finding W3-W1-01; layered Mittag-Leffler
  W3-W1-02)
* `/Users/raeez/topological-strings/appendix-factorization-current-conventions.tex`
  (full; lines 1–171; principal-part current bracket prop)
* `/Users/raeez/topological-strings/tate-T3-quillen-equivalence.tex`
  (full; admissible model envelope §1; transfer §2; Tate Quillen
  equivalence §3; $\infty$-promotion §4; Lurie 5.5 / CG 6.4
  invocations §5–§7; Weiss-cosheaf residual §8)
* `/Users/raeez/topological-strings/main.tex`:1996–2210
  (`thm:open-closed-derived-center-factorization`; HKR appeal in Step 1;
  `rmk:E1-translation`); 2274–2305
  (`prop:ce-source-obstruction`); 2307–2320
  (`rmk:ce-source-obstruction-disk` perfectness); 2322–2438
  (`thm:open-closed-derived-center` cochain proof); 3323–3479
  (`lem:continuous-bar-cobar`, `lem:linear-poisson-schouten`)
* `/Users/raeez/topological-strings/tate-T1-weighted-completion.tex`
  (full; weighted pair; Casimir convergence; regulator-admissible
  sector; strict no-go)

---

## §1. Per-target attack findings

### Target T1 — Lurie HA §5.5.4 invocation

**Manuscript invocation loci (three).**
1. `thm:open-closed-derived-center-factorization` clause (3),
   `main.tex`:2027–2031: "the induced equivalence is locally constant
   in the topological direction $\R$ in the sense of Lurie,
   *Higher Algebra*, §5.5; Costello-Gwilliam Vol. I §6.4 supplies the
   published factorization-algebra terminology."
2. `rmk:E1-translation`, `main.tex`:2193–2210: "factorization
   algebras are equivalent to homotopy associative algebras up to
   translation invariance by Lurie *Higher Algebra* §5.5.4."
3. `thm:open-closed-derived-center-derived` proof, `tate-T3.tex`:466–467:
   "an equivalence in the $\infty$-category of locally constant
   factorization algebras on $\R$ in the sense of Lurie §5.5.4".

Plus structural uses: `tate-T3.tex`:329 (Lurie A.3 Hammock
localization); 339 (Lurie A.3.7.6, A.3.7.10); 345 (Lurie A.2.6.8 for
presentability); 377 ("Lurie *Higher Algebra* §5.5"); 419 ("framework
of Lurie *Higher Algebra* §5.5"); 473 (Lurie HA §5.5.5 higher-algebraic
Koszul); 552 (Lurie HA §5.5.4 inside `prop:weiss-cosheaf-residual`).

**Which Lurie 5.5.4.x theorem?** The manuscript cites "§5.5.4" and
"§5.5" rather loosely. The relevant precise theorem in Lurie's
*Higher Algebra* (September 2017 edition) is **Theorem 5.5.4.10**,
which states:

> *(Lurie HA Th. 5.5.4.10)* For every presentable symmetric monoidal
> $\infty$-category $\mathcal{C}^\otimes$, the functor
> $\Alg_{E_n}(\mathcal{C}) \to \mathrm{Fact}^{\mathrm{lc}}(\R^n;
> \mathcal{C})$ exhibits the right side as a localization of the
> left side; on the locally constant subcategory it is an equivalence.

For $n=1$ this gives $\Alg_{E_1}(\mathcal{C}) \simeq
\mathrm{Fact}^{\mathrm{lc}}(\R; \mathcal{C})$. The neighbouring
theorems used by the manuscript:
- §5.5.5: higher-algebraic Koszul duality (referenced
  `tate-T3.tex`:473);
- §A.2.6.8: presentability of localization;
- §A.3.7.6, A.3.7.10: simplicial-category model of Quillen-equivalent
  $\infty$-categories.

**Hypotheses verbatim of Th. 5.5.4.10.**

| # | Hypothesis | Verbatim content |
|---|---|---|
| H1 | Presentability | $\mathcal{C}^\otimes$ is a presentable symmetric monoidal $\infty$-category |
| H2 | Compatibility of $\otimes$ with colimits | Tensor product preserves small colimits separately in each variable |
| H3 | $E_n$-monoidal structure | $\mathcal{C}^\otimes$ has an $E_n$-monoidal (= $\Alg_{E_n}$-algebra) structure |
| H4 | Locally constant restriction | The factorization algebra is locally constant: structure maps on disk inclusions are equivalences |
| H5 | $n$-dimensional manifold | The manifold is $\R^n$ (or framed $n$-manifold for the framed version) |

**Manuscript's concrete cosheaf $\Omega^\bullet_c(I) \widehat\otimes \mathfrak h$.**
The target $\infty$-category is the admissible Tate envelope of
`stmt:tate-model-envelope`, with weak equivalences = admissible
filtered quasi-isomorphisms. The factorization algebras of interest
are $A_\partial^{\mathrm{Ham}}(I) = \widehat{\mathbf S}(\mathfrak h_I)$
with $\mathfrak h_I = \Omega^\bullet_c(I) \widehat\otimes \bar A$ and
$\mathcal F_{\mathrm{cl}}(I) = C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak g_I)$
with $\mathfrak g_I = \mathfrak h_I \ltimes \mathcal P_I[1]$.

**Hypothesis-by-hypothesis verification.**

| # | Status | Notes |
|---|---|---|
| H1 (presentability) | **PASS at finite window; UNVERIFIED at envelope** | The admissible envelope is locally presentable by `cor:tate-bar-cobar-infinity`'s "presentability is an attribute of the chosen locally presentable envelope, not of the raw Tate category" hedge; however, this hedge is at the *corollary* level, not the *theorem-statement* level. Wave-2 W6-04 already proposes a hypothesis paragraph; **W3-W1-01 finds the analogous gap for C₂(W) and C₂(R) is more severe.** See W3-W11-01 below. |
| H2 ($\otimes$ preserves colimits) | **UNVERIFIED** | Completed Tate tensor product on Mittag-Leffler systems is what is asserted. Whether $\widehat\otimes$ preserves *all* small colimits in each variable separately, in the admissible envelope, is not proved. The standard result for $\Cat{Vec}$ tensor product is colimit-preserving; the Tate version is conditional on the envelope's ML structure. |
| H3 ($E_n$-monoidal) | **PASS for $n=1$** | The admissible envelope is $E_1$-monoidal (associative monoidal), with the cobar-bar Quillen equivalence supplying the Tate associative algebra side. The manuscript invokes only $n=1$. |
| H4 (locally constant) | **PASS at cohomological level** (W6-05 heal) | $\Omega^\bullet_c(I)$ is *not* topologically constant as a chain complex but *is* cohomologically constant (one-dim fibre concentrated in degree 0 by `lem:derivative-jets`). W6-05 heal makes this explicit. |
| H5 ($n$-dim manifold) | **PASS for $\R$** | Brane line is $\R$; bulk $\R^2 \times \C^2$ would need $n=5$, but that is the Weiss residual `prop:weiss-cosheaf-residual` (not invoked). |

**Silent hypothesis strengthening detected: H2 colimit-preservation.**
Lurie 5.5.4.10's hypothesis on $\mathcal{C}^\otimes$ is that
$\otimes$ preserves *all* small colimits separately in each variable.
The manuscript's admissible envelope satisfies this only for
**Mittag-Leffler colimits**: filtered colimits with surjective transition
maps, in the cofibrant-generation argument of `thm:tate-model-structure`
proof (b)/(c). It is **not verified** that the admissible envelope is
closed under arbitrary small colimits. The Wave-2 W1 / wave-1 M-25 R-05
healed this for the Mittag-Leffler core; arbitrary-colimit
preservation in the admissible envelope is the residual.

#### W3-W11-01 — Lurie 5.5.4.10's H2 (colimit-preservation) is verified only for Mittag-Leffler colimits, not for arbitrary small colimits

**Severity 3. Status valid. Confidence high.**
**Lens.** Beilinson primary (descent / colimit-of-categories);
Hypotheses secondary.
**Provenance.** New, this wave. Cross-link to M-27 Mittag-Leffler
dictionary and W3-W1-02 layered dictionary.
**Target.** `cor:tate-bar-cobar-infinity` (T3:321–346); preamble of
`thm:open-closed-derived-center-derived` (T3:398–424); `rmk:E1-translation`
(`main.tex`:2193–2210).
**Claim under attack.** The admissible envelope of
`stmt:tate-model-envelope` satisfies the presentability + colimit-
compatible-tensor hypothesis of Lurie 5.5.4.10.
**Broken step.** The envelope is *defined* with weak equivalences =
admissible filtered qiso (qiso on every finite quotient + on the
associated graded); the small-object argument of
`thm:tate-model-structure` and Hinich's transfer of
`lem:transferred-model` go through *because each Tate window is
finite-dimensional*. This gives:
* sequential filtered colimits with surjective transitions
  (Mittag-Leffler) — preserved by $\widehat\otimes$ via §3 of
  M-27's `lem:tate-mittag-leffler-dictionary`;
* small-object termination in countably many steps (each
  generating cofibration changes one window).

It does **not** automatically give:
* preservation of *arbitrary* small colimits by $\widehat\otimes$
  (the standard requirement on a presentable symmetric monoidal
  $\infty$-category in Lurie 5.5.4.10's hypothesis statement);
* compactness of the generators in the Tate-completion sense
  (Lurie A.2.6.8 requires a *small* set of compact generators).

The specific issue: $\widehat\otimes$ is a *completed* tensor product.
On Mittag-Leffler systems with surjective transitions it is exact
(W3-W1-02 layered dictionary, item 1–2). On general small filtered
colimits it may *not* preserve qiso unless the colimit is itself
Mittag-Leffler. Lurie's framework requires the unrestricted version.

**Evidence type.** hypothesis_gap; missing_source.
**Evidence ref.** `tate-T3.tex`:329–346 (presentability hedge);
`stmt:tate-model-envelope` (T3:46–57, "Mittag-Leffler systems"
restriction); `lem:continuous-bar-cobar` items (1)–(4) (windowwise
finite-dimensionality).
**Confidence.** High.
**Blast radius.** Lurie 5.5.4.10's equivalence
$\Alg_{E_1}(\mathcal{C}) \simeq \mathrm{Fact}^{\mathrm{lc}}(\R;
\mathcal{C})$ holds in $\mathcal{C}$ presentable. If the admissible
envelope is presentable only for ML colimits, then the equivalence
holds in the **ML envelope**, not in the strict envelope. This
constrains:
* the universe of factorization algebras to which the equivalence
  applies — limited to those built from ML cosheaves
  (e.g., $\Omega^\bullet_c$ is fine; arbitrary factorization
  algebras may not be);
* the *sharpness* of the Wave-2 W6-04 hypothesis paragraph —
  W6-04 says "presentability of the admissible Tate envelope" without
  specifying the ML qualifier.
**Minimal heal.**
* **WP3-W11-01-A.** Sharpen W6-04's hypothesis paragraph from
  "presentability of the admissible Tate envelope" to:
  > "presentability of the admissible Tate envelope **in the
  > Mittag-Leffler colimit-restricted sense**: the envelope is
  > closed under filtered colimits with surjective transition maps
  > (cofibrant generation by `lem:transferred-model`,
  > `lem:tate-conilp-model`; Lurie A.2.6.8 applied to ML systems).
  > Lurie 5.5.4.10 is invoked only for factorization algebras built
  > from Mittag-Leffler cosheaves of the admissible envelope; in
  > particular $\Omega^\bullet_c(I) \widehat\otimes \mathfrak h$ is
  > such a cosheaf."

* **WP3-W11-01-B.** Add a one-sentence remark in
  `cor:tate-bar-cobar-infinity` proof noting that arbitrary-small-colimit
  preservation by $\widehat\otimes$ is **not** asserted; the
  factorization algebras of interest (built from $\Omega^\bullet_c$,
  cohomologically locally constant) satisfy ML hypotheses by
  W6-05 (cohomological local constancy) + W3-W1-02 layered ML
  exactness.

**Residual.** Closure of the admissible envelope under arbitrary
small colimits remains open; for the manuscript's purposes (factor
algebras from $\Omega^\bullet_c$), the ML restriction is sufficient.
**Adjudication.** Valid. Sharpens W6-04 by naming the ML qualifier
explicitly; without it, a hostile referee can attack Lurie 5.5.4.10's
hypothesis H2.
**Deciding evidence.** The sharpened hypothesis paragraph.

---

### Target T2 — Costello-Gwilliam Vol I §6.4 invocation

**Manuscript invocation loci (five).**
1. `thm:open-closed-derived-center-factorization` clause (3),
   `main.tex`:2030: "Costello-Gwilliam Vol. I §6.4 supplies the
   published factorization-algebra terminology."
2. `rmk:E1-translation`, `main.tex`:2197–2198: "Costello-Gwilliam
   vocabulary of locally constant factorization algebras Vol. I §6.4."
3. `thm:open-closed-derived-center-derived` proof, `tate-T3.tex`:466–467
   ("Costello-Gwilliam Vol. I §6.4 supplying the published vocabulary").
4. `prop:weiss-cosheaf-residual` proof, `tate-T3.tex`:553 ("with the
   same terminology as Costello-Gwilliam Vol. I §6.4").
5. `prop:weiss-cosheaf-residual` body, `tate-T3.tex`:543–545
   ("Costello-Gwilliam Vol. I §§ 6.1, 6.5, 7.2 provide the
   published factorization, cosheaf, and basis-extension vocabulary;
   no theorem from those sections is used here to close the
   unreduced descent obligation").

**Which CG §6.4 result?** CG Vol I §6.4 is "Locally constant
prefactorization algebras". The relevant precise statements:
- **CG Vol I Definition 6.4.0.1:** locally constant prefactorization
  algebra on a manifold = the structure maps on disk inclusions are
  isomorphisms (or weak equivalences in the dg case).
- **CG Vol I Proposition 6.4.0.4:** locally constant prefactorization
  algebra on $\R$ ≃ associative algebra (in $\Cat{Vec}$, $\Cat{Cat}$, or
  $\Cat{Ch}$).
- **CG Vol I Example 6.4.0.5:** for an associative algebra $A$, the
  prefactorization algebra $\mathcal F_A$ with $\mathcal F_A(I) = A$
  for connected $I$ and structure maps = identity, multiplication, etc.

**Hypotheses of CG 6.4.0.4 verbatim.**

| # | Hypothesis | Verbatim content |
|---|---|---|
| H1 | Cosheaf source | $\mathcal F$ is a prefactorization algebra on $\R$ valued in $\Cat{Ch}$ |
| H2 | Locally constant | structure map $\mathcal F(I) \to \mathcal F(I')$ is a quasi-isomorphism for every disk inclusion $I \subset I'$ |
| H3 | Compactly supported source | (implicit, from §6.5/7.2 toolkit) the prefactorization algebra is built from compactly supported sections (cosheaf-of-modules dualization) |

CG §6.4 does NOT cover (verbatim, by manuscript prose at
`tate-T3.tex`:543–545):
- Vol I §6.1 factorization-algebra full definition (Weiss cover descent);
- Vol I §6.5 "factorization algebras built from cosheaves" toolkit;
- Vol I §7.2 extension-from-a-basis vocabulary.

The manuscript is **explicit** that no theorem from CG §§6.1, 6.5, 7.2
is used to close the unreduced descent obligation
(`tate-T3.tex`:545); only §6.4 *terminology* is used.

**Hypothesis-by-hypothesis verification.**

| # | Status | Notes |
|---|---|---|
| H1 (cosheaf source) | **PASS** | $A_\partial^{\mathrm{Ham}}(I) = \widehat{\mathbf S}(\mathfrak h_I)$ with $\mathfrak h_I = \Omega^\bullet_c(I) \widehat\otimes \bar A$; constructed exactly as a prefactorization algebra in the sense of §6.4. Distinction from §6.1 full FA is acknowledged. |
| H2 (locally constant) | **PASS at cohomological level** (W6-05) | At cochain level $\Omega^\bullet_c(I) \to \Omega^\bullet_c(I')$ for $I \subset I'$ is *not* an isomorphism (compactly supported degree-0 changes); but the cohomology $H^\bullet(\Omega^\bullet_c(I))$ is concentrated in degree 0 with one-dim fibre by `lem:derivative-jets`, so the structure map is a quasi-isomorphism. W6-05 names this. |
| H3 (compactly supported) | **PASS** | $\Omega^\bullet_c$ is the compactly supported de Rham complex; matches CG §6.4. |

**Silent hypothesis: nuclearity / completed-tensor-product topology
(W4 Gelfand flagged).** CG Vol I §A.5 (completed tensor products
in $\Cat{Ch}_{\mathrm{Nuc}}$, the nuclear chain complexes) requires
the cosheaves to be **nuclear** so that the completed tensor product
is well-behaved. This is silent in the manuscript's invocation of
§6.4. Two checks:

(i) **Is $\Omega^\bullet_c(I) \widehat\otimes \bar A$ nuclear?**
$\Omega^\bullet_c(I)$ is a strict colimit of finite-dimensional
nuclear pieces (compactly supported smooth forms on bounded open
sub-intervals); $\bar A = \C[z_1, z_2]/\C \cdot 1$ is a polynomial
algebra (not nuclear in the Schwartz sense, but a strict
filtered union of finite-dimensional pieces $\bar A_{\le w}$
which *are* nuclear). The completed tensor product of two
strict-ML-of-finite-dim systems is well-defined and is itself a
strict-ML system. **Nuclearity in the relevant CG sense holds.**

(ii) **Is the bracket $\{B_f(a), B_g(b)\}$ continuous in the
nuclear topology?** The pointwise product $ab$ on $\Omega^0_c(I)$ is
not continuous on arbitrary distributional pairs (Schwartz / Hörmander
"impossible product theorem"); but the $P_0$-bracket forces zero on
distribution-distribution pairs by the structural abelian-ideal
argument (W6-08 / M-36). On smooth-test-function pairs the bracket
is continuous. **Continuity holds for the $P_0$-bracket structure
maps; fails generically (avoided by structure).**

#### W3-W11-02 — CG §6.4 nuclearity/completed-tensor-product hypothesis is silent in manuscript; silent hypothesis is satisfied but should be named

**Severity 2 (sharpening). Status valid. Confidence high.**
**Lens.** Beilinson (cosheaf-theoretic topology) primary;
Hypotheses secondary.
**Provenance.** New, this wave. Cross-link to W4 Gelfand
nuclearity flag (W3-W4-A residual?), and W6-08 / M-36 distribution-product
avoidance.
**Target.** `thm:open-closed-derived-center-factorization` clause (3)
preamble; `tate-T3.tex`:466–467; `prop:weiss-cosheaf-residual`
preamble.
**Claim under attack.** The manuscript invokes CG Vol I §6.4 for
locally-constant-FA terminology without explicitly verifying the
nuclear / completed-tensor-product hypothesis under which CG's
factorization-algebra construction operates.
**Broken step.** CG Vol I §A.5 (completed tensor products) and §6.4
(locally constant prefactorization algebras) implicitly require:
* the cosheaf is valued in nuclear chain complexes
  ($\Cat{Ch}_{\mathrm{Nuc}}$);
* the completed tensor product $\widehat\otimes$ is well-defined and
  preserves quasi-isomorphisms in each variable (Künneth-clean).

The manuscript verifies neither in the invocation locus, nor names
nuclearity as a hypothesis. The manuscript's specific cosheaf
$\Omega^\bullet_c(I) \widehat\otimes \bar A$ is in fact nuclear in
the strict-ML-of-finite-dim sense, but a hostile referee can object
that this is silent.

**Evidence type.** silent_hypothesis; documentation_gap.
**Evidence ref.** `main.tex`:2030 (the CG §6.4 cite without nuclear
qualifier); `tate-T3.tex`:466–467 (the same); CG Vol I §A.5
(implicit nuclear chain complex framework).
**Confidence.** High.
**Blast radius.** Editorial-plus. The manuscript's specific cosheaf
is nuclear; the hypothesis check passes silently. Naming it
explicitly closes the loophole.
**Minimal heal.**

* **WP3-W11-02-A.** Add a one-sentence remark to W6-05's heal
  preamble:
  > "$\Omega^\bullet_c(I) \widehat\otimes \bar A$ is a strict
  > Mittag-Leffler colimit of finite-dimensional nuclear chain
  > complexes; the completed tensor product $\widehat\otimes$ is
  > well-defined and preserves filtered quasi-isomorphisms in each
  > variable on this nuclear-sub-envelope (CG Vol. I §A.5)."

* **WP3-W11-02-B.** Cross-link W6-08 / M-36 (distribution-product
  avoidance) explicitly to nuclear-sub-envelope: the distribution-
  distribution products *would* break nuclearity, but the
  $P_0$-bracket structurally forces zero on those pairs.

**Residual.** None at this layer.
**Adjudication.** Valid sharpening. The hypothesis is satisfied; it
should be named explicitly.
**Deciding evidence.** The two-sentence addition.

---

### Target T3 — PV/CE coherence (R-04) as sheaf-theoretic descent statement

**The R-04 claim.** Wave-1 R-04 (master ledger 1220) is "Full
one-loop QME calculation in the unreduced BV setup
(`appendix-unreduced-bv-qme.tex`) showing the only quantum anomaly
is the U(1)$_{\mathrm{ghost}}$ Capelli class. Plan §7 N7 / Phase-4
research." The "PV/CE coherence" interpretation: in Theorem A's
locus, the polyvector (PV) side and the Chevalley-Eilenberg (CE)
side are matched. Under the Beilinson lens, this is a sheaf-theoretic
descent statement: PV is sheaves on the cotangent (formal affine
$\mathfrak h^\vee$), CE is sheaves on the Lie algebra ($\mathfrak h$
or $\mathfrak g$).

**Concrete content of the descent.**
* PV side: $\mathrm{PV}(\widehat{\mathbf S}_{\mathrm{Tate}}(\mathfrak h)) =
  \widehat{\mathbf S}_{\mathrm{Tate}}(\mathfrak h) \widehat\otimes
  \widehat\Lambda(\theta^I)$, polyvector fields on the formal affine
  space $\mathfrak h^\vee$ with vector fields $\theta^I = \partial/\partial O_I$.
* CE side: $C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak g) =
  \widehat{\mathbf S}_{\mathrm{Tate}}(\{u_I\}) \widehat\otimes
  \widehat\Lambda(\{c^I\})$, continuous CE cochains on the
  shifted-cotangent extension $\mathfrak g = \mathfrak h \ltimes
  \mathfrak h^\vee_{\mathrm{cont}}[1]$.
* Match: $\Phi(c^I) = \theta^I$, $\Phi(u_I) = O_I$
  (`thm:open-closed-derived-center` cochain-level isomorphism).

**Beilinson-lens rephrasing: descent diagram.**
$$
\begin{array}{ccc}
\text{Sh}(\mathfrak h^\vee, \mathrm{PV}) & \xleftarrow{\text{shifted Legendre}} & \text{Sh}(\mathfrak h, \mathrm{CE}) \\
\downarrow_{[\pi, -]_S} & & \downarrow_{d_{\mathrm{CE}}} \\
\text{Sh}(\mathfrak h^\vee, \mathrm{PV}^{\bullet+1}) & \xleftarrow{\Phi} & \text{Sh}(\mathfrak h, \mathrm{CE}^{\bullet+1})
\end{array}
$$
where the horizontal arrows are $\Phi$, the vertical arrows are the
two differentials (Lichnerowicz on PV, Chevalley-Eilenberg on CE),
and the diagram commutes by `thm:open-closed-derived-center`.

**Is the descent diagram fully drawn?** **No.** The manuscript draws
the cochain-level commuting square but does not draw:
* the Beilinson sheaf-theoretic descent diagram with sheaves over
  $\mathfrak h^\vee$ and $\mathfrak h$ as objects;
* the *spectral sequence of the Tate filtration* on the PV side
  (filtration by symmetric/PV degree on $\widehat{\mathbf S} \otimes
  \widehat\Lambda$);
* the *spectral sequence of the CE-length filtration* on the CE side;
* the *abutment / convergence statement* relating the two spectral
  sequences.

**Are the spectral-sequence convergences verified?** **Partially.**
The proof of `thm:open-closed-derived-center` (`main.tex`:2351–2438)
uses:
* CE differential acts on length-$\le 1$ generators by
  $d_{\mathrm{CE}} c^K = -\tfrac12 C^K_{IJ} c^I c^J$,
  $d_{\mathrm{CE}} u_K = C^L_{KJ} u_L c^J$ — fixed by
  `lem:continuous-bar-cobar` items (2)–(3) at length 1;
* Schouten differential on PV side: $d_\pi \theta^K = -\tfrac12
  C^K_{IJ} \theta^I \theta^J$, $d_\pi O_K = C^L_{KJ} O_L \theta^J$;
* Generator-level matching plus Leibniz/algebra-homomorphism gives
  agreement on every word at fixed total length;
* "Tate-completeness of both sides plus continuity of $d_{\mathrm{CE}}$,
  $d_\pi$, $\Phi$ in the Tate filtration extends the equality to the
  completed algebras" (`main.tex`:2393–2396).

The last step is a *spectral-sequence convergence claim in disguise*:
the cochain identity holds at every finite length; passage to the
completed algebra requires the spectral sequence of the length
filtration to converge. This is exactly the Wave-2 W1-WP1-1 /
Wave-3 W3-W1-04 symmetric-filtration hypothesis gap.

**Missing in the manuscript.** A statement of the form:
> "The cochain identity $\Phi d_{\mathrm{CE}} = d_\pi \Phi$ holds at
> every finite CE-length / PV-degree. The spectral sequence of the
> CE-length filtration on $C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak g)$
> and the parallel spectral sequence of the PV-degree filtration on
> $\mathrm{PV}(\widehat{\mathbf S}_{\mathrm{Tate}}(\mathfrak h))$
> are bounded-below and converge in the admissible Tate envelope.
> The abutment of both spectral sequences is the cochain identity
> on the completed graded algebras."

#### W3-W11-03 — PV/CE coherence is asserted at cochain level only; the sheaf-theoretic descent diagram and its spectral sequence convergence are not drawn

**Severity 2. Status valid. Confidence high.**
**Lens.** Beilinson (sheaf-theoretic descent + spectral sequences)
primary; Hypotheses secondary.
**Provenance.** New, this wave. Cross-link to W3-W1-04
(symmetric-filtration Definitions gap on $\Phi$).
**Target.** `thm:open-closed-derived-center` proof
(`main.tex`:2351–2438), specifically the "Tate-completeness…
extends the equality" line at 2393–2396.
**Claim under attack.** The cochain identity $\Phi d_{\mathrm{CE}} =
d_\pi \Phi$ extends from generators to the full completed algebras
"by Tate-completeness plus continuity."
**Broken step.** This is an unstated spectral-sequence convergence
statement. Specifically:
* The CE-length filtration on $C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak g)$
  is bounded below (length $\ge 0$) but **not bounded above**
  (CE chains include length $= \infty$ via the completion).
* The PV-degree filtration on $\mathrm{PV}(\widehat{\mathbf S}_{\mathrm{Tate}}(\mathfrak h))$
  similarly is bounded below but not bounded above.
* For two unbounded-above filtrations, the spectral sequence
  abutment to the completed algebra is **not automatic**: it
  requires *exhaustivity* (covered by the conilpotency hypothesis
  of `lem:continuous-bar-cobar` item (2)) **and** *Mittag-Leffler
  exactness on the dual filtration* (covered by W3-W1-02 layered
  dictionary's exactness component).

The wave-2 W1's symmetric-filtration hypothesis (R-W1-01,
formalized as W3-W1-04) is a special case of this: it asserts
that the *CE-length filtration agrees with a symmetric filtration*
on each side, so the two abutments coincide. This is provable on
the formal symplectic disk (W1's WP1-2 verification) but has not
been promoted to a general sheaf-theoretic descent statement.

**Evidence type.** spectral_sequence_gap; sheaf_theoretic_descent_gap.
**Evidence ref.** `main.tex`:2393–2396 ("Tate-completeness of both
sides plus continuity"); `lem:continuous-bar-cobar` item (2);
W3-W1-04 (symmetric-filtration Definitions gap).
**Confidence.** High.
**Blast radius.** The cochain identity holds at every finite length;
the abutment to completed algebras is correct on the formal
symplectic disk by W1's verification. The Beilinson-lens issue is
that the *general* descent statement (for any Tate Lie algebra
satisfying the conilpotency hypothesis) is the spectral-sequence
abutment, which is unstated. For the manuscript's specific use
case, this is editorial.
**Minimal heal.**

* **WP3-W11-03-A.** Add a numbered Lemma (or paragraph in the proof
  of `thm:open-closed-derived-center`) stating:
  > "*Spectral sequence of the CE-length filtration.* Under the
  > Tate-conilpotency hypothesis of `lem:continuous-bar-cobar`,
  > the CE-length filtration on
  > $C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak g)$ and the
  > PV-degree filtration on
  > $\mathrm{PV}(\widehat{\mathbf S}_{\mathrm{Tate}}(\mathfrak h))$
  > are exhaustive and Mittag-Leffler. The associated spectral
  > sequences converge to the completed algebras. The cochain
  > identity $\Phi d_{\mathrm{CE}} = d_\pi \Phi$ holds at every
  > $E_1$-page (= generator-level identity) and propagates to the
  > $E_\infty$-page (= completed-algebra identity) by abutment."

* **WP3-W11-03-B.** Draw the Beilinson sheaf-theoretic descent
  diagram once in the manuscript, e.g., in `principles.tex` or a
  preamble to `thm:open-closed-derived-center`, with sheaves on
  $\mathfrak h^\vee$ (PV side) and $\mathfrak h$ (CE side), with
  $\Phi$ as a horizontal arrow and the two differentials as vertical
  arrows.

**Residual.** None at this layer; the descent diagram is editorial.
**Adjudication.** Valid sharpening. The cochain-level proof is
correct; the sheaf-theoretic descent is implicit but unstated.
**Deciding evidence.** The sheaf-theoretic descent diagram + the
spectral-sequence abutment lemma.

---

### Target T4 — Filtrations and weights ($w(d) = q^d$) as filtration on chiral algebra

**The W4 Gelfand finding.** Wave-3 W4 found that the Tate lanes
T1–T5 have a canonical weight $w(d) = q^d$ with $q > 1$ (T1's
exponential weight; W4-A4 / W4-A5 examples). The weight is on the
Hamiltonian degree $d$ (= polynomial degree in $z_1, z_2$ on
$\mathfrak h_d = \{H_{a,b} : a+b = d\}$).

**Beilinson-lens rephrasing: filtration on the chiral algebra.**
The chiral algebra structure on the formal symplectic disk's
factorization centre would carry, under the canonical weight, a
**weight filtration** $F^w \mathfrak h = \prod_{d \ge w} H_d$. Three
questions to address.

**(a) Does the filtration converge?** Yes, by construction:
$\mathfrak h = \prod_{d \ge 1} H_d = \varprojlim_w (\prod_{d \le w} H_d)$
is the *Tate inverse limit* of finite-dimensional pieces. The
filtration is exhaustive (every element of $\mathfrak h$ has a finite
projection at each window) and Hausdorff ($\bigcap_w F^w \mathfrak h
= 0$ by `lem:continuous-bar-cobar` (1)).

**(b) Is the associated graded computable?** Yes, in the weighted
envelope:
$$\mathrm{gr}^w \mathfrak h = \bigoplus_d (H_d)^{(w)} = \bigoplus_d w(d) \cdot H_d \cong \bigoplus_d H_d \quad (\text{as a graded vector space, weight-twisted})$$

This is `tate-T1`:184–221's weighted Tate coefficient pair
$(\mathfrak h_w, \mathfrak h^{\vee, w}_{\mathrm{cont}})$.

**(c) Does the spectral sequence of the filtration degenerate?**
**This is the key Beilinson-lens question, and the answer is
conditional.** Two cases:
* **Strict ($q = 1$, unweighted) case:** The strict-no-cy theorem
  `\thm:strict-unweighted-no-go` (M-11 closure) forbids the strict
  $q \to 1^+$ limit: the Casimir does not converge in the strict
  product/direct-sum pair. So the spectral sequence of the unweighted
  filtration **does not degenerate** in any meaningful sense — the
  $E_2$-page already detects the Casimir-non-convergence pathology.
* **Weighted ($q > 1$) case:** The weighted Casimir converges
  (`prop:wt-casimir-convergence`); the heat-kernel propagator
  extends (`prop:wt-propagator-extends`); each fixed Costello graph
  preserves the weighted category (`thm:wt-rg-compatibility`); the
  cochain-level $\Phi$ extends to the weighted cotangent
  (`thm:wt-cotangent-lift`). For *graphwise* contributions, the
  spectral sequence degenerates at $E_1$ (each graph is a finite-
  vertex computation). For the *full effective interaction*, the
  spectral sequence is **conditional on Costello-locality / QME
  compatibility** (Problem `prob:weighted-rg-locality`).

#### W3-W11-04 — Weight filtration spectral sequence is degenerate at $E_1$ on graphwise contributions but conditional on QME compatibility for the full effective interaction

**Severity 3 (sharpening). Status valid. Confidence high.**
**Lens.** Beilinson (filtrations / spectral sequences) primary;
Hypotheses secondary.
**Provenance.** New, this wave. Sharpens M-11 (admissible-only
regulator-independence), M-37 / W6-07 (R-03 four-ingredient closure
plan), W3-W1-01-A (C₂(W) target-category gap).
**Target.** `tate-T1`:170–815 (weighted construction, weighted
RG flow, regulator-independence, conditional QME, strict no-go);
master ledger M-11 (line 565–605, "admissible-only" reformulation
of Obligation III).
**Claim under attack.** The weighted construction "stabilises" or
"converges" as a function of the weight $q$.
**Broken step.** The wave-2 M-11 reformulation correctly says
"admissible-only regulator-independence; no $q \to 1^+$ limit."
But the *spectral-sequence content* of the weighted filtration is
not stated. Specifically:
* At each fixed $q > 1$, the spectral sequence of the weight
  filtration on the weighted CE / PV cochains degenerates at $E_1$
  on every fixed Costello graph contribution (by
  `prop:wt-rg-tame`'s finite-vertex bound).
* The *full* spectral sequence (over all graph orders) does not
  degenerate at $E_1$; convergence to the QME-compatible quantum
  observable is conditional on
  `prob:weighted-rg-locality`'s vanishing obstruction class.
* M-11's "admissible-only regulator-independence" is the
  graphwise-degeneration statement, not the all-order degeneration.

The Wave-2 W6-07 (R-03 four-ingredient closure plan) also encounters
this: the heat-kernel propagator (ingredient 1) is constructed
graphwise; the transverse Mittag-Leffler resolution (ingredient 4)
is the genuinely beyond-reach piece; the all-order spectral
sequence convergence is the residual.

**Evidence type.** spectral_sequence_partial_degeneration;
hypothesis_strengthening_silent.
**Evidence ref.** `tate-T1.tex`:375–429 (`prop:wt-rg-tame`,
`thm:wt-rg-compatibility`); `tate-T1.tex`:493–512
(`prop:wt-conditional-qme-lift`); `tate-T1.tex`:531–556
(`prob:weighted-rg-locality`); M-11 reformulation.
**Confidence.** High.
**Blast radius.** Editorial-plus. The weighted construction's
graphwise / conditional-all-order distinction is correctly named in
T1 and M-11; the *spectral-sequence-of-the-filtration* phrasing
makes it more transparent.
**Minimal heal.**

* **WP3-W11-04-A.** Add a numbered remark in `tate-T1` (or master
  ledger update to M-11) stating:
  > "*Spectral sequence of the weight filtration.* At each fixed
  > admissible weight $q > 1$, the spectral sequence of the
  > weight filtration on the weighted CE / PV cochains
  > degenerates at $E_1$ on every fixed Costello graph
  > contribution (by `prop:wt-rg-tame`). The all-order convergence
  > to the full effective interaction's QME-compatible cohomology
  > is conditional on `prob:weighted-rg-locality`'s vanishing
  > obstruction class. Regulator-independence among admissible
  > weights $q, q' > 1$ holds at the graphwise / finite-window level
  > (`thm:wt-regulator-independence-admissible`); the strict
  > $q \to 1^+$ limit is forbidden by
  > `\thm:strict-unweighted-no-go`."

* **WP3-W11-04-B.** Cross-link to W6-07 (R-03 four-ingredient
  closure plan): the spectral-sequence convergence in the spacetime
  direction (heat-kernel propagator + transverse ML resolution) is
  the fourth ingredient.

**Residual.** Same as M-11 / W6-07: the all-order QME compatibility
in the weighted envelope is Phase-4 / open.
**Adjudication.** Valid sharpening. The graphwise-vs-all-order
distinction is implicit in the weighted construction; making it
explicit as a spectral-sequence statement clarifies the residual.
**Deciding evidence.** The numbered remark + cross-link.

---

### Target T5 — Chiral algebra structure on the formal symplectic disk's factorization centre

**The Beilinson-Drinfeld chiral algebra question.** The formal
symplectic disk's factorization centre, as constructed in
`thm:open-closed-derived-center-factorization`, is a **locally
constant factorization algebra** on $\R$ (the brane line). In
Beilinson-Drinfeld's framework (BD, *Chiral Algebras*, 2004,
§3.3–3.4), a chiral algebra on a complex curve $X$ is a
$\mathcal D$-module on $X$ with a bracket
$\mu: j_*j^*(\mathcal A \boxtimes \mathcal A) \to \Delta_!\mathcal A$
where $\Delta: X \hookrightarrow X \times X$ is the diagonal and $j$
is the open complement. For $X = \R$ (or $\R \times \{0\}$
embedded in $\C$ as the brane line), the chiral algebra structure
specializes.

**Manuscript's factorization algebra.** The brane factorization
algebra on $\R$ is $A_\partial^{\mathrm{Ham}}(I) =
\widehat{\mathbf S}(\mathfrak h_I)$ with $\mathfrak h_I =
\Omega^\bullet_c(I) \widehat\otimes \bar A$. Its factorization
centre is $\mathcal F_{\mathrm{cl}}(I) =
C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak g_I)$ with
$\mathfrak g_I = \mathfrak h_I \ltimes \mathcal P_I[1]$. Wave-2
W6's eight-link DAG L1–L8 closes the locally-constant FA equivalence.

**Chiral algebra structure?**

**(a) λ-bracket.** A chiral / vertex algebra structure on the
factorization centre would carry an OPE / λ-bracket
$Y_\lambda(a, z) b = \sum_n \frac{\lambda^n}{n!} a_{(n)} b$
(Borcherds' λ-bracket convention). The manuscript's bracket on
the principal-part current
$$\{B_f(a), \Theta_\rho(B)\} = \Theta_{f \cdot \rho}(aB)$$
(`appendix-factorization-current-conventions.tex`:120) is exactly
the OPE-style operation: the smeared Hamiltonian acts on the
smeared principal-part by *coadjoint shift* in the label $\rho$
multiplied by *pointwise product* in the test function. This is
the **chiral λ-bracket on the formal symplectic disk's
factorization centre**, in the Beilinson-Drinfeld sense.

**(b) Central charge.** The U(1)/Capelli class $[\bar c]$
(M-09 weight-$(0,0)$ cohomology line) is the central extension of
the Hamiltonian Lie algebra $\bar A = \C[z_1, z_2]/\C \cdot 1$ by
$\bar\omega(z_1^k z_2^l, z_1^m z_2^n) = (kn - lm) \mathbf 1_{(k+m, l+n) = (1,1)}$.
This is a **chiral central charge** in the Beilinson-Drinfeld
sense: it is the cocycle measuring the failure of strict
commutativity of the chiral OPE under the U(1) trace anomaly.
In the standard chiral-vertex-algebra dictionary, central charge
$c$ is the leading coefficient of the OPE $T(z) T(w) \sim c/(z-w)^4 + ...$;
here, the analogous role is played by $[\bar c]$ at weight $(0,0)$.

**(c) Universal property.** Beilinson-Drinfeld chiral algebras
are characterized by a universal property: chiral algebra structures
on $X$ correspond to factorization algebras with locally constant
structure on $X$ in the Ran-space sense. The manuscript's
`thm:open-closed-derived-center-derived` realizes the equivalence
in Lurie's framework (5.5.4.10 for $n=1$); the BD framework would
require Ran-space descent (analogous to Weiss-cosheaf descent on
$\R^2 \times \C^2$, M-14 / R-03 / M-37).

**Sketch of the chiral algebra structure.** On the formal
symplectic disk's factorization centre, with the canonical
weight $w(d) = q^d$:

* **Underlying vector space.** $\mathcal A = C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak g_I)$
  for $I$ a small open interval, with the strict cochain identity
  to $\mathrm{PV}(\widehat{\mathbf S}_{\mathrm{Tate}}(\mathfrak h))$
  via $\Phi$.
* **λ-bracket / OPE.** The $P_0$-bracket of
  `prop:app-factorization-principal-part-bracket`:
  $\{B_f(a), B_g(b)\} = B_{\{f,g\}}(ab)$,
  $\{B_f(a), \Theta_\rho(B)\} = \Theta_{f \cdot \rho}(aB)$,
  $\{\Theta_\rho(B), \Theta_\sigma(C)\} = 0$.
  Promoted to a λ-bracket via the chain map
  $\Phi^{\mathrm{Ham}}_{\mathrm{fact}}$; the bracket is "chiral"
  because it is the cosheaf-theoretic factorization product of
  observables on disjoint intervals.
* **Central charge.** $[\bar c] \in H^2_{\mathrm{Lie}}(\bar A; \C)_{(0,0)}$
  with $\bar c(z_1, z_2) = 1$ (the constant cocycle on the
  weight-(1,1) sector). Theorem G's quantum side identifies this
  with the U(1)$_{\mathrm{ghost}}$ Capelli class
  $YX - XY + \hbar N I = 0$ at finite $N$ (M-12 trace-pair vs
  index-pair clarification).

**Universal-property check.** Three checks.

(i) **Translation invariance.** Locally constant FA on $\R$ is
translation-invariant in the cohomology direction (W6 / DAG L6;
$[d_\R, \iota_{\partial_t}] = \partial_t$). **Pass.**

(ii) **Conformal invariance.** A chiral / vertex algebra has a
conformal structure (Virasoro action). The manuscript's
factorization centre is *topological* on $\R$ (locally constant),
not conformal. The Symp$_{\mathrm{form}}$-equivariance (M-35)
provides a partial naturality, but this is *transverse to* the
brane line direction, not along it. **Conditional pass:** the
Beilinson-Drinfeld chiral algebra is the *topological* analog
(no conformal weight on the brane line), with the
transverse (formal disk) symplectic structure providing the
"chiral coefficient module."

(iii) **Coassociativity / chiral Jacobi.** The
$P_0$-bracket satisfies the graded Jacobi identity (Schouten
biderivation). On the chiral algebra side, this becomes the
chiral Jacobi identity: $\{a, \{b, c\}\} = \{\{a, b\}, c\} \pm
\{b, \{a, c\}\}$, which is the standard $P_0$ axiom. **Pass.**

#### W3-W11-05 — Chiral algebra structure on factorization centre is implicit; explicit Beilinson-Drinfeld interpretation closes M-37 transverse-ML residual interpretively

**Severity 2 (sharpening). Status valid. Confidence medium-high.**
**Lens.** Beilinson (chiral algebra interpretation) primary;
Hypotheses secondary.
**Provenance.** New, this wave. Cross-link to M-37 / W6-07
(R-03 four-ingredient closure plan, "transverse Mittag-Leffler
on defect-localised distributions, closer to Beilinson-Drinfeld
chiral algebra than Costello-RG").
**Target.** `appendix-factorization-current-conventions.tex`
(the $P_0$-bracket structure); `theorem-lanes.tex` Lane 6
(primitive cotangent shadow); master ledger M-37 (R-03 four-ingredient
plan).
**Claim under attack.** The factorization centre on the formal
symplectic disk is *implicitly* a Beilinson-Drinfeld chiral algebra,
with λ-bracket = $P_0$-bracket, central charge = U(1)/Capelli class,
and universal property = locally-constant-FA equivalence. The
manuscript does not name this interpretation explicitly.
**Sharpening.** The Beilinson-Drinfeld interpretation:
* unifies the M-09 weight-$(0,0)$ cohomology line, M-12
  trace-pair-vs-index-pair Capelli, and M-32 U(1)$_{\mathrm{ghost}}$
  regularization-compatible findings into a single structural
  statement: "the formal symplectic disk's factorization centre is
  a topological chiral algebra in the Beilinson-Drinfeld sense,
  with central charge given by the U(1)/Capelli class";
* clarifies the M-37 / W6-07 transverse ML residual: the genuinely
  hard ingredient ("Mittag-Leffler resolution transverse to the
  brane on defect-localised distributions") is exactly the *Ran-space
  descent* of the BD chiral algebra, which is non-standard for
  Costello-RG and standard for BD.
**Evidence type.** structural_interpretation; cross-link.
**Evidence ref.** `appendix-factorization-current-conventions.tex`:107–148
(λ-bracket structure); BD *Chiral Algebras* §3.3–3.4 (chiral algebra
definition); M-09, M-12, M-32, M-37.
**Confidence.** Medium-high. The interpretation is structurally
sound; verification at the level of explicit Ran-space descent is
beyond present-paper scope.
**Blast radius.** Interpretive / editorial. The Beilinson-Drinfeld
interpretation does not break any existing theorem; it provides a
unifying frame for several existing master-ledger entries.
**Minimal heal.**

* **WP3-W11-05-A.** Add a one-paragraph remark in
  `principles.tex` or `theorem-lanes.tex` Lane 6 stating:
  > "*Chiral algebra interpretation.* The formal symplectic disk's
  > factorization centre, as constructed in
  > `thm:open-closed-derived-center-factorization`, is a topological
  > chiral algebra in the Beilinson-Drinfeld sense
  > (BD *Chiral Algebras* 2004, §3.3–3.4): the locally-constant FA
  > on $\R$ has a λ-bracket given by the $P_0$-bracket of
  > `prop:app-factorization-principal-part-bracket`, and a central
  > charge given by the U(1)/Capelli weight-(0,0) cohomology class
  > $[\bar c]$. The Ran-space descent (Beilinson-Drinfeld §3.4) is
  > exactly the transverse Mittag-Leffler residual M-37 / R-03,
  > genuinely beyond Costello-RG."

* **WP3-W11-05-B.** Cross-link the Beilinson-Drinfeld
  interpretation in master ledger §B (cross-walk) to M-09, M-12,
  M-32, M-37 as a unifying structural frame.

**Residual.** Full Ran-space descent verification (analogous to
the Weiss-cosheaf descent of M-14) remains Phase-4. The
interpretive sharpening does not close it; it names the residual
more precisely.
**Adjudication.** Valid. The interpretation is structurally
correct; explicit naming is a sharpening of M-37 / R-03 + a
unification of M-09, M-12, M-32.
**Deciding evidence.** The one-paragraph remark + cross-link to
M-09, M-12, M-32, M-37.

---

## §2. Hypothesis-by-hypothesis verification table (consolidated)

| # | External cite | Locus | Hypothesis | Verbatim status | Verification | Heal |
|---|---|---|---|---|---|---|
| L-H1 | Lurie HA 5.5.4.10 | `main.tex`:2027–2031 | Presentability | implicit | PASS at finite window; UNVERIFIED at envelope (ML colimit only) | W6-04 + WP3-W11-01-A |
| L-H2 | Lurie HA 5.5.4.10 | `main.tex`:2027–2031 | $\otimes$ preserves colimits | implicit, **silently strengthened** | PASS for ML colimits; UNVERIFIED for arbitrary | WP3-W11-01-A |
| L-H3 | Lurie HA 5.5.4.10 | `main.tex`:2027–2031 | $E_n$-monoidal | implicit | PASS for $n=1$ | (already explicit) |
| L-H4 | Lurie HA 5.5.4.10 | `main.tex`:2027–2031 | locally constant | implicit | PASS at cohomological level | W6-05 |
| L-H5 | Lurie HA 5.5.4.10 | `main.tex`:2027–2031 | $n$-dim manifold | implicit | PASS for $\R$ ($n=1$) | (already explicit) |
| C-H1 | CG Vol I 6.4.0.4 | `main.tex`:2030 | cosheaf source | implicit | PASS | (already explicit) |
| C-H2 | CG Vol I 6.4.0.4 | `main.tex`:2030 | locally constant | implicit | PASS at cohomological level | W6-05 |
| C-H3 | CG Vol I §A.5 | (not stated) | nuclearity / completed-tensor | **silent** | PASS by structure | WP3-W11-02-A |
| C-H4 | CG Vol I §6.4 | (not stated) | continuity of bracket | **silent** | PASS for $P_0$ pairs (avoidance) | WP3-W11-02-B + W6-08 |
| L-A1 | Lurie HA A.2.6.8 | `tate-T3.tex`:345 | locally presentable + small generators | implicit | PASS for ML systems; UNVERIFIED for arbitrary | WP3-W11-01-A |
| L-A2 | Lurie HA A.3.7.6, .10 | `tate-T3.tex`:339 | Quillen equivalence ⇒ $\infty$-cat equivalence | explicit | PASS | (none needed) |

**Aggregate.** Of 11 hypothesis checks across the two cited
sections:
* **Pass (explicit or addressable):** 7 (L-H1 finite window, L-H3,
  L-H4, L-H5, C-H1, C-H2, L-A2);
* **Pass with silent hypothesis (heal proposed):** 3 (L-H2 with
  ML qualifier, C-H3 nuclearity, C-H4 bracket continuity);
* **Pass with strengthening required at envelope level:** 1 (L-A1
  arbitrary-colimit closure);
* **Fail:** 0.

No hypothesis fails outright. Three hypotheses are silently
strengthened (L-H2 colimit-preservation, C-H3 nuclearity, C-H4
bracket continuity); WP3-W11-01-A and WP3-W11-02-A heal these
with one-sentence additions.

---

## §3. New residuals (W11-originated)

* **R-W3-W11-01** (from W3-W11-01 / WP3-W11-01-A,B). Lurie 5.5.4.10's
  presentability + colimit-preservation hypothesis is satisfied in
  the admissible Tate envelope **only for Mittag-Leffler colimits**.
  The arbitrary-small-colimit closure of the envelope is open;
  for the manuscript's specific use case (factorization algebras
  built from $\Omega^\bullet_c$, cohomologically locally constant),
  the ML restriction is sufficient.

* **R-W3-W11-02** (from W3-W11-02 / WP3-W11-02-A,B). Nuclearity of
  the manuscript's specific cosheaf $\Omega^\bullet_c(I) \widehat\otimes
  \bar A$ is satisfied by structure (strict ML colimit of
  finite-dimensional nuclear pieces); the nuclearity hypothesis on
  CG §6.4 is silent and should be named explicitly.

* **R-W3-W11-03** (from W3-W11-03 / WP3-W11-03-A,B). The
  sheaf-theoretic descent diagram for PV/CE coherence is implicit;
  the spectral-sequence convergence statement is not drawn. For
  the manuscript's specific use case (formal symplectic disk),
  W1's WP1-1 symmetric-filtration hypothesis closes the abutment;
  the general case is the spectral-sequence convergence statement.

* **R-W3-W11-04** (from W3-W11-04 / WP3-W11-04-A,B). The weight
  filtration spectral sequence degenerates at $E_1$ on graphwise
  contributions; all-order convergence is conditional on
  `prob:weighted-rg-locality`'s vanishing obstruction class.

* **R-W3-W11-05** (from W3-W11-05 / WP3-W11-05-A,B). The
  Beilinson-Drinfeld chiral algebra interpretation of the
  factorization centre is implicit; explicit naming unifies M-09,
  M-12, M-32, M-37 and clarifies the M-37 transverse-ML residual
  as Ran-space descent.

---

## §4. Wave-3 W11 minimal-heal proposals

### Tier 1 — Phrasing edits to wave-2 master ledger / W6 heals

**WP3-W11-T1-1** (W3-W11-01 / R-W3-W11-01). Sharpen W6-04's
hypothesis paragraph in
`thm:open-closed-derived-center-derived` preamble from "presentability
of the admissible Tate envelope" to "presentability of the admissible
Tate envelope **in the Mittag-Leffler colimit-restricted sense**:
the envelope is closed under filtered colimits with surjective
transition maps."

**WP3-W11-T1-2** (W3-W11-02 / R-W3-W11-02). Add one sentence to
W6-05's heal preamble naming nuclearity of $\Omega^\bullet_c(I)
\widehat\otimes \bar A$ as a strict-ML-of-finite-dimensional-pieces
property.

### Tier 2 — Numbered remark / lemma additions

**WP3-W11-T2-1** (W3-W11-03 / R-W3-W11-03). Add a numbered Lemma
or paragraph in the proof of `thm:open-closed-derived-center` (or
in `principles.tex`) stating the spectral-sequence convergence of
the CE-length and PV-degree filtrations under conilpotency,
with abutment to the cochain identity on completed algebras.
Optionally draw the Beilinson sheaf-theoretic descent diagram once.

**WP3-W11-T2-2** (W3-W11-04 / R-W3-W11-04). Add a numbered remark
in `tate-T1` (or master ledger update to M-11) on the weight
filtration spectral sequence: degenerate at $E_1$ on graphwise
contributions; all-order conditional on `prob:weighted-rg-locality`.

**WP3-W11-T2-3** (W3-W11-05 / R-W3-W11-05). Add a one-paragraph
remark in `principles.tex` or `theorem-lanes.tex` Lane 6 naming
the Beilinson-Drinfeld chiral algebra interpretation of the
factorization centre, with cross-link to M-09, M-12, M-32, M-37.

### Tier 3 — Hypothesis verification table

**WP3-W11-T3-1** (consolidated). The verification table in §2 of this
report can be inscribed as a numbered Table in the manuscript's
appendix — either in `appendix-factorization-current-conventions.tex`
or as a new appendix section "Hypothesis audit of external citations"
— so the hypothesis-by-hypothesis status is visible at the publication
level.

---

## §5. Wave-3 W11 verdict

The wave-2 stable-core declaration **survives the Beilinson +
Hypotheses probe**, with three new severity-3 attacks (W3-W11-01,
W3-W11-04 sharpening of M-11, W3-W11-03 sheaf-theoretic descent),
two severity-2 attacks/sharpenings (W3-W11-02 nuclearity,
W3-W11-05 chiral algebra interpretation), and a hypothesis-by-hypothesis
verification table that documents one silent strengthening
(arbitrary-colimit-vs-ML-colimit on Lurie 5.5.4.10's H2) and
two silent hypotheses (CG §6.4 nuclearity, bracket continuity).

**No external citation hypothesis fails outright.** Of the eleven
hypothesis checks, seven pass explicitly, three pass with silent
qualifiers that admit one-sentence heals (WP3-W11-01-A,
WP3-W11-02-A,B), and one passes only at the ML-restricted level
of the admissible Tate envelope (WP3-W11-01-A).

**The PV/CE coherence (R-04 sheaf-theoretic descent rephrasing)
is correct at the cochain level on the formal symplectic disk** by
W1's WP1-2 symmetric-filtration verification; the general
sheaf-theoretic descent statement (for any Tate Lie algebra
satisfying conilpotency) is the spectral-sequence abutment, which
W3-W11-03 names as missing.

**The weight filtration $w(d) = q^d$ (W4 Gelfand) is the canonical
chiral-algebra-style filtration on the formal symplectic disk's
factorization centre.** Its spectral sequence degenerates at $E_1$
on graphwise contributions; all-order convergence is conditional on
`prob:weighted-rg-locality`'s vanishing obstruction class. M-11's
"admissible-only regulator-independence" is the graphwise-degeneration
statement; the all-order analog is residual.

**The chiral algebra interpretation (Beilinson-Drinfeld,
WP3-W11-05)** unifies M-09 (weight-(0,0) cohomology), M-12
(trace-pair vs index-pair Capelli), M-32 (U(1)$_{\mathrm{ghost}}$
regularization-compatible), and M-37 (R-03 four-ingredient closure
plan, "transverse ML closer to Beilinson-Drinfeld") into a single
structural frame. The Ran-space descent (BD §3.4) is the
M-37-transverse-ML residual.

**The wave-2 stable-core verdict is confirmed and sharpened, not
broken.** The five-way C-split (M-26 / W3-W1-01) carries through;
the eight-link DAG (M-33 / W6) carries through; the universal
no-go (M-29) carries through. The Beilinson-lens probe of the
Lurie 5.5.4.10 / CG §6.4 invocations finds three silent hypotheses
that should be named explicitly, but no fatal gap.

---

## §6. Summary (200 words)

This W11 Beilinson + Hypotheses probe of the wave-2 master ledger's
stable-core verdict produced three new severity-3 attacks, two
severity-2 sharpenings, and a hypothesis-by-hypothesis verification
table for the Lurie HA §5.5.4.10 and Costello-Gwilliam Vol I §6.4
invocations. **W3-W11-01** locates that Lurie 5.5.4.10's
colimit-preservation hypothesis on the admissible Tate envelope
is verified only for Mittag-Leffler colimits, not arbitrary small
colimits; for the manuscript's specific factorization algebras
(built from $\Omega^\bullet_c$) the ML restriction suffices.
**W3-W11-02** flags the nuclearity hypothesis on CG §6.4 as silent;
the manuscript's cosheaf is nuclear by structure (strict ML of
finite-dim pieces), but should be named. **W3-W11-03** names the
sheaf-theoretic descent diagram for PV/CE coherence as implicit
(spectral-sequence convergence on completed algebras, conditional
on conilpotency). **W3-W11-04** sharpens M-11: the weight filtration
spectral sequence degenerates at $E_1$ graphwise but conditionally
all-order. **W3-W11-05** names the Beilinson-Drinfeld chiral algebra
interpretation, unifying M-09 / M-12 / M-32 / M-37 as a topological
chiral algebra with central charge = U(1)/Capelli class. Of eleven
hypothesis checks across the two external cites, none fails;
three are silently strengthened and admit one-sentence heals.
The wave-2 stable core is confirmed and sharpened, not broken.

---

End of W3-W11 report.
