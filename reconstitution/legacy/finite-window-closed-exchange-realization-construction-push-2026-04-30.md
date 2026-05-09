# Finite-Window Closed-Exchange Realization Construction Push

Date: 2026-04-30.

Scope: ordinary scalar-reduced \(\mathfrak{gl}_N\) brane-defect QME
branch.  This is a report-only construction push.  No manuscript or
script file is modified.

## Verdict

There is a minimal algebraic defect-supported cone that solves the scalar
finite-window equations after one adjoins a new central closed source line.
It is not a construction from the closed Costello-local bulk sector already
present in the manuscript.  Under the stricter reading of closed exchange as
an actual Costello-local closed field, bulk-to-defect propagator, source
face, scalar-contact projection gate, and compatible counterterm tower, the
ordinary scalar-reduced branch remains obstructed.

The obstruction is exact.  The gate obstruction is the first scalar-lift
class \(o_{\sigma,w}^{(1)}=\hbar N[\bar c]\).  If a scalar-contact gate is
assumed and a candidate closed-exchange tower is supplied, the next
obstructions are
\[
  \beta^{\mathrm{sc}}_M,\qquad
  \beta^{\mathrm{sc}}_{\mathrm{cl}},\qquad
  \mu^{\mathrm{sc}}_{\mathrm{cl}},\qquad
  \lambda^{\mathrm{sc}}_{C}.
\]

## Anchors

- `appendix-unreduced-bv-qme.tex:53-111`: local scalar cocycle
  \(\omega(f,g)=[\{f,g\}]_0\), \(\omega(z_1,z_2)=1\), finite windows do not
  change this local scalar datum.
- `appendix-unreduced-bv-qme.tex:135-183`: scalar-symbol map is only
  associated-graded until a filtered chain projection
  \(\widehat\sigma_{\mathrm{sc}}\) is constructed.
- `appendix-unreduced-bv-qme.tex:236-305`: in the ordinary branch the first
  scalar-lift obstruction evaluates to
  \(\hbar N\,\omega(f,g)\gamma_{\mathbf 1}\), nonzero on
  \((z_1,z_2)\).
- `appendix-unreduced-bv-qme.tex:560-589`: the primitive
  \(\eta(f)=-[f]_0\) exists on \(A=\C[z_1,z_2]\) and does not descend to
  \(\bar A=A/\C\cdot1\).
- `appendix-unreduced-bv-qme.tex:591-685`: scalar QME class
  \(\hbar N[\bar c]\) is not exact in the scalar-reduced source.
- `main.tex:7569-7643`: ordinary scalar branch, central-character branch,
  balanced-supertrace branch, and the necessary closed-exchange equation.
- `main.tex:8022-8194`: scalar-contact gate first, then finite-window
  closed-exchange criterion and Roos obstructions.
- `tate-T1-weighted-completion.tex:1526-1735`: fixed-window image
  criterion and the \(\beta,\mu,\lambda\) inverse-system theorem.
- `reconstitution/scalar-qme-closed-exchange-construction-target-2026-04-30.md:62-265`:
  scalar closed-exchange target equations.

## Algebraic Cone Attempt

Let \(M\geq M_0\) be a transported finite window containing \(z_1,z_2\).
Let \(\bar A_{\mathrm{fw},M}\) denote the finite-window scalar source used
by the scalar-symbol target, with bracket transported from the accepted
finite-window machinery.  Define
\[
  \bar c_M(f,g)=[\{f,g\}_{\Omega_{\mathrm{loc}}}]_0,
  \qquad \bar c_M(z_1,z_2)=1.
\]
The CE cocycle equation is
\[
  \bar c_M([f,g],h)+\bar c_M([g,h],f)+\bar c_M([h,f],g)=0.
\]
It is non-exact on the scalar quotient: if
\(\bar c_M=d_{\mathrm{CE}}\eta_M\), then
\[
  1=\bar c_M(z_1,z_2)
    =(d_{\mathrm{CE}}\eta_M)(z_1,z_2)
    =-\eta_M(\{z_1,z_2\}_{\bar A_{\mathrm{fw},M}})
    =-\eta_M(0)=0.
\]

