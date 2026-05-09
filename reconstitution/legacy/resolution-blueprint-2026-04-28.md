# Resolution Blueprint for the Main Casualties

Date: 2026-04-28.

This blueprint gives construction instructions for the major casualties
identified by the canonical 17:50 critique, with the earlier 08:36
critique and C-wave attack-heal agents treated as archival supporting
evidence. It does not declare these lanes proved. It defines what a
proof would have to contain and what fallback statement is allowed until
then.

The active 17:50 execution matrix is
`reconstitution/roadmap-1750-execution-matrix-2026-04-28.md`. Where that
matrix is more specific, it governs this file.

## 1. Full `Z^{P_0}_{fact}` and Open BV Center

Target theorem:

```tex
\mathcal O_{\mathrm{closed}}^{P_0}
  \longrightarrow
Z^{P_0}_{fact}(\mathrm{Obs}_{open}^{unred,pp})
```

in a specified completed dg BV/factorization category, with explicit
centrality homotopies against all open observables.

Construction DAG:

1. Introduce separate notation
   `Z^{P_0}_{red}(A):=\mathrm{PV}_{red}(A)` for the reduced local CE/PV
   model. Reserve `Z^{P_0}_{fact}` for the full abstract center.
2. Fix the interval current object as
   `\Omega_c^\bullet(I)\widehat\otimes\mathfrak h` with the necessary
   shift or density convention. Prove the compact-support integration
   lemma and recompute CE degrees and brackets.
3. Prove or cite with matching hypotheses a continuous Tate HKR theorem:
   finite windows, transition maps, antisymmetrization, Hochschild/PV
   bracket compatibility, completion topology, and `lim^1` control.
4. Prove cosheaf/factorization functoriality for completed symmetric
   algebras: extension by zero, restriction duality, disjoint-union
   product, associativity, and topology.
5. Define `\mathrm{Obs}_{open}^{unred,pp}`: field complex, topology,
   completed algebra, BV bracket, differential, pairings, factorization
   products, and map from ordinary open observables.
6. Compute the full primitive stable Koszul homology, including higher
   psi/Tor classes, or prove that omitted classes are outside the stated
   center claim.
7. Type the 17:50 bubble-sort construction: cyclic domain, signs, normal
   ordering, current smearing, `H`, `K_{f,\rho}`, source/target degrees,
   and the identity
   ```tex
   \{O_f,\Theta_\rho\}+\Theta_{f\cdot\rho}=[Q,K_{f,\rho}].
   ```

Acceptance gate:

- A numbered theorem states the category, the source, the target, the
  centrality identity, and the factorization products.
- Every homotopy has explicit degree and sign.
- The proof covers arbitrary open observables or explicitly restricts
  the theorem to a named subalgebra.

Fallback until proved:

- State only the reduced local CE/PV model and the selected
  scalar-reduced Hamiltonian brane sector. Do not use full
  `Z^{P_0}_{fact}` language for the reduced convention.

## 2. Conilpotent Koszul Duality for the Hamiltonian Algebra

Target theorem:

A conilpotent/admissible filtered replacement of the formal Hamiltonian
Lie algebra satisfies the bar-cobar/Koszul comparison used by the paper.

Construction DAG:

1. Define admissible finite windows and the transition maps.
2. Prove pronilpotence or conilpotence in that replacement category.
3. Prove Mittag-Leffler/continuity needed to pass from windows to the
   completed object.
4. Identify exactly which CE/PV theorem survives the passage.
5. Separate any full formal disk statement from finite-window evidence.

Acceptance gate:

- A lemma verifies conilpotence/pronilpotence for the actual object used.
- No statement applies the conilpotent bar-cobar lemma to the full
  unfiltered formal Hamiltonian algebra.

Fallback until proved:

- Use direct reduced CE/PV computations and mark any Tate extension
  conditional/admissible.

## 3. Matlis Principal Parts

Target theorem:

Principal parts form the Matlis residue-current coadjoint module

```tex
E_R(k)\simeq H^2_{\mathfrak m}(\mathbb C[[z_1,z_2]])
```

with C-linear residue basis `\rho_{a,b}` and coadjoint Hamiltonian
action.

Construction DAG:

1. State the Cech-Laurent model and residue pairing.
2. Define `\operatorname{Ann}_{res}(\mathbb C\cdot 1)` inside the
   local cohomology/residue-current object, not as an `R`-submodule.
3. Prove the coadjoint action by residue integration by parts.
4. Record the strict no-polynomial/no-same-action obstruction.
5. State the Rees/Fourier bridge only as a label/lattice comparison
   unless a chain map is constructed.

Acceptance gate:

- No active text says principal parts are an `R`-submodule quotient or
  bare `Ann(C.1)`.
- The action formulas are coadjoint principal-part formulas, not
  polynomial raising/lowering slogans.

Fallback until proved:

- Use the C-linear Matlis residue-current module and keep polynomial
  descendants as PBW shadows.

## 4. Unconditional Radial Parts and Stable Quantum Target

Target theorem:

For every `N`, a specified radial-parts map `Rad_N` carries the open
operator algebra to the stated Weyl/Moyal target with the exact Capelli
normalization and connected projection.

Construction DAG:

1. Define the source filtered differential-operator algebra and target
   coefficient ring. Decide between `C[[\hbar,\lambda]]`, a pro-system
   in `N`, or an associated-graded target.
2. Define `Rad_N`, its domain, and its image.
3. Prove the Capelli/triangular correction formula.
4. Prove pure-power and Weyl-shear generation of mixed monomials.
5. Prove connected projection/cumulant compatibility as a Lie quotient
   or a linear projection theorem.
6. Match script checks to the theorem statement and keep finite-rank
   checks as evidence only.

Acceptance gate:

- The all-`N` theorem does not cite finite-rank scripts as proof.
- The coefficient ring supports the displayed `\hbar N` and
  `\hbar^2 N^3` terms.
- The connected projection is proved to preserve the bracket structure
  claimed.

Fallback until proved:

- State the radial-parts comparison as conditional on the all-`N`
  input; present exact `N=2,3` checks as evidence.

## 5. Moyal Parity and `\hbar^2` Corrections

Target theorem:

The raw Moyal commutator has odd powers of `\hbar`; the normalized
Hamiltonian bracket `\hbar^{-1}[f,g]_*` has even powers and generally a
nonzero `\hbar^2` term proportional to `P^3(f,g)/24`.

Construction DAG:

1. Fix the star-product normalization.
2. Write raw commutator and normalized bracket expansions separately.
3. Compute the first nonzero correction for the generators used in the
   manuscript.
4. Align scripts and prose with the same normalization.

Acceptance gate:

- No text asserts "no `\hbar^2` correction" for the normalized bracket
  unless the particular pair has `P^3(f,g)=0`.

Fallback until proved:

- Keep only formal coefficient computations with stated normalization.

## 6. Costello Graph Theorem from Reduced Wick Diagrams

Target theorem:

An elliptic BV/Costello brane-defect theory realizes the reduced
first/third Wick coefficients as renormalized graph weights.

Construction DAG:

1. Define the field complex, defect condition, gauge fixing, and heat
   kernel.
2. Define boundary/defect propagators and interaction vertices.
3. Prove locality, counterterm recursion, and obstruction-complex
   vanishing or exhibit the obstruction.
4. Compute the first and third graph weights in the Costello scheme.
5. Match those weights to the reduced Wick coefficients with all
   normalizations.

Acceptance gate:

- A Costello theorem includes heat kernels, propagators, scale
  dependence, counterterms, and the coefficient match. Reduced Wick
  diagrams alone do not pass.

Fallback until proved:

- Call the existing diagrams "reduced Wick coefficient diagrams"; state
  the Costello realization as conditional/open.

## 7. Weighted Regulator and BV Pairing

Target theorem:

The finite-window weighted Tate regulator has a continuous BV inverse
pairing and a controlled limit in the stated topology.

Construction DAG:

1. Define finite-window fields and pairings.
2. Prove kernel compatibility under window transitions.
3. Prove admissible-weight equivalence as transported observables, not
   raw observable stabilization.
4. State exactly which unweighted strict endpoint is ruled out.
5. Separate finite-scale graph bounds from renormalized
   `\epsilon\to0`, `L\to\infty` limits.

Acceptance gate:

- Product/product pairings are not described as actual BV inverse
  kernels unless continuity is proved.

Fallback until proved:

- Use finite-window weighted control and the strict unweighted no-go.

## 8. QME Classification

Target theorem:

The QME obstruction problem is governed by an explicit obstruction
complex, with a computed `H^1` and a classification of solutions only if
that computation is complete.

Construction DAG:

1. Fix the QME sign convention and compute whether the central character
   is `0`, `N`, or `-N` in the normalization used.
2. Define the local-functional complex containing the scalar contact
   class.
3. Compute the BV Laplacian and bracket contributions.
4. Compute the obstruction cohomology controlling inequivalent
   counterterms.
5. Prove classification only after all cocycles and coboundaries are
   enumerated.

Acceptance gate:

- No "exactly three" or "if and only if" QME statement appears before
  the obstruction complex is computed.

Fallback until proved:

- Present scalar contact, Capelli, and counterterm mechanisms as an open
  menu of candidate cancellations, not a classification.

## 9. Cross-Volume Non-Transfer

Target theorem:

The local formal-disk Hamiltonian BF/Moyal theorem does not imply compact
Calabi-Yau, global BCOV, Vol III, Borcherds, BKM, Igusa, K3 x E, or
sister-volume consequences without a separate matched-conventions
functor.

Construction DAG:

1. List exactly the local data used:
   `C[[z_1,z_2]]`, `dz_1 wedge dz_2`, `h`, `P`, and the scalar class
   `[bar c]`.
2. List absent global data: compact Calabi-Yau fields, global BCOV
   anomaly data, chiral homology over compact curves, Borcherds
   denominator identities, Igusa cusp-form coefficients, K3 x E cycles,
   and sibling-volume convention identifications.
3. Define a matched-conventions datum preserving degree shifts,
   pairings, central classes, factorization products, and normalizations.
4. State that no cross-volume consequence is asserted without such a
   datum and proof.

Acceptance gate:

- Every global or sibling-volume sentence is either firewall language or
  cites a separate matched-conventions theorem.

Fallback until proved:

- Keep cross-volume material as motivation and convention checking only.
