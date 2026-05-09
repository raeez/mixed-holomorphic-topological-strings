# Native CxR/VOA/Zhu Reduction Construction Target

Date: 2026-04-30.
Writable scope for this report: this file and
`reconstitution/swarm-2026-04-30-agent-228-native-cxr-voa-zhu-reduction-construction-target.md`.

## Verdict

The strongest stable target is a retained-mode reduction.  The target is
not a one-variable Hamiltonian theory on
\(\mathbb C[[z_1]]/\mathbb C\).  It is a \(\mathbb C_{z_1}\times
\mathbb R_t\) mixed shadow whose coefficient system still carries the
formal \(z_2\)-modes and the full two-index Matlis principal-part dual.

The reduction datum to construct is
\[
  R_{\mathbb C\times\mathbb R}
  =
  (\pi,B_{z_2},\pi_!,K_{\mathrm{red}},
   L_{\mathrm{red}},\langle-,-\rangle_{\mathrm{red}},H_{\mathrm{anom}}).
\]
Its algebraic core is determined.  Its analytic/factorization and
anomaly-transport parts remain exact obstruction problems.

The native object remains the holomorphic factorization algebra on
\(\mathbb C^2\)
\[
  \mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}(B)
  =
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  \bigl(
    \Omega_c^{0,\bullet}(B)\widehat\otimes
    (\mathfrak h\ltimes\mathcal P[1])
  \bigr),
  \qquad
  \mathfrak h=\mathbb C[[z_1,z_2]]/\mathbb C\cdot1 .
\]
A curve VOA or Zhu theorem is admissible only after
\(R_{\mathbb C\times\mathbb R}\) and an additional factorization-to-vertex
package have been constructed.

## Evidence Anchors

- `CLAUDE.md`: native \(\mathbb C^2\) factorization object and controlled
  reduction firewall.
- `AGENTS.md`: curve VOA/Zhu comparison requires reduced directions,
  retained \(z_2\)-modes or principal parts, pushforward, pairing, brane
  image, and anomaly data.
- `main.tex:80-184`: local pair, Dirac brane, Hamiltonian algebra, scalar
  quotient.
- `main.tex:1111-1240`: constructed Hamiltonian CE/factorization
  observables and no native one-dimensional OPE.
- `main.tex:1242-1452`: finite-window Bochner-Martinelli transfer and the
  two-index principal-part obstruction to killing \(z_2\).
- `appendix-matlis-principal-parts.tex:27-244`: continuous dual and
  Matlis coadjoint action.
- `appendix-factorization-current-conventions.tex:36-120`,
  `:277-397`: interval current source, principal-part current dual, and
  strict reduced current brackets.
- `theorem-lanes.tex:698-884`: current controlled \(\mathbb C\times\mathbb R\)
  theorem surface and obstruction vector.
- `theorem-lanes.tex:886-1025`: reduced Dirac BRST/Zhu surface, conditional
  on controlled reduction.
- Vol II `chapters/connections/concordance.tex:12-20`: status words are
  part of the mathematics; no theorem is strengthened by concordance.
- Vol II `chapters/theory/sc_chtop_heptagon.tex:218-265`: the
  \(\mathsf{SC}^{\mathrm{ch,top}}\) target is a two-coloured curve/topological
  operadic shadow, not this reduction theorem.
- Vol II `chapters/connections/hochschild.tex:674-782`: the Zhu bridge
  exists for a graded vertex algebra with conformal vector and has
  additional finiteness hypotheses for quasi-isomorphism claims.

## The Target Datum

### 1. Projection

The projection is fixed:
\[
  X=\mathbb R_t\times\mathbb R_s\times
    \mathbb C_{z_1}\times\mathbb C_{z_2},
  \qquad
  Y=\mathbb R_t\times\mathbb C_{z_1},
\]
\[
  \pi:X\to Y,\qquad \pi(t,s;z_1,z_2)=(t;z_1).
\]
For product opens
\[
  U=I_t\times J_s\times D_{z_1}\times E_{z_2},
  \qquad
  V=I_t\times D_{z_1},
\]
the native mixed dg Lie input is
\[
  \mathfrak G_X(U)
  =
  \Omega_c^\bullet(I)\widehat\otimes
  \Omega_c^\bullet(J)\widehat\otimes
  \Omega_c^{0,\bullet}(D)\widehat\otimes
  \Omega_c^{0,\bullet}(E)\widehat\otimes
  (\mathfrak h\ltimes\mathcal P[1]).
\]
The desired reduced input is
\[
  \mathfrak G_Y(V)
  =
  \Omega_c^\bullet(I)\widehat\otimes
  \Omega_c^{0,\bullet}(D)\widehat\otimes
  (\mathfrak h_{\mathrm{red}}\ltimes\mathcal P_{\mathrm{red}}[1])
  \otimes o_\pi ,
\]
where
\[
  o_\pi=H_c^1(J_s)\otimes H_c^{0,1}(E_{z_2})
\]
is the fiber orientation/cohomology line.  A later theorem may trivialize
\(o_\pi\); if it does, the sign and degree shifts must be stated.

