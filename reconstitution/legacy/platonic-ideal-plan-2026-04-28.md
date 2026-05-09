# Platonic-Ideal Plan — Topological Strings Whitepaper

> Superseded control note. This plan was written against the older
> non-canonical critique extraction and contains full-strength
> `Z^{P_0}_{fact}` / open-BV / Matlis quotient language that the
> canonical 08:36 attack-heal pass rejects as unproved. Use only as an
> archival diagnosis. Active roadmap control is
> `reconstitution/roadmap-index-2026-04-28.md`.

**Date.** 2026-04-28.
**Source.** Five-round critical analysis (176 pp.) at
`materials/raw/2026-04-28-whitepaper-critical-analysis.pdf`,
processed copy `materials/processed/2026-04-28-whitepaper-critical-analysis.txt`.
**Manuscript locus.** `main.tex` and bound parts; apparatus in
`theorem-lanes.tex`, `claim-strength-ledger.tex`, `open-obligations.tex`,
`principles.tex`, `local-dictionary.tex`, plus the recent appendices
`appendix-matlis-principal-parts.tex`, `appendix-radial-parts-moyal.tex`,
`appendix-factorization-current-conventions.tex`,
`appendix-unreduced-bv-qme.tex`.

This plan is the synthesis of what the paper is trying to prove, what it
has proved, what it almost-proves but mis-states, and what it must
construct anew. Voice: Russian school, Dirac-style first principles —
brackets, observables, locality before string slogans. The point is not
to shrink the paper. The point is to identify the correct underlying
mathematical structure and write the constructions, derivations, and
deductions that realize it.

---

## §0. Diagnosis: what the paper is actually about

Strip away every adjective and the manuscript is one statement.

> The closed Hamiltonian BF theory of the formal holomorphic symplectic
> disk is the **derived Poisson factorization centre** of a Dirac-reduced
> matrix-probe brane algebra. Its cotangent direction is realized
> physically by **principal-part residue currents** localized at the
> brane defect, and only shadow-realized by the polynomial one-$\psi$
> descendants $\Psi_{a,b}$.

Everything else — the PBW comparison, the Procesi–Razmyslov stable
trace identification, the one-$\psi$ chip-moving homology, the Moyal
target, the Matlis duality, the weighted Tate regulator, the U(1)
center anomaly, the BCOV motivation — is downstream of that one
identification.

The 176-page critical analysis converges on three structural diagnoses.

**(D1) Title-vs-body misalignment in the older draft.** The phrase
"Koszul duality" sounded like a deformation-level theorem; the body
explicitly delivered a PBW special-fibre comparison only. The repair
is not to weaken the result but to **promote** it to the correct
deformation-level theorem — the CE/PV derived-centre isomorphism —
which is genuinely stronger.

**(D2) Source-convention error in the closed-open map.** The boundary
observable $O_f = \mathrm{Tr}\, f(\phi_1,\phi_2)$ was being identified
with the CE coordinate dual to $f \in \mathfrak h$. That coordinate is
not closed (because $\mathfrak h$ is perfect). The correct
identification sends $O_f$ to the CE coordinate **dual to the shifted
cotangent generator** $f^{\vee}[1]$. This is the breakthrough on which
the derived-centre theorem rests.

**(D3) Module mismatch between $\Psi_{a,b}$ and $\rho_{a,b}$.** The
linear-Hamiltonian action $z_1 \cdot \rho_{a,b} = -(b{+}1)\rho_{a,b+1}$
on principal parts is not locally nilpotent; the action $O_{1,0}\colon
\Psi_{a,b} \mapsto b\,\Psi_{a,b-1}$ on polynomial descendants is. Local
nilpotence is preserved by module isomorphism. Hence no map
$\Psi_{a,b} \mapsto \rho_{a,b}$ is an $\mathfrak h$-module
intertwiner. The PBW shadow and the coadjoint module share a label set,
not a module structure. Any "interpolation" must change category — a
Rees $D_\hbar$-module construction, not an algebra-level
identification.

The current manuscript — to its credit — already encodes (D1)–(D3) in
the apparatus files (`open-obligations.tex` lines 42–69, 328–337;
`theorem-lanes.tex` lines 53–55, 328–337). What remains is to make
**every theorem statement and every prose paragraph** reflect those
distinctions, and to **add the platonic constructions** that the
analysis has now identified. This document is that programme.

---

## §1. The platonic-ideal thesis

One paragraph, to be installed verbatim near the beginning of the
introduction:

> A stack of $N$ probe branes is a Dirac-constrained measurement of
> the formal holomorphic symplectic disk. Its stable connected
> Hamiltonian trace algebra $A_\partial = S(\mathfrak h)$ is the open
> measurement algebra. The closed Hamiltonian BF theory is the shifted
> cotangent theory $\mathfrak g = \mathfrak h \ltimes \mathfrak h^\vee_{\mathrm{cont}}[1]$
> of infinitesimal canonical transformations of the disk. The closed
> Chevalley–Eilenberg observables are exactly the derived Poisson
> centre of the open algebra:
> $$
> C^\bullet_{\mathrm{CE,cont}}(\mathfrak h \ltimes \mathfrak h^\vee_{\mathrm{cont}}[1])
> \;\cong\; \mathrm{PV}(S(\mathfrak h))
> \;\simeq\; Z^{P_0}_{\mathrm{fact}}(S(\mathfrak h)),
> \qquad c^I \mapsto \theta_I,\;\; u_I \mapsto O_I.
> $$
> Cotangent generators correspond to boundary trace Hamiltonians; the
> polynomial one-$\psi$ descendants $\Psi_{a,b}$ are the PBW
> special-fibre shadow; the deformation-level cotangent module is the
> principal-part Matlis dual $\mathfrak h^\vee_{\mathrm{cont}} \cong \mathcal P
> = H^2_{\mathfrak m}(\mathbb C[[z_1,z_2]])\,dz_1\,dz_2 / \mathbb C\rho_{0,0}$,
> realized as residue currents transverse to the brane. The scalar
> $U(1)$/Capelli class is the same distinguished anomaly classically
> and quantum-mechanically.

This is what the paper is. The work below is to make every theorem
and section align with it.

---

## §2. First-principles foundation: the three Diracian principles

`principles.tex` already contains the three principles in the right
form. The platonic version emphasises that **factorization algebras are
forced** by Diracian observable algebra; they are not categorical
decoration.

### Principle 1 — Dirac (constrained probe).

The brane stack probes the formal symplectic disk by matrix
substitution $z_i \rightsquigarrow \phi_i$. The symplectic potential
is forced: $\theta_N = \mathrm{Tr}(\phi_1\, d\phi_2)$. Conjugation
invariance gives the moment map $\mu_\epsilon = -\mathrm{Tr}(\epsilon[\phi_1,\phi_2])$,
the open action $S_\partial = \int_{\mathbb R} \mathrm{Tr}(\phi_1\, d\phi_2 + A[\phi_1,\phi_2])$,
and the BV Koszul differential $Q\psi = [\phi_1,\phi_2]$. This is
**Dirac reduction in homological form**, not a stringy ansatz.

