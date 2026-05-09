# Stratified Weiss Cech/Roos Proof Push

Agent: 293.

Date: 2026-04-30.

Status: report-only proof push.  No TeX file was edited.

Owned writable files:

- `reconstitution/stratified-weiss-cech-roos-proof-push-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-293-stratified-weiss-cech-roos-proof-push.md`

## Verdict

The reduced product-basis prefactorization datum can be promoted to a
theorem-grade obstruction statement, but not to full stratified Weiss
descent from the current manuscript data.

The strongest closed statement is:

1. On the reduced product-stratified basis, extension by zero gives
   product maps and kills
   \(\delta_{\mathrm{pref}}\) and \(\delta_{\mathrm{assoc}}\).
2. For an arbitrary collared stratified Weiss cover, the exact descent
   defect is the cohomology of a Cech cone.
3. Compatibility under refinements, finite normal windows, interval
   inclusions, and admissible weight transports is measured by a Roos
   complex of those cone defects.
4. Full descent is equivalent to vanishing of the Cech cone cohomology
   for every collared Weiss cover, together with vanishing of the Roos
   compatibility class for the chosen null-homotopies.

Thus the current blocking class is not a parameter convention.  It is the
unconstructed class
\[
  \mathfrak w^{\check C/R}_{V,\Omega,N,M}
  \in
  H^0\operatorname{Tot}
  \operatorname{Roos}\!\left(
    \mathsf{Ref}^{\mathrm{str}}_{\mathrm W}(V);
    \underline{\operatorname{End}}(\Delta_{V,\bullet}^{N,M})
  \right),
\]
represented by the identity of the Cech cone system.  Equivalently,
descent fails on a specific cover as soon as some class
\[
  [(b,x)]\in H^q\Delta_{V,\mathcal U}^{N,M}
\]
is nonzero.  The present text has not produced the contractions or
null-homotopies needed to kill these classes.

## Evidence Anchors

- `main.tex:1092-1163`: local pair, native mixed Hamiltonian
  factorization object, and brane interval principal-part current target.
- `main.tex:1175-1235`: CE/factorization observables and
  extension-by-zero products.
- `main.tex:4239-4255`: centrality and compact-support naturality are
  still required before a global descent/action theorem.
- `main.tex:6390-6404`: reduced principal-part current brackets are
  support-local \(P_0\) data, not unreduced centrality homotopies.
- `main.tex:7411-7568`: Costello BV graph realization requires topology,
  propagator, anomaly, counterterms, and QME data.
- `theorem-lanes.tex:3007-3206`: current stratified trace lane still
  treats the full stratified object as a theorem surface; it carries the
  stale seven-component vector and uses the wrong QME/Weyl parameter in
  the \(P_0\)-centrality homotopy.
- `open-obligations.tex:906-1120`: stratified brane datum, collar maps,
  products, old holim-style descent defect, centrality rows, QME
  curvature, and stale source-internal vector.
- `claim-strength-ledger.tex:548-553` and `:774-798`: stratified
  factorization remains a construction target and still records the old
  vector.
- `local-dictionary.tex:441-541`: normal torus, \(Q_\Omega^2=L_{V_\Omega}\),
  coefficient ring, and normal contraction datum.
- `local-dictionary.tex:678-712`: stratified datum and open
  \(\Omega\)-obstruction vector.
- `appendix-unreduced-bv-qme.tex:2487-2630`: normal \(\Omega\)-equivariant
  Costello kernel datum and the three-parameter gate.
- `references/primary-sources/weiss-ran-stratified-descent-source-anchors-2026-04-30.md`:
  external sources support Weiss/Cech grammar, not the mixed HT
  brane-defect construction.
- `references/primary-sources/omega-stratified-source-anchors-2026-04-30.md`:
  AFT and CFG give external model theorems and trace vocabulary only
  after their hypotheses are rebuilt for this \((X,L)\).

## Reduced Product-Basis Result

Let
\[
  X=\mathbb R_t\times\mathbb R_s\times\mathbb C^2_{z_1,z_2},
  \qquad
  L=\mathbb R_t\times\{s=z_1=z_2=0\}.
\]
Let \(\mathcal B^{\mathrm{red}}_{\mathrm{prod}}(X,L)\) be the two-color
product basis with bulk product disks \(U\times B\subset X\setminus L\),
brane intervals \(I\subset L\), and finite disjoint unions.  The proved
reduced values are
\[
  \mathcal F^{\mathrm{red}}_{\Omega,X}(U\times B)
  =
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  \left(
    \Omega_c^\bullet(U)\widehat\otimes
    \Omega_c^{0,\bullet}(B)\widehat\otimes
    (\mathfrak h\ltimes\mathcal P[1])
  \right)
  \widehat\otimes R_\Omega^{N,M},
\]
where
\[
  \mathcal P=\operatorname{Ann}_{\mathrm{res}}(\mathbb C\cdot1)
  \cong\mathfrak h^\vee_{\mathrm{cont}},
\]
and
\[
  \mathcal F^{\mathrm{red}}_{\Omega,L}(I)
  =
  A^{\mathrm{pp},w}_{\partial,\Omega,\hbar_{\mathrm{W}}}(I).
\]
The product maps are extension by zero on compact supports followed by
the CE product or completed symmetric multiplication.  Hence
\[
  \delta_{\mathrm{pref}}=\delta_{\mathrm{assoc}}=0
\]
on this reduced product basis.  This result does not construct collar
modules, arbitrary collared Weiss descent, unreduced centrality
homotopies, brane-defect QME curvature cancellation, basic
\(\Omega\)-primitives, or trace-state topology.

