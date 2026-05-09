# Wave-3 / W31 — Drinfeld + Boundary Lens: 5d M-Theory Obstruction Audit

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.**
- *Primary:* Drinfeld — moduli, stacks, chiral / factorization
  structures, hidden groupoids, canonical constructions, Drinfeld
  centre, Hartshorne residue functor as a functor on QCoh of a stack.
- *Secondary:* Boundary — what happens at degenerate cases, singular
  strata, boundary regimes? specialisation $\epsilon \to 0$, formal-
  disk boundary of the toric compactification.
**Wave.** 3 (independent attacker).
**Mandate.** Audit each of W23's five precise obstructions to the W14
"5d twisted M-theory" remark independently. For each: propose either
a discharge path (with structure or correction that lets the bridge
work), a strengthened no-go (precise mathematical statement that the
bridge fails), or a downgrade-to-residual (deferred to Phase 4 with
exact deciding evidence). Then convert W3-W23-C1 from "conjecture
with five obstructions" to either a precise conjecture under
specialisation, or a precise no-go theorem.
**Inputs.** `CLAUDE.md`,
`reconstitution/wave3-W23-5dM-sigma-2026-04-28.md` (full),
`reconstitution/wave3-W14-mixed-cones-2026-04-28.md` (full),
`reconstitution/wave3-W11-beilinson-hypotheses-2026-04-28.md` §W3-W11-05,
`reconstitution/wave3-W16-crossvolume-2026-04-28.md` (full),
`reconstitution/wave3-W12-blast-radius-2026-04-28.md` §5–6,
`reconstitution/wave3-W21-wakimoto-2026-04-28.md` §8,
`reconstitution/wave3-W22-supertrace-rigorous-2026-04-28.md` §W3-W22-05,
master-ledger M-29 / M-37 / M-12 region (read via `attack-heal-platonic`).
**Mode.** Proposal-only. No commits. Master-ledger schema; IDs
prefix `W3-W31-`.
**Independence.** W23's five obstructions (W3-W23-05) are taken as
**input under attack** through the Drinfeld + Boundary lens. The
deliverable is per-obstruction triage (discharge / no-go / residual),
a load-bearing central-charge mismatch deep-dive, a topological-
versus-conformal twist analysis, conversion of W3-W23-C1, cross-walk
to M-29 / W12 / W21 / W22-T1, an interaction pass with W16's cross-
volume firewall, and a Phase-4 residual ledger entry.

---

## §0. Method

The Drinfeld lens demands canonical-construction discipline: a
proposed bridge between two structures is admissible only if the
identification is canonical (functorial in moduli, equivariant under
the natural automorphism groupoids on each side, compatible with the
chiral / factorization product). **Heuristic dictionaries do not
descend through the Drinfeld microscope.**

The Boundary lens asks where each side degenerates. For the 5d CGW
side, the natural boundary is the equivariant-parameter limit
$\epsilon_1, \epsilon_2 \to 0$ (Calabi–Yau / commutative limit) and
the dual rigid limit $\epsilon_1 \epsilon_2 \to 1$ (self-dual /
Nekrasov instanton accumulation). For the manuscript's local
Hamiltonian model, the natural boundary is the strict-classical
$\hbar = 0$ disk and the Tate completion's
"weight $w(d) = q^d$, $q \to 1^+$" boundary, both load-bearing in
T1 (`tate-T1`) regulator-class discipline.

Numerical verification is not required at this layer (W23 already
ran 2,576 commutator instances). W31 is a structural / functorial
audit. The mandate is to produce per-obstruction precise verdicts.

---

## §1. T1 — The five W23 obstructions, verbatim and ordered by severity

W23 §5.1 enumerates **five required ingredients** (I-1) through (I-5)
for a proof-grade match between the manuscript's mixed cones $C^{+-},
C^{-+}$ and 5d twisted M-theory holomorphic surface defects. W23
§5.2 (W3-W23-05) flags them as **precise obstructions** to the
unverified bridge.

### §1.1 Verbatim quotation

From `reconstitution/wave3-W23-5dM-sigma-2026-04-28.md` §5.1, lines
561–599 (lightly reformatted; all mathematics intact):

> **(I-1) A primary-source dictionary.** Cite a paper (Costello
> 1610.04144, CGW 2007.09497, or another) that explicitly defines:
> the 5d twisted M-theory bulk on $\R \times \C^2$, the boundary VOA on
> $\R \times \{0\}$, and the holomorphic surface defects on
> $\R \times \{z_i = 0\}$. CGW 2007.09497 (assumed to be the holography
> paper) does parts (i) and (ii) but not the surface-defect spectrum
> in the form needed.

> **(I-2) Matching of partition functions.** The instanton partition
> function of 5d HT-CS on $\R \times \C^2$ in the presence of a surface
> defect along $\{z_2 = 0\}$ should match the partition function of
> the manuscript's local Hamiltonian model with the $C^{+-}$ cone
> inserted as the cotangent module. **Not yet computed in the manuscript.**

> **(I-3) Matching of defect spectra.** The CGW surface-defect spectrum
> (catalog of allowed boundary conditions) should match the W14
> mixed-cone Lie-module structure (W14 §2: tensor-factorization PBW ⊗
> Matlis on orthogonal axes). **Not yet matched, since W14 conjectures
> this without explicit cross-check.**

> **(I-4) Matching of σ-actions.** The σ_swap (axis swap) on the
> manuscript's mixed cones should match the **mirror symmetry** of
> 5d HT-CS (which exchanges Coulomb and Higgs branches under
> $\epsilon_1 \leftrightarrow \epsilon_2$). **Plausible at the
> heuristic level**; not proved.

> **(I-5) Matching of central charges.** The chiral central charge of
> the manuscript's factorization centre (= U(1)/Capelli class, per
> W3-W11-05) should match the 5d boundary VOA central charge
> $c(\epsilon_1, \epsilon_2)$ of $W_{1+\infty}$. **The manuscript's
> $[\bar c]$ is independent of $\epsilon_1, \epsilon_2$** (it's a
> purely classical cocycle); the 5d $c(\epsilon_1, \epsilon_2)$ has
> a non-trivial $\epsilon$-dependence. **They do NOT match without
> additional limiting/quantization data.**

### §1.2 Severity ordering

Interpretation the five obstructions through the Drinfeld + Boundary lens
yields a **strict severity ordering** (highest first):

