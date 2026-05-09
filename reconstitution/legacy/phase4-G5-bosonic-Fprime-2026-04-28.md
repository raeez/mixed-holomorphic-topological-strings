# Phase-4 / G5 — Bosonic F$'$ unconditionalization research outline

**Date.** 2026-04-28. **Author.** Raeez Lorgat (G5 research initiator,
Phase-4).
**Lens.** Costello (factorization, BV/BRST, renormalization) primary;
Composition (associativity, transactional coherence) secondary;
Witten (physical consistency, dualities) tertiary.
**Mode.** Proposal-only; research outline. Master ledger schema; IDs
prefix `P4-G5-`.
**Posture.** Wave 3 has CERTIFIED CONVERGED. F$'$ is unconditional on
the super-balanced $\mathfrak{gl}(N|N)$ source via W22-T1 + W22-T2
(chain-level + all-loop) and W30 (admissible-class condition (A5)
parity-equivariance verified for all manuscript-cited regulators).
The bosonic source remains conditional. G5's Phase-4 mandate: outline
the research program for unconditionalizing F$'$ on the **bosonic**
source, including precise statements of the desideratum, three escape
routes beyond super-balancing, source-change candidates, and a
milestone ladder with Phase-5 criteria.
**Inputs.** `wave3-W22-supertrace-rigorous-2026-04-28.md`
(W22-T1, W22-T2, W22-Obs); `wave3-W10-witten-examples-2026-04-28.md`
(W3-W10-01: bosonic one-loop QME = $\hbar N$);
`wave3-W15-conditional-theorems-2026-04-28.md`
(F$'$ / G boundary; F$'$-blast-radius);
`wave3-W6-costello-composition-2026-04-28.md`
(R-W3-W6-05: C$_2$(W)-q gating);
`wave3-W18-thmB-escape-routes-2026-04-28.md`
(W18-T4 central-character; W18-T5 unreduced primitive; W18-CT2/C3);
`wave3-W30-A5-heal-2026-04-28.md` ((A5) parity-equivariance);
`wave3-W36-skeptic-2026-04-28.md` (S1 vs S2/S3 super-balanced scope);
`appendix-unreduced-bv-qme.tex` (full).

---

## §0. Executive verdict

**Three named verdicts, ordered by weight.**

1. **The bosonic-F$'$ obstruction is structural and load-bearing, not
   technical.** W3-W10-01 closed `prob:weighted-rg-locality` in the
   negative on the unreduced bosonic $\mathfrak{gl}_N$ scalar-reduced
   Hamiltonian source: the one-loop QME obstruction class is exactly
   $\hbar N[\bar c]$, equal to Theorem G's Capelli central anomaly.
   The obstruction is regulator-independent inside the admissible
   class (W3-W6-04), so no choice of regulator scheme inside the M-26
   admissible envelope can clear it. The bosonic-F$'$ obstruction is
   therefore **not a hypothesis** to be checked or removed by a
   careful proof — it is **the same anomaly class** that gates
   Theorem G. Any unconditionalization route must change the source,
   change the obstruction class, or build a parallel factorization
   theory. **`P4-G5-V1`**.

2. **W18-T4 (central character) is RESOLVED-INTO-EXISTING; W18-C3
   (unreduced primitive) is PHASE-4 CONJECTURE; source-change beyond
   super-balanced is PHASE-4/5.** W18-T4 found that the
   $\hbar$-deformed central character $\chi_\hbar$ with
   $\chi_\hbar(\mathrm{Tr}\,I)=0$ is informationally equivalent to the
   manuscript's existing Capelli/Weyl renormalized stable trace
   (`lem:capelli-renormalized-stable-trace`). The character "escape"
   is the Capelli counterterm under another name; it does **not**
   open a new vanishing class on the bosonic source. The unreduced-
   primitive route (W18-C3) and source-change candidates ($\mathfrak{osp}$,
   $\mathfrak{gl}_{\infty|\infty}$, etc.) remain genuine Phase-4
   options. **`P4-G5-V2`**.

3. **The honest milestone ladder runs 3, 6, 12, 18+ months; the
   Phase-5 criterion is reached if all three Phase-4 routes
   (unreduced-primitive, source-change beyond super-balancing,
   parallel-factorization-on-$\mathfrak{h}_{\mathrm{poly}}$) close
   in the negative.** The criterion for declaring bosonic F$'$
   Phase-5 is structural: **any of the Phase-4 routes opening a new
   theorem candidate keeps F$'$ in Phase-4; all three closing in the
   negative escalates to Phase-5** (requiring fundamentally new
   technique, e.g., a categorical reformulation of the constant-
   Hamiltonian sector or a derived-CY framework for the BCOV
   bosonic source). **`P4-G5-V3`**.

**Bottom line.** Bosonic-F$'$ is hard for **structural** reasons;
the one-loop class is exactly $\hbar N[\bar c]$, and Theorem G
*classifies* this anomaly as non-vanishing on the bosonic source.
The Phase-4 program named here is honest about what each route can
achieve and where each fails; the Phase-5 criterion is reached only
if all three routes definitively close in the negative.

---

## §1. T1 — Why bosonic F$'$ fails: the precise obstruction class

### `P4-G5-T1-01` — The one-loop diagram with bosonic trace

**Severity 4 (load-bearing). Status valid (per W3-W10-01).
Confidence high.**
**Provenance.** Mandate T1 of G5 prompt; cross-link W3-W10-01.

**Verbatim restatement.** On the bosonic $\mathfrak{gl}_N$ Dirac probe
of the formal symplectic disk $(\widehat{\C^2}_0, dz_1\wedge dz_2)$,
with normal coordinates $\phi_1,\phi_2\in\mathfrak{gl}_N$ and Koszul
antifield $\psi\in\mathfrak{gl}_N$ ($Q\psi=[\phi_1,\phi_2]$):
- **Propagator-loop closure.** $\sum_{i,j}\delta^i_j\delta^j_i=N$.
- **One-loop QME diagram.** Gauge-generator tadpole giving anomaly
  $\hbar\cdot\mathrm{Tr}_{\mathfrak{gl}_N}(I)=\hbar\cdot N$.
- **Obstruction class.** $\hbar N[\bar c] \in
  H^1(\mathcal O_{\mathrm{loc}}(\mathcal E_w), Q+\{I_0,-\})$,
  non-zero for every $N\geq 1$.

