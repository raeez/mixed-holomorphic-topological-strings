# Agent 308 - Theta3 Restricted-Habitat Counterterm Theorem Design

Date: 2026-04-30

Lane: theta3 restricted-habitat Bianchi-defect counterterm theorem
design.

Ownership: report only.  No TeX edits.

## Claim Attacked

Can the current Costello/local-functional theta3 habitat construct
\[
  B^M_{02,20}
\]
with
\[
  d_{\mathrm{ns},M}B^M_{02,20}=-b^M_{02,20}
\]
and compatible scalar-zero, locality, wavefront, and Roos transport
data?

## Finding

No current report or TeX surface constructs \(B^M_{02,20}\).  The
current \(M=2\) habitat contains the lower-source column
\[
  A^2_D=(-2,2,1)^T
\]
but not the needed Bianchi-defect column
\[
  A^2_B=(0,0,-1)^T.
\]
The covector
\[
  \widetilde\lambda
   =\tfrac12(E^2_{\nu_{02}})^*+(b^2_{02,20})^*
\]
kills \(A^2_D\) and evaluates nontrivially on the residual, so the
present habitat is obstructed.

## Evidence Checked

- Current theta3 surfaces in `main.tex`, `theorem-lanes.tex`,
  `open-obligations.tex`, and `claim-strength-ledger.tex`.
- Finite-row and companion-face gates in
  `tate-P1-hadamard-mittag-leffler.tex`.
- Native realization and row-matrix criterion in
  `appendix-unreduced-bv-qme.tex`.
- Regular-density and wavefront-admissible habitats in
  `appendix-factorization-current-conventions.tex`.
- Weighted inverse-limit/Roos criterion in
  `tate-T1-weighted-completion.tex`.
- Reconstitution reports on Costello source-theorem search, local
  functional habitat construction, theta3 B-column construction,
  Bianchi closure, matrix integration, companion faces, non-diagonal
  transport, and Roos obstruction.
- Primary anchor reports for Costello graph/QME local functionals and
  H\"ormander wavefront operations.

I also checked the finite-window graph script output.  It still reports
the theta3 row obstruction, the eight-face residual, and acceptance only
for supplied exact primitives with differential entry \(-1\).

## Theorem Designed

The required theorem is:

> In the native finite-window brane-defect Costello habitat, with the
> marked theta3 Bianchi package codimension-two closed, restricted to
> regular-density labels or graphwise wavefront-admissible finite-scaling
> labels, and with scalar projection plus window/interval/weight
> transport, there exist degree-zero local counterterms
> \(B^M_{02,20}\in Q^0_{\mathrm{ns},M}\) supported on allowed
> collision/source-face strata such that
> \[
>   d_{\mathrm{ns},M}B^M_{02,20}=-b^M_{02,20}.
> \]
> At \(M=2\), this gives the column \((0,0,-1)^T\) in the basis
> \((E^2_{\nu_{02}},E^2_{\nu_{20}},b^2_{02,20})\), with no scalar
> leakage and with strict transport or vanishing corrected Roos class.

The full theorem statement, hypotheses, estimates, redundancies, and
missing data are recorded in
`reconstitution/theta3-restricted-habitat-counterterm-theorem-design-2026-04-30.md`.

## Nonredundant Clauses

The theorem must include:

1. Native mixed HT finite-window local-functional habitat, not compact
   CY or curve chiral replacement.
2. Marked theta3 Bianchi row data and codimension-two closure.
3. Restricted coefficient habitat: regular densities or graphwise
   wavefront-admissible finite-scaling currents, not all
   \(\mathcal D'_c(I)\).
4. Pullback non-characteristic, product transversality, finite scaling
   degree, local extension, pushforward wavefront, and small-scale
   counterterm estimates.
5. Filtered chain scalar projection and scalar-zero conclusion for the
   constructed \(B\).
6. \(M=2\) row coordinate computation with no extra
   \(E_{\nu_{02}}\) or \(E_{\nu_{20}}\) terms.
7. Finite-window, interval, and weight transport; in the non-strict
   case, \(H^{M,N}\) killing the degree-one transport defect and
   vanishing of the resulting \(\lim^1H^0\) Roos class.

## Redundancies Removed

- \(B\in Q_{\mathrm{ns}}\) and \(\sigma_{\mathrm{sc}}(B)=0\) are the
  same condition.
- \(\sigma_{\mathrm{sc}}(b)=0\) follows from \(dB=-b\) and
  \(B\in Q_{\mathrm{ns}}\) when the scalar projection is a chain map.
- \(A_B=(0,0,-1)^T\) is the \(M=2\) coordinate form of \(dB=-b\), not a
  separate assumption.
- Direct theta3 primitive, CE ancestor, and companion-face table are
  alternate lanes, not hypotheses here.
- All-current \(\mathcal D'_c\) generality is false and was excluded.

## Missing Data

The exact missing construction data are:

1. A concrete marked graph/local counterterm formula for
   \(B^M_{02,20}\).
2. The corresponding incidence maps, source-face labels, graph weights,
   and finite-scale kernels.
3. The graph-specific wavefront and finite-scaling estimates.
4. The local normal-derivative delta formula and extension order for the
   \(B\)-counterterm.
5. The scalar projection proof on the enlarged \(B\)-habitat.
6. The row-coordinate calculation proving \(dB=-b\) with zero
   \(E\)-coordinates.
7. The finite-window transport data or corrected Roos cochains
   \(H^{M,N}\).
8. The Roos vanishing proof, unless strict transport and \(H^0=0\) are
   proved in the actual graph habitat.

## Files Changed

- `reconstitution/theta3-restricted-habitat-counterterm-theorem-design-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-308-theta3-restricted-habitat-counterterm-theorem-design.md`

No TeX files were edited.

## Claim Status

The theorem design is complete.  The mathematical construction of
\(B^M_{02,20}\) remains open until the missing graph/counterterm,
analytic, scalar-zero, and transport data are supplied.
