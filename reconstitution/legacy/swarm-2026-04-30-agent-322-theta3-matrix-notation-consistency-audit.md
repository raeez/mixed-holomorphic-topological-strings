# Swarm 2026-04-30 Agent 322: Theta3 Matrix Notation Consistency Audit

Report-only audit. No TeX edited. No build run.

## Claim Attacked

The post-patch manuscript might conflate the theta3 lower Bianchi matrix
notation with the generic finite-window non-scalar obstruction pair, or might
carry stale signs after the `\Delta^1_{M,N}` naming and BMK pro-Matlis patches.

## Verdict

No live TeX contradiction found.

The current theorem surface keeps the levels separate:

- generic pair:
  `\mathfrak O^{\mathrm{ns}}_n=(([\mathfrak o^{\mathrm{ns}}_{n,M}])_M,\lambda_n)`;
- theta3 fixed lower basis:
  `(E^2_{\nu_{02}},E^2_{\nu_{20}},\mathfrak b^2_{02,20})`;
- source-coordinate column:
  `A_D^2=(-2,2,1)^T`;
- lower residual:
  `r_2=(2,-2,0)^T`;
- missing Bianchi-killing local-functional column:
  `A_B^2=(0,0,-1)^T`;
- transport cocycle:
  `\Delta^1_{M,N}:=-\pi_{M,N}\mathfrak b^M+\mathfrak b^N`.

The matrix signs are coherent: `A_D^2c=-r_2` is inconsistent in the current
free presentation; if a genuine `A_B^2` column is constructed, then
`A_D^2+A_B^2=-r_2`.

## Evidence Anchors

- Generic obstruction pair: `main.tex:8617-8622`,
  `open-obligations.tex:690-700`, `claim-strength-ledger.tex:1329-1335`.
- Theta3 one-row gate: `main.tex:8757-8832`,
  `appendix-unreduced-bv-qme.tex:2416-2455`,
  `theorem-lanes.tex:3433-3452`.
- Lower Bianchi matrix: `main.tex:8875-8924`,
  `theorem-lanes.tex:3505-3542`, `open-obligations.tex:886-923`,
  `claim-strength-ledger.tex:949-963`.
- Missing `B` column and transport: `main.tex:8932-8962`,
  `theorem-lanes.tex:3544-3571`, `open-obligations.tex:925-950`,
  `claim-strength-ledger.tex:964-984`.
- BMK separation: `main.tex:1248-1462`,
  `theorem-lanes.tex:489-528`, `open-obligations.tex:274-309`,
  `claim-strength-ledger.tex:319-336`.

## Remaining Defects

1. `appendix-unreduced-bv-qme.tex` contains the generic `A^Mc=-r^M` criterion
   and the theta3 one-row obstruction, but not the lower Bianchi-exposed
   `A_D^2,r_2,A_B^2,\Delta^1_{M,N}` notation. Patch target:
   add a corollary after `prop:app-closed-rows-and-theta-three-source-face`,
   or cross-reference the main theta3 acceptance gate.

2. The one-row theta3 complex is called `\mathcal Q_{\theta_3,M}` in
   `main.tex`, `open-obligations.tex`, and `claim-strength-ledger.tex`, but
   `\mathcal K_{\theta_3,M}` in `appendix-unreduced-bv-qme.tex` and
   `theorem-lanes.tex`. This is compatible but not maximally clean. Patch
   target: add a convention equating the finite-window non-scalar kernel
   notations, or standardize the symbol.

3. Older internal reports still use the two-coordinate lower residual
   `(2,-2)^T` and the two-coordinate column `(-2,2)^T`. Patch target:
   future synthesis must mark those as pre-Bianchi-exposure and use the live
   three-coordinate basis.

4. `scripts/finite_window_graph_array.py` does not yet emit the
   three-coordinate Bianchi matrix record. Patch target: add a lower
   Bianchi-exposed matrix block if this row becomes machine-gated.

## Files Changed

- `reconstitution/theta3-matrix-notation-consistency-audit-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-322-theta3-matrix-notation-consistency-audit.md`