**Identification with Theorem G.** The class $\hbar N[\bar c]$ is
exactly the Capelli central anomaly of Theorem G
(`thm:u1-center-anomaly`, `main.tex`:280–470). M-31 records this:
$[\mathrm{Tr}\,\psi]_{\mathrm{BV}}\leftrightarrow N\cdot[\bar c]_{\mathrm{CE}}$
on the bosonic source. The QME obstruction governing F$'$ and the
U(1) anomaly of Theorem G are **the same class**, viewed from BV
and CE sides.

**The obstruction class is regulator-class-canonical.** By
W3-W6-04 + W3-W30, the obstruction class $\hbar N[\bar c]$ is
preserved by every admissible regulator inside the (A1)–(A5) class.
A change of regulator scheme inside the admissible class does
**not** clear it. (A5) parity-equivariance is vacuous on the
bosonic source (no $\Z/2$-grading), so it imposes no constraint;
the bosonic obstruction is therefore *robust* against admissible-
class deformations.

**Files read.** `wave3-W10-witten-examples-2026-04-28.md` 105–195
(W3-W10-01); `appendix-unreduced-bv-qme.tex` 93–158
(`prop:app-scalar-contact-qme-class`); `wave3-W30-A5-heal-2026-04-28.md`
75–84 ((A5) vacuous on bosonic).
**Confidence.** High.
**Adjudication.** Valid. The bosonic-F$'$ obstruction class is
exactly $\hbar N[\bar c]$, equal to Theorem G's Capelli anomaly,
preserved by every admissible regulator. Any unconditionalization
route must (i) change the source so that $\mathrm{Tr}(I)=0$, or
(ii) change the obstruction class (e.g., by lifting to an unreduced
primitive on $\mathfrak h_{\mathrm{poly}}$), or (iii) build a
parallel factorization theory in which $[\bar c]$ is exact.
**Residual.** None at the obstruction-class layer; the structural
class is well-identified.

---

## §2. T2 — Three escape routes (beyond super-balanced)

### `P4-G5-T2-01` — Route (a): central character W18-T4 — STATUS: RESOLVED-INTO-EXISTING

**Severity 3. Status valid; route does NOT open new candidate.
Confidence high.**
**Provenance.** Mandate T2(a) of G5 prompt; cross-link W3-W18-04.

**W18-T4 verdict.** The central character $\chi:Z(\widehat U(\mathfrak{gl}_N))\to\C$
satisfying $\chi(\mathrm{Tr}\,I)=0$ exists at the augmentation
character $\chi_0$. To absorb the $\hbar N$ Capelli shift, the
character must be $\hbar$-deformed: $\chi_\hbar(\mathrm{Tr}\,I)=0$
quantum, but $\chi^{\mathrm{cl}}(\mathrm{Tr}\,I)=N$ classical. This
$\hbar$-deformation **is** the Capelli counterterm
(`lem:capelli-renormalized-stable-trace`, `main.tex`:4821–4900). The
"central-character escape" therefore reduces to the manuscript's
existing Weyl renormalization; it does **not** open a new vanishing
class on a different source.

**Verdict.** Route (a) is **resolved into the manuscript's existing
Capelli normalization**; it is **not** an escape from bosonic-F$'$.

**Status update on W18-T4.** The G5 prompt asks "verify status." The
status is: **RESOLVED-INTO-EXISTING** (per W18-T4 / W3-W18-04).
The route does not require Phase-4 work on the bosonic source; it
is structurally circular.

**Adjudication.** Valid status check. Route (a) closed; it is the
Capelli counterterm under another name.
**Residual.** None.

---

### `P4-G5-T2-02` — Route (b): unreduced-primitive W18-C3 — STATUS: PHASE-4 CONJECTURE

**Severity 4 (Phase-4 conjecture). Status open; conjecture-grade.
Confidence medium.**
**Provenance.** Mandate T2(b) of G5 prompt; cross-link W3-W18-05
(W18-C2/C3).

**The setup.** Lift to the unreduced polynomial Hamiltonian algebra
$\mathfrak h_{\mathrm{poly}}=\C[z_1,z_2]$ (with the constant line
retained). On this source the primitive $\eta(f)=-[f]_0=-f(0,0)$
exists and satisfies $\delta\eta=\omega$ (the constant-Taylor
cocycle of `lem:omega-cocycle`); hence $[\bar c]$ is **exact** on
the unreduced algebra.

**The descent obstruction.** $\eta$ does **not** descend to
$\bar A=\mathfrak h_{\mathrm{poly}}/\C\cdot 1$, because the descent
would require $\eta(1)=-[1]_0=-1\neq 0$, contradicting $1\in\bar A$
being the zero class. The unreduced $\eta$ exists; the reduced
$\bar\eta$ does not.

**The Phase-4 program.** A genuine theorem candidate via this route
would require constructing a **parallel Costello-RG factorization
theory on $\mathfrak h_{\mathrm{poly}}$** that is *not* obtained by
descent from $\bar A$, with the constant Hamiltonian sector
treated as a structural part of the theory rather than a quotient.
The full requirement set (per W3-W18-05):
- $(\alpha)$ Factorization theory on $\mathfrak h_{\mathrm{poly}}$ with
  the constant line retained.
- $(\beta)$ Costello-RG locality property compatible with the
  constant line.
- $(\gamma)$ A descent-functor or non-descent chain map $\mathfrak h_{\mathrm{poly}}\to\bar A$
  that preserves QME class without forcing $\eta\to\bar\eta$
  contradiction.

**Status.** **PHASE-4 CONJECTURE `W18-C3`**. Outline of the parallel
theory is the focus of T3 below.

**Adjudication.** Valid Phase-4 conjecture. Route exists at the
primitive level but needs fresh techniques.
**Residual.** R-`P4-G5-T2-02`: Parallel Costello-RG factorization
theory on $\mathfrak h_{\mathrm{poly}}$ is the open research problem
of T3.

---

### `P4-G5-T2-03` — Route (c): source-change beyond $\mathfrak{gl}(N|N)$ — STATUS: PHASE-4

**Severity 4 (Phase-4 candidates). Status open; family of conjectures.
Confidence medium.**
**Provenance.** Mandate T2(c) of G5 prompt; cross-link W3-W36-D2
(super-balanced scope: S1 vs S2 vs S3).

**The W36 skeptic decomposition.** "Super-balanced" can mean:
- **(S1) $\mathfrak{gl}(N|N)$ specifically with $N=M$.** Verified
  (W22-T1, W22-T2, W30 (A5)).
- **(S2) Any super-Lie algebra with $\mathrm{Str}(I)=0$.** Includes
  $\mathfrak{osp}(2N|2N)$, $\mathfrak{psl}(N|N)$ (the projective
  super-Lie algebra), and other super-Lie algebras with vanishing
  supertrace-of-identity. **Conjectured** but not verified.
