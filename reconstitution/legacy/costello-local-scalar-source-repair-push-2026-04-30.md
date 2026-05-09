# Costello-Local Scalar Source Repair Push

Date: 2026-04-30.

Scope: ordinary scalar-reduced \(\mathfrak{gl}_N\) brane-defect QME branch,
with \(N>0\), finite windows \(M\) containing \(z_1,z_2\), and no
central-character source replacement or balanced supertrace open model.
Report-only. No TeX, script, bibliography, source fixture, or figure file is
modified.

## Verdict

I attacked the strongest same-branch construction target:
\[
  x_M\in Z^1(\mathcal X^{\bullet,\mathrm{Cost},\mathrm{sc}}_{w,M}(I)),
  \qquad
  H^1(\widehat\sigma_{\mathrm{sc},M}\Xi^{\mathrm{Cost},\mathrm{sc}}_M)[x_M]
  =
  -\hbar N[\bar c_M].
\]
No such Costello-local source class is constructed by the current data.

The algebraic cone
\[
  \mathcal X_{\mathrm{alg},M}^{1}=\mathbb C[[\hbar]]e_M,\qquad
  \Xi^{\mathrm{alg},\mathrm{sc}}_M(e_M)
  =
  -\hbar N\,\bar c_M(f,g)
  \int_I a(t)b(t)\gamma_{\mathbf 1}(t)\,dt
\]
does solve the scalar equation after adjoining a defect-supported central
contact line. It is not a genuine Costello-local closed exchange: it has no
closed field, finite-scale closed propagator, source-face graph computation,
wavefront theorem, or local counterterm/RG construction.

The sharp obstruction in the original ordinary branch is still first the
scalar-contact chain-projection obstruction
\[
  o_{\sigma,M}^{(1),\mathrm{sc}}
  =
  \hbar N[\bar c_M],
  \qquad
  \operatorname{ev}_{z_1,z_2}(o_{\sigma,M}^{(1),\mathrm{sc}})
  =
  \hbar N\gamma_{\mathbf 1}\neq0.
\]
If a scalar-contact chain projection is supplied externally, the next exact
obstruction is
\[
  \beta_M^{\mathrm{Cost},\mathrm{sc}}
  =
  [\hbar N[\bar c_M]]
  \in
  \operatorname{coker}
  H^1(\widehat\sigma_{\mathrm{sc},M}\Xi^{\mathrm{Cost},\mathrm{sc}}_M).
\]
For the presently constructed genuine Costello-local graph/source data,
\(\widehat\sigma_{\mathrm{sc},M}\Xi^{\mathrm{Cost},\mathrm{sc}}_M\) has zero
image on the scalar line. Hence \(\beta_M^{\mathrm{Cost},\mathrm{sc}}\neq0\)
in the original ordinary branch.

## Claim Attacked

The attacked claim is:

> The ordinary scalar-reduced \(\mathfrak{gl}_N\) branch admits a genuine
> Costello-local closed-exchange source class whose graph/Hom image has
> scalar leading class \(-\hbar N[\bar c_M]\), satisfies
> \(d_{\mathbf K}\Xi=0\), obeys locality and support, is compatible with
> scalar-contact chain projection, and transports through finite windows.

This claim would prove the same-branch scalar cancellation equation
\[
  \operatorname{Ob}_{\mathrm{sc},M}
  +\Xi^{\mathrm{Cost},\mathrm{sc}}_M(W_M)
  +d_M C_M=0,
\]
with
\[
  \widehat\sigma_{\mathrm{sc},M}\Xi^{\mathrm{Cost},\mathrm{sc}}_M(W_M)
  =
  -\hbar N\bar c_M+d_{\mathrm{CE}}\eta_M.
\]

## Source Habitat

