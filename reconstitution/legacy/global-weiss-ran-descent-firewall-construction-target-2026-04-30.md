# Global Weiss/Ran Descent Firewall Construction Target

Date: 2026-04-30.

Scope: report-only construction target for the formal-local mixed
holomorphic-topological theory on
\[
  X=\mathbb R_t\times\mathbb R_s\times\widehat{\mathbb C^2}_{0},
  \qquad
  L=\mathbb R_t\times\{s=z_1=z_2=0\}.
\]
No manuscript or Vol II file is edited by this report.

## Verdict

The native stable core is local.  It contains the formal Hamiltonian
holomorphic factorization object on \(\mathbb C^2\), the mixed
topological-current enhancement on product opens, the coordinate CE/PV
stalk comparison under its admissibility hypotheses, the reduced
brane-line principal-part current \(P_0\) prefactorization datum, and
the degree-zero Weyl/Moyal trace surface where already proved.

The global theorem is not obtained by gluing formal Darboux stalks.  The
strongest true target is a Weiss/Ran descent theorem with an exact
obstruction vector.  If the vector vanishes with compatible
null-homotopies, the local Hamiltonian map descends to a global
factorization-center morphism.  If a component is nonzero, that component
is the obstruction theorem.  If a required component is absent, the
target datum is incomplete.

Compact Calabi-Yau, compact BCOV, CoHA, MNOP, quintic, OSV/GV,
Abel-Jacobi, Vol III, Igusa/BKM, Borcherds, curve VOA, Zhu, and
sister-volume claims remain firewalled unless a matched-conventions
target datum supplies comparison maps and kills the obstruction vector.

## Evidence Anchors

- `CLAUDE.md`: local geometry, local Calabi-Yau datum, native
  \(\mathbb C^2\) factorization, controlled curve reduction, and external
  comparison quarantine.
- `AGENTS.md`: no compact-CY or Vol II direct import; curve VOA/Zhu
  claims require a controlled reduction; deep supremum discipline.
- `local-dictionary.tex:13-166`: the local Calabi-Yau datum is only
  \((\widehat{\mathbb C^2}_0,dz_1\wedge dz_2)\); compact Hodge theory,
  compact CY3, CoHA, BKM, VOA, and Vol III imports are inadmissible.
- `local-dictionary.tex:189-288`: the native objects are
  \(\mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}\), the mixed current
  enhancement, Weyl/Moyal brane algebra, and the principal-part current
  algebra; none is a compact-CY chiral homology object or a curve VOA.
- `theorem-lanes.tex:227-379`: local chiral/factorization taxonomy and
  firewall.
- `claim-strength-ledger.tex:481-546`: native \(\mathbb C^2\) \(E_2\)
  factorization is proved on its named habitat; all-window BM transfer
  and curve/Zhu reductions remain construction targets.
- `main.tex:4118-4172`: the unreduced factorization-center lift requires
  Tate coefficients, cotangent boundary realization, centrality
  homotopies, factorization compatibility, and descent; a stalkwise disk
  map is not Weiss/Ran descent.
- `main.tex:4231-4247`: the Weiss/Ran total complex is the global
  obstruction habitat.
- `tate-P5-cross-volume.tex:153-188`: definition of the global
  Hamiltonian descent complex and the classes
  \(\operatorname{ob}^{(1)}_{\mathrm{WR}}\) and
  \(\operatorname{ob}^{(r)}_{\mathrm{WR}}\).
- `tate-P5-cross-volume.tex:190-302`: formal local-to-global Hamiltonian
  descent theorem data and sharp compact-surface period obstruction.
- `tate-P5-cross-volume.tex:304-415`: matched-conventions transfer
  criterion and the acceptance class
  \(\operatorname{Ob}_{\mathrm{UKD}}\).
- `tate-P5-cross-volume.tex:428-435`: product-disk site is not asserted
  cofinal in arbitrary Weiss/Ran covers.
- `tate-P5-cross-volume.tex:445-490`: mixed six-relation obstruction
  surface for real Weiss, holomorphic Ran, and interchange data.
- `open-obligations.tex:757-888`: stratified brane prefactorization
  requires collar maps, products, descent, centrality homotopies, and QME
  curvature; the exact obstruction vector contains
  \(\delta_{\mathrm{Weiss}}\).
- `open-obligations.tex:1083-1122`: external targets require
  \(\mathfrak C_{\mathrm{tar}}\), vanishing obstruction vector,
  null-homotopies, and comparison morphisms.
