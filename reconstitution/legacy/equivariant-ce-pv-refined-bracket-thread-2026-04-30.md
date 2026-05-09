# Equivariant CE/PV Refined Bracket Thread, 2026-04-30

## Scope

This thread constructs the report-level theorem surface for the
\(T_\Omega\)-equivariant CE/PV comparison.  It does not edit theorem
files.  It uses the normal \(\Omega\)-background dictionary in
`local-dictionary.tex:377-624`, the coordinate CE/PV lane in
`theorem-lanes.tex:676-1261`, and the manuscript proof of the
cochain-level central-operation map in `main.tex:3434-3543`.

The stable target is:

\[
  \Phi_\Omega:
  C^\bullet_{\mathrm{CE},\mathrm{coord},\Omega}
  (\mathfrak h_\Omega\ltimes
  \mathfrak h^\vee_{\mathrm{cont},\Omega}[1])
  \longrightarrow
  \mathrm{PV}_{\mathrm{coord},\Omega}(A_{\partial,\Omega}),
  \qquad
  c^{a,b}\mapsto\theta^{a,b},\quad
  u_{a,b}\mapsto O_{a,b}.
\]

It is a \(T_\Omega\)-equivariant coordinate dg-algebra isomorphism.  It
becomes a \(P_0\)-isomorphism only on a bracket-admissible weighted
completion.  The strict ambient coordinate product is not promoted to a
global \(P_0\)-algebra.

## Weights

Let
\[
  T_\Omega=\C^*_{\epsilon_s}\times\C^*_{\epsilon_1}\times
  \C^*_{\epsilon_2},
  \qquad
  \chi_\omega=\epsilon_1+\epsilon_2.
\]

The holomorphic coordinates have
\[
  w(z_1)=\epsilon_1,\qquad w(z_2)=\epsilon_2,
  \qquad w(dz_1\wedge dz_2)=\chi_\omega,
  \qquad w(P)=-\chi_\omega .
\]

For \(I=(a,b)\), \(a+b>0\), put
\[
  H_I=H_{a,b}=z_1^az_2^b,\qquad
  W_I=a\epsilon_1+b\epsilon_2.
\]
The residue-dual principal part is
\[
  \rho_I=\rho_{a,b}
  =z_1^{-a-1}z_2^{-b-1}\,dz_1dz_2,
  \qquad w(\rho_I)=-W_I.
\]

The shifted cotangent generator
\(\eta^I=\rho_I[1]\in\mathfrak h^\vee_{\mathrm{cont}}[1]\) has the
same \(T_\Omega\)-weight \(-W_I\).  Shifts do not change equivariant
weight.

The coordinate weights are forced by invariant evaluation:

| object | role | weight |
|---|---|---|
| \(H_I\) | Hamiltonian basis | \(W_I\) |
| \(\eta^I=\rho_I[1]\) | shifted cotangent generator | \(-W_I\) |
| \(c^I\) | CE coordinate dual to \(H_I\) | \(-W_I\) |
| \(u_I\) | CE coordinate dual to \(\eta^I\) | \(W_I\) |
| \(O_I\) | PV/boundary Hamiltonian coordinate | \(W_I\) |
| \(\theta^I\) | PV odd vector-field coordinate | \(-W_I\) |
| \(\hbar_\omega\) | symplectic-character trivializer | \(\chi_\omega\) |

Thus the generator assignment is \(T_\Omega\)-equivariant:
\[
  w(c^I)=w(\theta^I),\qquad w(u_I)=w(O_I).
\]

This is the first necessary repair.  Assigning \(u_I\) the cotangent
generator's weight \(-W_I\), rather than the coordinate-dual weight
\(W_I\), would make \(u_I\mapsto O_I\) non-equivariant.

## Refined Bracket

