# Wave 3 / W6 — Costello + Composition Lens

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Costello (factorization algebras, BV/BRST, renormalization,
perturbative QFT) + Composition (associativity, coherence,
transactionality of local-to-global passages).
**Mode.** Proposal-only. Master ledger schema; IDs prefix `W3-W6-`.
**Posture.** Wave-2 W1 (Costello+Hypotheses) declared the C-block
healed by a 5-way split (M-26: C₁ᶠʷ, C₁ᶜᵒᵐᵖ, C₂(NT), C₂(W), C₂(R))
together with `lem:tate-mittag-leffler-dictionary` (M-27). Wave-2 W6
(Beilinson+Composition) declared an 8-link DAG (M-33: L1–L8) for
`thm:open-closed-derived-center-factorization`. Wave-3 W6
stress-tests these declarations against five primary targets (T1–T5
of the prompt) under the Costello-physics + Composition lens.
**Inputs.** `attack-heal-platonic-2026-04-28.md` (M-26, M-27, M-33);
`wave2-W1-costello-2026-04-28.md`; `wave2-W6-beilinson-2026-04-28.md`;
`tate-T1-weighted-completion.tex` (full); `tate-T2-nilpotent-truncation.tex`
(full); `tate-T3-quillen-equivalence.tex` (full);
`tate-T4-bv-vanishing.tex` (full); `tate-T5-chain-level-primitive.tex`
1–688; `tate-P1-hadamard-mittag-leffler.tex` (full);
`tate-P3-universality.tex` (full); `appendix-unreduced-bv-qme.tex`
(full); `main.tex` 2196–2475, 2322–2475 (`thm:open-closed-derived-center`).
**Independence.** Wave-2 W1's 5-way split and Wave-2 W6's 8-link DAG
are taken as inputs **under attack**. The deliverable is a
composition audit, with each obstruction either supplied as an
explicit higher-coherence requirement or named as an open-coherence
residual.

---

## §0. Executive verdict (precedes the ledger)

The 5-way C₁/C₂ split (M-26) **survives the Costello + Composition
lens, with three new coherence obligations identified**:

1. **C₁ᶠʷ → C₁ᶜᵒᵐᵖ is not a free composition.** The completed-algebra
   promotion of the finite-word identity requires a *bidirectional*
   continuity hypothesis (continuity of $\Phi$ AND of $\Phi^{-1}$ in
   one and the same Tate filtration). Wave-2 W1 named the
   continuity-of-$\Phi^{-1}$ requirement (W1-02 / R-W1-01) but did
   not name the *symmetric* / *both-directional* version. The
   composition $C_1^{\rm fw} \circ \text{(promotion)} = C_1^{\rm comp}$
   is **not associative** in the regulator parameter without a
   symmetric-filtration declaration.

2. **C₂(NT) ∘ C₂(W) ∘ C₂(R) is not a chain of derived natural
   transformations.** They live on **inequivalent source Lie
   algebras** (NT on $\mathfrak m^3$, W on $\mathfrak h^w$ with
   product dual, R on regulator-equivalence classes). The composition
   that wave-2 W1 envisaged (R lifts NT and W simultaneously) is
   really a **span of independent objects sharing only the
   finite-window stable diagram**. The "associativity" wave-3 needed
   to check is whether the regulator-equivalence class of C₂(R)
   *contains* the NT-truncation as a representative; it does on
   $\mathfrak m^3 \cap F^{\le w}$ for every fixed window, but does
   not on the full Lie algebra.

3. **The 5-way split is regulator-class-canonical, not
   regulator-canonical.** A change of regulator scheme inside the
   admissible class (Definition `defn:regulator-admissible-sector`)
   preserves C₂(R), C₂(W), C₂(NT) up to the diagonal isomorphism
   $R_{w,w'}$. A change of regulator class (e.g.\ from exponential
   weights to a non-Mittag-Leffler completion, or a different
   Hörmander wave-front-set restriction) is **outside the proved
   coherence**. The Costello-canonicity of the renormalization scheme
   is unverified at the level of the M-26 split.

The M-27 lemma (`lem:tate-mittag-leffler-dictionary`) **survives**
under the Composition lens, with the additional verification that
each Tate lane T1–T5 individually exhibits the surjective-transition
hypothesis on a **different** inverse system — the lemma's hypothesis
package is verified by the conjunction of T1, T2, T3, T5 (with T4 as
no-go), and **not** by any one lane alone. Wave-2 W1 implicitly
assumed the conjunction; this report makes the conjunctive structure
explicit.

The QME coherence on C₂(W): C₂(W)'s differential **does** satisfy a
classical $P_0$-bracket compatibility (via the Schouten/Lichnerowicz
structure of `thm:wt-cotangent-lift`); it does **not** satisfy the
quantum master equation (QME) exactly. The QME compatibility is
**conditional on `prob:weighted-rg-locality`** (the brane-defect
obstruction class). Wave-2 W1's classification of C₂(W) as "stable"
is correct **at the classical chain level only**; the quantum
extension is conditional and does not propagate.

**Stable core verdict (Wave-3-W6-amended).** Theorems A, B, C₁ᶠʷ,
C₁ᶜᵒᵐᵖ (formal disk, with explicit symmetric filtration), C₂(NT),
C₂(W) (classical only), C₂(R), D, E, F, G remain stable. The
quantum extension of C₂(W) is **conditional** on
`prob:weighted-rg-locality` and should be flagged as such anywhere
that classical and quantum statements meet. The 5-way split is
**not** disturbed by the new coherence obligations; the obligations
sharpen the hypothesis layer beneath the split, not the split itself.

---

## §1. New ledger entries

### W3-W6-01 — C₁ᶠʷ → C₁ᶜᵒᵐᵖ promotion is *not* free; requires symmetric filtration on **both** $\Phi$ and $\Phi^{-1}$