- Vol II control surface:
  `/Users/raeez/chiral-bar-cobar-vol2/notes/antipatterns_catalogue.md:9986-9992`
  and `:10110-10117` record the same no-transfer rule.

## Native Claims

These claims are native and do not require external global comparison.

1. Formal-local unimodularity:
\[
  \Omega_{\mathrm{loc}}=dz_1\wedge dz_2,\qquad
  \mathfrak h=\mathbb C[[z_1,z_2]]/\mathbb C\cdot1,
\]
with Hamiltonian bracket
\[
  \{f,g\}
  =
  \partial_{z_1}f\,\partial_{z_2}g
  -
  \partial_{z_2}f\,\partial_{z_1}g .
\]

2. Native holomorphic factorization on a polydisk \(B\subset\mathbb C^2\):
\[
  \mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}(B)
  =
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  \left(
    \Omega_c^{0,\bullet}(B)\widehat\otimes
    (\mathfrak h\ltimes\mathcal P[1])
  \right),
\]
where
\[
  \mathcal P
  =
  \operatorname{Ann}_{\mathrm{res}}(\mathbb C\cdot1)
  \subset
  H^2_{(z_1,z_2)}(\mathbb C[[z_1,z_2]])\,dz_1dz_2 .
\]
Extension by zero on disjoint polydisks gives the local
factorization products.

3. Mixed product-open enhancement:
\[
  \mathfrak g^{\mathrm{mix}}_{U,B}
  =
  \Omega_c^\bullet(U)\widehat\otimes
  \Omega_c^{0,\bullet}(B)\widehat\otimes
  (\mathfrak h\ltimes\mathcal P[1]).
\]
It is locally constant in the real topological directions and
holomorphic in the \(B\)-direction on the product-open habitat.

4. Coordinate CE/PV formal stalk and reduced \(P_0\) central-operation
shadow under the named admissibility hypotheses:
\[
  c^I\mapsto\theta^I,\qquad u_I\mapsto O_I.
\]
This is not a universal factorization-center theorem.

5. Brane-line support-local principal-part current datum on intervals:
\[
  \mathfrak h_I=\Omega_c^\bullet(I)\widehat\otimes\mathfrak h,\qquad
  \mathcal P_I=\mathcal D'_c(I)\widehat\otimes\mathcal P,
\]
\[
  \{B_f(a),B_g(b)\}=B_{\{f,g\}}(ab),\qquad
  \{B_f(a),\Theta_\rho(B)\}=\Theta_{f\cdot\rho}(aB),\qquad
  \{\Theta_\rho(B),\Theta_\sigma(C)\}=0.
\]
This is support-local \(P_0\) current algebra, not a Costello graph/QME
theorem and not a curve OPE theorem.

6. The compact-surface Hamiltonian period obstruction is a native
obstruction calculation once a compact holomorphic symplectic surface is
chosen:
\[
  \operatorname{per}_X(v)
  =
  \delta(-\iota_v\omega)\in H^1(X,\mathbb C_X).
\]
On compact connected \(X\),
\[
  \operatorname{per}_X(v)=0
  \Longleftrightarrow
  -\iota_v\omega=dh\text{ for }h\in H^0(X,\mathcal O_X)
  \Longleftrightarrow
  v=0.
\]
Thus every nonzero global holomorphic symplectic vector field used as a
locally Hamiltonian descent field is rejected by the period component.

## Claims Requiring Weiss/Ran Data

These are construction targets, not native consequences.

1. A global factorization-center morphism
\[
  \mathrm{Obs}^{\mathrm{cl}}_{\mathrm{closed},H}\big|_L
  \longrightarrow
  \mathrm Z^{P_0}_{\mathrm{fact}}
  (\mathrm{Obs}^{\mathrm{cl}}_{\mathrm{open}})
\]
with Darboux restrictions equal to the local maps.

2. The full descent complex
\[
\mathfrak G_{\mathrm{WR}}(L)
=
\operatorname{Tot} C^\bullet_{\mathrm{WR}}\left(
  \operatorname{Ran}(L);
  \underline{\operatorname{RHom}}\left(
    \mathrm{Obs}^{\mathrm{cl}}_{\mathrm{closed},H},
    \mathrm Z^{P_0}_{\mathrm{fact}}
    (\mathrm{Obs}^{\mathrm{cl}}_{\mathrm{open}})
  \right)\right).
\]
For local Darboux maps \(\Phi_{\mathrm{loc}}=\{\Phi_U\}\), the first
obstruction is
\[
  \operatorname{ob}^{(1)}_{\mathrm{WR}}(\Phi_{\mathrm{loc}})
  =
  [d_{\mathrm{WR}}\Phi_{\mathrm{loc}}]\in
  H^1(\mathfrak G_{\mathrm{WR}}(L)),
\]
and the filtered higher collision/cotangent coherences are
\[
  \operatorname{ob}^{(r)}_{\mathrm{WR}}(\Phi_{\mathrm{loc}})
  \in
  H^{r+1}(\operatorname{gr}^r\mathfrak G_{\mathrm{WR}}(L)),
  \qquad r\ge 1.
\]

