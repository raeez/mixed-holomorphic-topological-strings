# BMK Finite Current Quotient Construction Push, 2026-04-30

Scope: report-only construction push beyond Agent 276.  No manuscript TeX
is edited.  The target is the finite-window current quotient, or a modified
\(H_{\chi,N}\), that would make
\[
  \bar\partial H_{\chi,N}+H_{\chi,N}\bar\partial
    =\operatorname{id}-i_Np_N+E_{\chi,N}
\]
true in the BMK lane.

## Verdict

There is a formal one-pair derived quotient on which the differential
identity is true, provided one first supplies the full analytic BMK
deformation retract and fixes the diagonal orientation convention.  This
quotient is not the desired finite support-local current quotient and is not
compatible with the native factorization/Hamiltonian current structure.

No strict finite-window current quotient that kills the scalar and high
moments while retaining \(\mathcal P_{\le N}\) can be compatible with the
full Hamiltonian action.  The killed high-current class
\(\rho_{N+1,0}\) is carried by the Hamiltonian \(z_1^{N+2}\) to the retained
class \(\rho_{0,1}\):
\[
  z_1^{N+2}\cdot\rho_{N+1,0}=-(N+2)\rho_{0,1}.
\]
Thus a quotient relation killing \(\rho_{N+1,0}\) is not a Hamiltonian
submodule relation.  The same failure already appears at the scalar line:
\[
  z_1\cdot\rho_{0,0}=-\rho_{0,1}.
\]
The finite window can be used as an output projection or as a homotopy
ledger.  It cannot be a strict native factorization current quotient unless
one changes the source to a truncated/projected \(L_\infty\) object carrying
the boundary leakage as structure.

## Inputs Read

- `CLAUDE.md`.
- `/Users/raeez/ecosystem/INVARIANTS.md`.
- `/Users/raeez/ecosystem/AGENTS-HARNESS.md`.
- `~/topological-strings/.agents/skills/chriss-ginzburg-rectify/SKILL.md`.
- `~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`.
- `commands.tex`, `mathmacros.tex`, `notation.tex`.
- `main.tex:1210-1510`.
- `appendix-factorization-current-conventions.tex:1-180`,
  `360-720`, `880-1010`, `1180-1245`.
- `appendix-matlis-principal-parts.tex:1-280`.
- `open-obligations.tex:900-1020`.
- `claim-strength-ledger.tex:560-630`.
- Reports 206, 211, 222, 241, 268, 276 and the BMK source anchor file.

## Diagonal Annulus Normalization

The diagonal annulus term is not a collar term.  Its scalar is fixed by
the angular integral of the displayed kernel.

Put \(|\eta|=1\) and parametrize
\[
  \eta_1=e^{i\alpha}\cos\phi,\qquad
  \eta_2=e^{i\beta}\sin\phi,\qquad
  0\leq\phi\leq\pi/2 .
\]
Then
\[
  \bigl(\bar\eta_1d\bar\eta_2-\bar\eta_2d\bar\eta_1\bigr)
    \wedge d\eta_1\wedge d\eta_2
  =
  -2\sin\phi\cos\phi\,
    d\phi\wedge d\alpha\wedge d\beta .
\]
Since \((2\pi i)^2=-4\pi^2\),
\[
  K_{\mathrm{BM}}|_{S^3}
  =
  \frac{\sin\phi\cos\phi}{2\pi^2}\,
    d\phi\wedge d\alpha\wedge d\beta .
\]
For the real orientation
\[
  dx_1\wedge dy_1\wedge dx_2\wedge dy_2
  =
  -r^3\sin\phi\cos\phi\,
    dr\wedge d\phi\wedge d\alpha\wedge d\beta ,
\]
the outward boundary orientation on \(S^3\) is
\(-d\phi\wedge d\alpha\wedge d\beta\).  Hence
\[
  \int_{S^3_{\mathrm{out}}}K_{\mathrm{BM}}=-1 .
\]
Therefore the annular cutoff limit satisfies
\[
  \bar\partial\vartheta_\epsilon(|\eta|)\wedge K_{\mathrm{BM}}
    \longrightarrow
  -[\Delta]_{\mathrm{real}}
\]
relative to the real outward orientation.  The manuscript's positive
identity is obtained only after one of the following convention choices is
made explicitly:

1. define the BMK diagonal current by
   \([\Delta]_{\mathrm{BM}}=-[\Delta]_{\mathrm{real}}\); or
2. reverse the sign of the displayed kernel, equivalently exchange the
   numerator order or the relative coordinate convention.

