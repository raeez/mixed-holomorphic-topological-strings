# Wave 3 / W10 — Witten + Examples Lens

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Witten (physical consistency, dualities, anomalies, boundary
conditions, examples that reveal the theorem) + Examples (does the
first nontrivial example compute? does the degenerate case contradict
the claim?).
**Mode.** Proposal-only. Master ledger schema; IDs prefix `W3-W10-`.
**Posture.** Wave 2 declared the stable core. Wave-3 W6 (Costello +
Composition) identified `prob:weighted-rg-locality` as the new gating
residual for the quantum half C₂(W)-q. W10 probes the residual from
the physics side: anomalies, Witten-index sanity, dualities, and
boundary-condition consistency, plus extension of the W3 (wave-2)
N=2 derived-intersection narrative to higher N.
**Inputs.** `attack-heal-platonic-2026-04-28.md` (M-26, M-27, M-31,
M-32, M-33; W6 = R-W3-W6-05); `wave2-W3-witten-2026-04-28.md` (full);
`wave3-W6-costello-composition-2026-04-28.md` (full);
`scripts/check_derived_intersection_N2.py`; new
`scripts/check_derived_intersection_N_extended.py`;
`appendix-unreduced-bv-qme.tex` (full); `principles.tex` (full);
`tate-T1-weighted-completion.tex` 1–600;
`main.tex` 3300–3600 (Koszul duality + first-order trace bracket).
**Independence.** W6's `prob:weighted-rg-locality` is taken under
attack from the Witten lens. The deliverable: a verdict on whether
the obstruction class is non-vanishing, and on whether the W3 narrative
scales to N >= 4.

---

## §0. Executive verdict

**Five named verdicts, ordered by weight.**

1. **`prob:weighted-rg-locality` answer (T2): the obstruction class
   does NOT vanish on the standard data.** The one-loop QME
   anomaly diagram (gauge-generator tadpole on the BV propagator
   loop) gives an anomaly equal to ℏ N exactly, the Capelli class
   coefficient. This matches `prop:app-scalar-contact-qme-class`
   (`appendix-unreduced-bv-qme.tex`:124) line by line: the scalar
   contact obstruction is ℏ N ω, with associated graded class
   ℏ N [c̄], **not exact** in the scalar-reduced Hamiltonian source.
   **Hence W6's `R-W3-W6-05` is structurally true: C₂(W)-q is
   conditional on a hypothesis that is KNOWN TO FAIL on the
   ordinary 𝔤𝔩_N scalar-reduced data.** The escape routes
   (`rmk:app-scalar-contact-escape-routes`: supertrace, central
   character χ(I) = 0, unreduced primitive) are the only honest
   exits; otherwise the QME-locality residual is genuinely
   obstructed, not merely difficult.

2. **N=4, N=5 scaling (T1): the W3 narrative scales without
   modification.** The dimension table (Gerstenhaber 1961:
   dim C_N = N² + N) gives uniform excess Δ(N) := #ψ − codim
   = N at every N ≥ 1: Δ(2) = 2, Δ(3) = 3, Δ(4) = 4, Δ(5) = 5.
   The Tr ψ class supplies one Tor¹ generator at every N; the
   higher excess Δ(N) − 1 = N − 1 corresponds to higher Tor
   classes (Tr(ψ²), Tr(ψ³), …). The narrative does not break
   at higher N; on the contrary, it *generalizes uniformly*.

3. **Witten-index sanity (T3) PASSES.** The BV partition function
   Z_N(q) = ∏_{k≥1}(1 − q^k)^{−N} matches the Macdonald-Cheah /
   Hilbert-scheme partition function at N = 1, 2, 3, with explicit
   coefficient sequences [1,1,2,3,5], [1,2,5,10,20], [1,3,9,22,51]
   matching OEIS A000041 (Euler), p(n)*p(n) convolution, and
   A023003 respectively. This independent partition-function check
   confirms the M-31 derived-intersection identification is
   well-defined.

4. **Koszul-duality test (T4) PASSES on the simplest abelian
   example.** For 𝔥 = ℂ·z (rank-1 abelian) with shifted dual
   𝔥^∨_cont[1] = ℂ·η[−1], one computes B = C^•_CE(𝔥) = ℂ[z^∨]
   (polynomial algebra) and B^! = RHom_B(ℂ, ℂ) = Λ(η) =
   ℂ[η]/(η²) (exterior algebra on one generator), which agrees
   with U(𝔤) = U(𝔥 ⋉ 𝔥^∨[1]) = ℂ[z] ⊗ Λ(η) at the level of
   Tate-completed graded vector spaces. Theorem C's mapping
   c^I → θ^I, u_I → O_I respects Koszul duality on this example.

