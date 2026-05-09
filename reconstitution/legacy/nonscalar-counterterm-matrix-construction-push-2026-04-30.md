# Non-scalar counterterm matrix construction push

Date: 2026-04-30.
Scope: report-only attack-heal pass for the finite-window non-scalar
Costello/QME counterterm matrix problem.  No TeX, script, figure, source, or
build file was edited.

## Stable result

The finite-window matrix criterion is sharp enough to decide the first
supplied non-scalar row.  The construction does not close with the current
data.

The first solved rows remain zero:

- the retained scalar-zero order-one row \(\alpha_{11}\) has
  \(R^{\mathrm{row}}_{\alpha_{11},M}=0\),
  \(S_{\alpha_{11},M}=0\), and \(C_{1,M}=0\);
- the minimal full-equivariant order-two branch has empty residual,
  empty primitive matrix, zero primitive, and zero Roos class.

The first unsolved supplied row is the order-three CE-source row
\[
  \theta_3=\mathrm{CE}(\Theta_3,\nu_3),\qquad
  \mathsf E_{\theta_3,M}=-K^M_{\Theta_3}(\zeta_{M,\nu_3}).
\]
Its scalar gate is zero, and its row transport is identity for
\(N\ge 3\), zero below the degree-three window.  In the currently supplied
one-row finite complex,
\[
  \mathcal K^0_{\theta_3,M}=0,\qquad
  \mathcal K^1_{\theta_3,M}=\C\mathsf E_{\theta_3,M},\qquad d=0.
\]
Thus
\[
  A^M=\begin{bmatrix}\end{bmatrix}_{1\times0},\qquad
  r^M=(1),\qquad -r^M=(-1).
\]
The equation \(A^M c=-r^M\) has no solution.  The left-cokernel functional
\[
  \ell_{\theta_3}(\mathsf E_{\theta_3,M})=1
\]
satisfies \(\ell_{\theta_3}A^M=0\) and
\(\ell_{\theta_3}(r^M)=1\).  This is an exact obstruction in the displayed
finite row subcomplex.

## Primitive construction attempt

The only fixed-window primitive column that would kill the row is
\[
  A^M_{\theta_3,C}=-1,\qquad
  d_{\mathrm{ns},M}C_{\theta_3,M}=-\mathsf E_{\theta_3,M}.
\]
With this column the system is solved by \(c_M=1\).  If the primitive has
identity/zero transport
\[
  P^{M,N}_{C,C}=1\quad(N\ge3),\qquad P^{M,N}_{C,C}=0\quad(N<3),
\]
then \(T^{M,N}A^M=A^NP^{M,N}\) and
\([P^{M,N}c_M-c_N]=0\).  The Roos class is zero for this supplied payload.

The script accepts exactly this interface fixture for a CE ancestor and for
a local counterterm.  It rejects the current data, because no degree-zero
row and no differential entry \(dC=-E\) is supplied.

## CE-source ancestor attack

I tested the pure source-ancestor route in the finite two-\(u\),
Hamiltonian-degree \(\le 3\) envelope with constants removed and
\[
  [H_{a,b},H_{r,s}]=(as-br)H_{a+r-1,b+s-1}.
\]
In the symmetric presentation:
\[
  \#H=9,\qquad \#\eta\text{-columns}=45,\qquad
  \#\text{output rows}=304,\qquad \#\text{nonzero entries}=380.
\]
The covector
\[
  q=
  -\frac12 e^*_{((H_{0,1},H_{0,1}),c_{\rho_{0,2}})}
  +e^*_{((H_{0,1},H_{2,0}),c_{\rho_{2,1}})}
\]
satisfies \(q\,d_{\mathrm{CE}}=0\) and evaluates to \(1\) on the
\(\nu_3\) target \(((H_{0,1},H_{2,0}),c_{\rho_{2,1}})\).  In the ordered
presentation the analogous covector
\[
  q_{\mathrm{ord}}=
  -\frac12 e^*_{((H_{0,1},H_{0,1}),c_{\rho_{0,2}})}
  +\frac13 e^*_{((H_{0,1},H_{0,2}),c_{\rho_{0,3}})}
  +e^*_{((H_{2,0},H_{0,1}),c_{\rho_{2,1}})}
\]
also satisfies \(q_{\mathrm{ord}}d_{\mathrm{CE}}=0\) and
\(q_{\mathrm{ord}}(\nu_3)=1\).  Hence no pure CE ancestor
\(d_{\mathrm{CE}}\eta=\zeta_{M,\nu_3}\) exists in this finite source
envelope.  A CE-ancestor construction must enlarge the source habitat and
then rerun the Hom-valued Bianchi, scalar, transport, and Roos gates.

## Companion-face attack

The eight-face source-algebraic companion candidate is not a primitive.  It
changes the degree-one row presentation.  The current residual vector in the
declared basis is
\[
\begin{aligned}
  R^{\mathrm{cand}}_{\Theta_3,M}
  ={}&2E_{\nu02}-2E_{\nu20}+3E_{\nu03}+2E_{\nu12,1}
      -E_{\nu12,2}\\
    &+E_{\theta_3}-2E_{\nu21,2}-3E_{\nu30}.
\end{aligned}
\]
Its coefficient sum is zero and every listed scalar projection is zero, but
the row vector is not zero.  With no degree-zero primitive rows in this
presentation, \(A^M\) is an \(8\times0\) matrix and
\[
  \ell_{\theta_3}(R^{\mathrm{cand}}_{\Theta_3,M})=1
\]
is again a left-cokernel certificate in the declared row basis.

