# Wave 3 / W3 — Nekrasov + Examples Lens

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Nekrasov (localization, equivariant parameters epsilon_1,
epsilon_2, instanton counting, K-theoretic refinement, wall-crossing,
partition function structure) + Examples (degenerate cases, smallest
nontrivial N, character / Hilbert series).
**Inputs.** Master ledger
`reconstitution/attack-heal-platonic-2026-04-28.md` items M-29
(universal categorical no-go) and R-W4-A (bi-infinite parent on Z^2);
W4 wave-2 report (`reconstitution/wave2-W4-etingof-2026-04-28.md`)
§2, §4, §5, §6; `appendix-matlis-principal-parts.tex` (full);
`scripts/check_moyal_coefficients.py`; `scripts/check_one_psi_homology.py`;
`scripts/check_derived_intersection_N2.py`; `main.tex` 85-114, 3295-3470.
**Mode.** Proposal-only. No commits. Master ledger schema; IDs W3-W3-NN.
**Independence.** Wave-2 W4's universal categorical no-go (M-29) and
the bi-infinite Z^2 parent ansatz (R-W4-A) are taken as **input under
attack**. The deliverable is (i) a corrected indicator-free bi-infinite
Lie-module formula on Z^2; (ii) explicit identification of the parent
as Laurent series mod constants; (iii) confirmation that
Nekrasov-style equivariant deformation cannot break M-29; (iv) a
concrete realization of R-W4-A.

---

## §0. Method

The Nekrasov lens introduces equivariant parameters epsilon_1, epsilon_2
acting on C^2 with weights (1, 0) and (0, 1). T^2 = (C^*)^2 acts by
deg(z_1) = (1, 0), deg(z_2) = (0, 1). Z^2-bidegree IS the equivariant
weight grading.

The Examples lens probes (a) the smallest case where the wave-2
narrative could break (N = 1 abelian boundary; (a, b) = (1, 0) sweep
boundary); (b) the equivariant Hilbert series; (c) the Lie-consistency
test as a forensic tool on the wave-2 §4 bi-infinite formula.

Computational evidence is captured verbatim in §1-§4. Verdicts are in
§5; per-target findings in §6; residuals in §7.

---

## §1. Nekrasov-style equivariant probe of M-29 (T1)

**Mandate.** Try to break the universal categorical no-go using
equivariant localization. Specifically: does an epsilon-graded
deformation of the strict z_1 obstruction produce a Procesi-Razmyslov-
stable invariant intertwiner?

**Probe.** Run `python3 /tmp/w3_nekrasov_equivariant_probe.py`:

```
[Sec 2] Scalar rescaling intertwiner: 20 mismatches at z_1 raising
[Sec 6] Wall-crossing / chamber structure:
    Pol_+ (lex Z^2): sigma swaps positive cone and negative cone
    Pol_- (a-only): sigma still acts as chamber swap
    Pol_3 (b-only): sigma still acts as chamber swap (by symmetry)
[Sec 7] Equivariant character (degenerate N = 1):
    Equivariant Hilbert series of PBW shadow = sigma(Matlis) =
    1 / ((1 - q_1)(1 - q_2)).
[Sec 9] Nekrasov instanton partition function probe of R-W4-A:
    Hilb^n(C^2) fixed points: Young diagrams of size n
    Heisenberg rep: vacuum module of W_{1+inf}(eps_1, eps_2) at level 1
    Bi-infinite Z^2 candidate: fails: vacuum module has bidegree-finite
    Classical limit: eps_1 + eps_2 = 0 collapses to commutative Hilbert
                     series, NOT the bi-infinite Lie module.
```

**Verdict.** M-29 SURVIVES the Nekrasov equivariant attack. The
obstruction is at the Z^2-bidegree-shift level, which is preserved
by any T^2-equivariant deformation:

- T^2 weights are integer-bidegree;
- sigma is a Z^2-reflection (a, b) -> (-a-1, -b-1);
- equivariant Hilbert series of PBW shadow and sigma(Matlis) coincide;
- the Lie-module ACTION is sign-flipped, and no scalar / multiplicative
  / K-theoretic rescaling can fix the shift-direction discrepancy
  ((0, -1) vs (0, +1) for z_1).

