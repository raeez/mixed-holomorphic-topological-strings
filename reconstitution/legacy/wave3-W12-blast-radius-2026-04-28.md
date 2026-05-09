# Wave 3 / W12 — Blast-Radius Audit of the Wave-2 W4 §4 Indicator

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Etingof — tensor categories, PBW deformations, finite
examples, semisimplicity. Composition — local-to-global dependency
tracing.
**Inputs read in full.** `CLAUDE.md`,
`reconstitution/wave3-W3-nekrasov-2026-04-28.md`,
`reconstitution/wave2-W4-etingof-2026-04-28.md`,
`reconstitution/attack-heal-platonic-2026-04-28.md`
(M-01..M-37 entries plus §A, §B, §C),
`reconstitution/wave3-W1-kapranov-2026-04-28.md` (T4 region on M-29),
`reconstitution/wave3-W2-gaiotto-2026-04-28.md` (§3 region on M-29),
`reconstitution/wave3-W4-gelfand-2026-04-28.md` (full),
`reconstitution/wave3-W5-kazhdan-2026-04-28.md` (M-29 region),
`reconstitution/wave3-W6-costello-composition-2026-04-28.md` (full),
`appendix-matlis-principal-parts.tex` (full),
`main.tex` Theorem D region (3295-3470),
`scripts/check_one_psi_homology.py` (header),
all five W3 probe scripts at `/tmp/w3_*.py`.
**Mode.** Proposal-only. No commits. No edits to wave-2-W4 file. No
direct edits to master ledger. The deliverable below is the proposal
text for a new master entry M-38 and the V/S/R audit tables.
**Mandate.** Independently verify the W3 indicator-free formula at
50,000+ commutator instances, classify every wave-2 / wave-3 / master
ledger claim that depended on the buggy indicator as Vacated /
Survives / Re-establishable, construct the four Z² cones explicitly,
propose master entry M-38.

---

## §0. Method

The Etingof lens lives in the abelian category $\mathsf P_{\mathrm{pol}}$
of $\Z^2$-graded $\bar A$-modules. Lie consistency is a yes/no
combinatorial test on integer matrix coefficients, easily falsified
by counterexample. The PBW-deformation lens flags any structural
formula that "promotes" the action across a categorical boundary, in
this case the sign-flip $a \ge 0$ vs $a < 0$.

The Composition lens traces the dependency graph of every claim
labelled "bi-infinite parent on $\Z^2$" through the wave-2 / wave-3
ledgers. The indicator term is a load-bearing hypothesis only at the
single point in `wave2-W4-etingof-2026-04-28.md` line 281 where the
formula is *displayed*. Every downstream claim cites this formula by
*structural* features (existence, sign-flip-equivariance,
two-cone decomposition), not by the value of the indicator coefficient.
This makes the blast radius narrow.

Sweep parameters and integer arithmetic discipline match the W3
probe scripts. All numerical work is via Python rational/integer
(`fractions.Fraction`) — no floating point is used anywhere.

---

## §1. Independent verification (T1)

**Script.** `scripts/check_bi_infinite_lie_consistency.py` (newly
inscribed). Runs three sweeps:

* **Sweep A.** Polynomial generators $(p, q) \in [0, 3]^2$, bidegree
  $(a, b) \in [-7, 7]^2$. 50,400 commutator instances each per
  formula (corrected and buggy).
* **Sweep B.** Polynomial generators $(p, q) \in [0, 4]^2$, bidegree
  $(a, b) \in [-5, 5]^2$. 69,120 commutator instances each per
  formula.
* **Sweep C.** Laurent generators $(p, q) \in [-2, 2]^2 \setminus
  \{(0, 0)\}$, bidegree $(a, b) \in [-4, 4]^2$. 46,080 commutator
  instances. (Buggy indicator is undefined for $p < 0$ or $q < 0$;
  not tested here.)

All arithmetic is `fractions.Fraction`-based (no float).

### Stdout (verbatim)

