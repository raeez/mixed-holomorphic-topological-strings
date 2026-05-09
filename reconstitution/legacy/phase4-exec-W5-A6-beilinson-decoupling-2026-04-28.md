# Phase-4 EXEC W5-A6 — Beilinson + Composition decoupling probe of wave-4 #105 P4-Decoupling-Proposition

**Date.** 2026-04-28.
**Author.** Raeez Lorgat.
**Phase.** 4 EXEC, attack-heal-swarm Wave 5 (server rate-limit relaunch).
**Wave.** Wave 5 attacker A6 = Beilinson + Composition.
**Target.** `reconstitution/platonic-ideal-plan-2026-04-28.md` and the
wave-4 ledger entry `attack-heal-platonic-2026-04-28.md` Phase-4 EXEC
#105 closure of `P4-Decoupling-Proposition`.
**Mode.** Proposal-only. No commits. No manuscript edits.
**ID prefix.** `P4-EXEC-W5-A6-`.

**Probe.** Wave-4 #105 closed the Decoupling-Proposition with the
verdict that Theorem G's chain-level closure requires **exactly three
ingredients**

* **(I-1)** brane-line BD chiral algebra $\mathfrak h_I = \Omega^\bullet_c(I) \widehat\otimes \mathfrak h$ on $\R$ (G1-M1 closed);
* **(I-2)** strict $E_2$-multiplication on the brane-line factorization in $\mathcal C_{\mathrm{ML}}$ via Lurie HA §5.5.4.16 + LC translation invariance (G1-M2 closed);
* **(I-3)** Hamiltonian Maurer-Cartan twist $\alpha = \alpha_{x_i} dx^i + \alpha_{\bar z_j} d\bar z^j$ with $F_\alpha = 0$ (`main.tex`:1789-1840),

and the verdict that operadic mixed-Dunn $\E_m^{\mathrm{top}} \otimes \E_n^{\mathrm{hol}} \simeq \E_{m,n}^{\mathrm{mixed}}$ is **not required**. This wave-5 probe re-examines that closure under four pressure tests:

* **Q1.** Does strict $E_2$ in $\mathcal C_{\mathrm{ML}}$ (I-2) implicitly compose with (I-1) across the topological-holomorphic interface, requiring partial mixed-Dunn after all?
* **Q2.** BD §3.4.10-11 chiral axioms (Ax.1)-(Ax.5) on the product manifold: does the (I-1) BD chiral algebra implicitly invoke (Ax.4) chiral Jacobi at depth $> 5$?
* **Q3.** Does the locally-constant cosheaf direction on $\Omega^\bullet_c(I) \otimes \mathfrak h$ require factoring through bulk Čech covers on $\R^2 \times \C^2$ that wave-4 missed?
* **Q4.** CE chains versus cochains: does the proposed `Decoupling.` clause at `theorem-lanes.tex` lines 453-455 maintain canonical CE chains (covariant) or slip into CE cochains (contravariant)?

**Primary citations.**
- Beilinson-Drinfeld, *Chiral Algebras*, AMS Coll. Pub. vol. 51, 2004 (`BD04`): §3.4.1 (page 162-163) chiral OPE bracket and chiral central charge; §3.4.5 (page 165) chiral algebra ≃ FA on Ran($X$); §3.4.10 (page 173) chiral product on $X \times Y$; §3.4.11 (page 174) chiral axiom on the product manifold.
- Beilinson-Bernstein, *Localisation de* $\mathfrak g$-*modules*, C. R. Acad. Sci. Paris 292, 1981 (`BB81`): the canonical "$\mathcal D$-module on flag variety = representation of $\mathfrak g$" descent picture, prototype for the local-to-global Beilinson-school move.
- Beilinson-Drinfeld, *Quantization of Hitchin's integrable system and Hecke eigensheaves*, preprint 1996 (`BD96`): the Hitchin $\mathcal D$-module construction; the prototype "global flatness from local Hamiltonians" used here as analytic foil.
- Lurie, *Higher Algebra*, May 2017 / kerodon §HA.5.5.4 (`LurieHA`): §5.5.4.10 (LCFA on $\R^n$ ≃ $E_n$-algebra); §5.5.4.16 (Dunn additivity $E_m \otimes E_n \simeq E_{m+n}$ in $\Pr^L$).
- Costello-Gwilliam, *Factorization Algebras in Quantum Field Theory*, Cambridge UP, 2017/2021, Vol. I (`CGW1`): §6.4 LCFA / Weiss covers; §A.5.4-6 cosheaf product stability.