- **(S3) Any matrix source with parity-equivariant supertrace.**
  Includes the bi-infinite $\mathfrak{gl}_{\infty|\infty}$ in the
  appropriate completion; **conjectured**.

**Verified scope of W22-T1/T2.** Exactly (S1). The (A5) verification
in W30 is for manuscript-cited regulators applied to
$\mathfrak{gl}(N|M)$ specifically. The wider classes (S2), (S3)
need separate proofs and source-change verification.

**Source-change candidates audit (Phase-4 conjectures).** See T4
below for detailed audit.

**Status.** **PHASE-4** for each candidate; full structure
preservation (PBW, factorization, M-26 split) verifiable per
candidate by separate audit.

**Adjudication.** Valid Phase-4 program.
**Residual.** R-`P4-G5-T2-03`: per-candidate audit; details in T4.

---

## §3. T3 — Unreduced-primitive parallel-factorization program

### `P4-G5-T3-01` — Outline of the parallel theory

**Severity 4 (Phase-4 program). Status: outline only.
Confidence medium.**
**Provenance.** Mandate T3 of G5 prompt; W18-C3 conjecture.

**Goal.** Construct a parallel Costello-RG factorization theory
$\mathcal F^{\mathrm{poly}}$ on $\mathfrak h_{\mathrm{poly}}$ such
that:
- The unreduced primitive $\eta(f)=-[f]_0$ is a **chain-level
  primitive** for $\omega$ (i.e., $\delta\eta=\omega$ at chain level
  in the factorization complex).
- The QME class $[\bar c]$ becomes **exact** on $\mathfrak h_{\mathrm{poly}}$.
- F$'$ becomes unconditional on the unreduced bosonic source.

**Phase-4 ingredients required.**

**(I-1) Factorization theory on $\mathfrak h_{\mathrm{poly}}$ with
constant line retained.** The manuscript's CE/PV theorem (Theorem C)
is on $\bar A=\mathfrak h_{\mathrm{poly}}/\C\cdot 1$ by construction.
A parallel theorem on $\mathfrak h_{\mathrm{poly}}$ would treat the
constant Hamiltonian as a *structural* generator, not a redundancy.
Concretely:
- The CE complex $C^\bullet_{\mathrm{Lie}}(\mathfrak h_{\mathrm{poly}};\C)$
  on the unreduced source has a **non-trivial $H^0$** (the constant
  line cohomology), which the reduced theory kills by quotient. The
  unreduced theory would treat $H^0$ as a unit object.
- The PV side: $\mathrm{PV}(\widehat{\mathbf S}_{\mathrm{Tate}}(\mathfrak h_{\mathrm{poly}}))$
  has additional generators corresponding to the constant line dual.
  The Schouten bracket extends.
- A parallel `prop:ce-koszul` (Theorem C) on $\mathfrak h_{\mathrm{poly}}$
  needs re-derivation; the structure constants $C^L_{(a,b),(c,d)}=(ad-bc)$
  are unchanged, but the constant-Hamiltonian generator gives rise
  to additional zero-degree terms.

**(I-2) Costello-RG locality property.** The Costello locality / QME
compatibility identity (`prob:weighted-rg-locality`) on
$\mathfrak h_{\mathrm{poly}}$ would need:
- A weighted Tate completion of the unreduced source
  $\mathfrak h_{\mathrm{poly},w}$ with a regulator-independent
  finite-window stable diagram.
- Verification that the bracket $\{\cdot,\cdot\}_{\mathrm{poly}}$ on
  $\mathfrak h_{\mathrm{poly},w}$ is admissible-regulator-tame in
  the sense of (A1)–(A5).
- A parallel Hadamard parametrix (`thm:hadamard-mittag-leffler`)
  with constant-Hamiltonian sector.

**(I-3) QME-class exactness via $\eta$.** On
$\mathfrak h_{\mathrm{poly}}$, $\delta\eta=\omega$, so the QME
obstruction class
$[\hbar N\bar c] = \hbar N\delta\eta$ is exact in the unreduced
chain complex. The parallel F$'$ on $\mathfrak h_{\mathrm{poly}}$
becomes unconditional **provided** the parallel factorization
theory is constructed and the chain-level primitive $\eta$ is
**Costello-RG-local**, i.e., compatible with the regulator scheme.

**(I-4) Non-descent chain map.** The parallel factorization theory
must NOT descend to $\bar A$ in the naive way (descent destroys
$\eta$). Instead, the parallel theory on $\mathfrak h_{\mathrm{poly}}$
gives **a different theorem about a different source**, in the
spirit of the supertrace route on $\mathfrak{gl}(N|N)$ — both are
"different brane theories" that discharge `prob:weighted-rg-locality`
on their own data.

**(I-5) Coherence with M-31.** M-31 states
$[\mathrm{Tr}\,\psi]_{\mathrm{BV}}\leftrightarrow N\cdot[\bar c]_{\mathrm{CE}}$
on the reduced bosonic source. On the unreduced source, the
identification would deform: the BV side carries an additional
component from the constant-Hamiltonian generator, and the CE side
is the unreduced $C^2_{\mathrm{Lie}}(\mathfrak h_{\mathrm{poly}};\C)$
class.

**Theorem candidate (Phase-4).**

> **Conjecture `P4-G5-CT1` (Unreduced-bosonic F$'$ unconditionalization
> on $\mathfrak h_{\mathrm{poly}}$).** Suppose a parallel Costello-RG
> factorization theory $\mathcal F^{\mathrm{poly}}$ on
> $\mathfrak h_{\mathrm{poly}}$ exists, satisfying (I-1)–(I-4).
> Then the QME obstruction class on $\mathcal F^{\mathrm{poly}}$ is
> exact via the unreduced primitive $\eta$, and F$'$ becomes
> unconditional on the unreduced bosonic source.

**Status.** **Phase-4 conjecture.** Construction (I-1)–(I-5) is the
research program. None of the manuscript's Phase-1/2/3 theorems
imply this; new techniques required.

**Adjudication.** Valid outline.
**Residual.** R-`P4-G5-T3-01`: All five ingredients (I-1)–(I-5)
must be constructed. Estimated work: 6–18 months at
mathematical-physics frontier rate.

---

## §4. T4 — Source-change program: candidates beyond $\mathfrak{gl}(N|N)$

### `P4-G5-T4-01` — Audit framework: "next supersymmetric source admitting stable PBW filtration AND vanishing supertrace"

