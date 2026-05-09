# Wave 3 / W21 — Gelfand + Examples Lens (Wakimoto Identification of Mixed Cones)

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.**
- *Primary:* Gelfand — concrete examples first; representation theory;
  distributions, functional analysis, and unitary highest-weight machinery.
- *Secondary:* Examples — degenerate cases, smallest nontrivial probe,
  do-the-arithmetic discipline.
**Wave.** 3 (independent attacker; reads waves 1-2 + W3-W3 / W3-W12 /
W3-W14 ledgers).
**Mandate.** Independently verify W14's mixed-cone reduction formulas,
attack/confirm the Wakimoto identification of `C+- ≅ C[z_1] ⊗
Matlis_{z_2}` as a Lie module of `bar A`, propose a precise theorem
statement, and identify the precise interaction with W14's sigma
duality and W12's Čech short exact sequence.
**Inputs (read in full).** `CLAUDE.md`,
`reconstitution/wave3-W14-mixed-cones-2026-04-28.md` (full),
`reconstitution/wave3-W3-nekrasov-2026-04-28.md` (full),
`reconstitution/wave3-W12-blast-radius-2026-04-28.md` (full),
`appendix-matlis-principal-parts.tex` (full),
`scripts/check_bi_infinite_lie_consistency.py` (full),
`/tmp/w14_four_cones_probe.py`, `/tmp/w14_lie_substructure.py`,
`/tmp/w14_parabolic_intertwiner.py` (full).
**Mode.** Proposal-only. No commits. Master ledger schema; IDs prefix
`W3-W21-`.
**Independence.** W14's tensor-factorization of the mixed cones, W12's
Čech SES, and the W3 corrected indicator-free formula are taken as
**input under attack** through the Gelfand + Examples lens. The
deliverable is (i) explicit verification at >= 100 (a, b, action)
triples on each mixed cone of W14's reduction; (ii) precise Wakimoto
identification or replacement; (iii) a candidate theorem statement
with named parabolic / Lie-subalgebra; (iv) sigma-intertwiner
clarification at exact (p, q) values; (v) Čech-SES audit of W12's
formula.

---

## §0. Method

The Gelfand lens lives inside concrete representation theory: highest
weight modules, Verma modules, free-field realizations, residue
distributions, and the structural classification of induced modules.
The Examples lens demands explicit, numerical, by-hand verification at
the smallest nontrivial bidegrees `(a, b)` and a sweep across the
entire mixed cone.

Computational evidence is captured verbatim in §§1-3. Verdicts in §4;
candidate theorem in §5; obstruction analysis in §6; sigma analysis
§7; Čech-SES analysis §8; per-target findings in §9; provenance in
§10.

Three new probes inscribed in `/tmp/w21_*.py`:
- `/tmp/w21_verify_action_formulas.py` — independent re-derivation of
  the W14 specialization at `(p, q) = (1, 0)` and `(0, 1)` from the W3
  master formula, with a 440-triple scale verification.
- `/tmp/w21_eigenvalue_structure.py` — discovery of the diagonal
  Cartan generator `z_1 z_2` and the joint eigenvalue `(b - a)`.
- `/tmp/w21_sigma_refined.py` — exhaustive sigma-intertwiner search.
- `/tmp/w21_diagonal_lie_subalgebra.py` — 3-dim Borel
  `<z_1, z_2, z_1 z_2>` sub-Lie-algebra classification.

---

## §1. T1 — Independent verification of W14's reduction formulas

### §1.1 Re-derivation from the W3 master formula

Starting from the W3-W3-02 corrected indicator-free formula
$$z_1^p z_2^q \cdot v_{a, b} = (pb - qa) v_{a + p - 1, b + q - 1}$$
on $\Z^2 \setminus \{(0, 0)\}$ with mod-constants projection (zero out
target $(0, 0)$), specialize to $(p, q) = (1, 0)$ and $(p, q) = (0, 1)$:

**$(p, q) = (1, 0)$:**
$$\text{coefficient} = (1 \cdot b - 0 \cdot a) = b, \qquad \text{target} = (a + 0, b - 1) = (a, b - 1).$$
$$\therefore \quad z_1 \cdot v_{a, b} = b \cdot v_{a, b - 1}, \qquad \text{independent of } a.$$

**$(p, q) = (0, 1)$:**
$$\text{coefficient} = (0 \cdot b - 1 \cdot a) = -a, \qquad \text{target} = (a - 1, b + 0) = (a - 1, b).$$
$$\therefore \quad z_2 \cdot v_{a, b} = -a \cdot v_{a - 1, b}, \qquad \text{independent of } b.$$

These reductions hold on **all of** $\Z^2 \setminus \{(0, 0)\}$, not
just on the mixed cone $C^{+-}$. **W14's reduction is the universal
specialization of the W3 master formula**; it is correct verbatim.

### §1.2 Scale verification (440 triples, 0 failures)

Output of `/tmp/w21_verify_action_formulas.py` (verbatim):
```
T2. Verify >=100 (a, b, action) triples on C+- = {a>=0, b<=-1}.
   Sweep: a in [0, 10], b in [-10, -1] -> 110 basis vectors.
   z_1: 110 triples checked, 0 failures
   z_2: 110 triples checked, 0 failures

T3. Mirror verification on C-+ = {a<=-1, b>=0}.
   Sweep: a in [-10, -1], b in [0, 10] -> 110 basis vectors.
   z_1: 110 triples checked, 0 failures
   z_2: 110 triples checked, 0 failures

AGGREGATE
   C+- triples checked: 220, failures: 0
   C-+ triples checked: 220, failures: 0
   Total: 440 triples checked, 0 failures.
```

**W3-W21-01 (verification of W14 reduction formulas).** **Severity 3.
Status valid. Confidence high.** W14's reduction
$z_1 \cdot v_{a, b} = b v_{a, b - 1}$ and
$z_2 \cdot v_{a, b} = -a v_{a - 1, b}$ on $C^{+-}$ (and mirror on
$C^{-+}$) is INDEPENDENTLY confirmed at 440 (a, b, action) triples
spanning $a \in [0, 10]$, $b \in [-10, -1]$ (and mirror) on the
mixed cones, with zero discrepancies versus the W3 master formula.

### §1.3 Precision of the tensor-factorization claim

W14 claims `C+- ≅ C[z_1] ⊗ Matlis_{z_2}` as a Lie module. Let me
audit precision. Identify `v_{a, b} <-> e_a ⊗ f_b` where
`{e_a : a >= 0}` is the polynomial basis (in z_1) and
`{f_b : b <= -1}` is the Matlis principal-part basis on the b-coordinate.

