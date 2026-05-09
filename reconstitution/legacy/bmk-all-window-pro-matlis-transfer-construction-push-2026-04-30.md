# BMK All-Window / Pro-Matlis Transfer Construction Push, 2026-04-30

Scope: report-only construction push for the all-window/pro-Matlis BMK
transfer after the strict finite quotient and projected finite
\(L_\infty\) escape package have both been obstructed.  No manuscript TeX
is edited.

## Verdict

The finite boundary-mode obstruction is healed only by retaining the whole
Matlis tail.  Once this is done, the obstruction moves from finite
Hamiltonian invariance to topology.

There is a strongest positive one-pair construction:

\[
  \bar\partial H_\chi^0+H_\chi^0\bar\partial
    =
  \operatorname{id}-I_{\mathrm{an}}P_{\mathrm{an}}
\]

on the single-pair analytic BMK retract, after the diagonal orientation is
fixed and collar terms are quotiented.  Passing through Taylor moments gives
a compatible pro-analytic moment map

\[
  P_{\Pi}^{\mathrm{an}}\colon
  C^\bullet(B_2,B_1)\longrightarrow
  \mathcal P_{\mathrm{an}}(B_1)
  \subset
  \widehat{\mathcal P}_{\Pi}
  =
  \prod_{a+b>0}\C\rho_{a,b}.
\]

This is not the native all-window direct-sum Matlis current transfer.  The
native cotangent module remains

\[
  \mathcal P
  =
  \bigoplus_{a+b>0}\C\rho_{a,b}
  \cong \mathfrak h^\vee_{\mathrm{cont}},
  \qquad
  \mathfrak h=\C[[z_1,z_2]]/\C\cdot1 .
\]

The product/pro target accepts the all-window moment sequence, but it loses
two native structures: an arbitrary element of
\(\widehat{\mathcal P}_\Pi\) is not a compactly supported current at the
collision point, and the full formal Hamiltonian algebra does not act on
\(\widehat{\mathcal P}_\Pi\).  It carries at most the polynomial
Hamiltonian action, or an analytic/growth-restricted action after a new
bornology is declared.

Thus the theorem-grade outcome is:

1. constructed: one-pair analytic pro-Matlis BMK retract with compatible
   finite projections;
2. obstructed: strict native all-window direct-sum Matlis current transfer
   from the full compact-support current complex;
3. obstructed: strict pro-product current transfer for the full formal
   Hamiltonian algebra.

## Inputs Read

- `CLAUDE.md`.
- `AGENTS.md`.
- `/Users/raeez/ecosystem/INVARIANTS.md`.
- `/Users/raeez/ecosystem/AGENTS-HARNESS.md`.
- `~/topological-strings/.agents/skills/chriss-ginzburg-rectify/SKILL.md`.
- `~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`.
- `commands.tex`, `mathmacros.tex`, `notation.tex`.
- `main.tex:1210-1561`, especially
  Proposition `prop:finite-window-bm-native-e2-transfer`.
- `appendix-factorization-current-conventions.tex:1-230`,
  `360-780`, especially
  Theorem `thm:app-finite-window-bmk-current-transfer`.
- `appendix-matlis-principal-parts.tex:1-330`.
- `open-obligations.tex:880-1030`.
- `claim-strength-ledger.tex:540-660`.
- `theorem-lanes.tex:200-330`.
- `local-dictionary.tex:1-140`.
- `references/primary-sources/matlis-local-cohomology-residue-anchor.md`.
- `reconstitution/bmk-finite-current-quotient-construction-push-2026-04-30.md`.
- `reconstitution/bmk-projected-finite-window-linfty-escape-operations-2026-04-30.md`.
- `reconstitution/bmk-boundary-mode-obstruction-integration-spec-2026-04-30.md`.
- `reconstitution/bm-transfer-native-e2-construction-2026-04-30.md`.
- Reports 206, 211, 222, 268, 284, 286, 292.

## Direct-Sum Versus Pro-Matlis

The direct-sum Matlis module is the continuous dual of the formal
Hamiltonian algebra:

\[
  \mathcal P
  =
  \varinjlim_N\mathcal P_{\leq N}
  =
  \bigoplus_{0<a+b}\C\rho_{a,b}
  \cong
  \mathfrak h^\vee_{\mathrm{cont}} .
\]

This is the module on which the full formal Hamiltonian action is defined.
For each basis vector only a finite jet of \(f\in\mathfrak h\) contributes,
as proved in `appendix-matlis-principal-parts.tex:219-244`.

The pro object

