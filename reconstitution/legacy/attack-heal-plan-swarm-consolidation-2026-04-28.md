# Attack-Heal Swarm Consolidation

Date: 2026-04-28.

Inputs:

- Plan under attack:
  `reconstitution/platonic-clean-paper-plan-2026-04-28.md`.
- Critical feedback:
  `materials/processed/2026-04-28-0836-whitepaper-critical-analysis.txt`.
- Launch record:
  `reconstitution/attack-heal-plan-swarm-launch-2026-04-28.md`.
- First-wave attackers: A01 through A06, all read-only.

No consensus theorem is inferred from the agents. This file records which
attacks survive integration and how the manuscript plan must be healed.

## Executive Decision

The old governing sentence is too strong. The surviving theorem spine is
not:
```tex
closed observables \simeq Z^{P_0}_{fact}(full open BV algebra).
```

The surviving core is:
```tex
C^\bullet_{\mathrm{CE},cont}
  (\mathfrak h\ltimes\mathfrak h^\vee_{cont}[1])
  \cong
\mathrm{PV}_{red}(\mathcal O(\mathfrak h^\vee_{cont}))
```
as a reduced local Poisson-CE/PV model, mapped to a selected
scalar-reduced connected Hamiltonian PBW sector of the first-class Dirac
brane probe. Full unreduced factorization centrality, continuous Tate
HKR, Costello graphs, QME cancellation, all-`N` radial parts, and
cross-volume consequences remain conditional or open.

## Dependency-Ordered Root Causes

### R1. Full Factorization-Center Overclaim

Attacks: A01-006, A01-007, A03-01, A05-09, A06-003, A06-007.

Failure:

- The manuscript proves or defines a reduced constant-stalk
  Poisson-CE/PV model.
- It does not yet prove a full morphism into the `P_0` factorization
  center of the unreduced open BV/factorization algebra.
- Continuous HKR for the completed symmetric algebra on the relevant
  Tate current algebra is not checked.
- Multiplication by a closed element is ordinary centrality in a
  graded-commutative model; it is not the main theorem.

Heal:

- State the theorem as a reduced local CE/PV model.
- Use `Z^{P_0}_{fact}` only after defining the reduced convention, or
  after proving the real factorization-center theorem.
- Demote multiplication centrality to a lemma.
- Reserve theorem strength for compatibility of the CE differential,
  Schouten/PV differential, current/factorization functoriality, and
  brane-sector target map.

Survives:

- The generator-level CE/PV coordinate correspondence survives after
  degree corrections.

### R2. Degree, Shift, and Compact-Support Conventions

Attacks: A01-001, A01-002, A01-003, A01-004.

Failure:

- `\Omega^\bullet_c(I)` on an open interval has its point-like compact
  support class in top degree, not degree zero.
- The degree-zero boundary Poisson bracket and the shifted
  Schouten/Gerstenhaber bracket cannot be silently identified.
- The coordinate `u_K` is not closed:
  `d_{CE}u_K=C^L_{KJ}u_Lc^J`.
- The shift convention for cotangent coordinates must say whether `[1]`
  raises or lowers cohomological degree.

Heal:

- Add a sign/degree block before CE/PV.
- Represent interval point currents by `a(t)dt` with the orientation
  shift visible.
- Separate the boundary Poisson bracket from the shifted PV bracket.
- Replace every "closed CE coordinate `u`" phrase by "degree-zero CE
  coordinate with the displayed CE differential."

Survives:

- `c^I -> theta^I` and `u_I -> O_I` survive as typed generator
  assignments.

### R3. Scalar Quotient and Effective Group

Attacks: A03-03, A05-07, A06-002.

Failure:

- `Tr(psi)` is a genuine `GL_N` Koszul class.
- Removing constants on the closed Hamiltonian side explains why it is
  not paired, but it does not by itself derive deletion from the finite
  `GL_N` Dirac probe.
- The scalar anomaly cannot sit after derived-center/factorization
  claims. It decides the effective brane sector.
- The plan's "exactly three" QME cancellation routes are not proved and
  omit manuscript alternatives.

Heal:

