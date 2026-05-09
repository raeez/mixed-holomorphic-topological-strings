# Stratified Weiss Parameter Collision Patch Sheet

Apply these TeX replacements when integrating the stratified/Omega lane.
This sheet is report-only; no TeX was edited by Agent 283.

## Theorem Lane

`theorem-lanes.tex:2934-2939`: replace the Weyl bracket in the QME
residual by the QME bracket:

```tex
\{C_{<n,\Omega,M},C_{<n,\Omega,M}\}_{\hbar_{\mathrm{QME}},M,\Omega}
```

`theorem-lanes.tex:3071-3084`: replace the \(P_0\)-centrality homotopy
parameter by:

```tex
\(P_{0,\hbar_{\mathrm{QME}}}\)-homotopies
```

and:

```tex
\{\rho(x),a\}_{P_{0,\hbar_{\mathrm{QME}}}}
```

`theorem-lanes.tex:1663-1674`: clarify the weighted classical
contraction:

```tex
The latter is the \(L_\omega\)-weighted classical \(P_0\) contraction
convention.  It is neither the Weyl/Moyal
\(P_{0,\hbar_{\mathrm{W}}}\) bracket nor the brane-defect
\(P_{0,\hbar_{\mathrm{QME}}}\) bracket.
```

Normalize `\hbar_{\mathrm W}` to `\hbar_{\mathrm{W}}` at
`theorem-lanes.tex:1681`, `1683`, `3034`, `3035`, `3037`, `3043`,
`3046`, and `3232`.

## Open Obligations

`open-obligations.tex:1049`: replace:

```tex
\{K^M_{\Gamma_1},K^M_{\Gamma_2}\}_{\hbar,M}
```

by:

```tex
\{K^M_{\Gamma_1},K^M_{\Gamma_2}\}_{\hbar_{\mathrm{QME}},M}
```

## Vector Label

After the stratified obstruction vectors, add:

```tex
Here \(\operatorname{ob}^{P_0}_{\mathrm{cent}}\) abbreviates the
\(P_{0,\hbar_{\mathrm{QME}}}\)-centrality obstruction in the
brane-defect local-functional complex.  It is not the reduced
Weyl/Moyal current bracket over \(\hbar_{\mathrm{W}}\).
```

Anchors: `theorem-lanes.tex:3061-3069`,
`open-obligations.tex:1105-1113`, and
`claim-strength-ledger.tex:783-791`.
