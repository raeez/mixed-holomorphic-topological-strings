# Agent 165 Curved Bulk-Defect Centrality Homotopy

Status: repaired the owned appendix surface.  The stable core is
conditional and local: strict zero homotopies exist in the algebraic
coefficient-current target and in the minimal full-equivariant marked
finite-window habitat.  The general unreduced Costello local-functional
centrality homotopy is not constructed by the existing data.

## Valid Attacks

```yaml
id: A1-165-01
severity: 1
status: healed
lens: coefficient-current versus Costello target
target: unreduced centrality homotopy claim
claim: The coefficient-current kernel already witnesses unreduced closed-open centrality.
broken_step: The coefficient-current kernel has strict zero defects only in the freely adjoined current algebra; it is not a local-functional graph kernel in the unreduced open BV target.
evidence_type: proof_gap
evidence_ref: thm:app-algebraic-factorization-centre-zero-homotopies; prop:app-bulk-defect-kernel-layer; thm:app-curved-kernel-centrality-homotopy-criterion
minimal_heal: State the binary curvature/homotopy criterion and record zero homotopies only in the coefficient-current habitat.
residual: Supply graph rows and primitives in the unreduced Costello target.
```

```yaml
id: A1-165-02
severity: 1
status: healed
lens: marked-graph scalar shadow
target: minimal full-equivariant marked graph package
claim: Scalar-shadow vanishing alone supplies the unreduced centrality homotopy.
broken_step: Scalar gate zero only places the row in the non-scalar kernel; a primitive row and transition coefficients are still required.
evidence_type: proof_gap
evidence_ref: def:app-nonscalar-kernel-row-complex; prop:app-marked-row-centrality-homotopy-test
minimal_heal: Add the marked-row test with the exact row formula, scalar gate, and primitive equation.
residual: Larger packages must supply actual graph/source/bracket/counterterm rows.
```

```yaml
id: A1-165-03
severity: 2
status: healed
lens: arbitrary current labels
target: D'_c defect labels in graph kernels
claim: Compactly supported distributional labels automatically enter the graph-level centrality homotopy.
broken_step: Arbitrary D'_c labels still lack wavefront transversality, diagonal extension, and compatible counterterm data.
evidence_type: counterexample
evidence_ref: prop:app-current-compatible-Dprimec-theorem-surface; reports 108, 142, 154
minimal_heal: Keep the general D'_c graph theorem outside the stable core; allow only regular-density or graphwise wavefront-admissible labels.
residual: New renormalization rules for failed distributional products.
```

```yaml
id: A1-165-04
severity: 2
status: healed
lens: minimal branch scope
target: minimal full-equivariant all-order vanishing
claim: The minimal all-order zero theorem proves the centrality homotopy for every unreduced graph/counterterm habitat.
broken_step: The theorem assumes no additional positive-order seed graph, CE-source face, graph counterterm face, or nonzero scalar-zero row.
evidence_type: line_reference
evidence_ref: thm:app-minimal-full-equivariant-all-order-vanishing; prop:app-first-order-three-larger-package-datum; prop:app-marked-row-centrality-homotopy-test
minimal_heal: State \(R^{\mathrm{cent}}_{x,y,M}=0\), \(H^M_{x,y}=0\) only inside the minimal finite marked habitat.
residual: Any enlarged package must be populated row by row.
```

## Repaired Labels

- Added `thm:app-curved-kernel-centrality-homotopy-criterion` in `appendix-factorization-current-conventions.tex`.
- Added `eq:app-centrality-homotopy-equation`.
- Added `prop:app-marked-row-centrality-homotopy-test` in `appendix-unreduced-bv-qme.tex`.

## Exact Formulas

Binary curvature component:
\[
  \mathfrak D^M_\kappa(x,y)
  =
  \operatorname{Curv}_{\mathbf K,M}(\kappa_M)(x\wedge y).
\]

Centrality homotopy equation:
\[
  \mathfrak D^M_\kappa(x,y)+d_MH^M_{x,y}=0.
\]