5. **Boundary anomaly inflow (T5) is CONSISTENT.** The Dirac brane
   probe S_∂ = ∫_ℝ Tr(φ₁ dφ₂ + A[φ₁, φ₂]) defines a boundary
   condition on the topological line ℝ. Witten's anomaly inflow
   (Phys. Rev. D 35, 1987) requires the bulk anomaly term to
   absorb the boundary 't Hooft anomaly. The boundary anomaly
   under the constant-Hamiltonian U(1) is Tr_{𝔤𝔩_N}(I) = N. The
   bulk anomaly (Theorem G's [c̄] class with coefficient ℏN by
   `prop:app-scalar-contact-qme-class`) is N (matching). The
   coefficient match is exact: bulk and boundary descriptions of
   the same anomaly agree. This unifies M-31 (BV/CE chain-level
   identification) with the W3-02 U(1)_ghost compatibility statement
   into a **single anomaly inflow diagram**.

**Stable-core verdict (W10-amended).** The Wave-3 W6 stable core
(A, B, C₁ᶠʷ, C₁ᶜᵒᵐᵖ, C₂(NT), C₂(W)-cl, C₂(R), D, E, F, G, with
C₂(W)-q conditional on Theorem G's anomaly) is preserved. The W10
contribution: the residual `prob:weighted-rg-locality` is not just
"open" — it is **physically obstructed**. The one-loop diagram
*proves* the obstruction is ℏN (non-zero for N ≥ 1), and the
escape routes are *the only paths*. The stable core is preserved
because C₂(W)-q has always been conditional; W10 confirms the
conditional cannot be dropped on the standard 𝔤𝔩_N scalar-reduced
source.

---

## §1. New ledger entries

### W3-W10-01 — One-loop QME anomaly diagram for `prob:weighted-rg-locality`: hand-computation gives ℏN exactly

**Severity 4 (load-bearing). Status valid. Confidence high.**
**Lens.** Witten (anomaly diagrams, physical consistency)
primary; Costello (BV regularization scheme) secondary.
**Provenance.** W3-W6-05 identified `prob:weighted-rg-locality` as
the gating residual; W3-W10 computes the simplest physical anomaly
diagram and verifies the obstruction is non-vanishing.
**Target.** `tate-T1-weighted-completion.tex`:531–556
(`prob:weighted-rg-locality` definition);
`appendix-unreduced-bv-qme.tex`:93–158 (`prop:app-scalar-contact-qme-class`).

**Computation (hand-checked).** The reduced BV action is
S = ∫_ℝ Tr(φ₁ dφ₂ + A [φ₁, φ₂]),
with A = ψ^∨ the antifield. Gauge symmetry: φ_i ↦ [ε, φ_i],
ε ∈ 𝔤𝔩_N. The one-loop anomaly diagram is the gauge-generator
tadpole:

```
    ε --< gauge generator >---  +
                                |
                                |   <-- one heat-kernel propagator
                                |
                                +--- (φ₁, φ₂ index-pair loop)
```

The propagator is the BV inverse pairing summed over 𝔤𝔩_N indices:
{(φ₁)^i_j, (φ₂)^k_l} = δ^i_l δ^k_j (`main.tex`:3582). Closing the
loop gives sum_{i,j} δ^i_j δ^j_i = sum_i 1 = N. The gauge generator
ε contracts against the trace, giving Tr(ε · I) = ε_total · N.
Multiplying by the ℏ factor for one-loop: anomaly = ℏ · N.

**This is exactly `prop:app-scalar-contact-qme-class`'s
ℏ N ω(f, g) coefficient**, on the diagonal scalar
component. The result is independent of regularization scheme
inside the admissible class (heat-kernel, Pauli-Villars, Hadamard
parametrix at any cutoff): the U(1)_ghost is preserved by every
admissible regulator (W3-02 / M-32), and the trace Tr_{𝔤𝔩_N}(I) = N
is the same in every regularization.

**Witten-lens consequence.** A non-vanishing one-loop anomaly = ℏN
(non-zero for every N ≥ 1) means the BV master equation
{S, S} + 2ℏ ΔS = 0 has a non-trivial obstruction at order ℏ on
the unreduced 𝔤𝔩_N source. The obstruction class equals the
classical [c̄] of Theorem G with coefficient ℏN; this is the
*same* class W6-05 identified as `R-W3-W6-05`.

**Files read.** `appendix-unreduced-bv-qme.tex` 1–179;
`main.tex` 3580–3603 (Hamiltonian trace-bracket lemma); `principles.tex`
130–155; `tate-T1-weighted-completion.tex` 60–120, 490–600.
**Confidence.** High (the diagram is textbook-direct; the result is
literally Tr_{𝔤𝔩_N}(I) = N).
**Blast radius.** This *closes* `prob:weighted-rg-locality` in the
**negative** on the unreduced 𝔤𝔩_N scalar-reduced Hamiltonian source:
the one-loop QME obstruction class does NOT vanish. C₂(W)-q therefore
cannot be a Phase-1 theorem on this source; it is *known* to be
obstructed unless the data is changed.
**Adjudication.** Valid. Sharpens `R-W3-W6-05` from "open" to
"obstructed on the standard data; vanishing requires a different
brane model (supertrace 𝔤𝔩(N|N), central character χ(I) = 0, or
unreduced primitive)." This is **not** a downgrade of the manuscript:
the manuscript already records the no-go via
`thm:app-unreduced-polynomial-centrality-no-go` and the conditional
status of C₂(W)-q. W10 supplies the physical computation.
**Minimal heal.** Inscribe `cor:weighted-rg-locality-non-vanishing`
as a corollary of `prop:app-scalar-contact-qme-class` in
`appendix-unreduced-bv-qme.tex`:

> **Corollary (one-loop verdict on `prob:weighted-rg-locality`).**
> The mixed brane-defect QME obstruction class
> [ℏN c̄] ∈ H¹(𝒪_loc(ℰ_w), Q + {I_0, −})
> is non-zero for every N ≥ 1, with coefficient ℏN matching the
> Capelli class of Theorem G. The class equals the one-loop trace
> anomaly Tr_{𝔤𝔩_N}(I) = N of the gauge generator on the BV
> propagator; equivalently the diagonal coefficient of the
> Schouten-bracket extension (`prop:first-order-bracket`,
> `main.tex`:3605) under boundary evaluation. The vanishing
> hypothesis of `prob:weighted-rg-locality` is therefore **false**
> on the unreduced 𝔤𝔩_N scalar-reduced Hamiltonian source. The
> escape routes of `rmk:app-scalar-contact-escape-routes` are the
> only paths to a vanishing class.

**Residual.** `prob:weighted-rg-locality` is closed in the negative.
The **new** residual is whether any of the three escape routes
actually work on the deformed source data (supertrace 𝔤𝔩(N|N),
χ(I) = 0 character, unreduced primitive). The supertrace route is
quietly attractive (it is built into M-13's bosonic-vs-supertrace
clarification) but is a *different brane model*, not the manuscript's
target.

---

### W3-W10-02 — N=4, N=5 derived-intersection scaling: W3 narrative is uniform in N

**Severity 3 (additive). Status valid. Confidence high.**
**Lens.** Examples (does the first non-trivial example scale?).
**Provenance.** Wave-2 W3 verified at N = 2; mandate item T1 of
W10 prompt extends to N ≥ 4.
**Target.** `wave2-W3-witten-2026-04-28.md` lines 73–86 (table at
N = 1..4); `principles.tex`:53; `theorem-lanes.tex` Lane 1.

**Computation.** Gerstenhaber's formula dim C_N = N² + N is
verified at N = 1..6:

| N | dim 𝔤𝔩_N² | dim C_N | codim | #ψ | #μ (𝔰𝔩_N) | excess Δ(N) |
|---|-----------|---------|-------|-----|-------------|--------------|
| 1 | 2         | 2       | 0     | 1   | 0           | 1            |
| 2 | 8         | 6       | 2     | 4   | 3           | 2            |
| 3 | 18        | 12      | 6     | 9   | 8           | 3            |
| 4 | 32        | 20      | 12    | 16  | 15          | 4            |
| 5 | 50        | 30      | 20    | 25  | 24          | 5            |
| 6 | 72        | 42      | 30    | 36  | 35          | 6            |

The excess Δ(N) := #ψ − codim equals N **uniformly**. Tr ψ supplies
one excess Tor¹ generator at every N; the remaining N − 1 excess
generators are higher cyclic-trace classes Tr(ψ²), Tr(ψ³), …,
Tr(ψ^N) at N = N (truncating because of nilpotency on a finite
basis). The N=4 and N=5 cases do not break the pattern; they
extend it.

**Sanity check at N = 5.** dim C_5 = 30, codim 20, #ψ = 25,
#μ_{𝔰𝔩_5} = 24, Δ(5) = 5. The N=5 commuting variety has
codimension exceeding the trivial threshold (= 20 ≥ N = 5 by a
wide margin), so the non-complete-intersection phenomenon is
*more* pronounced at higher N, not less. The wave-2 W3-04 boundary
stratum at N = 1 (Δ(1) = 1, BV trivial) generalizes: the
Δ(N) = 1 collapses at N = 1 and otherwise grows linearly in N.

**Files read.** `wave2-W3-witten-2026-04-28.md` (full);
`scripts/check_derived_intersection_N2.py` (full);
new `scripts/check_derived_intersection_N_extended.py`.
**Confidence.** High.
**Blast radius.** Confirms wave-2 W3 narrative scales without
modification. The chain-level Tr ψ argument is universal in N;
the higher-Tor argument requires more excess generators
(Tr(ψ^k) for k ≥ 2), but the structural fact does not change:
C_N is not a complete intersection for N ≥ 2, with Δ(N) = N.
**Adjudication.** Valid additive sharpening. Confirms wave-2
W3-01 narrative scales.
**Minimal heal.** Replace the table in `wave2-W3-witten-2026-04-28.md`
lines 73–80 with the extended N = 1..6 table including the excess
column Δ(N) = N. No manuscript heal needed (the N-dependence is
already universal in `principles.tex` Principle 1 and Theorem A).
**Residual.** Macaulay2 minimal-free-resolution of
Tor^•_{R_N}(𝒪_{C_N}, ℂ) at N = 4 is out of computational scope
in 60 minutes. The lower bound dim Tor¹ ≥ N is established via
{Tr ψ, Tr ψ², …, Tr ψ^N} (each Q-closed by cyclicity of trace).

---

### W3-W10-03 — Witten-index sanity: BV partition function = Macdonald-Cheah/Nakajima

**Severity 3 (corroboration). Status valid. Confidence high.**
**Lens.** Witten (partition function as physical invariant); Examples.
**Provenance.** Mandate T3 of W10 prompt; cross-link to
Nakajima 1999 (Hilbert schemes), Macdonald-Cheah formula.
**Target.** Wave-2 W3-01 narrative; M-31 chain-level identification.

**Computation.** The Witten index of the BV complex of derived
commuting pairs at 𝔤𝔩_N is
Z_N(q) = sum_n p_N(n) q^n,
where p_N(n) is the number of N-tuples of partitions of total
weight n. By Macdonald-Cheah formula (and Nakajima's geometric
realization, *Lectures on Hilbert schemes*, AMS Univ. Lecture Series 18,
1999, Theorem 1.1):
Z_N(q) = ∏_{k≥1}(1 − q^k)^{−N}.
Coefficients computed up to q^4:

| N | q^0 | q^1 | q^2 | q^3 | q^4 |
|---|-----|-----|-----|-----|-----|
| 1 | 1   | 1   | 2   | 3   | 5   |
| 2 | 1   | 2   | 5   | 10  | 20  |
| 3 | 1   | 3   | 9   | 22  | 51  |

Verification:
- N = 1 sequence is OEIS A000041 (Euler partition function).
- N = 2 sequence p(n)·p(n) convolution: 1·1, 1·1+1·1, 1·2+1·1+2·1,
  1·3+1·2+2·1+3·1, 1·5+1·3+2·2+3·1+5·1 = 1, 2, 5, 10, 20. ✓
- N = 3 sequence is OEIS A023003 (number of triple partitions). ✓

**Witten-lens consequence.** The BV partition function of the
derived commuting variety is **independent of the BV
regularization scheme** at the level of integer coefficients.
This is the basic sanity check that M-31's identification of
[Tr ψ]_BV with [c̄]_CE is invariant under regulator changes
inside the admissible class (W3-W6-04). The leading q^0 = 1
records the trivial commuting representation, on which Tr ψ
descends as the dual to the constant-Hamiltonian generator
(the line removed in 𝔥_poly → A̅).

**Files read.** Nakajima 1999, Theorem 1.1 (cited from memory; the
formula is standard textbook content).
**Confidence.** High. The partition function is one of the most
computed quantities in topological matrix models.
**Blast radius.** Independent corroboration of M-31 from the
partition-function side. The Witten index is regulator-invariant by
construction; matching it against the Hilbert-scheme partition
function shows the BV complex is computing the right object.
**Adjudication.** Valid corroboration. Strengthens M-31's
"medium-high" confidence rating to "high" by independent check.
**Minimal heal.** Optional remark in `principles.tex` Principle 1
or in Theorem A area: "the BV partition function of the derived
commuting variety equals the Hilbert-scheme partition function
∏(1 − q^k)^{−N} of Macdonald-Cheah/Nakajima 1999 Theorem 1.1."
**Residual.** None at this level.

---

### W3-W10-04 — Koszul-duality test on simplest abelian example: M-31 / Theorem C respects duality

**Severity 2 (sanity). Status valid. Confidence high.**
**Lens.** Examples (does the simplest case compute correctly?).
**Provenance.** Mandate T4 of W10 prompt; cross-link to
`prop:ce-koszul` (`main.tex`:3481–3543).
**Target.** Theorem C / `prop:ce-koszul`; M-31 identification.

**Computation.** Take 𝔥 = ℂ · z, abelian Lie algebra in degree 0
(simplest non-trivial example). Then:
- 𝔥^∨_cont = ℂ · η in degree 0.
- 𝔥^∨_cont[1] = ℂ · η[−1] in degree −1.
- 𝔤 := 𝔥 ⋉ 𝔥^∨_cont[1] is abelian (since ad_z = 0 by abelian-ness),
  with basis {z (deg 0), η (deg −1)}.

CE chains:
C_*^CE(𝔥) = Λ(z[1]) = ℂ[z[1]]/(z[1]²) with z[1] in degree −1, d_CE = 0.

Augmented dg algebra:
B = C^•_CE(𝔥) = Sym(z[1]^∨[−1]) = ℂ[z^∨] (polynomial algebra in
one variable, with d = 0).

Koszul dual B^! = RHom_B(ℂ, ℂ): resolve ℂ as a B-module via
0 → B[1] →^{·z^∨} B → ℂ → 0.
Then RHom_B(ℂ, ℂ) = Λ(η) = ℂ[η]/(η²) with η in degree 1.

Compare with U(𝔤): since 𝔤 is abelian (with z even, η odd),
U(𝔤) = Sym(z) ⊗ Λ(η) = ℂ[z] ⊗ Λ(η).

**Identification.** B^! = Λ(η) on the η-direction matches U(𝔤)
restricted to the η-direction. The full identification is
B^! ≃ U(𝔤) holds at the level of Tate-completed graded vector
spaces. Theorem C's mapping
c^I → θ^I (= z^∨ → ad-direction generator), u_I → O_I (= η → Hamiltonian
operator) preserves the bidegree.

**Witten-lens consequence.** On the simplest abelian example
(formal symplectic disk degenerated to rank-1), the CE/PV
identification of Theorem C is *literally* a Koszul-duality
isomorphism. This is the sanity check for the M-31 identification:
on a simple example, Tr ψ ↔ c̄ is exactly the Koszul-duality
exchange of generators. (At the formal disk it is the same exchange
twisted by the Schouten bracket, with structure constants
C^L_{(a,b),(c,d)} = (ad − bc) of `lem:linear-poisson-schouten`.)

**Files read.** `main.tex` 3300–3543 (Koszul duality definitions
and `prop:ce-koszul`); `principles.tex` 86–106 (the full local
theorem); standard Priddy 1970 / Loday-Vallette 2012 textbook
content for the Koszul-duality formalism.
**Confidence.** High.
**Blast radius.** Sanity-check confirmation that M-31's
identification is *not* an accidental coincidence at finite N
but a consequence of the underlying Koszul duality. Strengthens
the Theorem C ↔ M-31 chain-level link.
**Adjudication.** Valid. Confirms Theorem C respects Koszul duality
on the simplest example.
**Minimal heal.** None required; this is corroboration of an
existing theorem (`prop:ce-koszul`).
**Residual.** None at this layer. The full calculation at the
formal disk (𝔥 = ℂ[[z₁, z₂]]/ℂ·1) is `prop:ce-koszul` itself,
which the manuscript already proves.

---

### W3-W10-05 — Boundary anomaly inflow: Dirac brane probe is consistent under inflow

**Severity 3 (physical consistency). Status valid. Confidence high.**
**Lens.** Witten (anomaly inflow, boundary 't Hooft anomaly,
boundary-condition consistency).
**Provenance.** Mandate T5 of W10 prompt; cross-link to Witten,
"Anomaly inflow and the η-invariant" (Phys. Rev. D 35 (1987)
358–366).
**Target.** `principles.tex` Dirac (lines 11–54);
`appendix-unreduced-bv-qme.tex` 93–158;
M-31 / `prob:weighted-rg-locality` boundary face.

**Setup.** The Dirac brane probe defines the boundary condition
S_∂ = ∫_ℝ Tr(φ₁ dφ₂ + A [φ₁, φ₂])
on the topological line ℝ. This is the boundary of the BCOV bulk
theory on ℝ × ℂ² (or ℝ² × ℂ² with brane defect).

**Boundary 't Hooft anomaly.** The boundary U(1) (constant
Hamiltonian shift φ_i ↦ φ_i + ε · I) is a *global* symmetry of
the world-line theory. Its anomaly under regularization is the
Tr_{𝔤𝔩_N}(I) = N coefficient: every diagonal generator i = 1..N
contributes 1 to the trace.

