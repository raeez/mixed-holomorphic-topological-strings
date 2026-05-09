# Wave-3 W8 — Polyakov + Composition Lens

**Author.** Raeez Lorgat. **Date.** 2026-04-28.
**Lens.** Polyakov (scaling, renormalization, anomaly, physical
dimension, path-integral sanity) + Composition (associativity,
coherence, transactionality of local-to-global passages).
**Mode.** Proposal-only. Master ledger schema; IDs prefix `W3-W8-`.
**Mission.** Stress-test the regulator coherence and BV/CE composition
associativity through Polyakov + Composition, against the Wave-2
declared stable core and the Wave-3 W6 (Costello+Composition)
sharpenings. Independent of W2 (Gaiotto / M-31), W5 (Kazhdan / Weiss
defect), W6 (Costello / C₂(W)-q gating); cross-check, do not import.

**Inputs read.**
`reconstitution/attack-heal-platonic-2026-04-28.md` §M-26 to §M-35
(master ledger from Wave 2);
`reconstitution/wave2-W5-polyakov-crossvolume-2026-04-28.md`
(W5 Polyakov + Invariants prior wave);
`reconstitution/wave3-W6-costello-composition-2026-04-28.md`
(in-flight W3 W6 raising T4-side regulator question);
`appendix-unreduced-bv-qme.tex` (full, lines 1–179);
`tate-T4-bv-vanishing.tex` (full, lines 1–203);
`tate-T5-chain-level-primitive.tex` (lines 1–200);
`tate-T1-weighted-completion.tex` lines 596–832
(`defn:regulator-admissible-sector`, `thm:wt-regulator-independence-admissible`,
`ex:bad-weight-not-regulator`);
`principles.tex` (full, lines 1–227, including the Capelli/QME line
133–154); `main.tex` lines 280–470
(`lem:omega-cocycle`, Theorems
`thm:u1-center-anomaly`, `thm:u1-center-anomaly-open`,
`thm:quantum-classical-anomaly`); `main.tex` lines 2360–2438
(`thm:open-closed-derived-center` cochain-identity proof);
`main.tex` lines 5125–5345 (`stmt:costello-bv-package`,
`prob:analytic-graph-realization` regulator declarations);
`scripts/check_moyal_coefficients.py` lines 1–66 (Capelli /
Moyal numerical verification harness, used as a Polyakov path-integral
sanity check at low order).

**Independence.** I am independent of the Wave-2 W5 prior wave (same
lens primary, different mission: W5 audited cross-volume firewall;
W8 audits regulator coherence). I cross-check W3-W6's findings without
importing them as authority. The deliverable is per-target findings,
a verdict on regulator-canonicity, and a verdict on the stable core
under Polyakov + Composition.

---

## §0. Executive verdict (precedes the ledger)

**Verdict on regulator-canonicity (Polyakov primary).** The
manuscript's regulator scheme is **partially declared** and **not
canonical** in the strong Costello-renormalization sense. Specifically:

(i) The **path-integral / heat-kernel scheme** is declared at
`stmt:costello-bv-package` (`main.tex`:5136–5153) as the universal
import; the propagator
$P_{\epsilon,L}=\int_{\epsilon}^{L}Q^{\rm GF}K_t\,dt$ and the RG
operator are stated in heat-kernel form. This is the **default**
regulator class the manuscript inherits.

(ii) The **weighted Tate / Mittag-Leffler scheme** is declared at
`defn:regulator-admissible-sector` (T1:596–632); regulator-independence
**inside this admissible class** is `thm:wt-regulator-independence-admissible`
(T1:634–707). Outside this class (`ex:bad-weight-not-regulator`,
T1:789–803, e.g.\ super-exponential $w(d)=\exp(d^2)$), independence
is **not proved** and is genuinely false, since bracket-tameness fails.

(iii) Cross-scheme canonicity (heat-kernel vs.\ point-splitting vs.\
ζ-function vs.\ Pauli–Villars) is **not asserted** anywhere. The
W3-W6 residual R-W3-W6-04 names this as an open Phase-4 question.

This is **not a defect** in the local theorem; it is an **honest
restriction of scope**, and `prob:analytic-graph-realization`
(`main.tex`:5278–5345) records it as a named open obligation. But the
M-26 split's quantum-side claims (C₂(W)-q in particular) inherit the
restriction: they are valid **inside** the heat-kernel + admissible-
weight class, **not** across regulator-class boundaries.

**Verdict on stable core (Composition secondary).** The Wave-2 + W3-W6
declared stable core (Theorems A, B, C₁ᶠʷ, C₁ᶜᵒᵐᵖ, C₂(NT),
C₂(W)-cl, C₂(W)-q [conditional], C₂(R), D, E, F, G) **survives**
the Polyakov + Composition attack, with five new sharpenings:

1. **The Capelli/U(1) anomaly coefficient is universal across the
   declared admissible class** (Polyakov scheme-independence of the
   anomaly), but **only inside the admissible class**. Outside it,
   the coefficient could shift; the manuscript correctly does not
   assert universality across regulator classes (see §1 / W3-W8-01).

2. **BV/CE composition associativity is exact at the chain level**
   for the formal symplectic disk; the proof at `main.tex`:2381–2403
   uses Leibniz + generator agreement plus Tate continuity, with no
   regulator-dependent residue (W3-W8-02). The QME associativity is
   a **separate** statement and is **not** automatic — it is gated
   by `prop:app-scalar-contact-qme-class` (the $\hbar N[\bar c]$
   obstruction, M-32 ledger).

3. **Path-integral sanity at minimal order:** the chain-level
   primitive (T5) is a pure cumulant projection, **not** a heat-kernel
   regularized observable. It integrates to a finite quantity at every
   order without regularization. The "hidden infinity" question
   (T4 of the prompt) is real but lives **elsewhere**: in the mixed
   brane-defect QME obstruction class of the unreduced lift (T4-tex:
   the Costello–Li hypotheses-fail proposition); the chain-level T5
   is finite **because** it bypasses that analytic content (W3-W8-03).

4. **ℏ-rescaling consistency:** under $\hbar \mapsto \lambda \hbar$,
   the Capelli shift $\hbar N$ rescales to $\lambda\hbar N$, the
   quantum cocycle $\hbar N[\bar c]$ rescales identically, and the
   Tr-ψ ↔ $[\bar c]$ identification (M-31) is invariant up to the
   uniform $\lambda$ overall scaling (W3-W8-04). No anomalous scale
   anomaly is hidden.

5. **Composition of regulator schemes is not transactional.** A heat-
   kernel regulator at scale $L$ composed with a weighted Tate
   completion at weight $w$ gives a **two-parameter** family
   $(L, w)$; the Wave-2 W1 split implicitly takes the windowwise
   inverse limit in $w$ first, then the $\epsilon \to 0$ / $L$ flow
   (the Mittag-Leffler dictionary M-27 is the technical content of
   this order). Reversing the order (heat-kernel limit first, then
   weighted-window assembly) gives an **inequivalent** result; the
   manuscript implicitly uses the W-then-RG order, but this is not
   declared (W3-W8-05). This is a **load-bearing**
   regulator-composition order obligation.

