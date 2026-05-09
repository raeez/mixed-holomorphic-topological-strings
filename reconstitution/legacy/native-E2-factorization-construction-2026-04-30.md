# Native holomorphic E2 factorization construction

Date: 2026-04-30.
Lane: native \(\mathbb C^2\) holomorphic \(E_2\)/factorization algebra and
controlled-reduction firewall.

## Verdict

The native object is already a constructed two-complex-dimensional
holomorphic factorization algebra:
\[
  \mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}(B)
  =
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  \bigl(
    \Omega_c^{0,\bullet}(B)\widehat\otimes
    (\mathfrak h\ltimes\mathcal P[1])
  \bigr),
  \qquad B\subset \mathbb C^2_{\mathrm{hol}}.
\]
Here
\[
  \mathfrak h=\mathbb C[[z_1,z_2]]/\mathbb C\cdot 1,\qquad
  \mathcal P=\operatorname{Ann}_{\mathrm{res}}(\mathbb C\cdot1)
  \subset H^2_{(z_1,z_2)}(\mathbb C[[z_1,z_2]])\,dz_1dz_2
  \cong \mathfrak h^\vee_{\mathrm{cont}} .
\]
This is proved for the CE/factorization assignment and for the
semidirect Hamiltonian-cotangent collision algebra.  The explicit
Bochner-Martinelli transfer kernel remains a named construction
obligation.  No curve vertex algebra, Laurent OPE, Zhu algebra, or
Volume II \(\mathbb C\times\mathbb R\) theorem is native to this object.

## Object Map

### Geometry and fields

The base formal local pair is
\[
  X=\mathbb R_t\times\mathbb R_s\times\mathbb C^2_{z_1,z_2},
  \qquad
  L=\mathbb R_t\times\{s=z_1=z_2=0\}.
\]
The holomorphic Darboux disk is
\[
  (\widehat{\mathbb C^2}_0,\omega=dz_1\wedge dz_2),
  \qquad
  \Omega_{\mathrm{loc}}=dz_1dz_2 .
\]
On a holomorphic polydisk \(B\), the Hamiltonian BF fields are the
Dolbeault fields
\[
  \alpha\in \Omega^{0,\bullet}(B)\widehat\otimes\mathfrak h[1],
  \qquad
  \beta\in \Omega^{0,\bullet}(B)\widehat\otimes\mathcal P[2],
\]
with linear differential \(\bar\partial\) and cubic Hamiltonian BF
interaction
\[
  I_{\mathrm{Ham}}(\alpha,\beta)
  =
  \frac12\int_B
  \bigl\langle \beta,\{\alpha,\alpha\}\bigr\rangle_{\mathrm{res}}.
\]
The classical master equation is the Jacobi identity for
\(\mathfrak h\) plus the coadjoint-module identity for \(\mathcal P\).
The observable Lie input uses compact supports:
\[
  \mathfrak g_B
  =
  \Omega_c^{0,\bullet}(B)\widehat\otimes
  \mathfrak g,\qquad
  \mathfrak g=\mathfrak h\ltimes\mathcal P[1],
\]
with differential
\[
  d_{\mathfrak g_B}=\bar\partial\otimes 1.
\]
The CE differential on
\(\mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}(B)\) is the sum of the dual
Dolbeault differential and the continuous CE differential dual to the
semidirect bracket.

For a mixed open \(U\times B\), \(U\subset\mathbb R^2_{\mathrm{top}}\),
the enhancement is
\[
  \mathfrak g^{\mathrm{mix}}_{U,B}
  =
  \Omega_c^\bullet(U)\widehat\otimes
  \Omega_c^{0,\bullet}(B)\widehat\otimes\mathfrak g,
\]
\[
  \mathcal F_{\mathrm{Ham}}^{\mathrm{mix}}(U\times B)
  =
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  (\mathfrak g^{\mathrm{mix}}_{U,B}),
  \qquad
  d=d_U+\bar\partial_B+d_{\mathrm{CE}}.
\]
It is locally constant in \(U\) and holomorphic in \(B\).

### Scalar quotient

