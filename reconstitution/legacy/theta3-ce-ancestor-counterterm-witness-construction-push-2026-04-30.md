# Theta3 CE-Ancestor And Counterterm Witness Construction Push

Status: report-only.  No TeX, script, figure, or source file was edited.
This note attacks the order-three `theta_3` row and records the strongest
construction theorem target still compatible with the current data.

## Stable Core

The active row is the full-equivariant order-three CE-source row
\[
  \theta_3=\mathrm{CE}(\Theta_3,\nu_3),\qquad |\Theta_3|_\hbar=3,
\]
with source-face convention
\[
  d_{\mathrm{CE}}\zeta_M=+\zeta_{M,\nu_3}+\cdots,
  \qquad
  \mathsf E_{\theta_3,M}
    =-K^M_{\Theta_3}(\zeta_{M,\nu_3}).
\]
The scalar gate is zero:
\[
  \widehat\sigma_{\mathrm{sc},M}(\mathsf E_{\theta_3,M})=0,
\]
and the supplied row closure is
\[
  d_{\mathrm{ns},M}\mathsf E_{\theta_3,M}=0.
\]

In the actual one-row finite complex,
\[
  \mathcal K^0_{\theta_3,M}=0,\qquad
  \mathcal K^1_{\theta_3,M}=\mathbb C\mathsf E_{\theta_3,M},\qquad
  d_{\theta_3,M}=0.
\]
Thus \(r^M=(1)\), the primitive-search matrix is \(1\times0\), and
\[
  \ell_{\theta_3}(\mathsf E_{\theta_3,M})=1,\qquad
  \ell_{\theta_3}d_{\theta_3,M}=0
\]
certifies
\[
  [\mathsf E_{\theta_3,M}]\ne0
  \quad\text{in}\quad
  H^1(\mathcal K^\bullet_{\theta_3,M}).
\]

This proves exact nonexistence of witness (2) inside the supplied row
complex: there is no scalar-zero Costello local counterterm
\[
  C^{\mathrm{ct}}_{\theta_3,M}\in\mathcal K^0_{\theta_3,M}
\]
because \(\mathcal K^0_{\theta_3,M}=0\).  It does not prove nonexistence in
the full local-functional complex.

## Primitive Gate

Any CE-ancestor or local-counterterm heal must add a degree-zero column
\[
  C_{\theta_3,M}\in\mathcal K^0_{\mathrm{ns},M}(I)
\]
with
\[
  A^M_{\theta_3,C}=-1,\qquad
  d_{\mathrm{ns},M}C_{\theta_3,M}=-\mathsf E_{\theta_3,M}.
\]
Then \(A^Mc=-r^M\) is solved by \(c_M=1\).  The scalar and tower gates are
\[
  \widehat\sigma_{\mathrm{sc},M}(C_{\theta_3,M})=0,
\]
\[
  \pi_{M,N}C_{\theta_3,M}=
  \begin{cases}
    C_{\theta_3,N},&N\ge3,\\
    0,&N<3,
  \end{cases}
\]
which give
\[
  T^{M,N}A^M=A^NP^{M,N},\qquad
  [P^{M,N}c_M-c_N]=0.
\]
For this identity/zero transport the Roos class is zero.  For any transport
\(\pi_{M,N}C_{\theta_3,M}=C_{\theta_3,N}+h_{M,N}\), the fixed-window row is
healed but the remaining tower obstruction is
\[
  [h_{M,N}]\in H^0(\mathcal K^\bullet_{\mathrm{ns},N}(I)).
\]

## CE-Ancestor Attack

Witness (1) would require a source element
\[
  \eta_{\theta_3,M},\qquad
  d_{\mathrm{CE}}\eta_{\theta_3,M}=\zeta_{M,\nu_3},
\]
and a Hom-valued Bianchi calculation proving
\[
  C^{\mathrm{CE}}_{\theta_3,M}
    =K^M_{\Theta_3}(\eta_{\theta_3,M})
    \in\mathcal K^0_{\mathrm{ns},M}(I),
  \qquad
  d_{\mathrm{ns},M}C^{\mathrm{CE}}_{\theta_3,M}
    =-\mathsf E_{\theta_3,M}.
\]

