# Agent 284 BMK Finite Current Quotient Construction Push, 2026-04-30

Owned files:

- `reconstitution/swarm-2026-04-30-agent-284-bmk-finite-current-quotient-construction-push.md`
- `reconstitution/bmk-finite-current-quotient-construction-push-2026-04-30.md`

No manuscript TeX was edited.  No PDF build was run.

## Claim Attacked

Push beyond Agent 276 by trying to construct the finite-window current
quotient, or a modified \(H_{\chi,N}\), that would make the BMK
finite-window differential identity true.  The required checks were:

1. diagonal annulus sign and normalization;
2. finite moment/current quotient;
3. collar factorization compatibility.

## Verdict

Closed in a weak single-pair sense: if the full analytic BMK deformation
retract is supplied, then a derived quotient by the full analytic finite
moment kernel makes
\[
  \bar\partial \bar H_{\chi,N}+\bar H_{\chi,N}\bar\partial
  =
  \operatorname{id}-i_Np_N
\]
true after the single-pair collar quotient.

Blocked for the manuscript target: this quotient is not a finite
support-local current quotient and is not compatible with the native
Hamiltonian/factorization structure.  A strict finite quotient killing high
moments cannot retain the full Hamiltonian current action.

## New Computation Beyond Agent 276

For the displayed kernel, on \(|\eta|=1\) with
\[
  \eta_1=e^{i\alpha}\cos\phi,\qquad
  \eta_2=e^{i\beta}\sin\phi,
\]
one has
\[
  \bigl(\bar\eta_1d\bar\eta_2-\bar\eta_2d\bar\eta_1\bigr)
    \wedge d\eta_1\wedge d\eta_2
  =
  -2\sin\phi\cos\phi\,
    d\phi\wedge d\alpha\wedge d\beta .
\]
Hence
\[
  K_{\mathrm{BM}}|_{S^3}
  =
  \frac{\sin\phi\cos\phi}{2\pi^2}\,
    d\phi\wedge d\alpha\wedge d\beta .
\]
With the real orientation
\[
  dx_1\wedge dy_1\wedge dx_2\wedge dy_2
  =
  -r^3\sin\phi\cos\phi\,
    dr\wedge d\phi\wedge d\alpha\wedge d\beta,
\]
the outward \(S^3\)-integral is
\[
  \int_{S^3_{\mathrm{out}}}K_{\mathrm{BM}}=-1 .
\]
Therefore the diagonal cutoff annulus contributes
\[
  \bar\partial\vartheta_\epsilon(|\eta|)\wedge K_{\mathrm{BM}}
  \to -[\Delta]_{\mathrm{real}}.
\]
The manuscript's positive identity requires the BMK diagonal current
orientation
\[
  [\Delta]_{\mathrm{BM}}=-[\Delta]_{\mathrm{real}},
\]
or the kernel sign must be reversed.  The Taylor sign in
\[
  \Delta_{a,b}
  =
  \frac{(-1)^{a+b}}{a!b!}
  \partial_{z_1}^a\partial_{z_2}^b
  \delta_0\,d\bar z_1\wedge d\bar z_2
\]
does not fix this global orientation scalar.

## Positive One-Pair Construction

Assume a full analytic contraction
\[
  \bar\partial H_\chi+H_\chi\bar\partial
    =
  \operatorname{id}-I_{\mathrm{an}}P_{\mathrm{an}}+E_\chi .
\]
Normalize
\[
  H_\chi^0
  =
  (1-I_{\mathrm{an}}P_{\mathrm{an}})
  H_\chi
  (1-I_{\mathrm{an}}P_{\mathrm{an}}),
\]
so that \(H_\chi^0I_{\mathrm{an}}=0\).  Let
\[
  \pi_N:\mathcal O(B_1)^\vee\to \mathcal P_{\le N}
\]
be the finite moment map and \(K_N=\ker\pi_N\).  Define
\[
  C_N^{\mathrm{der}}(B_2,B_1)
  =
  C^\bullet(B_2,B_1)/I_{\mathrm{an}}(K_N).
\]
Then \(H_\chi^0\) descends and the induced identity is
\[
  \bar\partial \bar H_{\chi,N}
  +\bar H_{\chi,N}\bar\partial
  =
  \operatorname{id}-i_Np_N .
\]