**Severity 3. Status valid. Confidence high.**
**Lens.** Costello + Composition.
**Target.** Wave-2 W1's split into C₁ᶠʷ (hypothesis-free) and
C₁ᶜᵒᵐᵖ (symmetric-filtration hypothesis), specifically W1-02
(R-W1-01).
**Claim under attack.** Wave-2 W1 phrased C₁ᶜᵒᵐᵖ as requiring
"continuity of $\Phi$, $d_{\rm CE}$, $d_\pi$ in some Tate filtration,
plus continuity of the inverse map (A1-08)." The implicit
composition is "C₁ᶠʷ + (continuity of $\Phi$ and $\Phi^{-1}$) ⇒
C₁ᶜᵒᵐᵖ" treated as a free promotion.
**Broken composition step.** Continuity of $\Phi$ and continuity of
$\Phi^{-1}$ are **two independent topological conditions**, and they
are *not* equivalent for arbitrary Tate Lie algebras. Concretely:
$\Phi$ is filtration-preserving in any filtration making
$d_{\rm CE}$ filtration-decreasing; $\Phi^{-1}$ is filtration-
preserving only if the **dual** filtration on PV (filtered by
polyvector degree and Tate window on the underlying functions) is
matched. Wave-2 W1 acknowledges this asymmetry (W1-02): "the CE
side is a completed symmetric algebra in the *product* convention…
while the PV side is the Schouten polyvector algebra over the
Tate-completed Kirillov–Poisson algebra (filtered by polyvector
degree…)." Naming the requirement as "continuity of $\Phi^{-1}$"
suggests a single one-way condition; what is actually required is
**joint** continuity in a **single** filtration that respects both
sides. The proper statement is:

> **Symmetric filtration hypothesis (sharpened).** There exists a
> single filtration $F^\bullet$ on the underlying graded vector
> space $\mathfrak h \oplus \mathfrak h^\vee[1]$, refining both the
> $\mathfrak m$-adic Tate filtration and the polyvector-degree
> filtration, in which **all four operators** ($d_{\rm CE}$, $d_\pi$,
> $\Phi$, $\Phi^{-1}$) are filtration-preserving and continuous.

For the formal symplectic disk, wave-2 W1 verifies this via
$C^L_{(a,b),(c,d)} = (ad-bc)$ filtration-decreasing (lines 73–77 of
W1 report). For abstract Tate Lie algebras, the **bidirectional**
condition is strictly stronger than either continuity statement
alone, and wave-2's R-W1-01 should be expanded to include the
bidirectional version.
**Counterexample / explicit higher-coherence requirement.** Take
$\mathfrak h$ = a Tate Lie algebra in which the structure constants
land in a *strictly larger* Tate window than their inputs (e.g.\ the
unweighted Hamiltonian $\mathfrak h_{\rm poly}$ on $\C^2$ with the
$\mathfrak m$-adic filtration: $\{z_1, z_2^{N+1}\} = (N+1) z_2^N$
*decreases* the $\mathfrak m$-adic degree by $N$, breaking the
filtration in the *reverse* direction; the filtration on the
PV side is therefore not matched). C₁ᶠʷ holds (pointwise on every
finite word); the promotion to C₁ᶜᵒᵐᵖ on the *unweighted* full
$\mathfrak h_{\rm poly}$ fails because $\Phi^{-1}$ is filtration-
*increasing* and not continuous in the symmetric filtration. This
is the same obstruction as `lem:finite-window-hamiltonian-obstruction`,
seen from the topological-symmetry side.
**Composition consequence.** Wave-2 W1's claim that C₁ᶠʷ + symmetric-
filtration ⇒ C₁ᶜᵒᵐᵖ is correct, **provided** the symmetric
filtration is bidirectional. The composition is **strictly** valid
on the formal disk where both directions are filtration-preserving;
on the unweighted abstract case it is **conditional** on a
hypothesis that is generically false.
**Files read.** `main.tex` 2381–2403, 2496–2503;
`tate-T1-weighted-completion.tex` 184–221 (the asymmetric-filtration
remark); wave-2 W1 lines 89–149.
**Confidence.** High.
**Blast radius.** This sharpens R-W1-01 from "explicit symmetric-
filtration hypothesis" to "explicit *bidirectional* symmetric-
filtration hypothesis." It does not invalidate the M-26 split; it
adds one phrase to the C₁ᶜᵒᵐᵖ statement.
**Minimal heal.** Insert in the proposed `thm:open-closed-derived-
center` (or its corollary on the formal disk) the phrase:

> "Suppose $\Phi$ and $\Phi^{-1}$ are *jointly* filtration-preserving
> in a single filtration refining the $\mathfrak m$-adic Tate
> filtration on $\mathfrak h$ and the polyvector-degree filtration
> on $\mathrm{PV}(\widehat{\mathbf S}_{\rm Tate}(\mathfrak h))$.
> [For the formal symplectic disk, the structure constants
> $C^L_{(a,b),(c,d)} = (ad-bc)$ are filtration-decreasing in both
> directions, so the joint filtration is the $\mathfrak m$-adic Tate
> filtration itself.]"

**Residual.** None at this layer. The bidirectional statement is
verifiable on the formal disk; it remains an exterior-face
hypothesis on abstract Tate Lie algebras.
**Adjudication.** Valid. Sharpens W1-02 / R-W1-01; preserves the
M-26 split.

---

### W3-W6-02 — C₂(NT), C₂(W), C₂(R) live on *different* sources; their "composition" is a span, not a chain

**Severity 4. Status valid. Confidence high.**
**Lens.** Composition primary; Costello secondary.
**Target.** Wave-2 W1's M-26 split into three C₂ admissibility
windows. Specifically, the implicit suggestion in Wave-2 W1 §5
("Convergence verdict") that "C₂(NT) ∘ C₂(W) ∘ C₂(R)" composes
along the lanes T1–T5.
**Claim under attack.** The three C₂ statements (NT, W, R) compose
as a chain of derived natural transformations between equivalent
source / target categories.
**Broken composition step.** They prove statements about *different*
Lie algebras, *different* coefficient categories, and *different*
notions of equivalence:

* **C₂(NT) source.** $\mathfrak h_{\le N} = \mathfrak m^3 / \mathfrak m^{N+1}$,
  finite-dimensional, in $\Cat{Vec}$ (no Tate completion needed
  because $\mathfrak h_{\le N}$ is finite-dim). Coefficient category:
  $\mathfrak h_{\le N}^\vee$ in $\Cat{Vec}$.
* **C₂(W) source.** $\mathfrak h_w = \varprojlim_{w_0} \prod_{d \le w_0}
  H_d^{(w)}$, *infinite-dim*, in $\Cat{TateVec}$. Coefficient
  category: weighted product dual
  $\mathfrak h^{\vee,w}_{\rm cont} = \varprojlim_{w_0} \prod_{d \le w_0}
  (H_d^\vee)^{(w^{-1})}$, **not the strict continuous dual**.
* **C₂(R) source.** Equivalence class of admissible weights; the
  source is not a Lie algebra but an equivalence class
  $[\mathfrak h_w]_{\rm reg}$ under diagonal rescaling
  $R_{w,w'}$. Coefficient category: same equivalence class in the
  cotangent direction.

The three sources do **not** sit in a chain. The compositions one
might consider are:

(a) NT ↪ R: nilpotent truncation is a *representative* of an
    equivalence class. **Holds**: $\mathfrak h_{\le N}$ embeds into
    every $\mathfrak h_w$ (for any admissible $w$) as the rank-bounded
    sub-Lie algebra in degrees $3, \ldots, N$. The image is a
    representative of the regulator-equivalence class on the
    finite-window quotient.

(b) W ↪ R: weighted is a representative of the equivalence class.
    **Holds by definition**: $\mathfrak h_w$ is one choice of
    admissible weight; another admissible weight $w'$ gives a
    representative diagonally isomorphic via $R_{w,w'}$.

(c) NT ∘ W: nilpotent truncation of a weighted Lie algebra. The
    composition $\mathfrak h_w \to \mathfrak h_{w, \le N}$ is the
    truncation in $\mathfrak m$-adic degree to monomials $3 \le d
    \le N$, with the weight $w$ restricted. This **is** the
    composition the wave-2 W1 split implicitly used; but the
    surrounding R-equivalence class is a *coarser* object (it is
    not generally true that two regulator-equivalent weights restrict
    to two regulator-equivalent NT-truncations, because the
    regulator-equivalence on R is in the *infinite-window* direction,
    while NT discards everything outside a single fixed window).

The composition diagram is **not a commutative chain** but rather a
**span**:

```
                C₂(NT) on m^3/m^{N+1}     C₂(W) on h_w
                       ↓                        ↓
                          \      /
                           \    /
                            \  /
                             ▼
                       C₂(R) on [h_w]_{reg}
                  (equivalence class of admissible weights)
```

The two arms (NT and W) feed C₂(R), but they do **not** compose
through C₂(R) in a derived sense: there is no derived natural
transformation NT → W → R that descends to the level of
indecomposable factors of the underlying Lie algebras.

**Counterexample / explicit higher-coherence requirement.** Take
two admissible weights $w(d) = q^d$ and $w'(d) = (q')^d$ with
$q \ne q'$ both $> 1$. The diagonal $R_{w,w'}$ is an isomorphism
on every finite window. Now restrict to $\mathfrak m^3$ (NT route).
The restricted maps $R_{w,w'}|_{\mathfrak h_{w, \le N}}$ are
isomorphisms of finite-dimensional Lie algebras at every $N$. **But:**
the inverse limit of NT representatives ($\mathfrak m^3$) is **not**
the same as the inverse limit of weighted representatives
($\mathfrak h_w$), because they live on different ambient Lie
algebras (the former excludes $H_1 \oplus H_2$; the latter
includes them). The two arms do not commute through C₂(R) at the
inverse-limit level. The "composition" that survives is only at
the **finite-window** level.
**Composition consequence.** The 5-way split is honest, but the
implicit *associativity* of "C₂(NT) ∘ C₂(W) ∘ C₂(R)" is **not** a
theorem the manuscript proves. What is proved is a **span**:
finite-window isomorphisms in the regulator class commute with
NT-truncation restricted to that class. The infinite-window /
inverse-limit composition is a different question, governed by
which sectors of $\mathfrak h$ each route covers.
**Files read.** `tate-T2-nilpotent-truncation.tex` 313–355 (lost
sectors); `tate-T1-weighted-completion.tex` 596–636 (admissible-
sector definition); `tate-T1-weighted-completion.tex` 634–707
(regulator-independence theorem); wave-2 W1 lines 198–280 (the
three windows proved structurally different).
**Confidence.** High.
**Blast radius.** Wave-2 W1's "C₂ split" is correct as a
disjunction of three named theorems; what is **not** proved is
that they assemble into a single derived statement on a unified
source. They are three siblings on three different sources, with
**partial** maps between them at the finite-window level only.
This is consistent with wave-2 W1's R-W1-02 ("a unified C₂
statement covering all three windows simultaneously is not a Phase-1
deliverable"), but it sharpens R-W1-02 from "future work" to "the
composition is structurally a span, not a chain — the unified
statement is *not* in the same category as its representatives."
**Minimal heal.** Add to the theorem-lanes / claim-strength ledger
entry for C₂ a remark:

> "C₂(NT), C₂(W), C₂(R) form a **span**: each prove statements about
> different source Lie algebras, sharing only the finite-window
> stable diagram. The composition NT → W → R is well-defined at the
> finite-window level (by diagonal rescaling), but does not extend
> to a derived natural transformation at the infinite-window /
> inverse-limit level. C₂(R) is a theorem about **equivalence
> classes** of admissible regulators; the equivalence class is the
> object, not the Lie algebra."

**Residual.** R-W3-W6-02: the unified statement (a single derived
$\infty$-categorical object containing NT, W, R as representatives)
is open and lives outside Phase-1. Possibility: a derived
filtered $\infty$-category whose objects are admissible
regulator-equivalence classes; this would require a *new*
category-theoretic construction, not a theorem of the existing
M-26 split.
**Adjudication.** Valid. Strengthens R-W1-02 from a residual to a
named structural feature: the M-26 split is honest as a span, not
as a chain.

---

### W3-W6-03 — `lem:tate-mittag-leffler-dictionary` (M-27): hypothesis package is verified by the *conjunction* of T1, T2, T3, T5 — not by any one lane

**Severity 3. Status valid. Confidence high.**
**Lens.** Composition primary; Costello secondary.
**Target.** Wave-2 W1's M-27 (W1-05, W1-06): the
`lem:tate-mittag-leffler-dictionary` lemma. Specifically, the claim
that the lemma's hypothesis package (Mittag-Leffler exactness on
inverse systems with surjective transitions and finite-dimensional
transition kernels in $\Cat{TateChain}_{\geq 0}^{\rm adm}$) is
verified at every invocation site (17 sites in `tate-T3` and `tate-P1`).
**Claim under attack.** The M-27 lemma is locally applicable at every
`\alpharef\ item~1` invocation in T3 and P1 by a single uniform
argument.
**Broken step.** Each invocation site uses the lemma on a **different**
inverse system, with different finite-dimensional pieces and
different transitions. The audit sites are:

* **T3:114** — model-categorical Mittag-Leffler exactness: tower of
  windowed acyclic cofibrations. Inverse system: pushouts of
  generating cofibrations across Tate windows. Transitions:
  truncation. Verified via finite-dimensional standard chain-complex
  theory (T3 lines 105–117).
* **T3:189** — operad-algebra transfer: filtered-colimit assembly
  of windowwise quasi-isomorphisms in $\mathcal P\text{-alg}$.
  Inverse system: $\mathrm{Free}_{\mathcal P}(F^w D^n)$. Transitions:
  pushouts along acyclic generating cofibrations.
* **T3:250** — Lefevre-Hasegawa transfer to conilpotent coalgebras:
  unit weak-equivalence checked windowwise. Inverse system: bar-cobar
  unit map at each window. Transitions: truncation.
* **T3:301–303** — main bar-cobar Quillen equivalence: limit/colimit
  swap of length cap and Tate window. Inverse system:
  $\{\Omega(C^{\rm CE}_*(\mathfrak g_{\le w}))\}_w$. Transitions:
  surjections of finite-dimensional dg algebras.
* **T3:514** — counit calculation: PBW filtration on
  $\widehat U(\mathfrak g)$, windowwise bar-cobar acyclicity.
* **T3:569** — module-category equivalence:
  $\mathrm{TateConilpCoAlg}_{\rm Lie}^{\rm cf} \simeq
  \mathrm{TateAssocAlg}_{\rm Lie}^{+,\rm cf}$. Inverse system:
  cofibrant-fibrant objects at each window.
* **P1 sites (9 invocations)** — Hadamard parametrix at each window,
  wave-front bound, counterterm tower. Inverse system:
  $\{P_{\epsilon,L}^{w,w_0}\}_{w_0}$ with surjective truncation
  transitions.

These inverse systems are **not** equivalent: they are constructed
from different building blocks (CE coalgebras, dg algebras, free
operad-algebras, propagators) and have different transition
structures (cofibration generators, surjections, truncations). The
M-27 lemma applies to each by a separate verification of the
surjective-transition hypothesis.

**Composition consequence.** The lemma is an **abstract**
Mittag-Leffler dictionary; its application at each site is a
**concrete instance**. The hypothesis package (surjective transitions
+ finite-dim transition kernels) is verified:

| Lane | Inverse system | Transitions | Verification |
|------|----------------|-------------|--------------|
| T1 | $\{P_{\epsilon,L}^{w,w_0}\}_{w_0}$ | Truncation | `lem:windowwise-parametrix`(2): surjective on coefficient direction |
| T2 | $\{\Phi_{\le N}\}_N$ | $\pi_{M\to N}$: surjection | `prop:colim-recovery`: each $\pi_{M\to N}$ is a Lie surjection of finite-dim spaces |
| T3 | Multiple (cofibrations, free algebras, PBW filtration, etc.) | Various, all surjective | `lem:tate-conilp-model` proof; each site verifies its own |
| T4 | N/A — T4 is a **no-go** for Costello-Li, no Mittag-Leffler invocation | — | — |
| T5 | $\{\pi_{\rm prim}\}_N$ at finite $N$ for stable cyclic words | Restriction | `prop:stable-trace-invariants`: stable in $N \ge d$ |

T4 does not contribute to the verification (it is the BV-cohomology
no-go route). The **conjunction** of T1, T2, T3, T5 verifies all 17
invocations; **no single lane** verifies all of them.

**Counterexample / explicit higher-coherence requirement.** A
"non-conjunctive" interpretation of M-27 — i.e.\ that T3 alone supplies the
dictionary — would fail because T3's inverse systems do not include
the Hadamard / propagator system of P1, which is a T1-Hadamard
construct. The composition coherence required is:

> **The `lem:tate-mittag-leffler-dictionary` lemma is statement-only;
> its applicability at any specific site is a separate hypothesis-
> verification step.** The 17 sites cited in W1-06 require **17
> separate verifications**, each checking surjective-transition
> + finite-dim-transition-kernel for that site's inverse system.
> Wave-2 W1's heal authors the lemma centrally; this report
> identifies that the **hypothesis verification is per-site**, with
> each verification supplied by the corresponding Tate lane.