Fix \(I,w,M\). Put
\[
  \mathfrak Q^\bullet_{\mathcal G,M}(I)
  =
  \left(
  \mathcal O^{\mathrm{bd}}_{\mathrm{loc},\mathcal G,M}
  (\mathcal E^M_w|_I;A^{\mathrm{pp},w,M}_{\partial,\hbar}(I)),
  d_M
  \right),
  \qquad
  d_M=Q+\{I^w_{0,M},-\}_{\hbar,M}.
\]
The topology is the completed \(\hbar\)-adic, scalar-contact, and
finite-window topology. The source is Costello-local only if it is generated
by finite-scale graph/Hom data:
\[
  \Xi^{\mathrm{Cost},\mathrm{sc}}_M(x)
  =
  \sum_{\Gamma\in\mathcal G^{\mathrm{cl}\to\mathrm{bd}}_M}
  {1\over |\operatorname{Aut}\Gamma|}
  W^{R,M}_{\Gamma,L,w}(x;-)
\]
with local counterterms supported on the small diagonal or brane-collision
stratum. Its Hom differential is
\[
  d_{\mathbf K,M}T=d_MT-(-1)^{|T|}T\,d_X.
\]
For a degree-zero graph kernel the required source-face equation is
\[
  d_{\mathbf K,M}\Xi_M
  =
  d_M\Xi_M-\Xi_Md_X=0.
\]
For a curved central-operation kernel the stronger condition is
\[
  \operatorname{Curv}_{\mathbf K,M}(\kappa)
  =
  d_{\mathbf K,M}\kappa+\frac12[\kappa,\kappa]_{\mathbf K,M}=0.
\]

The scalar target, after a chain projection exists, is
\[
  \mathcal S^\bullet_M(I)
  =
  C^\bullet_{\mathrm{Lie}}
  (\bar A_{\mathrm{fw},M};\mathbb C\gamma_{\mathbf 1})[1][[\hbar]].
\]
The map to be tested is
\[
  H^1(\widehat\sigma_{\mathrm{sc},M}\Xi^{\mathrm{Cost},\mathrm{sc}}_M)\colon
  H^1(\mathcal X^{\bullet,\mathrm{Cost},\mathrm{sc}}_{w,M}(I))
  \to
  H^1(\mathcal S^\bullet_M(I)).
\]
The finite-window class is
\[
  \bar c_M(f,g)=[\{f,g\}_{\Omega_{\mathrm{loc}}}]_0,
  \qquad
  \bar c_M(z_1,z_2)=1,
\]
and the transported family satisfies
\[
  \rho^S_{M,N}[\bar c_M]=[\bar c_N]
\]
for windows retaining \(z_1,z_2\).

This habitat excludes the one-line algebraic generator \(e_M\), because
\(e_M\) is a prescribed central contact value, not a finite-scale graph
weight. It also excludes the unreduced central-character replacement as a
same-branch closed exchange.

## Construction Attempts

### Attempt 1: Algebraic Central-Contact Cone

The cone of Agents 241 and 247 gives
\[
  d^X_Me_M=0,\qquad
  \rho^X_{M,N}e_M=e_N,
\]
\[
  \Xi^{\mathrm{alg},\mathrm{sc}}_M(e_M)
  =
  -\hbar N\,\bar c_M(f,g)
  \int_I a(t)b(t)\gamma_{\mathbf 1}(t)\,dt.
\]
With \(W_M=e_M\) and \(C_M=0\), the scalar finite-window and Roos equations
vanish inside the enlarged algebraic branch.

Rejection as Costello-local: the displayed \(\Xi\) is the contact term itself.
It is not produced by a closed field, finite-scale propagator, source-face
table, local counterterm subtraction, or RG-compatible graph weight. Costello
supports finite-scale propagators and local counterterms in an elliptic BV
setting, but the Hamiltonian brane-defect current target and bulk-to-defect
kernel are manuscript obligations.

### Attempt 2: Opposite Central Extension of the Source

Adjoin
\[
  \bar A^{\mathrm{cl}}_{-\hbar N\bar c}
  =
  \bar A\oplus\mathbb C K_{\mathrm{cl}},
  \qquad
  [(f,aK),(g,bK)]
  =
  (\{f,g\}_{\bar A},-\hbar N\bar c(f,g)K).
\]
Let \(k^\vee\) be the CE one-cochain dual to \(K_{\mathrm{cl}}\). Then
\[
  d_{\mathrm{CE}}k^\vee(f,g)
  =
  -k^\vee([f,g])
  =
  \hbar N\bar c(f,g),
\]
so
\[
  d_{\mathrm{CE}}(-k^\vee)=-\hbar N\bar c.
\]
This is algebraically the desired opposite scalar. It is not a source class
in \(H^1\): the would-be cochain \(-k^\vee\) is not closed. It changes the
source so that the scalar class becomes exact before reduction. This is the
central-character/source-replacement branch, not a Costello-local
closed-exchange class in the original scalar-reduced branch.

