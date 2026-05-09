# Agent 149 Local Chiral-Algebra Taxonomy

Date: 2026-04-30.

Owned writable surface: `local-dictionary.tex`, `theorem-lanes.tex`, and
this report.  No subagents were launched.  The checkout already had staged
swarm edits in `local-dictionary.tex` and `theorem-lanes.tex`; this pass
edited the current working tree on top of those changes and did not revert
or stage other work.

## Stable Core

The word "chiral" is now fenced to local factorization meanings inside the
formal-local mixed HT theory on
\[
  \mathbb R^2_{\mathrm{top}}\times
  \widehat{\mathbb C^2}_{0,\mathrm{hol}} .
\]
The allowed objects are:

1. the formal Hamiltonian holomorphic factorization algebra on
   \(\mathbb C^2\);
2. the mixed topological-current enhancement over
   \(\mathbb R^2_{\mathrm{top}}\);
3. the Weyl/Moyal open-string brane algebra, with matrix/supermatrix
   cyclic bar-cobar trace avatars;
4. the defect/principal-part current algebra on brane intervals.

None is compact-CY chiral homology, a one-dimensional vertex algebra, a
CoHA, a quintic/GV/OSV object, an Abel--Jacobi normal-function object, an
Igusa product, a Borcherds lift, or a BKM algebra.

## Valid Attacks

```yaml
id: A149-01
severity: 2
status: healed
lens: taxonomy gap
target: local-dictionary.tex, theorem-lanes.tex
claim: The manuscript's local use of chiral/factorization language is already disambiguated.
broken_step: The assigned files had no local taxonomy distinguishing the holomorphic factorization algebra, mixed topological-current enhancement, Weyl/Moyal brane algebra, and principal-part defect current algebra.
evidence_type: missing_source
evidence_ref: pre-repair rg found no local chiral taxonomy in local-dictionary.tex or theorem-lanes.tex
minimal_heal: Add a dictionary taxonomy and a theorem-lane statement with exact formulas.
residual: None for the local taxonomy.
```

```yaml
id: A149-02
severity: 2
status: healed
lens: vertex-algebra overclaim
target: theorem-lanes.tex
claim: A brane-line or current statement can be read as a one-dimensional vertex algebra.
broken_step: The brane interval is a real topological line and the holomorphic sector is two-complex-dimensional. A VOA would require an extra complex-line or holomorphic-defect restriction theorem.
evidence_type: proof_gap
evidence_ref: main.tex definitions of local holomorphic/mixed factorization sectors; theorem-lanes brane-current lanes
minimal_heal: State explicitly that a vertex algebra requires choosing a complex line or holomorphic defect, proving restriction to disks in that line, and constructing OPE modes.
residual: Such a restriction theorem remains open and is not used.
```

```yaml
id: A149-03
severity: 2
status: healed
lens: compact-CY firewall
target: local-dictionary.tex, theorem-lanes.tex
claim: The word chiral could import compact-CY chiral homology, CoHA, or BKM objects.
broken_step: Existing compact-CY firewalls did not name compact-CY chiral homology or vertex algebra in the local dictionary's inadmissible-use row.
evidence_type: unsupported
evidence_ref: local-dictionary.tex admissible/inadmissible table before repair
minimal_heal: Add compact-CY chiral homology and one-dimensional vertex-algebra structure to the inadmissible imports, and repeat the exclusion in the theorem lane.
residual: External matched-conventions comparison remains outside the core theorem.
```

```yaml
id: A149-04
severity: 3
status: healed
lens: cyclic-avatar conflation
target: local-dictionary.tex, theorem-lanes.tex
claim: Matrix/supermatrix cyclic bar-cobar avatars can be treated as CoHA or compact chiral-homology structures.
broken_step: The cyclic avatars here are trace/supertrace word complexes for the brane Weyl algebra and balanced scalar-contact branch, not Hall multiplication or compact curve/surface chiral homology.
evidence_type: line_reference
evidence_ref: main.tex Weyl/Moyal and balanced supertrace formulas; reports 140, 143, 146
minimal_heal: Define the Weyl/Moyal brane algebra separately from cyclic/supercyclic trace bookkeeping and add explicit non-CoHA/non-BKM exclusions.
residual: None inside the local brane algebra taxonomy.
```

## Repairs Made

- Added `Local chiral/factorization taxonomy` to `local-dictionary.tex`.
- Extended the local dictionary inadmissible-use row to exclude compact-CY
  chiral homology and one-dimensional vertex-algebra structure.
- Added `thm:lane-local-chiral-taxonomy` to `theorem-lanes.tex`.
- Split the new Moyal and principal-part bracket displays after the first
  draft TeX pass showed overfull boxes.

## Exact Definitions and Formulas

Formal Hamiltonian holomorphic object:
\[
  \mathfrak h=\mathbb C[[z_1,z_2]]/\mathbb C\cdot1,\qquad
  \mathfrak g=\mathfrak h\ltimes
  \mathfrak h^\vee_{\mathrm{cont}}[1],
\]
\[
  \Omega_c^{0,\bullet}(B)\widehat\otimes\mathfrak g,
  \qquad
  C^\bullet_{\mathrm{CE},\mathrm{cont}}(\mathfrak g)
  \text{ as the formal CE/PV stalk only under the stated completions.}
\]

