# Agent 215 - Theta3 Companion-Face Construction Attempt

Status: report-only.  No TeX or script files were edited.

## Result

I constructed the first CE source-face table that can contain the exposed
\(\theta_3\) face.  It starts from the only two-\(u\), degree-zero monomial
source of the same external shape whose CE differential can produce
\[
  u_{a,H_{2,0}}u_{b,H_{0,1}}c_{B_\theta,\rho_{2,1}}:
\]
namely
\[
  \zeta^0_M=u_{a,H_{1,0}}u_{b,H_{0,1}},
  \qquad [H_{1,0},H_{2,1}]=H_{2,0}.
\]
The resulting degree-\(\leq3\) table has eight nonzero faces after the
\(\rho_{1,1}\)-terms cancel.  Its \(\nu_3\)-row is the current
\(\mathsf E_{\theta_3,M}\), but the table does not yet prove a zero signed
Costello row sum.

## Attempted Table

With
\[
  E^M_{\Theta_3,\nu}:=-K^M_{\Theta_3}(\zeta_{M,\nu}),
\]
the candidate residual is
\[
\begin{aligned}
  R^{\mathrm{cand}}_{\Theta_3,M}
  ={}&2E_{\nu_{02}}-2E_{\nu_{20}}
      +3E_{\nu_{03}}+2E_{\nu_{12}^{(1)}}-E_{\nu_{12}^{(2)}}\\
    &+\mathsf E_{\theta_3,M}
      -2E_{\nu_{21}^{(2)}}-3E_{\nu_{30}} .
\end{aligned}
\]
The full table is recorded in
`reconstitution/theta3-companion-face-construction-attempt-2026-04-30.md`.

The candidate source-face transport is diagonal:
\[
  v^{M,N}_{\nu;\nu'}=
  \begin{cases}
    1,&\nu=\nu'\text{ and }d(\nu)\leq N,\\
    0,&\text{otherwise}.
  \end{cases}
\]
It satisfies the cocycle identity, but it does not preserve cancellation
unless the lower-window graph rows also cancel.  At \(N=2\) the projected
residual is \(2E_{\nu_{02}}-2E_{\nu_{20}}\), so a further identity
\(E_{\nu_{02}}=E_{\nu_{20}}\) or a different row presentation is required.

## Attacks

- The companion table is not a primitive counterterm.  It changes the
  degree-one residual.  A primitive counterterm would instead be a
  degree-zero row \(C_{\theta_3,M}\) with
  \(d_MC_{\theta_3,M}=-\mathsf E_{\theta_3,M}\).
- The table is source-algebraic only.  The actual current CE differential
  with \(a,b,B_\theta\) labels is not supplied for this \(\Theta_3\) seed.
- The graph weights
  \(K^M_{\Theta_3}(\zeta_{M,\nu})\) are not supplied for the seven
  companion faces, so no row-coordinate equality can be checked.
- The marked incidence signs and marker transports are not supplied.
  The source coefficients are not yet the full Costello boundary signs.
- The diagonal \(v\)-transport exposes a lower-window residual at \(N=2\);
  fixed-window cancellation would still need inverse-system compatibility.

## Exact Residual

The exact missing datum is the marked source-face computation for the
actual \(\Theta_3\) seed:
\[
  d_{\mathrm{CE}}\zeta_M,\quad
  \epsilon^{\mathrm{CE}}_{\Theta_3,\nu},\quad
  K^M_{\Theta_3}(\zeta_{M,\nu}),\quad
  \mu_\nu,\quad
  v^{M,N}_{\nu;\nu'}.
\]
The minimal computation is to evaluate the renormalized
\(\Theta_3\)-weight on every face of the table, express the results in one
degree-one row basis, then verify the signed zero sum and the \(v\)-cocycle
after projection.  Without that computation, the script's complete
companion-face case remains an interface fixture.  The current validator
also rejects cancelling coordinates unless they are derived from the CE
coefficients.

## Commands Run

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
        coeff=s; L=(r,s-1)
        if coeff and min(L)>=0 and sum(L)>0:
            terms.append(("du_z1",(r,s),L,(L,K2),coeff))
        coeff=-r; L=(r-1,s)
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
rg -n "[[:blank:]]$" reconstitution/theta3-companion-face-construction-attempt-2026-04-30.md \
  reconstitution/swarm-2026-04-30-agent-215-theta3-companion-face-construction-attempt.md || true
```

`py_compile`, JSON emission, the focused validator checks, and the
trailing-whitespace scan passed.

## Files Changed

- `reconstitution/theta3-companion-face-construction-attempt-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-215-theta3-companion-face-construction-attempt.md`
