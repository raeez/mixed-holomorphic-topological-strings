# Costello-Local Closed-Exchange Cone Realization

Date: 2026-04-30.

Scope: ordinary scalar-reduced \(\mathfrak{gl}_N\) brane-defect QME branch.
Report-only.  No TeX or script file is modified.

## Verdict

The algebraic cone of Agent 241 is correct as a changed algebraic source
branch.  It is not a Costello-local closed exchange in the present ordinary
branch.

For every finite window \(M\) containing \(z_1,z_2\), the cone
\[
  \mathcal X_{\mathrm{alg},\mathrm{sc},w,M}^{1}(I)
    =\mathbb C[[\hbar]]e_M,\qquad
  \mathcal X_{\mathrm{alg},\mathrm{sc},w,M}^{0}(I)=0,\qquad
  d^X_M e_M=0
\]
with
\[
  \Xi^{\mathrm{alg},\mathrm{sc}}_M(e_M)
    =
  -\hbar N\,\bar c_M(f,g)
  \int_I a(t)b(t)\gamma_{\mathbf 1}(t)\,dt
\]
has \(W_M=e_M\), \(C_M=0\), \(\rho^X_{M,N}e_M=e_N\), and hence
\[
  \beta_M^{\mathrm{sc}}
  =\beta_{\mathrm{cl}}^{\mathrm{sc}}
  =\mu_{\mathrm{cl}}^{\mathrm{sc}}
  =\lambda_C^{\mathrm{sc}}=0
\]
inside the adjoined defect-supported central-contact extension.  This is a
tautological central source line.  It contains no closed bulk field, no
finite-scale closed propagator, no bulk-to-defect restriction, no source-face
calculation, and no Costello counterterm support.

The Costello-local realization fails for the current data.  The first ordinary
obstruction remains
\[
  o_{\sigma,M}^{(1),\mathrm{sc}}
    =
  \hbar N[\bar c_M]\neq 0.
\]
If a scalar-contact gate is externally supplied, the next obstruction is the
Costello-local scalar image class
\[
  \beta_{M}^{\mathrm{Cost},\mathrm{sc}}
  =
  [\hbar N[\bar c_M]]
  \in
  \operatorname{coker}
  H^1\!\left(
    \widehat\sigma_{\mathrm{sc},M}\Xi^{\mathrm{Cost},\mathrm{sc}}_M
  \right),
\]
where \(\Xi^{\mathrm{Cost},\mathrm{sc}}_M\) is restricted to maps built from
Costello-local closed fields, finite-scale propagators, bulk-to-defect
support rules, and local counterterms.  For the presently constructed genuine
towers this image is scalar-zero; hence the displayed class is nonzero.

## Required Costello-Local Data

A genuine realization of the cone must replace \(e_M\) by a closed-exchange
complex
\[
  \mathcal X^{\bullet,\mathrm{Cost}}_{\mathrm{sc},w,M}(I)
\]
and a degree-zero continuous cochain map
\[
  \Xi^{\mathrm{Cost},\mathrm{sc}}_M\colon
  \mathcal X^{\bullet,\mathrm{Cost}}_{\mathrm{sc},w,M}(I)
  \longrightarrow
  \mathfrak Q^\bullet_{\mathrm{sc},w,M}(I)
\]
such that
\[
  \pi_{M,N}\Xi^{\mathrm{Cost},\mathrm{sc}}_M
  =
  \Xi^{\mathrm{Cost},\mathrm{sc}}_N\rho^X_{M,N}
\]
and admissible weight transports commute with both sides.

The map must be produced by a Hom-valued kernel, not by declaring its value:
\[
  \Xi^{\mathrm{Cost},\mathrm{sc}}_M(x)
    =
  \sum_{\Gamma\in\mathcal G^{\mathrm{cl}\to\mathrm{bd}}_M}
  {1\over |\operatorname{Aut}\Gamma|}
  W^{R,M}_{\Gamma,L,w}(x;-).
\]
The rows must satisfy the source-face Bianchi equation
\[
  d_{\mathbf K,M}\Xi_M
  =
  d_M\Xi_M-\Xi_M d^X_M=0,
\]
or, for a curved central-operation kernel,
\[
  \operatorname{Curv}_{\mathbf K,M}(\kappa)
  =
  d_{\mathbf K,M}\kappa
  +{1\over2}[\kappa,\kappa]_{\mathbf K,M}=0 .
\]

