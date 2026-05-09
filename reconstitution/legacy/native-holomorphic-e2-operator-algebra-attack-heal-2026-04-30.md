# Native holomorphic E2 operator algebra attack-heal

Date: 2026-04-30
Agent: 312
Scope: mixed holomorphic-topological strings on
`\mathbb R^2_{\mathrm{top}}\times\mathbb C^2_{\mathrm{hol}}`.
No manuscript TeX edited.

## Verdict

The native algebra constructed in the manuscript is a
two-complex-dimensional holomorphic factorization algebra, equivalently
the local holomorphic `E_2` collision algebra on `\mathbb C^2`, with
topological current enhancement along `\mathbb R^2`. It is not a curve
vertex algebra, not a Zhu algebra, not a compact-Calabi-Yau chiral
homology object, not a CoHA, and not a BKM/Igusa object.

The strongest true local statement is:

```tex
\mathcal F^{\mathrm{hol}}_{\mathrm{Ham}}(B)
  =
C^*_{\mathrm{CE,cont}}\!\left(
  \Omega^{0,*}_c(B)\,\widehat\otimes\,
  \mathfrak g
\right),
\qquad
\mathfrak g=\mathfrak h\ltimes P[1],
\qquad
\mathfrak h=\mathbb C[[z_1,z_2]]/\mathbb C\cdot 1,
```

where

```tex
P=\operatorname{Ann}_{\operatorname{res}}(\mathbb C\cdot 1)
  =
\bigoplus_{a,b\ge 0,\ a+b>0}\mathbb C\,\rho_{a,b}
\cong \mathfrak h^\vee_{\mathrm{cont}}.
```

For `U\subset \mathbb R^2_{\mathrm{top}}` the mixed enhancement is

```tex
\mathcal F^{\mathrm{mix}}_{\mathrm{Ham}}(U\times B)
  =
C^*_{\mathrm{CE,cont}}\!\left(
  \Omega^*_c(U)\widehat\otimes
  \Omega^{0,*}_c(B)\widehat\otimes
  (\mathfrak h\ltimes P[1])
\right).
```

This is locally constant in the topological variables and holomorphic in
the two complex variables. The word "chiral", when retained, must mean
this holomorphic factorization structure on the complex surface.

## Algebra Actually Constructed

### 1. Native closed algebra

The closed Hamiltonian algebra is the continuous semidirect Lie algebra

```tex
\mathfrak g=\mathfrak h\ltimes P[1],
\qquad
\mathfrak h=\mathbb C[[z_1,z_2]]/\mathbb C\cdot 1.
```

The binary brackets are

```tex
[\alpha\otimes f,\beta\otimes g]
  =
(\alpha\wedge\beta)\otimes\{f,g\},
```

```tex
[\alpha\otimes f,\beta\otimes\rho[1]]
  =
(\alpha\wedge\beta)\otimes(f\cdot\rho)[1],
\qquad
[\alpha\otimes\rho[1],\beta\otimes\sigma[1]]=0.
```

Here

```tex
\{f,g\}
  =
\partial_{z_1}f\,\partial_{z_2}g
 -
\partial_{z_2}f\,\partial_{z_1}g.
```

The Matlis coadjoint action is characterized by

```tex
\operatorname{Res}_0((f\cdot\rho)g)
  =
-\operatorname{Res}_0(\rho\,\{f,g\}),
```

and on monomials by

```tex
z_1^p z_2^q\cdot\rho_{a,b}
  =
-(pb-qa+p-q)\,\rho_{a-p+1,b-q+1},
```

with negative indices interpreted as zero. This is the native
two-variable coefficient system. It is not a one-variable mode algebra.

### 2. Brane Ext and open algebra

For the point brane in the local surface the constructed Ext algebra is

```tex
\operatorname{Ext}^*_{\mathbb C[z_1,z_2]}(\mathcal O_p,\mathcal O_p)
  \cong
\Lambda_{\mathbb C}(\epsilon_1,\epsilon_2).
```