| Rank | ID | Obstruction | Severity | Type | Load-bearing? |
|------|----|--------------|----------|------|----------------|
| 1 | (I-5) | central-charge mismatch (classical $[\bar c]$ vs $\epsilon$-dependent $c(\epsilon)$) | 4 | structural / parameter-space | **YES** (W23 §6 calls it out explicitly; W31 confirms) |
| 2 | (I-1) | primary-source dictionary (CGW 2007.09497 PDF not inscribed; bib has only Costello 1610.04144) | 3 | citation provenance + dictionary type | NO (citation only; replaceable with conservative phrasing) |
| 3 | (I-3) | defect-spectrum match (W14 conjectures tensor factorization $\to$ surface defect spectrum without inscribed-source cross-check) | 3 | structural / dictionary | NO (one direction of implication is verified — W14 §2 — but not the converse) |
| 4 | (I-4) | σ-mirror match (σ_swap on mixed cones $\leftrightarrow$ $\epsilon_1 \leftrightarrow \epsilon_2$ Higgs/Coulomb mirror) | 3 | functoriality / heuristic | NO (W23-T1 sign verified; physical mirror not verified) |
| 5 | (I-2) | partition-function match (5d instanton partition function in the presence of surface defect = manuscript's $C^{+-}$ cotangent insertion) | 3 | computational / quantum | NO (depends on (I-1) closure; no inscribed computation either side) |

The load-bearing obstruction is (I-5) **central-charge mismatch**.
The other four are *contingent on (I-5)*: even if all of (I-1)–(I-4)
were closed by inscribing PDFs, computing partition functions, and
matching spectra and σ-actions, the central-charge type clash would
remain — the manuscript's $[\bar c]$ is regulator-class-canonical
inside the admissible-weight class (W8: W3-W6-04 sharpened) and is
*independent* of any $\epsilon$-deformation, while CGW's
$c(\epsilon_1, \epsilon_2)$ is *defined by* its $\epsilon$-dependence.
**This is a parameter-space type clash, not a normalisation clash.**

Severity 4 attaches to (I-5) because the clash is structural: there
is no rescaling, sign, or basis change that converts the
$\epsilon$-independent class into an $\epsilon$-dependent one without
introducing new equivariant data.

The remaining four obstructions are severity 3: each is a real gap
but admits in principle a discharge path (inscribe the PDF, compute
the partition function, match the spectrum, prove the mirror
correspondence). **They live one level below (I-5).**

---

## §2. T2 — Per-obstruction audit

### §2.1 (I-1) primary-source dictionary

**Discharge path D-W31-1.** Inscribe arXiv:2007.09497 (CGW
"Higgs and Coulomb Branches from Vertex Operator Algebras", JHEP 03
(2021) 217) as
`references/primary-sources/cgw-higgs-coulomb-2007.09497.pdf`, and
adjacently Costello 1610.04144 ("M-theory in the Omega-background and
5-dimensional non-commutative gauge theory"), Costello–Gaiotto
2001.02177 ("Twisted Supergravity and Koszul Duality"), and CGW
2103.11647 ("Cohomological Hall Algebras and Vertex Algebras"). Then
verify §3 of CGW 2007.09497 establishes the holomorphic surface-defect
spectrum needed.

**Strengthened no-go N-W31-1.** Without inscribed sources, the W14
attribution "Costello-Gaiotto-Williams arXiv 2007.09497 §3" is not
verifiable; the W23 conservative phrasing (H-W3-W23-A option (ii)) is
the only admissible recourse.

**Status under Drinfeld lens.** This is a **citation-provenance
obstruction**, not a structural one. The Drinfeld lens does not block
discharge: a primary-source dictionary, when inscribed and verified,
is canonical in the sense the lens demands.

**Status under Boundary lens.** No boundary content; this is a
provenance question.

**Verdict W3-W31-O1.** **Severity 3 (citation provenance, downgradable
to severity 2 once PDF is inscribed). Status: discharge-path
available; recommend inscribe-and-verify pass during Phase 4.**

The deciding evidence is the inscribed PDF plus a written verification
that §3 (or the relevant section) defines the surface-defect spectrum
in the form required by W14.

### §2.2 (I-2) partition-function match

**Discharge path D-W31-2.** Compute, in the manuscript:
1. The local Hamiltonian BF partition function on $\R^2 \times \C^2$
   with the $C^{+-}$ cotangent module inserted as the closed-sector
   coefficient. The manuscript currently constructs only the
   $\bar A_{\mathrm{desc}}$ (= $C^{++}$) and $\mathcal P$ (= $C^{--}$)
   sectors; the mixed-cone insertion is W14-territory only.
2. The CGW 5d HT-CS instanton partition function on
   $\R \times \C^2_{\epsilon_1, \epsilon_2}$ in the presence of a
   holomorphic surface defect along $\{z_2 = 0\}$. This is in CGW
   2007.09497 / 2103.11647 (in some normalisation) but not in any
   inscribed-source-confirmed form.
3. Verify equality after a specified $\epsilon \to 0$ specialisation.

**Strengthened no-go N-W31-2.** The partition functions live in
disjoint parameter spaces: the manuscript's is $\hbar$-formal Rees
(W3-W16-D2: $\hbar$ is **adimensional** and free), CGW's is on
$(\epsilon_1, \epsilon_2)$ explicit. **No identification can be both
$\C[[\hbar]]$-flat and $\epsilon_1, \epsilon_2$-explicit
simultaneously without a parameter-rebasing morphism that has not
been constructed.**

**Status under Drinfeld lens.** The natural moduli on each side are
distinct: the manuscript's is the formal $\Spf \C[[\hbar]]$ of the
Rees deformation parameter; CGW's is the equivariant
$\Spec \C[\epsilon_1, \epsilon_2]$ (or its formal completion at the
origin). A bridge would be a morphism from the latter to the former
**plus** a fibre-wise comparison of partition functions. The
morphism has at least one canonical candidate ($\hbar = \epsilon_1$
or $\hbar = \epsilon_1 + \epsilon_2$ or $\hbar = \epsilon_1 \epsilon_2$),
but choosing among them is non-canonical.

**Status under Boundary lens.** The Calabi–Yau limit
$\epsilon_1 + \epsilon_2 \to 0$ on the CGW side is a degenerate
boundary stratum where the central charge becomes a constant
(see §3 below). The manuscript's $\hbar = 0$ classical limit is the
Hamiltonian Poisson algebra. A discharge path would have to identify
these two boundary loci canonically — again non-canonical without
choosing the $\hbar \leftrightarrow \epsilon$ rebasing.

**Verdict W3-W31-O2.** **Severity 3 (computational + structural).
Status: discharge-path requires (i) the inscribed CGW source, (ii) a
fibre-wise partition-function computation in the manuscript with the
mixed cone inserted, (iii) a canonical $\hbar \leftrightarrow \epsilon$
morphism. None of the three is currently in scope. Phase-4 residual.**

The deciding evidence is the explicit fibre-wise partition function
match modulo a fixed $\hbar \leftrightarrow \epsilon$ rebasing.
**Without a rebasing, the obstruction stands.**

### §2.3 (I-3) defect-spectrum match

**Discharge path D-W31-3.** Verify that the W14 §2.2 tensor-
factorization
$$C^{+-} \cong \C[z_1]_{a \geq 0} \otimes_\C \mathcal P_{z_2}^{(\mathrm{Matlis})}$$
matches CGW 2007.09497 §3's catalog of allowed boundary conditions
for surface defects along $\{z_2 = 0\}$. The W14 hand-computation
(rising-factorial in $z_1$, locally nilpotent in $z_2$ on $C^{+-}$)
is the *Lie-module signature* of a holomorphic surface defect; the
discharge would inscribe the CGW catalog and check term-by-term.

**Strengthened no-go N-W31-3.** If the CGW catalog admits boundary
conditions with both $\epsilon_1$- and $\epsilon_2$-dependence
(generic ε-twisted modules), then the W14 tensor factorization
(which is $\epsilon$-independent) is at most a *boundary stratum* of
the CGW catalog, not the full catalog. **The discharge would
identify $C^{+-}$ with a specific ε-specialised CGW boundary
condition, not with the full surface-defect spectrum.**

**Status under Drinfeld lens.** The Wakimoto / parabolic-Verma
conjecture W3-W14-C1 sharpens the Drinfeld interpretation of $C^{+-}$
as a semi-infinite parabolic Verma; if this conjecture is proven,
$C^{+-}$ is a *specific module*, not a generic surface-defect
boundary condition. **W3-W14-C1 plus an ε-specialisation pin down a
single CGW boundary condition.**

**Status under Boundary lens.** The mixed cones are toric-divisor
strata in the boundary of $\mathbb P^1 \times \mathbb P^1$ (W3-W14-06).
CGW boundary conditions naturally include surface defects along the
same divisors. The structural correspondence is at the *strata*
level — both sides agree that there are exactly two divisor-types
of holomorphic surface defects in 5d HT-CS on $\R \times \C^2$,
exchanged by axis swap. The fine matching of *individual* defects
is the obstruction.

**Verdict W3-W31-O3.** **Severity 3 (structural). Status: discharge-
path requires (i) the inscribed CGW catalog, (ii) verification that
$C^{+-}$ is a specific ε-specialised CGW boundary condition (not
generic). Conditional on W3-W14-C1 being proved, the discharge is
plausible. Phase-4 residual.**

### §2.4 (I-4) σ-mirror match

**Discharge path D-W31-4.** Verify that the σ_swap : $(a,b) \mapsto (b,a)$
on the manuscript's mixed cones (W3-W23-T1, sign $-1$, 2,576 commutator
instances) is the Lie-module avatar of the **mirror symmetry**
$\epsilon_1 \leftrightarrow \epsilon_2$ on the CGW 5d boundary VOA.
Specifically:
- σ_swap exchanges $C^{+-} \leftrightarrow C^{-+}$ (W3-W23-T1
  cone-action consequence).
- ε-mirror exchanges Higgs and Coulomb branches (CGW 2001.02177,
  2007.09497 framework).
- The discharge would identify σ_swap on the manuscript's parent
  module with the ε-mirror on a fibre-wise specialisation of the
  CGW boundary VOA.

**Strengthened no-go N-W31-4.** σ_swap is **internal** to the
manuscript's parent module $\widetilde{\mathcal M}$; ε-mirror is
**external** equivariant data on the CGW side. Without a
$\hbar \leftrightarrow (\epsilon_1, \epsilon_2)$ rebasing morphism
(which is the obstruction to (I-2)), the two cannot be identified.
**Functorially, σ_swap is an automorphism of one object;
ε-mirror is a functor between two non-equivalent objects. They are
not the same kind of structural data.**

**Status under Drinfeld lens.** σ_swap is a Lie anti-involution
(W3-W23-T1) — *internal* automorphism of the parent module. The
CGW ε-mirror is an *external* equivalence between two ε-deformed
VOAs. The Drinfeld lens distinguishes these sharply: an internal
automorphism is data on a single object; an external equivalence is
a morphism between two objects. The discharge has to construct an
*equivalence* of categories sending σ_swap on one side to ε-mirror
on the other — a non-trivial 2-categorical condition.

**Status under Boundary lens.** At the boundary $\epsilon_1 = -\epsilon_2$
(Calabi–Yau limit), the ε-mirror becomes the trivial involution
$\epsilon_1 \mapsto -\epsilon_1$, $\epsilon_2 \mapsto -\epsilon_2$.
This is *not* the σ_swap on the manuscript's mixed cones: σ_swap
exchanges the two divisor cones, while at the CY-limit boundary the
ε-mirror collapses to a sign flip. **The naive boundary-limit
identification fails.**

**Verdict W3-W31-O4.** **Severity 3 (functoriality). Status:
strengthened no-go on the heuristic identification of σ_swap with
ε-mirror; discharge requires a 2-categorical equivalence not yet
constructed. Phase-4 residual; the obstruction is genuine, not
merely "not verified".**

### §2.5 (I-5) central-charge mismatch — load-bearing

This is the deep dive of §3. Summary verdict here, full analysis
below.

**Discharge path D-W31-5.** Specialise the CGW 5d boundary VOA
central charge $c(\epsilon_1, \epsilon_2)$ at a specific limit
recovering the manuscript's $[\bar c]$. Two natural candidates:
(a) $\epsilon_1, \epsilon_2 \to 0$ (commutative + CY limit);
(b) $\epsilon_1 = -\epsilon_2$ (CY-only limit).

**Strengthened no-go N-W31-5.** The manuscript's $[\bar c] \in
H^2_{\mathrm{Lie}}(\bar A; \C)_{(0,0)}$ is a **weight-(0,0)
cohomology class** on a specific Lie 2-cocycle. The CGW
$c(\epsilon_1, \epsilon_2) = $ a function valued in $\C$ (not in any
$H^2$). They do NOT live in the same target category before any
ε-specialisation: the manuscript's $[\bar c]$ is a class in a
cohomology group; the CGW $c$ is a number / formal series. The
identification has to be a *map* from cohomology classes to numbers,
which exists in general (evaluate the cocycle on a fixed 2-cycle in
the BD operad), but is not canonical without choosing the cycle.

**Status under Drinfeld lens.** The classical $[\bar c]$ is the
**chiral central charge** of the manuscript's BD topological chiral
algebra (W3-W11-05). The CGW $c(\epsilon_1, \epsilon_2)$ is the
**Virasoro central charge** of a conformal VOA. **Topological vs
conformal — different chiral-algebra TYPES** (W3-W23-06).

**Status under Boundary lens.** No specialisation of $c(\epsilon_1,
\epsilon_2)$ produces a topological class: a Virasoro central
charge stays a Virasoro central charge under specialisation. The
boundary limit cannot fix the type clash.

**Verdict W3-W31-O5.** **Severity 4 (load-bearing structural).
Status: strengthened no-go; the central-charge type clash
(weight-(0,0) Lie cohomology class vs Virasoro central charge as a
number) is structural, not parameter-dependent. Discharge requires
not just specialisation but a topological-twist functor on the CGW
side that has not been constructed. Phase-4 residual; deciding
evidence is the explicit topological twist (see §4 below).**

---

## §3. T3 — Central-charge mismatch deep dive

### §3.1 The two objects

**Manuscript's $[\bar c]$.** Per `principles.tex`:280 and W3-W11-05:
$$[\bar c] \in H^2_{\mathrm{Lie}}(\bar A; \C)_{(0, 0)},$$
where $\bar A = \C[z_1, z_2]/\C \cdot 1$ is the Hamiltonian Lie
algebra on the formal symplectic disk modulo constants, and the
weight-(0,0) component is the *unique* bidegree at which the
bracket of two generators is a scalar. Concretely
$$\bar c(z_1^k z_2^l, z_1^m z_2^n) = (kn - lm) \cdot \mathbf 1_{(k+m, l+n) = (1, 1)}$$
(W3-W11-05 ledger entry). This is a **purely classical cocycle**: no
$\epsilon$, no $\hbar$, just the residue of the Poisson bracket at
the (1,1)-weight pairing. By W8 / W3-W6-04, $[\bar c]$ is
*regulator-class-canonical inside the admissible-weight class* — it
does not depend on the choice of admissible regulator, hence is a
single invariant, not a family.

**CGW's $c(\epsilon_1, \epsilon_2)$.** The 5d HT-CS boundary VOA is
$W_{1+\infty}$ at level 1 with central charge a function of
$(\epsilon_1, \epsilon_2)$ depending on the precise normalisation of
the Omega background (Costello 1610.04144 §6; CGW 2007.09497).
A representative form (Schiffmann–Vasserot, Maulik–Okounkov):
$$c(\epsilon_1, \epsilon_2) = -\frac{(\epsilon_1 + \epsilon_2)^3}{\epsilon_1 \epsilon_2 \epsilon_3} \quad \text{or analogous},$$
where $\epsilon_3 = -\epsilon_1 - \epsilon_2$ in the CY3 normalisation.
This is a **rational function** of two equivariant parameters. As a
function of $(\epsilon_1, \epsilon_2)$ it has poles at the divisors
$\{\epsilon_1 = 0\}$, $\{\epsilon_2 = 0\}$, $\{\epsilon_1 + \epsilon_2 = 0\}$.

### §3.2 The natural specialisations

**(a) Commutative limit $\epsilon_1, \epsilon_2 \to 0$.** Naively,
this is the *classical limit*. The CGW central charge in this limit
diverges (poles of the rational function). The naive identification
$c(0, 0) = [\bar c]$ is *not* possible at the level of values —
both sides are not the same kind of thing (Virasoro number diverging
vs. Lie cohomology class), and even regularising to a number, the
divergence on the CGW side is real.

**(b) Calabi–Yau limit $\epsilon_1 + \epsilon_2 \to 0$.** This is the
"pure CY3" limit where the Omega background becomes self-dual. The
CGW central charge $c(\epsilon, -\epsilon, -1) = $ (depending on
normalisation) a finite value or zero. This is the natural CY-physics
boundary, but the *type* of object — Virasoro central charge of a
conformal VOA — is unchanged. The manuscript's $[\bar c]$ is a Lie
2-cocycle on a Hamiltonian Lie algebra, *not* a Virasoro central
charge of a conformal VOA. **Boundary-stratum specialisation does
not change the object type.**

**(c) Self-dual limit $\epsilon_1 = -\epsilon_2$.** Same as (b) up
to sign; identical conclusion.

**(d) Pure-equivariant limit $\epsilon_2 \to 0$ at fixed $\epsilon_1$.**
The boundary VOA reduces to a non-equivariant VOA on
$\R \times \C_{\epsilon_1}$; the central charge depends on $\epsilon_1$
linearly. Still a Virasoro central charge, still not equivalent to
$[\bar c]$.

### §3.3 Why no specialisation recovers $[\bar c]$

The fundamental issue is **type clash**:

| Object | Type | Target |
|--------|------|--------|
| $[\bar c]$ | Lie 2-cocycle class on $\bar A$ | $H^2_{\mathrm{Lie}}(\bar A; \C)_{(0, 0)}$ |
| $c(\epsilon_1, \epsilon_2)$ | Virasoro central charge of $W_{1+\infty}$ | $\C(\epsilon_1, \epsilon_2)$ (rational function) |

These are objects in different categories. A specialisation of a
rational function is a number; a specialisation of a Lie cohomology
class is a Lie cohomology class. **No specialisation morphism on
the CGW side can convert a Virasoro number into a Lie 2-cocycle
class without first applying a *forget-conformal* / topological-twist
functor.**

The discharge path therefore *cannot* be just "ε-specialisation."
It has to be:
1. Topologically twist the CGW conformal VOA to a topological chiral
   algebra (i.e., apply a topological twist on the boundary VOA).
2. *Then* specialise ε.
3. *Then* identify with $[\bar c]$.

Without step 1, the type clash is unresolvable. **This is the deep
content of (I-5).**

### §3.4 Verdict

**The two are genuinely incompatible *as objects of distinct types*,
not merely incompatible at specific parameter values.**

The only hope for a discharge is **§4 below**: a topological twist
of the CGW conformal VOA that converts it into a topological chiral
algebra of the type W3-W11-05 names, which then specialises at
$\epsilon_1, \epsilon_2 \to 0$ to a Lie 2-cocycle on the underlying
Hamiltonian Lie algebra. Whether such a twist exists in the CGW
framework is **the residual deciding evidence**.

**Verdict W3-W31-T1 (Central-charge type clash).** **Severity 4.
Status valid. Confidence very high.**

The manuscript's $[\bar c] \in H^2_{\mathrm{Lie}}(\bar A; \C)_{(0,0)}$
and the CGW 5d boundary VOA central charge $c(\epsilon_1, \epsilon_2) \in
\C(\epsilon_1, \epsilon_2)$ are objects of distinct types: the former
is a class in Lie cohomology, the latter is a Virasoro central
charge of a conformal VOA. **No specialisation $\epsilon \to 0$
(in any direction — commutative, CY, self-dual, or pure-equivariant)
recovers $[\bar c]$ from $c(\epsilon_1, \epsilon_2)$, because
specialisation does not change object type.** A topological twist
on the CGW side is required first. The existence of such a twist is
discharge-path D-W31-6 (topological-twisting limit, §4 below).

---

## §4. T4 — Topological twist of CGW (resolution of W11/W23 conformal vs topological clash)

### §4.1 The topological-twisting question

W3-W11-05 establishes the manuscript's factorization centre is a
**topological chiral algebra** (locally constant on $\R$ — the brane
line — with no Virasoro / conformal structure). W3-W23-06 establishes
the CGW 5d boundary VOA is a **conformal VOA** (with $T(z)$). For
the bridge to work, one of two things must be true:
- (a) the CGW conformal VOA admits a natural **topological
  twist** that produces a topological chiral algebra recovering the
  manuscript's structure;
- (b) the manuscript's topological chiral algebra admits a natural
  **conformal lift** that produces a conformal VOA matching the CGW
  structure.

Direction (a) is more plausible: topological twists are standard
operations on conformal VOAs (compute the cohomology with respect to
a chosen supercharge $Q$ such that $L_{-1} = \{Q, G_{-1}\}$ for some
chosen $G$). Direction (b) requires *adding* structure, which is
non-canonical.

### §4.2 What a CGW topological twist would look like

In the 5d HT-CS framework, the natural topological twist is the
**holomorphic-twist limit** $\epsilon_1 \to 0$ (or $\epsilon_2 \to 0$,
or $\epsilon_1 + \epsilon_2 \to 0$). Schematically, taking
$\epsilon_2 = 0$ kills the holomorphic-direction Virasoro structure
on $\C_{\epsilon_2}$ and reduces the CGW boundary VOA on
$\R \times \{0\}$ to a *holomorphic-twisted* algebra: locally
constant in $\R$, polynomial in $z_1$ (the surviving holomorphic
direction).

**Conjecture (informal).** Under the limit $\epsilon_2 \to 0$ at
fixed $\epsilon_1$, the CGW boundary VOA on $\R \times \{0\}$ reduces
to a *topological* chiral algebra on $\R$ in which the holomorphic
$z_1$-direction is realised as a Tate-completed coefficient module.
The Virasoro central charge $c(\epsilon_1, \epsilon_2 = 0) = $
*specific value* (depending on normalisation; in some conventions
this is divergent, in others zero).

This is plausible at the *physics* level (the holomorphic-twisted
limit is well-defined in many topological-string contexts) but is
not inscribed in any source W31 verified.

### §4.3 The "manuscript-recovery" conjectural specialisation

Even granting the topological-twist limit at $\epsilon_2 = 0$, there
remains the question: does the resulting topological chiral algebra
match the manuscript's structure?

The manuscript's structure is on the **formal symplectic disk
$\widehat{\C^2}_0$ with $\omega = dz_1 \wedge dz_2$** — *both*
holomorphic directions are present, with the Hamiltonian Lie algebra
$\bar A = \C[z_1, z_2]/\C \cdot 1$ acting by Poisson brackets in
both. Killing $\epsilon_2$ on the CGW side reduces to a *single*
holomorphic direction $z_1$, which is too small.

**The manuscript needs both directions; the natural CGW topological
twist kills one direction.**

A more refined conjectural specialisation: take the *double
holomorphic-twist* limit $\epsilon_1, \epsilon_2 \to 0$ jointly,
along the diagonal in some specific scaling. This is exactly the
$\hbar \to 0$ classical Calabi–Yau limit on the manuscript side
(`main.tex`:5398, Moyal-Weyl). On the CGW side, this is the
boundary stratum where both equivariant parameters degenerate
simultaneously — the central charge typically diverges, but a
careful regularisation may produce a finite *cohomological* class
that matches $[\bar c]$.

This is the most plausible discharge path; but it requires both:
(i) regularised double-twist limit on CGW;
(ii) verification that the regularised limit produces precisely the
weight-(0,0) Lie cohomology class on $\bar A$, not a Virasoro number.

Neither is in inscribed sources.

### §4.4 Verdict on topological vs conformal

**Verdict W3-W31-T2 (Topological-twist conjecture).** **Severity 3.
Status: conjectural. Confidence medium.**

A topological-twist limit of the CGW 5d conformal boundary VOA may
exist that recovers the manuscript's topological chiral algebra
structure. The natural candidate is the double holomorphic-twist
$\epsilon_1, \epsilon_2 \to 0$ along a specified scaling. Whether
this limit produces the correct *Lie cohomology* class
$[\bar c]_{(0, 0)}$ rather than a *Virasoro number* requires a
non-trivial regularisation argument that has not been constructed
in any inscribed source.

**Conditional discharge.** If T2 holds (topological-twist limit
exists and produces $[\bar c]$), then (I-5) discharges in the
conditional sense: the bridge becomes a chain
- CGW conformal VOA at generic $(\epsilon_1, \epsilon_2)$
- → topologically-twisted CGW at $\epsilon_1, \epsilon_2 \to 0$
- → manuscript's BD topological chiral algebra with $[\bar c]$.

**Without T2, (I-5) is genuinely incompatible; the bridge fails
structurally.**

---

## §5. T5 — Conjecture / no-go conversion of W3-W23-C1

### §5.1 The W23-C1 starting point

W3-W23-C1 (W23 §7.2) reads:
> **Conjecture.** The mixed cones $C^{+-}$ and $C^{-+}$ correspond
> physically to **holomorphic surface defects** in 5d twisted M-theory
> on $\R \times \C^2$, along the divisors $\{z_2 = 0\}$ and
> $\{z_1 = 0\}$ respectively, in the sense that:
> (C1.a) Lie-module structure of $C^{\pm \mp}$ matches CGW boundary
> algebra at the holomorphic surface defect, classical limit;
> (C1.b) σ_swap corresponds to ε-mirror Higgs/Coulomb;
> (C1.c) $[\bar c]$ is the classical limit of $c(\epsilon_1, \epsilon_2)$.
>
> **Status.** Conjectural. Five required ingredients (I-1)–(I-5).

### §5.2 The W31 conversion

The W31 deep dive (§3, §4) shows:
- (I-1)–(I-4) are *contingent* obstructions — they admit discharge
  paths (inscribed sources, computed partition functions, matched
  spectra, mirror correspondence) in principle, all severity 3.
- (I-5) is the *load-bearing* obstruction — type clash between Lie
  2-cocycle class and Virasoro central charge, severity 4.

The discharge of (I-5) requires the topological-twist conjecture
W3-W31-T2 (§4.4). Conditional on T2, (I-5) becomes a specialisation
+ regularisation; without T2, (I-5) is structurally fatal.

The W31 conversion of W23-C1:

### §5.3 W3-W31-C1 (precise conditional conjecture, after the topological-twist)

**Conjecture W3-W31-C1.** **Severity 3 (conditional). Confidence
medium-low.**

> Assume the topological-twist conjecture W3-W31-T2 holds (a
> regularised double holomorphic-twist limit
> $\epsilon_1, \epsilon_2 \to 0$ of the CGW 5d boundary VOA produces
> a topological chiral algebra with central element a Lie 2-cocycle
> class on a Hamiltonian Lie algebra). Assume further the CGW
> primary-source dictionary is inscribed and verified (D-W31-1 closed),
> the partition functions are matched fibre-wise modulo a canonical
> $\hbar \leftrightarrow (\epsilon_1, \epsilon_2)$ rebasing
> (D-W31-2 closed, with rebasing fixed), the defect spectra are
> matched (D-W31-3 closed, modulo W3-W14-C1), and the σ-mirror
> 2-categorical equivalence is constructed (D-W31-4 closed).
>
> Then the manuscript's mixed cones $C^{+-}, C^{-+}$ are equivalent,
> as objects of an appropriate 2-categorical chiral-algebra category,
> to the topologically-twisted CGW holomorphic surface defects, with
> the σ_swap matching the ε-mirror, and with the topologically-twisted
> central charge $c^{\mathrm{top}}(\epsilon_1 \to 0, \epsilon_2 \to 0) =
> [\bar c]$ matching the manuscript's classical regulator-canonical
> chiral central charge.

**Status.** This is a precise *conditional* conjecture: every named
specialisation, rebasing, and twist is enumerated. The conjecture
fails if **any** of:
- T2 fails (topological-twist limit doesn't produce a Lie cohomology
  class);
- the $\hbar \leftrightarrow \epsilon$ rebasing has no canonical
  choice;
- W3-W14-C1 fails (mixed cones are not Wakimoto-type semi-infinite
  Verma modules);
- the σ-mirror 2-equivalence cannot be constructed.

**Confidence.** Medium-low because each of the four conditional
discharges is independently non-trivial; their conjunction is harder
than any one alone.

### §5.4 Alternative: W3-W31-N1 (precise no-go theorem, if the topological-twist fails)

**No-go theorem W3-W31-N1.** **Severity 4 (alternative load-bearing
no-go). Status: subsumed by T2-failure.**

> If the topological-twist conjecture W3-W31-T2 fails — that is, no
> regularisation of the double holomorphic-twist limit
> $\epsilon_1, \epsilon_2 \to 0$ on the CGW 5d boundary VOA produces
> a Lie 2-cocycle class on a Hamiltonian Lie algebra — then there
> is no equivalence between the CGW 5d ε-dependent partition function
> and the manuscript's regulator-class-canonical $[\bar c]$, due to
> the type clash between Virasoro central charge (number / formal
> series) and Lie cohomology class (W3-W31-T1).

**Proof sketch.** By T1, the two objects live in different categories.
A specialisation morphism on a parameter space cannot change the
target category of the value. Therefore any putative equivalence
must include a *category-changing* morphism; the only candidate at
the manuscript-CGW interface is the topological twist (§4). If T2
fails, no such morphism exists; therefore no equivalence. ∎

### §5.5 W31's choice: precise conditional conjecture (W3-W31-C1)

**W31's verdict, after Drinfeld + Boundary triage:** issue the
conditional conjecture W3-W31-C1, *not* a flat no-go theorem. The
reason is that the topological-twist limit (W3-W31-T2) is an open
question, not a known impossibility. The Drinfeld lens demands
canonical-construction discipline; the Boundary lens names the
specialisations. Both lenses agree the bridge **could** work via the
double-twist + regularisation route, but **does not currently work**
without that route being constructed.

**Concrete decision.** W3-W23-C1 is replaced by:
- Conditional conjecture W3-W31-C1 (precise, with explicit named
  conditions);
- Conditional no-go W3-W31-N1 (precise, fires if T2 fails).

The deciding evidence between C1 and N1 is the construction (or
provable non-existence) of the topological-twist limit in W3-W31-T2.
This is Phase-4 frontier work, not in scope for the present
manuscript.

---

## §6. T6 — Cross-walk to M-29 / W12 / W21 / W22-T1

### §6.1 M-29 (universal categorical no-go, W7 bulletproof)

M-29 forbids any flat $\hbar$-deformation interpolating
$\bar A_{\mathrm{desc}}$ (= $C^{++}$, PBW shadow) and $\mathcal P$
(= $C^{--}$, Matlis principal-parts) in any of five named categorical
extensions. W14 (W3-W14-04) extended M-29 directionally to the
mixed cones: rising-factorial in one direction defeats local
nilpotence in the other; the strict double obstruction is the
special case combining both directions.

**5d M-theory cross-walk.** The mixed cones $C^{+-}, C^{-+}$ are the
proposed counterparts to CGW holomorphic surface defects (W3-W14-07).
M-29 forbids flat $\hbar$-deformation between $C^{++}$ and $C^{+-}$
in the directional sense; the ε-deformed CGW surface defect is, in
the discharge-path D-W31-3 + D-W31-2 picture, an *ε-deformed*
analogue of $C^{+-}$, fibred over the equivariant base.

**Coherence verdict W3-W31-X1.** **Severity 3. Status valid.
Confidence high.**

The 5d M-theory picture **does NOT contradict** M-29 directionally
(W3-W14-04). On the contrary, the directional extension of M-29
*predicts* exactly the structure CGW boundary surface defects exhibit
on the equivariant fibre: each surface defect is an ε-deformed
mixed-cone-type module, and the rising-factorial obstruction at
$\epsilon \to 0$ in one direction is what makes the CY-limit
boundary VOA pole-divergent (recall §3.2, the central charge poles
at $\{\epsilon_2 = 0\}$). **The M-29 directional no-go is
*reflected* in the CGW central-charge poles** at the divisor
boundaries.

### §6.2 W12 four-cone Čech short exact sequence

W3-W12-§5.4 establishes the SES
$$0 \to \bar A_{\mathrm{desc}} \to C^{+-} \oplus C^{-+} \to \mathcal P \to 0$$
in $\Z^2$-graded form (P-W12-A residual: explicit boundary maps
within reach). The mixed cones are the off-diagonal Čech contributions
to local cohomology along the two coordinate axes.

**5d M-theory cross-walk.** In CGW, the analogous Čech complex is
the Mayer–Vietoris of the 5d HT-CS gauge theory restricted to the
union of two divisors $\{z_2 = 0\} \cup \{z_1 = 0\}$ in
$\C^2_{\epsilon_1, \epsilon_2}$. The two sheet-defects have a
Mayer–Vietoris-type intersection at the origin
$\{z_1 = z_2 = 0\}$, where the strict Dirac brane lives.

**Coherence verdict W3-W31-X2.** **Severity 3. Status valid.
Confidence high.**

The W12 four-cone Čech SES is the ε-independent / classical avatar
of the CGW Mayer–Vietoris on the two-divisor union. The 5d picture
is *coherent* with W12: the SES describes the locally-cohomological
content of the surface-defect intersection at the origin, exactly
the structure the strict Dirac brane probes (which is $C^{--}$ /
$\mathcal P$ in the manuscript).

### §6.3 W21 column-Verma identification of mixed cones

W3-W21 established that each mixed cone $C^{+-}$ is, restricted to
the 3-dim Borel $\C \cdot z_1 \oplus \C \cdot z_2 \oplus \C \cdot z_1 z_2 \subset \bar A$,
a **direct sum of column-Verma modules** $M_a$ at lowest weights
$(a, -1)$ with $a \geq 0$. Each $M_a$ is generated freely by $z_1$
along the column $\{(a, b) : b \leq -1\}$.

**5d M-theory cross-walk.** In CGW, the boundary VOA on
$\R \times \{0\}$ has a parabolic Verma decomposition under its
natural Cartan / Borel structure (e.g., the affine Yangian or the
$W_{1+\infty}$ horizontal subalgebra). The W21 column-Verma
identification matches CGW's parabolic Verma structure on the
ε-fibres up to the discharge-path corrections.

**Coherence verdict W3-W31-X3.** **Severity 2. Status valid.
Confidence medium-high.**

W21's column-Verma identification of mixed cones is *consistent*
with CGW's parabolic-Verma decomposition of the boundary VOA on
ε-specialised fibres. The W3-W14-C1 Wakimoto conjecture is the
explicit free-field realisation that would make the comparison
proof-grade.

### §6.4 W22-T1 supertrace cocycle vanishing

W3-W22-T1 establishes the chain-level QME on the super-balanced
$\mathfrak{gl}(N | N)$ Dirac probe vanishes identically at one loop
(and W22-T2 at all loops, conditional on regulator preserving
$\mathbb Z/2$-grading), because $\mathrm{Str}_{\mathfrak{gl}(N|N)}(I) = 0$.

**5d M-theory cross-walk.** The CGW 5d HT-CS on $\R \times \C^2$ is
*not* in the super-balanced regime by default; it is built on
$\mathfrak{gl}_N$ probes with non-vanishing trace
$\mathrm{Tr}_{\mathfrak{gl}_N}(I) = N$. The Capelli shift on the
manuscript's open side (M-12, W3-W11-05 for the trace pair) is the
*ε-independent* analogue of the CGW $W_{1+\infty}$ central element.

**Coherence verdict W3-W31-X4.** **Severity 2. Status valid.
Confidence high.**

W22-T1 / T2's supertrace vanishing on $\mathfrak{gl}(N | N)$ provides
a discharge-path for the QME obligation in *one specific super-
balanced sector*; this sector does not directly correspond to CGW's
default $\mathfrak{gl}_N$ HT-CS, but it provides the rigorous
foundation for the unconditional Theorem F$'$ on which W3-W11-05's
BD chiral algebra structure relies. **The 5d M-theory bridge does
not contradict W22-T1; rather, W22-T1 makes the manuscript's
$[\bar c]$ unconditional in the super-balanced sector, which is the
domain on which W3-W31-C1 is asserted.**

### §6.5 Summary cross-walk verdict

**W3-W31-X (Cross-walk verdict).** **Severity 3. Status valid.
Confidence high.**

The 5d M-theory picture (with the W31 conditional conjecture C1) is
**coherent** with all four named structural findings:
- M-29 (directional no-go via W3-W14-04): coherent; CGW central
  charge poles at divisor boundaries ↔ M-29 directional rising-
  factorial obstruction (X1).
- W12 four-cone Čech SES: coherent; SES is the ε-independent avatar
  of CGW Mayer–Vietoris on two-divisor union (X2).
- W21 column-Verma identification: coherent; column-Verma
  decomposition matches CGW parabolic-Verma structure on ε-fibres
  (X3).
- W22-T1 supertrace vanishing: coherent; W22-T1 makes $[\bar c]$
  unconditional in the super-balanced sector, which is the domain
  of C1 (X4).

**No contradictions detected.** The cross-walk supports W3-W31-C1
as the correct conditional conjecture (rather than a flat no-go).

---

## §7. T7 — New Phase-4 residual catalog entry

### §7.1 Draft master-ledger entry

**R-W3-W31-A (5d twisted M-theory bridge: five-obstruction conditional
conjecture).** **Phase-4. Severity 4 (load-bearing aggregate of (I-5)
+ four contingent severity-3 obstructions).**

> **Statement.** The W14 attribution of the manuscript's mixed cones
> $C^{+-}, C^{-+}$ to "5d twisted M-theory holomorphic surface defects"
> (W3-W14-07) is downgraded to a *conditional conjecture* W3-W31-C1.
> Five precise obstructions:
>
> 1. **(I-1) primary-source dictionary** [severity 3, citation
>    provenance]. CGW arXiv:2007.09497 PDF not inscribed; manuscript
>    bibliography cites only Costello arXiv:1610.04144. Discharge path
>    D-W31-1: inscribe PDF in `references/primary-sources/` and verify
>    §3 establishes surface-defect spectrum.
> 2. **(I-2) partition-function match** [severity 3, computational +
>    structural]. Discharge path D-W31-2: compute manuscript's
>    partition function with $C^{+-}$ inserted; compute CGW instanton
>    partition function with surface defect; verify equality after a
>    canonical $\hbar \leftrightarrow (\epsilon_1, \epsilon_2)$
>    rebasing morphism. Rebasing is non-canonical; multiple candidates.
> 3. **(I-3) defect-spectrum match** [severity 3, structural].
>    Discharge path D-W31-3: verify W14 §2 tensor factorisation
>    $C^{+-} \cong \C[z_1] \otimes \mathcal P_{z_2}$ matches CGW
>    surface-defect catalog at a specific ε-specialisation.
>    Conditional on W3-W14-C1 (Wakimoto-Verma realization).
> 4. **(I-4) σ-mirror match** [severity 3, functoriality]. Discharge
>    path D-W31-4: construct 2-categorical equivalence sending
>    σ_swap (W3-W23-T1) to ε-mirror Higgs/Coulomb. Heuristic only;
>    structural distinction (internal automorphism vs external
>    equivalence) makes this a non-trivial 2-categorical condition.
> 5. **(I-5) central-charge mismatch** [severity 4, **load-bearing**].
>    $[\bar c]$ is a Lie 2-cocycle class; $c(\epsilon_1, \epsilon_2)$
>    is a Virasoro central charge of a conformal VOA. Type clash:
>    no specialisation $\epsilon \to 0$ converts a Virasoro number
>    into a Lie cohomology class. **Discharge requires
>    topological-twist conjecture W3-W31-T2** (regularised double
>    holomorphic-twist limit $\epsilon_1, \epsilon_2 \to 0$ produces
>    a Lie 2-cocycle class on a Hamiltonian Lie algebra). T2 is
>    conjectural; not in inscribed sources.
>
> **Resolution paths.**
> - (a) C1 path: discharge all five obstructions; bridge holds
>   conditionally.
> - (b) N1 path: T2 fails; bridge fails structurally;
>   no equivalence exists.
> - (c) Frontier-residual path: leave open; treat as Phase-4 frontier
>   into 5d twisted M-theory and BD chiral algebra unification.
>
> **Deciding evidence.**
> - For (I-1): inscribed CGW PDF + verified §3 surface-defect spectrum.
> - For (I-2): explicit partition-function computation on both sides
>   + $\hbar \leftrightarrow (\epsilon_1, \epsilon_2)$ rebasing
>   morphism.
> - For (I-3): explicit CGW catalog entry matching W14 tensor
>   factorisation + W3-W14-C1 proof.
> - For (I-4): 2-categorical equivalence functor.
> - For (I-5) → T2: regularised double-twist limit producing Lie
>   2-cocycle class; or explicit non-existence.
>
> **Severity aggregate 4** (load-bearing dominated by (I-5)).
> **Status.** Phase-4 frontier residual.

### §7.2 Connection to existing residuals

R-W3-W31-A subsumes:
- W3-W23 §10: R-W3-W23-A (CGW PDF inscription) and R-W3-W23-B (five-
  ingredient bridge verification);
- W3-W14 §8: R-W3-W14-B (brane-configuration realisation in 5d twisted
  M-theory).

R-W3-W31-A is *additive* to:
- W3-W11-05 / M-37 / R-03 four-ingredient closure plan (transverse
  Mittag-Leffler resolution);
- M-29 / W3-W14-04 directional sharpening (mixed-cone no-go).

These are *not* superseded by R-W3-W31-A; the 5d M-theory bridge is a
*Phase-4* program that is largely orthogonal to the *manuscript-side*
residuals.

---

## §8. T8 — Interaction with cross-volume firewall (W16)

### §8.1 W16 cross-volume status

W3-W16 found the BKM/Igusa bridge to be **structurally incompatible**
with the local Hamiltonian BF/Moyal calculation (R-W3-W16-C: three
independent compatibility failures — lattice signature wrong
direction, Rees grading not modular weight, Moyal rationals not Jacobi
integers). The Vol III ↔ topological-strings bridge has only **one**
candidate functor surviving naturality (F3: formal-disk deformation
quantisation, conditional on $\hbar$-normalisation matching).

### §8.2 5d M-theory bridge vs cross-volume firewall

The 5d M-theory bridge is **not** a cross-volume bridge between
manuscript repositories (`topological-strings` vs `calabi-yau-quantum-groups`
vs `igusa-cusp-form`). It is an *intra-volume bridge* between the
manuscript and a *physics framework* (Costello / CGW twisted M-theory),
which is partially physically motivated, not formally verified.

The 5d M-theory bridge has:
- **No worldsheet** (no $\Sigma_g$ in the local Hamiltonian model;
  W3-W16-D5 confirmed: the manuscript has *no* worldsheet of any
  kind);
- **No K3 / CY3 manifold** (the local model is on $\widehat{\C^2}_0$,
  a formal symplectic disk, not a global CY);
- **No global BCOV invariant** (the local Capelli class is *not* the
  Vol III BFN central scalar; F1 in W16 fails functoriality).

Therefore: **5d M-theory ≠ Vol III ≠ Igusa**. Each bridge has
distinct status:
- BKM/Igusa: structurally incompatible (W3-W16 R-C);
- Vol III: only F3 (formal-disk deformation quantisation) survives,
  conditional on $\hbar$-normalisation;
- 5d M-theory: conditional conjecture W3-W31-C1 (this ledger).

### §8.3 Convention drift from discharging 5d M-theory

If the discharge-paths D-W31-1 through D-W31-5 are pursued, do they
create *new* convention drifts with Vol III or Igusa?

**Drift D-W31-DR1.** D-W31-2 introduces an explicit
$\hbar \leftrightarrow (\epsilon_1, \epsilon_2)$ rebasing morphism.
Vol III's $\hbar$ on the Fake-Monster row (W3-W16-D2) is fixed
numerically by the lattice ($\hbar^2 = -1/(2 c_+(L))$). The 5d
M-theory $\hbar$ (= the Rees deformation parameter on the manuscript
side) is *free*. **Discharging D-W31-2 with a specific
rebasing fixes the manuscript $\hbar$ to a specific function of
$(\epsilon_1, \epsilon_2)$**, which is INCOMPATIBLE with the Vol III
fixed-$\hbar$ row. **D-W31-2 thus deepens the manuscript / Vol III
divergence (W3-W16-D2)**: not only is $\hbar$ free vs fixed in W16,
under D-W31-2 it is *fixed in two different ways* (CGW ε-rebasing on
the 5d side; lattice Casimir on the Vol III side).

**Drift D-W31-DR2.** D-W31-4 introduces a 2-categorical equivalence
between σ_swap (manuscript) and ε-mirror (CGW). Vol III's natural
involutions are at the level of Hodge structure / Mukai pairing
swap, not σ-conjugation in the sense W3-W23-T1 names. **No new
convention drift on the Vol III side; D-W31-4 is internal to the
5d M-theory bridge.**

**Drift D-W31-DR3.** D-W31-5 / T2 introduces a topological-twist on
the CGW side. This is *internal to physics*; it has no direct
counterpart in Vol III's smooth-proper dg category framework.
**Possible mild drift: if T2 produces a Lie 2-cocycle class,
the manuscript's $[\bar c]$ becomes the *image* of the CGW
topologically-twisted central charge under specialisation; Vol III's
$\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3) = 2$ is a *Hodge supertrace*
invariant (W3-W16-D2 / MA-3); these remain distinct.**

