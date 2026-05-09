# Binary Centrality Zero-Row Integration Spec

Status: report-only manuscript integration specification.  No TeX file is
edited by this note.

## Verdict

The proved statement is the zero-row statement, in its named habitat.

For source generators
\[
  x,y\in\{u_{a(t)dt\otimes f},c_{B,\rho}\},
\]
the reduced coefficient-current target and the minimal full-equivariant
finite marked habitat give
\[
  R^{\mathrm{cent},\mathrm{coef}}_{x,y,M}=0,\qquad
  S^{\mathrm{cent},\mathrm{coef}}_{x,y,M}=0,\qquad
  H^{\mathrm{coef},M}_{x,y}=0 .
\]
Equivalently, after suppressing zero rows,
\[
  A^M_{\min}:0\to0,\qquad r^M_{\min}=0,\qquad h^M_{\min}=0,
\]
and the primitive Roos class is zero.  If labelled zero rows are retained,
the same assertion is the zero matrix with zero residual and zero primitive.

This is a theorem only in the reduced coefficient-current/minimal
full-equivariant zero-row habitat.  It does not construct a nonzero
Costello-local binary centrality homotopy in an enlarged graph/counterterm
package.

For any enlarged Costello package, the manuscript must state the binary row
as the finite matrix obstruction
\[
  A^M h^M=-r^M.
\]
The vector \(r^M\) is the coordinate vector of the supplied scalar-zero
centrality residual \(R^{\mathrm{cent}}_{x,y,M}\).  The unknown \(h^M\) is
the coordinate vector of the candidate binary homotopy row
\[
  H^M_{x,y}=\sum_j h^M_j\eta^M_j .
\]
No row basis, no scalar-zero gate, no primitive candidate, or no transition
matrix means no Costello homotopy has been constructed.

## Source anchors

- `appendix-factorization-current-conventions.tex:277-367`: strict reduced
  current interface; product and \(P_0\)-defect homotopies are zero in the
  current target.
- `appendix-factorization-current-conventions.tex:1029-1123`: coefficient
  kernel layer and finite-window compatibility.
- `appendix-factorization-current-conventions.tex:1171-1196`: Moyal current
  identities and residual class mechanism; graph lift remains an obstruction
  unless analytic/current locality data are supplied.
- `appendix-factorization-current-conventions.tex:1936-2070`: curved kernel
  centrality criterion; binary homotopy is exactly
  \(R^{\mathrm{cent}}_{x,y,M}+d_MH^M_{x,y}=0\) with interval, window, and
  weight compatibility.
- `appendix-unreduced-bv-qme.tex:3316-3368`: marked-row formula for
  \(R^{\mathrm{cent}}_{x,y,M}\), scalar gate, and cohomology class.
- `appendix-unreduced-bv-qme.tex:3369-3395`: actual centrality homotopy row
  criterion and minimal full-equivariant zero primitive.
- `appendix-unreduced-bv-qme.tex:3411-3428`: proof that the minimal package has
  zero centrality row and zero compatible primitive, and that enlarged rows
  must be supplied explicitly.
- `appendix-unreduced-bv-qme.tex:2290-2333`: finite-row matrix criterion and
  Roos primitive compatibility in the same row-complex notation.
- `theorem-lanes.tex:3279-3306`: minimal full-equivariant finite-window branch
  and first supplied nonzero source-face row.
- `theorem-lanes.tex:3307-3317`: one-row \(\theta_3\) obstruction does not rule
  out primitives in larger complexes.
- `main.tex:2091-2102`: current front-facing summary of the non-scalar
  Costello/QME finite-window surface.
- `main.tex:8121-8330`: non-scalar quantum \(P_0\)-operation obstruction
  complex.
- `main.tex:8332-8511`: current first \(\theta_3\) finite-window acceptance
  gate and generic finite-row primitive equation.
- `scripts/finite_window_graph_array.py:1810-1827`: finite-row primitive
  matrix convention and tower condition.
- `scripts/finite_window_graph_array.py:1831-1863`: direct script record:
  minimal full-equivariant order-two zero is solved; \(\theta_3\) one-row
  package is obstructed.