### Principle 2 — Witten (closed-open centrality).

A closed insertion brought to the brane is not a boundary value but a
**central operation** on the open observable algebra. Therefore the
correct target of the closed-open map is the derived Poisson
factorization centre $Z^{P_0}_{\mathrm{fact}}(\mathrm{Obs}_{\mathrm{open}})$,
not $\mathrm{Obs}_{\mathrm{open}}$ itself. The substitution $f \mapsto
\mathrm{Tr}\,f(\phi_1,\phi_2)$ is the **moment-map shadow** of the
larger structure. Boundary functions are images of cotangent CE
coordinates $u_I$; closed Hamiltonian ghost coordinates $c^I$ map to
constant polyvector field operations.

### Principle 3 — Grothendieck (residue duality).

The continuous dual of holomorphic functions is not another family of
holomorphic functions; it is the **Matlis local-cohomology module of
residue currents**,
$$
\mathfrak h^\vee_{\mathrm{cont}} \;\cong\; \mathcal P
\;\;=\;\;
H^2_{\mathfrak m}(\mathbb C[[z_1,z_2]])\, dz_1\, dz_2 \,\big/\, \mathbb C\,\rho_{0,0},
\qquad \rho_{a,b} = z_1^{-a-1}z_2^{-b-1}\,dz_1\,dz_2.
$$
The reduced exclusion $a+b>0$ is the dual of removing constants from
$\mathfrak h$, and ties directly to the scalar $\rho_{0,0} \leftrightarrow 1
\leftrightarrow \mathrm{Tr}(1) = N$ identification — the same class
that propagates as the U(1)/Capelli anomaly.

**Locality from these three principles.** Three notions of locality
arise canonically:

1. **Support locality on the brane line** — $\delta(t-s)$ contact terms
   from equal-time Poisson brackets.
2. **Topological locality** in the brane direction — $L_v = [Q,\iota_v]$,
   so factorization is locally constant.
3. **Formal holomorphic / distributional locality** transverse to the
   brane — $L_{\partial/\partial \bar z_i} = [Q,\iota_{\partial/\partial \bar z_i}]$;
   coadjoint modes are residue currents (defect-localised
   distributions, not smooth fields).

Unitarity is replaced by CME/QME plus factorization associativity. The
model is a protected cohomological sector; if a unitary parent theory
exists, unitarity belongs to the parent.

---

## §3. The theorem package — six independent blocks

The umbrella theorem in the current draft fuses too many statements.
The platonic version splits the result into six independent theorem
blocks A–F (plus the anomaly theorem G), each with its own status,
proof skeleton, and dependencies. This matches the lane decomposition
already adopted in `theorem-lanes.tex`; the work is to align main-text
prose and theorem statements with that split.

### Theorem A — Dirac brane probe theorem
**Status.** Proved in finite algebraic model.
**Anchor.** `theorem-lanes.tex` Lane 1 (lines 12–50).

> **Theorem.** For the brane $\mathbb R \times \{0\} \subset \mathbb R^2 \times \mathbb C^2$,
> the ghost-zero open BV action is the Dirac first-order constrained
> system $S_\partial = \int_{\mathbb R} \mathrm{Tr}(\phi_1\,d\phi_2 + A[\phi_1,\phi_2])$,
> with reduced local BV algebra $R_N = \mathbb C[\phi_1,\phi_2]\otimes\Lambda(\psi)$,
> $Q\psi = [\phi_1,\phi_2]$, $Q\phi_i = 0$.

**Proof skeleton.** Symplectic potential forced from $\Omega_N =
\mathrm{Tr}(d\phi_1 \wedge d\phi_2)$; constraint first-class with
moment map $\mu_\epsilon$; BV reduction = homological version of Dirac
constraint.

**Action items.**
- Promote `\section{The local physical system}` (currently embedded in
  `principles.tex`) into a numbered theorem at the start of the local
  body.
- Cite finite algebraic status from `claim-strength-ledger.tex`.

### Theorem B — Stable Hamiltonian trace theorem
**Status.** Proved degreewise stable.
**Anchor.** `theorem-lanes.tex` Lane 2 (lines 52–94).

> **Theorem.** The stable connected Hamiltonian open trace sector is
> $$\mathrm{Obs}^{\mathrm{cl}}_{\partial,H} \;\simeq\; S(\bar A \oplus \bar A_{\mathrm{desc}}[1]),$$
> where $\bar A_{\mathrm{desc}}$ is the bidegree label set of primitive
> one-$\psi$ Koszul classes $\Psi_{a,b}$, $a+b>0$.

**Proof skeleton.** (i) Procesi–Razmyslov stable invariants for two
matrices give freely generated cyclic words; (ii) adjacent $xy/yx$
swaps are $Q$-exact via $Q\,\mathrm{Tr}(\psi vu) = \mathrm{Tr}([x,y]vu)$;
(iii) ghost-zero classes labelled by nonconstant commutative monomials;
(iv) one-$\psi$ classes generated by $\Psi_{a,b} = \sum_{w \in W_{a,b}} \mathrm{Tr}(\psi w)$;
(v) Proposition 0.2.28 closure plus the chip-moving state-complex
calculation gives $H_1 = \mathbb C\cdot\Psi_{a,b}$.

**Critical disclaimer.** $\bar A_{\mathrm{desc}} \cong \mathfrak h^\vee_{\mathrm{cont}}$
is a **graded vector-space identification only**, not an
$\mathfrak h$-module identification. This is the **PBW special-fibre
shadow**, not a deformation-level coadjoint realization.

**Action items.**
- Strengthen the one-$\psi$ homology proof per analysis item §24
  (formal $C_2 \to C_1 \to C_0$, sign lemma, cellular-chain lemma,
  attaching-cells lemma, Abel-map cyclic relabelling, stabilizer
  lemma, $S^1$-cycle identification). Move computational script to a
  reproducibility appendix.
- Wherever the older draft writes "Koszul duality of the open
  Hamiltonian sector with the closed Lie algebra", replace by "PBW
  special-fibre shadow of the Koszul dual closed CE algebra".

### Theorem C — CE/PV derived-centre theorem ★ (the platonic centre)
**Status.** Proved degreewise stable.
**Anchor.** `theorem-lanes.tex` Lane 3 (lines 96–148);
`tate-T1`–`tate-T5` for the Tate-categorical enhancement;
`appendix-factorization-current-conventions.tex` for sign data.

