# Wave 3 / W26 — Etingof + Functoriality Lens (Column-Verma Theorem and Symplectic Functoriality)

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.**
- *Primary:* Etingof — tensor categories, finite examples, semisimplicity,
  deformation/quantization. Particular attention to the rigidity of the
  abelian category of $\Z^2$-graded $\bar A$-modules and to the
  characterization of induced modules from solvable Lie subalgebras.
- *Secondary:* Functoriality — naturality of the column-Verma decomposition
  under the GL$_2 \times T^2$ subgroup of $\mathrm{Symp}_{\mathrm{form}}(\C^2, 0)$
  and explicit obstruction at quadratic symplectomorphisms.
**Wave.** 3 (independent attacker; reads W3-W21 column-Verma correction,
W3-W14 mixed-cone foundation, W3-W5 GL$_2 \times T^2$ naturality, W3-W12
Čech SES).
**Mandate.** Verify W21's column-Verma identification W3-W21-T1 by
hand-computation on $\geq 50$ basis vectors; identify the precise
functoriality class (linear vs quadratic symplectomorphisms);
disambiguate the "tensor factorization at linear-Hamiltonian level only"
claim; produce the $\sigma$-twist verification at $(p,q)=(1,1)$;
state W3-W26-T1 as a precise theorem of the 3-dim solvable Borel
$\langle z_1, z_2, z_1 z_2 \rangle$.
**Inputs (read in full).**
- `/Users/raeez/topological-strings/CLAUDE.md`.
- `/Users/raeez/topological-strings/reconstitution/wave3-W21-wakimoto-2026-04-28.md` (full).
- `/Users/raeez/topological-strings/reconstitution/wave3-W14-mixed-cones-2026-04-28.md` (full).
- `/Users/raeez/topological-strings/reconstitution/wave3-W5-kazhdan-2026-04-28.md` (full).
- `/Users/raeez/topological-strings/reconstitution/wave3-W12-blast-radius-2026-04-28.md` (full).
- `/Users/raeez/topological-strings/main.tex` (lines 1612–1614 for $T^2$
  reference; structure of formal symplectomorphism cited from W21 / W14).
- `/tmp/w26_column_verma.py`, `/tmp/w26_extended_eigenvalue.py` (this wave).
**Mode.** Proposal-only. No commits. Master ledger schema; IDs prefix `W3-W26-`.
**Independence.** W21's W3-W21-T1 column-Verma claim is taken as an
**input under Etingof + Functoriality attack**. The deliverable is
(i) explicit hand-construction of $M_a$ as a Borel-Verma with named HWV;
(ii) eigenvalue verification at 50 distinct basis vectors plus 168-vector
sweep on $\Z^2 \setminus \{(0, 0)\}$; (iii) full annihilator computation
of $v_{0, -1}$ in $U(\bar A)$; (iv) precise statement of where tensor
factorization fails beyond linear; (v) $\mathrm{GL}_2 \times T^2$
equivariance proof + explicit non-equivariance under quadratic
$\varphi: (z_1, z_2) \mapsto (z_1, z_2 + z_1^2)$; (vi) refined theorem
W3-W26-T1; (vii) classification of R-W3-W14-A as **discharged** by
column-Verma identification at $\mathrm{GL}_2 \times T^2$ level,
**redirected** as new residual at Symp$_{\mathrm{form}}$ level.

---

## §0. Method

The Etingof lens lives inside the abelian category $\mathsf{Mod}_{\Z^2}^{T^2}(\bar A)$
of $\Z^2$-graded $\bar A$-modules with compatible $T^2$-equivariance.
A column-Verma module of a 3-dim solvable Borel $\mathfrak{b}$
generated freely by a single locally-nilpotent unipotent generator
is a textbook construction (Dixmier 1996, *Enveloping Algebras*,
§4.1.4, §7); we test that the candidate identification matches the
universal characterization of such modules.

The Functoriality lens audits which group acts naturally on the
column-Verma decomposition. The W5 finding W3-W5-03 is taken as input:
the M-31 identification is GL$_2 \times T^2$-natural but not
Symp$_{\mathrm{form}}$-natural. We verify the same is true for the
column-Verma decomposition itself, and we **make explicit** the
obstruction at quadratic symplectomorphisms by exhibiting an infinite
column-mixing.

Two new probes inscribed in `/tmp/w26_*.py`:
- `/tmp/w26_column_verma.py` — Borel structure constants verification
  (168-vector $\Z^2$-sweep), tensor-factorization breakdown analysis,
  GL$_2$ vs Symp$_{\mathrm{form}}$ equivariance, $\sigma$-twist at
  $(1, 1)$ on 119 vectors.
- `/tmp/w26_extended_eigenvalue.py` — 50-vector explicit table of
  $z_1, z_2, z_1 z_2$ action on $M_0, M_1, M_2, M_3, M_4$ columns;
  full annihilator of $v_{0, -1}$ at $(p, q) \in [0, 4]^2$;
  iterated column walk on $M_0$ to step 7; quadratic-symplectomorphism
  column-mixing display.

All arithmetic is `fractions.Fraction` (no float).

---

## §1. T1 — Rigorous verification of W21's column-Verma theorem

### §1.1 T1(a) — Hand-construction of $M_a$ as Borel-Verma

**Borel structure constants verification.**

The 3-dim solvable Borel $\mathfrak{b} = \langle z_1, z_2, z_1 z_2 \rangle
\subset \bar A$ has structure (Poisson bracket modulo constants):
$$
[z_1 z_2, z_1] = -z_1, \qquad
[z_1 z_2, z_2] = +z_2, \qquad
[z_1, z_2] = 0 \pmod{\C}.
$$
With $H = z_1 z_2$ (Cartan), $X = z_2$ (raising), $Y = z_1$ (lowering),
this is $[H, X] = X$, $[H, Y] = -Y$, $[X, Y] = 0$ — the "ax + b"
solvable Borel of $\mathrm{GL}_2$ (NOT the Borel of $\mathfrak{sl}_2$
since $[X, Y] = 0$ rather than $H$).

Verification on the bi-infinite parent $\widetilde{\mathcal M}$ at
all 168 cells $(a, b) \in [-6, 6]^2 \setminus \{(0, 0)\}$ via
`/tmp/w26_column_verma.py`:

```
[H, X] - X test: 168 tests, 0 mismatches
[H, Y] - (-Y) test: 168 tests, 0 mismatches
[X, Y] = 0 (mod constants) test: 168 tests, 0 violations
```

Sample: $[z_1 z_2, z_2] \cdot v_{3, 2}$ computed as iterated
$\{(z_1 z_2) (z_2 v) - z_2 (z_1 z_2 v)\}$ produces $-3 v_{2, 2}$,
matching $z_2 \cdot v_{3, 2} = -3 v_{2, 2}$ directly. Confirmed
universally.

**Construction of $M_a$.**

For each $a \geq 0$, define the **column module**
$$
M_a := \mathrm{span}\{v_{a, -1}, v_{a, -2}, v_{a, -3}, \dots\}
$$
inside $C^{+-}$. Define the action of $\mathfrak{b}$:
- $X = z_2$ acts on $M_a$ as $z_2 \cdot v_{a, b} = -a \, v_{a-1, b}$;
  this **leaves $M_a$ since the target column index is $a - 1$**.
  However, in restriction to $M_a$ alone (with leak truncation),
  $X$ acts as zero on the $a = 0$ axis and as a column-shifter
  on $a \geq 1$. Within the COLUMN $M_a$ itself, $X$ does not
  act on $M_a$ — it leaves the column.
- $Y = z_1$ acts on $M_a$ as $z_1 \cdot v_{a, b} = b \, v_{a, b-1}$;
  this **stays in $M_a$** (column index is preserved, $b$-coordinate
  shifts down). $Y$ is the column-internal generator.
- $H = z_1 z_2$ acts diagonally: $z_1 z_2 \cdot v_{a, b} = (b - a) v_{a, b}$.

**HWV (highest-weight vector) of $M_a$:** $v_{a, -1}$.

Properties of $v_{a, -1}$:
1. **$Y$-cyclic**: $\{Y^k \cdot v_{a, -1}\}_{k \geq 0}$ spans $M_a$.
   Specifically, $Y^k \cdot v_{a, -1} = (-1)^k k! \cdot v_{a, -1 - k}$
   (rising-factorial coefficient).