Adjoin an opposite central closed source line
\[
  \bar A^{\mathrm{cl}}_{-\hbar N\bar c}
    =\bar A\oplus \C K_{\mathrm{cl}},
  \qquad
  [(f,aK),(g,bK)]
    =
  (\{f,g\}_{\bar A},-\hbar N\bar c(f,g)K).
\]
The minimal defect-supported cone is
\[
  \mathcal X^{1,\mathrm{alg}}_{\mathrm{sc},w,M}(I)
    =\C[[\hbar]]\,e_M,
  \qquad
  \mathcal X^{0,\mathrm{alg}}_{\mathrm{sc},w,M}(I)=0,
  \qquad
  d^X_Me_M=0.
\]
For \(M\geq N\geq M_0\), set
\[
  \rho^X_{M,N}(e_M)=e_N,
  \qquad R^M_{w,w'}(e_M)=e_M.
\]
Define the scalar contact map
\[
  \Xi^{\mathrm{alg},\mathrm{sc}}_M(e_M)
    (\gamma_{\mathbf 1};a,f;b,g)
   =
  -\hbar N\,\bar c_M(f,g)
  \int_I a(t)b(t)\gamma_{\mathbf 1}(t)\,dt .
\]
Then
\[
  d_M\Xi^{\mathrm{alg},\mathrm{sc}}_M(e_M)=0,
  \qquad
  \pi_{M,N}\Xi^{\mathrm{alg},\mathrm{sc}}_M(e_M)
    =
  \Xi^{\mathrm{alg},\mathrm{sc}}_N\rho^X_{M,N}(e_M),
\]
and the scalar symbol is
\[
  \widehat\sigma_{\mathrm{sc},M}
  \Xi^{\mathrm{alg},\mathrm{sc}}_M(e_M)
    =
  -\hbar N\,\bar c_M .
\]

Taking
\[
  W_M=e_M,\qquad C_M=0
\]
gives the formal scalar equation
\[
  \operatorname{Ob}_{\mathrm{sc},M}
    +\Xi^{\mathrm{alg},\mathrm{sc}}_M(W_M)
    +d_MC_M=0
\]
on the scalar contact line.  The fixed-window cokernel class vanishes:
\[
  \beta^{\mathrm{sc}}_M=0,
\]
because \(H^1(\widehat\sigma_{\mathrm{sc},M}\Xi_M)\) contains
\(-\hbar N[\bar c_M]\).  The representative Roos class vanishes since
\(\rho^X_{M+1,M}W_{M+1}-W_M=0\), hence
\[
  \mu^{\mathrm{sc}}_{\mathrm{cl}}=0.
\]
The counterterm Roos class also vanishes because the compatible primitive is
the zero family:
\[
  C_M=0,\qquad
  \pi_{M+1,M}C_{M+1}-C_M=0,\qquad
  \lambda^{\mathrm{sc}}_{C}=0.
\]

This is a valid algebraic central-contact extension.  It is not, by itself,
a Costello-local closed-exchange theorem.

## Hostile Audit

The cone above is rejected as a genuine closed-exchange realization in the
current ordinary branch for four reasons.

1. It adjoins the negative scalar contact as a generator.  It does not
   construct a closed bulk field, a finite-scale closed propagator, or a
   brane-restriction map whose boundary value is the displayed contact term.
2. It has no source-face computation.  A genuine \(\Xi_M\) must satisfy the
   Hom differential equation
   \[
     d_{\mathbf K,M}\Xi_M
       =
     d_M\Xi_M-\Xi_Md^X_M=0
   \]
   as a consequence of the closed-source differential and the brane-defect
   QME differential, not by declaring a one-dimensional cone.
3. It does not construct the scalar-contact projection gate on the original
   ordinary complex.  The manuscript proves that the first chain-defect of
   any ordinary filtered lift is
   \[
     o_{\sigma,w}^{(1)}(z_1,z_2)
       =
     \hbar N\gamma_{\mathbf 1}\neq0.
   \]
4. It supplies no Costello locality data: no wavefront rule, no small-diagonal
   extension, no local counterterm support, no RG compatibility, and no
   finite-window graph table.

Thus the algebraic cone is admissible only if the theorem explicitly changes
the branch by adding a defect-supported central closed source line.  Without
that addition it is just the negative of the obstruction.

## Obstruction Theorem

Fix the ordinary scalar-reduced \(\mathfrak{gl}_N\) branch with \(N>0\).
Assume no central-character source replacement and no balanced supertrace
open model.  Let \(M\geq M_0\) contain \(z_1,z_2\).

First, the scalar-contact projection gate is obstructed:
\[
  o_{\sigma,M}^{(1),\mathrm{sc}}
    =
  \hbar N[\bar c_M]
  \neq0.
\]
Consequently an actual filtered chain projection
\(\widehat\sigma_{\mathrm{sc},M}\) on the original ordinary scalar-reduced
complex is not constructed by the current manuscript data.

If one nevertheless assumes a gate and supplies a candidate finite-window
closed-exchange complex and cochain map
\[
  \Xi^{\mathrm{sc}}_M\colon
  \mathcal X^\bullet_{\mathrm{sc},w,M}(I)
  \to
  \mathfrak Q^\bullet_{\mathrm{sc},w,M}(I),
\]
then fixed-window scalar cancellation is possible if and only if
\[
  \hbar N[\bar c_M]
  \in
  \operatorname{im}\!\left(
    -H^1(\widehat\sigma_{\mathrm{sc},M}\Xi^{\mathrm{sc}}_M)
  \right).
\]
The exact fixed-window obstruction is
\[
  \beta^{\mathrm{sc}}_M
  =
  \left[\hbar N[\bar c_M]\right]
  \in
  \operatorname{coker}
  H^1(\widehat\sigma_{\mathrm{sc},M}\Xi^{\mathrm{sc}}_M).
\]
For the current genuine branch, the constructed closed-exchange input has
zero scalar image: the regular-density \(X/\Xi\) tower is scalar-zero and the
balanced-supertrace tower is a different open model.  Therefore
\(\beta^{\mathrm{sc}}_M\neq0\) in this branch.

In the inverse system the primary scalar closed-exchange obstruction is
\[
  \beta^{\mathrm{sc}}_{\mathrm{cl}}
  =
  \left[
    (\hbar N[\bar c_M])_M
  \right]
  \in
  \operatorname{coker}\!\left(
    \varprojlim_M H^1(\mathcal X^\bullet_{\mathrm{sc},w,M}(I))
    \xrightarrow{\ \varprojlim H^1(\widehat\sigma_{\mathrm{sc},M}
      \Xi^{\mathrm{sc}}_M)\ }
    \varprojlim_M H^1(\mathcal S^\bullet_M(I))
  \right).
\]
If \(\beta^{\mathrm{sc}}_{\mathrm{cl}}\neq0\), the branch is obstructed and
the secondary Roos classes are not reached.

If \(\beta^{\mathrm{sc}}_{\mathrm{cl}}=0\), choose a compatible cohomology
class \(\alpha=(\alpha_M)_M\) and cocycle representatives \(w_M\).  The
representative compatibility obstruction is
\[
  \mu^{\mathrm{sc}}_{\mathrm{cl}}(\alpha)
  =
  \left[([u_M])_M\right]
  \in
  \varprojlim\nolimits^1_M
  H^0(\mathcal X^\bullet_{\mathrm{sc},w,M}(I)),
\]
where
\[
  \rho^X_{M+1,M}w_{M+1}-w_M=d^X_Mu_M.
\]
If this class is nonzero, no compatible closed-exchange cocycle family
\((W_M)_M\) exists.

If compatible \(W_M\) exist, choose primitives
\[
  d_Mc_M=
  -\bigl(\operatorname{Ob}_{\mathrm{sc},M}
      +\Xi^{\mathrm{sc}}_M(W_M)\bigr).
\]
The counterterm compatibility obstruction is
\[
  \lambda^{\mathrm{sc}}_{C}(W)
  =
  \left[
    ([\pi_{M+1,M}c_{M+1}-c_M])_M
  \right]
  \in
  \varprojlim\nolimits^1_M
  H^0(\mathfrak Q^\bullet_{\mathrm{sc},w,M}(I)).
\]
It vanishes exactly when the primitives can be adjusted to compatible
finite-window counterterms \(C_M\).

Thus the genuine ordinary scalar-reduced closed-exchange theorem is not
proved by naming \(-\hbar N[\bar c]\).  It requires either the accepted
defect-supported central-contact source described above, or a Costello-local
closed-exchange tower whose scalar image contains that class and whose Roos
classes vanish.

## Verification Commands

Executed read-only verification:

```bash
rg -n "scalar|closed-exchange|beta|mu|lambda|Xi|scalar-contact|Roos" \
  main.tex open-obligations.tex claim-strength-ledger.tex \
  appendix-unreduced-bv-qme.tex local-dictionary.tex

nl -ba appendix-unreduced-bv-qme.tex | sed -n '236,305p'
nl -ba appendix-unreduced-bv-qme.tex | sed -n '591,685p'
nl -ba main.tex | sed -n '7569,7643p'
nl -ba main.tex | sed -n '8022,8194p'
nl -ba tate-T1-weighted-completion.tex | sed -n '1526,1735p'

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
monos=[(a,b) for a in range(5) for b in range(5) if (a,b)!=(0,0)]
fail=[]
for x,y,z in product(monos, repeat=3):
    s=0
    for coeff,e in bracket(x,y): s += coeff*omega(e,z)
    for coeff,e in bracket(y,z): s += coeff*omega(e,x)
    for coeff,e in bracket(z,x): s += coeff*omega(e,y)
    if s!=0:
        fail.append((x,y,z,s)); break
print('CE cocycle failures through bidegree<5:', len(fail))
print('omega(z1,z2)=', omega((1,0),(0,1)))
print('If eta descends to bar A then d eta(z1,z2)= -eta(0)=0, so omega non-exact on the quotient.')
PY

git diff --cached --check -- \
  reconstitution/finite-window-closed-exchange-realization-construction-push-2026-04-30.md \
  reconstitution/swarm-2026-04-30-agent-241-finite-window-closed-exchange-realization-construction-push.md
```

Observed computation:

```text
CE cocycle failures through bidegree<5: 0
omega(z1,z2)= 1
If eta descends to bar A then d eta(z1,z2)= -eta(0)=0, so omega non-exact on the quotient.
```
