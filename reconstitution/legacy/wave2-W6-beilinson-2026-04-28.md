# Wave 2 / W6 — Beilinson + Composition Lens

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Beilinson (sheaf/cosheaf, descent, filtrations, exactness,
spectral sequences) + Composition (associativity, coherence,
transactionality of local-to-global passages).
**Inputs.** Wave-1 master ledger
`reconstitution/attack-heal-platonic-2026-04-28.md` items M-09, M-13,
M-14 (= R-03), M-15, M-16, M-17, M-23, M-24, M-25;
`appendix-factorization-current-conventions.tex` (full);
`tate-T3-quillen-equivalence.tex` 257–589;
`tate-T5-chain-level-primitive.tex` 1–688; `theorem-lanes.tex`
209–342; `main.tex` 1900–2475, 2780–2802, 3323–3438.
**Mode.** Proposal-only. No manuscript edits. Inscribable durable
deliverable: this report.
**Independence.** Wave-1 A6's four-lemma chain (M-24) is taken as the
**input under attack**. The deliverable is an explicit eight-link DAG,
its acyclicity verification, hypothesis-on-the-exterior-face audit of
Lurie HA §5.5.4 / Costello–Gwilliam Vol. I §6.4 invocations, T5 rename
precision, R-03 sharpening, and a structural (not by-fiat) account of
distribution-product avoidance.

---

## §0. The eight-link chain, explicit

Wave-1 A6 / M-24 names four lemmas required for the locally constant
factorization equivalence `thm:open-closed-derived-center-factorization`:
`lem:locally-constant-cosheaf`, `lem:B-cohom-well-defined`,
`lem:n-tuple-coassoc`, `lem:composition-chain`. The full proof in
`main.tex` 1996–2191 has eight steps; the four lemmas of M-24 cover
sub-parts of those steps. The **eight-link DAG below** decomposes the
chain into atomic content, each link with explicit hypothesis set and
output, so the composition can be audited.

* **L1 (cosheaf-of-Lie).** $I\mapsto \mathfrak h_I=\Omega^\bullet_c(I)
  \widehat\otimes \bar A$ and $I\mapsto \mathfrak g_I=\mathfrak h_I
  \ltimes\mathcal P_I[1]$ are cosheaves of dg Lie algebras on $\R$
  with extension by zero as structure maps. *Hypothesis:* $\Omega^\bullet_c$
  cosheaf on $\R$ (Costello–Gwilliam Vol. I §6.5 / §A.5.4); strict
  $P_0$-bracket extends as biderivation. *Output:* a strict cosheaf
  morphism $I'\hookrightarrow I$ for every interval inclusion, with
  bracket and de Rham product compatible. *Manuscript locus:*
  `constr:interval-fact-algebras`, lines 1914–1963.
* **L2 (source-convention dictionary).** $u_{a(t)dt\otimes f}\mapsto
  B_f(a)$ on length-one shifted-cotangent CE coordinates;
  $c_\lambda\mapsto\theta_\lambda$ on length-one Hamiltonian CE
  coordinates. *Hypothesis:* `prop:app-factorization-source-of-B`
  (cotangent-direction CE coordinate is the source of the smeared
  boundary observable, not a shifted Hamiltonian dual). *Output:*
  generator-level dictionary on length one, with
  $\Phi(d_{\mathrm{CE}}u_K) = d_\pi O_K$. *Manuscript locus:*
  `appendix-factorization-current-conventions.tex` lines 73–105.
* **L3 (interval-wise generator-level CE/PV identity).** On each
  interval $I$, $\Phi^{\mathrm{Ham}}_{\mathrm{fact}}(I)$ matches CE
  differential and Schouten differential on length-$\le 1$ words, hence
  by Leibniz on every word at fixed length. *Hypothesis:* `lem:linear-poisson-schouten`
  (Schouten/Lichnerowicz on $\widehat{\mathbf S}_{\mathrm{Tate}}(\mathfrak h_I)$);
  Tate completeness of both source and target; Leibniz/algebra-homomorphism.
  *Output:* a strict cochain isomorphism $\Phi$ on the completed dg
  graded-commutative source. *Manuscript locus:*
  `thm:open-closed-derived-center-factorization` Steps 1–5,
  `thm:open-closed-derived-center` Generators / Cochain identity / Inverse / $P_0$-bracket steps.