The existing companion attempt identifies the only obvious two-\(u\)
source monomial of the same external shape:
\[
  \zeta^0_M=u_{a,H_{1,0}}u_{b,H_{0,1}},\qquad
  [H_{1,0},H_{2,1}]=H_{2,0}.
\]
Its degree-\(\le3\) monomial CE differential does not isolate
\(\nu_3\).  It gives the eight-face candidate
\[
\begin{aligned}
  R^{\mathrm{cand}}_{\Theta_3,M}
    ={}&2E^M_{\nu_{02}}-2E^M_{\nu_{20}}
        +3E^M_{\nu_{03}}+2E^M_{\nu_{12}^{(1)}}
        -E^M_{\nu_{12}^{(2)}}\\
     &+\mathsf E_{\theta_3,M}
        -2E^M_{\nu_{21}^{(2)}}-3E^M_{\nu_{30}} .
\end{aligned}
\]
The coefficient sum is zero, but the row vector is not zero.

I pushed this one step further by solving the finite source-level CE
linear system in the two-\(u\), Hamiltonian-degree \(\le3\) envelope.  With
\[
  H_{a,b}=z_1^az_2^b,\qquad
  [H_{a,b},H_{r,s}]=(as-br)H_{a+r-1,b+s-1},
\]
and with constants removed, the target
\[
  ((H_{2,0},H_{0,1}),\,c_{\rho_{2,1}})
\]
is not in the image of the source differential.  In the symmetric
two-\(u\) presentation a left-cokernel functional is
\[
  q
  =
  -\frac12\,e^*_{((H_{0,1},H_{0,1}),\,c_{\rho_{0,2}})}
  +e^*_{((H_{0,1},H_{2,0}),\,c_{\rho_{2,1}})}.
\]
It satisfies \(q\,d_{\mathrm{CE}}=0\) and
\[
  q\bigl(((H_{2,0},H_{0,1}),c_{\rho_{2,1}})\bigr)=1.
\]
Thus no pure CE ancestor \(d_{\mathrm{CE}}\eta=\zeta_{M,\nu_3}\) exists in
this finite two-\(u\) source envelope.  In the ordered \(a,b\)-labelled
presentation the same target is also outside the image; one computed
left-cokernel functional has support
\[
  -\frac12\,e^*_{((H_{0,1},H_{0,1}),c_{\rho_{0,2}})}
  +\frac13\,e^*_{((H_{0,1},H_{0,2}),c_{\rho_{0,3}})}
  +e^*_{((H_{2,0},H_{0,1}),c_{\rho_{2,1}})}.
\]

This is not a universal no-go theorem for all CE sources.  It is an exact
source-level obstruction for the finite two-\(u\) envelope containing the
displayed \(\Theta_3\) row.  A CE-ancestor construction must therefore
leave this envelope: add higher source arity, add current-label dependent
terms, or supply a larger labelled CE complex in which the above cokernel
functional no longer exists.

## Companion-Face Attack

Witness (3) is not a primitive.  It replaces the one-face residual by a
complete signed CE-source-face sum.  The current eight-face candidate fails
the acceptance gate for three independent reasons:

1. Fixed-window residual is not zero in the declared row basis:
   \[
   R^{\mathrm{cand}}_{\Theta_3,M}\ne0
   \]
   with coordinates
   \[
   (2,-2,3,2,-1,1,-2,-3)
   \]
   on
   \[
   E_{\nu_{02}},E_{\nu_{20}},E_{\nu_{03}},E_{\nu_{12}^{(1)}},
   E_{\nu_{12}^{(2)}},E_{\theta_3},E_{\nu_{21}^{(2)}},E_{\nu_{30}}.
   \]
