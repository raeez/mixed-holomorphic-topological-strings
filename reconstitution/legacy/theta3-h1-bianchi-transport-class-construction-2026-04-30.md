# Theta3 H1 Bianchi Transport Class Construction

Date: 2026-04-30.
Status: report-only construction.  No TeX, script, figure, source fixture,
bibliography, PDF, or build artifact was edited.

## Decision

The \(H^1\) Bianchi transport class can be defined canonically for a proposed
finite-window system of Bianchi rows
\[
  \mathfrak b^M
  \in Z^1(\mathcal K^\bullet_{\theta_3,M},d_M).
\]
It cannot be evaluated as a theorem-grade current obstruction in the checkout,
because the checkout does not supply:

1. a genuine \(B^2_{02,20}\) local functional;
2. Bianchi-row transport matrices
   \(\pi_{M,N}\mathfrak b^M\);
3. a marked Costello incidence/weight table reducing the projected rows in a
   common lower basis.

If a genuine inverse-system \(B^M\)-tower is assumed, with
\[
  d_MB^M=-\mathfrak b^M
\]
and with \(\pi_{M,N}B^M\) defined by a chain map, then the \(H^1\) class is
killed tautologically:
\[
  -\pi_{M,N}\mathfrak b^M+\mathfrak b^N
  =
  d_N(\pi_{M,N}B^M-B^N).
\]
This is a formal consequence of the tower axioms, not a construction of the
tower.  The actual current lower habitat still fails at \(N=2\):
\[
  (0,0,-1)^T=-\mathfrak b^2_{02,20}
  \notin \operatorname{im}((-2,2,1)^T).
\]
The detecting covector is
\[
  \widetilde\lambda_{02,\mathfrak b}
  =
  \frac12(E^2_{\nu_{02}})^*
  +(\mathfrak b^2_{02,20})^*,
\]
with
\[
  \widetilde\lambda_{02,\mathfrak b}(-2,2,1)^T=0,
  \qquad
  \widetilde\lambda_{02,\mathfrak b}(0,0,-1)^T=-1.
\]

Thus the strongest true statement is:

- formal projected \(B^M\)-tower: the \(H^1\) Bianchi transport class is zero;
- current checkout: no such tower is constructed, and even the \(N=2\)
  Bianchi counterterm is obstructed in the supplied finite-row habitat;
- next theorem datum: construct \(B^M\), \(\pi_{M,N}\mathfrak b^M\), and
  primitive transport, or prove the resulting obstruction class nonzero after
  those maps are supplied.

## Class Definition

Let \((\mathcal K^\bullet_{\theta_3,M},d_M,\pi_{M,N})\) be a proposed
inverse system of scalar-zero non-scalar finite-window complexes, with
\(\pi_{N,P}\pi_{M,N}=\pi_{M,P}\) and \(d_N\pi_{M,N}=\pi_{M,N}d_M\).  Let
\(\mathfrak b^M\in Z^1(\mathcal K^\bullet_{\theta_3,M})\) be the
Hom-valued Bianchi row attached to the lower source-coordinate primitive.

For \(M\geq N\), define
\[
  \Delta^1_{M,N}
  =
  -\pi_{M,N}\mathfrak b^M+\mathfrak b^N
  \in Z^1(\mathcal K^\bullet_{\theta_3,N}).
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
Equivalently, it is the Roos coboundary of the row family
\(([\mathfrak b^M])_M\).  It vanishes at the \(H^1\) gate exactly when
there are degree-zero correction cochains
\[
  H^{M,N}\in \mathcal K^0_{\theta_3,N}
\]
with
\[
  d_NH^{M,N}
  =
  -\pi_{M,N}\mathfrak b^M+\mathfrak b^N.
\]
After choosing such \(H^{M,N}\), a \(B\)-primitive family has the secondary
degree-zero Roos class
\[
  \operatorname{ob}^0_B
  =
  \bigl([\pi_{M,N}B^M-B^N-H^{M,N}]\bigr)
  \in
  \varprojlim\nolimits^1_M H^0(\mathcal K^\bullet_{\theta_3,M}).
\]

If \(H^{M,N}\) is chosen to be \(\pi_{M,N}B^M-B^N\), then the secondary
representative is zero.  This choice is available only after the \(B^M\)
tower and its primitive projection maps exist.

## Source Rows

The lower source-coordinate candidate is
\[
  \zeta^0_2=u_{a,H_{1,0}}u_{b,H_{0,1}},
  \qquad
  D^2_{02,20}=K^2_{\Theta_3}(\zeta^0_2).
\]
At \(N=2\),
\[
  d_{\mathrm{CE}}\zeta^0_2
  =
  2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}}.
\]
The Hom-valued Bianchi row is
\[
  \mathfrak b^2_{02,20}
  =
  d_{\mathrm{ns},2}K^2_{\Theta_3}(\zeta^0_2)
  -
  K^2_{\Theta_3}(d_{\mathrm{CE}}\zeta^0_2).
\]
Hence
\[
  d_{\mathrm{ns},2}D^2_{02,20}
  =
  -2E^2_{\nu_{02}}+2E^2_{\nu_{20}}
  +\mathfrak b^2_{02,20}.
\]
In the ordered lower basis
\[
  (E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20}),