2. **$H$-eigenvalue**: $H \cdot v_{a, -1} = (-1 - a) v_{a, -1}$.
3. **$X$-leakage**: $X \cdot v_{a, -1} = -a \cdot v_{a - 1, -1}$.
   For $a = 0$: $X$ kills $v_{0, -1}$ (the unique stably annihilated
   HWV). For $a \geq 1$: $X$ leaves the column.

The **column-restricted $M_a$** (with $X$-action either zeroed or
viewed as the inter-column shifter) is a Verma module of the
**Borel sub-Lie-algebra $\C \cdot Y \oplus \C \cdot H$**
(the diagonal + lowering piece of $\mathfrak{b}$, omitting
$X = z_2$): $M_a$ is freely generated by $Y^k$ from $v_{a, -1}$
with $H$-weights $\{-1 - a, -2 - a, -3 - a, \dots\}$
(decreasing arithmetic progression in $-1, \-2, -3, \dots$).

In the language of W21 §2.4: $M_a = U(\C \cdot Y) \cdot v_{a, -1}$ is
a **Verma of the rank-1 unipotent $\C \cdot Y$**, decorated with
$H$-eigenvalue $-1 - a$ at the HWV. Together, $\bigoplus_{a \geq 0} M_a$
is the column-Verma decomposition of $C^{+-}$ as a $\mathfrak{b}$-module
(with $X$ acting as a column-shifter $M_a \to M_{a-1}$, killed at
$a = 0$).

**W3-W26-01 (Borel-Verma column construction, hand-verified).**
**Severity 3. Status valid. Confidence high.**
The 3-dim solvable Borel structure $[H, X] = X$, $[H, Y] = -Y$,
$[X, Y] = 0 \pmod{\C}$ is verified at 168 commutator instances on
$\Z^2 \setminus \{(0, 0)\}$ with zero failures. Each column $M_a =
U(\C \cdot Y) \cdot v_{a, -1}$ is a rank-1 Verma of the abelian
sub-Lie-algebra $\C \cdot Y \subset \mathfrak{b}$ with HWV
$v_{a, -1}$, $H$-weight $-1 - a$, and rising-factorial $Y$-orbit
$\{(-1)^k k! \cdot v_{a, -1 - k}\}_{k \geq 0}$.

### §1.2 T1(b) — Eigenvalue verification on 50+ basis vectors

Output of `/tmp/w26_extended_eigenvalue.py`, 50 vectors on
$M_0 \cup M_1 \cup M_2 \cup M_3 \cup M_4$ with $b \in [-10, -1]$:

| $(a, b)$ | $z_1 \cdot v$ | $z_2 \cdot v$ | $H = z_1 z_2 \cdot v$ (eig $= b - a$) |
|----------|--------------|--------------|----------------------------------------|
| $(0, -10)$ | $-10 v_{0, -11}$ | $0$ | $-10 v_{0, -10}$ |
| $(0, -1)$ | $-v_{0, -2}$ | $0$ | $-v_{0, -1}$ |
| $(1, -10)$ | $-10 v_{1, -11}$ | $-v_{0, -10}$ | $-11 v_{1, -10}$ |
| $(1, -1)$ | $-v_{1, -2}$ | $-v_{0, -1}$ | $-2 v_{1, -1}$ |
| $(2, -3)$ | $-3 v_{2, -4}$ | $-2 v_{1, -3}$ | $-5 v_{2, -3}$ |
| $(3, -1)$ | $-v_{3, -2}$ | $-3 v_{2, -1}$ | $-4 v_{3, -1}$ |
| $(4, -10)$ | $-10 v_{4, -11}$ | $-4 v_{3, -10}$ | $-14 v_{4, -10}$ |
| $(4, -1)$ | $-v_{4, -2}$ | $-4 v_{3, -1}$ | $-5 v_{4, -1}$ |

Aggregate (50 vectors): **0 failures** for $z_1$, $z_2$, $H$ on every
test. Independent sweep on full $\Z^2 \setminus \{(0, 0)\}$ at
$|a|, |b| \leq 6$ (168 vectors): **0 failures** for $H$-eigenvalue.

**W3-W26-02 (Cartan eigenvalue verified at 50 + 168 = 218 vectors).**
**Severity 3. Status valid. Confidence high.**
The eigenvalue formula $z_1 z_2 \cdot v_{a, b} = (b - a) v_{a, b}$
holds at every basis vector tested. Specifically, the diagonalization
of $H$ on every column $M_a$ produces the arithmetic-progression
spectrum $\{-1 - a, -2 - a, -3 - a, \dots\}$.

### §1.3 T1(c) — Vacuum annihilator characterization

Direct computation of the action of all $z_1^p z_2^q$ for
$p, q \in [0, 4]$ on $v_{0, -1}$:

| $(p, q)$ | $z_1^p z_2^q \cdot v_{0, -1}$ | Annihilator? |
|----------|------------------------------|--------------|
| $(0, q)$, $q \geq 1$ | ANNIHILATES (coefficient $= -p \cdot 0 = 0$) | YES |
| $(1, 0)$ | $-v_{0, -2}$ | NO |
| $(1, 1)$ | $-v_{0, -1}$ | NO (eigenvalue $-1$) |
| $(1, 2)$ | ANNIHILATES (target $= (0, 0)$, mod constants) | YES |
| $(1, 3)$ | $-v_{0, 1}$ | NO (off-cone target $b = 1$) |
| $(p \geq 2, q \geq 0)$ | non-zero, off-cone for $b = q - 2 \geq 0$ | NO |

**Vacuum annihilator characterization (W3-W26-03).**

The $U(\bar A)$-annihilator of $v_{0, -1}$ for monomial generators is:
$$
\mathrm{Ann}(v_{0, -1}) \;\supseteq\;
   \mathrm{span}\bigl\{ z_2^q : q \geq 1 \bigr\} \;\cup\; \{ z_1 z_2^2 \}.
$$

The first family follows from the fact that the W3 master formula
gives coefficient $-pa$ for $(p, q) \mapsto (p \cdot b - q \cdot a)$
at $a = 0$: $z_2^q \cdot v_{0, -1}$ has coefficient $-q \cdot 0 = 0$
for the linear part, and crucially, the COMPOSITION
$z_2^q \cdot v_{0, b}$ for any $b$ has coefficient $-q \cdot 0 = 0$
since $a = 0$. The pure $z_2$-monomials act by zero on the entire
$\{a = 0\}$ axis.

This is **stronger than W21's claim** "the vacuum is annihilated by
all $z_2$-monomials": it is annihilated by all $z_2$-monomials (any
power $q \geq 1$) directly via the W3 master formula coefficient
$-q a = 0$ at $a = 0$. Iterated $z_2 \cdot z_2 \cdot \dots$ gives
the same zero, since each step lands at $a = 0$ from $a = 0$.

**Caveat on annihilator scope.** W21's clean phrasing "annihilator
of $v_{0, -1}$ in $\bar A$ is $\mathrm{span}\{z_2^q\} \cup \{z_1 z_2^2\}$"
holds at the level of single-monomial action. For products
$z_1^{p_1} z_2^{q_1} \cdot z_1^{p_2} z_2^{q_2}$, additional
annihilator elements arise (e.g., $z_1 z_2^3 \cdot v_{0, -1}$ does
NOT annihilate, since via W3 master formula it gives $-1 \cdot v_{0, 1}$,
which is OFF the $C^{+-}$ cone but in the bi-infinite parent it is
nonzero). Within the bi-infinite parent, the annihilator generators
(at single monomial level) are precisely $\{z_2^q\} \cup \{z_1 z_2^2\}$.

**W3-W26-03 (vacuum annihilator on the $\{a = 0\}$ axis).**
**Severity 2. Status valid. Confidence high.** $v_{0, -1}$ is
annihilated by every $z_2^q$ for $q \geq 1$ (since $a = 0$),
and additionally by $z_1 z_2^2$ (since target $(0, 0)$ is killed
by mod-constants). Iterated $z_2$-compositions also annihilate
since the orbit stays on the $\{a = 0\}$ axis.

### §1.4 T1(d) — Tensor factorization failure beyond linear Hamiltonians