### 2. Retained \(z_2\)-Coefficient System

The coefficient system is
\[
  B_{z_2}
  =
  (\mathfrak h_{\mathrm{red}},\mathcal P_{\mathrm{red}},
   \operatorname{Res}_{z_1,z_2},\{-,-\}_{\mathrm{red}},
   \operatorname{ad}^{\vee}_{\mathrm{red}}),
\]
with
\[
  \mathfrak h_{\mathrm{red}}
  =
  \mathbb C[[z_1]][[z_2]]/\mathbb C\cdot1
  \cong
  \mathbb C[[z_1,z_2]]/\mathbb C\cdot1
\]
read as formal \(z_2\)-coefficients over the curve coordinate \(z_1\).
The cotangent module is
\[
  \mathcal P_{\mathrm{red}}
  =
  \operatorname{Ann}_{\mathrm{res}}(\mathbb C\cdot1)
  \subset
  H^2_{(z_1,z_2)}(\mathbb C[[z_1,z_2]])\,dz_1dz_2,
\]
\[
  \rho_{a,b}=z_1^{-a-1}z_2^{-b-1}dz_1dz_2,\qquad a+b>0,
\]
with pairing
\[
  \langle\rho_{a,b},z_1^mz_2^n\rangle_{\mathrm{red}}
  =
  \operatorname{Res}_{z_1,z_2}(\rho_{a,b}z_1^mz_2^n)
  =
  \delta_{a,m}\delta_{b,n}.
\]
The bracket is still the two-variable Hamiltonian bracket
\[
  \{f,g\}_{\mathrm{red}}
  =
  \partial_{z_1}f\,\partial_{z_2}g
  -
  \partial_{z_2}f\,\partial_{z_1}g
  \pmod{\mathbb C}.
\]
For monomials,
\[
  \{z_1^az_2^b,z_1^cz_2^d\}_{\mathrm{red}}
  =
  (ad-bc)z_1^{a+c-1}z_2^{b+d-1}.
\]
The coadjoint action is fixed by residue integration by parts:
\[
  z_1^pz_2^q\cdot\rho_{i,j}
  =
  -(pj-qi+p-q)\rho_{i-p+1,j-q+1},
\]
with negative-index targets equal to zero.

This proves the first obstruction theorem: the quotient
\(\mathbb C[[z_1]]/\mathbb C\) is not an admissible reduction.  It kills
\(\partial_{z_2}\), hence kills the Hamiltonian bracket, the Moyal
bivector, and the scalar cocycle represented by \(\{z_1,z_2\}=1\).

It also proves the second obstruction theorem: the literal \(b=0\)
principal-part residue line is not stable.  Indeed
\[
  z_1\cdot\rho_{a,0}=-\rho_{a,1}.
\]
Thus no theorem may replace \(\mathcal P_{\mathrm{red}}\) by the
\(b=0\) line without changing the Hamiltonian action or proving a new
invariant quotient.

### 3. Pushforward and Kernel Target

The pushforward \(\pi_!\) must be a chain map with homotopy data
\[
  K_{\mathrm{red}}
  =
  (p_s,i_s,K_s;\;p_{z_2},i_{z_2},K_{z_2};\;\tau_\pi),
\]
where \(\tau_\pi\) is the chosen trivialization or explicit retention of
the orientation line \(o_\pi\).

For the real topological fiber, choose an oriented interval \(J\) and
\(\lambda_J(s)ds\in\Omega_c^1(J)\) with \(\int_J\lambda_Jds=1\).  Then
\[
  p_s(\alpha)=\int_J\alpha,\qquad i_s(1)=\lambda_Jds,
\]
and \(K_s\) must satisfy
\[
  d_sK_s+K_sd_s=\operatorname{id}-i_sp_s .
\]
The surviving line is \(H_c^1(J)\cong\mathbb C[-1]\); it is not an
acyclic contraction.

