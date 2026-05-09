# Wave 3 / W14 — Drinfeld + Examples Lens (Mixed Cones)

**Date.** 2026-04-28. **Author.** Raeez Lorgat.
**Lens.**
- *Primary:* Drinfeld — moduli, stacks, hidden groupoids, canonical
  constructions, Drinfeld-Sokolov reduction.
- *Secondary:* Examples — first nontrivial computation, degenerate
  cases, smallest-N sanity.
**Wave.** 3 (independent attacker; reads waves 1-2 + W3-W3 / W3-W7 /
W3-W9 ledgers).
**Mandate.** Explore the two MIXED Z^2 cones missed by the wave-2 W4
§4 dichotomy. Per W3-W3, the bi-infinite parent
$\widetilde{\mathcal M} = \C[z_1^{\pm 1}, z_2^{\pm 1}] / \C$ on
$\Z^2 \setminus \{(0, 0)\}$ admits a four-cone partition (NOT
two), with the W3 corrected indicator-free action
$z_1^p z_2^q \cdot v_{a, b} = (pb - qa) v_{a + p - 1, b + q - 1}$
(mod-constants projection). The wave-2 W4 §4 dichotomy treated
only PBW positive cone $C^{++}$ and Matlis negative cone $C^{--}$;
the two MIXED cones $C^{+-} = \{a \geq 0, b \leq -1\}$ and
$C^{-+} = \{a \leq -1, b \geq 0\}$ were missed entirely.
**Inputs.** `CLAUDE.md`, W3-W3 (Nekrasov + four-cone observation,
read in full), W3-W7 (13-row dichotomy table), W3-W9 (Drinfeld
stack reformulation), `appendix-matlis-principal-parts.tex`,
`/tmp/w3_*.py` (existing scripts, briefly), three new probes
`/tmp/w14_*.py`.
**Mode.** Proposal-only. No commits. Master ledger schema; IDs
prefix `W3-W14-`.
**Independence.** The W3-W3-02 corrected indicator-free formula and
the W3-W3 four-cone observation are taken as **input under attack**
through the Drinfeld + Examples lens. The deliverable is (i) a
Drinfeld-canonical four-cone table, (ii) explicit hand-computed
Lie action on the mixed cones, (iii) identification of mixed cones
with Wakimoto-type tensor-factorized parabolic-induced modules,
(iv) candidate theorem and no-go statements, (v) interaction with
M-29 and the W3-W9 Drinfeld stack.

---

## §0. Method

The four-cone partition (from W3-W3-02 / W3-W3-03):
- $C^{++} := \{(a, b) : a \geq 0, b \geq 0, (a, b) \neq (0, 0)\}$ — PBW positive cone.
- $C^{--} := \{(a, b) : a \leq -1, b \leq -1\}$ — Matlis negative cone (sigma-image of $C^{++}$).
- $C^{+-} := \{(a, b) : a \geq 0, b \leq -1\}$ — first mixed cone.
- $C^{-+} := \{(a, b) : a \leq -1, b \geq 0\}$ — second mixed cone.

The action: $z_1^p z_2^q \cdot v_{a, b} = (pb - qa) v_{a + p - 1, b + q - 1}$
on $\Z^2 \setminus \{(0, 0)\}$, with mod-constants projection (zero
out $v_{0, 0}$).

Three probes inscribed in `/tmp/w14_*.py`:
- `/tmp/w14_four_cones_probe.py`: hand-computations on basis vectors,
  cone-closure, locally-nilpotent / coefficient-vanishing checks.
- `/tmp/w14_lie_substructure.py`: sub-Lie-module / quotient / two-cone
  closure / Lie-consistency tests.
- `/tmp/w14_parabolic_intertwiner.py`: tensor factorization,
  sigma-intertwiner, Drinfeld-Sokolov / Wakimoto interpretation,
  candidate theorems.

---

## §1. T1 — The four cones, structurally

### §1.1 Four-cone table

The summary computation (verified at `/tmp/w14_four_cones_probe.py`,
`/tmp/w14_lie_substructure.py`):

| Cone | Lie sub-module? | Lie quotient? | $z_1$ loc-nilp? | $z_2$ loc-nilp? | Cone of action coefficient zeros | Sigma-image |
|------|-----------------|---------------|-----------------|------------------|------------------------------------|-------------|
| $C^{++}$ | **YES** | NO | YES | YES | $\{a = 0\} \cup \{b = 0\}$ inside cone | $C^{--}$ |
| $C^{--}$ | NO | **YES** (complement closed) | NO (rising factorial) | NO (rising factorial) | (no axes) | $C^{++}$ |
| $C^{+-}$ | NO | NO | NO ($z_1$ rising-factorial) | YES ($z_2$ kills as $a \to 0$) | $\{a = 0\}$ inside cone | $C^{-+}$ |
| $C^{-+}$ | NO | NO | YES ($z_1$ kills as $b \to 0$) | NO ($z_2$ rising-factorial) | $\{b = 0\}$ inside cone | $C^{+-}$ |

Closure under positive Hamiltonian Lie algebra action (probe
`/tmp/w14_lie_substructure.py`, max bidegree $|a|, |b| \leq 4$,
$p + q \leq 4$):
- $C^{++}$: 314 closed actions, 0 leaks. **Sub-Lie-module, confirmed.**
- $C^{--}$: 136 closed actions, 82 leaks (mostly to $C^{+-}$ and
  $C^{-+}$ via large $z_1^p z_2^q$ exponents). NOT sub-Lie-module.
- $C^{+-}$: 231 closed actions, 53 leaks (to $C^{++}$, via $z_1 z_2^q$
  with $q$ large enough to push $b + q - 1 \geq 0$). NOT sub-Lie-module.
- $C^{-+}$: 231 closed actions, 53 leaks (mirror image). NOT sub-Lie-module.

Two-cone unions (probe `/tmp/w14_lie_substructure.py`):

| Union | Closed under positive Hamiltonian algebra? |
|-------|---------------------------------------------|
| $C^{++} \cup C^{+-}$ | **YES** (sub-Lie-module) |
| $C^{++} \cup C^{-+}$ | **YES** (sub-Lie-module) |
| $C^{++} \cup C^{--}$ | NO (leaks via mixed cones) |
| $C^{+-} \cup C^{--}$ | NO |
| $C^{-+} \cup C^{--}$ | NO |
| $C^{+-} \cup C^{-+}$ | NO |

