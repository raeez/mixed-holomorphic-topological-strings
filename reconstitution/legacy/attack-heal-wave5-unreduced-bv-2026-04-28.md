# Worker 2 Report: Unreduced BV Cotangent Centrality / QME Lift

## Claim Attacked

The possible conflation was:

> the reduced CE/PV and reduced principal-part \(P_0\) current theorem
> already supplies an unreduced BV/factorization-centre morphism, its
> centrality homotopies, and a QME-compatible quantum cotangent lift.

Status after attack: false.  The lift is not closed honestly.  The
manuscript now records the exact obstruction in `open-obligations.tex`,
`theorem-lanes.tex`, and `principles.tex`.

## Strongest Failure Mode

The obstruction is already present before analytic regularization.

The open BV degrees and CE/PV type check are:

\[
|\phi_i|=0,\qquad |\psi=A^*|=-1 \text{ and odd},\qquad Q\psi=[\phi_1,\phi_2],
\]
\[
|H_f|=0,\qquad |\eta_\rho=\rho[1]|=-1,\qquad |c_f|=1,\qquad |u_\rho|=0.
\]

The CE/PV map sends the shifted-cotangent CE coordinate \(u_\rho\) to
a degree-zero Hamiltonian central operation.  It does not send the
Hamiltonian ghost coordinate \(c_f\) to a boundary observable, and it
does not identify the polynomial one-\(\psi\) classes with the
principal-part module.

The linear Hamiltonians give the decisive test:

\[
\{O_{1,0},\widetilde\Psi_{a,b}\}=b\,\widetilde\Psi_{a,b-1},
\qquad
\{O_{0,1},\widetilde\Psi_{a,b}\}=-a\,\widetilde\Psi_{a-1,b},
\]
but
\[
z_1\cdot\rho_{a,b}=-(b+1)\rho_{a,b+1},
\qquad
z_2\cdot\rho_{a,b}=(a+1)\rho_{a+1,b}.
\]

The index shifts go in opposite directions.  No bidegree-only
identification \(\Psi_{a,b}\leftrightarrow\rho_{a,b}\) can be an
\(\mathfrak h\)-module map.  Hence the primitive one-\(\psi\)
projection is a label shadow, not an unreduced centrality homotopy.

## QME Obstruction

The weighted Tate route closes the coefficient Casimir and finite-scale
propagator in the weighted coefficient category.  It does not prove QME
vanishing.  The remaining class is

\[
\operatorname{Ob}\in
H^1\bigl(\mathcal O_{\mathrm{loc}}(\mathcal E_w),
Q+\{I_0,-\}\bigr).
\]

The scalar boundary contact is explicit:

\[
\{I_\partial(a,f),I_\partial(b,g)\}_{\mathrm{open}}
=I_\partial(ab,\{f,g\}_{\bar A})
  +N\,\omega(f,g)\int_\R a(t)b(t)\,dt ,
\]
and quantum mechanically
\[
\operatorname{Tr}(A\,XY)-\operatorname{Tr}(A\,YX)
=\hbar N\,\operatorname{Tr}(A)
\quad\bmod\ \mathcal W_N\widehat\mu(\mathfrak{gl}_N).
\]

A QME theorem must cancel this class by a closed exchange graph and
counterterm, remove it by a specified supertrace or central-character
normalization, or absorb it into the renormalized boundary generators.
No such construction is present.

## Local Anchors

- `principles.tex`: Witten convention now explicitly states that the
  unreduced centrality and QME lift are not supplied by the reduced
  theorem.
- `theorem-lanes.tex`: the CE/PV lane now excludes BV heat-kernel,
  BV Laplacian, and QME-compatible graph conclusions; the reduced
  principal-part lane records the \(\Psi\) versus \(\rho\) mismatch.
- `open-obligations.tex`: the unreduced cotangent centre and mixed
  brane-defect QME entries now display the degree/sign formulas and
  scalar contact obstruction.
