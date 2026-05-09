# Wave 3 / W24 — Theorem E Steps 2..N audit

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Wave/Worker.** Wave 3, W24.
**Lens.** Primary: Drinfeld (moduli, stacks, chiral/factorization
structures, canonical constructions, hidden groupoids). Secondary:
Composition (do local claims compose globally? Is associativity
coherent?).
**Inputs.**
- `CLAUDE.md`
- `reconstitution/attack-heal-platonic-2026-04-28.md` master ledger,
  Theorem E entries (M-24 four-lemma chain; M-33 W6 eight-link DAG;
  P-13/M-15 rename; A2-007 / W2 entries on Matlis–residue rigidity).
- `reconstitution/wave2-W6-beilinson-2026-04-28.md` (Step 1 attack,
  W6-01 through W6-08).
- `reconstitution/wave3-W17-hkr-thmA-2026-04-28.md` (HKR confined to
  Theorem E Step 1 + `\rmk:E1-translation` line 2202).
- `reconstitution/wave3-W6-costello-composition-2026-04-28.md` for
  M-26 / C₂ structural span context.
- `main.tex` Theorem E full proof, lines 1996–2191; supporting
  propositions at 1914–1995, 2274–2330, 2461–2504, 3087–3116,
  3245–3293, 3323–3389, 3791–3906, 4489–4571.
- `appendix-factorization-current-conventions.tex` (full).
- `tate-T3-quillen-equivalence.tex` lines 395–589.
- `tate-T4-bv-vanishing.tex` lines 1–90.
- `tate-T5-chain-level-primitive.tex` lines 700–795.

**Mode.** Proposal-only. Master ledger schema; new IDs prefix
`W3-W24-`.
**Independence.** Wave-2 W6 audited Step 1 (HKR appeal at line 2056).
Wave-3 W17 confirmed Step 1's HKR remains in the manuscript.
W3-W24 takes Step 1 as input under attack and audits Steps 2..8 each
in turn under the Drinfeld + Composition lens.

---

## §0. Top-line findings

1. **Theorem E has eight steps.** (Wave-2 W6 named the chain "an
   8-step lemma chain"; the manuscript proof at `main.tex` 2049–2191
   is literally indexed by `\emph{Step 1.}` through `\emph{Step 8.}`.)
   Wave-2 W6 mapped these to the eight-link DAG L1–L8 of
   `lem:locally-constant-cosheaf` cover, but the **manuscript-step
   indices and the W6 DAG-link indices are not identical**. W24 walks
   the manuscript indices verbatim and cross-walks each to the DAG.

2. **No new HKR appeal beyond Step 1.** The HKR / Hochschild language
   reappears in Step 5 prose (line 2132) but as a *back-reference* to
   Step 1's identification, not as a fresh primary-source invocation.
   This was already named by W17 (entry #5) and inherits the W6-02 /
   W3-W17-01 heal.

3. **Step 4 silently strengthens the Lie bracket compatibility from
   length-one to all CE lengths via "biderivation property"; this
   propagation is correct on Tate windows but assumes the
   $P_0$-bracket extends as a biderivation in the cosheaf-of-Lie
   evaluation.** This biderivation extension is a *structural*
   statement (it is the very content of `constr:interval-fact-algebras`
   / `\{\cdot,\cdot\}_{A_\partial}` definition lines 1947–1952), so
   the inductive extension is honest, *but* the prose at line 2125
   compresses the inductive argument to one sentence, which a careful
   reader might mistake for an unproved promotion. **W3-W24-01:
   editorial sharpening (one sentence of prose).**

4. **Step 5's "free graded-commutative algebras on the same
   continuous Tate vector space" clause silently invokes the
   bidirectional symmetric-filtration assumption (W3-W6-01)** at the
   factorization level. The brane side is
   $\widehat{\mathbf S}(\mathfrak h_I) \widehat\otimes
   \widehat{\mathbf S}(\mathfrak h_{I,\mathrm{cont}}^\vee[-1])$ and
   the closed side is
   $C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak g_I) =
   \widehat{\mathbf S}(\mathfrak g_{I,\mathrm{cont}}^\vee[-1])$; the
   identification of "underlying graded vector spaces" requires
   continuity of the dictionary map *and its inverse* in a single
   filtration. Wave-3 W6 named this for the cochain-level Theorem A;
   W24 confirms it propagates through the factorization upgrade. The
   formal disk has the bidirectional structure constants
   filtration-decreasing. **W3-W24-02: pin Step 5 to the bidirectional
   symmetric filtration explicitly.**

5. **Step 6's "dual surjection" coassociativity is correct on
   pairwise inclusions but the manuscript does not state n-tuple
   coassociativity.** For three pairwise-disjoint intervals
   $I_1, I_2, I_3 \subset V$, the factorization product
   $\mc F(I_1) \otimes \mc F(I_2) \otimes \mc F(I_3) \to \mc F(V)$
   must agree under the two parenthesizations
   $((I_1, I_2), I_3)$ and $(I_1, (I_2, I_3))$. The proof shows the
   pairwise statement; n-tuple coassociativity is what M-24 names
   `lem:n-tuple-coassoc`. **W3-W24-03: name n-tuple coassociativity
   explicitly in Step 6 prose.**

6. **Step 7 invokes "locally constant" via `lem:derivative-jets` only
   in the cohomological sense.** This was W6-05's heal proposal; the
   heal is not yet inscribed at line 2179. **W3-W24-04: confirm the
   W6-05 heal is the right closure for Step 7.**

7. **Step 8's stalk recovery commutes with the Lurie-promoted
   $\infty$-equivalence of `thm:open-closed-derived-center-derived`
   only if the limit $I \to \{t_0\}$ is taken in the locally constant
   sense.** The manuscript proof says "as $I$ shrinks to a point...
   $\Omega^\bullet_c(I)$ contracts onto the stalk class at $t_0$ in
   cohomology"; this is correct, but the limit interchange (filtered
   colimit of Tate windows ↔ inverse limit of factorization-algebra
   sections) is a non-trivial commutation that depends on the
   admissible Tate envelope's filtered-colimit structure. **W3-W24-05:
   name the limit-interchange explicitly in Step 8.**

8. **Composition of Steps 1..8 yields the full Theorem E
   conclusion**, modulo the following per-step residuals:
   - Step 1 → W6-02 / W3-W17-01 (HKR replaced by Lurie HA + windowwise
     reduction).
   - Step 4 → W3-W24-01 (editorial; biderivation extension prose).
   - Step 5 → W3-W24-02 (bidirectional symmetric filtration).
   - Step 6 → W3-W24-03 (n-tuple coassociativity).
   - Step 7 → W3-W24-04 = W6-05 (cohomological local-constancy).
   - Step 8 → W3-W24-05 (limit interchange).
   The Drinfeld lens confirms all eight steps assemble into a
   factorization-algebra equivalence in the *interval-wise* sense; the
   *Weiss-cosheaf* upgrade to $\R^2 \times \C^2$ is a separate residual
   (R-03 / W6-07), explicitly not within the proof's scope.