**Inputs (read in full or relevant sections).**
- `reconstitution/platonic-ideal-plan-2026-04-28.md` (full).
- `reconstitution/attack-heal-platonic-2026-04-28.md` (#105 closure, lines 6128-6210; structural ledger).
- `reconstitution/phase4-exec-Decoupling-Proposition-2026-04-28.md` (full; the wave-4 closure under attack here).
- `reconstitution/phase4-exec-G1-M1-BD-chiral-2026-04-28.md` (full; D1-D6, hypothesis tables).
- `reconstitution/phase4-exec-G1-M2-E2-promotion-2026-04-28.md` (full; $E_2$-promotion, Hamiltonian flat connection on $\R^2$, transverse Hamiltonian Lie algebra $\bar A_\perp$).
- `reconstitution/phase4-exec-Mixed-Dunn-Probe-2026-04-28.md` (Mixed-Dunn obstruction class, cross-flatness MC, three Phase-5 sub-problems).
- `reconstitution/phase4-exec-Chiral-Product-Audit-2026-04-28.md` (per-axiom (Ax.1)-(Ax.5) verdicts at each layer).
- `main.tex`:280-470 (`lem:omega-cocycle`, `thm:u1-center-anomaly`, `thm:u1-center-anomaly-open`, `thm:quantum-classical-anomaly`).
- `main.tex`:1750-1900 (Hamiltonian BF action, $F_\alpha = 0$, ghost-zero $\alpha = \alpha_{x_i} dx_i + \alpha_{\bar z_j} d\bar z_j$).
- `main.tex`:1996-2438 (factorization upgrade and cochain CE/PV).
- `theorem-lanes.tex` lines 420-456 (`thm:lane-u1-anomaly`, the inscription target).

---

## §0. Executive verdict

**(V-0) Decoupling holds; certify with two sharpenings.** The
wave-4 closure (Theorem G chain-level closure ⊥ operadic mixed-Dunn)
**survives the Beilinson + Composition pressure test** at the chain
level on which Theorem G as currently stated lives. The
sharpenings recommended below do not re-open the proposition; they
sharpen the inscription so that the load-bearing distinctions are
explicit on the surface of the manuscript.

**(V-1) Composition lens interpretation of (I-1) ∘ (I-2).** The
$\mathcal C_{\mathrm{ML}}$ Dunn additivity uniting (I-1) and (I-2)
runs **entirely inside the topological factor $\R^2$**, not across
the topological-holomorphic interface. The G1-M2 construction
(`phase4-exec-G1-M2-E2-promotion-2026-04-28.md` §2.1 + §3.1)
manifestly tensors **two $E_1$ factors on two independent $\R$
copies inside $\R^2$**: a brane-direction $\R$ carrying $\bar A$
and a transverse-direction $\R$ carrying an isomorphic copy
$\bar A_\perp$, glued by the **topological-topological** cross-bracket
$\{\alpha_{x_1}, \alpha_{x_2}\}$ = 0 component of $F_\alpha$. The
$\C^2$ direction enters G1-M2 only as a *coefficient module*: both
$\bar A$ and $\bar A_\perp$ live on the same formal symplectic disk
$\widehat{\C^2}_0$, treated **algebraically**, not as an
$\E_2^{\mathrm{hol}}$-FA. **Q1 answered:** there is no implicit
partial mixed-Dunn in the (I-1) ∘ (I-2) composition; the cross-mix
of $\R^k$ with $\C^2$ is supplied separately by (I-3), and the
operadic mixed-Dunn equivalence is genuinely outside the
chain-level closure path.

**(V-2) BD chiral Jacobi (Ax.4) is invoked at depth 5 only on
$\R$, not on the product manifold.** (I-1) BD chiral algebra on
$\R$ (G1-M1 D1-D6) verifies BD §3.4.1 chiral OPE, chiral central
charge, and the Bakalov-Kac λ-bracket axioms, with chiral Jacobi at
depth 5 verified at 405 instances (P4-G2-M1 §4.2 T_HEX, 0 failures).
**This is not BD §3.4.11 chiral axiom on the product manifold.**
The latter would compose the chiral OPE bracket on factors
$X \times Y$ via the chiral cobracket on $\Delta^*(\mathcal F \boxtimes \mathcal G)$;
this composition is what Mixed-Dunn-Probe identifies as open. Theorem
G's chain-level proof
(`main.tex`:343-361) invokes only Lie-algebra Jacobi for $\bar A$
in the algebraic CE complex computing $H^2_{\mathrm{Lie}}(\bar A, \C)$:
this is **classical Lie-algebra Jacobi**, supplied algebraically,
not by chiral Jacobi at any depth on any manifold. **Q2 answered:**
Theorem G uses Lie Jacobi on $\bar A$ (cochain-level CE arithmetic),
**not** BD chiral Jacobi (Ax.4) on $\R^2 \times \C^2$. (I-1)'s
chiral Jacobi at depth 5 enters only `thm:u1-center-anomaly-open`
through the brane-line image of $[\bar c]$, where it is verified at
G1-M1 scope. Wave-4 #105 §2.4 conflates these; the sharpening is to
distinguish algebraic Lie Jacobi (on $\bar A$, classical) from BD
chiral Jacobi (on $\R$, depth 5, G1-M1-verified) from BD product
chiral Jacobi (on $X \times Y$, open).

**(V-3) Cosheaf factor through bulk Čech: no.** $\Omega^\bullet_c(I)
\otimes \mathfrak h$ is the brane-line cosheaf on $\R$ alone; its
cosheaf condition is verified by extension-by-zero functoriality
on $\R$ (M-1 §1, `phase4-exec-G1-M1-BD-chiral-2026-04-28.md`). The
**bulk Čech direction** on $\R^2 \times \C^2$ — i.e., a Weiss-cover
descent on the 6-real-dim Ran space — is exactly the M-37 / R-03
obligation, **not used** by the chain-level proof. The
brane-line cosheaf admits a stratum-restriction picture from
$\R \subset \R^2 \times \C^2$; the descent that the chain-level
proof **does** need is descent on $\mathrm{Ran}(\R)$, supplied
by Lurie 5.5.4.10 + G1-M1 D3. **Q3 answered:** no, the locally-constant
cosheaf direction does not require bulk Čech descent on
$\R^2 \times \C^2$. Wave-4 #105 §2 is correct on this point; the
sharpening is to record explicitly that the cosheaf descent runs
on $\mathrm{Ran}(\R)$ (single brane-line) and not on
$\mathrm{Ran}(\R^2 \times \C^2)$.

**(V-4) CE chains vs cochains: the inscription is correctly in
cochains; one phrasing should be sharpened.** The wave-4 #105
inscription at `theorem-lanes.tex` lines 453-455 cites "the algebraic
Lie-cohomology computation of $[\bar c]$"; this is **CE cochains**
(cohomology, contravariant), matching the cochain-level
formulation of `thm:u1-center-anomaly`'s proof at `main.tex`:343-361
(central extension class in $H^2_{\mathrm{Lie}}(\bar A, \C)$).
**Q4 answered:** the inscription is consistent with the cochain
direction. The Beilinson-school subtlety — that BD §3.4.5 equivalence
"chiral algebra ≃ FA on Ran($X$)" naturally pairs **chiral algebra =
cochain** with **factorization algebra = chain** under the
de Rham / Schouten dualities of Lurie HA Theorem 5.5.4.10 — is
manifested in the manuscript through the
$C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak g_I) \cong
\mathrm{PV}(S(\mathfrak h_I))$ identification of `theorem-lanes.tex`
lines 96-148 (Lane 3 / `thm:lane-ce-pv-center`). The wave-4 #105
inscription does not slip from cochains into chains: $H^2_{\mathrm{Lie}}$
appears only on the cochain side throughout. The sharpening is editorial:
where the inscription says "the algebraic Lie-cohomology computation
of $[\bar c]$ on the reduced Hamiltonian Lie algebra $\bar A$",
the prose could read "the algebraic Lie-algebra cohomology
$H^2_{\mathrm{Lie}}(\bar A, \C)$" to record the cochain direction
unambiguously. This is editorial only; no proof is changed.

**(V-5) Severity verdict.** **Decoupling holds; certify.**
None of the four probe questions destabilises the wave-4 #105
closure. Three editorial sharpenings are recommended (§7
inscription block); none is gating; all are additive. The
proposition's structural minimality verdict — only (I-1), (I-2),
(I-3) supply Theorem G's chain-level closure — is preserved.

**Severity: 0** (clean / certified). **Phase-5 deferral:** no new
obligations.

---

## §1. Probe Q1 — Does (I-2) implicitly compose with (I-1) crossing the topological-holomorphic interface?

The pressure question. Wave-4 #105 §2.3 states that (I-2) is the
strict $E_2$-multiplication on the brane-line factorization in
$\mathcal C_{\mathrm{ML}}$ via Lurie HA §5.5.4.16 (Dunn additivity)
plus LC-2 translation invariance, *restricted* to the ML-envelope
on which presentability is uniformly controlled. The probe asks: does
this $E_2$ structure manifestly compose with (I-1)'s $E_1$
brane-line structure, and if so, does the composition cross the
topological-holomorphic interface?

### §1.1 Interpretation G1-M2 §2.1 — the candidate $E_2$ algebra has TWO $\R$ factors

From `phase4-exec-G1-M2-E2-promotion-2026-04-28.md` §2.1:

> The candidate $E_2$ algebra on $\R^2$ has underlying chain complex
> $A_{E_2}(U) := C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak g^{(2)}_U)$,
> $\mathfrak g^{(2)}_U := \Omega^\bullet_c(U) \widehat\otimes (\bar A \oplus \bar A_\perp)$,
> where $U \subseteq \R^2$ is open, $\Omega^\bullet_c(U)$ is the
> compactly supported de Rham cosheaf, and $\bar A_\perp$ is the
> *transverse* Hamiltonian Lie algebra contributed by the second
> $\R$ direction. ... The transverse Hamiltonian Lie algebra
> $\bar A_\perp$ is *isomorphic* to $\bar A$ as a Lie algebra (both
> are the perfect Hamiltonian Lie algebra $\C[z_1, z_2]/\C\cdot 1$
> on the same formal symplectic disk $\widehat{\C^2}_0$); the
> distinction is which $\R$-direction-of-$\R^2$ is being smeared.

**Composition interpretation.** (I-1)'s brane-line $E_1$ algebra
$A_{\mathrm{brane}} = A_\partial^{\mathrm{Ham}}(I)
= \widehat{\mathbf S}(\mathfrak h_I)$ sits inside (I-2)'s
$E_2$ algebra $A_{E_2}$ as **the brane-direction tensor factor**,
via the Lurie HA §5.5.4.16 equivalence

