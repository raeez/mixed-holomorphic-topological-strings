# Physical \(\Omega\)-Large-\(N\) Trace-State Thread

Status: theorem-surface with missing construction.  The algebraic stable
trace theorem supplies candidate single-trace generators.  It does not
construct a physical state, a cumulant topology, a QME Ward functional, or
the genus expansion.  The strongest admissible formulation is therefore a
criterion: a physical \(\Omega\)-large-\(N\) trace theorem is exactly the
vanishing of the obstruction vector below, after the stated data have been
constructed.

Anchors used:

- `CLAUDE.md`: normal \(\Omega\)-background discipline and warning that
  \(\Omega\) does not prove physical large-\(N\) trace asymptotics.
- `AGENTS.md`: normal torus
  \(N_LX=\mathbb R_s\oplus\mathbb C_{z_1}\oplus\mathbb C_{z_2}\), with
  \(t\) fixed.
- `main.tex:1443-1520`: stable large-\(N\) means degreewise invariant
  stabilization, not physical large \(N\).
- `main.tex:4704-4780`: stable brane Hamiltonian algebra and the three
  large-\(N\) operations.
- `open-obligations.tex:520-735`: stratified brane datum, trace-state
  datum, Ward identities, cumulants, expansion, and obstruction vector.
- `claim-strength-ledger.tex:355-479`: normal \(\Omega\), protected trace,
  Costello QME, and physical \(\Omega\)-large-\(N\) controller rows.

## 1. Fixed Local Input

The local space is
\[
  X=\mathbb R_t\times\mathbb R_s\times\mathbb C^2_{z_1,z_2},
  \qquad
  L=\mathbb R_t\times\{s=z_1=z_2=0\}.
\]
The brane-preserving torus is
\[
  T_\Omega
  =
  \mathbb C^*_{\epsilon_s}\times
  \mathbb C^*_{\epsilon_1}\times
  \mathbb C^*_{\epsilon_2},
\]
acting on \(s,z_1,z_2\) and fixing \(t\).  Its vector field is
\[
  V_\Omega
  =
  \epsilon_s s\partial_s
  +\epsilon_1 z_1\partial_{z_1}
  +\epsilon_2 z_2\partial_{z_2},
  \qquad
  Q_\Omega=Q+\iota_{V_\Omega},
  \qquad
  Q_\Omega^2=L_{V_\Omega}.
\]
Thus every differential claim is either made on the invariant/basic
Cartan complex or includes the \(L_{V_\Omega}\)-curvature.  This is the
first gate.  A literal rotation in the \((t,s)\)-plane is not the native
brane-preserving datum.

The finite-\(N\) brane algebra branch is the derived equivariant quantum
Hamiltonian reduction
\[
  A^q_{N,\Omega}
  =
  \operatorname{Weyl}_{\hbar_N}(\operatorname{Mat}_N^2)
  /\!\!/_{\hbar_N} GL_N,
\]
with
\[
  \widehat\mu(\xi)
  =
  \operatorname{Tr}\!\left(\xi(YX-XY+\hbar_N N I)\right),
  \qquad
  w(X)=\epsilon_1,\quad
  w(Y)=\epsilon_2,\quad
  w(\hbar_N)=\epsilon_1+\epsilon_2.
\]
The robust definition is the BRST derived reduction.  The underived
presentation
\[
  \left(
  \operatorname{Weyl}_{\hbar_N}(\operatorname{Mat}_N^2)
  /
  \operatorname{Weyl}_{\hbar_N}\widehat\mu(\mathfrak{gl}_N)
  \right)^{GL_N}
\]
is an extra exactness statement and must not be assumed silently.

For the physical genus expansion requested here, fix the 't Hooft
normalization
\[
  \lambda=N\hbar_N,\qquad \hbar_N=\lambda/N.
\]
Then the quantum moment equation is
\[
  YX-XY+\lambda I=0,
\]
and \(w(\lambda)=\epsilon_1+\epsilon_2\).  A fixed-\(\hbar\) theory is a
different two-parameter asymptotic problem; it is not the
\(N^{2-2g-k}\) theorem surface unless a comparison theorem converts it to
the above scaling.

## 2. Coefficient Ring And Normalization