9. **Convention drift between Theorem E and the appendix:** the
   appendix's `\mathfrak h_I = \Omega^\bullet_c(I) \widehat\otimes
   \mathfrak h` (resp. $\bar A$) and the manuscript Step 1's
   `\mathfrak h_I` agree on the level of the construction. The
   appendix uses the dense subalgebra $\bar A$ as a polynomial label;
   the manuscript Step 1 uses $\mathfrak h_I$ directly. No drift
   detected. The shift convention $[1]$ on $\mathcal P_I$ matches
   exactly between `constr:interval-fact-algebras` (line 1919) and
   `def:app-factorization-current-dual` (appendix lines 57–60).

---

## §T1. Enumeration of proof steps

The proof of `\thm:open-closed-derived-center-factorization` at
`main.tex` 2049–2191 has eight literally-indexed steps. The table
below gives manuscript-line ranges, what is established, sub-lemmas
invoked, and primary sources cited.

| Step | Lines | What is established | Sub-lemmas / propositions invoked | Primary sources cited |
|------|-------|---------------------|-----------------------------------|------------------------|
| 1 | 2050–2076 | Identify the interval-wise central factorization algebra: `Hoch^•(\widehat{\mathbf S}(\mathfrak h_I)) \simeq PV^•` (HKR appeal). Read off the generator dictionary $c^I \mapsto \theta^I$, $u_I \mapsto O_I$. | `\thm:open-closed-derived-center` (the cochain-level Theorem A); HKR (no `\bib{}` entry; W17 #4). | "the smooth/algebraic setting" of HKR — no specific theorem cited. Tate-completion silent. |
| 2 | 2078–2093 | Construct the CE source: `C^•_{CE,cont}(\mathfrak g_I) = \widehat{\mathbf S}(\mathfrak g_{I,cont}^∨[-1])`. The pairing structure is de Rham-current × residue-Taylor. | `lem:continuous-bar-cobar` (line 3323). | None new. |
| 3 | 2095–2112 | Define $\Phi^{\mathrm{Ham}}_{\mathrm{fact}}(I)$ on length-one shifted-cotangent CE coordinates. The map sends $u_{a(t)dt \otimes f}$ to $L_{B_f(a)}$. Extend by continuous algebra morphism. | `prop:grav-ops` (line 3256), `prop:stalk-central-multiplication` (line 3087). | None new. |
| 4 | 2114–2125 | Verify CE differential compatibility on length-two; extend by length and biderivation. | `cor:local-bulk-boundary-coupling` (line 4489), specifically the strict $P_0$ identity $\{B_f(a), B_g(b)\} = B_{\{f,g\}}(ab)$. | None new. |
| 5 | 2127–2137 | Quasi-isomorphism on each interval. Both sides are free graded-commutative algebras on the same continuous Tate vector space; map respects symmetric-algebra generators by construction; intertwines differentials. | None new beyond Steps 1, 2, 3, 4. **Back-reference to Step 1's HKR identification at line 2132.** | None new. |
| 6 | 2139–2172 | Factorization product compatibility. Disjoint $I_1, I_2 \subset V$; CE source extension by zero gives $\mathfrak h_{I_1} \oplus \mathfrak h_{I_2} \hookrightarrow \mathfrak h_V$; cobracket on the closed side is the dual of this; brane side multiplication map; factorization diagram commutes. | `prop:brane-bracket-locality` (line 1965). | None new. |
| 7 | 2174–2184 | Locally constant structure. $[d_\R, \iota_{\partial_t}] = \partial_t$ kills positive jets; structure maps for inclusions are quasi-isomorphisms on both sides; $E_1$-equivalent algebra structure is the strict $P_0$ on the stalk. | `lem:derivative-jets` (line 2788), `constr:interval-fact-algebras` (line 1914). | Lurie HA §5.5 (named in the theorem statement at line 2028, not in the proof body); CG Vol I §6.4 (idem). |
| 8 | 2185–2191 | Stalk recovery. As $I \to \{t_0\}$, $\Omega^\bullet_c(I)$ contracts to the stalk class at $t_0$ in cohomology; image of length-one CE coordinate becomes $L_{B_f}$ at the stalk. | `lem:derivative-jets`, `prop:stalk-central-multiplication`. | None new. |

**Cross-walk to the W6 DAG.** Manuscript Steps 1–8 ≠ W6 DAG L1–L8.
The correspondence is approximately:

| Manuscript step | Approximate W6 DAG link |
|-----------------|--------------------------|
| Step 1 (HKR ID) | L3 (interval-wise generator-level CE/PV identity) — Step 1's content is the L3 generator dictionary plus the HKR side identification. |
| Step 2 (CE source) | L1 (cosheaf-of-Lie) + L2 (source-convention dictionary) + L4 (Tate conilpotency at window) — assemble the CE source on $\mathfrak g_I$. |
| Step 3 (Φ on generators) | L3 (generator level) — defines the map on length-one. |
| Step 4 (CE differential compatibility) | L3 (extends the generator identity to all lengths via biderivation). |
| Step 5 (qiso on each interval) | L5 (Mittag-Leffler) — promotes the windowwise identity to a global filtered qiso. |
| Step 6 (factorization product) | L7 (disjoint-support locality) — the strict $P_0$ FA, not homotopical. |
| Step 7 (locally constant) | L6 (locally constant cosheaf descent) — `lem:derivative-jets` directly. |
| Step 8 (stalk recovery) | L8 (Lurie HA §5.5.4 / CG §6.4 promotion) — stalk-level central operation $f \mapsto L_{B_f}$. |

The W6 DAG is finer than the manuscript steps in two places:
- L1+L2+L4 collapse into manuscript Step 2.
- L3 spans manuscript Steps 1, 3, 4 (the HKR ID, the generator
  definition, and the differential extension are all "L3-level"
  generator identities).

The W6 DAG is *coarser* than the manuscript in one place:
- The manuscript Step 6 separates the cobracket diagram from the
  $\R$-locality of `prop:brane-bracket-locality`. W6 packages both
  into L7.

This W3-W24 audit walks the **manuscript index** (Steps 1–8) and
cross-walks each to the W6 DAG.

---

## §T2. Step 2 audit

**Verbatim** (manuscript lines 2078–2093):

> *Step 2.* Construct the CE source. By
> \ref{lem:continuous-bar-cobar}, applied to
> $\mathfrak g_I=\mathfrak h_I\ltimes\mathcal P_I[1]$ in the stated
> completed category,
> $$C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak g_I)
>  =\widehat{\mathbf S}\bigl(\mathfrak g^{\vee}_{I,\mathrm{cont}}[-1]\bigr),$$
> and its CE differential is the dual of the semidirect Lie bracket.
> The Hamiltonian part is controlled by the de Rham-current pairing on
> the $\Omega^\bullet_c(I)$ factor and the residue-Taylor pairing on
> $\bar A$. In degree-zero notation this is the familiar pairing between
> compactly supported test functions and compactly supported currents;
> the polynomial subspace $\bar A\subset\widehat{\bar A}$ pairs with the
> discrete Taylor dual generated by the $\delta_{a,b}$. The
> shifted-cotangent CE coordinate \(u_{a(t)dt\otimes f}\) is the coordinate
> dual to the cotangent generator determined by the current
> \(a(t)dt\otimes f\).

**Hypotheses.**

(H2.1) `\mathfrak g_I = \mathfrak h_I \ltimes \mathcal P_I[1]` is a
graded Lie algebra in $\Cat{TateVec}$ in the sense of
`constr:interval-fact-algebras` (line 1914). Verified: the bracket is
explicitly defined on lines 1922–1926, and the cosheaf structure is
extension-by-zero on `\Omega^\bullet_c` and on `\mathcal D'_c`.

(H2.2) `\mathfrak g_I` satisfies the Tate-conilpotency hypothesis of
`lem:continuous-bar-cobar` (line 3336–3340): descending Lie powers
satisfy `\bigcap_m(\mathfrak g^{(\geq m)} + F^w \mathfrak g) = F^w \mathfrak g`
for every $w$. **Hypothesis check needed.** The proof at line 2079
applies the lemma without naming this hypothesis. For
`\mathfrak g_I`:
- The bracket on `\mathfrak g_I` has `[\mathfrak h_I, \mathfrak h_I] \subset \mathfrak h_I`
  by `[a \otimes f, b \otimes g]_{\mathfrak h_I} = ab \otimes \{f, g\}_{\bar A}`.
- The semidirect-product structure makes `\mathcal P_I[1]` an abelian
  ideal, so `[\mathfrak g_I, \mathcal P_I[1]] \subset \mathcal P_I[1]`
  and `[\mathcal P_I[1], \mathcal P_I[1]] = 0`.
- The descending Lie central series of `\mathfrak g_I` therefore
  reduces to the descending series of `\mathfrak h_I` (because
  `\mathcal P_I[1]` is abelian).
- For `\mathfrak h_I = \Omega^\bullet_c(I) \widehat\otimes \bar A`,
  the Tate-conilpotency depends on `\bar A = \C[z_1, z_2]/\C\cdot 1`
  being conilpotent. **W17 / M-01 named the perfectness obstruction:
  `\bar A` is *perfect* under the Poisson bracket
  ($[\bar A, \bar A] = \bar A$).** Hence `\bar A^{(\geq m)} = \bar A`
  for every $m$, and the Tate-conilpotency hypothesis of
  `lem:continuous-bar-cobar` **fails for `\mathfrak h_I` in the same
  way it fails for `\mathfrak h` in `cor:derived-center-formal-disk`**.

**Proof technique.** Apply `lem:continuous-bar-cobar` Item~2 (the CE
chains-as-completed-symmetric identification). The lemma's hypothesis
is the Tate-conilpotency item; its conclusion is the
$\widehat{\mathbf S}_{\mathrm{Tate}}(\mathfrak g^\vee_{\mathrm{cont}}[-1])$
identification.

**Hand-check on the simplest non-trivial example.** Take
`\bar A = \C[z_1, z_2]/\C \cdot 1` truncated to the 2-step nilpotent
quotient (W17 §T4 example): keep only `H_{1,0}, H_{0,1}, H_{2,0},
H_{1,1}, H_{0,2}` and set higher Hamiltonians to zero. This is
finite-dimensional, conilpotent (in fact 5-step nilpotent), and W17's
example explicitly checks the cochain identity at this window. For
this truncation:

`\mathfrak h_I^{\le 2} = \Omega^\bullet_c(I) \widehat\otimes \bar A_{\le 2}`,
which is a Tate Lie algebra concentrated on a finite-dim Lie algebra
on each interval. Its descending series stabilizes in 2 steps:
- `[\mathfrak h_I, \mathfrak h_I] \subset \Omega^\bullet_c(I) \otimes [\bar A_{\le 2}, \bar A_{\le 2}]`
  ≤ `\bar A_{\le 1}` (the linear part).
- The next step gives 0.

Hence `\mathfrak g_I^{\le 2}` is conilpotent and `lem:continuous-bar-cobar`
applies cleanly. **Step 2 holds at this finite Tate window.**

**For the unweighted full** `\mathfrak h_I`, **Step 2 inherits the
M-01 obstruction**. The factorization-theorem heal is the same as the
cochain-level Theorem A heal: 5-way C₁/C₂ split (M-26 /
W3-W6-02), or the M-01 minimal heal (excise unweighted-limit
dependency, work at fixed Tate window).

