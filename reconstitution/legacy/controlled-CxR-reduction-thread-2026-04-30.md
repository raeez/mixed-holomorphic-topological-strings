# Controlled CxR Reduction Thread, 2026-04-30

Scope: Agent 181.  Writable surface: this file and
`reconstitution/swarm-2026-04-30-agent-181-controlled-CxR-reduction-0957.md`.
No manuscript file is edited here.

## Verdict

There is a stable theorem surface only for a mode-retaining reduction.
The naive reduction
\[
  \mathbb R_t\times\mathbb R_s\times\mathbb C_{z_1}\times\mathbb C_{z_2}
  \longrightarrow
  \mathbb R_t\times\mathbb C_{z_1}
\]
does not produce a one-variable Hamiltonian algebra
\(\mathbb C[[z_1]]/\mathbb C\).  That quotient kills the Hamiltonian
bracket, the scalar anomaly, the principal-part module, and the
Weyl/Moyal relation.  The controlled reduction must keep the \(z_2\)
formal modes, or equivalently the \(z_2\)-principal-part coefficient
system.

The reduced coefficient algebra is therefore
\[
  \mathfrak h_{\mathrm{red}}
  =
  \mathbb C[[z_1]][[z_2]]/\mathbb C\cdot 1
  \cong
  \mathbb C[[z_1,z_2]]/\mathbb C\cdot 1,
\]
now read as a coefficient system over the reduced mixed space
\[
  Y=\mathbb R_t\times\mathbb C_{z_1}.
\]
Its continuous cotangent module is still the Matlis principal-part module
\[
  \mathcal P_{\mathrm{red}}
  =
  \operatorname{Ann}_{\mathrm{res}}(\mathbb C\cdot1)
  \subset
  H^2_{(z_1,z_2)}(\mathbb C[[z_1,z_2]])\,dz_1dz_2,
\]
with basis
\[
  \rho_{a,b}=z_1^{-a-1}z_2^{-b-1}dz_1dz_2,\qquad a+b>0.
\]

This is a \(C\times R\) shadow of the native
\(\mathbb R^2_{\mathrm{top}}\times\mathbb C^2_{\mathrm{hol}}\) theory,
not a new native curve theory.

## Anchors Read

- `CLAUDE.md`: native geometry and the controlled-reduction firewall.
- `AGENTS.md`: no direct import of Volume II curve chiral algebra.
- `reconstitution/critique-refresh-2026-04-30-0957-ingestion-and-swarm-plan.md`:
  theorem surface 10, controlled \(C\times R\) reduction retaining
  \(z_2\)-coefficients.
- `reconstitution/local-theorem-obligations-2026-04-30.md`: local theorem
  obligations and current scalar/non-scalar QME residuals.
- `reconstitution/chiral-algebra-construction-thread-2026-04-30.md`:
  constructed native \(\mathbb C^2\) holomorphic factorization algebra
  and vertex/OPE boundary.
- `main.tex:934-1228`: local holomorphic/mixed factorization definitions
  and the constructed Hamiltonian CE/factorization object.
- `main.tex:2867-2960`, `main.tex:2962-2998`, `main.tex:3240-3377`:
  defect-current kernel, interval currents, compact-support interval
  contraction, and smeared current center.
- `main.tex:7230-7286`, `main.tex:7336-7377`: scalar anomaly and
  Weyl/Moyal convention.
- `theorem-lanes.tex:227-675`, `theorem-lanes.tex:1613-1818`,
  `theorem-lanes.tex:1823-2005`: local chiral/factorization taxonomy,
  principal parts, current brackets, and quantum coefficient surface.
- `local-dictionary.tex:13-124`, `local-dictionary.tex:170-380`,
  `local-dictionary.tex:377-625`: local unimodularity, chiral taxonomy,
  and normal \(\Omega\)-background theorem surface.