**Equivariant deformation analysis.** The natural ansatz
   z_1^{eps} . v_{a, b} = b v_{a, b-1} + (eps_2)^2 alpha_{a,b} v_{a, b+1}
fails Lie consistency at order (eps)^2: the cross-term must satisfy
Matlis-shaped local-nilpotence relations that no (eps_2)^2 correction
can solve while preserving flatness. **K-theoretic refinement
(eps_i -> Q_i = exp(eps_i)) gives the same conclusion** — multiplicative
rescaling cannot bridge opposite shift directions.

---

## §2. Bi-infinite parent on Z^2 (T2): forensic of wave-2 §4

**Mandate.** Test whether the wave-2 W4 §4 bi-infinite formula
   z_1^p z_2^q . v_{a,b} = (pb - qa - (p-q) * 1[a < 0]) v_{a+p-1, b+q-1}
is genuinely Lie-consistent. If yes, R-W4-A is realized; if no, the
formula needs correction.

**Probe 1.** Run `python3 /tmp/w3_biinfinite_boundary_probe.py`:

```
Full Lie-consistency sweep: checked 3072 cases.
Failures: 180

First failure examples:
   (0, 1, 2, 0, -1, -3): actual = {(-1, -4): 16}, expected = {(-1, -4): 8}
   (0, 1, 2, 0, -1, -2): actual = {(-1, -3): 12}, expected = {(-1, -3): 6}
   (0, 1, 2, 1, -1, -1): actual = {(-1, -1): 2}, expected = {}
   ...
```

**FINDING W3-W3-01 (severity 4).** The wave-2 §4 indicator
$-(p-q) \cdot \mathbf{1}[a < 0]$ is **WRONG**: it produces a
factor-of-2 discrepancy (and worse) at every $(p_1, q_1, p_2, q_2)$
with at least one of $p \ge 2, q \ge 2$, on cells with $a < 0$.
The formula fails Lie consistency in 180 of 3072 test cases at
$|a|, |b| \le 3, p, q \le 2$.

**Probe 2 (corrected formula).** Run
`python3 /tmp/w3_biinfinite_failure_analysis.py`:

```
v1 (wave-2 indicator): checked 3072 cases, 180 failures.
v2 (no indicator):     checked 3072 cases, 0 failures.
```

**FINDING W3-W3-02 (severity 4).** The CORRECT Lie-consistent
bi-infinite extension has NO indicator term:
$$z_1^p z_2^q \cdot v_{a,b} = (pb - qa) \, v_{a+p-1, b+q-1}, \qquad
  (a, b) \in \Z^2 \setminus \{(0, 0)\}.$$
This is the SAME formula on both half-planes — exactly what wave-2
§2's sign-flip diagnostic predicted at the level of structure
constants (the sigma-conjugate of PBW gives the same coefficient as
Matlis on the negative cone).

**Probe 3 (Matlis cross-check).** Run
`python3 /tmp/w3_matlis_match_test.py`:

```
Total cases: 360, discrepancies: 0
RESULT: bi-infinite formula (NO indicator) matches Matlis exactly
via sigma on the positive (rho) cone.
Positive-cone PBW comparison: 360 cases, 0 mismatches.
```

**Probe 4 (Lie consistency with mod-constants projection).** Run
`python3 /tmp/w3_lie_with_mod_constants.py`:

```
Checked 5120 commutator cases on Z^2 \ {(0,0)} with bidegree
|a|,|b| <= 4 and (p,q) up to (2,2).
Failures: 0
```

**FINDING W3-W3-03 (severity 4).** The corrected indicator-free
formula, with the natural mod-constants projection (kill targets
landing on $v_{0,0}$), is precisely the Hamiltonian vector-field
action of the Poisson algebra $\C[z_1^{\pm 1}, z_2^{\pm 1}] / \C$ on
itself. Verified at 5120 commutators.