- `scripts/finite_window_graph_array.py:1872-1887`: missing row types for
  any enlarged nonzero package.
- `reconstitution/swarm-2026-04-30-agent-275-nonscalar-costello-binary-row-construction-push.md`:
  attack/heal source report for this integration.

## Integration invariant

Keep these two statements separate.

1. Reduced coefficient-current/minimal full-equivariant zero row:
   \[
     R^{\mathrm{cent}}_{x,y,M}=0,\qquad H^M_{x,y}=0 .
   \]
   This is proved because the reduced current brackets are strict identities,
   and in the minimal full-equivariant marked package every positive-order row
   is either absent or has zero scalar-contact factor.

2. Enlarged Costello row:
   \[
   \begin{aligned}
     R^{\mathrm{cent}}_{x,y,M}
       ={}&
       \sum_{\Gamma\in\mathsf A^d_{x,y,M}}
         \varepsilon_\Gamma d_MK^M_\Gamma
       -\sum_{\Gamma\in\mathsf A^{\mathrm{CE}}_{x,y,M}}
         \varepsilon^{\mathrm{CE}}_\Gamma
         K^M_\Gamma(\zeta_{\Gamma,x,y}) \\
       &+\frac12
         \sum_{(\Gamma_1,\Gamma_2)\in\mathsf A^{\mathrm{br}}_{x,y,M}}
         \varepsilon_{\Gamma_1,\Gamma_2}
         \{K^M_{\Gamma_1},K^M_{\Gamma_2}\}_{\hbar,M}
       +R^{\mathrm{ct}}_{x,y,M}.
   \end{aligned}
   \]
   Only after the scalar gate
   \[
     S^{\mathrm{cent}}_{x,y,M}
     =\widehat\sigma_{\mathrm{sc},M}(R^{\mathrm{cent}}_{x,y,M})
   \]
   is supplied and vanishes does this row define a class in
   \(H^{|x|+|y|}(\mathcal K^\bullet_{\mathrm{ns},M}(I))\).  Then choose
   degree \(|x|+|y|\) residual-row coordinates
   \(\rho^M_1,\ldots,\rho^M_a\) and degree \(|x|+|y|-1\) candidate homotopy
   rows \(\eta^M_1,\ldots,\eta^M_b\), and write
   \[
     R^{\mathrm{cent}}_{x,y,M}=\sum_i r^M_i\rho^M_i,\qquad
     d_M\eta^M_j=\sum_i A^M_{ij}\rho^M_i .
   \]
   For \(H^M_{x,y}=\sum_jh^M_j\eta^M_j\), the centrality equation
   \(R^{\mathrm{cent}}_{x,y,M}+d_MH^M_{x,y}=0\) is exactly
   \[
     A^Mh^M=-r^M .
   \]
   A left-null covector \(\ell A^M=0\), \(\ell(r^M)\ne0\), is the
   fixed-window obstruction certificate.

The inverse-system obstruction is
\[
  \left(
    ([R^{\mathrm{cent}}_{x,y,M}])_M,\,
    [P^{M,N}h^M-h^N_{\pi x,\pi y}]
  \right),
\]
with the second component read in
\[
  \varprojlim\nolimits^1_M
  H^{|x|+|y|-1}(\mathcal K^\bullet_{\mathrm{ns},M}(I)).
\]
In a normal-\(\Omega\) branch, add the secondary invariant-row obstruction
\[
  [L_{V_\Omega}H^\Omega_{x,y,M}].
\]

## `main.tex`

Current anchors:

- `main.tex:2091-2102`: front summary of the non-scalar Costello surface.
- `main.tex:8121-8330`: `prob:quantum-p0-operation-realization`.
- `main.tex:8332-8511`: first \(\theta_3\) row and generic primitive matrix.

Insert after `main.tex:2102`:

```tex
For the binary centrality row the proved statement is exactly the zero-row
statement in the reduced coefficient-current/minimal full-equivariant
habitat.  For
\[
  x,y\in\{u_{a(t)dt\otimes f},c_{B,\rho}\}
\]
one has
\[
  R^{\mathrm{cent},\mathrm{coef}}_{x,y,M}=0,\qquad
  S^{\mathrm{cent},\mathrm{coef}}_{x,y,M}=0,\qquad
  H^{\mathrm{coef},M}_{x,y}=0 .
\]
Equivalently \(A^M_{\min}:0\to0\), \(r^M_{\min}=0\), and
\(h^M_{\min}=0\), with zero Roos primitive class.  In a larger
Costello local-functional package the same assertion becomes the row
problem \(A^Mh^M=-r^M\); it is not a constructed centrality homotopy until
the row values, scalar gate, primitive columns, and transition matrices are
supplied.
```

Insert after `main.tex:8223` and before the paragraph beginning
"More explicitly":

```tex
For a fixed binary generator pair \(x,y\), the row form of this obstruction
is as follows.  Once the finite package supplies a scalar-zero basis
\(\rho^M_i\) for the degree \(|x|+|y|\) residual rows and candidate
homotopy rows \(\eta^M_j\) of degree \(|x|+|y|-1\), write
\[
  R^{\mathrm{cent}}_{x,y,M}=\sum_i r^M_i\rho^M_i,\qquad
  d_M\eta^M_j=\sum_i A^M_{ij}\rho^M_i .
\]
Then \(H^M_{x,y}=\sum_jh^M_j\eta^M_j\) is a binary centrality homotopy in
the supplied finite row span if and only if
\[
  A^Mh^M=-r^M .
\]
The compatible inverse-limit homotopy additionally requires
\[
  [P^{M,N}h^M-h^N_{\pi x,\pi y}]
  =
  0
  \quad\text{in}\quad
  H^{|x|+|y|-1}(\mathcal K^\bullet_{\mathrm{ns},N}(I)).
\]
Thus the coefficient-current zero row is not evidence for an enlarged
Costello row; the enlarged row is the displayed matrix obstruction.
```

Do not replace the generic \(\theta_3\) proof equation
`main.tex:8487-8500` unless the surrounding paragraph is specifically being
rewritten.  If it is rewritten for binary centrality, use \(h^M\) instead
of \(c^M\) to avoid identifying a binary homotopy row with a scalar
counterterm coordinate.

## `appendix-factorization-current-conventions.tex`

Current anchors:

- `appendix-factorization-current-conventions.tex:2022-2035`: coefficient
  current zero homotopy versus Costello-local requirement.

Optional minimal insertion after `appendix-factorization-current-conventions.tex:2028`:

```tex
In finite-row coordinates this is the empty solved system
\[
  A^M_{\min}:0\to0,\qquad r^M_{\min}=0,\qquad h^M_{\min}=0,
\]
and the primitive Roos class is zero.
```

Optional replacement for `appendix-factorization-current-conventions.tex:2029-2035`
if the paragraph is expanded:

```tex
For a genuine unreduced Costello local-functional target, the same
conclusion is not supplied by the coefficient-current formula.  It requires
the finite-window graph row representing \(\mathfrak D^M_\kappa(x,y)\), a
scalar-zero gate for that row, degree \(|x|+|y|-1\) primitive columns
\(\eta^M_j\), and coefficients \(h^M_j\) satisfying
\[
  A^Mh^M=-r^M,
\]
equivalently equation~\eqref{eq:app-centrality-homotopy-equation}, with the
displayed interval, window, and weight compatibilities.
```

## `appendix-unreduced-bv-qme.tex`

Current anchors:

- `appendix-unreduced-bv-qme.tex:3316-3368`: marked-row centrality formula.
- `appendix-unreduced-bv-qme.tex:3369-3395`: actual homotopy criterion and
  minimal full-equivariant zero statement.
- `appendix-unreduced-bv-qme.tex:3411-3428`: proof paragraph.

Insert after `appendix-unreduced-bv-qme.tex:3390`:

```tex
  Equivalently, the corresponding finite-row matrix is the empty solved
  system
  \[
    A^M_{\min}:0\to0,\qquad r^M_{\min}=0,\qquad h^M_{\min}=0.
  \]
  If labelled zero rows are retained, the same statement is the zero
  matrix with zero residual and zero primitive.  The Roos compatibility
  class of the primitive tower is therefore zero.
```