- `appendix-factorization-current-conventions.tex:122-188`,
  `appendix-factorization-current-conventions.tex:370-431`: local
  unimodular current input and monomial current brackets.
- Vol II `chapters/theory/sc_chtop_heptagon.tex:140-285`: target
  \(SC^{\mathrm{ch},\mathrm{top}}\) shape.  It is used here only as an
  interface to be reached after reduction, not as evidence that the
  reduction already exists.

## The Projection Datum

Let
\[
  X=\mathbb R_t\times\mathbb R_s\times\mathbb C_{z_1}\times\mathbb C_{z_2},
  \qquad
  Y=\mathbb R_t\times\mathbb C_{z_1},
\]
and
\[
  \pi:X\to Y,\qquad
  \pi(t,s;z_1,z_2)=(t;z_1).
\]
For product opens
\[
  I\subset\mathbb R_t,\quad J\subset\mathbb R_s,\quad
  D_1\subset\mathbb C_{z_1},\quad D_2\subset\mathbb C_{z_2},
\]
write \(V=I\times D_1\) and \(U=I\times J\times D_1\times D_2\).
The unreduced mixed input is
\[
  \Omega_c^\bullet(I)\widehat\otimes\Omega_c^\bullet(J)
  \widehat\otimes
  \Omega_c^{0,\bullet}(D_1)\widehat\otimes
  \Omega_c^{0,\bullet}(D_2)
  \widehat\otimes
  (\mathfrak h\ltimes\mathcal P[1]).
\]
The controlled pushforward is not the plain pullback of functions along
\(\pi\).  It is a choice of fiber integration/contraction data
\[
  \mathsf P_{\pi}
  =
  (p_s,i_s,K_s)\otimes
  \mathsf Z_{z_2}
\]
followed by the reinterpretation
\[
  \mathfrak h\cong\mathfrak h_{\mathrm{red}},
  \qquad
  \mathcal P\cong\mathcal P_{\mathrm{red}},
\]
where \(z_2\) is a retained coefficient variable over \(Y\).

## Topological \(s\)-Contraction

For a nonempty oriented interval \(J\subset\mathbb R_s\), choose
\(\lambda_J(s)ds\in\Omega_c^1(J)\) with
\[
  \int_J\lambda_J(s)\,ds=1.
\]
Define
\[
  p_s:\Omega_c^\bullet(J)\to\mathbb C[-1],
  \qquad
  p_s(\alpha)=\int_J\alpha,
\]
zero on degree \(0\), and
\[
  i_s:\mathbb C[-1]\to\Omega_c^\bullet(J),
  \qquad
  i_s(1)=\lambda_J(s)ds.
\]
For \(\alpha=f(s)ds\), set
\[
  K_s(\alpha)(s)=
  \int_{-\infty}^{s}
  \left(f(u)-\lambda_J(u)\int_J f(v)\,dv\right)du,
  \qquad
  K_s(\varphi)=0,\quad \varphi\in\Omega_c^0(J).
\]
Then
\[
  d_sK_s+K_sd_s=\operatorname{id}-i_sp_s.
\]
On \(I\times J\) the tensor homotopy is
\[
  H_s(\eta_t\otimes\alpha_s)
  =
  (-1)^{|\eta_t|}\eta_t\otimes K_s\alpha_s,
\]
so that
\[
  (d_t+d_s)H_s+H_s(d_t+d_s)=\operatorname{id}-j_sp_s
\]
with the ordinary Koszul sign.  The surviving line is the compact-support
cohomology line \(H_c^1(J)\cong\mathbb C[-1]\).  There is no acyclicity
claim.

## Holomorphic \(z_2\)-Reduction

There are two different operations.  Confusing them is the main failure
mode.

### Mode-Retaining Branch

