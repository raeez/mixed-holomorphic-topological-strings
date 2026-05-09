# Wave 3 / W5 — Kazhdan + Functoriality lens (Raeez Lorgat)

**Date.** 2026-04-28.
**Author.** Raeez Lorgat.
**Wave.** 3.
**Lens.**
- *Primary:* Kazhdan — rigidity, categorical representation theory,
  hidden equivalences, obstruction by known structure.
- *Secondary:* Functoriality — are maps natural? Are choices canonical
  or merely chosen?

**Mandate.** Attack the
$[\mathrm{Tr}\,\psi]_{\mathrm{BV}}\leftrightarrow[\bar c]_{\mathrm{CE}}$
identification (master entry **M-31**) for naturality holes.

---

## §0. Summary

W5 finds the M-31 identification **valid as a line-level equality of
distinguished anomaly classes, but not natural under the full
Symp$_{\mathrm{form}}(\widehat{\C^2}_0)$ action**. The identification
is canonical only up to an undetermined scalar $c\in\C^\times$, exactly
the M-28 / D₂ T$^2$-Cartan rigidity scalar, and only on the
GL$_2\times T^2$ subgroup of formal symplectomorphisms. The closed side
$[\bar c]\in H^2_{\mathrm{Lie}}(\bar A;\C)$ is
Symp$_{\mathrm{form}}$-canonical (a weight-(0,0) one-dimensional
cohomology line), but the open side $[\mathrm{Tr}\,\psi]_{\mathrm{BV}}$
lives on the Dirac probe substitution $z_i\rightsquigarrow\phi_i$,
which is functorial only for **linear** symplectomorphisms (matrix
substitution does not commute with non-linear coordinate changes). The
two sides have **different equivariance groups**, and M-31 is the
restriction of the identification to their intersection. This is
**not a defect** — it is a sharper classification — but the
manuscript's wave-2 W3-03 phrasing ("the same line viewed from CE/PV's
two sides") risks being read as a Symp$_{\mathrm{form}}$-natural
statement.

W5 proposes four ledger entries (W3-W5-01 through W3-W5-04) and
recommends two minimal sharpening edits to the M-31 narration.

**Verdict on M-31.** Confirmed at the line level; **per-equivariance
classification** required to state the identification cleanly. Stable
core unchanged.

**Verdict on stable core.** Wave-3 stable core after this attack:
M-26, M-27, M-28, M-29, M-30, M-31 (with the
naturality classification below), M-32, M-33, M-34, M-35, M-36, M-37
all stand. No master entry is overturned. M-31 acquires
**W3-W5-04** as a sharpening on per-equivariance naturality, in
parallel to how M-35 sharpens M-04 / M-05 with the per-theorem
classification.

---

## §1. Kazhdan rigidity attacks on M-31

### W3-W5-01 — The U(1) anomaly moduli is rigid: one C^× scalar
**Severity 2 (rigidity confirmation). Status valid. Confidence high.**
**Lens.** Kazhdan (rigidity) + Functoriality (canonicity).
**Provenance.** This wave; cross-link M-09, M-28 D₂, M-31, M-35
Theorem G classification.
**Target.** `main.tex`:284–316 (Lemma~\ref{lem:omega-cocycle}); 318–351
(Theorem~\ref{thm:u1-center-anomaly}); 412–464
(Theorem~\ref{thm:quantum-classical-anomaly}).

**Question.** Is the U(1) action that produces the Capelli anomaly
**rigid** — only one such anomaly up to isomorphism — or is there a
moduli of consistent U(1) anomalies, in which case the manuscript's
$[\bar c]$ is one chosen point?

**Result (rigid).** The M-09 weight-bidegree decomposition lemma —
combined with the proof of $\omega$'s nontriviality at
`main.tex`:300–316 and the M-28 / D₂ T$^2$-Cartan rigidity for
T$^2$-equivariant $H^2$ classes — **forces the entire moduli of
consistent T$^2$-equivariant scalar U(1) anomalies on
$\bar A=\C[z_1,z_2]/\C\cdot 1$ to be one-dimensional**. Specifically:

1. $\omega$ is concentrated in bidegree $(k+m-1,l+n-1)=(0,0)$, i.e.
   pairs $(k,l),(m,n)$ with $(k+m,l+n)=(1,1)$ (proof at
   `main.tex`:280–282 + Lemma~\ref{lem:omega-cocycle}).
2. Inside this single bidegree, $\omega(z_1^kz_2^l,z_1^mz_2^n)=
   (kn-lm)$ has the unique antisymmetric T$^2$-Cartan
   $(\mathrm{wt}(z_1)=(1,0),\mathrm{wt}(z_2)=(0,1))$-equivariant
   normalization up to one scalar.
3. Killing the constant line $\C\cdot 1$ removes the only candidate
   primitive ($\eta(f)=-[f]_0$ does not descend), so the cohomology
   class $[\bar c]\in H^2_{\mathrm{Lie}}(\bar A;\C)$ is genuine and
   one-dimensional.

**Consequence for M-31.** $[\bar c]$ is rigid up to the M-28 / D₂
$c\in\C^\times$ scalar. The corresponding open-side class
$[\mathrm{Tr}\,\psi]\in H^{-1}(\C[\phi_1,\phi_2]\otimes\Lambda(\psi),Q)$
inherits the rigidity through the boundary evaluation map
$\partial_{\mathrm{bb},N}^{\mathrm{full}}$ at
`main.tex`:362–369. The identification
$[\mathrm{Tr}\,\psi]_{\mathrm{BV}}\leftrightarrow[\bar c]_{\mathrm{CE}}$
is therefore the unique nontrivial line-to-line correspondence between
the two distinguished one-dimensional sub-quotients up to the
**same** scalar.

**Evidence type.** verification (M-09 weight-bidegree lemma); proof
chain (Lemma~\ref{lem:omega-cocycle} + M-28 D₂ T$^2$-Cartan rigidity).
**Files read.** `main.tex` 247–472; `principles.tex` lines 132–155;
ledger M-09, M-28, M-31, M-35.
**Confidence.** High.
**Blast radius.** None — this strengthens M-31's identification; the
underlying lift remains Obligation I.
**Minimal heal.** Optional: add one-sentence remark to
`thm:u1-center-anomaly` proof noting the M-28 D₂ rigidity.
**Residual.** None for the rigidity claim.
**Adjudication.** Valid rigidity classification.

---

### W3-W5-02 — Hidden-equivalence audit: A ↔ E independence

**Severity 2 (categorical). Status valid (with caveat). Confidence
medium-high.**
**Lens.** Kazhdan (hidden categorical equivalence).
**Provenance.** This wave; cross-link M-31, M-33 (eight-link DAG),
`thm:open-closed-derived-center` (cochain) and
`thm:open-closed-derived-center-factorization` (FA).

**Question.** Are A (CE/PV cochain-level derived-centre) and E
(factorization-centre identification) actually independent, or is one a
consequence of the other under a hidden equivalence the manuscript
misses?

**Result (not independent at line level; independent at proof-technique
level).** Under M-33's eight-link DAG verification, the FA-level theorem
$\mathrm{thm:open-closed-derived-center-factorization}$ at
`main.tex`:1997–2080 reduces, on a contractible open of the brane line
$\R$, to the cochain-level CE/PV statement
$\mathrm{thm:open-closed-derived-center}$ at `main.tex`:2322–. The eight
links L1–L8 promote the cochain identity to the locally constant FA
equivalence; the cochain identity itself is the L1 + L3 ingredient.

**Hidden-equivalence test.** The Kazhdan rigidity question is whether
M-31's identification of the BV avatar with the CE class on each side
is itself a *consequence* of a higher categorical equivalence between
the two factorization-algebras (open and closed). Two cases:

1. **At the line level (anomaly classification).** Yes —
   $[\mathrm{Tr}\,\psi]_{\mathrm{BV}}$ on the open side and
   $[\bar c]_{\mathrm{CE}}$ on the closed side are matched
   automatically by Theorem~\ref{thm:open-closed-derived-center} once
   one names them as the "distinguished anomaly line on each side."
   M-31 makes this matching explicit; it does not require a new
   theorem. **A and E are not independent at this line level.**

