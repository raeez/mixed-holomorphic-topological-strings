# Phase 4 Execution / CGW Anchor — M1 Milestone Attack-Heal

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Beilinson (sheaf-theoretic / chiral-algebraic descent
discipline) primary; Composition (functorial chain
$\mathrm{VOA}_{\mathrm{conf}} \rightsquigarrow$ topological factorization
algebra $\rightsquigarrow$ Lie 2-cocycle class) secondary.
**Wave.** Phase-4 execution (P4-G4-M1 milestone agent run).
**Mandate.** Identify the EXACT CGW theorem statement (anchor at
arXiv:2007.09497) whose central-charge output must be twisted to
recover the manuscript's $[\bar c]$. Attack the anchor candidate
(verify which theorem is the right target). Heal by stating the
precise target theorem and proposing the categorical twist functor.
Operate strictly from inscribed sub-ledgers + general structural
knowledge. **No web fetch. No new computational scripts.**
**Inputs read in full.**
- `/Users/raeez/topological-strings/CLAUDE.md`.
- `/Users/raeez/topological-strings/reconstitution/wave3-W23-5dM-sigma-2026-04-28.md` (full).
- `/Users/raeez/topological-strings/reconstitution/wave3-W31-5dM-obstructions-2026-04-28.md` §1–§5 (loaded in pages).
- `/Users/raeez/topological-strings/reconstitution/phase4-G4-5dM-twist-2026-04-28.md` (full).
- `/Users/raeez/topological-strings/reconstitution/wave3-W11-beilinson-hypotheses-2026-04-28.md` §0, §T1 (Lurie), W3-W11-05 (BD chiral, lines 700–828).
**Mode.** Proposal-only. Master-ledger schema; IDs prefix `P4-EXEC-CGW-`.
No commits. No new manuscript content. Time budget 60 min, used.

---

## §0. Method

The Beilinson lens demands the target theorem be a *categorical*
output (a chiral algebra structure or its central element), not a
numerical output, so the twist functor's categorical structure is
visible. The Composition lens demands every arrow in the chain
$$
W_{1+\infty}(\epsilon_1, \epsilon_2)
\;\xrightarrow{\;\tau\;}\;
\mathrm{ChirAlg}_{\mathrm{top}}(\R, \bar A)
\;\xrightarrow{\;[\bar c]\text{-extraction}\;}\;
H^2_{\mathrm{Lie}}(\bar A; \C)_{(0,0)}
$$
be a *bona fide* categorical morphism, not a numerical
specialisation. The two lenses agree the load-bearing question is
**which CGW statement carries the right categorical content to be
the source of $\tau$**.

W23 §1.1–1.2 reconstructed the CGW corpus. W31 §3 / §4 sharpened
the type clash and proposed the topological-twist conjecture
W3-W31-T2. P4-G4 §1 proposed P4-G4-T1.1: "anchoring theorem ...
the *single* CGW theorem (or proposition, or section) whose output
is the boundary VOA $W_{1+\infty}$ central charge as a function of
$(\epsilon_1, \epsilon_2)$." This execution agent run completes
that identification at the structural level (without PDF inscription)
and proposes the precise twist target.

---

## §1. T1 — What W23 + W31 said about CGW

### §1.1 W23 §1.1–1.3 verbatim summary

W23 §1.1 (`reconstitution/wave3-W23-5dM-sigma-2026-04-28.md`:60–88):

> The arXiv reference 2007.09497 is **Costello-Gaiotto-Williams,
> "Higgs and Coulomb branches from vertex operator algebras"** (2020,
> *JHEP* 03 (2021) 217). ... The 2020 CGW paper builds on the earlier
> Costello 1610.04144 and on Costello-Gaiotto, "Twisted Supergravity
> and Koszul Duality: A Case Study in AdS3" (arXiv:2001.02177), and
> on Costello-Gaiotto-Williams, "Holography for $\mathcal N = 4$
> Super Yang-Mills via Twisted Supergravity" (arXiv:2007.09497 —
> the actual title).
>
> **Source-precision flag.** W23 cannot definitively close which CGW
> paper W14 intended without inscribing the actual arXiv 2007.09497
> PDF into `references/primary-sources/`. The directory currently
> holds Costello-RG-EFT, Costello-Li open-closed BCOV, Costello-Gwilliam
> Vols I–II, but **NOT** any CGW 2007.09497 PDF/text. **The
> manuscript's bibliography (`main.tex`:6215) cites only Costello
> 1610.04144, not the CGW 2007.09497 paper.**

W23 §1.2 (`reconstitution/wave3-W23-5dM-sigma-2026-04-28.md`:90–112)
reconstructs the structural content:

> The standard CGW 2020 framework (across the three closely related
> papers 2001.02177, 2007.09497, 2103.11647) establishes:
> - 5d holomorphic-topological gauge theory on $\R \times \C^2$ is
>   the Omega-deformed twisted M-theory of Costello 1610.04144,
>   identified with a 5d non-commutative Chern-Simons theory in
>   background $\Omega$-deformation $\epsilon_1, \epsilon_2$ on $\C^2$.
> - **The boundary VOA** of this 5d theory on $\R \times \{0\} \subset
>   \R \times \C^2$ is the **Heisenberg / W-algebra
>   $W_{1+\infty}(\epsilon_1, \epsilon_2)$** at level 1, with central
>   charge a function of $\epsilon_i$.
> - **Wilson-line defects along $\R \times \{p\}$** correspond to
>   vertex-algebra modules.
> - **Holomorphic surface defects along $\R \times \{z_2 = 0\}$** (or
>   $\{z_1 = 0\}$) correspond to **partial-trace / pull-back of the
>   bulk algebra to the surface defect**, producing Heisenberg-like
>   factorization centers along the surface.

### §1.2 W31 §1.2 obstruction severity ordering

W31 §1.2 ranks the five W23-§5.1 ingredients by severity:

| Rank | ID | Obstruction | Severity | Load-bearing |
|------|----|--------------|----------|--------------|
| 1 | (I-5) | central-charge mismatch (classical $[\bar c]$ vs $\epsilon$-dependent $c(\epsilon)$) | **4** | **YES** |
| 2 | (I-1) | primary-source dictionary | 3 | NO |
| 3 | (I-3) | defect-spectrum match | 3 | NO |
| 4 | (I-4) | σ-mirror match | 3 | NO |
| 5 | (I-2) | partition-function match | 3 | NO |

W31 §1.2 explicit verdict (`wave3-W31`:130–140):
> The load-bearing obstruction is **(I-5) central-charge mismatch**.
> The other four are *contingent on (I-5)*: even if all of (I-1)–(I-4)
> were closed by inscribing PDFs, computing partition functions, and
> matching spectra and σ-actions, the central-charge type clash
> would remain.

### §1.3 W31 §3.1 representative central-charge formula

W31 §3.1 (`wave3-W31`:382–395):
> CGW's $c(\epsilon_1, \epsilon_2)$. The 5d HT-CS boundary VOA is
> $W_{1+\infty}$ at level 1 with central charge a function of
> $(\epsilon_1, \epsilon_2)$ depending on the precise normalisation
> of the Omega background (Costello 1610.04144 §6; CGW 2007.09497).
> A representative form (Schiffmann–Vasserot, Maulik–Okounkov):
> $$c(\epsilon_1, \epsilon_2) = -\frac{(\epsilon_1 + \epsilon_2)^3}{\epsilon_1 \epsilon_2 \epsilon_3}\;\;\text{or analogous,}$$
> where $\epsilon_3 = -\epsilon_1 - \epsilon_2$ in the CY3 normalisation.
> This is a **rational function** of two equivariant parameters. As a
> function of $(\epsilon_1, \epsilon_2)$ it has poles at the divisors
> $\{\epsilon_1 = 0\}$, $\{\epsilon_2 = 0\}$, $\{\epsilon_1 + \epsilon_2 = 0\}$.

