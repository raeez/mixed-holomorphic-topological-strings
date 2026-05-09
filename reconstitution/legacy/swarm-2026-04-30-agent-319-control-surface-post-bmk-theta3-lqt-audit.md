# Swarm 2026-04-30 Agent 319 Report - Control-Surface Post-BMK/theta3/LQT Audit

## Assignment

Attack-heal the open-obligations and claim-ledger control surfaces after the
BMK pro-Matlis, theta3 `Delta^1`, LQT averaged-beta, and Weiss Cech/Roos
patches.  Read `open-obligations.tex`, `claim-strength-ledger.tex`,
`theorem-lanes.tex`, `main.tex`, and reports 306, 309, 315.  Do not edit
manuscript TeX.

Files changed by Agent 319: this report and
`reconstitution/control-surface-post-bmk-theta3-lqt-audit-2026-04-30.md`.
No manuscript TeX edited.

## Claim Attacked

The four control surfaces should now contain theorem-grade statements and no
stale demotions for:

1. BMK pro-Matlis after the one-pair analytic retract.
2. LQT after the separated-block averaged-beta repair.
3. theta3 after the named `\Delta^1_{M,N}` transport cocycle.
4. Weiss descent after the Cech/Roos internal obstruction vector.

## Result

The claim is almost correct.  The three ledger surfaces
`open-obligations.tex`, `claim-strength-ledger.tex`, and `theorem-lanes.tex`
are theorem-grade on BMK, theta3, and Weiss; LQT has one local display defect
inside `theorem-lanes.tex`.  `main.tex` has healed the theta3 `Delta^1` gap, but
still carries an older Weiss/Ran total-complex remark that should be replaced
by the Cech/Roos vector.

No stale demotion survives in the requested lanes.  The remaining defects are
patchable TeX/control-surface hygiene defects, not fatal mathematical
contradictions.

## Evidence

BMK:

- Positive theorem data are bounded to the one-pair analytic pro-Matlis retract
  `P_{\Pi}^{\mathrm{an}}=\tau P_{\mathrm{an}}`,
  `\pi_NP_{\Pi}^{\mathrm{an}}=p_N`.
- Anchors: `open-obligations.tex:283-285`,
  `claim-strength-ledger.tex:330-331`,
  `theorem-lanes.tex:514-517`, `main.tex:1455-1459`,
  `main.tex:1684-1685`.
- The strict native transfer is blocked by
  `\operatorname{Ob}^{\Pi}_{\mathrm{BM}}`, anchored at
  `open-obligations.tex:291-309`,
  `claim-strength-ledger.tex:667-683`,
  `theorem-lanes.tex:520-526`, and `main.tex:1519-1546`.
- Agent 315's stale BMK findings are healed: the dot/codimension formula is
  correct at `claim-strength-ledger.tex:326`, and the appendix uses
  `\operatorname{ob}^{\chi}_{3,\Pi,N}` at
  `appendix-factorization-current-conventions.tex:806`.

LQT:

- The accepted theorem-grade statement is windowed and stable:
  `\lambda_{\mathrm{LQT},K,L}=\Theta_{N,K,L}^{-1}P_{1\mathrm{cyc}}` on the
  stable single-cycle image.
- Anchors: `open-obligations.tex:152-160`,
  `claim-strength-ledger.tex:403-411`, `main.tex:2008-2020`.
- Report 306's separated-block repair is represented by the normalized signed
  average `\beta_{M,K,L}` and
  `P^{\mathrm{sep}}_{M,K,L}=\beta_{M,K,L}P_{1\mathrm{cyc}}\alpha_{M,K,L}`; the
  false same-rank deletion route is not treated as proof evidence.
- Defect: `theorem-lanes.tex:2107-2111` juxtaposes
  `\operatorname{Prim}^{1\mathrm{cyc}}_{N,K,L}` with the CE complex in the
  source of `\lambda_{\mathrm{LQT},K,L}`.  Add the missing definition/subset
  relation, then map from `\operatorname{Prim}^{1\mathrm{cyc}}_{N,K,L}` to
  `CC_{\mathrm{red},\le L}(A_{\psi,K})[1]`.

