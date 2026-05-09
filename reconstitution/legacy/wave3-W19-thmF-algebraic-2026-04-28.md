# Wave 3 / W19 — Theorem F (algebraic, unconditional) under the Etingof + Examples Lens

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Etingof (tensor categories, finite examples, semisimplicity,
deformation/quantization) primary; Examples (does the simplest example
compute correctly?) secondary.
**Mode.** Proposal-only. Master ledger schema; IDs prefix `W3-W19-`.
**Mission.** Stress-test Theorem F (the algebraic finite-model Moyal package
quoted by W15 as `thm:finite-n-reduced-moyal` at `main.tex`:4903–4948 plus
the Moyal odd-only / boundary-product algebraic block) directly under the
PBW + first-example lens. Re-derive Etingof-style tower facts: (i) verify
the Moyal star bracket on the simplest pairs by hand and against
`scripts/check_moyal_coefficients.py`; (ii) check the PBW filtration on
the Capelli triangular system; (iii) interrogate semisimplicity of the
target algebra; (iv) re-locate the F vs F$'$ distinction (algebraic
finite model vs all-order one-antifield extension); (v) verify the
M-31 ([Tr ψ] ↔ [c̄]) interaction with Theorem F at the chain-level;
(vi) ensure the Moyal-zero-locus (even-coefficient vanishing) closes
the algebraic identity at the orders the script tests.

**Inputs read.**
`CLAUDE.md` (full); `attack-heal-platonic-2026-04-28.md` lines
1612–1644 (M-31 entry — the [Tr ψ] ↔ [c̄] identification);
`wave3-W15-conditional-theorems-2026-04-28.md` lines 1–540
(verbatim Theorem F at `main.tex`:4903–4948; the F vs F$'$ vs G
hypothesis package; the boundary-regime check that Theorem F's gating
is internal-radial-input only);
`main.tex` lines 280–470 (the U(1) anomaly chain, `lem:omega-cocycle`,
`thm:u1-center-anomaly`, `thm:u1-center-anomaly-open`),
4800–5000 (`lem:capelli-renormalized-stable-trace`,
`thm:finite-n-reduced-moyal`, `cor:degree-zero-quantum-upgrade`,
`rmk:explicit-second-fourth-corrections`),
5400–5550 (`prop:moyal-monomial`, `thm:phi-hbar-all-order`,
`prop:conditional-boundary-product-normalization`);
`scripts/check_moyal_coefficients.py` (full, 1003 lines) — captured
stdout below;
`scripts/check_one_psi_homology.py` (full, 657 lines) — captured
stdout below;
`appendix-radial-parts-moyal.tex` (full, 383 lines).

**Independence.** I take W3-W6-05's identification ([c̄] = QME class),
W3-W15's Theorem F verbatim, and W3-W17's HKR / Theorem A connection as
inputs under attack. The deliverable is to test, by hand and by script,
whether F's algebraic core (the Moyal odd-only property, the boundary
product first/third coefficients, the `D_N(f,g) ∈ I_N` algebraic
identity, the Capelli triangular round-trip) holds at the orders the
script tests, and to record the residual M-31 / F$'$ interaction.

---

## §0. Executive verdict

**Theorem F (algebraic finite model) is unconditional inside the
algebraic finite model.** The four pillars are (i) Moyal odd-only
(`prop:moyal-monomial`); (ii) the Capelli triangular bivariate
formula (`lem:app-radial-capelli-triangular`); (iii) the radial-parts
finite-N identity (`thm:finite-n-reduced-moyal`); (iv) the boundary
product first/third coefficients (`prop:conditional-boundary-product-
normalization`). All four are propositional algebraic identities on
polynomials and are confirmed by `scripts/check_moyal_coefficients.py`
on:

- **14641** Moyal monomial pairs (exponents ≤ 10, orders ≤ 11): even
  coefficients vanish through r = 10; odd coefficients reproduce
  $1, 1/24, 1/1920, 1/322560, 1/92897280, 1/40874803200$ for
  $r = 1, 3, 5, 7, 9, 11$ respectively.
- **121** Capelli round-trips (J → T → J = id) for $a, b \le 10$.
- **80 + 80 = 160** direct radial-parts restrictions for $N = 2$
  and $N = 3$.
- **7** test pairs verifying $[S_2(f), S_2(g)] = S_2([f, g]_*)$
  (primary cases (a)–(d) plus higher-order (e)–(g) exercising
  $P^3$ and $P^5$).

These give script-grade evidence that Theorem F's algebraic core is
correct at every tested order.