* **L4 (Tate conilpotency window-by-window for $\mathfrak g_I$).**
  At fixed Tate window, $\bar A_{\le w} = \C[z_1,z_2]_{\le w}/\C\cdot 1$
  is finite-dimensional and nilpotent under the descending Lie
  central series; hence $\mathfrak g_{I,\le w}$ satisfies
  `lem:continuous-bar-cobar` item~(2). *Hypothesis:* finite Tate
  window. *Output:* CE coalgebra $C_*^{\mathrm{CE}}(\mathfrak g_{I,\le w})$
  conilpotent, continuous CE chains identified with completed symmetric
  algebra on the continuous dual.
* **L5 (Mittag-Leffler exactness across Tate windows).** Inverse
  limits in the cofiltered Tate filtration are exact. *Hypothesis:*
  Mittag-Leffler condition (`alpharef` item~1) on the windowed inverse
  systems; the surjective transition maps in the bounded-below Tate
  envelope of `stmt:tate-model-envelope` satisfy this by construction.
  *Output:* the windowwise CE/PV qiso of L3 lifts to a global filtered
  qiso. *Manuscript locus:* `thm:tate-bar-cobar-quillen` proof
  (Mittag-Leffler resolution) lines 290–303.
* **L6 (locally constant cosheaf descent on $\R$).** Inclusions
  $I'\hookrightarrow I$ of nonempty open intervals induce
  quasi-isomorphisms of structure maps; $\partial_t = [d_\R,
  \iota_{\partial_t}]$ contracts positive jets. *Hypothesis:*
  `lem:derivative-jets`. *Output:* locally constant FA structure on
  $\R$, with stalkwise central operation $f\mapsto L_{B_f}$ as the
  $E_1$-shadow. *Manuscript locus:* `thm:open-closed-derived-center-factorization`
  Step 7, lines 2174–2184.
* **L7 (disjoint-support locality).** $\{B_f(a),B_g(b)\}=B_{\{f,g\}}(ab)
  = 0$ when $\mathrm{supp}(a)\cap\mathrm{supp}(b)=\emptyset$.
  *Hypothesis:* canonical equal-time bracket
  $\{(\phi_1)(t),(\phi_2)(s)\}=\delta(t-s)$; pointwise product $ab\equiv 0$
  on disjoint supports. *Output:* strict factorization product
  property — strict $P_0$ FA, not a homotopical one. *Manuscript locus:*
  `prop:brane-bracket-locality` lines 1965–1979 and
  `rmk:equal-time-locality` lines 1981–1994.
* **L8 (Lurie HA §5.5.4 / CG Vol. I §6.4 promotion).** Locally constant
  FAs on $\R$ are equivalent to $E_1$-algebras up to contractible
  choice. *Hypothesis:* presentability of the admissible Tate envelope
  (cofibrant generation of `thm:tate-model-structure` plus Lurie
  A.2.6.8); $n=1$ on the brane line. *Output:* the strict cochain
  equivalence $\Phi$ promotes to an equivalence in the $\infty$-category
  of locally constant $P_0$-FAs. *Manuscript locus:*
  `thm:open-closed-derived-center-derived` (T3 lines 398–468);
  `cor:tate-bar-cobar-infinity` (T3 321–346).

**Cross-walk to wave-1 M-24.** L1 ↔ `lem:locally-constant-cosheaf`
(A6-A2). Sub-statement of L7 ↔ `lem:B-cohom-well-defined` (A6-A3,
asserting $B_f(a)$ depends only on $[a(t)dt]$ modulo $Q$-exact). L7
$\to$ Step 6 disjoint factorization ↔ `lem:n-tuple-coassoc` (A6-A6).
L8 ↔ `lem:composition-chain` (A6-A10). Wave-1's four-lemma list is a
**necessary minimal cover** but not the **complete chain**: it omits
explicit naming of L3 (generator-level CE/PV identity), L4 (Tate
conilpotency at window), L5 (Mittag-Leffler), L6 (de Rham-jet
contraction).

---

## §1. DAG and acyclicity (Mandate item 1)

```
            L1 ───────────────────┐                        
                                  │                        
            L2 ──┐                ▼                        
                 ├──> L3 ──┐    L7 ───┐                    
            L4 ──┘         │          │                    
                           ▼          ▼                    
                          L5 ──> L6 ──> L8                 
                           ▲                               
                           │                               
                          L4                               
```

**Edge list:** L1→L3, L2→L3, L4→L3, L3→L5, L4→L5, L5→L6, L1→L6,
L1→L7, L6→L8, L7→L8, plus L8 also depends on the externally cited
Lurie HA §5.5.4 + CG Vol. I §6.4 + Tate Quillen equivalence
`thm:tate-bar-cobar-quillen` (which itself depends on L4 via
`lem:continuous-bar-cobar`(2)).

