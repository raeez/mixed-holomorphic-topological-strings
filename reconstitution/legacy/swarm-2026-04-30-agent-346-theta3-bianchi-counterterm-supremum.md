# Agent 346 Theta3 Bianchi Counterterm Supremum Report

Status: report-only. No TeX, script, figure, bibliography, PDF, or build
artifact was edited.

## Verdict

The next theorem cannot be upgraded by constructing
\(B^2_{02,20}\) from the current habitat. The current Bianchi-exposed
lower habitat proves an exact fixed-window obstruction.

The admissible supremum statement is habitat-relative:

1. In the present lower finite-row habitat, no scalar-zero local-functional
   column has boundary \(A_B^2=(0,0,-1)^T\).
2. A formal adjunction of such a column solves the \(N=2\) matrix, but is
   not a Costello counterterm until the local functional, scalar projection,
   locality or wavefront habitat, row coordinates, and tower transport are
   supplied.
3. The next positive theorem may be a Bianchi counterterm-column theorem only
   with those data as hypotheses or as a constructed package. It is not yet
   an existence theorem.

## Anchors

- `appendix-unreduced-bv-qme.tex:2077-2246`: the non-scalar complex is
  \(\mathcal K^\bullet_{\mathrm{ns},M}(I)=\ker\widehat\sigma_{\mathrm{sc},M}\);
  it exists only after \(\widehat\sigma_{\mathrm{sc},M}\) is a filtered
  chain map.
- `appendix-unreduced-bv-qme.tex:2248-2399`: the finite-row criterion is
  \(A^Mc=-r^M\), with tower conditions \(T^{M,N}r^M=r^N\),
  \(T^{M,N}A^M=A^NP^{M,N}\), and a zero Roos \(H^0\) primitive class.
- `appendix-unreduced-bv-qme.tex:2501-2642`: the lower \(\theta_3\)
  Bianchi gate displays \(A_D^2\), \(r_2\), \(A_B^2\), and
  \(\Delta^1_{M,N}\).
- `main.tex:8849-9118`: the main acceptance gate records the same
  obstruction and says the present habitat contains no \(B^2_{02,20}\).
- `reconstitution/swarm-2026-04-30-agent-338-nonscalar-qme-next-supremum-plan.md`:
  the next target is the scalar-zero Bianchi column followed by tower
  transport, not the full non-scalar Costello graph/QME theorem.

## Fixed-Window Computation

Let
\[
  e_1=E^2_{\nu_{02}},\qquad
  e_2=E^2_{\nu_{20}},\qquad
  e_3=\mathfrak b^2_{02,20}.
\]
The current lower habitat is
\[
  \mathcal H^0_{\mathrm{cur}}=\mathbb C D^2_{02,20},\qquad
  \mathcal H^1_{\mathrm{cur}}
  =
  \mathbb C e_1\oplus\mathbb C e_2\oplus\mathbb C e_3.
\]
The source-coordinate primitive is
\[
  \zeta^0_2=u_{a,H_{1,0}}u_{b,H_{0,1}},\qquad
  D^2_{02,20}=K^2_{\Theta_3}(\zeta^0_2),
\]
with
\[
  d_{\mathrm{CE}}\zeta^0_2
  =
  2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}}.
\]
The Hom-valued Bianchi defect is
\[
  \mathfrak b^2_{02,20}
  =
  d_{\mathrm{ns},2}K^2_{\Theta_3}(\zeta^0_2)
  -
  K^2_{\Theta_3}(d_{\mathrm{CE}}\zeta^0_2).
\]
Thus
\[
  d_{\mathrm{ns},2}D^2_{02,20}
  =
  -2E^2_{\nu_{02}}+2E^2_{\nu_{20}}
  +\mathfrak b^2_{02,20},
\]
so the only current boundary column is
\[
  A_D^2=(-2,2,1)^T.
\]
The transported lower residual is
\[
  r_2=(2,-2,0)^T.
\]
The Bianchi-killing target is
\[
  -\mathfrak b^2_{02,20}=(0,0,-1)^T=:A_B^2.
\]

