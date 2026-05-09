# Agent 340 Progress Audit: Current Theorem State

Ownership: report-only in `reconstitution/`.  No TeX or script edits.

Evidence boundary: the live log records agents 321-337 with materialized reports or
closures, and records 338-339 as launched/live without report artifacts in this
checkout.  I therefore treat the checked-out `main.tex`, `theorem-lanes.tex`,
`open-obligations.tex`, `claim-strength-ledger.tex`, and materialized 321-337
reports as evidence, not unreported 338/339 intent.  Live-log anchors:
`reconstitution/swarm-live-launch-log-2026-04-30.md:2119-2251`.

## 1. Native holomorphic E2 and BMK

Reconstituted:

- The native object is now the holomorphic `E_2`/factorization algebra on
  `C^2`, with mixed topological enhancement on `R^2_top x C^2_hol`; it is not
  a curve vertex algebra and not a compact Calabi-Yau claim.
  Anchors: `main.tex:1110-1230`, `theorem-lanes.tex:227-379`,
  `claim-strength-ledger.tex:650-663`.
- The CE/factorization observable object and semidirect collision algebra are
  theorem-grade in the local model.
  Anchors: `main.tex:1193-1230`, `main.tex:1670-1697`,
  `theorem-lanes.tex:381-480`.
- BMK data have been reconstituted only to the correct strength: current-limit
  BMK data, finite Matlis moment maps, arity-two output projection, and the
  one-pair analytic pro-Matlis retract are proved.
  Anchors: `main.tex:1260-1451`, `main.tex:2520-2597`,
  `theorem-lanes.tex:481-533`, `open-obligations.tex:274-283`,
  `claim-strength-ledger.tex:323-331`.
- The BMK source boundary was tightened: external BMK/Koppelman material is a
  source for the pre-cutoff analytic kernel and classical homotopy only, not
  for the support-local native current theorem.
  Anchors: `main.tex:1289-1312`, `theorem-lanes.tex:481-503`,
  `reconstitution/swarm-2026-04-30-agent-333-bmk-source-boundary-heal.md:1`.

Still open:

- Strict native all-window support-local current transfer remains open.  The
  finite-current obstruction is `Ob^{BMK-curr}_N`; the strict all-window
  obstruction is the six-entry `Ob^{Pi}_{BM}`.
  Anchors: `main.tex:1362-1429`, `main.tex:1710-1721`,
  `theorem-lanes.tex:506-545`, `open-obligations.tex:284-309`,
  `claim-strength-ledger.tex:332-340`, `claim-strength-ledger.tex:664-693`.
- The decisive finite-window obstruction includes the displayed
  `z_1^{N+2}`/rho row and projected Jacobiator; no current text promotes the
  one-pair analytic retract to a native support-local all-window quotient.
  Anchors: `main.tex:1386-1429`, `theorem-lanes.tex:515-533`.

## 2. LQT and cyclic trace comparison

Reconstituted:

- Loday-Quillen-Tsygan is now used as a template/source theorem, not as an
  imported coordinate-ring invariant theorem for the local model.
  Anchors: `main.tex:1981-2010`, `open-obligations.tex:143-160`.
- The proved local statement is the finite-window stable Eulerian comparison:
  block-sum stable primitive projection by the Eulerian idempotent, single-cycle
  trace span, and scalar one-psi quotient in the stated stable range.
  Anchors: `main.tex:2011-2060`, `open-obligations.tex:161-178`.

Still open:

- The raw same-rank operation is not certified as a chain map.  The remaining
  bridge is the separated-block/Roos-stabilized comparison, with obstruction
  vector `O_{LQT,K,L}` and same-rank defect `Gamma_N`.
  Anchors: `open-obligations.tex:179-212`.

## 3. Radial/Weyl, `Omega^{rad}`, and decorated PBW Stokes

Reconstituted:

- The formal Weyl/Moyal coefficient package is proved: raw odd Moyal
  coefficients, Capelli/free-normal ordering data, open-line Wick first/third
  coefficients, and the reduced degree-zero comparison through the stated
  algebraic targets.
  Anchors: `main.tex:8273-8402`, `main.tex:9158-9284`,
  `theorem-lanes.tex:2549-2648`, `claim-strength-ledger.tex:1238-1268`.
- The all-N Weyl trace problem has been sharpened to equivalent obstruction
  surfaces: moment-ideal primitive `E_{a,b,N}`, free normal-diagram obstruction
  `o_{a,b}`, dual potential `Omega^{rad}_{a,b}`, and decorated PBW Stokes
  equation.
  Anchors: `main.tex:7394-7491`, `main.tex:7576-7612`,
  `theorem-lanes.tex:2649-2719`, `open-obligations.tex:1354-1388`,
  `claim-strength-ledger.tex:996-1023`.
- Edge strips and finite certificates were propagated with current bounds:
  all edge families `(2,b),(b,2)`, balanced diagonal through `(6,6)`,
  all non-edge total degree `<=12`, listed total-degree 13 interiors, and
  listed total-degree 14 interiors except the frontier cases.
  Anchors: `main.tex:2437-2467`, `main.tex:2752-2812`,
  `open-obligations.tex:1389-1426`,
  `reconstitution/swarm-2026-04-30-agent-337-open-obligations-radial-heal-report.md:1`.
- The current frontier is correctly non-obstructional: `(6,8)`, `(8,6)`,
  and `(7,7)` are computation/frontier cases, not proved nonzero obstruction
  rows.
  Anchors: `open-obligations.tex:1427-1436`,
  `claim-strength-ledger.tex:581-594`,
  `claim-strength-ledger.tex:1024-1043`,
  `reconstitution/swarm-2026-04-30-agent-321-radial-decorated-stokes-computational-frontier-audit.md:1`.

Still open:

- The global theorem is exactly the all-bidegree decorated PBW Stokes/dual
  potential theorem: construct the signed-row homotopy/contraction proving
  `Omega^{rad}_{a,b}=0`, or exhibit the signed-row obstruction.  No current
  file claims that theorem is closed.
  Anchors: `main.tex:7439-7491`, `main.tex:8308-8402`,
  `open-obligations.tex:1437-1453`,
  `claim-strength-ledger.tex:1024-1043`.

## 4. Componentwise quantum coefficient surface

Reconstituted:

- The componentwise product surface is now explicit:
  weighted BV/Casimir data, balanced scalar-contact zero branch, principal-part
  current/Moyal coadjoint brackets, and a radial-gated Hamiltonian generator
  factor.
  Anchors: `main.tex:8435-8566`, `theorem-lanes.tex:2721-2791`,
  `open-obligations.tex:498-544`, `claim-strength-ledger.tex:221-239`,
  `claim-strength-ledger.tex:1270-1292`.
- The statement no longer advertises this as a full Costello graph/QME theorem.
  It is a componentwise surface with explicit gates to the non-scalar QME and
  radial packages.
  Anchors: `main.tex:8558-8566`, `theorem-lanes.tex:2788-2898`.

Still open:

- A larger non-scalar Costello graph realization remains open outside the named
  minimal habitat.  The next gates are scalar projection/lift, reduced QME
  class, finite-window pair arrays, curved bulk-to-defect kernel, and centrality
  homotopies.
  Anchors: `theorem-lanes.tex:2792-2898`,
  `claim-strength-ledger.tex:1294-1341`.

## 5. Non-scalar QME, `theta_3`, and `Delta^1`

Reconstituted:

- The finite-window non-scalar QME problem is now a concrete obstruction
  criterion: local-functional complex, scalar-symbol projection, reduced class
  `[Ob^{red}]`, kernel curvature equation, counterterm recursion, closed
  exchange triple, and row equations.
  Anchors: `main.tex:8616-8850`, `theorem-lanes.tex:3373-3471`,
  `open-obligations.tex:546-792`, `claim-strength-ledger.tex:924-994`.