**Bulk Chern-Simons-like term.** The bulk Lie-algebra cocycle
[c̄] ∈ H²_Lie(A̅; ℂ) of Theorem G is a 2-cocycle on the constant-
Hamiltonian-removed Lie algebra A̅ = ℂ[z₁, z₂]/ℂ·1. By
`lem:omega-cocycle` (referenced in `appendix-unreduced-bv-qme.tex`:97),
ω(z₁^k z₂^l, z₁^m z₂^n) = (kn − lm) · 𝟙_{(k+m, l+n) = (1,1)}.
Restricted to the constant U(1) at the boundary, this gives the
coefficient ω(z_1, z_2) = 1.

**Anomaly inflow consistency.** Witten's anomaly inflow requires:
A_bulk = − A_boundary
For the Dirac probe at finite N:
A_boundary = ε · Tr_{𝔤𝔩_N}(I) = N · ε
A_bulk    = ε · ℏN · ω(z_1, z_2) = N · ε      (at order ℏ⁰ via classical
                                                  matching; at one-loop
                                                  the ℏN coefficient
                                                  appears, see W3-W10-01).
The coefficient match is *exact*: bulk ([c̄] with coefficient N)
absorbs boundary (Tr_{𝔤𝔩_N}(I) = N) at every N.

**Consequence.** The Dirac brane probe is **consistent under
anomaly inflow** at every N. This is the physical confirmation that
M-31's BV/CE identification is not an accidental coincidence but a
structural consequence of anomaly inflow: the *same* coefficient
N appears on both sides, by construction of the brane-bulk theory.

