# Agent 300 Report: BMK All-Window / Pro-Matlis Transfer Construction Push

Date: 2026-04-30.

Owned files:

- `reconstitution/bmk-all-window-pro-matlis-transfer-construction-push-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-300-bmk-all-window-pro-matlis-transfer-construction-push.md`

No manuscript TeX was edited.

## Claim Attacked

After the strict finite support-local quotient and the projected finite
\(L_\infty\) escape package fail, the attacked claim is that a strict
all-window/pro-Matlis BMK transfer can replace them by retaining all
principal parts and constructing compatible \(H_\chi^0\), collar
primitives, and uniform estimates.

## Finding

The strongest positive construction is one-pair and analytic:

\[
  \bar\partial H_\chi^0+H_\chi^0\bar\partial
    =
  \operatorname{id}-I_{\mathrm{an}}P_{\mathrm{an}}
\]

after choosing the full analytic BMK retract, imposing the usual side
conditions, fixing the diagonal orientation, and passing to the collar
quotient.  Taylor coordinates give a compatible pro-analytic moment map

\[
  P_{\Pi}^{\mathrm{an}}\colon
  C^\bullet(B_2,B_1)\to
  \mathcal P_{\mathrm{an}}(B_1)
  \subset
  \widehat{\mathcal P}_\Pi
  =
  \prod_{a+b>0}\C\rho_{a,b}.
\]

This is not a native all-window current \(E_2\) transfer.  The native
cotangent module is the direct sum

\[
  \mathcal P=\bigoplus_{a+b>0}\C\rho_{a,b}
  \cong\mathfrak h^\vee_{\mathrm{cont}},
  \qquad
  \mathfrak h=\C[[z_1,z_2]]/\C\cdot1 .
\]

The product target accepts all moment sequences, but it does not provide a
compact-current derivative-delta section and it does not carry the full
formal Hamiltonian action.

## Exact Obstruction Vector

After the diagonal convention is fixed, the all-window/pro-Matlis gate is

\[
  \operatorname{Ob}^{\Pi}_{\mathrm{BM}}
  =
  \left(
    \operatorname{ob}_{\oplus},
    \operatorname{ob}_{I_\Pi},
    \operatorname{ob}_{\mathfrak h,\Pi},
    \operatorname{ob}_{\mathrm{collar},\Pi},
    \operatorname{ob}_{3,\Pi},
    \operatorname{ob}_{\mathrm{unif},\Pi}
  \right).
\]

The direct-sum, current-section, formal-action, and unweighted-uniformity
entries are decided.  The collar and ternary entries are exact construction
targets.

- \(\operatorname{ob}_{\oplus}\neq0\): a general compact-support top
  current has infinitely many holomorphic moments, so the all-moment map
  lands in \(\widehat{\mathcal P}_\Pi\), not in the direct-sum Matlis
  module \(\mathcal P\).
- \(\operatorname{ob}_{I_\Pi}\neq0\): an arbitrary product sequence would
  require an infinite-order derivative-delta sum.  Distributions supported
  at a point have finite order, so no support-local current section
  \(i_\Pi:\widehat{\mathcal P}_\Pi\to\mathcal D'_0{}^{0,2}(B)\) exists.
- \(\operatorname{ob}_{\mathfrak h,\Pi}\neq0\): the full formal
  Hamiltonian action is not defined on the product target.  For
  \[
    f=\sum_{p\ge2}z_1^p,\qquad
    \lambda=\sum_{p\ge2}\rho_{p-1,0},
  \]
  the \(\rho_{0,1}\)-coefficient of \(f\cdot\lambda\) would be
  \[
    -\sum_{p\ge2}p.
  \]

- \(\operatorname{ob}_{\mathrm{collar},\Pi}\): compatible collar
  primitives for \(E_{\chi,N}\) under extension by zero, products, and
  finite-window transition maps.
- \(\operatorname{ob}_{3,\Pi}\): the small-diagonal/collar primitive for
  the first ternary BMK transfer row.  Its coefficient Jacobiator vanishes
  on \(\mathfrak h\ltimes\mathcal P[1]\); the primitive is not supplied.
- \(\operatorname{ob}_{\mathrm{unif},\Pi}\): uniform estimates in \(N\).
  In the unweighted current topology this is already nonzero because
  \(i_N(\rho_{a,b})\) has distribution order \(a+b\), so no fixed
  \(C^s\)-test seminorm controls all windows.  A radius-loss analytic
  topology would be a changed-habitat repair, not the current theorem.

## Recommendation

Do not claim a strict native all-window BMK current transfer from the
present data.

The theorem-grade replacement is:

1. keep the direct-sum Matlis module as the native continuous cotangent
   module and retain all high modes when discussing Hamiltonian action;
2. record the one-pair pro-analytic BMK retract as a changed-habitat
   construction;
3. state the obstruction vector above for any strict native all-window or
   pro-product current transfer;
4. make any future positive theorem choose a new analytic/bornological
   factorization habitat with radius-loss estimates, a polynomial or
   convergent Hamiltonian action, compatible collar primitives, and the
   ternary small-diagonal primitive.

## Files Changed

- Added `reconstitution/bmk-all-window-pro-matlis-transfer-construction-push-2026-04-30.md`.
- Added `reconstitution/swarm-2026-04-30-agent-300-bmk-all-window-pro-matlis-transfer-construction-push.md`.

## Checks

No build was run because the task was report-only and no TeX was edited.
The arithmetic check for the formal-action obstruction was run:

```bash
python3 - <<'PY'
for M in [3, 5, 10]:
    coeff = 0
    terms = []
    for p in range(2, M + 1):
        i, j, q = p - 1, 0, 0
        target = (i - p + 1, j - q + 1)
        c = -(p*j - q*i + p - q)
        assert target == (0, 1)
        coeff += c
        terms.append(c)
    print(M, terms, coeff)
PY
```

It returned partial sums \(-5\), \(-14\), and \(-54\), confirming the
unbounded \(-\sum_{p\ge2}p\) coefficient row.