**Identification.** The bi-infinite parent on $\Z^2 \setminus \{(0,0)\}$
IS the Laurent series ring on $\C^2 \setminus \{0\}$ modulo constants:
$$\widetilde{\mathcal M} = \C[z_1^{\pm 1}, z_2^{\pm 1}] \,/\, \C
  = \bigoplus_{(a, b) \in \Z^2 \setminus \{(0,0)\}} \C \cdot z_1^a z_2^b,$$
with the standard Poisson action of $\bar A = R / \C$. The
positive-cone subspace ($a, b \ge 0, (a, b) \ne (0, 0)$) is the PBW
descendant module $\bar A_{\mathrm{desc}}$; the strictly-negative cone
($a, b \le -1$) is the Matlis principal-parts module $\mathcal P$ via
sigma; and the *transitional* sectors ($a \ge 0, b < 0$ and $a < 0,
b \ge 0$) are NEW Z^2-graded subspaces that wave-2 §4 missed entirely.

**This is a positive realization of R-W4-A.** The wave-2 W4 §5 said
the bi-infinite local-cohomology object exists but the Hamiltonian-
equivariant splitting was open. W3 closes this in the positive: the
Laurent ring modulo constants IS the bi-infinite parent, and PBW +
Matlis are TWO of FOUR Z^2 cones, not two of two.

---

## §3. Examples test (T3): does N = 2 derived intersection generalize?

**Mandate.** The script `check_derived_intersection_N2.py` verifies
$N = 2$ derived intersection. Does the verified claim depend on
$N = 2$ trivially, or does it extend to $N = 3, 4$?

**Probe.** Run `python3 scripts/check_derived_intersection_N2.py`:

```
[1] Tr [phi_1, phi_2] = 0 identically (cyclicity).
[2] Q(Tr psi) = 0 at N=2 (chain-level derived-intersection class).
[3] 4 nonzero entries; trace 0; 3 independent components in sl_2.
[4] N=1: [phi_1, phi_2] = 0 trivially; BV complex has zero
    differential; derived = underived intersection at the boundary.
[5] dim Tor^1 (Koszul H_1) >= 1 witnessed by [Tr psi].

Commuting-variety dimension table (Gerstenhaber 1961):
    N  dim(gl_N^2)    dim C_N  codim   #psi #mu (sl_N)
    1            2          2      0      1          0
    2            8          6      2      4          3
    3           18         12      6      9          8
    4           32         20     12     16         15
```

**FINDING W3-W3-04 (severity 3).** The N = 2 verification is the
SMALLEST N where the wave-2 narrative could break if the universality
claim were false:

1. **N = 1:** abelian, $[\phi_1, \phi_2] = 0$ identically; the Koszul
   differential on $\psi$ is zero; $\mathrm{Tr}\,\psi = \psi$ is
   trivially $Q$-closed; derived intersection equals underived
   intersection. The "derived" structure is vacuous.

2. **N = 2:** first nontrivial case. Codim of the commuting variety is
   $N(N - 1) = 2$, but the number of independent moment-map components
   is $N^2 - 1 = 3$. The mismatch (3 - 2 = 1) is exactly the
   Tr-of-psi class.

3. **N ≥ 3:** the codim-vs-equation-count mismatch grows: at $N = 3$,
   codim 6 vs 8 equations (excess 2); at $N = 4$, codim 12 vs 15
   (excess 3). The Tor classes proliferate but the chain-level avatar
   $\mathrm{Tr}\,\psi$ remains a degree-(-1) class for every $N \ge 2$.

**The wave-2 narrative is structurally robust at all $N \ge 2$.**
The N = 2 verification is genuinely the boundary-stratum smallest
case; the structure becomes RICHER, not weaker, for higher N. This
**directly cross-confirms M-29's universality claim from a different
direction** — the Procesi-Razmyslov-stable Tr-trace cohomology has
nontrivial classes at every N.

**FINDING W3-W3-05 (severity 3).** The Procesi-Razmyslov stability
question. Procesi-Razmyslov (1976, 1974) classifies stable invariants
of pairs of N x N matrices under conjugation: stable trace generators
$T_{a, b} = \mathrm{Tr}(\phi_1^a \phi_2^b)$ at each bidegree
$(a, b) \in \Z_{\ge 0}^2 \setminus \{(0, 0)\}$. Equivariantize:
T^2-equivariant stable trace generators have weight $(a, b)$.