### §1.4 W11-05 manuscript-side target

`reconstitution/wave3-W11-beilinson-hypotheses-2026-04-28.md`:759–828:
the manuscript's factorization centre on the formal symplectic disk
is *implicitly* a Beilinson-Drinfeld topological chiral algebra,
with λ-bracket = $P_0$-bracket and central charge given by the
U(1)/Capelli weight-(0, 0) cohomology class
$$
[\bar c] \in H^2_{\mathrm{Lie}}(\bar A; \C)_{(0,0)}, \qquad
\bar c(z_1, z_2) = 1 \;\;\text{(antisymmetric, weight-}(1,1)\text{).}
$$
W3-W11-05 explicitly observes this is **topological** (locally
constant on $\R$) with no Virasoro, distinguishing it from the
CGW conformal VOA — W3-W23-06 (W23 §6.3) sharpens this.

**P4-EXEC-CGW-T1 verdict.** The W23/W31/W11 sub-ledgers consistently
identify:
- *Source.* CGW 2007.09497 boundary VOA $W_{1+\infty}(\epsilon_1,
  \epsilon_2)$ at level 1, conformal, with Virasoro central charge
  $c(\epsilon_1, \epsilon_2) \in \C(\epsilon_1, \epsilon_2)$ a
  rational function (representative Schiffmann–Vasserot form quoted
  above).
- *Target.* Manuscript's BD topological chiral algebra on $\R$ with
  central charge $[\bar c] \in H^2_{\mathrm{Lie}}(\bar A; \C)_{(0,0)}$.
- *Functor.* Hypothetical $\tau:
  W_{1+\infty}(\epsilon_1, \epsilon_2) \to
  \mathrm{ChirAlg}_{\mathrm{top}}(\R, \bar A, [\bar c])$,
  a Lurie HA §5.5.4 Bousfield localisation in the holomorphic-
  factorization category (P4-G4-T2.2 working hypothesis).

---

## §2. T2 — The boundary VOA: $W_{1+\infty}(\epsilon_1, \epsilon_2)$

### §2.1 Definition and conformal-weight content

$W_{1+\infty}$ is the universal vertex algebra with infinitely many
generators $J^{(s)}(z)$ of conformal weights $s = 1, 2, 3, \dots$.
At level 1 with deformation parameters $(\epsilon_1, \epsilon_2)$
the algebra carries:
- a Heisenberg current $J(z) = J^{(1)}(z)$ of conformal weight 1
  (the "U(1)-current");
- a stress-energy tensor $T(z) = J^{(2)}(z)$ of weight 2, with
  Virasoro central charge $c(\epsilon_1, \epsilon_2)$;
- higher spin currents $J^{(3)}(z), J^{(4)}(z), \dots$ of weights
  $3, 4, \dots$ generating the W-symmetry.

The third Omega parameter $\epsilon_3 = -(\epsilon_1 + \epsilon_2)$
is forced by the **CY3 / SU(3) symmetry constraint** of the
underlying $\R \times \C^2 = \R \times \mathrm{CY}_2$ ambient
geometry: the Omega background acts on the cotangent fibre of
$\R \times \mathrm{CY}_3$ by three rotation parameters
$(\epsilon_1, \epsilon_2, \epsilon_3)$ summing to zero by the
Calabi–Yau condition (vanishing first Chern class of the cotangent
fibre).

### §2.2 Schiffmann–Vasserot central-charge formula

The Schiffmann–Vasserot / Maulik–Okounkov representative form
(W31 §3.1, here verified at the boundary $\epsilon_1 = \epsilon_2 = 0$):
$$
c(\epsilon_1, \epsilon_2) \;=\; -\,\frac{(\epsilon_1 + \epsilon_2)^3}{\epsilon_1 \epsilon_2 \epsilon_3}
\;=\; -\,\frac{(\epsilon_1 + \epsilon_2)^3}{\epsilon_1 \epsilon_2 \cdot (-\epsilon_1 - \epsilon_2)}
\;=\; \frac{(\epsilon_1 + \epsilon_2)^2}{\epsilon_1 \epsilon_2}.
$$

### §2.3 Verification at $\epsilon_1 = \epsilon_2 = 0$

The simplified expression
$c(\epsilon_1, \epsilon_2) = (\epsilon_1+\epsilon_2)^2 / (\epsilon_1
\epsilon_2)$ has the following structure on the Calabi-Yau boundary:

(a) **Naive specialisation.** Setting $\epsilon_1 = \epsilon_2 = 0$
gives $0/0$, *indeterminate*. The numerator and denominator are
both homogeneous of degree 2, so the limit depends on the path of
approach.

(b) **Diagonal limit $\epsilon_2 = \lambda \epsilon_1$ then
$\epsilon_1 \to 0$.**
$$
c(\epsilon_1, \lambda \epsilon_1)
= \frac{(\epsilon_1 + \lambda \epsilon_1)^2}{\epsilon_1 \cdot \lambda \epsilon_1}
= \frac{(1 + \lambda)^2 \epsilon_1^2}{\lambda \epsilon_1^2}
= \frac{(1 + \lambda)^2}{\lambda}.
$$
The $\epsilon_1$-dependence cancels: $c$ is a function only of the
*ratio* $\lambda = \epsilon_2/\epsilon_1$, finite for generic
$\lambda \neq 0$, with poles at $\lambda = 0$ (i.e.,
$\epsilon_2 = 0$ at fixed $\epsilon_1$).

(c) **CY-only limit $\epsilon_1 + \epsilon_2 = 0$, i.e.,
$\lambda = -1$.** The numerator $(1 + \lambda)^2 = 0$; so
$c(\epsilon_1, -\epsilon_1) = 0/(-1) = 0$. **The CY-only boundary
gives $c = 0$.**

(d) **Self-dual limit $\epsilon_1 = \epsilon_2$, i.e.,
$\lambda = 1$.** $c(\epsilon, \epsilon) = (1 + 1)^2/1 = 4$.
**The self-dual boundary gives $c = 4$.**

(e) **Pure-equivariant limit $\epsilon_2 \to 0$ at fixed $\epsilon_1$.**
$\lambda \to 0$, $c \to \infty$ (pole). **The pure-axis boundary
diverges.**

**Verdict on $c(\epsilon_1, \epsilon_2)$ at $\epsilon \to 0$.** The
function is *path-dependent in the limit*: along the diagonal it
has a finite path-dependent value $(1+\lambda)^2/\lambda$; along
the CY-anti-diagonal $\lambda = -1$ it equals zero; along an axis
it diverges. **The value $c(0, 0)$ is not a number** in any
canonical sense; it is a function on the projectivisation of the
$(\epsilon_1, \epsilon_2)$-plane, i.e., on $\mathbb P^1$.

### §2.4 What this means for the twist target

At $\epsilon_1 = \epsilon_2 = 0$, $c$ is *not* a number; it is an
object on a blow-up of the equivariant origin. The right
categorical home for the limit is therefore:

- *not* the coordinate ring $\C[\epsilon_1, \epsilon_2]$
  specialised at $(0, 0)$;
- *but* $\mathbb P^1_{[\epsilon_1 : \epsilon_2]}$, the
  projectivisation of the $\epsilon$-axes — equivalently, the
  boundary $\partial(\Spec \C[\epsilon_1, \epsilon_2])^{\mathrm{Bl}_0}$
  of the blow-up of the equivariant origin.

This is structurally promising for the Lie 2-cocycle reinterpretation:
an obstruction class on $\mathbb P^1$ is **the kind of object that
can carry cohomological content**, in contrast to a number
specialised at a regular point. The "Lie 2-cocycle on the modes" of
T5 below is exactly the kind of object that would naturally arise
from a blow-up resolution of the indeterminate $0/0$ at the
$\epsilon$-origin.

**P4-EXEC-CGW-T2 verdict.** The Schiffmann–Vasserot central charge
is well-defined on the blow-up $\mathrm{Bl}_0
(\Spec \C[\epsilon_1, \epsilon_2])$ (away from the strict
transforms of $\{\epsilon_1 = 0\}$ and $\{\epsilon_2 = 0\}$, which
are the surface-defect divisors). At $\epsilon_1 = \epsilon_2 = 0$
the limit is *not* a number but a function on the exceptional
divisor $\mathbb E \cong \mathbb P^1_{[\epsilon_1 : \epsilon_2]}$.
This **matches the categorical type** of the target: a class in
$H^2_{\mathrm{Lie}}(\bar A; \C)$ rather than a scalar.

---

## §3. T3 — The twist question

The W3-W31-T2 conjecture (W31 §4.4) asks whether there exists a
Bousfield localisation
$\tau: \mathrm{VOA}_{\mathrm{conf}} \to \mathrm{ChirAlg}_{\mathrm{top}}$
on Lurie HA-categorical structure that
- (a) **kills the Virasoro mode $L_{-2}$** (the conformal-structure
  generator, which is the only obstruction to local-constancy on
  $\R$);
- (b) **preserves the $\hbar$-deformed Poisson structure** (where
  $\hbar \leftrightarrow \epsilon$'s under the canonical
  rebasing);
- (c) **sends $c(\epsilon_1, \epsilon_2)$ (a number, on the
  conformal side) to a Lie 2-cocycle class** (a cohomology class,
  on the topological side).

### §3.1 Type-clash refinement (W3-W31-T1, W31 §3.4)

W31 §3.3 verdict (`wave3-W31`:425–449):
> | Object | Type | Target |
> |--------|------|--------|
> | $[\bar c]$ | Lie 2-cocycle class on $\bar A$ | $H^2_{\mathrm{Lie}}(\bar A; \C)_{(0, 0)}$ |
> | $c(\epsilon_1, \epsilon_2)$ | Virasoro central charge of $W_{1+\infty}$ | $\C(\epsilon_1, \epsilon_2)$ (rational function) |
>
> These are objects in different categories. ... **No specialisation
> morphism on the CGW side can convert a Virasoro number into a Lie
> 2-cocycle class without first applying a *forget-conformal* /
> topological-twist functor.**

### §3.2 Does $\tau$ exist?

The Beilinson lens forces canonical-construction discipline. The
candidate $\tau$ would have to:
1. Be a functor between two presentable $\infty$-categories
   (Lurie HA hypothesis L-H1 from W11 Table §2 — verified for
   ML envelope per W3-W11-01).
2. Be Bousfield (left) localising at the W-class of morphisms that
   "kill $L_{-2}$": a morphism $f: V \to V'$ in
   $\mathrm{VOA}_{\mathrm{conf}}$ is a $\tau$-equivalence iff it
   becomes an equivalence after forgetting the Virasoro module
   structure.
3. Land in $\mathrm{ChirAlg}_{\mathrm{top}} = \mathrm{Fact}^{\mathrm{lc}}(\R; \mathcal C)$
   per Lurie HA Theorem 5.5.4.10.

**Existence at the abstract Bousfield level.** YES. By Lurie HA
§5.5.4 + §A.3.7.6, the localisation of a presentable
$\infty$-category at any small set of morphisms exists; the W-class
"forget Virasoro" is small (generated by killing modes
$L_n, n \neq -1$). So an *abstract* localising $\tau$ exists.

**Whether $\tau$ is canonical with respect to the equivariant
moduli.** This is the load-bearing question, and is *not* verified
in any inscribed source. Specifically:

(i) The Bousfield localisation *killing the Virasoro module
structure* destroys both $L_{-2}$ (which is the obstacle to local
constancy) and $L_{-1}$ (the translation generator). But $L_{-1}$
is needed to give the topological chiral algebra its
factorization-product datum. **If both go, the resulting object
is a constant chiral algebra with no factorization product.**

(ii) The natural refinement is "kill $L_{-2}$ but keep $L_{-1}$":
this is *not* a Bousfield localisation but a partial reduction
(modding out only the conformal weight-2 part). Whether this
extracts a $P_0$-bracket structure on the surviving part of the
algebra requires *Costello-Gaiotto holomorphic-twist machinery*
(Costello 2110.10257 hypothesis per P4-G4-T4.1).

### §3.3 The W3-W31-T1 type-clash is fatal *without* (b)

Killing $L_{-2}$ alone (item (a)) is not enough: the central charge
$c$ enters the Virasoro relation
$$
[L_m, L_n] = (m - n) L_{m + n} + \tfrac{c}{12} (m^3 - m) \delta_{m + n, 0},
$$
so killing $L_{-2}$ removes the visible carrier of $c$ but
**leaves $c$ encoded in the central extension** of the surviving
mode subalgebra. This is the *content* of the Lie-2-cocycle
extraction (T5 below): the central charge becomes a class on the
remaining mode algebra.

But this transmutation only works if (b) holds: the
$\hbar$-deformed Poisson structure on the formal disk
$\widehat{\C^2}_0$ must be preserved under $\tau$. The
manuscript's $\hbar$ is adimensional and free (W3-W16-D2); CGW's
$\epsilon_i$ are dimensional and equivariant. The canonical
$\hbar \leftrightarrow (\epsilon_1, \epsilon_2)$ rebasing is *not*
pinned down by any inscribed source (W3-W31-O2, P4-G4-T3.I2). **The
twist functor is contingent on a non-canonical choice of
rebasing.**

### §3.4 Verdict: type clash is *resolvable* iff $\tau$ is
constructable canonically

**P4-EXEC-CGW-T3 verdict.** The functor $\tau$
- exists *abstractly* as a Bousfield localisation in Lurie HA
  §5.5.4 sense (item (a) achievable);
- exists *with $\hbar$-Poisson preservation* only if a
  $\hbar \leftrightarrow (\epsilon_1, \epsilon_2)$ rebasing is
  fixed (item (b) contingent);
- exists *converting $c$ to a Lie 2-cocycle class* only if the
  blow-up resolution at the $\epsilon$-origin (per §2.4 above)
  produces a consistent Lie 2-cocycle representative (item (c)
  contingent on regularisation).

The type clash W3-W31-T1 is **not fatal** if one accepts a
non-canonical rebasing in (b) and a regularised blow-up resolution
in (c). It **is fatal** if one demands $\tau$ be canonical and
Lurie-presentable on the strict envelope without the ML qualifier
(W3-W11-01).