$$
\mathrm{Fact}^{\mathrm{lc}}(\R^2; \mathcal C_{\mathrm{ML}})
\;\simeq\;
\Alg_{E_2}(\mathcal C_{\mathrm{ML}})
\;\simeq\;
\Alg_{E_1}(\Alg_{E_1}(\mathcal C_{\mathrm{ML}})),
$$

with the two $E_1$'s corresponding to the brane direction $\R$ and
the transverse direction $\R$ inside $\R^2 = \R \times \R$.

**Crucial structural fact.** Both $\R$ factors are **purely
topological** in the manuscript's setup. The composition (I-1) ∘ (I-2)
runs through the Lurie locally-constant equivalence on $\R^2$, which
is the **topological factor**. The $\C^2$ holomorphic factor
enters $A_{E_2}$ only as a *coefficient module*: both $\bar A$ and
$\bar A_\perp$ live on the same formal symplectic disk
$\widehat{\C^2}_0$, treated **algebraically** as the perfect
Hamiltonian Lie algebra $\C[z_1, z_2] / \C \cdot 1$. There is no
$\E_2^{\mathrm{hol}}$-FA on $\C^2$ in (I-1) ∘ (I-2); the holomorphic
direction is decoupled from the (I-1) ∘ (I-2) composition path.

### §1.2 Where the topological-holomorphic interface enters: only (I-3)

The $\R^k \times \C^2$ cross-mix enters not in (I-1) ∘ (I-2) but in
(I-3) — the Hamiltonian Maurer-Cartan twist
$\alpha = \alpha_{x_i} dx_i + \alpha_{\bar z_j} d\bar z_j$. Its
flatness equation $F_\alpha = 0$ decomposes into three pieces
(`main.tex`:1820, `phase4-exec-Mixed-Dunn-Probe-2026-04-28.md` §6.2):

1. **Topological-topological.**
   $\partial_{x_1} \alpha_{x_2} - \partial_{x_2} \alpha_{x_1}
    + \{\alpha_{x_1}, \alpha_{x_2}\} = 0$ on $\R^2$.
2. **Holomorphic-holomorphic.**
   $\bar\partial_{z_1} \alpha_{\bar z_2} - \bar\partial_{z_2} \alpha_{\bar z_1}
    + \{\alpha_{\bar z_1}, \alpha_{\bar z_2}\} = 0$ on $\C^2$.
3. **Cross.**
   $\partial_{x_i} \alpha_{\bar z_j} - \bar\partial_{z_j} \alpha_{x_i}
    + \{\alpha_{x_i}, \alpha_{\bar z_j}\} = 0$ across $\R^2 \times \C^2$.

Component (1) is the data G1-M2 uses to make the strict
$E_2$-multiplication on $\R^2$ in $\mathcal C_{\mathrm{ML}}$; it is
the topological-topological composition that (I-1) ∘ (I-2) refers to.
Component (2) governs the holomorphic factor on $\C^2$; in the
manuscript, it is realised algebraically by the constant Poisson
bracket on the formal disk (i.e., a degenerate connection in the
sense that $\alpha_{\bar z_j}$ is purely a Beltrami differential
encoding complex-structure data; cf. `main.tex`:1842-1850). Component
(3) is the **only place** where the topological and holomorphic
factors mix, and it is the locus of the operadic mixed-Dunn
obstruction (Mixed-Dunn-Probe O-6.5.3).

**Crucial decoupling fact.** Component (3) appears only in the
*BV-cohomological* identity $F_\alpha = 0$ at the chain level; it is
**not** an operadic equivalence. The Lagrange multiplier $\beta$
makes component (3) BV-exact at the chain level (`main.tex`:1818-1840;
`phase4-exec-Decoupling-Proposition-2026-04-28.md` §2.4). The
*operadic* statement of mixed-Dunn — that
$\E_m^{\mathrm{top}} \otimes \E_n^{\mathrm{hol}} \simeq \E_{m,n}^{\mathrm{mixed}}$
— would be needed to rigidify component (3) into a strict
equivalence at the $(\infty, 2)$-categorical level. The chain-level
closure of Theorem G needs only the BV-cohomological identity, **not**
the operadic equivalence.

### §1.3 Beilinson lens interpretation of the composition

Taking the Beilinson school (1981 localization, 1996 Hitchin) as
methodological foil: the canonical Beilinson move is to **factor a
global flatness statement through a local-to-global descent that
respects stratification**. Here the stratification is

$$
\R \times \{0\} \subset \R^2 \times \{0\} \subset \R^2 \times \C^2
$$

(brane-line ⊂ topological-bulk ⊂ full mixed manifold). The Beilinson
factorisation of $\mathrm{Th}_G$'s chain-level closure runs:

* **Brane-line stratum $\R \times \{0\}$.** The cocycle $\omega$ and
  its image $[\bar c]$ are pulled back to $H^2_{\mathrm{Lie}}(\bar A, \C)$
  (`lem:omega-cocycle`, `main.tex`:284-316); the brane-line BD chiral
  algebra (I-1) supplies the chiral OPE $J_f(z) J_g(w) \sim
  \bar c(f, g) / (z-w)^2 + J_{\{f, g\}}(w)/(z-w) + \cdots$
  (G1-M1 D1, `phase4-exec-G1-M1-BD-chiral-2026-04-28.md` §1.D2).
* **Topological-bulk stratum $\R^2 \times \{0\}$.** The G1-M2
  $E_2$-promotion (I-2) extends (I-1) to a strict $E_2$-multiplication
  via the topological flat-connection 2-form
  $\partial_{x_1} \alpha_{x_2} - \partial_{x_2} \alpha_{x_1} + \{\alpha_{x_1}, \alpha_{x_2}\} = 0$
  (`phase4-exec-G1-M2-E2-promotion-2026-04-28.md` §3.1).
* **Full mixed stratum $\R^2 \times \C^2$.** The (I-3) cross-flatness
  $\partial_{x_i} \alpha_{\bar z_j} - \bar\partial_{z_j} \alpha_{x_i} + \{\alpha_{x_i}, \alpha_{\bar z_j}\} = 0$
  is the only piece that crosses the topological-holomorphic
  interface; at the chain level, it is BV-exact under $\beta$, not
  an operadic equivalence.

**Beilinson conclusion.** The composition (I-1) ∘ (I-2) is
*manifestly stratum-preserving*: it never leaves the topological
factor $\R^2$ at the operadic level. The cross-stratum descent is
relegated to (I-3), where it is supplied as a chain-level identity,
not an operadic equivalence. **Q1 answered: no implicit partial
mixed-Dunn is hidden in (I-1) ∘ (I-2). The decoupling holds.**

### §1.4 Composition lens cross-check

From the Composition lens: do the (I-1) and (I-2) structure maps
compose at the chain / Mayer-Vietoris / Čech level?

* **(I-1) compose with itself (associativity on $\R$).** Strict $E_1$
  associativity on $\R$ via M-1 P4-G2-M1 (Bakalov-Kac Jacobi at depth
  5: 405 instances, 0 failures).
* **(I-2) compose with itself (associativity on $\R^2$).** Strict
  $E_2$ associativity on $\R^2$ in $\mathcal C_{\mathrm{ML}}$ via
  Lurie HA §5.5.4.16 + LC translation invariance.