**Acyclicity.** Topological sort: L1, L2, L4 (sources, no in-edges);
L3, L7 (depend on sources); L5 (depends on L3, L4); L6 (depends on
L5, L1); L8 (depends on L6, L7). No back-edges; **DAG acyclic**.

**Final composition closes.** Compose along the unique source-to-sink
path: from L1 (cosheaf), L2 (dictionary), L4 (Tate window) feed L3
(generator identity); L3, L4 feed L5 (Mittag-Leffler); L5, L1 feed
L6 (locally constant); L1 feeds L7 (locality); L6, L7 feed L8 (Lurie
$\infty$-promotion). Every output of a link is exactly the hypothesis
of the next. **Composition closes the locally constant
factorization-algebra equivalence on $\R$.**

**W6-01 (verified).** No silent forward dependency. Each lemma's
hypothesis set is satisfied by an earlier lemma's output, plus
externally cited resources at L8 (Lurie + CG + Tate Quillen).

**W6-02 (risk detected at L3).** Step 1 of
`thm:open-closed-derived-center-factorization` (lines 2050–2076)
invokes "the Hochschild–Kostant–Rosenberg theorem in the
smooth/algebraic setting, applied here to the free graded-commutative
algebra on the Tate vector space $\mathfrak h_I$" to identify
$\mathrm{Hoch}^\bullet(\widehat{\mathbf S}(\mathfrak h_I))$ with
$\mathrm{PV}^\bullet(\widehat{\mathbf S}(\mathfrak h_I))$. Wave-1 M-01
already excises Tate HKR from `thm:open-closed-derived-center` and
replaces it by the local Poisson-CE definition (M-08 path). The same
HKR appeal **survives inside L3 / Step 1** of the factorization
theorem. The unweighted Tate HKR is non-trivial in the $\Cat{TateVec}$
setting; finite-dimensional HKR (Hochschild–Kostant–Rosenberg 1962)
does not directly transfer.

**Heal proposal W6-02.** Replace the Step 1 HKR appeal in
`thm:open-closed-derived-center-factorization` by the local definition
$\mathrm Z^{P_0}_{\mathrm{fact}}(A_\partial^{\mathrm{Ham}})(I)
:= \mathrm{PV}(\widehat{\mathbf S}(\mathfrak h_I))$ for the linear
Poisson, free graded-commutative case (M-08 path: cite Costello–Gwilliam
Vol. II §1.4 local $P_0$-centre construction). HKR exits L3 and L8.

**W6-03 (DAG closure under M-01 split).** The perfectness obstruction
that M-01 names for unweighted $\mathfrak h$ does *not* propagate into
$\mathfrak g_I$ at fixed Tate window: window-by-window, $\bar A_{\le w}
= \C[z_1,z_2]_{\le w}/\C\cdot 1$ is finite-dimensional and the
descending Lie central series stabilises in finitely many steps. The
*limit* in the Tate filtration is what M-01 forbids; for each fixed
window, L4 is satisfied. Hence the DAG closes the locally constant FA
equivalence at the **interval-wise admissible envelope** for arbitrary
nonempty open $I\subset\R$. The unweighted limit on the brane line is
regulator-independent (M-11), not a $q\to 1^+$ limit.

---

## §2. Lurie HA §5.5.4 verification (Mandate item 2)

**§5.5.4 statement (paraphrase).** Lurie *Higher Algebra* §5.5.4
defines locally constant factorization algebras on a topological
manifold $M$: a factorization algebra $\mathcal F$ is locally constant
if the structure map $\mathcal F(U)\to\mathcal F(V)$ is an equivalence
for every disk inclusion $U\hookrightarrow V$. Theorem 5.5.4.10 (with
the disk frame bundle / Kan extension argument) establishes the
equivalence
$$\mathrm{Fact}^{\mathrm{lc}}(\R^n) \;\simeq\; \Alg_{E_n}(\Cat C)$$
in $\mathcal P r^L$, where $\Cat C$ is a presentable symmetric monoidal
$\infty$-category. The $n=1$ case identifies $E_1 = A_\infty$ associative
algebras up to contractible choice.

**Source verification.** I confirmed via web search that Lurie's
*Higher Algebra* (September 2017 version) is the canonical reference;
the equivalence on $\R^n$ between $E_n$-algebras and locally constant
FAs is established in §5.5.4.10. (Independent treatments: Matsuoka
"Koszul duality for locally constant factorization algebras" arXiv:1409.6945
and Münster J. Math 10 (2017) 83–118 confirm the equivalence and its
hypotheses.)