**Files read.** `tate-T3-quillen-equivalence.tex` (full);
`tate-P1-hadamard-mittag-leffler.tex` (full); `tate-T1-weighted-completion.tex`
160–166 (lemma `lem:wt-weights-exist` providing finite-window
maxima); `tate-T2-nilpotent-truncation.tex` 376–432 (`prop:colim-recovery`).
**Confidence.** High.
**Blast radius.** M-27 survives, **with** the addition that the
lemma is statement-only and per-site verification is supplied by
T1, T2, T3, T5 (T4 is a no-go and does not feed the lemma). This is
a sharpening, not a downgrade: the lemma authored by Wave-2 W1 is
the **correct** central object, and the per-site verifications
already exist in T1, T2, T3, T5 as stated.
**Minimal heal.** When authoring `lem:tate-mittag-leffler-dictionary`
in `tate-T3` (per Wave-2 W1's WP2-1), add a sentence:

> "Each application of this lemma is per-site: the user must verify
> the surjective-transition + finite-dim-transition-kernel hypothesis
> on the specific inverse system at hand. The 17 invocations in
> `tate-T3` and `tate-P1` are verified by their respective ambient
> proofs (T3's bar-cobar Quillen equivalence proof; T1/P1's
> Hadamard parametrix construction at each window). T4
> (Costello-Li no-go) is structurally outside the lemma's scope."

**Residual.** None at the lemma level. The per-site verifications
are already inscribed in the corresponding lane texts.
**Adjudication.** Valid. Sharpens M-27 from "central lemma"
to "central lemma + per-site verification, where the per-site
verification is supplied by the conjunction of T1, T2, T3, T5."

---

### W3-W6-04 — Renormalization-coherence: the M-26 split survives change of regulator scheme **inside the admissible class**, but is **not** Costello-canonical

**Severity 4. Status valid. Confidence high.**
**Lens.** Costello primary; Composition secondary.
**Target.** The M-26 split's claim that C₂(R) is a regulator-
independent statement.
**Claim under attack.** The 5-way C₁/C₂ split is canonical with
respect to Costello's renormalization scheme, in the sense that
any choice of regulator (heat-kernel, Pauli-Villars, Hadamard
parametrix at any cutoff) gives the same split.
**Broken step.** The split is regulator-independent **inside** the
admissible class of weights (Definition `defn:regulator-admissible-sector`,
T1 lines 596–632), which requires four conditions:
- (A1) Surjective windowwise transitions.
- (A2) Vertexwise polynomial-degree-bounded interactions.
- (A3) Diagonal rescaling $R_{w,w'}$ identifies brackets, propagators,
  counterterms.
- (A4) Cohomology detected on finite quotients and associated graded.

A **change of regulator scheme** that *preserves* (A1)–(A4) gives a
regulator-equivalent C₂(R); this is `thm:wt-regulator-independence-admissible`.
A **change of regulator scheme** that **leaves** the admissible class
(e.g.\ a non-exponential weight failing (W1) bracket-tameness, like
the super-exponential $w(d) = \exp(d^2)$ of `ex:bad-weight-not-regulator`,
or a regulator scheme outside the Mittag-Leffler envelope, e.g.\ a
non-surjective truncation) gives an **inequivalent** C₂(R), and the
M-26 split is **not** preserved.

**Composition consequence.** The M-26 split is **regulator-class-
canonical**: it is canonical inside the admissible class, **not**
across admissible-class boundaries. The Costello-canonicity question
("does the split survive a change of regulator that comes from a
different physical setup, e.g.\ Pauli-Villars vs.\ heat-kernel?") is
answered by checking whether the new regulator lives in the
admissible class of T1.

This is a **physics-level** subtlety: in Costello's *Renormalization
and Effective Field Theory* (2011) Ch.\ 5, the heat-kernel BV
regularization is not canonical *as a scheme*; what is canonical is
the *equivalence class* of effective interactions under the RG flow.
The M-26 split inherits this: it is canonical up to admissible-class
equivalence, not pointwise.

**Counterexample / explicit higher-coherence requirement.** Two
inequivalent regulators:

(α) Exponential weight $w(d) = q^d$, $q > 1$: in the admissible
    class. C₂(W) holds with the weighted product dual. C₂(R) holds
    among admissible exponential weights.

(β) **Non-exponential weight** $w'(d) = d^2$ (polynomial, not
    exponential): fails (W1) bracket-tameness. The bracket
    $\{H_p, H_q\} \subset H_{p+q-2}$ has weight ratio
    $w'(p+q-2) / (w'(p) w'(q)) = (p+q-2)^2 / (pq)^2 \to \infty$ as
    $p, q \to \infty$. Bracket-tameness fails. The corresponding
    coefficient kernel is **not** regulator-admissible. C₂(W) does
    not hold for $w'$.

(γ) **Heat-kernel cutoff at fixed $L$ but with a Pauli-Villars
    regulator on the coefficient side**: live outside the standard
    admissible class. Different propagator factorization; the
    `eq:wt-propagator-factor` (T1 line 78) does not apply.
    Costello's RG flow is different. The M-26 split does not
    automatically transfer.

**Higher-coherence requirement.** Wave-3-W6 names a residual:

> **R-W3-W6-04 (regulator-class-canonicity).** The M-26 split is
> regulator-class-canonical *inside* the admissible class of weights
> (Definition `defn:regulator-admissible-sector`). Costello-
> canonicity *across* regulator schemes (heat-kernel vs.\ Pauli-
> Villars vs.\ Hadamard parametrix) is **not** a theorem of M-26;
> it requires a separate verification that the new scheme falls in
> the admissible class. This is a Phase-4 / cross-regulator question.

**Files read.** `tate-T1-weighted-completion.tex` 596–814 (admissible-
sector + regulator-independence + the no-go for super-exponential
weights); Costello, *Renormalization and Effective Field Theory*,
AMS Math.\ Surveys 170 (2011) Ch.\ 5–7 (cited in the manuscript at
T1:300 and elsewhere).
**Confidence.** High.
**Blast radius.** Wave-2 W1's stable-core declaration (C₂(R) "stable
on regulator-independent finite-window observables") is correct as
written, but its *boundary of regulator-canonicity* is not stated.
This sharpens the stable-core declaration: the M-26 split is
**inside** the admissible class; it does not promise canonicity
across admissible-class boundaries. This does not invalidate M-26;
it adds an explicit hypothesis layer.
**Minimal heal.** In the claim-strength ledger entry for "CE/PV
derived centre" and the C₂(R) statement in `theorem-lanes.tex`,
add a sentence:

> "C₂(R) is regulator-independent **within the admissible class** of
> Definition `defn:regulator-admissible-sector`. A regulator scheme
> outside this class (e.g.\ a non-Mittag-Leffler completion or a
> non-exponential weight failing bracket-tameness) is **not** in
> the proved equivalence class; for such a scheme the M-26 split
> must be re-derived."

**Residual.** R-W3-W6-04 (above): cross-regulator-class canonicity
is open. Phase-4.
**Adjudication.** Valid. Sharpens stable-core declaration; preserves
M-26.

---

### W3-W6-05 — BV/BRST coherence: C₂(W)'s QME satisfied **modulo** weight filtration; conditional on `prob:weighted-rg-locality`

**Severity 4. Status valid. Confidence high.**
**Lens.** Costello primary.
**Target.** Wave-2 W1's classification of C₂(W) as stable. Specifically,
the implicit suggestion that C₂(W) covers **both** classical and
quantum (one-antifield, all-order in $\hbar$) cotangent identities.
**Claim under attack.** C₂(W) satisfies the Quantum Master Equation
exactly.
**Broken step.** Inspection of `tate-T1-weighted-completion.tex` lines
493–530 (`prop:wt-conditional-qme-lift`) shows that the all-order
quantum lift $\Phi_{\hbar, \rm cond}^w$ is **conditional** on the
identity in `prob:weighted-rg-locality`:

> "Assume the Costello-locality/QME compatibility identity of
> Problem~\ref{prob:weighted-rg-locality}: the finite-window
> counterterm system for the mixed brane-defect interaction has
> vanishing obstruction class and is compatible with the weighted
> coefficient category. Under this assumption, the formal quantum
> derived-center map $\Phi_\hbar^{(0)}$ … has a weighted-continuous
> cotangent extension."

Cross-checking `appendix-unreduced-bv-qme.tex` lines 33–91
(`thm:app-unreduced-polynomial-centrality-no-go`) and lines 93–158
(`prop:app-scalar-contact-qme-class`) confirms:

* The **classical** cotangent lift on C₂(W) (item (d) of
  `thm:wt-cotangent-lift`) is unconditional.
* The **quantum** cotangent lift (`prop:wt-conditional-qme-lift`,
  `cor:wt-cotangent-lift-conditional-hadamard` in P1) is
  **conditional on `prob:weighted-rg-locality`**.
* The QME obstruction class is the **mixed brane-defect**
  obstruction in $H^1(\mathcal O_{\rm loc}(\mathcal E_w),
  Q + \{I_0, -\})$, and `prop:app-scalar-contact-qme-class` shows
  that this obstruction is **not zero** on the scalar-reduced
  Hamiltonian source: the class is $\hbar N [\bar c]$, exactly the
  Capelli central anomaly (M-32 in master ledger).

**Composition consequence.** The QME for C₂(W) holds at the
**classical chain level** (Schouten/Lichnerowicz $P_0$-bracket
compatibility, item (d) of `thm:wt-cotangent-lift`), but **not** at
the all-order quantum level on the unreduced source. The
all-order quantum extension is **conditional** and propagates to
Theorem G (the U(1) anomaly), not to Theorems A–F.

**Counterexample / explicit higher-coherence requirement.** Take the
quantum classical Casimir of Theorem G: $[\bar c] \in H^2_{\rm Lie}(\bar A; \C)$.
On C₂(W) with weight $w(d) = q^d$, the corresponding obstruction class
$\hbar N [\bar c] \in H^1(\mathcal O_{\rm loc}(\mathcal E_w),
Q + \{I_0, -\})$ is **not exact** by `prop:app-scalar-contact-qme-class`.
Hence the QME on the **unreduced** weighted source has a non-zero
obstruction. The QME compatibility on C₂(W) holds **modulo this
obstruction class**, not exactly.

**Higher-coherence requirement.** Wave-3-W6 names:

> **R-W3-W6-05 (QME on C₂(W) is conditional, not exact).** C₂(W)'s
> quantum extension at all $\hbar$-orders is conditional on
> `prob:weighted-rg-locality` (the mixed brane-defect QME obstruction
> class). Wave-2 W1's stable-core declaration of C₂(W) is correct
> *at the classical level*; the quantum extension is **conditional**
> and should be flagged in any cross-reference. The unreduced
> all-order QME is governed by `thm:app-unreduced-polynomial-centrality-no-go`
> (no polynomial unreduced lift) plus `prop:app-scalar-contact-qme-class`
> (the scalar contact class is $\hbar N [\bar c]$, exactly Theorem G's
> Capelli anomaly).

**Files read.** `tate-T1-weighted-completion.tex` 408–530;
`appendix-unreduced-bv-qme.tex` 1–179 (full);
`tate-P1-hadamard-mittag-leffler.tex` 274–323 (Hadamard reduction
to brane-defect QME).
**Confidence.** High.
**Blast radius.** This is the most consequential composition
obstruction identified. It does **not** invalidate the M-26 split,
but it does sharpen the C₂(W) statement: classical C₂(W) is
unconditional; quantum C₂(W) is conditional on
`prob:weighted-rg-locality`. The Capelli anomaly (Theorem G) is the
**concrete obstruction**; in this sense, the M-26 split is closed
**up to** Theorem G's anomaly class.
**Minimal heal.** In the C₂(W) statement and in any cross-reference
to it, distinguish:

> **C₂(W)-cl (classical).** Unconditional. The classical cotangent
> lift `thm:wt-cotangent-lift` items (a)–(d).
> **C₂(W)-q (quantum).** Conditional on `prob:weighted-rg-locality`
> (i.e.\ on the vanishing of the mixed brane-defect QME obstruction
> class in $H^1(\mathcal O_{\rm loc}(\mathcal E_w), Q + \{I_0, -\})$).
> The obstruction class is **non-zero** on the unreduced scalar-
> reduced Hamiltonian source by `prop:app-scalar-contact-qme-class`;
> it is the same class as Theorem G's $\hbar N [\bar c]$. The
> quantum extension of C₂(W) is therefore *known not to be
> unconditional* — it is **gated by Theorem G**.

This is the strongest composition obstruction in this report: the
M-26 split's C₂(W) and the Theorem G anomaly are **the same
obstruction**, viewed from two sides.
**Residual.** R-W3-W6-05: see above.
**Adjudication.** Valid. Sharpens C₂(W) into C₂(W)-cl + C₂(W)-q,
with the quantum side conditional on Theorem G's anomaly class.

---

## §2. Stable-core update (Wave-3-W6 amended)

The wave-2 W1 / W6 stable core was: A, B, C₁ᶠʷ, C₁ᶜᵒᵐᵖ, C₂(NT),
C₂(W), C₂(R), D, E, F, G, after the M-26 split + M-27 lemma + M-33
DAG heals. Wave-3-W6's amendments:

- A. Stable.
- B. Stable.
- **C₁ᶠʷ.** Stable, hypothesis-free.
- **C₁ᶜᵒᵐᵖ.** Stable, with **bidirectional** symmetric-filtration
  hypothesis (W3-W6-01 sharpens R-W1-01).
- **C₂(NT).** Stable on $\mathfrak m^3 / \mathfrak m^{N+1}$ only;
  stable as a **representative** of the regulator-equivalence class
  C₂(R) (W3-W6-02 sharpens the composition).
- **C₂(W)-cl.** Stable on weighted Tate coefficient category,
  classical chain level (W3-W6-05).
- **C₂(W)-q.** Conditional on `prob:weighted-rg-locality` /
  Theorem G's anomaly class (W3-W6-05).
- **C₂(R).** Stable on regulator-independent finite-window
  observables, **inside** the admissible class of admissible weights
  (W3-W6-04 sharpens the canonicity statement).
- D. Stable.
- E. Stable.
- F. Stable.
- G. Stable, with the new **identification** that Theorem G's
  $[\bar c]$ class **gates** the quantum extension of C₂(W) — same
  obstruction, two sides.

The 5-way C₁/C₂ split (M-26) survives, with sharper hypothesis layers:
- C₁ᶜᵒᵐᵖ: bidirectional symmetric filtration (was: continuity of
  $\Phi^{-1}$).
- C₂ family: span structure (NT, W as arms feeding R; not a chain).
- C₂(W): split into classical (unconditional) and quantum
  (conditional).
- C₂(R): canonicity inside the admissible class only.

The M-27 lemma survives, with the addition that per-site verification
is supplied by T1, T2, T3, T5 (T4 is a no-go).

The M-33 DAG (8-link) is unchanged at the wave-3-W6 level: the 8-link
DAG is at the *factorization-theorem* (Theorem E lane) level, not at
the C₁/C₂ split level. Wave-3-W6's targets concern C₁/C₂; the DAG
is downstream.

---

## §3. Heal proposals (smallest first)

### Tier 1 — Statement-only edits

**WP3-W6-1 (W3-W6-01).** In the proposed `thm:open-closed-derived-
center` (or `cor:derived-center-formal-disk`), insert before the
displayed equality:

> "Suppose moreover that the Tate filtration on
> $\mathfrak h \oplus \mathfrak h^\vee[1]$ is **bidirectionally
> symmetric**: a single filtration in which $d_{\rm CE}$, $d_\pi$,
> $\Phi$, **and** $\Phi^{-1}$ are jointly filtration-preserving and
> continuous. For the formal symplectic disk, the structure constants
> $C^L_{(a,b),(c,d)} = (ad-bc)$ landing in degree $a+b+c+d-2$ are
> filtration-decreasing in **both** the CE and the polyvector-degree
> directions, so the joint filtration is the $\mathfrak m$-adic Tate
> filtration itself, and the bidirectional symmetric-filtration
> hypothesis is automatic on this Lie algebra."

**WP3-W6-2 (W3-W6-02).** In `theorem-lanes.tex` Lane 3 (CE/PV
center), and in the `claim-strength-ledger.tex` entry for "CE/PV
derived centre," add:

> "C₂(NT), C₂(W), C₂(R) form a **span**: each proves a statement
> about a different source Lie algebra, sharing only the finite-
> window stable diagram. The composition NT → W → R is well-defined
> at the finite-window level; the infinite-window / inverse-limit
> composition is governed by which sectors of $\mathfrak h$ each
> route covers. C₂(R) is a theorem about the regulator-equivalence
> class itself, not about a single Lie algebra. A unified statement
> covering all three windows simultaneously is open (Phase-4)."

**WP3-W6-3 (W3-W6-04).** In the C₂(R) statement and its
cross-reference in `claim-strength-ledger.tex`, add the sentence:

> "C₂(R) is regulator-independent **within the admissible class** of
> Definition `defn:regulator-admissible-sector`. A regulator scheme
> outside this class (non-exponential weight failing bracket-
> tameness, or a regulator outside the Mittag-Leffler envelope) is
> **not** in the proved equivalence class; for such a scheme the
> M-26 split must be re-derived."

**WP3-W6-4 (W3-W6-05).** Split C₂(W) into C₂(W)-cl (classical) and
C₂(W)-q (quantum, conditional). In `theorem-lanes.tex` and
`claim-strength-ledger.tex`:

> "**C₂(W)-cl** is the **classical** weighted Tate cotangent
> identity (`thm:wt-cotangent-lift` items (a)–(d)), unconditional.
> **C₂(W)-q** is the **quantum** all-$\hbar$-order extension
> (`prop:wt-conditional-qme-lift`,
> `cor:wt-cotangent-lift-conditional-hadamard`), **conditional** on
> the vanishing of the mixed brane-defect QME obstruction class in
> $H^1(\mathcal O_{\rm loc}(\mathcal E_w), Q + \{I_0, -\})$
> (`prob:weighted-rg-locality`). The obstruction class is
> **non-zero** on the unreduced scalar-reduced Hamiltonian source
> (`prop:app-scalar-contact-qme-class`); it equals $\hbar N [\bar c]$,
> exactly Theorem G's Capelli anomaly. The quantum extension of
> C₂(W) and Theorem G are the **same** obstruction class viewed from
> two sides."

### Tier 2 — Per-site verification statement for `lem:tate-mittag-leffler-dictionary`

**WP3-W6-5 (W3-W6-03).** In Wave-2 W1's WP2-1 (the dictionary
lemma authoring), add a sentence after the lemma:

> "Each application of this lemma is per-site: the user must verify
> the surjective-transition + finite-dim-transition-kernel hypothesis
> on the specific inverse system at hand. The 17 invocations in
> `tate-T3` and `tate-P1` are each verified by their respective
> ambient construction (T3: bar-cobar Quillen equivalence model
> structure proof; T1/P1: Hadamard parametrix at each window; T2:
> nilpotent-truncation surjection $\pi_{M\to N}$ on finite-dim
> $\mathfrak h_{\le N}$; T5: stable cyclic-word truncation in
> $N \ge d$). The conjunction of T1, T2, T3, T5 verifies all
> applications. T4 (Costello-Li no-go) is structurally outside this
> lemma's scope."

### Tier 3 — Architectural cross-link

**WP3-W6-6.** In `principles.tex` or `theorem-lanes.tex`, add a
remark naming the W3-W6-05 identification:

> "**Theorem G's anomaly class gates C₂(W)-q.** The Capelli central
> anomaly $[\bar c] \in H^2_{\rm Lie}(\bar A; \C)$ of Theorem G and
> the mixed brane-defect QME obstruction class
> $[\hbar N \bar c] \in H^1(\mathcal O_{\rm loc}(\mathcal E_w),
> Q + \{I_0, -\})$ governing C₂(W)-q are **the same anomaly line**,
> viewed from the closed (CE) and open (BV) sides. This unifies M-31
> (the $[\mathrm{Tr}\,\psi]_{\rm BV} \leftrightarrow [\bar c]_{\rm CE}$
> identification) and W3-W6-05 (the QME conditional on Theorem G).
> The C₂(W) split into classical + quantum reflects this anomaly:
> the classical level is unconditional; the quantum level is
> obstructed by the same anomaly that defines Theorem G."

This is the strongest **structural unification** the wave-3-W6
report inscribes: the 5-way C₁/C₂ split's quantum-conditional
boundary (R-W3-W6-05) is **the same boundary** as Theorem G's
anomaly. It is not a new obstruction; it is one obstruction with
two faces.

---

## §4. Residuals after Wave-3-W6

- **R-W3-W6-01 (from W3-W6-01).** Bidirectional symmetric-filtration
  is a strict additional condition on abstract Tate Lie algebras for
  C₁ᶜᵒᵐᵖ. Verified on the formal disk; not a free promotion in
  general. Sharpens R-W1-01.
- **R-W3-W6-02 (from W3-W6-02).** Unified statement covering all
  three C₂ windows simultaneously — span structure, not chain.
  Phase-4. Sharpens R-W1-02.
- **R-W3-W6-03 (from W3-W6-03).** Per-site verification of the M-27
  lemma is supplied by the conjunction of T1, T2, T3, T5; T4 is no-go.
  Closure: explicit cross-reference at the lemma authoring.
- **R-W3-W6-04 (from W3-W6-04).** Cross-regulator-class canonicity
  (heat-kernel vs.\ Pauli-Villars vs.\ Hadamard) is open. Phase-4.
- **R-W3-W6-05 (from W3-W6-05).** C₂(W)-q is conditional on
  `prob:weighted-rg-locality`; the obstruction class is **the same**
  as Theorem G's $[\bar c]$. Closure: a Costello-RG specialist
  computation of the brane-defect QME obstruction in the weighted
  Tate envelope, using
  `thm:hadamard-mittag-leffler` (already inscribed) plus the
  vanishing-class argument that is currently *not* in the manuscript
  (and may genuinely be non-zero, per
  `prop:app-scalar-contact-qme-class`). Estimate: open
  research problem, possibly *non-vanishing* on the unreduced
  $\mathfrak{gl}_N$ scalar-reduced source.

---

## §5. Convergence verdict

**M-26 (5-way C₁/C₂ split).** Survives the Costello + Composition
lens, with three sharpenings:
- C₁ᶜᵒᵐᵖ requires bidirectional symmetric filtration (W3-W6-01).
- C₂(NT, W, R) is a **span**, not a chain (W3-W6-02).
- C₂(W) splits into classical (unconditional) + quantum (conditional
  on Theorem G's anomaly) (W3-W6-05).
The 5-way split is honest; the hypothesis layer beneath is sharpened.
**Verdict: VALID, sharpened.**

**M-27 (`lem:tate-mittag-leffler-dictionary`).** Survives. Per-site
verification supplied by the conjunction of T1, T2, T3, T5 (T4 is
no-go). The lemma is statement-only; its applicability at each of
17 sites is verified by the ambient lane. **Verdict: VALID, with
explicit conjunctive structure named.**

**Stable core (Theorems A, B, C₁ᶠʷ, C₁ᶜᵒᵐᵖ, C₂(NT), C₂(W),
C₂(R), D, E, F, G).** Survives, with the C-block now finer:
A, B, C₁ᶠʷ, C₁ᶜᵒᵐᵖ (bidirectional), C₂(NT), C₂(W)-cl, C₂(W)-q
(conditional on Theorem G), C₂(R) (admissible-class only), D, E, F,
G (gates C₂(W)-q). **Verdict: STABLE, with sharper hypothesis
boundaries.**

The single most important new technical insight: **Theorem G's
anomaly $[\bar c]$ and the QME obstruction governing C₂(W)-q are
the same class, viewed from CE and BV sides.** This unifies M-31
(`[\mathrm{Tr}\,\psi]_{\rm BV} \leftrightarrow [\bar c]_{\rm CE}`)
with the C₂(W)-q-conditional residual. There is **one** anomaly,
not two; the M-26 split's quantum-side boundary and Theorem G's
classification are the **same** structural obligation.

**Posture against Wave 2.** Wave-2 W1's 5-way split is preserved;
wave-2 W6's 8-link DAG is not in scope (it concerns Theorem E lane,
not C₁/C₂). The wave-3-W6 contribution is a sharpening of the
hypothesis layers under the M-26 split, plus the structural
identification of the C₂(W)-q residual with Theorem G's anomaly. No
new theorems are needed; five named statements (W3-W6-01 through
W3-W6-05) are added to the master ledger.

End of W3-W6 report.