- Move scalar quotient/effective group before the CE/PV center theorem.
- Choose either an effective `PGL_N`/`\mathfrak sl_N` brane sector or a
  `GL_N` sector with explicit decoupled scalar exterior factor.
- State QME mechanisms as a classified list, not an iff theorem, until
  the obstruction complex is computed.
- Fix the central-character sign before any counterterm claim.

Survives:

- The scalar contact class and Capelli class remain real obstruction
  data.
- The finite moment-map sign and first-class identity survived A03's
  attack.

### R4. Koszul Duality and Conilpotence

Attacks: A01-005, A05-01.

Failure:

- The admissible continuous bar-cobar lemma assumes Tate/conilpotent
  hypotheses.
- The full formal Hamiltonian algebra with linear modes is explicitly
  not known to satisfy those hypotheses.
- Therefore the full Hamiltonian CE algebra cannot be advertised as
  having Koszul dual `\widehat U(\mathfrak g)` by that lemma.

Heal:

- Stratify "Koszul duality" into finite operadic, admissible Tate
  bar-cobar, reduced CE/PV, PBW special fibre, Matlis duality, and
  large-`N` horizon layers.
- Prove the full local Hamiltonian CE/PV identity directly on
  generators, or prove a new nonconilpotent completed bar-cobar theorem.

Survives:

- Admissible nilpotent/weighted envelopes may retain bar-cobar theorems.
- The reduced CE/PV generator identity is independent of this failure.

### R5. Matlis, PBW Descendants, and Rees/Fourier

Attacks: A02-001 through A02-009, A03-06, A06-004.

Failure:

- `\mathcal P=Ann(C*1)` is not an `R`-submodule. Multiplication by
  `z_1` sends `rho_{1,0}` to `rho_{0,0}` under the `R`-module action.
- The correct structure is a C-linear residue annihilator stable under
  Hamiltonian coadjoint action.
- The no-go proof for maps from principal parts to polynomial
  locally-nilpotent modules uses injectivity it does not have.
- Direction slogans such as "lowering action" are false globally.
- The abstract's denial of a Rees/Fourier bridge is too broad: there is
  a limited Fourier-delta associated-graded label bridge, but not a
  same-action `\mathfrak h`-module bridge.

Heal:

- Define `\mathcal P=Ann_{res}(C*1)` inside
  `H^2_m(C[[z_1,z_2]]) dz_1dz_2`.
- Say `\mathcal P` is a Hamiltonian coadjoint module, not an
  `R`-submodule.
- Patch the no-go theorem: either weaken it to no
  isomorphism/embedding, or prove Hom-vanishing without injectivity and
  remove the unproved reflection statement.
- Replace direction slogans by "adjoint polynomial action" and
  "coadjoint principal-part action"; display the linear examples.
- State the Rees/Fourier bridge as a label-lattice theorem only:
  `partial_1^a partial_2^b e_0` maps to
  `(-1)^{a+b}\hbar^{a+b}a!b! rho_{a,b}`.

Survives:

- The residue pairing and coadjoint formula survive:
  ```tex
  z_1^p z_2^q\cdot\rho_{a,b}
  =-(pb-qa+p-q)\rho_{a-p+1,b-q+1}.
  ```
- The front dictionary's separation of `c,u,theta,O,Psi,rho,Theta_rho`
  is structurally correct.

### R6. Stable Trace and One-Psi Sector

Attacks: A03-02, A03-04, A03-05.

Failure:

- `S(\bar A\oplus\bar A_{desc}[1])` is not the full open algebra. It is
  a selected scalar-reduced connected Hamiltonian PBW sector.
- Scalar `Tr(psi)` and higher-psi primitive homology are excluded by
  definition, not derived away.
- The stable trace range needs an exact Procesi/Razmyslov source theorem
  or an internal proof in the manuscript's word-degree convention.
- The one-psi homology proof needs an all-`(k,l)` cellular contraction,
  not just the finite script sweep.

Heal:

- Replace "the open algebra" by "selected scalar-reduced connected
  Hamiltonian PBW sector" wherever the formula is meant.
- Insert the exact stable invariant theorem and degree range.
- Write the chip-moving/Abel-map proof with stabilizers, orientations,
  and cyclic quotients explicit.

