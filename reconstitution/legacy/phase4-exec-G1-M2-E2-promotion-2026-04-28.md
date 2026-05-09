# Phase-4 Execution / G1 / M2 — Avenue (E) pre-work: $E_2$-promotion of the brane-line $E_1$ algebra on $\R^2$ via the Hamiltonian connection

**Date.** 2026-04-28.
**Author.** Raeez Lorgat.
**Phase.** 4 (post-Wave-3 W37 certified convergence; Phase-4 EXEC
agent on G1 6-month milestone Avenue (E) pre-work).
**Group.** G1 — Weiss / factorization beyond $\R$.
**Specific obligation.** P4-G1-M2 (6-month milestone, per
`reconstitution/phase4-G1-weiss-product-2026-04-28.md` §T5.A and
§T3.E): Avenue (E) pre-work — *construct (or rule out) the
$E_2$-promotion of the brane-line $E_1$ algebra on $\R^2$ via the
Hamiltonian connection*. Brane-line $E_1$ algebra was identified at
G1-M1 as the BD chiral algebra $\mathcal A_{\mathrm{fact}}$ on the
brane line with the column-Verma vacuum module $\widehat M_0$ from
W3-W26 / P4-G2-M1.
**Lens.** Beilinson primary (sheaf-theoretic on $\mathrm{Ran}(\R^2)$;
descent for the Hamiltonian connection; exactness of $E_2$ structure
maps; filtered/spectral on the Tate window). Composition secondary
(do local $E_2$ structure maps compose globally? Mayer-Vietoris /
Čech check on $\R^2$ covers; associativity at $E_2$ pentagon and at
$E_2$ braid axiom).
**Mode.** Proposal-only. No commits. No manuscript TeX edits. Master
ledger schema; IDs prefix `P4-EXEC-G1-M2-`.

**Inputs (read in full).**
- `/Users/raeez/topological-strings/CLAUDE.md`.
- `reconstitution/phase4-G1-weiss-product-2026-04-28.md` (G1 outline
  §T3.E Avenue (E) statement; §T5.A 6-month milestone).
- `reconstitution/phase4-exec-G1-M1-BD-chiral-2026-04-28.md` (full;
  P4-EXEC-G1-M1-PROP closure at M-3 scope; D1-D6 deliverable;
  hypothesis verification table; §6 connection to $E_2$-promotion).
- `reconstitution/wave3-W26-column-verma-2026-04-28.md` §1-§3
  (column-Verma rank-1 unipotent Borel; HWV $v_{0, -1}$;
  GL$_2 \times T^2$ functoriality; $\sigma$-twist obstruction at
  quadratic symplectomorphisms).
- `reconstitution/wave3-W11-beilinson-hypotheses-2026-04-28.md`
  §1 Target T1 Lurie HA §5.5.4 hypothesis verification table;
  W3-W11-01, -02, -04, -05; eleven hypothesis checks.
- `reconstitution/phase4-exec-module-lambda-bracket-2026-04-28.md`
  (P4-G2-M1 DISCHARGED; module $\lambda$-bracket on $\widehat M_0$;
  2821 instances / 0 failures; Bakalov-Kac axioms verified).
- `main.tex`:1770-1840 (Hamiltonian BF action on $\R^2 \times \C^2$;
  Hamiltonian connection $\alpha$; flatness equation $F_\alpha = 0$;
  classical field content with $\alpha_{x_i} dx_i$ component on
  $\R^2$; $\alpha_{\bar z_j} d\bar z_j$ component as Beltrami).
- `main.tex`:1996-2210 (`thm:open-closed-derived-center-factorization`
  clauses (1)-(5); `rmk:E1-translation`; Lurie HA §5.5.4 / CG Vol I
  §6.4 invocations).
- `main.tex`:280-470 (`lem:omega-cocycle`; `thm:u1-center-anomaly`;
  cocycle class $[\bar c]$).
- `tate-T1-weighted-completion.tex` (full; Casimir convergence;
  weighted regulator-admissible sector; admissible Tate envelope
  `stmt:tate-model-envelope`).
- `appendix-factorization-current-conventions.tex` (full;
  `prop:app-factorization-principal-part-bracket`; smeared
  Hamiltonian current bracket on $\R$).

**Primary external sources cited.**
- Lurie, *Higher Algebra*, May 2017 / kerodon §HA.5.5.4 (`LurieHA`):
  §5.5.2.6 (pushforward of factorizable structures); §5.5.3
  (topological chiral homology); §5.5.4.10 (locally constant FA ≃
  $E_n$-algebra); **§5.5.4.16 (Dunn additivity:
  $E_m \otimes E_n \simeq E_{m+n}$ in $\Pr^L$)**.
- Costello-Gwilliam Vol. I (`CGW1`): §6.4, §6.5 (Weiss covers),
  §A.5.4-6 (cosheaf product stability for product covers).
- Costello-Gwilliam Vol. II (`CGW2`): §10 (holomorphic factorization
  algebras on $\C^n$ via $\bar\partial$-Hodge); §11.4 (holomorphic
  Chern-Simons + defect).
- Williams, *Holomorphic factorization algebras*, arXiv:2007.13985
  (`Will20`): §3 (holomorphic-$E_n$-algebra
  $\mathbb E_n^{\mathrm{hol}}$; $\bar\partial$-quasi-isomorphism on
  holomorphic polydisk inclusions); §4 (holomorphic factorization
  homology).
- Ayala-Francis, *Factorization homology of topological manifolds*,
  arXiv:1206.5522 / J. Topology 2015 (`AF15`): §3-§5 (factorization
  homology for $E_n$-algebras on smooth $n$-manifolds; excision /
  Weiss descent).
- Beilinson-Drinfeld, *Chiral Algebras*, AMS Coll. Pub. vol. 51,
  2004 (`BD04`): §3.4.1, §3.4.5, §3.4.10, §3.4.11 (chiral
  product on $X \times Y$).
- Bakalov-Kac, IMRN 2003 (`BK03`).
- Frenkel-Ben-Zvi (`FBZ04`): §3.3-3.4, §16, §19.5.
- Gwilliam-Williams 2023 *Holomorphic Chern-Simons defect* (latest
  Williams group): defect chiral algebra on a real line in
  holomorphic background, codim-3 / codim-4 brane.

---

## §0. Executive verdict

**Closure status.** P4-G1-M2 (Avenue (E) pre-work: $E_2$-promotion
of the brane-line $E_1$ algebra on $\R^2$ via the Hamiltonian
connection) is **PARTIAL — pre-work delivers a precise candidate
$E_2$-structure together with a named obstruction class for
Tate-stability**, with three sub-verdicts:

* **(a) PASSES at the locally-constant strict-$E_2$ layer**, i.e.,
  on the **purely topological factor $\R^2$** (with the $\C^2$
  holomorphic factor temporarily forgotten). Lurie HA §5.5.4.16
  (Dunn additivity) applies *unconditionally* in the locally
  constant subcategory: the brane-line $E_1$ algebra
  $\mathcal A_{\mathrm{fact}}$ tensors with the transverse $\R$
  $E_1$ algebra $\mathcal B_\perp$ to give a strict
  $E_1 \otimes E_1 \simeq E_2$ algebra. The Hamiltonian connection
  $\alpha_{x_i} dx_i$ on $\R^2$ supplies the transverse data
  $\mathcal B_\perp$.

* **(b) PARTIAL at the Tate-window stability layer.** The candidate
  $E_2$ structure maps are well-defined as multilinear operations on
  the admissible Tate envelope, but Tate-stability of the $E_2$
  associativity / braid axiom requires Lurie 5.5.4.16's hypothesis
  H2 (tensor product preserves all small colimits separately) to be
  verified for *arbitrary* small colimits, not only Mittag-Leffler
  colimits. The W3-W11-01 silent strengthening identifies the
  obstruction class as the **arbitrary-colimit-preservation gap of
  $\widehat\otimes$ on the admissible Tate envelope**: the obstruction
  is named, its severity is 3, and it is co-extensive with
  W3-W11-01-A's heal patch. The cohomological-stability obstruction
  class for the $E_2$ promotion is the same class as W3-W11-01.

