# Critique Refresh Ingestion, 2026-04-30 09:43 SAST

Source:
`materials/raw/2026-04-30-mixed-holomorphic-topological-strings-critique.pdf`.

Extracted text:
`materials/processed/2026-04-30-mixed-holomorphic-topological-strings-critique.txt`.

Identity:

- PDF creation time: 2026-04-30 09:43:08 SAST.
- Desktop file copied at repository refresh after 09:47 SAST.
- Pages: 1394.
- Raw SHA-256:
  `b2ad8fe6156b4d5141c574e8f52cc1368f3fcdd76e8ff384b16850f83e8c7aa4`.
- Text SHA-256:
  `e05d28e561b04c4ffec170e4507562f8077d2d224d6cb2ab19326f50e8b2d6ad`.

This supersedes the prior 923-page, 04:11 SAST critique source in the
attack-heal launch manifest.  Earlier swarm reports remain evidence, not
authority.

## Core Reading

The refreshed critique pushes the paper toward a sharper native local
architecture.  It does not license automatic acceptance.  Every item
below is an attack-heal theorem surface requiring direct mathematical
construction, counterexample, or named obstruction.

The manuscript is about the formal local model
\[
  X_{\mathrm{loc}}
  =
  \mathbb R^2_{\mathrm{top}}\times\mathbb C^2_{\mathrm{hol}},
  \qquad
  L=\mathbb R_t\times\{s=0,z_1=z_2=0\}.
\]
The curve \(\mathbb C\times\mathbb R\) geometry of Vol II is a reduced
shadow only.  It is not the native setting.

## Principal Attacks To Preserve

1. **PBW shadow is not deformation-level Koszul duality.**  The stable
   open trace sector can match a PBW special fibre of
   \(U(\mathfrak h\ltimes P[1])\).  This does not by itself prove a
   deformation-level closed-open Koszul theorem.

2. **Closed-open source typing.**  The boundary Hamiltonian function
   \(f\mapsto \operatorname{Tr}f(\phi_1,\phi_2)\) is sourced by a
   Hamiltonian mode / \(u_I\)-coordinate in the CE/PV dictionary, not by a
   closed CE length-one Hamiltonian cochain \(c^I\).  The generator rule
   to attack and prove is
   \[
     c^I\mapsto \theta^I,\qquad u_I\mapsto O_I .
   \]

3. **Polynomial descendants are not the cotangent module.**  The
   one-\(\psi\) descendants are a PBW label shadow.  The deformation-level
   cotangent module is the Grothendieck-Matlis principal-part module
   \[
     P=\mathfrak h^\vee_{\mathrm{cont}}
     =
     \bigoplus_{a+b>0}\mathbb C\rho_{a,b},
     \qquad
     \rho_{a,b}=z_1^{-a-1}z_2^{-b-1}\,dz_1dz_2 ,
   \]
   with
   \[
     z_1^p z_2^q\cdot\rho_{a,b}
     =
     -(pb-qa+p-q)\rho_{a-p+1,b-q+1}.
   \]

4. **Scalar quotient cannot be implicit.**  Brackets involving
   \(z_1,z_2\) have a central trace contact term before scalar reduction:
   \(\{\operatorname{Tr}\phi_1,\operatorname{Tr}\phi_2\}=N\).  Any
   reduced Hamiltonian bracket theorem must state the scalar quotient or
   the scalar-anomaly branch.

5. **Central operation versus tautology.**  Multiplication by a boundary
   function is not the full derived factorization-centre theorem.  The
   target must be typed as a derived \(P_0\)-central operation or left as
   a reduced current shadow until centrality homotopies are constructed.

6. **Weyl/Moyal target is not Costello graph realization.**  The formal
   Moyal algebra, principal-part Moyal action, and Capelli/Weyl scalar
   term are algebraic theorem surfaces.  They do not prove Costello
   propagators, counterterms, QME, or all-order graph identities.

## Positive Architecture To Test

### Native closed sector

\[
  \mathfrak h=\mathbb C[[z_1,z_2]]/\mathbb C\cdot1,\qquad
  P=\mathfrak h^\vee_{\mathrm{cont}},\qquad
  \mathfrak g=\mathfrak h\ltimes P[1].
\]
For \(D\subset\mathbb R^2\), \(B\subset\mathbb C^2\),
\[
  \mathcal E_{\mathrm{cl}}(D\times B)
  =
  \Omega^\bullet(D)\widehat\otimes
  \Omega^{0,\bullet}(B)\widehat\otimes
  \bigl(\mathfrak h[1]\oplus P[2]\bigr),
  \qquad
  Q=d_{\mathbb R^2}+\bar\partial_{\mathbb C^2}.
\]
The classical action is Hamiltonian BF:
\[
  I_{\mathrm{cl}}=\frac12\int\langle\beta,\{\alpha,\alpha\}\rangle .
\]
The CME must be proved from \(Q^2=0\), Jacobi, and residue/coadjoint
invariance.