Survives:

- The finite Dirac moment-map computation and sign convention survive.
- The one-psi result is plausible and supported by finite checks, but
  not yet proof-grade at theorem strength.

### R7. Quantum Degree-Zero Lane

Attacks: A04-001 through A04-010, A05-05.

Failure:

- The raw star commutator has odd powers of `\hbar`; the normalized
  Hamiltonian bracket `\hbar^{-1}[f,g]_*` has even powers.
- The normalized bracket generally has a nonzero `\hbar^2` coefficient;
  for example the reported computation gives a nonzero `P^3/24` term.
- The all-order finite-`N` comparison uses a conditional radial-parts
  theorem but is sometimes stated without that hypothesis.
- The stable quantum target is ill-typed if it is an ordinary
  `N -> infinity` object over `C[[\hbar]]`, because Capelli terms contain
  powers of `N`, such as `\hbar N`.
- Connected projection is a linear cumulant operation unless the
  discarded subspace is proved to be a Lie/two-sided ideal.
- The script currently does not prove higher normalized `\hbar`
  coefficients or connected projection compatibility.

Heal:

- Split the quantum lane into:
  1. unconditional formal Weyl/Moyal coefficient algebra;
  2. finite-`N` Capelli basis and normalizer descent;
  3. conditional radial-parts comparison;
  4. chosen stable coefficient object.
- State parity correctly: raw odd, normalized even.
- Define stable quantum coefficients over `C[[\hbar,\lambda]]` with
  `\lambda=\hbar N`, as a polynomial-in-`N` pro-system, or only at the
  associated graded leading-symbol level.
- Extend the script if it is cited for higher-order behavior.

Survives:

- The formal Moyal coefficient formula survives.
- Weyl-ordered invariant traces normalize the quantum moment-map ideal,
  but this is not the radial theorem.

### R8. Weighted Tate, BV Pairing, QME, and Costello Graphs

Attacks: A05-02, A05-03, A05-06, A05-08, A05-10.

Failure:

- A product/product weighted pair is not automatically a continuous
  scalar-valued BV pairing on arbitrary product tails.
- Weighted finite-scale control is not the
  `epsilon -> 0, L -> infinity` renormalized Costello theorem.
- First/third coefficients currently compute reduced open-line
  Weyl/Wick data, not Costello brane-defect graph normalizations.
- Figure language can be read as analytic graph proof if it keeps
  Costello vocabulary without kernel, measure, orientation, counterterm,
  automorphism, and QME data.

Heal:

- State weighted Tate as finite-window/pro-kernel regulator control
  unless a continuous pairing is constructed.
- Restrict limits, counterterms, and QME to named open problems unless
  proved.
- Retitle figures as reduced Wick coefficient diagrams, or provide full
  Costello graph data.

Survives:

- The strict product/direct-sum endpoint no-go survives.
- Hadamard/Mittag-Leffler control is not currently being used as QME
  cancellation; preserve that firewall.

### R9. Architecture, Status Ledger, and Cross-Volume Firewall

Attacks: A06-001, A06-005, A06-006, A06-008, A06-009.

Failure:

- The claim-strength ledger uses undefined statuses.
- Some cross-volume material sits too early in the proof path.
- The proof/source ledger is not yet complete enough for the number of
  conditional theorem lanes.
- Verification scans are too narrow.

Heal:

- Define every status used by the abstract, ledger, theorem lanes, and
  open obligations.
- Collapse or move cross-volume programmatics behind a non-transfer
  theorem.
- Make proof-owner/source-owner coverage executable.
- Add scans for broad direction slogans, undefined statuses,
  overconfident quantum phrases, stale source anchors, process leakage,
  and cross-volume terms.

Survives:

- The 08:36 critique preservation and provenance row are correct.

## Destroyed or Demoted Claims

