# Theta3 Bianchi Matrix Integration Spec

Status: report-only manuscript integration specification.  No TeX file is
edited by this note.

## Source datum

Agent 270 isolates the lower-window source primitive
\[
  \zeta^0_2=u_{a,H_{1,0}}u_{b,H_{0,1}},
  \qquad
  D^2_{02,20}=K^2_{\Theta_3}(\zeta^0_2).
\]
The source CE differential is
\[
  d_{\mathrm{CE}}\zeta^0_2
  =
  2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}} .
\]
This is source exactness.  It is not yet local-functional exactness.

With \(E_\nu=-K_{\Theta_3}(\zeta_\nu)\), define the Hom-valued Bianchi
defect
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
Thus \(D^2_{02,20}\) kills the lower residual
\[
  r_2=2E^2_{\nu_{02}}-2E^2_{\nu_{20}}
\]
only after the Bianchi row is killed in the local-functional complex.

In the Bianchi-exposed lower basis
\[
  (E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20}),
\]
the candidate column and residual are
\[
  A_D^2=(-2,2,1)^T,\qquad r_2=(2,-2,0)^T .
\]
The equation \(A_D^2c=-r_2\) has no solution.  The first two coordinates
force \(c=1\), and the Bianchi coordinate then leaves residual \(1\).  The
normalized cokernel
\[
  \widetilde\lambda_{02,\mathfrak b}
  =
  \frac12(E^2_{\nu_{02}})^*
  +(\mathfrak b^2_{02,20})^*
\]
satisfies
\[
  \widetilde\lambda_{02,\mathfrak b}A_D^2=0,\qquad
  \widetilde\lambda_{02,\mathfrak b}(r_2)=1.
\]
This is the exact matrix obstruction.

## Integration invariant

The manuscript must distinguish:

1. Source exactness:
   \[
     d_{\mathrm{CE}}\zeta^0_2
     =
     2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}} .
   \]
2. Local-functional exactness:
   a scalar-zero local functional \(P^2_{02,20}\) in the finite-window
   Costello complex satisfies
   \[
     d_{\mathrm{ns},2}P^2_{02,20}
     =
     -2E^2_{\nu_{02}}+2E^2_{\nu_{20}},
   \]
   with locality or wavefront admissibility and compatible transport.

The candidate \(D^2_{02,20}\) proves only the first statement.  The second
requires one of:

1. \(\mathfrak b^2_{02,20}=0\), together with scalar-zero value and
   compatible transport for \(D^2_{02,20}\);
2. a scalar-zero local counterterm \(B^2_{02,20}\) with
   \[
     d_{\mathrm{ns},2}B^2_{02,20}=-\mathfrak b^2_{02,20},
   \]
   so that \(D^2_{02,20}+B^2_{02,20}\) is the local-functional primitive;
3. a marked non-diagonal transport or companion relation supplied from
   genuine Costello incidence, weight, lower-basis, and codimension-two
   closure data.

For primitive towers, add the Bianchi transport gate:
\[
  d_{\mathrm{ns},N}\bigl(\pi_{M,N}D^M-D^N\bigr)
  =
  \pi_{M,N}\mathfrak b^M_{\mathrm{cand}}
  -\mathfrak b^N_{\mathrm{cand}} .
\]
The Roos primitive class is closed only if the right side is zero or an
explicitly supplied boundary.

## `main.tex`

Current anchors:

- `main.tex:8332`: `prop:theta-three-finite-window-acceptance-gate`.
- `main.tex:8450-8472`: lower primitive candidate and Bianchi defect.
- `main.tex:8487-8500`: proof reduces primitives to \(A^Mc^M=-r^M\).

Replace the paragraph beginning at `main.tex:8450` and ending at
`main.tex:8472` by:

```tex
  The canonical lower source-coordinate candidate is
  \[
    \zeta^0_2=u_{a,H_{1,0}}u_{b,H_{0,1}},\qquad
    D^2_{02,20}
    =
    K^2_{\Theta_3}(\zeta^0_2),
  \]
  with source differential
  \[
    d_{\mathrm{CE}}\zeta^0_2
    =
    2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}}.
  \]
  This proves source exactness of the transported lower row.  It proves
  local-functional exactness only after the Hom-valued Bianchi defect
  \[
    \mathfrak b^2_{02,20}
    =
    d_{\mathrm{ns},2}K^2_{\Theta_3}(\zeta^0_2)
    -
    K^2_{\Theta_3}(d_{\mathrm{CE}}\zeta^0_2)
  \]
  is killed.  Indeed
  \[
    d_{\mathrm{ns},2}D^2_{02,20}
    =
    -2E^2_{\nu_{02}}+2E^2_{\nu_{20}}
    +\mathfrak b^2_{02,20}.
  \]
  In the Bianchi-exposed lower basis
  \[
    (E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20})
  \]
  the column of \(D^2_{02,20}\) and the residual are
  \[
    A_D^2=(-2,2,1)^T,\qquad r_2=(2,-2,0)^T .
  \]
  The equation \(A_D^2c=-r_2\) has no solution in this free presentation.
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
    \widetilde\lambda_{02,\mathfrak b}(r_2)=1.
  \]
  Thus the lower source primitive is a genuine local-functional primitive
  only in the quotient where \(\mathfrak b^2_{02,20}=0\), or after a
  scalar-zero local counterterm \(B^2_{02,20}\) with
  \(d_{\mathrm{ns},2}B^2_{02,20}=-\mathfrak b^2_{02,20}\) is supplied,
  with locality and transport compatibility.
```

Insert the following proof paragraph after `main.tex:8500` and before the
companion-face paragraph:

```tex
  The lower source-coordinate candidate illustrates the distinction between
  source exactness and local-functional exactness.  The source calculation
  gives \(d_{\mathrm{CE}}\zeta^0_2=2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}}\),
  but \(K^2_{\Theta_3}\) is not a chain map until its Hom-valued Bianchi
  defect is killed.  In the Bianchi-exposed basis the matrix equation is
  \(A_D^2c=-r_2\) with \(A_D^2=(-2,2,1)^T\) and \(r_2=(2,-2,0)^T\).
  The first two coordinates force \(c=1\), while the Bianchi coordinate
  forces \(c=0\).  Equivalently
  \(\widetilde\lambda_{02,\mathfrak b}A_D^2=0\) and
  \(\widetilde\lambda_{02,\mathfrak b}(r_2)=1\).  Hence the current
  checkout contains an exact obstruction certificate, not a completed
  local-functional counterterm.
```

Do not claim that \(D^2_{02,20}\) kills the \(N=2\) residual unless the
Bianchi row is killed or a \(B^2_{02,20}\) counterterm is supplied.

## `theorem-lanes.tex`

Current anchors:

- `theorem-lanes.tex:3300-3317`: one-row theta3 obstruction.
- `theorem-lanes.tex:3337-3369`: eight-face residual and lower transport.
- `theorem-lanes.tex:3370-3391`: lower primitive candidate and Bianchi defect.

Replace `theorem-lanes.tex:3370-3391` by the compact lane form:

```tex
    The canonical source-coordinate lower primitive candidate is
    \[
      \zeta^0_2=u_{a,H_{1,0}}u_{b,H_{0,1}},\qquad
      D^2_{02,20}=K^2_{\Theta_3}(\zeta^0_2),
      \qquad
      d_{\mathrm{CE}}\zeta^0_2
      =
      2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}}.
    \]
    This is source exactness.  In the local-functional complex
    \[
      d_{\mathrm{ns},2}D^2_{02,20}
      =
      -2E^2_{\nu_{02}}+2E^2_{\nu_{20}}
      +\mathfrak b^2_{02,20},
    \]
    where
    \[
      \mathfrak b^2_{02,20}
      =
      d_{\mathrm{ns},2}K^2_{\Theta_3}(\zeta^0_2)
      -
      K^2_{\Theta_3}(d_{\mathrm{CE}}\zeta^0_2).
    \]
    In the Bianchi-exposed lower basis
    \((E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20})\), the column
    and residual are
    \[
      A_D^2=(-2,2,1)^T,\qquad r_2=(2,-2,0)^T .
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
      \widetilde\lambda_{02,\mathfrak b}(r_2)=1.
    \]
    Thus the tested lower source primitive is source-exact but not
    local-functional-exact in the present Bianchi-exposed habitat.
```