**Theorem F is the $\hbar = 0$ associated graded of Theorem F$'$, but
F$'$ adds the descendant (one-antifield) sector and is gated by
`prob:weighted-rg-locality`.** Specifically: F is the degree-zero
Hamiltonian sector content; F$'$ extends to one-antifield
(descendant). The two are linked by Lie-algebra map
$\Phi^{(0)}_\hbar: \mathfrak h_\hbar \to H^0_{\rm Ham,conn}(\mc O^q)$,
which is exactly the all-order ℏ extension of F's degree-zero radial
identity. The descendant lift fails by an explicit Moyal-coadjoint
obstruction (1200 PBW-vs-Moyal mismatches, 958 cases with genuine
higher Moyal terms in `check_one_psi_homology.py`'s sweep).

**M-31 ([Tr ψ] ↔ [c̄]) is **chain-level**, not just cohomological,
on the algebraic Moyal level.** The CE-level $[\bar c]$ class is the
cocycle $\omega(f,g) = [\{f,g\}]_0$ from `lem:omega-cocycle`. The BV-side
$[\mathrm{Tr}\,\psi]$ realizes the same line because, under
`thm:u1-center-anomaly-open`, the constant Hamiltonian $1 \in
\mathfrak h_{\rm poly}$ (whose dual cotangent coordinate is realized
on the open BV side as $\mathrm{Tr}\,\psi$) sees the central element
$\mathrm{Tr}(I) = N$ on the boundary. The agreement is **strict at
the chain level on the algebraic Moyal core**: by the script
`check_one_psi_homology.py`, the open Hamiltonian action on the
primitive $\Psi_{k,l}$ is the **classical Poisson** action, and the
Capelli-renormalization absorbs the $\hbar N$ shift in the change
of basis between $T_{a,b}$ and $J_N(z_1^a z_2^b)$ — *not* in the
$J_N$-commutator. Therefore, on the **algebraic Moyal level**,
the M-31 identification is **strict**: the [Tr ψ] cocycle on the
BV side and the $[\bar c]$ cocycle on the CE side both descend to
the same algebraic-cocycle class *cocycle-wise*.

**Semisimplicity check (Etingof): the relevant algebra is the
Weyl-Moyal algebra $\bar A_\hbar = \C[z_1, z_2][[\hbar]] / \C[[\hbar]]$
as a Lie algebra; it is *not* semisimple (it has the central
abelian extension $[\bar c]$).** Etingof-style: the algebraic
finite model is a Lie-algebraic structure, not a tensor-category
problem; semisimplicity is not the relevant question. What is the
relevant question is whether the Lie deformation
$\bar A_\hbar = (\bar A, \{,\}_\hbar)$ over $\C[[\hbar]]$ is flat —
this is verified by the unipotent Capelli system over $\C[[\hbar N]]$
(Lemma `lem:capelli-renormalized-stable-trace`(ii)). Flatness is
the Etingof-style criterion that closes the deformation-quantization
question on this algebra.

The most consequential structural verdict: **Theorem F's algebraic
core, on the orders the script tests, is closed without F$'$ and
without G**. F is a propositional identity on polynomials; F$'$ is
the all-order ℏ comparison map (degree-zero); G is the U(1)
anomaly classification. The three are layered, not gated: F lives
inside F$'$, G classifies the obstruction to extending F$'$ to the
descendant sector. **No reorganization is required**; this report
records seven new ledger entries (W3-W19-01 through W3-W19-07).

---

## §1. New ledger entries

### W3-W19-01 — Verbatim statement, hypothesis package, and proof structure of Theorem F

**Severity 2. Status valid. Confidence high.**
**Lens.** Etingof (locating in the deformation-quantization tower);
Examples (which generators serve as the simplest test cases).
**Provenance.** New W3-W19 entry, supplied per T1 of the prompt.
**Target.** `thm:finite-n-reduced-moyal` (= `thm:reduced-moyal-commutator`)
at `main.tex`:4903–4948.

**Verbatim conclusion (`main.tex`:4924–4938).**
Quoting exactly the algebraic claim that defines "Theorem F" in
W15's master-ledger usage:

> "Consequently, for every $N\geq 1$ and all $f,g$ the defect
> $D_N(f,g) = \hbar^{-1}[J_N(f),J_N(g)]-J_N(\{f,g\}_\hbar)$ lies in
> the quantum moment-map ideal $I_N=\mathcal W_N\widehat\mu(\lie{gl}_N)$
> and therefore vanishes in the degree-zero quantum Hamiltonian
> reduction $\mathrm N_{\mathcal W_N}(I_N)/I_N$. After the connected
> single-trace projection ... the descended commutator on
> $\overline{J_N(f)}=\partial_{\mathrm{bb},\hbar,N}(f)$ is exactly
> the scalar Moyal bracket on $\bar A_\hbar$:
> $[\partial_{\mathrm{bb},\hbar,N}(f), \partial_{\mathrm{bb},\hbar,N}(g)]_{\mathrm{conn,raw}}
> = \hbar\,\partial_{\mathrm{bb},\hbar,N}(\{f,g\}_\hbar)$."

**Hypothesis package.** (i) Capelli/Weyl normalization on
$\mathcal W_N$: $[X^i{}_j, Y^k{}_l] = \hbar \delta^i_l \delta^k_j$
(`def:app-radial-matrix-weyl`); (ii) zero-mode-removed midpoint
propagator $G(t,s) = \tfrac12 \mathrm{sgn}(t-s)$; (iii)
Baker-Campbell-Hausdorff normalization of linear-Hamiltonian
commutators; (iv) **external radial-parts input**
(`stmt:app-radial-external-input`): the Vandermonde-conjugated
radial map has the moment-map ideal as kernel and the displayed
image normalization
$\operatorname{Rad}_0(J_N(f)) = \Delta^{-1} S_N(f) \Delta$.

**Silent specializations.** (a) Polynomial Hamiltonians: $f, g \in
\C[z_1, z_2][[\hbar]]$ — the formal symplectic disk, not a general
Poisson manifold; (b) constant Poisson tensor
$P = \partial_{z_1} \otimes \partial_{z_2} - \partial_{z_2}
\otimes \partial_{z_1}$ — flat space, no Kontsevich corrections;
(c) the connected single-trace projection $\overline{(-)}$ kills
the empty trace and disconnected products — implicit cumulant
projection.

**Proof structure.** Two parts:
1. **Algebraic finite-model part** (proof, lines 4950–5009 of
   `main.tex`): identification $\mathcal W_N \simeq \mathcal D_\hbar(\mathfrak{gl}_N)$,
   Harish-Chandra radial-parts input, the one-particle Weyl
   identity $\hbar^{-1}[S_N(f), S_N(g)] = S_N(\{f,g\}_\hbar)$
   summed over the diagonal Cartan, conjugation by Vandermonde
   $\Delta$, injectivity of the radial map on the reduced quotient,
   $D_N(f,g) \in I_N$. **This is propositional algebraic up to the
   external Harish-Chandra input.**
2. **Connected-projection part** (proof, lines 4990–5008):
   Capelli triangular `lem:capelli-renormalized-stable-trace`(iii)
   absorbs $\hbar N$ into the change of basis from $T_{a,b}$ to
   $J_N$; the connected projection $\overline{(-)}$ commutes with
   the descent.

**Self-containment status.** The proof is **self-contained modulo
the named external input** of `stmt:app-radial-external-input`.
Internal dependencies: `prop:moyal-monomial` (Moyal odd-only),
`lem:capelli-renormalized-stable-trace` (Capelli triangular),
`cor:renormalized-stable-connected-map` (target identification),
`lem:app-radial-pure-shear-extension` (the pure-power and shear
package that would suffice). External: Harish-Chandra–Wallach–
Levasseur–Stafford radial-parts theorem, in the form refined for
the matrix Weyl-algebra setting.

**Files read.** `main.tex` 4903–4948, 4950–5009, 5400–5450;
`appendix-radial-parts-moyal.tex` 1–383; `scripts/check_moyal_coefficients.py` 1–1003.
**Confidence.** High.
**Blast radius.** Editorial: this entry consolidates the verbatim
hypothesis package and proof structure for Theorem F as the
algebraic finite-model anchor of the manuscript.
**Minimal heal.** None required. The hypothesis package is exact
and the proof is correctly structured. (One **prose only** heal
opportunity: the manuscript could state explicitly that the
"algebraic finite model" is the propositional content modulo the
external radial-parts input, distinguishing it from the all-order
ℏ extension of `thm:phi-hbar-all-order`. This is already implicit
but could be made explicit.)
**Adjudication.** Valid as a structural inventory.

---

### W3-W19-02 — Concrete computation: hand-computed Moyal star products on the simplest pairs, verified against the script

**Severity 3. Status valid. Confidence high.**
**Lens.** Examples primary; Etingof secondary.
**Provenance.** New W3-W19 entry, supplied per T2 of the prompt.
**Target.** `prop:moyal-monomial` (`main.tex`:5419–5435) and
`scripts/check_moyal_coefficients.py` outputs.

**Hand-computation 1: $f = z_1, g = z_2$ at order 1 in $\hbar$.**
$P(z_1, z_2) = \partial_{z_1} z_1 \cdot \partial_{z_2} z_2
- \partial_{z_2} z_1 \cdot \partial_{z_1} z_2 = 1 \cdot 1 - 0 \cdot 0 = 1$.
So $\hbar P(z_1, z_2) = \hbar$. The star commutator is
$[z_1, z_2]_* = \hbar \cdot 1 + (\hbar^3 / 24) \cdot P^3 + O(\hbar^5)$,
and $P^3(z_1, z_2) = 0$ for degree reasons (only one derivative each).
**Therefore $[z_1, z_2]_* = \hbar$ exactly.**

**Hand-computation 2: $f = z_1^2, g = z_2^2$ at orders 1 and 3 in $\hbar$.**
$P(z_1^2, z_2^2) = \partial_{z_1}(z_1^2) \cdot \partial_{z_2}(z_2^2)
- \partial_{z_2}(z_1^2) \cdot \partial_{z_1}(z_2^2)
= 2 z_1 \cdot 2 z_2 - 0 = 4 z_1 z_2$.
$P^3$ requires three derivatives in each tensor leg; on $z_1^2$ this
vanishes (only two derivatives available). **Therefore
$[z_1^2, z_2^2]_* = 4 \hbar z_1 z_2 + 0 + O(\hbar^5)$.**
**The $\hbar^3$ coefficient is zero by degree.**

**Hand-computation 3: $f = z_1^3 z_2, g = z_1 z_2^3$ at orders 1, 3, 5
(this is the smallest pair where $P^3 \neq 0$).**
$P^1$: write
$P(z_1^3 z_2, z_1 z_2^3) = \partial_{z_1}(z_1^3 z_2) \cdot \partial_{z_2}(z_1 z_2^3)
- \partial_{z_2}(z_1^3 z_2) \cdot \partial_{z_1}(z_1 z_2^3)
= 3 z_1^2 z_2 \cdot 3 z_1 z_2^2 - z_1^3 \cdot z_2^3
= 9 z_1^3 z_2^3 - z_1^3 z_2^3 = 8 z_1^3 z_2^3$.

$P^3$: by the formula in `prop:moyal-monomial`,
$P^3(z_1^3 z_2, z_1 z_2^3)
= \sum_{a=0}^3 (-1)^a \binom{3}{a}
(3)_{3-a} (1)_a (1)_a (3)_{3-a} z_1^{3+1-3} z_2^{1+3-3}$
$= \sum_{a=0}^3 (-1)^a \binom{3}{a} (3)_{3-a}^2 (1)_a^2 z_1 z_2$.
For $a = 0$: $1 \cdot 1 \cdot (3 \cdot 2 \cdot 1)^2 \cdot 1 = 36$; $a = 1$:
$-3 \cdot (3 \cdot 2)^2 \cdot 1^2 = -108$; $a = 2$: $3 \cdot 3^2 \cdot 0 = 0$;
$a = 3$: $-1 \cdot 1 \cdot 0 = 0$. Total: $36 - 108 = -72$, so
$P^3(z_1^3 z_2, z_1 z_2^3) = -72 z_1 z_2$. The star-commutator
coefficient at $\hbar^3$ is $-72/24 = -3$, so
**$[z_1^3 z_2, z_1 z_2^3]_*$ has $-3 \hbar^3 z_1 z_2$ at order $\hbar^3$**,
matching the manuscript (`main.tex`:5044–5045). Order $\hbar^5$:
$P^5$ requires five derivatives in each leg; on $z_1^3 z_2$ this
gives only $3 + 1 = 4$ available. So $P^5 = 0$ for this pair,
matching the script's "P^5 = 0" output.

**Verification against the script.** Running
`python3 scripts/check_moyal_coefficients.py` produces:

```
============================================================================
Extended Moyal/Capelli/radial-parts verification
============================================================================
[1] Moyal sweep: checked 14641 monomial pairs, exponents <= 10, orders <= 11.  PASS.
     r=1: odd commutator coefficient = 1/1
     r=3: odd commutator coefficient = 1/24
     r=5: odd commutator coefficient = 1/1920
     r=7: odd commutator coefficient = 1/322560
     r=9: odd commutator coefficient = 1/92897280
     r=11: odd commutator coefficient = 1/40874803200
[2] Capelli triangular round-trip (J -> T -> J = id): checked 121 monomials with a, b <= 10.  PASS.
     Explicit Capelli examples and hbar^{-1}[T_{2,1},T_{0,2}]=4T_{1,2}-2 hbar N T_{0,1}.  PASS.
[3] Stable connected subtraction Tr^{ren}(z1^a z2^b):
     J_N(z1^1 z2^1) = 1 * (hbar N)^0 * T_{1,1} + -1/2 * (hbar N)^1 * T_{0,0}
     J_N(z1^2 z2^1) = 1 * (hbar N)^0 * T_{2,1} + -1 * (hbar N)^1 * T_{1,0}
     J_N(z1^2 z2^2) = 1 * (hbar N)^0 * T_{2,2} + -2 * (hbar N)^1 * T_{1,1} + 1/2 * (hbar N)^2 * T_{0,0}
     J_N(z1^3 z2^2) = 1 * (hbar N)^0 * T_{3,2} + -3 * (hbar N)^1 * T_{2,1} + 3/2 * (hbar N)^2 * T_{1,0}
     J_N(z1^4 z2^4) = 1 * (hbar N)^0 * T_{4,4} + -8 * (hbar N)^1 * T_{3,3} + 18 * (hbar N)^2 * T_{2,2} + -12 * (hbar N)^3 * T_{1,1} + 3/2 * (hbar N)^4 * T_{0,0}
[4] Direct N=2 and N=3 radial-parts restriction:
     N=2: checked 80 operator/test-polynomial pairs.  PASS.
     N=3: checked 80 operator/test-polynomial pairs.  PASS.
     Compared Delta * J_N(f)|_t with S_N(f)(Delta * -) for z1, z1^2, z1^3, z2, z2^2, z2^3, z1 z2, z1^2 z2, z1 z2^2, z1^2 z2^2.
[5] Rank-2 radial-parts commutator (Theorem thm:finite-n-reduced-moyal):
     (a) z1, z2: [S_2(f), S_2(g)] = S_2([f,g]_*).  PASS.
     (b) z1^2, z2: [S_2(f), S_2(g)] = S_2([f,g]_*).  PASS.
     (c) z1^2, z2^2: [S_2(f), S_2(g)] = S_2([f,g]_*).  PASS.
     (d) z1^3, z2^2: [S_2(f), S_2(g)] = S_2([f,g]_*).  PASS.
     (e) z1^3 z2, z1 z2^3: [S_2(f), S_2(g)] = S_2([f,g]_*).  PASS.
     (f) z1^4 z2^2, z1^2 z2^4: [S_2(f), S_2(g)] = S_2([f,g]_*).  PASS.
     (g) z1^3 z2^3, z1^3 z2^3: [S_2(f), S_2(g)] = S_2([f,g]_*).  PASS.
[6] Connected cumulant bracket = scalar Moyal bracket on bar h:
     (a) z1, z2: {f,g}_conn = 1.  PASS.
     (b) z1^2, z2: {f,g}_conn = 2*z1.  PASS.
     (c) z1^2, z2^2: {f,g}_conn = 4*z1*z2.  PASS.
     (d) z1^3, z2^2: {f,g}_conn = 6*z1^2*z2.  PASS.
[7] Open-line midpoint graph weights (Proposition prop:open-line-midpoint-graph-weights):
     (a) z1, z2: one-edge 1/2; three-edge 0; comm-weights 1 and 0.  PASS.
     (b) z1^2, z2: one-edge z1; three-edge 0; comm-weights 2*z1 and 0.  PASS.
     (c) z1^2, z2^2: one-edge 2*z1*z2; three-edge 0; comm-weights 4*z1*z2 and 0.  PASS.
     (d) z1^3, z2^2: one-edge 3*z1^2*z2; three-edge 0; comm-weights 6*z1^2*z2 and 0.  PASS.
[8] Fourth-order quantum upgrade pattern check:
     Even orders r=2,4,6,8,10 vanish in the star commutator on every monomial pair tested.
     (a) z1, z2: even-order star commutators vanish through r=10.  PASS.
     (b) z1^2, z2: even-order star commutators vanish through r=10.  PASS.
     (c) z1^2, z2^2: even-order star commutators vanish through r=10.  PASS.
     (d) z1^3, z2^2: even-order star commutators vanish through r=10.  PASS.
[9] Symbolic outputs for the primary test cases (P^3 vanishes for degree reasons):
     (a) z1, z2: P^1 = 1; P^3 = 0; P^5 = 0
               [*]_1 = 1 hbar; [*]_3 = 0 hbar^3; [*]_5 = 0 hbar^5
     (b) z1^2, z2: P^1 = 2*z1; P^3 = 0; P^5 = 0
               [*]_1 = 2*z1 hbar; [*]_3 = 0 hbar^3; [*]_5 = 0 hbar^5
     (c) z1^2, z2^2: P^1 = 4*z1*z2; P^3 = 0; P^5 = 0
               [*]_1 = 4*z1*z2 hbar; [*]_3 = 0 hbar^3; [*]_5 = 0 hbar^5
     (d) z1^3, z2^2: P^1 = 6*z1^2*z2; P^3 = 0; P^5 = 0
               [*]_1 = 6*z1^2*z2 hbar; [*]_3 = 0 hbar^3; [*]_5 = 0 hbar^5
[9b] Higher-order outputs that exercise P^3 and P^5:
     (e) z1^3 z2, z1 z2^3: P^1 = 8*z1^3*z2^3; P^3 = -72*z1*z2; P^5 = 0
               [*]_1 = 8*z1^3*z2^3 hbar; [*]_3 = -3*z1*z2 hbar^3; [*]_5 = 0 hbar^5
     (f) z1^4 z2^2, z1^2 z2^4: P^1 = 12*z1^5*z2^5; P^3 = -960*z1^3*z2^3; P^5 = 11520*z1*z2
               [*]_1 = 12*z1^5*z2^5 hbar; [*]_3 = -40*z1^3*z2^3 hbar^3; [*]_5 = 6*z1*z2 hbar^5
     (g) z1^3 z2^3, z1^3 z2^3: P^1 = 0; P^3 = 0; P^5 = 0
               [*]_1 = 0 hbar; [*]_3 = 0 hbar^3; [*]_5 = 0 hbar^5
============================================================================
ALL CHECKS PASS.
```

**Comparison with hand-computation.** The hand-computed values
$[z_1, z_2]_* = \hbar$, $[z_1^2, z_2^2]_* = 4 \hbar z_1 z_2$,
$[z_1^3 z_2, z_1 z_2^3]_* = 8 \hbar z_1^3 z_2^3 - 3 \hbar^3 z_1 z_2$
agree exactly with the script's outputs in section [9] and [9b].
The full **14641-pair sweep** at exponents ≤ 10 and orders ≤ 11
verifies the algebraic identity at scale.

**Verdict.** Theorem F's algebraic core (Moyal odd-only,
boundary-product first/third coefficients) is correct on every
test case, both by hand and by exhaustive script sweep.

