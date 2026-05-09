# Theta3 Marked-Source/Hom-Companion Repair Push

## Claim attacked

The attacked claim is that the all-degree ordinary pure two-u obstruction
to the first \(\theta_3\) row can be healed by one of the named routes using
only the data now present in the finite-window theta3 package:

1. a scalar-zero local counterterm column
   \(A^M_{\theta_3,C}=-1\) with zero Roos class;
2. a marked source generator outside the ordinary pure two-u algebra whose
   boundary column has \(q_{2u}\)-value \(1\), with codimension-two closure,
   Hom-valued Bianchi cancellation, scalar-zero value, and compatible
   transport;
3. a marked companion relation
   \(R^{\mathrm{cand}}_{\Theta_3,M}=0\) whose lower-window transport kills
   \(2E^2_{\nu_{02}}-2E^2_{\nu_{20}}\).

## Construction attempted

I tested the largest data-derived enlargement supported by the checkout:

* all ordinary pure two-u CE columns in every finite Hamiltonian degree;
* the Agent 215/221 eight-face source-algebraic companion column;
* the diagonal source-face transport recorded in the validator;
* the current scalar-zero primitive payload slots checked by
  `scripts/finite_window_graph_array.py`.

This habitat deliberately excludes a tautological new symbol
\(\eta\) with \(d\eta=\zeta_{M,\nu_3}\) unless the new symbol also carries
the codimension-two source table and the Hom-valued Bianchi calculation.
At the linear level such a formal column has \(q_{2u}\)-value \(1\), but
without the closure and Bianchi data it is exactly the missing theorem
datum, not a construction.

## Exact formulas/rows

Let \(H_{a,b}=z_1^a z_2^b\).  The Hamiltonian bracket is
\[
  [H_{a,b},H_{r,s}]
  =(as-br)H_{a+r-1,b+s-1},
\]
with invalid or constant terms discarded.  In finite Hamiltonian degree
\(\le D\), the ordinary pure two-u source columns are
\[
  u_Au_B,\qquad A,B\in\{H_{a,b}:0<a+b\le D\},
\]
and their CE boundary has rows
\[
  d_{\mathrm{CE}}(u_Au_B)
  =
  \sum_J\bigl(u_{[A,J]}u_B+u_Au_{[B,J]}\bigr)c_{\rho_J}.
\]

The all-degree left-cokernel functional is
\[
  q_{2u}
  =
  e^*_{((H_{0,1},H_{2,0}),c_{\rho_{2,1}})}
  -\frac12 e^*_{((H_{0,1},H_{0,1}),c_{\rho_{0,2}})}.
\]
Only the column \(u_{H_{1,0}}u_{H_{0,1}}\) can hit the support of \(q_{2u}\).
For that column,
\[
  [H_{1,0},H_{2,1}]=H_{2,0},\qquad
  [H_{1,0},H_{0,2}]=2H_{0,1}.
\]
Hence
\[
  q_{2u}d_{\mathrm{CE}}(u_{H_{1,0}}u_{H_{0,1}})
  =1-\frac12\cdot 2=0,
\]
and every other ordinary pure two-u column has \(q_{2u}\)-value \(0\).
Therefore \(q_{2u}d_{\mathrm{CE}}=0\) in every finite degree, while
\[
  q_{2u}(\zeta_{M,\nu_3})=1.
\]

The current fixed-window theta3 row complex remains
\[
  \mathcal Q^0_{\theta_3,M}=0,\qquad
  \mathcal Q^1_{\theta_3,M}=\mathbb C E_{\theta_3,M},\qquad
  d_M=0,
\]
with residual \(r_M=E_{\theta_3,M}\) and
\[
  \ell_{\theta_3}(E_{\theta_3,M})=1.
\]
Thus a scalar-zero primitive must supply the new degree-zero column
\[
  A^M_{\theta_3,C}=-1,\qquad
  d_MC_{\theta_3,M}=-E_{\theta_3,M}.
\]
The validator accepts this only for the guarded supplied-exact payloads.
Those payloads are interface fixtures; no local functional formula or CE
ancestor is present in the current data.