**Severity 4 (Phase-4 audit). Status: candidate-list with audit
criteria. Confidence medium.**
**Provenance.** Mandate T4 of G5 prompt; cross-link W3-W36-D2.

**Audit criteria for source change.** A source-change candidate
$\mathfrak{g}$ must satisfy:
- **(C1) Stable PBW filtration.** $\widehat U(\mathfrak{g})$
  admits the manuscript's stable PBW filtration data (M-30 / M-26
  C₂(NT) for $\mathfrak{gl}_N$). For super-Lie algebras, the
  super-PBW filtration (graded over $\Z/2$) must respect the
  manuscript's filtration data.
- **(C2) Vanishing trace/supertrace of identity.** The boundary
  evaluation map's coefficient ($\mathrm{Str}(I)$ on supertrace
  branch) must vanish, or the equivalent obstruction class for
  the chosen source must be controllable.
- **(C3) M-26 split preservation.** The 5-way M-26 split (C₁ᶠʷ,
  C₁ᶜᵒᵐᵖ, C₂(NT), C₂(W), C₂(R)) survives under the source change.
  Per W3-W22-03, super-stacking $\mathfrak{gl}(N|N)$ preserves all
  five; other source changes need separate audit.
- **(C4) (A5) parity-equivariance.** The regulator schemes admissible
  on the new source preserve the source's grading structure.
  $\mathfrak{gl}(N|N)$ has $\Z/2$ super-grading; $\mathfrak{osp}$ has
  $\Z/2$ + symplectic structure; $\mathfrak{gl}_{\infty|\infty}$ has
  $\Z/2$ + Tate completion.
- **(C5) Physical embedding.** The source must be physically
  meaningful as a brane source (BCOV / topological B-model on
  Calabi-Yau threefolds, or its anti-brane / orientifold variants).

**Per-candidate audit:**

---

### `P4-G5-T4-02` — Candidate: $\mathfrak{osp}(2N|2N)$

**Severity 3. Status: candidate; needs audit. Confidence medium.**

**Definition.** The orthosymplectic super-Lie algebra
$\mathfrak{osp}(2N|2N)$ has even part $\mathfrak{so}(2N)\oplus\mathfrak{sp}(2N)$
and odd part the bilinear pairing between them. Supertrace:
$\mathrm{Str}_{\mathfrak{osp}(2N|2N)}(I)=2N-2N=0$ (even and odd
ranks balance).

**Audit:**
- **(C1) Stable PBW.** $\widehat U(\mathfrak{osp}(2N|2N))$ has
  stable super-PBW filtration; it is a classical Lie superalgebra
  (Kac 1977) with explicit Capelli generators. The stable filtration
  exists in the connected large-$N$ range. **PASS** (preliminary).
- **(C2) $\mathrm{Str}(I)=0$.** Yes, by construction. **PASS.**
- **(C3) M-26 preservation.** The 5-way split should survive,
  because (per W3-W22-03) the matrix source enters only through
  the boundary-evaluation map; replacing $\mathfrak{gl}_{2N}$ by
  $\mathfrak{osp}(2N|2N)$ changes the boundary coefficient but not
  the structural form of M-26. **Likely pass; needs audit.**
- **(C4) (A5).** The $\Z/2$-grading is intrinsic; (A5) is
  satisfied by every admissible regulator (per W30 + W3-W22-T2).
  **PASS** (preliminary, by analogy with $\mathfrak{gl}(N|N)$).
- **(C5) Physical embedding.** $\mathfrak{osp}$ branes appear in
  BCOV with an additional involution structure (orientifold). Sen
  1998 / Witten 1998 anti-branes generalize to orientifolds;
  $\mathfrak{osp}$ is the natural source. **PASS** (heuristic).

**Theorem candidate (Phase-4).**