Keep the existing three repair routes at `theorem-lanes.tex:3355-3369`, but
refine the lower primitive route to require either
\(\mathfrak b^2_{02,20}=0\) or a counterterm \(B^2_{02,20}\) with
\(d_{\mathrm{ns},2}B^2_{02,20}=-\mathfrak b^2_{02,20}\).  Also add the
non-diagonal transport equation as a required datum when that route is
named:
\[
  3v_3+2v_4-v_5+v_6-2v_7-3v_8=(-2,2)^T .
\]
This equation is solvable as abstract linear algebra but is not supplied by
the current source-coordinate projection, which sends the degree-three
columns to zero.

## `open-obligations.tex`

Current anchors:

- `open-obligations.tex:715-758`: theta3 one-row obstruction and accepted
  repair interfaces.
- `open-obligations.tex:779-832`: eight-face residual, lower transport, and
  lower primitive candidate.

Replace `open-obligations.tex:821-832` by:

```tex
  This is source exactness only.  Put
  \[
    \zeta^0_2=u_{a,H_{1,0}}u_{b,H_{0,1}},\qquad
    D^2_{02,20}=K^2_{\Theta_3}(\zeta^0_2),
  \]
  and
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
  In the Bianchi-exposed lower basis
  \[
    (E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20}),
  \]
  the matrix data are
  \[
    A_D^2=(-2,2,1)^T,\qquad r_2=(2,-2,0)^T,\qquad
    \widetilde\lambda_{02,\mathfrak b}
    =
    \frac12(E^2_{\nu_{02}})^*
    +(\mathfrak b^2_{02,20})^* .
  \]
  Since
  \[
    \widetilde\lambda_{02,\mathfrak b}A_D^2=0,\qquad
    \widetilde\lambda_{02,\mathfrak b}(r_2)=1,
  \]
  the lower source primitive is not local-functional exact in the present
  package.  The open repair is exactly one of:
  \(\mathfrak b^2_{02,20}=0\) with scalar-zero and transport checks;
  a scalar-zero local counterterm \(B^2_{02,20}\) satisfying
  \(d_{\mathrm{ns},2}B^2_{02,20}=-\mathfrak b^2_{02,20}\); or a genuine
  marked non-diagonal transport/codimension-two table satisfying the
  lower equation
  \(3v_3+2v_4-v_5+v_6-2v_7-3v_8=(-2,2)^T\).
```

Also add the primitive-transport obligation near this paragraph:

```tex
  For a tower \(D^M=K^M_{\Theta_3}(\zeta^0_M)\), the Roos primitive class
  is closed only after the Bianchi defects transport:
  \[
    d_{\mathrm{ns},N}(\pi_{M,N}D^M-D^N)
    =
    \pi_{M,N}\mathfrak b^M_{\mathrm{cand}}
    -\mathfrak b^N_{\mathrm{cand}}.
  \]
  Hence strict transport of \(\mathfrak b^M_{\mathrm{cand}}\), or an
  explicit boundary for the right side, is part of the obligation.
```

In this file, keep \(\lambda^{(2)}_{\nu_{02}}=\frac12(E^2_{\nu_{02}})^*\)
only as the empty-lower-primitive-slot certificate.  Once
\(D^2_{02,20}\) is adjoined and the Bianchi row is exposed, the correct
cokernel is \(\widetilde\lambda_{02,\mathfrak b}\).

## `claim-strength-ledger.tex`

Current anchors:

- `claim-strength-ledger.tex:459-474`: theta3 primitive and companion-face
  item.
- `claim-strength-ledger.tex:816-835`: theta3 row as model case in the QME
  ledger.

