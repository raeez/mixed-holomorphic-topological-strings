# Swarm 2026-04-30 Agent 307: BMK Pro-Matlis Native Obstruction Integration Audit

Scope: report-only audit.  Wrote no TeX.

## Claim Attacked

The manuscript now states the BMK post-push split:

1. positive one-pair analytic pro-Matlis retract;
2. strict native all-window current \(E_2\) transfer obstructed with all
   listed entries.

## Verdict

Failed.  Partial integration only.

The finite BMK current data and finite-current obstruction gate are present.
The post-push pro-Matlis integration is not complete.

## Verified Present

- `main.tex:1242-1503` proves BMK current-limit data, finite moment maps,
  residue-current sections, the finite obstruction vector
  \(\operatorname{Ob}^{\mathrm{BMK\mbox{-}curr}}_N\), the boundary-mode
  obstruction
  \(z_1^{N+2}\cdot\rho_{N+1,0}=-(N+2)\rho_{0,1}\), and the projected
  finite-window Jacobiator \((N+1)(N+2)\rho_{0,1}\).
- `appendix-factorization-current-conventions.tex:399-677` repeats the
  appendix theorem with the same finite obstruction gate and arity-two
  Hamiltonian/Matlis comparison.
- `theorem-lanes.tex:381-514` records the finite BMK obstruction lane.
- `claim-strength-ledger.tex:319-331` and `claim-strength-ledger.tex:615-649`
  record the finite gate and four-entry all-window target.

## Missing

- The live TeX does not state the positive one-pair analytic pro-Matlis
  retract from
  `reconstitution/bmk-all-window-pro-matlis-transfer-construction-push-2026-04-30.md:14-34`
  and `:143-193`.
- The live TeX does not state the pro-analytic moment map
  \(P_{\Pi}^{\mathrm{an}}=\tau P_{\mathrm{an}}\) with
  \(\pi_NP_{\Pi}^{\mathrm{an}}=p_N\).
- The live all-window vector is still
  \[
    \operatorname{Ob}^{\infty}_{\mathrm{BM}}
    =
    (\operatorname{ob}_{\mathrm{mom}},
     \operatorname{ob}_{\mathrm{collar}},
     \operatorname{ob}_{3},
     \operatorname{ob}_{\mathrm{unif}}).
  \]
  It must be replaced by
  \[
    \operatorname{Ob}^{\Pi}_{\mathrm{BM}}
    =
    (\operatorname{ob}_{\oplus},
     \operatorname{ob}_{I_\Pi},
     \operatorname{ob}_{\mathfrak h,\Pi},
     \operatorname{ob}_{\mathrm{collar},\Pi},
     \operatorname{ob}_{3,\Pi},
     \operatorname{ob}_{\mathrm{unif},\Pi}).
  \]
- `open-obligations.tex` has no BMK all-window/pro-Matlis row.

## Failure Mode

The manuscript integrated the finite-current obstruction layer, then stopped
one layer early.  It treats pro-Matlis/all-window transfer as a future
construction target with a four-entry vector.  The construction push proves
more sharply that the one-pair analytic pro-Matlis retract is positive, while
the native strict all-window/product-current transfer is obstructed by six
entries.

Two missing entries are independent of the old uniformity/collar entries:

- \(\operatorname{ob}_{I_\Pi}\): a product sequence of derivative-delta
  coefficients has no compact-current section, since point-supported
  distributions have finite order.
- \(\operatorname{ob}_{\mathfrak h,\Pi}\): the full formal Hamiltonian
  action is not defined on \(\widehat{\mathcal P}_{\Pi}\); for
  \(f=\sum_{p\ge2}z_1^p\) and
  \(\lambda=\sum_{p\ge2}\rho_{p-1,0}\), the
  \(\rho_{0,1}\)-coefficient is \(-\sum_{p\ge2}p\).

## Exact Fixes

Use the detailed patch instructions in
`reconstitution/bmk-pro-matlis-native-obstruction-integration-audit-2026-04-30.md`.

Required TeX targets:

- `main.tex`: extend the BMK proposition with the positive pro-analytic
  one-pair retract and replace the four-entry all-window vector by
  \(\operatorname{Ob}^{\Pi}_{\mathrm{BM}}\).
- `appendix-factorization-current-conventions.tex`: make the appendix theorem
  carry the same pro-analytic positive statement and the six-entry native
  obstruction vector.
- `theorem-lanes.tex`: update the BMK lane status and obstruction summary.
- `claim-strength-ledger.tex`: update both BMK rows from four-entry
  \(\operatorname{Ob}^{\infty}_{\mathrm{BM}}\) to six-entry
  \(\operatorname{Ob}^{\Pi}_{\mathrm{BM}}\).
- `open-obligations.tex`: add the missing BMK all-window/pro-Matlis
  obstruction row.

## Files Changed

- `reconstitution/bmk-pro-matlis-native-obstruction-integration-audit-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-307-bmk-pro-matlis-native-obstruction-integration-audit.md`

## TeX Changed

None.

## Residual Obligation

An integration owner must make the TeX edits.  Until then, the manuscript
does not yet state the one-pair analytic pro-Matlis retract as positive or
the strict native all-window current \(E_2\) transfer as obstructed with all
listed entries.