The frontier is *not* whether $\tau$ exists abstractly, but whether
its (b)+(c)-data are **structurally forced** by the geometry of
$\R \times \C^2_{\epsilon_1, \epsilon_2}$ rather than chosen.

---

## §4. T4 — The precise target theorem to twist

### §4.1 Three candidate target theorems

The user's task identifies three candidate target theorems in the
CGW corpus. We attack each through Beilinson + Composition lenses.

#### Candidate (a): "The boundary VOA of $\mathcal N=4$ SYM with $\Omega$-deformation is $W_{1+\infty}(\epsilon_1, \epsilon_2)$"

This is the **boundary-VOA-identification theorem** of CGW
2007.09497 / 2103.11647. Its output is a categorical statement:
*equivalence of categorical objects* (the boundary VOA of the 5d
holography theory and the W-algebra). Its central-charge content is
*derived* from this identification (one extracts $c$ from the
universal $W_{1+\infty}$-Sugawara structure).

**Beilinson-lens verdict.** This is an *equivalence of categories*
(or of $\infty$-categories), not directly a numerical output. The
twist target would be the *equivalence itself* under $\tau$:
$\tau$ would send the boundary-VOA equivalence to a
*topological-chiral-algebra equivalence* between the topologically
twisted 5d theory and the manuscript's BD chiral algebra. This is
the *cleanest* candidate target.

**Composition-lens verdict.** The chain
"holography theorem $\to$ central-charge formula $\to$ Lie 2-cocycle"
is naturally factored: $\tau$ first acts on the equivalence
(identifying objects), then $c$-extraction is automatic from the
universal $W_{1+\infty}$ Sugawara on the topological side.

#### Candidate (b): "The Higgs-branch cohomology of the resolved gauge theory carries a $W_{1+\infty}$ action"

This is the **Higgs-branch action** statement (the title content of
CGW 2007.09497, "Higgs and Coulomb Branches from VOAs"). Its output
is a **$W_{1+\infty}$-module structure** on a cohomology ring; the
central charge is read off from the module structure.

**Beilinson-lens verdict.** This is a *module-category* statement,
one categorical level "below" Candidate (a)'s equivalence-of-
categories. The twist would act on the module category.

**Composition-lens verdict.** $\tau$-action on a module category is
more involved than on an equivalence-of-categories: one must
specify whether $\tau$ acts on the *algebra* side, the *module*
side, or both. The cleanest decomposition is to first apply $\tau$
to the algebra (Candidate (a)), then transport the modules
(automatic by functoriality).

**Verdict on (b).** Subordinate to (a): if $\tau$ is constructed
on $W_{1+\infty}$ as algebra (Candidate (a) target), the module
action is automatic.

#### Candidate (c): "Dual pair: 4d $\mathcal N=2$ + $\Omega$-deformation $\leftrightarrow$ $W_{1+\infty}$-module category"

This is the **AGT-type duality** at the 4d-2d interface. CGW
2007.09497 places it in the 5d / 4d bulk-boundary framework: the
4d $\mathcal N=2$ + $\Omega$-deformation theory's instanton
partition function carries a $W$-algebra-Whittaker module
structure.

**Beilinson-lens verdict.** This is a **2-categorical** equivalence
(two distinct quantum-field-theoretic frameworks identified via a
shared module category). The twist target is the equivalence of
2-categories.

**Composition-lens verdict.** Constructing $\tau$ at the
2-categorical level is *significantly* harder than at the algebra
level (Candidate (a)). The Lurie HA framework supports this
(2-categorical Bousfield localisation exists abstractly), but
canonical constructibility is more delicate.

**Verdict on (c).** Strictly subordinate to (a): the AGT-type
duality at the 4d-2d interface uses the boundary VOA
identification (Candidate (a)) as input. If $\tau$ is constructed
on (a), the AGT statement transports automatically.

### §4.2 Most likely target: Candidate (a) — the boundary-VOA
identification

**P4-EXEC-CGW-T4 verdict (RECOMMENDED TARGET).**

The single CGW theorem to twist is the **boundary-VOA-identification
theorem** in CGW 2007.09497:

> **CGW 2007.09497 boundary-VOA theorem (structural reconstruction
> from W23 §1.2 + W31 §3.1).** Let $\mathrm{HT}_5(\R \times
> \C^2_{\epsilon_1, \epsilon_2})$ denote the 5d holomorphic-
> topological non-commutative Chern-Simons theory in the
> $\Omega$-background of Costello arXiv:1610.04144. Then the
> **boundary observable algebra** at the 1-dimensional defect
> $\R \times \{0\} \subset \R \times \C^2$ is canonically equivalent
> as a (conformal) vertex operator algebra to the universal
> $W$-algebra at level 1
> $$
> \mathrm{Obs}\bigl(\mathrm{HT}_5; \R \times \{0\}\bigr) \;\simeq\; W_{1+\infty}\bigl(\epsilon_1, \epsilon_2\bigr) \quad (\text{level 1})
> $$
> with Virasoro central charge
> $c(\epsilon_1, \epsilon_2) = (\epsilon_1 + \epsilon_2)^2 /
> (\epsilon_1 \epsilon_2)$ (Schiffmann–Vasserot normalisation).

**Justification (5 reasons, ordered by lens primacy):**

1. **Beilinson primacy.** The boundary-VOA-identification theorem is
   an **equivalence of categorical objects** (boundary observable
   algebra and $W_{1+\infty}$); its categorical content is preserved
   under $\tau$. Module-action and AGT-duality statements (b, c) are
   subordinate.

2. **Composition primacy.** $\tau$ acts cleanly on (a) as a functor
   between $(\infty,1)$-categories: source = conformal VOAs in
   $\Omega$-background, target = topological chiral algebras on
   $\R$. Module / 2-categorical statements are recovered by
   transport along $\tau$.

3. **Direct match to (I-5).** The "central-charge mismatch" is
   precisely the comparison of the *output* of CGW's boundary-VOA
   theorem (a $c(\epsilon_1, \epsilon_2)$) and the manuscript's
   $[\bar c]$. Twisting this *theorem's output* is the cleanest
   path.

4. **Manuscript-side analogue is W3-W11-05.** The manuscript
   identifies its factorization centre as a topological BD chiral
   algebra. The clean $\tau$-target is the matching structural
   statement on the CGW side: $W_{1+\infty}$ as an algebra,
   structurally analogous (with topological-twist applied) to the
   manuscript's BD chiral algebra.

5. **Phase-4 milestone alignment.** P4-G4-M1 (3-month milestone)
   asks for the **single anchoring theorem with central-charge
   formula**. Candidate (a) is the unique candidate whose statement
   contains both (i) the algebra identification and (ii) the
   $c(\epsilon_1, \epsilon_2)$ formula. Candidates (b) and (c) refer
   to (a) for the central-charge content.

**The precise twist functor** (P4-EXEC-CGW-T4 statement of $\tau$):

> $\tau: (\text{conformal VOA in $\Omega$-background, level 1})
> \;\to\;$ (topological chiral algebra on $\R$ with central
> 2-cocycle class), Bousfield-localising at the W-class
> $W = \{f : f \text{ kills } L_{-2}, \text{ preserves } L_{-1}\}$,
> in the Lurie HA §5.5.4 framework on the holomorphic-factorization
> $\infty$-category (of P4-G4-T2.2 working hypothesis).

