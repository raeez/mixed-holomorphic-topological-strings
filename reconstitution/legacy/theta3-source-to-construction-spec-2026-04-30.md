# Theta3 Source-to-Construction Specification

## Status

No native primitive is present in the current manuscript or script.  The
available data give one closed one-row finite obstruction, not a solved
order-three QME branch:
\[
  \mathsf E_{\theta_3,M}
    =
  -K^M_{\Theta_3}(\zeta_{M,\nu_3}),\qquad
  \widehat\sigma_{\mathrm{sc},M}(\mathsf E_{\theta_3,M})=0.
\]
The finite-row complex supplied by the row array is
\[
  K^0_{\theta_3,M}=0,\qquad
  K^1_{\theta_3,M}=\mathbb C\mathsf E_{\theta_3,M},\qquad d=0.
\]
Thus the residual vector is \(r=(1)\), and the covector
\(\ell(\mathsf E_{\theta_3,M})=1\) certifies a nonzero class in this
displayed finite row subcomplex.

The obstruction is killed only by one of the following supplied data.  A
symbolic name \(C_{\theta_3}\) is not a datum.

## Common Finite-Window Record

For every \(M\ge 3\), a theta-killing record must contain:

- graph label \(\Theta_3\) with \(|\Theta_3|_\hbar=3\);
- source face \(\nu_3\) with coefficient
  \(d_{\mathrm{CE}}\zeta_M=+\zeta_{M,\nu_3}+\cdots\);
- row value
  \[
    \mathsf E_{\theta_3,M}
      =
    -K^M_{\Theta_3}(\zeta_{M,\nu_3});
  \]
- the closure proof
  \(d_{\mathrm{ns},M}\mathsf E_{\theta_3,M}=0\);
- scalar projection
  \(\widehat\sigma_{\mathrm{sc},M}(\mathsf E_{\theta_3,M})=0\);
- truncation
  \[
    \pi_{M,N}\mathsf E_{\theta_3,M}
      =
    \begin{cases}
      \mathsf E_{\theta_3,N},&N\ge3,\\
      0,&N<3;
    \end{cases}
  \]
- the inherited labels
  \(P^{w,M}_{\epsilon,L}(h_{2,1},\rho_{2,1})\),
  \(\Delta^{w,M}_{\epsilon,L}(h_{1,1},\rho_{1,1})\),
  \(E_{\mathrm{Weyl}}(z_1^2,z_2)\),
  \(u_{a(t)dt\otimes z_1^2}\),
  \(u_{b(t)dt\otimes z_2}\),
  \(c_{B_\theta,\rho_{2,1}}\), \(I^w_{0,M}\), and
  \(W^{R,M}_{\Theta_3,L,w}(B^\Theta_\bullet)\);
- the full \(\mathfrak{gl}(N|N)\)-equivariant Brauer marker
  \(\mathfrak m_{\theta_3}\) with cyclic supertrace zero.

These fields are necessary because the finite-window package definition
requires every row value, sign, scalar gate, counterterm face, source face,
and truncation coefficient before the \(H^1/\varprojlim^1\) question is
defined.

## Construction A: CE Ancestor

A CE-ancestor primitive is a degree-zero source element
\[
  \eta_{\theta_3,M}\in C^\bullet_{\mathrm{CE,lab}}(\mathcal G_M)
\]
with
\[
  d_{\mathrm{CE}}\eta_{\theta_3,M}
    =
  \zeta_{M,\nu_3}.
\]
The primitive candidate is
\[
  C^{\mathrm{CE}}_{\theta_3,M}
    =
  K^M_{\Theta_3}(\eta_{\theta_3,M}).
\]
For a degree-zero Hom-valued kernel,
\[
  d_{\mathbf K}K(\eta)
    =
  d_MK(\eta)-K(d_{\mathrm{CE}}\eta).
\]
Therefore the desired boundary
\[
  d_M C^{\mathrm{CE}}_{\theta_3,M}
    =
  K^M_{\Theta_3}(\zeta_{M,\nu_3})
    =
  -\mathsf E_{\theta_3,M}
\]
is valid exactly when the Hom-valued Bianchi term
\[
  d_{\mathbf K}K^M_{\Theta_3}(\eta_{\theta_3,M})
\]
vanishes, or when every extra target-differential, bracket, collision, and
counterterm face in that term is included in the same degree-one row basis
and cancels in the total residual.

The finite primitive matrix then has
\[
  A^M_{\mathsf E,C^{\mathrm{CE}}}=-1,\qquad r^M_{\mathsf E}=1,
  \qquad c_M=1.
\]
The compatible tower additionally requires
\[
  \pi_{M,N}C^{\mathrm{CE}}_{\theta_3,M}
    =
  \begin{cases}
    C^{\mathrm{CE}}_{\theta_3,N},&N\ge3,\\
    0,&N<3,
  \end{cases}
\]
or else the Roos class is represented by
\([\pi_{M,N}C^{\mathrm{CE}}_{\theta_3,M}-C^{\mathrm{CE}}_{\theta_3,N}]\).