### Attempt 3: Existing Regular-Density Costello Tower

The genuine constructed tower is the regular-density non-scalar tower:
\[
  \mathcal X^{\bullet,\mathrm{reg}}_{w,M}(I)
  \subset
  \mathcal Q^\bullet_{w,M}(I)
  =
  \ker\widehat\sigma_{\mathrm{sc},M},
  \qquad
  \Xi^{\mathrm{reg}}_M=\mathrm{incl}.
\]
Therefore, whenever the scalar projection exists,
\[
  \widehat\sigma_{\mathrm{sc},M}\Xi^{\mathrm{reg}}_M=0
\]
on cochains and hence on \(H^1\). This tower cannot hit
\(-\hbar N[\bar c_M]\).

The current row/source-face data confirm scalar-zero image:
\[
  R^{\mathrm{row}}_{\alpha_{\mathrm{sc}},M}=0,\quad
  S_{\alpha_{\mathrm{sc}},M}=0,\quad
  C_{\alpha_{\mathrm{sc}},M}=0
\]
in the full-equivariant branch, and
\[
  R^{\mathrm{row}}_{\alpha_{11},M}
  =
  \operatorname{Str}_{\mathrm{cyc}}
  (\mu_{\beta_{11}}(\mathfrak m))\,
  \omega(z_1,z_1)
  \int_I a(t)b(t)\gamma_{\mathbf 1}(t)\,dt
  =0.
\]
The first supplied nonzero source-face row is
\[
  R^{\mathrm{row}}_{\theta_3,M}
  =
  -K^M_{\Theta_3}(\zeta_{M,\nu_3})
  =\mathsf E_{\theta_3,M},
  \qquad
  S_{\theta_3,M}=0.
\]
Thus \(\theta_3\) is non-scalar: it can obstruct the non-scalar row complex,
but it has zero scalar projection and cannot cancel \(\hbar N[\bar c_M]\).

### Attempt 4: Distributional Current Contact

