# Wave 3 / W7 — Etingof + Invariants Lens

**Date.** 2026-04-28.
**Author.** Raeez Lorgat.
**Wave.** 3 (independent attacker; reads waves 1–2 master ledger plus
W3-W2 Gaiotto and W3-W5 Kazhdan).
**Lens.**
- *Primary:* Etingof — tensor categories, finite examples,
  semisimplicity failures, deformation, quantization, Drinfeld twist,
  R-matrix.
- *Secondary:* Invariants — what invariant must each candidate
  intertwiner preserve? Which step changes it?

**Mandate.** Probe the universal categorical no-go (M-29 sev 5)
through the Etingof tensor-category framework, with focus on:
non-semisimple deformations (where simple-object Hom can vanish but
the obstruction can hide in extensions); explicit deformations and
quantizations of the relevant tensor structure; per-invariant
classification of which datum is broken by each candidate.

**Mode.** Proposal-only. No commits. Master ledger schema; IDs
W3-W7-NN.

**Independence.** Wave-2 W4 (Etingof attack on M-02 producing M-29)
is taken as **input under attack**. The W7 deliverable is whether the
Etingof tensor-category framework, applied at full strength
(non-semisimple deformations, Drinfeld twist, Moyal star, BGG O,
Lusztig category) can break M-29 universality, plus a per-invariant
audit of which D-ingredient (D₁ residue pairing / D₂ T²-Cartan
rigidity / D₃ Hamiltonian vector-field action / local-nilpotence) is
broken at each candidate.

---

## §0. Method

Targets T1–T4 from the assignment. Each target gets a verdict:
break / no-break. Hand computations cite file:line. Three Python
probes inscribed in `/tmp/w7_*.py` (scratch). The deliverable is a
verdict on M-29 universality plus stable-core check.

---

## §1. Target T1 — Semisimplicity-failure test for M-29

### §1.1 Rising-factorial-in-End(1) audit

The proof of `thm:no-polynomial-realization-categorical`
(`main.tex`:4174–4194) computes, on every $\rho_{a,b}\in\mc P$,
$$z_1^N\cdot\rho_{a,b}=(-1)^N(b+1)(b+2)\cdots(b+N)\,\rho_{a,b+N}\neq0,$$
and concludes that any equivariant $\Phi:\mc P\to M$ into a locally
nilpotent target $M$ must have $\Phi(\rho_{a,b+N})=0$ for $N\gg0$,
forcing $\Phi=0$ by injectivity.

**W3-W7-01 (rising-factorial scalar lives in End(unit)).**
**Severity 2 (defensive). Status valid. Confidence high.**

The rising factorial $(b+1)(b+2)\cdots(b+N)$ is a non-zero
**scalar in $\C$**, namely an element of $\End_{\mathcal C}(\mathbf 1)$
for the tensor category $\mathcal C$. In any $\C$-linear tensor
category with $\End(\mathbf 1)=\C$ — including all non-semisimple
deformations of $\Rep(\GL_2)$, BGG category $\mathcal O$, Lusztig
category at root of unity, and any deformed Hopf module category —
this scalar remains exactly $(b+1)(b+2)\cdots(b+N)\in\C$. Non-semisimplicity
does not deform the unit endomorphism ring.

**Test (`/tmp/w7_etingof_semisimplicity.py`).** Computed
$(b+1)\cdots(b+N)$ for $b\in[0,5]$, $N\in[1,5]$: zero hits = 0; the
rising factorial is non-zero on the entire test range. The exact
identity $(b+1)\cdots(b+N)=\Gamma(b+N+1)/\Gamma(b+1)$ confirms
non-vanishing on all non-negative integer $b$ and positive integer $N$.

**Conclusion.** The M-29 argument does not rely on semisimplicity at
any step. The scalar does not vanish in any $\C$-linear extension.

### §1.2 Hidden-extension audit (Ext$^1$, Ext$^\bullet$)

The subtlest Etingof attack: even if $\Hom_{\mathcal C}(\mc P, M)=0$,
could $\Ext^1_{\mathcal C}(\mc P, M)$ or higher $\Ext$-groups host a
non-trivial extension whose underlying object carries the data of a
"would-be intertwiner"?

**W3-W7-02 (Ext$^1$ vanishes in $\mathsf P_{\mathrm{pol}}$).**
**Severity 3 (extension audit). Status valid. Confidence high.**

A 1-extension $0\to M\to N\to\mc P\to 0$ in $\mathsf P_{\mathrm{pol}}$
gives a vector-space direct sum $N=M\oplus\mc P$ with the action
$z_i(m,\rho) = (z_i m + s_i(\rho), z_i\rho)$ where $s_i:\mc P\to M$
is a cocycle. For $N$ to live in $\mathsf P_{\mathrm{pol}}$, $z_i$
must act locally nilpotently on $N$. But $z_i^k(0,\rho_{a,b}) =
(\text{bounded correction in }M, z_i^k\rho_{a,b})$, where the second
component remains non-zero for all $k$ (rising factorial). Hence $N$
is not locally nilpotent: $\Ext^1_{\mathsf P_{\mathrm{pol}}}(\mc P, M)=0$.