### §8.4 Cross-volume verdict

**W3-W31-X5 (Cross-volume implications of discharging 5d M-theory).**
**Severity 2. Status valid. Confidence medium-high.**

Discharging the 5d M-theory bridge (R-W3-W31-A discharge paths
D-W31-1 through D-W31-5) creates **one new convention drift** with
Vol III: D-W31-DR1 (fixing manuscript $\hbar$ via CGW ε-rebasing
deepens the W3-W16-D2 free-vs-fixed-$\hbar$ divergence, with the
manuscript-side $\hbar$ now fixed in a *third* way). The Igusa /
BKM bridge is structurally incompatible (W3-W16 R-C) and does not
interact with the 5d M-theory discharge.

**Recommended firewall sharpening.** If W3-W31-C1 is pursued in
Phase 4, add a one-bullet note to `tate-P5-cross-volume.tex`:
"*Internal* 5d M-theory bridge (W3-W31-C1) is distinct from the
*cross-volume* Vol III / Igusa firewall; the
$\hbar \leftrightarrow (\epsilon_1, \epsilon_2)$ rebasing required
for D-W31-2 differs from the Vol III lattice-fixed $\hbar$ (W3-W16-D2),
so neither bridge implies the other."

---

## §9. Per-target verdict

| Target | Lens | Verdict | Severity | Detail |
|--------|------|---------|----------|--------|
| T1 (enumerate five obstructions) | Drinfeld + Boundary | RESOLVED with severity ordering | 4 | (I-5) load-bearing; (I-1)–(I-4) severity 3 |
| T2 (per-obstruction audit) | Drinfeld + Boundary | RESOLVED, five verdicts | 3-4 | W3-W31-O1 through O5 |
| T3 (central-charge mismatch deep dive) | Drinfeld + Boundary | TYPE CLASH (Lie cohomology vs Virasoro number) | 4 | W3-W31-T1 |
| T4 (topological vs conformal) | Drinfeld + Boundary | CONDITIONAL: T2 (topological-twist) needed | 3 | W3-W31-T2 |
| T5 (conjecture / no-go conversion) | Drinfeld + Boundary | conditional conjecture C1 (chosen); no-go N1 if T2 fails | 4 | W3-W31-C1 / N1 |
| T6 (cross-walk M-29, W12, W21, W22-T1) | Drinfeld + Boundary | COHERENT with all four | 3 | W3-W31-X1 through X4 |
| T7 (Phase-4 residual entry) | summarise | DRAFTED (R-W3-W31-A) | 4 | §7.1 |
| T8 (cross-volume implications) | Functoriality | one new drift (D-W31-DR1) | 2 | W3-W31-X5 |