The algebraic coefficient map is the identity on holomorphic \(z_2\)
modes:
\[
  \operatorname{zm}_{z_2}:
  \mathbb C[[z_1,z_2]]/\mathbb C
  \longrightarrow
  \mathbb C[[z_1]][[z_2]]/\mathbb C,
\]
\[
  \sum_{a,b\ge0}c_{a,b}z_1^az_2^b
  \longmapsto
  \sum_{a,b\ge0}c_{a,b}z_1^az_2^b.
\]
The point is not to set \(z_2=0\).  The point is to make \(z_2\) a
formal coefficient over the reduced base \(Y\).

The analytic theorem must still construct a Dolbeault fiber datum
\[
  \mathsf Z_{z_2}=(p_{z_2},i_{z_2},K_{z_2})
\]
for the \(\bar\partial_{z_2}\)-complex, with
\[
  \bar\partial_{z_2}K_{z_2}+K_{z_2}\bar\partial_{z_2}
  =
  \operatorname{id}-i_{z_2}p_{z_2},
\]
support control, compatibility with extension by zero, and compatibility
with binary and ternary factorization products.  This is not presently
proved in the manuscript.

### Literal Residue Branch

The literal one-variable residue
\[
  \operatorname{Res}_{z_2}
  (z_2^{-b-1}dz_2)=\delta_{b,0}
\]
is not a stable quotient of the cotangent module.  Indeed
\[
  z_1\cdot\rho_{a,0}=-(0+1)\rho_{a,1},
\]
so projecting to the \(b=0\) residue line kills a vector that is produced
by the Hamiltonian action.  Thus a theorem that keeps only \(b=0\) is not
\(\mathfrak h_{\mathrm{red}}\)-equivariant.

The admissible residue operation is the coefficient pairing
\[
  \operatorname{Res}_{z_2}(z_2^n\,z_2^{-b-1}dz_2)=\delta_{n,b},
\]
used inside the full two-index pairing
\[
  \langle \rho_{a,b},z_1^mz_2^n\rangle
  =
  \delta_{a,m}\delta_{b,n}.
\]
This keeps the principal-part coefficient system.  It does not collapse
it.

## Reduced Lie Algebra and Bracket

The reduced Hamiltonian Lie algebra is
\[
  \mathfrak h_{\mathrm{red}}
  =
  \mathbb C[[z_1]][[z_2]]/\mathbb C.
\]
Its bracket is still the two-variable Hamiltonian bracket
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
If \(z_2\)-dependence is killed, this bracket is zero.  That quotient
cannot carry the Hamiltonian BF, scalar anomaly, or Moyal theorem.

The reduced cotangent action remains
\[
  z_1^pz_2^q\cdot\rho_{i,j}
  =
  -(pj-qi+p-q)\rho_{i-p+1,j-q+1},
\]
with negative-index targets equal to zero.  This is the same Matlis
coadjoint action, now read as a coefficient action over \(Y\).

The reduced shifted cotangent algebra is
\[
  \mathfrak g_{\mathrm{red}}
  =
  \mathfrak h_{\mathrm{red}}\ltimes
  \mathcal P_{\mathrm{red}}[1].
\]
The CE/PV generator rule is unchanged:
\[
  c_{a,b}\mapsto\theta_{a,b},
  \qquad
  u_{a,b}\mapsto O_{a,b}.
\]
Only the habitat changes: \(z_1\) is the holomorphic coordinate of the
reduced mixed space, while \(z_2\) is retained in the coefficient
system.

## Reduced BV Pairing

At the formal coefficient level the reduced pairing is the same residue
evaluation
\[
  \langle \rho_{a,b},z_1^mz_2^n\rangle_{\mathrm{red}}
  =
  \delta_{a,m}\delta_{b,n}.
\]
On reduced mixed fields it has the schematic form
\[
  \int_{I\times D_1}
  \langle \beta_{\mathrm{red}},\alpha_{\mathrm{red}}\rangle_{z_2\text{-coeff}}
  \,dt\,dz_1,
\]
where the \(z_2\)-coefficient pairing is the two-index residue pairing
above.  The exact theorem must specify whether the orientation line
coming from the \(s\)-compact-support contraction and the
\(\bar\partial_{z_2}\) or residue pushforward is absorbed into the field
degrees or left explicit.  This is a degree and sign obligation, not
notation.