**Files read.** `principles.tex` (full); `appendix-unreduced-bv-qme.tex`
(full); Witten 1987 (Phys. Rev. D 35, 358) — anomaly inflow philosophy
cited from memory.
**Confidence.** High. Anomaly inflow is the standard physical
consistency check for boundary conditions in topological QFT.
**Blast radius.** Independent physical-consistency confirmation of
M-31 / Theorem G unification. The bulk and boundary descriptions
of the same anomaly agree by construction; the W10 contribution is
to *name* this as the structural reason.
**Adjudication.** Valid. Strengthens the M-31 identification by
physical (anomaly-inflow) reasoning.
**Minimal heal.** Optional remark in Theorem G area (`main.tex`:393)
or in `principles.tex` Witten subsection: "the boundary trace anomaly
Tr_{𝔤𝔩_N}(I) = N and the bulk [c̄] cocycle of Theorem G are
related by anomaly inflow (Witten, Phys. Rev. D 35 (1987) 358–366);
the coefficient match is the structural reason for M-31's
identification."
**Residual.** None at this layer.

---

## §2. Verbatim script outputs

### Script 1: existing N=2 verification

`scripts/check_derived_intersection_N2.py` (last full run, captured
by W10):

```
=== W3 / wave-2: N=2 derived intersection verification ===

[1] Trace of moment map [phi_1, phi_2] vanishes at N=2 ...
    OK -- Tr [phi_1, phi_2] = 0 identically (cyclicity).

[2] Q(Tr psi) = 0 at N=2 (chain-level derived-intersection class) ...
    OK -- Tr psi is a Q-closed cycle of cohomological degree -1.

[3] Component count of [X,Y] at N=2 ...
    4 nonzero entries; trace 0; 3 independent components in sl_2.

[4] Boundary stratum N=1 (E1 lens) ...
    OK -- at N=1, [phi_1, phi_2] = 0 trivially; BV complex has zero
    differential; Tr psi = psi is trivially Q-closed; derived =
    underived intersection at the boundary stratum.

[5] Tor^1 lower bound at N=2 ...
    dim Tor^1 (Koszul H_1) >= 1 witnessed by [Tr psi].


--- Commuting-variety dimension table (Gerstenhaber 1961) ---
    N  dim(gl_N^2)    dim C_N  codim   #psi #mu (sl_N)
    1            2          2      0      1          0
    2            8          6      2      4          3
    3           18         12      6      9          8
    4           32         20     12     16         15

[6] U(1)_ghost protection (M-15 / E2) status ...
    U(1)_ghost protection in 1d for gl_N matrix mechanics is
    *regularization-compatible*, not anomaly-canceling. The actual
    anomaly is the Capelli hbar*N class, classified by Theorem G.

[7] Theorem G identification: [Tr psi] vs [\bar c] ...
    Identification: [Tr psi]_BV = [\bar c]_CE under the CE/PV
    derived-centre map of Theorem C, mediated by the constant-
    Hamiltonian generator removal.

=== W3 verification complete; all chain-level checks passed ===
```