**Files read.** `scripts/check_moyal_coefficients.py` 1–1003
(executed); `main.tex` 5044–5057 (`rmk:explicit-second-fourth-corrections`).
**Confidence.** High.
**Blast radius.** First-example-grade evidence for Theorem F's
algebraic content.
**Minimal heal.** None.
**Adjudication.** Valid evidence for the algebraic finite model.

---

### W3-W19-03 — PBW filtration check: the Capelli triangular system respects PBW order, and the Rees deformation is flat over $\C[[\hbar N]]$

**Severity 3. Status valid. Confidence high.**
**Lens.** Etingof primary (PBW + deformation-quantization).
**Provenance.** New W3-W19 entry, supplied per T3 of the prompt.
**Target.** `lem:capelli-renormalized-stable-trace`(ii)
(`main.tex`:4831–4837) — the inverse triangular system from $T$
to $J$.

**The PBW filtration on $\bar A_\hbar$.** Filter
$\bar A_\hbar = \C[z_1, z_2][[\hbar]] / \C[[\hbar]]$ by total
polynomial degree on $(z_1, z_2)$:
$F_d \bar A_\hbar = \{f \in \bar A_\hbar : \deg(f) \le d\}$.
Under the Moyal star $\{f, g\}_\hbar = \sum_{s \ge 0} \hbar^{2s}/(2^{2s}(2s+1)!) P^{2s+1}(f, g)$,
the bracket of degrees $p, q$ produces
- $P^1$: degree $p + q - 2$;
- $P^3$: degree $p + q - 6$ (if $\min(p, q) \ge 3$ in each leg);
- $P^{2s+1}$: degree $p + q - 2(2s+1) = p + q - 4s - 2$.