theta3:

- Agent 309's missing `Delta^1` transport package is now present across the
  control surfaces.
- Anchors: `open-obligations.tex:937-951`,
  `claim-strength-ledger.tex:972-983`,
  `theorem-lanes.tex:3557-3572`, `main.tex:8952-8962`.
- The statement requires
  `\Delta^1_{M,N}:=-\pi_{M,N}\mathfrak b^M+\mathfrak b^N` and
  `\Delta^1_{M,N}=d_{\mathrm{ns},N}(\pi_{M,N}B^M-B^N)`, plus vanishing of the
  `H^1` transport class and secondary `\varprojlim^1H^0` class.
- No theta3 patch target remains.

Weiss:

- The internal obstruction vector is theorem-grade in the three ledger
  surfaces:
  `\delta_{\mathrm{Weiss}}^{\check C/R}
  =(\{H^\bullet(\Delta^{N,M}_{V,\mathcal U})\}_{V,\mathcal U,N,M},
  \mathfrak w^{\check C/R}_{V,\Omega,N,M})`.
- Anchors: `open-obligations.tex:1204-1233`,
  `claim-strength-ledger.tex:850-886`, `theorem-lanes.tex:3150-3196`.
- The source-primary class
  `\operatorname{ob}^{\mathrm{src}}_{\mathrm{CFG}}` is correctly external.
- Defect: `main.tex:4639-4655` still uses the older "Weiss/Ran total complex"
  wording and does not name the Cech cone/Roos class.  Replace this remark with
  the current Cech/Roos vector or make it an explicit cross-reference to the
  exact internal vector in the control surfaces.

## Remaining Patch Targets

1. `theorem-lanes.tex:2107-2111`
   - Problem: malformed LQT source display.
   - Patch: define
     `\operatorname{Prim}^{1\mathrm{cyc}}_{N,K,L}
     :=\operatorname{im}\Theta_{N,K,L}
     \subset C_{*,\le L}^{\mathrm{CE}}(\mathfrak{gl}_N(A_{\psi,K}))^{GL_N}`
     and type
     `\lambda_{\mathrm{LQT},K,L}\colon
     \operatorname{Prim}^{1\mathrm{cyc}}_{N,K,L}\to
     CC_{\mathrm{red},\le L}(A_{\psi,K})[1]`.

2. `main.tex:4639-4655`
   - Problem: stale Weiss/Ran total-complex control wording.
   - Patch: replace by
     `\delta_{\mathrm{Weiss}}^{\check C/R}
     =(\{H^\bullet(\Delta^{N,M}_{V,\mathcal U})\}_{V,\mathcal U,N,M},
     \mathfrak w^{\check C/R}_{V,\Omega,N,M})`
     and state that full descent requires vanishing of the Cech-cone
     cohomology and the Roos refinement/window/transport compatibility class.

3. Layout-only warnings from `make pdf`
   - `claim-strength-ledger.tex:241-247`: overfull vbox at `out/main.log:2527`.
   - `local-dictionary.tex:707`: overfull hbox, 36.48196pt.
   - `tate-T1-weighted-completion.tex:1772`: overfull hbox, 1.29213pt.
   - `tate-T1-weighted-completion.tex:2080`: overfull hbox, 15.05399pt.
   - `open-obligations.tex:1226-1234`: overfull hbox, 1.62016pt.
   - `appendix-radial-parts-moyal.tex:638`: overfull hbox, 9.61589pt.

## Checks Run

- Loaded repo instructions and Vol II rectification standard.
- Read the four requested TeX control surfaces and reports 306, 309, 315.
- Searched for stale demotion markers and checked each hit against the named
  obstruction data.
- Ran `make pdf`; it completed and wrote `out/main.pdf` with 435 pages.
- Searched `out/main.log` for undefined-reference and fatal TeX errors; none
  were found.
