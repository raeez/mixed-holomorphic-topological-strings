# 17:50 Execution Matrix

Date: 2026-04-28.

Canonical source:
`materials/processed/2026-04-28-1750-whitepaper-critical-analysis.txt`.

This matrix is the active execution control for the 17:50 critique. It
does not prove theorem lanes. It assigns each 17:50 scaffold component a
status, owner locus, acceptance gate, and fallback.

## Koszul Layers

| Layer | Content | Current Status | Owner Locus | Acceptance Gate |
|---|---|---|---|---|
| 0 | Operadic Lie/coComm Koszul self-duality | background | future layer ledger | Stated only as background; no local theorem depends on it. |
| 1 | Tate CE/bar-cobar identity | conditional/admissible | `main.tex`, `tate-T2-nilpotent-truncation.tex` | No application to full formal `h` without conilpotent/admissible proof. |
| 2 | Tate Quillen envelope | assumed envelope | `tate-T3-quillen-equivalence.tex` | Every claim says "in the fixed admissible envelope"; no raw-Tate global model-structure claim. |
| 3 | CE/PV derived `P_0` center | stable after conilpotency wording repair | `main.tex`, `theorem-lanes.tex` | Generator proof `c_I -> theta_I`, `u_I -> O_I` is stated without bar-cobar overhypothesis. |
| 4 | PBW/Rees special-fibre shadow | stable selected sector | `main.tex`, `tate-T5-chain-level-primitive.tex` | One-psi classes are labels/shadows, not Matlis principal parts. |
| 5 | Matlis/Grothendieck cotangent module | stable after notation repair | `appendix-matlis-principal-parts.tex`, `local-dictionary.tex` | Use `Ann_res`/C-linear residue-current language; no bare `Ann(C.1)` or `R`-submodule quotient. |
| 6 | Brane-line factorization current | open repair | `appendix-factorization-current-conventions.tex`, `main.tex` | Algorithm 7 compact-support contraction is written with degree/orientation checks. |
| 7 | Stable large-`N` bulk-boundary horizon | conjectural horizon | claim ledger / conclusion | Not used to prove the local theorem. |

## Algorithms

| Algorithm | Object Built | Current Status | Owner Locus | Acceptance Gate |
|---|---|---|---|---|
| A1 | Dirac probe construction | stable finite algebraic lane | `main.tex` | Moment-map sign, action, and `Q psi=[phi_1,phi_2]` are checked. |
| A2 | Classical bubble-sort homotopy | partially used, not full centrality | `main.tex`, `tate-T5-chain-level-primitive.tex` | Deterministic `H` and `QH+HQ=id-iN` are stated for the cyclic-word target. |
| A3 | Construction of `Psi_{a,b}` | stable selected sector | `main.tex`, `scripts/check_one_psi_homology.py` | Proof is written independent of finite scripts; scripts are checks only. |
| A4 | Matlis principal-part construction | stable after notation repair | `appendix-matlis-principal-parts.tex` | Cech representatives, `rho_{a,b}`, exclusion of `rho_{0,0}`, and residue pairing are explicit. |
| A5 | Coadjoint action by residue | stable | `appendix-matlis-principal-parts.tex`, `local-dictionary.tex` | Formula for `z_1^p z_2^q . rho_{a,b}` follows from residue pairing. |
| A6 | CE/PV derived-center construction | stable after conilpotency wording repair | `main.tex`, `theorem-lanes.tex` | CE and Schouten differentials match on `c_I,u_I`. |
| A7 | Compactly supported interval contraction | open repair | `appendix-factorization-current-conventions.tex`, `main.tex` | Choose `lambda_I`, define `p`, `i`, `K`, and prove `dK+Kd=id-ip`. |
| A8 | Reduced principal-part current bracket | stable reduced model | `main.tex`, `appendix-factorization-current-conventions.tex` | Brackets avoid distribution-distribution products and remain reduced/post-contraction. |
| A9 | Moyal coefficient computation | stable formal algebra | `main.tex`, `appendix-radial-parts-moyal.tex`, `scripts/check_moyal_coefficients.py` | Raw and normalized expansions are separated; normalized `hbar^2` correction is not denied. |
| A10 | Reduced Wick theorem | stable as reduced theorem, not Costello | `main.tex`, figure captions | All-order reduced Wick/Moyal theorem is distinct from analytic Costello realization. |

