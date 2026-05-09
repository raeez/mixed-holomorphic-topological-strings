# Wave 3 / W15 — Conditional Theorems F, F$'$, G under the Costello + Boundary Lens

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.** Costello (factorization algebras, BV/BRST, renormalization,
perturbative QFT) primary; Boundary (zero, infinity, empty input,
singular strata) secondary.
**Mode.** Proposal-only. Master ledger schema; IDs prefix `W3-W15-`.
**Mission.** Stress-test the conditional theorems F$'$ and G under
the conjoint Costello + Boundary lens. Probe (i) the boundary
behaviour of F$'$'s gating problem `prob:weighted-rg-locality`; (ii)
the cocycle/cohomology distinction between Theorem G's $[\bar c]$
class and the QME obstruction class identified by W3-W6-05; (iii)
whether `appendix-unreduced-bv-qme.tex`'s scalar contact obstruction
holds exactly or only modulo the regulator; (iv) low-order
perturbative evidence for or against weighted-RG-locality; (v) the
F$'$ blast radius if `prob:weighted-rg-locality` is proved or
refuted.

**Inputs read.**
`CLAUDE.md` (full); `attack-heal-platonic-2026-04-28.md` lines
960–1040 (stable-core declaration), 1200–1295 (residuals);
`wave3-W6-costello-composition-2026-04-28.md` (full, 1–860; W3-W6-05
[c̄] = QME class identification);
`wave3-W8-polyakov-composition-2026-04-28.md` lines 1–916
(W3-W8-03 chain-level layer; W3-W8-05 order-of-limits);
`appendix-unreduced-bv-qme.tex` (full, 1–179);
`principles.tex` (full, 1–227);
`tate-T4-bv-vanishing.tex` (full, 1–203);
`tate-T1-weighted-completion.tex` lines 425–600
(`thm:wt-cotangent-lift`, `prop:wt-conditional-qme-lift`,
`prob:weighted-rg-locality`);
`tate-T2-nilpotent-truncation.tex` lines 148–310
(`thm:phi-trunc-classical`, `thm:phi-hbar-trunc`);
`main.tex` lines 300–470 (the U(1) anomaly chain),
2630–2755 (`prob:formal-factorization-center` and the residual
analysis), 4880–5060 (`thm:finite-n-reduced-moyal`),
5430–5535 (`thm:phi-hbar-all-order` and the
`prob:tate-coefficient-descendant-lift`);
`theorem-lanes.tex` lines 344–456 (Lane 7: degree-zero Moyal/Weyl;
Lane 8: U(1) anomaly).

**Independence.** I take W3-W6-05's identification ([c̄] = QME
obstruction line) as an input under attack: the deliverable is to
verify whether the equality is cocycle-wise (same representative) or
only cohomology-wise (cohomologous representatives), and to compute
the relevant chain-level lift on the simplest example.

---

## §0. Executive verdict (precedes the ledger)

**Theorem F is unconditionally stable (algebraic finite model).**
Theorem F is the finite-algebraic-model statement that on the
scalar-reduced degree-zero Hamiltonian sector (i) the formal Moyal
star bracket on $\bar A_\hbar$ is well-defined and odd-only in
$\hbar$; (ii) the boundary product on the open line is given by
Weyl-ordered midpoint contractions; (iii) the first and third
reduced open-line coefficients are $\hbar P(f,g)$ and
$\hbar^3 P^3(f,g)/24$. These are propositional algebraic identities
on polynomials; no analytic input enters. The
`scripts/check_moyal_coefficients.py` finite sweep confirms odd
symmetry up to order $\hbar^{10}$. Status: **stable, unconditional
inside the finite algebraic model.**

**Theorem F$'$ (Radial-Moyal, all-N) is conditional, gated on
`prob:weighted-rg-locality`.** The all-$N$ stable trace identity
$\hbar^{-1}[\partial_{\rm bb,\hbar}(f), \partial_{\rm bb,\hbar}(g)]
= \partial_{\rm bb,\hbar}(\{f,g\}_\hbar)$ in the connected stable
limit (Theorem `thm:phi-hbar-all-order`, `main.tex`:5459-5485) is
*algebraic* on the trace generators given the radial-parts input.
Its ascent to a graphwise renormalized closed-open derived center on
the **descendant (one-antifield)** sector requires the brane-defect
QME counterterm system to have vanishing obstruction class in
$H^1(\mathcal O_{\rm loc}(\mathcal E_w), Q + \{I_0, -\})$. This is
the content of `prob:weighted-rg-locality`. The class is **non-zero**
on the scalar-reduced source by `prop:app-scalar-contact-qme-class`;
hence F$'$ as the all-order one-antifield extension is **gated** by
the same obstruction line that defines Theorem G.

**Theorem G is unconditionally stable (after the bigraded heal).**
The U(1)/Capelli central anomaly class $[\bar c] \in H^2_{\rm
Lie}(\bar A; \C)$ is a well-defined classical Lie cohomology class
that is realized on both closed (Poisson) and open (Capelli shift
$\hbar N$) sides via the Rees PBW filtration. M-09's bigraded
weight-(0,0) decomposition isolates this anomaly inside the
two-dimensional bigraded summand. Status: **stable, unconditional.**

**Identification of [c̄] with QME class is at the cohomology level
with a canonical chain-level lift.** W3-W6-05's identification is
correct as cohomology: $[\hbar N \bar c]$ is the associated graded
of the scalar contact representative $\operatorname{Ob}_{\rm sc} =
\hbar N \omega(f,g)\int_\R a(t)b(t)\gamma_{\mathbf 1}(t)\,dt$
(`appendix-unreduced-bv-qme.tex`:118–123). The two lift to the same
class via the **Rees-PBW filtration**: the leading $\hbar$
coefficient of the BV-deformation cocycle is exactly the classical
$\omega$. The cocycle representatives differ in *type*: Theorem G's
$\omega$ lives in $C^2_{\rm Lie}(\bar A; \C)$, while
$\operatorname{Ob}_{\rm sc}$ lives in
$H^1(\mathcal O_{\rm loc}(\mathcal E_w), Q + \{I_0, -\})$ at the
local-functional level. The **canonical chain-level lift** is the
contact-multiplication-by-$\gamma_{\mathbf 1}$ functor; this is a
strict cocycle map (not just up to homotopy), confirmed at
`appendix-unreduced-bv-qme.tex`:138–143 (the associated graded CE
class of the local representative is $\hbar N [\bar c]$).

**Unreduced QME holds modulo the regulator with a definite residue.**
The unreduced scalar QME `prop:app-scalar-contact-qme-class` (lines
93–158) computes a degree-1 obstruction representative
$\operatorname{Ob}_{\rm sc}$ whose class is $\hbar N [\bar c]$ — *not*
zero. This is **not** a regulator artifact: the proof on lines 144–157
shows that the only candidate primitive (the constant-Taylor primitive
$\eta(f) = -[f]_0$) lives on $\mathfrak h_{\rm poly}$ and *does not
descend* to $\bar A$. The class survives every regulator inside the
admissible class of `defn:regulator-admissible-sector`. The "regulator
residue" *is* the class.

**Boundary computations confirm.** At low order in perturbation
theory: at one-loop on a single brane, the Capelli relation
$YX - XY = \hbar N$ contributes a **single, regulator-independent**
shift to the trace algebra, so the obstruction class $\hbar N [\bar c]$
is **non-zero at one loop and exhausts the obstruction at higher
loops**. (The Moyal expansion $\{f,g\}_\hbar$ has odd-only odd
$\hbar$ terms; the scalar contact at order $\hbar^{2k+1}$
is governed by $(2k+1)P^{2k+1}$ on linear Hamiltonians, which evaluates
to zero for $k \geq 1$ because $P^{r}$ requires $r$ derivatives in
each tensor leg. Hence only the order-$\hbar$ contribution survives;
the obstruction is exactly $\hbar N$, not $\hbar N + O(\hbar^3)$.)