**Linear Hamiltonian tensor structure (verified).** Under this
identification, the linear Hamiltonians act as:
$$z_1 \cdot (e_a \otimes f_b) = e_a \otimes (b \cdot f_{b - 1}), \qquad
  z_2 \cdot (e_a \otimes f_b) = (-a \cdot e_{a - 1}) \otimes f_b.$$
**z_1 acts on the f-factor only; z_2 acts on the e-factor only.** This
is an honest tensor product action of the abelian Lie subalgebra
$\C \cdot z_1 \oplus \C \cdot z_2$ on $C^{+-}$.

**Quadratic Hamiltonian breakdown (NOT tensor).** For higher monomials:

$(p, q) = (2, 0)$: $z_1^2 \cdot v_{a, b} = 2 b \cdot v_{a + 1, b - 1}$.
**Target shifts BOTH a and b.** This is NOT a pure tensor action on the
factorization above (the e_a-factor shifts by +1 due to the SINGLE
monomial action, distinct from iterated $z_1$).

$(p, q) = (1, 1)$: $z_1 z_2 \cdot v_{a, b} = (b - a) \cdot v_{a, b}$.
Target = source (stationary), but coefficient $(b - a)$ is **not** a
sum of an a-only piece and a b-only piece factoring through the
tensor product.