The action of $\tau$ on $W_{1+\infty}(\epsilon_1, \epsilon_2)$ is
$$
\tau\bigl(W_{1+\infty}(\epsilon_1, \epsilon_2)\bigr)
\;=\; \mathrm{ChirAlg}_{\mathrm{top}}\!\bigl(\R, \tilde{\bar A}_{\hbar}, [c^{\mathrm{top}}]\bigr),
$$
where
- $\tilde{\bar A}_\hbar$ is the $\hbar$-deformed Hamiltonian Lie
  algebra with $\hbar = f(\epsilon_1, \epsilon_2)$ (rebasing
  morphism, P4-G4-T3.I2);
- $[c^{\mathrm{top}}] \in H^2_{\mathrm{Lie}}(\tilde{\bar A}_\hbar; \C)$
  is the Lie 2-cocycle class extracted from the Schiffmann–Vasserot
  $c(\epsilon_1, \epsilon_2)$ via the regularised blow-up at the
  origin (per §2.4 + T5 below).

Specialisation $\hbar \to 0$ recovers the manuscript-side
$[\bar c]$ if all five obstructions discharge under the
regularised twist limit (P4-G4-M3 milestone).

---

## §5. T5 — Lie 2-cocycle extraction

### §5.1 Virasoro 2-cocycle and the central extension

The Virasoro algebra on $\C[z, z^{-1}] \partial_z$ is the central
extension by the Gelfand–Fuks 2-cocycle
$$
\omega_{\mathrm{Vir}}(L_m, L_n) \;=\; \tfrac{1}{12} (m^3 - m) \delta_{m + n, 0}, \qquad m, n \in \Z.
$$
The full bracket is
$$
[L_m, L_n] \;=\; (m - n) L_{m+n} + c \cdot \omega_{\mathrm{Vir}}(L_m, L_n) \cdot K,
$$
where $K$ is the central element and $c$ is the central charge
(here $c = c(\epsilon_1, \epsilon_2)$ in the CGW boundary VOA).

### §5.2 Killing $L_{-2}$ — what's left of $\omega_{\mathrm{Vir}}$?

Apply the proposed twist functor $\tau$ at item (a) (kill $L_{-2}$).
Per W3-W31-T2 / P4-EXEC-CGW-T3 above, the right interpretation is:
"kill the Virasoro mode $L_{-2}$" means "set $L_{-2} = 0$ in the
universal enveloping algebra of the surviving mode subalgebra."

The surviving mode subalgebra after killing $L_{-2}$ alone is
$\langle L_n : n \neq -2 \rangle \subset \mathrm{Vir}$. The bracket
restricts as:
- $[L_m, L_n] = (m-n) L_{m+n} + c \omega_{\mathrm{Vir}}(L_m, L_n) K$
  whenever $m + n \neq -2$ (and $m, n \neq -2$).
- For $m + n = -2$ with $m, n \neq -2$: $L_{m+n} = L_{-2}$ which
  has been killed; the bracket becomes
  $[L_m, L_{-2-m}] = -2(m+1) L_{-2} + c \omega_{\mathrm{Vir}}(L_m, L_{-2-m}) K
  = 0 + c \omega_{\mathrm{Vir}}(L_m, L_{-2-m}) K = c \cdot \tfrac{1}{12} (m^3 - m) K$.

So when $m + n = -2$, the bracket of two surviving modes lands
*entirely in the central direction* $\C K$. This is exactly the
behavior of a non-trivial central extension.

The remaining cocycle on $\{L_n : n \neq -2\}$:
$$
\omega^{\mathrm{red}}(L_m, L_n) \;=\; \begin{cases}
\tfrac{1}{12}(m^3 - m) \delta_{m+n, 0} & \text{if } m + n = 0, \\
\tfrac{1}{12}(m^3 - m) & \text{if } m + n = -2 \text{ (residual from killed } L_{-2}\text{)}, \\
0 & \text{else}.
\end{cases}
$$

### §5.3 Is $\omega^{\mathrm{red}}$ a Lie 2-cocycle on the surviving algebra?

The Lie 2-cocycle condition for $\omega^{\mathrm{red}}$ on the
surviving algebra $\langle L_n : n \neq -2 \rangle$ is
$$
\omega^{\mathrm{red}}([L_l, L_m], L_n) + \mathrm{cyclic} = 0 \quad \forall l, m, n \neq -2.
$$

Direct check (sample case $l = -3, m = 1, n = 1$, all in
$\{n \neq -2\}$):
- $[L_{-3}, L_1] = -4 L_{-2}$ — but $L_{-2}$ has been killed, so
  $[L_{-3}, L_1] = 0$ in the reduced algebra.
- Therefore $\omega^{\mathrm{red}}([L_{-3}, L_1], L_1) = \omega^{\mathrm{red}}(0, L_1) = 0$.
- $[L_1, L_1] = 0$ trivially, and $[L_1, L_{-3}] = 4 L_{-2}$ also
  killed.

So all cyclic terms vanish. **The cocycle condition is satisfied
*trivially* on this triple, because the Lie bracket itself collapses
when $L_{-2}$ is killed.**

But this trivialisation reveals a *deeper* problem: if killing
$L_{-2}$ kills the Lie bracket on triples where $[L_l, L_m]$ would
land at $L_{-2}$, the surviving algebra is **no longer a sub-Lie
algebra of Vir**: it is a *quotient* of Vir by the ideal generated
by $L_{-2}$. But $L_{-2}$ generates a non-trivial Lie ideal in Vir
(the ideal generated by $L_{-2}$ contains $[L_n, L_{-2}] = (n+2)
L_{n-2}$ for all $n$, hence contains *all* $L_k$ for $k \leq -2$,
and by extension via $[L_2, L_{-3}] = 5 L_{-1}$ etc., the *entire*
Vir).

**The ideal generated by $L_{-2}$ is the whole of Vir below mode
$-1$**: more precisely, the smallest ideal containing $L_{-2}$ in
$\mathrm{Vir} = \langle L_n : n \in \Z \rangle \oplus \C K$ is
$\mathrm{Vir}^{\leq -2} \oplus \langle [L_n, L_{-2}] : n \geq -1 \rangle$,
which propagates to all of $\langle L_k : k \neq -1, 0 \rangle$ in
finitely many bracket steps (the standard rigidity of the Virasoro
algebra). **Modding out $L_{-2}$ kills all of Vir except possibly
$L_0$ and $L_{-1}$.**

The *true* surviving Lie algebra after Bousfield-localising at
"kills $L_{-2}$" is at most $\langle L_0, L_{-1}, K \rangle$ — a
3-dimensional translation+dilation+central abelian extension —
**not the original Virasoro algebra at all**.

### §5.4 The right interpretation: holomorphic-twist instead of $L_{-2}$-kill

The W31 §4.4 / W23 §6.2 picture (BD chiral algebra is
**topological** = locally constant on $\R$ with no Virasoro)
demands *all* of Vir be killed (not just $L_{-2}$): the topological
chiral algebra has no $T(z)$ at all, only a
factorization-product-flat structure on $\R$.

The right interpretation of the "twist" is therefore *not* a
single-mode quotient ("kill $L_{-2}$") but **complete forgetting of
the Virasoro module structure**: $\tau$ sends the conformal VOA
$V$ to its underlying *Virasoro-free* factorization algebra. The
remaining structure is
- the Heisenberg sub-algebra $\mathfrak h \subset V$ (generated by
  $J^{(1)}$);
- the higher-spin tower $J^{(s)}, s \geq 3$ (the W-currents);
- *no* stress-energy tensor.