This construction is not enough for the manuscript theorem surface.  It
kills the full analytic moment kernel, not only finite support-at-zero high
derivatives.  It depends on noncanonical representatives of
\(\ker\pi_N\).  It is not a support-local factorization quotient.

## Exact Obstruction

A strict finite quotient compatible with the full Hamiltonian current action
would require the killed relation subspace \(R_N\) to satisfy
\[
  \mathfrak h\cdot R_N\subset R_N.
\]
This is false.  The Matlis coadjoint formula gives
\[
  z_1^p z_2^q\cdot\rho_{i,j}
  =
  -(pj-qi+p-q)\rho_{i-p+1,j-q+1}.
\]
Taking \(p=N+2\), \(q=0\), \(i=N+1\), \(j=0\),
\[
  z_1^{N+2}\cdot\rho_{N+1,0}
  =
  -(N+2)\rho_{0,1}.
\]
The class \(\rho_{N+1,0}\) is killed by a finite window
\(\mathcal P_{\le N}\), while \(\rho_{0,1}\) is retained for every
\(N\geq1\).  Thus the finite moment kernel is not a Hamiltonian submodule.
The scalar line has the same defect:
\[
  z_1\cdot\rho_{0,0}=-\rho_{0,1}.
\]

Therefore no strict finite support-local current quotient can both kill the
scalar/high moments and retain the native Hamiltonian factorization action.
The exact obstruction vector is
\[
  \operatorname{Ob}_{284,N}
  =
  \left(
    \operatorname{ob}_{\mathrm{diag}},
    \operatorname{ob}_{\mathrm{an}/\mathrm{fin},N},
    \operatorname{ob}_{\mathfrak h,N},
    \operatorname{ob}_{\mathrm{collar\mbox{-}fact},N}
  \right),
\]
where:

- \(\operatorname{ob}_{\mathrm{diag}}\) is the BMK annulus sign/scalar.
  With the displayed kernel and real outward orientation the mass is
  \(-1\).
- \(\operatorname{ob}_{\mathrm{an}/\mathrm{fin},N}\) is the nonzero gap
  between the full analytic moment kernel \(\ker\pi_N\) and the smaller
  support-zero high-derivative span.
- \(\operatorname{ob}_{\mathfrak h,N}
  =\pi_N(\mathfrak h\cdot\ker\pi_N)\), nonzero by
  \(z_1^{N+2}\cdot\rho_{N+1,0}=-(N+2)\rho_{0,1}\).
- \(\operatorname{ob}_{\mathrm{collar\mbox{-}fact},N}\) is the failure of
  the quotient relation to be a cosheaf/factorization ideal under extension
  by zero, disjoint products, and the BMK homotopy.

## Next Construction Target

The finite quotient is decided.  It can close a single-pair derived
differential identity only by using the full analytic quotient; it cannot
be the native finite factorization current quotient.

The next target is either:

1. the all-window/pro-Matlis BMK transfer with uniform estimates and collar
   primitives; or
2. a projected finite-window \(L_\infty\) factorization package whose first
   escape operation records
   \[
     \kappa_N(z_1^{N+2},\rho_{N+1,0})
       =
     -(N+2)\rho_{0,1}.
   \]

Finite windows should be treated as output projections or as a
homotopy-coherent ledger, not as strict current quotients.

## Files Changed

- Added
  `reconstitution/bmk-finite-current-quotient-construction-push-2026-04-30.md`.
- Added
  `reconstitution/swarm-2026-04-30-agent-284-bmk-finite-current-quotient-construction-push.md`.
