#!/usr/bin/env python3
"""Exact free-algebra checks for the necklace and BRST sign conventions."""

from __future__ import annotations

from collections import defaultdict
from itertools import product
from pathlib import Path


Word = tuple[str, ...]
Poly = dict[Word, int]

DEGREE = {"x": 0, "y": 0, "g": 1, "p": -1}
GENERATORS = tuple(DEGREE)


def clean(poly: Poly) -> Poly:
    return {word: coeff for word, coeff in poly.items() if coeff}


def monomial(*letters: str, coeff: int = 1) -> Poly:
    return {tuple(letters): coeff} if coeff else {}


def add(*polys: Poly) -> Poly:
    out: defaultdict[Word, int] = defaultdict(int)
    for poly in polys:
        for word, coeff in poly.items():
            out[word] += coeff
    return clean(dict(out))


def scale(poly: Poly, scalar: int) -> Poly:
    return clean({word: scalar * coeff for word, coeff in poly.items()})


def multiply(left: Poly, right: Poly) -> Poly:
    out: defaultdict[Word, int] = defaultdict(int)
    for word_l, coeff_l in left.items():
        for word_r, coeff_r in right.items():
            out[word_l + word_r] += coeff_l * coeff_r
    return clean(dict(out))


def word_degree(word: Word) -> int:
    return sum(DEGREE[letter] for letter in word)


def parity(word: Word) -> int:
    return word_degree(word) & 1


def homogeneous_degree(poly: Poly) -> int:
    degrees = {word_degree(word) for word in poly}
    if len(degrees) != 1:
        raise AssertionError(f"polynomial is not nonzero homogeneous: {poly}")
    return degrees.pop()


def derivation(poly: Poly, images: dict[str, Poly], derivation_degree: int) -> Poly:
    """Extend generator images by the graded Leibniz rule."""
    out: defaultdict[Word, int] = defaultdict(int)
    derivation_parity = derivation_degree & 1
    for word, coeff in poly.items():
        prefix_degree = 0
        for index, letter in enumerate(word):
            sign = -1 if derivation_parity * (prefix_degree & 1) & 1 else 1
            prefix = word[:index]
            suffix = word[index + 1 :]
            for image_word, image_coeff in images.get(letter, {}).items():
                out[prefix + image_word + suffix] += coeff * sign * image_coeff
            prefix_degree += DEGREE[letter]
    return clean(dict(out))


def cyclic_representative(word: Word) -> tuple[Word | None, int]:
    """Return c and s with [word] = s[c], or zero for an odd stabilizer."""
    if not word:
        return (), 1
    rotations: list[tuple[Word, int]] = []
    for index in range(len(word)):
        prefix = word[:index]
        suffix = word[index:]
        sign = -1 if parity(prefix) * parity(suffix) & 1 else 1
        rotations.append((suffix + prefix, sign))
    representative = min(rotation for rotation, _ in rotations)
    signs = {sign for rotation, sign in rotations if rotation == representative}
    if len(signs) > 1:
        return None, 0
    return representative, signs.pop()


def cyclicize(poly: Poly) -> Poly:
    out: defaultdict[Word, int] = defaultdict(int)
    for word, coeff in poly.items():
        representative, sign = cyclic_representative(word)
        if representative is not None:
            out[representative] += coeff * sign
    return clean(dict(out))


def cyclic_derivative(cyclic_poly: Poly, letter: str) -> Poly:
    """Left cyclic derivative with the manuscript's Koszul cut sign."""
    out: defaultdict[Word, int] = defaultdict(int)
    letter_parity = DEGREE[letter] & 1
    for word, coeff in cyclic_poly.items():
        for index, current in enumerate(word):
            if current != letter:
                continue
            prefix = word[:index]
            suffix = word[index + 1 :]
            exponent = parity(prefix) * (letter_parity + parity(suffix))
            sign = -1 if exponent & 1 else 1
            out[suffix + prefix] += coeff * sign
    return clean(dict(out))


def hamiltonian_images(cyclic_hamiltonian: Poly, *, full: bool) -> dict[str, Poly]:
    images = {
        "x": scale(cyclic_derivative(cyclic_hamiltonian, "y"), -1),
        "y": cyclic_derivative(cyclic_hamiltonian, "x"),
        "g": {},
        "p": {},
    }
    if full:
        odd_sign = (
            -1
            if cyclic_hamiltonian and homogeneous_degree(cyclic_hamiltonian) & 1
            else 1
        )
        images["g"] = scale(cyclic_derivative(cyclic_hamiltonian, "p"), odd_sign)
        images["p"] = scale(cyclic_derivative(cyclic_hamiltonian, "g"), odd_sign)
    return images


