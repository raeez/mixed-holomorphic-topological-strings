# Agent 282 - Theta3 Bianchi Counterterm Construction Push

Status: report-only. Files staged by this agent:

- `reconstitution/theta3-bianchi-counterterm-construction-push-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-282-theta3-bianchi-counterterm-construction-push.md`

No manuscript TeX, script, figure, source fixture, bibliography, PDF, or build
artifact was edited.

## Claim Attacked

The attacked claim is the strongest available lower-window theta3 repair:
construct a scalar-zero local counterterm
\[
  B^2_{02,20}
\]
such that
\[
  d_{\mathrm{ns},2}B^2_{02,20}
  =
  -\mathfrak b^2_{02,20},
\]
where
\[
  \mathfrak b^2_{02,20}
  =
  d_{\mathrm{ns},2}K^2_{\Theta_3}(\zeta^0_2)
  -
  K^2_{\Theta_3}(d_{\mathrm{CE}}\zeta^0_2),
  \qquad
  \zeta^0_2=u_{a,H_{1,0}}u_{b,H_{0,1}}.
\]
This is the exact datum that would turn the source-coordinate primitive
\[
  D^2_{02,20}=K^2_{\Theta_3}(\zeta^0_2)
\]
into a genuine local-functional lower primitive.

## Context Loaded

Governing files:

- `CLAUDE.md`
- `AGENTS.md`
- `~/ecosystem/INVARIANTS.md`
- `~/ecosystem/AGENTS-HARNESS.md`
- `.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`

Mathematical anchors:

- `main.tex:8332-8550`: theta3 finite-window acceptance gate and current
  Bianchi-exposed matrix language.
- `theorem-lanes.tex:3260-3411`: theorem-lane theta3 obstruction and lower
  primitive gate.
- `open-obligations.tex:715-852`: open theta3 repair obligations.
- `claim-strength-ledger.tex:459-493`, `:818-868`: claim-strength entries
  for theta3 and Costello graph/QME.
- `tate-P1-hadamard-mittag-leffler.tex:400-680`: finite-window graph/QME
  package and local-functional subcomplex.
- `tate-P1-hadamard-mittag-leffler.tex:1816-1875`: finite-row primitive
  search interface.
- `tate-P1-hadamard-mittag-leffler.tex:2226-2368`: theta3 companion-face
  obstruction.
- `tate-P1-hadamard-mittag-leffler.tex:2370-2550`: actual finite-window
  non-scalar decision datum.
- `scripts/finite_window_graph_array.py:1000-1620`: theta3 common record,
  primitive payload gates, eight-face table, and marked Costello table
  obstruction.
- Recent reports by Agents 240, 245, 263, 270, and 277.

Source boundary:

- `references/primary-sources/local-costello-bv-kernel-source-anchors-2026-04-30.md`
  supports the general Costello local-functional/counterterm vocabulary, but
  not an automatic current-valued target, distributional defect-current
  theorem, or bulk-to-defect kernel.

## Construction Attempt

The source-coordinate calculation is stable. In the degree-two source window,
\[
  d_{\mathrm{CE}}\zeta^0_2
  =
  2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}}.
\]
With \(E_\nu=-K_{\Theta_3}(\zeta_\nu)\),
\[
  d_{\mathrm{ns},2}D^2_{02,20}
  =
  -2E^2_{\nu_{02}}+2E^2_{\nu_{20}}
  +\mathfrak b^2_{02,20}.
\]
Thus \(D^2_{02,20}\) would kill the transported lower residual only after
the Bianchi row is killed.

I then granted the strongest current lower habitat: keep \(D^2_{02,20}\) as
a degree-zero column and expose \(\mathfrak b^2_{02,20}\) as a third
degree-one row. The ordered lower row basis is
\[
  (E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20}),
\]
and the available column is
\[
  A_D^2=(-2,2,1)^T.
\]
A counterterm \(B^2_{02,20}\) made from the current degree-zero span would
have the form \(xD^2_{02,20}\). The equation
\[
  d_{\mathrm{ns},2}(xD^2_{02,20})=-\mathfrak b^2_{02,20}
\]
is
\[
  x(-2,2,1)^T=(0,0,-1)^T.
\]
The \(E^2_{\nu_{02}}\) and \(E^2_{\nu_{20}}\) coordinates force \(x=0\);
the Bianchi coordinate forces \(x=-1\). Hence no such \(B^2_{02,20}\)
exists in this habitat.

## Exact Obstruction

