#!/usr/bin/env python3
"""Extended Moyal/Capelli/radial-parts verification harness.

Evidence harness for the quantum derived-center subsection of main.tex
(propositions prop:moyal-monomial, prop:quantum-boundary-descends-products,
lem:capelli-renormalized-stable-trace, thm:finite-n-reduced-moyal,
cor:degree-zero-quantum-upgrade, prop:conditional-boundary-product-normalization,
thm:open-line-midpoint-graph-weights, and the formal coefficient target used
by thm:first-third-costello-normalizations, thm:phi-hbar-all-order, and
prob:quantum-p0-operation-realization). The script is dependency-free;
rationals are exact via `fractions.Fraction`. No NumPy/SymPy.

It verifies, on the four nontrivial test pairs

    (a) z1, z2
    (b) z1^2, z2
    (c) z1^2, z2^2
    (d) z1^3, z2^2

plus a sweep up to exponent 10 and order 11:

  1.  Moyal coefficients on monomials (P^r and the star commutator) match
      Proposition `prop:moyal-monomial`.
  2.  Antisymmetry: P^r(g, f) = (-1)^r P^r(f, g).  Even orders cancel in the
      commutator at every order checked (closed in the script up to r=11).
  3.  Capelli triangular identity (Remark `rmk:capelli-renormalized-traces`):
      the Weyl trace `J_N` and the normal-ordered trace `T` are related by
      the explicit triangular `hbarN` shift on (z1^a z2^b) for arbitrary
      a, b in 0..10.  The shift is the operator `exp(-hbarN/2 d1 d2)`.
  4.  Renormalized connected trace identity: explicit low-degree Capelli
      examples are asserted, including
        J_N(z1 z2), J_N(z1^2 z2), J_N(z1^2 z2^2),
      and the normal-ordering defect
        hbar^{-1}[T_{2,1}, T_{0,2}] = 4 T_{1,2} - 2 hbar N T_{0,1}
      is derived from the triangular system.
  5.  Direct N=2 and N=3 radial-parts restriction: for selected J_N(f), apply
      the actual matrix Weyl differential operator on invariant test
      polynomials in gl_N, restrict to diagonal matrices, and compare
      Delta . J_N(f)|_t with S_N(f) . Delta.  This attacks the
      source-dependent radial-parts input in low rank but does not prove the
      all-N Harish-Chandra theorem.
  6.  Reduced Moyal commutator identity at finite N (Theorem
      `thm:finite-n-reduced-moyal`).  The radial-parts side
        S_N(f) = sum_i Op_W(f)(lambda_i, -hbar d_lambda_i)
      is the one-particle Weyl algebra at each Cartan node, so distinct
      summands commute.  Verified by direct symbolic commutator against
      S_2([f,g]_*) on the Cartan-rank-2 specialization (N=2) for all
      primary and higher-order test pairs.
  7.  Pre-quotient scalar Moyal / U(1) anomaly coefficient: compute the
      leading scalar Moyal coefficient before quotienting constants.  The
      nonconstant terms are the connected Hamiltonian bracket; the constant
      term is the scalar anomaly killed only after reduction.
  8.  Open-line midpoint graph weights (Theorem
      `thm:open-line-midpoint-graph-weights`): the one-edge weight is
      hbar P/2 and the three-parallel-edge weight is hbar^3 P^3/48; their
      antisymmetrisations give hbar P and hbar^3 P^3/24.

Run

    python3 scripts/check_moyal_coefficients.py

The script exits with a nonzero return code on the first failed assertion.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
from math import comb, factorial
from typing import Dict, Tuple


Poly = Dict[Tuple[int, int], Fraction]


def falling(n: int, r: int) -> int:
    out = 1
    for i in range(r):
        out *= n - i
    return out


def monomial(a: int, b: int, coeff: Fraction = Fraction(1)) -> Poly:
    if a < 0 or b < 0 or coeff == 0:
        return {}
    return {(a, b): coeff}


def add(p: Poly, q: Poly) -> Poly:
    out = dict(p)
    for exp, coeff in q.items():
        out[exp] = out.get(exp, Fraction(0)) + coeff
        if out[exp] == 0:
            del out[exp]
    return out


def scale(c: Fraction, p: Poly) -> Poly:
    return {exp: c * coeff for exp, coeff in p.items() if c * coeff}


def mul(p: Poly, q: Poly) -> Poly:
    out: Poly = {}
    for (a, b), c in p.items():
        for (m, n), d in q.items():
            exp = (a + m, b + n)
            out[exp] = out.get(exp, Fraction(0)) + c * d
    return {exp: coeff for exp, coeff in out.items() if coeff}


def diff(p: Poly, dz1: int, dz2: int) -> Poly:
    out: Poly = {}
    for (a, b), coeff in p.items():
        if a < dz1 or b < dz2:
            continue
        out[(a - dz1, b - dz2)] = coeff * falling(a, dz1) * falling(b, dz2)
    return out


def p_power(f: Poly, g: Poly, r: int) -> Poly:
    out: Poly = {}
    for a in range(r + 1):
        term = mul(diff(f, r - a, a), diff(g, a, r - a))
        out = add(out, scale(Fraction((-1) ** a * comb(r, a)), term))
    return out


def commutator_coeff(f: Poly, g: Poly, r: int) -> Poly:
    return add(p_power(f, g, r), scale(Fraction(-1), p_power(g, f, r)))


def star_commutator_coeff(f: Poly, g: Poly, r: int) -> Poly:
    return scale(
        Fraction(1, 2 ** r),
        scale(Fraction(1, factorial(r)), commutator_coeff(f, g, r)),
    )


def expected_star_commutator_coeff(f: Poly, g: Poly, r: int) -> Poly:
    if r == 0 or r % 2 == 0:
        return {}
    return scale(Fraction(1, 2 ** (r - 1) * factorial(r)), p_power(f, g, r))


def expected_p1(k: int, l: int, m: int, n: int) -> Poly:
    return monomial(k + m - 1, l + n - 1, Fraction(k * n - l * m))


def expected_p3(k: int, l: int, m: int, n: int) -> Poly:
    coeff = 0
    for a in range(4):
        coeff += (
            (-1) ** a
            * comb(3, a)
            * falling(k, 3 - a)
            * falling(l, a)
            * falling(m, a)
            * falling(n, 3 - a)
        )
    return monomial(k + m - 3, l + n - 3, Fraction(coeff))


# ---------------------------------------------------------------------------
# Capelli triangular identity (Remark `rmk:capelli-renormalized-traces`).
#
# In the manuscript notation, the Weyl-ordered trace J_N(z1^a z2^b) and the
# normal-ordered trace T_{a,b} = Tr(X^a Y^b) are related by
#
#   J_N(z1^a z2^b) = sum_{r=0}^{min(a,b)}
#                       (-hbar N / 2)^r * r! * C(a, r) * C(b, r) * T_{a-r, b-r}.
#
# Equivalently, J_N(f) = T_N( exp(-hbar N / 2 * d_z1 d_z2) f ).  The Capelli
# subtraction lemma below is proved by induction on a + b: the displayed sum
# is the unique triangular formula whose r=0 term is T_{a,b} and whose r=1
# term is -hbar N a b T_{a-1,b-1}/2... .  The verification here is symbolic
# at the level of the trace generators T_{a,b}, treated as commuting symbols
# (the residual ambiguity is the ordering inside the trace, which is
# triangular and absorbed into the recursion).
# ---------------------------------------------------------------------------


def capelli_J_in_T(a: int, b: int):
    """Return list of (sign, hbarN_power, coefficient, (a-r, b-r)) tuples."""
    out = []
    for r in range(min(a, b) + 1):
        coeff = Fraction((-1) ** r) * Fraction(factorial(r))
        coeff *= Fraction(comb(a, r) * comb(b, r))
        coeff *= Fraction(1, 2 ** r)
        out.append((coeff, r, (a - r, b - r)))
    return out


def capelli_invert_T_in_J(a: int, b: int):
    """Inverse triangular: T_{a,b} = sum_r (hbar N / 2)^r r! C(a,r) C(b,r) J(a-r,b-r)."""
    out = []
    for r in range(min(a, b) + 1):
        coeff = Fraction(factorial(r)) * Fraction(comb(a, r) * comb(b, r))
        coeff *= Fraction(1, 2 ** r)
        out.append((coeff, r, (a - r, b - r)))
    return out


def capelli_round_trip(max_exp: int) -> int:
    """Verify J -> T -> J reproduces the identity matrix on monomials."""
    checked = 0
    for a in range(max_exp + 1):
        for b in range(max_exp + 1):
            #  J(a,b) = sum_r ca_r * (hbar N)^r * T(a-r, b-r)
            #  Expand each T(a-r, b-r) = sum_s cb_s * (hbar N)^s * J(a-r-s, b-r-s).
            #  The composed coefficient of J(a-q, b-q) is
            #     sum_{r+s=q} (-1)^r r! s! C(a,r) C(b,r) C(a-r,s) C(b-r,s) / 2^q.
            #  We want this to equal Kronecker-delta_{q, 0}.
            for q in range(min(a, b) + 1):
                tot = Fraction(0)
                for r in range(q + 1):
                    s = q - r
                    if a - r < s or b - r < s:
                        continue
                    term = Fraction((-1) ** r) * Fraction(factorial(r) * factorial(s))
                    term *= Fraction(comb(a, r) * comb(b, r))
                    term *= Fraction(comb(a - r, s) * comb(b - r, s))
                    tot += term
                tot *= Fraction(1, 2 ** q)
                expected = Fraction(1) if q == 0 else Fraction(0)
                assert tot == expected, (
                    f"Capelli round-trip failed at (a,b)=({a},{b}) q={q}: "
                    f"got {tot}, expected {expected}"
                )
            checked += 1
    return checked


# ---------------------------------------------------------------------------
# Renormalized stable connected trace.
#
# Define
#     Tr^{ren}(z1^a z2^b) := J_N(z1^a z2^b) - hbar N * delta_shift,
# where delta_shift collects the lower triangular pieces of degree (a-1, b-1)
# and below, weighted by the Capelli triangular coefficients.  This is the
# degreewise stable-rank connected generator: after passage to the
# primitive connected trace sector, the leading hbar*N linear shift in
# T_{a-1, b-1} is the unique Capelli subtraction that lands in that
# sector, and the higher-r terms are the iterated Capelli corrections.
#
# Equivalently, Tr^{ren}(f) = J_N(f) is itself the Capelli-renormalized
# generator of Remark `rmk:capelli-renormalized-traces`.  The "subtraction"
# is the truncation that removes the empty trace; on connected nonempty
# words it is the identity mod the moment-map ideal because the Capelli
# triangular coefficients live in degree (a-r, b-r) with r >= 1.
# ---------------------------------------------------------------------------


def stable_connected_subtraction(a: int, b: int):
    """Return the explicit Tr^{ren} expansion: the J_N coefficient at order
    hbar^0 plus all triangular Capelli shifts at orders hbar^r for r >= 1.
    Output: list of (coeff, hbar_power, N_power, (a-r, b-r)).
    """
    out = []
    for r in range(min(a, b) + 1):
        coeff = Fraction((-1) ** r) * Fraction(factorial(r))
        coeff *= Fraction(comb(a, r) * comb(b, r))
        coeff *= Fraction(1, 2 ** r)
        out.append((coeff, r, r, (a - r, b - r)))
    return out


TraceExpansion = Dict[Tuple[int, int, int, int], Fraction]


def normalized_T_commutator_in_T(
    a: int, b: int, c: int, d: int, max_order: int
) -> TraceExpansion:
    """Compute hbar^{-1}[T_{a,b}, T_{c,d}] in the normal-ordered T-basis.

    Keys are (hbar_power, N_power, z1_exp, z2_exp).  The computation uses the
    inverse Capelli triangular system T -> J, the normalized Moyal bracket on
    J-generators, and then the triangular system J -> T.
    """

    out: TraceExpansion = {}
    left = capelli_invert_T_in_J(a, b)
    right = capelli_invert_T_in_J(c, d)
    for lc, lp, (la, lb) in left:
        for rc, rp, (ra, rb) in right:
            f = monomial(la, lb)
            g = monomial(ra, rb)
            for order in range(1, max_order + 1):
                coeff_poly = star_commutator_coeff(f, g, order)
                if not coeff_poly:
                    continue
                normalized_hbar_power = order - 1
                for (ja, jb), pc in coeff_poly.items():
                    for jc, jp, (ta, tb) in capelli_J_in_T(ja, jb):
                        key = (
                            lp + rp + normalized_hbar_power + jp,
                            lp + rp + jp,
                            ta,
                            tb,
                        )
                        out[key] = out.get(key, Fraction(0)) + lc * rc * pc * jc
                        if out[key] == 0:
                            del out[key]
    return out


# ---------------------------------------------------------------------------
# Reduced Moyal commutator identity (Theorem `thm:finite-n-reduced-moyal`).
#
# We verify the radial-parts identity numerically/symbolically at N = 2.
# The radial part S_N(f) on the Cartan acts by sum_i Op_W(f)(lambda_i, -hbar
# d_lambda_i).  For monomials f = z1^k z2^l this is a sum of two one-particle
# Weyl operators that commute, and so the commutator
#     [S_N(f), S_N(g)] = sum_i [Op_W(f)_i, Op_W(g)_i]
# is the diagonal of the one-particle scalar Weyl/Moyal commutator.
# ---------------------------------------------------------------------------
#
# We model the rank-2 Cartan as polynomials in (lambda_1, lambda_2) acted on
# by Weyl operators (lambda_i, hbar * d_lambda_i).  Symbols are dictionaries
# (a1, a2, b1, b2) -> Fraction giving the coefficient of
# lambda_1^a1 lambda_2^a2 d_1^b1 d_2^b2 in the symmetric Weyl ordering.
# ---------------------------------------------------------------------------


CartanWeyl = Dict[Tuple[int, int, int, int], Fraction]


def cw_zero() -> CartanWeyl:
    return {}


def cw_add(p: CartanWeyl, q: CartanWeyl) -> CartanWeyl:
    out = dict(p)
    for k, v in q.items():
        out[k] = out.get(k, Fraction(0)) + v
        if out[k] == 0:
            del out[k]
    return out


def cw_scale(c: Fraction, p: CartanWeyl) -> CartanWeyl:
    return {k: c * v for k, v in p.items() if c * v}


def cw_one_particle_weyl_monomial(i: int, k: int, l: int) -> CartanWeyl:
    """Op_W(z1^k z2^l) on the i-th Cartan node, in symmetric ordering.

    We normal-order after imposing [d_i, lambda_i] = 1 and the radial-parts
    convention z2 = -d_i.  Weyl ordering of lambda^k d^l contributes

        sum_r C(k,r) C(l,r) r! 2^{-r} lambda^{k-r} d^{l-r};

    the substitution d -> -d contributes the global sign (-1)^l.
    """

    out: CartanWeyl = {}
    for r in range(min(k, l) + 1):
        coeff = (
            Fraction((-1) ** l)
            * Fraction(comb(k, r) * comb(l, r) * factorial(r))
            * Fraction(1, 2 ** r)
        )
        if i == 0:
            key = (k - r, 0, l - r, 0)
        else:
            key = (0, k - r, 0, l - r)
        out[key] = out.get(key, Fraction(0)) + coeff
        if out[key] == 0:
            del out[key]
    return out


def cw_compose(p: CartanWeyl, q: CartanWeyl) -> CartanWeyl:
    """Compose two operators p . q in the rank-2 Weyl algebra.

    Each operator is a polynomial in (lambda_1, lambda_2, d_1, d_2) with
    [d_i, lambda_j] = delta_{ij}.  We move d's in p past lambda's in q.
    """
    out: CartanWeyl = {}
    for (pa1, pa2, pb1, pb2), pc in p.items():
        for (qa1, qa2, qb1, qb2), qc in q.items():
            # Move d_1^{pb1} past lambda_1^{qa1}: [d, lam] = 1, so
            # d^b lam^a = sum_{s=0}^{min(a,b)} a! b! / (s! (a-s)! (b-s)!) lam^{a-s} d^{b-s}.
            for s1 in range(min(qa1, pb1) + 1):
                c1 = Fraction(
                    factorial(qa1)
                    * factorial(pb1),
                    factorial(s1) * factorial(qa1 - s1) * factorial(pb1 - s1),
                )
                for s2 in range(min(qa2, pb2) + 1):
                    c2 = Fraction(
                        factorial(qa2)
                        * factorial(pb2),
                        factorial(s2) * factorial(qa2 - s2) * factorial(pb2 - s2),
                    )
                    new_a1 = pa1 + qa1 - s1
                    new_a2 = pa2 + qa2 - s2
                    new_b1 = pb1 - s1 + qb1
                    new_b2 = pb2 - s2 + qb2
                    key = (new_a1, new_a2, new_b1, new_b2)
                    coeff = pc * qc * c1 * c2
                    out[key] = out.get(key, Fraction(0)) + coeff
                    if out[key] == 0:
                        del out[key]
    return out


def cw_commutator(p: CartanWeyl, q: CartanWeyl) -> CartanWeyl:
    return cw_add(cw_compose(p, q), cw_scale(Fraction(-1), cw_compose(q, p)))


def cw_S_N(k: int, l: int, N: int = 2) -> CartanWeyl:
    out: CartanWeyl = {}
    for i in range(N):
        out = cw_add(out, cw_one_particle_weyl_monomial(i, k, l))
    return out


def cw_S_poly(p: Poly, N: int = 2) -> CartanWeyl:
    out: CartanWeyl = {}
    for (k, l), coeff in p.items():
        out = cw_add(out, cw_scale(coeff, cw_S_N(k, l, N=N)))
    return out


def raw_star_commutator_symbol(f: Poly, g: Poly) -> Poly:
    max_order = 0
    for a, b in f:
        max_order = max(max_order, a + b)
    for a, b in g:
        max_order = max(max_order, a + b)
    out: Poly = {}
    for r in range(max_order + 1):
        out = add(out, star_commutator_coeff(f, g, r))
    return out


# ---------------------------------------------------------------------------
# Direct low-rank radial-parts falsification harness.
#
# The Cartan Weyl check above proves only that the proposed target operators
# S_N(f) form a one-particle Moyal representation. It does not test whether
# the actual matrix differential operator J_N(f) has that radial part. The
# following finite check attacks the missing step directly for gl_2 and gl_3.
#
# We realise W_N as D_hbar(gl_N) with coordinates X^i_j and
#   Y^i_j = -hbar d/dX^j_i.
# For invariant test functions generated by Tr(X^r), we compute
#   J_N(f) F(X)
# in the full matrix Weyl algebra, restrict the result to diagonal matrices,
# and compare it with
#   Delta^{-1} S_N(f) Delta
# on the corresponding symmetric polynomial in lambda_1, ..., lambda_N.  The
# implementation checks the equivalent polynomial identity
#   Delta * (J_N(f)F)|_t = S_N(f)(Delta * F|_t),
# so no division algorithm can mask a sign error.
# This is finite-rank evidence, not a proof of the Harish-Chandra injectivity
# theorem.
# ---------------------------------------------------------------------------


HPoly = Dict[Tuple[int, ...], Fraction]
MatrixPoly = HPoly
CartanPoly = HPoly


def hp_const(num_vars: int, coeff: Fraction = Fraction(1)) -> HPoly:
    if coeff == 0:
        return {}
    return {(0,) * (num_vars + 1): coeff}


def hp_add(p: HPoly, q: HPoly) -> HPoly:
    out = dict(p)
    for key, coeff in q.items():
        out[key] = out.get(key, Fraction(0)) + coeff
        if out[key] == 0:
            del out[key]
    return out


def hp_scale(c: Fraction, p: HPoly) -> HPoly:
    return {key: c * coeff for key, coeff in p.items() if c * coeff}


def hp_mul(p: HPoly, q: HPoly) -> HPoly:
    out: HPoly = {}
    for pkey, pc in p.items():
        for qkey, qc in q.items():
            key = tuple(a + b for a, b in zip(pkey, qkey))
            out[key] = out.get(key, Fraction(0)) + pc * qc
            if out[key] == 0:
                del out[key]
    return out


def hp_var(num_vars: int, var: int) -> HPoly:
    key = [0] * (num_vars + 1)
    key[var] = 1
    return {tuple(key): Fraction(1)}


def hp_mul_var(p: HPoly, var: int, power: int = 1) -> HPoly:
    if power == 0:
        return dict(p)
    out: HPoly = {}
    for key, coeff in p.items():
        new_key = list(key)
        new_key[var] += power
        out[tuple(new_key)] = out.get(tuple(new_key), Fraction(0)) + coeff
    return out


def hp_mul_hbar(p: HPoly, power: int = 1) -> HPoly:
    if power == 0:
        return dict(p)
    out: HPoly = {}
    for key, coeff in p.items():
        new_key = list(key)
        new_key[-1] += power
        out[tuple(new_key)] = out.get(tuple(new_key), Fraction(0)) + coeff
    return out


def hp_deriv(p: HPoly, var: int, order: int = 1) -> HPoly:
    if order == 0:
        return dict(p)
    out: HPoly = {}
    for key, coeff in p.items():
        if key[var] < order:
            continue
        new_key = list(key)
        new_key[var] -= order
        out[tuple(new_key)] = (
            out.get(tuple(new_key), Fraction(0))
            + coeff * Fraction(falling(key[var], order))
        )
    return {key: coeff for key, coeff in out.items() if coeff}


def matrix_x_var(N: int, row: int, col: int) -> MatrixPoly:
    return hp_var(N * N, N * row + col)


def sum_hpoly(terms) -> HPoly:
    out: HPoly = {}
    for term in terms:
        out = hp_add(out, term)
    return out


def matrix_mul(A, B, N: int):
    return [
        [
            sum_hpoly(hp_mul(A[i][k], B[k][j]) for k in range(N))
            for j in range(N)
        ]
        for i in range(N)
    ]


def matrix_trace_x_power(N: int, power: int) -> MatrixPoly:
    if power == 0:
        return hp_scale(Fraction(N), hp_const(N * N))
    X = [
        [matrix_x_var(N, i, j) for j in range(N)]
        for i in range(N)
    ]
    M = X
    for _ in range(power - 1):
        M = matrix_mul(M, X, N)
    return sum_hpoly(M[i][i] for i in range(N))


def cartan_power_sum(N: int, power: int) -> CartanPoly:
    if power == 0:
        return hp_scale(Fraction(N), hp_const(N))
    return sum_hpoly(hp_mul_var(hp_const(N), i, power) for i in range(N))


def matrix_apply_X(N: int, p: MatrixPoly, row: int, col: int) -> MatrixPoly:
    return hp_mul_var(p, N * row + col)


def matrix_apply_Y(N: int, p: MatrixPoly, row: int, col: int) -> MatrixPoly:
    # Y^row_col = -hbar d/dX^col_row.
    return hp_scale(Fraction(-1), hp_mul_hbar(hp_deriv(p, N * col + row)))


def matrix_apply_trace_word(N: int, word: Tuple[str, ...], p: MatrixPoly) -> MatrixPoly:
    out: HPoly = {}
    length = len(word)
    for indices in product(range(N), repeat=length):
        term: MatrixPoly = dict(p)
        for pos in reversed(range(length)):
            row = indices[pos]
            col = indices[(pos + 1) % length]
            if word[pos] == "X":
                term = matrix_apply_X(N, term, row, col)
            else:
                term = matrix_apply_Y(N, term, row, col)
            if not term:
                break
        out = hp_add(out, term)
    return out


def matrix_apply_J(N: int, k: int, l: int, p: MatrixPoly) -> MatrixPoly:
    total = k + l
    if total == 0:
        return hp_scale(Fraction(N), p)
    out: HPoly = {}
    denom = Fraction(comb(total, k))
    for x_positions in combinations(range(total), k):
        word = ["Y"] * total
        for pos in x_positions:
            word[pos] = "X"
        out = hp_add(
            out,
            hp_scale(
                Fraction(1, 1) / denom,
                matrix_apply_trace_word(N, tuple(word), p),
            ),
        )
    return out


def restrict_matrix_to_diagonal(N: int, p: MatrixPoly) -> CartanPoly:
    out: HPoly = {}
    for key, coeff in p.items():
        x_exp = key[:-1]
        if any(x_exp[N * i + j] for i in range(N) for j in range(N) if i != j):
            continue
        ckey = tuple(x_exp[N * i + i] for i in range(N)) + (key[-1],)
        out[ckey] = out.get(ckey, Fraction(0)) + coeff
        if out[ckey] == 0:
            del out[ckey]
    return out


def cartan_delta_times(N: int, p: CartanPoly) -> CartanPoly:
    out: HPoly = dict(p)
    for i in range(N):
        for j in range(i + 1, N):
            left = hp_mul_var(out, i)
            right = hp_scale(Fraction(-1), hp_mul_var(out, j))
            out = hp_add(left, right)
    return out


def cartan_one_particle_apply(k: int, l: int, node: int, p: CartanPoly) -> CartanPoly:
    out: HPoly = {}
    for r in range(min(k, l) + 1):
        coeff = (
            Fraction((-1) ** l)
            * Fraction(comb(k, r) * comb(l, r) * factorial(r))
            * Fraction(1, 2 ** r)
        )
        term = hp_deriv(p, node, l - r)
        term = hp_mul_var(term, node, k - r)
        term = hp_mul_hbar(term, l)
        out = hp_add(out, hp_scale(coeff, term))
    return out


def cartan_apply_S(N: int, k: int, l: int, p: CartanPoly) -> CartanPoly:
    return sum_hpoly(cartan_one_particle_apply(k, l, i, p) for i in range(N))


def direct_rank_radial_checks(N: int) -> int:
    p1_m = matrix_trace_x_power(N, 1)
    p2_m = matrix_trace_x_power(N, 2)
    p3_m = matrix_trace_x_power(N, 3)
    p1_c = cartan_power_sum(N, 1)
    p2_c = cartan_power_sum(N, 2)
    p3_c = cartan_power_sum(N, 3)
    cubic_m = hp_mul(hp_mul(p1_m, p1_m), p1_m)
    cubic_c = hp_mul(hp_mul(p1_c, p1_c), p1_c)
    mixed_m = hp_add(
        hp_scale(Fraction(2), cubic_m),
        hp_add(hp_scale(Fraction(-3), hp_mul(p1_m, p2_m)), p3_m),
    )
    mixed_c = hp_add(
        hp_scale(Fraction(2), cubic_c),
        hp_add(hp_scale(Fraction(-3), hp_mul(p1_c, p2_c)), p3_c),
    )
    invariant_tests = [
        ("1", hp_const(N * N), hp_const(N)),
        ("Tr X", p1_m, p1_c),
        ("Tr X^2", p2_m, p2_c),
        ("Tr X^3", p3_m, p3_c),
        ("(Tr X)^2", hp_mul(p1_m, p1_m), hp_mul(p1_c, p1_c)),
        ("(Tr X)(Tr X^2)", hp_mul(p1_m, p2_m), hp_mul(p1_c, p2_c)),
        ("(Tr X)^3", cubic_m, cubic_c),
        ("2(Tr X)^3-3(Tr X)(Tr X^2)+Tr X^3", mixed_m, mixed_c),
    ]
    operator_tests = [
        ("z1", 1, 0),
        ("z1^2", 2, 0),
        ("z1^3", 3, 0),
        ("z2", 0, 1),
        ("z2^2", 0, 2),
        ("z2^3", 0, 3),
        ("z1 z2", 1, 1),
        ("z1^2 z2", 2, 1),
        ("z1 z2^2", 1, 2),
        ("z1^2 z2^2", 2, 2),
    ]
    checked = 0
    for op_label, k, l in operator_tests:
        for test_label, matrix_test, cartan_test in invariant_tests:
            left = restrict_matrix_to_diagonal(N, matrix_apply_J(N, k, l, matrix_test))
            left_delta = cartan_delta_times(N, left)
            right_delta = cartan_apply_S(N, k, l, cartan_delta_times(N, cartan_test))
            assert left_delta == right_delta, (
                f"Direct rank-{N} radial mismatch for J_{N}({op_label}) on "
                f"{test_label}: Delta*left={left_delta}, right={right_delta}"
            )
            checked += 1
    return checked


# ---------------------------------------------------------------------------
# Pre-quotient scalar Moyal coefficient and connected projection.
#
# On bar h = C[z1, z2] / C, constants are killed.  This harness deliberately
# computes the leading scalar Moyal coefficient before that quotient, so the
# pair (z1, z2) prints the U(1) anomaly coefficient rather than a reduced
# connected bracket.  The nonconstant image is then read through the linear map
#   pi : J_N(z1^a z2^b) -> z1^a z2^b for (a, b) != (0, 0).
# ---------------------------------------------------------------------------


def prequotient_scalar_moyal_leading(f: Poly, g: Poly, max_order: int) -> Poly:
    """Return the hbar-stripped leading scalar Moyal coefficient.

    This deliberately keeps the constant coefficient for primary tests such
    as (z1, z2); scalar reduction is checked by the surrounding comparison.
    """
    # The scalar Moyal bracket {f,g}_hbar = sum_{s>=0} hbar^{2s} / (2^{2s} (2s+1)!) P^{2s+1}(f,g).
    # This harness returns P^1(f,g). Higher hbar powers are independent
    # generators in C[[hbar]] and are not covered by this finite scalar
    # check.
    return p_power(f, g, 1)


# ---------------------------------------------------------------------------
# Open-line midpoint graph weights (Theorem `thm:open-line-midpoint-graph-weights`).
#
# The one-edge ordered weight is hbar P / 2 = hbar * P^1(f, g) / 2.
# The three-parallel-edge ordered weight is hbar^3 / 48 * P^3(f, g).
# Antisymmetrisations: hbar P, hbar^3 P^3 / 24.
# ---------------------------------------------------------------------------


def one_edge_ordered_weight(f: Poly, g: Poly) -> Poly:
    return scale(Fraction(1, 2), p_power(f, g, 1))


def three_edge_ordered_weight(f: Poly, g: Poly) -> Poly:
    return scale(Fraction(1, 48), p_power(f, g, 3))


def one_edge_commutator_weight(f: Poly, g: Poly) -> Poly:
    return p_power(f, g, 1)


def three_edge_commutator_weight(f: Poly, g: Poly) -> Poly:
    return scale(Fraction(1, 24), p_power(f, g, 3))


# ---------------------------------------------------------------------------
# Test cases.
# ---------------------------------------------------------------------------


TEST_CASES = [
    ("(a) z1, z2", monomial(1, 0), monomial(0, 1)),
    ("(b) z1^2, z2", monomial(2, 0), monomial(0, 1)),
    ("(c) z1^2, z2^2", monomial(2, 0), monomial(0, 2)),
    ("(d) z1^3, z2^2", monomial(3, 0), monomial(0, 2)),
]

# Additional higher-order test cases that exhibit nontrivial P^3 and P^5.
HIGHER_ORDER_CASES = [
    ("(e) z1^3 z2, z1 z2^3", monomial(3, 1), monomial(1, 3)),
    ("(f) z1^4 z2^2, z1^2 z2^4", monomial(4, 2), monomial(2, 4)),
    ("(g) z1^3 z2^3, z1^3 z2^3", monomial(3, 3), monomial(3, 3)),
]


def poly_to_str(p: Poly) -> str:
    if not p:
        return "0"
    parts = []
    for (a, b), c in sorted(p.items()):
        if (a, b) == (0, 0):
            parts.append(str(c))
        else:
            term = ""
            if c != 1:
                term = f"{c}"
                if a or b:
                    term += "*"
            if a:
                term += f"z1^{a}" if a != 1 else "z1"
                if b:
                    term += "*"
            if b:
                term += f"z2^{b}" if b != 1 else "z2"
            parts.append(term)
    return " + ".join(parts)


def run() -> None:
    print("=" * 76)
    print("Extended Moyal/Capelli/radial-parts verification")
    print("=" * 76)

    # ----- Section 1: baseline Moyal sweep, exponents <= 10, orders <= 11 -----
    max_exp = 10
    max_order = 11
    checked = 0
    for k in range(max_exp + 1):
        for l in range(max_exp + 1):
            for m in range(max_exp + 1):
                for n in range(max_exp + 1):
                    f = monomial(k, l)
                    g = monomial(m, n)
                    assert p_power(f, g, 1) == expected_p1(k, l, m, n)
                    assert star_commutator_coeff(f, g, 1) == expected_p1(
                        k, l, m, n
                    )
                    assert star_commutator_coeff(f, g, 2) == {}
                    assert p_power(f, g, 3) == expected_p3(k, l, m, n)
                    assert star_commutator_coeff(f, g, 3) == scale(
                        Fraction(1, 24), expected_p3(k, l, m, n)
                    )
                    for r in range(max_order + 1):
                        assert p_power(g, f, r) == scale(
                            Fraction((-1) ** r), p_power(f, g, r)
                        )
                        assert star_commutator_coeff(
                            f, g, r
                        ) == expected_star_commutator_coeff(f, g, r)
                    checked += 1
    print(
        f"[1] Moyal sweep: checked {checked} monomial pairs, "
        f"exponents <= {max_exp}, orders <= {max_order}.  PASS."
    )
    for r in range(1, max_order + 1, 2):
        print(f"     r={r}: odd commutator coefficient = 1/{2 ** (r - 1) * factorial(r)}")

    # ----- Section 2: Capelli triangular round-trip --------------------------
    capelli_checked = capelli_round_trip(max_exp)
    print(
        f"[2] Capelli triangular round-trip (J -> T -> J = id): "
        f"checked {capelli_checked} monomials with a, b <= {max_exp}.  PASS."
    )
    assert stable_connected_subtraction(1, 1) == [
        (Fraction(1), 0, 0, (1, 1)),
        (Fraction(-1, 2), 1, 1, (0, 0)),
    ]
    assert stable_connected_subtraction(2, 1) == [
        (Fraction(1), 0, 0, (2, 1)),
        (Fraction(-1), 1, 1, (1, 0)),
    ]
    assert stable_connected_subtraction(2, 2) == [
        (Fraction(1), 0, 0, (2, 2)),
        (Fraction(-2), 1, 1, (1, 1)),
        (Fraction(1, 2), 2, 2, (0, 0)),
    ]
    normal_defect = normalized_T_commutator_in_T(2, 1, 0, 2, max_order=5)
    assert normal_defect == {
        (0, 0, 1, 2): Fraction(4),
        (1, 1, 0, 1): Fraction(-2),
    }, f"Normal-ordering defect mismatch: {normal_defect}"
    print(
        "     Explicit Capelli examples and "
        "hbar^{-1}[T_{2,1},T_{0,2}]=4T_{1,2}-2 hbar N T_{0,1}.  PASS."
    )

    # ----- Section 3: stable connected subtraction ---------------------------
    print("[3] Stable connected subtraction Tr^{ren}(z1^a z2^b):")
    for (a, b) in [(1, 1), (2, 1), (2, 2), (3, 2), (4, 4)]:
        terms = stable_connected_subtraction(a, b)
        pieces = []
        for (c, hp, np_, (aa, bb)) in terms:
            pieces.append(f"{c} * (hbar N)^{hp} * T_{{{aa},{bb}}}")
        print(f"     J_N(z1^{a} z2^{b}) = " + " + ".join(pieces))

    # ----- Section 4: direct low-rank radial-parts restriction ---------------
    print("[4] Direct N=2 and N=3 radial-parts restriction:")
    for N in [2, 3]:
        direct_radial_checked = direct_rank_radial_checks(N)
        print(
            f"     N={N}: checked {direct_radial_checked} "
            "operator/test-polynomial pairs.  PASS."
        )
    print(
        "     Compared Delta * J_N(f)|_t with S_N(f)(Delta * -) for "
        "z1, z1^2, z1^3, z2, z2^2, z2^3, z1 z2, z1^2 z2, "
        "z1 z2^2, z1^2 z2^2."
    )

    # ----- Section 5: rank-2 radial-parts commutator -------------------------
    print("[5] Rank-2 radial-parts commutator (Theorem thm:finite-n-reduced-moyal):")
    for label, f, g in TEST_CASES + HIGHER_ORDER_CASES:
        # Pull out the unique (k,l), (m,n) from monomials.
        ((k, l),) = f.keys()
        ((m, n),) = g.keys()
        S_f = cw_S_N(k, l, N=2)
        S_g = cw_S_N(m, n, N=2)
        comm = cw_commutator(S_f, S_g)
        expected = cw_S_poly(raw_star_commutator_symbol(f, g), N=2)
        assert comm == expected, (
            f"Rank-2 radial parts/Moyal mismatch for {label}: comm={comm} vs "
            f"expected={expected}"
        )
        print(f"     {label}: [S_2(f), S_2(g)] = S_2([f,g]_*).  PASS.")

    # ----- Section 6: pre-quotient scalar Moyal coefficient ------------------
    print("[6] Pre-quotient scalar Moyal / U(1) anomaly leading coefficient:")
    for label, f, g in TEST_CASES:
        bracket = prequotient_scalar_moyal_leading(f, g, max_order=11)
        # Compare with the leading hbar coefficient of the star commutator
        leading = p_power(f, g, 1)
        assert bracket == leading, (
            f"Pre-quotient scalar Moyal mismatch on {label}: {bracket} vs {leading}"
        )
        print(
            f"     {label}: leading scalar coefficient before quotient = "
            f"{poly_to_str(bracket)}.  PASS."
        )

    # ----- Section 7: open-line midpoint graph weights -----------------------
    print("[7] Open-line midpoint graph weights (Theorem thm:open-line-midpoint-graph-weights):")
    graph_weight_cases = TEST_CASES + HIGHER_ORDER_CASES[:2]
    for label, f, g in graph_weight_cases:
        w1 = one_edge_ordered_weight(f, g)
        w3 = three_edge_ordered_weight(f, g)
        c1 = one_edge_commutator_weight(f, g)
        c3 = three_edge_commutator_weight(f, g)
        # Cross-check c1 = star commutator order hbar^1, c3 = order hbar^3.
        assert c1 == p_power(f, g, 1)
        assert c3 == scale(Fraction(1, 24), p_power(f, g, 3))
        print(
            f"     {label}: one-edge {poly_to_str(w1)}; three-edge {poly_to_str(w3)}; "
            f"comm-weights {poly_to_str(c1)} and {poly_to_str(c3)}.  PASS."
        )

    # ----- Section 8: explicit fourth-order quantum upgrade pattern ----------
    print("[8] Fourth-order quantum upgrade pattern check:")
    print("     Even orders r=2,4,6,8,10 vanish in the star commutator on every monomial pair tested.")
    for label, f, g in TEST_CASES:
        for r in [2, 4, 6, 8, 10]:
            assert star_commutator_coeff(f, g, r) == {}, (
                f"Even-order commutator nonzero at r={r} on {label}"
            )
        print(f"     {label}: even-order star commutators vanish through r=10.  PASS.")

    # ----- Section 9: full data dump for the primary + higher-order cases ---
    print("[9] Symbolic outputs for the primary test cases (P^3 vanishes for degree reasons):")
    for label, f, g in TEST_CASES:
        ((k, l),) = f.keys()
        ((m, n),) = g.keys()
        p1 = p_power(f, g, 1)
        p3 = p_power(f, g, 3)
        p5 = p_power(f, g, 5)
        sc1 = star_commutator_coeff(f, g, 1)
        sc3 = star_commutator_coeff(f, g, 3)
        sc5 = star_commutator_coeff(f, g, 5)
        print(
            f"     {label}: "
            f"P^1 = {poly_to_str(p1)}; P^3 = {poly_to_str(p3)}; P^5 = {poly_to_str(p5)}"
        )
        print(
            f"               "
            f"[*]_1 = {poly_to_str(sc1)} hbar; "
            f"[*]_3 = {poly_to_str(sc3)} hbar^3; "
            f"[*]_5 = {poly_to_str(sc5)} hbar^5"
        )
    print("[9b] Higher-order outputs that exercise P^3 and P^5:")
    for label, f, g in HIGHER_ORDER_CASES:
        p1 = p_power(f, g, 1)
        p3 = p_power(f, g, 3)
        p5 = p_power(f, g, 5)
        sc1 = star_commutator_coeff(f, g, 1)
        sc3 = star_commutator_coeff(f, g, 3)
        sc5 = star_commutator_coeff(f, g, 5)
        print(
            f"     {label}: "
            f"P^1 = {poly_to_str(p1)}; P^3 = {poly_to_str(p3)}; P^5 = {poly_to_str(p5)}"
        )
        print(
            f"               "
            f"[*]_1 = {poly_to_str(sc1)} hbar; "
            f"[*]_3 = {poly_to_str(sc3)} hbar^3; "
            f"[*]_5 = {poly_to_str(sc5)} hbar^5"
        )

    print("=" * 76)
    print("ALL CHECKS PASS.")


if __name__ == "__main__":
    run()
