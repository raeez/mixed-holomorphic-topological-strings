# Theta3 Bianchi Defect Closure Push

Status: report-only.  No TeX, script, figure, source fixture, build artifact,
or bibliography file was edited.  No PDF build was run.

Companion synthesis:

- `reconstitution/theta3-bianchi-defect-closure-push-2026-04-30.md`

## Claim Attacked

The attacked claim is that the current theta3 data already contain enough
structure to close the lower-window companion residual by the source-coordinate
primitive
\[
  D^2_{02,20}
  =
  K^2_{\Theta_3}(u_{a,H_{1,0}}u_{b,H_{0,1}}),
  \qquad H_{p,q}=z_1^p z_2^q .
\]

The target was stronger than a restatement of the existing obstruction.  I
tried to construct one of:

1. the Hom-valued Bianchi identity making \(D^2_{02,20}\) a genuine
   local-functional primitive;
2. a local counterterm killing the Bianchi defect;
3. a compatible transport matrix killing the \(N=2\) residual;
4. an exact obstruction row or matrix equation blocking these routes.

## Anchors Read

- `main.tex:8295-8476`: finite-window acceptance gate for the first
  \(\theta_3\) row.
- `theorem-lanes.tex:3260-3383`: theorem-lane integration of the theta3
  one-row obstruction, \(q_{2u}\), eight-face residual, and lower primitive
  candidate.
- `open-obligations.tex:706-823`: current proof ledger for the three healing
  routes and the lower-window primitive candidate.
- `tate-P1-hadamard-mittag-leffler.tex:1816-2369`: finite-row primitive
  search interface, theta3 row certificate, payload gate, and companion-face
  obstruction theorem.
- `scripts/finite_window_graph_array.py:1043-1561`: theta3 common record,
  primitive payload gates, eight-face candidate, diagonal transport, and
  marked Costello table obstruction.
- Recent theta3 reports:
  `finite-window-theta3-companion-primitive-search-2026-04-30.md`,
  `theta3-source-to-construction-spec-2026-04-30.md`,
  `theta3-ce-ancestor-counterterm-witness-construction-push-2026-04-30.md`,
  `theta3-marked-source-hom-companion-repair-push-2026-04-30.md`,
  `theta3-nondiagonal-transport-counterterm-construction-push-2026-04-30.md`,
  and `theta3-acceptance-gate-consistency-2026-04-30.md`.

## Stable Row Data

The supplied one-row theta3 complex is
\[
  \mathcal K^0_{\theta_3,M}=0,\qquad
  \mathcal K^1_{\theta_3,M}=\mathbb C\mathsf E_{\theta_3,M},\qquad
  d_{\theta_3,M}=0,
\]
with
\[
  \mathsf E_{\theta_3,M}=-K^M_{\Theta_3}(\zeta_{M,\nu_3}),\qquad
  \widehat\sigma_{\mathrm{sc},M}(\mathsf E_{\theta_3,M})=0,\qquad
  \ell_{\theta_3}(\mathsf E_{\theta_3,M})=1.
\]
Thus the current fixed-window obstruction remains real:
\[
  A_{\mathrm{cur}}^M\colon 0\to\mathbb C\mathsf E_{\theta_3,M},
  \qquad r^M=(1),
\]
and \(\ell_{\theta_3}A_{\mathrm{cur}}^M=0\), \(\ell_{\theta_3}(r^M)=1\).

## Lower Source Calculation

For
\[
  \zeta^0_2=u_{a,H_{1,0}}u_{b,H_{0,1}},
\]
the Hamiltonian bracket
\[
  [H_{a,b},H_{r,s}]=(as-br)H_{a+r-1,b+s-1}
\]
gives, in the degree-\(2\) source window,
\[
  d_{\mathrm{CE}}\zeta^0_2
  =
  2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}} .
\]
With the row convention \(E_\nu=-K_{\Theta_3}(\zeta_\nu)\),
\[
  K^2_{\Theta_3}(d_{\mathrm{CE}}\zeta^0_2)
  =
  -2E^2_{\nu_{02}}+2E^2_{\nu_{20}} .
\]

Define the Hom-valued Bianchi defect
\[
  \mathfrak b^2_{02,20}
  =
  d_{\mathrm{ns},2}K^2_{\Theta_3}(\zeta^0_2)
  -
  K^2_{\Theta_3}(d_{\mathrm{CE}}\zeta^0_2).
\]
Then
\[
  d_{\mathrm{ns},2}D^2_{02,20}
  =
  -2E^2_{\nu_{02}}+2E^2_{\nu_{20}}
  +\mathfrak b^2_{02,20}.
\]
Hence \(D^2_{02,20}\) kills the transported residual
\[
  r_2=2E^2_{\nu_{02}}-2E^2_{\nu_{20}}
\]
if and only if \(\mathfrak b^2_{02,20}=0\) in the chosen local-functional
row complex, with scalar-zero value and compatible primitive transport.