---

## §10. Heal proposals

**Heal H-W3-W31-A (Replace W23-C1 with W31-C1 in master ledger).**
The W3-W23-C1 conjecture is replaced by the precise conditional
conjecture W3-W31-C1 (§5.3) plus the alternative no-go W3-W31-N1
(§5.4). The deciding evidence is the topological-twist conjecture
W3-W31-T2 (§4.4).

**Heal H-W3-W31-B (Inscribe R-W3-W31-A into master ledger).** Add
the Phase-4 residual entry §7.1 to the master ledger. Cross-walk
to existing W23 / W14 residuals (§7.2).

**Heal H-W3-W31-C (Cross-volume firewall sharpening).** Add the
W3-W31-X5 / D-W31-DR1 note to `tate-P5-cross-volume.tex` (§8.3)
clarifying that the 5d M-theory bridge is internal (intra-volume)
and does not interact with the Vol III / Igusa cross-volume
firewall.

**Heal H-W3-W31-D (Distinguish topological vs conformal in BD
remark).** The W3-W23-D heal (BD chiral / 5d VOA distinction) is
sharpened: the manuscript's BD chiral algebra is *topological*
(no Virasoro on $\R$); the CGW 5d boundary VOA is *conformal*
(with $T(z)$); the bridge requires either a topological-twist on
CGW (W3-W31-T2, conjectural) or no bridge (W3-W31-N1).