The five sharpenings do not invalidate the M-26 split or the M-27
dictionary; they sharpen the regulator-canonicity boundary and the
order-of-limits discipline beneath the stable core.

---

## §1. New ledger entries

### W3-W8-01 — Capelli/U(1) anomaly coefficient is universal **inside the admissible class**, not across schemes

**Severity 4. Status valid. Confidence high.**
**Lens.** Polyakov primary; Composition secondary.
**Provenance.** New W3-W8 entry. Cross-link M-26 C₂(R), M-32
(U(1)$_{\rm ghost}$ regularization-compatible), Wave-2 W1 R-W1-02
("admissible-only regulator-independence").
**Target.** `thm:quantum-classical-anomaly` (`main.tex`:412–470);
`prop:app-scalar-contact-qme-class` (`appendix-unreduced-bv-qme.tex`:93–158);
`thm:wt-regulator-independence-admissible` (T1:634–707);
`defn:regulator-admissible-sector` (T1:596–632).
**Claim under attack.** The Capelli coefficient $\hbar N$ in
$YX - XY + \hbar N\,I \equiv 0$ and the corresponding obstruction
class $\hbar N [\bar c] \in H^1(\mathcal O_{\rm loc}(\mathcal E_w),
Q + \{I_0, -\})$ are scheme-independent quantum anomaly coefficients
that any consistent renormalization of the Hamiltonian BF theory will
reproduce.
**Polyakov-style hand computation.** Compute the simplest cross-check:
shift the regulator scale and verify the anomaly coefficient is
unchanged.

*Setup.* The anomaly cocycle $\omega(f, g) = [\{f, g\}]_0$
(`lem:omega-cocycle`, `main.tex`:284–316) is a **scalar** Lie
2-cocycle on $\mathfrak h_{\rm poly}$, evaluated at the
**constant-Taylor-coefficient** projection. On linear generators
$\omega(z_1, z_2) = [\{z_1, z_2\}]_0 = [1]_0 = 1$, manifestly
independent of any propagator scale.

