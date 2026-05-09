# Wave 2 — W1 Attack Report — Costello / Hypotheses Lens

**Date.** 2026-04-28.
**Author.** Raeez Lorgat.
**Wave.** 2, agent W1.
**Lens.** Costello (factorization algebras, BV/BRST, renormalization)
+ Hypotheses (which theorem hypotheses are missing, weakened, or
silently strengthened?).
**Mode.** Read-only / proposal-only.
**Posture against Wave 1.** The wave-1 master ledger declared a stable
core conditional on the C₁/C₂ split healing M-01. This report attacks
that split itself, the surrounding admissible-envelope claims, and
the residuals R-05 and M-21 that wave 1 left undecided.

---

## §1. New ledger entries

### W1-01 — C₁ is **not** hypothesis-free: continuous-Leibniz extension is what runs the proof
**Severity 3. Status valid. Confidence high. Lens.** Hypotheses primary.
**Target.** `main.tex`:2322–2438 (`thm:open-closed-derived-center`); the
proof's "Cochain identity on the full completed algebra" paragraph,
lines 2381–2396; the Wave-1 minimal heal calling C₁ "hypothesis-free,
applies to any Lie h via Lichnerowicz–Schouten + structure-constant
identification".
**Claim under attack.** Theorem C₁ as proposed by Wave 1 (M-01 minimal
heal): "for *any* Lie algebra $\mathfrak h$ in $\Cat{TateVec}$, the
generator dictionary $c^I\mapsto\theta^I$, $u_I\mapsto O_I$ matches
the differentials on length-$\le 1$ generators and respects the
Schouten-bracket relations".
**Broken step.** The cochain-level identification asserted by the
manuscript is not just a generator equality; it is the equality of
the two completed dg algebras. The proof at `main.tex`:2381–2396
explicitly invokes (a) graded Leibniz on the *completed* free
graded-commutative algebra structures on each side and (b)
"Tate-completeness of both sides plus continuity of $d_{\mathrm{CE}},
d_\pi,\Phi$ in the Tate filtration extends the equality to the
completed algebras". Step (b) is a continuity statement on a specific
topology. Without it, generator-level matching plus Leibniz gives
agreement on every word at fixed total length, but the pointwise
equality on a completed product is not automatic: the reduction is
through finite-window quotients, and convergence requires the same
Mittag-Leffler regularity that Wave 1 attached only to C₂.
**Evidence type.** proof-internal step audit.
**Evidence ref.** `main.tex`:2381–2396; the displayed Leibniz step
plus "Tate-completeness of both sides … extends the equality".
**Files read.** `main.tex` 2196–2475 and 3295–3470;
`tate-T2`:400–500.
**Confidence.** High.
**Blast radius.** The Wave-1 claim that C₁ as the
*generator-plus-Schouten* identity is hypothesis-free needs sharpening.
What is genuinely hypothesis-free is the **finite-word identity**
$\Phi(d_{\mathrm{CE}}w)=d_\pi\Phi(w)$ for every word $w$ of bounded
total CE length. Promotion to the completed algebra needs continuity
of $\Phi$, $d_{\mathrm{CE}}$, $d_\pi$ in *some* Tate filtration on
$\mathfrak h$. The manuscript's Cor.~`derived-center-formal-disk`
(`main.tex`:2496–2503) hedges exactly this way: "no lower-central
conilpotence of the full Hamiltonian algebra is used" — but that
hedge is silent on the topology question.
**Minimal heal.** Restate C₁ as **Theorem C₁ᶠʷ (finite-word generator
identity)**: for any Tate Lie algebra $\mathfrak h$ and the linear-Poisson
target $A_\partial=\widehat{\mathbf S}_{\mathrm{Tate}}(\mathfrak h)$,
the assignment $c^I\mapsto\theta^I,u_I\mapsto O_I$ extends to a
compatible cochain map of free graded-commutative algebras on
**finite-word truncations**: for every CE total length $N$ and every
Tate window $w$, $\Phi$ intertwines $d_{\mathrm{CE}}$ and $d_\pi$ on
$\mathrm{Length}_{\le N}\cap F^{\le w}$. Promotion from finite-word
truncations to the completed algebra is then **C₁ᶜᵒᵐᵖ**: a separate
statement requiring continuity of all three operators in the filtration.
For the formal symplectic disk $\mathfrak h=(z_1,z_2)\C[[z_1,z_2]]$
with the $\mathfrak m$-adic Tate filtration, C₁ᶜᵒᵐᵖ holds by direct
inspection of the structure constants $C^L_{(a,b),(c,d)}=(ad-bc)$
landing in degree $a+b+c+d-2$, i.e. the differentials are
filtration-decreasing and continuous; the finite-word-to-completed
reduction is then trivially Mittag-Leffler exact. **The manuscript
gets the result it claims, but only because the structure constants
on this *specific* Lie algebra are filtration-tame.**
**Residual.** The continuity of $\Phi$, $d_{\mathrm{CE}}$, $d_\pi$ is
not generically true for arbitrary Tate Lie algebras with arbitrary
filtrations; it must be checked for each application. The hedge in
the corollary should be propagated to the abstract C₁ statement.
**Adjudication.** Valid. The Wave-1 split is structurally correct,
but C₁'s "hypothesis-free" phrasing is overclaim; what is hypothesis-
free is the finite-word generator identity, which is what
`prop:ce-source-obstruction` already proves.
**Deciding evidence.** Insertion of the C₁ᶠʷ vs C₁ᶜᵒᵐᵖ distinction
into the proposed split.