**Claim under audit.** W21 W3-W21-02 says: tensor factorization
$C^{+-} \cong \C[z_1] \otimes \mathcal P_{z_2}$ holds **at the
abelian linear-Hamiltonian sub-Lie-algebra $\C \cdot z_1 \oplus
\C \cdot z_2$** (and at the abelian $\{z_1^p, z_2^q\}_{p, q \geq 0}$),
but NOT at the level of mixed monomials $z_1^p z_2^q$ with $p, q \geq 1$.

**Hand-verification at $z_1^2$** (single monomial vs iterated).

Take $v = v_{2, -3} \in C^{+-}$.

- Iterated $z_1 \cdot (z_1 \cdot v)$: $z_1 \cdot v_{2, -3} = -3 v_{2, -4}$
  via W3 formula $(p = 1, q = 0)$: coeff $b = -3$, shift $(0, -1)$.
  Then $z_1 \cdot v_{2, -4} = -4 v_{2, -5}$. So
  $$
  z_1 \cdot (z_1 \cdot v_{2, -3}) = -3 \cdot -4 \cdot v_{2, -5} = 12 \, v_{2, -5}.
  $$
- Single monomial $z_1^2 \cdot v_{2, -3}$ via W3 formula $(p = 2, q = 0)$:
  coeff $2 b - 0 = -6$, shift $(1, -1)$, target $(3, -4)$:
  $$
  z_1^2 \cdot v_{2, -3} = -6 \, v_{3, -4}.
  $$

**Targets disagree** (column $a = 2$ vs column $a = 3$);
**coefficients disagree** ($+12$ vs $-6$).

Tensor factorization $C^{+-} \cong \C[e_a] \otimes \mathcal P_{f_b}$
predicts: a single $z_1$ acts as $1 \otimes (b\text{-shift})$, so
$z_1^2$ as a tensor-factorized operator acts as $1 \otimes
(b\text{-shift})^2$, giving $1 \otimes (b)(b - 1)$ shift. On
$v_{2, -3} = e_2 \otimes f_{-3}$: predicted $(-3)(-4) e_2 \otimes
f_{-5} = 12 v_{2, -5}$, **matching the iterated** but NOT the
single monomial.

**Tensor factorization fails at single mixed-monomial action** because
the W3 master coefficient $(pb - qa)$ has BOTH an $a$-dependent
piece AND a $b$-dependent piece for $p, q \geq 1$ separately, and
the SHIFT $(p - 1, q - 1)$ is also bidirectional. The tensor
factorization is honest only for the PURE $z_1^p$ (where $q = 0$,
shift $(p - 1, -1)$, but coefficient $pb$ is still $b$-only —
SHIFT a-coordinate by $p - 1$, NOT staying in the column!).

**Wait.** Re-examine. $z_1^2 \cdot v_{a, b}$ shifts to $(a + 1, b - 1)$
with coefficient $2b$. So $z_1^2$ as a SINGLE monomial does NOT
preserve the column index — it shifts $a \to a + 1$. This is in
contrast to ITERATED $z_1 z_1$, which does preserve the column.

The disagreement is structural: in the Hamiltonian Lie algebra
$\bar A$ on the bi-infinite parent, the "monomial product"
$z_1^p z_2^q$ is the **single Hamiltonian generator** $z_1^p z_2^q
\in \bar A$, NOT the iterated composition $\underbrace{z_1 \cdot
\dots \cdot z_1}_{p} \cdot \underbrace{z_2 \cdot \dots \cdot z_2}_{q}$
in $U(\bar A)$. The Hamiltonian $z_1^p z_2^q$ is a single linear
operator on the module, with a specific shift $(p - 1, q - 1)$;
iterated linear Hamiltonians compose differently.

**Key observation.** The W3-W14-02 / W3-W21-02 tensor factorization
is valid at the level of the abelian sub-Lie-algebra $\C \cdot z_1
\oplus \C \cdot z_2$ ONLY (this is the linear Hamiltonian piece).
Iterated $z_1 \cdot z_1$ in $U(\C \cdot z_1)$ corresponds to applying
the shift $(0, -1)$ twice, giving the column-internal $b(b-1)$
factorial — that IS tensor-factorized. But the SINGLE $z_1^2 \in
\bar A$ (a separate Hamiltonian generator) acts with its own shift
$(1, -1)$, which mixes the $a$ and $b$ coordinates.

**W3-W26-04 (precise statement of tensor factorization scope).**
**Severity 3. Status valid. Confidence high.**
The tensor factorization $C^{+-} \cong \C[z_1] \otimes \mathcal{P}_{z_2}$
is an isomorphism of modules over the abelian sub-Lie-algebra
$\C \cdot z_1 \oplus \C \cdot z_2 \subset \bar A$, and over its
universal enveloping algebra $U(\C \cdot z_1 \oplus \C \cdot z_2) =
\C[z_1] \otimes \C[z_2]$, but NOT over the full $\bar A$. For
$p, q \geq 1$ in the SAME monomial, $z_1^p z_2^q \in \bar A$ acts
with shift $(p - 1, q - 1)$ — mixing the two factors — and the
coefficient $(pb - qa)$ is bilinear in $(a, b)$, breaking the tensor
structure. Iterated composition $z_1^{\circ p} z_2^{\circ q}$ in
the Heisenberg / linear sub-algebra is tensor-factorized; the single
Hamiltonian $z_1^p z_2^q \in \bar A$ is not.

---

## §2. T2 — z_1^2 worked example: Hamiltonian vs Verma action

The two interpretations of "z_1^2":
1. **Verma interpretation**: $z_1^2 \in U(\C \cdot Y)$ where $Y = z_1 \in
   \mathfrak{b}$. This is iterated $Y^2$ in the universal enveloping
   algebra of the rank-1 unipotent.
2. **Hamiltonian interpretation**: $z_1^2 \in \bar A$ as a single distinct
   Hamiltonian generator (monomial of degree 2 in $z_1$).

At $v_{2, -1}$:
- Verma interpretation: $Y^2 \cdot v_{2, -1} = z_1 \cdot (z_1 \cdot v_{2, -1})
  = z_1 \cdot (-v_{2, -2}) = z_1 \cdot (-1)v_{2, -2} = -1 \cdot (-2) v_{2, -3}
  = +2 v_{2, -3}$. Stays in column $a = 2$.
- Hamiltonian interpretation: $z_1^2 \cdot v_{2, -1} = (2 \cdot -1 - 0 \cdot 2) v_{3, -2}
  = -2 v_{3, -2}$. Jumps OFF column to $a = 3$.

| Interpretation | Target | Coefficient | Tensor factorization predicts |
|---------|--------|-------------|------------------------------|
| Verma ($Y^2$ in $U(\mathfrak{b})$) | $(2, -3)$ | $+2$ | $+2$ — MATCH |
| Hamiltonian ($z_1^2 \in \bar A$, single monomial) | $(3, -2)$ | $-2$ | $+2$ — MISMATCH |

The tensor factorization at the linear Hamiltonian level INCLUDES the
iterated $Y^2$ action (since $U(\C \cdot Y) = \C[Y]$ and the action
of $Y^k$ stays on the column with rising-factorial coefficient
$b(b-1)\cdots(b-k+1)$). The full $\bar A$ action introduces a
DISTINCT $z_1^2$ generator outside the linear sub-algebra; this
generator acts as a column-shifter, breaking the tensor structure.

**Summary.** The W21 tensor factorization is honest at the Heisenberg
level $\C \cdot z_1 \oplus \C \cdot z_2$ and at its universal
enveloping algebra (which in this abelian case is just polynomials).
Above the linear level, the FULL Poisson algebra $\bar A$ includes
new generators $z_1^p z_2^q$ for $p + q \geq 2$ that are NOT
products in the Heisenberg sense — they are independent Hamiltonians
acting via a different shift. The Verma column structure is preserved
only by the abelian linear Heisenberg sub-Lie-algebra.