For finite `N` the brane-side derived commuting-pair model is the
Dirac/Koszul algebra

```tex
R_N=\mathbb C[\phi_1,\phi_2]\otimes\Lambda(\psi),
\qquad
Q\psi=[\phi_1,\phi_2],
\qquad
Q\phi_1=Q\phi_2=0.
```

Its degree-zero invariant cohomology describes the reduced open algebra
of the commuting-pair derived zero fibre. The quantum degree-zero target
is the Weyl/Moyal algebra and quantum Hamiltonian reduction:

```tex
f*g
 =
m\exp\!\left(\frac{\hbar}{2}
(\partial_{z_1}\otimes\partial_{z_2}
 -\partial_{z_2}\otimes\partial_{z_1})\right)(f\otimes g),
```

```tex
[\phi_1{}^i{}_j,\phi_2{}^k{}_\ell]
  =
\hbar\,\delta^i_\ell\delta^k_j.
```

The reduced Zhu-shadow relation after the controlled curve reduction is

```tex
YX-XY+\hbar N I=0.
```

This is not, by itself, a full open BV factorization-center theorem.
The full brane theorem still needs a stratified prefactorization/module
datum, collar kernels, centrality homotopies, and QME compatibility.

### 3. Principal-part coefficient algebra

The correct coefficient system is the reduced Matlis principal-part
space

```tex
P
 =
\operatorname{Ann}_{\operatorname{res}}(\mathbb C\cdot 1)
 =
\bigoplus_{a,b\ge0,\ a+b>0}\mathbb C\,\rho_{a,b},
\qquad
\rho_{a,b}=z_1^{-a-1}z_2^{-b-1}\,dz_1\,dz_2,
```

with pairing

```tex
\langle\rho_{a,b},z_1^m z_2^n\rangle
  =
\delta_{a,m}\delta_{b,n}.
```

The reduced support-local current algebra on an interval `I` is

```tex
\mathcal A_{\mathrm{pp},\partial}(I)
 =
S^\wedge(\Omega_c^0(I)\widehat\otimes\overline A)
\widehat\otimes
S^\wedge(\mathcal D'_c(I)\widehat\otimes P[1]),
```

with brackets

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

This reduced current algebra is a controlled support-local avatar. It is
not an unreduced BV factorization algebra and not the full
factorization center.

### 4. BMK transfer status

The manuscript constructs BMK current-limit data, finite Matlis moment
maps, and an arity-two output projection. The full finite-window or
all-window strict transfer is obstructed.

The finite moment map is

```tex
p_N(\alpha)
 =
\sum_{0<a+b\le N}
\left(
\int_B z_1^a z_2^b\,\alpha^{0,2}\wedge dz_1\wedge dz_2
\right)\rho_{a,b}.
```

The residue current section is

```tex
\Delta_{a,b}
 =
\frac{(-1)^{a+b}}{a!\,b!}
\partial_{z_1}^a\partial_{z_2}^b\delta_0\,
d\bar z_1\wedge d\bar z_2.
```

The arity-two projected bracket is

```tex
\ell_2^{\mathrm{BM},N}(f,g)
 =
\operatorname{pr}_{\le N}
(\partial_{z_1}f\,\partial_{z_2}g
 -\partial_{z_2}f\,\partial_{z_1}g)\bmod\mathbb C,
```

```tex
\ell_2^{\mathrm{BM},N}(f,\rho_{i,j})
 =
-(pj-qi+p-q)\,
\operatorname{pr}_{\le N}\rho_{i-p+1,j-q+1},
\qquad
\ell_2^{\mathrm{BM},N}(\rho,\sigma)=0.
```

The exact finite-window obstruction includes

```tex
z_1^{N+2}\cdot\rho_{N+1,0}=-(N+2)\rho_{0,1},
```

and the projected Jacobiator contains

```tex
(N+1)(N+2)\rho_{0,1}.
```

The obstruction vector is

