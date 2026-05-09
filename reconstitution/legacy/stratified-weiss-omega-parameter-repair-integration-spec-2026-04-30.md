# Stratified Weiss/Omega Parameter Repair Integration Spec

Status: report-only integration specification.  No TeX file is edited by
this report.

Owned writable files:

- `reconstitution/stratified-weiss-omega-parameter-repair-integration-spec-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-290-stratified-weiss-omega-parameter-repair-integration-spec.md`

## Verdict

The current TeX still has two coupled defects in the stratified
Weiss/Omega lane.

First, the internal stratified obstruction vector is stale.  It is the
old seven-component vector
\[
  \operatorname{Ob}_{\mathrm{str},\Omega,N}
\]
with \(\operatorname{ob}^{\mathrm{src}}_{\mathrm{CFG}}\) inside the
internal theorem surface.  Replace it by
\[
  \operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}
\]
with nine internal components.  Keep
\(\operatorname{ob}^{\mathrm{src}}_{\mathrm{CFG}}\) outside that vector
as an external matched-conventions source gate.

Second, `theorem-lanes.tex` still collides the Weyl/Moyal parameter
\(\hbar_{\mathrm{W}}\) with the Costello/BV graph parameter
\(\hbar_{\mathrm{QME}}\).  QME curvature, Costello counterterm, and
brane-defect \(P_0\)-centrality brackets use
\(\hbar_{\mathrm{QME}}\).  Weyl/Moyal current brackets and Hamiltonian
reduction formulas use \(\hbar_{\mathrm{W}}\).  Equivariant Hamiltonian
scalarization uses \(\hbar_\omega\).

## Current TeX Verification

Verified in the current checkout:

- stale internal vectors:
  `theorem-lanes.tex:3061`,
  `open-obligations.tex:1105`,
  `claim-strength-ledger.tex:553`,
  `claim-strength-ledger.tex:789`;
- \(\operatorname{ob}^{\mathrm{src}}_{\mathrm{CFG}}\) still inside the
  internal vectors:
  `theorem-lanes.tex:3069`,
  `open-obligations.tex:1113`,
  `claim-strength-ledger.tex:797`;
- obsolete holim-style Weiss defect:
  `open-obligations.tex:1005-1010`;
- wrong QME residual bracket:
  `theorem-lanes.tex:2938`;
- wrong \(P_0\)-centrality bracket parameter:
  `theorem-lanes.tex:3072`,
  `theorem-lanes.tex:3082`;
- bare Costello bracket parameter in the stratified obligation row:
  `open-obligations.tex:1049`;
- unbraced Weyl parameter spelling in `theorem-lanes.tex`:
  `1681`, `1683`, `1686`, `2938`, `3034`, `3035`, `3037`,
  `3043`, `3046`, `3072`, `3082`, `3090`, `3091`, `3107`,
  `3153`, `3195`, `3198`, `3232`, `3236`.

The canonical three-parameter gate is already stated in
`local-dictionary.tex:567-581`, `open-obligations.tex:976-987`,
`claim-strength-ledger.tex:759-772`, and
`appendix-unreduced-bv-qme.tex:2546-2558`.

## Canonical TeX Replacements

### Internal vector

Use this vector wherever the full internal stratified theorem is asserted:

```tex
\[
  \operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}
  =
  (
    \delta_{\mathrm{pref}},
    \delta_{\mathrm{assoc}},
    \delta_{\mathrm{Weiss}},
    \operatorname{ob}_{\mathrm{collar}},
    \operatorname{ob}^{\mathrm{prod}}_{\mathrm{cent}},
    \operatorname{ob}^{P_0}_{\mathrm{cent}},
    \operatorname{ob}^{\mathrm{bd}}_{\mathrm{QME}},
    \operatorname{ob}_{\Omega\mathrm{-basic}},
    \operatorname{ob}_{\mathrm{tr}\mathrm{-top}}
  ).
\]
```

Add this label gate immediately after the vector:

```tex
Here \(\operatorname{ob}^{P_0}_{\mathrm{cent}}\) abbreviates the
\(P_{0,\hbar_{\mathrm{QME}}}\)-centrality obstruction in the
brane-defect local-functional complex.  It is not the reduced
Weyl/Moyal current bracket over \(\hbar_{\mathrm{W}}\).
```