The quotient by constants is forced, not decorative.  If
\[
  X_f=(\partial_{z_1}f)\partial_{z_2}
      -(\partial_{z_2}f)\partial_{z_1},
  \qquad \iota_{X_f}\omega=-df,
\]
then \(X_f=0\) exactly for constant \(f\).  Thus
\[
  \mathfrak h=\mathbb C[[z_1,z_2]]/\mathbb C\cdot1
\]
is the Hamiltonian Lie algebra of the formal disk.  Its bracket is
\[
  \{f,g\}
  =
  \partial_{z_1}f\,\partial_{z_2}g
  -
  \partial_{z_2}f\,\partial_{z_1}g
  \pmod{\mathbb C}.
\]
For monomials,
\[
  \{z_1^az_2^b,z_1^cz_2^d\}
  =
  (ad-bc)z_1^{a+c-1}z_2^{b+d-1}.
\]
The scalar quotient removes the constant Hamiltonian from the native Lie
algebra.  It does not erase the finite-\(N\) quantum scalar-contact
anomaly; that anomaly is carried in the separate Weyl/Moyal and Capelli
lanes.

### Principal parts and coadjoint action

Use the residue basis
\[
  \rho_{a,b}=z_1^{-a-1}z_2^{-b-1}dz_1dz_2,
  \qquad
  \operatorname{Res}_0(\rho_{a,b}z_1^mz_2^n)
  =
  \delta_{a,m}\delta_{b,n}.
\]
The scalar line \(\rho_{0,0}\) is removed by
\(\operatorname{Ann}_{\mathrm{res}}(\mathbb C\cdot1)\).  The coadjoint
action is fixed by integration by parts:
\[
  \operatorname{Res}_0((f\cdot\rho)g)
  =
  -\operatorname{Res}_0(\rho\,\{f,g\}).
\]
Equivalently,
\[
  z_1^pz_2^q\cdot\rho_{i,j}
  =
  -(pj-qi+p-q)\rho_{i-p+1,j-q+1},
\]
with negative-index targets equal to zero.

### Factorization product

For disjoint holomorphic polydisks
\[
  B_1,\ldots,B_n\subset B,
\]
extension by zero gives continuous maps
\[
  \Omega_c^{0,\bullet}(B_i)\widehat\otimes\mathfrak g
  \longrightarrow
  \Omega_c^{0,\bullet}(B)\widehat\otimes\mathfrak g.
\]
The factorization product is the induced map on continuous CE
observables, followed by completed graded-commutative multiplication:
\[
  \bigotimes_i \mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}(B_i)
  \longrightarrow
  \mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}(B).
\]
The same formula, tensoring with extension by zero on
\(\Omega_c^\bullet(U)\), gives the mixed product over
\(\mathbb R^2_{\mathrm{top}}\times\mathbb C^2_{\mathrm{hol}}\).

The only universal property used here is the CE one: a continuous
linear map on compactly supported generators, compatible with
differentials and brackets, extends uniquely to a continuous morphism of
degreewise completed symmetric CE algebras.  No universal property of
factorization centers, vertex envelopes, or Zhu algebras is invoked.

### Collision operations

The arity-two collision coefficients are the semidirect dg Lie brackets.
For compactly supported Dolbeault forms \(\alpha,\beta\),
Hamiltonians \(f,g\in\mathfrak h\), and principal parts
\(\rho,\sigma\in\mathcal P\),
\[
  [\alpha\otimes f,\beta\otimes g]
  =
  (\alpha\wedge\beta)\otimes\{f,g\},
\]
\[
  [\alpha\otimes f,\beta\otimes\rho[1]]
  =
  (\alpha\wedge\beta)\otimes(f\cdot\rho)[1],
  \qquad
  [\alpha\otimes\rho[1],\beta\otimes\sigma[1]]=0,
\]
with the ordinary tensor-product Koszul signs.  The ternary \(E_2\)
coherence at this algebraic level is the Jacobi identity for
\(\mathfrak h\ltimes\mathcal P[1]\).  This is a holomorphic
factorization collision law on \(\mathbb C^2\), not a one-variable
Laurent OPE.

## Bochner-Martinelli Boundary