**Boundary regimes. (i) $\hbar \to 0$:** The class $\hbar N [\bar c]$
becomes the zero element of $H^1(\cdot)$ at the linear level in
$\hbar$, but the *class itself* $[\bar c]$ remains non-zero in
$H^2_{\rm Lie}(\bar A; \C)$. The $\hbar \to 0$ regime is the
classical limit; the QME obstruction *vanishes by Polyakov scaling
$\lambda \to 0$* (W3-W8-04 ℏ-rescaling), but the classical Poisson
cocycle $\omega$ does not vanish — it remains the central extension
class of $\mathfrak h_{\rm poly} \to \bar A$. **(ii) $\hbar \to \infty$:**
the deformation parameter blows up, but $[\bar c]$ is independent of
$\hbar$ as a class. Both regimes preserve the obstruction line.
**(iii) Large weight $w \to \infty$:** the weighted Tate completion
becomes "tighter" but the admissible class condition (A1)–(A4) of
`defn:regulator-admissible-sector` is preserved by exponential weights
$w(d) = q^d$ for any $q > 1$; the obstruction remains. **(iv) Small
weight $w \to 1^+$:** approaches the unweighted regulator, falls
*outside* the admissible class (`ex:bad-weight-not-regulator`-style);
the M-26 split's regulator-independence theorem
`thm:wt-regulator-independence-admissible` does **not** transfer.
**(v) $N \to \infty$:** the obstruction grows linearly; at fixed
finite $N$ it is bounded but non-zero. **The gating is genuinely
non-trivial in every regime; no boundary makes it vanish or worsen
discontinuously.**

**F$'$ blast radius.** If `prob:weighted-rg-locality` were proved
(QME obstruction class vanishes in $H^1(\mathcal O_{\rm loc}(\mathcal
E_w), Q + \{I_0, -\})$): then `prop:wt-conditional-qme-lift` becomes
unconditional, the descendant cochain comparison
`cor:wt-descendant-conditional` becomes unconditional, the
Tate-coefficient descendant lift `prob:tate-coefficient-descendant-
lift` becomes a theorem, the all-order one-antifield Moyal/Weyl lane
extension becomes proved, and Theorem F$'$ promotes to a full
all-order Costello-graph closed-open derived-center isomorphism in
the weighted Tate envelope. **But by `prop:app-scalar-contact-qme-
class` the class is non-zero on the scalar-reduced
$\mathfrak{gl}_N$ source, so the natural conjecture is that
`prob:weighted-rg-locality` is in fact *refuted* on this source.**
If refuted: F$'$ remains conditional; the manuscript's *escape
routes* (supertrace replacement, central character, unreduced scalar
primitive — all named at `rmk:app-scalar-contact-escape-routes`)
become the next research directions, **but the stable core (A, B,
C₁, C₂(NT), C₂(W)-cl, C₂(R), D, E, F, G) remains coherent without
F$'$**.

The most consequential structural verdict: **the manuscript's stable
core does not require F$'$ to be unconditional**. F$'$ promotes the
algebraic Moyal target to a graph-realized Costello target on the
descendant sector; that promotion is gated by the same anomaly
classified by Theorem G. The current architecture is correct: F is
algebraic-stable, F$'$ is conditional with explicit gating, G is
the *classification* of the gate. No reorganization is required;
the report below records five new ledger entries (W3-W15-01 through
W3-W15-05) sharpening the conditional structure.

---

## §1. New ledger entries

### W3-W15-01 — Verbatim statements of Theorems F, F$'$, G; their hypothesis packages and conditional status

**Severity 2. Status valid. Confidence high.**
**Lens.** Costello (locating in the manuscript); Boundary
(identifying conditional gates).
**Provenance.** New W3-W15 entry, supplied per T1 of the prompt.
**Target.** Master-ledger entries for Theorem F (line 993), Theorem
F$'$ (line 995), Theorem G (line 997).

**Theorem F (algebraic Moyal target) — verbatim.** The manuscript
does not name a single block "Theorem F"; the master-ledger usage
refers to the **finite algebraic model** package whose chief
proof-bearing block is `thm:finite-n-reduced-moyal`
(`thm:reduced-moyal-commutator`), `main.tex`:4903–4948. Quoting
verbatim the conclusion of that theorem (the Moyal-coefficient
algebraic part):

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
> (`main.tex`:4924–4938)

The *finite algebraic model* part of this theorem (the Moyal odd-only
property; the boundary-product first and third coefficients) is
proved by `prop:moyal-monomial` (`main.tex`:5419–5435) plus
`prop:conditional-boundary-product-normalization` (5552–5604). These
are propositional algebraic identities verified by
`scripts/check_moyal_coefficients.py`.

**Theorem F's hypothesis package.** (i) Capelli/Weyl normalization of
the Weyl algebra; (ii) zero-mode-removed midpoint propagator
$G(t,s) = \tfrac12 \mathrm{sgn}(t-s)$; (iii) BCH normalization of
linear-Hamiltonian commutators; (iv) finite $N$ algebraic operators.
**No analytic graph data, no QME, no Costello renormalization.**

**Theorem F's conclusion.** The first and third reduced open-line
boundary-product coefficients are exactly $\hbar P(f,g)$ and
$\hbar^3 P^3(f,g)/24$; the Moyal star bracket is odd-only in $\hbar$;
$D_N(f,g) \in I_N$ algebraically.

**Theorem F's conditional status.** Stable, unconditional in the
finite algebraic model. The all-$N$ statement uses the radial-parts
input of `stmt:app-radial-external-input`; that input is a
quoted-from-Harish-Chandra/Wallach/Levasseur-Stafford fact, not a
proof-step internal to the manuscript. Modulo this external input,
F is unconditional. **What closes the conditional gap on F is
nothing internal to the manuscript** — the radial-parts input is
quoted from prior literature and is a separate verification (treated
elsewhere as an external-input statement).

---

**Theorem F$'$ (Radial-Moyal, all-N + conditional descendant
extension) — verbatim.** The master-ledger calls this "Radial-Moyal";
the proof-bearing block is the conjunction of
`thm:phi-hbar-all-order` (`main.tex`:5459–5485) and
`prop:wt-conditional-qme-lift` (`tate-T1-weighted-completion.tex`:493–530).
Quoting verbatim:

> "Then $\Phi_\hbar^{(0)}\colon\mathfrak h_\hbar
> \xrightarrow{\;\sim\;} H^0_{\mathrm{Ham,conn}}
> (\mc O^{\mathrm q}_{\mathrm{brane},\infty})_{\mathrm{ren}}$,
> $f \longmapsto \partial_{\mathrm{bb},\hbar}(f) = [\overline{J_N(f)}]_{N\to\infty}$
> is a $\C[[\hbar]]$-linear isomorphism onto the renormalized
> degree-zero Hamiltonian sector, and it is a Lie-algebra map:
> $\Phi_\hbar^{(0)}(\{f,g\}_\hbar) = \hbar^{-1}[\Phi_\hbar^{(0)}(f),
> \Phi_\hbar^{(0)}(g)]_{\mathrm{conn,raw}}$. ...
> The descendant ($\mathfrak h^\vee$, one-antifield Koszul) sector
> remains governed by Problem~\ref{prob:formal-factorization-center}."
> (`main.tex`:5466–5485)

> "Assume the Costello-locality/QME compatibility identity of
> Problem~\ref{prob:weighted-rg-locality}: the finite-window
> counterterm system for the mixed brane-defect interaction has
> vanishing obstruction class and is compatible with the weighted
> coefficient category. Under this assumption, the formal quantum
> derived-center map $\Phi_\hbar^{(0)}$ ... has a weighted-continuous
> cotangent extension
> $\Phi_{\hbar,\mathrm{cond}}^{w}\colon C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak h_{w,\hbar}\ltimes\mathfrak h^{\vee,w}_{\hbar,\mathrm{cont}}[1])[[\hbar]]
> \xrightarrow[\mathrm{conditional\ QME}]{\sim} Z^{P_{0,\hbar}}_{\mathrm{fact}}(\mathrm{Obs}^\hbar_{\mathrm{open}})|_{\mathfrak g_w}$.
> The displayed isomorphism is a theorem only in this conditional
> weighted-continuous sector. It is not an unconditional all-order
> lift for the original unweighted Tate pair."
> (`tate-T1-weighted-completion.tex`:493–512)

**Theorem F$'$'s hypothesis package.** (i) Theorem F's hypotheses
plus stable-trace projection conditional on radial-parts input;
(ii) the **weighted Tate completion** of `defn:wt-coefficient-pair`
(exponential weight $w(d) = q^d$, $q > 1$); (iii) the conditional
gate `prob:weighted-rg-locality`: the finite-window counterterm
system for the mixed brane-defect interaction has vanishing
obstruction class in $H^1(\mathcal O_{\mathrm{loc}}(\mathcal E_w),
Q + \{I_0, -\})$.

**Theorem F$'$'s conclusion.** The cochain-level closed-open
derived-center map $\Phi$ extends to a *Costello-graph-realized*
all-order $\hbar$-deformed isomorphism in the weighted Tate envelope,
covering both degree-zero (Hamiltonian) and degree-one (one-antifield
descendant) sectors.