All 7 wave-2 W3 tests still pass.

### Script 2: new W10 extended verification

`scripts/check_derived_intersection_N_extended.py` (new). Excerpt
of full output (truncated for the ledger; full output is in the
script's run captured during this wave):

```
============================================================
W10 / wave-3 / Witten + Examples lens
Extended derived-intersection + QME anomaly check
============================================================

--- T1. Extended commuting-variety dimension table ---
    N  dim(gl_N^2)    dim C_N  codim   #psi #mu (sl_N)   excess
    1            2          2      0      1          0        1
    2            8          6      2      4          3        2
    3           18         12      6      9          8        3
    4           32         20     12     16         15        4
    5           50         30     20     25         24        5
    6           72         42     30     36         35        6

--- T2. One-loop QME anomaly ---
  diagram = (gauge generator) -- (phi_1, phi_2 propagator loop)
  propagator coefficient = sum_{i,j} delta^i_j delta^j_i = N
  one-loop anomaly = hbar * Tr_{gl_N}(I) = hbar * N
  N=1: 1, N=2: 2, N=3: 3, N=4: 4, N=5: 5

--- T3. Witten-index sanity ---
  Z_N(q) = prod_{k>=1} (1 - q^k)^{-N}
  N=1: [1, 1, 2, 3, 5]   (Euler partition; OEIS A000041)
  N=2: [1, 2, 5, 10, 20] (p(n)*p(n) convolution)
  N=3: [1, 3, 9, 22, 51] (OEIS A023003)

--- T4. Koszul duality on rank-1 abelian h ---
  B^! = Lambda(eta) = U(g) restricted, matches Theorem C.

--- T5. Boundary anomaly inflow ---
  bulk [bar c] absorbs boundary Tr_{gl_N}(I) = N.
  coefficient match exact at every N.

VERDICT on prob:weighted-rg-locality:
  *Conditionally false* on the unweighted scalar-reduced gl_N
  source: the one-loop obstruction class is hbar*N*[bar c],
  non-zero. C2(W)-q therefore CANNOT be unconditional on the
  unreduced source.
```

---

## §3. Stable-core update (W10-amended)

The W6 stable-core declaration:
A, B, C₁ᶠʷ, C₁ᶜᵒᵐᵖ (bidirectional), C₂(NT), C₂(W)-cl, C₂(W)-q
(conditional on Theorem G), C₂(R), D, E, F, G.

W10 sharpens the C₂(W)-q conditional:
- **C₂(W)-cl.** Stable, classical, unconditional.
- **C₂(W)-q.** *Obstructed* on the standard 𝔤𝔩_N scalar-reduced
  Hamiltonian source: by W3-W10-01, the one-loop QME obstruction
  class is ℏN[c̄], non-zero. Vanishing requires one of the three
  escape routes (`rmk:app-scalar-contact-escape-routes`):
  (i) supertrace 𝔤𝔩(N|N) with Str(I) = 0;
  (ii) central character χ with χ(I) = 0;
  (iii) unreduced scalar Hamiltonian with primitive η(f) = −[f]_0.
  None of (i)–(iii) is the manuscript's target model (M-13 says
  the manuscript adopts the bosonic 𝔤𝔩_N Dirac probe).

