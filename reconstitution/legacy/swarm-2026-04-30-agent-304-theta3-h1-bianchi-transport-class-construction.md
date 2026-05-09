# Agent 304 - Theta3 H1 Bianchi Transport Class Construction

Status: report-only.  No TeX, script, figure, source fixture, bibliography,
PDF, or build artifact was edited.

## Claim Attacked

Lane: construct or kill the \(H^1\) Bianchi transport class for a
hypothetical \(B^M\)-tower attached to the lower \(\theta_3\) Bianchi row.

## Result

The class is constructed.  It is killed only under the formal hypothesis that
the \(B^M\)-tower already exists as an inverse-system datum.

For an inverse system
\[
  (\mathcal K^\bullet_{\theta_3,M},d_M,\pi_{M,N})
\]
and Bianchi cycles \(\mathfrak b^M\), define
\[
  \Delta^1_{M,N}
  =
  -\pi_{M,N}\mathfrak b^M+\mathfrak b^N .
\]
The \(H^1\) Bianchi transport class is
\[
  \operatorname{ob}^1_{\mathfrak b}
  =
  \bigl([\Delta^1_{M,N}]\bigr)_{M\geq N}
  \in
  C^1_{\mathrm{Roos}}
  \bigl(H^1(\mathcal K^\bullet_{\theta_3,\bullet})\bigr).
\]

If a genuine projected tower \(B^M\) satisfies
\[
  d_MB^M=-\mathfrak b^M,
\]
then
\[
  \Delta^1_{M,N}
  =
  d_N(\pi_{M,N}B^M-B^N).
\]
Thus the \(H^1\) class is zero with explicit correction
\[
  H_B^{M,N}=\pi_{M,N}B^M-B^N.
\]
This is formal.  It does not construct \(B^M\).

## Current Checkout Obstruction

The current data do not contain \(B^2_{02,20}\).  In the Bianchi-exposed
lower basis
\[
  (E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20}),
\]
the only available lower degree-zero column is
\[
  A_D^2=(-2,2,1)^T,
\]
while the Bianchi-counterterm target is
\[
  A_B^2=(0,0,-1)^T.
\]
The cokernel
\[
  \widetilde\lambda_{02,\mathfrak b}
  =
  \frac12(E^2_{\nu_{02}})^*
  +(\mathfrak b^2_{02,20})^*
\]
satisfies
\[
  \widetilde\lambda_{02,\mathfrak b}A_D^2=0,\qquad
  \widetilde\lambda_{02,\mathfrak b}A_B^2=-1.
\]
Hence the actual current finite-row habitat has no \(B^2\), so the formal
tower kill cannot be promoted to a theorem in this checkout.

## Source Rows And Transport

The lower source-coordinate row is
\[
  \zeta^0_2=u_{a,H_{1,0}}u_{b,H_{0,1}},
  \qquad
  d_{\mathrm{CE}}\zeta^0_2
  =
  2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}}.
\]
The Bianchi row is
\[
  \mathfrak b^2_{02,20}
  =
  d_{\mathrm{ns},2}K^2_{\Theta_3}(\zeta^0_2)
  -
  K^2_{\Theta_3}(d_{\mathrm{CE}}\zeta^0_2).
\]
Thus
\[
  d_{\mathrm{ns},2}K^2_{\Theta_3}(\zeta^0_2)
  =
  -2E^2_{\nu_{02}}+2E^2_{\nu_{20}}
  +\mathfrak b^2_{02,20}.
\]

For \(M\ge3\), the tested eight-face source-algebraic vector is
\[
  (2,-2,3,2,-1,1,-2,-3)
\]
on
\[
  E_{\nu_{02}},E_{\nu_{20}},E_{\nu_{03}},
  E_{\nu_{12}^{(1)}},E_{\nu_{12}^{(2)}},
  E_{\theta_3},E_{\nu_{21}^{(2)}},E_{\nu_{30}}.
\]
The supplied diagonal source-face transport
\[
  v^{M,N}_{\nu;\nu'}=1
  \quad\text{for}\quad \nu=\nu',\ \deg(\nu)\leq N
\]
and zero otherwise sends this vector at \(N=2\) to
\[
  2E^2_{\nu_{02}}-2E^2_{\nu_{20}}.
\]
This is not a Bianchi-row transport.  The missing theorem datum is
\[
  \pi_{M,N}\mathfrak b^M=\mathfrak b^N
\]
or a supplied correction
\[
  d_NH^{M,N}
  =
  -\pi_{M,N}\mathfrak b^M+\mathfrak b^N.
\]

## Insertion Blocks

Report-only insertion targets are recorded in:

- `reconstitution/theta3-h1-bianchi-transport-class-construction-2026-04-30.md`

They include:

1. a definition of \(\operatorname{ob}^1_{\mathfrak b}\);
2. a formal lemma that a projected \(B^M\)-tower kills the \(H^1\) class;
3. a current-checkout gate showing \(B^2_{02,20}\) is absent by
   \(\widetilde\lambda_{02,\mathfrak b}\).

## Verification

Read:

- `CLAUDE.md`
- `AGENTS.md`
- `reconstitution/theta3-roos-transport-obstruction-push-2026-04-30.md`
- theta3 reconstitution reports for Agents 193, 197, 201, 207, 213, 215,
  224, 245, 251, 257, 263, 270, 277, 282, 287, 294, and 299
- `main.tex:8588-8905`
- `theorem-lanes.tex:3330-3578`
- `open-obligations.tex:720-895`
- `scripts/finite_window_graph_array.py:430-560`
- `scripts/finite_window_graph_array.py:982-2039`

Commands run:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py
python3 - <<'PY'
# focused theta3 row, eight-face, Bianchi matrix, and formal H1 witness check
PY
git status --short
```

Focused output:

```text
theta_3_current_finite_row_subcomplex primitive_exists= False ell_r= 1 deg0= ()
theta3_counterterm_without_differential_entry accepted= False dC= 0 missing= ('differential entry dC=-E',)
theta3_counterterm_supplied_exact_payload accepted= True dC= -1 missing= ()
eight_face_accepted= False
eight_face_n2= (('E_nu02', '2'), ('E_nu20', '-2'))
A_D= ['-2', '2', '1']
r= ['2', '-2', '0']
target_-b= ['0', '0', '-1']
ell_A_D= 0
ell_r= 1
ell_target_-b= -1
d(D+B)= ['-2', '2', '0']
-r= ['-2', '2', '0']
Delta1_symbol= -pi_{M,N} b^M + b^N
H1_witness_if_B_tower= pi_{M,N} B^M - B^N
```

## Files Changed

- `reconstitution/theta3-h1-bianchi-transport-class-construction-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-304-theta3-h1-bianchi-transport-class-construction.md`