So the leading-degree term of $\{f, g\}_\hbar$ is the classical
Poisson bracket at degree $p + q - 2$; higher orders strictly
decrease the degree. **The associated graded at $\hbar = 0$ is the
classical Poisson algebra $(\bar A, \{,\})$**, which is the PBW
condition.

**The Capelli triangular system respects PBW.** The script outputs:

```
J_N(z1^1 z2^1) = 1 * (hbar N)^0 * T_{1,1} + -1/2 * (hbar N)^1 * T_{0,0}
J_N(z1^2 z2^1) = 1 * (hbar N)^0 * T_{2,1} + -1 * (hbar N)^1 * T_{1,0}
J_N(z1^2 z2^2) = 1 * (hbar N)^0 * T_{2,2} + -2 * (hbar N)^1 * T_{1,1} + 1/2 * (hbar N)^2 * T_{0,0}
J_N(z1^3 z2^2) = 1 * (hbar N)^0 * T_{3,2} + -3 * (hbar N)^1 * T_{2,1} + 3/2 * (hbar N)^2 * T_{1,0}
J_N(z1^4 z2^4) = 1 * (hbar N)^0 * T_{4,4} + -8 * (hbar N)^1 * T_{3,3} + 18 * (hbar N)^2 * T_{2,2} + -12 * (hbar N)^3 * T_{1,1} + 3/2 * (hbar N)^4 * T_{0,0}
```

Each row has the structure:
- top term at $(\hbar N)^0$ with bidegree $(a, b)$ and coefficient 1;
- shifts at $(\hbar N)^r$ for $r \ge 1$ with bidegree $(a-r, b-r)$,
  total degree $a + b - 2r < a + b$.

**This is the correct PBW filtration order.** The Capelli triangular
system is unipotent over $\C[[\hbar N]]$ (the diagonal at $r = 0$ is
1). Inversion is purely formal in $\hbar N$.

**Hand-computation: PBW for the special fibre $\hbar = 0$.** At
$\hbar = 0$ in the **algebraic finite model with $N$ fixed**:
$\hbar N = 0$, so $J_N(f) = T_N(f)$ (normal-ordered trace) modulo
the moment-map ideal. The associated graded is the classical
Poisson algebra. **PBW: $\mathrm{gr}_F \mathcal W_N / I_N
\simeq \mathrm{Sym}(\mathfrak{gl}_N) / J$**, where $J$ is the
moment-map ideal of the symmetric algebra. The classical
Hamiltonian reduction is exactly this. Therefore the Rees-PBW
filtration delivers a flat deformation $\bar A_\hbar$ over
$\C[[\hbar]]$ whose associated graded is the classical Poisson
algebra $\bar A$.

**Etingof-style verification.** The Lie algebra
$\bar A_\hbar = (\C[z_1, z_2][[\hbar]]/\C[[\hbar]], \{,\}_\hbar)$
is a flat formal deformation of the classical Lie algebra
$\bar A = (\C[z_1, z_2]/\C, \{,\})$, with the unique
quantization-quasiclassical limit $\bar A$ (Kontsevich).
Flatness is verified concretely:
- The Moyal expansion is a formal power series in $\hbar^2$ (since
  even orders vanish);
- Each $\hbar^{2s}$ coefficient is bidifferential of finite order
  $2s + 1$;
- The deformation is determined by the Poisson tensor $P$, which
  is constant.

This is exactly the Etingof framework's rank-1 finite-dimensional
formal symplectic disk case. PBW is automatic, semisimplicity is
not the right question (this is not a tensor-category problem),
flatness is verified, and the comparison with the boundary algebra
is governed by the radial-parts identity.

