# Non-Scalar Row-Matrix Script Evidence Audit

Status: integration-facing audit. No TeX or script edit.

## Conclusion

The current TeX is aligned with `scripts/finite_window_graph_array.py` for
the script-backed row-matrix facts:

- generic finite-row primitive equation \(Ac=-r\);
- minimal full-equivariant empty-row primitive search;
- current \(\theta_3\) one-row obstruction;
- accepted primitive payloads only as interface fixtures with \(dC=-E\);
- rejection of the eight-face companion candidate as theorem-grade
  cancellation;
- \(N=2\) diagonal-transport residual \(2E_{\nu_{02}}-2E_{\nu_{20}}\).

The Bianchi-exposed lower matrix
\[
  A_D^2=(-2,2,1)^T,\qquad r_2=(2,-2,0)^T
\]
is not a `finite_window_graph_array.py` output. It is evidence from the
theta3 Bianchi reports. Keep this boundary explicit.

## Script-Certified Matrix Data

The current one-row \(\theta_3\) package has
\[
  K^0_{\theta_3,M}=0,\qquad
  K^1_{\theta_3,M}=\mathbb C E_{\theta_3},\qquad
  d=0,\qquad r=(1).
\]
The boundary matrix is \(1\times0\). The equation \(Ac=-r\) has no solution.
The cokernel covector \(\ell(E_{\theta_3})=1\) detects the residual. This is
exactly the TeX statement in `tate-P1-hadamard-mittag-leffler.tex` and the
front theorem-lane summaries.

The minimal full-equivariant order-two case has empty row and primitive
bases, residual zero, target zero, primitive exists, and zero Roos class.
This supports the minimal zero-row matrix
\[
  A^M_{\min}:0\to0,\qquad r^M_{\min}=0.
\]
The \(h^M_{\min}=0\) notation in centrality statements is the homotopy
coefficient version of the script's generic coefficient vector \(c\).

## Payload Gates

Current script decisions:

- absent CE ancestor: rejected;
- CE ancestor without \(dC=-E\): rejected;
- CE ancestor with \(dC=-E\), scalar-zero, \(TA=AP\), zero Roos: accepted
  as an interface fixture, not current data;
- absent local counterterm: rejected;
- local counterterm without \(dC=-E\): rejected;
- local counterterm with \(dC=-E\), scalar-zero, \(TA=AP\), zero Roos:
  accepted as an interface fixture, not current data;
- complete companion fixture without marked Costello table and lower-window
  zero: rejected.

Current TeX keeps these statuses. It does not claim the current
\(\theta_3\) row is solved by a named \(C_{\theta_3}\).

## Eight-Face Table

The script records the eight-face candidate vector
\[
  (2,-2,3,2,-1,1,-2,-3)
\]
on
\[
  E_{\nu_{02}},E_{\nu_{20}},E_{\nu_{03}},
  E_{\nu_{12}^{(1)}},E_{\nu_{12}^{(2)}},
  E_{\theta_3},E_{\nu_{21}^{(2)}},E_{\nu_{30}}.
\]
The coefficient sum is zero, but the residual vector is nonzero. Diagonal
transport to \(N=2\) leaves
\[
  2E^2_{\nu_{02}}-2E^2_{\nu_{20}}.
\]
The marked Costello incidence/weight table and lower-window zero are
missing. Current TeX states this as an obstruction, not a cancellation.

## Evidence Boundary

Do not cite `finite_window_graph_array.py` for these TeX claims:

- \(q_{2u}d_{\mathrm{CE}}=0\) and
  \(q_{2u}(\zeta_{M,\nu_3})=1\);
- \(q_{2u}\)-value zero on the eight-face row;
- \(D^2_{02,20}=K^2_{\Theta_3}(\zeta^0_2)\);
- the Bianchi row \(\mathfrak b^2_{02,20}\);
- \(A_D^2=(-2,2,1)^T\), \(r_2=(2,-2,0)^T\);
- \(\widetilde\lambda_{02,\mathfrak b}A_D^2=0\) and
  \(\widetilde\lambda_{02,\mathfrak b}(r_2)=1\).

Those are later Bianchi/source-envelope evidence. They are present in current
TeX with the right obstruction status, but they are not script outputs.

## Checks Run

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py
rg -n -F -e 'A^M h' -e 'A^M c' -e 'A_D^2' --glob '*.tex'
```

No PDF build was run.
