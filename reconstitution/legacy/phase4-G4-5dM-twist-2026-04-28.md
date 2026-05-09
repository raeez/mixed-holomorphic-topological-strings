# Phase 4 / G4 — 5d M-Theory Twist Program (W3-W31-T2 Research Outline)

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Group.** G4 — Cross-volume / 5d M-theory.
**Wave.** Phase 4 (Wave 3 CERTIFIED CONVERGED).
**Lens (inherited).** Drinfeld (canonical-construction discipline) +
Boundary (specialisation strata) — from W31. Witten (physical
consistency) + Hypotheses (which hypotheses are missing) — from W23.
The Phase-4 G4 program inherits W23/W31's lens hierarchy and proposes
research milestones, not new theorems.
**Mandate.** Frame the W3-W31-T2 conjecture (regularised double
holomorphic-twist limit $\epsilon_1, \epsilon_2 \to 0$ of the CGW
boundary VOA produces a Lie 2-cocycle class matching manuscript
$[\bar c]$) as a Phase-4 research program. Identify CGW theorem
statements to twist; address the type clash; map the five W23/W31
obstructions onto a milestone schedule; audit cross-volume risk;
test interaction with G2 Symp_form-equivariance.
**Mode.** Proposal-only. Master ledger schema; IDs prefix `P4-G4-`.
No commits. No new theorems. No web search.
**Inputs read in full.**
- `/Users/raeez/topological-strings/CLAUDE.md`.
- `/Users/raeez/topological-strings/reconstitution/wave3-W31-5dM-obstructions-2026-04-28.md` (T2 conjecture origin, §4.1–4.4).
- `/Users/raeez/topological-strings/reconstitution/wave3-W23-5dM-sigma-2026-04-28.md` (5 obstructions enumerated, §5.1).
- `/Users/raeez/topological-strings/reconstitution/wave3-W14-mixed-cones-2026-04-28.md` (5d M-theory remark origin, §4.2 brane-configuration).
- `/Users/raeez/topological-strings/reconstitution/wave3-W16-crossvolume-2026-04-28.md` (cross-volume firewall, F1–F6).
- `/Users/raeez/topological-strings/reconstitution/wave3-W35-R26A-symp-2026-04-28.md` §5 (T2 ↔ Symp_form interaction).

---

## §0. Method

The Drinfeld lens demands the program identifies a **canonical**
twist functor $\tau: \mathrm{VOA}_{\mathrm{conformal}} \to
\mathrm{ChirAlg}_{\mathrm{topological}}$ that respects the obvious
symmetry groupoids on each side. The Boundary lens demands the
specialisation $\epsilon_1, \epsilon_2 \to 0$ be along a specified
scaling direction in the equivariant moduli, with each stratum's
content named.

The Witten lens (inherited from W23) demands physical consistency:
field content, defect spectrum, anomaly structure, duality
crosscheck. The Hypotheses lens demands explicit hypothesis
tracking on both sides.

The G4 program is **structural reconnaissance**, not theorem
production. Each milestone produces an artifact (citation, toy
model, computation, audit) on which the next milestone depends.
Failure at any milestone bifurcates the program into either
(i) a refined reach (with the failure mode named as a residual)
or (ii) a precise no-go (W3-W31-N1 fires).

---

## §1. T1 — CGW Program Review (P4-G4-T1)

### §1.1 What CGW arXiv:2007.09497 actually is

**arXiv:2007.09497.** Costello-Gaiotto-Williams, "Higgs and Coulomb
Branches from Vertex Operator Algebras", JHEP 03 (2021) 217. The
W23 §1.1 verification (provenance flag W3-W23-01) found the W14
attribution names this paper and its title is correct. The PDF is
**not inscribed** in `references/primary-sources/`; the manuscript
bibliography (`main.tex`:6215) cites only Costello arXiv:1610.04144.