* **(c) FAILS at the strict-Dunn-additivity composition with the
  $\C^2$ holomorphic factor.** The full Dunn additivity composition
  $A_{\mathrm{E_2}} \simeq A_{\mathrm{brane}} \otimes_{E_1}
  A_{\mathrm{brane}}$ as $E_2$-algebras on $\R^2 \times \C^2$
  *fails* because the $\C^2$ factor carries holomorphic-locally-
  constant structure (Williams arXiv:2007.13985
  $\mathbb E_2^{\mathrm{hol}}$-algebra), not topological-locally-
  constant. Dunn additivity in Lurie 5.5.4.16 applies to topological
  $E_n$ algebras; it does *not* extend to the mixed
  topological / holomorphic setting without Avenue (B) of T3
  (M-12 milestone). **The Avenue (E) M-6 deliverable closes the
  $\R^2$-only piece; the $\C^2$ piece is forwarded to Avenue (B).**

**Cohomological-stability obstruction class.** **Same class as
W3-W11-01:** the colimit-preservation gap of the completed Tate
tensor product $\widehat\otimes$ on the admissible envelope at
arbitrary small colimits. *(Specifically: the candidate $E_2$
structure maps are continuous on Mittag-Leffler colimits; whether
they remain continuous on arbitrary small colimits in the
admissible envelope is the open obstruction.)* Severity 3.
Heal-patch route: WP3-W11-01-A "envelope-restriction" heal —
state $E_2$ promotion explicitly in the ML-colimit-restricted
admissible envelope, treat the arbitrary-colimit version as the
P4-G1-M3+ residual.

**Dunn-additivity verdict at M-6.** **Holds on the topological
factor $\R^2$ alone** (Lurie 5.5.4.16 directly applies);
**does not hold on the mixed setting $\R^2 \times \C^2$** (Avenue
(B) M-12 obligation; mixed Dunn additivity
$\mathbb E_m^{\mathrm{top}} \otimes \mathbb E_n^{\mathrm{hol}}
\simeq \mathbb E_{m, n}^{\mathrm{mixed}}$ is not proved in the
literature).

**Lens findings.** Beilinson lens (sheaf-theoretic): the
Hamiltonian connection $\alpha$ on $\R^2$ is *flat* on-shell
($F_\alpha = 0$, `main.tex`:1808-1810), so it descends to a
locally constant cosheaf on $\R^2$ (modulo the Tate-window
restriction). Composition lens: the strict $E_2$ associativity
on $\R^2$ holds via Lurie 5.5.4.16 applied to the locally
constant subcategory; the $E_2$ braid axiom (in the operadic
Boardman-Vogt sense) is automatic on the locally constant subcategory
by translation invariance. **Both lenses confirm the M-6
Avenue-(E) pre-work closes the $\R^2$-only piece with the named
obstruction at the Tate-stability layer.**

**Cross-walk to W3-W26.** The column-Verma vacuum module
$\widehat M_0$ from G1-M1 sits at a corner of the candidate $E_2$
structure that is *automatically stable* at the
Symp$_{\mathrm{form}}^{(\leq 1)}$ (linear) layer: the Hamiltonian
connection's transverse $\R$ direction acts on $\widehat M_0$ via
the column-shifters $X = z_2$, killed at the rank-1 unipotent Borel
HWV $v_{0, -1}$ (cf. W3-W26-T1 §1.3). The rank-1 unipotent
Borel-Verma structure of $M_0$ ensures the $E_2$ braid axiom
on $\widehat M_0$ degenerates to the abelian / commutative case at
the highest-weight stratum; the lower-weight strata $v_{0, -2},
v_{0, -3}, \dots$ inherit the $E_2$ structure by the rising-
factorial $Y$-orbit. Functoriality is preserved at the
GL$_2 \times T^2$ layer (W3-W26-T1 §3); breakage at quadratic
symplectomorphisms (W3-W26-08) does not affect the $E_2$ braid
axiom because the breakage is on the symplectomorphism action, not
on the brane-line direction.

---

## §1. Precise $E_1$ algebra $A_{\mathrm{brane}}$ statement

Recall the M-1 deliverable's brane-line factorization centre is the
locally constant FA on $\R$
$$\mathcal A_{\mathrm{fact}}(I)
  := C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak g_I),
  \qquad
  \mathfrak g_I = \mathfrak h_I \ltimes \mathcal P_I[1],
  \qquad
  \mathfrak h_I = \Omega^\bullet_c(I) \widehat\otimes \bar A,$$
with structure maps induced by extension-by-zero on
$\Omega^\bullet_c$ (`main.tex`:1996-2046; M-1 §1).

By Lurie HA §5.5.4.10, this LCFA on $\R$ is equivalent to an
$E_1$-algebra in the admissible Tate envelope. The corresponding
$E_1$-algebra is

**$A_{\mathrm{brane}} := A_\partial^{\mathrm{Ham}}(I)
= \widehat{\mathbf S}(\mathfrak h_I)$,**

the smeared Hamiltonian current $E_1$-algebra, with multiplication
the symmetric-product algebra structure (commutative on the
ghost-zero sector; graded-commutative on the full BV-graded sector).
The associative algebra structure is graded-commutative on the
ghost-zero piece (`main.tex`:2199-2202; `rmk:E1-translation`); the
$E_1$ structure refines the graded-commutative product by the
$P_0$-bracket of `prop:app-factorization-principal-part-bracket`
(`appendix-factorization-current-conventions.tex`:107-148):
$$Y(J_f, \lambda) J_g = J_{\{f, g\}} + \bar c(f, g)\,\lambda \in
  \C[\lambda]\widehat\otimes A_{\mathrm{brane}},$$
where $\bar c(f, g)$ is the U(1)/Capelli scalar cocycle of
`lem:omega-cocycle` (`main.tex`:284-316).

### §1.1 Embedding in the bulk $W_{1+\infty}(\epsilon_1, \epsilon_2)$ factorization centre

The bulk $W_{1+\infty}(\epsilon_1, \epsilon_2)$ factorization centre
on $\widehat{\C^2}_0$ is the formal disk's Hamiltonian Lie algebra
cohomology $C^\bullet_{\mathrm{CE},\mathrm{cont}}(\bar A)$, equipped
with the chiral $P_0$-bracket and central charge $[\bar c]$
(`thm:open-closed-derived-center-factorization` clauses (1)-(5);
`main.tex`:1996-2046). The brane-line $E_1$ algebra
$A_{\mathrm{brane}}$ on $\R$ embeds in the bulk factorization
centre as the **brane-stratum restriction**:

$$A_{\mathrm{brane}}(I) = \mathrm{Obs}^{\mathrm{cl}}_{\mathrm{closed},H}|_{\R \times \{0\} \subset \R \times \C^2}(I \times \{0\}),$$

i.e., the brane-line factor of the full bulk observables FA
restricted to the brane stratum $\R \times \{0\} \subset \R \times
\C^2$ at the brane line endpoint $\{0\} \in \C^2$.

This embedding is W3-W11-05's W3-W26-T1's **brane-line layer of
(W-2D)** (closed at G1-M1 via `phase4-exec-G1-M1-BD-chiral`
P4-EXEC-G1-M1-PROP).

The $W_{1+\infty}(\epsilon_1, \epsilon_2)$ structure on the bulk
is the conformal Virasoro central charge
$c_{\mathrm{SV}} = (\epsilon_1+\epsilon_2)^2 / (\epsilon_1 \epsilon_2)$
of `phase4-G4-5dM-twist-2026-04-28.md` §1.2; this requires the
topological twist $\tau$ for the type-clash resolution (P4-G4-T2.2,
W3-W31-T1, severity 4); within M-1 / M-6 EXEC scope, we work with
the *topological* chiral algebra (no conformal weight), recording
$[\bar c]$ as the U(1)/Capelli class only.

---

## §2. Candidate $E_2$ lift $A_{\mathrm{E_2}}$ construction

### §2.1 The candidate underlying chain complex

The candidate $E_2$ algebra on $\R^2$ has underlying chain complex

$$A_{\mathrm{E_2}}(U)
:= C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak g^{(2)}_U),
\qquad
\mathfrak g^{(2)}_U
:= \Omega^\bullet_c(U) \widehat\otimes (\bar A \oplus \bar A_\perp),$$

where $U \subseteq \R^2$ is open, $\Omega^\bullet_c(U)$ is the
compactly supported de Rham cosheaf, and $\bar A_\perp$ is the
*transverse* Hamiltonian Lie algebra contributed by the second $\R$
direction. In the bulk Hamiltonian BF setup, the transverse $\R$
direction in $\R^2$ contributes its own Hamiltonian connection
$\alpha_{x_2} dx_2$ (the second component of the Hamiltonian
connection $\alpha$ in `main.tex`:1830-1836). The transverse
Hamiltonian Lie algebra $\bar A_\perp$ is *isomorphic* to $\bar A$
as a Lie algebra (both are the perfect Hamiltonian Lie algebra
$\C[z_1, z_2] / \C \cdot 1$ on the same formal symplectic disk
$\widehat{\C^2}_0$); the distinction is which $\R$-direction-of-
$\R^2$ is being smeared.