The derivative-delta factor
\[
  \Delta_{a,b}
  =
  \frac{(-1)^{a+b}}{a!b!}
  \partial_{z_1}^a\partial_{z_2}^b
  \delta_0\,d\bar z_1\wedge d\bar z_2
\]
fixes the Taylor sign.  It does not by itself fix the global diagonal
orientation scalar.  The BMK diagonal orientation must be tied to the
Matlis residue convention
\[
  \langle\Delta_{a,b},f\rangle
  =\operatorname{Res}_0(\rho_{a,b}f)
\]
before the sign in \(i_Np_N\) is theorem-grade.

## No Modified \(H_{\chi,N}\) on the Full Current Complex

Let \(C^\bullet\) be the relative compact-support Dolbeault current
complex after killing the single-pair collar \(B_2\setminus B_1\).  Let
\[
  \pi_N:H_c^{0,2}(B_1)\simeq \mathcal O(B_1)^\vee
    \longrightarrow \mathcal P_{\leq N}
\]
be the finite Taylor-moment map.  If a modified operator \(H_{\chi,N}\)
existed on the full relative complex with
\[
  \bar\partial H_{\chi,N}+H_{\chi,N}\bar\partial
    =\operatorname{id}-i_Np_N,
\]
then every closed top current \(T_\lambda\) whose cohomology class
\(\lambda\) lies in \(\ker\pi_N\) would be exact.  Choose a holomorphic
function \(f\) with \(\lambda(f)\neq0\).  Pairing the identity with \(f\)
gives
\[
  \lambda(f)
  =
  \langle T_\lambda,f\rangle
  =
  \langle \bar\partial H_{\chi,N}T_\lambda,f\rangle
  =
  \pm\langle H_{\chi,N}T_\lambda,\bar\partial f\rangle
  =
  0,
\]
a contradiction.  Agent 276 used derivative delta currents for this
attack.  The stronger statement is that the obstruction is the full kernel
of the finite moment map on \(\mathcal O(B_1)^\vee\), not only the
support-at-zero high derivatives.

## One-Pair Derived Quotient That Works

Assume the full analytic BMK contraction has been supplied:
\[
  \bar\partial H_\chi+H_\chi\bar\partial
    =
  \operatorname{id}-I_{\mathrm{an}}P_{\mathrm{an}}+E_\chi ,
\]
where \(P_{\mathrm{an}}\) is the compact-support Dolbeault moment map to
\(\mathcal O(B_1)^\vee\), \(I_{\mathrm{an}}\) is a chosen current
representative map, and \(E_\chi\) is killed in the single-pair collar
quotient.  Normalize the homotopy by
\[
  H_\chi^0
    =
  (1-I_{\mathrm{an}}P_{\mathrm{an}})
  H_\chi
  (1-I_{\mathrm{an}}P_{\mathrm{an}}).
\]
Then
\[
  \bar\partial H_\chi^0+H_\chi^0\bar\partial
    =
  \operatorname{id}-I_{\mathrm{an}}P_{\mathrm{an}},
  \qquad
  H_\chi^0 I_{\mathrm{an}}=0 .
\]
Let \(K_N=\ker\pi_N\subset\mathcal O(B_1)^\vee\), choose the section of
\(\pi_N\) sending \(\rho_{a,b}\) to the derivative-delta class
\(\Delta_{a,b}\), and define
\[
  C_N^{\mathrm{der}}(B_2,B_1)
    =
  C^\bullet(B_2,B_1)\big/ I_{\mathrm{an}}(K_N).
\]
Because \(H_\chi^0I_{\mathrm{an}}(K_N)=0\), the homotopy descends.  In the
quotient,
\[
  I_{\mathrm{an}}P_{\mathrm{an}}
  \equiv
  i_Np_N,
\]
and therefore
\[
  \bar\partial \bar H_{\chi,N}
  +\bar H_{\chi,N}\bar\partial
    =
  \operatorname{id}-i_Np_N .
\]
This is the strongest positive construction found in this pass.

It has three defects.

First, \(I_{\mathrm{an}}(K_N)\) is not the finite support-at-zero current
span
\[
  \C\Delta_{0,0}\oplus
  \bigoplus_{a+b>N}\C\Delta_{a,b}.
\]
It also kills every analytic compact-support cohomology class with zero
selected finite moments.  Thus it is a global Serre-dual quotient, not a
finite current quotient.

Second, the representative map \(I_{\mathrm{an}}\) is not canonical on
\(K_N\).  Only the finite section \(i_N\) is fixed by the Matlis residue
normalization.  The killed classes generally cannot all be represented by
currents supported at the collision point.

Third, the quotient is not a native factorization quotient.  It depends on
the chosen collision point, chosen polydisk pair, full analytic moment
space, and chosen representatives for \(\ker\pi_N\).

## Failure of the Finite Support-Current Quotient