> **Conjecture `P4-G5-CT2` (Orthosymplectic F$'$ unconditionalization).**
> On the $\mathfrak{osp}(2N|2N)$ Dirac-orientifold probe, the
> chain-level mixed brane-defect QME obstruction class vanishes
> at one loop and (under (A5) parity-equivariance) at every loop
> order. F$'$ becomes unconditional on this source.

**Status.** **Phase-4 conjecture.** Verification is similar in
form to W22-T1 / W22-T2, with super-Killing-form replaced by the
orthosymplectic bilinear form.

**Adjudication.** Valid candidate; pending full audit.
**Residual.** R-`P4-G5-T4-02`: Full audit of (C1)–(C5) for
$\mathfrak{osp}(2N|2N)$, including verification that the
orthosymplectic Capelli generators give the correct stable trace
identity.

---

### `P4-G5-T4-03` — Candidate: $\mathfrak{gl}_{\infty|\infty}$ (bi-infinite super-stack)

**Severity 3. Status: candidate; conditional on Tate completion.
Confidence medium-low.**

**Definition.** The bi-infinite general linear super-Lie algebra
$\mathfrak{gl}_{\infty|\infty}$ as the inductive limit
$\varinjlim_N \mathfrak{gl}(N|N)$ with the natural inclusions. The
identity element is "ill-defined" pointwise but has a regularized
supertrace via the manuscript's stable PBW filtration data
(M-26 C₂(NT) generalized to super-stacks).

**Audit:**
- **(C1) Stable PBW.** Requires Tate-completion of the super-stack;
  the bi-infinite parent's existence and PBW filtration need
  Phase-4 verification (see R-W4-A, R-W4-B, R-W4-C of M-29).
  **Conditional on Tate-superalgebra theory (Phase-4).**
- **(C2) $\mathrm{Str}(I)=0$.** In any regularized sense
  (cyclically-renormalized supertrace inside the admissible class),
  $\mathrm{Str}_{\mathfrak{gl}_{\infty|\infty}}(I)=\lim_{N\to\infty}(N-N)=0$.
  **PASS** (in the regularized sense).
- **(C3) M-26 preservation.** The 5-way split lives at the
  finite-window level; the bi-infinite limit needs separate audit
  (R-W4-A/B/C). **Conditional.**
- **(C4) (A5).** Inherited from finite $\mathfrak{gl}(N|N)$.
  **PASS.**
- **(C5) Physical embedding.** Bi-infinite super-stacks arise in
  large-$N$ topological strings (Aganagic-Klemm-Marino-Vafa 2003,
  Costello 2016); physical relevance is established but the BCOV
  embedding requires checking.

**Theorem candidate (Phase-4).**

> **Conjecture `P4-G5-CT3` (Bi-infinite super-stack F$'$
> unconditionalization).** On the $\mathfrak{gl}_{\infty|\infty}$
> Dirac probe with regularized supertrace, the chain-level QME
> obstruction class vanishes inside the (A1)–(A5) admissible
> regulator envelope. F$'$ becomes unconditional on this source.

**Status.** **Phase-4 conjecture, conditional on bi-infinite Tate
completion (R-W4-A/B/C).**

**Adjudication.** Valid candidate; conditional on Phase-4 Tate
super-algebra apparatus.
**Residual.** R-`P4-G5-T4-03`: Bi-infinite Tate completion of
super-Lie algebras; Phase-4. (R-W4-A/B/C generalize.)

---

### `P4-G5-T4-04` — Candidate: $\Z/2$-graded Lie algebras with non-trivial automorphism

**Severity 3. Status: family of candidates; speculative.
Confidence low.**

**Definition.** A $\Z/2$-graded Lie algebra $\mathfrak g=\mathfrak g_0\oplus\mathfrak g_1$
with non-trivial $\Z/2$-automorphism $\sigma:\mathfrak g\to\mathfrak g$
acting on $\mathfrak g_0$ trivially and on $\mathfrak g_1$ by $-1$.
Supertrace: $\mathrm{Str}_\sigma(X)=\mathrm{Tr}(\sigma X)$. If
$\mathrm{Tr}_{\mathfrak g_0}(I)=\mathrm{Tr}_{\mathfrak g_1}(I)$,
then $\mathrm{Str}_\sigma(I)=0$.

**Examples.**
- $\mathfrak{gl}(N|N)$: standard super-Lie algebra, $\sigma=$ parity.
  Verified by W22-T1/T2.
- $\mathfrak{gl}_{2N}$ with $\sigma=$ block-swap involution: even part
  $=\mathfrak{gl}_N\oplus\mathfrak{gl}_N$, odd part = bimodule, with
  $\mathrm{Tr}=N+N=2N$ on $\mathfrak g_0$ and on $\mathfrak g_1$,
  giving $\mathrm{Str}_\sigma(I)=2N-2N=0$. **This is essentially
  $\mathfrak{gl}(N|N)$ in disguise** (equivalent up to a basis change);
  not a new candidate.
- More exotic: a Lie algebra with non-standard $\sigma$ where
  $\mathfrak g_0$ and $\mathfrak g_1$ have different ranks but
  still balanced traces. **Speculative.**

**Audit (criterial).** Each candidate requires:
- A stable super-PBW filtration on $\widehat U(\mathfrak g)$
  consistent with $\sigma$.
- The boundary evaluation $\partial_{\mathrm{bb},N}^{\mathrm{full}}$
  computing $\mathrm{Str}_\sigma$ instead of $\mathrm{Tr}$.
- (A5) parity-equivariance under $\sigma$ for all admissible
  regulators.

**Status.** **Phase-4 / Phase-5 family.** Most natural candidates
reduce to $\mathfrak{gl}(N|N)$ or $\mathfrak{osp}(2N|2N)$; genuinely
new candidates (with non-equivalent $\sigma$) are speculative.

**Adjudication.** Valid speculative-candidate family; not in scope
for Phase-4 unless a specific new candidate is identified.
**Residual.** R-`P4-G5-T4-04`: Search for genuinely new
$\Z/2$-graded candidates beyond $\mathfrak{gl}(N|N)$ and
$\mathfrak{osp}$.

---

### `P4-G5-T4-05` — Source-change program: phasing

**Severity 3. Status: program-level. Confidence medium.**

**Phase-4 priority order.**
- **Priority 1: $\mathfrak{osp}(2N|2N)$ (P4-G5-CT2).** The
  closest analogue to $\mathfrak{gl}(N|N)$ with a clean physical
  interpretation (BCOV orientifold). Audit work: full (C1)–(C5)
  verification, parallel of W22-T1/T2 + W30 (A5) for the
  orthosymplectic bilinear form. **Estimated 6 months.**
- **Priority 2: $\mathfrak{gl}_{\infty|\infty}$ (P4-G5-CT3).**
  Conditional on bi-infinite Tate-superalgebra apparatus
  (R-W4-A/B/C). Audit work: Phase-4 Tate-completion of super-Lie
  algebras + W22-style chain-level proof. **Estimated 12 months.**
- **Priority 3: Other $\Z/2$-graded candidates (P4-G5-T4-04).**
  Speculative; only proceeds if a specific candidate is identified
  in the Phase-4 program. **Estimated 18+ months.**

**Cross-program coupling.** G3 (supertrace beyond $\mathfrak{gl}(N|N)$)
feeds priorities 1–3 directly. G4 (5d-M-theory twist) might supply
a non-bosonic source for free (see T6 below). G2 (column-Verma
functoriality) interacts via the Borel structure of the chosen
source.

**Adjudication.** Valid program structure.
**Residual.** R-`P4-G5-T4-05`: Phase-4 work calendar; coordination
with G3, G4, G2.

---

## §5. T5 — Milestone ladder

### `P4-G5-T5-01` — 3-month milestone (precise statement of the desideratum)

**Severity 4 (deliverable). Confidence high (the deliverable is
well-defined).**

**Deliverable (3 months).** **Precise mathematical statement of the
bosonic-F$'$ unconditionalization desideratum.**

> **Desideratum (D).** Construct or prove the existence of a
> chain-level primitive
> $\xi:\mathcal O_{\mathrm{loc}}(\mathcal E_w^{\mathrm{bosonic}})\to
> \mathcal O_{\mathrm{loc}}(\mathcal E_w^{\mathrm{bosonic}})[-1]$
> such that
> $(Q+\{I_0,-\})\xi=\hbar N\bar c\cdot\mathbf 1$
> at chain level, where $\mathcal E_w^{\mathrm{bosonic}}$ is the
> bosonic $\mathfrak{gl}_N$ Dirac probe weighted local-functional
> complex, and the equality holds modulo the **Costello-RG
> locality** of the chosen factorization theory.

**Sub-deliverables.**
- **(D-a)** Restate `prob:weighted-rg-locality` precisely as the
  vanishing-class problem; identify all ingredients of the chain-
  level primitive $\xi$.
- **(D-b)** State the precise form of the obstruction
  $\hbar N\bar c$ as a chain-level cocycle (already done by
  W22-L2 on the super-stack; bosonic version per W3-W10-01 +
  W3-W15-03).
- **(D-c)** State precisely which Phase-4 routes (T2-(b), T2-(c))
  could discharge (D), with explicit sub-criteria for each route.

**Verification.** This is a deliverable that produces a precise
written statement; it does not require new theorems. Estimated
work: 3 months / one G5-coordinator + cross-volume consultation.

**Adjudication.** Valid 3-month deliverable.

---

### `P4-G5-T5-02` — 6-month milestone (explore unreduced-primitive parallel theory)

**Severity 4 (deliverable). Confidence medium.**

**Deliverable (6 months).** **Outline of the parallel Costello-RG
factorization theory on $\mathfrak h_{\mathrm{poly}}$.**

**Sub-deliverables.**
- **(D-a)** Explicit construction of (I-1): factorization theory
  on $\mathfrak h_{\mathrm{poly}}$ with constant line retained.
  Outcome: detailed chain complex specification, possibly with a
  specific prototype on the formal disk.
- **(D-b)** Outline of (I-2): Costello-RG locality on the
  unreduced source. Outcome: regulator class admissibility audit
  parallel to W30 (A5).
- **(D-c)** Hand-computation at the simplest case (e.g., abelian
  rank-1 Hamiltonian $\mathfrak h_{\mathrm{poly}}=\C[z]$, or
  truncated to bidegree 1) verifying the chain-level $\delta\eta=\omega$
  identity.
- **(D-d)** Verification or counterexample for (I-3): does the
  unreduced primitive $\eta$ Costello-RG-localize? This is a
  Phase-4 research question; likely outcome: partial verification
  with named obstruction.

**Outcome scenarios.**
- **Best case.** (D-c) verifies and (D-d) verifies; F$'$ on the
  unreduced bosonic source is set up for proof. (Phase-4
  completion possible by 12-month milestone.)
- **Mid case.** (D-c) verifies but (D-d) names a precise
  obstruction. The unreduced-primitive route is **conditionally
  open**; F$'$ status is "unreduced unconditional, reduced still
  conditional." (Open Phase-4.)
- **Worst case.** (D-c) fails; the parallel factorization theory
  cannot be constructed. The unreduced-primitive route closes in
  the negative. **Phase-5 escalation candidate.**

**Adjudication.** Valid 6-month deliverable.

---

### `P4-G5-T5-03` — 12-month milestone (source-change candidates with full structure preservation)

**Severity 4 (deliverable). Confidence medium-low.**

**Deliverable (12 months).** **Full audit of source-change
candidates: $\mathfrak{osp}(2N|2N)$, $\mathfrak{gl}_{\infty|\infty}$,
exotic $\Z/2$-graded.**

**Sub-deliverables.**
- **(D-a) $\mathfrak{osp}(2N|2N)$ audit.** Full (C1)–(C5)
  verification per `P4-G5-T4-02`. Outcome: theorem candidate
  `P4-G5-CT2` proved or named obstruction.
- **(D-b) $\mathfrak{gl}_{\infty|\infty}$ audit.** Conditional
  on bi-infinite Tate-superalgebra apparatus. Outcome: theorem
  candidate `P4-G5-CT3` proved or named obstruction (likely
  conditional on R-W4-A/B/C).
- **(D-c) Other candidates.** Targeted search for genuinely new
  $\Z/2$-graded sources; cross-verification with G3 supertrace
  beyond $\mathfrak{gl}(N|N)$.
- **(D-d) Cross-coupling.** Coordinate with G4 (5d-M-theory
  twist) — see T6.

**Outcome scenarios.**
- **Best case.** $\mathfrak{osp}$ closes positively; F$'$ on
  $\mathfrak{osp}$ is unconditional, supplying a second
  source-change discharge route. Phase-4 in good standing.
- **Mid case.** $\mathfrak{osp}$ closes with named obstruction;
  bi-infinite remains Phase-4. F$'$ on bosonic source is partially
  cleared via $\mathfrak{osp}$ as alternative.
- **Worst case.** All source-change candidates close in the negative
  with no new theorem; combined with worst-case T5-02, **Phase-5
  escalation criterion is met**.

**Adjudication.** Valid 12-month deliverable.

---

### `P4-G5-T5-04` — 18+ month milestone (bosonic-F$'$ status: proven / disproven / Phase-5)

**Severity 4 (terminal verdict). Confidence medium-low.**

**Deliverable (18+ months).** **Final verdict on bosonic-F$'$
unconditionalization.**

**Three terminal verdicts:**

- **PROVEN.** Bosonic F$'$ is unconditionalized on the unreduced
  source via P4-G5-CT1 (parallel factorization on
  $\mathfrak h_{\mathrm{poly}}$) and/or P4-G5-CT2 (orthosymplectic
  source-change). The reduced bosonic source is closed via
  appropriate descent or parallel-source identification.

- **DISPROVEN.** All three Phase-4 routes (unreduced-primitive,
  source-change, parallel-factorization) close in the negative.
  The bosonic-F$'$ obstruction $\hbar N[\bar c]$ is structurally
  irreducible inside the manuscript's framework. **Status updates
  to Phase-5 escalation.**

- **PHASE-5.** A specific obstruction has been identified that
  requires fundamentally new technique (e.g., a categorical
  reformulation of the constant-Hamiltonian sector, or a
  derived-CY framework for BCOV). The route is named but the
  technique is outside the existing apparatus. **Phase-5 program
  outlined.**

**Cross-coupling at 18+ months.** Coordination with all groups
(G2 Borel structure, G3 supertrace, G4 5d-M-theory, G6
manuscript) is essential at this milestone; the verdict has
manuscript-wide implications.

**Adjudication.** Valid terminal milestone.

---

## §6. T6 — Interaction with other groups

### `P4-G5-T6-01` — G3 (supertrace beyond $\mathfrak{gl}(N|N)$) feeds G5 source-change

**Severity 3. Status: clear synergy. Confidence high.**

**Interaction.** G3's mandate to extend the supertrace mechanism
beyond $\mathfrak{gl}(N|N)$ directly feeds G5's source-change
program (P4-G5-T4). Specifically:
- G3 verification that $\mathfrak{osp}(2N|2N)$ admits the supertrace
  $\Z/2$-grading equivalent to $\mathfrak{gl}(N|N)$ feeds
  `P4-G5-T4-02`.
- G3 verification of the bi-infinite super-stack
  $\mathfrak{gl}_{\infty|\infty}$ feeds `P4-G5-T4-03`.

**Concrete dependency.** G5's 12-month milestone (T5-03 sub-
deliverable D-a) depends on G3's audit of $\mathfrak{osp}(2N|2N)$
admitting (A5) parity-equivariance. Without G3's verification, G5
would need to re-derive the (A5) audit per source.