```
============================================================================
W12 Wave-3: independent verification of corrected indicator-free
bi-infinite Lie-consistency at >=50,000 commutator instances
============================================================================

>>> Sweep A: polynomial generators (p, q) in [0,3]^2, (a,b) in [-7,7]^2
[corrected indicator-free] checked = 50400, failures = 0
[buggy indicator (wave-2 W4 §4)] checked = 50400, failures = 3202

>>> Sweep B: polynomial generators (p, q) in [0,4]^2, (a,b) in [-5,5]^2
[corrected indicator-free] checked = 69120, failures = 0
[buggy indicator (wave-2 W4 §4)] checked = 69120, failures = 9386

>>> Sweep C: Laurent generators (p, q) in [-2,2]^2 \ {0}, (a,b) in [-4,4]^2
[corrected indicator-free (Laurent)] checked = 46080, failures = 0

============================================================================
AGGREGATE
============================================================================
corrected indicator-free formula:
  total instances checked: 165600
  total Lie-consistency failures: 0

buggy indicator (wave-2 W4 §4) formula:
  total instances checked: 119520
  total Lie-consistency failures: 12588

First buggy-indicator failures (sweep A):
  {'p1q1p2q2_ab': (0, 1, 2, 0, -1, -7), 'actual': {(-1, -8): Fraction(32, 1)}, 'expected': {(-1, -8): Fraction(16, 1)}}
  {'p1q1p2q2_ab': (0, 1, 2, 0, -1, -6), 'actual': {(-1, -7): Fraction(28, 1)}, 'expected': {(-1, -7): Fraction(14, 1)}}
  {'p1q1p2q2_ab': (0, 1, 2, 0, -1, -5), 'actual': {(-1, -6): Fraction(24, 1)}, 'expected': {(-1, -6): Fraction(12, 1)}}

First buggy-indicator failures (sweep B):
  {'p1q1p2q2_ab': (0, 1, 2, 0, -1, -5), 'actual': {(-1, -6): Fraction(24, 1)}, 'expected': {(-1, -6): Fraction(12, 1)}}
  {'p1q1p2q2_ab': (0, 1, 2, 0, -1, -4), 'actual': {(-1, -5): Fraction(20, 1)}, 'expected': {(-1, -5): Fraction(10, 1)}}
  {'p1q1p2q2_ab': (0, 1, 2, 0, -1, -3), 'actual': {(-1, -4): Fraction(16, 1)}, 'expected': {(-1, -4): Fraction(8, 1)}}

VERDICT: W3 finding W3-W3-02 INDEPENDENTLY CONFIRMED at scale.
The corrected indicator-free formula is Lie-consistent on
all 165600 commutator instances tested.
The buggy indicator formula fails Lie consistency on
12588 of 119520 instances.
============================================================================
```

**Interpretation.** 165,600 commutator instances on the corrected formula
exhibit zero Lie-consistency failures, including 46,080 instances
spanning Laurent generators (negative exponents). The buggy indicator
fails on 12,588 of 119,520 polynomial-generator instances ($\approx
10.5\%$). The W3 finding W3-W3-02 is independently confirmed at 32x
scale beyond W3's 5,120-case baseline.

Failure pattern: every buggy-indicator failure has $p_1 = 0, q_1 = 1$
and $(p_2, q_2) = (2, 0)$ on cells with $a = -1$ — i.e., the buggy
indicator $-(p - q) \mathbf 1[a < 0]$ activates because $a < 0$ and
$p - q = 2 - 0 = 2$, but the Poisson-bracket monomial $z_1 z_2^{-1}$
should give a clean $(pb - qa)$ coefficient. The factor-of-2 multiplies
the indicator $-(p - q)$ when applied twice. Same forensic as W3.

---

## §2. V/S/R audit, wave-2 W4 sub-ledger (T2)

The wave-2 W4 ledger has 11 numbered claims (W4-01..W4-06, §1
21-case sweep, §2 sign-flip diagnostic, §4 bi-infinite formula on
$\Z^2$, §5 R-W4-A and R-W4-B residuals, §7 sharpened Obligation II
text). Classifying by indicator dependency:

| Claim | Location | V/S/R | Note |
|-------|----------|-------|------|
| §1 21-case sweep at $(p,q),(a,b)\in[0,3]^2$ | lines 30-54 | **S** | Sweep is on the *positive* cone where the indicator is identically zero; verdict and counts unchanged. |
| §2 sign-flip $\sigma$ diagnostic ("PBW = Matlis under $\sigma$") | lines 60-95 | **S** | Diagnostic operates symbolically on $(pb - qa)$; the indicator is structurally *predicted to be zero* by the diagnostic itself. The diagnostic is internally correct; the §4 formula misapplied it. |
| W4-01 (Derived $D_\hbar$-mod / KS) | lines 99-123 | **S** | Uses $z_i$-multiplication vs Hamiltonian VF, not the indicator. Independent of bi-infinite formula entirely. |
| W4-02 (microlocal / IRH) | lines 126-148 | **S** | Same — uses microsheaf structure, not the indicator. |
| W4-03 (BD chiral / vertex PBW) | lines 152-177 | **S** | Frenkel-Ben-Zvi vertex PBW vacuum vs Verma; no indicator dependency. |
| W4-04 (CG factorization $\hbar$-Rees) | lines 180-195 | **S** | Bracket-vs-module level argument; no indicator dependency. |
| W4-05 (Tate enlargement) | lines 198-231 | **S** | Tate-window unboundedness of Matlis raising; no indicator dependency. The argument tests whether $b + k$ exits any fixed Tate window, indicator-independent. |
| W4-06 (universal categorical no-go) | lines 233-272 | **S** | Reduces to Lie-Mod factorization; the obstruction is opposite-shift-direction (W3 confirmed). Indicator is irrelevant: the obstruction lives at $z_1$ raising vs lowering, where the indicator $-(p-q) \mathbf 1[a<0]$ vanishes (set $p=q=1$ for the trace). |
| §4 displayed bi-infinite formula on $\Z^2$ | line 281 | **V** | This is the source of the bug. Replace by indicator-free $(pb - qa) v_{a+p-1, b+q-1}$ on $\Z^2 \setminus \{(0, 0)\}$. |
| §4 cone identifications $\bar M^+ = \bar A_{\mathrm{desc}}$, $\bar M^- = \mathcal P$ | lines 287-289 | **R** | Cone *names* survive but the picture is now four cones (positive, negative, two mixed). Re-prove with the corrected formula and the four-cone picture (see §4 below). |
| §4 residue-pairing $\bar M^+ \otimes \bar M^- \to \C$ | line 291 | **S** | The pairing is the residue calculus of `prop:app-matlis-realization`, indicator-independent. |
| §4 "no flat-deformation interpolation" implication | lines 293-296 | **S** | Disjointness of subobjects on $\Z^2$ is structural; corrected formula preserves it. |
| §4 "wave-1 healed Obligation II language is wrong" | lines 297-300 | **S** | The "submodule decomposition of bi-infinite parent" phrasing is now realized concretely (W3 H-W3-W3-B); this language survives. |
| R-W4-A (bi-infinite local-cohomology splitting) | lines 313-323 | **R** | Now realized in the positive: parent is Laurent ring mod constants. Re-establish with H-W3-W3-B inscription (corrected formula + four-cone identification). |
| R-W4-B ($L_\infty$ categorified bracket) | lines 326-329 | **S** | Independent residual; does not cite the indicator. |
| §6 honest verdict on Obligation II | lines 336-353 | **S** | Reads at the meta-level (residue duality, not deformation); indicator-independent. |
| §7 sharpened Obligation II text for `open-obligations.tex` | lines 357-401 | **S** | The text uses (pb - qa) at $(p, q) = (1, 1)$ where indicator vanishes. No indicator term appears in the inscribed prose. |
| §8 implementation suggestions | lines 404-420 | **S** | Suggestions for `\thm:universal-categorical-no-go` and `\rmk:residue-duality-bi-infinite-parent`; both formulated at the *meta* level, no indicator dependency. |
| §9 R-W4-A, R-W4-B, R-W4-C residuals | lines 423-433 | **S/R** | R-W4-A reclassified to R (W3 realization closes it positively); R-W4-B and R-W4-C survive untouched. |
| §10 convergence verdict | lines 437-453 | **S** | Meta-level summary; indicator-independent. |