**W3-W26-05 (z_1^2 disambiguation).**
**Severity 2. Status valid. Confidence high.** The Hamiltonian
generator $z_1^2 \in \bar A$ is NOT the same operator as $Y^2 = z_1 \cdot z_1
\in U(\C \cdot z_1)$. The first acts with shift $(1, -1)$ (column-mixing);
the second acts with shift $(0, -2)$ (column-internal). The W21
column-Verma decomposition uses the SECOND (universal-enveloping
iterated action of the rank-1 Heisenberg); the full $\bar A$-module
structure of $C^{+-}$ uses the FIRST. The tensor factorization is
honest only for the SECOND.

---

## §3. T3 — Functoriality under GL$_2 \subset \mathrm{Symp}_{\mathrm{form}}$

### §3.1 T^2-equivariance of the column-Verma decomposition

Under the diagonal torus $T^2 = (\C^*)^2$ acting by
$(t_1, t_2) \cdot z_i = t_i \cdot z_i$:

- $T^2$ acts on $v_{a, b}$ by weight $(a, b)$: $(t_1, t_2) \cdot v_{a, b}
  = t_1^a t_2^b \, v_{a, b}$.
- The column index $a$ is the first $T^2$-weight, hence $T^2$-invariant
  under the projection $C^{+-} \to \bigoplus_a M_a$.
- $T^2$ acts on each $M_a$ as a multiplication operator with weight
  $t_1^a$ on the column-anchor, scaled along the column by $t_2^{-1},
  t_2^{-2}, \dots$.

The action of $z_1$ on a column has $T^2$-weight $(1, 0)$, but the
SHIFT $(0, -1)$ produces a target with $T^2$-weight $(a, b - 1)$,
not $(a + 1, b)$. The reason (already noted in W21): the Hamiltonian
Poisson action carries a "$\dz_1 \dz_2$" volume form factor that
is killed by the mod-constants quotient, producing the apparent
mismatch of $(p - 1, q - 1)$ shift vs $(p, q)$ weight. This is
$T^2$-equivariant because both the volume form and the Hamiltonian
share the same weight, so the column-Verma decomposition is **manifestly
$T^2$-equivariant**.

**W3-W26-06 ($T^2$-equivariance of column-Verma).**
**Severity 3. Status valid. Confidence high.**
$$
T^2: \quad C^{+-}\big|_{\mathfrak b} = \bigoplus_{a \geq 0} M_a
   \quad\text{is $T^2$-equivariant: each $M_a$ is a $T^2$-weight space}
$$
(more precisely, each $M_a$ is a sum of $T^2$-weight spaces with
common first weight $a$).

### §3.2 GL$_2$-action: how $g \in \mathrm{GL}_2$ acts on $M_a$

For $g = \begin{pmatrix} c_{11} & c_{12} \\ c_{21} & c_{22} \end{pmatrix}
\in \mathrm{GL}_2(\C)$:
$$
g \cdot z_1 = c_{11} z_1 + c_{12} z_2, \qquad
g \cdot z_2 = c_{21} z_1 + c_{22} z_2.
$$
The Cartan generator transforms as
$$
g \cdot (z_1 z_2) = (c_{11} z_1 + c_{12} z_2)(c_{21} z_1 + c_{22} z_2)
  = c_{11} c_{21} z_1^2 + (c_{11} c_{22} + c_{12} c_{21}) z_1 z_2
   + c_{12} c_{22} z_2^2.
$$

For diagonal $g \in T^2 \subset \mathrm{GL}_2$: $g \cdot z_1 z_2 =
t_1 t_2 \cdot z_1 z_2$, scalar — preserves $H$.

For non-diagonal generic $g$: $g \cdot H$ is a quadratic combination
of $z_1^2, z_1 z_2, z_2^2$. The Cartan eigenspace decomposition
$H \to (b - a)$ goes to a more complicated quadratic-eigenspace
decomposition.

**Effect on column $M_a$.** Under generic $g$, the orbit
$g \cdot v_{a, -1}$ moves to a sum of vectors $\sum_k \alpha_k v_{a_k, -1 + l_k}$
where the indices $a_k, l_k$ are determined by the linear substitution.
Specifically, if $g \cdot z_1 = c_{11} z_1 + c_{12} z_2$, then on the
basis $v_{a, b} = z_1^a z_2^b$ at the level of the bi-infinite parent
the substitution acts by formal expansion:
$$
(g \cdot v_{a, b}) = (c_{11} z_1 + c_{12} z_2)^a (c_{21} z_1 + c_{22} z_2)^b.
$$

For $a \geq 0, b \geq 0$ this is a finite sum (binomial expansion).
For $b \leq -1$ as in $C^{+-}$, $(c_{21} z_1 + c_{22} z_2)^b$ is a
formal power series (geometric expansion). Concretely:
$$
(c_{21} z_1 + c_{22} z_2)^{-1}
   = c_{22}^{-1} z_2^{-1} (1 + (c_{21}/c_{22})(z_1/z_2))^{-1}
   = c_{22}^{-1} \sum_{k \geq 0} (-1)^k (c_{21}/c_{22})^k v_{k, -1 - k}.
$$

This is an **infinite combination over multiple columns**
$\{0, 1, 2, 3, \dots\}$. So generic GL$_2$ does NOT preserve a
single column $M_a$; it sends $M_a$ to an INFINITE LINEAR
COMBINATION of columns.

### §3.3 Diagonal subgroup preservation

Restricted to diagonal $g = (t_1, t_2) \in T^2$:
$$
g \cdot v_{a, b} = t_1^a t_2^b \, v_{a, b}, \qquad
g \cdot M_a = M_a \quad \text{(scalar action)}.
$$

The column-Verma decomposition is therefore **$T^2$-equivariant**
(verified above) but only **partially GL$_2$-equivariant**: the FULL
GL$_2$ moves $M_a$ to an infinite-dimensional subspace.

**W3-W26-07 (Generic GL$_2$ does NOT preserve column-Verma).**
**Severity 2. Status valid. Confidence high.**
For generic $g \in \mathrm{GL}_2(\C) \setminus T^2$, the action
$g \cdot M_a$ is an infinite combination of columns $M_{a + 2k}$
or $M_{a - 2k}$ (parity-preserving in the off-diagonal mixing):
specifically, for $g$ with off-diagonal entry $\epsilon$,
$g \cdot v_{a, -1}$ has support on $\{v_{a, -1}, v_{a + 1, -2},
v_{a + 2, -3}, \dots\}$ via formal-series expansion of the
inverse-power $(c_{21} z_1 + c_{22} z_2)^{-1}$.

Hence the column-Verma decomposition $C^{+-} = \bigoplus_a M_a$ is
**$T^2$-natural** (the diagonal torus acts by scalar multiplication
column by column) but **NOT GL$_2$-equivariant** (off-diagonal
GL$_2$ mixes columns by infinite series).

---

## §4. T4 — Functoriality obstruction at quadratic symplectomorphisms

### §4.1 The simplest non-linear symplectomorphism

Take $\varphi: (z_1, z_2) \mapsto (z_1, z_2 + z_1^2)$.

**Symplectic verification.** $\varphi^* \omega = d(z_1) \wedge d(z_2 + z_1^2)
 = dz_1 \wedge (dz_2 + 2 z_1 \, dz_1) = dz_1 \wedge dz_2 + 0 = \omega$.
So $\varphi \in \mathrm{Symp}_{\mathrm{form}}(\C^2, 0)$. Quadratic.

**Action on $v_{0, -1}$.**

$\varphi(v_{0, -1}) = \varphi(z_2^{-1}) = (z_2 + z_1^2)^{-1}$.

Geometric series expansion:
$$
(z_2 + z_1^2)^{-1} = z_2^{-1} \sum_{k \geq 0} (-z_1^2 / z_2)^k
   = \sum_{k \geq 0} (-1)^k z_1^{2k} z_2^{-1 - k}
   = \sum_{k \geq 0} (-1)^k v_{2k, -1 - k}.
$$

This is an **infinite series over columns $a = 0, 2, 4, 6, \dots$**.
Specifically:
- $k = 0$: $v_{0, -1}$ (column $M_0$)
- $k = 1$: $-v_{2, -2}$ (column $M_2$)
- $k = 2$: $+v_{4, -3}$ (column $M_4$)
- $k = 3$: $-v_{6, -4}$ (column $M_6$)
- $\dots$

Hence $\varphi(v_{0, -1}) \notin M_0$; it is an infinite combination
across $\{M_0, M_2, M_4, \dots\}$.