For the holomorphic fiber, the target is a retained-mode
Cauchy-Green/Serre contraction, not evaluation at \(z_2=0\).  In finite
window \(N\), one may target operators
\[
  p_{z_2,N}:
  \Omega_c^{0,\bullet}(E)\widehat\otimes B_{z_2}
  \longrightarrow
  B_{z_2,\leq N}\otimes H_c^{0,1}(E),
\]
\[
  i_{z_2,N}:B_{z_2,\leq N}\otimes H_c^{0,1}(E)
  \longrightarrow
  \Omega_c^{0,\bullet}(E)\widehat\otimes B_{z_2},
\]
and a Cauchy-Green homotopy \(K_{z_2,N}\) satisfying, modulo collar
terms,
\[
  \bar\partial_{z_2}K_{z_2,N}
  +K_{z_2,N}\bar\partial_{z_2}
  =
  \operatorname{id}-i_{z_2,N}p_{z_2,N}.
\]
The moment projection is normalized by
\[
  p_{z_2,N}(\alpha)_{b}
  =
  \frac{1}{2\pi i}\int_E z_2^b\,\alpha^{0,1}(z_2)\wedge dz_2,
  \qquad 0\leq b\leq N,
\]
and is interpreted through the retained principal-part coefficient
\(\rho^{(2)}_b=z_2^{-b-1}dz_2\), not through a collapse to \(b=0\).

The exact chain-homotopy obstruction is
\[
  \operatorname{ob}_{K,N}
  =
  d_FK_{\mathrm{red},N}
  +K_{\mathrm{red},N}d_F
  -
  (\operatorname{id}-i_N\pi_{!,N}),
\]
where \(d_F=d_s+\bar\partial_{z_2}\).  It lives in the degree-zero
endomorphism complex of the finite-window fiber dg module.  The
all-window obstruction is the compatible-system class
\[
  \operatorname{ob}_{K,\infty}
  =
  \bigl(
    [\operatorname{ob}_{K,N}]_{N\geq0},
    [K_{\mathrm{red},N+1}|_N-K_{\mathrm{red},N}]_{N\geq0}
  \bigr)
\]
in the product of finite-window endomorphism cohomologies together with
the derived inverse-limit defect for the chosen window tower.  Vanishing
of this class is the exact analytic \(\pi_!\)-theorem.

### 4. Reduced Brane Image

The brane image is
\[
  L_{\mathrm{red}}=\pi(L)
  =
  \mathbb R_t\times\{z_1=0\}\subset Y .
\]
It is a line defect in \(Y\), not a brane with only one normal matrix.
The \(z_2\)-normal coordinate survives as coefficient data.  At finite
\(N\),
\[
  \operatorname{ev}_N^{\mathrm{red}}(f)
  =
  \overline{\operatorname{Tr}f(X,Y)},
  \qquad X=\phi_1,\quad Y=\phi_2.
\]
For an interval \(I\subset\mathbb R_t\),
\[
  B_f(a)
  =
  \int_Ia(t)\,\overline{\operatorname{Tr}f(X(t),Y(t))}\,dt,
\]
and the reduced current brackets are
\[
  \{B_f(a),B_g(b)\}
  =
  B_{\{f,g\}_{\mathrm{red}}}(ab),
\]
\[
  \{B_f(a),\Theta_\rho(B)\}
  =
  \Theta_{f\cdot\rho}(aB),
  \qquad
  \{\Theta_\rho(B),\Theta_\sigma(C)\}=0.
\]
The obstruction to a stronger closed-to-open factorization-centre theorem
is not in these reduced brackets.  It is the missing collar/stratified
brane module and its centrality homotopies against arbitrary open
observables.

### 5. Reduced Pairing