2. **At the cochain / factorization-centre level.** The full bridge
   $[\mathrm{Tr}\,\psi]_{\mathrm{BV}}\xleftrightarrow{\text{q.i.}}
   [\bar c]_{\mathrm{CE}}$ at the factorization-centre quasi-isomorphism
   level is **not** a consequence of A or E; it is exactly Obligation I
   (unreduced BV factorization-centre lift). **A and E are independent
   in the sense that neither implies Obligation I.**

**Consequence for M-31.** The identification is "line-level
free" but "quasi-isomorphism-level Obligation I." This matches the
wave-2 W3-03 phrasing exactly. **No hidden equivalence is missed**,
because the manuscript already separates the line-level identification
(in M-31 and the wave-3 narration) from the cochain/FA-level lift
(Obligation I).

**Caveat.** A reader could mistake M-31 for asserting a quasi-isomorphism
between BV-cohomology and CE-cohomology on the basis of the line
identification. The recommended sharpening is one numbered remark in
the Theorem G area (around `main.tex`:393) explicitly distinguishing
**line-level free identification** from **cochain-level Obligation I
lift**.

**Evidence type.** verification (M-33 DAG + cochain/FA decomposition).
**Files read.** `main.tex` 1997–2080, 2322–2470; ledger M-31, M-33;
`reconstitution/wave2-W3-witten-2026-04-28.md` §W3-03.
**Confidence.** Medium-high.
**Blast radius.** None on the proof; one prose-level sharpening.
**Minimal heal.** One-sentence sharpening of the Theorem G area
narration to explicitly separate the two levels.
**Residual.** Obligation I — already named.
**Adjudication.** Valid hidden-equivalence classification.

---

### W3-W5-03 — Symp$_{\mathrm{form}}$ rescaling functoriality of M-31

**Severity 2 (functoriality). Status valid with classification. Confidence
high.**
**Lens.** Kazhdan + Functoriality.
**Provenance.** This wave; cross-link M-31, M-35 Theorem G classification,
M-29 Lie-Mod equivariance.

**Question (rescaling).** Under $\hbar\mapsto\lambda\hbar$ for
$\lambda\in\C^\times$, does the M-31 identification scale correctly?

**Result.** Yes, with explicit scalar tracking:

1. $[\mathrm{Tr}\,\psi]_{\mathrm{BV}}$ has $\hbar$-degree $0$ — it is
   the classical chain-level avatar of the derived intersection (W3-01
   N=2 verification confirms; the BV differential
   $Q\psi=[\phi_1,\phi_2]$ has no $\hbar$).
2. $[\bar c]_{\mathrm{CE}}$ has $\hbar$-degree $0$ as a CE class on
   $\bar A$; its quantum incarnation
   $\hbar N\cdot[\bar c]$ (Theorem~\ref{thm:quantum-classical-anomaly},
   `main.tex`:412–464) carries $\hbar$-weight $1$ via the Capelli
   shift.
3. Under $\hbar\mapsto\lambda\hbar$, the Capelli shift scales as
   $\hbar N\mapsto\lambda\hbar N$, so the Rees-deformation Lie cocycle
   on $U_\hbar(\bar A_{[\bar c]})$ scales by $\lambda$. The
   classical-to-quantum identification at `main.tex`:430–434 is
   $\C[[\hbar]]$-linear and respects this scaling.
4. The identification
   $[\mathrm{Tr}\,\psi]\leftrightarrow[\bar c]$ at the **classical
   $\hbar=0$ line** is independent of $\lambda$; the
   identification at the **quantum $\hbar\neq 0$ line** scales as
   $\lambda$.

**Consequence.** Rescaling $\hbar\mapsto\lambda\hbar$ multiplies both
sides of the identification by the same $\lambda$ at the quantum
level, and leaves both sides invariant at the classical level.
M-31 is therefore **rescaling-natural up to the unique
$c\in\C^\times$ scalar of M-28 D₂**. There is no extra scaling
ambiguity beyond this single overall normalization.