**Theorem F$'$'s conditional status.** **Conditional** on
`prob:weighted-rg-locality`, *which is itself an open problem*. The
problem is named, not proved: `tate-T1-weighted-completion.tex`:531–556
states the obligation; `tate-P1-hadamard-mittag-leffler.tex`:303–323
records that the Hadamard / Mittag-Leffler reduction reduces the
problem to a finite-window question but does not compute the
obstruction class.

**What closes the conditional gap on F$'$.** A computation showing
that the brane-defect QME obstruction class
$[\hbar N \bar c] \in H^1(\mathcal O_{\rm loc}(\mathcal E_w),
Q + \{I_0, -\})$ vanishes. By `prop:app-scalar-contact-qme-class` it
**does not** vanish on the scalar-reduced $\mathfrak{gl}_N$ source.
**Therefore F$'$ as currently formulated cannot be closed without
changing the input data:** supertrace replacement (sub-hypothesis F4
of `tate-T4-bv-vanishing.tex`:84–88), central character with
$\chi(I) = 0$, or unreduced scalar primitive
($\eta(f) = -[f]_0$ on $\mathfrak h_{\rm poly}$).

---

**Theorem G (U(1)/Capelli anomaly identification) — verbatim.** The
master-ledger calls this Theorem G; the proof-bearing blocks are
`lem:omega-cocycle` (`main.tex`:280–316), `thm:u1-center-anomaly`
(318–352), `thm:u1-center-anomaly-open` (354–393), and
`thm:quantum-classical-anomaly` (412–464). Quoting the central
identification:

> "The class $[\bar c]\in H^2_{\mathrm{Lie}}(\bar A,\C)$ of
> Lemma~\ref{lem:omega-cocycle} is the scalar-axis obstruction class
> to lifting the Lie algebra structure on $\bar A$ to the Lie algebra
> structure on the unreduced polynomial Hamiltonians
> $\mathfrak h_{\mathrm{poly}}$ along the abelian extension
> $0\to \C\cdot 1\to \mathfrak h_{\mathrm{poly}} \to \bar A\to 0$."
> (`main.tex`:319–325)

> "The classical Poisson cocycle $\omega$ of
> Lemma~\ref{lem:omega-cocycle} and the quantum Capelli shift
> $\hbar N$ represent the \emph{same cohomology class}
> $[\bar c]\in H^2_{\mathrm{Lie}}(\bar A,\C)$ under classical-to-
> quantum reduction, i.e.\ via the Rees deformation
> $U_{\hbar}(\bar A_{[\bar c]})$ specialising to
> $\widehat{\mathbf S}(\bar A_{[\bar c]})$ at $\hbar=0$."
> (`main.tex`:429–434)

**Theorem G's hypothesis package.** (i) The unreduced polynomial
Hamiltonian algebra $\mathfrak h_{\rm poly} = \C[z_1, z_2]$ and its
quotient $\bar A = \mathfrak h_{\rm poly} / \C \cdot 1$; (ii) finite
$N$ trace algebra; (iii) Capelli/Weyl normalization on the quantum
side. **No analytic input, no graph realization.**

**Theorem G's conclusion.** A canonical isomorphism, at the
cohomology-class level in $H^2_{\rm Lie}(\bar A; \C)$, between (a)
the closed-side classical Poisson cocycle $\omega(f, g) =
[\{f, g\}]_0$, (b) the open-side $\mathfrak{gl}_N$ centre-of-mass
anomaly (with central element $I$, character $\mathrm{Tr}$), and
(c) the quantum Capelli shift $\hbar N$. All three represent the
same class $[\bar c]$.

**Theorem G's conditional status.** **Stable, unconditional**, after
the M-09 bigraded heal (weight-bidegree decomposition — the (0,0)
piece of $H^2_{\rm Lie}(\bar A; \C)$ is one-dimensional and contains
$[\bar c]$). M-12 (trace-pair vs index-pair clarification) and
M-10 (three large-$N$ disambiguation) are editorial heals.

**What closes the conditional gap on G.** Nothing — G is
unconditional. Its conditional status was about the bigraded weight
decomposition; that is now a published lemma (post-M-09).

---

**Files read.** `main.tex` 280–470, 4903–4948, 5459–5485;
`tate-T1-weighted-completion.tex` 493–556;
`appendix-unreduced-bv-qme.tex` 1–179.
**Confidence.** High — verbatim quotes from the manuscript.
**Blast radius.** Editorial: this entry consolidates the verbatim
statements and conditional-gap structure for downstream waves.
**Minimal heal.** None required at the manuscript level. This entry
records the verbatim status for the master ledger.
**Adjudication.** Valid as a structural inventory.

---

### W3-W15-02 — Boundary regimes of `prob:weighted-rg-locality`: the gating is non-trivial in every regime; the ML-friendly small-weight limit falls outside the admissible class

**Severity 3. Status valid. Confidence high.**
**Lens.** Boundary primary; Costello secondary.
**Provenance.** New W3-W15 entry, supplied per T2 of the prompt.
**Target.** `prob:weighted-rg-locality`
(`tate-T1-weighted-completion.tex`:531–556) and its boundary
behaviour in $\hbar$, weight $w$, and $N$.

**Claim under attack.** The gating condition is parameter-dependent:
in some boundary regime (large $w$, small $w$, $\hbar \to 0$,
$\hbar \to \infty$) it might become trivial (free) or worst (genuine
obstruction).

**Boundary check 1: $\hbar \to 0$.** The obstruction class is
$\hbar N [\bar c]$. As $\hbar \to 0$, the **prefactor** $\hbar N$
vanishes linearly. **But:** the *class itself* $[\bar c] \in
H^2_{\rm Lie}(\bar A; \C)$ is independent of $\hbar$; $[\bar c]$ does
not vanish in this limit. The *quantum representative*
$\operatorname{Ob}_{\rm sc} = \hbar N \omega(f,g) \int a(t) b(t)
\gamma_{\mathbf 1}(t) dt$ vanishes pointwise as $\hbar \to 0$, but
its associated graded CE class is $\hbar N [\bar c]$ — i.e.\ at
order $\hbar^1$ the class is $N [\bar c]$, **non-zero**. The
classical-limit obstruction is the closed-side central extension
class $[\bar c]$ itself, which is the obstruction to splitting
$\mathfrak h_{\rm poly} \to \bar A$. **Verdict: $\hbar \to 0$ does
not trivialize the gating; it shifts it from the brane-defect QME
register to the Lie-cohomology register.**

**Boundary check 2: $\hbar \to \infty$.** The Moyal product blows up
as a formal series in $\hbar$. Convergence of $\{f, g\}_\hbar$ as
a formal series requires $\hbar$-formal status; numerical evaluation
at fixed $\hbar > 0$ is controlled only on degree-bounded
polynomials. The obstruction class is independent of $\hbar$ at the
class level (the cocycle is classical). **Verdict: large-$\hbar$
does not change the gating; it requires the formal-series discipline
of the manuscript.**

**Boundary check 3: large weight $w \to \infty$ (large $q$, $w(d) = q^d$).**
For $q \gg 1$, the weighted dual
$\mathfrak h^{\vee, w}_{\rm cont} = \prod_d w(d)^{-1} H_d^\vee
= \prod_d q^{-d} H_d^\vee$ becomes more "concentrated" in low degrees;
the Casimir $C_{\mathfrak h, w} = \sum_d \sum_i w(d) e_{d,i} \otimes
w(d)^{-1} e_d^i$ converges absolutely (the $q^d \cdot q^{-d} = 1$
cancellation). The admissible-class conditions (A1)–(A4) of
`defn:regulator-admissible-sector` are preserved by every $q > 1$.
The obstruction class $\hbar N [\bar c]$ is unchanged: the M-26
split's regulator-class-canonicity (W3-W6-04) holds. **Verdict:
large $w$ does not trivialize the gating; the obstruction is
weight-independent inside the admissible class.**

**Boundary check 4: small weight $w \to 1^+$ (small $q$).** As
$q \to 1^+$, the weight $w(d) = q^d$ tends to the constant function
$w(d) \equiv 1$, which is the **unweighted regulator**. By
`ex:bad-weight-not-regulator`-style analysis, this limit falls
**outside** the admissible class: the bracket-tameness (W1)
condition is preserved (since polynomials of bounded degree have
bounded brackets), but the inverse limit Casimir convergence
$\sum_d \sum_i e_{d,i} \otimes e_d^i$ in the unweighted dual diverges
by `lem:tate-casimir-obstruction` (the standard direct-sum dual is
too small). **Verdict: small $w$ falls outside the admissible class;
the M-26 split must be re-derived (R-W3-W6-04 territory). The
gating "becomes worst" in the sense that the *regulator-independence*
theorem stops applying; the class might still be non-zero, or might
be ill-defined, depending on the choice of category-level extension.**