For \(I=(a,b)\), \(J=(c,d)\),
\[
  \{H_I,H_J\}=(ad-bc)H_{I+J-(1,1)}.
\]
When \(K=I+J-(1,1)\), the weights satisfy
\[
  W_K=W_I+W_J-\chi_\omega.
\]
Hence the ordinary Poisson bracket is not a scalar
\(T_\Omega\)-equivariant Lie bracket unless \(\chi_\omega=0\).  It is a
bracket with values in the inverse symplectic-character line:
\[
  \{-,-\}\colon \wedge^2\mathfrak h
  \longrightarrow \mathfrak h\otimes L_\omega^{-1}.
\]

The scalar refined convention adjoins a parameter of weight
\(\chi_\omega\):
\[
  [f,g]_\Omega=\hbar_\omega\{f,g\},
  \qquad w(\hbar_\omega)=\chi_\omega.
\]
Then
\[
  [H_I,H_J]_\Omega
  =\hbar_\omega C^K_{IJ}H_K,
  \qquad
  C^{I+J-(1,1)}_{IJ}=ad-bc,
\]
is weight-homogeneous:
\[
  w(\hbar_\omega H_K)=\chi_\omega+W_K=W_I+W_J.
\]

Jacobi survives because \(\hbar_\omega\) is central:
\[
  [[f,g]_\Omega,h]_\Omega+\mathrm{cyc}
  =
  \hbar_\omega^2
  \bigl(\{\{f,g\},h\}+\mathrm{cyc}\bigr)=0.
\]

## Equivariant CE Differential

Let
\[
  \mathfrak h_\Omega
  =
  \mathfrak h\otimes
  \C[\epsilon_s,\epsilon_1,\epsilon_2,\hbar_\omega]
\]
with bracket \([f,g]_\Omega=\hbar_\omega\{f,g\}\).  Localizing normal
weights is a separate operation; the CE/PV formulas below do not require
inverting \(\chi_\omega\).

For \(K=(r,s)\), the equivariant CE differential is
\[
  d_{\mathrm{CE},\Omega}c^K
  =
  -\frac12\hbar_\omega
  \sum_{I,J}C^K_{IJ}c^Ic^J,
\]
or in monomial coordinates,
\[
  d_{\mathrm{CE},\Omega}c^{r,s}
  =
  -\frac12\hbar_\omega
  \sum_{\substack{a+c-1=r\\ b+d-1=s}}
  (ad-bc)c^{a,b}c^{c,d}.
\]

The shifted-cotangent coordinate differential is
\[
  d_{\mathrm{CE},\Omega}u_K
  =
  \hbar_\omega
  \sum_J C^L_{KJ}u_Lc^J,
\]
equivalently
\[
  d_{\mathrm{CE},\Omega}u_{r,s}
  =
  \hbar_\omega
  \sum_{c,d}(rd-sc)
  u_{r+c-1,s+d-1}c^{c,d}.
\]
Terms with negative labels or the reduced constant \(H_{0,0}\) are
omitted, as in the non-equivariant coordinate lane.

Weight check:
\[
  w(d_{\mathrm{CE},\Omega}c^K)
  =\chi_\omega-W_I-W_J=-W_K=w(c^K),
\]
and, since \(L=K+J-(1,1)\),
\[
  w(\hbar_\omega u_Lc^J)
  =
  \chi_\omega+W_L-W_J
  =
  W_K=w(u_K).
\]
Thus \(d_{\mathrm{CE},\Omega}\) preserves \(T_\Omega\)-weight.

The square-zero proof is the old CE proof multiplied by central powers of
\(\hbar_\omega\).  On \(c\)-coordinates it is Jacobi for
\([-, -]_\Omega\).  On \(u\)-coordinates it is the coadjoint
representation identity:
\[
  [\operatorname{ad}^{\vee,\Omega}_f,
    \operatorname{ad}^{\vee,\Omega}_g]
  =
  \operatorname{ad}^{\vee,\Omega}_{[f,g]_\Omega},
  \qquad
  \operatorname{ad}^{\vee,\Omega}_f=\hbar_\omega\operatorname{ad}^{\vee}_f.
\]

## PV Differential And Compatibility

