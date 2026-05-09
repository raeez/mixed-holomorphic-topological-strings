# Swarm 2026-04-30 Agent 316: Theorem-Surface Consistency Audit

Report-only audit.  No TeX edited.  No build run.

## Claim Attacked

Final theorem-surface consistency after main-thread patches for:

- BMK `Ob^{\Pi}_{BM}` versus stale `Ob^{\infty}_{BM}`;
- theta3 `\Delta^1` transport;
- LQT averaged-beta separated-block bridge;
- Weiss `\delta_{\mathrm{Weiss}}^{\check C/R}`;
- compact-CY and curve-VOA false transfers.

## Verdict

No live mathematical contradiction found.

One notation propagation patch remains: `main.tex:8918-8927` states the
correct theta3 transport equation and the \(H^1/\varprojlim^1H^0\) gates, but
does not name the cocycle `\Delta^1_{M,N}`.  The same cocycle is named in
`theorem-lanes.tex`, `open-obligations.tex`, and `claim-strength-ledger.tex`.

The current launch log has no Agent 316 entry; this is an operational stale
log, not a theorem-surface issue.

## Exact rg Findings

### BMK labels

```sh
rg -n -F '\operatorname{Ob}^{\Pi}_{\mathrm{BM}}' main.tex appendix-factorization-current-conventions.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex
```

```text
claim-strength-ledger.tex:336:  \(\operatorname{Ob}^{\Pi}_{\mathrm{BM}}\).
claim-strength-ledger.tex:667:    \operatorname{Ob}^{\Pi}_{\mathrm{BM}}
appendix-factorization-current-conventions.tex:696:    \operatorname{Ob}^{\Pi}_{\mathrm{BM}}
appendix-factorization-current-conventions.tex:816:  precisely the six entries of \(\operatorname{Ob}^{\Pi}_{\mathrm{BM}}\).
theorem-lanes.tex:520:    \operatorname{Ob}^{\Pi}_{\mathrm{BM}}
main.tex:1513:    \operatorname{Ob}^{\Pi}_{\mathrm{BM}}
main.tex:2493:\(\operatorname{Ob}^{\Pi}_{\mathrm{BM}}\).
main.tex:2530:  \(\operatorname{Ob}^{\Pi}_{\mathrm{BM}}\).
```

```sh
rg -n -F '\operatorname{Ob}^{\infty}_{\mathrm{BM}}' main.tex appendix-factorization-current-conventions.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex; printf 'exit=%s\n' $?
```

```text
exit=1
```

### Theta3 transport

```sh
rg -n -F '\Delta^1_{M,N}' main.tex appendix-factorization-current-conventions.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex
```

```text
claim-strength-ledger.tex:969:    \Delta^1_{M,N}
claim-strength-ledger.tex:975:    \Delta^1_{M,N}
claim-strength-ledger.tex:980:  \(\Delta^1_{M,N}\) and the secondary \(\varprojlim^1H^0\)
theorem-lanes.tex:3559:      \Delta^1_{M,N}
theorem-lanes.tex:3565:      \Delta^1_{M,N}
theorem-lanes.tex:3570:    \(\Delta^1_{M,N}\) and the secondary
open-obligations.tex:902:    \Delta^1_{M,N}
open-obligations.tex:908:    \Delta^1_{M,N}
open-obligations.tex:913:  \(\Delta^1_{M,N}\); after a choice of primitive, it must also kill the
```

Patch target: `main.tex:8918-8927` should name
`\Delta^1_{M,N}:=-\pi_{M,N}\mathfrak b^M+\mathfrak b^N` before the displayed
compatibility equation.

### LQT separated-block bridge

```sh
rg -n -F '\beta_{M,K,L}' main.tex appendix-factorization-current-conventions.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex
```

```text
theorem-lanes.tex:2138:      \(\beta_{M,K,L}\) be the normalized signed average over injections
theorem-lanes.tex:2142:      \(\alpha_{M,K,L}\beta_{M,K,L}=\operatorname{id}\), and use
theorem-lanes.tex:2146:        \beta_{M,K,L}P_{1\mathrm{cyc}}\alpha_{M,K,L}.
main.tex:2066:    \beta_{M,K,L}\colon
main.tex:2080:  Thus \(\alpha_{M,K,L}\beta_{M,K,L}=\operatorname{id}\).
main.tex:2085:    \beta_{M,K,L}P_{1\mathrm{cyc}}\alpha_{M,K,L}
claim-strength-ledger.tex:430:  \(\beta_{M,K,L}\) over injections into the \(L\) labeled diagonal
claim-strength-ledger.tex:432:  \(\alpha_{M,K,L}\beta_{M,K,L}=\operatorname{id}\); its idempotent is
claim-strength-ledger.tex:436:    \beta_{M,K,L}P_{1\mathrm{cyc}}\alpha_{M,K,L},
open-obligations.tex:195:  \(\beta_{M,K,L}\) is the normalized signed average over injections into
open-obligations.tex:197:  labels, \(\alpha_{M,K,L}\beta_{M,K,L}=\operatorname{id}\), and the
open-obligations.tex:202:    \beta_{M,K,L}P_{1\mathrm{cyc}}\alpha_{M,K,L}.
```