**Question (formal symplectic frame change).** Under
$\Sympform(\widehat{\C^2}_0)$, does the identification commute with the
induced action on each side?

**Result (per-equivariance classification, not full
Symp$_{\mathrm{form}}$-natural).** This is the load-bearing
naturality finding.

- **Closed side.** $\Sympform(\widehat{\C^2}_0)$ acts on
  $\mathfrak h_{\mathrm{poly}}$ by formal substitution
  $f\mapsto f\circ\varphi^{-1}$ for $\varphi$ a formal
  symplectomorphism. The bracket
  $\{f,g\}=\partial_{z_1}f\,\partial_{z_2}g-\partial_{z_2}f\,\partial_{z_1}g$
  is intrinsic to $\omega=dz_1\wedge dz_2$, hence $\Sympform$-invariant.
  The cocycle $\omega(f,g)=[\{f,g\}]_0$ uses the constant Taylor
  coefficient projection at the origin, which IS $\Sympform$-equivariant
  (constants are intrinsic), so $[\bar c]$ is genuinely
  $\Sympform$-canonical (this matches M-35's classification of Theorem G
  as "Symp$_{\mathrm{form}}$-canonical").
- **Open side.** The Dirac probe substitution $z_i\rightsquigarrow\phi_i$
  at `principles.tex`:21–24 is **linear** in $z_1,z_2$. Non-linear
  $\varphi\in\Sympform$ does not commute with substitution into
  matrices: $\varphi(z_1)$ is a power series in $z_1,z_2$, and
  $\varphi(z_1)(\phi_1,\phi_2)$ requires an ordering convention for
  matrix powers. Cyclic-trace inequality
  $\mathrm{Tr}(\phi_1^a\phi_2^b)\neq\mathrm{Tr}(\phi_2^b\phi_1^a)$ in
  the unreduced ring. Hence the substitution map is functorial only for
  the **linear** subgroup, $\mathrm{GL}_2 \subset \Sympform$, which acts on
  the matrices $\phi_i$ by the same linear change of variables.
- **Identification commutes for GL$_2$ \boldmath$\times$ T$^2$ only.**
  M-35's classification of Theorem A as **GL$_2$-only** matches
  exactly. The W3-03 mechanism — constant-Hamiltonian removal $\leftrightarrow$
  empty-trace removal — is GL$_2$-equivariant: linear changes of
  variables on $z_1,z_2$ pull back to linear changes on $\phi_1,\phi_2$
  and preserve both removals.

**Per-equivariance table (M-31 specifically).**

| Group | Acts non-trivially on | Identification commutes? |
|---|---|---|
| $\mathrm{GL}_2$ (linear symplectic) | both sides | **yes** |
| $T^2$ (Cartan torus) | both sides; bidegree (0,0) line invariant | **yes** |
| Full $\Sympform(\widehat{\C^2}_0)$ | closed side acts on $\bar A$; open side is GL$_2$-only | **no** — only GL$_2 \times T^2$ subgroup |
| $\hbar$-rescaling $\C^\times$ | both sides at quantum level; multiplies by $\lambda$ | **yes** (uniform scale) |

**Consequence.** M-31 is **GL$_2 \times T^2$-natural and
$\hbar$-rescaling-natural**, but **not $\Sympform$-natural** in the
sense that the open-side substitution map is not functorial for
non-linear $\varphi$. This is *not* a defect: it is the per-equivariance
sharpening of the M-31 narration parallel to M-35's per-theorem
classification.

**Evidence type.** verification (`principles.tex` substitution map
inspection); cross-link (M-35 Theorem A GL$_2$-only).
**Files read.** `principles.tex`:11–54; `main.tex`:863–875,
4040–4239; ledger M-35.
**Confidence.** High.
**Blast radius.** None on proofs; one prose paragraph in the M-31
narration.
**Minimal heal.** Add a per-equivariance sentence to M-31's heal:
"M-31 is GL$_2 \times T^2$-natural and $\hbar$-rescaling-natural; the
open side is GL$_2$-only by M-35 Theorem A, restricting the full
identification to the GL$_2 \times T^2$ subgroup of
$\Sympform$." Mirror the same sentence in the manuscript's Theorem G
narration if/when M-31 is inscribed.
**Residual.** None for naturality classification.
**Adjudication.** Valid functoriality classification.