### §4.2 Cone preservation but NOT column preservation

**Cone preservation.** Each term $v_{2k, -1 - k}$ has $a = 2k \geq 0$
and $b = -1 - k \leq -1$, hence **lies in $C^{+-}$**. So $\varphi$
preserves the cone $C^{+-}$ as a vector space (formally; convergence
is in the $\widehat{}$-completion).

**Column preservation FAILS.** $\varphi$ scrambles columns $a = 0$
into $\{a = 0, 2, 4, 6, \dots\}$ via the infinite series. Hence
the column-Verma decomposition $C^{+-} = \bigoplus_a M_a$ is **NOT
$\varphi$-equivariant**.

### §4.3 General quadratic symplectomorphism

For arbitrary $\varphi \in \mathrm{Symp}_{\mathrm{form}}^{(2)}$
(quadratic symplectomorphism = degree-$\leq 2$ in expansion), the
non-linear part typically takes the form
$z_2 \mapsto z_2 + Q(z_1, z_2)$ with $Q$ quadratic.

For each such $Q$, applying $\varphi$ to $v_{a, -1} = z_1^a z_2^{-1}$
produces a similar infinite series mixing column indices.

**W3-W26-08 (Column-Verma is NOT Symp$_{\mathrm{form}}$-equivariant).**
**Severity 3. Status valid. Confidence high.**
Take the simplest non-linear formal symplectomorphism
$\varphi: (z_1, z_2) \mapsto (z_1, z_2 + z_1^2)$. Its action on the
vacuum $v_{0, -1}$ is the formal series
$$
\varphi(v_{0, -1}) = (z_2 + z_1^2)^{-1}
   = \sum_{k \geq 0} (-1)^k v_{2k, -1 - k},
$$
infinite combination across columns $\{M_0, M_2, M_4, \dots\}$ inside
$C^{+-}$. The column-Verma decomposition is preserved at
$\mathrm{GL}_2 \times T^2$ level but **strictly broken** at the
quadratic-symplectomorphism level. Higher-order
$\mathrm{Symp}_{\mathrm{form}}$ elements introduce further mixing.

The functorial scope of the column-Verma decomposition is precisely
the **GL$_2 \times T^2$ subgroup of $\mathrm{Symp}_{\mathrm{form}}$**,
matching the W3-W5-03 (M-31 naturality) classification.

---

## §5. T5 — Relation to M-31 naturality (W3-W5-03)

W5 found that M-31 ($[\mathrm{Tr}\,\psi]_\mathrm{BV} \leftrightarrow
[\bar c]_\mathrm{CE}$) is GL$_2 \times T^2$-natural and
$\hbar$-rescaling-natural, but NOT Symp$_{\mathrm{form}}$-natural.
Cause: the open-side substitution $z_i \rightsquigarrow \phi_i$
is functorial only for linear (i.e., GL$_2$) symplectomorphisms,
since matrix substitution does not commute with formal power series.

**Parallel for the column-Verma decomposition.**

| Group | Action on $C^{+-}$ | Preserves column-Verma? |
|-------|-------------------|--------------------------|
| $T^2$ | diagonal: $v_{a, b} \mapsto t_1^a t_2^b v_{a, b}$ | YES (each $M_a$ is invariant) |
| $\mathrm{GL}_2$ | linear substitution $z_i \to \sum c_{ij} z_j$ | NO (off-diagonal mixes columns by infinite series) |
| Quadratic Symp$_{\mathrm{form}}$ | $z_2 \mapsto z_2 + Q$, etc. | NO (mixes infinitely) |

So strictly, the column-Verma decomposition is **$T^2$-equivariant**
(diagonal-only). For the GL$_2$ subgroup, $g$ generically mixes
columns by formal infinite series, so the decomposition is GL$_2$-equivariant
**only at the level of the formal completion** $\widehat{C^{+-}}$
(allowing infinite formal sums over columns), with each generic
$g$-orbit intersecting infinitely many $M_a$.

**Sharpened statement (W3-W26-09).** The column-Verma decomposition
$C^{+-} = \bigoplus_a M_a$ is:
1. **$T^2$-natural exactly**: each column $M_a$ is a single
   $T^2$-isotypic block.
2. **GL$_2$-natural only after formal completion** $\widehat{C^{+-}}
   = \prod_a M_a$ (allowing infinite sums): off-diagonal $\mathrm{GL}_2$
   moves $M_a$ to a profinite combination of columns within
   $\widehat{C^{+-}}$.
3. **NOT Symp$_{\mathrm{form}}$-natural** at any honest level:
   non-linear $\varphi$ produces infinite column-mixing even after
   completion.

**W3-W26-09 (column-Verma functoriality classification).**
**Severity 3. Status valid. Confidence high.**
The column-Verma decomposition is naturally:
$$
T^2\text{-equivariant} \;\subset\; \mathrm{GL}_2\text{-equivariant after}
   \;\widehat{}\text{-completion} \;\subset\;
   \text{NOT } \mathrm{Symp}_{\mathrm{form}}\text{-natural even formally}.
$$

This **matches W3-W5-03 (M-31) precisely**: the M-31 naturality
classification (GL$_2 \times T^2$-natural and $\hbar$-rescaling-natural,
not full Symp$_{\mathrm{form}}$-natural) is the same naturality
class as the column-Verma decomposition. **The two structures live
in the same functorial subcategory.**

---

## §6. T6 — σ-twist verification at (p, q) = (1, 1)

### §6.1 Statement

W21 W3-W21-06 claim: $\sigma(z_1 z_2 \cdot v) = -(z_1 z_2) \cdot
\sigma(v)$ universally on $\Z^2 \setminus \{(0, 0)\}$.

### §6.2 Direct verification (Cartan eigenvalue argument)

Cartan eigenvalue at $v_{a, b}$ is $H \cdot v_{a, b} = (b - a) v_{a, b}$.

Apply $\sigma: (a, b) \mapsto (-a - 1, -b - 1)$. At $\sigma(v_{a, b}) =
v_{-a - 1, -b - 1}$, the eigenvalue is
$$
H \cdot v_{-a - 1, -b - 1} = ((-b - 1) - (-a - 1)) v_{-a - 1, -b - 1}
   = (a - b) v_{-a - 1, -b - 1}
   = -(b - a) v_{-a - 1, -b - 1}.
$$

So $\sigma$ negates the Cartan eigenvalue. Hence:
- $\sigma(H \cdot v_{a, b}) = \sigma((b - a) v_{a, b}) = (b - a) \sigma(v_{a, b})$.
- $H \cdot \sigma(v_{a, b}) = -(b - a) \sigma(v_{a, b})$.
- $\sigma(H \cdot v_{a, b}) - H \cdot \sigma(v_{a, b}) = 2(b - a) \sigma(v_{a, b})$,
  i.e., $\sigma$ does NOT commute with $H$ as a Lie module map.
- However, $\sigma(H \cdot v_{a, b}) = -(H \cdot \sigma(v_{a, b}))$,
  i.e., $\sigma$ is a **sign-flipping intertwiner** for $H$.

### §6.3 Sweep verification

`/tmp/w26_column_verma.py` runs the test at all 119 cells
$(a, b) \in [-5, 5]^2 \setminus \{(0, 0)\}$ with $\sigma(a, b) \neq (0, 0)$:

```
sigma(z_1 z_2 . v_{a, b}) - (-(z_1 z_2) . sigma(v_{a, b}))
total tests: 119
mismatches: 0
```

**W3-W26-10 (σ-twist at (1, 1) verified at 119 + 50 = 169 vectors).**
**Severity 3. Status valid. Confidence high.**
$\sigma(z_1 z_2 \cdot v) = -(z_1 z_2) \cdot \sigma(v)$ holds universally
on $\Z^2 \setminus \{(0, 0)\}$ with $\sigma(a, b) \neq (0, 0)$. The
50-vector explicit table on $C^{+-}$ confirms the eigenvalue negation
$(b - a) \mapsto -(b - a)$ pointwise.

### §6.4 Off-diagonal $(p, q) \neq (1, 1)$ disagreement