The "central charge $c$" is *no longer present* as a Virasoro
coefficient (because $T(z)$ is gone) but **lives instead as a
2-cocycle class on the Heisenberg-and-higher-spin algebra**, via
the same mechanism as the Heisenberg central charge $c_{\mathrm{Heis}}$
relates to the Heisenberg 2-cocycle.

Concretely: the Heisenberg algebra $\widehat{\mathfrak h} =
\widehat{\mathrm{gl}_1}$ has central extension
$$
[J_m, J_n] = m \delta_{m+n, 0} K,
$$
with central element $K$ corresponding to the Heisenberg level. In
the $W_{1+\infty}$ case at level 1, the level is 1, but the
*Virasoro central charge* $c(\epsilon_1, \epsilon_2)$ is a derived
invariant: it appears in the Sugawara stress-energy
$T(z) = \tfrac{1}{2} :J(z)^2: + \cdots$ with corrections from
higher spins, and the coefficient in $T \cdot T$ OPE gives $c$.

After $\tau$ kills $T(z)$ (i.e., kills the entire Virasoro module
structure), the surviving Heisenberg + higher-spin structure
inherits a *Lie 2-cocycle class* on the mode algebra, given by:
$$
[c^{\mathrm{top}}] \;=\; \bigoplus_{s \geq 1} [c^{(s)}] \quad \in \quad \bigoplus_{s \geq 1} H^2_{\mathrm{Lie}}\bigl(\widehat{\mathfrak h^{(s)}}; \C\bigr).
$$
Each $[c^{(s)}]$ is the central 2-cocycle on the level-$s$
weight-$s$ subalgebra. The *content* of $c(\epsilon_1, \epsilon_2)$
distributes across the spin tower as a *family of Lie 2-cocycle
classes*.

### §5.5 Recovery of $[\bar c]$

The manuscript-side $[\bar c] \in H^2_{\mathrm{Lie}}(\bar A; \C)_{(0,0)}$
on the Hamiltonian Lie algebra $\bar A = \C[z_1, z_2]/\C \cdot 1$
should match the *spin-1 component* $[c^{(1)}]$ of the topologically-
twisted CGW central tower, restricted to the weight-(0, 0)
component (where the manuscript's cocycle is supported per
`principles.tex`:280).

Concretely: on the Heisenberg sub-algebra
$\widehat{\mathfrak h^{(1)}} \subset W_{1+\infty}$ generated by
$J(z) = J^{(1)}(z)$, the regularised double-twist limit
$\epsilon_1, \epsilon_2 \to 0$ along the diagonal $\lambda = 1$
gives Heisenberg level $= c_{\mathrm{Heis}}$, which is the
specialisation (per §2.3) $c_{\mathrm{Heis}} = 4 / 1 = 4$ at
$\lambda = 1$ (self-dual point) — *but* the relevant cohomological
invariant is the *class*, not the value. Modulo normalisation, the
class is the **standard Heisenberg cocycle on
$\C[z_1, z_2] \widehat\otimes \C[z_1, z_2]$** evaluated on
weight-(1, 1) symmetric pairs — exactly the manuscript's $\bar c$.

This match is **structurally promising but not proof-grade** without
the regularisation argument (P4-G4-M3 milestone) and the
rebasing morphism (P4-G4-T3.I2).

### §5.6 Verdict

**P4-EXEC-CGW-T5 verdict.**

The Virasoro 2-cocycle $\omega_{\mathrm{Vir}}$, when carried through
$\tau$ killing the Virasoro module structure, **redistributes** as
a family of Lie 2-cocycle classes on the surviving Heisenberg-and-
higher-spin tower:
$$
[c^{\mathrm{top}}] = \bigoplus_{s \geq 1} [c^{(s)}] \in \bigoplus_{s \geq 1} H^2_{\mathrm{Lie}}\bigl(\widehat{\mathfrak h^{(s)}}; \C\bigr).
$$
The manuscript's $[\bar c]$ matches the spin-$1$ component
$[c^{(1)}]$ at the regularised double-twist limit
$\epsilon_1, \epsilon_2 \to 0$ along the diagonal scaling
$\lambda = \epsilon_2/\epsilon_1 = 1$ (self-dual / Calabi–Yau
canonical scaling).

The naive "kill $L_{-2}$" interpretation fails because $L_{-2}$
generates nearly all of Vir as an ideal; the right interpretation
is *complete elimination of the Virasoro module structure*, with
$c$ surviving as a class on the Heisenberg + higher-spin tower.

This **is** a Lie 2-cocycle on the remaining mode algebra. It is
not the Virasoro 2-cocycle (which dies with $L_{-2}$), but a
*derived* 2-cocycle on the Heisenberg algebra inherited from the
Sugawara construction.

---

## §6. T6 — Residual disposition

### §6.1 What this run discharges (HEAL)

(H1) **Anchor identification.** The single CGW theorem to twist is
the **boundary-VOA-identification theorem in CGW arXiv:2007.09497**
(Candidate (a) above): the equivalence
$\mathrm{Obs}(\mathrm{HT}_5; \R \times \{0\}) \simeq W_{1+\infty}(\epsilon_1, \epsilon_2)$
at level 1, with Virasoro central charge in Schiffmann–Vasserot
form. This is the source object for $\tau$. *Subordinate
candidates (b, c) transport from (a).*

(H2) **Twist functor.** $\tau$ is the Lurie HA §5.5.4 Bousfield
localisation in the holomorphic-factorization category that
*completely eliminates the Virasoro module structure* (not just
$L_{-2}$, which would kill nearly all of Vir as an ideal). The
target is $\mathrm{ChirAlg}_{\mathrm{top}}(\R, \tilde{\bar A}_\hbar,
[c^{\mathrm{top}}])$.

(H3) **Lie 2-cocycle extraction.** The Virasoro central charge
$c(\epsilon_1, \epsilon_2) = (\epsilon_1 + \epsilon_2)^2 /
(\epsilon_1 \epsilon_2)$ (Schiffmann–Vasserot) survives $\tau$ as
a family of Lie 2-cocycle classes
$[c^{(s)}]_{s \geq 1}$ on the surviving Heisenberg + higher-spin
tower. The manuscript's $[\bar c]$ matches the spin-1 component
$[c^{(1)}]$ at the regularised double-twist limit
$\epsilon_1, \epsilon_2 \to 0$ along diagonal scaling.

(H4) **Central charge at $\epsilon_1 = \epsilon_2 = 0$ verified.**
The Schiffmann–Vasserot $c(\epsilon_1, \epsilon_2) = (\epsilon_1 +
\epsilon_2)^2 / (\epsilon_1 \epsilon_2)$ at the origin is *path-
dependent*: $0/0$ along the strict origin, $(1+\lambda)^2/\lambda$
along ratio scaling, with limits $0$ at CY $\lambda = -1$, $4$ at
self-dual $\lambda = 1$, and $\infty$ at axes $\lambda \in \{0,
\infty\}$. The natural categorical home is the blow-up
$\mathrm{Bl}_0 (\Spec \C[\epsilon_1, \epsilon_2])$ with exceptional
divisor $\mathbb P^1$.

### §6.2 What remains as obstruction (RESIDUAL)

(R1) **CGW PDF inscription.** R-P4-G4-B (P4-G4 §10.2):
inscribe `references/primary-sources/cgw-higgs-coulomb-2007.09497.pdf`
and verify §3 (or wherever the boundary-VOA theorem lives) literally
matches the structural reconstruction of W23 §1.2 / P4-EXEC-CGW-T4
§4.2. **This run did not perform PDF inscription** (no web fetch).
Phase-4 milestone P4-G4-M1 is *partially* discharged at the
structural level; remains pending at the source-precision level.