2. The diagonal source-face transport
   \[
     v^{M,N}_{\nu;\nu'}=
     \begin{cases}
       1,&\nu=\nu'\text{ and }d(\nu)\le N,\\
       0,&\text{otherwise}
     \end{cases}
   \]
   is a cocycle, but at \(N=2\) it leaves
   \[
     \pi_{M,2}R^{\mathrm{cand}}_{\Theta_3,M}
       =2E^2_{\nu_{02}}-2E^2_{\nu_{20}}.
   \]
   The missing lower-window identity is
   \[
     E^2_{\nu_{02}}=E^2_{\nu_{20}},
   \]
   or a recomputed lower-window row presentation.
3. The marked Costello incidence/weight table is absent.  The missing datum is
   \[
     \left(
       d_{\mathrm{CE}}\zeta_M,\,
       \epsilon^{\mathrm{CE}}_{\Theta_3,\nu},\,
       K^M_{\Theta_3}(\zeta_{M,\nu}),\,
       \mu_\nu,\,
       v^{M,N}_{\nu;\nu'},\,
       \mathcal C^{(2)}_{\nu,\nu'}
     \right)_{\nu,\nu'} .
   \]

Therefore the available eight-face table is an obstruction datum, not an
acceptable companion witness.

## Attack Ledger

```yaml
- id: A1-240-01
  severity: 1
  status: valid
  lens: finite-row linear algebra
  target: theta_3 one-row finite complex
  claim: The current row data contain a scalar-zero local counterterm primitive.
  broken_step: K^0_{theta_3,M}=0, so no degree-zero counterterm lives in the supplied complex.
  evidence_type: computation
  evidence_ref: "python3 scripts/finite_window_graph_array.py: theta_3_current_finite_row_subcomplex primitive_exists=false, obstruction_value_on_residual=1"
  minimal_heal: Supply a new degree-zero local functional C^{ct}_{theta_3,M} with dC=-E, scalar projection zero, T A=A P, and zero Roos class.
  residual: Existence in the full local-functional complex is open.

- id: A1-240-02
  severity: 1
  status: valid
  lens: source CE exactness
  target: CE ancestor eta_{theta3,M}
  claim: The finite two-u source envelope contains eta with d_CE eta=zeta_{M,nu3}.
  broken_step: The source-level CE matrix does not hit the pure nu_3 target.
  evidence_type: finite_linear_algebra
  evidence_ref: "left cokernel q=-1/2 e^*_{nu02}+e^*_{nu3}; q d_CE=0, q(nu3)=1"
  minimal_heal: Enlarge the source habitat beyond the two-u degree<=3 envelope and recompute the CE matrix.
  residual: Hom-valued Bianchi and Costello locality still must be supplied after any source ancestor is found.

- id: A1-240-03
  severity: 1
  status: valid
  lens: companion-face closure
  target: eight-face companion candidate
  claim: The eight-face source-algebraic table is an acceptable companion-face witness.
  broken_step: The residual vector is nonzero, diagonal transport leaves the N=2 residual, and the marked Costello incidence/weight table is absent.
  evidence_type: script_output
  evidence_ref: "theta_3_eight_face_candidate_obstruction_check accepted=false"
  minimal_heal: Compute K^M_{\Theta_3}(zeta_{M,nu}) for every face in one row basis, the marked signs, marker transports, codimension-two table, and lower-window cancellation.
  residual: A larger marked table may still cancel; the current one does not.
```

## Construction Theorem Target

The next theorem-grade positive result should be stated as follows.

**Theta3 witness construction theorem, target form.**  For every \(M\ge3\)
construct one of:

1. A CE ancestor in an enlarged labelled CE complex, escaping the two-\(u\)
   cokernel above, with
   \[
     d_{\mathrm{CE}}\eta_{\theta_3,M}=\zeta_{M,\nu_3},
     \quad
     d_{\mathbf K}K^M_{\Theta_3}(\eta_{\theta_3,M})=0,
   \]
   scalar-zero \(K^M_{\Theta_3}(\eta_{\theta_3,M})\), identity/zero transport,
   and zero Roos class.
2. A Costello local counterterm
   \[
     C^{\mathrm{ct}}_{\theta_3,M}
       =C^M_{\Theta_3,\nu_3,w}(\epsilon;B^\Theta_\bullet)
   \]
   with regular-density or wavefront-admissible locality, scalar projection
   zero, and
   \[
     d_{\mathrm{ns},M}C^{\mathrm{ct}}_{\theta_3,M}
       =-\mathsf E_{\theta_3,M}.
   \]
3. A complete companion-face table proving
   \[
     \sum_{\nu\in F_{\Theta_3,M}}
       \epsilon^{\mathrm{CE}}_{\Theta_3,\nu}E^M_{\Theta_3,\nu}=0
   \]
   in a common row basis, with scalar-zero faces, codimension-two closure,
   source-face transport cocycle, and transported residual zero in every lower
   window.

Failure of all three in a fixed enlarged habitat should be recorded as the
obstruction theorem
\[
  \left(
    [\mathsf E_{\theta_3,M}],\,
    q_{\mathrm{src}},\,
    R^{\mathrm{cand}}_{\Theta_3,M},\,
    2E^2_{\nu_{02}}-2E^2_{\nu_{20}},\,
    \mathcal C^{(2)}_{\mathrm{missing}}
  \right),
\]
where \(q_{\mathrm{src}}\) is the finite source-level left-cokernel
functional displayed above.

## Verification Commands

```bash
sed -n '1,240p' CLAUDE.md
sed -n '1,240p' AGENTS.md
sed -n '1,260p' /Users/raeez/ecosystem/skills/shared/attack-heal-swarm/protocol.md
sed -n '1,220p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
rg -n "theta_?3|Theta_?3|E_\\theta|E_theta|zeta|nu_?3|companion|Roos|counterterm|CE ancestor|ancestor|Costello|scalar-zero|finite-window|truncation" main.tex claim-strength-ledger.tex open-obligations.tex tate-P1-hadamard-mittag-leffler.tex theorem-lanes.tex commands.tex mathmacros.tex notation.tex
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py
```

Focused validator extraction:

```bash
python3 - <<'PY'
import json, subprocess
data=json.loads(subprocess.run(
    ['python3','scripts/finite_window_graph_array.py'],
    check=True,capture_output=True,text=True).stdout)
print(data['theta_3_common_finite_window_record']['row_value'])
for row in data['finite_row_primitive_search_results']:
    if row['case'].startswith('theta'):
        print(row['case'], row['primitive_exists'],
              row['obstruction_value_on_residual'],
              row['primitive_coefficients'], row['obstruction_covector'])
for row in data['theta_3_primitive_payload_checks']:
    print(row['case'], row['accepted'], row['differential_entry_value'],
          row['missing_fields'])
check=data['theta_3_eight_face_candidate_obstruction_check']
print(check['accepted'], check['candidate_residual_vector'])
print(check['diagonal_v_transport']['n_2_residual_vector'])
PY
```

Source-level CE exactness probe:

```bash
python3 - <<'PY'
from fractions import Fraction
from itertools import combinations_with_replacement

def deg(x): return x[0]+x[1]
def basis(M):
    return [(a,b) for a in range(M+1) for b in range(M+1-a) if a+b>0]
def br(A,J):
    a,b=A; r,s=J
    c=a*s-b*r
    L=(a+r-1,b+s-1)
    if c==0 or L[0]<0 or L[1]<0 or deg(L)==0:
        return None
    return c,L
def pair(A,B): return tuple(sorted((A,B)))

M=3
H=basis(M)
eta_basis=list(combinations_with_replacement(H,2))
out=[]; idx={}
def add(P,J):
    key=(P,J)
    if key not in idx:
        idx[key]=len(out); out.append(key)
for A,B in eta_basis:
    for J in H:
        for X,Y in [(A,B),(B,A)]:
            v=br(X,J)
            if v:
                c,L=v
                if deg(L)<=M:
                    add(pair(L,Y),J)
rows=len(out); cols=len(eta_basis)
mat=[[Fraction(0) for _ in range(cols)] for __ in range(rows)]
for col,(A,B) in enumerate(eta_basis):
    for J in H:
        for X,Y in [(A,B),(B,A)]:
            v=br(X,J)
            if v:
                c,L=v
                if deg(L)<=M:
                    mat[idx[(pair(L,Y),J)]][col]+=Fraction(c)
target=(pair((2,0),(0,1)),(2,1))
nu02=(pair((0,1),(0,1)),(0,2))
q=[Fraction(0) for _ in range(rows)]
q[idx[nu02]]=Fraction(-1,2)
q[idx[target]]=Fraction(1)
assert all(sum(q[i]*mat[i][j] for i in range(rows))==0 for j in range(cols))
assert q[idx[target]]==1
print('eta cols',cols,'out rows',rows,'target index',idx[target])
print('left covector verifies q d_CE = 0 and q(target)=1')
print('support: -1/2*((0,1),(0,1);(0,2)) + 1*((0,1),(2,0);(2,1))')
PY
```

Observed decisive outputs:

```text
theta_3_current_finite_row_subcomplex primitive_exists=false obstruction_value_on_residual=1
theta3_ce_ancestor_without_differential_entry accepted=false differential_entry_value=0
theta3_ce_ancestor_supplied_exact_payload accepted=true differential_entry_value=-1
theta3_counterterm_without_differential_entry accepted=false differential_entry_value=0
theta3_counterterm_supplied_exact_payload accepted=true differential_entry_value=-1
theta3_eight_face_candidate_source_algebraic_obstruction accepted=false
N=2 residual [['E_nu02', '2'], ['E_nu20', '-2']]
source CE probe: eta cols 45, out rows 310; target outside image by displayed left covector
```