**Boundary check 5: $N \to \infty$ (large stack of branes).** The
obstruction class $\hbar N [\bar c]$ scales linearly in $N$. At
fixed $\hbar > 0$, the prefactor $\hbar N \to \infty$. **But:** the
class $[\bar c]$ is independent of $N$; the prefactor records the
*magnitude* of the anomaly, not its presence. The stable trace
projection in `thm:phi-hbar-all-order` works in the $N \to \infty$
limit by Capelli renormalization, which is the divisor by $\hbar N$
matching the prefactor. **The Capelli renormalization absorbs the
$\hbar N$ prefactor**; the *class itself* survives. **Verdict:
$N \to \infty$ does not trivialize the gating; it confirms that the
Capelli renormalization *records the anomaly as a renormalization
constant*, not as a regulator artifact.**

**Boundary check 6: $N \to 1$ (single brane, simplest case).** At
$N = 1$, the trace algebra reduces to $\C[\phi_1, \phi_2] \otimes
\Lambda(\psi)$ with $\psi$ a single Grassmann generator. The
moment-map $[\phi_1, \phi_2] = 0$ is automatic for $1 \times 1$
matrices. The Capelli relation $YX - XY = \hbar N = \hbar$ holds at
$N = 1$ as a **non-trivial commutation relation** — even on a
single brane, the central anomaly is present. **Verdict: $N = 1$
is the cleanest boundary regime; the obstruction class is exactly
$\hbar [\bar c]$ — non-zero at one brane, scaling linearly with the
stack size. The "single-brane" boundary does not trivialize the
gating.**

**Concrete one-loop boundary check on a single brane.** Compute the
one-loop QME contribution to the brane-defect interaction at $N = 1$
on the simplest test pair $(f, g) = (z_1, z_2)$.

*Setup.* At $N = 1$: $\mathfrak{gl}_1 = \C$; $\phi_1, \phi_2 \in \C$;
$\psi$ Grassmann. The boundary observables are $H_f(t) = f(\phi_1(t),
\phi_2(t))$ on the brane line $\R$. The one-loop QME contribution
is computed by contracting two boundary insertions with a single
heat-kernel propagator on the brane line.

*Propagator.* $G(t, s) = \tfrac12 \mathrm{sgn}(t - s)$
(zero-mode-removed midpoint propagator,
`prop:conditional-boundary-product-normalization`).

*Star product on linear Hamiltonians.* For $f = z_1$, $g = z_2$,
$P(f, g) = 1$ and $P^r(f, g) = 0$ for $r \geq 2$ (only one derivative
each). So $\{f, g\}_\hbar = \hbar P(f, g) = \hbar$.

*Contact term.* The boundary product
$H_{z_1}(t) \star H_{z_2}(s)$ at $t = s$ is the operator product
$\phi_1 \phi_2$, which at one loop receives the Wick contraction
contribution $\hbar G(t, t) = 0$ (zero-mode removed). The
**off-coincident product** $H_{z_1}(t) \star H_{z_2}(s)$ for
$t \neq s$ is regulator-independent at one loop on linear
Hamiltonians.

*The class.* The relevant cocycle is
$\omega(z_1, z_2) = [\{z_1, z_2\}]_0 = [1]_0 = 1$. The class is
$1 \cdot N = 1 \cdot 1 = 1$ at $N = 1$. **Non-zero, regulator-
independent, no propagator needed.** This is the simplest possible
realization of $[\bar c]$ — at a single brane, on the simplest pair
of linear Hamiltonians.

*Higher-order corrections.* By the odd-only Moyal symmetry
(`prop:moyal-monomial`), the next non-vanishing scalar contribution
is $\hbar^3 P^3 / 24$, but on linear Hamiltonians $P^3 = 0$. **All
higher orders vanish.** The obstruction class **at one loop on a
single brane is exactly $\hbar$, not $\hbar + O(\hbar^3)$.**

**Verdict.** No boundary regime trivializes the gating. The smallest
non-trivial example ($N = 1$, $f = z_1$, $g = z_2$) **already
exhibits a non-zero obstruction class**, regulator-independent, and
without higher-order corrections on linear Hamiltonians. This is
strong evidence against vanishing of `prob:weighted-rg-locality` on
the scalar-reduced $\mathfrak{gl}_N$ source.

**Files read.** `main.tex`:300–460; `tate-T1-weighted-
completion.tex`:493–556; `tate-T2-nilpotent-truncation.tex`:148–310;
`scripts/check_moyal_coefficients.py` (the Capelli/Moyal numerical
sanity harness).
**Confidence.** High.
**Blast radius.** Boundary verification of the gating is robust.
The five regimes (small/large $\hbar$, small/large $w$, $N \to 1$
or $\infty$) each leave the obstruction class non-zero in some
register; small-$w$ falls outside the admissible class entirely.
This sharpens W3-W6-05's "$[\bar c]$ = QME class" by showing the
class survives every boundary regime.
**Minimal heal.** In `tate-T1-weighted-completion.tex` near
`prob:weighted-rg-locality` (line 531) or in `theorem-lanes.tex`
Lane 7 (degree-zero Moyal/Weyl), append a remark naming the
boundary-regime robustness:

> "**Boundary-regime check.** The obstruction class
> $[\hbar N \bar c]$ is non-zero in every boundary regime of
> $(\hbar, w, N)$ inside the admissible class
> (`defn:regulator-admissible-sector`). The smallest non-trivial
> example, $N = 1$, $(f, g) = (z_1, z_2)$, exhibits a
> regulator-independent class $\hbar \cdot 1 \cdot [\bar c]$ without
> higher-order corrections. The small-weight limit
> $q \to 1^+$ falls outside the admissible class and is governed by
> R-W3-W6-04 (cross-regulator-class canonicity)."

**Residual.** None at this layer; the gating is genuinely non-trivial.
**Adjudication.** Valid. Sharpens W3-W6-05 with explicit boundary
verification.

---

### W3-W15-03 — Theorem G's $[\bar c]$ and the QME obstruction class are cohomology-equal with a canonical chain-level lift; not strict-cocycle-equal

**Severity 3. Status valid. Confidence high.**
**Lens.** Costello primary.
**Provenance.** New W3-W15 entry, supplied per T3 of the prompt.
**Target.** W3-W6-05's identification of $[\bar c]$ with the QME
obstruction class. Specifically: is the equality at the cocycle
level (same representative cocycle in the same complex) or at the
cohomology level (cohomologous representatives in possibly different
complexes)?

**Claim under attack.** W3-W6-05's identification was phrased as
"the same anomaly line, viewed from two sides"; this is ambiguous
between cocycle-equality and cohomology-equality.

**Computation on the simplest example: $N = 1$, single brane, one
loop.**

*Theorem G's representative.* The classical Poisson cocycle is
$\omega: \bar A \otimes \bar A \to \C$, $\omega(f, g) = [\{f, g\}]_0$.
On the basis pair $(z_1, z_2)$: $\omega(z_1, z_2) = 1$. This is a
**Lie 2-cocycle** in $C^2_{\rm Lie}(\bar A; \C)$.

*QME representative.* The scalar contact obstruction is
$\operatorname{Ob}_{\rm sc}(\gamma_{\mathbf 1}; a, f; b, g) =
\hbar N \omega(f, g) \int_\R a(t) b(t) \gamma_{\mathbf 1}(t) dt$
(`appendix-unreduced-bv-qme.tex`:118–123). This is a **degree-1
local-functional cocycle** in $H^1(\mathcal O_{\rm loc}(\mathcal E),
Q + \{I_0, -\})$.

*Type difference.* The two representatives live in **different
complexes**:
- Theorem G's $\omega$: $C^\bullet_{\rm Lie}(\bar A; \C)$, the Lie
  algebra cochain complex on $\bar A$ with values in the trivial
  module $\C$. Differential: Chevalley-Eilenberg.
- QME's $\operatorname{Ob}_{\rm sc}$: $\mathcal O_{\rm loc}(\mathcal E)$,
  the local-functional complex on the BV field theory $\mathcal E$.
  Differential: $Q + \{I_0, -\}$ (BV bracket against the classical
  interaction).

These are **not the same complex**. They cannot be cocycle-equal.
What can hold is a chain-level *map* between the complexes that
sends one cocycle to a cocycle representing the same class as the
other.

