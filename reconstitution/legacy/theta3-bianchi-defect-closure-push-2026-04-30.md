# Theta3 Bianchi Defect Closure Push

Status: synthesis note for the report-only Agent 270 push.  No manuscript or
script file was edited.

## Decision

No complete theta3 repair is present in the current checkout.  The
lower-window source primitive is real, but it is not yet a local-functional
counterterm.  The exact obstruction is the Hom-valued Bianchi row.

Let
\[
  \zeta^0_2=u_{a,H_{1,0}}u_{b,H_{0,1}},
  \qquad
  D^2_{02,20}=K^2_{\Theta_3}(\zeta^0_2).
\]
The source CE calculation gives
\[
  d_{\mathrm{CE}}\zeta^0_2
  =
  2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}}.
\]
Since \(E_\nu=-K_{\Theta_3}(\zeta_\nu)\),
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
Thus \(D^2_{02,20}\) kills the transported lower residual precisely when
\(\mathfrak b^2_{02,20}=0\), or when a scalar-zero local counterterm
\(B^2_{02,20}\) with \(dB^2_{02,20}=-\mathfrak b^2_{02,20}\) is supplied.

## Exact Matrix

In the Bianchi-exposed lower row basis
\[
  (E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20}),
\]
the candidate column and residual are
\[
  A_D^2=(-2,2,1)^T,\qquad r_2=(2,-2,0)^T .
\]
The equation \(A_D^2c=-r_2\) has no solution in the free Bianchi-row
presentation.  The cokernel
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
This is the exact lower obstruction class.

## Transport Gate

The eight-face residual transports diagonally to
\[
  2E^2_{\nu_{02}}-2E^2_{\nu_{20}}.
\]
An abstract non-diagonal transport can kill it only if the degree-three
columns \(v_3,\ldots,v_8\) satisfy
\[
  3v_3+2v_4-v_5+v_6-2v_7-3v_8=(-2,2)^T.
\]
The present source-coordinate projection forces these degree-three columns
to zero.  A non-diagonal solution therefore requires extra marked Costello
transport data and lower row-basis reduction; it is not derivable from the
current finite-window graph array.

For primitive transport,
\[
  d_{\mathrm{ns},N}(\pi_{M,N}D^M-D^N)
  =
  \pi_{M,N}\mathfrak b^M-\mathfrak b^N.
\]
Thus the Roos primitive class is closed only after the Bianchi defects
transport strictly or by a supplied boundary.

## Strongest True Statement

The theta3 lower-window obstruction is source-exact but not
local-functional-exact in the current data-derived habitat.  A theorem-grade
repair must supply one of:

1. \(\mathfrak b^2_{02,20}=0\) with scalar-zero and transport checks for
   \(D^2_{02,20}\);
2. a local counterterm \(B^2_{02,20}\) with
   \(dB^2_{02,20}=-\mathfrak b^2_{02,20}\), scalar-zero value, locality, and
   compatible transport;
3. a non-diagonal marked transport satisfying the displayed matrix equation,
   together with the marked incidence/weight and codimension-two closure
   table.

Absent these data, the validator's rejection is correct.