The normalized cokernel functional
\[
  \widetilde\lambda_{02,\mathfrak b}
  =
  \frac12(E^2_{\nu_{02}})^*
  +(\mathfrak b^2_{02,20})^*
\]
satisfies
\[
  \widetilde\lambda_{02,\mathfrak b}A_D^2=0,\qquad
  \widetilde\lambda_{02,\mathfrak b}(r_2)=1,\qquad
  \widetilde\lambda_{02,\mathfrak b}(A_B^2)=-1.
\]
Hence \(A_D^2c=-r_2\) has no solution in the current one-column habitat, and
\(A_B^2\notin\operatorname{im}A_D^2\). This is a proved obstruction in the
current lower finite-row habitat.

If a genuine \(B^2_{02,20}\) is added, the enlarged fixed-window matrix is
\[
  A^2_{D,B}
  =
  \begin{pmatrix}
    -2&0\\
     2&0\\
     1&-1
  \end{pmatrix}.
\]
Then
\[
  A^2_{D,B}(1,1)^T=(-2,2,0)^T=-r_2,
\]
equivalently
\[
  d_{\mathrm{ns},2}(D^2_{02,20}+B^2_{02,20})
  =
  -2E^2_{\nu_{02}}+2E^2_{\nu_{20}}.
\]

## Degrees

The lower source primitive \(\zeta^0_2\) is a degree-zero source element, and
\(d_{\mathrm{CE}}\zeta^0_2\) is a degree-one source-face row.

The local-functional candidates
\[
  D^2_{02,20},\quad B^2_{02,20}
\]
must lie in
\[
  \mathcal K^0_{\mathrm{ns},2}(I).
\]
The target rows
\[
  E^2_{\nu_{02}},\quad E^2_{\nu_{20}},\quad
  \mathfrak b^2_{02,20}
\]
lie in
\[
  \mathcal K^1_{\mathrm{ns},2}(I).
\]
Thus \(A_D^2\) and \(A_B^2\) are columns for
\[
  d_{\mathrm{ns},2}\colon
  \mathcal K^0_{\mathrm{ns},2}(I)\to
  \mathcal K^1_{\mathrm{ns},2}(I).
\]
For the tower, \(\Delta^1_{M,N}\) is a degree-one cocycle in
\(\mathcal K^\bullet_{\mathrm{ns},N}(I)\), and any transport correction
\(H^{M,N}\) or primitive defect \(\pi_{M,N}B^M-B^N-H^{M,N}\) is degree zero.

## Required Habitat Enlargement

A theorem-grade positive construction must add all of the following data.

1. A marked finite graph/counterterm habitat \(\mathcal G^B_M\) containing the
   lower Bianchi row \(\mathfrak b^M\) and a degree-zero counterterm generator
   \(B^M_{02,20}\).
2. A genuine local functional
   \[
     B^M_{02,20}\in
     \mathcal O^{\mathrm{bd}}_{\mathrm{loc},\mathcal G^B,M}
     (\mathcal E^M_w|_I;A^{\mathrm{pp},w,M}_{\partial,\hbar}(I))
   \]
   whose class lies in \(\mathcal K^0_{\mathrm{ns},M}(I)\).
3. A row-coordinate computation proving
   \[
     d_{\mathrm{ns},M}B^M_{02,20}=-\mathfrak b^M,
   \]
   and, at \(M=2\), no extra \(E^2_{\nu_{02}}\) or \(E^2_{\nu_{20}}\)
   components.
4. The scalar projection condition
   \[
     \widehat\sigma_{\mathrm{sc},M}(B^M_{02,20})=0,
   \]
   with \(\widehat\sigma_{\mathrm{sc},M}\) already a filtered chain map on the
   enlarged habitat. Without this, \(\mathcal K_{\mathrm{ns},M}\) is not a
   complex.
5. Regular-density locality or a graphwise wavefront-admissible representative,
   including the graph, current labels, scaling-degree extension, counterterm
   support, and incidence signs.
6. Bianchi-row transport maps and primitive transport maps in a common lower
   row basis.

## Tower Gate