The refined linear Poisson tensor is
\[
  \pi_\Omega
  =
  \frac12\hbar_\omega C^K_{IJ}O_K\theta^I\theta^J.
\]
It is \(T_\Omega\)-invariant:
\[
  w(\hbar_\omega O_K\theta^I\theta^J)
  =
  \chi_\omega+W_K-W_I-W_J=0.
\]

The Lichnerowicz differential \(d_{\pi,\Omega}=[\pi_\Omega,-]_S\) gives
\[
  d_{\pi,\Omega}\theta^K
  =
  -\frac12\hbar_\omega C^K_{IJ}\theta^I\theta^J,
  \qquad
  d_{\pi,\Omega}O_K
  =
  \hbar_\omega C^L_{KJ}O_L\theta^J.
\]
Therefore
\[
  \Phi_\Omega d_{\mathrm{CE},\Omega}
  =
  d_{\pi,\Omega}\Phi_\Omega
\]
on \(c^K\) and \(u_K\).  Both sides are completed derivations, so the
identity extends to every finite word and then to the coordinate product
exactly as in `theorem-lanes.tex:1064-1087` and
`main.tex:3490-3536`.

For the bracketed \(P_0\) refinement there are two equivalent records of
the same line data:

1. Keep the canonical cotangent/Schouten contraction
   \[
     \{c^I,u_J\}_{\mathrm{CE}}=\delta^I_J,\qquad
     [\theta^I,O_J]_S=\delta^I_J
   \]
   for the cochain-level theorem.
2. For the refined central-operation bracket, multiply both source and
   target contractions by the same line parameter:
   \[
     \{c^I,u_J\}_{\mathrm{CE},\Omega}
       =\hbar_\omega\delta^I_J,\qquad
     [\theta^I,O_J]_{S,\Omega}
       =\hbar_\omega\delta^I_J.
   \]

The second convention is the \(L_\omega\)-weighted \(P_0\) bracket.  The
generator map remains bracket-compatible because both contractions are
scaled by the same central parameter.  Without adjoining
\(\hbar_\omega\), this is a line-valued bracket, not an ordinary scalar
\(P_0\)-bracket.

## Low-Degree Check

For \(K=(1,1)\), the non-equivariant lane gives
\[
  d_{\mathrm{CE}}u_{1,1}
  =
  2u_{0,2}c^{0,2}-2u_{2,0}c^{2,0}
  -u_{1,0}c^{1,0}+u_{0,1}c^{0,1}+\cdots .
\]
The equivariant lift is
\[
  d_{\mathrm{CE},\Omega}u_{1,1}
  =
  \hbar_\omega
  \bigl(
    2u_{0,2}c^{0,2}-2u_{2,0}c^{2,0}
    -u_{1,0}c^{1,0}+u_{0,1}c^{0,1}+\cdots
  \bigr).
\]
Each displayed term has weight
\[
  w(\hbar_\omega u_Lc^J)
  =
  \epsilon_1+\epsilon_2
  =
  w(u_{1,1}).
\]
The PV side is the same expression with \(u\mapsto O\) and
\(c\mapsto\theta\):
\[
  d_{\pi,\Omega}O_{1,1}
  =
  \hbar_\omega
  \bigl(
    2O_{0,2}\theta^{0,2}-2O_{2,0}\theta^{2,0}
    -O_{1,0}\theta^{1,0}+O_{0,1}\theta^{0,1}+\cdots
  \bigr).
\]

## Self-Dual Specialization

On
\[
  \epsilon_1+\epsilon_2=0
\]
the Poisson tensor has weight zero.  The ordinary Hamiltonian bracket
\(\{f,g\}\) is a scalar \(T_\Omega\)-equivariant bracket on
\(\mathfrak h\).  The parameter \(\hbar_\omega\) also has weight zero;
one may keep it as a central formal parameter or specialize
\(\hbar_\omega=1\) to recover the non-equivariant CE/PV formulas.

No theorem may invert \(\epsilon_1+\epsilon_2\) and then specialize to
the self-dual locus.  The self-dual branch has its own localized
coefficient ring, with only the nonzero normal characters inverted.