\[
  \widehat{\mathcal P}_{\Pi}
  =
  \varprojlim_N\mathcal P_{\leq N}
  =
  \prod_{0<a+b}\C\rho_{a,b}
\]

is different.  It is the coordinate receptacle for all Taylor moments.  It
pairs naturally with polynomial Hamiltonians.  It does not pair with an
arbitrary formal power series unless an additional convergence structure is
imposed.

The analytic pro-Matlis subspace relevant to BMK is not the whole product.
It is the Taylor-coordinate image

\[
  \mathcal P_{\mathrm{an}}(B_1)
  =
  \tau\bigl(\mathcal O(B_1)^\vee_{\mathrm{red}}\bigr)
  \subset
  \widehat{\mathcal P}_{\Pi},
  \qquad
  \tau(\lambda)=(\lambda(z_1^az_2^b))_{a+b>0}.
\]

Polynomials are dense in \(\mathcal O(B_1)\), so \(\tau\) is injective.
The image is cut out by analytic growth conditions depending on \(B_1\).
A compactly supported top Dolbeault current has such a pro-analytic moment
sequence.  It need not have finite support in \((a,b)\).

## Positive One-Pair Construction

Assume the full analytic BMK contraction has been supplied on the
single-pair relative/collar complex:

\[
  \bar\partial H_\chi+H_\chi\bar\partial
    =
  \operatorname{id}-I_{\mathrm{an}}P_{\mathrm{an}}+E_\chi ,
\]

where \(P_{\mathrm{an}}\colon C^\bullet(B_2,B_1)\to
\mathcal O(B_1)^\vee\) is the analytic moment map and
\(I_{\mathrm{an}}\) is a chosen closed-current representative map.  After
passing to the collar quotient \(E_\chi=0\).  Normalize

\[
  H_\chi^0
    =
  (1-I_{\mathrm{an}}P_{\mathrm{an}})H_\chi
  (1-I_{\mathrm{an}}P_{\mathrm{an}}).
\]

With the usual side conditions \(P_{\mathrm{an}}I_{\mathrm{an}}=1\) and
\(H_\chi^0I_{\mathrm{an}}=0\), this gives

\[
  \bar\partial H_\chi^0+H_\chi^0\bar\partial
    =
  \operatorname{id}-I_{\mathrm{an}}P_{\mathrm{an}}.
\]

Composing with \(\tau\) gives the all-window pro-analytic moment map

\[
  P_{\Pi}^{\mathrm{an}}=\tau P_{\mathrm{an}}.
\]

The finite maps are compatible:

\[
  \pi_NP_{\Pi}^{\mathrm{an}}=p_N,\qquad
  \pi_{M,N}p_M=p_N .
\]

Thus the strongest constructed object is a compatible tower of finite
BMK moment identities controlled by a single analytic retract.  It is
one-pair and analytic.  It is not support-local factorization data, because
\(I_{\mathrm{an}}\) is a chosen representative map for analytic
functionals, not the derivative-delta section of the direct-sum Matlis
module.

## Why Direct-Sum All-Window Fails

For a general compact-support top current \(\alpha\), the all-moment
sequence

\[
  \operatorname{mom}_\infty(\alpha)
  =
  \left(
    \int_B z_1^az_2^b\alpha^{0,2}\wedge dz_1\wedge dz_2
  \right)_{a+b>0}
\]

lies in \(\widehat{\mathcal P}_\Pi\), not in \(\mathcal P\).  If
\(\alpha\) is a smooth compactly supported top form concentrated near a
point with \(z_1\neq0\), then the moments in the line \(b=0\) are nonzero
for infinitely many \(a\).  Hence the class

\[
  \operatorname{ob}_{\oplus}(\alpha)
  =
  [\operatorname{mom}_\infty(\alpha)]
  \in
  \widehat{\mathcal P}_\Pi/\mathcal P
\]

is nonzero.  This is the manuscript's
\(\operatorname{ob}_{\mathrm{mom}}\).  It is not a proof gap; it is the
exact obstruction to replacing the finite maps \(p_N\) by a direct-sum
all-window moment map on the full current complex.

## Why The Product Target Is Not A Native Current Target

The formal sum

\[
  \sum_{a+b>0} c_{a,b}\Delta_{a,b}
\]

does not define a compactly supported distribution for arbitrary
\((c_{a,b})\in\widehat{\mathcal P}_\Pi\).  A distribution supported at a
single point has finite order, hence is a finite linear combination of
derivatives of \(\delta_0\).  Therefore there is no support-local current
section

\[
  i_\Pi\colon
  \widehat{\mathcal P}_\Pi\longrightarrow
  \mathcal D'_0{}^{0,2}(B)
\]