## Cech Cone

Let \(\mathcal U=\{U_i\}_{i\in I}\) be a collared stratified Weiss cover
of a stratified open pair \((V,V\cap L)\): every finite subset of \(V\)
lies in some \(U_i\), and if the subset meets \(L\), the same \(U_i\)
contains a product collar of its lower-stratum part.

For a candidate stratified object
\(\mathcal F^{\mathrm{str}}_{\Omega,N,M}\), put
\[
  U_J=\bigcap_{j\in J}U_j,\qquad |J|=p+1,
\]
and
\[
  \check C^p(\mathcal U;\mathcal F^q)
  =
  \prod_{i_0<\cdots<i_p}
  \mathcal F^q(U_{i_0\cdots i_p}).
\]
If \(J\subset K\), write
\[
  \rho_{J,K}\colon \mathcal F(U_J)\longrightarrow \mathcal F(U_K)
\]
for restriction to the smaller intersection.  The Cech differential is
\[
  (\check\delta c)_K
  =
  \sum_{\nu=0}^{p+1}
  (-1)^\nu
  \rho_{K\setminus\{k_\nu\},K}
  \bigl(c_{K\setminus\{k_\nu\}}\bigr),
\]
and the total differential is
\[
  \mathbb D=\check\delta+(-1)^p d_{\mathcal F}
  \quad
  \text{on } \check C^p(\mathcal U;\mathcal F^q).
\]

The descent map is
\[
  r_{V,\mathcal U}\colon
  \mathcal F^{\mathrm{str}}_{\Omega,N,M}(V)
  \longrightarrow
  \operatorname{Tot}\check C^\bullet
  (\mathcal U;\mathcal F^{\mathrm{str}}_{\Omega,N,M}),
\]
with \(r(x)_i=\rho_{\{i\},V}(x)\) in Cech degree zero.

Define the cohomological cone
\[
  \Delta_{V,\mathcal U}^{N,M}
  =
  \operatorname{Cone}(r_{V,\mathcal U}),
\]
with
\[
  (\Delta_{V,\mathcal U}^{N,M})^n
  =
  \operatorname{Tot}^n\check C^\bullet(\mathcal U;\mathcal F)
  \oplus
  \mathcal F^{n+1}(V),
\]
and
\[
  d_\Delta(b,x)=
  (\mathbb D b+r_{V,\mathcal U}(x),-d_{\mathcal F}x).
\]
The Cech descent obstruction for this cover is
\[
  \delta_{\mathrm{Weiss}}(V,\mathcal U;N,M)
  =
  H^\bullet(\Delta_{V,\mathcal U}^{N,M}).
\]
A class
\[
  [(b,x)]\in H^q(\Delta_{V,\mathcal U}^{N,M})
\]
is exact precisely when there are \((b',x')\) with
\[
  (b,x)=d_\Delta(b',x').
\]
Thus \([(b,0)]\) is the obstruction to lifting a Cech-compatible local
observable \(b\) to a global observable on \(V\), and \([(b,x)]\) is the
obstruction to replacing a partially lifted global class \(x\) by a
strictly compatible descent datum.  The cover-level descent theorem is
equivalent to \(H^\bullet(\Delta_{V,\mathcal U}^{N,M})=0\).

## Roos Transitions

Let \(\mathsf{Ref}^{\mathrm{str}}_{\mathrm W}(V)\) be the category whose
objects are collared stratified Weiss covers of \(V\), together with the
chosen finite normal window \((N,M)\), branch, and coefficient ring
\(R_\Omega^{N,M}\).  Morphisms are generated by:

- cover refinements \(\alpha\colon\mathcal V\to\mathcal U\);
- interval inclusions on lower-stratum basics;
- finite-window projections \(P_{M'\to M}\);
- admissible normal-weight transports and base changes of
  \(R_\Omega^{N,M}\);
- self-dual specialization formed before any further inversion.

For a refinement \(\alpha\colon\mathcal V=\{V_a\}\to\mathcal U=\{U_i\}\),
where \(V_a\subset U_{\alpha(a)}\), the transition
\[
  T_\alpha\colon
  \operatorname{Tot}\check C^\bullet(\mathcal U;\mathcal F)
  \longrightarrow
  \operatorname{Tot}\check C^\bullet(\mathcal V;\mathcal F)
\]
is
\[
  (T_\alpha c)_{a_0\cdots a_p}
  =
  \rho_{\alpha(a_0)\cdots\alpha(a_p),\,a_0\cdots a_p}
  \bigl(c_{\alpha(a_0)\cdots\alpha(a_p)}\bigr).
\]
The induced cone transition is
\[
  \Delta_\alpha(b,x)=(T_\alpha b,x).
\]
Window projections, interval inclusions, and weight transports act on
both cone terms by the corresponding maps on
\(\mathcal F^{\mathrm{str}}_{\Omega,N,M}\).

For the resulting inverse system
\(\Delta_\bullet\), define the Roos complex
\[
  \operatorname{Roos}^p
  (\mathsf{Ref}^{\mathrm{str}}_{\mathrm W}(V);\Delta)^q
  =
  \prod_{\alpha_0\to\cdots\to\alpha_p}
  \Delta_{\alpha_0}^q.
\]
The Roos differential is
\[
\begin{aligned}
  (d_R c)_{\alpha_0\cdots\alpha_{p+1}}
  ={}&
  \Delta_{\alpha_0\alpha_1}
  (c_{\alpha_1\cdots\alpha_{p+1}})
  \\
  &+
  \sum_{\nu=1}^{p}
  (-1)^\nu
  c_{\alpha_0\cdots\widehat{\alpha_\nu}\cdots\alpha_{p+1}}
  +
  (-1)^{p+1}c_{\alpha_0\cdots\alpha_p}.
\end{aligned}
\]
The total differential is
\[
  D_{\check C/R}=d_\Delta+(-1)^q d_R
  \quad\text{on internal degree }q.
\]

The Roos obstruction to a compatible family of Cech null-homotopies is
the class
\[
  \mathfrak w^{\check C/R}_{V,\Omega,N,M}
  =
  [\operatorname{id}_{\Delta_\bullet}]
  \in
  H^0\operatorname{Tot}
  \operatorname{Roos}\!\left(
    \mathsf{Ref}^{\mathrm{str}}_{\mathrm W}(V);
    \underline{\operatorname{End}}(\Delta_\bullet)
  \right).
\]
It vanishes exactly when the cone system admits compatible continuous
contractions
\[
  h_\alpha\colon\Delta_\alpha^\bullet\to\Delta_\alpha^{\bullet-1},
  \qquad
  d_\Delta h_\alpha+h_\alpha d_\Delta=\operatorname{id}_{\Delta_\alpha},
\]
with the refinement/window/weight-transition defects killed by higher
Roos homotopies.  This is the theorem-grade form of stratified Weiss
descent in the present completed habitats.  The current reduced
product-basis construction supplies no such \(h_\alpha\).

## Internal Obstruction Vector

The manuscript should use the internal vector
\[
  \operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}
  =
  (
    \delta_{\mathrm{pref}},
    \delta_{\mathrm{assoc}},
    \delta_{\mathrm{Weiss}}^{\check C/R},
    \operatorname{ob}_{\mathrm{collar}},
    \operatorname{ob}^{\mathrm{prod}}_{\mathrm{cent}},
    \operatorname{ob}^{P_0}_{\mathrm{cent}},
    \operatorname{ob}^{\mathrm{bd}}_{\mathrm{QME}},
    \operatorname{ob}_{\Omega\mathrm{-basic}},
    \operatorname{ob}_{\mathrm{tr}\mathrm{-top}}
  ).
\]
Here
\(\delta_{\mathrm{Weiss}}^{\check C/R}\) means the coverwise Cech cone
cohomology together with the Roos compatibility class above.  On the
reduced product basis,
\[
  \delta_{\mathrm{pref}}=\delta_{\mathrm{assoc}}=0,
\]
but no current manuscript argument kills
\(\delta_{\mathrm{Weiss}}^{\check C/R}\), the collar class, the two
centrality classes, the QME curvature class, the basicness class, or the
trace-topology class.

The \(P_0\)-centrality row is a
\(P_{0,\hbar_{\mathrm{QME}}}\)-row in the unreduced brane-defect
local-functional complex:
\[
  \operatorname{ob}^{P_0}_{\mathrm{cent}}(x,A)
  =
  \left[
    \{\kappa_\Omega(x),A\}_{P_{0,\hbar_{\mathrm{QME}}}}
    -\rho_{\mathrm{mod}}(x;A)
  \right].
\]
It is not a reduced Weyl/Moyal current bracket over
\(\hbar_{\mathrm{W}}\).

## External Source Gate

The source-primary class
\[
  \operatorname{ob}^{\mathrm{src}}_{\mathrm{CFG}}
\]
must stay outside
\(\operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}\).  It is not
an internal component of the mixed HT construction.