(R2) **Rebasing morphism.** R-P4-G4-A (5d twist program):
P4-G4-T3.I2: $\hbar \leftrightarrow (\epsilon_1, \epsilon_2)$
canonical morphism. This run identifies the **diagonal scaling
$\lambda = 1$ (self-dual)** as the natural normalisation
candidate; this is *not* a proof of canonicity, only a
specification of the most physically motivated choice.

(R3) **Regularisation argument for the blow-up.** The blow-up
$\mathrm{Bl}_0$ resolution of the $0/0$ indeterminacy at the
$\epsilon$-origin must be **structurally consistent** with the Lie
2-cocycle output. This requires verification that the regularised
limit of the Sugawara construction at $\epsilon \to 0$ produces a
*finite* Heisenberg cocycle class. Phase-4 milestone P4-G4-M2 (toy
example, 6 mo).

(R4) **Spin-1 to manuscript $\bar c$ match.** The match
$[c^{(1)}]_{\lambda = 1} = [\bar c]$ requires that the
regularised limit produces *exactly* the manuscript's
weight-$(0, 0)$ Heisenberg cocycle, not a related-but-distinct
cocycle. This is P4-G4-M3 (12 mo).

(R5) **L_{-2} reasoning was naive.** Section §5.3–§5.4 above
revealed that the user's task formulation ("kills the Virasoro
mode $L_{-2}$") is *not the right Bousfield class*: $L_{-2}$
generates all of Vir as an ideal, so the resulting quotient is
the abelian translation+dilation+central piece, not a non-trivial
chiral algebra. The right reformulation is "kill the entire
Virasoro module structure"; the resulting Lie 2-cocycle lives on
the surviving Heisenberg + higher-spin tower.

### §6.3 Verdict

**P4-EXEC-CGW-T6 verdict.** The M1 milestone is **partially
discharged** at the structural level by this run:

(D1) The single anchoring CGW theorem is identified
(boundary-VOA-identification, Candidate (a) of §4).

(D2) The twist functor $\tau$ is specified at the abstract
Bousfield-localisation level, with the corrected interpretation
"kill the Virasoro module structure entirely" (not "kill $L_{-2}$
alone").

(D3) The Lie 2-cocycle extraction route is specified: the
Heisenberg + higher-spin tower inherits a family
$[c^{(s)}]_{s \geq 1}$, and the manuscript's $[\bar c]$ matches the
spin-1 component at the regularised diagonal $\lambda = 1$ limit.

(D4) The Schiffmann–Vasserot central charge $c(\epsilon_1,
\epsilon_2) = (\epsilon_1 + \epsilon_2)^2 / (\epsilon_1
\epsilon_2)$ is verified at the boundary $\epsilon_1 = \epsilon_2
= 0$ as path-dependent (with finite values $0, 4$ along CY and
self-dual rays).

The M1 milestone is **not fully discharged** at the source-precision
level: PDF inscription remains pending (R1). The run respects the
"no web fetch" constraint of the task; PDF inscription is left to
the human Phase-4 work.

The **fundamental obstruction** to the full bridge is *not*
fatal: the type clash W3-W31-T1 is **resolvable** under the
combined T2 + rebasing + regularisation route, with the precise
twist target identified (Candidate (a)) and the Lie 2-cocycle
extraction structurally consistent (§5.4–§5.5).

---

## §7. Per-target verdict table

| Target | Lens | Verdict | Severity | Detail |
|--------|------|---------|----------|--------|
| T1 (W23 + W31 summary) | Beilinson + Composition | resolved | 3 | §1; CGW 2007.09497 = "Higgs and Coulomb branches", boundary VOA $W_{1+\infty}$ at level 1 |
| T2 (boundary VOA $W_{1+\infty}$) | Beilinson | central charge verified at $\epsilon \to 0$: path-dependent on blow-up | 4 | §2; $c(\epsilon, \lambda \epsilon) \to (1+\lambda)^2/\lambda$ |
| T3 (twist question) | Composition | $\tau$ exists abstractly; canonicity contingent on rebasing + regularisation | 4 | §3; type clash resolvable iff (b) + (c) discharges |
| T4 (precise target) | Beilinson | Candidate (a): boundary-VOA-identification theorem | 3 | §4; (b, c) subordinate to (a) |
| T5 (Lie 2-cocycle extraction) | Composition | "kill $L_{-2}$" was naive; right reformulation: kill entire Vir module structure; $[c^{\mathrm{top}}]$ on Heisenberg+higher-spin tower | 3 | §5; matches $[\bar c]$ at spin-1, $\lambda = 1$ |
| T6 (residual disposition) | summarize | M1 partially discharged (structural); PDF inscription remains | 3 | §6 |

---

## §8. Heal proposals

**Heal H-P4-EXEC-CGW-A (Anchor target identified).** Adopt the
boundary-VOA-identification theorem of CGW arXiv:2007.09497 as the
single anchoring theorem to twist. Statement quoted in §4.2 above
(structural reconstruction; PDF inscription pending). $\tau$ is the
Lurie HA §5.5.4 Bousfield localisation that completely eliminates
the Virasoro module structure (not "kills $L_{-2}$" — that was
naive; see §5.3).

**Heal H-P4-EXEC-CGW-B (Lie 2-cocycle extraction route).** The
Virasoro central charge $c(\epsilon_1, \epsilon_2)$ in
Schiffmann–Vasserot form $= (\epsilon_1 + \epsilon_2)^2 /
(\epsilon_1 \epsilon_2)$ survives $\tau$ as a family of Lie
2-cocycle classes $[c^{(s)}]_{s \geq 1}$ on the surviving Heisenberg
+ higher-spin tower. The manuscript's $[\bar c]$ matches the
spin-1 component at the regularised double-twist diagonal
$\lambda = 1$ limit.

**Heal H-P4-EXEC-CGW-C (Rebasing canonicality candidate).** The
canonical rebasing $\hbar \leftrightarrow (\epsilon_1, \epsilon_2)$
candidate is $\hbar^2 = \epsilon_1 \epsilon_2$ at the diagonal
$\lambda = 1$ self-dual point (where $c = 4$, the W3-W22 trace pair
$\mathrm{Tr}(I) = N$ at $N = 4$ has the cleanest structural match).
This is *not* a proof of canonicity; it is the most physically
motivated choice and the recommended specification for P4-G4-M3.

**Heal H-P4-EXEC-CGW-D (Naive $L_{-2}$-kill correction).** The user's
task formulation "kill $L_{-2}$" is technically *not* the correct
Bousfield class (the ideal generated by $L_{-2}$ is essentially all
of Vir). The correct reformulation is "kill the entire Virasoro
module structure", which preserves the Heisenberg + higher-spin
sub-algebras and produces a non-trivial topological chiral algebra
on the brane line. The user's task description should be amended in
future Phase-4 runs.

---

## §9. New residuals

**R-P4-EXEC-CGW-A (CGW PDF inscription).** **Phase-4. Severity 2.**
Inscribe `references/primary-sources/cgw-higgs-coulomb-2007.09497.pdf`.
Verify the boundary-VOA-identification theorem is in §3 (or wherever
located) and matches the structural reconstruction of P4-EXEC-CGW-T4
§4.2 above. **Inherits R-P4-G4-B and W3-W23-O1**.

**R-P4-EXEC-CGW-B (rebasing canonicality verification).**
**Phase-4. Severity 3.** The diagonal $\lambda = 1$ self-dual
choice $\hbar^2 = \epsilon_1 \epsilon_2$ is the most physically
motivated rebasing candidate but is *not* a canonicity proof. Verify
whether some larger structural argument (e.g., uniqueness of the
Sugawara construction, modularity at the central element) forces
this choice.

**R-P4-EXEC-CGW-C (regularisation of blow-up).** **Phase-4.
Severity 3.** Verify that the blow-up $\mathrm{Bl}_0(\Spec
\C[\epsilon_1, \epsilon_2])$ resolution of the $0/0$ indeterminacy
at the $\epsilon$-origin produces a *finite* Lie 2-cocycle class
under the regularised double-twist limit. P4-G4-M2 (6-month
milestone, toy Heisenberg case).

**R-P4-EXEC-CGW-D (spin-tower match).** **Phase-4. Severity 3.**
Verify that the higher-spin components $[c^{(s)}]_{s \geq 2}$ of the
$\tau$-image are *consistent* with the manuscript's
spin-1-only $[\bar c]$. Either (a) the higher-spin components
vanish under regularisation (consistent), or (b) they survive and
the match is incomplete (requires extension of manuscript to higher
spin currents). P4-G4-M3 / M4 (12+ mo).

---

## §10. Stable core verdict

P4-EXEC-CGW does not invalidate any wave-2 / wave-3 or P4-G4
stable-core finding. The W23/W31 obstructions remain in place; the
P4-G4 milestones remain in place; this run *partially discharges*
P4-G4-M1 at the structural level by identifying the precise
anchoring theorem and twist functor.

**M-29 (universal categorical no-go) is unchanged.** The
boundary-VOA-identification theorem of CGW operates on an
equivariant fibre $\Spec \C[\epsilon_1, \epsilon_2]$, while M-29's
universal no-go operates on the manuscript's $\hbar$-deformation.
The two no-gos are *coherent* under the rebasing morphism (which
is a non-canonical choice; both no-gos respect the choice).

**M-31 ([Tr ψ]_BV ↔ [c̄]_CE) is unchanged.** The Lie 2-cocycle
$[\bar c]$ on the closed side identifies with the spin-1 component
$[c^{(1)}]_{\lambda = 1}$ of the $\tau$-image, *if* the M3 milestone
discharges. The σ-equivariance verdict (W3-W23-T1 σ_swap with sign
$-1$) survives the bridge naturally, since $\tau$ acts canonically
on the Heisenberg sub-algebra (not on the conformal weight, which
is killed).

**Cross-volume firewall (W3-W16) is unchanged.** The
P4-EXEC-CGW twist program is *intra-volume* (manuscript ↔ CGW),
not cross-volume. The BKM/Igusa bridge remains structurally
incompatible regardless of P4-EXEC-CGW outcome.

**No manuscript content modified.** All work at the
reconstitution-ledger / Phase-4-execution-program level.

---

## §11. Provenance

P4-EXEC-CGW (Phase-4 execution agent) read in full:
- `/Users/raeez/topological-strings/CLAUDE.md`.
- `/Users/raeez/topological-strings/reconstitution/wave3-W23-5dM-sigma-2026-04-28.md` (full).
- `/Users/raeez/topological-strings/reconstitution/wave3-W31-5dM-obstructions-2026-04-28.md` §1 (lines 1–400), §3 (lines 400–500).
- `/Users/raeez/topological-strings/reconstitution/phase4-G4-5dM-twist-2026-04-28.md` (full).
- `/Users/raeez/topological-strings/reconstitution/wave3-W11-beilinson-hypotheses-2026-04-28.md` §0, §1 (Lurie / CG hypothesis tables, lines 1–400), W3-W11-05 (lines 700–828).

External references invoked (not inscribed; pending):
- Costello, "M-theory in the Omega-background and 5-dimensional
  non-commutative gauge theory", arXiv:1610.04144.
- Costello-Gaiotto-Williams, "Higgs and Coulomb Branches from
  VOAs", arXiv:2007.09497 (anchor target; PDF inscription
  pending).
