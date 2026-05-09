# Theta3 Matrix Notation Consistency Audit, 2026-04-30

Report-only audit. No manuscript TeX edited. No build run.

## Claim Attacked

The theta3 finite-window obstruction notation might have drifted after the
`\Delta^1_{M,N}` naming and BMK pro-Matlis patches. The attacked risk is a
false identification among:

- the fixed lower Bianchi matrix column `A_D^2`;
- the transported lower residual `r_2`;
- the missing local-functional Bianchi-killing column `A_B^2`;
- the tower cocycle `\Delta^1_{M,N}`;
- the generic finite-window non-scalar obstruction pair
  `\mathfrak O_n^{\mathrm{ns}}`.

## Verdict

CONVERGED for notation consistency in the live manuscript surface.

There is no fatal mismatch in `main.tex`, `theorem-lanes.tex`,
`open-obligations.tex`, or `claim-strength-ledger.tex`. The symbols live at
different levels:

| Symbol | Level | Current meaning |
|---|---|---|
| `\mathfrak O_n^{\mathrm{ns}}` | generic order-`n` tower | `(([\mathfrak o^{\mathrm{ns}}_{n,M}])_M,\lambda_n)`: fixed-window `H^1` classes plus the Roos `\varprojlim^1 H^0` primitive-compatibility class. |
| `A_D^2` | fixed `N=2` lower Bianchi row | the column of the source-coordinate primitive `D^2_{02,20}` in the exposed basis `(E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20})`. |
| `r_2` | fixed `N=2` lower residual | the transported residual `(2,-2,0)^T` in the same exposed basis. |
| `A_B^2` | missing fixed-window local-functional column | the required column `(0,0,-1)^T`, equivalent to `d_{\mathrm{ns},2}B^2_{02,20}=-\mathfrak b^2_{02,20}`. |
| `\Delta^1_{M,N}` | tower Bianchi transport | `-\pi_{M,N}\mathfrak b^M+\mathfrak b^N`, exact only if a compatible family `B^M` gives `d_{\mathrm{ns},N}(\pi_{M,N}B^M-B^N)`. |

Thus the theta3 lower matrix is a fixed-window certificate inside the generic
pair. It is not a renaming of the generic pair. `\Delta^1_{M,N}` is the tower
compatibility obstruction for the missing `B` column, not a second residual
vector.

## Matrix Check

Current TeX uses the Bianchi-exposed basis
`(E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20})`.

The source-coordinate candidate gives

```tex
A_D^2=(-2,2,1)^T, \qquad r_2=(2,-2,0)^T.
```

The equation `A_D^2 c=-r_2` is inconsistent: the first two coordinates force
`c=1`, while the Bianchi coordinate forces `c=0`. The cokernel

```tex
\widetilde\lambda_{02,\mathfrak b}
  =\frac12(E^2_{\nu_{02}})^*+(\mathfrak b^2_{02,20})^*
```

kills `A_D^2` and evaluates to `1` on `r_2`. This appears in
`main.tex:8905-8924`, `theorem-lanes.tex:3529-3542`,
`open-obligations.tex:910-923`, and `claim-strength-ledger.tex:960-963`.

The missing counterterm target is

```tex
-\mathfrak b^2_{02,20}=(0,0,-1)^T.
```

It is outside the current image of `A_D^2`, because the same cokernel evaluates
to `-1` on it. The controlled enlargement must add

```tex
A_B^2=(0,0,-1)^T.
```

If constructed, `A_D^2+A_B^2=(-2,2,0)^T=-r_2`, so the fixed lower equation
closes. This is only a formal matrix closure until the local functional,
scalar-zero value, locality or wavefront habitat, and transport data are built.
Anchors: `main.tex:8932-8951`, `theorem-lanes.tex:3544-3557`,
`open-obligations.tex:925-937`, `claim-strength-ledger.tex:964-970`.

The tower condition is named consistently:

```tex
\Delta^1_{M,N}:=-\pi_{M,N}\mathfrak b^M+\mathfrak b^N
  =d_{\mathrm{ns},N}(\pi_{M,N}B^M-B^N).
```

It also requires the vanishing of the corresponding `H^1` transport class and
then the secondary `\varprojlim^1H^0` primitive-compatibility class. Anchors:
`main.tex:8952-8962`, `theorem-lanes.tex:3557-3571`,
`open-obligations.tex:939-950`, `claim-strength-ledger.tex:970-984`.

## Generic Pair Compatibility

The generic non-scalar finite-window pair is still the two-stage obstruction:

```tex
\mathfrak O^{\mathrm{ns}}_n
  =
  (([\mathfrak o^{\mathrm{ns}}_{n,M}])_M,\lambda_n).
```

This is explicit in `open-obligations.tex:690-700` and compatible with
`main.tex:8617-8622`, where the text states the inverse-limit `H^1` class and
the `\varprojlim^1H^0` primitive class. The lower theta3 Bianchi data are a
specific fixed-window obstruction feeding this pattern; `\Delta^1_{M,N}` is
the tower cocycle whose `H^1` and secondary `H^0` classes must vanish before
the corresponding theta3 entry of `\mathfrak O_n^{\mathrm{ns}}` is zero.

