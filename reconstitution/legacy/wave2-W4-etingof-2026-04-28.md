# Wave-2 W4 Etingof Lens — Categorical Extensions of Obligation II

**Date.** 2026-04-28.
**Author.** Raeez Lorgat.
**Wave.** 2 (independent attacker; reads wave-1 master ledger).
**Lens.** Etingof — tensor categories, finite examples, semisimplicity
failures, deformation, quantization, first-nontrivial-example sanity.
**Mandate.** Attack each named categorical extension to Obligation II
(M-02 wave-1) — derived $D_\hbar$-modules, microlocal sheaves,
factorization $D_\hbar$-bimodules — to determine whether the heal
"categorical extension is open" is genuinely tractable or just a
rebranding of the same impossibility. Independently verify the 21-case
sweep, identify the precise category $\mathsf P_{\mathrm{pol}}$ hosting
the embedded no-go, propose Obligation II sharpening.
**Mode.** Proposal-only.

---

## §0. Method

IDs are W4-NN. Each named extension gets a verdict: tractable / open /
forbidden. Wave-1 M-02 established the literal Rees candidate fails
both fibre conditions; W4 sharpens by attacking each named successor
category, by independent sweep, by analysis of the host category, and
by residue-duality reframing.

---

## §1. Independent verification of the 21-case sweep

Compare for $(p,q)\in[0,3]^2$ Hamiltonians acting on $(a,b)\in[0,3]^2$
labels:
* PBW raising: $F_{p,q}(\widetilde\Psi_{a,b})=(pb-qa)\widetilde\Psi_{a+p-1,b+q-1}$.
* Matlis coadjoint: $z_1^pz_2^q\cdot\rho_{a,b}=-(pb-qa+p-q)\rho_{a-p+1,b-q+1}$,
  zero when any new index is negative or both vanish.

Restricted to $(a,b)\in[0,3]^2,a+b>0$:
* Total nontrivial cases: **214**.
* Total label-shift matches: **12**, all at $(p,q)=(1,1)$.
* Total label+coefficient matches: **0**.

Theoretical confirmation: $(a+p-1,b+q-1)=(a-p+1,b-q+1)$ forces
$2(p-1,q-1)=0$, so $p=q=1$ is the unique label-match $(p,q)$. At
$(p,q)=(1,1)$ the coefficients $(b-a)$ versus $-(b-a)$ are sign-opposite.

Spot checks at the named test cases:
* $(2,1,2,1)$: PBW shift $(3,1)$, coeff $0$; coadj shift $(1,1)$, coeff $-1$.
* $(2,1,1,2)$: PBW shift $(2,2)$, coeff $3$; coadj shift $(0,2)$, coeff $-4$.
* $(1,2,2,2)$: PBW shift $(2,3)$, coeff $-2$; coadj shift $(2,1)$, coeff $3$.
* $(2,2,2,2)$: both vanish.

Wave-1 sweep is independently confirmed. Index-direction separation
$(a+p-1,b+q-1)-(a-p+1,b-q+1)=2(p-1,q-1)$ is unbounded as $p,q$ grow.

---

## §2. New diagnostic — sign-flip / Matlis-residue equivalence

**The obstruction is not Lie-module-structural; it is a support /
lattice positivity obstruction.**

Define $\sigma:(a,b)\mapsto(-a-1,-b-1)$. Symbolically:

$$
F_{p,q}\bigl(\widetilde\Psi_{-a-1,-b-1}\bigr)
=-(pb-qa+p-q)\,\widetilde\Psi_{-a-1+(p-1),\,-b-1+(q-1)}.
$$

Apply $\sigma^{-1}$: the shift in the $\rho$-frame is $(a-p+1,b-q+1)$,
exactly the coadjoint shift; the coefficient $-(pb-qa+p-q)$ is exactly
the coadjoint coefficient.

**Conclusion.** Under $\sigma$, PBW raising and Matlis coadjoint are
the **same formula**. The two realizations $\widetilde\Psi_{a,b}$ and
$\rho_{a,b}$ (both indexed by $a,b\geq0,a+b>0$) are not different
$\mathfrak h$-modules; they are two **positive cones** of a single
bi-infinite formula on $\Z^2$, sitting on opposite sides. This is the
Matlis-duality statement of `\prop:app-matlis-realization` read at the
level of structure constants.

