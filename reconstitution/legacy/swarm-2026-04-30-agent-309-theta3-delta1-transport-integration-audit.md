# Agent 309 Theta3 Delta1 Transport Integration Audit

Date: 2026-04-30.
Lane: theta3 Delta1 transport class integration audit.
Ownership: report-only. No TeX edits.

## Claim Attacked

The current manuscript/control surfaces should make all three objects visible:

1. the transport class
   \[
     \Delta^1_{M,N}=-\pi_{M,N}\mathfrak b^M+\mathfrak b^N;
   \]
2. the \(N=2\) fixed-window cokernel obstruction for
   \((0,0,-1)^T=-\mathfrak b^2_{02,20}\);
3. the secondary \(\varprojlim^1H^0\) primitive-transport class.

## Finding

Failure mode: partial integration.

The fixed-window cokernel is visible in all audited surfaces.  The exact
\(\Delta^1\) class is not visible as a named class in the theorem lane, open
obligations, or claim ledger.  The secondary \(\varprojlim^1H^0\) class is
explicit only in `main.tex`; the other control surfaces retain generic Roos
compatibility language.

## Evidence

- `reconstitution/theta3-h1-bianchi-transport-class-construction-2026-04-30.md`
  supplies the exact construction:
  \(\Delta^1_{M,N}=-\pi_{M,N}\mathfrak b^M+\mathfrak b^N\), the
  \(H^1\)-gate correction \(H^{M,N}\), and the secondary class
  \([\pi_{M,N}B^M-B^N-H^{M,N}]\in\varprojlim^1H^0\).
- `main.tex:8812-8857` exposes the Bianchi lower basis,
  \(A_D^2=(-2,2,1)^T\), \(A_B^2=(0,0,-1)^T\), and
  \(\widetilde\lambda_{02,\mathfrak b}\).
- `main.tex:8859-8867` exposes the correct sign
  \[
    d_{\mathrm{ns},N}(\pi_{M,N}B^M-B^N)
    =
    -\pi_{M,N}\mathfrak b^M+\mathfrak b^N
  \]
  and names the \(H^1\) Bianchi transport class plus secondary
  \(\varprojlim^1H^0\)-class.  It does not introduce the symbol
  \(\Delta^1_{M,N}\).
- `theorem-lanes.tex:3513-3541` exposes the cokernel and missing
  \(B^2_{02,20}\) column.  `theorem-lanes.tex:3542-3556` says the larger rows
  need \(H^1\) and Roos finite-window compatibility, but it does not display
  \(\Delta^1_{M,N}\) or the secondary \(\varprojlim^1H^0\) representative.
- `open-obligations.tex:870-897` exposes the same cokernel.  Its tower display
  at `open-obligations.tex:897-904` uses
  \(\pi_{M,N}\mathfrak b^M_{\mathrm{cand}}-\mathfrak b^N_{\mathrm{cand}}\),
  the \(D\)-candidate sign, not the \(B\)-counterterm sign of
  \(\Delta^1\).
- `claim-strength-ledger.tex:520-537` and
  `claim-strength-ledger.tex:932-955` expose the Bianchi defect, the
  cokernel, and the missing \(B\)-column.  The ledger records
  Bianchi transport / zero Roos compatibility only schematically.

## Claim-Status Recommendation

Record the current status as:

`theta3 Delta1 transport`: theorem-surface-with-missing-integration, not a
computed vanishing theorem.

The strongest true theorem surface is:

- fixed-window \(N=2\): exact obstruction theorem, proved by
  \(\widetilde\lambda_{02,\mathfrak b}\);
- formal \(B^M\)-tower: if constructed with chain maps, then the
  \(H^1\) class is killed by
  \(H_B^{M,N}=\pi_{M,N}B^M-B^N\);
- current checkout: no \(B^2_{02,20}\), no marked Bianchi-row transport
  matrices, and no secondary \(\varprojlim^1H^0\) representative are
  constructed.

## Remaining Open Obligation

Integrate, in TeX by a future owner, the named definition
\[
  \Delta^1_{M,N}:=-\pi_{M,N}\mathfrak b^M+\mathfrak b^N
\]
together with:

\[
  d_NH^{M,N}=\Delta^1_{M,N},
  \qquad
  [\pi_{M,N}B^M-B^N-H^{M,N}]
  \in
  \varprojlim\nolimits^1_M H^0(\mathcal K^\bullet_{\theta_3,M}).
\]

That insertion should be made on the theorem-lane/open-obligations/claim-ledger
surfaces without weakening the fixed-window cokernel obstruction.

## Files Changed

- `reconstitution/theta3-delta1-transport-integration-audit-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-309-theta3-delta1-transport-integration-audit.md`