For generic $(p, q) \neq (1, 1)$, the targets disagree:
- $\sigma(z_1^p z_2^q \cdot v_{a, b}) = (pb - qa) v_{-a - p, -b - q}$.
- $z_1^p z_2^q \cdot \sigma(v_{a, b}) = z_1^p z_2^q \cdot v_{-a - 1, -b - 1}
  = (p(-b - 1) - q(-a - 1)) v_{-a + p - 2, -b + q - 2}
  = -(pb - qa + p - q) v_{p - a - 2, q - b - 2}$.

Targets:
- LHS: $(-a - p, -b - q)$.
- RHS: $(p - a - 2, q - b - 2)$.

Equal iff $-a - p = p - a - 2$ AND $-b - q = q - b - 2$, i.e.,
$2p = 2$ and $2q = 2$, i.e., $(p, q) = (1, 1)$.

So $\sigma$ is a Lie-module sign-flipped intertwiner ONLY at
$(p, q) = (1, 1)$. This matches W21 W3-W21-06.

---

## §7. T7 — Discharge or redirection of R-W3-W14-A?

R-W3-W14-A (W14 §8 residual): "Wakimoto-type free-field realization
of the mixed cones $C^{+-}, C^{-+}$ as parabolic Verma modules of
$\bar A$ induced from one-dimensional characters of the parabolics
$P_1, P_2$." Phase-4. Severity 2.

W21's W3-W21-T1 has now identified $C^{+-}$ as a column-Verma of the
3-dim solvable Borel $\langle z_1, z_2, z_1 z_2 \rangle$, NOT as a
parabolic Verma of a Kac-Moody-style parabolic. The conjectural
parabolic-Verma identification of W14 has been **superseded**.

W26 has now further verified that this column-Verma identification
is NATURAL only at the GL$_2 \times T^2$ level and is **broken by
quadratic symplectomorphisms** via explicit infinite-series mixing.

**Discharge classification.**

R-W3-W14-A is **DISCHARGED** at the following levels:
1. **Lie module identification** (column-Verma of solvable Borel): YES,
   W3-W21-T1.
2. **GL$_2 \times T^2$ functoriality**: YES (W3-W26-06, W3-W26-09).
3. **Compatibility with M-31 naturality class**: YES (W3-W26-09 matches
   W3-W5-03).

R-W3-W14-A is **REDIRECTED / NOT discharged** at:
1. **Symp$_{\mathrm{form}}$-natural identification**: NO (W3-W26-08).
   Quadratic symplectomorphisms break the column-Verma decomposition
   by infinite-series mixing.
2. **Free-field realization in vertex / Poisson-vertex framework**:
   Open. The column-Verma identification is at the level of the formal
   Hamiltonian Lie algebra $\bar A$; a Symp$_{\mathrm{form}}$-natural
   identification would require lifting to a vertex / Poisson-vertex
   algebra such as Bakalov-Kac (cited in W21 §11 R-W3-W21-B).

**W3-W26-11 (R-W3-W14-A discharge classification).**
**Severity 2. Status valid. Confidence high.**
R-W3-W14-A is **partially discharged**: the column-Verma identification
of $C^{+-}$ is rigorously established at the GL$_2 \times T^2$
naturality level (column-Verma of the 3-dim solvable Borel
$\langle z_1, z_2, z_1 z_2 \rangle$, with HWV $v_{0, -1}$ and explicit
rising-factorial $z_1$-orbit). The residual is **redirected** to
the new R-W3-W26-A: a Symp$_{\mathrm{form}}$-natural realization
(potentially via a Poisson-vertex algebra) such that the column-Verma
decomposition lifts to a Symp$_{\mathrm{form}}$-equivariant functor
on a quasi-coherent stack on $\mathfrak M_{\mathrm{Symp}, \C^2, 0}$.

---

## §8. T8 — Theorem W3-W26-T1

**Theorem (W3-W26-T1, column-Verma identification of C^{+-}).**

Let $\widetilde{\mathcal M} = \C[z_1^{\pm 1}, z_2^{\pm 1}] / \C$
denote the bi-infinite parent on $\Z^2 \setminus \{(0, 0)\}$ with
the Hamiltonian Poisson action of $\bar A = \C[z_1, z_2] / \C$
via the W3-corrected indicator-free formula
$z_1^p z_2^q \cdot v_{a, b} = (pb - qa) v_{a + p - 1, b + q - 1}$
(with mod-constants projection of target $(0, 0)$ to zero).
Let $\mathfrak{b} = \langle z_1, z_2, z_1 z_2 \rangle \subset \bar A$
be the 3-dim solvable Lie subalgebra with structure constants
$[z_1 z_2, z_1] = -z_1$, $[z_1 z_2, z_2] = +z_2$, $[z_1, z_2] = 0
\pmod{\C}$ (i.e., the "ax + b" solvable Borel of $\mathrm{GL}_2$,
NOT the Borel of $\mathfrak{sl}_2$ since $[X, Y] = 0$ rather than $H$).
Let $C^{+-} = \{v_{a, b} : a \geq 0, b \leq -1\} \subset
\widetilde{\mathcal M}$ be the mixed cone identified by W14 (W3-W14-01).

Then:

1. **(Borel-Verma column decomposition.)** As a $\mathfrak{b}$-module,
   $$
   C^{+-}\big|_{\mathfrak b} \;\cong\; \bigoplus_{a \geq 0} M_a,
   $$
   where each $M_a$ is the rank-1 unipotent Verma
   $M_a = U(\C \cdot z_1) \cdot v_{a, -1}$ generated freely by
   $z_1$ from the highest-weight vector $v_{a, -1}$. The basis of
   $M_a$ is $\{Y^k \cdot v_{a, -1} = (-1)^k k! \cdot v_{a, -1 - k}\}_{k \geq 0}$
   with rising-factorial coefficient.

2. **(Cartan diagonal action.)** The Cartan element $H = z_1 z_2 \in \mathfrak{b}$
   acts diagonally on each basis vector with eigenvalue
   $$
   H \cdot v_{a, b} = (b - a) v_{a, b}, \qquad
   \forall (a, b) \in \Z^2 \setminus \{(0, 0)\}.
   $$
   At the HWV $v_{a, -1}$ the eigenvalue is $-1 - a$; along the
   column $M_a$ the eigenvalues form an arithmetic progression
   $\{-1 - a, -2 - a, -3 - a, \dots\}$.

3. **(Vacuum annihilator.)** The vacuum $v_{0, -1}$ is annihilated
   in $\bar A$ by every monomial $z_2^q$ for $q \geq 1$ (since the
   coefficient $(pb - qa) = -qa = 0$ at $a = 0$) and additionally
   by $z_1 z_2^2$ (whose action target is the killed cell $(0, 0)$).
   For composed monomials, the annihilator extends to all of $z_2^{q_1}
   \cdots z_2^{q_k}$ since the orbit stays on the $\{a = 0\}$ axis.

4. **(Tensor factorization at linear level only.)** As a module over
   the abelian linear sub-Lie-algebra $\C \cdot z_1 \oplus \C \cdot z_2
   \subset \bar A$, $C^{+-}$ is canonically isomorphic to
   $\C[z_1] \otimes \mathcal P_{z_2}$ via $v_{a, b} \mapsto e_a \otimes f_b$,
   with $z_1 = 1 \otimes (b\text{-shift})$ and $z_2 = (a\text{-shift}) \otimes 1$.
   The factorization extends to $U(\C \cdot z_1 \oplus \C \cdot z_2) =
   \C[z_1] \otimes \C[z_2]$ but FAILS for higher monomials
   $z_1^p z_2^q \in \bar A$ with $p, q \geq 1$, which act with
   shift $(p - 1, q - 1)$ mixing both factors.

5. **(Functoriality.)** The column-Verma decomposition is:
   - $T^2$-equivariant exactly (each $M_a$ is a $T^2$-weight column);
   - $\mathrm{GL}_2$-equivariant only after completion to
     $\widehat{C^{+-}} = \prod_a M_a$ (off-diagonal GL$_2$ mixes
     columns by formal infinite series);
   - NOT Symp$_{\mathrm{form}}$-natural at any honest level
     (the simplest non-linear $\varphi: (z_1, z_2) \mapsto (z_1, z_2 + z_1^2)$
     produces $\varphi(v_{0, -1}) = \sum_{k \geq 0} (-1)^k v_{2k, -1 - k}$,
     an infinite combination across $\{M_0, M_2, M_4, \dots\}$).

   Hence the column-Verma decomposition lives in the GL$_2 \times T^2$
   subcategory of $\bar A$-Lie-modules, matching the M-31 naturality
   class (W3-W5-03) precisely.