Marked finite-window row:
\[
\begin{aligned}
  R^{\mathrm{cent}}_{x,y,M}
    ={}&
    \sum_{\Gamma\in\mathsf A_{x,y,M}^{d}}
      \varepsilon_\Gamma\,d_M K^M_\Gamma
    -\sum_{\Gamma\in\mathsf A_{x,y,M}^{\mathrm{CE}}}
      \varepsilon^{\mathrm{CE}}_\Gamma
      K^M_\Gamma(\zeta_{\Gamma,x,y}) \\
    &\quad
    +\frac12
    \sum_{(\Gamma_1,\Gamma_2)\in
      \mathsf A_{x,y,M}^{\mathrm{br}}}
      \varepsilon_{\Gamma_1,\Gamma_2}
      \{K^M_{\Gamma_1},K^M_{\Gamma_2}\}_{\hbar,M}
    +R^{\mathrm{ct}}_{x,y,M}.
\end{aligned}
\]

Scalar gate and obstruction:
\[
  S^{\mathrm{cent}}_{x,y,M}
  =
  \widehat\sigma_{\mathrm{sc},M}
  (R^{\mathrm{cent}}_{x,y,M}),\qquad
  \mathfrak o^{\mathrm{cent}}_{x,y,M}
  =
  [R^{\mathrm{cent}}_{x,y,M}].
\]

Minimal full-equivariant branch:
\[
  R^{\mathrm{cent}}_{x,y,M}=0,\qquad H^M_{x,y}=0.
\]

## Files Changed / Staged

Changed:

- `appendix-factorization-current-conventions.tex`
- `appendix-unreduced-bv-qme.tex`
- `reconstitution/swarm-2026-04-30-agent-165-curved-bulk-defect-centrality-homotopy.md`

Staged:

- none.  The shared checkout already has concurrent edits in the owned
  appendix files, so staging whole files would also stage work outside
  this agent's authorship.

## Verification

Commands run:

```bash
git diff --check -- appendix-factorization-current-conventions.tex appendix-unreduced-bv-qme.tex reconstitution/swarm-2026-04-30-agent-165-curved-bulk-defect-centrality-homotopy.md
grep -n '[[:blank:]]$' appendix-factorization-current-conventions.tex appendix-unreduced-bv-qme.tex reconstitution/swarm-2026-04-30-agent-165-curved-bulk-defect-centrality-homotopy.md
rg -n "label\\{([^}]*)\\}" appendix-factorization-current-conventions.tex appendix-unreduced-bv-qme.tex | sed 's/.*label{//; s/}.*//' | sort | uniq -d
rg -n "app-curved-kernel-centrality-homotopy-criterion|app-marked-row-centrality-homotopy-test|eq:app-centrality-homotopy-equation|compact Calabi|CoHA|quintic|OSV|GV|Abel|Igusa|BKM" appendix-factorization-current-conventions.tex appendix-unreduced-bv-qme.tex reconstitution/swarm-2026-04-30-agent-165-curved-bulk-defect-centrality-homotopy.md
chktex -q appendix-factorization-current-conventions.tex
chktex -q appendix-unreduced-bv-qme.tex
lacheck appendix-factorization-current-conventions.tex
lacheck appendix-unreduced-bv-qme.tex
```

Results:

- `git diff --check` passed.
- trailing-whitespace grep returned no hits.
- duplicate-label scan returned no hits.
- firewall scan found only explicit local-quarantine language and the new labels.
- `chktex` returned the existing appendix warning class.  A filtered scan
  on the new centrality lines shows only the standard label-placement
  warning already present throughout these appendices.
- `lacheck` returned the existing appendix warning class; filtered scans
  on the new centrality lines returned no hits after the displayed
  punctuation repair.

No full `make pdf` was run.  The shared checkout has many concurrent
staged edits and tracked build output outside this agent's writable
surface.

## Remaining Theorem Obligations

- For a general unreduced Costello local-functional target, supply the
  actual finite-window graph row \(R^{\mathrm{cent}}_{x,y,M}\), its scalar
  gate, and a compatible primitive \(H^M_{x,y}\).
- For arbitrary \(\mathcal D'_c(I)\) labels, prove a wavefront,
  small-diagonal extension, and counterterm theorem, or keep the graph
  layer restricted to regular-density and graphwise wavefront-admissible
  tuples.
- For enlarged marked packages, supply every target-differential,
  CE-source, convolution-bracket, and counterterm row with signs,
  marker transport, scalar projection, and truncation coefficients.
- Kill the inverse-limit \(H^1\) class and the corresponding
  \(\varprojlim^1H^0\) primitive-compatibility class before claiming a
  global unreduced centrality homotopy.
