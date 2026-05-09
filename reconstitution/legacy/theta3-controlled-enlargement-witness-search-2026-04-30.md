# Theta3 Controlled-Enlargement Witness Search

Status: report-only.  No TeX, script, figure, or manuscript file was edited.
This note is the supremum follow-up to Agent 240.  It searches the next
controlled enlargement that could make the \(\theta_3\) row true without
softening the theorem.

## Stable Core

The active row is
\[
  \mathsf E_{\theta_3,M}
  =
  -K^M_{\Theta_3}(\zeta_{M,\nu_3}),
  \qquad
  \widehat\sigma_{\mathrm{sc},M}(\mathsf E_{\theta_3,M})=0,
\]
with supplied one-row complex
\[
  \mathcal K^0_{\theta_3,M}=0,\qquad
  \mathcal K^1_{\theta_3,M}=\C\mathsf E_{\theta_3,M},\qquad d=0.
\]
The primitive-search matrix is \(1\times0\), the residual is \(r=(1)\),
and the covector \(\ell_{\theta_3}(\mathsf E_{\theta_3,M})=1\) proves
\[
  [\mathsf E_{\theta_3,M}]\neq0
  \quad\text{in the supplied one-row finite complex.}
\]

The executable validator agrees:

```text
one_row False [[]] [['E_theta_3', '1']] [['E_theta_3', '1']] 1
```

Thus a formal symbol \(C_{\theta_3}\) is not a counterterm.  A primitive
must add a degree-zero column
\[
  A^M_{\theta_3,C}=-1,\qquad
  d_{\mathrm{ns},M}C_{\theta_3,M}=-\mathsf E_{\theta_3,M},
\]
with scalar projection zero, \(T^{M,N}A^M=A^NP^{M,N}\), and zero Roos
class.

## Source-CE Enlargement

Agent 240 obstructed the finite two-\(u\), Hamiltonian-degree-\(\leq3\)
pure CE ancestor.  The obstruction is in fact degree-independent for the
ordinary symmetric two-\(u\) source envelope.

Let \(H_{a,b}=z_1^az_2^b\) and
\[
  [H_{a,b},H_{r,s}]=(as-br)H_{a+r-1,b+s-1}.
\]
In the symmetric two-\(u\) source complex define
\[
  B_{\nu_3}
  =
  ((H_{0,1},H_{2,0}),c_{\rho_{2,1}}),
  \qquad
  B_{\nu_{02}}
  =
  ((H_{0,1},H_{0,1}),c_{\rho_{0,2}}),
\]
and the row functional
\[
  q_{2u}=e^*_{B_{\nu_3}}-\frac12 e^*_{B_{\nu_{02}}}.
\]
Then
\[
  q_{2u}d_{\mathrm{CE}}=0,\qquad q_{2u}(B_{\nu_3})=1.
\]

The proof is local.  The only two-\(u\) source column hitting either
displayed row is \(u_{H_{1,0}}u_{H_{0,1}}\).  Its \(c_{\rho_{0,2}}\)-face
has coefficient \(2\), since \([H_{1,0},H_{0,2}]=2H_{0,1}\), and its
\(c_{\rho_{2,1}}\)-face has coefficient \(1\), since
\([H_{1,0},H_{2,1}]=H_{2,0}\).  Hence
\[
  q_{2u}\bigl(d_{\mathrm{CE}}(u_{H_{1,0}}u_{H_{0,1}})\bigr)
  =
  -\frac12\cdot2+1=0,
\]
and all other columns pair trivially with \(q_{2u}\).

The computation was also checked for degree bounds \(D=3,\ldots,9\):

```text
two_u_q 3 basis 9 cols 45 q_d=0 True q_target 1
two_u_q 4 basis 14 cols 105 q_d=0 True q_target 1
two_u_q 5 basis 20 cols 210 q_d=0 True q_target 1
two_u_q 6 basis 27 cols 378 q_d=0 True q_target 1
two_u_q 7 basis 35 cols 630 q_d=0 True q_target 1
two_u_q 8 basis 44 cols 990 q_d=0 True q_target 1
two_u_q 9 basis 54 cols 1485 q_d=0 True q_target 1
```

Conclusion: no ordinary pure two-\(u\) CE ancestor exists in any
polynomial finite window.  Enlarging the degree cutoff alone cannot make
\(\theta_3\) true.

## Candidate Enlargements

### 1. Minimal lower-window rows