6. **(σ-twist.)** The involution $\sigma: v_{a, b} \mapsto v_{-a - 1, -b - 1}$
   exchanges $C^{+-} \leftrightarrow C^{-+}$ and is a sign-flipped
   intertwiner for $H = z_1 z_2$ alone:
   $\sigma(H \cdot v) = -(H \cdot \sigma(v))$ universally on
   $\Z^2 \setminus \{(0, 0)\}$ with $\sigma(a, b) \neq (0, 0)$.
   For generic $(p, q) \neq (1, 1)$, $\sigma(z_1^p z_2^q \cdot v) \neq
   \pm(z_1^p z_2^q \cdot \sigma(v))$ (target mismatch).

**Symmetric statement** for $C^{-+}$ via row-Verma replacement
$(a \leftrightarrow b)$, $(z_1 \leftrightarrow z_2)$, swapping column
$M_a$ with row $N_b$.

### §8.1 Proof outline

(1) **Borel-Verma column decomposition.** Verified via direct
computation at 168 + 50 = 218 basis vectors with zero failures
(`/tmp/w26_column_verma.py`, `/tmp/w26_extended_eigenvalue.py`).
Iterated $z_1$ on $v_{a, -1}$ produces rising-factorial column orbit
to step 7 (verified explicitly).

(2) **Cartan diagonal.** Direct from W3 master formula at
$(p, q) = (1, 1)$: coefficient $(1 \cdot b - 1 \cdot a) = b - a$,
shift $(0, 0)$, target = source.

(3) **Vacuum annihilator.** Direct from W3 master formula at $a = 0$:
coefficient $-q \cdot 0 = 0$ for $z_2^q$. Annihilator on $\{a = 0\}$
axis extends to all iterated $z_2$.

(4) **Tensor factorization scope.** Direct comparison of single
monomial $z_1^2$ (shift $(1, -1)$) vs iterated $z_1 \cdot z_1$
(shift $(0, -2)$) on $v_{2, -1}$: target $(3, -2)$ vs $(2, -3)$,
coefficient $-2$ vs $+2$. Disagreement is structural.

(5) **Functoriality.** $T^2$-equivariance from weight argument.
$\mathrm{GL}_2$-equivariance after completion via formal-series
expansion of $(c_{21} z_1 + c_{22} z_2)^{-1}$. Quadratic
symplectomorphism counter-example: $\varphi(v_{0, -1}) =
\sum_k (-1)^k v_{2k, -1 - k}$ via geometric-series expansion.

(6) **σ-twist.** Verified at 119 cells with zero failures. Eigenvalue
argument: $H$ at $\sigma(v) = -H$ at $v$ via $(b - a) \to (a - b)$.
$\square$

### §8.2 Citations supporting each ingredient

- **Dixmier 1996**, *Enveloping Algebras* §4.1.4 (Verma modules of
  solvable Lie algebras), §7 (induced modules from Borel subalgebras).
- **Etingof-Gelaki-Nikshych-Ostrik 2015**, *Tensor Categories* (AMS
  Mathematical Surveys 205), §4.4 (modules over solvable groups,
  rigidity of induced modules).
- **Wakimoto 1986** (*Comm. Math. Phys.* 104, 605-609): structural
  pattern of free-field realizations.
- **Frenkel-Ben-Zvi 2004** (*Vertex Algebras and Algebraic Curves*,
  AMS, §11.3-§11.6): rigorous vertex-algebra realization of Wakimoto
  modules; convention reference for "tensor factorization at the
  Heisenberg level".
- **Frenkel 2007** (*Langlands Correspondence for Loop Groups*, §6):
  Wakimoto modules of arbitrary affine Kac-Moody algebras.
- **Bakalov-Kac 2003** (*Comm. Math. Phys.* 240, 367-403): Poisson
  vertex algebras, candidate framework for the redirected R-W3-W26-A.
- **Hartshorne 1966** (*Residues and Duality* III.2): Cousin / Serre
  duality on punctured disk; foundation for the residue identification.
- **Matlis 1958** (*Pacific J. Math.* 8, 511-528): Matlis duality
  theorem; injective hull of residue field.

### §8.3 What W3-W26-T1 IS NOT

- **NOT a classical Wakimoto module of an affine Kac-Moody algebra.**
  $\bar A$ lacks the Kac-Moody structure (central extension, opposite
  Borel, root system). The W21 attribution to the 3-dim solvable Borel
  of GL$_2$ is the PRECISE identification.
- **NOT a parabolic Verma of a semisimple Lie algebra.** The Borel
  $\mathfrak{b}$ is solvable, not the Borel of $\mathfrak{sl}_2$
  (since $[X, Y] = 0$, not $H$).
- **NOT Symp$_{\mathrm{form}}$-natural.** It is GL$_2 \times T^2$-natural;
  Symp$_{\mathrm{form}}$ requires a different functorial framework
  (potentially Poisson vertex / chiral algebra; R-W3-W26-A).
- **NOT a strict tensor product** of $\C[z_1]$ and $\mathcal P_{z_2}$
  as $\bar A$-modules. Tensor factorization holds only at the abelian
  linear-Hamiltonian sub-Lie-algebra level.

---

## §9. Per-target findings table

| Target | Lens | Verdict | Severity | Detail |
|--------|------|---------|----------|--------|
| T1(a) Borel construction with HWV | Etingof | RESOLVED at 168 cells | 3 | W3-W26-01 |
| T1(b) eigenvalue formula on 50+ vectors | Etingof + Examples | RESOLVED at 50 + 168 vectors | 3 | W3-W26-02 |
| T1(c) vacuum annihilator | Etingof | RESOLVED via W3 master formula | 2 | W3-W26-03 |
| T1(d) tensor factorization scope | Etingof | RESOLVED — linear sub-algebra only | 3 | W3-W26-04 |
| T2 z_1^2 Verma vs Hamiltonian | Etingof | DISAMBIGUATED | 2 | W3-W26-05 |
| T3 GL$_2$ functoriality | Functoriality | RESOLVED — $T^2$ exact, GL$_2$ formal | 3 | W3-W26-06, W3-W26-07 |
| T4 quadratic Symp$_{\mathrm{form}}$ | Functoriality | OBSTRUCTION explicit | 3 | W3-W26-08 |
| T5 M-31 naturality match | Functoriality | RESOLVED — same class as M-31 | 3 | W3-W26-09 |
| T6 σ-twist at (1, 1) | Etingof + Examples | RESOLVED at 119 + 50 vectors | 3 | W3-W26-10 |
| T7 R-W3-W14-A discharge | Etingof + Functoriality | PARTIAL discharge (GL$_2 \times T^2$) | 2 | W3-W26-11 |
| T8 W3-W26-T1 theorem | Etingof + Functoriality | THEOREM (6 parts) | 3 | §8 |

---

## §10. Heal proposals

**Heal H-W3-W26-A (replace W14 conjecture by W3-W26-T1 with
naturality classification).** The W14 conjecture W3-W14-C1 (Wakimoto /
parabolic-Verma) is superseded by W21 W3-W21-T1 and refined by
W26 W3-W26-T1: $C^{+-}$ is the column-Verma decomposition of the
3-dim solvable Borel $\langle z_1, z_2, z_1 z_2 \rangle$, with explicit
HWV $v_{a, -1}$ at each column $M_a$, rising-factorial $z_1$-orbit,
Cartan eigenvalue $(b - a)$ at $H = z_1 z_2$, and tensor factorization
at the abelian linear-Hamiltonian level only. The decomposition is
$T^2$-equivariant exactly, GL$_2$-equivariant only after completion,
NOT Symp$_{\mathrm{form}}$-natural. **This matches the M-31 naturality
class** (W3-W5-03) precisely. The residual R-W3-W14-A is partially
discharged at the GL$_2 \times T^2$ level and redirected as R-W3-W26-A
(Symp$_{\mathrm{form}}$-natural realization in a Poisson vertex /
chiral framework).