The coefficient pairing is fixed:
\[
  \langle\rho,f\rangle_{\mathrm{coeff}}
  =
  \operatorname{Res}_{z_1,z_2}(\rho f).
\]
The reduced field pairing must have the form
\[
  \langle \beta_{\mathrm{red}},\alpha_{\mathrm{red}}\rangle_{\mathrm{red}}
  =
  \int_{I\times D}
  \langle\beta_{\mathrm{red}},
  \alpha_{\mathrm{red}}\rangle_{\mathrm{coeff}}\,
  dt\,dz_1
\]
after tensoring with or trivializing \(o_\pi\).  The exact obstruction is
the pairing-defect class
\[
  \operatorname{ob}_{\mathrm{pair}}
  =
  \bigl[
    \langle\pi_!x,\pi_!y\rangle_{\mathrm{red}}
    -
    \pi_!\langle x,y\rangle_X
  \bigr]
  \in
  H^{-1}\bigl((\mathfrak G_Y\widehat\otimes\mathfrak G_Y)^\vee\bigr),
\]
with the declared orientation line included.  This class vanishes only
after the degree shift, sign, residue normalization, and compact-support
orientation convention are fixed.

### 6. Anomaly Homotopy

The reduced scalar class survives.  Since
\[
  \{z_1,z_2\}=1,
\]
the scalar cocycle
\[
  \omega(f,g)=[\{f,g\}_{\mathrm{red}}]_0
\]
remains present, and on the reduced line-current surface it has
representative
\[
  \operatorname{Ob}^{\mathrm{red}}_{\mathrm{sc}}
  (\gamma_{\mathbf1};a,f;b,g)
  =
  \hbar N\,\omega(f,g)
  \int_{\mathbb R_t}a(t)b(t)\gamma_{\mathbf1}(t)\,dt .
\]
Thus \(H_{\mathrm{anom}}\) is not optional.  It is a homotopy or
counterterm solving
\[
  (Q_{\mathrm{red}}+\{I_{\mathrm{red}},-\})H_{\mathrm{anom}}
  =
  \pi_!\mathfrak A_X-\mathfrak A_{\mathrm{red}}
\]
in the reduced local functional complex.  On the scalar component this
includes the Lie-cohomology equation
\[
  d_{\mathrm{CE}}H_{\mathrm{anom,sc}}
  =
  -\hbar N\,\bar c
\]
unless the theorem chooses the unreduced central-character branch,
balanced supertrace branch, or an external closed-exchange/brane-defect
contribution with leading class \(-\hbar N[\bar c]\).

The exact obstruction is
\[
  \operatorname{ob}_{\mathrm{anom}}
  =
  [\pi_!\mathfrak A_X-\mathfrak A_{\mathrm{red}}]
  \in
  H^1_{\mathrm{loc}}
  \bigl(\mathcal O_{\mathrm{red}},
  Q_{\mathrm{red}}+\{I_{\mathrm{red}},-\}\bigr),
\]
with scalar projection
\[
  \hbar N[\bar c]\in H^2_{\mathrm{Lie}}(\bar A;\mathbb C)[[\hbar]].
\]

## Factorization Compatibility

The datum \(R_{\mathbb C\times\mathbb R}\) is a factorization reduction
only if \(\pi_!\) is compatible with extension by zero and disjoint
products.  For two disjoint product opens the binary defect is
\[
  \operatorname{ob}_{\mathrm{fac},2}
  =
  \pi_!\mu_X
  -
  \mu_Y(\pi_!\otimes\pi_!).
\]
For three opens the associativity defect is the corresponding ternary
Stokes/collar class
\[
  \operatorname{ob}_{\mathrm{fac},3}
  =
  \mu_Y(\mu_Y\otimes1)(\pi_!^{\otimes3})
  -
  \mu_Y(1\otimes\mu_Y)(\pi_!^{\otimes3})
\]
after subtracting the pushed-forward native associator.  These classes
must vanish in the homotopy endomorphism complex of the reduced
factorization cosheaf.  In finite windows they are controlled by collar
terms of the Cauchy-Green/Bochner-Martinelli kernels.  The all-window
strict theorem requires uniform control in the \(m\)-adic/principal-part
window.

## Curve VOA and Zhu Target After Reduction

Even after \(R_{\mathbb C\times\mathbb R}\) is built, a curve vertex
algebra needs additional data
\[
  R_{\mathrm{VOA}}
  =
  (V_{\mathrm{red}},\mathbf1,T,Y,
   \operatorname{wt},\zeta_\hbar).
\]
The factorization-to-vertex theorem must produce finite Laurent products
\[
  Y(a,w)b=\sum_{n\in\mathbb Z}(a_{(n)}b)w^{-n-1},
  \qquad a_{(n)}b=0\quad(n\gg0),
\]
with vacuum, translation, and locality.  The obstruction is the finite
Laurent-tail class
\[
  \operatorname{ob}_{\mathrm{VOA}}(a,b)
  =
  \left[
    \mu_{w,0}(a,b)
    -
    \sum_{0\leq n\leq N(a,b)}
    (a_{(n)}b)w^{-n-1}
  \right]
\]
in the quotient of the two-point reduced factorization product by finite
principal parts.  If this class has an infinite singular tail or fails
locality, no vertex algebra has been constructed.