def necklace_formula(left: Poly, right: Poly, *, full: bool) -> Poly:
    terms = [
        multiply(cyclic_derivative(left, "x"), cyclic_derivative(right, "y")),
        scale(
            multiply(cyclic_derivative(left, "y"), cyclic_derivative(right, "x")),
            -1,
        ),
    ]
    if full:
        odd_sign = -1 if homogeneous_degree(left) & 1 else 1
        terms.extend(
            [
                scale(
                    multiply(
                        cyclic_derivative(left, "g"),
                        cyclic_derivative(right, "p"),
                    ),
                    odd_sign,
                ),
                scale(
                    multiply(
                        cyclic_derivative(left, "p"),
                        cyclic_derivative(right, "g"),
                    ),
                    odd_sign,
                ),
            ]
        )
    return cyclicize(add(*terms))


def hamiltonian_action(left: Poly, right: Poly, *, full: bool) -> Poly:
    return cyclicize(
        derivation(
            right,
            hamiltonian_images(left, full=full),
            homogeneous_degree(left),
        )
    )


def commutator_on_generators(left: Poly, right: Poly, *, full: bool) -> dict[str, Poly]:
    degree_l = homogeneous_degree(left)
    degree_r = homogeneous_degree(right)
    sign = -1 if (degree_l * degree_r) & 1 else 1
    images_l = hamiltonian_images(left, full=full)
    images_r = hamiltonian_images(right, full=full)
    return {
        letter: add(
            derivation(images_r[letter], images_l, degree_l),
            scale(derivation(images_l[letter], images_r, degree_r), -sign),
        )
        for letter in GENERATORS
    }


def cyclic_basis(letters: tuple[str, ...], max_length: int) -> list[Poly]:
    representatives: set[Word] = set()
    for length in range(1, max_length + 1):
        for word in product(letters, repeat=length):
            representative, _ = cyclic_representative(word)
            if representative is not None:
                representatives.add(representative)
    return [{word: 1} for word in sorted(representatives)]


def commutative_image(poly: Poly) -> dict[tuple[int, int], int]:
    out: defaultdict[tuple[int, int], int] = defaultdict(int)
    for word, coeff in poly.items():
        if any(letter not in {"x", "y"} for letter in word):
            continue
        out[(word.count("x"), word.count("y"))] += coeff
    return clean(dict(out))  # type: ignore[arg-type,return-value]


def without_gamma(poly: Poly) -> Poly:
    return clean({word: coeff for word, coeff in poly.items() if "g" not in word})