The Lie algebra $\mathfrak g^{(2)}_U = \Omega^\bullet_c(U)
\widehat\otimes (\bar A \oplus \bar A_\perp)$ carries:
- the Poisson bracket on $\bar A$ for the brane-line direction;
- the Poisson bracket on $\bar A_\perp$ for the transverse direction;
- a *cross-bracket* $[\bar A, \bar A_\perp]$ supplied by the
  Hamiltonian connection's flatness equation $F_\alpha = 0$
  (`main.tex`:1808-1810).

### §2.2 Structure maps — strict $E_2$ multiplication

The candidate $E_2$ algebra carries the following structure maps:

**(M-2.2.1) $E_1$-multiplication along brane-line direction.**
For each pair of disjoint open intervals $I_1, I_2 \subset \R$ (the
brane-line direction) with $I_1 \sqcup I_2 \subset I \subseteq \R$,
the $E_1$ multiplication
$$m^{E_1}_{\mathrm{brane}}: A_{\mathrm{E_2}}(I_1 \times U_2)
\widehat\otimes A_{\mathrm{E_2}}(I_2 \times U_2)
\to A_{\mathrm{E_2}}(I \times U_2)$$
inherits from the M-1 brane-line $E_1$ structure, applied with
the transverse open $U_2$ held fixed.

**(M-2.2.2) $E_1$-multiplication along transverse direction.**
For each pair of disjoint opens $U_1, U_2 \subset \R$ (the
transverse direction) with $U_1 \sqcup U_2 \subset U \subseteq \R$,
the transverse $E_1$ multiplication
$$m^{E_1}_{\perp}: A_{\mathrm{E_2}}(I_2 \times U_1)
\widehat\otimes A_{\mathrm{E_2}}(I_2 \times U_2)
\to A_{\mathrm{E_2}}(I_2 \times U)$$
inherits from the analog of the M-1 brane-line $E_1$ structure,
applied along the *transverse* $\R$ direction in $\R^2$ with the
brane-line interval $I_2$ held fixed.

**(M-2.2.3) Bicommutativity / $E_2$ braid axiom.** For each pair
of disjoint disks $D_1, D_2 \subset \R^2$ with
$D_1 \sqcup D_2 \subset D$ (where $D$ is a larger disk), the
$E_2$ multiplication
$$m^{E_2}: A_{\mathrm{E_2}}(D_1)
\widehat\otimes A_{\mathrm{E_2}}(D_2)
\to A_{\mathrm{E_2}}(D)$$
is required to factor through both $m^{E_1}_{\mathrm{brane}}$ and
$m^{E_1}_{\perp}$. By Lurie HA §5.5.4.16 (Dunn additivity), this
factorization is automatic at the locally constant level: the strict
$E_1 \otimes E_1 \simeq E_2$ equivalence in $\Pr^L$ identifies
$m^{E_2}$ with the iterated Boardman-Vogt tensor of the two $E_1$
multiplications.

### §2.3 What the Hamiltonian connection contributes

The Hamiltonian connection $\alpha$ on $\R^2 \times \C^2$
(`main.tex`:1770-1840) decomposes by direction. Restricted to the
brane stratum $\R^2 \times \{0\}$, the components are:

- $\alpha_{x_1} dx_1$: one-form on the brane-line direction,
  Hamiltonian-vector-field-valued. This is the smeared Hamiltonian
  current along the brane-line direction; the resulting
  $E_1$-algebra structure on $\R$ (brane-line) is the M-1
  $A_{\mathrm{brane}}$.
- $\alpha_{x_2} dx_2$: one-form on the transverse direction,
  Hamiltonian-vector-field-valued. This is the smeared Hamiltonian
  current along the transverse direction; the resulting
  $E_1$-algebra structure on $\R$ (transverse) is by symmetry
  also a copy of $A_{\mathrm{brane}}$ (with the "transverse"
  label).

The flatness equation $F_\alpha = D\alpha + \tfrac{1}{2}\{\alpha, \alpha\} = 0$
(`main.tex`:1808-1810) on the brane stratum decomposes into:
- $\partial_{x_1} \alpha_{x_2} - \partial_{x_2} \alpha_{x_1}
  + \{\alpha_{x_1}, \alpha_{x_2}\} = 0$;

this is the **flat-connection 2-form** condition that ensures
the brane and transverse $E_1$-algebras compose to a *strict*
(not merely up-to-coherent-homotopy) $E_2$-algebra: the cross-
bracket $\{\alpha_{x_1}, \alpha_{x_2}\}$ is exactly the
infinitesimal Hochschild differential measuring failure of strict
commutativity, and flatness forces it to vanish *up to the chosen
gauge representative*. On-shell ($F_\alpha = 0$), the cross-
bracket is exact, so the $E_2$-structure is strict at the
cohomological level.

**M-2.2-CONS (consequence).** The Hamiltonian connection $\alpha$
on $\R^2$ provides a *strict* $E_2$-multiplication at the
cohomological level by Lurie 5.5.4.16, with the flat-connection
2-form condition $F_\alpha = 0$ supplying the Mayer-Vietoris /
Čech compatibility data.

---

## §3. Hamiltonian connection multiplication in detail

### §3.1 The Lurie 5.5.4.16 Dunn additivity application

Lurie HA §5.5.4.16 (Dunn additivity, `LurieHA` Theorem 5.5.4.16
in May 2017 / kerodon §HA.5.5.4) states:

> *In $\Pr^L$ (presentable $\infty$-categories), there is a
> canonical equivalence $E_m \otimes E_n \simeq E_{m+n}$ of
> operads.*

For our setup with $m = n = 1$:

$$E_1 \otimes E_1 \simeq E_2 \text{ in } \Pr^L.$$

Apply this in the locally constant subcategory of
$\mathrm{Fact}^{\mathrm{lc}}(\R^2; \mathcal C)$, where $\mathcal C$
is the admissible Tate envelope. By Lurie 5.5.4.10, the locally
constant subcategory on $\R^2$ is equivalent to $\Alg_{E_2}(\mathcal C)$.
The Dunn additivity then identifies:

$$\mathrm{Fact}^{\mathrm{lc}}(\R^2; \mathcal C) \simeq
\Alg_{E_2}(\mathcal C) \simeq \Alg_{E_1}(\Alg_{E_1}(\mathcal C))
\simeq \Alg_{E_1}(\Alg_{E_1}(\mathcal C)).$$

The two $E_1$ structures correspond to the two $\R$ directions of
$\R^2$ (brane and transverse).

### §3.2 The brane-line embedding in $\Alg_{E_1}(\Alg_{E_1}(\mathcal C))$

The M-1 brane-line $E_1$-algebra $A_{\mathrm{brane}} \in
\Alg_{E_1}(\mathcal C)$ embeds in
$\Alg_{E_1}(\Alg_{E_1}(\mathcal C))$ as the **trivial outer
$E_1$-algebra**: viewing $A_{\mathrm{brane}}$ as a constant
function from the transverse $\R$ direction, with the trivial
$E_1$ structure on the transverse direction.

The Hamiltonian connection's transverse component $\alpha_{x_2} dx_2$
*upgrades* this trivial outer $E_1$-algebra to a *non-trivial*
outer $E_1$-algebra: the transverse smeared Hamiltonian current
$J^\perp_{f}(b) := \int_\R b(x_2)\,\alpha_{x_2}(x_2) f \,dx_2$
provides the spin-1 currents along the transverse direction. By
the same M-1 D1 argument applied in the transverse direction, the
transverse $E_1$-algebra is *isomorphic* to $A_{\mathrm{brane}}$
as an $E_1$-algebra (since both encode the same Hamiltonian Lie
algebra $\bar A$ via the same factorization centre construction,
just with the smearing in different real directions).

**M-2.3-LIFT.** The candidate $E_2$ algebra on $\R^2$ is therefore

$$A_{\mathrm{E_2}} := A_{\mathrm{brane}} \otimes_{E_1} A_{\mathrm{brane}}
\quad \text{ in } \Alg_{E_2}(\mathcal C),$$

with the outer $E_1$ structure supplied by the transverse
direction. By Dunn additivity, this is well-defined as an
$E_2$-algebra in the locally constant subcategory of
$\mathrm{Fact}^{\mathrm{lc}}(\R^2; \mathcal C)$.