3. Hyperdescent and pro-convergence:
the target must give a complete pronilpotent descent complex,
hyperdescent for the relevant Weiss/Ran cosheaf, and exact inverse-limit
conditions excluding hidden \(\varprojlim^1\) defects.

4. Stratified brane factorization on \((X,L)\):
\[
  \mathcal F^{\mathrm{str}}_{\Omega,N}\colon
  \operatorname{Disk}^{\mathrm{str}}_{X,L}
  \to
  \operatorname{Ch}_{R_\Omega^{N,M}[[\hbar_{\mathrm{QME}}]]}
\]
with bulk values, brane values, collar module, products, centrality
homotopies, brane-defect QME curvature, and stratified Weiss descent.
The first obstruction vector is
\[
  \operatorname{Ob}_{\mathrm{str},\Omega,N}
  =
  (\delta_{\mathrm{pref}}\mu_{\mathrm{str}},
   \delta_{\mathrm{assoc}}\mu_{\mathrm{str}},
   \delta_{\mathrm{Weiss}},
   \operatorname{ob}^{\mathrm{prod}}_{\mathrm{cent}},
   \operatorname{ob}^{P_0}_{\mathrm{cent}},
   \operatorname{ob}^{\mathrm{bd}}_{\mathrm{QME}},
   \operatorname{ob}^{\mathrm{src}}_{\mathrm{CFG}}).
\]

5. Product-disk mixed factorization beyond its stated site.  The
product-disk site \(\operatorname{Ran}_{\prod}(M,Y)\) is not asserted
cofinal in arbitrary Weiss covers of \(M\times Y\).  A target using
ordinary \(\operatorname{Ran}(M\times Y)\) must supply
\(\operatorname{ob}_{\mathrm{WR}}\), \(\operatorname{ob}_{\mathrm{hyp}}\),
and compatible null-homotopies.

## Firewalled Claims

These claims cannot be inferred from the local theorem.

1. Compact CY3 BCOV amplitudes, compact Hodge theory, holomorphic
anomaly equations, compact Costello-Li anomaly cancellation, and global
BCOV QME.

2. CoHA, compact critical CoHA, Hall algebra, finite Rees Hall, completed
Rees Hall, Drinfeld double, Yangian, or \(W_{1+\infty}\) identifications.
Vol II AP2157-AP2165 require layer-aware source data; a finite
DWR/Ran/Rees construction is not compact critical CoHA.

3. Igusa, Borcherds, BKM, \(\Delta_5\), \(\Phi_{10}\), \(\Phi_{12}\),
Weyl chamber, denominator identity, CHL, or \(K3\times E\) claims.
Vol II AP2166-AP2167 require denominator and ladder scope labels.

4. Curve VOA, BRST curve algebra, Zhu algebra, or Volume II
\(\mathbb C\times\mathbb R\) theorem.  These require a controlled
reduction datum retaining the \(z_2\)-mode or principal-part coefficient
system and proving the pushed-forward bracket, BV pairing, brane image,
and anomaly data.

5. Physical large-\(N\) trace states and protected brane correlators.
Stable algebraic trace generators are not continuous states on
stratified factorization homology without topology, state functional,
Ward identities, counterterms, and cumulant estimates.

## Strongest Positive Target

Construct a target datum
\[
\mathfrak C_{\mathrm{tar}}
=
(d,Y,\eta,(\Sigma_{d-1},C),L,\tau,\lambda,\mathfrak f,\Lambda,
\hbar_{\mathrm{tar}},\mathcal O_{\mathrm{tar}},
\chi_{\mathrm{cl}},\chi_{\mathrm{op}},\chi_{\mathrm{anom}},
\mathcal K_{\mathrm{obs}},\mathfrak K_{\mathrm{KD}},\Theta_{\mathrm{KD}})
\]
whose formal restriction is identified with the local convention base
\(\mathfrak C_{\mathrm{loc}}^{(2)}\).

