# Agent 344: Non-Scalar QME Patch Blueprint

Status: report-only.  No TeX, script, figure, bibliography, PDF, or build
artifact was edited.

## Verdict

The next non-scalar QME construction target is not the full Costello graph/QME
theorem.  It is the finite-window \(\theta_3\) Bianchi counterterm-column
criterion:
\[
  B^M_{02,20}\in\mathcal K^0_{\mathrm{ns},M}(I),\qquad
  d_{\mathrm{ns},M}B^M_{02,20}=-\mathfrak b^M,
  \qquad
  \widehat\sigma_{\mathrm{sc},M}(B^M_{02,20})=0,
\]
with regular-density or graphwise wavefront admissibility, compatible
finite-window transport, and zero secondary Roos class.  This converts the
formal lower \(A_B=(0,0,-1)^T\) target into an accepted local-functional
theorem surface.  It does not construct the all-graph curved kernel
\(\operatorname{Curv}(\kappa+C)=0\).

## Source Anchors

- `reconstitution/swarm-2026-04-30-agent-338-nonscalar-qme-next-supremum-plan.md`:
  next target is the scalar-zero Bianchi column, then tower transport.
- `main.tex:8616-8850`: non-scalar QME is a filtered local-functional
  vanishing problem after the scalar projection lift.
- `main.tex:8852-9121`: \(\theta_3\) acceptance gate, lower Bianchi matrix,
  missing \(B^2_{02,20}\) column, and \(\Delta^1_{M,N}\) transport gate.
- `appendix-unreduced-bv-qme.tex:2077-2246`: non-scalar kernel complex
  \(\mathcal K^\bullet_{\mathrm{ns},M}=\ker\widehat\sigma_{\mathrm{sc},M}\).
- `appendix-unreduced-bv-qme.tex:2248-2399`: generic finite-row criterion
  \(A^Mc=-r^M\), \(T^{M,N}A^M=A^NP^{M,N}\), and Roos \(H^0\) gate.
- `appendix-unreduced-bv-qme.tex:2501-2642`: appendix version of the lower
  \(\theta_3\) Bianchi-exposed gate.
- `open-obligations.tex:939-956`: the open target is already named, but not
  yet converted into a patch-grade theorem skeleton.
- `theorem-lanes.tex:3574-3611`: theorem lane records the target and transport
  cocycle, but not the full definition/theorem insertion.

## Main Patch

Insert in `main.tex` immediately after the proof of
`prop:theta-three-finite-window-acceptance-gate` and before
`prob:tate-coefficient-descendant-lift`, currently between
`main.tex:9121` and `main.tex:9123`.

### Definition Skeleton

```tex
\begin{defn}[\(\theta_3\) Bianchi counterterm-column datum]
\label{def:theta-three-bianchi-counterterm-column-datum}
  Fix the scalar-zero finite-window non-scalar kernel
  \[
    \mathcal K^\bullet_{\mathrm{ns},M}(I)
    =
    \ker\widehat\sigma_{\mathrm{sc},M}
  \]
  of Definition~\ref{def:app-nonscalar-kernel-row-complex}, in a native
  finite-window realization habitat of
  Definition~\ref{def:app-native-finite-window-realization-habitat}.
  A \(\theta_3\) Bianchi counterterm-column datum over the tower
  \(M\ge N\ge2\) consists of the following data.

  First, for every \(M\ge2\), the lower source-coordinate primitive
  \[
    \zeta^0_M=u_{a,H_{1,0}}u_{b,H_{0,1}},\qquad
    D^M_{02,20}=K^M_{\Theta_3}(\zeta^0_M),
  \]
  with
  \[
    d_{\mathrm{CE}}\zeta^0_M
      =
    2\zeta_{M,\nu_{02}}-2\zeta_{M,\nu_{20}} .
  \]
  Put
  \[
    \mathfrak b^M
      =
    d_{\mathrm{ns},M}K^M_{\Theta_3}(\zeta^0_M)
      -
    K^M_{\Theta_3}(d_{\mathrm{CE}}\zeta^0_M).
  \]
  Thus
  \[
    d_{\mathrm{ns},M}D^M_{02,20}
      =
    -2E^M_{\nu_{02}}+2E^M_{\nu_{20}}+\mathfrak b^M .
  \]

  Second, a degree-zero local functional
  \(B^M_{02,20}\in\mathcal K^0_{\mathrm{ns},M}(I)\) satisfying
  \[
    d_{\mathrm{ns},M}B^M_{02,20}=-\mathfrak b^M,\qquad
    \widehat\sigma_{\mathrm{sc},M}(B^M_{02,20})=0 .
  \]
  The functional \(B^M_{02,20}\) must be represented by a regular-density
  graph counterterm or by a graphwise wavefront-admissible counterterm in
  the chosen finite row package; a formal column is not part of the datum.

  Third, for \(M\ge N\ge2\), transition data for rows and primitives.  Define
  \[
    \Delta^1_{M,N}:=-\pi_{M,N}\mathfrak b^M+\mathfrak b^N .
  \]
  The datum contains scalar-zero cochains \(H^{M,N}_{02,20}\in
  \mathcal K^0_{\mathrm{ns},N}(I)\) with
  \[
    d_{\mathrm{ns},N}H^{M,N}_{02,20}=\Delta^1_{M,N},
  \]
  where \(H^{M,N}_{02,20}=0\) in the strictly transported case.  The
  resulting degree-zero transport defect
  \[
    \Delta^0_{M,N}
      =
    \pi_{M,N}B^M_{02,20}
      -B^N_{02,20}
      -H^{M,N}_{02,20}
  \]
  is required to define the zero class in
  \[
    \varprojlim\nolimits^1_N
    H^0(\mathcal K^\bullet_{\mathrm{ns},N}(I)).
  \]
\end{defn}
```