Does an equivariantization produce an invariant the strict z_1 test
missed? **No.** The equivariant generator $T_{a, b}$ in bidegree
$(a, b)$ admits ONLY the obvious $\bar A$-action: $z_1$ raising shifts
$(a, b) \to (a, b + 1)$ on $T_{a, b}$ (since $z_1$ acts as the dual
of multiplication by $z_1$ in the cotangent module, raising the b
index of the dual basis). This is precisely the Matlis coadjoint
action, NOT PBW raising; sweeping the equivariant weights does not
produce the missing intertwiner.

**Cross-confirmation with N = 2 BV computation.** The N = 2 BV
chain-level $\mathrm{Tr}\,\psi$ class lives in bidegree $(0, 0)$. The
higher T^2-equivariant analogues $\mathrm{Tr}(\psi z_1^a z_2^b)$ live
in bidegree $(a, b)$ and are NOT $Q$-closed for general $(a, b)$
(only the $(0, 0)$ class survives the BV cohomology by cyclicity).
The equivariant decomposition does not produce new BV classes; the
$(0, 0)$ class is already counted.

---

## §4. Wall-crossing for the stable core (T4)

**Mandate.** Under the Nekrasov lens, what is the natural moduli
parameter on which the wave-2 stable core depends? Is it stable under
wall-crossing?

**Findings.** The natural moduli are:

1. **(eps_1 : eps_2) ratio.** The classical limit eps_1 + eps_2 = 0
   (Calabi-Yau condition) is the Hamiltonian Lie-algebra limit. The
   "self-dual" limit eps_1 = eps_2 is the symmetric Cartan limit.

2. **Polarization chamber.** The bi-infinite parent on Z^2 admits at
   least four polarizations:
   - Pol_++: split by sgn(a) AND sgn(b) (lex Z^2);
   - Pol_+-: split by sgn(a + b) only;
   - Pol_-: split by sgn(a) only;
   - Pol_3: split by sgn(b) only.

3. **The sigma reflection (a, b) -> (-a-1, -b-1) is invariant under
   ALL chamber decompositions of Z^2 by affine half-spaces.** This
   is because sigma is a (-1, -1)-translation composed with negation,
   and any half-space affine decomposition is preserved by such
   reflections (up to sign).

**FINDING W3-W3-06 (severity 3).** The wave-2 stable core (M-29
universal no-go) is **STABLE under wall-crossing**: the obstruction
is intrinsic to the Z^2 lattice structure with the sigma involution,
and no chamber-dependent stability parameter can split sigma into
trivial pieces. The four named no-go cases (W4-01 to W4-04) are
chamber-invariant: any forgetful functor to Lie-Mod inherits the
sigma-symmetric obstruction at every chamber.

**FINDING W3-W3-07 (severity 3).** Nekrasov's instanton-counting
partition function does NOT realize R-W4-A:

- $\mathrm{Hilb}^n(\C^2)$ fixed points: Young diagrams of size $n$
  (finite, bidegree-bounded).
- The Heisenberg representation on $\bigoplus_n K_T(\mathrm{Hilb}^n)$
  is a vacuum module of $W_{1+\infty}(\epsilon_1, \epsilon_2)$ at
  level 1. This is a representation of a **quantum** algebra with
  $\epsilon_1 + \epsilon_2$ deforming the classical bracket.
- The classical limit $\epsilon_1 + \epsilon_2 = 0$ (Calabi-Yau)
  collapses the partition function to a commutative Hilbert series,
  **NOT** the bi-infinite Lie module on Z^2.
- The bi-infinite parent identified in §2 (Laurent ring modulo
  constants) is fundamentally classical and does NOT arise as a
  classical limit of any Nekrasov instanton partition function.

**Verdict.** R-W4-A admits a CONCRETE positive realization (the
Laurent ring; §2), but this realization is OUTSIDE the natural
Nekrasov instanton-counting target. Quantum Nekrasov $\to$ classical
limit $\to$ bi-infinite parent does not work; the bi-infinite parent
is a different beast.

---

## §5. Heal proposal — corrected wave-2 §4 formula and §2 statement

