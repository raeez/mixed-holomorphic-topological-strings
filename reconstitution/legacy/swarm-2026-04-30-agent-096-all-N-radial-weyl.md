# Agent 096 — All-\(N\) Radial/Weyl Trace

Status: proposal-only return, integrated by the main thread.

## Result

The all-\(N\) Weyl-trace image is not closed by the present
Harish-Chandra, Wallach, and Levasseur--Stafford source anchors.  Those
sources support the radial map, kernel, and injectivity framework, but
not the exact generator normalisation

```tex
\operatorname{Rad}_0(J_N(f))=\Delta^{-1}S_N(f)\Delta
```

in this manuscript's Weyl/Capelli convention.

The missing lemma is the quantum shear congruence

```tex
\hbar^{-1}[J_N(z_1^{a+1}/(a+1)),J_N(z_2^{b+1})]
\equiv
J_N(\{z_1^{a+1}/(a+1),z_2^{b+1}\}_\hbar)
\pmod {I_N}.
```

Together with the pure \(z_1\)- and \(z_2\)-power radial images, this
congruence implies the all-\(N\) Weyl-trace image by triangular
induction.

## Integrated Repair

The main thread added
`appendix-radial-parts-moyal.tex`, Proposition
`prop:app-quantum-shear-suffices-radial-image`.

The induction uses

```tex
\{z_1^{a+1}/(a+1),z_2^{b+1}\}_\hbar
=(b+1)z_1^az_2^b
+\sum_{s\ge1}
\frac{\hbar^{2s}(a+1)_{2s+1}(b+1)_{2s+1}}
{(a+1)2^{2s}(2s+1)!}
z_1^{a-2s}z_2^{b-2s}.
```

All non-leading terms have lower total degree.

## Valid Attacks

- Classical nonlinear shear covariance does not determine the mixed
  Weyl-trace image.  The residual \(2\hbar^2y\) in
  Lemma `app-radial-nonlinear-shear-obstruction` is exactly the first
  quantum correction that a classical shear argument misses.
- The current source fixtures do not state the manuscript's exact
  \(J_N\)-normalisation.  They cannot be used as a theorem-grade proof
  of Statement `app-radial-external-input` item (3).
- Finite exact tests in ranks \(N=2,3,4,5\) are evidence only; they are
  not an all-\(N\) proof.

## Checks

Agent 096 reported:

```text
python3 scripts/check_moyal_coefficients.py
direct_rank_radial_checks(4) -> 80
direct_rank_radial_checks(5) -> 80
```

## Remaining Obligation

Prove the quantum shear congruence in the matrix Weyl algebra modulo the
quantum moment-map ideal, or replace the ordinary trace generators
\(J_N(f)\) by explicitly constructed radially normalised classes
\(J_N^{\mathrm{rad}}(f)\) and propagate that change through the stable
trace theorem.