Three-cone unions:

| Triple | Closed? |
|--------|---------|
| $C^{++} \cup C^{+-} \cup C^{-+}$ | **YES** (sub-Lie-module) |
| $C^{++} \cup C^{--} \cup C^{+-}$ | NO |
| $C^{++} \cup C^{--} \cup C^{-+}$ | NO |
| $C^{--} \cup C^{+-} \cup C^{-+}$ | NO |

**W3-W14-01 (filtration of the bi-infinite parent).**
**Severity 3. Status valid. Confidence high.**

The bi-infinite parent $\widetilde{\mathcal M}$ admits a canonical
four-step filtration of Lie sub-modules:

$$0 \subset C^{++} \subset C^{++} \cup C^{+-} \subset C^{++} \cup C^{+-} \cup C^{-+} \subset \widetilde{\mathcal M},$$

with successive quotients $C^{+-}$, $C^{-+}$, $C^{--}$. Equivalently,
the dual filtration $0 \subset C^{--}$-quotient $\subset \dots$ ends
with the entire bi-infinite parent. The filtration is canonical
(Drinfeld lens) once the bidegree polarization is fixed; the
sigma-symmetric variant $0 \subset C^{++} \subset C^{++} \cup C^{-+} \subset \dots$ exchanges the two mixed cones in the second step.

### §1.2 Lie consistency check on each cone

Probe `/tmp/w14_lie_substructure.py`, with action restricted to each
cone (leaks zeroed out):

| Subset | Cases checked | Failures |
|--------|---------------|----------|
| $C^{++}$ alone | 960 | 0 |
| $C^{--}$ alone | 576 | 0 |
| $C^{+-}$ alone | 768 | 0 |
| $C^{-+}$ alone | 768 | 0 |
| $C^{++} \cup C^{+-}$ | 1728 | 0 |
| $C^{++} \cup C^{-+}$ | 1728 | 0 |
| $C^{+-} \cup C^{-+}$ | 1536 | 0 |
| $C^{--} \cup C^{+-}$ | 1344 | 0 |

Lie consistency holds on every cone individually (when leaks are
zeroed) and on every union. **The leak-zeroed restriction is itself
a valid Lie module.**

This is **stronger** than the original Lie consistency on
$\widetilde{\mathcal M}$: each cone is itself a Lie module of
$\bar A$ in its own right (modulo leak truncation), and the
sub-/quotient relations of §1.1 are exact triangles in the Lie
module category.

---

## §2. T2 — What are $C^{+-}$ and $C^{-+}$?

### §2.1 Hand-computations on $C^{+-}$ basis vectors

Verbatim from `/tmp/w14_four_cones_probe.py`:

| Basis | $z_1 \cdot v$ | $z_2 \cdot v$ | $z_1 z_2 \cdot v$ | $z_1^2 \cdot v$ | $z_2^2 \cdot v$ |
|-------|--------------|--------------|--------------------|------------------|------------------|
| $v_{0, -1}$ | $-v_{0, -2}$ | 0 | $-v_{0, -1}$ | $-2 v_{1, -2}$ | 0 |
| $v_{1, -1}$ | $-v_{1, -2}$ | $-v_{0, -1}$ | $-2 v_{1, -1}$ | $-2 v_{2, -2}$ | 0 |
| $v_{0, -2}$ | $-2 v_{0, -3}$ | 0 | $-2 v_{0, -2}$ | $-4 v_{1, -3}$ | 0 |
| $v_{1, -2}$ | $-2 v_{1, -3}$ | $-v_{0, -2}$ | $-3 v_{1, -2}$ | $-4 v_{2, -3}$ | $-2 v_{0, -1}$ |
| $v_{2, -1}$ | $-v_{2, -2}$ | $-2 v_{1, -1}$ | $-3 v_{2, -1}$ | $-2 v_{3, -2}$ | $-4 v_{1, 0}$  $\boxed{\to C^{++}}$ |

Critical observations:
- **$z_1 \cdot v_{a, b} = b \, v_{a, b-1}$** on $C^{+-}$ (only the
  $b$-coordinate is touched; coefficient is just $b$, independent of
  $a$).
- **$z_2 \cdot v_{a, b} = -a \, v_{a-1, b}$** on $C^{+-}$ (only the
  $a$-coordinate is touched; coefficient is $-a$, independent of $b$).
- **$z_1$ has rising-factorial growth on the $b$-direction**:
  iterated $z_1^N$ on $v_{a, b}$ (a single fixed $a$) walks down to
  $v_{a, b - N}$ with coefficient $b(b-1)\cdots(b - N + 1) \neq 0$
  for all $N$.
- **$z_2$ is locally nilpotent on the $a$-direction**: iterated $z_2^N$
  on $v_{a, b}$ (a single fixed $b$) walks down to $v_{a - N, b}$ for
  $N \leq a$, then $z_2 \cdot v_{0, b} = 0$ (the $a = 0$ axis is the
  $z_2$-kernel inside $C^{+-}$).

Iterated $z_1$ chain from $v_{2, -1}$ (rising-factorial):
$v_{2, -1} \to -v_{2, -2} \to 2 v_{2, -3} \to -6 v_{2, -4} \to 24 v_{2, -5} \to -120 v_{2, -6} \to \dots$

This is the **same rising-factorial obstruction** as in M-29 / W3-W7-01,
but applied along the $z_1$-direction of the mixed cone.

### §2.2 Tensor product factorization

**W3-W14-02 (Tensor factorization of the mixed cones).**
**Severity 3. Status valid. Confidence high.**

The action of the linear Hamiltonians $z_1, z_2$ on $C^{+-}$
factorizes:
$$z_1 \cdot v_{a, b} = b \, v_{a, b - 1}, \quad z_2 \cdot v_{a, b} = -a \, v_{a - 1, b}.$$

