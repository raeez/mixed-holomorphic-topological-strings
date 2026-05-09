# Phase 4 / G2 — Bi-infinite parent / Z² cones, complementary research outline (R-W3-W26-A)

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Group.** Phase-4 G2 — Bi-infinite parent / Z² cones.
**Specific target.** R-W3-W26-A: $\mathrm{Symp}_{\mathrm{form}}(\C^2, 0)$-natural
realization of the column-Verma decomposition $C^{+-}\big|_{\mathfrak b}
= \bigoplus_{a \geq 0} M_a$ in a chiral / Poisson-vertex /
factorization framework.
**Mode.** Proposal-only. ID prefix `P4-G2-`. Schema = master ledger
(severity, status, confidence, deciding evidence). No commits.
**Posture.** *Complementary* to the W35 research outline
(`wave3-W35-R26A-symp-2026-04-28.md`, 1144 lines). W35 produced:
(i) the precise open question Q-W3-W35-A; (ii) algebra-level PVA
$\mathrm{Symp}_{\mathrm{form}}$-equivariance check on
$\varphi: (z_1, z_2) \mapsto (z_1, z_2 + z_1^2)$; (iii) three attack
paths (A) direct PVA, (B) CGW pull-back, (C) Drinfeld stack; (iv)
draft Phase-4 obligation entry. This G2 outline does **not** restate
those results. Its job is to close five gaps where W35 named the
issue but did not pin it down, and to declare the smallest verifiable
3-month deliverable.

**Cross-references.**
- W35 = `reconstitution/wave3-W35-R26A-symp-2026-04-28.md` (parent;
  cited verbatim).
- W26 = `reconstitution/wave3-W26-column-verma-2026-04-28.md` (column-
  Verma identification; W3-W26-08 is the load-bearing
  $\varphi$-counter-example; W3-W26-T1 the 6-part theorem).