The acceptance vector is
\[
  \operatorname{Ob}_{\mathfrak C_{\mathrm{tar}}}
  =
  (\operatorname{per}_{\mathrm{tar}},
   \operatorname{ob}_{\mathrm{WR}},
   \operatorname{ob}_{\mathrm{anom}},
   \operatorname{ob}_{\mathrm{QME}},
   \operatorname{ob}_{\mathrm{conv}},
   \operatorname{ob}_{\mathrm{hyp}},
   \operatorname{ob}_{\mathrm{VolIII}},
   \operatorname{ob}_{\mathrm{Igusa/BKM}},
   \operatorname{ob}_{6r},
   \operatorname{ob}_{\mathrm{MD}}),
\]
with target-specific components omitted only when the corresponding
structure is not asserted.

The transported Koszul-duality acceptance class is
\[
  \operatorname{Ob}_{\mathrm{UKD}}(\mathfrak C_{\mathrm{tar}})
  =
  \left(
    \operatorname{Ob}_{\mathfrak C_{\mathrm{tar}}},
    [d\Theta_{\mathrm{KD}}+\tfrac12[\Theta_{\mathrm{KD}},\Theta_{\mathrm{KD}}]]
  \right)
  \in
  H^1(\mathcal K_{\mathrm{obs}})
  \oplus
  H^1(\mathfrak K_{\mathrm{KD}}).
\]

If this class is zero and a compatible null-homotopy is chosen, the
target theorem gets the accepted morphism
\[
  \Phi_{\mathfrak C_{\mathrm{tar}}}\colon
  \mathrm{Obs}^{\mathrm{cl}}_{\mathrm{closed},\mathrm{tar}}\big|_L
  \longrightarrow
  \mathrm Z^{P_0}_{\mathrm{fact}}
  (\mathrm{Obs}^{\mathrm{cl}}_{\mathrm{open},\mathrm{tar}})
\]
whose formal restriction is
\[
  \chi_{\mathrm{op}}^{-1}
  \Phi^{\mathrm{Ham}}_{\mathrm{fact}}
  \chi_{\mathrm{cl}}.
\]

## Exact Obstruction Theorem Target

Order the obstruction search by dependency:

1. target convention mismatch;
2. Hamiltonian period;
3. scalar/anomaly normalization;
4. first Weiss/Ran descent class;
5. higher Weiss/Ran coherence tower;
6. product-disk versus arbitrary-Ran hyperdescent and \(\varprojlim^1\);
7. cotangent boundary realization;
8. product and \(P_0\)-centrality homotopies;
9. brane-defect QME curvature;
10. convergence of the transported Maurer-Cartan tower;
11. mixed six-relation or mixed-Dunn obstruction;
12. Vol III, Igusa/BKM, compact-CY, CoHA, or VOA target-specific
    obstruction.

The obstruction theorem says: for the first nonzero component in this
dependency order, no global or external matched-conventions theorem with
the asserted target structure exists whose formal restriction is the
local Hamiltonian BF/Moyal map.  The nonzero component is the precise
cohomology class, curvature class, \(\varprojlim^1\) class, or source
fixture gap blocking the transfer.

This is the supremum form: either construct all data and null-homotopies,
or prove the first obstruction.  Do not replace it by a vague
conditional theorem.

## Verification Commands

Commands used to ground this report:

```bash
git status --short
sed -n '1,220p' CLAUDE.md
sed -n '1,260p' AGENTS.md
sed -n '1,260p' /Users/raeez/ecosystem/skills/claude-code/attack-heal-swarm-plugin/skills/attack-heal-swarm/SKILL.md
sed -n '1,260p' /Users/raeez/ecosystem/skills/shared/attack-heal-swarm/protocol.md
sed -n '1,260p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
rg -n "Weiss|Ran|descent|firewall|matched-conventions|compact|CoHA|BKM|VOA|Vol III" main.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex local-dictionary.tex principles.tex tate-P5-cross-volume.tex
nl -ba tate-P5-cross-volume.tex | sed -n '153,415p'
nl -ba open-obligations.tex | sed -n '757,888p'
nl -ba open-obligations.tex | sed -n '1083,1122p'
nl -ba claim-strength-ledger.tex | sed -n '481,546p'
nl -ba local-dictionary.tex | sed -n '13,166p'
nl -ba /Users/raeez/chiral-bar-cobar-vol2/notes/antipatterns_catalogue.md | sed -n '9980,10005p'
nl -ba /Users/raeez/chiral-bar-cobar-vol2/notes/antipatterns_catalogue.md | sed -n '10106,10124p'
```
