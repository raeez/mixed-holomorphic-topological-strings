# Proof and Source Owner Matrix

Date: 2026-04-28.

This matrix turns the active roadmap into auditable proof obligations.
The "owner" column names the locus responsible for the proof; no human
ownership is implied.

| Claim family | Current status | Proof owner | Source owner | Acceptance gate |
|---|---|---|---|---|
| Reduced local CE/PV spine | stable after notation cleanup | `main.tex`, `theorem-lanes.tex` | local CE/PV computation plus `source-convention-ledger` | Use `Z^{P_0}_{red}` for reduced PV; no full-center wording. |
| Interval current local constancy | open repair | `appendix-factorization-current-conventions.tex` | compact-support de Rham/locality sources | Prove shifted `H_c^\bullet(I)` lemma and recompute CE degrees. |
| Continuous Tate HKR | open theorem lane | future Tate-HKR lemma in `main.tex` or appendix | primary HKR/factorization/Tate source anchors | Finite-window proof, topology, bracket compatibility, `lim^1` control. |
| Full open BV/factorization algebra | open construction | `appendix-unreduced-bv-qme.tex` plus future appendix | Costello-Gwilliam/Costello plus local definitions | Define fields, topology, BV bracket, differential, pairings, products. |
| Full `Z^{P_0}_{fact}` morphism | open construction | future centrality theorem | full open BV construction plus bubble-sort proof | Typed centrality homotopy against all claimed open observables. |
| Full primitive stable Koszul homology | open computation | `tate-T5-chain-level-primitive.tex` | local script/proof plus invariant-theory anchors | Include higher psi/Tor classes or restrict theorem explicitly. |
| Conilpotent Koszul duality | restricted/conditional | `tate-T2-nilpotent-truncation.tex`, `tate-T3-quillen-equivalence.tex` | bar-cobar/Koszul primary anchors | Apply only to conilpotent/admissible replacement, not full formal Hamiltonian algebra. |
| Matlis principal parts | stable with wording repair | `appendix-matlis-principal-parts.tex`, `local-dictionary.tex` | Matlis/local cohomology/residue anchors | `Ann_res` inside `H^2_m`; no `R`-submodule quotient or bare `Ann(C.1)`. |
| Rees/Fourier bridge | partial label/lattice comparison | `appendix-matlis-principal-parts.tex` | local Rees/Fourier computation | State Rees lattice label comparison only unless a chain map is built. |
| One-psi PBW shadow | partial/open beyond selected sector | `tate-T5-chain-level-primitive.tex`, `scripts/check_one_psi_homology.py` | local computation/invariant theory | All `(k,l)` and sign/cell proof before full theorem wording. |
| Radial-parts theorem | conditional | `appendix-radial-parts-moyal.tex`, `scripts/check_moyal_coefficients.py` | Levasseur-Stafford/Wallach/Capelli anchors plus local proof | Define `Rad_N`, image, Capelli correction, connected projection, stable target. |
| Moyal parity | repair required | `main.tex`, `scripts/check_moyal_coefficients.py` | direct Moyal expansion | Raw odd powers; normalized even powers with general `\hbar^2 P^3/24`. |
| Reduced Wick coefficients | stable as reduced computation | figure captions, coefficient scripts/prose | local Wick/Moyal computation | Label as reduced Wick coefficients, not Costello graph theorem. |
| Costello graph realization | open theorem lane | future Costello appendix | Costello/Costello-Gwilliam anchors | Field complex, heat kernel, propagators, counterterms, coefficient match. |
| Weighted Tate regulator | finite-window stable, limit open | `tate-T1-weighted-completion.tex`, `tate-P1-hadamard-mittag-leffler.tex` | local finite-window proof plus Tate references | Do not claim product/product BV inverse or renormalized limit without proof. |
| QME cancellation/classification | open classification | `appendix-unreduced-bv-qme.tex` | local BV/QME computation plus Costello anchors | Fix sign/value, define obstruction complex, compute `H^1`. |
| Cross-volume consequences | firewall/no-transfer | `tate-P5-cross-volume.tex`, `principles.tex` | sibling repo anchors | No compact CY3/Vol III/BKM/Igusa consequence without separate matched theorem. |

## Immediate Hygiene Scans

These scans are necessary but not sufficient:

```bash
rg -n "Z\\^\\{P_0\\}_\\{fact\\}|Ann\\(C\\.1\\)|Costello graph normalizations|hbar\\^2 correction|exactly three" .
rg -n "partly constructed / open unreduced lift" claim-strength-ledger.tex theorem-lanes.tex open-obligations.tex abstract.tex
```

Passing these scans only proves editorial hygiene. The hard lanes pass
only by their acceptance gates.