## Brane Image

The original brane is
\[
  L=\mathbb R_t\times\{s=z_1=z_2=0\}\subset X.
\]
Its image is
\[
  L_{\mathrm{red}}
  =
  \pi(L)
  =
  \mathbb R_t\times\{z_1=0\}\subset Y.
\]
The image is a line defect in \(Y=\mathbb R_t\times\mathbb C_{z_1}\).
It is not a brane with only one normal matrix.  The \(z_2\) normal
coordinate survives as coefficient data and, at finite \(N\), as the
second matrix variable.

The reduced finite-\(N\) evaluation map is
\[
  \operatorname{ev}_{N}^{\mathrm{red}}(f)
  =
  \overline{\operatorname{Tr}f(X,Y)},
  \qquad X=\phi_1,\quad Y=\phi_2,
\]
for \(f\in\bar A_\hbar\) or \(f\in\mathfrak h_{\mathrm{red}}\) in the
classical limit.  The support-local current is
\[
  B_f(a)
  =
  \int_I a(t)\,
  \overline{\operatorname{Tr}f(X(t),Y(t))}\,dt.
\]
The principal-part current is still
\[
  \Theta_\rho(B),\qquad
  B\in\mathcal D'_c(I),\quad \rho\in\mathcal P_{\mathrm{red}}.
\]
The reduced current brackets are
\[
  \{B_f(a),B_g(b)\}=B_{\{f,g\}_{\mathrm{red}}}(ab),
\]
\[
  \{B_f(a),\Theta_\rho(B)\}
  =
  \Theta_{f\cdot\rho}(aB),
  \qquad
  \{\Theta_\rho(B),\Theta_\sigma(C)\}=0.
\]

## Scalar Anomaly

The scalar anomaly survives the controlled reduction.  Since
\[
  \{z_1,z_2\}=1,
\]
the scalar-reduced cocycle
\[
  \omega(f,g)=[\{f,g\}]_0
\]
is still present.  On the reduced line-current surface its representative
is
\[
  \operatorname{Ob}_{\mathrm{sc}}^{\mathrm{red}}
  (\gamma_{\mathbf 1};a,f;b,g)
  =
  \hbar N\,\omega(f,g)
  \int_{\mathbb R_t} a(t)b(t)\gamma_{\mathbf 1}(t)\,dt,
\]
with the \(s\)-fiber normalized by \(p_s(\lambda_Jds)=1\).  No
\(\epsilon_s\epsilon_1\epsilon_2\) Euler factor is inserted unless a
separate residue-versus-Euler normalization theorem supplies it.

Therefore the same alternatives remain:

1. work unreduced before quotienting constants and use
   \(\eta(f)=-[f]_0\);
2. replace the source by the central-character branch
   \(\chi_N(f)=N[f]_0\);
3. use the balanced supertrace branch;
4. construct an external brane-defect or closed-exchange contribution
   with scalar class \(-\hbar N[\bar c]\).

The controlled \(C\times R\) reduction does not itself cancel the scalar
class.

## Moyal Compatibility

The Weyl/Moyal product remains the two-variable product
\[
  f*g
  =
  m\circ
  \exp\left(
    \frac{\hbar}{2}
    (\partial_{z_1}\otimes\partial_{z_2}
    -\partial_{z_2}\otimes\partial_{z_1})
  \right)(f\otimes g).
\]
It is well-defined on the retained coefficient algebra
\(\mathbb C[[z_1]][[z_2]]\) in finite polynomial windows and in the
weighted/completed habitats already used by the manuscript.