A compactly supported distributional defect current could formally produce a
delta contact. This fails the declared Costello-local support test in the
current habitat. The local Costello mirrors do not supply a
\(\mathcal D'_c(I)\)-valued graph theorem, wavefront/counterterm theorem, or
bulk-to-defect kernel for this Hamiltonian defect target. The construction is
therefore not admissible unless restricted to regular densities or accompanied
by a new wavefront/transversality and counterterm theorem.

## Exact Obstruction Theorem

Fix \(N>0\), the ordinary scalar-reduced \(\mathfrak{gl}_N\) branch, and a
finite window \(M\) containing \(z_1,z_2\). In the current Costello-local
source habitat above, no same-branch scalar closed-exchange repair is
constructed. More precisely:

1. The scalar-contact chain projection is obstructed by
   \[
     o_{\sigma,M}^{(1),\mathrm{sc}}
     =
     \hbar N[\bar c_M]
     \in
     H^1\operatorname{Hom}
     (\operatorname{gr}_F\mathfrak Q^\bullet_{\mathcal G,M}(I),
      \mathcal S^\bullet_M(I)).
   \]
   Evaluation at the two linear Hamiltonians gives
   \[
     \operatorname{ev}_{z_1,z_2}
     (o_{\sigma,M}^{(1),\mathrm{sc}})
     =
     \hbar N\gamma_{\mathbf 1}\neq0.
   \]
   Non-exactness is detected already in the finite window: if
   \(\bar c_M=d_{\mathrm{CE}}\eta\) on \(\bar A_{\mathrm{fw},M}\), then
   \[
     1=\bar c_M(z_1,z_2)
     =
     (d_{\mathrm{CE}}\eta)(z_1,z_2)
     =
     -\eta(\{z_1,z_2\}_{\bar A})
     =
     -\eta(0)=0,
   \]
   a contradiction.

2. If a filtered scalar-contact chain projection
   \(\widehat\sigma_{\mathrm{sc},M}\) is supplied by additional data, the
   fixed-window scalar image obstruction is
   \[
     \beta_M^{\mathrm{Cost},\mathrm{sc}}
     =
     [\hbar N[\bar c_M]]
     \in
     \operatorname{coker}
     H^1(\widehat\sigma_{\mathrm{sc},M}
       \Xi^{\mathrm{Cost},\mathrm{sc}}_M).
   \]
   For the current graph/source data, the image is zero on the scalar line:
   regular-density towers land in \(\ker\widehat\sigma_{\mathrm{sc},M}\);
   the explicit \(\alpha_{\mathrm{sc}}\), \(\alpha_{11}\), and
   \(\theta_3\) rows have zero scalar gates; and the algebraic/contact
   alternatives fail the Costello-local habitat. Hence
   \[
     \beta_M^{\mathrm{Cost},\mathrm{sc}}
     =
     [\hbar N[\bar c_M]]\neq0.
   \]

3. The compatible tower obstruction, if the fixed-window image problem is
   later healed, is
   \[
     \beta_{\mathrm{cl}}^{\mathrm{Cost},\mathrm{sc}}
     =
     \left[(\hbar N[\bar c_M])_M\right]
     \in
     \operatorname{coker}\!\left(
       \varprojlim_M H^1(\mathcal X^{\bullet,\mathrm{Cost},\mathrm{sc}}_{w,M}(I))
       \to
       \varprojlim_M H^1(\mathcal S^\bullet_M(I))
     \right).
   \]
   After a compatible cohomology lift is chosen, representative transport and
   counterterm transport must also kill
   \[
     \mu_{\mathrm{cl}}^{\mathrm{Cost},\mathrm{sc}}
     \in
     \varprojlim\nolimits^1_M
     H^0(\mathcal X^{\bullet,\mathrm{Cost},\mathrm{sc}}_{w,M}(I)),
   \]
   represented by
   \[
     \rho^X_{M+1,M}w_{M+1}-w_M=d^X_Mu_M,
   \]
   and
   \[
     \lambda_C^{\mathrm{Cost},\mathrm{sc}}
     \in
     \varprojlim\nolimits^1_M
     H^0(\mathfrak Q^\bullet_{\mathcal G,M}(I)),
   \]
   represented by
   \[
     [\pi_{M+1,M}c_{M+1}-c_M],
     \qquad
     d_Mc_M=
     -(\operatorname{Ob}_{\mathrm{sc},M}
       +\Xi^{\mathrm{Cost},\mathrm{sc}}_M(W_M)).
   \]
   The present branch does not reach these secondary classes, because
   \(o_{\sigma,M}^{(1),\mathrm{sc}}\) and then
   \(\beta_M^{\mathrm{Cost},\mathrm{sc}}\) already obstruct it.

## TeX-Ready Insertion

Suggested insertion in the scalar closed-exchange obligation lane:

```tex
\paragraph{Costello-local scalar source obstruction.}
Fix \(N>0\) in the ordinary scalar-reduced \(\mathfrak{gl}_N\) branch and a
finite window \(M\) containing \(z_1,z_2\).  A same-branch scalar
closed-exchange repair must be a Costello-local source class
\[
  W_M\in Z^1(\mathcal X^{\bullet,\mathrm{Cost},\mathrm{sc}}_{w,M}(I))
\]
whose finite-scale graph/Hom map satisfies
\[
  d_{\mathbf K,M}\Xi_M=0,\qquad
  \pi_{M,N}\Xi_M=\Xi_N\rho^X_{M,N},
\]
and whose scalar projection obeys
\[
  H^1(\widehat\sigma_{\mathrm{sc},M}\Xi_M)[W_M]
  =
  -\hbar N[\bar c_M].
\]
The algebraic one-line cone with
\(\Xi(e_M)=-\hbar N\bar c_M\) proves only an adjoined
defect-supported central-contact source branch.  It is not produced by a
closed field, finite-scale propagator, source-face graph table, local
counterterms, or RG-compatible bulk-to-defect kernel.  In the original
ordinary branch the first obstruction remains
\[
  o_{\sigma,M}^{(1),\mathrm{sc}}=\hbar N[\bar c_M],
  \qquad
  o_{\sigma,M}^{(1),\mathrm{sc}}(z_1,z_2)=\hbar N\gamma_{\mathbf 1}\neq0.
\]
If a scalar-contact chain projection is supplied externally, the next
obstruction is
\[
  \beta_M^{\mathrm{Cost},\mathrm{sc}}
  =
  [\hbar N[\bar c_M]]
  \in
  \operatorname{coker}
  H^1(\widehat\sigma_{\mathrm{sc},M}\Xi_M^{\mathrm{Cost},\mathrm{sc}}).
\]
For the presently constructed Costello-local rows and regular-density
closed-exchange towers this scalar image is zero; distributional-current
contacts fail the required wavefront/counterterm and bulk-to-defect locality
theorem.  Thus the same-branch scalar repair remains obstructed until a new
Costello-local source class with scalar image \(-\hbar N[\bar c_M]\) is
constructed and its inverse-system \(\beta,\mu,\lambda_C\) classes vanish.
```

## Anchors

- `CLAUDE.md:119-141`: supremum discipline: repair by construction or exact
  obstruction.
- `AGENTS.md:139-148`: attack-heal reports must include claim, failure/proof,
  anchors, formulas, files changed, and verification.
- `/Users/raeez/ecosystem/skills/shared/attack-heal-swarm/protocol.md:52-57`:
  mathematical repair rule requiring the exact obstruction if construction
  fails.
- `/Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md:54-70`:
  stop rule requiring a proved theorem or exact obstruction.
- `main.tex:423-492`: \(\omega(f,g)=[\{f,g\}]_0\), nontrivial
  \([\bar c]\) on \(\bar A\).
- `main.tex:7403-7567`: Hamiltonian Costello specialization data,
  current-compatible target, bulk-to-defect kernel, counterterms, and scalar
  opposite-class requirement.
- `main.tex:7569-7643`: scalar QME alternatives and the necessary
  closed-exchange class \(-\hbar N[\bar c]\).
- `main.tex:8022-8194`: scalar projection must precede non-scalar and
  closed-exchange obstruction towers.
- `appendix-unreduced-bv-qme.tex:53-111`: formal-local scalar shadow and
  \(\omega(z_1,z_2)=1\).
- `appendix-unreduced-bv-qme.tex:135-183`: scalar-symbol projection is only
  associated-graded until a filtered chain projection is constructed.
- `appendix-unreduced-bv-qme.tex:185-234`: Hom obstruction tower for the
  scalar-contact chain projection.
- `appendix-unreduced-bv-qme.tex:236-305`: first scalar-lift obstruction is
  \(\hbar N[\bar c]\), nonzero on \(z_1,z_2\).
- `appendix-unreduced-bv-qme.tex:560-685`: unreduced primitive exists on
  \(A\) and does not descend to \(\bar A\); scalar QME class is non-exact.
- `appendix-unreduced-bv-qme.tex:2142-2232`: native finite-window
  Costello/QME habitat, Hom differential, source-face term, graph weights,
  and scalar projection.
- `appendix-unreduced-bv-qme.tex:2387-2485`: closed rows and first supplied
  open source-face row; current rows have zero scalar gate.
- `local-dictionary.tex:820-960`: dictionary entries for
  \(\mathfrak Q\), \(F^\bullet\), \(\sigma_{\mathrm{sc}}\),
  \(\widehat\sigma_{\mathrm{sc}}\), \(o_\sigma\), and \(\kappa\).
- `tate-T1-weighted-completion.tex:1526-1741`: closed-exchange image
  criterion and \(\beta,\mu,\lambda\) Roos obstruction theorem.
- `scripts/finite_window_graph_array.py:1480-1545`: theta-three companion
  source-face obstruction data.
- `reconstitution/swarm-2026-04-30-agent-220-nonscalar-costello-qme-construction-frontier.md:8-24`:
  missing non-scalar Costello/QME construction data.
- `reconstitution/swarm-2026-04-30-agent-241-finite-window-closed-exchange-realization-construction-push.md:10-69`:
  algebraic cone success versus ordinary branch obstruction.
- `reconstitution/swarm-2026-04-30-agent-247-costello-local-closed-exchange-cone-realization.md:10-45`:
  cone is not a Costello-local closed exchange.
- `reconstitution/swarm-2026-04-30-agent-118-construct-X-Xi-closed-exchange.md:5-53`:
  regular-density \(\mathcal X^{\mathrm{reg}}\) and \(\Xi^{\mathrm{reg}}\)
  are scalar-zero inclusions into the non-scalar tower.
- `references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md:40-130`:
  Costello finite-scale BV/QME graph vocabulary.
- `references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md:156-232`:
  no automatic current-valued target, \(\mathcal D'_c\) wavefront theorem,
  or bulk-to-defect kernel.
- `references/primary-sources/costello-renormalisation-bv-0706.1533.txt:77-90`:
  finite-scale propagator and singular \(t=0\) limit.
- `references/primary-sources/costello-renormalisation-bv-0706.1533.txt:407-423`:
  regularized BV operator \(\Delta_t\) and ill-defined \(\Delta_0\).

## Commands Run

```bash
nl -ba AGENTS.md | sed -n '1,260p'
nl -ba CLAUDE.md | sed -n '1,260p'
nl -ba /Users/raeez/ecosystem/skills/shared/attack-heal-swarm/protocol.md | sed -n '1,260p'
nl -ba /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md | sed -n '1,260p'
rg --files | rg 'agent-(220|241|247)|swarm-2026-04-30-agent-(220|241|247)'
nl -ba reconstitution/swarm-2026-04-30-agent-220-nonscalar-costello-qme-construction-frontier.md | sed -n '1,260p'
nl -ba reconstitution/swarm-2026-04-30-agent-241-finite-window-closed-exchange-realization-construction-push.md | sed -n '1,320p'
nl -ba reconstitution/swarm-2026-04-30-agent-247-costello-local-closed-exchange-cone-realization.md | sed -n '1,360p'
nl -ba commands.tex | sed -n '1,220p'
nl -ba mathmacros.tex | sed -n '1,260p'
nl -ba notation.tex | sed -n '1,220p'
nl -ba preamble.tex | sed -n '1,220p'
nl -ba main.tex | sed -n '423,655p'
nl -ba main.tex | sed -n '7300,7650p'
nl -ba main.tex | sed -n '7860,8210p'
nl -ba appendix-unreduced-bv-qme.tex | sed -n '45,310p'
nl -ba appendix-unreduced-bv-qme.tex | sed -n '555,705p'
nl -ba appendix-unreduced-bv-qme.tex | sed -n '2140,2488p'
nl -ba local-dictionary.tex | sed -n '820,960p'
nl -ba tate-T1-weighted-completion.tex | sed -n '1520,1745p'
nl -ba reconstitution/swarm-2026-04-30-agent-118-construct-X-Xi-closed-exchange.md | sed -n '1,260p'
nl -ba reconstitution/swarm-2026-04-30-agent-198-nonscalar-costello-qme-realization.md | sed -n '1,220p'
nl -ba reconstitution/swarm-2026-04-30-agent-232-scalar-qme-closed-exchange-construction-target.md | sed -n '1,320p'
nl -ba reconstitution/swarm-2026-04-30-agent-108-bulk-defect-kernel-construction.md | sed -n '1,190p'
nl -ba reconstitution/swarm-2026-04-30-agent-102-costello-graph-qme-source.md | sed -n '1,140p'
nl -ba references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md | sed -n '1,250p'
nl -ba references/primary-sources/local-costello-bv-kernel-source-anchors-2026-04-30.md | sed -n '1,300p'
nl -ba references/primary-sources/costello-renormalisation-bv-0706.1533.txt | sed -n '77,95p'
nl -ba references/primary-sources/costello-renormalisation-bv-0706.1533.txt | sed -n '407,423p'
rg -n -F "current-valued" references/primary-sources/costello-renormalisation-bv-0706.1533.txt references/primary-sources/costello-gwilliam-vol1-cambridge.html references/primary-sources/costello-gwilliam-vol2-cambridge.html references/primary-sources/costello-li-quantum-bcov-1201.4501.txt references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt
rg -n -F "D'_c" references/primary-sources/costello-renormalisation-bv-0706.1533.txt references/primary-sources/costello-gwilliam-vol1-cambridge.html references/primary-sources/costello-gwilliam-vol2-cambridge.html references/primary-sources/costello-li-quantum-bcov-1201.4501.txt references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt
rg -n -F "bulk-to-defect" references/primary-sources/costello-renormalisation-bv-0706.1533.txt references/primary-sources/costello-gwilliam-vol1-cambridge.html references/primary-sources/costello-gwilliam-vol2-cambridge.html references/primary-sources/costello-li-quantum-bcov-1201.4501.txt references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
from itertools import product
def bracket(x,y):
    a,b=x; c,d=y
    coeff=a*d-b*c
    exp=(a+c-1,b+d-1)
    if coeff==0 or exp[0]<0 or exp[1]<0:
        return []
    if exp==(0,0):
        return []
    return [(coeff,exp)]
def omega(x,y):
    a,b=x; c,d=y
    return (a*d-b*c) if (a+c,b+d)==(1,1) else 0
monos=[(a,b) for a in range(6) for b in range(6) if (a,b)!=(0,0)]
fail=[]
for x,y,z in product(monos, repeat=3):
    s=0
    for coeff,e in bracket(x,y): s += coeff*omega(e,z)
    for coeff,e in bracket(y,z): s += coeff*omega(e,x)
    for coeff,e in bracket(z,x): s += coeff*omega(e,y)
    if s != 0:
        fail.append((x,y,z,s)); break
print('CE cocycle failures through bidegree<6:', len(fail))
print('omega(z1,z2)=', omega((1,0),(0,1)))
print('reduced exactness test at (z1,z2): d eta = -eta({z1,z2} mod C) = -eta(0)=0, so omega non-exact on A/C')
PY
python3 -m py_compile scripts/finite_window_graph_array.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite_window_graph_array.py > /tmp/finite-window-agent259.json
python3 -m json.tool /tmp/finite-window-agent259.json > /tmp/finite-window-agent259.pretty.json
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
import json
with open('/tmp/finite-window-agent259.json') as f:
    data=json.load(f)
for row in data['computed_truncation_matrix_families']:
    if row['family'] in ('one-cross scalar-contact row alpha_sc','scalar-zero row alpha_11'):
        print(row['family'], '::', row['status'])
theta=data['theta_3_common_finite_window_record']
print('theta3 row:', theta['row_value'])
print('theta3 scalar projection:', theta['scalar_projection'])
for res in data['finite_row_primitive_search_results']:
    if res['case']=='theta_3_current_finite_row_subcomplex':
        print('theta3 current primitive exists:', res['primitive_exists'])
        print('theta3 current obstruction value:', res['obstruction_value_on_residual'])
PY
git diff --check -- reconstitution/costello-local-scalar-source-repair-push-2026-04-30.md reconstitution/swarm-2026-04-30-agent-259-costello-local-scalar-source-repair-push.md
grep -n '[[:blank:]]$' reconstitution/costello-local-scalar-source-repair-push-2026-04-30.md reconstitution/swarm-2026-04-30-agent-259-costello-local-scalar-source-repair-push.md
git diff --cached --name-status
git add -- reconstitution/costello-local-scalar-source-repair-push-2026-04-30.md reconstitution/swarm-2026-04-30-agent-259-costello-local-scalar-source-repair-push.md
git diff --cached --check -- reconstitution/costello-local-scalar-source-repair-push-2026-04-30.md reconstitution/swarm-2026-04-30-agent-259-costello-local-scalar-source-repair-push.md
git status --short -- reconstitution/costello-local-scalar-source-repair-push-2026-04-30.md reconstitution/swarm-2026-04-30-agent-259-costello-local-scalar-source-repair-push.md
git diff --cached --name-status -- reconstitution/costello-local-scalar-source-repair-push-2026-04-30.md reconstitution/swarm-2026-04-30-agent-259-costello-local-scalar-source-repair-push.md
```

Observed outputs:

- Negative source searches for `current-valued`, `D'_c`, and
  `bulk-to-defect` returned no hits in the listed Costello/Costello--Li/
  Costello--Gwilliam mirrors.
- Finite CE check:
  `CE cocycle failures through bidegree<6: 0`,
  `omega(z1,z2)= 1`, and the reduced exactness test gives
  `-eta(0)=0`.
- `python3 -m py_compile scripts/finite_window_graph_array.py` passed.
- `python3 scripts/finite_window_graph_array.py` emitted valid JSON;
  `python3 -m json.tool` passed after the script completed. One premature
  parallel `json.tool` invocation was attempted before the redirected JSON
  file was complete and returned `Expecting value`; the rerun above passed.
- Script extraction confirmed:
  `alpha_sc` is computed with zero value in the full-equivariant branch,
  `alpha_11` is a computed zero row,
  `theta3 scalar projection: 0`,
  and `theta3 current primitive exists: False` with obstruction value `1`.
- `git diff --check` and `git diff --cached --check` passed on the two owned
  reports.
- The trailing-whitespace scan returned no hits.
- The two owned reports are staged. A large pre-existing staged set was
  present before this agent's `git add`; it was left untouched.

## Files Changed

- `reconstitution/costello-local-scalar-source-repair-push-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-259-costello-local-scalar-source-repair-push.md`

No PDF build was run.