## BMK Separation

The BMK pro-Matlis patch is orthogonal to the theta3 non-scalar QME matrix.
The manuscript distinguishes:

- finite-current obstruction
  `\operatorname{Ob}^{\mathrm{BMK\mbox{-}curr}}_N`;
- strict native all-window current obstruction
  `\operatorname{Ob}^{\Pi}_{\mathrm{BM}}`;
- non-scalar QME obstruction pair `\mathfrak O_n^{\mathrm{ns}}`.

The BMK lane supplies current-limit data, finite Matlis moments, the arity-two
Hamiltonian/Matlis comparison, and a one-pair analytic pro-Matlis retract. It
does not assert a native finite-window current transfer and does not alter the
theta3 `A_D^2,r_2,A_B^2,\Delta^1` notation. Anchors:
`main.tex:1248-1462`, `theorem-lanes.tex:489-528`,
`open-obligations.tex:274-309`, `claim-strength-ledger.tex:319-336`.

## Remaining Defects And Patch Targets

1. Appendix propagation gap. `appendix-unreduced-bv-qme.tex:2298-2333` gives
   the generic finite-row matrix criterion `A^Mc=-r^M`, and
   `appendix-unreduced-bv-qme.tex:2416-2455` gives the theta3 one-row class.
   It does not yet record the Bianchi-exposed lower matrix
   `A_D^2,r_2,A_B^2,\Delta^1_{M,N}`. This is not a contradiction, but the
   appendix is no longer the complete notation source. Patch target: add a
   short corollary after
   `prop:app-closed-rows-and-theta-three-source-face`, or cross-reference
   `prop:theta-three-finite-window-acceptance-gate`.

2. `\mathcal Q` versus `\mathcal K` drift. `main.tex:8762-8764`,
   `open-obligations.tex:794-797`, and `claim-strength-ledger.tex:935-937`
   use `\mathcal Q_{\theta_3,M}` for the one-row complex; the appendix and
   theorem lane use `\mathcal K_{\theta_3,M}` as the non-scalar kernel
   complex. The meanings are compatible because
   `\mathcal Q^\bullet_{w,M}(I)=\ker\widehat\sigma_{\mathrm{sc},M}` and
   `\mathcal K^\bullet_{\mathrm{ns},M}(I)=\ker\widehat\sigma_{\mathrm{sc},M}`.
   Patch target: insert a convention sentence equating the two notations in
   this lane, or standardize the theta3 subcomplex notation.

3. Claim-ledger duplication. `claim-strength-ledger.tex:512-546` records
   `A_D^2` and `r_2` but only refers generically to Bianchi transport; the
   later ledger entry `claim-strength-ledger.tex:960-984` names
   `A_B^2` and `\Delta^1_{M,N}`. This is a partial duplicate, not a
   mathematical conflict. Patch target: add a one-line pointer in the earlier
   item to the later full Bianchi transport notation, or merge the duplicate
   theta3 paragraphs.

4. Stale internal reports. Older `reconstitution/` reports still contain the
   two-coordinate lower notation, for example
   `reconstitution/swarm-2026-04-30-agent-275-nonscalar-costello-binary-row-construction-push.md:163-208`
   and
   `reconstitution/theta3-nondiagonal-transport-counterterm-construction-push-2026-04-30.md:95-115`.
   They are internal historical evidence, not live manuscript TeX. Patch
   target: any future synthesis should mark those two-coordinate formulas as
   pre-Bianchi-exposure and use the three-coordinate basis above.

5. Machine-evidence gap. `scripts/finite_window_graph_array.py` verifies the
   theta3 one-row obstruction and rejects the tested companion payloads, but
   it does not emit the three-coordinate Bianchi matrix
   `A_D^2=(-2,2,1)^T`, `r_2=(2,-2,0)^T`, or `A_B^2=(0,0,-1)^T`.
   Patch target: add a script record for the lower Bianchi-exposed matrix if
   future acceptance gates require reproducible machine output for this
   notation.

## Checks Run

```sh
rg -n "theta_?3|theta3|Theta_?3|Delta\^\{?1\}?|A_D\^2|A_B\^2|r_2|finite-window|non-scalar|nonscalar|Matlis|BMK" main.tex appendix-unreduced-bv-qme.tex theorem-lanes.tex open-obligations.tex claim-strength-ledger.tex
nl -ba main.tex | sed -n '8738,8962p'
nl -ba appendix-unreduced-bv-qme.tex | sed -n '2298,2334p'
nl -ba appendix-unreduced-bv-qme.tex | sed -n '2416,2455p'
nl -ba theorem-lanes.tex | sed -n '3375,3585p'
nl -ba open-obligations.tex | sed -n '690,960p'
nl -ba claim-strength-ledger.tex | sed -n '500,548p'
nl -ba claim-strength-ledger.tex | sed -n '960,984p'
python3 scripts/finite_window_graph_array.py
```

No build was run because the task was report-only and no TeX was edited.