* **(I-1) ∘ (I-2) (compatibility of brane-line $E_1$ with bulk $E_2$).**
  Strict by the Lurie 5.5.4.10 LCFA equivalence on $\R$
  (locally-constant FA on $\R$ ≃ $E_1$-algebra in
  $\Alg_{E_1}(\mathcal C_{\mathrm{ML}})$, the inner $E_1$ of the Dunn
  decomposition $E_2 \simeq E_1 \otimes E_1$). The brane-line $E_1$
  $A_{\mathrm{brane}}$ inscribes as the *trivial-outer-$E_1$* element
  of $\Alg_{E_1}(\Alg_{E_1}(\mathcal C_{\mathrm{ML}}))$; this is a
  well-defined object of the doubly-iterated $E_1$-category, and its
  enhancement to a non-trivial outer $E_1$ via the transverse
  $\bar A_\perp$ Hamiltonian connection $\alpha_{x_2}$ is supplied by
  (I-2) and the topological flat-connection 2-form.

**Composition conclusion.** The (I-1) ∘ (I-2) composition is strict
at the cohomological level inside $\mathcal C_{\mathrm{ML}}$,
supplied by the Lurie 5.5.4.10 LCFA equivalence on $\R$, and respects
the stratum filtration. **No partial mixed-Dunn is invoked.**

### §1.5 Verdict for Q1

**(V-Q1) The composition (I-1) ∘ (I-2) does NOT cross the
topological-holomorphic interface.** The G1-M2 $E_2$-promotion uses
two $\R$ factors of $\R^2$ via Lurie's Dunn additivity in
$\mathcal C_{\mathrm{ML}}$; both factors are topological. The
$\C^2$ direction enters only as an algebraic coefficient module on
the formal disk. The cross-stratum mixing is exclusively (I-3) at
the chain level. **No implicit partial mixed-Dunn obstruction is
hidden in the (I-1) ∘ (I-2) composition.** Wave-4 #105's verdict
survives this probe.

**Sharpening recommendation.** The wave-4 inscription at
`theorem-lanes.tex` lines 453-455 should record explicitly that
the (I-2) $E_2$-multiplication runs **inside the topological factor
$\R^2$** (not crossing into $\C^2$), so that the reader sees the
stratum-preserving composition path on the surface of the
manuscript. Drafted in §7.

---

## §2. Probe Q2 — BD §3.4.10-11 chiral axioms (Ax.1)-(Ax.5): which are implicitly used?

The pressure question. BD §3.4.1 chiral axioms (Ax.1)-(Ax.5)
(symmetry, chiral Jacobi, differential-compatibility,
locally-constant-topological, locally-constant-holomorphic) describe
the chiral algebra structure on a single curve; BD §3.4.10-11 lifts
to the product manifold. Wave-4 #105 §3.4 states that the partial
chiral product (HTPCP) supplies (Ax.1)-(Ax.4) at the chain /
BV-cohomological level on the brane-line stratum and replaces (Ax.5)
+ cross-direction operadic glue with the Maurer-Cartan twist. The
probe asks: is BD chiral Jacobi (Ax.4) — wait, (Ax.4) is
locally-constant-topological; (Ax.2) is chiral Jacobi — implicitly
used at higher depth than what (I-1) verifies, or on the product
manifold rather than on $\R$?

(Note on numbering. In BD §3.4.1, the chiral axioms are: (Ax.1)
symmetry, (Ax.2) chiral Jacobi / associativity, (Ax.3) differential
compatibility, (Ax.4) locally-constant-topological, (Ax.5)
locally-constant-holomorphic. The W5-A6 task asks specifically about
chiral Jacobi, which is (Ax.2) in `BD04` / Chiral-Product-Audit
numbering. Treating "(Ax.4)" in the probe as a typographical slip for
"chiral Jacobi (Ax.2)".)

### §2.1 What chiral Jacobi G1-M1 verifies

From `phase4-exec-G1-M1-BD-chiral-2026-04-28.md` §1.D1:

> The Bakalov-Kac axioms (`BK03`) — $\C[\lambda]$-linearity,
> sesquilinearity $Y(\partial a, \lambda) = -\lambda Y(a, \lambda)$,
> quasi-commutativity $Y(a, \lambda) b = -Y(b, -\lambda - \partial) a$,
> Leibniz on the commutative product, and Jacobi
> $[Y(a, \lambda), Y(b, \mu)] = Y([Y(a, \lambda) b], \lambda + \mu)$
> — hold on linear and quadratic generators by the explicit
> verification of P4-G2-M1
> (`phase4-exec-module-lambda-bracket-2026-04-28.md` §3.4, §4.2):
> **256 quasi-commutativity instances + 405 Jacobi instances
> (9 generators × 81 pairs × 5 vacuum levels) at zero failures**.

This is BD chiral Jacobi (Ax.2) **on $\R$ at the linear / quadratic
generator level, depth 5 (i.e., 5 vacuum levels)**. The 405
Jacobi instances cover all triples $(f, g, h)$ on linear / quadratic
generators of $\bar A$ at vacuum levels 0 through 4. This is enough
for the M-1 deliverable.

### §2.2 What chiral Jacobi Theorem G's chain-level proof uses

From `main.tex`:343-361 (proof of `thm:u1-center-anomaly`):

> Central extensions of $\bar A$ by $\C$ are classified by
> $H^2_{\mathrm{Lie}}(\bar A, \C)$ via the standard Chevalley-Eilenberg
> argument. The exact sequence above is a central extension because the
> constant Hamiltonian $1 \in \mathfrak h_{\mathrm{poly}}$ has zero
> Hamiltonian vector field, so $\C\cdot 1$ is central in
> $\mathfrak h_{\mathrm{poly}}$. The class of this extension is the
> obstruction to a Lie-algebra splitting; computing the class on
> monomial generators...

The proof invokes **classical Lie-algebra Jacobi for $\bar A$ in the
algebraic Chevalley-Eilenberg complex of `lem:omega-cocycle`'s proof
at `main.tex`:301-308**:

> The Jacobi identity for $\{-, -\}$ on $\mathfrak h_{\mathrm{poly}}$
> asserts $\{f, \{g, h\}\} + \{g, \{h, f\}\} + \{h, \{f, g\}\} = 0$,
> and projecting each summand to its constant Taylor coefficient gives
> the cocycle identity
> $\omega(f, \{g, h\}) + \omega(g, \{h, f\}) + \omega(h, \{f, g\}) = 0.$

This is **classical Lie Jacobi**, supplied by the Poisson algebra
structure on $\C[z_1, z_2]$, **not** BD chiral Jacobi at any depth on
any curve.

### §2.3 Distinguishing three Jacobis

The W5-A6 probe pressure-tests the conflation of three distinct
Jacobi conditions. We separate them:

**(J-1) Classical Lie-algebra Jacobi for $\bar A$.** The Poisson
bracket on $\C[z_1, z_2]$ satisfies $\{f, \{g, h\}\} + \cdots = 0$
classically; this is what `lem:omega-cocycle`'s cocycle proof uses.
**Status: classical, supplied algebraically.**

**(J-2) BD chiral Jacobi (Ax.2) on $\R$ at depth 5.** The
$\lambda$-bracket on $\mathcal A_{\mathrm{fact}}$ satisfies the
Bakalov-Kac chiral Jacobi identity at depth 5 on linear / quadratic
generators. **Status: G1-M1 D1 verified at 405 instances /
0 failures.**

**(J-3) BD chiral Jacobi (Ax.2) on $\R^2 \times \C^2$ at the operadic
level (BD §3.4.11 axiom on the product manifold).** The chiral
cobracket on $\Delta^*(\mathcal F \boxtimes \mathcal G)$ satisfying
the chiral axiom on the 6-real-dim mixed manifold. **Status: open
at the operadic level (Mixed-Dunn-Probe O-6.5.3); BV-cohomologically
true via $F_\alpha = 0$ exactness (Chiral-Product-Audit (V-1)).**

