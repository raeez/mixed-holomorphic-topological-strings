# Local Theorem-Obligation Index, 09:57 Refresh, 2026-04-30

Owner: Agent 196.

Scope:
\[
  X=\mathbb R_t\times\mathbb R_s\times\mathbb C^2_{z_1,z_2},
  \qquad
  L=\mathbb R_t\times\{s=z_1=z_2=0\}.
\]
The native holomorphic object is two-complex-dimensional.  Curve vertex
algebras, Zhu algebras, protected traces, Costello graph/QME closure, and
physical large-\(N\) asymptotics enter only after their named reduction,
stratified, QME, state, normalization, topology, and source-hypothesis data
are constructed.

Evidence packet: `local-theorem-obligations-2026-04-30.md`, the 09:57
critique ingestion and plan, Agent 190 integration map, reports 174--189,
the finite-window script output from `scripts/finite_window_graph_array.py`,
and the launch-log status through Agent 196.  Agent 192's report is present
locally but the launch log still marks Agent 192 live; its current-bracket
row is treated below as provisional after-context, not as part of the
174--190 closed packet.

## Status Legend

- `proved`: proof or computation in the current manuscript/report packet.
- `computed`: script or explicit coordinate computation decides the stated
  finite problem.
- `theorem surface`: correct target has been named, but construction or
  proof remains open.
- `exact obstruction`: the blocking class, map, or counterexample is named.
- `false transfer`: claim cannot enter the local theorem surface without a
  matched-conventions theorem.

## Closed Or Proved Branches

### CL-01. Formal local geometry and firewall

Status: proved/localized.

Closed branch: the theorem surface is the formal-local pair \((X,L)\) with
holomorphic Darboux disk
\((\widehat{\mathbb C^2}_0,dz_1\wedge dz_2)\).  Compact Calabi-Yau, CoHA,
quintic, OSV/GV, Abel-Jacobi, MNOP, Vol III, Igusa, Borcherds, and BKM
claims are external comparison surfaces.

Evidence: Agents 174 and 175; Agent 190 integration map.

Next action: none for the firewall except final manuscript scans after
integration.

### CL-02. Dirac brane probe and Hamiltonian BF package

Status: proved local theorem package.

Closed branch:
\[
  S_\partial=\int_{\mathbb R}\operatorname{Tr}
  (\phi_1\,d\phi_2+A[\phi_1,\phi_2]),
  \qquad Q\psi=[\phi_1,\phi_2],
\]
and the closed Hamiltonian BF sector uses
\[
  \mathfrak h=\mathbb C[[z_1,z_2]]/\mathbb C\cdot1,\qquad
  \mathfrak g=\mathfrak h\ltimes\mathfrak h^\vee_{\rm cont}[1].
\]
The scalar quotient and coordinate CE/PV derived-centre map
\[
  c^I\mapsto\theta^I,\qquad u_I\mapsto O_I
\]
are part of the stable local algebraic core.

Evidence: Agents 174 and 175.

Next action: keep unreduced factorization-centre and QME language outside
this closed branch unless the kernel and centrality homotopies are supplied.

### CL-03. Native holomorphic \(E_2\) / \(\mathbb C^2\) CE object

Status: proved for the CE/factorization assignment; BM transfer still open.

Closed branch:
\[
  \mathcal F_{\rm Ham}^{\rm hol}(B)
  =
  C^\bullet_{\rm CE,cont}
  \bigl(
    \Omega_c^{0,\bullet}(B)\widehat\otimes
    (\mathfrak h\ltimes\mathcal P[1])
  \bigr),
\]
where
\[
  \mathcal P=\operatorname{Ann}_{\rm res}(\mathbb C\cdot1)
  \cong\mathfrak h^\vee_{\rm cont}.
\]
The binary operation is the Hamiltonian/cotangent semidirect bracket and
not a Laurent OPE.

Open part: the Bochner-Martinelli lane still requires a cutoff-controlled
kernel \(H_{\rm BM}\), the normalized \(\bar\partial\)-homotopy identity,
binary/ternary support estimates, and arity-two comparison with the
Hamiltonian/coadjoint bracket.

Evidence: Agent 176.

Next agent needed: native BM transfer constructor, or Agent 194 if its
theorem-lane integration closes with this proof boundary intact.

### CL-04. Classical Matlis/principal-part cotangent module

Status: proved classical theorem surface.