For \(M\ge N\), define
\[
  \Delta^1_{M,N}
  :=
  -\pi_{M,N}\mathfrak b^M+\mathfrak b^N
  \in Z^1(\mathcal K^\bullet_{\mathrm{ns},N}(I)).
\]
A compatible \(B\)-tower requires
\[
  \Delta^1_{M,N}
  =
  d_{\mathrm{ns},N}(\pi_{M,N}B^M-B^N),
\]
or, more generally, scalar-zero corrections \(H^{M,N}\in
\mathcal K^0_{\mathrm{ns},N}(I)\) with
\[
  d_{\mathrm{ns},N}H^{M,N}=\Delta^1_{M,N}.
\]
After choosing \(H^{M,N}\), the secondary class
\[
  [\pi_{M,N}B^M-B^N-H^{M,N}]
  \in
  \varprojlim\nolimits^1_N
  H^0(\mathcal K^\bullet_{\mathrm{ns},N}(I))
\]
must vanish. The current checkout does not construct \(\mathfrak b^M\) in a
common transported row basis, does not construct \(B^M\), and does not compute
this secondary class.

## Patch Recommendations

Do not patch the manuscript to assert existence of \(B^2_{02,20}\). The
current TeX should retain the obstruction statement: in the present
Bianchi-exposed habitat, \(A_B^2=(0,0,-1)^T\) is outside the current boundary
image.

The next acceptable TeX patch, when manuscript editing is authorized, is a
definition/theorem pair for a supplied \(\theta_3\) Bianchi counterterm-column
datum:
\[
  B^M_{02,20}\in\mathcal K^0_{\mathrm{ns},M}(I),\qquad
  d_{\mathrm{ns},M}B^M_{02,20}=-\mathfrak b^M,\qquad
  \widehat\sigma_{\mathrm{sc},M}(B^M_{02,20})=0,
\]
plus locality or wavefront admissibility, \(\Delta^1\)-killing correction, and
zero secondary \(\varprojlim^1H^0\). The theorem should conclude only that
\(D^M_{02,20}+B^M_{02,20}\) kills the lower \(\theta_3\) Bianchi residual in
the supplied finite-row tower. It should not claim a CE ancestor, a complete
companion-face table, centrality homotopies, or the full curved
bulk-to-defect Costello kernel.

If the row becomes machine-gated, extend `scripts/finite_window_graph_array.py`
to emit the three-coordinate Bianchi matrix record
\[
  A_D^2=(-2,2,1)^T,\quad r_2=(2,-2,0)^T,\quad A_B^2=(0,0,-1)^T,
\]
and the values of \(\widetilde\lambda_{02,\mathfrak b}\). This is a future
script patch, not part of this report.

## Verification

Read:

- `CLAUDE.md`
- `AGENTS.md`
- `~/ecosystem/INVARIANTS.md`
- `~/ecosystem/AGENTS-HARNESS.md`
- `~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `commands.tex`
- `mathmacros.tex`
- `main.tex:8720-9165`
- `appendix-unreduced-bv-qme.tex:2050-2642`
- `open-obligations.tex:500-958`
- `claim-strength-ledger.tex:500-550`
- `claim-strength-ledger.tex:930-994`
- `reconstitution/swarm-2026-04-30-agent-338-nonscalar-qme-next-supremum-plan.md`
- theta3 reports for the no-counterterm, actual local-functional, matrix,
  and \(\Delta^1\) transport lanes

Commands run:

```bash
git status --short
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
# targeted finite-row payload and matrix verification
PY
```

Decisive output:

```text
theta_3_current_finite_row_subcomplex False 1 []
theta3_counterterm_without_differential_entry True False 0 ['differential entry dC=-E']
theta3_counterterm_supplied_exact_payload True True -1 []
eight_face_accepted False
eight_face_n2 [['E_nu02', '2'], ['E_nu20', '-2']]
matrix_A_D ['-2', '2', '1']
matrix_r ['2', '-2', '0']
matrix_A_B ['0', '0', '-1']
ell_A_D 0
ell_r 1
ell_A_B -1
D_plus_B ['-2', '2', '0']
equals_minus_r [True, True, True]
```

Files changed:

- `reconstitution/swarm-2026-04-30-agent-346-theta3-bianchi-counterterm-supremum.md`