The Theorem G chain-level proof uses **(J-1) only**. The
brane-line image image of $[\bar c]$ (`thm:u1-center-anomaly-open`
at `main.tex`:354-393) uses (J-1) on $\bar A$ via the boundary
evaluation map $f \mapsto \mathrm{Tr}\, f(\phi_1, \phi_2)$, with the
factorization-algebra structure on the brane line supplied by (I-1),
which **as a side-effect implicitly inherits (J-2)**. Theorem G's
explicit proof never invokes (J-2) or (J-3) directly.

### §2.4 Wave-4 #105's treatment of chiral Jacobi

Wave-4 #105 §2.5 (Step 5 of the proof outline) says:

> **The composition closes** because (i) the Lie-cohomology cocycle
> $\omega$ is computed on the **algebraic** Lie algebra $\bar A$
> (no global descent needed), (ii) the closed-open coupling
> factorizes through the brane-line stratum (where (I-1) supplies
> $E_1$ and (I-2) supplies $E_2$ in $\mathcal C_{\mathrm{ML}}$),
> and (iii) the cross-direction chain-level identity is supplied
> by $F_\alpha = 0$ as a Maurer-Cartan twist.

This is correct but elliptic on the Jacobi distinction. **The
Beilinson + Composition interpretation is:** (i) uses (J-1) (classical
Lie Jacobi), (ii) uses (J-2) inside (I-1) and the Lurie 5.5.4.16
strict $E_2$ inside (I-2), (iii) avoids (J-3) by replacing the
operadic chiral axiom on the product manifold with the chain-level
Maurer-Cartan identity.

**Q2 answered.** Theorem G's chain-level proof requires only (J-1)
classical Lie Jacobi for $\bar A$ in the algebraic CE complex.
(I-1) implicitly invokes (J-2) chiral Jacobi at depth 5 on $\R$ as a
*side input* needed to make the brane-line factorization a BD chiral
algebra; this is verified at G1-M1. (J-3) chiral Jacobi on the
product manifold is **not** invoked. **The decoupling holds with
(J-3) outside the proof path.**

### §2.5 Other BD axioms (Ax.1), (Ax.3), (Ax.4), (Ax.5)

Brief checks:

* **(Ax.1) symmetry.** Used in (I-1) at the brane-line linear-generator
  level (i.e., antisymmetry of the Poisson bracket on $\bar A$ projects
  to antisymmetry of $\omega$ in `lem:omega-cocycle` proof, line 307-308:
  "Antisymmetry $\omega(g, f) = -\omega(f, g)$ is inherited from
  antisymmetry of the bracket"). Classical.
* **(Ax.3) differential compatibility.** Theorem G's proof uses
  $\omega = \delta\eta$ on $\mathfrak h_{\mathrm{poly}}$ (which is
  the CE differential acting on the cochain $\eta$);
  $H^2_{\mathrm{Lie}}$ is computed by the CE differential on cochains.
  **Classical CE differential on $\bar A$.**
* **(Ax.4) locally-constant-topological on $\R^2$.** Used by (I-2)
  G1-M2 at the LC translation-invariance level. Inside the
  topological factor only.
* **(Ax.5) locally-constant-holomorphic on $\C^2$.** Wave-4 #105 §3.4
  records that this is replaced by the algebraic $\bar A$-action on
  $\widehat{\C^2}_0$ (which is *not* an $\E_2^{\mathrm{hol}}$-FA in
  the Williams §3 sense). **Ax.5 NOT invoked at the operadic level
  on $\C^2$.**

**All five BD axioms are accounted for in wave-4 #105. The
decoupling holds.**

---

## §3. Probe Q3 — Does the locally-constant cosheaf on $\Omega^\bullet_c(I) \otimes \mathfrak h$ require bulk Čech descent on $\R^2 \times \C^2$?

The pressure question. (I-1)'s brane-line factorization
$\mathfrak h_I = \Omega^\bullet_c(I) \widehat\otimes \mathfrak h$
on $\R$ is a locally-constant cosheaf (G1-M1 D3). The probe asks: in
the manuscript's setting where the brane line $L = \R \times \{0\}
\times \{0\}$ embeds in the 6-real-dim space $\R^2 \times \C^2$, does
the cosheaf condition factor through bulk Čech covers on
$\R^2 \times \C^2$ that wave-4 #105 missed?

### §3.1 The cosheaf condition in (I-1)

From G1-M1 D3, the cosheaf condition on $\mathfrak h_I$ is:

* Source category: open subsets $I \subset \R$ ordered by inclusion.
* Functor: $I \mapsto \mathfrak h_I = \Omega^\bullet_c(I) \widehat\otimes \mathfrak h$
  (or its CE-cochain partner $\mathcal A_{\mathrm{fact}}(I)$).
* Cosheaf axiom: for any cover $\{I_\alpha\}$ of $I$, the natural
  map $\mathrm{colim}_{\Delta^{op}} \mathrm{Cech}_\bullet(\{I_\alpha\}) \to \mathfrak h_I$
  is a quasi-isomorphism (in the $\mathcal C_{\mathrm{ML}}$ sense).

This is a **cosheaf on $\R$ alone**. The 6-real-dim manifold
$\R^2 \times \C^2$ does not enter.

### §3.2 Bulk Čech direction: M-37 / R-03 obligation, NOT in chain-level proof

From `phase4-exec-G1-M1-BD-chiral-2026-04-28.md` §1.D5:

> The transverse Mittag-Leffler resolution (I-4), W3-W11-05 language:
> *the genuinely hard ingredient is exactly the Ran-space descent of
> the BD chiral algebra*. In BD §3.4.10-11 language, this is the
> chiral-cobracket on $\Delta^*(\mathcal A \boxtimes \mathcal A)$
> satisfying the chiral axiom on $\R^2 \times \C^2$ (rather than on
> the brane-line factor alone). This is the Avenue (D) of P4-G1-T3
> (`phase4-G1-weiss-product-2026-04-28.md` §T3.D).

**This is the Weiss-cosheaf descent on $\R^2 \times \C^2$ at every
Weiss cover: (W-2D) of W3-W9.** It is the M-37 / R-03 obligation,
**explicitly not a hypothesis of Theorem G's chain-level closure**.

### §3.3 Theorem G's actual descent direction

Theorem G's proof at `main.tex`:343-361 invokes:

* The classical Lie-algebra Jacobi on $\bar A$ (no descent).
* The CE cochain differential $\delta$ on $C^\bullet_{\mathrm{Lie}}(\bar A, \C)$
  computing $H^2_{\mathrm{Lie}}(\bar A, \C)$ (no descent).
* The classification of central extensions by $H^2$ (no descent).
* The boundary evaluation map $f \mapsto \mathrm{Tr}\, f(\phi_1, \phi_2)$
  in `thm:u1-center-anomaly-open` (algebraic, finite-$N$, no descent).

**No cosheaf or Čech descent appears in Theorem G's proof.** The
brane-line factorization (I-1) appears only in
`thm:u1-center-anomaly-open`'s lift of $[\bar c]$ to the brane
algebra; there, the cosheaf descent runs on **$\mathrm{Ran}(\R)$** —
not on $\mathrm{Ran}(\R^2 \times \C^2)$.

### §3.4 Beilinson lens interpretation

The Beilinson school's localisation picture (BB81; BD96 Hitchin) is:
**a global flatness statement on a moduli space descends to a
$\mathcal D$-module on a stratification respecting the local
Hamiltonians**. In our setting:

* Global object: $\mathrm{Th}_G$ (a chain-level cocycle identity).
* Stratification: brane-line ⊂ topological-bulk ⊂ mixed-bulk.
* Local Hamiltonian: $\bar A = \C[z_1, z_2] / \C \cdot 1$ on
  $\widehat{\C^2}_0$.

The Beilinson factorization runs through the brane-line stratum
$\R \subset \R^2 \times \C^2$; the descent is on $\mathrm{Ran}(\R)$,
not on $\mathrm{Ran}(\R^2 \times \C^2)$.

The **bulk Čech descent on $\R^2 \times \C^2$** would be the
Beilinson-Drinfeld §3.4.10-11 chiral product on the product manifold,
which Mixed-Dunn-Probe identifies as the open Phase-5 obligation. The
chain-level proof avoids this descent by living on the brane-line
stratum.

### §3.5 Verdict for Q3

**(V-Q3) The locally-constant cosheaf direction on
$\Omega^\bullet_c(I) \otimes \mathfrak h$ does NOT require bulk
Čech descent on $\R^2 \times \C^2$.** The cosheaf is on $\R$ alone;
its descent is on $\mathrm{Ran}(\R)$. Bulk descent on
$\mathrm{Ran}(\R^2 \times \C^2)$ is the M-37 / R-03 obligation,
*not* invoked by Theorem G's proof. **Wave-4 #105's verdict is
correct.**

**Sharpening recommendation.** The wave-4 inscription at
`theorem-lanes.tex` lines 453-455 should record explicitly the
*surface direction of descent*: the cosheaf condition is on $\R$
(brane-line $\mathrm{Ran}$), not on $\R^2 \times \C^2$ (bulk
$\mathrm{Ran}$). Drafted in §7.

---

## §4. Probe Q4 — CE chains versus cochains: does the inscription preserve the cochain direction?

The pressure question. The platonic ideal plan §3 Theorem C uses
$C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak g)$ — CE cochains
(superscript $\bullet$). The wave-4 #105 inscription at
`theorem-lanes.tex` lines 453-455 cites "the algebraic Lie-cohomology
computation of $[\bar c]$". The probe asks: does the inscription
slip into chains (subscript $\bullet$, covariant) when it should be
in cochains (superscript $\bullet$, contravariant), or vice versa?