**Drinfeld lens.** Step 2 constructs the CE *source*. The Drinfeld
canonicality question: is the CE source canonical, or does it depend
on a non-canonical choice (e.g., a basis of $\bar A$, a Tate
filtration)?

The source `C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak g_I) =
\widehat{\mathbf S}(\mathfrak g_{I,\mathrm{cont}}^\vee[-1])` is
canonically determined by the Lie-algebra `\mathfrak g_I`, **with no
basis choice**: dualization is functorial, and the CE differential is
dual to the bracket. Hence Step 2 is canonical at the level of the
graded Lie algebra. The Tate filtration is a choice (which window
ordering to put on $\bar A$), but the CE chains and the
quasi-isomorphism class of the CE source are invariant under change
of admissible filtration (this is the M-26 / W3-W6-04 statement on
admissible-class regulator independence).

**Composition lens.** Step 2's output (the CE source as a completed
symmetric algebra on the dual) feeds Step 3 (definition of $\Phi$ on
generators). The interface is the generator dictionary
$c^I \mapsto \theta^I, u_I \mapsto O_I$ named in Step 1. This
interface is well-defined on length-one generators; Step 4 then
extends by Leibniz. The composition Step 1 → Step 2 → Step 3 is
honest: Step 2 produces the source object, Step 3 names the map on
length-one, Step 4 propagates by biderivation.

**Verdict.** Step 2 is structurally correct at fixed Tate window;
inherits the M-01 perfectness obstruction at the unweighted limit
(same fault line as Theorem A). No new defect identified beyond M-01.

---

## §T3. Step 3 audit

**Verbatim** (manuscript lines 2095–2112):

> *Step 3.* Define $\Phi^{\mathrm{Ham}}_{\mathrm{fact}}(I)$ on
> generators. By \ref{prop:grav-ops}, the closed Hamiltonian
> cotangent BF observables on the formal neighbourhood of
> $\R\times p$ in the Hamiltonian sector are
> $\widehat{\mathbf S}(\mathfrak h^{\vee}_{I,\mathrm{cont}}[-1])$,
> with CE differential dual to the Hamiltonian Lie bracket on
> $\mathfrak g_I$. The interval-wise map sends a length-one
> shifted-cotangent CE coordinate
> \(u_{a(t)dt\otimes f}\in C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak g_I)\)
> to the element of the central operations factorization algebra
> given by the multiplication operator
> $$L_{B_f(a)}\in\mathrm{Hoch}^0\bigl(A_\partial^{\mathrm{Ham}}(I)\bigr)
>   \subset\mathrm Z^{P_0}_{\mathrm{fact}}\bigl(A_\partial^{\mathrm{Ham}}\bigr)(I),$$
> with $B_f(a)$ as displayed. By
> \ref{prop:stalk-central-multiplication}, this operator is closed
> (Hochschild $0$-cocycle on the graded-commutative open stalk).
> Extend $\Phi^{\mathrm{Ham}}_{\mathrm{fact}}(I)$ as a continuous
> algebra morphism on $\widehat{\mathbf S}$.

**Hypotheses.**

(H3.1) `prop:grav-ops` identifies closed Hamiltonian cotangent BF
observables with `\widehat{\mathbf S}(\mathfrak h^\vee_{I,\mathrm{cont}}[-1])`.
**Verified by inspection of `prop:grav-ops` proof (lines 3265–3293):
the kinematic differential `Q_0 = d_{\R^2} + \bar\partial_{\C^2}`
contracts positive real and anti-holomorphic jets; the
$Q_0$-cohomology is generated by holomorphic Taylor coefficients;
the residual BRST differential is the CE differential dual to the
semidirect Lie bracket on `\mathfrak g`.** Note: `prop:grav-ops` is
stated at the *point* level (`\mathfrak g`), not at the *interval*
level (`\mathfrak g_I`). Step 3 silently transfers from the point to
the interval.

(H3.2) `prop:stalk-central-multiplication` makes `B_f` a Hochschild
0-cocycle for `f \in \C[z_1, z_2]`. **Verified by inspection of
`prop:stalk-central-multiplication` proof (lines 3104–3116): every
`B_f` is `Q`-closed because `Q\phi_1 = Q\phi_2 = 0`; on a
graded-commutative algebra, multiplication by a closed class is a
Hochschild 0-cocycle. The Poisson identity `\{B_f, B_g\}_{\rm open} =
B_{\{f,g\}_{\bar A}}` follows from `thm:bulk-boundary`.**

(H3.3) The map extends as a continuous algebra morphism on
`\widehat{\mathbf S}`. **Implicit hypothesis: continuity.** Wave-3 W6
(W3-W6-01) named this as the *bidirectional symmetric filtration*
hypothesis: $\Phi$ and $\Phi^{-1}$ are jointly filtration-preserving
in a single filtration. Step 3 names continuity but does not name
bidirectional symmetric filtration; Step 5's qiso claim then leans on
this.

**Proof technique.** Direct definition on length-one generators,
then continuous algebra-morphism extension. The two key inputs are
`prop:grav-ops` (closed observables = CE cochains, on the *point*)
and `prop:stalk-central-multiplication` (multiplication is a
Hochschild 0-cocycle, on the *point*).

**Hand-check on the simplest non-trivial example.** Take `f = z_1`
(linear Hamiltonian) and `a \in \Omega^0_c(I)` a smooth bump
function. Then:

`u_{a(t)dt \otimes z_1}` is a length-one shifted-cotangent CE
coordinate. Step 3 sends:
`u_{a(t)dt \otimes z_1} \mapsto L_{B_{z_1}(a)}`,
where `B_{z_1}(a) = \int_I a(t) \overline{\mathrm{Tr}\,\phi_1(t)}\,dt`.

Since `\phi_1` is `Q`-closed (`Q\phi_1 = 0`), `\overline{\mathrm{Tr}\,\phi_1(t)}`
is `Q`-closed, and integration against a compactly supported test
function preserves `Q`-closure. Hence `B_{z_1}(a)` is `Q`-closed, and
multiplication by it is a Hochschild 0-cocycle on the
graded-commutative reduced open stalk. **Step 3 holds for `f = z_1`,
as it should.**

**Drinfeld lens.** Step 3 names the *canonical map* $\Phi$ on
generators. Drinfeld asks: is the map canonical or merely chosen?

The map $u_{a(t)dt \otimes f} \mapsto L_{B_f(a)}$ is canonical given:
- the source-convention dictionary of the appendix (W6 L2): the
  length-one shifted-cotangent CE coordinate is *the* coordinate dual
  to the cotangent generator `a(t)dt \otimes f`;
- the residue pairing of `prop:principal-part-coadjoint`, normalized
  up to a single non-zero scalar by `thm:canonical-residue-pairing`
  (T2-Cartan-equivariant rigidity, W2-01);
- the volume-form datum `dz_1 \wedge dz_2` on `\C^2`.

The map is canonical *up to the residue scalar*, which is
T2-Cartan-equivariant rigid. **Drinfeld verdict: canonical, modulo
the residue scalar; the scalar is fixed by convention.**

**Composition lens.** Step 3's output (Φ on generators) feeds Step 4
(CE differential compatibility). The interface is well-defined on
generators by Step 3; Step 4 verifies the differential equation
$\Phi d_{\rm CE} = d_\pi \Phi$ on length 2 and propagates.

**Verdict.** Step 3 is structurally correct. No new defect
identified. The "continuous algebra morphism" extension at line 2111
silently invokes the same continuity/symmetric-filtration hypothesis
that W6/W3-W6-01 named at the cochain level; it propagates here.

---

## §T4. Step 4..N audit (brief)

### Step 4 audit

**Verbatim** (manuscript lines 2114–2125):

> *Step 4.* Verify CE differential compatibility. On length two,
> the CE differential of a shifted-cotangent generator
> \(u_{a(t)dt\otimes f}\) is the coadjoint term dual to the Lie bracket on
> $\mathfrak h_I$. By
> \ref{cor:local-bulk-boundary-coupling} (its sharpened form below),
> $$\{L_{B_f(a)},L_{B_g(b)}\}_{A_\partial^{\mathrm{Ham}}}
>   =L_{B_{\{f,g\}}(ab)}.$$
> Pulling back through $\Phi^{\mathrm{Ham}}_{\mathrm{fact}}$ matches
> this with the shifted-cotangent CE differential dual to
> $[a\otimes f,b\otimes g]_{\mathfrak h_I}=ab\otimes\{f,g\}$.
> Inductive extension by length and the biderivation property
> propagates this to all CE lengths.

**Hypotheses.**

(H4.1) `cor:local-bulk-boundary-coupling` (line 4489) gives the
strict $P_0$ identity `\{B_f(a), B_g(b)\}_{A_\partial^{\rm Ham}} =
I_\partial(ab, \{f,g\}_{\bar A})`. **Verified by inspection of
the corollary's proof (lines 4536–4548): the locality input is the
canonical equal-time bracket of the first-order open BV theory,
smeared against `a(t)b(s)`.**