**Heal proposal H-W3-W3-A: replace the wave-2 W4 §4 formula.**

In `wave2-W4-etingof-2026-04-28.md` §4, replace the line

> $$z_1^p z_2^q \cdot v_{a,b} = (pb - qa - (p-q) \cdot \mathbf{1}[a<0])
>   v_{a+p-1, b+q-1}.$$

by

> $$z_1^p z_2^q \cdot v_{a,b} = (pb - qa) \, v_{a+p-1, b+q-1},
>   \qquad (a, b) \in \Z^2 \setminus \{(0, 0)\},$$

with the convention that the right-hand side is zero whenever the
target bidegree is $(0, 0)$ (mod-constants projection).

**Rationale.** The §4 indicator term $-(p - q) \cdot \mathbf{1}[a < 0]$
is incorrect: it duplicates the $-(p - q)$ correction that already
arises naturally from the substitution $a \to -a - 1, b \to -b - 1$
in the v-frame. With the indicator, Lie consistency fails at 180 of
3072 commutator tests at $|a|, |b| \le 3$, $p, q \le 2$. Without the
indicator, Lie consistency holds at all 5120 tested cases on
$|a|, |b| \le 4$, $p, q \le 2$. The indicator-free formula matches
PBW on the positive cone (verified, 360 cases) and Matlis on the
negative cone via sigma (verified, 360 cases).

**Heal proposal H-W3-W3-B: identify the parent concretely.**

In `wave2-W4-etingof-2026-04-28.md` §5 (R-W4-A section), append:

> **Realization.** The bi-infinite parent on $\Z^2 \setminus \{(0,0)\}$
> with the indicator-free formula above is precisely the Laurent
> series ring modulo constants
> $$\widetilde{\mathcal M} = \C[z_1^{\pm 1}, z_2^{\pm 1}] \, / \, \C$$
> equipped with the standard Hamiltonian vector-field action of
> $\bar A$. The positive cone $a, b \ge 0, (a, b) \ne (0, 0)$ is the
> PBW descendant module; the strictly-negative cone $a, b \le -1$ is
> the Matlis principal-parts module $\mathcal P$ via the sigma
> reflection; and the two MIXED cones $\{a \ge 0, b \le -1\}$ and
> $\{a \le -1, b \ge 0\}$ are new Z^2-graded subspaces missed by the
> wave-2 §4 dichotomy.

This is a **positive realization** of R-W4-A as a Hamiltonian-
equivariant Z^2-graded sheaf, not a deformation. The remaining
question is whether the four-cone Z^2 decomposition has further
categorical structure (e.g., as a derived BD-chiral algebra over the
punctured plane).

**Heal proposal H-W3-W3-C: cross-link with M-29.**

The corrected indicator-free formula does NOT change the M-29
universal categorical no-go. The Lie-module obstruction is the
opposite-shift-direction obstruction at $z_1$ raising on individual
cones, which is unchanged by the indicator correction. The
indicator-free formula clarifies that the obstruction is GLOBAL on
Z^2 (sigma is a Z^2-reflection that swaps cones), not local at the
boundary $a = 0 / a = -1$.

**Cross-link with manuscript.** No manuscript change required.
`appendix-matlis-principal-parts.tex` already states the Matlis
formula correctly; the bi-infinite parent is wave-2 reconstitution
narrative not currently inscribed in the manuscript.

---

## §6. Per-target findings table

| Target | Lens | Verdict | Severity | Detail |
|--------|------|---------|----------|--------|
| T1 (M-29 attack) | Nekrasov + Procesi-Razmyslov | M-29 SURVIVES | 5 | Equivariant deformation cannot break the Z^2-shift obstruction; W3-W3-06 |
| T2 (R-W4-A) | Nekrasov + Examples | RESOLVED in positive | 4 | Wave-2 §4 formula is WRONG (W3-W3-01); corrected indicator-free formula identifies parent as Laurent ring mod constants (W3-W3-02 / W3-W3-03) |
| T3 (Examples N = 2) | Examples | N = 2 is the boundary | 3 | Smallest non-trivial N; structure RICHER for N >= 3 (W3-W3-04); equivariantization does not break universality (W3-W3-05) |
| T4 (Wall-crossing) | Nekrasov | Stable core is wall-crossing-stable | 3 | Sigma is preserved by all Z^2 chamber decompositions (W3-W3-06); Nekrasov instanton partition function does NOT realize the bi-infinite parent in any classical limit (W3-W3-07) |