The cokernel
\[
  \widetilde\lambda_{02,\mathfrak b}
  =
  \frac12(E^2_{\nu_{02}})^*
  +(\mathfrak b^2_{02,20})^*
\]
annihilates the entire current lower boundary image:
\[
  \widetilde\lambda_{02,\mathfrak b}A_D^2=0.
\]
It does not annihilate the desired Bianchi target:
\[
  \widetilde\lambda_{02,\mathfrak b}(-\mathfrak b^2_{02,20})=-1.
\]
Thus \(\mathfrak b^2_{02,20}\) is non-exact in the current
Bianchi-exposed lower row complex. This is a fixed-window cohomology
obstruction, not a notation gap.

The same functional detects the residual obstruction:
\[
  \widetilde\lambda_{02,\mathfrak b}(2E^2_{\nu_{02}}-2E^2_{\nu_{20}})=1.
\]
Consequently the equations
\[
  A_D^2c=-r_2,\qquad A_D^2c=(0,0,-1)^T
\]
fail for the same reason: the Bianchi row is not in the current boundary
image.

## Scalar-Zero And Locality Gates

The scalar-zero requirement does not repair the matrix failure. It is an
additional positive datum. A future \(B^2_{02,20}\) must supply all four
entries:

1. a local-functional formula in \(\mathcal K^0_{\mathrm{ns},2}(I)\);
2. boundary column \(A_B^2=(0,0,-1)^T\);
3. scalar projection
   \(\widehat\sigma_{\mathrm{sc},2}(B^2_{02,20})=0\);
4. regular-density or wavefront-admissible locality and finite-window
   transport.

The current checkout supplies none of these for \(B^2_{02,20}\). The
validator's accepted `theta3_counterterm_supplied_exact_payload` is an
interface fixture for a different target, \(dC_{\theta_3}=-E_{\theta_3}\);
it is not present as current data and does not provide a boundary
\(-\mathfrak b^2_{02,20}\).

## Tower Obstruction

Even if a fixed-window \(B^2_{02,20}\) were supplied, a theorem-grade
finite-window tower would require
\[
  d_{\mathrm{ns},N}(\pi_{M,N}B^M-B^N)
  =
  -\pi_{M,N}\mathfrak b^M+\mathfrak b^N.
\]
Thus the Bianchi defects must transport strictly, or the displayed
right-hand side must be a supplied boundary. The current graph-array data do
not contain this Bianchi-transport homotopy.

## Claim Status

Exact obstruction in the current finite-window/local-functional habitat.

The strongest true positive statement is:

- If a new scalar-zero local counterterm column
  \(A_B^2=(0,0,-1)^T\) is supplied, then \(D^2_{02,20}+B^2_{02,20}\) kills
  the \(N=2\) lower residual.
- If these columns and Bianchi rows also satisfy the tower transport identity
  with zero Roos class, then the lower primitive is compatible.
- These are missing data. They are not consequences of source exactness or
  the Hom-valued Bianchi identity alone.

This does not prove a universal no-go in the full Costello complex. It proves
that the current finite-row package contains no \(B^2_{02,20}\).

## Verification Commands

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 - <<'PY'
from fractions import Fraction
import json, subprocess

data = json.loads(subprocess.run(
    ['python3','scripts/finite_window_graph_array.py'],
    check=True, capture_output=True, text=True
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
print(check['diagonal_v_transport']['n_2_residual_vector'])

A_D = [Fraction(-2), Fraction(2), Fraction(1)]
r = [Fraction(2), Fraction(-2), Fraction(0)]
b_target = [Fraction(0), Fraction(0), Fraction(-1)]
ell = [Fraction(1,2), Fraction(0), Fraction(1)]
dot = lambda x,y: sum(a*b for a,b in zip(x,y))
print(dot(ell, A_D), dot(ell, r), dot(ell, b_target))
PY
python3 - <<'PY'
# source-coordinate CE differential scan for zeta^0_2, M=2..10
PY
```

Decisive output:

```text
theta_3_current_finite_row_subcomplex exists=False ell_r=1 deg0=[]
theta3_counterterm_without_differential_entry accepted=False dC=0
theta3_counterterm_supplied_exact_payload accepted=True dC=-1
eight_face_accepted False
n2_residual [['E_nu02', '2'], ['E_nu20', '-2']]
bianchi_A_D ['-2', '2', '1']
target_-b ['0', '0', '-1']
ell_A_D 0
ell_r 1
ell_target_-b -1
kill_residual coordinate_forced_values ['1', '1', '0']
kill_bianchi coordinate_forced_values ['0', '0', '-1']
M 2 nu02 2 nu20 -2 terms 2
M 3 nu02 2 nu20 -2 terms 8
M 10 nu02 2 nu20 -2 terms 106
```
