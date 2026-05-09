# Equivariant CE/PV Refined-Bracket Completion: Construction Target

Worktree: `/Users/raeez/topological-strings`

Owned file: `reconstitution/equivariant-ce-pv-refined-bracket-completion-construction-target-2026-04-30.md`

## Verdict

The coordinate equivariant CE/PV formula is stable.  The global-completion
theorem is not yet proved.  The strongest true next theorem is a weighted
basic-Cartan CE/PV prefactorization theorem over finite normal windows, with
an exact obstruction theorem for the strict product/direct-sum endpoint and for
failure of descent to global sections.

The theorem must not be weakened to "expected global completion."  It must be
inscribed as the following construction target.

## Native Complex

For a topological open \(U\subset \mathbb R^2\) and a holomorphic polydisk
\(B\subset \mathbb C^2\), the native mixed Hamiltonian input is
\[
  \mathfrak g^{\mathrm{mix}}_{U,B,\Omega,w}
  =
  \Omega^\bullet_c(U)\widehat\otimes
  \Omega^{0,\bullet}_c(B)\widehat\otimes
  (\mathfrak h_{\Omega,w}\ltimes D_{\Omega,w}[1]),
\]
where
\[
  \mathfrak h_{\Omega,w}
  =
  \mathfrak h_w\otimes R_\Omega^{N,M},
  \qquad
  D_{\Omega,w}
  =
  \mathfrak h^{\vee,w}_{\mathrm{cont}}\otimes R_\Omega^{N,M}.
\]
Here
\[
  \mathfrak h=\mathbb C[[z_1,z_2]]/\mathbb C\cdot1,\qquad
  D=\mathfrak h^\vee_{\mathrm{cont}}\cong
  \operatorname{Ann}_{\mathrm{res}}(\mathbb C\cdot1),
\]
and the weighted pair is the Mittag-Leffler product pair of
`tate-T1-weighted-completion.tex:188-224`.

The corresponding observable object is
\[
  \mathcal F_{\Omega,w}^{\mathrm{mix}}(U\times B)
  =
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  (\mathfrak g^{\mathrm{mix}}_{U,B,\Omega,w}).
\]
This is the native \(\mathbb C^2\) holomorphic \(E_2\)-type object with
topological-current enhancement.  It is not a curve VOA, Zhu algebra, compact
BCOV theory, CoHA, Igusa/BKM object, or physical large-\(N\) state.

## Topology And Coefficients

The completion must be finite-window first:
\[
  \mathsf W_{N,M}=\{(n,a,b)\mid 0\le n\le N,\ a,b\ge0,\ 1\le a+b\le M\}.
\]
The coefficient ring is
\[
  R_\Omega^{N,M}
  =
  \mathbb C[\epsilon_s,\epsilon_1,\epsilon_2,\hbar_\omega]
  [\chi^{-1}\mid \chi\in\mathsf X_{N,M}],
\]
where only nonzero moving characters in the chosen window are inverted.  On
the self-dual branch one first imposes \(\epsilon_1+\epsilon_2=0\), then
inverts only surviving nonzero characters.

For Hamiltonian degree \(d=a+b\), use an admissible exponential weight
\[
  w(d)=q^d,\qquad q>1.
\]
The weighted coefficient pair is
\[
  \mathfrak h_w=\varprojlim_{M}\prod_{d\le M}w(d)H_d,\qquad
  \mathfrak h^{\vee,w}_{\mathrm{cont}}
  =
  \varprojlim_M\prod_{d\le M}w(d)^{-1}H_d^\vee.
\]
This changes the coefficient category.  It is not the strict continuous dual
of \(\mathfrak h_w\).  Its purpose is to make the diagonal coefficient kernel
converge:
\[
  C_{\mathfrak h,w}
  =
  \sum_{d\ge1}\sum_i
  (w(d)e_{d,i})\otimes(w(d)^{-1}e_d^i).
\]

The \(P_0\) completion requires a bracket-admissible subalgebra
\[
  B_{\Omega,w}\subset
  \mathrm{PV}_{\mathrm{coord},\Omega}
  (A_{\partial,\Omega,w})
\]
with complete Hausdorff topology, continuous inclusion into the coordinate
product, continuous multiplication, continuous \(d_{\pi,\Omega}\), and
continuous Schouten contraction bracket.  Kernel admissibility is extra: the
completed convolution target \(\mathcal K_{\Omega,w,B}\) must contain
\[
  \Theta_{\Omega,w,B}
  =
  \sum_I H_I\otimes\theta^I+\sum_I\eta^I\otimes O_I
\]
as a convergent element.

