# Theorem-Surface Consistency Audit

Date: 2026-04-30.
Agent: 316.
Scope: report-only final consistency audit after the BMK/LQT/theta3/Weiss patches.
No manuscript TeX was edited.

## Verdict

The live theorem surface is mostly consistent.

Clean:

- BMK now uses `\operatorname{Ob}^{\Pi}_{\mathrm{BM}}`; no live
  `\operatorname{Ob}^{\infty}_{\mathrm{BM}}` hit remains in the audited
  manuscript/control files.
- LQT now separates the stable Hopf Eulerian projection from the finite-rank
  separated-block bridge.  The bridge uses the normalized signed average
  `\beta_{M,K,L}`, the read-back map `\alpha_{M,K,L}`, and
  `P^{\mathrm{sep}}_{M,K,L}`.
- Weiss descent now uses
  `\delta_{\mathrm{Weiss}}^{\check C/R}` for the internal stratified vector,
  with the coverwise Cech cone plus Roos compatibility class.
- Compact-CY, curve-VOA, Zhu, CoHA, Igusa, and BKM transfers remain fenced as
  external comparison or controlled-reduction targets.

One live stale-label target:

- `main.tex:8918-8927` has the correct theta3 Bianchi transport equation
  but does not name the class `\Delta^1_{M,N}`.  The theorem lanes, open
  obligations, and claim ledger do name it.  This is a notation propagation
  gap, not a mathematical contradiction.

Operational note:

- `reconstitution/swarm-live-launch-log-2026-04-30.md` has no `Agent 316`
  entry.  The live assignment came from the principal prompt, not the launch
  log.  This is not a theorem-surface defect.

## Patch Targets

1. `main.tex:8918-8927`: name the displayed theta3 Bianchi transport cocycle.
   Suggested future TeX target:

   ```tex
   In a tower this requires
   \[
     \Delta^1_{M,N}:=-\pi_{M,N}\mathfrak b^M+\mathfrak b^N,
     \qquad
     d_{\mathrm{ns},N}(\pi_{M,N}B^M-B^N)=\Delta^1_{M,N},
   \]
   together with vanishing of the \(H^1\) Bianchi transport class ...
   ```

2. Optional non-theorem launch-log hygiene:
   `reconstitution/swarm-live-launch-log-2026-04-30.md`: add Agent 316 if
   the launch log is intended to be complete beyond Agent 303.

No other TeX patch target is indicated by this audit.

## Exact rg Findings

### BMK: `Ob^{\Pi}_{BM}` present, `Ob^{\infty}_{BM}` absent

Command:

```sh
rg -n -F '\operatorname{Ob}^{\Pi}_{\mathrm{BM}}' main.tex appendix-factorization-current-conventions.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex
```

Output:

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

Command:

```sh
rg -n -F '\operatorname{Ob}^{\infty}_{\mathrm{BM}}' main.tex appendix-factorization-current-conventions.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex; printf 'exit=%s\n' $?
```

Output:

```text
exit=1
```

### Theta3: `\Delta^1_{M,N}` propagated except root `main.tex`

Command:

```sh
rg -n -F '\Delta^1_{M,N}' main.tex appendix-factorization-current-conventions.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex
```

Output:

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

Relevant root anchor:

```text
main.tex:8918-8927: displays d_{\mathrm{ns},N}(\pi_{M,N}B^M-B^N)
=-\pi_{M,N}\mathfrak b^M+\mathfrak b^N and the H^1/secondary
\varprojlim^1H^0 gates, but does not name \Delta^1_{M,N}.
```

### LQT: averaged beta separated-block bridge present

Command:

```sh
rg -n -F '\beta_{M,K,L}' main.tex appendix-factorization-current-conventions.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex
```

Output:

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

Command:

```sh
rg -n -F 'P^{\mathrm{sep}}_{M,K,L}' main.tex appendix-factorization-current-conventions.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex
```

Output:

```text
open-obligations.tex:200:    P^{\mathrm{sep}}_{M,K,L}
claim-strength-ledger.tex:434:    P^{\mathrm{sep}}_{M,K,L}
theorem-lanes.tex:2144:        P^{\mathrm{sep}}_{M,K,L}
main.tex:2083:    P^{\mathrm{sep}}_{M,K,L}
```

Command:

```sh
rg -n -F 'separated-block' main.tex appendix-factorization-current-conventions.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex
```

Output:

```text
theorem-lanes.tex:2136:      separated-block stabilization zigzag: with
open-obligations.tex:193:  zero.  The finite-rank bridge must use separated-block stabilization:
open-obligations.tex:198:  strict separated-block idempotent is
main.tex:2087:  is the strict finite-rank chain idempotent on the separated-block
```

### Weiss: `\delta_{\mathrm{Weiss}}^{\check C/R}` present

Command:

```sh
rg -n -F '\delta_{\mathrm{Weiss}}' main.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex appendix-factorization-current-conventions.tex
```

Output:

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

Interpretation: the bare `\delta_{\mathrm{Weiss}}(V,\mathcal U)` at
`open-obligations.tex:1067` is the local cover cone.  The internal obstruction
vector uses the corrected `^{\check C/R}` package.

### False-transfer firewalls

Command:

```sh
rg -n "not a core local obligation|cannot support|neither.*curve|curve VOA|one-dimensional VOA|No compact|false transfer|not theorem support|can enter only|does not construct a one-dimensional|does not prove a curve|does not yet assert the stronger one-dimensional" main.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex appendix-factorization-current-conventions.tex
```

Output:

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

### Launch log

Command:

```sh
rg -n "Agent 316|agent-316|316" reconstitution/swarm-live-launch-log-2026-04-30.md; printf 'exit=%s\n' $?
```

Observed output:

```text
exit=1
```

The tail of the launch log ends at Agent 303, so this is launch-log hygiene
rather than a manuscript theorem-surface contradiction.

## Claim Status Recommendations

- BMK: proved finite current data plus exact finite-current and all-window
  obstruction vectors.  No stale `Ob^\infty` label remains.
- Theta3: fixed-window obstruction and Bianchi transport theorem surface are
  consistent; add the `\Delta^1_{M,N}` name in root `main.tex` for label
  synchronization.
- LQT: theorem-grade separated-block bridge is clean; same-rank deletion is
  consistently obstructed.
- Weiss: clean after the `\check C/R` patch; the coverwise bare cone is only
  a component definition.
- Compact-CY/curve-VOA: clean firewall; no false transfer found.

## Files Changed

- `reconstitution/theorem-surface-consistency-audit-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-316-theorem-surface-consistency-audit.md`