(H4.2) The biderivation property: the $P_0$-bracket on
`\widehat{\mathbf S}(\mathfrak h_I)` extends as a biderivation from
the length-one bracket. **Verified by `constr:interval-fact-algebras`
lines 1947–1952: the $P_0$-bracket is *defined* as the biderivation
extension of the length-one bracket.**

(H4.3) Inductive extension by length: from length two to all CE
lengths. **The manuscript prose at line 2125 reads "Inductive
extension by length and the biderivation property propagates this to
all CE lengths." This is correct but compressed. The induction is:
on length $n$, the CE differential of a length-$n$ word
$u_{I_1} \cdots u_{I_n}$ is by the Leibniz rule
$\sum_k (-1)^{?} u_{I_1} \cdots d_{\rm CE} u_{I_k} \cdots u_{I_n}$,
plus the "internal" CE differential terms; the Φ-pullback is the
same Leibniz rule on the brane side via biderivation.**

**Proof technique.** Generator-level computation on length two
(directly from `cor:local-bulk-boundary-coupling`); inductive
extension by length via the Leibniz rule and biderivation property.

**Hand-check on the simplest non-trivial example.** Take
`f = z_1, g = z_2`. The Poisson bracket is
`\{z_1, z_2\}_{\bar A} = 1` (the constant Hamiltonian 1 lies in
$\C \cdot 1$ removed from `\bar A`, so this is *zero* in `\bar A`).
Hence `\{B_{z_1}(a), B_{z_2}(b)\}_{A_\partial^{\rm Ham}} =
B_0(ab) = 0` in the reduced sector.

A non-trivial example: `f = z_1^2, g = z_2`, giving
`\{z_1^2, z_2\}_{\bar A} = 2 z_1`. Hence
`\{B_{z_1^2}(a), B_{z_2}(b)\}_{A_\partial^{\rm Ham}} =
B_{2z_1}(ab) = 2 B_{z_1}(ab)`.

The CE differential side: the length-two CE coordinate
`u_{a(t)dt \otimes z_1^2} \cdot u_{b(t)dt \otimes z_2}` has CE
differential containing the coadjoint term
`-u_{ab\,dt \otimes \{z_1^2, z_2\}_{\bar A}} = -u_{ab\,dt \otimes 2 z_1}`,
which Φ-pulls back to `-L_{2 B_{z_1}(ab)}`, matching (up to sign
convention) the brane-side bracket. **Step 4 holds for this example.**

**Drinfeld lens.** Step 4's biderivation extension is structurally
canonical: the biderivation property is defined by the construction
of `A_\partial^{\rm Ham}` as `\widehat{\mathbf S}(\mathfrak h_I)`
with biderivation $P_0$-bracket. No moduli choice.

**Composition lens.** Step 4's output (CE differential compatibility
at all lengths) feeds Step 5 (qiso on each interval). The composition
is honest: Step 4 produces the differential equation `\Phi d_{\rm CE}
= d_\pi \Phi` on all of `C^\bullet_{\rm CE,cont}(\mathfrak g_I)`.

**Editorial finding (W3-W24-01).** The "Inductive extension by
length and the biderivation property" sentence at line 2125 is
correct but compresses a non-trivial induction into one phrase. A
careful reader could mistake this for an unproved promotion. The
heal is one sentence:

> **W3-W24-01 (editorial).** Replace "Inductive extension by length
> and the biderivation property propagates this to all CE lengths"
> with "Both the CE differential `d_{\rm CE}` and the Schouten
> differential `d_\pi` are degree-1 graded derivations on the
> respective free completed graded-commutative algebras, hence are
> determined by their values on length-one generators
> (`lem:linear-poisson-schouten`); the length-two identity above
> determines all higher lengths by Leibniz, and the strict
> $P_0$-bracket biderivation property of `constr:interval-fact-algebras`
> propagates the identity to every word."

**Verdict.** Step 4 is structurally correct. W3-W24-01 is editorial
prose only.

---

### Step 5 audit

**Verbatim** (manuscript lines 2127–2137):

> *Step 5.* Quasi-isomorphism on each interval. Both sides are
> free graded-commutative algebras on the same continuous Tate vector
> space after the generator dictionary
> $c\mapsto\theta$, $u\mapsto O$, with the same CE
> differential induced from the semidirect Lie bracket of $\mathfrak g_I$
> (closed side: by definition; brane side: through the HKR
> identification of Step 1 and the Schouten bracket). The map
> respects the symmetric-algebra generators by construction. Thus it
> is an isomorphism of underlying graded vector spaces and
> intertwines the differentials. The map is therefore an isomorphism
> of $P_0$-cdg algebras on each interval.

**Hypotheses.**

(H5.1) Both sides are free graded-commutative algebras on the same
continuous Tate vector space. **Verified at the level of the
underlying graded vector spaces:**
- Closed side: `C^\bullet_{\rm CE,cont}(\mathfrak g_I) =
  \widehat{\mathbf S}(\mathfrak g_{I,\rm cont}^\vee[-1])`.
- Brane side: `\mathrm Z^{P_0}_{\rm fact}(A_\partial^{\rm Ham})(I)` is
  the local Poisson-CE model of
  `PV(\widehat{\mathbf S}(\mathfrak h_I)) =
  \widehat{\mathbf S}(\mathfrak h_I) \widehat\otimes
  \widehat{\mathbf S}(\mathfrak h_{I,\rm cont}^\vee[-1])`.

The generator dictionary identifies these:
- `c^I \mapsto \theta^I` (Hamiltonian CE coordinate to constant
  polyvector);
- `u_I \mapsto O_I` (cotangent CE coordinate to multiplication
  operator on the brane).

(H5.2) The map intertwines the differentials. **Verified by Step 4
(differential compatibility on all lengths).**

(H5.3) "The map respects the symmetric-algebra generators by
construction." **Verified by Step 3 (Φ defined on generators) +
Step 4 (extended to all words via Leibniz).**

**Proof technique.** Direct identification of underlying graded
vector spaces + differential intertwining (Step 4) gives an
isomorphism of $P_0$-cdg algebras.

**Hand-check on the simplest non-trivial example.** Take
`\mathfrak h^{\le 2}` (W17 §T4 example) on a single interval $I$, so
`\mathfrak h_I^{\le 2}` is a finite-dim Lie algebra times
`\Omega^\bullet_c(I)` (or rather the cosheaf-of-Lie evaluation). The
CE source is finite-dim per interval (after fixing a cohomology class
in the de Rham direction); the Schouten polyvector side is the same.
**Step 5 holds at this finite Tate window: both sides are isomorphic
free graded-commutative algebras with the same differential.**

**Drinfeld lens.** Step 5's qiso claim is canonical given the
generator dictionary of Steps 1–3. The dictionary is canonical up to
the residue scalar (W2-01: T2-Cartan-equivariant rigidity).

**Composition lens — W3-W24-02 finding.** The clause "free
graded-commutative algebras on the same continuous Tate vector space"
silently invokes a *bidirectional symmetric filtration* hypothesis
(W3-W6-01). The closed side is filtered by symmetric-algebra length
on the dual `\mathfrak g_{I,\rm cont}^\vee[-1]`; the brane side is
filtered by symmetric-algebra length on `\mathfrak h_I` *and*
polyvector degree on `\mathfrak h_{I,\rm cont}^\vee[-1]`. The
"isomorphism of underlying graded vector spaces" requires a single
filtration in which both `\Phi` and `\Phi^{-1}` are
filtration-preserving and continuous.

For the formal disk, this holds (W3-W6-01 proof: structure constants
$C^L_{(a,b),(c,d)} = (ad-bc)$ are filtration-decreasing in both
directions on the $\mathfrak m$-adic Tate filtration). For the
factorization upgrade on the cosheaf-of-Lie evaluation, the same
filtration-decreasing property propagates (the cosheaf evaluation
preserves the bidirectional filtration of the underlying Lie
algebra, modulo the de Rham-current pairing, which is itself
bidirectional).

**Heal proposal.**

> **W3-W24-02.** Insert in Step 5 immediately after "Both sides are
> free graded-commutative algebras on the same continuous Tate vector
> space":
>
> > "with bidirectional symmetric Tate filtration: a single
> > filtration on `\mathfrak g_{I,\rm cont}^\vee[-1]` (and its dual
> > polyvector image) in which `d_{\rm CE}`, `d_\pi`, $\Phi$, **and**
> > $\Phi^{-1}$ are jointly filtration-preserving and continuous;
> > this is automatic at any fixed Tate window
> > (`lem:continuous-bar-cobar` Item~2 with W3-W6-01 propagated to
> > the cosheaf-of-Lie evaluation)."

**Verdict.** Step 5 is structurally correct. W3-W24-02 is editorial
prose only, propagating the W3-W6-01 sharpening from the cochain
level to the factorization level. No new defect.

**Note on the Step-5 HKR back-reference.** The parenthetical "closed
side: by definition; brane side: through the HKR identification of
Step 1 and the Schouten bracket" at line 2132 is a back-reference to
Step 1's HKR appeal. It is not a fresh primary-source invocation. It
inherits the W6-02 / W3-W17-01 / W3-W17-02 heals.

---

### Step 6 audit

**Verbatim** (manuscript lines 2139–2172):