---

## §11. New residuals

**R-W3-W31-A.** Phase-4 frontier residual: 5d twisted M-theory
bridge with five-obstruction conditional conjecture (§7.1). Severity
4 (load-bearing).

**R-W3-W31-B.** Phase-4 frontier residual: topological-twist
conjecture W3-W31-T2 — does the regularised double holomorphic-twist
limit $\epsilon_1, \epsilon_2 \to 0$ on the CGW 5d boundary VOA
produce a Lie 2-cocycle class on a Hamiltonian Lie algebra, or
not? The deciding evidence is either an explicit construction (C1
path) or an explicit non-existence proof (N1 path). **Severity 3
(conditional). Status open.**

**R-W3-W31-C.** Phase-4 frontier residual: $\hbar \leftrightarrow
(\epsilon_1, \epsilon_2)$ rebasing morphism (D-W31-2). Multiple
candidates exist ($\hbar = \epsilon_1$, $\hbar = \epsilon_1 + \epsilon_2$,
$\hbar = \epsilon_1 \epsilon_2$, etc.). The discharge path requires
selecting one canonically; this is an open functorial question.
**Severity 2. Status open.**

---

## §12. Stable core verdict

W3-W31 does not invalidate any wave-2 or wave-3 stable-core finding.
The W14 / W23 5d twisted M-theory bridge is **further refined**:
W23 demoted W14 from "connection" to "conjectural with five
obstructions" (W3-W23-C1, W3-W23-05); W31 sharpens W3-W23-C1 into
a *precise conditional conjecture* W3-W31-C1 (with explicit named
discharge paths D-W31-1 through D-W31-5) plus a *precise
alternative no-go* W3-W31-N1 (firing if the topological-twist
conjecture T2 fails). The deciding evidence between C1 and N1 is
T2 (R-W3-W31-B).