**Manuscript invocations.** Three loci use Lurie §5.5.4:
1. `thm:open-closed-derived-center-derived` (T3 lines 466–467).
2. `prop:weiss-cosheaf-residual` (T3 lines 552–558).
3. `rmk:E1-translation` (`main.tex` lines 2196–2198).

All three correctly invoke $n=1$ on the brane line $\R$.

**Hypothesis check.** Lurie 5.5.4.10 lives in $\mathcal P r^L$, so the
target $\infty$-category must be locally presentable and accessible.
The manuscript's `cor:tate-bar-cobar-infinity` (T3 lines 321–346)
correctly hedges: "Presentability is an attribute of the chosen
locally presentable envelope, not of the raw Tate category."
Cofibrant generation of `thm:tate-model-structure` (`thm:tate-model-structure`
lines 83–96; transferred via `lem:transferred-model`,
`lem:tate-conilp-model` lines 155–253) plus Lurie A.2.6.8 supplies
presentability inside the envelope. **Hypothesis satisfied — but not
explicit on the exterior face of the theorem statement.**

**Critical $n$-check.** Lurie 5.5.4 with $n=5$ would be required for
locally constant FAs on $\R^2\times\C^2$ (real dimension 6, of which
five are "topological" in the sense that the BV theory has $Q$-exact
translation; the brane defect $\R\times\{0\}\subset\R^2\times\C^2$ is
codimension 5, see M-19). The manuscript invokes $n=1$ only and
explicitly names the higher-$n$ extension as residual in
`prop:weiss-cosheaf-residual` (T3 lines 530–563). **No false
invocation.**

**Heal proposal W6-04.** Add a hypothesis paragraph immediately
preceding `thm:open-closed-derived-center-derived`:

> *Hypotheses for Lurie §5.5.4 invocation.* The admissible Tate
> envelope of `thm:tate-model-structure` is locally presentable and
> accessible (cofibrant generation by `lem:transferred-model`,
> `lem:tate-conilp-model`; Lurie A.2.6.8). Lurie §5.5.4.10 is invoked
> for $n=1$ on the brane line $\R$ only. The $n>1$ extension to
> $\R^2\times\C^2$ is the Weiss-cosheaf descent residual of
> `prop:weiss-cosheaf-residual` and is not used here.

---

## §3. Costello–Gwilliam Vol. I §6.4 verification (Mandate item 3)

**§6.4 content.** Costello–Gwilliam Vol. I §6.4 develops *locally
constant prefactorization algebras* on $\R$ and the structure-theorem
that they correspond to associative ($A_\infty$) algebras (Example
6.4.0.5 / Proposition 6.4.0.4). The data of a locally constant FA on
$\R$: an algebra $A = \mathcal F(\R)$ together with structure maps
$\mathcal F(I_1)\otimes\mathcal F(I_2)\to\mathcal F(V)$ for disjoint
inclusions $I_1\sqcup I_2\subset V$, equivalent to $A\otimes A\to A$
(multiplication) up to coherent homotopy.

**Applicability checks for the manuscript invocations.**

(a) *Compactly supported observables.* The brane factorization algebras
$A_\partial^{\mathrm{Ham}}(I) = \widehat{\mathbf S}(\mathfrak h_I)$
with $\mathfrak h_I = \Omega^\bullet_c(I)\widehat\otimes\bar A$ are
constructed from compactly supported de Rham forms on $I$, with
extension by zero as structure maps. CG §6.4 covers exactly this
setup (factorization algebras built from cosheaves of compactly
supported forms). **Compatible.**

(b) *De Rham cosheaf direction.* The source $\mathfrak h_I$ is *not*
constant as a topological vector space: $\Omega^\bullet_c(I)$ is
non-trivial as a chain complex. But it is **cohomologically constant**:
$H^\bullet(\Omega^\bullet_c(I))$ is concentrated in degree 0 with
one-dimensional fibre (by `lem:derivative-jets` and the contraction
$[d_\R, \iota_{\partial_t}] = \partial_t$). Structure maps on
$I'\hookrightarrow I$ are quasi-isomorphisms at this cohomological
level. **Locally constant in the CG §6.4 sense.**

(c) *$P_0$ refinement.* CG Vol. I §6.4 covers the underlying
$E_1$-algebra structure but not the $P_0$-algebra refinement of
locally constant FAs explicitly. The manuscript's
`thm:open-closed-derived-center-derived` is what promotes the
cochain-level identification to the $P_0$ level, drawing on
Cattaneo–Felder's BV operad and CG Vol. II §1.4. The cite
`\cite{costello-gwilliam}*{Vol.~I \S 6.4}` in the manuscript
is for the *locally constant terminology only*, not for a
$P_0$-version theorem. **Correctly scoped.**