The scalar-contact projection gate must be an actual filtered chain map
\[
  \widehat\sigma_{\mathrm{sc},M}\colon
  \mathfrak Q^\bullet_{\mathrm{sc},w,M}(I)
  \longrightarrow
  C^\bullet_{\mathrm{Lie}}
  (\bar A_{\mathrm{fw},M};\mathbb C\gamma_{\mathbf 1})[1][[\hbar]]
\]
with
\[
  \widehat\sigma_{\mathrm{sc},M}d_M
  =
  d_{\mathrm{CE}}\widehat\sigma_{\mathrm{sc},M}.
\]
The required source class is forced:
\[
  H^1(
    \widehat\sigma_{\mathrm{sc},M}\Xi^{\mathrm{Cost},\mathrm{sc}}_M
  )[W_M]
  =
  -\hbar N[\bar c_M].
\]

## Locality and Support Conditions

The Costello source anchors impose the following support discipline.

1. Finite-scale propagator.  The propagator is the heat-kernel expression
\[
  P(\epsilon,T)=\int_\epsilon^T(Q^{\mathrm{GF}}\otimes1)K_t\,dt,
\]
with the \(t=0\) singularity excluded at finite scale.  See
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:77-90`.

2. Regularized BV operator.  The BV operator used in the QME must be
\(\Delta_t=-\partial K_t\) for \(t>0\), not the ill-defined \(\Delta_0\).
See `references/primary-sources/costello-renormalisation-bv-0706.1533.txt:407-423`.

3. Local functionals.  Taylor coefficients must factor through
polydifferential operators into densities.  See
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:1122-1151`.

4. Counterterms and graph weights.  Renormalized graph weights and
counterterms must be local, supported on the relevant small diagonal or
brane-collision stratum, and preserved by RG flow.  See
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:1746-1807`,
`:2121-2190`, and `:3544-3572`.

5. Defect currents.  The present local mirrors do not supply a theorem for a
\(\mathcal D'_c(I)\)-valued target, a current-valued bulk-to-defect kernel,
or compactly supported distributional defect labels.  Local searches for
`current-valued`, `D'_c`, and `bulk-to-defect` over the Costello,
Costello--Gwilliam, and Costello--Li mirrors returned no hits.  The only
wavefront anchor is Costello--Li's BCOV small-diagonal condition at
`references/primary-sources/costello-li-quantum-bcov-1201.4501.txt:611-620`;
it does not construct the interval-current target.

The algebraic cone violates this discipline as a Costello-local realization:
its kernel is already the defect contact distribution
\[
  -\hbar N\,\bar c_M(f,g)\,\delta_{\Delta_I}\gamma_{\mathbf 1},
\]
with no finite-scale closed propagator whose boundary value gives it and no
renormalized source-face graph table producing the central source line.

## Exact Obstruction Theorem

Fix \(N>0\), the ordinary scalar-reduced \(\mathfrak{gl}_N\) branch, and a
finite window \(M\) containing \(z_1,z_2\).  Exclude the unreduced
central-character source replacement and the balanced supertrace open model.
Let \(\mathcal X^{\bullet,\mathrm{Cost}}_{\mathrm{sc},w,M}(I)\) range only
over closed-exchange complexes constructed from Costello-local closed fields,
finite-scale graph kernels, bulk-to-defect support rules, and local
counterterms in the current manuscript habitat.

Then the algebraic cone realizes the scalar cancellation if and only if the
branch is enlarged by the defect-supported central source line \(e_M\).  In
the original Costello-local branch, scalar cancellation is possible only if
the following obstruction sequence vanishes.