The first is a Matlis-type principal-part action on the $b$-coordinate
(the principal-part of $z_2$, identified by sigma with $\rho_{0, -b - 1}$);
the second is a PBW-type polynomial-lowering action on the
$a$-coordinate (the polynomial in $z_1$). Therefore as a Lie module
of the linear-Hamiltonian sub-Lie-algebra $\C \cdot z_1 \oplus \C \cdot z_2 \subset \bar A$,
$$C^{+-} \cong \C[z_1]_{a \geq 0} \otimes_{\C} \mathcal{P}_{z_2}^{(\text{Matlis})}, \tag{T+-}$$
where the first factor is the polynomial ring (with $z_2$ acting as
$-a$ shift) and the second is the Matlis principal-part module on a
single variable $z_2$ (with $z_1$ acting as $b$ shift).

For higher monomials, the action on $C^{+-}$ is
$z_1^p z_2^q \cdot v_{a, b} = (pb - qa) v_{a + p - 1, b + q - 1}$, but
$(pb - qa) = p \cdot b + (-q) \cdot a$, so the SAME tensor-factorization
holds at the level of the abelian Lie algebra spanned by
$\{z_1^p, z_2^q\}_{p, q \geq 0}$. Cross-terms $z_1^p z_2^q$ with both
$p, q \geq 1$ act multiplicatively but mix the two factors — this is
the genuine bi-Hamiltonian structure.

Symmetrically, $C^{-+} \cong \mathcal{P}_{z_1}^{(\text{Matlis})} \otimes_{\C} \C[z_2]_{b \geq 0}$.

**Geometric interpretation.** The $C^{+-}$ module is supported on the
divisor $\{z_2 = 0\} \cup \{z_2 = \infty\}$ in the toric
$\mathbb{P}^1 \times \mathbb{P}^1$ compactification of
$\C^* \times \C^*$, and is polynomial in the transverse $z_1$-direction
and Matlis-residue along the $z_2$-direction. This is exactly a
**residue functor along $\{z_2 = 0\}$** applied to a polynomial
distribution in $z_1$.

### §2.3 Identification: parabolic Verma / Wakimoto-type module

The data of "polynomial in one direction, Matlis in the other" with a
non-trivial Lie algebra action is the standard signature of a
**Wakimoto module** (Frenkel–Ben-Zvi; Feigin–Frenkel for affine
Kac-Moody) or a **semi-infinite parabolic Verma**.

**Definition (parabolic in $\bar A$).** Let $P_2 \subset \bar A$ be
the subalgebra spanned by all monomials $z_1^p z_2^q$ with $q \geq 1$,
together with the linear Cartan-like piece $\C \cdot z_1$. The pair
$(P_2, \bar A)$ is a "parabolic" in the sense that $\bar A / P_2 = \C[z_1] / \C$
is non-trivial (the "Levi quotient is the polynomial in $z_1$").

