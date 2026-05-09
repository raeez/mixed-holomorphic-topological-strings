# Costello Local-Functional Habitat Construction Push

Date: 2026-04-30.
Status: report-only construction push. No TeX, script, figure, source, or
build file was edited.

## Claim Attacked

The attacked claim is that a scalar-zero finite-row symbol can be promoted
to a non-scalar Costello counterterm column just by naming a local
counterterm.

That claim is false.  A counterterm column is theorem-grade only inside a
specified filtered local-functional habitat whose differential, bracket,
scalar projection, label class, finite-window projections, weight
transport, and Roos compatibility have already been constructed.

## Stable Source Floor

Costello's finite-scale BV/RG package supports heat-kernel propagators,
regularized BV Laplacians, RG/QME compatibility, local counterterms,
graphwise asymptotics, and \(H^1\)-valued obstruction theory.  The local
source fixture records those anchors at
`references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md:40-130`.

The same fixture records the non-support: no automatic current-valued
target, no theorem for arbitrary \(\mathcal D'_c(I)\)-labelled defect
graphs, and no automatic bulk-to-defect kernel.  See
`references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md:156-240`.

The manuscript already supplies the finite-window grammar:

- `main.tex:8365-8599`: the non-scalar QME obstruction complex,
  scalar-projection lift, bulk-to-defect kernel, and counterterm equation.
- `main.tex:8601-8804`: the \(\theta_3\) one-row obstruction and the lower
  Bianchi defect.
- `appendix-factorization-current-conventions.tex:992-1107`: unreduced
  current lift and convolution habitat.
- `appendix-factorization-current-conventions.tex:1279-1472`: regular
  density graph layer.
- `appendix-factorization-current-conventions.tex:1474-1860`: graphwise
  wavefront-admissible current labels and the exact obstruction to all of
  \(\mathcal D'_c(I)\).
- `appendix-unreduced-bv-qme.tex:2142-2385`: native finite-window
  realization habitat and row-by-row counterterm criterion.
- `tate-P1-hadamard-mittag-leffler.tex:379-609`: finite-window graph/QME
  package and assembly theorem.
- `tate-T1-weighted-completion.tex:1172-1327`: finite-window non-scalar
  QME tower and Milnor/Roos counterterm criterion.

## Filtered Habitat Defined

For a finite Hamiltonian window \(M\), admissible degree weight \(w\),
interval \(I\), and finite connected graph set \(\mathcal G_M\), define
the only presently defensible Costello local-functional habitat by
restricting the cotangent-current labels graphwise:
\[
  B^\Gamma_\bullet\in
  \bigl(\mathcal D^{\mathrm{reg}}_c(I)\bigr)^{r_\Gamma}
  \quad\text{or}\quad
  B^\Gamma_\bullet\in
  \mathcal D'_{c,\mathrm{WF}}(I;\Gamma,M).
\]
Here the second relation is the H\"ormander relation of
`appendix-factorization-current-conventions.tex:1474-1588`; one-sided
finite-scaling classes
\(\mathcal D'_{c,\Lambda_\pm,\mathrm{fs}}(I)\) give honest linear source
subspaces for ordinary collision-conormal kernels.

The target is the completed brane-defect local-functional complex
\[
  \mathfrak Q^\bullet_{\mathcal G,\Lambda,M}(I)
  =
  \left(
  \mathcal O^{\mathrm{bd}}_{\mathrm{loc},\mathcal G,\Lambda,M}
  (\mathcal E_w^M|_I;A^{\mathrm{pp},w,M}_{\partial,\hbar}(I)),
  d_M
  \right),
  \qquad
  d_M=Q+\{I^w_{0,M},-\}_{\hbar,M}.
\]
The completion is in the \(\hbar\)-adic, scalar-contact, and
finite-window filtrations.  The generators are:

- the zero-edge coefficient-current values
  \(\iota_I(B_f^{w,M}(a))\) and
  \(\iota_I(\Theta_\rho^{w,M}(B))\);
- the positive-edge renormalized graph weights
  \(K^M_\Gamma=W^{R,M}_{\Gamma,L,w}(B^\Gamma_\bullet)\);
- the local counterterm extension ambiguities supported on graph
  collision strata
  \(\Delta\cap\operatorname{supp}(B_\Gamma)\);
- every \(d_M\)-boundary, BV-bracket row, source-face row, collision face,
  and lower-counterterm row forced by the finite marked table.

This is a subcomplex only after the last bullet is satisfied.  Omitting a
face is not a choice of presentation; it is exactly a missing theorem
datum.

The target bracket is the finite-window BV/\(P_{0,\hbar}\) bracket
\[
  \{-,-\}_{\hbar,M}\colon
  \mathfrak Q^i_{\mathcal G,\Lambda,M}(I)\widehat\otimes
  \mathfrak Q^j_{\mathcal G,\Lambda,M}(I)
  \to
  \mathfrak Q^{i+j}_{\mathcal G,\Lambda,M}(I),
\]
with Costello signs and the transported weighted Hamiltonian coefficient
bracket.  The Hom-valued kernel habitat is
\[
  \mathbf K^\bullet_{\mathcal G,\Lambda,M}(I)
  =
  \operatorname{Hom}_{\mathrm{cont}}
  (C^\bullet_{\mathrm{lab}}(\mathcal G_M),
   \mathfrak Q^\bullet_{\mathcal G,\Lambda,M}(I)),
\]
with
\[
  d_{\mathbf K,M}T=d_MT-(-1)^{|T|}T\,d_{\mathrm{CE}},
  \qquad
  [T_1,T_2]_{\mathbf K,M}
  =
  [-,-]_{\hbar,M}\circ(T_1\widehat\otimes T_2)\circ\Delta_{\mathrm{CE}},
\]
and
\[
  \operatorname{Curv}_{\mathbf K,M}(\kappa)
  =
  d_{\mathbf K,M}\kappa+\frac12[\kappa,\kappa]_{\mathbf K,M}.
\]
The source-face term \(-\kappa d_{\mathrm{CE}}\) is part of the
differential, not optional bookkeeping.

## Scalar-Zero Kernel

A scalar-zero counterterm column is allowed only after a filtered chain
projection has been constructed:
\[
  \widehat\sigma_{\mathrm{sc},M}\colon
  \mathfrak Q^\bullet_{\mathcal G,\Lambda,M}(I)
  \to
  C^\bullet_{\mathrm{Lie}}(\bar A;\mathbb C\gamma_{\mathbf 1})[1][[\hbar]].
\]
Then
\[
  \mathcal K^\bullet_{\mathrm{ns},M}(I)
  =
  \ker\widehat\sigma_{\mathrm{sc},M},
  \qquad
  d_{\mathrm{ns},M}=d_M|_{\mathcal K_{\mathrm{ns},M}}
\]
is a complex.  If \(\widehat\sigma_{\mathrm{sc},M}\) is only an
associated-graded scalar symbol, \(\ker\widehat\sigma_{\mathrm{sc},M}\) is
not a QME complex and no non-scalar \(H^1\) statement is formed.

In the full-equivariant balanced marked habitat the zero scalar projection
is supported by the cyclic supertrace argument
`appendix-unreduced-bv-qme.tex:1998-2075`.  For a larger graph/counterterm
habitat, one must either prove that every new row lies in that marked
balanced habitat or kill the scalar-extension classes named in
`tate-P1-hadamard-mittag-leffler.tex:448-466`.

## Wavefront And Locality Condition

The strongest current-label class available from the present manuscript is
not all of \(\mathcal D'_c(I)\).  For each \((\Gamma,M)\), the tuple
\(B_\bullet\) must satisfy:

1. non-characteristic incidence pullback for \(e_\Gamma^*B^\boxtimes\);
2. H\"ormander product transversality for
   \(K^M_{\Gamma,\alpha}B_\Gamma\);
3. finite scaling degree along every collision diagonal \(\Delta\);
4. final graph-pushforward wavefront inside the brane-defect
   local-functional class.

The extension ambiguity across \(\Delta\) is a finite sum of normal
derivatives of \(\delta_\Delta\) with coefficients supported in
\(\Delta\cap\operatorname{supp}(B_\Gamma)\).  This is the only
distributional counterterm habitat presently justified for non-regular
labels.  The coincident-current test
\(B_1=B_2=\delta_{t_0}\) fails the product criterion; therefore an
arbitrary \(\mathcal D'_c(I)\) theorem is false without extra
renormalization data.

## Finite-Window Projections And Transport

The finite-window projections and weight transports are part of the
habitat:
\[
  \pi_{M,N}\mathfrak Q^\bullet_{\mathcal G,\Lambda,M}(I)
  \subset
  \mathfrak Q^\bullet_{\mathcal G,\Lambda,N}(I),
  \qquad
  R^M_{w,w'}\mathfrak Q^\bullet_{\mathcal G,\Lambda,M,w}(I)
  =
  \mathfrak Q^\bullet_{\mathcal G,\Lambda,M,w'}(I).
\]
For graph weights and counterterms this means
\[
  \pi_{M,N}W^{R,M}_{\Gamma,L,w}
  =
  W^{R,N}_{\Gamma,L,w}\pi^{\mathrm{CE}}_{M,N},
  \qquad
  R^M_{w,w'}W^{R,M}_{\Gamma,L,w}
  =
  W^{R,M}_{\Gamma,L,w'}R^{M,\mathrm{CE}}_{w,w'},
\]
and the same equations for
\(C_{\Gamma,w}^{M}(\epsilon;B_\bullet)\).  For a primitive column \(C_M\),
the tower condition is
\[
  d_MC_M=-R_M,\qquad
  [\pi_{M,N}C_M-C_N]=0
  \quad\text{in}\quad
  H^0(\mathcal K^\bullet_{\mathrm{ns},N}(I)).
\]
Equivalently, in finite row coordinates,
\[
  A^Mc_M=-r^M,\qquad
  T^{M,N}A^M=A^NP^{M,N},\qquad
  [P^{M,N}c_M-c_N]=0.
\]
The last class is the Roos/Milnor primitive-compatibility obstruction of
`tate-T1-weighted-completion.tex:1221-1327` and
`appendix-unreduced-bv-qme.tex:2234-2385`.

## Candidate Counterterm Columns

The direct \(\theta_3\) column would be a scalar-zero degree-zero element
\[
  C^{\mathrm{ct}}_{\theta_3,M}
  \in\mathcal K^0_{\mathrm{ns},M}(I),
  \qquad
  d_MC^{\mathrm{ct}}_{\theta_3,M}=-\mathsf E_{\theta_3,M},
  \qquad
  \widehat\sigma_{\mathrm{sc},M}(C^{\mathrm{ct}}_{\theta_3,M})=0,
\]
with zero Roos class.  This is accepted by the finite matrix validator
exactly when its differential coefficient is \(-1\), its scalar value is
zero, \(TA=AP\), and its Roos class is zero.  The script verifies this as
an interface fixture, but the current data do not contain such a
Costello local counterterm.

The lower Bianchi route needs a second column.  In the Bianchi-exposed
window \(N=2\),
\[
  d_{\mathrm{CE}}\zeta^0_2=2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}},
\]
but local-functionally
\[
  d_{\mathrm{ns},2}D^2_{02,20}
  =
  -2E^2_{\nu_{02}}+2E^2_{\nu_{20}}
  +\mathfrak b^2_{02,20}.
\]
With only \(D^2_{02,20}\),
\[
  A_D^2=(-2,2,1)^T,\qquad r_2=(2,-2,0)^T
\]
has no solution.  The first matrix that can close the lower row is
\[
  A^2_{D,B}
  =
  \begin{pmatrix}
  -2&0\\
  2&0\\
  1&-1
  \end{pmatrix},
  \qquad
  A^2_{D,B}
  \begin{pmatrix}1\\1\end{pmatrix}
  =
  -r_2,
\]
where the new column is
\[
  B^2_{02,20}\in\mathcal K^0_{\mathrm{ns},2}(I),
  \qquad
  d_{\mathrm{ns},2}B^2_{02,20}=-\mathfrak b^2_{02,20}.
\]
The current habitat does not contain \(B^2_{02,20}\).  Adding it is
theorem-grade only if it is produced as a local counterterm with the
wavefront/locality support, scalar-zero value, and finite-window
transport equations above.

## Heal Attempt Result

The construction closes only as a habitat definition.  It gives a precise
home for scalar-zero counterterm columns:
\[
  C\in
  \mathcal K^0_{\mathrm{ns},M}(I)
  \subset
  \mathfrak Q^0_{\mathcal G,\Lambda,M}(I),
\]
where \(C\) is a regular-density or wavefront-admissible Costello local
counterterm, and its differential is computed by
\(d_M=Q+\{I^w_{0,M},-\}_{\hbar,M}\).

It does not construct the missing columns.  The direct \(\theta_3\)
primitive and the lower Bianchi-killing primitive remain exact
cohomological and microlocal obligations, not consequences of Costello's
general source theorem.

## Exact Missing Theorem

The direct column route requires:

**Theta-three local counterterm exactness theorem.**  For every finite
window \(M\geq3\) in the chosen graph package and for the fixed
wavefront-admissible label class, the source-face row
\(\mathsf E_{\theta_3,M}=-K^M_{\Theta_3}(\zeta_{M,\nu_3})\) is a
\(d_M\)-boundary in
\(\mathcal K^\bullet_{\mathrm{ns},M}(I)\).  Equivalently, there exist
counterterms \(C^{\mathrm{ct}}_{\theta_3,M}\) satisfying
\[
  d_MC^{\mathrm{ct}}_{\theta_3,M}=-\mathsf E_{\theta_3,M},\qquad
  \widehat\sigma_{\mathrm{sc},M}(C^{\mathrm{ct}}_{\theta_3,M})=0,
  \qquad
  [\pi_{M,N}C^{\mathrm{ct}}_{\theta_3,M}
    -C^{\mathrm{ct}}_{\theta_3,N}]=0.
\]
Analytically, the theorem must identify \(C^{\mathrm{ct}}_{\theta_3,M}\)
as a local extension/counterterm supported on the relevant graph
collision stratum, prove finite scaling degree of the representing
Hadamard-current product, and prove compatibility with interval
extension, \(\pi_{M,N}\), and \(R^M_{w,w'}\).

The lower route requires the sharper finite-window theorem:

**Bianchi-defect counterterm theorem.**  In window \(N=2\), the
Hom-valued Bianchi defect \(\mathfrak b^2_{02,20}\) is
\(d_{\mathrm{ns},2}\)-exact by a scalar-zero local counterterm
\(B^2_{02,20}\), and the tower satisfies
\[
  d_{\mathrm{ns},N}(\pi_{M,N}B^M-B^N)
  =
  -\pi_{M,N}\mathfrak b^M+\mathfrak b^N
\]
with zero resulting Roos \(H^0\)-class after any transport correction.
This theorem must compute the actual marked Costello source-face
incidence/weight table and the finite-window transport of the
\(\nu_{02},\nu_{20}\) rows.  Source exactness alone is insufficient.

Until one of these theorems is proved, the correct status is:
filtered local-functional habitat constructed; scalar-zero columns typed;
specific counterterm exactness unproved.

## Attack Ledger

```yaml
- id: A297-01
  severity: 1
  status: blocked
  lens: counterterm-existence overclaim
  target: theta_3 scalar-zero row
  claim: A named Costello local counterterm kills \(\mathsf E_{\theta_3,M}\).
  broken_step: Costello supplies a local obstruction calculus, not a proof that this named scalar-zero row is exact in the Hamiltonian brane-defect local-functional complex.
  evidence_ref: main.tex:8601-8676; references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md:106-137
  deciding_evidence: \(C^{ct}_{\theta_3,M}\) with \(d_MC=-\mathsf E_{\theta_3,M}\), scalar-zero value, wavefront/locality support, \(TA=AP\), and zero Roos class.
```

```yaml
- id: A297-02
  severity: 1
  status: blocked
  lens: source-exactness versus local-functional exactness
  target: lower \(N=2\) Bianchi route
  claim: \(d_{\mathrm{CE}}\zeta^0_2=2\zeta_{\nu_{02}}-2\zeta_{\nu_{20}}\) supplies the lower primitive.
  broken_step: The Hom-valued Bianchi defect \(\mathfrak b^2_{02,20}\) remains in the local-functional differential.
  evidence_ref: main.tex:8719-8804
  deciding_evidence: scalar-zero \(B^2_{02,20}\) with \(d_{\mathrm{ns},2}B^2_{02,20}=-\mathfrak b^2_{02,20}\) and compatible tower transport.
```

```yaml
- id: A297-03
  severity: 1
  status: healed
  lens: arbitrary-current overreach
  target: \(\mathcal D'_c(I)\)-labelled graph habitat
  claim: The filtered habitat can use all compactly supported distributions.
  broken_step: Coincident delta labels fail H\"ormander product transversality against the singular boundary propagator.
  evidence_ref: appendix-factorization-current-conventions.tex:1714-1727; appendix-factorization-current-conventions.tex:1844-1859
  heal: Restrict the habitat to regular densities, graphwise wavefront-admissible tuples, or sign-conic finite-scaling classes.
```

```yaml
- id: A297-04
  severity: 2
  status: healed
  lens: finite-window transport
  target: proposed counterterm-column habitat
  claim: A fixed-window primitive is enough.
  broken_step: The manuscript's QME criterion is an inverse-limit criterion; primitives must satisfy Roos compatibility.
  evidence_ref: tate-T1-weighted-completion.tex:1221-1327; appendix-unreduced-bv-qme.tex:2302-2333
  heal: Build \(\pi_{M,N}\), \(R^M_{w,w'}\), \(TA=AP\), and \([P^{M,N}c_M-c_N]=0\) into the habitat definition.
```

## Verification

Commands run:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py
rg -n "nonscalar|non-scalar|scalar-zero|QME|theta_?3|theta3|Counterterm|counterterm|Costello|local functional|local-functional|wavefront|finite-window|finite window" main.tex appendix-factorization-current-conventions.tex reconstitution/nonscalar-costello-graph-qme-realization-next-construction-push-2026-04-30.md references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md
```

Observed script floor:

```text
minimal_full_equivariant_order_2_zero: primitive_exists true, counterterm C_{2,M}=0, Roos class zero.
theta_3_current_finite_row_subcomplex: primitive_exists false, residual E_theta_3, left covector value 1.
theta3_counterterm_supplied_exact_payload: accepted only as an interface fixture when dC=-E, scalar-zero, TA=AP, and Roos zero are supplied.
theta3_eight_face_candidate_source_algebraic_obstruction: rejected; diagonal transport leaves 2E_nu02-2E_nu20 at N=2 and the marked Costello incidence/weight table is absent.
```

No PDF build was run because this was report-only and no TeX was edited.