**Consequence for Obligation II.** The honest question is not "find a
flat $D_\hbar$-deformation between PBW and coadjoint" — there is no
such deformation in the Lie-module sense, because they are not modules
of a deformation parameter; they are modules over a residue duality.
The honest question is: in which category does there exist an object
realizing the bi-infinite Lie module on $\Z^2$, restricting to PBW on
$\Z_{\geq0}^2$ and to Matlis coadjoint on $\Z_{<0}^2$?

Constructions of bi-infinite objects exist (local cohomology
$H^2_{\mathfrak m}(R)$, Cech complexes of $D_\hbar$-modules), but each
carries an additional structure (multiplication action of $z_i$, not
vector-field action) that ruins the Lie-module match. This is W4-01,
W4-02 below.

---

## §3. Master ledger entries — W4 wave-2 attacks

### W4-01 — Derived $D_\hbar$-modules / Kashiwara–Schapira derived category

**Severity 4. Verdict FORBIDDEN.**

**Candidate.** $M_\hbar^\bullet \in D^b_h(D_\hbar\text{-mod})$ on
$\C^2$ with $H^0$ giving PBW and $\hbar$-localization giving Matlis.

**Broken step.** "$z_i$ acts as Hamiltonian vector field" is a
Lie-module condition over $\bar A$, not a $D_\hbar$-module condition
(where $z_1$ acts by polynomial multiplication). Embedded no-go
`\thm:no-polynomial-realization-categorical` applies pointwise: for
$X_{z_1}=\partial_{z_2}$ to be locally nilpotent on PBW shadow but
unbounded on coadjoint module is a Lie-level fact, not a multiplication
fact.

The natural $D_\hbar$-module $H^2_{\mathfrak m}(R)$ realizes
$\rho_{a,b}=z_1^{-a-1}z_2^{-b-1}\,dz_1dz_2$ with multiplication action
$z_1\cdot\rho_{a,b}=\rho_{a-1,b}$ — not the Matlis coadjoint
(raising the second index). Multiplication and coadjoint are residue-dual,
not equivalent.

**Derived enhancement does not help.** Shifts and resolutions act on
chain-level structure, not on zero-mode Lie module action. **Confidence
high. Blast radius:** all $D^b_h(D_\hbar\text{-mod})$ candidates.

---

### W4-02 — Microlocal / IRH / D'Agnolo–Kashiwara enhanced sheaves

**Severity 4. Verdict FORBIDDEN.**

**Candidate.** Kashiwara–Schapira microsheaf with singular support
along the brane conormal $T^*_{\{z_1=z_2=0\}}\C^2$, or its
D'Agnolo–Kashiwara IRH enhancement.

**Broken step.** The natural microlocal candidate is $B_{0|\C^2}=
D_\hbar/D_\hbar(z_1,z_2)$ — the Fourier delta lattice. Action:
$z_1\cdot(\partial_1^a\partial_2^b e_0)=-\hbar\,a\,
\partial_1^{a-1}\partial_2^b e_0$, lowering the first index by 1
(multiplication action on Cech-Fourier basis). At $\hbar=0$: trivial.
Generic fibre: same with $\hbar$ invertible. Neither matches PBW
raising on $\widetilde\Psi$ ($z_1$ as $\partial_{z_2}$) nor Matlis
coadjoint on $\rho$ ($z_1$ as second-index raising).

IRH operates on $D_\hbar$-modules treating $z_i$ as multiplication;
singular-support calculus refines the microlocal structure of
multiplication operators, cannot replace them by Hamiltonian vector
fields. **Confidence high. Blast radius:** all microsheaf and IRH
candidates at the brane conormal.

---

### W4-03 — Beilinson–Drinfeld chiral / Poisson-vertex algebras

**Severity 4. Verdict FORBIDDEN (by Verma reduction).**