The eight-face companion residual has ordered basis
\[
  (E_{\nu_{02}},E_{\nu_{20}},E_{\nu_{03}},E_{\nu_{12}^{(1)}},
  E_{\nu_{12}^{(2)}},E_{\theta_3},E_{\nu_{21}^{(2)}},E_{\nu_{30}})
\]
and vector
\[
  r_8=(2,-2,3,2,-1,1,-2,-3)^T.
\]
The current diagonal transport to the \(N=2\) lower window is
\[
  V^{M,2}_{\mathrm{diag}}
  =
  \begin{pmatrix}
  1&0&0&0&0&0&0&0\\
  0&1&0&0&0&0&0&0
  \end{pmatrix},
\]
so
\[
  V^{M,2}_{\mathrm{diag}}r_8=(2,-2)^T.
\]
Thus lower rows alone cannot repair the fixed \(M\geq3\) residual.  Even
after a fixed-window identity \(R_{\Theta_3,M}^{\mathrm{cand}}=0\) is
proved, the tower still needs one of:
\[
  E^2_{\nu_{02}}=E^2_{\nu_{20}},
  \qquad\text{or}\qquad
  D^2_{02,20}\in\mathcal K^0_{\mathrm{ns},2}(I),\quad
  dD^2_{02,20}=-2E^2_{\nu_{02}}+2E^2_{\nu_{20}}.
\]

A non-diagonal transport could also kill the \(N=2\) residual, for example
by replacing the \(\theta_3\)-column with
\[
  v^{M,2}_{\theta_3;\nu_{02}}=-2,\qquad
  v^{M,2}_{\theta_3;\nu_{20}}=2.
\]
Then \(V^{M,2}r_8=0\).  This is not admissible with the current data,
because Proposition `concrete-order-three-larger-package-row` and the
script both set the \(N<3\) transport of \(E_{\theta_3}\) to zero.  Such a
matrix is a new theorem datum: it must be derived from projected
renormalized weights, not chosen to cancel a vector.

### 2. Marked source generator

The all-degree covector \(q_{2u}\) rules out every ordinary two-\(u\)
ancestor.  A marked source route must therefore add a genuinely new source
generator
\[
  \eta^{\mathrm{mark}}_{\theta_3,M}
\]
outside the ordinary symmetric two-\(u\) CE algebra.  The minimal useful
boundary is
\[
  d_{\mathrm{CE}}\eta^{\mathrm{mark}}_{\theta_3,M}
  =
  \zeta_{M,\nu_3}
\]
or a closed corrected boundary
\[
  d_{\mathrm{CE}}\eta^{\mathrm{mark}}_{\theta_3,M}
  =
  \zeta_{M,\nu_3}+Z^{\mathrm{extra}}_M
\]
whose extra faces have zero total Costello row after the marked table is
included.

The required matrix datum is a new source column \(G_{\theta_3}\) with
\[
  q_{2u}(G_{\theta_3})=1,
\]
plus the codimension-two closure table proving \(d_{\mathrm{CE}}^2=0\) on
the marked extension and the Hom-valued Bianchi identity proving
\[
  d_{\mathrm{ns},M}K^M_{\Theta_3}(\eta^{\mathrm{mark}}_{\theta_3,M})
  =
  -\mathsf E_{\theta_3,M}.
\]
No such generator, closure table, or transport matrix is present.

### 3. Controlled local counterterm primitive

This is the smallest fixed-window enlargement that would close the row.
Add one scalar-zero degree-zero local functional
\[
  C^{\mathrm{ct}}_{\theta_3,M}
  =
  C^M_{\Theta_3,\nu_3,w}(\epsilon;B^\Theta_\bullet)
  \in\mathcal K^0_{\mathrm{ns},M}(I)
\]
with
\[
  d_{\mathrm{ns},M}C^{\mathrm{ct}}_{\theta_3,M}
  =
  -\mathsf E_{\theta_3,M},\qquad
  \widehat\sigma_{\mathrm{sc},M}(C^{\mathrm{ct}}_{\theta_3,M})=0,
\]
and identity/zero transport
\[
  \pi_{M,N}C^{\mathrm{ct}}_{\theta_3,M}
  =
  C^{\mathrm{ct}}_{\theta_3,N}\ (N\geq3),\qquad
  0\ (N<3).
\]
Then the fixed-window matrix is \(A=(-1)\), \(r=(1)\), and \(c=1\).
The validator records exactly this:

```text
theta3_counterterm_supplied_exact_payload True -1 [['C_theta_3_ct', '1']] []
```

But this is an interface fixture, not current mathematics.  Without the
differential entry the matrix is \(A=(0)\), and the same cokernel
\(\ell_{\theta_3}\) survives:

```text
theta3_counterterm_without_differential_entry False 0 [] [['E_theta_3', '1']]
```