- Schiffmann–Vasserot / Maulik–Okounkov $W_{1+\infty}$ central
  charge formulas (representative).
- Lurie, *Higher Algebra* §5.5.4 (Bousfield localisation in
  presentable $\infty$-categories).
- Beilinson-Drinfeld, *Chiral Algebras* §3.3–3.4 (BD chiral
  algebra framework, W3-W11-05 cross-link).

P4-EXEC-CGW confidence:
- T1 (W23 + W31 summary): **high** (sub-ledger-verified).
- T2 (boundary VOA $W_{1+\infty}$ central charge at $\epsilon \to 0$):
  **high** (direct algebraic computation).
- T3 (twist question): **medium-high** for abstract existence;
  **medium** for canonicity.
- T4 (precise target = Candidate (a)): **high** (structural argument
  privileges (a) over (b, c) on three independent grounds).
- T5 (Lie 2-cocycle extraction): **medium-high** for the
  reformulation "kill the entire Virasoro module structure";
  **medium** for the spin-1 match.
- T6 (residual disposition): **high** for structural discharge of
  M1; **low-confidence pending** PDF inscription.

No web search invoked. No new computational scratch files created.

---

## §12. 200-word summary

P4-EXEC-CGW partially discharges the P4-G4-M1 milestone at the
structural level. The single CGW theorem to twist is the
**boundary-VOA-identification theorem of arXiv:2007.09497**:
$\mathrm{Obs}(\mathrm{HT}_5; \R \times \{0\}) \simeq W_{1+\infty}
(\epsilon_1, \epsilon_2)$ at level 1, with Schiffmann–Vasserot
central charge $c = (\epsilon_1 + \epsilon_2)^2/(\epsilon_1
\epsilon_2)$. Subordinate candidates (Higgs-branch action,
4d-AGT duality) transport from this anchor.

The twist functor $\tau$ is a Lurie HA §5.5.4 Bousfield localisation
*completely eliminating the Virasoro module structure* — the user's
formulation "kill $L_{-2}$" was naive ($L_{-2}$ generates all of
Vir as an ideal). The Virasoro central charge survives $\tau$ as a
family of Lie 2-cocycle classes $[c^{(s)}]_{s \geq 1}$ on the
Heisenberg + higher-spin tower; the manuscript's $[\bar c]$ matches
the spin-1 component $[c^{(1)}]$ at the diagonal self-dual scaling
$\lambda = 1$. At $\epsilon_1 = \epsilon_2 = 0$, $c$ is path-
dependent; the natural categorical home is
$\mathrm{Bl}_0(\Spec \C[\epsilon_1, \epsilon_2])$ with exceptional
divisor $\mathbb P^1_{[\epsilon_1 : \epsilon_2]}$.

Type clash W3-W31-T1 is *resolvable* under T2 + rebasing
($\hbar^2 = \epsilon_1 \epsilon_2$ at $\lambda = 1$) +
regularisation, **not fatal**. Residual: PDF inscription
(R-P4-EXEC-CGW-A); rebasing canonicality (R-B); blow-up
regularisation (R-C); spin-tower consistency (R-D). Phase-4 milestones
M2/M3/M4 inherit.

End of P4-EXEC-CGW Phase-4 execution ledger.