```tex
\operatorname{Ob}^{\mathrm{BMK-curr}}_N
 =
(\operatorname{ob}_{\mathrm{diag}},
 \operatorname{ob}_{\mathrm{an/fin},N},
 \operatorname{ob}_{\mathfrak h,N},
 \operatorname{ob}_{\mathrm{collar-fact},N}).
```

The all-window target is governed by

```tex
\operatorname{Ob}^{\infty}_{\mathrm{BM}}
 =
(\operatorname{ob}_{\mathrm{mom}},
 \operatorname{ob}_{\mathrm{collar}},
 \operatorname{ob}_3,
 \operatorname{ob}_{\mathrm{unif}}).
```

Therefore the BMK material strengthens the native `E_2` surface, but it
does not construct a curve vertex algebra or a strict all-arity transfer.

### 5. Pushed-forward curve algebra

A curve algebra may enter only after a controlled
`\mathbb C\times\mathbb R` reduction. The required datum is

```tex
\mathfrak R_{\mathbb C\times\mathbb R}
 =
(\pi,\kappa_{\mathrm{top}},\kappa_{\mathrm{hol}},
 \mathcal B_{z_2},\pi_!,L_{\mathrm{red}},
 \langle-,-\rangle_{\mathrm{red}},
 \{-,-\}_{\mathrm{red}},H_{\mathrm{anom}}).
```

The reduction must retain the `z_2` coefficient system:

```tex
\mathfrak h_{\mathrm{red}}
 =
\mathbb C[[z_1]][[z_2]]/\mathbb C,
\qquad
P_{\mathrm{red}}
 =
\operatorname{Ann}_{\operatorname{res}}(\mathbb C)
\subset
H^2_{(z_1,z_2)}(\mathbb C[[z_1,z_2]])\,dz_1\,dz_2.
```

The curve vertex/Zhu interface requires

```tex
\mathfrak I_{\mathrm{ch}}
 =
(\mathfrak R_{\mathbb C\times\mathbb R},
 \mathcal F_{\mathrm{red}},V_{\mathrm{red}},Q_{\mathrm{BRST}},
 \mathbf 1,T,Y,\operatorname{wt},\zeta_\hbar,H_{\mathrm{anom}}),
```

with obstruction vector

```tex
\operatorname{Ob}_{\mathfrak I_{\mathrm{ch}}}
 =
(\operatorname{Ob}_{\mathrm{red}},
 \operatorname{Ob}_{\mathrm{vert}},
 \operatorname{Ob}_{\mathrm{Zhu}},
 \operatorname{Ob}_{\mathrm{nat}}).
```

Only after these data are constructed can the reduced Dirac BRST vertex
algebra be used:

```tex
Z_1{}^i{}_j(z)\,Z_2{}^k{}_\ell(w)
  \sim
\frac{\hbar\,\delta^i_\ell\delta^k_j}{z-w},
\qquad
b^i{}_j(z)c^k{}_\ell(w)
  \sim
\frac{\delta^i_\ell\delta^k_j}{z-w},
```

```tex
j_{\mathrm{BRST}}
 =
\operatorname{Tr}(c[Z_1,Z_2])
\frac12\operatorname{Tr}(b[c,c]),
\qquad
Q_{\mathrm{BRST}}=\operatorname{Res}j_{\mathrm{BRST}}\,dz.
```

Before this reduction, any curve VOA, Zhu algebra, or
`\mathbb C\times\mathbb R` chiral algebra language is false transfer.

## Attack-Heal Table

