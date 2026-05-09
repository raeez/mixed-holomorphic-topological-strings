# Attack-heal wave 6: quantum descendant target

Date: 2026-04-28  
Role: Worker 4  
Worktree: `/private/tmp/topological-strings-remainder-wave6-20260428-073738/quantum-target`

## Claim Attacked

The wave5 obstruction killed the naive label map
\(\Psi_{a,b}\mapsto\rho_{a,b}\).  The remaining question was whether a
corrected quantum descendant complex exists, or whether every
\(\hbar\)-adic deformation of the classical primitive projection is
obstructed.

## Construction

The surviving construction is target-side.  For an interval \(I\),
the reduced quantum descendant target is
\[
  A^{\mathrm{pp}}_{\partial,\hbar}(I)
  =
  \widehat{\mathbf S}_{\C[[\hbar]]}
    (\Omega^\bullet_c(I)\widehat\otimes\bar A_\hbar)
  \widehat\otimes
  \widehat{\mathbf S}_{\C[[\hbar]]}
    ((\mathcal D'_c(I)\widehat\otimes\mathcal P[[\hbar]])[1]).
\]
The differential is the de Rham/current differential on the interval
factor and zero on \(\bar A_\hbar\) and \(\mathcal P[[\hbar]]\).
The bracket is
\[
  \{B_f(a),B_g(b)\}_\hbar=B_{\{f,g\}_\hbar}(ab),
  \qquad
  \{B_f(a),\Theta_\rho(B)\}_\hbar
    =\Theta_{\operatorname{ad}^{\vee}_{f,\hbar}\rho}(aB),
  \qquad
  \{\Theta_\rho(B),\Theta_\sigma(C)\}_\hbar=0 .
\]

For \(f=z_1^pz_2^q\), put
\[
  C_r(p,q;m,n)=
  \sum_{\alpha=0}^{r}(-1)^\alpha\binom r\alpha
  (p)_{r-\alpha}(q)_\alpha(m)_\alpha(n)_{r-\alpha}.
\]
Then the full Moyal coadjoint action is
\[
  z_1^pz_2^q\cdot_\hbar\rho_{a,b}
  =
  -\sum_{\substack{r\geq1\\r\ \mathrm{odd}}}
  \frac{\hbar^{r-1}}{2^{r-1}r!}
  C_r(p,q;a-p+r,b-q+r)
  \rho_{a-p+r,b-q+r},
\]
with negative indices and \((0,0)\) set to zero.  The \(r=1\) term is
the Matlis coadjoint action; \(r\geq3\) are the genuine Moyal terms.

## No-go

The polynomial one-\(\psi\) source still cannot map to this target.  If
\[
  T_\hbar(\widetilde\Psi_{a,b})=\rho_{a,b}[1]+O(\hbar)
\]
and the source linear Hamiltonians reduce to the PBW action
\[
  z_1\cdot_0\widetilde\Psi_{a,b}=b\widetilde\Psi_{a,b-1},
  \qquad
  z_2\cdot_0\widetilde\Psi_{a,b}=-a\widetilde\Psi_{a-1,b},
\]
then \(T_\hbar\) cannot intertwine the full Moyal coadjoint action.
Already modulo \(\hbar\),
\[
  T_0(z_1\cdot_0\widetilde\Psi_{1,0})=0,
  \qquad
  z_1\cdot_0T_0(\widetilde\Psi_{1,0})
    =z_1\cdot\rho_{1,0}[1]=-\rho_{1,1}[1].
\]
The coefficient differential on \(\mathcal P[[\hbar]]\) is zero, so
this is not a boundary in the reduced target.  A higher homotopy can
remove it only after changing the target complex or the classical
source action.

The wave5 high-order counterexample remains:
\[
  \operatorname{ad}^{\vee}_{z_1^4,\hbar}\delta_{1,1}
  =-24\hbar^2\delta_{0,4}+\cdots,
\]
whereas the PBW action sends
\(\widetilde\Psi_{1,1}\mapsto4\widetilde\Psi_{4,0}\).

## Computation Ranges

`scripts/check_one_psi_homology.py` now verifies:

- primitive one-\(\psi\) homology: 36 bidegrees, exponents \(\leq5\);
- open Hamiltonian action on primitive descendants: 240 cases,
  exponents \(\leq3\);
- classical Taylor-dual coadjoint formula: 1225 cases, exponents
  \(\leq5\);
- principal-part coadjoint realization: 1225 cases, exponents \(\leq5\);
- naive quantum descendant lift: 1225 cases, exponents \(\leq5\),
  Moyal order \(\leq5\), with 1200 PBW-vs-Moyal mismatches and 958
  cases with genuine higher Moyal coadjoint terms;
- corrected Moyal principal-part target: 3375 representation identities,
  exponents \(\leq3\), Moyal order \(\leq5\), \(\hbar\)-power
  \(\leq4\);
- no \(\hbar\)-adic deformation of the classical label projection:
  70 linear-generator leading-term tests with labels \(\leq5\).

## Files Changed

- `tate-T5-chain-level-primitive.tex`
- `scripts/check_one_psi_homology.py`
- `theorem-lanes.tex`
- `open-obligations.tex`
- `reconstitution/attack-heal-wave6-quantum-target-2026-04-28.md`

## Commands Run

- `sed -n ...` reads of the required instruction and target files.
- `rg -n ...` scans for descendant, Moyal, Rees/Fourier, and
  principal-part anchors.
- `python3 scripts/check_one_psi_homology.py`
- `rg -n "[ \t]+$" tate-T5-chain-level-primitive.tex scripts/check_one_psi_homology.py open-obligations.tex theorem-lanes.tex`
- `git diff --check -- tate-T5-chain-level-primitive.tex scripts/check_one_psi_homology.py`
- `make pdf`
- `rg -n '(^!|Emergency stop|Fatal error|Undefined control sequence|LaTeX Error|Missing \$|Extra |Runaway|File .* not found|No pages of output|Label\(s\) may have changed|undefined references|undefined citations|Rerun)' out/main.log`
- `rg -n 'Reference `|Citation `|undefined' out/main.log`
- `pdfinfo out/main.pdf`

`make pdf` exits 0 after replacing the forbidden memoir `\rm` use by
`\mathrm`.  The final log scan shows no fatal TeX errors, undefined
references, undefined citations, or rerun warnings.  The generated PDF
has 148 pages.

## Remaining Open Questions

1. Construct the unreduced boundary BV model whose cotangent sector
   lands in the reduced Moyal principal-part target.
2. Construct centrality homotopies against arbitrary unreduced open
   observables.
3. Prove the Costello brane-defect QME and anomaly cancellation for the
   principal-part target.
4. Any Fourier/Rees route that changes polarization remains a label or
   transformed-action bridge; it is not a same-action repair of the
   primitive polynomial one-\(\psi\) projection.