> **Theorem.** Let $\mathfrak h = \mathbb C[[z_1,z_2]]/\mathbb C\cdot 1$
> with reduced Poisson bracket, $\mathfrak g = \mathfrak h \ltimes
> \mathfrak h^\vee_{\mathrm{cont}}[1]$, and $A_\partial = S(\mathfrak h) =
> \mathcal O_{\mathrm{poly}}(\mathfrak h^\vee)$ with Kirillov–Poisson
> bracket $\{O_f, O_g\} = O_{\{f,g\}}$. Then there is a canonical
> isomorphism of completed dg commutative algebras and of $P_0$-algebras
> $$
> \Phi:\;
> C^\bullet_{\mathrm{CE,cont}}(\mathfrak g) \;\xrightarrow{\,\sim\,}\;
> \mathrm{PV}(A_\partial) \;\simeq\; Z^{P_0}_{\mathrm{fact}}(A_\partial),
> \qquad c^I \mapsto \theta_I = \partial/\partial O_I,\;\; u_I \mapsto O_I.
> $$
> Under $\Phi$, the CE coordinate $c^I$ dual to a Hamiltonian generator
> $e_I \in \mathfrak h$ maps to the constant polyvector field
> operation $\theta_I$; the CE coordinate $u_I$ dual to the shifted
> cotangent generator $e_I[1] \in \mathfrak h^\vee[1]$ maps to the
> boundary Hamiltonian function $O_I$. The induced moment-map shadow
> $f \mapsto O_f = \mathrm{Tr}\,f(\phi_1,\phi_2)$ satisfies
> $\{O_f, O_g\}_\partial = O_{\{f,g\}}$ in the connected scalar-reduced
> quotient.

**Proof skeleton.**
1. Generator-level identification: $C^\bullet_{\mathrm{CE}}(\mathfrak g) =
   S(u_I) \otimes \Lambda(c^I)$ and $\mathrm{PV}(A_\partial) = S(O_I)
   \otimes \Lambda(\theta^I)$.
2. Differentials match on generators:
   $d_{\mathrm{CE}} c^K = -\tfrac12 C^K_{IJ} c^I c^J$,
   $d_{\mathrm{CE}} u_K = C^L_{KJ} u_L c^J$;
   $d_\pi \theta^K = -\tfrac12 C^K_{IJ} \theta^I \theta^J$,
   $d_\pi O_K = C^L_{KJ} O_L \theta^J$.
3. Shifted-cotangent / Schouten bracket compatibility: $\{c^I, u_J\}
   = \delta^I_J$, $[\theta^I, O_J] = \delta^I_J$.
4. Pass through finite Taylor windows $\mathfrak h_{\le D}$ and Mittag-Leffler
   exact inverse limits to the Tate-completed statement.

**Coordinate-free version.** Lichnerowicz: for $A = S(\mathfrak h)$
linear-Poisson, $\mathrm{PV}(A) \cong C^\bullet_{\mathrm{CE}}(\mathfrak h;
S(\mathfrak h))$ with the coadjoint representation, and
$C^\bullet_{\mathrm{CE}}(\mathfrak h; S(\mathfrak h)) \cong
C^\bullet_{\mathrm{CE}}(\mathfrak h \ltimes \mathfrak h^\vee[1])$.

**Action items.**
- Insert this theorem **before** any PBW/Koszul-dual statement in the
  introduction. It is the central mathematical result.
- Author the **sign-convention appendix** (analysis item §11 / planning
  item below).
- In every place where the source convention currently reads
  "$f \mapsto O_f$ via the CE coordinate dual to $f$", replace by the
  $u_I \mapsto O_I$ / $c^I \mapsto \theta^I$ assignment.

### Theorem D — Principal-part / Matlis dual theorem
**Status.** Proved degreewise stable.
**Anchor.** `theorem-lanes.tex` Lane 4 (lines 150–207);
`appendix-matlis-principal-parts.tex`.

> **Theorem.** The continuous Taylor dual of $\mathfrak h$ is realized
> by the reduced Matlis local-cohomology module
> $$
> \mathfrak h^\vee_{\mathrm{cont}} \;\cong\; \mathcal P
> \;\;=\;\; H^2_{\mathfrak m}(\mathbb C[z_1,z_2])\,dz_1\,dz_2 \,\big/\, \mathbb C\,\rho_{0,0},
> \qquad \rho_{a,b} = z_1^{-a-1}z_2^{-b-1}\,dz_1\,dz_2,
> $$
> with residue pairing $\langle \rho_{a,b}, z_1^m z_2^n\rangle = \delta_{a,m}\delta_{b,n}$
> and coadjoint Hamiltonian action
> $$
> z_1^p z_2^q \cdot \rho_{a,b} \;=\; -(pb - qa + p - q)\,\rho_{a-p+1,\,b-q+1},
> $$
> with negative-index targets zero. The pairing is the unique
> continuous degree-preserving pairing satisfying coefficient
> extraction and Hamiltonian integration by parts after normalising
> $\langle \rho_{a,b}, z_1^a z_2^b\rangle = 1$.

**Proof skeleton.** (i) Čech model $H^2_{\mathfrak m}(R) = R[z_1^{-1},z_2^{-1}]
/ (R[z_1^{-1}] + R[z_2^{-1}])$; (ii) residue pairing as
contour-integral coefficient extraction; (iii) coadjoint action via
$\langle f \cdot \rho, g\rangle = -\langle \rho, \{f,g\}\rangle$ and
direct monomial calculation; (iv) uniqueness via local-cohomology
duality (replacing the older "Schur rigidity" sketch).

**Embedded no-go theorem (analysis item §42).**

> **Theorem (no polynomial coadjoint realization).** There is no
> $\mathfrak h$-module isomorphism from the polynomial one-$\psi$
> descendant module to the principal-part coadjoint module. *Proof.*
> $O_{1,0}, O_{0,1}$ act on polynomial observables by constant
> derivations $\partial_{\phi_2}, -\partial_{\phi_1}$, hence locally
> nilpotently. Principal-part action raises pole order indefinitely
> (e.g. $z_1 \cdot \rho_{a,b} = -(b{+}1)\rho_{a,b+1}$). Local
> nilpotence is preserved by module isomorphism. $\square$

**Action items.**
- Replace "Schur rigidity" prose by Matlis-dual / local-cohomology
  uniqueness throughout `appendix-matlis-principal-parts.tex` and
  main-body references.
- Add explicit derivation of $f \cdot \rho = -\mathcal L_{X_f}\rho$ Lie-derivative
  formulation with sign verification (analysis item §144).
- Reverse any prose that says "$z_1$ lowers principal-part indices" —
  the formula gives $z_1 \cdot \rho_{a,b} = -(b+1)\rho_{a,b+1}$ (raises
  $b$).

### Theorem E — Factorization-current theorem (de Rham / $\Omega^\bullet_c$)
**Status.** Proved degreewise stable.
**Anchor.** `theorem-lanes.tex` Lane 5 (lines 209–265);
`appendix-factorization-current-conventions.tex`.

