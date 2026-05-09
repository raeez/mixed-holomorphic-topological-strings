# Omega Physical Large-N State Construction Target

Status: construction theorem target with exact obstruction vector.  This
file separates three layers which must not be identified:

1. algebraic stable trace invariant theory;
2. finite-window equivariant coefficient rings for normal localization;
3. physical BV/correlator large-N states.

Only the third layer is a physical trace-state theorem.

## Anchors

- `CLAUDE.md`: normal `Omega` discipline and the warning that localization
  does not prove physical large-N trace asymptotics.
- `AGENTS.md`: normal torus on
  `N_LX = R_s \oplus C_{z_1}\oplus C_{z_2}` with `t` fixed.
- `local-dictionary.tex:377-664`: normal `Omega` dictionary, coefficient
  ring, weights, parameter branches, residue/Euler normalization, and
  obstruction vector.
- `open-obligations.tex:687-999`: stratified brane datum, trace-state
  datum, Ward identities, cumulants, expansion, and obstruction vector.
- `theorem-lanes.tex:2836-3079`: stratified trace and physical
  `Omega`-large-N criterion.
- `appendix-unreduced-bv-qme.tex:2487-2835`: equivariant finite-window
  Costello/QME habitat and scalar/non-scalar obstruction criterion.
- `appendix-unreduced-bv-qme.tex:3431-3555`: `Q_Omega` centrality
  homotopy criterion.
- `appendix-factorization-current-conventions.tex:697-788`: algebraic
  `Omega`-weighted current brackets and QME firewall.
- `main.tex:6380-6985`: algebraic stable trace, Capelli
  triangularization, and connected trace projection.
- `main.tex:7402-7565`: Hamiltonian Costello specialization requirements.
- `main.tex:7733-8125`: componentwise quantum coefficient surface and
  non-scalar QME obstruction.
- `appendix-radial-parts-moyal.tex:1239-1338`: stable connected cumulant
  extraction for the algebraic trace target.

## Notation Gate

Use different symbols for rank and finite windows.

The matrix rank is \(N_{\mathrm{rk}}\).  A finite normal/Hamiltonian
window is \((N_{\mathrm{win}},M)\).  The window coefficient ring is
\[
  R_\Omega^{N_{\mathrm{win}},M}
  =
  \mathbb C[\epsilon_s,\epsilon_1,\epsilon_2,\hbar_\omega]
  [\chi^{-1}\mid \chi\in\mathsf X_{N_{\mathrm{win}},M}],
\]
where \(\mathsf X_{N_{\mathrm{win}},M}\) contains the nonzero moving
characters occurring in the window, including
\[
  n\epsilon_s+a\epsilon_1+b\epsilon_2,\qquad
  n\epsilon_s-a\epsilon_1-b\epsilon_2.
\]
This ring is a coefficient habitat.  It is not a state, not a trace, and
not a convergence theorem.  A field-valued version may replace it by a
declared \(K_\Omega\) or an all-character localization, but only after
the required small-denominator and compatibility theorem is named.

The normal torus is
\[
  T_\Omega=
  \mathbb C^*_{\epsilon_s}\times
  \mathbb C^*_{\epsilon_1}\times
  \mathbb C^*_{\epsilon_2},
  \qquad
  V_\Omega=
  \epsilon_s s\partial_s+
  \epsilon_1 z_1\partial_{z_1}+
  \epsilon_2 z_2\partial_{z_2},
  \qquad V_\Omega(t)=0.
\]
The Cartan operator is
\[
  Q_\Omega=Q+\iota_{V_\Omega},\qquad
  Q_\Omega^2=L_{V_\Omega}.
\]
Thus every differential statement is made on the invariant/basic Cartan
complex, or else it keeps the \(L_{V_\Omega}\)-curvature.

The three parameters are separate:
\[
  \hbar_{\mathrm{QME}},\qquad
  \hbar_{\mathrm W},\qquad
  \hbar_\omega .
\]
Here \(\hbar_{\mathrm{QME}}\) counts BV/Costello graph order,
\(\hbar_{\mathrm W}\) deforms the Weyl/Moyal brane algebra, and
\(\hbar_\omega\) scalarizes the equivariant Hamiltonian bracket.  A Weyl
branch may set \(\hbar_{\mathrm W}=\hbar_\omega\).  No branch identifies
either with \(\hbar_{\mathrm{QME}}\) without a separate QME theorem.

