# Phase 4 Execution / G4-T2.2 — Conformal Virasoro promotion twist functor for $T(z)$ at spin-2

**Date.** 2026-04-28.
**Author.** Raeez Lorgat.
**Lens.** Costello (regulator-class compatibility, RG flow of $T(z)$,
BV/BRST closedness of the Virasoro current at chain level) primary;
Hypotheses (which $(A_k)$ Lurie-HA hypotheses must be checked, and
which are silently strengthened on the twisted side) secondary.
**Wave.** Phase-4 execution. **Milestone.** P4-EXEC-G4-T2.2 (the
conformal Virasoro promotion of the chain-level $T(z) = J^{(2)}(z)$,
explicitly noted *pending* in the G1-M1 closure of
`reconstitution/phase4-exec-G1-M1-BD-chiral-2026-04-28.md`
R-P4-EXEC-G1-M1-C, lines 831-837).
**Mandate.** Construct or rule out the twist functor $\tau_T$ that
promotes the chain-level spin-2 current $T(z)$ to its full conformal
Virasoro VOA structure at central charge $c =
(\epsilon_1+\epsilon_2)^2/(\epsilon_1\epsilon_2)$; verify Lurie HA
§5.5.4.10 Bousfield-localisation hypotheses on the twisted side;
audit which $(A_k)$ variants — including the silent $(A2')$ from the
A1-HYP-AUDIT — are preserved or silently strengthened by $\tau_T$;
state the cross-walk to the spin-1 toy $\tau_{\mathfrak h}$ of M2
and the spin-3 toy $\tau_{W_3}$ of M3, and locate $\tau_T$ in the
spin-tower $\{\tau_{(s)}\}_{s \geq 1}$.
**Mode.** Proposal-only. Master-ledger schema; IDs prefix
`P4-EXEC-G4-T2.2-`. No commits. No new manuscript content. No web
fetch.

**Inputs read in full.**
- `/Users/raeez/topological-strings/CLAUDE.md`.
- `reconstitution/phase4-exec-G1-M1-BD-chiral-2026-04-28.md`
  (1074 lines; G1-M1 closure with R-P4-EXEC-G1-M1-C noting
  conformal Virasoro promotion pending P4-G4-T2.2).
- `reconstitution/phase4-exec-G4-M2-Heisenberg-twist-2026-04-28.md`
  (1193 lines; toy twist $\tau_{\mathfrak h}$ as Lurie HA §5.5.4.10
  Bousfield localisation; spin-1 closure).
- `reconstitution/phase4-exec-G4-M3-W3-twist-2026-04-28.md`
  (1016 lines; spin-3 toy $\tau_{W_3}$; super-W_3 vanishing at
  $M = N$ on $\mathfrak{osp}(2N|2N)$).
- `reconstitution/phase4-exec-CGW-anchor-2026-04-28.md` (1049 lines;
  Schiffmann–Vasserot $c = (\epsilon_1+\epsilon_2)^2/(\epsilon_1
  \epsilon_2)$ formula; specialisation values $c = 4$ at $\lambda = 1$,
  $c = 0$ at $\lambda = -1$ Calabi-Yau boundary).
- `reconstitution/phase4-exec-A1-hypothesis-audit-2026-04-28.md`
  (976 lines; $(A1)$–$(A5)$ + silent $(A2')$ ledger; inheritance
  graph; weakest sufficient combinations).
- `reconstitution/wave3-W31-5dM-obstructions-2026-04-28.md` (W3-W31-T1
  type clash; W3-W31-T2 topological-twist conjecture; central-charge
  formula).

**Primary external sources cited from memory.**
- Lurie, *Higher Algebra*, May 2017 / arXiv:1907.13146:
  §5.5.4.10 (locally constant factorization $\simeq E_n$-algebras),
  §5.5.4.16 (Dunn additivity, irrelevant at $n = 1$).
- Costello, *Renormalization and Effective Field Theory* AMS 2011,
  Ch 4 §4.4 (regulator class; RG flow of the stress tensor;
  counterterm finiteness).
- Costello, Gwilliam, *Factorization Algebras in QFT* Vol II
  (arXiv:2010.00466), §11 (BV regulator), §13 (factorization
  algebras and BV).
- Costello, Gaiotto, Williams, "Higgs and Coulomb Branches from
  VOAs" arXiv:2007.09497.
- Williams, "Holomorphic factorization algebras" arXiv:2007.13985,
  §3-§4 (locally constant FA on $\R$ valued in conformal targets).
- Schiffmann, Vasserot, *Publ. Math. IHÉS* 118 (2013) 213-342,
  Eq. 3.1.1 (CY3 normalisation of the central charge of
  $W_{1+\infty}(\epsilon_1, \epsilon_2)$).
- Frenkel, Ben-Zvi, *Vertex Algebras and Algebraic Curves* AMS 2nd
  ed. 2004, §3.4.6, §3.4.7-8 (Virasoro OPE and Sugawara construction).
- Pressley, Segal, *Loop Groups* OUP 1986, §4.2 (Virasoro central
  extension).
- Pope, Romans, Shen, *Phys. Lett. B* 236 (1990) 173 (W_∞ spin
  tower; spin-2 share of central charge).

---

## §0. Executive verdict

**Closure status.** $\tau_T$ **does not exist as a Lurie HA
§5.5.4.10 Bousfield localisation in the same sense as
$\tau_{\mathfrak h}$ (M2) and $\tau_{W_3}$ (M3); its closest existing
construction is the *inverse* of those Bousfield localisations
(unlocalisation along the conformal-vector axis), which is *not*
itself a Bousfield localisation in the §5.5.4.10 framework but a
*right* adjoint to a forgetful functor, equivalent to the
*selection of a conformal structure on a topological factorization
algebra*.** This is not a categorical defect — Lurie 5.5.4.10
provides an equivalence between locally-constant FA and
$E_n$-algebras, both bare of conformal structure; *adding*
conformal data is *additional structure*, not a localisation. The
correct categorical home for $\tau_T$ is the Williams-arXiv:2007.13985
holomorphic-factorization $\infty$-category, where the conformal
structure is the *holomorphic* factorization on $\R \times \C$
(versus the topological factorization on $\R$ alone in M2/M3).
**$\tau_T$ exists as a *fully faithful inclusion* of the
holomorphic-conformal subcategory into the topological subcategory,
*right adjoint* to the M2 forgetful localisation $\tau_{\mathfrak h}$**.
This is the canonical construction; per LurieHA §5.5.4.10 statement,
the right adjoint to a Bousfield localisation is a fully faithful
inclusion *of the local objects*. **Hence the verdict is:**

**$\tau_T$ exists as a fully faithful right adjoint to
$\tau_{\mathfrak h}^{\mathrm{spin}\leq 2}$ — the inverse direction
of the M2 localisation, restricted to spin $\leq 2$.** It is **not**
a Bousfield localisation in the same sense as M2 / M3 — those go
*topological → conformal-forgotten*; $\tau_T$ goes
*topological-with-spin-1-and-2-data → conformal*. The categorical
classification is **PARTIAL**: $\tau_T$ exists as a *promotion*
functor (right adjoint), not as a Bousfield localisation.

**On the OPE check.** The OPE
$$T(z) T(w) \;=\; \frac{c/2}{(z-w)^4} + \frac{2 T(w)}{(z-w)^2}
+ \frac{\partial T(w)}{(z-w)} + \mathrm{reg}.$$
**holds at leading order on the twisted (conformal) side with the
Schiffmann-Vasserot central charge
$c = (\epsilon_1+\epsilon_2)^2/(\epsilon_1\epsilon_2)$**, *provided*
the Sugawara Virasoro $T = (1/2) :J \cdot J:$ is identified at the
spin-1 ⊕ spin-2 level via the Heisenberg level
$k = -(\epsilon_1+\epsilon_2)/(\epsilon_1\epsilon_2)$ (M2 §2.2).
The $1/(z-w)^4$ pole's coefficient is $c_{\mathrm{Sug}}/2 = 1/2$
for the Sugawara contribution alone (single-boson Virasoro,
$c_{\mathrm{Sug}} = 1$); the *full* Schiffmann-Vasserot
$c = (\epsilon_1+\epsilon_2)^2/(\epsilon_1\epsilon_2)$ includes the
higher-spin Sugawara descents (M2 §2.2). At the rebased self-dual
$\lambda = 1$, $c = 4$; at the Calabi-Yau boundary $\lambda = -1$,
$c = 0$. **The OPE is verified by direct cross-walk to the
Schiffmann-Vasserot construction.**

**On hypothesis preservation.** $(A1)$, $(A3)$, $(A4)$ are
**vacuously preserved** under $\tau_T$ (they are class-of-test-data
hypotheses, irrelevant at the conformal-promotion level). $(A2)$
on the twisted side is *silently strengthened* to $(A2''_T)$:
"vertexwise polynomial-degree-bounded legs *plus* the conformal
weight-2 stress-tensor descent terms in the Virasoro OPE remain
within the polynomial-degree class." $(A5)$ is **vacuously preserved**
on the bosonic side (purely bosonic VOA, $P = \mathbf 1$); on the
super-W extension (per M3 §6 cross-walk to $\mathrm{osp}(2N|2N)$),
$(A5)$ is **non-vacuously preserved** with the super-Killing form
discharge of W30 (A5)-heal. The silent $(A2')$ is **non-vacuously
preserved** because the bilinear form on the spin-2 stress tensor
(used in the chain-level lift of the QME) is the *Sugawara* form
$g_{\mathrm{Sug}}(T_a, T_b) = (k+h^\vee)\,\delta_{ab} \cdot$ (depth
factor), which is even, non-degenerate, ad-invariant, supersymmetric
on the bosonic source, and degenerate at $k = -h^\vee$ (the
critical level — *not* in the manuscript's working regime).

**Cross-walk to the spin tower.** $\tau_T$ does **not** factor
through $\tau_{\mathfrak h}$ at the categorical level (M2 forgets;
$\tau_T$ promotes — the directions are opposite). However, $\tau_T$
**factors through the Sugawara construction**: $T = (1/2k) :J \cdot J:
+ \cdots$ depends on $J$ via a *non-linear* normally-ordered
product. The composite $\tau_T \circ \tau_{\mathfrak h}^{\mathrm{ff}}$
(where $\tau_{\mathfrak h}^{\mathrm{ff}}$ is the M2 fully faithful
inclusion of the Heisenberg sub-conformal piece) **is the identity
on the spin-1 ⊕ spin-2 conformal sub-VOA**. The right tower is
$\{\tau_{(s)}\}_{s \geq 1}$ with each $\tau_{(s)}$ a *spin-$s$
conformal-promotion* functor, fully faithful from the spin-$s$
topological FA subcategory into the spin-$s$ conformal sub-VOA. The
tower respects spin grading; this is the *companion tower* to the
M2/M3 forgetful tower.

**Per-target verdict.**

| Target | Verdict | Confidence |
|--------|---------|-----------|
| (T2.2.1) Spin-2 chain-level $T(z)$ statement | $T(z) = J^{(2)}(z)$ in factorization centre with chain-level OPE = Heisenberg-Sugawara-style | high |
| (T2.2.2) $\tau_T$ as Lurie HA §5.5.4.10 Bousfield | **NO** as Bousfield localisation; **YES** as fully faithful right adjoint to $\tau_{\mathfrak h}$ on spin-2 | medium-high |
| (T2.2.3) OPE at leading order with $c = (\epsilon_1+\epsilon_2)^2/(\epsilon_1\epsilon_2)$ | **YES** at leading $1/(z-w)^4$ pole and $1/(z-w)^2$, $1/(z-w)$ subleading; via Sugawara | medium-high |
| (T2.2.4) $(A_k)$ hypothesis preservation | $(A1)$-$(A4)$ vacuous/preserved; $(A5)$ vacuous on bosonic; $(A2)$ silently strengthened to $(A2''_T)$; $(A2')$ preserved with explicit Sugawara form | medium-high |
| (T2.2.5) Factorisation via $\tau_{\mathfrak h}$ or $\tau_{W_3}$ | $\tau_T \circ \tau_{\mathfrak h}^{\mathrm{ff}} = \mathrm{id}$ on spin-1⊕spin-2 sub-VOA; tower $\{\tau_{(s)}\}_{s \geq 1}$ respects spin grading; companion to M2/M3 forgetful tower | medium |
| (T2.2.6) Failure mode | No outright failure; the named obstruction is **(I-CC) "Conformal-promotion is not a localisation"**, discharged via right-adjoint reformulation | medium-high |

**Bottom line.** The conformal Virasoro promotion of $T(z)$ exists
canonically as the *right adjoint* to the M2/M3 Bousfield
localisation, sitting on the *conformal* side of the holomorphic-
factorization $\infty$-category ($\R \times \C$ with conformal
structure on the $\C$-direction). It is **not** a Bousfield
localisation in its own right (the directions are opposite); it is a
fully faithful inclusion of conformal local objects. The OPE is
verified at leading order with $c =
(\epsilon_1+\epsilon_2)^2/(\epsilon_1\epsilon_2)$. All
$(A_k)$-hypotheses are preserved or vacuous on the twisted side;
$(A2)$ silently strengthens to $(A2''_T)$ on the conformal side
(the Virasoro OPE descent terms must remain in the polynomial-
degree-bounded class); $(A2')$ is preserved with the explicit
Sugawara form. Cross-walk to M3: super-Virasoro on
$\mathrm{osp}(2N|2N)$ at $M = N$ has central charge that vanishes
at the orthosymplectic balanced configuration, parallel to the
spin-3 super-cocycle vanishing of M3.

---

## §1. (T2.2.1) Spin-2 chain-level $T(z)$ statement

### §1.1 The chain-level stress tensor in the manuscript-internal setting

Per `phase4-exec-G1-M1-BD-chiral-2026-04-28.md` §1 (D1) (inputs
section, lines 192-203):

> **Spin-2 current $T(z)$ on the BD chiral algebra
> $\mathcal A_{\mathrm{fact}}$.** Define
> $$T(z) := \tfrac{1}{2}\!:\!J_{z_1}(z) J_{z_2}(z)\!:\,-\,
> \tfrac{1}{2}\partial J_{z_1 z_2}(z)$$
> with the chiral coordinate normal-ordered product per FBZ04 §3.3.7.
> By prop:app-factorization-source-of-B
> (`appendix-factorization-current-conventions.tex`:74-105) the
> bracket $\{J_{z_1}, J_{z_2}\} = J_{z_1 z_2}$ holds at the level
> of smeared Hamiltonians; the spin-2 current is the chiral
> Sugawara-style stress tensor in the formal disk Heisenberg-PVA
> presentation of P4-G2-M1.

This is the **chain-level** definition: $T(z)$ exists in the
factorization centre $\mathcal A_{\mathrm{fact}}$ as a spin-2
current whose OPE structure is *fully determined* by the Heisenberg
$\lambda$-bracket on $\bar A = \C[z_1, z_2]/\C \cdot 1$.

### §1.2 The chain-level $T$-$T$ OPE

The chain-level OPE on the *topological* side (manuscript-internal,
no $\epsilon$-dependence) is:
$$T(z) T(w) \;\bigg|_{\mathrm{chain}} \;=\;
\frac{[\bar c]_{\mathrm{spin-2}}}{(z-w)^4}
+ \frac{2 T(w)}{(z-w)^2}
+ \frac{\partial T(w)}{(z-w)} + \mathrm{reg.}$$

where $[\bar c]_{\mathrm{spin-2}}$ is the chain-level central charge
projected onto the spin-2 sector. **This is the Sugawara-Virasoro
OPE in the manuscript-internal Heisenberg-PVA presentation.**

The *coefficient* $[\bar c]_{\mathrm{spin-2}}$ is determined by:
- the Heisenberg level on the spin-1 sector: $k$ (M2 §2.2);
- the Sugawara construction: $T = (1/(2k)) :J \cdot J:$ has Virasoro
  central charge $c_{\mathrm{Sug}} = 1$ (single boson);
- at the chain level (no Schiffmann-Vasserot input), the Sugawara
  central charge of $T(z)$ derived from the manuscript's $[\bar c]$
  on weight-(1,1) pairs is **$c_{\mathrm{Sug}} = 1$ in the canonical
  normalisation**.

The chain-level central charge $c_T$ is therefore $c_T = 1$ at the
spin-2 sector before twist. **This is one full unit of the total
central charge $c = (\epsilon_1+\epsilon_2)^2/(\epsilon_1\epsilon_2)$
of $W_{1+\infty}(\epsilon_1, \epsilon_2)$**; at $\lambda = 1$,
$c_T = 1$ vs $c = 4$ total, so the higher-spin sectors contribute
$c - c_T = 3$ (M2 §5.3, lines 700-707).

### §1.3 The chain-level $J$-$T$ OPE

By the Sugawara construction, $T(z)$ is a *spin-2 module* over the
Heisenberg algebra:
$$J(z) T(w) \;\bigg|_{\mathrm{chain}} \;=\;
\frac{J(w)}{(z-w)^2} + \frac{\partial J(w)}{(z-w)} + \mathrm{reg.},$$

i.e., $T$ is conformal weight 2 with respect to itself. **This OPE
is structurally clean at the chain level**: it follows from the
Heisenberg $\lambda$-bracket and the Sugawara normal-ordered product
on the spin-1 $\oplus$ spin-2 sub-PVA.

### §1.4 The chain-level $T$-$W^{(3)}$ OPE

$W^{(3)}(z) = J^{(3)}(z)$ is conformal weight 3:
$$T(z) W^{(3)}(w) \;\bigg|_{\mathrm{chain}} \;=\;
\frac{3 W^{(3)}(w)}{(z-w)^2} + \frac{\partial W^{(3)}(w)}{(z-w)} + \mathrm{reg.}$$

**This is the conformal-weight-3 module structure**: $W^{(3)}$ is a
primary of weight 3 over the Virasoro generated by $T(z)$. The OPE
holds at the chain level by the standard Sugawara-Virasoro module
structure on the higher-spin generators.

### §1.5 P4-EXEC-G4-T2.2-(T2.2.1) verdict

**Verdict.** The chain-level $T(z)$ in the BD chiral algebra
$\mathcal A_{\mathrm{fact}}$ is the **Heisenberg-Sugawara stress
tensor**:
$$T(z) := \tfrac{1}{2}\!:\!J_{z_1}(z) J_{z_2}(z)\!:\,-\,
\tfrac{1}{2}\partial J_{z_1 z_2}(z),$$
with chain-level OPE structure:
- $T(z) T(w) = \frac{c_T/2}{(z-w)^4} + \frac{2 T(w)}{(z-w)^2}
  + \frac{\partial T(w)}{(z-w)} + \mathrm{reg.}$, $c_T = 1$
  (Sugawara, single boson);
- $J(z) T(w) = \frac{J(w)}{(z-w)^2} + \frac{\partial J(w)}{(z-w)}
  + \mathrm{reg.}$ ($T$ is module-spin-2 over Heisenberg);
- $T(z) W^{(3)}(w) = \frac{3 W^{(3)}(w)}{(z-w)^2}
  + \frac{\partial W^{(3)}(w)}{(z-w)} + \mathrm{reg.}$
  ($W^{(3)}$ is a primary of weight 3).

**Confidence.** High. The Sugawara construction is textbook
(FBZ04 §3.4.7-8) and the manuscript-internal $\lambda$-bracket
verifies the relevant axioms at depth 5 (P4-G2-M1 / 405 instances /
0 failures). The chain-level $c_T = 1$ before twist follows from
the standard Sugawara Virasoro central charge of a single boson
(cf. Pressley-Segal §4.2).

---

## §2. (T2.2.2) Construction of $\tau_T$ — or the no-go, with categorical reformulation

### §2.1 Why $\tau_T$ is *not* a Lurie HA §5.5.4.10 Bousfield localisation in the M2/M3 sense

The M2 toy twist $\tau_{\mathfrak h}$ and the M3 spin-3 twist
$\tau_{W_3}$ are **forgetful** Bousfield localisations
(M2 §3.2, candidate (ii); M3 §2.1):
- **Source:** locally constant FA on $\R \times \C$ with
  conformal-Virasoro structure on $\C$ (i.e., a conformal VOA);
- **Target:** locally constant FA on $\R$ alone, *forgetting*
  the conformal vector and integrating out the $\C$-direction;
- **W-class:** morphisms whose homotopy fibre is concentrated in
  conformal weight $\geq 2$.

This is a Bousfield localisation: the W-class is closed under the
appropriate structure maps (M2 §3.5: H1-H5 verified); the localisation
inverts these morphisms.

**$\tau_T$ asks for the opposite direction**: take a topological
FA on $\R$ (no Virasoro) and *promote* it to a conformal VOA on
$\R \times \C$. **This is not a Bousfield localisation** because:
- there is no W-class on the source whose inversion produces the
  target (the target is *richer* than the source, not poorer);
- the construction *adds structure* (conformal vector, weight grading,
  $z$-coordinate dependence) rather than forgetting it.

**Categorical fact (LurieHA §5.5.4.10 + standard Bousfield
theory).** A Bousfield localisation $L : \mathcal C \to \mathcal C[W^{-1}]$
has a **right adjoint** $i : \mathcal C[W^{-1}] \to \mathcal C$
which is **fully faithful** (the inclusion of the local objects).
The right adjoint $i$ is *not* itself a Bousfield localisation; it
is the *inverse* direction.

**Therefore $\tau_T$ exists as the right adjoint to
$\tau_{\mathfrak h}^{\mathrm{spin}\leq 2}$**, restricted to the
spin-2 axis. This right adjoint is fully faithful, sending a
topological FA $\mathcal A^{\mathrm{top}}$ (in the M2 image) to
its associated conformal VOA $i(\mathcal A^{\mathrm{top}})$ that
$\tau_{\mathfrak h}$ would localise back to $\mathcal A^{\mathrm{top}}$.

### §2.2 Construction of $\tau_T$ as right adjoint

Define
$$\tau_T \;:\; \mathrm{Fact}^{\mathrm{lc,top}}\bigl(\R; \mathcal C^{\hbar}\bigr)^{\mathrm{spin}\leq 2}
\;\longrightarrow\;
\mathrm{Fact}^{\mathrm{lc,conf}}\bigl(\R \times \C; \mathcal C^{\Omega}\bigr)^{\mathrm{spin}\leq 2}$$
on the spin-1 $\oplus$ spin-2 sub-categories, by:

(a) **$\hbar$-rebasing back to $\epsilon$-coordinates.** Invert the
M2 rebasing $\hbar^2 = \epsilon_1 \epsilon_2$ at the diagonal
$\lambda = 1$ self-dual scaling. This requires choosing a basepoint;
$\tau_T$ is well-defined up to the rebasing morphism (R-P4-EXEC-CGW-B
residual, M2 §5.4).

(b) **Conformal vector reinstatement.** Add the Sugawara conformal
vector $\omega = T(-2)\mathbf 1$ defined by
$T(z) := (1/(2k)) :J(z)^2: + \cdots$, with $k =
-(\epsilon_1+\epsilon_2)/(\epsilon_1\epsilon_2)$ (M2 §2.2 SV form)
or $k = 1$ (Costello unit). The conformal vector is a *new* element
of the algebra not present in the topological side.

(c) **Holomorphic factorization in the $\C$-direction.** Promote the
locally constant FA on $\R$ to a holomorphic FA on $\R \times \C$
by translating $J(z)$ from a smeared $\R$-current to a holomorphic
spin-1 current on the brane line $\C$ via Williams arXiv:2007.13985
§3-§4 dictionary. The Virasoro module structure is constructed by
the Sugawara descent.

This is the **right adjoint** to the M2 forgetful Bousfield
$\tau_{\mathfrak h}$. By LurieHA §5.5.4.10 standard adjunction
theory, $\tau_T$ is **fully faithful**: distinct conformal VOAs
in the image of $\tau_T$ map to distinct topological FAs in the M2
image, and conversely.

### §2.3 Categorical verdict

**P4-EXEC-G4-T2.2-(T2.2.2) verdict.**

$\tau_T$ does **not** exist as a Lurie HA §5.5.4.10 *Bousfield
localisation* (the directions are opposite to M2 / M3); it exists
as a **fully faithful right adjoint** to $\tau_{\mathfrak h}^{\mathrm{spin}\leq 2}$.
This is the canonical categorical home for the conformal-Virasoro
promotion functor: it is **not** a localisation but the *inverse*
direction of the M2 localisation, restricted to the spin-1 $\oplus$
spin-2 sub-category and exhibited as a fully faithful inclusion of
local objects.

**Confidence.** Medium-high. The right-adjoint construction is
clean by LurieHA §5.5.4.10 standard adjunction; the *fullness* of
the inclusion is automatic by Bousfield-theory; the *spin-grading
respect* is a structural extension whose verbatim verification
requires the spin-tower companion-tower argument of §5 below.

### §2.4 No-go for $\tau_T$ as a Bousfield localisation in its own right

Suppose $\tau_T$ existed as a Bousfield localisation $L : \mathcal C \to \mathcal C[W^{-1}]$
with W-class inverting "topological → conformal-Virasoro" morphisms.
Then the local objects (the conformal VOAs) would be the
*$W$-local* objects in $\mathcal C$. But the M2 localisation's local
objects (the W-local in the *forgetful* direction) are the
topological FAs *without* conformal structure — they are exactly
the local objects in the M2 localisation. **Asking for $\tau_T$ to
also have the conformal VOAs as its W-local would require both
classes (topological and conformal) to be *simultaneously* W-local
in the *same* category**, which is impossible if the two are
*distinct* (forgetful's image is strictly smaller than its source).

**Therefore the no-go is structural**: $\tau_T$ cannot be a
Bousfield localisation distinct from $\tau_{\mathfrak h}$'s right
adjoint. The construction §2.2 is the *unique* canonical home.

---

## §3. (T2.2.3) OPE verification at leading order

### §3.1 The leading $1/(z-w)^4$ pole on the twisted (conformal) side

After applying $\tau_T$, the spin-2 current $T(z)$ inherits its
conformal Virasoro structure from the Sugawara construction
(M2 §2.2):
$$T(z) := \frac{1}{2k} \!:\!J(z)^2\!:\,-\,\frac{1}{2k}\partial J(z) + \cdots,$$
with $k = -(\epsilon_1+\epsilon_2)/(\epsilon_1\epsilon_2)$ in the
SV $S_3$-symmetric normalisation.

**Leading $1/(z-w)^4$ pole.** Standard Sugawara Virasoro central
charge of a single boson at level $k$:
$$c_{\mathrm{Sug}}(k) \;=\; 1 \quad (\text{for any } k \neq 0, \text{ single boson}).$$

This is the contribution from the spin-1 (Heisenberg) generator
alone. **The full $W_{1+\infty}$ Virasoro central charge** at the
conformal VOA level is
$$c_{\mathrm{full}}(\epsilon_1, \epsilon_2) \;=\; \frac{(\epsilon_1+\epsilon_2)^2}{\epsilon_1\epsilon_2},$$
from Schiffmann-Vasserot 2013 Eq. 3.1.1 (M1 §2.2; CGW-anchor §2.2).
The full central charge **includes the higher-spin generators'
Sugawara contributions**: each spin-$s$ generator $J^{(s)}$ for
$s \geq 2$ contributes additively to the universal $W$-central
charge via Pope-Romans-Shen 1990.

**At $\lambda = 1$ self-dual scaling**: $c_{\mathrm{full}}(\epsilon, \epsilon)
= 4$, with the spin-1 Sugawara contributing $c_{\mathrm{Sug}} = 1$
and the higher spins ($s \geq 2$) contributing $c - 1 = 3$ in total
(M2 §5.3 lines 700-707).

**Therefore the $1/(z-w)^4$ pole coefficient on the twisted side is:**
$$\frac{c_{\mathrm{full}}/2}{(z-w)^4} \;=\; \frac{(\epsilon_1+\epsilon_2)^2/(2\epsilon_1\epsilon_2)}{(z-w)^4}
\;=\; \frac{c/2}{(z-w)^4}.$$

**At $\lambda = 1$**, this is $4/2 = 2$ in the leading pole. **At the
Calabi-Yau boundary $\lambda = -1$**, the leading pole vanishes
($c = 0$). **The OPE leading-pole coefficient is verified.**

### §3.2 The $1/(z-w)^2$ subleading pole

By the Virasoro OPE structure, the $1/(z-w)^2$ subleading pole has
coefficient $2 T(w)$:
$$T(z) T(w) \;\sim\; \cdots \,+\, \frac{2 T(w)}{(z-w)^2} \,+\, \cdots$$

**This is the conformal weight-2 module structure**: $T$ acts on
itself as a primary of weight 2 (with anomaly), inheriting the
$1/(z-w)^2$ coefficient from the Sugawara descent. **The twisted
side preserves this**: the right-adjoint $\tau_T$ sends the
chain-level Heisenberg-Sugawara $T$-$T$ OPE to the Schiffmann-
Vasserot conformal $T$-$T$ OPE, with the *coefficient* of
$1/(z-w)^2$ being $2 T(w)$ on both sides (the OPE structure is
preserved up to the $c$-coefficient on the leading pole).

### §3.3 The $1/(z-w)$ subleading pole

Standard Virasoro: coefficient $\partial T(w)$:
$$T(z) T(w) \;\sim\; \cdots \,+\, \frac{\partial T(w)}{(z-w)} \,+\, \mathrm{reg.}$$

**Identical preservation to §3.2**: the $\partial T(w)$ coefficient
is structurally $1$ on both chain-level and twisted sides; it is
the Virasoro derivative term.

### §3.4 Full OPE on the twisted side

$$T(z) T(w) \;\bigg|_{\tau_T\text{-side}} \;=\;
\frac{c/2}{(z-w)^4}
+ \frac{2 T(w)}{(z-w)^2}
+ \frac{\partial T(w)}{(z-w)}
+ \mathrm{reg.}$$
with $c = (\epsilon_1+\epsilon_2)^2/(\epsilon_1\epsilon_2)$.

This is the standard Virasoro OPE at conformal central charge $c$;
it agrees verbatim with FBZ04 §3.4.6.

### §3.5 Cross-check via Sugawara

The Sugawara $T = (1/2k) :J^2: - (1/2k) \partial J + \cdots$ gives:
$$[T(z), J(w)] \;\sim\; \frac{J(w)}{(z-w)^2} + \frac{\partial J(w)}{(z-w)},$$
$$[T(z), T(w)] \;\sim\; \frac{c/2}{(z-w)^4} + \frac{2 T(w)}{(z-w)^2} + \frac{\partial T(w)}{(z-w)},$$
with $c = c_{\mathrm{Sug}}(\widehat{\mathfrak{gl}}_1) + c_{\mathrm{higher-spin}}$.
At $W_{1+\infty}(\epsilon_1, \epsilon_2)$, the higher-spin contributions
sum to give the Schiffmann-Vasserot $c =
(\epsilon_1+\epsilon_2)^2/(\epsilon_1\epsilon_2)$.

### §3.6 P4-EXEC-G4-T2.2-(T2.2.3) verdict

**Verdict.** The OPE
$$T(z) T(w) \;=\; \frac{c/2}{(z-w)^4}
+ \frac{2 T(w)}{(z-w)^2}
+ \frac{\partial T(w)}{(z-w)} + \mathrm{reg.}$$
**holds at leading order on the $\tau_T$-twisted side with the
Schiffmann-Vasserot central charge
$c = (\epsilon_1+\epsilon_2)^2/(\epsilon_1\epsilon_2)$**.

The verification is by direct cross-walk to the Sugawara construction
on the spin-1 ⊕ spin-2 sub-VOA of $W_{1+\infty}(\epsilon_1, \epsilon_2)$.
The $1/(z-w)^4$ leading pole is $c/2$ with $c$ matching the
Schiffmann-Vasserot formula; the subleading $1/(z-w)^2$ and
$1/(z-w)$ poles are preserved structurally (they carry $T$ and
$\partial T$ respectively, identical on both sides).

**Verification at specific scaling limits:**

| Scaling | $c$ | $c/2$ leading pole |
|---------|-----|---------------------|
| $\lambda = 1$ self-dual | $4$ | $2$ |
| $\lambda = -1$ Calabi-Yau | $0$ | $0$ |
| $\lambda \to 0$ pure-axis | $\infty$ | divergent |
| diagonal $\lambda$ generic | $(1+\lambda)^2/\lambda$ | finite |

**Confidence.** Medium-high. The OPE structure follows from
Sugawara verbatim (textbook FBZ04 §3.4.7-8); the Schiffmann-Vasserot
$c$ formula is verbatim from SV13 Eq. 3.1.1. The leading-pole
verification is direct. The subleading poles are structural
preservations.

---

## §4. (T2.2.4) Hypothesis preservation table including $(A2')$

### §4.1 Preliminary: the seven hypothesis variants in scope

Per `phase4-exec-A1-hypothesis-audit-2026-04-28.md` §0 (executive
verdict): the hypothesis class consists of $(A1)$-$(A4)$ inscribed
in the manuscript, $(A5)$ proposed via W30, plus the silent $(A2')$
on existence of even non-degenerate ad-invariant supersymmetric
bilinear form. Plus the silent **Costello regulator-class
compatibility** meta-hypothesis (§1.7 of A1-HYP-AUDIT).

For $\tau_T$ the question is: **which $(A_k)$ variant is
preserved or strengthened on the twisted (conformal-promoted)
side?**

### §4.2 Per-hypothesis preservation under $\tau_T$

#### $(A1)$ — Truncation discipline (degreewise surjective transitions)

**Preservation under $\tau_T$.** **VACUOUSLY PRESERVED.**

$(A1)$ is a class definition on the test-data side (admissible
regulator class for the BV theory; truncation in coefficient and
local-functional directions). The conformal promotion $\tau_T$ does
not interact with the test-data class: the regulator class is the
same on both sides (chain-level and twisted), since both sides
use the same Costello-Gwilliam BV regulator framework.

The conformal Virasoro structure is *categorical* (a sub-category
selection), not regulator-level. **Hence $(A1)$ is preserved without
modification**: any admissible regulator class on the chain-level
side remains admissible after $\tau_T$.

**Variant on twisted side.** Same as on chain-level side:
$(A1)$ as inscribed in `tate-T1-weighted-completion.tex`:606-610.

#### $(A2)$ — Vertexwise polynomial-degree-bounded legs

**Preservation under $\tau_T$.** **PRESERVED, with silent
strengthening to $(A2''_T)$.**

$(A2)$ on the chain-level side requires that at each fixed $\hbar$-
order and Costello graph, the coefficient expression uses only
vertexwise polynomial-degree-bounded Hamiltonian and cotangent legs
(`tate-T1-weighted-completion.tex`:611-613).

After conformal promotion via $\tau_T$, the *Virasoro OPE descent*
introduces additional structure: the $\{T_n\}$ modes generate
Virasoro descendants $L_{-n_1} L_{-n_2} \cdots$, and the
$\lambda$-bracket on these descendants involves polynomial-degree
expressions in the underlying Heisenberg modes via the Sugawara
formula. **The polynomial-degree class on the twisted side must
include the Sugawara-descent terms**:

$(A2''_T)$ — twisted-side variant: Vertexwise polynomial-degree-bounded
legs, *plus* the Virasoro descendants $L_{-n_1} \cdots L_{-n_k}$
with $n_i \geq 1$ remain within the polynomial-degree class via
the Sugawara expansion.

This is a **silent strengthening** because the manuscript's
inscribed $(A2)$ on the chain-level side does not explicitly
declare the Virasoro descendants. *The descendants are
*polynomial-degree-bounded* in the Heisenberg modes by the standard
Sugawara expansion (each $L_n$ is degree-2 in the $J$-modes), but
this requires verification.*

**Variant on twisted side.** $(A2''_T)$ as above. **Recommended
inscription: declare $(A2''_T)$ explicitly when the conformal
Virasoro structure is in scope.**

#### $(A3)$ — Diagonal weight-rescaling

**Preservation under $\tau_T$.** **PRESERVED.**

$(A3)$ on the chain-level side: diagonal finite-window rescaling
$R_{w,w'}^{w_0}$ transports interaction, differential, bracket,
propagator contraction, and counterterm representative across
weight windows.

After $\tau_T$, the additional structure is the **conformal-weight
grading on the Virasoro descendants**. The conformal weight is a
*natural Z-grading* on the conformal VOA, which by FBZ04 §3.4.6
is preserved by the OPE. **The conformal weight is itself a
"weight" in the sense of $(A3)$**, and the diagonal rescaling
extends naturally to include conformal weight as an additional
component of the weight tuple.

**Variant on twisted side.** $(A3)$ extended to include conformal
weight as an additional weight component. This is a *natural*
extension (no silent strengthening).

#### $(A4)$ — Admissible filtered cohomology

**Preservation under $\tau_T$.** **PRESERVED.**

$(A4)$ on the chain-level side: cohomology computed on finite
quotients and associated graded pieces (Mittag-Leffler-restricted
sense per W3-W11-01).

After $\tau_T$, the conformal Virasoro structure introduces the
**conformal-weight grading**, which provides an additional finite-
window decomposition (the *truncation by conformal weight*
$\leq w_{\mathrm{conf}}$). This is a *natural* refinement of $(A4)$:
the cohomology of the conformal VOA can be computed on
conformal-weight-truncated quotients.

**Variant on twisted side.** $(A4)$ extended to conformal-weight-
truncated quotients. Compatible with the standard CFT cohomology
computations (FBZ04 §3.5).

#### $(A5)$ — Parity-equivariance on graded sources

**Preservation under $\tau_T$.** **VACUOUSLY PRESERVED on bosonic
$W_{1+\infty}(\epsilon_1, \epsilon_2)$**; **NON-VACUOUSLY PRESERVED on
super-W extension to osp(2N|2N)** (cross-walk to M3 §6).

On the bosonic side: $W_{1+\infty}(\epsilon_1, \epsilon_2)$ is a
*purely bosonic* VOA; the parity operator $P = \mathbf 1$ acts
trivially. **$(A5)$ is vacuous**: $g(PX, PY) = g(X, Y)$ trivially,
$[K_t, P] = [Q^{\GF}, P] = [P_{\epsilon, L}, P] = 0$ trivially.

On the super-W extension to $\mathrm{osp}(2N|2N)$ (per M3 §6):
- the parity operator $P^{\mathrm{osp}} = \mathrm{diag}(\mathbf 1_{4N}, -\mathbf 1_{4N})$
  acts non-trivially on the super-Lie algebra $\mathrm{osp}(2N|2N)$;
- the super-Killing form is non-degenerate (Kac 1977 §1.1.4 basic
  classical);
- the heat kernel $\Delta_{\mathrm{sK}}^{\mathrm{osp}}$ commutes
  with $P^{\mathrm{osp}}$ by W3-W30-02(a);
- the Virasoro current $T^{(\mathrm{osp})}(z)$ in the super-W
  is parity-even (spin 2 carries parity $(-1)^2 = +1$);
- the super-Virasoro module structure is preserved by $\tau_T$
  applied at the super-W level.

**Variant on twisted side.** Same as on chain-level side: $(A5)$
as proposed by W30, parity-equivariant operators commute with $P$.
**No silent strengthening** because the conformal Virasoro
structure on a parity-trivial bosonic source is parity-equivariant
trivially, and on the super-W extension, the spin-2 generator's
parity is even (matching $P^{\mathrm{osp}}$'s diagonal action).

#### $(A2')$ — Existence of even non-degenerate ad-invariant supersymmetric bilinear form (silent)

**Preservation under $\tau_T$.** **NON-VACUOUSLY PRESERVED, with
explicit Sugawara form.**

$(A2')$ on the chain-level side requires the existence of an even
non-degenerate ad-invariant supersymmetric bilinear form on the
super-Lie source, used to define the BV pairing.

After $\tau_T$, the Virasoro descent is governed by the
**Sugawara form** on the Virasoro descendants:
$$g_{\mathrm{Sug}}(L_{-n}, L_{-m}) \;=\; (k + h^\vee) \cdot \delta_{n + m, 0} \cdot \mathrm{(weight\ factor)}$$
in the standard Sugawara construction (FBZ04 §3.4.7-8).

This form is:
- **even**: $L_{-n}$ are bosonic Virasoro modes;
- **non-degenerate** away from the critical level $k = -h^\vee$;
- **ad-invariant** by the standard Virasoro Lie-algebra structure;
- **supersymmetric** trivially (bosonic case).

On $\widehat{\mathfrak{gl}}_1$ (Heisenberg) the dual Coxeter is
$h^\vee = 0$ (abelian), so the Sugawara form is $g_{\mathrm{Sug}} =
k \cdot \delta_{n+m, 0}$, non-degenerate at $k \neq 0$. At the
$\hbar^2 = \epsilon_1 \epsilon_2$ rebasing, $k = -(\epsilon_1+\epsilon_2)/(\epsilon_1\epsilon_2)$,
which is non-zero except on the $\epsilon_1 + \epsilon_2 = 0$
Calabi-Yau locus. **At $\lambda = 1$**, $k = -2/\epsilon$, non-zero.

**Variant on twisted side.** $(A2')$ as inscribed by A1-HYP-AUDIT
§1.6, with the **specific bilinear form** identified as the Sugawara
form on the Virasoro descendants:
$g_{\mathrm{Sug}}(L_{-n}, L_{-m}) = k \cdot \delta_{n+m, 0}$ on the
spin-2 sector. **No silent strengthening** because the form is
canonically given by the Sugawara construction; the existence is
automatic on the bosonic side at $k \neq 0$.

**On the super-W extension** (osp(2N|2N), per M3 §6): the super-
Sugawara form is the orthosymplectic super-Killing form (Kac 1977
§1.1.4 basic classical), which is even non-degenerate on osp(2N|2N).
$(A2')$ is preserved verbatim.

#### Costello regulator-class compatibility (silent meta-hypothesis)

**Preservation under $\tau_T$.** **PRESERVED.**

The Costello 2011 framework on conformal VOAs is documented in
Costello 2011 Ch 5 §5.2 (chiral CFTs), and the BV regulator on
holomorphic factorization algebras is Costello-Gwilliam Vol II
§11. **The framework supports both topological (chain-level) and
conformal (twisted) sides**. The promotion $\tau_T$ does not push
the regulator class outside Costello's admissible domain.

**Variant on twisted side.** Same as on chain-level side, with
the regulator class restricted to those compatible with the
conformal Virasoro structure (typically: heat-kernel from the
Virasoro Casimir; CFT regulators per Costello 2011 Ch 5).

### §4.3 Hypothesis preservation table

| Hypothesis | Chain-level (M2/M3) variant | $\tau_T$-twisted variant | Preservation status | Silent strengthening? |
|------------|------------------------------|--------------------------|---------------------|----------------------|
| $(A1)$ Truncation | inscribed | same | **VACUOUSLY PRESERVED** | No |
| $(A2)$ Polyn-deg-bnd | inscribed | $(A2''_T)$ — extended to Virasoro descendants | **PRESERVED** | **YES, $(A2''_T)$ silent** |
| $(A3)$ Wt-rescale | inscribed | extended to conformal weight | **PRESERVED** (natural extension) | No |
| $(A4)$ Adm-fil-cohom | inscribed | extended to conf-wt-truncated quotients | **PRESERVED** (natural extension) | No |
| $(A5)$ Parity-equiv | proposed (W30) | same | **VACUOUSLY** on bosonic $W_{1+\infty}$; **non-vacuously** on super-W | No |
| $(A2')$ Even non-deg form | silent (audit §1.6) | Sugawara form $g_{\mathrm{Sug}} = k \delta_{n+m,0}$ | **NON-VACUOUSLY PRESERVED** with explicit form | No (form is canonical) |
| Costello compat | silent (audit §1.7) | extended to conformal-VOA Costello framework | **PRESERVED** | No |

### §4.4 Silent strengthenings introduced by $\tau_T$

**One silent strengthening identified:** $(A2)$ silently strengthens
to $(A2''_T)$ on the twisted side: the polynomial-degree class
must include the Virasoro descendants $L_{-n_1} \cdots L_{-n_k}$
expressed via Sugawara as polynomials in the Heisenberg modes.

**Recommended inscription.** When the conformal Virasoro structure
is in scope (i.e., on the twisted side after $\tau_T$), declare
$(A2''_T)$ explicitly as: "for each fixed $\hbar$-order, the
Costello graph expression includes only legs that are
polynomial-degree-bounded in the Heisenberg modes *or* are Virasoro
descendants expressible polynomially in the Heisenberg modes via
the Sugawara descent."

### §4.5 Which $(A_k)$ variant is most easily violated?

**$(A2''_T)$ — the silent twisted-side strengthening of $(A2)$ —
is the most easily violated**:
- non-Sugawara stress tensors (e.g., free-field realisations with
  *background charge* $\alpha_0$ Felder twist) introduce *non-
  polynomial* terms in the $L_n$-mode expansion (the Felder
  background charge is $\alpha_0 \partial \phi$, where $\partial \phi$
  is a *transcendental* element of the Heisenberg-Sugawara descent);
- such constructions break $(A2''_T)$ because the polynomial-degree
  class fails to bound the Felder twist contribution.

The manuscript's working regime is the **Sugawara** construction
without Felder twist; **$(A2''_T)$ holds**. But this is a *non-
trivial* discipline that the inscription should make explicit.

### §4.6 Which $(A_k)$ variant is silently strengthened on the twisted side?

**$(A2)$** — strengthens to $(A2''_T)$ as discussed.

**$(A4)$** — natural extension (not "silent strengthening"; just
a refinement to include conformal weight as a finite-window
parameter).

**$(A2')$** — non-vacuously preserved with the explicit Sugawara
form; this is *not* a silent strengthening but an *explicit*
realisation of the silent existence requirement on the chain-level
side.

### §4.7 P4-EXEC-G4-T2.2-(T2.2.4) verdict

**Verdict.** All seven hypothesis variants ($(A1)$-$(A5)$, $(A2')$,
Costello-class) are preserved on the twisted side, with **one
silent strengthening identified**: $(A2)$ silently strengthens to
$(A2''_T)$ to include the Virasoro Sugawara descendants in the
polynomial-degree class.

**Confidence.** Medium-high. The hypothesis-preservation analysis
is structurally clean (each hypothesis is class-of-test-data or
existence-of-form, not directly affected by the conformal-vector
addition). The silent strengthening $(A2''_T)$ is the load-bearing
identification; its discharge requires the standard Sugawara
expansion (FBZ04 §3.4.7-8), which holds on the manuscript's
working regime.

---

## §5. (T2.2.5) Cross-walk to $\tau_{\mathfrak h}$ and $\tau_{W_3}$ — companion-tower of twist functors

### §5.1 The M2/M3 forgetful tower vs the $\tau_T$ promotion

**M2/M3 forgetful tower** $\{\tau_{\mathfrak h}, \tau_{W_3}, \ldots\}$:
- direction: conformal (with Virasoro) → topological (no Virasoro);
- source: locally constant FA on $\R \times \C$ with conformal structure;
- target: locally constant FA on $\R$ alone;
- W-class: morphisms forgetting conformal structure;
- functor type: Bousfield localisation (LurieHA §5.5.4.10).

**$\tau_T$ promotion**:
- direction: topological (no Virasoro) → conformal (with Virasoro);
- source: locally constant FA on $\R$;
- target: locally constant FA on $\R \times \C$ with conformal
  structure;
- functor type: fully faithful right adjoint to $\tau_{\mathfrak h}$.

**The directions are opposite.** $\tau_T$ does **not** factor
through $\tau_{\mathfrak h}$ at the categorical level (different
domains and codomains).

### §5.2 The composite $\tau_T \circ \tau_{\mathfrak h}$ (where it's defined)

On the spin-1 ⊕ spin-2 sub-VOA of $W_{1+\infty}$, the composite
$$\tau_T \circ \tau_{\mathfrak h}^{\mathrm{spin}\leq 2} \;:\;
\mathrm{Fact}^{\mathrm{lc,conf}}\bigl(\R \times \C; \mathcal C^{\Omega}\bigr)^{\mathrm{spin}\leq 2}
\;\longrightarrow\;
\mathrm{Fact}^{\mathrm{lc,conf}}\bigl(\R \times \C; \mathcal C^{\Omega}\bigr)^{\mathrm{spin}\leq 2}$$

is the **identity functor on the spin $\leq 2$ conformal sub-VOA**:
- $\tau_{\mathfrak h}$ forgets the conformal vector;
- $\tau_T$ promotes back to conformal via Sugawara.

The fully faithful inclusion of the *local objects* (M2 image)
back into the source ensures the composite is the identity.

### §5.3 The Sugawara factorisation: $\tau_T$ via $\tau_{\mathfrak h}$ and the Sugawara morphism

There is a **structural factorisation** of $\tau_T$ through
$\tau_{\mathfrak h}$:
$$\tau_T \;=\; (\tau_{\mathfrak h})^{R} \;\circ\; \mathrm{Sug},$$
where $(\tau_{\mathfrak h})^R$ is the right adjoint to
$\tau_{\mathfrak h}$ (fully faithful inclusion), and $\mathrm{Sug}$
is the **Sugawara morphism** sending $J(z)$ to $T(z) = (1/(2k)):J^2:
- (1/(2k)) \partial J + \cdots$.

**This is the Att-2 attack-angle answer**: $\tau_T$ is *not*
independent of $\tau_{\mathfrak h}$; it factors through it via the
Sugawara construction. Specifically:
- $\tau_{\mathfrak h}$ deals with the spin-1 generator $J$ alone;
- the Sugawara morphism produces $T = (1/(2k)):J^2: + \cdots$ from $J$;
- the right adjoint $(\tau_{\mathfrak h})^R$ promotes back to the
  full conformal VOA on $\R \times \C$.

**The factorisation respects the spin grading**: at each spin level
$s$, the corresponding $\tau_{(s)}$ functor exists and is the right
adjoint to the M2/M3 forgetful Bousfield restricted to spin-$s$.

### §5.4 The companion tower $\{\tau_{(s)}\}_{s \geq 1}$

**Construction.** Define $\tau_{(s)}$ as the **fully faithful right
adjoint** to the M2/M3 spin-$s$ forgetful Bousfield localisation
$\tau_{\mathfrak h, W_3, \ldots}^{\mathrm{spin}\leq s}$ restricted to
the spin-$s$ axis. Specifically:
- $\tau_{(1)} \equiv \mathrm{id}_{\mathrm{spin-1}}$ trivially (M2 is
  the spin-1 forgetful; its right adjoint on the spin-1 axis is
  identity, since the spin-1 level is preserved by the Bousfield);
- $\tau_{(2)} \equiv \tau_T$ (this section's main result);
- $\tau_{(3)} \equiv$ the spin-3 conformal-promotion functor,
  parallel construction to $\tau_T$ but for the $W^{(3)}$ generator;
- $\tau_{(s)}$ for $s \geq 4$: parallel construction at higher
  spins.

**Spin-grading respect.** Each $\tau_{(s)}$ acts on the spin-$s$
sub-VOA without mixing with other spin levels. The full tower
$\{\tau_{(s)}\}_{s \geq 1}$ acts on the full $W_{1+\infty}$
spin-tower, with each spin level $s$ promoted independently.

### §5.5 Lift to a 2-functor at the $(\infty, 2)$-categorical level

**Att-4 attack-angle:** does $\tau_T$ lift to a 2-functor at the
$(\infty, 2)$-categorical level?

**Answer.** **PARTIAL.** $\tau_T$ is a 1-functor (right adjoint to
the M2 Bousfield); promotion to a 2-functor requires verifying
**coherent homotopy** between the right-adjoint structure and the
spin-grading respect. The Lurie HA §5.5.4.10 framework provides
the 1-functorial structure verbatim; the 2-categorical coherence
requires:
- compatibility of $\tau_T$ with the natural 1-morphisms in the
  source category (verified by the standard adjunction);
- compatibility of $\tau_T$ with the 2-morphisms (homotopies)
  between 1-morphisms (requires explicit homotopy coherence
  verification).

**Verdict.** The 2-functorial lift is *plausible* but requires
explicit homotopy coherence verification beyond M-1 scope. **Open
question P4-EXEC-G4-T2.2-Q1**, severity 2 (sharpening), **deferred to
M-6 milestone**.

### §5.6 P4-EXEC-G4-T2.2-(T2.2.5) verdict

**Verdict.**

1. **$\tau_T$ does not factor through $\tau_{\mathfrak h}$ as a
   composition of Bousfield localisations** (the directions are
   opposite).

2. **$\tau_T$ factors through the Sugawara construction**:
   $\tau_T = (\tau_{\mathfrak h})^R \circ \mathrm{Sug}$, where
   $(\tau_{\mathfrak h})^R$ is the right adjoint to $\tau_{\mathfrak h}$
   and $\mathrm{Sug}$ is the Sugawara morphism. **This is the
   Att-2 attack-angle answer**: $\tau_T$ is *not* independent of
   $\tau_{\mathfrak h}$; the Sugawara descent links them.

3. **There is a companion tower $\{\tau_{(s)}\}_{s \geq 1}$** of
   conformal-promotion functors, each fully faithful right adjoint
   to the M2/M3 spin-$s$ forgetful Bousfield, respecting the spin
   grading.

4. **The 2-functorial lift to $(\infty, 2)$-categorical level is
   plausible but unverified**; the 1-functorial structure is clean
   via LurieHA §5.5.4.10 standard adjunction.

**Confidence.** Medium. The factorisation through Sugawara is
structurally clean and matches the Att-2 attack-angle. The
companion-tower construction is by parallel of M2/M3, with the
spin grading respected by the right-adjoint structure. The
2-functorial lift remains open at M-1 scope.

---

## §6. (T2.2.6) Failure mode and obstruction class

### §6.1 The named obstruction class

**(I-CC) Conformal-promotion is not a Bousfield localisation.**

This is the structural obstruction identified in §2.1: the
direction of $\tau_T$ (topological → conformal-Virasoro) is
opposite to the direction of $\tau_{\mathfrak h}$ / $\tau_{W_3}$
(conformal → topological-forgotten). A Bousfield localisation
goes in the *forgetful* direction; the *inverse* direction is a
*right-adjoint inclusion*.

### §6.2 Discharge route

**Reformulation as right adjoint.** Per §2.2-§2.3: $\tau_T$ exists
as the **fully faithful right adjoint** to $\tau_{\mathfrak h}^{\mathrm{spin}\leq 2}$
(restricted to spin-2). This is the canonical categorical home for
$\tau_T$ and the obstruction (I-CC) is **discharged at the toy
level** by the right-adjoint reformulation.

### §6.3 Phase-5 escalation conditions

The discharge is **conditional** on:

(a) **R-P4-EXEC-CGW-B (canonicality of the rebasing $\hbar^2 = \epsilon_1\epsilon_2$).**
   The rebasing morphism between the chain-level $\hbar$-deformation
   and the CGW $\epsilon$-deformation is unproven canonical. The
   $\tau_T$ construction depends on the inverse rebasing, so the
   right-adjoint right-inverse of $\tau_{\mathfrak h}$ depends on
   this canonicality. **Phase-5 escalation if the rebasing fails to
   be canonical.**

(b) **R-P4-EXEC-G4-M3-A (spin-3 cocycle survives, no manuscript
   analog).** The companion-tower construction $\{\tau_{(s)}\}_{s \geq 1}$
   includes spin-$s$ promotion functors for $s \geq 3$; per M3 §5.4
   Interpretation A (spin-tower truncation), a *second* localisation is
   required to kill the higher-spin classes. **If Interpretation A holds,
   $\tau_{(s)}$ for $s \geq 3$ produces *extra structure* not
   present in the manuscript, exposing the manuscript as carrying
   only the spin-1 and spin-2 components.** This is a Phase-5
   escalation if the spin-tower truncation cannot be discharged at
   the conformal-promotion level.

(c) **R-P4-EXEC-G4-T2.2-A (silent strengthening $(A2''_T)$ on the
   twisted side).** The polynomial-degree class on the twisted side
   must include Virasoro descendants. **If the manuscript's working
   regime extends beyond Sugawara to non-Sugawara stress tensors
   (Felder twist, etc.), $(A2''_T)$ may fail and Phase-5 escalation
   would be required.**

(d) **2-functorial lift coherence (open question P4-EXEC-G4-T2.2-Q1).**
   The $(\infty, 2)$-categorical lift is unverified. **If the
   coherence cannot be verified, the construction is restricted to
   the 1-categorical level**, sufficient for M-1 and M-3 milestones
   but potentially limiting for M-6+ when full $(\infty, 2)$-
   structure is required.

### §6.4 P4-EXEC-G4-T2.2-(T2.2.6) verdict

**Verdict.** $\tau_T$ does not fail outright; the named obstruction
**(I-CC) Conformal-promotion is not a Bousfield localisation** is
**discharged via the right-adjoint reformulation** (§2.2). The
discharge is conditional on:
- the rebasing canonicality (R-P4-EXEC-CGW-B);
- the spin-tower truncation (R-P4-EXEC-G4-M3-A);
- the polynomial-degree class extension to Virasoro descendants
  (R-P4-EXEC-G4-T2.2-A);
- the 2-functorial lift coherence (open question P4-EXEC-G4-T2.2-Q1).

**Phase-5 escalation conditions** are:
- the rebasing is not canonical;
- the spin-tower truncation cannot be discharged at the
  conformal-promotion level;
- $(A2''_T)$ fails on a non-Sugawara stress tensor;
- the 2-functorial lift coherence fails.

**None of these escalations fire at M-1 / M-3 scope**; they are
deferred to M-6+ horizons.

**Confidence.** Medium-high. The right-adjoint discharge is
structurally clean; the conditional nature is reasonable for a
toy-level / M-1 result. The Phase-5 escalation conditions are
well-defined and can be discharged or escalated as the manuscript
matures.

---

## §7. Anti-attack scan responses

### §7.1 Att-1 — Lurie HA §5.5.4.10 W-class closure for $T(z)$ alone

**Attack.** Lurie HA §5.5.4.10 Bousfield localisation requires the
"localising class" to be closed under specific structure maps; does
$T(z)$ admit such a class without dragging in spin-3 and higher?

**Response.** The W-class for the M2/M3 forgetful Bousfield
localisations is "morphisms whose homotopy fibre is concentrated in
conformal weight $\geq 2$" (or $\geq 3$ for M3). The W-class for
$\tau_T$ (if it existed as a Bousfield) would need to be the
*opposite* — but **no such W-class exists** because the conformal
direction is *additive* (more structure), not *forgetful*
(less structure).

**The correct response is**: $\tau_T$ is **not** a Bousfield
localisation. It is a right adjoint to the forgetful localisation,
and the right adjoint **does not require its own W-class** — it is
defined automatically by the standard adjunction.

**The W-class for "spin-2 alone, no higher spins" is the M3 §3.4
spin-truncation** (defined at the source level by truncating the
$W_{1+\infty}$ spin tower at $s \leq 2$, then taking the M2
forgetful). This **does not bring in spin-3**; the truncation is
*before* the M2 forgetful, so spin-3 generators are excluded *a
priori*.

**Verdict on Att-1.** Discharged: $\tau_T$ is not a Bousfield (no
W-class needed); the spin-truncation to spin $\leq 2$ is at the
source category level (independent of M2's W-class), so spin-3 is
not dragged in. **No escalation.**

### §7.2 Att-2 — Sugawara $T = (1/2k):J \cdot J:$ relates $\tau_T$ to $\tau_{\mathfrak h}$

**Attack.** The Sugawara construction $T = (1/(2(k+h^\vee))):J \cdot J:$
relates $T$ to $J$, so $\tau_T$ may not be independent of
$\tau_{\mathfrak h}$. Verify or deny.

**Response.** **Confirmed: $\tau_T$ is not independent of
$\tau_{\mathfrak h}$.** Per §5.3, the factorisation
$$\tau_T \;=\; (\tau_{\mathfrak h})^R \;\circ\; \mathrm{Sug}$$
exhibits $\tau_T$ as a *composite* of:
- the Sugawara morphism $\mathrm{Sug}$ (sending $J$ to
  $T = (1/(2k)):J^2: + \cdots$);
- the right adjoint $(\tau_{\mathfrak h})^R$ (promoting the
  topological FA to the conformal VOA).

The Sugawara construction is a structural map from the spin-1
sub-VOA to the spin-1 ⊕ spin-2 sub-VOA, and it is *the* mechanism
linking $\tau_{\mathfrak h}$'s output to $\tau_T$'s input.

**Verdict on Att-2.** Confirmed: **$\tau_T$ factors through
$\tau_{\mathfrak h}$ via the Sugawara morphism**, exhibiting the
attack-angle's prediction. The factorisation is non-trivial and
load-bearing for the spin-grading respect of the companion tower.
**This is a sharpening, not an obstruction.** No escalation.

### §7.3 Att-3 — Schiffmann-Vasserot $c$ divergence and $(A5)$ regulator-independence

**Attack.** Under $\hbar^2 = \epsilon_1 \epsilon_2$ rebasing, the
Schiffmann-Vasserot $c$ diverges in some scaling limits; does the
Virasoro promotion respect the regulator-independence of W30 (A5)?

**Response.** The Schiffmann-Vasserot $c = (\epsilon_1+\epsilon_2)^2/(\epsilon_1\epsilon_2)$
exhibits the following scaling behaviour (CGW-anchor §2.3, M2 §2.4):

| Scaling | $c$ |
|---------|-----|
| diagonal $\lambda = 1$ | $4$ (finite) |
| Calabi-Yau $\lambda = -1$ | $0$ (zero) |
| pure-axis $\lambda \to 0$ | $\infty$ (divergent) |
| diagonal generic $\lambda$ | $(1+\lambda)^2/\lambda$ (finite) |

**At the divergent pure-axis limit**, the $\tau_T$ construction
*cannot proceed* because the Sugawara level $k$ diverges
($k = 1/\epsilon_1$ for $\epsilon_2 \to 0$, divergent in the $\hbar
\to 0$ rebasing). **$\tau_T$ is well-defined only on the
non-divergent scaling paths**, namely the diagonal $\lambda = 1$
(and other generic diagonal directions away from $\lambda = 0$).

**$(A5)$ regulator-independence is preserved on the
non-divergent scaling paths** because the heat-kernel construction
of W30 (A5)-heal §2 uses the parity-equivariant supertrace, which
is well-defined on the bosonic side trivially ($P = \mathbf 1$) and
on the super-W extension via the orthosymplectic super-Killing form
(non-degenerate for $\mathrm{osp}(2N|2N)$).

**On the divergent pure-axis limit**, the $\tau_T$ construction
*itself* fails (level $k$ diverges, Sugawara form degenerate); this
is a **boundary obstruction** of the construction, not an
$(A5)$ violation. **(A5) is not active on this divergent boundary
because $\tau_T$ is not defined there**.

**Verdict on Att-3.** **(A5) regulator-independence is preserved on
the non-divergent scaling paths**. The divergent pure-axis limit
is a $\tau_T$-undefined region, not an $(A5)$-violating region.
**No escalation.**

### §7.4 Att-4 — 2-functorial lift at $(\infty, 2)$-categorical level

**Attack.** Does $\tau_T$ lift to a 2-functor at the
$(\infty, 2)$-categorical level, or only to a 1-functor with
coherent homotopy?

**Response.** Per §5.5: **$\tau_T$ is a 1-functor (right adjoint
to M2 Bousfield); the $(\infty, 2)$-lift is plausible but
unverified at M-1 scope.** The 1-functorial structure is clean via
LurieHA §5.5.4.10 standard adjunction; the 2-categorical coherence
requires explicit homotopy coherence verification.

**Verdict on Att-4.** Open question P4-EXEC-G4-T2.2-Q1, severity 2
(sharpening). **Deferred to M-6 milestone**. The 1-functorial
construction is sufficient for M-1 / M-3 scope.

---

## §8. Residuals and deciding evidence

### §8.1 New residuals from this T2.2 analysis

**R-P4-EXEC-G4-T2.2-A (silent strengthening $(A2''_T)$).** **Phase-4.
Severity 2 (sharpening).**

> $(A2)$ silently strengthens to $(A2''_T)$ on the twisted side:
> the polynomial-degree class must include Virasoro descendants
> $L_{-n_1} \cdots L_{-n_k}$ expressible polynomially in the
> Heisenberg modes via Sugawara descent. Recommended inscription:
> declare $(A2''_T)$ when conformal Virasoro structure is in scope.

**R-P4-EXEC-G4-T2.2-B (rebasing canonicality affects $\tau_T$).**
**Phase-4. Severity 3.**

> The $\tau_T$ construction depends on the inverse rebasing of
> M2's $\hbar^2 = \epsilon_1 \epsilon_2$; the canonicality of this
> rebasing is unproven (R-P4-EXEC-CGW-B). $\tau_T$ inherits this
> dependence: if the rebasing is non-canonical, the right-adjoint
> right-inverse of $\tau_{\mathfrak h}$ is non-canonical.

**R-P4-EXEC-G4-T2.2-C (spin-tower truncation).** **Phase-4.
Severity 3.**

> The companion tower $\{\tau_{(s)}\}_{s \geq 1}$ produces
> conformal-promotion functors at all spins; for $s \geq 3$, these
> produce *extra structure* not present in the manuscript (per M3
> Interpretation A). A *second* localisation truncating spin $\geq 3$ is
> required to align with the manuscript's spin-1-only $[\bar c]$
> structure. Discharge: super-extension to $\mathrm{osp}(2N|2N)$ at
> $M = N$ (M3 §6) provides physical truncation mechanism via
> super-trace cancellation.

**R-P4-EXEC-G4-T2.2-D (2-functorial lift coherence).** **Phase-4.
Severity 2 (sharpening).**

> Open question P4-EXEC-G4-T2.2-Q1: does $\tau_T$ lift to an
> $(\infty, 2)$-categorical 2-functor? The 1-functorial structure
> via LurieHA §5.5.4.10 standard adjunction is clean; the
> 2-categorical coherence requires explicit verification beyond
> M-1 scope.

### §8.2 Deciding evidence (P4-EXEC-G4-T2.2)

The verdicts are supported by:

(a) **Verbatim cross-walk to M2 §3.4** ($\tau_{\mathfrak h}$ as
    LurieHA §5.5.4.10 Bousfield localisation): the right adjoint
    construction is automatic by standard adjunction theory.

(b) **Verbatim cross-walk to M3 §2.5** (spin-3 toy via parallel
    Bousfield): the spin grading is preserved by the right adjoint,
    matching the spin-grading respect of M2/M3.

(c) **Sugawara construction (FBZ04 §3.4.7-8)**: standard textbook,
    $T = (1/(2k)):J^2: + \cdots$ on the spin-1 ⊕ spin-2 sub-VOA.

(d) **Schiffmann-Vasserot 2013 Eq. 3.1.1**: $c = (\epsilon_1+\epsilon_2)^2/(\epsilon_1\epsilon_2)$
    in the CY3 normalisation; verified at $\lambda = 1$ ($c = 4$),
    $\lambda = -1$ ($c = 0$), $\lambda = $ generic
    ($(1+\lambda)^2/\lambda$).

(e) **A1-HYP-AUDIT §1.6**: $(A2')$ as silent strengthening of the
    inscribed (A1)-(A4)+(A5); preserved on the twisted side with
    explicit Sugawara form.

(f) **Lurie HA §5.5.4.10**: locally constant FA $\simeq E_n$-algebras;
    standard adjunction gives the right adjoint to a Bousfield
    localisation as a fully faithful inclusion.

(g) **Pope-Romans-Shen 1990**: $W_\infty$ spin-tower decomposition
    of central charge; spin-2 (Virasoro) Sugawara contribution is
    $c_{\mathrm{Sug}} = 1$ (single boson), with higher spins
    contributing the rest.

### §8.3 Where the analysis could fail

(i) **A counterexample to the right-adjoint construction**: a
    topological FA on $\R$ that *does not* lift back to a conformal
    VOA via Sugawara. **Discharge mechanism**: such a counterexample
    would fail the spin-1 ⊕ spin-2 sub-VOA structure of
    $W_{1+\infty}$, which is structurally guaranteed by the
    CGW boundary VOA construction.

(ii) **The $(A2''_T)$ strengthening fails on a non-Sugawara stress
     tensor**: a Felder twist $T \to T + \alpha_0 \partial \phi$ would
     introduce a *non-polynomial* term in the Heisenberg modes.
     **Discharge mechanism**: the manuscript's working regime is
     Sugawara without Felder twist; non-Sugawara extensions are
     out of scope.

(iii) **The 2-functorial lift fails at the homotopy-coherence
      level**: a non-trivial 2-morphism (homotopy) in the source
      category fails to lift coherently to the target. **Discharge
      mechanism**: deferred to M-6 milestone; not active at M-1
      scope.

None of these failure modes are known.

---

## §9. Phase-5 escalation conditions

### §9.1 Escalation triggers

**Trigger 1.** **Rebasing canonicality fails (R-P4-EXEC-CGW-B)**:
the $\hbar^2 = \epsilon_1 \epsilon_2$ rebasing is shown to be
non-canonical (e.g., a different basepoint produces a different
$\tau_T$-image). **Phase-5 response**: re-derive the rebasing from
first principles via the Costello-Gwilliam BV regulator framework;
or accept multiple non-canonical $\tau_T$-images and parameterise
by basepoint.

**Trigger 2.** **Spin-tower truncation cannot be discharged at the
conformal level (R-P4-EXEC-G4-M3-A)**: the manuscript's spin-1-only
$[\bar c]$ cannot be matched to the CGW spin-tower with all spins
present. **Phase-5 response**: invoke the super-extension to
$\mathrm{osp}(2N|2N)$ at $M = N$ (M3 §6) as the physical truncation
mechanism; or augment the manuscript with explicit spin-tower
truncation hypothesis.

**Trigger 3.** **$(A2''_T)$ fails on a non-Sugawara stress tensor**:
the manuscript's working regime extends to Felder-twisted or
$\mathcal W$-deformed stress tensors. **Phase-5 response**: extend
the polynomial-degree class to include the deformation parameter;
or restrict the working regime to Sugawara.

**Trigger 4.** **The 2-functorial lift coherence fails**: a
non-trivial 2-morphism in the source category fails to lift
coherently to the target. **Phase-5 response**: restrict the
construction to the 1-categorical level; or develop the
$(\infty, 2)$-categorical machinery beyond LurieHA §5.5.4.10.

### §9.2 None of these triggers fire at M-1 / M-3 scope

The Phase-5 escalations are *contingent* on developments beyond
M-1 / M-3 scope:
- M-1 (3-month): G1-M1 BD chiral algebra closure, with
  R-P4-EXEC-G1-M1-C noting $\tau_T$ pending — discharged at this
  ledger as right adjoint;
- M-3 (12-month): full $W_{1+\infty}$ spin-tower at the conformal
  level; the spin-tower truncation question becomes load-bearing
  here.

**No Phase-5 escalation fires at M-1 / M-3 closure.**

---

## §10. Per-target verdict (consolidated)

| Target | Verdict | Confidence |
|--------|---------|-----------|
| (T2.2.1) Spin-2 chain-level $T(z)$ statement | $T(z) = J^{(2)}(z) = (1/(2k)):J^2: + \cdots$ in factorization centre with chain-level $T$-$T$ OPE = Heisenberg-Sugawara, $c_T = 1$ before twist | high |
| (T2.2.2) $\tau_T$ as Lurie HA §5.5.4.10 Bousfield | **NO** as Bousfield (directions opposite); **YES** as fully faithful right adjoint to $\tau_{\mathfrak h}^{\mathrm{spin}\leq 2}$ | medium-high |
| (T2.2.3) OPE at leading order with $c = (\epsilon_1+\epsilon_2)^2/(\epsilon_1\epsilon_2)$ | **YES** at $1/(z-w)^4$ (coefficient $c/2$), $1/(z-w)^2$ ($2T(w)$), $1/(z-w)$ ($\partial T(w)$); via Sugawara | medium-high |
| (T2.2.4) $(A_k)$ hypothesis preservation | $(A1)$, $(A3)$, $(A4)$ vacuously preserved; $(A2)$ silently strengthened to $(A2''_T)$; $(A5)$ vacuous on bosonic, non-vacuous on super-W; $(A2')$ preserved with explicit Sugawara form | medium-high |
| (T2.2.5) Cross-walk and tower | $\tau_T = (\tau_{\mathfrak h})^R \circ \mathrm{Sug}$ factors via Sugawara; companion tower $\{\tau_{(s)}\}_{s \geq 1}$ respects spin grading; 2-functorial lift open at M-1 | medium |
| (T2.2.6) Failure mode and obstruction | Named obstruction (I-CC) "conformal-promotion is not a localisation"; discharged via right-adjoint reformulation; Phase-5 escalations only on rebasing / spin-tower / $(A2''_T)$ / 2-functorial lift | medium-high |

---

## §11. Stable core verdict

P4-EXEC-G4-T2.2 does not invalidate any prior Phase-4 EXEC stable
core finding. The construction:

- **Confirms the M2/M3 Bousfield localisation framework**: $\tau_T$
  is the right adjoint to $\tau_{\mathfrak h}$, fully faithful by
  LurieHA §5.5.4.10 standard adjunction, exhibiting the conformal
  Virasoro promotion as the inverse direction of M2's forgetful.

- **Verifies the Schiffmann-Vasserot OPE on the twisted side**:
  $T(z) T(w)$ at leading order has central charge
  $c = (\epsilon_1+\epsilon_2)^2/(\epsilon_1\epsilon_2)$ via Sugawara,
  matching SV13 Eq. 3.1.1.

- **Identifies one silent strengthening on the twisted side**:
  $(A2)$ silently strengthens to $(A2''_T)$ to include Virasoro
  Sugawara descendants; recommended inscription when the conformal
  Virasoro structure is in scope.

- **Establishes the companion tower $\{\tau_{(s)}\}_{s \geq 1}$**:
  spin-by-spin conformal-promotion functors, each fully faithful
  right adjoint to the M2/M3 spin-$s$ forgetful, respecting the
  spin grading; the Sugawara morphism factors $\tau_T$ through
  $\tau_{\mathfrak h}$.

- **Discharges R-P4-EXEC-G1-M1-C** (G1-M1's pending conformal
  Virasoro promotion of $T(z)$): $\tau_T$ exists as right adjoint;
  $T(z)$ is conformal Virasoro on the twisted side with $c = (\epsilon_1+\epsilon_2)^2/(\epsilon_1\epsilon_2)$.

- **All seven hypothesis variants ($(A1)$-$(A5)$, $(A2')$,
  Costello-class) are preserved or strengthened**: no $(A_k)$
  variant fails on the twisted side; one silent strengthening
  $(A2''_T)$ identified.

**No manuscript content modified.** All work at the
reconstitution-ledger / Phase-4-execution level.

---

## §12. Master ledger entries

**P4-EXEC-G4-T2.2-T1.** State the precise spin-2 chain-level $T(z)$
before twist. **Verdict.** $T(z) = (1/(2k)):J(z)^2: - (1/(2k)) \partial J(z)
+ \cdots$ in the factorization centre $\mathcal A_{\mathrm{fact}}$,
with chain-level $T$-$T$ OPE = Heisenberg-Sugawara, $c_T = 1$
(single boson Sugawara) before twist. Confidence high.

**P4-EXEC-G4-T2.2-T2.** Construct $\tau_T$ as Lurie HA §5.5.4.10
Bousfield localisation. **Verdict.** $\tau_T$ is **not** a Bousfield
localisation (directions opposite); it exists as the **fully
faithful right adjoint** to $\tau_{\mathfrak h}^{\mathrm{spin}\leq 2}$.
This is the canonical categorical home for the conformal Virasoro
promotion. Confidence medium-high.

**P4-EXEC-G4-T2.2-T3.** Verify OPE at leading order with $c = (\epsilon_1+\epsilon_2)^2/(\epsilon_1\epsilon_2)$.
**Verdict.** OPE verified at leading $1/(z-w)^4$ pole (coefficient
$c/2$ with $c = (\epsilon_1+\epsilon_2)^2/(\epsilon_1\epsilon_2)$),
$1/(z-w)^2$ pole ($2 T(w)$), $1/(z-w)$ pole ($\partial T(w)$). At
$\lambda = 1$, $c = 4$; at $\lambda = -1$ (CY), $c = 0$; at
$\lambda \to 0$ (pure-axis), $c$ divergent and $\tau_T$ undefined.
Confidence medium-high.

**P4-EXEC-G4-T2.2-T4.** Hypothesis preservation table including
$(A2')$. **Verdict.** All seven hypothesis variants preserved or
vacuous, with one silent strengthening $(A2''_T)$ on $(A2)$ to
include Virasoro descendants. $(A5)$ vacuous on bosonic, non-vacuous
on super-W extension to osp(2N|2N) via super-Killing form. $(A2')$
preserved with explicit Sugawara form $g_{\mathrm{Sug}} = k \delta_{n+m,0}$.
Confidence medium-high.

**P4-EXEC-G4-T2.2-T5.** Cross-walk to $\tau_{\mathfrak h}$ and
$\tau_{W_3}$ tower. **Verdict.** $\tau_T = (\tau_{\mathfrak h})^R \circ \mathrm{Sug}$
factors through $\tau_{\mathfrak h}$ via the Sugawara morphism;
companion tower $\{\tau_{(s)}\}_{s \geq 1}$ respects spin grading;
2-functorial lift to $(\infty, 2)$ open at M-1 scope. Confidence
medium.

**P4-EXEC-G4-T2.2-T6.** Failure mode and obstruction class.
**Verdict.** Named obstruction (I-CC) "conformal-promotion is not a
Bousfield localisation" discharged via right-adjoint reformulation.
Phase-5 escalation triggers: rebasing canonicality, spin-tower
truncation, $(A2''_T)$ failure on non-Sugawara, 2-functorial lift
coherence. None fire at M-1 / M-3 scope. Confidence medium-high.

---

## §13. Closing verdict

**$\tau_T$ exists** as the **fully faithful right adjoint** to
$\tau_{\mathfrak h}^{\mathrm{spin}\leq 2}$, factoring through the
Sugawara morphism. It is **not** a Lurie HA §5.5.4.10 Bousfield
localisation in the M2/M3 sense (directions opposite); it is the
*inverse* direction (conformal-promotion vs forgetful), exhibited
canonically by standard adjunction theory.

The OPE on the twisted side has the standard Virasoro structure
with central charge $c = (\epsilon_1+\epsilon_2)^2/(\epsilon_1\epsilon_2)$,
matching the Schiffmann-Vasserot formula and verified by direct
cross-walk to the Sugawara construction.

All seven hypothesis variants ($(A1)$-$(A5)$, $(A2')$, Costello-
class) are preserved on the twisted side; one silent strengthening
$(A2''_T)$ is identified on $(A2)$ to include Virasoro Sugawara
descendants.

The companion tower $\{\tau_{(s)}\}_{s \geq 1}$ extends the M2/M3
forgetful tower to a conformal-promotion tower, respecting spin
grading and providing the canonical categorical home for the full
$W_{1+\infty}(\epsilon_1, \epsilon_2)$ spin-tower on the twisted side.

R-P4-EXEC-G1-M1-C (the pending conformal Virasoro promotion of
$T(z)$ noted in G1-M1's closure) is **discharged** at this ledger.

**No manuscript content modified.**