Choose one normalization branch:
\[
  R_\Omega^{\mathrm{res}}
  =
  \mathbb C((\epsilon_s,\epsilon_1,\epsilon_2))[[\lambda]]
\]
for residue-normalized brane variables, or
\[
  R_\Omega^{\mathrm{Eul}}
  =
  e_{T_\Omega}(N_LX)^{-1}R_\Omega^{\mathrm{res}},
  \qquad
  e_{T_\Omega}(N_LX)^{-1}
  =
  (\epsilon_s\epsilon_1\epsilon_2)^{-1},
\]
for Euler-localized variables.  These are not the same convention.  A
physical theorem chooses one, or supplies an explicit comparison
\[
  C_{\mathrm{res}\to\mathrm{Eul}}\colon
  R_\Omega^{\mathrm{res}}\to R_\Omega^{\mathrm{Eul}}
\]
with its sign, orientation, and insertion-count rule.  Until this is
done, the normalizing factor is an obstruction, not notation.

The empty trace is fixed by
\[
  O_{0,0}^{(N)}=\operatorname{Tr}(I_N)=N.
\]
It is not a primitive Hamiltonian insertion.  The physical trace tests are
\[
  O_{a,b}^{(N)}
  =
  \operatorname{Tr}(X^aY^b),
  \qquad
  a,b\ge0,\quad a+b>0,
\]
with the displayed normal ordering.  A different word ordering is another
observable unless the quantum moment relation, centrality homotopies, and
finite-\(N\) trace identities identify it in the chosen quotient.

## 3. State On \(A^q_{N,\Omega}\)

A physical \(\Omega\)-trace state at rank \(N\) is not a positive Hilbert
state.  The fields include BV and BRST variables.  It is a continuous
degree-zero cyclic correlation functional
\[
  \omega_{N,\Omega}\colon
  A^q_{N,\Omega,\lambda}
  \longrightarrow
  R_\Omega
\]
obtained from a continuous BRST/BV lift
\[
  \widetilde\omega_{N,\Omega}\colon
  \mathcal A^{\mathrm{BRST}}_{N,\Omega,\lambda}
  \longrightarrow
  R_\Omega.
\]
The lift is part of the data.  It must satisfy:
\[
  \widetilde\omega_{N,\Omega}(D_{N,\Omega}F)=0,
\]
\[
  \widetilde\omega_{N,\Omega}(\widehat\mu(\xi)F)=0,
  \qquad
  \widetilde\omega_{N,\Omega}(\xi\cdot F)=0,
\]
\[
  \widetilde\omega_{N,\Omega}(L_{V_\Omega}F)=0,
  \qquad
  \widetilde\omega_{N,\Omega}(Q_\Omega F)=0
  \quad\text{on the invariant/basic complex},
\]
and the cyclic/factorization trace condition
\[
  \omega_{N,\Omega}(FG)
  =
  (-1)^{|F||G|}\omega_{N,\Omega}(GF)
\]
whenever \(F,G\) lie in the \(E_1\) brane algebra represented by the
chosen factorization-homology trace.  If a non-cyclic ordered state is
chosen instead, the theorem surface changes: the cumulants become
ordered correlators, not trace cumulants.

Here
\[
  D_{N,\Omega}
  =
  Q_\Omega+\{I_{N,\Omega},-\}_{\hbar_N}
  +\hbar_N\Delta_{N,\Omega}
\]
is the renormalized BV/QME differential on the full brane-defect complex.
The expression only makes sense after the equivariant propagator,
counterterms, scalar projection, and non-scalar kernel complex have been
constructed.  If \(D_{N,\Omega}^2\ne0\), the state cannot enter the stable
core.

The normalization datum is
\[
  \nu_{N,\Omega}
  =
  (\omega_{N,\Omega}(1)=1,\ O_{0,0}^{(N)}=N,\ \lambda=N\hbar_N,\
  \nu_\Omega^{\mathrm{res}}\ \text{or}\ \nu_\Omega^{\mathrm{Eul}}).
\]

## 4. Topology

The finite-\(N\) algebra is completed in the combined topology generated
by:

1. the \(\lambda\)-adic filtration after substituting
   \(\hbar_N=\lambda/N\);
2. the order filtration on the Weyl algebra;
3. the \(T_\Omega\)-weight decomposition after localizing nonzero normal
   weights;
