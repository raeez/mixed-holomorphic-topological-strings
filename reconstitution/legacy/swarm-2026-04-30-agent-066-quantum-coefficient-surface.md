# Agent 066 Quantum Coefficient Surface Report

## Attacked Claim

Lane attacked: the quantum coefficient package around
`thm:quantum-coefficient-surface`.

The previous local surface had no theorem with that label.  The quantum package
was distributed across the weighted Tate completion, scalar QME appendix,
principal-part current appendix, Moyal/radial-parts lane, and a vague
`prob:quantum-p0-operation-realization` placeholder.

The attacked overclaim risk was silent composition: treating the formal Moyal
degree-zero comparison, weighted BV kernel, scalar QME cancellation, and
principal-part cotangent current sector as if they already formed a full
Costello graph/QME realization.

## Strengthened Statement And Proof Edits

Edited `main.tex` only in the local quantum lane after
`thm:phi-hbar-all-order`.

Added `thm:quantum-coefficient-surface` as a componentwise theorem with product
target
\[
  \mathfrak S_{\hbar,w}(I)=
  \mathcal K_{\mathrm{BV}}^w
  \times\{0_{\mathrm{sc}}\}
  \times A^{\mathrm{pp},w}_{\partial,\hbar}(I)
  \times T_{\mathrm{Ham},\hbar}.
\]

The theorem proves the strongest true surface currently supported:

1. weighted coefficient/BV kernel convergence and graphwise weighted
   boundedness;
2. balanced-supertrace scalar QME cancellation;
3. reduced weighted Moyal principal-part current bracket package;
4. degree-zero Moyal coefficient comparison, conditional on the external
   radial-parts input.

Replaced the vague quantum realization placeholder with
`prob:quantum-p0-operation-realization` as an explicit non-scalar obstruction
complex:
\[
  \mathfrak Q^\bullet_{w,\partial,\hbar}(I)=
  \left(
    \mathcal O_{\mathrm{loc}}^{\mathrm{bd}}
    (\mathcal E_w|_I;A^{\mathrm{pp},w}_{\partial,\hbar}(I)),
    Q+\{I_0^w,-\}_\hbar
  \right).
\]
The remaining theorem obligation is the vanishing of the non-scalar class in
\[
  H^1(\ker\widehat\sigma_{\mathrm{sc}},d_{\mathrm{QME}}),
\]
together with compatible finite-window counterterms and a curved
bulk-to-defect kernel.

## Component Theorems Cited

- `defn:wt-coefficient-pair`, `thm:wt-cotangent-lift`:
  weighted coefficient pair, Casimir convergence, propagator extension,
  graphwise RG compatibility.
- `def:app-scalar-obstruction-complex`,
  `thm:app-balanced-supertrace-qme-cancellation`,
  `thm:scalar-qme-alternatives`:
  scalar obstruction complex, balanced supertrace cancellation, ordinary
  scalar-reduced alternatives.
- `thm:reduced-principal-part-boundary-current`,
  `cor:app-factorization-principal-part-current-brackets`,
  `constr:quantum-principal-part-descendant-target`:
  reduced current brackets and the Moyal principal-part target.
- `prop:quantum-descendant-label-obstruction`,
  `thm:one-psi-label-hbar-obstruction`:
  no transport from polynomial one-psi PBW labels to the Moyal coadjoint target.
- `thm:phi-hbar-all-order`,
  `stmt:app-radial-external-input`:
  conditional degree-zero stable trace comparison.

## New Hypothesis And Map Introduced

Introduced the weighted Moyal principal-part envelope
\[
  A^{\mathrm{pp},w}_{\partial,\hbar}(I)
\]
with
\[
  \mathfrak h_{w,\hbar}=\mathfrak h_w[[\hbar]],\qquad
  \mathfrak h^{\vee,w}_{\hbar,\mathrm{cont}}
  =\mathfrak h^{\vee,w}_{\mathrm{cont}}[[\hbar]].
\]
The Moyal bracket on \(\mathfrak h_{w,\hbar}\) is transported by the diagonal
weight rescaling.  The Moyal coadjoint action on the weighted dual is asserted
only in the vertexwise polynomial-degree-bounded finite-window sector; W2 in
`defn:wt-degree-weight` gives the continuity bound.  Its strict dense Matlis
subtarget is the reduced target of
`constr:quantum-principal-part-descendant-target`.

This closes the `P` to `P_\hbar` transport issue: the theorem now requires the
full Moyal coadjoint action and explicitly excludes the PBW one-psi action.

## Checks Run

- `git diff --check`
- `pdflatex -interaction=nonstopmode -file-line-error -draftmode -output-directory=/tmp/ts-agent-066-texcheck main.tex`

The draftmode TeX pass exited 0.  The log reports the repository's existing
font/box warnings and a rerun notice for labels; it has no TeX errors or
undefined control sequences from this patch.

## Files Changed

- `main.tex`
- `reconstitution/swarm-2026-04-30-agent-066-quantum-coefficient-surface.md`

## Remaining Theorem Obligations

The full non-scalar Costello graph/QME theorem is not closed.  It is now
localized to `prob:quantum-p0-operation-realization`: construct the filtered
local-functional complex, scalar projection, finite-window counterterms,
bulk-to-defect kernel, and prove the non-scalar obstruction class vanishes.

Ledger/theorem-lane propagation may be appropriate after integration, but was
not edited in this lane.
