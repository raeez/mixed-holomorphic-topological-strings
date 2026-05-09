# Theta3 Companion-Face Construction Attempt

Status: construction attempted; no TeX or script edit made.  The current
one-row obstruction is not a terminal conclusion.  The first source-algebra
table containing the displayed \(\nu_3\) face can be written, but it does
not yet give a zero signed Costello row sum.

## Starting Data

The active row is
\[
  \mathsf E_{\theta_3,M}
    =
  -K^M_{\Theta_3}(\zeta_{M,\nu_3}),
  \qquad
  \epsilon^{\mathrm{CE}}_{\Theta_3,\nu_3}=+1.
\]
It has labels
\[
  u_{a(t)dt\otimes z_1^2},\qquad
  u_{b(t)dt\otimes z_2},\qquad
  c_{B_\theta,\rho_{2,1}},
\]
and scalar projection zero in the full-equivariant marked habitat.  The
finite row subcomplex currently supplied has
\[
  \mathcal K^0_{\theta_3,M}=0,\qquad
  \mathcal K^1_{\theta_3,M}=\mathbb C\mathsf E_{\theta_3,M}.
\]

The CE/PV sign convention gives, for \(H_{p,q}=z_1^pz_2^q\),
\[
  [H_{a,b},H_{r,s}]=(as-br)H_{a+r-1,b+s-1},
  \qquad
  d_{\mathrm{CE}}u_K=\sum_J C^L_{KJ}u_Lc^J .
\]
Among two-\(u\), degree-zero source monomials with the same external
shape, the face \(\nu_3\) can only come from the differential of
\(u_{a,H_{1,0}}\) against \(c_{B_\theta,\rho_{2,1}}\), with the second
input \(u_{b,H_{0,1}}\) unchanged:
\[
  [H_{1,0},H_{2,1}]=H_{2,0}.
\]
Thus the minimal source ancestor of this shape whose differential contains
\(\nu_3\) is
\[
  \zeta^0_M=u_{a,H_{1,0}}\,u_{b,H_{0,1}},
\]
up to the still-unsupplied current-label convention for the fixed
\(B_\theta\)-coordinate.

## Candidate Source-Face Table

For \(M\geq3\), the monomial CE differential of
\(\zeta^0_M\), truncated to Hamiltonian degree \(\leq3\) and with constants
removed, gives the following nonzero faces after the two
\(\rho_{1,1}\)-terms cancel.  Put
\[
  E^M_{\Theta_3,\nu}:=-K^M_{\Theta_3}(\zeta_{M,\nu}),
  \qquad
  R^M_{\Theta_3,\nu}
  =\epsilon^{\mathrm{CE}}_{\Theta_3,\nu}E^M_{\Theta_3,\nu}.
\]

| face | \(\epsilon^{\mathrm{CE}}\) | source face \(\zeta_{M,\nu}\) | row contribution |
|---|---:|---|---|
| \(\nu_{02}\) | \(+2\) | \(u_{a,H_{0,1}}u_{b,H_{0,1}}c_{B_\theta,\rho_{0,2}}\) | \(2E_{\nu_{02}}\) |
| \(\nu_{20}\) | \(-2\) | \(u_{a,H_{1,0}}u_{b,H_{1,0}}c_{B_\theta,\rho_{2,0}}\) | \(-2E_{\nu_{20}}\) |
| \(\nu_{03}\) | \(+3\) | \(u_{a,H_{0,2}}u_{b,H_{0,1}}c_{B_\theta,\rho_{0,3}}\) | \(3E_{\nu_{03}}\) |
| \(\nu_{12}^{(1)}\) | \(+2\) | \(u_{a,H_{1,1}}u_{b,H_{0,1}}c_{B_\theta,\rho_{1,2}}\) | \(2E_{\nu_{12}^{(1)}}\) |
| \(\nu_{12}^{(2)}\) | \(-1\) | \(u_{a,H_{1,0}}u_{b,H_{0,2}}c_{B_\theta,\rho_{1,2}}\) | \(-E_{\nu_{12}^{(2)}}\) |
| \(\nu_3=\nu_{21}^{(1)}\) | \(+1\) | \(u_{a,H_{2,0}}u_{b,H_{0,1}}c_{B_\theta,\rho_{2,1}}\) | \(\mathsf E_{\theta_3,M}\) |
| \(\nu_{21}^{(2)}\) | \(-2\) | \(u_{a,H_{1,0}}u_{b,H_{1,1}}c_{B_\theta,\rho_{2,1}}\) | \(-2E_{\nu_{21}^{(2)}}\) |
| \(\nu_{30}\) | \(-3\) | \(u_{a,H_{1,0}}u_{b,H_{2,0}}c_{B_\theta,\rho_{3,0}}\) | \(-3E_{\nu_{30}}\) |