- W21 = `reconstitution/wave3-W21-wakimoto-2026-04-28.md` (Wakimoto
  re-label corrected to "rank-1 unipotent column-Verma of the 3-dim
  solvable Borel").
- W22 = `reconstitution/wave3-W22-supertrace-rigorous-2026-04-28.md`
  (G3-supertrace anchor; super-balanced $\mathfrak{gl}(N|N)$ discharge).
- W31 = `reconstitution/wave3-W31-5dM-obstructions-2026-04-28.md` (CGW
  twist conjecture T2).
- final = `reconstitution/wave3-FINAL-convergence-report-2026-04-28.md`
  (Wave 3 certified converged; G2 lives at Rank 4).

---

## §0. Method and posture

The W35 outline is structurally complete at the level of *naming* the
attack paths. What G2 owes is the next, finer slice:

1. The **module topology** that makes $\sum_k(-1)^kv_{2k,-1-k}$ converge
   was named (W35 §3.6, R-W3-W35-B) but **not pinned**. There are at
   least three concrete candidates (m-adic, Tate inverse-limit,
   factorization / locally constant). Each gives a different category
   of completed modules. G2 §1 picks them out.

2. The **cocycle compatibility** condition in Q-W3-W35-A clause (c)
   was stated as a quantifier over $\mathrm{Symp}_{\mathrm{form}}$ but
   not unfolded. G2 §2 turns it into a finite, verifiable test set
   (group-theoretic reduction).

3. The **Heisenberg PVA candidate** of W35 §2.2 was written down at the
   level of the $\lambda$-bracket on linear generators. The full
   *deformed* Heisenberg PVA carrying the BD chiral central charge
   $[\bar c]$ was hinted at (W35 §2.4) but its OPE was not computed.
   G2 §3 writes it.

4. The **Drinfeld stack pull-back machinery** was named (W35 §6.3,
   path C) but its coordinates and tangent complex were not specified.
   G2 §4 writes a working definition.

5. The **interaction with Phase-4 G3 (supertrace discharge on
   $\mathfrak{gl}(N|N)$)** was not addressed in W35. G2 §5 asks the
   load-bearing question: does the G3 super-balanced discharge of
   `prob:weighted-rg-locality` extend from $\mathrm{GL}_2 \times T^2$
   to all of $\mathrm{Symp}_{\mathrm{form}}$?

The G2 deliverable is a 3-month milestone: the *smallest* result that,
once produced, makes one of the three W35 attack paths concretely
testable on a numerical probe. We argue this is **path (A) at one
explicit non-quadratic test** (the cubic $\varphi: z_2 \mapsto z_2 +
z_1^3$ at the algebra level, on the $\mathfrak m$-adic completion of
$M_0$), with an explicit OPE table.

---

## §1. T1 — What W35 didn't cover (gap inventory)

### §1.1 Gap G1 — Module topology not pinned

**W35 statement (verbatim, §3.6).** "The discharge requires a topology
on the module $M$ in which $\sum_k(-1)^kv_{2k,-1-k}$ is a converging
element of $\widehat M$." W35 named three candidate topologies in
R-W3-W35-B but did not decide between them or write the structure
morphism $\widehat M \to \widehat M$ induced by $\varphi$ in any
chosen topology.

**Why this matters.** Different topologies yield different categories
of completed PVA modules; cocycle compatibility in the $\mathfrak m$-
adic category does not automatically extend to Tate or factorization
categories.

**G2 task.** Pin the topology. The three candidates:

| Topology | Filtration | Convergence test | Category | Candidate strength |
|----------|-----------|------------------|----------|--------------------|
| (i) $\mathfrak m$-adic with $\mathfrak m = (z_1)\subset\widehat\C[z_1,z_2]$ | $\mathfrak m^kM \supset\mathfrak m^{k+1}M$ | each $v_{2k,-1-k}$ has $z_1$-degree $2k$ → $\mathfrak m^{2k}$ | Pro-finite-dim PVA modules | Strongest — converges by Krull |
| (ii) Tate inverse-limit on bidegree $(a,b)$ | $\widehat M = \varprojlim M/M_{\geq N}$ where $M_{\geq N} = \{v_{a,b}: a+b \geq N\}$ | partial sums truncate | Tate $\C((z))$-modules in 2 vars | Mid — needs Tate self-duality |
| (iii) factorization-algebra locally-constant | colimit over open intervals $I\subset\R$ | locally constant in brane line direction | BD chiral category | Weakest — convergence is structural, not numerical |

**P4-G2-01 (gap-pin proposal).** **Severity 2. Status: structural
proposal. Confidence high.** Topology (i), the $\mathfrak m$-adic with
$\mathfrak m = (z_1) \subset \widehat\C[z_1, z_2]$, is the natural
choice because the W3-W26-08 counter-example
$\varphi(v_{0,-1}) = \sum_k(-1)^k(z_1^2)^k z_2^{-1-k}$ has $z_1$-degree
exactly $2k$ at term $k$, which is precisely the $\mathfrak m^{2k}$-filtration
level. Convergence is Krull / linear-topology convergence and is
unconditional.

### §1.2 Gap G2 — Cocycle-compatibility condition not unfolded

**W35 statement (verbatim, §1.4 condition (c)).** "for every $\varphi
\in \mathrm{Symp}_{\mathrm{form}}(\C^2, 0)$, … cocycle condition on
composites." W35 verified the algebra-level test on one element
($\varphi: z_2 \mapsto z_2 + z_1^2$); cocycle compatibility is a
higher-coherence condition about *pairs* and *triples* of
symplectomorphisms.

**Reduction.** $\mathrm{Symp}_{\mathrm{form}}(\C^2, 0)$ is
the formal-group exponential of $\bar A = \C[z_1, z_2]/\C\cdot1$,
generated by the polynomial Hamiltonians. By the
Baker-Campbell-Hausdorff formula and the linear-topology completeness
of $\bar A$ (W12 / final-convergence § Rank 4), it suffices to check
cocycle compatibility on:

1. **Linear generators**: $\mathrm{ad}_{z_1}$ and $\mathrm{ad}_{z_2}$
   (translation Hamiltonians); these generate $T^2$ subgroup.
2. **Quadratic generator**: $\mathrm{ad}_{z_1 z_2}$ (rotation/scaling
   Hamiltonian); generates $\mathrm{GL}_2$ Cartan.
3. **First non-linear generators**: $\mathrm{ad}_{z_1^2}$ and
   $\mathrm{ad}_{z_2^2}$ (the W3-W26-C3 conjectured $\mathfrak{sl}_2$
   inside $\bar A$).
4. **One cubic generator**: $\mathrm{ad}_{z_1^2 z_2}$ or
   $\mathrm{ad}_{z_1 z_2^2}$ (the first place where degree-3
   commutators decide the BCH series).

**G2 claim.** The full cocycle condition reduces to compatibility on
**finitely many tests at degree $\leq 4$** (the bracket of two
degree-2 generators).

**P4-G2-02 (cocycle reduction).** **Severity 3. Status: structural
proposal. Confidence medium.** Cocycle compatibility on
$\mathrm{Symp}_{\mathrm{form}}(\C^2, 0)$ reduces to verification on
the finite set $\{z_1, z_2, z_1z_2, z_1^2, z_2^2, z_1^2z_2, z_1z_2^2,
z_1^3, z_2^3\}$ (9 Hamiltonian generators in degrees 1-3) plus all
2-fold and 3-fold Poisson brackets. Concretely: a Symp-equivariant
PVA module structure on $\widehat{C^{+-}}$ exists iff for every pair
$H_1, H_2$ in this set, the diagram
$$\widehat\varphi_{H_1}^*\widehat\varphi_{H_2}^*\widehat M \cong
  \widehat\varphi_{H_2 + H_1 + \frac12\{H_1, H_2\}+\dots}^*\widehat M$$
commutes in the $\mathfrak m$-adic category, where
$\{H_1, H_2\}+\dots$ is the Baker-Campbell-Hausdorff series in
$\bar A$. Verification is finite per fixed cubic truncation.

### §1.3 Gap G3 — Heisenberg-PVA candidate at the algebra level only

**W35 statement (verbatim, §2.2).** Heisenberg PVA generated by
$z_1, z_2$ at canonical symplectic pairing.

**Why W35 stopped short.** W35 wrote $[(z_1)_\lambda z_2] = 1$ at the
algebra level but did not write the **module** $\lambda$-bracket
$Y_M(z_i, \lambda) v_{a, b}$, did not specify the vacuum module-state
triangular decomposition, and did not check the deformed bracket
$[(z_1)_\lambda z_2] = 1 + c\lambda$ at the column-Verma vacuum.

**G2 task.** Write the module $\lambda$-bracket explicitly.

**Construction.** On the candidate completed module $\widehat M_0
\subset \widehat{C^{+-}}$ (the column $a=0$, $\mathfrak m$-adically
completed in $z_1$), define the **module $\lambda$-bracket** by:
$$Y_{M_0}(z_1, \lambda) v_{0, b} = b \cdot v_{0, b-1} + O(\lambda),$$
$$Y_{M_0}(z_2, \lambda) v_{0, b} = 0,$$
the leading $\lambda^0$-term reproducing the W3 master action
formula. The $\lambda$-corrections $O(\lambda)$ encode the chiral
Heisenberg level $c$ and need to satisfy:

- **PVA-module sesquilinearity**: $Y_{M_0}(\partial a, \lambda)
  v = -\lambda Y_{M_0}(a, \lambda) v$.
- **PVA-module Jacobi**: $Y_{M_0}(a, \lambda) Y_{M_0}(b, \mu) v -
  Y_{M_0}(b, \mu) Y_{M_0}(a, \lambda) v = Y_{M_0}([a_\lambda b],
  \lambda + \mu) v$.

**P4-G2-03 (module $\lambda$-bracket candidate).** **Severity 3.
Status: structural proposal. Confidence medium.** A Heisenberg PVA
module $\widehat M_0$ exists in the $\mathfrak m$-adic category with
classical limit recovering $M_0$ as a column-Verma. Construction:
$\widehat M_0 = \widehat\C[z_1]\langle\langle z_2^{-1}\rangle\rangle$
with $\partial = \partial_w$ (chiral direction), $z_1$ acting by
shift in inverse $z_2$-power, $z_2$ acting by zero on the $a=0$
column. The $\lambda$-bracket $\lambda$-corrections are:
$Y_{M_0}(z_1, \lambda) v_{0, b} = b\,v_{0, b-1} + c\lambda \cdot
v_{0, b-1}$, with $c$ the BD chiral central charge of W3-W11-05.
Verification of sesquilinearity / Jacobi at $b \in [-5, -1]$ is the
3-month deliverable §2 below.

### §1.4 Gap G4 — Drinfeld stack pull-back machinery undefined

**W35 statement (verbatim, §6.3).** "Define the moduli stack
$\mathfrak M_{\mathrm{Symp}, \C^2, 0}$: $S$-points = pairs $(\mathcal
A, M)$ where $\mathcal A$ is a chiral algebra over $S \times
\widehat{\C^2}_0$ and $M$ is a chiral module."

**Why W35 stopped short.** This is a one-line definition: it does not
specify the cotangent complex of the stack, the deformation theory
controlling $\mathrm{Symp}_{\mathrm{form}}$-equivariant deformations,
or the obstruction class for lifting the classical Lie module to a
chiral module. Without these, "Drinfeld stack" is a placeholder.

**G2 task.** Give the deformation-theoretic definition.

**Working definition (P4-G2-04).** Let $L_{\C^2, 0}$ be the Lie
algebra $\Omega^\bullet_c(\widehat{\C^2}_0) \otimes \bar A$ (formal
Hamiltonian Lie algebra valued in compactly supported jet forms).
Then $\mathfrak M_{\mathrm{Symp}, \C^2, 0}$ is the formal stack
$\mathrm{Def}(L_{\C^2, 0})$ classifying $L_{\C^2, 0}$-Maurer-Cartan
elements modulo gauge, where the gauge group is
$\mathrm{Symp}_{\mathrm{form}}$ acting via the natural action on
$\bar A$. **Cotangent complex** at the trivial point: $\mathrm{cl}^*(L_{\C^2,
0}[1])$, where $\mathrm{cl}$ is the classical-limit / shifted-tangent
functor. The PVA module data lives as a quasi-coherent sheaf on this
stack via the standard Pridham / Lurie deformation-theoretic
realization (Pridham 2012; Lurie HA §13).

**P4-G2-04 (Drinfeld stack working definition).** **Severity 3.
Status: structural proposal. Confidence medium-low.** $\mathfrak
M_{\mathrm{Symp}, \C^2, 0}$ is the formal Maurer-Cartan stack of
$L_{\C^2, 0} = \Omega^\bullet_c(\widehat{\C^2}_0) \otimes \bar A$
modulo $\mathrm{Symp}_{\mathrm{form}}$ gauge. Cotangent complex at
the trivial origin is $L_{\C^2, 0}[1]$; obstructions to lifting a
classical Lie module $C^{+-}$ to a chiral module live in
$\mathrm{Ext}^2_{L_{\C^2, 0}}(C^{+-}, C^{+-})$. Verification of the
existence of a non-zero obstruction class is a Phase-4 derivation
(estimate: 6 months of focused work).

### §1.5 Gap G5 — Interaction with G3 supertrace discharge

**W35 statement.** None. W35 did not address the supertrace lane.

**G2 question.** The W22 / W30 supertrace discharge of
`prob:weighted-rg-locality` works at $\mathrm{GL}_2 \times T^2$ level
via super-balanced $\mathfrak{gl}(N|N)$. Does it extend to
$\mathrm{Symp}_{\mathrm{form}}$? See §4 below for full treatment.

---

## §2. T2 — Three-month milestone (the smallest verifiable result)

### §2.1 Statement

**P4-G2-M1 (3-month milestone).** Construct the candidate Heisenberg
PVA module $\widehat M_0$ of P4-G2-03 in the $\mathfrak m$-adic
category of P4-G2-01, and verify by hand (or by a `fractions.Fraction`
script analogous to `/tmp/w26_*.py`) that:

1. **Algebra-level $\mathrm{Symp}_{\mathrm{form}}$-equivariance
   passes on $\{\varphi: z_2 \mapsto z_2 + z_1^k\}_{k=2,3,4}$**: the
   Leibniz expansion of the PVA $\lambda$-bracket transforms
   consistently for all three (extending the W35 §3.4 check from $k=2$
   to $k=4$).

2. **Module-level $\mathfrak m$-adic convergence passes on
   $\widehat M_0$**: for $\varphi: z_2 \mapsto z_2 + z_1^2$ (the
   W3-W26-08 case), the formal sum $\sum_{k\geq 0}(-1)^k v_{2k, -1-k}$
   is a Cauchy sequence in the $\mathfrak m$-adic topology and
   converges to a single element of $\widehat M_0$.

3. **Sesquilinearity / Jacobi axioms hold for the module
   $\lambda$-bracket** at depth $b \in [-5, -1]$, with the explicit
   chiral central charge $c$ determined by the W3-W11-05 BD class.

4. **Cocycle compatibility on the $T^2$ subgroup is exact**: for
   $\varphi_1, \varphi_2 \in T^2$, $\widehat\varphi_2^*\widehat
   \varphi_1^* \widehat M_0 = \widehat\varphi_{12}^*\widehat M_0$
   strictly (no completion needed; $T^2$-equivariance is exact on
   the column-Verma per W3-W26-T1).

**Deciding evidence.** A LaTeX appendix (or extension to
`appendix-radial-parts-moyal.tex` style) plus a `scripts/`
script `check_pva_module_lambda_bracket.py` performing the four
checks on `fractions.Fraction` arithmetic, with verbatim output
captured in the milestone document.

### §2.2 Why this is the smallest verifiable result

The minimum content needed to make path (A) of W35 §6.1
"concretely testable" is:

- A specific **module** (not just an algebra) — provided by P4-G2-03.
- A specific **topology** — provided by P4-G2-01.
- A specific **non-linear test** — extending W35 §3.4 from one to
  three test symplectomorphisms.

Without P4-G2-M1, path (A) cannot be falsified. With P4-G2-M1, every
subsequent stage of the program (verifying cocycle compatibility on
cubic generators, extending to all polynomial Hamiltonians, making
contact with CGW path (B)) has a concrete numerical baseline.

### §2.3 What P4-G2-M1 does NOT provide

- **Full $\mathrm{Symp}_{\mathrm{form}}$-equivariance.** The cocycle
  on cubic and higher Hamiltonians is left for the 6-12 month
  milestone (P4-G2-M2 below).
- **CGW pull-back identification.** Path (B) of W35 §6.2 is left for
  the 12-month milestone (P4-G2-M3).
- **Drinfeld stack verification.** Path (C) of W35 §6.3 is left for
  the 18+ month milestone (P4-G2-M4).
- **Manuscript inscription.** P4-G2-M1 is research-program output, not
  a manuscript theorem; inscription would happen only after P4-G2-M2.

### §2.4 Failure modes

If the milestone fails: (a) Jacobi failure at $b \in [-5, -1]$ →
diagnostic: Heisenberg PVA insufficient; enrich to a $W$-algebra or a
larger PVA (R-W3-W26-C conjectured $\mathfrak{sl}_2 \subset \bar A$
via $\{z_1^2, z_2^2, z_1z_2\}$). (b) $\mathfrak m$-adic convergence
failure at cubic / quartic → switch topology to Tate inverse-limit
(P4-G2-01 (ii)) or locally constant factorization (P4-G2-01 (iii)).
(c) $T^2$-cocycle failure → revisit P4-G2-03 with $\partial$ acting
non-trivially on $z_2^{-1}$ (which W35 took as trivial). Each failure
mode has a concrete next step.

---

## §3. T3 — Open research questions

The following 7 questions arise from the three W35 attack paths after
the gap inventory of §1.

### §3.1 Path (A) — direct PVA construction

**Q-P4-G2-1 (module topology vs PVA topology).** Which topology on
$\widehat M_0$ is compatible with the PVA topology on $V$?
Specifically: in the standard PVA framework, $V$ is a $\C[\partial]$-module
with a topology induced by jet-degree filtration. A
$\mathfrak m$-adic topology on $\widehat M_0$ uses $\mathfrak m =
(z_1)$ in the symplectic-target direction, which is **transverse** to
the chiral $\partial$-direction. Is the resulting joint topology
(jet-degree on $V$, $\mathfrak m$-adic on $M$) functorial under
$\mathrm{Symp}_{\mathrm{form}}$?

**Q-P4-G2-2 (cocycle at degree 3 vs degree 4).** P4-G2-02 reduced
cocycle compatibility to 9 generators at degrees 1-3. Does the
reduction terminate at degree 3 or do degree-4 generators
($z_1^2 z_2^2$, $z_1^4$, $z_2^4$) introduce new constraints? The BCH
series produces new commutator structure at degree 4 (sum of three
$\bar A$-elements equals fourth via Jacobi). Verification of finite
truncation is the heart of the cocycle reduction.

**Q-P4-G2-3 (chiral central charge interaction).** The deformed
Heisenberg PVA (W35 §2.4) has $\lambda$-bracket
$[(z_1)_\lambda z_2] = 1 + c\lambda$. Does the central charge $c$
make the module-level cocycle condition exact, or does it need to
match the BD chiral central charge $[\bar c]$ of W3-W11-05 explicitly?
If the latter: the unique value $c$ that closes the cocycle is itself
a structural identification of the BD chiral central charge.

### §3.2 Path (B) — CGW pull-back

**Q-P4-G2-4 (which CGW limit produces the column-Verma).** W35 §5.1
quoted W3-W31-T2 as a double-twist limit $\epsilon_1, \epsilon_2 \to 0$
along a "specified scaling." Which specific scaling? Linear
($\epsilon_1 = t\epsilon_2$ as $t \to 0$), exponential ($\epsilon_1 =
e^{-1/\epsilon_2}$), or universal (independent of scaling)? The CGW
boundary VOA $W_{1+\infty}$ at general $(\epsilon_1, \epsilon_2)$ has
a 2-parameter family of surface defects; which one degenerates to
$C^{+-}$? An answer requires inscribing CGW arXiv:2007.09497 §3 (per
W3-W31-O1) and identifying the surface-defect spectrum at one
specified scaling.

**Q-P4-G2-5 (Symp-equivariance survival).** Even granting W3-W31-T2
holds, does $\mathrm{Symp}_{\mathrm{form}}$-equivariance survive the
$\epsilon \to 0$ limit? CGW VOA at $\epsilon \neq 0$ is
Symp-equivariant by construction (the Omega-deformed M-theory respects
the formal symplectic disk). But the limit is singular and
regularization may break Symp-equivariance to a smaller subgroup
(e.g.\ to $T^2$ or $\mathrm{GL}_2$, exactly recovering the W3-W26-T1
naturality class). If so, path (B) does not gain over path (A).

### §3.3 Path (C) — Drinfeld stack

**Q-P4-G2-6 (equivariant sheaf existence).** P4-G2-04 gave a working
definition of $\mathfrak M_{\mathrm{Symp}, \C^2, 0}$ via formal
Maurer-Cartan. Does there exist a $\mathrm{Symp}_{\mathrm{form}}$-equivariant
quasi-coherent sheaf $\mathcal M$ on $\mathfrak M$ whose fibre at the
trivial origin recovers $C^{+-}$? Existence is controlled by
$\mathrm{Ext}^2_{L_{\C^2, 0}}(C^{+-}, C^{+-})$; non-vanishing is the
obstruction. If the Ext class is zero, $\mathcal M$ exists canonically;
if non-zero, the column-Verma data does not lift to a
Symp-equivariant quasi-coherent sheaf.

**Q-P4-G2-7 (Ran-space descent).** The BD chiral algebra of W3-W11-05
is realized as a quasi-coherent sheaf on $\mathrm{Ran}(\widehat{\C^2}_0)$.
Does the column-Verma module descend to a Symp-equivariant chiral
module on $\mathrm{Ran}$, or does it descend only to an
"intersection-cohomology"-style stratified module that is canonical
on the open dense stratum but ill-defined on the closed strata?
Stratification of $\mathrm{Ran}(\widehat{\C^2}_0)$ under
$\mathrm{Symp}_{\mathrm{form}}$ is a non-trivial open question; the
naive descent is not Symp-equivariant.

### §3.4 Severity and dependencies

| Question | Path | Severity | Dependency | Estimate |
|----------|------|----------|------------|----------|
| Q-P4-G2-1 | (A) | 2 | P4-G2-M1 | Falls out of M1 |
| Q-P4-G2-2 | (A) | 3 | M1 + cubic verification | 6 mo |
| Q-P4-G2-3 | (A) | 3 | M1 + W3-W11-05 | 6-9 mo |
| Q-P4-G2-4 | (B) | 4 | CGW PDF (W3-W31-O1) | 12 mo |
| Q-P4-G2-5 | (B) | 4 | Q-P4-G2-4 + W3-W31-T2 | 12-18 mo |
| Q-P4-G2-6 | (C) | 4 | P4-G2-04 + Ext computation | 12-18 mo |
| Q-P4-G2-7 | (C) | 4 | Q-P4-G2-6 + Ran-stratification | 18+ mo |

The 3-month milestone (P4-G2-M1) addresses Q-P4-G2-1 directly and lays
groundwork for Q-P4-G2-2 and Q-P4-G2-3. The cross-volume questions
(Q-P4-G2-4 through Q-P4-G2-7) are deferred.

---

## §4. T4 — Interaction with Phase-4 G3 (supertrace discharge)

### §4.1 G3 input

W22 / W30 supertrace ledgers proved (W22-T1, W22-T2): on the
super-balanced $\mathfrak{gl}(N|N)$ source, the chain-level mixed
brane-defect QME obstruction class of `prob:weighted-rg-locality`
vanishes unconditionally; Theorem F$'$ becomes unconditional on this
source, since $\mathrm{Str}(I) = N - N = 0$ kills every regulator-class
representative of the obstruction class.

The W22 lens is **gl(N|N) with $\mathrm{GL}_2 \times T^2$
naturality**: the supertrace argument respects the column-Verma
identification of W3-W26-T1 because the underlying $\bar A$-module
structure is intact; the supertrace acts on the $\mathfrak{gl}(N|N)$
matrix-trace direction transversely to the column-Verma direction.

### §4.2 G2 cross-question

**Q-P4-G2-G3-INT (load-bearing).** Does the W22 / W30 super-balanced
discharge of `prob:weighted-rg-locality` extend from $\mathrm{GL}_2
\times T^2$ to all of $\mathrm{Symp}_{\mathrm{form}}$?

**Why this is the right question.** The Symp-equivariance of the
column-Verma identification is the load-bearing G2 obstruction
(R-W3-W26-A). The supertrace discharge of W22 is the load-bearing G3
result. If the two discharges are independent — supertrace handles
the Lie-algebra direction, Symp-equivariance handles the
representation-module direction — then they compose without
interference. If they are entangled, then resolving one resolves the
other simultaneously.

**Concrete entanglement test.** The W22 chain-level
$[\mathrm{Str}\,\psi]_{\mathrm{BV}}$ class is computed as a residue
on the $\mathfrak{gl}(N|N)$ module structure. The Symp-equivariance
of this residue depends on whether
$\mathrm{Str}(\varphi(\psi)) = \mathrm{Str}(\psi)$ for $\varphi \in
\mathrm{Symp}_{\mathrm{form}}$. By the cyclicity of supertrace
under the matrix conjugation, this holds iff $\varphi$ acts on the
$\mathfrak{gl}(N|N)$ direction by the trivial action — which it
does, since $\varphi$ acts on the *symplectic-target* coordinates
$(z_1, z_2)$, not on the matrix indices.

**P4-G2-05 (G3 extension verdict, conditional).** **Severity 2.
Status: structural proposal. Confidence high.** The W22 / W30
super-balanced supertrace discharge of `prob:weighted-rg-locality` is
$\mathrm{Symp}_{\mathrm{form}}$-equivariant by **transversality**:
the supertrace acts on the $\mathfrak{gl}(N|N)$ matrix direction,
$\mathrm{Symp}_{\mathrm{form}}$ acts on the $(z_1, z_2)$ symplectic-target
direction; the two actions commute exactly. **Therefore: if R-W3-W26-A
is discharged by any path (A, B, or C), the supertrace discharge of
W22 extends from $\mathrm{GL}_2 \times T^2$ to all of
$\mathrm{Symp}_{\mathrm{form}}$ with no additional condition.**

### §4.3 Verification

The verification of P4-G2-05 reduces to checking that the W22
chain-level cocycle $[\mathrm{Str}\,\psi]_{\mathrm{BV}}$ is independent
of the column-Verma decomposition of the underlying module. This is
**already proven** by W22 § (chain-level $\Lambda^{\mathrm{Str}}$):
the supertrace pulls back through any $\bar A$-module structure
because it lives in the matrix direction. The cyclicity-of-supertrace
argument is universal in $\bar A$-modules; it does not see the
column-Verma decomposition at all.

**Conclusion.** The G3 supertrace lane and the G2 Symp-equivariance
lane are **transverse** — independent and composable. A discharge
on one side does not interfere with a discharge on the other, and a
joint discharge gives:

$$
\text{F}^{\prime\prime}: \text{Theorem F}^\prime\text{ on }
\mathfrak{gl}(N|N)\text{ super-balanced source, with full
}\mathrm{Symp}_{\mathrm{form}}\text{-equivariance of the
column-Verma module structure on }C^{+-}.
$$

This is the **joint G2 + G3 deliverable** at the 18+ month horizon
(P4-G2-M5 below).

### §4.4 Why this is good news

Independence of the two lanes means each can be attacked separately:
G2 pursues path (A) without depending on G3; G3 extends W22-T1 /
W22-T2 to all-loop without depending on G2. Joint convergence gives
$\mathfrak{gl}(N|N)$ + $\mathrm{Symp}_{\mathrm{form}}$ Theorem F$''$
unconditionally.

---

## §5. T5 — Numerical exploration: distinguishing paths (A), (B), (C)

### §5.1 The simplest distinguishing test

**Setup.** A computational test that distinguishes the three paths
must be sensitive to:
- whether the obstruction lives at the **algebra level** (path A
  module topology) or the **module level** (paths B, C);
- whether the obstruction is **finite** at the cubic test (path A
  resolves) or **infinite** (paths B, C resolve);
- whether the obstruction is **regulator-class-dependent** (path B
  CGW double-twist requires a specific regulator) or
  **regulator-independent** (paths A, C are structural).

**Probe.** The candidate test: at the cubic symplectomorphism
$\varphi^{(3)}: (z_1, z_2) \mapsto (z_1, z_2 + z_1^3)$, compute on
the candidate completed module $\widehat M_0$ of P4-G2-03 the formal
sum
$$
\widehat\varphi^{(3)}(v_{0, -1}) = (z_2 + z_1^3)^{-1}
   = \sum_{k \geq 0} (-1)^k z_1^{3k} z_2^{-1-k}
   = \sum_{k \geq 0} (-1)^k v_{3k, -1-k}.
$$

At the $\mathfrak m$-adic topology of P4-G2-01, the term at $k$ has
$z_1$-degree $3k$, in $\mathfrak m^{3k}$. Krull convergence is
unconditional; the sum converges to a single element of $\widehat
M_0$.

### §5.2 Distinguishing signature

The three paths predict different things at this test:

**Path (A).** The element $\widehat\varphi^{(3)}(v_{0, -1}) \in
\widehat M_0$ is a single, computable, finite element in the
$\mathfrak m$-adic completion. Cocycle compatibility with the
quadratic test at $\varphi^{(2)}: z_2 \mapsto z_2 + z_1^2$ requires:
$$\widehat\varphi^{(3)} = \widehat\varphi^{(2)} \circ
\widehat\varphi^{(2,3)}$$ where $\varphi^{(2,3)}$ is the BCH
correction. Computability is finite per fixed $\mathfrak m$-adic
truncation depth. **Pass ↔ path (A) discharges R-W3-W26-A.**

**Path (B).** $\widehat\varphi^{(3)}(v_{0, -1})$ matches the CGW
surface-defect at $\R \times \{z_2 + z_1^3 = 0\}$ under the double-
twist limit. Distinguishing test: compute the CGW character (using
the arXiv:2007.09497 §3 surface-defect spectrum formula) at the
$\epsilon \to 0$ limit, compare to path (A) prediction. Match ↔
consistency.

**Path (C).** The Drinfeld stack pull-back predicts $\mathcal M$ is
quasi-coherent on $\mathfrak M_{\mathrm{Symp}}$; action of
$\mathrm{ad}_{z_1^3}$ controlled by the $\mathrm{Ext}^2$ obstruction
of P4-G2-04. Distinguishing test: compute $\mathrm{Ext}^2_{L_{\C^2,
0}}(C^{+-}, C^{+-})$ via Maurer-Cartan deformation theory; non-
vanishing ↔ path (C) fails; vanishing ↔ canonical $\mathcal M$.

### §5.3 The minimal computational deliverable

**P4-G2-CT1 (computational test).** A single Python script
`scripts/check_pva_cubic_test.py` that:

1. Constructs the truncated $\mathfrak m$-adic completion $\widehat
   M_0 / \mathfrak m^{N}$ for $N = 24$ ($z_1$-degrees up to 24,
   capturing $k \leq 8$ in the cubic test).
2. Computes $\widehat\varphi^{(3)}(v_{0, -1})$ explicitly as a finite
   linear combination $\sum_{k=0}^{7}(-1)^k v_{3k, -1-k}$ at
   `fractions.Fraction` arithmetic.
3. Compares to the BCH-cocycle composite $\widehat\varphi^{(2)} \circ
   \widehat\varphi^{(2,3)}(v_{0, -1})$ to verify cocycle compatibility.
4. Outputs (a) the $\mathfrak m$-adic limit element; (b) the cocycle
   discrepancy at truncation depth 24.

**Expected output if path (A) succeeds.** Cocycle discrepancy = 0 at
truncation 24, with explicit element $\widehat\varphi^{(3)}(v_{0, -1})
\in \widehat M_0/\mathfrak m^{24}$ identifiable by basis listing.

**Expected output if path (A) fails.** Cocycle discrepancy nonzero at
truncation 24, identifying the obstruction class and the leading
term $z_1^{2k_0} z_2^{-1-k_0}$ at which the discrepancy first
appears.

**Difficulty.** The script is straightforward extension of
`/tmp/w26_*.py` style; estimated 1-2 weeks of focused implementation
once P4-G2-M1 is articulated.

---

## §6. T6 — Proposed milestone ladder

### §6.1 3-month milestone (P4-G2-M1)

**Deliverable.** Extension to `appendix-radial-parts-moyal.tex` style
appendix and `scripts/check_pva_module_lambda_bracket.py`, executing
the four checks of §2.1: algebra-equivariance on $\{\varphi^{(k)}: k =
2, 3, 4\}$, $\mathfrak m$-adic convergence at $k=2$, sesquilinearity
/ Jacobi at depth $b \in [-5, -1]$, $T^2$-cocycle exactness.

**Consumer.** Phase-4 G2 working group; not yet in manuscript.

**Severity.** 2 (research-program output).

### §6.2 6-month milestone (P4-G2-M2)

**Deliverable.** Extend P4-G2-M1 to all 9 Hamiltonian generators of
P4-G2-02 (degrees 1-3); verify cocycle compatibility on the full set
via BCH series; write up as a research note `pva-module-cubic-cocycle.tex`
candidate appendix.

**Consumer.** Manuscript candidate inscription as a Phase-3 / Phase-4
note (NOT main theorem); cross-references R-W3-W26-A as discharged at
cubic level.

**Severity.** 2.

**Failure modes.** If Q-P4-G2-2 (cocycle reduction terminates at
degree 3) fails, the milestone restricts to "cocycle on degrees 1-2"
and degrees 3+ remain Phase-4.

### §6.3 12-month milestone (P4-G2-M3)

**Deliverable.** Inscribed CGW PDF arXiv:2007.09497 in
`references/primary-sources/`; identification of the surface-defect
spectrum at $\R \times \{z_2 = 0\}$; explicit computation of the
double-twist limit $\epsilon \to 0$ producing a candidate Lie 2-cocycle
class on $\bar A$; comparison with $[\bar c]$ of W3-W11-05.

**Consumer.** Joint Phase-4 G2 / G5 (CGW lens) deliverable; addresses
W3-W31-O1 and partially W3-W31-T2.

**Severity.** 3 (cross-volume; partial).

**Failure modes.** If Q-P4-G2-4 (which CGW limit) does not have a
clean answer at the inscribed source, the milestone restricts to "the
linear scaling $\epsilon_1 = t\epsilon_2 \to 0$ produces a class in
the same cohomology class as $[\bar c]$ but with an undetermined
multiplicative constant" (i.e., partial discharge).

### §6.4 18+ month milestone (P4-G2-M4)

**Deliverable.** Drinfeld stack $\mathfrak M_{\mathrm{Symp}, \C^2, 0}$
constructed via Pridham / Lurie deformation theory; equivariant sheaf
$\mathcal M$ recovering $C^{+-}$ at trivial origin; verification of
Ran-space descent on the open stratum.

**Consumer.** Joint Phase-4 G2 / G7 (Drinfeld lens) deliverable;
addresses Q-P4-G2-6 and Q-P4-G2-7.

**Severity.** 4 (highest abstract / categorical machinery).

**Failure modes.** If $\mathrm{Ext}^2_{L_{\C^2, 0}}(C^{+-}, C^{+-})
\neq 0$, the equivariant sheaf does not exist and path (C) is closed
out as "no canonical Symp-equivariant chiral lift exists." This
would be a positive negative result: it would force path (A) or (B).

### §6.5 Joint Phase-4 G2 + G3 milestone (P4-G2-M5)

**Deliverable.** Joint extension of W22 / W30 supertrace discharge
(G3) plus PVA / chiral lift (G2) producing **Theorem F$''$**:
$\mathrm{Symp}_{\mathrm{form}}$-natural unconditional discharge of
`prob:weighted-rg-locality` on $\mathfrak{gl}(N|N)$ super-balanced
source. Specifically: combine P4-G2-M2 (cocycle on generators 1-3) +
W22 / W30 supertrace discharge (already proven for $\mathrm{GL}_2
\times T^2$) via the transversality argument of P4-G2-05.

**Consumer.** Manuscript inscription candidate as a joint
Phase-4 / Phase-3 theorem (uncertain whether to scope as Theorem F$''$
or as a new C-3 / D-4 corollary).

**Severity.** 2 (load-bearing for Wave-3 stable core).

**Estimate.** 18-24 months (after P4-G2-M2).

### §6.6 Tabulated milestone ladder

| Milestone | Horizon | Path | Deliverable | Severity | Manuscript? |
|-----------|---------|------|-------------|----------|-------------|
| P4-G2-M1 | 3 mo | (A) | Module $\lambda$-bracket + cocycle on T² | 2 | No |
| P4-G2-M2 | 6 mo | (A) | Cocycle on 9 generators (degrees 1-3) | 2 | Candidate appendix |
| P4-G2-M3 | 12 mo | (B) | CGW double-twist surface-defect | 3 | No (cross-volume) |
| P4-G2-M4 | 18+ mo | (C) | Drinfeld stack + equivariant sheaf | 4 | No (research program) |
| P4-G2-M5 | 18-24 mo | joint G2+G3 | Theorem F$''$ on $\mathfrak{gl}(N|N)$ + Symp | 2 | Candidate theorem |

---

## §7. Per-target findings table

| Target | Verdict | Severity | Detail |
|--------|---------|----------|--------|
| T1 (G1: module topology) | $\mathfrak m$-adic chosen | 2 | P4-G2-01 |
| T1 (G2: cocycle reduction) | 9 generators, degrees 1-3 | 3 | P4-G2-02 |
| T1 (G3: PVA module candidate) | Heisenberg PVA module written | 3 | P4-G2-03 |
| T1 (G4: Drinfeld stack definition) | Pridham / Lurie working def | 3 | P4-G2-04 |
| T1 (G5: G3 interaction) | Transversality, no entanglement | 2 | P4-G2-05 |
| T2 (3-mo milestone) | P4-G2-M1 declared | 2 | §2 |
| T3 (open questions) | 7 questions enumerated | 2-4 | §3 |
| T4 (G2 + G3 interaction) | Independent, composable | 2 | §4 |
| T5 (numerical test) | P4-G2-CT1 cubic test | 3 | §5 |
| T6 (milestone ladder) | 5 milestones, 3-24 mo | 2-4 | §6 |

---

## §8. New residuals / obligation entries

### §8.1 Phase-4 entries

**R-P4-G2-A (Phase-4, complementary to R-W3-W35-A).** Module-level
cocycle compatibility on cubic Hamiltonian generators.
$\mathrm{Symp}_{\mathrm{form}}$-equivariance at the cubic level
(degrees 1-3 generators) is the next provable extension of the W35
algebra-level check. Severity 3. Deciding evidence: P4-G2-M2 (6 mo).

**R-P4-G2-B (Phase-4, conditional on path (B)).** CGW arXiv:2007.09497
inscription and surface-defect identification at the linear scaling
$\epsilon_1 = t \epsilon_2 \to 0$. Severity 4. Conditional on
W3-W31-O1.

**R-P4-G2-C (Phase-4, conditional on path (C)).** Computation of
$\mathrm{Ext}^2_{L_{\C^2, 0}}(C^{+-}, C^{+-})$ via Pridham / Lurie
deformation theory. Severity 4. Phase-4 frontier; needs derived-
algebraic-geometry expertise.

**R-P4-G2-D (Phase-4, joint G2+G3).** Theorem F$''$ on
$\mathfrak{gl}(N|N)$ super-balanced source with full
$\mathrm{Symp}_{\mathrm{form}}$-equivariance. Severity 2 (load-bearing
once available). Conditional on R-P4-G2-A discharge.

### §8.2 Phase-3 entries (within reach)

**R-P4-G2-E (Phase-3).** Implementation of P4-G2-CT1 / `scripts/
check_pva_cubic_test.py`. Severity 1. Estimate 1-2 weeks.

**R-P4-G2-F (Phase-3).** Verification of P4-G2-05 (transversality of
G2 and G3 lanes) at the W22 chain-level. Severity 2. Estimate 1-2
months.

---

## §9. Provenance

G2 (Phase-4 complementary outline) read in full:
- `/Users/raeez/topological-strings/CLAUDE.md`.
- `/Users/raeez/topological-strings/reconstitution/wave3-W35-R26A-symp-2026-04-28.md` (parent W35 outline; gaps identified §1).
- `/Users/raeez/topological-strings/reconstitution/wave3-W26-column-verma-2026-04-28.md` (column-Verma identification).
- `/Users/raeez/topological-strings/reconstitution/wave3-W21-wakimoto-2026-04-28.md` (Wakimoto label correction).
- `/Users/raeez/topological-strings/reconstitution/wave3-W22-supertrace-rigorous-2026-04-28.md` (G3 supertrace anchor; transversality §4).
- `/Users/raeez/topological-strings/reconstitution/wave3-FINAL-convergence-report-2026-04-28.md` (Wave 3 certified converged; G2 lives at Rank 4).

External references invoked (W35-shared, no new web search):
- Frenkel-Ben-Zvi 2004 (PVA module theory), Bakalov-Kac 2003 (PVA axioms),
  De Sole-Kac 2006 (classical PVA), Beilinson-Drinfeld 2004 (chiral
  algebras), Lurie HA §13 (deformation theory), Pridham 2012
  (Maurer-Cartan moduli), Costello-Gaiotto-Williams 2007.09497
  (CGW VOA + surface defects).

G2 confidence: every claim either flags W35 verbatim or extends it
by a clearly stated next step. No new theorems claimed; only research-
program structure plus the next testable milestone.

---

## §10. 200-word summary

Phase-4 G2 outlines the next-step research program complementary to
W35 (`wave3-W35-R26A-symp-2026-04-28.md`, 1144 lines). W35 produced
the open question Q-W3-W35-A, an algebra-level
$\mathrm{Symp}_{\mathrm{form}}$-equivariance check on the quadratic
test, and three attack paths (A) direct PVA, (B) CGW pull-back, (C)
Drinfeld stack. G2 closes five gaps W35 named but did not pin down:
(G1) module topology — choose $\mathfrak m$-adic with $\mathfrak m
= (z_1)$ giving Krull convergence; (G2) cocycle compatibility — reduces
to 9 Hamiltonian generators at degrees 1-3 via BCH; (G3) Heisenberg-PVA
module $\lambda$-bracket with explicit chiral central charge $c$ matching
the BD class $[\bar c]$ of W3-W11-05; (G4) Drinfeld stack $\mathfrak
M_{\mathrm{Symp}, \C^2, 0}$ via Pridham / Lurie formal Maurer-Cartan;
(G5) G2 + G3 supertrace lanes are transverse — independent and
composable. The 3-month milestone (P4-G2-M1) is the smallest verifiable
result: explicit module $\lambda$-bracket + cocycle on $T^2$ + cubic-test
$\mathfrak m$-adic convergence + Jacobi at depth 5. Seven open
questions (Q-P4-G2-1 through 7) and a five-step milestone ladder
(P4-G2-M1 through M5) enumerate the research program. Joint G2 + G3
deliverable: Theorem F$''$ on $\mathfrak{gl}(N|N)$ super-balanced
source with full $\mathrm{Symp}_{\mathrm{form}}$-equivariance,
unconditional, at 18-24 months.

---

End of P4-G2 complementary outline.
