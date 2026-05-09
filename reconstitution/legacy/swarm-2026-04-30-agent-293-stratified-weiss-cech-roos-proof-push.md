# Agent 293 Stratified Weiss Cech/Roos Proof Push

Date: 2026-04-30.

Scope: report-only.  Writable ownership was restricted to this file and
`reconstitution/stratified-weiss-cech-roos-proof-push-2026-04-30.md`.
No TeX was edited.

## Claim Attacked

The lane claim under attack was:

> The reduced product-basis prefactorization datum can be upgraded to
> full stratified Weiss descent for
> \((X,L)=(\mathbb R_t\times\mathbb R_s\times\mathbb C^2,
> \mathbb R_t\times\{s=z_1=z_2=0\})\).

## Result

The upgrade closes only as an obstruction theorem.

The reduced product-basis datum is proved: bulk product disks carry the
mixed CE/factorization object, brane intervals carry
\(A^{\mathrm{pp},w}_{\partial,\Omega,\hbar_{\mathrm{W}}}\), and products
are extension by zero followed by CE or completed symmetric
multiplication.  Thus \(\delta_{\mathrm{pref}}\) and
\(\delta_{\mathrm{assoc}}\) vanish on that reduced basis.

Full stratified Weiss descent is blocked by the Cech/Roos obstruction:
\[
  \delta_{\mathrm{Weiss}}^{\check C/R}
  =
  \left(
    \{H^\bullet(\Delta_{V,\mathcal U}^{N,M})\}_{(V,\mathcal U,N,M)},
    \mathfrak w^{\check C/R}_{V,\Omega,N,M}
  \right).
\]
Here
\[
  \Delta_{V,\mathcal U}^{N,M}
  =
  \operatorname{Cone}\left(
  \mathcal F^{\mathrm{str}}_{\Omega,N,M}(V)
  \to
  \operatorname{Tot}\check C^\bullet
  (\mathcal U;\mathcal F^{\mathrm{str}}_{\Omega,N,M})
  \right),
\]
with cohomological cone differential
\[
  d_\Delta(b,x)=
  (\mathbb D b+r_{V,\mathcal U}(x),-d_{\mathcal F}x).
\]
A nonzero class \([(b,x)]\in H^q\Delta_{V,\mathcal U}^{N,M}\) is the
cover-level descent obstruction.

The refinement/window compatibility obstruction is
\[
  \mathfrak w^{\check C/R}_{V,\Omega,N,M}
  =
  [\operatorname{id}_{\Delta_\bullet}]
  \in
  H^0\operatorname{Tot}
  \operatorname{Roos}\left(
    \mathsf{Ref}^{\mathrm{str}}_{\mathrm W}(V);
    \underline{\operatorname{End}}(\Delta_\bullet)
  \right).
\]
It vanishes only after compatible continuous contractions of the cone
system are constructed.

## Internal Vector

Use the nine-component internal vector:
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

The source-primary class
\(\operatorname{ob}^{\mathrm{src}}_{\mathrm{CFG}}\) is external.  It is
a matched-conventions gate for importing AFT, Costello--Gwilliam,
Weiss/Ran, Costello \(\Omega\)-background, or CFG trace theorems.  It
does not belong to
\(\operatorname{Ob}^{\mathrm{int}}_{\mathrm{str},\Omega,N}\).

## Evidence

- `theorem-lanes.tex:3007-3206`: stale seven-component vector and
  parameter collision remain on the stratified trace lane.
- `open-obligations.tex:1005-1010`: descent defect is still the old
  holim-style expression; it should be a Cech cone.
- `open-obligations.tex:1012-1089`: centrality homotopies and basicness
  are separate unreduced QME obligations.
- `claim-strength-ledger.tex:774-798`: stratified factorization is still
  a construction target with the stale vector.
- `main.tex:1175-1235`: reduced product-basis products are supported by
  extension by zero.
- `references/primary-sources/weiss-ran-stratified-descent-source-anchors-2026-04-30.md`:
  source material supplies descent grammar, not this mixed HT proof.

## Files Changed

- Added this report.
- Added `reconstitution/stratified-weiss-cech-roos-proof-push-2026-04-30.md`.

No build was run.