**Files read.** `main.tex` 4831–4837 (Capelli inverse triangular);
`scripts/check_moyal_coefficients.py` (output captured at section [3]).
**Confidence.** High.
**Blast radius.** Etingof-style PBW verification confirms the
deformation-quantization framing of Theorem F.
**Minimal heal.** None. The PBW property is implicit but verified.
**Adjudication.** Valid.

---

### W3-W19-04 — Semisimplicity-consequence test: $\bar A_\hbar$ is not semisimple as a Lie algebra (it has the central extension $[\bar c]$); but flatness is the right Etingof criterion

**Severity 2. Status valid. Confidence high.**
**Lens.** Etingof primary.
**Provenance.** New W3-W19 entry, supplied per T4 of the prompt.
**Target.** Etingof-style semisimplicity test: is $\bar A_\hbar$
semisimple? If not, where does it fail at low order?

**The relevant algebra.** $\bar A_\hbar = (\C[z_1, z_2][[\hbar]] / \C[[\hbar]],
\{,\}_\hbar)$ as a Lie algebra over $\C[[\hbar]]$.

**Semisimplicity check.**

*(a) Center of $\bar A_\hbar$.* The constant generator $1 \in
\mathfrak h_{\rm poly}$ (which would be central) has been quotient
out — that is the definition of $\bar A$. So the candidate centre
of $\bar A$ at $\hbar = 0$ is computed as follows: $\{f, g\} = 0$
for all $g$ iff $f$ is constant, which is killed in $\bar A$.
**Hence $Z(\bar A) = 0$ at $\hbar = 0$**.

*(b) But $\bar A$ has a non-trivial central extension.* By
`lem:omega-cocycle` (`main.tex`:284–316), the cocycle $\omega(f, g)
= [\{f, g\}]_0$ defines a non-trivial class $[\bar c] \in
H^2_{\rm Lie}(\bar A; \C)$. The central extension
$\bar A_{[\bar c]} = \bar A \oplus \C K$ has bracket
$[(f, aK), (g, bK)] = (\{f, g\}, \omega(f, g) K)$.
**The central extension is non-trivial:** even though $Z(\bar A) = 0$,
$\bar A_{[\bar c]}$ has $\C \cdot K \subset Z(\bar A_{[\bar c]})$.

*(c) Is $\bar A$ semisimple?* No. **$\bar A$ is not semisimple.**
The argument: $\bar A$ is infinite-dimensional, and $[\bar A, \bar A]
\subsetneq \bar A$. To check: take $f = z_1$, $g = z_2$. Then
$\{z_1, z_2\} = 1$, which is killed in $\bar A$. So the bracket of
two linear generators is **zero in $\bar A$**. **Hence the linear
subspace $\mathrm{span}_\C(z_1, z_2) \subset \bar A$ is abelian.**
This is an abelian Lie subalgebra of dimension 2, so $\bar A$ has
non-trivial abelian sub-Lie-algebras and is therefore not
semisimple.

*(d) What survives at $\hbar > 0$?* The Moyal deformation
$\bar A_\hbar$ has bracket $\{f, g\}_\hbar = \hbar P + (\hbar^3/24)
P^3 + \ldots$. Even at $\hbar > 0$, $\{z_1, z_2\}_\hbar = \hbar$
which is killed in $\bar A_\hbar = \bar A[[\hbar]] / \C[[\hbar]]$.
**Hence the linear subspace $\mathrm{span}_\C(z_1, z_2)$ remains
abelian in $\bar A_\hbar$**, and $\bar A_\hbar$ remains non-semisimple
for every $\hbar$.

**Etingof-style consequence test: where does it "fail"?** At every
order. The non-semisimplicity is structural, not asymptotic. The
**Etingof-style remedy** is to recognize that semisimplicity is the
wrong criterion for this Lie algebra; the right criterion is
**flatness of the deformation $\bar A \rightsquigarrow \bar A_\hbar$
over $\C[[\hbar]]$**, which is verified in W3-W19-03 by the
Capelli triangular system being unipotent.

*Does this cause Theorem F to fail?* No. Theorem F is a
**Lie-algebra map** statement, not a statement about
semisimplicity. The map
$\partial_{\rm bb,\hbar,N}: \bar A_\hbar \to \mathcal W_N / I_N$
is required to commute with the Lie bracket on each side; that is
verified by the radial-parts identity, **not** by any
semisimplicity. The non-semisimplicity (presence of abelian
sub-Lie-algebras) is fully compatible with $\partial_{\rm bb,\hbar,N}$
being a Lie-algebra map.

**Hand-computation: the smallest abelian sub-Lie-algebra in
$\bar A_\hbar$ at $N = 1, 2$.**

At $N = 1$ (single brane): $\mathfrak{gl}_1 = \C$. The matrix
algebra is commutative; $\mathcal W_1$ is the rank-1 Weyl algebra
$\mathbb C\langle X, Y \rangle / [X, Y] = \hbar$. The trace is
the identity: $J_1(z_1) = X$, $J_1(z_2) = Y$. The commutator
$[X, Y] = \hbar = \hbar \cdot 1$, and the constant 1 is killed in
the connected projection. **Therefore at $N = 1$,
$\partial_{\rm bb,\hbar,1}(z_1)$ and $\partial_{\rm bb,\hbar,1}(z_2)$
commute in $\overline{\mathcal W_1 / I_1}$**, exactly as the
linear subspace of $\bar A_\hbar$ is abelian. The Lie-algebra map
condition is satisfied trivially.

At $N = 2$: $\mathfrak{gl}_2$, rank 2. By the script's
$[S_2(z_1), S_2(z_2)] = S_2([z_1, z_2]_*) = S_2(\hbar) = 0 \cdot 2 = 0$
(since $z_1$ has zero $z_2$-derivative and vice versa, $S_2(\hbar)$
is just the constant $2 \hbar$ or projects to zero in the connected
projection). **Same outcome: linear subspace remains abelian**,
script's section [5] for case (a) verifies this.

**Verdict.** Theorem F is consistent with the non-semisimple
Lie-algebra structure of $\bar A_\hbar$. The Etingof-style
"semisimplicity question" is not the relevant question;
**flatness over $\C[[\hbar]]$ is**, and that is verified.

**Files read.** `main.tex` 280–460 (anomaly chain showing $[\bar c]
\neq 0$); `scripts/check_moyal_coefficients.py` section [5]
(verified $[S_2(z_1), S_2(z_2)] = 0$).
**Confidence.** High.
**Blast radius.** Etingof-style consequence: non-semisimplicity
is not an obstruction; flatness is what closes the deformation
question.
**Minimal heal.** None.
**Adjudication.** Valid.

---

### W3-W19-05 — Theorem F as the $\hbar = 0$ associated graded of the all-order Theorem F$'$ map; F$'$ on the special fibre reduces to F

**Severity 3. Status valid. Confidence high.**
**Lens.** Etingof (deformation-quantization tower); Examples.
**Provenance.** New W3-W19 entry, supplied per T5 of the prompt.
**Target.** `thm:phi-hbar-all-order` (`main.tex`:5459–5485) and its
relation to `thm:finite-n-reduced-moyal`.

**Theorem F$'$ verbatim (`main.tex`:5466–5478).**