### W1-02 — Inverse-map continuity (A1-08) is non-trivial precisely where C₁ᶜᵒᵐᵖ runs
**Severity 3. Status valid. Confidence high. Lens.** Hypotheses primary.
**Target.** `main.tex`:2398–2403, the "Inverse" paragraph of the C
theorem proof: "The assignment $\theta^I\mapsto c^I$, $O_I\mapsto u_I$
extends to a continuous algebra homomorphism in the opposite direction.
By the same Leibniz argument, it intertwines $d_\pi$ and
$d_{\mathrm{CE}}$. The two compositions fix generators, hence fix the
completed algebras."
**Claim under attack.** The inverse $\Phi^{-1}:\theta^I\mapsto c^I$,
$O_I\mapsto u_I$ is a continuous algebra homomorphism on the
**completed** PV algebra; symmetric Leibniz argument plus
generator-fixing gives invertibility on the **completed** algebras.
**Broken step.** This is exactly Wave 1's residual A1-08
(continuity of inverse map). The two sides are not symmetric: the CE
side is a completed symmetric algebra in the *product* convention
(filtered by CE-length and Tate window), while the PV side is the
Schouten polyvector algebra over the Tate-completed Kirillov–Poisson
algebra (filtered by polyvector degree and Tate window on the
underlying functions). The correspondence on generators is
$|c^I|=1, |u_I|=0$ on the CE side vs $|\theta^I|=1, |O_I|=0$ on the
PV side, but the Tate convergence of an arbitrary PV element
$\sum_n a_n O_{I_1}\cdots O_{I_n}\theta^{J_1}\cdots\theta^{J_m}$ is
not the same Tate convergence of an arbitrary CE cochain
$\sum_n b_n u_{I_1}\cdots u_{I_n}c^{J_1}\cdots c^{J_m}$. The
identification at the level of completed graded vector spaces is
fine; the identification of *continuity* of the bijection requires
showing the two filtrations match.
**Evidence type.** proof-internal step audit; cross-link to A1-08
left undecided in Wave 1.
**Evidence ref.** `main.tex`:2398–2403.
**Files read.** `main.tex`:2354–2403; `tate-T1`:184–220 (definition of
the weighted Tate coefficient pair, where the asymmetry is explicit:
"The second factor is a product coefficient module, not the strict
continuous dual of the first product Tate space").
**Confidence.** High.
**Blast radius.** Non-trivial: the *inverse* of $\Phi$ is the map
that turns the existence of $\Phi$ as a quasi-isomorphism into the
existence of $\Phi$ as an isomorphism. If the inverse is only
continuous on a smaller subcategory, then C₁ᶜᵒᵐᵖ degenerates to "a
continuous map with a generically discontinuous inverse" — an
isomorphism only on the dense finite-word-truncation subspace.
**Minimal heal.** Make the topological-symmetry datum **explicit** in
the definition of $\Phi$: declare a single Tate filtration in which
both sides are simultaneously complete, and require
**continuity of the inverse** on the same filtration. For the
formal disk this is achievable: the filtration "min(CE-length,
PV-polyvector-degree)" together with the $\mathfrak m$-adic Tate
window gives a symmetric filtration; both differentials and both
algebra maps preserve it; the inverse is filtration-preserving by
the symmetry of the structure constants.
**Residual.** For the abstract Theorem C₁ᶜᵒᵐᵖ on arbitrary Tate Lie
algebras, the inverse-continuity is genuinely an additional
hypothesis beyond Tate-conilpotency. This sharpens A1-08 from
"undecided" (Wave 1) to "explicit additional hypothesis required for
abstract C₁ᶜᵒᵐᵖ; verified by direct calculation on the formal
symplectic disk".
**Adjudication.** Valid. Closes Wave 1's A1-08 in the negative for
the abstract case and positive for the concrete formal-disk case.
**Deciding evidence.** Explicit symmetric filtration on
$C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak g)$ vs
$\mathrm{PV}(A_\partial)$ on the formal symplectic disk.