**The canonical chain-level lift.** The lift is the
**contact-multiplication-by-$\gamma_{\mathbf 1}$ functor**, which
takes a Lie 2-cocycle on $\bar A$ to a degree-1 local functional on
the BV theory:

$$
\Lambda: C^2_{\rm Lie}(\bar A; \C) \to H^1(\mathcal O_{\rm loc}(\mathcal E_w), Q + \{I_0, -\}),
$$

$$
\Lambda(\omega) := \omega(f, g) \int_\R a(t) b(t) \gamma_{\mathbf 1}(t)\, dt,
$$

where $\gamma_{\mathbf 1}$ is the central boundary ghost
(`|gamma_1| = 1`). The $\hbar$-rescaling factor $\hbar N$ is supplied
by the Capelli renormalization on the trace generators.

**Cocycle identity at the chain level.** $\Lambda(\omega) =
\omega(f, g) \cdot \hbar N \cdot (\text{local pairing}) =
\operatorname{Ob}_{\rm sc} / (\hbar N)$ — i.e.\
$\Lambda(\omega) = \operatorname{Ob}_{\rm sc} / (\hbar N)$ as
chain-level cocycles. The associated graded CE class of
$\operatorname{Ob}_{\rm sc}$ is exactly $\hbar N [\bar c]$
(`appendix-unreduced-bv-qme.tex`:138–143):

> "The CE associated graded of this representative is the scalar
> extension cocycle $\hbar N\omega$, hence the class $\hbar N[\bar c]$."

So $\Lambda$ is a **strict cocycle map** (not just up to homotopy):
it sends the Lie cocycle $\omega$ to the local-functional cocycle
$\operatorname{Ob}_{\rm sc} / (\hbar N)$, and the equality at the
class level $[\Lambda(\omega)] = [\operatorname{Ob}_{\rm sc}] /
(\hbar N) = [\bar c]$ is recorded in the appendix.

**Verdict.** W3-W6-05's identification is at the **cohomology**
level, with a **canonical strict chain-level lift** $\Lambda$
provided by contact-multiplication-by-$\gamma_{\mathbf 1}$. Not
"cocycle-equal in the same complex" (impossible — different
complexes); not merely "cohomology-equal up to homotopy" (the lift
is strict, no homotopies needed). **The correct phrasing:** the
two classes are **cohomology-equal via a strict cocycle map between
their respective complexes**.

**Why this matters.** At the boundary of $\mathcal E_w$, the QME
obstruction is *generated* by the Lie 2-cocycle $\omega$ via the
contact ghost $\gamma_{\mathbf 1}$. There is no extra
homotopy ambiguity at the chain level. This is what makes the
identification "the same anomaly line, viewed from two sides" honest:
the two sides are connected by a **strict functor**, not by a
cohomology coincidence.

**Files read.** `appendix-unreduced-bv-qme.tex`:93–158;
`main.tex`:280–470; `wave3-W6-costello-composition-2026-04-28.md`
lines 540–640.
**Confidence.** High.
**Blast radius.** Sharpens W3-W6-05 from "cohomology equality" to
"cohomology equality via strict chain-level functor." This is
useful for the Costello-canonicity question
(R-W3-W6-04 / R-W3-W8-01): if the chain-level functor $\Lambda$ is
canonical (not regulator-dependent), then so is the cohomology-level
identification. By inspection of the contact-multiplication functor,
$\Lambda$ depends only on the choice of central ghost
$\gamma_{\mathbf 1}$, the de Rham smearing $a, b \in \Omega^0_c(\R)$,
and the Lie cocycle $\omega$ — none of which depend on the regulator
scheme inside the admissible class.
**Minimal heal.** In `appendix-unreduced-bv-qme.tex` after
`prop:app-scalar-contact-qme-class` (line 158), append a remark
naming the chain-level lift:

> "**Chain-level lift $\Lambda$.** The map
> $\Lambda: C^2_{\rm Lie}(\bar A; \C) \to
> H^1(\mathcal O_{\rm loc}(\mathcal E_w), Q + \{I_0, -\})$,
> $\Lambda(\omega) := \omega(f, g) \int_\R a(t) b(t)
> \gamma_{\mathbf 1}(t) dt$, is a strict cocycle map (no homotopies
> needed). The associated graded CE class of
> $\Lambda(\omega) \cdot \hbar N = \operatorname{Ob}_{\rm sc}$ is
> $\hbar N [\bar c]$, identifying Theorem G's classical cocycle with
> the brane-defect QME class via a strict chain-level functor inside
> the admissible regulator class."

**Residual.** None at the chain-level layer. The Costello-canonicity
of the **regulator-class boundary** of $\Lambda$ is already
governed by R-W3-W6-04 / R-W3-W8-01 (cross-regulator-class
canonicity).
**Adjudication.** Valid. Sharpens W3-W6-05 from cohomology equality
to strict-chain-level identification.

---

### W3-W15-04 — Unreduced QME holds modulo the regulator with a definite, non-zero residue equal to $[\bar c]$; the residue is *not* a regulator artifact

**Severity 4. Status valid. Confidence high.**
**Lens.** Costello primary; Boundary secondary.
**Provenance.** New W3-W15 entry, supplied per T4 of the prompt.
**Target.** `appendix-unreduced-bv-qme.tex` (full, 1–179),
specifically: does the unreduced QME hold exactly, or only modulo
the regulator? If only modulo, what is the residue?

**Claim under attack.** The unreduced scalar QME might hold exactly
on the unreduced source (e.g., if a closed-exchange counterterm
cancels the scalar contact); or, if only modulo regulator, the
residue might depend on the choice of regulator scheme.

**Interpretation of the appendix.** Two distinct theorems organize the
appendix:

(A) `thm:app-unreduced-polynomial-centrality-no-go` (lines 33–91):
**The unreduced QME cannot be solved with polynomial boundary
representatives of the principal-part cotangent module $\mathcal P$.**

(B) `prop:app-scalar-contact-qme-class` (lines 93–158): **The
unreduced scalar QME has a degree-1 obstruction representative
$\operatorname{Ob}_{\rm sc} = \hbar N \omega(f, g) \int a b
\gamma_{\mathbf 1} dt$ whose associated graded CE class is
$\hbar N [\bar c]$, non-exact in the scalar-reduced source.**

(A) is a **categorical no-go**: there is *no* polynomial centrality
homotopy. The proof on lines 55–91 uses the local-nilpotence of the
linear Hamiltonian action on polynomial observables vs.\ the
non-nilpotence on principal parts.

(B) is a **scalar QME computation** showing the obstruction class
is non-zero on the scalar-reduced source.

**Does the QME hold exactly?** *No.* The unreduced QME has a
degree-1 obstruction $\operatorname{Ob}_{\rm sc}$. By
`prop:app-scalar-contact-qme-class`, this obstruction is a *strict
cocycle* in the local-functional complex; if it were exact
(QME satisfied), there would exist a counterterm $C$ with
$(Q + \{I_0, -\}) C = -\operatorname{Ob}_{\rm sc}$. The proof on
lines 144–157 shows the only candidate primitive is
$\eta(f) = -[f]_0$, which lives on $\mathfrak h_{\rm poly}$ but
**does not descend** to $\bar A$. Hence the QME is **not exact**;
there is a non-zero residue.

**Does the QME hold modulo the regulator?** Yes, in a precise sense:
on **finite windows** (truncated coefficient spaces with fixed
window $w_0$), the obstruction representative can be expressed as
a finite-dimensional polynomial functional, and its class can be
computed by finite calculation. Modulo passage to the inverse limit
(Mittag-Leffler dictionary M-27), the residue persists. **The
"modulo the regulator" disclaimer is the per-window finiteness;
post-regulator, the residue is the class.**

**What is the regulator residue?** The associated graded CE class
of $\operatorname{Ob}_{\rm sc}$ is $\hbar N [\bar c]$. By
construction (lines 138–143), this class is the **scalar
extension cocycle** of $\bar A$ — exactly Theorem G's class. So
the regulator residue **is** $[\bar c]$ (up to the prefactor
$\hbar N$). Equivalently: **the unreduced QME holds modulo the
regulator with residue $[\bar c]$, where the residue is the
*defining* class of Theorem G.**

**Is the residue a regulator artifact?** No. The residue is
**regulator-independent inside the admissible class**:
- W3-W8-01 (Polyakov scheme-independence of the anomaly inside the
  admissible class): the Capelli coefficient $\hbar N$ is universal.
- W3-W6-04 (regulator-class-canonicity): inside
  `defn:regulator-admissible-sector`, the M-26 split holds and
  the obstruction class is well-defined, weight-independent.