4. the quotient topology by the closed BRST quantum moment ideal.

The trace-test algebra is
\[
  \mathscr T_+
  =
  R_\Omega[[p_{a,b}\mid a,b\ge0,\ a+b>0]]
\]
with product topology by total trace degree, \(\lambda\)-adic order, and
equivariant Laurent coefficient.  Evaluation is the continuous map
\[
  \pi_N\colon\mathscr T_+\to A^q_{N,\Omega,\lambda},
  \qquad
  p_{a,b}\mapsto O_{a,b}^{(N)}.
\]
The partition functional is
\[
  Z_{N,\Omega}(J)
  =
  \omega_{N,\Omega}
  \left(
    \exp\left(\sum_{a+b>0}J_{a,b}O_{a,b}^{(N)}\right)
  \right)
  \in R_\Omega[[J_{a,b}]].
\]
The logarithm is taken in the completed augmentation ideal after
normalizing \(Z_{N,\Omega}(0)=1\).

The large-\(N\) topology \(\mathcal T_\Omega\) is coefficientwise
asymptotic.  A sequence \(c_N\in R_\Omega\) has expansion
\[
  c_N\sim \sum_{g\ge0}N^{\alpha-2g}c_g
\]
if for every \(\lambda\)-order and every Laurent monomial in the
\(\epsilon\)'s, the coefficient sequence has the corresponding Poincare
asymptotic expansion in \(N^{-2}\).  Equivalently, the obstruction to such
an expansion is the class of \((c_N)_N\) in the quotient of all coefficient
sequences by the subspace of sequences with a \(N^{-2}\)-Poincare
expansion.

For the full brane-line theory, replace \(O_{a,b}^{(N)}\) by smeared
operators
\[
  O_{a,b}^{(N)}(\varphi)
  =
  \int_L \varphi(t)\operatorname{Tr}(X(t)^aY(t)^b)\,dt.
\]
Then the coefficients lie in
\[
  \mathcal D'(L^k)\widehat\otimes R_\Omega
\]
with the weak distributional topology against compactly supported test
functions.  The point-algebra statement is the constant-test or local
fiber shadow of this stronger topology.

## 5. Connected Cumulants

For \(F_i\in A^q_{N,\Omega,\lambda}\), define
\[
  \langle F_1,\ldots,F_k\rangle^c_{N,\Omega}
  =
  [t_1\cdots t_k]\,
  \log
  \omega_{N,\Omega}
  \left(
    \exp\left(\sum_i t_iF_i\right)
  \right).
\]
For trace words this gives
\[
  C^{\Omega}_{N;k}
  \bigl((a_1,b_1),\ldots,(a_k,b_k)\bigr)
  =
  \left\langle
    O_{a_1,b_1}^{(N)},\ldots,O_{a_k,b_k}^{(N)}
  \right\rangle^c_{N,\Omega}.
\]
The physical genus expansion is the assertion
\[
  C^{\Omega}_{N;k}
  \bigl((a_1,b_1),\ldots,(a_k,b_k)\bigr)
  \sim
  \sum_{g\ge0}
  N^{2-2g-k}
  F^\Omega_{g;k}
  \bigl((a_1,b_1),\ldots,(a_k,b_k)\bigr)
\]
in \(\mathcal T_\Omega\).  The same formula with smeared insertions has
\[
  F^\Omega_{g;k}
  \in
  \mathcal D'(L^k)\widehat\otimes R_\Omega.
\]

This is the unnormalized single-trace convention.  If one instead uses
normalized traces \(N^{-1}\operatorname{Tr}(X^aY^b)\), the exponent shifts
by \(k\).  The theorem must state the convention.  The surface above uses
the manuscript convention in which \(\operatorname{Tr}(1)=N\) is the
empty trace and nonempty single traces are unnormalized.

## 6. Ward Identities

