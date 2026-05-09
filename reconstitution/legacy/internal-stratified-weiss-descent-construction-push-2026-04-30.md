# Internal Stratified Weiss Descent Construction Push

Agent: 266.

Date: 2026-04-30.

Worktree: `/Users/raeez/topological-strings`.

Branch: `master`.

Owned writable files:

- `reconstitution/internal-stratified-weiss-descent-construction-push-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-266-internal-stratified-weiss-descent-construction-push.md`

No manuscript TeX, scripts, bibliography, source fixture, PDF, or figure
artifact was edited.

## Claim Attacked

The claim under attack is the strongest internal version of the stratified
Weiss/Ran descent theorem:

> The mixed HT pair
> \[
>   X=\mathbb R_t\times\mathbb R_s\times\mathbb C^2_{z_1,z_2},
>   \qquad
>   L=\mathbb R_t\times\{s=z_1=z_2=0\}
> \]
> carries a normal-\(\Omega\) stratified factorization algebra
> \(\mathcal F^{\mathrm{str}}_{\Omega,N}\) with bulk disks, brane
> intervals, collars, products, stratified Weiss descent, centrality
> homotopies, brane-defect QME curvature cancellation, and a trace-state
> topology, all constructed internally from the mixed HT model.

## Verdict

The construction closes only at the reduced product-basis prefactorization
level.  The full stratified factorization/descent theorem does not close
from the current manuscript data.

The exact obstruction theorem is this:

\[
  \operatorname{Ob}^{266}_{\mathrm{str},\Omega,N}
  =
  (
    \delta_{\mathrm{pref}},
    \delta_{\mathrm{assoc}},
    \delta_{\mathrm{Weiss}},
    \operatorname{ob}_{\mathrm{collar}},
    \operatorname{ob}^{\mathrm{prod}}_{\mathrm{cent}},
    \operatorname{ob}^{P_0}_{\mathrm{cent}},
    \operatorname{ob}^{\mathrm{bd}}_{\mathrm{QME}},
    \operatorname{ob}_{\Omega\text{-}\mathrm{basic}},
    \operatorname{ob}_{\mathrm{tr}\text{-}\mathrm{top}}
  ).
\]

The full theorem is true exactly when this vector vanishes, with chosen
null-homotopies compatible under interval inclusions, finite-window
projections, admissible weight transports, and Cech/Weiss refinements.
The current reduced current identities kill the product and associativity
defects on the reduced product basis, but they do not kill
\(\delta_{\mathrm{Weiss}}\), the collar obstruction, centrality rows,
QME curvature, \(\Omega\)-basic secondary classes, or trace-state topology.

This is an obstruction theorem, not a demotion.  The missing object is now
an explicit total descent/QME Maurer-Cartan problem.

## Evidence Anchors

- `main.tex:1092-1163`: local pair, native Hamiltonian holomorphic
  factorization object, mixed topological-current enhancement, and
  interval principal-part current target.
- `main.tex:1175-1235`: constructed CE/factorization observables and
  extension-by-zero products.
- `main.tex:4239-4255`: Weiss/Ran total obstruction complex for global
  factorization-center descent.
- `main.tex:6390-6404`: reduced principal-part current theorem is not an
  unreduced BV/factorization algebra and supplies no centrality homotopies.
- `main.tex:6436-6480`: unreduced lift requires full BV differential,
  primitive/cumulant projection, and centrality homotopies.
- `main.tex:7411-7568`: Costello perturbative BV specialization requires
  field topology, propagator, anomaly class, counterterms, bulk-to-defect
  kernel, graph normalization, and cotangent current lift.
- `open-obligations.tex:897-1021`: structure maps, descent defect,
  centrality homotopies, Hom-curvature rows, QME curvature, and obstruction
  vector.
- `open-obligations.tex:1030-1143`: trace-state functional,
  normalization, Ward identities, cumulant topology, and trace obstruction
  vector.
- `local-dictionary.tex:441-491`: normal torus, \(V_\Omega\), and
  \(Q_\Omega^2=L_{V_\Omega}\).
- `local-dictionary.tex:518-541`: normal contraction is required data and
  not yet a transported Costello graph/counterterm theorem.
- `local-dictionary.tex:678-712`: stratified datum
  \((\mathcal F_{\Omega,X\setminus L},\mathcal F_{\Omega,L},
  \mathcal M_{\Omega,L},j^*,i^!,\mu_{\mathrm{str}})\) and the open
  \(\Omega\)-obstruction vector.
- `local-dictionary.tex:829-982`: non-scalar Costello/QME obstruction
  habitat and scalar-contact projection gate.
- `local-dictionary.tex:1094-1127`: reduced principal-part brackets do
  not supply Costello estimates, unreduced centrality homotopies, or the
  non-scalar QME.