> **Theorem.** Define on each interval $I \subset \mathbb R$
> $$\mathfrak h_I \;=\; \Omega^\bullet_c(I) \otimes \mathfrak h, \qquad
> \mathfrak g_I \;=\; \mathfrak h_I \ltimes \mathfrak h^\vee_I[1].$$
> Then there is a canonical isomorphism of locally constant
> factorization algebras
> $$
> C^\bullet_{\mathrm{CE}}(\mathfrak g_I) \;\cong\; \mathrm{PV}(S(\mathfrak h_I))
> \;\simeq\; Z^{P_0}_{\mathrm{fact}}(A_\partial)(I),
> \qquad u_{a(t)dt\otimes f} \mapsto B_f(a),\;\; c_\lambda \mapsto \theta_\lambda,
> $$
> where the smeared boundary current is
> $B_f(a) = \int_I a(t)\,\mathrm{Tr}\,f(\phi_1(t), \phi_2(t))\,dt$.

**Proof skeleton.** (i) The de Rham cosheaf $\Omega^\bullet_c$ has
top-degree compactly supported forms $a(t)\,dt$ realizing the
degree-zero current; (ii) the bracket $[\alpha\otimes f, \beta\otimes g]
= (\alpha\wedge\beta)\otimes\{f,g\}$ is local at coinciding supports;
(iii) extension by zero is the correct cosheaf operation, making
inclusions of intervals quasi-isomorphisms; (iv) interval CE/PV
diagram from Theorem C extends by Theorem C applied stalkwise plus
multiplicativity over disjoint intervals.

**Critical correction (highest-priority edit).** Replace **every**
statement of the form
$$(a \otimes f)^\vee[-1] \;\mapsto\; B_f(a)$$
by
$$u_{a(t)dt \otimes f} \;\mapsto\; B_f(a)$$
and split Theorem 0.2.21 into two parts:

- **Part 1 (Hamiltonian ghosts only).** $C^\bullet_{\mathrm{CE}}(\mathfrak h_I)
  \to \mathrm{PV}_{\mathrm{const}}(S(\mathfrak h_I))$, $c_\lambda \mapsto
  \theta_\lambda$. (No boundary functions.)
- **Part 2 (shifted cotangent extension).** $C^\bullet_{\mathrm{CE}}(\mathfrak g_I)
  \cong \mathrm{PV}(S(\mathfrak h_I))$, $u_x \mapsto O_x$. (Boundary
  functions appear as images of the cotangent CE coordinates.)

**Action items.**
- Globally replace $C_c^\infty(I) \otimes \mathfrak h$ by
  $\Omega^\bullet_c(I) \otimes \mathfrak h$ in factorization
  definitions; keep $C_c^\infty$ only at the degree-zero shadow.
- Add the **distribution-locality subsection** (analysis item §54): no
  product of two arbitrary distributions appears; only $aB$ where
  $a \in C_c^\infty$ and $B \in \mathcal D'_c$.

### Theorem F — Quantum degree-zero Moyal/Weyl theorem
**Status.** Proved in finite algebraic model; extension to all $N$
**conditional on the radial-parts theorem F$'$**.
**Anchor.** `theorem-lanes.tex` Lane 7 (lines 344–418);
`appendix-radial-parts-moyal.tex`; `scripts/check_moyal_coefficients.py`.

> **Theorem F (algebraic Moyal target).** In the reduced first-order
> open-line Weyl model, the boundary product is
> $F \star G = m \circ \exp(\tfrac\hbar 2 P_\partial)(F \otimes G)$,
> with $P^r$-coefficients verified to stated order against
> `check_moyal_coefficients.py`.

> **Theorem F$'$ (Radial–Moyal, *to be proved as standalone*).** Let
> $W_N = D_\hbar(\mathfrak{gl}_N)$, $I_N$ the quantum moment ideal for
> conjugation, $J_N(f) = \mathrm{Tr}\,\mathrm{Op}_W(f)(X,Y)$. Then in
> $N_{W_N}(I_N)/I_N$,
> $$\hbar^{-1}[J_N(f), J_N(g)] \;=\; J_N(\{f,g\}_\hbar) \quad \text{mod } [\bar c]\,,$$
> for all $f, g \in \mathbb C[z_1,z_2][[\hbar]]$, with $[\bar c]$ the
> distinguished scalar Capelli class.

**Proof obligations for F$'$.** (i) state the exact radial-parts
identity used ($\mathrm{Rad}_0(J_N(f)) = \Delta^{-1} S_N(f)\Delta$);
(ii) verify it applies to all Weyl-ordered mixed traces, not just
constant-coefficient invariant operators; (iii) compute and either
cancel or scalar-reduce Calogero–Moser/Dunkl correction terms; (iv)
verify injectivity of the radial map on the relevant subspace; (v)
verify connected single-trace projection commutes with the bracket;
(vi) prove finite-$N \to$ stable cumulant extraction preserves the
identity. Each is a separate lemma; they belong in
`appendix-radial-parts-moyal.tex`.

**Hard separation from Costello.** Theorem F is *internal to the
reduced first-order open-line Weyl model*. It is **not** the Costello
graph realization of Moyal coefficients, which remains open (see §4).

### Theorem G — Scalar $U(1)$/Capelli anomaly theorem
**Status.** Proved (existing `\thm:u1-center-anomaly` and
`\thm:quantum-classical-anomaly`).
**Anchor.** `main.tex` Theorems 318, 354, 412.

> **Theorem.** The classical cocycle
> $\bar\omega(z_1^k z_2^l, z_1^m z_2^n) = (kn - lm)\,\mathbf 1_{(k+m,l+n)=(1,1)}$
> defines the distinguished one-dimensional anomaly line $[\bar c] \in
> H^2_{\mathrm{Lie}}(\bar A; \mathbb C)$. Its boundary realization is
> $\{\mathrm{Tr}\,\phi_1, \mathrm{Tr}\,\phi_2\} = N$. Quantum
> mechanically, the same class appears as the Capelli/normal-ordering
> shift $YX - XY + \hbar N\,I = 0$, so
> $\mathrm{Tr}(AXY) - \mathrm{Tr}(AYX) = \hbar N\,\mathrm{Tr}(A)$
> mod the quantum moment ideal. The classical $\bar\omega$ and the
> quantum $\hbar N$ are the same distinguished line:
> $\mathrm{classical}\ \bar\omega \;\longleftrightarrow\; \mathrm{quantum}\ \hbar N$.

**Action items.**
- Sharpen the wording from "the one-dimensional sub-line of $H^2_{\mathrm{Lie}}$"
  to "the distinguished one-dimensional anomaly line" wherever the
  full $H^2$ is not classified.
- Clarify "scalar reduction" $\ne$ "removing the entire $U(1)$
  centre-of-mass sector": linear $\mathrm{Tr}\,\phi_i$ remain;
  $\mathrm{Tr}(1) = N$ as a primitive is removed.

---

## §4. Open obligations package — precisely formulated

The current `open-obligations.tex` enumerates these. The platonic
version sharpens each statement so each is a named problem with an
exact target, not a fuzzy aspiration.