The tempting quotient
\[
  C^\bullet(B_2,B_1)\Big/
  \left(
    \C\Delta_{0,0}
    \oplus
    \bigoplus_{a+b>N}\C\Delta_{a,b}
  \right)
\]
does not make the differential identity true.  It kills only the
support-at-zero part of \(\ker\pi_N\).  A smooth compactly supported top
form can have all selected moments zero and still define a nonzero analytic
functional on some holomorphic function of degree \(>N\), or on a
non-polynomial holomorphic function.  Such a class pairs nontrivially with
holomorphic tests, hence cannot be a Dolbeault boundary.  The identity
would force it to be exact, contradicting Stokes.

Homotopy saturation,
\[
  \operatorname{Sat}_{\bar\partial,H_\chi}
  \left(
    \C\Delta_{0,0}
    \oplus
    \bigoplus_{a+b>N}\C\Delta_{a,b}
  \right),
\]
does give a chain quotient by definition, but it still does not give the
desired factorization-current quotient.  The saturation is not stable under
the Hamiltonian current action.

## Hamiltonian Invariance Obstruction

A factorization-current quotient retaining the bracket must have a relation
subspace \(R_N\) satisfying
\[
  \mathfrak h\cdot R_N\subset R_N .
\]
For finite moments this condition is false.  In the Matlis coadjoint
formula,
\[
  z_1^p z_2^q\cdot\rho_{i,j}
  =
  -(pj-qi+p-q)\rho_{i-p+1,j-q+1}.
\]
With \(p=N+2\), \(q=0\), \(i=N+1\), \(j=0\), one obtains
\[
  z_1^{N+2}\cdot\rho_{N+1,0}
  =
  -(N+2)\rho_{0,1}.
\]
The source \(\rho_{N+1,0}\) must be killed by a finite window
\(\mathcal P_{\le N}\), while the target \(\rho_{0,1}\) is retained for
every \(N\geq1\).  Therefore the finite moment kernel is not an
\(\mathfrak h\)-submodule.

The scalar line gives the same warning:
\[
  z_1\cdot\rho_{0,0}=-\rho_{0,1}.
\]
This is why scalar reduction must be performed at the Hamiltonian quotient
level, not by treating the full Matlis scalar current line as an ordinary
stable relation inside the unreduced current module.

Thus a finite-window quotient can be strict only after changing the acting
algebra to a projected/truncated operation.  That change produces boundary
defects and higher operations; it is no longer the full native Hamiltonian
factorization current algebra.

## Collar Factorization Compatibility

The single-pair collar quotient
\[
  \mathcal D'^{0,\bullet}(B_2)\to
  \mathcal D'^{0,\bullet}(B_2)/
  \mathcal D'^{0,\bullet}_{B_2\setminus B_1}(B_2)
\]
is valid for killing terms supported where \(d\chi\neq0\), after the
diagonal annulus has been separated.  A factorization quotient needs more.
For every inclusion and every disjoint product one needs
\[
  j_!R_N(B_2,B_1)\subset R_N(B'_2,B'_1),
\]
\[
  \mu\bigl(R_N(U),C(V)\bigr)+
  \mu\bigl(C(U),R_N(V)\bigr)
  \subset R_N(U\sqcup V),
\]
and
\[
  H_\chi R_N\subset R_N .
\]
The derived quotient \(I_{\mathrm{an}}(K_N)\) is nonlocal, not
support-defined, and not stable under the Hamiltonian action.  The finite
support-zero quotient is support-defined but fails the Hamiltonian
stability equation above.  Hence neither quotient supplies the collar
factorization datum required by the native \(E_2\) theorem surface.

## Obstruction Theorem

Fix \(N\geq1\).  Work in the local mixed HT BMK setting of
`main.tex:1242-1452` and
`appendix-factorization-current-conventions.tex:399-695`.  Suppose a
finite-window current quotient \(Q_N\) satisfies:

1. the classes \(i_N(\rho_{a,b})=\Delta_{a,b}\) for
   \(0<a+b\leq N\) survive and pair by the Matlis residue convention;
2. the scalar current and all high support-at-zero currents are killed;
3. the quotient is compatible with the full Hamiltonian current action and
   extension-by-zero factorization products; and
4. some operator \(H_{\chi,N}\) satisfies the normalized finite-window BMK
   differential identity on \(Q_N\).

Then \(Q_N\) does not exist.  Indeed, condition (2) kills
\(\rho_{N+1,0}\), while condition (3) forces its Hamiltonian translate
\[
  z_1^{N+2}\cdot\rho_{N+1,0}=-(N+2)\rho_{0,1}
\]
to be killed.  This contradicts condition (1), since \(\rho_{0,1}\) is in
\(\mathcal P_{\leq N}\).

Equivalently, the exact obstruction is
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

- \(\operatorname{ob}_{\mathrm{diag}}\) is the sign/scalar comparison
  between the annular BMK diagonal current and the Matlis
  derivative-delta convention.  With the displayed kernel and real outward
  orientation the angular mass is \(-1\).