**Recommendation.** G3 and G5 should coordinate on shared
candidate-list: $\mathfrak{osp}(2N|2N)$, $\mathfrak{gl}_{\infty|\infty}$,
exotic $\Z/2$-graded. G3's verification feeds G5's source-change
discharge; G5's source-change discharge gives G3 a published
target.

**Adjudication.** Valid synergy.

---

### `P4-G5-T6-02` — G4 (5d-M-theory twist) might give a non-bosonic source for free

**Severity 3. Status: speculative; needs G4 confirmation. Confidence
medium-low.**

**The hypothesis.** G4's mandate to verify the 5d twisted M-theory
embedding (Costello 2016, *M-theory in the Omega-background*; cf.
W3-W23-5dM) might supply a non-bosonic brane source as a structural
component of the Omega-deformed M-theory framework. If the M5-brane
worldvolume / M2-brane topological string boundary in 5d twisted
M-theory carries a built-in $\Z/2$-grading or supertrace structure,
then the bosonic-F$'$ obstruction might be discharged by **lifting
to the 5d twisted M-theory ambient**, where the supertrace structure
is intrinsic to the physical setup rather than imposed by hand.

**Concrete possibility.** Costello 1610.04144's Omega-deformed
M-theory has fields including:
- Bosonic 3-form $C^{(3)}$ on the 11d ambient (background).
- Worldvolume scalar fields on M5/M2 reduction.
- Topological worldvolume gauge field with $\Z/2$-grading from
  spinor structures.

