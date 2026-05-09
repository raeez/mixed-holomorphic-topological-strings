# Swarm Report: Agent 306 -- LQT Separated-Block Zigzag Proof Construction

Date: 2026-04-30

Lane: LQT separated-block zigzag proof construction.

Ownership: report-only.  No TeX edited.

## Claim Attacked

The finite-rank bridge from the stable block-sum Hopf LQT projection to a
matrix CE window is the separated-block zigzag
\[
  P^{\mathrm{sep}}_{M,K,L}
  =
  \beta_{M,K,L}P_{1\mathrm{cyc}}\alpha_{M,K,L},
  \qquad
  M=L\max(K,L+2).
\]
The requested point was to prove the maps
\(\alpha_{M,K,L}\), \(\beta_{M,K,L}\), their chain-map identities, and the
stable range.

## Result

Closed, with one precision repair.

The exact \(\beta_{M,K,L}\) for the graded symmetric stable Hopf window is not
the unsymmetrized first-\(m\)-blocks placement.  It is the normalized signed
average over injections into the \(L\) labeled blocks:
\[
  \beta_{M,K,L}(z_1\cdots z_m)
  =
  \frac{1}{(L)_m}
  \sum_{f:\{1,\ldots,m\}\hookrightarrow\{1,\ldots,L\}}
  \theta_{f(1)}(z_1)\wedge\cdots\wedge\theta_{f(m)}(z_m),
\]
where \((L)_m=L(L-1)\cdots(L-m+1)\).  This descends to the graded symmetric
product and gives
\[
  \alpha_{M,K,L}\beta_{M,K,L}=\mathrm{id}.
\]

The read-back map \(\alpha_{M,K,L}\) forgets block labels and multiplies the
connected stable factors in the graded symmetric Hopf algebra.  It is a chain
map because separated diagonal block Lie subalgebras commute, so the CE
differential has no cross-block bracket term.

Therefore
\[
  P^{\mathrm{sep}}_{M,K,L}
  =
  \beta_{M,K,L}P_{1\mathrm{cyc}}\alpha_{M,K,L}
\]
is a strict chain idempotent on the separated-block subcomplex:
\[
  (P^{\mathrm{sep}}_{M,K,L})^2=P^{\mathrm{sep}}_{M,K,L},
  \qquad
  d_{\mathrm{CE}}P^{\mathrm{sep}}_{M,K,L}
  =
  P^{\mathrm{sep}}_{M,K,L}d_{\mathrm{CE}}.
\]

## Stability Range

Set
\[
  B(K,L)=\max(K,L+2),\qquad M=L\,B(K,L).
\]
The block size \(B(K,L)\) is the stable rank per occupied block.  The total
rank \(M\) appears because a CE-length-\(\leq L\) monomial has at most \(L\)
connected Hopf factors.

Source-dependent range inputs:

- Procesi 1976 and Razmyslov 1974: trace-identity stability in total
  word/Koszul degree \(\leq K\).
- Loday--Quillen 1984, Theorem 6.9: homological stabilization
  \(H_i(\mathfrak{gl}_{n-1}(A))\to H_i(\mathfrak{gl}_n(A))\) is an
  isomorphism for \(i<n-1\), giving the safe \(n\geq L+2\) clause.

Not used as a proof of this dg finite-window zigzag:

- Loday--Quillen 1984, Theorem 6.2.  It remains only the stable external
  template \(\operatorname{Prim}H_n(\mathfrak{gl}_\infty(A))\cong
  HC_{n-1}(A)\).

## Failure Mode Retained

The same-rank fold is still false without an all-window collision homotopy.
The obstruction is
\[
  \Gamma_N=d_{\mathrm{same}}F_N-F_Nd_{\oplus},
  \qquad
  \Gamma_N(\Theta_1^N(a)\wedge\Theta_1^N(b))
  =
  \pm\Theta_1^N(ab-(-1)^{|a||b|}ba).
\]
Thus the proved bridge is separated-block stabilization.  It is not a
same-rank endomorphism of one exterior CE complex.

## Files Written

- `reconstitution/lqt-separated-block-zigzag-proof-construction-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-306-lqt-separated-block-zigzag-proof-construction.md`

## Checks

Read anchors included `CLAUDE.md`, `AGENTS.md`, the local rectify harness,
the delegated Vol II rectify harness, `main.tex:1848-2020`,
`theorem-lanes.tex:2070-2135`, `open-obligations.tex:143-200`,
`claim-strength-ledger.tex:388-426`, the Agent 295 fixed-rank bridge report,
the Agent 302 integration audit, and the LQT/Tsygan source anchor file.

Computed checks:

- Eulerian logarithm coefficient equals \(1\) on one connected factor and
  \(0\) on \(2,\ldots,8\) connected factors.
- Injection counts \((L)_m\) are nonzero for \(m\leq L\), justifying the
  characteristic-zero normalization in \(\beta_{M,K,L}\).

No PDF build was run.