| Attack | Failure mode | Heal |
|---|---|---|
| Native object is a curve vertex algebra. | The constructed object is over opens in `\mathbb C^2`; no line, translation operator, vacuum, state-field map, finite Laurent OPE, or Zhu map is native. | State native object as holomorphic `E_2`/factorization algebra on `\mathbb C^2`. Put curve VOA behind `\mathfrak R_{\mathbb C\times\mathbb R}` and `\mathfrak I_{\mathrm{ch}}`. |
| Set `z_2=0` to get a curve algebra. | The Hamiltonian bracket on `\mathbb C^2` is destroyed. | Retain `z_2` modes or the full two-index principal-part system. |
| Keep only `b=0` principal parts. | Not stable: `z_1\cdot\rho_{a,0}=-\rho_{a,1}`. | Use full `P=\oplus_{a+b>0}\mathbb C\rho_{a,b}`. |
| Identify PBW polynomial labels `\Psi_{a,b}` with Matlis coefficients `\rho_{a,b}`. | PBW special-fibre action and Matlis coadjoint action differ. | Keep polynomial descendants, PBW labels, and principal parts in separate habitats. |
| Treat reduced current brackets as the full factorization center. | Missing stratified prefactorization, collar kernels, centrality homotopies, and QME compatibility. | Classify reduced current algebra as support-local avatar; leave full center as obstruction-vector problem. |
| Treat Weyl/Moyal checks as Costello graph QME. | Formal coefficients do not supply field topology, propagator, gauge fixing, counterterms, anomaly class, or brane-defect kernel. | State Moyal/Weyl theorem as coefficient-level quantum brane algebra; put Costello QME behind analytic graph-realization data. |
| Import compact CY, CoHA, or BKM language. | No matched-conventions theorem from local formal `\mathbb C^2` Hamiltonian BF data to those global objects. | Quarantine as external comparison only, with datum, obstruction vector, and null-homotopies. |
| Use Vol II curve grammar as native theorem. | Vol II supplies useful anti-patterns and possible target grammar, not a proof of a `\mathbb C^2` reduction. | Use it only after constructing the local reduction and anomaly comparison. |

## Exact TeX Patch Targets

These are patch targets only. No TeX patch was applied.

1. `theorem-lanes.tex:473-487`

Replace the scalar BM expression using only `d\bar\zeta_j` by the full
BMK kernel used in `main.tex` and
`appendix-factorization-current-conventions.tex`:

```tex
\eta=\zeta-z,\qquad
d\bar\eta_j=d\bar\zeta_j-d\bar z_j,\qquad
r^2=|\eta_1|^2+|\eta_2|^2,
```

```tex
K_{\mathrm{BM}}(z,\zeta)
 =
\frac{1}{(2\pi i)^2}
\frac{\bar\eta_1\,d\bar\eta_2-\bar\eta_2\,d\bar\eta_1}{r^4}
\wedge d\zeta_1\wedge d\zeta_2.
```

Reason: the scalar component is useful for moment extraction, but the
native current-limit theorem requires the full diagonal kernel.

2. `main.tex:655-671`

After the displayed list of the two algebras, add a firewall sentence:

```tex
The product on the closed side in this paragraph is the
topological-current avatar used for the local trace comparison; the
native holomorphic operator algebra is the
\mathbb C^2-holomorphic factorization algebra
\mathcal F^{\mathrm{hol}}_{\mathrm{Ham}} of
Definition~\ref{def:local-hamiltonian-chiral-factorization-algebra}.
No one-dimensional vertex OPE or Zhu algebra is asserted here.
```

Reason: the phrase "operator-product expansion in the `R`-direction"
can be misread as a curve VOA assertion.

3. `local-dictionary.tex:290-323`

Replace the current one-dimensional restriction tuple by the complete
gate:

```tex
\mathfrak R_L
 =
(\iota_L,\mathcal B_\perp,\mathsf R_{L,\mathcal B_\perp},
 V_L,\mathbf 1_L,T_L,Y_L,\zeta_{L,\hbar}).
```

Reason: the dictionary later refers to OPE and Zhu data, but the tuple
does not list `V_L`, `Y_L`, or `\zeta_{L,\hbar}`. Match
`theorem-lanes.tex:638-675`.

4. `main.tex:1713-1719`

Add a local cross-reference to the curve-interface obstruction vector:

```tex
\operatorname{Ob}_{\mathfrak I_{\mathrm{ch}}}
 =
(\operatorname{Ob}_{\mathrm{red}},
 \operatorname{Ob}_{\mathrm{vert}},
 \operatorname{Ob}_{\mathrm{Zhu}},
 \operatorname{Ob}_{\mathrm{nat}}).
```