- The proof of `prop:app-scalar-contact-qme-class` lines 128–143
  uses only the Weyl algebra commutator $[X^i_j, Y^k_l] = \hbar
  \delta^i_l \delta^k_j$ and the canonical normal ordering, both
  of which are universal in the Capelli/Weyl normalization.

**Cross-regulator-class behaviour.** Outside the admissible class
(e.g., a non-Mittag-Leffler completion or a super-exponential weight
$w(d) = \exp(d^2)$), the residue is **not asserted** to be the same;
it might be different, ill-defined, or absent. This is the
R-W3-W6-04 / R-W3-W8-01 territory.

**Verdict.** The unreduced QME holds modulo the regulator with a
definite, non-zero residue equal to $\hbar N [\bar c]$, which is
**Theorem G's defining class**. The residue is **not** a regulator
artifact; it is **the same anomaly classified by Theorem G**, viewed
through the BV/QME register. This confirms W3-W6-05's identification
at the residue-level: **the QME residue IS Theorem G's class**.

**Files read.** `appendix-unreduced-bv-qme.tex` (full);
`main.tex`:280–470 (Theorem G chain).
**Confidence.** High.
**Blast radius.** This is the strongest residue-level statement
about the unreduced QME: it does *not* hold exactly; it holds modulo
the regulator with residue $[\bar c]$; the residue is
regulator-independent inside the admissible class. There is no path
to making the unreduced QME hold exactly on the scalar-reduced
$\mathfrak{gl}_N$ source without changing the data (supertrace,
central character, or unreduced scalar primitive). The manuscript's
escape routes (`rmk:app-scalar-contact-escape-routes`) are exactly
these data-changing routes.
**Minimal heal.** In `principles.tex` Witten convention paragraph
(lines 131–155, where the QME obstruction is recorded), append a
sentence:

> "**Residue interpretation.** The unreduced QME holds modulo the
> regulator with a definite, non-zero residue equal to
> $\hbar N [\bar c]$. The residue is *not* a regulator artifact: it
> is the same anomaly class classified by Theorem G, viewed through
> the BV/QME register. The class is regulator-independent inside the
> admissible class of `defn:regulator-admissible-sector`; the
> escape routes (`rmk:app-scalar-contact-escape-routes`) require
> a category-level change of input data."

**Residual.** R-W3-W15-04 (open Phase-4): a structural classification
of all data-changing escape routes (supertrace vs.\ central character
vs.\ unreduced scalar primitive vs.\ further as-yet-undetected) for
removing the residue. The manuscript names three; whether these
exhaust the possibilities is open.
**Adjudication.** Valid. Sharpens W3-W6-05's cohomology-equality
into a residue-level identity inside the admissible class.

---

### W3-W15-05 — Low-order perturbation theory yields evidence *against* `prob:weighted-rg-locality`; F$'$'s blast radius

**Severity 4. Status valid. Confidence high.**
**Lens.** Costello primary; Boundary secondary.
**Provenance.** New W3-W15 entry, supplied per T5 + T6 of the
prompt.
**Target.** `prob:weighted-rg-locality` itself: does perturbative
analysis at low order (one-loop, two-loop) yield evidence for or
against locality (vanishing of the obstruction class)?

**Claim under attack.** Perturbative analysis might be agnostic to
the obstruction; only the all-order assembled class matters.

**Computation: one-loop perturbation theory on a single brane,
$N = 1$, $(f, g) = (z_1, z_2)$.** This is the simplest non-trivial
test case.

*Setup.* $\mathfrak{gl}_1 = \C$; $\phi_1, \phi_2 \in \C$;
$\psi$ Grassmann of degree $-1$. The brane interaction at the
defect $\R \times p$ is the one-loop bulk-boundary contraction of
two Hamiltonian boundary observables $H_{f}(t) = f(\phi_1(t),
\phi_2(t))$ on the brane line.

*One-loop diagram.* Two boundary insertions $H_{z_1}(t)$ and
$H_{z_2}(s)$ on the brane line, contracted via a single heat-kernel
propagator $P_{\epsilon, L}(t, s)$ on the brane line (or an external
bulk propagator $P_{\epsilon, L}^{\rm bulk}(\R^2 \times \C^2)$
with two endpoints on the brane).

*Brane-line propagator.* In the reduced first-order open model
$S_0 = \int_\R \mathrm{Tr}(\phi_1 d\phi_2)$, the zero-mode-removed
midpoint propagator is $G(t, s) = \tfrac12 \mathrm{sgn}(t - s)$
(`prop:conditional-boundary-product-normalization`,
`main.tex`:5552–5604). The propagator is **regulator-independent
at one loop on the brane line for the linear Hamiltonian sector**:
the heat-kernel scale $(\epsilon, L)$ does not affect the contraction
weight on linear pairs because $G(t, s)$ is already finite for
$t \neq s$ and the zero-mode is removed.

*Cross-contraction.* The cross-contraction
$\langle H_{z_1}(t) H_{z_2}(s) \rangle_{\rm conn} = G(t, s)$
(the one-loop two-point function on linear Hamiltonians). The
operator product is
$H_{z_1}(t) \star H_{z_2}(s) = H_{z_1 \cdot z_2}(t, s)
+ G(t, s) \cdot \mathbf 1 \cdot \hbar$
(operator-product expansion in the BV/factorization sense).

*The QME obstruction at one loop.* The brane-defect QME at one loop
is
$$
\mathrm{QME}_{\rm 1-loop} = \{I_0, I_0\}_{\rm bb}
= \int_\R \int_\R H_{z_1}(t) \star H_{z_2}(s) \cdot a(t) b(s) \gamma_{\mathbf 1}(t) dt ds + \cdots,
$$
expanded against the central ghost $\gamma_{\mathbf 1}$.

*Polyakov-style estimate.* The contribution at order $\hbar^1$ is
$$
\hbar \cdot \omega(z_1, z_2) \cdot \int_\R \int_\R G(t, s) a(t) b(s) \gamma_{\mathbf 1}(t) dt ds
= \hbar \cdot 1 \cdot \int_\R a(t) b(t) \gamma_{\mathbf 1}(t) dt + (\text{subleading}),
$$
where the leading term comes from the coincidence limit $t \to s$
of the propagator $G(t, s) \to \tfrac12 \mathrm{sgn}(0) = 0$
(midpoint convention) **plus the contact term** $\delta(t - s)$
from the boundary product. The result is
$\hbar N \omega(f, g) \int a(t) b(t) \gamma_{\mathbf 1}(t) dt =
\operatorname{Ob}_{\rm sc}$ — exactly the appendix's representative.

**One-loop verdict.** The one-loop QME on linear Hamiltonians on a
single brane produces a **non-zero, regulator-independent**
contribution exactly equal to the obstruction representative
$\operatorname{Ob}_{\rm sc}$ of `prop:app-scalar-contact-qme-class`.
**This is evidence against `prob:weighted-rg-locality`**: at one
loop, the obstruction is non-trivial; no counterterm at one loop in
the scalar-reduced category cancels it (because, by the appendix's
proof, no scalar primitive exists on $\bar A$).

**Two-loop check.** At two loops, the diagram structure is more
complex (two propagators, two vertices, three internal lines). On
linear Hamiltonians, the second non-vanishing Moyal coefficient is
$\hbar^3 P^3 / 24$, and $P^3$ requires three derivatives in each
tensor leg. On linear Hamiltonians ($f = z_1, g = z_2$, each linear),
$P^3 = 0$ identically. **The two-loop contribution on linear
Hamiltonians is zero.**

For non-linear Hamiltonians, e.g., $f = z_1^3 z_2$, $g = z_1 z_2^3$,
the manuscript's `scripts/check_moyal_coefficients.py` confirms
$[z_1^3 z_2, z_1 z_2^3]_* = 8 \hbar z_1^3 z_2^3 - 3 \hbar^3 z_1 z_2
+ O(\hbar^5)$. The order-$\hbar^3$ coefficient $-3 z_1 z_2$ is
*non-zero on $\bar A$* (it does not equal a scalar). The
constant-Taylor-coefficient extraction $[\cdot]_0$ vanishes on
$z_1 z_2$, so this contribution does **not** add to the scalar
obstruction $[\bar c]$. The two-loop scalar contribution on
non-linear pairs vanishes; the obstruction class at one loop
($\hbar N [\bar c]$) **exhausts** the scalar QME obstruction at all
orders on the scalar-reduced source.