The stronger analytic transfer theorem would construct a cutoff
continuous homotopy
\[
  H_{\mathrm{BM}}\alpha(z)
  =
  \int_{\zeta\in B}\omega_{\mathrm{BM}}(\zeta,z)\wedge\alpha(\zeta)
\]
from
\[
  \omega_{\mathrm{BM}}(\zeta,z)
  =
  \frac{1}{(2\pi i)^2}
  \frac{
    (\overline{\zeta_1-z_1})\,d\bar\zeta_2
    -
    (\overline{\zeta_2-z_2})\,d\bar\zeta_1
  }
  {|\zeta-z|^4}
  \wedge d\zeta_1\wedge d\zeta_2.
\]
The required identity is
\[
  \bar\partial H_{\mathrm{BM}}+H_{\mathrm{BM}}\bar\partial
  =
  \operatorname{id}-\pi_{\mathrm{hol}}.
\]
The present stable theorem does not assert this transfer.  The missing
data are the completed tensor habitat, cutoff/support estimates,
compatibility with extension by zero on two and three polydisks, and the
identification of the transferred arity-two operation with the
Hamiltonian/coadjoint brackets above.

## Controlled \(\mathbb C\times\mathbb R\) Shadow

The only admissible curve shadow is a controlled reduction.  Let
\[
  Y=\mathbb R_t\times\mathbb C_{z_1},
  \qquad
  \pi(t,s;z_1,z_2)=(t;z_1).
\]
A reduction datum is
\[
  \mathcal R_{\mathbb C\times\mathbb R}
  =
  (\pi,\kappa_{\mathrm{top}},\kappa_{\mathrm{hol}},
   B_{z_2},\pi_!,L_{\mathrm{red}},
   \langle-,-\rangle_{\mathrm{red}},
   \{-,-\}_{\mathrm{red}},H_{\mathrm{anom}}).
\]
The topological fiber part must include, on each oriented compact-support
\(s\)-interval \(J\),
\[
  p_s:\Omega_c^\bullet(J)\to\mathbb C[-1],
  \qquad
  i_s:\mathbb C[-1]\to\Omega_c^\bullet(J),
  \qquad
  K_s,
\]
\[
  d_sK_s+K_sd_s=\operatorname{id}-i_sp_s.
\]
The surviving line is \(H_c^1(J)\cong\mathbb C[-1]\); it is not an
acyclic discard of the \(s\)-direction.

The holomorphic fiber part must retain \(z_2\).  The algebraic
coefficient system is
\[
  \mathfrak h_{\mathrm{red}}
  =
  \mathbb C[[z_1]][[z_2]]/\mathbb C\cdot1,
  \qquad
  \mathcal P_{\mathrm{red}}
  =
  \operatorname{Ann}_{\mathrm{res}}(\mathbb C\cdot1),
\]
with the same two-variable bracket
\[
  \{f,g\}_{\mathrm{red}}
  =
  \partial_{z_1}f\,\partial_{z_2}g
  -
  \partial_{z_2}f\,\partial_{z_1}g.
\]
Thus
\[
  \mathfrak g_{\mathrm{red}}
  =
  \mathfrak h_{\mathrm{red}}\ltimes\mathcal P_{\mathrm{red}}[1].
\]
The reduced brane is
\[
  L_{\mathrm{red}}=\mathbb R_t\times\{z_1=0\}\subset Y,
\]
but the \(z_2\) normal coordinate survives as coefficient/open data:
\[
  \operatorname{ev}^{\mathrm{red}}_N(f)
  =
  \overline{\operatorname{Tr}f(X,Y)},
  \qquad
  X=\phi_1,\quad Y=\phi_2.
\]