Closed branch:
\[
  \mathfrak h^\vee_{\rm cont}
  =
  \bigoplus_{a+b>0}\mathbb C\,\delta_{a,b}
  \cong
  \mathcal P
  =
  \bigoplus_{a+b>0}\mathbb C\,\rho_{a,b},
  \qquad
  \rho_{a,b}=z_1^{-a-1}z_2^{-b-1}dz_1dz_2.
\]
The action is
\[
  z_1^p z_2^q\cdot\rho_{a,b}
  =
  -(pb-qa+p-q)\rho_{a-p+1,b-q+1},
\]
with negative-index targets zero.  The excluded \(\rho_{0,0}\) scalar line
is nonzero in local cohomology but is removed because the target is the
dual of \(R/\mathbb C\cdot1\); it is not produced by the action.  Perfect
continuous equivariant pairings are unique up to scalar after the residue
normalization.

Exact obstruction closed: a same-action polynomial \(\Psi\)-module bridge is
impossible.  At the boundary,
\[
  z_1\cdot\widetilde\Psi_{a,0}=0,
  \qquad
  z_1\cdot\rho_{a,0}=-\rho_{a,1}\ne0.
\]

Evidence: Agent 188.

Next action: none for the classical Matlis statement.  Any quantum
principal-part theorem must use the Moyal coadjoint action, not this
classical action alone.

### CL-05. Moyal/Capelli coefficient and scalar-contact surface

Status: computed/proved on the algebraic target.

Closed branch: the raw Weyl/Moyal odd coefficients are
\[
  [f,g]_{\rm raw}^{(2s+1)}
  =
  \frac{\hbar^{2s+1}}{2^{2s}(2s+1)!}P^{2s+1}(f,g),
  \qquad
  [f,g]_{\rm raw}^{(2s)}=0.
\]
Agent 183 verified the sweep through odd orders, including coefficients
\[
  1,\quad 1/24,\quad 1/1920,\quad 1/322560,
  \quad 1/92897280,\quad 1/40874803200.
\]
The Capelli contact relation is
\[
  YX-XY+\hbar N I\equiv0
  \pmod{\mathcal W_N\widehat\mu(\mathfrak{sl}_N)}.
\]
The scalar \(U(1)\) line is removed only after passing to
\(\bar A_\hbar\) and the empty-trace quotient.

Exact obstruction still open: all-bidegree radial/Weyl closure requires the
moment-ideal primitive
\[
  E_{a,b,N}=\sum_{i,j}A^j{}_i(a,b,N)\widehat\mu^i{}_j
\]
or the equivalent free normal-diagram primitive \(K_{a,b}\).  Existing
certificates cover \(K_{4,4}\) and finite checks; they are not a uniform
contracting homotopy.

Evidence: Agent 183.

Next agent needed: Agent 191 radial all-bidegree obstruction/homotopy lane
is live.

### CL-06. Equivariant coordinate CE/PV formulas

Status: proved for the coordinate dg algebra; topology remains open.

Closed branch:
\[
  w(c^{a,b})=w(\theta^{a,b})=-a\epsilon_1-b\epsilon_2,
  \qquad
  w(u_{a,b})=w(O_{a,b})=a\epsilon_1+b\epsilon_2.
\]
Off the self-dual locus the scalarized bracket is
\[
  [f,g]_\Omega=\hbar_\omega
  (\partial_{z_1}f\,\partial_{z_2}g
  -\partial_{z_2}f\,\partial_{z_1}g),
  \qquad w(\hbar_\omega)=\epsilon_1+\epsilon_2.
\]
The CE and PV differentials agree under
\(\Phi_\Omega(c^I)=\theta^I\), \(\Phi_\Omega(u_I)=O_I\):
\[
  d_{{\rm CE},\Omega}c^K
  =
  -\frac12\hbar_\omega C^K_{IJ}c^Ic^J,
  \qquad
  d_{{\rm CE},\Omega}u_K
  =
  \hbar_\omega C^L_{KJ}u_Lc^J.
\]

Open part: mixed \(T_\Omega\)-Cartan/basic coefficient model, weighted
completion continuity, diagonal kernel convergence, residue/Euler
normalization, and resonant self-dual summands.

Evidence: Agent 189.

Next agents needed: Agent 194 theorem-lane integration and Agent 195 Omega
notation/formula audit are live.

### CL-07. Minimal full-equivariant finite-window order-two rows