The current data do not contain \(\eta_{\theta_3,M}\), the Bianchi
companion rows, or this transport.  Hence this is a precise construction
specification, not an existing primitive.

## Construction B: Local Counterterm Primitive

A direct local counterterm primitive is a degree-zero local functional
\[
  C^{\mathrm{ct}}_{\theta_3,M}
    \in
  \mathcal K^0_{\mathrm{ns},M}(I)
\]
with the explicit target differential
\[
  d_{\mathrm{ns},M}C^{\mathrm{ct}}_{\theta_3,M}
    =
  -\mathsf E_{\theta_3,M}.
\]
The counterterm record must specify the local vertex
\[
  C^M_{\Theta_3,\nu_3,w}(\epsilon;B^\Theta_\bullet),
\]
its regular-density or wavefront-admissible locality proof, its scalar
projection
\[
  \widehat\sigma_{\mathrm{sc},M}(C^{\mathrm{ct}}_{\theta_3,M})=0,
\]
and the same identity/zero truncation as above.  If the primitive has
nonidentity transport
\[
  \pi_{M,N}C^{\mathrm{ct}}_{\theta_3,M}
    =
  C^{\mathrm{ct}}_{\theta_3,N}+h_{M,N},
\]
then the fixed-window obstruction is gone but the remaining obstruction is
\([h_{M,N}]\in H^0(\mathcal K^\bullet_{\mathrm{ns},N}(I))\).

The current Costello package names possible counterterm vertices in
general, but it does not provide this vertex, this differential, or this
scalar and truncation verification.

## Construction C: Complete Companion-Face Table

A companion-face cancellation is not a primitive.  It replaces the one-row
presentation by the complete source-face presentation.  Let
\[
  d_{\mathrm{CE}}\zeta_M
    =
  \sum_{\nu\in F_{\Theta_3,M}}
  \epsilon^{\mathrm{CE}}_{\Theta_3,\nu}\zeta_{M,\nu},
  \qquad
  \epsilon^{\mathrm{CE}}_{\Theta_3,\nu_3}=+1.
\]
The complete degree-one residual is
\[
  R^{\mathrm{CE}}_{\Theta_3,M}
    =
  -\sum_{\nu\in F_{\Theta_3,M}}
  \epsilon^{\mathrm{CE}}_{\Theta_3,\nu}
  K^M_{\Theta_3}(\zeta_{M,\nu}).
\]
The theta obstruction is killed by companion faces exactly when
\[
  R^{\mathrm{CE}}_{\Theta_3,M}=0
\]
in the declared row basis, with scalar gates zero for every summand and
with source-face truncation matrices
\[
  \pi_{M,N}E^M_{\Theta_3,\nu}
    =
  \sum_{\nu'}
  v^{M,N}_{\Theta_3,\nu;\Theta_3,\nu'}
  E^N_{\Theta_3,\nu'}
\]
satisfying the cocycle identity for \(v\).

The complete table must also include the codimension-two equations
identifying the two orders of every pair of boundary operations:
output graph, sign, and marker transport.  Without these entries the
marked differential is not known to square to zero, and the residual is not
a theorem-grade cocycle.

The current row records only the summand \(\nu_3\) and the phrase
"other faces"; it does not give \(F_{\Theta_3,M}\), the signs, the row
coordinates, the scalar gates, or \(v^{M,N}\).

## Minimal Exact Data Payload

The next manuscript/script datum that can decide the theta branch is one
of the following machine-checkable payloads:

```yaml
theta3_ce_ancestor:
  eta_label: eta_theta_3
  ce_boundary:
    - [zeta_M_nu_3, 1]
  bianchi_rows: []
  bianchi_identity: d_K K_Theta3(eta_theta3) = 0
  primitive_row:
    label: C_theta_3_CE
    differential_entries:
      - [E_theta_3, -1]
    scalar_projection: 0
    transport:
      N_ge_3: identity
      N_lt_3: zero
```

```yaml
theta3_counterterm_primitive:
  counterterm_vertex: C^M_{Theta_3,nu_3,w}(epsilon;B^Theta_bullet)
  locality: regular_density_or_wavefront_admissible
  differential_entries:
    - [E_theta_3, -1]
  extra_degree_one_entries: []
  scalar_projection: 0
  transport:
    N_ge_3: identity
    N_lt_3: zero
```

```yaml
theta3_complete_companion_faces:
  source_faces:
    - [nu_3, 1, E_theta_3]
    - [nu_i, epsilon_i, E_theta_i]
  residual_sum: 0
  scalar_projection_each_face: 0
  v_truncation_matrices: supplied
  codimension_two_closure: supplied
```

These are genuinely necessary, not presentational conveniences.  The
finite-row differential is zero until a degree-zero row is supplied; the
source row is not complete until all CE faces and signs are supplied; the
inverse-limit QME claim is not defined until primitive transport and the
Roos class are computed.