If \(z_2\) is killed, this product becomes commutative on the reduced
one-variable algebra and cannot match the matrix Weyl relation
\[
  [X^i{}_j,Y^k{}_\ell]
  =
  \hbar\,\delta^i_\ell\delta^k_j.
\]
Thus Moyal compatibility forces the retained \(z_2\)-mode or
principal-part branch.

In the equivariant refinement, the weights are
\[
  w(z_1)=\epsilon_1,\qquad w(z_2)=\epsilon_2,\qquad
  w(\hbar)=\epsilon_1+\epsilon_2.
\]
On the self-dual locus \(\epsilon_1+\epsilon_2=0\), the Poisson bracket
is scalar.  Off that locus the scalar bracket is
\[
  [f,g]_\Omega=\hbar_\omega\{f,g\},
  \qquad w(\hbar_\omega)=\epsilon_1+\epsilon_2,
\]
or else the bracket is valued in the inverse symplectic-character line.

## Optional Dirac BRST Curve Algebra

After the controlled reduction and a further factorization-to-vertex
comparison along the \(z_1\)-line, one may target the Dirac BRST vertex
surface with fields \(Z_1,Z_2,b,c\), singular products
\[
  Z_1{}^i{}_j(z)Z_2{}^k{}_\ell(w)
  \sim
  \frac{\hbar\,\delta^i_\ell\delta^k_j}{z-w},
  \qquad
  b^i{}_j(z)c^k{}_\ell(w)
  \sim
  \frac{\delta^i_\ell\delta^k_j}{z-w},
\]
and BRST current
\[
  j_{\mathrm{BRST}}
  =
  \operatorname{Tr}(c[Z_1,Z_2])
  +\frac12\operatorname{Tr}(b[c,c]).
\]
This is not part of the stable core yet.  It requires:

1. the controlled \(\pi_!\) reduction above;
2. a factorization-to-vertex theorem on the \(z_1\)-line;
3. a proof that \(Q_{\mathrm{BRST}}^2=0\), including the scalar anomaly
   branch used;
4. a zero-mode or Zhu map
   \[
     \zeta_{\hbar}:(\bar A_\hbar,*)\to\operatorname{Zhu}(V_{\mathrm{red}});
   \]
5. compatibility of zero modes with
   \(\operatorname{ad}^{\vee}_{f,\hbar}\) on principal parts.

## Attack Ledger

