# Agent 100 — Scalar-Lift Obstruction Tower

Status: proposal-only return, integrated by the main thread.

## Result

In the ordinary scalar-reduced \(\lie{gl}_N\) weighted brane-defect
complex, the scalar-symbol projection does not admit a natural filtered
chain lift from the present data.  The first obstruction is already
detected on the linear Hamiltonian window:

```tex
o_{\sigma,w}^{(1)}\mapsto
\hbar N[\bar c]\in H^2_{\mathrm{Lie}}(\bar A;\C)[[\hbar]].
```

Changing admissible weight cannot kill it, because the class lives in a
finite window and is transported unchanged.

## Integrated Repair

The main thread added
`appendix-unreduced-bv-qme.tex`, Proposition
`prop:app-first-scalar-lift-obstruction`.

The ordinary scalar-reduced branch is now separated from the two
possible repair branches:

- central-character unreduction, where the primitive exists before
  scalar reduction;
- balanced supertrace, where the scalar representative is multiplied by
  \(\operatorname{sdim}\C^{N|N}=0\), though a full filtered projection for
  all local functionals remains to be constructed.

## Valid Attack

The first scalar-lift obstruction is not a high-order analytic subtlety.
It is the same Capelli/\(U(1)\) class computed by the scalar contact QME
theorem:

```tex
\{I_\partial(a,f),I_\partial(b,g)\}_{\mathrm{open},\hbar}
-I_\partial(ab,\{f,g\}_{\bar A})
=
\hbar N\,\omega(f,g)\int_Ia(t)b(t)\,dt.
```

For \(f=z_1\), \(g=z_2\), this gives
\(\hbar N\gamma_{\mathbf 1}\neq0\).

## Remaining Obligation

The balanced supertrace branch still needs the positive construction of
a complete \(d_{\mathrm{QME}}\)-stable scalar-contact filtration and a
filtered chain projection for the whole local-functional complex.  The
ordinary branch requires external data with leading scalar class
\(-\hbar N[\bar c]\) or a source replacement before scalar reduction.
