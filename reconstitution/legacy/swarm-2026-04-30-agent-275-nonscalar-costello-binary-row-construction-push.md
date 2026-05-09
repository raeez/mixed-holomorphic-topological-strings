# Agent 275 - Non-Scalar Costello Binary Row Construction Push

Status: report-only attack/heal.  Worktree:
`/Users/raeez/topological-strings`.

Owned file:

- `reconstitution/swarm-2026-04-30-agent-275-nonscalar-costello-binary-row-construction-push.md`

No manuscript TeX, script, source fixture, bibliography, figure, or build
artifact was edited.  No PDF build was run.

## Claim Attacked

The attacked claim is that the non-scalar Costello binary centrality row is
already constructed as an unreduced brane-defect homotopy, rather than only as
a reduced coefficient-current identity or a finite-row obstruction problem.

## Result

There is one actual finite-window row plus primitive in the present data:
the reduced coefficient-current / minimal full-equivariant habitat has
\[
  R^{\mathrm{cent},\mathrm{coef}}_{x,y,M}=0,\qquad
  S^{\mathrm{cent},\mathrm{coef}}_{x,y,M}=0,\qquad
  H^{\mathrm{coef},M}_{x,y}=0
\]
for generator pairs
\[
  x,y\in\{u_{a(t)dt\otimes f},c_{B,\rho}\}.
\]
The matrix form is the empty solved system
\[
  A^M_{\min}:0\to0,\qquad r^M_{\min}=0,\qquad h^M_{\min}=0,
\]
and the primitive Roos class is zero.  This is an honest construction only in
that minimal habitat.

For a genuine enlarged Costello local-functional target, the present data do
not construct a nonzero binary centrality homotopy.  The exact fixed-window
obstruction equation is
\[
  A^M h^M=-r^M,
\]
where \(r^M\) is the coordinate vector of
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
    +R^{\mathrm{ct}}_{x,y,M}
\end{aligned}
\]
in a scalar-zero degree-one row basis, and \(A^M\) is the differential matrix
from supplied degree-zero centrality-homotopy rows.  The inverse-limit
obstruction is
\[
  \left(
    ([R^{\mathrm{cent}}_{x,y,M}])_M,\,
    [P^{M,N}h^M-h^N_{\pi x,\pi y}]
  \right),
\]
with the second component read in
\(\varprojlim^1_MH^{|x|+|y|-1}(\mathcal K^\bullet_{\mathrm{ns},M}(I))\).
In the normal-\(\Omega\) branch one must also kill
\[
  [L_{V_\Omega}H^\Omega_{x,y,M}].
\]

## Evidence

`appendix-factorization-current-conventions.tex:277-367` proves the strict
reduced current interface: the product and \(P_0\) defects vanish in the
freely adjoined current target.  The coefficient-current kernel layer at
`appendix-factorization-current-conventions.tex:1029-1197` preserves that
identity windowwise and records the residual graph problem.  The binary
centrality criterion at
`appendix-factorization-current-conventions.tex:1936-2070` says exactly that
a binary homotopy is a primitive of the arity-two curvature row with
interval, finite-window, and weight compatibility.

The minimal full-equivariant finite marked branch agrees with the script:
`scripts/finite_window_graph_array.py` reports
`minimal_full_equivariant_order_2_zero primitive_exists=True` and zero Roos
class.  This matches `theorem-lanes.tex:3279-3293` and
`appendix-unreduced-bv-qme.tex:3382-3395`: in the minimal full-equivariant
habitat every positive-order row contains the zero scalar-contact factor or
is absent, so the centrality row and its primitive are both zero.

That positive construction does not extend to an arbitrary enlarged Costello
package.  The same centrality criterion requires actual marked graph rows,
CE-source faces, bracket rows, counterterm rows, scalar gates, and transition
coefficients.  `scripts/finite_window_graph_array.py:1872-1887` lists the
missing finite row types: genuine seed lists, renormalized weights
\(K^M_\Gamma\), \(d_MK^M_\Gamma\) expansions, orientation/Koszul/symmetry
coefficients, CE-source decompositions, nonzero bracket rows, locality data,
row bases, and \(u,v,q\) projection matrices.