The eight-face companion candidate has row vector
\[
\begin{aligned}
  R^{\mathrm{cand}}_{\Theta_3,M}
  ={}&2E_{\nu_{02}}-2E_{\nu_{20}}+3E_{\nu_{03}}
      +2E_{\nu_{12}^{(1)}}-E_{\nu_{12}^{(2)}}\\
   &+E_{\theta_3}-2E_{\nu_{21}^{(2)}}-3E_{\nu_{30}}.
\end{aligned}
\]
On the \(q_{2u}\)-support it gives
\[
  q_{2u}(R^{\mathrm{cand}}_{\Theta_3,M})
  =1-\frac12\cdot 2=0,
\]
so it cannot serve as the marked source column with \(q_{2u}\)-value \(1\).
Under diagonal source-face transport to \(N=2\),
\[
  v^{M,2}R^{\mathrm{cand}}_{\Theta_3,M}
  =2E^2_{\nu_{02}}-2E^2_{\nu_{20}}.
\]
In the lower free row presentation
\[
  \mathcal R^1_2=\mathbb C E^2_{\nu_{02}}\oplus
  \mathbb C E^2_{\nu_{20}},
\]
the normalized cokernel functional
\[
  \lambda^{(2)}_{\nu_{02}}=\frac12(E^2_{\nu_{02}})^*
\]
has
\[
  \lambda^{(2)}_{\nu_{02}}
  (2E^2_{\nu_{02}}-2E^2_{\nu_{20}})=1.
\]
Thus the diagonal lower-window companion route is blocked unless a new
relation \(E^2_{\nu_{02}}=E^2_{\nu_{20}}\), a lower primitive, or a
recomputed non-diagonal transport matrix is supplied.

## Verification commands

Validator extraction:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 - <<'PY'
import json, subprocess
payload=json.loads(subprocess.run(
    ['python3','scripts/finite_window_graph_array.py'],
    check=True,capture_output=True,text=True).stdout)
for row in payload['finite_row_primitive_search_results']:
    if row['case'].startswith('theta'):
        print(row['case'], row['primitive_exists'],
              row['obstruction_value_on_residual'],
              row['obstruction_covector'])
for row in payload['theta_3_primitive_payload_checks']:
    print(row['case'], row['accepted'],
          row['differential_entry_value'], row['missing_fields'])
for row in payload['theta_3_companion_face_payload_checks']:
    if row['case'].startswith('theta3_eight') or row['case'].startswith('theta3_complete'):
        print(row['case'], row['accepted'],
              row['residual_vector'], row['missing_fields'])
check=payload['theta_3_eight_face_candidate_obstruction_check']
print(check['accepted'])
print(check['candidate_residual_vector'])
print(check['diagonal_v_transport']['n_2_residual_vector'])
print(check['marked_costello_table']['codimension_two_closure_supplied'])
PY
```

Decisive output:

```text
theta_3_current_finite_row_subcomplex False 1 [['E_theta_3', '1']]
theta3_ce_ancestor_without_differential_entry False 0 ['differential entry dC=-E']
theta3_ce_ancestor_supplied_exact_payload True -1 []
theta3_counterterm_without_differential_entry False 0 ['differential entry dC=-E']
theta3_counterterm_supplied_exact_payload True -1 []
theta3_eight_face_candidate_source_algebraic_obstruction False
  [['E_nu02', '2'], ['E_nu20', '-2'], ['E_nu03', '3'],
   ['E_nu12_1', '2'], ['E_nu12_2', '-1'], ['E_theta_3', '1'],
   ['E_nu21_2', '-2'], ['E_nu30', '-3']]
  ['zero signed residual sum', 'codimension-two closure table',
   'marked Costello incidence/weight table',
   'transported lower-window residual zero']
eight accepted=False
eight N2=[['E_nu02', '2'], ['E_nu20', '-2']]
marked table supplied=False
```

Finite scans supporting the all-degree support proof:

```bash
python3 -u - <<'PY'
from fractions import Fraction
from itertools import combinations_with_replacement

def deg(x): return x[0]+x[1]
def basis(D): return [(a,b) for a in range(D+1)
                     for b in range(D+1-a) if a+b>0]
def br(A,J):
    a,b=A; r,s=J
    c=a*s-b*r
    L=(a+r-1,b+s-1)
    if c==0 or L[0]<0 or L[1]<0 or deg(L)==0:
        return None
    return c,L
