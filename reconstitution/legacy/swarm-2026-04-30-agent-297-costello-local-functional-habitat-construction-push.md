# Agent 297 Costello Local-Functional Habitat Construction Push

Status: report-only.  Wrote the habitat construction report and did not
edit TeX.

## Claim Attacked

The lane attacked the assertion that the missing scalar-zero counterterm
columns for the non-scalar Costello graph/QME problem can be added by
formal naming.  They cannot.  A column is meaningful only in a filtered
Costello local-functional habitat with a chain scalar projection,
wavefront/locality rule, finite-window projections, admissible weight
transport, and zero Roos primitive class.

## Construction Result

Defined the strongest habitat currently supported by the manuscript:
\[
  \mathfrak Q^\bullet_{\mathcal G,\Lambda,M}(I)
  =
  \left(
  \mathcal O^{\mathrm{bd}}_{\mathrm{loc},\mathcal G,\Lambda,M}
  (\mathcal E_w^M|_I;A^{\mathrm{pp},w,M}_{\partial,\hbar}(I)),
  d_M=Q+\{I^w_{0,M},-\}_{\hbar,M}
  \right),
\]
completed in the \(\hbar\)-adic, scalar-contact, and finite-window
filtrations.  The label class is restricted to regular compactly
supported densities, graphwise wavefront-admissible tuples, or the
one-sided finite-scaling sign-conic habitats
\(\mathcal D'_{c,\Lambda_\pm,\mathrm{fs}}(I)\).  There is no present
theorem for all of \(\mathcal D'_c(I)\).

The Hom-valued convolution habitat is
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
  \operatorname{Curv}_{\mathbf K,M}(\kappa)
  =
  d_{\mathbf K,M}\kappa+\frac12[\kappa,\kappa]_{\mathbf K,M}.
\]
The source-face term is essential.

Scalar-zero columns live in
\[
  \mathcal K^\bullet_{\mathrm{ns},M}(I)
  =
  \ker\widehat\sigma_{\mathrm{sc},M}
\]
only after \(\widehat\sigma_{\mathrm{sc},M}\) is a filtered chain map.
The finite-window equations are
\[
  A^Mc_M=-r^M,\qquad
  T^{M,N}A^M=A^NP^{M,N},\qquad
  [P^{M,N}c_M-c_N]=0.
\]

## Blocked Column

The direct \(\theta_3\) column would require
\[
  C^{\mathrm{ct}}_{\theta_3,M}\in
  \mathcal K^0_{\mathrm{ns},M}(I),\qquad
  d_MC^{\mathrm{ct}}_{\theta_3,M}=-\mathsf E_{\theta_3,M},
  \qquad
  \widehat\sigma_{\mathrm{sc},M}(C^{\mathrm{ct}}_{\theta_3,M})=0,
\]
with wavefront/locality support and zero Roos class.  This is not present
in the current data.

The lower Bianchi route would require
\[
  B^2_{02,20}\in\mathcal K^0_{\mathrm{ns},2}(I),
  \qquad
  d_{\mathrm{ns},2}B^2_{02,20}=-\mathfrak b^2_{02,20}.
\]
Without it,
\[
  A_D^2=(-2,2,1)^T,\qquad r_2=(2,-2,0)^T
\]
has no solution.  Adding the column gives
\[
  A^2_{D,B}
  =
  \begin{pmatrix}
  -2&0\\
  2&0\\
  1&-1
  \end{pmatrix},
  \qquad
  A^2_{D,B}(1,1)^T=-r_2,
\]
but the local counterterm producing that second column is not constructed.

## Exact Missing Theorem

Either prove a theta-three local counterterm exactness theorem:
\[
  d_MC^{\mathrm{ct}}_{\theta_3,M}=-\mathsf E_{\theta_3,M}
\]
in the restricted Costello local-functional habitat, with scalar-zero
value, wavefront/locality support, finite-window transport, and zero Roos
class; or prove the lower Bianchi-defect counterterm theorem:
\[
  d_{\mathrm{ns},2}B^2_{02,20}=-\mathfrak b^2_{02,20}
\]
with the same locality and transport data.  The analytic estimate needed
in either case is a finite-scaling local-extension/counterterm estimate
for the specific Hadamard-current product representing the row, compatible
with interval extension, \(\pi_{M,N}\), and \(R^M_{w,w'}\).

## Anchors

- `main.tex:8365-8599`: non-scalar QME obstruction complex.
- `main.tex:8601-8804`: \(\theta_3\) acceptance gate and lower Bianchi
  obstruction.
- `appendix-factorization-current-conventions.tex:992-1107`: unreduced
  current lift and convolution habitat.
- `appendix-factorization-current-conventions.tex:1279-1860`: regular and
  wavefront graph-current habitats.
- `appendix-unreduced-bv-qme.tex:2142-2385`: native finite-window
  realization habitat and row criterion.
- `tate-P1-hadamard-mittag-leffler.tex:379-609`: finite-window graph/QME
  package and assembly.
- `tate-T1-weighted-completion.tex:1172-1327`: non-scalar tower and Roos
  counterterm criterion.
- `references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md:40-240`:
  Costello support and non-support.

## Verification

Ran:

```bash
python3 -m py_compile scripts/finite_window_graph_array.py
python3 scripts/finite_window_graph_array.py
```

The script still reports the minimal full-equivariant order-two branch as
zero, the \(\theta_3\) one-row subcomplex as obstructed, the exact
counterterm payload as accepted only when its differential coefficient is
\(-1\), and the eight-face companion route as rejected because the marked
Costello incidence/weight table and lower-window transport identity are
absent.

## Files Changed

- `reconstitution/costello-local-functional-habitat-construction-push-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-297-costello-local-functional-habitat-construction-push.md`