(d) *Verifying the manuscript's prose.* `rmk:E1-translation` lines
2193–2198 reads:
> "factorization algebras are equivalent to homotopy associative
> algebras up to translation invariance by Lurie, *Higher Algebra*,
> §5.5.4, in the Costello–Gwilliam vocabulary of locally constant
> factorization algebras Vol. I §6.4."

This is precise: Lurie supplies the equivalence theorem; CG §6.4
supplies the locally-constant-FA terminology. **No semantic
overreach.**

**Heal proposal W6-05.** Add one sentence to Step 7 of
`thm:open-closed-derived-center-factorization` (proof, line 2179):

> "Locally constant structure is at the *cohomological* level:
> $H^\bullet(\Omega^\bullet_c(I))$ is concentrated in degree zero
> with one-dimensional fibre (`lem:derivative-jets`), so structure
> maps on $I'\hookrightarrow I$ are quasi-isomorphisms in the sense
> of CG Vol. I §6.4."

This makes the hypothesis explicit on the exterior face of L6.

---

## §4. T5 rename precision check (Mandate item 4)

**What `pi_{prim}^{cot}` actually is** (T5 lines 353–482).
$\pi_{\mathrm{prim}}^{\mathrm{cot}}$ is defined piecewise on three
strata:
* *zero-$\psi$ Hamiltonian sector:* cumulant projection
  $\pi_{\mathrm{prim}}: \mathrm{Obs}\twoheadrightarrow\Omega^\bullet_c(I)
  \widehat\otimes\bar A$ followed by inclusion into
  $\bar A\oplus\mc P[1]$;
* *primitive one-$\psi$ sector:* label projection
  $B\otimes\Psi_{a,b}\mapsto B\otimes\rho_{a,b}[1]$;
* *multi-trace sector:* $\to 0$.

`Theorem~thm:chain-level-primitive-projection` (T5 lines 388–482)
proves four compatibilities: (1) BV chain map, (2) factorization
product strict mod zero homotopy, (3) $P_0$-bracket strict mod zero
homotopy **on the Hamiltonian zero-$\psi$ indecomposable quotient
only**, (4) cosheaf compatibility.

**Verbatim against T5 lines 600–688.**
`thm:no-hbar-primitive-descendant-intertwiner` (lines 619–688) proves
the obstruction on $\widetilde\Psi_{1,0}$ already at order $\hbar^0$:
source-then-target gives $z_1\cdot_0\widetilde\Psi_{1,0} = 0$;
target-then-action gives $z_1\cdot\rho_{1,0}[1] = -\rho_{1,1}[1]\ne 0$.
The mismatch is **structural and propagates to all $\hbar$-orders**.
The same computation with $z_2$ on $\widetilde\Psi_{0,1}$ gives 0 vs
$\rho_{1,1}\ne 0$. The asymmetry in coordinates rules out a coordinate
choice as a fix.

**Verdict on the wave-1 rename ("primitive indecomposable
$P_0$-shadow").** The proposed name is **accurate but
under-specifies the $P_0$ direction**: only the bracket on the
zero-$\psi$ Hamiltonian sector is intertwined. The label-projection
on the one-$\psi$ sector is **not** $\mathfrak h$-equivariant — this
is the Theorem D embedded no-go and
`prop:quantum-descendant-label-obstruction`. A reader could mistake
the M-15 rename for a full $P_0$-isomorphism, which it is not.

**Heal proposal W6-06 (refined rename).** Promote M-15 to:

> "Primitive indecomposable cotangent shadow ($P_0$-bracket
> intertwined on the Hamiltonian zero-$\psi$ sector;
> $\mathfrak h$-non-equivariant label projection on the one-$\psi$
> sector)."

The long form appears once at the theorem statement; downstream prose
contracts to "the primitive cotangent shadow." This precisely captures
all four compatibilities (1)–(4) of
`thm:chain-level-primitive-projection`, names the equivariance
failure on the cotangent direction, and closes the loophole.

**Cross-check against
`rmk:cumulant-target-indecomposable`** (T5 lines 178–196): the target
$\Omega^\bullet_c(I)\widehat\otimes\bar A$ is described as "the
indecomposable or linear primitive part of the brane $P_0$
factorization algebra." This matches the rename: indecomposable on
the zero-$\psi$ sector, label-only on the one-$\psi$ sector.
**Consistent.**