- \(\operatorname{ob}_{\mathrm{an}/\mathrm{fin},N}\) is the quotient
  between the full analytic moment kernel \(\ker\pi_N\) and the smaller
  support-zero high-derivative span.  This class is nonzero unless the
  source complex is replaced by the derived analytic quotient.
- \(\operatorname{ob}_{\mathfrak h,N}\) is the Hamiltonian invariance
  defect
  \[
    \pi_N\bigl(\mathfrak h\cdot\ker\pi_N\bigr),
  \]
  nonzero by the displayed \(z_1^{N+2}\)-calculation.
- \(\operatorname{ob}_{\mathrm{collar\mbox{-}fact},N}\) is the failure of
  the quotient relation to be a cosheaf/factorization ideal under
  extension by zero, disjoint products, and the BMK homotopy.

After the diagonal convention is declared, the first entry can be set to
zero.  The Hamiltonian and collar-factorization entries remain nonzero for
a strict finite quotient.

## Next Construction Target

The next theorem target is not another strict finite current quotient.  The
finite quotient has been decided: it can close a single-pair derived
differential identity only by using the full analytic moment quotient, and
it cannot be the native factorization current quotient.

The correct construction target is one of the following two objects.

1. An all-window/pro-Matlis BMK transfer:
   retain the direct-sum Matlis module \(\mathcal P\), construct compatible
   \(H_\chi^0\), collar primitives, and uniform \(N\)-estimates.  This is
   the existing \(\operatorname{Ob}^{\infty}_{\mathrm{BM}}\) target.

2. A projected finite-window \(L_\infty\) factorization package:
   keep \(\mathcal P_{\leq N}\) as output data, but add explicit boundary
   operations for escaped modes
   \[
     \kappa_N(f,\rho)
       =
     \pi_N\bigl(f\cdot \tilde\rho\bigr)
   \]
   whenever \(\tilde\rho\in\ker\pi_N\).  The first required row is forced by
   \[
     \kappa_N(z_1^{N+2},\rho_{N+1,0})
       =
     -(N+2)\rho_{0,1}.
   \]
   The collar Cech/Roos class for these boundary operations is then the
   object to construct or obstruct.

The manuscript-facing formulation should therefore not say that the finite
window is a strict current quotient.  It should say: finite windows are
output projections for computations; strict quotient/factorization is
all-window, or else finite-window only after adding homotopy-coherent
escape operations.

## Commands Run

```bash
sed -n '1,260p' CLAUDE.md
sed -n '1,220p' /Users/raeez/topological-strings/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '1,260p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '1,220p' /Users/raeez/ecosystem/INVARIANTS.md
sed -n '1,260p' /Users/raeez/ecosystem/AGENTS-HARNESS.md
git status --short
rg -n "BMK|finite-window|finite window|H_\\{chi|H_chi|diagonal annulus|collar|current quotient|Agent 276|moment|current" .
sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-276-bmk-kernel-current-limit-construction-push.md
sed -n '260,560p' reconstitution/swarm-2026-04-30-agent-276-bmk-kernel-current-limit-construction-push.md
sed -n '1,280p' reconstitution/swarm-2026-04-30-agent-268-bmk-koppelman-source-fixture.md
sed -n '1,260p' references/primary-sources/bmk-koppelman-source-anchors-2026-04-30.md
sed -n '1,260p' reconstitution/bm-transfer-native-e2-construction-2026-04-30.md
sed -n '260,560p' reconstitution/bm-transfer-native-e2-construction-2026-04-30.md
sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-206-bm-transfer-native-e2-construction.md
sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-211-bm-transfer-main-integration.md
sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-222-bm-all-window-transfer-supremum-rework.md
sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-241-finite-window-closed-exchange-realization-construction-push.md
sed -n '1,260p' reconstitution/finite-window-closed-exchange-realization-construction-push-2026-04-30.md
nl -ba commands.tex | sed -n '1,220p'
nl -ba mathmacros.tex | sed -n '1,260p'
nl -ba notation.tex | sed -n '1,220p'
nl -ba main.tex | sed -n '1210,1510p'
nl -ba appendix-factorization-current-conventions.tex | sed -n '1,180p'
nl -ba appendix-factorization-current-conventions.tex | sed -n '360,720p'
nl -ba appendix-factorization-current-conventions.tex | sed -n '880,1010p'
nl -ba appendix-factorization-current-conventions.tex | sed -n '1180,1245p'
nl -ba appendix-matlis-principal-parts.tex | sed -n '1,280p'
nl -ba open-obligations.tex | sed -n '900,1020p'
nl -ba claim-strength-ledger.tex | sed -n '560,630p'
```