---

### W3-W5-04 — Choice of representatives: canonical vs silently chosen

**Severity 1 (canonicity). Status: silent choice flagged. Confidence
high.**
**Lens.** Functoriality (canonicity of representatives).
**Provenance.** This wave; cross-link
Lemma~\ref{lem:omega-cocycle},
Theorem~\ref{thm:u1-center-anomaly-open}, M-31 W3-03.

**Question.** Is the choice of representative in each cohomology class
canonical, or did the manuscript silently pick lifts?

**Result (silent but well-motivated choices).**

- **Closed side (canonical up to scalar).** The cocycle representative
  $\omega(f,g)=[\{f,g\}]_0$ is the **unique** T$^2$-Cartan equivariant
  bilinear form in bidegree (0,0) up to scalar (M-28 D₂ rigidity +
  M-09 weight-bidegree). Choice of overall scalar $c\in\C^\times$ is
  silent in the manuscript but exhibited explicitly in
  Theorem~\ref{thm:u1-center-anomaly-open} via
  $\{\mathrm{Tr}\,\phi_1,\mathrm{Tr}\,\phi_2\}=N$ (`main.tex`:359), pinning
  $c=1$ canonically against the boundary trace pairing. **Canonical
  after the M-28 / D₂ scalar is fixed.**

- **Open side (representative chosen from a 1-parameter family).** The
  chain-level avatar $\mathrm{Tr}\,\psi$ at `main.tex`:1003 is one of
  many Q-closed chain-level cycles in the cohomology class
  $[\mathrm{Tr}\,\psi]\in H^{-1}(\C[\phi_1,\phi_2]\otimes\Lambda(\psi),Q)$.
  Other Q-closed cycles include $\mathrm{Tr}\,\psi\,p(\phi_1,\phi_2)$
  for any commuting polynomial $p$ in the ideal of cyclic relations,
  or smeared versions $\int_\R a(t)\,\mathrm{Tr}\,\psi(t)\,dt$ for
  $a\in\Omega^0_c(\R)$. The empty-trace stratum (constant $p=1$, no
  smearing) is the **most natural choice** because:

  1. It pairs canonically against the open-side Chan-Paton central
     line $\C\cdot I=\C\cdot\mathrm{Tr}(1)\subset\mathfrak{gl}_N$.
  2. It corresponds, under the boundary evaluation map at
     `main.tex`:362–369, to the constant-Hamiltonian generator $1\in
     \mathfrak h_{\mathrm{poly}}$ removed in passing to $\bar A$.
  3. It is the unique GL$_2 \times T^2$-equivariant chain-level
     representative of weight $(0,0)$ and BV-degree $-1$ that pairs
     non-trivially against the empty-trace Chan-Paton scalar.

  However, the canonicity of these three properties **as a
  characterization** of the chosen representative is not stated in the
  manuscript: it is silent.

**Consequence.** Both sides of M-31 use canonical-after-pinning choices.
The closed side is pinned by Theorem~\ref{thm:u1-center-anomaly-open}
($c=1$ via $\{\mathrm{Tr}\,\phi_1,\mathrm{Tr}\,\phi_2\}=N$). The open
side is pinned by GL$_2\times T^2$-equivariance, weight (0,0), and
non-triviality against the Chan-Paton scalar. No moduli of free
choice survives once these pinning conditions are stated.

**Minimal heal.** One numbered remark — call it
`rmk:M-31-canonical-representatives` — in the Theorem G area
(around `main.tex`:393), summarizing:

> *The closed-side representative $\omega(f,g)=[\{f,g\}]_0$ is the unique
> T$^2$-Cartan equivariant bilinear bidegree-(0,0) cocycle up to
> $c\in\C^\times$, pinned to $c=1$ by
> Theorem~\ref{thm:u1-center-anomaly-open}. The open-side
> representative $\mathrm{Tr}\,\psi$ at the empty-trace stratum is the
> unique GL$_2\times T^2$-equivariant weight-(0,0) BV-degree-$(-1)$
> chain-level avatar pairing non-trivially against the Chan-Paton
> scalar $\C\cdot\mathrm{Tr}(1)$. The M-31 identification is the
> resulting canonical line-to-line correspondence on the GL$_2\times
> T^2$-equivariant subcategory.*

