# Agent 240 - Theta3 CE-Ancestor Counterterm Witness Construction Push

Status: report-only.  Files staged: this report and
`reconstitution/theta3-ce-ancestor-counterterm-witness-construction-push-2026-04-30.md`.
No TeX, script, figure, or manuscript file was edited.

## Claim Attacked

The attacked claim is that the order-three row
\[
  \mathsf E_{\theta_3,M}
    =-K^M_{\Theta_3}(\zeta_{M,\nu_3})
\]
can already be killed by one of the three accepted witnesses:

1. CE ancestor \(\eta_{\theta_3,M}\) with
   \(d_{\mathrm{CE}}\eta_{\theta_3,M}=\zeta_{M,\nu_3}\) and
   \(dK(\eta)=-\mathsf E_{\theta_3,M}\);
2. scalar-zero local counterterm
   \(C^{\mathrm{ct}}_{\theta_3,M}\) with
   \(dC^{\mathrm{ct}}=-\mathsf E_{\theta_3,M}\);
3. complete companion-face table with zero signed residual,
   codimension-two closure, source-face transport cocycle, and transported
   lower-window residual zero.

## Findings

The supplied one-row finite complex is
\[
  \mathcal K^0_{\theta_3,M}=0,\qquad
  \mathcal K^1_{\theta_3,M}=\mathbb C\mathsf E_{\theta_3,M},\qquad d=0.
\]
Therefore no local counterterm primitive exists inside the supplied complex.
The finite-row obstruction is exact:
\[
  r^M=(1),\qquad \ell_{\theta_3}(\mathsf E_{\theta_3,M})=1.
\]

The primitive gate is also exact.  Any future CE-ancestor or counterterm
payload must supply
\[
  A^M_{\theta_3,C}=-1,\qquad
  d_{\mathrm{ns},M}C_{\theta_3,M}=-\mathsf E_{\theta_3,M},
\]
plus scalar projection zero, \(T A=A P\), and zero Roos class.  With
identity/zero transport, \(c_M=1\) gives \([P^{M,N}c_M-c_N]=0\).

I tested the CE-ancestor route in the finite two-\(u\) source envelope of the
displayed row.  In the symmetric degree-\(\le3\) Hamiltonian source complex,
the pure \(\nu_3\) target is not a CE boundary.  A left-cokernel functional is
\[
  q
  =
  -\frac12\,e^*_{((H_{0,1},H_{0,1}),c_{\rho_{0,2}})}
  +e^*_{((H_{0,1},H_{2,0}),c_{\rho_{2,1}})},
\]
with \(q\,d_{\mathrm{CE}}=0\) and \(q(\nu_3)=1\).  Thus a CE ancestor must
enlarge the source habitat beyond this two-\(u\), degree-\(\le3\) envelope.

The existing eight-face companion candidate is not accepted.  Its residual is
\[
\begin{aligned}
  R^{\mathrm{cand}}_{\Theta_3,M}
    ={}&2E_{\nu_{02}}-2E_{\nu_{20}}+3E_{\nu_{03}}
        +2E_{\nu_{12}^{(1)}}-E_{\nu_{12}^{(2)}}\\
     &+\mathsf E_{\theta_3,M}
        -2E_{\nu_{21}^{(2)}}-3E_{\nu_{30}},
\end{aligned}
\]
and diagonal transport leaves
\[
  \pi_{M,2}R^{\mathrm{cand}}_{\Theta_3,M}
    =2E^2_{\nu_{02}}-2E^2_{\nu_{20}}.
\]
The missing companion datum is the marked Costello table
\[
  (d_{\mathrm{CE}}\zeta_M,\epsilon^{\mathrm{CE}}_{\Theta_3,\nu},
    K^M_{\Theta_3}(\zeta_{M,\nu}),\mu_\nu,
    v^{M,N}_{\nu;\nu'},\mathcal C^{(2)}_{\nu,\nu'})_{\nu,\nu'}.
\]

## Claim Status

Exact obstruction theorem for the current data.  The scalar-zero local
counterterm witness does not exist in the supplied one-row complex.  The
finite two-\(u\) source envelope does not contain a pure CE ancestor.  The
available eight-face companion table is an obstruction datum, not a
companion-face witness.

Supremum construction target: enlarge one of the three habitats and rerun the
same gates.  A valid positive theorem must supply either the degree-zero
column \(A_{\theta_3,C}=-1\), or a marked companion table with zero residual
and lower-window cancellation.

## Verification

Commands run:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py
python3 - <<'PY'
import json, subprocess
data=json.loads(subprocess.run(
    ['python3','scripts/finite_window_graph_array.py'],
    check=True,capture_output=True,text=True).stdout)
for row in data['finite_row_primitive_search_results']:
    if row['case'].startswith('theta'):
        print(row['case'], row['primitive_exists'],
              row['obstruction_value_on_residual'])
for row in data['theta_3_primitive_payload_checks']:
    print(row['case'], row['accepted'], row['differential_entry_value'])
check=data['theta_3_eight_face_candidate_obstruction_check']
print(check['accepted'], check['candidate_residual_vector'])
print(check['diagonal_v_transport']['n_2_residual_vector'])
PY
```

Additional source-level finite CE matrix probe:

```text
H basis degree <= 3
eta columns = 45
output rows = 310
q d_CE = 0
q(target) = 1
left covector support =
  -1/2 ((H_{0,1},H_{0,1}), c_{rho_{0,2}})
  +1   ((H_{0,1},H_{2,0}), c_{rho_{2,1}})
```

No PDF build was run because the assignment is report-only and the shared
checkout has active concurrent TeX/build edits outside the owned paths.
