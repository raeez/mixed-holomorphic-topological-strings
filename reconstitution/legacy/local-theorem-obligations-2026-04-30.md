# Local Theorem-Obligation Index, 2026-04-30

Scope: the formal-local mixed holomorphic-topological theory on
\[
  \mathbb R^2_{\mathrm{top}}\times
  \widehat{\mathbb C^2}_{0,\mathrm{hol}},
  \qquad \Omega_{\mathrm{loc}}=dz_1\wedge dz_2 .
\]
Compact Calabi-Yau, CoHA, quintic, OSV/GV, Abel-Jacobi, MNOP, Vol III,
Igusa, Borcherds, and BKM data are not core local obligations.  They are
quarantined external comparison surfaces.

Evidence used: the current launch log, `attack-heal-latest-2026-04-30.md`,
Agents 092--096, 099, 105, 118, 121, 123, 130, 133, 139--151, 153--159,
and the current TeX control labels.  Agent 152 and Agent 161 reports are
absent locally.  Agent 159 is present locally but untracked at this read.

## Stable Local Branches

- Local geometry and firewall: the core theorem surface is local
  \(\mathbb R^2_{\mathrm{top}}\times\widehat{\mathbb C^2}_{0,\mathrm{hol}}\).
- Local unimodularity: \(\Omega_{\mathrm{loc}}\), Hamiltonian bracket,
  divergence, BV density, residue basis, and cyclic trace are the only
  Calabi-Yau input.
- Componentwise quantum coefficient surface:
  Theorem `thm:quantum-coefficient-surface` is proved componentwise.
- Balanced scalar branch: the ordinary scalar obstruction is
  \(\hbar N[\bar c]\); the balanced supertrace branch kills only the
  scalar class.
- Minimal full-equivariant finite-window graph package: through Agent 158,
  the minimal package has all positive scalar-contact closure rows zero:
  \(R^{\mathrm{ns}}_{n,M}=0\), \(\mathfrak o^{\mathrm{ns}}_{n,M}=0\),
  \(C_{n,M}=0\) for \(n\ge1\).  This does not decide larger packages.
- Regular-density graph branch: the regular-density evaluated-curvature
  certificate kills the regular-density quotient classes on its stated
  habitat.