def pair(A,B): return tuple(sorted((A,B)))

target=(pair((2,0),(0,1)),(2,1))
nu02=(pair((0,1),(0,1)),(0,2))
for D in range(3,9):
    H=basis(D)
    bad=[]; support=[]
    for A,B in combinations_with_replacement(H,2):
        qval=Fraction(0); hits=[]
        for J in H:
            for X,Y in ((A,B),(B,A)):
                v=br(X,J)
                if not v: continue
                c,L=v
                if deg(L)>D: continue
                key=(pair(L,Y),J)
                if key == target:
                    qval += Fraction(c); hits.append(('target', c))
                if key == nu02:
                    qval -= Fraction(c,2); hits.append(('nu02', c))
        if qval: bad.append(((A,B),qval,hits))
        if hits: support.append(((A,B),qval,hits))
    print('D=',D,'qD_zero=',not bad,'support=',support)
    if bad:
        raise SystemExit(1)
print('finite scan supports the symbolic qD=0 calculation through D=8')
PY
```

Observed output:

```text
D= 3 qD_zero= True support= [(((0, 1), (1, 0)), Fraction(0, 1), [('nu02', 2), ('target', 1)])]
D= 4 qD_zero= True support= [(((0, 1), (1, 0)), Fraction(0, 1), [('nu02', 2), ('target', 1)])]
D= 5 qD_zero= True support= [(((0, 1), (1, 0)), Fraction(0, 1), [('nu02', 2), ('target', 1)])]
D= 6 qD_zero= True support= [(((0, 1), (1, 0)), Fraction(0, 1), [('nu02', 2), ('target', 1)])]
D= 7 qD_zero= True support= [(((0, 1), (1, 0)), Fraction(0, 1), [('nu02', 2), ('target', 1)])]
D= 8 qD_zero= True support= [(((0, 1), (1, 0)), Fraction(0, 1), [('nu02', 2), ('target', 1)])]
finite scan supports the symbolic qD=0 calculation through D=8
```

Eight-face and lower-window obstruction check:

```bash
python3 - <<'PY'
from fractions import Fraction
eight = {
    'E_nu02': Fraction(2), 'E_nu20': Fraction(-2),
    'E_nu03': Fraction(3), 'E_nu12_1': Fraction(2),
    'E_nu12_2': Fraction(-1), 'E_theta_3': Fraction(1),
    'E_nu21_2': Fraction(-2), 'E_nu30': Fraction(-3),
}
print('q2u(eight_face_candidate)=',
      eight['E_theta_3'] - Fraction(1,2)*eight['E_nu02'])
print('N2_residual=', [('E_nu02', eight['E_nu02']),
                       ('E_nu20', eight['E_nu20'])])
print('lambda_N2=1/2*E_nu02^* gives',
      Fraction(1,2)*eight['E_nu02'])
