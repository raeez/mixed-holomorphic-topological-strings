# Phase-4 EXEC / P4-A1-HYP-AUDIT — Costello + Hypotheses Inheritance Audit

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Costello primary (factorization, BV/BRST, RG locality,
admissible regulator class formal definition, Costello 2011
Renormalization Ch. 4 §4.4 grounding); Hypotheses secondary
(precise statement of (A1)–(A5) variants, transitive-closure of
which combinations make Theorem G chain-level closed).
**Mode.** Proposal-only. Master ledger schema; ID prefix
`P4-EXEC-A1-`. No commits, no manuscript edits.
**Mandate.** Build the publication-grade hypothesis inheritance
graph and dependency audit across all Phase-4 EXEC milestones for
the load-bearing (A1)–(A5) admissible-regulator hypotheses;
identify silent strengthenings, circular dependencies; produce
graph-readable inheritance ledger; classify Theorem G chain-level
closure status under the weakest sufficient hypothesis combination.

**Inputs read in full.**
- `CLAUDE.md` (full).
- `reconstitution/attack-heal-platonic-2026-04-28.md` (master
  ledger; Wave-3 FINAL §M-01..M-68; Phase-4 EXEC progress §3998–4357).
- `reconstitution/wave3-W22-supertrace-rigorous-2026-04-28.md` (1049
  lines; W22-T1, W22-T2, W22-Obs; lemmas L1/L2/L3).
- `reconstitution/wave3-W30-A5-heal-2026-04-28.md` (867 lines;
  precise (A5) formulation; verification on three regulator schemes).
- `reconstitution/wave3-W15-conditional-theorems-2026-04-28.md`
  (W3-W15-03, W3-W15-04 — Theorem G residue $=\hbar N[\bar c]$).
- `reconstitution/phase4-exec-osp-supertrace-2026-04-28.md` (757
  lines; P4-G3-T-A1 DISCHARGED on $\mathfrak{osp}(2N|2N)$).
- `reconstitution/phase4-exec-classical-super-extension-2026-04-28.md`
  (1247 lines; P4-G3-M2 strategic boundary across psl/p/q/sl(M|N)).
- `reconstitution/phase4-exec-unreduced-primitive-2026-04-28.md`
  (933 lines; G5 RELAUNCH-2; W18-C3 closes negatively).
- `reconstitution/phase4-exec-reduced-primitives-catalog-2026-04-28.md`
  (1151 lines; G5-M2 closes negatively across 5 candidate primitives).
- `reconstitution/phase4-exec-module-lambda-bracket-2026-04-28.md`
  (598 lines; P4-G2-M1 module λ-bracket DISCHARGED).
- `reconstitution/phase4-exec-G2G3-transversality-2026-04-28.md`
  (898 lines; joint Theorem F$''$ transversality verified).
- `reconstitution/phase4-exec-CGW-anchor-2026-04-28.md` (1049 lines;
  G4 CGW anchor with spin-tower correction; Heisenberg level
  identified).
- `reconstitution/phase4-exec-G4-M2-Heisenberg-twist-2026-04-28.md`
  (1193 lines; G4-M2 PARTIAL; Lurie HA §5.5.4.10 Bousfield).
- `reconstitution/phase4-exec-editorial-specimen-2026-04-28.md`,
  `reconstitution/phase4-exec-editorial-specimen-2-HKR-2026-04-28.md`
  (G6 editorial specimens).
- `main.tex` (Theorems G `thm:u1-center-anomaly`,
  `thm:u1-center-anomaly-open`, `thm:quantum-classical-anomaly`;
  `lem:omega-cocycle`).
- `appendix-unreduced-bv-qme.tex` (full, 179 lines).
- `tate-T1-weighted-completion.tex` (`defn:regulator-admissible-sector`
  at 596–632; `thm:wt-regulator-independence-admissible` at 634–707).
- `claim-strength-ledger.tex` (current 142 lines).

**Primary external sources cited.**
- K. Costello, *Renormalization and Effective Field Theory*, AMS
  Math. Surveys & Monographs 170 (2011), Ch 4 §4.4 (counterterm
  finiteness, regulator class).
- K. Costello, O. Gwilliam, *Factorization Algebras in QFT*, Vol I
  (CUP 2017) §6.4–6.5; Vol II (CUP 2021) §11 (BV regulator), §13.
- J. Lurie, *Higher Algebra*, §5.5.4 (Bousfield localisation;
  Theorem 5.5.4.10 locally constant factorization equivalent to
  $E_n$-algebras; Theorem 5.5.4.16 Dunn additivity).
- M. Bershadsky, S. Cecotti, H. Ooguri, C. Vafa, *Comm. Math.
  Phys.* **165** (1994), 311–427 (BCOV closed B-model).

---

## §0. Executive verdict