This is the strongest construction obtained from the current source
coordinates.  The source primitive exists.  The local-functional primitive
exists exactly after the Bianchi row is killed.

## Bianchi-Exposed Matrix

Expose the Bianchi defect as a third degree-one row.  In the ordered lower
row basis
\[
  (E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20})
\]
the candidate \(D^2_{02,20}\) has boundary column
\[
  A_D^2=
  \begin{pmatrix}
    -2\\
    2\\
    1
  \end{pmatrix},
\]
while the lower residual is
\[
  r_2=
  \begin{pmatrix}
    2\\
    -2\\
    0
  \end{pmatrix}.
\]
The primitive equation \(A_D^2c=-r_2\) forces \(c=1\) from the first two
coordinates and then leaves the Bianchi coordinate \(1\).  Thus it has no
solution in the free Bianchi-row presentation.

A normalized cokernel certificate is
\[
  \widetilde\lambda_{02,\mathfrak b}
  =
  \frac12(E^2_{\nu_{02}})^*
  +(\mathfrak b^2_{02,20})^* .
\]
It satisfies
\[
  \widetilde\lambda_{02,\mathfrak b}A_D^2=0,\qquad
  \widetilde\lambda_{02,\mathfrak b}(r_2)=1.
\]
Therefore the exact lower obstruction is the Bianchi row
\(\mathfrak b^2_{02,20}\), not the source differential.  In the quotient
where \(\mathfrak b^2_{02,20}=0\), the same column becomes
\((-2,2)^T\) and \(c=1\) solves the lower primitive equation.

Equivalently, a local counterterm repair must supply a degree-zero
functional \(B^2_{02,20}\) with
\[
  d_{\mathrm{ns},2}B^2_{02,20}=-\mathfrak b^2_{02,20},
\]
scalar-zero value, local support or wavefront admissibility, and compatible
transport.  Then \(D^2_{02,20}+B^2_{02,20}\) is a genuine lower primitive.
No such \(B^2_{02,20}\) is present in the current checkout.

## Full Eight-Face Transport

At degree \(3\), the same source \(\zeta^0_M\) gives the eight-face
residual
\[
\begin{aligned}
  R^{\mathrm{cand}}_{\Theta_3,M}
  ={}&2E_{\nu_{02}}-2E_{\nu_{20}}+3E_{\nu_{03}}
      +2E_{\nu_{12}^{(1)}}-E_{\nu_{12}^{(2)}}\\
   &+E_{\theta_3}-2E_{\nu_{21}^{(2)}}-3E_{\nu_{30}} .
\end{aligned}
\]
The current diagonal source-face transport to \(N=2\) gives
\[
  v^{M,2}_{\mathrm{diag}}R^{\mathrm{cand}}_{\Theta_3,M}
  =
  2E^2_{\nu_{02}}-2E^2_{\nu_{20}}.
\]

An abstract non-diagonal transport could kill this residual.  If the first
two degree-two columns are fixed and the degree-three columns are
\[
  v_3,\ldots,v_8\in
  \mathbb C E^2_{\nu_{02}}\oplus\mathbb C E^2_{\nu_{20}},
\]
then the equation is
\[
  3v_3+2v_4-v_5+v_6-2v_7-3v_8=(-2,2)^T.
\]
It is solvable as linear algebra; for example \(v_6=(-2,2)^T\) and
the other degree-three columns zero.  This is not a construction from the
present data.  The current source-coordinate projection sends every
degree-three column to zero because those faces have no \(N=2\) monomial
representative.  A non-diagonal solution is therefore an extra marked
Costello transport datum: projected renormalized weights, lower row-basis
reduction, and codimension-two compatibility must be supplied.

For a full primitive \(D^M=K^M_{\Theta_3}(\zeta^0_M)\), the Bianchi-exposed
identity is
\[
  d_{\mathrm{ns},M}D^M
  =
  -R^{\mathrm{cand}}_{\Theta_3,M}
  +\mathfrak b^M_{\mathrm{cand}} .
\]
Primitive transport requires
\[
  d_{\mathrm{ns},N}\bigl(\pi_{M,N}D^M-D^N\bigr)
  =
  \pi_{M,N}\mathfrak b^M_{\mathrm{cand}}
  -\mathfrak b^N_{\mathrm{cand}}
\]
after row transport has matched the residuals.  Thus the Roos primitive
class is not even closed unless the Bianchi defects themselves transport
strictly, or differ by an explicitly supplied boundary.  The current script
does not supply this Bianchi transport datum.

## Source-Ancestor Obstruction

