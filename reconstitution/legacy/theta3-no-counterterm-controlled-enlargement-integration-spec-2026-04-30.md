# Theta3 No-Counterterm Controlled-Enlargement Integration Spec

Status: report-only integration specification.  No TeX, script, figure,
source fixture, bibliography, or build artifact is edited by this note.

## Decision

The current Bianchi-exposed finite-row habitat contains no
\(B^2_{02,20}\) counterterm.  The obstruction is not a notation gap.  It is
the fixed-window cokernel of the only available lower degree-zero column.

The strongest true statement is habitat-relative:

- the source-coordinate primitive
  \(D^2_{02,20}=K^2_{\Theta_3}(u_{a,H_{1,0}}u_{b,H_{0,1}})\) proves source
  exactness only;
- in the current local-functional finite-row habitat, the target
  \(-\mathfrak b^2_{02,20}\) is not in the boundary image;
- a positive repair must add a new scalar-zero local-functional column
  \(A_B^2=(0,0,-1)^T\), with locality or wavefront admissibility and
  finite-window transport.

This note does not construct that Costello local-functional habitat from the
current data.  The formal algebraic adjunction of such a column is immediate
and is recorded below as the acceptance target.  It is not a construction of
the required counterterm until the local functional, scalar projection,
locality, and transport are supplied.

## Current finite-row habitat

Let
\[
  e_1=E^2_{\nu_{02}},\qquad
  e_2=E^2_{\nu_{20}},\qquad
  e_3=\mathfrak b^2_{02,20}.
\]
The current Bianchi-exposed lower habitat is the finite complex
\[
  \mathcal H^0_{\mathrm{cur}}=\C D^2_{02,20},\qquad
  \mathcal H^1_{\mathrm{cur}}=\C e_1\oplus\C e_2\oplus\C e_3,
\]
with
\[
  d_{\mathrm{ns},2}D^2_{02,20}
  =
  -2e_1+2e_2+e_3.
\]
Thus the single current boundary column is
\[
  A_D^2=(-2,2,1)^T.
\]
The transported lower residual is
\[
  r_2=(2,-2,0)^T,
\]
and the desired Bianchi counterterm target is
\[
  -e_3=(0,0,-1)^T.
\]

The normalized cokernel functional is
\[
  \widetilde\lambda_{02,\mathfrak b}
  =
  \frac12 e_1^*+e_3^* .
\]
It satisfies
\[
  \widetilde\lambda_{02,\mathfrak b}A_D^2=0,\qquad
  \widetilde\lambda_{02,\mathfrak b}(r_2)=1,\qquad
  \widetilde\lambda_{02,\mathfrak b}(-e_3)=-1.
\]

## TeX-ready obstruction block

Insert only when manuscript editing is authorized.

```tex
\begin{prop}[Bianchi-row no-counterterm gate for the lower \(\theta_3\) row]
  Work in the Bianchi-exposed lower finite-window habitat generated in
  degree \(1\) by
  \[
    E^2_{\nu_{02}},\quad E^2_{\nu_{20}},\quad
    \mathfrak b^2_{02,20}
  \]
  and in degree \(0\) by the single source-coordinate column
  \(D^2_{02,20}=K^2_{\Theta_3}(\zeta^0_2)\), where
  \(\zeta^0_2=u_{a,H_{1,0}}u_{b,H_{0,1}}\).  Assume no additional
  degree-zero local-functional column, no row relation among the three
  displayed rows, and no non-diagonal transport relation has been supplied.
  Then there is no element \(B^2_{02,20}\) in this habitat with
  \[
    d_{\mathrm{ns},2}B^2_{02,20}
    =
    -\mathfrak b^2_{02,20}.
  \]
\end{prop}

\begin{proof}
  The source calculation gives
  \[
    d_{\mathrm{CE}}\zeta^0_2
    =
    2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}},
  \]
  but \(K^2_{\Theta_3}\) is not a chain map until its Hom-valued Bianchi
  defect is killed.  In the ordered basis
  \[
    (E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20})
  \]
  the current column is
  \[
    A_D^2=(-2,2,1)^T,
  \]
  while the desired Bianchi-counterterm target is
  \[
    (0,0,-1)^T.
  \]
  If \(xD^2_{02,20}\) had this boundary, then
  \[
    x(-2,2,1)^T=(0,0,-1)^T .
  \]
  The first two coordinates force \(x=0\), and the Bianchi coordinate
  forces \(x=-1\).  Equivalently, the covector
  \[
    \widetilde\lambda_{02,\mathfrak b}
    =
    \frac12(E^2_{\nu_{02}})^*
    +(\mathfrak b^2_{02,20})^*
  \]
  annihilates \(A_D^2\) but satisfies
  \[
    \widetilde\lambda_{02,\mathfrak b}
    ((0,0,-1)^T)=-1.
  \]
  Hence the target is not in the current boundary image.
\end{proof}
```

## Controlled-enlargement target

