# Swarm report: Agent 312 native holomorphic E2 operator algebra

Date: 2026-04-30
Agent: 312
Task: attack-heal the native operator algebra/chiral-algebra surface for
mixed holomorphic-topological strings on
`\mathbb R^2_{\mathrm{top}}\times\mathbb C^2_{\mathrm{hol}}`.
Files changed: this report and
`reconstitution/native-holomorphic-e2-operator-algebra-attack-heal-2026-04-30.md`.
No manuscript TeX edited.

## Claim Attacked

The vulnerable claim surface is any sentence that lets the native
operator algebra be read as a one-dimensional curve vertex algebra,
Zhu algebra, compact-CY chiral homology object, CoHA, or BKM/Igusa
object.

## Result

The native object actually constructed is the holomorphic
`E_2`/factorization algebra on the complex surface:

```tex
\mathcal F^{\mathrm{hol}}_{\mathrm{Ham}}(B)
 =
C^*_{\mathrm{CE,cont}}\!\left(
\Omega^{0,*}_c(B)\widehat\otimes(\mathfrak h\ltimes P[1])
\right),
\qquad
\mathfrak h=\mathbb C[[z_1,z_2]]/\mathbb C\cdot 1.
```

The mixed object is

```tex
\mathcal F^{\mathrm{mix}}_{\mathrm{Ham}}(U\times B)
 =
C^*_{\mathrm{CE,cont}}\!\left(
\Omega^*_c(U)\widehat\otimes
\Omega^{0,*}_c(B)\widehat\otimes(\mathfrak h\ltimes P[1])
\right).
```

The principal-part coefficient module is

```tex
P
 =
\operatorname{Ann}_{\operatorname{res}}(\mathbb C\cdot 1)
 =
\bigoplus_{a,b\ge0,\ a+b>0}\mathbb C\,\rho_{a,b},
\qquad
\rho_{a,b}=z_1^{-a-1}z_2^{-b-1}\,dz_1\,dz_2.
```

The coadjoint action is

```tex
z_1^p z_2^q\cdot\rho_{a,b}
  =
-(pb-qa+p-q)\rho_{a-p+1,b-q+1}.
```

This two-index coefficient system is essential. The `z_2=0` quotient
kills the symplectic Hamiltonian bracket, and the `b=0` residue line is
not stable because

```tex
z_1\cdot\rho_{a,0}=-\rho_{a,1}.
```

## Failure Modes Found

1. Native curve VOA reading.

Failure: no native choice of line, pushforward, vacuum, translation
operator, state-field map, finite Laurent OPE, or Zhu map exists in the
constructed `\mathbb C^2` factorization algebra.

Heal: call the native object holomorphic `E_2`/factorization on
`\mathbb C^2`. Put curve VOA/Zhu claims behind the controlled reduction
interface.

2. Naive one-variable reduction.

Failure: setting `z_2=0` destroys
`\{f,g\}=\partial_{z_1}f\partial_{z_2}g
-\partial_{z_2}f\partial_{z_1}g`.

Heal: any reduction must retain `z_2` modes or the full two-index
principal-part coefficient system.

3. Principal-part truncation.

Failure: `\oplus_a\mathbb C\rho_{a,0}` is not a module for the
Hamiltonian coadjoint action.

Heal: use the full reduced Matlis module `P`.

4. Reduced current algebra overstated as full factorization center.

Failure: support-local current brackets do not supply stratified
prefactorization, collar module, kernel, centrality homotopies, or QME
data.

Heal: classify the current algebra as a reduced avatar; keep the full
factorization center as an obstruction-vector problem.

5. Moyal coefficients overstated as Costello graph QME.

Failure: Moyal/Weyl formulas do not supply field topology, gauge fixing,
propagator, counterterms, anomaly class, or brane-defect graph kernel.

Heal: state Weyl/Moyal as the degree-zero quantum brane coefficient
theorem. Costello graph/QME remains gated by analytic graph-realization
data.

6. Compact-CY/CoHA/BKM import.

Failure: no matched-conventions theorem transfers local formal
`\mathbb C^2` Hamiltonian BF data to compact CY, CoHA, Igusa, BKM,
quintic, OSV/GV, MNOP, or Abel-Jacobi conclusions.

Heal: quarantine these as external comparison targets only.

## Constructed Open/Brane Algebra

Point-brane Ext:

```tex
\operatorname{Ext}^*_{\mathbb C[z_1,z_2]}(\mathcal O_p,\mathcal O_p)
  \cong
\Lambda_{\mathbb C}(\epsilon_1,\epsilon_2).
```

Finite-N derived commuting-pair algebra:

```tex
R_N=\mathbb C[\phi_1,\phi_2]\otimes\Lambda(\psi),
\qquad
Q\psi=[\phi_1,\phi_2],
\qquad
Q\phi_1=Q\phi_2=0.
```