Status: computed.

Closed branch: in the minimal full-equivariant package, the order-two
non-scalar residual is zero:
\[
  R^{\rm ns}_{2,M}=0,\qquad C_{2,M}=0.
\]
The script reports primitive existence for
`minimal_full_equivariant_order_2_zero`; zero primitives are compatible
under all truncations and the Roos \(\varprojlim^1\) class is zero.

Evidence: Agent 187 and `python3 scripts/finite_window_graph_array.py`.

Next action: do not extrapolate this to larger packages.  Larger packages
need actual row values, seed weights, bracket rows, scalar gates, and
truncation matrices.

### CL-08. Source-transfer firewall

Status: proved as non-transfer.

Closed branch: Ayala-Francis-Tanaka, Costello 1610.04144, Costello
1705.02500, and Costello-Francis-Gwilliam 2602.12412 support external
vocabulary and hypothesis ledgers only.  None constructs this local mixed
HT brane-defect coefficient system, normal-scaling \(T_\Omega\), BV/QME
package, or physical large-\(N\) trace state.

Evidence: Agents 178 and 186.

Next action: any external import requires a matched-conventions morphism
and an obstruction-vector vanishing theorem.

## Active Theorem Surfaces And Exact Obstructions

### LO-01. \(\theta_3\) finite-row obstruction and companion row

Status: exact obstruction in the displayed finite row subcomplex.

Current row complex:
\[
  \mathcal K^0_{\theta_3,M}=0,\qquad
  \mathcal K^1_{\theta_3,M}=\mathbb C\mathsf E_{\theta_3,M},
  \qquad d=0.
\]
The scalar gate is zero:
\[
  S_{\theta_3,M}=0.
\]
The residual is the basis vector:
\[
  R_{\theta_3,M}=\mathsf E_{\theta_3,M}.
\]
The obstruction covector
\[
  \ell_{\theta_3}(\mathsf E_{\theta_3,M})=1
\]
certifies
\[
  [\mathsf E_{\theta_3,M}]\ne0
  \quad\text{in the displayed finite row subcomplex.}
\]

Companion-row interface: if a degree-zero row
\(C_{\theta_3,M}\) is supplied with
\[
  d_{\rm ns,M}C_{\theta_3,M}=-\mathsf E_{\theta_3,M},
\]
then the fixed-window class vanishes.  Tower compatibility then asks
\[
  [\pi_{M,N}C_{\theta_3,M}-C_{\theta_3,N}]
  \in H^0(\mathcal K^\bullet_{\rm ns,N}(I))
\]
to vanish as a Roos \(\varprojlim^1\) class.

Missing evidence: actual renormalized Costello weight
\[
  K^M_{\Theta_3}=W^{R,M}_{\Theta_3,L,w}(B^\Theta_\bullet),
\]
closure
\[
  d_{\rm ns,M}\mathsf E_{\theta_3,M}=0
\]
from the Hom-valued Bianchi identity, and a larger local-functional
primitive or proof of nonexistence.

Deciding evidence: one of:

- a companion \(C_{\theta_3,M}\) with verified differential and compatible
  truncation maps;
- Hom-valued companion rows changing the residual vector and killing the
  covector;
- a proof that no primitive exists in the larger local-functional complex.

Next agent needed: Agent 193 is live on the theta_3 companion-row primitive
search.

### LO-02. Larger finite-window graph packages

Status: theorem surface with exact row-array obstruction.

Exact obstruction: after scalar gates vanish, each finite window must solve
\[
  A^M c=-r^M.
\]
If no solution exists, a left-null covector
\[
  \ell A^M=0,\qquad \ell(r^M)\ne0
\]
certifies a nonzero \(H^1\) class.  If fixed-window solutions exist,
compatibility is the Roos class represented by
\[
  [P^{M,N}c_M-c_N]\in
  H^0(\mathcal K^\bullet_{\rm ns,N}(I)).
\]

Missing data: seed graph sets \(\mathcal G^{\rm gen}_{n,M}\),
renormalized weights \(K^M_\Gamma\), CE-source faces, signs, nonzero
BV/convolution bracket rows, scalar gates, row presentations, and the
\(u,v,q\) truncation matrices.

Deciding evidence: populated row tables plus primitive-search output,
including scalar-gate values and Roos compatibility.

Next agents needed: finite-row package constructor after Agent 193, with
special attention to genuine order-three rows.