**Six (A1)–(A5) variants currently in use.** Beyond the manuscript's
inscribed (A1)–(A4) plus the proposed (A5), the audit identifies
**one additional silent variant, (A2$'$)**, used in P4-EXEC-G3-T-A1
(osp) and P4-EXEC-G3-M2 (classical super extension), namely
*existence of an even non-degenerate ad-invariant supersymmetric
bilinear form on the matrix source*. This is structurally implicit
in (A5)'s "BV bilinear form is parity-equivariant" but is logically
distinct: (A2$'$) is an **existence** condition; (A5) is a
**compatibility** condition assuming the form exists. The (M2)
$\mathfrak p(N)$ failure proves (A2$'$) is non-vacuous: periplectic
satisfies the $\Z/2$-grading-respect of (A5) on the *Lie* level, but
fails (A2$'$) at the form-existence layer. **Silent strengthening
identified** — see §1.6 below.

**Number of milestones discharged unconditionally vs conditionally
under the inscribed (A1)–(A4) hypothesis class.**

* **Unconditional under (A1)–(A4):**
  - Theorem G (`thm:u1-center-anomaly`,
    `thm:u1-center-anomaly-open`, `thm:quantum-classical-anomaly`)
    on bosonic $\mathfrak{gl}_N$ source. Rigid up to $c\in\C^\times$
    rescaling.
  - W22-T1 (one-loop chain-level QME vanishing on super-balanced
    $\mathfrak{gl}(N|N)$). One-loop is structural; (A5) not used.
  - W3-W15-04 residue identity (residue of unreduced QME $=
    \hbar N[\bar c]$).
  - P4-G2-M1 module λ-bracket on $\widehat M_0$.
  - G5 / G5-M2 negative closure of unreduced/reduced primitive
    routes (negative results require only the existing apparatus).

* **Conditional under (A1)–(A4) only (becomes unconditional under
  (A1)–(A5) with (A2$'$)):**
  - W22-T2 (all-loop chain-level QME vanishing on
    $\mathfrak{gl}(N|N)$). Was conditional on "regulator preserves
    $\Z/2$"; (A5) discharges this at the operator level, but
    *requires* (A2$'$) at the form-existence level.
  - P4-G3-T-A1 (osp(2N|2N) chain-level vanishing). Same.
  - P4-G3-M2 (M1) psl(N|N) via lift — discharges *only via
    lift to $\mathfrak{gl}(N|N)$* under (A1)–(A5); native discharge
    requires (A2$'$) which fails on psl alone (degenerate Killing).
  - P4-G3-M2 (M3) q(N) — discharges at ordinary-supertrace layer
    under (A1)–(A5); the queer-trace parallel structure is
    independent.
  - Joint Theorem F$''$ on $\mathfrak{gl}(N|N)\otimes\C[z_1,z_2]$
    — transversality verified, hypotheses reduce to G2-M1+G2-M2
    + P4-G3-T-A1 plus (A1)–(A5).

* **Conditional and remaining conditional (Phase-5 frontier):**
  - F$'$ on bosonic $\mathfrak{gl}_N$ source — closed in the
    negative under W18-C3 unreduced primitive (G5) and under
    G5-M2 reduced primitive catalog. Genuine cohomological
    obstruction.
  - W3-W31-T2 topological-twist limit (CGW conjecture).
  - G4-M2 Heisenberg sub-VOA toy twist — **partial** discharge.

**Identified silent strengthening.** Two:
1. **(A2$'$) existence of even non-degenerate ad-invariant
   supersymmetric bilinear form**, used in W22-L2 / P4-G3-T-A1 /
   P4-G3-M2-(M3) but not declared in
   `defn:regulator-admissible-sector` (A1)–(A5). Bilinear-form-level
   refinement of (A5) in W30-W3-W30-03 is closer but still requires
   *existence* implicitly — the precise "$g(PX,PY)=g(X,Y)$"
   condition presupposes that $g$ exists as a non-degenerate even
   supersymmetric ad-invariant form. **§1.6 below.**
2. **Costello regulator-class admissibility on graded sources**
   (the Costello 2011 framework is stated for ungraded BV theories;
   the manuscript implicitly assumes the Costello apparatus extends
   to $\Z/2$-graded sources, and (A5) makes this extension precise
   *within* the manuscript's framework but does not certify external
   compatibility with Costello 2011 Ch 4 §4.4). **§1.7 below.**

**Identified circular dependencies.** **None at the load-bearing
layer.** A potential circularity at the structural sharpening
layer is identified between W30 ((A5) heal) and W3-W8-01
(regulator-class canonicity sharpening): W30's (A5) is verified
on three regulators by W3-W30-02, but the verification *uses*
the regulator-class canonicity established by W3-W8-01 to argue
that the verification on three named regulators extends to the
admissible class. This is **not strictly circular** because
W3-W8-01 itself does not require (A5); (A5) sharpens W3-W8-01
on graded sources. The dependency direction is W3-W8-01 ⊢
W3-W30-02 (verification on three regulators by W3-W8-01 logic)
⊢ (A5) extends to admissible class. **No circular dependency.**

**Bottom line.** The publication-grade inheritance graph is
**logically clean** at the load-bearing layer: (A1)–(A5) plus
(A2$'$) form a non-circular hypothesis set. The principal
obligation for inscription is to **declare (A2$'$) explicitly**
in `defn:regulator-admissible-sector` as a precondition to (A5),
and to **declare the Costello-class compatibility** as a
side-bar remark (§1.7). The weakest sufficient combination for
Theorem G chain-level closure is precisely (A1)–(A4) on the
bosonic source for the *non-vanishing* class, plus (A1)–(A5)
+(A2$'$) on the super-balanced super-Lie sources for the
*vanishing-coupling* discharge.

---

## §1. Per-hypothesis ledger

### §1.1 (A1) — Truncation discipline (degreewise surjective transitions)

**(L1) Precise statement.** The transition maps in the coefficient
and local-functional directions are the truncations to degrees
$d\leq w_0$, or the induced restriction obtained by setting
higher-degree coefficient fields to zero. They are degreewise
surjective maps of complexes.

**(L2) Where introduced.**
`tate-T1-weighted-completion.tex`:606–610 (`defn:regulator-admissible-sector`
clause (A1)). External anchor: Costello 2011 Ch 4 §4.4 (the
regulator class is parameterized by a finite-degree truncation
filtration); Costello-Gwilliam Vol II §11 (factorization
regulator).

**(L3) Where invoked.**
- W22-T1 (one-loop chain-level lift): (A1) ensures the truncation
  $\mathcal E_w^{w_0}\to\mathcal E_w$ is degreewise surjective so
  the inverse-limit is exact in the admissible envelope.
- W22-T2 (all-loop): (A1) governs the regulator-class boundary at
  every $\hbar$-order.
- W3-W15-03 (chain-level lift $\Lambda$ strict): (A1) is implicit
  in the "no homotopy correction" claim because Mittag-Leffler
  (A1) gives $\varprojlim^1 = 0$ on the truncation tower.
- W3-W15-04 (residue identity): (A1) governs the per-window
  representative.
- P4-G3-T-A1, P4-G3-M2: (A1) inherited verbatim from W22.
- P4-G2-M1 module λ-bracket: (A1) controls the m-adic
  completion's filtration discipline (identical mathematical
  content, applied to $\mathfrak m=(z_1)\subset\widehat\C[z_1,z_2]$
  rather than to polynomial-degree filtration on $\bar A$).

**(L4) Where discharged.** **Always assumed; never independently
proved.** (A1) is a *definition* of the admissible class, not a
theorem. Its content is "we work inside this class"; admissibility
within the class is a hypothesis, not a derivation.

**(L5) Cross-dependency.**
- *Depends on:* nothing internal; external compatibility with
  Costello 2011 framework.
- *Strengthens:* W3-W6-04 (regulator-class canonicity), W3-W8-01
  (Polyakov scheme-independence).
- *Weakens:* nothing.

**(L6) Theorem G transitive closure status.** Under (A1) alone
(without (A2)–(A5)):
- (a) chain-level proved? **YES** for the bosonic source — the
  Theorem G class $[\bar c]$ is constructed from
  `lem:omega-cocycle` which uses only Lie-algebra cohomology of
  $\bar A$ (no regulator class).
- (b) cohomologically forced non-trivial? **YES** —
  `lem:omega-cocycle` proof at `main.tex`:307–315 is purely
  Lie-algebraic.
- (c) conditional on named external hypothesis? **NO at the
  bosonic level.**

**(L7) Silent strengthening?** None. (A1) is the cleanest of the
five.

**(L8) Circular dependency?** None.

**(L9) Graph entry.**
- **Node:** (A1) Truncation.
- **Edges:**
  - introduces: `defn:regulator-admissible-sector`
  - invokes ⊃ {W22-T1, W22-T2, W3-W15-03, W3-W15-04, P4-G3-T-A1,
    P4-G3-M2, P4-G2-M1, joint F$''$, G4-M2}
  - discharges: ∅
  - weakens: ∅
  - strengthens: {W3-W6-04, W3-W8-01}
  - requires: external Costello 2011 framework

---

### §1.2 (A2) — Vertexwise polynomial-degree-bounded legs

**(L1) Precise statement.** At each fixed $\hbar$-order and for
each fixed Costello graph, the coefficient expression uses only
vertexwise polynomial-degree-bounded Hamiltonian and cotangent
legs.

**(L2) Where introduced.**
`tate-T1-weighted-completion.tex`:611–613.

**(L3) Where invoked.**
- W22-T1 (one-loop): (A2) ensures the gauge-generator tadpole
  has finitely many polynomial-bounded legs at each $\hbar$-order.
- W22-T2 (all-loop): (A2) controls Costello graph contractions
  at every loop order. **Load-bearing for the combinatorial
  reduction Lemma W22-L3.**
- P4-G3-T-A1, P4-G3-M2: (A2) inherited.
- W3-W15-03, W3-W15-04: (A2) governs the per-window representative
  of $\Lambda$.
- G2-M1, joint F$''$: (A2) inherited.

**(L4) Where discharged.** **Always assumed.** Like (A1), this
is a class definition.

**(L5) Cross-dependency.**
- *Depends on:* nothing internal.
- *Strengthens:* W22-L3 combinatorial reduction (the $\ell$-loop
  diagram contracts to product of $\Str(I^{k_i})$ factors).
- *Weakens:* nothing.

**(L6) Theorem G transitive closure status.** (A2) is required
for the *all-loop* W22-T2 / P4-G3-T-A1 statements but **not** for
the bosonic Theorem G itself — Theorem G is a Lie-algebra cocycle
identity, independent of Costello-graph order.

**(L7) Silent strengthening?** Recall **(A2$'$):** existence of
even non-degenerate ad-invariant supersymmetric bilinear form on
the matrix source. This is *not* declared in (A2) but is
required by W22-L1's super-Berezin loop contraction
(`(A2)` controls polynomial-degree-bounded legs; the *existence*
of the dual basis $\{T_a\}$ on $\mathfrak{g}$ is a separate
condition, not implied by (A2)). **§1.6 below.**

**(L8) Circular dependency?** None.

**(L9) Graph entry.**
- **Node:** (A2) Polynomial-degree-bounded legs.
- **Edges:**
  - introduces: `defn:regulator-admissible-sector`
  - invokes ⊃ {W22-T1, W22-T2, W3-W15-03, W3-W15-04, P4-G3-T-A1,
    P4-G3-M2, P4-G2-M1, joint F$''$}
  - discharges: ∅
  - weakens: ∅
  - strengthens: {W22-L3 combinatorial reduction}
  - requires: (A2$'$) for graded-source applications

---

### §1.3 (A3) — Diagonal weight-rescaling

**(L1) Precise statement.** If $w,w'$ are two degree weights
satisfying `defn:wt-degree-weight`, the diagonal finite-window
rescaling $R_{w,w'}^{w_0}$ transports the interaction,
differential, bracket, propagator contraction, and counterterm
representative from the $w$-window to the $w'$-window.

**(L2) Where introduced.**
`tate-T1-weighted-completion.tex`:614–625.

**(L3) Where invoked.**
- `thm:wt-regulator-independence-admissible` (T1:634): primary
  consumer. This theorem is the one that gives weight-independence
  inside the admissible class.
- W22-T1, W22-T2, W3-W15-04: (A3) controls cross-weight
  comparison of QME residue.
- P4-G3-T-A1, P4-G3-M2: inherited.
- W3-W8-01 / M-45 (regulator-class canonicity): (A3) is the
  load-bearing hypothesis.

**(L4) Where discharged.** **Always assumed.** (A3) is the
definition of "admissible weights generate isomorphic finite-window
theories."

**(L5) Cross-dependency.**
- *Depends on:* `defn:wt-degree-weight` (which is a separate
  internal definition).
- *Strengthens:* W3-W8-01 / M-45 (Polyakov regulator-class
  canonicity); `thm:wt-regulator-independence-admissible`.
- *Weakens:* nothing.

**(L6) Theorem G transitive closure status.** (A3) is needed for
the *regulator-independence* of the residue identity W3-W15-04;
without (A3), the residue might depend on weight choice. But the
*existence* of the residue is independent of (A3).

**(L7) Silent strengthening?** None at the (A3) layer.

**(L8) Circular dependency?** None.

**(L9) Graph entry.**
- **Node:** (A3) Diagonal weight-rescaling.
- **Edges:**
  - introduces: `defn:regulator-admissible-sector`
  - invokes ⊃ {`thm:wt-regulator-independence-admissible`, W22-T1,
    W22-T2, W3-W15-04, P4-G3-T-A1, P4-G3-M2, W3-W8-01}
  - discharges: ∅
  - weakens: ∅
  - strengthens: {W3-W8-01, `thm:wt-regulator-independence-admissible`}
  - requires: `defn:wt-degree-weight`

---

### §1.4 (A4) — Admissible filtered cohomology

**(L1) Precise statement.** The cohomology being computed is the
admissible filtered cohomology detected on finite quotients and
associated graded pieces in the envelope of
`stmt:tate-model-envelope`; no observable is allowed to detect an
infinite product tail invisible in every finite quotient.

**(L2) Where introduced.**
`tate-T1-weighted-completion.tex`:626–631.

**(L3) Where invoked.**
- `thm:wt-regulator-independence-admissible`(iii): "vanishing
  or nonvanishing of the mixed brane-defect QME obstruction is
  independent of the admissible weight" — under (A4), this is
  computed on finite quotients.
- W22-T1, W22-T2: (A4) ensures the Berezinian product
  $\prod_{k\geq 1}(1-q^k)^{-(N-M)}$ vanishes on every finite
  quotient at $N=M$ (W3-W25-05 partition-function check).
- W3-W15-04 (residue): (A4) ensures the residue is detected on
  finite quotients (Mittag-Leffler envelope).
- W3-W30-02 (regulator verification): (A4) is implicit in the
  finite-window decomposition $H=H^{\rm ev}\oplus H^{\rm odd}$.
- P4-G3-T-A1, P4-G3-M2: inherited.

**(L4) Where discharged.** **Always assumed.** (A4) is the
class definition.

**(L5) Cross-dependency.**
- *Depends on:* `stmt:tate-model-envelope` (Tate-model
  envelope statement, which is itself a structural hypothesis).
- *Strengthens:* `thm:strict-unweighted-no-go` (the strict
  unweighted product/direct-sum pair fails (A4)).
- *Weakens:* nothing.

**(L6) Theorem G transitive closure status.** (A4) is required
for the *finiteness-detectability* of the residue. Without (A4),
the residue might be a "tail-only" class invisible on finite
windows.

**(L7) Silent strengthening?** None at the (A4) layer.

**(L8) Circular dependency?** None.

**(L9) Graph entry.**
- **Node:** (A4) Admissible filtered cohomology.
- **Edges:**
  - introduces: `defn:regulator-admissible-sector`
  - invokes ⊃ {`thm:wt-regulator-independence-admissible`, W22-T1,
    W22-T2, W3-W15-04, P4-G3-T-A1, P4-G3-M2, W3-W30-02}
  - discharges: ∅
  - weakens: nothing
  - strengthens: {`thm:strict-unweighted-no-go`}
  - requires: `stmt:tate-model-envelope`

---

### §1.5 (A5) — Parity-equivariance on graded sources (proposed; not yet inscribed)

**(L1) Precise statement (W30 final form).** Let
$P=\diag(\mathbf 1_N,-\mathbf 1_M)$ be the parity operator on
$\mathfrak{gl}(N|M)$. The BV bilinear form $g$ defining the BV
pairing is parity-equivariant: $g(PX,PY)=g(X,Y)$ for all
$X,Y\in\mathfrak{gl}(N|M)$. The associated regulator data —
the heat operator $K_t$, the gauge-fixing $Q^{\GF}$, and the
regularized BV propagator
$P_{\epsilon,L}=Q^{\GF}\int_\epsilon^L K_t\,dt$ — commute with $P$
at the operator level: $[K_t,P]=[Q^{\GF},P]=[P_{\epsilon,L},P]=0$.
On a parity-trivial (purely bosonic) source, (A5) is vacuous:
$P=\mathbf 1$ and every operator trivially commutes with the
identity.

**(L2) Where introduced.** *Not yet inscribed in the manuscript.*
Proposed insertion at `tate-T1-weighted-completion.tex`:631
(immediately before `\end{enumerate}` closing the (A1)–(A4) list).
Source: W30-W3-W30-01 / WP3-W30-1.

**(L3) Where invoked.**
- W22-T2 (all-loop): (A5) is the load-bearing precondition for
  the unconditional all-loop discharge.
- P4-G3-T-A1 (osp(2N|2N)): (A5) verbatim.
- P4-G3-M2 (M1) psl(N|N): (A5) inherited via lift to
  $\mathfrak{gl}(N|N)$.
- P4-G3-M2 (M3) q(N): (A5) verbatim at ordinary-supertrace layer.
- W3-W30-02 (regulator verification): heat-kernel from
  super-Killing, Pauli-Villars, Hadamard parametrix all satisfy.
- Joint F$''$ (P4-EXEC-G2-G3-RELAUNCH-3): (A5) preserved by
  Symp$_{\rm form}$ trivially (transversality lemma).

**(L4) Where discharged.**
- **(A5) on heat-kernel from super-Killing form:** discharged in
  W3-W30-02(a). Direct computation $[\Delta_{\rm sK},P]=0$.
  **Confidence high.**
- **(A5) on Pauli-Villars:** discharged in W3-W30-02(b). Sector-
  pure argument with parity-correct mass assignments.
  **Confidence high.**
- **(A5) on Hadamard parametrix:** discharged in W3-W30-02(c).
  Block-diagonal $H=H^{\rm ev}\oplus H^{\rm odd}$.
  **Confidence high.**
- **(A5) on counterexamples:** verified to break in W3-W30-03
  (mixed propagator (a); ungraded heat-kernel (c)).

**(L5) Cross-dependency.**
- *Depends on:* (A2$'$) implicitly (the bilinear form $g$ must
  exist as a non-degenerate even ad-invariant supersymmetric form
  before "g(PX,PY)=g(X,Y)" can be required); also depends on
  Cheng-Wang 2012 / Kac 1977 classification of which super-Lie
  algebras have even non-degenerate forms.
- *Strengthens:* W22-T2 from conditional to unconditional;
  W3-W8-01 on graded sources; P4-G3-T-A1, P4-G3-M2 (M1, M3).
- *Weakens:* W22-T2's previous conditional clause.

**(L6) Theorem G transitive closure status.** (A5) is **vacuous**
on bosonic Theorem G. (A5) is **load-bearing** on the
super-balanced source where Theorem G's coupling becomes
$\hbar\Str(I)=0$. Without (A5), the all-loop super-balanced
W22-T2 + P4-G3-T-A1 are conditional; with (A5), they are
unconditional.

**(L7) Silent strengthening?** **YES — (A2$'$) is silently
required by (A5).** See §1.6.

**(L8) Circular dependency?** Discussed in §0; no strict
circularity.

**(L9) Graph entry.**
- **Node:** (A5) Parity-equivariance.
- **Edges:**
  - introduces (proposed): `defn:regulator-admissible-sector`
    (after (A4))
  - invokes ⊃ {W22-T2, P4-G3-T-A1, P4-G3-M2 (M1 lift, M3),
    W3-W30-02, joint F$''$}
  - discharges: {W22-T2 conditional clause; P4-G3-T-A1 conditional
    clause; P4-G3-M2 (M1, M3) conditional}
  - weakens: ∅
  - strengthens: {W3-W8-01 on graded sources}
  - requires: (A2$'$) (implicit)

---

### §1.6 (A2$'$) — Existence of even non-degenerate ad-invariant supersymmetric bilinear form (silent)

**(L1) Precise statement.** *Whenever the open matrix source is a
$\Z/2$-graded super-Lie algebra $\mathfrak g$, there exists an
even non-degenerate ad-invariant supersymmetric bilinear form
$g:\mathfrak g\otimes\mathfrak g\to\C$ used to construct the BV
pairing.* "Even" means $g$ has parity 0 (pairs even-even and
odd-odd, vanishes on mixed-parity); "supersymmetric" means
$g(X,Y)=(-1)^{|X||Y|}g(Y,X)$; "ad-invariant" means
$g([Z,X],Y)+(-1)^{|Z||X|}g(X,[Z,Y])=0$.

**(L2) Where introduced.** *Not declared explicitly anywhere in
the manuscript or in the W30 (A5) inscription.* It is presupposed
by:
- W22-L1 super-Berezin loop contraction (uses $(-1)^{|a|\cdot|b|}\delta^a_d\delta^c_b$
  super-pairing, which presupposes the dual basis under an even
  non-degenerate $g$).
- W22-L2 chain-level lift (presupposes the dual basis exists).
- W3-W30-02(a) heat-kernel construction $\Delta_{\rm sK}=\sum_a
  (-1)^{|a|}T^aT_a$ (presupposes $\{T_a\}$ as dual basis).

External anchors: Kac 1977 *Lie superalgebras* §1.1.4 (basic
classical classification); Cheng-Wang 2012 Prop. 1.34 (Killing
form vanishing on $\mathfrak{psl}(N|N)$ and $\mathfrak{p}(N)$);
Sergeev 1984 (queer non-degenerate even form
$B_0(X,Y)=\Tr(\ev XY+\ev YX)/2$).

**(L3) Where invoked.**
- W22-L1, W22-L2 (verbatim — the loop contraction *requires* an
  even dual basis).
- P4-G3-T-A1: verified to hold on $\mathfrak{osp}(2N|2N)$ (basic
  classical, super-Killing non-degenerate).
- P4-G3-M2 (M1) psl(N|N): **fails natively** (Killing form
  identically zero); discharge requires lift to $\mathfrak{gl}(N|N)$
  where the form exists. (A2$'$) is the structural reason for the
  lift requirement.
- P4-G3-M2 (M2) p(N): **structurally fails** (no even non-degenerate
  ad-invariant supersymmetric form exists for $N\geq 2$, only an
  odd symmetric form; Cheng-Wang 2012 §1.1.5). This is the **unique
  obstruction** identified in P4-G3-M2 — periplectic *fails*
  (A2$'$) intrinsically.
- P4-G3-M2 (M3) q(N): satisfied via the alternative even form
  $B_0(X,Y)=\Tr(\ev XY+\ev YX)/2$ (not the Killing form).
- P4-G3-M2 (M4) sl(M|N) for M≠N: satisfied (basic classical,
  Killing non-degenerate); fails on $\Str(I)\neq 0$ instead.

**(L4) Where discharged.**
- **(A2$'$) on $\mathfrak{gl}(N|N)$:** discharged tautologically
  (defining-rep supertrace $B_0(X,Y)=\Str(XY)$ is non-degenerate
  on the supertraceless quotient).
- **(A2$'$) on $\mathfrak{osp}(2N|2N)$:** discharged by Kac 1977
  §1.1.4 (basic classical, super-Killing non-degenerate).
- **(A2$'$) on $\mathfrak{q}(N)$ for $N\geq 2$:** discharged by
  Sergeev 1984 / Cheng-Wang 2012 Prop. 1.36 (alternative even form
  $B_0$ non-degenerate).
- **(A2$'$) on $\mathfrak{psl}(N|N)$:** **fails natively**;
  discharged via lift to $\mathfrak{gl}(N|N)$.
- **(A2$'$) on $\mathfrak{p}(N)$:** **fails outright**. Cheng-Wang
  2012 Prop. 1.34 + the "no even invariant form" structural
  obstruction.

**(L5) Cross-dependency.**
- *Depends on:* Kac 1977 / Cheng-Wang 2012 / Sergeev 1984 (basic
  classical classification + alternative form structure).
- *Strengthens:* the W22-L1/L2 derivation; the (A5) precondition.
- *Weakens:* the *naive* universality of W22-T2 across all
  super-Lie sources (P4-G3-M2 shows p(N) breaks).

**(L6) Theorem G transitive closure status.** (A2$'$) is
**vacuous** on bosonic Theorem G. (A2$'$) is the **structural
gate** for super-balanced extensions: gl(N|N), osp(2N|2N), q(N)
pass; psl(N|N) passes only via lift; p(N) fails outright.

**(L7) Silent strengthening?** **(A2$'$) is itself the silent
strengthening identified in §0.** Recommended inscription: add
to `defn:regulator-admissible-sector` as a precondition to (A5).

**(L8) Circular dependency?** None.

**(L9) Graph entry.**
- **Node:** (A2$'$) Existence of even non-degenerate ad-invariant
  supersymmetric form (silent).
- **Edges:**
  - introduces (proposed): precondition to (A5)
  - invokes ⊃ {W22-L1, W22-L2, P4-G3-T-A1, P4-G3-M2 (M1, M3),
    W3-W30-02(a)}
  - discharges (case-by-case): {gl(N|N), osp(2N|2N), q(N) pass;
    psl(N|N) via lift; p(N) FAILS; sl(M|N) M≠N passes (different
    failure)}
  - weakens: universality of (A5) across all super-Lie sources
  - strengthens: ∅
  - requires: Kac 1977, Cheng-Wang 2012

---

### §1.7 Costello regulator-class compatibility (silent meta-hypothesis)

**(L1) Precise statement.** *The Costello 2011 regulator
formalism (heat-kernel parametrix, Pauli-Villars, Hadamard) on
ungraded BV theories extends, mutatis mutandis, to $\Z/2$-graded
sources via the parity-equivariant supertrace replacement of W22.*

**(L2) Where introduced.** Not declared anywhere. It is implicit
in:
- W3-W6-04 / M-45 regulator-class canonicity inside the admissible
  class.
- W3-W8-01 Polyakov scheme-independence on ungraded
  $\mathfrak{gl}_N$, extended (silently) to graded
  $\mathfrak{gl}(N|M)$ in W22-T2.
- W3-W30-02 regulator verification on three named regulator
  schemes.

External anchors: Costello 2011 *Renormalization* §5.2 (graded
case mentioned); Costello-Gwilliam Vol II §11; Faddeev 1980
*Methods of Path Integration* on super-Lie algebras (graded PV).

**(L3) Where invoked.** All super-balanced theorems (W22-T1, T2;
P4-G3-T-A1; P4-G3-M2 except for the failure cases).

**(L4) Where discharged.** Discharged informally in W3-W30-02 by
construction-on-three-regulators: heat-kernel from super-Killing,
Pauli-Villars on graded source, Hadamard parametrix. **Not formally
verified against Costello 2011 §5.2 graded-case statement.**

**(L5) Cross-dependency.**
- *Depends on:* Costello 2011 framework + graded-extension
  consistency.
- *Strengthens:* (A5) verification on three regulators.
- *Weakens:* if Costello 2011's graded-case framework has
  hypotheses not declared in the manuscript, those hypotheses are
  silently strengthened.

**(L6) Theorem G transitive closure status.** Vacuous on
bosonic Theorem G. Important for super-balanced extensions.

**(L7) Silent strengthening?** **YES** — second silent
strengthening identified in §0. Recommended remark inscription:
acknowledge that the manuscript's regulator class is the
*intersection* of Costello 2011 admissible regulators with
$\Z/2$-graded extensions thereof; this intersection is non-empty
(verified on three named schemes) but its precise characterization
in Costello 2011 vocabulary is informally inherited.

**(L8) Circular dependency?** None.

**(L9) Graph entry.**
- **Node:** Costello-class compatibility (meta-hypothesis).
- **Edges:**
  - introduces: silent (manuscript-wide presupposition)
  - invokes ⊃ {W22-T1, W22-T2, P4-G3-T-A1, P4-G3-M2, W3-W30-02}
  - discharges (informally): {three named regulators verified}
  - weakens: ∅
  - strengthens: ∅
  - requires: Costello 2011 §5.2; CG Vol II §11.

---

## §2. Cross-milestone inheritance graph

Notation: `→` denotes "depends on"; `⊢` denotes "discharges
under"; `∥` denotes "is parallel/independent".

```
              Costello 2011 + CG Vol II §11      Kac 1977 + Cheng-Wang 2012
                       │                                    │
                       ▼                                    ▼
            ┌──────────────────────┐               ┌────────────────────┐
            │ (A1) Truncation      │               │ (A2') Existence   │
            │ (A2) Polyn-deg-bnd   │               │ of even non-deg    │
            │ (A3) Wt-rescale     │               │ ad-inv super-      │
            │ (A4) Adm-fil-cohom   │               │ symm bilin form    │
            └──────────┬───────────┘               └─────────┬──────────┘
                       │                                     │
                       ▼                                     ▼
                                ┌──────────────────────┐
                                │ (A5) Parity-equiv    │
                                │ (proposed; W30)      │
                                └──────────┬───────────┘
                                           │
            ┌──────────────────────────────┼──────────────────────────────┐
            │                              │                              │
            ▼                              ▼                              ▼
  ╔═════════════════════╗      ╔═══════════════════════╗      ╔════════════════════════╗
  ║ Theorem G            ║      ║ W22-T1 (one-loop      ║      ║ W22-T2 (all-loop      ║
  ║ (`thm:u1-center-     ║      ║ chain-level QME       ║      ║ chain-level QME on    ║
  ║  anomaly`,           ║      ║ vanishing on          ║      ║ super-balanced gl(N|N))║
  ║ `lem:omega-cocycle`) ║      ║ super-balanced       ║      ║                       ║
  ║ on bosonic gl_N      ║      ║ gl(N|N))             ║      ║ ⊢ under (A1)–(A5)+(A2')║
  ║ ⊢ under (A1)–(A4)    ║      ║ ⊢ under (A1)–(A4)+   ║      ║                       ║
  ║                      ║      ║ (one-loop is         ║      ║                       ║
  ║ Class non-trivial    ║      ║ structural; no (A5)) ║      ║                       ║
  ║ (G5-M2 catalog)      ║      ║                      ║      ║                       ║
  ╚══════════╤═══════════╝      ╚═══════════╤═══════════╝      ╚═══════════╤════════════╝
             │                              │                              │
             │ ∥                            │                              │
             ▼                              ▼                              ▼
  ┌─────────────────────┐      ┌────────────────────────┐     ┌────────────────────────┐
  │ W3-W15-04 residue   │      │ W3-W15-03 chain-level  │     │ P4-G3-T-A1            │
  │ identity            │      │ lift Λ strict          │     │ (osp(2N|2N))          │
  │ residue=ℏN[c]       │ →    │                        │     │ ⊢ under (A1)–(A5)+    │
  │ ⊢ under (A1)–(A4)   │      │ ⊢ under (A1)–(A4)      │     │ (A2')                 │
  └─────────────────────┘      └────────────────────────┘     └──────────┬─────────────┘
             │                              │                              │
             │                              │                              │
             ▼                              ▼                              ▼
  ┌─────────────────────┐                                       ┌──────────────────────┐
  │ G5 / G5-M2          │                                       │ P4-G3-M2 catalog    │
  │ neg primitive       │                                       │                     │
  │ catalog             │                                       │ M1: psl(N|N) via   │
  │                     │                                       │     lift ⊢ (A1)-(A5)│
  │ ⊢ under (A1)–(A4)   │                                       │ M2: p(N) FAILS    │
  │ confirms G's class  │                                       │     (A2') breaks  │
  │ non-trivial         │                                       │ M3: q(N) ⊢       │
  └─────────────────────┘                                       │ M4: sl(M|N) M≠N   │
                                                                │     FAILS Str(I)≠0│
                                                                └──────────────────────┘

                                  ┌─────────────────────────────┐
                                  │ Joint Theorem F''           │
                                  │ on gl(N|N)⊗C[z_1,z_2]       │
                                  │ ⊢ under (A1)–(A5)+(A2') +  │
                                  │   G2-M1 + G2-M2 + P4-G3-T-A1│
                                  │ + transversality verified   │
                                  └─────────────────────────────┘

   ╔═══════════════════════════════════════════════════════════════════════╗
   ║ FRONTIER (still conditional or partial)                              ║
   ║                                                                      ║
   ║ • F' on bosonic gl_N (genuine cohomological obstruction; G5/G5-M2)   ║
   ║ • W3-W31-T2 topological-twist limit (CGW conjecture)                 ║
   ║ • G4-M2 Heisenberg sub-VOA toy twist (PARTIAL)                       ║
   ║ • R-W3-W22-A BCOV embedding of super-balanced source (Phase-4)       ║
   ║ • R-W3-W26-A Symp_form-natural realization in PVA (Phase-4)          ║
   ╚═══════════════════════════════════════════════════════════════════════╝
```

**Interpretation.** Every super-balanced super-Lie discharge milestone
depends on the chain (A1)–(A5)+(A2$'$). The bosonic Theorem G is
parallel and independent of (A5)+(A2$'$). The negative primitive
catalogs (G5 unreduced, G5-M2 reduced) confirm that the class
$[\bar c]$ on $\bar A$ is *not* discharged by any chain-level
primitive — it is genuinely cohomologically non-trivial.

---

## §3. Theorem G chain-level closure status under the weakest sufficient hypothesis combination

**Theorem G, bosonic side (`thm:u1-center-anomaly`,
`thm:u1-center-anomaly-open`).** Under (A1)–(A4) only:
- (a) **Chain-level proved:** `lem:omega-cocycle` proof
  (`main.tex`:292–315) is purely Lie-algebraic on
  $\mathfrak h_{\rm poly}=\C[z_1,z_2]$; no regulator class enters.
- (b) **Cohomologically forced non-trivial:** by `lem:omega-cocycle`
  proof contradiction at $\omega(z_1,z_2)=1$; reinforced by G5
  unreduced-primitive negative closure and G5-M2 reduced-primitive
  catalog negative closure.
- (c) **Conditional on named external hypothesis:** **NO** —
  Theorem G stands unconditionally under (A1)–(A4).

**Theorem G chain-level open-side equality (`thm:quantum-classical-anomaly`).**
Under (A1)–(A4) plus the Capelli renormalization on the trace
generators (`lem:capelli-renormalized-stable-trace`): chain-level
proved; cohomologically forced; not conditional.

**W3-W15-04 residue identity (residue $=\hbar N[\bar c]$).**
Under (A1)–(A4): chain-level identity holds modulo the regulator;
the residue equals $\hbar N[\bar c]$ inside the admissible class.
Outside the admissible class, not asserted.

**W22-T1 + W22-T2 + P4-G3-T-A1 (super-balanced super-Lie discharge
of the *coupling*).** Under (A1)–(A5)+(A2$'$): the coupling
coefficient $\hbar\Str(I)$ vanishes on every super-balanced source
satisfying (A2$'$) (gl(N|N), osp(2N|2N), q(N) at the ordinary-
supertrace layer; psl(N|N) via lift). Theorem G's *class* $[\bar c]$
is unchanged; only the *coupling* is forced to zero. **The
chain-level QME holds at zero residue on these sources.**

**Weakest sufficient hypothesis combination summary.**
- *For Theorem G's bosonic chain-level non-trivial residue:* (A1)–(A4)
  alone. **Already inscribed.**
- *For Theorem G's super-balanced vanishing (W22-T2, P4-G3-T-A1
  classes):* (A1)–(A5)+(A2$'$). (A5) currently proposed via W30;
  (A2$'$) currently silent.
- *For Theorem G's class identification with the QME residue
  (W3-W6-05 / W3-W15-03 / W3-W15-04):* (A1)–(A4) alone. The lift
  $\Lambda$ is strict (no homotopies); the regulator-class
  canonicity is governed by (A1)–(A4) plus
  `thm:wt-regulator-independence-admissible`.

---

## §4. Recommendations for inscription

In order of inscription priority:

### Priority 1 — Inscribe (A5) at `tate-T1-weighted-completion.tex`:631

Per W30-WP3-W30-1. The exact LaTeX is in W30 §3 Tier-0:

```latex
    \item\label{itm:A5-parity-equivariance}
      \emph{Parity-equivariance on graded sources.}
      When the open matrix source carries a $\Z/2$-grading, with
      parity operator $P=\diag(\mathbf 1_N,-\mathbf 1_M)$ on
      $\lie{gl}(N|M)$, the bilinear form $g$ defining the BV
      pairing is parity-equivariant:
      \[
        g(PX,PY)=g(X,Y)
        \quad\text{for all }X,Y\in\lie{gl}(N|M),
      \]
      and the regularization data — the heat operator $K_t$, the
      gauge-fixing $Q^{\GF}$, and the regularized propagator
      $P_{\epsilon,L}=Q^{\GF}\int_\epsilon^L K_t\,dt$ — commute
      with $P$ at the operator level: $[K_t,P]=[Q^{\GF},P]=
      [P_{\epsilon,L},P]=0$.
      On a parity-trivial (purely bosonic) source, this condition
      is vacuous: $P=\mathbf 1$ and every operator trivially
      commutes with the identity. The heat-kernel constructed
      from the super-Killing form, Pauli--Villars on a graded
      source with parity-correct auxiliary assignments, and the
      Hadamard parametrix all satisfy this condition by
      construction.
```

### Priority 2 — Declare (A2$'$) as a precondition to (A5)

**Recommended new inscription** at
`tate-T1-weighted-completion.tex`:631, immediately *before* (A5):

```latex
    \item\label{itm:A2-prime-form-existence}
      \emph{Existence of an even non-degenerate ad-invariant
      supersymmetric bilinear form on graded sources.}  When the
      open matrix source is a $\Z/2$-graded super-Lie algebra
      $\mathfrak g$, there exists an even non-degenerate
      ad-invariant supersymmetric bilinear form
      $g:\mathfrak g\otimes\mathfrak g\to\C$ used to construct the
      BV pairing.  On a parity-trivial source, $g$ is the
      standard $\Tr$-form on the matrix factor and this condition
      is automatic.  This condition is satisfied on
      $\mathfrak{gl}(N|N)$, $\mathfrak{osp}(2N|2N)$, and
      $\mathfrak q(N)$ (with the Sergeev form
      $B_0(X,Y)=\Tr(\ev XY+\ev YX)/2$); it fails on
      $\mathfrak{p}(N)$ (periplectic preserves only an odd
      symmetric form, with Killing form identically zero) and on
      $\mathfrak{psl}(N|N)$ natively (Killing form identically
      zero; discharge requires lift to $\mathfrak{gl}(N|N)$).
```

This makes the (A2$'$) silent strengthening explicit and
documents the boundary of where the W22 / P4-G3 super-balanced
mechanism applies.

### Priority 3 — Add `rmk:wt-regulator-parity-equivariance`

Per W30-WP3-W30-2 at `tate-T1-weighted-completion.tex`:706 (after
`thm:wt-regulator-independence-admissible`).

### Priority 4 — Inscribe W22-T1, W22-T2, P4-G3-T-A1 candidate theorems

In `appendix-unreduced-bv-qme.tex` after
`rmk:app-scalar-contact-escape-routes` (line 179), per
W22-WP3-W22-1, W22-WP3-W22-2, P4-G3-T-A1-WP4-G3-T-A1-1.

### Priority 5 — Update `claim-strength-ledger.tex`

Add three rows:
1. *Super-balanced QME chain-level discharge.* Status: *proved
   degreewise stable* (under (A1)–(A5)+(A2$'$)). Scope:
   $\mathfrak{gl}(N|N)$, $\mathfrak{osp}(2N|2N)$, $\mathfrak{q}(N)$
   ordinary-supertrace; $\mathfrak{psl}(N|N)$ via lift. Excluded:
   $\mathfrak{p}(N)$ structurally; $\mathfrak{sl}(M|N)$ for
   $M\neq N$ by construction.
2. *(A5) parity-equivariance hypothesis.* Status: *proved on
   admissible regulators* (heat-kernel from super-Killing,
   Pauli-Villars graded, Hadamard parametrix). Scope: graded
   sources only; vacuous on bosonic.
3. *(A2$'$) form-existence hypothesis.* Status: *proved on
   classical super-Lie families with even non-degenerate forms*
   (Kac 1977, Cheng-Wang 2012). Scope: necessary precondition
   to (A5).

### Priority 6 — Cross-volume cross-link in `principles.tex`

Per W22-WP3-W22-3 / W30-WP3-W30-4 / P4-EXEC-G3-M2 inscription
remark. Names which super-Lie families discharge and which fail
(p(N) periplectic FAILS structurally).

### Priority 7 — Costello-class compatibility remark (optional)

Acknowledges that the manuscript's regulator class is the
*intersection* of Costello 2011 admissible regulators with
$\Z/2$-graded extensions thereof, with formal external
verification deferred to Phase-5.

---

## §5. Residual silent strengthenings or circular dependencies that block convergence

### §5.1 Identified silent strengthenings (non-blocking)

1. **(A2$'$) form-existence** — silent in current manuscript.
   Recommended inscription Priority 2 above.
2. **Costello-class compatibility on graded sources** — silent
   meta-hypothesis. Recommended inscription Priority 7
   (optional remark).

### §5.2 Identified circular dependencies (blocking)

**None at the load-bearing layer.** The W30 ↔ W3-W8-01 loop
discussed in §0 is logically clean because W3-W8-01 provides the
bosonic regulator-class canonicity that W30 *extends* to graded
sources, not vice versa.

### §5.3 Convergence-blocking residuals

**ZERO load-bearing residuals.** After the Priority 1–2
inscriptions above, the (A1)–(A5)+(A2$'$) chain becomes:
- explicitly declared (no silent strengthenings),
- non-circular (all dependencies one-way),
- minimally adequate for W22-T2 / P4-G3-T-A1 / P4-G3-M2 (M1 lift,
  M3) discharges,
- vacuous on bosonic Theorem G (preserving the manuscript's main
  M-13 disambiguation),
- complete in its delineation of where the mechanism applies vs
  fails (P4-G3-M2 boundary at p(N)).

---

## §6. New residuals from this audit

- **R-P4-EXEC-A1-01.** Inscription of (A2$'$) as a separate
  declared hypothesis in `defn:regulator-admissible-sector`.
  Severity 2 (definitional precision); scope: tate-T1.
- **R-P4-EXEC-A1-02.** Costello 2011 §5.2 graded-case
  cross-walk to verify the manuscript's regulator class is
  contained in Costello's framework. Severity 1 (cosmetic /
  external compatibility check); scope: optional remark.
- **R-P4-EXEC-A1-03.** Once (A5) and (A2$'$) are inscribed, the
  claim-strength-ledger needs three rows added (Priority 5
  above). Severity 2 (precision in claim-strength).
- **R-P4-EXEC-A1-04.** The W22-T1, W22-T2, P4-G3-T-A1 candidate
  theorems should be inscribed into
  `appendix-unreduced-bv-qme.tex` as `thm:` blocks. Severity 3
  (load-bearing inscription of theorems). Per Priority 4 above.
- **R-P4-EXEC-A1-05.** A future audit pass should verify that the
  joint Theorem F$''$ (P4-EXEC-G2-G3-RELAUNCH-3) has all hypotheses
  declared after the Priority 1–4 inscriptions are made. Severity
  2 (verification audit).

---

## §7. 200-word summary

(a) **Total (A1)–(A5) variants currently in use: SIX.** Beyond
(A1)–(A4) inscribed and (A5) proposed via W30, one silent variant
(A2$'$) — *existence of even non-degenerate ad-invariant
supersymmetric bilinear form on graded sources* — is required by
W22-L1/L2, P4-G3-T-A1, and P4-G3-M2-(M1, M3). (A2$'$) is the
structural reason periplectic $\mathfrak{p}(N)$ fails outright in
P4-G3-M2-(M2) while $\mathfrak{psl}(N|N)$ requires lift to
$\mathfrak{gl}(N|N)$.

(b) **Weakest sufficient combination for Theorem G chain-level
closure.** *Bosonic side*: (A1)–(A4) alone — already inscribed.
The Theorem G class $[\bar c]$ is non-trivially cohomologically
forced (G5 + G5-M2 negative primitive catalogs confirm).
*Super-balanced super-Lie side*: (A1)–(A5)+(A2$'$) — discharges
the coupling $\hbar\Str(I)\to 0$ on gl(N|N), osp(2N|2N), q(N),
psl(N|N) via lift; fails on p(N), sl(M|N) for M≠N.

(c) **Silent strengthenings identified.** Two: (A2$'$)
form-existence (load-bearing); Costello-class graded compatibility
(meta, optional). No circular dependencies.

(d) **Report path:** `/Users/raeez/topological-strings/reconstitution/phase4-exec-A1-hypothesis-audit-2026-04-28.md`.
**Line count:** 976.

End of P4-EXEC-A1-HYP-AUDIT.