Weyl/Moyal quantum coefficient algebra:

```tex
f*g
 =
m\exp\!\left(\frac{\hbar}{2}
(\partial_{z_1}\otimes\partial_{z_2}
 -\partial_{z_2}\otimes\partial_{z_1})\right)(f\otimes g),
\qquad
[\phi_1{}^i{}_j,\phi_2{}^k{}_\ell]
 =
\hbar\,\delta^i_\ell\delta^k_j.
```

This is constructed brane-side coefficient data, not the full open BV
factorization center.

## Principal-Part Current Algebra

The reduced current algebra on an interval `I` is

```tex
\mathcal A_{\mathrm{pp},\partial}(I)
 =
S^\wedge(\Omega_c^0(I)\widehat\otimes\overline A)
\widehat\otimes
S^\wedge(\mathcal D'_c(I)\widehat\otimes P[1]),
```

with

```tex
\{B_f(a),B_g(b)\}=B_{\{f,g\}}(ab),
```

```tex
\{B_f(a),\Theta_\rho(B)\}
 =
\Theta_{f\cdot\rho}(aB),
\qquad
\{\Theta_\rho(B),\Theta_\sigma(C)\}=0.
```

Status: proved reduced support-local current algebra. Not unreduced BV.
Not curve OPE.

## BMK Transfer Status

Constructed: BMK current-limit data, finite Matlis moments, arity-two
output projection.

Finite moment map:

```tex
p_N(\alpha)
 =
\sum_{0<a+b\le N}
\left(\int_B z_1^a z_2^b\,\alpha^{0,2}
\wedge dz_1\wedge dz_2\right)\rho_{a,b}.
```

Residue current section:

```tex
\Delta_{a,b}
 =
\frac{(-1)^{a+b}}{a!\,b!}
\partial_{z_1}^a\partial_{z_2}^b\delta_0\,
d\bar z_1\wedge d\bar z_2.
```

Obstructed: strict finite-window quotient and all-window transfer.

Exact finite-window obstruction:

```tex
z_1^{N+2}\cdot\rho_{N+1,0}=-(N+2)\rho_{0,1},
\qquad
\operatorname{Jac}_{\mathrm{proj}}
=(N+1)(N+2)\rho_{0,1}.
```

Obstruction vector:

```tex
\operatorname{Ob}^{\mathrm{BMK-curr}}_N
 =
(\operatorname{ob}_{\mathrm{diag}},
 \operatorname{ob}_{\mathrm{an/fin},N},
 \operatorname{ob}_{\mathfrak h,N},
 \operatorname{ob}_{\mathrm{collar-fact},N}).
```

All-window obstruction:

```tex
\operatorname{Ob}^{\infty}_{\mathrm{BM}}
 =
(\operatorname{ob}_{\mathrm{mom}},
 \operatorname{ob}_{\mathrm{collar}},
 \operatorname{ob}_3,
 \operatorname{ob}_{\mathrm{unif}}).
```

## Curve Algebra Gate

A pushed-forward curve algebra is allowed only after constructing

```tex
\mathfrak R_{\mathbb C\times\mathbb R}
 =
(\pi,\kappa_{\mathrm{top}},\kappa_{\mathrm{hol}},
 \mathcal B_{z_2},\pi_!,L_{\mathrm{red}},
 \langle-,-\rangle_{\mathrm{red}},
 \{-,-\}_{\mathrm{red}},H_{\mathrm{anom}})
```

and

```tex
\mathfrak I_{\mathrm{ch}}
 =
(\mathfrak R_{\mathbb C\times\mathbb R},
 \mathcal F_{\mathrm{red}},V_{\mathrm{red}},Q_{\mathrm{BRST}},
 \mathbf 1,T,Y,\operatorname{wt},\zeta_\hbar,H_{\mathrm{anom}}).
```

The obstruction vector is

```tex
\operatorname{Ob}_{\mathfrak I_{\mathrm{ch}}}
 =
(\operatorname{Ob}_{\mathrm{red}},
 \operatorname{Ob}_{\mathrm{vert}},
 \operatorname{Ob}_{\mathrm{Zhu}},
 \operatorname{Ob}_{\mathrm{nat}}).
```

After this gate, the reduced Dirac BRST vertex algebra may have fields

```tex
Z_1{}^i{}_j(z)Z_2{}^k{}_\ell(w)
 \sim
\frac{\hbar\,\delta^i_\ell\delta^k_j}{z-w},
\qquad
b^i{}_j(z)c^k{}_\ell(w)
 \sim
\frac{\delta^i_\ell\delta^k_j}{z-w},
```

with

```tex
j_{\mathrm{BRST}}
 =
\operatorname{Tr}(c[Z_1,Z_2])
\frac12\operatorname{Tr}(b[c,c]).
```

Before this gate, these formulas are not native claims.

## Exact TeX Patch Targets