Keep the source gate outside the internal vector:

```tex
The source-primary class
\(\operatorname{ob}^{\mathrm{src}}_{\mathrm{CFG}}\) is not an internal
component of
\(\operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}\).  It is an
external matched-conventions gate for importing Costello--Gwilliam,
AFT, CFG, Weiss/Ran, or Costello \(\Omega\)-background source theorems.
```

### Reduced product-basis datum

Install this before the full obstruction vector in
`theorem-lanes.tex`, `open-obligations.tex`, and the ledger row when the
positive construction is recorded:

```tex
Let \(\mathcal B^{\mathrm{red}}_{\mathrm{prod}}(X,L)\) be the
two-color product basis whose basics are bulk product disks
\(U\times B\subset X\setminus L\), brane intervals \(I\subset L\), and
finite disjoint unions.  Put
\[
  \mathcal F^{\mathrm{red}}_{\Omega,X}(U\times B)
  =
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  \left(
    \Omega_c^\bullet(U)\widehat\otimes
    \Omega_c^{0,\bullet}(B)\widehat\otimes
    (\mathfrak h\ltimes\mathcal P[1])
  \right)
  \widehat\otimes R_\Omega^{N,M},
\]
where
\(\mathcal P=\operatorname{Ann}_{\mathrm{res}}(\mathbb C\cdot1)
\cong\mathfrak h^\vee_{\mathrm{cont}}\), and
\[
  \mathcal F^{\mathrm{red}}_{\Omega,L}(I)
  =
  A^{\mathrm{pp},w}_{\partial,\Omega,\hbar_{\mathrm{W}}}(I).
\]
The products are extension by zero on compact supports followed by CE
or completed symmetric multiplication.  Hence
\(\delta_{\mathrm{pref}}=\delta_{\mathrm{assoc}}=0\) on this reduced
product-basis datum.  No collar module, arbitrary collared Weiss
descent, unreduced centrality homotopy, brane-defect QME curvature
cancellation, basic \(\Omega\)-primitive, or trace-state topology is
constructed here.
```

### Cech/Weiss descent defect

Replace the holim-difference expression by the Cech cone:

```tex
A collared stratified Weiss cover \(\mathcal U=\{U_i\}\) of \(V\) is a
stratified cover such that every finite subset of \(V\) lies in some
\(U_i\), and if the subset meets \(L\), the same \(U_i\) contains a
product collar of its lower-stratum part.  For a candidate
\(\mathcal F^{\mathrm{str}}_{\Omega,N}\), put
\[
  \check C^p(\mathcal U;\mathcal F^q)
  =
  \prod_{i_0<\cdots<i_p}
  \mathcal F^q(U_{i_0}\cap\cdots\cap U_{i_p}),
  \qquad
  \mathbb D=\check\delta+(-1)^p d_{\mathcal F},
\]
and
\[
  \delta_{\mathrm{Weiss}}(V,\mathcal U)
  =
  \operatorname{Cone}\left(
    \mathcal F^{\mathrm{str}}_{\Omega,N}(V)
    \to
    \operatorname{Tot}\check C^\bullet
    (\mathcal U;\mathcal F^{\mathrm{str}}_{\Omega,N})
  \right).
\]
```

### QME residual bracket

Replace `theorem-lanes.tex:2931-2940` by:

```tex
  \[
  \begin{aligned}
    R^{\mathrm{ns}}_{n,\Omega,M}
      =
    [\hbar_{\mathrm{QME}}^n]\bigl(
      &\operatorname{Curv}_{\mathbf K,\Omega,M}
      +d_{M,\Omega}C_{<n,\Omega,M}\\
      &+\frac12
      \{C_{<n,\Omega,M},C_{<n,\Omega,M}\}_{\hbar_{\mathrm{QME}},M,\Omega}
    \bigr),
  \end{aligned}
  \]
```

### Stratified centrality homotopies

Replace `theorem-lanes.tex:3071-3084` by:

```tex
  The centrality terms require product and
  \(P_{0,\hbar_{\mathrm{QME}}}\)-homotopies
  against unreduced brane observables:
  \[
    d_{\mathrm{QME}}H^{\mathrm{prod}}_{x,a}
    =
    \rho(x)a-(-1)^{|x||a|}a\rho(x),
  \]
  \[
    d_{\mathrm{QME}}H^{P_0}_{x,a}
    =
    \{\rho(x),a\}_{P_{0,\hbar_{\mathrm{QME}}}}
    -\rho_{\mathrm{mod}}(x;a).
  \]
```

For cover-level assertions, use the total Cech Hom complex:

```tex
  H^{P_0}_{x,a}
  \in
  \operatorname{Tot}^{|x|+|a|-1}
  \check C^\bullet(\mathcal U;\mathfrak K^\bullet_{\Omega,M}),
  \qquad
  \mathbb D H^{P_0}_{x,a}
  =
  \{\rho(x),a\}_{P_{0,\hbar_{\mathrm{QME}}}}
  -\rho_{\mathrm{mod}}(x;a).
```

### Weighted classical contraction sentence

Replace the final sentence after the displayed contractions at
`theorem-lanes.tex:1663-1674` by:

```tex
  The latter is the \(L_\omega\)-weighted classical \(P_0\) contraction
  convention.  It is neither the Weyl/Moyal
  \(P_{0,\hbar_{\mathrm{W}}}\) bracket nor the brane-defect
  \(P_{0,\hbar_{\mathrm{QME}}}\) bracket.
```

### Open-obligations centrality row

Replace `open-obligations.tex:1049`:

```tex
        \{K^M_{\Gamma_1},K^M_{\Gamma_2}\}_{\hbar,M}
```

by:

```tex
        \{K^M_{\Gamma_1},K^M_{\Gamma_2}\}_{\hbar_{\mathrm{QME}},M}
```

The legacy non-Omega graph rows with a generic \(\hbar\) outside this
stratified/Omega lane are not changed by this spec.

### Trace aggregate

Tie the trace block back to the internal vector:

```tex
The component \(\operatorname{ob}_{\mathrm{tr}\mathrm{-top}}\) is the
aggregate trace-state topology obstruction; its expanded trace vector is
\(\operatorname{Ob}_{\mathrm{tr},\Omega}\).
```

## File-by-File Integration Map

### `theorem-lanes.tex`

1. At `theorem-lanes.tex:1663-1689`, install the weighted-classical
   contraction sentence and normalize
   \(\hbar_{\mathrm W}\mapsto\hbar_{\mathrm{W}}\) and
   \(\hbar_{\mathrm W,N}\mapsto\hbar_{\mathrm{W},N}\).
2. At `theorem-lanes.tex:2931-2940`, replace the QME residual bracket
   by the \(\hbar_{\mathrm{QME}}\)-bracket.
3. After `theorem-lanes.tex:3003`, add that invariant centrality
   primitives are the
   \(\operatorname{ob}_{\Omega\mathrm{-basic}}\) entry of
   \(\operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}\).
4. After `theorem-lanes.tex:3055`, insert the reduced product-basis
   datum.
5. Replace `theorem-lanes.tex:3057-3070` by the internal vector and
   external source gate.
6. Replace `theorem-lanes.tex:3071-3084` by the
   \(P_{0,\hbar_{\mathrm{QME}}}\)-homotopy text.
7. Normalize remaining Weyl notation:
   \[
     \hbar_{\mathrm W}\to\hbar_{\mathrm{W}},
     \qquad
     \hbar_{\mathrm W,N}\to\hbar_{\mathrm{W},N}.
   \]
   The chosen-Weyl-branch catalogue at `theorem-lanes.tex:3232-3236`
   receives bracing normalization only unless the older generic-\(\hbar\)
   non-Omega graph convention is split in the appendix.

### `open-obligations.tex`

1. Insert the reduced product-basis datum before the full stratified
   brane object is treated as a construction target.
2. Replace `open-obligations.tex:1005-1010` by the Cech cone definition
   of \(\delta_{\mathrm{Weiss}}(V,\mathcal U)\).
3. Replace `open-obligations.tex:1049` by the
   \(\hbar_{\mathrm{QME}}\)-bracket.
