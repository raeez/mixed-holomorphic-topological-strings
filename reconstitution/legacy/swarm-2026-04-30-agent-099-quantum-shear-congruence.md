# Swarm Report, 2026-04-30, Agent 099

Lane: all-\(N\) quantum shear congruence for the radial-parts/Weyl-trace
image.

## Claim Attacked

The manuscript hoped to close the exact Weyl-trace image from pure
\(z_1\)- and \(z_2\)-power radial images plus shear compatibility.  That
is not enough.  The classical nonlinear shear already fails at the
one-particle Weyl-algebra level, so the all-\(N\) proof must be a
quantum Egorov/shear proof modulo the traceless moment-map ideal.

## Exact Reduction

For
\[
  E_{a,b,N}
  =
  \sum_{j=0}^{b}\operatorname{Tr}(Y^jX^aY^{b-j})
  -
  J_N\!\left(
    \{z_1^{a+1}/(a+1),z_2^{b+1}\}_\hbar
  \right),
\]
the needed quantum shear congruence is equivalent to
\[
  E_{a,b,N}\in \mathcal W_N\widehat\mu(\mathfrak{sl}_N).
\]
Equivalently, one must construct coefficients
\[
  A^j{}_i(a,b,N)\in\mathcal W_N
\]
with
\[
  E_{a,b,N}=\sum_{i,j}A^j{}_i(a,b,N)\widehat\mu^i{}_j .
\]
This has now been integrated as
`lem:app-quantum-shear-primitive-obstruction` in
`appendix-radial-parts-moyal.tex`.

## Evidence

The decisive low-order obstruction to a classical shear proof remains:
for \([\lambda,y]=\hbar\),
\[
  [t](y+t\lambda^2)^4
  =
  4\lambda^2y^3-12\hbar\lambda y^2+8\hbar^2y,
\]
whereas \(4\operatorname{Op}_{\mathrm W}(z_1^2z_2^3)\) gives the same
expression with \(6\hbar^2y\).  The missing \(2\hbar^2y\) is the
\(s=1\) term in
\[
  \{z_1^3/3,z_2^4\}_\hbar=4z_1^2z_2^3+2\hbar^2z_2.
\]

Agent 099 reran the existing finite harness:

```bash
python3 scripts/check_moyal_coefficients.py
```

The harness reported the intended Moyal coefficient tests, Capelli round
trips, and direct radial checks in ranks \(N=2,3\).  The agent also ran a
read-only finite invariant-module test of the shear defect for
\(N=2,3\), \(0\leq a,b\leq 3\), with \(288\) cases passing.  These tests
are evidence only; they do not prove left-ideal membership for all
\(N,a,b\).

## Residual Obligation

Construct the all-\(N\) moment-ideal primitive above, or prove that no
such primitive exists.  This is now the precise radial-parts bottleneck;
radial machinery alone is circular because identifying the \(J_N\)-term
with the radial image is exactly the mixed Weyl-trace normalization being
proved.