Agent 259 blocks the scalar shortcut: in the ordinary scalar-reduced branch
the scalar-contact obstruction is
\[
  o_{\sigma,M}^{(1),\mathrm{sc}}=\hbar N[\bar c_M],
  \qquad
  o_{\sigma,M}^{(1),\mathrm{sc}}(z_1,z_2)=\hbar N\gamma_{\mathbf 1}\ne0.
\]
Thus the non-scalar kernel is not formed in that branch until the scalar
projection gate has been killed.

Agent 266 identifies the same binary row as a centrality obstruction:
\[
  R^{\mathrm{cent}}_{x,y,\Omega,M}
\]
is closed only after the scalar gate, and a centrality homotopy is exactly a
primitive satisfying \(R+dH=0\) plus finite-window compatibility.  Agent 267
adds the graph-label restriction: regular densities and graphwise
wavefront-admissible tuples are legitimate habitats; arbitrary
\(\mathcal D'_c(I)\) labels are obstructed by the delta-delta collision
counterexample.

## First Nonzero Tested Enlargement

The first supplied nonzero scalar-zero source-face row is the theta3 row
\[
  E_{\theta_3,M}=-K^M_{\Theta_3}(\zeta_{M,\nu_3}),\qquad
  S_{\theta_3,M}=0.
\]
In the present one-row complex,
\[
  \mathcal K^0_{\theta_3,M}=0,\qquad
  \mathcal K^1_{\theta_3,M}=\mathbb C E_{\theta_3,M},\qquad
  d=0.
\]
The finite matrix is
\[
  A_{\theta_3}^M=(\ ):\,0\to\mathbb C,\qquad
  r_{\theta_3}^M=(1),
\]
and the left cokernel covector
\[
  \ell_{\theta_3}(E_{\theta_3,M})=1
\]
has \(\ell_{\theta_3}A^M=0\) and \(\ell_{\theta_3}(r^M)=1\).  Hence no
primitive exists in the current one-row package.

The tested eight-face companion vector is
\[
  r_8=(2,-2,3,2,-1,1,-2,-3)^T
\]
on
\[
  (E_{\nu_{02}},E_{\nu_{20}},E_{\nu_{03}},
   E_{\nu_{12}^{(1)}},E_{\nu_{12}^{(2)}},
   E_{\theta_3},E_{\nu_{21}^{(2)}},E_{\nu_{30}}).
\]
Diagonal source-coordinate transport to the \(N=2\) window gives
\[
  r_2=(2,-2)^T.
\]
The current lower primitive span is empty:
\[
  A_{\mathrm{cur}}^2:0\to\mathbb C^2,
\]
and
\[
  \lambda^{(2)}_{\nu_{02}}=\frac12(E^2_{\nu_{02}})^*
\]
satisfies
\[
  \lambda^{(2)}_{\nu_{02}}A_{\mathrm{cur}}^2=0,\qquad
  \lambda^{(2)}_{\nu_{02}}(r_2)=1.
\]

There is a canonical source-coordinate candidate
\[
  D^2_{02,20}
  =
  K^2_{\Theta_3}(u_{a,H_{1,0}}u_{b,H_{0,1}}),
\]
because
\[
  d_{\mathrm{CE}}(u_{a,H_{1,0}}u_{b,H_{0,1}})
  =
  2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}}.
\]
If the Hom-valued Bianchi defect
\[
  \mathfrak b^2_{02,20}
  =
  d_{\mathrm{ns},2}K^2_{\Theta_3}(u_{a,H_{1,0}}u_{b,H_{0,1}})
  -
  K^2_{\Theta_3}\!\left(
    d_{\mathrm{CE}}(u_{a,H_{1,0}}u_{b,H_{0,1}})
  \right)
\]
vanishes, and if the candidate has scalar-zero value and compatible
transport, then the new boundary column is
\[
  A_D^2=\begin{pmatrix}-2\\2\end{pmatrix},
\]
and \(A_D^2c=-r_2\) is solved by \(c=1\).  This is a real matrix repair
criterion, not a constructed homotopy in the checkout, because
\(\mathfrak b^2_{02,20}=0\), scalar-zero value, codimension-two closure, and
primitive transport are not supplied.