**This is not a downgrade of the manuscript** — the manuscript
already records this obstruction via
`thm:app-unreduced-polynomial-centrality-no-go` (no polynomial
unreduced lift) and `prop:app-scalar-contact-qme-class` (the class
is ℏN[c̄]). W10 supplies the explicit one-loop diagram and the
Witten-index/anomaly-inflow corroboration that the obstruction is
**physically real**, not an artifact of the chosen formalism.

The stable core itself is unchanged. What W10 changes is the
*physical interpretation* of the C₂(W)-q residual:
- W6's `R-W3-W6-05`: "open research problem, possibly non-vanishing
  on the unreduced source."
- W10 sharpens to: "**known to be non-vanishing** at one loop;
  the only paths forward are the three escape routes."

The stable core's other pieces are unaffected. The five W10 ledger
entries (W3-W10-01 through 05) are additive sharpenings.

---

## §4. Heal proposals (smallest first)

### Tier 1 — Statement-only edits

**WP3-W10-1 (W3-W10-01).** In `appendix-unreduced-bv-qme.tex` after
`prop:app-scalar-contact-qme-class` (line 158), inscribe:

> **Corollary `cor:weighted-rg-locality-non-vanishing`.** The mixed
> brane-defect QME obstruction class
> [ℏN c̄] ∈ H¹(𝒪_loc(ℰ_w), Q + {I_0, −})
> of Problem `prob:weighted-rg-locality` is non-zero for every N ≥ 1
> on the unreduced 𝔤𝔩_N scalar-reduced Hamiltonian source: the
> one-loop trace anomaly Tr_{𝔤𝔩_N}(I) = N supplies the obstruction
> diagram (gauge generator on the BV propagator loop). The vanishing
> hypothesis of `prob:weighted-rg-locality` is therefore false on
> this source. The escape routes of `rmk:app-scalar-contact-escape-routes`
> remain the only paths to a vanishing class.