**Candidate.** Chiral algebra $\mathcal A_\hbar$ over $\mathbb A^1_\hbar$
in the BD sense, with stalk at $\hbar=0$ equal to the chiral PBW
$V_0(\bar A)$.

**Broken step.** By Frenkel–Ben-Zvi vertex PBW, any chiral algebra with
$\hbar=0$ stalk equal to $S(\bar A)$ is the chiral universal envelope
$V_\hbar(\bar A)$. Modules split into:
* **Vacuum / induced** (PBW): positive-mode generators locally
  nilpotent on $S(\bar A_-)$.
* **Verma** (coadjoint): positive-mode generators with non-trivial
  higher composites; underlying space is the Matlis dual of a Borel.

These are *two different module classes* of the same chiral algebra,
not specializations of one $\hbar$-flat object. Etingof–Frenkel–Kac on
affine Kac–Moody at integer levels: vacuum and Verma are
non-isomorphic at every level. The same triangular-decomposition
obstruction applies here at the zero-mode level.

The $\hbar$ parameter deforms the chiral *bracket* (Poisson-vertex
to Lie-vertex), not the Lie module structure. **Confidence high.
Blast radius:** all BD chiral and Poisson-vertex candidates with PBW
$\hbar=0$ stalk.

---

### W4-04 — Costello–Gwilliam factorization $D_\hbar$-bimodules

**Severity 4. Verdict FORBIDDEN.**

**Candidate.** A Costello–Gwilliam factorization algebra with
$\hbar$-Rees deformation of the OPE, with brane-stalk module fibres.

**Broken step.** Costello–Gwilliam parametrizes the operator product
over spacetime; $\hbar$ deforms the OPE / Lie bracket of currents at
coinciding support. The module structure on a factorization-stalk
module is fixed by the Lie algebra structure of currents at coinciding
support, not by $\hbar$. Bracket-deforming $\bar A$ to Moyal at
$O(\hbar^2)$ does not produce a flat family of *modules* of $\bar A$.
The PBW vs coadjoint distinction is module-level; factorization
deformation is bracket-level. **Confidence high. Blast radius:** all
Costello–Gwilliam factorization $D_\hbar$-bimodule candidates.

---

### W4-05 — Host category $\mathsf P_{\mathrm{pol}}$ and Tate enlargement

**Severity 3. Verdict no-go extends to Tate-completed PBW shadow.**

The embedded no-go `\thm:no-polynomial-realization-categorical` lives
in the abelian category $\mathsf P_{\mathrm{pol}}$ of $\Z$-graded
bimodules over $\bar A$ with locally nilpotent linear-Hamiltonian
action. Question: does Tate-completed
$S^{\mathrm{Tate}}(\bar A_{\mathrm{desc}})$ live inside $\mathsf
P_{\mathrm{pol}}$, or in a strictly larger category that escapes the
no-go?

**Tate enlargement.** Replace literal local nilpotence by:

* **(2-Tate).** Every $m\in M$ has a Tate window $F^N\subset M$ such
  that $z_i^k m\in F^N$ for $k$ large.

PBW shadow on $\widetilde\Psi$ satisfies (2-Tate) under any standard
weight Tate window: raising preserves the bidegree cone and pushes
elements into deeper windows. Define $\mathsf P^{\mathrm{Tate}}_{\mathrm{pol}}$
as Tate-topological $\bar A$-modules satisfying (2-Tate). Tate-completed
$S^{\mathrm{Tate}}(\bar A_{\mathrm{desc}})$ lives **inside** this
category.

**$\mathcal P$ does not enter $\mathsf P^{\mathrm{Tate}}_{\mathrm{pol}}$.**
Matlis coadjoint raises $\rho_{a,b}$ to $\rho_{a,b+k}$; second index
$b+k$ grows outside every fixed Tate window with bounded total degree.
Embedded no-go extends verbatim with "Tate-continuous local
nilpotence" replacing "local nilpotence."

**Confidence high. Blast radius:** Tate-topological enlargements of
PBW shadow do not host $\mathcal P$ as a Lie module.

---

### W4-06 — Universal categorical no-go (consolidation)