- `local-dictionary.tex:1508-1518`: reduced principal-part model receives
  an unreduced BV algebra only after centrality, kernel, propagator,
  descent, and BV/QME data are supplied.
- `appendix-factorization-current-conventions.tex:697-790`: normal
  \(\Omega\)-weighted current brackets are algebraic current identities,
  not graph/QME or trace-state theorems.
- `appendix-unreduced-bv-qme.tex:2487-2630`: normal \(\Omega\)-equivariant
  Costello kernel datum, coefficient ring, normal contraction, propagator,
  and normalization requirements.
- `appendix-unreduced-bv-qme.tex:3431-3554`:
  \(Q_\Omega\)-centrality homotopy criterion and secondary
  \(L_{V_\Omega}H\) obstruction.
- `references/primary-sources/weiss-ran-stratified-descent-source-anchors-2026-04-30.md`:
  external sources supply descent grammar only, not the mixed HT
  construction.
- `references/primary-sources/omega-stratified-source-anchors-2026-04-30.md`:
  AFT/Costello/CFG sources are templates or related models, not theorem
  support for this local brane system.

## Constructed Reduced Product-Basis Datum

Let \(\mathcal B^{\mathrm{str}}_{\mathrm{prod}}(X,L)\) be the colored
product-stratified basis with three kinds of basic opens.

1. A bulk product disk is
   \[
     V=D_{t,s}\times B_{z_1,z_2}\subset X,\qquad V\cap L=\varnothing,
   \]
   with \(D_{t,s}\subset\mathbb R^2\) a real disk and
   \(B_{z_1,z_2}\subset\mathbb C^2\) a holomorphic polydisk.

2. A brane interval is
   \[
     I\subset L\simeq\mathbb R_t.
   \]

3. A collared brane basic is
   \[
     C(I;\epsilon,B)
     =
     I_t\times(-\epsilon,\epsilon)_s\times B_{z_1,z_2},
     \qquad C(I;\epsilon,B)\cap L=I.
   \]

Finite disjoint unions of these basics are allowed.  Multimorphisms are
pairwise disjoint inclusions into a target basic or finite union.

### Bulk Value

For a bulk product disk \(U\times B\) the value is the already constructed
mixed CE/factorization object:
\[
  \mathcal F_{\Omega,X}^{\mathrm{red}}(U\times B)
  =
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  \left(
    \Omega^\bullet_c(U)\widehat\otimes
    \Omega_c^{0,\bullet}(B)\widehat\otimes
    (\mathfrak h\ltimes\mathcal P[1])
  \right)
  \widehat\otimes R_\Omega^{N,M}.
\]
Here
\[
  \mathfrak h=\mathbb C[[z_1,z_2]]/\mathbb C\cdot1,\qquad
  \mathcal P=\operatorname{Ann}_{\mathrm{res}}(\mathbb C\cdot1)
  \subset H^2_{(z_1,z_2)}(\mathbb C[[z_1,z_2]])\,dz_1dz_2.
\]
The differential is the total de Rham/Dolbeault/CE differential, with the
normal-\(\Omega\) branch read on the invariant/basic Cartan complex:
\[
  Q_\Omega=Q+\iota_{V_\Omega},\qquad Q_\Omega^2=L_{V_\Omega}.
\]

### Brane Value