- The minimal full-equivariant finite-window branch is theorem-grade only in
  its named minimal marked habitat; it does not solve the larger non-scalar
  package.
  Anchors: `theorem-lanes.tex:3444-3471`,
  `appendix-unreduced-bv-qme.tex:3031-3309`,
  `claim-strength-ledger.tex:226-239`.
- The `theta_3` gate has been sharpened to exact finite-window alternatives:
  CE ancestor, scalar-zero Costello counterterm, or complete companion-face
  table with transport compatibility.
  Anchors: `main.tex:8852-9121`, `theorem-lanes.tex:3472-3611`,
  `open-obligations.tex:794-956`, `claim-strength-ledger.tex:516-550`.
- The lower Bianchi-exposed row is now present: `A_D^2=(-2,2,1)^T`,
  `r_2=(2,-2,0)^T`, no solution to `A_D^2 c=-r_2`, and the needed new column
  `A_B^2=(0,0,-1)^T` is identified.
  Anchors: `main.tex:9042-9119`, `theorem-lanes.tex:3548-3611`,
  `appendix-unreduced-bv-qme.tex:2502-2643`,
  `reconstitution/swarm-2026-04-30-agent-332-appendix-theta3-notation-heal-report.md:1`.

Still open:

- No current file supplies the CE ancestor, scalar-zero Costello counterterm, or
  complete companion-face table for `theta_3`.
  Anchors: `main.tex:8852-9121`, `claim-strength-ledger.tex:516-550`.
- The tower compatibility remains the `Delta^1_{M,N}` and secondary
  `varprojlim^1 H^0` problem.  This is named precisely, not closed.
  Anchors: `main.tex:9100-9121`, `theorem-lanes.tex:3592-3611`,
  `open-obligations.tex:928-956`.
- For the larger non-scalar QME theorem, scalar-zero projection, local
  counterterms, kernel curvature, finite row arrays, transition matrices, Roos
  compatibility, and centrality homotopies remain to be constructed.
  Anchors: `main.tex:8616-8850`, `theorem-lanes.tex:3373-3471`,
  `claim-strength-ledger.tex:1294-1341`.

## 6. Weiss/Roos and stratified factorization

Reconstituted:

- The stratified target is now stated as a construction problem, not a hidden
  consequence of Darboux stalks: finite brane branch, stable principal-part
  branch, collar restrictions, internal descent defect, and Cech/Roos class.
  Anchors: `main.tex:4675-4707`, `theorem-lanes.tex:3115-3250`,
  `open-obligations.tex:1000-1169`, `claim-strength-ledger.tex:846-899`.
- The source-primary Weiss material is quarantined as external comparison
  support.  The local manuscript requires internal Weiss/Cech/Roos data.
  Anchors: `theorem-lanes.tex:3210-3235`,
  `open-obligations.tex:1131-1169`, `claim-strength-ledger.tex:866-899`.

Still open:

- The internal stratified descent theorem remains open: construct the
  prefactorization-to-factorization descent, collar compatibility, centrality
  homotopies, and kill the internal obstruction vector
  `Ob^{int}_{str,Omega,N}` together with the Cech/Roos class.
  Anchors: `theorem-lanes.tex:3189-3250`,
  `open-obligations.tex:1131-1237`, `claim-strength-ledger.tex:846-899`.

## 7. Omega-background

Reconstituted:

- The native Omega background is the brane-preserving normal scaling torus on
  `N_LX=R_s + C_{z_1} + C_{z_2}` with `t` fixed, with
  `Q_Omega=Q+iota_{V_Omega}` and `Q_Omega^2=L_{V_Omega}`.
  Anchors: `theorem-lanes.tex:2901-2925`,
  `open-obligations.tex:1000-1040`,
  `claim-strength-ledger.tex:596-620`.