### §4.1 The native direction of `thm:u1-center-anomaly`

From `main.tex`:284-352, Theorem G is stated and proved in **CE
cochains**:

* `lem:omega-cocycle` (line 293): "$\omega$ is a Lie 2-cocycle on
  $\mathfrak h_{\mathrm{poly}}$." — The 2-**cocycle** is a CE 2-cochain
  $C^2_{\mathrm{Lie}}(\mathfrak h_{\mathrm{poly}}, \C) \ni \omega$ in
  the *kernel* of $\delta: C^2 \to C^3$.
* `thm:u1-center-anomaly` (line 327): "$[\bar c] \in
  H^2_{\mathrm{Lie}}(\bar A, \C)$ is the scalar-axis obstruction
  class". — $H^2_{\mathrm{Lie}}$ is **Lie-algebra cohomology**, not
  homology. Cohomology = cochains modulo coboundary.
* Proof at line 343: "Central extensions of $\bar A$ by $\C$ are
  classified by $H^2_{\mathrm{Lie}}(\bar A, \C)$". — Standard CE
  classification by 2-cohomology.

**The native direction of Theorem G is CE cochains.** This is
contravariant: maps go $C^p \to C^{p+1}$ with $\delta$ raising
degree.

### §4.2 The native direction of (I-1) brane-line factorization

From G1-M1 D1 and the surrounding manuscript text
(`main.tex`:1996-2046, `thm:open-closed-derived-center-factorization`):

* The brane-line factorization centre is
  $\mathcal A_{\mathrm{fact}}(I) = C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak g_I)$.
  — **Cochain.**
* `theorem-lanes.tex` Lane 3 (`thm:lane-ce-pv-center`, lines 96-148):
  "$C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak g)
  \xrightarrow{\sim} \mathrm{PV}(\widehat{\mathbf S}_{\mathrm{Tate}}(\mathfrak h)) \simeq Z^{P_0}_{\mathrm{red, Ham}}$".
  — **Cochain → polyvector**.
* The platonic ideal plan §3 Theorem C: "$C^\bullet_{\mathrm{CE,cont}}(\mathfrak g)
  \cong \mathrm{PV}(S(\mathfrak h)) \simeq Z^{P_0}_{\mathrm{fact}}(S(\mathfrak h))$".
  — **Cochain.**

**The native direction of (I-1) and its CE/PV partner is also CE
cochains.**

### §4.3 The native direction of FA-on-Ran($X$) in BD §3.4.5

A subtle point. BD §3.4.5 (`BD04`, page 165) states the equivalence

> *chiral algebra on smooth complex curve $X$* ≃ *factorization
> algebra on $\mathrm{Ran}(X)$*.

The factorization algebra side, in Lurie HA Theorem 5.5.4.10 + CG §6.4
formulation, is *covariant* on the open category (i.e., a *cosheaf*,
not a sheaf): structure maps go from finer covers to coarser opens.
The chiral algebra side is *contravariant* on $\mathcal D$-modules
(a sheaf with $\mathcal D_X$-action). The BD §3.4.5 equivalence
*matches* a covariant cosheaf on the Ran space with a contravariant
$\mathcal D$-module on $X$ via the diagonal map and Verdier-duality
adjunction.

**In the manuscript's setting**, the brane-line factorization
$\mathcal A_{\mathrm{fact}}(I) = C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak g_I)$
is a **cosheaf in $I$** (covariant): if $I_1 \subset I_2$, then
$\mathcal A_{\mathrm{fact}}(I_1) \to \mathcal A_{\mathrm{fact}}(I_2)$
is the *extension by zero* on $\Omega^\bullet_c$ (G1-M1 D3). The CE
*cochain* differential acts in each $\mathcal A_{\mathrm{fact}}(I)$ in
the cohomological direction (raising the CE degree).

**So the FA on $\mathrm{Ran}(\R)$ is covariant in $I$ but cochain
(contravariant) in CE degree**, with no slippage between these
distinct directions: the cosheaf direction and the CE direction are
*orthogonal* in the bigraded structure
$\mathcal A_{\mathrm{fact}}(I)^{p, q} = (\Omega^p_c(I) \widehat\otimes \mathfrak h^{q})$
or its CE companion.

### §4.4 The wave-4 #105 inscription wording

The wave-4 #105 inscription text (Decoupling-Proposition §6.1) reads:

> (ii) the algebraic Lie-cohomology computation of $[\bar c]$ on the
> reduced Hamiltonian Lie algebra $\bar A = \mathfrak h_{\mathrm{poly}} / \C \cdot 1$,
> supplied by Lemma~\ref{lem:omega-cocycle} and the central-extension
> classification.

**"Lie-cohomology"** is the cochain direction (cohomology, not
homology). The inscription is consistent.

> (i) the brane-line factorization $\mathfrak h_I = \Omega^\bullet_c(I)
> \widehat\otimes \mathfrak h$ with extension-by-zero functoriality
> and disjoint-support $P_0$-bracket locality, supplied by
> Theorem~\ref{thm:lane-factorization-current};

**"Extension-by-zero functoriality"** is the cosheaf direction
(covariant in $I$). The cochain direction is implicit in the
"$P_0$-bracket locality" via the Schouten / CE differential.

> (iii) the chain-level identity $\delta\eta = \omega$ on
> $\mathfrak h_{\mathrm{poly}}$.

**"$\delta\eta = \omega$"** uses $\delta$ in the CE *cochain*
direction (raising degree from 1-cochain $\eta$ to 2-cocycle
$\omega$). The phrase "chain-level identity" is colloquial here —
"chain level" in BV / factorization-algebra parlance means *before
passing to cohomology*, so the identity is a chain-level (i.e.,
cocycle-level) cochain identity. **This is consistent.** The word
"chain" in "chain-level identity" should not be read as "homological"
chain; it is the BV usage = "before cohomology".