Reason: the Darboux package should state locally that the reduced
chiral interface is gated by reduction, vertex, Zhu, and native-return
obstructions.

5. `claim-strength-ledger.tex:319-331`

If the older finite-window row is retained beside the newer Supremum
controller rows, write

```tex
z_1^{N+2}\cdot\rho_{N+1,0}=-(N+2)\rho_{0,1}
```

rather than juxtaposition. Reason: juxtaposition can be read as ordinary
multiplication in `P`, while the formula is the coadjoint action.

## Claim-Status Recommendations

1. Proved: native closed holomorphic `E_2`/factorization algebra
   `\mathcal F^{\mathrm{hol}}_{\mathrm{Ham}}` and mixed topological
   enhancement.

2. Proved: point-brane Ext algebra and finite-N Dirac/Koszul
   commuting-pair model as reduced open algebra.

3. Proved: Matlis principal-part coefficient system and reduced
   support-local current brackets.

4. Proved to arity two / obstructed beyond current data: BMK
   finite-window transfer and all-window strict transfer. Record exact
   obstruction vector, not a demotion to expectation.

5. Theorem surface with missing construction: controlled
   `\mathbb C\times\mathbb R` reduction with retained `z_2` modes or
   two-index principal parts.

6. Theorem surface only after reduction: reduced Dirac BRST curve vertex
   algebra and Zhu bridge.

7. False transfer unless separately proved: compact CY, global BCOV,
   CoHA, BKM/Igusa, quintic, OSV/GV, MNOP, Abel-Jacobi, Vol III compact
   consequences.

## Firewall Rules

1. Say "holomorphic `E_2`/factorization algebra on `\mathbb C^2`" for
   the native operator algebra. Do not say "vertex algebra" without a
   completed reduction datum.

2. A curve OPE requires a line or defect, pushforward, retained
   transverse coefficient system, vacuum, translation operator,
   state-field map, finite singular OPEs, anomaly homotopy, and Zhu map.

3. Do not set `z_2=0`. Do not replace `P` by the `b=0` line. Both break
   the native Hamiltonian/coadjoint structure.

4. Keep `\rho_{a,b}` principal parts separate from PBW polynomial labels
   `\Psi_{a,b}`.

5. Keep reduced current brackets separate from the unreduced BV
   factorization center.

6. Keep `\hbar_{\mathrm{QME}}`, `\hbar_W`, and `\hbar_\omega` separate.

7. Compact-CY, CoHA, BKM, Igusa, quintic, OSV/GV, MNOP, and
   Abel-Jacobi claims are external comparison targets. They require a
   matched-conventions datum, a vanishing obstruction vector, and
   null-homotopies.

8. Vol II curve algebra material is grammar and anti-pattern evidence
   until the local reduction theorem is constructed in this manuscript.

## Local Anchors

- `main.tex:1111-1240`: native Hamiltonian holomorphic factorization
  definition and proposition.
- `main.tex:1242-1503`: BMK finite-window and all-window obstruction
  package.
- `main.tex:1635-1719`: native Darboux theorem package and reduced
  chiral-interface warning.
- `main.tex:2860-3008`: local mixed model and point-brane Ext algebra.
- `theorem-lanes.tex:227-379`: local chiral/factorization taxonomy.
- `theorem-lanes.tex:381-533`: native `E_2` collision lane and BM
  obligation.
- `theorem-lanes.tex:535-699`: vertex/OPE boundary.
- `theorem-lanes.tex:701-887`: controlled `\mathbb C\times\mathbb R`
  reduction.
- `theorem-lanes.tex:889-1087`: reduced Dirac BRST/Zhu interface.
- `open-obligations.tex:221-251`: chiral interface obstruction gate.
- `claim-strength-ledger.tex:633-725`: Supremum controller
  classification for native `E_2`, reduction, and BRST/Zhu surfaces.
- `appendix-matlis-principal-parts.tex:81-217`: principal parts and
  coadjoint action.
- `appendix-factorization-current-conventions.tex:399-430`: full BMK
  kernel convention.