The minimal algebraic enlargement that would close the lower Bianchi gate is
\[
  \mathcal H^0_{\mathrm{ct}}
  =
  \C D^2_{02,20}\oplus\C B^2_{02,20},
  \qquad
  \mathcal H^1_{\mathrm{ct}}
  =
  \C e_1\oplus\C e_2\oplus\C e_3,
\]
with boundary matrix
\[
  A^2_{\mathrm{ct}}
  =
  \begin{pmatrix}
    -2&0\\
     2&0\\
     1&-1
  \end{pmatrix},
  \qquad
  A_B^2=(0,0,-1)^T.
\]
Then
\[
  d_{\mathrm{ns},2}(D^2_{02,20}+B^2_{02,20})
  =
  -2e_1+2e_2
  =
  -r_2.
\]

This formal matrix extension becomes a theorem-grade local-functional
habitat only after the following data are supplied.

1. A genuine local functional
   \[
     B^2_{02,20}\in\mathcal K^0_{\mathrm{ns},2}(I)
   \]
   with
   \[
     d_{\mathrm{ns},2}B^2_{02,20}
     =
     -\mathfrak b^2_{02,20}.
   \]
2. Scalar-zero value:
   \[
     \widehat\sigma_{\mathrm{sc},2}(B^2_{02,20})=0.
   \]
3. Locality or wavefront admissibility for the current labels and interval
   support entering \(B^2_{02,20}\).
4. Compatible finite-window transport.  For a tower \(B^M\), the necessary
   identity is
   \[
     d_{\mathrm{ns},N}(\pi_{M,N}B^M-B^N)
     =
     -\pi_{M,N}\mathfrak b^M+\mathfrak b^N .
   \]
   The Roos class is closed only if the Bianchi rows transport strictly, or
   after a supplied correction \(H^{M,N}\) kills the right side and the
   class of \(\pi_{M,N}B^M-B^N-H^{M,N}\) vanishes in
   \(H^0(\mathcal K^\bullet_{\mathrm{ns},N}(I))\).

## TeX-ready target block

```tex
\begin{constr}[Controlled target for a Bianchi counterterm column]
  A repair of the lower \(\theta_3\) Bianchi gate must add a genuine
  scalar-zero local functional
  \[
    B^2_{02,20}\in\mathcal K^0_{\mathrm{ns},2}(I)
  \]
  whose boundary column in the basis
  \((E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20})\) is
  \[
    A_B^2=(0,0,-1)^T .
  \]
  Equivalently,
  \[
    d_{\mathrm{ns},2}B^2_{02,20}
    =
    -\mathfrak b^2_{02,20},
    \qquad
    \widehat\sigma_{\mathrm{sc},2}(B^2_{02,20})=0,
  \]
  with regular-density or wavefront-admissible locality.  If this datum is
  supplied, then
  \[
    d_{\mathrm{ns},2}(D^2_{02,20}+B^2_{02,20})
    =
    -2E^2_{\nu_{02}}+2E^2_{\nu_{20}},
  \]
  so \(D^2_{02,20}+B^2_{02,20}\) is the lower local-functional primitive.
  For a finite-window tower the additional requirement is
  \[
    d_{\mathrm{ns},N}(\pi_{M,N}B^M-B^N)
    =
    -\pi_{M,N}\mathfrak b^M+\mathfrak b^N,
  \]
  together with vanishing of the resulting Roos \(H^0\)-class after the
  supplied transport correction.
\end{constr}
```

## Claim-strength rules

Allowed now:

- The lower residual is source-exact in the CE source complex.
- The Bianchi-exposed lower local-functional complex has no
  \(B^2_{02,20}\) in the current finite-row habitat.
- The cokernel
  \(\widetilde\lambda_{02,\mathfrak b}\) detects both the lower residual
  and the missing Bianchi-counterterm target.

Forbidden without new data:

- \(D^2_{02,20}\) kills the \(N=2\) residual.
- A \(B^2_{02,20}\) local counterterm exists.
- The formal column \(A_B^2=(0,0,-1)^T\) is a Costello local functional.
- The primitive tower has zero Roos class.

Admissible after new data:

- If \(B^2_{02,20}\) is supplied with \(A_B^2=(0,0,-1)^T\), scalar-zero
  value, locality, and transport, then \(D^2_{02,20}+B^2_{02,20}\) kills
  the lower residual.
- If the tower also supplies strict Bianchi-row transport, or a correction
  killing the transport defect, then the lower primitive can be made
  finite-window compatible.

## Verification

Read anchors:

- `CLAUDE.md`
- `AGENTS.md`
- `reconstitution/theta3-bianchi-counterterm-construction-push-2026-04-30.md`
- `reconstitution/theta3-bianchi-matrix-integration-spec-2026-04-30.md`
- `main.tex:8378-8604`
- `theorem-lanes.tex:3307-3421`
- `open-obligations.tex:715-862`
- `claim-strength-ledger.tex:465-499`
- `claim-strength-ledger.tex:841-874`
- `scripts/finite_window_graph_array.py:982-2035`

Commands run:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py
python3 - <<'PY'
# focused matrix check for A_D, r, target -b, and formal A_B column
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

## Files changed

- `reconstitution/theta3-no-counterterm-controlled-enlargement-integration-spec-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-287-theta3-no-counterterm-controlled-enlargement-integration-spec.md`