### §4.5 The platonic-ideal Theorem C direction

The platonic ideal plan §3 Theorem C states:

> $\Phi: C^\bullet_{\mathrm{CE,cont}}(\mathfrak g) \xrightarrow{\sim}
> \mathrm{PV}(A_\partial) \simeq Z^{P_0}_{\mathrm{fact}}(A_\partial)$.

Both sides are **cochains** (superscript $\bullet$): CE cochains on
the left, polyvector field cochains on the right. The Schouten
differential $d_\pi$ raises CE-cochain degree by 1, matching $\delta$
on the left. **All directions agree.**

### §4.6 Verdict for Q4

**(V-Q4) The wave-4 #105 inscription preserves the cochain
direction.** No slippage from cochains into chains is detected. The
phrase "chain-level identity $\delta \eta = \omega$" is the standard
BV usage of "chain" = "pre-cohomology", not the homological direction.

**Editorial sharpening.** The inscription text at
`theorem-lanes.tex` lines 453-455 could replace "the algebraic
Lie-cohomology computation of $[\bar c]$ on the reduced Hamiltonian
Lie algebra $\bar A$" with the slightly more explicit "the
algebraic Lie-algebra cohomology $H^2_{\mathrm{Lie}}(\bar A, \C)$
computed at the cochain level on the reduced Hamiltonian Lie
algebra $\bar A$" to record the cochain direction unambiguously.
This is editorial only; no proof is changed.

### §4.7 Cross-volume firewall implication

A corollary from the chain/cochain distinction: **the
manuscript-internal chain-level identity does NOT slip into a
chain-level (homological) statement on a global Ran space** that
might tempt a cross-volume transfer. The classical cocycle
$\omega$ is in CE 2-cochains; its image in homology under the
universal coefficient theorem would be a class in
$H_2^{\mathrm{Lie}}(\bar A, \C^*)$ (with the dual coefficient
module). No such homological transfer is asserted. The cross-volume
firewall (`claim-strength-ledger.tex` lines 130-140;
`lem:no-formal-disk-transfer`) is preserved.

---

## §5. Beilinson school methodological foil: BB81 + BD96

We use Beilinson-Bernstein 1981 and Beilinson-Drinfeld 1996 as
**methodological foil** to triangulate the wave-4 #105 closure.

### §5.1 BB81 localization as decoupling prototype

The Beilinson-Bernstein 1981 localization theorem
(`BB81`, C.R. Acad. Sci. Paris 292) reads, schematically:

> $\mathcal D$-modules on the flag variety $G/B$ ≃
> $\mathfrak g$-modules at the central character.

This is a **local-to-global decoupling**: the global object
($\mathcal D$-module on $G/B$) is built from a *local* algebraic
structure ($\mathfrak g$-representation) at a *single point* (the
central character). The descent passes through the open Bruhat
stratification.

**Analogy.** Our setting:
* Global object: factorization algebra on $\mathrm{Ran}(\R^2 \times \C^2)$.
* Local object: $\bar A$-action on $\widehat{\C^2}_0$ at the formal
  symplectic disk.
* Stratification: brane-line $L = \R \times \{0\} \times \{0\}$
  ⊂ topological-bulk $\R^2 \times \{0\}$ ⊂ full mixed-bulk.

The Beilinson-Bernstein-style decoupling result for our setting is:
**Theorem G's chain-level closure descends to the algebraic
$\bar A$-action on $\widehat{\C^2}_0$ via the brane-line stratum,
without invoking the global factorization-algebra structure on
$\mathrm{Ran}(\R^2 \times \C^2)$.** This is the wave-4 #105 closure
formulated as a Beilinson-Bernstein-style decoupling.

### §5.2 BD96 Hitchin connection as flatness foil

The Beilinson-Drinfeld 1996 Hitchin connection (`BD96`, preprint;
later Frenkel-Ben-Zvi 2004 §16) reads:

> The Hitchin connection is a flat connection on the bundle of
> conformal blocks over the moduli of Riemann surfaces with marked
> points; it descends from a Maurer-Cartan element in a chiral algebra
> at the marked points.

The flat connection is a *global* object on a moduli space; the MC
element is *local* at the marked points. The descent uses the
$\mathcal D$-module structure on conformal blocks.

**Analogy.** Our (I-3) Hamiltonian Maurer-Cartan twist
$\alpha$ with $F_\alpha = 0$ is the precise analogue of the BD96
Hitchin MC element: a flat connection on the bundle of factorization
algebras over $\R^2 \times \C^2$ descending to a chain-level
Maurer-Cartan datum in the (I-1) ∘ (I-2) brane-line $E_2$ structure.
The BD96 descent passes through the chiral $\lambda$-bracket on
conformal blocks; our descent passes through the $P_0$-bracket on
$\bar A$ in the unreduced BV complex with Lagrange multiplier
$\beta$.

**Crucial distinction.** BD96's Hitchin connection lives on a moduli
of *complex curves* with marked points, where BD §3.4.10-11 chiral
products on the product manifold are operadically formulated (because
both factors are smooth complex curves). Our setting has $\R^2$
topological + $\C^2$ holomorphic; the "Hitchin-style" (I-3) lives at
the chain level, not at the operadic level, because the operadic
mixed-Dunn equivalence on $\R^k \times \C^n$ is exactly what is
unproved (Mixed-Dunn-Probe O-6.5.3).

**Foil verdict.** The BD96 prototype suggests the (I-3) Maurer-Cartan
twist is *the* correct manuscript-internal device for the
cross-direction chain-level descent. Wave-4 #105's verdict is
methodologically aligned with the Beilinson-Drinfeld 1996 prototype.

---

## §6. Composition lens summary: do (I-1) + (I-2) + (I-3) genuinely close?

We synthesize the four probe answers under the Composition lens and
record the chain-level closure path.

### §6.1 The closure diagram

The Theorem G chain-level closure, with the four probe answers
incorporated, traces:

```
[Classical Lie Jacobi on bar A]                          (J-1)
        |
        v
[CE cochain identity delta eta = omega on h_poly]        (cochain Q4)
        |
        v
[H^2_Lie(bar A, C) classifies central extensions]        (Q4 cochain)
        |
        +--> [bar c] = obstruction class                 (closes Th_G closed-side)
        |
        v
[Brane-line image: f -> Tr f(phi_1, phi_2)]              (open-side)
        |
        v
[(I-1) BD chiral algebra on R + (J-2) chiral Jacobi at depth 5]
        |  via Lurie 5.5.4.10 LCFA on R
        v
[(I-2) E_2 in C_ML on R^2 via Lurie 5.5.4.16 + LC]       (Q1 topological-only)
        |  via cosheaf direction on Ran(R), NOT bulk Ran (Q3)
        v
[Cochain CE/PV identification thm:open-closed-derived-center]
        |
        v
[(I-3) F_alpha = 0 cross-direction MC twist via beta]    (BV-cohomological,
                                                          NOT operadic mixed-Dunn)
        |
        v
[Theorem G chain-level closure CLOSED]
```

Each step is local; each is supplied by a manuscript-internal
mechanism (no Phase-5 dependency). The composition is strict at the
chain / BV-cohomological level.

### §6.2 What the probe doesn't change

* (V-Q1) (I-1) ∘ (I-2) is purely topological (inside $\R^2$); no
  partial mixed-Dunn.
* (V-Q2) (J-3) chiral Jacobi on the product manifold is NOT
  invoked; (J-1) and (J-2) suffice.