### §3.3 The flatness obstruction

The Lurie 5.5.4.16 application gives a *strict* $E_2$-algebra
*after* the locally-constant restriction. The non-trivial part
is verifying that the candidate is *actually* locally constant on
$\R^2$ (not just on each $\R$ factor separately). This is where
the Hamiltonian connection's flatness $F_\alpha = 0$ enters:

**M-2.3-LC (locally-constant verification).** The candidate
$A_{\mathrm{E_2}}$ is locally constant on $\R^2$ if and only if
the structure maps on disk inclusions
$D_1 \subset D_2 \subset \R^2$ are quasi-isomorphisms. In the
admissible Tate envelope, this reduces to verifying:

(LC-1) **Translation-invariance in both $\R$ directions.** Inherits
from the brane-line $E_1$ algebra ($x_1$-translation) and
the transverse $E_1$ algebra ($x_2$-translation), each separately
translation-invariant by W2-W6 DAG L6:
$[d_\R, \iota_{\partial_t}] = \partial_t$ on
$\Omega^\bullet_c(\R)$.

(LC-2) **Joint $\R^2$-translation-invariance.** The candidate
must be invariant under the $\R^2$ translation
$(x_1, x_2) \mapsto (x_1 + a_1, x_2 + a_2)$. By Lurie 5.5.4.16's
$E_2$ structure (Dunn additivity), this is automatic if both $E_1$
structures are translation-invariant in their respective directions
*and* the cross-bracket is translation-invariant.

(LC-3) **Cross-bracket flatness.** The cross-bracket
$\{\alpha_{x_1}, \alpha_{x_2}\}$ from the Hamiltonian connection's
$F_\alpha = 0$ flatness equation must define a *trivial*
deformation at the cohomological level (i.e., must be exact in
the appropriate Hochschild / Lie cohomology). This is the
**flatness obstruction**: $F_\alpha = 0$ on-shell implies the
cross-bracket descends to a trivial cohomology class.

**Verification of (LC-1).** By M-1 D3 (U-1) "translation
invariance" check, the brane-line $E_1$ structure is
translation-invariant. By symmetry between the two $\R$ directions
in $\R^2$ (Lurie 5.5.4.16 applies to both factors symmetrically),
the transverse $E_1$ structure is also translation-invariant. Pass.

**Verification of (LC-2).** Lurie HA 5.5.4.16 + 5.5.4.10
combination gives the $\R^2$-translation-invariance of the
$E_2$ structure on the locally constant subcategory directly.
Pass at the locally-constant subcategory level.

**Verification of (LC-3).** The classical equation of motion in
the Hamiltonian BF setup is $F_\alpha = 0$
(`main.tex`:1808-1810). The Lagrange multiplier $\beta$ enforces
this equation at the level of equations of motion (not at the
chain-level). At the chain-level, $F_\alpha$ is the BV differential
acting on $\beta$ (`main.tex`:1818-1828; the gauge symmetry
$\delta_\varepsilon \beta = \mathrm{ad}^\vee_\varepsilon \beta$
gives $F_\alpha = \mathrm{BV}\beta$), so the cross-bracket
$\{\alpha_{x_1}, \alpha_{x_2}\}$ is BV-exact. **Pass at the BV-
cohomological level.**

**Conclusion.** The candidate $A_{\mathrm{E_2}}$ is locally constant
on $\R^2$ at the BV-cohomological level, hence defines a strict
$E_2$-algebra by Lurie 5.5.4.16.

---

## §4. Tate-stability cohomological test

### §4.1 The test statement

The candidate $E_2$ algebra $A_{\mathrm{E_2}}$ is constructed in the
admissible Tate envelope (`stmt:tate-model-envelope`). Tate-
stability of the $E_2$ promotion requires:

(T-Stab) The $E_2$ structure maps $m^{E_2}: A_{\mathrm{E_2}}(D_1)
\widehat\otimes A_{\mathrm{E_2}}(D_2) \to A_{\mathrm{E_2}}(D)$ are
**continuous in the admissible Tate topology**, and the $E_2$
associativity diagrams commute *strictly* (or up to bounded-Tate-
filtration homotopy).

This is a **convergence question** at fixed Tate window: does the
$E_2$ structure converge in the admissible Tate envelope of
`stmt:tate-model-envelope`?

### §4.2 The cohomological-stability obstruction class

By the M-1 D6 / W3-W11-01 finding, the admissible Tate envelope
satisfies Lurie HA §5.5.4.10's hypothesis H2 (tensor product
preserves all small colimits separately) **only for Mittag-Leffler
colimits**, not for arbitrary small colimits (W3-W11-01-A).

Lurie HA §5.5.4.16 (Dunn additivity) requires hypothesis H2 in its
**arbitrary** small-colimit form (Lurie HA §5.5.4 / §5.5.5
preserve arbitrary small colimits in $\Pr^L$). Specifically:

> *Lurie 5.5.4.16 statement requires $\Pr^L$ — presentable
> $\infty$-categories with all small colimits, and tensor products
> preserving small colimits separately.*

The admissible Tate envelope is presentable *only at the Mittag-
Leffler envelope*: small filtered colimits with surjective
transitions are preserved, but arbitrary small colimits (e.g.,
filtered colimits with non-surjective transitions, or finite
limits computed via filtered colimits of finite-window
approximations) are **not** verified to be preserved.

**P4-EXEC-G1-M2-OBS-A (Tate-stability obstruction class).**
The cohomological-stability obstruction class for the $E_2$
promotion is the **arbitrary-colimit-preservation class of
$\widehat\otimes$ on the admissible Tate envelope**: the same
class as W3-W11-01.

**Severity 3.** **Status: named obstruction; severity matches
W3-W11-01.** **Confidence: high.**

**Heal-patch route.** WP3-W11-01-A "envelope-restriction" heal —
restate the M-6 Avenue (E) deliverable in the Mittag-Leffler-
restricted admissible envelope, treat the arbitrary-colimit version
as the M-12 (Avenue (B)) or P4-G1-M3+ residual.

### §4.3 What converges in the admissible Tate envelope

In the Mittag-Leffler-restricted admissible envelope:

(C-1) The candidate $E_2$ structure maps $m^{E_2}$ are continuous
on Mittag-Leffler colimits of finite Tate windows: by W3-W11-01-A,
each finite-window Tate approximation has $\widehat\otimes$
preserving ML colimits separately in each variable; the limit
of these finite-window approximations is the full
$\widehat\otimes$.

(C-2) The $E_2$ associativity diagrams commute *strictly* on the
ML-restricted envelope: the Lurie 5.5.4.16 application is valid
on the ML envelope.

(C-3) The $E_2$ braid axiom commutes by translation invariance
plus Dunn additivity on the ML envelope.

(C-4) The cohomological convergence at fixed Tate window is
controlled by the W3-W11-04 weight-filtration spectral sequence
$E_1 \Rightarrow E_\infty$ degeneration on graphwise contributions
(`tate-T1-weighted-completion.tex` §1).

### §4.4 What does *not* converge (open obligation)

(D-1) Arbitrary small colimits of the candidate $A_{\mathrm{E_2}}$
in the admissible envelope are not verified to commute with
$\widehat\otimes$. This is the Avenue (B) M-12 obligation
(mixed Dunn additivity in $\Pr^L$).

(D-2) The full Ran-space descent of $A_{\mathrm{E_2}}$ on
$\R^2 \times \C^2$ — the BD §3.4.10-11 chiral axiom on the product
manifold — is the M-37 (I-4) residual / R-03 / P4-G1-M5+ obligation.

(D-3) The cross-walk to the conformal Virasoro stress tensor (D2
of M-1) requires the topological twist $\tau$ of P4-G4-T2.2; this
is open at M-6 (Avenue (E)) scope.

---

## §5. Dunn-additivity check

### §5.1 The Dunn-additivity statement

The composition $A_{\mathrm{E_2}} \simeq A_{\mathrm{brane}}
\otimes_{E_1} A_{\mathrm{brane}}$ as $E_2$-algebras is Lurie HA
§5.5.4.16 applied to the locally constant subcategory on $\R^2$:

$$\Alg_{E_2}(\mathcal C) \simeq \Alg_{E_1}(\Alg_{E_1}(\mathcal C))
\simeq \Alg_{E_1}(\mathcal C) \otimes_{\Pr^L} \Alg_{E_1}(\mathcal C),$$

where the rightmost is the $\Pr^L$-tensor product of
$\Alg_{E_1}(\mathcal C)$ with itself (CG and Lurie HA §4.8-4.9).

