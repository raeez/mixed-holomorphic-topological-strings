# Control-Surface Post-BMK/theta3/LQT Audit - 2026-04-30

Agent: 319.
Scope: report-only audit of `open-obligations.tex`, `claim-strength-ledger.tex`,
`theorem-lanes.tex`, `main.tex`, and reports 306, 309, 315.  No manuscript TeX
was edited.

## Verdict

The post-integration control surfaces are mostly theorem-grade after the BMK
pro-Matlis, theta3 `Delta^1`, LQT averaged-beta, and Weiss Cech/Roos patches.
I found no stale demotion in the three main ledger surfaces: construction-target
language there names exact obstruction data rather than weakening a proved
claim.  Two semantic TeX patch targets remain, plus build-layout warnings.

## BMK pro-Matlis surface

Status: theorem-grade, with proof strength correctly bounded.

- The positive statement is the one-pair analytic pro-Matlis retract
  `P_{\Pi}^{\mathrm{an}}=\tau P_{\mathrm{an}}` with
  `\pi_NP_{\Pi}^{\mathrm{an}}=p_N`, visible in `open-obligations.tex:283-285`,
  `claim-strength-ledger.tex:330-331`, `theorem-lanes.tex:514-517`, and
  `main.tex:1455-1459`, `main.tex:1684-1685`.
- The strict native all-window current transfer is not overclaimed.  It is
  blocked by the six-entry vector `\operatorname{Ob}^{\Pi}_{\mathrm{BM}}` in
  `open-obligations.tex:291-309`, `claim-strength-ledger.tex:667-683`,
  `theorem-lanes.tex:520-526`, and `main.tex:1519-1546`.
- Agent 315's stale BMK defects are healed in the current checkout: the
  moment identity uses
  `z_1^{N+2}\cdot\rho_{N+1,0}=-(N+2)\rho_{0,1}` at
  `claim-strength-ledger.tex:326`, and the appendix notation now uses
  `\operatorname{ob}^{\chi}_{3,\Pi,N}` at
  `appendix-factorization-current-conventions.tex:806`.

No BMK patch target remains.

## LQT averaged-beta surface

Status: theorem-grade in `open-obligations.tex`, `claim-strength-ledger.tex`,
and `main.tex`; one semantic display defect remains in `theorem-lanes.tex`.

- The accepted surface is the stable single-cycle image of
  `\Theta_{N,K,L}`, with
  `\lambda_{\mathrm{LQT},K,L}=\Theta_{N,K,L}^{-1}P_{1\mathrm{cyc}}`.
  This is stated in `open-obligations.tex:152-160`,
  `claim-strength-ledger.tex:403-411`, and `main.tex:2008-2020`.
- The separated-block repair from report 306 is present: the same-rank
  deletion route is not used as theorem evidence, and the actual
  finite-rank bridge is the normalized signed average
  `\beta_{M,K,L}` and
  `P^{\mathrm{sep}}_{M,K,L}=\beta_{M,K,L}P_{1\mathrm{cyc}}\alpha_{M,K,L}`.

Patch target:

- `theorem-lanes.tex:2107-2111` has a malformed source display:
  `\operatorname{Prim}^{1\mathrm{cyc}}_{N,K,L}` is juxtaposed with
  `C_{*,\le L}^{\mathrm{CE}}(...)` without `:=`, `\subset`, or a domain
  separator.  The mathematical intent is clear from the other surfaces, but
  the display should be repaired before this lane is treated as clean.
  Suggested patch:
  define
  `\operatorname{Prim}^{1\mathrm{cyc}}_{N,K,L}:=\operatorname{im}\Theta_{N,K,L}
  \subset C_{*,\le L}^{\mathrm{CE}}(\mathfrak{gl}_N(A_{\psi,K}))^{GL_N}`
  immediately before the display, then type
  `\lambda_{\mathrm{LQT},K,L}\colon
  \operatorname{Prim}^{1\mathrm{cyc}}_{N,K,L}\to
  CC_{\mathrm{red},\le L}(A_{\psi,K})[1]`.

## theta3 `Delta^1` surface

Status: theorem-grade.  Agent 309's missing transport notation is now healed in
the current checkout.