**M-29 (universal categorical no-go) is unchanged.** The
directional sharpening of M-29 (W3-W14-04) is *coherent* with the
5d M-theory picture: CGW central-charge poles at divisor boundaries
correspond exactly to the directional rising-factorial obstruction
on the mixed cones (W3-W31-X1).

**M-31 ([Tr ψ]_BV ↔ [c̄]_CE)** is σ_swap-equivariant (W3-W23-04)
and — under the conditional discharge-path D-W31-5 / T2 — would
become the *manuscript-side* avatar of the CGW topologically-twisted
central charge at $\epsilon_1, \epsilon_2 \to 0$. **No new
identification is forced** at the manuscript level; the 5d M-theory
bridge is a Phase-4 program that lives *outside* the manuscript's
strict scope.

**No new residuals affect the inscribed manuscript content.** The
W31 heals are entirely at the reconstitution-ledger / master-
ledger level (replace W3-W23-C1 with W3-W31-C1; inscribe R-W3-W31-A;
cross-volume firewall note; topological-vs-conformal sharpening).

**W16 cross-volume firewall is unchanged.** The 5d M-theory bridge
is intra-volume (manuscript ↔ CGW physics framework), not cross-
volume (manuscript ↔ Vol III ↔ Igusa). One new convention drift
(D-W31-DR1) deepens the W3-W16-D2 free-vs-fixed-$\hbar$ divergence;
no other cross-volume drift detected.