```sh
rg -n -F 'P^{\mathrm{sep}}_{M,K,L}' main.tex appendix-factorization-current-conventions.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex
```

```text
open-obligations.tex:200:    P^{\mathrm{sep}}_{M,K,L}
claim-strength-ledger.tex:434:    P^{\mathrm{sep}}_{M,K,L}
theorem-lanes.tex:2144:        P^{\mathrm{sep}}_{M,K,L}
main.tex:2083:    P^{\mathrm{sep}}_{M,K,L}
```

No LQT patch target.

### Weiss Cech/Roos notation

```sh
rg -n -F '\delta_{\mathrm{Weiss}}' main.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex appendix-factorization-current-conventions.tex
```

```text
claim-strength-ledger.tex:190:\delta_{\mathrm{Weiss}}^{\check C/R})\)\\
claim-strength-ledger.tex:469:  \delta_{\mathrm{Weiss}}^{\check C/R})\), with the last entry the
claim-strength-ledger.tex:853:     \delta_{\mathrm{Weiss}}^{\check C/R},
claim-strength-ledger.tex:863:    \delta_{\mathrm{Weiss}}^{\check C/R}
open-obligations.tex:1067:    \delta_{\mathrm{Weiss}}(V,\mathcal U)
open-obligations.tex:1173:     \delta_{\mathrm{Weiss}}^{\check C/R},
open-obligations.tex:1183:    \delta_{\mathrm{Weiss}}^{\check C/R}
theorem-lanes.tex:3156:     \delta_{\mathrm{Weiss}}^{\check C/R},
theorem-lanes.tex:3173:    \delta_{\mathrm{Weiss}}^{\check C/R}
```

The bare `\delta_{\mathrm{Weiss}}(V,\mathcal U)` is the local cover cone;
the obstruction vector uses `^{\check C/R}`.  No Weiss patch target.

### False-transfer firewall

```sh
rg -n "not a core local obligation|cannot support|neither.*curve|curve VOA|one-dimensional VOA|No compact|false transfer|not theorem support|can enter only|does not construct a one-dimensional|does not prove a curve|does not yet assert the stronger one-dimensional" main.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex appendix-factorization-current-conventions.tex
```

```text
claim-strength-ledger.tex:351:  that construction, any curve VOA or Zhu assertion is false transfer.
claim-strength-ledger.tex:637:\emph{exact obstruction}, \emph{false transfer}, and
claim-strength-ledger.tex:681:  It is not a curve VOA theorem and not a Costello QME theorem.
claim-strength-ledger.tex:702:  \emph{false transfer}.
claim-strength-ledger.tex:706:  the controlled reduction, and \emph{false transfer} before it.  The
claim-strength-ledger.tex:740:  target.  Before that reduction datum it is \emph{false transfer}, not
claim-strength-ledger.tex:1427:  arithmetic fixtures.  It is not theorem support for a compact-CY
open-obligations.tex:10:Igusa, BKM, and global BCOV material is not a core local obligation.  It
open-obligations.tex:11:is a comparison surface only, and it cannot support the local QME, Ext,
open-obligations.tex:1196:  analogy is motivation, not theorem support.
appendix-factorization-current-conventions.tex:33:No compact Calabi--Yau target, global BCOV moduli space, CoHA, quintic,
appendix-factorization-current-conventions.tex:725:  \(z_1\cdot\rho_{a,0}=-\rho_{a,1}\).  No curve VOA, Zhu algebra, or
appendix-factorization-current-conventions.tex:1266:  or else remains an obstruction problem.  No compact target or global
theorem-lanes.tex:350:  algebra can enter only after an additional theorem chooses a complex
theorem-lanes.tex:576:  on principal parts.  No compact Calabi--Yau, CoHA, quintic, OSV/GV,
theorem-lanes.tex:696:  manuscript does not yet assert the stronger one-dimensional VOA/OPE
theorem-lanes.tex:905:  Statement~\ref{thm:lane-controlled-cxr-reduction}, with false transfer
theorem-lanes.tex:1046:  controlled reduction; false transfer before it}.  A constructed curve
main.tex:1169:  or BKM data.  A one-dimensional VOA/OPE statement requires an
main.tex:1555:  curve VOA, a Zhu algebra, a strict support-local finite-window quotient,
main.tex:1688:  Calabi--Yau theory, a curve VOA, CoHA, or BKM data can enter only
main.tex:2487:does not construct a one-dimensional VOA or OPE algebra, nor a strict
main.tex:9485:They can enter only through a supplied matched-conventions datum and the
```

No false-transfer patch target.

### Launch log

```sh
rg -n "Agent 316|agent-316|316" reconstitution/swarm-live-launch-log-2026-04-30.md; printf 'exit=%s\n' $?
```

```text
exit=1
```

Optional non-theorem hygiene target: append Agent 316 to
`reconstitution/swarm-live-launch-log-2026-04-30.md` if that log is intended
to track this late assignment.

## Files Changed

- `reconstitution/theorem-surface-consistency-audit-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-316-theorem-surface-consistency-audit.md`