```yaml
- id: A181-01
  severity: 1
  status: healed
  lens: coefficient algebra
  claim: pi_* gives C[[z1]]/C as the reduced Hamiltonian algebra.
  broken_step: setting z2=0 kills the Hamiltonian bracket.
  evidence_type: counterexample
  evidence_ref: "{z1,z2}=1 before scalar reduction; one-variable bracket is zero."
  minimal_heal: retain h_red=C[[z1]][[z2]]/C as coefficient algebra over C_z1.
  residual: analytic Dolbeault fiber contraction still must be built.

- id: A181-02
  severity: 2
  status: healed
  lens: compact-support topology
  claim: the s-direction is acyclic and can be discarded.
  broken_step: Omega_c^*(J) has H_c^1(J)=C[-1].
  evidence_type: proof_gap
  evidence_ref: compact-support interval contraction in main.tex:2962-2998.
  minimal_heal: use p_s, i_s, K_s and keep the compact-support orientation line.
  residual: global naturality for arbitrary stratified intervals remains a theorem datum.

- id: A181-03
  severity: 1
  status: healed
  lens: principal parts
  claim: residue along z2 keeps only b=0 principal parts.
  broken_step: the b=0 line is not stable under the Hamiltonian action.
  evidence_type: counterexample
  evidence_ref: z1.rho_{a,0}=-(1)rho_{a,1}.
  minimal_heal: keep the full two-index principal-part coefficient system.
  residual: choose zero-mode versus residue-pairing realization in analytic TeX.

- id: A181-04
  severity: 1
  status: healed
  lens: brane image
  claim: the projected brane has one normal matrix.
  broken_step: the second normal coordinate is retained as coefficient data and is needed for Moyal.
  evidence_type: counterexample
  evidence_ref: [X,Y]=hbar in the matrix Weyl algebra.
  minimal_heal: L_red=R_t x {z1=0} with X=phi1 and Y=phi2 retained.
  residual: collar/stratified module for this line defect is still open.

- id: A181-05
  severity: 1
  status: healed
  lens: scalar anomaly
  claim: the CxR reduction removes the scalar anomaly.
  broken_step: omega(f,g)=[{f,g}]_0 survives because {z1,z2}=1.
  evidence_type: proof_gap
  evidence_ref: main.tex:7230-7286.
  minimal_heal: carry the same scalar anomaly alternatives into the reduced theorem.
  residual: pick and prove one anomaly branch for a BRST/Zhu theorem.

- id: A181-06
  severity: 1
  status: healed
  lens: Moyal compatibility
  claim: a one-variable reduced algebra can match the finite-N Weyl algebra.
  broken_step: the Moyal bivector needs partial_z2.
  evidence_type: counterexample
  evidence_ref: f*g=m exp(hbar P/2), P=partial_z1 tensor partial_z2 - partial_z2 tensor partial_z1.
  minimal_heal: use the retained z2 coefficient algebra and weighted completed habitats.
  residual: all-N radial/Capelli normalization remains the existing conditional branch.

- id: A181-07
  severity: 2
  status: non_core
  lens: Volume II interface
  claim: Vol II SCchtop directly supplies the CxR reduction.
  broken_step: Vol II describes the target chiral-topological apparatus; it does not construct pi_! for this local C2 Hamiltonian BF model.
  evidence_type: unsupported
  evidence_ref: repo firewall and theorem-lanes.tex:494-503.
  minimal_heal: treat SCchtop/BRST/Zhu as target interface after the reduction theorem.
  residual: factorization-to-vertex and Zhu comparison must be built.
```

## Theorem-Surface Plan

**Theorem surface: controlled \(C\times R\) reduction with retained
\(z_2\)-coefficients.**

Hypotheses:

1. \(X=\mathbb R_t\times\mathbb R_s\times\mathbb C^2_{z_1,z_2}\),
   \(Y=\mathbb R_t\times\mathbb C_{z_1}\), and
   \(\pi(t,s;z_1,z_2)=(t;z_1)\).
2. A compact-support de Rham contraction
   \((p_s,i_s,K_s)\) of the \(s\)-fiber, normalized by
   \(\int_J\lambda_Jds=1\).
3. A mode-retaining holomorphic fiber datum
   \(\mathsf Z_{z_2}\), or an explicitly equivalent residue-pairing
   model, which keeps all \(z_2\) modes/principal parts.
4. The coefficient system
   \[
     \mathfrak g_{\mathrm{red}}
     =
     (\mathbb C[[z_1]][[z_2]]/\mathbb C)
     \ltimes
     \mathcal P_{\mathrm{red}}[1].
   \]
5. A declared scalar-anomaly branch: unreduced central character,
   balanced supertrace, or an explicitly constructed external
   cancellation.
6. For quantum statements, the weighted/completed Moyal habitat and the
   Capelli/Weyl normalization used in the current manuscript.

Conclusions to prove:

1. The pushed-forward mixed factorization object on
   \(Y=\mathbb R_t\times\mathbb C_{z_1}\) has local input
   \[
     \Omega_c^\bullet(I)\widehat\otimes
     \Omega_c^{0,\bullet}(D_1)\widehat\otimes
     \mathfrak g_{\mathrm{red}},
   \]
   up to the explicitly trivialized fiber-orientation line.
2. Its bracket is
   \[
     \{f,g\}_{\mathrm{red}}
     =
     \partial_{z_1}f\,\partial_{z_2}g
     -
     \partial_{z_2}f\,\partial_{z_1}g.
   \]