If the M2-brane topological string boundary inherits the
ambient $\Z/2$-grading from the 11d spinor structure, then the
brane probe matrix algebra is naturally $\mathfrak{gl}(N|N)$ rather
than $\mathfrak{gl}_N$. **Conjecture: bosonic F$'$ on the M2-brane
boundary is automatically promoted to super-balanced F$'$ via the
5d twisted M-theory ambient.**

**Status.** **Speculative**; depends on G4's verification of the
5d twisted M-theory ambient structure and its coupling to the
brane probe matrix algebra.

**Recommendation.** G5 and G4 should coordinate on the brane-probe
matrix-algebra structure in 5d twisted M-theory. If G4 confirms
intrinsic $\Z/2$-grading, F$'$ is unconditionalized "for free" on
the physically-relevant source (M2-brane in 5d twisted M-theory),
and G5's source-change program acquires a new priority-1 candidate.

**Adjudication.** Valid speculation; needs G4 confirmation.

---

### `P4-G5-T6-03` — G2 (column-Verma functoriality) interaction with bosonic obstruction

**Severity 3. Status: cross-functoriality question. Confidence
medium.**

**The question.** G2's column-Verma functoriality program (per
W3-W26) audits the symplectomorphism-equivariance of the column-
Verma decomposition $C^{+-}=\bigoplus_a M_a$ on the principal-part
cotangent module. The decomposition is $T^2$-equivariant (W3-W26-06)
but **not** generic-$GL_2$-equivariant (W3-W26-07).

**Does the bosonic-F$'$ obstruction inherit?** The bosonic-F$'$
obstruction $\hbar N[\bar c]$ on the brane side has a corresponding
class on the closed (CE) side via M-31. The CE side is
$[\bar c]\in H^2_{\mathrm{Lie}}(\bar A;\C)$, a Lie-algebra cocycle
on the reduced unreduced polynomial Hamiltonian $\bar A$.
$T^2$-equivariance of the column-Verma decomposition implies
$[\bar c]$ is $T^2$-equivariant (it pairs with $T^2$-equivariant
homology classes). The non-$GL_2$-equivariance of the column-Verma
decomposition does **not** directly affect $[\bar c]$, since
$[\bar c]$ is a global Lie cocycle, not a column-Verma component.

**However:** the unreduced-primitive route (T3) constructs a
parallel theory on $\mathfrak h_{\mathrm{poly}}$ where the
constant-Hamiltonian sector is structural. The corresponding
column-Verma decomposition on the unreduced source might have
**different** equivariance properties, since the constant
Hamiltonian generator changes the Borel structure.

**Recommendation.** G5 and G2 should verify that the unreduced-
primitive parallel theory's column-Verma decomposition is consistent
with G2's $T^2$-equivariance findings. This is a Phase-4 cross-
audit, deliverable at the 6-month milestone (alongside T5-02).

**Adjudication.** Valid cross-audit question.

---

## §7. T7 — Phase-5 escalation criterion

### `P4-G5-T7-01` — Precise criterion for declaring bosonic-F$'$ Phase-5

**Severity 4 (epistemic deliverable). Status: criterion formulated.
Confidence high (the criterion is well-defined).**

**The criterion.** Bosonic F$'$ is declared **Phase-5** (requires
fundamentally new technique) if and only if all three of the
following hold:

- **(P5-α) Unreduced-primitive route closes in the negative.** The
  parallel Costello-RG factorization theory on
  $\mathfrak h_{\mathrm{poly}}$ either (i) cannot be constructed,
  or (ii) is constructed but the unreduced primitive $\eta$ does
  not Costello-RG-localize, or (iii) the descent obstruction to
  $\bar A$ is structurally irreducible. (Per T5-02 worst-case
  scenario.)
- **(P5-β) Source-change routes all close in the negative.** All
  Phase-4 source-change candidates ($\mathfrak{osp}$,
  $\mathfrak{gl}_{\infty|\infty}$, exotic $\Z/2$-graded) either
  (i) do not satisfy the audit (C1)–(C5), or (ii) satisfy the audit
  but produce theorems on different sources (not the bosonic
  source). (Per T5-03 worst-case scenario.)
- **(P5-γ) No 5d-M-theory free pass.** G4 confirms that the 5d
  twisted M-theory ambient does NOT supply an intrinsic
  $\Z/2$-grading on the M2-brane boundary, so the bosonic source
  remains the relevant brane-physics target. (Per T6-02
  hypothesis closure.)

**If (P5-α) AND (P5-β) AND (P5-γ) all hold, then bosonic F$'$ is
unsolvable inside the existing manuscript framework and requires
fundamentally new technique.** The precise nature of "new
technique" would be:
- A categorical reformulation of the constant-Hamiltonian sector
  that does not rely on the reduced/unreduced quotient structure.
- A derived-CY framework for BCOV (per Costello-Gwilliam Vol 2)
  that handles the bosonic source intrinsically without requiring
  $\mathrm{Tr}(I)=0$.
- A Vol-III-cross-volume technique (per `~/calabi-yau-quantum-groups`)
  that handles bosonic branes via the chiral algebra side.

**If any of (P5-α), (P5-β), (P5-γ) fails (i.e., a route opens or
G4 confirms intrinsic $\Z/2$), bosonic F$'$ remains in Phase-4 and
the corresponding route is pursued.**