The all-degree ordinary pure two-\(u\) source route remains blocked by
\[
  q_{2u}
  =
  e^*_{((H_{0,1},H_{2,0}),c_{\rho_{2,1}})}
  -\frac12
  e^*_{((H_{0,1},H_{0,1}),c_{\rho_{0,2}})} .
\]
For every scanned finite degree \(3\le D\le10\),
\[
  q_{2u}d_{\mathrm{CE}}=0,\qquad
  q_{2u}(\zeta_{M,\nu_3})=1.
\]
The eight-face candidate has \(q_{2u}\)-value zero.  Hence it is not the
missing marked source generator.  A valid marked source repair must leave
the ordinary pure two-\(u\) envelope and must bring its own codimension-two
closure and Hom-valued Bianchi table.

## Exact Obstruction Theorem

Let \(\mathcal H^{\mathrm{B}}_{\theta_3}\) be the data-derived theta3
habitat generated by:

1. the current theta3 one-row finite complex;
2. the ordinary pure two-\(u\) source columns;
3. the eight source-algebraic companion faces;
4. the diagonal source-face transport;
5. the lower source-coordinate primitive \(D^2_{02,20}\);
6. the exposed Bianchi row \(\mathfrak b^2_{02,20}\);
7. no additional local counterterm, marked Costello incidence/weight table,
   codimension-two table, lower row relation, non-diagonal transport, or
   Bianchi-transport homotopy.

Then the theta3 row is not killed in \(\mathcal H^{\mathrm B}_{\theta_3}\).
The obstruction is the tuple
\[
  \left(
    \ell_{\theta_3},\,
    q_{2u},\,
    \widetilde\lambda_{02,\mathfrak b},\,
    3v_3+2v_4-v_5+v_6-2v_7-3v_8-(-2,2)^T,\,
    \mathcal C^{(2)}_{\mathrm{missing}}
  \right).
\]
The first component blocks the current one-row counterterm.  The second
blocks ordinary pure two-\(u\) CE ancestors.  The third proves that the
lower primitive \(D^2_{02,20}\) fails exactly by the Bianchi row.  The
fourth is the precise missing non-diagonal transport equation.  The fifth
records the absent marked Costello incidence/weight and codimension-two
closure table.

The strongest true positive statement is:

* If \(\mathfrak b^2_{02,20}=0\), or if a scalar-zero local counterterm
  \(B^2_{02,20}\) with \(dB^2_{02,20}=-\mathfrak b^2_{02,20}\) is supplied,
  then \(D^2_{02,20}\) kills the \(N=2\) transported residual.
* If, moreover, the family \(D^M\) and the Bianchi rows satisfy the
  transport identity above with zero Roos class, then the lower-window
  primitive is compatible.
* These hypotheses are exact missing data.  They are not present in the
  current checkout, and the validator correctly rejects the route.

## Verification Commands And Decisive Output

Commands run:

```bash
python3 scripts/finite_window_graph_array.py
python3 -m py_compile scripts/finite_window_graph_array.py
python3 - <<'PY'
# finite CE differential, q_{2u} scan, Bianchi-row matrix,
# and non-diagonal transport equation
PY
```

Decisive computed output:

```text
D= 2
  2 (((0, 1), (0, 1)), (0, 2))
  -2 (((1, 0), (1, 0)), (2, 0))
D= 3
  2 (((0, 1), (0, 1)), (0, 2))
  3 (((0, 1), (0, 2)), (0, 3))
  2 (((0, 1), (1, 1)), (1, 2))
  -1 (((0, 2), (1, 0)), (1, 2))
  -2 (((1, 0), (1, 0)), (2, 0))
  1 (((0, 1), (2, 0)), (2, 1))
  -2 (((1, 0), (1, 1)), (2, 1))
  -3 (((1, 0), (2, 0)), (3, 0))
qscan D= 3..10 q_dCE_zero=True
bianchi_exposed_A= [-2, 2, 1]
target_minus_r= [-2, 2, 0]
forced_c= 1
residual_after_D= [0, 0, 1]
ell_A= 0
ell_r= 1
diag_N2= [2, -2]
affine_needed_degree3_columns_sum= [-2, 2]
```

Focused validator output:

```text
theta_3_current_finite_row_subcomplex primitive_exists=false obstruction_value_on_residual=1
theta3_ce_ancestor_without_differential_entry accepted=false differential_entry_value=0
theta3_ce_ancestor_supplied_exact_payload accepted=true differential_entry_value=-1
theta3_counterterm_without_differential_entry accepted=false differential_entry_value=0
theta3_counterterm_supplied_exact_payload accepted=true differential_entry_value=-1
theta3_eight_face_candidate_source_algebraic_obstruction accepted=false
N=2 residual [['E_nu02', '2'], ['E_nu20', '-2']]
```

## Files Changed

- `reconstitution/swarm-2026-04-30-agent-270-theta3-bianchi-defect-closure-push.md`
- `reconstitution/theta3-bianchi-defect-closure-push-2026-04-30.md`