In the item at `claim-strength-ledger.tex:459`, replace the sentence
beginning "The eight-face companion attempt..." through the repair sentence
by:

```tex
  The eight-face companion attempt has nonzero coordinate row
  \((2,-2,3,2,-1,1,-2,-3)\) and its diagonal transport to \(N=2\)
  leaves \(2E_{\nu_{02}}^2-2E_{\nu_{20}}^2\).  The lower source primitive
  \(D^2_{02,20}=K^2_{\Theta_3}(u_{a,H_{1,0}}u_{b,H_{0,1}})\) proves only
  source exactness:
  \(d_{\mathrm{CE}}(u_{a,H_{1,0}}u_{b,H_{0,1}})
  =2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}}\).  In the local-functional
  Bianchi-exposed basis
  \((E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20})\), the column
  and residual are \(A_D^2=(-2,2,1)^T\) and \(r_2=(2,-2,0)^T\), detected by
  \(\widetilde\lambda_{02,\mathfrak b}
  =\frac12(E^2_{\nu_{02}})^*+(\mathfrak b^2_{02,20})^*\).
  Thus the current lower-window route is source-exact but not
  local-functional-exact.  A repair must add a controlled degree-zero local
  counterterm primitive, prove the Bianchi row zero, supply higher or
  marked CE-source rows with Hom-valued Bianchi cancellation, or construct a
  complete transport-compatible companion table with scalar-zero, signed
  residual zero, codimension-two closure, truncation cocycle, and zero Roos
  class.
```

In the model-case paragraph at `claim-strength-ledger.tex:816-835`, add:

```tex
  The lower source-coordinate primitive is not evidence for such a witness
  until its Hom-valued Bianchi row is killed.  In the Bianchi-exposed basis
  it has \(A_D^2=(-2,2,1)^T\), \(r_2=(2,-2,0)^T\), and cokernel
  \(\widetilde\lambda_{02,\mathfrak b}\) with
  \(\widetilde\lambda_{02,\mathfrak b}A_D^2=0\) and
  \(\widetilde\lambda_{02,\mathfrak b}(r_2)=1\).
```

## Claim-strength rules

Allowed:

- "The lower residual is source-exact in the CE source complex."
- "The Bianchi-exposed lower local-functional matrix is obstructed by
  \(\widetilde\lambda_{02,\mathfrak b}\)."
- "The validator rejection is correct for the current data-derived habitat."

Forbidden without new data:

- "The lower primitive \(D^2_{02,20}\) kills the \(N=2\) residual."
- "The theta3 row is repaired by the source primitive."
- "A local counterterm \(C_{\theta_3}\) exists."
- "The Roos primitive class is closed."

Admissible after new data:

- If \(\mathfrak b^2_{02,20}=0\), then \(D^2_{02,20}\) kills the lower
  residual, subject to scalar-zero and transport checks.
- If \(B^2_{02,20}\) satisfies
  \(d_{\mathrm{ns},2}B^2_{02,20}=-\mathfrak b^2_{02,20}\), then
  \(D^2_{02,20}+B^2_{02,20}\) is the lower local-functional primitive,
  subject to scalar-zero, locality, and transport checks.
- If marked non-diagonal transport is supplied, it must include the equation
  \(3v_3+2v_4-v_5+v_6-2v_7-3v_8=(-2,2)^T\), the projected weights, the
  lower row-basis reduction, and codimension-two closure.

## Verification

Matrix check:

```text
A_D= [-2, 2, 1]
r= [2, -2, 0]
ellA= 0
ellr= 1
coordinate_forced_c= [1, 1, 0]
residual_after_c1= [0, 0, 1]
```

Read anchors:

- `reconstitution/swarm-2026-04-30-agent-270-theta3-bianchi-defect-closure-push.md`
- `reconstitution/theta3-bianchi-defect-closure-push-2026-04-30.md`
- `main.tex:8332-8511`
- `theorem-lanes.tex:3298-3391`
- `open-obligations.tex:715-832`
- `claim-strength-ledger.tex:459-474`
- `claim-strength-ledger.tex:816-835`