- Current labels: arbitrary \(B\in\mathcal D'_c(I)\) are allowed in the
  algebraic coefficient-current kernel, not in arbitrary Costello graph
  products.
- Radial branch: \(K_{4,4}\) is verified in the free indexed trace-diagram
  algebra.  No all-bidegree contracting homotopy is known.
- Chiral/factorization taxonomy: the constructed object is a local
  two-complex-dimensional holomorphic factorization object, not a
  one-dimensional VOA/OPE algebra.

## Finite Core Obligation List

### LO-01. Non-scalar quantum \(P_0\) / Costello QME realization

Target theorem: upgrade the componentwise theorem
`thm:quantum-coefficient-surface` to the non-scalar realization problem
`prob:quantum-p0-operation-realization`.

Current proved branch: weighted coefficient convergence, balanced scalar
cancellation, reduced principal-part current brackets, and the minimal
full-equivariant scalar-contact branch are proved on their stated habitats.

Missing data/map/homotopy: a complete \(d_{\mathrm{QME}}\)-stable
scalar-contact filtration, a filtered chain projection
\[
  \widehat\sigma_{\mathrm{sc}}\colon
  \mathfrak Q^\bullet_{w,\partial,\hbar}(I)
  \to C^\bullet_{\mathrm{Lie}}(\bar A;\mathbb C\gamma_{\mathbf 1})[1][[\hbar]],
\]
the reduced obstruction cocycle
\(\operatorname{Ob}^{\mathrm{red}}_{w,\partial,\hbar}\), and compatible
finite-window counterterms.

Exact obstruction: the scalar-lift tower
\[
o_{\sigma,w}^{(r)}\in
H^1(\operatorname{Hom}(\operatorname{gr}_F\mathfrak Q^\bullet_{\mathrm{bd}},
C^\bullet_{\mathrm{Lie}}(\bar A;\mathbb C\gamma_{\mathbf 1})[1])_{-r})
\]
and, after the lift exists,
\[
[\operatorname{Ob}^{\mathrm{red}}_{w,\partial,\hbar}]
\in H^1(\ker\widehat\sigma_{\mathrm{sc}},d_{\mathrm{QME}}).
\]

Responsible surface: `main.tex:7296`, `main.tex:7463`,
`appendix-unreduced-bv-qme.tex:2078`, `tate-T1-weighted-completion.tex:932`,
`tate-T1-weighted-completion.tex:981`.

Deciding evidence: a filtered chain projection with all
\(o_{\sigma,w}^{(r)}=0\), followed by a degree-zero compatible primitive
for the displayed \(H^1\) class, or a computed nonzero class.

Likely next lane: non-scalar QME scalar-projection and counterterm lane.

### LO-02. Finite-window graph row arrays for larger packages

Target theorem: finite-window graph/QME rows beyond the minimal
full-equivariant package, feeding `thm:wt-nonscalar-counterterm-criterion`
and `def:app-nonscalar-kernel-row-complex`.

Current proved branch: \(K^M_{\alpha_{\mathrm{sc}}}=0\); bracket rows
containing \(\alpha_{\mathrm{sc}}\) are zero; \(\alpha_{11}\) is a retained
zero diagnostic row if zero rows are allowed; genuine order-two and
order-three rows are empty in the minimal package.

Missing data/object/map/homotopy: for any larger package, the actual seed
sets \(\mathcal G^{\mathrm{gen}}_{n,M}\), renormalized weights
\(K^M_\Gamma\), \(d_MK^M_\Gamma\), CE-source faces, BV/convolution bracket
rows, lower-counterterm rows, scalar gates, row signs, and normalized
truncation matrices.

Exact obstruction:
\[
  \mathfrak o^{\mathrm{ns}}_{n,M}
    =[R^{\mathrm{ns}}_{n,M}]
    \in H^1(\mathcal K^\bullet_{\mathrm{ns},M}(I),d_{\mathrm{ns},M})
\]
and the compatible tower obstruction
\[
  \mathfrak O^{\mathrm{ns}}_n
  =
  (([\mathfrak o^{\mathrm{ns}}_{n,M}])_M,\lambda_n),
  \qquad
  \lambda_n\in\varprojlim\nolimits^1_M H^0(\mathcal Q^\bullet_{w,M}(I)).
\]

Responsible surface: `tate-P1-hadamard-mittag-leffler.tex:1011`,
`tate-P1-hadamard-mittag-leffler.tex:1075`,
`appendix-unreduced-bv-qme.tex:2196`,
`appendix-unreduced-bv-qme.tex:2291`,
`appendix-unreduced-bv-qme.tex:2422`,
`appendix-unreduced-bv-qme.tex:2476`,
`scripts/finite_window_graph_array.py`.

Deciding evidence: a populated row table whose scalar gates vanish or
identify the scalar obstruction, a computation of the resulting \(H^1\)
class, and compatible truncation matrices with Roos class zero or nonzero.

Likely next lane: finite-window row/truncation matrix lane.  Agent 161 is
named in the launch log but no local report is present.

### LO-03. Curved bulk-to-defect kernel and unreduced centrality homotopies

Target theorem: the unreduced non-scalar current lift and \(P_{0,\hbar}\)
central-operation kernel.

Current proved branch: reduced support-local current brackets and the
regular-density inclusion
\[
  \Xi_M^{\mathrm{reg}}\colon
  \mathcal X^{\bullet,\mathrm{reg}}_{w,M}(I)
  \hookrightarrow
  \mathcal Q^\bullet_{w,M}(I)
\]
are constructed.  The raw kernel is not yet a cochain map or a curved
Maurer-Cartan solution.

Missing data/object/map/homotopy: a continuous kernel
\[
  \kappa_{\hbar,w,I}\colon
  C^\bullet_{\mathrm{CE},\mathrm{cont}}
  (\mathfrak g^{w,\mathrm{cur}}_{\hbar,I})
  \to\mathfrak Q^\bullet_{w,\partial,\hbar}(I),
\]
finite-scale Costello BV propagator and Laplacian in the chosen habitat,
and \(d_{\mathrm{QME}}\)-homotopies killing the generator defects
\(D_{f,g}\), \(D_{f,\rho}\), and \(D_{\rho,\sigma}\).

Exact obstruction:
\[
  d_{\mathbf K}\kappa
  =
  d_M\kappa-\kappa d_{\mathrm{CE}},
  \qquad
  \operatorname{Curv}_{\mathbf K}(\kappa)
  =
  d_{\mathbf K}\kappa+\frac12[\kappa,\kappa]_{\mathbf K}.
\]
After scalar projection, the residual lives in
\(H^1(\ker\widehat\sigma_{\mathrm{sc}},d_{\mathrm{QME}})\).

Responsible surface: `appendix-factorization-current-conventions.tex:462`,
`appendix-factorization-current-conventions.tex:1334`,
`tate-T1-weighted-completion.tex:1136`,
`tate-T1-weighted-completion.tex:1218`,
`open-obligations.tex:473`.

Deciding evidence: \(\widehat\sigma_{\mathrm{sc}}\kappa=0\) and
\(d_{\mathbf K}\kappa=0\), or full
\(\operatorname{Curv}_{\mathbf K}(\kappa)=0\), with interval,
factorization-product, finite-window, and weight compatibility.

Likely next lane: bulk-defect kernel / centrality-homotopy constructor.

### LO-04. Current-compatible Costello graph theorem for distributional labels

Target theorem: extend the graph/counterterm theorem from regular densities
and graphwise wavefront-admissible tuples to a specified current habitat,
or keep arbitrary \(\mathcal D'_c(I)\) out of the Costello graph theorem.

Current proved branch: coefficient-current maps allow arbitrary
\(B\in\mathcal D'_c(I)\); graph products are proved for regular compactly
supported densities and finite graphwise wavefront-admissible tuples.
Arbitrary \(\mathcal D'_c(I)\) graph labels are false in the present
theorem surface.

Missing data/object/map/homotopy: renormalization rules for failed
Hormander products, numerical scaling-degree bounds, local counterterm
coefficients, interval-extension compatibility, finite-window truncation,
and admissible weight transport for each graph family.

Exact obstruction: coincident singular labels, for example
\(B_1=B_2=\delta_{t_0}\), can violate product transversality against the
collision diagonal.  This is a counterexample to the full
\(\mathcal D'_c(I)\) claim, not a class already killed in the manuscript.

Responsible surface: `appendix-factorization-current-conventions.tex:749`,
`appendix-factorization-current-conventions.tex:944`,
`appendix-factorization-current-conventions.tex:1032`,
`appendix-factorization-current-conventions.tex:1164`.

Deciding evidence: a graphwise microlocal theorem supplying wavefront
transversality, finite scaling degree, diagonal extension ambiguity, and
counterterm compatibility; otherwise theorem text remains restricted.

Likely next lane: microlocal Costello current theorem lane.

### LO-05. Wavefront quotient exactness in the original complex

Target theorem: decide whether nonregular wavefront residuals vanish in
the original regular-density quotient complex, not merely in the formal
primitive cone extension.

Current proved branch: the regular-density certificate kills the branch
when the evaluated curvature and all lower counterterms lie in
\(\mathcal Q^{\bullet,\mathrm{rd}}=\mathcal X^{\bullet,\mathrm{reg}}\).
Agent 144 adds a primitive cone that kills a compatible wavefront residual
in an enlarged complex.

Missing data/object/map/homotopy: the actual finite-window coefficient
array for the nonregular graph curvature and lower counterterms, and an
intrinsic degree-zero distributional primitive in the original quotient
if it exists.

Exact obstruction:
\[
  \eta^{\mathrm{reg}}_{n_0,M}
  =
  [\mathfrak s^{\mathrm{WF}}_{n_0,M}]
  \in H^1(\mathcal C^{\bullet,\mathrm{reg}}_{w,M}(I)).
\]
If finite-window quotient classes vanish, the next obstruction is
\[
  \kappa^{\mathrm{reg}}_{n_0}
  \in \varprojlim\nolimits^1_M\ker H^1(\Xi^{\mathrm{reg}}_M),
\]
followed outside the saturated branch by \(\mu^{\mathrm{cl}}_{n_0}\) and
\(\lambda^{\mathrm{cl}}_{n_0}\).

Responsible surface: `tate-T1-weighted-completion.tex:1503`,
`tate-T1-weighted-completion.tex:1731`,
`tate-T1-weighted-completion.tex:1935`,
`tate-T1-weighted-completion.tex:2158`,
`tate-T1-weighted-completion.tex:2344`.

Deciding evidence: compute \(q_M(\mathfrak o^{\mathrm{ns}}_{n_0,M})\);
exhibit a primitive in the original quotient complex, or prove a nonzero
class.  Cone exactness alone does not decide this obligation.

Likely next lane: wavefront residual quotient computation.

### LO-06. Weighted Costello locality and analytic RG compatibility

Target theorem: `prob:weighted-rg-locality`, namely compatibility of the
finite-window weighted coefficient package with Costello locality, RG flow,
defect counterterms, and the QME recursion.

Current proved branch: strict finite-window ML exactness, weighted
coefficient kernels, regulator transport, and admissible weight
independence are constructed.  Costello source fixtures support
finite-scale BV/RG/QME vocabulary, not the current-valued theorem.

Missing data/object/map/homotopy: bulk field complex, heat kernel,
propagator, local functional estimates, defect counterterm estimates, and
RG/QME compatibility for the chosen brane-defect current target.

Exact obstruction: for non-scalar QME this reduces to
\(\mathfrak O^{\mathrm{ns}}_n\); for the strict product/direct-sum endpoint
the obstruction is the Casimir/support no-go recorded as
\(\mathfrak o^{\mathrm{Cas}}\).

Responsible surface: `tate-T1-weighted-completion.tex:541`,
`tate-T1-weighted-completion.tex:932`,
`tate-T1-weighted-completion.tex:981`,
`tate-T3-quillen-equivalence.tex:49`,
`tate-T3-quillen-equivalence.tex:95`.

Deciding evidence: a Costello-locality proof in the selected weighted
habitat, or a narrowed theorem that never invokes the missing analytic
QME package.

Likely next lane: Costello locality / weighted RG analytic proof lane.

### LO-07. All-\(N\) radial/Weyl trace comparison

Target theorem: the all-\(N\) Weyl/Moyal trace normalization used by the
degree-zero radial comparison.

Current proved branch: formal Moyal coefficients and reduced open-line
Wick weights are proved; \(K_{4,4}\) is verified in the free indexed
trace-diagram algebra; finite-rank checks are evidence only.

Missing data/object/map/homotopy: a functorial contracting homotopy on
\(\ker\partial\) producing \(K_{a,b}\), or a replacement by radially
normalized generators propagated through the stable trace theorem.

Exact obstruction:
\[
  E_{a,b,N}\in \mathcal W_N\widehat\mu(\mathfrak{sl}_N),
  \qquad
  E_{a,b,N}=\sum_{i,j}A^j{}_i(a,b,N)\widehat\mu^i{}_j,
\]
equivalently
\[
  \mathcal N_{\mathrm{free}}(K_{a,b})=R^{\mathrm{free}}_{a,b}.
\]

Responsible surface: `appendix-radial-parts-moyal.tex:214`,
`appendix-radial-parts-moyal.tex:401`,
`appendix-radial-parts-moyal.tex:713`,
`appendix-radial-parts-moyal.tex:815`,
`scripts/quantum_shear_trace_diagram_normal_form.py`.

Deciding evidence: an explicit all-bidegree homotopy or closed formula for
\(K_{a,b}\), verified in the free diagram algebra before finite-rank
specialization.  Agent 152 is named for this lane; no local report is
present.

Likely next lane: radial kernel-contracting-homotopy lane.

### LO-08. Holomorphic-defect / complex-line restriction before VOA/OPE

Target theorem: any one-dimensional vertex/OPE algebra attached to the
local twofold theory.

Current proved branch: local holomorphic factorization on the formal
\(\mathbb C^2\)-disk, the mixed topological-current enhancement, Weyl/Moyal
brane algebra, cyclic trace avatars, and principal-part interval currents
are separated.  No VOA/OPE theorem follows.

Missing data/object/map/homotopy: a line or defect germ
\(\iota_L\colon\operatorname{Spf}\mathbb C[[w]]\hookrightarrow
\widehat{\mathbb C^2}_0\), transverse boundary condition
\(\mathcal B_\perp\), restriction functor \(\mathsf R_{L,\mathcal B_\perp}\),
factorization-to-vertex comparison, finite singular OPEs, vacuum,
translation, locality, and Weyl/Moyal compatibility via
\(\zeta_{L,\hbar}\) or fields \(J_f(w)\).

Exact obstruction: no cohomology class has been computed; the obstruction
is absence of the restriction tuple
\[
  \mathfrak R_L=(\iota_L,\mathcal B_\perp,\mathsf R_L,
  V_L,\mathbf 1_L,T_L,Y_L,\zeta_{L,\hbar}).
\]

Responsible surface: `local-dictionary.tex:281`,
`local-dictionary.tex:306`,
`local-dictionary.tex:332`,
`theorem-lanes.tex:349`,
`reconstitution/swarm-2026-04-30-agent-155-holomorphic-defect-voa-restriction.md`.

Deciding evidence: construction of \(\mathfrak R_L\) and verification of
vacuum, translation, locality, finite-pole OPE, and Weyl/Moyal zero-mode
compatibility.

Likely next lane: holomorphic-defect restriction constructor.  Agent 155's
report is present locally; Agent 159 foregrounds the taxonomy but leaves
the theorem obligation open.

### LO-09. Tate/bar-cobar and mixed Koszul admissible envelopes

Target theorem: bar-cobar, CE/Koszul, and stable open-side
\(A_\infty\)-Koszul comparisons beyond the strict ML finite-window habitat.

Current proved branch: the strict ML Tate habitat is constructed; ML
exactness and \(\varprojlim^1=0\) hold there.  Degreewise stable trace and
primitive one-\(\psi\) PBW shadows are proved as local algebraic statements.

Missing data/object/map/homotopy: a target-specific admissible model
envelope with transfer, smallness, monoid axiom, finite-window
compatibility, local conilpotence of twisting cochains, and the mixed
two-colour/Swiss-cheese operadic data if the theorem is upgraded to an
unreduced or physical large-\(N\) statement.

Exact obstruction: the universal strict endpoint is blocked by the
direct-sum support/Casimir obstruction; open-side cobar upgrades are
governed by the obstruction complex
\(\mathcal O_{\mathrm{cobar}}(\tau)\).  No physical large-\(N\)
BV-state/correlator class has been constructed.

Responsible surface: `tate-T3-quillen-equivalence.tex:132`,
`tate-T3-quillen-equivalence.tex:369`,
`tate-T3-quillen-equivalence.tex:471`,
`tate-T3-quillen-equivalence.tex:804`,
`theorem-lanes.tex:105`,
`theorem-lanes.tex:1307`,
`theorem-lanes.tex:1389`,
`tate-T5-chain-level-primitive.tex:101`,
`tate-T5-chain-level-primitive.tex:690`.

Deciding evidence: a concrete admissible envelope and twisting cochain with
zero MC curvature, associated-graded cone acyclicity, zero Milnor defects,
and verified stable trace/Koszul compatibility in the target category.

Likely next lane: mixed Koszul / admissible-envelope proof constructor.

### LO-10. Integration build and reference gate

Target theorem: none.  This is the verification gate for the local theorem
surface after concurrent edits land.

Current proved branch: Agent 150 reports an isolated clean draft build with
no undefined references or duplicate labels at that time.  Later Agent 153,
155, 156, 158, and 159 edits landed after that evidence window.

Missing data/object/map/homotopy: a final main-thread clean-aux build and
reference scan after live lanes have reported or been marked absent.

Exact obstruction: stale root auxiliary state can produce false TeX
failures.  This is not a mathematical obstruction.

Responsible surface: `reconstitution/swarm-2026-04-30-agent-150-local-build-reference-audit.md`,
`Makefile`, current TeX tree.

Deciding evidence: clean-aux `make pdf` or equivalent isolated build after
integration, plus duplicate-label and undefined-reference scans.

Likely next lane: integration/build verification lane.

### LO-11. Native holomorphic \(E_2\) / \(\mathbb C^2\) factorization theorem

Target theorem: construct the native holomorphic factorization algebra on
the complex surface \(\mathbb C^2\), not a curve VOA:
\[
  V_{\mathrm{Ham}}^{(2)}(B)
  =
  C^\bullet_{\mathrm{CE}}
  \bigl(\Omega_c^{0,\bullet}(B)\widehat\otimes
  (\mathfrak h\ltimes P[1])\bigr).
\]

Current proved branch: the CE/factorization observable assignment is
recorded for the formal Hamiltonian local model.

Missing data/object/map/homotopy: explicit holomorphic collision
operations in complex codimension two, Bochner-Martinelli kernel
normalization, compatibility with the Hamiltonian bracket and coadjoint
action, and a proof that any use of "chiral" means this
two-complex-dimensional factorization object unless a reduction theorem is
invoked.

Exact obstruction: no curve OPE, Zhu, or \(SC_{\mathrm{ch,top}}\) theorem
is native to \(\mathbb C^2\).  Those require LO-12 and LO-13.

Likely next lane: native holomorphic \(E_2\) / Bochner-Martinelli kernel
constructor.

### LO-12. Controlled \(\mathbb C\times\mathbb R\) reduction theorem

Target theorem: construct a reduction from
\[
  \mathbb R^2_{\mathrm{top}}\times\mathbb C^2_{\mathrm{hol}}
  \to
  \mathbb R_t\times\mathbb C_{z_1}
\]
with retained \(z_2\)-modes or principal-part coefficients.

Missing data/object/map/homotopy: projection
\(\pi(t,s;z_1,z_2)=(t;z_1)\), topological de Rham contraction or compact
support pushforward, holomorphic zero-mode or residue pushforward,
brane image \(L_{\mathrm{red}}\), reduced BV pairing, induced bracket,
principal-part transport, scalar-anomaly transport, and comparison to
Vol II only after these maps exist.

Exact obstruction: setting \(z_2=0\) kills the Hamiltonian bracket.  A
faithful reduction must keep
\[
  \mathfrak h_{\mathrm{red}}=\mathbb C[[z_1]][[z_2]]/\mathbb C\cdot1
\]
or the corresponding residue/principal-part coefficient system.

Likely next lane: controlled reduction datum and pushed-forward field
equations.

### LO-13. Reduced Dirac BRST chiral algebra and Zhu bridge

Target theorem: after LO-12, construct the reduced Dirac BRST vertex
algebra and its Zhu/Hochschild/CE-PV comparison.

Candidate object:
\[
  A_{\partial,N}^{\mathrm{Dir\text{-}ch}}
  =
  H^\bullet(V_N^{\mathrm{Dir}},Q_{\mathrm{BRST}}),
  \qquad
  j_{\mathrm{BRST}}
  =
  \operatorname{Tr}(c[Z_1,Z_2])
  +\frac12\operatorname{Tr}(b[c,c]).
\]

Missing data/object/map/homotopy: OPE convention, conformal weights,
proof \(Q_{\mathrm{BRST}}^2=0\), invariant/BRST cohomology, zero-mode
identification with the Dirac brane algebra, Zhu algebra computation, and
Hochschild-to-HKR-to-CE/PV comparison.

Exact obstruction: the Zhu algebra is a reduction bridge, not a native
\(\mathbb C^2\) object.  At finite \(N\), the relation includes the
Capelli/Weyl shift \(YX-XY+\hbar NI=0\).

Likely next lane: reduced Dirac BRST/Zhu bridge constructor.

### LO-14. Normal \(\Omega\)-background equivariant refinement

Target theorem: formulate and prove the normal equivariant localization
surface for the brane line with parameters
\[
  T_\Omega=
  \mathbb C^*_{\varepsilon_s}\times
  \mathbb C^*_{\varepsilon_1}\times
  \mathbb C^*_{\varepsilon_2}.
\]

Missing data/object/map/homotopy: weight conventions for \(s,z_1,z_2\),
Hamiltonian and principal-part bases, residue pairing, CE/PV map,
open trace map, Moyal parameter, fixed-locus localization, and reduced
brane-line equations.

Exact obstruction: the \(\Omega\)-background gives a grading and
localization theorem surface.  It does not by itself prove Costello
kernel convergence, non-scalar QME, scalar-anomaly cancellation, or
physical large-\(N\) duality.

Likely next lane: equivariant weights/localization and refined Moyal
parameter lane.

### LO-15. Stratified factorization algebra and protected trace surface

Target theorem: formulate the brane as a lower stratum in a stratified
mixed HT factorization algebra on
\[
  (X,L)=
  \bigl(\mathbb R^2_{t,s}\times\mathbb C^2_{z_1,z_2},
  \mathbb R_t\times\{s=z_1=z_2=0\}\bigr).
\]

Missing data/object/map/homotopy: the stratified prefactorization
assignment for bulk opens, brane intervals, and mixed neighborhoods; the
brane module or boundary algebra \(A^q_{N,\Omega}\); compatibility of
extension-by-zero products with the closed-open operations; the
brane-defect Costello QME package; and a trace/state functional if
physical large \(N\) is claimed.

Exact obstruction: analogy with external Chern-Simons or M2/M5
\(\Omega\)-background constructions is not admissible evidence.  The
paper needs its own reduced BV theory, defect module, centrality
homotopies, and factorization-homology trace normalization.

Likely next lane: stratified factorization and trace-state theorem
surface.

## Quarantined External Surfaces

Compact Calabi-Yau, CoHA, quintic, OSV/GV, Abel-Jacobi, MNOP, Vol III,
Igusa, Borcherds, and BKM obligations are external comparison only.  If the
principal reopens any such lane, it must supply target data, comparison
maps, obstruction vectors, and compatible null-homotopies, for example an
\(\operatorname{Ob}_{\mathrm{UKD}}(C_{\mathrm{tar}})=0\) theorem.  None of
these data is part of the core local theorem list above.