---

## §5. Sharpened R-03 (Mandate item 5)

**Current statement.** M-14 / R-03 (master ledger lines 663–691):
Weiss-cosheaf descent on $\R^2\times\C^2$ is open. Locus:
`prop:weiss-cosheaf-residual` (T3 lines 530–563).

**The four ingredients required to close R-03.**

1. **Heat-kernel propagator $P_{\epsilon,L}^{\R^2\times\C^2}$**,
   *separated into directions*:
   - topological direction $\R$: Wick-rotated 1d propagator
     $G_t(x,y) = \tfrac12 e^{-|x-y|^2/4t}/\sqrt{4\pi t}$, with regulator
     $\epsilon\le t\le L$;
   - transverse $\R\times\C^2$: $\bar\partial$-Hodge propagator on
     $\C^2\setminus\{z=0\}$, with the brane line $\R\times\{0\}$
     excised. The propagator must vanish in distribution at the
     defect to respect the principal-part structure of Theorem D.
2. **Defect boundary condition** for $\R\times\{0\}\hookrightarrow
   \R^2\times\C^2$, derived from the brane Lagrangian
   $\int_\R\mathrm{Tr}(\phi_1\,d\phi_2 + A[\phi_1,\phi_2])$. Specifically:
   matter fields $\phi_1, \phi_2$ are restricted to the brane line;
   gauge field $A$ provides the moment-map constraint; antifield $\psi$
   carries $Q\psi = [\phi_1,\phi_2]$. The boundary condition must be
   compatible with the bulk holomorphic structure (transverse $\C^2$
   direction).
3. **Bulk-to-defect kernel** $K_{\mathrm{bd}}: \mathcal F^{\mathrm{bulk}}
   \to \mathcal F^{\mathrm{defect}}$ compatible with: (i) Theorem D's
   principal-part residue calculus (the kernel must reproduce
   $\rho_{a,b}$ as defect-localised distributions in transverse
   coordinates); (ii) M-13/N9 distribution-product avoidance (no
   ill-defined $\delta\cdot\delta$ products at the defect line).
4. **Mittag-Leffler resolution transverse to the brane** of the
   cofiltered Tate windowing in the principal-part direction:
   $\mathcal P[1]$ is a strict colimit of finite-window principal
   parts $\rho_{a,b}$ with $a+b\le w$, and the inverse system on the
   Weiss cover must satisfy ML on each window.

Once these four are in hand, descent follows by standard CG Vol. I
§6.5 / §7.2 + Vol. II §A.5 Weiss-cosheaf machinery.

**Within-reach assessment.** Costello's RG construction (Costello,
*Renormalization and Effective Field Theory*, AMS Math. Surveys 170,
2011) handles 5d/6d defect theories of this character (twisted
M-theory with Costello–Gaiotto–Williams; $\Omega$-deformed
holomorphic-topological theories). The brane-line BF defect on
$\R^2\times\C^2$ is structurally similar to CG holomorphic
Chern–Simons + defect setups (Costello–Gwilliam Vol. II Ch. 11).
**The genuinely hard ingredient is Mittag-Leffler resolution
transverse to the brane**: principal parts $\rho_{a,b}$ are
defect-localised distributions, *not* bulk fields, and the
bulk-to-defect kernel must respect the residue calculus of Theorem D.
This is closer to Beilinson–Drinfeld chiral algebra factorization than
to standard Costello-RG on a closed manifold.

**Estimate.** Six-month research project for a Costello-RG specialist
with chiral-algebra background; prerequisites are already present in
the manuscript (M-14 names the residual; Theorem A forces brane
action; Theorem D fixes Matlis dual; M-23/N9 names distribution
avoidance). What is missing is the *analytic* propagator + ML
construction.

**Genuinely beyond reach component.** If the principal-part Matlis
dual genuinely requires the $\bar\partial$-resolution to be exact at
the defect — which the residue pairing of Theorem D suggests — the
Hodge-theoretic construction may be **non-trivially obstructed**:
the resolution of distributions supported on a codimension-4
holomorphic subspace inside $\C^2$ is not a standard
$\bar\partial$-operation. This is the residual of the residual: not
**within** Costello-RG as stated, but reachable via a chiral-algebra
factorization + Beilinson–Drinfeld localization technique.