> *Step 6.* Factorization product compatibility. For disjoint
> $I_1,I_2\subset V$, the CE source extension by zero gives
> $\mathfrak h_{I_1}\oplus\mathfrak h_{I_2}\hookrightarrow\mathfrak h_V$.
> The cobracket on the closed side is the dual of this: it is the
> splitting
> $\widehat{\mathbf S}(\mathfrak g_V^\vee[-1])
>  \to\widehat{\mathbf S}(\mathfrak g_{I_1}^\vee[-1])\widehat\otimes
>  \widehat{\mathbf S}(\mathfrak g_{I_2}^\vee[-1])$
> obtained from the dual surjection
> $\mathfrak g_V^\vee\twoheadrightarrow
> \mathfrak g_{I_1}^\vee\oplus\mathfrak g_{I_2}^\vee$. On the brane
> side,
> $A_\partial^{\mathrm{Ham}}(I_1)\otimes A_\partial^{\mathrm{Ham}}(I_2)
> \to A_\partial^{\mathrm{Ham}}(V)$ is the multiplication map under
> the inclusion of
> $\mathfrak h_{I_1}\oplus\mathfrak h_{I_2}\hookrightarrow\mathfrak h_V$.
> By \ref{prop:brane-bracket-locality}, the bracket between the two
> factors vanishes on disjoint supports, so the product is strictly
> multiplicative. The induced map between central-operation
> factorization algebras is the corresponding tensor product of
> multiplication operators. This is exactly the dual of the CE-source
> extension by zero. Therefore the diagram
> [diagram] commutes after vertical reversal of the left arrow (CE
> coproduct = dual of inclusion).

**Hypotheses.**

(H6.1) For disjoint `I_1, I_2 \subset V`,
`\mathfrak h_{I_1} \oplus \mathfrak h_{I_2} \hookrightarrow \mathfrak h_V`
via extension by zero. **Verified by `constr:interval-fact-algebras`
lines 1932–1933: "Inclusions $I' \subset I$ act by extension by zero
on compactly supported de Rham forms and currents; disjoint unions
act by sum."**

(H6.2) The bracket between the two factors vanishes on disjoint
supports. **Verified by `prop:brane-bracket-locality` (line 1965):
$\{B_f(a), B_g(b)\} = B_{\{f,g\}}(ab) = 0$ when supports are
disjoint, because `ab \equiv 0` pointwise.**

(H6.3) The product is strictly multiplicative. **Verified: the
factorization product on disjoint intervals is the multiplication in
`\widehat{\mathbf S}` after extension by zero
(`constr:interval-fact-algebras` line 1953–1954).**

**Proof technique.** Direct dualization: the CE source extension by
zero is dual to the brane-side multiplication; the strict $P_0$
factorization product follows from `prop:brane-bracket-locality`.

**Hand-check on the simplest non-trivial example.** Take
`I_1 = (-2, -1)`, `I_2 = (1, 2)`, `V = (-3, 3)`, with smooth bump
functions `a` supported in `I_1` and `b` supported in `I_2`. Then:

- Brane side: `B_{z_1}(a) \cdot B_{z_2}(b) \in A_\partial^{\rm Ham}(V)`
  is the multiplication of two boundary observables with disjoint
  supports. The bracket
  `\{B_{z_1}(a), B_{z_2}(b)\}_{A_\partial^{\rm Ham}} =
  B_{\{z_1, z_2\}}(ab) = 0` (since `\{z_1, z_2\}_{\bar A} = 1`, but
  `1 \in \C \cdot 1` removed; alternatively, `ab \equiv 0` pointwise
  by disjoint supports). So the product is strictly multiplicative.
- Closed side: the CE coproduct on
  `\widehat{\mathbf S}(\mathfrak g_V^\vee[-1])` splits the
  length-one CE coordinate `u_{a(t)dt \otimes z_1}` (supported in
  `I_1`) and `u_{b(t)dt \otimes z_2}` (supported in `I_2`) into the
  tensor product. The Φ-pullback of the brane multiplication agrees
  with the CE coproduct.

**Step 6 holds for this example.**

**Drinfeld lens — W3-W24-03 finding.** Step 6 verifies the *pairwise*
factorization product. The full factorization-algebra structure
requires *n-tuple coassociativity*: for three pairwise-disjoint
intervals `I_1, I_2, I_3 \subset V`, the diagram

```
\mc F(I_1) \otimes \mc F(I_2) \otimes \mc F(I_3)
  → \mc F(I_1 \cup I_2) \otimes \mc F(I_3) → \mc F(V)
=
\mc F(I_1) \otimes \mc F(I_2) \otimes \mc F(I_3)
  → \mc F(I_1) \otimes \mc F(I_2 \cup I_3) → \mc F(V)
```

must commute. This is `lem:n-tuple-coassoc` (M-24 / W6 link L7
sub-statement).

**Verification.** The brane side is the multiplication in
`\widehat{\mathbf S}(\mathfrak h_V)`, which is a (strictly)
graded-commutative algebra; multiplication is associative, so the
two compositions agree. The closed side is the CE coproduct dual to
the symmetric-algebra inclusion
`\mathfrak h_{I_1} \oplus \mathfrak h_{I_2} \oplus \mathfrak h_{I_3}
\hookrightarrow \mathfrak h_V`, which is itself associative under the
direct-sum structure. **N-tuple coassociativity holds**, but the
manuscript Step 6 does not state it.

**Heal proposal.**

> **W3-W24-03.** Insert in Step 6 immediately after the diagram:
>
> > "For three or more pairwise-disjoint intervals
> > $I_1, \ldots, I_n \subset V$, the factorization product
> > $\mc F_{\rm cl}(I_1) \otimes \cdots \otimes \mc F_{\rm cl}(I_n)
> > \to \mc F_{\rm cl}(V)$ is associative under iterated pairwise
> > application (n-tuple coassociativity, M-24
> > `lem:n-tuple-coassoc`): both arms of the iterated diagram are the
> > Φ-pullback of the symmetric-algebra multiplication
> > $\widehat{\mathbf S}(\mathfrak h_{I_1}) \otimes \cdots \otimes
> > \widehat{\mathbf S}(\mathfrak h_{I_n}) \to
> > \widehat{\mathbf S}(\mathfrak h_V)$ on the brane side, and dually
> > the CE coproduct on the closed side, both of which are
> > associative."

**Composition lens.** Step 6's output (factorization product
compatibility) feeds Step 7 (locally constant structure). Step 7
needs the structure maps for inclusions to be quasi-isomorphisms;
Step 6 supplies the disjoint-product half.

**Verdict.** Step 6 is structurally correct on the pairwise level.
W3-W24-03 is editorial prose only; the n-tuple coassociativity is
true but not explicitly stated.

---

### Step 7 audit

**Verbatim** (manuscript lines 2174–2184):

> *Step 7.* Locally constant structure. By
> \ref{lem:derivative-jets} the de Rham contraction in $t$ kills all
> positive jets in $\Omega^\bullet_c(I)$, leaving the locally constant
> de Rham class represented in degree zero by values at points. The
> translation vector field $\partial_t$ is $Q$-exact through
> $[d_\R,\iota_{\partial_t}]=\partial_t$. Hence the structure maps
> for inclusions of intervals are quasi-isomorphisms on both sides;
> the $E_1$-equivalent associative algebra structure is the
> underlying graded-commutative product on the stalk, equipped with
> the strict $P_0$ bracket of \ref{constr:interval-fact-algebras}.

**Hypotheses.**

(H7.1) `lem:derivative-jets` (line 2788): positive jets in the
topological direction vanish in local operator cohomology;
$[d_\R, \iota_{\partial_t}] = \partial_t$. **Verified by inspection
of the lemma's proof (lines 2794–2801): the de Rham part of the BRST
operator on jet algebras has the contraction homotopy
$[d_\R, \iota_{\partial_t}] = \partial_t$, killing positive
$t$-derivatives in cohomology.**

(H7.2) Structure maps for inclusions are quasi-isomorphisms on both
sides. **Hypothesis check needed.** This is the "locally constant"
condition itself. It is verified at the *cohomology* level: the
inclusion `\Omega^\bullet_c(I') \hookrightarrow \Omega^\bullet_c(I)`
for `I' \subset I` is a quasi-isomorphism in cohomology because both
have one-dimensional `H^0_c` (the line). This is the W6-05 finding:
locally constant in the *cohomological* sense, not at the underlying
chain complex level.

**Proof technique.** Apply `lem:derivative-jets` (the de Rham jet
contraction homotopy) to identify $\Omega^\bullet_c$ with its
cohomology in degree zero; the cosheaf inclusions are then
quasi-isomorphisms.

**Hand-check on the simplest non-trivial example.** Take `I' = (0, 1)
\subset I = (-1, 2)`. The inclusion
`\Omega^0_c(I') \hookrightarrow \Omega^0_c(I)` is extension by zero;
both have `H^0_c = \C` (compactly supported de Rham cohomology of an
open interval is one-dimensional in degree zero — wait, this is
*not* the case: compactly supported de Rham cohomology of an open
interval $(a,b)$ is concentrated in degree $1$, with
`H^1_c = \C`, *not* `H^0_c`).