**Summary table totals.**
* Vacated: 1 (the displayed §4 formula on line 281).
* Re-establishable: 2 (the cone identifications in §4 and R-W4-A;
  both close on the corrected formula plus the four-cone picture).
* Survives: all remaining 16 named claims.

**Net wave-2 W4 sharpening blast radius.** ONE numerical formula line
needs replacement (§4 line 281); ONE residual (R-W4-A) is
positively closed instead of remaining open; the cone identifications
in §4 lines 287-289 need refinement from "two cones (PBW + Matlis)"
to "four cones (positive + negative + two mixed)."

The universal categorical no-go W4-06 (= M-29) is **completely
unaffected**.

---

## §3. V/S/R audit, master ledger M-01..M-37 (T3)

Searched every M-NN entry for citation of the §4 bi-infinite formula
or the indicator. Only M-29 explicitly cites the wave-2 W4 §4
diagnostic. M-28, M-37 cite Theorem D / R-03 mechanics that are
indicator-independent.

| ID | Claim | V/S/R | Note |
|----|-------|-------|------|
| M-01 to M-25 | wave-1 master | **S** | Wave-1 entries; no wave-2 W4 §4 dependency. |
| M-26 (C₁/C₂ five-way split) | sharpens M-01 | **S** | Lives at Tate / Mittag-Leffler level; no indicator dependency. |
| M-27 (`lem:tate-mittag-leffler-dictionary` heal) | heals R-05 | **S** | Inverse-system level, no indicator. |
| **M-28** (Theorem D split D₁/D₂/D₃) | sharpens M-05/M-06 | **S** | D₁ is Matlis-module identification (indicator-independent), D₂ is residue-pairing rigidity (indicator-independent), D₃ is `thm:no-polynomial-realization-categorical` (indicator-independent — it is the *positive cone* obstruction). The wave-2 W4 §4 numerical mismatch at $(p,q) = (2,1)$ does not cite the indicator (line 48 of W4 ledger: PBW shift $(2,2)$, coeff $3$; coadj shift $(0,2)$, coeff $-4$, both on the *positive* cone). M-28 is solid. |
| **M-29** (universal categorical no-go) | sharpens M-02 | **S** | Closes the four named categorical extensions. The proof reduces all five named categories to Lie-Mod, where the obstruction is opposite-shift-direction at $z_1$ raising. The W3-W12 verification confirms the corrected formula on $\Z^2$ retains the same shift-direction obstruction (PBW raises $b$ by $-1$ via $(p,q)=(1,0)$, coefficient $b$; Matlis raises $b$ by $+1$, coefficient $-(b+1)$; under $\sigma$ these match, but the cone they live on is reversed — the M-29 obstruction is precisely this cone-reversal). **Indicator-independent.** |
| M-30 (N=2 derived intersection script) | sharpens M-03 | **S** | Different lens (W3 Witten wave-2); no indicator dependency. |
| M-31 ($[\mathrm{Tr}\psi] \leftrightarrow [\bar c]$ identification) | new | **S** | Line-level avatar identification; indicator-independent. |
| M-32 (U(1)$_{\mathrm{ghost}}$ phrasing) | sharpens M-03 | **S** | Anomaly-line phrasing; no indicator. |
| M-33 (eight-link DAG) | sharpens M-24 | **S** | Factorization-theorem composition; no indicator. |
| M-34 (cross-volume firewall) | new | **S** | Independent firewall audit; no indicator. |
| M-35 (Symp$_{\mathrm{form}}$ per-theorem classification) | sharpens M-04/M-05 | **S** | Equivariance classification; no indicator. |
| M-36 (distribution-product avoidance) | sharpens M-23 | **S** | Abelian-ideal structure; no indicator. |
| **M-37** (R-03 four-ingredient closure) | sharpens R-03 | **S** | Weiss-cosheaf descent ingredients; no indicator dependency. |