### Native open Dirac brane

\[
  S_\partial=\int_{\mathbb R_t}
  \operatorname{Tr}\bigl(\phi_1\,d\phi_2+A[\phi_1,\phi_2]\bigr),
  \qquad
  Q\psi=[\phi_1,\phi_2],\quad Q\phi_i=0.
\]
This is the matrix Dirac probe of the holomorphic normal surface.

### Inner CE/PV derived-centre theorem

The central reduced theorem is
\[
  C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak h\ltimes P[1])
  \cong
  \mathrm{PV}\bigl(\widehat S(\mathfrak h)\bigr),
  \qquad
  c^I\mapsto\theta^I,\quad u_I\mapsto O_I.
\]
Agents must attack signs, degrees, topology, continuity, and whether this
has been accidentally promoted to the unreduced factorization centre.

### Native holomorphic \(E_2\) / factorization algebra

The native holomorphic algebra is not a curve VOA.  It is the
two-complex-dimensional factorization object
\[
  V_{\mathrm{Ham}}^{(2)}(B)
  =
  C^\bullet_{\mathrm{CE}}
  \bigl(\Omega_c^{0,\bullet}(B)\widehat\otimes
  (\mathfrak h\ltimes P[1])\bigr),
  \qquad B\subset\mathbb C^2 .
\]
The binary collision operations are the Hamiltonian bracket and the
coadjoint action.  A Costello-quality construction should test the
Bochner-Martinelli kernel
\[
  K_{\mathrm{BM}}(z)
  =
  \frac{1}{(2\pi i)^2}
  \frac{\bar z_1\,d\bar z_2-\bar z_2\,d\bar z_1}
       {( |z_1|^2+|z_2|^2)^2},
  \qquad
  \bar\partial K_{\mathrm{BM}}=\delta_0 .
\]

### Curve chiral algebra only after reduction

A curve vertex/chiral algebra enters only after a controlled reduction to
\(\mathbb C_z\times\mathbb R_x\).  The legitimate reduced Dirac BRST
vertex algebra has adjoint fields \(Z_1,Z_2\), ghosts \(b,c\), OPEs
\[
  Z_1{}^i{}_j(z)Z_2{}^k{}_\ell(w)
  \sim
  \frac{\hbar\,\delta^i_\ell\delta^k_j}{z-w},
  \qquad
  b^i{}_j(z)c^k{}_\ell(w)
  \sim
  \frac{\delta^i_\ell\delta^k_j}{z-w},
\]
and
\[
  j_{\mathrm{BRST}}
  =
  \operatorname{Tr}(c[Z_1,Z_2])
  +\frac12\operatorname{Tr}(b[c,c]).
\]
The reduced chiral algebra is
\[
  A_{\partial,N}^{\mathrm{Dir\text{-}ch}}
  =
  H^\bullet(V_N^{\mathrm{Dir}},Q_{\mathrm{BRST}}).
\]
The zero-mode and Zhu bridge must be proved after reduction, not assumed
in the native \(\mathbb C^2\) theory.

### Controlled \(\mathbb C\times\mathbb R\) reduction

A reduction datum must specify
\[
  \pi(t,s;z_1,z_2)=(t;z_1),
  \qquad
  \kappa_{\mathrm{top}},
  \qquad
  \kappa_{\mathrm{hol}},
  \qquad
  L_{\mathrm{red}}=\mathbb R_t\times\{z_1=0\}.
\]
It must retain \(z_2\)-modes or residue/principal-part coefficients:
\[
  \mathfrak h_{\mathrm{red}}
  =
  \mathbb C[[z_1]][[z_2]]/\mathbb C\cdot1.
\]
Setting \(z_2=0\) collapses the Hamiltonian bracket and is therefore not
a faithful reduction.

### Zhu bridge after reduction