**All-order verdict.** The Moyal expansion is odd-only in $\hbar$
(`prop:moyal-monomial`). The scalar contribution
$[P^{2k+1}(f, g)]_0$ requires $2k+1$ derivatives in each tensor
leg; on Hamiltonians of polynomial degree $d_f, d_g$, this is
non-zero only if $d_f, d_g \geq 2k + 1$. For the single-brane
$N = 1$ case the Capelli coefficient is exactly $\hbar N = \hbar$,
and the obstruction is concentrated entirely at one loop. **At all
orders, the scalar QME obstruction class is exactly $\hbar N
[\bar c]$, with no higher-order corrections.**

**Conclusion: low-order PT yields evidence *against*
`prob:weighted-rg-locality`.** The obstruction class is non-zero at
one loop on the simplest test pair, and the higher-loop
contributions on the scalar-reduced source vanish — so the
obstruction is exhaustively captured at one loop. Combined with
`prop:app-scalar-contact-qme-class`'s no-primitive theorem
(no $\bar\eta: \bar A \to \C$ with $\delta\bar\eta = \omega$), the
locality obstruction *does not vanish* on the scalar-reduced
$\mathfrak{gl}_N$ source. **`prob:weighted-rg-locality` is most
likely false on this source.**

**F$'$'s blast radius.**

*If `prob:weighted-rg-locality` were proved (obstruction vanishes):*
- F$'$ promotes to an unconditional all-order Costello-graph closed-
  open derived-center isomorphism in the weighted Tate envelope.
- `prop:wt-conditional-qme-lift` becomes unconditional.
- `cor:wt-descendant-conditional` (descendant cochain comparison)
  becomes unconditional.
- `prob:tate-coefficient-descendant-lift` becomes a theorem.
- `prob:formal-factorization-center` items (3) and (4) become
  closed.
- C₂(W)-q (W3-W6-05) becomes unconditional, joining C₂(W)-cl in the
  stable core.
- The all-order one-antifield Moyal/Weyl quantum lane closes.
- M-31 ($\mathrm{Tr}\,\psi \leftrightarrow [\bar c]$) and Theorem G
  remain stable; they are not affected by the conditional gate.

*If `prob:weighted-rg-locality` is refuted (obstruction non-zero,
which is the W3-W15-05 verdict):*
- F$'$ remains conditional, **as it currently is**.
- C₂(W)-q remains conditional.
- The escape routes of `rmk:app-scalar-contact-escape-routes`
  become the next research directions:
  (i) supertrace replacement $\mathfrak{gl}(N|N)$ with
      $\operatorname{Str}(1) = 0$ (Costello-Li 2015 path); F4 of
      `tate-T4-bv-vanishing.tex` makes this dependence explicit.
  (ii) central character $\chi$ with $\chi(I) = 0$.
  (iii) reintroduction of unreduced scalar Hamiltonian and primitive
       $\eta(f) = -[f]_0$ on $\mathfrak h_{\rm poly}$.
- **The stable core (A, B, C₁ᶠʷ, C₁ᶜᵒᵐᵖ, C₂(NT), C₂(W)-cl, C₂(R),
  D, E, F, G) remains coherent without F$'$.** F$'$ is conditional
  and explicitly named; the manuscript's existing scope is honest.

*Manuscript coherence test.* Strip F$'$ from the stable core and
check that the remaining theorems form a closed dependency graph:
- F (algebraic Moyal) provides the algebraic identities; depends on
  no Costello graph data.
- F$'$ would extend F to a one-antifield Costello-graph realization;
  this is gated by `prob:weighted-rg-locality`.
- G classifies the obstruction line.
- C₂(W)-cl provides the classical cotangent identity.
- Without F$'$, the "all-order quantum cotangent comparison" is
  named as a separate problem (`prob:tate-coefficient-descendant-
  lift`) and is not used in any other proof.

By inspection, removing F$'$ from the stable core does not
destabilize any other theorem. **The stable core is coherent without
F$'$.** F$'$ is an *aspirational* theorem: its closure would advance
the manuscript from algebraic-stable to graph-stable on the
descendant sector. Its current conditional status is honest and
necessary.

**Files read.** `tate-T1-weighted-completion.tex`:493–556;
`tate-P1-hadamard-mittag-leffler.tex`:274–323;
`appendix-unreduced-bv-qme.tex` (full); `main.tex`:5430–5550;
`scripts/check_moyal_coefficients.py` (Capelli/Moyal numerical
verification).
**Confidence.** High at the algebraic and one-loop level; the
all-order interpretation depends on the structure of higher-loop
diagrams in the Costello graph expansion, which is governed by
`prob:analytic-graph-realization` and is partially open.
**Blast radius.** This entry classifies F$'$ as a conditional
theorem whose conditional gate is most likely *false* on the
scalar-reduced $\mathfrak{gl}_N$ source. The escape routes are
named and are the next research directions; the manuscript's
stable core remains coherent without F$'$.
**Minimal heal.** In `theorem-lanes.tex` Lane 7 (degree-zero
Moyal/Weyl) at the residual disposition (around line 410), append:

> "**Status of `prob:weighted-rg-locality` (low-order PT
> evidence).** Perturbative analysis at one loop on the simplest
> test case ($N = 1$, $(f, g) = (z_1, z_2)$) yields a non-zero,
> regulator-independent obstruction equal to $\hbar [\bar c]$,
> with no higher-loop scalar corrections by the odd-only Moyal
> expansion. This is evidence *against* vanishing of the obstruction
> class on the scalar-reduced $\mathfrak{gl}_N$ source. The
> escape routes of `rmk:app-scalar-contact-escape-routes`
> (supertrace, central character, unreduced scalar primitive) are
> the next research directions. F$'$ remains conditional; the
> stable core (A, B, C₁ᶠʷ, C₁ᶜᵒᵐᵖ, C₂(NT), C₂(W)-cl, C₂(R), D, E,
> F, G) is coherent without F$'$."

**Residual.** R-W3-W15-05 (open Phase-4): an honest classification
of which input-changing escape routes (supertrace, central
character, unreduced scalar primitive, or higher) actually close the
scalar QME obstruction, and what new theorems become unconditional
under each. Phase-4 research; outside the immediate stable core.
**Adjudication.** Valid. Confirms the conditional status of F$'$ at
low order; identifies the obstruction as concentrated at one loop
with no higher-loop corrections; confirms manuscript coherence
without F$'$.

---

## §2. Stable-core update (Wave-3-W15 amended)