**Obligation I — Unreduced BV factorization-centre lift.**
Construct, in the unreduced BV/factorization model (not the
post-contraction reduced model), a morphism
$\mathrm{Obs}^{\mathrm{cl,BV}}_{\mathrm{closed},H} \to
Z^{P_0}_{\mathrm{fact}}(\mathrm{Obs}^{\mathrm{cl,BV}}_{\mathrm{open},H})$
extending Theorem C and realizing the principal-part defect-current
sector $A^{\mathrm{pp}}_\partial = S(\mathfrak h_I) \otimes S(\mathcal P_I[1])$
as the strict centre with centrality homotopies against arbitrary open
observables.

**Obligation II — Rees / Fourier $D_\hbar$-module interpolation.**
Construct an $\hbar$-flat module $M_\hbar$ over the Rees Weyl algebra
$D_\hbar = \mathbb C\langle z_1, z_2, \hbar\partial_{z_1}, \hbar\partial_{z_2}\rangle/([\hbar\partial_{z_i}, z_j] = \hbar\delta_{ij})$
such that $M_\hbar/(\hbar) \cong \bar A_{\mathrm{desc}}$ as PBW symbol
module and $M_\hbar[\hbar^{-1}] \cong \mathcal P$ as coadjoint module.
The strict no-go theorem on $h$-module identification (Theorem D
embedded no-go) tells us this **must change category** — Rees /
holonomic $D_\hbar$-modules supported at the brane, not polynomial
modules. Replace every "interpolated by $\hbar$" sentence in the main
body by this conjectural statement.

**Obligation III — Regulator independence of weighted Tate.**
For exponential weights $q, q' > 1$, prove that the weighted
$(\mathfrak h^w, \mathfrak h^{\vee, w}_{\mathrm{cont}})$-pairs supply
canonically equivalent finite-degree local observables and that the
derived-centre map of Theorem C stabilises as $q \to 1^+$ on every
finite-degree window. This is the regulator-independence statement
that the weighted Tate construction needs to claim it solves any
problem about the **unweighted** original cotangent theory (rather
than merely defining a new analytic theory). Anchor:
`tate-T1`–`tate-T5` lanes and the strict-no-cy theorem already in
`open-obligations.tex` (line 118).

**Obligation IV — Mixed brane-defect QME anomaly cancellation.**
The classical centrality obstruction
$\{I_\partial(a,f), I_\partial(b,g)\}_{\mathrm{open}} = I_\partial(ab, \{f,g\}_{\bar A})
+ N\cdot\bar\omega(f,g)\int_{\mathbb R} a(t)b(t)\,dt$
and the quantum
$\mathrm{Tr}(AXY) - \mathrm{Tr}(AYX) = \hbar N\,\mathrm{Tr}(A)\ \mathrm{mod}\ \mathcal W_N$
must cancel against (a) closed exchange-graph contributions, (b)
supertrace mechanism (would require $\mathfrak{gl}(N|N)$ rather than
$\mathfrak{gl}_N$ — different model), or (c) central-character /
normal-ordering counterterm. State exactly which mechanism, prove the
cancellation, separate from Hadamard/Mittag-Leffler claims. Anchor:
`appendix-unreduced-bv-qme.tex`.

**Obligation V — Costello graph realization of Moyal coefficients.**
Prove that the renormalized BV observable product in this mixed
holomorphic-topological brane model gives exactly $m\circ\exp(\hbar P/2)$
by constructing: elliptic mixed bulk BV complex; brane-defect boundary
condition for $\mathbb R\times\{0\}$; gauge fixing; heat kernel and
propagator; bulk-to-defect kernel; counterterms solving QME; scalar
anomaly renormalization; connected-trace normalization; first graph
coefficient $1$; third graph coefficient $1/24$; all odd
$P^r$-coefficients matching Moyal. This is the analytic theorem.

**Obligation VI — Full higher-$\psi$ primitive Koszul homology.**
Determine the complete primitive stable Koszul homology of
$\mathbb C\langle x, y, \psi \rangle_{\mathrm{cyc}}$ with $Q\psi = [x,y]$,
including two-$\psi$ and higher-$\psi$ classes, and characterize the
sectors lying outside the Hamiltonian comparison.

**Obligation VII — Global descent.**
Globalize the formal-local main theorem to compact holomorphic
symplectic surfaces. Requires descent of local Hamiltonian sheaves and
choice of period class in $H^1(X, \mathbb C)$ obstruction; also ties
to Vol III when stated alongside CY$_3$ contexts.

---

## §5. Editorial reorganization

The current draft is structurally too dense at the front. The
platonic-ideal reorganization, in dependency order:

### Replacement table of contents

1. **Local measurements and constraints** — Diracian framing; three
   notions of locality; unitarity status. (Promotion of
   `principles.tex` content.)
2. **The Dirac brane probe** — Theorem A; explicit derivation of the
   open action from $\Omega_N$ and $\mu_\epsilon$.
3. **The closed Hamiltonian BF theory** — $\mathfrak h$, $\mathfrak g$,
   BF action and its CME.
4. **The CE/PV derived-centre theorem** — Theorem C, the central
   result, with both coordinate and coordinate-free proofs.
5. **Principal parts and defect-local cotangent currents** — Theorem D.
6. **Brane-line factorization** — Theorem E, with $\Omega^\bullet_c(I)$
   convention.
7. **PBW special-fibre descendants and the $\Psi_{a,b}$ shadow** —
   Theorem B and the embedded no-go.