Equivalently, a non-diagonal transport repair would need columns
\[
  v_3,\ldots,v_8\in\mathbb C^2
\]
satisfying
\[
  3v_3+2v_4-v_5+v_6-2v_7-3v_8=(-2,2)^T.
\]
This affine equation has formal solutions, for example putting
\(v_6=(-2,2)^T\) and the other degree-three columns zero.  It is not derived
from the present row package, whose source-coordinate projection forces all
degree-three columns to vanish at \(N=2\).  Such a non-diagonal block would be
an additional marked Costello transport datum.

## Exact Obstruction Theorem

Let \(\mathcal H^{\mathrm{bin}}_{\mathrm{Cost},M}\) be the finite-window
habitat generated by the present coefficient-current kernel, the minimal
full-equivariant zero rows, the theta3 one-row source-face package, the
eight source-coordinate companion faces, and the regular-density or
wavefront-admissible graph-label restrictions, with no additional marked
Costello incidence/weight table and no verified lower primitive
\(D^2_{02,20}\).

Then the binary centrality row is solved exactly on the minimal zero-row
subhabitat by \(H=0\).  In any enlargement containing the first theta3
source-face obstruction, the current data leave the obstruction
\[
  \left(
    \ell_{\theta_3},\,
    \lambda^{(2)}_{\nu_{02}},\,
    \mathfrak b^2_{02,20},\,
    \mathfrak m_{\Theta_3}^{\mathrm{Cost}}
  \right),
\]
where
\[
  \ell_{\theta_3}(E_{\theta_3})=1,\qquad
  \lambda^{(2)}_{\nu_{02}}(2E^2_{\nu_{02}}-2E^2_{\nu_{20}})=1,
\]
\(\mathfrak b^2_{02,20}\) is the Hom-curvature/Bianchi defect above, and
\(\mathfrak m_{\Theta_3}^{\mathrm{Cost}}\) denotes the absent marked
Costello incidence/weight table:
labelled \(d_{\mathrm{CE}}\zeta_M\), Costello orientation/Koszul signs,
renormalized weights \(K^M_{\Theta_3}(\zeta_{M,\nu})\), marked output graph
and marker transport, projected \(v^{M,N}\) coordinates, and the
codimension-two closure table.

Thus the exact obstruction is not a vague absence of proof.  It is the
finite-window matrix equation
\[
  A^Mh^M=-r^M
\]
together with scalar-zero, locality/wavefront, transition, and Roos
conditions.  In the first tested nonzero enlargement the current matrix has
no column killing \(r=(1)\), and the lower companion residual is killed only
after adjoining the column \(A_D^2=(-2,2)^T\) with verified
\(\mathfrak b^2_{02,20}=0\).

## Verification

Commands run:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py
python3 -c "import scripts.finite_window_graph_array as f; ..."
python3 -c "from fractions import Fraction; ..."
```

Focused outputs:

```text
minimal_order2 True () zero primitives are compatible under every truncation map; the Roos lim^1 class is 0
theta3_one_row False ((),) (('E_theta_3', '1'),) (('E_theta_3', '1'),) 1
eight_vector (('E_nu02', '2'), ('E_nu20', '-2'), ('E_nu03', '3'), ('E_nu12_1', '2'), ('E_nu12_2', '-1'), ('E_theta_3', '1'), ('E_nu21_2', '-2'), ('E_nu30', '-3'))
n2_vector (('E_nu02', '2'), ('E_nu20', '-2'))
A_cur^2 [] r2 [Fraction(2, 1), Fraction(-2, 1)] lambda_r 1
A_D [Fraction(-2, 1), Fraction(2, 1)] target [Fraction(-2, 1), Fraction(2, 1)] solution_c 1 A_D_c [Fraction(-2, 1), Fraction(2, 1)] residual_plus_boundary [Fraction(0, 1), Fraction(0, 1)]
```

## Files Changed

- `reconstitution/swarm-2026-04-30-agent-275-nonscalar-costello-binary-row-construction-push.md`