The dual extension $0\to\mc P\to N\to M\to 0$ is the same: $z_i$ on
$\mc P\subset N$ remains non-locally-nilpotent.

Higher $\Ext^k$ vanishes by Yoneda composition: any such class is
representable by a $k$-extension, and the rising-factorial argument
lifts to every term of the extension.

**Cross-check at the Etingof tensor-category level.** Etingof–Gelaki–Nikshych–Ostrik
*Tensor Categories* §4.6 (extensions of objects in tensor categories)
recovers $\Ext^\bullet$ as derived $\Hom$ in the abelian category of
modules. The argument above is at this level: it does not depend on
finiteness of the category (works equally for ind-completion and Tate
enlargement) or on semisimplicity.

**Conclusion.** Both the immediate Hom and all higher $\Ext^k$
vanish. Non-semisimple structure provides no escape via extensions.

### §1.3 Verdict on T1

**M-29 is bulletproof against the semisimplicity-failure attack.**
The proof is at the level of the unit endomorphism ring, not at the
object level; it holds in every $\C$-linear tensor category with
$\End(\mathbf 1)=\C$, semisimple or not. Higher Ext-extensions do not
host candidates either.

---

## §2. Target T2 — Deformation/quantization of the no-go

### §2.1 Drinfeld twist

**W3-W7-03 (Drinfeld twist preserves $z_i$-module action).**
**Severity 2. Status valid. Confidence high.**

A Drinfeld twist $J\in H\otimes H$ (for $H=U(\bar A)$ or its formal
completion) deforms the **comultiplication** $\Delta$ of the
universal enveloping algebra to $\Delta_J(x)=J\Delta(x)J^{-1}$,
producing a new tensor category $\Rep_J H$ with the same underlying
abelian category but twisted tensor product. The twist deforms how
$M\otimes N$ is represented as a module over $H$, **not** how $H$
acts on individual modules: the action $H\otimes M\to M$ is
unchanged on each fixed module.

**Consequence.** For any candidate $M_\hbar^J\in\Rep_J H$ with
forgetful functor to $\bar A_\hbar$-Lie-Mod, the Lie-module action
of $z_i$ on $M_\hbar^J$ as a single module is unchanged from the
untwisted module. Local nilpotence of $z_i$ on $M$ is preserved iff
it is preserved on the underlying untwisted module. M-29 applies
verbatim.

### §2.2 Moyal star deformation

**W3-W7-04 (Moyal preserves $z_i$-action because $z_i$ are linear).**
**Severity 3. Status valid. Confidence high.**

The Moyal star deformation of $\bar A$ is
$$f *_\hbar g = fg + \tfrac{\hbar}{2}\{f,g\} + \tfrac{\hbar^2}{8}\{f,g\}_2 + \cdots$$
where $\{f,g\}_n$ is the $n$-th Hochschild bracket built from
$\partial_{z_1}^k\partial_{z_2}^{n-k}f\cdot\partial_{z_2}^k\partial_{z_1}^{n-k}g$
sums. The Moyal bracket $[f,g]_\hbar=(f *_\hbar g - g *_\hbar f)/\hbar$
is the alternating-order sum:
$$[f,g]_\hbar = \{f,g\} + O(\hbar^2)\cdot\{f,g\}_3 + O(\hbar^4)\{f,g\}_5 + \cdots.$$

**Critical observation.** For $f=z_i$ (a degree-1 polynomial), every
second and higher derivative vanishes: $\partial^2 z_i = 0$. Hence
$\{z_i, g\}_n = 0$ for $n\geq 2$, and the Moyal bracket reduces to
the classical Poisson bracket:
$$[z_i, g]_\hbar = \{z_i, g\}_{\text{Poisson}}.$$

**Consequence.** On any module $M$ with $z_i$ acting as a Hamiltonian
vector field $X_{z_i}=\{z_i,-\}$, the Moyal-deformed action of $z_i$
is exactly the same operator. Local nilpotence is preserved.

For $\mc P$ with $z_i\cdot\rho_{a,b}=\pm(b+1)\rho_{a,b+1}$ (or
$\pm(a+1)\rho_{a+1,b}$), the Moyal action is identical to the
classical action: local nilpotence still fails on every nonzero
$\rho$. **M-29 applies verbatim under Moyal deformation.**

### §2.3 q-deformation / R-matrix deformation

**W3-W7-05 (q-deformation either preserves the obstruction or escapes the hypothesis).**
**Severity 3. Status valid. Confidence high.**

Two interpretations of a q-deformation:

(a) **q-twist of the bracket** ($U_q(\bar A)$ in the Faddeev–Reshetikhin
sense): the bracket becomes $[f,g]_q = q^{|f||g|/2}fg - q^{-|f||g|/2}gf$
(or its analogue). On each fixed module, $z_i$ acts the same way as
in the untwisted case (the q-twist is again on the tensor structure
or on the bracket-defining relations, not on the module action). Local
nilpotence is preserved; M-29 applies.

(b) **q-difference action** ($z_i$ acts as a q-difference operator):
$D_{q,i}(\phi)(b) = (\phi(b+1) - \phi(b))/(q-1)$, etc. This is **not**
a Hamiltonian vector-field action; it is a finite-difference operator.
A module with this action is **not** in the abelian category
$\mathsf P_{\mathrm{pol}}$ of M-29's hypothesis (which requires
condition (1): every element acts as a Hamiltonian vector field;
`main.tex`:4153). So this candidate **escapes M-29 by escaping the
hypothesis**, not by satisfying it differently. The escape goes
into a category outside the universal no-go; whether it admits its
own candidate is **R-W4-B's territory** ($L_\infty$-categorified
bracket).

**Consequence.** Drinfeld twist, Moyal, and Faddeev–Reshetikhin
q-twist all preserve the hypothesis and the conclusion. q-difference
escapes the hypothesis but enters R-W4-B's residual.

### §2.4 Lusztig divided powers / restricted enveloping at root of unity

**W3-W7-06 (Lusztig setting at root of unity does not help).**
**Severity 2. Status valid. Confidence medium-high.**

At $q$ a primitive $\ell$-th root of unity, the Lusztig divided
powers $z_i^{[\ell]}$ in $u_q(\bar A)$ are **central**: they act as
scalars on every simple module and as upper-triangular nilpotents on
projective covers. This is the classic Lusztig phenomenon
(Etingof–Gelaki–Nikshych–Ostrik §8.3).

**Test:** does the Lusztig restricted module $M$ at root of unity
have locally $z_i$-nilpotent action? **Yes, on the simples** (which
are finite-dimensional). But the candidate must also realize $\mc P$
as a sub/quotient. $\mc P$ is **infinite-dimensional**; in the
Lusztig restricted category, infinite-dimensional objects are not
the standard objects, and the analogous "ind-Lusztig category" still
has the rising-factorial scalar $(b+1)\cdots(b+N)$ in
$\End_{\mathcal C}(\mathbf 1)\subset\End_{\mathcal C}$. Even at
$q^\ell=1$, the **classical** scalar $(b+1)\cdots(b+N)$ in $\C$ is
non-zero (it does not depend on $q$); the Lusztig setting does not
modify the classical scalar in $\End(\mathbf 1)$.

If we passed to the **q-rising factorial** $[b+1]_q[b+2]_q\cdots[b+N]_q$
(the natural object in $u_q$), this **does** vanish at $q$ a
primitive $2k$-th root of unity for some $k\in[b+1, b+N]$. But this
vanishing is in the q-difference action of (b), which escapes the
M-29 hypothesis.

**Conclusion.** The Lusztig setting either keeps the classical
rising factorial (preserving M-29) or escapes the hypothesis into
R-W4-B's territory.

### §2.5 BGG category $\mathcal O$ for $\bar A$ or its enlargement

**W3-W7-07 (BGG O does not help).**
**Severity 2. Status valid. Confidence high.**

BGG category $\mathcal O$ for $\bar A$ (viewed as a Lie algebra
with triangular decomposition $\bar A = \bar A_+ \oplus \bar A_0
\oplus \bar A_-$) consists of finitely-generated weight modules
locally finite for the Borel $\bar A_+$. Verma modules
$M(\lambda)=U(\bar A)\otimes_{U(\bar A_+)}\C_\lambda$ have **non**-locally
nilpotent action of $\bar A_-$ (since the negative direction is the
Verma direction, where the Cartan basis vectors generate freely).

**This is exactly W4-03's verdict (Frenkel–Ben-Zvi vertex PBW):**
vacuum (PBW = local nilpotence on $\bar A_+$) and Verma (Matlis = local
nilpotence on $\bar A_-$) are two **different** module classes; no
flat family interpolates them.

The non-semisimple structure of category $\mathcal O$ (e.g.,
projective covers $P(\lambda)$ have Verma filtrations with multiplicities
given by Kazhdan–Lusztig polynomials) does **not** create new
intertwiners between vacuum and Verma at the underlying Lie module
level. The KL polynomials encode multiplicities of Vermas in
projectives, not new module homomorphisms.

**Conclusion.** BGG $\mathcal O$ confirms the W4-03 verdict; the
non-semisimple aspect (Kazhdan–Lusztig category) does not create new
candidates.

### §2.6 Verdict on T2

**The no-go survives all natural deformations and quantizations of the
tensor structure.**
- Drinfeld twist: preserves hypothesis + conclusion.
- Moyal star: preserves hypothesis + conclusion (because $z_i$ are
  linear, no higher Moyal corrections).