## Attack Result

The false surface is:

\[
  \text{stable trace generators}
  +
  R_\Omega^{N_{\mathrm{win}},M}
  \quad\Longrightarrow\quad
  \text{physical Omega-large-N state}.
\]

The implication is false.  Stable trace theory supplies algebraic labels
for single-trace generators after scalar reduction, connected projection,
and Capelli triangularization.  The finite-window ring only says which
normal weights may be inverted in a localized equivariant complex.  A
physical state additionally requires a continuous BV/BRST correlation
functional, a trace normalization, Ward identities, a completed cumulant
topology, and an asymptotic large-N theorem.

The algebraic current brackets are also not enough.  They are
support-local current identities.  A physical trace theorem needs the
brane-defect Costello QME kernel, scalar projection, non-scalar
counterterms, centrality homotopies, and trace-state compatibility.

## Target Theorem Data

The theorem to construct is a compatible family
\[
  \mathfrak T_{N_{\mathrm{rk}},\Omega}^{N_{\mathrm{win}},M}
\]
over ranks \(N_{\mathrm{rk}}\) and windows \((N_{\mathrm{win}},M)\),
or an all-window replacement with a declared coefficient field, consisting
of the following data.

### 1. Normal Cartan Package

Construct the mixed Cartan/basic complex and localized normal contraction
\[
  \mathsf C_\Omega=(\pi_L,j_L,h_\Omega)
\]
with
\[
  \pi_Lj_L=\operatorname{id},\qquad
  Q_\Omega h_\Omega+h_\Omega Q_\Omega
  =
  \operatorname{id}-j_L\pi_L
\]
on the localized invariant normal complex.  On a nonzero weight
\(\chi\)-summand, \(h_\Omega\) divides the Euler/Koszul homotopy by
\(\chi\).  On the self-dual branch, impose
\(\epsilon_1+\epsilon_2=0\) first and invert only the surviving nonzero
characters.

### 2. Stratified Brane Object

Construct a stratified prefactorization algebra
\[
  \mathcal F^{\mathrm{str}}_{\Omega,N_{\mathrm{rk}}}\colon
  \operatorname{Disk}^{\mathrm{str}}_{X,L}
  \longrightarrow
  \operatorname{Ch}_{R_\Omega^{N_{\mathrm{win}},M}
  [[\hbar_{\mathrm{QME}}]]}
\]
for
\[
  X=\mathbb R_t\times\mathbb R_s\times\mathbb C^2_{z_1,z_2},
  \qquad
  L=\mathbb R_t\times\{s=z_1=z_2=0\}.
\]
Its values include bulk mixed HT disks, brane intervals, and collars
meeting \(L\).  It carries products, collar module maps, stratified
descent, and product/\(P_0\)-centrality homotopies against unreduced brane
observables.

### 3. Brane Algebra Branch

The finite-rank physical branch is the derived BRST quantum Hamiltonian
reduction
\[
  A^q_{N_{\mathrm{rk}},\Omega,\lambda}
  =
  \operatorname{Weyl}_{\hbar_{\mathrm W,N_{\mathrm{rk}}}}
  (\operatorname{Mat}_{N_{\mathrm{rk}}}^2)
  /\!\!/_{\hbar_{\mathrm W,N_{\mathrm{rk}}}} GL_{N_{\mathrm{rk}}},
\]
with the 't Hooft scaling
\[
  \lambda=N_{\mathrm{rk}}\hbar_{\mathrm W,N_{\mathrm{rk}}},
  \qquad
  \hbar_{\mathrm W,N_{\mathrm{rk}}}=\lambda/N_{\mathrm{rk}},
\]
and quantum moment equation
\[
  YX-XY+\lambda I=0.
\]
Weights are
\[
  w(X)=\epsilon_1,\qquad
  w(Y)=\epsilon_2,\qquad
  w(\hbar_{\mathrm W})=\epsilon_1+\epsilon_2,\qquad
  w(\lambda)=\epsilon_1+\epsilon_2.
\]

The stable principal-part branch is a different branch.  It uses
\(A^{\mathrm{pp},w}_{\partial,\Omega,\hbar_{\mathrm W}}(I)\).  A
physical theorem must choose the finite branch, choose the stable branch,
or construct a comparison map between them.