Assume the brane-defect QME has been solved:
\[
  D_{N,\Omega}^2=0.
\]
Then the state is a \(D_{N,\Omega}\)-cycle in the continuous dual.  For
closed insertions \(F_i\),
\[
  \langle D_{N,\Omega}G,F_1,\ldots,F_k\rangle^c_{N,\Omega}=0.
\]
The gauge and moment-map Ward identities are
\[
  \langle \widehat\mu(\xi)G,F_1,\ldots,F_k\rangle^c_{N,\Omega}=0,
  \qquad
  \langle \xi\cdot G,F_1,\ldots,F_k\rangle^c_{N,\Omega}=0.
\]
The equivariant Ward identity is
\[
  \langle L_{V_\Omega}G,F_1,\ldots,F_k\rangle^c_{N,\Omega}=0,
\]
or, in the invariant Cartan complex,
\[
  \langle Q_\Omega G,F_1,\ldots,F_k\rangle^c_{N,\Omega}=0.
\]
The brane-defect curvature Ward identity is
\[
  \left\langle
    \operatorname{Curv}(K_{\Omega,N})\,G,
    F_1,\ldots,F_k
  \right\rangle^c_{N,\Omega}=0,
\]
where
\[
  \operatorname{Curv}(K_{\Omega,N})
  =
  d_{\mathrm{QME}}K_{\Omega,N}
  +\frac12[K_{\Omega,N},K_{\Omega,N}]_{\hbar_N}.
\]
If the curvature is nonzero, the displayed expression is the anomaly in
the Ward identity.  It is not repaired by stable trace invariant theory.

## 7. Theorem Surface

The strongest admissible theorem is the following criterion.

Let \(A^q_{N,\Omega,\lambda}\) be the derived quantum Hamiltonian
reduction above, with \(\lambda=N\hbar_N\).  Suppose:

1. the mixed Cartan \(\Omega\)-complex and localized normal contraction
   are constructed on the chosen coefficient topology;
2. the stratified brane prefactorization algebra
   \(\mathcal F^{\mathrm{str}}_{\Omega,N}\) on \((X,L)\) is constructed,
   with brane value \(A^q_{N,\Omega,\lambda}\), collar module, products,
   and stratified descent;
3. the equivariant brane-defect Costello package supplies
   \(D_{N,\Omega}\), \(K_{\Omega,N}\), counterterms, scalar projection,
   and product/\(P_0\)-centrality homotopies, with zero curvature;
4. a continuous cyclic state \(\omega_{N,\Omega}\) exists with the
   normalization \(\nu_{N,\Omega}\);
5. the cumulants of the normal-ordered trace insertions
   \(O_{a,b}^{(N)}=\operatorname{Tr}(X^aY^b)\) have coefficientwise
   \(N^{-2}\)-Poincare asymptotics in \(\mathcal T_\Omega\).

Then the connected trace cumulants define amplitudes
\[
  F^\Omega_{g;k}
  \bigl((a_1,b_1),\ldots,(a_k,b_k)\bigr)
\]
by the coefficient of \(N^{2-2g-k}\).  These amplitudes satisfy the
QME, moment-map, equivariant, and brane-curvature Ward identities above,
and they descend to \(D_{N,\Omega}\)-cohomology of the chosen
brane-defect complex.

Conversely, any assertion of physical \(\Omega\)-large-\(N\) trace
states for this local model must provide data satisfying the five
conditions or name the first failed obstruction below.  Degreewise stable
trace invariant theory proves none of conditions 1-5.  It only supplies
the candidate labels \(O_{a,b}\) in the algebraic single-trace sector.

## 8. Exact Obstruction Vector

The physical theorem surface is closed exactly when
\[
  \operatorname{Ob}_{\Omega,\mathrm{phys}}
  =
  (
    \operatorname{ob}_{\Omega,\mathrm{Cartan}},
    \operatorname{ob}_{\Omega,\mathrm{contr}},
    \operatorname{ob}_{\mathrm{red}},
    \operatorname{ob}_{\mathrm{state}},
    \operatorname{ob}_{\mathrm{norm}},
    \operatorname{ob}^{\mathrm{sc}}_{\mathrm{QME}},
    \operatorname{ob}^{\mathrm{ns}}_{\mathrm{QME}},
    \operatorname{ob}_{\mathrm{cent}},
    \operatorname{ob}_{\mathrm{Ward}},
    \operatorname{ob}_{\mathrm{cum}},
    \operatorname{ob}_{\mathrm{asymp}},
    \operatorname{ob}_{\mathrm{src}}
  )
\]
vanishes.

Definitions:

- \(\operatorname{ob}_{\Omega,\mathrm{Cartan}}\): failure to construct the
  mixed Cartan model where \(Q_\Omega^2=L_{V_\Omega}\) is handled by
  invariants/basic data.