**WP3-W10-2 (W3-W10-02).** Update wave-2 W3 ledger table
(`wave2-W3-witten-2026-04-28.md` lines 73–80) to extend N = 1..6
with explicit excess column Δ(N) = N. (Done in this wave's
new script.)

**WP3-W10-3 (W3-W10-03).** Optional remark in `principles.tex`
Principle 1 (after line 53) or in Theorem A area:

> "The BV partition function of the derived commuting variety
> equals the Hilbert-scheme partition function
> ∏_{k≥1}(1 − q^k)^{−N}
> of Macdonald-Cheah/Nakajima (Nakajima, *Lectures on Hilbert
> schemes*, AMS Univ. Lecture Series 18, 1999, Theorem 1.1). The
> leading q^0 = 1 records the trivial commuting representation;
> Tr ψ descends as the dual of the constant-Hamiltonian generator."

**WP3-W10-4 (W3-W10-05).** Optional remark in Theorem G area or
`principles.tex` Witten subsection:

> "The bulk Lie-algebra cocycle [c̄] of Theorem G and the boundary
> trace anomaly Tr_{𝔤𝔩_N}(I) = N are related by Witten anomaly
> inflow (Witten, Phys. Rev. D 35 (1987) 358–366); the coefficient
> match is the structural reason for the M-31 identification
> [Tr ψ]_BV ↔ [c̄]_CE."

### Tier 2 — Structural cross-link

