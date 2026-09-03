#!/usr/bin/env python3
"""Exact free-algebra check for the fixed-rank Lie defect and its homotopy."""

from collections import defaultdict


def add(*polynomials):
    result = defaultdict(int)
    for polynomial in polynomials:
        for word, coefficient in polynomial.items():
            result[word] += coefficient
    return {word: coefficient for word, coefficient in result.items() if coefficient}


def scale(coefficient, polynomial):
    return {
        word: coefficient * value
        for word, value in polynomial.items()
        if coefficient * value
    }


def monomial(*letters):
    return {tuple(letters): 1}


def multiply(left, right):
    result = defaultdict(int)
    for left_word, left_coefficient in left.items():
        for right_word, right_coefficient in right.items():
            result[left_word + right_word] += left_coefficient * right_coefficient
    return {word: coefficient for word, coefficient in result.items() if coefficient}


ONE = monomial()
X = monomial("x")
Y = monomial("y")
PSI = monomial("p")
MU = add(multiply(X, Y), scale(-1, multiply(Y, X)))


def letter_degree(letter):
    return -1 if letter == "p" else 0


def derivation_on_word(word, values, degree):
    result = {}
    prefix_degree = 0
    for index, letter in enumerate(word):
        sign = -1 if (degree * prefix_degree) % 2 else 1
        prefix = {tuple(word[:index]): 1}
        suffix = {tuple(word[index + 1 :]): 1}
        result = add(
            result,
            scale(sign, multiply(multiply(prefix, values[letter]), suffix)),
        )
        prefix_degree += letter_degree(letter)
    return result


def derivation(polynomial, values, degree):
    result = {}
    for word, coefficient in polynomial.items():
        result = add(
            result,
            scale(coefficient, derivation_on_word(word, values, degree)),
        )
    return result


Q_VALUES = {"x": {}, "y": {}, "p": MU}
XF_VALUES = {
    "x": scale(-1, multiply(X, X)),
    "y": scale(2, multiply(X, Y)),
    "p": add(multiply(X, PSI), scale(-1, multiply(PSI, X))),
}
XG_VALUES = {
    "x": scale(-2, multiply(X, Y)),
    "y": multiply(Y, Y),
    "p": add(multiply(Y, PSI), scale(-1, multiply(PSI, Y))),
}
XH_VALUES = {
    "x": scale(-6, multiply(multiply(X, X), Y)),
    "y": scale(6, multiply(multiply(X, Y), Y)),
    "p": scale(
        3,
        add(
            multiply(add(multiply(X, Y), multiply(Y, X)), PSI),
            scale(-1, multiply(PSI, add(multiply(X, Y), multiply(Y, X)))),
        ),
    ),
}
K_VALUES = {
    "x": scale(2, multiply(X, PSI)),
    "y": scale(-2, multiply(PSI, Y)),
    "p": {},
}


def compose(values_left, degree_left, values_right, degree_right, letter):
    del degree_right
    return derivation(values_right[letter], values_left, degree_left)


def commutator(values_left, degree_left, values_right, degree_right, letter):
    sign = -1 if (degree_left * degree_right) % 2 else 1
    return add(
        compose(values_left, degree_left, values_right, degree_right, letter),
        scale(
            -sign,
            compose(values_right, degree_right, values_left, degree_left, letter),
        ),
    )


def assert_equal(actual, expected, label):
    if actual != expected:
        raise AssertionError(f"{label}: expected {expected}, got {actual}")
    print(f"PASS {label}")


def cyclic_normal_form(polynomial):
    result = defaultdict(int)
    for word, coefficient in polynomial.items():
        rotations = [word[index:] + word[:index] for index in range(len(word))]
        result[min(rotations) if rotations else tuple()] += coefficient
    return {word: coefficient for word, coefficient in result.items() if coefficient}


for name, values in (("f", XF_VALUES), ("g", XG_VALUES), ("h", XH_VALUES)):
    for letter in ("x", "y", "p"):
        assert_equal(
            commutator(Q_VALUES, 1, values, 0, letter),
            {},
            f"[Q,X_{name}]({letter})=0",
        )

delta_expected = {
    "x": scale(2, multiply(X, MU)),
    "y": scale(-2, multiply(MU, Y)),
    "p": scale(
        2,
        add(
            multiply(PSI, multiply(Y, X)),
            scale(-1, multiply(multiply(Y, X), PSI)),
        ),
    ),
}
for letter in ("x", "y", "p"):
    delta = add(
        commutator(XF_VALUES, 0, XG_VALUES, 0, letter),
        scale(-1, XH_VALUES[letter]),
    )
    assert_equal(delta, delta_expected[letter], f"Lie defect on {letter}")
    assert_equal(
        commutator(Q_VALUES, 1, K_VALUES, -1, letter),
        delta_expected[letter],
        f"[Q,K]({letter})=defect",
    )

g = multiply(multiply(X, Y), Y)
h = scale(3, multiply(multiply(X, X), multiply(Y, Y)))
trace_defect = add(derivation(g, XF_VALUES, 0), scale(-1, h))
trace_primitive = scale(-2, multiply(multiply(PSI, Y), X))
assert_equal(
    cyclic_normal_form(trace_defect),
    cyclic_normal_form(derivation(trace_primitive, Q_VALUES, 1)),
    "trace-action defect is Q-boundary",
)


def matrix_multiply(left, right):
    return [
        [
            sum(left[row][index] * right[index][column] for index in range(2))
            for column in range(2)
        ]
        for row in range(2)
    ]


def matrix_add(left, right):
    return [
        [left[row][column] + right[row][column] for column in range(2)]
        for row in range(2)
    ]


def matrix_scale(coefficient, matrix):
    return [[coefficient * entry for entry in row] for row in matrix]


x_matrix = [[0, 1], [0, 0]]
y_matrix = [[0, 0], [1, 0]]
mu_matrix = matrix_add(
    matrix_multiply(x_matrix, y_matrix),
    matrix_scale(-1, matrix_multiply(y_matrix, x_matrix)),
)
assert_equal(
    {("matrix",): matrix_scale(2, matrix_multiply(x_matrix, mu_matrix))},
    {("matrix",): [[0, -2], [0, 0]]},
    "N=2 defect on x is nonzero",
)
assert_equal(
    {("matrix",): matrix_scale(-2, matrix_multiply(mu_matrix, y_matrix))},
    {("matrix",): [[0, 0], [2, 0]]},
    "N=2 defect on y is nonzero",
)

print("All fixed-rank Lie-defect checks passed.")