### 4. Extended companion faces

The current eight-face table is source-algebraic only.  Its residual is
\[
\begin{aligned}
  R_{\Theta_3,M}^{\mathrm{cand}}
  ={}&2E_{\nu_{02}}-2E_{\nu_{20}}+3E_{\nu_{03}}
      +2E_{\nu_{12}^{(1)}}-E_{\nu_{12}^{(2)}}\\
    &+E_{\theta_3}-2E_{\nu_{21}^{(2)}}-3E_{\nu_{30}},
\end{aligned}
\]
and the validator returns the nonzero coordinate vector
\[
  (2,-2,3,2,-1,1,-2,-3).
\]

A theorem-grade companion enlargement must supply the marked Costello table
\[
  \left(
    d_{\mathrm{CE}}\zeta_M,\,
    \epsilon^{\mathrm{CE}}_{\Theta_3,\nu},\,
    K^M_{\Theta_3}(\zeta_{M,\nu}),\,
    \mu_\nu,\,
    v^{M,N}_{\nu;\nu'},\,
    \mathcal C^{(2)}_{\nu,\nu'}
  \right)_{\nu,\nu'} ,
\]
and prove two equations:
\[
  R_{\Theta_3,M}^{\mathrm{cand}}=0\quad(M\geq3),
  \qquad
  v^{M,N}R_{\Theta_3,M}^{\mathrm{cand}}=0\quad(N<M).
\]
At \(N=2\) this includes the lower-window relation or primitive displayed
above.  The current table supplies neither the fixed-window row relation nor
the lower-window relation.

## Minimal-Enlargement Obstruction Theorem

The exact obstruction theorem to insert is:

**Theta3 controlled-enlargement obstruction.**  In the current
finite-window graph package, and after adjoining all ordinary pure two-\(u\)
CE source rows in any Hamiltonian degree, the row
\(\mathsf E_{\theta_3,M}\) remains non-exact.  The source obstruction is the
degree-independent covector
\[
  q_{2u}
  =
  e^*_{((H_{0,1},H_{2,0}),c_{\rho_{2,1}})}
  -\frac12 e^*_{((H_{0,1},H_{0,1}),c_{\rho_{0,2}})},
\]
with \(q_{2u}d_{\mathrm{CE}}=0\) and
\(q_{2u}(\zeta_{M,\nu_3})=1\).  Therefore an accepted enlargement must
leave the ordinary pure two-\(u\) source envelope by supplying one of the
following exact data:

1. a marked source generator \(\eta^{\mathrm{mark}}_{\theta_3,M}\) whose
   boundary has \(q_{2u}\)-value \(1\), together with codimension-two
   closure, Hom-valued Bianchi cancellation, scalar-zero value, and
   compatible transport;
2. a scalar-zero local counterterm primitive
   \(C^{\mathrm{ct}}_{\theta_3,M}\) with boundary matrix column
   \(A^M_{\theta_3,C}=-1\) and zero Roos class;
3. a marked companion-face table proving
   \(R_{\Theta_3,M}^{\mathrm{cand}}=0\) and a lower-window transport
   relation killing \(2E^2_{\nu_{02}}-2E^2_{\nu_{20}}\).

Absent these data, the obstruction is the tuple
\[
  \left(
    \ell_{\theta_3},\,
    q_{2u},\,
    r_8,\,
    V^{M,2}_{\mathrm{diag}}r_8,\,
    \mathcal C^{(2)}_{\mathrm{missing}}
  \right)
  =
  \left(
    e^*_{\theta_3},\,
    q_{2u},\,
    (2,-2,3,2,-1,1,-2,-3),\,
    (2,-2),\,
    \mathcal C^{(2)}_{\mathrm{missing}}
  \right).
\]

## Next Theorem Insertion

Insert the theorem after
`thm:theta-three-companion-face-obstruction` in
`tate-P1-hadamard-mittag-leffler.tex`, and mirror the short consequence
after `prop:theta-three-finite-window-acceptance-gate` in `main.tex` only
when manuscript editing is authorized.

The insertion should not downgrade the \(\theta_3\) target.  It should say:
ordinary finite-degree source enlargement is now ruled out; the next true
positive theorem must construct the missing marked generator, the missing
local counterterm column, or the missing marked companion/transport matrix.

## Verification

Commands run:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py
python3 - <<'PY'
# focused extraction of theta3 primitive, companion, and pure two-u q checks
PY
```

The focused extraction returned the matrix rows quoted above.  No PDF build
was run because this assignment is report-only and the shared checkout has
active concurrent manuscript/build edits outside the owned paths.