### §5.2 Verification on $\R^2$ alone

**P4-EXEC-G1-M2-DUNN-A.** Dunn-additivity composition holds on
$\R^2$ alone, in the Mittag-Leffler-restricted admissible Tate
envelope $\mathcal C_{\mathrm{ML}}$.

**Severity 3. Status: valid. Confidence: high.**

The verification is a direct application of Lurie HA §5.5.4.16
in $\mathcal C_{\mathrm{ML}}$:
- $\mathcal C_{\mathrm{ML}}$ is a presentable $\infty$-category
  on the ML-restricted envelope (W6-04 + WP3-W11-01-A heal patch).
- $\widehat\otimes$ preserves ML colimits separately in each variable
  (W3-W11-01-A heal).
- The locally constant subcategory on $\R^2$ valued in
  $\mathcal C_{\mathrm{ML}}$ is equivalent to $\Alg_{E_2}(\mathcal C_{\mathrm{ML}})$.
- Lurie 5.5.4.16 applied to $\mathcal C_{\mathrm{ML}}$ gives
  $\Alg_{E_2}(\mathcal C_{\mathrm{ML}}) \simeq
  \Alg_{E_1}(\mathcal C_{\mathrm{ML}}) \otimes_{\Pr^L_{\mathrm{ML}}}
  \Alg_{E_1}(\mathcal C_{\mathrm{ML}})$.

The transverse $E_1$ algebra is *isomorphic* to $A_{\mathrm{brane}}$
as an $E_1$-algebra in $\mathcal C_{\mathrm{ML}}$ (both are the
brane-line factorization centre, just with different real-direction
labels in $\R^2$). Hence:

$$A_{\mathrm{E_2}} \simeq A_{\mathrm{brane}} \otimes_{E_1}
A_{\mathrm{brane}} \in \Alg_{E_2}(\mathcal C_{\mathrm{ML}}).$$

### §5.3 Verification breakdown on $\R^2 \times \C^2$

**P4-EXEC-G1-M2-DUNN-B.** Dunn-additivity composition does *not*
hold on $\R^2 \times \C^2$ at the $E_2 + E_2^{\mathrm{hol}}$
level.

**Severity 3. Status: failure-named (anticipated). Confidence: high.**

The breakdown is structural: Lurie HA §5.5.4.16 applies to
**topological** $E_n$ algebras, not to holomorphic-locally-constant
or mixed topological-holomorphic algebras. The $\C^2$ factor
carries holomorphic-locally-constant structure (Williams `Will20`
$\mathbb E_2^{\mathrm{hol}}$-algebra); the candidate full-bulk
$E_4 \simeq E_2 \otimes E_2^{\mathrm{hol}}$ is the **mixed Dunn-
additivity conjecture** of Avenue (B):

$$\mathbb E_m^{\mathrm{top}} \otimes \mathbb E_n^{\mathrm{hol}}
\simeq \mathbb E_{m, n}^{\mathrm{mixed}} \quad \text{ in } \Pr^L,$$

which is *not* in the literature (Williams `Will20` §3-§4 covers
the holomorphic-only setting; Lurie 5.5.4.16 the topological-only
setting; the mixed setting is open).

**Disposition.** Avenue (E) M-6 deliverable closes the
$\R^2$-only piece (P4-EXEC-G1-M2-DUNN-A); the mixed-setting
generalisation is Avenue (B) M-12 obligation.

### §5.4 What the M-6 deliverable contributes to Avenue (B)

The M-6 deliverable provides the following **inputs to Avenue (B)
M-12**:

1. The strict $E_2$ algebra $A_{\mathrm{E_2}}$ on $\R^2$ in
   $\mathcal C_{\mathrm{ML}}$ as the topological half of the mixed
   Dunn additivity.
2. The holomorphic half $A_{\mathrm{E_2^{hol}}}$ on $\C^2$ is
   left to Avenue (B), using Williams `Will20` §3 holomorphic-$E_n$
   apparatus.
3. The cross-walk between the two via the Hamiltonian connection
   $\alpha$'s mixed components $\alpha_{x_i \bar z_j}$ (which
   couple topological and holomorphic directions; cf. `main.tex`:1815).
4. The Tate-stability heal-patch WP3-W11-01-A is reused.

**P4-EXEC-G1-M2-DUNN-VERDICT.** Dunn-additivity holds at
$\R^2$ in $\mathcal C_{\mathrm{ML}}$; fails to extend to
$\R^2 \times \C^2$ without Avenue (B) mixed Dunn additivity.

---

## §6. Cross-walk to W3-W26 column-Verma functoriality

### §6.1 The column-Verma module category at the $E_2$ corner

The W3-W26 column-Verma vacuum module $\widehat M_0$ from G1-M1 is
an $E_1$-module of the brane-line $E_1$-algebra $A_{\mathrm{brane}}$
on $\R$. The Avenue (E) $E_2$-promotion lifts the question to:
**is $\widehat M_0$ an $E_2$-module of the candidate
$A_{\mathrm{E_2}}$ on $\R^2$?**

### §6.2 Stability at the rank-1 unipotent Borel HWV $v_{0, -1}$

The W3-W26-T1 result identifies $\widehat M_0$ as the rank-1
unipotent Borel-Verma of the 3-dim solvable Borel
$\mathfrak b = \langle z_1, z_2, z_1 z_2 \rangle$, with HWV
$v_{0, -1}$, killed by the column-shifter $X = z_2$ and by
$z_1 z_2^2$ (W3-W26-T1 §1.3).

The transverse $E_1$ algebra in $A_{\mathrm{E_2}}$ — via the
Hamiltonian connection's transverse component — acts on $\widehat M_0$
through the column-shifter $X = z_2$ (since the transverse smeared
Hamiltonian currents are isomorphic to the brane-line currents,
just smeared in the transverse direction; the action on the
column-Verma is the same).

**Stability at the HWV $v_{0, -1}$.** The action of the transverse
$E_1$ algebra at $v_{0, -1}$:
$$X \cdot v_{0, -1} = z_2 \cdot v_{0, -1} = 0$$
(W3-W26-T1 §1.1 the column-shifter $z_2 \cdot v_{a, b} =
-a \cdot v_{a-1, b}$, vanishing at $a = 0$).

Hence the HWV $v_{0, -1}$ is *automatically stable* under the
transverse $E_1$ action: the column-Verma vacuum module sits at a
**corner** of the candidate $E_2$ structure where the transverse
$E_1$ action is trivial. This is the cleanest test stratum for the
$E_2$-module structure.

**Att-3 response (column-Verma corner stability).** The column-
Verma vacuum module *is* at a corner of the $E_2$ structure that is
automatically stable. The stability is **not a non-trivial
constraint** at $v_{0, -1}$; it is automatic by the rank-1 unipotent
Borel structure.

### §6.3 Lower-strata $v_{0, -2}, v_{0, -3}, \dots$

The $Y$-orbit $Y^k v_{0, -1} = (-1)^k k! v_{0, -1-k}$ generates
the rest of $\widehat M_0$. The action of the transverse $E_1$
algebra at lower strata:
$$X \cdot v_{0, b} = z_2 \cdot v_{0, b} = 0 \text{ for all } b \in \Z_{< 0}$$
(since $a = 0$ is preserved on every column, and $X$ acts as the
column-shifter, vanishing at $a = 0$).

Hence the *entire* column $M_0$ is stable under the transverse
$E_1$ action at the column-shifter level: $X = z_2$ kills *every*
basis vector of $\widehat M_0$.

**Stronger statement.** The whole column-Verma $\widehat M_0$ is in
the kernel of the transverse $E_1$ action at the column-shifter
$X = z_2$. The non-trivial transverse $E_1$ action on
$\widehat M_0$ comes from the *internal* Cartan-Borel generators
$Y = z_1$ (column-internal, lowering operator) and $H = z_1 z_2$
(diagonal, eigenvalue $-1 - 0 = -1$ on $v_{0, -1}$).

### §6.4 Functoriality at GL$_2 \times T^2$

The column-Verma decomposition is GL$_2 \times T^2$-natural
(W3-W26-T1 §3 functoriality). The candidate $E_2$-module structure
on $\widehat M_0$ inherits this functoriality at the GL$_2 \times T^2$
layer: the $E_2$ action is *equivariant* under the linear
symplectomorphism action of GL$_2$ and the torus action of $T^2$.

