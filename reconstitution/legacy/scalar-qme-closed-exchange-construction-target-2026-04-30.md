# Scalar QME Closed-Exchange Construction Target

Date: 2026-04-30.

Scope: ordinary scalar-reduced \(\mathfrak{gl}_N\) brane-defect QME
branch.  This file is a construction target and obstruction theorem for
the closed-exchange repair.  It does not modify the manuscript.

## Stable Core

The ordinary scalar-reduced \(\mathfrak{gl}_N\) branch has scalar QME
class
\[
  [\operatorname{Ob}_{\mathrm{sc}}]
    =
  \hbar N[\bar c]
  \in H^2_{\mathrm{Lie}}(\bar A;\C)[[\hbar]],
  \qquad \bar A=\C[z_1,z_2]/\C\cdot 1.
\]
Here
\[
  \bar c(f,g)=\omega(f,g)=[\{f,g\}]_0,
  \qquad \omega(z_1,z_2)=1.
\]
The class is nonzero in the scalar-reduced source.  Therefore an
internal ordinary scalar counterterm cannot kill it.  A closed-exchange
repair in the same ordinary reduced branch must supply a genuine
opposite scalar class
\[
  [w_{\mathrm{cl}}]=-\hbar N[\bar c].
\]
If the closed-exchange datum is absent, exact, incompatible with scalar
projection, or incompatible in the finite-window inverse system, the
ordinary scalar-reduced branch remains obstructed.

## Algebraic Source Extension

The algebraic source target is the central extension
\[
  \bar A^{\mathrm{cl}}_{-\hbar N\bar c}
  =
  \bar A\oplus \C K_{\mathrm{cl}}
\]
with bracket
\[
  [(f,aK_{\mathrm{cl}}),(g,bK_{\mathrm{cl}})]
  =
  \bigl(\{f,g\}_{\bar A},
        -\hbar N\,\bar c(f,g)K_{\mathrm{cl}}\bigr).
\]
This extension is not the same as the central-character unreduction.
It is an opposite closed source line added to the scalar-reduced branch.
Its only admissible scalar leading class is
\(-\hbar N[\bar c]\).  Changing the coefficient changes the obstruction
equation; an exact class gives no repair.

The source-extension datum is theorem-grade only after it is realized by
a Costello-local closed-exchange complex and a map into the brane-defect
QME obstruction complex.  Naming the central extension alone does not
construct a closed exchange.

## Closed-Exchange Complex

For every admissible weight \(w\), interval \(I\), and finite window
\(M\), a scalar closed-exchange repair must construct:
\[
  \mathcal X^\bullet_{\mathrm{sc},w,M}(I)
\]
with differential \(d^X_M\), truncation maps
\[
  \rho^X_{M,N}\colon
  \mathcal X^\bullet_{\mathrm{sc},w,M}(I)
  \to
  \mathcal X^\bullet_{\mathrm{sc},w,N}(I),
  \qquad M\geq N,
\]
and cochain maps
\[
  \Xi^{\mathrm{sc}}_M\colon
  \mathcal X^\bullet_{\mathrm{sc},w,M}(I)
  \to
  \mathfrak Q^\bullet_{\mathrm{sc},w,M}(I).
\]
The target \(\mathfrak Q^\bullet_{\mathrm{sc},w,M}(I)\) is the
finite-window scalar-contact part of the brane-defect local-functional
QME complex, with differential
\[
  d_M=Q+\{I^w_{0,M},-\}_{\hbar,M}.
\]
It is the transported finite-window object, not a naive degree
truncation.