It is a gate for imported source support.  It vanishes only after a
source fixture supplies:

- the exact source theorem and its hypotheses;
- the target stratified pair and tangential/framing data;
- a matched-conventions morphism to
  \(X=\mathbb R^2_{\mathrm{top}}\times\mathbb C^2_{\mathrm{hol}}\) and
  \(L=\mathbb R_t\times\{s=z_1=z_2=0\}\);
- the parameter comparison for
  \(\hbar_{\mathrm{QME}},\hbar_{\mathrm{W}},\hbar_\omega\);
- the brane-defect QME and trace-state comparison.

Until those data exist, AFT, Costello--Gwilliam, Weiss/Ran, Costello
\(\Omega\)-background, or CFG trace results supply grammar and analogy
only.

## Proof Push

The reduced basis theorem is internal because extension by zero commutes
with \(d_{\mathbb R}\), \(\bar\partial\), the CE differential, and
completed symmetric multiplication.  This proves exactly the
product/associativity row on
\(\mathcal B^{\mathrm{red}}_{\mathrm{prod}}(X,L)\).

The full descent theorem would require, for each collared Weiss cover,
that \(r_{V,\mathcal U}\) be a quasi-isomorphism.  In the completed
cochain convention this is exactly the acyclicity of
\(\Delta_{V,\mathcal U}^{N,M}\).  In the stronger construction used by
the manuscript, one needs compatible continuous contractions, not merely
untracked coverwise acyclicity; this is the Roos class
\(\mathfrak w^{\check C/R}_{V,\Omega,N,M}\).

No loaded manuscript passage constructs:

- collar restriction maps transported through the Costello
  local-functional target;
- null-homotopies \(H^{\mathrm{prod}}\) and \(H^{P_0}\) in the unreduced
  non-scalar Hom complex;
- a Cech-local QME kernel \(K\) solving
  \(\mathbb D K+\frac12[K,K]_{\hbar_{\mathrm{QME}}}=0\);
- basic Cartan primitives satisfying \(L_{V_\Omega}H=0\);
- trace-state topology and Ward-compatible state functional.

Therefore full Weiss descent is blocked precisely by
\[
  \delta_{\mathrm{Weiss}}^{\check C/R}
  =
  \left(
    \{H^\bullet(\Delta_{V,\mathcal U}^{N,M})\}_{(V,\mathcal U,N,M)},
    \mathfrak w^{\check C/R}_{V,\Omega,N,M}
  \right).
\]
This is the correct obstruction theorem surface.  It is stronger than a
parameter repair and sharper than a conditional descent statement.

## Attack Ledger

```yaml
- id: A293-01
  severity: 1
  status: healed
  target: reduced product-basis prefactorization datum
  claim: Extension by zero gives product and associativity on the reduced product basis.
  result: proved on the named reduced basis
  residual: no collars or arbitrary Weiss descent

- id: A293-02
  severity: 1
  status: valid
  target: arbitrary collared stratified Weiss covers
  claim: Product-basis prefactorization implies full Weiss descent.
  failure_mode: product-basis products do not prove that r_{V,U} is a quasi-isomorphism.
  obstruction: H^*(Delta_{V,U}^{N,M})

- id: A293-03
  severity: 1
  status: valid
  target: refinements and inverse-window compatibility
  claim: Coverwise cone vanishing automatically gives compatible descent data.
  failure_mode: null-homotopies must commute with refinements, interval inclusions, finite-window projections, and weight transports.
  obstruction: w^{Cech/R}_{V,Omega,N,M} in the Roos endomorphism complex

- id: A293-04
  severity: 1
  status: valid
  target: internal obstruction vector
  claim: ob_src_CFG belongs in the internal stratified obstruction vector.
  failure_mode: source import is an external matched-conventions gate, not internal mixed HT data.
  heal: use nine internal components and keep ob_src_CFG outside the vector

- id: A293-05
  severity: 1
  status: valid
  target: P0-centrality parameter
  claim: reduced Weyl/Moyal brackets over hbar_W solve P0-centrality.
  failure_mode: the centrality row lives in the unreduced QME local-functional complex over hbar_QME.
  heal: use P_{0,hbar_QME}; keep hbar_W for Weyl/Moyal current algebra
```

## Files Changed

- Added `reconstitution/stratified-weiss-cech-roos-proof-push-2026-04-30.md`.
- Added `reconstitution/swarm-2026-04-30-agent-293-stratified-weiss-cech-roos-proof-push.md`.

No TeX edit and no PDF build were performed.