**Paper content per W23 §1.2.** Three closely related papers
operate together:
- **Costello arXiv:1610.04144** ("M-theory in the Omega-background
  and 5-dimensional non-commutative gauge theory"). Establishes 5d
  Omega-deformed twisted M-theory on $\R \times \C^2$ as a 5d
  non-commutative Chern-Simons theory in background $\Omega$-deformation.
  Foundational; **inscribed via citation only**, not as PDF.
- **Costello-Gaiotto arXiv:2001.02177** ("Twisted Supergravity and
  Koszul Duality: A Case Study in AdS3"). Develops the
  Koszul-duality dictionary between gauge sector and gravity sector
  via twisted supergravity. Cited as motivation; not PDF-inscribed.
- **CGW arXiv:2007.09497** ("Higgs and Coulomb Branches from VOAs"
  / "Holography for $\mathcal N=4$ SYM via Twisted Supergravity").
  Builds the boundary VOA dictionary at the level of holography.
  PDF NOT inscribed. **W23 §1.1 source-precision flag still open.**

### §1.2 Key theorems / propositions to twist

**Per W23 §1.2 (best-available structural reconstruction):**

(1) **5d HT-CS bulk on $\R \times \C^2$** is identified as the
$\Omega$-deformed twisted M-theory of Costello 1610.04144. Bulk
fields are 5d non-commutative Chern-Simons gauge fields with
$\Omega$-background $\epsilon_1, \epsilon_2$ on $\C^2$.

(2) **Boundary VOA on $\R \times \{0\}$** is the **Heisenberg /
$W_{1+\infty}(\epsilon_1, \epsilon_2)$ at level 1**, with central
charge a function of $\epsilon_i$. (Schiffmann–Vasserot,
Maulik–Okounkov representative form per W31 §3.1:
$c(\epsilon_1, \epsilon_2) = -(\epsilon_1+\epsilon_2)^3 / (\epsilon_1
\epsilon_2 \epsilon_3)$ with $\epsilon_3 = -\epsilon_1 - \epsilon_2$
in CY3 normalisation.)

(3) **Wilson-line defects along $\R \times \{p\}$** correspond to
modules of the boundary VOA. The Wilson-line ↔ VOA-module
dictionary is canonical.

(4) **Holomorphic surface defects along $\R \times \{z_i = 0\}$**
correspond to **partial-trace / pull-back of the bulk algebra to
the surface defect**, producing Heisenberg-like factorization
centers along the surface. This is the key piece for the
manuscript's mixed cones.

### §1.3 Specific theorems to be twisted

**P4-G4-T1.1 (anchoring theorem).** The G4 program will identify
the **single** CGW theorem (or proposition, or section) whose
output is the boundary VOA $W_{1+\infty}$ central charge as a
function of $(\epsilon_1, \epsilon_2)$. This is the load-bearing
output (per W31 §3, type-clash analysis).

**Candidates per W31 §3 / W23 §1.2:** CGW 2007.09497 §3 (W14
attribution, unverified, PDF pending); Costello 1610.04144 §6
(Omega-background central-charge formula); Schiffmann–Vasserot /
Maulik–Okounkov representative formulas.

**Discharge action.** Read Costello 1610.04144 §6 and CGW
2007.09497 §3 (after inscription); identify the precise proposition
defining $c(\epsilon_1, \epsilon_2)$ for the boundary VOA. This is
the input to the twist functor. P4-G4-T1.1 is the **first**
Phase-4 milestone (M1, 3-month horizon).

### §1.4 What ε_1, ε_2 are

**Per Costello 1610.04144 / W31:** $(\epsilon_1, \epsilon_2)$ are
the Omega-background parameters on $\C^2$: $\epsilon_i$ is the
rotation parameter on the $i$-th holomorphic axis (equivariant
parameter for $T^2 = (\C^*)^2$ acting on $\C^2$). CY3 condition
imposes $\epsilon_3 = -\epsilon_1 - \epsilon_2$. The classical
limit $\epsilon_1, \epsilon_2 \to 0$ is CY-and-commutative; the
central charge has poles at $\{\epsilon_1 = 0\}$,
$\{\epsilon_2 = 0\}$, $\{\epsilon_1 + \epsilon_2 = 0\}$ in the
Schiffmann-Vasserot normalisation.

**Cross-walk to manuscript $\hbar$ (W3-W16-D2).** Manuscript $\hbar$
is the formal Rees deformation parameter (adimensional, free); CGW
$(\epsilon_1, \epsilon_2)$ is two-dimensional equivariant data. The
canonical $\hbar \leftrightarrow (\epsilon_1, \epsilon_2)$ rebasing
is not in any inscribed source. Candidates: $\hbar = \epsilon_1$,
$\hbar = \epsilon_1 + \epsilon_2$, $\hbar = \epsilon_1 \epsilon_2$
(R-W3-W31-C).

---

## §2. T2 — Type-Clash Problem (P4-G4-T2)

### §2.1 The type clash, restated

Per W3-W31-T1 (W31 §3.4, severity 4):
| Object | Type | Target |
|--------|------|--------|
| $[\bar c]$ | Lie 2-cocycle class on $\bar A$ | $H^2_{\mathrm{Lie}}(\bar A; \C)_{(0,0)}$ |
| $c(\epsilon_1, \epsilon_2)$ | Virasoro central charge of $W_{1+\infty}$ | $\C(\epsilon_1, \epsilon_2)$ |

These live in different categories: a class in Lie cohomology is
not the same kind of thing as a number / formal series (or an
element of a rational function field). **No specialisation morphism
on a parameter space converts a number into a cohomology class.**

### §2.2 The category-changing structure: topological twist

Per W31 §4.4: the only morphism known to convert a conformal VOA
into a topological chiral algebra is a **topological twist**.

**P4-G4-T2.1 (categorical structure question).** Candidates for
the CGW boundary VOA → twist-image map:

(a) **Lurie HA §5.5.4 ($\infty$-categorical localisation).** A
localising functor between presentable $\infty$-categories that
inverts the Virasoro structure and produces a topologically
locally constant factorization algebra. **Default candidate** in
the Costello-Gwilliam framework.

(b) **Alternatives.** Lurie HA §5.5.2 $\hbar$-deformation; Lurie
§5.2/§5.4 Koszul-dual functor with degree shift; Beilinson-Drinfeld
§3.4 chiral product specialisation.

**P4-G4-T2.2 (working hypothesis).** The CGW topological twist is
a Lurie HA §5.5.4 *Bousfield localisation* killing the Virasoro
mode while preserving the $\hbar$-deformed Poisson structure on
the formal disk. **Justification.** Only option (a) preserves the
Lie-algebra structure that specialises to $\bar A$ at $\epsilon \to 0$.
Options (b) introduce additional structural data not named in W31/W23.

**Status.** P4-G4-T2.2 is a structural meta-conjecture (in which
categorical framework should the limit be constructed?), distinct
from W3-W31-T2 itself (existence of limit producing $[\bar c]$).

### §2.3 The object types in the limit

**Source (CGW).** $W_{1+\infty}(\epsilon_1, \epsilon_2)$ at level
1, conformal VOA with $T(z)$ generating Virasoro of central charge
$c(\epsilon_1, \epsilon_2)$. Category: $(\infty,1)$-category of
$\hbar$-deformed factorization algebras on $\R \times \C^2$
(Costello-Gwilliam framework).

**Target (manuscript).** BD topological chiral algebra (W3-W11-05)
on $\R$, locally constant on $\R$, no Virasoro, with central charge
$[\bar c] \in H^2_{\mathrm{Lie}}(\bar A; \C)_{(0,0)}$.

**The functor.** $\tau: W_{1+\infty}(\epsilon_1, \epsilon_2)
\mapsto \mathrm{ChirAlg}_{\mathrm{top}}(\R, \bar A, [\bar c])$.

**Open question P4-G4-T2.3.** Does $\tau$ exist as a Lurie HA
§5.5.4 localisation? **This is the load-bearing categorical
question.**

---

## §3. T3 — The Five Obstructions (P4-G4-T3)

The W23/W31 obstruction list, with G4-specific commentary on what
the twist program would need to address per obstruction.

### §3.1 (I-1) Primary-source dictionary [severity 3]

**G4 action P4-G4-T3.I1.** Inscribe four PDFs into
`references/primary-sources/`:
- `costello-omega-twisted-M-1610.04144.pdf` (foundation).
- `costello-gaiotto-koszul-duality-2001.02177.pdf` (motivation).
- `cgw-higgs-coulomb-2007.09497.pdf` (boundary VOA dictionary;
  PRIMARY for the twist program).
- `cgw-cohomological-hall-2103.11647.pdf` (cohomological Hall
  algebra structure on the surface defect).

Verify §3 of CGW 2007.09497 establishes the surface-defect
spectrum needed for (I-3) and the boundary VOA central charge
needed for (I-5).

**Without P4-G4-T3.I1 closure, the twist program has no anchoring
text.** The 3-month milestone (T6 below) is precisely this.

### §3.2 (I-2) Partition-function match [severity 3]

**G4 action P4-G4-T3.I2.** The twist program subsumes (I-2) at the
*regularised* limit: the partition function in the limit
$\epsilon_1, \epsilon_2 \to 0$ should match the manuscript's
$\hbar$-formal Rees deformation. The matching is at the level of
**the regularised twist limit**, not the bare limit (which is
divergent per W31 §3.2).

**Twist-program-specific obligation.** Compute the regularised
$\epsilon_1, \epsilon_2 \to 0$ limit of the CGW partition function
in the presence of a holomorphic surface defect along
$\{z_2 = 0\}$, modulo the canonical $\hbar \leftrightarrow
(\epsilon_1, \epsilon_2)$ rebasing morphism. The manuscript-side
partition function (with $C^{+-}$ inserted as cotangent module)
must match this regularised limit.

**Phase-4 milestone.** 12-month horizon (see T6 below).
Prerequisite: P4-G4-T3.I1 closure (CGW PDF + §3 verification).

### §3.3 (I-3) Defect-spectrum match [severity 3]

**G4 action P4-G4-T3.I3.** The twist program inherits the W23 §5.1
(I-3) requirement: verify the W14 §2.2 tensor factorization
$C^{+-} \cong \C[z_1] \otimes \mathcal{P}_{z_2}^{(\mathrm{Matlis})}$
matches CGW 2007.09497 §3's surface-defect catalog. The
twist-program addition: the matching must hold at the
*regularised twist limit*, not at finite $(\epsilon_1, \epsilon_2)$.

**Conditional on W3-W14-C1.** The Wakimoto / parabolic-Verma
realization of the mixed cones (W14 §5.2, conjecture, severity 2)
is the clearest path to identify $C^{+-}$ with a specific CGW
boundary condition. **The twist program needs both W3-W14-C1 and
P4-G4-T3.I1 closure.**

### §3.4 (I-4) σ-mirror match [severity 3]

**G4 action P4-G4-T3.I4.** Construct a 2-categorical equivalence
between σ_swap (manuscript, W3-W23-T1, sign $-1$, internal
anti-involution) and ε-mirror (CGW, Higgs/Coulomb mirror,
$\epsilon_1 \leftrightarrow \epsilon_2$, external functor between
two ε-deformed VOAs).

**Twist-program-specific obligation.** At the regularised
$\epsilon_1, \epsilon_2 \to 0$ limit, the ε-mirror (which acts on
the equivariant base) collapses to a sign flip
$\epsilon_1 \mapsto -\epsilon_1$, $\epsilon_2 \mapsto -\epsilon_2$
(per W31 §2.4 boundary analysis). This is *not* σ_swap on the
manuscript's mixed cones (which exchanges divisor cones, not signs).
**The twist program must verify the σ-mirror match survives the
$\epsilon \to 0$ limit, where the naive boundary correspondence
fails.**

The 2-categorical equivalence is genuinely non-trivial.

### §3.5 (I-5) Central-charge mismatch [severity 4, load-bearing]

**G4 action P4-G4-T3.I5.** This is the W3-W31-T2 conjecture itself:
construct (or prove non-existence of) the regularised double
holomorphic-twist limit $\epsilon_1, \epsilon_2 \to 0$ producing a
Lie 2-cocycle class. Per W31 §4.3, the manuscript needs *both*
holomorphic directions; the natural single-direction twist
($\epsilon_2 \to 0$ at fixed $\epsilon_1$) produces only a
single-direction VOA, too small to recover $\bar A$.

**The double-twist-with-regularisation is the central technical
obstacle** of the entire P4-G4 program. Without it, the type clash
P4-G4-T2 is fatal.

**Phase-4 milestone.** 12–18 month horizon (see T6).

### §3.6 Summary table of obstructions

| ID | Obstruction | Severity | G4 action | Milestone |
|----|-------------|----------|-----------|-----------|
| (I-1) | Primary-source dictionary | 3 | Inscribe four PDFs; verify CGW §3 | 3 mo |
| (I-2) | Partition-function match | 3 | Compute regularised twist limit; rebasing morphism | 12 mo |
| (I-3) | Defect-spectrum match | 3 | Match W14 tensor factorization to CGW catalog at twist limit; needs W14-C1 | 12 mo |
| (I-4) | σ-mirror match | 3 | Construct 2-categorical equivalence at twist limit | 12 mo |
| (I-5) | Central-charge mismatch | **4** | Construct double-twist regularisation producing Lie 2-cocycle | 12–18 mo |

---

## §4. T4 — Connection to Costello 2110.10257 (P4-G4-T4)

### §4.1 Costello 2110.10257 (cited reference)

**arXiv:2110.10257.** Likely Costello's "Holomorphic factorization
algebras" or "Quantum field theory and factorization algebras"
work-in-progress (paper to be inscribed and verified per
P4-G4-T3.I1). The hypothesis from the user's task is that this
paper provides a parallel thread on **holomorphic field theory +
factorization algebras** that bridges manuscript's BV-FA framework
and CGW's boundary VOA.

### §4.2 Why this might be the bridge

The manuscript's framework (per W3-W11-05 / W3-W23-06) is:
- **BV / factorization algebra** on the brane line $\R$, with the
  formal-disk transverse $\C^2$ providing the Hamiltonian Lie
  algebra coefficient.
- **Topological** chiral algebra (locally constant on $\R$, no
  Virasoro).

The CGW framework is:
- **Conformal VOA** on the brane line $\R \times \{0\} \subset
  \R \times \C^2$.
- $W_{1+\infty}$ at level 1 with $T(z)$ generating Virasoro.

The Costello 2110.10257 framework (hypothesis) operates at the
intersection: **holomorphic** factorization algebras that are
*conformal* in the holomorphic direction and *topological* in the
real direction. This intermediate object would naturally be the
bridge:
- Specialise from holomorphic-conformal in $z_1, z_2$ to
  topological in $\R$: gives the manuscript's BV-FA framework.
- Specialise from topological in $\R$ to conformal in $\R$ (e.g.,
  by adding a Virasoro mode along the brane line): gives CGW's
  boundary VOA.

### §4.3 The candidate factorisation

**P4-G4-T4.1 (working hypothesis).** Costello 2110.10257 may
establish a holomorphic factorization algebra $\mathcal F$ on
$\R \times \C^2$ such that:
- The boundary $\R \times \{0\}$ restriction of $\mathcal F$ is
  the CGW boundary VOA.
- The topological-twist limit $\epsilon_1, \epsilon_2 \to 0$ of
  $\mathcal F$ on $\R \times \C^2$ is the manuscript's BV-FA
  framework (with $\bar A$ as Hamiltonian Lie algebra coefficient).
- The transition functor between these two specialisations is the
  topological-twist functor of W3-W31-T2 (P4-G4-T2.3 above).

**Status of P4-G4-T4.1.** This is structurally the cleanest
candidate bridge, but is **conjectural and unverified.** The
G4 program 6-month milestone (T6) includes inscribing
2110.10257 and verifying whether such a factorization algebra is
constructed there.

### §4.4 Connection to Costello-Gwilliam Vols I–II

The Costello-Gwilliam *Factorization Algebras in QFT* Vols I–II
(inscribed at `references/primary-sources/costello-gwilliam-vol1-cambridge.html`
and `vol2-cambridge.html`) establish the foundational framework
for factorization algebras on Lorentzian manifolds and Euclidean
manifolds. The 2110.10257 paper (if the hypothesis holds) would
extend this to holomorphic factorization algebras on
$\C^d$-factor manifolds, which is exactly the setting needed for
the CGW ↔ manuscript bridge.

**P4-G4-T4.2 (cross-walk).** If the 2110.10257 holomorphic
factorization framework is consistent with Costello-Gwilliam Vols
I–II, then the twist functor of P4-G4-T2.3 is a Lurie HA §5.5.4
localisation in the holomorphic-factorization category. This
would *directly* close the categorical-structure question
(P4-G4-T2.3) modulo the regularisation obstacle (P4-G4-T3.I5).

### §4.5 Verdict

**P4-G4-O4 (Costello holomorphic factorization bridge,
conjectural).** **Severity 3 (Phase-4 milestone). Status:
inscribe-and-verify pending. Confidence medium.**

The bridge between manuscript BV-FA and CGW boundary VOA is
plausibly via Costello 2110.10257's holomorphic factorization
framework. The G4 6-month milestone is to inscribe 2110.10257 and
verify whether (i) the holomorphic factorization framework is
constructed therein; (ii) the boundary specialisation matches the
CGW boundary VOA; (iii) the topological twist limit matches the
manuscript's BV-FA. **All three subparts are conjectural until
PDF inscription.**

---

## §5. T5 — Scope Statement (P4-G4-T5)

### §5.1 IN scope

The P4-G4 program addresses:

(S1) **Construction of the twist functor P4-G4-T2.3** at the
categorical level (Lurie HA §5.5.4 or alternative).

(S2) **Verification of the regularised double holomorphic-twist
limit P4-G4-T3.I5** producing a Lie 2-cocycle class on a
Hamiltonian Lie algebra (W3-W31-T2).

(S3) **Discharge of the five W23/W31 obstructions** at the
regularised twist limit (P4-G4-T3.I1 through P4-G4-T3.I5),
modulo the canonical $\hbar \leftrightarrow (\epsilon_1,
\epsilon_2)$ rebasing.

(S4) **Identification of the manuscript's mixed cones $C^{+-},
C^{-+}$** with CGW holomorphic surface defects at the
regularised twist limit, conditional on W3-W14-C1
(Wakimoto-Verma realization).

(S5) **Symp_form-equivariance inheritance** for the column-Verma
identification of $C^{+-}$ via the twist limit (per W3-W35-05,
conditional on T2 and T2's preservation of Symp_form-action).

### §5.2 OUT of scope (forced by structural firewalls)

The following are STRUCTURALLY incompatible with the P4-G4 program
(per W3-W16 cross-volume firewall, W23 / W31 obstructions):

(O1) **BKM / Igusa $\Delta_5$ bridge** is structurally
incompatible (W3-W16-C, three independent compatibility failures:
wrong-direction lattice signature, Rees grading not modular weight,
Moyal rationals not Jacobi integers). The P4-G4 program does NOT
attempt this bridge. The CLAUDE.md "convention-checking bridge"
phrasing is correctly conservative.

(O2) **Vol III BFN central scalar identification (F1 in W16)**
fails functoriality on automorphism groups (formal-Symp on
manuscript side; finite Weyl group on Vol III side). Even at the
discharged twist limit, the manuscript's $[\bar c]$ would be
identified with the CGW topologically-twisted central charge
(if T2 holds), NOT with Vol III's BFN central scalar. The cross-
volume firewall stays intact.

(O3) **Vol III Heisenberg level $k$ identification (F2 in W16)**
fails on scaling axis. Same reason as O2.

(O4) **Worldsheet identifications across volumes (W3-W16-D5)**:
the manuscript has *no* worldsheet $\Sigma_g$; Vol III at $d=2$
has a reference algebraic curve $C \subset K3$; Igusa has Siegel
period $\mathbb H_2$. Three different genus axes; no two-side
identification possible.

(O5) **Cross-volume $\hbar$-rebasing**: the P4-G4 program
introduces a $\hbar \leftrightarrow (\epsilon_1, \epsilon_2)$
rebasing morphism (P4-G4-T3.I2). This is INTERNAL to the
manuscript-CGW bridge and DOES NOT extend to Vol III's
lattice-fixed $\hbar^2 = -1/(2c_+(L))$. Per W31 §8.3 drift
D-W31-DR1, this *deepens* the W3-W16-D2 manuscript/Vol III
$\hbar$ divergence rather than closing it.

### §5.3 Summary scope verdict

**P4-G4-O5 (Scope of the twist program).** The P4-G4 program is
**intra-volume** (manuscript ↔ CGW physics framework), NOT
cross-volume (manuscript ↔ Vol III ↔ Igusa). The cross-volume
firewall (W3-W16) is *unaffected* by the program; the BKM/Igusa
bridge remains structurally incompatible regardless of P4-G4
outcome.

**Severity 3 (Phase-4 framing). Status valid. Confidence high.**

---

## §6. T6 — Milestone Proposals (P4-G4-T6)

### §6.1 3-month milestone: P4-G4-M1 — Anchor the twist target

**Goal.** Identify the exact CGW theorem statement to twist.

**Deliverables.**
1. Inscribe four PDFs in `references/primary-sources/`:
   - `costello-omega-twisted-M-1610.04144.pdf`.
   - `costello-gaiotto-koszul-duality-2001.02177.pdf`.
   - `cgw-higgs-coulomb-2007.09497.pdf`.
   - `cgw-cohomological-hall-2103.11647.pdf`.
2. Read CGW 2007.09497 §3 (or wherever the boundary VOA is defined)
   and identify the proposition stating $c(\epsilon_1, \epsilon_2)$
   for $W_{1+\infty}$ at level 1.
3. Read Costello 1610.04144 §6 and verify whether the boundary VOA
   central charge is computed there or in CGW.
4. Inscribe a 5–10 page **anchoring memo** at
   `reconstitution/phase4-G4-anchor-2026-XX-XX.md` reporting
   the precise theorem statement (proposition + central-charge
   formula + normalization conventions).

**Success criterion.** A specific quoted theorem with arXiv
number, paper section, and central-charge formula. The W31 §3.1
representative form $c(\epsilon_1, \epsilon_2) = -(\epsilon_1+
\epsilon_2)^3/(\epsilon_1\epsilon_2\epsilon_3)$ should be either
confirmed or replaced by the inscribed-source formula.

**Resources.** PDF acquisition (arXiv) + paper interpretation + memo
writing. ~ 30–60 hours of close interpretation.

**Failure mode.** If the CGW PDF reveals the boundary VOA central
charge is computed *only* via lattice / cohomological data not
representable as a formula in $(\epsilon_1, \epsilon_2)$, the
P4-G4-T2 type clash deepens (the target may not be a rational
function but a cohomology class itself). This would partially
discharge T2 but introduce a new obstruction at the
$\hbar \leftrightarrow \epsilon$ rebasing level.

### §6.2 6-month milestone: P4-G4-M2 — Toy example construction

**Goal.** Construct the twist limit on a toy example (Heisenberg
sub-VOA).

**Deliverables.**
1. Identify the **Heisenberg sub-VOA** of $W_{1+\infty}(\epsilon_1,
   \epsilon_2)$ at level 1. The Heisenberg VOA $\mathcal H$ has a
   simpler central charge $c_\mathcal{H}(\epsilon_1, \epsilon_2)$
   (typically a quadratic in the $\epsilon$'s).
2. Construct the **regularised double holomorphic-twist limit**
   $\epsilon_1, \epsilon_2 \to 0$ of $\mathcal H$ along a specific
   scaling path (e.g., $\epsilon_2 = \lambda \epsilon_1$, then
   $\epsilon_1 \to 0$).
3. Verify the regularised limit produces a **finite cohomological
   class** rather than a divergent number. (The limit is divergent
   without regularisation per W31 §3.2.)
4. Verify the limit produces a Lie 2-cocycle class on a 1-dimensional
   Heisenberg algebra (the trivial / classical case where $[\bar c]$
   is the standard Heisenberg cocycle).

**Success criterion.** A finite cohomological class
$[c_{\mathcal H}^{\mathrm{top}}] \in H^2_{\mathrm{Lie}}(\mathfrak{heis};
\C)$ computed as the regularised limit of $c_\mathcal{H}(\epsilon_1,
\epsilon_2)$. This is the **toy proof of concept** for the W3-W31-T2
mechanism.

**Resources.** Symbolic computation + manuscript-style Russian-
school analysis + ~ 60–120 hours.

**Failure mode.** If no scaling path produces a finite limit (all
paths diverge), then T2 is partially refuted on the toy case,
and the W3-W31-N1 no-go fires for the Heisenberg sub-VOA. This
would *strongly* suggest N1 fires for the full $W_{1+\infty}$,
but is not a proof.

### §6.3 12-month milestone: P4-G4-M3 — Compute Lie 2-cocycle in twist limit

**Goal.** Compute the Lie 2-cocycle in the full twist limit and
verify it matches manuscript $[\bar c]$.

**Deliverables.**
1. Inherit the toy success criterion from P4-G4-M2 to the full
   $W_{1+\infty}(\epsilon_1, \epsilon_2)$.
2. Construct the regularised double holomorphic-twist limit of
   the full boundary VOA central charge $c(\epsilon_1, \epsilon_2)$,
   recovering a Lie 2-cocycle class
   $[c^{\mathrm{top}}_{W_{1+\infty}}] \in H^2_{\mathrm{Lie}}(\bar A; \C)$.
3. **Compute** $[c^{\mathrm{top}}_{W_{1+\infty}}]$ explicitly as a
   cohomology class.
4. Verify equality $[c^{\mathrm{top}}_{W_{1+\infty}}] = [\bar c]$
   modulo the canonical $\hbar \leftrightarrow (\epsilon_1, \epsilon_2)$
   rebasing.

**Success criterion.** Explicit cohomology-class equality, modulo
rebasing. The rebasing must be specified as a specific morphism
(canonical or defensibly natural).

**Failure mode.**
- If the twist limit produces a cohomology class but it differs
  from $[\bar c]$, the W3-W14-C1 Wakimoto identification is
  wrong; the CGW surface defect does not correspond to $C^{+-}$.
  The bridge to mixed cones fails; the program partially
  discharges (I-5) but fails at (I-3).
- If no rebasing makes the equality hold, the P4-G4-T3.I2
  obstruction is structurally fatal.

### §6.4 18-month+ milestone: P4-G4-M4 — Full W3-W31-T2 verification

**Goal.** Full verification of W3-W31-T2 with all five obstructions
discharged.

**Deliverables.**
1. P4-G4-M1 / M2 / M3 closed.
2. (I-3) defect-spectrum match: verify the W14 tensor factorization
   $C^{+-} \cong \C[z_1] \otimes \mathcal{P}_{z_2}^{(\mathrm{Matlis})}$
   matches the CGW surface-defect catalog at the twist limit
   (assuming W3-W14-C1).
3. (I-4) σ-mirror match: construct 2-categorical equivalence
   between σ_swap and ε-mirror at the twist limit.
4. (I-2) partition-function match: compute the regularised twist
   limit of the CGW partition function (with surface defect) and
   verify equality with the manuscript's partition function (with
   $C^{+-}$ inserted).
5. (I-1) primary-source dictionary: closed by P4-G4-M1.
6. **Final verdict on W3-W31-C1 / W3-W31-N1.** Either the
   conditional conjecture holds (all five discharges succeed), or
   the alternative no-go fires (at least one discharge fails
   structurally).

**Success criterion.** Complete twist-limit construction, with
all five obstructions discharged at the regularised level. The
P4-G4 verdict is then *either* W3-W31-C1 holds (full bridge), or
the precise failure mode is named (one of the five obstructions
is structurally fatal).

**Resources.** This is a **multi-paper research program**, likely
collaborative, with substantial computational + categorical-theoretic
machinery. ~ 6 person-years of effort, possibly more.

**Failure mode.** Even if all four M1–M3 milestones succeed, the
final verification at M4 may fail at (I-3), (I-4), or (I-2). Each
failure produces a refined no-go.

### §6.5 Milestone summary

| Milestone | Horizon | Goal | Success criterion | Dependency |
|-----------|---------|------|-------------------|------------|
| P4-G4-M1 | 3 mo | Anchor twist target | Quote inscribed CGW theorem with central-charge formula | Independent |
| P4-G4-M2 | 6 mo | Toy twist construction | Heisenberg sub-VOA produces finite Lie 2-cocycle class at $\epsilon \to 0$ | M1 |
| P4-G4-M3 | 12 mo | Full twist Lie 2-cocycle | $[c^{\mathrm{top}}_{W_{1+\infty}}] = [\bar c]$ modulo rebasing | M2 |
| P4-G4-M4 | 18+ mo | Full W3-W31-T2 verification | All five obstructions discharged at twist limit | M3, W3-W14-C1 |

---

## §7. T7 — Cross-Volume Risk (P4-G4-T7)

### §7.1 The convention-drift question

The P4-G4 program introduces (per W31 §8.3) a new convention
drift D-W31-DR1: fixing the manuscript's $\hbar$ as a function of
$(\epsilon_1, \epsilon_2)$ via the rebasing morphism (P4-G4-T3.I2).
Vol III's $\hbar$ on the Fake-Monster row is fixed as
$\hbar^2 = -1/(2c_+(L))$ by lattice Casimir (W3-W16-D2). These two
fixings are **distinct and inconsistent**.

### §7.2 ℏ-normalization audit

**P4-G4-T7.1 (audit obligation).** During M3, when the canonical
$\hbar \leftrightarrow (\epsilon_1, \epsilon_2)$ rebasing is fixed,
audit the cross-volume implications:

(A) **Manuscript ↔ CGW.** The rebasing is internal to the P4-G4
program. The manuscript's $\hbar$ becomes a specific function
of $(\epsilon_1, \epsilon_2)$ at the regularised twist limit
(e.g., $\hbar = \epsilon_1 + \epsilon_2$ in some normalisation,
or $\hbar = \sqrt{\epsilon_1 \epsilon_2}$ in another).

(B) **Manuscript ↔ Vol III.** The Vol III lattice-fixed
$\hbar^2 = -1/(2c_+(L))$ on Fake-Monster (where $c_+(L) = 25$ on
$\II_{25,1}$, giving $\hbar^2 = -1/50$). For consistency, would
this be compatible with the P4-G4 rebasing
$\hbar = f(\epsilon_1, \epsilon_2)$ for some $(\epsilon_1, \epsilon_2)$
specialisation? Generically NO: the P4-G4 rebasing produces a
**continuous family** of $\hbar$ values; the Vol III lattice-fixing
selects a **discrete** value.

(C) **CGW ↔ Vol III.** No direct identification; both are physics
frameworks operating on different geometric ground states (CGW on
$\R \times \C^2$, Vol III on K3 / CY3 / Fake-Monster).

### §7.3 The drift verdict

**P4-G4-O7 (Cross-volume risk verdict).** **Severity 2. Status
valid. Confidence medium-high.**

The P4-G4 program **deepens** the W3-W16-D2 free-vs-fixed-$\hbar$
divergence between manuscript and Vol III: under P4-G4, the
manuscript's $\hbar$ becomes *continuously fixed* by the
$(\epsilon_1, \epsilon_2)$ rebasing; Vol III's $\hbar$ remains
*discretely fixed* by lattice Casimir. **Neither bridge implies
the other; the cross-volume firewall remains intact**, but
becomes *internally* more refined (manuscript-CGW bridge fixes
$\hbar$ in one way; manuscript-Vol III bridge would fix $\hbar$
in another way; no single $\hbar$ value satisfies both).

**Recommended action.** During M3, when the P4-G4 rebasing is
chosen, document the choice with a one-paragraph audit of which
Vol III specialisation (if any) it is *consistent* with, and which
it is *inconsistent* with. The output is a refined firewall
sharpening.

### §7.4 BKM / Igusa interaction

Per W31 §8.3 and W3-W16-C, the BKM / Igusa bridge is
**structurally incompatible** with the manuscript regardless of
the P4-G4 outcome (three compatibility failures). The P4-G4
program does NOT interact with the BKM / Igusa axis. The
CLAUDE.md "convention-checking bridge" phrasing is correctly
conservative.

---

## §8. T8 — Interaction with G2 Symp_form Equivariance (P4-G4-T8)

### §8.1 The W35 question

W3-W35-05 (W35 §5.4) asks: if the W3-W31-T2 twist limit holds
and the CGW boundary VOA carries a structural Symp_form-action
that survives the regularised limit, then the column-Verma
identification of $C^{+-}$ inherits Symp_form-equivariance "for
free" via the CGW identification.

### §8.2 Conditional analysis

**P4-G4-T8.1 (conditional inheritance).** Conditional on:
1. **W3-W31-T2 holds** (regularised double-twist limit produces
   $[\bar c]$).
2. **W3-W31-O3 holds** (CGW surface defect at $\{z_2 = 0\}$
   matches column-Verma at the regularised limit).
3. **CGW boundary VOA is Symp_form-equivariant** (asserted by
   structural argument; needs CGW PDF inscription per
   P4-G4-T3.I1).
4. **Symp_form-equivariance survives the regularised twist limit**
   (additional condition; W35 §5.4 boundary subtlety).

THEN: the column-Verma identification of $C^{+-}$ inherits
Symp_form-equivariance via the CGW chain, discharging
R-W3-W26-A.

### §8.3 The boundary subtlety

Per W35 §5.4: the regularised $\epsilon_1, \epsilon_2 \to 0$ limit
is the Calabi-Yau boundary stratum of the equivariant moduli space.
Symp_form-equivariance of the CGW side at this limit is *not*
automatic from generic-$\epsilon$ Symp_form-equivariance. It
requires the *survival* of the action through the regularisation.

**P4-G4-T8.2 (survival check).** The 12-month M3 milestone must
verify, in addition to the cohomology-class equality, that the
Symp_form-action on the CGW boundary VOA descends to a
Symp_form-action on the regularised twist-image such that the
descent is canonical (not a choice).

**Severity 3 (Phase-4 milestone). Confidence medium.** This adds
one more condition to the P4-G4-M3 success criterion.

### §8.4 G2 ↔ G4 interaction summary

If G4 succeeds at M3 with Symp_form-survival verified, then:
- **G4 outcome.** W3-W31-C1 conditional conjecture discharges.
- **G2 outcome.** R-W3-W26-A column-Verma Symp_form-equivariance
  discharges as a *corollary* of the G4 chain (rather than via
  a direct PVA construction per W35 path A or path B).

If G4 fails at M3, the G2 column-Verma program is unaffected
(G2 has independent paths via W35 path A — direct PVA construction
— or path B — inheritance from a different physics framework).

**P4-G4-O8 (G2 / G4 interaction).** **Severity 2. Status valid.
Confidence medium-high.**

The G2 Symp_form-program and G4 5d-M-theory-twist-program are
*independent* but *coupled at success*: a G4 success at M3 with
Symp_form-survival verified produces a G2 corollary
(R-W3-W26-A discharge). Failure at G4 does NOT propagate to G2.
The two programs can be pursued in parallel.

---

## §9. Per-target verdict

| Target | Verdict | Severity | Detail |
|--------|---------|----------|--------|
| T1 (CGW program review) | RESOLVED with anchoring memo plan | 3 | P4-G4-T1.1 (3-mo M1 milestone) |
| T2 (Type-clash problem) | Lurie HA §5.5.4 working hypothesis | 4 | P4-G4-T2.1/T2.2/T2.3 |
| T3 (Five obstructions for twist) | Mapped to milestones M1–M4 | 3-4 | P4-G4-T3.I1 through I5 |
| T4 (Costello 2110.10257) | Conjectural bridge; inscribe-and-verify | 3 | P4-G4-T4.1/T4.2/O4 |
| T5 (Scope statement) | IN: twist + 5 obstructions; OUT: BKM + Vol III bridges | 3 | P4-G4-O5 |
| T6 (Milestones) | M1 (3 mo), M2 (6 mo), M3 (12 mo), M4 (18+ mo) | 3-4 | §6.5 table |
| T7 (Cross-volume risk) | Drift D-W31-DR1 deepens W16-D2; firewall intact | 2 | P4-G4-O7 |
| T8 (G2 Symp_form interaction) | Conditional G4-success → G2 corollary | 2 | P4-G4-O8 |

---

## §10. Phase-4 residual entries

### §10.1 R-P4-G4-A (twist program master residual)

**R-P4-G4-A (5d M-theory twist program).** **Phase-4. Severity 4
(load-bearing aggregate of P4-G4-T2.3 + W3-W31-T2 + four
contingent obstructions).**

> **Statement.** Construct (or prove non-existence of) the
> regularised double holomorphic-twist limit
> $\epsilon_1, \epsilon_2 \to 0$ of the CGW boundary VOA
> $W_{1+\infty}(\epsilon_1, \epsilon_2)$ at level 1 producing a
> Lie 2-cocycle class on the Hamiltonian Lie algebra $\bar A$.
> The categorical structure of the limit is conjectured to be a
> Lurie HA §5.5.4 localisation in the holomorphic-factorization
> category (P4-G4-T2.2). Five specific obstructions
> (P4-G4-T3.I1 through I5) must be discharged at the regularised
> twist limit:
> - (I-1) primary-source dictionary [3 mo, M1].
> - (I-2) partition-function match [12 mo, M3].
> - (I-3) defect-spectrum match (conditional on W3-W14-C1) [12 mo, M3].
> - (I-4) σ-mirror match (2-categorical) [12 mo, M3].
> - (I-5) central-charge mismatch (load-bearing, T2 itself) [12-18 mo, M3 + M4].
>
> **Resolution paths.**
> - W3-W31-C1 path: discharge all five obstructions at twist limit;
>   bridge holds conditionally.
> - W3-W31-N1 path: T2 fails (no regularisation produces Lie
>   2-cocycle class); bridge fails structurally; no equivalence.
> - Frontier-residual path: leave open as Phase-4 frontier into
>   5d twisted M-theory and BD chiral algebra unification.
>
> **Deciding evidence.**
> - For (I-1): inscribed CGW PDF + verified §3 surface-defect spectrum.
> - For (I-2): explicit fibre-wise partition-function computation +
>   $\hbar \leftrightarrow (\epsilon_1, \epsilon_2)$ rebasing morphism.
> - For (I-3): explicit CGW catalog match to W14 tensor factorisation
>   at twist limit + W3-W14-C1 proof.
> - For (I-4): 2-categorical equivalence functor at twist limit.
> - For (I-5) → T2: M2 toy success (Heisenberg sub-VOA) + M3 full
>   verification.
>
> **Severity aggregate 4** (load-bearing dominated by (I-5)).
> **Status.** Phase-4 frontier residual; M1–M4 milestones span
> 3 months to 18+ months.

### §10.2 R-P4-G4-B (anchoring memo)

**R-P4-G4-B (CGW anchoring memo).** **Phase-4. Severity 3
(prerequisite for all P4-G4 milestones).**

> Inscribe `references/primary-sources/cgw-higgs-coulomb-2007.09497.pdf`
> and three companions; produce 5–10 page anchoring memo with
> precise theorem identification for $W_{1+\infty}$ at level 1
> central charge formula. **3-month horizon (P4-G4-M1).**

### §10.3 R-P4-G4-C (Costello holomorphic factorization bridge)

**R-P4-G4-C (Costello 2110.10257 inscribe-and-verify).** **Phase-4.
Severity 3.**

> Inscribe Costello arXiv:2110.10257 (or correct arXiv ID, to be
> verified) and check whether it establishes a holomorphic
> factorization framework bridging manuscript BV-FA and CGW
> boundary VOA. **6-month horizon (P4-G4-M2).**

### §10.4 R-P4-G4-D (Symp_form survival check)

**R-P4-G4-D (Symp_form survival under twist limit).** **Phase-4.
Severity 2 (G2 corollary).**

> If P4-G4-M3 succeeds, additionally verify that the CGW
> boundary VOA's Symp_form-action survives the regularised
> $\epsilon_1, \epsilon_2 \to 0$ limit canonically. This is the
> additional condition for R-W3-W26-A discharge as a corollary of
> P4-G4. **12-month horizon (M3 dependent).**

---

## §11. Stable core verdict

P4-G4 does not invalidate any wave-2 or wave-3 stable-core finding.
The W31 / W23 5d twisted M-theory bridge is **promoted from
"conditional conjecture" to "research program with explicit
milestone structure"**: W3-W31-C1 / W3-W31-N1 are the binary
endpoints; P4-G4-M1 through M4 are the milestone intermediates.

**M-29 (universal categorical no-go) is unchanged.** The
directional sharpening of M-29 (W3-W14-04) is *coherent* with the
P4-G4 picture: CGW central-charge poles at divisor boundaries
correspond exactly to the directional rising-factorial obstruction
on the mixed cones (W3-W31-X1).

**M-31 ([Tr ψ]_BV ↔ [c̄]_CE)** is σ_swap-equivariant
(W3-W23-04). Conditional on P4-G4-M3 success, M-31 becomes the
*manuscript-side* avatar of the CGW topologically-twisted central
charge at the regularised $\epsilon_1, \epsilon_2 \to 0$ limit. **No new
identification is forced** at the manuscript level.

**Cross-volume firewall (W3-W16) is unchanged.** The P4-G4
program is *intra-volume* (manuscript ↔ CGW physics framework),
NOT cross-volume (manuscript ↔ Vol III ↔ Igusa). One new
convention drift (D-W31-DR1) is *deepened* under P4-G4: under
M3 fixing, the manuscript's $\hbar$ becomes a continuous function
of $(\epsilon_1, \epsilon_2)$ rather than free.

**G2 column-Verma program** is independent but coupled at success
(P4-G4-O8). G4 success at M3 with Symp_form-survival verified
produces R-W3-W26-A discharge as a G2 corollary; G4 failure does
NOT propagate to G2.

**No manuscript content modified.** All P4-G4 work is at the
reconstitution-ledger / Phase-4-research-program level.

---

## §12. Provenance

P4-G4 read in full:
- `/Users/raeez/topological-strings/CLAUDE.md`.
- `/Users/raeez/topological-strings/reconstitution/wave3-W31-5dM-obstructions-2026-04-28.md` (full).
- `/Users/raeez/topological-strings/reconstitution/wave3-W23-5dM-sigma-2026-04-28.md` (full).
- `/Users/raeez/topological-strings/reconstitution/wave3-W14-mixed-cones-2026-04-28.md` (full).
- `/Users/raeez/topological-strings/reconstitution/wave3-W16-crossvolume-2026-04-28.md` (full).
- `/Users/raeez/topological-strings/reconstitution/wave3-W35-R26A-symp-2026-04-28.md` §5 (T5 region, lines 648–733).

External references cited (not inscribed; pending P4-G4-M1):
- Costello, "M-theory in the Omega-background and 5-dimensional
  non-commutative gauge theory", arXiv:1610.04144 (foundational;
  cited in `main.tex`:6215).
- Costello-Gaiotto-Williams, "Higgs and Coulomb Branches from VOAs",
  arXiv:2007.09497 (boundary VOA dictionary; PDF inscription pending).
- Costello-Gaiotto, "Twisted Supergravity and Koszul Duality",
  arXiv:2001.02177 (motivation).
- Costello-Gaiotto-Williams, "Cohomological Hall Algebras",
  arXiv:2103.11647 (cohomological structure).
- Costello, holomorphic factorization framework arXiv:2110.10257
  (hypothesis; PDF inscription + verification pending).
- Schiffmann–Vasserot / Maulik–Okounkov $W_{1+\infty}$ central
  charge formulas (representative; cited in W31 §3.1).
- Lurie, *Higher Algebra* §5.5.4 (Bousfield localisation in
  presentable $\infty$-categories; working hypothesis for
  topological-twist functor).
- Beilinson-Drinfeld, *Chiral Algebras* §3.3–3.4 (BD chiral
  algebra framework; W3-W11-05).
- Costello-Gwilliam, *Factorization Algebras in QFT* Vols I–II
  (inscribed).

P4-G4 confidence:
- T1 (CGW review): **high** for the structural reconstruction;
  **medium** for the precise theorem statement (PDF inscription
  pending).
- T2 (type-clash + Lurie HA hypothesis): **medium-high** for the
  type clash itself (W31 §3.4); **medium** for the Lurie HA §5.5.4
  working hypothesis (P4-G4-T2.2).
- T3 (five obstructions mapped to milestones): **high** (each
  obstruction has a milestone target).
- T4 (Costello 2110.10257 bridge): **medium-low** (depends on
  inscribe-and-verify outcome of M2).
- T5 (scope): **high** (W16 cross-volume firewall is rigorously
  out of scope).
- T6 (milestones): **medium-high** (M1 is independent; M2–M4 are
  contingent on prior milestones).
- T7 (cross-volume risk): **medium-high** (drift D-W31-DR1 is
  named; firewall remains intact).
- T8 (G2 / G4 coupling): **medium** (conditional inheritance
  chain; W35 §5.4 boundary subtlety adds an additional condition).

No web search invoked. No new computational scratch files.

---

## §13. 200-word summary

P4-G4 frames the W3-W31-T2 conjecture (regularised double
holomorphic-twist limit $\epsilon_1, \epsilon_2 \to 0$ of the CGW
boundary VOA $W_{1+\infty}$ producing a Lie 2-cocycle class
matching manuscript $[\bar c]$) as a four-milestone Phase-4
research program. The categorical structure is a working hypothesis:
Lurie HA §5.5.4 Bousfield localisation in the holomorphic-
factorization category (P4-G4-T2.2). Five W23/W31 obstructions
map to milestones: M1 (3 mo, anchor CGW theorem in inscribed PDFs),
M2 (6 mo, Heisenberg sub-VOA toy twist limit), M3 (12 mo, full
$W_{1+\infty}$ Lie 2-cocycle equality with $[\bar c]$ modulo
canonical $\hbar \leftrightarrow (\epsilon_1, \epsilon_2)$
rebasing), M4 (18+ mo, full discharge of all five obstructions).
The load-bearing obstruction is (I-5) central-charge type clash,
discharged only via T2's regularised twist limit. Costello
arXiv:2110.10257 (holomorphic factorization framework) is the
candidate bridge between manuscript BV-FA and CGW boundary VOA;
PDF inscription pending (R-P4-G4-C). Cross-volume firewall (W16)
is intra-volume to P4-G4: BKM/Igusa structurally incompatible
remains out of scope; manuscript/Vol III $\hbar$ divergence
(W3-W16-D2) is *deepened* under M3 fixing (drift D-W31-DR1).
G2 Symp_form column-Verma program inherits as a corollary if
M3 succeeds with Symp_form-survival verified (W3-W35-05).
No manuscript content modified; all work at reconstitution-
ledger / Phase-4-program level.

End of P4-G4 Phase-4 ledger.