8. **Scalar anomaly and Capelli shift** — Theorem G.
9. **Quantum Weyl/Moyal degree-zero theorem** — Theorem F (and the
   conditional F$'$).
10. **Weighted Tate regulator and analytic QME problem** — Lane 6 +
    Obligations III, IV.
11. **Open obligations** — Obligations I–VII, named problems.
12. **Appendices** — sign conventions; one-$\psi$ homology proof in
    full; Matlis local-cohomology details; radial-parts proof;
    finite-check reproducibility; Tate Quillen enhancement; Costello
    graph problem checklist.

The sections currently labelled "Cross-volume horizon", "Twisted
M-theory universality", and "BCOV/Kodaira-Spencer analogy" should be
demoted: the first goes to a private convention appendix, the second
becomes a "Conditional realization in admissible protected
twisted-M sectors" outlook section, the third becomes one paragraph of
motivation under "Hamiltonian BF theory for the formal symplectic
disk" as the primary terminology.

### Replacement abstract

Two paragraphs only. Physics paragraph (Dirac probe, BF closed sector,
$\mathbb R^2 \times \mathbb C^2$ near $\mathbb R \times \{0\}$, the
forced first-order action and BV constraint $Q\psi = [\phi_1, \phi_2]$).
Theorem paragraph (CE/PV derived-centre, cotangent CE coordinate ↦
boundary trace, Hamiltonian CE coordinate ↦ vector-field operation,
Matlis-dual realization of $\mathfrak h^\vee_{\mathrm{cont}}$, PBW
special-fibre shadow status of $\Psi_{a,b}$, scalar anomaly / Capelli
identification, Costello graph realization isolated as analytic
problem). Use precisely the language in §1.

### Title

Current title "Remarks on Mixed Holomorphic–Topological Strings"
under-claims and over-generalizes. The analysis converged on a longer
descriptive title; the platonic version is

> **Closed Hamiltonian BF Theory as the Derived Poisson Centre of a
> Dirac Brane Probe**

with subtitle

> *A formal local mixed holomorphic–topological model on $\mathbb R^2 \times \mathbb C^2$.*

### Voice and prose discipline

Russian-school + Diracian-physical: brackets, observables, locality
first. Avoid "we hope", "morally", "essentially", "groundbreaking",
"advances human knowledge". Let theorem names carry the ambition.
Avoid "string theory" decoration in theorem titles; use "Hamiltonian
BF brane model". Preserve every honest epistemic disclaimer; no rhetoric
in their place.

---

## §6. Surgical correction list (highest priority)

These are the edits whose absence currently lets the manuscript leak
old confusions despite the apparatus already encoding the right
distinctions. Order is dependency-respecting; each item names the file
and the substitution.

1. **Source convention in interval factorization** — `main.tex`
   Theorem 0.2.21 and every related interval statement: replace
   $(a \otimes f)^\vee[-1] \mapsto B_f(a)$ by $u_{a(t)dt \otimes f}
   \mapsto B_f(a)$, and add the companion $c_\lambda \mapsto
   \theta_\lambda$.
2. **De Rham factorization source** — globally replace
   $C_c^\infty(I) \otimes \mathfrak h$ by $\Omega^\bullet_c(I) \otimes
   \mathfrak h$ in factorization definitions; keep $C_c^\infty$ for
   the top-degree shadow only.
3. **Delete the $\Psi \leftrightarrow \rho$ "same module" sentence** —
   wherever $\Psi_{a,b}$ and $\rho_{a,b}$ are described as "two bases
   of the same $\mathfrak g$-module / interpolated by $\hbar$",
   replace by "two distinct realizations of the same PBW label set;
   $\bar A_{\mathrm{desc}} \cong \mathfrak h^\vee_{\mathrm{cont}}$ as
   graded vector spaces, not as $\mathfrak h$-modules". Cross-link to
   the embedded no-go theorem in Theorem D.
4. **Add the no-go lemma as a numbered lemma**, not an aside.
5. **Replace "Schur rigidity"** in
   `appendix-matlis-principal-parts.tex` and main-body uses by the
   Matlis local-cohomology / residue-pairing uniqueness statement.
6. **Rename the "primitive projection theorem"** —
   `tate-T5-chain-level-primitive.tex` and references — call it the
   *primitive indecomposable $P_0$-shadow*, not a *factorization
   algebra equivalence*. State explicitly $\pi_{\mathrm{prim}}(XY)=0$
   for positive primitive $X,Y$.
7. **Recast the principal-part boundary sector** as an *enlarged
   reduced defect-current model*, not as derived from polynomial
   observables. State: "The principal-part sector is not obtained
   from ordinary polynomial matrix observables. It is adjoined as
   the reduced local-dual defect-current module forced by the
   coadjoint action."
8. **Sign-convention appendix.** Author Appendix A: define $V[1]^n$
   convention; CE differential signs $d_{\mathrm{CE}} c^K$,
   $d_{\mathrm{CE}} u_K$; verify $d^2_{\mathrm{CE}} u_K = 0$ via
   coadjoint Jacobi; Schouten bracket convention $[\theta^I, O_J] =
   \delta^I_J$; $d_\pi = [\pi, -]$ formulas; sign-checklist
   $\Phi(d_{\mathrm{CE}} c^K) = d_\pi \Phi(c^K)$,
   $\Phi(d_{\mathrm{CE}} u_K) = d_\pi \Phi(u_K)$; sign of
   Hamiltonian vector field $X_{z_1} = \partial_{z_2}$, $X_{z_2} =
   -\partial_{z_1}$; principal-part action sign verification
   $f \cdot \rho = -\mathcal L_{X_f}\rho$ and the explicit derivation
   $z_1 \cdot \rho_{a,b} = -(b{+}1)\rho_{a,b+1}$, $z_2 \cdot \rho_{a,b}
   = (a{+}1)\rho_{a+1,b}$.
9. **Claim-strength ledger near the abstract.** Promote the existing
   `claim-strength-ledger.tex` table into a visible block right after
   the abstract: every status line of the form "proved in finite
   algebraic model / proved degreewise stable / conditional / open /
   not asserted" against named theorems.
10. **Cross-volume material out of main paper.** Move "Cross-volume
    horizon" and convention transfers to a private appendix
    (`appendix-cross-volume-private.tex` not bundled in `\input`s)
    or the `reconstitution/` directory. Keep one paragraph in the main
    text: "No compact CY$_3$, Igusa, Borcherds, BKM, K3$\times$E, or
    Vol III claim is used in this paper. Any such transfer requires a
    separate matched-conventions proof." Anchor:
    `claim-strength-ledger.tex` lines 131–139.
11. **Citation cleanup.** Audit all `\cite{...}` for malformed labels
    (e.g. `[13]razmyslov`, `[2]tsygan`); ensure Loday–Vallette /
    Priddy / Loday–Quillen / Tsygan / Hinich / Berger–Moerdijk /
    Lefèvre-Hasegawa / Costello / Costello–Gwilliam / Gwilliam–Williams
    keys exist and resolve; insert a precise citation for the
    $P_0$-centre = Poisson cochains identification (Calaque–Pantev–
    Toën–Vaquié–Vezzosi or Costello–Gwilliam) where currently it is
    folklore.
12. **Notation index.** Add a one-page notation index reproducing the
    `local-dictionary.tex` table verbatim near the introduction (or
    front matter), with the explicit separation rule and the
    cotangent-objects table (cf. analysis item §7):
    | Object | Lives where | Action | Status |
    |--------|-------------|--------|--------|
    | $u_I$ | $C^\bullet_{\mathrm{CE}}(\mathfrak h \ltimes \mathfrak h^\vee[1])$ | $d_{\mathrm{CE}} u_K = C^L_{KJ} u_L c^J$ | closed CE cotangent coordinate |
    | $O_I$ | $\mathrm{PV}(S(\mathfrak h))$ | $d_\pi O_K = C^L_{KJ} O_L \theta^J$ | boundary Hamiltonian function |
    | $\Psi_{a,b}$ | stable open Koszul homology | symmetric PBW action | PBW special-fibre shadow |
    | $\rho_{a,b}$ | $\mathfrak h^\vee_{\mathrm{cont}}$ | $\mathrm{ad}^\vee$ | closed cotangent coadjoint mode |
    | $\Theta_\rho$ | $A^{\mathrm{pp}}_\partial$ | $\{B_f, \Theta_\rho\} = \Theta_{f\cdot\rho}$ | reduced distributional boundary current |

---

## §7. New constructions to author

These are the constructions the analysis identifies as missing or
under-proved, ordered by mathematical value.

**(N1) The CE/PV theorem as a self-contained section.** Even though
Lane 3 already covers it in `theorem-lanes.tex`, the *main body* of
`main.tex` should contain a 6–10 page section that states Theorem C,
gives both the coordinate-level and the coordinate-free (Lichnerowicz)
proofs, includes the toy finite-dimensional warm-up
$C^\bullet_{\mathrm{CE}}(\mathfrak l \ltimes \mathfrak l^\vee[1]) \cong
\mathrm{PV}(S(\mathfrak l))$ for finite Lie $\mathfrak l$ (analysis
item §156), and ends with the moment-map shadow corollary. This is the
section that earns the paper its main contribution.

**(N2) Strengthened one-$\psi$ homology proof.** The chip-moving /
Abel-map argument needs to become a fully formal calculation: explicit
$C_2(k,l) \to C_1(k,l) \to C_0(k,l)$, sign lemma for the two-$\psi$
boundary, cellular-chain identification with the two-skeleton of
$Y_{k,l}$, attaching-cells argument for $H_1$ stability, Abel-map
cyclic-relabelling well-definedness, stabilizer-quotient
contractibility, $S^1$-cycle identification of $\Psi_{k,l}$. The
existing `scripts/check_one_psi_homology.py` provides finite checks but
not a proof. Author this in a dedicated appendix.

**(N3) Standalone Radial–Moyal theorem.** Theorem F$'$ deserves a
self-contained appendix (`appendix-radial-parts-moyal.tex` is the
locus). State the exact radial-parts identity invoked; argue
applicability to all Weyl-ordered mixed traces; identify and either
cancel or scalar-reduce Calogero–Moser/Dunkl correction terms; verify
radial-map injectivity; commute connected-trace projection with the
bracket; verify finite-$N \to$ stable cumulant extraction. Each step
is a numbered lemma. Without this, F$'$ is a black box.

**(N4) The unreduced BV cotangent factorization-centre construction.**
Obligation I, written as a formal target with named sub-problems:
de Rham/Dolbeault closed BF fields with compact support; defect
boundary condition; centrality homotopies against arbitrary open
observables; functoriality under interval inclusions; principal-part
defect currents as primary boundary modes (not derived from
polynomials).

**(N5) The Rees / Fourier $D_\hbar$-module construction.**
Obligation II: write the candidate $M_\hbar = D_\hbar / D_\hbar(z_1, z_2)$
or its holomorphic local-cohomology realization; identify the
specializations $M_\hbar/(\hbar) \cong \bar A_{\mathrm{desc}}$ and
$M_\hbar[\hbar^{-1}] \cong \mathcal P$; verify the action; replace
the "Rees parameter $\hbar$ interpolates $\Psi$ and $\rho$" wording
throughout the main body with reference to this conjectural
construction.

**(N6) Regulator-independence theorem.** Obligation III: prove that
the derived-centre map of Theorem C and all finite-degree observables
stabilize as $q \to 1^+$, or that any two exponential weights $q, q'>1$
give canonically equivalent finite-degree local observables. This
makes the weighted Tate construction a regulator (rather than a
different theory).

**(N7) Mixed brane-defect QME theorem.** Obligation IV: identify the
mechanism (closed exchange graph, supertrace, central-character) and
prove the anomaly cancellation. Authoring locus:
`appendix-unreduced-bv-qme.tex`.

**(N8) Costello graph realization checklist as a boxed problem.**
Obligation V: a single theorem statement that says "if the
following twelve constructions can be carried out (elliptic complex,
defect boundary condition, gauge fixing, heat kernel, propagator,
bulk-to-defect kernel, renormalization scheme, counterterms solving
QME, scalar anomaly renormalization, connected-trace normalization,
first graph coefficient = 1, third graph coefficient = $1/24$), then
the renormalized BV observable product gives exactly the Moyal
product." Author as a self-contained boxed problem in the analytic
chapter.

**(N9) Distribution-locality subsection.** In Theorem E and the
factorization current sections, author the explicit explanation:
$aB$ for $a \in C_c^\infty(I)$ and $B \in \mathcal D'_c(I)$; the
bracket $\{B_f(a), \Theta_\rho(B)\} = \Theta_{f\cdot\rho}(aB)$;
$\{\Theta_\rho, \Theta_\sigma\} = 0$ avoids distribution products.
This neutralizes the distribution-product objection.

**(N10) Three-large-$N$ disambiguation subsection.** Per analysis item
§23: define separately
- $\mathrm{Prim}_{\mathrm{st}}$ (degreewise invariant stabilization, $N \ge d$);
- $\mathrm{Conn}_{N\to\infty}$ (primitive single-trace extraction);
- Hamiltonian scalar quotient (omit empty trace as primitive).

These are not the same operation. Author as a one-page subsection
near Theorem B.

**(N11) Coordinate-free closed-open synthesis section.** Write the
short physics-prose section (3–4 pages) that states: in the linear
Poisson algebra $A_\partial = S(\mathfrak h)$, the derived centre is
$Z^{P_0}(A_\partial) \simeq \mathrm{PV}(A_\partial)$; functions
correspond to cotangent CE coordinates ($u_I \mapsto O_I$); vector
fields correspond to Hamiltonian CE coordinates ($c^I \mapsto
\theta^I$); $d_\pi O_f = X_{O_f}$ (the Hamiltonian vector field) is
exactly $\Phi(d_{\mathrm{CE}} u_f)$; ordinary Hochschild centrality of
$O_f$ is tautological in graded-commutative reduced models, but the
non-trivial statement is *Poisson centrality*. This is the conceptual
explanation of why the boundary trace is the image of the *cotangent*
generator, not the Hamiltonian generator.

---

## §8. Sequencing and dependencies

The work is mostly orthogonal across pillars; here is a build order.

**Phase 1 — Foundational alignment (one week, surgical edits only).**
1. (S6.1) Source convention $u_{a\otimes f} \mapsto B_f(a)$ globally
   in `main.tex` and lane files. Verify against
   `appendix-factorization-current-conventions.tex`.
2. (S6.2) $\Omega^\bullet_c$ replacing $C_c^\infty$.
3. (S6.3, S6.4) Delete "same module" wording; install no-go lemma.
4. (S6.5) "Schur rigidity" → Matlis local-cohomology uniqueness.
5. (S6.6) Rename primitive projection.
6. (S6.7) Recast principal-part sector as enlarged reduced defect.
7. (S6.10) Cross-volume out of main paper.
8. (S6.11) Citation audit.
9. (S6.12) Notation index.

After Phase 1 the manuscript is internally consistent.

**Phase 2 — Theorem-block reorganization (two weeks).**
10. (S5) Replacement table of contents.
11. (N1) CE/PV section in main body; promote Theorem C to centre stage.
12. (S6.8) Sign-convention appendix.
13. (S6.9) Claim-strength ledger near abstract.
14. Replacement abstract; replacement title.
15. (N10) Three-large-$N$ subsection.
16. (N11) Coordinate-free closed-open synthesis section.

After Phase 2 the manuscript reads as the platonic-ideal paper for the
proved core (Theorems A, B, C, D, E, F, G).

**Phase 3 — Strengthening proved theorems (two-three weeks).**
17. (N2) Full one-$\psi$ homology proof.
18. (N3) Standalone Radial–Moyal theorem F$'$.
19. (N9) Distribution-locality subsection in Theorem E.

After Phase 3 every proved theorem is armored against hostile referee
attack.

**Phase 4 — Open-obligations programme (research, six months — one year).**
20. (N4) Unreduced BV factorization-centre construction.
21. (N5) Rees / $D_\hbar$-module interpolation.
22. (N6) Regulator-independence theorem.
23. (N7) Mixed brane-defect QME cancellation.
24. (N8) Costello graph realization.

These are research problems, not editorial ones. Each could become its
own paper.

**Concurrent cross-repo coordination.** Phases 1–3 do not require any
cross-volume movement. Phase 4 items (N6, N7, N8) feed into Vol III
(`~/calabi-yau-quantum-groups`) and the Igusa programme
(`~/igusa-cusp-form`) only after matched-conventions proofs in those
repos.

---

## §9. Cross-volume coordination

The repo-local `CLAUDE.md` is unambiguous: BCOV/Kodaira-Spencer
gravity supplies physics motivation and convention-checking interface
for the Vol III CY-to-chiral frontier; treat as context unless a local
theorem states and proves a precise comparison; conventions ($d =
\dim_{\mathbb C} X$, worldsheet $\Sigma$, framing datum on $S^3$) must
agree with Vol III when stated in both; any divergence is load-bearing.

The platonic-ideal version of this paper makes **no cross-volume
claim** in the main body. Vol III, Igusa $\Delta_5$, BKM/Borcherds,
K3$\times$E, sister-volume transfers are all listed only in a
private/programmatic appendix. This is the strongest possible
position: the local theorem is genuinely standalone; cross-volume
transfers happen elsewhere via separately matched-conventions proofs
(Obligation VII enables this for compact CY$_3$ globalizations).

What the paper *does* announce in one paragraph at the end of the
introduction:

> The local Hamiltonian BF model studied here is a natural source for
> generating-function and modularity questions in topological-string
> theory and the BKM/Borcherds programme. Comparison with the Igusa
> cusp-form $\Delta_5$ construction in `~/igusa-cusp-form` and with the
> Vol III CY-to-chiral frontier in `~/calabi-yau-quantum-groups` is a
> heuristic and convention-checking bridge here, not a consequence of
> the local Hamiltonian BF/Moyal calculation.

The intelligence-propagation rule from `~/ecosystem/INVARIANTS.md`
applies in the other direction: insights from this paper (Theorem C,
the Matlis-dual realization, the $\rho_{0,0} \leftrightarrow N$
identification) are propagated to those repos as motivation, not as
imported theorems.

---

## §10. What success looks like

The platonic-ideal paper, when finished, has these visible
characteristics.

**Structural.** The body is organized around six numbered theorem
blocks (A–F, plus the anomaly G) with explicit status lines from the
claim-strength ledger. The lane decomposition is visible; the
obligations list is named and precise. Cross-volume material is
absent from the body.

**Mathematical.** Theorem C — the CE/PV derived-centre isomorphism —
is the central mathematical contribution, with both coordinate-level
and coordinate-free proofs and a finite-dimensional toy warm-up. The
Matlis-dual / local-cohomology realization of $\mathfrak h^\vee_{\mathrm{cont}}$
makes the cotangent direction physically natural (residue currents at
the brane defect). The PBW special-fibre shadow status of the
polynomial $\Psi_{a,b}$ descendants is unambiguous, with the embedded
no-go theorem ruling out any ordinary $\mathfrak h$-module
intertwiner. The de Rham factorization construction is built on
$\Omega^\bullet_c(I) \otimes \mathfrak h$ throughout, with
distribution-locality discipline. Every bracket identity carries the
scalar-reduction caveat; the $U(1)$/Capelli class is the same line
classically and quantum-mechanically.

**Physical.** The first sections speak Diracian: brackets, observables,
locality before strings. Three notions of locality (support,
topological, distributional-holomorphic) are derived from the
$Q$-exact translation arguments. Unitarity is replaced by
CME/QME plus factorization associativity, with explicit acknowledgment
that this is a protected cohomological sector. The Witten centrality
principle makes the factorization algebra inevitable rather than
imposed.

**Epistemic.** Every conditional theorem is named conditional. Every
open obligation is precisely formulated. The radial-parts theorem is
either fully armored as F$'$ or explicitly conditional. The Costello
graph realization is a checklist, not a sketch. The cross-volume
exclusions are explicit.

**Voice.** Russian-school / mathematical-physics frontier; named
attribution (Bershadsky–Cecotti–Ooguri–Vafa 1993, Witten 1988, Costello
2011, Polyakov 1987, Grothendieck residues, Matlis duality, Procesi–
Razmyslov stable invariants, Loday–Quillen / Tsygan cyclic homology
templates). No em-dashes; no "groundbreaking"; theorem names carry the
ambition.

---

## Appendix to this plan — the highest-priority edits in compact form

If only ten edits are made, make these.

1. Replace $(a \otimes f)^\vee[-1] \mapsto B_f(a)$ by $u_{a(t)dt \otimes f}
   \mapsto B_f(a)$ globally.
2. Replace $C_c^\infty(I)$ by $\Omega^\bullet_c(I)$ in factorization
   definitions.
3. Delete every "same $\mathfrak g$-module / interpolated by $\hbar$"
   sentence about $\Psi_{a,b}$ vs $\rho_{a,b}$.
4. Insert the embedded no-go lemma as a numbered lemma in Theorem D.
5. Replace "Schur rigidity" with Matlis local-cohomology / residue-pairing
   uniqueness.
6. Rename the primitive projection theorem to *primitive
   indecomposable $P_0$-shadow*.
7. Recast $A^{\mathrm{pp}}_\partial$ as an enlarged reduced
   defect-current model.
8. Author the sign-convention appendix with $d^2_{\mathrm{CE}} u_K = 0$
   and the $\Phi$-compatibility checklist.
9. Promote the claim-strength ledger to a visible block right after
   the abstract.
10. Move cross-volume material out of the main body.

Everything else is downstream of these.

---

## Provenance

Synthesized from five rounds of critical analysis across 176 PDF
pages: hostile-referee attack (pp. 1–11), constructive derived-centre
proposal (pp. 12–22), Diracian first-principles rewrite (pp. 23–71),
second-pass critique of v3 draft (pp. 72–91), exhaustive 201-item
technical punch list (pp. 91–176). Cross-referenced against
`abstract.tex`, `theorem-lanes.tex`, `claim-strength-ledger.tex`,
`open-obligations.tex`, `principles.tex`, `local-dictionary.tex`,
`main.tex` headers and prose, and the appendix files.

The current manuscript apparatus already encodes the right
distinctions; the surgical work in §6 propagates them through every
theorem statement and prose paragraph. The new constructions in §7
realize the platonic ideal. The open obligations in §4 are the next
research horizon.