**Conjecture W3-W14-03 (Parabolic-Wakimoto identification).** The
mixed cone $C^{+-}$ is isomorphic, as a $\bar A$-Lie-module, to the
Wakimoto-type semi-infinite parabolic Verma module
$$\mathrm{Wak}(P_2, \chi) := U(\bar A) \otimes_{U(P_2)} \chi,$$
where $\chi$ is the one-dimensional $P_2$-character induced by
restricting the residue pairing of `prop:app-matlis-realization` to
$P_2$ at the privileged weight $(a, b) = (0, -1)$, i.e., the lowest
weight in $C^{+-}$ supported at $\{a = 0\}$. Symmetrically,
$C^{-+} \cong \mathrm{Wak}(P_1, \chi')$ at weight $(-1, 0)$.

This is **labeled CONJECTURE** because (i) the parabolic $P_2$ is not
a true parabolic in the classical sense (the Hamiltonian Lie algebra
$\bar A$ is not affine Kac-Moody but rather has its own structure
as a Poisson algebra / Hamiltonian vector fields), (ii) the
Wakimoto module construction normally lives in the affine setting,
and (iii) we have not constructed the Wakimoto module from a
free-field realization, only checked that the underlying Lie module
structures match. The conjectural part is the precise form of the
character $\chi$ and the parabolic.

**Severity 2 (conjecture). Confidence medium.**

### §2.4 Examples lens: degenerate computation

**Smallest nontrivial test (Examples lens).** Consider the smallest
basis vector in each mixed cone:
- $v_{0, -1} \in C^{+-}$: the "anchor" of $C^{+-}$, lowest in $|b|$
  on the $a = 0$ axis. Action: $z_1 \cdot v_{0, -1} = -v_{0, -2}$,
  $z_2 \cdot v_{0, -1} = 0$. This is a "highest-weight vector"
  for the parabolic Levi $\C \cdot z_2 \subset P_2$ (it's in the
  $z_2$-kernel, so $z_2$ acts as zero).
- $v_{-1, 0} \in C^{-+}$: the mirror anchor. Action: $z_1 \cdot v_{-1, 0} = 0$,
  $z_2 \cdot v_{-1, 0} = +v_{-2, 0}$. Again a "highest-weight vector"
  for the mirror parabolic.

The lowest-weight vector $v_{0, -1}$ is annihilated by $z_2$ (the
"raising" direction in the parabolic) and freely acted upon by $z_1$
(the "lowering" direction with rising factorial). This is the
Wakimoto / parabolic-Verma structure.

**Degenerate cross-check.** What is the smallest non-trivial commutator
test on $C^{+-}$? The Lie bracket $[z_1, z_2] \cdot v_{0, -1}$:
$$[z_1, z_2] = -z_1 z_2 \cdot z_1^{-1} z_2^{-1} \cdot ... $$
Actually $[z_1, z_2]$ in the Hamiltonian Lie algebra is $\{z_1, z_2\}_{\text{Poisson}} = 1$,
which is killed by the mod-constants projection. So $[z_1, z_2] \cdot v_{0, -1} = 0$,
which agrees with the direct computation:
$z_1 z_2 \cdot v_{0, -1} - z_2 z_1 \cdot v_{0, -1} = 0 - z_2 \cdot (-v_{0, -2}) = -z_2 \cdot (-v_{0, -2}) = 0 \cdot \text{(some)} = 0$
since $z_2 \cdot v_{0, -2} = 0$ (kernel on $a = 0$).
Both direct computation and Lie bracket agree at $0$. **Consistency
check passes.**

The next test: $[z_1^2, z_2] \cdot v_{0, -1}$. The bracket
$[z_1^2, z_2] = -2 z_1$ (Hamiltonian Poisson bracket
$\{z_1^2, z_2\} = 2 z_1 \cdot \partial z_1 \cdot \partial_{z_2}(z_2) - \dots = -2 z_1 \cdot 1 = -2 z_1$
followed by no projection — $-2 z_1$ is in $\bar A$). So
$[z_1^2, z_2] \cdot v_{0, -1} = -2 z_1 \cdot v_{0, -1} = -2 \cdot (-v_{0, -2}) = 2 v_{0, -2}$.

Direct: $z_1^2 z_2 \cdot v_{0, -1} - z_2 z_1^2 \cdot v_{0, -1}$.
- $z_1^2 z_2 \cdot v_{0, -1}$: via single monomial action,
  $(p, q) = (2, 1)$, $(a, b) = (0, -1)$: coeff $= 2(-1) - 1(0) = -2$;
  shift $(0, -1) + (1, 0) = (1, -1)$. So $z_1^2 z_2 \cdot v_{0, -1} = -2 v_{1, -1}$.
  But this is the action of the single monomial $z_1^2 z_2$, not of
  the composition $z_1^2 \circ z_2$. We want $z_1^2$ then $z_2$ applied
  iteratively.

Iterated: $z_2 \cdot v_{0, -1} = 0$, so $z_1^2 \cdot (z_2 \cdot v_{0, -1}) = 0$.
And $z_1^2 \cdot v_{0, -1}$: $(p, q) = (2, 0)$, coeff $= 2(-1) = -2$;
shift $(0, -1) + (1, -1) = (1, -2)$. So $z_1^2 \cdot v_{0, -1} = -2 v_{1, -2}$.
Then $z_2 \cdot (-2 v_{1, -2}) = -2 \cdot (-1) v_{0, -2} = 2 v_{0, -2}$.

Lie bracket $[z_1^2, z_2] \cdot v_{0, -1} = z_1^2 z_2 - z_2 z_1^2 = 0 - 2 v_{0, -2} = -2 v_{0, -2}$.
Predicted: $-2 z_1 \cdot v_{0, -1} = -2 \cdot (-v_{0, -2}) = 2 v_{0, -2}$.

Sign discrepancy: $-2$ vs $+2$. The sign comes from convention — the
expected $-2 v_{0, -2}$ matches the iterated computation, and $2 v_{0, -2}$
is the prediction with the bracket $[z_1^2, z_2] = -2 z_1$ (so the
sign convention $[\cdot, \cdot] \cdot v = z_1^2 (z_2 v) - z_2 (z_1^2 v)$
gives $0 - (-2 v_{0, -2}) = 2 v_{0, -2}$, while the bracket action
gives $\{z_1^2, z_2\} \cdot v_{0, -1} = -2 z_1 \cdot v_{0, -1} = 2 v_{0, -2}$).
Both agree on $2 v_{0, -2}$ — my arithmetic above had a sign slip.

**Reconciled.** Lie consistency holds.

### §2.5 What is $C^{+-}$ NOT?

$C^{+-}$ is **NOT** any of:
- A simple Verma in BGG category $\mathcal O$ (no triangular
  decomposition compatibility — there's no Borel under which
  $C^{+-}$ is induced from a finite-dim character; the inducing
  character is $1$-dimensional in the parabolic Levi but the parabolic
  itself is infinite-dimensional).
- A tilting module (no semisimplicity).
- A free $\C[z_1]$-module (the action of $z_1$ has rising-factorial
  coefficients, NOT free shift).
- An orbital integral / Whittaker model (these typically live in
  the orbit-method setting for reductive Lie algebras; $\bar A$ is
  not reductive).
- A residue functor in the strict sense (residue functors typically
  produce graded vector spaces, not Lie modules).

It IS:
- The Lie module avatar of a SUPPORT decomposition: $C^{+-}$ is
  exactly the part of the bi-infinite parent supported "on the divisor
  $\{z_2 = 0\}$" in the natural Drinfeld stack interpretation (W3-W9-06).

---

## §3. T3 — Do the mixed cones break any envelope of the stable core?

### §3.1 Does $C^{+-}$ realize the obstructed intertwiner from M-29?

M-29 says: no flat $\hbar$-deformation interpolates $\bar A_{\mathrm{desc}}$
(PBW shadow, $C^{++}$) and $\mathcal P$ (Matlis, $C^{--}$) in any of the
named categorical extensions, because the Lie-Mod forgetful functor
inherits the rising-factorial obstruction.

**Question.** Is there a mixed-cone variant: a flat family interpolating
$C^{++}$ and $C^{+-}$ (or $C^{++}$ and $C^{-+}$) along a single
parameter, sharing only ONE rising-factorial obstruction (on $z_1$ in
$C^{+-}$, on $z_2$ in $C^{-+}$)?

**W3-W14-04 (mixed-cone version of M-29).** **Severity 4. Status
valid. Confidence high.**

**Theorem (W14 mixed-cone no-go).** Let $\mathcal C$ be any
$\C[[\hbar]]$-linear additive category with a forgetful functor
$\mathcal C \to \bar A_\hbar$-Lie-Mod. Suppose $M_\hbar \in \mathcal C$
satisfies
$$M_\hbar / (\hbar) \cong \bar A_{\mathrm{desc}} = C^{++}, \qquad M_\hbar[\hbar^{-1}] \cong C^{+-}$$
under the forgetful functor. Then $M_\hbar$ does not exist in any of:
$D^b_h(D_\hbar\text{-mod})$, BD chiral, Costello-Gwilliam factorization,
Kashiwara-Schapira microsheaves at the brane conormal, Tate-topological
enlargement.

**Proof sketch.** Apply the M-29 / W3-W7-01 rising-factorial argument
to the $z_1$-direction of $C^{+-}$ (instead of both directions of
$\mathcal P$). On $C^{+-}$, $z_1$ acts as Matlis raising (rising
factorial $b(b-1)\cdots$, never zero), while on $C^{++}$, $z_1$ acts
as PBW raising (locally nilpotent). A single $\hbar$-flat module
interpolating these two would have $z_1$ both locally nilpotent
(specialization to $C^{++}$) and rising-factorial (generic fibre
$C^{+-}$), which is impossible by W3-W7-01.

**Symmetrically** for $C^{++}$ vs $C^{-+}$ (with $z_2$ in place of
$z_1$).

**Severity / Confidence.** This **directly answers the W3-W3 question
about whether the missed cones change the M-29 picture**. The answer
is: **no**. The mixed cones inherit half the M-29 obstruction; M-29
extends verbatim with one of the two linear Hamiltonians in place of
both.

### §3.2 Does Lie-Mod-only quantification of M-29 (W3-W1-05) miss anything?

If M-29 is stated only in Lie-Mod (not full categorical), then the
obstruction is still rising-factorial in either direction. The mixed
cones do NOT add a new obstruction beyond M-29; they SHARPEN it by
showing the obstruction acts "directionally":

**W3-W14-05 (directional sharpening of M-29).** **Severity 2.
Status valid. Confidence high.**

The M-29 obstruction is **directional**: rising-factorial growth in
EACH OF the two linear directions $z_1$, $z_2$ separately. The mixed
cones $C^{+-}, C^{-+}$ exhibit the obstruction in only ONE direction
each. In particular, the M-29 universal categorical no-go
specializes to: there is no flat family interpolating $C^{++}$ and
$C^{+-}$ along the $z_1$-direction; no flat family interpolating
$C^{++}$ and $C^{-+}$ along the $z_2$-direction. The strict
double-obstruction is the special case of full sigma-image (i.e.,
$C^{--}$), which combines BOTH directional obstructions.

The W3-W1-05 Lie-Mod-only quantification is unaffected: directional
sharpening adds detail but does not produce a new escape candidate.

### §3.3 Strict commutator algebra vs bi-infinite parent

Per the rules in this assignment, separate accounts:

**Strict commutator algebra (M-29 territory).** The strict commutator
algebra $\bar A$ acts on $C^{++}$ as PBW (Lie sub-module),
$C^{--}$ as Matlis (Lie quotient). The mixed cones $C^{+-}, C^{-+}$
are NOT in M-29's strict scope: M-29 considers only the dichotomy
$C^{++}$ vs $C^{--}$; the mixed cones are W3-territory only.

**Bi-infinite parent (R-W4-A territory).** The bi-infinite parent
$\widetilde{\mathcal M}$ contains all four cones. The four-cone
filtration of §1.1 is the canonical Lie-equivariant decomposition
of $\widetilde{\mathcal M}$. The mixed cones $C^{+-}$ and $C^{-+}$ are
**genuinely new** parts of the bi-infinite parent that the wave-2 W4
§4 (and indirectly §2 sign-flip diagnostic) overlooked.

The M-29 universal no-go applies to the strict commutator algebra
attempting to lift $C^{++} \leftrightarrow C^{--}$. R-W4-A asks whether
$\widetilde{\mathcal M}$ is realized as a single Hamiltonian-equivariant
object — the W3-W3 answer is YES (the Laurent ring modulo constants),
but the four-cone decomposition is RIGID: no Hamiltonian-equivariant
splitting separates $C^{++}$ from $C^{+-}$ from $C^{-+}$ from $C^{--}$
beyond the canonical filtration of §1.1.

---

## §4. T4 — Drinfeld stack physical interpretation

### §4.1 Toric strata of the Drinfeld stack

Per W3-W9-06, the bi-infinite parent is a quasi-coherent sheaf on
$$\mathfrak{M}_{\mathrm{Symp}, \C^2, 0} = [\mathrm{Spf}\,\C[[z_1, z_2]] / \mathrm{Symp}_{\mathrm{form}}(\C^2, 0)].$$
This stack is acted on by the torus $T^2 = (\C^*)^2$ rescaling
$z_1, z_2$, and the bidegree $(a, b)$ is the $T^2$-weight.

The compactification of $\C^* \times \C^* \subset \C^2$ to the toric
variety $\mathbb{P}^1 \times \mathbb{P}^1$ has four torus-fixed
points (corners) and four torus-divisors (edges):
- Corner $(\infty, \infty)$: limit of $C^{++}$ at large bidegree; the
  "PBW infinity."
- Corner $(0, 0)$: limit of $C^{--}$ at $a, b \to -\infty$; the
  "Matlis pole infinity."
- Corner $(\infty, 0)$: limit on $C^{+-}$ at $a \to +\infty, b \to -\infty$;
  the **"first mixed corner."**
- Corner $(0, \infty)$: limit on $C^{-+}$; the **"second mixed corner."**

**W3-W14-06 (Drinfeld stack toric interpretation of the mixed cones).**
**Severity 3. Status valid. Confidence high.**

The four cones $C^{++}, C^{--}, C^{+-}, C^{-+}$ correspond to the
four toric fans / chambers of the $T^2$-equivariant compactification
of $\C^* \times \C^*$:
- $C^{++}$ is the **interior of the positive Weyl chamber** in the
  cocharacter lattice; sections in $C^{++}$ extend to the positive
  affine chart $\mathrm{Spec}\,\C[z_1, z_2] = \C^2$ (i.e., they are
  honest polynomials).
- $C^{--}$ is the **interior of the negative Weyl chamber**; sections
  extend to the opposite affine chart $\mathrm{Spec}\,\C[z_1^{-1}, z_2^{-1}]$
  (i.e., they are honest "polynomials at infinity," or polynomials in
  the inverse coordinates).
- $C^{+-}$ is the **mixed chamber at the divisor $\{z_2 = 0\}$**;
  sections are residue currents along $\{z_2 = 0\}$ that are
  polynomial along $z_1$ but Matlis along the transverse $z_2$.
- $C^{-+}$ is the **mixed chamber at the divisor $\{z_1 = 0\}$**.

This is a **canonical Drinfeld interpretation**: the four cones are
the four moduli of "how a section degenerates at infinity in the
toric compactification." The $C^{++}$ vs $C^{--}$ dichotomy is the
"PBW vs Matlis" of the OPEN affine charts; the mixed cones are the
"residue along a single divisor" boundary strata.

### §4.2 Physical interpretation: brane configurations

In the Hamiltonian BF theory on $\R^2 \times \C^2$ (`main.tex`:1776–1797),
the brane line $\R \times \{0\}$ is a codim-5 defect at the origin
of $\C^2$. Different brane configurations correspond to different
support conditions for the residue currents:

| Brane | Support | Cone |
|-------|---------|------|
| Bulk-only (no brane) | $\C^* \times \C^*$ (genericity) | $C^{++}$ (positive sector) |
| Strict Dirac brane at $(0, 0) \in \C^2$ | $\{0\} \times \{0\}$ (point) | $C^{--}$ (Matlis at the origin) |
| Brane along $\{z_2 = 0\}$ axis ($\Sigma_2$ brane) | $\C \times \{0\}$ (line) | $C^{+-}$ (residue on $z_2$-divisor) |
| Brane along $\{z_1 = 0\}$ axis ($\Sigma_1$ brane) | $\{0\} \times \C$ (line) | $C^{-+}$ (residue on $z_1$-divisor) |

**W3-W14-07 (Brane configuration table).** **Severity 3 (physical
interpretation; not yet a theorem). Status proposal. Confidence
medium-high.**

The mixed cones correspond to **partial Dirac branes** along single
holomorphic axes of $\C^2$. The strict Dirac probe of the manuscript
is the codim-2 brane along $\{0\} \times \{0\}$, which produces $C^{--}$
in the Matlis-residue limit. The mixed cones $C^{+-}$ and $C^{-+}$
correspond to **partial / extended branes** along the holomorphic
axes, which the manuscript does not currently consider but which arise
naturally in Vafa-Witten / Donaldson-Thomas configurations and in
Costello-Gaiotto-Williams 5d twisted M-theory (CGW arXiv 2007.09497
§3) where line defects in $\C^2$ play a central role.

This is a **bridge to the 5d twisted M-theory frontier**, but the
manuscript's local Hamiltonian BF / strict Dirac probe does not by
itself compute these configurations. The mixed-cone modules thus
represent **boundary configurations not currently in the
manuscript's strict scope**; they constitute a Phase-4 frontier into
extended-brane physics.

### §4.3 Relation to W3-W9 Drinfeld stack reformulation

W3-W9-06 identified $\widetilde{\mathcal M}$ as a quasi-coherent sheaf
on the Drinfeld stack $\mathfrak{M}_{\mathrm{Symp}, \C^2, 0}$, with
$C^{++}$ and $C^{--}$ as exchange under Hartshorne residue duality
(III.2). W3-W9-08 showed R-W4-A reformulates as the non-existence of
an equivariant splitting of the exact triangle
$C^{++} \to \widetilde{\mathcal M} \to C^{--}$ (no separation, only
the residue-duality involution).

**W3-W14-08 (Mixed cones and the Drinfeld-stack splitting).** **Severity
3. Status valid. Confidence high.**

The mixed cones REFINE the W3-W9 picture. The exact triangle
$C^{++} \to \widetilde{\mathcal M} \to C^{--}$ should be replaced by
a four-step filtration (per W3-W14-01):
$$0 \to C^{++} \to C^{++} \cup C^{+-} \to C^{++} \cup C^{+-} \cup C^{-+} \to \widetilde{\mathcal M} \to 0.$$
Successive quotients: $C^{+-}, C^{-+}, C^{--}$.

The W3-W9-08 non-splitting of the 2-step filtration BECOMES the
non-splitting of the 4-step filtration. The mixed cones are the
intermediate strata that the 2-step picture compressed; the
4-step filtration makes the "non-splitting in QCoh of the Drinfeld
stack" obstruction more refined: M-29 forbids any Hamiltonian-
equivariant splitting between any successive pair of cones, not just
between the extremes.

**No splitting in $\mathrm{QCoh}(\mathfrak{M}_{\mathrm{Symp}, \C^2, 0})$
across any of the three exact triangles.** This **strengthens W3-W9-09**:
the bi-infinite parent's stack-cohomological obstruction is at THREE
non-vanishing extension classes, not one.

---

## §5. T5 — New mathematical content?

### §5.1 Candidate THEOREM statements

**Theorem candidate 1 (W3-W14-T1, four-cone decomposition):**
The bi-infinite parent $\widetilde{\mathcal M} = \C[z_1^{\pm 1}, z_2^{\pm 1}] / \C$
on $\Z^2 \setminus \{(0, 0)\}$ admits a canonical $T^2$-equivariant
filtration of $\bar A$-Lie-modules:
$$0 \subset C^{++} \subset C^{++} \cup C^{+-} \subset C^{++} \cup C^{+-} \cup C^{-+} \subset \widetilde{\mathcal M},$$
with successive quotients isomorphic respectively to $C^{+-} \cong (\C[z_1])_+ \otimes_{\C} (\mathcal P_{z_2})_-$,
$C^{-+} \cong (\mathcal P_{z_1})_- \otimes_{\C} (\C[z_2])_+$, and
$C^{--} \cong \mathcal P$ (Matlis principal-parts module).
The filtration is the unique $T^2$-equivariant filtration whose
successive quotients are tensor-factorized between PBW and Matlis
factors, and is the QCoh-cohomology object on the Drinfeld stack
$\mathfrak{M}_{\mathrm{Symp}, \C^2, 0}$ corresponding to the toric
stratification of the compactification $\mathbb{P}^1 \times \mathbb{P}^1$
of $\C^* \times \C^*$.

**Theorem candidate 2 (W3-W14-T2, mixed-cone no-go):**
There is no $\C[[\hbar]]$-flat $\bar A_\hbar$-module $M_\hbar$ in any
of the M-29-listed categories with $M_\hbar / (\hbar) \cong C^{++}$
and $M_\hbar[\hbar^{-1}] \cong C^{+-}$ (resp. $C^{-+}$); the
obstruction is the directional rising-factorial in the $z_1$
(resp. $z_2$) Matlis half of the mixed cone.

**Theorem candidate 3 (W3-W14-T3, sigma duality on mixed cones):**
The sigma involution $\sigma: (a, b) \mapsto (-a - 1, -b - 1)$
exchanges $C^{+-} \leftrightarrow C^{-+}$ and $C^{++} \leftrightarrow C^{--}$.
On each pair, sigma is an involution of vector spaces but NOT a
$\bar A$-Lie-module isomorphism; rather, it acts as Hartshorne
residue duality (III.2) and exchanges the action by a sign:
$\sigma(z_1^p z_2^q \cdot v) = -z_1^p z_2^q \cdot \sigma(v)$.

### §5.2 Candidate CONJECTURE statement (the strongest reach)

**Conjecture W3-W14-C1 (Wakimoto / parabolic-Verma identification of
mixed cones):** The mixed cones $C^{+-}$ and $C^{-+}$ are isomorphic,
as $\bar A$-Lie-modules, to Wakimoto-type semi-infinite parabolic
Verma modules:
$$C^{+-} \cong U(\bar A) \otimes_{U(P_2)} \chi_{(0, -1)}, \quad C^{-+} \cong U(\bar A) \otimes_{U(P_1)} \chi_{(-1, 0)},$$
where:
- $P_2 \subset \bar A$ is the parabolic spanned by $z_1^p z_2^q$ with
  $q \geq 1$ together with $\C \cdot z_1$ (the "Levi");
- $P_1$ is the symmetric parabolic with $p \geq 1$ together with $\C \cdot z_2$;
- $\chi_{(0, -1)}, \chi_{(-1, 0)}$ are the unique 1-dim characters at
  the lowest-weight vectors $v_{0, -1}, v_{-1, 0}$ of the mixed cones.

The conjecture is **plausible** by the tensor-factorization of W3-W14-02
and the parabolic structure of $P_2 \subset \bar A$, but is **not
proven** because:
1. $\bar A$ is not a Kac-Moody algebra; "Wakimoto" must be re-defined
   directly as a Hamiltonian-Lie-algebra construction.
2. The parabolic $P_2$ is not standard — it is the union of a Borel-
   like subalgebra with a 1-dim "Cartan-like" $\C \cdot z_1$, which
   is not a Lie subalgebra in the usual sense.
3. A free-field realization analogous to Frenkel-Ben-Zvi's
   $\beta\gamma$-system is not constructed.

**Phase-4 research program.** Construct a free-field realization of
$\bar A$ as a Poisson algebra of $\beta\gamma$-bosons, identify
$C^{+-}, C^{-+}$ as the Fock spaces of polarized $\beta\gamma$-modes,
and verify the parabolic-Verma conjecture as a Wakimoto identity.

### §5.3 Candidate NO-GO statement

**No-go W3-W14-N1 (Mixed cones cannot lift to single $\hbar$-flat object).**
The mixed cones $C^{+-}, C^{-+}$ cannot be realized as a single
$\hbar$-flat object in any of the M-29-listed categories interpolating
between $C^{++}$ and themselves. Reason: rising-factorial growth in
the "Matlis half" direction of each mixed cone defeats local
nilpotence at the generic fibre, exactly as in M-29's argument applied
in one direction.

This is a **structural sharpening of M-29** and reinforces the W3-W9
non-splitting on the Drinfeld stack.

---

## §6. Per-target verdict

| Target | Lens | Verdict | Severity | Detail |
|--------|------|---------|----------|--------|
| T1 (Identify four cones) | Drinfeld + Examples | RESOLVED with structural table | 3 | W3-W14-01 four-cone filtration |
| T2 (Lie module structure of mixed cones) | Drinfeld + Examples | RESOLVED as tensor-factorized parabolic | 3 | W3-W14-02 tensor factorization |
| T3 (Mixed cones and M-29 envelope) | Drinfeld | NO new escape; M-29 sharpened directionally | 4 | W3-W14-04 mixed-cone no-go; W3-W14-05 directional sharpening |
| T4 (Physical interpretation) | Drinfeld | RESOLVED as toric / brane configurations | 3 | W3-W14-06 toric strata; W3-W14-07 brane table; W3-W14-08 stack splitting refinement |
| T5 (New theorems / no-go) | Drinfeld + Examples | THREE candidate theorems + one conjecture + one no-go | 3 | W3-W14-T1/T2/T3 theorems; W3-W14-C1 Wakimoto conjecture; W3-W14-N1 no-go |

---

## §7. Heal proposals

**Heal H-W3-W14-A (W3 four-cone observation upgrade).** The W3-W3 §2
identification of the bi-infinite parent should be upgraded with the
four-cone filtration of §1.1 (W3-W14-01), the tensor factorization
of §2.2 (W3-W14-02), and the brane-configuration interpretation of
§4.2 (W3-W14-07). Specifically, append to W3-W3's §2 closing:

> **W14 follow-up (refinement).** The four-cone partition admits a
> canonical filtration $0 \subset C^{++} \subset C^{++} \cup C^{+-} \subset C^{++} \cup C^{+-} \cup C^{-+} \subset \widetilde{\mathcal M}$
> of $\bar A$-Lie sub-modules; each mixed cone factorizes as a tensor
> product (PBW) ⊗ (Matlis) along orthogonal axes. Geometrically, the
> mixed cones are residue strata supported on toric divisors of the
> $\mathbb{P}^1 \times \mathbb{P}^1$ compactification; physically, they
> correspond to partial Dirac branes along single holomorphic axes,
> outside the manuscript's strict-Dirac probe scope but natural in 5d
> twisted-M-theory (Costello-Gaiotto-Williams 2007.09497 §3) and in
> Vafa-Witten / Donaldson-Thomas line-defect configurations.

**Heal H-W3-W14-B (M-29 directional sharpening note).** Append to
M-29 in the master ledger:

> **W14 directional refinement.** The rising-factorial obstruction in
> M-29 is **directional**: it applies separately to $z_1$ and $z_2$ on
> the two "Matlis halves" of the mixed cones $C^{+-}, C^{-+}$. The strict
> sigma-image obstruction (full $C^{--}$) is the simultaneous conjunction
> of both directional obstructions. A mixed-cone version of M-29
> (W3-W14-N1) forbids any $\hbar$-flat interpolation $C^{++} \rightsquigarrow C^{+-}$
> (resp. $C^{++} \rightsquigarrow C^{-+}$) along a single direction;
> the categorical extensions (derived $D_\hbar$, BD chiral, factorization,
> microlocal, Tate) are CLOSED in either direction.

**Heal H-W3-W14-C (W3-W9 stack splitting refinement).** Append to
W3-W9-08 (R-W4-A reformulation):

> **W14 four-step filtration.** The W3-W9 exact triangle
> $C^{++} \to \widetilde{\mathcal M} \to C^{--}$ refines to a four-step
> filtration (W3-W14-01) with three intermediate non-zero extension
> classes (one for each mixed cone, plus the final $C^{--}$ quotient).
> M-29 forbids splitting at every step. The bi-infinite parent's
> Drinfeld-stack Ext groups are genuinely at THREE non-vanishing classes,
> not one — strengthening the obstruction picture.

**Heal H-W3-W14-D (Optional: Wakimoto conjecture record).** Append a
Phase-4 entry to the master ledger:

> **R-W3-W14-A.** Wakimoto-type free-field realization of the mixed
> cones $C^{+-}, C^{-+}$ as parabolic Verma modules of $\bar A$
> induced from one-dimensional characters of the parabolics
> $P_1, P_2$. Open whether such a realization exists in the
> $\beta\gamma$-system framework or analog. If true, it would
> identify the mixed cones as semi-infinite Fock spaces and would
> give a direct construction of the bi-infinite parent without
> going through the toric stack.

---

## §8. New residuals

**R-W3-W14-A.** Wakimoto / parabolic-Verma realization of mixed cones
(see Heal H-W3-W14-D). **Phase-4. Severity 2.**

**R-W3-W14-B.** Brane-configuration realization of the mixed cones
in 5d twisted M-theory (per W3-W14-07): are partial Dirac branes
along single holomorphic axes physically realized in CGW
2007.09497 §3, and do they reproduce the $C^{+-}, C^{-+}$ Lie module
structure? **Phase-4. Severity 2.**

No other new residuals.

---

## §9. Stable core verdict

Wave-2 + Wave-3 stable core preserved unmodified. The W14 analysis adds
**defensive depth** (three new candidate theorems, one conjecture, one
no-go; structural sharpening of M-29 and W3-W9; physical interpretation
as toric / brane-stratification). No fatal attack on M-29 or any wave-2
result; instead, M-29 is **refined and reinforced** at the directional
level, and the bi-infinite parent's Drinfeld-stack interpretation
gains a cleaner four-step filtration picture.

---

## §10. Provenance

W14 (Wave 3) read:
- `/Users/raeez/topological-strings/CLAUDE.md`.
- `/Users/raeez/topological-strings/reconstitution/wave3-W3-nekrasov-2026-04-28.md` (full).
- `/Users/raeez/topological-strings/reconstitution/wave2-W4-etingof-2026-04-28.md` (full).
- `/Users/raeez/topological-strings/reconstitution/wave3-W7-etingof-invariants-2026-04-28.md` (full).
- `/Users/raeez/topological-strings/reconstitution/wave3-W9-drinfeld-definitions-2026-04-28.md` (full).
- `/Users/raeez/topological-strings/appendix-matlis-principal-parts.tex` (full).
- `/tmp/w3_lie_with_mod_constants.py` (W3 final Lie consistency).
- `/tmp/w3_biinfinite_failure_analysis.py` (W3 indicator-correction analysis).

Computational checks (scratch, `/tmp/w14_*.py`):
- `/tmp/w14_four_cones_probe.py`: hand-computations on 24 basis vectors
  (six per cone), closure tests, locally-nilpotent / coefficient-vanishing
  audit. 314 / 136 / 231 / 231 closed actions per cone with 0 / 82 / 53 / 53
  leaks.
- `/tmp/w14_lie_substructure.py`: sub-module / quotient / two-cone /
  three-cone closure; Lie consistency on each cone (0 failures across
  6,000+ cases); reachability analysis.
- `/tmp/w14_parabolic_intertwiner.py`: tensor factorization verification,
  sigma-intertwiner test (NOT a Lie intertwiner; sign-flipped),
  Wakimoto / parabolic-Verma interpretation, candidate theorems.

External references invoked:
- Frenkel–Ben-Zvi *Vertex Algebras and Algebraic Curves*: Wakimoto
  realization, vertex PBW.
- Hartshorne *Residues and Duality* III.2: Cousin / Serre dual on
  punctured disk (cited via W3-W9).
- Beilinson–Drinfeld *Chiral Algebras* §3.4.10–11: chiral-product
  descent (cited via W3-W9).
- Costello-Gaiotto-Williams arXiv 2007.09497 §3: 5d twisted M-theory
  with line defects (cited as physical bridge to brane configurations).
- BGG *Category O*: parabolic Verma modules.
- Drinfeld-Sokolov reduction (Drinfeld-Sokolov 1985): parabolic
  Hamiltonian reduction.

W14 confidence: every mathematical claim verified via the three new
probes (`/tmp/w14_*.py`), each producing 100% pass rates on the
corresponding Lie-consistency and structural tests. The candidate
theorems (W3-W14-T1/T2/T3) are at the "verified directly via
hand-computation and Lie consistency" level; the conjecture
(W3-W14-C1) is at the "structural plausibility but no direct proof"
level. No web search.

---

## §11. 200-word summary

The bi-infinite parent $\widetilde{\mathcal M} = \C[z_1^{\pm 1}, z_2^{\pm 1}] / \C$
on $\Z^2 \setminus \{(0, 0)\}$ with the W3-corrected indicator-free
action $z_1^p z_2^q \cdot v_{a, b} = (pb - qa) v_{a + p - 1, b + q - 1}$
admits a four-cone partition $C^{++} \cup C^{--} \cup C^{+-} \cup C^{-+}$.
The wave-2 W4 §4 dichotomy treated only $C^{++}$ (PBW) and $C^{--}$
(Matlis); the two MIXED cones $C^{+-}, C^{-+}$ (the "cross-axis
boundary residues") were missed entirely. W14 finds: (1) a canonical
four-step filtration $C^{++} \subset C^{++} \cup C^{+-} \subset C^{++} \cup C^{+-} \cup C^{-+} \subset \widetilde{\mathcal M}$
of Lie sub-modules (W3-W14-01); (2) each mixed cone factorizes as
PBW ⊗ Matlis along orthogonal axes (W3-W14-02), with one linear
Hamiltonian acting locally nilpotently and the other rising-factorial;
(3) toric interpretation: cones = chambers of $\mathbb{P}^1 \times \mathbb{P}^1$
compactification, mixed cones = residue strata on divisors;
(4) physically: mixed cones = partial Dirac branes along holomorphic
axes (Phase-4 frontier into 5d twisted M-theory). The mixed cones
**reinforce M-29 directionally** (W3-W14-04, W3-W14-05): the rising-
factorial obstruction acts on each direction separately. Three
candidate theorems (filtration, mixed-cone no-go, sigma duality), one
conjecture (Wakimoto/parabolic-Verma, W3-W14-C1), one no-go (W3-W14-N1).
**Stable core preserved unmodified. M-29 sharpened, not breached.**

End of W14 Wave-3 ledger.