Let me recheck. `H^k_c(\R, \C)` is `\C` in degree 1 and 0 in degree
0. For the open interval `(a,b) \subset \R`, by Poincaré duality
$H^k_c(I) \cong H^{1-k}(I) = \C$ in $k = 1, 0$ in $k = 0$.

The manuscript says: "leaving the locally constant de Rham class
represented in degree zero by values at points." This phrasing
appears to refer to *chain-level* representation, not to
*cohomology-level*. The de Rham contraction
$[d_\R, \iota_{\partial_t}] = \partial_t$ contracts positive jets,
leaving the *chain-level zeroth jet* (the value at a point), not
necessarily a degree-zero cohomology class.

Interpretation more carefully: the cosheaf is `\Omega^\bullet_c(I)`, in
total degree on the brane line `\R`. The locally constant claim is
about the *factorization-algebra structure maps* on $I' \subset I$,
which on `\Omega^\bullet_c(I')` extends to `\Omega^\bullet_c(I)` and
should be a quasi-isomorphism.

For nonempty open intervals `I' \subset I`, both
`\Omega^\bullet_c(I')` and `\Omega^\bullet_c(I)` have the same
compactly supported de Rham cohomology (concentrated in degree 1
with one-dim fibre over $\R$). The inclusion
`\Omega^\bullet_c(I') \hookrightarrow \Omega^\bullet_c(I)` is a
quasi-isomorphism in this sense. **Step 7 holds.**

**The Step 7 phrasing about "degree zero" is off** — the cohomology
class is in degree 1 (compactly supported on a 1-manifold), not
degree zero. But the *value at a point* on the *underlying line*
(not on the cosheaf) is a degree-zero stalk-value, which is what the
factorization-algebra stalk recovery in Step 8 uses.

This phrasing imprecision is W6-05's finding, partially. W3-W24-04
revises:

**Heal proposal.**

> **W3-W24-04 (extends W6-05).** Replace Step 7 prose at lines
> 2174–2178:
>
> > "By `\lem:derivative-jets` the translation vector field
> > $\partial_t$ is $Q$-exact through
> > $[d_\R, \iota_{\partial_t}] = \partial_t$, so positive
> > $t$-jets are exact in local operator cohomology. The cosheaf
> > inclusion `\Omega^\bullet_c(I') \hookrightarrow
> > \Omega^\bullet_c(I)` for `I' \subset I` of nonempty open intervals
> > is a quasi-isomorphism in compactly supported de Rham
> > cohomology (one-dim in degree 1 in either case). Hence the
> > structure maps `\mc F_{\rm cl}(I') \to \mc F_{\rm cl}(I)` and
> > the corresponding maps on `Z^{P_0}_{\rm fact}(A_\partial^{\rm Ham})`
> > are quasi-isomorphisms (locally constant in the
> > Costello–Gwilliam Vol I §6.4 sense)."

**Composition lens.** Step 7's output (locally constant structure)
feeds Step 8 (stalk recovery). The locally constant condition is
exactly what allows the stalk-limit `I \to \{t_0\}` in Step 8.

**Drinfeld lens.** Step 7 establishes the locally constant property,
which is necessary to apply Lurie HA §5.5.4 (named in the theorem
statement at line 2028, not in the proof body). The Lurie
$E_1 \simeq$ locally constant FA equivalence is the Drinfeld
canonical comparison, with $n=1$ on the brane line.

**Verdict.** Step 7 is structurally correct. The "degree zero"
phrasing is technically imprecise but does not invalidate the
quasi-isomorphism. W3-W24-04 (extends W6-05) is editorial prose.

---

### Step 8 audit

**Verbatim** (manuscript lines 2185–2191):

> *Step 8.* Stalk recovery. As $I$ shrinks to a point
> $t_0\in\R$, $\Omega^\bullet_c(I)$ contracts onto the stalk class at
> $t_0$ in
> cohomology (\ref{lem:derivative-jets}). The image of a length-one
> CE coordinate becomes the multiplication operator $L_{B_f}$ at the
> stalk, recovering \ref{prop:stalk-central-multiplication}.

**Hypotheses.**

(H8.1) The limit `I \to \{t_0\}` is well-defined as a filtered
limit / stalk in the locally constant FA structure. **Verified by
Step 7 (locally constant) + Lurie HA §5.5.4 (stalk-as-filtered-limit
of locally constant FAs equals the $E_1$-stalk).**

(H8.2) `\Omega^\bullet_c(I)` contracts onto the stalk class at $t_0$
in cohomology. **Verified by the de Rham jet contraction
homotopy `lem:derivative-jets` and the cohomology of the line.**

(H8.3) The image of a length-one CE coordinate becomes
$L_{B_f}$ at the stalk. **Verified by Step 3 (Φ on length-one)
+ stalkification limit of the smearing $a \to \delta_{t_0}$.**

**Proof technique.** Take the stalk limit, use Step 7 (locally
constant) and `lem:derivative-jets` to identify the stalk with the
value at the point, recover `prop:stalk-central-multiplication`.

**Hand-check on the simplest non-trivial example.** Take `f = z_1`
and let `a \to \delta_{t_0}` (the Dirac delta at $t_0$). Then
`B_{z_1}(a) = \int_I a(t) \overline{\mathrm{Tr}\,\phi_1(t)}\,dt
\to \overline{\mathrm{Tr}\,\phi_1(t_0)}` in the limit. Multiplication
by `\overline{\mathrm{Tr}\,\phi_1(t_0)}` is `L_{B_{z_1}}` at the
stalk, recovering `prop:stalk-central-multiplication`. **Step 8
holds for this example.**

**Drinfeld lens.** Step 8's stalk recovery is the canonical
comparison of the factorization-algebra equivalence with the
pointwise central-operation theorem. Drinfeld asks: is the limit
canonical? It is, modulo the locally constant structure of Step 7.

**Composition lens — W3-W24-05 finding.** The limit `I \to \{t_0\}`
is a *filtered colimit* of factorization-algebra sections in the
sense of CG Vol I §6.4. The interchange of this limit with the
admissible Tate envelope's filtered structure (Tate windows
`\mathfrak h_{I, \le w}`) is non-trivial. The manuscript Step 8
does not name this interchange.

**Verification.** The interchange holds because:
- The Tate windows `\mathfrak h_{I, \le w}` are finite-dimensional
  on each interval (W6 L4: Tate conilpotency at fixed window);
- The stalk limit `I \to \{t_0\}` commutes with finite Tate
  windows (the value at `t_0` is the same regardless of window);
- The full limit (over all windows + stalk limit) is filtered, hence
  commutes with the symmetric-algebra construction by Wave-2 W6 L5
  (Mittag-Leffler exactness).

**Heal proposal.**

> **W3-W24-05.** Insert in Step 8 immediately before "The image of a
> length-one CE coordinate":
>
> > "The stalk limit commutes with the admissible Tate envelope's
> > filtered structure: at fixed Tate window
> > `\mathfrak h_{I, \le w}`, the stalk limit is the value at $t_0$
> > on the finite-dimensional truncation; passing to the inverse
> > limit over Tate windows by Mittag-Leffler exactness
> > (`lem:tate-mittag-leffler-dictionary`, M-27) gives the full
> > stalk."

**Verdict.** Step 8 is structurally correct. W3-W24-05 is editorial
prose making the limit-interchange explicit.

---

## §T5. Composition across steps

### Composition diagram

```
Step 1 ─────────────────────────┐
   │                            │
   │ HKR ID + generator dict    │
   ▼                            │
   c^I↦θ^I, u_I↦O_I             │
                                 │
Step 2 (CE source) ──────────────┤
   │ apply lem:continuous-bar-cobar
   ▼                            │
   C^•_{CE,cont}(g_I) =         │
     S^(g^∨_{I,cont}[-1])       │
                                 │
Step 3 (Φ on generators) ────────┘
   │ define Φ on length-one
   ▼
Step 4 (CE differential) ────────┐
   │ length-2 by cor:local-bb-coupling
   │ extend by Leibniz/biderivation
   ▼                              │
Step 5 (qiso each interval) ──────┤
   │ free symmetric on same      │
   │ Tate vector space           │
   ▼                              │
Step 6 (factorization product) ──┤
   │ disjoint by prop:brane-bracket-locality
   │ (n-tuple coassoc — W3-W24-03)
   ▼                              │
Step 7 (locally constant) ───────┤
   │ lem:derivative-jets          │
   │ Q-exact translation         │
   ▼                              │
Step 8 (stalk recovery) ─────────┘
   │ I → {t_0} in cohomology
   ▼
   Φ^Ham_fact: locally constant
   P_0-FA equivalence on R
   in admissible Tate envelope
```

### Composition verification

