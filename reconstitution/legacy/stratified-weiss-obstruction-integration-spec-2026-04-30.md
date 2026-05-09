# Stratified Weiss Obstruction Integration Spec

Integrate Agent 266 by recording one proved reduced construction and one
full obstruction theorem.

## Positive Construction

The constructed datum is the reduced product-basis prefactorization
object on:

- bulk product disks \(U\times B\subset X\setminus L\);
- brane intervals \(I\subset L\);
- finite disjoint unions of these basics.

Values:
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
\[
  \mathcal F^{\mathrm{red}}_{\Omega,L}(I)
  =
  A^{\mathrm{pp},w}_{\partial,\Omega,\hbar_{\mathrm W}}(I).
\]

Products are extension by zero on compact supports followed by CE or
completed symmetric multiplication.  This kills the product and
associativity defects on the reduced product basis.  It does not
construct collars, arbitrary collared Weiss descent, unreduced
centrality homotopies, QME curvature cancellation, basic
\(\Omega\)-primitives, or trace-state topology.

## Full Theorem Surface

Use
\[
  \operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}
\]
as the manuscript obstruction vector.  Do not use the report-local
superscript `266` in TeX.

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

The full theorem is:
\[
  \mathcal F^{\mathrm{str}}_{\Omega,N}
  \text{ exists with collars, Weiss descent, centrality, QME, and trace}
  \quad\Longleftrightarrow\quad
  \operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}=0
\]
with compatible null-homotopies.  This is a strengthening: the failed
surface becomes an exact construction problem, not a demotion.

Keep \(\operatorname{ob}^{\mathrm{src}}_{\mathrm{CFG}}\) outside this
internal vector.  It is a source-fixture gate for imported external
analogies.

## Required File Changes

`local-dictionary.tex`: add entries for the reduced product-basis datum,
the Cech cone \(\delta_{\mathrm{Weiss}}\), the internal vector,
\(\operatorname{ob}_{\Omega\mathrm{-basic}}\), and
\(\operatorname{ob}_{\mathrm{tr}\mathrm{-top}}\).  Expand
\(\operatorname{ob}_{\Omega,\mathrm{strat}}\) through the internal vector.

`open-obligations.tex`: replace the informal
\(\mathcal F(V)-\operatorname*{holim}\mathcal F(U)\) descent defect with
the Cech totalization cone.  Insert the proved reduced product-basis
construction before the full stratified obstruction vector.  Replace the
current seven-component vector by the nine-component internal vector.

`theorem-lanes.tex`: split the stratified trace lane into the proved
reduced product-basis subdatum and the full internal obstruction theorem.
Align centrality homotopies with
\(\{\ ,\ \}_{P_{0,\hbar_{\mathrm{QME}}}}\) unless a branch explicitly
identifies this with the Weyl parameter.

`claim-strength-ledger.tex`: add a proved reduced product-basis row.
Update the stratified factorization row to use
\(\operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}\).  Treat
\(\operatorname{Ob}_{\mathrm{tr},\Omega}\) as the expansion of
\(\operatorname{ob}_{\mathrm{tr}\mathrm{-top}}\).

`main.tex`: after the local CE/factorization observables or near the
Weiss/Ran remark, record the reduced product-basis datum and the
internal obstruction theorem.  Cross-reference the same vector from the
reduced principal-part current scope, the unreduced lift obstruction, and
the Costello perturbative BV specialization problem.
