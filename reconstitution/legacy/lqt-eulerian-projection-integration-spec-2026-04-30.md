# LQT Eulerian Projection Integration Spec

Date: 2026-04-30

Purpose: TeX-ready integration target for the finite-window
Loday--Quillen--Tsygan projection repair.

## Core Statement

Use the stable block-sum Hopf CE complex.  Do not use same-rank deletion of
multicycle tensors.

For Koszul weight \(K\) and CE length \(L\),
\[
  A_{\psi,K}=A_\psi/F^{>K}A_\psi,
  \qquad
  N\geq\max(K,L+2).
\]
Let \(J=\mathrm{id}-u\epsilon\).  In the stable block-sum Hopf CE window,
\[
  P_{1\mathrm{cyc}}
  =
  \log^*(\mathrm{id})
  =
  \sum_{m=1}^{L}\frac{(-1)^{m-1}}{m}J^{*m}.
\]
Then
\[
  P_{1\mathrm{cyc}}^2=P_{1\mathrm{cyc}},
  \qquad
  d_{\mathrm{CE}}P_{1\mathrm{cyc}}
  =
  P_{1\mathrm{cyc}}d_{\mathrm{CE}},
  \qquad
  \operatorname{im}P_{1\mathrm{cyc}}=\operatorname{im}\Theta_{N,K,L}.
\]
The finite-window map is
\[
  \lambda_{\mathrm{LQT},K,L}
  =
  \Theta_{N,K,L}^{-1}P_{1\mathrm{cyc}}.
\]
If one symbol \(W\) bounds both \(K\) and \(L\), use \(N\ge W+2\).

## False Projection Fence

The raw projection
\[
  P_{\mathrm{del}}=\text{``keep fixed-rank one-cycles, delete fixed-rank multicycles''}
\]
is not a chain map.  For homogeneous \(a,b\),
\[
  P_{\mathrm{del}}d_{\mathrm{CE}}
  \bigl(\Theta_1(a)\wedge\Theta_1(b)\bigr)
  =
  \pm\Theta_1(ab-(-1)^{|a||b|}ba),
  \qquad
  d_{\mathrm{CE}}P_{\mathrm{del}}
  \bigl(\Theta_1(a)\wedge\Theta_1(b)\bigr)=0.
\]
This obstruction must appear wherever the manuscript risks reading
\(P_{1\mathrm{cyc}}\) as fixed-rank deletion.

## Insertions

1. `theorem-lanes.tex`: replace the K3 finite-window LQT clause with the
   two-parameter stable Hopf construction, the trace-cycle formula, the
   cyclic relation, the Eulerian idempotent, the stable range, the scalar
   two-term quotient, and the false-projection fence.
2. `open-obligations.tex`: change the LQT item from open obstruction tuple to
   healed stable tuple, retaining scalar quotient conditions and the larger
   open \(A_\infty\), \(\Psi\to\rho\), BV/QME obligations.
3. `claim-strength-ledger.tex`: mark the LQT component theorem-grade in the
   stable block-sum Hopf finite window and false for same-rank deletion.
4. `main.tex`: after the external LQT theorem, state the internal stable
   Eulerian finite-window construction and the same-rank deletion obstruction;
   sharpen connected large-\(N\) extraction to mean the stable cumulant
   idempotent.

## Scalar Quotient

The scalar one-\(\psi\) line is not killed alone at chain level:
\[
  d_{\mathrm{CE}}\Theta_1(\psi)=\Theta_1(xy-yx).
\]
The Hamiltonian scalar quotient is a chain quotient only after quotienting by
\[
  \Theta_1(\psi)\mapsto\Theta_1(xy-yx),
  \qquad
  [\psi]\mapsto[xy-yx],
\]
or after homology.

## Source Boundary

Loday--Quillen 1984 and Tsygan 1983 support the stable homological template
\[
  \operatorname{Prim}H_*^{\mathrm{CE}}(\mathfrak{gl}_\infty(A);\C)
  \cong
  HC_{*-1}(A).
\]
They do not prove the dg finite-window \(A_\psi\) chain map, scalar quotient,
open \(A_\infty\) transfer, \(\Psi\to\rho\) bridge, or BV/QME package.