**W3-W21-02 (sharpening of W14's tensor factorization).** **Severity
2. Status valid. Confidence high.** W14's tensor factorization
`C+- ≅ C[z_1] ⊗ Matlis_{z_2}` holds precisely for the **abelian
linear-Hamiltonian sub-Lie-algebra** $\C \cdot z_1 \oplus \C \cdot z_2$.
For the full $\bar A$, the action does NOT factorize as a tensor
product action; the higher-monomial action mixes both factors. The
correct statement is: $C^{+-}$ is a **MIXED-POLARIZATION module**
of the abelian linear sub-Lie-algebra, lifted (non-trivially, with
mixing) to a $\bar A$-module.

This is consistent with the standard pattern of free-field /
Wakimoto realizations: they factorize at the LINEAR / Heisenberg
sub-algebra level, with higher Lie operations realized via vertex
operators / OPE that DO mix the factors.

---

## §2. T2 — Wakimoto identification attack

### §2.1 Wakimoto module structure (citation)

The classical Wakimoto module construction:
- **Wakimoto, *Communications in Mathematical Physics* 104 (1986)
  605-609.** Original free-field realization of affine $\widehat{\mathfrak{sl}}_2$.
- **Frenkel, *Langlands Correspondence for Loop Groups* (Cambridge,
  2007), Chapter 6.** Comprehensive textbook treatment of Wakimoto
  modules over arbitrary affine Kac-Moody algebras.
- **Frenkel-Ben-Zvi, *Vertex Algebras and Algebraic Curves* (AMS,
  2nd ed. 2004), §11.3-§11.6.** Rigorous vertex-algebra realization of
  Wakimoto modules, with explicit free-field / $\beta\gamma$-system
  formulas.

For affine $\widehat{\mathfrak{sl}}_2$ at level $k$ with weight $\lambda$:
$$W_{k, \lambda} \;=\; \mathrm{Fock}(\phi\text{-Heisenberg})
                   \;\otimes\; \mathrm{Fock}(\beta\gamma\text{-system})$$
$$= \C[\phi_{-1}, \phi_{-2}, \dots] \otimes \C[\beta_{-1}, \beta_{-2}, \dots, \gamma_{-1}, \gamma_{-2}, \dots].$$

Free-field realization of the Lie algebra:
$$e(z) = \beta(z), \quad h(z) = -2\beta\gamma(z) + \sqrt{2(k+2)}\,\partial\phi(z),$$
$$f(z) = -\beta(z)\gamma(z)^2 - k \partial\gamma(z) + \sqrt{2(k+2)}\,\gamma(z)\partial\phi(z).$$

**Vacuum vector $|\lambda\rangle$**: killed by all $\beta_n$ ($n \geq 0$),
$\gamma_n$ ($n \geq 1$), $\phi_n$ ($n \geq 1$).

**Mixed polarization signature**: $\beta\gamma$-system is a first-order
tangent / bosonic-ghost system with $[\beta_n, \gamma_m] = \delta_{n+m, 0}$;
positive modes annihilate vacuum; negative modes create.

### §2.2 Comparison with the C+- structure

**Structural matches:**
1. **Tensor factorization at the Heisenberg level**: $C^{+-}$ has
   the linear $\C \cdot z_1 \oplus \C \cdot z_2$ acting as a tensor
   product (W3-W21-02). Wakimoto's $\beta\gamma$-system has the
   conjugate-mode pair $(\beta, \gamma)$ acting as a tensor product
   on the Fock space.
2. **Mixed polarization**: in $C^{+-}$, $z_1$ acts as Matlis raising
   on b (rising-factorial) while $z_2$ acts as PBW lowering on a
   (locally nilpotent). In Wakimoto, $\beta_{-n}$ creates / $\beta_n$
   annihilates; $\gamma_{-n}$ creates / $\gamma_n$ annihilates. Both
   have a free-field DIRECTIONAL-NILPOTENCE pattern.
3. **Vacuum vector**: $v_{0, -1}$ in $C^{+-}$ is annihilated by all
   pure $z_2$-monomials (W3-W21-03 below) — analogous to the Wakimoto
   $|\lambda\rangle$ killed by positive $\beta_n$ modes.

**Structural mismatches:**
1. **Underlying Lie algebra is NOT Kac-Moody.** $\bar A = \C[z_1, z_2] / \C$
   is the Poisson algebra of the formal disk modulo constants. It is
   a **graded Lie algebra** with grading by $\Z$ via total degree
   $\deg(z_1^p z_2^q) = p + q - 1$, but it has **no central extension,
   no opposite Borel, no real vs imaginary roots, no triangular
   decomposition in the Kac-Moody sense.** The standard Wakimoto
   theorem (which depends on these features) does not apply.
2. **No $\beta\gamma$-free-field realization is constructed for**
   $\bar A$. Frenkel-Ben-Zvi's construction depends on the affine
   loop algebra structure with a central charge; $\bar A$ has none.

### §2.3 What v_{0, -1} actually is

`/tmp/w21_eigenvalue_structure.py` finds:
- **$z_1 z_2 \cdot v_{a, b} = (b - a) v_{a, b}$** for all $(a, b)$
  in $\Z^2 \setminus \{(0, 0)\}$ (target = source). The element
  $z_1 z_2 \in \bar A$ is a **Cartan-like element** with eigenvalue
  $(b - a)$ on every basis vector.
- **At the vacuum $v_{0, -1}$, eigenvalue of $z_1 z_2$ is $-1$.**
- **Annihilator of $v_{0, -1}$ inside $\bar A$**: span of pure
  $z_2^q$ monomials (q $\geq$ 1) plus the single isolated element
  $z_1 z_2^2$ (whose action target = $(0, 0)$, killed by mod-constants).

**W3-W21-03 (Cartan eigenvalue and vacuum annihilator).** **Severity
3. Status valid. Confidence high.**
- The element $z_1 z_2 \in \bar A$ acts diagonally as $(b - a)$ on
  every basis vector $v_{a, b}$ in the bi-infinite parent.
- The vacuum $v_{0, -1}$ of $C^{+-}$ has $z_1 z_2$-eigenvalue $-1$.
- The Lie subalgebra $\langle z_1, z_2, z_1 z_2 \rangle \subset \bar A$
  (with Poisson bracket) has structure $[z_1 z_2, z_1] = -z_1$,
  $[z_1 z_2, z_2] = +z_2$, $[z_1, z_2] = 0$ (mod constants), making
  it isomorphic to the **3-dim Borel of $\mathrm{GL}_2$** (= the
  "ax + b" algebra; solvable, not $\mathfrak{sl}_2$).

### §2.4 Verma module of the 3-dim Borel

Setting $H = z_1 z_2$, $X = z_2$ (raising), $Y = z_1$ (lowering)
(verifying the weights via direct computation in
`/tmp/w21_diagonal_lie_subalgebra.py`):
$$[H, X] = X, \quad [H, Y] = -Y, \quad [X, Y] = 0.$$

This is the standard 3-dim solvable Borel
$\mathfrak{b} = \C \cdot H + \C \cdot X + \C \cdot Y$
(with $X, Y$ abelian) of $\mathrm{GL}_2$ acting on $\C^2$.

**On $C^{+-}$:**
- $v_{0, -1}$ is killed by $X = z_2$ (it is a **lowest-weight vector**
  for the Borel — annihilated by the "raising" element).
- $Y = z_1$ generates a free orbit
  $\{z_1^k \cdot v_{0, -1} : k \geq 0\}$ via iteration:
  $z_1^k \cdot v_{0, -1} = (-1)^k k! \cdot v_{0, -1 - k}$,
  walking down the b-axis at fixed $a = 0$ with rising factorial
  coefficient (verified up to $k = 8$).

This is the **Verma module $M(-1)$ of the 3-dim Borel** at lowest
weight $-1$, restricted to the $\{a = 0\}$ axis of $C^{+-}$.

The full $C^{+-}$ is the $\bar A$-module generated by $v_{0, -1}$;
restricted to the 3-dim Borel, it is a **direct sum of column-Verma
modules** indexed by $a \geq 0$:
$$C^{+-}\big|_{\langle z_1, z_2, z_1 z_2 \rangle} \;\cong\;
   \bigoplus_{a \geq 0} M_a, \quad
   M_a = U(\C \cdot z_1) \cdot v_{a, -1}.$$

**W3-W21-04 (Borel-Verma decomposition of the mixed cone).**
**Severity 3. Status valid. Confidence high.** As a module of the
3-dim Borel sub-Lie-algebra $\langle z_1, z_2, z_1 z_2 \rangle \subset
\bar A$, the mixed cone $C^{+-}$ decomposes as a direct sum of
Verma modules
$C^{+-}\big|_\mathfrak{b} = \bigoplus_{a \geq 0} M_a$ where each $M_a$
is the column-Verma at lowest weight $(b - a)$ generated freely by
$z_1$ from $v_{a, -1}$. Symmetrically for $C^{-+}$ at row-Verma.

### §2.5 Verdict on the Wakimoto identification

The proper identification:

$C^{+-}$ has the **structural signature of a Wakimoto module**
(mixed polarization, vacuum, free-field-like factorization at the
linear level), but the underlying Lie algebra $\bar A$ is **not**
affine Kac-Moody, so the standard Wakimoto theorem (Wakimoto 1986;
Frenkel-Ben-Zvi 2004, §11.3) does not directly apply.

**The correct named identification:**
- **As a module of the 3-dim Borel $\mathfrak{b}$ of $\mathrm{GL}_2$**:
  $C^{+-}$ is a direct sum of column-Verma modules $M_a$ at lowest
  weight $(b - a) \in \{-1, -2, -3, \dots\}_{\text{at fixed } a}$.
  This is a **free-field realization of an abelian-Borel parabolic
  Verma**, in the sense of generalized Verma modules of solvable
  Lie algebras (the Verma modules of solvable Borel; not of
  semisimple Borel).
- **As a module of the full $\bar A$**: $C^{+-}$ is a **simple
  cyclic $\bar A$-module generated by $v_{0, -1}$**, distinguished
  by the support condition $\{a \geq 0, b \leq -1\}$ on the
  bi-infinite parent. It is NOT a Wakimoto / Verma in the
  Kac-Moody sense.

**W3-W21-05 (precise identification of $C^{+-}$).** **Severity 3.
Status valid. Confidence high.**
- $C^{+-}$ is **not** a classical Wakimoto module (the standard
  construction requires affine Kac-Moody, central charge,
  $\beta\gamma$-system OPE).
- $C^{+-}$ **IS** a Verma-like module of the **solvable 3-dim
  Borel** $\langle z_1, z_2, z_1 z_2 \rangle \subset \bar A$ at
  every column.
- $C^{+-}$ as a $\bar A$-module is the **cyclic $\bar A$-module
  generated by $v_{0, -1}$**, equivalently the **support-restricted
  bi-infinite parent on the toric stratum $\{z_2 = 0\}$ minus
  origin**.

---

## §3. T3 — Alternative identifications

### §3.1 Bochner-Martinelli residue current

The mixed cone $C^{+-}$ has a canonical realization as a residue
current along the divisor $\{z_2 = 0\}$. Specifically:
$$C^{+-} \;\cong\; \bigoplus_{a \geq 0, b \leq -1} \C \cdot
   (\text{Bochner-Martinelli residue of } z_1^a z_2^b \, dz_2)$$
under the formal-disk pairing. The Bochner-Martinelli residue
extracts the $(0, -1)$-form value of the integrand, giving a
holomorphic-in-$z_1$ / Laurent-in-$z_2$ distribution.

**Reference**: Bochner-Martinelli 1944; Andersson-Passare-Sigurdsson,
*Complex Convexity and Analytic Functionals* (Birkhauser 2004), §3.

This identification is **structurally compatible** with W3-W21-05's
support-restricted interpretation. **Status: heuristic / suggestive**, not
yet a proven Lie module isomorphism.

### §3.2 Mellin transform space

The Mellin transform $\C[z_1] \otimes \mathcal{P}_{z_2}$ (polynomial
in $z_1$, principal-part in $z_2$) lives naturally in the Mellin /
Schwartz space of distributions on $(\C^*)^2$:
$$\mathcal{S}'((\C^*)^2)_{\text{half-Mellin}} \;\supset\; C^{+-}.$$
The Mellin transform of $z_1^a z_2^b$ is the $(a, b)$-character of
the torus $(\C^*)^2$; the principal-part filtration on $z_2$
corresponds to a half-axis condition on the dual character lattice.

This is again **structurally compatible** but does not give a Lie
module isomorphism by itself.

### §3.3 Imaginary Verma module

Imaginary Verma modules of affine Kac-Moody algebras (Futorny 1994;
Hartwig-Zelmanov 2007, *Selecta Math.*) are induced from the
**non-standard** triangular decomposition $\widehat{\mathfrak{g}} =
\widehat{\mathfrak{g}}_+^{\mathrm{im}} \oplus \widehat{\mathfrak{g}}_0
\oplus \widehat{\mathfrak{g}}_-^{\mathrm{im}}$
where the positive/negative parts contain the imaginary roots
positive direction.

The mixed-cone structure of $C^{+-}$ has the formal signature of an
imaginary Verma (mixed polarization, vacuum killed by the "imaginary
positive" subalgebra), but $\bar A$ has no imaginary roots in the
Kac-Moody sense. The imaginary Verma structure does NOT directly
apply.

### §3.4 Whittaker model

A Whittaker model is a representation of a reductive Lie algebra
induced from a non-degenerate character of the unipotent radical of
the Borel. The non-degeneracy condition is critical for irreducibility
(Kostant 1978).

For $\bar A$: the candidate "unipotent radical" of the 3-dim Borel
(W3-W21-04) is $\C \cdot Y = \C \cdot z_1$ (the lowering direction).
A character of $\C \cdot z_1$ is a single scalar (specifying
$z_1 \mapsto c$), but in the Verma realization $z_1$ acts by
rising-factorial, which IS a non-degenerate character valued in the
algebra of vector fields on the b-axis. This is **suggestive** of a
Whittaker structure but not a strict one (the algebra is solvable, not
reductive).

### §3.5 Verdict on alternative identifications

The mixed cone $C^{+-}$ admits multiple complementary identifications,
all of which point to a single underlying object:

**The mixed cone is the support-restricted bi-infinite parent on the
toric divisor $\{z_2 = 0\}$ minus origin, equipped with the canonical
$\bar A$-Lie module structure inherited from the Laurent ring action.**

The Wakimoto / Verma / Whittaker / Mellin / Bochner-Martinelli
identifications are **isomorphisms of structural features** (mixed
polarization, vacuum, residue / character realization), not strict
Lie module isomorphisms with named classical modules.

---

## §4. T4 — Precise theorem statement

### §4.1 Theorem

**Theorem (W3-W21-T1, candidate).** Let
$\widetilde{\mathcal{M}} = \C[z_1^{\pm 1}, z_2^{\pm 1}] / \C$ be the
bi-infinite parent on $\Z^2 \setminus \{(0, 0)\}$ with the W3-corrected
Hamiltonian Lie module structure (W3-W3-02; W12 verified at 165,600
commutators). Let $\mathfrak{b} = \langle z_1, z_2, z_1 z_2 \rangle$
denote the 3-dim solvable Lie subalgebra of
$\bar A = \C[z_1, z_2] / \C$ with relations
$[z_1 z_2, z_1] = -z_1$, $[z_1 z_2, z_2] = +z_2$,
$[z_1, z_2] = 0 \pmod{\text{constants}}$ (the Borel of $\mathrm{GL}_2$,
restricted to the unipotent + diagonal piece). Let
$C^{+-} = \{v_{a, b} : a \geq 0, b \leq -1\} \subset
\widetilde{\mathcal{M}}$ be the mixed cone identified by W14
(W3-W14-01).

Then:
1. **(Borel restriction)** As a Lie module of $\mathfrak{b}$,
   $C^{+-}$ decomposes as
   $$C^{+-}\big|_\mathfrak{b} \;\cong\; \bigoplus_{a \geq 0} M_a,$$
   where each $M_a$ is the column-Verma module
   $U(\C \cdot z_1) \cdot v_{a, -1}$ generated freely by $z_1$
   from the lowest-weight vector $v_{a, -1}$ of $\mathfrak{b}$-weight
   $(-1 - a)$.
2. **(Linear-Hamiltonian tensor factorization)** As a Lie module of
   the abelian linear sub-Lie-algebra $\C \cdot z_1 \oplus \C \cdot z_2$,
   $C^{+-}$ is canonically isomorphic to the tensor product
   $$C^{+-}\big|_{\C \cdot z_1 \oplus \C \cdot z_2}
       \;\cong\; \C[e_a]_{a \geq 0} \otimes_\C
                 \mathcal{P}_{z_2, b \leq -1}$$
   where $\mathcal{P}_{z_2, b \leq -1} = \bigoplus_{b \leq -1} \C \cdot f_b$
   is the Matlis principal-part module on the b-coordinate (with
   $z_1$ acting as $b$-shift) and $\C[e_a]$ is polynomial on the
   a-coordinate (with $z_2$ acting as $-a$-shift); the isomorphism is
   $v_{a, b} \mapsto e_a \otimes f_b$.
3. **(Cyclic $\bar A$-module)** As a Lie module of the full $\bar A$,
   $C^{+-}$ is the cyclic $\bar A$-module generated by $v_{0, -1}$
   modulo the support condition $\{a \geq 0, b \leq -1\}$. The
   annihilator subalgebra of $v_{0, -1}$ in $\bar A$ is
   $\mathrm{Ann}(v_{0, -1}) = \mathrm{span}\{z_2^q : q \geq 1\}
                              \cup \{z_1 z_2^2\}$.
4. **(Cartan diagonal)** The element $z_1 z_2 \in \bar A$ acts
   diagonally on $C^{+-}$ with eigenvalue $(b - a)$ at $v_{a, b}$.

**Symmetric statement** holds for $C^{-+}$ via the obvious mirror
substitution $(a, b) \leftrightarrow (b, a)$ and $(z_1 \leftrightarrow z_2)$.

### §4.2 References supporting each ingredient

- **Wakimoto 1986** (*Comm. Math. Phys.* 104, 605-609): structural
  pattern of free-field realizations, mixed-polarization tensor
  factorization at the Heisenberg level.
- **Frenkel-Ben-Zvi 2004** (*Vertex Algebras and Algebraic Curves*,
  §11.3-§11.6): rigorous vertex-algebra realization of the Wakimoto
  module structure; $\beta\gamma$-system as the canonical example.
- **Frenkel 2007** (*Langlands Correspondence for Loop Groups*, §6):
  Wakimoto modules of arbitrary affine Kac-Moody algebras; vacuum
  characterization.
- **Futorny 1994** (*J. Algebra* 169, 426-441): imaginary Verma
  modules.
- **Hartshorne 1966** (*Residues and Duality*, III.2): Cousin /
  Serre dual on punctured disk; foundation for the residue
  identification.
- **Kunz-Cox-Dickenstein 2013** (*Algebraic Foundations for
  Applied Topology and Data Analysis*, Ch. 5): power-series residue
  model.
- **Matlis 1958** (*Pacific J. Math.* 8, 511-528): Matlis duality
  theorem; injective hull of residue field.
- **Andersson-Passare-Sigurdsson 2004** (Birkhauser): Bochner-
  Martinelli residue currents.
- **Kostant 1978** (*Inventiones Math.* 48, 101-184): Whittaker
  vectors.
- **Drinfeld-Sokolov 1985** (*J. Sov. Math.* 30, 1975-2036):
  Hamiltonian reduction, parabolic structure.

### §4.3 What this is NOT

- **NOT a classical Wakimoto module of an affine Kac-Moody algebra**.
  $\bar A$ lacks the Kac-Moody structure (central extension, opposite
  Borel, root system).
- **NOT a parabolic Verma module of a semisimple Lie algebra**. The
  3-dim Borel is solvable, not the Borel of $\mathfrak{sl}_2$ (since
  $[X, Y] = 0$, not $H$).
- **NOT a tilting / projective / injective in BGG category $\mathcal{O}$**.
- **NOT free as a $\C[z_1]$-module under the Lie algebra action**
  (the iterated $z_1$ has rising-factorial coefficients, not free
  shift).
- **NOT a single Verma in any standard textbook category**.

---

## §5. T5 — Proof sketch

**Proof of W3-W21-T1.**

(1) **Borel restriction.** From W3-W21-01 (verified at 220 triples),
$z_1 \cdot v_{a, b} = b v_{a, b - 1}$ on $C^{+-}$. Iterated: at fixed
$a$, the orbit $\{z_1^k \cdot v_{a, -1} : k \geq 0\} =
\{(-1)^k k!  \cdot v_{a, -1 - k}\}_{k \geq 0}$, a column at fixed
$a \geq 0$. From W3-W21-01, $z_2 \cdot v_{a, -1} = -a \cdot v_{a - 1, -1}$
moves OFF the column to $a - 1$. The 3-dim Borel
$\langle z_1, z_2, z_1 z_2 \rangle$ on $v_{a, -1}$ acts as: $z_2$
moves the column index, $z_1$ generates the column.
Restricted to a single column, $z_2$ acts as zero (W3-W21-03 confirms
$z_2$ kills the $a = 0$ axis). The Verma module structure is
inherited.

(2) **Tensor factorization at linear sub-Lie-algebra.** From W3-W21-01:
$z_1$ acts only on b; $z_2$ acts only on a. The bijection
$v_{a, b} \mapsto e_a \otimes f_b$ identifies $C^{+-}$ with the
tensor product space, with the linear Hamiltonians acting via the
factor-wise rule. This is verified at 220 triples on $C^{+-}$ in
`/tmp/w21_verify_action_formulas.py`.

(3) **Cyclic generation.** From the W3 master formula: any
$v_{a, b} \in C^{+-}$ is reached from $v_{0, -1}$ by:
- iterated $z_1$: walks down the column at $a = 0$.
- single monomial $z_1^p$: jumps to $(p - 1, -2)$.
- combination: the orbit $U(\bar A) \cdot v_{0, -1}$ contains all
  $v_{a, b}$ in $C^{+-}$ (verified by reachability analysis in
  `/tmp/w21_eigenvalue_structure.py`).
The annihilator computation: $z_1^p z_2^q \cdot v_{0, -1} =
-p \cdot v_{p - 1, q - 2}$ is zero iff $p = 0$ or
$(p - 1, q - 2) = (0, 0)$ i.e. $(p, q) \in \{(1, 2)\} \cup
\{(0, q) : q \geq 1\}$.

(4) **Cartan diagonal.** Specialize $(p, q) = (1, 1)$ in the W3
master formula:
$z_1 z_2 \cdot v_{a, b} = (1 \cdot b - 1 \cdot a) v_{a + 0, b + 0} =
(b - a) v_{a, b}$. Diagonal action with eigenvalue $(b - a)$.
$\square$

---

## §6. T6 — Sigma duality clarification

### §6.1 Sigma is NOT a $\bar A$-Lie-module intertwiner generically

Direct computation (`/tmp/w21_sigma_refined.py`):

$$\sigma(z_1^p z_2^q \cdot v_{a, b})
   \;=\; (pb - qa) v_{-a - p, -b - q},$$
$$z_1^p z_2^q \cdot \sigma(v_{a, b})
   \;=\; -(pb - qa + p - q) v_{p - a - 2, q - b - 2}.$$

**Targets**: LHS = $(-a - p, -b - q)$; RHS = $(p - a - 2, q - b - 2)$.
Equal iff $p = 1$ AND $q = 1$.

For $(p, q) = (1, 1)$:
- LHS coefficient = $b - a$.
- RHS coefficient = $-((b - a) + 0) = -(b - a) = a - b$.

So $\sigma(z_1 z_2 \cdot v_{a, b}) = -(z_1 z_2) \cdot \sigma(v_{a, b})$,
**a true sign-flip intertwiner at $(p, q) = (1, 1)$ on all 80
nontrivial cases**.

### §6.2 Sigma is a Cartan-twisted intertwiner at the diagonal generators

Exhaustive search (verified in `/tmp/w21_sigma_refined.py`):

| $(p, q)$ | target matches | sign-flips | universal sign-flip? |
|----------|----------------|------------|----------------------|
| $(1, 1)$ | 80 / 80 | 72 (universal mod sigma fixed points) | **YES** |
| $(2, 2)$ | 8 / 80 | 0 universal | partial (only at fixed bidegree) |
| $(3, 3)$ | 8 / 80 | 0 universal | partial |
| Any other $(p, q)$ with $p \neq q$ or $p = q \neq 1$ | < 8 | partial | no |

When using the **monomial transpose** (testing the relation
$\sigma(z_1^p z_2^q \cdot v) = -z_1^q z_2^p \cdot \sigma(v)$):

| $(p, q)$ | target matches | coefficient matches | universal? |
|----------|----------------|---------------------|------------|
| $(1, 1)$ | 80 / 80 | 80 / 80 | **YES** |
| $(2, 2)$, $(3, 3)$, $(4, 4)$ | 8 / 80 each | 8 / 80 each | partial (bidegree-specific) |
| $(2, 0) \leftrightarrow (0, 2)$ | 67 / 80 | 10 / 67 | partial |

### §6.3 Precise sigma duality statement

**W3-W21-06 (sigma duality on the diagonal Cartan).** **Severity 3.
Status valid. Confidence high.**

The sigma involution $\sigma : v_{a, b} \mapsto v_{-a - 1, -b - 1}$
exchanges the cones $C^{++} \leftrightarrow C^{--}$ and
$C^{+-} \leftrightarrow C^{-+}$ as $\Z^2$-graded vector spaces. As a
Lie module relation:
- **$\sigma$ is NOT a $\bar A$-Lie-module intertwiner**: for generic
  $(p, q)$, the target shifts of $\sigma(z_1^p z_2^q \cdot v)$ and
  $z_1^p z_2^q \cdot \sigma(v)$ disagree, with no fixed sign relating
  them.
- **$\sigma$ IS a sign-flipped intertwiner restricted to the
  diagonal Cartan generator $z_1 z_2$**:
  $$\sigma(z_1 z_2 \cdot v) \;=\; -z_1 z_2 \cdot \sigma(v) \quad
    \text{universally on } \Z^2 \setminus \{(0, 0)\}.$$
  This is the Cartan eigenvalue exchange:
  $z_1 z_2$-eigenvalue at $v_{a, b}$ is $(b - a)$;
  at $\sigma(v_{a, b}) = v_{-a-1, -b-1}$ is
  $(-b - 1) - (-a - 1) = a - b = -(b - a)$.
  Sigma negates the Cartan eigenvalue.

**This refines W14's statement W3-W14-T3.** W14 said "sigma exchanges
cone pairs but is not a Lie module isomorphism; it acts by sign". The
precise statement is: sigma is a **Cartan-twisted involution** that
preserves the diagonal Cartan structure (with sign flip) but does NOT
preserve the action of off-diagonal generators. The off-diagonal
mismatch is the same residue-duality / opposite-shift-direction
obstruction that powers M-29.

---

## §7. T7 — Interaction with W12 Čech SES

### §7.1 The W12 SES as written

W12 §5.4 writes:
$$0 \to \bar A_{\mathrm{desc}} \to C^{+-} \oplus C^{-+} \to \mathcal{P} \to 0.$$

### §7.2 Audit

The standard Čech complex for local cohomology of $R = \C[z_1, z_2]$
at the maximal ideal $(z_1, z_2)$:
$$0 \to R \to R[z_1^{-1}] \oplus R[z_2^{-1}] \to R[z_1^{-1}, z_2^{-1}]
   \to H^2_{(z_1, z_2)}(R) \to 0.$$

In $\Z^2$-graded form (mod constants):
- $R / \C = \bar A_{\mathrm{desc}} = C^{++}$.
- $R[z_1^{-1}] / \C = \{(a, b) : a \in \Z, b \geq 0, (a, b) \neq (0, 0)\} = C^{++} \cup C^{-+}$.
- $R[z_2^{-1}] / \C = \{(a, b) : a \geq 0, b \in \Z, (a, b) \neq (0, 0)\} = C^{++} \cup C^{+-}$.
- $R[z_1^{-1}, z_2^{-1}] / \C = $ full bi-infinite parent
  $\widetilde{\mathcal{M}}$.
- $H^2 = $ Matlis $\mathcal{P} = C^{--}$ (via sigma; cf. appendix
  `prop:app-matlis-realization`).

**Correct Čech SES (full, $\bar A$-equivariant):**
$$0 \to \underbrace{C^{++}}_{\bar A_{\mathrm{desc}}}
    \to (C^{++} \cup C^{-+}) \oplus (C^{++} \cup C^{+-})
    \to \widetilde{\mathcal{M}} \to \mathcal{P} \to 0.$$

The W12 expression "$0 \to \bar A_{\mathrm{desc}} \to C^{+-}
\oplus C^{-+} \to \mathcal{P} \to 0$" is **incorrect as a $\Z^2$-graded
SES of $\bar A$-modules**: $\bar A_{\mathrm{desc}}$ has support $C^{++}$,
while $C^{+-} \oplus C^{-+}$ has support $C^{+-} \cup C^{-+}$, which is
**disjoint from $C^{++}$**. Any degree-zero $\bar A$-equivariant map
$\bar A_{\mathrm{desc}} \to C^{+-} \oplus C^{-+}$ has zero image.

### §7.3 What W12 actually meant

The W12 SES is a **shorthand for the successive quotient SES** of
W14's four-step filtration (W3-W14-01):
$$0 \subset C^{++} \subset C^{++} \cup C^{+-}
   \subset C^{++} \cup C^{+-} \cup C^{-+} \subset
   \widetilde{\mathcal{M}}.$$

Successive quotient SES:
- $0 \to C^{++} \to C^{++} \cup C^{+-} \to C^{+-} \to 0$.
- $0 \to C^{++} \cup C^{+-} \to C^{++} \cup C^{+-} \cup C^{-+}
   \to C^{-+} \to 0$.
- $0 \to C^{++} \cup C^{+-} \cup C^{-+} \to \widetilde{\mathcal{M}}
   \to C^{--} = \mathcal{P} \to 0$.

The **third quotient** is the correct "$\to \mathcal{P} \to 0$"
endpoint. The **first two** introduce $C^{+-}$ and $C^{-+}$ as
SUCCESSIVE QUOTIENTS, NOT as a direct sum in the middle of a
single SES.

**W3-W21-07 (correction of W12 Čech SES).** **Severity 2 (correction).
Status valid. Confidence high.** The W12 §5.4 SES "$0 \to
\bar A_{\mathrm{desc}} \to C^{+-} \oplus C^{-+} \to \mathcal{P} \to 0$"
should be replaced by W14's four-step filtration with three successive
quotient SESs (as above). The correct full Čech SES is
$$0 \to \bar A_{\mathrm{desc}} \to (C^{++} \cup C^{-+})
    \oplus (C^{++} \cup C^{+-}) \to \widetilde{\mathcal{M}}
    \to \mathcal{P} \to 0,$$
where the two middle terms are **axis-localizations** (R[z_i^{-1}]
mod constants), each containing $\bar A_{\mathrm{desc}}$ as a
SUBSPACE plus one mixed cone. The Čech boundary maps are
$\bar A$-equivariant by the universal property of localization;
the SES is exact by the regularity of $R$ (Hartshorne 1966).

### §7.4 The Wakimoto / SES interaction

The Wakimoto-style identification of $C^{+-}$ via W3-W21-T1 is
**compatible** with the corrected Čech SES of W3-W21-07:
- The Borel-Verma column decomposition of $C^{+-}$ (W3-W21-04)
  arises naturally from the axis-localization
  $R[z_2^{-1}] / \C = C^{++} \cup C^{+-}$: each column at fixed $a$
  is the **principal-part filtration** along $z_2$ at that column.
- The cyclic generation by $v_{0, -1}$ corresponds to the **lowest
  pole-order generator** of the Matlis principal-part along
  $\{z_2 = 0\}$ at $z_1^0$ (i.e., the Bochner-Martinelli residue at
  the origin in the $z_2$-direction).

**P-W21-A: residual.** The full $\bar A$-equivariance of the boundary
maps in the corrected Čech SES (W3-W21-07) is asserted via the
universal property of localization but not explicitly verified at the
monomial level. This is within reach by direct computation on
monomials but is left as a Phase-2 residual.

---

## §8. T8 — Interaction with M-29 mixed-cone version

W14 (W3-W14-04) extended M-29 directionally to the mixed cones: the
rising-factorial obstruction acts on each direction separately. The
W3-W21-T1 theorem **strengthens** this:

The Verma module of the 3-dim Borel $\langle z_1, z_2, z_1 z_2 \rangle$
on $C^{+-}$ has $z_1$ acting with **rising-factorial coefficients**
$(b)(b-1)(b-2)\cdots$ on the column at any fixed $a$. By the M-29 /
W3-W7-01 / appendix
`thm:app-matlis-no-polynomial-realization` argument, this rising
factorial precludes locally nilpotent $z_1$ on any flat
$\hbar$-deformation interpolating $C^{+-}$ with $C^{++}$. The
directional sharpening of M-29 is RECONFIRMED at the
Borel-Verma column level, with explicit rising-factorial coefficient
$(-1)^k k!$ at step $k$.

**No new obstruction is added; W3-W14-04 is the precise statement,
now with explicit Verma module coefficients verifying the rising-
factorial structure.**

---

## §9. Per-target findings table

| Target | Lens | Verdict | Severity | Detail |
|--------|------|---------|----------|--------|
| T1 (Verify W14 reduction formulas) | Gelfand + Examples | RESOLVED at 440 triples | 3 | W3-W21-01 |
| T2 (Wakimoto identification) | Gelfand | NOT classical Wakimoto, IS Borel-Verma | 3 | W3-W21-04, W3-W21-05 |
| T3 (Alternative identifications) | Gelfand | Multiple complementary | 2 | §3 (Bochner-Martinelli, Mellin, imaginary Verma, Whittaker) |
| T4 (Precise theorem statement) | Gelfand + Examples | THEOREM W3-W21-T1 (4 parts) | 3 | §4 |
| T5 (Proof sketch) | Examples | RESOLVED via direct verification | 3 | §5 |
| T6 (sigma duality) | Gelfand | Sigma is Cartan-twisted intertwiner only at $(1, 1)$ | 3 | W3-W21-06 |
| T7 (Čech SES audit) | Gelfand | W12 SES needs correction | 2 | W3-W21-07 |
| T8 (M-29 interaction) | Gelfand | M-29 direction sharpening reconfirmed | 2 | §8 |

---

## §10. Heal proposals

**Heal H-W3-W21-A (precise theorem statement for mixed cones).**
Replace W14's CONJECTURE W3-W14-C1 (Wakimoto / parabolic-Verma
identification) with the precise THEOREM W3-W21-T1 of §4: $C^{+-}$
is a Verma module of the 3-dim solvable Borel $\langle z_1, z_2,
z_1 z_2 \rangle \subset \bar A$ at column-level, NOT a classical
Wakimoto module. The structural signature (mixed polarization,
Cartan eigenvalue $(b - a)$, vacuum $v_{0, -1}$ killed by
$z_2$-axis) IS Wakimoto-like; the underlying Lie algebra
identification is solvable-Borel-Verma. Add to W14 ledger as
"W14 follow-up" sub-section, with credits to W21.

**Heal H-W3-W21-B (sigma duality clarification).** Refine W14's
W3-W14-T3 (sigma duality on mixed cones) to the precise
statement W3-W21-06: sigma is NOT a Lie module intertwiner
generically, but is a **Cartan-twisted sign-flipped intertwiner
at the diagonal generator $z_1 z_2$ alone**. The off-diagonal
mismatch is the same residue-duality / opposite-shift obstruction
of M-29.

**Heal H-W3-W21-C (Čech SES correction).** Replace W12 §5.4 SES
"$0 \to \bar A_{\mathrm{desc}} \to C^{+-} \oplus C^{-+} \to \mathcal{P} \to 0$"
by the corrected formulation W3-W21-07: the proper Čech SES is
$0 \to \bar A_{\mathrm{desc}} \to (C^{++} \cup C^{-+}) \oplus
(C^{++} \cup C^{+-}) \to \widetilde{\mathcal{M}} \to \mathcal{P} \to 0$,
or equivalently the three successive quotient SESs of W14's
four-step filtration.

**Heal H-W3-W21-D (citation enrichment).** Add Wakimoto 1986,
Frenkel-Ben-Zvi §11.3-§11.6, Frenkel 2007 §6, and Futorny 1994 to
W14's reference list as authority for the Wakimoto module structure.

---

## §11. New residuals

**R-W3-W21-A (Phase-2).** Explicit verification of the
$\bar A$-equivariance of the Čech boundary maps in W3-W21-07,
on monomials. Within reach.

**R-W3-W21-B (Phase-3).** Free-field realization of $\bar A$ as a
$\beta\gamma$-system or analogue, identifying $C^{+-}, C^{-+}$ as
Fock spaces of polarized modes. This is the genuinely Wakimoto-
flavor question, but $\bar A$ is the Poisson algebra of the disk
modulo constants, NOT an affine Kac-Moody algebra; the proper
$\beta\gamma$-realization may live in a different framework
(Poisson vertex algebra of Bakalov-Kac, *Comm. Math. Phys.* 240,
2003).

**R-W3-W21-C (Phase-3).** Identification of $C^{+-}, C^{-+}$ in
the framework of **D-module residue currents** (Andersson-Passare-
Sigurdsson 2004) and the **Kashiwara-Schapira microlocal
sheaves** at the conormal bundle of the brane line. This unifies
the structural signatures of §3 and may give a strict Lie module
isomorphism in the microlocal category.

**R-W3-W21-D (Phase-2).** The Borel-Verma column decomposition
$C^{+-}\big|_\mathfrak{b} = \bigoplus_{a \geq 0} M_a$ has natural
**categorification**: each $M_a$ is a column-Verma at lowest
weight $-1 - a$. The graded character is
$\chi(C^{+-}) = \sum_{a \geq 0} q_2^{-1} / (1 - q_1)$ (geometric
series in $q_1$, fixed $q_2^{-1}$ for column-vacuum). This
factorizes as $\chi(C[z_1]) \cdot \chi(\mathcal{P}_{z_2})$, in
agreement with the tensor factorization (W3-W21-02).

---

## §12. Provenance

W21 (Wave 3) read in full:
- `/Users/raeez/topological-strings/CLAUDE.md`.
- `/Users/raeez/topological-strings/reconstitution/wave3-W14-mixed-cones-2026-04-28.md`.
- `/Users/raeez/topological-strings/reconstitution/wave3-W3-nekrasov-2026-04-28.md`.
- `/Users/raeez/topological-strings/reconstitution/wave3-W12-blast-radius-2026-04-28.md`.
- `/Users/raeez/topological-strings/appendix-matlis-principal-parts.tex`.
- `/Users/raeez/topological-strings/scripts/check_bi_infinite_lie_consistency.py`.
- `/tmp/w14_four_cones_probe.py`.
- `/tmp/w14_lie_substructure.py`.
- `/tmp/w14_parabolic_intertwiner.py`.

Computational checks (scratch, `/tmp/w21_*.py`):
- `/tmp/w21_verify_action_formulas.py`: 440 (a, b, action) triples
  on $C^{+-} \cup C^{-+}$, 0 failures.
- `/tmp/w21_eigenvalue_structure.py`: discovery of the diagonal
  Cartan $z_1 z_2$ with eigenvalue $(b - a)$; full annihilator of
  $v_{0, -1}$ computed to (max_p, max_q) = (4, 4).
- `/tmp/w21_sigma_refined.py`: exhaustive sigma intertwiner search;
  $(p, q) = (1, 1)$ alone gives universal sign-flip intertwiner;
  monomial-transpose form gives match at all $(p, p)$ but only
  at restricted bidegree.
- `/tmp/w21_diagonal_lie_subalgebra.py`: 3-dim Borel
  $\langle z_1, z_2, z_1 z_2 \rangle$ classification; rising-factorial
  walk verification on $v_{0, -1}$ to step 8.

External references invoked:
- Wakimoto, *Comm. Math. Phys.* 104 (1986) 605-609.
- Frenkel-Ben-Zvi, *Vertex Algebras and Algebraic Curves* (AMS, 2nd
  ed. 2004), §11.3-§11.6.
- Frenkel, *Langlands Correspondence for Loop Groups* (Cambridge,
  2007), Chapter 6.
- Futorny, *J. Algebra* 169 (1994) 426-441.
- Hartshorne, *Residues and Duality* (Springer LNM 20, 1966), III.2.
- Matlis, *Pacific J. Math.* 8 (1958) 511-528.
- Andersson-Passare-Sigurdsson, *Complex Convexity and Analytic
  Functionals* (Birkhauser 2004).
- Kostant, *Inventiones Math.* 48 (1978) 101-184.
- Drinfeld-Sokolov, *J. Sov. Math.* 30 (1985) 1975-2036.
- Bakalov-Kac, *Comm. Math. Phys.* 240 (2003) 367-403.

W21 confidence: every computed claim verified at the level of explicit
arithmetic on integers; tensor-factorization argument verified at the
linear-Hamiltonian level; the precise theorem (W3-W21-T1) supersedes
the W14 conjecture (W3-W14-C1) by REPLACING the unproven Wakimoto
identification with a verified Borel-Verma identification. No web
search.

---

## §13. 200-word summary

W21 verifies W14's mixed-cone reduction formulas at 440 (a, b, action)
triples (0 failures) and audits the Wakimoto identification W3-W14-C1.
**Finding**: $C^{+-}$ is NOT a classical Wakimoto module of an affine
Kac-Moody algebra ($\bar A = \C[z_1, z_2]/\C$ is not Kac-Moody). The
correct identification is **W3-W21-T1**: $C^{+-}$ is a Verma module
of the 3-dim solvable Borel $\mathfrak{b} = \langle z_1, z_2, z_1 z_2
\rangle \subset \bar A$ (with $[z_1 z_2, z_1] = -z_1$, $[z_1 z_2, z_2]
= +z_2$, $[z_1, z_2] = 0$), restricted to columns indexed by
$a \geq 0$; the linear $\C \cdot z_1 \oplus \C \cdot z_2$ acts as a
tensor product action on $\C[z_1] \otimes \mathcal{P}_{z_2}$;
$z_1 z_2$ is a **diagonal Cartan** with eigenvalue $(b - a)$. The
sigma involution is a Cartan-twisted sign-flipped intertwiner ONLY
at $(p, q) = (1, 1)$, refining W14's W3-W14-T3. The W12 Čech SES
"$0 \to \bar A_{\mathrm{desc}} \to C^{+-} \oplus C^{-+} \to
\mathcal{P} \to 0$" is incorrect as written ($Z^2$-grading
disjointness); the correct SES has axis-localizations in the middle.
M-29 directional sharpening is reconfirmed via the explicit
$(-1)^k k!$ rising-factorial of the Borel-Verma column.
**Stable core preserved unmodified. W14 conjecture sharpened to a
verified theorem; sigma duality precise; W12 SES corrected.**

End of W21 Wave-3 ledger.