### Theorem Skeleton

```tex
\begin{thm}[Finite-window \(\theta_3\) Bianchi counterterm column]
\label{thm:theta-three-bianchi-counterterm-column}
  Suppose a \(\theta_3\) Bianchi counterterm-column datum exists in the
  sense of Definition~\ref{def:theta-three-bianchi-counterterm-column-datum}.
  Then the lower transported \(\theta_3\) residual is killed in every finite
  window by the scalar-zero local functional
  \[
    P^M_{02,20}=D^M_{02,20}+B^M_{02,20}.
  \]
  More precisely,
  \[
    d_{\mathrm{ns},M}P^M_{02,20}
      =
    -2E^M_{\nu_{02}}+2E^M_{\nu_{20}} .
  \]
  In the \(N=2\) Bianchi-exposed basis
  \[
    (E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20}),
  \]
  the boundary matrix for the two columns \(D^2_{02,20},B^2_{02,20}\) is
  \[
    A^2_{D,B}
    =
    \begin{pmatrix}
      -2&0\\
       2&0\\
       1&-1
    \end{pmatrix},
    \qquad
    r_2=(2,-2,0)^T,
  \]
  and \(c=(1,1)^T\) solves \(A^2_{D,B}c=-r_2\).

  If the transport correction equations of
  Definition~\ref{def:theta-three-bianchi-counterterm-column-datum} hold and
  the secondary Roos class vanishes, the family \(P^M_{02,20}\) is a
  compatible finite-window primitive.  Consequently the lower \(\theta_3\)
  Bianchi residual is no longer an obstruction in the supplied finite-row
  tower.
\end{thm}
```

### Proof Skeleton

Use this proof architecture.

1. Start from the defining identity for the Hom-valued Bianchi defect:
   \[
     d_{\mathrm{ns},M}D^M_{02,20}
     =
     K^M_{\Theta_3}(d_{\mathrm{CE}}\zeta^0_M)+\mathfrak b^M
     =
     -2E^M_{\nu_{02}}+2E^M_{\nu_{20}}+\mathfrak b^M .
   \]
2. Add the new column:
   \[
     d_{\mathrm{ns},M}(D^M_{02,20}+B^M_{02,20})
     =
     -2E^M_{\nu_{02}}+2E^M_{\nu_{20}} .
   \]
   This proves the fixed-window claim.
3. In \(N=2\), display the matrix \(A^2_{D,B}\) and verify
   \(A^2_{D,B}(1,1)^T=(-2,2,0)^T=-r_2\).
4. For \(M\ge N\), compute
   \[
     d_{\mathrm{ns},N}
     (\pi_{M,N}B^M_{02,20}-B^N_{02,20})
     =
     -\pi_{M,N}\mathfrak b^M+\mathfrak b^N
     =
     \Delta^1_{M,N}.
   \]
   If \(H^{M,N}_{02,20}\) kills \(\Delta^1_{M,N}\), then
   \(\Delta^0_{M,N}\) is closed.