The diagonal source-face transport
\[
  v^{M,N}_{\nu;\nu'}=
  \begin{cases}
    1,&\nu=\nu',\ d(\nu)\le N,\\
    0,&\text{otherwise}
  \end{cases}
\]
is a cocycle, but it sends the candidate to
\[
  2E^2_{\nu02}-2E^2_{\nu20}
\]
at \(N=2\).  The missing lower-window identity is
\[
  E^2_{\nu02}=E^2_{\nu20}
\]
in the chosen lower-window row basis, or a recomputed lower-window
presentation.  The missing marked Costello data are the labelled
\(d_{\mathrm{CE}}\zeta_M\) with current labels, orientation/Koszul signs,
renormalized weights \(K^M_{\Theta_3}(\zeta_{M,\nu})\) in one row basis,
marker transports, basis-reduced \(v^{M,N}\), and codimension-two incidence
table.

## Current and wavefront gate

The \(\theta_3\) script row uses \(B_\theta\in\mathcal D_c^{\mathrm{reg}}(I)\).
For arbitrary compactly supported distributions the graph weight is not
defined by the current data.  A non-regular wavefront branch must first pass
the graphwise product, diagonal-extension, counterterm, and pushforward
wavefront conditions.  Otherwise the obstruction is microlocal before the
matrix \(A^M c=-r^M\) is formed.  If a singular quotient residual survives,
the obstruction is
\[
  \eta^{\mathrm{reg}}_{n_0,M}=[s^{\mathrm{WF}}_{n_0,M}],
\]
killed in the original complex only by a degree-zero singular primitive
\(\bar d_Mq_M(C^{\mathrm{sing}}_{n_0,M})=-s^{\mathrm{WF}}_{n_0,M}\).

## Exact obstruction theorem to insert next

Insert after the present \(\theta_3\) acceptance gate, or after
Proposition~\(\ref{prop:app-first-order-three-larger-package-datum}\):

```tex
\begin{prop}[First non-scalar counterterm matrix obstruction]
Work in the native finite-window realization habitat and assume the
minimal full-equivariant package is closed through order two with
\(C_{1,M}=C_{2,M}=0\).  Let the first supplied nonzero scalar-zero
order-three row be
\[
  \mathsf E_{\theta_3,M}=-K^M_{\Theta_3}(\zeta_{M,\nu_3}),
  \qquad \widehat\sigma_{\mathrm{sc},M}(\mathsf E_{\theta_3,M})=0,
\]
with identity/zero row transport as above.  In the supplied one-row
finite subcomplex the primitive matrix is \(1\times0\), the residual is
\(r^M=(1)\), and \(\ell_{\theta_3}(\mathsf E_{\theta_3,M})=1\) proves
\([ \mathsf E_{\theta_3,M}]\ne0\).

The row is killed in an enlarged package exactly by one of the following
data:
\[
  d_{\mathrm{ns},M}C_{\theta_3,M}=-\mathsf E_{\theta_3,M},\qquad
  \widehat\sigma_{\mathrm{sc},M}(C_{\theta_3,M})=0,\qquad
  T^{M,N}A^M=A^NP^{M,N},\qquad
  [P^{M,N}c_M-c_N]=0,
\]
or by a complete companion-face table whose signed residual vector is
zero in one marked Costello row basis and whose source-face transport has
zero lower-window residual.  In the finite two-\(u\), degree-\(\le3\)
source envelope, the covector \(q\) displayed in the report satisfies
\(qd_{\mathrm{CE}}=0\) and \(q(\zeta_{M,\nu_3})=1\), so no pure CE ancestor
exists there.  The eight-face source-algebraic table remains obstructed
by its nonzero row vector and by the \(N=2\) residual
\(2E^2_{\nu02}-2E^2_{\nu20}\).
\end{prop}
```

## Verification

Commands run:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py > /tmp/finite-window-agent244.json
python3 -m json.tool /tmp/finite-window-agent244.json > /tmp/finite-window-agent244.pretty.json
python3 - <<'PY'
# focused JSON inspection of primitive, payload, and companion rows
PY
python3 - <<'PY'
# finite two-u CE matrix probe with H-degree <= 3 and constants removed
PY
rg -n -F -e 'A^M c=-r^M' -e 'theta_3' -e 'Roos' \
  main.tex appendix-unreduced-bv-qme.tex open-obligations.tex claim-strength-ledger.tex
```

Observed results:

- `py_compile`, JSON emission, and JSON parsing passed.
- `minimal_full_equivariant_order_2_zero`: primitive exists, empty
  residual, zero Roos class.
- `theta_3_current_finite_row_subcomplex`: primitive does not exist;
  \(A=[[]]\), \(r=(E_{\theta_3}:1)\), target \(-r\), obstruction covector
  \(E_{\theta_3}\mapsto1\), obstruction value \(1\).
- `theta3_ce_ancestor_supplied_exact_payload` and
  `theta3_counterterm_supplied_exact_payload`: accepted only with
  differential value \(-1\), scalar zero, \(TA=AP\), and zero Roos class.
- the eight-face candidate is rejected; its residual vector is
  \((2,-2,3,2,-1,1,-2,-3)\), coefficient sum \(0\), and \(N=2\) residual
  \((2,-2)\).
- the finite CE probe gave \(q d_{\mathrm{CE}}=0\), \(q(\nu_3)=1\) in both
  symmetric and ordered presentations above.
