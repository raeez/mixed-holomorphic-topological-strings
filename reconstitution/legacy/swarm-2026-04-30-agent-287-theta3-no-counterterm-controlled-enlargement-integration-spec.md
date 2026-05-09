# Agent 287 - Theta3 No-Counterterm Controlled-Enlargement Integration Spec

Status: report-only.  No TeX, script, figure, source fixture, bibliography,
PDF, or build artifact was edited.

Owned files:

- `reconstitution/theta3-no-counterterm-controlled-enlargement-integration-spec-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-287-theta3-no-counterterm-controlled-enlargement-integration-spec.md`

## Claim attacked

The attacked claim is that the current theta3 Bianchi surface already
contains, or can derive from the present finite-row data, a scalar-zero local
counterterm
\[
  B^2_{02,20}
\]
with
\[
  d_{\mathrm{ns},2}B^2_{02,20}
  =
  -\mathfrak b^2_{02,20}.
\]

This is the exact datum needed to turn the source-coordinate primitive
\[
  D^2_{02,20}=K^2_{\Theta_3}(u_{a,H_{1,0}}u_{b,H_{0,1}})
\]
into a local-functional primitive for the transported lower residual.

## Context loaded

Governing and skill files:

- `CLAUDE.md`
- `AGENTS.md`
- `~/ecosystem/INVARIANTS.md`
- `~/ecosystem/AGENTS-HARNESS.md`
- `.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`

Theta3 anchors:

- `reconstitution/theta3-bianchi-counterterm-construction-push-2026-04-30.md`
- `reconstitution/theta3-bianchi-matrix-integration-spec-2026-04-30.md`
- `reconstitution/theta3-controlled-enlargement-witness-search-2026-04-30.md`
- `reconstitution/theta3-nondiagonal-transport-counterterm-construction-push-2026-04-30.md`
- `reconstitution/theta3-bianchi-defect-closure-push-2026-04-30.md`
- `main.tex:8378-8604`
- `theorem-lanes.tex:3307-3421`
- `open-obligations.tex:715-862`
- `claim-strength-ledger.tex:465-499`
- `claim-strength-ledger.tex:841-874`
- `scripts/finite_window_graph_array.py:982-2035`

## Attack result

The present source calculation is correct:
\[
  d_{\mathrm{CE}}(u_{a,H_{1,0}}u_{b,H_{0,1}})
  =
  2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}}.
\]
With \(E_\nu=-K_{\Theta_3}(\zeta_\nu)\), the local-functional boundary is
\[
  d_{\mathrm{ns},2}D^2_{02,20}
  =
  -2E^2_{\nu_{02}}+2E^2_{\nu_{20}}
  +\mathfrak b^2_{02,20}.
\]
The Bianchi row is the obstruction to local-functional exactness.

In the current Bianchi-exposed lower row basis
\[
  (E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20}),
\]
the only available degree-zero column is
\[
  A_D^2=(-2,2,1)^T.
\]
The desired counterterm target is
\[
  (0,0,-1)^T.
\]
No scalar multiple of \(A_D^2\) equals this target.  The first two
coordinates force the multiplier to be \(0\); the Bianchi coordinate forces
it to be \(-1\).

The cokernel certificate is
\[
  \widetilde\lambda_{02,\mathfrak b}
  =
  \frac12(E^2_{\nu_{02}})^*
  +(\mathfrak b^2_{02,20})^*.
\]
It gives
\[
  \widetilde\lambda_{02,\mathfrak b}A_D^2=0,\qquad
  \widetilde\lambda_{02,\mathfrak b}((0,0,-1)^T)=-1.
\]
Hence \(B^2_{02,20}\) does not exist in the current finite-row habitat.

## Heal

The healed theorem surface is not a downgrade.  It is an exact obstruction
plus a precise positive target.

The controlled target is a new local-functional column
\[
  A_B^2=(0,0,-1)^T,
\]
represented by a genuine element
\[
  B^2_{02,20}\in\mathcal K^0_{\mathrm{ns},2}(I)
\]
such that
\[
  d_{\mathrm{ns},2}B^2_{02,20}
  =
  -\mathfrak b^2_{02,20},\qquad
  \widehat\sigma_{\mathrm{sc},2}(B^2_{02,20})=0.
\]
It must also carry regular-density or wavefront-admissible locality and
finite-window transport.

With this column added, the boundary matrix becomes
\[
  A^2_{\mathrm{ct}}
  =
  \begin{pmatrix}
    -2&0\\
     2&0\\
     1&-1
  \end{pmatrix}.
\]
Then
\[
  d_{\mathrm{ns},2}(D^2_{02,20}+B^2_{02,20})
  =
  -2E^2_{\nu_{02}}+2E^2_{\nu_{20}},
\]
so the lower residual is killed.  This is a formal algebraic construction
target, not a current Costello counterterm construction.

For a tower \(B^M\), compatibility requires
\[
  d_{\mathrm{ns},N}(\pi_{M,N}B^M-B^N)
  =
  -\pi_{M,N}\mathfrak b^M+\mathfrak b^N.
\]
The Roos class is closed only after the Bianchi rows transport strictly, or
after a supplied correction kills the right side and the corrected
\(H^0\)-class vanishes.

## Construction status

No theorem-grade \(B^2_{02,20}\) habitat was constructed.  The missing data
are exactly:

1. the local-functional formula for \(B^2_{02,20}\);
2. the boundary column \(A_B^2=(0,0,-1)^T\);
3. scalar-zero value;
4. regular-density or wavefront-admissible locality;
5. compatible finite-window transport and zero Roos class.

The current script fixture `theta3_counterterm_supplied_exact_payload` is
for a different target, \(dC_{\theta_3}=-E_{\theta_3}\).  It is an
interface acceptance fixture and does not supply
\(dB^2_{02,20}=-\mathfrak b^2_{02,20}\).

## Verification

Commands run:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py
python3 - <<'PY'
# focused finite-row matrix check
PY
```

Decisive output:

```text
A_D= ['-2', '2', '1']
r= ['2', '-2', '0']
target_-b= ['0', '0', '-1']
ell_A_D= 0
ell_r= 1
ell_target_-b= -1
kill_residual_target_-r ['1', '1', '0']
kill_bianchi_target ['0', '0', '-1']
A_DB_solution_for_lower_residual_D_plus_B= ['-2', '2', '0']
D_plus_B_equals_-r= [True, True, True]
theta_3_current_finite_row_subcomplex False 1 []
theta3_counterterm_without_differential_entry False 0 ['differential entry dC=-E']
theta3_counterterm_supplied_exact_payload True -1 []
eight_face_accepted False
eight_face_n2 [['E_nu02', '2'], ['E_nu20', '-2']]
```

## Claim status

Exact obstruction in the current finite-row habitat.  Positive theorem
target fixed: construct \(B^2_{02,20}\) with
\[
  A_B^2=(0,0,-1)^T
\]
and prove scalar-zero, locality, transport, and zero Roos compatibility.