def main() -> None:
    checks = 0

    def check(condition: bool, message: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(message)

    x = cyclicize(monomial("x"))
    y = cyclicize(monomial("y"))
    g = cyclicize(monomial("g"))
    p = cyclicize(monomial("p"))
    scalar = monomial()

    check(necklace_formula(x, y, full=False) == scalar, "{x,y} must be +1")
    check(hamiltonian_action(x, y, full=False) == scalar, "X_x(y) must be +1")
    check(
        hamiltonian_action(y, x, full=False) == scale(scalar, -1),
        "X_y(x) must be -1",
    )
    check(
        necklace_formula(g, p, full=True) == scale(scalar, -1),
        "the odd inverse-pairing bracket {gamma,psi} must be -1",
    )

    f = cyclicize(monomial("x", "x", "y"))
    h = cyclicize(monomial("x", "y", "y"))
    expected_fh = cyclicize(
        add(monomial("x", "x", "y", "y"), monomial("x", "y", "x", "y", coeff=2))
    )
    check(
        necklace_formula(f, h, full=False) == expected_fh,
        "noncommutative necklace bracket has the wrong word coefficients",
    )
    check(
        hamiltonian_action(f, h, full=False) == expected_fh,
        "X_F(G) fails for F=x^2y and G=xy^2",
    )
    check(
        commutative_image(expected_fh) == {(2, 2): 3},
        "normal ordering must recover the coefficient 3",
    )

    expected_commutator = {
        "x": add(
            scale(monomial("y", "x", "x"), -1),
            scale(monomial("x", "y", "x"), -4),
            scale(monomial("x", "x", "y"), -1),
        ),
        "y": add(
            monomial("x", "y", "y"),
            monomial("y", "x", "y", coeff=4),
            monomial("y", "y", "x"),
        ),
        "g": {},
        "p": {},
    }
    commutator = commutator_on_generators(f, h, full=False)
    check(commutator == expected_commutator, "explicit noncommutative commutator changed")
    check(
        commutator == hamiltonian_images(expected_fh, full=False),
        r"[X_F,X_G] is not X_{\{F,G\}} on generators",
    )

    koszul_images = {
        "x": {},
        "y": {},
        "g": {},
        "p": add(monomial("x", "y"), scale(monomial("y", "x"), -1)),
    }
    koszul_basis = cyclic_basis(("x", "y", "p"), 3)
    for left in koszul_basis:
        degree_l = homogeneous_degree(left)
        q_left = cyclicize(derivation(left, koszul_images, 1))
        for right in koszul_basis:
            bracket = necklace_formula(left, right, full=False)
            action = hamiltonian_action(left, right, full=False)
            check(action == bracket, "X_F(G) failed in the cyclic Koszul sweep")
            reverse = necklace_formula(right, left, full=False)
            antisymmetry_sign = -(-1 if (degree_l * homogeneous_degree(right)) & 1 else 1)
            check(
                bracket == scale(reverse, antisymmetry_sign),
                "graded antisymmetry failed in the cyclic Koszul sweep",
            )
            check(
                commutator_on_generators(left, right, full=False)
                == hamiltonian_images(bracket, full=False),
                r"[X_F,X_G] is not X_{\{F,G\}} in the cyclic Koszul sweep",
            )
            q_right = cyclicize(derivation(right, koszul_images, 1))
            q_bracket = cyclicize(derivation(bracket, koszul_images, 1))
            derivation_rhs = add(
                necklace_formula(q_left, right, full=False) if q_left else {},
                scale(
                    necklace_formula(left, q_right, full=False) if q_right else {},
                    -1 if degree_l & 1 else 1,
                ),
            )
            check(q_bracket == derivation_rhs, "Q is not a necklace-bracket derivation")

    full_basis = cyclic_basis(("x", "y", "g", "p"), 2)
    for left in full_basis:
        degree_l = homogeneous_degree(left)
        for right in full_basis:
            bracket = necklace_formula(left, right, full=True)
            check(
                hamiltonian_action(left, right, full=True) == bracket,
                "full graded Hamiltonian action does not equal the bracket",
            )
            reverse = necklace_formula(right, left, full=True)
            antisymmetry_sign = -(-1 if (degree_l * homogeneous_degree(right)) & 1 else 1)
            check(
                bracket == scale(reverse, antisymmetry_sign),
                "full graded antisymmetry failed",
            )
            commutator = commutator_on_generators(left, right, full=True)
            expected = hamiltonian_images(bracket, full=True)
            check(commutator == expected, "full graded Hamiltonian commutator failed")

    mu = add(monomial("x", "y"), scale(monomial("y", "x"), -1))
    s = cyclicize(
        add(
            scale(multiply(monomial("g"), mu), -1),
            scale(monomial("p", "g", "g"), -1),
        )
    )
    q_images = hamiltonian_images(s, full=True)
    expected_q = {
        "g": monomial("g", "g"),
        "x": add(monomial("g", "x"), scale(monomial("x", "g"), -1)),
        "y": add(monomial("g", "y"), scale(monomial("y", "g"), -1)),
        "p": add(
            mu,
            monomial("g", "p"),
            monomial("p", "g"),
        ),
    }
    for letter in GENERATORS:
        check(q_images[letter] == expected_q[letter], f"wrong BRST value on {letter}")
        check(
            derivation(q_images[letter], q_images, 1) == {},
            f"Q^2 is nonzero on {letter}",
        )
    check(without_gamma(q_images["p"]) == mu, "gamma=0 must recover Q psi=[x,y]")
    check(necklace_formula(s, s, full=True) == {}, "the cyclic master equation failed")
    check(hamiltonian_action(s, s, full=True) == {}, "X_S(S) is nonzero")
    even_master = cyclicize(
        multiply(
            add(monomial("g", "y"), scale(monomial("y", "g"), -1)),
            add(monomial("x", "g"), scale(monomial("g", "x"), -1)),
        )
    )
    check(
        even_master == cyclicize(multiply(mu, monomial("g", "g"))),
        "the even part of the displayed master-equation cancellation failed",
    )
    ghost_master = cyclicize(
        multiply(
            add(monomial("g", "p"), monomial("p", "g")),
            monomial("g", "g"),
        )
    )
    check(ghost_master == {}, "the odd cyclic master-equation cancellation failed")
    check(
        necklace_formula(g, cyclicize(monomial("p", "x")), full=True)
        == cyclicize(scale(monomial("x"), -1)),
        "the gauge-paired nonzero defect must have sign -[x]",
    )

    main_source = Path("main.tex").read_text(encoding="utf-8")
    appendix_source = Path("appendix-sign-conventions.tex").read_text(encoding="utf-8")
    check("X_F(x)=-\\partial_yF" in main_source, "main source lost X_F(x) sign")
    check("X_F(y)=\\partial_xF" in main_source, "main source lost X_F(y) sign")
    check("X_F(\\gamma)=(-1)^{|F|}\\partial_\\psi F" in main_source, "main source lost odd sign")
    check("X_F(\\psi)=(-1)^{|F|}\\partial_\\gamma F" in main_source, "main source lost odd sign")
    check("S=-[\\gamma(xy-yx)]-[\\psi\\gamma\\gamma]" in main_source, "main source lost S sign")
    check("X_F(x)=\\partial_yF" not in main_source, "opposite X_F(x) sign remains")
    check("X_F(y)=-\\partial_xF" not in main_source, "opposite X_F(y) sign remains")
    check("\\iota_{X_F}\\omega=-dF" in appendix_source, "appendix lost contraction convention")
    check("\\{[\\gamma],[\\psi]\\}_{\\mathrm{neck}}=-[1]" in appendix_source, "appendix lost odd coordinate bracket")

    print(f"necklace/Hamiltonian sign checks passed: {checks}")


if __name__ == "__main__":
    main()
