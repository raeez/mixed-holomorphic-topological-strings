# Agent 206 Report: BM Transfer for Native E2 Construction

Date: 2026-04-30.
Owned files:

- `reconstitution/bm-transfer-native-e2-construction-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-206-bm-transfer-native-e2-construction.md`

No TeX file was edited.

## Claim Attacked

Agents 176 and 199 left the explicit Bochner-Martinelli transfer as the
missing construction for the native holomorphic \(E_2\) lane:
kernel, cutoff/support control, normalized \(\bar\partial\) homotopy,
arity-two Hamiltonian/coadjoint comparison, and first ternary
compatibility.

## Verdict

The transfer is now specified as a finite-window and support-at-collision
construction.  The correct homotopy kernel is the
Bochner-Martinelli-Koppelman current
\[
  K_{\mathrm{BM}}(\zeta,z)
  =
  \frac{1}{(2\pi i)^2}
  \frac{
    \overline{\zeta_1-z_1}(d\bar\zeta_2-d\bar z_2)
    -
    \overline{\zeta_2-z_2}(d\bar\zeta_1-d\bar z_1)
  }{|\zeta-z|^4}
  \wedge d\zeta_1\wedge d\zeta_2 .
\]
The form currently displayed in the theorem lane is its \(d\bar z=0\)
component; a full Dolbeault homotopy needs the displayed \(d\bar z\)
terms.

The normalized identity is
\[
  \bar\partial H_{\mathrm{BM},N}
  +H_{\mathrm{BM},N}\bar\partial
  =
  \operatorname{id}-i_Np_N
\]
on finite principal-part windows, with
\[
  p_N(\alpha)=
  \sum_{0<a+b\le N}
  \left(\int_B z_1^az_2^b\alpha^{0,2}dz_1dz_2\right)\rho_{a,b}.
\]
The support-at-zero inclusion uses
\[
  \Delta_{a,b}
  =
  \frac{(-1)^{a+b}}{a!\,b!}
  \partial_{z_1}^a\partial_{z_2}^b
  \delta_0\,d\bar z_1\wedge d\bar z_2,
  \qquad
  \langle\Delta_{a,b},f\rangle
  =
  \operatorname{Res}_0(\rho_{a,b}f).
\]

## Proof Status

| Transfer datum | Status |
|---|---|
| BM/Koppelman kernel | constructed with the required \(d\bar z\)-terms; the theorem-lane scalar BM form is only a component |
| cutoff support estimates | proved on fixed finite configuration strata; uniform all-window estimates remain open |
| normalized \(\bar\partial\) identity | proved in finite principal-part windows and relative to the cutoff collar; collar removal is part of \(\operatorname{Ob}^{\infty}_{\mathrm{BM}}\) |
| arity-two Hamiltonian bracket | proved: transfer gives \(\{f,g\}\) modulo constants |
| arity-two cotangent action | proved: transfer gives the Matlis coadjoint action |
| first ternary term | coefficient Jacobiator vanishes; the cutoff/collar small-diagonal term remains the exact obstruction |

## Arity-Two Result

For Hamiltonians,
\[
  \ell_2^{\mathrm{BM}}(f,g)=
  \partial_{z_1}f\,\partial_{z_2}g
  -
  \partial_{z_2}f\,\partial_{z_1}g
  \pmod{\mathbb C}.
\]
For \(f=z_1^pz_2^q\),
\[
  \ell_2^{\mathrm{BM}}(f,\rho_{i,j})
  =
  -(pj-qi+p-q)\rho_{i-p+1,j-q+1},
\]
with negative-index targets zero, and
\(\ell_2^{\mathrm{BM}}(\rho,\sigma)=0\).  This is exactly the Matlis
coadjoint action proved in the principal-part appendix.

## Ternary Compatibility

The first transfer obstruction is
\[
  \operatorname{Ob}_3^\chi(x,y,z)
  =
  p[H_{\mathrm{BM}}([ix,iy]-i\ell_2(x,y)),iz]
  +\text{cyclic Koszul terms}.
\]
For separated supports it vanishes by the kernel estimates.  On the
collision stratum the coefficient Jacobiator of
\(\mathfrak h\ltimes\mathcal P[1]\) vanishes.  The only remaining term is
a cutoff/collar contribution supported on the small diagonal.