**Adjudication.** Valid Phase-5 criterion.

---

### `P4-G5-T7-02` — What "Phase-5" means for the manuscript

**Severity 3. Status: epistemic note. Confidence high.**

**Phase-5 implications for the manuscript.**
- **F$'$ status.** The manuscript's Theorem F$'$ remains
  **conditional** on `prob:weighted-rg-locality` for the bosonic
  source; the conditional is not removable inside Phase-1/2/3/4.
- **F$'$ blast radius.** Per W3-W15, F$'$ is a **descendant
  comparison** statement on the all-$N$ stable trace identity.
  Phase-5 status of bosonic F$'$ does **not** invalidate F (which
  is unconditional on the algebraic finite model) or G (which is
  unconditional on the closed CE side). The conditional
  cross-reference between the open and closed sides remains
  load-bearing for the manuscript's central result, but the
  conditional is honest.
- **Manuscript stance.** The manuscript can/should explicitly
  declare F$'$ **conditional on the bosonic source, unconditional
  on the super-balanced source**, with the Phase-5 escalation
  noted as the open frontier. This is consistent with M-13's
  bosonic-vs-supertrace clarification and with the manuscript's
  existing `thm:app-unreduced-polynomial-centrality-no-go`.
- **Cross-volume implications.** Vol III (CY-to-chiral frontier)
  at `~/calabi-yau-quantum-groups` may inherit the F$'$
  conditional structure; Phase-5 escalation is therefore a
  cross-volume concern, not just a local matter.

**Adjudication.** Valid epistemic note.

---

## §8. Heal proposals (smallest first)

### Tier 1 — Statement-only edits (Phase-4 ledger)

**`P4-G5-WP-1`.** Inscribe `P4-G5-CT1` (unreduced-bosonic F$'$
unconditionalization conjecture) in the master ledger as a Phase-4
research target, with explicit dependency on (I-1)–(I-5).

**`P4-G5-WP-2`.** Inscribe `P4-G5-CT2` (orthosymplectic F$'$
unconditionalization conjecture) in the master ledger as a Phase-4
research target with priority 1.

**`P4-G5-WP-3`.** Inscribe `P4-G5-CT3` (bi-infinite super-stack
F$'$ unconditionalization conjecture) in the master ledger as a
Phase-4 research target, conditional on R-W4-A/B/C.

### Tier 2 — Cross-volume cross-link

**`P4-G5-WP-4`.** Add to `appendix-unreduced-bv-qme.tex`'s
`rmk:app-scalar-contact-escape-routes` a paragraph:

> "**Phase-4 status (G5).** The three escape routes have distinct
> Phase-4 status:
> (i) **Supertrace** (W22-T1, W22-T2): closed positively on
>      $\mathfrak{gl}(N|N)$ via W30 (A5).
> (ii) **Central character**: resolved into the existing Capelli
>      counterterm; not a new route.
> (iii) **Unreduced primitive**: Phase-4 conjecture (P4-G5-CT1);
>      requires parallel factorization theory.
> Source-change beyond $\mathfrak{gl}(N|N)$ (e.g.,
> $\mathfrak{osp}(2N|2N)$, $\mathfrak{gl}_{\infty|\infty}$) supplies
> additional Phase-4 candidates (P4-G5-CT2, P4-G5-CT3). The bosonic
> source remains conditional in Phase-1/2/3; Phase-4 program is
> outlined in `reconstitution/phase4-G5-bosonic-Fprime-2026-04-28.md`."

### Tier 3 — Phase-5 escalation note

**`P4-G5-WP-5`.** In `theorem-lanes.tex` Lane (F$'$) or in
`claim-strength-ledger.tex`, add a sentence:

> "Bosonic F$'$ is conditional in Phase-1/2/3/4 on
> `prob:weighted-rg-locality`. Phase-5 escalation criterion:
> (P5-α) AND (P5-β) AND (P5-γ) per
> `phase4-G5-bosonic-Fprime-2026-04-28.md` `P4-G5-T7-01`. As of
> Phase-4 launch, the criterion has not been triggered."

---

## §9. Residuals after Phase-4 / G5

- **R-`P4-G5-T2-02`.** Parallel Costello-RG factorization theory on
  $\mathfrak h_{\mathrm{poly}}$ (P4-G5-CT1). 6-month deliverable;
  Phase-4 research.
- **R-`P4-G5-T2-03`.** Source-change beyond $\mathfrak{gl}(N|N)$.
  12-month deliverable; Phase-4 research.
- **R-`P4-G5-T4-02`.** $\mathfrak{osp}(2N|2N)$ full audit.
  Priority 1; coordinate with G3.
- **R-`P4-G5-T4-03`.** $\mathfrak{gl}_{\infty|\infty}$ Tate
  completion. Priority 2; conditional on R-W4-A/B/C.
- **R-`P4-G5-T4-04`.** Other $\Z/2$-graded candidates; speculative.
- **R-`P4-G5-T6-02`.** 5d-M-theory twist; coordinate with G4.
- **R-`P4-G5-T6-03`.** Column-Verma functoriality on unreduced
  source; coordinate with G2.
- **R-`P4-G5-T7-01`.** Phase-5 criterion check at 18-month
  milestone.

---

## §10. Convergence verdict

**Bosonic F$'$ unconditionalization research outline: COMPLETE.**

The bosonic F$'$ obstruction is **structural and load-bearing**
(T1: $\hbar N[\bar c]$ = Theorem G's Capelli class, regulator-
class-canonical inside M-26). Three Phase-4 routes (T2): (a)
central character RESOLVED-INTO-EXISTING (Capelli counterterm);
(b) unreduced primitive PHASE-4 CONJECTURE (T3, P4-G5-CT1, 6-mo
deliverable); (c) source-change PHASE-4 family (T4, priorities:
$\mathfrak{osp}(2N|2N)$ → $\mathfrak{gl}_{\infty|\infty}$ →
exotic). Milestone ladder 3/6/12/18+ months (T5). Cross-group
coupling: G3 feeds source-change, G4 5d-M-theory might supply
free $\Z/2$, G2 column-Verma cross-audit (T6). Phase-5 criterion
(T7): (P5-α) AND (P5-β) AND (P5-γ) — not triggered at Phase-4
launch.

**Inscribed durables.** This document; three theorem candidates
(P4-G5-CT1, CT2, CT3); cross-volume cross-link to
`appendix-unreduced-bv-qme.tex`; Phase-5 criterion formalized.

End of Phase-4 / G5 research outline.