### 4. BV/QME Differential

Construct the renormalized brane-defect differential
\[
  D_{N_{\mathrm{rk}},\Omega}
  =
  Q_\Omega+
  \{I_{N_{\mathrm{rk}},\Omega},-\}_{\hbar_{\mathrm W,N_{\mathrm{rk}}}}
  +
  \hbar_{\mathrm{QME}}\Delta_{N_{\mathrm{rk}},\Omega}
\]
on the chosen BRST/BV lift.  The QME requirement is
\[
  D_{N_{\mathrm{rk}},\Omega}^2=0.
\]
Equivalently, the brane-defect kernel and counterterms must satisfy
\[
  \operatorname{Curv}(K_{\Omega,N_{\mathrm{rk}}})
  =
  d_{\mathrm{QME}}K_{\Omega,N_{\mathrm{rk}}}
  +\frac12[K_{\Omega,N_{\mathrm{rk}}},
          K_{\Omega,N_{\mathrm{rk}}}]_{\hbar_{\mathrm{QME}}}
  =0.
\]

### 5. State

A physical trace state is a continuous degree-zero cyclic functional
\[
  \omega_{N_{\mathrm{rk}},\Omega}\colon
  A^q_{N_{\mathrm{rk}},\Omega,\lambda}
  \longrightarrow
  R_\Omega^{N_{\mathrm{win}},M}[[\hbar_{\mathrm{QME}},\lambda]]
\]
or a state on
\[
  \int_{L\subset X}\mathcal F^{\mathrm{str}}_{\Omega,N_{\mathrm{rk}}}.
\]
It must come from a continuous BRST/BV lift
\[
  \widetilde\omega_{N_{\mathrm{rk}},\Omega}\colon
  \mathcal A^{\mathrm{BRST/BV}}_{N_{\mathrm{rk}},\Omega,\lambda}
  \longrightarrow
  R_\Omega^{N_{\mathrm{win}},M}[[\hbar_{\mathrm{QME}},\lambda]]
\]
with
\[
  D_{N_{\mathrm{rk}},\Omega}^\vee
  \widetilde\omega_{N_{\mathrm{rk}},\Omega}=0.
\]
It also annihilates the derived moment ideal and infinitesimal gauge
action:
\[
  \widetilde\omega_{N_{\mathrm{rk}},\Omega}(\widehat\mu(\xi)F)=0,
  \qquad
  \widetilde\omega_{N_{\mathrm{rk}},\Omega}(\xi\cdot F)=0.
\]
Cyclicity means
\[
  \omega(FG)=(-1)^{|F||G|}\omega(GF)
\]
for the represented \(E_1\) brane product or its factorization-homology
trace.  If an ordered non-cyclic state is chosen, the theorem is no
longer a trace theorem; it becomes an ordered-correlator theorem.

### 6. Trace Normalization

The normalization datum is
\[
  \nu_{N_{\mathrm{rk}},\Omega}
  =
  (
    \omega_{N_{\mathrm{rk}},\Omega}(1)=1,\;
    O_{0,0}^{(N_{\mathrm{rk}})}=\operatorname{Tr}(I)=N_{\mathrm{rk}},\;
    \lambda=N_{\mathrm{rk}}\hbar_{\mathrm W,N_{\mathrm{rk}}},\;
    \nu_\Omega
  ).
\]
The normal branch is one of
\[
  \nu_\Omega^{\mathrm{res}}=1,
\]
or
\[
  \nu_\Omega^{\mathrm{Eu}}
  =
  \sigma_s(\epsilon_s\epsilon_1\epsilon_2)^{-1},
\]
or an explicitly named Euler-rescaled residue convention
\[
  \nu_\Omega^{\mathrm{Eres}}
  =
  \sigma_s(\epsilon_s\epsilon_1\epsilon_2)^{-1}.
\]
Plain residue normalization never contains the Euler denominator
silently.  The sign \(\sigma_s\) is part of the theorem data.

