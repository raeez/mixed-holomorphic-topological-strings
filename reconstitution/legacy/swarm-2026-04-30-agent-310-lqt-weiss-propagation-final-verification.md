# Agent 310 LQT/Weiss Propagation Verification

Date: 2026-04-30.

Worktree: `/Users/raeez/topological-strings`.

Owned files:

- `reconstitution/lqt-weiss-propagation-final-verification-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-310-lqt-weiss-propagation-final-verification.md`

No TeX was edited.

## Claim Attacked

After the latest patches, verify whether either defect remains:

1. LQT \(K,L/W\) collision, same-rank deletion, or missing
   separated-block propagation.
2. Weiss \(\delta_{\mathrm{Weiss}}^{\check C/R}\) propagation failure.

## Result

The LQT lane is clean.  Current live anchors agree:

- `main.tex:1903-2039`;
- `theorem-lanes.tex:2079-2143`;
- `open-obligations.tex:143-208`;
- `claim-strength-ledger.tex:398-449`.

These anchors use \(K,L\) as the primary finite windows, \(W\) only as
the one-bound abbreviation \(K,L\le W\), and record
\[
  P^{\mathrm{sep}}_{M,K,L}
  =
  \beta_{M,K,L}P_{1\mathrm{cyc}}\alpha_{M,K,L},
  \qquad
  M=L\max(K,L+2),
\]
together with
\[
  \Gamma_N=d_{\mathrm{same}}F_N-F_Nd_{\oplus}.
\]
No live manuscript-facing hit still promotes raw same-rank deletion to a
chain map.

The Weiss lane is mostly clean, with one residual ledger row.

Fixed anchors:

- `theorem-lanes.tex:3130-3180`;
- `theorem-lanes.tex:3181-3195`;
- `open-obligations.tex:1047-1066`;
- `open-obligations.tex:1158-1187`;
- `claim-strength-ledger.tex:183-190`;
- `claim-strength-ledger.tex:820-872`.

Remaining anchor:

- `claim-strength-ledger.tex:451-461` still ends the full open BV
  factorization-center obstruction vector with bare
  \(\delta_{\mathrm{Weiss}}\).

Recommended exact replacement:

```tex
  Failure is
  \((\operatorname{ob}^{\mathrm{prod}}_{\mathrm{cent}},
  \operatorname{ob}^{P_0}_{\mathrm{cent}},
  \operatorname{ob}^{\mathrm{bd}}_{\mathrm{QME}},
  \delta_{\mathrm{Weiss}}^{\check C/R})\).
```

Stronger ledger replacement:

```tex
  Failure is
  \((\operatorname{ob}^{\mathrm{prod}}_{\mathrm{cent}},
  \operatorname{ob}^{P_0}_{\mathrm{cent}},
  \operatorname{ob}^{\mathrm{bd}}_{\mathrm{QME}},
  \delta_{\mathrm{Weiss}}^{\check C/R})\), where the Weiss term is the
  coverwise Cech cone together with the Roos compatibility class defined
  in the stratified factorization row below.
```

## Claim-Status Recommendation

- LQT \(K,L/W\): cleared.
- LQT same-rank bridge: cleared as an obstruction, not a theorem.
- Weiss \(\delta_{\mathrm{Weiss}}^{\check C/R}\): cleared on theorem
  lane and open obligations; one claim-ledger propagation patch remains.

No build was run.  This was a report-only verification.