**Severity 5. Verdict UNIVERSAL.**

**Theorem (W4 universal categorical no-go).** Let $\mathcal C$ be any
$\C[[\hbar]]$-linear additive category with a forgetful functor
$\mathcal C\to\bar A_\hbar$-Lie-Mod. Suppose $M_\hbar\in\mathcal C$
satisfies $M_\hbar/(\hbar)\cong\bar A_{\mathrm{desc}}$ as PBW Lie module
and $M_\hbar[\hbar^{-1}]\cong\mathcal P((\hbar))$ as Matlis Lie module
under the forgetful functor. Then $M_\hbar$ does not exist in any of:

1. $D^b_h(D_\hbar\text{-mod})$ (Kashiwara–Schapira).
2. BD chiral algebras over $\mathbb A^1_\hbar$ (W4-03).
3. Costello–Gwilliam factorization with $\hbar$-Rees deformation (W4-04).
4. Kashiwara–Schapira microsheaves at the brane conormal, including
   D'Agnolo–Kashiwara IRH enhancements (W4-02).
5. Any $D_\hbar$-module subcategory with multiplication action of $z_i$
   (W4-01).
6. Any Tate-topological enlargement satisfying Tate-continuous local
   nilpotence (W4-05).

**Proof sketch.** All six factor through Lie-Mod $\bar A_\hbar$:
* **Multiplication-action categories** (1, 2, 4, 5): $z_i$ acts by
  polynomial multiplication, locally nilpotent on bounded-pole-order
  representatives. Coadjoint generic fibre is not locally nilpotent;
  21-case sweep at $(p,q)=(2,1)$ exhibits the explicit numerical
  mismatch.
* **Lie-module / Tate categories** (5, 6): both fibres are Lie modules
  but with opposite raising/lowering directions; categorical no-go
  applies, extends Tate-continuously (W4-05).
* **Factorization / chiral** (2, 3): $\hbar$-parameter at bracket-deformation
  level, not module-deformation level.

The obstruction is at the Lie-module level: PBW raising and Matlis
coadjoint are related by **residue duality** (sign-flip relabel), not
by deformation. Categorical enrichments factor through Lie-Mod and
inherit the obstruction.

**Confidence high.**

---

## §4. Residue-duality reframing

Define the bi-infinite Lie module $\bar M$ of $\bar A$ on $\Z^2$ by

$$
z_1^pz_2^q\cdot v_{a,b}=(pb-qa-(p-q)\cdot\mathbf 1[a<0])\,v_{a+p-1,b+q-1}.
$$

(Same $(pb-qa)$ raising on both half-planes, with $-(p-q)$ correction
crossing the sign-flip boundary.) Then:

* $\bar M^+=\bigoplus_{a,b\geq0,a+b>0}\C\cdot v_{a,b}\cong\bar A_{\mathrm{desc}}$.
* $\bar M^-=\bigoplus_{a,b<0}\C\cdot v_{a,b}\cong\mathcal P$ via
  $v_{-a-1,-b-1}=\rho_{a,b}$.

Residue pairing is the canonical $\bar M^+\otimes\bar M^-\to\C$.

**Implications.**
* No flat-deformation interpolation exists between $\bar M^+$ and
  $\bar M^-$: they are *disjoint subobjects*, not specializations.
* Categorical obligations are well-formulated only at the level of
  $\bar M$, not at sub-cones.
* Wave-1 healed Obligation II is correct in spirit but its language
  ("$\hbar$-flat family") is wrong. The right language is
  "submodule decomposition of a bi-infinite parent."

**This is the genuine platonic structure** behind the manuscript's
$\Psi$/$\rho$ duality: the parent object is not an interpolation; it
is the bi-infinite local-cohomology module before symmetric-residue
splitting.

---

## §5. Two narrow open avenues

W4-06 closes the four named categorical extensions of M-02. Two narrow
avenues lie outside the named list and remain open:

**(R-W4-A) Bi-infinite local-cohomology realization.** Define unreduced
parent

$$
\widetilde{\mathcal M}=H^0\bigl(\C^2\smallsetminus\{0\},\mathcal O\bigr)\big/\mathcal O(\C^2)\,dz_1dz_2.
$$