The reduced Dirac BRST candidate is the free vertex algebra with fields
\[
  Z_1{}^i{}_j(z),\quad Z_2{}^i{}_j(z)
  \quad\text{even},\qquad
  c^i{}_j(z),\quad b^i{}_j(z)
  \quad\text{odd},
\]
singular products
\[
  Z_1{}^i{}_j(z)Z_2{}^k{}_\ell(w)
  \sim
  \frac{\hbar\,\delta^i_\ell\delta^k_j}{z-w},
  \qquad
  b^i{}_j(z)c^k{}_\ell(w)
  \sim
  \frac{\delta^i_\ell\delta^k_j}{z-w},
\]
and all other generating singular products regular.  Its BRST current is
\[
  j_{\mathrm{BRST}}
  =
  \operatorname{Tr}(c[Z_1,Z_2])
  +\frac12\operatorname{Tr}(b[c,c]),
  \qquad
  Q_{\mathrm{BRST}}=\operatorname{Res}j_{\mathrm{BRST}}(z)\,dz.
\]
The square-zero computation is algebraic:
\[
  QZ_a=[c,Z_a],\qquad Qc=\frac12[c,c],
  \qquad Qb=[Z_1,Z_2]+[b,c],
\]
\[
  Q[Z_1,Z_2]=[c,[Z_1,Z_2]],
\]
and graded Jacobi gives \(Q^2Z_a=Q^2c=Q^2b=0\) once the scalar anomaly
branch in \(H_{\mathrm{anom}}\) is fixed.

For the Zhu theorem one must prove the conformal weights
\[
  \operatorname{wt}(Z_1)=0,\quad
  \operatorname{wt}(Z_2)=1,\quad
  \operatorname{wt}(c)=0,\quad
  \operatorname{wt}(b)=1.
\]
With zero modes
\[
  X^j{}_i=o(Z_1{}^i{}_j),\quad
  Y^j{}_i=o(Z_2{}^i{}_j),\quad
  C^j{}_i=o(c^i{}_j),\quad
  B^j{}_i=o(b^i{}_j),
\]
the target Zhu relations are
\[
  [Y^j{}_i,X^\ell{}_k]
  =
  \hbar\,\delta^\ell_i\delta^j_k,
  \qquad
  [B^j{}_i,C^\ell{}_k]_{\mathrm{super}}
  =
  \delta^\ell_i\delta^j_k.
\]
The pre-BRST Zhu algebra is expected to be
\[
  W_\hbar(\operatorname{Mat}_N^2)
  \otimes
  \operatorname{Cliff}_{bc}(\mathfrak{gl}_N),
\]
with BRST differential
\[
  QX=[C,X],\qquad QY=[C,Y],\qquad QC=\frac12[C,C],
\]
\[
  QB=YX-XY+\hbar N I+[B,C].
\]
The \(\hbar N I\) term is forced by the manuscript's Capelli/Weyl
normalization; omitting it contradicts the finite-\(N\) quantum
Hamiltonian reduction.

The exact multiplicativity obstruction for the Zhu/zero-mode map is the
Hochschild two-cocycle
\[
  \operatorname{ob}_{\mathrm{Zhu}}(f,g)
  =
  \zeta_\hbar(f*g)-\zeta_\hbar(f)\zeta_\hbar(g)
  \in C^2_{\mathrm{Hoch}}(\bar A_\hbar,\operatorname{Zhu}(V_{\mathrm{red}})).
\]
The Vol II Zhu bridge supplies a map
\[
  \operatorname{ChirHoch}^\bullet(V_{\mathrm{red}})
  \to HH^\bullet(A(V_{\mathrm{red}}))
\]
only after \(V_{\mathrm{red}}\) is a graded vertex algebra with conformal
vector.  It is not automatically a quasi-isomorphism.  The stronger
quasi-isomorphism hypotheses such as rationality and \(C_2\)-cofiniteness
are not proved for this free Dirac BRST reduction and should not be
imported.