Given the full datum \(\mathcal R_{\mathbb C\times\mathbb R}\), the
reduction functor on product opens
\[
  I\times J\times D_1\times D_2\longrightarrow I\times D_1
\]
is
\[
  \operatorname{Red}_{\mathcal R}
  \mathcal F_{\mathrm{Ham}}^{\mathrm{mix}}(I\times J\times D_1\times D_2)
  =
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  \bigl(
    \Omega_c^\bullet(I)\widehat\otimes
    \Omega_c^{0,\bullet}(D_1)\widehat\otimes
    \mathfrak g_{\mathrm{red}}
  \bigr),
\]
with the \(s\)-orientation shift placed either in the fields or kept as
the explicit line \(\mathbb C[-1]\), according to
\(\langle-,-\rangle_{\mathrm{red}}\).  The map on Lie inputs is
\[
  \Omega_c^\bullet(I)\widehat\otimes\Omega_c^\bullet(J)
  \widehat\otimes
  \Omega_c^{0,\bullet}(D_1)\widehat\otimes
  \Omega_c^{0,\bullet}(D_2)\widehat\otimes\mathfrak g
  \xrightarrow{\ p_s\otimes p_{z_2}\otimes B_{z_2}\ }
  \Omega_c^\bullet(I)\widehat\otimes
  \Omega_c^{0,\bullet}(D_1)\widehat\otimes
  \mathfrak g_{\mathrm{red}}.
\]
This is a genuine dg Lie/factorization functor only after the
\(z_2\)-Dolbeault or residue pushforward \(p_{z_2}\) has support control,
is compatible with extension by zero, and preserves binary and ternary
factorization products.  Without those analytic data, the algebraic
retained-coefficient map is constructed, while the full functor remains a
theorem surface.

Killing \(z_2\) is false:
\[
  \mathbb C[[z_1,z_2]]/\mathbb C\cdot1
  \longrightarrow
  \mathbb C[[z_1]]/\mathbb C\cdot1
\]
turns the Hamiltonian bracket into zero, sends \(\{z_1,z_2\}=1\) out of
the retained algebra, destroys Moyal compatibility, and fails on
principal parts since
\[
  z_1\cdot\rho_{a,0}=-\rho_{a,1}.
\]

## Curve VOA and Zhu Firewall

A one-dimensional vertex algebra requires extra data:
\[
  \mathfrak R_L
  =
  (\iota_L,\mathcal B_\perp,\mathsf R_{L,\mathcal B_\perp},
   V_L,\mathbf 1_L,T_L,Y_L,\zeta_{L,\hbar}),
\]
where
\[
  \iota_L:\operatorname{Spf}\mathbb C[[w]]
  \hookrightarrow \widehat{\mathbb C^2}_0
\]
is a chosen holomorphic line or defect germ, \(\mathcal B_\perp\) is a
normal boundary condition, and \(\mathsf R_{L,\mathcal B_\perp}\) is a
restriction functor compatible with disjoint disks and translations in
\(w\).  The vertex data must include
\[
  Y_L(a,w)b=\sum_{n\in\mathbb Z}(a_{(n)}b)w^{-n-1},
  \qquad a_{(n)}b=0\quad(n\gg0),
\]
vacuum, translation, locality, and a continuous Zhu/zero-mode map
\[
  \zeta_{L,\hbar}:(\bar A_\hbar,*)\longrightarrow\operatorname{Zhu}(V_L).
\]
These are not consequences of the native \(\mathbb C^2\) factorization
object.