The trace-coordinate branch must also be fixed.  The natural quantum
single-trace coordinates are the Capelli-renormalized Weyl traces
\[
  J_{N_{\mathrm{rk}}}(f)
  =
  \operatorname{Tr}\operatorname{Op}_{\mathrm W}(f)(X,Y).
\]
If the normal-ordered traces
\[
  O_{a,b}^{(N_{\mathrm{rk}})}=\operatorname{Tr}(X^aY^b)
\]
are used instead, the theorem must include the triangular comparison
\[
  J_{N_{\mathrm{rk}}}(z_1^az_2^b)
  \equiv
  \sum_{r=0}^{\min(a,b)}
    \left(-\frac{\lambda}{2}\right)^r
    r!\binom ar\binom br\,
    O_{a-r,b-r}^{(N_{\mathrm{rk}})}
\]
modulo the quantum moment ideal.  A naive normal-ordered trace basis is
not enough, because the Capelli contact term can produce nonempty
connected traces.

### 7. Trace-Test Topology

For a chosen trace coordinate family \(\tau_\alpha^{(N_{\mathrm{rk}})}\),
where \(\alpha=(a,b)\) or a polynomial Hamiltonian label, define
\[
  \mathscr T_+
  =
  R_\Omega^{N_{\mathrm{win}},M}
  [[\hbar_{\mathrm{QME}},\lambda]]
  [[p_\alpha\mid \alpha\ne0]]
\]
with product topology by:

- trace degree;
- \(\lambda\)-adic order;
- \(\hbar_{\mathrm{QME}}\)-adic order;
- finite-window equivariant Laurent coefficient;
- Weyl/Moyal order filtration when the branch uses \(\hbar_{\mathrm W}\);
- quotient topology by the closed BRST quantum moment ideal.

The evaluation map is continuous:
\[
  \pi_{N_{\mathrm{rk}}}\colon
  \mathscr T_+
  \longrightarrow
  A^q_{N_{\mathrm{rk}},\Omega,\lambda},
  \qquad
  p_\alpha\longmapsto\tau_\alpha^{(N_{\mathrm{rk}})}.
\]
For the brane-line theory use smeared insertions
\[
  \tau_\alpha^{(N_{\mathrm{rk}})}(\varphi)
  =
  \int_L
  \varphi(t)\tau_\alpha^{(N_{\mathrm{rk}})}(t)\,dt.
\]
Then cumulant coefficients lie in
\[
  \mathcal D'(L^k)\widehat\otimes
  R_\Omega^{N_{\mathrm{win}},M}
  [[\hbar_{\mathrm{QME}},\lambda]]
\]
with the weak distributional topology against compactly supported test
functions.

### 8. Connected Cumulants

The partition functional is
\[
  Z_{N_{\mathrm{rk}},\Omega}(J)
  =
  \omega_{N_{\mathrm{rk}},\Omega}
  \left(
    \exp\left(\sum_\alpha
      J_\alpha\tau_\alpha^{(N_{\mathrm{rk}})}\right)
  \right),
  \qquad
  Z_{N_{\mathrm{rk}},\Omega}(0)=1.
\]
The logarithm is taken in the completed augmentation ideal.  Connected
cumulants are
\[
  \langle F_1,\ldots,F_k\rangle^c_{N_{\mathrm{rk}},\Omega}
  =
  [t_1\cdots t_k]\,
  \log
  \omega_{N_{\mathrm{rk}},\Omega}
  \left(
    \exp\left(\sum_i t_iF_i\right)
  \right).
\]
The empty trace \(O_{0,0}=N_{\mathrm{rk}}\) is treated by
\(\nu_{N_{\mathrm{rk}},\Omega}\), not as a primitive Hamiltonian
insertion.

### 9. Large-N Topology And Convergence

The large-N topology \(\mathcal T_\Omega\) is coefficientwise
Poincare-asymptotic in \(N_{\mathrm{rk}}^{-2}\).  A sequence
\(c_{N_{\mathrm{rk}}}\) of coefficients has expansion
\[
  c_{N_{\mathrm{rk}}}
  \sim
  \sum_{g\ge0}
  N_{\mathrm{rk}}^{\alpha-2g}c_g
\]
if, after fixing every trace tuple, every
\((\lambda,\hbar_{\mathrm{QME}})\)-order, every finite-window
equivariant Laurent monomial, and every distributional test functional
when insertions are smeared, the coefficient sequence has the displayed
Poincare expansion.  No analytic all-window convergence is asserted
unless a separate \(q\)-moderate small-denominator theorem is supplied.