---

## §13. Provenance

W31 (Wave 3) read:
- `/Users/raeez/topological-strings/CLAUDE.md`.
- `/Users/raeez/topological-strings/reconstitution/wave3-W23-5dM-sigma-2026-04-28.md` (full).
- `/Users/raeez/topological-strings/reconstitution/wave3-W14-mixed-cones-2026-04-28.md` (full).
- `/Users/raeez/topological-strings/reconstitution/wave3-W11-beilinson-hypotheses-2026-04-28.md` §W3-W11-05 region (lines 380–828).
- `/Users/raeez/topological-strings/reconstitution/wave3-W16-crossvolume-2026-04-28.md` (full).
- `/Users/raeez/topological-strings/reconstitution/wave3-W12-blast-radius-2026-04-28.md` §5–6 (lines 340–460).
- `/Users/raeez/topological-strings/reconstitution/wave3-W21-wakimoto-2026-04-28.md` §8 (column-Verma identification, lines 264–712).
- `/Users/raeez/topological-strings/reconstitution/wave3-W22-supertrace-rigorous-2026-04-28.md` §W3-W22-05 (W22-T1, W22-T2 theorem statements, lines 537–612).
- `/Users/raeez/topological-strings/reconstitution/wave3-W8-polyakov-composition-2026-04-28.md` (regulator-class canonicity, lines 77, 778, 925).