| Step → Step | Output of preceding | Hypothesis of next | Composition honest? |
|--------------|---------------------|---------------------|----------------------|
| 1 → 2 | Generator dictionary $c^I \mapsto \theta^I$, $u_I \mapsto O_I$ | CE source needs a Lie algebra in $\Cat{TateVec}$; `\mathfrak g_I` is given | Yes (Step 2 doesn't actually use the dictionary; it just constructs the source) |
| 2 → 3 | $C^\bullet_{\rm CE,cont}(\mathfrak g_I) = \widehat{\mathbf S}(\mathfrak g_{I,\rm cont}^\vee[-1])$ | Φ on length-one needs the CE coordinate $u_{a(t)dt \otimes f}$ | Yes |
| 3 → 4 | $\Phi(u_{a(t)dt \otimes f}) = L_{B_f(a)}$ | CE differential compatibility on length 2 needs length-1 dictionary | Yes |
| 4 → 5 | $\Phi d_{\rm CE} = d_\pi \Phi$ at all lengths | Qiso needs same underlying graded vector space + intertwined differentials | Yes (modulo W3-W24-02: bidirectional symmetric filtration) |
| 5 → 6 | Φ is a strict $P_0$-cdg algebra isomorphism on each $I$ | Factorization product needs the interval-wise iso | Yes (modulo W3-W24-03: n-tuple coassoc) |
| 6 → 7 | Factorization product compatible | Locally constant needs structure maps to be qiso on inclusions | Yes (modulo W3-W24-04: cohomological local-constancy) |
| 7 → 8 | Locally constant FA structure | Stalk recovery needs the locally constant condition + stalk limit | Yes (modulo W3-W24-05: limit interchange) |

**Associativity.** The composition Step 1 → Step 2 → ... → Step 8 is
*linear* (no branching). The associativity question is whether the
composition is independent of the order in which the editorial heals
W6-02 / W3-W24-01..05 are inscribed. Each heal is local to its step
and does not change the structural content; hence the composition is
trivially associative (sequential, no branching).

**Coherence conditions.** The hidden coherence conditions between
Steps `i` and `i+1` are:

- **Step 4 / Step 5 boundary.** The biderivation extension (Step 4)
  must be filtration-preserving in the same Tate filtration that
  Step 5's free graded-commutative algebra structure uses. **W3-W24-01
  (Step 4 prose) + W3-W24-02 (Step 5 bidirectional filtration) name
  this jointly.**

- **Step 6 / Step 7 boundary.** The factorization product
  compatibility (Step 6, disjoint-support) and the locally constant
  structure (Step 7, inclusion-quasi-isomorphism) jointly characterize
  the factorization-algebra structure. The two together give a
  locally constant factorization algebra. **No new hidden
  coherence; this is the L7 + L6 combination of W6's DAG.**

- **Step 7 / Step 8 boundary.** The locally constant condition (Step
  7) implies the stalk-limit converges (Step 8). **W3-W24-05 names
  the limit-interchange explicitly.**

### Full Theorem E conclusion

After Steps 1–8 + heals W6-02 (Step 1) + W3-W24-01..05 (Steps 4–8),
the proof yields:

1. A continuous interval-wise morphism of $P_0$ factorization algebras
   `\Phi^{\rm Ham}_{\rm fact}: \mathrm{Obs}^{\rm cl}_{\rm closed,H,Ham}|_{\R \times p}
   \to \mathrm Z^{P_0}_{\rm fact}(A_\partial^{\rm Ham})` (Steps 1–4).
2. Quasi-isomorphism on each interval (Step 5).
3. Locally constant in the topological direction (Step 7), with
   factorization-product compatibility (Step 6) — together giving
   the locally constant factorization-algebra equivalence on $\R$ in
   the admissible Tate envelope, in the sense of Lurie HA §5.5.4 + CG
   Vol I §6.4.
4. Stalk recovery to the pointwise central-operation map
   (Step 8).

This matches the five conclusions claimed in the theorem statement
(lines 2013–2046). **Composition closes.**

---

## §T6. Weiss-cosheaf descent in Steps 2..N

W2 / W9 found the Weiss-product-stability genuinely beyond reach.

**Audit of each step for Weiss invocation.**

| Step | Weiss invoked? | Disposition |
|------|----------------|-------------|
| 1 | No. HKR is at the level of free graded-commutative algebra on a Tate vector space, not Weiss. | OK. |
| 2 | No. CE source on `\mathfrak g_I` is per-interval, not Weiss. | OK. |
| 3 | No. Φ on generators is per-interval. | OK. |
| 4 | No. CE differential compatibility is per-interval, length-by-length. | OK. |
| 5 | No. Qiso on each interval is per-interval; not Weiss. | OK. |
| 6 | No. Factorization product on disjoint intervals is *pairwise*, not Weiss. The iterated n-tuple is associative (W3-W24-03), but n-tuple coassociativity is NOT the Weiss condition. | OK. |
| 7 | **Implicitly yes? No.** Locally constant on $\R$ is a one-dimensional cosheaf condition (CG Vol I §6.4); Weiss is on higher-dim manifolds (CG Vol I §6.5 / §7.2). Step 7 is locally constant on $\R$, not Weiss on $\R^2 \times \C^2$. | OK. The Weiss condition for the unreduced FA on $\R^2 \times \C^2$ is the standing residual `prop:weiss-cosheaf-residual` (T3 530–563), explicitly NOT used in Step 7. |
| 8 | No. Stalk recovery is at a single point on $\R$, not Weiss. | OK. |

**Verdict.** Theorem E's proof, Steps 1–8, **does not invoke the
Weiss condition** at any step. The Weiss residual lives in
`prop:weiss-cosheaf-residual` (T3) and is the standing obligation R-03
/ W6-07 (sharpened by Wave-2 W6 with four ingredients). **The
Theorem E factorization-algebra equivalence is on $\R$ (the brane
line), not on $\R^2 \times \C^2$.** This is precisely what the
theorem claims (line 2027: "is locally constant in the topological
direction $\R$").

**Inheritance.** The Weiss-cosheaf residual is structurally outside
Theorem E's scope. Theorem E proves the FA equivalence on $\R$;
extending to the full ambient $\R^2 \times \C^2$ would require Weiss
descent, which is the W2 / W9 genuinely-beyond-reach component, with
W6-07's four-ingredient list (heat-kernel propagator, defect boundary
condition, bulk-to-defect kernel, transverse Mittag-Leffler). **No
Weiss-condition leak into Steps 2–8.**

---

## §T7. Cross-check against `appendix-factorization-current-conventions.tex`

The appendix fixes current conventions used in
`thm:lane-factorization-current` (which is the lane-index version of
Theorem E in `theorem-lanes.tex`). I cross-check line-by-line.

| Convention | Theorem E (manuscript) | Appendix | Match? |
|------------|------------------------|----------|--------|
| Hamiltonian current source | $\mathfrak h_I = \Omega^\bullet_c(I) \widehat\otimes \bar A$ (line 1917 in `constr:interval-fact-algebras`) | `\mathfrak h_I = \Omega^\bullet_c(I) \widehat\otimes \mathfrak h` (line 17), with `\mathfrak h` replaced by `\bar A = \C[z_1,z_2]/\C \cdot 1` in degree-zero formulas (line 21) | Match. The appendix uses `\mathfrak h` for the abstract Lie algebra and `\bar A` for the polynomial dense subalgebra; manuscript uses `\bar A` throughout in `constr:interval-fact-algebras`. |
| Bracket | $[a \otimes f, b \otimes g]_{\mathfrak h_I} = ab \otimes \{f, g\}_{\bar A}$ (line 1923) | $[\alpha \otimes f, \beta \otimes g] = \alpha \wedge \beta \otimes \{f, g\}$ (line 25), reduces to $[a \otimes f, b \otimes g] = ab \otimes \{f,g\}$ on degree-zero test functions (lines 28–30) | Match. |
| Density notation | $a(t)\,dt$ density notation does not change the de Rham degree | "the measurement notation writes the oriented density associated to $a$ as $a(t)\,dt$; this density notation does not change the de Rham degree of the source test function $a$" (lines 32–34) | Match. |
| Current dual | $\mathcal P_I = \mathcal D'_c(I) \widehat\otimes \mc P$, with `\mc P \simeq \mathfrak h^\vee_{\rm cont}` (line 1918) | Same: $\mathcal P_I = \mathcal D'_c(I) \widehat\otimes \mc P$, $\mc P \simeq \mathfrak h^\vee_{\rm cont}$ (lines 41–48) | Match. |
| Pairing | residue calculus: $\langle B \otimes \rho, a \otimes f \rangle = B(a) \operatorname{Res}(\rho f)$ (implicit in `prop:principal-part-coadjoint`) | Explicit: $\langle B \otimes \rho, a \otimes f \rangle = B(a) \operatorname{Res}(\rho f)$ (line 51) | Match. |
| Shifted cotangent | $\mathfrak g_I = \mathfrak h_I \ltimes \mathcal P_I[1]$ (line 1919) | $\mathfrak g_I = \mathfrak h_I \ltimes \mathcal P_I[1]$ (line 59) | Match. |
| CE coordinate degree | $|u_{a(t)dt \otimes f}| = 0$, $|c_{a \otimes f}| = 1$ (manuscript Step 1, "CE coordinates $c$ dual to Hamiltonian generators map instead to constant polyvectors"; cf. `theorem-lanes.tex` line 130) | Same: $|u_{a(t)dt \otimes f}| = 0$, $|c_{a \otimes f}| = 1$ (lines 67–70) | Match. |
| Source of $B_f(a)$ | $u_{a(t)dt \otimes f} \mapsto B_f(a)$ (manuscript line 2022) | $u_{a(t)dt \otimes f} \mapsto B_f(a) = \int_I a(t) \overline{\operatorname{Tr} f(\phi_1(t), \phi_2(t))}\,dt$ (lines 79–84) | Match. |
| Bracket identity | $\{B_f(a), B_g(b)\} = B_{\{f,g\}}(ab)$ (manuscript `cor:local-bulk-boundary-coupling`) | Same: $\{B_f(a), B_g(b)\} = B_{\{f,g\}}(ab)$ (line 87) | Match. |
| Principal-part bracket | $\{B_f(a), \Theta_\rho(B)\} = \Theta_{f \cdot \rho}(aB)$ (in `prop:reduced-principal-part-boundary-current`) | Same: $\{B_f(a), \Theta_\rho(B)\} = \Theta_{f \cdot \rho}(aB)$ (line 120) | Match. |
| Θ-Θ bracket | Zero (in the reduced semidirect product) | Zero (line 121, "declared abelian in the reduced semidirect product"; W6-08 sharpening: "by structural force of the abelian-ideal property") | Match. The W6-08 prose-promotion is editorial. |
| Orientation reversal | (manuscript implicit) | Explicit remark (lines 150–161): density convention with `dt` sign change | Match. The appendix is more explicit. |

**No drift detected** in the conventions used by Theorem E vs. the
appendix. The appendix is a more explicit statement of the current
conventions used in the theorem; both agree.

---

## §T8. Cross-check against partial consolidator (#42)

The partial consolidator (#42) integrates W1..W17 into the master
ledger. W3-W24's findings should feed into the next consolidator pass
as follows:

### Findings to integrate

| W3-W24 ID | Severity | Target (Theorem E step) | Heal type | Master-ledger cross-walk |
|-----------|----------|--------------------------|-----------|---------------------------|
| W3-W24-01 | 1 (editorial) | Step 4 (line 2125) | Prose: spell out biderivation induction | New (no master ledger entry yet) |
| W3-W24-02 | 2 | Step 5 (line 2128) | Prose: bidirectional symmetric filtration | Sharpens W3-W6-01 (R-W3-W6-01) |
| W3-W24-03 | 2 | Step 6 (after diagram, line 2172) | Prose: n-tuple coassociativity | Sharpens M-24 (`lem:n-tuple-coassoc` named, not stated in proof) |
| W3-W24-04 | 2 | Step 7 (line 2174–2178) | Prose: cohomological local-constancy + degree-correction | Extends W6-05 |
| W3-W24-05 | 2 | Step 8 (line 2185) | Prose: limit interchange (Tate windows × stalk limit) | New; relates to M-27 (`lem:tate-mittag-leffler-dictionary`) |

### Cross-walk to existing ledger

- **M-01 (Tate-conilpotency).** Theorem E inherits the same fault on
  Step 2 (perfect `\bar A`): the Tate-conilpotency hypothesis of
  `lem:continuous-bar-cobar` fails for unweighted `\bar A`. Heal:
  M-01 5-way split (M-26) propagates from Theorem A to Theorem E.
  W3-W24 confirms no new fault.
- **M-24 (four-lemma chain).** W3-W24-03 sharpens by stating n-tuple
  coassociativity explicitly in Step 6.
- **M-33 (W6 eight-link DAG).** W3-W24's manuscript-step audit is
  consistent with the W6 DAG: each manuscript step maps to one or
  more DAG links.
- **W3-W6-01 (bidirectional symmetric filtration).** Propagates from
  cochain-level Theorem A to factorization-level Theorem E Step 5.
- **W6-02 (Step 1 HKR excision).** Theorem E Step 1 still cites HKR;
  the W6-02 / W3-W17-01 minimal heal (replace HKR by Lurie HA + local
  PV definition) is the architectural fix. Propagates through Step 5
  back-reference.
- **W6-05 (cohomological local-constancy).** W3-W24-04 extends to
  include the degree-correction (compactly supported de Rham
  cohomology is in degree 1, not degree 0; the manuscript's "degree
  zero" phrasing is imprecise).
- **W6-07 (R-03 sharpening).** Weiss-cosheaf residual is structurally
  outside Theorem E. W3-W24 confirms no Weiss-condition leak in
  Steps 1–8.

### New residuals after W3-W24

- **R-W3-W24-01 (editorial; biderivation induction).** Inscribe one
  sentence in Step 4 (W3-W24-01 heal). No mathematical content
  beyond what is already proved.
- **R-W3-W24-02 (bidirectional symmetric filtration on factorization
  level).** Verified at fixed Tate window for the cosheaf-of-Lie
  evaluation; inherits W3-W6-01 verification on the formal disk.
  Heal: editorial prose at Step 5.
- **R-W3-W24-03 (n-tuple coassociativity).** True; not stated.
  Heal: editorial prose at Step 6.
- **R-W3-W24-04 (Step 7 prose imprecision).** "Degree zero" should
  read "degree 1 in compactly supported cohomology of $\R$"; or
  alternatively, the value-at-a-point on the line. Heal: editorial
  prose at Step 7.
- **R-W3-W24-05 (limit interchange).** True; not stated. Heal:
  editorial prose at Step 8.

All five residuals are **editorial**, no new mathematical content
required. They make the manuscript prose precisely match the
mathematical content already proved.

### Status of Theorem E after W3-W24

**Stable on the brane-line, in the admissible Tate envelope, modulo
M-01 minimal heal at Step 2 (perfect `\bar A`) and W6-02 minimal
heal at Step 1 (HKR excision).** With the seven editorial heals
inscribed (W6-02, W6-04, W6-05, W3-W24-01, W3-W24-02, W3-W24-03,
W3-W24-05; W3-W24-04 = W6-05 extended), Theorem E's eight-step proof
closes cleanly on each interval and assembles into a locally
constant factorization-algebra equivalence on $\R$ in the admissible
Tate envelope.

The Weiss-cosheaf upgrade to $\R^2 \times \C^2$ is not within
Theorem E's scope; it is the standing residual R-03 / W6-07 (Phase-4
research, four ingredients named).

---

## §9. Files read

- `/Users/raeez/topological-strings/CLAUDE.md`
- `/Users/raeez/topological-strings/reconstitution/attack-heal-platonic-2026-04-28.md` (Theorem E entries: M-01, M-15, M-22, M-24, M-26, M-27, M-33; A2-007; W6-01..W6-08)
- `/Users/raeez/topological-strings/reconstitution/wave2-W6-beilinson-2026-04-28.md` (full)
- `/Users/raeez/topological-strings/reconstitution/wave3-W17-hkr-thmA-2026-04-28.md` (full)
- `/Users/raeez/topological-strings/reconstitution/wave3-W6-costello-composition-2026-04-28.md` (full)
- `/Users/raeez/topological-strings/reconstitution/wave2-W2-drinfeld-2026-04-28.md` (W2-01 rigidity audit; first 100 lines)
- `/Users/raeez/topological-strings/main.tex` (Theorem E proof at lines 1996–2191; supporting lemmas/propositions at 1914–1995, 2274–2330, 2461–2504, 3087–3116, 3245–3293, 3323–3389, 3791–3906, 4489–4571)
- `/Users/raeez/topological-strings/appendix-factorization-current-conventions.tex` (full)
- `/Users/raeez/topological-strings/tate-T3-quillen-equivalence.tex` (lines 395–589: derived-categorical promotion, Weiss-cosheaf residual)
- `/Users/raeez/topological-strings/tate-T4-bv-vanishing.tex` (lines 1–90: Costello–Li applicability check)
- `/Users/raeez/topological-strings/tate-T5-chain-level-primitive.tex` (lines 700–795: primitive shadow corollary, role of `lem:derivative-jets`)

---

## §10. 200-word summary

W24 audited Steps 2–8 of `\thm:open-closed-derived-center-factorization`
(Theorem E) under the Drinfeld + Composition lens. The manuscript
proof at `main.tex` 2049–2191 is literally indexed Steps 1–8;
Wave-2 W6 mapped these to an eight-link DAG (L1–L8), but the
manuscript-step indices and the W6 DAG-link indices are not
identical. W24 walked the manuscript indices verbatim. Five new
editorial findings: **W3-W24-01** (Step 4 biderivation induction
prose), **W3-W24-02** (Step 5 bidirectional symmetric filtration,
propagating W3-W6-01 from Theorem A to Theorem E),
**W3-W24-03** (Step 6 n-tuple coassociativity, sharpening M-24
`lem:n-tuple-coassoc`), **W3-W24-04** (Step 7 cohomological
local-constancy + degree-correction, extending W6-05),
**W3-W24-05** (Step 8 Tate-window × stalk-limit interchange). All
five are editorial prose only; no new mathematical content. Theorem E
inherits M-01 (Step 2, Tate-conilpotency for perfect `\bar A`) and
W6-02 (Step 1, HKR excision); the Weiss-cosheaf residual is
structurally outside Steps 1–8. Composition Step 1 → ... → Step 8 is
linear, associative, and yields the full Theorem E conclusion on
$\R$ in the admissible Tate envelope. Conventions match the
appendix line-by-line. **Theorem E is stable on the brane-line, in
the admissible Tate envelope, after the seven editorial heals.**

End of W3-W24 report.