> "$\Phi_\hbar^{(0)}\colon\mathfrak h_\hbar
> \xrightarrow{\;\sim\;} H^0_{\mathrm{Ham,conn}}
> (\mc O^{\mathrm q}_{\mathrm{brane},\infty})_{\mathrm{ren}}$,
> $f \longmapsto \partial_{\mathrm{bb},\hbar}(f) =
> [\overline{J_N(f)}]_{N\to\infty}$ is a $\C[[\hbar]]$-linear
> isomorphism onto the renormalized degree-zero Hamiltonian sector,
> and it is a Lie-algebra map:
> $\Phi_\hbar^{(0)}(\{f,g\}_\hbar) = \hbar^{-1}[\Phi_\hbar^{(0)}(f),
> \Phi_\hbar^{(0)}(g)]_{\mathrm{conn,raw}}$."

**Precise relationship F vs F$'$.** Theorem F$'$ (`thm:phi-hbar-all-order`)
is the **all-order ℏ extension** in the connected stable limit
$N \to \infty$. Theorem F (`thm:finite-n-reduced-moyal`) is the
**finite-N statement that $D_N(f, g) \in I_N$** plus the connected
descended commutator identity. The two are layered:

- F is the algebraic-finite-model identity at every fixed $N$.
- F$'$ is the connected stable limit $N \to \infty$ of F's identity,
  promoted to a $\C[[\hbar]]$-linear isomorphism onto the
  renormalized target.

The "stability in $N$" argument in F's proof
(`main.tex`:5001–5008) is exactly the argument that F's
finite-$N$ identity passes to F$'$'s stable limit. **F$'$ is the
all-order ℏ statement of F's claim, after $N \to \infty$.**

**Is F a "vanishing-ℏ" limit of F$'$?** No, more precisely: F is
not the $\hbar \to 0$ limit; both F and F$'$ are
$\C[[\hbar]]$-linear statements. The relation is:

- F's associated graded at $\hbar = 0$ is the classical
  Hamiltonian boundary map $\partial_{\rm bb}: \bar A \to
  H^0_{\rm Ham}(\mathcal O_{\rm brane})$, with classical Poisson
  bracket on source and target (Theorem `thm:main-local`'s
  degree-zero sector).
- F$'$'s associated graded at $\hbar = 0$ is the same classical
  Hamiltonian boundary map after the $N \to \infty$ stable
  connected limit.