The maps must satisfy:
\[
  \pi_{M,N}\Xi^{\mathrm{sc}}_M
    =
  \Xi^{\mathrm{sc}}_N\rho^X_{M,N},
\]
and must commute with admissible weight transport \(R^M_{w,w'}\).

## Scalar-Contact Projection Gate

The branch is meaningful only after choosing a filtered chain scalar
projection
\[
  \widehat\sigma_{\mathrm{sc},M}\colon
  \mathfrak Q^\bullet_{\mathrm{sc},w,M}(I)
  \to
  \mathcal S^\bullet_M(I),
\]
where
\[
  \mathcal S^\bullet_M(I)
  =
  C^\bullet_{\mathrm{Lie}}
  (\bar A_{\mathrm{fw},M};\C\gamma_{\mathbf 1})[1][[\hbar]]
\]
denotes the finite-window scalar-symbol target induced by the same
truncation machinery.  The notation \(\bar A_{\mathrm{fw},M}\) means the
transported finite-window scalar CE source; it is not the naive subspace
of polynomials of degree \(\leq M\) unless that subspace has already been
proved closed under the transported bracket.

The projection must obey
\[
  \widehat\sigma_{\mathrm{sc},M}d_M
    =
  d_{\mathrm{CE}}\widehat\sigma_{\mathrm{sc},M},
\]
\[
  \widehat\sigma_{\mathrm{sc},M}
  (\operatorname{Ob}_{\mathrm{sc},M})
    =
  \hbar N\,\bar c_M,
\]
and
\[
  \widehat\sigma_{\mathrm{sc},M}
  \Xi^{\mathrm{sc}}_M(W_M)
    =
  -\hbar N\,\bar c_M+d_{\mathrm{CE}}\eta_M
\]
for the chosen closed-exchange cocycle \(W_M\).  Thus the scalar leading
class is forced:
\[
  H^1(\widehat\sigma_{\mathrm{sc},M}\Xi^{\mathrm{sc}}_M)[W_M]
    =
  -\hbar N[\bar c_M].
\]

Any non-scalar component of \(\Xi^{\mathrm{sc}}_M(W_M)\) lies in
\(\ker\widehat\sigma_{\mathrm{sc},M}\) and is governed by the separate
non-scalar QME obstruction tower.  The scalar branch may not hide a
non-scalar residual.

## Fixed-Window Criterion

At a fixed window \(M\), the ordinary scalar branch closes by
closed exchange if and only if there are
\[
  W_M\in Z^1(\mathcal X^\bullet_{\mathrm{sc},w,M}(I)),
  \qquad
  C_M\in \mathfrak Q^0_{\mathrm{sc},w,M}(I)
\]
such that
\[
  \operatorname{Ob}_{\mathrm{sc},M}
    +\Xi^{\mathrm{sc}}_M(W_M)+d_MC_M=0.
\]
Equivalently, the scalar cohomology class satisfies
\[
  [\operatorname{Ob}_{\mathrm{sc},M}]
  \in
  -\operatorname{im}\!\left(
    H^1(\Xi^{\mathrm{sc}}_M)\colon
    H^1(\mathcal X^\bullet_{\mathrm{sc},w,M}(I))
    \to
    H^1(\mathfrak Q^\bullet_{\mathrm{sc},w,M}(I))
  \right),
\]
and after applying \(\widehat\sigma_{\mathrm{sc},M}\) this condition
contains the required equation
\[
  H^1(\widehat\sigma_{\mathrm{sc},M}\Xi^{\mathrm{sc}}_M)[W_M]
  =
  -\hbar N[\bar c_M].
\]

Failure at this stage is the fixed-window scalar closed-exchange
obstruction
\[
  \beta^{\mathrm{sc}}_{M}
  =
  \left[
    \hbar N[\bar c_M]
  \right]
  \in
  \operatorname{coker}
  H^1(\widehat\sigma_{\mathrm{sc},M}\Xi^{\mathrm{sc}}_M).
\]
If \(\beta^{\mathrm{sc}}_M\neq0\), no local counterterm can repair that
window in the ordinary reduced branch.

## Finite-Window and Roos Conditions

In the inverse system, put
\[
  \beta^{\mathrm{sc}}_{\mathrm{cl}}
  =
  \left[
    \bigl(\hbar N[\bar c_M]\bigr)_M
  \right]
  \in
  \operatorname{coker}\!\left(
    \varprojlim_M H^1(\mathcal X^\bullet_{\mathrm{sc},w,M}(I))
    \xrightarrow{\ \varprojlim H^1(\widehat\sigma_{\mathrm{sc},M}
      \Xi^{\mathrm{sc}}_M)\ }
    \varprojlim_M H^1(\mathcal S^\bullet_M(I))
  \right).
\]
Vanishing of \(\beta^{\mathrm{sc}}_{\mathrm{cl}}\) is equivalent to an
inverse-system cohomology class \(\alpha=(\alpha_M)_M\) whose scalar
image is \(-\hbar N[\bar c_M]\) in every window.

This is still not a chain-level closed-exchange kernel.  Choose cocycle
representatives \(w_M\) for \(\alpha_M\).  Their representative
compatibility obstruction is the Roos class
\[
  \mu^{\mathrm{sc}}_{\mathrm{cl}}(\alpha)
  \in
  \varprojlim\nolimits^1_M
  H^0(\mathcal X^\bullet_{\mathrm{sc},w,M}(I)),
\]
represented by \(u_M\) satisfying
\[
  \rho^X_{M+1,M}w_{M+1}-w_M=d^X_Mu_M.
\]
After compatible \(W_M\) are chosen, the counterterm primitive
compatibility obstruction is
\[
  \lambda^{\mathrm{sc}}_{\mathrm{cl}}(W)
  \in
  \varprojlim\nolimits^1_M
  H^0(\mathfrak Q^\bullet_{\mathrm{sc},w,M}(I)),
\]
represented by
\[
  [\pi_{M+1,M}c_{M+1}-c_M],
  \qquad
  d_Mc_M=-(\operatorname{Ob}_{\mathrm{sc},M}
      +\Xi^{\mathrm{sc}}_M(W_M)).
\]

The ordinary scalar-reduced closed-exchange branch closes exactly when
\[
  \beta^{\mathrm{sc}}_{\mathrm{cl}}=0,\qquad
  \mu^{\mathrm{sc}}_{\mathrm{cl}}=0,\qquad
  \lambda^{\mathrm{sc}}_{\mathrm{cl}}=0,
\]
with the scalar-contact projection identities above.  Mittag--Leffler
for the \(H^0(\mathcal X_{\mathrm{sc}})\) tower kills
\(\mu^{\mathrm{sc}}_{\mathrm{cl}}\).  Mittag--Leffler for the
\(H^0(\mathfrak Q_{\mathrm{sc}})\) tower kills
\(\lambda^{\mathrm{sc}}_{\mathrm{cl}}\).  Without those hypotheses, the
Roos classes are independent obstruction data.

## Alternatives

The central-character branch changes the source before scalar reduction.
On \(A=\C[z_1,z_2]\), the primitive
\[
  \eta(f)=-[f]_0
\]
satisfies \(d_{\mathrm{CE}}\eta=\omega\), and the character
\[
  \chi_N(f)=N[f]_0
\]
gives
\[
  \hbar N\omega+d_{\mathrm{CE}}(\hbar\chi_N)=0.
\]
This is a source replacement.  It is not a counterterm or a closed
exchange inside the original scalar-reduced ordinary branch.

The balanced supertrace branch changes the open model.  For
\(V=\C^{N|N}\),
\[
  \operatorname{sdim}V=\operatorname{Str}(\operatorname{id}_V)=0,
\]
so the scalar representative vanishes on the balanced scalar-contact
habitat.  This closes the scalar-contact branch on that habitat.  It is
not a proof that the ordinary \(\mathfrak{gl}_N\) scalar-reduced branch
has been repaired.

## Obstruction Theorem Target

The precise theorem target is:

Given the ordinary scalar-reduced \(\mathfrak{gl}_N\) brane-defect QME
complex, a closed-exchange scalar cancellation exists if and only if the
source extension \(\bar A^{\mathrm{cl}}_{-\hbar N\bar c}\), the
closed-exchange tower
\(\mathcal X^\bullet_{\mathrm{sc},w,M}(I)\), the cochain maps
\(\Xi^{\mathrm{sc}}_M\), the scalar-contact projections
\(\widehat\sigma_{\mathrm{sc},M}\), and compatible finite-window
representatives \(W_M,C_M\) are constructed with
\[
  [w_{\mathrm{cl}}]=-\hbar N[\bar c],
\]
\[
  \operatorname{Ob}_{\mathrm{sc},M}
    +\Xi^{\mathrm{sc}}_M(W_M)+d_MC_M=0,
\]
and
\[
  \beta^{\mathrm{sc}}_{\mathrm{cl}}
  =
  \mu^{\mathrm{sc}}_{\mathrm{cl}}
  =
  \lambda^{\mathrm{sc}}_{\mathrm{cl}}
  =
  0.
\]
If any one of these data fails, the result is the obstruction theorem:
the ordinary scalar-reduced \(\mathfrak{gl}_N\) QME branch remains
obstructed by the named nonzero scalar class or by the named finite-window
or Roos obstruction.