The PBW $\bar A$-module $\bar A_{\mathrm{desc}}$ is *not* canonically
embedded — the Hamiltonian vector-field action does not preserve any
Cech splitting. Whether a Hamiltonian-equivariant splitting / lift
exists is open.

**(R-W4-B) Bi-residue $L_\infty$-categorified bracket.** A Tamarkin /
Kontsevich-style $L_\infty$ deformation of $\bar A$'s Lie bracket
allowing higher Massey-product corrections that interpolate raising
and lowering directions. No construction is known.

Both lie outside W4-06; neither is known to admit a candidate. Verdict
**open**, Phase 4.

---

## §6. Honest verdict on Obligation II

**Every named categorical extension in M-02's residual is FORBIDDEN by
W4-06.** The conflict is at the Lie-module level: PBW raising and
Matlis coadjoint are residue-dual, not deformation-related.
Categorical enrichments (derived, microlocal, factorization, Tate,
chiral) factor through Lie-modules and inherit the obstruction.

**The honest physical content of Obligation II's residual is the
bi-infinite parent / residue duality of §2 and §4**, not an $\hbar$-flat
deformation. The wave-1 heal language ("$\hbar$-flat module" with two
specializations) needs to be replaced by the residue-duality language.

Two speculative residuals (R-W4-A, R-W4-B) outside the named
categories; neither known to admit a candidate.

This is a strict sharpening of M-02 (the open question is now narrower
and conceptually corrected), not a downgrade.

---

## §7. Sharpened Obligation II text

Replacement for `open-obligations.tex` 159–180 and Obligation II in
`platonic-ideal-plan-2026-04-28.md` §4:

> **Obligation II (W4-sharpened).** The maximal honest comparison
> between $\bar A_{\mathrm{desc}}$ and $\mathcal P$ is the
> *residue-duality* sign-flip relabel
> $\widetilde\Psi_{a,b}\leftrightarrow\widetilde\Psi_{-a-1,-b-1}=\rho_{a,b}$
> under which the Hamiltonian PBW raising formula and the Matlis
> coadjoint lowering formula are formally identical. The two
> realizations are not specializations of one $\hbar$-flat module; they
> are the positive and negative cones of a bi-infinite Lie module of
> $\bar A$ on $\Z^2$, related by residue duality, not deformation. The
> Fourier–Rees label bridge of `\thm:app-matlis-rees-fourier-bridge`
> records this duality at the level of bookkeeping.
>
> The 21-case sweep at $(p,q),(a,b)\in[0,3]^2$ exhibits structural
> index-direction conflict on the positive cone alone: PBW raising
> sends $(a,b)\mapsto(a+p-1,b+q-1)$, coadjoint lowering sends
> $(a,b)\mapsto(a-p+1,b-q+1)$, separating by $2(p-1,q-1)$. The
> separation vanishes only in the bi-infinite parent.
>
> No $\mathfrak h_\hbar$-equivariant Rees-flat candidate $M_\hbar$
> exists in any of: $D^b_h(D_\hbar\text{-mod})$; BD chiral algebras
> over $\mathbb A^1_\hbar$; Costello–Gwilliam factorization with
> $\hbar$-Rees deformation; Kashiwara–Schapira microsheaves at the
> brane conormal $T^*_{\{z_1=z_2=0\}}\C^2$ including D'Agnolo–Kashiwara
> IRH enhancements; any Tate-topological enlargement satisfying
> Tate-continuous local nilpotence.
>
> The structural obstruction is at the Lie-module level: the five
> categories above have forgetful functors to $\bar A_\hbar$-Lie-Mod
> and inherit the residue-duality obstruction.
>
> Open: whether bi-infinite local-cohomology realization (R-W4-A) or
> categorified $L_\infty$-deformation (R-W4-B) could carry both cones
> equivariantly inside a single Lie module. Both lie outside the named
> five categories.
>
> **Verification standard.** Any future proposal must be tested
> against the 21-case sweep at $(p,q)\in\{(1,1),(2,1),(1,2),(2,2),(3,3)\}$
> and $(a,b)\in[0,3]^2$, exhibiting equivariant matching of both
> coefficient and bidegree label.