### W1-03 — Leibniz extension at higher tensor length (A1-09) is genuine and reduces to a single inductive identity
**Severity 2. Status valid. Confidence high. Lens.** Hypotheses primary.
**Target.** `main.tex`:2381–2396; Wave 1 residual A1-09.
**Claim under attack.** "Generator-level agreement plus Leibniz/algebra-
homomorphism gives agreement on every word in $\{c^I,u_J\}$ at fixed
total length".
**Broken step.** The argument at length 1 is the displayed generator
calculation; the argument at length 2 needs $d_{\mathrm{CE}}(xy) =
(d_{\mathrm{CE}}x)y \pm x(d_{\mathrm{CE}}y)$ and the same for $d_\pi$,
plus $\Phi$ a graded algebra map. This is correct but **not** the
non-trivial step. The non-trivial inductive step is at length $\ge 2$
when $x$ or $y$ is itself **closed** but the bracket on the source
has both $u$- and $c$-components: $d_{\mathrm{CE}}u_K=C^L_{KJ}u_Lc^J$
mixes the cotangent and Hamiltonian directions. To verify
$\Phi(d_{\mathrm{CE}}(u_Iu_J))=d_\pi(\Phi(u_I)\Phi(u_J))$
$=d_\pi(O_IO_J)$ requires expanding both sides:
$\Phi(d_{\mathrm{CE}}u_I\cdot u_J + u_I\cdot d_{\mathrm{CE}}u_J)
=\Phi(C^L_{IM}u_Lc^Mu_J + u_IC^L_{JM}u_Lc^M)
=C^L_{IM}O_LO_J\theta^M + C^L_{JM}O_IO_L\theta^M$,
while $d_\pi(O_IO_J)=O_J\cdot d_\pi O_I + O_I\cdot d_\pi O_J
=O_JC^L_{IM}O_L\theta^M + O_IC^L_{JM}O_L\theta^M$. These agree under
graded-commutativity of $O_IO_J$. The induction at length 3 is the
same up to signs.
**Evidence type.** verification.
**Evidence ref.** `main.tex`:2381–2396.
**Files read.** Same.
**Confidence.** High.
**Blast radius.** The Leibniz extension is a genuine induction, not an
incantation; A1-09's residual is closeable but only after explicit
verification at length 2 and 3. The Wave-1 ledger is right that this
is non-trivial; the *content* is non-trivial mostly in the
**sign convention** (when does $u_Lc^M$ pick up a Koszul sign in the
PV side?) and the **Schouten antisymmetry** ($C^L_{IJ}=-C^L_{JI}$
collapses cross-terms).
**Minimal heal.** Author **`lem:tate-leibniz-extension-cu`** in the
sign-convention appendix (Wave 1's plan §6 item 8): explicit length-2
and length-3 verifications of $\Phi(d_{\mathrm{CE}}\cdot)=d_\pi\Phi$
on the four word types $u_Iu_J$, $u_Ic^J$, $c^Ic^J$, and the
length-3 mixed combinations, with explicit Koszul signs. The
inductive step from length $n$ to length $n+1$ is then a single
Leibniz application plus the previous case.
**Residual.** None at this layer; the inductive proof is short and
mechanical once the sign convention is declared.
**Adjudication.** Valid. Closes Wave 1's A1-09 with concrete heal.
**Deciding evidence.** The two length-2/length-3 calculations in the
sign appendix.

### W1-04 — C₂'s admissibility windows are NOT interchangeable
**Severity 4. Status valid. Confidence high. Lens.** Costello primary.
**Target.** Wave 1's M-01 proposal that "the nilpotent truncations
$\mathfrak h_{\le N}=\mathfrak h/\mathfrak m^{N+1}$ from T2, the
weighted regulators $\mathfrak h^w$ for $w>1$ from T1, and the
cofiltered limit recovered through the regulator-independence
argument of Obligation III" all carry C₂ honestly.
**Claim under attack.** The three admissibility windows are
co-extensive carriers of C₂: any one of them suffices, and they prove
the same theorem.
**Broken step.** They prove **structurally different** statements.
- **Nilpotent truncation $\mathfrak h_{\le N}=\mathfrak m^3/\mathfrak m^{N+1}$
  (T2).** As `tate-T2`:411–432 records explicitly: "The Lie algebra
  $\mathfrak m^3$ is Tate-conilpotent in the $\mathfrak m$-adic Tate
  filtration: its descending Lie powers satisfy
  $(\mathfrak m^3)^{(\geq m)}\subset\mathfrak m^{m+3}$". But — this is
  the load-bearing point — the truncation is taken inside
  $\mathfrak m^3$, *not* $\mathfrak m=\mathfrak h$. The low-degree
  sector $\mathfrak m/\mathfrak m^3=H_1\oplus H_2$ (linear translations
  and the conformal $\mathfrak{sl}_2$) is **excluded**, and explicitly
  so by `rmk:colim-does-not-recover-full` (`tate-T2`:434–461). C₂ on
  $\mathfrak m^3$ is a theorem about the conformal-$\mathfrak{sl}_2$-
  free, translation-free sector.
- **Weighted Tate regulator $\mathfrak h^w$ for exponential $w(d)=q^d$,
  $q>1$ (T1).** This *includes* the low-degree sector $H_1\oplus H_2$
  but **changes the coefficient category**: the dual $\mathfrak
  h^{\vee,w}_{\mathrm{cont}}$ is a product Mittag-Leffler module, not
  the strict continuous dual of the (product) $\mathfrak h^w$
  (`tate-T1`:184–221, "the second factor is a product coefficient
  module, not the strict continuous dual"). C₂ in the weighted regime
  is a theorem about an **enlarged coefficient category**, not about
  the original $\mathfrak h^\vee_{\mathrm{cont}}$.
- **Cofiltered-limit / regulator-independence (Wave 1's Obligation III
  reformulation).** As Wave 1's M-11 itself records, the strict
  $q\to1^+$ limit is *forbidden* by `\thm:strict-unweighted-no-go`. The
  honest statement is admissible regulator-independence: any two
  $q,q'>1$ supply canonically equivalent finite-degree local
  observables. This is a theorem about a **completion class**, not
  about $\mathfrak h$ itself.
None of these is C₂ on $\mathfrak h$ in its native topology. C₂ as
a theorem about $\mathfrak h$ does not exist; C₂ as a theorem about a
choice of admissible enlargement does, but the choice changes the
content.
**Evidence type.** counterexample (the three windows are inequivalent
as carriers); proof-gap (Wave 1's M-01 minimal heal conflated them).
**Evidence ref.** `tate-T2`:434–461 (truncation excludes $H_1\oplus H_2$);
`tate-T1`:184–221 (weighted dual is a different coefficient category);
Wave 1's M-11 (regulator-independence forbids strict limit).
**Files read.** `tate-T1`:1–300, 480–600; `tate-T2`:400–570;
`tate-T3`:30–340; main.tex 5240–5320.
**Confidence.** High.
**Blast radius.** Wave 1's M-01 split was the load-bearing heal of
the whole consolidation. If C₂ does not have a single common content
across the three admissibility windows, then the Wave-1 stable core
"Theorem C as currently stated" is split into **three** sibling
theorems, each with explicit hypothesis on the choice of
admissibility:
- **Theorem C₂(NT) — Nilpotent-truncation cotangent identity** on
  $\mathfrak m^3/\mathfrak m^{N+1}$: classical-level only; no
  $H_1\oplus H_2$.
- **Theorem C₂(W) — Weighted-Tate cotangent identity** on
  $(\mathfrak h^w,\mathfrak h^{\vee,w}_{\mathrm{cont}})$: full
  low-degree sector, but enlarged coefficient module on the cotangent
  side.
- **Theorem C₂(R) — Regulator-independent finite-window identity**:
  any two admissible weights agree on every finite Taylor window.
**Minimal heal.** Replace Wave 1's single C₂ statement by the three
named theorems above. State explicitly that none of them is "C₂ on
$\mathfrak h$ in its native topology"; the latter is a theorem about
a regulator class. Update `\rmk:E1-translation` and the claim-strength
ledger entry "CE/PV derived centre" to flag *which* admissibility is
in force at each invocation.
**Residual.** A unified statement covering all three windows
simultaneously is not a Phase-1 deliverable. The strongest unified
form is C₂(R), but it is a statement about *equivalence classes of
local observables*, not about a single Tate Lie algebra.
**Adjudication.** Valid. Strengthens Wave 1's M-01 minimal heal from
"split into C₁ and C₂" to "split into C₁ᶠʷ, C₁ᶜᵒᵐᵖ, C₂(NT), C₂(W),
C₂(R)".
**Deciding evidence.** Three named theorems with disjoint admissibility
hypotheses on the exterior face; cross-references in the claim-strength
ledger.

### W1-05 — `\lem:continuous-bar-cobar` items (3) and (4) silently use limit/colimit swap (proof-gap, M-01b sharpened)
**Severity 3. Status valid. Confidence high. Lens.** Costello primary.
**Target.** `main.tex`:3399–3415, the proof of items (3) and (4) of
`lem:continuous-bar-cobar`.
**Claim under attack.** "These finite comparisons are compatible with
enlargement of the Tate window and increase of the length cap …
Passing to the Tate limit and completing in tensor length gives the
asserted filtered quasi-isomorphism in $\Cat{TateVec}$."
**Broken step.** "Passing to the Tate limit" and "completing in tensor
length" are **two distinct limit operations** that are taken
sequentially in the proof, but the order is not stated. The two
filtrations are:
- Tate window $F^w\mathfrak g$, an inverse limit on the **outside**
  ($\mathfrak g=\varprojlim \mathfrak g_{\le w}$);
- bar/CE length $n$, a colimit (CE chains $\bigoplus_n S^n$) and an
  inverse limit (CE cochains $\prod_n$) on the **inside**.
The order of operations matters: $\varprojlim_w \varinjlim_n
(\text{finite cellular bar-cobar quasi-iso on }(\mathfrak g_{\le w},
\le n))$ is **not** generically the same as
$\varinjlim_n \varprojlim_w(\cdots)$. Mittag-Leffler exactness
(`\alpharef\ item~1`) saves the day, but only for systems with
surjective transition maps in the inverse direction; the
windowwise CE coalgebra is finite-dimensional, the transition maps
$\mathfrak g_{\le w'}\to\mathfrak g_{\le w}$ for $w'>w$ are
projections (so dual to inclusions), but the quasi-iso passes
through bar-cobar where the $\Omega C$ cobar construction is *not*
strictly compatible with truncation: $\Omega(C_{\le w})$ is not the
windowwise cap of $\Omega(C)$ unless conilpotency forces the
truncation to be exhaustive.
**Evidence type.** proof-internal step audit.
**Evidence ref.** `main.tex`:3399–3415.
**Files read.** Same; `tate-T3`:283–320 (uses Mittag-Leffler exactness
to lift windowwise qiso to global filtered qiso).
**Confidence.** High.
**Blast radius.** Item (3) of `\lem:continuous-bar-cobar` is the bar-
cobar quasi-isomorphism that is the gear of C₂. Item (4) is the PBW
filtration's separateness/completeness. Both depend on the
limit/colimit ordering. This sharpens M-01b (Wave 1 had the gap
flagged as residual): the gap is a **specific proof step** in the
manuscript, not a generic Tate-categorical concern.
**Minimal heal.** Insert in the proof of `\lem:continuous-bar-cobar`
items (3) and (4) an explicit **Mittag-Leffler dictionary** lemma:
under the Tate-conilpotency hypothesis, the inverse-system
$\{\Omega C_*^{\mathrm{CE}}(\mathfrak g_{\le w})\}_w$ is
Mittag-Leffler (transition maps are surjections of finite-
dimensional dg algebras), and therefore $\varprojlim$ commutes with
homology / commutes with $\varinjlim$ over the length cap. Cite
Roos's *Lectures on noetherian rings*, or Costello–Gwilliam Vol I
§A.5.
**Residual.** The Mittag-Leffler exactness statement is
**conditional on conilpotency**, which is exactly the hypothesis the
manuscript already makes explicit. So the heal is to factor the
proof into a separate **Mittag-Leffler dictionary** lemma so that
the dependency is visible. This subsumes Wave 1's residual A6-A7
("Mittag-Leffler resolution to a *proved lemma*"), which is also R-05.
**Adjudication.** Valid. Both M-01b and R-05 (next entry) are
healed by the same factored lemma.
**Deciding evidence.** A `lem:tate-mittag-leffler-dictionary` proved
within `tate-T3` or `tate-P1`.

### W1-06 — R-05 resolution: the "proved lemma" that `\alpharef\ item~1` should resolve to **does not yet exist**
**Severity 3. Status valid. Confidence high. Lens.** Costello primary;
Hypotheses cross-link.
**Target.** Wave 1's R-05; `\alpharef\ item~1` references in
`tate-T3`:114, 189, 250, 301–306, 514, 569; `tate-P1`:71, 102, 158, 174,
213, 268, 298, 309, 316.
**Claim under attack.** The Wave-1 ledger named R-05 ("Mittag-Leffler
resolution in T3 must be verified as a *proved* lemma (not external
axiom). Closure: explicit windowwise-Tate Mittag-Leffler verification.").
**Broken step.** I traced every `\alpharef\ item~1` in T3 and P1.
- `\alpharef` resolves to `\ref{lem:continuous-bar-cobar}`
  (`main.tex`:54 and `preamble.tex`:51).
- "`\alpharef\ item~1`" therefore means **item (1) of
  `lem:continuous-bar-cobar`**: the dualization-is-exact-and-continuous
  statement (`main.tex`:3342–3347).
- Each invocation in T3 ("Mittag-Leffler exactness in the Tate
  filtration (\alpharef\ item~1)") and in P1 ("by (A1)") **uses**
  Mittag-Leffler exactness as if it were a proved consequence of item
  (1) of `lem:continuous-bar-cobar`. But item (1) only states
  exactness of $V\mapsto V^\vee_{\mathrm{cont}}$ in the Tate
  filtration — i.e. a duality lemma — and **not** a Mittag-Leffler
  inverse-limit-exactness theorem.
- The standard Mittag-Leffler-exactness theorem in homological
  algebra (Roos 1961; Grothendieck *Tôhoku* Ch. 1) states that an
  inverse system $\{V_w\}$ with surjective transition maps satisfies
  $\varprojlim^1 V_w = 0$ and the inverse limit is exact on it.
  This is **not** the content of item (1).
- Conclusion: **the lemma being invoked does not exist as such**. The
  manuscript repeatedly invokes Mittag-Leffler exactness via
  `\alpharef\ item~1` without an actual proved Mittag-Leffler
  exactness lemma to resolve to.
**Evidence type.** missing source; line-references to invocation
sites; trace from `\alpharef` macro to its resolution.
**Evidence ref.** `preamble.tex`:51; `main.tex`:54;
`main.tex`:3342–3347 (item 1 statement); seventeen invocations in
`tate-T3` and `tate-P1` (lines listed above).
**Files read.** `commands.tex`, `preamble.tex`, `main.tex` 54 and
3340-area, `tate-T3`:1–600, `tate-P1`:1–323.
**Confidence.** High. This is a structural over-citation, not a
semantic ambiguity.
**Blast radius.** Multiple proofs in T3 and P1 invoke `\alpharef\
item~1` precisely where they need Mittag-Leffler exactness — the
limit/colimit swap of W1-05 above, the bar-cobar Quillen equivalence's
unit weak-equivalence (`tate-T3`:289–303), the windowwise-parametrix
assembly in `tate-P1`. Each invocation is morally correct (Mittag-
Leffler does apply, because the Tate transition maps are surjections
of finite-dimensional spaces) but is unsupported as cited.
**Minimal heal.** Author **`lem:tate-mittag-leffler-dictionary`** as a
single proved lemma, in `tate-T3` (or in `lem:continuous-bar-cobar`
as a new item (5)), with the precise statement:

> **Lemma (Tate Mittag-Leffler dictionary).** Let $\{V_w\}_{w\in\N}$
> be an inverse system in $\Cat{TateVec}$ such that each transition
> map $V_{w+1}\to V_w$ is a surjection of finite-dimensional pieces
> (Tate window finite-dimensional, transition surjective). Then the
> inverse system is Mittag-Leffler in the sense of Roos
> (\cite{roos-derived-functors-of-lim}, \cite{grothendieck-tohoku}*{Ch.~1}):
> $\varprojlim^{(1)}_w V_w=0$, the functor $\varprojlim_w$ is exact on
> short exact sequences of such systems, and Tate-windowed
> quasi-isomorphisms lift to filtered quasi-isomorphisms on the
> abutment.

Then redirect every `\alpharef\ item~1` to
`lem:tate-mittag-leffler-dictionary`. This closes R-05 explicitly.
**Residual.** None at the dictionary level. Each individual invocation
should be re-checked to verify the surjective-transition hypothesis;
in T3 and P1 it is satisfied because the Tate windows are
finite-dimensional and the transitions are coordinate projections.
**Adjudication.** Valid. R-05 is **healed** by inserting the named
dictionary lemma.
**Deciding evidence.** The lemma authored in `tate-T3` with citation
to Roos / Grothendieck.

### W1-07 — M-21 unitarity-table reframe: harmless — confirmed non-propagating
**Severity 1. Status invalid as an attack on Theorem-C content; valid
as confirmation of the M-21 reframe. Confidence high. Lens.** Costello.
**Target.** Wave 1's M-21 ($Z^{P_0}_{\mathrm{fact}}\simeq\mathrm{PV}$
definitional reframe; my mandate includes "verify the manuscript's
claim doesn't propagate into a stronger Costello–Gwilliam centrality
assertion elsewhere"). Note: the master ledger's M-21 in Wave 1 is
the unitarity-table issue, not the $Z^{P_0}_{\mathrm{fact}}$ reframe;
the wave-2 prompt cross-tags this. Following the prompt I treat it as
the $Z^{P_0}_{\mathrm{fact}}\simeq\mathrm{PV}$ definitional reframe of
**M-08** in the Wave-1 ledger.
**Claim under attack.** Promoting $Z^{P_0}_{\mathrm{fact}}(A)\simeq
\mathrm{PV}(A)$ to a numbered local **Definition** (Wave 1's option,
M-08 minimal heal) does not weaken the theorem's content; the
manuscript's claim does not propagate into a stronger Costello–
Gwilliam centrality assertion elsewhere.
**Broken step.** Verified. The manuscript already does this exactly,
in `main.tex`:2212–2220:

> "For a factorization algebra $\mathcal A$ on the line, write $Z_{\mathrm{fact}}(\mathcal A)$
> for the factorization algebra of $E_1$ central operations…
> $Z^{P_0}_{\mathrm{fact}}(\mathcal A)$ means the same central operations
> with the additional compatibility homotopies for the classical
> Poisson/BV bracket. **This is the local convention used below; no
> unrestricted Costello–Gwilliam central-operations theorem is imported
> into the reduced Hamiltonian proof.**" (Emphasis added.)

And in `main.tex`:2427–2438 (the proof's "Identification with the
derived $P_0$-factorization center" paragraph):

> "For the reduced constant-stalk convention used in this paper, the
> derived $P_0$-factorization center of a Poisson algebra $A$ is by
> definition represented by the Poisson cochain complex $\mathrm{PV}(A)$
> with the Lichnerowicz differential $[\pi,-]_S$. **This is the local
> Poisson-CE model; it is not an import of an unreduced Costello–
> Gwilliam central-operations theorem.**"

So the manuscript already treats $Z^{P_0}_{\mathrm{fact}}\simeq
\mathrm{PV}$ as a **local definition / convention**, not as an
imported Costello–Gwilliam theorem. The Wave-1 ledger's M-08 minimal
heal is already in place; the open question was only whether to
add a precise CPTVV citation. Verified that no later invocation
silently strengthens the convention into a global centrality claim.
The factorization-current statement (M-07/`thm:open-closed-derived-
center-factorization`) is the next-strongest claim, and it remains
restricted to the *reduced* boundary and a brane-line stalk.
**Evidence type.** verification (manuscript already encodes the
correct hedge).
**Evidence ref.** `main.tex`:2212–2220, 2427–2438; cross-checked
`thm:hamiltonian-current-center-lift` (`main.tex`:2225–2271, also
`reduced` only).
**Files read.** `main.tex` 2196–2470.
**Confidence.** High.
**Blast radius.** None. The reframe is harmless because it has
already been done.
**Minimal heal.** Optional: add **one citation** at line 2434
("Costello–Gwilliam Vol II §3.3" or "Calaque–Pantev–Toën–Vaquié–
Vezzosi, *Shifted Poisson Structures and Deformation Quantization*,
J. Topology 2017") so that the local definition is *anchored* in the
external literature without claiming the import. This is cosmetic.
**Residual.** None.
**Adjudication.** Confirmed non-propagating. The reframe was
already in the manuscript; Wave 1's M-08 is closed by the existing
text. The remaining edit is editorial.
**Deciding evidence.** No further evidence needed; the manuscript
already states it correctly.

---

## §2. Stable-core update

The Wave-1 stable core was: A, B, C₁, C₂ (admissibility-explicit), D,
E, F, G, after the proposed heals. The C₁/C₂ split was the load-bearing
heal of M-01.

**Wave-2-W1 verdict.** The C₁/C₂ split *does* close M-01, **but the
split is finer than Wave 1 stated**. The corrected split is:

- **C₁ᶠʷ — Finite-word generator identity.** Hypothesis-free
  (W1-01). Proved at the level of every CE word of bounded total
  length; uses only `prop:hamiltonian-polyvector-reduction` /
  `lem:linear-poisson-schouten` + structure-constant identification.
- **C₁ᶜᵒᵐᵖ — Completed-algebra cochain identity on the formal
  symplectic disk.** Filtration-tame on this Lie algebra; hypothesis
  needs explicit Tate-symmetric filtration + inverse-map continuity
  (W1-02). For the formal disk both hold; for an arbitrary Tate Lie
  algebra C₁ᶜᵒᵐᵖ requires the symmetric-filtration hypothesis. The
  Leibniz extension (W1-03) is a short induction with explicit signs.
- **C₂(NT) — Nilpotent-truncation cotangent identity** on
  $\mathfrak m^3/\mathfrak m^{N+1}$. Excludes $H_1\oplus H_2$ (the
  conformal $\mathfrak{sl}_2$ direction).
- **C₂(W) — Weighted-Tate cotangent identity** on
  $(\mathfrak h^w,\mathfrak h^{\vee,w}_{\mathrm{cont}})$. Includes
  $H_1\oplus H_2$ but uses an enlarged coefficient module (the
  product Mittag-Leffler dual, not the strict continuous dual).
- **C₂(R) — Regulator-independent finite-window identity.** Any
  two admissible weights $q,q'>1$ give canonically equivalent
  finite-degree local observables. Wave 1's M-11 admissible-only
  reformulation. The strict $q\to1^+$ limit remains forbidden.

These five named theorems replace the Wave-1 single C₁/C₂ split.
Crucially, **none** of them is "Theorem C on $\mathfrak h$ in its
native unweighted topology"; that statement remains outside the
stable core. The original Theorem C's content is **distributed**
across the admissibility classes; the choice of admissibility is the
hypothesis on the exterior face.

**Stable core, Wave-2-W1 amended.**
- A (Dirac brane probe). Stable.
- B (Stable Hamiltonian trace). Stable, with PBW special-fibre
  shadow disclaimer.
- **C₁ᶠʷ. Stable, hypothesis-free.**
- **C₁ᶜᵒᵐᵖ. Stable on the formal symplectic disk; abstract case
  needs explicit symmetric-filtration hypothesis.**
- **C₂(NT). Stable on $\mathfrak m^3/\mathfrak m^{N+1}$ only.**
- **C₂(W). Stable in the weighted Tate coefficient category.**
- **C₂(R). Stable on regulator-independent finite-window
  observables.**
- D (Matlis-dual realization). Stable, after M-05/M-06.
- E (Factorization-current). Stable, after M-23/M-24/M-16/M-17, with
  Weiss descent (M-14) residual.
- F (algebraic Moyal target). Stable; F$'$ conditional.
- G (U(1)/Capelli). Stable, after M-09/M-10/M-12.

The factor-of-two refinement is in C₁ and C₂. The rest of the Wave-1
stable core is preserved.

---

## §3. Heal proposals (smallest first)

### Tier 1 — Statement-only edits to the Wave-1 ledger and plan

**WP1-1.** In `main.tex`:2322–2349 (statement of `thm:open-closed-
derived-center`), insert before the displayed equality:

> "Suppose moreover that the Tate filtration on $\mathfrak h$ is
> *symmetric* in the sense that the natural filtration on
> $\widehat{\mathbf S}_{\mathrm{Tate}}(\mathfrak h)\widehat\otimes
> \widehat\Lambda(\theta^I)$ matches the filtration on
> $C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak g)$ under
> $u_I\leftrightarrow O_I, c^I\leftrightarrow\theta^I$."

This makes the inverse-map continuity (W1-02) an exterior-face
hypothesis. For the formal symplectic disk this hypothesis is verified
in `cor:derived-center-formal-disk` by inspection of the structure
constants.

**WP1-2.** In `main.tex`:2496–2503 (proof of
`cor:derived-center-formal-disk`), expand the hedge "no lower-central
conilpotence of the full Hamiltonian algebra is used" into:

> "The structure constants $C^L_{(a,b),(c,d)}=(ad-bc)\delta_{L=(a+c-1,b+d-1)}$
> are filtration-decreasing in the $\mathfrak m$-adic Tate filtration:
> the bracket of two generators of total Hamiltonian degree $a+b+c+d$
> lands in degree $a+b+c+d-2$, a *strictly smaller* Tate window. Hence
> $d_{\mathrm{CE}}, d_\pi, \Phi$ and $\Phi^{-1}$ are all
> filtration-preserving and continuous; the symmetric-filtration
> hypothesis of `thm:open-closed-derived-center` holds, and no
> lower-central conilpotence on $\mathfrak h$ is invoked."

This sharpens the corollary's existing hedge into an explicit
verification.

### Tier 2 — Authoring a single proved lemma (closes R-05 and W1-05)

**WP2-1.** In `tate-T3` (after `\stmt:tate-model-envelope`), author:

> **Lemma (Tate Mittag-Leffler dictionary).**
> \label{lem:tate-mittag-leffler-dictionary}
> Let $\{V_w\}_{w\in\N}$ be an inverse system in
> $\Cat{TateChain}_{\geq 0}^{\mathrm{adm}}$ with finite-dimensional
> transition kernels and surjective transition maps
> $\pi_{w'\to w}:V_{w'}\to V_w$ for $w'\geq w$. Then:
> (1) $\varprojlim^{(1)}_w V_w = 0$;
> (2) The functor $\varprojlim_w$ is exact on short exact sequences of
> such systems;
> (3) Tate-windowwise quasi-isomorphisms lift to filtered
> quasi-isomorphisms on $\varprojlim_w V_w$.
> *Proof.* Roos \cite{roos-derived-functors-of-lim};
> Grothendieck \cite{grothendieck-tohoku}*{Ch.~1}; the surjective-
> transition hypothesis is the classical Mittag-Leffler condition.
> The lift in (3) uses two-out-of-three on the long exact sequence
> of the filtered tower. $\square$

Then **redirect every `\alpharef\ item~1`** in `tate-T3` and `tate-P1`
to `lem:tate-mittag-leffler-dictionary`.

**WP2-2.** In the proof of `lem:continuous-bar-cobar` items (3) and
(4) (`main.tex`:3399–3426), insert one sentence after "Passing to the
Tate limit and completing in tensor length…":

> "The order of the two limits — Tate window $\varprojlim_w$ outside
> and bar-cobar length $\varinjlim_n$ inside — commutes by
> `lem:tate-mittag-leffler-dictionary`(2)–(3); each bar-cobar
> windowwise quasi-isomorphism is finite-dimensional and the
> transitions $\mathfrak g_{\le w'}\to\mathfrak g_{\le w}$ are
> surjections, so the inverse system has surjective transitions and
> the inverse limit is exact."

### Tier 3 — Renaming the C₂ statements

**WP3-1.** Replace Wave 1's M-01 minimal heal with:

> "Split Theorem C into:
> - **Theorem C₁ᶠʷ** (finite-word generator identity, hypothesis-free).
> - **Theorem C₁ᶜᵒᵐᵖ** (completed cochain identity, with the
>   *symmetric-filtration hypothesis* on $\mathfrak g$).
> - **Theorem C₂(NT)** (nilpotent-truncation extension on $\mathfrak m^3$).
> - **Theorem C₂(W)** (weighted-Tate extension on
>   $(\mathfrak h^w,\mathfrak h^{\vee,w}_{\mathrm{cont}})$).
> - **Theorem C₂(R)** (regulator-independent finite-window extension)."

**WP3-2.** Update the claim-strength ledger entry "CE/PV derived
centre" (`claim-strength-ledger.tex`:38–44) to record which
sub-statement is in force at each cross-reference, and to flag the
admissibility hypothesis.

**WP3-3.** Update `theorem-lanes.tex` Lane 3 (`thm:lane-ce-pv-center`)
to name C₁ᶠʷ, C₁ᶜᵒᵐᵖ, C₂(NT), C₂(W), C₂(R) in the "exact
hypotheses" block.

### Tier 4 — Sign-convention appendix authoring

**WP4-1.** Author `lem:tate-leibniz-extension-cu` in the sign-convention
appendix (Wave 1 plan §6 item 8): explicit length-2 and length-3
verifications of $\Phi(d_{\mathrm{CE}}\cdot)=d_\pi\Phi$ on the four
word types, with explicit Koszul signs. Closes A1-09 (Wave 1 residual).

---

## §4. Residuals after Wave-2-W1

- **R-W1-01 (from W1-02).** For the abstract Theorem C₁ᶜᵒᵐᵖ on
  arbitrary Tate Lie algebras, the symmetric-filtration / inverse-
  continuity hypothesis is genuinely additional. Closure is at
  application sites, not at the theorem statement itself.
- **R-W1-02 (from W1-04).** A unified C₂ statement covering all three
  admissibility windows simultaneously is not a Phase-1 deliverable.
  The strongest unified form is C₂(R), but it is a statement about
  equivalence classes, not about a single Lie algebra.
- **R-05 (Wave-1 residual) — healed.** Resolved by
  `lem:tate-mittag-leffler-dictionary` (W1-06).
- **R-01 (Wave-1, from M-01) — partially healed.** Tate-categorical
  bar-cobar argument that survives perfectness in $\Cat{TateVec}$
  remains open as an unweighted statement. The C₂(R) reformulation
  + WP2-1 dictionary closes the *manuscript-internal* gap; an
  abstract Tate-perfect statement is still a Phase-4 problem.
- **R-W1-03 (new, from W1-04).** The M-21 / M-08 reframe is
  confirmed non-propagating; one editorial citation (CPTVV or
  Costello–Gwilliam Vol II) is the closure if desired.

---

## §5. Convergence verdict

The Wave-1 C₁/C₂ split *does* close M-01, **once it is sharpened to
the five-way split (C₁ᶠʷ, C₁ᶜᵒᵐᵖ, C₂(NT), C₂(W), C₂(R)) and once
the Mittag-Leffler dictionary lemma is authored to back the
`\alpharef\ item~1` invocations**. With these two further
refinements:

- M-01 is healed at the level of admissibility-explicit theorem
  statements (Wave 1's intent), but with five sub-theorems instead of
  two.
- A1-08 (continuity of inverse) is healed for the formal disk via
  WP1-2 explicit verification; for abstract Tate Lie algebras it
  becomes an exterior-face hypothesis (WP1-1).
- A1-09 (Leibniz extension) is healed by an explicit length-2/3
  inductive verification (WP4-1).
- R-05 (`\alpharef\ item~1` Mittag-Leffler residual) is healed by
  `lem:tate-mittag-leffler-dictionary` (WP2-1).
- M-08 / M-21 (definitional reframe of $Z^{P_0}_{\mathrm{fact}}\simeq
  \mathrm{PV}$) is **already in the manuscript**; the reframe does
  not weaken theorem content and does not propagate elsewhere; one
  optional citation closes the cosmetic loose end (WP1-2 cosmetic).

The single most important architectural insight: **the Wave-1 plan's
M-01 minimal heal under-described the structure**. The three
admissibility windows (T2, T1, regulator-independence) are
inequivalent carriers; promoting them to three named sibling theorems
makes the manuscript honest at the level of which Lie algebra is in
force where.

The single most important new technical insight: **`\alpharef\ item~1`
does not currently resolve to a proved Mittag-Leffler exactness
lemma**; item (1) of `lem:continuous-bar-cobar` is a duality lemma,
not an inverse-limit-exactness lemma. The fix is one new lemma
authored once and referenced everywhere.

**Posture against Wave 1.** Wave-1's stable-core declaration is
preserved at the level of theorems-A-through-G; Wave-2-W1 sharpens
the C-block from a 2-way split to a 5-way split, identifies the
Mittag-Leffler dictionary as a missing proved lemma, and confirms
M-21's reframe is harmless and already encoded.

End of attack.