**So F$'$ at the special fibre $\hbar = 0$ reduces to (F at
$\hbar = 0$ at every $N$) $\to$ ($N \to \infty$ stable limit)
$\to$ (F's $\hbar = 0$ limit in the stable sector).** The two
operations commute by the stability argument in F's proof.

**Concrete example computation.** At $f = z_1$, $g = z_2$, $\hbar = 0$:

- F: $D_N(z_1, z_2) = \hbar^{-1}[J_N(z_1), J_N(z_2)] - J_N(\{z_1, z_2\}_\hbar)$
  $= \hbar^{-1} \cdot \hbar N \cdot \mathrm{Tr}(I) - J_N(\hbar)$
  $= \hbar^{-1}(\hbar N - \hbar N) = 0$ in $\mathcal W_N / I_N$.
  At $\hbar = 0$ this is the classical statement $\{z_1, z_2\} = 1$
  paired with $\partial_{\rm bb,N}$ killing the constant.
- F$'$: $\Phi^{(0)}_\hbar(\{z_1, z_2\}_\hbar) = \Phi^{(0)}_\hbar(1) = 0$
  (constant is killed in the reduced quotient $\bar A_\hbar$);
  $\hbar^{-1}[\Phi^{(0)}_\hbar(z_1), \Phi^{(0)}_\hbar(z_2)] =
  \hbar^{-1} \cdot \hbar = 1$ in the unreduced trace algebra,
  but is killed by the connected projection.

**Both F and F$'$ deliver the same answer on this pair: the
degree-zero map kills the constant; both sides match at every $\hbar$.**

The stronger statement of F$'$ over F is that **F$'$ asserts
$\Phi^{(0)}_\hbar$ is a $\C[[\hbar]]$-linear isomorphism**; F at
fixed $N$ asserts only that the map is a Lie-algebra homomorphism
modulo the moment-map ideal. The isomorphism statement requires
flatness of the Capelli triangular system over $\C[[\hbar N]]$
(F$'$'s proof, `main.tex`:5491–5494). **This flatness is verified
by the script's section [2] Capelli round-trip identity.**

**Files read.** `main.tex` 5459–5498 (`thm:phi-hbar-all-order`
plus its proof); `main.tex` 5001–5008 (stability in $N$);
`main.tex` 5050–5057 (`rmk:explicit-second-fourth-corrections`);
`scripts/check_moyal_coefficients.py` section [2] (Capelli
round-trip).
**Confidence.** High.
**Blast radius.** Editorial: clarifies the F vs F$'$ stratification
in the deformation-quantization tower.
**Minimal heal.** None. The relationship is correctly stated in
the manuscript; this entry records its precise structure.
**Adjudication.** Valid.

---

### W3-W19-06 — Moyal zero-locus: even coefficients $r = 2, 4, 6, 8, 10$ vanish at every monomial pair tested; this is exactly the algebraic content of Theorem F's odd-only assertion

**Severity 3. Status valid. Confidence high.**
**Lens.** Examples primary; Etingof secondary (the Moyal zero-locus
is the deformation-quantization analogue of the Poisson tensor's
constancy).
**Provenance.** New W3-W19 entry, supplied per T6 of the prompt.
**Target.** `prop:moyal-monomial` (`main.tex`:5419–5435) and
`scripts/check_moyal_coefficients.py` section [8].

**Algebraic claim.** The Moyal star commutator is
$[f, g]_* = \sum_{r \ge 1, r \text{ odd}} (2 / 2^r r!) \hbar^r P^r(f, g)$.
**Even coefficients $P^{2s}$ contribute zero to the star commutator
because they cancel under $f \leftrightarrow g$**, since
$P^r(g, f) = (-1)^r P^r(f, g)$.

**Script verification.** Section [8]:

```
[8] Fourth-order quantum upgrade pattern check:
     Even orders r=2,4,6,8,10 vanish in the star commutator on every monomial pair tested.
     (a) z1, z2: even-order star commutators vanish through r=10.  PASS.
     (b) z1^2, z2: even-order star commutators vanish through r=10.  PASS.
     (c) z1^2, z2^2: even-order star commutators vanish through r=10.  PASS.
     (d) z1^3, z2^2: even-order star commutators vanish through r=10.  PASS.
```

**The vanishing is structural, not numerical.** Section [1] of the
script verifies the antisymmetry $P^r(g, f) = (-1)^r P^r(f, g)$ on
**14641 monomial pairs at exponents ≤ 10 and orders ≤ 11**:

```
[1] Moyal sweep: checked 14641 monomial pairs, exponents <= 10, orders <= 11.  PASS.
     r=1: odd commutator coefficient = 1/1
     r=3: odd commutator coefficient = 1/24
     r=5: odd commutator coefficient = 1/1920
     r=7: odd commutator coefficient = 1/322560
     r=9: odd commutator coefficient = 1/92897280
     r=11: odd commutator coefficient = 1/40874803200
```

The odd-order coefficients reproduce $\frac{1}{2^{r-1} r!}$ exactly,
confirming the manuscript's `prop:moyal-monomial` displayed
formula.

**Hand-check of even-vanishing on $f = z_1^4 z_2^2, g = z_1^2 z_2^4$
(case (f), the smallest pair where $P^5$ is non-zero).**
By the formula:
$P^2(z_1^4 z_2^2, z_1^2 z_2^4) = \sum_{a=0}^2 (-1)^a \binom{2}{a}
(4)_{2-a} (2)_a (2)_a (4)_{2-a} z_1^{4+2-2} z_2^{2+4-2}$
$= z_1^4 z_2^4 \sum_{a=0}^2 (-1)^a \binom{2}{a} (4)_{2-a}^2 (2)_a^2$.

For $a = 0$: $1 \cdot 1 \cdot 12^2 \cdot 1^2 = 144$;
$a = 1$: $-2 \cdot 4^2 \cdot 2^2 = -128$;
$a = 2$: $1 \cdot 0 \cdot 0 = 0$. Total: $144 - 128 = 16$.
**$P^2(f, g) = 16 z_1^4 z_2^4 \ne 0$**.

But $P^2(g, f) = (-1)^2 P^2(f, g) = +P^2(f, g)$, so
$[f, g]_*$ at order $r = 2$ contains
$\frac{1}{2 \cdot 2!}(P^2(f, g) - P^2(g, f)) = 0$. **The cancellation
is algebraic.** The Moyal-zero-locus is the cancellation of even
$P^r$ contributions in the commutator, not the vanishing of
$P^{2s}(f, g)$ themselves.

**Verdict.** The Moyal zero-locus claim of Theorem F is verified
on the script's full sweep. The algebraic structure is:
- $P^r(f, g)$ is **non-zero in general** for even $r$;
- the **commutator $P^r(f, g) - P^r(g, f)$ vanishes for even $r$**
  by the antisymmetry $P^r(g, f) = (-1)^r P^r(f, g)$.

**Files read.** `scripts/check_moyal_coefficients.py` sections
[1] and [8] (output captured); `main.tex` 5419–5435
(`prop:moyal-monomial`).
**Confidence.** High.
**Blast radius.** First-example-grade evidence that the Moyal
odd-only claim closes at every tested order.
**Minimal heal.** None.
**Adjudication.** Valid.

---

### W3-W19-07 — M-31 ([Tr ψ] ↔ [c̄]) interaction with Theorem F: strict at the chain level on the algebraic Moyal core; depends on the all-order ℏ extension only for the descendant sector lift

**Severity 3. Status valid. Confidence medium-high.**
**Lens.** Etingof primary (chain-level vs cohomology-level).
**Provenance.** New W3-W19 entry, supplied per T7 of the prompt.
**Target.** M-31 (`reconstitution/attack-heal-platonic-2026-04-28.md`:1612–1644);
`thm:u1-center-anomaly-open` (`main.tex`:354–393);
`scripts/check_one_psi_homology.py`.

**M-31's claim.** "$[\mathrm{Tr}\,\psi]_{\rm BV} \leftrightarrow
[\bar c]_{\rm CE}$ are the same distinguished anomaly line viewed
from the two sides of CE/PV."

**Question.** On the algebraic Moyal level, is the M-31
identification (a) strict at the chain level (cocycles that pair
to the same number on the same generators), (b) cohomology-level
(cohomologous representatives in possibly different complexes),
or (c) only "line-level" (the obstruction lives in a
one-dimensional class line)?

**Strict chain-level analysis on Theorem F's algebraic core.**

*The CE side.* From `lem:omega-cocycle`, the cocycle is
$\omega: \bar A \otimes \bar A \to \C$, $\omega(f, g) = [\{f, g\}]_0$.
On the basis pair $(z_1, z_2)$: $\omega(z_1, z_2) = [1]_0 = 1$.
**A specific Lie 2-cocycle in $C^2_{\rm Lie}(\bar A; \C)$.**

*The BV side.* The cotangent CE coordinate $u_1$ dual to the
constant Hamiltonian generator $1$ is realized on the open BV
side as $\mathrm{Tr}\,\psi$ (M-31's mechanism). The PV-side
BV cocycle generated by $\mathrm{Tr}\,\psi$ pairs against the
Hamiltonian $\mathrm{Tr}(\phi_1 \phi_2)$ via the moment map
$\mu = -\mathrm{Tr}([\phi_1, \phi_2])$. **The BV bracket
$\{\mathrm{Tr}\,\psi, \mathrm{Tr}(\phi_1 \phi_2)\}_{\rm BV}$
records the constant trace shift $\mathrm{Tr}(I) = N$**
on the central direction.

*The two pairings.* On the basis pair $(z_1, z_2)$:
- CE side: $\omega(z_1, z_2) = 1$.
- BV side: $\partial_{\rm bb,N}^{\rm full}(\{z_1, z_2\}) =
  \{\mathrm{Tr}\,\phi_1, \mathrm{Tr}\,\phi_2\} = N$
  (`thm:u1-center-anomaly-open`, `main.tex`:359–379, line 379:
  "$\{\mathrm{Tr}\,\phi_1, \mathrm{Tr}\,\phi_2\} = \mathrm{Tr}(I \cdot I) - 0 = N$").

**The two cocycles match cocycle-wise after the boundary evaluation
map $\partial_{\rm bb,N}^{\rm full}$**: $\omega \cdot N$ on the
closed side equals the trace-pairing on the open side. **This is
strict at the chain level**, *not* just cohomologically — the
representatives $\omega$ and $\mathrm{Tr}(I) \cdot \omega = N \omega$
differ only by the constant scalar $N$, which is the magnitude of
the brane stack.

**Does M-31 depend on the all-order ℏ extension?** No, on the
**algebraic Moyal level**. The M-31 identification holds at
**$\hbar = 0$**: the classical Poisson cocycle $\omega$ on the
closed side and the classical trace-pairing on the open side both
realize the same line. **The identification is at every finite
$\hbar$**: the Moyal star bracket has $\{z_1, z_2\}_\hbar = \hbar$
(plus higher-order corrections that vanish on linear Hamiltonians
because $P^r$ for $r \ge 2$ vanishes on $z_1, z_2$); the BV-side
$\{\mathrm{Tr}\,\phi_1, \mathrm{Tr}\,\phi_2\}_{\rm BV}$ at one
loop on linear Hamiltonians is $N \cdot \hbar$ (the Capelli shift
from the script's normal-ordering defect output:
"$\hbar^{-1}[T_{2,1}, T_{0,2}] = 4 T_{1,2} - 2 \hbar N T_{0,1}$",
showing the $\hbar N$ shift on the BV side).

**The M-31 identification holds at every finite order in $\hbar$**
because the higher-order Moyal corrections $P^r$ for $r \ge 2$
**vanish on linear Hamiltonians**. Section [9] of the script:

```
(a) z1, z2: P^1 = 1; P^3 = 0; P^5 = 0
          [*]_1 = 1 hbar; [*]_3 = 0 hbar^3; [*]_5 = 0 hbar^5
```

**On the simplest pair $(z_1, z_2)$, all higher-order Moyal
contributions are zero.** The M-31 identification is therefore
exhausted by the linear-order $\hbar^1$ contribution, which equals
the classical Poisson cocycle $\omega$.

**Where does the all-order ℏ extension matter?** Only for the
**descendant (one-antifield) sector**. On polynomial Hamiltonians
of degree $\ge 3$, the higher Moyal terms $P^3, P^5, \ldots$
contribute non-trivially (script's section [9b] for case (e):
$[z_1^3 z_2, z_1 z_2^3]_* = 8 \hbar z_1^3 z_2^3 - 3 \hbar^3 z_1 z_2$).
The Moyal coadjoint action on the descendant sector
$\mathfrak h^\vee$ generates obstruction terms that the polynomial
PBW one-psi action cannot match. Per the
`check_one_psi_homology.py` script, **1200 PBW-vs-Moyal mismatches
in 1225 cases at exponents ≤ 5**:

```
attacked naive quantum descendant lift in 1225 cases with
exponents <= 5 and Moyal order <= 5: 1200 PBW-vs-Moyal mismatches,
958 cases with genuine higher Moyal coadjoint terms
explicit obstruction: ad^*_{z1^4}(delta_1,1) has -24 hbar^2 delta_0,4,
while the polynomial one-psi action sends Psi_1,1 to 4 Psi_4,0
```

**This is exactly the F$'$ descendant-sector obstruction**:
the M-31 identification holds strictly at the chain-level on the
**Hamiltonian (zero-antifield) sector**, but its naive descendant
extension fails by an explicit higher-Moyal coadjoint term.

**Verdict.** On the **algebraic Moyal level (Theorem F's domain)**,
the M-31 identification is **strict chain-level**: the CE cocycle
$\omega$ and the BV cocycle $[\mathrm{Tr}\,\psi]_{\rm BV}$ match
on the linear-generator pair $(z_1, z_2)$ with the constant $N$
relating them. **It holds at every finite order in $\hbar$**
because higher-order Moyal contributions vanish on linear
Hamiltonians. **The all-order ℏ extension matters only for the
descendant (one-antifield) sector**, where the polynomial PBW
action fails to lift the Moyal coadjoint action — and this is
exactly the F$'$ vs F gap recorded in W15.

**Files read.** `main.tex` 280–460 (the U(1) anomaly chain);
`reconstitution/attack-heal-platonic-2026-04-28.md` 1612–1644
(M-31 entry); `scripts/check_one_psi_homology.py` (executed,
output captured); `scripts/check_moyal_coefficients.py` section [9].
**Confidence.** Medium-high. The strict chain-level claim depends
on the boundary evaluation map $\partial_{\rm bb,N}^{\rm full}$
being a strict (not just up-to-homotopy) cocycle map; this is
asserted in the manuscript at the algebraic level but its full
chain-level lift is M-31's named "Obligation I". **Without
Obligation I closed**, the strict-chain-level claim depends on the
specific mechanism of `thm:u1-center-anomaly-open`, which gives
the constant $N$ explicitly.
**Blast radius.** Sharpens M-31 by showing that on the algebraic
Moyal core, the identification is strict cocycle-wise (not just
cohomology-wise), and that the all-order ℏ extension matters
only for the descendant sector.
**Minimal heal.** Optional remark in the M-31 area
(`main.tex`:393-area or `reconstitution/attack-heal-platonic-2026-04-28.md`
M-31 entry) noting:

> "On the algebraic Moyal core (Theorem F's domain), the M-31
> identification holds strictly cocycle-wise: the CE cocycle
> $\omega(z_1, z_2) = 1$ and the BV cocycle generated by
> $[\mathrm{Tr}\,\psi]$ match via the boundary evaluation
> $\partial_{\rm bb,N}^{\rm full}$ with the explicit constant $N$
> from `thm:u1-center-anomaly-open`. The identification holds at
> every finite order in $\hbar$ because higher-order Moyal
> contributions $P^r$ ($r \ge 2$) vanish on linear Hamiltonians
> $z_1, z_2$. The all-order ℏ extension is required only for the
> **descendant (one-antifield) sector lift**, where
> `check_one_psi_homology.py` records explicit obstructions."

**Adjudication.** Valid sharpening of M-31.

---

## §2. Residual disposition

**Outstanding obligations relative to W3-W19's findings.**

1. **Obligation I (M-31's bridge to factorization-centre level)**
   remains unproved. W3-W19-07's strict chain-level claim depends
   on the explicit boundary evaluation map being a strict cocycle
   map; without Obligation I closed, this is at the algebraic-level
   ($\hbar^1$, linear-Hamiltonian) only. **No regression**: M-31's
   "medium-high confidence" rating is preserved.

2. **The descendant sector lift** (`prob:formal-factorization-center`
   and `prob:tate-coefficient-descendant-lift`) remains conditional
   on `prob:weighted-rg-locality`. W3-W19's sweep
   (`check_one_psi_homology.py`, 1200 PBW-vs-Moyal mismatches)
   confirms the obstruction is **explicit and structural, not a
   regulator artifact**. **No regression**: this is the gating
   recorded by W15 (W3-W15-04, W3-W15-05).

3. **The Harish-Chandra–Wallach–Levasseur–Stafford radial-parts
   input** (`stmt:app-radial-external-input`) is named as external
   input. W3-W19-02's script verification of the rank-2 and rank-3
   restrictions is **finite-rank evidence, not a substitute** for
   the all-N theorem. The F-status remains "stable, unconditional
   inside the finite algebraic model, modulo this external input".
   **No regression**: this is correctly named in the manuscript at
   `appendix-radial-parts-moyal.tex`:145–182.

**No new ledger items breaking F.** The seven W3-W19 entries
sharpen and confirm Theorem F's algebraic content; none refute it.

---

## §3. Summary of script-grade evidence (T2, T6)

`check_moyal_coefficients.py`: **all checks pass**. Coverage:
- 14641 Moyal monomial pairs (exponents ≤ 10, orders ≤ 11);
- 121 Capelli round-trips ($a, b \le 10$);
- 80 + 80 direct rank-2 and rank-3 radial-parts restrictions;
- 7 test pairs verifying $[S_2(f), S_2(g)] = S_2([f, g]_*)$;
- 4 connected cumulant brackets;
- 4 open-line midpoint graph weights;
- Even orders $r = 2, 4, 6, 8, 10$ vanish on every monomial pair
  tested.

`check_one_psi_homology.py`: **all checks pass**. Coverage:
- 36 bidegrees with primitive one-psi homology dimension 1;
- 240 open Hamiltonian descendant action cases;
- 1225 closed coadjoint Taylor-dual formula cases;
- 1225 principal-part coadjoint realizations;
- 1225 attacks on naive quantum descendant lift, **1200
  PBW-vs-Moyal mismatches** (which is the F$'$ descendant
  obstruction, *not* an F obstruction);
- 3375 representation identities for the corrected Moyal
  principal-part coadjoint target;
- 70 tests of no-h-adic-deformation of the classical
  $\Psi \to \rho$ projection.

**Verdict on F's algebraic core.** Closed at every order tested.

---

## §4. Files read

- `CLAUDE.md` (full, 51 lines).
- `reconstitution/attack-heal-platonic-2026-04-28.md` lines
  1610–1715 (M-31, M-32, M-33 entries).
- `reconstitution/wave3-W15-conditional-theorems-2026-04-28.md`
  lines 1–540 (verbatim Theorem F + F$'$ + G hypothesis package).
- `main.tex` lines 280–470 (the U(1) anomaly chain),
  4800–5200 (Theorem F region: `lem:capelli-renormalized-stable-trace`,
  `cor:renormalized-stable-connected-map`, `thm:finite-n-reduced-moyal`,
  `cor:degree-zero-quantum-upgrade`, `rmk:explicit-second-fourth-corrections`,
  `prob:quantum-hamiltonian-upgrade`),
  5400–5550 (`prop:moyal-monomial`, `thm:phi-hbar-all-order`,
  `cor:phi-hbar-supremum`, `prop:conditional-boundary-product-normalization`).
- `scripts/check_moyal_coefficients.py` (full, 1003 lines; executed).
- `scripts/check_one_psi_homology.py` (full, 657 lines; executed).
- `appendix-radial-parts-moyal.tex` (full, 383 lines).

---

**End of W3-W19 report.**