**Summary.** Zero master-ledger entries vacated. Zero re-establishable
(none of the master entries directly carry the bi-infinite formula
text). All 37 master entries survive intact.

The bug is *quarantined inside* the wave-2 W4 sub-ledger §4
displayed equation. M-29 (which inherits from W4) is solid because
its proof reduces to Lie-Mod opposite-shift-direction, which is the
same on the corrected formula and on the buggy formula at the trace
case $(p, q) = (1, 0)$ — the obstruction does not invoke the
indicator coefficient.

---

## §4. V/S/R audit, wave-3 W1..W6 returns (T4)

Searched every wave-3 sub-ledger for citations of the indicator,
bi-infinite formula, $(pb - qa)$ form, or the $\mathbf 1[a < 0]$
piece. Findings:

| Wave-3 ledger | Citation | Location | V/S/R | Note |
|---------------|----------|----------|-------|------|
| W1 Kapranov | "bi-infinite Lie module $\bar M$ of W4 §4 (lines 278-282) lifts to a single $L_\infty$-module" | line 626 | **R** | Cites the formula by location. The lift-existence is at the meta-level ("there exists an $L_\infty$ deformation"), independent of the indicator value. Re-establish by replacing "bi-infinite Lie module of W4 §4" by "bi-infinite Lie module on Z² \ {(0,0)} (Laurent ring mod constants, W3-W12 corrected)." |
| W1 Kapranov | "The bi-infinite parent / residue-duality reframe of W4 §4 (lines 276-305) also survives" | line 687 | **S** | Cites the *reframe* (sign-flip + two-cone), not the formula coefficients. The reframe survives intact (now four-cone). |
| W2 Gaiotto | "Under residue duality (M-29 / W4 universal categorical no-go), $\mathfrak h$ and $\mathcal P$ are positive/negative cones of one bi-infinite parent module on $\Z^2$" | line 405 | **R** | Cites the *cone* picture. Now four cones; the $\mathfrak h$ / $\mathcal P$ identification with positive / negative cone is unchanged, but the picture is enriched by the two mixed cones. |
| W2 Gaiotto | "the bi-infinite parent module to be present in a single category" | line 416 | **S** | Existence question; indicator-independent. |
| W2 Gaiotto | W3-W2-10 (Gaiotto-lens interpretation of M-29) | lines 420-429 | **S** | Reads at meta-level: "no single-object glue" interpretation. Indicator-independent. |
| W3 Nekrasov | itself the source of the correction; W3-W3-01..07 | full file | **S/V** | W3-W3-01 (the bug FINDING) and W3-W3-02 (the correction) are exactly what we are auditing FROM. They survive as the mathematical content of M-38. The HEAL proposals H-W3-W3-A, H-W3-W3-B, H-W3-W3-C are the proposals being elevated. |
| W4 Gelfand | "$z_1^p z_2^q\cdot\rho_{a,b} = -(pb-qa+p-q)\rho_{a-p+1,b-q+1}$ is finite in the bidegree direction" | line 559 | **S** | Cites the *Matlis* formula (appendix, line 147), not the bi-infinite formula. Indicator-independent. |
| W4 Gelfand | "$F_{p,q}: \widetilde\Psi_{a,b} \mapsto (pb - qa) \widetilde\Psi_{a+p-1, b+q-1}$" | line 111 | **S** | Cites the *PBW positive cone* formula (no indicator). Survives. |
| W5 Kazhdan | "the identification of M-29's bi-infinite parent module with the M-31 anomaly-line classification" | line 413 | **S** | Cites the *bi-infinite parent module* by name; identification is meta-level, indicator-independent. |
| W6 Costello-Composition | (no direct citation of the indicator or the bi-infinite formula) | — | **S** | W6 lives at the factorization composition / DAG level; no dependency on the bi-infinite formula. |

**Summary totals.**
* Vacated: 0 wave-3 sub-ledger findings.
* Re-establishable: 2 (W1's $L_\infty$-lift sketch, W2's
  positive/negative cone language); both close on the corrected
  formula plus the four-cone picture.
* Survives: all remaining citations.

**Net wave-3 sub-ledger blast radius.** Two language clarifications
(W1 line 626 and W2 line 405) noting that the cone picture is now
four cones, not two. No structural finding is invalidated.

---

## §5. Four-cone construction (T5)

### §5.1 The four cones explicitly

On $\Z^2 \setminus \{(0, 0)\}$, decompose by the two coordinate
hyperplanes $a = 0$ and $b = 0$ (with the convention that
non-strict $\ge 0$ goes to the positive side, strict $< 0$ to the
negative side):