## Bracket, Divergence, And CE/PV Differential

The local volume form is
\[
  \Omega_{\mathrm{loc}}=dz_1\wedge dz_2.
\]
For \(X=a_1\partial_{z_1}+a_2\partial_{z_2}\),
\[
  \operatorname{div}_{\Omega_{\mathrm{loc}}}X
  =
  \partial_{z_1}a_1+\partial_{z_2}a_2.
\]
Hamiltonian vector fields are divergence-free:
\[
  X_f=(\partial_{z_1}f)\partial_{z_2}
      -(\partial_{z_2}f)\partial_{z_1},
  \qquad
  \operatorname{div}_{\Omega_{\mathrm{loc}}}X_f=0.
\]

For \(H_{a,b}=z_1^az_2^b\), put
\[
  W_{a,b}=a\epsilon_1+b\epsilon_2,\qquad
  \chi_\omega=\epsilon_1+\epsilon_2.
\]
The ordinary Poisson tensor has weight \(-\chi_\omega\).  Off the self-dual
locus the scalar refined bracket is therefore
\[
  [f,g]_\Omega=\hbar_\omega\{f,g\},
  \qquad w(\hbar_\omega)=\chi_\omega.
\]
In monomial coordinates,
\[
  [H_I,H_J]_\Omega
  =
  \hbar_\omega C^K_{IJ}H_K,\qquad
  C^{I+J-(1,1)}_{IJ}=ad-bc .
\]

The coordinate-dual weights are forced:
\[
  w(c^{a,b})=w(\theta^{a,b})=-W_{a,b},
  \qquad
  w(u_{a,b})=w(O_{a,b})=W_{a,b}.
\]
The equivariant CE differential is
\[
  d_{\mathrm{CE},\Omega}c^K
  =
  -\frac12\hbar_\omega C^K_{IJ}c^Ic^J,\qquad
  d_{\mathrm{CE},\Omega}u_K
  =
  \hbar_\omega C^L_{KJ}u_Lc^J.
\]
The PV tensor is
\[
  \pi_\Omega=\frac12\hbar_\omega C^K_{IJ}O_K\theta^I\theta^J,
\]
and
\[
  d_{\pi,\Omega}=[\pi_\Omega,-]_S.
\]
The generator map
\[
  \Phi_{\Omega,w}(c^I)=\theta^I,\qquad
  \Phi_{\Omega,w}(u_I)=O_I
\]
intertwines \(d_{\mathrm{CE},\Omega}\) and \(d_{\pi,\Omega}\) on finite
windows and on any completion where the displayed operations are continuous.

## Cartan / BRST Differential

The normal \(\Omega\)-background is the brane-preserving torus on
\[
  N_LX=\mathbb R_s\oplus\mathbb C_{z_1}\oplus\mathbb C_{z_2},
  \qquad t\ \text{fixed},
\]
with
\[
  V_\Omega=
  \epsilon_s s\partial_s+
  \epsilon_1z_1\partial_{z_1}+
  \epsilon_2z_2\partial_{z_2}.
\]
The mixed Cartan differential is
\[
  Q_\Omega=Q+\iota_{V_\Omega},\qquad
  Q_\Omega^2=L_{V_\Omega}.
\]
Thus the total CE/PV Cartan-BRST differentials are
\[
  D_{\mathrm{CE},\Omega}
  =
  Q_\Omega+d_{\mathrm{CE},\Omega},
  \qquad
  D_{\mathrm{PV},\Omega}
  =
  Q_\Omega+d_{\pi,\Omega}.
\]
They square to \(L_{V_\Omega}\) before passing to \(T_\Omega\)-basic
objects and square to zero on the basic/invariant subcomplex.  Any global
theorem stated as an ordinary dg theorem must either restrict to the basic
subcomplex or retain the curved Cartan package.

The normal contraction datum needed for global completion is
\[
  \mathsf C_\Omega=(\pi_L,j_L,h_\Omega),
  \qquad
  Q_\Omega h_\Omega+h_\Omega Q_\Omega
  =
  \operatorname{id}-j_L\pi_L
\]
on the localized nonresonant normal complex.  On a moving summand of character
\(\chi\), \(h_\Omega\) is the Koszul/Euler homotopy divided by \(\chi\).
Zero-character summands are not denominators; they are the residual
\(\operatorname{pr}_{\chi=0}\) sector.