First, the scalar-contact chain projection obstruction:
\[
  o_{\sigma,M}^{(1),\mathrm{sc}}
  =
  \hbar N[\bar c_M]\in
  H^1\operatorname{Hom}
  (\operatorname{gr}_F\mathfrak Q^\bullet_{w,\partial,\hbar}(I),
   C^\bullet_{\mathrm{Lie}}(\bar A;\mathbb C\gamma_{\mathbf 1})[1][[\hbar]]) .
\]
This class is nonzero because
\[
  \bar c_M(z_1,z_2)=1,\qquad \{z_1,z_2\}=1=0\text{ in }\bar A.
\]

Second, assuming a chain projection is supplied, the fixed-window
Costello-local scalar image obstruction:
\[
  \beta_{M}^{\mathrm{Cost},\mathrm{sc}}
  =
  [\hbar N[\bar c_M]]
  \in
  \operatorname{coker}
  H^1(
    \widehat\sigma_{\mathrm{sc},M}\Xi^{\mathrm{Cost},\mathrm{sc}}_M).
\]
For the constructed regular-density and non-scalar towers,
\[
  H^1(
    \widehat\sigma_{\mathrm{sc},M}\Xi^{\mathrm{Cost},\mathrm{sc}}_M)
  =0
  \quad\text{on the scalar line},
\]
so \(\beta_{M}^{\mathrm{Cost},\mathrm{sc}}\neq0\).

Third, if fixed-window classes are later supplied, the inverse-limit class
\[
  \beta_{\mathrm{cl}}^{\mathrm{Cost},\mathrm{sc}}
  =
  \left[(\hbar N[\bar c_M])_M\right]
  \in
  \operatorname{coker}\!\left(
    \varprojlim_M H^1(\mathcal X^{\bullet,\mathrm{Cost}}_{\mathrm{sc},w,M}(I))
    \to
    \varprojlim_M H^1(\mathcal S^\bullet_M(I))
  \right)
\]
must vanish.

Fourth, after choosing a compatible cohomology lift
\(\alpha=(\alpha_M)_M\), the representative Roos class
\[
  \mu_{\mathrm{cl}}^{\mathrm{Cost},\mathrm{sc}}(\alpha)
  \in
  \varprojlim\nolimits^1_M
  H^0(\mathcal X^{\bullet,\mathrm{Cost}}_{\mathrm{sc},w,M}(I))
\]
is represented by
\[
  \rho^X_{M+1,M}w_{M+1}-w_M=d^X_Mu_M.
\]

Fifth, after compatible \(W_M\) are chosen, the counterterm Roos class
\[
  \lambda_C^{\mathrm{Cost},\mathrm{sc}}(W)
  \in
  \varprojlim\nolimits^1_M
  H^0(\mathfrak Q^\bullet_{\mathrm{sc},w,M}(I))
\]
is represented by
\[
  [\pi_{M+1,M}c_{M+1}-c_M],
  \qquad
  d_Mc_M=
  -(\operatorname{Ob}_{\mathrm{sc},M}
    +\Xi^{\mathrm{Cost},\mathrm{sc}}_M(W_M)).
\]

Thus the exact separation is:
\[
  \text{algebraic cone success}
  \Longleftrightarrow
  \text{adjoined central source line},
\]
whereas
\[
  \text{Costello-local closed exchange}
  \Longleftrightarrow
  o_\sigma=\beta_M^{\mathrm{Cost}}
  =\beta_{\mathrm{cl}}^{\mathrm{Cost}}
  =\mu_{\mathrm{cl}}^{\mathrm{Cost}}
  =\lambda_C^{\mathrm{Cost}}=0
\]
with the source, support, propagator, Bianchi, and counterterm data above.
The present branch fails before \(\mu\) and \(\lambda_C\): it has no
Costello-local class mapping to \(-\hbar N[\bar c_M]\).

## Proposed Insertion

Suggested insertion after the scalar closed-exchange paragraph in
`open-obligations.tex`:

```tex
\item \emph{Algebraic central-contact cone versus Costello-local exchange.}
The one-line cone
\[
  \mathcal X^{1,\mathrm{alg}}_{\mathrm{sc},w,M}(I)
  =\mathbb C[[\hbar]]e_M,\qquad
  \Xi^{\mathrm{alg},\mathrm{sc}}_M(e_M)
  =-\hbar N\bar c_M
\]
with \(W_M=e_M\), \(C_M=0\), and \(\rho^X_{M,N}e_M=e_N\) kills the scalar
finite-window and Roos classes only after adjoining a defect-supported
central source line.  It is therefore a changed algebraic branch.  A genuine
Costello-local closed exchange must instead construct a closed source complex
\(\mathcal X^{\bullet,\mathrm{Cost}}_{\mathrm{sc},w,M}(I)\), finite-scale
propagator and bulk-to-defect graph weights, source-face Bianchi identity
\(d_{\mathbf K,M}\Xi_M=0\), local counterterm support, a filtered scalar
chain projection \(\widehat\sigma_{\mathrm{sc},M}\), and compatible
finite-window representatives.  Its first scalar image obstruction is
\[
  \beta_{M}^{\mathrm{Cost},\mathrm{sc}}
  =
  [\hbar N[\bar c_M]]
  \in
  \operatorname{coker}
  H^1(\widehat\sigma_{\mathrm{sc},M}\Xi^{\mathrm{Cost},\mathrm{sc}}_M).
\]
For the current genuine Costello-local towers this scalar image is zero, so
the ordinary scalar-reduced branch remains obstructed unless a new
Costello-local source class with image \(-\hbar N[\bar c_M]\) is constructed.
If such a class is supplied, the remaining inverse-limit obstructions are
\(\beta_{\mathrm{cl}}^{\mathrm{Cost},\mathrm{sc}}\),
\(\mu_{\mathrm{cl}}^{\mathrm{Cost},\mathrm{sc}}\), and
\(\lambda_C^{\mathrm{Cost},\mathrm{sc}}\) with the standard Roos
representatives.
```

## Anchors

- `appendix-unreduced-bv-qme.tex:53-111`: local scalar cocycle
  \(\omega(f,g)=[\{f,g\}]_0\), \(\omega(z_1,z_2)=1\), finite windows do not
  change the local formal bracket.
- `appendix-unreduced-bv-qme.tex:135-183`: scalar-symbol projection is only
  associated graded before a filtered chain projection is chosen.
- `appendix-unreduced-bv-qme.tex:236-305`: first scalar-lift obstruction in
  the ordinary branch is \(\hbar N[\bar c]\), nonzero on \(z_1,z_2\).
- `appendix-unreduced-bv-qme.tex:560-685`: unreduced primitive exists on
  \(A=\mathbb C[z_1,z_2]\) and does not descend to \(\bar A=A/\mathbb C1\).
- `appendix-unreduced-bv-qme.tex:2142-2232`: native finite-window
  Costello/QME habitat requires Hom differential, source faces, kernel, and
  scalar projection.
- `main.tex:7441-7510`: analytic graph realization requires local
  obstruction, kernel, counterterms, principal-part current compatibility,
  and RG data.
- `main.tex:7569-7643`: scalar QME alternatives and necessary
  closed-exchange leading class.
- `main.tex:8022-8194`: scalar projection first, then non-scalar and
  closed-exchange obstruction triples.
- `open-obligations.tex:322-350`: current ledger already records algebraic
  cone success but not Costello-local realization.
- `claim-strength-ledger.tex:1155-1165`: same distinction in the claim
  ledger.
- `local-dictionary.tex:840-874`: \(\widehat\sigma_{\mathrm{sc}}\) exists
  exactly after scalar-lift obstruction classes vanish; ordinary branch has
  first nonzero evaluation \(\hbar N\omega(f,g)\gamma_{\mathbf 1}\).
- `tate-T1-weighted-completion.tex:1526-1740`: closed-exchange image,
  inverse-limit, and Roos obstruction theorem.