4. Replace `open-obligations.tex:1103-1114` by
   \(\operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}\), the
   \(P_0\)-parameter gate, and the external source gate.
5. Tie the trace-state block to
   \(\operatorname{ob}_{\mathrm{tr}\mathrm{-top}}\).

### `claim-strength-ledger.tex`

1. At `claim-strength-ledger.tex:548-553`, replace the generic failure
   reference by
   \(\operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}\).
2. Add a row:

```tex
  \item \emph{Reduced product-basis stratified prefactorization datum.}
  Classification: \emph{proved reduced product-basis construction}.
  Bulk product disks carry
  \(\mathcal F^{\mathrm{red}}_{\Omega,X}\), brane intervals carry
  \(A^{\mathrm{pp},w}_{\partial,\Omega,\hbar_{\mathrm{W}}}\), and
  products are extension by zero followed by CE or completed symmetric
  multiplication.  This proves
  \(\delta_{\mathrm{pref}}=\delta_{\mathrm{assoc}}=0\) only on the
  reduced product basis.  It does not construct collars, arbitrary
  collared Weiss descent, unreduced centrality homotopies, brane-defect
  QME curvature cancellation, basic \(\Omega\)-primitives, or
  trace-state topology.
```

3. Replace `claim-strength-ledger.tex:787-798` by the nine-component
   internal vector, then add the \(P_0\)-parameter gate and external
   source gate.
4. Update the protected trace row so the missing construction is exactly
   \(\operatorname{ob}_{\mathrm{tr}\mathrm{-top}}\), with
   \(\operatorname{Ob}_{\mathrm{tr},\Omega}\) as its expanded trace
   vector.

### `local-dictionary.tex`

Record the same split:

- \(\mathcal B^{\mathrm{red}}_{\mathrm{prod}}(X,L)\);
- \(\mathcal F^{\mathrm{red}}_{\Omega,\mathrm{prod}}\);
- \(\delta_{\mathrm{Weiss}}(V,\mathcal U)\) as a Cech cone;
- \(\operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}\);
- \(\operatorname{ob}_{\Omega\mathrm{-basic}}\);
- \(\operatorname{ob}_{\mathrm{tr}\mathrm{-top}}\).

In the open obstruction vector, expand
\(\operatorname{ob}_{\Omega,\mathrm{strat}}\) through
\(\operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}\), and route
\(\operatorname{ob}_{\Omega,N\to\infty}\) through
\(\operatorname{ob}_{\mathrm{tr}\mathrm{-top}}\).

## Acceptance Checks

Run after TeX integration:

```bash
rg -n -F '\hbar_{\mathrm W' theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex local-dictionary.tex appendix-unreduced-bv-qme.tex main.tex
rg -n -F 'P_{0,\hbar_{\mathrm W}}' theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex local-dictionary.tex appendix-unreduced-bv-qme.tex main.tex
rg -n -F '\{C_{<n,\Omega,M},C_{<n,\Omega,M}\}_{\hbar_{\mathrm{QME}},M,\Omega}' theorem-lanes.tex
rg -n -F '\{K^M_{\Gamma_1},K^M_{\Gamma_2}\}_{\hbar_{\mathrm{QME}},M}' open-obligations.tex
rg -n -F '\operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}' theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex local-dictionary.tex main.tex
rg -n -F '\operatorname{ob}^{\mathrm{src}}_{\mathrm{CFG}}' theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex local-dictionary.tex main.tex
rg -n -F '\operatorname*{holim}_{U\in\mathcal U}' open-obligations.tex theorem-lanes.tex main.tex
```

Expected:

- no `\hbar_{\mathrm W` remains;
- no `P_{0,\hbar_{\mathrm W}}` remains in a QME-centrality homotopy;
- QME residual and stratified centrality brackets use
  \(\hbar_{\mathrm{QME}}\);
- \(\operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}\) appears
  in the target files;
- every occurrence of
  \(\operatorname{ob}^{\mathrm{src}}_{\mathrm{CFG}}\) is in a source-gate
  sentence, not inside the internal vector;
- the theorem-grade Weiss defect is represented by the Cech cone, not
  by the formal holim difference.

No build was run.  This is a report-only artifact.