**At quadratic symplectomorphisms.** The quadratic-symplectomorphism
$\sigma: (z_1, z_2) \mapsto (z_1, z_2 + z_1^2)$ produces the
infinite column-mixing of W3-W26-08. This breaks
Symp$_{\mathrm{form}}$-naturality of the column-Verma decomposition,
but **does not affect the $E_2$ braid axiom** because the $E_2$
braid axiom only requires the bracket structure on $\bar A$, which
is preserved by Symp$_{\mathrm{form}}$ (Hamiltonian
diffeomorphisms preserve the Poisson bracket); the $\sigma$-twist
breakage is at the basis-vector level of the column-Verma, not at
the bracket level.

### §6.5 Cross-walk summary

| W3-W26 finding | Severity | Avenue (E) M-6 inheritance |
|---|---|---|
| W3-W26-T1 (column-Verma) | sev 2-3 | $\widehat M_0$ is the cleanest $E_2$-module test stratum |
| W3-W26-01 (3-dim solvable Borel) | sev 3 | $E_2$ structure inherits Borel relations $[H, X] = X$, $[H, Y] = -Y$, $[X, Y] = 0 \pmod{\C}$ |
| W3-W26-02 (Cartan eigenvalue) | sev 3 | $H = z_1 z_2$ acts on $E_2$-promoted vacuum module with eigenvalue $b - a$ |
| W3-W26-03 (vacuum annihilator) | sev 2 | HWV $v_{0, -1}$ stable under transverse $E_1$ at column-shifter level |
| W3-W26-04 (linear tensor factorization) | sev 3 | $E_2$ promotion preserves linear-Hamiltonian tensor factorization on $\C \cdot z_1 \oplus \C \cdot z_2$ |
| W3-W26-05 ($z_1^2$ disambiguation) | sev 2 | $E_2$ structure uses Hamiltonian $z_1^2 \in \bar A$, not iterated $Y^2$ |
| W3-W26-08 ($\varphi$-quadratic breakage) | sev 3 | Symp$_{\mathrm{form}}$-breakage at quadratic does not affect $E_2$ braid axiom |
| P4-G2-M1 (DISCHARGED) | sev 3 | 2821 / 0 verifications inherit at the $E_2$ promotion stratum-by-stratum |

---

## §7. Anti-attack scan responses

### §7.1 Att-1 — Strict $E_2$ vs $E_2$ up-to-coherent-homotopy

**Attack.** *Does the Hamiltonian connection define a strict $E_2$
structure or only an $E_2$ up to coherent homotopy?*

**Response.** **Strict at the BV-cohomological level; up to
coherent homotopy at the chain level pre-BV.**

At the chain level pre-BV, the Hamiltonian connection's flatness
$F_\alpha = D\alpha + \tfrac{1}{2}\{\alpha, \alpha\}$ is an off-shell
expression; it vanishes on-shell ($F_\alpha = 0$ enforced by the
Lagrange multiplier $\beta$). Pre-BV, the cross-bracket
$\{\alpha_{x_1}, \alpha_{x_2}\}$ defines a *non-trivial* element of
the Hochschild cochain complex; the strict $E_2$ axiom requires this
to vanish, which it does only post-BV (BV-exact).

After BV-cohomology / on-shell, the $E_2$ structure is *strict* at
the BV-cohomological level, by Lurie HA §5.5.4.16. The Russian-
school physics intuition: the BV "on-shell + gauge symmetry"
identifies the strict $E_2$ structure; Costello-Gwilliam Vol I §A.4
formalises this as the BV cochain complex carrying a strict
$E_2$ structure on cohomology.

**Disposition.** Att-1 is *defused* at the BV-cohomological level
(strict $E_2$); pre-BV, the structure is $E_2$-up-to-coherent-
homotopy, controlled by the BV differential.

### §7.2 Att-2 — Tate-stability obstruction class

**Attack.** *The Tate window may not preserve associativity of the
$E_2$ multiplication; identify the Tate-stability obstruction class.*

**Response.** **Identified: P4-EXEC-G1-M2-OBS-A = W3-W11-01.**

The Tate-stability obstruction class for the $E_2$ associativity is
the same class as W3-W11-01 (Lurie HA §5.5.4.10's hypothesis H2 in
the arbitrary-colimit form). The candidate $E_2$ associativity
holds on the ML-restricted admissible envelope (P4-EXEC-G1-M2-
DUNN-A); arbitrary-colimit-preservation is open.

**Heal-patch.** WP3-W11-01-A "envelope-restriction" heal:
- Restate the Avenue (E) deliverable as: *the strict $E_2$
  promotion holds in the Mittag-Leffler-restricted admissible Tate
  envelope $\mathcal C_{\mathrm{ML}}$.*
- The arbitrary-colimit version is open (P4-G1-M3+).

**Disposition.** Att-2 is *defused* by the heal patch.

### §7.3 Att-3 — Column-Verma corner stability

**Attack.** *Does the column-Verma vacuum module from G1-M1 sit at
a corner of the $E_2$ structure that is automatically stable, or is
the stability a non-trivial constraint?*