extending all \(i_N\).  Infinite-order analytic functionals may be used
after changing habitat from compactly supported currents to analytic
functionals or hyperfunction-type objects.  That is a different target.

The exact obstruction entry is

\[
  \operatorname{ob}_{I_\Pi}
  =
  [(\Delta_{a,b})_{a+b>0}]
  \in
  \operatorname{coker}
  \left(
    \operatorname{Hom}_{\mathrm{cont}}
    (\widehat{\mathcal P}_\Pi,\mathcal D'_0{}^{0,2}(B))
    \to
    \varprojlim_N
    \operatorname{Hom}(\mathcal P_{\leq N},\mathcal D'_0{}^{0,2}(B))
  \right).
\]

Concretely, the compatible finite derivative-delta sections do not have a
limit in the current category.

## Why The Full Formal Hamiltonian Action Does Not Extend To The Product

The direct-sum module \(\mathcal P\) carries the full formal action because
each basis vector sees only a finite jet of \(f\).  The product module has
the opposite problem: a low output coefficient can receive contributions
from infinitely many high input coefficients.

Take

\[
  f=\sum_{p\geq2}z_1^p\in\mathfrak h,\qquad
  \lambda=\sum_{p\geq2}\rho_{p-1,0}\in\widehat{\mathcal P}_\Pi .
\]

For each \(p\geq2\),

\[
  z_1^p\cdot\rho_{p-1,0}=-p\,\rho_{0,1}.
\]

Thus the coefficient of \(\rho_{0,1}\) in \(f\cdot\lambda\) would be

\[
  -\sum_{p\geq2}p,
\]

which is not a complex number.  Hence the action map

\[
  \mathfrak h\times\widehat{\mathcal P}_\Pi
  \longrightarrow
  \widehat{\mathcal P}_\Pi
\]

is not defined in the native topology.  It exists on
\(\mathcal P\), and it exists on \(\widehat{\mathcal P}_\Pi\) for
polynomial Hamiltonians.  It may exist on analytic/growth-restricted
subspaces after a bornology is chosen.  It is not the formal-local
Hamiltonian action of the manuscript.

The exact obstruction entry is

\[
  \operatorname{ob}_{\mathfrak h,\Pi}
  =
  [\operatorname{ad}^{\vee}_{\mathfrak h}]
  \in
  \operatorname{coker}
  \left(
    \operatorname{Bil}_{\mathrm{cont}}
    (\mathfrak h,\widehat{\mathcal P}_\Pi;\widehat{\mathcal P}_\Pi)
    \to
    \varprojlim_N
    \operatorname{Bil}
    (\mathfrak h,\mathcal P_{\leq N};\mathcal P_{\leq N})
  \right),
\]

detected by the divergent \(\rho_{0,1}\)-coefficient above.

## Collar Primitive Obstruction

The single-pair collar quotient kills \(E_\chi\).  A native factorization
transfer needs compatible primitives, not only a quotient for one nested
pair.  For inclusions and disjoint products one needs operators
\(C_{\chi,N}\), \(R_{j,N}\), and \(R_{\mu,N}\) such that

\[
  \bar\partial C_{\chi,N}+C_{\chi,N}\bar\partial=E_{\chi,N},
\]

\[
  j_!C_{\chi_U,N}-C_{\chi_V,N}j_!
    =
  \bar\partial R_{j,N}+R_{j,N}\bar\partial,
\]

and

\[
  \mu(C_{\chi_U,N}\otimes1+1\otimes C_{\chi_V,N})
  -C_{\chi_{U\sqcup V},N}\mu
    =
  \bar\partial R_{\mu,N}+R_{\mu,N}\bar\partial .
\]

These identities must also commute with \(\pi_{M,N}\) and satisfy the
same estimates as \(H_\chi^0\).  No such compatible collar primitive
system is constructed in the current manuscript.

The exact obstruction entry is the Cech/Roos class

\[
  \operatorname{ob}_{\mathrm{collar},\Pi}
  =
  \left[
    (E_{\chi,N},
     j_!C_{\chi_U,N}-C_{\chi_V,N}j_!,
     \mu(C_{\chi_U,N}\otimes1+1\otimes C_{\chi_V,N})
       -C_{\chi_{U\sqcup V},N}\mu,
     \pi_{M,N}C_{\chi,M}-C_{\chi,N}\pi_{M,N})
  \right]_{M\geq N}.
\]

Vanishing of this class is exactly the missing collar primitive theorem.

## Ternary Transfer Obstruction

After the finite-current gate is replaced by a genuine all-window habitat,
the first higher transfer row is

\[
  \operatorname{Ob}_3^\chi(x,y,z)
    =
  p[H_{\mathrm{BM}}([ix,iy]-i\ell_2^{\mathrm{BM}}(x,y)),iz]
  +\operatorname{cyc}_{x,y,z}.
\]

On separated support strata it vanishes by the BMK estimates.  On the
coefficient collision stratum its non-collar part is the Jacobiator of
\(\mathfrak h\ltimes\mathcal P[1]\), hence zero.  The remaining term is a
small-diagonal/collar primitive problem in the same completed habitat.

The exact obstruction entry is

\[
  \operatorname{ob}_{3,\Pi}
  =
  [(\operatorname{Ob}_{3,N}^{\chi})_N]
  \in
  H^0
  \operatorname{Hom}
  \bigl((\mathfrak h\ltimes\mathcal P[1])^{\otimes3},
        \widehat{\mathcal P}_\Pi\bigr)
  \big/
  \operatorname{im}
  (\bar\partial C_{3,\Pi}+C_{3,\Pi}\bar\partial),
\]

with the understanding that the Hom complex must first be replaced by a
habitat on which \(H_\chi^0\), the moment map, and the Hamiltonian action
are all defined.

## Uniform Estimate Obstruction

Product topology gives coordinatewise convergence.  It does not give the
uniform finite-window estimates required by the native current transfer.
Two elementary estimates already show the failure.

First, the derivative-delta section has increasing distribution order:

\[
  i_N(\rho_{a,b})
  =
  \frac{(-1)^{a+b}}{a!b!}
  \partial_{z_1}^a\partial_{z_2}^b\delta_0\,
  d\bar z_1\wedge d\bar z_2 .
\]

In a fixed current seminorm controlled by \(C^s\)-tests, the norm of
\(\Delta_{a,b}\) is not finite once \(a+b>s\).  Hence no fixed \(s\)
controls the sections \(i_N\) uniformly in \(N\).

Second, if \(\alpha\) is supported in \(|z|\leq r\), then

\[
  \left|
    \int z_1^az_2^b\alpha^{0,2}\wedge dz_1\wedge dz_2
  \right|
  \leq
  C_\alpha r^{a+b}.
\]

This is an analytic growth estimate, not an \(\ell^\infty_N\)-uniform
direct-sum estimate.  The correct positive replacement is a radius-loss
Kothe/analytic-functional topology.  That replacement is not the current
topology declared in the factorization-current appendix.

The exact obstruction entry is the existing uniformity class sharpened to

\[
  \operatorname{ob}_{\mathrm{unif},\Pi}
  =
  \left(\left[(C_{s,N}^{I,H,p,E,3})_{N\geq1}\right]\right)_s
  \in
  \prod_s
  \left(
    \prod_{N\geq1}\R_{\geq0}/\ell^\infty_N
  \right),
\]

where \(C_{s,N}^{I,H,p,E,3}\) are the optimal constants for
\(i_N\), \(H_{\chi,N}^0\), \(p_N\), collar primitives, and the ternary row.
For the current section alone this class is nonzero in the unweighted
current topology.

## Final Obstruction Vector

After fixing the diagonal convention, the all-window/pro-Matlis transfer
is controlled by

\[
  \operatorname{Ob}^{\Pi}_{\mathrm{BM}}
  =
  \left(
    \operatorname{ob}_{\oplus},
    \operatorname{ob}_{I_\Pi},
    \operatorname{ob}_{\mathfrak h,\Pi},
    \operatorname{ob}_{\mathrm{collar},\Pi},
    \operatorname{ob}_{3,\Pi},
    \operatorname{ob}_{\mathrm{unif},\Pi}
  \right).
\]

The entries have the following status.

- \(\operatorname{ob}_{\oplus}\) is nonzero on the full compact-support
  current complex.  It is the failure of all moments to land in the
  direct-sum Matlis module.
- \(\operatorname{ob}_{I_\Pi}\) is nonzero in the compact-current category.
  Infinite pro-Matlis derivative-delta sums are not distributions.
- \(\operatorname{ob}_{\mathfrak h,\Pi}\) is nonzero for the full formal
  Hamiltonian algebra.  The product target does not carry the native
  coadjoint action.
- \(\operatorname{ob}_{\mathrm{collar},\Pi}\) is unconstructed.  It is the
  exact collar primitive compatibility class.
- \(\operatorname{ob}_{3,\Pi}\) is unconstructed.  Its coefficient part is
  zero, but the collar/small-diagonal primitive is not supplied.
- \(\operatorname{ob}_{\mathrm{unif},\Pi}\) is nonzero in the unweighted
  current topology; it may be replaced by a radius-loss analytic estimate
  only after changing habitat.

## Claim Status Recommendation

- Proved: retaining the full direct-sum Matlis tail removes the finite
  boundary-mode quotient obstruction.
- Constructed: one-pair analytic pro-Matlis BMK retract with compatible
  finite projections, conditional on the full analytic BMK contraction,
  side conditions, diagonal orientation, and collar quotient.
- Proved obstruction: direct-sum all-window moment map from the full
  current complex does not exist.
- Proved obstruction: pro-product Matlis does not admit a support-local
  compact-current section.
- Proved obstruction: pro-product Matlis does not carry the full formal
  Hamiltonian action.
- Proved obstruction: unweighted current seminorms do not give uniform
  all-window estimates for the derivative-delta sections.
- Open construction target: a new analytic/bornological factorization
  habitat with radius-loss estimates, polynomial or convergent Hamiltonian
  action, compatible collar primitives, and a ternary small-diagonal
  primitive.

## Commands Run

```bash
sed -n '1,240p' CLAUDE.md
sed -n '1,280p' AGENTS.md
sed -n '1,220p' /Users/raeez/ecosystem/INVARIANTS.md
sed -n '1,260p' /Users/raeez/ecosystem/AGENTS-HARNESS.md
sed -n '1,220p' /Users/raeez/topological-strings/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '1,260p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
rg -n -e 'BMK' -e 'Matlis' -e 'pro-Matlis' -e 'finite window' -e 'finite-window' -e 'current quotient' -e 'H_\\chi' -e 'collar' -e 'all-window' main.tex appendix-factorization-current-conventions.tex appendix-matlis-principal-parts.tex reconstitution
sed -n '1,520p' reconstitution/bmk-projected-finite-window-linfty-escape-operations-2026-04-30.md
sed -n '1,620p' reconstitution/bmk-finite-current-quotient-construction-push-2026-04-30.md
nl -ba main.tex | sed -n '1210,1568p'
nl -ba appendix-factorization-current-conventions.tex | sed -n '1,230p'
nl -ba appendix-factorization-current-conventions.tex | sed -n '360,780p'
nl -ba appendix-matlis-principal-parts.tex | sed -n '1,330p'
sed -n '1,280p' reconstitution/swarm-2026-04-30-agent-222-bm-all-window-transfer-supremum-rework.md
sed -n '1,680p' reconstitution/bm-transfer-native-e2-construction-2026-04-30.md
sed -n '1,320p' reconstitution/swarm-2026-04-30-agent-206-bm-transfer-native-e2-construction.md
sed -n '1,320p' reconstitution/swarm-2026-04-30-agent-211-bm-transfer-main-integration.md
sed -n '1,320p' reconstitution/bmk-boundary-mode-obstruction-integration-spec-2026-04-30.md
sed -n '1,320p' reconstitution/swarm-2026-04-30-agent-286-bmk-boundary-mode-obstruction-integration-spec.md
sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-268-bmk-koppelman-source-fixture.md
rg -n -e 'Ob\\^\\{\\\\infty\\}' -e 'ob_\\{\\\\mathrm\\{mom\\}\\}' -e 'pro-Matlis' -e 'direct-sum' -e 'completed all-window' -e 'all-window' -e 'Matlis' open-obligations.tex claim-strength-ledger.tex theorem-lanes.tex local-dictionary.tex reconstitution/*.md
nl -ba open-obligations.tex | sed -n '880,1030p'
nl -ba claim-strength-ledger.tex | sed -n '540,660p'
nl -ba theorem-lanes.tex | sed -n '200,330p'
nl -ba local-dictionary.tex | sed -n '1,140p'
python3 - <<'PY'
for M in [3, 5, 10]:
    coeff = 0
    terms = []
    for p in range(2, M + 1):
        i, j, q = p - 1, 0, 0
        target = (i - p + 1, j - q + 1)
        c = -(p*j - q*i + p - q)
        assert target == (0, 1)
        coeff += c
        terms.append(c)
    print(M, terms, coeff)
PY
rg -n -F -e 'rho_{N+1,0}' -e 'z_1^{N+2}' -e 'Ob}^{\\infty}_{\\mathrm{BM}' -e 'widehat{\\mc P}_{\\Pi}' -e 'Q_{\\mathrm{mom}}' main.tex appendix-factorization-current-conventions.tex appendix-matlis-principal-parts.tex reconstitution/bmk-finite-current-quotient-construction-push-2026-04-30.md reconstitution/bmk-projected-finite-window-linfty-escape-operations-2026-04-30.md
git status --short
```
