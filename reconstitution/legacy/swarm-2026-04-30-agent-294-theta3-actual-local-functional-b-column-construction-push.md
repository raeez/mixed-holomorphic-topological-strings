# Agent 294 - Theta3 Actual Local-Functional B-Column Construction Push

Status: report-only. No TeX, script, figure, source, bibliography, PDF, or
build artifact was edited.

Owned reports:

- `reconstitution/theta3-actual-local-functional-b-column-construction-push-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-294-theta3-actual-local-functional-b-column-construction-push.md`

## Claim Attacked

Construct a genuine scalar-zero local functional
\[
  B^2_{02,20}\in\mathcal K^0_{\mathrm{ns},2}(I)
\]
with
\[
  d_{\mathrm{ns},2}B^2_{02,20}
  =
  -\mathfrak b^2_{02,20},
\qquad
  \widehat\sigma_{\mathrm{sc},2}(B^2_{02,20})=0,
\]
including locality or wavefront admissibility and finite-window transport.

This is the lower Bianchi-killing column needed after the source-coordinate
primitive
\[
  D^2_{02,20}=K^2_{\Theta_3}(u_{a,H_{1,0}}u_{b,H_{0,1}})
\]
exposes the Hom-valued Bianchi defect.

## Context Loaded

Governing files:

- `CLAUDE.md`
- `AGENTS.md`
- `~/ecosystem/INVARIANTS.md`
- `~/ecosystem/AGENTS-HARNESS.md`
- `.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`

Mathematical anchors:

- `reconstitution/theta3-no-counterterm-controlled-enlargement-integration-spec-2026-04-30.md`
- `main.tex:8370-8845`
- `theorem-lanes.tex:3288-3440`
- `appendix-factorization-current-conventions.tex:1-399`
- `appendix-factorization-current-conventions.tex:992-1905`
- `scripts/finite_window_graph_array.py:1-280`
- `scripts/finite_window_graph_array.py:1040-2045`
- `reconstitution/theta3-bianchi-counterterm-construction-push-2026-04-30.md`
- `reconstitution/nonscalar-costello-graph-qme-realization-next-construction-push-2026-04-30.md`

I also read `commands.tex`, `mathmacros.tex`, `notation.tex`, and
`preamble.tex` before writing.

## Construction Attempt

The source-coordinate calculation is fixed:
\[
  d_{\mathrm{CE}}\zeta^0_2
  =
  2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}},
  \qquad
  \zeta^0_2=u_{a,H_{1,0}}u_{b,H_{0,1}}.
\]
The local-functional differential is not the source differential transported
through \(K^2_{\Theta_3}\). It is
\[
  d_{\mathrm{ns},2}D^2_{02,20}
  =
  -2E^2_{\nu_{02}}+2E^2_{\nu_{20}}
  +\mathfrak b^2_{02,20}.
\]
Thus the available lower column has coordinates
\[
  A_D^2=(-2,2,1)^T
\]
in the basis
\[
  (E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20}).
\]

A counterterm extracted from the current degree-zero span would be a scalar
multiple \(xD^2_{02,20}\). The equation
\[
  x(-2,2,1)^T=(0,0,-1)^T
\]
has no solution. The first two coordinates force \(x=0\); the Bianchi
coordinate forces \(x=-1\).

I then tested whether the current local-functional habitats supply an
actual new column.

The coefficient-current kernel supplies only the algebraic current interface.
It does not build the small-diagonal graph extension or counterterm whose
differential could equal the Bianchi row.

The regular-density graph layer supplies Costello-local graph weights and
counterterms for fixed graphs with smooth compactly supported density labels.
It does not identify \(\mathfrak b^2_{02,20}\) as the boundary of a
degree-zero counterterm, does not give the row-coordinate map of such a
counterterm, and does not prove scalar-zero exactness.