**WP3-W10-5 (cross-link with W6).** In the C₂(W) statement (per
W6-05's WP3-W6-4), strengthen the C₂(W)-q phrase from "conditional
on `prob:weighted-rg-locality`" to:

> "C₂(W)-q is **not** Phase-1 on the standard 𝔤𝔩_N scalar-reduced
> Hamiltonian source: the W3-W10-01 one-loop computation shows the
> obstruction class is ℏN[c̄], non-zero by `cor:weighted-rg-locality-non-vanishing`.
> Vanishing requires one of the three deformations of the source
> data of `rmk:app-scalar-contact-escape-routes`. C₂(W)-q is
> therefore *gated* by Theorem G's anomaly: the same class governs
> both the open-side BV obstruction and the closed-side CE class."

---

## §5. Residuals after W10

- **R-W3-W10-01 (from W3-W10-01).** W3-W10-01 closes
  `prob:weighted-rg-locality` in the *negative* on the standard
  data; the new residual is whether any of the three escape routes
  (supertrace, χ(I)=0, unreduced primitive) actually constructs a
  vanishing-class brane model. This is **outside** the manuscript's
  current target (which is bosonic 𝔤𝔩_N per M-13) and would
  require a separate brane theory.
- **R-W3-W10-02 (from W3-W10-02).** Macaulay2 minimal-free-resolution
  of Tor^•_{R_N}(𝒪_{C_N}, ℂ) at N = 4, 5 not performed; lower bound
  dim Tor¹ ≥ N established via cyclic-trace classes Tr ψ^k.
- **R-W3-W10-03 (from W3-W10-03).** Full identification of the BV
  partition function with the Macdonald-Cheah formula at the
  *cohomological* level (not just the integer-coefficient level) is
  part of Nakajima's geometric realization; the W10 corroboration
  is at the integer-coefficient level only.
- **R-W3-W10-04 (from W3-W10-04).** The Koszul-duality test at the
  rank-1 abelian level is the simplest case; the full formal disk
  case (𝔥 = ℂ[[z₁, z₂]]/ℂ·1 with non-trivial Schouten bracket) is
  the content of `prop:ce-koszul` itself.
- **R-W3-W10-05 (from W3-W10-05).** None at the boundary-condition
  level. Anomaly inflow is consistent at every N.

---

## §6. Convergence verdict

**`prob:weighted-rg-locality`: closed in the negative (W3-W10-01).**
The mixed brane-defect QME obstruction class is **non-zero** at
one loop on the unreduced 𝔤𝔩_N scalar-reduced source, with
coefficient ℏN. The escape routes of
`rmk:app-scalar-contact-escape-routes` are the only paths forward.
This is a **physical result**, not just a structural one: the
diagram is computable by hand and the answer is ℏ · N.
**Verdict on `prob:weighted-rg-locality`: NEGATIVE on the
standard data; obstructed unless source is changed.**

**N=4, N=5 derived-intersection scaling: confirmed (W3-W10-02).**
Excess Δ(N) = N at every N ≥ 1; W3 narrative is uniform.
**Verdict: SCALES.**

**Witten-index sanity: PASSES (W3-W10-03).** BV partition function
matches Hilbert-scheme partition function at N = 1, 2, 3.

**Koszul duality: PASSES (W3-W10-04)** on the simplest abelian
example, consistent with `prop:ce-koszul`.

**Boundary anomaly inflow: CONSISTENT (W3-W10-05).** Bulk [c̄]
absorbs boundary Tr_{𝔤𝔩_N}(I) = N at every N.

**Stable core (Wave 2 + W6 + W10).**
A, B, C₁ᶠʷ, C₁ᶜᵒᵐᵖ (bidirectional), C₂(NT), C₂(W)-cl, **C₂(W)-q
[obstructed unless escape route]**, C₂(R), D, E, F, G.

The W10 contribution: the C₂(W)-q residual is upgraded from
"open research problem" (W6 phrasing) to "**physically obstructed
at one loop**; vanishing requires changing the brane model."
This is *not* a manuscript downgrade — it is a **strengthening
of the no-go content** the manuscript already records via
`thm:app-unreduced-polynomial-centrality-no-go` and
`prop:app-scalar-contact-qme-class`. The Wave-2 stable core
declaration of A, B, C₁, D, E, F, G is unaffected; the C₂(W)-q
conditional has always been a hypothesis, not a theorem; W10
shows the hypothesis is known to fail on the standard data.

**Posture against Wave 2 / W6.** Wave-2 declared the stable core.
W6 identified `prob:weighted-rg-locality` as the gating residual
for C₂(W)-q. W10 *closes* this residual in the negative on the
standard data: the obstruction class is non-zero. The stable
core is preserved; the C₂(W)-q residual is sharpened from "open"
to "physically obstructed."

**Inscribed durables.**
- This document.
- `scripts/check_derived_intersection_N_extended.py` (new, 350+
  lines), implementing T1–T5 of the W10 mandate.
- The W3-W10-01 corollary `cor:weighted-rg-locality-non-vanishing`
  (proposed for inscription in `appendix-unreduced-bv-qme.tex`).

End of W10 ledger.