print('q2u(formal_theta_column)=', Fraction(1))
PY
```

Output:

```text
q2u(eight_face_candidate)= 0
N2_residual= [('E_nu02', Fraction(2, 1)), ('E_nu20', Fraction(-2, 1))]
lambda_N2=1/2*E_nu02^* gives 1
q2u(formal_theta_column)= 1
```

Two larger exploratory scans were stopped because they materialized or
streamed more of the CE matrix than was needed.  They produced no evidence
used in the claim.

## Whether a real repair was constructed

No real repair was constructed in the data-derived habitat.

The script confirms the exact shape of a repair: a supplied CE ancestor or
counterterm payload with differential entry \(-1\), scalar zero, transport
identity, and zero Roos class would pass the finite gate.  The current
checkout does not contain the actual source ancestor, local counterterm
functional, marked Costello incidence/weight table, codimension-two table,
or lower-window transport cancellation.

## Exact obstruction theorem

Define the data-derived theta3 enlargement
\(\mathcal H^{\mathrm{der}}_{\theta_3,M}\) as follows.

1. Its source columns are all ordinary pure two-u CE columns
   \(d_{\mathrm{CE}}(u_Au_B)\) in finite Hamiltonian degree, together with
   linear combinations of the eight source-algebraic faces recorded for the
   Agent 215/221 companion candidate.
2. Its theta3 primitive sector is the current scalar-zero finite row
   package checked by `finite_window_graph_array.py`; a named primitive with
   no differential entry is a zero column.
3. Its companion transport is the recorded diagonal source-face transport
   \(v^{M,N}_{\nu;\nu'}=1\) for \(\nu=\nu'\) and \(\deg\nu\le N\), and
   \(0\) otherwise.
4. No additional Costello local functional, marked incidence/weight table,
   codimension-two table, lower-window relation, or non-diagonal transport
   is adjoined.

Then all three repair routes are blocked inside
\(\mathcal H^{\mathrm{der}}_{\theta_3,M}\):

* counterterm route: the cokernel \(\ell_{\theta_3}\) has
  \(\ell_{\theta_3}d_M=0\) and \(\ell_{\theta_3}(E_{\theta_3,M})=1\);
  there is no column \(A^M_{\theta_3,C}=-1\);
* marked-source route: \(q_{2u}\) kills every ordinary pure two-u source
  boundary and the eight-face source-algebraic column, while
  \(q_{2u}(\zeta_{M,\nu_3})=1\);
* companion route: the lower-window cokernel
  \(\lambda^{(2)}_{\nu_{02}}=\frac12(E^2_{\nu_{02}})^*\) evaluates to
  \(1\) on \(v^{M,2}R^{\mathrm{cand}}_{\Theta_3,M}\).

This theorem does not rule out a genuinely new marked cone with its own
codimension-two closure and Hom-valued Bianchi table, nor a genuine
scalar-zero local counterterm formula.  Those are exactly the missing
objects.

## TeX-ready insertion draft

The following obstruction statement is justified for the data-derived
habitat above only.

```tex
\begin{prop}[Data-derived obstruction for the \(\theta_3\) repair routes]
  Fix \(M\ge 3\).  Let
  \(\mathcal H^{\mathrm{der}}_{\theta_3,M}\) be the enlargement generated by
  the ordinary pure two-\(u\) CE source columns in all finite Hamiltonian
  degrees, the eight source-algebraic faces of the tested companion
  candidate, the current scalar-zero theta-row primitive slots, and the
  diagonal source-face transport.  No new Costello local functional,
  marked incidence/weight table, codimension-two table, lower-window
  relation, or non-diagonal transport is adjoined.

  In this habitat the first \(\theta_3\) row is not killed.  The
  counterterm route is obstructed by
  \(\ell_{\theta_3}(E_{\theta_3,M})=1\).  The marked-source route is
  obstructed by
  \[
    q_{2u}
    =
    e^*_{((H_{0,1},H_{2,0}),c_{\rho_{2,1}})}
    -\frac12e^*_{((H_{0,1},H_{0,1}),c_{\rho_{0,2}})},
  \]
  since \(q_{2u}d_{\mathrm{CE}}=0\) on every ordinary pure two-\(u\)
  column and \(q_{2u}(\zeta_{M,\nu_3})=1\).  The tested companion route is
  obstructed after diagonal transport to \(N=2\), where
  \[
    v^{M,2}R^{\mathrm{cand}}_{\Theta_3,M}
      =2E^2_{\nu_{02}}-2E^2_{\nu_{20}},
    \qquad
    \frac12(E^2_{\nu_{02}})^*
    (v^{M,2}R^{\mathrm{cand}}_{\Theta_3,M})=1.
  \]
  Thus a repair must adjoin data outside
  \(\mathcal H^{\mathrm{der}}_{\theta_3,M}\): either a scalar-zero local
  counterterm column \(A^M_{\theta_3,C}=-1\) with zero Roos class, a marked
  source generator with a \(q_{2u}\)-visible boundary and a closed
  codimension-two/Hom-valued Bianchi table, or a companion relation with
  lower-window transport killing
  \(2E^2_{\nu_{02}}-2E^2_{\nu_{20}}\).
\end{prop}
```

## Files changed

* `reconstitution/theta3-marked-source-hom-companion-repair-push-2026-04-30.md`
* `reconstitution/swarm-2026-04-30-agent-257-theta3-marked-source-hom-companion-repair-push.md`

No manuscript, theorem-lane, script, figure, build artifact, or proof file
was edited.  No PDF build was run.
