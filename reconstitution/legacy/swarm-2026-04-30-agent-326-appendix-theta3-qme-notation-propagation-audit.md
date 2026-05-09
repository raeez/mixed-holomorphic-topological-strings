# Swarm 2026-04-30 Agent 326: Appendix theta3/QME notation propagation audit

Report-only audit. No manuscript TeX edited. No build run.

## Claim attacked

The appendices might now lag the main `theta_3` QME surface after Agent 322:
the main text uses `\mathcal Q`, `A_D^2`, `r_2`, `A_B^2`, and
`\Delta^1_{M,N}`, while `appendix-unreduced-bv-qme.tex` still uses
`\mathcal K` and only the generic finite-row criterion.

## Verdict

No contradiction. The main theorem surface is enough for correctness. The
appendix should still be patched when TeX edits are authorized, because it is
the natural QME notation source and currently omits the lower Bianchi-exposed
matrix notation.

Claim status recommendation:

- `main.tex`: keep as current theorem surface.
- `theorem-lanes.tex`, `open-obligations.tex`, `claim-strength-ledger.tex`:
  no theta3 notation patch required for correctness.
- `appendix-unreduced-bv-qme.tex`: patch recommended for propagation.
- `appendix-factorization-current-conventions.tex`: optional pointer only.

## Local anchors

- Generic non-scalar tower in main:
  `main.tex:8651-8676`, especially
  `\mathcal Q^\bullet_{w,M}(I)=\ker\widehat\sigma_{\mathrm{sc},M}` at
  `main.tex:8671`.
- Main theta3 acceptance gate:
  `main.tex:8810-9016`.
- Lower Bianchi matrix in main:
  `main.tex:8964-9015`.
- Theorem lane repetition:
  `theorem-lanes.tex:3463-3591`.
- Open-obligations repetition:
  `open-obligations.tex:793-955`.
- Claim-ledger repetition:
  `claim-strength-ledger.tex:921-991`.
- Appendix generic finite-row criterion:
  `appendix-unreduced-bv-qme.tex:2224-2333`.
- Appendix one-row theta3 obstruction:
  `appendix-unreduced-bv-qme.tex:2416-2455`.
- Factorization-current non-scalar habitat:
  `appendix-factorization-current-conventions.tex:1030-1118` and
  `appendix-factorization-current-conventions.tex:1954-2033`.

## Exact formulas

The live lower basis is

```tex
(E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20}).
```

The source-coordinate column and lower residual are

```tex
A_D^2=(-2,2,1)^T,\qquad r_2=(2,-2,0)^T.
```

The current habitat has no `B^2_{02,20}` column. The missing column is

```tex
A_B^2=(0,0,-1)^T,\qquad
d_{\mathrm{ns},2}B^2_{02,20}=-\mathfrak b^2_{02,20}.
```

The tower obstruction is

```tex
\Delta^1_{M,N}:=-\pi_{M,N}\mathfrak b^M+\mathfrak b^N
=d_{\mathrm{ns},N}(\pi_{M,N}B^M-B^N).
```

This must kill the `H^1` Bianchi transport class and then the secondary
`\varprojlim^1H^0` primitive-compatibility class.

## Patch targets

1. `appendix-unreduced-bv-qme.tex`, after
   `def:app-native-finite-window-realization-habitat`:
   add a convention identifying
   `\mathcal Q^\bullet_{w,M}(I)=\mathcal K^\bullet_{\mathrm{ns},M}(I)`.

2. `appendix-unreduced-bv-qme.tex`, after
   `prop:app-closed-rows-and-theta-three-source-face`:
   add a short corollary or remark carrying `D^2_{02,20}`,
   `\mathfrak b^2_{02,20}`, `A_D^2`, `r_2`, `A_B^2`, and
   `\Delta^1_{M,N}`, with an explicit sentence that this is not a solved
   Costello graph/QME.

3. Optional: `appendix-factorization-current-conventions.tex`, after item (4)
   of `prop:app-nonscalar-current-lift-obstructions`:
   cross-reference `prop:theta-three-finite-window-acceptance-gate` and say
   the coefficient-current kernel does not supply `A_B^2` or the
   `\Delta^1_{M,N}` primitive.

4. Optional machine target: `scripts/finite_window_graph_array.py`, near the
   `theta3_eight_face_candidate_obstruction_check` records:
   add a Bianchi-exposed matrix record if this notation becomes machine-gated.

## Checks run

```sh
rg -n "theta3|\\theta_3|Theta_3|Theta3|QME|non-scalar|scalar-contact|Delta\\^1|\\Delta\\^1|A_D|A_B|K\\^|Q/K|habitat|Costello|matrix|Bianchi|Roos|transport" appendix-unreduced-bv-qme.tex appendix-factorization-current-conventions.tex main.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex
nl -ba appendix-unreduced-bv-qme.tex | sed -n '2217,2485p'
nl -ba appendix-factorization-current-conventions.tex | sed -n '1030,1120p'
nl -ba appendix-factorization-current-conventions.tex | sed -n '1950,2035p'
nl -ba main.tex | sed -n '8788,9085p'
nl -ba theorem-lanes.tex | sed -n '3448,3595p'
nl -ba open-obligations.tex | sed -n '760,965p'
nl -ba claim-strength-ledger.tex | sed -n '488,548p'
nl -ba claim-strength-ledger.tex | sed -n '920,992p'
python3 scripts/finite_window_graph_array.py
```

## Files changed

- `reconstitution/appendix-theta3-qme-notation-propagation-audit-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-326-appendix-theta3-qme-notation-propagation-audit.md`