## Filtration And Spectral Sequence

Use the finite-window filtration by \((N,M)\), Hamiltonian degree, normal
character, and word length.  On each finite window the CE/PV map is the finite
cotangent identity over \(R_\Omega^{N,M}\).  The inverse-limit theorem must be
proved by the spectral sequence
\[
  E_1^{p,q}=
  H^{p+q}\bigl(\operatorname{gr}_{N,M}
  \operatorname{Cone}(\Phi_{\Omega,w})\bigr)
  \Longrightarrow
  H^{p+q}\bigl(\operatorname{Cone}(\Phi_{\Omega,w})\bigr),
\]
together with the Milnor/Roos exact sequence
\[
  0\to
  \varprojlim\nolimits^1 H^{k-1}(\operatorname{Cone}\Phi_{\Omega,w}^{N,M})
  \to
  H^k(\operatorname{Cone}\Phi_{\Omega,w})
  \to
  \varprojlim H^k(\operatorname{Cone}\Phi_{\Omega,w}^{N,M})
  \to0.
\]
The finite-window cone vanishes.  The global theorem therefore reduces to
strict Mittag-Leffler compatibility, bracket continuity, basic Cartan
compatibility, and diagonal kernel convergence.  If any of these fail, the
surviving \(\varprojlim^1\), bracket, or diagonal class is the exact
obstruction theorem.

## Comparison To Factorization And Global Sections

The local maps must assemble to a natural transformation of prefactorization
objects on mixed disks:
\[
  \Phi_{\Omega,w}^{\mathrm{fact}}(U\times B)\colon
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  (\mathfrak g^{\mathrm{mix}}_{U,B,\Omega,w})
  \longrightarrow
  \mathrm{PV}_{\Omega,w}(U\times B).
\]
Compatibility to check:

1. Extension by zero for compactly supported de Rham/Dolbeault factors.
2. Disjoint factorization products.
3. The basic Cartan differential \(Q_\Omega\).
4. The refined \(L_\omega\)-weighted \(P_0\) bracket.
5. The kernel-admissible \(\Theta_{\Omega,w,B}\).
6. Residue or Euler normalization, but not both silently.

For a stratified pair \((X,L)\), the induced global-sections comparison is a
map on Weiss/Ran homotopy limits:
\[
  R\Gamma_{\mathrm{fact}}(\Phi_{\Omega,w})\colon
  \operatorname*{holim}_{U_i}
  \mathcal F_{\Omega,w}^{\mathrm{CE}}(U_i)
  \longrightarrow
  \operatorname*{holim}_{U_i}
  \mathcal F_{\Omega,w}^{\mathrm{PV}}(U_i).
\]
It is a theorem only if the descent defect
\[
  \delta_{\mathrm{Weiss}}(V,\mathcal U)=
  \mathcal F_{\Omega,w}(V)-
  \operatorname*{holim}_{U\in\mathcal U}\mathcal F_{\Omega,w}(U)
\]
vanishes in the chosen completed category.  Reduced current brackets on the
brane line do not supply this descent or the unreduced centrality homotopies.

## Exact Obstruction Vector

The obstruction vector for the global-completion theorem is
\[
  \operatorname{Ob}^{\mathrm{glob}}_{\Omega,\mathrm{CE/PV}}
  =
  (
  \operatorname{ob}_{\Omega,\mathrm{Cartan}},
  \operatorname{ob}_{\Omega,\mathrm{top}},
  \operatorname{ob}_{\Omega,\mathrm{br}},
  \operatorname{ob}_{\Omega,\mathrm{diag}},
  \operatorname{ob}_{\Omega,\mathrm{res}},
  \operatorname{ob}_{\Omega,\mathrm{norm}},
  \operatorname{ob}_{\Omega,\mathrm{fact}},
  \operatorname{ob}_{\Omega,\mathrm{Roos}},
  \operatorname{ob}_{\Omega,\mathrm{QME}}
  ).
\]

- \(\operatorname{ob}_{\Omega,\mathrm{Cartan}}\): the class of \(L_{V_\Omega}\)
  if the theorem is stated before passing to basic objects or supplying the
  localized contraction.
- \(\operatorname{ob}_{\Omega,\mathrm{top}}\): failure to specify a complete
  \(T_\Omega\)-graded topology in which multiplication, \(D_{\mathrm{CE},\Omega}\),
  \(D_{\mathrm{PV},\Omega}\), and projections are continuous.
