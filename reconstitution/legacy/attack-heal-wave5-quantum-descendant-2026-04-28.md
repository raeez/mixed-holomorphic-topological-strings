# Quantum Descendant Lift Attack-Heal Report

## Claim Attacked

The primitive polynomial one-psi descendant sector could survive the
Weyl/Moyal quantization by the same chain-level primitive projection
\(\Psi_{a,b}\mapsto\rho_{a,b}\), with Moyal corrections either absent or
absorbed into decomposable multi-trace terms.

## Failure Mode

The obstruction is already linear.  It occurs after cumulant projection
to the indecomposable target, so it is not a multi-trace artifact.

For the Moyal bracket
\[
  \{f,g\}_\hbar
  =
  \sum_{j\geq0}
  \frac{\hbar^{2j}}{(2j+1)!\,2^{2j}}P^{2j+1}(f,g),
\]
the coadjoint action is
\[
  (\operatorname{ad}^{\vee}_{f,\hbar}\delta)(g)
  =-\delta(\{f,g\}_\hbar).
\]
Taking \(f=z_1^4\) and \(\delta_{1,1}\), the classical term vanishes
on degree grounds, but
\[
  P^3(z_1^4,z_2^4)=576z_1z_2,
  \qquad
  \frac{1}{3!\,2^2}P^3(z_1^4,z_2^4)=24z_1z_2.
\]
Thus
\[
  \operatorname{ad}^{\vee}_{z_1^4,\hbar}\delta_{1,1}
  =-24\hbar^2\delta_{0,4}.
\]
The polynomial PBW one-psi action instead gives
\[
  z_1^4:\widetilde\Psi_{1,1}\mapsto4\widetilde\Psi_{4,0}.
\]
The target label and the \(\hbar\)-order disagree.

## Heal Inscribed

Added Proposition
`\ref{prop:quantum-descendant-label-obstruction}` in
`tate-T5-chain-level-primitive.tex`.  The theorem now states the
strongest proved form: the classical primitive one-psi label map is a
PBW special-fibre shadow and does not quantize to the Moyal coadjoint
module.  `open-obligations.tex` now records the same obstruction in the
one-antifield quantum-lift item.

## Computed Range

`scripts/check_one_psi_homology.py` now attacks the naive label map by
exact rational arithmetic:

- Primitive one-psi homology: 36 bidegrees, exponents \(\leq5\).
- Open Hamiltonian action on primitive descendants: 240 cases,
  exponents \(\leq3\).
- Closed coadjoint Taylor-dual formula: 1225 cases, exponents \(\leq5\).
- Principal-part coadjoint realization: 1225 cases, exponents \(\leq5\).
- Naive quantum descendant lift: 1225 cases, exponents \(\leq5\),
  Moyal order \(\leq5\); 1200 PBW-vs-Moyal mismatches; 958 cases with
  genuine higher Moyal coadjoint terms.

`scripts/check_moyal_coefficients.py` was rerun unchanged:
14641 Moyal monomial pairs with exponents \(\leq10\), orders \(\leq11\);
odd coefficients \(1,1/24,1/1920,1/322560,1/92897280,1/40874803200\);
rank-two radial-parts tests and first/third open-line weights pass.

## Files Changed

- `scripts/check_one_psi_homology.py`
- `tate-T5-chain-level-primitive.tex`
- `open-obligations.tex`
- `reconstitution/attack-heal-wave5-quantum-descendant-2026-04-28.md`

## Commands Run

- `python3 scripts/check_one_psi_homology.py`
- `python3 scripts/check_moyal_coefficients.py`
- `rg -n "quantum-descendant-label-obstruction|quantum descendant lift|PBW-vs-Moyal|ad\\^\\*|z_1\\^4" scripts/check_one_psi_homology.py tate-T5-chain-level-primitive.tex open-obligations.tex`

## Remaining Open Questions

1. Construct, or rule out, a corrected \(D_\hbar\), Fourier, or Rees
   bridge from polynomial one-psi classes to the continuous Moyal
   coadjoint module.
2. Construct a Moyal-flat descendant source or weighted coefficient
   model whose CE differential is closed under the full Moyal bracket.
3. Produce the analytic Costello brane-defect QME and centrality
   homotopies for an unreduced cotangent sector.