- `open-obligations.tex:937-951`,
  `claim-strength-ledger.tex:972-983`,
  `theorem-lanes.tex:3557-3572`, and
  `main.tex:8952-8962` all name
  `\Delta^1_{M,N}:=-\pi_{M,N}\mathfrak b^M+\mathfrak b^N`.
- The required equation is no longer a slogan:
  `\Delta^1_{M,N}
  =d_{\mathrm{ns},N}(\pi_{M,N}B^M-B^N)`.
- The control surfaces also require both the `H^1` Bianchi transport class and
  the secondary `\varprojlim^1H^0` primitive-compatibility class to vanish.

No theta3 patch target remains.

## Weiss Cech/Roos surface

Status: theorem-grade in `open-obligations.tex`, `claim-strength-ledger.tex`,
and `theorem-lanes.tex`; `main.tex` still carries older Weiss/Ran wording.

- The internal stratified obstruction vector includes
  `\delta_{\mathrm{Weiss}}^{\check C/R}` at
  `open-obligations.tex:1204-1233`,
  `claim-strength-ledger.tex:850-886`, and
  `theorem-lanes.tex:3150-3196`.
- The component is not a homotopy-limit slogan.  It is
  `(\{H^\bullet(\Delta^{N,M}_{V,\mathcal U})\}_{V,\mathcal U,N,M},
  \mathfrak w^{\check C/R}_{V,\Omega,N,M})`, with the Cech cone
  `\Delta^{N,M}_{V,\mathcal U}` and a Roos compatibility class.
- The source-primary class
  `\operatorname{ob}^{\mathrm{src}}_{\mathrm{CFG}}` is correctly marked
  external to the internal vector, not as theorem evidence.

Patch target:

- `main.tex:4639-4655` still states that the obstruction lives in a
  "Weiss/Ran total complex" and refers to the matched-conventions datum, but it
  does not name
  `\delta_{\mathrm{Weiss}}^{\check C/R}`,
  `\Delta^{N,M}_{V,\mathcal U}`, or
  `\mathfrak w^{\check C/R}_{V,\Omega,N,M}`.  Replace this remark with the
  current Cech/Roos obstruction vector, or explicitly point the remark to
  `open-obligations.tex:1204-1233` and `theorem-lanes.tex:3150-3196`.

## Stale-demotion check

I searched the four control files for stale demotion language including
`conditional`, `expected`, `external input`, `not theorem-grade`, `stale`,
`demot`, `partial integration`, `currently proved is only`,
`construction target`, and `no such`.

Legitimate hits remain:

- BMK "currently proved is only" in `theorem-lanes.tex:514-517` is the correct
  one-pair analytic pro-Matlis bound.
- theta3 "no such `B^2_{02,20}`" in `open-obligations.tex:929-936`,
  `theorem-lanes.tex:3547-3556`, and `main.tex:8932-8946` is the exact finite-row
  obstruction.
- Weiss "must still be supplied" in `theorem-lanes.tex:3147-3150` is tied to
  the named internal vector.
- Construction-target rows in `claim-strength-ledger.tex` name exact missing
  objects or obstruction vectors; I did not find a stale demotion among the
  four requested lanes.

## Build and TeX defects

`make pdf` completed and wrote `out/main.pdf` with 435 pages.  A final log scan
found no undefined-reference warnings and no fatal TeX error.

Remaining semantic TeX patch targets:

1. `theorem-lanes.tex:2107-2111` - malformed LQT source display for
   `\lambda_{\mathrm{LQT},K,L}`.
2. `main.tex:4639-4655` - stale Weiss/Ran total-complex remark; replace by the
   Cech/Roos obstruction vector or cross-reference the exact internal vector.

Remaining layout warnings from `out/main.log`:

1. `claim-strength-ledger.tex:241-247` - overfull vbox on the compact-CY/CoHA
   table page, reported at `out/main.log:2527`.
2. `local-dictionary.tex:707` - overfull hbox, 36.48196pt too wide.
3. `tate-T1-weighted-completion.tex:1772` - overfull hbox, 1.29213pt too wide.
4. `tate-T1-weighted-completion.tex:2080` - overfull hbox, 15.05399pt too wide.
5. `open-obligations.tex:1226-1234` - overfull hbox, 1.62016pt too wide.
6. `appendix-radial-parts-moyal.tex:638` - overfull hbox, 9.61589pt too wide.

I did not classify the many underfull hbox warnings as control-surface defects.