- \(\operatorname{ob}_{\Omega,\mathrm{br}}\): failure of the refined
  cotangent/Schouten contraction to be a continuous biderivation.  The
  ambient product admits divergent contractions such as
  \(\{\sum_Ic^I,\sum_Iu_I\}=\sum_I1\).
- \(\operatorname{ob}_{\Omega,\mathrm{diag}}\): failure of the two diagonal
  sums defining \(\Theta_{\Omega,w,B}\) to converge in the specified
  completed convolution dg Lie algebra.
- \(\operatorname{ob}_{\Omega,\mathrm{res}}\): zero-character or self-dual
  resonant summands incorrectly inverted instead of retained in
  \(\operatorname{pr}_{\chi=0}\).
- \(\operatorname{ob}_{\Omega,\mathrm{norm}}\): no comparison between residue
  normalization \(\nu_\Omega^{\mathrm{res}}=1\) and Euler normalization
  \(\nu_\Omega^{\mathrm{Eu}}=\sigma_s(\epsilon_s\epsilon_1\epsilon_2)^{-1}\).
- \(\operatorname{ob}_{\Omega,\mathrm{fact}}\): failure of prefactorization,
  associativity, collar, or Weiss descent identities.
- \(\operatorname{ob}_{\Omega,\mathrm{Roos}}\): a nonzero
  \(\varprojlim^1\) class for compatible finite-window primitives, brackets,
  kernels, or descent homotopies.
- \(\operatorname{ob}_{\Omega,\mathrm{QME}}\): separate Costello
  brane-defect graph/QME obstruction.  It is outside the coordinate CE/PV
  stable core but blocks any claim that the completed CE/PV package already
  gives a physical brane-defect quantum theory.

## Attack-Heal Conclusion

Stable core: the \(\hbar_\omega\)-weighted coordinate CE/PV theorem and its
finite-window weighted versions.

Healed theorem target: the weighted basic-Cartan CE/PV prefactorization theorem
with bracket-admissible \(B_{\Omega,w}\), kernel-admissible
\(\mathcal K_{\Omega,w,B}\), finite-window spectral sequence, and Weiss/Roos
descent gate.

Exact obstruction theorem if still open: the strict product/direct-sum endpoint
has no global Casimir or contraction bracket; the global theorem is blocked by
the displayed \(\operatorname{Ob}^{\mathrm{glob}}_{\Omega,\mathrm{CE/PV}}\).

## Anchors

- `CLAUDE.md:24-76`: local model, native \(\mathbb C^2\) object, normal
  \(\Omega\)-discipline.
- `local-dictionary.tex:28-122`: local volume, divergence, BV pairing,
  residue/cyclic density.
- `local-dictionary.tex:420-666`: \(V_\Omega\), \(Q_\Omega\), normal
  localization ring, contraction datum, refined bracket, normalization,
  stratified factorization obstruction vector.
- `theorem-lanes.tex:227-379`: local chiral/factorization taxonomy.
- `theorem-lanes.tex:382-515`: native holomorphic factorization algebra and
  semidirect collision formulas.
- `theorem-lanes.tex:1180-1271`: coordinate product, bracket-admissible and
  kernel-admissible completions, \(E_q\) topology.
- `theorem-lanes.tex:1489-1658`: equivariant refined CE/PV coordinate formula
  and obstruction boundary.
- `theorem-lanes.tex:1660-1752`: abstract bracket-compatible CE/PV recognition
  criterion.
- `theorem-lanes.tex:2671-2883`: normal \(\Omega\) weighted kernels and QME
  boundary.
- `open-obligations.tex:674-888`: stratified brane prefactorization,
  descent, centrality, and QME obstruction data.
- `tate-T1-weighted-completion.tex:128-224`: admissible weights and weighted
  coefficient pair.
- `tate-T1-weighted-completion.tex:227-347`: Casimir convergence and
  heat-kernel extension in the weighted pair.
- `tate-T1-weighted-completion.tex:370-605`: equivariant finite normal window,
  localized kernel, denominator, and QME boundary.
- `tate-T1-weighted-completion.tex:2785-3000`: strict unweighted endpoint
  obstruction and finite-window CE/PV stabilization.
- `/Users/raeez/chiral-bar-cobar-vol2/notes/first_principles_cache_comprehensive.md:10964-11033`:
  control-surface patterns 490--500 on PBW, CE/PV, Casimir, unreduced
  factorization, QME, global descent, and named habitats.