*Quantum side.* The Capelli relation in Weyl normalization:
$[X^i_j, Y^k_l] = \hbar \delta^i_l \delta^k_j$, hence
$YX - XY = -\hbar N I \pmod{\text{ideal}}$, i.e.\ $XY - YX = \hbar N$
on $\C[\mathfrak{gl}_N \oplus \mathfrak{gl}_N]^{GL_N}$ trace
generators (`thm:quantum-classical-anomaly`:441–445). The
coefficient $\hbar N$ is **fixed by the canonical commutation
relation** of the Weyl algebra, **not** by the regulator scheme:
the heat-kernel propagator scales out of the canonical commutator,
the Pauli–Villars subtraction does not change the $\hbar$-leading
term, and a ζ-function regularization on the trace would only affect
$\mathrm{Tr}(I) = N$ if the zeta-trace differed from the naive trace
(it does not on a finite-dim'l space).

*Heat-kernel scale shift.* Consider the propagator
$P_{\epsilon, L}^{\rm op} = \int_\epsilon^L Q^{\rm GF} K_t^{\rm base}\,dt
\widehat\otimes \mathrm{id}$ (`rmk:linear-heat-versus-bv-kernel`,
`main.tex`:5219–5245). Rescaling $L \mapsto \lambda L$, $\epsilon
\mapsto \lambda \epsilon$ rescales the coefficient kernel by a uniform
$\lambda$ (a scale shift in the topological $\R^2$ direction, which is
the only dimensionful direction in this BF-on-flat-space sector). The
Capelli central commutator at order $\hbar$ on linear Hamiltonians
$X, Y$ is the integrated bulk-to-boundary contraction
$\int_\R \dot X \dot Y \delta(t_1 - t_2)\,dt_1 dt_2 = \int_\R \dot X
\dot Y \,dt$, which is invariant under reparameterization of $\R$;
the scale of the heat-kernel cutoff drops out. The **coefficient
$\hbar N$ is universal across heat-kernel scales**.

*Inside-admissible-class verification.* By
`thm:wt-regulator-independence-admissible`(iii), the obstruction
class $\hbar N[\bar c]$ is independent of the admissible weight $w$,
so changing the weight (e.g.\ from $q^d$ to $(q')^d$, both with
$q, q' > 1$) preserves the coefficient. By M-32, the
U(1)$_{\rm ghost}$ grading is preserved by the heat-kernel BV
regularization in 1d (Costello *RenEFT* §5.3), so the
$U(1)_{\rm ghost}$-charge of the anomaly is unchanged.

*Outside-admissible-class question.* For a non-admissible regulator,
e.g.\ a non-Mittag-Leffler completion or a super-exponential weight
violating bracket-tameness (`ex:bad-weight-not-regulator`), the
graphwise constants of `prop:wt-rg-tame` need not be finite uniformly
(T1:797–800). The **anomaly coefficient could in principle absorb a
divergent counterterm** outside the admissible class. The manuscript
does **not** claim universality here, and correctly so.

**Verdict.** The Capelli/U(1) anomaly coefficient $\hbar N$ is
**universal inside the admissible class** of T1 +
`stmt:costello-bv-package` (heat-kernel + admissible weight
$w(d) = q^d$, $q > 1$); it is **not asserted** to be universal across
all admissible regulator schemes (heat-kernel vs.\ ζ-function
vs.\ Pauli–Villars). Polyakov-style: the coefficient is "physical"
inside the declared scheme; cross-scheme physicality is a separate
obligation.
**Files read.** `main.tex`:412–470, 5125–5345; T1:596–832;
`appendix-unreduced-bv-qme.tex` 93–158;
`scripts/check_moyal_coefficients.py` 1–66 (the script verifies the
$\hbar$-leading and $\hbar^3$-correction structure of the Moyal
commutator, confirming the $\hbar N$ leading coefficient is canonical
under Weyl normalization).
**Confidence.** High.
**Blast radius.** Sharpens M-32 from "U(1)$_{\rm ghost}$ preserved by
the regularization (free statement)" to "the Capelli coefficient is
preserved within the admissible class; cross-class universality is
unverified." This is a one-sentence sharpening of M-32's heal text.
**Minimal heal.** In `theorem-lanes.tex` Lane 8 (Theorem G) and the
`claim-strength-ledger.tex` entry for the U(1) anomaly, append:

> "The Capelli coefficient $\hbar N$ is universal **inside the
> admissible regulator class** of Definition
> `defn:regulator-admissible-sector`; cross-class universality (heat-
> kernel vs.\ ζ-function vs.\ Pauli–Villars) is not asserted by this
> theorem. The coefficient $\hbar N$ is fixed by the canonical
> commutation relation of the Weyl algebra plus
> $\mathrm{Tr}_{\mathfrak{gl}_N}(I) = N$, and the heat-kernel scale
> drops out by reparameterization invariance of the brane-line
> propagator integral."

**Residual.** None at the M-26 / M-32 layer. Cross-class universality
remains R-W3-W6-04 (Phase-4).
**Adjudication.** Valid. Sharpens M-32 from compatibility-only to
explicit inside-class universality.

---

### W3-W8-02 — BV/CE composition associativity is exact at the cochain level on the formal disk; QME associativity is gated by Theorem G's anomaly

**Severity 3. Status valid. Confidence high.**
**Lens.** Composition primary; Polyakov secondary.
**Provenance.** New W3-W8 entry. Cross-link M-26 (C₁ᶜᵒᵐᵖ, C₂(W)),
W3-W6-05 (C₂(W)-q gated by Theorem G), M-32, M-31.
**Target.** `thm:open-closed-derived-center` proof at
`main.tex`:2381–2403; `lem:filtration-preservation`
(`tate-T5-chain-level-primitive.tex`:64–99); the
$d_{\rm CE}$/$d_\pi$ Leibniz argument; the $P_0$-bracket compatibility
at `main.tex`:2405–2426; the QME at
`appendix-unreduced-bv-qme.tex`:93–158.
**Claim under attack.** The composition
$d_{\rm CE} \circ \Phi^{-1}$, $\Phi \circ d_\pi$, $\{-, -\}_{\rm CE}$,
$[-, -]_S$, $Q$, $\{I_0, -\}$ all associate exactly under the chosen
heat-kernel + admissible-weight regularization, with no residual
correction at higher order in $\hbar$ or the regulator scale.
**Hand-computation at minimal order.** I compute the simplest
non-trivial case: the BV bracket and CE differential applied to a
length-2 word in $\{c^{(1,0)}, c^{(0,1)}, u_{(1,0)}, u_{(0,1)}\}$
generators on the formal symplectic disk.

*Setup.* On the disk, the structure constants are
$C^{(a+c-1, b+d-1)}_{(a,b),(c,d)} = (ad - bc)$
(`cor:derived-center-formal-disk`, `main.tex`:2465–2479). Take
$f = z_1$, $g = z_2$, with $\{f, g\} = 1$ in $\mathfrak h_{\rm poly}$,
and $\{f, g\} = 0$ in $\bar A = \mathfrak h_{\rm poly} / \C \cdot 1$.

*CE side, length-2 generator.* The CE word $w = c^{(1,0)} \wedge c^{(0,1)}$
has $|w| = 2$. The CE differential acts as
$$d_{\rm CE}(c^{(1,0)} c^{(0,1)})
   = (d_{\rm CE} c^{(1,0)}) c^{(0,1)} - c^{(1,0)} (d_{\rm CE} c^{(0,1)}).$$
Generator-level computation:
$d_{\rm CE} c^{(1,0)} = -\tfrac12 C^{(1,0)}_{IJ} c^I c^J = 0$
on $\bar A$ (no monomial of bidegree $(1,0)$ has the bracket landing
in bidegree $(1,0)$ on $\bar A$, since the bracket lowers total degree
by 1, hitting the constant line we discard). Same for $c^{(0,1)}$.
So $d_{\rm CE} w = 0$.

*PV side.* $\Phi(w) = \theta^{(1,0)} \wedge \theta^{(0,1)}$, with
$d_\pi$ computed analogously: $d_\pi \theta^{(1,0)} = 0$,
$d_\pi \theta^{(0,1)} = 0$ on $\bar A$. So $d_\pi \Phi(w) = 0
= \Phi(d_{\rm CE} w)$. **Cochain identity holds at length 2**:
exact, with no regulator correction.

*$P_0$-bracket compatibility on length-2 mixed word.*
$\{c^{(1,0)}, u_{(0,1)}\}_{\rm CE} = \delta^{(1,0)}_{(0,1)} = 0$.
$[\theta^{(1,0)}, O_{(0,1)}]_S = \delta^{(1,0)}_{(0,1)} = 0$.
$\Phi(\{c^{(1,0)}, u_{(0,1)}\}_{\rm CE}) = 0
= [\Phi(c^{(1,0)}), \Phi(u_{(0,1)})]_S$. Holds.

Take a non-trivial case: $\{c^{(2,0)}, u_{(0,2)}\}_{\rm CE} = 0$ (the
two indices differ). $[\theta^{(2,0)}, O_{(0,2)}]_S = 0$. Trivial.
Now the **Leibniz-mediated** mixed word
$\{c^{(1,0)} c^{(0,1)}, u_{(2,2)}\}_{\rm CE}$:
$$\{c^{(1,0)} c^{(0,1)}, u_{(2,2)}\}_{\rm CE}
   = c^{(1,0)} \{c^{(0,1)}, u_{(2,2)}\}_{\rm CE}
   - \{c^{(1,0)}, u_{(2,2)}\}_{\rm CE} c^{(0,1)} = 0,$$
since both Kronecker deltas vanish. Same on the PV side. **Bracket
associativity holds exactly via Leibniz.**

*Higher-length / higher-bracket.* The argument at
`main.tex`:2381–2403 is: generator-level agreement + Leibniz +
algebra-homomorphism + Tate continuity ⇒ full-completed-algebra
agreement. **This composition is associative because Leibniz
distributes through the bracket and the algebra-homomorphism property
of $\Phi$ is preserved.** No regulator scale enters this step. **The
chain-level CE/PV identity is regulator-independent at the cochain
level.**

*QME side: separate question.* The associativity
$Q + \{I_0, -\}$ on the local-functional complex
$\mathcal O_{\rm loc}(\mathcal E_w)$ requires that $\{I_0, -\}$ be a
**derivation** of the BV bracket and that
$(Q + \{I_0, -\})^2 = 0$. The latter is the QME:
$$Q I_0 + \tfrac12 \{I_0, I_0\} = 0 \pmod{\hbar}.$$
By `prop:app-scalar-contact-qme-class`
(`appendix-unreduced-bv-qme.tex`:93–158), the **scalar contact term
contributes $\hbar N \omega(f, g)$ to the unreduced obstruction**;
this is a degree-0 contribution to a degree-1 obstruction complex
when contracted with the central ghost $\gamma_{\mathbf 1}$. The
class is $\hbar N [\bar c]$, **non-zero** on the unreduced source.

**Hence:** the chain-level CE/PV composition
$d_{\rm CE} \circ \Phi = \Phi \circ d_\pi$ is exact, with no
regulator residue (Polyakov: the regulator is irrelevant at this
algebraic step). The QME composition
$Q + \{I_0, -\}$ has a **non-zero residue** $\hbar N [\bar c]$ on
the unreduced source, **gated** by Theorem G's anomaly. The two
composition statements live at different layers and the latter is
**not** trivially regulator-independent — it depends on whether the
admissible-class regulator preserves the $\hbar N$ coefficient
(W3-W8-01 verifies that it does, inside the admissible class).

**Verdict.** BV/CE composition associativity is **exact** at the
chain level for the formal symplectic disk; QME associativity holds
**only modulo** the Capelli class $\hbar N [\bar c]$ on the unreduced
source. This is consistent with W3-W6-05's identification: classical
C₂(W) is unconditional; quantum C₂(W) is gated by Theorem G. Wave-2
W1's M-26 split is honest at both the cochain layer and the
QME-conditional layer; W3-W8 cross-checks the layered split.
**Files read.** `main.tex`:2381–2403, 2405–2426 (cochain identity +
$P_0$ bracket compatibility); `appendix-unreduced-bv-qme.tex`:1–179
(unreduced QME + scalar contact class); T5:64–176
(filtration preservation by $Q$ and $P_0$ bracket; the chain-level
primitive projection commutes strictly with $Q$).
**Confidence.** High.
**Blast radius.** Confirms M-26 + W3-W6-05 layered split; no new
obstruction. The minor sharpening: name the **distinction** between
chain-level associativity (regulator-irrelevant, Leibniz-mediated)
and QME associativity (gated by anomaly class) as a **layer
distinction**, not a scheme-dependence.
**Minimal heal.** In `claim-strength-ledger.tex`, distinguish:

> "**Chain-level associativity** (CE/PV cochain identity,
> $P_0$-bracket compatibility, $\Phi$ algebra homomorphism): proved
> exactly on the formal symplectic disk by generator agreement +
> Leibniz + Tate continuity. Regulator-independent at this layer
> (the regulator does not enter the cochain identity).
> **QME associativity** (Quantum Master Equation
> $Q I_0 + \tfrac12 \{I_0, I_0\} = 0 \pmod{\hbar}$): holds **modulo**
> the scalar contact class $\hbar N [\bar c]$
> (`prop:app-scalar-contact-qme-class`); this class is non-zero on
> the unreduced scalar-reduced Hamiltonian source. The QME is
> conditional on `prob:weighted-rg-locality` (W3-W6-05)."

**Residual.** None at the cochain layer; QME residual is W3-W6-05
(closed by W3-W8-01 inside the admissible class, gated by Theorem G
on the unreduced source).
**Adjudication.** Valid layered distinction. Cross-checks W3-W6-05
and M-26's layer structure.

---

### W3-W8-03 — Path-integral sanity at minimal order: the chain-level primitive integrates without regularization; the "hidden infinity" lives in the unreduced lift, and is the same Capelli class

**Severity 3. Status valid. Confidence high.**
**Lens.** Polyakov primary.
**Provenance.** New W3-W8 entry. Cross-link M-26 C₂(NT)/C₂(W),
M-31 (Tr ψ ↔ $[\bar c]$), W3-W6-05.
**Target.** T5:23–55 (chain-level primitive projection,
explicitly **without recourse to any heat-kernel propagator or
finite-scale regularization**); `thm:chain-level-primitive-projection-Q`
(T5:157–176); `prob:weighted-rg-locality`;
`thm:app-unreduced-polynomial-centrality-no-go`
(`appendix-unreduced-bv-qme.tex`:33–91).
**Claim under attack.** The chain-level constructions correspond to
path-integral expressions; check whether the chain-level primitive
(T5) actually integrates to a finite path-integral, or whether there
is a regularization-dependent infinity that the chain-level approach
hides.
**Polyakov-style minimal-order computation.** I compute the simplest
case: the chain-level primitive of a single-trace single-cyclic-word
class.

*Setup.* In the stable connected limit $N \to \infty$,
$\mc R_\infty^{GL_\infty,{\rm st}} \cong \mathbf S(\mathrm{Cyc}(F)_{\rm
nonempty})$ with $F = \C \langle x_1, x_2 \rangle$ (T5:43–44).
The trace-count filtration is the symmetric-algebra filtration. Take
the simplest non-trivial cyclic word: $x_1 x_2 \in \mathrm{Cyc}(F)$,
of trace count 1, total degree 2.

*Boundary evaluation.* $\partial_{\rm bb,N}(z_1 z_2) =
\mathrm{Tr}(\phi_1 \phi_2)$. In the open BV ring
$\mc R_N = \C[(\phi_i)^a_b] \otimes \Lambda(\psi^a_b)$ with $|\psi| = -1$,
$Q\psi = [\phi_1, \phi_2]$. This is a **finite polynomial expression**
at each finite $N$, taking values in a finite-dim'l polynomial ring.

*Chain-level primitive projection.* $\pi_{\rm prim}: \mathrm{Tr}(\phi_1 \phi_2)
\mapsto z_1 z_2 \in \bar A$ (T5:101–133). This is the cumulant
projection on the symmetric algebra, restricted to single-trace
generators. **No integration over field configurations is performed.**
The result $z_1 z_2$ is a **finite polynomial**, with no regulator
needed.

*Smearing by a de Rham form on $I \subset \R$.* The full target is
$\Omega^\bullet_c(I) \widehat\otimes \bar A$. Smear $\mathrm{Tr}(\phi_1
\phi_2)$ by a compactly supported de Rham form $\alpha \in
\Omega^0_c(\R)$. The smeared observable is
$$\int_I \alpha(t)\, \mathrm{Tr}(\phi_1(t) \phi_2(t))\, dt.$$
**This is a finite Lebesgue integral**, since $\alpha$ has compact
support and the integrand is bounded for fixed $\phi_1, \phi_2 \in
\mathfrak{gl}_N$. **No path-integral over $\phi$-configurations is
asserted at this layer.** The chain-level construction lives at the
**observable** layer, not the **expectation-value** layer.

*Where the path-integral lives.* The actual perturbative
path-integral is given by the Costello formalism in
`stmt:costello-bv-package` (`main.tex`:5136–5153), with propagator
$P_{\epsilon, L}$ and RG operator $W$. **The chain-level primitive is
a classical observable**, not an effective action.
$$\pi_{\rm prim}: \mathrm{Obs}^{\rm cl}_{\rm open, N}(I)
   \to \Omega^\bullet_c(I) \widehat\otimes \bar A.$$
The codomain is **classical**; no expectation value is taken. The
quantum / one-loop / all-order extension of $\pi_{\rm prim}$ to a
quantum observable is an entirely separate question, governed by
`prob:formal-factorization-center` items (3) and the brane-defect QME
of `appendix-unreduced-bv-qme.tex`.

*Where the "hidden infinity" actually lives.* By
`thm:app-unreduced-polynomial-centrality-no-go` (`appendix-unreduced-
bv-qme.tex`:33–91), the unreduced polynomial $M_{\rm pol}$ has **no
$\rho_{a,b}[1] \mapsto \Theta_{a,b}$ assignment with the required
centrality homotopies**: the principal-part action is locally
non-nilpotent (lines 75–77: $z_1^r \cdot \rho_{a,b} = (-1)^r (b+1)
\cdots (b+r) \rho_{a, b+r} \neq 0$), while the polynomial Hamiltonian
action is locally nilpotent. The **infinity** that any regulator must
absorb to produce a centrality homotopy on the unreduced lift is
**categorical**, not analytical: the polynomial category does not
contain principal-part objects, so the homotopy cannot exist there.

The path-integral analog: the brane-defect QME obstruction
$\hbar N [\bar c]$ is the class that any putative one-loop
counterterm tower would have to absorb. By
`prop:app-scalar-contact-qme-class`, **this class is non-zero on the
scalar-reduced source**. Hence the all-$\hbar$-order brane-defect
QME is **obstructed**, not by a regulator-dependent divergence, but
by a class that survives **any** regulator (inside the admissible
class). The "hidden infinity" is **not** a regulator pathology of T5;
it is the same Capelli anomaly $\hbar N [\bar c]$ that gates C₂(W)-q
(W3-W6-05) and that is **independent of regulator scheme inside the
admissible class** (W3-W8-01).

**Verdict.** The chain-level primitive (T5) **integrates to a finite
classical observable** at every finite order without regularization;
**no hidden infinity** exists at this layer because the layer is
classical, pre-quantization. The "hidden infinity" of the prompt's
T4 question lives in the **unreduced quantum lift** of T4-tex /
appendix-unreduced-bv-qme, and is the same Capelli class $\hbar N
[\bar c]$ that Theorem G classifies and that gates C₂(W)-q. **Path-
integral sanity at the chain-level layer is intact**; the obstruction
to the unreduced quantum lift is **not** a regulator divergence but a
**genuine cohomology class**, and the manuscript correctly records it
as a non-zero anomaly, not as a regulator artifact.
**Files read.** T5:23–176 (chain-level construction without
regularization); `appendix-unreduced-bv-qme.tex`:33–158 (no-go for
polynomial unreduced lift + scalar contact class);
`tate-T4-bv-vanishing.tex`:1–203 (Costello–Li hypotheses fail; the
fifth obstruction is the coefficient-system Tate completion, T4-tex
lines 89–107).
**Confidence.** High.
**Blast radius.** Confirms the layered structure of the manuscript:
chain-level (T5) is regulator-independent; quantum extension
(C₂(W)-q + Theorem G) is gated by the Capelli class. No new
obstruction; this entry **distinguishes the layers** so the path-
integral question lands at the correct address.
**Minimal heal.** In `principles.tex` Principle 1 (Dirac) preface or
in `tate-T5-chain-level-primitive.tex` introduction (around lines
23–37, where the construction is declared regulator-free), append:

> "**Path-integral sanity remark.** The chain-level primitive
> projection $\pi_{\rm prim}$ is a **classical observable
> construction**, not an expectation value. It produces a finite
> polynomial at every finite order without invoking the heat-kernel
> propagator or any other regulator. The path-integral expectation
> value of $\pi_{\rm prim}$ — i.e.\ the all-$\hbar$-order quantum
> extension to an effective observable on
> $\mathcal O_{\rm loc}(\mathcal E_w)$ — is a separate construction,
> conditional on the brane-defect QME obstruction class
> (`prob:weighted-rg-locality`,
> `prop:app-scalar-contact-qme-class`). The 'infinity' that a
> path-integral renormalization would have to absorb is the Capelli
> class $\hbar N [\bar c]$, which is **non-zero** on the scalar-
> reduced source by the same lemma; the chain-level T5 primitive
> bypasses this analytic content by living at the classical layer."

**Residual.** None at the chain-level layer. The quantum extension
residual is W3-W6-05 / R-W3-W6-05.
**Adjudication.** Valid Polyakov-lens classification: layer the
constructions, locate the regulator dependence at the correct address.

---

### W3-W8-04 — ℏ-rescaling consistency across the stable core; the Tr-ψ ↔ $[\bar c]$ identification (M-31) is invariant up to uniform $\lambda$

**Severity 2. Status valid. Confidence high.**
**Lens.** Polyakov primary.
**Provenance.** New W3-W8 entry. Cross-link M-31, M-32, Theorem G.
**Target.** `thm:quantum-classical-anomaly`:412–470;
`prop:app-scalar-contact-qme-class`:93–158; M-31 in master ledger.
**Claim under attack.** Under $\hbar \mapsto \lambda \hbar$ (with
$\lambda > 0$ a real scaling parameter, the natural Polyakov scaling),
the Capelli/U(1) anomaly coefficient and the M-31 Tr-ψ ↔ $[\bar c]$
identification rescale consistently across all stable-core members
(A, B, C₁ᶠʷ, C₁ᶜᵒᵐᵖ, C₂(NT), C₂(W)-cl, C₂(W)-q, C₂(R), D, E, F, G).
**Polyakov-style hand-computation.**

*Capelli relation.* $YX - XY = \hbar N \mapsto YX - XY = \lambda \hbar
N$ under $\hbar \mapsto \lambda \hbar$. **Consistent.** The Weyl algebra
relation $[X^i_j, Y^k_l] = \hbar \delta^i_l \delta^k_j$ rescales
identically; the Moyal product
$f * g = m \circ \exp(\tfrac{\hbar}{2} P)(f \otimes g)$ rescales to
$m \circ \exp(\tfrac{\lambda \hbar}{2} P)(f \otimes g)$. The
all-order Moyal corrections (verified numerically by
`scripts/check_moyal_coefficients.py` lines 13–60) all carry uniform
$\lambda^r$ at order $\hbar^r$. **No anomalous scale anomaly.**

*Cocycle.* $\omega(f, g) = [\{f, g\}]_0$ is a **classical** Lie
2-cocycle with no $\hbar$-dependence; under $\hbar \mapsto \lambda
\hbar$, $\omega$ is unchanged. The class $[\bar c] \in
H^2_{\rm Lie}(\bar A; \C)$ is independent of $\hbar$.

*Quantum cocycle.* $\hbar N [\bar c] \mapsto \lambda \hbar N
[\bar c]$. Multiplied by $\lambda$, but **the class itself is
unchanged**; only the prefactor scales. The Rees deformation
$U_{\hbar}(\bar A_{[\bar c]}) \mapsto U_{\lambda \hbar}(\bar A_{[\bar
c]})$ is an isomorphism on $\bar A_{[\bar c]}$ (the Rees specialization
at $\hbar = 0$ recovers $\widehat{\mathbf S}(\bar A_{[\bar c]})$
identically; at $\hbar = \lambda \hbar_0$ it recovers the rescaled
universal enveloping algebra, isomorphic to $U_{\hbar_0}$ via the
$\lambda$-rescaling of the generators).

*M-31 identification.* M-31 says
$[\mathrm{Tr}\,\psi]_{\rm BV} \leftrightarrow [\bar c]_{\rm CE}$ are
the same anomaly line. Under $\hbar \mapsto \lambda \hbar$,
$\mathrm{Tr}\,\psi$ is **classical** (it has no explicit $\hbar$);
$[\bar c]$ is **classical**. **Both sides are $\hbar$-independent**;
the identification is invariant under $\hbar \mapsto \lambda \hbar$
**at the classical layer**. The quantum extension
($\mathrm{Tr}\,\psi$ as a derived intersection class at one loop;
$[\bar c]$ as the leading $\hbar$-coefficient of the Rees deformation)
rescales by uniform $\lambda$, matching consistently.

*Cross-stable-core check.*
- **Theorem A** (Dirac probe, classical Koszul). No $\hbar$
  dependence. Invariant.
- **Theorem B** (one-ψ chain-level homology). No $\hbar$.
  Invariant.
- **Theorem C₁/C₂** (CE/PV identification). The structure
  constants $C^L_{(a,b),(c,d)} = (ad-bc)$ are $\hbar$-independent. The
  Tate completion is $\hbar$-independent. **Invariant** under $\hbar
  \mapsto \lambda \hbar$.
- **Theorem D** (Matlis principal-part). No $\hbar$. Invariant.
- **Theorem E** (factorization currents). The bulk-to-boundary
  bracket has no explicit $\hbar$ at the chain level; the quantum
  extension carries uniform $\lambda$. Invariant up to uniform scale.
- **Theorem F** (Moyal/Weyl quantum coefficients). All Moyal
  corrections at order $\hbar^r$ rescale by $\lambda^r$. **Consistent.**
- **Theorem G** (U(1) anomaly). $\hbar N [\bar c]$ rescales by
  $\lambda$; the class $[\bar c]$ is invariant. **Consistent.**

**Verdict.** $\hbar \mapsto \lambda \hbar$ is a **consistent
rescaling** across all stable-core members: classical statements are
invariant, quantum statements rescale by the appropriate power of
$\lambda$, and no anomalous scale anomaly is hidden.
**Files read.** `main.tex`:412–470; `scripts/check_moyal_coefficients.py`
1–66; M-31 / M-32 in master ledger.
**Confidence.** High.
**Blast radius.** Editorial confirmation. No structural change.
**Minimal heal.** Optional editorial sentence in
`principles.tex` (post Capelli/QME line) or in the quantum
classical-equivalence theorem area (`main.tex`:412–470):

> "**ℏ-scaling.** Under $\hbar \mapsto \lambda \hbar$ for $\lambda
> > 0$, the Moyal product, the Capelli shift, and the Rees
> deformation rescale consistently. The classical cocycle $\omega$
> and the cohomology class $[\bar c] \in H^2_{\rm Lie}(\bar A; \C)$
> are $\hbar$-independent; the quantum coefficient $\hbar N$ in the
> Capelli relation rescales by $\lambda$. The Tr-ψ ↔ $[\bar c]$
> identification of Remark M-31 is invariant at the classical
> layer; the quantum extension carries the uniform $\lambda$
> rescaling. No scale anomaly is hidden in the stable core."

**Residual.** None.
**Adjudication.** Valid editorial confirmation.

---

### W3-W8-05 — Order-of-limits discipline: weighted-window inverse limit must precede heat-kernel RG flow; reverse order is inequivalent

**Severity 4. Status valid. Confidence high.**
**Lens.** Composition primary; Polyakov secondary.
**Provenance.** New W3-W8 entry. Cross-link M-26 (C₂(W)+C₂(R)), M-27
(`lem:tate-mittag-leffler-dictionary`), W3-W6-04 (regulator-class-
canonical, not regulator-canonical).
**Target.** `prob:analytic-graph-realization` (`main.tex`:5278–5345);
`thm:wt-regulator-independence-admissible` (T1:634–707); the Mittag-
Leffler dictionary M-27.
**Claim under attack.** The two regulator parameters of the manuscript
— the **heat-kernel scale** $(\epsilon, L)$ and the **weighted Tate
window** $w_0$ (with weight $w$ as a derived parameter) — can be taken
to limits in any order, and the resulting effective theory / cohomology
class is the same.
**Composition consequence.** This is **not** asserted in the
manuscript, and it is **not** true. The proof of
`thm:wt-regulator-independence-admissible` (T1:671–707) takes the
inverse limit in $w_0$ **first** (line 695: "Passing to the inverse
limit gives the displayed isomorphism"), then identifies admissible
filtered cohomology classes. The heat-kernel limit $\epsilon \to 0$ /
$L \to \infty$ (Costello RG flow) is composed **after** the weighted
inverse limit, with the windowwise propagator
$P_{\epsilon, L}^{w, w_0}$ already restricted to the
$w_0$-truncation.
**Hand-computation: reversing the order.** Consider the
**reverse-order** composition: take $\epsilon \to 0, L \to \infty$
first at each $w_0$ separately, then attempt to assemble the
$w_0$-tower into an inverse limit.

*The reverse-order issue.* At each fixed $w_0$, the propagator
$P_{0, \infty}^{w, w_0}$ is the heat-kernel-limit propagator on the
**finite-dim'l** truncated coefficient space $\mathcal E_w^{w_0}$.
Costello's renormalization at fixed $w_0$ produces an effective
interaction $I_\infty^{w, w_0}$ in the renormalized BV theory on
$\mathcal E_w^{w_0}$. This is fine at each $w_0$.

The transition $w_0 + 1 \mapsto w_0$ is a **truncation** of the
coefficient space (`defn:regulator-admissible-sector` (A1)). Under
the heat-kernel-first ordering, the renormalized effective interactions
$I_\infty^{w, w_0}$ at different $w_0$ are connected by **truncation
of the renormalized interaction**, **not** by the original truncation
of the bare interaction. By Costello's RG flow,
**truncation does not commute with renormalization** in general:
the counterterms $I^{\rm CT}_{g_v}(\epsilon)$ at order $\hbar^{g_v}$
on $\mathcal E_w^{w_0+1}$ project under truncation to **different**
counterterms on $\mathcal E_w^{w_0}$ than the ones supplied by the
direct renormalization on $\mathcal E_w^{w_0}$.

Concretely, consider a one-loop diagram with two vertices, each
absorbing a coefficient leg of degree $d_1, d_2$. If $d_1 + d_2 > w_0$
but $d_1, d_2 \leq w_0$, the diagram contributes to the
$w_0$-windowed renormalization; if $d_1, d_2 \leq w_0 + 1$ but
$d_1 + d_2 > w_0 + 1$, it is dropped at $w_0 + 1$ but might be present
at the renormalization done directly at $w_0$. The truncation
discards an interaction-vertex that was relevant for the original
$w_0$-windowed counterterm calculation; the **reverse order produces
an effectively different counterterm tower**.

*The forward-order resolution.* The manuscript's discipline is to
take the windowwise inverse limit **first**, producing a Mittag-
Leffler tower $\{(\mathcal O_{\rm loc}(\mathcal E_w^{w_0}),
Q + \{I_0^w, -\})\}_{w_0}$ with **bare** transitions; M-27's
dictionary applies to this tower (surjective transitions + finite-
dim'l kernels) and gives $\varprojlim^1 = 0$ + $\varprojlim$ exact.
The heat-kernel RG flow then runs on the inverse limit, which is
well-defined because the bare interaction is admissible (A2: vertexwise
polynomial-degree-bounded).

**Verdict.** The order of limits is **load-bearing**: weighted-window
inverse limit must precede heat-kernel RG flow. The reverse order
gives an inequivalent counterterm tower. The manuscript implicitly
uses the forward order; W3-W8-05 names this as a **declared
discipline**, not a free choice. This is exactly what the M-27 lemma
encodes: the Mittag-Leffler dictionary makes the inverse limit
exact, so that the post-limit RG flow is well-defined.
**Files read.** `main.tex`:5125–5345 (Costello BV package +
analytic-graph-realization problem); T1:634–707 (admissible
regulator-independence proof); M-27 in master ledger.
**Confidence.** High.
**Blast radius.** This sharpens M-27 from "the lemma is statement-
only; per-site verification supplied by T1, T2, T3, T5" (W3-W6-03)
to "the lemma encodes a **load-bearing order-of-limits discipline**
in the regulator composition: weight-window inverse limit precedes
heat-kernel RG flow." This is a structural sharpening of M-27, not
a downgrade.
**Minimal heal.** When authoring `lem:tate-mittag-leffler-dictionary`
(per WP2-1 from W1, sharpened by WP3-W6-5 from W3-W6-03), append a
sentence:

> "**Regulator-composition order.** The lemma encodes the
> discipline that the weight-window inverse limit
> $\varprojlim_{w_0}$ must be taken **before** the heat-kernel
> RG flow ($\epsilon \to 0$, $L \to \infty$). Under this order, the
> Mittag-Leffler hypothesis package (surjective transitions + finite-
> dim'l kernels) gives $\varprojlim^1 = 0$ on bare interactions, and
> the post-limit Costello RG flow runs on a well-defined inverse
> limit. The reverse order — heat-kernel limit first, then assembly
> of the $w_0$-tower — produces an inequivalent counterterm tower
> in general, because truncation does not commute with
> renormalization on a non-truncating interaction. The manuscript
> uses the forward order throughout."

**Residual.** **R-W3-W8-05** (open Phase-4): a complete proof that
the forward order is **canonical** (in the sense of giving the
unique-up-to-equivalence Costello renormalized theory) requires a
Costello-RG-flow-with-Mittag-Leffler-input theorem; this is not
proved in the manuscript and remains a Phase-4 obligation, related
to but distinct from R-W3-W6-04 (cross-class canonicity).
**Adjudication.** Valid. Sharpens M-27 from a Mittag-Leffler
dictionary to a regulator-composition order discipline.

---

## §2. Stable-core update (Wave-3-W8 amended)

The Wave-2 + W3-W6 stable core was: A, B, C₁ᶠʷ, C₁ᶜᵒᵐᵖ
(bidirectional symmetric filtration), C₂(NT), C₂(W)-cl, C₂(W)-q
(conditional on Theorem G), C₂(R) (admissible-class only), D, E, F,
G (gates C₂(W)-q). Wave-3-W8's amendments:

- **A, B, D, E, F, G:** Stable. ℏ-rescaling consistent (W3-W8-04);
  Polyakov path-integral sanity at the chain level (W3-W8-03);
  Capelli coefficient universal in the admissible class (W3-W8-01);
  no new obstruction.
- **C₁ᶠʷ, C₁ᶜᵒᵐᵖ:** Stable. Chain-level associativity exact under
  the Leibniz argument (W3-W8-02); no regulator residue at this
  layer; the symmetric-filtration hypothesis (W3-W6-01) is
  bidirectional and verified on the formal disk.
- **C₂(NT), C₂(W)-cl, C₂(W)-q, C₂(R):** Stable, with the order-of-
  limits discipline made explicit (W3-W8-05): weighted-window
  inverse limit before heat-kernel RG flow.
- **C₂(W)-q:** Conditional on Theorem G's Capelli class (W3-W6-05);
  the conditionality is **inside the admissible regulator class**
  (W3-W8-01); cross-class universality remains R-W3-W6-04 (Phase-4).
- **G:** Stable. Capelli coefficient $\hbar N$ universal in the
  admissible class (W3-W8-01); ℏ-rescaling consistent (W3-W8-04);
  the M-31 identification is regulator-independent at the classical
  layer (W3-W8-04); the unreduced quantum extension is gated by
  `prop:app-scalar-contact-qme-class` (the same class).

**Verdict on stable core (Polyakov + Composition lens).** STABLE,
with the regulator-canonicity boundary now sharpened to:

1. **Heat-kernel + admissible-weight class** (T1's
   `defn:regulator-admissible-sector` + Costello
   `stmt:costello-bv-package`): the canonical regulator class of
   the manuscript. Inside this class, the Capelli coefficient is
   universal, the M-26 split is canonical, and the cohomology
   classes $[\bar c]$, $\hbar N [\bar c]$, $[\mathrm{Tr}\,\psi]$
   are well-defined.

2. **Order-of-limits discipline** (W3-W8-05 / M-27 sharpened):
   weighted-window inverse limit before heat-kernel RG flow.

3. **Layer discipline** (W3-W8-02 / W3-W8-03): chain-level
   associativity is regulator-independent (Leibniz-mediated); QME
   associativity is gated by the Capelli class; path-integral
   sanity holds at the classical layer; the "hidden infinity" lives
   in the same Capelli class that gates C₂(W)-q.

4. **ℏ-scaling consistency** (W3-W8-04): no anomalous scale
   anomaly in the stable core; classical statements are invariant,
   quantum statements rescale uniformly.

The stable core is **regulator-class-canonical** (W3-W6-04 sharpened
by W3-W8-01), **not** Costello-canonical across all renormalization
schemes. This is consistent with the W3-W6 verdict and with the
manuscript's honest scope statement at
`prob:analytic-graph-realization`.

---

## §3. Heal proposals (smallest first)

### Tier 1 — Statement-only edits

**WP3-W8-1 (W3-W8-01).** In `theorem-lanes.tex` Lane 8 (Theorem G)
and `claim-strength-ledger.tex` U(1)-anomaly entry, append the
"Capelli coefficient universal inside the admissible class" sentence
as in W3-W8-01's minimal heal. One sentence.

**WP3-W8-2 (W3-W8-02).** In `claim-strength-ledger.tex` distinguish
chain-level associativity (regulator-irrelevant, exact via Leibniz)
from QME associativity (gated by anomaly), per W3-W8-02's minimal
heal. Two named sub-bullets.

**WP3-W8-3 (W3-W8-03).** In `tate-T5-chain-level-primitive.tex`
introduction (around lines 23–37) or in `principles.tex` Principle 1
preface, insert the "path-integral sanity remark" of W3-W8-03's
minimal heal. One paragraph.

**WP3-W8-4 (W3-W8-04).** In `main.tex` near the Capelli quantum-
classical theorem (`thm:quantum-classical-anomaly`:412–470), or in
`principles.tex` post Capelli/QME line, insert the optional
"ℏ-scaling" sentence of W3-W8-04's minimal heal. One paragraph,
optional editorial.

**WP3-W8-5 (W3-W8-05).** Authoring `lem:tate-mittag-leffler-dictionary`
(per WP3-W6-5), append the regulator-composition-order sentence of
W3-W8-05's minimal heal. One paragraph at the end of the lemma.

### Tier 2 — Architectural cross-links

**WP3-W8-6.** In `principles.tex` after the three-principles deduction
(§deduction-of-the-local-package), add a "Regulator scope" subsection:

> "**Regulator scope.** The local theorem is canonical in the
> following regulator class: heat-kernel BV propagator
> ($\stmt{costello-bv-package}$, with admissible flat gauge-fixing
> and Costello renormalization scheme), composed with the
> admissible weighted Tate completion
> (`defn:regulator-admissible-sector`, T1). Inside this class, the
> Capelli/U(1) anomaly coefficient is universal; the order-of-limits
> discipline (weight-window inverse limit before heat-kernel RG
> flow) is verified by the Mittag-Leffler dictionary. Cross-class
> regulator canonicity (heat-kernel vs.\ ζ-function vs.\ Pauli-
> Villars vs.\ point-splitting) is **not** asserted; it is named in
> `prob:analytic-graph-realization` as an open obligation
> (residual R-W3-W6-04 / R-W3-W8-05)."

This is the strongest Polyakov-lens classification: **declared
regulator scope, with named open boundaries at the cross-class
direction.**

---

## §4. Residuals after Wave-3-W8

- **R-W3-W8-01** (closed inside the admissible class).
  Coefficient universality across regulator classes (heat-kernel
  vs.\ ζ-function vs.\ Pauli-Villars) for the Capelli/U(1) anomaly.
  Phase-4. Cross-link R-W3-W6-04.
- **R-W3-W8-02** (closed at the chain level). QME associativity on
  the unreduced source is gated by the Capelli class
  (`prop:app-scalar-contact-qme-class`); see R-W3-W6-05.
- **R-W3-W8-03** (closed at the classical layer). Path-integral
  expectation values for the chain-level primitive at the all-
  $\hbar$-order quantum layer require the brane-defect QME
  obstruction to vanish; conditional on
  `prob:weighted-rg-locality`; same residual as R-W3-W6-05.
- **R-W3-W8-04** (closed). ℏ-scaling consistent across the stable
  core. No open residual.
- **R-W3-W8-05** (open Phase-4). Canonicity of the forward order
  (weight-window inverse limit before heat-kernel RG flow) as a
  Costello-RG-with-Mittag-Leffler-input theorem; the manuscript uses
  the order, but does not prove its canonicity. Phase-4.

---

## §5. Convergence verdict

**M-26 (5-way C₁/C₂ split).** Survives the Polyakov + Composition
lens, with three new sharpenings:
- C₂(R) inside admissible class only, with the Capelli coefficient
  universal inside (W3-W8-01).
- BV/CE chain-level associativity exact (W3-W8-02); QME associativity
  gated by anomaly (W3-W8-02 + W3-W6-05, consistent).
- Order-of-limits discipline: weight-window before RG flow
  (W3-W8-05).
**Verdict: VALID, sharpened.**

**M-27 (`lem:tate-mittag-leffler-dictionary`).** Survives, sharpened
to encode a load-bearing order-of-limits discipline for regulator
composition (W3-W8-05). **Verdict: VALID, with composition-order
discipline named.**

**M-31 (Tr-ψ ↔ $[\bar c]$ identification).** Survives, with
ℏ-rescaling consistency confirmed (W3-W8-04): the identification is
invariant at the classical layer, rescales uniformly at the quantum
layer. **Verdict: VALID, with explicit scaling discipline.**

**M-32 (U(1)$_{\rm ghost}$ regularization-compatible).** Survives,
sharpened to "Capelli coefficient $\hbar N$ universal inside the
admissible class" (W3-W8-01). **Verdict: VALID, sharpened.**

**Stable core (Theorems A, B, C₁ᶠʷ, C₁ᶜᵒᵐᵖ, C₂(NT), C₂(W)-cl,
C₂(W)-q, C₂(R), D, E, F, G).** Survives, with the regulator-
canonicity boundary now sharpened to (i) heat-kernel + admissible-
weight class declared, (ii) order-of-limits discipline declared,
(iii) layer discipline (chain-level vs.\ QME) declared,
(iv) ℏ-rescaling consistency declared. **Verdict: STABLE, with
sharper regulator-scope boundary.**

The single most important new technical insight: **the
Mittag-Leffler dictionary M-27 encodes a load-bearing
regulator-composition order discipline** (weight-window inverse
limit before heat-kernel RG flow). Reversing the order produces an
inequivalent counterterm tower in general, because truncation does
not commute with renormalization on a non-truncating interaction.
The manuscript uses the forward order; W3-W8-05 names this as a
declared discipline rather than a free choice.

**Posture against Wave 2 / W3-W6.** Wave-2 W1's 5-way split,
Wave-2 W6's 8-link DAG, W3-W6's three sharpenings, and
M-27/M-31/M-32 are all preserved. The W3-W8 contribution is a
**Polyakov-lens classification of regulator scope** (heat-kernel
+ admissible-weight, with cross-class canonicity open) and a
**Composition-lens declaration of order-of-limits discipline**
(weight-window before RG flow, encoded by M-27). No new theorems are
needed; five named statements (W3-W8-01 through W3-W8-05) are added
to the master ledger.

End of W3-W8 report.

---

## 200-word executive summary

W3-W8 (Polyakov + Composition lens) cross-checks the Wave-2 + W3-W6
stable core against regulator coherence and BV/CE composition
associativity. **Verdict on regulator canonicity**: the manuscript is
**regulator-class-canonical inside the admissible class** of T1's
`defn:regulator-admissible-sector` + Costello
`stmt:costello-bv-package` (heat-kernel BV propagator + admissible
weight $w(d) = q^d$, $q > 1$); cross-class canonicity (heat-kernel
vs.\ ζ-function vs.\ Pauli-Villars vs.\ point-splitting) is **not
asserted**, correctly named as a Phase-4 open obligation
(`prob:analytic-graph-realization`). **Verdict on stable core**:
SURVIVES, with five sharpenings (W3-W8-01 through W3-W8-05): Capelli
coefficient $\hbar N$ universal inside the admissible class; chain-
level CE/PV associativity exact via Leibniz with no regulator residue,
QME associativity gated by Theorem G's anomaly; chain-level T5 is
classical and integrates without regularization, the "hidden infinity"
lives in the Capelli class that gates C₂(W)-q (W3-W6-05);
ℏ-rescaling consistent across all stable-core members; the Mittag-
Leffler dictionary M-27 encodes a load-bearing order-of-limits
discipline (weight-window inverse limit precedes heat-kernel RG
flow). Five tier-1 statement-only heals + one tier-2
"Regulator scope" subsection in `principles.tex` proposed.