After the controlled \(\mathbb C\times\mathbb R\) reduction, one may
target the reduced Dirac BRST vertex surface with fields
\[
  Z_1{}^i{}_j(z),\quad Z_2{}^i{}_j(z),\quad c^i{}_j(z),\quad b^i{}_j(z),
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
and BRST current
\[
  j_{\mathrm{BRST}}
  =
  \operatorname{Tr}(c[Z_1,Z_2])
  +\frac12\operatorname{Tr}(b[c,c]).
\]
Then
\[
  Q_{\mathrm{BRST}}=\operatorname{Res}j_{\mathrm{BRST}}(z)\,dz
\]
has square zero by moment-map equivariance and graded Jacobi, provided
the anomaly convention in \(\mathcal R_{\mathbb C\times\mathbb R}\) is
used.  The Zhu zero-mode theorem further requires weights
\[
  \operatorname{wt}(Z_1)=0,\quad \operatorname{wt}(Z_2)=1,\quad
  \operatorname{wt}(c)=0,\quad \operatorname{wt}(b)=1,
\]
and gives the Capelli-shifted relation
\[
  QB=YX-XY+\hbar N I+[B,C],
  \qquad
  YX-XY+\hbar N I=0.
\]
This is a reduced theorem surface, not the native holomorphic \(E_2\)
object.

## Status Table

| Construction | Status | Exact boundary |
|---|---|---|
| Native CE/factorization object \(\mathcal F_{\mathrm{Ham}}^{\mathrm{hol}}\) | proved | Lives on polydisks in \(\mathbb C^2\), not on a curve. |
| Hamiltonian scalar quotient | proved | Constants are killed in \(\mathfrak h\); finite-\(N\) scalar contact is separate. |
| Principal-part cotangent module \(\mathcal P\) | proved classical target | Quantum branch uses Moyal coadjoint action. |
| Semidirect collision algebra | proved | Jacobi gives algebraic ternary coherence; no Laurent OPE. |
| Holomorphic compact-support factorization product | proved at CE/extension-by-zero level | Explicit BM transfer kernel still open. |
| Bochner-Martinelli transfer | theorem surface | Needs cutoff habitat, homotopy identity, support estimates, arity-two comparison. |
| CE/PV coordinate comparison | proved as coordinate dg algebra | \(P_0\) form only in bracket-admissible/kernel-admissible habitats. |
| Controlled \(\mathbb C\times\mathbb R\) shadow | theorem surface with algebraic retained-\(z_2\) target | Needs analytic \(z_2\) pushforward, reduced BV pairing degrees, anomaly homotopy, factorization compatibility. |
| Dirac BRST/Zhu curve package | conditional theorem surface after controlled reduction | False transfer before \(\mathcal R_{\mathbb C\times\mathbb R}\). |

## File Anchors

- `main.tex:934-1228`: holomorphic/mixed sector definitions and the
  constructed Hamiltonian CE/factorization observables.
- `main.tex:2703-2753`: Hamiltonian polyvector reduction and scalar
  quotient.
- `theorem-lanes.tex:227-379`: local chiral/factorization taxonomy.
- `theorem-lanes.tex:381-511`: native holomorphic \(E_2\) collision lane
  and Bochner-Martinelli obligation.
- `theorem-lanes.tex:513-674`: vertex/OPE boundary.
- `theorem-lanes.tex:676-862`: controlled
  \(\mathbb C\times\mathbb R\) reduction with retained \(z_2\)
  coefficients.
- `theorem-lanes.tex:864-1002`: reduced Dirac BRST/Zhu theorem surface.
- `local-dictionary.tex:170-370`: local taxonomy and vertex/OPE
  restriction boundary.
- `claim-strength-ledger.tex:298-353`: status ledger for native E2,
  controlled reduction, and reduced Dirac BRST/Zhu.
- `reconstitution/chiral-algebra-construction-thread-2026-04-30.md`: local
  construction thread.
- `reconstitution/controlled-CxR-reduction-thread-2026-04-30.md`: retained
  \(z_2\) reduction thread.
- `reconstitution/reduced-dirac-brst-zhu-thread-2026-04-30.md`: reduced
  BRST/Zhu thread.
- `reconstitution/local-theorem-obligations-0957-refresh-2026-04-30.md`:
  current obligation index, especially CL-03, LO-06, and LO-07.

## Verification

Commands run for this report:

```bash
shasum -a 256 materials/raw/2026-04-30-mixed-holomorphic-topological-strings-critique.pdf
rg -n "Dirac|BRST|Zhu|chiral algebra|native holomorphic|E_2|E2|factorization|obligation|reduction" theorem-lanes.tex local-dictionary.tex reconstitution materials main.tex
rg -n -F -e "curve vertex algebra" -e "Bochner-Martinelli" -e "mathcal R" -e "hbar N I" -e "rho_{a,0}" -e "mathcal F_{\\mathrm{Ham}}^{\\mathrm{hol}}" reconstitution/native-E2-factorization-construction-2026-04-30.md reconstitution/swarm-2026-04-30-agent-199-native-E2-factorization-construction.md
git diff --cached --check -- reconstitution/native-E2-factorization-construction-2026-04-30.md reconstitution/swarm-2026-04-30-agent-199-native-E2-factorization-construction.md
rg -n -F "curve vertex algebra" reconstitution/native-E2-factorization-construction-2026-04-30.md reconstitution/swarm-2026-04-30-agent-199-native-E2-factorization-construction.md
```