- `references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md:40-130`:
  Costello finite-scale propagator, QME/RG, locality, counterterms, graph
  asymptotics, and local obstruction anchors.
- `references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md:156-232`:
  exact non-support for automatic current target, \(\mathcal D'_c\)
  wavefront theorem, and bulk-to-defect kernel.

## Verification

Read-only checks run:

```bash
rg --files reconstitution references scripts | rg -i 'scalar|closed-exchange|costello|qme|finite-window|agent-241|agent-232|agent-220|agent-198|agent-147'
nl -ba reconstitution/swarm-2026-04-30-agent-241-finite-window-closed-exchange-realization-construction-push.md | sed -n '1,360p'
nl -ba reconstitution/scalar-qme-closed-exchange-construction-target-2026-04-30.md | sed -n '1,330p'
nl -ba main.tex | sed -n '7440,7650p'
nl -ba main.tex | sed -n '8020,8205p'
nl -ba appendix-unreduced-bv-qme.tex | sed -n '45,190p'
nl -ba appendix-unreduced-bv-qme.tex | sed -n '230,310p'
nl -ba appendix-unreduced-bv-qme.tex | sed -n '555,690p'
nl -ba appendix-unreduced-bv-qme.tex | sed -n '2140,2245p'
nl -ba open-obligations.tex | sed -n '315,475p'
nl -ba open-obligations.tex | sed -n '548,650p'
nl -ba claim-strength-ledger.tex | sed -n '1048,1178p'
nl -ba local-dictionary.tex | sed -n '820,890p'
nl -ba tate-T1-weighted-completion.tex | sed -n '1520,1740p'
nl -ba references/primary-sources/costello-renormalisation-bv-0706.1533.txt | sed -n '70,95p'
nl -ba references/primary-sources/costello-renormalisation-bv-0706.1533.txt | sed -n '405,425p'
nl -ba references/primary-sources/costello-renormalisation-bv-0706.1533.txt | sed -n '1120,1152p'
nl -ba references/primary-sources/costello-renormalisation-bv-0706.1533.txt | sed -n '1740,1810p'
nl -ba references/primary-sources/costello-renormalisation-bv-0706.1533.txt | sed -n '2120,2192p'
nl -ba references/primary-sources/costello-renormalisation-bv-0706.1533.txt | sed -n '2372,2422p'
nl -ba references/primary-sources/costello-renormalisation-bv-0706.1533.txt | sed -n '2464,2488p'
nl -ba references/primary-sources/costello-li-quantum-bcov-1201.4501.txt | sed -n '608,628p'
nl -ba references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt | sed -n '800,812p'
rg -n -F "bulk-to-defect" references/primary-sources/costello-renormalisation-bv-0706.1533.txt references/primary-sources/costello-gwilliam-vol1-cambridge.html references/primary-sources/costello-gwilliam-vol2-cambridge.html references/primary-sources/costello-li-quantum-bcov-1201.4501.txt references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt || true
rg -n -F "current-valued" references/primary-sources/costello-renormalisation-bv-0706.1533.txt references/primary-sources/costello-gwilliam-vol1-cambridge.html references/primary-sources/costello-gwilliam-vol2-cambridge.html references/primary-sources/costello-li-quantum-bcov-1201.4501.txt references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt || true
rg -n -F "D'_c" references/primary-sources/costello-renormalisation-bv-0706.1533.txt references/primary-sources/costello-gwilliam-vol1-cambridge.html references/primary-sources/costello-gwilliam-vol2-cambridge.html references/primary-sources/costello-li-quantum-bcov-1201.4501.txt references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt || true
```

Finite scalar check:

```text
CE cocycle failures through bidegree<6: 0
omega(z1,z2)= 1
reduced exactness test: d eta(z1,z2) = -eta({z1,z2} mod C) = 0, so omega is not exact on A/C
```

No build was run.  The task is report-only, and the shared checkout contains
concurrent TeX and PDF changes outside this agent's ownership.