### LO-03. Normal \(\Omega\)-background localization

Status: theorem surface; dictionary and weighted finite-window algebra are
installed, full localization proof remains open.

Stable data:
\[
  T_\Omega=
  \mathbb C^*_{\epsilon_s}\times
  \mathbb C^*_{\epsilon_1}\times
  \mathbb C^*_{\epsilon_2},
  \qquad t\text{ fixed},
\]
\[
  V_\Omega=\epsilon_s s\partial_s
  +\epsilon_1z_1\partial_{z_1}
  +\epsilon_2z_2\partial_{z_2},
  \qquad
  Q_\Omega=Q+\iota_{V_\Omega},
  \qquad
  Q_\Omega^2=L_{V_\Omega}.
\]
Finite-window characters are
\[
  \chi^H_{n,a,b}=n\epsilon_s+a\epsilon_1+b\epsilon_2,
  \qquad
  \chi^\vee_{n,a,b}=n\epsilon_s-a\epsilon_1-b\epsilon_2.
\]

Exact obstructions:

- resonant summands \(\chi=0\), which remain in
  \(\operatorname{pr}_{\chi=0}\);
- missing normal Koszul numerator signs in the mixed de Rham/Dolbeault
  category;
- missing \(q\)-moderate small-denominator bounds for all-window analytic
  use;
- normalization fork
  \[
    \nu_\Omega^{\rm res}=1,\qquad
    \nu_\Omega^{\rm Eu}=
    \sigma_s(\epsilon_s\epsilon_1\epsilon_2)^{-1}.
  \]

Deciding evidence: a mixed Cartan/basic coefficient model, a localized
normal retract
\[
  Q_\Omega h_\Omega+h_\Omega Q_\Omega=\operatorname{id}-j_L\pi_L,
\]
resonance computation for chosen specializations, and a residue/Euler
comparison with fixed sign \(\sigma_s\).

Next agents needed: Agent 195 Omega consistency audit, then a normal
Cartan/contraction proof lane.

### LO-04. Equivariant weighted kernels and Costello boundary

Status: theorem surface with exact obstruction vector.

Stable finite-window kernel:
\[
  C_{\Omega,w}^{N,M}
  =
  \sum_{\alpha\in\mathsf A_{N,M}}
  e_{\alpha,w}\otimes e^\alpha_{w^{-1}}.
\]
If
\[
  Q_\Omega k^{\rm Kos}_\alpha+k^{\rm Kos}_\alpha Q_\Omega
  =
  \chi_\alpha\,\operatorname{id}_\alpha,
\]
then the localized normal kernel is
\[
  H_{\Omega,w}^{N,M}
  =
  \sum_{\alpha\in\mathsf A^{\rm mov}_{N,M}}
  \chi_\alpha^{-1}e_{\alpha,w}\otimes e^\alpha_{w^{-1}}
  \otimes k^{\rm Kos}_\alpha.
\]

Exact QME obstruction vector:
\[
  \operatorname{Ob}^{\rm QME}_{\Omega,w}
  =
  \left(
    \mathcal R_{\Omega},
    \operatorname{ob}_{\Omega,\nu},
    \{\mathfrak s_{n,\Omega}\}_{n\ge1},
    \{(([\mathfrak o^{\rm ns}_{n,\Omega,M}])_M,
      \lambda_{n,\Omega})\}_{n\ge1}
  \right).
\]

Deciding evidence: normal numerator signs, nonresonance or \(q\)-moderate
bounds, global normalization choice, and computed scalar gates,
non-scalar \(H^1\) classes, and Milnor primitive-compatibility classes.

Next agents needed: equivariant graph/QME package constructor after the
finite-row and Omega consistency lanes close.

### LO-05. Equivariant brane-line current brackets

Status: provisional after-context; Agent 192 report exists but launch log
still marks Agent 192 live.