## Obligations

| Obligation | Status | Owner Locus | Acceptance Gate | Fallback |
|---|---|---|---|---|
| O1 All-`N` radial-parts normalization | open/conditional | `appendix-radial-parts-moyal.tex` | Define `J_N^{rad}`, radial image, injectivity theorem/hypothesis, and ordinary trace comparison. | Formal Moyal target only; finite scripts as evidence. |
| O2 Unreduced cotangent factorization center | open in active TeX | future cyclic-word appendix | Define `C_cyc,N,i,H,K_f`, prove `QH+HQ=id-iN` and centrality homotopy with signs/support. | Reduced defect-current model only. |
| O3 One-antifield quantum lift | target-side stable, unreduced lift open | `tate-T5-chain-level-primitive.tex` | Use `P[[hbar]]` with Moyal coadjoint action; do not lift polynomial `Psi` as same-action module. | Principal-part quantum target only. |
| O4 Mixed brane-defect QME | open obstruction theorem | `appendix-unreduced-bv-qme.tex`, `open-obligations.tex` | Boundary complex and `H^1` computed; QME routes have signs and data. | Candidate exits only. |
| O5 All-order Costello graph realization | open analytic theorem | `main.tex`, future Costello appendix | Nine prerequisites: mixed BV complex, defect, gauge fixing, heat kernel, propagator, brane-bulk kernel, scalar QME, connected trace normalization, product equality. | Reduced Wick theorem. |
| O6 Same-action Rees/Fourier `Psi <-> rho` | negative theorem stable | `appendix-matlis-principal-parts.tex` | State no same-action bridge; Fourier-Rees is polarization/label bridge only. | Label comparison only. |
| O7 Cross-volume consequences | no-transfer stable locally | `tate-P5-cross-volume.tex` | Matched-conventions theorem required before any compact CY3/BCOV/Vol III/BKM/Igusa/K3 x E consequence. | Motivation/convention checking only. |

## Callout Groups

| Callouts | Group | Current Status | Gate |
|---|---|---|---|
| C001-C020 | Structure and theorem naming | open repair | Add layer ledger, forbidden-conflation table, and status table. |
| C021-C040 | Dirac/open theory | mostly stable | Verify moment-map sign, scalar reduction, connected trace, and sector exclusions. |
| C041-C060 | Stable trace and descendants | selected sector stable | Scripts remain reproducibility checks; no `Psi ~= rho` module claim. |
| C061-C080 | Closed Hamiltonian BF | mostly stable | Check shift signs, completions, and closed fields versus observables. |
| C081-C100 | CE/PV center | stable after wording repair | Generator proof and bracket preservation are explicit; conilpotency not required for Layer 3. |
| C101-C120 | Principal parts | stable after notation repair | `Ann_res`, residue pairing, continuity, coadjoint formula, quantum coadjoint action. |
| C121-C140 | Factorization currents | open repair | Algorithm 7 and reduced/unreduced distinction written explicitly. |
| C141-C155 | Unreduced centrality | open in active TeX | Cyclic-word `N,i,H,K_f` theorem with signs/support. |
| C156-C170 | Scalar anomaly and QME | scalar anomaly stable, QME open | No classification before obstruction complex. |
| C171-C190 | Quantum/Moyal/radial/Costello | mixed | Moyal target stable; radial and Costello conditional; scripts finite only. |
| C191-C200 | Weighted Tate and firewalls | mostly stable | Weighted Tate is coefficient regulator; cross-volume consequences not asserted. |

## Immediate Roadmap Heals

1. Add a layer-status ledger to the manuscript control surface.
2. Add Algorithm A1-A10 owners and gates to the proof/source matrix.
3. Rewrite open obligations as O1-O7 plus separate hygiene obligations.
4. Add coupling-grammar theorem/proposition: closed-open couplings are
   maps into the derived `P_0` center, equivalently MC/twisting data or
   `U(g)` actions through central operations.
5. Patch manuscript summary defects: Costello labels, normalized
   `hbar^2`, `Ann_res`, `J_N^{rad}`, and stale script counts.