5. The zero class of \(\Delta^0\) in
   \(\varprojlim^1H^0(\mathcal K^\bullet_{\mathrm{ns},N}(I))\) is exactly
   the primitive-compatibility condition from
   Theorem~\ref{thm:app-constructive-nonscalar-costello-qme-realization}.
6. End with a boundary sentence:
   this theorem solves only the lower \(\theta_3\) Bianchi counterterm
   column in the supplied finite row tower; it does not supply a CE ancestor
   for \(\zeta_{M,\nu_3}\), a complete companion-face table, the centrality
   homotopies, or the full curved bulk-to-defect kernel.

## Open-Obligations Patch

Insert in `open-obligations.tex` inside the item
`Componentwise quantum coefficient surface and non-scalar obstruction
complex`, immediately after the current paragraph ending "The tested finite
routes do not close the row.", currently after `open-obligations.tex:956` and
before the next item `Unreduced factorization-current lift`.

Patch block:

```tex
  The next positive construction target is now the
  \(\theta_3\) Bianchi counterterm-column theorem.  It is accepted only if a
  finite-window local-functional package supplies, for every \(M\ge2\),
  \[
    B^M_{02,20}\in\mathcal K^0_{\mathrm{ns},M}(I),\qquad
    d_{\mathrm{ns},M}B^M_{02,20}=-\mathfrak b^M,\qquad
    \widehat\sigma_{\mathrm{sc},M}(B^M_{02,20})=0,
  \]
  with a regular-density or graphwise wavefront-admissible representative.
  The \(N=2\) acceptance matrix is
  \[
    A^2_{D,B}
    =
    \begin{pmatrix}
      -2&0\\
       2&0\\
       1&-1
    \end{pmatrix},
    \qquad
    A^2_{D,B}(1,1)^T=-r_2 .
  \]
  In the tower the Bianchi transport class
  \[
    \Delta^1_{M,N}:=-\pi_{M,N}\mathfrak b^M+\mathfrak b^N
  \]
  must be killed by an explicit scalar-zero correction
  \(H^{M,N}_{02,20}\) with
  \(d_{\mathrm{ns},N}H^{M,N}_{02,20}=\Delta^1_{M,N}\), and the resulting
  closed defect
  \[
    \pi_{M,N}B^M_{02,20}-B^N_{02,20}-H^{M,N}_{02,20}
  \]
  must define zero in
  \(\varprojlim^1_NH^0(\mathcal K^\bullet_{\mathrm{ns},N}(I))\).
  Without these entries the manuscript must retain the cokernel certificate
  \(\widetilde\lambda_{02,\mathfrak b}\); with them, the lower Bianchi row is
  a solved finite-window counterterm column, not a full Costello/QME theorem.
```

## Theorem-Lanes Patch

Insert in `theorem-lanes.tex` after the paragraph ending
"\(\varprojlim^1H^0\) primitive-compatibility class; otherwise the Bianchi
row remains obstructed.", currently after `theorem-lanes.tex:3611`.  Place it
before the paragraph beginning "For any larger package..." at
`theorem-lanes.tex:3612`.

Patch block:

```tex
    The first patch-grade positive theorem to add here is the
    \(\theta_3\) Bianchi counterterm-column criterion.  A controlled
    enlargement is accepted when it supplies local functionals
    \(B^M_{02,20}\in\mathcal K^0_{\mathrm{ns},M}(I)\) with
    \[
      d_{\mathrm{ns},M}B^M_{02,20}=-\mathfrak b^M,\qquad
      \widehat\sigma_{\mathrm{sc},M}(B^M_{02,20})=0,
    \]
    regular-density or graphwise wavefront admissibility, and compatible
    row/primitive transport.  Then
    \[
      P^M_{02,20}=D^M_{02,20}+B^M_{02,20}
    \]
    satisfies
    \[
      d_{\mathrm{ns},M}P^M_{02,20}
      =
      -2E^M_{\nu_{02}}+2E^M_{\nu_{20}}.
    \]
    At \(N=2\), this is the matrix identity
    \[
      \begin{pmatrix}
        -2&0\\
         2&0\\
         1&-1
      \end{pmatrix}
      \binom{1}{1}
      =
      (-2,2,0)^T=-r_2 .
    \]
    The theorem lane must still require the two tower gates
    \[
      \Delta^1_{M,N}
      =
      -\pi_{M,N}\mathfrak b^M+\mathfrak b^N
      =
      d_{\mathrm{ns},N}H^{M,N}_{02,20}
    \]
    and
    \[
      [\pi_{M,N}B^M_{02,20}-B^N_{02,20}-H^{M,N}_{02,20}]
      =
      0
      \quad\text{in}\quad
      \varprojlim\nolimits^1_N
      H^0(\mathcal K^\bullet_{\mathrm{ns},N}(I)).
    \]
```