External references invoked (not inscribed; cited as motivation):
- Costello, "M-theory in the Omega-background and 5-dimensional
  non-commutative gauge theory", arXiv:1610.04144 (cited in
  `main.tex`:6215; foundational paper on Omega-deformed twisted
  M-theory).
- Costello-Gaiotto-Williams, "Higgs and Coulomb Branches from Vertex
  Operator Algebras", arXiv:2007.09497 (W14 cited; PDF not inscribed;
  W23 / W31 flag as needing inscribe-and-verify).
- Costello-Gaiotto, "Twisted Supergravity and Koszul Duality:
  A Case Study in AdS3", arXiv:2001.02177 (cited as motivation).
- Schiffmann–Vasserot / Maulik–Okounkov $W_{1+\infty}$ central
  charge formulas (cited as representative form for
  $c(\epsilon_1, \epsilon_2)$).
- Beilinson–Drinfeld, *Chiral Algebras*, AMS 2004, §3.3–3.4.
- Hartshorne, *Residues and Duality* III.2.

W31 confidence:
- T1 / T2 (obstruction enumeration + per-obstruction audit): **high**
  (each obstruction has a precise discharge path or strengthened
  no-go).
- T3 (central-charge type clash): **very high** (the Lie cohomology
  vs Virasoro number clash is structural, not parameter-dependent).
- T4 (topological-twist conjecture T2): **medium** (plausible but
  not in inscribed sources).
- T5 (C1 / N1 conversion): **high** for the binary structure;
  **medium** for which branch holds.
- T6 (cross-walk): **high** (no contradictions detected; coherent
  with M-29, W12, W21, W22-T1).
- T7 (residual entry): **high** (precise five-ingredient ledger
  draft).
- T8 (cross-volume drift D-W31-DR1): **medium-high** (deepens
  W3-W16-D2; no Igusa interaction).

No web search invoked. No new computational scratch files (the
audit is structural; W23's 2,576 commutator instances are inherited).

---

## §14. 200-word summary

W31 audits W23's five precise obstructions to the W14 5d twisted
M-theory bridge through Drinfeld + Boundary lenses. Severity
ordering: (I-5) central-charge mismatch is **load-bearing**
(severity 4); (I-1)–(I-4) are contingent (severity 3 each).
Per-obstruction verdicts (W3-W31-O1 through O5): all five admit
discharge paths in principle; (I-5) requires the topological-twist
conjecture W3-W31-T2 (regularised double holomorphic-twist limit
$\epsilon_1, \epsilon_2 \to 0$ on CGW boundary VOA producing a
Lie 2-cocycle class). The central-charge mismatch is a **type
clash** (W3-W31-T1): manuscript's $[\bar c]$ is a Lie cohomology
class; CGW's $c(\epsilon_1, \epsilon_2)$ is a Virasoro number. No
specialisation $\epsilon \to 0$ converts a number into a cohomology
class without a category-changing topological twist. W23-C1 is
replaced by precise **conditional conjecture W3-W31-C1**
(discharge path with five named conditions) plus alternative
**no-go W3-W31-N1** (T2-failure path). Cross-walk verifies coherence
with M-29 directional sharpening, W12 four-cone Čech SES, W21
column-Verma identification, W22-T1 supertrace cocycle vanishing
(W3-W31-X1 through X4). Cross-volume: discharging 5d M-theory
deepens W3-W16-D2 manuscript/Vol III $\hbar$ divergence (drift
D-W31-DR1); does not interact with BKM/Igusa firewall. Phase-4
residual R-W3-W31-A inscribes the five-obstruction structure with
explicit deciding evidence per obstruction. No manuscript content
modified; all heals at master-ledger / reconstitution level.

End of W31 Wave-3 ledger.