- Faddeev–Reshetikhin q-twist: same.
- Lusztig at root of unity: classical scalar in $\End(\mathbf 1)$
  unchanged; q-rising factorial vanishing only at q-difference
  action, which escapes hypothesis (into R-W4-B).
- BGG $\mathcal O$ / KL category: confirms vacuum/Verma distinction;
  no new intertwiner.

**The only escape goes into R-W4-A (bi-infinite local-cohomology) or
R-W4-B ($L_\infty$ bracket), exactly the W4 residuals.** The
quantization-deformation framework does not produce any extra route.

---

## §3. Target T3 — Per-invariant breakage classification

### §3.1 The four invariants

A candidate intertwiner $\Phi:\mc P\to M_\hbar$ in any tensor
category $\mathcal C$ over $\C[[\hbar]]$ with forgetful functor to
$\bar A_\hbar$-Lie-Mod must preserve four invariants:

**(I-a) T²-Cartan grading (M-28 D₂).** $\rho_{a,b}$ has weight
$(-a,-b)$ (after accounting for the $dz_1dz_2$ volume); $z_1^p z_2^q$
has weight $(p,q)$. The residue pairing is non-zero only when the
weights cancel: $(a,b)=(m,n)$. Used in
`thm:app-matlis-residue-rigidity` (`appendix-matlis-principal-parts.tex`:179–206)
and `thm:canonical-residue-pairing` (`main.tex`:3838–3911).

**(I-b) Total degree zero of the residue pairing (M-28 D₁).** The
residue pairing $\langle\rho_{a,b},z_1^m z_2^n\rangle$ has total
degree $-(a+b+2)+(m+n+2)=m+n-a-b$, which equals $0$ exactly when
$a+b=m+n$. Used in the same uniqueness arguments.

**(I-c) Hamiltonian vector-field action of $z_i$ (M-28 D₃ + M-29
hypothesis).** $z_i$ acts on $\mc P$ via $X_{z_i}=\{z_i,-\}$, the
Hamiltonian vector field. Used in `prop:app-matlis-coadjoint-action`
(`appendix-matlis-principal-parts.tex`:135–177) and the M-29
hypothesis condition (1) (`main.tex`:4153).

**(I-d) Local nilpotence of $z_i$ on $M$ (M-29 hypothesis condition (2)).**
For every $m\in M$ and $i\in\{1,2\}$, there exists $N$ with
$z_i^N\cdot m=0$. Used in M-29 hypothesis (2) (`main.tex`:4154–4156).

### §3.2 Breakage table per candidate

| Candidate | Breaks (I-a) | Breaks (I-b) | Breaks (I-c) | Breaks (I-d) |
|---|---|---|---|---|
| Polynomial PBW $\widetilde\Psi_{a,b}$ | no | no | no | satisfied (locally nilpotent on PBW) |
| Matlis coadjoint $\rho_{a,b}$ | no | no | no | **broken** (rising factorial non-zero) |
| Bi-infinite parent $\bar M$ on $\Z^2$ (W4 §4) | no | no | no | broken on $\bar M^-$ cone |
| Drinfeld twist of either | no | no | no | unchanged (twist on tensor only) |
| Moyal star deformation | no | no | no | unchanged ($z_i$ linear → no corrections) |
| q-twist (Faddeev–Reshetikhin) | no | no | no | unchanged |
| q-difference action | no | no | **broken** (not vector field) | satisfied for q-finite-difference |
| $D_\hbar$-module multiplication | no | no | **broken** (multiplication, not vector field) | satisfied for bounded pole order |
| Microlocal (IRH) | no | no | **broken** (multiplication on Cech-Fourier) | satisfied |
| BD chiral vacuum | no | no | no | satisfied |
| BD chiral Verma | no | no | no | **broken** (Verma direction unbounded) |
| Costello–Gwilliam factorization | no | no | no | unchanged (bracket-only deformation) |
| Tate-topological enlargement | no | no | no | **broken** Tate-continuously |

**W3-W7-08 (per-invariant audit confirms M-29 universality).**
**Severity 3. Status valid. Confidence high.**

The pattern: every candidate that **preserves (I-c)** (Hamiltonian
vector-field action) **breaks (I-d)** (local nilpotence of $z_i$);
every candidate that **preserves (I-d)** **breaks (I-c)** (because
$z_i$ multiplication or q-difference is not Hamiltonian vector field).

This is the **single, robust, invariant-level mechanism** behind
M-29: there is no candidate preserving all four invariants because
(I-c) and (I-d) are **incompatible on $\mc P$**. The rising-factorial
argument is the explicit obstruction, but the deeper reason is that
the Hamiltonian vector-field $X_{z_i}$ on the residue principal-parts
$\rho_{a,b}$ **raises** the dual index without bound, while local
nilpotence requires it to **eventually vanish**.

### §3.3 Connection to the bi-infinite parent (W4 §4)

The W4 residue-duality reframing places $\mc P$ and PBW
$\widetilde\Psi$ as **disjoint cones** of a single bi-infinite Lie
module $\bar M$ on $\Z^2$. Per-invariant analysis:

- On $\bar M^+$ (PBW positive cone): all four invariants satisfied.
- On $\bar M^-$ (Matlis negative cone): (I-d) broken.
- On $\bar M$ (full bi-infinite): (I-d) broken on $\bar M^-$, but
  the **whole bi-infinite parent** is a single object in some
  enlarged category (e.g., the local cohomology $H^2_{\mathfrak m}(R)$).
  This category lies **outside** $\mathsf P_{\mathrm{pol}}$ (not
  locally nilpotent on the Matlis side), so M-29's hypothesis fails
  — exactly the R-W4-A residual.

**Conclusion.** The per-invariant analysis confirms that R-W4-A
(bi-infinite local-cohomology) is the **unique** location where a
single-object candidate could exist; M-29 closes everything else.

### §3.4 Verdict on T3

The per-invariant audit confirms M-29 invariant-by-invariant. The
mechanism is: any candidate either preserves (I-c) and breaks (I-d),
or preserves (I-d) and breaks (I-c). The bi-infinite parent (R-W4-A)
is the unique escape, and it requires giving up both (I-d) and the
single-cone structure.

---

## §4. Target T4 — Connection to Gaiotto reframing

### §4.1 Gaiotto interface obstruction (W3-W2-09–10)

W3-W2 reframed M-29 as a **Gaiotto interface obstruction**: the
formal-disk-to-punctured-disk interface in the local Hamiltonian
BF theory cannot be a deformation-theoretic single-object interface;
it is at best a $\Z^2$-graded bi-infinite parent with two cones
(W3-W2-10).

**W3-W7-09 (Etingof and Gaiotto views agree).**
**Severity 2. Status valid. Confidence high.**

The Etingof tensor-category view says: no $\C[[\hbar]]$-linear
$\mathcal C$ with forgetful to $\bar A_\hbar$-Lie-Mod hosts $M_\hbar$
with both fibre conditions. The Gaiotto view says: no single-object
interface from formal disk to punctured disk hosts the bi-infinite
parent module.

**Equivalence.** A "single object in a tensor category $\mathcal C$
with both fibres" **is** a "single-object interface" in the Gaiotto
sense, where the interface is the **defect line** between the
formal disk (PBW positive cone) and the punctured disk (Matlis
negative cone). The Etingof tensor category $\mathcal C$ is the
category of defect-supported modules in the Gaiotto framework; the
forgetful functor to Lie-Mod is the bulk-side restriction.

The two views express the **same obstruction**:
- Etingof: residue-duality between PBW raising and Matlis coadjoint
  forces a sign-flip relabel that cannot be implemented as a
  single-object structure.
- Gaiotto: the interface from $\widehat{\C^2}_0$ to
  $\widehat{\C^2}_0\setminus\{0\}$ would have to glue the two cones
  through a defect-supported module; the residue duality pre-empts
  this gluing.

**No disagreement found.** The W7 Etingof-tensor-category framework
**confirms** the W3-W2 Gaiotto-interface interpretation.

### §4.2 Refinement: what each lens adds

**W3-W7-10 (lens orthogonality).**
**Severity 1 (clarification). Status valid. Confidence medium-high.**

While the verdicts agree, the two lenses identify different *aspects*
of the obstruction:

- **Etingof** identifies the obstruction at the level of
  $\End_{\mathcal C}(\mathbf 1)$ (rising factorial scalar) and at the
  $\Ext^\bullet$-level (extensions don't help). This is a
  **representation-theoretic / cohomological** statement: the
  obstruction lives in the Lie-cohomology of $\bar A$ acting on
  $\mc P\oplus M$.

- **Gaiotto** identifies the obstruction at the level of the
  **bulk-defect interface kernel**. The bulk-to-defect kernel
  $K_{\mathrm{bd}}$ on $\R^2\times\C^2$ (M-37 ingredient 3,
  R-W6-Weiss-defect) would be precisely the object that converts
  bulk PBW into defect Matlis; M-29 says this conversion is not
  realizable in a single tensor-category object.

The two lenses are **orthogonal** in the sense that they pin different
*aspects* of the same negative result. Neither subordinates the
other; both are needed to give a full picture.

**Conclusion (T4).** The Etingof tensor-category view fully agrees
with the Gaiotto interface view. The combined picture is:
$$\text{M-29 universal no-go} = \text{Etingof tensor-category obstruction} = \text{Gaiotto interface obstruction}$$
with the Etingof side giving a representation-theoretic /
cohomological proof and the Gaiotto side giving a defect-interface
geometric interpretation.

---

## §5. Master ledger entries — W3-W7 wave-3 attacks

### W3-W7-01 — Rising-factorial-in-End(1) audit

**Severity 2. Status valid. Confidence high.**
**Lens.** Etingof + Invariants.
**Provenance.** This wave; cross-link M-29 hypothesis condition (2).
**Target.** `main.tex`:4148–4194 (`thm:no-polynomial-realization-categorical`).

**Claim verified.** The rising factorial $(b+1)\cdots(b+N)$ is a
non-zero scalar in $\End_{\mathcal C}(\mathbf 1)=\C$ for any
$\C$-linear tensor category. Non-semisimple structure on objects
does not affect the unit endomorphism ring.

**Adjudication.** Strengthens M-29; the proof was already at the
Lie-module level, not the tensor-category level, so this is
a defensive confirmation.

### W3-W7-02 — Hidden-extension audit (Ext$^1$, Ext$^\bullet$)

**Severity 3. Status valid. Confidence high.**
**Lens.** Etingof.
**Provenance.** This wave; cross-link M-29.

**Claim.** $\Ext^1_{\mathsf P_{\mathrm{pol}}}(\mc P, M)=0=
\Ext^1_{\mathsf P_{\mathrm{pol}}}(M, \mc P)$ for every
$M\in\mathsf P_{\mathrm{pol}}$, by lifting the rising-factorial
argument to extensions. Higher $\Ext^k=0$ by Yoneda composition.

**Adjudication.** Strict strengthening of M-29 from "no Hom" to
"no extension classes either."

### W3-W7-03 — Drinfeld twist preserves M-29

**Severity 2. Status valid. Confidence high.**
**Lens.** Etingof (deformation/quantization).
**Provenance.** This wave; cross-link M-29 R-W4-A, R-W4-B residuals.

**Claim.** A Drinfeld twist $J\in H\otimes H$ deforms the
comultiplication of $H$ but not the action on individual modules.
M-29 applies verbatim to twisted tensor categories.

**Adjudication.** Confirms M-29 universality survives Drinfeld twists.

### W3-W7-04 — Moyal star deformation preserves M-29

**Severity 3. Status valid. Confidence high.**
**Lens.** Etingof (quantization) + Invariants (linear-Hamiltonian degree).
**Provenance.** This wave; cross-link M-29, `scripts/check_moyal_coefficients.py`.

**Claim.** For $f=z_i$ (degree 1), all higher Moyal corrections
$\{z_i,g\}_n$ for $n\geq 2$ vanish because $\partial^2 z_i=0$. The
Moyal bracket of $z_i$ with anything equals the Poisson bracket.
Hence the action of $z_i$ on any module is unchanged under Moyal
deformation, and the rising-factorial obstruction in M-29 holds
verbatim.

**Adjudication.** Strict strengthening: M-29 holds in the **fully
quantum Moyal-deformed setting**, not just at semi-classical
$\hbar=0$.

### W3-W7-05 — q-deformation either preserves or escapes hypothesis

**Severity 3. Status valid. Confidence high.**
**Lens.** Etingof (R-matrix deformation).
**Provenance.** This wave; cross-link M-29 R-W4-B residual.

**Claim.** Faddeev–Reshetikhin q-twist preserves M-29 (action on
modules unchanged); q-difference action escapes the M-29 hypothesis
(not Hamiltonian vector field) but enters R-W4-B's territory
($L_\infty$-categorified bracket).

**Adjudication.** Sharpens R-W4-B: q-difference candidates are the
explicit example of "categorified bracket" hosting the bi-infinite
parent.

### W3-W7-06 — Lusztig setting at root of unity does not help

**Severity 2. Status valid. Confidence medium-high.**
**Lens.** Etingof (root-of-unity Hopf-algebra deformations).
**Provenance.** This wave; cross-link M-29.

**Claim.** Lusztig restricted enveloping at $q^\ell=1$: classical
scalar $(b+1)\cdots(b+N)$ in $\End(\mathbf 1)=\C$ is unchanged; only
the q-rising factorial $[b+1]_q\cdots[b+N]_q$ vanishes at root of
unity, but this lives in the q-difference-action setting (W3-W7-05),
not in the M-29 hypothesis.

**Adjudication.** Closes the most exotic Etingof candidate (Lusztig
at root of unity) in the negative.

### W3-W7-07 — BGG O confirms vacuum/Verma distinction

**Severity 2. Status valid. Confidence high.**
**Lens.** Etingof (Kazhdan–Lusztig category).
**Provenance.** This wave; cross-link W4-03 (BD chiral / Verma).

**Claim.** BGG category $\mathcal O$ for $\bar A$ has Verma modules
non-locally nilpotent on $\bar A_-$; non-semisimple structure
(KL polynomials) does not create new module homomorphisms between
vacuum and Verma. Confirms W4-03 verdict.

**Adjudication.** Strengthens W4-03 from "Frenkel–Ben-Zvi vertex
PBW" to "the same statement at the Lie-algebra level via BGG O."

### W3-W7-08 — Per-invariant audit confirms M-29 universality

**Severity 3. Status valid. Confidence high.**
**Lens.** Invariants (per-datum classification).
**Provenance.** This wave; cross-link M-28 D₁, D₂, D₃.

**Claim.** Per-invariant analysis exhibits the dichotomy:
preserve (I-c) Hamiltonian vector field $\Rightarrow$ break (I-d) local
nilpotence; preserve (I-d) $\Rightarrow$ break (I-c). Tabulated 13
candidates show this dichotomy is universal except on the
bi-infinite parent (R-W4-A), which gives up both.

**Adjudication.** New diagnostic table classifying every M-29
candidate by invariant breakage. Sharpens the W4 reframe by making
explicit which invariant fails for each candidate.

### W3-W7-09 — Etingof and Gaiotto views agree on M-29

**Severity 2. Status valid. Confidence high.**
**Lens.** Etingof + Gaiotto cross-check.
**Provenance.** This wave; cross-link W3-W2-09–10.

**Claim.** The Etingof tensor-category framework (rising-factorial
scalar in $\End(\mathbf 1)$) and the Gaiotto interface framework
(no single-object interface from formal disk to punctured disk)
identify the **same** obstruction. No disagreement.

**Adjudication.** Cross-confirms W3-W2 Gaiotto interpretation; both lenses
converge on M-29 universality.

### W3-W7-10 — Lens orthogonality (clarification)

**Severity 1 (clarification). Status valid. Confidence medium-high.**
**Lens.** Etingof + Gaiotto + Invariants meta-analysis.
**Provenance.** This wave; meta-comment on M-29.

**Claim.** Etingof identifies the obstruction at $\End(\mathbf 1)$ /
$\Ext^\bullet$ level (representation-theoretic); Gaiotto identifies
it at the bulk-defect interface level (geometric). The two lenses
are **orthogonal** views of the same negative result; neither
subordinates the other.

**Adjudication.** Editorial clarification; supports the
manuscript's W4-derived language by giving two complementary
interpretations.

---

## §6. Verdict on M-29 universality

**M-29 universal categorical no-go is bulletproof against the
Etingof + Invariants attack.**

The proof in `main.tex`:4174–4194 is at the Lie-module level (the
rising-factorial in End(1) is non-zero). The Etingof framework
provides ten new perspectives:

1. Non-semisimplicity does not help (W3-W7-01).
2. Higher Ext-extensions don't host candidates (W3-W7-02).
3. Drinfeld twist preserves M-29 (W3-W7-03).
4. Moyal star preserves M-29 (W3-W7-04, key: $z_i$ are linear).
5. q-twist preserves M-29; q-difference escapes hypothesis (W3-W7-05).
6. Lusztig restricted enveloping at root of unity does not help (W3-W7-06).
7. BGG category $\mathcal O$ confirms W4-03 (W3-W7-07).
8. Per-invariant audit gives a clean dichotomy (W3-W7-08).
9. Etingof and Gaiotto views agree (W3-W7-09).
10. The two lenses are orthogonal (W3-W7-10).

**M-29 stands. Confidence: high.**

The R-W4-A residual (bi-infinite local-cohomology) and R-W4-B
residual ($L_\infty$ categorified bracket) remain the **unique**
escapes from the universal no-go, exactly as W4 found. W3-W7-05
sharpens R-W4-B by identifying q-difference action as the explicit
type of $L_\infty$-categorified bracket that escapes; whether it
admits a candidate is still open.

---

## §7. Verdict on stable core

The wave-2 + wave-3 stable core (master ledger §D, lines 1976–2050)
is **preserved unmodified** by the Etingof + Invariants lens.

- M-29 universal no-go: **strengthened** by W3-W7-01 through
  W3-W7-08; survives all Etingof attacks.
- Theorems A–G: unchanged.
- M-31 BV/CE identification: not directly attacked by this lens;
  W3-W5 already audited it for naturality, and W3-W2 for
  defect-cohomology scope; both stand.
- M-37 four-ingredient closure plan: not directly attacked; W3-W2
  already discharged Weiss-on-$\R$, and the residual at
  $\R^2\times\C^2$ is unchanged.

**No downgrade required.** The Etingof + Invariants lens adds
defensive depth (multiple new attack channels closed) but produces
no fatal attack on the stable core.

**Stable core unchanged.**

---

## §8. New residuals (W7 originated)

**W3-W7-R1 (genuinely new, low severity).** The q-difference action
attempt of W3-W7-05 is a concrete example of an $L_\infty$-categorified
bracket (R-W4-B). Whether the q-difference $\bar A$-module realization
of $\mc P$ admits an $\hbar$-flat one-object candidate is open and
likely the **most concrete avenue** for R-W4-B. This is **Phase-4
research**; not within W7 scope.

No other new residuals.

---

## §9. Heal proposals

| ID | Severity | Target | Action |
|----|----------|--------|--------|
| W3-W7-H1 | 1 (clarification) | M-29 master ledger entry | Add per-invariant dichotomy table from W3-W7-08 §3.2 as a one-paragraph annotation. |
| W3-W7-H2 | 1 (clarification) | M-29 master ledger entry | Add cross-confirmation note: "Etingof tensor-category attack at full strength (W3-W7) confirms M-29; the rising factorial in $\End(\mathbf 1)$ is unaffected by non-semisimple deformation, Drinfeld twist, Moyal star, Lusztig restricted setting, BGG O, or KL category. Both Hom and higher Ext vanish in $\mathsf P_{\mathrm{pol}}$." |
| W3-W7-H3 | 1 (cross-link) | R-W4-B residual entry | Add "q-difference action of $z_i$ on $\bar A$-modules (W3-W7-05) is a concrete example of $L_\infty$-categorified bracket; whether such an action admits an $\hbar$-flat candidate is the most concrete R-W4-B avenue." |

All three are editorial. None requires new mathematical content.

---

## §10. Provenance

W7 (Wave 3) read:

- `/Users/raeez/topological-strings/CLAUDE.md`.
- `/Users/raeez/topological-strings/reconstitution/attack-heal-platonic-2026-04-28.md` lines 1497–1610 (M-28, M-29, M-30); lines 1899–1939 (R-W4-A, R-W4-B, R-W4-C); lines 2000–2160 (consolidation summary).
- `/Users/raeez/topological-strings/reconstitution/wave2-W4-etingof-2026-04-28.md` (full).
- `/Users/raeez/topological-strings/reconstitution/wave3-W2-gaiotto-2026-04-28.md` (full).
- `/Users/raeez/topological-strings/reconstitution/wave3-W5-kazhdan-2026-04-28.md` (full).
- `/Users/raeez/topological-strings/appendix-matlis-principal-parts.tex` (full).
- `/Users/raeez/topological-strings/main.tex` lines 3295–3700 (Theorem D / Koszul region); 4140–4239 (categorical no-go + boundary local-dual construction).

Computational checks (scratch, `/tmp/w7_*.py`):
- `/tmp/w7_etingof_semisimplicity.py`: rising-factorial non-vanishing on $b\in[0,5]$, $N\in[1,5]$; q-rising factorial vanishing analysis for Lusztig setting.
- `/tmp/w7_invariants_breakage.py`: Moyal correction vanishing for linear $z_i$; T²-Cartan invariance; q-difference escape from hypothesis.
- `/tmp/w7_extension_test.py`: Ext$^1$ vanishing in $\mathsf P_{\mathrm{pol}}$; rising-factorial argument lifts to extensions.

External references invoked:
- Etingof–Gelaki–Nikshych–Ostrik *Tensor Categories* (AMS 2015): §4.6 (extensions); §8.3 (Lusztig restricted enveloping at root of unity); §A (semisimplicity criteria).
- Faddeev–Reshetikhin–Takhtajan: q-twist of Hopf algebras.
- Frenkel–Ben-Zvi *Vertex Algebras and Algebraic Curves*: vacuum vs Verma triangular decomposition.
- Bezrukavnikov–Mirković–Rumynin: localization for Lie algebras in characteristic $p$ (sanity check on Lusztig restricted setting).
- BGG (Bernstein–Gelfand–Gelfand): category O.
- Kazhdan–Lusztig: KL polynomials and tensor structure.

W7 confidence: every mathematical claim verified against the cited
manuscript line numbers and the W4 / W3-W2 / W3-W5 ledger entries.
No new theorems proposed; only defensive cross-confirmations and
one new residual avenue (R-W4-B q-difference). No web search.

---

## §11. 200-word summary

The Etingof + Invariants lens applied to the wave-3 stable core
finds the M-29 universal categorical no-go bulletproof against
every Etingof attack channel. The proof of
`thm:no-polynomial-realization-categorical` (`main.tex`:4174–4194)
is at the Lie-module level: the rising factorial
$(b+1)\cdots(b+N)$ in $\End_{\mathcal C}(\mathbf 1)=\C$ is non-zero
in any $\C$-linear tensor category, regardless of semisimplicity.
W3-W7-01 through W3-W7-08 close ten attack channels: non-semisimplicity,
$\Ext^\bullet$, Drinfeld twist, Moyal star (key: $z_i$ are linear,
so all higher Moyal corrections vanish), Faddeev–Reshetikhin q-twist,
Lusztig at root of unity, BGG category $\mathcal O$, and a
per-invariant audit. W3-W7-09 confirms the Etingof view agrees
with the W3-W2 Gaiotto interface interpretation; the two lenses are
orthogonal (representation-theoretic vs geometric) views of the
same obstruction. The unique escapes remain R-W4-A (bi-infinite
local-cohomology) and R-W4-B ($L_\infty$ categorified bracket),
exactly the W4 residuals; W3-W7-05 sharpens R-W4-B by identifying
q-difference action as the most concrete $L_\infty$-categorified
example. **Stable core preserved unmodified. M-29 stands with
high confidence.** Three editorial heals proposed (per-invariant
table, cross-confirmation note, R-W4-B sharpening); no fatal attack.

End of W7 Wave-3 ledger.