The wavefront-admissible layer supplies the analytic class in which a
distributional counterterm could live. It requires a fixed graph, incidence
pullback, Hormander product criterion, finite scaling degree, local
extension across collision diagonals, and compatible counterterm choices.
None of those data are supplied for the lower Bianchi row. Arbitrary
\(\mathcal D'_c(I)\) labels are explicitly not available.

Therefore the actual local-functional construction is blocked before a new
boundary column can be tested.

## Exact Obstruction

The current finite-row lower habitat is
\[
  \mathcal H^0_{\mathrm{cur}}=\mathbb C D^2_{02,20},
\qquad
  \mathcal H^1_{\mathrm{cur}}
  =
  \mathbb C E^2_{\nu_{02}}
  \oplus
  \mathbb C E^2_{\nu_{20}}
  \oplus
  \mathbb C\mathfrak b^2_{02,20}.
\]
The only boundary column is
\[
  A_D^2=(-2,2,1)^T.
\]
The target for the B-column is
\[
  -\mathfrak b^2_{02,20}=(0,0,-1)^T.
\]

The cokernel functional
\[
  \widetilde\lambda_{02,\mathfrak b}
  =
  \frac12(E^2_{\nu_{02}})^*
  +(\mathfrak b^2_{02,20})^*
\]
satisfies
\[
  \widetilde\lambda_{02,\mathfrak b}A_D^2=0,
\qquad
  \widetilde\lambda_{02,\mathfrak b}((0,0,-1)^T)=-1.
\]
Hence the target is not in the image of the current differential.

This also detects the lower residual:
\[
  r_2=(2,-2,0)^T,\qquad
  \widetilde\lambda_{02,\mathfrak b}(r_2)=1.
\]
So \(D^2_{02,20}\) kills the transported lower residual only after the
Bianchi row is killed or after a genuinely new \(B\)-column is supplied.

## Roos Gate

A fixed-window \(B^2_{02,20}\) is not enough. For a tower \(B^M\), one must
prove
\[
  d_{\mathrm{ns},N}(\pi_{M,N}B^M-B^N)
  =
  -\pi_{M,N}\mathfrak b^M+\mathfrak b^N.
\]
If the right-hand side is nonzero, it must be killed by an explicit
transport correction \(H^{M,N}\), and then
\[
  [\pi_{M,N}B^M-B^N-H^{M,N}]
  =
  0
  \quad\text{in}\quad
  H^0(\mathcal K^\bullet_{\mathrm{ns},N}(I)).
\]
The current data contain no Bianchi-row transport identity, no correction
\(H^{M,N}\), and no zero Roos class. Diagonal transport of the eight-face
source-algebraic candidate leaves \(2E^2_{\nu_{02}}-2E^2_{\nu_{20}}\) at
\(N=2\).

## Claim Status

Blocked by an exact finite-window cokernel obstruction and by missing
actual local-functional habitat data.

The strongest true positive target is:

- add a marked graph/counterterm habitat containing a degree-zero local
  functional \(B^2_{02,20}\);
- prove its boundary column is \((0,0,-1)^T\);
- prove \(\widehat\sigma_{\mathrm{sc},2}(B^2_{02,20})=0\);
- prove regular-density or wavefront admissibility;
- prove compatible finite-window transport and zero Roos class.

Without these data, the formal column \(A_B^2=(0,0,-1)^T\) remains a matrix
target, not a Costello local functional.

## Verification Commands

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 - <<'PY'
from fractions import Fraction
import json, subprocess

data = json.loads(subprocess.run(
    ['python3', 'scripts/finite_window_graph_array.py'],
    check=True, capture_output=True, text=True,
).stdout)

for row in data['finite_row_primitive_search_results']:
    if row['case'].startswith('theta'):
        print(row['case'], row['primitive_exists'],
              row['obstruction_value_on_residual'], row['degree_zero_basis'])

for row in data['theta_3_primitive_payload_checks']:
    print(row['case'], row['supplied'], row['accepted'],
          row['differential_entry_value'], row['missing_fields'])

check = data['theta_3_eight_face_candidate_obstruction_check']
print(check['accepted'])
print(check['candidate_residual_coefficient_sum'])
print(check['diagonal_v_transport']['n_2_residual_vector'])

A_D = [Fraction(-2), Fraction(2), Fraction(1)]
r = [Fraction(2), Fraction(-2), Fraction(0)]
target = [Fraction(0), Fraction(0), Fraction(-1)]
ell = [Fraction(1,2), Fraction(0), Fraction(1)]
dot = lambda x,y: sum(a*b for a,b in zip(x,y))
print('ell_A_D=', dot(ell, A_D))
print('ell_r=', dot(ell, r))
print('ell_target=', dot(ell, target))
PY
```

Decisive output:

```text
theta_3_current_finite_row_subcomplex exists= False ell_r= 1 deg0= []
theta3_counterterm_without_differential_entry supplied= True accepted= False dC= 0 missing= ['differential entry dC=-E']
theta3_counterterm_supplied_exact_payload supplied= True accepted= True dC= -1 missing= []
eight_face_accepted= False
eight_face_coeff_sum= 0
eight_face_n2= [['E_nu02', '2'], ['E_nu20', '-2']]
ell_A_D= 0
ell_r= 1
ell_target= -1
```

## Files Changed

- `reconstitution/theta3-actual-local-functional-b-column-construction-push-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-294-theta3-actual-local-functional-b-column-construction-push.md`