- \(\operatorname{ob}_{\Omega,\mathrm{contr}}\): failure to construct
  \((\pi_L,j_L,h_\Omega)\) with
  \(Q_\Omega h_\Omega+h_\Omega Q_\Omega=\operatorname{id}-j_L\pi_L\)
  after inverting nonzero normal weights.
- \(\operatorname{ob}_{\mathrm{red}}\): failure of the derived quantum
  Hamiltonian reduction, including nonclosed quantum moment ideal or
  unjustified passage from BRST reduction to an underived invariant
  quotient.
- \(\operatorname{ob}_{\mathrm{state}}\): for a candidate lift
  \(\widetilde\omega\), the dual cohomology class
  \[
    [D_{N,\Omega}^{\vee}\widetilde\omega]
    \in
    H^1\bigl((\mathcal A^{\mathrm{BRST}}_{N,\Omega,\lambda})^\vee_{\mathrm{cont}}\bigr),
  \]
  together with the failure to annihilate the moment ideal and infinitesimal
  \(GL_N\)-action.
- \(\operatorname{ob}_{\mathrm{norm}}\): unresolved choice or comparison of
  residue normalization, Euler localization by
  \((\epsilon_s\epsilon_1\epsilon_2)^{-1}\), empty trace
  \(O_{0,0}=N\), and \(\lambda=N\hbar_N\).
- \(\operatorname{ob}^{\mathrm{sc}}_{\mathrm{QME}}\): scalar-contact
  obstruction.  In the ordinary scalar-reduced \(\mathfrak{gl}_N\) branch
  the first class is
  \[
    \hbar_N N[\bar c]=\lambda[\bar c].
  \]
  It must be killed by a central-character source, a balanced supertrace
  model, or an explicit leading counterclass \(-\lambda[\bar c]\).
- \(\operatorname{ob}^{\mathrm{ns}}_{\mathrm{QME}}\): non-scalar
  brane-defect obstruction
  \[
    [\operatorname{Ob}^{\mathrm{red}}_{w,\partial,\hbar}]
    \in
    H^1(\ker\widehat\sigma_{\mathrm{sc}},d_{\mathrm{QME}})
  \]
  plus the finite-window obstruction pairs
  \[
    \mathfrak O_n^{\mathrm{ns}}
    =
    \bigl(([\mathfrak o^{\mathrm{ns}}_{n,M}])_M,\lambda_n\bigr).
  \]
- \(\operatorname{ob}_{\mathrm{cent}}\): failure to construct product and
  \(P_0\)-centrality homotopies against unreduced brane observables,
  compatible with finite-window projections, interval inclusions, and
  \(T_\Omega\)-weights.
- \(\operatorname{ob}_{\mathrm{Ward}}\): nonzero values of
  \(\omega(D F)\), \(\omega(Q_\Omega F)\),
  \(\omega(\widehat\mu(\xi)F)\), or
  \(\omega(\operatorname{Curv}(K_{\Omega,N})F)\) in the chosen topology.
- \(\operatorname{ob}_{\mathrm{cum}}\): failure of the exponential and
  logarithm defining connected cumulants in the completed trace-test
  topology, or failure to handle finite-\(N\) trace identities and the
  empty trace scalar.
- \(\operatorname{ob}_{\mathrm{asymp}}\): for some trace tuple and some
  truncation \(G\), the remainder
  \[
    N^{k-2}
    C^\Omega_{N;k}
    -
    \sum_{0\le g<G}N^{-2g}F^\Omega_{g;k}
  \]
  has no \(O(N^{-2G})\) limit coefficientwise in \(\mathcal T_\Omega\).
  Equivalently, the sequence class is nonzero in the quotient of
  coefficient sequences by \(N^{-2}\)-Poincare-asymptotic sequences.
- \(\operatorname{ob}_{\mathrm{src}}\): any use of external
  factorization-homology, Chern-Simons, Costello, CFG, compact
  Calabi-Yau, Vol III, or physical large-\(N\) analogy without a
  primary-source fixture and matched-conventions morphism to this local
  pair \((X,L)\).

## 9. Attack-Heal Ledger