| Old claim | New status | Required proof to restore |
|---|---|---|
| Full closed observables are `Z^{P_0}_{fact}` of the full open BV algebra | Demoted to reduced local CE/PV model | Continuous Tate HKR, compact-support current shifts, unreduced centrality homotopies |
| Full Hamiltonian CE has Koszul dual `\widehat U(g)` by the current lemma | Invalid as written | Nonconilpotent completed bar-cobar theorem or admissible restriction |
| `\mathcal P` is an `R`-submodule/quotient by `rho_{0,0}` | Invalid | Use C-linear residue annihilator and coadjoint module language |
| Polynomial `Psi` and Matlis `rho` are bridgeable as same-action modules | Invalid | Change action/target or prove a different theorem |
| `S(\bar A+\bar A_{desc}[1])` is the open algebra | Demoted | Full primitive Koszul homology computation |
| Scalar `Tr(psi)` disappears just by removing closed constants | Invalid | Effective `PGL_N` model or explicit scalar factor |
| Normalized Moyal bracket has no `hbar^2` correction | False | Cannot restore under standard normalization |
| All-order radial-parts comparison is unconditional | Conditional | Exact source theorem or internal proof |
| Stable quantum target is ordinary `N -> infinity` over `C[[hbar]]` | Ill-typed | Choose `lambda=hbar N`, pro-system, or associated graded |
| First/third diagrams are Costello graph computations | Demoted | Full elliptic BV graph package and QME/anomaly treatment |
| Exactly three QME cancellation routes | Not proved | Obstruction-complex classification with signs |

## Stable Core

The first wave leaves the following core intact:

1. Finite first-class Dirac matrix probe, with the moment-map sign
   convention and first-class identity intact.
2. Effective scalar-reduced Hamiltonian brane sector, once the
   `PGL_N`/`\mathfrak sl_N` choice or scalar factor is stated.
3. Selected connected PBW one-psi label sector, provided it is not called
   the full open algebra.
4. Reduced local CE/PV generator identity for
   `\mathfrak h\ltimes\mathfrak h^\vee_{cont}[1]`, after degree and
   compact-support conventions are fixed.
5. Matlis residue-current coadjoint module and residue pairing formula.
6. Limited Fourier-Rees associated-graded label bridge.
7. Formal Weyl/Moyal coefficient algebra, with raw-versus-normalized
   powers stated correctly.
8. Reduced Wick coefficients as algebraic targets.
9. Strict endpoint no-go and Hadamard/Mittag-Leffler versus QME firewall.
10. Cross-volume non-transfer as a theorem-style firewall.

## Immediate Integration Queue

1. Put sign/degree conventions before CE/PV.
2. Move scalar quotient/effective group before center claims.
3. Rewrite the governing theorem as reduced local Poisson-CE/PV.
4. Split Koszul duality into named layers.
5. Patch Matlis wording: C-linear residue annihilator, not `R`-submodule.
6. Replace all raising/lowering slogans by typed action names.
7. Patch quantum parity and mark radial parts conditional.
8. Retitle graph figures as reduced Wick coefficient diagrams unless the
   Costello theorem is supplied.
9. Define every claim-status word and remove cross-volume proof-path
   leakage.
10. Add executable scans for all of the above.

## Verification Gates

The plan is not stable until these gates pass:

```bash
rg -n "lowering|raising" main.tex abstract.tex theorem-lanes.tex local-dictionary.tex open-obligations.tex appendix-*.tex tate-*.tex
rg -n "closed CE coordinate|second-order vanishes|hbar\\^2 correction|no remaining obstruction|exactly three" main.tex abstract.tex theorem-lanes.tex local-dictionary.tex open-obligations.tex appendix-*.tex tate-*.tex
rg -n "Z\\^\\{P_0\\}.*full|factorization-center equivalence|full open BV" main.tex abstract.tex theorem-lanes.tex local-dictionary.tex open-obligations.tex appendix-*.tex tate-*.tex
rg -n "partly constructed|open unreduced lift" claim-strength-ledger.tex theorem-lanes.tex open-obligations.tex abstract.tex
python3 scripts/check_one_psi_homology.py
python3 scripts/check_moyal_coefficients.py
make pdf
```

Expected interpretation:

- Some hits may be legitimate quoted warnings, theorem titles, or open
  obligations. The gate is "zero inappropriate hits", not zero raw hits.
- Script success is reproducibility evidence only. It does not replace
  the all-`(k,l)` one-psi proof or higher-order normalized Moyal tests.