**Heal proposal W6-07.** Replace the text of
`prop:weiss-cosheaf-residual` (T3 lines 530–563) by the sharpened R-03
statement above with the four-ingredient list and the
within-reach/beyond-reach sub-decomposition. Mark as Phase-4 research
per plan §8. Cross-link to Beilinson–Drinfeld *Chiral Algebras*
(2004) §3.4 for the relevant factorization technique and to Costello
(2011) §10 for the heat-kernel apparatus.

---

## §6. Distribution-product avoidance discipline (Mandate item 6)

**The bracket $\{\Theta_\rho, \Theta_\sigma\} = 0$.**
`prop:app-factorization-principal-part-bracket`
(`appendix-factorization-current-conventions.tex` lines 107–148)
declares the third bracket zero "in the reduced semidirect product"
(line 121, proof line 147).

**Three structural checks.**

(a) **Internal consistency of the abelian-ideal declaration.** The
shifted-cotangent Lie algebra $\mathfrak g_I = \mathfrak h_I \ltimes
\mathcal P_I[1]$ has $\mathcal P_I[1]$ as an *abelian odd ideal* by
construction of the semidirect product. The biderivation extension
of the Lie bracket to $\widehat{\mathbf S}(\mathcal P_I[1])$
(which sits in $A_\partial^{\mathrm{pp}}$) is *necessarily* zero on
cotangent-cotangent pairs: in the semidirect-product structure on
$\mathfrak g_I$, the cotangent factor is abelian. **The bracket is
zero by construction, not by fiat.**

(b) **Distribution-product issue.** If $B \in \mathcal D'_c(I_1)$ and
$C \in \mathcal D'_c(I_2)$ have overlapping supports (e.g.,
$I_1 = I_2$), the distribution-distribution product $BC$ is generally
ill-defined as an operation on $\mathcal D'_c(I)$ (Hörmander wave-front
condition, Schwartz "no impossible product theorem"). The bracket
$\{\Theta_\rho, \Theta_\sigma\} = 0$ is the *structural* avoidance of
this issue: the formalism never encounters distribution-distribution
multiplication because the $P_0$-bracket structure forces zero on
cotangent-cotangent pairs by (a).

(c) **Other distribution operations — audit.**
- *Multiplication-by-smooth* ($aB$, $a\in C^\infty_c$): well-defined
  (Schwartz product); appears in
  $\{B_f(a),\Theta_\rho(B)\}=\Theta_{f\cdot\rho}(aB)$.
- *Differentiation* $\partial_t B$: well-defined; in the de Rham
  differential on $\mathcal D'_c(I)$.
- *Restriction / extension by zero*: well-defined; the cosheaf
  structure on $\mathcal D'_c(I)$.
- *Pairing with smooth* $\langle B, a\rangle = B(a)$: well-defined;
  in `def:app-factorization-current-dual`.
- *Convolution* $B*C$: not used in the formalism.
- *Composition* $B\circ C$: not used.
- *Distribution-distribution multiplication* $BC$: **forbidden by
  structural force** per (b).

**Verdict.** The distribution-product avoidance is **structural, not
by fiat**. It is a theorem of the structure (forced by the abelian-
ideal property of $\mathcal P_I[1]$ in the semidirect product), not a
hypothesis on the structure. The proof of
`prop:app-factorization-principal-part-bracket` (line 147) currently
reads "The $\Theta$-sector is declared abelian in the reduced
semidirect product, giving the third bracket." The word "declared"
under-states the situation: it is forced, not declared.

**Heal proposal W6-08.** Replace the line in
`appendix-factorization-current-conventions.tex` proof of
`prop:app-factorization-principal-part-bracket`:

> "The cotangent factor $\mathcal P_I[1]$ is the shifted abelian odd
> ideal of the semidirect product $\mathfrak g_I = \mathfrak h_I
> \ltimes \mathcal P_I[1]$. Biderivation extension of the Lie bracket
> to $\widehat{\mathbf S}(\mathcal P_I[1])$ is identically zero on
> cotangent-cotangent pairs *by the abelian-ideal structure of the
> semidirect product*, not by an extra declaration. This is structural
> distribution-product avoidance (M-13 / N9): distribution-distribution
> products $BC$ on $\mathcal D'_c(I)$ are ill-defined as operations
> (Schwartz/Hörmander), and the $P_0$-bracket structure forces zero on
> the relevant pairs, so the formalism never encounters such a
> product."

---

## §7. Validated DAG (final)