```yaml
- id: A1-185-01
  severity: 1
  status: healed
  lens: physical large-N separation
  target: physical Omega-large-N theorem surface
  claim: Degreewise stable trace invariant theory implies physical large-N trace states.
  broken_step: Stable invariant theory supplies generators only; it does not choose a state, topology, normalization, cumulants, QME Ward identities, or asymptotic expansion.
  evidence_type: proof_gap
  evidence_ref: main.tex:1443-1520; main.tex:4704-4780; open-obligations.tex:638-716
  confidence: high
  blast_radius: false physical open/closed duality theorem
  minimal_heal: Define the state datum, trace-test topology, cumulants, genus expansion, Ward identities, and obstruction vector.
  residual: construct the state and prove asymptotics.
  deciding_evidence: vanishing of Ob_{Omega,phys}

- id: A1-185-02
  severity: 1
  status: healed
  lens: QME Ward identities
  target: state on A^q_{N,Omega}
  claim: A word trace on the quantum Hamiltonian reduction automatically satisfies physical Ward identities.
  broken_step: Ward identities require a D_{N,Omega}-closed continuous functional on the full BRST/BV brane-defect complex; QME curvature and moment-map anomalies must vanish.
  evidence_type: proof_gap
  evidence_ref: open-obligations.tex:678-692; claim-strength-ledger.tex:441-457
  confidence: high
  blast_radius: correlators would not descend to cohomology and curvature anomalies would be hidden.
  minimal_heal: State D^vee omega=0, moment-map Ward, Q_Omega Ward, and Curv(K) Ward as part of the theorem.
  residual: construct K_{Omega,N}, counterterms, scalar projection, and centrality homotopies.
  deciding_evidence: a QME solution with omega(D F)=0 and omega(Curv(K)F)=0.

- id: A1-185-03
  severity: 2
  status: healed
  lens: normalization
  target: N and Omega scaling
  claim: The same formulas can mix fixed hbar, t Hooft scaling, residue normalization, and Euler localization.
  broken_step: The requested N^{2-2g-k} expansion requires a stated hbar-N scaling, and residue/Euler localization differ by the inverse normal Euler class.
  evidence_type: missing_hypothesis
  evidence_ref: open-obligations.tex:663-676; claim-strength-ledger.tex:423-439
  confidence: high
  blast_radius: wrong powers of N, wrong equivariant scalar factors, incompatible comparisons.
  minimal_heal: Fix lambda=N hbar_N for the physical branch and split residue/Euler normalizations.
  residual: prove any comparison map between branches.
  deciding_evidence: nu_{N,Omega} including lambda, empty trace, and the chosen Omega normalization.

- id: A1-185-04
  severity: 2
  status: healed
  lens: topology
  target: cumulant and asymptotic statements
  claim: Formal trace cumulants can be asserted without a convergence topology.
  broken_step: The exponential, logarithm, coefficient extraction, and large-N expansion need a complete trace-test topology and a precise asymptotic sequence topology.
  evidence_type: proof_gap
  evidence_ref: open-obligations.tex:694-735; materials/processed/2026-04-30-mixed-holomorphic-topological-strings-critique.txt:105725-105752
  confidence: high
  blast_radius: no mathematical content to the genus expansion.
  minimal_heal: Define T_+ and T_Omega coefficientwise, with distributional extension on L^k.
  residual: prove actual coefficientwise asymptotics.
  deciding_evidence: vanishing of ob_cum and ob_asymp for every trace tuple.
```

## 10. Stable Core And Residual

Stable core: the typed theorem surface.  A physical
\(\Omega\)-large-\(N\) trace theorem must be a statement about a
continuous cyclic \(D_{N,\Omega}\)-closed state on the derived quantum
Hamiltonian reduction or on the associated stratified factorization
homology, with fixed normalization, connected cumulants, topology, Ward
identities, and a coefficientwise \(N^{-2}\) genus expansion.

Residual: no construction in the current local manuscript supplies
\(\omega_{N,\Omega}\), \(D_{N,\Omega}\), \(K_{\Omega,N}\),
\(\mathcal T_\Omega\), or the amplitudes \(F^\Omega_{g;k}\).  The
correct theorem status is therefore:

\[
  \text{physical \(\Omega\)-large-\(N\) trace state}
  =
  \text{theorem-surface with exact obstruction vector}.
\]