Insert after `appendix-unreduced-bv-qme.tex:3395` if the enlarged-row
criterion needs to be explicit in this proposition:

```tex
  In any enlarged finite marked package, choose residual-row coordinates
  \(\rho^M_i\) and candidate homotopy rows \(\eta^M_j\) in the scalar-zero
  kernel, and write
  \[
    R^{\mathrm{cent}}_{x,y,M}=\sum_i r^M_i\rho^M_i,\qquad
    d_M\eta^M_j=\sum_i A^M_{ij}\rho^M_i.
  \]
  Then \(H^M_{x,y}=\sum_jh^M_j\eta^M_j\) exists in the supplied span
  exactly when
  \[
    A^Mh^M=-r^M.
  \]
  The compatible tower further requires the Roos class
  \([P^{M,N}h^M-h^N_{\pi x,\pi y}]\) to vanish.
```

## `theorem-lanes.tex`

Current anchors:

- `theorem-lanes.tex:3279-3298`: minimal full-equivariant branch.
- `theorem-lanes.tex:3298-3317`: first supplied nonzero source-face row.
- `theorem-lanes.tex:2958-2974`: generic finite-row primitive interface.

Insert after `theorem-lanes.tex:3293`:

```tex
    For the binary centrality specialization this says, for all
    \(x,y\in\{u_{a(t)dt\otimes f},c_{B,\rho}\}\),
    \[
      R^{\mathrm{cent}}_{x,y,M}=0,\qquad
      S^{\mathrm{cent}}_{x,y,M}=0,\qquad
      H^M_{x,y}=0 .
    \]
    In coordinates this is the empty solved system
    \(A^M_{\min}:0\to0\), \(r^M_{\min}=0\), \(h^M_{\min}=0\), with zero
    Roos class.
```

If the finite-row primitive interface at `theorem-lanes.tex:2958-2974` is
being reused for centrality, leave the generic \(c\) notation in place, but
add one sentence:

```tex
  For binary centrality rows the primitive coordinate is denoted \(h^M\),
  and the same equation reads \(A^Mh^M=-r^M\).
```

## `claim-strength-ledger.tex`

Current anchors:

- `claim-strength-ledger.tex:110-122`: Stage A6b distinguishes the minimal
  full-equivariant branch from larger Costello/QME.
- `claim-strength-ledger.tex:449-457`: non-scalar Costello/QME beyond the
  minimal marked branch.

Optional insertion after `claim-strength-ledger.tex:457`:

```tex
  Binary centrality has the same status.  In the reduced
  coefficient-current/minimal full-equivariant zero-row habitat,
  \(R^{\mathrm{cent}}_{x,y,M}=0\) and \(H^M_{x,y}=0\) for the length-one
  generator pairs.  In any enlarged Costello package the claim is the
  matrix obstruction \(A^Mh^M=-r^M\), together with scalar-zero and Roos
  compatibility gates; no nonzero Costello homotopy is constructed by the
  zero-row theorem.
```

## Verification

Read and checked:

- `CLAUDE.md`
- `AGENTS.md`
- `~/ecosystem/INVARIANTS.md` voice section
- `~/ecosystem/AGENTS-HARNESS.md` self-reflection section
- local and Vol II `chriss-ginzburg-rectify` skill files
- Agent 275 report
- current anchors in `main.tex`, `theorem-lanes.tex`,
  `appendix-factorization-current-conventions.tex`,
  `appendix-unreduced-bv-qme.tex`, `claim-strength-ledger.tex`, and
  `open-obligations.tex`
- `scripts/finite_window_graph_array.py`

Direct command run:

```text
python3 scripts/finite_window_graph_array.py
```

Relevant checked output:

```text
case: minimal_full_equivariant_order_2_zero
primitive_exists: true
residual_vector: []
primitive_coefficients: []
roos_compatibility: zero primitives are compatible under every truncation map; the Roos lim^1 class is 0

case: theta_3_current_finite_row_subcomplex
primitive_exists: false
residual_vector: [("E_theta_3", 1)]
obstruction_covector: [("E_theta_3", "1")]
```

No PDF build was run.