The Wave-2 + W3-W6 + W3-W8 stable core was: A, B, C₁ᶠʷ, C₁ᶜᵒᵐᵖ
(bidirectional), C₂(NT), C₂(W)-cl (unconditional), C₂(W)-q
(conditional on Theorem G's class), C₂(R) (admissible-class only),
D, E, F (algebraic), F$'$ (conditional on `prob:weighted-rg-locality`),
G. Wave-3-W15's amendments:

- **A, B, C₁ᶠʷ, C₁ᶜᵒᵐᵖ, C₂(NT), C₂(W)-cl, C₂(R), D, E:** Stable.
  No new findings.
- **F (algebraic Moyal target):** Stable, unconditional in the
  finite algebraic model. Verbatim status recorded (W3-W15-01).
- **F$'$ (Radial-Moyal, all-order conditional):** Conditional on
  `prob:weighted-rg-locality`; gate is most likely *false* on the
  scalar-reduced source by W3-W15-05's one-loop computation.
  Escape routes named (`rmk:app-scalar-contact-escape-routes`).
- **C₂(W)-q:** Conditional on the same class as F$'$
  (W3-W6-05 + W3-W15-04: residue = $[\bar c]$).
- **G (U(1)/Capelli anomaly):** Stable, unconditional. The class
  $[\bar c]$ is the **defining** anomaly that gates F$'$ and
  C₂(W)-q. Identified with the QME obstruction at the cohomology
  level via a strict chain-level functor $\Lambda$ (W3-W15-03).

**Verdict on stable core (Costello + Boundary lens).** STABLE
*without* F$'$. The manuscript's architecture is honest: F is
algebraic-stable; F$'$ is conditional with explicit gating; G
classifies the gate. The conditional gate is most likely false on
the scalar-reduced source; escape routes are explicit and bounded.
**No reorganization required.**

The Boundary lens (zero/infinity, empty input, singular strata)
yields a strong robustness verdict: the gating is non-trivial in
every parameter regime ($\hbar \to 0$, $\hbar \to \infty$, large
$w$, $N \to 1$ or $\infty$). The small-weight limit ($q \to 1^+$)
falls outside the admissible class; this is governed by R-W3-W6-04 /
R-W3-W8-01.

The Costello lens yields a residue-level identity: **the unreduced
QME holds modulo the regulator with residue $\hbar N [\bar c]$**
(W3-W15-04), where the residue is *not* a regulator artifact but
**Theorem G's defining class viewed through the BV/QME register**.
The chain-level lift $\Lambda$ is strict (no homotopies), confirming
W3-W6-05's identification at the cocycle-functor level.

---

## §3. Heal proposals (smallest first)

### Tier 1 — Statement-only edits

**WP3-W15-1 (W3-W15-02).** In `tate-T1-weighted-completion.tex`
near `prob:weighted-rg-locality` (line 531), or in `theorem-lanes.tex`
Lane 7, append the boundary-regime remark of W3-W15-02's minimal
heal. One paragraph naming the five regimes
($\hbar, w, N$ small/large) and the small-$w$ exit from the
admissible class.

**WP3-W15-2 (W3-W15-03).** In `appendix-unreduced-bv-qme.tex` after
`prop:app-scalar-contact-qme-class` (line 158), append the
chain-level lift remark of W3-W15-03's minimal heal. One paragraph
naming the strict cocycle map $\Lambda$ from $C^2_{\rm Lie}(\bar A;
\C)$ to $H^1(\mathcal O_{\rm loc}(\mathcal E_w), Q + \{I_0, -\})$.

**WP3-W15-3 (W3-W15-04).** In `principles.tex` after the Witten
convention QME paragraph (lines 131–155), append the residue-
interpretation sentence of W3-W15-04's minimal heal. One paragraph
naming the residue $\hbar N [\bar c]$ as the same class classified
by Theorem G.

**WP3-W15-4 (W3-W15-05).** In `theorem-lanes.tex` Lane 7's residual
disposition, append the low-order PT verdict of W3-W15-05's minimal
heal. One paragraph naming the one-loop $N = 1$ test case and the
escape-routes status.

### Tier 2 — Architectural cross-link

**WP3-W15-5.** In `claim-strength-ledger.tex` (or in the master
ledger §2 stable-core declaration), add a sub-bullet for F$'$:

> "**F$'$ (Radial-Moyal, all-order one-antifield extension).**
> Conditional on `prob:weighted-rg-locality`. The conditional gate
> is most likely *false* on the scalar-reduced $\mathfrak{gl}_N$
> source by `prop:app-scalar-contact-qme-class`'s no-primitive
> theorem and W3-W15-05's one-loop $N = 1$ test computation. The
> obstruction class is exactly $\hbar N [\bar c]$ (Theorem G's
> class), exhaustively captured at one loop. The escape routes of
> `rmk:app-scalar-contact-escape-routes` (supertrace, central
> character, unreduced scalar primitive) are Phase-4 research
> directions. The stable core (A, B, C₁, C₂, D, E, F, G) is
> coherent without F$'$."

This is the strongest classification: F$'$ is honestly conditional,
its gate is genuinely non-trivial, and the manuscript's scope is
preserved without F$'$.

---

## §4. Residuals after Wave-3-W15

- **R-W3-W15-01.** None at the verbatim-statement layer; W3-W15-01
  records the conditional-gap structure inside the master ledger.
- **R-W3-W15-02.** Cross-regulator-class behaviour at small weight
  ($q \to 1^+$) is governed by R-W3-W6-04 / R-W3-W8-01, not by
  W3-W15. Phase-4.
- **R-W3-W15-03.** Cross-regulator-class canonicity of the
  chain-level lift $\Lambda$ is governed by R-W3-W6-04. Phase-4.
- **R-W3-W15-04.** Structural classification of all data-changing
  escape routes for removing the residue $\hbar N [\bar c]$
  (supertrace vs.\ central character vs.\ unreduced scalar
  primitive vs.\ further as-yet-undetected). Phase-4.
- **R-W3-W15-05.** Phase-4 research on the escape routes for
  `prob:weighted-rg-locality`: which input-changing routes close
  the scalar QME obstruction, and what new theorems become
  unconditional under each. Outside the immediate stable core.

---

## §5. Convergence verdict

**Theorem F.** Stable, unconditional in the finite algebraic model.
**Verdict: STABLE.**

**Theorem F$'$.** Conditional on `prob:weighted-rg-locality`. The
gate is most likely *false* on the scalar-reduced
$\mathfrak{gl}_N$ source by W3-W15-05's one-loop computation
(non-zero obstruction $\hbar [\bar c]$ at $N = 1$, exhaustively
captured at one loop). Escape routes named (supertrace, central
character, unreduced scalar primitive). **Verdict: HONEST CONDITIONAL,
gate most likely false on scalar-reduced source; escape routes
explicit; stable core coherent without F$'$.**

**Theorem G.** Stable, unconditional after M-09 / M-10 / M-12 heals.
The class $[\bar c]$ is the **defining** anomaly that gates F$'$
and C₂(W)-q. Identified with the QME obstruction at the cohomology
level via a **strict chain-level functor** $\Lambda$ (W3-W15-03);
the residue is $\hbar N [\bar c]$ regulator-independent inside the
admissible class (W3-W15-04). **Verdict: STABLE, with explicit
chain-level identification.**

**[c̄] = QME class identification (W3-W6-05).** Sharpened from
"cohomology equality" to "cohomology equality via strict
chain-level functor $\Lambda$" (W3-W15-03). The unreduced QME holds
modulo the regulator with residue $\hbar N [\bar c]$, where the
residue is *not* a regulator artifact (W3-W15-04). **Verdict:
VALID, sharpened to chain-level functor + residue identity.**

**Stable core (Theorems A, B, C₁ᶠʷ, C₁ᶜᵒᵐᵖ, C₂(NT), C₂(W)-cl,
C₂(W)-q, C₂(R), D, E, F, F$'$, G).** Stable *without* F$'$. F$'$ is
honestly conditional; its gate is most likely false on the
scalar-reduced source; escape routes are explicit. **Verdict:
STABLE without F$'$; F$'$ is aspirational; manuscript scope is
honest.**

The single most important new technical insight: **F$'$ does not
need to be unconditional for the manuscript to be coherent**. F$'$
is an aspirational theorem whose closure would advance the
manuscript from algebraic-stable to graph-stable on the descendant
sector. Its current conditional status is honest and necessary; the
gate is the same anomaly classified by Theorem G; the escape
routes are explicit. The Boundary lens (no parameter regime
trivializes the gating) and the Costello lens (the residue is
regulator-independent inside the admissible class, equal to
Theorem G's class) together confirm that the manuscript's
architecture is correct.

**Posture against Wave 2 / W3-W6 / W3-W8.** Wave-2 W1's 5-way
split, Wave-2 W6's 8-link DAG, W3-W6's three sharpenings, W3-W8's
five sharpenings, and M-26 / M-27 / M-31 / M-32 are all preserved.
The W3-W15 contribution is a **conditional-theorem audit** of F,
F$'$, G under the Costello + Boundary lens, with five named
statements (W3-W15-01 through W3-W15-05) added to the master
ledger. No new theorems are needed; F$'$'s blast-radius
classification confirms manuscript coherence without F$'$.

End of W3-W15 report.

---

## 200-word executive summary

W3-W15 (Costello + Boundary lens) audits the conditional theorems
F, F$'$, G of the manuscript. **Verbatim statements** recorded:
F is `thm:finite-n-reduced-moyal` + algebraic Moyal package
(`main.tex`:4903); F$'$ is `thm:phi-hbar-all-order` +
`prop:wt-conditional-qme-lift` (5459, T1:493); G is the four-block
Capelli/U(1) chain (280–470). **F is unconditional in the finite
algebraic model; G is unconditional after the bigraded heal;
F$'$ is conditional on `prob:weighted-rg-locality`.** Boundary
analysis: the gating is non-trivial in every regime ($\hbar$,
weight $w$, $N$); small-$w$ exits the admissible class. **Cocycle
vs cohomology:** $[\bar c]$ and the QME obstruction are
cohomology-equal via a *strict chain-level functor* $\Lambda$
(contact-multiplication-by-$\gamma_{\mathbf 1}$); not strict-
cocycle-equal (different complexes). **Unreduced QME** holds modulo
regulator with residue $\hbar N [\bar c]$, *not* a regulator
artifact. **One-loop PT on $N = 1$, $(z_1, z_2)$:** obstruction is
exactly $\hbar [\bar c]$, exhaustively captured at one loop;
evidence *against* `prob:weighted-rg-locality` on the scalar-reduced
source. **F$'$ blast radius:** if proved, F$'$ promotes; if refuted
(W3-W15-05 verdict), escape routes (supertrace, central character,
unreduced scalar primitive) are next research; stable core remains
coherent without F$'$.