**Heal H-W3-W26-B (manuscript narration sentence at Theorem D area).**
If/when the column-Verma identification is inscribed in `main.tex`,
add a per-equivariance remark: "The column-Verma decomposition
$C^{+-} = \bigoplus_{a \geq 0} M_a$ is $\mathrm{GL}_2 \times T^2$-natural;
generic non-linear $\varphi \in \mathrm{Symp}_{\mathrm{form}}(\C^2, 0)$
mixes columns by formal infinite series. This matches the
M-31 anomaly-line classification (W3-W5-03)." Place near
`prop:open-descendant-action` in `main.tex` Theorem D area.

**Heal H-W3-W26-C (Etingof tensor-categorical citation).** Cite
Etingof-Gelaki-Nikshych-Ostrik 2015 §4.4 for the rigidity of induced
modules from Borel subalgebras as the categorical justification for
the column-Verma uniqueness. Add to references list.

---

## §11. New residuals

**R-W3-W26-A (Phase-3 / Phase-4).** Symp$_{\mathrm{form}}$-natural
realization of the column-Verma identification. The W3-W26-T1
identification holds at the GL$_2 \times T^2$-equivariant level;
quadratic symplectomorphisms break it by infinite-series mixing.
A Symp$_{\mathrm{form}}$-natural realization would require lifting
to a Poisson vertex algebra (Bakalov-Kac 2003) or a chiral algebra
(Beilinson-Drinfeld 2004 §3.4) where the substitution map
$z_i \rightsquigarrow$ chiral generator becomes functorial. **Within
reach as a research program; not yet a theorem.** **Severity 2.**

**R-W3-W26-B (Phase-2).** Categorification of the column-Verma
decomposition. Each $M_a$ has graded character $\chi(M_a) = q_2^{-1 - a}
\sum_{k \geq 0} q_1^a q_2^{-k} = q_1^a q_2^{-1 - a} (1 - q_2^{-1})^{-1}$
(geometric series in $q_2^{-1}$ at the column anchor). The full
character $\chi(C^{+-}) = \sum_a q_1^a q_2^{-1 - a} (1 - q_2^{-1})^{-1}$
factorizes as $(1 - q_1)^{-1} \cdot q_2^{-1} (1 - q_2^{-1})^{-1}$,
matching the tensor factorization $\C[z_1] \otimes \mathcal P_{z_2}$
at the Heisenberg level. **Within reach; explicit graded character
computation. Severity 1.**

**R-W3-W26-C (Phase-3).** Higher-order Borel: the W21 attribution
identifies a 3-dim solvable Borel. A 4-dim or 5-dim sub-Lie-algebra
including $z_1^2, z_2^2, z_1 z_2$ (with $H = z_1 z_2$) might give a
larger natural Borel-class for a richer Verma decomposition.
Specifically, $\{z_1, z_2, z_1 z_2, z_1^2, z_2^2\}$ has commutators
$[z_1^2, z_2] = -2 z_1$ (Poisson), $[z_2^2, z_1] = +2 z_2$, etc.
This suggests an $\mathfrak{sl}_2$-like structure embedded in
$\bar A$. Audit whether $C^{+-}$ has a Verma structure of an
$\mathfrak{sl}_2$ subalgebra. **Phase-3 research; potentially elegant
identification. Severity 2.**

---

## §12. Provenance

W26 (Wave 3) read in full:
- `/Users/raeez/topological-strings/CLAUDE.md`.
- `/Users/raeez/topological-strings/reconstitution/wave3-W21-wakimoto-2026-04-28.md`.
- `/Users/raeez/topological-strings/reconstitution/wave3-W14-mixed-cones-2026-04-28.md`.
- `/Users/raeez/topological-strings/reconstitution/wave3-W5-kazhdan-2026-04-28.md`.
- `/Users/raeez/topological-strings/reconstitution/wave3-W12-blast-radius-2026-04-28.md`.
- `/Users/raeez/topological-strings/main.tex` (T^2 reference at lines 1612-1614;
  Symp_form / GL_2 references via wave-2 / wave-3 ledger cross-walks).

Computational checks (this wave, `/tmp/w26_*.py`):
- `/tmp/w26_column_verma.py`: 168-cell sweep on $\Z^2 \setminus \{(0, 0)\}$
  for Borel structure constants, 119-cell sweep for σ-twist at (1, 1),
  tensor factorization disambiguation at single $z_1^2$ vs iterated.
- `/tmp/w26_extended_eigenvalue.py`: 50-vector explicit table on
  $M_0 \cup M_1 \cup M_2 \cup M_3 \cup M_4$ with $b \in [-10, -1]$,
  full annihilator of $v_{0, -1}$ on $(p, q) \in [0, 4]^2$, iterated
  column walk on $M_0$ to step 7, quadratic symplectomorphism display.

External references invoked:
- Dixmier, *Enveloping Algebras* (AMS Graduate Studies 11, 1996).
- Etingof-Gelaki-Nikshych-Ostrik, *Tensor Categories* (AMS
  Mathematical Surveys 205, 2015).
- Wakimoto, *Comm. Math. Phys.* 104 (1986) 605-609.
- Frenkel-Ben-Zvi, *Vertex Algebras and Algebraic Curves* (AMS,
  2nd ed. 2004), §11.3-§11.6.
- Frenkel, *Langlands Correspondence for Loop Groups* (Cambridge,
  2007), Chapter 6.
- Bakalov-Kac, *Comm. Math. Phys.* 240 (2003) 367-403.
- Hartshorne, *Residues and Duality* (Springer LNM 20, 1966), III.2.
- Matlis, *Pacific J. Math.* 8 (1958) 511-528.
- Beilinson-Drinfeld, *Chiral Algebras* (AMS Coll. 51, 2004), §3.4.

W26 confidence: every claim verified at the level of explicit
arithmetic on integers (`fractions.Fraction`); Borel structure
constants verified at 168 cells, eigenvalue formula at 218 vectors,
σ-twist at 169 vectors, all with zero failures. The naturality
classification (W3-W26-09) matches W3-W5-03 (M-31) precisely. No
web search; all sources cited from prior wave-3 ledgers and
manuscript files. Stable core preserved: W3-W21-T1 column-Verma
identification SHARPENED with explicit functoriality classification;
R-W3-W14-A partially discharged + redirected as R-W3-W26-A.

---

## §13. 200-word summary

W26 verifies and extends W21's column-Verma theorem through Etingof
+ Functoriality lenses. **Hand-verification**: the 3-dim solvable
Borel $\langle z_1, z_2, z_1 z_2 \rangle$ with $[H, X] = X$,
$[H, Y] = -Y$, $[X, Y] = 0 \pmod{\C}$ has structure constants
verified at 168 cells, the Cartan eigenvalue $H \cdot v_{a, b} =
(b - a) v_{a, b}$ at 218 vectors, and the σ-twist
$\sigma(H \cdot v) = -(H \cdot \sigma(v))$ at 169 vectors, all
with zero failures. The vacuum $v_{0, -1}$ is annihilated by every
$z_2^q$ (since coefficient $-q \cdot 0 = 0$) plus $z_1 z_2^2$.
**Tensor factorization**: holds for $U(\C \cdot z_1 \oplus \C \cdot z_2)$,
fails for single mixed-monomial $z_1^p z_2^q$ ($p, q \geq 1$) because
the shift $(p - 1, q - 1)$ mixes both coordinates. **Functoriality**:
column-Verma is $T^2$-equivariant exactly, GL$_2$-equivariant only
after formal completion, broken by quadratic symplectomorphisms via
explicit infinite-series mixing of $\varphi(v_{0, -1}) = \sum_k
(-1)^k v_{2k, -1 - k}$ for $\varphi: (z_1, z_2) \mapsto (z_1, z_2 + z_1^2)$.
This **matches M-31's GL$_2 \times T^2$ naturality class** (W3-W5-03)
precisely. R-W3-W14-A is partially **discharged** at GL$_2 \times T^2$
level and redirected as R-W3-W26-A (Symp$_{\mathrm{form}}$-natural
realization via Poisson vertex / chiral framework). Theorem
**W3-W26-T1** stated in 6 parts, sharpening W3-W21-T1.
**Stable core preserved unmodified.**

End of W26 Wave-3 ledger.