For unnormalized single traces the physical genus expansion is
\[
  \langle
    \tau_{\alpha_1}^{(N_{\mathrm{rk}})},\ldots,
    \tau_{\alpha_k}^{(N_{\mathrm{rk}})}
  \rangle^c_{N_{\mathrm{rk}},\Omega}
  \sim
  \sum_{g\ge0}
  N_{\mathrm{rk}}^{2-2g-k}
  F^\Omega_{g;k}(\alpha_1,\ldots,\alpha_k).
\]
If normalized traces \(N_{\mathrm{rk}}^{-1}\tau_\alpha\) are chosen, the
power of \(N_{\mathrm{rk}}\) changes by \(k\).  The theorem must state
which convention it uses.

### 10. Ward Identities

The state must satisfy the Ward identities in the chosen completed
BRST/BV complex:
\[
  \omega_{N_{\mathrm{rk}},\Omega}
  (D_{N_{\mathrm{rk}},\Omega}F)=0,
\]
\[
  \omega_{N_{\mathrm{rk}},\Omega}(Q_\Omega F)=0
  \quad\text{on the invariant/basic complex},
\]
\[
  \omega_{N_{\mathrm{rk}},\Omega}(\widehat\mu(\xi)F)=0,
  \qquad
  \omega_{N_{\mathrm{rk}},\Omega}(\xi\cdot F)=0,
\]
and
\[
  \omega_{N_{\mathrm{rk}},\Omega}
  (\operatorname{Curv}(K_{\Omega,N_{\mathrm{rk}}})F)=0.
\]
For connected cumulants this gives
\[
  \langle
    D_{N_{\mathrm{rk}},\Omega}G,F_1,\ldots,F_k
  \rangle^c_{N_{\mathrm{rk}},\Omega}=0
\]
and the analogous \(Q_\Omega\), moment-map, and curvature identities.
If \(\operatorname{Curv}(K_{\Omega,N_{\mathrm{rk}}})\ne0\), the last
expression is the Ward anomaly.  Stable trace invariant theory does not
remove it.

## Obstruction Vector

The physical theorem is closed exactly when the following obstruction
vector vanishes:
\[
  \operatorname{Ob}_{\Omega,\mathrm{phys}}
  =
  (
    \operatorname{ob}_{\Omega,\mathrm{Cartan}},
    \operatorname{ob}_{\Omega,\mathrm{contr}},
    \operatorname{ob}_{\Omega,\mathrm{coeff}},
    \operatorname{ob}_{\mathrm{str}},
    \operatorname{ob}_{\mathrm{red}},
    \operatorname{ob}_{\mathrm{branch}},
    \operatorname{ob}_{\mathrm{state}},
    \operatorname{ob}_{\mathrm{norm}},
    \operatorname{ob}^{\mathrm{sc}}_{\mathrm{QME}},
    \operatorname{ob}^{\mathrm{ns}}_{\mathrm{QME}},
    \operatorname{ob}_{\mathrm{cent}},
    \operatorname{ob}_{\mathrm{Ward}},
    \operatorname{ob}_{\mathrm{cum}},
    \operatorname{ob}_{\mathrm{asymp}},
    \operatorname{ob}_{\mathrm{src}}
  ).
\]

Definitions:

- \(\operatorname{ob}_{\Omega,\mathrm{Cartan}}\): failure to construct the
  mixed Cartan/basic model with \(Q_\Omega^2=L_{V_\Omega}\) handled
  correctly.
- \(\operatorname{ob}_{\Omega,\mathrm{contr}}\): failure to construct
  \((\pi_L,j_L,h_\Omega)\) after inverting nonzero normal weights, or
  failure of the self-dual no-inversion guard.
- \(\operatorname{ob}_{\Omega,\mathrm{coeff}}\): failure to choose
  \(R_\Omega^{N_{\mathrm{win}},M}\), a compatible inverse system, or a
  declared \(K_\Omega\) with all needed normal characters and
  small-denominator controls.
- \(\operatorname{ob}_{\mathrm{str}}\): failure of stratified products,
  collar module maps, associativity, or Weiss descent for
  \(\mathcal F^{\mathrm{str}}_{\Omega,N_{\mathrm{rk}}}\).