\]
the present column, lower residual, and desired Bianchi target are
\[
  A_D^2=(-2,2,1)^T,\qquad
  r_2=(2,-2,0)^T,\qquad
  A_B^2=(0,0,-1)^T.
\]

For \(M\geq3\), the tested source-algebraic companion row has coordinates
\[
  (2,-2,3,2,-1,1,-2,-3)
\]
on
\[
  E_{\nu_{02}},E_{\nu_{20}},E_{\nu_{03}},
  E_{\nu_{12}^{(1)}},E_{\nu_{12}^{(2)}},
  E_{\theta_3},E_{\nu_{21}^{(2)}},E_{\nu_{30}}.
\]
This is not a Bianchi counterterm.  It is the monomial source-face table
whose marked Costello incidence/weight lift is still missing.

## Transition Maps

The source-face transition map currently supplied by the script is the
diagonal cutoff
\[
  v^{M,N}_{\nu;\nu'}
  =
  \begin{cases}
    1,&\nu=\nu'\text{ and }\deg(\nu)\leq N,\\
    0,&\text{otherwise}.
  \end{cases}
\]
It satisfies the cocycle identity.  For \(M\geq3\) and \(N=2\), it sends the
eight-face vector to
\[
  2E^2_{\nu_{02}}-2E^2_{\nu_{20}}.
\]
It does not supply a Bianchi-row transition
\[
  \pi_{M,N}\mathfrak b^M
  =
  \mathfrak b^N,
\]
nor a correction
\[
  H^{M,N}\quad\text{with}\quad
  d_NH^{M,N}
  =
  -\pi_{M,N}\mathfrak b^M+\mathfrak b^N.
\]

The strict positive target for a \(B\)-tower is the matrix identity
\[
  T^{M,N}A^M=A^NP^{M,N}
\]
with
\[
  T^{M,N}r^M=r^N,\qquad
  T^{M,N}\mathfrak b^M=\mathfrak b^N,
\]
and
\[
  P^{M,N}D^M=D^N,\qquad
  P^{M,N}B^M=B^N.
\]
If these strict maps are supplied, then
\[
  \Delta^1_{M,N}=0
\]
on the nose, so the \(H^1\) Bianchi transport class vanishes.  If strict
Bianchi-row transport fails but a projected \(B^M\)-family exists, then
\[
  H_B^{M,N}:=\pi_{M,N}B^M-B^N
\]
is the explicit \(H^1\)-gate correction.

## Why The Current Data Do Not Decide The Class

The obstruction reports supply only the lower row
\(\mathfrak b^2_{02,20}\) and the one current degree-zero column
\(D^2_{02,20}\).  They do not supply the rows
\(\mathfrak b^M\) in a common marked Costello row basis for all \(M\), nor
the projection coordinates of these rows to lower windows.

Consequently, the expression
\[
  -\pi_{M,N}\mathfrak b^M+\mathfrak b^N
\]
is the exact class to construct, but its coordinate vector is not a current
checkout datum.  The already tested diagonal source-face transport controls
the source rows \(E^M_{\Theta_3,\nu}\), not the Hom-valued Bianchi rows.
Replacing the missing Bianchi transition by the source-face diagonal
transport would be a false proof.

At \(N=2\), the class fails even earlier: the formal target
\[
  d_{\mathrm{ns},2}B^2_{02,20}
  =
  -\mathfrak b^2_{02,20}
\]
requires the missing column \(A_B^2=(0,0,-1)^T\).  The current habitat has
only \(A_D^2=(-2,2,1)^T\), so
\[
  \widetilde\lambda_{02,\mathfrak b}A_D^2=0,\qquad
  \widetilde\lambda_{02,\mathfrak b}A_B^2=-1.
\]
Thus there is no actual \(B^2\) from which to form a projected tower.

## Insertion Blocks

These blocks are report-only insertion targets.  They were not applied.

### H1 Transport Class

```tex
\begin{defn}[Bianchi transport class for the lower \(\theta_3\) row]
  Let \((\mathcal K^\bullet_{\theta_3,M},d_M,\pi_{M,N})\) be a finite-window
  inverse system of scalar-zero local-functional complexes, and let
  \(\mathfrak b^M\in Z^1(\mathcal K^\bullet_{\theta_3,M})\) be the
  Hom-valued Bianchi row of the lower source-coordinate primitive.  For
  \(M\geq N\) set
  \[
    \Delta^1_{M,N}
    =
    -\pi_{M,N}\mathfrak b^M+\mathfrak b^N .
  \]
  The first transport obstruction is
  \[
    \operatorname{ob}^1_{\mathfrak b}
    =
    \bigl([\Delta^1_{M,N}]\bigr)_{M\geq N}
    \in
    C^1_{\mathrm{Roos}}
    \bigl(H^1(\mathcal K^\bullet_{\theta_3,\bullet})\bigr).
  \]
  It vanishes at the \(H^1\) gate exactly when there are
  \(H^{M,N}\in\mathcal K^0_{\theta_3,N}\) with
  \(d_NH^{M,N}=\Delta^1_{M,N}\), coherently in the Roos complex.
\end{defn}
```

### Formal Tower Kill

```tex
\begin{lem}[Formal \(B\)-tower kills the \(H^1\) Bianchi class]
  Suppose a finite-window tower contains degree-zero local functionals
  \(B^M\) and chain maps \(\pi_{M,N}\) such that
  \[
    d_MB^M=-\mathfrak b^M .
  \]
  Then
  \[
    -\pi_{M,N}\mathfrak b^M+\mathfrak b^N
    =
    d_N(\pi_{M,N}B^M-B^N).
  \]
  Hence the \(H^1\) Bianchi transport class is zero, with explicit
  correction \(H_B^{M,N}=\pi_{M,N}B^M-B^N\).  This lemma is formal: it does
  not construct \(B^M\), the scalar-zero value, locality, or the projection
  coordinates.
\end{lem}
```

### Current Checkout Gate

```tex
\begin{rmk}[Current lower-window obstruction]
  In the current Bianchi-exposed \(N=2\) lower habitat the only
  degree-zero column is
  \(D^2_{02,20}=K^2_{\Theta_3}(\zeta^0_2)\), with
  \[
    A_D^2=(-2,2,1)^T
  \]
  in the basis
  \((E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20})\).  The desired
  Bianchi-counterterm target is
  \[
    A_B^2=(0,0,-1)^T.
  \]
  The covector
  \[
    \widetilde\lambda_{02,\mathfrak b}
    =
    \frac12(E^2_{\nu_{02}})^*
    +(\mathfrak b^2_{02,20})^*
  \]
  kills \(A_D^2\) and evaluates to \(-1\) on \(A_B^2\).  Thus no
  \(B^2_{02,20}\) exists in the current finite-row habitat.  The
  inverse-system \(H^1\) Bianchi class is therefore a construction target,
  not a computed zero class in the current checkout.
\end{rmk}
```

## Verification

Read anchors:

- `CLAUDE.md`
- `AGENTS.md`
- `~/ecosystem/INVARIANTS.md:129-170`
- `~/ecosystem/AGENTS-HARNESS.md:143-158`
- `.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `preamble.tex`
- `commands.tex`
- `mathmacros.tex`
- `notation.tex`
- `nomenclature.tex`
- `main.tex:8588-8905`
- `theorem-lanes.tex:3330-3578`
- `open-obligations.tex:720-895`
- `scripts/finite_window_graph_array.py:430-560`
- `scripts/finite_window_graph_array.py:982-2039`
- `reconstitution/theta3-roos-transport-obstruction-push-2026-04-30.md`
- `reconstitution/theta3-actual-local-functional-b-column-construction-push-2026-04-30.md`
- `reconstitution/theta3-bianchi-counterterm-construction-push-2026-04-30.md`
- `reconstitution/theta3-bianchi-defect-closure-push-2026-04-30.md`
- `reconstitution/theta3-bianchi-matrix-integration-spec-2026-04-30.md`
- `reconstitution/theta3-no-counterterm-controlled-enlargement-integration-spec-2026-04-30.md`
- `reconstitution/theta3-nondiagonal-transport-counterterm-construction-push-2026-04-30.md`
- `reconstitution/theta3-controlled-enlargement-witness-search-2026-04-30.md`
- `reconstitution/theta3-marked-source-hom-companion-repair-push-2026-04-30.md`
- `reconstitution/theta3-ce-ancestor-counterterm-witness-construction-push-2026-04-30.md`
- `reconstitution/theta3-source-to-construction-spec-2026-04-30.md`
- `reconstitution/theta3-companion-face-construction-attempt-2026-04-30.md`
- `reconstitution/theta3-acceptance-gate-consistency-2026-04-30.md`

Commands run:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py
python3 - <<'PY'
# focused theta3 row, eight-face, Bianchi matrix, and formal H1 witness check
PY
git status --short
```

Decisive focused output:

```text
theta_3_current_finite_row_subcomplex primitive_exists= False ell_r= 1 deg0= ()
theta3_counterterm_without_differential_entry accepted= False dC= 0 missing= ('differential entry dC=-E',)
theta3_counterterm_supplied_exact_payload accepted= True dC= -1 missing= ()
eight_face_accepted= False
eight_face_vector= (('E_nu02', '2'), ('E_nu20', '-2'), ('E_nu03', '3'), ('E_nu12_1', '2'), ('E_nu12_2', '-1'), ('E_theta_3', '1'), ('E_nu21_2', '-2'), ('E_nu30', '-3'))
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

The `git status --short` scan showed many pre-existing staged, modified, and
untracked files from the concurrent swarm.  This report touched only the two
Agent 304 owned reconstitution paths.

## Files Changed

- `reconstitution/theta3-h1-bianchi-transport-class-construction-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-304-theta3-h1-bianchi-transport-class-construction.md`