## Stable Core

The following claims are stable.

1. The native local object is the \(\mathbb C^2\) Hamiltonian
   CE/factorization algebra, not a curve VOA.
2. Any \(\mathbb C\times\mathbb R\) reduction must use
   \(Y=\mathbb R_t\times\mathbb C_{z_1}\) and retain \(z_2\) as a formal
   coefficient/principal-part system.
3. The algebraic reduced Hamiltonian bracket, Matlis cotangent module,
   residue pairing, and coadjoint action are fixed by the same formulas as
   the native \(\mathbb C^2\) formal disk.
4. The reduced brane image is
   \(L_{\mathrm{red}}=\mathbb R_t\times\{z_1=0\}\), with \(X=\phi_1\) and
   \(Y=\phi_2\) both retained in finite-\(N\) evaluation.
5. The scalar \(U(1)\) anomaly and the Capelli contact
   \(\hbar N I\) survive the reduction unless a named anomaly branch
   cancels them.
6. Vol II \(\mathsf{SC}^{\mathrm{ch,top}}\), chiral Hochschild, and Zhu
   technology are target interfaces after reduction.  They do not
   construct \(R_{\mathbb C\times\mathbb R}\).

## Obstruction Ledger

```yaml
- id: A228-01
  severity: 1
  status: valid
  lens: native-geometry
  claim: A curve VOA or Zhu algebra is native to the C^2 Hamiltonian object.
  broken_step: A vertex algebra requires a complex curve, vacuum, translation, finite Laurent OPEs, and zero modes; the native object is a holomorphic factorization algebra on polydisks in C^2.
  evidence_type: line_reference
  evidence_ref: "main.tex:1111-1240; theorem-lanes.tex:227-696"
  minimal_heal: Use the native CE/factorization algebra as the source and require R_CxR plus R_VOA before any curve statement.
  residual: Construct factorization-to-vertex data after R_CxR.

- id: A228-02
  severity: 1
  status: healed
  lens: coefficient-algebra
  claim: The reduction sends C[[z1,z2]]/C to C[[z1]]/C.
  broken_step: Setting z2=0 kills the Hamiltonian bracket and the Moyal bivector.
  evidence_type: counterexample
  evidence_ref: "{z1,z2}=1 before scalar reduction; P=partial_z1 tensor partial_z2 - partial_z2 tensor partial_z1."
  minimal_heal: Retain h_red=C[[z1]][[z2]]/C as a coefficient system over R_t x C_z1.
  residual: None for the algebraic coefficient target.

- id: A228-03
  severity: 1
  status: healed
  lens: principal-parts
  claim: A z2 residue reduction may keep only b=0 principal parts.
  broken_step: The b=0 line is not stable under the Hamiltonian coadjoint action.
  evidence_type: counterexample
  evidence_ref: "z1.rho_{a,0}=-rho_{a,1}"
  minimal_heal: Keep the full two-index Matlis principal-part module P_red.
  residual: None for the algebraic cotangent target.

- id: A228-04
  severity: 1
  status: valid
  lens: analytic-pushforward
  claim: The reduction datum is constructed once the algebraic retained z2 system is named.
  broken_step: A factorization reduction needs a chain map pi_!, a fiber homotopy K_red, support control, collar cancellation, and compatibility with two- and three-disk products.
  evidence_type: proof_gap
  evidence_ref: "theorem-lanes.tex:856-880; controlled-CxR thread Ob-CxR-01/02/07"
  minimal_heal: Construct finite-window Cauchy-Green/Serre contraction and prove ob_K,infty=0.
  residual: ob_K,infty and ob_fac remain open.

- id: A228-05
  severity: 1
  status: valid
  lens: bv-pairing
  claim: The reduced BV pairing follows automatically from formal residue.
  broken_step: The s compact-support line and z2 Dolbeault/Serre line shift degree and sign; the target pairing must prove compatibility with pi_!.
  evidence_type: proof_gap
  evidence_ref: "local-dictionary.tex:83-114; theorem-lanes.tex:864-868"
  minimal_heal: Include o_pi and prove ob_pair=0.
  residual: orientation/sign convention and degree shift must be fixed in the theorem.

- id: A228-06
  severity: 1
  status: valid
  lens: anomaly
  claim: The CxR reduction cancels the scalar anomaly.
  broken_step: The scalar cocycle survives because the retained coefficient system still has {z1,z2}=1.
  evidence_type: counterexample
  evidence_ref: "theorem-lanes.tex:830-849; theorem-lanes.tex:3346-3385"
  minimal_heal: Carry H_anom and choose a scalar branch with d_CE H_anom,sc=-hbar N cbar, or keep the anomaly as obstruction.
  residual: ob_anom remains open until a branch is selected and proved.

- id: A228-07
  severity: 2
  status: valid
  lens: zhu-bridge
  claim: Vol II Zhu results give the desired CxR/VOA/Zhu theorem directly.
  broken_step: Vol II requires an existing graded vertex algebra with conformal vector; its quasi-isomorphism statements require additional finiteness hypotheses.
  evidence_type: missing_source
  evidence_ref: "chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:674-782"
  minimal_heal: Treat Vol II as a bridge after R_CxR and R_VOA, not as a construction of either.
  residual: ob_VOA and ob_Zhu remain open.
```