No patch was applied. Recommended targets:

1. `theorem-lanes.tex:473-487`: replace the scalar BM expression by
   the full BMK kernel

```tex
\eta=\zeta-z,\qquad d\bar\eta_j=d\bar\zeta_j-d\bar z_j,
```

```tex
K_{\mathrm{BM}}(z,\zeta)
 =
\frac{1}{(2\pi i)^2}
\frac{\bar\eta_1d\bar\eta_2-\bar\eta_2d\bar\eta_1}
{(|\eta_1|^2+|\eta_2|^2)^2}
\wedge d\zeta_1\wedge d\zeta_2.
```

2. `main.tex:655-671`: add a sentence that the closed-side product
   there is a topological-current avatar, while the native holomorphic
   operator algebra is
   `\mathcal F^{\mathrm{hol}}_{\mathrm{Ham}}`; no one-dimensional OPE
   or Zhu algebra is asserted.

3. `local-dictionary.tex:290-323`: expand the one-dimensional
   restriction tuple to

```tex
\mathfrak R_L
 =
(\iota_L,\mathcal B_\perp,\mathsf R_{L,\mathcal B_\perp},
 V_L,\mathbf 1_L,T_L,Y_L,\zeta_{L,\hbar}).
```

4. `main.tex:1713-1719`: add a local cross-reference to
   `\operatorname{Ob}_{\mathfrak I_{\mathrm{ch}}}`.

5. `claim-strength-ledger.tex:319-331`: write
   `z_1^{N+2}\cdot\rho_{N+1,0}` rather than juxtaposition in the older
   BM finite-window row.

## Claim-Status Recommendations

Proved:

- Native holomorphic `E_2`/factorization algebra on `\mathbb C^2`.
- Mixed topological-current enhancement.
- Point-brane Ext and finite-N Dirac/Koszul reduced open algebra.
- Matlis principal parts and reduced support-local current brackets.

Computed/proved with obstruction:

- BMK current-limit data, finite moments, and arity-two transfer.
- Strict finite-window and all-window transfers are blocked by named
  obstruction vectors.

Theorem surface with missing construction:

- Controlled `\mathbb C\times\mathbb R` reduction retaining `z_2`.
- Reduced Dirac BRST curve vertex algebra and Zhu bridge after the
  reduction.

False transfer unless separately proved:

- Native curve VOA/Zhu assertion.
- Compact CY/global BCOV conclusion.
- CoHA, BKM/Igusa, quintic, OSV/GV, MNOP, Abel-Jacobi consequence.

## Firewall Rules

1. Native equals holomorphic `E_2`/factorization on `\mathbb C^2`.
2. Curve VOA requires the full reduction and vertex/Zhu interface.
3. Retain `z_2` or full two-index principal parts.
4. Do not identify `\Psi_{a,b}` with `\rho_{a,b}`.
5. Do not treat reduced current brackets as full factorization center.
6. Do not treat Moyal/Weyl coefficients as Costello graph QME.
7. External compact-CY/CoHA/BKM claims need matched conventions,
   obstruction vector, and null-homotopies.

## Local Anchors

- `main.tex:1111-1240`
- `main.tex:1242-1503`
- `main.tex:1635-1719`
- `main.tex:2860-3008`
- `theorem-lanes.tex:227-1087`
- `open-obligations.tex:221-251`
- `claim-strength-ledger.tex:633-725`
- `appendix-matlis-principal-parts.tex:81-217`
- `appendix-factorization-current-conventions.tex:399-430`
- `~/chiral-bar-cobar-vol2/notes/antipatterns_catalogue.md`
- `~/chiral-bar-cobar-vol2/notes/first_principles_cache_comprehensive.md`

## Tests and Commands

Read and grep audit only. No TeX build was run because manuscript files
were not edited.

Recommended verification after any later TeX patch:

```bash
rg -n "F\\^\\{\\\\mathrm\\{hol\\}\\}_\\{\\\\mathrm\\{Ham\\}\\}|Ob_\\{\\\\mathfrak I_\\{\\\\mathrm\\{ch\\}\\}\\}|K_\\{\\\\mathrm\\{BM\\}\\}|z_1\\^\\{N\\+2\\}" main.tex theorem-lanes.tex local-dictionary.tex claim-strength-ledger.tex
make pdf
```

## Remaining Open Questions

1. Construct the full `\mathfrak R_{\mathbb C\times\mathbb R}` reduction
   or prove its exact obstruction class.
2. Construct the vertex package `V_{\mathrm{red}},\mathbf 1,T,Y,wt` and
   the Zhu morphism `\zeta_\hbar`, or prove the named obstruction.
3. Lift reduced current brackets to a stratified BV factorization-center
   theorem with collar kernels and centrality homotopies.
4. Supply analytic Costello graph/QME realization data if quantum graph
   claims are to exceed coefficient-level Moyal/Weyl formulas.