- Finite-window weighted kernel admissibility is stated under character,
  nonresonance, residue/Euler normalization, and small-denominator hypotheses.
  Anchors: `theorem-lanes.tex:2927-3007`,
  `appendix-unreduced-bv-qme.tex:2645-2867`.
- The physical trace state surface is now a target with explicit topology,
  Ward identities, cumulant bounds, convergence, and QME/source obstruction
  vector.
  Anchors: `theorem-lanes.tex:3252-3369`,
  `open-obligations.tex:1239-1352`, `claim-strength-ledger.tex:900-923`.

Still open:

- The Omega QME theorem is not closed.  The obstruction vector
  `Ob^{QME}_{Omega,w}` still requires scalar projection, non-scalar kernel
  curvature zero, finite row compatibility, transition/Roos control, and
  centrality homotopies.
  Anchors: `theorem-lanes.tex:3066-3112`,
  `claim-strength-ledger.tex:596-620`, `claim-strength-ledger.tex:924-940`.
- The physical large-N Omega trace state remains a construction target, not a
  theorem.
  Anchors: `theorem-lanes.tex:3252-3369`,
  `open-obligations.tex:1239-1352`.

## 8. Compact-Calabi-Yau firewall

Reconstituted:

- The local theorem surface is firewalled from compact Calabi-Yau, CoHA,
  quintic, HKQ/CDGP/GV/OSV, Abel-Jacobi, MNOP/chiral-volume, Igusa,
  Borcherds, and BKM consequences.
  Anchors: `main.tex:8219-8233`, `main.tex:9602-9630`,
  `open-obligations.tex:9-13`, `claim-strength-ledger.tex:57-79`.
- External compact/global material can enter only by a matched-conventions
  comparison theorem with its own obstruction vector; it is not evidence for
  the core local Hamiltonian BF/Moyal theorem.
  Anchors: `open-obligations.tex:1478-1517`,
  `claim-strength-ledger.tex:246-252`,
  `claim-strength-ledger.tex:1408-1431`.

Still open:

- No compact-Calabi-Yau theorem is open inside the core manuscript.  The only
  admissible future surface is an explicitly assigned external comparison
  theorem with matched conventions and vanishing/null-homotopy data.
  Anchors: `main.tex:9602-9630`, `open-obligations.tex:1478-1517`.

## 9. Exact remaining theorem surfaces

Current open theorem surfaces after the materialized 321-337 band are:

1. Native all-window BMK support-local current transfer: kill or replace
   `Ob^{Pi}_{BM}` after the finite-current `Ob^{BMK-curr}_N` gate.
2. LQT fixed-rank/raw same-rank bridge: separated-block stabilization/Roos
   comparison remains the admissible route; `Gamma_N` blocks the raw map.
3. All-bidegree radial/Weyl trace theorem: prove the decorated PBW
   Stokes/signed-row theorem for `Omega^{rad}_{a,b}`, with frontier cases
   `(6,8)`, `(8,6)`, `(7,7)` still computational, not obstructional.
4. Larger non-scalar Costello QME realization: scalar lift, `[Ob^{red}]`,
   counterterm tower, curved kernel, finite row arrays, transition matrices,
   Roos compatibility, and centrality homotopies.
5. `theta_3`: construct one of the three accepted witnesses and then solve the
   `Delta^1_{M,N}`/secondary `varprojlim^1 H^0` transport problem.
6. Stratified Weiss/Roos descent: internal descent, collar, Cech/Roos, and
   centrality data are named but not constructed.
7. Omega-background QME and physical trace state: finite-window weighted
   kernels are formulated; full QME, centrality, Roos, and state-convergence
   requirements remain open.
8. Compact/global comparison: quarantined external route only; no compact
   theorem is part of the current local theorem surface.

No checked-out file I audited promotes any of these eight surfaces to closed
theorems after the current 321-339 integration band.
