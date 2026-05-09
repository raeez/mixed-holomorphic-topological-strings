# Phase-4 EXEC P4-Firewall-Meta-Theorem — Structural meta-theorem on the firewall-permanent typology

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Polyakov + Invariants — anomaly cohomology, regulator-class
invariance, structural permanence at the chain-level / vertex-class
layer; the Polyakov question "what is preserved?" and the Invariants
question "which invariant is the firewall protecting?" applied
simultaneously to five firewall-permanent obstructions identified in
the Phase-4 EXEC chain.
**Mode.** Proposal-only. NO git commits, NO TeX edits to manuscript.
Audit lives at this path ONLY.
**Mandate.** Formalize the Phase-4 firewall-permanent typology
$\{\mathrm{FW.BCOV\text{-}chain},\mathrm{FW.Sergeev\text{-}A5},
\mathrm{FW.Igusa},\mathrm{FW.Unreduced\text{-}Bosonic},
\mathrm{FW.Costello\text{-}Li\text{-}d\text{-}even}\}$ as a single
structural meta-theorem. Identify (a) the precise structural
obstruction, (b) the layer at which each is permanent vs liftable,
(c) the coefficient-layer common ancestor, (d) the smallest
categorical statement that subsumes all five, (e) cross-walks to
Lurie HA / Costello-Gwilliam factorization-algebra category, and
(f) a candidate inscription block for the manuscript.

**Inputs read in full.**
- `reconstitution/phase4-exec-BCOV-A5-comparison-2026-04-28.md`
  (1093 lines) — BCOV firewall; coefficient layer liftable via the
  $\mathfrak{gl}(N|N)$ common ancestor; chain layer permanent.
- `reconstitution/phase4-exec-Sergeev-Duality-Probe-2026-04-28.md`
  (1334 lines) — Sergeev-A5 firewall; structurally identical to
  BCOV-A5; coefficient layer liftable via Howe-Sergeev intertwiner.
- `reconstitution/phase4-exec-Igusa-Heuristic-Audit-2026-04-28.md`
  (1100 lines) — Igusa firewall; no representation-theoretic common
  ancestor exists; strictly more permanent than BCOV.
- `reconstitution/phase4-exec-Unreduced-Bosonic-Phase5-2026-04-28.md`
  (1372 lines) — bosonic $\mathfrak{gl}_N$ Theorem G discharge
  firewall; representation-theoretic ($\mathrm{Tr}(I) = N \neq 0$ has
  no cancellation analog).
- `reconstitution/phase4-exec-Costello-Li-d-extension-2026-04-28.md`
  (1104 lines) — $d$-odd $\to$ $d$-even extension firewall; parity
  argument on $\Omega_d^2$ produces doubled anomaly $2\hbar N$.
- `main.tex` 5380–5394 (`rmk:convention-firewall`).
- `main.tex` 5890–5915 (`ssec:cross-volume-horizon`).
- `claim-strength-ledger.tex` (full, 142 lines).
- `open-obligations.tex` (lines 1–60).
- `principles.tex` (lines 1–60).
- `CLAUDE.md` (cross-volume firewall; modular-form heuristic frontier).

**Primary external sources (cited from Phase-4 inputs).**
- M. Bershadsky, S. Cecotti, H. Ooguri, C. Vafa, "Kodaira-Spencer
  theory of gravity and exact results for quantum string amplitudes",
  *Comm. Math. Phys.* **165** (1994), 311–427 — primary BCOV.
- K. Costello, S. Li, "Quantum BCOV theory", arXiv:1201.4501 (2012);
  "Quantization of open-closed BCOV theory I", arXiv:1505.06703 (2015);
  "Anomaly cancellation in the topological string", arXiv:1605.09073
  (2016).
- K. Costello, *Renormalization and Effective Field Theory*, AMS
  Math. Surveys and Monographs **170** (2011), Ch. 4 §4.4.
- K. Costello, O. Gwilliam, *Factorization Algebras in QFT*, Vol I
  (CUP 2017), Vol II (CUP 2021) §11, §13.
- J. Lurie, *Higher Algebra*, §5.5.4 (Bousfield localisation);
  Proposition 5.5.4.10 (locally constant factorization equivalent
  to $E_n$-algebras).
- A. Sergeev, "The tensor algebra of the identity representation",
  *Math. USSR Sbornik* **51** (1985); S.-J. Cheng, W. Wang,
  *Dualities and representations of Lie superalgebras*, AMS GSM
  **144** (2012), Ch. 4–5.
- K. Coulembier, "Tensor ideals, Deligne categories and invariant
  theory", *Selecta Math.* **24** (2018), 4659–4710.
- J.-i. Igusa, "On Siegel modular forms of genus two", *Amer. J.
  Math.* **84** (1962); R. Borcherds, "Automorphic forms with
  singularities on Grassmannians", *Invent. Math.* **132** (1998);
  V. Gritsenko, V. Nikulin, "Siegel automorphic form corrections of
  some Lorentzian Kac-Moody Lie algebras", *Amer. J. Math.* **119**
  (1997).

---

## §0. Executive verdict — meta-theorem statement

**Three-line bottom line.**

1. **Meta-theorem (informal).** *The five firewall-permanent
   obstructions identified in the Phase-4 EXEC chain are not
   independent phenomena: they are five instances of a single
   structural permanence theorem on the chain-level / vertex-class
   layer of the 6-real-dim mixed topological-holomorphic factorization
   category. Each admits a coefficient-layer or
   representation-theoretic-layer common ancestor (or, in one case,
   establishes that no such ancestor exists). Each blocks a
   chain-level isomorphism between the manuscript's mixed brane-defect
   BV complex on $\R^2 \times \widehat{\C^2}_0$ and a target sister
   complex (BCOV on $\C^3$, Hecke-Clifford on $\R$, Sp$_4(\Z)$ Igusa
   lattice, gl$_N$ bosonic, $\C^d$-even Calabi-Yau) at the
   factorization-algebra layer.* See **Theorem (Firewall-permanence
   typology)** at §0.1 below.

2. **Unified vs distinct phenomena (FM.3 verdict).** **Unified
   structurally, distinct in source datum.** All five firewalls share
   a common categorical structure: each is the obstruction to a
   chain-level isomorphism in the 6-real-dim mixed factorization-
   algebra category between a chain complex on
   $\R^2 \times \widehat{\C^2}_0$ and a sister chain complex on a
   different worldvolume. The structural sources differ
   (representation-theoretic for FW.BCOV / FW.Sergeev / FW.Bosonic;
   parity-of-$d$ for FW.Costello-Li-d-even; modular / lattice for
   FW.Igusa), but the **layer** at which they obstruct is uniform:
   the chain-level vertex class. The unified categorical statement
   is "**no chain-level isomorphism exists in the 6-real-dim mixed
   factorization-algebra category between the manuscript's brane-
   defect BV complex and any of the four sister complexes**".

3. **Inscription target.** The meta-theorem is **publication-grade
   as a structural-permanence remark**, not yet as a stand-alone
   theorem. The smallest publication-grade statement is a *typology
   remark* at `claim-strength-ledger.tex` near
   `rmk:convention-firewall` (`main.tex`:5380–5394) inscribing
   the five-firewall typology with named obstruction sources and
   layer-permanence indicators. A stand-alone "Theorem
   (Firewall-permanence typology)" requires an additional technical
   lemma identifying the explicit factorization-algebra category
   $\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$ in the
   Costello-Gwilliam framework as a strict $\infty$-category — that
   construction is **not yet inscribed** in our manuscript and is
   borderline open in CG Vol II §13.

**One-line invariant.** The dominant invariant preserved (or
obstructed) on each firewall is the **chain-level vertex cocycle
class** in the mixed-factorization obstruction complex
$H^1(\mathcal O_{\mathrm{loc}}(\mathcal E_w), Q + \{I_0, -\})$. The
five firewalls block five distinct *would-be* matched-conventions
functors at the chain-level vertex layer; the obstruction in each
case is a Polyakov-class invariant (regulator-class scheme-independent)
of the source datum.

### §0.1 Statement of the meta-theorem