- \(\operatorname{ob}_{\mathrm{red}}\): failure of the derived quantum
  Hamiltonian reduction, including nonclosed BRST moment ideal or
  unjustified passage to an underived invariant quotient.
- \(\operatorname{ob}_{\mathrm{branch}}\): failure to choose and compare
  the finite-rank brane algebra branch, the stable principal-part branch,
  and the trace-coordinate branch \(J_N\) versus \(O_{a,b}\).
- \(\operatorname{ob}_{\mathrm{state}}\): the dual cohomology class
  \[
    [D_{N_{\mathrm{rk}},\Omega}^{\vee}
      \widetilde\omega_{N_{\mathrm{rk}},\Omega}]
  \]
  in the continuous dual BRST/BV complex, together with failure to
  annihilate moment-map and gauge-action terms.
- \(\operatorname{ob}_{\mathrm{norm}}\): unresolved empty trace, 't
  Hooft scaling, \(\hbar\)-branch, residue/Euler branch, Euler sign
  \(\sigma_s\), or Capelli triangular normalization.
- \(\operatorname{ob}^{\mathrm{sc}}_{\mathrm{QME}}\): scalar-contact QME
  obstruction.  In the ordinary scalar-reduced branch the Capelli scalar
  class is
  \[
    \hbar_{\mathrm W,N_{\mathrm{rk}}}N_{\mathrm{rk}}[\bar c]
    =
    \lambda[\bar c],
  \]
  while the Costello scalar-symbol test uses the selected
  \(\nu_\Omega\) and \(\hbar_{\mathrm{QME}}\) branch.  These must be
  reconciled by an explicit scalar branch theorem.
- \(\operatorname{ob}^{\mathrm{ns}}_{\mathrm{QME}}\): the non-scalar
  brane-defect obstruction
  \[
    [\operatorname{Ob}^{\mathrm{red}}]
    \in
    H^1(\ker\widehat\sigma_{\mathrm{sc}},d_{\mathrm{QME}})
  \]
  plus finite-window obstruction pairs
  \[
    \mathfrak O_n^{\mathrm{ns}}
    =
    (([\mathfrak o^{\mathrm{ns}}_{n,\Omega,M}])_M,
    \lambda_{n,\Omega}).
  \]
- \(\operatorname{ob}_{\mathrm{cent}}\): failure of product and
  \(P_0\)-centrality homotopies, including the secondary
  \([L_{V_\Omega}H]\) obstruction before passing to basic primitives.
- \(\operatorname{ob}_{\mathrm{Ward}}\): nonzero \(D\), \(Q_\Omega\),
  moment-map, gauge-action, or curvature Ward functional.
- \(\operatorname{ob}_{\mathrm{cum}}\): failure of the exponential,
  logarithm, cumulant extraction, trace identities, or empty-trace
  treatment in the completed trace-test topology.
- \(\operatorname{ob}_{\mathrm{asymp}}\): for some trace tuple and
  truncation \(G\), the remainder
  \[
    N_{\mathrm{rk}}^{k-2}
    C^\Omega_{N_{\mathrm{rk}};k}
    -
    \sum_{0\le g<G}
      N_{\mathrm{rk}}^{-2g}F^\Omega_{g;k}
  \]
  fails to be \(O(N_{\mathrm{rk}}^{-2G})\) coefficientwise in
  \(\mathcal T_\Omega\).  Equivalently, its sequence class is nonzero in
  the quotient by \(N^{-2}\)-Poincare-asymptotic sequences.
- \(\operatorname{ob}_{\mathrm{src}}\): use of external Costello,
  factorization-homology, Chern-Simons, compact Calabi-Yau, Vol III, or
  physical large-N analogy without a primary-source fixture and a
  matched-conventions morphism to the local pair \((X,L)\).

## Stable Core

The stable core is a theorem target:

\[
  \text{physical Omega-large-N trace state}
  =
  \text{continuous BV/QME state}
  +
  \text{normalization}
  +
  \text{Ward identities}
  +
  \text{connected cumulant topology}
  +
  \text{coefficientwise }N^{-2}\text{ asymptotics}.
\]

Stable trace invariant theory supplies only algebraic labels.  The
finite-window coefficient ring supplies only the normal localization
habitat.  Neither supplies the physical state.