| Link | Verification | Heal needed |
|------|--------------|-------------|
| L1 (cosheaf) | verified | none |
| L2 (dictionary) | verified (M-16) | none (already inscribed) |
| L3 (generator CE/PV) | verified mod heal | **W6-02** (excise HKR from Step 1) |
| L4 (Tate conilpotency at window) | verified at fixed window; M-01 split required for unweighted limit | inscribed via M-01 |
| L5 (Mittag-Leffler) | verified mod ML lemma | inscribed via M-25 / R-05 |
| L6 (locally constant) | verified mod prose | **W6-05** (cohomological local-constancy sentence) |
| L7 (locality) | verified | none |
| L8 (Lurie/CG promotion) | verified for $n=1$ | **W6-04** (hypothesis paragraph for presentability + $n=1$ scope) |

**Validated DAG of the lemma chain.** With the three editorial heals
(W6-02, W6-04, W6-05), the eight-link DAG closes the locally constant
factorization-algebra equivalence on $\R$ in the admissible Tate
envelope, for arbitrary nonempty open $I\subset\R$, without HKR
appeal and without unweighted-limit dependency.

---

## §8. Summary of W6 heal proposals

| ID | Severity | Target | Action |
|----|----------|--------|--------|
| W6-02 | 3 | `thm:open-closed-derived-center-factorization` Step 1 | Replace HKR appeal by local-definition cite (M-08 path); push Tate HKR out of L3, L8 |
| W6-04 | 2 | Preamble of `thm:open-closed-derived-center-derived` | Add explicit Lurie 5.5.4 hypothesis paragraph (presentability/$n=1$ scope) |
| W6-05 | 2 | `thm:open-closed-derived-center-factorization` Step 7 | Add one sentence: cohomological local-constancy of $\Omega^\bullet_c$ via `lem:derivative-jets` |
| W6-06 | 2 | M-15 rename in T5 + `theorem-lanes.tex` Lane 6 | Refine to "Primitive indecomposable cotangent shadow ($P_0$-bracket on Hamiltonian zero-$\psi$; $\mathfrak h$-non-equivariant label projection on one-$\psi$)" |
| W6-07 | 3 | `prop:weiss-cosheaf-residual` text (T3 530–563) | Replace by sharpened R-03 with four-ingredient minimal-extra-input list + within-reach/beyond-reach sub-decomposition |
| W6-08 | 2 | `prop:app-factorization-principal-part-bracket` proof line 147 | Promote distribution-product avoidance from "declared" to "by structural force of the abelian-ideal property of $\mathcal P_I[1]$" |

All six are editorial. None requires new mathematical content beyond
prose-level promotion of structural facts. W6-02 requires aligning
with M-01 / M-08 (already in master ledger). W6-04 names the
presentability hypothesis explicitly. W6-05 names the cohomological
sense. W6-06 sharpens M-15. W6-07 is the most substantive (R-03
sharpening with four named ingredients). W6-08 is structural prose
promotion.

---

## §9. Closing

The Beilinson + Composition lens does not invalidate any wave-1
master ledger item. It produces:

1. **Validated eight-link DAG** of the locally constant
   factorization-algebra equivalence (§0–§1, §7), with explicit
   acyclicity verification and one HKR risk at L3 (W6-02).
2. **Hypothesis-on-the-exterior-face audit** of Lurie HA §5.5.4 (§2)
   and CG Vol. I §6.4 (§3), with two prose heals (W6-04, W6-05).
3. **T5 rename precision** (§4): wave-1's "primitive indecomposable
   $P_0$-shadow" is accurate but under-specifies; W6-06 refines.
4. **R-03 sharpening** (§5): four-ingredient list + within-reach /
   beyond-reach sub-decomposition (W6-07).
5. **Distribution-product avoidance** (§6): structural, not by fiat;
   W6-08 promotes the prose accordingly.

The eight-link DAG is acyclic; with the six W6 heals inscribed, the
chain closes cleanly in the admissible Tate envelope. The mandate's
"8-step lemma chain" is realized as L1–L8; wave-1's four-lemma list
of M-24 maps as L1↔`lem:locally-constant-cosheaf`,
sub-statement of L7↔`lem:B-cohom-well-defined`,
L7→Step-6→L8↔`lem:n-tuple-coassoc`,
L8↔`lem:composition-chain`. The DAG-level explicit naming improves
readability and makes the hypotheses manifest on the exterior face.

The R-03 sharpening (§5, W6-07) is the most concrete inscribable
contribution: it names the four ingredients (heat-kernel propagator,
defect boundary condition, bulk-to-defect kernel, transverse
Mittag-Leffler) and isolates the genuinely hard piece (transverse ML
on defect-localised distributions, closer to Beilinson–Drinfeld
chiral algebra than standard Costello-RG).

End of W6 report.