Mixed topological-current enhancement:
\[
  \mathfrak g^{\mathrm{mix}}_{U,B}
  =
  \Omega^\bullet_c(U)\widehat\otimes
  \Omega^{0,\bullet}_c(B)\widehat\otimes\mathfrak g .
\]

Weyl/Moyal brane target:
\[
  P=\partial_{z_1}\otimes\partial_{z_2}
   -\partial_{z_2}\otimes\partial_{z_1},
\]
\[
  f*g=m\circ\exp\!\left(\frac{\hbar}{2}P\right)(f\otimes g),
  \qquad
  \{f,g\}_\hbar=\hbar^{-1}(f*g-g*f),
\]
\[
  [(\phi_1)^i{}_j,(\phi_2)^k{}_l]
  =\hbar\,\delta^i_l\delta^k_j .
\]

Defect/principal-part current algebra:
\[
  \mathfrak h_I=\Omega^\bullet_c(I)\widehat\otimes\mathfrak h,\qquad
  \mathcal P_I=\mathcal D'_c(I)\widehat\otimes\mathcal P,\qquad
  \mathfrak g_I=\mathfrak h_I\ltimes\mathcal P_I[1],
\]
\[
  A^{\mathrm{pp}}_\partial(I)
  =
  \widehat{\mathbf S}(\Omega_c^0(I)\widehat\otimes\bar A)
  \widehat\otimes
  \widehat{\mathbf S}(\mathcal D'_c(I)\widehat\otimes\mathcal P[1]),
\]
\[
  \{B_f(a),B_g(b)\}=B_{\{f,g\}}(ab),\qquad
  \{B_f(a),\Theta_\rho(B)\}=\Theta_{f\cdot\rho}(aB),\qquad
  \{\Theta_\rho(B),\Theta_\sigma(C)\}=0 .
\]

Vertex-algebra restriction obligation:
a one-dimensional vertex algebra requires an added theorem choosing a
complex line or holomorphic defect, proving factorization on disks in that
line, and constructing OPE modes.  No theorem lane now asserts this.

## Verification

Commands run:

```bash
rg -n "chiral algebra|vertex algebra|chiral homology|CoHA|quintic|OSV|GV|Abel-Jacobi|Igusa|BKM|factorization|current algebra|Moyal|Weyl|principal-part" main.tex local-dictionary.tex theorem-lanes.tex appendix-unreduced-bv-qme.tex appendix-factorization-current-conventions.tex
rg -n -F -e "formal holomorphic" -e "local holomorphic" -e "Hamiltonian BF" -e "CE/PV" -e "factorization algebra on" -e "vertex algebra" -e "chiral" main.tex theorem-lanes.tex local-dictionary.tex appendix-factorization-current-conventions.tex appendix-unreduced-bv-qme.tex
rg -n "label\{(def:local-holomorphic-string-sector|def:local-th-string|thm:formal-disk-completed-ce-pv|thm:reduced-ce-pv-central-operation|thm:hamiltonian-current-factorization|thm:reduced-principal-part-boundary-current|cor:app-factorization-principal-part-current-brackets|prop:moyal-monomial|thm:finite-n-reduced-moyal)\}" main.tex theorem-lanes.tex appendix-factorization-current-conventions.tex
rg -n "label\{([^}]*)\}" theorem-lanes.tex | sed 's/.*label{//; s/}.*//' | sort | uniq -d
git diff --check -- local-dictionary.tex theorem-lanes.tex
pdflatex -halt-on-error -interaction=nonstopmode -draftmode -output-directory=/tmp/topological-strings-agent149-build main.tex
```

Results:

- `git diff --check` passed.
- The reference-label scan found every cited label used by the new theorem
  lane.
- The duplicate-label scan returned no hits.
- The `/tmp` draft `pdflatex` pass exited with status 0.  It reports
  pre-existing underfull/overfull box warnings elsewhere, including
  `tate-T1-weighted-completion.tex` and `appendix-radial-parts-moyal.tex`.
  The first draft pass exposed overfull boxes in the new displays; those
  displays were split and the final draft pass no longer reports new
  overfulls in `local-dictionary.tex` or the new theorem-lane block.

## Files Changed / Staged

Changed by Agent 149:

- `local-dictionary.tex`
- `theorem-lanes.tex`
- `reconstitution/swarm-2026-04-30-agent-149-local-chiral-algebra-taxonomy.md`

Staged by Agent 149: none.  The two TeX files already had staged swarm
changes on entry; Agent 149 left this pass unstaged to avoid staging other
agents' deltas.

## Remaining Theorem Obligations

- Prove a genuine complex-line or holomorphic-defect restriction theorem
  before asserting any one-dimensional vertex algebra or OPE-mode object.
- Keep compact-CY chiral homology, CoHA, quintic/GV/OSV, Abel--Jacobi,
  Igusa, Borcherds, and BKM material outside the core local theorem unless
  a matched-conventions theorem is written.
- The non-scalar Costello graph/QME construction, finite-window
  counterterms, and all-\(N\) radial trace primitive remain exactly the
  obligations recorded by Agents 140--146.