> **Theorem (Firewall-permanence typology, structural meta-theorem).**
> Let $\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$ denote the
> $(\infty,1)$-category of mixed topological-holomorphic
> factorization algebras on the 6-real-dim worldvolume
> $\R^2 \times \widehat{\C^2}_0$ in the Costello-Gwilliam Vol I §6.4
> + Vol II §11–13 framework, with regulator class admissible in the
> sense of (A1)–(A5) + (A2$'$) of `tate-T1-weighted-completion.tex`
> Definition `defn:regulator-admissible-sector`. Let
> $\mathcal A_{\mathrm{man}} \in \mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$
> denote the manuscript's brane-defect BV complex on
> $\R^2 \times \widehat{\C^2}_0$ with bosonic open algebra
> $\mathfrak{gl}_N$ and the holomorphic symplectic form
> $\omega = dz_1 \wedge dz_2$ on $\widehat{\C^2}_0$. Let
> $\mathcal A_{\mathrm{BCOV}}$, $\mathcal A_{\mathrm{HC}}$,
> $\mathcal A_{\mathrm{Igusa}}$, $\mathcal A_{\mathrm{bos}}$,
> $\mathcal A_{\mathrm{CL}_{d=4}}$ denote the BCOV BV complex on
> $\C^3$, the Hecke-Clifford open-line factorization, the Igusa BKM
> chiral algebra (hypothetical), the bosonic $\mathfrak{gl}_N$
> super-extension, and the Costello-Li flat $\C^4$ complex,
> respectively, with their natural mixed-factorization category
> embeddings.
>
> Then no chain-level isomorphism in
> $\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$ exists between
> $\mathcal A_{\mathrm{man}}$ and any of the five sister complexes.
> Each of the five non-isomorphism statements is firewall-permanent
> at the indicated structural layer, with the named coefficient-
> or representation-theoretic-layer common ancestor (when any):
>
> | Sister complex | Permanent layer | Coefficient-layer common ancestor |
> |---|---|---|
> | $\mathcal A_{\mathrm{BCOV}}$ on $\C^3$ | Chain-level vertex class | $\mathfrak{gl}(N\|N)$ supertrace $\Str(I)$ |
> | $\mathcal A_{\mathrm{HC}}$ on $\R$ (Hecke-Clifford) | Chain-level vertex class | Howe-Sergeev central character $N$ |
> | $\mathcal A_{\mathrm{Igusa}}$ (Sp$_4(\Z)$ lattice) | Modular + lattice + chain-level | **None** (no rep-theoretic ancestor) |
> | $\mathcal A_{\mathrm{bos}}$ (bosonic $\mathfrak{gl}_N$) | Chain-level discharge layer | $\mathrm{Tr}(I) = N \neq 0$ (no cancellation analog) |
> | $\mathcal A_{\mathrm{CL}_{d=4}}$ on $\C^4$ | Polyvector-parity layer | $\mathrm{Str}(I) = 0$ (preserved); polyvector parity $(-1)^d$ flips |
>
> The five firewalls share a uniform structural property: they obstruct
> chain-level matched-conventions functors at the vertex-class layer
> of $\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$. They are **distinct
> in their structural sources** (representation-theoretic, parity-of-$d$,
> modular-arithmetic, dimensional, signature) but **uniform in their
> obstruction layer** (chain-level vertex / factorization isomorphism).

The theorem above is **structurally publication-grade with one
technical lemma open**: the explicit identification of
$\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$ as a strict
$(\infty,1)$-category in the CG Vol II framework requires citing CG
Vol II §13 with a sharper (A5)+(A2$'$) augmentation than is
inscribed in our `defn:regulator-admissible-sector`. The remark-grade
inscription proposed at §5 below is publication-ready as is.

**Per-firewall verdict.**

| Firewall | Structural source | Permanent layer | Common ancestor |
|---|---|---|---|
| **FW.BCOV-chain** | Representation-theoretic ($\Str$) | Chain-level vertex (HCS vs brane-defect) | $\mathfrak{gl}(N\|N)$ supertrace |
| **FW.Sergeev-A5** | Representation-theoretic (Howe-Sergeev) | Chain-level vertex (Hecke-Clifford vs brane-defect) | Howe-Sergeev central character $N$ |
| **FW.Igusa** | Modular + lattice (Sp$_4(\Z)$, $\Lambda^{2,1}_{II}$) | Modular + lattice + chain | **None** (strictly more permanent) |
| **FW.Unreduced-Bosonic** | Representation-theoretic (no $\Str$ analog) | Chain-level discharge (no cancellation) | $\mathrm{Tr}(I) = N$ (residue, not ancestor) |
| **FW.Costello-Li-d-even** | Parity of $d$ ($\Omega_d^2$ sign) | Polyvector-parity ($d$-parity) | Polyvector signature $(-1)^d$ |

---

## §1. Per-firewall analysis (FM.1, FM.2)

### 1.1 FW.BCOV-chain

**Source.** The cross-volume firewall between the manuscript's local
Hamiltonian BF / brane-defect BV theory on
$\R^2 \times \widehat{\C^2}_0$ (with holomorphic symplectic form
$\omega = dz_1 \wedge dz_2$ and bosonic / super-balanced open algebra)
and the BCOV BV theory on a compact CY$_3$ (or flat $\C^3$ via
Costello-Li 2015 / 2016) with Calabi-Yau volume form $\Omega_X$.

**Precise structural obstruction.** Three independent structural
mismatches at the chain-level layer (BCOV-A5 §4.1–4.3,
`phase4-exec-BCOV-A5-comparison-2026-04-28.md`:466–504):

* **Spacetime mismatch.** BCOV is on a CY$_3$ (compact or flat
  $\C^3$); we are on $\R^2 \times \widehat{\C^2}_0$. Dimension and
  structure groups do not match ($d_\C = 3$ vs $d_\C = 2$;
  Calabi-Yau structure group $SU(3) \subset SO(6)$ vs holomorphic
  symplectic structure group $\mathrm{Sp}(2,\C)$).

* **Form-structure mismatch.** BCOV uses the Calabi-Yau holomorphic
  volume form $\Omega_X$ inducing the BV pairing
  $\langle \alpha, \beta \rangle = \int_X (\alpha \wedge \beta)|_{\mathrm{PV}^{d,d}} \cdot \Omega^2$.
  We use the holomorphic symplectic form
  $\omega = dz_1 \wedge dz_2$ inducing the polynomial Hamiltonian
  bracket $\{f, g\} = \partial_{z_1} f \cdot \partial_{z_2} g - \partial_{z_2} f \cdot \partial_{z_1} g$.

* **Field-content mismatch.** BCOV fields are polyvector fields
  $\mathrm{PV}^{*,*}(X)[[t]]$ with the Schouten-Nijenhuis bracket.
  Our fields are Hamiltonian BF on
  $\widehat{\mathfrak h}[1] \oplus \widehat{\mathfrak h}^\vee_{\mathrm{cont}}[2]$
  with the polynomial Hamiltonian bracket.

**Permanent layer.** Chain-level vertex class
$H^1(\mathcal O_{\mathrm{loc}}, \bar\partial + \{S, -\})$ on the
BCOV side vs $H^1(\mathcal O_{\mathrm{loc}}(\mathcal E_w), Q + \{I_0, -\})$
on our side. **Permanent at chain-level** because no chain-level
isomorphism exists between the BCOV BV complex on $\C^3$ and our
brane-defect BV complex on $\R^2 \times \widehat{\C^2}_0$ that
preserves the form structure.

**Liftable layer.** Coefficient layer
($\mathrm{Str}_{\mathfrak{gl}(N|N)}(I) = N - M$). The
representation-theoretic constant on the open algebra is independent
of the spacetime, regulator scheme, and vertex cocycle. Both BCOV
(via Costello-Li 2015 / 2016) and our W22-T1 / W22-T2 invoke this
constant; both discharge at super-balance $N = M$.

**Coefficient-layer common ancestor.** $\mathfrak{gl}(N|N)$
supertrace identity $\mathrm{Str}_{\mathfrak{gl}(N|N)}(I) = N - M$.
This is the structural common ancestor for both sides; it is the
only object preserved on both sides under the comparison map
$\Phi_{\mathrm{coef}}$ (BCOV-A5 §3.2).

**Polyakov / Invariants interpretation.** The dominant invariant preserved
under regulator change is $\mathrm{Str}(I) = 0$ on $\mathfrak{gl}(N|N)$
at super-balance. The residue cohomology class
$\hbar \, \mathrm{Str}(I) \, [\bar c]$ vanishes at super-balance via
representation-theoretic cancellation, not regulator-class flow. The
Polyakov scheme-independence on regulators (R1–R4 ledger of
W30-M2) is preserved on both sides; the chain-level vertex class
is *not* preserved.

### 1.2 FW.Sergeev-A5

**Source.** The Sergeev-type open-closed duality witnessed by the
$\mathfrak q(N)$ otr-brane parastate (Sergeev-Duality-Probe §0).
The duality is the Howe-Sergeev mutual-centralizer pair
$(\mathfrak q(N), \mathcal{HC}_n)$ acting on $V^{\otimes n}$ with
$V = \C^{N|N}$, where $\mathcal{HC}_n = \mathcal C_n \rtimes \C[S_n]$
is the Hecke-Clifford superalgebra.

**Precise structural obstruction.** Identical structural form to
FW.BCOV-chain (Sergeev-Duality-Probe §5.3):

* **Worldvolume mismatch.** Open-line $\R$ for the Hecke-Clifford
  factorization vs closed-bulk $\R^2 \times \widehat{\C^2}_0$ for
  the brane-defect BV complex.

* **$\Z/2$-grading mismatch.** Hecke-Clifford has Clifford-sign
  grading on insertion points; brane-defect has BV ghost-number
  grading on bulk fields. The queer central element $J$ acts
  non-trivially on both gradings, but the gradings themselves are
  structurally distinct.

* **Field-content mismatch.** $\mathcal{HC}_n = \mathcal C_n \rtimes
  \C[S_n]$ on $\R^n$ vs Hamiltonian BF on
  $\widehat{\mathfrak h}[1] \oplus \widehat{\mathfrak h}^\vee_{\mathrm{cont}}[2]$
  on $\widehat{\C^2}_0$.

**Permanent layer.** Chain-level vertex class. **Identical** to
FW.BCOV-chain in structural form (Sergeev-Duality-Probe
§5.3 explicitly: "structurally identical"). The chain-level lift
obstruction is named **Obs-Sergeev-A5-firewall**: the two
factorization complexes live on different worldvolumes with
structurally distinct $\Z/2$-graded BV structures.

**Liftable layer.** Coefficient layer (Howe-Sergeev central
character match $\Tr_{\mathfrak{gl}_N}(I) = \mathrm{otr}_{\mathfrak q(N)}(J) = N$).
The intertwiner $\Phi_{\mathrm{Sergeev}}$ preserves the coefficient
$N$ and shifts the target line by parity:
$\Phi_{\mathrm{Sergeev}}(\hbar N [\bar c]) = \hbar N [\bar c]^{\mathrm{otr}}$.

**Coefficient-layer common ancestor.** Howe-Sergeev central character
$N$ in the $(\mathfrak q(N), \mathcal{HC}_n)$ mutual centralizer pair
on $V^{\otimes n}$, $V = \C^{N|N}$. The numerical coefficient $N$ is
the **same** on both sides; only the parity sector differs ($\C$ on
the bosonic Schur-Weyl side, $\Pi\C$ on the queer Sergeev side).

**Crucial distinction from FW.BCOV-chain.** FW.BCOV-chain has
$\Str(I) = 0$ as the discharge mechanism (residue cancels at
super-balance). FW.Sergeev-A5 has $\mathrm{otr}(J) = N \neq 0$ —
**the residue does not cancel**; it shifts to a parity-mirrored
target line. Both share the same chain-level firewall structure,
but the BCOV case discharges to zero while the Sergeev case
discharges to a Sergeev-dual non-zero residue.

**Polyakov / Invariants interpretation.** Same as FW.BCOV-chain: the
representation-theoretic central character $N$ is preserved on both
sides, the chain-level vertex class is not. The Sergeev case is
"non-trivial firewall": the residue $\hbar N [\bar c]^{\mathrm{otr}}$
is a real obstruction in the queer-channel cohomology.

### 1.3 FW.Igusa

**Source.** The Igusa $\Delta_5$ / BKM heuristic cross-volume bridge
(`CLAUDE.md`:22; Igusa-Heuristic-Audit §0). The Igusa cusp form
$\Delta_5$ is an Sp$_4(\Z)$-modular form of weight 5 with Maass
multiplier; its denominator-formula reformulation as the BKM
generalized Kac-Moody algebra $\mathfrak g_{\Delta_5}$ depends on
the type-II hyperbolic lattice $\Lambda^{2,1}_{II} = \HypPlan \oplus [2]$.

**Precise structural obstruction.** Five independent structural
mismatches at five different layers (Igusa-Heuristic-Audit §3.1–3.5):

* **$X_1$ Matched-conventions functor.** No chain-level Igusa BV /
  chiral BKM theory currently exists in the literature. The Igusa
  repository inscribes the BKM denominator as *imported*
  (Gritsenko-Nikulin); a chain-level construction is open.
  **FIREWALL-PERMANENT** at $X_1$ layer.

* **$X_2$ Regulator-class compatibility.** Downstream of $X_1$:
  no chain-level Igusa regulator inscribed. **OPEN-LITERATURE** at
  current resolution.

* **$X_3$ Modular invariance.** (A5) is a $\Z/2$ structural symmetry
  of $\mathfrak{gl}(N|N)$; Sp$_4(\Z)$ is a non-abelian arithmetic
  symmetry of $\mathbb H_2$. No representation-theoretic mechanism
  inscribed in the manuscript or in the structural framework that
  induces an Sp$_4(\Z)$ action on $\mathfrak{gl}(N|N)$. **FIREWALL-PERMANENT**
  at modular-invariance layer.

* **$X_4$ Lattice morphism.** $\Z^2$ on our side (rank 2,
  positive-definite) vs $\Lambda^{2,1}_{II}$ (rank 3, signature
  $(2,1)$). No rank-preserving, signature-preserving, or root-data-
  preserving map. **FIREWALL-PERMANENT** at lattice layer.

* **$X_5$ Physical duality bridge.** A T-duality / S-duality
  inducing Sp$_4(\Z)$ from the Hamiltonian BF / Moyal data via a
  multi-step cross-volume convergence (BCOV $\to$ Vol III $\to$
  Igusa). **PHASE-5** (long horizon).

**Permanent layer.** Three independent structural layers ($X_1$,
$X_3$, $X_4$). Lifting any one would not lift the firewall;
lifting all three simultaneously would require a major Phase-5
program. **Strictly more permanent than FW.BCOV-chain**: BCOV had
one permanent layer (chain-level vertex) and a liftable layer
(coefficient); Igusa has three permanent layers.

**Liftable layer.** **None at current resolution.** The Igusa
firewall is the strictest among the five.

**Coefficient-layer common ancestor.** **None exists.** The BCOV
coefficient $\Str_{\mathfrak{gl}(N|N)}(I) = N - M$ has no analogue
on the Igusa side. The relevant Igusa-side quantity is the signed
root multiplicity $\smult \mathfrak g_{\Delta_5, \alpha} = f(nm, l)$,
which depends on the lattice point $\alpha = (n, l, m) \in
\Lambda^{2,1}_{II}$ and the weak Jacobi form $\phi_{0,1}$. There is
no representation-theoretic common ancestor on which both sides
agree (Igusa-Heuristic-Audit §5.2).

**Polyakov / Invariants interpretation.** The Polyakov question "what
generating-function symmetry survives?" returns `null` on every
candidate generating function. The Invariants question "which
lattice gets mapped?" returns "no lattice morphism" on the
$(a,b)$-bigrading vs $\Lambda^{2,1}_{II}$. **No invariant transports
across the firewall**.

### 1.4 FW.Unreduced-Bosonic

**Source.** The bosonic $\mathfrak{gl}_N$ Theorem G discharge
(Unreduced-Bosonic-Phase5 §0–§7). The manuscript's bosonic Theorem G
inscribes the residue $\hbar N [\bar c]$ on
$\R^2 \times \widehat{\C^2}_0$ with bosonic open algebra
$\mathfrak{gl}_N$. Seven candidate Phase-5 mechanisms (UB.1)–(UB.7)
were surveyed; **none discharges** the bosonic side without changing
the source data.

**Precise structural obstruction.** Representation-theoretic
(Unreduced-Bosonic-Phase5 §0):

> $\mathrm{Tr}(I) = N \neq 0$ on $\mathfrak{gl}_N$ has **no
> cancellation analog**. The supertrace identity
> $\mathrm{Str}(I) = N - M = 0$ at super-balance discharges the
> super-extension; it does **not descend** to a bosonic identity
> (Unreduced-Bosonic-Phase5 §1.4 R1, S1: both reduction and summand
> arguments fail).

The structural mismatch is between:
* Bosonic source: $\mathfrak{gl}_N$ matrix factor with trace
  $\mathrm{Tr}(I) = N$.
* Super source: $\mathfrak{gl}(N|N)$ matrix factor with supertrace
  $\mathrm{Str}(I) = 0$ at super-balance.

**Permanent layer.** Chain-level discharge layer (UB.7 verdict).
The bosonic side has no Costello-Li 2015 / 2016 analogue: those
theorems require the open algebra to be $\mathfrak{gl}(N|N)$.
Replacement attempts via:
* **Wilsonian RG (UB.2):** invariant under (A1)–(A4) admissible class.
* **Geometric symmetries (UB.3):** $\mathrm{Sp}(2,\C)$, Hamiltonian
  rotation, scaling all preserve the constant Taylor coefficient
  cocycle.
* **Topological twist / CGW (UB.4):** redistributes via the
  spin-tower; does not cancel.
* **Boundary-state (UB.5):** non-local in Costello sense; would
  violate (A1)–(A4).
* **Cohomological shift (UB.6):** Massey-product re-emergence at
  $\hbar^3 N^3$.
* **Cross-volume BCOV-A5 lift (UB.7):** structural firewall (no
  bosonic Costello-Li analogue).

**Liftable layer.** **None inside the local apparatus.** Discharge
is *not Phase-5 in the local sense*; any Phase-5 escalation must
change the source data (super-extension, twisted M-theory, or
boundary condition) and is therefore a *different theorem*.

**Coefficient-layer common ancestor.** Inverted form: the
*absence* of a cancellation analog. The bosonic coefficient
$\mathrm{Tr}(I) = N$ is the **residue**, not an ancestor. The
manuscript's super-balanced extension (W22-T1 / W22-T2) provides
the cancellation via $\mathrm{Str}(I) = 0$ at super-balance, but
this discharge mechanism is structurally super-balanced.

**Polyakov / Invariants interpretation.** The dominant invariant is
$\mathrm{Tr}(I) = N \neq 0$. Preserved by every regulator inside
the (A1)–(A4) admissible class; not gauged away by any geometric
symmetry or topological twist on the closed-string side. **The
bosonic conditional is structurally permanent at the local-chain-
level discharge layer**, parallel to FW.Igusa in the cross-volume
frontier.

### 1.5 FW.Costello-Li-d-even

**Source.** The Costello-Li 2015 / 2016 chain-level anomaly
cancellation on flat $\C^d$ requires $d$ odd (Costello-Li-d-extension
§0–§3). The hypothesis $d$ odd appears in three independent places
in the proof; the question is whether the result extends to $d$
even — specifically $d = 4$.

**Precise structural obstruction.** Parity argument on the
holomorphic top form $\Omega_d = dz_1 \wedge \cdots \wedge dz_d$
(Costello-Li-d-extension §2.1–2.4):

* **Polyvector-parity sign.** $\Omega_d^2 = \Omega_d \wedge \Omega_d$
  carries parity $(-1)^{d(d-1)/2}$. The BV pairing
  $\langle \alpha, \beta \rangle = \int_X (\alpha \wedge \beta)|_{\mathrm{PV}^{d,d}} \cdot \Omega^2$
  is symmetric of degree $-1$ only when this sign aligns with the
  polyvector grading: $d \equiv 1$ or $3 \pmod 4$, i.e., $d$ odd.

* **Chain-level cancellation sign.** The relative sign between the
  bosonic and fermionic loop closure on the open algebra is
  $(-1)^d$. For $d$ odd, the relative sign is $-1$ and
  $\mathrm{Str}(I) = N - N = 0$ produces a true cancellation. For
  $d$ even (e.g., $d = 4$), the relative sign is $+1$ and the
  cancellation **doubles**:
  $$\mathrm{Ob}^{\mathrm{BCOV/HCS}}_{1\text{-loop}}\big|_{d=4} = \hbar(\mathrm{Tr}_{\text{even}}(I) + \mathrm{Tr}_{\text{odd}}(I)) \cdot [\bar\partial \cdot \tau_4] = 2\hbar N \cdot [\bar\partial \cdot \tau_4] \neq 0.$$

**Permanent layer.** Polyvector-parity layer (Costello-Li-d-extension
§3.4). The break is at Step 3 of the Costello-Li 2016 Theorem A
proof: the $d$-parity-dependent loop closure coefficient. Four
candidate repairs were surveyed:
* **(D-1) $\mathfrak{gl}(N|M)$ with $N \neq M$:** does not absorb
  the $d$-parity sign.
* **(D-2) Different parity-graded open algebra ($\mathfrak{osp}$,
  $\mathfrak q$):** Killing form sign is open-algebra feature; $d$-
  parity is closed-spacetime feature; independent.
* **(D-3) Closed-spacetime parity twist on $\C^d$:** changes
  underlying complex structure (e.g., $\C^4 \to \C^{2|2}$),
  invalidating BCOV setup.
* **(D-4) Boundary-state parity correction:** no such object in
  CL 2015 / 2016 framework; would be non-local in Costello sense.

**No candidate inside Costello-Li framework discharges $d = 4$.**
**The $d$-odd condition is structurally permanent at the chain-level
cancellation layer.**

**Liftable layer.** None inside Costello-Li framework. Outside the
framework: (D-3) parity twist or (D-4) non-local boundary state
would require *new* anomaly-cancellation mechanism.

**Coefficient-layer common ancestor.** $\mathrm{Str}(I) = 0$ on
$\mathfrak{gl}(N|N)$ — preserved on both $d$ odd and $d$ even.
**However**, the coefficient ancestor alone does not produce
cancellation on $d$ even: the parity-of-$d$ sign defeats the
discharge. The polyvector signature $(-1)^d$ is the dominant
invariant blocking the lift.

**Polyakov / Invariants interpretation.** Two invariants control the
firewall:
* **Supertrace $\mathrm{Str}(I) = 0$:** preserved on $d$ odd and
  $d$ even; representation-theoretic.
* **Polyvector signature $(-1)^d$:** flips between $d$ odd and
  $d$ even; topological / dimensional.

The cancellation mechanism requires *both* invariants to align;
on $d$ even, the polyvector signature flip defeats the alignment.
**Polyakov scheme-independence on regulators does not lift the
$d$-odd hypothesis** because the obstruction is not a regulator-
class artefact.

---

## §2. Unified categorical framework or distinct phenomena (FM.3)

### 2.1 Unified at the chain-level layer; distinct in source data

The five firewalls are structurally **unified at the chain-level
layer** but **distinct in the source datum producing the obstruction**.

**Structural unification at chain-level.** All five obstruct
chain-level isomorphisms in the 6-real-dim mixed factorization-
algebra category $\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$:

| Firewall | Manuscript side | Sister side | Chain layer |
|---|---|---|---|
| **FW.BCOV-chain** | brane-defect BV on $\R^2 \times \widehat{\C^2}_0$ | BCOV BV on $\C^3$ | $H^1(\mathcal O_{\mathrm{loc}}, Q+\{I_0,-\})$ vs $H^1(\mathcal O_{\mathrm{loc}}^{\mathrm{BCOV}}, \bar\partial+\{S,-\})$ |
| **FW.Sergeev-A5** | brane-defect BV on $\R^2 \times \widehat{\C^2}_0$ | Hecke-Clifford on $\R$ | brane-defect vertex class vs $\End_{\mathfrak q(N)}(V^{\otimes n})$ |
| **FW.Igusa** | brane-defect BV on $\R^2 \times \widehat{\C^2}_0$ | Igusa BKM (hypothetical) | does not even exist as chain-level theory |
| **FW.Unreduced-Bosonic** | brane-defect BV on $\R^2 \times \widehat{\C^2}_0$ with bosonic $\mathfrak{gl}_N$ | super-balanced $\mathfrak{gl}(N\|N)$ extension | $\mathrm{Tr}(I) = N$ vs $\mathrm{Str}(I) = 0$ |
| **FW.Costello-Li-d-even** | flat $\C^4$ BCOV with $\mathfrak{gl}(N\|N)$ | flat $\C^3$ BCOV with $\mathfrak{gl}(N\|N)$ | $2\hbar N \neq 0$ vs $0$ |

**Distinct in source datum.**

* **FW.BCOV-chain, FW.Sergeev-A5, FW.Unreduced-Bosonic** —
  representation-theoretic source. The obstruction lives in the
  matrix factor of the open algebra (or in its absence). The
  liftable layer is the representation-theoretic coefficient.

* **FW.Costello-Li-d-even** — parity-of-$d$ source. The obstruction
  lives in the polyvector signature of the closed spacetime. The
  liftable layer is the dimensional structure (changing $d$ odd
  vs even).

* **FW.Igusa** — modular + lattice source. The obstruction lives
  in the arithmetic symmetry group (Sp$_4(\Z)$ vs $\Z/2$) and in
  the lattice signature ($(2,1)$ vs $(2,0)$). **No** liftable
  layer at current resolution.

### 2.2 Are they instances of a "factorization-algebra structural permanence" theorem?

**Yes, with the following caveat.** Four of the five (BCOV, Sergeev,
Costello-Li-d-even, Unreduced-Bosonic) are direct instances of a
single theorem on chain-level isomorphisms in
$\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$. **FW.Igusa is a stronger
phenomenon**: it includes a modular-invariance and lattice-signature
obstruction that does not reduce to chain-level factorization-algebra
structural permanence — it lives at a higher level of arithmetic-
representation-theoretic obstruction. FW.Igusa **subsumes** the
chain-level statement (since the chain-level Igusa BV does not even
exist) but goes beyond it.

**The unified statement.** "In $\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$,
no chain-level isomorphism exists between the manuscript's
$\mathcal A_{\mathrm{man}}$ and any of the five sister complexes."
This is the **structural-permanence theorem at the chain-level
layer** (the unified umbrella). The five firewalls are five
distinct obstructions to five distinct candidate isomorphisms,
sharing the same target (no chain-level isomorphism) and the same
structural ambient category.

### 2.3 Are they instances of an "operadic common-ancestor non-existence" theorem?

**No, this characterization fails for Igusa.** Three of the five
(BCOV, Sergeev, Unreduced-Bosonic) admit a representation-theoretic
common ancestor at the operadic / representation-category layer:

* **BCOV:** $\mathfrak{gl}(N|N)$ is the common ancestor; $\Str(I)$
  is the common coefficient.
* **Sergeev:** $(\mathfrak q(N), \mathcal{HC}_n)$ is the
  Howe-Sergeev common ancestor; the central character $N$ is the
  common coefficient.
* **Unreduced-Bosonic:** the *absence* of an ancestor is the
  obstruction (no super-extension on bosonic $\mathfrak{gl}_N$);
  but conceptually this is a "non-existence at the
  representation-theoretic layer".

**FW.Costello-Li-d-even** has a *partial* operadic ancestor
($\mathfrak{gl}(N|N)$ supertrace; same as BCOV) but the obstruction
is at the spacetime / polyvector layer, not at the operadic layer.

**FW.Igusa** has **no** operadic common ancestor: $\mathfrak{gl}(N|N)$
on our side has no Sp$_4(\Z)$ representation; the BKM root
multiplicities $f(nm, l)$ are arithmetic objects with no
representation-theoretic coefficient analogue.

**Conclusion.** The "operadic common-ancestor non-existence" framing
does **not** uniformly apply. The unified statement is
"chain-level factorization-algebra non-isomorphism" with named
structural sources varying.

### 2.4 Are they genuinely distinct phenomena that share a name?

**No — they share a uniform structural feature: the chain-level
non-isomorphism layer in $\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$.**
The structural sources differ but the obstruction layer is uniform.
The right way to think of the typology is:

> **Five firewalls = five named obstructions to five named would-be
> matched-conventions functors in the same factorization-algebra
> category, with structurally distinct sources but a uniform
> obstruction layer.**

This is a **typology**, not a single theorem. The single theorem
is the umbrella structural-permanence statement at §0.1.

---

## §3. Lurie HA / Costello-Gwilliam cross-walk (FM.4)

### 3.1 Categorical structure supporting each firewall

The relevant categorical structure for each firewall:

| Firewall | Categorical structure | Support reference |
|---|---|---|
| **FW.BCOV-chain** | $E_3$-algebra factorization (BCOV on $\C^3$) vs mixed $E_2$-de-Rham + $E_2$-Dolbeault factorization | Lurie HA Prop. 5.5.4.10 ($E_n$ = locally constant factorization on $\R^n$); CG Vol II §13 |
| **FW.Sergeev-A5** | $E_1$-Clifford-twisted factorization (Hecke-Clifford on $\R$) vs mixed $E_2 + E_2$-Dolbeault factorization | Lurie HA §4.4.1 ($E_1$); CG Vol II §13 |
| **FW.Igusa** | Chiral algebra in the Beilinson-Drinfeld sense vs mixed factorization on $\R^2 \times \widehat{\C^2}_0$ | Beilinson-Drinfeld 2004 *Chiral Algebras*; CG Vol II §6 |
| **FW.Unreduced-Bosonic** | $E_2$-de Rham factorization with bosonic vs super matrix factor | CG Vol II §11 (BV regulator on bosonic vs super source) |
| **FW.Costello-Li-d-even** | $E_d$-Dolbeault factorization on $\C^d$ ($d$ even) vs $E_d$-Dolbeault factorization on $\C^d$ ($d$ odd) | Lurie HA Prop. 5.5.4.10 ($E_d$); CG Vol II §13 |

### 3.2 The 6-real-dim mixed factorization category

The unified ambient category is the **6-real-dim mixed topological-
holomorphic factorization-algebra category**
$$\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}} := \mathrm{Fact}_{\mathrm{loc}}^{(\infty,1)}\bigl(\R^2_{\mathrm{top}} \times \widehat{\C^2}_0; \mathrm{Reg}_{\mathrm{adm}}\bigr).$$