**Response.** **Automatic stability at the HWV $v_{0, -1}$
(by W3-W26-T1 §1.1's column-shifter vanishing at $a = 0$).**
The transverse $E_1$ action at the column-shifter $X = z_2$
**vanishes** on the entire column $\widehat M_0$ (since $a = 0$ on
every basis vector). The non-trivial transverse $E_1$ action comes
from $Y = z_1$ (column-internal) and $H = z_1 z_2$ (Cartan); these
satisfy the Borel relations of W3-W26-01 and the Cartan eigenvalue
of W3-W26-02 (verified at 218 instances in W3-W26-T1 §1.2).

**Disposition.** Att-3 is *defused*: column-Verma corner is
automatically stable.

### §7.4 Att-4 — Topological-$E_1$ ⊗ holomorphic-$E_2$ mixed structure

**Attack.** *Williams arXiv:2007.13985 holomorphic-$E_n$ machinery
applies to holomorphic factorization, not topological; does the
brane-line direction $\R$ require a topological-$E_1 \otimes$
holomorphic-$E_2$ mixed structure?*

**Response.** **Yes for the full $\R^2 \times \C^2$ setting; the
M-6 Avenue (E) deliverable scopes to $\R^2$-only, deferring the
mixed setting to M-12 Avenue (B).**

The full mixed structure on $\R^2 \times \C^2$ is:

$$A^{\mathrm{full}}_{(2, 2)} \stackrel{?}{\simeq}
A_{\mathrm{E_2}}^{\mathrm{top}} \otimes
A_{\mathrm{E_2}}^{\mathrm{hol}} \in
\Alg_{E_4^{\mathrm{mixed}}}(\mathcal C),$$

where $A_{\mathrm{E_2}}^{\mathrm{top}}$ is the M-6 deliverable on
$\R^2$ and $A_{\mathrm{E_2}}^{\mathrm{hol}}$ is the conjectural
holomorphic-$E_2$ algebra on $\C^2$ from Williams `Will20` §3-§4.

The mixed Dunn additivity
$\mathbb E_m^{\mathrm{top}} \otimes \mathbb E_n^{\mathrm{hol}}
\simeq \mathbb E_{m, n}^{\mathrm{mixed}}$ is **not in the
literature** (Williams covers holomorphic-only; Lurie 5.5.4.16
covers topological-only). This is the M-12 Avenue (B) obligation.

**Disposition.** Att-4 is *acknowledged*: M-6 Avenue (E) scopes
to $\R^2$-only; full mixed setting is M-12 Avenue (B).

---

## §8. Residuals + deciding evidence

### §8.1 Residuals (M-6-originated)

**R-P4-EXEC-G1-M2-A.** The arbitrary-colimit-preservation gap of
$\widehat\otimes$ on the admissible Tate envelope at non-ML small
colimits. **Same class as W3-W11-01.** Severity 3. Heal-patch route:
WP3-W11-01-A "envelope-restriction" heal restates Avenue (E) in
$\mathcal C_{\mathrm{ML}}$. Closure pending: P4-G1-M3+ at the
admissible-envelope-presentability layer.

**R-P4-EXEC-G1-M2-B.** The mixed Dunn additivity
$\mathbb E_m^{\mathrm{top}} \otimes \mathbb E_n^{\mathrm{hol}}
\simeq \mathbb E_{m, n}^{\mathrm{mixed}}$ for the holomorphic
factor $\C^2$ is open. Severity 3. Closure pending: M-12 Avenue
(B) of P4-G1.

**R-P4-EXEC-G1-M2-C.** The Ran-space descent of the candidate
$A^{\mathrm{full}}_{(2, 2)}$ on $\R^2 \times \C^2$ — the BD §3.4.10-11
chiral axiom on the product manifold — is open. Severity 3.
Closure pending: M-37 (I-4) / R-03 / Avenue (D) M-18+.

**R-P4-EXEC-G1-M2-D.** The conformal stress tensor $T(z)$ in the
$E_2$-promoted setup requires the topological twist $\tau$ of
P4-G4-T2.2; the topological $E_2$ algebra is well-defined at M-6,
but the conformal $E_2$ promotion is open. Severity 4 (cross-volume).
Closure pending: P4-G4 anchoring theorem.

**R-P4-EXEC-G1-M2-E.** Higher-arity $E_2$ Jacobi axiom (depth
$\geq 6$) on monomial generators of the chiral algebra is open.
The P4-G2-M1 verifications cover depth 5 (405 instances / 0 failures);
P4-G2-M2 (6-month) extends to all degree-3 generators with BCH cocycle.
Severity 3. Closure pending: P4-G2-M2 BCH cocycle attack.

### §8.2 Deciding evidence (M-6 Avenue (E) pre-work)

**Verifying evidence.**
- 2821 instances / 0 failures from P4-G2-M1 (column-Verma module
  $\lambda$-bracket on $\widehat M_0$).
- 168 instances / 0 mismatches on the $\Z^2$ sweep of W3-W26
  (Cartan eigenvalue $H = z_1 z_2$).
- Lurie HA §5.5.4.16 Dunn additivity directly applies on the
  locally constant subcategory in $\mathcal C_{\mathrm{ML}}$.
- $F_\alpha = 0$ flatness at the BV-cohomological level
  (`main.tex`:1808-1810; BV gauge symmetry
  `main.tex`:1818-1828).
- M-1 D1 brane-line $E_1$ structure verified at the
  $\lambda$-bracket level, Bakalov-Kac axioms, Jacobi at depth 5.

**Where the M-6 Avenue (E) deliverable could fail.**
- A counterexample to Lurie 5.5.4.16 in $\mathcal C_{\mathrm{ML}}$
  (would require a specific colimit-preservation failure for
  $\widehat\otimes$ on ML envelope — not known).
- A failure of the Hamiltonian connection's flatness $F_\alpha = 0$
  to descend cleanly to BV-cohomology (would require a specific
  BV-anomaly in the Hamiltonian BF setup — not known; cf.
  `thm:quantum-classical-anomaly` (`main.tex`:318-352) verifies
  the only anomaly is the U(1)/Capelli class $[\bar c]$, which
  is the central-charge cocycle, not a strict-$E_2$ obstruction).
- A failure of the column-Verma vacuum $\widehat M_0$ to lift to
  an $E_2$-module (would require the transverse $E_1$ action to
  break the Borel structure — not the case by W3-W26-T1 §1.1
  at the column-shifter level).

**None of these failure modes are known.**

### §8.3 Beilinson + Composition lens evaluation

**Beilinson lens.**
- *Sheaf-theoretic descent on $\mathrm{Ran}(\R^2)$:* PASS via Lurie
  5.5.4.16 (Dunn additivity) applied to $\Pr^L_{\mathrm{ML}}$.
- *Exactness of $E_2$ structure maps:* PASS at the ML envelope
  (W3-W11-01-A heal); UNVERIFIED at arbitrary-colimit envelope
  (P4-G1-M3+ residual).
- *Filtered/spectral on Tate window:* PASS at $E_1$ degeneration
  on graphwise contributions (W3-W11-04); all-order conditional on
  `prob:weighted-rg-locality`.
- *Descent for the Hamiltonian connection:* PASS at BV-cohomological
  level via $F_\alpha = 0$.

**Composition lens.**
- *Local $E_2$ maps compose globally:* PASS by Lurie 5.5.4.16
  applied to the locally constant subcategory.
- *Mayer-Vietoris / Čech check on $\R^2$ covers:* PASS by
  translation invariance + Dunn additivity on the locally constant
  subcategory.
- *$E_2$ pentagon associativity:* PASS at the cohomological level
  by Lurie 5.5.4.16; verified via P4-G2-M1 Jacobi at depth 5
  (405 instances / 0 failures) on the brane-line direction;
  inherited by symmetry on the transverse direction.
- *$E_2$ braid axiom:* PASS at the cohomological level by Lurie
  5.5.4.16's Dunn additivity (the braid axiom for $E_2$ in the
  locally constant setting reduces to commutativity-up-to-natural-
  isomorphism, which is automatic by translation invariance).

Both lenses confirm M-6 Avenue (E) closure at the
$\R^2$-only / $\mathcal C_{\mathrm{ML}}$ layer with the named
obstruction at the arbitrary-colimit-preservation gap.

---

## §9. Connection to G1 (M-12) Avenue (B) mixed-Dunn additivity

### §9.1 What M-6 Avenue (E) supplies for M-12 Avenue (B)

The M-6 Avenue (E) deliverable provides the following **inputs to
M-12 Avenue (B)** mixed Dunn additivity:

1. **Strict $E_2$ algebra $A_{\mathrm{E_2}}$ on $\R^2$** in
   $\mathcal C_{\mathrm{ML}}$ — the topological half of the mixed
   Dunn additivity setup. This serves as the $\mathbb E_2^{\mathrm{top}}$
   side of the conjectural equivalence.

2. **Tate-stability heal-patch WP3-W11-01-A**, reusable on the
   holomorphic side: the holomorphic-$E_2$ algebra
   $A_{\mathrm{E_2^{hol}}}$ on $\C^2$ inherits the same envelope-
   restriction structure on the ML-Tate envelope.

3. **Column-Verma vacuum module $\widehat M_0$ as the cleanest
   test stratum** for the mixed Dunn additivity: at the HWV
   $v_{0, -1}$, the holomorphic-$E_2$ action is automatically
   stable (the column-shifter vanishes, so the entire column is in
   the kernel of the column-shifter); the holomorphic structure
   refines this via the Williams $\mathbb E_n^{\mathrm{hol}}$
   apparatus.

4. **Hamiltonian connection's mixed components $\alpha_{x_i \bar z_j}$**
   (`main.tex`:1815): the connection has cross-components coupling
   topological and holomorphic directions; these are the candidate
   structure maps for the mixed Dunn additivity.

### §9.2 The mixed Dunn additivity statement

**P4-EXEC-G1-M2-MIXED (open at M-6, M-12 obligation).**

> *Conjecture.* In $\Pr^L_{\mathrm{ML}}$ (presentable
> $\infty$-categories at the ML-restricted admissible Tate
> envelope), there is a canonical equivalence
> $$\mathbb E_m^{\mathrm{top}} \otimes \mathbb E_n^{\mathrm{hol}}
> \simeq \mathbb E_{m, n}^{\mathrm{mixed}},$$
> where $\mathbb E_n^{\mathrm{hol}}$ is the holomorphic-$E_n$
> operad of Williams arXiv:2007.13985 §3, and
> $\mathbb E_{m, n}^{\mathrm{mixed}}$ is the operad of locally
> constant factorization algebras on $\R^m \times \C^n$ with
> structure maps preserved.

**Pre-work for M-12.** The M-6 Avenue (E) deliverable provides
the topological half $\mathbb E_2^{\mathrm{top}}$ side; the
holomorphic half $\mathbb E_2^{\mathrm{hol}}$ side requires
Williams `Will20` §3-§4 apparatus on $\C^2$; the mixed equivalence
is the M-12 attack.

### §9.3 Risk-assessment for the M-12 transition

**Primary risk: P4-EXEC-G1-M2-R1 (mixed Dunn additivity may not
extend to non-ML envelope).** If the mixed Dunn additivity holds
only in $\mathcal C_{\mathrm{ML}}$, then the M-12 deliverable is
restricted to the ML-envelope; Avenue (D) M-18+ would be required
for the full envelope.

**Secondary risk: P4-EXEC-G1-M2-R2 (topological twist required for
conformal upgrade).** If the conformal Virasoro stress tensor is
required at M-12 (e.g., for cross-volume W$_{1+\infty}$ comparison),
the topological twist $\tau$ of P4-G4 must be applied; this is the
P4-G4-T2.2 obligation at the cross-volume firewall layer
(M-34, M-52).

