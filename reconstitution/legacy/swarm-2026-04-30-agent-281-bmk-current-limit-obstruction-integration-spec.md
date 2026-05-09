# Agent 281 BMK Current-Limit Obstruction Integration Spec, 2026-04-30

Owned files:

- `reconstitution/swarm-2026-04-30-agent-281-bmk-current-limit-obstruction-integration-spec.md`
- `reconstitution/bmk-current-limit-obstruction-integration-spec-2026-04-30.md`

No TeX file was edited.  No build was run.

## Claim Integrated

Agent 276 attacks the BMK finite-window current identity in
`main.tex` and `appendix-factorization-current-conventions.tex`.  The
attack succeeds.  The finite-window differential identity currently
displayed in the manuscript is not justified on the undeclared
compact-support/current complex and is false on the full current complex.

This report turns that failure into manuscript integration instructions.
The exact instructions are in:

`reconstitution/bmk-current-limit-obstruction-integration-spec-2026-04-30.md`

## Current Verdict

Keep as partially constructed:

- the cutoff current limit \(H_\chi\) on fixed finite configuration
  strata;
- the finite moment map \(p_N\) on compactly supported top Dolbeault
  degree;
- the support-at-zero residue currents \(i_N(\rho_{a,b})=\Delta_{a,b}\),
  modulo the remaining analytic current-pairing scalar convention;
- the single-pair collar quotient killing terms supported on
  \(\operatorname{supp}d\chi\);
- the arity-two Hamiltonian/Matlis coefficient calculation.

Block as unproved:

- the identity
  \[
    \bar\partial H_{\chi,N}+H_{\chi,N}\bar\partial
    =
    \operatorname{id}-i_Np_N+E_{\chi,N};
  \]
- the relative identity
  \[
    \bar\partial H_{\mathrm{BM},N}
    +H_{\mathrm{BM},N}\bar\partial
    =
    \operatorname{id}-i_Np_N;
  \]
- any sentence saying the cutoff regularization "adds only" collar terms.

## Named Obstruction

Use the manuscript-ready name
\[
  \operatorname{Ob}^{\mathrm{BMK\mbox{-}curr}}_N
  =
  \left(
    \operatorname{ob}_{\mathrm{diag\mbox{-}sign}},
    \operatorname{ob}_{\mathrm{curr},N},
    \operatorname{ob}_{\mathrm{collar\mbox{-}fact}}
  \right).
\]

Here
\[
  \operatorname{ob}_{\mathrm{curr},N}
  =
  [\Delta_{0,0}]
  \oplus
  \bigoplus_{a+b>N}\C[\Delta_{a,b}]
\]
plus the missing descent of \(H_\chi\) through the quotient killing these
classes.

The finite-window current obstruction is prior to
\(\operatorname{Ob}^{\infty}_{\mathrm{BM}}\).  The all-window vector is
not the right first obstruction while the finite-window identity itself
has not been proved.

## Counterexample to Preserve

For \(T=\Delta_{N+1,0}\), one has \(p_N(T)=0\).  If the relative identity
held on the full current complex, then
\[
  T=\bar\partial H_{\mathrm{BM},N}T .
\]
Pairing with \(z_1^{N+1}\) gives
\[
  \langle T,z_1^{N+1}\rangle=1,\qquad
  \langle\bar\partial H_{\mathrm{BM},N}T,z_1^{N+1}\rangle=0,
\]
the second equality by Stokes and \(\bar\partial z_1^{N+1}=0\).  The
same obstruction appears at \(\Delta_{0,0}\) because the reduced Matlis
module excludes \(\rho_{0,0}\).

This counterexample is the guardrail against a false finite-window
differential identity.

## Manuscript Anchors

Line anchors are from the shared checkout read pass on 2026-04-30 and may
drift under concurrent edits.

- `main.tex:1242-1420`: proposition
  `prop:finite-window-bm-native-e2-transfer`.  Rename and reclassify as
  BMK current-limit data plus finite-window obstruction.  Replace
  `main.tex:1333-1348`.
- `main.tex:1422-1452`: proof.  Replace "adds only the displayed collar
  term" with the three-term cutoff derivative and isolate the annular
  diagonal term.
- `appendix-factorization-current-conventions.tex:399-628`: theorem
  `thm:app-finite-window-bmk-current-transfer`.  Apply the same
  reclassification.  Replace `482-498` and proof lines `630-640`.
- `main.tex:1494-1502`, `2142-2147`, `2174-2181`, `2321-2329`,
  `2394-2395`: replace "finite-window BMK arity-two transfer" language
  by "BMK current-limit data, finite-window Matlis moments, and arity-two
  Hamiltonian/Matlis comparison; finite-window differential identity
  obstructed by \(\operatorname{Ob}^{\mathrm{BMK\mbox{-}curr}}_N\)".
- `theorem-lanes.tex:381-533`: sharpen lane status and replace the
  \(d\bar z=0\) kernel by the full Koppelman form.
- `claim-strength-ledger.tex:319-325` and `585-615`: add the finite-window
  current obstruction gate before the all-window BM obstruction.

## Source Boundaries

Agent 268's BMK source fixture supports the external kernel and classical
Koppelman formula only.  It does not prove:

- cutoff current regularization;
- the finite-window projection \(i_Np_N\);
- the collar quotient;
- support-at-zero residue-current normalization;
- native \(E_2\) all-window transfer;
- Costello graph/QME, scalar-contact, or compact-Calabi-Yau consequences.

## Checks Run

Read and compared:

```bash
sed -n '1,240p' CLAUDE.md
sed -n '1,260p' /Users/raeez/topological-strings/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '1,260p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '1,220p' /Users/raeez/ecosystem/INVARIANTS.md
sed -n '143,170p' /Users/raeez/ecosystem/AGENTS-HARNESS.md
sed -n '1,360p' reconstitution/swarm-2026-04-30-agent-276-bmk-kernel-current-limit-construction-push.md
sed -n '1,260p' reconstitution/swarm-2026-04-30-agent-268-bmk-koppelman-source-fixture.md
sed -n '1,260p' references/primary-sources/bmk-koppelman-source-anchors-2026-04-30.md
nl -ba main.tex | sed -n '1240,1465p'
nl -ba appendix-factorization-current-conventions.tex | sed -n '395,705p'
nl -ba appendix-matlis-principal-parts.tex | sed -n '1,270p'
nl -ba theorem-lanes.tex | sed -n '381,535p'
nl -ba claim-strength-ledger.tex | sed -n '310,335p'
nl -ba claim-strength-ledger.tex | sed -n '580,620p'
```

Two exploratory `rg` regex searches failed due escape parsing.  They made
no file changes.