* (V-Q3) Cosheaf direction is on $\mathrm{Ran}(\R)$, not on
  $\mathrm{Ran}(\R^2 \times \C^2)$.
* (V-Q4) Cochain direction is preserved throughout; no slippage.

**Wave-4 #105 closure stands.**

### §6.3 What the probe sharpens

Three editorial sharpenings, all additive, none gating:

* **(SH-1)** Record explicitly that (I-2)'s $E_2$-multiplication runs
  *inside the topological factor* $\R^2$, not crossing into $\C^2$.
* **(SH-2)** Record explicitly that the cosheaf descent runs on
  $\mathrm{Ran}(\R)$ (single brane-line), not on
  $\mathrm{Ran}(\R^2 \times \C^2)$ (full mixed manifold).
* **(SH-3)** Replace "the algebraic Lie-cohomology computation of
  $[\bar c]$" with "the algebraic Lie-algebra cohomology
  $H^2_{\mathrm{Lie}}(\bar A, \C)$ at the cochain level" for cochain
  direction unambiguity.

Drafted in §7.

---

## §7. Sharpened inscription block (additive only, no proof change)

Recommended replacement for the wave-4 #105 inscription text at
`theorem-lanes.tex` lines 453-455 (proposed, NOT inscribed):

```latex
  \emph{Decoupling.} The chain-level closure of
  Theorem~\ref{thm:u1-center-anomaly} requires exactly:
  (i) the brane-line factorization
  \(\mathfrak h_I=\Omega^\bullet_c(I)\widehat\otimes\mathfrak h\)
  with extension-by-zero functoriality (cosheaf direction on
  \(\mathrm{Ran}(\R)\), single brane line) and disjoint-support
  \(P_0\)-bracket locality, supplied by
  Theorem~\ref{thm:lane-factorization-current}; (ii) the
  algebraic Lie-algebra cohomology
  \(H^2_{\mathrm{Lie}}(\bar A,\C)\) at the cochain level on the
  reduced Hamiltonian Lie algebra
  \(\bar A=\mathfrak h_{\mathrm{poly}}/\C\cdot1\), supplied by
  Lemma~\ref{lem:omega-cocycle} and the central-extension classification;
  and (iii) the cochain identity \(\delta\eta=\omega\) on
  \(\mathfrak h_{\mathrm{poly}}\) at the CE cochain level.
  No operadic chiral product on the 6-real-dimensional mixed
  manifold \(\R^2\times\C^2\) is invoked: in particular, no full
  Beilinson--Drinfeld chiral product axiom on the product manifold,
  no \(\mathbb E_m^{\mathrm{top}}\otimes\mathbb E_n^{\mathrm{hol}}
  \simeq\mathbb E_{m,n}^{\mathrm{mixed}}\) operadic equivalence, and
  no holomorphic factorization-algebra structure on \(\C^2\) beyond
  the algebraic action of \(\bar A\) on the formal symplectic disk
  \((\widehat{\C^2}_0,dz_1\wedge dz_2)\) enters the chain-level proof.
  The bulk Hamiltonian-BF data
  \(\alpha=\alpha_{x_i}dx_i+\alpha_{\bar z_j}d\bar z^j\) of the
  manuscript's BF action with flatness \(F_\alpha=0\) supplies any
  cross-direction chain-level identity required by the closed side as
  a Maurer--Cartan twist enforced by the Lagrange multiplier
  \(\beta\); the topological-topological component of \(F_\alpha=0\)
  glues the brane-line and transverse \(\R\) directions inside
  \(\R^2\) into the strict \(E_2\)-multiplication via Lurie HA
  \S5.5.4.16, while the topological-holomorphic cross component
  enters only as the BV-cohomological identity
  \(\partial_{x_i}\alpha_{\bar z_j}-\bar\partial_{z_j}\alpha_{x_i}+\{\alpha_{x_i},\alpha_{\bar z_j}\}=0\)
  trivialized by the \(\beta\)-multiplier coboundary, not as an
  operadic equivalence.
```

This is a **+18-line replacement** (vs the existing wave-4 #105
+11-line block), adding three sharpenings:

* **(SH-1)** "the topological-topological component of $F_\alpha = 0$
  glues the brane-line and transverse $\R$ directions inside $\R^2$
  into the strict $E_2$-multiplication via Lurie HA §5.5.4.16".
* **(SH-2)** "(cosheaf direction on $\mathrm{Ran}(\R)$, single brane
  line)".
* **(SH-3)** "the algebraic Lie-algebra cohomology
  $H^2_{\mathrm{Lie}}(\bar A, \C)$ at the cochain level".

All editorial. No proof changed. Net inscription delta:
**+18 lines** (vs the wave-4 #105 base of +11 lines): **+7 lines
incremental**.

---

## §8. Verdict & severity

**(V-final) Decoupling holds; certify with three editorial
sharpenings.**

The wave-4 #105 P4-Decoupling-Proposition closure **survives the
Beilinson + Composition pressure test**:

* **Q1 (composition crossing topological-holomorphic interface):
  no slip detected.** The (I-1) ∘ (I-2) composition runs inside the
  topological factor $\R^2$ via Lurie's Dunn additivity in
  $\mathcal C_{\mathrm{ML}}$, with both $\R$ factors topological. The
  cross-direction enters only via (I-3) at the chain level.
* **Q2 (BD chiral Jacobi (Ax.2) at higher depth or on product
  manifold): no slip detected.** Theorem G uses classical Lie
  Jacobi (J-1) on $\bar A$; the brane-line image inherits BD chiral
  Jacobi at depth 5 (J-2) from (I-1); the operadic chiral Jacobi
  (J-3) on the product manifold is NOT invoked.
* **Q3 (locally-constant cosheaf factoring through bulk Čech): no
  slip detected.** The cosheaf descent is on $\mathrm{Ran}(\R)$;
  bulk descent on $\mathrm{Ran}(\R^2 \times \C^2)$ is the M-37 / R-03
  obligation, not used.
* **Q4 (CE chains vs cochains): no slip detected.** All directions
  are cochain (cohomology); the inscription is consistent.

**Severity: 0 (clean / certified).** No new Phase-5 obligations.

**Recommended sharpenings (editorial only, no proof change).**

* (SH-1) Topological-topological glue inside $\R^2$ explicit.
* (SH-2) Cosheaf direction on $\mathrm{Ran}(\R)$ explicit.
* (SH-3) Lie-algebra cohomology at cochain level explicit.

Drafted as a +18-line block in §7 (vs wave-4 #105's +11-line base);
**+7 lines incremental**, optional, additive only.

**Inscription delta (cumulative, with #105 base + W5-A6 sharpenings):**
+7 lines beyond wave-4 #105 closure. The base wave-4 #105 closure
remains publication-grade without the W5-A6 sharpenings; the W5-A6
sharpenings are an **optional editorial improvement**.

---

## Appendix A — Provenance

* **Lens.** Beilinson + Composition. Beilinson primary
  (sheaf-theoretic, BB81 / BD96 methodological foil). Composition
  secondary (Mayer-Vietoris / Čech across the (I-1)+(I-2)+(I-3)
  triangulation).
* **Inputs cited.** All listed at the report head; no fresh PDF
  inscription.
* **Authorship.** Raeez Lorgat. No AI attribution.
* **Date.** 2026-04-28.
* **Phase.** 4 EXEC, attack-heal-swarm Wave 5 (server rate-limit relaunch).
* **Mode.** Proposal-only. No git commits. No manuscript TeX
  edits. Writable surface restricted to this report file and the
  ledger summary append.

End of W5-A6 report.
