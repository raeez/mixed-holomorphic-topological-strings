# Agent 222 Report: BM All-Window Transfer Supremum Rework

Date: 2026-04-30.

Owned files:

- `appendix-factorization-current-conventions.tex`
- `reconstitution/swarm-2026-04-30-agent-222-bm-all-window-transfer-supremum-rework.md`

## Claim Attacked

The native Bochner--Martinelli--Koppelman transfer was theorem-grade in
`main.tex` but not yet carried by the local factorization-current
appendix.  The vulnerable point was the passage from finite
principal-part windows and arity two to an all-window native \(E_2\)
transfer.

## Repairs Made

Inserted
`appendix-factorization-current-conventions.tex:399`,
`thm:app-finite-window-bmk-current-transfer`.

The theorem proves the finite-window local transfer component:

\[
  \bar\partial H_{\mathrm{BM},N}
  +H_{\mathrm{BM},N}\bar\partial
  =
  \operatorname{id}-i_Np_N
\]

after the explicit cutoff-collar quotient, with

\[
  K_{\mathrm{BM}}(\zeta,z)
  =
  \frac{1}{(2\pi i)^2}
  \frac{\overline{\eta_1}\,d\bar\eta_2
  -\overline{\eta_2}\,d\bar\eta_1}{r^4}
  \wedge d\zeta_1\wedge d\zeta_2 ,
  \qquad d\bar\eta_j=d\bar\zeta_j-d\bar z_j .
\]

It also records the arity-two binary transfer:

\[
  \ell^{\mathrm{BM},N}_2(x,y)=p_N[ix,iy],
\]

the Hamiltonian bracket on monomials, and the Matlis coadjoint action

\[
  \ell^{\mathrm{BM},N}_2(z_1^pz_2^q,\rho_{i,j})
  =
  -(pj-qi+p-q)\operatorname{pr}_{\leq N}\rho_{i-p+1,j-q+1}.
\]

## Obstruction Surface

The all-window/arity-three target is now exact, not vague:

\[
  \operatorname{Ob}^{\infty}_{\mathrm{BM}}
  =
  \left(
  \operatorname{ob}_{\mathrm{mom}},
  (\operatorname{ob}_{\mathrm{collar},N})_N,
  (\operatorname{ob}^{\chi}_{3,N})_N,
  \operatorname{ob}_{\mathrm{unif}}
  \right).
\]

Components:

- \(\operatorname{ob}_{\mathrm{mom}}\): the class of the full moment
  sequence in \(\prod_{a+b>0}\C\rho_{a,b}/\mc P\).
- \(\operatorname{ob}_{\mathrm{collar},N}\): the cutoff-collar homotopy
  defect \(E_{\chi,N}\).
- \(\operatorname{ob}^{\chi}_{3,N}\): the first ternary
  cutoff/small-diagonal transfer term.
- \(\operatorname{ob}_{\mathrm{unif}}\): the unbounded-window seminorm
  class for the finite-window estimates.

The theorem states: the proved object is the finite-window normalized BMK
transfer with arity-two Hamiltonian/Matlis comparison; the all-window
theorem target is the construction of compatible primitives killing the
displayed vector.

## Attacks Closed

- A222-01: Appendix lacked a native BMK theorem surface.  Healed by
  `thm:app-finite-window-bmk-current-transfer`.
- A222-02: All-window direct-sum Matlis transfer could silently replace
  finite moments by an infinite product.  Healed by
  \(Q_{\mathrm{mom}}=\prod\C\rho_{a,b}/\mc P\).
- A222-03: Arity-three could be mistaken for proved strict transfer.
  Healed by the explicit \(\operatorname{ob}^{\chi}_{3,N}\) collar
  term.
- A222-04: Curve VOA/Zhu slippage.  Healed by the two-variable Cauchy
  face and the instability \(z_1\cdot\rho_{a,0}=-\rho_{a,1}\).

## Anchors Used

- `main.tex:1242`: `prop:finite-window-bm-native-e2-transfer`.
- `main.tex:1395`: main all-window obstruction vector.
- `appendix-matlis-principal-parts.tex:164`:
  `prop:app-matlis-coadjoint-action`.
- `reconstitution/swarm-2026-04-30-agent-206-bm-transfer-native-e2-construction.md`.
- `reconstitution/swarm-2026-04-30-agent-211-bm-transfer-main-integration.md`.

## Checks

Commands run:

```bash
git diff --check -- appendix-factorization-current-conventions.tex
rg -n -F -e "thm:app-finite-window-bmk-current-transfer" \
  -e "prop:finite-window-bm-native-e2-transfer" \
  -e "prop:app-matlis-coadjoint-action" \
  -e "Ob}^{\\infty}_{\\mathrm{BM}}" \
  main.tex appendix-factorization-current-conventions.tex \
  appendix-matlis-principal-parts.tex \
  reconstitution/swarm-2026-04-30-agent-206-bm-transfer-native-e2-construction.md \
  reconstitution/swarm-2026-04-30-agent-211-bm-transfer-main-integration.md
chktex -q appendix-factorization-current-conventions.tex
```

`git diff --check` passed.  `chktex` returned style warnings across the
appendix, including pre-existing dash/reference-spacing warnings and
similar local warnings in the new theorem block; no PDF build was run
because the assigned write surface excludes build artifacts.

Staging note: the appendix already had staged material and one unrelated
unstaged hunk before this pass.  I staged the BMK theorem hunk and this
report; the unrelated curved-kernel hunk remains unstaged.