3. Its cotangent action is the Matlis coadjoint action
   \[
     z_1^pz_2^q\cdot\rho_{i,j}
     =
     -(pj-qi+p-q)\rho_{i-p+1,j-q+1}.
   \]
4. The brane image is the line defect
   \(L_{\mathrm{red}}=\mathbb R_t\times\{z_1=0\}\), with finite-\(N\)
   evaluation \(f\mapsto\overline{\operatorname{Tr}f(X,Y)}\).
5. The reduced BV pairing is induced from
   \[
     \operatorname{Res}_{z_1,z_2}(\rho f),
   \]
   together with the compact-support \(t\)-density and the chosen fiber
   orientation normalization.
6. The scalar anomaly is the same class
   \[
     \hbar N[\bar c]\in H^2_{\mathrm{Lie}}(\bar A;\mathbb C)[[\hbar]]
   \]
   unless the selected anomaly branch cancels it.
7. The Moyal product and finite-\(N\) Weyl relation are compatible because
   \(z_2\) was retained.
8. A Dirac BRST curve/vertex algebra, Zhu map, or \(SC^{\mathrm{ch},\mathrm{top}}\)
   comparison is a corollary only after the reduction theorem plus
   factorization-to-vertex and anomaly data are constructed.

## Obstruction List

- `Ob-CxR-01`: Dolbeault \(z_2\)-fiber datum.  Need an explicit
  \(p_{z_2},i_{z_2},K_{z_2}\) with support and factorization-product
  compatibility.  A formal identity on coefficients is not enough for a
  mixed factorization theorem.
- `Ob-CxR-02`: orientation and degree line.  The \(s\)-compact-support
  contraction and holomorphic/residue pushforward carry shifts and
  orientation factors.  The theorem must state how they are absorbed into
  the reduced BV degrees and pairing.
- `Ob-CxR-03`: residue collapse.  Literal \(b=0\) residue is not an
  \(\mathfrak h\)-module quotient.  The theorem must retain all
  \(z_2\)-principal parts or prove a different invariant subquotient.
- `Ob-CxR-04`: brane collar module.  The reduced brane is a line defect
  in \(Y\), and a stratified/collar module must be constructed before
  claiming full closed-to-open factorization centrality.
- `Ob-CxR-05`: scalar anomaly branch.  The reduced surface inherits
  \(\hbar N[\bar c]\).  A BRST theorem must choose and verify its
  cancellation mechanism.
- `Ob-CxR-06`: Moyal/Capelli normalization.  Moyal compatibility uses the
  retained \(z_2\) coefficient system and the existing Weyl/Capelli
  normalization.  The all-\(N\) radial comparison remains conditional on
  its moment-ideal primitive.
- `Ob-CxR-07`: factorization-to-vertex.  A \(C\times R\) mixed
  factorization algebra is not automatically a vertex algebra.  Need
  finite Laurent OPEs, vacuum, translation, locality, and a Zhu/zero-mode
  map.
- `Ob-CxR-08`: equivariant normalization.  In an \(\Omega\)-background,
  residue normalization and smooth Euler localization differ by the
  explicit normal Euler factor
  \((\epsilon_s\epsilon_1\epsilon_2)^{-1}\) up to orientation sign.  The
  theorem must choose or compare them.
- `Ob-CxR-09`: graph/QME transport.  The controlled reduction does not
  transport Costello propagators, counterterms, or brane-defect QME data.
  Those remain in the non-scalar QME and stratified trace-state lanes.

## Manuscript Impact

No immediate TeX correction is forced if the manuscript only states the
native \(\mathbb C^2\) factorization algebra and marks curve/VOA claims as
future reductions.  If the manuscript introduces a reduced Dirac BRST
chiral algebra, a Zhu bridge, or an \(SC^{\mathrm{ch},\mathrm{top}}\)
comparison as a theorem, it needs a new controlled \(C\times R\) theorem
lane with the hypotheses and obstruction vector above before that claim.