**Evidence type.** verification (cocycle-class uniqueness);
proof_chain (boundary evaluation pinning).
**Files read.** `main.tex` 247–472, 1003, 2858–2906;
`appendix-unreduced-bv-qme.tex`:93–158; ledger M-09, M-28 D₂.
**Confidence.** High.
**Blast radius.** Editorial only.
**Adjudication.** Valid canonicity flag.

---

## §2. Functoriality audit of M-26, M-29 alongside M-31

### M-26 (5-way C₁/C₂ split)

Each of the five named theorems C₁ᶠʷ, C₁ᶜᵒᵐᵖ, C₂(NT), C₂(W), C₂(R)
has its own equivariance group:

- C₁ᶠʷ (finite-word, hypothesis-free): $\Sympform$-natural at the level
  of CE words, since the Lie bar-cobar generator identity is
  intrinsic.
- C₁ᶜᵒᵐᵖ (completed, symmetric-filtration hypothesis): $\Sympform$-natural
  if the symmetric filtration is preserved by $\varphi$; in the formal
  symplectic disk Cartan-grading is preserved automatically.
- C₂(NT) (nilpotent truncation on $\mathfrak m^3$): $\Sympform$-natural
  in the sense that $\mathfrak m^3$ is intrinsic.
- C₂(W) (weighted Tate, enlarged coefficient category): natural for the
  weight-respecting subgroup of $\Sympform$, i.e. roughly
  $\GL_2 \subset \Sympform$ that preserves the weight structure
  $\mathrm{wt}(z_1)+\mathrm{wt}(z_2)$.
- C₂(R) (regulator-independent finite-window): natural for the
  regulator-respecting subgroup.