---

## §8. Implementation suggestions

* `open-obligations.tex` 159–180: replace with §7 text.
* New `\thm:universal-categorical-no-go` in
  `appendix-matlis-principal-parts.tex` after the Fourier–Rees bridge:
  W4-06 statement; proof reduces all five named categories to Lie-module
  residue-duality obstruction.
* New `\rmk:residue-duality-bi-infinite-parent` after
  `\thm:app-matlis-no-polynomial-realization`: bi-infinite parent
  realization of §2 makes the PBW/coadjoint duality an instance of
  residue duality, not deformation.
* `scripts/check_one_psi_homology.py`: extend
  `check_no_hbar_deformation_of_label_projection` with explicit symbolic
  verification of the §2 sign-flip diagnostic.
* Cross-link `platonic-ideal-plan-2026-04-28.md` §4 to the new theorem
  and remark.

---

## §9. Residuals (not closed by this wave)

* **R-W4-A.** Bi-infinite local-cohomology Hamiltonian-equivariant
  splitting / lift — Phase 4.
* **R-W4-B.** $L_\infty$-categorified bracket deformation bridging
  raising and lowering — Phase 4.
* **R-W4-C.** Obligation I (unreduced BV factorization-centre lift):
  the bi-infinite parent of §2 may suggest a hint — unreduced BV
  currents pair against bi-infinite test sections, splitting into PBW
  polynomial pieces and Matlis coadjoint distributional pieces by
  residue duality, not deformation.

---

## §10. Convergence verdict

W4 closes the wave-2 attack on M-02's residual:

* All four named extensions FORBIDDEN by W4-06.
* Tate enlargement also forbidden (W4-05).
* Two open speculative residuals (R-W4-A bi-infinite parent; R-W4-B
  $L_\infty$ bracket) outside the named list.
* Sharpened Obligation II text in §7, ready for inscription.
* New conceptual reframing in §2/§4: the obstruction is residue
  duality, not deformation; the bi-infinite parent module is the
  genuine platonic structure.

Wave 1's M-02 said "categorical extension is open." W4 tightens this
to: *every named categorical extension is forbidden by a universal
Lie-module-level residue-duality obstruction; only narrow non-named
constructions (bi-infinite parent, $L_\infty$-bracket) remain open.*

The manuscript's existing prose around the Fourier–Rees bridge and the
no-polynomial-realization theorem is structurally correct; W4 sharpens
the Obligation II language to make the residue-duality content
explicit, rather than describing it as "$\hbar$-flat interpolation."

---

## §11. Provenance

* 21-case sweep verification independently reproduced
  (`/tmp/w4_independent_sweep.py`, scratch). Confirms wave-1 A4: zero
  label+coefficient matches off $(p,q)=(1,1)$; at $(1,1)$ labels match
  but coefficients sign-opposite (PBW $(b-a)$ vs coadjoint $-(b-a)$).
* Sign-flip / residue-duality diagnostic in §2 is new in this wave.
  Verified symbolically: under $\widetilde\Psi_{a,b}\leftrightarrow
  \widetilde\Psi_{-a-1,-b-1}$, PBW raising and Matlis coadjoint
  formulas coincide as bi-infinite formulas (`/tmp/w4_signflip.py`,
  scratch).
* Categorical attacks (W4-01–W4-05) verified via structural arguments
  using `\thm:no-polynomial-realization-categorical`,
  `\thm:no-hbar-primitive-descendant-intertwiner`,
  `\thm:app-matlis-rees-fourier-bridge`, plus standard
  Beilinson–Drinfeld / Kashiwara–Schapira / D'Agnolo–Kashiwara IRH /
  Costello–Gwilliam frameworks. BD chiral analysis uses
  Frenkel–Ben-Zvi vertex PBW (vacuum vs Verma triangular decomposition).
* Cross-links to wave 1: M-02, M-04, M-25.
* No web search invoked.

---

End of W4 ledger.