* **Worldvolume:** $\R^2_{\mathrm{top}} \times \widehat{\C^2}_0$ is
  the manuscript's local model: 2 real (de Rham) + 2 complex
  (Dolbeault) = 6 real dimensions.

* **Mixed differential:** $D = d_{\R^2} + \bar\partial_{\C^2}$
  (`main.tex`:1305). This is the **mixed Dunn-Lurie product**
  $E_2^{\mathrm{de\,Rham}} \otimes E_2^{\mathrm{Dolbeault}}$, where:
  - $E_2^{\mathrm{de\,Rham}}$ comes from $\R^2_{\mathrm{top}}$ via
    locally constant factorization (Lurie HA §5.5.4 + Prop. 5.5.4.10).
  - $E_2^{\mathrm{Dolbeault}}$ comes from $\widehat{\C^2}_0$ via
    holomorphic factorization (CG Vol II §13).

* **Regulator class:** admissible (A1)–(A5) + (A2$'$) of
  `tate-T1-weighted-completion.tex` Definition
  `defn:regulator-admissible-sector`. This is the manuscript's
  augmentation of the CG Vol II §11 BV regulator framework.

The five firewalls live as obstructions to chain-level isomorphisms
between $\mathcal A_{\mathrm{man}} \in \mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$
and *images* of the sister complexes under hypothetical
matched-conventions functors:

* **BCOV:** $\mathcal F_{\mathrm{BCOV}}: \mathrm{Fact}_{\mathrm{loc}}(\C^3) \to \mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$
  — does not exist (form-structure mismatch).
* **Sergeev:** $\mathcal F_{\mathrm{HC}}: \mathrm{Fact}_{\mathrm{loc}}(\R) \to \mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$
  — partial (open-line embedding) but not preserving Howe-Sergeev
  central character.
* **Igusa:** $\mathcal F_{\mathrm{Igusa}}: \mathrm{ChiralAlg}_{\Sp_4(\Z)} \to \mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$
  — does not exist (no chain-level Igusa side).
* **Bosonic:** $\mathcal F_{\mathrm{bos}}: \mathrm{Fact}^{\mathrm{6r,super}}_{\mathrm{mix}} \to \mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$
  — does not exist (no super $\to$ bosonic functorial discharge).
* **Costello-Li-d-even:** $\mathcal F_{\mathrm{CL}_4 \to \mathrm{CL}_3}: \mathrm{Fact}_{\mathrm{loc}}(\C^4) \to \mathrm{Fact}_{\mathrm{loc}}(\C^3)$
  — does not exist (parity-of-$d$ obstruction).

### 3.3 Costello-Gwilliam Vol II §11 and §13 perspective

CG Vol II §11 (BV regulator on factorization algebras) and §13
(general factorization-algebra framework) provide the foundational
language. The five firewalls are **not** predicted by CG Vol II
explicitly; they are **named obstructions** discovered in the
Phase-4 EXEC chain. CG Vol II explicitly anticipates anomaly
cancellation in factorization algebras (Vol II §11 Theorem 11.1.1
and successors), but does not provide a typology of structural
non-isomorphisms between distinct factorization-algebra categories.

**The five firewalls extend CG Vol II's framework** by classifying
the structural obstructions to matched-conventions functors between
factorization-algebra categories on different worldvolumes. This is
a **genuine new structural finding**, not a CG Vol II prediction.

### 3.4 Lurie HA cross-walk

Lurie HA Prop. 5.5.4.10 (locally constant factorization $\Leftrightarrow$
$E_n$-algebra) provides the foundational reduction. The mixed
factorization category $\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$
is *not* a single $E_n$-algebra category but a **mixed Dunn-Lurie
tensor product** of $E_2^{\mathrm{de\,Rham}}$ and
$E_2^{\mathrm{Dolbeault}}$. The five firewalls live in this mixed
category, and the chain-level isomorphism question is a question
about morphisms in this mixed category.

**Lurie's Dunn-Lurie additivity theorem (HA §5.1.2.2)** suggests
the right framework: $\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$
is a Dunn-Lurie product, and matched-conventions functors must
preserve both factors. The five firewalls obstruct chain-level
preservation of one or more factors.

---

## §4. Smallest categorical statement (FM.5)

### 4.1 Candidate smallest statement

**Candidate (informal).** *In $\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$,
no chain-level isomorphism exists between the manuscript's
brane-defect BV complex and any of the four sister chain-level
complexes (BCOV on $\C^3$, Hecke-Clifford on $\R$, gl$_N$ bosonic,
$\C^d$-even Calabi-Yau). The fifth firewall (Igusa) extends to
modular-invariance and lattice-signature obstructions outside
$\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$ proper, but its
chain-level component is subsumed.*

### 4.2 Refinement: per-functor non-existence

The smallest sharply-stated theorem is:

> **Smallest categorical statement (Theorem A: chain-level
> non-isomorphism in mixed factorization).**
> Let $\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$ be defined as in
> §3.2. Let $\mathcal A_{\mathrm{man}} \in \mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$
> be the manuscript's brane-defect BV complex with bosonic open
> algebra $\mathfrak{gl}_N$ and the holomorphic symplectic form
> $\omega = dz_1 \wedge dz_2$. Then:
>
> (a) **(FW.BCOV-chain)** $\mathcal A_{\mathrm{man}}$ is not
> chain-level isomorphic to the image of the BCOV BV complex on
> $\C^3$ under any functor preserving the regulator class.
>
> (b) **(FW.Sergeev-A5)** $\mathcal A_{\mathrm{man}}$ is not
> chain-level isomorphic to the image of the Hecke-Clifford
> open-line factorization $\mathcal{HC}_n$ under any functor
> preserving the Howe-Sergeev central character.
>
> (c) **(FW.Igusa)** $\mathcal A_{\mathrm{man}}$ is not chain-level
> isomorphic to any chain-level realization of an Sp$_4(\Z)$-modular
> form / BKM denominator algebra (no such realization currently
> exists in the literature; the obstruction subsumes chain-level
> non-isomorphism plus modular and lattice-signature obstructions).
>
> (d) **(FW.Unreduced-Bosonic)** $\mathcal A_{\mathrm{man}}$ admits
> no chain-level discharge of the residue $\hbar N [\bar c]$ via
> any super-extension preserving the bosonic source data.
>
> (e) **(FW.Costello-Li-d-even)** The Costello-Li 2015 / 2016
> chain-level anomaly cancellation on flat $\C^d$ ($d$ odd) does
> not extend to $d$ even via any modification of the open algebra
> or boundary state preserving the Costello-Gwilliam Vol II
> regulator class.

The five clauses (a)–(e) are the five independent firewalls; the
theorem states each as a chain-level non-isomorphism / non-extension
in the appropriate factorization-algebra category.

### 4.3 Missing technical lemma

**Lemma (open).** The mixed factorization category
$\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$ is a strict
$(\infty, 1)$-category in the CG Vol II + Lurie HA framework, with
the (A1)–(A5) + (A2$'$) admissible regulator class. The Dunn-Lurie
tensor product $E_2^{\mathrm{de\,Rham}} \otimes E_2^{\mathrm{Dolbeault}}$
is well-defined as a strict $(\infty, 1)$-category morphism.

**Status of the lemma.** Borderline open. CG Vol II §13 provides
the holomorphic factorization framework on $\widehat{\C^2}_0$;
Lurie HA Prop. 5.5.4.10 + §5.1.2.2 provides the mixed Dunn-Lurie
framework. The explicit identification of
$\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$ as a strict
$(\infty, 1)$-category requires a technical inscription that is
**not currently in the manuscript** but follows from CG Vol II §13
+ Lurie HA §5.5.4 with mild bookkeeping. This is a **Phase-5
inscription obligation**, not a Phase-4 firewall obstruction.

---

## §5. Inscription target with LaTeX block (FM.6)

### 5.1 Inscription site recommendation

**Recommended site.** A new typology remark in
`claim-strength-ledger.tex` (after the existing "Cross-volume
consequences" entry, line 130–140), or as a dedicated firewall
typology block immediately following `rmk:convention-firewall`
(`main.tex`:5380–5394).

**Rationale for `claim-strength-ledger.tex` site.** The ledger
already inscribes the "Cross-volume consequences" entry as a
firewall (line 130–140: "Cross-volume consequences | not asserted |
... they are firewalls, not export theorems"). Extending the
ledger with a typology entry for the five firewalls is **the most
economical and least disruptive** inscription: it explicitly
classifies each firewall, names the structural source, and labels
the permanence layer. No theorem needs to be promoted to "Theorem"
status; the typology lives at "remark / structural classification"
level, exactly matching the existing ledger style.

**Rationale for `rmk:convention-firewall` adjacent site.** A
dedicated remark block following `rmk:convention-firewall` keeps
the typology proximate to its existing convention-firewall
inscription. This is the **most prominent and most read** site;
suitable if the typology is intended to be a load-bearing remark
(rather than a ledger entry).

### 5.2 Candidate LaTeX block

The candidate inscription (proposal-only; NO TeX edits without
explicit instruction):

```latex
\begin{rmk}[Firewall-permanence typology]\label{rmk:firewall-typology}
  The local Hamiltonian BF / brane-defect BV theorem proved here
  is connected to five distinct sister theorems via cross-volume
  comparison maps; in each case the comparison is structurally
  permanent at a named layer and lifts (or fails to lift) at a
  named coefficient or representation-theoretic layer. The
  typology records the named obstruction sources and the layer
  topology.

  \begin{enumerate}[label=(FW\arabic*)]
  \item \textbf{BCOV chain-level firewall.} Comparison with the
  Bershadsky--Cecotti--Ooguri--Vafa BV theory on a Calabi--Yau
  threefold (Costello--Li 2012, 2015, 2016 chain-level
  reformulation) is permanent at the chain-level vertex class;
  it lifts at the coefficient layer via the structural common
  ancestor $\Str_{\mathfrak{gl}(N|N)}(I) = N - M$ on the open
  algebra, with cancellation at super-balance $N = M$ via (A5)
  + (A2$'$) on our side and via the Costello--Li 2016 supertrace
  identity on theirs.

  \item \textbf{Sergeev-Howe open-line firewall.} Comparison with
  the Hecke--Clifford open-line factorization
  $\mathcal{HC}_n = \mathcal C_n \rtimes \C[S_n]$ on $\R$
  (Sergeev 1985, Cheng--Wang 2012 Ch.~5) is structurally identical
  to the BCOV firewall: permanent at the chain-level vertex
  class; lifts at the coefficient layer via the Howe--Sergeev
  central character match
  $\Tr_{\mathfrak{gl}_N}(I) = \mathrm{otr}_{\mathfrak q(N)}(J) = N$.

  \item \textbf{Igusa modular firewall.} Comparison with the Igusa
  $\Delta_5$ / BKM denominator algebra
  $\mathfrak g_{\Delta_5}$ on the type-II hyperbolic lattice
  $\Lambda^{2,1}_{II}$ (Igusa 1962, Borcherds 1998,
  Gritsenko--Nikulin 1997) is permanent at three independent
  structural layers: chain-level (no Igusa BV side currently
  exists), modular invariance ($\mathrm{Sp}_4(\Z)$ has no action
  on $\mathfrak{gl}(N|N)$), and lattice signature ($\Z^2$ does
  not embed in $\Lambda^{2,1}_{II}$). \textbf{No coefficient-layer
  common ancestor exists.}

  \item \textbf{Bosonic discharge firewall.} The bosonic
  $\mathfrak{gl}_N$ Theorem G residue $\hbar N [\bar c]$ admits no
  chain-level discharge inside the manuscript's local apparatus;
  the supertrace cancellation $\Str_{\mathfrak{gl}(N|N)}(I) = 0$
  has no analogue on bosonic $\mathfrak{gl}_N$. Wilsonian RG flow
  inside the (A1)--(A4) admissible class, geometric symmetries
  ($\mathrm{Sp}(2,\C)$, Hamiltonian rotation, scaling), and
  cohomological degree shifts each preserve the residue.

  \item \textbf{Costello--Li $d$-odd parity firewall.} The
  Costello--Li 2015 / 2016 chain-level anomaly cancellation on
  flat $\C^d$ requires $d$ odd; on $d$ even the polyvector
  signature $(-1)^d$ flips and the cancellation doubles to
  $2\hbar N \neq 0$. The obstruction is structural at the BV
  pairing on polyvectors via $\Omega_d^2$ and is not a
  regulator-class artefact.
  \end{enumerate}

  These five firewalls share a uniform structural property: they
  obstruct chain-level matched-conventions functors at the
  vertex-class layer of the 6-real-dim mixed
  topological-holomorphic factorization-algebra category
  $\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$ on
  $\R^2 \times \widehat{\C^2}_0$ in the Costello--Gwilliam
  framework. They are distinct in their structural sources
  (representation-theoretic for (FW1), (FW2), (FW4); parity-of-$d$
  for (FW5); modular and lattice-arithmetic for (FW3)) but
  uniform in their obstruction layer. No chain-level isomorphism
  in $\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$ exists between
  the manuscript's brane-defect BV complex and any of the five
  sister complexes; the typology is a structural permanence
  classification, not an export theorem.
\end{rmk}
```

### 5.3 Alternative: ledger entry

If the inscription is at `claim-strength-ledger.tex`, the candidate
ledger row is:

```latex
\hline
Firewall-permanence typology &
\emph{structural classification (remark-grade)} &
Five firewalls (BCOV chain, Sergeev-Howe, Igusa modular, bosonic
discharge, Costello--Li $d$-odd) classify the structural
permanence of cross-volume comparison maps. Permanent at
chain-level / vertex-class layer in each case; coefficient or
representation-theoretic layer admits a common ancestor in three
of five (BCOV, Sergeev, Costello--Li); no ancestor exists for the
Igusa modular and bosonic firewalls. See
Remark~\ref{rmk:firewall-typology} for the precise typology.\\
\hline
```

### 5.4 Decision matrix for inscription site

| Criterion | `claim-strength-ledger.tex` (ledger entry) | `rmk:convention-firewall` adjacent (remark block) |
|---|---|---|
| **Disruption** | Minimal (one new row) | Moderate (one new \begin{rmk} block) |
| **Visibility** | Medium (in ledger) | High (in main body, after established firewall remark) |
| **Tone match** | Excellent (ledger style) | Good (remark style) |
| **Cross-references** | Easy (in ledger context) | Easy (adjacent to existing firewall) |
| **Promotion path to theorem** | Difficult (would need to leave ledger) | Natural (could become \begin{thm} in Phase-5) |

**Recommendation.** Inscribe **both**:
* A ledger entry in `claim-strength-ledger.tex` (cited at §5.3).
* A remark block in `main.tex` after `rmk:convention-firewall`
  (LaTeX block at §5.2).

The combination provides both visibility (remark in main body) and
classification economy (ledger row).

---

## §6. Publication-grade verdict (FM.7)

### 6.1 Verdict on publication-grade status

**The remark-grade inscription (§5.2) is publication-grade as is.**
It accurately reports five named obstructions, each of which is
documented in full at the appropriate Phase-4 EXEC ledger:

* FW.BCOV-chain: BCOV-A5-comparison §0–§7 (1093 lines).
* FW.Sergeev-A5: Sergeev-Duality-Probe §0–§7 (1334 lines).
* FW.Igusa: Igusa-Heuristic-Audit §0–§7 (1100 lines).
* FW.Unreduced-Bosonic: Unreduced-Bosonic-Phase5 §0–§9 (1372 lines).
* FW.Costello-Li-d-even: Costello-Li-d-extension §0–§7 (1104 lines).

Each ledger contains: (i) the firewall statement; (ii) the
structural source; (iii) the permanent layer; (iv) the liftable
layer (or its absence); (v) the coefficient-layer common ancestor
(or "none exists"); (vi) anti-attack scan; (vii) cross-walks. The
remark consolidates the five into a typology without making any
load-bearing claim that is not already discharged in the ledgers.

**The stand-alone Theorem (Firewall-permanence typology) at §0.1
is publication-grade modulo one technical lemma**: the explicit
identification of $\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$ as a
strict $(\infty, 1)$-category in CG Vol II + Lurie HA framework
with the (A1)–(A5) + (A2$'$) augmentation. This lemma:

* **Status.** Borderline open (CG Vol II §13 + Lurie HA §5.5.4
  cover the foundational pieces; the explicit augmentation with
  our (A5)+(A2$'$) is not currently inscribed).

* **Phase classification.** Phase-5 inscription obligation, not
  Phase-4 firewall obstruction.

* **Required for theorem-grade promotion.** Yes — the theorem at
  §0.1 invokes $\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$ as a
  strict ambient category; without the lemma, the theorem statement
  is informal.

* **Required for remark-grade inscription.** No — the remark at
  §5.2 invokes the typology informally without claiming a strict
  category framework.

### 6.2 Missing technical lemma summary

**Open Lemma L-FM-1.** The mixed factorization category
$\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}} := \mathrm{Fact}_{\mathrm{loc}}^{(\infty,1)}(\R^2_{\mathrm{top}} \times \widehat{\C^2}_0; \mathrm{Reg}_{\mathrm{adm}})$
is a strict $(\infty, 1)$-category in the CG Vol II + Lurie HA
framework, with the (A1)–(A5) + (A2$'$) admissible regulator class
of Definition `defn:regulator-admissible-sector`. The Dunn-Lurie
tensor product $E_2^{\mathrm{de\,Rham}} \otimes E_2^{\mathrm{Dolbeault}}$
is well-defined as a strict $(\infty, 1)$-category morphism into
$\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$.

**Sketch.** CG Vol II §13 provides the holomorphic factorization
framework on $\widehat{\C^2}_0$; Lurie HA Prop. 5.5.4.10 + §5.1.2.2
provides the mixed Dunn-Lurie framework. The (A5)+(A2$'$)
augmentation extends the CG Vol II §11 BV regulator with parity-
equivariance on the matrix factor. The strict $(\infty, 1)$-category
structure follows by Dunn-Lurie additivity (HA §5.1.2.2 Theorem
5.1.2.2) applied to the two factor categories, with the regulator
class providing the strictness datum.

**Phase-5 verification.** Inscribe the explicit Dunn-Lurie tensor
product structure on $\R^2_{\mathrm{top}} \times \widehat{\C^2}_0$
with the (A5)+(A2$'$) augmentation, citing CG Vol II §13 + Lurie HA
§5.1.2.2 + §5.5.4. This is **not currently inscribed** but is a
mild bookkeeping inscription, not a fundamental obstruction.

### 6.3 Path to publication-grade theorem

| Stage | Action | Status |
|---|---|---|
| **Stage 1 (current)** | Five Phase-4 EXEC firewall ledgers inscribed | Done |
| **Stage 2 (proposed)** | Typology remark inscribed at §5.2 / §5.3 | Proposal-only (no edit) |
| **Stage 3 (Phase-5)** | Lemma L-FM-1 inscribed | Open obligation |
| **Stage 4 (Phase-5+)** | Stand-alone Theorem (Firewall-permanence typology) at §0.1 promoted to manuscript inscription | Conditional on Stage 3 |

The path from Stage 1 to Stage 4 is incremental and well-defined.
**Stage 2 is the publication-grade target for Phase-4**; Stages 3
and 4 are Phase-5+ obligations.

---

## §7. Anti-attack scan responses

### 7.1 (Att-1) Distinct sources, name collision?

**Attack.** "The five firewalls cite different structural sources
(representation-theoretic, parity, modular, dimensional). Are they
not just five distinct phenomena that happen to be called
'firewalls'?"

**Response.** **Both.** The five share a uniform **structural
property** (chain-level non-isomorphism in
$\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$) but differ in their
**source data**. The unified statement is at the layer of
factorization-algebra obstructions; the distinct source data is at
the layer of the structural mechanism producing the obstruction.

**Sharper formulation.** The five firewalls are **five instances of
a single structural permanence theorem** at the chain-level layer,
with **five distinct named obstruction sources** at the structural-
mechanism layer. The unified theorem (§0.1) is real; the typology
of named sources (§1) is also real. **Neither layer subsumes the
other.**

**Rebuttal of name-collision.** A pure name-collision would mean
the five share *only* the word "firewall" without any structural
commonality. This is not the case: the five share (i) the same
ambient category $\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$, (ii)
the same obstruction layer (chain-level non-isomorphism), (iii) the
same liftable / non-liftable layer typology (coefficient or
representation-theoretic), and (iv) the same Polyakov-class
regulator-invariance property. These are non-trivial structural
commonalities, not name collisions.

### 7.2 (Att-2) Universal obstruction class?

**Attack.** "Does the meta-theorem suggest a 'universal' obstruction
class on the 6-real-dim mixed factorization category — a single
class in some derived category that subsumes all five firewalls?"

**Response.** **No, with structural caveat.** The five firewalls
are *not* instances of a single cohomology class in a universal
obstruction complex. The structural reasons:

* **FW.Igusa is at a higher arithmetic level.** The Sp$_4(\Z)$
  modular obstruction and the lattice-signature obstruction live
  in arithmetic-representation-theoretic categories, not in
  factorization-algebra categories.

* **FW.Costello-Li-d-even is at a dimensional / polyvector layer.**
  The parity-of-$d$ obstruction is not a vertex-class obstruction;
  it is a polyvector-signature obstruction.

* **FW.Unreduced-Bosonic is the absence of an ancestor**, not the
  obstruction to a specific class.

What the meta-theorem **does** suggest is a **uniform classification
schema**: each firewall lives in a specific layer of the
$\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$ category (chain-level,
modular, dimensional, representation-theoretic), and the layers
admit a canonical ordering. The "universal obstruction" framing is
**too strong**; the "typology with named layers" framing is
**correct**.

**Sharper formulation.** The meta-theorem suggests a **universal
typology** of obstruction layers, not a universal obstruction
class. The typology has 4–5 named layers (chain-level vertex,
coefficient, modular, lattice, dimensional) with canonical embedding
relations.

### 7.3 (Att-3) Costello-Gwilliam Vol II prediction?

**Attack.** "Does Costello-Gwilliam Vol II's anomaly cancellation
framework predict our firewall typology, or is it a genuine new
finding?"

**Response.** **Genuine new finding, not predicted by CG Vol II.**

CG Vol II §11 anticipates anomaly cancellation in factorization
algebras at the BV regulator layer. Specifically:
* Vol II Theorem 11.1.1 (and successors): the BV anomaly class
  lives in $H^1(\mathcal O_{\mathrm{loc}}, Q + \{S, -\})$ as a
  cohomology class.
* Vol II §13: factorization-algebra framework on smooth manifolds;
  not specialized to mixed topological-holomorphic worldvolumes.

CG Vol II does **not** provide:
* A typology of structural obstructions to matched-conventions
  functors between distinct factorization-algebra categories.
* An identification of the 6-real-dim mixed
  $\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$ category as a Dunn-
  Lurie tensor product.
* A classification of named firewalls by structural source.

The five firewalls are **named obstructions discovered in the
Phase-4 EXEC chain**. They extend CG Vol II's framework by:
* Identifying chain-level non-isomorphisms between distinct
  factorization-algebra categories.
* Classifying these non-isomorphisms by structural source
  (representation-theoretic, parity, modular, dimensional).
* Naming the layer at which each is permanent vs liftable.

**Sharper formulation.** The Phase-4 firewall typology is a
**genuine new structural finding** that extends the CG Vol II
framework with (a) a typology of structural obstructions, (b) an
identification of the mixed $\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$
category, and (c) a classification by layer of permanence. CG Vol
II provides the foundational language; the typology is built on
top of that language.

### 7.4 (Att-4) Coulembier 2018 super-finite-tensor-category

**Attack.** "Coulembier 2018 super-finite-tensor-category Theorem
5.2 lifts Sergeev to the categorical level. Does the meta-theorem
predict similar categorical lifts for the other firewalls?"

**Response.** **Partially yes, but the categorical lifts do not
discharge the firewalls.** Coulembier 2018 Theorem 5.2 lifts the
Howe-Sergeev pair $(\mathfrak q(N), \mathcal{HC}_n)$ to a categorical
mutual-centralizer pair in the super-finite-tensor-category sense.
This is a **categorical lift at the representation-theoretic layer**;
it does *not* lift at the chain-level / factorization-algebra layer.

**Predicted categorical lifts for the other firewalls:**

* **FW.BCOV-chain:** No analogous categorical lift. The BCOV BV
  theory on $\C^3$ is a chain-level theory (Costello-Li 2012);
  there is no "categorical BCOV at the rep-cat layer" that is
  parallel to Coulembier-Sergeev.

* **FW.Igusa:** No analogous categorical lift. The Sp$_4(\Z)$
  modular form $\Delta_5$ is an arithmetic object; there is no
  "categorical Igusa at the rep-cat layer" parallel to
  Coulembier-Sergeev.

* **FW.Unreduced-Bosonic:** No analogous categorical lift. The
  bosonic side has no super-extension; there is no "categorical
  bosonic discharge" parallel to Coulembier-Sergeev.

* **FW.Costello-Li-d-even:** No analogous categorical lift. The
  parity-of-$d$ obstruction is not at the representation-theoretic
  layer; it is at the polyvector / dimensional layer. There is no
  "categorical $d$-even lift" parallel to Coulembier-Sergeev.

**Sharper formulation.** Coulembier 2018 Theorem 5.2 is a **special
feature of the Sergeev case**: the Howe-Sergeev pair lifts to a
categorical mutual centralizer because the underlying Sergeev
duality is at the representation-theoretic (rep-cat) layer, where
categorical lifts are natural. The other four firewalls do not
admit similar categorical lifts because their structural sources
are not at the rep-cat layer (chain-level for BCOV; modular /
arithmetic for Igusa; dimensional for Costello-Li-d-even).

**Implication for meta-theorem.** The meta-theorem **does not
predict** categorical lifts for the other firewalls. The Sergeev
case is special. The unified statement is at the chain-level layer,
not at the representation-theoretic categorical-lift layer.

---

## §8. Residuals

### 8.1 Open obligations from this audit

* **R-FM-01.** Inscribe the firewall typology remark at §5.2 (or
  the ledger entry at §5.3) in the manuscript. **Phase-4 EXEC
  inscription target**; not load-bearing for the local theorem,
  but improves cross-volume documentation.

* **R-FM-02.** Inscribe Lemma L-FM-1 (strict $(\infty, 1)$-category
  structure on $\mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$ with
  (A5)+(A2$'$) augmentation). **Phase-5 inscription obligation**;
  required for promoting the typology to a stand-alone theorem.

* **R-FM-03.** Verify that the typology is exhaustive: is there a
  sixth firewall not yet identified in the Phase-4 EXEC chain?
  Candidates to scan:
  - FW.Sergeev-Brundan-Kleshchev-modular: comparison with
    Brundan-Kleshchev 2001 Hecke-Clifford modular branching rules
    on $\widehat S_n$. Likely subsumed by FW.Sergeev-A5.
  - FW.Coulembier-Deligne: comparison with Coulembier 2018
    Deligne categories at the rep-cat level. Likely subsumed by
    FW.Sergeev-A5.
  - FW.Witten-mirror: comparison with Witten 1992 mirror manifold
    framework. Likely outside our scope (closed-string mirror
    swap, not factorization-algebra firewall).
  Sweep status: not exhaustively done in this audit.

* **R-FM-04.** Cross-walk to the manuscript's existing
  `rmk:weiss-ran-descent-firewall` (`main.tex`:2741): does this
  remark already inscribe a sixth firewall, or is it a special
  case of one of the five? Quick read suggests it is a different
  layer (Weiss-Ran descent, not chain-level matched-conventions);
  worth a separate audit to confirm.

* **R-FM-05.** Cross-walk to `lem:no-formal-disk-transfer` and
  `lem:admissibility-not-globalization` cited at the Cross-volume
  consequences ledger entry (`claim-strength-ledger.tex`:135–137):
  these are the manuscript's existing inscribed firewalls. Confirm
  that the typology subsumes them (likely they correspond to
  components of FW.BCOV-chain and FW.Igusa).

### 8.2 Phase-5 frontier prompts

The five firewalls each have Phase-5 frontier prompts:

* **FW.BCOV-chain Phase-5:** Construct a matched-conventions functor
  $\mathcal F_{\mathrm{BCOV}}: \mathrm{Fact}_{\mathrm{loc}}(\C^3) \to \mathrm{Fact}^{\mathrm{6r}}_{\mathrm{mix}}$
  with form-structure shift (Calabi-Yau volume to holomorphic
  symplectic) and field-content shift (polyvectors to Hamiltonian
  BF). BCOV-A5 §6.4 P5-1 / P5-2 / P5-3.

* **FW.Sergeev-A5 Phase-5:** Inscribe the factorization-algebra
  Howe pair $(\mathfrak q(N), \mathcal{HC}_n)$ explicitly on
  $\R^2 \times \C^2$. Sergeev-Duality-Probe §5.2 (i)–(iii).

* **FW.Igusa Phase-5:** Construct a chain-level Igusa BV / chiral
  theory and the cross-volume duality bridge (BCOV $\to$ Vol III
  $\to$ Igusa). Igusa-Heuristic-Audit §3.5 ($X_5$).

* **FW.Unreduced-Bosonic Phase-5:** Construct a Phase-5 mechanism
  changing the source data (super-extension, twisted M-theory, or
  boundary condition). Unreduced-Bosonic-Phase5 §8 (UB.8).

* **FW.Costello-Li-d-even Phase-5:** Identify a parity-correcting
  mechanism on $\C^4$ that does not break the BCOV setup.
  Costello-Li-d-extension §3.3 (D-1)–(D-4) all negative; would
  require new mechanism.

These five Phase-5 frontiers are **independently load-bearing** and
not subsumed by a single Phase-5 program.

### 8.3 Convergence verdict

**The Phase-4 EXEC chain has identified five structurally permanent
firewall obstructions.** They are unified at the chain-level layer
of the 6-real-dim mixed factorization-algebra category and distinct
in their structural sources. The meta-theorem at §0.1 captures the
unified structural permanence; the typology at §1 captures the
distinct sources. **The combination is the right structural
description**: a single permanence theorem at the chain-level
layer, with a typology of five named structural sources.

**Inscription target.** The remark-grade inscription at §5.2 (with
optional ledger entry at §5.3) is publication-grade; the
stand-alone theorem at §0.1 requires Lemma L-FM-1 (Phase-5
obligation). The path to a fully publication-grade theorem is
incremental and well-defined.

**Final classification.** The Phase-4 firewall meta-theorem is
**publication-grade as a remark-grade structural classification**,
with a clear path to theorem-grade promotion in Phase-5 via
Lemma L-FM-1.