- Existing proof anchors: `main.tex` around
  `cor:descendant-coadjoint-difference`,
  `prop:reduced-principal-part-boundary-current`,
  `prob:formal-factorization-center`,
  `prob:weighted-rg-locality`,
  `cor:local-bulk-boundary-coupling`, and
  `lem:tate-casimir-obstruction`.

## Primary Source Anchors

- Costello 2007/2011 BV package: local mirror
  `references/primary-sources/costello-renormalisation-bv-0706.1533.txt`
  records the BV setup, heat-kernel propagator, renormalized QME, and
  RG formalism; the source-anchoring ledger warns not to depend on
  unverified published theorem numbers.
- Costello--Li quantum BCOV:
  `references/primary-sources/costello-li-quantum-bcov-1201.4501.txt`
  lines 890--928 define the RG/QME/locality axioms for BCOV
  quantization.
- Costello--Li open-closed BCOV:
  `references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt`
  lines 79--82 prove the odd-dimensional flat
  \(\mathfrak{gl}(N|N)\) theorem, while lines 103--109 state the
  ordinary \(\mathfrak{gl}_N\) one-loop anomaly obstruction.

These sources support the manuscript's use of Costello vocabulary and
the anomaly warning.  They do not prove the mixed
\(\R^2\times\C^2\), brane \(\R\times p\), ordinary \(\mathfrak{gl}_N\)
QME lift.

## Files Changed

- `open-obligations.tex`
- `theorem-lanes.tex`
- `principles.tex`
- `reconstitution/attack-heal-wave5-unreduced-bv-2026-04-28.md`

## Commands Run

- Read rule and context files: `CLAUDE.md`, `AGENTS.md`,
  `~/ecosystem/INVARIANTS.md`, `~/ecosystem/AGENTS-HARNESS.md`.
- Read manuscript context: `main.tex`, `principles.tex`,
  `theorem-lanes.tex`, `open-obligations.tex`, `commands.tex`,
  `mathmacros.tex`, `notation.tex`, `preamble.tex`, `nomenclature.tex`.
- Read relevant appendices/fragments:
  `appendix-factorization-current-conventions.tex`,
  `appendix-matlis-principal-parts.tex`,
  `tate-T1-weighted-completion.tex`,
  `tate-T4-bv-vanishing.tex`,
  `tate-T5-chain-level-primitive.tex`,
  `tate-P1-hadamard-mittag-leffler.tex`,
  `tate-P5-cross-volume.tex`.
- Read source anchors in `references/primary-sources/` and
  `/Users/raeez/calabi-yau-quantum-groups/FRONTIER.md`.
- Search commands used `rg` for `unreduced`, `BV`, `QME`,
  `centrality`, `cotangent`, `factorization`, and source terms.
- Verification attempted with `make pdf`.  The build stopped before
  processing the edited TeX because `raeez-math-template.sty` is a
  broken symlink to `../latex-template/raeez-math-template.sty`; the
  target directory is absent in this worktree.

## Operational Note

The first relative `apply_patch` wrote duplicate hunks to the base
checkout instead of this assigned worktree.  Those duplicate hunks and
the duplicate report file were removed immediately by an exact reverse
patch.  The surviving edits are the files listed above inside
`/private/tmp/topological-strings-remainder-wave5-20260428-061212/finite-bv`.

## Remaining Open Questions

1. Construct actual unreduced boundary representatives for
   \(\rho[1]\) in a non-polynomial boundary observable category, not just
   the reduced principal-part target.
2. Build centrality homotopies against arbitrary unreduced open
   observables before primitive/cumulant projection.
3. Compute the mixed brane-defect QME obstruction class in
   \(H^1(\mathcal O_{\mathrm{loc}}(\mathcal E_w),Q+\{I_0,-\})\).
4. Decide whether the scalar contact term is cancelled by closed exchange
   graphs, removed by supertrace/central-character normalization, or
   absorbed into renormalized boundary generators.
5. Prove regulator independence between the weighted coefficient model
   and the original unweighted Tate pair, or keep the quantum theorem
   explicitly weighted and conditional.