With conformal weights chosen so that \(o(Z_1)=X\), \(o(Z_2)=Y\),
the Zhu algebra before BRST reduction should be
\[
  A(V^{\mathrm{free}}_{\mathrm{red},N})
  =
  \mathrm{Weyl}(\mathrm{Mat}_{2N})
  \otimes
  \mathrm{Cliff}_{bc}(\mathfrak{gl}_N).
\]
The induced BRST relation should include the Capelli/Weyl shift
\[
  QB=YX-XY+\hbar N I+[B,C],
  \qquad
  YX-XY+\hbar N I=0
\]
in cohomology.  The comparison chain to test is
\[
  \mathrm{ChirHoch}^\bullet(V_{\mathrm{red},N}^{\mathrm{Dir}})
  \to
  HH^\bullet(A(V_{\mathrm{red},N}^{\mathrm{Dir}}))
  \rightsquigarrow_{\mathrm{gr},\,N\to\infty}
  \mathrm{PV}(S(\mathfrak h))
  \cong
  C^\bullet_{\mathrm{CE}}(\mathfrak h\ltimes P[1]).
\]

### Normal \(\Omega\)-background theorem surface

The proposed equivariant normal localization is
\[
  T_\Omega=\mathbb C^*_{\varepsilon_s}\times
  \mathbb C^*_{\varepsilon_1}\times
  \mathbb C^*_{\varepsilon_2}
\]
acting on \((s,z_1,z_2)\).  The fixed locus is the brane line.  Weights:
\[
  w(H_{a,b})=a\varepsilon_1+b\varepsilon_2,\qquad
  w(\rho_{a,b})=-a\varepsilon_1-b\varepsilon_2,\qquad
  w(\hbar)=\varepsilon_1+\varepsilon_2.
\]
On \(\varepsilon_1+\varepsilon_2=0\) the Poisson bracket is strictly
equivariant.  Off that locus it is valued in the inverse symplectic
character line.  This is a theorem surface for equivariant refinement and
kernel grading, not a proof of Costello QME convergence.

## Platonic Theorem Package To Attack

The refreshed critique suggests the following theorem order.  The swarm
must attack each item for proof strength and source typing:

1. Dirac brane probe.
2. Stable trace theorem.
3. Principal-part cotangent theorem.
4. Coadjoint action theorem.
5. \(\Psi\)-no-go theorem.
6. Hamiltonian BF equations and CME.
7. Inner CE/PV derived \(P_0\)-centre theorem.
8. Brane-line current theorem.
9. Native holomorphic \(E_2\) theorem.
10. Moyal principal-part quantum target.
11. Scalar anomaly theorem.
12. Controlled \(\mathbb C\times\mathbb R\) reduction theorem.
13. Zhu bridge theorem for the reduced Dirac chiral algebra.
14. Zhu-Hochschild-CE/PV comparison theorem.
15. Normal \(\Omega\)-background construction.
16. Physical large-\(N\) theorem surface.
17. Costello graph/QME theorem surface.
18. Global compact-CY/firewall comparison surface.

## Next Swarm Partition

Do not launch from the stale 04:11 manifest without this override.  The
next six-at-a-time swarm should be partitioned by theorem surface:

1. Native \(R^2\times C^2\) BV/Hamiltonian BF fields.
2. Open Dirac brane and scalar-contact anomaly.
3. Principal parts, coadjoint action, and \(\Psi\)-no-go.
4. CE/PV derived-centre signs, degrees, topology, and continuity.
5. Native holomorphic \(E_2\) / Bochner-Martinelli factorization kernel.
6. Brane-line currents and unreduced centrality homotopies.
7. Controlled \(C\times R\) reduction retaining \(z_2\)-coefficients.
8. Reduced Dirac BRST chiral algebra and \(Q_{\mathrm{BRST}}^2=0\).
9. Zhu / Hochschild / stable HKR bridge after reduction.
10. Moyal coefficients, Capelli shift, scalar quotient, and finite-\(N\)
    Weyl relations.
11. Radial-parts all-\(N\) normalization and trace-diagram homotopy.
12. Costello graph/QME realization, weighted kernels, counterterms, and
    wavefront habitats.
13. Normal \(\Omega\)-background weights, localization, and refined
    Moyal parameter.
14. Physical large-\(N\) state/cumulant/Ward-identity requirements.
15. Compact-CY/Vol III/Igusa/BKM firewall audit.
16. Manuscript theorem-package reordering and title/abstract repair.
17. Source-primary audit for Costello, Witten, BV/factorization, Zhu,
    HKR, and principal parts.
18. Integration build, labels, references, and stale report reconciliation.

Each lane must use Supremum Discipline: reconstruct the strongest true
theorem by adding the missing object, habitat, map, reduction datum,
kernel, or obstruction class.  Do not lower a claim merely to make it
harmless.