**M-31 connection.** M-31's identification proceeds through
Theorem C (CE/PV) and depends on whichever C-flavor is invoked. In
the formal symplectic disk specialization, all five flavors agree
(M-26's claim), so M-31 is C-flavor-independent in the local model.
**M-31 is GL$_2 \times T^2$-natural across all five C-flavors.**

### M-29 (universal categorical no-go for Obligation II)

This is a Lie-Mod statement on $\bar A$-modules; it is fully
$\Sympform$-equivariant since $\bar A$ is the intrinsic
scalar-reduced Hamiltonian Lie algebra and the no-go is a property of
the module category, not the realization. **Fully
$\Sympform$-natural.**

**M-31 connection.** M-29 closes the categorical extension question
in the negative; M-31 supplies the corresponding line-level avatar
identification. M-29 is $\Sympform$-natural; M-31 is GL$_2 \times
T^2$-natural; the **identification of M-29's bi-infinite parent
module with the M-31 anomaly-line classification** would require
extending M-31 to the full $\Sympform$ subcategory by replacing the
substitution-map open side with a Costello-graph-compatible variant
or a chiral / vertex-algebra realization. **This is Phase-4
research**, parallel to M-29's own R-W4-A and R-W4-B residuals.

---

## §3. Verdict on M-31 and stable core

**Verdict on M-31 identification's naturality.**

- **Line-level identification:** confirmed valid (W3-W5-01, W3-W5-02).
  $[\mathrm{Tr}\,\psi]_{\mathrm{BV}}\leftrightarrow[\bar c]_{\mathrm{CE}}$
  is the unique line-to-line correspondence between the two
  distinguished one-dimensional sub-quotients up to the M-28 / D₂
  scalar $c\in\C^\times$.

- **Equivariance classification (per-equivariance, parallel to
  M-35).** M-31 is GL$_2 \times T^2$-natural and
  $\hbar$-rescaling-natural; **not** $\Sympform$-natural in general
  (W3-W5-03). This is the open-side restriction of substitution-map
  functoriality to the linear subgroup.

- **Canonical representatives.** Closed-side $\omega$ is unique up to
  scalar, pinned to $c=1$ by the boundary trace pairing
  $\{\mathrm{Tr}\,\phi_1,\mathrm{Tr}\,\phi_2\}=N$. Open-side
  $\mathrm{Tr}\,\psi$ at the empty-trace stratum is unique under
  GL$_2 \times T^2$-equivariance, weight $(0,0)$, and Chan-Paton
  pairing non-triviality (W3-W5-04). Both sides are
  canonical-after-pinning.

- **Hidden equivalence audit.** A and E are **not independent at the
  line level**, but **independent in proof technique and at the
  cochain/FA level** (W3-W5-02). The manuscript's separation is well
  justified.

**M-31 stands** with the addition of W3-W5-03 and W3-W5-04 as a
naturality classification entry.

**Verdict on stable core.** All twelve wave-2 master entries
(M-26 through M-37) survive the W5 Wave-3 attack. M-31 acquires a
per-equivariance sharpening (W3-W5-03) and a canonical-representatives
remark (W3-W5-04); these are editorial improvements, not defects.
**Stable core unchanged.**

---

## §4. Proposed ledger entries for inscription

| ID         | Severity | Lens                      | Action                                                                                                                                                                              |
|------------|----------|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| W3-W5-01   | 2        | Kazhdan + Functoriality   | Confirm rigidity of U(1) anomaly moduli at one C^× scalar via M-09 weight-bidegree + M-28 D₂ T²-Cartan rigidity; optional one-sentence remark in `thm:u1-center-anomaly` proof.       |
| W3-W5-02   | 2        | Kazhdan                   | Hidden-equivalence audit: A/E independent at proof-technique level, dependent at line level; one-sentence sharpening in Theorem G area separating line vs cochain/FA-level.          |
| W3-W5-03   | 2        | Kazhdan + Functoriality   | Add per-equivariance sentence to M-31 narration: GL$_2 \times T^2$-natural and ℏ-rescaling-natural; not full $\Sympform$-natural (open side GL$_2$-only).                              |
| W3-W5-04   | 1        | Functoriality             | Add `rmk:M-31-canonical-representatives` in Theorem G area pinning closed and open representatives.                                                                                  |

All four are editorial; no new theorems, no new proofs required. They
mirror M-35's per-theorem classification pattern and the M-28 / D₂
T²-Cartan rigidity argument.

---

## §5. Provenance

W5 (Wave 3) read:

- `/Users/raeez/topological-strings/CLAUDE.md`.
- `/Users/raeez/topological-strings/reconstitution/attack-heal-platonic-2026-04-28.md` §A entries M-26 through M-37 and §B cross-walk.
- `/Users/raeez/topological-strings/reconstitution/wave2-W3-witten-2026-04-28.md` (full).
- `/Users/raeez/topological-strings/reconstitution/wave2-W5-polyakov-crossvolume-2026-04-28.md` (full).
- `/Users/raeez/topological-strings/principles.tex` (full).
- `/Users/raeez/topological-strings/appendix-unreduced-bv-qme.tex` (full).
- `/Users/raeez/topological-strings/main.tex` lines 240–472 (Theorem G area), 820–908 (formal Darboux + global restriction), 1003 (Tr ψ exclusion site), 1997–2080
  (`thm:open-closed-derived-center-factorization`), 2322–2470
  (`thm:open-closed-derived-center` cochain), 2858–2906, 3040–3085 (PBW
  bidegree label),  4040–4239 (Theorem E neighborhood: descendant
  module + categorical no-go + boundary-local-dual construction).

External references invoked: M-09 weight-bidegree decomposition lemma;
M-28 D₂ T²-Cartan rigidity; M-35 Theorem A GL$_2$-only and Theorem G
$\Sympform$-canonical classification; Costello *RenEFT* §5.3 (regularization
preserves U(1)$_{\mathrm{ghost}}$ as in M-32); Henneaux–Teitelboim
§18.3 (regularization-compatibility vs anomaly-cancellation).

W5 confidence: every claim checked against the cited line numbers in
the manuscript and the wave-2 ledger entries. No new theorems
proposed; only naturality classification.

End of W5 Wave-3 ledger.