If the lane should be more legible, split the current long
`Finite-window arrays and the minimal full-equivariant branch` item: keep the
minimal branch and one-row \(\theta_3\) obstruction in that item, then add a
new sibling item
`\item \emph{\(\theta_3\) Bianchi counterterm column.}` containing the block
above.

## Acceptance Checklist

A later TeX patch should be rejected unless it supplies all of the following.

- Scalar gate already formed: \(\widehat\sigma_{\mathrm{sc},M}\) is a
  filtered chain map on the chosen finite graph/counterterm habitat.
- Actual local functional: \(B^M_{02,20}\) is a Costello-local regular-density
  or graphwise wavefront-admissible counterterm, not only the formal vector
  \((0,0,-1)^T\).
- Boundary column:
  \(d_{\mathrm{ns},M}B^M_{02,20}=-\mathfrak b^M\).
- Scalar-zero:
  \(\widehat\sigma_{\mathrm{sc},M}(B^M_{02,20})=0\).
- Matrix closure at \(N=2\):
  \(A^2_{D,B}(1,1)^T=-r_2\).
- Bianchi transport:
  \(\Delta^1_{M,N}=-\pi_{M,N}\mathfrak b^M+\mathfrak b^N\) is an explicit
  \(d_{\mathrm{ns},N}\)-boundary.
- Secondary Roos gate:
  \([\pi B^M-B^N-H^{M,N}]=0\) in
  \(\varprojlim^1H^0(\mathcal K^\bullet_{\mathrm{ns}})\).
- Claim boundary:
  the statement says "finite-window \(\theta_3\) Bianchi column", not "full
  non-scalar Costello graph/QME construction".

## Attack-Heal Audit

Attack.  The present manuscript already proves the exact obstruction in the
current finite-row habitat:
\[
  \mathcal H^0_{\mathrm{cur}}=\C D^2_{02,20},\qquad
  A_D^2=(-2,2,1)^T,\qquad
  r_2=(2,-2,0)^T.
\]
The cokernel
\[
  \widetilde\lambda_{02,\mathfrak b}
  =
  \frac12(E^2_{\nu_{02}})^*+(\mathfrak b^2_{02,20})^*
\]
kills \(A_D^2\), detects \(r_2\), and detects the desired \(B\)-target:
\[
  \widetilde\lambda_{02,\mathfrak b}A_D^2=0,\qquad
  \widetilde\lambda_{02,\mathfrak b}(r_2)=1,\qquad
  \widetilde\lambda_{02,\mathfrak b}((0,0,-1)^T)=-1.
\]
Thus a patch that merely names \(B^2_{02,20}\) is false.

Heal.  The proposed theorem makes \(B^M_{02,20}\) an actual supplied
local-functional counterterm, requires scalar-zero and locality data, and
passes the tower through \(\Delta^1_{M,N}\) and the secondary Roos class.
This is the strongest true next theorem surface.  It upgrades the lower
finite-window \(\theta_3\) row only after the missing column is built, and it
does not demote the larger non-scalar QME theorem.

## Verification

Read:

- `CLAUDE.md`
- `AGENTS.md`
- `/Users/raeez/ecosystem/INVARIANTS.md` section IV
- `/Users/raeez/ecosystem/AGENTS-HARNESS.md` section VIII
- `/Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex`
- `/Users/raeez/chiral-bar-cobar-vol2/metadata/theorem_registry.md`
- `reconstitution/swarm-2026-04-30-agent-338-nonscalar-qme-next-supremum-plan.md`
- `main.tex`, `appendix-unreduced-bv-qme.tex`, `open-obligations.tex`,
  `theorem-lanes.tex`, `claim-strength-ledger.tex` at the anchors listed
  above
- theta3 reports by Agents 277, 282, 294, 299, 313, 322, and 332

No PDF build was run; this task is a report-only blueprint.

Command run after writing:

```bash
git diff --no-index --check /dev/null \
  reconstitution/swarm-2026-04-30-agent-344-nonscalar-qme-patch-blueprint.md
```

Result: no whitespace or conflict-marker warnings.  The direct no-index diff
returns status \(1\) because `/dev/null` and the report differ; the normalized
check treated status \(1\) with empty output as success.