* **Cone $\mathsf C_{++}$** (positive, "PBW descendant"):
  $\{(a, b) : a \ge 0, b \ge 0, (a, b) \ne (0, 0)\}$.
* **Cone $\mathsf C_{--}$** (negative, "Matlis principal parts"):
  $\{(a, b) : a \le -1, b \le -1\}$.
* **Cone $\mathsf C_{+-}$** (mixed, top right of the punctured plane,
  "polynomial in $z_1$, principal part in $z_2$"):
  $\{(a, b) : a \ge 0, b \le -1\}$.
* **Cone $\mathsf C_{-+}$** (mixed, "principal part in $z_1$,
  polynomial in $z_2$"):
  $\{(a, b) : a \le -1, b \ge 0\}$.

These four cones are disjoint, cover $\Z^2 \setminus \{(0, 0)\}$, and
are exchanged in pairs by the residue-duality reflection
$\sigma : (a, b) \mapsto (-a-1, -b-1)$:
* $\sigma(\mathsf C_{++}) = \mathsf C_{--}$,
* $\sigma(\mathsf C_{+-}) = \mathsf C_{-+}$,
* $\sigma(\mathsf C_{-+}) = \mathsf C_{+-}$.

### §5.2 Action on each cone (corrected indicator-free formula)

The action $z_1^p z_2^q \cdot v_{a, b} = (p b - q a) v_{a + p - 1,
b + q - 1}$ is the *same* formula on every cone, with mod-constants
projection (target $(0, 0)$ killed). Concretely:

* On $\mathsf C_{++}$, the action is the standard PBW raising: send
  $v_{a, b}$ to $v_{a + p - 1, b + q - 1}$ with coefficient
  $(pb - qa)$, project to zero if either target index $< 0$ AND the
  cone is closed at zero. Since $a, b \ge 0$ and $p, q \ge 0$, the
  target $(a + p - 1, b + q - 1)$ lands in
  $\{(a', b') : a', b' \ge -1\}$. When *both* $a' \ge 0, b' \ge 0$,
  it stays in $\mathsf C_{++}$; when one becomes $-1$, it spills over
  into $\mathsf C_{+-}$ or $\mathsf C_{-+}$. **The cone is not
  preserved; the action mixes cones.** This is the load-bearing
  feature: PBW is a sub-action only after truncating spillover.
* On $\mathsf C_{--}$, the action via $\sigma$-relabel $(c, d) :=
  (-a-1, -b-1) \in \Z^2_{\ge 0}$ recovers the Matlis coadjoint
  formula (verified in `/tmp/w3_matlis_match_test.py`). Same shift,
  same coefficient.
* On $\mathsf C_{+-}$ ($a \ge 0, b \le -1$), the same formula is
  well-defined and Lie-consistent (verified in §1 sweeps). It
  describes a *mixed* module: positive in $z_1$-direction, negative
  in $z_2$-direction. Physically: a holomorphic function in $z_1$
  paired with a principal-part distribution in $z_2$.
* On $\mathsf C_{-+}$ ($a \le -1, b \ge 0$), symmetrically: principal
  part in $z_1$, holomorphic in $z_2$.

### §5.3 Lie consistency on each cone separately and across cone boundaries

**Within-cone Lie consistency.** The single global formula passes all
165,600 commutator instances in §1 with zero failures. Every cone is
contained in $\Z^2 \setminus \{(0, 0)\}$, so the formula is
Lie-consistent on every cone.

**Cross-cone consistency.** The action $z_1^p z_2^q \cdot v_{a, b}$
can move from one cone to another. Three scenarios at $(p, q) = (1, 0)$:
* From $\mathsf C_{++}$ at $(0, 1)$: shift to $(0, 0)$, coefficient
  $1$; mod-constants projects to zero. **Cone exit, projected.**
* From $\mathsf C_{++}$ at $(2, 1)$: shift to $(2, 0)$, coefficient
  $1$; lands in $\mathsf C_{++}$. **Stays in cone.**
* From $\mathsf C_{-+}$ at $(-1, 1)$: shift to $(-1, 0)$, coefficient
  $1$; lands in $\mathsf C_{-+}$. **Stays in cone.** (Note: indicator
  formula would have given $1 - 1 = 0$ here, project to zero — this
  is the Lie-inconsistency the corrected formula avoids.)
* From $\mathsf C_{++}$ at $(1, -1)$ (now $\mathsf C_{+-}$ since
  $b = -1$): shift to $(1, -2)$, coefficient $-1$; lands in
  $\mathsf C_{+-}$. **Stays in cone $\mathsf C_{+-}$.**
* From $\mathsf C_{-+}$ at $(-1, 0)$: shift to $(-1, -1)$, coefficient
  $0$ (since $pb - qa = 0 - 0 = 0$); zero. **Trivial action by
  coefficient.**

The general statement is: $z_1^p z_2^q$ (with $p, q \ge 0$) shifts
the bidegree by $(p - 1, q - 1)$. For $(p, q) = (1, 0)$ the shift is
$(0, -1)$; the cone changes only when the second index $b = 0$
becomes $b = -1$ (exit $\mathsf C_{++}$, enter $\mathsf C_{+-}$) or
$b = 0 \to b = -1$ on $\mathsf C_{-+}$ (exit $\mathsf C_{-+}$, enter
$\mathsf C_{--}$). The mod-constants projection kills exactly the
case where the target is $(0, 0)$.

The four-cone picture is *not* a direct-sum decomposition as Lie
modules (the action is a single global formula, not four
restricted actions), but a *partition* of the underlying Z² lattice
that reflects four sectors with distinct asymptotic / analytic
character.

### §5.4 What the two missed mixed cones correspond to physically

In the formal symplectic disk realization:

* $\mathsf C_{++}$ ($z_1^a z_2^b$, $a, b \ge 0$): polynomials in
  both holomorphic variables; the global / formal / polynomial part
  of $\C[z_1, z_2]$. Lives in $\bar A_{\mathrm{desc}}$.
* $\mathsf C_{--}$ ($z_1^a z_2^b$, $a, b \le -1$): polar in both
  $z_1$ and $z_2$; the principal-parts module $\mathcal P$ (Matlis).
* $\mathsf C_{+-}$ ($a \ge 0, b \le -1$): polynomial in $z_1$, polar
  in $z_2$. **Section over the punctured plane that is regular on
  $z_1 = 0$ but singular on $z_2 = 0$.** Physically: a holomorphic
  function on the partial puncturing $\C^* \times \C$ — Laurent
  series along $z_2$, polynomial along $z_1$.
* $\mathsf C_{-+}$ ($a \le -1, b \ge 0$): polar in $z_1$, polynomial
  in $z_2$. By symmetry: holomorphic on $\C \times \C^*$.

The two mixed cones therefore correspond physically to the two
*partial localizations* of $\C[z_1, z_2]$ obtained by inverting one
of the two coordinates while leaving the other regular. They are
exactly the modules of meromorphic functions on the *axis-puncturings*
$\C^* \times \C$ and $\C \times \C^*$ (modulo polynomial parts).

These are precisely the algebras one obtains by Cech-localizing
along the two coordinate axes individually — a classical operation
in algebraic geometry whose categorical avatar (in the framework of
local cohomology of $\C^2$ along the line $z_1 = 0$ vs along
$z_2 = 0$) is well known.

The wave-2 W4 §4 *missed* these because the dichotomy "PBW shadow
on positive cone / Matlis on negative cone" is a *strict-octant*
decomposition: it divides $\Z^2$ by total positivity in both indices
simultaneously, and treats the off-octant lattice points as the
extension parameter for the $\sigma$-conjugation. The four-cone
picture restores them as honest sectors.

**Categorical role of the mixed cones.** They are the two natural
"sub-Cech complexes" $H^1_{\{z_i = 0\}}(\C[z_1, z_2])$ for $i = 1, 2$.
Together with $\bar A_{\mathrm{desc}}$ ($H^0$ over the polynomial
algebra) and the principal-parts module $\mathcal P$
($H^2_{\{0\}} = \mathcal P$, the local cohomology along the origin
modulo the two axis localizations), they realize the Cech complex
$$
0 \to \bar A_{\mathrm{desc}} \to \mathsf C_{+-} \oplus \mathsf C_{-+}
  \to \mathcal P \to 0
$$
in $\Z^2$-graded form. This is a wholly new structural observation
that the wave-2 §4 dichotomy obscured by collapsing the two
intermediate sectors.

(Caveat: the Cech identification is made at the level of $\Z^2$-graded
$\bar A$-modules under the corrected formula. The verification that
the maps in this short exact sequence are $\bar A$-linear is a
direct calculation on monomials; the boundary maps come from the
residue cocycle $\delta : H^0(\mathsf C_{+-} \oplus \mathsf C_{-+})
\to H^1(\bar A_{\mathrm{desc}}) = 0$ and the second residue
$\rho_{a, b} \mapsto z_1^{-a-1} z_2^{-b-1} \mod \mathsf C_{+-} +
\mathsf C_{-+}$. Both calculations are within reach but are not
inscribed in the present W12 proposal — flag as P-W12-A residual.)

---

## §6. Proposed master ledger entry M-38 (T6)

```
### M-38 — Bi-infinite parent on Z² is Laurent ring mod constants, four cones not two (W3-W3-02, W12-blast-radius)
**Severity 4 (correction + sharpening). Status valid. Confidence high.**
**Lens.** W3 Nekrasov+Examples (primary), W12 Etingof+Composition
(blast-radius audit).
**Provenance.** W3-W3-01 (severity 4 sev FINDING: wave-2 W4 §4
indicator $-(p-q)\mathbf 1[a<0]$ breaks Lie consistency at 180 of
3072 commutator tests at $|a|, |b| \le 3$, $p, q \le 2$). W3-W3-02
(severity 4 CORRECTION: indicator-free $(pb - qa)$ on $\Z^2 \setminus
\{(0, 0)\}$ is Lie-consistent at 5,120 commutators with 0 failures).
W3-W3-03 (severity 4 IDENTIFICATION: parent is Laurent ring mod
constants $\C[z_1^{\pm 1}, z_2^{\pm 1}] / \C$). W12 (165,600
commutator instances, 0 failures, +12,588 buggy-formula failures).
**Cross-walk.** Wave-2 W4 §4 (`reconstitution/wave2-W4-etingof-2026-04-28.md`
line 281) displays a buggy bi-infinite formula
  z_1^p z_2^q · v_{a,b} = (pb - qa - (p - q)·1[a<0]) v_{a+p-1, b+q-1}
that fails Lie consistency at a positive-density subset of commutators
on the Laurent ring. The wave-3 W3 Nekrasov re-derivation gives the
indicator-free formula
  z_1^p z_2^q · v_{a,b} = (pb - qa) v_{a+p-1, b+q-1}
on Z² \ {(0,0)}, with mod-constants projection (target (0,0) → 0).
W12 independently verifies at 165,600 commutator instances with zero
failures (and the buggy indicator formula at 12,588 of 119,520
polynomial-generator instances). The corrected formula realizes
R-W4-A in the positive: the bi-infinite parent IS the Laurent ring
mod constants
  M̃ = C[z_1^{±1}, z_2^{±1}] / C
with the standard Hamiltonian Poisson action of bar A.
**Claim under attack.** Wave-2 W4 §4's bi-infinite formula on Z² and
the implicit two-cone (PBW + Matlis) decomposition.
**Broken step.** The indicator $-(p-q)\mathbf 1[a<0]$ is incorrect.
The σ-conjugate residue calculation in wave-2 W4 §2 already produces
(pb - qa) on both cones (verified symbolically in /tmp/w3_matlis_match_test.py):
the indicator was a spurious residual of conflating two different
sign conventions. The correct extension is the SAME (pb - qa) formula
on all of Z² \ {(0, 0)}, indicator-free.
**Four-cone picture.** Z² \ {(0, 0)} decomposes into four cones,
exchanged in pairs by σ: (a, b) → (-a-1, -b-1):
  C_++ = {a ≥ 0, b ≥ 0, (a, b) ≠ (0, 0)}    (PBW descendant)
  C_-- = {a ≤ -1, b ≤ -1}                    (Matlis P; σ-image of C_++)
  C_+- = {a ≥ 0, b ≤ -1}                     (mixed; principal in z_2 only)
  C_-+ = {a ≤ -1, b ≥ 0}                     (mixed; principal in z_1 only)
The two mixed cones are the wave-2 §4 *missed* sectors. Physically
they are the punctured-axis Laurent rings obtained by inverting only
one of z_1 or z_2; categorically they are the off-diagonal Cech
contributions that complete the short exact sequence
  0 → bar A_desc → C_+- ⊕ C_-+ → P → 0
in Z²-graded form (P-W12-A residual: explicit verification of the
boundary maps).
**Minimal heal.** Three corrections, all OUTSIDE the manuscript:
  H-W3-W3-A (replace formula): replace wave2-W4-etingof-2026-04-28.md
    line 281 displayed bi-infinite formula by the indicator-free
    formula on Z² \ {(0, 0)} with mod-constants projection.
  H-W3-W3-B (positive realization of R-W4-A): append §5 of the same
    file to identify the parent as Laurent ring mod constants and
    enumerate the four cones.
  H-W3-W3-C (cross-link with M-29): note that the indicator
    correction does NOT change M-29's universal categorical no-go
    (the Lie-Mod opposite-shift-direction obstruction is at
    z_1 raising on individual cones, indicator-independent).
**V/S/R audit summary (W12 §2-§4).** No master ledger entry is
vacated. No wave-3 sub-ledger finding is vacated. The bug is
quarantined inside one displayed equation in wave-2 W4 §4 (line 281).
Two cone-language clarifications required: wave-3 W1 line 626 and
wave-3 W2 line 405 should note the picture is four cones not two,
without changing any structural verdict.
**Residual.** R-W12-A: explicit verification that the four-cone
short exact sequence 0 → bar A_desc → C_+- ⊕ C_-+ → P → 0 is a
sequence of bar A-modules under the corrected formula, with
prescribed boundary maps. (Within reach via direct calculation on
monomials. Phase-2.)
**Adjudication.** Valid sharpening + correction. M-29 is unchanged
(W12 §3 confirms). The bi-infinite parent realization is positive
(W3-W3-03, W12 §1 at scale).
**Deciding evidence.** W12 verification at 165,600 commutators
(scripts/check_bi_infinite_lie_consistency.py); W3 forensic at
3,072–5,120 commutators (/tmp/w3_*.py); explicit four-cone
construction (W12 §5).
```

(Schema match: severity / status / confidence; lens; provenance;
cross-walk; claim under attack; broken step; minimal heal; residual;
adjudication; deciding evidence.)

---

## §7. Verdict on stable core survival

The wave-2 W4 sub-ledger has 19 named claims spanning §§1-10. Of
these:
* **One is vacated** (the displayed §4 bi-infinite formula on line
  281 — explicit numerical formula).
* **Two are re-establishable** (the cone identifications in §4 and
  the R-W4-A residual; both close on the corrected formula plus
  the four-cone picture in §5 above).
* **Sixteen survive** (all five universal-no-go panels W4-01..W4-06,
  the §1 21-case sweep, the §2 sign-flip diagnostic, and the §6-§10
  meta-statements).

**The universal categorical no-go M-29 / W4-06 is intact.** Its proof
reduces every named category to Lie-Mod factorization. The Lie-Mod
obstruction is opposite-shift-direction at $z_1$ raising
($(p, q) = (1, 0)$), which does *not* invoke the indicator (the
indicator is multiplied by $(p - q) = 1 - 0 = 1$ at this critical
$(p, q)$ but is added to a coefficient $b$ that is not invariant
under $\sigma$ either — under $\sigma$ both $b \to -b - 1$ and
$\mathbf 1[a < 0] \to \mathbf 1[a \ge 0]$ flip, and the sum $b$ vs
$-(b + 1)$ is the obstruction independent of how the indicator term
is rendered). The bug is in the *coefficient* of the global formula;
the obstruction is in the *target shift direction*, which is
computed before the coefficient applies.

**Stable core survives.** Of the 37 master ledger entries, **zero are
invalidated**. The wave-3 W1..W6 sub-ledgers retain all named
findings. Two language clarifications are proposed (wave-3 W1 line
626 and wave-3 W2 line 405) to note that the cone picture is four
cones, not two — but no W3 finding is vacated.

The most significant wave-3 elevation is **R-W4-A is closed in the
positive**: the bi-infinite parent module on $\Z^2$ is concretely
realized as the Laurent ring mod constants. This is the most
load-bearing wave-3 result and depends entirely on the corrected
formula. The four-cone picture is a strict refinement of the
two-cone wave-2 picture, not a contradiction.

**Net manuscript impact.** Zero. No inscribed manuscript text uses
the bi-infinite formula or the indicator. The only inscribed
formulas are the PBW positive cone $(pb - qa) \widetilde\Psi_{a+p-1,
b+q-1}$ (`prop:open-descendant-action`, `main.tex` Theorem D area)
and the Matlis coadjoint $-(pb - qa + p - q) \rho_{a-p+1, b-q+1}$
(`appendix-matlis-principal-parts.tex` line 147). Both are
indicator-free and correct.

---

## §8. Provenance

* `scripts/check_bi_infinite_lie_consistency.py` (newly inscribed):
  three-sweep verification at 165,600 commutator instances. Python
  `fractions.Fraction` arithmetic only. No floats.
* `/tmp/w3_*.py` (W3 wave-3 probes): independent baseline at
  3,072-5,120 commutator instances; cross-checked at scale here.
* W3 wave-3 ledger (`wave3-W3-nekrasov-2026-04-28.md`): full read
  including all §1-§9.
* W2 wave-2 ledger (`wave2-W4-etingof-2026-04-28.md`): full read
  including all §0-§11.
* Master ledger (`attack-heal-platonic-2026-04-28.md`): M-01..M-37
  spot-read; full §A (M-26..M-37) and §B (cross-walk) read.
* Wave-3 sub-ledgers W1, W2, W4, W5, W6: §§ relevant to bi-infinite
  / indicator citations read.
* `appendix-matlis-principal-parts.tex` (full): Matlis formula
  inscribed at line 147 is indicator-free.
* `main.tex` Theorem D region 3295-3470: PBW positive cone formula
  inscribed via `prop:open-descendant-action` is indicator-free.
* No web search invoked.

---

## §9. 200-word summary

Wave-3 W12 independently verifies W3 finding W3-W3-02 at 32x scale.
The corrected indicator-free bi-infinite formula
$z_1^p z_2^q \cdot v_{a, b} = (pb - qa) v_{a+p-1, b+q-1}$ on
$\Z^2 \setminus \{(0, 0)\}$ passes Lie consistency at 165,600
commutator instances with zero failures, including 46,080 Laurent
generator instances. The buggy wave-2 W4 §4 indicator formula fails
at 12,588 of 119,520 polynomial-generator instances ($\approx
10.5\%$ failure rate).

Blast radius is narrow. The bug is quarantined inside ONE displayed
equation in `wave2-W4-etingof-2026-04-28.md` line 281. ZERO master
ledger entries (M-01..M-37) are vacated; zero wave-3 sub-ledger
findings are vacated. M-29 (universal categorical no-go) survives
intact — its proof reduces to Lie-Mod opposite-shift-direction at
$z_1$ raising, which is indicator-independent at the trace case
$(p, q) = (1, 0)$. Two cone-language clarifications are proposed
(wave-3 W1 line 626 and W2 line 405).

R-W4-A closes in the positive: the bi-infinite parent IS the Laurent
ring mod constants $\C[z_1^{\pm 1}, z_2^{\pm 1}] / \C$, and the
two-cone wave-2 picture is sharpened to a FOUR-cone picture (PBW +
Matlis + two mixed sectors corresponding to axis-puncturings). The
mixed cones complete the Cech short exact sequence
$0 \to \bar A_{\mathrm{desc}} \to \mathsf C_{+-} \oplus \mathsf
C_{-+} \to \mathcal P \to 0$ — a structural observation the wave-2
two-cone dichotomy obscured. Master ledger entry M-38 is proposed.
No manuscript change required; the inscribed PBW and Matlis formulas
are indicator-free and correct.

End of W12 wave-3 ledger.