## False VOA Attack

No one-variable reduction is used.  The principal-part face is the
two-variable Cauchy expansion
\[
  \frac{1}{(2\pi i)^2}
  \frac{d\zeta_1\wedge d\zeta_2}
       {(\zeta_1-z_1)(\zeta_2-z_2)}
  =
  \sum_{a,b\ge0}z_1^az_2^b\rho_{a,b}(\zeta).
\]
Killing \(z_2\) kills the Hamiltonian bracket; keeping only \(b=0\)
principal parts fails because \(z_1\cdot\rho_{a,0}=-\rho_{a,1}\).
A curve VOA/Zhu theorem remains downstream of the controlled
\(\mathbb C\times\mathbb R\) reduction retaining \(z_2\).

## Exact Remaining Obstruction

\[
  \operatorname{Ob}^{\infty}_{\mathrm{BM}}
  =
  (\operatorname{ob}_{\mathrm{mom}},
   \operatorname{ob}_{\mathrm{collar}},
   \operatorname{ob}_{3},
   \operatorname{ob}_{\mathrm{unif}}).
\]
The open point is the all-window strict theorem: prove that analytic
compact-support moments restrict uniformly to the direct-sum Matlis
module, cutoff collar terms vanish under extension-by-zero
factorization, \(\operatorname{Ob}_3^\chi=0\), and the estimates are
uniform in the \(m\)-adic window \(N\).  Without that, the honest theorem
surface is finite-window BM transfer plus arity-two comparison.

## Commands Run

```bash
sed -n '1,240p' CLAUDE.md
sed -n '1,220p' /Users/raeez/topological-strings/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '1,280p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '129,170p' /Users/raeez/ecosystem/INVARIANTS.md
sed -n '143,170p' /Users/raeez/ecosystem/AGENTS-HARNESS.md
sed -n '1,220p' AGENTS.md
git status --short
rg --files | rg '(^|/)(theorem-lanes|local-dictionary)\.tex$|agent-176|agent-199|176|199|CxR|controlled|reduction|bm|Bochner|Martinelli|native-e2|principal'
nl -ba theorem-lanes.tex | sed -n '220,530p'
nl -ba theorem-lanes.tex | sed -n '650,1015p'
nl -ba local-dictionary.tex | sed -n '1,380p'
nl -ba main.tex | sed -n '900,1250p'
nl -ba main.tex | sed -n '2680,2765p'
nl -ba main.tex | sed -n '2860,3005p'
nl -ba reconstitution/swarm-2026-04-30-agent-176-native-e2-lanes-0957.md | sed -n '1,170p'
nl -ba reconstitution/swarm-2026-04-30-agent-199-native-E2-factorization-construction.md | sed -n '1,260p'
nl -ba reconstitution/controlled-CxR-reduction-thread-2026-04-30.md | sed -n '1,700p'
nl -ba appendix-matlis-principal-parts.tex | sed -n '1,220p'
nl -ba appendix-factorization-current-conventions.tex | sed -n '120,200p'
nl -ba appendix-factorization-current-conventions.tex | sed -n '360,445p'
git diff --check -- reconstitution/bm-transfer-native-e2-construction-2026-04-30.md reconstitution/swarm-2026-04-30-agent-206-bm-transfer-native-e2-construction.md
rg -n -F -e "Bochner-Martinelli-Koppelman" -e "Ob^{\\infty}_{\\mathrm{BM}}" -e "d\\bar\\eta" -e "z_1\\cdot\\rho_{a,0}" -e "curve VOA" reconstitution/bm-transfer-native-e2-construction-2026-04-30.md reconstitution/swarm-2026-04-30-agent-206-bm-transfer-native-e2-construction.md
git status --short -- reconstitution/bm-transfer-native-e2-construction-2026-04-30.md reconstitution/swarm-2026-04-30-agent-206-bm-transfer-native-e2-construction.md
```

One exploratory `rg` command failed because `\bar\partial` was passed as
a regex escape.  It made no file changes.