## Refined Line-Valued Form

Off the self-dual locus, without a chosen trivializing parameter
\(\hbar_\omega\), the correct object is Picard-graded:
\[
  \{-,-\}\colon\wedge^2\mathfrak h
  \to\mathfrak h\otimes L_\omega^{-1}.
\]
Dually, the CE differential has \(L_\omega\)-valued coefficients:
\[
  d_{\mathrm{CE},L}c^K
  \in
  L_\omega\otimes
  \widehat\Lambda^2(\mathfrak h^\vee),
  \qquad
  d_{\mathrm{CE},L}u_K
  \in
  L_\omega\otimes
  \widehat{\mathbf S}(\mathfrak h)\otimes\mathfrak h^\vee.
\]
Choosing \(\hbar_\omega\in L_\omega\) converts this line-valued CE/PV
theorem into the scalar weighted formulas above.

## Obstructions

The stable core above is a coordinate equivariant dg-algebra theorem.  It
does not close the global bracketed, kernel, QME, or trace claims.  The
open obstruction vector is:

\[
  \operatorname{Ob}_{\Omega,\mathrm{CE/PV}}
  =
  (
    \operatorname{ob}_{\Omega,\mathrm{Cartan}},
    \operatorname{ob}_{\Omega,\mathrm{top}},
    \operatorname{ob}_{\Omega,\mathrm{br}},
    \operatorname{ob}_{\Omega,\mathrm{diag}},
    \operatorname{ob}_{\Omega,\mathrm{res}},
    \operatorname{ob}_{\Omega,\mathrm{norm}},
    \operatorname{ob}_{\Omega,\mathrm{QME}}
  ).
\]

- \(\operatorname{ob}_{\Omega,\mathrm{Cartan}}\): construct the mixed
  Cartan/basic coefficient model.  Before invariants,
  \(Q_\Omega^2=L_{V_\Omega}\), not zero.
- \(\operatorname{ob}_{\Omega,\mathrm{top}}\): choose a complete
  \(T_\Omega\)-graded mixed or weighted topology in which multiplication,
  \(d_{\mathrm{CE},\Omega}\), \(d_{\pi,\Omega}\), and finite coordinate
  projections are continuous.
- \(\operatorname{ob}_{\Omega,\mathrm{br}}\): prove the refined
  cotangent/Schouten contraction is a continuous biderivation.  The
  strict coordinate product still contains divergent contractions such as
  the diagonal pairing of \(\sum_Ic^I\) with \(\sum_Iu_I\).
- \(\operatorname{ob}_{\Omega,\mathrm{diag}}\): prove convergence of the
  diagonal kernel
  \[
    \Theta_B=\sum_I H_I\otimes\theta^I+\sum_I\eta^I\otimes O_I
  \]
  in the chosen completed convolution habitat.  The \(\hbar_\omega\)
  factor does not by itself create a strict Casimir.
- \(\operatorname{ob}_{\Omega,\mathrm{res}}\): isolate zero-character
  summands and self-dual resonances.  They are fixed or residual modes,
  not denominators to be inverted.
- \(\operatorname{ob}_{\Omega,\mathrm{norm}}\): choose residue
  normalization or Euler localization and prove the comparison constant
  including the real \(s\)-orientation sign.
- \(\operatorname{ob}_{\Omega,\mathrm{QME}}\): build the equivariant
  Costello brane-defect graph package.  The CE/PV weight theorem supplies
  the coefficient algebra; it does not supply a propagator, counterterms,
  QME curvature vanishing, or physical large-\(N\) trace state.

## Claim Status

Proved in this thread: the weight assignment, the
\(\hbar_\omega\)-weighted CE formulas, and generator-level CE/PV
compatibility in the coordinate completion.

Theorem surface with named obstruction: bracketed \(P_0\), kernel, and
stratified/QME upgrades in a completed weighted habitat.

False if stated without refinement: the old scalar Hamiltonian bracket
is \(T_\Omega\)-equivariant for arbitrary
\(\epsilon_1,\epsilon_2\).
