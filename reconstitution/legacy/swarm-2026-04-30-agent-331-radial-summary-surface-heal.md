# Agent 331: radial appendix summary surface heal

Date: 2026-04-30.

Owned write paths:

- `appendix-radial-parts-moyal.tex`
- `reconstitution/swarm-2026-04-30-agent-331-radial-summary-surface-heal.md`

Scope correction honored: `main.tex`, `theorem-lanes.tex`, and
`claim-strength-ledger.tex` were not edited.

Concurrency update honored: Agent 334's displayed \(K_{4,4}\) layout in
`appendix-radial-parts-moyal.tex` was preserved.  The theorem-surface
patches were checked against the current file state after that update.

## Attacked Claims

1. Appendix summary language still treated the fixed-lift
   \(\mathfrak o_{a,b}\in\operatorname{coker}\mathcal C_{a,b}\) Hodge
   class as the exact radial obstruction.
2. The trace-diagram and edge-summary paragraphs still pointed to a
   global contracting-homotopy or left-cokernel theorem rather than the
   current theorem surface.
3. The appendix did not explicitly state the square-cell Stokes upgrade
   \[
     \Omega^{\mathrm{rad}}_{a,b}=0
     \Longleftrightarrow
     D^\square_{a,b}H_{a,b}=R^{\mathrm{free}}_{a,b},
     \qquad
     D^\square_{a,b}=C^+_{a,b}\partial_2 .
   \]
4. The computational frontier cases \((6,8),(8,6),(7,7)\) needed to be
   recorded as timeout/frontier cases, not obstruction rows.

## Patches

- `appendix-radial-parts-moyal.tex:646`: replaced the old global
  homotopy obligation by the decorated PBW Stokes identity and normalized
  signed-row failure certificate.
- `appendix-radial-parts-moyal.tex:901`: made
  \(\mathfrak o_{a,b}\) an intermediate kernel-correction class after a
  classical lift, not the final radial obstruction.
- `appendix-radial-parts-moyal.tex:907`: retitled and reworded the Hodge
  statement as a fixed-lift criterion, pointing the exact obstruction to
  \(\Omega^{\mathrm{rad}}\), \(D^\square\), and signed rows.
- `appendix-radial-parts-moyal.tex:988`: inserted the square-cell PBW
  Stokes complex, the ordinary necklace Stokes theorem
  \(\operatorname{im}\partial_2=\ker\partial\), and the upgraded
  dual-potential obstruction theorem.
- `appendix-radial-parts-moyal.tex:1172`: rewrote the potential-form
  remark so the row condition is \(\lambda D^\square_{a,b}=0\), with
  square-cell Green operator \(D^\square(D^\square)^*\).
- `appendix-radial-parts-moyal.tex:1239`,
  `appendix-radial-parts-moyal.tex:1531`,
  `appendix-radial-parts-moyal.tex:1808`, and
  `appendix-radial-parts-moyal.tex:1870`: propagated the same exact
  obstruction theorem through edge, finite-\(N\), verification, and final
  realization-boundary summaries.

## Verification Commands

```text
git status --short -- appendix-radial-parts-moyal.tex \
  reconstitution/swarm-2026-04-30-agent-331-radial-summary-surface-heal.md \
  main.tex theorem-lanes.tex claim-strength-ledger.tex

rg -n -e "uniform" -e "left-cokernel" -e "left cokernel" \
  -e "old coker" -e "coker C" -e "contracting homotopy" \
  -e "obstruction class" -e "free normal-diagram obstruction" \
  appendix-radial-parts-moyal.tex

rg -n -F -e "Omega^{\\mathrm{rad}}" -e "D^\\square" \
  -e "normalized signed" -e "(6,8)" -e "(8,6)" -e "(7,7)" \
  appendix-radial-parts-moyal.tex

git diff --check -- appendix-radial-parts-moyal.tex

git diff --no-index --check -- /dev/null \
  reconstitution/swarm-2026-04-30-agent-331-radial-summary-surface-heal.md
```

Result: stale-phrase grep returned no hits; current-surface grep returned
the expected appendix anchors; `git diff --check` passed on the TeX file;
the no-index whitespace check passed on this report.

## Remaining Exact Frontiers

The all-bidegree decorated PBW Stokes identity is still open.  The exact
next deliverable is either a proof that
\[
  D^\square_{a,b}H_{a,b}=R^{\mathrm{free}}_{a,b}
  \quad\text{for all }a,b,
\]
or the first normalized signed row
\[
  (\phi,-\lambda)\in\ker B_{a,b}^*,
  \qquad
  \lambda(E^+_{a,b})-\phi(T_{a,b})=1.
\]
The bidegrees \((6,8),(8,6),(7,7)\) remain exact-enumeration timeouts in
the current harness.  They are not known obstruction rows.