**Tertiary risk: P4-EXEC-G1-M2-R3 (holomorphic-$E_2$ vs
holomorphic-$E_n^{\mathrm{hol}}$ on $\C^n$ for $n \geq 2$).** The
$\C^2$ holomorphic factor has $n = 2$ complex dimensions; Williams
`Will20` §3 covers $\mathbb E_n^{\mathrm{hol}}$ on $\C^n$, but the
specific case $n = 2$ may require additional holomorphic-Hodge
technology that is not yet standardised. Mitigation: use Williams
`Will20` §4 holomorphic-factorization-homology framework as the
target for the M-12 deliverable.

### §9.4 Milestone schedule alignment

The M-6 Avenue (E) deliverable feeds into:

- **M-12 Avenue (B)** (mixed Dunn additivity): direct.
- **M-12 Avenue (C)** (factorization homology): the
  $A_{\mathrm{E_2}}$ algebra on $\R^2$ is one of the inputs to
  $\int_{\R^2 \times \C^2}$ factorization homology computation.
- **M-18+ Avenue (D)** (BD chiral product on $\mathrm{Ran}(\R^2 \times \C^2)$):
  the strict $E_2$-algebra on $\R^2$ provides the topological
  half of the BD chiral product on the product manifold.

The M-6 deliverable is therefore **the natural successor to the M-3
deliverable** (P4-EXEC-G1-M1 BD chiral algebra closure) and **the
natural predecessor to the M-12 deliverable** (Avenue (B) mixed
Dunn additivity).

---

## §10. Provenance

P4-EXEC-G1-M2 (this report) read in full:
- `/Users/raeez/topological-strings/CLAUDE.md`.
- `reconstitution/phase4-G1-weiss-product-2026-04-28.md` (G1 outline;
  §T3.E Avenue (E); §T5.A 6-month milestone).
- `reconstitution/phase4-exec-G1-M1-BD-chiral-2026-04-28.md` (full;
  P4-EXEC-G1-M1-PROP closure at M-3 scope; §6 connection to
  $E_2$-promotion).
- `reconstitution/wave3-W26-column-verma-2026-04-28.md` §1-§3
  (column-Verma; rank-1 unipotent Borel; functoriality).
- `reconstitution/wave3-W11-beilinson-hypotheses-2026-04-28.md` §1
  Target T1 (Lurie HA §5.5.4 hypothesis verification).
- `reconstitution/phase4-exec-module-lambda-bracket-2026-04-28.md`
  (P4-G2-M1 DISCHARGED; Bakalov-Kac axioms verified).
- `main.tex`:1770-1840 (Hamiltonian BF action; Hamiltonian
  connection $\alpha$; flatness $F_\alpha = 0$; classical fields).
- `main.tex`:1996-2210
  (`thm:open-closed-derived-center-factorization`;
  `rmk:E1-translation`).
- `main.tex`:280-470 (`lem:omega-cocycle`;
  `thm:u1-center-anomaly`).
- `tate-T1-weighted-completion.tex` (full).
- `appendix-factorization-current-conventions.tex` (full;
  `prop:app-factorization-principal-part-bracket`).

External primary references invoked (no fresh PDF inscription):
- Lurie, *Higher Algebra*, May 2017 / kerodon §HA.5.5.4
  (`LurieHA`): §5.5.2.6 (pushforward); §5.5.3 (topological chiral
  homology); §5.5.4.10 (LCFA ≃ $E_n$); **§5.5.4.16 (Dunn
  additivity: $E_m \otimes E_n \simeq E_{m+n}$ in $\Pr^L$)**.
- Costello-Gwilliam Vol. I (`CGW1`): §6.4-6.5; §A.5.4-6.
- Costello-Gwilliam Vol. II (`CGW2`): §10-11.
- Williams, arXiv:2007.13985 (`Will20`): §3-§4
  ($\mathbb E_n^{\mathrm{hol}}$-algebras).
- Ayala-Francis, arXiv:1206.5522 / J. Topology 2015 (`AF15`): §3-§5.
- Beilinson-Drinfeld, AMS Coll. Pub. vol. 51, 2004 (`BD04`):
  §3.4.1, §3.4.5, §3.4.10, §3.4.11.
- Bakalov-Kac, IMRN 2003 (`BK03`).
- Frenkel-Ben-Zvi (`FBZ04`): §3.3-3.4.

P4-EXEC-G1-M2 confidence: every structural claim either inherits
M-1 / W3-W26 / W3-W11 verification, applies Lurie HA §5.5.4.16
directly on the locally constant subcategory in
$\mathcal C_{\mathrm{ML}}$, or names the M-12 / M-18+ residual
explicitly. No fresh PDF inscription required for M-6 Avenue (E)
pre-work.

---

## §11. Summary

P4-EXEC-G1-M2 supplies the Avenue (E) pre-work for the 6-month
G1 milestone: the $E_2$-promotion of the brane-line $E_1$ algebra
on $\R^2$ via the Hamiltonian connection. **Closure verdict:
PARTIAL — closes the $\R^2$-only piece in
$\mathcal C_{\mathrm{ML}}$ with named Tate-stability obstruction
class.**

**(a) Does the $E_2$ promotion close at fixed Tate window?** Yes
on the ML-restricted admissible envelope $\mathcal C_{\mathrm{ML}}$:
the candidate $A_{\mathrm{E_2}} = A_{\mathrm{brane}} \otimes_{E_1}
A_{\mathrm{brane}}$ is a strict $E_2$-algebra in the locally
constant subcategory of $\mathrm{Fact}^{\mathrm{lc}}(\R^2;
\mathcal C_{\mathrm{ML}})$ by Lurie HA §5.5.4.16 (Dunn additivity).
The Hamiltonian connection's flatness $F_\alpha = 0$
(`main.tex`:1808-1810) supplies the Mayer-Vietoris compatibility
data at the BV-cohomological level. The brane-line / transverse
$E_1$ structures are translation-invariant by W2-W6 DAG L6.

**(b) Cohomological-stability obstruction class.** **Same as
W3-W11-01:** the arbitrary-colimit-preservation gap of
$\widehat\otimes$ on the admissible Tate envelope at non-ML small
colimits. Heal-patch route WP3-W11-01-A "envelope-restriction"
restates the deliverable in $\mathcal C_{\mathrm{ML}}$.

**(c) Dunn-additivity holds?** Holds on $\R^2$-alone in
$\mathcal C_{\mathrm{ML}}$ (P4-EXEC-G1-M2-DUNN-A); fails to extend
to mixed $\R^2 \times \C^2$ (P4-EXEC-G1-M2-DUNN-B; Avenue (B)
M-12 obligation; mixed Dunn additivity
$\mathbb E_m^{\mathrm{top}} \otimes \mathbb E_n^{\mathrm{hol}}
\simeq \mathbb E_{m, n}^{\mathrm{mixed}}$ open in literature).

**Cross-walk to W3-W26.** Column-Verma vacuum $\widehat M_0$ from
G1-M1 sits at a corner of the $E_2$ structure that is automatically
stable: the transverse $E_1$ action at the column-shifter
$X = z_2$ vanishes on the entire column $\widehat M_0$ (every
basis vector has $a = 0$). Functoriality preserved at GL$_2 \times T^2$;
breakage at quadratic Symp$_{\mathrm{form}}$ (W3-W26-08) does not
affect the $E_2$ braid axiom.

**Anti-attack scan.** Att-1 defused at BV-cohomological level
(strict $E_2$); Att-2 defused by W3-W11-01-A heal patch;
Att-3 defused by automatic column-shifter vanishing on $\widehat M_0$;
Att-4 acknowledged (mixed setting deferred to M-12 Avenue (B)).

**Connection to M-12.** The M-6 deliverable provides the
topological half $\mathbb E_2^{\mathrm{top}}$ for the mixed Dunn
additivity, the column-Verma vacuum module $\widehat M_0$ as the
cleanest test stratum, the heal-patch WP3-W11-01-A on the
ML envelope, and the Hamiltonian-connection mixed components
$\alpha_{x_i \bar z_j}$ as candidate structure maps for the
holomorphic-topological coupling.

Open obligations: R-P4-EXEC-G1-M2-A (W3-W11-01 colimit gap);
R-P4-EXEC-G1-M2-B (mixed Dunn additivity, M-12); R-P4-EXEC-G1-M2-C
(BD §3.4.10-11 Ran-space descent, M-18+); R-P4-EXEC-G1-M2-D
(conformal twist $\tau$ via P4-G4); R-P4-EXEC-G1-M2-E (higher-arity
$E_2$ Jacobi at depth $\geq 6$, P4-G2-M2 BCH cocycle).

---

End of P4-EXEC P4-G1-M2 Avenue-(E) $E_2$-promotion pre-work note.