The candidate full companion residual is therefore
\[
\begin{aligned}
  R^{\mathrm{cand}}_{\Theta_3,M}
  ={}&2E_{\nu_{02}}-2E_{\nu_{20}}
      +3E_{\nu_{03}}+2E_{\nu_{12}^{(1)}}-E_{\nu_{12}^{(2)}}\\
    &+\mathsf E_{\theta_3,M}
      -2E_{\nu_{21}^{(2)}}-3E_{\nu_{30}} .
\end{aligned}
\]
This is the first honest table to test.  It is not a proof of
cancellation.  Cancellation would require the actual graph-weight identity
\[
  R^{\mathrm{cand}}_{\Theta_3,M}=0
\]
in the declared degree-one row basis.

## Transport

The monomial source labels give a diagonal candidate for the source-face
transport.  Let \(d(\nu)\) be the Hamiltonian degree of the \(c\)-label:
\[
  d(\nu_{02})=d(\nu_{20})=2,\qquad
  d(\nu)=3\quad\text{for the other six faces}.
\]
For \(M\geq N\), set
\[
  v^{M,N}_{\nu;\nu'}=
  \begin{cases}
    1,&\nu=\nu'\text{ and }d(\nu)\leq N,\\
    0,&\text{otherwise}.
  \end{cases}
\]
This diagonal cutoff satisfies \(v^{M,P}=v^{N,P}v^{M,N}\).  It does not by
itself preserve a zero sum.  At \(N=2\) the projected candidate residual is
\[
  2E^N_{\nu_{02}}-2E^N_{\nu_{20}},
\]
so the tower would additionally require
\[
  E^N_{\nu_{02}}=E^N_{\nu_{20}}
\]
or a different lower-window row presentation.  No such graph-weight
identity is present.

## Attacks

1. Sign attack.  The sign of the exposed row is fixed:
\(\epsilon^{\mathrm{CE}}_{\nu_3}=+1\) and the curvature term
\(-\kappa d_{\mathrm{CE}}\) gives
\(\mathsf E_{\theta_3,M}=-K^M_{\Theta_3}(\zeta_{M,\nu_3})\).  A primitive
would need \(dC=-\mathsf E_{\theta_3,M}\).  The companion table above is not
a primitive; it changes the degree-one residual.

2. Source attack.  The source-algebra table is only monomial-level.  The
current labelled CE differential with the fixed distributional label
\(B_\theta\), interval labels \(a,b\), and admissible current products is
not written as a manuscript datum for this \(\Theta_3\) package.

3. Graph-weight attack.  The table cannot be tested without the eight
values
\[
  K^M_{\Theta_3}(\zeta_{M,\nu})
\]
in a common row basis.  In particular, the two \(c_{\rho_{2,1}}\)-faces
\[
  u_{a,H_{2,0}}u_{b,H_{0,1}}c_{\rho_{2,1}},
  \qquad
  u_{a,H_{1,0}}u_{b,H_{1,1}}c_{\rho_{2,1}}
\]
both have Hamiltonian product \(H_{2,1}\), but no Costello weight or
orientation computation identifies their row values or their ratio.

4. Incidence attack.  The marked Costello list requires the orientation
set \(\mathsf B_M(\Theta_3)\), output graphs, coefficients, and marker
transports.  The source CE signs above are not the full marked incidence
signs until those graph-orientation and marker-transport entries are
supplied and codimension-two closure is checked.

5. Tower attack.  Even a fixed-window identity at \(M=3\) would not solve
the inverse-system claim unless \(v^{M,N}\) sends the signed zero sum to
the lower-window signed zero sum.  The diagonal cutoff exposes the
degree-two residual \(2E_{\nu_{02}}-2E_{\nu_{20}}\), so lower-window
compatibility needs a separate graph-weight identity.

## Exact Residual

The exact missing datum is not the formal existence of another symbol
\(\nu_i\).  It is the marked source-face computation
\[
  \left(
    d_{\mathrm{CE}}\zeta_M,\,
    \epsilon^{\mathrm{CE}}_{\Theta_3,\nu},\,
    K^M_{\Theta_3}(\zeta_{M,\nu}),\,
    \mu_\nu,\,
    v^{M,N}
  \right)_{\nu\in F_{\Theta_3,M}}
\]
for the actual \(\Theta_3\) seed.  The minimal computation that would
supply it is:

1. fix the labelled source ancestor \(\zeta_M\) and compute its current CE
differential, including the \(B_\theta,a,b\) current labels;
2. evaluate the renormalized graph seed
\(K^M_{\Theta_3}=W^{R,M}_{\Theta_3,L,w}(B^\Theta_\bullet)\) on every
source face in the table;
3. express those evaluations in the chosen finite degree-one row basis;
4. compute the marked incidence signs and marker transports from the
finite marked Costello list;
5. verify codimension-two closure and the \(v\)-cocycle;
6. check the signed residual vector at \(M=3\) and after projection to
each \(N<3\).

Until this computation is made, the script's accepted
`theta3_complete_companion_faces_supplied_exact_payload` is an interface
fixture, not a construction.  The current validator also rejects a table
whose coordinates cancel but are not derived from the CE coefficients.  The
current one-row obstruction remains exact in the supplied finite row
subcomplex.

## Verification

Commands run:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py >/tmp/finite-window-agent215.json
python3 -m json.tool /tmp/finite-window-agent215.json >/tmp/finite-window-agent215.pretty.json
python3 - <<'PY'
import json
with open('/tmp/finite-window-agent215.json') as f:
    data=json.load(f)
print('primitive-search')
for row in data['finite_row_primitive_search_results']:
    if row['case'].startswith('theta'):
        print(row['case'], row['primitive_exists'],
              row['obstruction_value_on_residual'],
              row['primitive_coefficients'], row['obstruction_covector'])
print('companion-face checks')
for row in data['theta_3_companion_face_payload_checks']:
    print(row['case'], row['accepted'],
          row['residual_vector'], row['missing_fields'])
PY
python3 - <<'PY'
from collections import defaultdict
M=3
terms=[]
K1=(1,0); K2=(0,1)
for r in range(M+1):
    for s in range(M+1-r):
        if r+s==0:
            continue
        coeff=s
        L=(r,s-1)
        if coeff and min(L)>=0 and sum(L)>0:
            terms.append(("du_z1",(r,s),L,(L,K2),coeff))
        coeff=-r
        L=(r-1,s)
        if coeff and min(L)>=0 and sum(L)>0:
            terms.append(("du_z2",(r,s),L,(K1,L),coeff))
agg=defaultdict(int)
for origin,J,L,us,coeff in terms:
    key=(tuple(sorted(us)),J)
    agg[key]+=coeff
for (us,J),coeff in sorted(agg.items()):
    if coeff:
        print(coeff, us, J)
PY
git diff --check -- reconstitution/theta3-companion-face-construction-attempt-2026-04-30.md \
  reconstitution/swarm-2026-04-30-agent-215-theta3-companion-face-construction-attempt.md
rg -n "[[:blank:]]$" reconstitution/theta3-companion-face-construction-attempt-2026-04-30.md \
  reconstitution/swarm-2026-04-30-agent-215-theta3-companion-face-construction-attempt.md || true
```

`py_compile`, JSON emission, JSON parsing, focused script checks, and the
trailing-whitespace scan passed.  The current script reports the one-face
table as rejected, rejects the cancelling-coordinate guard case whose
coordinates are not verified from CE coefficients, and accepts the complete
table only as an interface payload.  No build was run; this lane is
report-only and the shared checkout has large concurrent manuscript edits
outside these owned paths.