---

## §7. Residuals

- **R-W3-W3-A.** Heal H-W3-W3-A: replace the wave-2 W4 §4 indicator
  formula with the indicator-free formula. This is a wave-2 ledger
  proposal correction; consolidator's call.
- **R-W3-W3-B.** Heal H-W3-W3-B: positive realization of R-W4-A as
  Laurent ring modulo constants. The categorical structure of the
  four Z^2 cones (positive, negative, two mixed) is open: do they
  carry a $\C[[\hbar]]$-flat structure as Verma-induced modules of
  some quantum algebra? No, by W3-W3-07 (Nekrasov instanton route
  fails); but a Drinfeld-Sokolov / Yangian / DAHA route may exist
  and is unexplored.
- **R-W3-W3-C.** The mixed-cone Z^2-graded subspaces are NEW. They
  may carry distinct Lie-module-class structure (positive cone is
  PBW, negative is Matlis; mixed cones are mixed PBW-Matlis with
  partial truncation). Their categorical role is unexplored. No
  named Phase-4 question here yet.

---

## §8. Convergence verdict

W3 closes the wave-3 attack on M-29 + R-W4-A:

* **M-29 survives** the Nekrasov equivariant attack. The universal
  categorical no-go is robust: T^2-equivariant rescaling, K-theoretic
  refinement, wall-crossing across all Z^2 chamber decompositions,
  and Procesi-Razmyslov-stable equivariantization all fail to break
  the obstruction. This is a strong reinforcement of M-29's status.
* **R-W4-A is REALIZED in the positive** by the Laurent ring modulo
  constants on the punctured plane. This is a concrete, classical,
  Hamiltonian-equivariant Z^2-graded sheaf with the corrected
  indicator-free formula. The wave-2 §4 indicator was WRONG and
  should be removed.
* **The Examples lens confirms** that N = 2 is the boundary stratum
  smallest non-trivial case; the wave-2 derived-intersection
  narrative is structurally robust at all N >= 2 with growing
  complexity.
* **No manuscript change required.** The two ledger heals
  (H-W3-W3-A, H-W3-W3-B) are corrections to the wave-2 W4 reconstitution
  ledger, NOT to inscribed manuscript text.

The single most actionable W3 deliverable is the **wave-2 §4 formula
correction** plus the **positive realization of R-W4-A as Laurent
ring modulo constants**. Both are durably evidence-backed by the
Lie-consistency probes in /tmp/w3_*.py (3072-5120 commutator tests
at multiple bidegrees, 0 failures with the corrected formula).

---

## §9. Provenance

* `/tmp/w3_nekrasov_equivariant_probe.py`: T1 + T4 main probe.
  Equivariant intertwiner test, character cross-check, wall-crossing
  chamber audit, Nekrasov instanton K-theoretic probe.
* `/tmp/w3_biinfinite_boundary_probe.py`: T2 forensic, exposing the
  180 wave-2 §4 indicator failures.
* `/tmp/w3_biinfinite_failure_analysis.py`: T2 correction, verifying
  the indicator-free formula passes at 0 failures.
* `/tmp/w3_matlis_match_test.py`: T2 cross-check, indicator-free
  formula matches Matlis via sigma at 360 cases.
* `/tmp/w3_local_cohomology_realization.py`: T2 identification,
  bi-infinite parent IS Laurent ring mod constants.
* `/tmp/w3_lie_with_mod_constants.py`: T2 final Lie consistency
  with mod-constants projection at 5120 cases.
* `scripts/check_derived_intersection_N2.py`: T3 verbatim re-run.
* All probes are dependency-free (Python stdlib only). Source files
  read: master ledger, wave2-W4-etingof, appendix-matlis-principal-parts.
* No web search invoked.

---

End of W3 Wave-3 ledger.