On an interval \(I\subset L\), the maximal internally constructed brane
value is the reduced weighted principal-part current branch:
\[
  \mathcal F_{\Omega,L}^{\mathrm{red}}(I)
  =
  A_{\partial,\Omega,\hbar_{\mathrm W}}^{\mathrm{pp},w}(I)
  =
  \widehat{\mathbf S}(\Omega_c^0(I)\widehat\otimes\bar A_{w,\hbar_{\mathrm W}})
  \widehat\otimes
  \widehat{\mathbf S}(\mathcal D'_c(I)\widehat\otimes\mathcal P_w[1]).
\]
The length-one brackets are
\[
  \{B_{p,q}(a),B_{r,s}(b)\}_{\Omega}
  =
  \hbar_\omega(ps-qr)B_{p+r-1,q+s-1}(ab),
\]
\[
  \{B_{p,q}(a),\Theta_{r,s}(B)\}_{\Omega}
  =
  -\hbar_\omega(ps-qr+p-q)\Theta_{r-p+1,s-q+1}(aB),
\]
\[
  \{\Theta_{r,s}(B),\Theta_{u,v}(C)\}_{\Omega}=0.
\]
This uses only multiplication of a compactly supported current by a
smooth compactly supported function.  No product of two distributions is
formed.

### Product Maps

For pairwise disjoint bulk product disks
\[
  U_i\times B_i\subset U\times B
\]
the product map is induced by extension by zero on compactly supported
de Rham/Dolbeault forms, followed by the completed graded-commutative CE
product:
\[
  \mu_X:
  \bigotimes_i
  \mathcal F_{\Omega,X}^{\mathrm{red}}(U_i\times B_i)
  \longrightarrow
  \mathcal F_{\Omega,X}^{\mathrm{red}}(U\times B).
\]

For disjoint brane intervals \(I_i\subset J\), the product map is induced
by extension by zero
\[
  j_!\colon \Omega_c^0(I_i)\to\Omega_c^0(J),
  \qquad
  j_!\colon \mathcal D'_c(I_i)\to\mathcal D'_c(J),
\]
and multiplication in the completed symmetric algebra:
\[
  \mu_L:
  \bigotimes_i
  A_{\partial,\Omega,\hbar_{\mathrm W}}^{\mathrm{pp},w}(I_i)
  \longrightarrow
  A_{\partial,\Omega,\hbar_{\mathrm W}}^{\mathrm{pp},w}(J).
\]
The bracket is compatible with interval extension by zero:
\[
  j_!\{x,y\}_{\Omega,I}=\{j_!x,j_!y\}_{\Omega,J}.
\]

These maps give a reduced product-basis prefactorization datum.  The
proof is formal: extension by zero commutes with \(d_{\mathbb R}\),
\(\bar\partial\), and the CE differential; associativity is functoriality
of extension by zero and associativity of the completed symmetric product;
disjoint-support brackets vanish after extension to a common interval.

### Collar Attempt

For a collar \(C=C(I;\epsilon,B)\), the natural candidate is
\[
  \mathcal M_{\Omega,N}^{\mathrm{cand}}(C;I)
  =
  A_{\partial,\Omega,\hbar_{\mathrm W}}^{\mathrm{pp},w}(I)
\]
with the bulk action obtained by the composite
\[
  \mathcal F_{\Omega,X}^{\mathrm{red}}(C)
  \xrightarrow{\pi_{L,\Omega}^{\mathrm{cand}}}
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  (\Omega_c^\bullet(I)\widehat\otimes(\mathfrak h\ltimes\mathcal P[1]))
  \xrightarrow{\kappa_{\mathrm{coef}}}
  A_{\partial,\Omega,\hbar_{\mathrm W}}^{\mathrm{pp},w}(I).
\]
On generators this would send
\[
  a(t)dt\otimes f\mapsto B_f(a),
  \qquad
  B\otimes\rho\mapsto \Theta_\rho(B).
\]
The second arrow is the reduced coefficient-current interface.  The first
arrow is not presently constructed as a Costello-compatible collar map:
it requires the normal contraction
\[
  \mathsf C_\Omega=(\pi_L,j_L,h_\Omega),\qquad
  Q_\Omega h_\Omega+h_\Omega Q_\Omega=\operatorname{id}-j_L\pi_L,
\]
transported through the brane-defect local-functional target, propagator,
counterterms, and QME differential.  This is the collar obstruction
\(\operatorname{ob}_{\mathrm{collar}}\).

## Stratified Weiss Descent Map

A collared stratified Weiss cover of a stratified open pair
\((V,V_L=V\cap L)\) is a cover \(\mathcal U=\{U_i\}\) by stratified
opens such that every finite subset \(S\subset V\) is contained in some
\(U_i\), and whenever \(S\cap L\neq\varnothing\), the chosen \(U_i\)
contains a product collar of \(S\cap L\) inside \(V\).

For the cochain-observable convention used in the manuscript, define
\[
  \check C^p(\mathcal U;\mathcal F^q)
  =
  \prod_{i_0<\cdots<i_p}
  \mathcal F^q(U_{i_0\cdots i_p}),
  \qquad
  U_{i_0\cdots i_p}=U_{i_0}\cap\cdots\cap U_{i_p}.
\]
The total differential is
\[
  \mathbb D(\alpha_{p,q})
  =
  \check\delta\alpha_{p,q}
  +(-1)^p d_{\mathcal F}\alpha_{p,q}.
\]
The descent map is
\[
  r_{V,\mathcal U}\colon
  \mathcal F^{\mathrm{str}}_{\Omega,N}(V)
  \longrightarrow
  \operatorname{Tot}\check C^\bullet(\mathcal U;
  \mathcal F^{\mathrm{str}}_{\Omega,N}).
\]
The exact Weiss defect is the cone
\[
  \delta_{\mathrm{Weiss}}(V,\mathcal U)
  =
  \operatorname{Cone}(r_{V,\mathcal U}).
\]
Thus \(\delta_{\mathrm{Weiss}}(V,\mathcal U)=0\) means that
\(r_{V,\mathcal U}\) is a quasi-isomorphism.  In the covariant
compact-support convention this is dual to the corresponding homotopy
colimit-to-global cosheaf map; the obstruction is the same after
continuous dualization in the completed nuclear habitats.

The product-basis reduced prefactorization datum above does not prove
\(\delta_{\mathrm{Weiss}}=0\) for arbitrary collared stratified Weiss
covers.  This is exactly the boundary already recorded in the global
Weiss/Ran reports and in the source fixture: external Weiss/Ran sources
give the grammar of the descent test, not this mixed HT verification.

## Centrality Obstruction Cochains

Let
\[
  \mathfrak K^\bullet_{\Omega,M}(I)
  =
  \mathcal K^\bullet_{\mathrm{ns},\Omega,M}(I)
\]
be the finite-window non-scalar Hom complex after the scalar gate
\(\widehat\sigma_{\mathrm{sc},\Omega,M}\) has been constructed.  For a
cover \(\mathcal U\) put
\[
  \operatorname{Tot}\check C^\bullet(\mathcal U;\mathfrak K^\bullet_{\Omega,M})
\]
with the same total differential \(\mathbb D\).

For a closed source generator \(x\) and an unreduced open observable
\(A\), the product-centrality cochain is
\[
  C^{\mathrm{prod}}_{x,A}
  =
  \kappa_\Omega(x)A
  -
  (-1)^{|x||A|}A\kappa_\Omega(x).
\]
The obstruction is
\[
  \operatorname{ob}^{\mathrm{prod}}_{\mathrm{cent}}(x,A)
  =
  [C^{\mathrm{prod}}_{x,A}]
  \in
  H^{|x|+|A|}
  \operatorname{Tot}\check C^\bullet
  (\mathcal U;\mathfrak K^\bullet_{\Omega,M}).
\]
A product-centrality homotopy is a cochain
\[
  H^{\mathrm{prod}}_{x,A}
  \in
  \operatorname{Tot}^{|x|+|A|-1}
  \check C^\bullet(\mathcal U;\mathfrak K^\bullet_{\Omega,M})
\]
such that
\[
  \mathbb D H^{\mathrm{prod}}_{x,A}
  =
  C^{\mathrm{prod}}_{x,A}.
\]

The \(P_0\)-centrality cochain is
\[
  C^{P_0}_{x,A}
  =
  \{\kappa_\Omega(x),A\}_{P_{0,\hbar_{\mathrm{QME}}}}
  -
  \rho_{\mathrm{mod}}(x;A),
\]
and
\[
  \operatorname{ob}^{P_0}_{\mathrm{cent}}(x,A)
  =
  [C^{P_0}_{x,A}]
  \in
  H^{|x|+|A|}
  \operatorname{Tot}\check C^\bullet
  (\mathcal U;\mathfrak K^\bullet_{\Omega,M}).
\]
The homotopy equation is
\[
  \mathbb D H^{P_0}_{x,A}=C^{P_0}_{x,A}.
\]

For generator pairs
\[
  x,y\in\{u_{a(t)dt\otimes f},c_{B,\rho}\},
\]
this is the same finite-window row as the manuscript's Hom-curvature row:
\[
\begin{aligned}
  R^{\mathrm{cent}}_{x,y,\Omega,M}
    ={}&
    \sum_{\Gamma\in\mathsf A^d_{x,y,\Omega,M}}
      \varepsilon_\Gamma d_{M,\Omega}K^M_{\Gamma,\Omega}
    -
    \sum_{\Gamma\in\mathsf A^{\mathrm{CE}}_{x,y,\Omega,M}}
      \varepsilon^{\mathrm{CE}}_\Gamma
      K^M_{\Gamma,\Omega}(\zeta_{\Gamma,x,y,\Omega})\\
    &+
    \frac12
    \sum_{(\Gamma_1,\Gamma_2)\in\mathsf A^{\mathrm{br}}_{x,y,\Omega,M}}
      \varepsilon_{\Gamma_1,\Gamma_2}
      \{K^M_{\Gamma_1,\Omega},K^M_{\Gamma_2,\Omega}\}_{\hbar_{\mathrm{QME}},M,\Omega}
    +R^{\mathrm{ct}}_{x,y,\Omega,M}.
\end{aligned}
\]
The obstruction class is
\[
  [R^{\mathrm{cent}}_{x,y,\Omega,M}]
  \in
  H^{|x|+|y|}
  (\mathcal K^\bullet_{\mathrm{ns},\Omega,M}(I),d_{\mathrm{ns},\Omega,M}),
\]
together with the corresponding \(\varprojlim^1H^{|x|+|y|-1}\)
primitive-compatibility class.

The current reduced brackets kill only the freely adjoined reduced current
defect.  They do not produce \(H^{\mathrm{prod}}\) or \(H^{P_0}\) in the
unreduced brane-defect local-functional complex.

## QME Curvature Obstruction

For a Cech-local bulk-to-defect kernel \(K=\{K_i\}\), the QME descent
equation is the Maurer-Cartan equation in the total Cech dg Lie algebra:
\[
  \mathcal R_{\mathrm{QME}}(K)
  =
  \mathbb D K+\frac12[K,K]_{\hbar_{\mathrm{QME}}}.
\]
In components,
\[
  \mathcal R_{\mathrm{QME},i}^{0,1}
  =
  d_{\mathrm{QME},\Omega}K_i
  +\frac12[K_i,K_i]_{\hbar_{\mathrm{QME}}},
\]
and
\[
  \mathcal R_{\mathrm{QME},ij}^{1,0}
  =
  K_j|_{U_{ij}}-K_i|_{U_{ij}}
\]
before transition homotopies are chosen.  Higher components are the
ordinary Cech cocycle defects for the chosen transition homotopies.

The QME obstruction is
\[
  \operatorname{ob}^{\mathrm{bd}}_{\mathrm{QME}}
  =
  [\mathcal R_{\mathrm{QME}}(K)]
  \in
  H^1
  \operatorname{Tot}\check C^\bullet
  (\mathcal U;\mathfrak Q^\bullet_{\Omega,M}),
\]
after the scalar gate
\[
  \widehat\sigma_{\mathrm{sc},\Omega,M}(\mathcal R_{\mathrm{QME}}(K))=0
\]
has placed the row in the non-scalar kernel.  A counterterm
\(C\in\operatorname{Tot}^0\check C^\bullet(\mathcal U;\mathfrak Q^\bullet)\)
changes the first unsolved row by
\[
  \mathcal R_{\mathrm{QME}}(K+C)
  =
  \mathcal R_{\mathrm{QME}}(K)
  +\mathbb D C+[K,C]+\frac12[C,C].
\]
Thus the obstruction is killed exactly by compatible counterterms and
transition homotopies.  No reduced current bracket or normal-weight
localization identity supplies this equation.

## Omega-Basic Obstruction

The normal torus is
\[
  T_\Omega=
  \mathbb C^*_{\epsilon_s}\times
  \mathbb C^*_{\epsilon_1}\times
  \mathbb C^*_{\epsilon_2},
  \qquad
  V_\Omega=
  \epsilon_s s\partial_s+\epsilon_1z_1\partial_{z_1}
  +\epsilon_2z_2\partial_{z_2},
  \qquad V_\Omega(t)=0.
\]
Because \(Q_\Omega^2=L_{V_\Omega}\), every homotopy entering the descent
theorem must be basic.  For a centrality primitive \(H\), the secondary
obstruction is
\[
  \ell^{266}_{x,A,\Omega,M}
  =
  [L_{V_\Omega}H_{x,A,\Omega,M}]
  \in
  H^{|x|+|A|}
  (\mathcal K^\bullet_{\mathrm{ns},\Omega,M}(I),d_{\mathrm{ns},\Omega,M}).
\]
For a QME kernel \(K\), the analogous basic obstruction is
\[
  \ell^{266}_{K,\Omega,M}
  =
  [L_{V_\Omega}K_{\Omega,M}]
  \in
  H^1(\mathfrak Q^\bullet_{\Omega,M},d_{\mathrm{QME},\Omega}).
\]
These vanish automatically only after the construction is made in the
invariant/basic Cartan subcomplex.  A primitive chosen before passing to
invariants is not a \(Q_\Omega\)-homotopy until the corresponding
\(L_{V_\Omega}\)-class vanishes.

## Trace-State Topology Obstruction

Even if the stratified factorization object is constructed, a protected
trace theorem requires a continuous state
\[
  \omega_{N,\Omega}\colon
  \int_{L\subset X}\mathcal F^{\mathrm{str}}_{\Omega,N}
  \longrightarrow
  R_\Omega^{N,M}[[\hbar_{\mathrm{QME}}]]
\]
with a BRST/BV lift \(\widetilde\omega_{N,\Omega}\).  The state
obstruction is
\[
  \operatorname{ob}_{\mathrm{state}}
  =
  [D_{N,\Omega}^{\vee}\widetilde\omega_{N,\Omega}]
\]
in the continuous dual completed BRST/BV complex, together with the
moment-map and gauge-action Ward functionals
\[
  \widetilde\omega_{N,\Omega}(\widehat\mu(\xi)F),\qquad
  \widetilde\omega_{N,\Omega}(\xi\cdot F).
\]
The topology obstruction is the failure to place all cumulants in a
declared topology \(\mathcal T_\Omega\).  Equivalently, for each trace
tuple, truncation, Laurent coefficient, and distributional test
functional, the coefficient sequence defines a class in the quotient of
all sequences by the subspace with a Poincare expansion in
\(N_{\mathrm{rk}}^{-2}\).  This quotient class is
\(\operatorname{ob}_{\mathrm{asymp}}\).  It is not touched by algebraic
stable trace generators.

## Attack Ledger

```yaml
- id: A1-266-01
  severity: 1
  status: healed
  lens: product-basis construction
  target: reduced stratified product-basis prefactorization datum
  claim: The internal mixed HT objects at least form a reduced product-basis prefactorization datum.
  broken_step: None at the reduced product-basis level after branch choice; extension by zero supplies products.
  evidence_type: derivation
  evidence_ref: main.tex:1175-1235; appendix-factorization-current-conventions.tex:697-790
  confidence: high
  minimal_heal: record the construction only on the reduced product-stratified basis.
  residual: arbitrary stratified Weiss descent and collars remain open.

- id: A1-266-02
  severity: 1
  status: valid
  lens: collar module
  target: collars C(I;epsilon,B)
  claim: The reduced interval current algebra automatically gives the collar module.
  broken_step: The needed normal contraction and bulk-to-defect map have not been transported through Costello local functionals, propagators, counterterms, and QME differential.
  evidence_type: proof_gap
  evidence_ref: local-dictionary.tex:518-541; main.tex:7411-7568
  confidence: high
  minimal_heal: construct \(\pi_{L,\Omega}\), \(\kappa_{\Omega,N}\), and compatible collar action.
  residual: \(\operatorname{ob}_{\mathrm{collar}}\).

- id: A1-266-03
  severity: 1
  status: valid
  lens: Weiss descent
  target: arbitrary collared stratified Weiss covers
  claim: Product-basis prefactorization gives arbitrary stratified Weiss descent.
  broken_step: Product-basis products do not prove the Cech totalization map is a quasi-isomorphism for arbitrary collared stratified Weiss covers.
  evidence_type: proof_gap
  evidence_ref: main.tex:4239-4255; open-obligations.tex:911-918; references/primary-sources/weiss-ran-stratified-descent-source-anchors-2026-04-30.md
  confidence: high
  minimal_heal: prove \(\delta_{\mathrm{Weiss}}(V,\mathcal U)=0\) for the constructed stratified object.
  residual: cone of \(r_{V,\mathcal U}\).

- id: A1-266-04
  severity: 1
  status: valid
  lens: centrality homotopies
  target: product and \(P_0\)-centrality against unreduced open observables
  claim: Reduced current bracket identities provide centrality homotopies.
  broken_step: Reduced brackets live after de Rham-current contraction and freely adjoined current variables; the required homotopies live in the unreduced brane-defect local-functional complex.
  evidence_type: proof_gap
  evidence_ref: main.tex:6390-6404; main.tex:6436-6480; appendix-unreduced-bv-qme.tex:3431-3554
  confidence: high
  minimal_heal: construct \(H^{prod}\), \(H^{P_0}\), and compatible finite-window/Roos primitives.
  residual: \(\operatorname{ob}^{prod}_{cent}\), \(\operatorname{ob}^{P_0}_{cent}\).

- id: A1-266-05
  severity: 1
  status: valid
  lens: QME curvature
  target: brane-defect Costello kernel
  claim: Normal localization or reduced current brackets solve the QME.
  broken_step: The QME is a curvature equation in the local-functional complex after scalar projection and counterterm recursion; neither localization nor reduced brackets supplies it.
  evidence_type: proof_gap
  evidence_ref: local-dictionary.tex:829-982; local-dictionary.tex:1094-1127; appendix-unreduced-bv-qme.tex:2487-2630
  confidence: high
  minimal_heal: solve \(\mathbb D K+\frac12[K,K]=0\) with counterterms.
  residual: \(\operatorname{ob}^{bd}_{QME}\).

- id: A1-266-06
  severity: 1
  status: valid
  lens: Omega basicness
  target: \(Q_\Omega\)-homotopies
  claim: A nonequivariant primitive is automatically a \(Q_\Omega\)-primitive.
  broken_step: \(Q_\Omega^2=L_{V_\Omega}\); primitives must be basic or the secondary class \([L_{V_\Omega}H]\) remains.
  evidence_type: derivation
  evidence_ref: local-dictionary.tex:481-491; appendix-unreduced-bv-qme.tex:3431-3554
  confidence: high
  minimal_heal: construct primitives in the basic Cartan subcomplex.
  residual: \(\operatorname{ob}_{\Omega\text{-}basic}\).

- id: A1-266-07
  severity: 1
  status: valid
  lens: trace-state topology
  target: protected trace and physical large-\(N\) theorem
  claim: Algebraic stable trace generators produce the physical trace state.
  broken_step: A state, normalization, Ward identities, cumulant topology, and Poincare asymptotic expansion are separate data.
  evidence_type: proof_gap
  evidence_ref: open-obligations.tex:1030-1143; reconstitution/omega-physical-largeN-state-construction-target-2026-04-30.md
  confidence: high
  minimal_heal: construct \(\omega_{N,\Omega}\), \(\nu_{\Omega,N}\), \(\mathcal T_\Omega\), and Ward identities.
  residual: \(\operatorname{ob}_{tr-top}\).
```

## TeX-Ready Insertion

```tex
\begin{defn}[Internal stratified Weiss obstruction complex]
Let
\[
  X=\mathbb R_t\times\mathbb R_s\times\mathbb C^2_{z_1,z_2},
  \qquad
  L=\mathbb R_t\times\{s=z_1=z_2=0\}.
\]
A collared stratified Weiss cover of a stratified open pair
\((V,V\cap L)\) is a cover \(\mathcal U=\{U_i\}\) by stratified opens
such that every finite subset of \(V\) lies in some \(U_i\), and whenever
the finite subset meets \(L\), the same \(U_i\) contains a product collar
of its lower-stratum part.

For a candidate stratified mixed HT object
\(\mathcal F^{\mathrm{str}}_{\Omega,N}\), set
\[
  \check C^p(\mathcal U;\mathcal F^q)
  =
  \prod_{i_0<\cdots<i_p}
  \mathcal F^q(U_{i_0}\cap\cdots\cap U_{i_p}),
  \qquad
  \mathbb D=\check\delta+(-1)^p d_{\mathcal F}.
\]
The Weiss descent defect is the cone
\[
  \delta_{\mathrm{Weiss}}(V,\mathcal U)
  =
  \operatorname{Cone}\left(
  \mathcal F^{\mathrm{str}}_{\Omega,N}(V)
  \longrightarrow
  \operatorname{Tot}\check C^\bullet(\mathcal U;
  \mathcal F^{\mathrm{str}}_{\Omega,N})
  \right).
\]
\end{defn}

\begin{thm}[Internal stratified descent obstruction theorem]
Fix a branch of the brane algebra, a normal-\(\Omega\) coefficient ring,
and a finite-window Costello local-functional habitat.  The local mixed HT
pair carries the corresponding stratified factorization algebra with
collars, product and \(P_0\)-centrality homotopies, brane-defect QME
curvature cancellation, and trace-state topology if and only if the
obstruction vector
\[
  \operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}
  =
  (
    \delta_{\mathrm{pref}},
    \delta_{\mathrm{assoc}},
    \delta_{\mathrm{Weiss}},
    \operatorname{ob}_{\mathrm{collar}},
    \operatorname{ob}^{\mathrm{prod}}_{\mathrm{cent}},
    \operatorname{ob}^{P_0}_{\mathrm{cent}},
    \operatorname{ob}^{\mathrm{bd}}_{\mathrm{QME}},
    \operatorname{ob}_{\Omega\mathrm{-basic}},
    \operatorname{ob}_{\mathrm{tr}\mathrm{-top}}
  )
\]
vanishes with compatible null-homotopies.  Here
\[
  \operatorname{ob}^{\mathrm{prod}}_{\mathrm{cent}}(x,A)
  =
  [\kappa_\Omega(x)A-(-1)^{|x||A|}A\kappa_\Omega(x)]
\]
and
\[
  \operatorname{ob}^{P_0}_{\mathrm{cent}}(x,A)
  =
  [\{\kappa_\Omega(x),A\}_{P_{0,\hbar_{\mathrm{QME}}}}
  -\rho_{\mathrm{mod}}(x;A)]
\]
are classes in the total Cech non-scalar Hom complex,
\[
  \operatorname{ob}^{\mathrm{bd}}_{\mathrm{QME}}
  =
  [\mathbb D K+\tfrac12[K,K]_{\hbar_{\mathrm{QME}}}],
\]
and
\[
  \operatorname{ob}_{\Omega\mathrm{-basic}}
  =
  [L_{V_\Omega}H]
\]
for any primitive chosen before passing to the basic Cartan subcomplex.
\end{thm}
```

## Proof/Verification

1. The reduced product-basis prefactorization construction is internal:
   it uses the CE/factorization observables and extension-by-zero products
   in `main.tex:1175-1235`, plus the interval current identities in
   `appendix-factorization-current-conventions.tex:697-790`.

2. The construction does not extend to an unconditional collar theorem:
   the normal contraction in `local-dictionary.tex:518-541` is required
   data and has not been transported through the Costello local-functional
   package demanded in `main.tex:7411-7568`.

3. The descent map is an explicit Cech totalization map.  Its cone is the
   exact defect.  This matches the manuscript obstruction surface in
   `open-obligations.tex:911-918` and the global Weiss/Ran total complex
   in `main.tex:4239-4255`.

4. The centrality obstruction equations are exactly the homotopy equations
   in `open-obligations.tex:920-997` and the finite-window
   \(Q_\Omega\)-centrality criterion in
   `appendix-unreduced-bv-qme.tex:3431-3554`.

5. The QME row is the total Cech Maurer-Cartan curvature.  Existing
   reduced current brackets are explicitly excluded as QME evidence by
   `local-dictionary.tex:1094-1127`.

6. External source anchors were used only as descent grammar.  The source
   fixtures explicitly state that none of Costello-Gwilliam, Boavida-Weiss,
   AFT, Costello Omega/M2, or CFG constructs this mixed HT brane object.

## Commands Run

```bash
sed -n '1,240p' AGENTS.md
sed -n '1,240p' CLAUDE.md
sed -n '1,260p' /Users/raeez/ecosystem/skills/shared/attack-heal-swarm/protocol.md
sed -n '1,260p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
git status --short
rg -n "(^##? IV|Russian|Voice|destructive|standalone)" /Users/raeez/ecosystem/INVARIANTS.md
rg -n "(^##? VIII|Self-reflection|rubric|Correctness|Rigor|Attribution|Supremum)" /Users/raeez/ecosystem/AGENTS-HARNESS.md
sed -n '1,560p' references/primary-sources/weiss-ran-stratified-descent-source-anchors-2026-04-30.md
rg --files reconstitution references/primary-sources | rg -i 'weiss|ran|stratified|omega|trace|largeN|large-n|state|factorization'
nl -ba main.tex | sed -n '1090,1235p'
nl -ba main.tex | sed -n '4080,4275p'
nl -ba main.tex | sed -n '6380,6495p'
nl -ba main.tex | sed -n '7400,7570p'
nl -ba open-obligations.tex | sed -n '860,1145p'
nl -ba local-dictionary.tex | sed -n '420,990p'
nl -ba local-dictionary.tex | sed -n '1090,1128p'
nl -ba local-dictionary.tex | sed -n '1508,1522p'
nl -ba appendix-factorization-current-conventions.tex | sed -n '697,790p'
nl -ba appendix-factorization-current-conventions.tex | sed -n '880,965p'
nl -ba appendix-factorization-current-conventions.tex | sed -n '1185,1235p'
nl -ba appendix-unreduced-bv-qme.tex | sed -n '2480,2675p'
nl -ba appendix-unreduced-bv-qme.tex | sed -n '3430,3565p'
nl -ba claim-strength-ledger.tex | sed -n '180,236p'
nl -ba claim-strength-ledger.tex | sed -n '490,510p'
nl -ba claim-strength-ledger.tex | sed -n '730,790p'
nl -ba theorem-lanes.tex | sed -n '1668,1720p'
nl -ba theorem-lanes.tex | sed -n '2350,2468p'
sed -n '1,280p' reconstitution/global-weiss-ran-descent-firewall-construction-target-2026-04-30.md
sed -n '1,280p' reconstitution/swarm-2026-04-30-agent-238-global-weiss-ran-descent-firewall-construction-target.md
sed -n '1,280p' reconstitution/swarm-2026-04-30-agent-178-stratified-trace-obligations-0957.md
sed -n '1,280p' reconstitution/swarm-2026-04-30-agent-186-omega-stratified-source-audit-0957.md
sed -n '1,560p' reconstitution/omega-physical-largeN-state-construction-target-2026-04-30.md
sed -n '1,280p' reconstitution/full-open-bv-factorization-center-construction-target-2026-04-30.md
sed -n '1,280p' reconstitution/swarm-2026-04-30-agent-234-full-open-bv-factorization-center-construction-target.md
sed -n '1,260p' reconstitution/native-E2-factorization-construction-2026-04-30.md
sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-199-native-E2-factorization-construction.md
sed -n '1,220p' mathmacros.tex
sed -n '1,220p' commands.tex
sed -n '1,180p' notation.tex
sed -n '1,220p' preamble.tex
sed -n '1,120p' main.tex
sed -n '1,220p' scripts/check_moyal_coefficients.py
python3 scripts/check_moyal_coefficients.py
kill 52746
ps -axo pid,command | rg 'check_moyal_coefficients|python3 scripts/check'
git branch --show-current
```

The `python3 scripts/check_moyal_coefficients.py` run produced no output
within the interactive wait window and was terminated.  It is not used as
evidence for this descent report.

## Files Changed

- Added `reconstitution/internal-stratified-weiss-descent-construction-push-2026-04-30.md`.
- Added `reconstitution/swarm-2026-04-30-agent-266-internal-stratified-weiss-descent-construction-push.md`.

No PDF build was run.