Provisional stable algebraic bracket:
\[
\begin{aligned}
  \{B_{p,q}(a),B_{r,s}(b)\}_{\Omega}
    &=
    \hbar_\omega(ps-qr)B_{p+r-1,q+s-1}(ab),\\
  \{B_{p,q}(a),\Theta_{r,s}(B)\}_{\Omega}
    &=
    -\hbar_\omega(ps-qr+p-q)
    \Theta_{r-p+1,s-q+1}(aB),\\
  \{\Theta_{r,s}(B),\Theta_{u,v}(C)\}_{\Omega}
    &=0 .
\end{aligned}
\]
Here \(a\in C_c^\infty(I)\) and \(B\in\mathcal D'_c(I)\) live on the fixed
brane line and have weight zero.

Boundary: this is an algebraic current theorem.  It does not permit
arbitrary distributional labels in Costello graph products.

Deciding evidence: closure of Agent 192 in the launch log and integration
owner verification.  Until then, use this row only as a compatibility check
for LO-06 and LO-10.

Next agent needed: Agent 192 closure or integration-owner recheck.

### LO-06. Controlled \(\mathbb C\times\mathbb R\) reduction

Status: theorem surface; retained-\(z_2\) branch only.

Stable target:
\[
  \mathfrak h_{\rm red}
  =
  \mathbb C[[z_1]][[z_2]]/\mathbb C\cdot1,
  \qquad
  \mathcal P_{\rm red}
  =
  \operatorname{Ann}_{\rm res}(\mathbb C\cdot1).
\]
The bracket is
\[
  \{f,g\}_{\rm red}
  =
  \partial_{z_1}f\,\partial_{z_2}g
  -
  \partial_{z_2}f\,\partial_{z_1}g.
\]

Exact obstruction: setting \(z_2=0\) kills the Hamiltonian bracket.  Literal
residue along \(z_2\) keeping only \(b=0\) principal parts is not stable
because
\[
  z_1\cdot\rho_{a,0}=-\rho_{a,1}.
\]
The scalar anomaly also survives:
\[
  \operatorname{Ob}^{\rm red}_{\rm sc}
  =
  \hbar N\,\omega(f,g)\int a(t)b(t)\gamma_{\mathbf 1}(t)\,dt.
\]

Deciding evidence: a theorem lane defining \(\pi\), \(s\)-contraction,
retained \(z_2\) mode/principal-part datum, brane image, reduced BV pairing,
bracket, anomaly homotopy, and Moyal compatibility.

Next agent needed: controlled-reduction theorem constructor; Agent 194 may
perform theorem-lane integration but must not erase the retained-\(z_2\)
condition.

### LO-07. Reduced Dirac BRST/Zhu bridge

Status: theorem surface conditional on LO-06.

Constructed reduced object:
\[
  j_{\rm BRST}
  =
  \operatorname{Tr}(c[Z_1,Z_2])
  +\frac12\operatorname{Tr}(b[c,c]),
  \qquad
  Q_{\rm BRST}=\operatorname{Res}j_{\rm BRST}(z)\,dz.
\]
The differential is
\[
  QZ_a=[c,Z_a],\qquad Qc=\frac12[c,c],\qquad
  Qb=[Z_1,Z_2]+[b,c],
\]
and Agent 182 supplies the Jacobi/equivariance check for
\(Q_{\rm BRST}^2=0\) inside the reduced vertex-algebra model.

Zhu target:
\[
  QB=YX-XY+\hbar N I+[B,C],
\]
so degree-zero Zhu cohomology gives the BRST quantum Hamiltonian reduction
with moment relation
\[
  YX-XY+\hbar N I=0.
\]

Exact obstruction: this is false as native \(\mathbb C^2\) geometry.  It
requires LO-06, OPE normalization, conformal weights, zero-mode convention,
Capelli shift, and a conditional Hochschild/HKR/CE-PV comparison chain.

Deciding evidence: integrated controlled reduction, reduced OPE theorem,
Zhu computation, anomaly matching, and continuous HKR hypotheses.

Next agent needed: reduced BRST/Zhu theorem constructor after LO-06
integration.

### LO-08. Stratified factorization algebra on \((X,L)\)

Status: theorem surface with named obstruction vector.

Target data:
\[
  \mathcal F^{\rm str}_{\Omega,N}\colon
  \operatorname{Disk}^{\rm str}_{X,L}\to \operatorname{Alg},
\]
including bulk disks, brane intervals, mixed collars, a brane module
\(\mathcal M_{\Omega,N}\), and centrality homotopies
\[
  H^{\rm prod}_{x,a},\qquad H^{P_0}_{x,a}.
\]

Exact obstruction:
\[
  \operatorname{Ob}_{\rm str,\Omega,N}
  =
  (\text{descent defects},
   \text{collar-module defects},
   \text{centrality defects},
   \text{QME curvature defects}).
\]
A reduced interval current target is not a stratified factorization algebra
on \((X,L)\).

Deciding evidence: completed stratified disk algebra, collar module,
descent proof, and brane-defect QME centrality homotopies.

Next agent needed: stratified mixed HT coefficient/brane-module constructor.

### LO-09. Stratified trace and physical large-\(N\) state

Status: theorem surface with exact physical obstruction vector.

Physical branch:
\[
  A^q_{N,\Omega}
  =
  \operatorname{Weyl}_{\hbar_N}(\operatorname{Mat}_N^2)
  /\!\!/_{\hbar_N}GL_N,
  \qquad
  YX-XY+\hbar_N N I=0,
\]
with \(\lambda=N\hbar_N\).  A physical trace requires a continuous cyclic
state
\[
  \omega_{N,\Omega}\colon A^q_{N,\Omega,\lambda}\to R_\Omega
\]
and cumulants
\[
  \langle F_1,\ldots,F_k\rangle^c_{N,\Omega}
  =
  [t_1\cdots t_k]\log\omega_{N,\Omega}
  \left(\exp\left(\sum_i t_iF_i\right)\right).
\]
The expected asymptotic statement has form
\[
  \langle O_{a_1,b_1}^{(N)},\ldots,O_{a_k,b_k}^{(N)}
  \rangle^c_{N,\Omega}
  \sim
  \sum_{g\ge0}N^{2-2g-k}
  F^\Omega_{g;k}((a_1,b_1),\ldots,(a_k,b_k)).
\]

Exact obstruction:
\[
  \operatorname{Ob}_{\Omega,\rm phys}
  =
  (
    \operatorname{ob}_{\Omega,\rm Cartan},
    \operatorname{ob}_{\Omega,\rm contr},
    \operatorname{ob}_{\rm red},
    \operatorname{ob}_{\rm state},
    \operatorname{ob}_{\rm norm},
    \operatorname{ob}^{\rm sc}_{\rm QME},
    \operatorname{ob}^{\rm ns}_{\rm QME},
    \operatorname{ob}_{\rm cent},
    \operatorname{ob}_{\rm Ward},
    \operatorname{ob}_{\rm cum},
    \operatorname{ob}_{\rm asymp},
    \operatorname{ob}_{\rm src}
  ).
\]

Deciding evidence: \(D_{N,\Omega}^\vee\omega_{N,\Omega}=0\), moment-map
Ward identities, \(Q_\Omega\)-Ward identities, curvature Ward identities,
normalization, trace-test topology, and coefficientwise \(N^{-2}\)
asymptotics.

Next agent needed: physical trace-state construction only after LO-03,
LO-04, LO-08, and source-hypothesis checks close.

### LO-10. Costello graph/QME and brane-defect kernel

Status: theorem surface with scalar-projection and non-scalar obstruction
classes.

Normal \(\Omega\) supplies weights and candidate contractions; it does not
solve the QME.  The finite-window kernel datum must include an equivariant
propagator
\[
  [Q_\Omega,P^{w,M}_{\epsilon,L,\Omega}]
  =
  K^{w,M}_{\epsilon,\Omega}-K^{w,M}_{L,\Omega},
  \qquad
  [L_{V_\Omega},P^{w,M}_{\epsilon,L,\Omega}]=0.
\]
Scalar projection is controlled by
\[
  \delta^{(0)}_{\Omega,\sigma,M}
  =
  d_{{\rm CE},\Omega}\sigma_{{\rm sc},\Omega,M}
  -
  \sigma_{{\rm sc},\Omega,M}d_{\operatorname{gr},\Omega},
\]
and higher classes
\[
  \mathfrak o^{(r)}_{\Omega,\sigma,M}
  \in
  H^1\left(
    \operatorname{Hom}_{T_\Omega,-r}
    (\operatorname{gr}_F\mathfrak Q^\bullet_{\mathcal G,\Omega,M},
     S^\bullet_{\Omega,M})
  \right).
\]
Only after these vanish does
\[
  \mathcal K^\bullet_{{\rm ns},\Omega,M}
  =
  \ker\widehat\sigma_{{\rm sc},\Omega,M}
\]
become the non-scalar obstruction complex.

Order \(n\) residual:
\[
\begin{aligned}
  R^{\rm ns}_{n,\Omega,M}
    =
  [\hbar^n]\bigl(
    &\operatorname{Curv}_{\mathbf K,\Omega,M}
      (\kappa^M_{\mathcal G,\Omega,w,I})
    +d_{M,\Omega}C_{<n,\Omega,M} \\
    &+\frac12\{C_{<n,\Omega,M},C_{<n,\Omega,M}\}_{\hbar,M,\Omega}
  \bigr).
\end{aligned}
\]
Scalar gate:
\[
  \mathfrak s_{n,\Omega,M}
  =
  \widehat\sigma_{{\rm sc},\Omega,M}
  (R^{\rm ns}_{n,\Omega,M}).
\]
Non-scalar class:
\[
  \mathfrak o^{\rm ns}_{n,\Omega,M}
  =
  [R^{\rm ns}_{n,\Omega,M}]
  \in H^1(\mathcal K^\bullet_{{\rm ns},\Omega,M}).
\]
Tower compatibility includes \(\lambda_{n,\Omega}\in\varprojlim^1H^0\).

Deciding evidence: equivariant propagator, local counterterms,
normalization, scalar-projection chain-map lift, scalar gates,
non-scalar \(H^1\) computations, \(\varprojlim^1H^0\) compatibility, and
invariant \(Q_\Omega\)-centrality primitives.

Next agents needed: Costello equivariant graph/QME constructor after
Agents 193 and 195 close.

### LO-11. Current-compatible graph products for distributional labels

Status: exact obstruction / false generalization.

Closed algebraic current branch permits arbitrary \(B\in\mathcal D'_c(I)\)
for coefficient-current brackets because only multiplication by a smooth
function is used.  Costello graph products do not permit arbitrary compactly
supported distributions without microlocal conditions.

Exact obstruction: coincident singular labels such as
\(B_1=B_2=\delta_{t_0}\) can fail Hormander transversality against a
collision diagonal.

Deciding evidence: a graphwise microlocal theorem giving wavefront
transversality, finite scaling degree, diagonal-extension ambiguity, and
counterterm compatibility; otherwise graph theorems stay restricted to
regular densities or graphwise wavefront-admissible tuples.

Next agent needed: microlocal current/Costello graph lane.

### LO-12. Integration and build gate

Status: verification gate.

Exact obstruction: stale auxiliary files and concurrent edits can produce
false TeX failures.  This is not a mathematical obstruction.

Deciding evidence: after live agents 191--196 and any integration lanes
close, run the Agent 190 verification package:

```bash
git diff --check -- abstract.tex main.tex theorem-lanes.tex local-dictionary.tex open-obligations.tex appendix-unreduced-bv-qme.tex appendix-radial-parts-moyal.tex tate-T1-weighted-completion.tex
rg -n -F -e "curve vertex algebra" -e "Zhu" -e "physical large" -e "protected trace" -e "Costello" -e "CFG" main.tex theorem-lanes.tex local-dictionary.tex open-obligations.tex appendix-unreduced-bv-qme.tex
rg -n -F -e "Q_\\Omega" -e "T_\\Omega" -e "hbar_\\omega" -e "e_{T_\\Omega}" local-dictionary.tex appendix-unreduced-bv-qme.tex tate-T1-weighted-completion.tex
rg -n -F -e "YX-XY+\\hbar N I" -e "P^3(f,g)/24" -e "Capelli" main.tex theorem-lanes.tex appendix-radial-parts-moyal.tex
make pdf
```

Next agent needed: integration owner after all live lanes close.

## Dependency Order For Next Work

1. Close Agent 193's theta_3 companion-row search.  It decides whether the
   current finite obstruction is healed by \(C_{\theta_3}\) or survives in a
   larger complex.
2. Close Agent 191 radial all-bidegree search.  It decides whether
   Moyal/Capelli remains only finite/casewise or gets an all-bidegree
   homotopy.
3. Close Agent 195 Omega consistency audit.  Then integrate the refined
   bracket, weights, residue/Euler fork, and self-dual branch without
   notation drift.
4. Integrate controlled \(C\times R\) reduction before any BRST/Zhu theorem.
5. Build the mixed Cartan/basic normal-localization proof and weighted
   kernel proof before QME or trace claims.
6. Build stratified brane factorization before trace-state or protected
   trace language.
7. Construct the equivariant Costello graph package and compute the scalar
   gates, non-scalar classes, theta_3 companions, and Milnor classes.
8. Only after those closures, attempt physical large-\(N\) state,
   Ward-identity, and cumulant-asymptotic theorems.
