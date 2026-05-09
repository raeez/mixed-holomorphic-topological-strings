# Agent 245 - Theta3 Controlled-Enlargement Witness Search

Status: report-only.  Files staged: this report and
`reconstitution/theta3-controlled-enlargement-witness-search-2026-04-30.md`.
No TeX, script, figure, build artifact, or manuscript file was edited.

## Claim Attacked

Agent 240 left three exact obstructions:

1. no one-row scalar-zero counterterm in
   \(K^0_{\theta_3,M}=0\), \(K^1_{\theta_3,M}=\C E_{\theta_3,M}\);
2. no finite two-\(u\), Hamiltonian-degree-\(\leq3\), pure CE ancestor;
3. no accepted eight-face companion table.

The attacked supremum claim was that the next controlled enlargement could
make \(\theta_3\) true without weakening the theorem.

## Findings

The pure two-\(u\) CE obstruction strengthens.  In every finite Hamiltonian
degree, not only degree \(\leq3\), the covector
\[
  q_{2u}
  =
  e^*_{((H_{0,1},H_{2,0}),c_{\rho_{2,1}})}
  -\frac12 e^*_{((H_{0,1},H_{0,1}),c_{\rho_{0,2}})}
\]
satisfies \(q_{2u}d_{\mathrm{CE}}=0\) and
\(q_{2u}(\zeta_{M,\nu_3})=1\).  The only source column seen by \(q_{2u}\)
is \(u_{H_{1,0}}u_{H_{0,1}}\), where the coefficients \(2\) and \(1\)
cancel.  Degree enlargement alone is therefore dead.

The local counterterm route is the smallest closing enlargement, but only
as missing data.  The required matrix is
\[
  A=(-1),\qquad r=(1),\qquad c=1.
\]
The present no-column or zero-column cases still have cokernel
\(\ell(E_{\theta_3})=1\).

The companion route needs two independent additions.  At \(M\ge3\) the
candidate residual is
\[
  r_8=(2,-2,3,2,-1,1,-2,-3)^T.
\]
The current lower transport is
\[
  V^{M,2}_{\mathrm{diag}}r_8=(2,-2)^T,
\]
so a fixed-window companion identity would still require either
\(E^2_{\nu_{02}}=E^2_{\nu_{20}}\), a lower primitive with boundary
\(-2E^2_{\nu_{02}}+2E^2_{\nu_{20}}\), or a recomputed non-diagonal
transport matrix.  A formal non-diagonal theta column
\((-2,2)^T\) would cancel the lower residual, but it contradicts the current
declared truncation \(E_{\theta_3}\mapsto0\) for \(N<3\) unless derived from
new marked weight coordinates.

The marked-source route must add a generator outside the ordinary two-\(u\)
source algebra.  The missing datum is a marked generator
\(\eta^{\mathrm{mark}}_{\theta_3,M}\) with a boundary column of
\(q_{2u}\)-value \(1\), plus codimension-two closure, Hom-valued Bianchi
cancellation, scalar-zero value, and compatible transport.

## Claim Status

No current enlargement closes.  The stronger obstruction theorem is:
ordinary pure two-\(u\) source enlargement in any polynomial degree cannot
produce the \(\theta_3\) ancestor.  A valid positive theorem must supply one
of:

- \(A^M_{\theta_3,C}=-1\) from a scalar-zero CE or local counterterm
  primitive with zero Roos class;
- a marked source generator whose new boundary defeats \(q_{2u}\) and
  satisfies \(d_{\mathrm{CE}}^2=0\) by a supplied codimension-two table;
- a marked companion table proving \(r_8=0\) and
  \(V^{M,N}r_8=0\) in every lower window.

## Next Theorem Insertion

Insert a theorem after `thm:theta-three-companion-face-obstruction`:

**Theta3 controlled-enlargement obstruction.**  The tuple
\[
  (\ell_{\theta_3},q_{2u},r_8,V^{M,2}_{\mathrm{diag}}r_8,
  \mathcal C^{(2)}_{\mathrm{missing}})
\]
is the exact obstruction to the current controlled enlargements.  It is
killed only by the missing degree-zero column, marked source generator, or
marked companion/transport matrix listed above.

Mirror a short consequence near `prop:theta-three-finite-window-acceptance-gate`
in `main.tex` only when TeX edits are authorized.

## Verification

Commands run:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py
python3 - <<'PY'
# checked theta3 primitive gates, eight-face residual, N=2 transport,
# and q_{2u}d=0 for degree bounds D=3,...,9
PY
```

Focused output:

```text
one_row False [[]] [['E_theta_3', '1']] [['E_theta_3', '1']] 1
theta3_counterterm_without_differential_entry False 0 [] [['E_theta_3', '1']]
theta3_counterterm_supplied_exact_payload True -1 [['C_theta_3_ct', '1']] []
two_u_q 3..9 q_d=0 True q_target 1
eight_residual [['E_nu02','2'],...,['E_nu30','-3']]
eight_n2 [['E_nu02','2'], ['E_nu20','-2']]
```

No PDF build was run because the task is report-only and the checkout has
concurrent edits outside the owned paths.