## Manuscript Integration Target

A later TeX integration can state:

**Theorem target.**  If the seven-tuple
\[
  R_{\mathbb C\times\mathbb R}
  =
  (\pi,B_{z_2},\pi_!,K_{\mathrm{red}},
   L_{\mathrm{red}},\langle-,-\rangle_{\mathrm{red}},H_{\mathrm{anom}})
\]
satisfies
\[
  \operatorname{ob}_{K,\infty}
  =
  \operatorname{ob}_{\mathrm{fac},2}
  =
  \operatorname{ob}_{\mathrm{fac},3}
  =
  \operatorname{ob}_{\mathrm{pair}}
  =
  \operatorname{ob}_{\mathrm{anom}}
  =
  0,
\]
then the native
\(\mathbb R^2_{\mathrm{top}}\times\mathbb C^2_{\mathrm{hol}}\)
Hamiltonian CE/factorization algebra has a controlled
\(\mathbb C_{z_1}\times\mathbb R_t\) reduced shadow with coefficient
algebra
\[
  \mathfrak h_{\mathrm{red}}
  =
  \mathbb C[[z_1]][[z_2]]/\mathbb C\cdot1,
\]
cotangent module \(\mathcal P_{\mathrm{red}}\), brane image
\[
  L_{\mathrm{red}}=\mathbb R_t\times\{z_1=0\},
\]
and reduced current brackets as displayed above.  A curve VOA/Zhu theorem
then requires, in addition, \(R_{\mathrm{VOA}}\) and vanishing of
\(\operatorname{ob}_{\mathrm{VOA}}\) and \(\operatorname{ob}_{\mathrm{Zhu}}\).

**Obstruction theorem.**  The naive reductions
\[
  \mathbb C[[z_1,z_2]]/\mathbb C\to\mathbb C[[z_1]]/\mathbb C,
  \qquad
  \mathcal P_{\mathrm{red}}\to
  \bigoplus_{a\geq0}\mathbb C\rho_{a,0},
\]
are false as Hamiltonian reductions.  The first kills the bracket and
Moyal bivector.  The second is not stable under the coadjoint action
because \(z_1\cdot\rho_{a,0}=-\rho_{a,1}\).  Thus any valid
\(\mathbb C\times\mathbb R\) curve shadow must retain \(z_2\)-modes or
the full two-index principal-part coefficient system.

## Verification

Read-only checks run:

```bash
sed -n '1,240p' CLAUDE.md
sed -n '1,260p' AGENTS.md
sed -n '1,260p' /Users/raeez/ecosystem/skills/claude-code/attack-heal-swarm-plugin/skills/attack-heal-swarm/SKILL.md
sed -n '1,260p' /Users/raeez/ecosystem/skills/claude-code/attack-heal-swarm-plugin/skills/attack-heal-swarm/references/protocol.md
sed -n '1,260p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
rg -n -e 'chiral' -e 'VOA' -e 'vertex' -e 'Zhu' -e 'z_2' -e 'principal' -e 'factorization' main.tex theorem-lanes.tex local-dictionary.tex
nl -ba main.tex | sed -n '1110,1460p'
nl -ba theorem-lanes.tex | sed -n '227,1030p'
nl -ba appendix-matlis-principal-parts.tex | sed -n '1,260p'
nl -ba appendix-factorization-current-conventions.tex | sed -n '1,460p'
nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex | sed -n '1,260p'
nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex | sed -n '660,800p'
```

No manuscript or script files were edited.
